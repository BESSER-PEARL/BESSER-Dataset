from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mealymodel_Transition:

    def __init__(self, input: str, output: str, mealymodel_Transition: "mealymodel_MealyMachine" = None, mealymodel_Transition12: "mealymodel_State" = None, mealymodel_Transition15: "mealymodel_State" = None):
        self.input = input
        self.output = output
        self.mealymodel_Transition = mealymodel_Transition
        self.mealymodel_Transition12 = mealymodel_Transition12
        self.mealymodel_Transition15 = mealymodel_Transition15
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def mealymodel_Transition12(self):
        return self.__mealymodel_Transition12

    @mealymodel_Transition12.setter
    def mealymodel_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_Transition__mealymodel_Transition12", None)
        self.__mealymodel_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_State13"):
                opp_val = getattr(old_value, "mealymodel_State13", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_State13"):
                opp_val = getattr(value, "mealymodel_State13", None)
                setattr(value, "mealymodel_State13", self)

    @property
    def mealymodel_Transition(self):
        return self.__mealymodel_Transition

    @mealymodel_Transition.setter
    def mealymodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_Transition__mealymodel_Transition", None)
        self.__mealymodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_MealyMachine10"):
                opp_val = getattr(old_value, "mealymodel_MealyMachine10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_MealyMachine10"):
                opp_val = getattr(value, "mealymodel_MealyMachine10", None)
                if opp_val is None:
                    setattr(value, "mealymodel_MealyMachine10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mealymodel_Transition15(self):
        return self.__mealymodel_Transition15

    @mealymodel_Transition15.setter
    def mealymodel_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_Transition__mealymodel_Transition15", None)
        self.__mealymodel_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_State16"):
                opp_val = getattr(old_value, "mealymodel_State16", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_State16"):
                opp_val = getattr(value, "mealymodel_State16", None)
                setattr(value, "mealymodel_State16", self)

class mealymodel_Alphabet:

    def __init__(self, characters: str, mealymodel_Alphabet: "mealymodel_MealyMachine" = None, mealymodel_Alphabet8: "mealymodel_MealyMachine" = None):
        self.characters = characters
        self.mealymodel_Alphabet = mealymodel_Alphabet
        self.mealymodel_Alphabet8 = mealymodel_Alphabet8
        
    @property
    def characters(self) -> str:
        return self.__characters

    @characters.setter
    def characters(self, characters: str):
        self.__characters = characters

    @property
    def mealymodel_Alphabet8(self):
        return self.__mealymodel_Alphabet8

    @mealymodel_Alphabet8.setter
    def mealymodel_Alphabet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_Alphabet__mealymodel_Alphabet8", None)
        self.__mealymodel_Alphabet8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_MealyMachine7"):
                opp_val = getattr(old_value, "mealymodel_MealyMachine7", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_MealyMachine7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_MealyMachine7"):
                opp_val = getattr(value, "mealymodel_MealyMachine7", None)
                setattr(value, "mealymodel_MealyMachine7", self)

    @property
    def mealymodel_Alphabet(self):
        return self.__mealymodel_Alphabet

    @mealymodel_Alphabet.setter
    def mealymodel_Alphabet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_Alphabet__mealymodel_Alphabet", None)
        self.__mealymodel_Alphabet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_MealyMachine5"):
                opp_val = getattr(old_value, "mealymodel_MealyMachine5", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_MealyMachine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_MealyMachine5"):
                opp_val = getattr(value, "mealymodel_MealyMachine5", None)
                setattr(value, "mealymodel_MealyMachine5", self)

class mealymodel_State:

    def __init__(self, name: str, mealymodel_State: "mealymodel_MealyMachine" = None, mealymodel_State3: "mealymodel_MealyMachine" = None, mealymodel_State13: "mealymodel_Transition" = None, mealymodel_State16: "mealymodel_Transition" = None):
        self.name = name
        self.mealymodel_State = mealymodel_State
        self.mealymodel_State3 = mealymodel_State3
        self.mealymodel_State13 = mealymodel_State13
        self.mealymodel_State16 = mealymodel_State16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mealymodel_State3(self):
        return self.__mealymodel_State3

    @mealymodel_State3.setter
    def mealymodel_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_State__mealymodel_State3", None)
        self.__mealymodel_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_MealyMachine2"):
                opp_val = getattr(old_value, "mealymodel_MealyMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_MealyMachine2"):
                opp_val = getattr(value, "mealymodel_MealyMachine2", None)
                if opp_val is None:
                    setattr(value, "mealymodel_MealyMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mealymodel_State16(self):
        return self.__mealymodel_State16

    @mealymodel_State16.setter
    def mealymodel_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_State__mealymodel_State16", None)
        self.__mealymodel_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_Transition15"):
                opp_val = getattr(old_value, "mealymodel_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_Transition15"):
                opp_val = getattr(value, "mealymodel_Transition15", None)
                setattr(value, "mealymodel_Transition15", self)

    @property
    def mealymodel_State13(self):
        return self.__mealymodel_State13

    @mealymodel_State13.setter
    def mealymodel_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_State__mealymodel_State13", None)
        self.__mealymodel_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_Transition12"):
                opp_val = getattr(old_value, "mealymodel_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_Transition12"):
                opp_val = getattr(value, "mealymodel_Transition12", None)
                setattr(value, "mealymodel_Transition12", self)

    @property
    def mealymodel_State(self):
        return self.__mealymodel_State

    @mealymodel_State.setter
    def mealymodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mealymodel_State__mealymodel_State", None)
        self.__mealymodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mealymodel_MealyMachine"):
                opp_val = getattr(old_value, "mealymodel_MealyMachine", None)
                if opp_val == self:
                    setattr(old_value, "mealymodel_MealyMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mealymodel_MealyMachine"):
                opp_val = getattr(value, "mealymodel_MealyMachine", None)
                setattr(value, "mealymodel_MealyMachine", self)

class mealymodel_MealyMachine:

    pass