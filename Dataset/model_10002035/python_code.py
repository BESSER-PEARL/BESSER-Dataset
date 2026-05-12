from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
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



class Registration:

    def __init__(self, userName: str, fname: str, lname: str, password: secret, user7: "User" = None):
        self.userName = userName
        self.fname = fname
        self.lname = lname
        self.password = password
        self.user7 = user7
        
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
    def password(self, password: secret):
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



class secret:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class public:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Others:

    def __init__(self, name: str, discription: str, user5: "User" = None):
        self.name = name
        self.discription = discription
        self.user5 = user5
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def discription(self):
        return self.__discription
    @discription.setter
    def discription(self, discription: str):
        self.__discription = discription

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Others__user5", None)
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
    def about(self):
        return self.__about
    @about.setter
    def about(self, about: str):
        self.__about = about

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

    def __init__(self, name: str, myprofile0: "Profile" = None, post2: set["Post"] = None, group4: set["Others"] = None, registeration6: "Registration" = None):
        self.name = name
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        self.group4 = group4 if group4 is not None else set()
        self.registeration6 = registeration6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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

