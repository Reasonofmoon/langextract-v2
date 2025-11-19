# LangExtract Content Generator v2

🚀 AI 기반 콘텐츠 추출 및 분석 웹 애플리케이션

Google Gemini AI를 활용하여 텍스트에서 다양한 정보를 자동으로 추출하는 강력한 도구입니다.

## 🌐 온라인 데모

**바로 사용하기**: https://reasonofmoon.github.io/langextract-v2/

API 키만 입력하면 바로 사용할 수 있습니다! 설치 불필요.

## ✨ 주요 기능

### 📝 5가지 분석 템플릿
- **📚 문학 분석**: 등장인물, 감정, 이미지, 은유, 배경 추출
- **🎓 교육 분석**: 과목, 학습 방법, 난이도, 핵심 개념 파악
- **💭 감정 분석**: 긍정/부정 감정, 강도, 의견 분석
- **🏷️ 개체명 인식**: 인명, 조직명, 지명, 날짜, 제품명 추출
- **✨ 커스텀**: 자유롭게 설정 가능

### 🎯 핵심 기능
- ⚡ 최신 Gemini 2.0/2.5 모델 지원
- 📊 실시간 통계 및 시각화
- 💾 JSON, TXT 내보내기 및 클립보드 복사
- 🌐 한국어 UI
- 📱 반응형 디자인
- 🔒 브라우저에서 직접 실행 (API 키 안전)
- 🚀 백엔드 불필요 - 순수 클라이언트 사이드

## 🚀 사용 방법

### 온라인 버전 (추천)

1. https://reasonofmoon.github.io/langextract-v2/ 접속
2. [Google AI Studio](https://aistudio.google.com/app/apikey)에서 무료 API 키 발급
3. API 키 입력 후 바로 사용!

### 로컬 실행 (Flask 버전)

```bash
# 1. 저장소 클론
git clone https://github.com/Reasonofmoon/langextract-v2.git
cd langextract-v2

# 2. 의존성 설치
pip install -r requirements.txt

# 3. API 키 설정
echo "LANGEXTRACT_API_KEY=your-api-key-here" > .env

# 4. 실행
python app.py
```

브라우저에서 `http://localhost:5001`로 접속

## 📖 사용 예제

### 문학 분석

**입력 텍스트:**
```
해가 지평선 너머로 지고 있었고, 하늘을 화려한 주황색과 분홍색으로 물들이고 있었다. 
사라는 하루가 끝나가는 것을 바라보며 평화로운 느낌이 밀려오는 것을 느꼈다.
```

**추출 결과:**
- **등장인물**: 사라 (감정 상태: 평화로움)
- **감정**: 평화로운 느낌 (강도: 중간)
- **이미지**: 해가 지는 장면 (문학적 기법: 시각적 묘사)

### 개체명 인식

**입력 텍스트:**
```
삼성전자는 2024년 1월 서울에서 새로운 갤럭시 스마트폰을 공개했습니다.
```

**추출 결과:**
- **조직명**: 삼성전자 (타입: ORGANIZATION)
- **날짜**: 2024년 1월 (타입: DATE)
- **지명**: 서울 (타입: LOCATION)
- **제품명**: 갤럭시 스마트폰 (타입: PRODUCT)

## 🛠️ 기술 스택

### 온라인 버전
- **Frontend**: HTML5, CSS3, JavaScript (ES6 Modules)
- **AI**: Google Gemini API (직접 호출)
- **호스팅**: GitHub Pages

### Flask 버전
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: Google Gemini API (langextract 라이브러리)

## 📁 프로젝트 구조

```
langextract-v2/
├── index.html              # 온라인 버전 (GitHub Pages)
├── app.py                  # Flask 백엔드
├── templates/
│   └── index.html         # Flask 프론트엔드
├── requirements.txt       # Python 의존성
├── .env.example          # 환경변수 템플릿
├── .gitignore            # Git 제외 파일
└── README.md             # 프로젝트 문서
```

## 🌟 특징

### 온라인 버전의 장점
- ✅ 설치 불필요
- ✅ 어디서나 접속 가능
- ✅ API 키가 브라우저에만 저장됨 (서버 전송 안 함)
- ✅ 빠른 로딩
- ✅ 무료 호스팅

### Flask 버전의 장점
- ✅ 더 많은 커스터마이징 가능
- ✅ 백엔드 로직 추가 가능
- ✅ 데이터베이스 연동 가능
- ✅ 배치 처리 지원

## 🔒 보안

- API 키는 브라우저 메모리에만 저장됩니다
- 서버로 API 키가 전송되지 않습니다 (온라인 버전)
- HTTPS를 통한 안전한 통신
- `.env` 파일은 Git에서 제외됩니다

## 🔧 개발 및 기여

### 로컬 개발

```bash
# 온라인 버전 테스트
# index.html을 브라우저에서 직접 열기

# Flask 버전 개발
python app.py  # Debug mode 활성화
```

### 기여 방법

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 Apache 2.0 라이선스를 따릅니다.

## 🙏 감사의 말

- [LangExtract](https://github.com/google-deepmind/langextract) - Google DeepMind의 강력한 추출 라이브러리
- [Google Gemini](https://ai.google.dev/) - 최첨단 AI 모델

## 📧 문의

문제가 있거나 제안사항이 있으시면 [Issues](https://github.com/Reasonofmoon/langextract-v2/issues)에 등록해주세요.

---

Made with ❤️ using LangExtract and Gemini AI
