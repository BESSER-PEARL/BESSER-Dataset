from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Schedule:

    pass


class Note:

    pass


class Subject:

    pass


class Grade:

    def __init__(self, name: str, teacher0: "Teacher" = None, students3: "Student" = None):
        self.name = name
        self.teacher0 = teacher0
        self.students3 = students3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def students3(self):
        return self.__students3
    @students3.setter
    def students3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grade__students3", None)
        self.__students3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grade2"):
                opp_val = getattr(old_value, "grade2", None)
                if opp_val == self:
                    setattr(old_value, "grade2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grade2"):
                opp_val = getattr(value, "grade2", None)
                setattr(value, "grade2", self)

    @property
    def teacher0(self):
        return self.__teacher0
    @teacher0.setter
    def teacher0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grade__teacher0", None)
        self.__teacher0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grades1"):
                opp_val = getattr(old_value, "grades1", None)
                if opp_val == self:
                    setattr(old_value, "grades1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grades1"):
                opp_val = getattr(value, "grades1", None)
                setattr(value, "grades1", self)



class Teacher:

    def __init__(self, name: str, surname: str, email: str, phone: str, grades1: "Grade" = None):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.grades1 = grades1
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def grades1(self):
        return self.__grades1
    @grades1.setter
    def grades1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teacher__grades1", None)
        self.__grades1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teacher0"):
                opp_val = getattr(old_value, "teacher0", None)
                if opp_val == self:
                    setattr(old_value, "teacher0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teacher0"):
                opp_val = getattr(value, "teacher0", None)
                setattr(value, "teacher0", self)



class Student:

    def __init__(self, phone: str, email: str, surname: str, name: str, grade2: "Grade" = None, subjects4: "Subject" = None, schedule9: "Schedule" = None):
        self.phone = phone
        self.email = email
        self.surname = surname
        self.name = name
        self.grade2 = grade2
        self.subjects4 = subjects4
        self.schedule9 = schedule9
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def schedule9(self):
        return self.__schedule9
    @schedule9.setter
    def schedule9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__schedule9", None)
        self.__schedule9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student8"):
                opp_val = getattr(old_value, "student8", None)
                if opp_val == self:
                    setattr(old_value, "student8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student8"):
                opp_val = getattr(value, "student8", None)
                setattr(value, "student8", self)

    @property
    def grade2(self):
        return self.__grade2
    @grade2.setter
    def grade2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__grade2", None)
        self.__grade2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students3"):
                opp_val = getattr(old_value, "students3", None)
                if opp_val == self:
                    setattr(old_value, "students3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students3"):
                opp_val = getattr(value, "students3", None)
                setattr(value, "students3", self)

    @property
    def subjects4(self):
        return self.__subjects4
    @subjects4.setter
    def subjects4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__subjects4", None)
        self.__subjects4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student5"):
                opp_val = getattr(old_value, "student5", None)
                if opp_val == self:
                    setattr(old_value, "student5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student5"):
                opp_val = getattr(value, "student5", None)
                setattr(value, "student5", self)

