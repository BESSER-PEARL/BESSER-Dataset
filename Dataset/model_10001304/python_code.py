from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Admin:

    pass


class Subject:

    def __init__(self, name: str, course3: "Course" = None):
        self.name = name
        self.course3 = course3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def course3(self):
        return self.__course3
    @course3.setter
    def course3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Subject__course3", None)
        self.__course3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subject2"):
                opp_val = getattr(old_value, "subject2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subject2"):
                opp_val = getattr(value, "subject2", None)
                if opp_val is None:
                    setattr(value, "subject2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Attendance:

    pass


class Access_Information:

    pass


class Authentication:

    pass


class Course:

    def __init__(self, subjects__: Subject, duration: str, department1: "Department" = None, subject2: set["Subject"] = None):
        self.subjects__ = subjects__
        self.duration = duration
        self.department1 = department1
        self.subject2 = subject2 if subject2 is not None else set()
        
        pass
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def subjects__(self):
        return self.__subjects__
    @subjects__.setter
    def subjects__(self, subjects__: Subject):
        self.__subjects__ = subjects__

    @property
    def subject2(self):
        return self.__subject2
    @subject2.setter
    def subject2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__subject2", None)
        self.__subject2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course3"):
                    opp_val = getattr(item, "course3", None)
                    
                    if opp_val == self:
                        setattr(item, "course3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course3"):
                    opp_val = getattr(item, "course3", None)
                    
                    setattr(item, "course3", self)
                    

    @property
    def department1(self):
        return self.__department1
    @department1.setter
    def department1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__department1", None)
        self.__department1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course0"):
                opp_val = getattr(old_value, "course0", None)
                if opp_val == self:
                    setattr(old_value, "course0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course0"):
                opp_val = getattr(value, "course0", None)
                setattr(value, "course0", self)



class Department:

    def __init__(self, course: Course, students__: Student, teachers__: Teacher, hod: HOD, course0: "Course" = None, student4: set["Student"] = None, employee6: set["Employee_Interface"] = None, access_Information19: "Access_Information" = None):
        self.course = course
        self.students__ = students__
        self.teachers__ = teachers__
        self.hod = hod
        self.course0 = course0
        self.student4 = student4 if student4 is not None else set()
        self.employee6 = employee6 if employee6 is not None else set()
        self.access_Information19 = access_Information19
        
        pass
    @property
    def teachers__(self):
        return self.__teachers__
    @teachers__.setter
    def teachers__(self, teachers__: Teacher):
        self.__teachers__ = teachers__

    @property
    def students__(self):
        return self.__students__
    @students__.setter
    def students__(self, students__: Student):
        self.__students__ = students__

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: Course):
        self.__course = course

    @property
    def hod(self):
        return self.__hod
    @hod.setter
    def hod(self, hod: HOD):
        self.__hod = hod

    @property
    def employee6(self):
        return self.__employee6
    @employee6.setter
    def employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__employee6", None)
        self.__employee6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department7"):
                    opp_val = getattr(item, "department7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department7"):
                    opp_val = getattr(item, "department7", None)
                    
                    if opp_val is None:
                        setattr(item, "department7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student4(self):
        return self.__student4
    @student4.setter
    def student4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__student4", None)
        self.__student4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department5"):
                    opp_val = getattr(item, "department5", None)
                    
                    if opp_val == self:
                        setattr(item, "department5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department5"):
                    opp_val = getattr(item, "department5", None)
                    
                    setattr(item, "department5", self)
                    

    @property
    def access_Information19(self):
        return self.__access_Information19
    @access_Information19.setter
    def access_Information19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__access_Information19", None)
        self.__access_Information19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department18"):
                opp_val = getattr(old_value, "department18", None)
                if opp_val == self:
                    setattr(old_value, "department18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department18"):
                opp_val = getattr(value, "department18", None)
                setattr(value, "department18", self)

    @property
    def course0(self):
        return self.__course0
    @course0.setter
    def course0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__course0", None)
        self.__course0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department1"):
                opp_val = getattr(old_value, "department1", None)
                if opp_val == self:
                    setattr(old_value, "department1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department1"):
                opp_val = getattr(value, "department1", None)
                setattr(value, "department1", self)



class HOD:

    pass


class Teacher:

    pass


class Employee_Interface:

    pass


class Student:

    def __init__(self, Name: str, ID: str, department5: "Department" = None, Having_Attendance8: "Access_Information" = None, admin13: "Admin" = None):
        self.Name = Name
        self.ID = ID
        self.department5 = department5
        self.Having_Attendance8 = Having_Attendance8
        self.admin13 = admin13
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Having_Attendance8(self):
        return self.__Having_Attendance8
    @Having_Attendance8.setter
    def Having_Attendance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__Having_Attendance8", None)
        self.__Having_Attendance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student9"):
                opp_val = getattr(old_value, "student9", None)
                if opp_val == self:
                    setattr(old_value, "student9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student9"):
                opp_val = getattr(value, "student9", None)
                setattr(value, "student9", self)

    @property
    def department5(self):
        return self.__department5
    @department5.setter
    def department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__department5", None)
        self.__department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student4"):
                opp_val = getattr(old_value, "student4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student4"):
                opp_val = getattr(value, "student4", None)
                if opp_val is None:
                    setattr(value, "student4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def admin13(self):
        return self.__admin13
    @admin13.setter
    def admin13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__admin13", None)
        self.__admin13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student12"):
                opp_val = getattr(old_value, "student12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student12"):
                opp_val = getattr(value, "student12", None)
                if opp_val is None:
                    setattr(value, "student12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

