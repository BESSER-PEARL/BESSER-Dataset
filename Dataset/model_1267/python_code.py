from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_person:

    def __init__(self, name: str, age: str, cpr: str, family_person: "family_person" = None, family_person1: "family_person" = None, family_person5: "family_person" = None, family_person3: set["family_person"] = None, family_person8: "family_person" = None, family_person6: set["family_person"] = None, family_person10: "family_family" = None, family_person13: "family_studyprogramme" = None):
        self.name = name
        self.age = age
        self.cpr = cpr
        self.family_person = family_person
        self.family_person1 = family_person1
        self.family_person5 = family_person5
        self.family_person3 = family_person3 if family_person3 is not None else set()
        self.family_person8 = family_person8
        self.family_person6 = family_person6 if family_person6 is not None else set()
        self.family_person10 = family_person10
        self.family_person13 = family_person13
        
    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def cpr(self) -> str:
        return self.__cpr

    @cpr.setter
    def cpr(self, cpr: str):
        self.__cpr = cpr

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_person3(self):
        return self.__family_person3

    @family_person3.setter
    def family_person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person3", None)
        self.__family_person3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_person5"):
                    opp_val = getattr(item, "family_person5", None)
                    
                    if opp_val == self:
                        setattr(item, "family_person5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_person5"):
                    opp_val = getattr(item, "family_person5", None)
                    
                    setattr(item, "family_person5", self)
                    

    @property
    def family_person(self):
        return self.__family_person

    @family_person.setter
    def family_person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person", None)
        self.__family_person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person1"):
                opp_val = getattr(old_value, "family_person1", None)
                if opp_val == self:
                    setattr(old_value, "family_person1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person1"):
                opp_val = getattr(value, "family_person1", None)
                setattr(value, "family_person1", self)

    @property
    def family_person10(self):
        return self.__family_person10

    @family_person10.setter
    def family_person10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person10", None)
        self.__family_person10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_family"):
                opp_val = getattr(old_value, "family_family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_family"):
                opp_val = getattr(value, "family_family", None)
                if opp_val is None:
                    setattr(value, "family_family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_person1(self):
        return self.__family_person1

    @family_person1.setter
    def family_person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person1", None)
        self.__family_person1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person"):
                opp_val = getattr(old_value, "family_person", None)
                if opp_val == self:
                    setattr(old_value, "family_person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person"):
                opp_val = getattr(value, "family_person", None)
                setattr(value, "family_person", self)

    @property
    def family_person13(self):
        return self.__family_person13

    @family_person13.setter
    def family_person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person13", None)
        self.__family_person13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_studyprogramme12"):
                opp_val = getattr(old_value, "family_studyprogramme12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_studyprogramme12"):
                opp_val = getattr(value, "family_studyprogramme12", None)
                if opp_val is None:
                    setattr(value, "family_studyprogramme12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_person5(self):
        return self.__family_person5

    @family_person5.setter
    def family_person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person5", None)
        self.__family_person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person3"):
                opp_val = getattr(old_value, "family_person3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person3"):
                opp_val = getattr(value, "family_person3", None)
                if opp_val is None:
                    setattr(value, "family_person3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_person8(self):
        return self.__family_person8

    @family_person8.setter
    def family_person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person8", None)
        self.__family_person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person6"):
                opp_val = getattr(old_value, "family_person6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person6"):
                opp_val = getattr(value, "family_person6", None)
                if opp_val is None:
                    setattr(value, "family_person6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_person6(self):
        return self.__family_person6

    @family_person6.setter
    def family_person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person6", None)
        self.__family_person6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_person8"):
                    opp_val = getattr(item, "family_person8", None)
                    
                    if opp_val == self:
                        setattr(item, "family_person8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_person8"):
                    opp_val = getattr(item, "family_person8", None)
                    
                    setattr(item, "family_person8", self)
                    

class family_studyprogramme:

    def __init__(self, name: str, family_studyprogramme12: set["family_person"] = None, family_studyprogramme: "family_university" = None):
        self.name = name
        self.family_studyprogramme12 = family_studyprogramme12 if family_studyprogramme12 is not None else set()
        self.family_studyprogramme = family_studyprogramme
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_studyprogramme(self):
        return self.__family_studyprogramme

    @family_studyprogramme.setter
    def family_studyprogramme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_studyprogramme__family_studyprogramme", None)
        self.__family_studyprogramme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_university"):
                opp_val = getattr(old_value, "family_university", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_university"):
                opp_val = getattr(value, "family_university", None)
                if opp_val is None:
                    setattr(value, "family_university", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_studyprogramme12(self):
        return self.__family_studyprogramme12

    @family_studyprogramme12.setter
    def family_studyprogramme12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_studyprogramme__family_studyprogramme12", None)
        self.__family_studyprogramme12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_person13"):
                    opp_val = getattr(item, "family_person13", None)
                    
                    if opp_val == self:
                        setattr(item, "family_person13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_person13"):
                    opp_val = getattr(item, "family_person13", None)
                    
                    setattr(item, "family_person13", self)
                    

class family_university:

    def __init__(self, name: str, family_university18: "family_Root" = None, family_university: set["family_studyprogramme"] = None):
        self.name = name
        self.family_university18 = family_university18
        self.family_university = family_university if family_university is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_university(self):
        return self.__family_university

    @family_university.setter
    def family_university(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_university__family_university", None)
        self.__family_university = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_studyprogramme"):
                    opp_val = getattr(item, "family_studyprogramme", None)
                    
                    if opp_val == self:
                        setattr(item, "family_studyprogramme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_studyprogramme"):
                    opp_val = getattr(item, "family_studyprogramme", None)
                    
                    setattr(item, "family_studyprogramme", self)
                    

    @property
    def family_university18(self):
        return self.__family_university18

    @family_university18.setter
    def family_university18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_university__family_university18", None)
        self.__family_university18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Root17"):
                opp_val = getattr(old_value, "family_Root17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Root17"):
                opp_val = getattr(value, "family_Root17", None)
                if opp_val is None:
                    setattr(value, "family_Root17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class family_Root:

    pass
class family_family:

    def __init__(self, name: str, family_family: set["family_person"] = None, family_family15: "family_Root" = None):
        self.name = name
        self.family_family = family_family if family_family is not None else set()
        self.family_family15 = family_family15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_family(self):
        return self.__family_family

    @family_family.setter
    def family_family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_family__family_family", None)
        self.__family_family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_person10"):
                    opp_val = getattr(item, "family_person10", None)
                    
                    if opp_val == self:
                        setattr(item, "family_person10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_person10"):
                    opp_val = getattr(item, "family_person10", None)
                    
                    setattr(item, "family_person10", self)
                    

    @property
    def family_family15(self):
        return self.__family_family15

    @family_family15.setter
    def family_family15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_family__family_family15", None)
        self.__family_family15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Root"):
                opp_val = getattr(old_value, "family_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Root"):
                opp_val = getattr(value, "family_Root", None)
                if opp_val is None:
                    setattr(value, "family_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
