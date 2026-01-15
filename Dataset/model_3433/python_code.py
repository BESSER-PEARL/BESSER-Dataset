from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class school_SchoolYear:

    def __init__(self, year: date, school_SchoolYear: set["school_ClassGroup"] = None, school_SchoolYear13: set["school_Student"] = None, school_SchoolYear16: set["school_ClassLevel"] = None):
        self.year = year
        self.school_SchoolYear = school_SchoolYear if school_SchoolYear is not None else set()
        self.school_SchoolYear13 = school_SchoolYear13 if school_SchoolYear13 is not None else set()
        self.school_SchoolYear16 = school_SchoolYear16 if school_SchoolYear16 is not None else set()
        
    @property
    def year(self) -> date:
        return self.__year

    @year.setter
    def year(self, year: date):
        self.__year = year

    @property
    def school_SchoolYear13(self):
        return self.__school_SchoolYear13

    @school_SchoolYear13.setter
    def school_SchoolYear13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolYear__school_SchoolYear13", None)
        self.__school_SchoolYear13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student14"):
                    opp_val = getattr(item, "school_Student14", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student14"):
                    opp_val = getattr(item, "school_Student14", None)
                    
                    setattr(item, "school_Student14", self)
                    

    @property
    def school_SchoolYear16(self):
        return self.__school_SchoolYear16

    @school_SchoolYear16.setter
    def school_SchoolYear16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolYear__school_SchoolYear16", None)
        self.__school_SchoolYear16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_ClassLevel17"):
                    opp_val = getattr(item, "school_ClassLevel17", None)
                    
                    if opp_val == self:
                        setattr(item, "school_ClassLevel17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_ClassLevel17"):
                    opp_val = getattr(item, "school_ClassLevel17", None)
                    
                    setattr(item, "school_ClassLevel17", self)
                    

    @property
    def school_SchoolYear(self):
        return self.__school_SchoolYear

    @school_SchoolYear.setter
    def school_SchoolYear(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolYear__school_SchoolYear", None)
        self.__school_SchoolYear = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_ClassGroup11"):
                    opp_val = getattr(item, "school_ClassGroup11", None)
                    
                    if opp_val == self:
                        setattr(item, "school_ClassGroup11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_ClassGroup11"):
                    opp_val = getattr(item, "school_ClassGroup11", None)
                    
                    setattr(item, "school_ClassGroup11", self)
                    

class school_store:

    def __init__(self, lastIn: str):
        self.lastIn = lastIn
        
    @property
    def lastIn(self) -> str:
        return self.__lastIn

    @lastIn.setter
    def lastIn(self, lastIn: str):
        self.__lastIn = lastIn

class school_NewEClass7:

    pass
class school_Room:

    def __init__(self, location: str, school_Room9: "school_Teacher" = None, school_Room: "school_ClassGroup" = None):
        self.location = location
        self.school_Room9 = school_Room9
        self.school_Room = school_Room
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def school_Room(self):
        return self.__school_Room

    @school_Room.setter
    def school_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Room__school_Room", None)
        self.__school_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_ClassGroup6"):
                opp_val = getattr(old_value, "school_ClassGroup6", None)
                if opp_val == self:
                    setattr(old_value, "school_ClassGroup6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassGroup6"):
                opp_val = getattr(value, "school_ClassGroup6", None)
                setattr(value, "school_ClassGroup6", self)

    @property
    def school_Room9(self):
        return self.__school_Room9

    @school_Room9.setter
    def school_Room9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Room__school_Room9", None)
        self.__school_Room9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Teacher8"):
                opp_val = getattr(old_value, "school_Teacher8", None)
                if opp_val == self:
                    setattr(old_value, "school_Teacher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Teacher8"):
                opp_val = getattr(value, "school_Teacher8", None)
                setattr(value, "school_Teacher8", self)

    def AffectTeacher(self, t: str) -> str:
        # TODO: Implement AffectTeacher method
        pass

class school_ClassLevel:

    def __init__(self, level: int, school_ClassLevel: "school_ClassGroup" = None, school_ClassLevel17: "school_SchoolYear" = None):
        self.level = level
        self.school_ClassLevel = school_ClassLevel
        self.school_ClassLevel17 = school_ClassLevel17
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def school_ClassLevel(self):
        return self.__school_ClassLevel

    @school_ClassLevel.setter
    def school_ClassLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassLevel__school_ClassLevel", None)
        self.__school_ClassLevel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_ClassGroup4"):
                opp_val = getattr(old_value, "school_ClassGroup4", None)
                if opp_val == self:
                    setattr(old_value, "school_ClassGroup4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassGroup4"):
                opp_val = getattr(value, "school_ClassGroup4", None)
                setattr(value, "school_ClassGroup4", self)

    @property
    def school_ClassLevel17(self):
        return self.__school_ClassLevel17

    @school_ClassLevel17.setter
    def school_ClassLevel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassLevel__school_ClassLevel17", None)
        self.__school_ClassLevel17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolYear16"):
                opp_val = getattr(old_value, "school_SchoolYear16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolYear16"):
                opp_val = getattr(value, "school_SchoolYear16", None)
                if opp_val is None:
                    setattr(value, "school_SchoolYear16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_Teacher:

    def __init__(self, name: str, school_Teacher8: "school_Room" = None, school_Teacher: "school_ClassGroup" = None):
        self.name = name
        self.school_Teacher8 = school_Teacher8
        self.school_Teacher = school_Teacher
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Teacher(self):
        return self.__school_Teacher

    @school_Teacher.setter
    def school_Teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__school_Teacher", None)
        self.__school_Teacher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_ClassGroup2"):
                opp_val = getattr(old_value, "school_ClassGroup2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassGroup2"):
                opp_val = getattr(value, "school_ClassGroup2", None)
                if opp_val is None:
                    setattr(value, "school_ClassGroup2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Teacher8(self):
        return self.__school_Teacher8

    @school_Teacher8.setter
    def school_Teacher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__school_Teacher8", None)
        self.__school_Teacher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Room9"):
                opp_val = getattr(old_value, "school_Room9", None)
                if opp_val == self:
                    setattr(old_value, "school_Room9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Room9"):
                opp_val = getattr(value, "school_Room9", None)
                setattr(value, "school_Room9", self)

class school_Student:

    def __init__(self, name: str, school_Student: "school_ClassGroup" = None, school_Student14: "school_SchoolYear" = None):
        self.name = name
        self.school_Student = school_Student
        self.school_Student14 = school_Student14
        
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
            if hasattr(old_value, "school_ClassGroup"):
                opp_val = getattr(old_value, "school_ClassGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassGroup"):
                opp_val = getattr(value, "school_ClassGroup", None)
                if opp_val is None:
                    setattr(value, "school_ClassGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Student14(self):
        return self.__school_Student14

    @school_Student14.setter
    def school_Student14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student14", None)
        self.__school_Student14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolYear13"):
                opp_val = getattr(old_value, "school_SchoolYear13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolYear13"):
                opp_val = getattr(value, "school_SchoolYear13", None)
                if opp_val is None:
                    setattr(value, "school_SchoolYear13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_ClassGroup:

    def __init__(self, name: str, school_ClassGroup: set["school_Student"] = None, school_ClassGroup2: set["school_Teacher"] = None, school_ClassGroup4: "school_ClassLevel" = None, school_ClassGroup6: "school_Room" = None, school_ClassGroup11: "school_SchoolYear" = None):
        self.name = name
        self.school_ClassGroup = school_ClassGroup if school_ClassGroup is not None else set()
        self.school_ClassGroup2 = school_ClassGroup2 if school_ClassGroup2 is not None else set()
        self.school_ClassGroup4 = school_ClassGroup4
        self.school_ClassGroup6 = school_ClassGroup6
        self.school_ClassGroup11 = school_ClassGroup11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_ClassGroup2(self):
        return self.__school_ClassGroup2

    @school_ClassGroup2.setter
    def school_ClassGroup2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassGroup__school_ClassGroup2", None)
        self.__school_ClassGroup2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Teacher"):
                    opp_val = getattr(item, "school_Teacher", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Teacher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Teacher"):
                    opp_val = getattr(item, "school_Teacher", None)
                    
                    setattr(item, "school_Teacher", self)
                    

    @property
    def school_ClassGroup6(self):
        return self.__school_ClassGroup6

    @school_ClassGroup6.setter
    def school_ClassGroup6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassGroup__school_ClassGroup6", None)
        self.__school_ClassGroup6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Room"):
                opp_val = getattr(old_value, "school_Room", None)
                if opp_val == self:
                    setattr(old_value, "school_Room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Room"):
                opp_val = getattr(value, "school_Room", None)
                setattr(value, "school_Room", self)

    @property
    def school_ClassGroup11(self):
        return self.__school_ClassGroup11

    @school_ClassGroup11.setter
    def school_ClassGroup11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassGroup__school_ClassGroup11", None)
        self.__school_ClassGroup11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolYear"):
                opp_val = getattr(old_value, "school_SchoolYear", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolYear"):
                opp_val = getattr(value, "school_SchoolYear", None)
                if opp_val is None:
                    setattr(value, "school_SchoolYear", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_ClassGroup(self):
        return self.__school_ClassGroup

    @school_ClassGroup.setter
    def school_ClassGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassGroup__school_ClassGroup", None)
        self.__school_ClassGroup = value if value is not None else set()
        
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
    def school_ClassGroup4(self):
        return self.__school_ClassGroup4

    @school_ClassGroup4.setter
    def school_ClassGroup4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassGroup__school_ClassGroup4", None)
        self.__school_ClassGroup4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_ClassLevel"):
                opp_val = getattr(old_value, "school_ClassLevel", None)
                if opp_val == self:
                    setattr(old_value, "school_ClassLevel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassLevel"):
                opp_val = getattr(value, "school_ClassLevel", None)
                setattr(value, "school_ClassLevel", self)
