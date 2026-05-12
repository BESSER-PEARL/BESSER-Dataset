from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Login:

    pass


class Course:

    def __init__(self, CourseName: str, CourseNumber: str, Course_Teacher: Teacher, takes_course0: set["Student"] = None, teacher11: "Teacher" = None):
        self.CourseName = CourseName
        self.CourseNumber = CourseNumber
        self.Course_Teacher = Course_Teacher
        self.takes_course0 = takes_course0 if takes_course0 is not None else set()
        self.teacher11 = teacher11
        
        pass
    @property
    def Course_Teacher(self):
        return self.__Course_Teacher
    @Course_Teacher.setter
    def Course_Teacher(self, Course_Teacher: Teacher):
        self.__Course_Teacher = Course_Teacher

    @property
    def CourseName(self):
        return self.__CourseName
    @CourseName.setter
    def CourseName(self, CourseName: str):
        self.__CourseName = CourseName

    @property
    def CourseNumber(self):
        return self.__CourseNumber
    @CourseNumber.setter
    def CourseNumber(self, CourseNumber: str):
        self.__CourseNumber = CourseNumber

    @property
    def takes_course0(self):
        return self.__takes_course0
    @takes_course0.setter
    def takes_course0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__takes_course0", None)
        self.__takes_course0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course1"):
                    opp_val = getattr(item, "course1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course1"):
                    opp_val = getattr(item, "course1", None)
                    
                    if opp_val is None:
                        setattr(item, "course1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def teacher11(self):
        return self.__teacher11
    @teacher11.setter
    def teacher11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__teacher11", None)
        self.__teacher11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Teaches10"):
                opp_val = getattr(old_value, "Teaches10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Teaches10"):
                opp_val = getattr(value, "Teaches10", None)
                if opp_val is None:
                    setattr(value, "Teaches10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin:

    pass


class Database:

    def __init__(self, Materials: Database, Schedules: Database, Grades: Database, Accounts: Database, User_Database_13: "User" = None, login5: "Login" = None, admin6: "Admin" = None, Student_Database_19: "Student" = None, teacher15: set["Teacher"] = None):
        self.Materials = Materials
        self.Schedules = Schedules
        self.Grades = Grades
        self.Accounts = Accounts
        self.User_Database_13 = User_Database_13
        self.login5 = login5
        self.admin6 = admin6
        self.Student_Database_19 = Student_Database_19
        self.teacher15 = teacher15 if teacher15 is not None else set()
        
        pass
    @property
    def Schedules(self):
        return self.__Schedules
    @Schedules.setter
    def Schedules(self, Schedules: Database):
        self.__Schedules = Schedules

    @property
    def Accounts(self):
        return self.__Accounts
    @Accounts.setter
    def Accounts(self, Accounts: Database):
        self.__Accounts = Accounts

    @property
    def Grades(self):
        return self.__Grades
    @Grades.setter
    def Grades(self, Grades: Database):
        self.__Grades = Grades

    @property
    def Materials(self):
        return self.__Materials
    @Materials.setter
    def Materials(self, Materials: Database):
        self.__Materials = Materials

    @property
    def User_Database_13(self):
        return self.__User_Database_13
    @User_Database_13.setter
    def User_Database_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__User_Database_13", None)
        self.__User_Database_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_user2"):
                opp_val = getattr(old_value, "has_user2", None)
                if opp_val == self:
                    setattr(old_value, "has_user2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_user2"):
                opp_val = getattr(value, "has_user2", None)
                setattr(value, "has_user2", self)

    @property
    def teacher15(self):
        return self.__teacher15
    @teacher15.setter
    def teacher15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__teacher15", None)
        self.__teacher15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "upload_to_database14"):
                    opp_val = getattr(item, "upload_to_database14", None)
                    
                    if opp_val == self:
                        setattr(item, "upload_to_database14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "upload_to_database14"):
                    opp_val = getattr(item, "upload_to_database14", None)
                    
                    setattr(item, "upload_to_database14", self)
                    

    @property
    def login5(self):
        return self.__login5
    @login5.setter
    def login5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__login5", None)
        self.__login5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "verify_account4"):
                opp_val = getattr(old_value, "verify_account4", None)
                if opp_val == self:
                    setattr(old_value, "verify_account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "verify_account4"):
                opp_val = getattr(value, "verify_account4", None)
                setattr(value, "verify_account4", self)

    @property
    def Student_Database_19(self):
        return self.__Student_Database_19
    @Student_Database_19.setter
    def Student_Database_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__Student_Database_19", None)
        self.__Student_Database_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database8"):
                opp_val = getattr(old_value, "database8", None)
                if opp_val == self:
                    setattr(old_value, "database8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database8"):
                opp_val = getattr(value, "database8", None)
                setattr(value, "database8", self)

    @property
    def admin6(self):
        return self.__admin6
    @admin6.setter
    def admin6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__admin6", None)
        self.__admin6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database_Admin_17"):
                opp_val = getattr(old_value, "Database_Admin_17", None)
                if opp_val == self:
                    setattr(old_value, "Database_Admin_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database_Admin_17"):
                opp_val = getattr(value, "Database_Admin_17", None)
                setattr(value, "Database_Admin_17", self)



class Teacher:

    def __init__(self, Assigned_Courses: str, Teaches10: set["Course"] = None, upload_to_database14: "Database" = None):
        self.Assigned_Courses = Assigned_Courses
        self.Teaches10 = Teaches10 if Teaches10 is not None else set()
        self.upload_to_database14 = upload_to_database14
        
        pass
    @property
    def Assigned_Courses(self):
        return self.__Assigned_Courses
    @Assigned_Courses.setter
    def Assigned_Courses(self, Assigned_Courses: str):
        self.__Assigned_Courses = Assigned_Courses

    @property
    def Teaches10(self):
        return self.__Teaches10
    @Teaches10.setter
    def Teaches10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teacher__Teaches10", None)
        self.__Teaches10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "teacher11"):
                    opp_val = getattr(item, "teacher11", None)
                    
                    if opp_val == self:
                        setattr(item, "teacher11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "teacher11"):
                    opp_val = getattr(item, "teacher11", None)
                    
                    setattr(item, "teacher11", self)
                    

    @property
    def upload_to_database14(self):
        return self.__upload_to_database14
    @upload_to_database14.setter
    def upload_to_database14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teacher__upload_to_database14", None)
        self.__upload_to_database14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teacher15"):
                opp_val = getattr(old_value, "teacher15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teacher15"):
                opp_val = getattr(value, "teacher15", None)
                if opp_val is None:
                    setattr(value, "teacher15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Student:

    def __init__(self, Year: str, course1: set["Course"] = None, database8: "Database" = None):
        self.Year = Year
        self.course1 = course1 if course1 is not None else set()
        self.database8 = database8
        
        pass
    @property
    def Year(self):
        return self.__Year
    @Year.setter
    def Year(self, Year: str):
        self.__Year = Year

    @property
    def course1(self):
        return self.__course1
    @course1.setter
    def course1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__course1", None)
        self.__course1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "takes_course0"):
                    opp_val = getattr(item, "takes_course0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "takes_course0"):
                    opp_val = getattr(item, "takes_course0", None)
                    
                    if opp_val is None:
                        setattr(item, "takes_course0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def database8(self):
        return self.__database8
    @database8.setter
    def database8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__database8", None)
        self.__database8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Student_Database_19"):
                opp_val = getattr(old_value, "Student_Database_19", None)
                if opp_val == self:
                    setattr(old_value, "Student_Database_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Student_Database_19"):
                opp_val = getattr(value, "Student_Database_19", None)
                setattr(value, "Student_Database_19", self)



class User:

    def __init__(self, First_Name: str, Last_Name: str, ID_Number: int, Password: str, has_user2: "Database" = None, login12: "Login" = None):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.ID_Number = ID_Number
        self.Password = Password
        self.has_user2 = has_user2
        self.login12 = login12
        
        pass
    @property
    def Last_Name(self):
        return self.__Last_Name
    @Last_Name.setter
    def Last_Name(self, Last_Name: str):
        self.__Last_Name = Last_Name

    @property
    def ID_Number(self):
        return self.__ID_Number
    @ID_Number.setter
    def ID_Number(self, ID_Number: int):
        self.__ID_Number = ID_Number

    @property
    def First_Name(self):
        return self.__First_Name
    @First_Name.setter
    def First_Name(self, First_Name: str):
        self.__First_Name = First_Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def login12(self):
        return self.__login12
    @login12.setter
    def login12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__login12", None)
        self.__login12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user13"):
                opp_val = getattr(old_value, "user13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user13"):
                opp_val = getattr(value, "user13", None)
                if opp_val is None:
                    setattr(value, "user13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has_user2(self):
        return self.__has_user2
    @has_user2.setter
    def has_user2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__has_user2", None)
        self.__has_user2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Database_13"):
                opp_val = getattr(old_value, "User_Database_13", None)
                if opp_val == self:
                    setattr(old_value, "User_Database_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Database_13"):
                opp_val = getattr(value, "User_Database_13", None)
                setattr(value, "User_Database_13", self)

