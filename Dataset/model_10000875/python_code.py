from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class barcode:

    pass


class controller:

    pass


class staff_member:

    pass


class Department:

    def __init__(self, dept_name: str, dept_id: int, student0: set["student"] = None, course16: set["course"] = None):
        self.dept_name = dept_name
        self.dept_id = dept_id
        self.student0 = student0 if student0 is not None else set()
        self.course16 = course16 if course16 is not None else set()
        
        pass
    @property
    def dept_id(self):
        return self.__dept_id
    @dept_id.setter
    def dept_id(self, dept_id: int):
        self.__dept_id = dept_id

    @property
    def dept_name(self):
        return self.__dept_name
    @dept_name.setter
    def dept_name(self, dept_name: str):
        self.__dept_name = dept_name

    @property
    def student0(self):
        return self.__student0
    @student0.setter
    def student0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__student0", None)
        self.__student0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department1"):
                    opp_val = getattr(item, "department1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department1"):
                    opp_val = getattr(item, "department1", None)
                    
                    if opp_val is None:
                        setattr(item, "department1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def course16(self):
        return self.__course16
    @course16.setter
    def course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__course16", None)
        self.__course16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department17"):
                    opp_val = getattr(item, "department17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department17"):
                    opp_val = getattr(item, "department17", None)
                    
                    if opp_val is None:
                        setattr(item, "department17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class course:

    def __init__(self, course_name: str, course_id: int, course_preq: str, credit_hours: int, student3: set["student"] = None, admin4: set["Admin"] = None, person8: set["Person"] = None, department17: set["Department"] = None):
        self.course_name = course_name
        self.course_id = course_id
        self.course_preq = course_preq
        self.credit_hours = credit_hours
        self.student3 = student3 if student3 is not None else set()
        self.admin4 = admin4 if admin4 is not None else set()
        self.person8 = person8 if person8 is not None else set()
        self.department17 = department17 if department17 is not None else set()
        
        pass
    @property
    def course_preq(self):
        return self.__course_preq
    @course_preq.setter
    def course_preq(self, course_preq: str):
        self.__course_preq = course_preq

    @property
    def credit_hours(self):
        return self.__credit_hours
    @credit_hours.setter
    def credit_hours(self, credit_hours: int):
        self.__credit_hours = credit_hours

    @property
    def course_id(self):
        return self.__course_id
    @course_id.setter
    def course_id(self, course_id: int):
        self.__course_id = course_id

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, course_name: str):
        self.__course_name = course_name

    @property
    def admin4(self):
        return self.__admin4
    @admin4.setter
    def admin4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course__admin4", None)
        self.__admin4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course5"):
                    opp_val = getattr(item, "course5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course5"):
                    opp_val = getattr(item, "course5", None)
                    
                    if opp_val is None:
                        setattr(item, "course5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student3(self):
        return self.__student3
    @student3.setter
    def student3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course__student3", None)
        self.__student3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course2"):
                    opp_val = getattr(item, "course2", None)
                    
                    if opp_val == self:
                        setattr(item, "course2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course2"):
                    opp_val = getattr(item, "course2", None)
                    
                    setattr(item, "course2", self)
                    

    @property
    def department17(self):
        return self.__department17
    @department17.setter
    def department17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course__department17", None)
        self.__department17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course16"):
                    opp_val = getattr(item, "course16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course16"):
                    opp_val = getattr(item, "course16", None)
                    
                    if opp_val is None:
                        setattr(item, "course16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def person8(self):
        return self.__person8
    @person8.setter
    def person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course__person8", None)
        self.__person8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course9"):
                    opp_val = getattr(item, "course9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course9"):
                    opp_val = getattr(item, "course9", None)
                    
                    if opp_val is None:
                        setattr(item, "course9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Class:

    pass


class Interface_Interface:

    pass


class Admin:

    pass


class student:

    def __init__(self, major_dept: str, minor_dept: str, department1: set["Department"] = None, course2: "course" = None, barcode6: set["barcode"] = None):
        self.major_dept = major_dept
        self.minor_dept = minor_dept
        self.department1 = department1 if department1 is not None else set()
        self.course2 = course2
        self.barcode6 = barcode6 if barcode6 is not None else set()
        
        pass
    @property
    def minor_dept(self):
        return self.__minor_dept
    @minor_dept.setter
    def minor_dept(self, minor_dept: str):
        self.__minor_dept = minor_dept

    @property
    def major_dept(self):
        return self.__major_dept
    @major_dept.setter
    def major_dept(self, major_dept: str):
        self.__major_dept = major_dept

    @property
    def barcode6(self):
        return self.__barcode6
    @barcode6.setter
    def barcode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__barcode6", None)
        self.__barcode6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student7"):
                    opp_val = getattr(item, "student7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student7"):
                    opp_val = getattr(item, "student7", None)
                    
                    if opp_val is None:
                        setattr(item, "student7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def course2(self):
        return self.__course2
    @course2.setter
    def course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__course2", None)
        self.__course2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student3"):
                opp_val = getattr(old_value, "student3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student3"):
                opp_val = getattr(value, "student3", None)
                if opp_val is None:
                    setattr(value, "student3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def department1(self):
        return self.__department1
    @department1.setter
    def department1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__department1", None)
        self.__department1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student0"):
                    opp_val = getattr(item, "student0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student0"):
                    opp_val = getattr(item, "student0", None)
                    
                    if opp_val is None:
                        setattr(item, "student0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Person:

    def __init__(self, name: str, id: int, username: str, email: str, date_of_birth: str, address: str, password: int, department: str, course9: set["course"] = None):
        self.name = name
        self.id = id
        self.username = username
        self.email = email
        self.date_of_birth = date_of_birth
        self.address = address
        self.password = password
        self.department = department
        self.course9 = course9 if course9 is not None else set()
        
        pass
    @property
    def date_of_birth(self):
        return self.__date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        self.__date_of_birth = date_of_birth

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def course9(self):
        return self.__course9
    @course9.setter
    def course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__course9", None)
        self.__course9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person8"):
                    opp_val = getattr(item, "person8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person8"):
                    opp_val = getattr(item, "person8", None)
                    
                    if opp_val is None:
                        setattr(item, "person8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

