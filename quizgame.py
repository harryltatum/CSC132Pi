#############################################################
# Group Members: Harry Tatum, Sammy Breaux, Dillan Mickel   #
# Project: Dynamic Quiz Game                                #
#############################################################

#imports
from tkinter import *
import random
import pygame

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
        self.rightAnswer = answer
        self.answers = [str(answer), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(self.answers)

    #str method
    #prints the question and then the 4 answers
    def __str__(self):
        return "{}\n{}".format(self._question, self._answers)

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
        self._rightAnswer = str(val)

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
        if(guess is self._rightAnswer):
            return True
        else:
            return False

#####################################################
# Game Class                                        #
# This class will inherit from the Tkinter frame    #
# Akin to the room adventure reloaded activity      #
# it will be responsible for GUI, gameplay, etc.    #
#####################################################
class Game(Frame):
    #constructor
    def __init__(self, window):
        #use parent constructor (Tkinter Frame)
        Frame.__init__(self, window)
    #TODO: implement rest of Game class (GUI, gameplay, etc)

    #Regarding subjects/questions/difficulty:
    #Questions will be stored in a list
    #each list of questions will have an associated subject/difficulty
    #with the exception of math which will have RNG questions
    
    def setupPygame(self):
        pygame.init()
        pygame.mixer.music.load("4-MAT_mm-complete")
        pygame.mixer.music.play(loops=-1)
        
        # this be the music, yar
        

################
# Testing Code #       
################

#create question
q1 = Question("What is the first letter of the alphabet?", "A","B","C","D")
#print quesstion
print(q1)
#take answer and return correctness
print(q1.checkAnswer(input("Answer: ")))

 #######################
### MAIN PROGRAM CODE ###
 #######################

#create window
window = Tk()
window.title("Dynamic Quiz")

#create GUI as tkinter frame
#TODO
