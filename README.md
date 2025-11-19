# LangExtract Content Generator v2

🚀 AI 기반 콘텐츠 추출 및 분석 웹 애플리케이션

Google Gemini AI를 활용하여 텍스트에서 다양한 정보를 자동으로 추출하는 강력한 도구입니다.

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
- 💾 JSON, HTML, CSV 내보내기
- 🌐 한국어 UI
- 📱 반응형 디자인
- 🔒 API 키 보안 관리

## 🚀 빠른 시작

### 1. 저장소 클론

```bash
git clone https://github.com/Reasonofmoon/langextract-v2.git
cd langextract-v2
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. API 키 설정

`.env` 파일을 생성하고 Gemini API 키를 추가하세요:

```bash
LANGEXTRACT_API_KEY=your-api-key-here
```

[Google AI Studio](https://aistudio.google.com/app/apikey)에서 무료 API 키를 발급받을 수 있습니다.

### 4. 애플리케이션 실행

```bash
cd apps/web_apps/content_generator
python app.py
```

브라우저에서 `http://localhost:5001`로 접속하세요!

## 📖 사용 방법

### 기본 사용법

1. **템플릿 선택**: 5가지 템플릿 중 하나를 선택하거나 커스텀 설정
2. **텍스트 입력**: 분석할 텍스트를 입력
3. **추출 지시사항**: 원하는 정보 추출 방법을 설명
4. **콘텐츠 추출**: 버튼 클릭으로 AI 분석 시작
5. **결과 확인**: 추출된 정보를 확인하고 내보내기

### 고급 설정

- **API 키**: 환경변수 또는 직접 입력
- **모델 선택**: Gemini 2.0 Flash (추천), 2.5 Pro 등
- **커스텀 프롬프트**: 자유롭게 추출 규칙 정의

## 🛠️ 기술 스택

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI**: Google Gemini API (langextract 라이브러리)
- **Styling**: 커스텀 CSS (그라디언트, 애니메이션)

## 📁 프로젝트 구조

```
langextract-v2/
├── apps/
│   └── web_apps/
│       └── content_generator/
│           ├── app.py              # Flask 백엔드
│           ├── templates/
│           │   └── index.html      # 프론트엔드 UI
│           ├── requirements.txt    # Python 의존성
│           └── README.md          # 앱 문서
├── .env                           # API 키 설정
├── .gitignore                     # Git 제외 파일
└── README.md                      # 프로젝트 문서
```

## 🌟 예제

### 문학 분석 예제

**입력 텍스트:**
```
해가 지평선 너머로 지고 있었고, 하늘을 화려한 주황색과 분홍색으로 물들이고 있었다. 
사라는 하루가 끝나가는 것을 바라보며 평화로운 느낌이 밀려오는 것을 느꼈다.
```

**추출 결과:**
- **등장인물**: 사라 (감정 상태: 평화로움)
- **감정**: 평화로운 느낌 (강도: 중간)
- **이미지**: 해가 지는 장면 (문학적 기법: 시각적 묘사)

## 🔧 개발 및 기여

### 로컬 개발

```bash
# 개발 모드로 실행
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
