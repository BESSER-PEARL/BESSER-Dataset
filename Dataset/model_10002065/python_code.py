from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Exceptions:

    pass


class Report:

    pass


class Email:

    pass


class Exam:

    def __init__(self, ETime: str, EName: str, MaxGrade: str, course8: "Course" = None, binary_File44: "Binary_File" = None):
        self.ETime = ETime
        self.EName = EName
        self.MaxGrade = MaxGrade
        self.course8 = course8
        self.binary_File44 = binary_File44
        
        pass
    @property
    def MaxGrade(self):
        return self.__MaxGrade
    @MaxGrade.setter
    def MaxGrade(self, MaxGrade: str):
        self.__MaxGrade = MaxGrade

    @property
    def EName(self):
        return self.__EName
    @EName.setter
    def EName(self, EName: str):
        self.__EName = EName

    @property
    def ETime(self):
        return self.__ETime
    @ETime.setter
    def ETime(self, ETime: str):
        self.__ETime = ETime

    @property
    def binary_File44(self):
        return self.__binary_File44
    @binary_File44.setter
    def binary_File44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exam__binary_File44", None)
        self.__binary_File44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam45"):
                opp_val = getattr(old_value, "exam45", None)
                if opp_val == self:
                    setattr(old_value, "exam45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam45"):
                opp_val = getattr(value, "exam45", None)
                setattr(value, "exam45", self)

    @property
    def course8(self):
        return self.__course8
    @course8.setter
    def course8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exam__course8", None)
        self.__course8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam9"):
                opp_val = getattr(old_value, "exam9", None)
                if opp_val == self:
                    setattr(old_value, "exam9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam9"):
                opp_val = getattr(value, "exam9", None)
                setattr(value, "exam9", self)



class Course:

    def __init__(self, CName: str, CPrice: str, CCode: str, CInstructor: str, binary_File6: "Binary_File" = None, exam9: "Exam" = None, report19: "Report" = None, admin31: "Admin" = None, department33: "Department" = None, student35: "Student" = None, report38: "Report" = None):
        self.CName = CName
        self.CPrice = CPrice
        self.CCode = CCode
        self.CInstructor = CInstructor
        self.binary_File6 = binary_File6
        self.exam9 = exam9
        self.report19 = report19
        self.admin31 = admin31
        self.department33 = department33
        self.student35 = student35
        self.report38 = report38
        
        pass
    @property
    def CPrice(self):
        return self.__CPrice
    @CPrice.setter
    def CPrice(self, CPrice: str):
        self.__CPrice = CPrice

    @property
    def CCode(self):
        return self.__CCode
    @CCode.setter
    def CCode(self, CCode: str):
        self.__CCode = CCode

    @property
    def CInstructor(self):
        return self.__CInstructor
    @CInstructor.setter
    def CInstructor(self, CInstructor: str):
        self.__CInstructor = CInstructor

    @property
    def CName(self):
        return self.__CName
    @CName.setter
    def CName(self, CName: str):
        self.__CName = CName

    @property
    def report38(self):
        return self.__report38
    @report38.setter
    def report38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__report38", None)
        self.__report38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course39"):
                opp_val = getattr(old_value, "course39", None)
                if opp_val == self:
                    setattr(old_value, "course39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course39"):
                opp_val = getattr(value, "course39", None)
                setattr(value, "course39", self)

    @property
    def department33(self):
        return self.__department33
    @department33.setter
    def department33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__department33", None)
        self.__department33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course32"):
                opp_val = getattr(old_value, "course32", None)
                if opp_val == self:
                    setattr(old_value, "course32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course32"):
                opp_val = getattr(value, "course32", None)
                setattr(value, "course32", self)

    @property
    def admin31(self):
        return self.__admin31
    @admin31.setter
    def admin31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__admin31", None)
        self.__admin31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course30"):
                opp_val = getattr(old_value, "course30", None)
                if opp_val == self:
                    setattr(old_value, "course30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course30"):
                opp_val = getattr(value, "course30", None)
                setattr(value, "course30", self)

    @property
    def student35(self):
        return self.__student35
    @student35.setter
    def student35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__student35", None)
        self.__student35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course34"):
                opp_val = getattr(old_value, "course34", None)
                if opp_val == self:
                    setattr(old_value, "course34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course34"):
                opp_val = getattr(value, "course34", None)
                setattr(value, "course34", self)

    @property
    def binary_File6(self):
        return self.__binary_File6
    @binary_File6.setter
    def binary_File6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__binary_File6", None)
        self.__binary_File6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course7"):
                opp_val = getattr(old_value, "course7", None)
                if opp_val == self:
                    setattr(old_value, "course7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course7"):
                opp_val = getattr(value, "course7", None)
                setattr(value, "course7", self)

    @property
    def report19(self):
        return self.__report19
    @report19.setter
    def report19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__report19", None)
        self.__report19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course18"):
                opp_val = getattr(old_value, "course18", None)
                if opp_val == self:
                    setattr(old_value, "course18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course18"):
                opp_val = getattr(value, "course18", None)
                setattr(value, "course18", self)

    @property
    def exam9(self):
        return self.__exam9
    @exam9.setter
    def exam9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__exam9", None)
        self.__exam9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course8"):
                opp_val = getattr(old_value, "course8", None)
                if opp_val == self:
                    setattr(old_value, "course8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course8"):
                opp_val = getattr(value, "course8", None)
                setattr(value, "course8", self)



