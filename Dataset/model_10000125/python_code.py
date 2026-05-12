from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










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
                    



class Department:

    def __init__(self, course: Course, students__: Student, lecturer__: Lecturer, hod: HOD, course0: "Course" = None, Department_Student_04: set["Student"] = None, access_Information13: "Access_Information" = None, hOD15: "HOD" = None, lecturer17: "Lecturer" = None):
        self.course = course
        self.students__ = students__
        self.lecturer__ = lecturer__
        self.hod = hod
        self.course0 = course0
        self.Department_Student_04 = Department_Student_04 if Department_Student_04 is not None else set()
        self.access_Information13 = access_Information13
        self.hOD15 = hOD15
        self.lecturer17 = lecturer17
        
        pass
    @property
    def hod(self):
        return self.__hod
    @hod.setter
    def hod(self, hod: HOD):
        self.__hod = hod

    @property
    def students__(self):
        return self.__students__
    @students__.setter
    def students__(self, students__: Student):
        self.__students__ = students__

    @property
    def lecturer__(self):
        return self.__lecturer__
    @lecturer__.setter
    def lecturer__(self, lecturer__: Lecturer):
        self.__lecturer__ = lecturer__

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: Course):
        self.__course = course

    @property
    def lecturer17(self):
        return self.__lecturer17
    @lecturer17.setter
    def lecturer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__lecturer17", None)
        self.__lecturer17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department16"):
                opp_val = getattr(old_value, "department16", None)
                if opp_val == self:
                    setattr(old_value, "department16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department16"):
                opp_val = getattr(value, "department16", None)
                setattr(value, "department16", self)

    @property
    def Department_Student_04(self):
        return self.__Department_Student_04
    @Department_Student_04.setter
    def Department_Student_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__Department_Student_04", None)
        self.__Department_Student_04 = value if value is not None else set()
        
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
    def hOD15(self):
        return self.__hOD15
    @hOD15.setter
    def hOD15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__hOD15", None)
        self.__hOD15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department14"):
                opp_val = getattr(old_value, "department14", None)
                if opp_val == self:
                    setattr(old_value, "department14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department14"):
                opp_val = getattr(value, "department14", None)
                setattr(value, "department14", self)

    @property
    def access_Information13(self):
        return self.__access_Information13
    @access_Information13.setter
    def access_Information13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__access_Information13", None)
        self.__access_Information13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department12"):
                opp_val = getattr(old_value, "department12", None)
                if opp_val == self:
                    setattr(old_value, "department12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department12"):
                opp_val = getattr(value, "department12", None)
                setattr(value, "department12", self)

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


class Lecturer:

    pass


class Student:

    def __init__(self, Name: str, ID: str, department5: "Department" = None, Having_Attendance6: "Access_Information" = None, admin9: "Admin" = None):
        self.Name = Name
        self.ID = ID
        self.department5 = department5
        self.Having_Attendance6 = Having_Attendance6
        self.admin9 = admin9
        
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
    def admin9(self):
        return self.__admin9
    @admin9.setter
    def admin9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__admin9", None)
        self.__admin9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student8"):
                opp_val = getattr(old_value, "student8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student8"):
                opp_val = getattr(value, "student8", None)
                if opp_val is None:
                    setattr(value, "student8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Department_Student_04"):
                opp_val = getattr(old_value, "Department_Student_04", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department_Student_04"):
                opp_val = getattr(value, "Department_Student_04", None)
                if opp_val is None:
                    setattr(value, "Department_Student_04", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Having_Attendance6(self):
        return self.__Having_Attendance6
    @Having_Attendance6.setter
    def Having_Attendance6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__Having_Attendance6", None)
        self.__Having_Attendance6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student7"):
                opp_val = getattr(old_value, "student7", None)
                if opp_val == self:
                    setattr(old_value, "student7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student7"):
                opp_val = getattr(value, "student7", None)
                setattr(value, "student7", self)



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

