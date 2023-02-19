from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dictionary in question_data:
    our_question = dictionary["question"]
    our_answer = dictionary["correct_answer"]
    question_bank.append(Question(our_question, our_answer))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()
    print()
print("You have completed the Quiz")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")
































# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank = []
# for index in range(0, len(question_data) - 1):
#     dicts = question_data[index]
#     text = dicts["text"]
#     answer = dicts["answer"]
#     question_bank.append(Question(text, answer))
#
# running = True
# while running:
#     quiz_brain = QuizBrain(question_bank)
#     if quiz_brain.next_question() == answer:
#         quiz_brain.next_question()
#
#     else:
#         print(f"Your score is: {quiz_brain.question_number}/{len(question_bank)}")
#         running = False
