# 🎯 CLI Python 퀴즈 게임 (Quiz Game)

터미널 환경에서 작동하는 객체지향 기반의 Python 퀴즈 게임 프로젝트입니다.  
Python 기본 문법과 클래스 구조, JSON 기반 데이터 영속성 처리, 그리고 Git/GitHub을 활용한 버전 관리를 실습하기 위해 제작되었습니다.

---

## 📌 1. 프로젝트 개요

* **개발 언어:** Python 3.10+ (표준 라이브러리만 사용)
* **주요 기능:** 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 조회, 최고 점수 확인, 데이터 자동 저장 및 불러오기
* **데이터 관리:** `state.json` (UTF-8 인코딩)

---

## 💡 2. 퀴즈 주제 및 선정 이유

* **주제:** 파이썬 기초 프로그래밍 지식 (Python Fundamentals)
* **선정 이유:** 
  프로그래밍 언어를 학습할 때 가장 중요한 기초 개념(자료형, 제어문, 함수, 클래스 등)을 스스로 다지고, 퀴즈를 직접 출제·풀이하며 파이썬 문법 이해도를 높이기 위해 선정했습니다.

---

## 🚀 3. 실행 방법

 별도의 외부 라이브러리 설치가 필요 없습니다. 터미널에서 아래 명령어를 실행하세요.

```bash
# 저장소 복제
git clone [https://github.com/CodysseyAI2/E1_2](https://github.com/CodysseyAI2/E1_2)

# 프로젝트 디렉터리 이동
cd E1_2

# 프로그램 실행
python main.py

---

## 📋 4. 요구사항 구현 체크리스트

### 🎯 기능 요구사항 (Functional Requirements)

- [x] **퀴즈 풀기 (Quiz Play)**
  - [x] 기본 주제(파이썬 기초) 퀴즈 5개 이상 제공
  - [x] 각 문제별 질문 및 4개 선택지 출력
  - [x] 사용자 입력 답안(1~4번) 정답 여부 즉시 출력
  - [x] 모든 문제 풀이 완료 후 최종 점수 및 정답률 표시
  - [x] 최고 점수 경신 시 자동 반영 및 파일 업데이트
  - [x] 등록된 퀴즈가 없는 경우 예외 안내 문구 출력

- [x] **퀴즈 추가 (Add Quiz)**
  - [x] 문제(Question) 입력 받기
  - [x] 4개의 선택지(Choices) 순차적 입력 받기
  - [x] 정답 번호(1~4번) 입력 받기
  - [x] 신규 퀴즈 등록 성공 시 `state.json` 즉시 갱신

- [x] **퀴즈 목록 조회 (Quiz List)**
  - [x] 현재 등록되어 있는 전체 퀴즈 문제 출력
  - [x] 등록된 퀴즈가 0개일 때 안내 메시지 출력

- [x] **점수 확인 (Score Check)**
  - [x] 저장된 최고 점수 조회 및 출력
  - [x] 아직 게임을 플레이하지 않은 상태에 대한 처리

- [x] **데이터 영속성 (Data Persistence)**
  - [x] 프로젝트 루트의 `state.json` 파일 읽기/쓰기 구현
  - [x] UTF-8 인코딩 적용으로 한글 깨짐 방지
  - [x] 프로그램 종료 후 재실행 시에도 추가된 퀴즈 및 최고 점수 유지

---

### 🛡️ 비기능 요구사항 (Non-Functional Requirements)

- [x] **입력 검증 및 방어적 프로그래밍**
  - [x] 모든 입력값 앞뒤 공백 제거 (`strip()`)
  - [x] 숫자 변환 실패(문자 입력 등) 시 에러 안내 및 재입력 유도
  - [x] 허용 범위를 벗어난 숫자(예: 메뉴 9번, 정답 0번) 입력 시 재입력 유도
  - [x] 빈 입력(Enter만 누름) 시 재입력 유도

- [x] **예외 처리 및 견고성 (Robustness)**
  - [x] `Ctrl+C` (`KeyboardInterrupt`) 또는 `EOFError` 발생 시 비정상 종료 없이 안전하게 저장 후 종료
  - [x] `state.json` 파일이 없을 경우 기본 퀴즈 데이터 자동 생성
  - [x] `state.json` 파일이 손상되었거나 파싱 에러 발생 시 안내 후 기본 데이터로 자동 복구

---

### 🎁 보너스 과제 (선택 구현 사항)

- [x] **랜덤 출제:** `random.shuffle()`을 활용한 문제 출제 순서 무작위화
- [x] **문제 수 선택:** 퀴즈 시작 전 풀이할 문제 수 선택 기능
- [x] **힌트 기능:** `Quiz` 클래스 내 힌트 속성 추가 및 힌트 사용 시 점수 차감 로직
- [x] **퀴즈 삭제 기능:** 등록된 퀴즈 삭제 및 `state.json` 반영
- [x] **점수 히스토리:** 플레이 날짜/시간, 푼 문제 수, 점수 기록 누적 저장

### 메뉴 출력, 퀴즈 실행, 종료 흐름
```python
# quiz_game.py > run()
def run(self):
    while True:
        try:
            self.display_menu()
            choice = self.get_valid_input_int("선택: ", 1, 7)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                self.show_history()
            elif choice == 6:
                self.delete_quiz()
            elif choice == 7:
                self.save_state()
                print("👋 게임을 종료합니다. 이용해 주셔서 감사합니다!")
                break
        except (KeyboardInterrupt, EOFError):
            self.safe_exit()
