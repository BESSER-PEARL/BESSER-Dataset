from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class university_Course:

    def __init__(self, id: str, name: str, etcs: int, university_Course: "university_CourseCatalog" = None):
        self.id = id
        self.name = name
        self.etcs = etcs
        self.university_Course = university_Course
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def etcs(self) -> int:
        return self.__etcs

    @etcs.setter
    def etcs(self, etcs: int):
        self.__etcs = etcs

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def university_Course(self):
        return self.__university_Course

    @university_Course.setter
    def university_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__university_Course", None)
        self.__university_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_CourseCatalog"):
                opp_val = getattr(old_value, "university_CourseCatalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_CourseCatalog"):
                opp_val = getattr(value, "university_CourseCatalog", None)
                if opp_val is None:
                    setattr(value, "university_CourseCatalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_CourseCatalog:

    pass