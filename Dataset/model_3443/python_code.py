from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class skol_Classroom:

    def __init__(self, name: str, skol_Classroom: set["skol_Student"] = None, skol_Classroom4: "skol_School" = None):
        self.name = name
        self.skol_Classroom = skol_Classroom if skol_Classroom is not None else set()
        self.skol_Classroom4 = skol_Classroom4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def skol_Classroom(self):
        return self.__skol_Classroom

    @skol_Classroom.setter
    def skol_Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_Classroom__skol_Classroom", None)
        self.__skol_Classroom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "skol_Student"):
                    opp_val = getattr(item, "skol_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "skol_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "skol_Student"):
                    opp_val = getattr(item, "skol_Student", None)
                    
                    setattr(item, "skol_Student", self)
                    

    @property
    def skol_Classroom4(self):
        return self.__skol_Classroom4

    @skol_Classroom4.setter
    def skol_Classroom4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_Classroom__skol_Classroom4", None)
        self.__skol_Classroom4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "skol_School3"):
                opp_val = getattr(old_value, "skol_School3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "skol_School3"):
                opp_val = getattr(value, "skol_School3", None)
                if opp_val is None:
                    setattr(value, "skol_School3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class skol_School:

    def __init__(self, name: str, skol_School: "skol_Diagram" = None, skol_School3: set["skol_Classroom"] = None):
        self.name = name
        self.skol_School = skol_School
        self.skol_School3 = skol_School3 if skol_School3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def skol_School(self):
        return self.__skol_School

    @skol_School.setter
    def skol_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_School__skol_School", None)
        self.__skol_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "skol_Diagram"):
                opp_val = getattr(old_value, "skol_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "skol_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "skol_Diagram"):
                opp_val = getattr(value, "skol_Diagram", None)
                setattr(value, "skol_Diagram", self)

    @property
    def skol_School3(self):
        return self.__skol_School3

    @skol_School3.setter
    def skol_School3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_School__skol_School3", None)
        self.__skol_School3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "skol_Classroom4"):
                    opp_val = getattr(item, "skol_Classroom4", None)
                    
                    if opp_val == self:
                        setattr(item, "skol_Classroom4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "skol_Classroom4"):
                    opp_val = getattr(item, "skol_Classroom4", None)
                    
                    setattr(item, "skol_Classroom4", self)
                    

class skol_Diagram:

    pass
class skol_Student:

    def __init__(self, name: str, skol_Student: "skol_Classroom" = None, skol_Student7: "skol_Student" = None, skol_Student5: set["skol_Student"] = None):
        self.name = name
        self.skol_Student = skol_Student
        self.skol_Student7 = skol_Student7
        self.skol_Student5 = skol_Student5 if skol_Student5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def skol_Student(self):
        return self.__skol_Student

    @skol_Student.setter
    def skol_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_Student__skol_Student", None)
        self.__skol_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "skol_Classroom"):
                opp_val = getattr(old_value, "skol_Classroom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "skol_Classroom"):
                opp_val = getattr(value, "skol_Classroom", None)
                if opp_val is None:
                    setattr(value, "skol_Classroom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def skol_Student5(self):
        return self.__skol_Student5

    @skol_Student5.setter
    def skol_Student5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_Student__skol_Student5", None)
        self.__skol_Student5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "skol_Student7"):
                    opp_val = getattr(item, "skol_Student7", None)
                    
                    if opp_val == self:
                        setattr(item, "skol_Student7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "skol_Student7"):
                    opp_val = getattr(item, "skol_Student7", None)
                    
                    setattr(item, "skol_Student7", self)
                    

    @property
    def skol_Student7(self):
        return self.__skol_Student7

    @skol_Student7.setter
    def skol_Student7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_skol_Student__skol_Student7", None)
        self.__skol_Student7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "skol_Student5"):
                opp_val = getattr(old_value, "skol_Student5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "skol_Student5"):
                opp_val = getattr(value, "skol_Student5", None)
                if opp_val is None:
                    setattr(value, "skol_Student5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
