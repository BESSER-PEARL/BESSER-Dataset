from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class Search:

    pass


class Item:

    pass


class Login:

    def __init__(self, username: str, password: str, user5: "User" = None):
        self.username = username
        self.password = password
        self.user5 = user5
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login4"):
                opp_val = getattr(old_value, "login4", None)
                if opp_val == self:
                    setattr(old_value, "login4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login4"):
                opp_val = getattr(value, "login4", None)
                setattr(value, "login4", self)



class Registration:

    def __init__(self, name: str, username: str, password: str, userName: str, user7: "User" = None):
        self.name = name
        self.username = username
        self.password = password
        self.userName = userName
        self.user7 = user7
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeration6"):
                opp_val = getattr(old_value, "registeration6", None)
                if opp_val == self:
                    setattr(old_value, "registeration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeration6"):
                opp_val = getattr(value, "registeration6", None)
                setattr(value, "registeration6", self)



class Hashtag:

    def __init__(self, name: str, _113: "Item" = None):
        self.name = name
        self._113 = _113
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def _113(self):
        return self.___113
    @_113.setter
    def _113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hashtag___113", None)
        self.___113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item_Hashtag_012"):
                opp_val = getattr(old_value, "Item_Hashtag_012", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item_Hashtag_012"):
                opp_val = getattr(value, "Item_Hashtag_012", None)
                if opp_val is None:
                    setattr(value, "Item_Hashtag_012", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Comment:

    pass


class Post:

    def __init__(self, type: str, user3: "User" = None):
        self.type = type
        self.user3 = user3
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post2"):
                opp_val = getattr(old_value, "post2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post2"):
                opp_val = getattr(value, "post2", None)
                if opp_val is None:
                    setattr(value, "post2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Profile:

    def __init__(self, username: str, user1: "User" = None):
        self.username = username
        self.user1 = user1
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myprofile0"):
                opp_val = getattr(old_value, "myprofile0", None)
                if opp_val == self:
                    setattr(old_value, "myprofile0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myprofile0"):
                opp_val = getattr(value, "myprofile0", None)
                setattr(value, "myprofile0", self)



class User:

    def __init__(self, name: str, registeration6: "Registration" = None, pages10: set["Item"] = None, myprofile0: "Profile" = None, post2: set["Post"] = None, login4: "Login" = None):
        self.name = name
        self.registeration6 = registeration6
        self.pages10 = pages10 if pages10 is not None else set()
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        self.login4 = login4
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myprofile0(self):
        return self.__myprofile0
    @myprofile0.setter
    def myprofile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__myprofile0", None)
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
    def pages10(self):
        return self.__pages10
    @pages10.setter
    def pages10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__pages10", None)
        self.__pages10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user11"):
                    opp_val = getattr(item, "user11", None)
                    
                    if opp_val == self:
                        setattr(item, "user11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user11"):
                    opp_val = getattr(item, "user11", None)
                    
                    setattr(item, "user11", self)
                    

    @property
    def post2(self):
        return self.__post2
    @post2.setter
    def post2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__post2", None)
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
    def registeration6(self):
        return self.__registeration6
    @registeration6.setter
    def registeration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__registeration6", None)
        self.__registeration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user7"):
                opp_val = getattr(old_value, "user7", None)
                if opp_val == self:
                    setattr(old_value, "user7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user7"):
                opp_val = getattr(value, "user7", None)
                setattr(value, "user7", self)

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__login4", None)
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

