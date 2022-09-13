from man_shape import stages
from words import word_list
import random


class Words:
    def __init__(self):
        self.close_word = ""
        self.word = ""
        self.rights = 6
        self.found_letter = []

    def get_word(self):
        self.word = random.choice(word_list)
        for _ in range(len(self.word)):
            self.found_letter.append("_ ") 

        
    def show_word_stage(self):
        self.close_word = ""
        
        for j in self.found_letter:
            self.close_word += j
        
        man_stage = stages[self.rights]  
        print(f"{man_stage}\n{self.close_word}")


    def set_word(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.found_letter[i] = letter
        
      
        
    def lose_right(self):
        self.rights -= 1
