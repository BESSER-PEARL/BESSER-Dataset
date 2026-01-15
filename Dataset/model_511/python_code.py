from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class familyright_Father:

    def __init__(self, name: str, age: int, address: str, father: "familyright_Family" = None, Father: "familyright_Family" = None):
        self.name = name
        self.age = age
        self.address = address
        self.father = father
        self.Father = Father
        
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
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Father__father", None)
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
        old_value = getattr(self, f"_familyright_Father__Father", None)
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

class familyright_Daughter:

    def __init__(self, name: str, age: int, daughters: "familyright_Family" = None, Daughter: "familyright_Family" = None):
        self.name = name
        self.age = age
        self.daughters = daughters
        self.Daughter = Daughter
        
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
    def daughters(self):
        return self.__daughters

    @daughters.setter
    def daughters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Daughter__daughters", None)
        self.__daughters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family6"):
                opp_val = getattr(old_value, "Family6", None)
                if opp_val == self:
                    setattr(old_value, "Family6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family6"):
                opp_val = getattr(value, "Family6", None)
                setattr(value, "Family6", self)

    @property
    def Daughter(self):
        return self.__Daughter

    @Daughter.setter
    def Daughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Daughter__Daughter", None)
        self.__Daughter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family13"):
                opp_val = getattr(old_value, "family13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family13"):
                opp_val = getattr(value, "family13", None)
                if opp_val is None:
                    setattr(value, "family13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class familyright_Son:

    def __init__(self, name: str, age: int, sons: "familyright_Family" = None, Son: "familyright_Family" = None):
        self.name = name
        self.age = age
        self.sons = sons
        self.Son = Son
        
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
    def sons(self):
        return self.__sons

    @sons.setter
    def sons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Son__sons", None)
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

    @property
    def Son(self):
        return self.__Son

    @Son.setter
    def Son(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Son__Son", None)
        self.__Son = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family11"):
                opp_val = getattr(old_value, "family11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family11"):
                opp_val = getattr(value, "family11", None)
                if opp_val is None:
                    setattr(value, "family11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class familyright_Mother:

    def __init__(self, name: str, age: int, address: str, mother: "familyright_Family" = None, Mother: "familyright_Family" = None):
        self.name = name
        self.age = age
        self.address = address
        self.mother = mother
        self.Mother = Mother
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def Mother(self):
        return self.__Mother

    @Mother.setter
    def Mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Mother__Mother", None)
        self.__Mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family9"):
                opp_val = getattr(old_value, "family9", None)
                if opp_val == self:
                    setattr(old_value, "family9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family9"):
                opp_val = getattr(value, "family9", None)
                setattr(value, "family9", self)

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyright_Mother__mother", None)
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

class familyright_Family:

    pass