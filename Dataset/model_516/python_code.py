from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class familyleft1_Son:

    def __init__(self, name: str, age: int, sex: str, Son: "familyleft1_Family" = None, sons: "familyleft1_Family" = None):
        self.name = name
        self.age = age
        self.sex = sex
        self.Son = Son
        self.sons = sons
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def Son(self):
        return self.__Son

    @Son.setter
    def Son(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Son__Son", None)
        self.__Son = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family9"):
                opp_val = getattr(old_value, "family9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family9"):
                opp_val = getattr(value, "family9", None)
                if opp_val is None:
                    setattr(value, "family9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sons(self):
        return self.__sons

    @sons.setter
    def sons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Son__sons", None)
        self.__sons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family4"):
                opp_val = getattr(old_value, "Family4", None)
                if opp_val == self:
                    setattr(old_value, "Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family4"):
                opp_val = getattr(value, "Family4", None)
                setattr(value, "Family4", self)

class familyleft1_Father:

    def __init__(self, age: int, name: str, father: "familyleft1_Family" = None, Father: "familyleft1_Family" = None):
        self.age = age
        self.name = name
        self.father = father
        self.Father = Father
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Father__father", None)
        self.__father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family"):
                opp_val = getattr(old_value, "Family", None)
                if opp_val == self:
                    setattr(old_value, "Family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family"):
                opp_val = getattr(value, "Family", None)
                setattr(value, "Family", self)

    @property
    def Father(self):
        return self.__Father

    @Father.setter
    def Father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Father__Father", None)
        self.__Father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family"):
                opp_val = getattr(old_value, "family", None)
                if opp_val == self:
                    setattr(old_value, "family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family"):
                opp_val = getattr(value, "family", None)
                setattr(value, "family", self)

class familyleft1_Mother:

    def __init__(self, name: str, age: int, Mother: "familyleft1_Family" = None, mother: "familyleft1_Family" = None):
        self.name = name
        self.age = age
        self.Mother = Mother
        self.mother = mother
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Mother(self):
        return self.__Mother

    @Mother.setter
    def Mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Mother__Mother", None)
        self.__Mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family7"):
                opp_val = getattr(old_value, "family7", None)
                if opp_val == self:
                    setattr(old_value, "family7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family7"):
                opp_val = getattr(value, "family7", None)
                setattr(value, "family7", self)

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Mother__mother", None)
        self.__mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family2"):
                opp_val = getattr(old_value, "Family2", None)
                if opp_val == self:
                    setattr(old_value, "Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family2"):
                opp_val = getattr(value, "Family2", None)
                setattr(value, "Family2", self)

class familyleft1_Family:

    def __init__(self, surname: str, location: str, Family: "familyleft1_Father" = None, family7: "familyleft1_Mother" = None, family9: set["familyleft1_Son"] = None, Family2: "familyleft1_Mother" = None, Family4: "familyleft1_Son" = None, family: "familyleft1_Father" = None):
        self.surname = surname
        self.location = location
        self.Family = Family
        self.family7 = family7
        self.family9 = family9 if family9 is not None else set()
        self.Family2 = Family2
        self.Family4 = Family4
        self.family = family
        
    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def Family2(self):
        return self.__Family2

    @Family2.setter
    def Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Family__Family2", None)
        self.__Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mother"):
                opp_val = getattr(old_value, "mother", None)
                if opp_val == self:
                    setattr(old_value, "mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mother"):
                opp_val = getattr(value, "mother", None)
                setattr(value, "mother", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "father"):
                opp_val = getattr(old_value, "father", None)
                if opp_val == self:
                    setattr(old_value, "father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "father"):
                opp_val = getattr(value, "father", None)
                setattr(value, "father", self)

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Family__family", None)
        self.__family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Father"):
                opp_val = getattr(old_value, "Father", None)
                if opp_val == self:
                    setattr(old_value, "Father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Father"):
                opp_val = getattr(value, "Father", None)
                setattr(value, "Father", self)

    @property
    def family9(self):
        return self.__family9

    @family9.setter
    def family9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Family__family9", None)
        self.__family9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Son"):
                    opp_val = getattr(item, "Son", None)
                    
                    if opp_val == self:
                        setattr(item, "Son", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Son"):
                    opp_val = getattr(item, "Son", None)
                    
                    setattr(item, "Son", self)
                    

    @property
    def family7(self):
        return self.__family7

    @family7.setter
    def family7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Family__family7", None)
        self.__family7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mother"):
                opp_val = getattr(old_value, "Mother", None)
                if opp_val == self:
                    setattr(old_value, "Mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mother"):
                opp_val = getattr(value, "Mother", None)
                setattr(value, "Mother", self)

    @property
    def Family4(self):
        return self.__Family4

    @Family4.setter
    def Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft1_Family__Family4", None)
        self.__Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sons"):
                opp_val = getattr(old_value, "sons", None)
                if opp_val == self:
                    setattr(old_value, "sons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sons"):
                opp_val = getattr(value, "sons", None)
                setattr(value, "sons", self)
