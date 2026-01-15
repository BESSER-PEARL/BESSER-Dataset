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

class TestMM_Action:

    def __init__(self, id: str, type: str, xpath: str, value: str, description: str, Action: "TestMM_Test" = None, act: "TestMM_Test" = None):
        self.id = id
        self.type = type
        self.xpath = xpath
        self.value = value
        self.description = description
        self.Action = Action
        self.act = act
        
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
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def act(self):
        return self.__act

    @act.setter
    def act(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Action__act", None)
        self.__act = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Test5"):
                opp_val = getattr(old_value, "Test5", None)
                if opp_val == self:
                    setattr(old_value, "Test5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Test5"):
                opp_val = getattr(value, "Test5", None)
                setattr(value, "Test5", self)

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "te2"):
                opp_val = getattr(old_value, "te2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "te2"):
                opp_val = getattr(value, "te2", None)
                if opp_val is None:
                    setattr(value, "te2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TestMM_Metadata:

    def __init__(self, user: str, webpage: str, date: str, taglist: str, Metadata: "TestMM_Test" = None, md: "TestMM_Test" = None):
        self.user = user
        self.webpage = webpage
        self.date = date
        self.taglist = taglist
        self.Metadata = Metadata
        self.md = md
        
    @property
    def taglist(self) -> str:
        return self.__taglist

    @taglist.setter
    def taglist(self, taglist: str):
        self.__taglist = taglist

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def webpage(self) -> str:
        return self.__webpage

    @webpage.setter
    def webpage(self, webpage: str):
        self.__webpage = webpage

    @property
    def Metadata(self):
        return self.__Metadata

    @Metadata.setter
    def Metadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Metadata__Metadata", None)
        self.__Metadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "te"):
                opp_val = getattr(old_value, "te", None)
                if opp_val == self:
                    setattr(old_value, "te", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "te"):
                opp_val = getattr(value, "te", None)
                setattr(value, "te", self)

    @property
    def md(self):
        return self.__md

    @md.setter
    def md(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Metadata__md", None)
        self.__md = value
        
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

class TestMM_Test:

    def __init__(self, id: str, te: "TestMM_Metadata" = None, te2: set["TestMM_Action"] = None, Test5: "TestMM_Action" = None, Test: "TestMM_Metadata" = None):
        self.id = id
        self.te = te
        self.te2 = te2 if te2 is not None else set()
        self.Test5 = Test5
        self.Test = Test
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def te(self):
        return self.__te

    @te.setter
    def te(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Test__te", None)
        self.__te = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metadata"):
                opp_val = getattr(old_value, "Metadata", None)
                if opp_val == self:
                    setattr(old_value, "Metadata", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metadata"):
                opp_val = getattr(value, "Metadata", None)
                setattr(value, "Metadata", self)

    @property
    def Test(self):
        return self.__Test

    @Test.setter
    def Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Test__Test", None)
        self.__Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "md"):
                opp_val = getattr(old_value, "md", None)
                if opp_val == self:
                    setattr(old_value, "md", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "md"):
                opp_val = getattr(value, "md", None)
                setattr(value, "md", self)

    @property
    def te2(self):
        return self.__te2

    @te2.setter
    def te2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Test__te2", None)
        self.__te2 = value if value is not None else set()
        
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
                    

    @property
    def Test5(self):
        return self.__Test5

    @Test5.setter
    def Test5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM_Test__Test5", None)
        self.__Test5 = value
        
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
