from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Login:

    def __init__(self, username: str, password: str, user3: "User" = None):
        self.username = username
        self.password = password
        self.user3 = user3
        
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
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login2"):
                opp_val = getattr(old_value, "login2", None)
                if opp_val == self:
                    setattr(old_value, "login2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login2"):
                opp_val = getattr(value, "login2", None)
                setattr(value, "login2", self)



class Registration:

    def __init__(self, password: str, fname: str, userName: str, lname: str, user7: "User" = None):
        self.password = password
        self.fname = fname
        self.userName = userName
        self.lname = lname
        self.user7 = user7
        
        pass
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

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



class Event:

    def __init__(self, name: str, location: str, time: str, user9: "User" = None):
        self.name = name
        self.location = location
        self.time = time
        self.user9 = user9
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__user9", None)
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



class Notification:

    def __init__(self, update: str, user11: "User" = None):
        self.update = update
        self.user11 = user11
        
        pass
    @property
    def update(self):
        return self.__update
    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Notification__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "friends10"):
                opp_val = getattr(old_value, "friends10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "friends10"):
                opp_val = getattr(value, "friends10", None)
                if opp_val is None:
                    setattr(value, "friends10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Interest:

    def __init__(self, name: str, discription: str, user5: "User" = None, pages12: set["Post"] = None):
        self.name = name
        self.discription = discription
        self.user5 = user5
        self.pages12 = pages12 if pages12 is not None else set()
        
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
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Interest__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group4"):
                opp_val = getattr(old_value, "group4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group4"):
                opp_val = getattr(value, "group4", None)
                if opp_val is None:
                    setattr(value, "group4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pages12(self):
        return self.__pages12
    @pages12.setter
    def pages12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Interest__pages12", None)
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
                    



class Post:

    def __init__(self, info: str, user13: "Interest" = None):
        self.info = info
        self.user13 = user13
        
        pass
    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__user13", None)
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



class Profile:

    def __init__(self, username: str, password: str, interests: str, user1: "User" = None):
        self.username = username
        self.password = password
        self.interests = interests
        self.user1 = user1
        
        pass
    @property
    def interests(self):
        return self.__interests
    @interests.setter
    def interests(self, interests: str):
        self.__interests = interests

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

    def __init__(self, fname: str, lname: str, username: str, myprofile0: "Profile" = None, login2: "Login" = None, group4: set["Interest"] = None, registeration6: "Registration" = None, message8: set["Event"] = None, friends10: set["Notification"] = None):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.myprofile0 = myprofile0
        self.login2 = login2
        self.group4 = group4 if group4 is not None else set()
        self.registeration6 = registeration6
        self.message8 = message8 if message8 is not None else set()
        self.friends10 = friends10 if friends10 is not None else set()
        
        pass
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def login2(self):
        return self.__login2
    @login2.setter
    def login2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__login2", None)
        self.__login2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user3"):
                opp_val = getattr(old_value, "user3", None)
                if opp_val == self:
                    setattr(old_value, "user3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user3"):
                opp_val = getattr(value, "user3", None)
                setattr(value, "user3", self)

    @property
    def friends10(self):
        return self.__friends10
    @friends10.setter
    def friends10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__friends10", None)
        self.__friends10 = value if value is not None else set()
        
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
    def group4(self):
        return self.__group4
    @group4.setter
    def group4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__group4", None)
        self.__group4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val == self:
                        setattr(item, "user5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    setattr(item, "user5", self)
                    

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

