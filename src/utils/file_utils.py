"""
파일 처리 유틸리티 함수들
"""

import os
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..config.constants import MAX_FILE_SIZE, SUPPORTED_FILE_TYPES


def format_file_size(size_bytes: int) -> str:
    """
    파일 크기를 읽기 쉬운 형태로 변환
    
    Args:
        size_bytes: 바이트 단위 파일 크기
    
    Returns:
        str: 포맷된 파일 크기 문자열
    """
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"


def calculate_file_hash(file_path: str, algorithm: str = 'md5') -> str:
    """
    파일의 해시값 계산
    
    Args:
        file_path: 파일 경로
        algorithm: 해시 알고리즘 ('md5', 'sha1', 'sha256')
    
    Returns:
        str: 파일 해시값
    """
    hash_func = hashlib.new(algorithm)
    
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        raise Exception(f"파일 해시 계산 중 오류 발생: {e}")


def is_supported_file_type(mime_type: str) -> bool:
    """
    지원되는 파일 타입인지 확인
    
    Args:
        mime_type: MIME 타입
    
    Returns:
        bool: 지원 여부
    """
    return mime_type in SUPPORTED_FILE_TYPES


def is_file_size_valid(size: int) -> bool:
    """
    파일 크기가 유효한지 확인
    
    Args:
        size: 파일 크기 (바이트)
    
    Returns:
        bool: 유효 여부
    """
    return 0 < size <= MAX_FILE_SIZE


def sanitize_filename(filename: str) -> str:
    """
    파일명에서 특수문자 제거 및 정리
    
    Args:
        filename: 원본 파일명
    
    Returns:
        str: 정리된 파일명
    """
    # Windows에서 사용할 수 없는 문자들
    invalid_chars = '<>:"/\\|?*'
    
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # 연속된 언더스코어 제거
    while '__' in filename:
        filename = filename.replace('__', '_')
    
    # 앞뒤 공백 및 점 제거
    filename = filename.strip(' .')
    
    # 빈 파일명 처리
    if not filename:
        filename = 'unnamed_file'
    
    return filename


def create_safe_filename(filename: str, max_length: int = 255) -> str:
    """
    안전한 파일명 생성 (길이 제한 포함)
    
    Args:
        filename: 원본 파일명
        max_length: 최대 길이
    
    Returns:
        str: 안전한 파일명
    """
    # 파일명 정리
    safe_name = sanitize_filename(filename)
    
    # 길이 제한
    if len(safe_name) > max_length:
        name, ext = os.path.splitext(safe_name)
        max_name_length = max_length - len(ext)
        safe_name = name[:max_name_length] + ext
    
    return safe_name


def get_file_metadata(file_path: str) -> Dict[str, Any]:
    """
    파일 메타데이터 추출
    
    Args:
        file_path: 파일 경로
    
    Returns:
        Dict[str, Any]: 파일 메타데이터
    """
    try:
        path = Path(file_path)
        stat = path.stat()
        
        return {
            'name': path.name,
            'size': stat.st_size,
            'created_time': datetime.fromtimestamp(stat.st_ctime),
            'modified_time': datetime.fromtimestamp(stat.st_mtime),
            'is_file': path.is_file(),
            'is_dir': path.is_dir(),
            'extension': path.suffix.lower(),
            'parent_dir': str(path.parent)
        }
    except Exception as e:
        raise Exception(f"파일 메타데이터 추출 중 오류 발생: {e}")


def ensure_directory_exists(directory_path: str) -> bool:
    """
    디렉토리가 존재하는지 확인하고 없으면 생성
    
    Args:
        directory_path: 디렉토리 경로
    
    Returns:
        bool: 성공 여부
    """
    try:
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"디렉토리 생성 중 오류 발생: {e}")
        return False


def get_directory_size(directory_path: str) -> int:
    """
    디렉토리 전체 크기 계산
    
    Args:
        directory_path: 디렉토리 경로
    
    Returns:
        int: 총 크기 (바이트)
    """
    total_size = 0
    
    try:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    # 접근할 수 없는 파일은 건너뛰기
                    continue
    except Exception as e:
        print(f"디렉토리 크기 계산 중 오류 발생: {e}")
    
    return total_size


def find_files_by_extension(directory_path: str, extensions: List[str]) -> List[str]:
    """
    특정 확장자를 가진 파일들 찾기
    
    Args:
        directory_path: 검색할 디렉토리
        extensions: 확장자 리스트 (예: ['.txt', '.pdf'])
    
    Returns:
        List[str]: 찾은 파일 경로 리스트
    """
    found_files = []
    
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if any(file.lower().endswith(ext.lower()) for ext in extensions):
                    found_files.append(os.path.join(root, file))
    except Exception as e:
        print(f"파일 검색 중 오류 발생: {e}")
    
    return found_files
