# Google Drive Migration Helper

## 프로젝트 개요

회사에서 GWS(Google Workspace) 도입에 따른 개인 Google 계정에서 회사 Google 계정으로의 대규모 파일 마이그레이션을 자동화하는 도구입니다.

## 배경 및 요구사항

### 현재 상황
- 회사에서 개인 Google 계정으로 협업 진행
- Google Drive를 통한 파일 공유가 주요 업무 방식
- GWS 유료 도입으로 인한 계정 전환 필요
- 마이그레이션 대상 인원: 100여명

### 핵심 요구사항
1. **대규모 자동화**: 100여명의 사용자를 위한 자동화된 마이그레이션
2. **사용자 중심 인증**: Google Colab을 통한 사용자 직접 인증 방식
3. **다중 계정 지원**: 개인 계정과 회사 계정 동시 인증
4. **배치 처리**: 한 번에 모든 사용자 처리 불가능한 상황 고려

## 기술 아키텍처

### 플랫폼: Google Colab
- **장점**:
  - Google API와의 완벽한 통합
  - 사용자가 직접 인증 가능
  - 클라우드 기반으로 안정적인 실행 환경
  - 무료 사용 가능

### 핵심 기술 스택
- **Python 3.x**
- **Google Drive API v3**
- **Google OAuth 2.0**
- **Google Colab Notebook**
- **Pandas** (진행 상황 추적)
- **Tqdm** (진행률 표시)

## 주요 기능

### 1. 계정 인증 및 권한 관리
- 개인 Google 계정 OAuth 인증
- 회사 Google 계정 OAuth 인증
- 필요한 권한 자동 요청 및 관리

### 2. 파일 스캔 및 분석
- 소스 계정의 모든 파일 및 폴더 구조 분석
- 파일 메타데이터 수집 (크기, 수정일, 공유 설정 등)
- 공유 권한 정보 추출

### 3. 마이그레이션 실행
- 폴더 구조 유지하며 파일 복사
- 공유 권한 재설정
- 파일 메타데이터 보존
- 중복 파일 처리

### 4. 진행 상황 추적
- 실시간 진행률 표시
- 오류 로그 및 재시도 메커니즘
- 마이그레이션 완료 보고서 생성

## 구현 계획

### Phase 1: 기본 인프라 구축 (1-2주)
- [ ] Google Colab Notebook 템플릿 생성
- [ ] Google Drive API 연동 설정
- [ ] OAuth 2.0 인증 플로우 구현
- [ ] 기본 파일 스캔 기능 개발

### Phase 2: 마이그레이션 엔진 개발 (2-3주)
- [ ] 파일 복사 및 폴더 구조 유지 로직
- [ ] 공유 권한 마이그레이션 기능
- [ ] 메타데이터 보존 기능
- [ ] 오류 처리 및 재시도 메커니즘

### Phase 3: 사용자 인터페이스 및 UX (1-2주)
- [ ] 직관적인 Colab 인터페이스 설계
- [ ] 진행률 표시 및 상태 모니터링
- [ ] 사용자 가이드 및 도움말
- [ ] 오류 메시지 및 해결 방법 안내

### Phase 4: 테스트 및 최적화 (1-2주)
- [ ] 소규모 테스트 (5-10명)
- [ ] 성능 최적화
- [ ] 대용량 파일 처리 개선
- [ ] 사용자 피드백 반영

### Phase 5: 배포 및 지원 (1주)
- [ ] 최종 사용자 가이드 작성
- [ ] 관리자 매뉴얼 작성
- [ ] 기술 지원 체계 구축

## 파일 구조

```
google-drive-migration-helper/
├── README.md
├── notebooks/
│   ├── migration_template.ipynb          # 메인 마이그레이션 노트북
│   ├── setup_and_test.ipynb             # 설정 및 테스트 노트북
│   └── batch_processing.ipynb           # 배치 처리 노트북
├── src/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── oauth_manager.py             # OAuth 인증 관리
│   │   └── credentials_handler.py       # 인증 정보 처리
│   ├── migration/
│   │   ├── __init__.py
│   │   ├── file_scanner.py              # 파일 스캔 및 분석
│   │   ├── migration_engine.py          # 마이그레이션 실행 엔진
│   │   ├── permission_manager.py        # 공유 권한 관리
│   │   └── progress_tracker.py          # 진행 상황 추적
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py                # 파일 유틸리티
│   │   ├── api_utils.py                 # Google API 유틸리티
│   │   └── logger.py                    # 로깅 시스템
│   └── config/
│       ├── __init__.py
│       ├── settings.py                  # 설정 관리
│       └── constants.py                 # 상수 정의
├── docs/
│   ├── user_guide.md                    # 사용자 가이드
│   ├── admin_guide.md                   # 관리자 가이드
│   └── troubleshooting.md               # 문제 해결 가이드
├── tests/
│   ├── test_auth.py
│   ├── test_migration.py
│   └── test_utils.py
└── requirements.txt
```

