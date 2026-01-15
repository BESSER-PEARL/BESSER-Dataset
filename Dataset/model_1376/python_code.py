from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Command:

    pass
class statemachine_ExecuteCommand(Command):

    def __init__(self, operation: str, statemachine_ExecuteCommand: set["statemachine_Expression"] = None):
        self.operation = operation
        self.statemachine_ExecuteCommand = statemachine_ExecuteCommand if statemachine_ExecuteCommand is not None else set()
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def statemachine_ExecuteCommand(self):
        return self.__statemachine_ExecuteCommand

    @statemachine_ExecuteCommand.setter
    def statemachine_ExecuteCommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_ExecuteCommand__statemachine_ExecuteCommand", None)
        self.__statemachine_ExecuteCommand = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Expression16"):
                    opp_val = getattr(item, "statemachine_Expression16", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Expression16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Expression16"):
                    opp_val = getattr(item, "statemachine_Expression16", None)
                    
                    setattr(item, "statemachine_Expression16", self)
                    

class statemachine_SetCommand(Command):

    def __init__(self, signal: str, statemachine_SetCommand: "statemachine_Expression" = None):
        self.signal = signal
        self.statemachine_SetCommand = statemachine_SetCommand
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def statemachine_SetCommand(self):
        return self.__statemachine_SetCommand

    @statemachine_SetCommand.setter
    def statemachine_SetCommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_SetCommand__statemachine_SetCommand", None)
        self.__statemachine_SetCommand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Expression14"):
                opp_val = getattr(old_value, "statemachine_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Expression14"):
                opp_val = getattr(value, "statemachine_Expression14", None)
                setattr(value, "statemachine_Expression14", self)

class statemachine_Expression:

    pass
class Expression:

    pass
class statemachine_StatePropertyExpression(Expression):

    def __init__(self, property: str, statemachine_StatePropertyExpression: "statemachine_State" = None):
        self.property = property
        self.statemachine_StatePropertyExpression = statemachine_StatePropertyExpression
        
    @property
    def property(self) -> str:
        return self.__property

    @property.setter
    def property(self, property: str):
        self.__property = property

    @property
    def statemachine_StatePropertyExpression(self):
        return self.__statemachine_StatePropertyExpression

    @statemachine_StatePropertyExpression.setter
    def statemachine_StatePropertyExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StatePropertyExpression__statemachine_StatePropertyExpression", None)
        self.__statemachine_StatePropertyExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State20"):
                opp_val = getattr(old_value, "statemachine_State20", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State20"):
                opp_val = getattr(value, "statemachine_State20", None)
                setattr(value, "statemachine_State20", self)

class statemachine_VerbatimExpression(Expression):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class statemachine_PrintCommand(Command):

    pass
class statemachine_Transition:

    pass
class statemachine_State:

    def __init__(self, name: str, initial: bool, final: bool, id: str, statemachine_State4: set["statemachine_Command"] = None, statemachine_State7: "statemachine_Transition" = None, statemachine_State10: "statemachine_Transition" = None, statemachine_State: "statemachine_Statemachine" = None, statemachine_State20: "statemachine_StatePropertyExpression" = None):
        self.name = name
        self.initial = initial
        self.final = final
        self.id = id
        self.statemachine_State4 = statemachine_State4 if statemachine_State4 is not None else set()
        self.statemachine_State7 = statemachine_State7
        self.statemachine_State10 = statemachine_State10
        self.statemachine_State = statemachine_State
        self.statemachine_State20 = statemachine_State20
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def statemachine_State10(self):
        return self.__statemachine_State10

    @statemachine_State10.setter
    def statemachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State10", None)
        self.__statemachine_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition9"):
                opp_val = getattr(old_value, "statemachine_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition9"):
                opp_val = getattr(value, "statemachine_Transition9", None)
                setattr(value, "statemachine_Transition9", self)

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine"):
                opp_val = getattr(old_value, "statemachine_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine"):
                opp_val = getattr(value, "statemachine_Statemachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State4(self):
        return self.__statemachine_State4

    @statemachine_State4.setter
    def statemachine_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State4", None)
        self.__statemachine_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Command"):
                    opp_val = getattr(item, "statemachine_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Command"):
                    opp_val = getattr(item, "statemachine_Command", None)
                    
                    setattr(item, "statemachine_Command", self)
                    

    @property
    def statemachine_State20(self):
        return self.__statemachine_State20

    @statemachine_State20.setter
    def statemachine_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State20", None)
        self.__statemachine_State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StatePropertyExpression"):
                opp_val = getattr(old_value, "statemachine_StatePropertyExpression", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_StatePropertyExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StatePropertyExpression"):
                opp_val = getattr(value, "statemachine_StatePropertyExpression", None)
                setattr(value, "statemachine_StatePropertyExpression", self)

    @property
    def statemachine_State7(self):
        return self.__statemachine_State7

    @statemachine_State7.setter
    def statemachine_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State7", None)
        self.__statemachine_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition6"):
                opp_val = getattr(old_value, "statemachine_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition6"):
                opp_val = getattr(value, "statemachine_Transition6", None)
                setattr(value, "statemachine_Transition6", self)

class statemachine_Command:

    pass
class statemachine_Statemachine:

    pass