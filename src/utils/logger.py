"""
로깅 시스템
"""

import logging
import os
from pathlib import Path
from datetime import datetime

from ..config.settings import settings


def setup_logger(name: str = "google_drive_migration", level: str = None) -> logging.Logger:
    """
    로거 설정
    
    Args:
        name: 로거 이름
        level: 로그 레벨
    
    Returns:
        logging.Logger: 설정된 로거
    """
    # 로그 레벨 설정
    log_level = level or settings.LOG_LEVEL
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # 로거 생성
    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)
    
    # 이미 핸들러가 있으면 제거 (중복 방지)
    if logger.handlers:
        logger.handlers.clear()
    
    # 포맷터 설정
    formatter = logging.Formatter(settings.LOG_FORMAT)
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 파일 핸들러
    try:
        # 로그 디렉토리 생성
        settings.create_directories()
        
        file_handler = logging.FileHandler(settings.LOG_FILE, encoding='utf-8')
        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        logger.warning(f"파일 로깅 설정 실패: {e}")
    
    return logger


def get_logger(name: str = "google_drive_migration") -> logging.Logger:
    """
    기존 로거 반환 또는 새로 생성
    
    Args:
        name: 로거 이름
    
    Returns:
        logging.Logger: 로거 인스턴스
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name)
    return logger


class MigrationLogger:
    """마이그레이션 전용 로거"""
    
    def __init__(self, migration_id: str = None):
        self.migration_id = migration_id or f"migration_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.logger = get_logger(f"migration_{self.migration_id}")
    
    def info(self, message: str, **kwargs):
        """정보 로그"""
        self.logger.info(f"[{self.migration_id}] {message}", **kwargs)
    
    def warning(self, message: str, **kwargs):
        """경고 로그"""
        self.logger.warning(f"[{self.migration_id}] {message}", **kwargs)
    
    def error(self, message: str, **kwargs):
        """오류 로그"""
        self.logger.error(f"[{self.migration_id}] {message}", **kwargs)
    
    def debug(self, message: str, **kwargs):
        """디버그 로그"""
        self.logger.debug(f"[{self.migration_id}] {message}", **kwargs)
