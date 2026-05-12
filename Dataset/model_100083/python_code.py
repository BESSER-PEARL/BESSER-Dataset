from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Element:

    pass
class Comment:

    pass
class Make_Makefile:

    def __init__(self, name: str, Make_Makefile2: set["Element"] = None, Make_Makefile: "Comment" = None):
        self.name = name
        self.Make_Makefile2 = Make_Makefile2 if Make_Makefile2 is not None else set()
        self.Make_Makefile = Make_Makefile
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Make_Makefile(self):
        return self.__Make_Makefile

    @Make_Makefile.setter
    def Make_Makefile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Make_Makefile__Make_Makefile", None)
        self.__Make_Makefile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Comment"):
                opp_val = getattr(old_value, "Comment", None)
                if opp_val == self:
                    setattr(old_value, "Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Comment"):
                opp_val = getattr(value, "Comment", None)
                setattr(value, "Comment", self)

    @property
    def Make_Makefile2(self):
        return self.__Make_Makefile2

    @Make_Makefile2.setter
    def Make_Makefile2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Make_Makefile__Make_Makefile2", None)
        self.__Make_Makefile2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class Make_Dependency(ABC):

    pass
class Make_Comment:

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class Rule:

    pass
class Make_ShellLine:

    def __init__(self, command: str, display: str, shellLines: "Rule" = None):
        self.command = command
        self.display = display
        self.shellLines = shellLines
        
        pass
    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, display: str):
        self.__display = display


    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, command: str):
        self.__command = command


    @property
    def shellLines(self):
        return self.__shellLines

    @shellLines.setter
    def shellLines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Make_ShellLine__shellLines", None)
        self.__shellLines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rule"):
                opp_val = getattr(old_value, "Rule", None)
                if opp_val == self:
                    setattr(old_value, "Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rule"):
                opp_val = getattr(value, "Rule", None)
                setattr(value, "Rule", self)

class Make_Macro(Element):

    def __init__(self, value: str, Element: "Make_Makefile" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ShellLine:

    pass
class Dependency:

    pass
class Make_FileDep(Dependency):

    def __init__(self, name: str, Dependency: "Make_Rule" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Make_RuleDep(Dependency):

    pass
class Make_Rule(Element):

    pass
class Make_Element(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

