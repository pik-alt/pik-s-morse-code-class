import winsound
import random
import time

class Converter:
    def __init__(self):
    
        self.unit = 300

        with open("words.txt", "r") as file:
            self.words = file.read().splitlines()
        file.close()

        self.morseToEnglish = {
            ".-"    : "A",
            "-..."  : "B",
            "-.-."  : "C",
            "-.."   : "D",
            "."     : "E",
            "..-."  : "F",
            "--."   : "G",
            "...."  : "H",
            ".."    : "I",
            ".---"  : "J",
            "-.-"   : "K",
            ".-.."  : "L",
            "--"    : "M",
            "-."    : "N",
            "---"   : "O",
            ".--."  : "P",
            "--.-"  : "Q",
            ".-."   : "R",
            "..."   : "S",
            "-"     : "T",
            "..-"   : "U",
            "...-"  : "V",
            ".--"   : "W",
            "-..-"  : "X",
            "-.--"  : "Y",
            "--.."  : "Z"
        }

        self.englishToMorse = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--.."
        }

    def wordToMorse(self,words):
        wordIndex = random.randint(0,9999)
        currentWord = words[wordIndex]
        currentWord = currentWord.upper()
        print(currentWord)

        #word is now a list with each item being its own letter
        splitWord = list(currentWord)
        wordMorse = []

        #converting each letter to its morse code
        for letter in splitWord:
            wordMorse.append(self.englishToMorse[letter])
        
        return currentWord, wordMorse
    

    def soundWord(self,wordMorse):
        for letter in wordMorse:
            letters = list(letter)

            for currentLetter in letters:
                if currentLetter == ".":
                    winsound.Beep(600, self.unit)
                else:
                    winsound.Beep(600, self.unit * 3)

                #gap between characters within letters    
                time.sleep(self.unit / 1000) #time class uses seconds by default, units are in ms

            #new letter
            time.sleep(self.unit * 3 / 1000)
        
        return

    def pickAndSound(self):
        self.soundWord(self.wordToMorse(self.words)[1])
    
