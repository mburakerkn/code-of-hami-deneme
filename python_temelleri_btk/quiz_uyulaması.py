# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer




# Quiz

class Quiz:
    def __init__(self,question):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 1
    
    def getQuestion(self):
        return self.questions[quiz.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionsIndex + 1}: {question.text}")
q1 = Question("En iyi programlama dili hangisidir ?",["C#","Python","JavaScript","Java"],"Python")
q2 = Question("En popüler programlama dili hangisidir ?",["Python","C#","Java","JavaScript"],"Python")
q3 = Question("En çok kazandıran programlama dili hangisidir ?",["Java","C#","JavaScript","Python"],"Python")

questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.displayQuestion()
question = quiz.getQuestion() 
print(question.text)

#print(q1.checkAnswer("Python"))
#print(q2.checkAnswer("C#"))