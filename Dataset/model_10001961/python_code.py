from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Status(Enum):
    pass
class Enumeration1(Enum):
    pass
class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################







class _UseCase:

    pass


class Corporate_UseCase:

    pass


class Corporate_Client_Actor:

    pass


class UseCase_UseCase:

    pass


class Update_Registar_UseCase:

    pass


class User_Info_UseCase:

    pass


class Grade_Course_UseCase:

    pass


class Select_Course_List_UseCase:

    pass


class Class_Course_List_UseCase:

    pass


class Teacher_Actor:

    pass


class Login_UseCase:

    pass


class Show_Grade_UseCase:

    pass


class Reports_UseCase:

    pass


class LearningMaterial_UseCase:

    pass


class Show_Course_UseCase:

    pass


class Modify_Course_UseCase:

    pass


class Remove_Course_UseCase:

    pass


class CompleteCourse_UseCase:

    pass


class Drop_Course_UseCase:

    pass


class Add_Course_UseCase:

    pass


class Create_Course_UseCase:

    pass


class Address_UseCase:

    pass


class Name_UseCase:

    pass


class Student_ID_UseCase:

    pass


class Traning_Admin_Actor:

    pass


class CORPORATE_CLIENT_Actor:

    pass


class TEACHER_Actor:

    pass


class Student_Actor:

    pass





class Class:

    pass


class courseList:

    def __init__(self, Class: Add_Course_UseCase, currentCourse: Course, teacher67: "Teacher" = None, course70: "Course" = None):
        self.Class = Class
        self.currentCourse = currentCourse
        self.teacher67 = teacher67
        self.course70 = course70
        
        pass
    @property
    def Class(self):
        return self.__Class
    @Class.setter
    def Class(self, Class: Add_Course_UseCase):
        self.__Class = Class

    @property
    def currentCourse(self):
        return self.__currentCourse
    @currentCourse.setter
    def currentCourse(self, currentCourse: Course):
        self.__currentCourse = currentCourse

    @property
    def teacher67(self):
        return self.__teacher67
    @teacher67.setter
    def teacher67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courseList__teacher67", None)
        self.__teacher67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classSchedule66"):
                opp_val = getattr(old_value, "classSchedule66", None)
                if opp_val == self:
                    setattr(old_value, "classSchedule66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classSchedule66"):
                opp_val = getattr(value, "classSchedule66", None)
                setattr(value, "classSchedule66", self)

    @property
    def course70(self):
        return self.__course70
    @course70.setter
    def course70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courseList__course70", None)
        self.__course70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseList71"):
                opp_val = getattr(old_value, "courseList71", None)
                if opp_val == self:
                    setattr(old_value, "courseList71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseList71"):
                opp_val = getattr(value, "courseList71", None)
                setattr(value, "courseList71", self)



class Admin:

    def __init__(self, attribute: str, Name: str, registrarList: str, courseList: str, User_status: str, registeredUser58: set["registeredUser"] = None, registeredUser60: set["registeredUser"] = None):
        self.attribute = attribute
        self.Name = Name
        self.registrarList = registrarList
        self.courseList = courseList
        self.User_status = User_status
        self.registeredUser58 = registeredUser58 if registeredUser58 is not None else set()
        self.registeredUser60 = registeredUser60 if registeredUser60 is not None else set()
        
        pass
    @property
    def User_status(self):
        return self.__User_status
    @User_status.setter
    def User_status(self, User_status: str):
        self.__User_status = User_status

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def registrarList(self):
        return self.__registrarList
    @registrarList.setter
    def registrarList(self, registrarList: str):
        self.__registrarList = registrarList

    @property
    def courseList(self):
        return self.__courseList
    @courseList.setter
    def courseList(self, courseList: str):
        self.__courseList = courseList

    @property
    def registeredUser58(self):
        return self.__registeredUser58
    @registeredUser58.setter
    def registeredUser58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__registeredUser58", None)
        self.__registeredUser58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin59"):
                    opp_val = getattr(item, "admin59", None)
                    
                    if opp_val == self:
                        setattr(item, "admin59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin59"):
                    opp_val = getattr(item, "admin59", None)
                    
                    setattr(item, "admin59", self)
                    

    @property
    def registeredUser60(self):
        return self.__registeredUser60
    @registeredUser60.setter
    def registeredUser60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__registeredUser60", None)
        self.__registeredUser60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin61"):
                    opp_val = getattr(item, "admin61", None)
                    
                    if opp_val == self:
                        setattr(item, "admin61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin61"):
                    opp_val = getattr(item, "admin61", None)
                    
                    setattr(item, "admin61", self)
                    



