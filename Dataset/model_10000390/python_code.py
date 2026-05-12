from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass:

    pass


class Admin:

    pass


class Course:

    def __init__(self, subjects__: str, duration: str, department1: "Department" = None):
        self.subjects__ = subjects__
        self.duration = duration
        self.department1 = department1
        
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
    def subjects__(self, subjects__: str):
        self.__subjects__ = subjects__

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

    def __init__(self, course: Course, students__: Student, teachers__: Teacher, hod: str, course0: "Course" = None, student2: set["Student"] = None, employee4: set["Employee_Interface"] = None):
        self.course = course
        self.students__ = students__
        self.teachers__ = teachers__
        self.hod = hod
        self.course0 = course0
        self.student2 = student2 if student2 is not None else set()
        self.employee4 = employee4 if employee4 is not None else set()
        
        pass
    @property
    def hod(self):
        return self.__hod
    @hod.setter
    def hod(self, hod: str):
        self.__hod = hod

    @property
    def students__(self):
        return self.__students__
    @students__.setter
    def students__(self, students__: Student):
        self.__students__ = students__

    @property
    def teachers__(self):
        return self.__teachers__
    @teachers__.setter
    def teachers__(self, teachers__: Teacher):
        self.__teachers__ = teachers__

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: Course):
        self.__course = course

    @property
    def employee4(self):
        return self.__employee4
    @employee4.setter
    def employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__employee4", None)
        self.__employee4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department5"):
                    opp_val = getattr(item, "department5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department5"):
                    opp_val = getattr(item, "department5", None)
                    
                    if opp_val is None:
                        setattr(item, "department5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student2(self):
        return self.__student2
    @student2.setter
    def student2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__student2", None)
        self.__student2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department3"):
                    opp_val = getattr(item, "department3", None)
                    
                    if opp_val == self:
                        setattr(item, "department3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department3"):
                    opp_val = getattr(item, "department3", None)
                    
                    setattr(item, "department3", self)
                    

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



class Teacher:

    pass


class Employee_Interface:

    pass


class Student:

    def __init__(self, Name: str, ID: str, department3: "Department" = None, admin7: "Admin" = None):
        self.Name = Name
        self.ID = ID
        self.department3 = department3
        self.admin7 = admin7
        
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
    def department3(self):
        return self.__department3
    @department3.setter
    def department3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__department3", None)
        self.__department3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student2"):
                opp_val = getattr(old_value, "student2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student2"):
                opp_val = getattr(value, "student2", None)
                if opp_val is None:
                    setattr(value, "student2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def admin7(self):
        return self.__admin7
    @admin7.setter
    def admin7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__admin7", None)
        self.__admin7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student6"):
                opp_val = getattr(old_value, "student6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student6"):
                opp_val = getattr(value, "student6", None)
                if opp_val is None:
                    setattr(value, "student6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

