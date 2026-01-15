from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TestMM2_Test:

    def __init__(self, id: str, te: "TestMM2_Metadata" = None, Test: "TestMM2_Metadata" = None):
        self.id = id
        self.te = te
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
        old_value = getattr(self, f"_TestMM2_Test__Test", None)
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
    def te(self):
        return self.__te

    @te.setter
    def te(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM2_Test__te", None)
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

class TestMM2_Metadata:

    def __init__(self, user: str, webpage: str, date: str, taglist: str, Metadata: "TestMM2_Test" = None, md: "TestMM2_Test" = None):
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
    def webpage(self) -> str:
        return self.__webpage

    @webpage.setter
    def webpage(self, webpage: str):
        self.__webpage = webpage

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def md(self):
        return self.__md

    @md.setter
    def md(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM2_Metadata__md", None)
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

    @property
    def Metadata(self):
        return self.__Metadata

    @Metadata.setter
    def Metadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMM2_Metadata__Metadata", None)
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
