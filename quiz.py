import json
import os
import sys

class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int, hint: str=""):
        self.question = question
        self.choices = choices
        self.answer = answer 
        self.hint = hint

    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer
    
    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", ""),
        )