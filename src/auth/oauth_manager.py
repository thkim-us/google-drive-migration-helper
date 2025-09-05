"""
Google OAuth 2.0 인증 관리자
"""

import os
import json
from typing import Optional, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from ..config.constants import GOOGLE_DRIVE_SCOPE, GOOGLE_DRIVE_API_VERSION
from ..config.settings import settings


class OAuthManager:
    """Google OAuth 2.0 인증을 관리하는 클래스"""
    
    def __init__(self, credentials_file: Optional[str] = None, token_file: Optional[str] = None):
        """
        OAuthManager 초기화
        
        Args:
            credentials_file: Google API 인증 파일 경로
            token_file: 토큰 저장 파일 경로
        """
        self.credentials_file = credentials_file or str(settings.get_google_credentials_path())
        self.token_file = token_file or str(settings.get_google_token_path())
        self.credentials: Optional[Credentials] = None
        self.service = None
    
    def authenticate(self) -> bool:
        """
        Google 계정 인증 수행
        
        Returns:
            bool: 인증 성공 여부
        """
        try:
            # 기존 토큰 로드
            if os.path.exists(self.token_file):
                self.credentials = Credentials.from_authorized_user_file(
                    self.token_file, GOOGLE_DRIVE_SCOPE
                )
            
            # 토큰이 없거나 유효하지 않은 경우 새로 인증
            if not self.credentials or not self.credentials.valid:
                if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                    # 토큰 갱신
                    self.credentials.refresh(Request())
                else:
                    # 새 인증 플로우 시작
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_file, GOOGLE_DRIVE_SCOPE
                    )
                    self.credentials = flow.run_local_server(port=0)
                
                # 토큰 저장
                self._save_token()
            
            # Google Drive API 서비스 생성
            self.service = build('drive', GOOGLE_DRIVE_API_VERSION, credentials=self.credentials)
            return True
            
        except Exception as e:
            print(f"인증 중 오류 발생: {e}")
            return False
    
    def _save_token(self):
        """토큰을 파일에 저장"""
        try:
            with open(self.token_file, 'w') as token:
                token.write(self.credentials.to_json())
        except Exception as e:
            print(f"토큰 저장 중 오류 발생: {e}")
    
    def get_service(self):
        """Google Drive API 서비스 반환"""
        if not self.service:
            raise Exception("먼저 authenticate()를 호출해주세요.")
        return self.service
    
    def get_user_info(self) -> Optional[Dict[str, Any]]:
        """현재 인증된 사용자 정보 반환"""
        if not self.service:
            return None
        
        try:
            about = self.service.about().get(fields="user").execute()
            return about.get('user', {})
        except Exception as e:
            print(f"사용자 정보 조회 중 오류 발생: {e}")
            return None
    
    def revoke_credentials(self):
        """인증 정보 취소"""
        if self.credentials:
            try:
                self.credentials.revoke(Request())
            except Exception as e:
                print(f"인증 정보 취소 중 오류 발생: {e}")
        
        # 토큰 파일 삭제
        if os.path.exists(self.token_file):
            try:
                os.remove(self.token_file)
            except Exception as e:
                print(f"토큰 파일 삭제 중 오류 발생: {e}")
        
        self.credentials = None
        self.service = None


class MultiAccountOAuthManager:
    """다중 계정 OAuth 인증 관리자"""
    
    def __init__(self):
        self.managers: Dict[str, OAuthManager] = {}
    
    def add_account(self, account_name: str, credentials_file: str, token_file: str) -> OAuthManager:
        """
        계정 추가
        
        Args:
            account_name: 계정 이름 (예: 'personal', 'work')
            credentials_file: 인증 파일 경로
            token_file: 토큰 파일 경로
        
        Returns:
            OAuthManager: 생성된 OAuth 매니저
        """
        manager = OAuthManager(credentials_file, token_file)
        self.managers[account_name] = manager
        return manager
    
    def authenticate_account(self, account_name: str) -> bool:
        """특정 계정 인증"""
        if account_name not in self.managers:
            print(f"계정 '{account_name}'이 등록되지 않았습니다.")
            return False
        
        return self.managers[account_name].authenticate()
    
    def get_account_service(self, account_name: str):
        """특정 계정의 서비스 반환"""
        if account_name not in self.managers:
            raise Exception(f"계정 '{account_name}'이 등록되지 않았습니다.")
        
        return self.managers[account_name].get_service()
    
    def get_all_authenticated_accounts(self) -> Dict[str, Any]:
        """인증된 모든 계정 정보 반환"""
        authenticated_accounts = {}
        
        for account_name, manager in self.managers.items():
            if manager.service:
                user_info = manager.get_user_info()
                if user_info:
                    authenticated_accounts[account_name] = user_info
        
        return authenticated_accounts
