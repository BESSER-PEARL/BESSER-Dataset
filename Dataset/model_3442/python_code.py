from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class epdemo_Teacher:

    def __init__(self, Id: str, Name: str, epdemo_Teacher7: "epdemo_Clazz" = None, epdemo_Teacher: "epdemo_School" = None):
        self.Id = Id
        self.Name = Name
        self.epdemo_Teacher7 = epdemo_Teacher7
        self.epdemo_Teacher = epdemo_Teacher
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def epdemo_Teacher7(self):
        return self.__epdemo_Teacher7

    @epdemo_Teacher7.setter
    def epdemo_Teacher7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Teacher__epdemo_Teacher7", None)
        self.__epdemo_Teacher7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epdemo_Clazz6"):
                opp_val = getattr(old_value, "epdemo_Clazz6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epdemo_Clazz6"):
                opp_val = getattr(value, "epdemo_Clazz6", None)
                if opp_val is None:
                    setattr(value, "epdemo_Clazz6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epdemo_Teacher(self):
        return self.__epdemo_Teacher

    @epdemo_Teacher.setter
    def epdemo_Teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Teacher__epdemo_Teacher", None)
        self.__epdemo_Teacher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epdemo_School4"):
                opp_val = getattr(old_value, "epdemo_School4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epdemo_School4"):
                opp_val = getattr(value, "epdemo_School4", None)
                if opp_val is None:
                    setattr(value, "epdemo_School4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class epdemo_Student:

    def __init__(self, Id: str, Name: str, epdemo_Student10: "epdemo_Clazz" = None, epdemo_Student: "epdemo_School" = None):
        self.Id = Id
        self.Name = Name
        self.epdemo_Student10 = epdemo_Student10
        self.epdemo_Student = epdemo_Student
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def epdemo_Student(self):
        return self.__epdemo_Student

    @epdemo_Student.setter
    def epdemo_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Student__epdemo_Student", None)
        self.__epdemo_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epdemo_School2"):
                opp_val = getattr(old_value, "epdemo_School2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epdemo_School2"):
                opp_val = getattr(value, "epdemo_School2", None)
                if opp_val is None:
                    setattr(value, "epdemo_School2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epdemo_Student10(self):
        return self.__epdemo_Student10

    @epdemo_Student10.setter
    def epdemo_Student10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Student__epdemo_Student10", None)
        self.__epdemo_Student10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epdemo_Clazz9"):
                opp_val = getattr(old_value, "epdemo_Clazz9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epdemo_Clazz9"):
                opp_val = getattr(value, "epdemo_Clazz9", None)
                if opp_val is None:
                    setattr(value, "epdemo_Clazz9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class epdemo_Clazz:

    def __init__(self, Id: str, Name: str, epdemo_Clazz6: set["epdemo_Teacher"] = None, epdemo_Clazz9: set["epdemo_Student"] = None, epdemo_Clazz: "epdemo_School" = None):
        self.Id = Id
        self.Name = Name
        self.epdemo_Clazz6 = epdemo_Clazz6 if epdemo_Clazz6 is not None else set()
        self.epdemo_Clazz9 = epdemo_Clazz9 if epdemo_Clazz9 is not None else set()
        self.epdemo_Clazz = epdemo_Clazz
        
    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def epdemo_Clazz9(self):
        return self.__epdemo_Clazz9

    @epdemo_Clazz9.setter
    def epdemo_Clazz9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Clazz__epdemo_Clazz9", None)
        self.__epdemo_Clazz9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epdemo_Student10"):
                    opp_val = getattr(item, "epdemo_Student10", None)
                    
                    if opp_val == self:
                        setattr(item, "epdemo_Student10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epdemo_Student10"):
                    opp_val = getattr(item, "epdemo_Student10", None)
                    
                    setattr(item, "epdemo_Student10", self)
                    

    @property
    def epdemo_Clazz(self):
        return self.__epdemo_Clazz

    @epdemo_Clazz.setter
    def epdemo_Clazz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Clazz__epdemo_Clazz", None)
        self.__epdemo_Clazz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epdemo_School"):
                opp_val = getattr(old_value, "epdemo_School", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epdemo_School"):
                opp_val = getattr(value, "epdemo_School", None)
                if opp_val is None:
                    setattr(value, "epdemo_School", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epdemo_Clazz6(self):
        return self.__epdemo_Clazz6

    @epdemo_Clazz6.setter
    def epdemo_Clazz6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_Clazz__epdemo_Clazz6", None)
        self.__epdemo_Clazz6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epdemo_Teacher7"):
                    opp_val = getattr(item, "epdemo_Teacher7", None)
                    
                    if opp_val == self:
                        setattr(item, "epdemo_Teacher7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epdemo_Teacher7"):
                    opp_val = getattr(item, "epdemo_Teacher7", None)
                    
                    setattr(item, "epdemo_Teacher7", self)
                    

class epdemo_School:

    def __init__(self, Id: str, Name: str, epdemo_School: set["epdemo_Clazz"] = None, epdemo_School2: set["epdemo_Student"] = None, epdemo_School4: set["epdemo_Teacher"] = None):
        self.Id = Id
        self.Name = Name
        self.epdemo_School = epdemo_School if epdemo_School is not None else set()
        self.epdemo_School2 = epdemo_School2 if epdemo_School2 is not None else set()
        self.epdemo_School4 = epdemo_School4 if epdemo_School4 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def epdemo_School4(self):
        return self.__epdemo_School4

    @epdemo_School4.setter
    def epdemo_School4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_School__epdemo_School4", None)
        self.__epdemo_School4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epdemo_Teacher"):
                    opp_val = getattr(item, "epdemo_Teacher", None)
                    
                    if opp_val == self:
                        setattr(item, "epdemo_Teacher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epdemo_Teacher"):
                    opp_val = getattr(item, "epdemo_Teacher", None)
                    
                    setattr(item, "epdemo_Teacher", self)
                    

    @property
    def epdemo_School(self):
        return self.__epdemo_School

    @epdemo_School.setter
    def epdemo_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_School__epdemo_School", None)
        self.__epdemo_School = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epdemo_Clazz"):
                    opp_val = getattr(item, "epdemo_Clazz", None)
                    
                    if opp_val == self:
                        setattr(item, "epdemo_Clazz", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epdemo_Clazz"):
                    opp_val = getattr(item, "epdemo_Clazz", None)
                    
                    setattr(item, "epdemo_Clazz", self)
                    

    @property
    def epdemo_School2(self):
        return self.__epdemo_School2

    @epdemo_School2.setter
    def epdemo_School2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epdemo_School__epdemo_School2", None)
        self.__epdemo_School2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epdemo_Student"):
                    opp_val = getattr(item, "epdemo_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "epdemo_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epdemo_Student"):
                    opp_val = getattr(item, "epdemo_Student", None)
                    
                    setattr(item, "epdemo_Student", self)
                    
