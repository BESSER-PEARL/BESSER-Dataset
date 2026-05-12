from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stateMachineActions_Parameters:

    def __init__(self, param: str, stateMachineActions_Parameters19: "stateMachineActions_Parameters" = None, stateMachineActions_Parameters17: "stateMachineActions_Parameters" = None, stateMachineActions_Parameters: "stateMachineActions_EventAction" = None):
        self.param = param
        self.stateMachineActions_Parameters19 = stateMachineActions_Parameters19
        self.stateMachineActions_Parameters17 = stateMachineActions_Parameters17
        self.stateMachineActions_Parameters = stateMachineActions_Parameters
        
        pass
    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param: str):
        self.__param = param


    @property
    def stateMachineActions_Parameters19(self):
        return self.__stateMachineActions_Parameters19

    @stateMachineActions_Parameters19.setter
    def stateMachineActions_Parameters19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_Parameters__stateMachineActions_Parameters19", None)
        self.__stateMachineActions_Parameters19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_Parameters17"):
                opp_val = getattr(old_value, "stateMachineActions_Parameters17", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_Parameters17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_Parameters17"):
                opp_val = getattr(value, "stateMachineActions_Parameters17", None)
                setattr(value, "stateMachineActions_Parameters17", self)

    @property
    def stateMachineActions_Parameters17(self):
        return self.__stateMachineActions_Parameters17

    @stateMachineActions_Parameters17.setter
    def stateMachineActions_Parameters17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_Parameters__stateMachineActions_Parameters17", None)
        self.__stateMachineActions_Parameters17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_Parameters19"):
                opp_val = getattr(old_value, "stateMachineActions_Parameters19", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_Parameters19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_Parameters19"):
                opp_val = getattr(value, "stateMachineActions_Parameters19", None)
                setattr(value, "stateMachineActions_Parameters19", self)

    @property
    def stateMachineActions_Parameters(self):
        return self.__stateMachineActions_Parameters

    @stateMachineActions_Parameters.setter
    def stateMachineActions_Parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_Parameters__stateMachineActions_Parameters", None)
        self.__stateMachineActions_Parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_EventAction16"):
                opp_val = getattr(old_value, "stateMachineActions_EventAction16", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_EventAction16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_EventAction16"):
                opp_val = getattr(value, "stateMachineActions_EventAction16", None)
                setattr(value, "stateMachineActions_EventAction16", self)

class stateMachineActions_EXPRESSION:

    def __init__(self, operator: str, stateMachineActions_EXPRESSION8: "stateMachineActions_TERM" = None, stateMachineActions_EXPRESSION10: "stateMachineActions_TERM" = None, stateMachineActions_EXPRESSION13: "stateMachineActions_TERM" = None, stateMachineActions_EXPRESSION: "stateMachineActions_Assignment" = None):
        self.operator = operator
        self.stateMachineActions_EXPRESSION8 = stateMachineActions_EXPRESSION8
        self.stateMachineActions_EXPRESSION10 = stateMachineActions_EXPRESSION10
        self.stateMachineActions_EXPRESSION13 = stateMachineActions_EXPRESSION13
        self.stateMachineActions_EXPRESSION = stateMachineActions_EXPRESSION
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stateMachineActions_EXPRESSION10(self):
        return self.__stateMachineActions_EXPRESSION10

    @stateMachineActions_EXPRESSION10.setter
    def stateMachineActions_EXPRESSION10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION10", None)
        self.__stateMachineActions_EXPRESSION10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_TERM11"):
                opp_val = getattr(old_value, "stateMachineActions_TERM11", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_TERM11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_TERM11"):
                opp_val = getattr(value, "stateMachineActions_TERM11", None)
                setattr(value, "stateMachineActions_TERM11", self)

    @property
    def stateMachineActions_EXPRESSION8(self):
        return self.__stateMachineActions_EXPRESSION8

    @stateMachineActions_EXPRESSION8.setter
    def stateMachineActions_EXPRESSION8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION8", None)
        self.__stateMachineActions_EXPRESSION8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_TERM"):
                opp_val = getattr(old_value, "stateMachineActions_TERM", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_TERM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_TERM"):
                opp_val = getattr(value, "stateMachineActions_TERM", None)
                setattr(value, "stateMachineActions_TERM", self)

    @property
    def stateMachineActions_EXPRESSION(self):
        return self.__stateMachineActions_EXPRESSION

    @stateMachineActions_EXPRESSION.setter
    def stateMachineActions_EXPRESSION(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION", None)
        self.__stateMachineActions_EXPRESSION = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_Assignment6"):
                opp_val = getattr(old_value, "stateMachineActions_Assignment6", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_Assignment6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_Assignment6"):
                opp_val = getattr(value, "stateMachineActions_Assignment6", None)
                setattr(value, "stateMachineActions_Assignment6", self)

    @property
    def stateMachineActions_EXPRESSION13(self):
        return self.__stateMachineActions_EXPRESSION13

    @stateMachineActions_EXPRESSION13.setter
    def stateMachineActions_EXPRESSION13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION13", None)
        self.__stateMachineActions_EXPRESSION13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_TERM14"):
                opp_val = getattr(old_value, "stateMachineActions_TERM14", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_TERM14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_TERM14"):
                opp_val = getattr(value, "stateMachineActions_TERM14", None)
                setattr(value, "stateMachineActions_TERM14", self)

class stateMachineActions_EventAction:

    def __init__(self, eventName: str, eventExtension: str, stateMachineActions_EventAction: "stateMachineActions_Action" = None, stateMachineActions_EventAction16: "stateMachineActions_Parameters" = None):
        self.eventName = eventName
        self.eventExtension = eventExtension
        self.stateMachineActions_EventAction = stateMachineActions_EventAction
        self.stateMachineActions_EventAction16 = stateMachineActions_EventAction16
        
        pass
    @property
    def eventExtension(self):
        return self.__eventExtension

    @eventExtension.setter
    def eventExtension(self, eventExtension: str):
        self.__eventExtension = eventExtension


    @property
    def eventName(self):
        return self.__eventName

    @eventName.setter
    def eventName(self, eventName: str):
        self.__eventName = eventName


    @property
    def stateMachineActions_EventAction(self):
        return self.__stateMachineActions_EventAction

    @stateMachineActions_EventAction.setter
    def stateMachineActions_EventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_EventAction__stateMachineActions_EventAction", None)
        self.__stateMachineActions_EventAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_Action4"):
                opp_val = getattr(old_value, "stateMachineActions_Action4", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_Action4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_Action4"):
                opp_val = getattr(value, "stateMachineActions_Action4", None)
                setattr(value, "stateMachineActions_Action4", self)

    @property
    def stateMachineActions_EventAction16(self):
        return self.__stateMachineActions_EventAction16

    @stateMachineActions_EventAction16.setter
    def stateMachineActions_EventAction16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_EventAction__stateMachineActions_EventAction16", None)
        self.__stateMachineActions_EventAction16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_Parameters"):
                opp_val = getattr(old_value, "stateMachineActions_Parameters", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_Parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_Parameters"):
                opp_val = getattr(value, "stateMachineActions_Parameters", None)
                setattr(value, "stateMachineActions_Parameters", self)

class stateMachineActions_Assignment:

    def __init__(self, leftvar: str, stateMachineActions_Assignment: "stateMachineActions_Action" = None, stateMachineActions_Assignment6: "stateMachineActions_EXPRESSION" = None):
        self.leftvar = leftvar
        self.stateMachineActions_Assignment = stateMachineActions_Assignment
        self.stateMachineActions_Assignment6 = stateMachineActions_Assignment6
        
        pass
    @property
    def leftvar(self):
        return self.__leftvar

    @leftvar.setter
    def leftvar(self, leftvar: str):
        self.__leftvar = leftvar


    @property
    def stateMachineActions_Assignment6(self):
        return self.__stateMachineActions_Assignment6

    @stateMachineActions_Assignment6.setter
    def stateMachineActions_Assignment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_Assignment__stateMachineActions_Assignment6", None)
        self.__stateMachineActions_Assignment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_EXPRESSION"):
                opp_val = getattr(old_value, "stateMachineActions_EXPRESSION", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_EXPRESSION", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_EXPRESSION"):
                opp_val = getattr(value, "stateMachineActions_EXPRESSION", None)
                setattr(value, "stateMachineActions_EXPRESSION", self)

    @property
    def stateMachineActions_Assignment(self):
        return self.__stateMachineActions_Assignment

    @stateMachineActions_Assignment.setter
    def stateMachineActions_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_Assignment__stateMachineActions_Assignment", None)
        self.__stateMachineActions_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_Action2"):
                opp_val = getattr(old_value, "stateMachineActions_Action2", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_Action2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_Action2"):
                opp_val = getattr(value, "stateMachineActions_Action2", None)
                setattr(value, "stateMachineActions_Action2", self)

class stateMachineActions_TERM:

    def __init__(self, variable: str, constant: int, stateMachineActions_TERM: "stateMachineActions_EXPRESSION" = None, stateMachineActions_TERM11: "stateMachineActions_EXPRESSION" = None, stateMachineActions_TERM14: "stateMachineActions_EXPRESSION" = None):
        self.variable = variable
        self.constant = constant
        self.stateMachineActions_TERM = stateMachineActions_TERM
        self.stateMachineActions_TERM11 = stateMachineActions_TERM11
        self.stateMachineActions_TERM14 = stateMachineActions_TERM14
        
        pass
    @property
    def constant(self):
        return self.__constant

    @constant.setter
    def constant(self, constant: int):
        self.__constant = constant


    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable


    @property
    def stateMachineActions_TERM14(self):
        return self.__stateMachineActions_TERM14

    @stateMachineActions_TERM14.setter
    def stateMachineActions_TERM14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_TERM__stateMachineActions_TERM14", None)
        self.__stateMachineActions_TERM14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_EXPRESSION13"):
                opp_val = getattr(old_value, "stateMachineActions_EXPRESSION13", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_EXPRESSION13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_EXPRESSION13"):
                opp_val = getattr(value, "stateMachineActions_EXPRESSION13", None)
                setattr(value, "stateMachineActions_EXPRESSION13", self)

    @property
    def stateMachineActions_TERM11(self):
        return self.__stateMachineActions_TERM11

    @stateMachineActions_TERM11.setter
    def stateMachineActions_TERM11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_TERM__stateMachineActions_TERM11", None)
        self.__stateMachineActions_TERM11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_EXPRESSION10"):
                opp_val = getattr(old_value, "stateMachineActions_EXPRESSION10", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_EXPRESSION10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_EXPRESSION10"):
                opp_val = getattr(value, "stateMachineActions_EXPRESSION10", None)
                setattr(value, "stateMachineActions_EXPRESSION10", self)

    @property
    def stateMachineActions_TERM(self):
        return self.__stateMachineActions_TERM

    @stateMachineActions_TERM.setter
    def stateMachineActions_TERM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineActions_TERM__stateMachineActions_TERM", None)
        self.__stateMachineActions_TERM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineActions_EXPRESSION8"):
                opp_val = getattr(old_value, "stateMachineActions_EXPRESSION8", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineActions_EXPRESSION8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineActions_EXPRESSION8"):
                opp_val = getattr(value, "stateMachineActions_EXPRESSION8", None)
                setattr(value, "stateMachineActions_EXPRESSION8", self)

class stateMachineActions_Action:

    pass
class stateMachineActions_Model:

    pass