class T:

    pass


class User:

    def __init__(self, email: str, Fname: str, Lname: str, Password: str, User_ILogin_02: "ILogin_Interface" = None, binary_File4: "Binary_File" = None, exceptions10: "Exceptions" = None):
        self.email = email
        self.Fname = Fname
        self.Lname = Lname
        self.Password = Password
        self.User_ILogin_02 = User_ILogin_02
        self.binary_File4 = binary_File4
        self.exceptions10 = exceptions10
        
        pass
    @property
    def Lname(self):
        return self.__Lname
    @Lname.setter
    def Lname(self, Lname: str):
        self.__Lname = Lname

    @property
    def Fname(self):
        return self.__Fname
    @Fname.setter
    def Fname(self, Fname: str):
        self.__Fname = Fname

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def binary_File4(self):
        return self.__binary_File4
    @binary_File4.setter
    def binary_File4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__binary_File4", None)
        self.__binary_File4 = value
        
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
    def exceptions10(self):
        return self.__exceptions10
    @exceptions10.setter
    def exceptions10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__exceptions10", None)
        self.__exceptions10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user11"):
                opp_val = getattr(old_value, "user11", None)
                if opp_val == self:
                    setattr(old_value, "user11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user11"):
                opp_val = getattr(value, "user11", None)
                setattr(value, "user11", self)

    @property
    def User_ILogin_02(self):
        return self.__User_ILogin_02
    @User_ILogin_02.setter
    def User_ILogin_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_ILogin_02", None)
        self.__User_ILogin_02 = value
        
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



class ILogin_Interface:

    pass


class Department:

    def __init__(self, deptName: str, deptId: str, instructor1: "Instructor" = None, binary_File12: "Binary_File" = None, course32: "Course" = None):
        self.deptName = deptName
        self.deptId = deptId
        self.instructor1 = instructor1
        self.binary_File12 = binary_File12
        self.course32 = course32
        
        pass
    @property
    def deptId(self):
        return self.__deptId
    @deptId.setter
    def deptId(self, deptId: str):
        self.__deptId = deptId

    @property
    def deptName(self):
        return self.__deptName
    @deptName.setter
    def deptName(self, deptName: str):
        self.__deptName = deptName

    @property
    def course32(self):
        return self.__course32
    @course32.setter
    def course32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__course32", None)
        self.__course32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department33"):
                opp_val = getattr(old_value, "department33", None)
                if opp_val == self:
                    setattr(old_value, "department33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department33"):
                opp_val = getattr(value, "department33", None)
                setattr(value, "department33", self)

    @property
    def binary_File12(self):
        return self.__binary_File12
    @binary_File12.setter
    def binary_File12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__binary_File12", None)
        self.__binary_File12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department13"):
                opp_val = getattr(old_value, "department13", None)
                if opp_val == self:
                    setattr(old_value, "department13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department13"):
                opp_val = getattr(value, "department13", None)
                setattr(value, "department13", self)

    @property
    def instructor1(self):
        return self.__instructor1
    @instructor1.setter
    def instructor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__instructor1", None)
        self.__instructor1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department0"):
                opp_val = getattr(old_value, "department0", None)
                if opp_val == self:
                    setattr(old_value, "department0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department0"):
                opp_val = getattr(value, "department0", None)
                setattr(value, "department0", self)



