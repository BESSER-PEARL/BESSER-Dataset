from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book:

    pass
class school_SpecialBook(Book):

    pass
class school_Book:

    pass
class school_Pupil:

    def __init__(self, name: str, school_Pupil: "school_School" = None, school_Pupil2: set["school_Book"] = None):
        self.name = name
        self.school_Pupil = school_Pupil
        self.school_Pupil2 = school_Pupil2 if school_Pupil2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Pupil(self):
        return self.__school_Pupil

    @school_Pupil.setter
    def school_Pupil(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Pupil__school_Pupil", None)
        self.__school_Pupil = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School"):
                opp_val = getattr(old_value, "school_School", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School"):
                opp_val = getattr(value, "school_School", None)
                if opp_val is None:
                    setattr(value, "school_School", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Pupil2(self):
        return self.__school_Pupil2

    @school_Pupil2.setter
    def school_Pupil2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Pupil__school_Pupil2", None)
        self.__school_Pupil2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Book"):
                    opp_val = getattr(item, "school_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Book"):
                    opp_val = getattr(item, "school_Book", None)
                    
                    setattr(item, "school_Book", self)
                    

class school_School:

    pass