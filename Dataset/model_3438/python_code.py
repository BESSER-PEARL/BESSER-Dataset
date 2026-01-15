from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class school_School:

    def __init__(self, zipCode: str, city: str, name: str, director: str, school_School: set["school_Classroom"] = None):
        self.zipCode = zipCode
        self.city = city
        self.name = name
        self.director = director
        self.school_School = school_School if school_School is not None else set()
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, director: str):
        self.__director = director

    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def school_School(self):
        return self.__school_School

    @school_School.setter
    def school_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School", None)
        self.__school_School = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Classroom2"):
                    opp_val = getattr(item, "school_Classroom2", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Classroom2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Classroom2"):
                    opp_val = getattr(item, "school_Classroom2", None)
                    
                    setattr(item, "school_Classroom2", self)
                    

class school_Student:

    def __init__(self, name: str, nickname: str, age: int, school_Student: "school_Classroom" = None, school_Student5: "school_Student" = None, school_Student3: set["school_Student"] = None):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.school_Student = school_Student
        self.school_Student5 = school_Student5
        self.school_Student3 = school_Student3 if school_Student3 is not None else set()
        
    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

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
    def school_Student3(self):
        return self.__school_Student3

    @school_Student3.setter
    def school_Student3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student3", None)
        self.__school_Student3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student5"):
                    opp_val = getattr(item, "school_Student5", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student5"):
                    opp_val = getattr(item, "school_Student5", None)
                    
                    setattr(item, "school_Student5", self)
                    

    @property
    def school_Student5(self):
        return self.__school_Student5

    @school_Student5.setter
    def school_Student5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student5", None)
        self.__school_Student5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Student3"):
                opp_val = getattr(old_value, "school_Student3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Student3"):
                opp_val = getattr(value, "school_Student3", None)
                if opp_val is None:
                    setattr(value, "school_Student3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class school_Classroom:

    def __init__(self, name: str, teacher: str, rank: int, capacity: int, school_Classroom: set["school_Student"] = None, school_Classroom2: "school_School" = None):
        self.name = name
        self.teacher = teacher
        self.rank = rank
        self.capacity = capacity
        self.school_Classroom = school_Classroom if school_Classroom is not None else set()
        self.school_Classroom2 = school_Classroom2
        
    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def teacher(self) -> str:
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher: str):
        self.__teacher = teacher

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

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
    def school_Classroom2(self):
        return self.__school_Classroom2

    @school_Classroom2.setter
    def school_Classroom2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Classroom__school_Classroom2", None)
        self.__school_Classroom2 = value
        
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

    def validate(self, diagnostic: str, context: str) -> bool:
        # TODO: Implement validate method
        pass
