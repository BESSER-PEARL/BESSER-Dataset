from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Add_notes:

    def __init__(self, Student_ID: int, Course_Name: str, Notes_taken: str, home_page9: "Home_page" = None):
        self.Student_ID = Student_ID
        self.Course_Name = Course_Name
        self.Notes_taken = Notes_taken
        self.home_page9 = home_page9
        
        pass
    @property
    def Student_ID(self):
        return self.__Student_ID
    @Student_ID.setter
    def Student_ID(self, Student_ID: int):
        self.__Student_ID = Student_ID

    @property
    def Notes_taken(self):
        return self.__Notes_taken
    @Notes_taken.setter
    def Notes_taken(self, Notes_taken: str):
        self.__Notes_taken = Notes_taken

    @property
    def Course_Name(self):
        return self.__Course_Name
    @Course_Name.setter
    def Course_Name(self, Course_Name: str):
        self.__Course_Name = Course_Name

    @property
    def home_page9(self):
        return self.__home_page9
    @home_page9.setter
    def home_page9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Add_notes__home_page9", None)
        self.__home_page9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "add_notes8"):
                opp_val = getattr(old_value, "add_notes8", None)
                if opp_val == self:
                    setattr(old_value, "add_notes8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "add_notes8"):
                opp_val = getattr(value, "add_notes8", None)
                setattr(value, "add_notes8", self)



class Show_all_grades:

    def __init__(self, Student_ID: int, First_Name: str, Last_Name: str, Course_name: str, Teacher: str, Grade_earned: str, home_page5: "Home_page" = None):
        self.Student_ID = Student_ID
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Course_name = Course_name
        self.Teacher = Teacher
        self.Grade_earned = Grade_earned
        self.home_page5 = home_page5
        
        pass
    @property
    def Course_name(self):
        return self.__Course_name
    @Course_name.setter
    def Course_name(self, Course_name: str):
        self.__Course_name = Course_name

    @property
    def First_Name(self):
        return self.__First_Name
    @First_Name.setter
    def First_Name(self, First_Name: str):
        self.__First_Name = First_Name

    @property
    def Last_Name(self):
        return self.__Last_Name
    @Last_Name.setter
    def Last_Name(self, Last_Name: str):
        self.__Last_Name = Last_Name

    @property
    def Grade_earned(self):
        return self.__Grade_earned
    @Grade_earned.setter
    def Grade_earned(self, Grade_earned: str):
        self.__Grade_earned = Grade_earned

    @property
    def Student_ID(self):
        return self.__Student_ID
    @Student_ID.setter
    def Student_ID(self, Student_ID: int):
        self.__Student_ID = Student_ID

    @property
    def Teacher(self):
        return self.__Teacher
    @Teacher.setter
    def Teacher(self, Teacher: str):
        self.__Teacher = Teacher

    @property
    def home_page5(self):
        return self.__home_page5
    @home_page5.setter
    def home_page5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Show_all_grades__home_page5", None)
        self.__home_page5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "show_all_grades4"):
                opp_val = getattr(old_value, "show_all_grades4", None)
                if opp_val == self:
                    setattr(old_value, "show_all_grades4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "show_all_grades4"):
                opp_val = getattr(value, "show_all_grades4", None)
                setattr(value, "show_all_grades4", self)



class Home_page:

    pass


class Interface2_Interface:

    pass


class Interface1_Interface:

    pass


class Class:

    pass


class Interface_Interface:

    pass


class New_user:

    def __init__(self, Student_ID: int, First_name: str, Last_Name: str, Major: str, Student_ID1: int, Contact_No: int, login1: "Login" = None):
        self.Student_ID = Student_ID
        self.First_name = First_name
        self.Last_Name = Last_Name
        self.Major = Major
        self.Student_ID1 = Student_ID1
        self.Contact_No = Contact_No
        self.login1 = login1
        
        pass
    @property
    def Major(self):
        return self.__Major
    @Major.setter
    def Major(self, Major: str):
        self.__Major = Major

    @property
    def First_name(self):
        return self.__First_name
    @First_name.setter
    def First_name(self, First_name: str):
        self.__First_name = First_name

    @property
    def Student_ID(self):
        return self.__Student_ID
    @Student_ID.setter
    def Student_ID(self, Student_ID: int):
        self.__Student_ID = Student_ID

    @property
    def Student_ID1(self):
        return self.__Student_ID1
    @Student_ID1.setter
    def Student_ID1(self, Student_ID1: int):
        self.__Student_ID1 = Student_ID1

    @property
    def Last_Name(self):
        return self.__Last_Name
    @Last_Name.setter
    def Last_Name(self, Last_Name: str):
        self.__Last_Name = Last_Name

    @property
    def Contact_No(self):
        return self.__Contact_No
    @Contact_No.setter
    def Contact_No(self, Contact_No: int):
        self.__Contact_No = Contact_No

    @property
    def login1(self):
        return self.__login1
    @login1.setter
    def login1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_New_user__login1", None)
        self.__login1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "new_user0"):
                opp_val = getattr(old_value, "new_user0", None)
                if opp_val == self:
                    setattr(old_value, "new_user0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "new_user0"):
                opp_val = getattr(value, "new_user0", None)
                setattr(value, "new_user0", self)



class names:

    pass


class Login:

    def __init__(self, Student_ID: int, Password: str, Email: str, new_user0: "New_user" = None, home_page2: "Home_page" = None):
        self.Student_ID = Student_ID
        self.Password = Password
        self.Email = Email
        self.new_user0 = new_user0
        self.home_page2 = home_page2
        
        pass
    @property
    def Student_ID(self):
        return self.__Student_ID
    @Student_ID.setter
    def Student_ID(self, Student_ID: int):
        self.__Student_ID = Student_ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def home_page2(self):
        return self.__home_page2
    @home_page2.setter
    def home_page2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__home_page2", None)
        self.__home_page2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login3"):
                opp_val = getattr(old_value, "login3", None)
                if opp_val == self:
                    setattr(old_value, "login3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login3"):
                opp_val = getattr(value, "login3", None)
                setattr(value, "login3", self)

    @property
    def new_user0(self):
        return self.__new_user0
    @new_user0.setter
    def new_user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__new_user0", None)
        self.__new_user0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login1"):
                opp_val = getattr(old_value, "login1", None)
                if opp_val == self:
                    setattr(old_value, "login1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login1"):
                opp_val = getattr(value, "login1", None)
                setattr(value, "login1", self)



class Course:

    def __init__(self, Course_name: str, Day: str, Time: str, Room: int, Teacher: str, Student_ID: int, Grade_earned: str, Status: str, Course_Index: int, home_page7: "Home_page" = None):
        self.Course_name = Course_name
        self.Day = Day
        self.Time = Time
        self.Room = Room
        self.Teacher = Teacher
        self.Student_ID = Student_ID
        self.Grade_earned = Grade_earned
        self.Status = Status
        self.Course_Index = Course_Index
        self.home_page7 = home_page7
        
        pass
    @property
    def Room(self):
        return self.__Room
    @Room.setter
    def Room(self, Room: int):
        self.__Room = Room

    @property
    def Student_ID(self):
        return self.__Student_ID
    @Student_ID.setter
    def Student_ID(self, Student_ID: int):
        self.__Student_ID = Student_ID

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def Course_name(self):
        return self.__Course_name
    @Course_name.setter
    def Course_name(self, Course_name: str):
        self.__Course_name = Course_name

    @property
    def Grade_earned(self):
        return self.__Grade_earned
    @Grade_earned.setter
    def Grade_earned(self, Grade_earned: str):
        self.__Grade_earned = Grade_earned

    @property
    def Day(self):
        return self.__Day
    @Day.setter
    def Day(self, Day: str):
        self.__Day = Day

    @property
    def Course_Index(self):
        return self.__Course_Index
    @Course_Index.setter
    def Course_Index(self, Course_Index: int):
        self.__Course_Index = Course_Index

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def Teacher(self):
        return self.__Teacher
    @Teacher.setter
    def Teacher(self, Teacher: str):
        self.__Teacher = Teacher

    @property
    def home_page7(self):
        return self.__home_page7
    @home_page7.setter
    def home_page7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__home_page7", None)
        self.__home_page7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course6"):
                opp_val = getattr(old_value, "course6", None)
                if opp_val == self:
                    setattr(old_value, "course6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course6"):
                opp_val = getattr(value, "course6", None)
                setattr(value, "course6", self)

