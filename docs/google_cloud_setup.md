# Google Cloud Console 설정 가이드

Google Drive Migration Helper를 사용하기 위해 Google Cloud Console에서 OAuth 2.0 클라이언트 ID를 생성하는 방법을 안내합니다.

## 1. Google Cloud Console 접속

1. [Google Cloud Console](https://console.cloud.google.com/)에 접속합니다.
2. Google 계정으로 로그인합니다.

## 2. 프로젝트 생성 또는 선택

### 새 프로젝트 생성 (권장)
1. 상단의 프로젝트 선택 드롭다운을 클릭합니다.
2. "새 프로젝트"를 클릭합니다.
3. 프로젝트 이름을 입력합니다 (예: "drive-migration-helper")
4. "만들기"를 클릭합니다.

### 기존 프로젝트 사용
1. 상단의 프로젝트 선택 드롭다운에서 기존 프로젝트를 선택합니다.

## 3. Google Drive API 활성화

1. 왼쪽 메뉴에서 "API 및 서비스" > "라이브러리"를 클릭합니다.
2. 검색창에 "Google Drive API"를 입력합니다.
3. "Google Drive API"를 클릭합니다.
4. "사용" 버튼을 클릭합니다.

## 4. OAuth 2.0 클라이언트 ID 생성

1. 왼쪽 메뉴에서 "API 및 서비스" > "사용자 인증 정보"를 클릭합니다.
2. 상단의 "+ 사용자 인증 정보 만들기"를 클릭합니다.
3. "OAuth 2.0 클라이언트 ID"를 선택합니다.

### 애플리케이션 유형 설정
1. "애플리케이션 유형"에서 "데스크톱 애플리케이션"을 선택합니다.
2. "이름"에 "Drive Migration Helper"를 입력합니다.
3. "만들기"를 클릭합니다.

## 5. 클라이언트 ID 다운로드

1. 생성된 OAuth 2.0 클라이언트 ID 팝업에서 "JSON 다운로드"를 클릭합니다.
2. 다운로드된 JSON 파일의 이름을 `credentials.json`으로 변경합니다.
3. 이 파일을 프로젝트 루트 디렉토리에 복사합니다.

## 6. OAuth 동의 화면 설정 (선택사항)

대량의 사용자가 사용할 경우 OAuth 동의 화면을 설정해야 할 수 있습니다.

1. 왼쪽 메뉴에서 "API 및 서비스" > "OAuth 동의 화면"을 클릭합니다.
2. "외부"를 선택하고 "만들기"를 클릭합니다.
3. 필수 정보를 입력합니다:
   - 앱 이름: "Google Drive Migration Helper"
   - 사용자 지원 이메일: 본인의 이메일
   - 개발자 연락처 정보: 본인의 이메일
4. "저장 후 계속"을 클릭합니다.

## 7. 테스트 사용자 추가 (개발 중)

개발 중에는 테스트 사용자를 추가해야 할 수 있습니다.

1. "OAuth 동의 화면"에서 "테스트 사용자" 섹션을 찾습니다.
2. "사용자 추가"를 클릭합니다.
3. 마이그레이션에 참여할 사용자들의 이메일을 추가합니다.

## 8. 파일 구조 확인

프로젝트 루트 디렉토리에 다음 파일들이 있는지 확인합니다:

```
google-drive-migration-helper/
├── credentials.json          # ← 이 파일이 있어야 함
├── demo_auth.py
├── requirements.txt
└── src/
    └── ...
```

## 9. 테스트 실행

설정이 완료되면 다음 명령어로 테스트를 실행합니다:

```bash
# 가상환경 활성화
source .venv/bin/activate

# 데모 실행
python demo_auth.py
```

## 문제 해결

### "credentials.json 파일이 없습니다" 오류
- Google Cloud Console에서 JSON 파일을 다운로드했는지 확인
- 파일명이 정확히 `credentials.json`인지 확인
- 파일이 프로젝트 루트 디렉토리에 있는지 확인

### "OAuth 동의 화면이 구성되지 않았습니다" 오류
- OAuth 동의 화면 설정을 완료했는지 확인
- 테스트 사용자로 등록된 계정으로 로그인했는지 확인

### "API가 활성화되지 않았습니다" 오류
- Google Drive API가 활성화되었는지 확인
- 올바른 프로젝트를 선택했는지 확인

## 보안 주의사항

- `credentials.json` 파일은 절대 공개 저장소에 업로드하지 마세요
- `.gitignore` 파일에 `credentials.json`이 포함되어 있는지 확인하세요
- 프로덕션 환경에서는 서비스 계정 키를 사용하는 것을 고려하세요
