import random
import time

with open("words2.txt", "r") as file:
    words = file.readlines()
file.close()


while True:
    print(words[random.randint(0,len(words))])
    time.sleep(3)