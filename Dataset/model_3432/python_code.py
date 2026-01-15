from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Matter:

    pass
class school_Math(Matter):

    pass
class school_Matter:

    pass
class school_ClassRoom:

    def __init__(self, number: int, school_ClassRoom: "school_School" = None, school_ClassRoom14: "school_Teacher" = None, school_ClassRoom17: set["school_Student"] = None):
        self.number = number
        self.school_ClassRoom = school_ClassRoom
        self.school_ClassRoom14 = school_ClassRoom14
        self.school_ClassRoom17 = school_ClassRoom17 if school_ClassRoom17 is not None else set()
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def school_ClassRoom17(self):
        return self.__school_ClassRoom17

    @school_ClassRoom17.setter
    def school_ClassRoom17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassRoom__school_ClassRoom17", None)
        self.__school_ClassRoom17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student18"):
                    opp_val = getattr(item, "school_Student18", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student18"):
                    opp_val = getattr(item, "school_Student18", None)
                    
                    setattr(item, "school_Student18", self)
                    

    @property
    def school_ClassRoom14(self):
        return self.__school_ClassRoom14

    @school_ClassRoom14.setter
    def school_ClassRoom14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassRoom__school_ClassRoom14", None)
        self.__school_ClassRoom14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Teacher15"):
                opp_val = getattr(old_value, "school_Teacher15", None)
                if opp_val == self:
                    setattr(old_value, "school_Teacher15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Teacher15"):
                opp_val = getattr(value, "school_Teacher15", None)
                setattr(value, "school_Teacher15", self)

    @property
    def school_ClassRoom(self):
        return self.__school_ClassRoom

    @school_ClassRoom.setter
    def school_ClassRoom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_ClassRoom__school_ClassRoom", None)
        self.__school_ClassRoom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School6"):
                opp_val = getattr(old_value, "school_School6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School6"):
                opp_val = getattr(value, "school_School6", None)
                if opp_val is None:
                    setattr(value, "school_School6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_Notation:

    def __init__(self, value: int, school_Notation: "school_Student" = None):
        self.value = value
        self.school_Notation = school_Notation
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def school_Notation(self):
        return self.__school_Notation

    @school_Notation.setter
    def school_Notation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Notation__school_Notation", None)
        self.__school_Notation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Student20"):
                opp_val = getattr(old_value, "school_Student20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Student20"):
                opp_val = getattr(value, "school_Student20", None)
                if opp_val is None:
                    setattr(value, "school_Student20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_Teacher:

    def __init__(self, name: str, school_Teacher: "school_Academy" = None, school_Teacher9: "school_School" = None, school_Teacher15: "school_ClassRoom" = None):
        self.name = name
        self.school_Teacher = school_Teacher
        self.school_Teacher9 = school_Teacher9
        self.school_Teacher15 = school_Teacher15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Teacher9(self):
        return self.__school_Teacher9

    @school_Teacher9.setter
    def school_Teacher9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__school_Teacher9", None)
        self.__school_Teacher9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School8"):
                opp_val = getattr(old_value, "school_School8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School8"):
                opp_val = getattr(value, "school_School8", None)
                if opp_val is None:
                    setattr(value, "school_School8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "school_Academy"):
                opp_val = getattr(old_value, "school_Academy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Academy"):
                opp_val = getattr(value, "school_Academy", None)
                if opp_val is None:
                    setattr(value, "school_Academy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Teacher15(self):
        return self.__school_Teacher15

    @school_Teacher15.setter
    def school_Teacher15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__school_Teacher15", None)
        self.__school_Teacher15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_ClassRoom14"):
                opp_val = getattr(old_value, "school_ClassRoom14", None)
                if opp_val == self:
                    setattr(old_value, "school_ClassRoom14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassRoom14"):
                opp_val = getattr(value, "school_ClassRoom14", None)
                setattr(value, "school_ClassRoom14", self)

    def evaluate(self, student: str) -> str:
        # TODO: Implement evaluate method
        pass

class school_Academy:

    def __init__(self, name: str, school_Academy2: set["school_Student"] = None, school_Academy4: set["school_School"] = None, school_Academy: set["school_Teacher"] = None):
        self.name = name
        self.school_Academy2 = school_Academy2 if school_Academy2 is not None else set()
        self.school_Academy4 = school_Academy4 if school_Academy4 is not None else set()
        self.school_Academy = school_Academy if school_Academy is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Academy4(self):
        return self.__school_Academy4

    @school_Academy4.setter
    def school_Academy4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Academy__school_Academy4", None)
        self.__school_Academy4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_School"):
                    opp_val = getattr(item, "school_School", None)
                    
                    if opp_val == self:
                        setattr(item, "school_School", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_School"):
                    opp_val = getattr(item, "school_School", None)
                    
                    setattr(item, "school_School", self)
                    

    @property
    def school_Academy2(self):
        return self.__school_Academy2

    @school_Academy2.setter
    def school_Academy2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Academy__school_Academy2", None)
        self.__school_Academy2 = value if value is not None else set()
        
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
    def school_Academy(self):
        return self.__school_Academy

    @school_Academy.setter
    def school_Academy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Academy__school_Academy", None)
        self.__school_Academy = value if value is not None else set()
        
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
                    

class school_School:

    def __init__(self, name: str, rank: int, school_School: "school_Academy" = None, school_School6: set["school_ClassRoom"] = None, school_School8: set["school_Teacher"] = None, school_School11: set["school_Student"] = None):
        self.name = name
        self.rank = rank
        self.school_School = school_School
        self.school_School6 = school_School6 if school_School6 is not None else set()
        self.school_School8 = school_School8 if school_School8 is not None else set()
        self.school_School11 = school_School11 if school_School11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

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
            if hasattr(old_value, "school_Academy4"):
                opp_val = getattr(old_value, "school_Academy4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Academy4"):
                opp_val = getattr(value, "school_Academy4", None)
                if opp_val is None:
                    setattr(value, "school_Academy4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_School6(self):
        return self.__school_School6

    @school_School6.setter
    def school_School6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School6", None)
        self.__school_School6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_ClassRoom"):
                    opp_val = getattr(item, "school_ClassRoom", None)
                    
                    if opp_val == self:
                        setattr(item, "school_ClassRoom", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_ClassRoom"):
                    opp_val = getattr(item, "school_ClassRoom", None)
                    
                    setattr(item, "school_ClassRoom", self)
                    

    @property
    def school_School11(self):
        return self.__school_School11

    @school_School11.setter
    def school_School11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School11", None)
        self.__school_School11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student12"):
                    opp_val = getattr(item, "school_Student12", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student12"):
                    opp_val = getattr(item, "school_Student12", None)
                    
                    setattr(item, "school_Student12", self)
                    

    @property
    def school_School8(self):
        return self.__school_School8

    @school_School8.setter
    def school_School8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School8", None)
        self.__school_School8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Teacher9"):
                    opp_val = getattr(item, "school_Teacher9", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Teacher9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Teacher9"):
                    opp_val = getattr(item, "school_Teacher9", None)
                    
                    setattr(item, "school_Teacher9", self)
                    

class school_Student:

    def __init__(self, name: str, age: int, school_Student: "school_Academy" = None, school_Student20: set["school_Notation"] = None, school_Student12: "school_School" = None, school_Student18: "school_ClassRoom" = None):
        self.name = name
        self.age = age
        self.school_Student = school_Student
        self.school_Student20 = school_Student20 if school_Student20 is not None else set()
        self.school_Student12 = school_Student12
        self.school_Student18 = school_Student18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def school_Student18(self):
        return self.__school_Student18

    @school_Student18.setter
    def school_Student18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student18", None)
        self.__school_Student18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_ClassRoom17"):
                opp_val = getattr(old_value, "school_ClassRoom17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_ClassRoom17"):
                opp_val = getattr(value, "school_ClassRoom17", None)
                if opp_val is None:
                    setattr(value, "school_ClassRoom17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Student12(self):
        return self.__school_Student12

    @school_Student12.setter
    def school_Student12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student12", None)
        self.__school_Student12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School11"):
                opp_val = getattr(old_value, "school_School11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School11"):
                opp_val = getattr(value, "school_School11", None)
                if opp_val is None:
                    setattr(value, "school_School11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Student20(self):
        return self.__school_Student20

    @school_Student20.setter
    def school_Student20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student20", None)
        self.__school_Student20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Notation"):
                    opp_val = getattr(item, "school_Notation", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Notation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Notation"):
                    opp_val = getattr(item, "school_Notation", None)
                    
                    setattr(item, "school_Notation", self)
                    

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
            if hasattr(old_value, "school_Academy2"):
                opp_val = getattr(old_value, "school_Academy2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Academy2"):
                opp_val = getattr(value, "school_Academy2", None)
                if opp_val is None:
                    setattr(value, "school_Academy2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
