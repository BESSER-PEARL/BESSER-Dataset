from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class User:

    def __init__(self, Id: int, project4: set["Project"] = None, account7: "Account" = None, comment2: set["Comment"] = None):
        self.Id = Id
        self.project4 = project4 if project4 is not None else set()
        self.account7 = account7
        self.comment2 = comment2 if comment2 is not None else set()
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def project4(self):
        return self.__project4
    @project4.setter
    def project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__project4", None)
        self.__project4 = value if value is not None else set()
        
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
    def comment2(self):
        return self.__comment2
    @comment2.setter
    def comment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__comment2", None)
        self.__comment2 = value if value is not None else set()
        
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
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user6"):
                opp_val = getattr(old_value, "user6", None)
                if opp_val == self:
                    setattr(old_value, "user6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user6"):
                opp_val = getattr(value, "user6", None)
                setattr(value, "user6", self)



class Account:

    def __init__(self, UserName: str, Info: str, user6: "User" = None, administrator8: "Administrator" = None):
        self.UserName = UserName
        self.Info = Info
        self.user6 = user6
        self.administrator8 = administrator8
        
        pass
    @property
    def Info(self):
        return self.__Info
    @Info.setter
    def Info(self, Info: str):
        self.__Info = Info

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def user6(self):
        return self.__user6
    @user6.setter
    def user6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__user6", None)
        self.__user6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account7"):
                opp_val = getattr(old_value, "account7", None)
                if opp_val == self:
                    setattr(old_value, "account7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account7"):
                opp_val = getattr(value, "account7", None)
                setattr(value, "account7", self)

    @property
    def administrator8(self):
        return self.__administrator8
    @administrator8.setter
    def administrator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__administrator8", None)
        self.__administrator8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account9"):
                opp_val = getattr(old_value, "account9", None)
                if opp_val == self:
                    setattr(old_value, "account9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account9"):
                opp_val = getattr(value, "account9", None)
                setattr(value, "account9", self)



class IAcc_Interface:

    pass


class Comment:

    def __init__(self, Id: int, Creator: User, Title: str, Body: str, CreationDate: str, administrator1: "Administrator" = None, user3: "User" = None):
        self.Id = Id
        self.Creator = Creator
        self.Title = Title
        self.Body = Body
        self.CreationDate = CreationDate
        self.administrator1 = administrator1
        self.user3 = user3
        
        pass
    @property
    def Creator(self):
        return self.__Creator
    @Creator.setter
    def Creator(self, Creator: User):
        self.__Creator = Creator

    @property
    def Body(self):
        return self.__Body
    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def CreationDate(self):
        return self.__CreationDate
    @CreationDate.setter
    def CreationDate(self, CreationDate: str):
        self.__CreationDate = CreationDate

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def administrator1(self):
        return self.__administrator1
    @administrator1.setter
    def administrator1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__administrator1", None)
        self.__administrator1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment0"):
                opp_val = getattr(old_value, "comment0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment0"):
                opp_val = getattr(value, "comment0", None)
                if opp_val is None:
                    setattr(value, "comment0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment2"):
                opp_val = getattr(old_value, "comment2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment2"):
                opp_val = getattr(value, "comment2", None)
                if opp_val is None:
                    setattr(value, "comment2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Administrator:

    def __init__(self, Id: int, account9: "Account" = None, comment0: set["Comment"] = None):
        self.Id = Id
        self.account9 = account9
        self.comment0 = comment0 if comment0 is not None else set()
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def account9(self):
        return self.__account9
    @account9.setter
    def account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__account9", None)
        self.__account9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator8"):
                opp_val = getattr(old_value, "administrator8", None)
                if opp_val == self:
                    setattr(old_value, "administrator8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator8"):
                opp_val = getattr(value, "administrator8", None)
                setattr(value, "administrator8", self)

    @property
    def comment0(self):
        return self.__comment0
    @comment0.setter
    def comment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__comment0", None)
        self.__comment0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator1"):
                    opp_val = getattr(item, "administrator1", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator1"):
                    opp_val = getattr(item, "administrator1", None)
                    
                    setattr(item, "administrator1", self)
                    



class Project:

    def __init__(self, Id: int, Title: str, Info: str, Access: str, State: str, user5: "User" = None):
        self.Id = Id
        self.Title = Title
        self.Info = Info
        self.Access = Access
        self.State = State
        self.user5 = user5
        
        pass
    @property
    def Access(self):
        return self.__Access
    @Access.setter
    def Access(self, Access: str):
        self.__Access = Access

    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Info(self):
        return self.__Info
    @Info.setter
    def Info(self, Info: str):
        self.__Info = Info

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project4"):
                opp_val = getattr(old_value, "project4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project4"):
                opp_val = getattr(value, "project4", None)
                if opp_val is None:
                    setattr(value, "project4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

