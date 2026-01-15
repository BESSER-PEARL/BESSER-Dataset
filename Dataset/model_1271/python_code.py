from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_ecore_Person:

    def __init__(self, name: str, age: int, family_ecore_Person4: "family_ecore_Person" = None, family_ecore_Person2: set["family_ecore_Person"] = None, family_ecore_Person7: "family_ecore_Person" = None, family_ecore_Person5: set["family_ecore_Person"] = None, family_ecore_Person9: "family_ecore_Family" = None, family_ecore_Person: "family_ecore_Person" = None, family_ecore_Person0: "family_ecore_Person" = None):
        self.name = name
        self.age = age
        self.family_ecore_Person4 = family_ecore_Person4
        self.family_ecore_Person2 = family_ecore_Person2 if family_ecore_Person2 is not None else set()
        self.family_ecore_Person7 = family_ecore_Person7
        self.family_ecore_Person5 = family_ecore_Person5 if family_ecore_Person5 is not None else set()
        self.family_ecore_Person9 = family_ecore_Person9
        self.family_ecore_Person = family_ecore_Person
        self.family_ecore_Person0 = family_ecore_Person0
        
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
    def family_ecore_Person5(self):
        return self.__family_ecore_Person5

    @family_ecore_Person5.setter
    def family_ecore_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person5", None)
        self.__family_ecore_Person5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_ecore_Person7"):
                    opp_val = getattr(item, "family_ecore_Person7", None)
                    
                    if opp_val == self:
                        setattr(item, "family_ecore_Person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_ecore_Person7"):
                    opp_val = getattr(item, "family_ecore_Person7", None)
                    
                    setattr(item, "family_ecore_Person7", self)
                    

    @property
    def family_ecore_Person0(self):
        return self.__family_ecore_Person0

    @family_ecore_Person0.setter
    def family_ecore_Person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person0", None)
        self.__family_ecore_Person0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_ecore_Person"):
                opp_val = getattr(old_value, "family_ecore_Person", None)
                if opp_val == self:
                    setattr(old_value, "family_ecore_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_ecore_Person"):
                opp_val = getattr(value, "family_ecore_Person", None)
                setattr(value, "family_ecore_Person", self)

    @property
    def family_ecore_Person7(self):
        return self.__family_ecore_Person7

    @family_ecore_Person7.setter
    def family_ecore_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person7", None)
        self.__family_ecore_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_ecore_Person5"):
                opp_val = getattr(old_value, "family_ecore_Person5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_ecore_Person5"):
                opp_val = getattr(value, "family_ecore_Person5", None)
                if opp_val is None:
                    setattr(value, "family_ecore_Person5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_ecore_Person4(self):
        return self.__family_ecore_Person4

    @family_ecore_Person4.setter
    def family_ecore_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person4", None)
        self.__family_ecore_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_ecore_Person2"):
                opp_val = getattr(old_value, "family_ecore_Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_ecore_Person2"):
                opp_val = getattr(value, "family_ecore_Person2", None)
                if opp_val is None:
                    setattr(value, "family_ecore_Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_ecore_Person(self):
        return self.__family_ecore_Person

    @family_ecore_Person.setter
    def family_ecore_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person", None)
        self.__family_ecore_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_ecore_Person0"):
                opp_val = getattr(old_value, "family_ecore_Person0", None)
                if opp_val == self:
                    setattr(old_value, "family_ecore_Person0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_ecore_Person0"):
                opp_val = getattr(value, "family_ecore_Person0", None)
                setattr(value, "family_ecore_Person0", self)

    @property
    def family_ecore_Person9(self):
        return self.__family_ecore_Person9

    @family_ecore_Person9.setter
    def family_ecore_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person9", None)
        self.__family_ecore_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_ecore_Family"):
                opp_val = getattr(old_value, "family_ecore_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_ecore_Family"):
                opp_val = getattr(value, "family_ecore_Family", None)
                if opp_val is None:
                    setattr(value, "family_ecore_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_ecore_Person2(self):
        return self.__family_ecore_Person2

    @family_ecore_Person2.setter
    def family_ecore_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_ecore_Person__family_ecore_Person2", None)
        self.__family_ecore_Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_ecore_Person4"):
                    opp_val = getattr(item, "family_ecore_Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "family_ecore_Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_ecore_Person4"):
                    opp_val = getattr(item, "family_ecore_Person4", None)
                    
                    setattr(item, "family_ecore_Person4", self)
                    

class family_ecore_Family:

    pass