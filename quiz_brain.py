class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_questions(self):
        length_of_question_list = len(self.question_list)
        #return self.question_number < length_of_question_list
        if self.question_number < length_of_question_list:
            return True
        else:
            print(f"\nYou've completed the quiz\nYour final score is {self.score}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}\nYour current score is: {self.score}/{self.question_number}\n")


