from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lMS_Course:

    def __init__(self, name: str, lMS_Course: "lMS_LMS" = None):
        self.name = name
        self.lMS_Course = lMS_Course
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lMS_Course(self):
        return self.__lMS_Course

    @lMS_Course.setter
    def lMS_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lMS_Course__lMS_Course", None)
        self.__lMS_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lMS_LMS"):
                opp_val = getattr(old_value, "lMS_LMS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lMS_LMS"):
                opp_val = getattr(value, "lMS_LMS", None)
                if opp_val is None:
                    setattr(value, "lMS_LMS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lMS_LMS:

    def __init__(self, description: str, lMS_LMS: set["lMS_Course"] = None):
        self.description = description
        self.lMS_LMS = lMS_LMS if lMS_LMS is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def lMS_LMS(self):
        return self.__lMS_LMS

    @lMS_LMS.setter
    def lMS_LMS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lMS_LMS__lMS_LMS", None)
        self.__lMS_LMS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lMS_Course"):
                    opp_val = getattr(item, "lMS_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "lMS_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lMS_Course"):
                    opp_val = getattr(item, "lMS_Course", None)
                    
                    setattr(item, "lMS_Course", self)
                    
