from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for c in range(len(question_data)):
  question = Question(question_data[c]["text"],question_data[c]["answer"])
  question_bank.append(question)

#for c in question_bank:
#  print(c.text)
#  print(c.answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  quiz.next_question()
print("You've completed the quiz")
print(f"Your final score: {quiz.score}/{quiz.question_number}")