from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Message:

    pass


class Group:

    pass


class Post:

    pass


class Profile:

    pass


class Login:

    pass


class Friend:

    pass


class ListaEncadeada:

    def __init__(self, attribute: str, myprofile0: "Profile" = None, post2: set["Post"] = None, login4: "Login" = None, group6: set["Group"] = None, message8: set["Message"] = None):
        self.attribute = attribute
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        self.login4 = login4
        self.group6 = group6 if group6 is not None else set()
        self.message8 = message8 if message8 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ListaEncadeada__login4", None)
        self.__login4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user5"):
                opp_val = getattr(old_value, "user5", None)
                if opp_val == self:
                    setattr(old_value, "user5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user5"):
                opp_val = getattr(value, "user5", None)
                setattr(value, "user5", self)

    @property
    def post2(self):
        return self.__post2
    @post2.setter
    def post2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ListaEncadeada__post2", None)
        self.__post2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

    @property
    def message8(self):
        return self.__message8
    @message8.setter
    def message8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ListaEncadeada__message8", None)
        self.__message8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    if opp_val == self:
                        setattr(item, "user9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    setattr(item, "user9", self)
                    

    @property
    def myprofile0(self):
        return self.__myprofile0
    @myprofile0.setter
    def myprofile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ListaEncadeada__myprofile0", None)
        self.__myprofile0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def group6(self):
        return self.__group6
    @group6.setter
    def group6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ListaEncadeada__group6", None)
        self.__group6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    if opp_val == self:
                        setattr(item, "user7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    setattr(item, "user7", self)
                    

