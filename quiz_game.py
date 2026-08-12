import json
import os
from quiz import Quiz

class QuizGame:
    
    FILE_PATH = "state.json"

    def __init__(self):
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.load_state()

    def get_default_quizzes(self) -> list[Quiz]:
        return [
            Quiz(
                question="Python에서 가변(Mutable) 객체는 무엇일까요?",
                choices=["tuple", "int", "list", "str"],
                answer=3,
            ),
            Quiz(
                question="리스트의 가장 끝에 요소를 추가하는 메서드는?",
                choices=["add()", "append()", "push()", "insert()"],
                answer=2,
            ),
            Quiz(
                question="다음 중 Python의 기본 데이터 타입이 아닌 것은?",
                choices=["dict", "set", "array", "bool"],
                answer=3,
            ),
            Quiz(
                question="조건문에서 조건이 거짓일 때 실행할 블록을 지정하는 키워드는?",
                choices=["else", "catch", "finally", "then"],
                answer=1,
            ),
            Quiz(
                question="키-값(Key-Value) 쌍으로 데이터를 저장하는 자료형은?",
                choices=["list", "tuple", "dict", "set"],
                answer=3,
            ),
        ]

    def reset_to_default(self):
        self.quizzes = self.get_default_quizzes()
        self.best_score = 0

    def load_state(self):
        if not os.path.exists(self.FILE_PATH):
            print("ℹ️ 데이터 파일이 없습니다. 기본 퀴즈 데이터로 초기화합니다.")
            self.reset_to_default()
            return

        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)

            if not self.quizzes:
                raise ValueError("퀴즈 데이터가 비어 있습니다.")

            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")

        except (json.JSONDecodeError, ValueError, KeyError) as e:
            print(f"⚠️ 데이터 파일이 손상되었거나 형식이 올바르지 않습니다. ({e})")
            print("🔄 기본 퀴즈 데이터로 복구합니다.")
            self.reset_to_default()
        except Exception as e:
            print(f"⚠️ 파일 로드 중 알 수 없는 오류 발생: {e}")
            self.reset_to_default()

    def save_state(self):
        data = {
           "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
      
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("💾 데이터가 안전하게 저장되었습니다.")
        except Exception as e:
            print(f"⚠️ 데이터 저장 실패: {e}")

    @staticmethod
    def get_valid_input_int(prompt: str, min_val: int, max_val: int) -> int:
        while True:
            try:
                user_input = input(prompt).strip()
                val = int(user_input)
                if min_val <= val <= max_val:
                    return val
                print(f"❌ {min_val}부터 {max_val} 사이의 숫자를 입력해 주세요.")
            except ValueError:
                print("❌ 숫자로 올바르게 입력해 주세요.")

    def play_quiz(self):
        if not self.quizzes:
            print("\n❌ 풀어볼 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n 📝 퀴즈를 시작합니다! (총 {total}문제)")

        for idx, quiz in enumerate(self.quizzes, start=1):
            print("\n" + "-" * 40)
            print(f"\n[문제 {idx}/{total}] {quiz.question}")
            for c_idx, choice in enumerate(quiz.choices, start=1):
                print(f"  {c_idx}. {choice}")

            user_ans = self.get_valid_input_int("정답 입력: ", 1, 4)

            if quiz.is_correct(user_ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                correct_choice = quiz.choices[quiz.answer - 1]
                print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번({correct_choice})입니다.")

        percentage = int((score / total) * 100) if total > 0 else 0

        print("\n" + "=" * 42)
        print(f"🏆 결과: {total}문제 중 {score}문제 정답! ({percentage}점)")

        

        if score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score
            self.save_state()
        print("=" * 42)

    def add_quiz(self):
        print("\n➕ 새 퀴즈 추가")
        
        while True:
            question = input("문제 내용을 입력하세요: ").strip()
            if question:
                break
            print("❌ 문제 내용은 공백일 수 없습니다.")

        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}번을 입력하세요: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("❌ 선택지는 공백일 수 없습니다.")

        answer = self.get_valid_input_int("정답 번호를 입력하세요 (1-4): ", 1, 4)

        new_quiz = Quiz(question=question, choices=choices, answer=answer)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("✅ 새 퀴즈가 성공적으로 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("\n❌ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 35)
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"Q{idx}. {quiz.question}")
            for c_idx, choice in enumerate(quiz.choices, start=1):
                mark = " (정답)" if c_idx == quiz.answer else ""
                print(f"   {c_idx}) {choice}{mark}")
            print("-" * 35)

    def show_best_score(self):
        """현재 최고 점수 조회"""
        total = len(self.quizzes)
        print("\n" + "=" * 42)
        print(f"🏆 현재 최고 점수: {self.best_score}점 / (총 {total}문제)")
        if self.best_score == 0:
            print("💡 아직 기록된 최고 점수가 없습니다. 퀴즈에 도전해 보세요!")
        elif self.best_score == total and total > 0:
            print("🥇 만점 기록 보유 중! 대단합니다!")
        print("=" * 42)
    
    def display_menu(self):
        print("\n" + "=" * 42)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 42)
        print(" 1. 퀴즈 풀기")
        print(" 2. 퀴즈 추가")
        print(" 3. 퀴즈 목록")
        print(" 4. 점수 확인")
        print(" 5. 종료")
        print("=" * 42)

    def run(self):
        while True:
            try:
                self.display_menu()
                choice = self.get_valid_input_int("선택: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    self.save_state()
                    print("👋 게임을 종료합니다. 이용해 주셔서 감사합니다!")
                    break

            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 사용자에 의해 프로그램이 중단되었습니다.")
                self.save_state()
                print("👋 데이터를 안전하게 저장하고 종료합니다.")
                break