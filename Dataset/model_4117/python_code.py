from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wh_Command:

    def __init__(self, cmd: str, wh_Command: "wh_Commands" = None):
        self.cmd = cmd
        self.wh_Command = wh_Command
        
    @property
    def cmd(self) -> str:
        return self.__cmd

    @cmd.setter
    def cmd(self, cmd: str):
        self.__cmd = cmd

    @property
    def wh_Command(self):
        return self.__wh_Command

    @wh_Command.setter
    def wh_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Command__wh_Command", None)
        self.__wh_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Commands6"):
                opp_val = getattr(old_value, "wh_Commands6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Commands6"):
                opp_val = getattr(value, "wh_Commands6", None)
                if opp_val is None:
                    setattr(value, "wh_Commands6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wh_Commands:

    pass
class wh_Definition:

    def __init__(self, input: str, output: str, wh_Definition: "wh_Program" = None, wh_Definition4: "wh_Commands" = None):
        self.input = input
        self.output = output
        self.wh_Definition = wh_Definition
        self.wh_Definition4 = wh_Definition4
        
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
    def wh_Definition4(self):
        return self.__wh_Definition4

    @wh_Definition4.setter
    def wh_Definition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Definition__wh_Definition4", None)
        self.__wh_Definition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Commands"):
                opp_val = getattr(old_value, "wh_Commands", None)
                if opp_val == self:
                    setattr(old_value, "wh_Commands", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Commands"):
                opp_val = getattr(value, "wh_Commands", None)
                setattr(value, "wh_Commands", self)

    @property
    def wh_Definition(self):
        return self.__wh_Definition

    @wh_Definition.setter
    def wh_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Definition__wh_Definition", None)
        self.__wh_Definition = value
        
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

    def __init__(self, name: str, wh_Program: "wh_Wh" = None, wh_Program2: "wh_Definition" = None):
        self.name = name
        self.wh_Program = wh_Program
        self.wh_Program2 = wh_Program2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wh_Program2(self):
        return self.__wh_Program2

    @wh_Program2.setter
    def wh_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Program__wh_Program2", None)
        self.__wh_Program2 = value
        
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
    def wh_Program(self):
        return self.__wh_Program

    @wh_Program.setter
    def wh_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Program__wh_Program", None)
        self.__wh_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Wh"):
                opp_val = getattr(old_value, "wh_Wh", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Wh"):
                opp_val = getattr(value, "wh_Wh", None)
                if opp_val is None:
                    setattr(value, "wh_Wh", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wh_Wh:

    pass