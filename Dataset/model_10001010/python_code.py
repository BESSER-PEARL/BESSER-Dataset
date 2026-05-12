from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Employee_Actor:

    pass


class Administrator_Actor:

    pass


class Salary_Management_UseCase:

    pass


class Authentication_UseCase:

    pass





class Logout_external:

    pass


class Login_external:

    pass


class Employee_Management_System_Component:

    pass


class Login:

    def __init__(self, UserName: str, Password: str):
        self.UserName = UserName
        self.Password = Password
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName



class Authenticate_staff:

    def __init__(self, UserName: str, Password: str, Authendication_Mood: str):
        self.UserName = UserName
        self.Password = Password
        self.Authendication_Mood = Authendication_Mood
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Authendication_Mood(self):
        return self.__Authendication_Mood
    @Authendication_Mood.setter
    def Authendication_Mood(self, Authendication_Mood: str):
        self.__Authendication_Mood = Authendication_Mood



class Employee:

    def __init__(self, Emp_Id: int, Emp_Name: str, Emp_Address: str, Emp_DOB: date, Emp_Date_Of_Joint: date, Emp_Position: str):
        self.Emp_Id = Emp_Id
        self.Emp_Name = Emp_Name
        self.Emp_Address = Emp_Address
        self.Emp_DOB = Emp_DOB
        self.Emp_Date_Of_Joint = Emp_Date_Of_Joint
        self.Emp_Position = Emp_Position
        
        pass
    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def Emp_Date_Of_Joint(self):
        return self.__Emp_Date_Of_Joint
    @Emp_Date_Of_Joint.setter
    def Emp_Date_Of_Joint(self, Emp_Date_Of_Joint: date):
        self.__Emp_Date_Of_Joint = Emp_Date_Of_Joint

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Emp_DOB(self):
        return self.__Emp_DOB
    @Emp_DOB.setter
    def Emp_DOB(self, Emp_DOB: date):
        self.__Emp_DOB = Emp_DOB

    @property
    def Emp_Position(self):
        return self.__Emp_Position
    @Emp_Position.setter
    def Emp_Position(self, Emp_Position: str):
        self.__Emp_Position = Emp_Position

    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

