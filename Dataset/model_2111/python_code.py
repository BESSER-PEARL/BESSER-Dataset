from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionType(Enum):
    comment = "comment"
    copy = "copy"
    click = "click"
    insert = "insert"


############################################
# Definition of Classes
############################################

class TestMM1_Test:

    def __init__(self, id: str, te: set["TestMM1_Action"] = None, Test: "TestMM1_Action" = None):
        self.id = id
        self.te = te if te is not None else set()
        self.Test = Test
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Test(self):
        return self.__Test

    @Test.setter
    def Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM1_Test__Test", None)
        self.__Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "act"):
                opp_val = getattr(old_value, "act", None)
                if opp_val == self:
                    setattr(old_value, "act", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "act"):
                opp_val = getattr(value, "act", None)
                setattr(value, "act", self)

    @property
    def te(self):
        return self.__te

    @te.setter
    def te(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM1_Test__te", None)
        self.__te = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

class TestMM1_Action:

    def __init__(self, id: str, type: str, xpath: str, value: str, description: str, Action: "TestMM1_Test" = None, act: "TestMM1_Test" = None):
        self.id = id
        self.type = type
        self.xpath = xpath
        self.value = value
        self.description = description
        self.Action = Action
        self.act = act
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def xpath(self) -> str:
        return self.__xpath

    @xpath.setter
    def xpath(self, xpath: str):
        self.__xpath = xpath

    @property
    def act(self):
        return self.__act

    @act.setter
    def act(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM1_Action__act", None)
        self.__act = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Test"):
                opp_val = getattr(old_value, "Test", None)
                if opp_val == self:
                    setattr(old_value, "Test", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Test"):
                opp_val = getattr(value, "Test", None)
                setattr(value, "Test", self)

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM1_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "te"):
                opp_val = getattr(old_value, "te", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "te"):
                opp_val = getattr(value, "te", None)
                if opp_val is None:
                    setattr(value, "te", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
