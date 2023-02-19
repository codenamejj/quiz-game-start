class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        current_answer = current_answer.lower()
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question}. (True/False): ").lower()
        self.check_answer(current_answer, choice)

    def check_answer(self, current_answer, choice):
        if current_answer == choice:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.question_number}")
