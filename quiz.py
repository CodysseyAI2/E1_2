class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer 

    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer