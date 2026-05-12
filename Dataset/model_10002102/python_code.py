from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Login:

    def __init__(self, username: str, password: str, user5: "User" = None):
        self.username = username
        self.password = password
        self.user5 = user5
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

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

    def __init__(self, fullname: str, password: str, userName: str, user7: "User" = None):
        self.fullname = fullname
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
    def fullname(self):
        return self.__fullname
    @fullname.setter
    def fullname(self, fullname: str):
        self.__fullname = fullname

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



class Page:

    def __init__(self, name: str, user13: "User" = None):
        self.name = name
        self.user13 = user13
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__user13", None)
        self.__user13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages12"):
                opp_val = getattr(old_value, "pages12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages12"):
                opp_val = getattr(value, "pages12", None)
                if opp_val is None:
                    setattr(value, "pages12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hashtag:

    def __init__(self, name: str, numOfRepeat: int, user11: "User" = None):
        self.name = name
        self.numOfRepeat = numOfRepeat
        self.user11 = user11
        
        pass
    @property
    def numOfRepeat(self):
        return self.__numOfRepeat
    @numOfRepeat.setter
    def numOfRepeat(self, numOfRepeat: int):
        self.__numOfRepeat = numOfRepeat

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hashtag__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashtag10"):
                opp_val = getattr(old_value, "hashtag10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashtag10"):
                opp_val = getattr(value, "hashtag10", None)
                if opp_val is None:
                    setattr(value, "hashtag10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Message:

    def __init__(self, maxChars: str, user9: "User" = None):
        self.maxChars = maxChars
        self.user9 = user9
        
        pass
    @property
    def maxChars(self):
        return self.__maxChars
    @maxChars.setter
    def maxChars(self, maxChars: str):
        self.__maxChars = maxChars

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__user9", None)
        self.__user9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message8"):
                opp_val = getattr(old_value, "message8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message8"):
                opp_val = getattr(value, "message8", None)
                if opp_val is None:
                    setattr(value, "message8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Post:

    def __init__(self, privacy: str, info: str, user3: "User" = None):
        self.privacy = privacy
        self.info = info
        self.user3 = user3
        
        pass
    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def privacy(self):
        return self.__privacy
    @privacy.setter
    def privacy(self, privacy: str):
        self.__privacy = privacy

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

    def __init__(self, username: str, password: str, user1: "User" = None):
        self.username = username
        self.password = password
        self.user1 = user1
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

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

    def __init__(self, name: str, myprofile0: "Profile" = None, post2: set["Post"] = None, login4: "Login" = None, registeration6: "Registration" = None, message8: set["Message"] = None, hashtag10: set["Hashtag"] = None, pages12: set["Page"] = None):
        self.name = name
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        self.login4 = login4
        self.registeration6 = registeration6
        self.message8 = message8 if message8 is not None else set()
        self.hashtag10 = hashtag10 if hashtag10 is not None else set()
        self.pages12 = pages12 if pages12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def message8(self):
        return self.__message8
    @message8.setter
    def message8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__message8", None)
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
    def hashtag10(self):
        return self.__hashtag10
    @hashtag10.setter
    def hashtag10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__hashtag10", None)
        self.__hashtag10 = value if value is not None else set()
        
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
    def pages12(self):
        return self.__pages12
    @pages12.setter
    def pages12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__pages12", None)
        self.__pages12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user13"):
                    opp_val = getattr(item, "user13", None)
                    
                    if opp_val == self:
                        setattr(item, "user13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user13"):
                    opp_val = getattr(item, "user13", None)
                    
                    setattr(item, "user13", self)
                    

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
                    

