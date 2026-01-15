from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Univerity_Person:

    def __init__(self, Name: str, Email: str, Univerity_Person9: "Univerity_Person" = None, Univerity_Person7: "Univerity_Person" = None, Univerity_Person: "Univerity_Courses" = None, Univerity_Person6: "Univerity_Courses" = None):
        self.Name = Name
        self.Email = Email
        self.Univerity_Person9 = Univerity_Person9
        self.Univerity_Person7 = Univerity_Person7
        self.Univerity_Person = Univerity_Person
        self.Univerity_Person6 = Univerity_Person6
        
    @property
    def Email(self) -> str:
        return self.__Email

    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Univerity_Person9(self):
        return self.__Univerity_Person9

    @Univerity_Person9.setter
    def Univerity_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Person__Univerity_Person9", None)
        self.__Univerity_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_Person7"):
                opp_val = getattr(old_value, "Univerity_Person7", None)
                if opp_val == self:
                    setattr(old_value, "Univerity_Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_Person7"):
                opp_val = getattr(value, "Univerity_Person7", None)
                setattr(value, "Univerity_Person7", self)

    @property
    def Univerity_Person7(self):
        return self.__Univerity_Person7

    @Univerity_Person7.setter
    def Univerity_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Person__Univerity_Person7", None)
        self.__Univerity_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_Person9"):
                opp_val = getattr(old_value, "Univerity_Person9", None)
                if opp_val == self:
                    setattr(old_value, "Univerity_Person9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_Person9"):
                opp_val = getattr(value, "Univerity_Person9", None)
                setattr(value, "Univerity_Person9", self)

    @property
    def Univerity_Person6(self):
        return self.__Univerity_Person6

    @Univerity_Person6.setter
    def Univerity_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Person__Univerity_Person6", None)
        self.__Univerity_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_Courses5"):
                opp_val = getattr(old_value, "Univerity_Courses5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_Courses5"):
                opp_val = getattr(value, "Univerity_Courses5", None)
                if opp_val is None:
                    setattr(value, "Univerity_Courses5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Univerity_Person(self):
        return self.__Univerity_Person

    @Univerity_Person.setter
    def Univerity_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Person__Univerity_Person", None)
        self.__Univerity_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_Courses3"):
                opp_val = getattr(old_value, "Univerity_Courses3", None)
                if opp_val == self:
                    setattr(old_value, "Univerity_Courses3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_Courses3"):
                opp_val = getattr(value, "Univerity_Courses3", None)
                setattr(value, "Univerity_Courses3", self)

class Univerity_University:

    pass
class Univerity_Courses:

    def __init__(self, Name: str, CFU: int, Semester: str, Univerity_Courses: "Univerity_Courses" = None, Univerity_Courses11: "Univerity_University" = None, Univerity_Courses0: set["Univerity_Courses"] = None, Univerity_Courses3: "Univerity_Person" = None, Univerity_Courses5: set["Univerity_Person"] = None):
        self.Name = Name
        self.CFU = CFU
        self.Semester = Semester
        self.Univerity_Courses = Univerity_Courses
        self.Univerity_Courses11 = Univerity_Courses11
        self.Univerity_Courses0 = Univerity_Courses0 if Univerity_Courses0 is not None else set()
        self.Univerity_Courses3 = Univerity_Courses3
        self.Univerity_Courses5 = Univerity_Courses5 if Univerity_Courses5 is not None else set()
        
    @property
    def Semester(self) -> str:
        return self.__Semester

    @Semester.setter
    def Semester(self, Semester: str):
        self.__Semester = Semester

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def CFU(self) -> int:
        return self.__CFU

    @CFU.setter
    def CFU(self, CFU: int):
        self.__CFU = CFU

    @property
    def Univerity_Courses0(self):
        return self.__Univerity_Courses0

    @Univerity_Courses0.setter
    def Univerity_Courses0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses0", None)
        self.__Univerity_Courses0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Univerity_Courses"):
                    opp_val = getattr(item, "Univerity_Courses", None)
                    
                    if opp_val == self:
                        setattr(item, "Univerity_Courses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Univerity_Courses"):
                    opp_val = getattr(item, "Univerity_Courses", None)
                    
                    setattr(item, "Univerity_Courses", self)
                    

    @property
    def Univerity_Courses5(self):
        return self.__Univerity_Courses5

    @Univerity_Courses5.setter
    def Univerity_Courses5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses5", None)
        self.__Univerity_Courses5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Univerity_Person6"):
                    opp_val = getattr(item, "Univerity_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "Univerity_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Univerity_Person6"):
                    opp_val = getattr(item, "Univerity_Person6", None)
                    
                    setattr(item, "Univerity_Person6", self)
                    

    @property
    def Univerity_Courses11(self):
        return self.__Univerity_Courses11

    @Univerity_Courses11.setter
    def Univerity_Courses11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses11", None)
        self.__Univerity_Courses11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_University"):
                opp_val = getattr(old_value, "Univerity_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_University"):
                opp_val = getattr(value, "Univerity_University", None)
                if opp_val is None:
                    setattr(value, "Univerity_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Univerity_Courses(self):
        return self.__Univerity_Courses

    @Univerity_Courses.setter
    def Univerity_Courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses", None)
        self.__Univerity_Courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_Courses0"):
                opp_val = getattr(old_value, "Univerity_Courses0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_Courses0"):
                opp_val = getattr(value, "Univerity_Courses0", None)
                if opp_val is None:
                    setattr(value, "Univerity_Courses0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Univerity_Courses3(self):
        return self.__Univerity_Courses3

    @Univerity_Courses3.setter
    def Univerity_Courses3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses3", None)
        self.__Univerity_Courses3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Univerity_Person"):
                opp_val = getattr(old_value, "Univerity_Person", None)
                if opp_val == self:
                    setattr(old_value, "Univerity_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Univerity_Person"):
                opp_val = getattr(value, "Univerity_Person", None)
                setattr(value, "Univerity_Person", self)
