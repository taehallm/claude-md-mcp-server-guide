# CLAUDE-KO.md

이 파일은 Claude Code (claude.ai/code)가 이 저장소의 코드를 작업할 때 참고할 한국어 가이드입니다.

## 프로젝트 유형

이 프로젝트는 UV 패키지 매니저와 FastMCP 프레임워크를 사용하여 Python으로 구축된 MCP (Model Context Protocol) 서버 프로젝트입니다.

추가 문서와 예제는 공식 MCP Python SDK를 참고하세요: https://github.com/modelcontextprotocol/python-sdk

## 개발 환경 설정

### 필수 조건
- UV 패키지 매니저 (pip/conda 대체)
- Python 3.10+ (MCP 요구사항)

### 주요 개발 명령어
```bash
# 의존성 설치
uv add "mcp[cli]"

# 서버 직접 실행 (출력 없이 조용히 실행)
uv run mcp run server.py

# MCP Inspector UI와 함께 개발 모드로 서버 실행
uv run mcp dev server.py

# Claude Desktop에 서버 설치
uv run mcp install server.py

# 사용 가능한 MCP 명령어 목록
uv run mcp --help

# MCP 버전 확인
uv run mcp version

# 테스트 실행
uv run pytest

# 코드 포맷팅
uv run ruff format .

# 코드 린팅
uv run ruff check .
```

## MCP 서버 아키텍처

### 프로젝트 구조

#### 옵션 1: 단순 구조 (직접 데코레이터)
```
project/
├── server.py           # 모든 도구/리소스가 여기에 정의됨
├── pyproject.toml     # UV 프로젝트 설정
├── tests/             # 테스트 파일
└── README.md          # 서버 문서
```

#### 옵션 2: 모듈형 구조 (수동 등록) - 권장
```
project/
├── server.py           # 메인 MCP 서버 진입점
├── pyproject.toml     # UV 프로젝트 설정
├── src/               # 서버 구현 모듈들
│   ├── tools/         # MCP 도구 구현
│   ├── resources/     # MCP 리소스 구현
│   └── prompts/       # MCP 프롬프트 구현
├── tests/             # 테스트 파일
└── README.md          # 서버 문서
```

### FastMCP 개발 패턴

#### 서버 정의
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server-name")
# if __name__ == "__main__" 블록 불필요 - MCP CLI가 실행을 처리
```

#### 접근법 1: 직접 데코레이터 (단순/모놀리식)
모든 도구/리소스를 server.py에서 데코레이터로 정의:
```python
@mcp.tool()
def tool_name(param: str) -> dict:
    """이 도구가 무엇을 하는지 명확한 설명."""
    return {"result": "value"}

@mcp.resource("resource://name")
def resource_name() -> str:
    """리소스 설명."""
    return "resource content"
```

#### 접근법 2: 모듈형 + 수동 등록 (권장)
도구/리소스를 별도 모듈에 정의하고 server.py에서 등록:

**src/tools/example.py에서:**
```python
def tool_name(param: str) -> dict:
    """이 도구가 무엇을 하는지 명확한 설명."""
    return {"result": "value"}
```

**server.py에서:**
```python
from src.tools.example import tool_name
from src.resources.info import resource_name

# 도구와 리소스 등록
mcp.tool()(tool_name)
mcp.resource("resource://name")(resource_name)
```

#### 코드 구성 원칙
- IDE 지원과 유효성 검사를 위해 타입 힌트를 광범위하게 사용
- 모든 도구, 리소스, 프롬프트에 포괄적인 독스트링 제공
- 오류를 우아하게 처리하고 의미 있는 오류 메시지 반환
- 구조화된 데이터에는 Pydantic 모델이나 TypedDict 사용
- `if __name__ == "__main__":` 블록 포함하지 않음 - MCP CLI가 서버 실행 처리

**단순 구조의 경우:**
- 데코레이터를 사용하여 모든 도구/리소스를 server.py에 유지
- 도구가 적은 작은 서버에 적합

**모듈형 구조의 경우:**
- 관련 기능을 `src/` 아래 별도 모듈로 그룹화
- `mcp.tool()(function_name)`으로 가져와서 수동 등록
- 많은 도구/리소스가 있는 대규모 서버에 더 적합
- 테스트와 유지보수가 더 쉬움

## 개발 워크플로

### 서버 개발 사이클
1. 적절한 타입 힌트와 독스트링으로 도구/리소스/프롬프트 구현
2. 서버 직접 테스트: `uv run mcp run server.py` (조용히 실행)
3. MCP Inspector UI로 테스트: `uv run mcp dev server.py` (웹 인터페이스 열림)
4. 린팅과 포맷팅 실행: `uv run ruff check . && uv run ruff format .`
5. 테스트 실행: `uv run pytest`
6. Claude Desktop에 설치: `uv run mcp install server.py`

### MCP 서버 테스트

#### 자동화된 테스트 (Claude Code가 도울 수 있음):
- 개별 도구와 리소스에 대한 단위 테스트 작성
- 오류 처리와 엣지 케이스 테스트
- 구조화된 출력에 대한 JSON 스키마 유효성 검사
- `uv run pytest`로 테스트 실행

#### 수동/인터랙티브 테스트 (사용자가 직접 해야 함):
- `uv run mcp dev server.py`로 MCP Inspector 웹 UI 열기
- 브라우저 인터페이스에서 도구를 인터랙티브하게 테스트
- 실제 입력으로 도구/리소스 동작 확인
- 서버 기능과 메타데이터 확인

#### 참고사항:
- `uv run mcp run server.py`는 출력 없이 조용히 실행됨
- Claude Code는 자동화된 테스트를 작성할 수 있지만 MCP Inspector UI와 상호작용할 수 없음
- 개발 시에는 자동화된 테스트와 수동 Inspector 테스트를 모두 결합하여 사용

### 설정 관리
- FastMCP 생성자에서 서버 메타데이터 정의
- 민감한 설정에는 환경 변수 사용
- 리소스에 대한 적절한 비동기 컨텍스트 관리 구현
- 필요시 `asynccontextmanager`로 서버 라이프사이클 처리

### 모범 사례
- 도구 함수는 집중적이고 단일 목적으로 유지
- 기능을 명확하게 나타내는 설명적인 이름 사용
- 유익한 메시지와 함께 적절한 오류 처리 구현
- 입력 유효성 검사 및 출력 정리
- 독스트링에서 예상되는 입력/출력 형식 문서화