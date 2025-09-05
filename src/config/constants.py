"""
Google Drive Migration Helper - 상수 정의
"""

# Google Drive API 관련 상수
GOOGLE_DRIVE_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.metadata',
    'https://www.googleapis.com/auth/drive.readonly'
]

# API 버전
GOOGLE_DRIVE_API_VERSION = 'v3'

# 파일 크기 제한 (바이트)
MAX_FILE_SIZE = 5 * 1024 * 1024 * 1024  # 5GB

# 배치 처리 크기
BATCH_SIZE = 100

# 재시도 설정
MAX_RETRIES = 3
RETRY_DELAY = 1  # 초

# 지원되는 파일 타입
SUPPORTED_FILE_TYPES = [
    'application/vnd.google-apps.document',
    'application/vnd.google-apps.spreadsheet',
    'application/vnd.google-apps.presentation',
    'application/vnd.google-apps.folder',
    'application/pdf',
    'image/jpeg',
    'image/png',
    'image/gif',
    'text/plain',
    'application/zip',
    'application/x-zip-compressed'
]

# 마이그레이션 상태
MIGRATION_STATUS = {
    'PENDING': 'pending',
    'IN_PROGRESS': 'in_progress',
    'COMPLETED': 'completed',
    'FAILED': 'failed',
    'CANCELLED': 'cancelled'
}

# 로그 레벨
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}
