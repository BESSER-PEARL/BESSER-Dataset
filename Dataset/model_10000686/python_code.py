from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


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

    def __init__(self, fname: str, lname: str, password: str, userName: str, user9: "User" = None):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.userName = userName
        self.user9 = user9
        
        pass
    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

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
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__user9", None)
        self.__user9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeration8"):
                opp_val = getattr(old_value, "registeration8", None)
                if opp_val == self:
                    setattr(old_value, "registeration8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeration8"):
                opp_val = getattr(value, "registeration8", None)
                setattr(value, "registeration8", self)



class Page:

    def __init__(self, name: str, user15: "User" = None):
        self.name = name
        self.user15 = user15
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user15(self):
        return self.__user15
    @user15.setter
    def user15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__user15", None)
        self.__user15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages14"):
                opp_val = getattr(old_value, "pages14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages14"):
                opp_val = getattr(value, "pages14", None)
                if opp_val is None:
                    setattr(value, "pages14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Friend:

    pass


class Message:

    def __init__(self, maxChars: str, user11: "User" = None):
        self.maxChars = maxChars
        self.user11 = user11
        
        pass
    @property
    def maxChars(self):
        return self.__maxChars
    @maxChars.setter
    def maxChars(self, maxChars: str):
        self.__maxChars = maxChars

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message10"):
                opp_val = getattr(old_value, "message10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message10"):
                opp_val = getattr(value, "message10", None)
                if opp_val is None:
                    setattr(value, "message10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Group:

    def __init__(self, name: str, discription: str, user7: "User" = None):
        self.name = name
        self.discription = discription
        self.user7 = user7
        
        pass
    @property
    def discription(self):
        return self.__discription
    @discription.setter
    def discription(self, discription: str):
        self.__discription = discription

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
        old_value = getattr(self, f"_Group__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group6"):
                opp_val = getattr(old_value, "group6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group6"):
                opp_val = getattr(value, "group6", None)
                if opp_val is None:
                    setattr(value, "group6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Post:

    def __init__(self, privacy: str, info: str, user3: "User" = None):
        self.privacy = privacy
        self.info = info
        self.user3 = user3
        
        pass
    @property
    def privacy(self):
        return self.__privacy
    @privacy.setter
    def privacy(self, privacy: str):
        self.__privacy = privacy

    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self, info: str):
        self.__info = info

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

    def __init__(self, username: str, password: str, about: str, user1: "User" = None):
        self.username = username
        self.password = password
        self.about = about
        self.user1 = user1
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def about(self):
        return self.__about
    @about.setter
    def about(self, about: str):
        self.__about = about

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

    def __init__(self, name: str, group6: set["Group"] = None, registeration8: "Registration" = None, message10: set["Message"] = None, friends12: set["Friend"] = None, pages14: set["Page"] = None, myprofile0: "Profile" = None, post2: set["Post"] = None, login4: "Login" = None):
        self.name = name
        self.group6 = group6 if group6 is not None else set()
        self.registeration8 = registeration8
        self.message10 = message10 if message10 is not None else set()
        self.friends12 = friends12 if friends12 is not None else set()
        self.pages14 = pages14 if pages14 is not None else set()
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
    def friends12(self):
        return self.__friends12
    @friends12.setter
    def friends12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__friends12", None)
        self.__friends12 = value if value is not None else set()
        
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
    def pages14(self):
        return self.__pages14
    @pages14.setter
    def pages14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__pages14", None)
        self.__pages14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user15"):
                    opp_val = getattr(item, "user15", None)
                    
                    if opp_val == self:
                        setattr(item, "user15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user15"):
                    opp_val = getattr(item, "user15", None)
                    
                    setattr(item, "user15", self)
                    

    @property
    def message10(self):
        return self.__message10
    @message10.setter
    def message10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__message10", None)
        self.__message10 = value if value is not None else set()
        
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
    def group6(self):
        return self.__group6
    @group6.setter
    def group6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__group6", None)
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
    def registeration8(self):
        return self.__registeration8
    @registeration8.setter
    def registeration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__registeration8", None)
        self.__registeration8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user9"):
                opp_val = getattr(old_value, "user9", None)
                if opp_val == self:
                    setattr(old_value, "user9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user9"):
                opp_val = getattr(value, "user9", None)
                setattr(value, "user9", self)

