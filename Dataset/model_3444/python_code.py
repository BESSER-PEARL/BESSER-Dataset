from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class schul_Diagram:

    pass
class schul_Student:

    def __init__(self, name: str, schul_Student7: "schul_Student" = None, schul_Student5: set["schul_Student"] = None, schul_Student: "schul_Classroom" = None):
        self.name = name
        self.schul_Student7 = schul_Student7
        self.schul_Student5 = schul_Student5 if schul_Student5 is not None else set()
        self.schul_Student = schul_Student
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schul_Student(self):
        return self.__schul_Student

    @schul_Student.setter
    def schul_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_Student__schul_Student", None)
        self.__schul_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schul_Classroom"):
                opp_val = getattr(old_value, "schul_Classroom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schul_Classroom"):
                opp_val = getattr(value, "schul_Classroom", None)
                if opp_val is None:
                    setattr(value, "schul_Classroom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schul_Student7(self):
        return self.__schul_Student7

    @schul_Student7.setter
    def schul_Student7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_Student__schul_Student7", None)
        self.__schul_Student7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schul_Student5"):
                opp_val = getattr(old_value, "schul_Student5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schul_Student5"):
                opp_val = getattr(value, "schul_Student5", None)
                if opp_val is None:
                    setattr(value, "schul_Student5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schul_Student5(self):
        return self.__schul_Student5

    @schul_Student5.setter
    def schul_Student5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_Student__schul_Student5", None)
        self.__schul_Student5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schul_Student7"):
                    opp_val = getattr(item, "schul_Student7", None)
                    
                    if opp_val == self:
                        setattr(item, "schul_Student7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schul_Student7"):
                    opp_val = getattr(item, "schul_Student7", None)
                    
                    setattr(item, "schul_Student7", self)
                    

class schul_Classroom:

    def __init__(self, name: str, schul_Classroom4: "schul_School" = None, schul_Classroom: set["schul_Student"] = None):
        self.name = name
        self.schul_Classroom4 = schul_Classroom4
        self.schul_Classroom = schul_Classroom if schul_Classroom is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schul_Classroom4(self):
        return self.__schul_Classroom4

    @schul_Classroom4.setter
    def schul_Classroom4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_Classroom__schul_Classroom4", None)
        self.__schul_Classroom4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schul_School3"):
                opp_val = getattr(old_value, "schul_School3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schul_School3"):
                opp_val = getattr(value, "schul_School3", None)
                if opp_val is None:
                    setattr(value, "schul_School3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schul_Classroom(self):
        return self.__schul_Classroom

    @schul_Classroom.setter
    def schul_Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_Classroom__schul_Classroom", None)
        self.__schul_Classroom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schul_Student"):
                    opp_val = getattr(item, "schul_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "schul_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schul_Student"):
                    opp_val = getattr(item, "schul_Student", None)
                    
                    setattr(item, "schul_Student", self)
                    

class schul_School:

    def __init__(self, name: str, schul_School: "schul_Diagram" = None, schul_School3: set["schul_Classroom"] = None):
        self.name = name
        self.schul_School = schul_School
        self.schul_School3 = schul_School3 if schul_School3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schul_School3(self):
        return self.__schul_School3

    @schul_School3.setter
    def schul_School3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_School__schul_School3", None)
        self.__schul_School3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schul_Classroom4"):
                    opp_val = getattr(item, "schul_Classroom4", None)
                    
                    if opp_val == self:
                        setattr(item, "schul_Classroom4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schul_Classroom4"):
                    opp_val = getattr(item, "schul_Classroom4", None)
                    
                    setattr(item, "schul_Classroom4", self)
                    

    @property
    def schul_School(self):
        return self.__schul_School

    @schul_School.setter
    def schul_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schul_School__schul_School", None)
        self.__schul_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schul_Diagram"):
                opp_val = getattr(old_value, "schul_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "schul_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schul_Diagram"):
                opp_val = getattr(value, "schul_Diagram", None)
                setattr(value, "schul_Diagram", self)
