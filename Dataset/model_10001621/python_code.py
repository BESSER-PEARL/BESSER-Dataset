from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Matching:

    def __init__(self, question: str, c1__c2__c3__c4: str, col1__col2: str, answer: str, multians: bool):
        self.question = question
        self.c1__c2__c3__c4 = c1__c2__c3__c4
        self.col1__col2 = col1__col2
        self.answer = answer
        self.multians = multians
        
        pass
    @property
    def c1__c2__c3__c4(self):
        return self.__c1__c2__c3__c4
    @c1__c2__c3__c4.setter
    def c1__c2__c3__c4(self, c1__c2__c3__c4: str):
        self.__c1__c2__c3__c4 = c1__c2__c3__c4

    @property
    def multians(self):
        return self.__multians
    @multians.setter
    def multians(self, multians: bool):
        self.__multians = multians

    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def col1__col2(self):
        return self.__col1__col2
    @col1__col2.setter
    def col1__col2(self, col1__col2: str):
        self.__col1__col2 = col1__col2



class MachingQuestion_Interface:

    pass


class Ranking:

    def __init__(self, question: str, c1__c2__c3__c4: str, answer: str, multians: bool):
        self.question = question
        self.c1__c2__c3__c4 = c1__c2__c3__c4
        self.answer = answer
        self.multians = multians
        
        pass
    @property
    def c1__c2__c3__c4(self):
        return self.__c1__c2__c3__c4
    @c1__c2__c3__c4.setter
    def c1__c2__c3__c4(self, c1__c2__c3__c4: str):
        self.__c1__c2__c3__c4 = c1__c2__c3__c4

    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def multians(self):
        return self.__multians
    @multians.setter
    def multians(self, multians: bool):
        self.__multians = multians

    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer



class Essay:

    def __init__(self, question: str, c1__c2__c3__c4: str, answer: str, multians: bool):
        self.question = question
        self.c1__c2__c3__c4 = c1__c2__c3__c4
        self.answer = answer
        self.multians = multians
        
        pass
    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def c1__c2__c3__c4(self):
        return self.__c1__c2__c3__c4
    @c1__c2__c3__c4.setter
    def c1__c2__c3__c4(self, c1__c2__c3__c4: str):
        self.__c1__c2__c3__c4 = c1__c2__c3__c4

    @property
    def multians(self):
        return self.__multians
    @multians.setter
    def multians(self, multians: bool):
        self.__multians = multians

    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question



class ShortAnswer:

    def __init__(self, question: str, c1__c2__c3__c4: str, answer: str, multians: bool):
        self.question = question
        self.c1__c2__c3__c4 = c1__c2__c3__c4
        self.answer = answer
        self.multians = multians
        
        pass
    @property
    def c1__c2__c3__c4(self):
        return self.__c1__c2__c3__c4
    @c1__c2__c3__c4.setter
    def c1__c2__c3__c4(self, c1__c2__c3__c4: str):
        self.__c1__c2__c3__c4 = c1__c2__c3__c4

    @property
    def multians(self):
        return self.__multians
    @multians.setter
    def multians(self, multians: bool):
        self.__multians = multians

    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer



class MC:

    def __init__(self, c1__c2__c3__c4: str, answer: str, multians: bool, question: str):
        self.c1__c2__c3__c4 = c1__c2__c3__c4
        self.answer = answer
        self.multians = multians
        self.question = question
        
        pass
    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def c1__c2__c3__c4(self):
        return self.__c1__c2__c3__c4
    @c1__c2__c3__c4.setter
    def c1__c2__c3__c4(self, c1__c2__c3__c4: str):
        self.__c1__c2__c3__c4 = c1__c2__c3__c4

    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def multians(self):
        return self.__multians
    @multians.setter
    def multians(self, multians: bool):
        self.__multians = multians



class TF:

    def __init__(self, question: str, c1__c2__c3__c4: str, answer: str, multians: bool):
        self.question = question
        self.c1__c2__c3__c4 = c1__c2__c3__c4
        self.answer = answer
        self.multians = multians
        
        pass
    @property
    def c1__c2__c3__c4(self):
        return self.__c1__c2__c3__c4
    @c1__c2__c3__c4.setter
    def c1__c2__c3__c4(self, c1__c2__c3__c4: str):
        self.__c1__c2__c3__c4 = c1__c2__c3__c4

    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def multians(self):
        return self.__multians
    @multians.setter
    def multians(self, multians: bool):
        self.__multians = multians



class Question_T__Interface:

    pass
