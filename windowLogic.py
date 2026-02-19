from Morselogic import Converter
from tkinter import *

class mainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("pik's Morse Code Class")
        self.window.geometry("500x300")
        self.window.resizable(False,False)
        self.window.config(bg="dark grey")

        self.convert = Converter()

        with open("words.txt", "r") as file:
            self.words = file.read().splitlines()
        file.close()

        self.currentWord = None
        self.morseWord = None
        self.window.grid_columnconfigure(0, weight=1)

        #
        #FRAMES
        #
        topFrame = Frame(self.window, bg="dark grey")
        topFrame.grid(row = 0, column = 0)
        topFrame.grid_columnconfigure(0, weight=1)
        topFrame.grid_columnconfigure(1, weight=1)
        topFrame.grid_columnconfigure(2, weight=1)

        midFrame = Frame(self.window, bg="dark grey")
        midFrame.grid(row = 1, column = 0, pady=(25,50))
        midFrame.grid_columnconfigure(0, weight=1)
        midFrame.grid_columnconfigure(1, weight=1)
        midFrame.grid_columnconfigure(2, weight=1)


        lowFrame = Frame(self.window, bg ="dark grey")
        lowFrame.grid(row = 2, column = 0)
        lowFrame.grid_columnconfigure(0, weight=1)
        lowFrame.grid_columnconfigure(1, weight=1)
        lowFrame.grid_columnconfigure(2, weight=1)

        #
        #WIDGETS
        #
        buttonGenerateWord = Button(topFrame, text="Generate \n new word", command = self.pickAndPlay)
        buttonGenerateWord.grid(row = 0, column = 1, pady=(25,50), padx=(0,00))

        self.currentScore = 0
        self.scoreText = "score: ", + self.currentScore
        self.scoreLabel = Label(topFrame,text = self.scoreText)
        self.scoreLabel.grid(row = 0, column= 1, padx = (200,0))

        self.winLoseLabel = Label(midFrame, text = "hey")
        self.winLoseLabel.grid(row = 0, column = 1)

        self.playAgainButton = Button(midFrame, text = "play again", command= self.playAgain)
        self.playAgainButton.grid(row = 0, column = 1, padx=(200,0))

        self.inputBox = Text(lowFrame, height = 1, width = 25)
        self.inputBox.grid(row = 0, column = 1)

        submitButton = Button(lowFrame, text = "✓", command = self.submitAnswer)
        submitButton.grid(row = 0, column = 2, padx=(50,0))


    def pickAndPlay(self):
        self.currentWord, self.morseWord = self.convert.wordToMorse(self.words)
        self.convert.soundWord(self.morseWord)



    def submitAnswer(self):
        answer = self.inputBox.get("1.0", END)
        answer = answer.upper()


        if answer == self.currentWord + "\n":
            self.currentScore += 1
            self.winLoseLabel.config(text="Well done!")
            self.scoreLabel.config(text = "score: " + str(self.currentScore))
        
        else:
            self.winLoseLabel.config(text = "kill yourself!!")

        self.inputBox.delete("1.0", END)


    def playAgain(self):
        self.convert.soundWord(self.morseWord)

    def run(self):
        self.window.mainloop()