class Binary_File:

    pass


class Student:

    def __init__(self, SAge: int, SGender: str, report14: "Report" = None, email23: "Email" = None, finance25: "Finance" = None, admin27: "Admin" = None, course34: "Course" = None):
        self.SAge = SAge
        self.SGender = SGender
        self.report14 = report14
        self.email23 = email23
        self.finance25 = finance25
        self.admin27 = admin27
        self.course34 = course34
        
        pass
    @property
    def SGender(self):
        return self.__SGender
    @SGender.setter
    def SGender(self, SGender: str):
        self.__SGender = SGender

    @property
    def SAge(self):
        return self.__SAge
    @SAge.setter
    def SAge(self, SAge: int):
        self.__SAge = SAge

    @property
    def admin27(self):
        return self.__admin27
    @admin27.setter
    def admin27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__admin27", None)
        self.__admin27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student26"):
                opp_val = getattr(old_value, "student26", None)
                if opp_val == self:
                    setattr(old_value, "student26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student26"):
                opp_val = getattr(value, "student26", None)
                setattr(value, "student26", self)

    @property
    def report14(self):
        return self.__report14
    @report14.setter
    def report14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__report14", None)
        self.__report14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student15"):
                opp_val = getattr(old_value, "student15", None)
                if opp_val == self:
                    setattr(old_value, "student15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student15"):
                opp_val = getattr(value, "student15", None)
                setattr(value, "student15", self)

    @property
    def email23(self):
        return self.__email23
    @email23.setter
    def email23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__email23", None)
        self.__email23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student22"):
                opp_val = getattr(old_value, "student22", None)
                if opp_val == self:
                    setattr(old_value, "student22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student22"):
                opp_val = getattr(value, "student22", None)
                setattr(value, "student22", self)

    @property
    def course34(self):
        return self.__course34
    @course34.setter
    def course34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__course34", None)
        self.__course34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student35"):
                opp_val = getattr(old_value, "student35", None)
                if opp_val == self:
                    setattr(old_value, "student35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student35"):
                opp_val = getattr(value, "student35", None)
                setattr(value, "student35", self)

    @property
    def finance25(self):
        return self.__finance25
    @finance25.setter
    def finance25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__finance25", None)
        self.__finance25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student24"):
                opp_val = getattr(old_value, "student24", None)
                if opp_val == self:
                    setattr(old_value, "student24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student24"):
                opp_val = getattr(value, "student24", None)
                setattr(value, "student24", self)



class Instructor:

    pass


class Finance:

    pass


class str:

    pass


class Stuff:

    def __init__(self, Salary: str, WorkHours: str):
        self.Salary = Salary
        self.WorkHours = WorkHours
        
        pass
    @property
    def WorkHours(self):
        return self.__WorkHours
    @WorkHours.setter
    def WorkHours(self, WorkHours: str):
        self.__WorkHours = WorkHours

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: str):
        self.__Salary = Salary



class Person:

    def __init__(self, PhoneNum: str, Id: str):
        self.PhoneNum = PhoneNum
        self.Id = Id
        
        pass
    @property
    def PhoneNum(self):
        return self.__PhoneNum
    @PhoneNum.setter
    def PhoneNum(self, PhoneNum: str):
        self.__PhoneNum = PhoneNum

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id



class Admin:

    pass
