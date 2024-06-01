from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# //loop through question_data
for item in question_data:
    # add question object to list
    question_bank.append(Question(item["text"], item["answer"]))

new_quiz_game = QuizBrain(question_bank)
while new_quiz_game.still_has_question():
    new_quiz_game.next_question()
