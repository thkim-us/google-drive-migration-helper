"""
Google Drive Migration Helper - 설정 관리
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    """애플리케이션 설정 클래스"""
    
    # 기본 경로
    BASE_DIR = Path(__file__).parent.parent.parent
    SRC_DIR = BASE_DIR / "src"
    NOTEBOOKS_DIR = BASE_DIR / "notebooks"
    DOCS_DIR = BASE_DIR / "docs"
    TESTS_DIR = BASE_DIR / "tests"
    
    # 로그 설정
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE = BASE_DIR / "logs" / "migration.log"
    
    # Google API 설정
    GOOGLE_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
    GOOGLE_TOKEN_FILE = os.getenv('GOOGLE_TOKEN_FILE', 'token.json')
    
    # 마이그레이션 설정
    MAX_CONCURRENT_UPLOADS = int(os.getenv('MAX_CONCURRENT_UPLOADS', '5'))
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', '1024')) * 1024  # 1MB 기본값
    TIMEOUT = int(os.getenv('TIMEOUT', '300'))  # 5분 기본값
    
    # 임시 파일 설정
    TEMP_DIR = BASE_DIR / "temp"
    BACKUP_DIR = BASE_DIR / "backup"
    
    @classmethod
    def create_directories(cls):
        """필요한 디렉토리 생성"""
        directories = [
            cls.LOG_FILE.parent,
            cls.TEMP_DIR,
            cls.BACKUP_DIR
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_google_credentials_path(cls):
        """Google 인증 파일 경로 반환"""
        return cls.BASE_DIR / cls.GOOGLE_CREDENTIALS_FILE
    
    @classmethod
    def get_google_token_path(cls):
        """Google 토큰 파일 경로 반환"""
        return cls.BASE_DIR / cls.GOOGLE_TOKEN_FILE

# 전역 설정 인스턴스
settings = Settings()
