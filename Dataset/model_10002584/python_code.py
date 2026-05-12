from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Review:

    def __init__(self, PostContent: str, Review_User_018: "User" = None):
        self.PostContent = PostContent
        self.Review_User_018 = Review_User_018
        
        pass
    @property
    def PostContent(self):
        return self.__PostContent
    @PostContent.setter
    def PostContent(self, PostContent: str):
        self.__PostContent = PostContent

    @property
    def Review_User_018(self):
        return self.__Review_User_018
    @Review_User_018.setter
    def Review_User_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Review__Review_User_018", None)
        self.__Review_User_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Review_User_119"):
                opp_val = getattr(old_value, "Review_User_119", None)
                if opp_val == self:
                    setattr(old_value, "Review_User_119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Review_User_119"):
                opp_val = getattr(value, "Review_User_119", None)
                setattr(value, "Review_User_119", self)



class Media:

    def __init__(self, MediaPath: str, Post_ImagePost_117: "Post" = None):
        self.MediaPath = MediaPath
        self.Post_ImagePost_117 = Post_ImagePost_117
        
        pass
    @property
    def MediaPath(self):
        return self.__MediaPath
    @MediaPath.setter
    def MediaPath(self, MediaPath: str):
        self.__MediaPath = MediaPath

    @property
    def Post_ImagePost_117(self):
        return self.__Post_ImagePost_117
    @Post_ImagePost_117.setter
    def Post_ImagePost_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Media__Post_ImagePost_117", None)
        self.__Post_ImagePost_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Post_ImagePost_016"):
                opp_val = getattr(old_value, "Post_ImagePost_016", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Post_ImagePost_016"):
                opp_val = getattr(value, "Post_ImagePost_016", None)
                if opp_val is None:
                    setattr(value, "Post_ImagePost_016", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Friend:

    pass


class Chat:

    pass


class Team_Timeline:

    def __init__(self, Name: str, User_Timeline_115: "User" = None):
        self.Name = Name
        self.User_Timeline_115 = User_Timeline_115
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def User_Timeline_115(self):
        return self.__User_Timeline_115
    @User_Timeline_115.setter
    def User_Timeline_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team_Timeline__User_Timeline_115", None)
        self.__User_Timeline_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeline14"):
                opp_val = getattr(old_value, "timeline14", None)
                if opp_val == self:
                    setattr(old_value, "timeline14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeline14"):
                opp_val = getattr(value, "timeline14", None)
                setattr(value, "timeline14", self)



class Profile:

    def __init__(self, Username: str, Password: str, About: str, User_Profile_19: "User" = None):
        self.Username = Username
        self.Password = Password
        self.About = About
        self.User_Profile_19 = User_Profile_19
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def About(self):
        return self.__About
    @About.setter
    def About(self, About: str):
        self.__About = About

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def User_Profile_19(self):
        return self.__User_Profile_19
    @User_Profile_19.setter
    def User_Profile_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__User_Profile_19", None)
        self.__User_Profile_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Profile_08"):
                opp_val = getattr(old_value, "User_Profile_08", None)
                if opp_val == self:
                    setattr(old_value, "User_Profile_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Profile_08"):
                opp_val = getattr(value, "User_Profile_08", None)
                setattr(value, "User_Profile_08", self)



class Post:

    def __init__(self, PostContent: str, User_Post_17: "User" = None, Post_ImagePost_016: set["Media"] = None):
        self.PostContent = PostContent
        self.User_Post_17 = User_Post_17
        self.Post_ImagePost_016 = Post_ImagePost_016 if Post_ImagePost_016 is not None else set()
        
        pass
    @property
    def PostContent(self):
        return self.__PostContent
    @PostContent.setter
    def PostContent(self, PostContent: str):
        self.__PostContent = PostContent

    @property
    def Post_ImagePost_016(self):
        return self.__Post_ImagePost_016
    @Post_ImagePost_016.setter
    def Post_ImagePost_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__Post_ImagePost_016", None)
        self.__Post_ImagePost_016 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Post_ImagePost_117"):
                    opp_val = getattr(item, "Post_ImagePost_117", None)
                    
                    if opp_val == self:
                        setattr(item, "Post_ImagePost_117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Post_ImagePost_117"):
                    opp_val = getattr(item, "Post_ImagePost_117", None)
                    
                    setattr(item, "Post_ImagePost_117", self)
                    

    @property
    def User_Post_17(self):
        return self.__User_Post_17
    @User_Post_17.setter
    def User_Post_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__User_Post_17", None)
        self.__User_Post_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Post_06"):
                opp_val = getattr(old_value, "User_Post_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Post_06"):
                opp_val = getattr(value, "User_Post_06", None)
                if opp_val is None:
                    setattr(value, "User_Post_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Registration:

    def __init__(self, Password: Secret, Username: str, Registration_User_02: "User" = None):
        self.Password = Password
        self.Username = Username
        self.Registration_User_02 = Registration_User_02
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: Secret):
        self.__Password = Password

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Registration_User_02(self):
        return self.__Registration_User_02
    @Registration_User_02.setter
    def Registration_User_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__Registration_User_02", None)
        self.__Registration_User_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Registration_User_13"):
                opp_val = getattr(old_value, "Registration_User_13", None)
                if opp_val == self:
                    setattr(old_value, "Registration_User_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Registration_User_13"):
                opp_val = getattr(value, "Registration_User_13", None)
                setattr(value, "Registration_User_13", self)



class Login:

    def __init__(self, Username: str, Password: str, Login_User_04: "User" = None):
        self.Username = Username
        self.Password = Password
        self.Login_User_04 = Login_User_04
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Login_User_04(self):
        return self.__Login_User_04
    @Login_User_04.setter
    def Login_User_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__Login_User_04", None)
        self.__Login_User_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Login_User_15"):
                opp_val = getattr(old_value, "Login_User_15", None)
                if opp_val == self:
                    setattr(old_value, "Login_User_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Login_User_15"):
                opp_val = getattr(value, "Login_User_15", None)
                setattr(value, "Login_User_15", self)



class Public:

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Secret:

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Group:

    def __init__(self, Name: str, Description: str, User_Group_11: "User" = None):
        self.Name = Name
        self.Description = Description
        self.User_Group_11 = User_Group_11
        
        pass
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
    def User_Group_11(self):
        return self.__User_Group_11
    @User_Group_11.setter
    def User_Group_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__User_Group_11", None)
        self.__User_Group_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Group_00"):
                opp_val = getattr(old_value, "User_Group_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Group_00"):
                opp_val = getattr(value, "User_Group_00", None)
                if opp_val is None:
                    setattr(value, "User_Group_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, Name: str, Login_User_15: "Login" = None, User_Post_06: set["Post"] = None, User_Profile_08: "Profile" = None, friend10: set["Friend"] = None, User_Chat_012: set["Chat"] = None, timeline14: "Team_Timeline" = None, Review_User_119: "Review" = None, User_Group_00: set["Group"] = None, Registration_User_13: "Registration" = None):
        self.Name = Name
        self.Login_User_15 = Login_User_15
        self.User_Post_06 = User_Post_06 if User_Post_06 is not None else set()
        self.User_Profile_08 = User_Profile_08
        self.friend10 = friend10 if friend10 is not None else set()
        self.User_Chat_012 = User_Chat_012 if User_Chat_012 is not None else set()
        self.timeline14 = timeline14
        self.Review_User_119 = Review_User_119
        self.User_Group_00 = User_Group_00 if User_Group_00 is not None else set()
        self.Registration_User_13 = Registration_User_13
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def User_Chat_012(self):
        return self.__User_Chat_012
    @User_Chat_012.setter
    def User_Chat_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_Chat_012", None)
        self.__User_Chat_012 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User_Chat_113"):
                    opp_val = getattr(item, "User_Chat_113", None)
                    
                    if opp_val == self:
                        setattr(item, "User_Chat_113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User_Chat_113"):
                    opp_val = getattr(item, "User_Chat_113", None)
                    
                    setattr(item, "User_Chat_113", self)
                    

    @property
    def friend10(self):
        return self.__friend10
    @friend10.setter
    def friend10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__friend10", None)
        self.__friend10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User_Friend_111"):
                    opp_val = getattr(item, "User_Friend_111", None)
                    
                    if opp_val == self:
                        setattr(item, "User_Friend_111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User_Friend_111"):
                    opp_val = getattr(item, "User_Friend_111", None)
                    
                    setattr(item, "User_Friend_111", self)
                    

    @property
    def User_Group_00(self):
        return self.__User_Group_00
    @User_Group_00.setter
    def User_Group_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_Group_00", None)
        self.__User_Group_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User_Group_11"):
                    opp_val = getattr(item, "User_Group_11", None)
                    
                    if opp_val == self:
                        setattr(item, "User_Group_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User_Group_11"):
                    opp_val = getattr(item, "User_Group_11", None)
                    
                    setattr(item, "User_Group_11", self)
                    

    @property
    def User_Post_06(self):
        return self.__User_Post_06
    @User_Post_06.setter
    def User_Post_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_Post_06", None)
        self.__User_Post_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User_Post_17"):
                    opp_val = getattr(item, "User_Post_17", None)
                    
                    if opp_val == self:
                        setattr(item, "User_Post_17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User_Post_17"):
                    opp_val = getattr(item, "User_Post_17", None)
                    
                    setattr(item, "User_Post_17", self)
                    

    @property
    def Registration_User_13(self):
        return self.__Registration_User_13
    @Registration_User_13.setter
    def Registration_User_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Registration_User_13", None)
        self.__Registration_User_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Registration_User_02"):
                opp_val = getattr(old_value, "Registration_User_02", None)
                if opp_val == self:
                    setattr(old_value, "Registration_User_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Registration_User_02"):
                opp_val = getattr(value, "Registration_User_02", None)
                setattr(value, "Registration_User_02", self)

    @property
    def timeline14(self):
        return self.__timeline14
    @timeline14.setter
    def timeline14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__timeline14", None)
        self.__timeline14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Timeline_115"):
                opp_val = getattr(old_value, "User_Timeline_115", None)
                if opp_val == self:
                    setattr(old_value, "User_Timeline_115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Timeline_115"):
                opp_val = getattr(value, "User_Timeline_115", None)
                setattr(value, "User_Timeline_115", self)

    @property
    def Review_User_119(self):
        return self.__Review_User_119
    @Review_User_119.setter
    def Review_User_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Review_User_119", None)
        self.__Review_User_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Review_User_018"):
                opp_val = getattr(old_value, "Review_User_018", None)
                if opp_val == self:
                    setattr(old_value, "Review_User_018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Review_User_018"):
                opp_val = getattr(value, "Review_User_018", None)
                setattr(value, "Review_User_018", self)

    @property
    def User_Profile_08(self):
        return self.__User_Profile_08
    @User_Profile_08.setter
    def User_Profile_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_Profile_08", None)
        self.__User_Profile_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Profile_19"):
                opp_val = getattr(old_value, "User_Profile_19", None)
                if opp_val == self:
                    setattr(old_value, "User_Profile_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Profile_19"):
                opp_val = getattr(value, "User_Profile_19", None)
                setattr(value, "User_Profile_19", self)

    @property
    def Login_User_15(self):
        return self.__Login_User_15
    @Login_User_15.setter
    def Login_User_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Login_User_15", None)
        self.__Login_User_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Login_User_04"):
                opp_val = getattr(old_value, "Login_User_04", None)
                if opp_val == self:
                    setattr(old_value, "Login_User_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Login_User_04"):
                opp_val = getattr(value, "Login_User_04", None)
                setattr(value, "Login_User_04", self)

