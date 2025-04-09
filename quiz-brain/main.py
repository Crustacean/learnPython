from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

i = 0

while i < len(question_data):
    for data in range(len(question_data)):
        question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
        i += 1
    
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    
print("You've completed the quiz.")
print(f"Your final score was {quiz_brain.score}/{len(quiz_brain.question_list)}")