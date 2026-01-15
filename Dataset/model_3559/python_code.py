from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ConsoleOutput:

    pass
class simpleimperative_Print(ConsoleOutput):

    pass
class simpleimperative_Println(ConsoleOutput):

    pass
class Expression:

    pass
class simpleimperative_VarRef(Expression):

    def __init__(self, varRef: str):
        self.varRef = varRef
        
    @property
    def varRef(self) -> str:
        return self.__varRef

    @varRef.setter
    def varRef(self, varRef: str):
        self.__varRef = varRef

class simpleimperative_Expression(ABC):

    def __init__(self, simpleimperative_Expression: "simpleimperative_Conditional" = None, simpleimperative_Expression16: "simpleimperative_Assignation" = None, simpleimperative_Expression6: "simpleimperative_Loop" = None, simpleimperative_Expression11: "simpleimperative_VarDecl" = None):
        self.simpleimperative_Expression = simpleimperative_Expression
        self.simpleimperative_Expression16 = simpleimperative_Expression16
        self.simpleimperative_Expression6 = simpleimperative_Expression6
        self.simpleimperative_Expression11 = simpleimperative_Expression11
        
    @property
    def simpleimperative_Expression(self):
        return self.__simpleimperative_Expression

    @simpleimperative_Expression.setter
    def simpleimperative_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleimperative_Expression__simpleimperative_Expression", None)
        self.__simpleimperative_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleimperative_Conditional"):
                opp_val = getattr(old_value, "simpleimperative_Conditional", None)
                if opp_val == self:
                    setattr(old_value, "simpleimperative_Conditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleimperative_Conditional"):
                opp_val = getattr(value, "simpleimperative_Conditional", None)
                setattr(value, "simpleimperative_Conditional", self)

    @property
    def simpleimperative_Expression16(self):
        return self.__simpleimperative_Expression16

    @simpleimperative_Expression16.setter
    def simpleimperative_Expression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleimperative_Expression__simpleimperative_Expression16", None)
        self.__simpleimperative_Expression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleimperative_Assignation15"):
                opp_val = getattr(old_value, "simpleimperative_Assignation15", None)
                if opp_val == self:
                    setattr(old_value, "simpleimperative_Assignation15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleimperative_Assignation15"):
                opp_val = getattr(value, "simpleimperative_Assignation15", None)
                setattr(value, "simpleimperative_Assignation15", self)

    @property
    def simpleimperative_Expression11(self):
        return self.__simpleimperative_Expression11

    @simpleimperative_Expression11.setter
    def simpleimperative_Expression11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleimperative_Expression__simpleimperative_Expression11", None)
        self.__simpleimperative_Expression11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleimperative_VarDecl"):
                opp_val = getattr(old_value, "simpleimperative_VarDecl", None)
                if opp_val == self:
                    setattr(old_value, "simpleimperative_VarDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleimperative_VarDecl"):
                opp_val = getattr(value, "simpleimperative_VarDecl", None)
                setattr(value, "simpleimperative_VarDecl", self)

    @property
    def simpleimperative_Expression6(self):
        return self.__simpleimperative_Expression6

    @simpleimperative_Expression6.setter
    def simpleimperative_Expression6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleimperative_Expression__simpleimperative_Expression6", None)
        self.__simpleimperative_Expression6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleimperative_Loop"):
                opp_val = getattr(old_value, "simpleimperative_Loop", None)
                if opp_val == self:
                    setattr(old_value, "simpleimperative_Loop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleimperative_Loop"):
                opp_val = getattr(value, "simpleimperative_Loop", None)
                setattr(value, "simpleimperative_Loop", self)

    def eval(self, context: str):
        # TODO: Implement eval method
        pass

class Statement:

    pass
class simpleimperative_ConsoleOutput(Statement):

    def __init__(self, input: str):
        self.input = input
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

class simpleimperative_Wait(Statement):

    def __init__(self, miliseconds: str):
        self.miliseconds = miliseconds
        
    @property
    def miliseconds(self) -> str:
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self, miliseconds: str):
        self.__miliseconds = miliseconds

class simpleimperative_Assignation(Statement):

    pass
class simpleimperative_Loop(Statement):

    pass
class simpleimperative_VarDecl(Statement):

    def __init__(self, name: str, simpleimperative_VarDecl13: "simpleimperative_Assignation" = None, simpleimperative_VarDecl: "simpleimperative_Expression" = None):
        self.name = name
        self.simpleimperative_VarDecl13 = simpleimperative_VarDecl13
        self.simpleimperative_VarDecl = simpleimperative_VarDecl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleimperative_VarDecl(self):
        return self.__simpleimperative_VarDecl

    @simpleimperative_VarDecl.setter
    def simpleimperative_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleimperative_VarDecl__simpleimperative_VarDecl", None)
        self.__simpleimperative_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleimperative_Expression11"):
                opp_val = getattr(old_value, "simpleimperative_Expression11", None)
                if opp_val == self:
                    setattr(old_value, "simpleimperative_Expression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleimperative_Expression11"):
                opp_val = getattr(value, "simpleimperative_Expression11", None)
                setattr(value, "simpleimperative_Expression11", self)

    @property
    def simpleimperative_VarDecl13(self):
        return self.__simpleimperative_VarDecl13

    @simpleimperative_VarDecl13.setter
    def simpleimperative_VarDecl13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleimperative_VarDecl__simpleimperative_VarDecl13", None)
        self.__simpleimperative_VarDecl13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleimperative_Assignation"):
                opp_val = getattr(old_value, "simpleimperative_Assignation", None)
                if opp_val == self:
                    setattr(old_value, "simpleimperative_Assignation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleimperative_Assignation"):
                opp_val = getattr(value, "simpleimperative_Assignation", None)
                setattr(value, "simpleimperative_Assignation", self)

class simpleimperative_Conditional(Statement):

    pass
class simpleimperative_Statement(ABC):

    pass
class simpleimperative_Program:

    pass