class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        """prints the next question on the screen. """
        current_question = self.question_list[self.question_number].question
        current_answer = self.question_list[self.question_number].answer
        answer = input(f"Q.{self.question_number + 1} {current_question}. (True/False)?: ")
        if self.check_answer(answer, current_answer):
            self.score += 1
            print(f"You are right!,your current score is {self.score}/{self.question_number+1}")
        else:
            print(f"You are wrong!,your current score is {self.score}/{self.question_number+1}")
        self.question_number += 1

    def still_has_question(self):
        """Returns true if has more questions, otherwise false."""
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self, player_answer, game_answer):
        """check the answer and return true if correct or vice versa."""
        if player_answer.lower() == game_answer.lower():
            return True
        return False