## 사용 시나리오

### 1. 개별 사용자 마이그레이션
1. 사용자가 Google Colab 노트북에 접속
2. 개인 계정과 회사 계정 인증
3. 마이그레이션 설정 (선택적 필터링)
4. 자동 마이그레이션 실행
5. 완료 보고서 확인

### 2. 관리자 배치 처리
1. 관리자가 사용자 목록 준비
2. 배치 처리 노트북 실행
3. 각 사용자별 진행 상황 모니터링
4. 전체 마이그레이션 현황 대시보드 확인

## 보안 고려사항

### 데이터 보호
- OAuth 2.0을 통한 안전한 인증
- 사용자 데이터는 사용자 브라우저에서만 처리
- 서버에 민감한 데이터 저장하지 않음

### 권한 관리
- 최소 권한 원칙 적용
- 필요한 Google Drive 권한만 요청
- 사용자 동의 하에 권한 부여

## 예상 이슈 및 해결 방안

### 1. API 할당량 제한
- **문제**: Google Drive API 일일 할당량 초과
- **해결**: 배치 처리 및 재시도 로직 구현

### 2. 대용량 파일 처리
- **문제**: 큰 파일의 업로드/다운로드 시간
- **해결**: 청크 단위 처리 및 진행률 표시

### 3. 공유 권한 복잡성
- **문제**: 다양한 공유 설정의 복잡한 마이그레이션
- **해결**: 권한 매핑 테이블 및 사용자 확인 절차

### 4. 네트워크 불안정성
- **문제**: 긴 마이그레이션 중 연결 끊김
- **해결**: 체크포인트 저장 및 재시작 기능

## 성공 지표

- [ ] 100% 사용자 마이그레이션 완료
- [ ] 파일 손실 0%
- [ ] 공유 권한 정확도 95% 이상
- [ ] 사용자 만족도 4.0/5.0 이상
- [ ] 평균 마이그레이션 시간 30분 이내

## 🚀 빠른 시작 (사용자용)

### 1. Google Colab에서 바로 시작
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[사용자명]/google-drive-migration-helper/blob/main/notebooks/migration_template.ipynb)

### 2. 사용 방법
1. 위 링크를 클릭하여 Google Colab에서 노트북 열기
2. "복사본 만들기" 클릭
3. 관리자로부터 받은 `credentials.json` 파일 업로드
4. 셀을 순서대로 실행하여 마이그레이션 진행

### 3. 자세한 가이드
- [사용자 가이드](docs/user_deployment_guide.md)
- [Google Cloud Console 설정](docs/google_cloud_setup.md)

## 📋 관리자용

### 배포 준비
- [관리자 배포 체크리스트](docs/admin_deployment_checklist.md)
- [Google Cloud Console 설정 가이드](docs/google_cloud_setup.md)

### 개발 및 테스트
```bash
# 가상환경 활성화
source .venv/bin/activate

# OAuth 인증 테스트
python demo_auth.py
```

## 📈 현재 진행 상황

### ✅ 완료된 작업
- **Phase 1**: 기본 인프라 구축 완료
  - Python 가상환경 설정 (`.venv`)
  - 프로젝트 구조 생성 (`src/`, `notebooks/`, `docs/`)
  - OAuth 인증 모듈 구현 (`src/auth/oauth_manager.py`)
  - Google Drive API 연동 코드 작성
  - Google Colab 마이그레이션 노트북 완성
  - 사용자/관리자 가이드 문서 작성

- **Google Cloud Console 설정**
  - GCP 프로젝트 생성 (`google-workspace`)
  - Google Drive API 활성화
  - OAuth 2.0 클라이언트 ID 생성
  - `credentials.json` 파일 준비 완료

### 🔄 다음 단계
1. **Google Colab 노트북 테스트** - OAuth 인증 및 파일 스캔 확인
2. **GitHub 배포** - 사용자들이 접근할 수 있도록 공개
3. **소규모 테스트** - 5-10명으로 파일 마이그레이션 테스트
4. **전체 배포** - 100여명 사용자 대상 마이그레이션 실행

---

**문의사항이나 개선 제안이 있으시면 이슈를 등록해 주세요.**
