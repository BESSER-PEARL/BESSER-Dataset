from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionType(Enum):
    insert = "insert"
    comment = "comment"
    copy = "copy"
    click = "click"


############################################
# Definition of Classes
############################################

class TestMM5_Action:

    def __init__(self, xpath: str, value: str, description: str, id: str, type: str, Action: "TestMM5_Test" = None, act: "TestMM5_Test" = None):
        self.xpath = xpath
        self.value = value
        self.description = description
        self.id = id
        self.type = type
        self.Action = Action
        self.act = act
        
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
    def act(self):
        return self.__act

    @act.setter
    def act(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Action__act", None)
        self.__act = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Test8"):
                opp_val = getattr(old_value, "Test8", None)
                if opp_val == self:
                    setattr(old_value, "Test8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Test8"):
                opp_val = getattr(value, "Test8", None)
                setattr(value, "Test8", self)

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "te4"):
                opp_val = getattr(old_value, "te4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "te4"):
                opp_val = getattr(value, "te4", None)
                if opp_val is None:
                    setattr(value, "te4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TestMM5_Metadata:

    def __init__(self, user: str, webpage: str, date: str, taglist: str, Metadata: "TestMM5_Test" = None, md: "TestMM5_Test" = None):
        self.user = user
        self.webpage = webpage
        self.date = date
        self.taglist = taglist
        self.Metadata = Metadata
        self.md = md
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

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
        old_value = getattr(self, f"_TestMM5_Metadata__Metadata", None)
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
        old_value = getattr(self, f"_TestMM5_Metadata__md", None)
        self.__md = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Test6"):
                opp_val = getattr(old_value, "Test6", None)
                if opp_val == self:
                    setattr(old_value, "Test6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Test6"):
                opp_val = getattr(value, "Test6", None)
                setattr(value, "Test6", self)

class TestMM5_Test:

    def __init__(self, id: str, Test: "TestMM5_TestSet" = None, ts: "TestMM5_TestSet" = None, te: "TestMM5_Metadata" = None, te4: set["TestMM5_Action"] = None, Test6: "TestMM5_Metadata" = None, Test8: "TestMM5_Action" = None):
        self.id = id
        self.Test = Test
        self.ts = ts
        self.te = te
        self.te4 = te4 if te4 is not None else set()
        self.Test6 = Test6
        self.Test8 = Test8
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def te4(self):
        return self.__te4

    @te4.setter
    def te4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Test__te4", None)
        self.__te4 = value if value is not None else set()
        
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
    def Test8(self):
        return self.__Test8

    @Test8.setter
    def Test8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Test__Test8", None)
        self.__Test8 = value
        
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
    def ts(self):
        return self.__ts

    @ts.setter
    def ts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Test__ts", None)
        self.__ts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestSet"):
                opp_val = getattr(old_value, "TestSet", None)
                if opp_val == self:
                    setattr(old_value, "TestSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestSet"):
                opp_val = getattr(value, "TestSet", None)
                setattr(value, "TestSet", self)

    @property
    def Test(self):
        return self.__Test

    @Test.setter
    def Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Test__Test", None)
        self.__Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tst"):
                opp_val = getattr(old_value, "tst", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tst"):
                opp_val = getattr(value, "tst", None)
                if opp_val is None:
                    setattr(value, "tst", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Test6(self):
        return self.__Test6

    @Test6.setter
    def Test6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Test__Test6", None)
        self.__Test6 = value
        
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
    def te(self):
        return self.__te

    @te.setter
    def te(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_Test__te", None)
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

class TestMM5_TestSet:

    def __init__(self, name: str, tst: set["TestMM5_Test"] = None, TestSet: "TestMM5_Test" = None):
        self.name = name
        self.tst = tst if tst is not None else set()
        self.TestSet = TestSet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tst(self):
        return self.__tst

    @tst.setter
    def tst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_TestSet__tst", None)
        self.__tst = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Test"):
                    opp_val = getattr(item, "Test", None)
                    
                    if opp_val == self:
                        setattr(item, "Test", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Test"):
                    opp_val = getattr(item, "Test", None)
                    
                    setattr(item, "Test", self)
                    

    @property
    def TestSet(self):
        return self.__TestSet

    @TestSet.setter
    def TestSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM5_TestSet__TestSet", None)
        self.__TestSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ts"):
                opp_val = getattr(old_value, "ts", None)
                if opp_val == self:
                    setattr(old_value, "ts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ts"):
                opp_val = getattr(value, "ts", None)
                setattr(value, "ts", self)
