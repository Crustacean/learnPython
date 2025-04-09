class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)        
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        
        self.question_number += 1
        
        ans = ""
            
        while ans not in ["true", "false"]:
        
            ans = input(f"Q. {self.question_number} {current_question.text} (True/False)?: ").lower()
            
        if ans == (current_question.answer).lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n"*2)
