#############################################################
# Group Members: Harry Tatum, Sammy Breaux, Dillan Mickel   #
# Project: Dynamic Quiz Game                                #
#############################################################

#imports
from tkinter import *
import tkinter
import random
import time
#import RPi.GPIO as GPIO
import os


#################################################################
# Questions class                                               #
# The questions class will have:                                #
# 1. A string value for the question                            #
# 2. A string value for the answer                              #
# 3. A list value which stores the 4 multiple choice answers    #
# The correct answer should be 1 of the 4 in the list           #
#################################################################
class Question:
    #constructor
    #it takes the question
    #it takes the 4 answer choices and shuffles them into a list
    #while using another var to keep track of the right answer
    def __init__(self, question, answer, wrong1, wrong2, wrong3):
        self.question = question
        self.answers = [str(answer), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(self.answers)
        self.rightAnswer = answer

    #str method
    #prints the question and then the 4 answers
    def __str__(self):
        return "{}\nA: {}\nB: {}\nC: {}\nD: {}".format(self._question, self._answers[0], self._answers[1], self._answers[2], self._answers[3])

    #access methods and mutators
    @property
    def question(self):
        return self._question

    @property
    def rightAnswer(self):
        return self._rightAnswer

    @property
    def answers(self):
        return self._answers

    @question.setter
    def question(self, val):
        self._question = str(val)

    @rightAnswer.setter
    def rightAnswer(self, val):
        for i in range(len(self._answers)):
            if(self.answers[i] == (val)):
                self._rightAnswer = i+1

    #this might have to be changed later
    #rn it takes a list, and makes a new list with all elements converted into a string
    @answers.setter
    def answers(self, val):
        newlist = []
        for i in val:
            newlist.append(str(i))
        self._answers = newlist

    #checkAnswer method
    #this method returns TRUE if the string input matches rightAnswer
    #otherwise it returns FALSE
    def checkAnswer(self, guess):

        if(int(guess) is self._rightAnswer):
            return True
        else:
            return False

class MainGUI(Frame, Question):
# the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", True)
        self.clearScreen = 0
        self.setupGUI()

# sets up the GUI
    def setupGUI(self):
        self.display = Label(self, text="", anchor=CENTER, bg="white",\
        height=3, font=("TexGyreAdventor", 45))
        # put it in the top row, spanning across all four columns;
        # and expand it on all four sides
        self.display.grid(row=0, column=0, columnspan=4,\
        sticky=E+W+N+S)
        # configure the rows and columns of the Frame to adjust to
        # the window
        # there are 2 rows (0 through 1)
        for row in range(2):
            Grid.rowconfigure(self, row, weight=1)
            # there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        path = os.getcwd()
        #Button A
        img = PhotoImage(file=r"{}/ButtonA.png".format(path))
        button = Button(self, bg="white", image=img, borderwidth=0,\
        highlightthickness=0, activebackground="white",\
        command=lambda: self.process("A"))
        button.image = img
        button.grid(row=1, column=0, sticky=N+S+E+W)
        #ButtonB
        img = PhotoImage(file=r"{}/ButtonB.png".format(path))
        button = Button(self, bg="white", image=img, borderwidth=0,\
        highlightthickness=0, activebackground="white",\
        command=lambda: self.process("B"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)
        #ButtonC
        img = PhotoImage(file=r"{}/ButtonC.png".format(path))
        button = Button(self, bg="white", image=img, borderwidth=0,\
        highlightthickness=0, activebackground="white",\
        command=lambda: self.process("C"))
        button.image = img
        button.grid(row=1, column=2, sticky=N+S+E+W)
        #ButtonD
        img = PhotoImage(file=r"{}/ButtonD.png".format(path))
        button = Button(self, bg="white", image=img, borderwidth=0,\
        highlightthickness=0, activebackground="white",\
        command=lambda: self.process("D"))
        button.image = img
        button.grid(row=1, column=3, sticky=N+S+E+W)
        # pack the GUI
        self.pack(fill=BOTH, expand=1)

    def setText(self, text):
        self.display["text"] = text
    
    def ending():
        ending = "That's all of the questions!"
        self.setText(ending)

    def question(self, questions):
        global currentQuestion
        if(len(questions)==0):
            self.display["text"] = "That's all of the questions!"
        elif(len(questions)>1):
            self.setText(questions[random.randint(0,len(questions)-1)])
            for i in range(len(questions)):
                if(self.display["text"] == str(questions[i-1])):
                    currentQuestion = questions[i-1]
                    questions.remove(currentQuestion)
        elif(len(questions)==1):
            currentQuestion = questions[0]
            self.setText(str(currentQuestion))
            questions.remove(currentQuestion)

        

    def process(self, button):
        tempAnswer = 0
        if(self.clearScreen == 1):
            self.display["text"] = ""
            self.clearScreen = 0
        if (button == "A"):
            tempAnswer = 1
        elif (button == "B"):
            tempAnswer = 2  
        elif (button == "C"):
            tempAnswer = 3
        elif (button == "D"):
            tempAnswer = 4
        if(len(questions)==0):
            self.setText("That's all of the questions!")
        if(currentQuestion.checkAnswer(tempAnswer)):
            self.setText("Correct")
            time.sleep(1)
            self.question(questions)
        else:
            self.setText("Incorrect")
            time.sleep(1)
            self.question(questions)

    


#switches on the board
#switches = [20, 16, 12, 26]
# use the Broadcom pin mode
#GPIO.setmode(GPIO.BCM)
# setup the input and output pins
#GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def mathQuestion(range):
    operator = random.randint(1,4)
    if(operator==1):
        mathQuestion = random.randint(1, range) + random.randint(1, range)
    elif(operator==2):
        mathQuestion = random.randint(1, range) - random.randint(1, range)
    elif(operator==3):
        mathQuestion = random.randint(1, range) * random.randint(1, range)
    elif(operator==4):
        mathQuestion = random.randint(1, range)/random.randint(1, range)
    return mathQuestion
################
# Testing Code #       
################

#create question
window = Tk()
quizGUI = MainGUI(window)


q1 = Question("What is the first letter of the alphabet?", "A","B","C","D")
q2 = Question("What is 2+2?", "4","8","16","22")
q3 = Question("What city was the first capital of the United States?", "New York City", "Washington D.C.", "Hampton", "Jersey City")
q4 = Question("When was the Declaration of independence signed?", "August 2, 1776", "July 4, 1776", "May 4, 1776", "September 2, 1776")
q5 = Question("What year did America gain its independence?", "1776","1861","1492","1607")
q6 = Question("What is the correct spelling of \"Apple\"?", "Apple","Appel","Apall","Aple")
q7 = Question("What was the last Chinese dynasty?", "Qing","Ming","Han","Yuan")
q8 = Question("What is the noun in \"Toad hopped.\"?", "Toad","Hopped","There is no noun.","That isn't a correct sentence.")
q9 = Question("What is the square root of 49?", "7","5","6","2,401")
q10 = Question("Convert the following unsigned byte into 0x10: 00010111", "39","10,111","256","255")
q11 = Question("Riga is the capital of what country?", "Latvia","Italy","Lithuania","Russia")
q12 = Question("What battle led to the dissolution of the Holy Roman Empire?", "The Battle of Austerlitz","The Battle of Waterloo","The Siege of Troy","The Battle of Britain")
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]
quizGUI.question(questions)
#game = True
#while game:
    #if(GPIO.input(switches[0]) == True):
        #quizGUI.process("A")
    #if(GPIO.input(switches[1]) == True):
        #quizGUI.process("B")
    #if(GPIO.input(switches[2]) == True):
        #quizGUI.process("C")
    #if(GPIO.input(switches[3]) == True):
        #quizGUI.process("D")
    #window.update()     
