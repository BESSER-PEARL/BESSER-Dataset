from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Page:

    def __init__(self, ID_Page: int, Name: str, Description: str, ID_User: int, user3: "User" = None, post8: set["Post"] = None):
        self.ID_Page = ID_Page
        self.Name = Name
        self.Description = Description
        self.ID_User = ID_User
        self.user3 = user3
        self.post8 = post8 if post8 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID_User(self):
        return self.__ID_User
    @ID_User.setter
    def ID_User(self, ID_User: int):
        self.__ID_User = ID_User

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def ID_Page(self):
        return self.__ID_Page
    @ID_Page.setter
    def ID_Page(self, ID_Page: int):
        self.__ID_Page = ID_Page

    @property
    def post8(self):
        return self.__post8
    @post8.setter
    def post8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__post8", None)
        self.__post8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "page9"):
                    opp_val = getattr(item, "page9", None)
                    
                    if opp_val == self:
                        setattr(item, "page9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "page9"):
                    opp_val = getattr(item, "page9", None)
                    
                    setattr(item, "page9", self)
                    

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page2"):
                opp_val = getattr(old_value, "page2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page2"):
                opp_val = getattr(value, "page2", None)
                if opp_val is None:
                    setattr(value, "page2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Message:

    def __init__(self, ID_Message: int, Max_Chars: str, Mail: str, ID_User: int, user5: "User" = None):
        self.ID_Message = ID_Message
        self.Max_Chars = Max_Chars
        self.Mail = Mail
        self.ID_User = ID_User
        self.user5 = user5
        
        pass
    @property
    def ID_User(self):
        return self.__ID_User
    @ID_User.setter
    def ID_User(self, ID_User: int):
        self.__ID_User = ID_User

    @property
    def ID_Message(self):
        return self.__ID_Message
    @ID_Message.setter
    def ID_Message(self, ID_Message: int):
        self.__ID_Message = ID_Message

    @property
    def Max_Chars(self):
        return self.__Max_Chars
    @Max_Chars.setter
    def Max_Chars(self, Max_Chars: str):
        self.__Max_Chars = Max_Chars

    @property
    def Mail(self):
        return self.__Mail
    @Mail.setter
    def Mail(self, Mail: str):
        self.__Mail = Mail

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message4"):
                opp_val = getattr(old_value, "message4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message4"):
                opp_val = getattr(value, "message4", None)
                if opp_val is None:
                    setattr(value, "message4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Group:

    def __init__(self, ID_Group: int, Name: str, Description: str, ID_User: int, user7: "User" = None):
        self.ID_Group = ID_Group
        self.Name = Name
        self.Description = Description
        self.ID_User = ID_User
        self.user7 = user7
        
        pass
    @property
    def ID_Group(self):
        return self.__ID_Group
    @ID_Group.setter
    def ID_Group(self, ID_Group: int):
        self.__ID_Group = ID_Group

    @property
    def ID_User(self):
        return self.__ID_User
    @ID_User.setter
    def ID_User(self, ID_User: int):
        self.__ID_User = ID_User

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

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

    def __init__(self, ID_Post: int, Privacy: str, Info: str, Mail: str, ID_Page: int, page9: "Page" = None):
        self.ID_Post = ID_Post
        self.Privacy = Privacy
        self.Info = Info
        self.Mail = Mail
        self.ID_Page = ID_Page
        self.page9 = page9
        
        pass
    @property
    def Info(self):
        return self.__Info
    @Info.setter
    def Info(self, Info: str):
        self.__Info = Info

    @property
    def ID_Page(self):
        return self.__ID_Page
    @ID_Page.setter
    def ID_Page(self, ID_Page: int):
        self.__ID_Page = ID_Page

    @property
    def Mail(self):
        return self.__Mail
    @Mail.setter
    def Mail(self, Mail: str):
        self.__Mail = Mail

    @property
    def ID_Post(self):
        return self.__ID_Post
    @ID_Post.setter
    def ID_Post(self, ID_Post: int):
        self.__ID_Post = ID_Post

    @property
    def Privacy(self):
        return self.__Privacy
    @Privacy.setter
    def Privacy(self, Privacy: str):
        self.__Privacy = Privacy

    @property
    def page9(self):
        return self.__page9
    @page9.setter
    def page9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__page9", None)
        self.__page9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post8"):
                opp_val = getattr(old_value, "post8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post8"):
                opp_val = getattr(value, "post8", None)
                if opp_val is None:
                    setattr(value, "post8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, ID_User: int, Name: str, Fist_Name: str, Mail: str, profile1: "Profile" = None, page2: set["Page"] = None, message4: set["Message"] = None, group6: set["Group"] = None):
        self.ID_User = ID_User
        self.Name = Name
        self.Fist_Name = Fist_Name
        self.Mail = Mail
        self.profile1 = profile1
        self.page2 = page2 if page2 is not None else set()
        self.message4 = message4 if message4 is not None else set()
        self.group6 = group6 if group6 is not None else set()
        
        pass
    @property
    def Mail(self):
        return self.__Mail
    @Mail.setter
    def Mail(self, Mail: str):
        self.__Mail = Mail

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID_User(self):
        return self.__ID_User
    @ID_User.setter
    def ID_User(self, ID_User: int):
        self.__ID_User = ID_User

    @property
    def Fist_Name(self):
        return self.__Fist_Name
    @Fist_Name.setter
    def Fist_Name(self, Fist_Name: str):
        self.__Fist_Name = Fist_Name

    @property
    def page2(self):
        return self.__page2
    @page2.setter
    def page2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__page2", None)
        self.__page2 = value if value is not None else set()
        
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
    def message4(self):
        return self.__message4
    @message4.setter
    def message4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__message4", None)
        self.__message4 = value if value is not None else set()
        
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
    def profile1(self):
        return self.__profile1
    @profile1.setter
    def profile1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__profile1", None)
        self.__profile1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user0"):
                opp_val = getattr(old_value, "user0", None)
                if opp_val == self:
                    setattr(old_value, "user0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user0"):
                opp_val = getattr(value, "user0", None)
                setattr(value, "user0", self)



class Profile:

    def __init__(self, About: str, ID_Profile: str, User_Name: str, Password: str, user0: "User" = None):
        self.About = About
        self.ID_Profile = ID_Profile
        self.User_Name = User_Name
        self.Password = Password
        self.user0 = user0
        
        pass
    @property
    def About(self):
        return self.__About
    @About.setter
    def About(self, About: str):
        self.__About = About

    @property
    def ID_Profile(self):
        return self.__ID_Profile
    @ID_Profile.setter
    def ID_Profile(self, ID_Profile: str):
        self.__ID_Profile = ID_Profile

    @property
    def User_Name(self):
        return self.__User_Name
    @User_Name.setter
    def User_Name(self, User_Name: str):
        self.__User_Name = User_Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def user0(self):
        return self.__user0
    @user0.setter
    def user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__user0", None)
        self.__user0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile1"):
                opp_val = getattr(old_value, "profile1", None)
                if opp_val == self:
                    setattr(old_value, "profile1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile1"):
                opp_val = getattr(value, "profile1", None)
                setattr(value, "profile1", self)

