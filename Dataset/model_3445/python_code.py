from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class schol_School:

    def __init__(self, name: str, schol_School: "schol_Diagram" = None, schol_School3: set["schol_Classroom"] = None):
        self.name = name
        self.schol_School = schol_School
        self.schol_School3 = schol_School3 if schol_School3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schol_School(self):
        return self.__schol_School

    @schol_School.setter
    def schol_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_School__schol_School", None)
        self.__schol_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schol_Diagram"):
                opp_val = getattr(old_value, "schol_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "schol_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schol_Diagram"):
                opp_val = getattr(value, "schol_Diagram", None)
                setattr(value, "schol_Diagram", self)

    @property
    def schol_School3(self):
        return self.__schol_School3

    @schol_School3.setter
    def schol_School3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_School__schol_School3", None)
        self.__schol_School3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schol_Classroom4"):
                    opp_val = getattr(item, "schol_Classroom4", None)
                    
                    if opp_val == self:
                        setattr(item, "schol_Classroom4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schol_Classroom4"):
                    opp_val = getattr(item, "schol_Classroom4", None)
                    
                    setattr(item, "schol_Classroom4", self)
                    

class schol_Diagram:

    pass
class schol_Student:

    def __init__(self, name: str, schol_Student7: "schol_Student" = None, schol_Student5: set["schol_Student"] = None, schol_Student: "schol_Classroom" = None):
        self.name = name
        self.schol_Student7 = schol_Student7
        self.schol_Student5 = schol_Student5 if schol_Student5 is not None else set()
        self.schol_Student = schol_Student
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schol_Student5(self):
        return self.__schol_Student5

    @schol_Student5.setter
    def schol_Student5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_Student__schol_Student5", None)
        self.__schol_Student5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schol_Student7"):
                    opp_val = getattr(item, "schol_Student7", None)
                    
                    if opp_val == self:
                        setattr(item, "schol_Student7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schol_Student7"):
                    opp_val = getattr(item, "schol_Student7", None)
                    
                    setattr(item, "schol_Student7", self)
                    

    @property
    def schol_Student7(self):
        return self.__schol_Student7

    @schol_Student7.setter
    def schol_Student7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_Student__schol_Student7", None)
        self.__schol_Student7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schol_Student5"):
                opp_val = getattr(old_value, "schol_Student5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schol_Student5"):
                opp_val = getattr(value, "schol_Student5", None)
                if opp_val is None:
                    setattr(value, "schol_Student5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schol_Student(self):
        return self.__schol_Student

    @schol_Student.setter
    def schol_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_Student__schol_Student", None)
        self.__schol_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schol_Classroom"):
                opp_val = getattr(old_value, "schol_Classroom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schol_Classroom"):
                opp_val = getattr(value, "schol_Classroom", None)
                if opp_val is None:
                    setattr(value, "schol_Classroom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class schol_Classroom:

    def __init__(self, name: str, schol_Classroom4: "schol_School" = None, schol_Classroom: set["schol_Student"] = None):
        self.name = name
        self.schol_Classroom4 = schol_Classroom4
        self.schol_Classroom = schol_Classroom if schol_Classroom is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schol_Classroom4(self):
        return self.__schol_Classroom4

    @schol_Classroom4.setter
    def schol_Classroom4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_Classroom__schol_Classroom4", None)
        self.__schol_Classroom4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schol_School3"):
                opp_val = getattr(old_value, "schol_School3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schol_School3"):
                opp_val = getattr(value, "schol_School3", None)
                if opp_val is None:
                    setattr(value, "schol_School3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schol_Classroom(self):
        return self.__schol_Classroom

    @schol_Classroom.setter
    def schol_Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schol_Classroom__schol_Classroom", None)
        self.__schol_Classroom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schol_Student"):
                    opp_val = getattr(item, "schol_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "schol_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schol_Student"):
                    opp_val = getattr(item, "schol_Student", None)
                    
                    setattr(item, "schol_Student", self)
                    