```

### 정답 판정 및 입력 예외/범위 검증 스니펫
```python
# 1. 정답 판정 (quiz.py)
def is_correct(self, user_answer: int) -> bool:
    """사용자가 입력한 답안 번호와 정답 번호 일치 여부 판정"""
    return self.answer == user_answer

# 2. 정수 입력 검증 및 범위 제한 (quiz_game.py)
def get_valid_input_int(prompt: str, min_val: int, max_val: int) -> int:
    """정수 변환 예외(ValueError) 처리 및 최소/최대 범위 유효성 검증"""
    while True:
        try:
            user_input = input(prompt).strip()
            val = int(user_input)
            if min_val <= val <= max_val:
                return val
            print(f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
```

### 기본 퀴즈 5종 이상 정의 증빙
```python
# quiz_game.py > get_default_quizzes()
def get_default_quizzes(self) -> list[Quiz]:
    return [
        Quiz(question="Python에서 가변(Mutable) 객체는 무엇일까요?", choices=["tuple", "int", "list", "str"], answer=3, hint="수정 가능한 리스트입니다."),
        Quiz(question="리스트의 가장 끝에 요소를 추가하는 메서드는?", choices=["add()", "append()", "push()", "insert()"], answer=2, hint="'붙이다'라는 뜻입니다."),
        Quiz(question="다음 중 Python의 기본 데이터 타입이 아닌 것은?", choices=["dict", "set", "array", "bool"], answer=3, hint="array 대신 list를 기본으로 씁니다."),
        Quiz(question="조건문에서 조건이 거짓일 때 실행할 블록을 지정하는 키워드는?", choices=["else", "catch", "finally", "then"], answer=1, hint="if의 반대 조건 블록입니다."),
        Quiz(question="키-값(Key-Value) 쌍으로 데이터를 저장하는 자료형은?", choices=["list", "tuple", "dict", "set"], answer=3, hint="사전(Dictionary)의 약자입니다.")
    ] # 정확히 5개 기본 데이터 인스턴스 반환
```

### 데이터 영속성 및 파일 I/O 라이프사이클
```Plaintext
[프로그램 시작] ➔ QuizGame.__init__() ➔ self.load_state() 실행 (state.json 읽기)
      │
[퀴즈 추가 / 풀기 / 삭제] ➔ 메모리 데이터 변경 (self.quizzes, self.best_score, self.history)
      │                                   │
      ▼                                   ▼
[즉시 저장 트리거] ───────────────> self.save_state() 호출 (state.json 쓰기)
      │
[프로그램 종료(메뉴 7 or Ctrl+C)] ➔ self.save_state() ➔ 최종 파일 쓰기 완료 후 종료
```

### state.json 스키마 설계 및 선정 이유
JSON 포맷 선정 이유: 가독성이 뛰어나 디버깅이 쉽고, 파이썬 내장 json 모듈로 경량화된 직렬화/역직렬화 처리가 가능합니다.

> 필드 구조 및 설계 의도:

- quizzes: Quiz 객체의 리스트를 중첩 구조로 보관하여 문제, 4개 선택지, 정답 번호, 힌트를 통합 관리.

- best_score: 역대 최고 정답 개수를 부동소수점(float) 또는 정수로 보관하여 점수 유지.

- history: 실행 일시(datetime), 총 문항수, 점수, 백분율을 리스트로 누적 기록.

### 파일 I/O 예외 처리 및 복구/백업 전략
- 예외 발생 사례 및 처리 의도:

  - FileNotFoundError: 파일이 처음 실행되어 존재하지 않을 때 get_default_quizzes()로 안전하게 자동 생성.

  - json.JSONDecodeError / ValueError / KeyError: 사용자의 임의 수정 등으로 JSON 문법이 깨지거나 필수 키가 유실된 경우 프로그램을 튕기지 않고 기본 데이터로 초기화 복구.

- 복구 및 백업 절차:

  - 데이터 변경 시점(퀴즈 추가/삭제/풀이 완료)마다 save_state()를 통해 즉시 파일 동기화.

  - 파일 손상 감지 시 콘솔 경고 메시지 출력 후 안전하게 기본 5개 퀴즈 및 0점 상태로 리셋.

### 안전 종료 및 자원 관리
```python
# quiz_game.py > safe_exit()
def safe_exit(self, message: str = "사용자에 의해 프로그램이 중단되었습니다."):
    """인터럽트 발생 시 메모리의 무결성이 검증된 데이터만 저장 후 안전 종료"""
    print(f"\n\n⚠️ {message}")
    self.save_state()  # 미완성 임시 데이터는 배제하고 기존 유효 상태만 디스크에 플러시
    print("👋 데이터를 안전하게 보존하고 프로그램을 종료합니다.")
    sys.exit(0)
```

### 🏛️ 클래스 기반 객체지향 설계의 이점
- 함수형/절차형 구조 대비 데이터(퀴즈 속성)와 행위(정답 검증, 직렬화)를 Quiz 클래스로 캡슐화하여 상태 오염을 방지합니다.
- 다형성과 확장성을 확보하여 추후 주관식 퀴즈, 다중 선택 퀴즈 등 다양한 서브 도메인으로의 확장이 용이합니다.

### 대량 데이터(1,000개 이상) 확장 시 한계점 및 대응 방안
- 한계점: 단일 state.json 파일 전체를 읽고 쓰는 방식은 $O(N)$의 메모리 사용량과 파일 I/O 병목을 유발합니다. 또한 리스트 기반 순차 탐색은 검색 속도 저하를 야기합니다.
- 개선 방안:경량 RDBMS(SQLite) 또는 NoSQL 인덱싱 도입으로 페이징(LIMIT/OFFSET) 및 인덱스 기반 $O(1)$ 탐색 구현.파일 쓰기 시 비동기 큐(Background Worker)를 적용하여 게임 흐름 지연 방지.

### 요구사항 변경에 따른 영향 범위(Impact Surface)

| 변경 요구사항 | 수정 대상 파일 및 클래스/메서드 |
| ------------ | ------------- |
| 변경 요구사항수정 대상 파일 및 클래스/메서드퀴즈 데이터 구조 변경 (보기 개수 변경, 해설 필드 추가) | quiz.py ➔ Quiz.__init__, to_dict, from_dict  |
| 점수 산정 정책 변경 (난이도별 가중치, 힌트 감점율 조정) | quiz_game.py ➔ QuizGame.play_quiz  |
| 저장소 교체 (JSON ➔ SQLite/DB 저장) | quiz_game.py ➔ QuizGame.load_state, save_state |
| 메뉴 및 CLI UI 변경 | quiz_game.py ➔ QuizGame.display_menu, run  |


### 커밋 이력 및 브랜치 병합 증빙 
```bash
git log --oneline --graph
```
![GIT_LOG](/docs/screenshots/git_log.png)


### 원격 변경 사항을 가져오는 표준 실습
git pull origin main