class registeredUser:

    def __init__(self, Id: int, Status: str, admin59: "Admin" = None, admin61: "Admin" = None):
        self.Id = Id
        self.Status = Status
        self.admin59 = admin59
        self.admin61 = admin61
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def admin59(self):
        return self.__admin59
    @admin59.setter
    def admin59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_registeredUser__admin59", None)
        self.__admin59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeredUser58"):
                opp_val = getattr(old_value, "registeredUser58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeredUser58"):
                opp_val = getattr(value, "registeredUser58", None)
                if opp_val is None:
                    setattr(value, "registeredUser58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def admin61(self):
        return self.__admin61
    @admin61.setter
    def admin61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_registeredUser__admin61", None)
        self.__admin61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeredUser60"):
                opp_val = getattr(old_value, "registeredUser60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeredUser60"):
                opp_val = getattr(value, "registeredUser60", None)
                if opp_val is None:
                    setattr(value, "registeredUser60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ADMIN:

    pass


class Registrar:

    def __init__(self, Status: Enumeration, courseList: str, _attr: str):
        self.Status = Status
        self.courseList = courseList
        self._attr = _attr
        
        pass
    @property
    def courseList(self):
        return self.__courseList
    @courseList.setter
    def courseList(self, courseList: str):
        self.__courseList = courseList

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: Enumeration):
        self.__Status = Status



class Teacher:

    def __init__(self, teacher_name: str, teacher_ID: int, phone: int, class_list: str, classSchedule66: "courseList" = None):
        self.teacher_name = teacher_name
        self.teacher_ID = teacher_ID
        self.phone = phone
        self.class_list = class_list
        self.classSchedule66 = classSchedule66
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def teacher_name(self):
        return self.__teacher_name
    @teacher_name.setter
    def teacher_name(self, teacher_name: str):
        self.__teacher_name = teacher_name

    @property
    def class_list(self):
        return self.__class_list
    @class_list.setter
    def class_list(self, class_list: str):
        self.__class_list = class_list

    @property
    def teacher_ID(self):
        return self.__teacher_ID
    @teacher_ID.setter
    def teacher_ID(self, teacher_ID: int):
        self.__teacher_ID = teacher_ID

    @property
    def classSchedule66(self):
        return self.__classSchedule66
    @classSchedule66.setter
    def classSchedule66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teacher__classSchedule66", None)
        self.__classSchedule66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teacher67"):
                opp_val = getattr(old_value, "teacher67", None)
                if opp_val == self:
                    setattr(old_value, "teacher67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teacher67"):
                opp_val = getattr(value, "teacher67", None)
                setattr(value, "teacher67", self)



class corprateClient:

    def __init__(self, client_name: str, client_ID: int, phone: int, companyRate: int, course69: "Course" = None):
        self.client_name = client_name
        self.client_ID = client_ID
        self.phone = phone
        self.companyRate = companyRate
        self.course69 = course69
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def client_ID(self):
        return self.__client_ID
    @client_ID.setter
    def client_ID(self, client_ID: int):
        self.__client_ID = client_ID

    @property
    def companyRate(self):
        return self.__companyRate
    @companyRate.setter
    def companyRate(self, companyRate: int):
        self.__companyRate = companyRate

    @property
    def client_name(self):
        return self.__client_name
    @client_name.setter
    def client_name(self, client_name: str):
        self.__client_name = client_name

    @property
    def course69(self):
        return self.__course69
    @course69.setter
    def course69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_corprateClient__course69", None)
        self.__course69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "corprateClient68"):
                opp_val = getattr(old_value, "corprateClient68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "corprateClient68"):
                opp_val = getattr(value, "corprateClient68", None)
                if opp_val is None:
                    setattr(value, "corprateClient68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Course:

    def __init__(self, courseName: str, Description: str, courseCode: int, start_date: str, end_date: str, student63: set["Student"] = None, student64: set["Student"] = None, corprateClient68: set["corprateClient"] = None, courseList71: "courseList" = None):
        self.courseName = courseName
        self.Description = Description
        self.courseCode = courseCode
        self.start_date = start_date
        self.end_date = end_date
        self.student63 = student63 if student63 is not None else set()
        self.student64 = student64 if student64 is not None else set()
        self.corprateClient68 = corprateClient68 if corprateClient68 is not None else set()
        self.courseList71 = courseList71
        
        pass
    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: str):
        self.__start_date = start_date

    @property
    def end_date(self):
        return self.__end_date
    @end_date.setter
    def end_date(self, end_date: str):
        self.__end_date = end_date

    @property
    def courseCode(self):
        return self.__courseCode
    @courseCode.setter
    def courseCode(self, courseCode: int):
        self.__courseCode = courseCode

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def student64(self):
        return self.__student64
    @student64.setter
    def student64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__student64", None)
        self.__student64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course65"):
                    opp_val = getattr(item, "course65", None)
                    
                    if opp_val == self:
                        setattr(item, "course65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course65"):
                    opp_val = getattr(item, "course65", None)
                    
                    setattr(item, "course65", self)
                    

    @property
    def student63(self):
        return self.__student63
    @student63.setter
    def student63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__student63", None)
        self.__student63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course62"):
                    opp_val = getattr(item, "Course62", None)
                    
                    if opp_val == self:
                        setattr(item, "Course62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course62"):
                    opp_val = getattr(item, "Course62", None)
                    
                    setattr(item, "Course62", self)
                    

    @property
    def corprateClient68(self):
        return self.__corprateClient68
    @corprateClient68.setter
    def corprateClient68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__corprateClient68", None)
        self.__corprateClient68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course69"):
                    opp_val = getattr(item, "course69", None)
                    
                    if opp_val == self:
                        setattr(item, "course69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course69"):
                    opp_val = getattr(item, "course69", None)
                    
                    setattr(item, "course69", self)
                    

    @property
    def courseList71(self):
        return self.__courseList71
    @courseList71.setter
    def courseList71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__courseList71", None)
        self.__courseList71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course70"):
                opp_val = getattr(old_value, "course70", None)
                if opp_val == self:
                    setattr(old_value, "course70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course70"):
                opp_val = getattr(value, "course70", None)
                setattr(value, "course70", self)



class Student:

    def __init__(self, student_name: str, student_ID: int, phone: int, studentRate: int, Course62: "Course" = None, course65: "Course" = None):
        self.student_name = student_name
        self.student_ID = student_ID
        self.phone = phone
        self.studentRate = studentRate
        self.Course62 = Course62
        self.course65 = course65
        
        pass
    @property
    def studentRate(self):
        return self.__studentRate
    @studentRate.setter
    def studentRate(self, studentRate: int):
        self.__studentRate = studentRate

    @property
    def student_ID(self):
        return self.__student_ID
    @student_ID.setter
    def student_ID(self, student_ID: int):
        self.__student_ID = student_ID

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def student_name(self):
        return self.__student_name
    @student_name.setter
    def student_name(self, student_name: str):
        self.__student_name = student_name

    @property
    def Course62(self):
        return self.__Course62
    @Course62.setter
    def Course62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__Course62", None)
        self.__Course62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student63"):
                opp_val = getattr(old_value, "student63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student63"):
                opp_val = getattr(value, "student63", None)
                if opp_val is None:
                    setattr(value, "student63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course65(self):
        return self.__course65
    @course65.setter
    def course65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__course65", None)
        self.__course65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student64"):
                opp_val = getattr(old_value, "student64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student64"):
                opp_val = getattr(value, "student64", None)
                if opp_val is None:
                    setattr(value, "student64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class class_Student_Registration_Admin:

    pass


class class_Student_Registration_Corporate:

    pass


class class_Student_Registration_Teacher:

    pass


class class_Student_Registration_Student:

    def __init__(self, attribute: str, String: Name_UseCase, String1: Student_ID_UseCase, String2: Address_UseCase, Integer: str, Function: Add_Course_UseCase):
        self.attribute = attribute
        self.String = String
        self.String1 = String1
        self.String2 = String2
        self.Integer = Integer
        self.Function = Function
        
        pass
    @property
    def String1(self):
        return self.__String1
    @String1.setter
    def String1(self, String1: Student_ID_UseCase):
        self.__String1 = String1

    @property
    def String(self):
        return self.__String
    @String.setter
    def String(self, String: Name_UseCase):
        self.__String = String

    @property
    def Integer(self):
        return self.__Integer
    @Integer.setter
    def Integer(self, Integer: str):
        self.__Integer = Integer

    @property
    def Function(self):
        return self.__Function
    @Function.setter
    def Function(self, Function: Add_Course_UseCase):
        self.__Function = Function

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def String2(self):
        return self.__String2
    @String2.setter
    def String2(self, String2: Address_UseCase):
        self.__String2 = String2



class class_Student_Registration:

    pass


class Courses_Component:

    pass
