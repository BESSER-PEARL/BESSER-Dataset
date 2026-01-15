from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wh_Output:

    def __init__(self, variable: str, wh_Output: "wh_Definition" = None, wh_Output19: "wh_Output" = None, wh_Output17: "wh_Output" = None):
        self.variable = variable
        self.wh_Output = wh_Output
        self.wh_Output19 = wh_Output19
        self.wh_Output17 = wh_Output17
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def wh_Output(self):
        return self.__wh_Output

    @wh_Output.setter
    def wh_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Output__wh_Output", None)
        self.__wh_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition13"):
                opp_val = getattr(old_value, "wh_Definition13", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition13"):
                opp_val = getattr(value, "wh_Definition13", None)
                setattr(value, "wh_Definition13", self)

    @property
    def wh_Output19(self):
        return self.__wh_Output19

    @wh_Output19.setter
    def wh_Output19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Output__wh_Output19", None)
        self.__wh_Output19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Output17"):
                opp_val = getattr(old_value, "wh_Output17", None)
                if opp_val == self:
                    setattr(old_value, "wh_Output17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Output17"):
                opp_val = getattr(value, "wh_Output17", None)
                setattr(value, "wh_Output17", self)

    @property
    def wh_Output17(self):
        return self.__wh_Output17

    @wh_Output17.setter
    def wh_Output17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Output__wh_Output17", None)
        self.__wh_Output17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Output19"):
                opp_val = getattr(old_value, "wh_Output19", None)
                if opp_val == self:
                    setattr(old_value, "wh_Output19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Output19"):
                opp_val = getattr(value, "wh_Output19", None)
                setattr(value, "wh_Output19", self)

class wh_Commands:

    def __init__(self, command: str, wh_Commands: "wh_Definition" = None, wh_Commands22: "wh_Commands" = None, wh_Commands20: "wh_Commands" = None):
        self.command = command
        self.wh_Commands = wh_Commands
        self.wh_Commands22 = wh_Commands22
        self.wh_Commands20 = wh_Commands20
        
    @property
    def command(self) -> str:
        return self.__command

    @command.setter
    def command(self, command: str):
        self.__command = command

    @property
    def wh_Commands22(self):
        return self.__wh_Commands22

    @wh_Commands22.setter
    def wh_Commands22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Commands__wh_Commands22", None)
        self.__wh_Commands22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Commands20"):
                opp_val = getattr(old_value, "wh_Commands20", None)
                if opp_val == self:
                    setattr(old_value, "wh_Commands20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Commands20"):
                opp_val = getattr(value, "wh_Commands20", None)
                setattr(value, "wh_Commands20", self)

    @property
    def wh_Commands(self):
        return self.__wh_Commands

    @wh_Commands.setter
    def wh_Commands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Commands__wh_Commands", None)
        self.__wh_Commands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition11"):
                opp_val = getattr(old_value, "wh_Definition11", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition11"):
                opp_val = getattr(value, "wh_Definition11", None)
                setattr(value, "wh_Definition11", self)

    @property
    def wh_Commands20(self):
        return self.__wh_Commands20

    @wh_Commands20.setter
    def wh_Commands20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Commands__wh_Commands20", None)
        self.__wh_Commands20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Commands22"):
                opp_val = getattr(old_value, "wh_Commands22", None)
                if opp_val == self:
                    setattr(old_value, "wh_Commands22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Commands22"):
                opp_val = getattr(value, "wh_Commands22", None)
                setattr(value, "wh_Commands22", self)

class wh_Input:

    def __init__(self, variable: str, wh_Input: "wh_Definition" = None, wh_Input16: "wh_Input" = None, wh_Input14: "wh_Input" = None):
        self.variable = variable
        self.wh_Input = wh_Input
        self.wh_Input16 = wh_Input16
        self.wh_Input14 = wh_Input14
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def wh_Input(self):
        return self.__wh_Input

    @wh_Input.setter
    def wh_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Input__wh_Input", None)
        self.__wh_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition9"):
                opp_val = getattr(old_value, "wh_Definition9", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition9"):
                opp_val = getattr(value, "wh_Definition9", None)
                setattr(value, "wh_Definition9", self)

    @property
    def wh_Input16(self):
        return self.__wh_Input16

    @wh_Input16.setter
    def wh_Input16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Input__wh_Input16", None)
        self.__wh_Input16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Input14"):
                opp_val = getattr(old_value, "wh_Input14", None)
                if opp_val == self:
                    setattr(old_value, "wh_Input14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Input14"):
                opp_val = getattr(value, "wh_Input14", None)
                setattr(value, "wh_Input14", self)

    @property
    def wh_Input14(self):
        return self.__wh_Input14

    @wh_Input14.setter
    def wh_Input14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Input__wh_Input14", None)
        self.__wh_Input14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Input16"):
                opp_val = getattr(old_value, "wh_Input16", None)
                if opp_val == self:
                    setattr(old_value, "wh_Input16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Input16"):
                opp_val = getattr(value, "wh_Input16", None)
                setattr(value, "wh_Input16", self)

class wh_Definition:

    pass
class wh_Function:

    def __init__(self, name: str, wh_Function: "wh_Program" = None, wh_Function7: "wh_Definition" = None):
        self.name = name
        self.wh_Function = wh_Function
        self.wh_Function7 = wh_Function7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wh_Function7(self):
        return self.__wh_Function7

    @wh_Function7.setter
    def wh_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Function__wh_Function7", None)
        self.__wh_Function7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition"):
                opp_val = getattr(old_value, "wh_Definition", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition"):
                opp_val = getattr(value, "wh_Definition", None)
                setattr(value, "wh_Definition", self)

    @property
    def wh_Function(self):
        return self.__wh_Function

    @wh_Function.setter
    def wh_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Function__wh_Function", None)
        self.__wh_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Program2"):
                opp_val = getattr(old_value, "wh_Program2", None)
                if opp_val == self:
                    setattr(old_value, "wh_Program2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Program2"):
                opp_val = getattr(value, "wh_Program2", None)
                setattr(value, "wh_Program2", self)

class wh_Program:

    pass
class wh_Model:

    pass