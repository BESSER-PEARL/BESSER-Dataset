from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class school_School:

    def __init__(self, name: str, school_School: "school_Diagram" = None, school_School3: set["school_Classroom"] = None):
        self.name = name
        self.school_School = school_School
        self.school_School3 = school_School3 if school_School3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_School3(self):
        return self.__school_School3

    @school_School3.setter
    def school_School3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School3", None)
        self.__school_School3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Classroom4"):
                    opp_val = getattr(item, "school_Classroom4", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Classroom4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Classroom4"):
                    opp_val = getattr(item, "school_Classroom4", None)
                    
                    setattr(item, "school_Classroom4", self)
                    

    @property
    def school_School(self):
        return self.__school_School

    @school_School.setter
    def school_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School", None)
        self.__school_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Diagram"):
                opp_val = getattr(old_value, "school_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "school_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Diagram"):
                opp_val = getattr(value, "school_Diagram", None)
                setattr(value, "school_Diagram", self)

class school_Diagram:

    pass
class school_Student:

    def __init__(self, name: str, school_Student: "school_Classroom" = None, school_Student7: "school_Student" = None, school_Student5: set["school_Student"] = None):
        self.name = name
        self.school_Student = school_Student
        self.school_Student7 = school_Student7
        self.school_Student5 = school_Student5 if school_Student5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Student(self):
        return self.__school_Student

    @school_Student.setter
    def school_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student", None)
        self.__school_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Classroom"):
                opp_val = getattr(old_value, "school_Classroom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Classroom"):
                opp_val = getattr(value, "school_Classroom", None)
                if opp_val is None:
                    setattr(value, "school_Classroom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Student5(self):
        return self.__school_Student5

    @school_Student5.setter
    def school_Student5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student5", None)
        self.__school_Student5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student7"):
                    opp_val = getattr(item, "school_Student7", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student7"):
                    opp_val = getattr(item, "school_Student7", None)
                    
                    setattr(item, "school_Student7", self)
                    

    @property
    def school_Student7(self):
        return self.__school_Student7

    @school_Student7.setter
    def school_Student7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student7", None)
        self.__school_Student7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Student5"):
                opp_val = getattr(old_value, "school_Student5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Student5"):
                opp_val = getattr(value, "school_Student5", None)
                if opp_val is None:
                    setattr(value, "school_Student5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_Classroom:

    def __init__(self, name: str, school_Classroom: set["school_Student"] = None, school_Classroom4: "school_School" = None):
        self.name = name
        self.school_Classroom = school_Classroom if school_Classroom is not None else set()
        self.school_Classroom4 = school_Classroom4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Classroom(self):
        return self.__school_Classroom

    @school_Classroom.setter
    def school_Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Classroom__school_Classroom", None)
        self.__school_Classroom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student"):
                    opp_val = getattr(item, "school_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student"):
                    opp_val = getattr(item, "school_Student", None)
                    
                    setattr(item, "school_Student", self)
                    

    @property
    def school_Classroom4(self):
        return self.__school_Classroom4

    @school_Classroom4.setter
    def school_Classroom4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Classroom__school_Classroom4", None)
        self.__school_Classroom4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School3"):
                opp_val = getattr(old_value, "school_School3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School3"):
                opp_val = getattr(value, "school_School3", None)
                if opp_val is None:
                    setattr(value, "school_School3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
