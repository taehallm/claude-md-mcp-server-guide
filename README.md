# CLAUDE.md 작성 가이드 & MCP 서버 예제

Claude Code 사용자들이 자신의 프로젝트에 맞는 **CLAUDE.md 파일을 작성**할 수 있도록 도와주는 가이드와 **FastMCP 기반 MCP 서버 개발 예제**를 포함합니다.

> 🎯 **초보 개발자도 1주 안에 PoC를 만들 수 있도록** 실용적인 내용에 집중했습니다.

## 📚 포함된 내용

### 1. CLAUDE.md 작성 가이드
- **[CLAUDE-CUSTOMIZATION-GUIDE.md](CLAUDE-CUSTOMIZATION-GUIDE.md)** - 다양한 프로젝트 유형에 맞는 CLAUDE.md 작성법
- **[CLAUDE-KO.md](CLAUDE-KO.md)** - MCP 서버 개발용 한국어 CLAUDE.md 예제
- **[CLAUDE.md](CLAUDE.md)** - MCP 서버 개발용 영어 CLAUDE.md 예제

### 2. MCP 서버 예제
FastMCP를 사용한 간단한 MCP (Model Context Protocol) 서버 구현 예제

**기능:**
- 계산기 도구 (덧셈, 곱셈)
- 텍스트 유틸리티 (단어 수 세기, 텍스트 뒤집기)
- 시스템 정보 리소스
- 서버 상태 리소스

## 🚀 빠른 시작

### MCP 서버 실행
```bash
# 의존성 설치
uv add "mcp[cli]"

# 개발 모드로 서버 실행 (MCP Inspector UI)
uv run mcp dev server.py

# 서버 직접 실행
uv run mcp run server.py
```

### 프로젝트 구조
```
├── server.py                           # MCP 서버 메인 파일
├── src/                               # 서버 구현 모듈
│   ├── tools/                        # MCP 도구들
│   │   ├── calculator.py            # 계산기 도구
│   │   └── text_utils.py            # 텍스트 유틸리티
│   └── resources/                   # MCP 리소스들
│       └── system_info.py          # 시스템 정보 리소스
├── CLAUDE.md                        # 영어 개발 가이드
├── CLAUDE-KO.md                     # 한국어 개발 가이드
├── CLAUDE-CUSTOMIZATION-GUIDE.md    # CLAUDE.md 작성 가이드
└── pyproject.toml                   # 프로젝트 설정
```

## 📖 사용법

### 1. CLAUDE.md 작성하기
자신의 프로젝트에 맞는 CLAUDE.md를 작성하려면:

1. **[CLAUDE-CUSTOMIZATION-GUIDE.md](CLAUDE-CUSTOMIZATION-GUIDE.md)** 읽기
2. 프로젝트 유형에 맞는 섹션 찾기 (LangGraph, FastAPI+LangChain, 풀스택 등)
3. 단계별 가이드를 따라 CLAUDE.md 작성
4. 우선순위에 따라 필수 내용부터 추가

### 2. MCP 서버 개발하기
이 예제를 참고하여 자신만의 MCP 서버를 개발할 수 있습니다:

1. `CLAUDE.md` 또는 `CLAUDE-KO.md` 참고
2. `src/tools/`에 새로운 도구 추가
3. `src/resources/`에 새로운 리소스 추가
4. `server.py`에서 도구/리소스 등록

## 🎯 대상 사용자

- **초보 개발자**: 1주 안에 PoC를 만들고 싶은 사람들
- **Claude Code 사용자**: 프로젝트에 맞는 CLAUDE.md를 작성하고 싶은 사람들
- **MCP 서버 개발자**: FastMCP로 MCP 서버를 만들고 싶은 사람들

## 🔧 요구사항

- Python 3.10+
- UV 패키지 매니저
- MCP CLI (`uv add "mcp[cli]"`)

## 📝 라이선스

MIT License

## 🤝 기여하기

이슈나 PR을 통해 개선사항을 제안해주세요!

## 🌟 이 저장소의 특징

- **실용적**: 이론보다는 바로 적용할 수 있는 실용적인 내용
- **초보자 친화적**: 복잡한 설정 없이 기본적인 내용부터 시작
- **한국어 지원**: 한국 개발자들을 위한 친절한 한국어 가이드
- **실제 예제**: 동작하는 MCP 서버 코드 포함

## 📚 관련 링크

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Code 문서](https://docs.anthropic.com/en/docs/claude-code)
- [FastMCP 문서](https://github.com/modelcontextprotocol/python-sdk)