from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Integer_AdminID_String_Password2_Interface:

    pass


class Integer_AdminID_String_Password_Interface:

    pass


class Candidate:

    pass


class SuperAdmin:

    def __init__(self, adminID: int, password: str, dataBase3: "DataBase" = None):
        self.adminID = adminID
        self.password = password
        self.dataBase3 = dataBase3
        
        pass
    @property
    def adminID(self):
        return self.__adminID
    @adminID.setter
    def adminID(self, adminID: int):
        self.__adminID = adminID

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def dataBase3(self):
        return self.__dataBase3
    @dataBase3.setter
    def dataBase3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SuperAdmin__dataBase3", None)
        self.__dataBase3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superAdmin2"):
                opp_val = getattr(old_value, "superAdmin2", None)
                if opp_val == self:
                    setattr(old_value, "superAdmin2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superAdmin2"):
                opp_val = getattr(value, "superAdmin2", None)
                setattr(value, "superAdmin2", self)



class UserAdmin:

    def __init__(self, adminID: int, password: str, dataBase5: "DataBase" = None):
        self.adminID = adminID
        self.password = password
        self.dataBase5 = dataBase5
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def adminID(self):
        return self.__adminID
    @adminID.setter
    def adminID(self, adminID: int):
        self.__adminID = adminID

    @property
    def dataBase5(self):
        return self.__dataBase5
    @dataBase5.setter
    def dataBase5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserAdmin__dataBase5", None)
        self.__dataBase5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAdmin4"):
                opp_val = getattr(old_value, "userAdmin4", None)
                if opp_val == self:
                    setattr(old_value, "userAdmin4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAdmin4"):
                opp_val = getattr(value, "userAdmin4", None)
                setattr(value, "userAdmin4", self)



class DataBase:

    def __init__(self, obj1: SuperAdmin, obj2: UserAdmin, obj3: Voter, obj4: Candidate, voter0: "Voter" = None, superAdmin2: "SuperAdmin" = None, userAdmin4: "UserAdmin" = None):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4
        self.voter0 = voter0
        self.superAdmin2 = superAdmin2
        self.userAdmin4 = userAdmin4
        
        pass
    @property
    def obj4(self):
        return self.__obj4
    @obj4.setter
    def obj4(self, obj4: Candidate):
        self.__obj4 = obj4

    @property
    def obj1(self):
        return self.__obj1
    @obj1.setter
    def obj1(self, obj1: SuperAdmin):
        self.__obj1 = obj1

    @property
    def obj3(self):
        return self.__obj3
    @obj3.setter
    def obj3(self, obj3: Voter):
        self.__obj3 = obj3

    @property
    def obj2(self):
        return self.__obj2
    @obj2.setter
    def obj2(self, obj2: UserAdmin):
        self.__obj2 = obj2

    @property
    def superAdmin2(self):
        return self.__superAdmin2
    @superAdmin2.setter
    def superAdmin2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DataBase__superAdmin2", None)
        self.__superAdmin2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataBase3"):
                opp_val = getattr(old_value, "dataBase3", None)
                if opp_val == self:
                    setattr(old_value, "dataBase3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataBase3"):
                opp_val = getattr(value, "dataBase3", None)
                setattr(value, "dataBase3", self)

    @property
    def voter0(self):
        return self.__voter0
    @voter0.setter
    def voter0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DataBase__voter0", None)
        self.__voter0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataBase1"):
                opp_val = getattr(old_value, "dataBase1", None)
                if opp_val == self:
                    setattr(old_value, "dataBase1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataBase1"):
                opp_val = getattr(value, "dataBase1", None)
                setattr(value, "dataBase1", self)

    @property
    def userAdmin4(self):
        return self.__userAdmin4
    @userAdmin4.setter
    def userAdmin4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DataBase__userAdmin4", None)
        self.__userAdmin4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataBase5"):
                opp_val = getattr(old_value, "dataBase5", None)
                if opp_val == self:
                    setattr(old_value, "dataBase5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataBase5"):
                opp_val = getattr(value, "dataBase5", None)
                setattr(value, "dataBase5", self)



class Voter:

    def __init__(self, serialNum: int, password: str, dataBase1: "DataBase" = None):
        self.serialNum = serialNum
        self.password = password
        self.dataBase1 = dataBase1
        
        pass
    @property
    def serialNum(self):
        return self.__serialNum
    @serialNum.setter
    def serialNum(self, serialNum: int):
        self.__serialNum = serialNum

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def dataBase1(self):
        return self.__dataBase1
    @dataBase1.setter
    def dataBase1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voter__dataBase1", None)
        self.__dataBase1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voter0"):
                opp_val = getattr(old_value, "voter0", None)
                if opp_val == self:
                    setattr(old_value, "voter0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voter0"):
                opp_val = getattr(value, "voter0", None)
                setattr(value, "voter0", self)

