from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class testpackage_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class testpackage_Group(NamedElement):

    def __init__(self, testpackage_Group: set["testpackage_User"] = None):
        self.testpackage_Group = testpackage_Group if testpackage_Group is not None else set()
        
    @property
    def testpackage_Group(self):
        return self.__testpackage_Group

    @testpackage_Group.setter
    def testpackage_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testpackage_Group__testpackage_Group", None)
        self.__testpackage_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testpackage_User"):
                    opp_val = getattr(item, "testpackage_User", None)
                    
                    if opp_val == self:
                        setattr(item, "testpackage_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testpackage_User"):
                    opp_val = getattr(item, "testpackage_User", None)
                    
                    setattr(item, "testpackage_User", self)
                    

    def isMember(self, user: str) -> bool:
        # TODO: Implement isMember method
        pass

class testpackage_User(NamedElement):

    def __init__(self, password: str, testpackage_User: "testpackage_Group" = None):
        self.password = password
        self.testpackage_User = testpackage_User
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def testpackage_User(self):
        return self.__testpackage_User

    @testpackage_User.setter
    def testpackage_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testpackage_User__testpackage_User", None)
        self.__testpackage_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testpackage_Group"):
                opp_val = getattr(old_value, "testpackage_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testpackage_Group"):
                opp_val = getattr(value, "testpackage_Group", None)
                if opp_val is None:
                    setattr(value, "testpackage_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
