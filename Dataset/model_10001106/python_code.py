from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class End_User:

    def __init__(self, login: str, password: str, userType: str, webUser1: "Internet_Users" = None, Thick_Client_Users2: "Thick_Client_Users" = None):
        self.login = login
        self.password = password
        self.userType = userType
        self.webUser1 = webUser1
        self.Thick_Client_Users2 = Thick_Client_Users2
        
        pass
    @property
    def userType(self):
        return self.__userType
    @userType.setter
    def userType(self, userType: str):
        self.__userType = userType

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Thick_Client_Users2(self):
        return self.__Thick_Client_Users2
    @Thick_Client_Users2.setter
    def Thick_Client_Users2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_User__Thick_Client_Users2", None)
        self.__Thick_Client_Users2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "endUser3"):
                opp_val = getattr(old_value, "endUser3", None)
                if opp_val == self:
                    setattr(old_value, "endUser3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "endUser3"):
                opp_val = getattr(value, "endUser3", None)
                setattr(value, "endUser3", self)

    @property
    def webUser1(self):
        return self.__webUser1
    @webUser1.setter
    def webUser1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_User__webUser1", None)
        self.__webUser1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Internet_Users0"):
                opp_val = getattr(old_value, "Internet_Users0", None)
                if opp_val == self:
                    setattr(old_value, "Internet_Users0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Internet_Users0"):
                opp_val = getattr(value, "Internet_Users0", None)
                setattr(value, "Internet_Users0", self)



class User_Admin_Module:

    def __init__(self, Generate_User: System_User, Delete_User: System_User, View_User: End_User, Account4: set["System_User"] = None):
        self.Generate_User = Generate_User
        self.Delete_User = Delete_User
        self.View_User = View_User
        self.Account4 = Account4 if Account4 is not None else set()
        
        pass
    @property
    def View_User(self):
        return self.__View_User
    @View_User.setter
    def View_User(self, View_User: End_User):
        self.__View_User = View_User

    @property
    def Generate_User(self):
        return self.__Generate_User
    @Generate_User.setter
    def Generate_User(self, Generate_User: System_User):
        self.__Generate_User = Generate_User

    @property
    def Delete_User(self):
        return self.__Delete_User
    @Delete_User.setter
    def Delete_User(self, Delete_User: System_User):
        self.__Delete_User = Delete_User

    @property
    def Account4(self):
        return self.__Account4
    @Account4.setter
    def Account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Admin_Module__Account4", None)
        self.__Account4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Admin5"):
                    opp_val = getattr(item, "Admin5", None)
                    
                    if opp_val == self:
                        setattr(item, "Admin5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Admin5"):
                    opp_val = getattr(item, "Admin5", None)
                    
                    setattr(item, "Admin5", self)
                    



class System_User:

    def __init__(self, login: str, password: str, Admin5: "User_Admin_Module" = None):
        self.login = login
        self.password = password
        self.Admin5 = Admin5
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def Admin5(self):
        return self.__Admin5
    @Admin5.setter
    def Admin5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_User__Admin5", None)
        self.__Admin5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Account4"):
                opp_val = getattr(old_value, "Account4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Account4"):
                opp_val = getattr(value, "Account4", None)
                if opp_val is None:
                    setattr(value, "Account4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Internet_Users:

    def __init__(self, Database_Access: System_User, Internet_Users0: "End_User" = None):
        self.Database_Access = Database_Access
        self.Internet_Users0 = Internet_Users0
        
        pass
    @property
    def Database_Access(self):
        return self.__Database_Access
    @Database_Access.setter
    def Database_Access(self, Database_Access: System_User):
        self.__Database_Access = Database_Access

    @property
    def Internet_Users0(self):
        return self.__Internet_Users0
    @Internet_Users0.setter
    def Internet_Users0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Internet_Users__Internet_Users0", None)
        self.__Internet_Users0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser1"):
                opp_val = getattr(old_value, "webUser1", None)
                if opp_val == self:
                    setattr(old_value, "webUser1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser1"):
                opp_val = getattr(value, "webUser1", None)
                setattr(value, "webUser1", self)



class Thick_Client_Users:

    def __init__(self, Database_Access: System_User, View_User: User_Admin_Module, endUser3: "End_User" = None):
        self.Database_Access = Database_Access
        self.View_User = View_User
        self.endUser3 = endUser3
        
        pass
    @property
    def View_User(self):
        return self.__View_User
    @View_User.setter
    def View_User(self, View_User: User_Admin_Module):
        self.__View_User = View_User

    @property
    def Database_Access(self):
        return self.__Database_Access
    @Database_Access.setter
    def Database_Access(self, Database_Access: System_User):
        self.__Database_Access = Database_Access

    @property
    def endUser3(self):
        return self.__endUser3
    @endUser3.setter
    def endUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Thick_Client_Users__endUser3", None)
        self.__endUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thick_Client_Users2"):
                opp_val = getattr(old_value, "Thick_Client_Users2", None)
                if opp_val == self:
                    setattr(old_value, "Thick_Client_Users2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thick_Client_Users2"):
                opp_val = getattr(value, "Thick_Client_Users2", None)
                setattr(value, "Thick_Client_Users2", self)

