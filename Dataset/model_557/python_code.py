from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_Family:

    pass
class family_person:

    def __init__(self, name: str, age: int, CPR: str, family_person7: "family_person" = None, family_person5: set["family_person"] = None, family_person9: set["family_university"] = None, family_person14: "family_course" = None, family_person: "family_person" = None, family_person0: "family_person" = None, family_person4: "family_person" = None, family_person2: "family_person" = None, family_person19: "family_Family" = None):
        self.name = name
        self.age = age
        self.CPR = CPR
        self.family_person7 = family_person7
        self.family_person5 = family_person5 if family_person5 is not None else set()
        self.family_person9 = family_person9 if family_person9 is not None else set()
        self.family_person14 = family_person14
        self.family_person = family_person
        self.family_person0 = family_person0
        self.family_person4 = family_person4
        self.family_person2 = family_person2
        self.family_person19 = family_person19
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def CPR(self) -> str:
        return self.__CPR

    @CPR.setter
    def CPR(self, CPR: str):
        self.__CPR = CPR

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_person14(self):
        return self.__family_person14

    @family_person14.setter
    def family_person14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person14", None)
        self.__family_person14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_course13"):
                opp_val = getattr(old_value, "family_course13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_course13"):
                opp_val = getattr(value, "family_course13", None)
                if opp_val is None:
                    setattr(value, "family_course13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_person7(self):
        return self.__family_person7

    @family_person7.setter
    def family_person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person7", None)
        self.__family_person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person5"):
                opp_val = getattr(old_value, "family_person5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person5"):
                opp_val = getattr(value, "family_person5", None)
                if opp_val is None:
                    setattr(value, "family_person5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_person5(self):
        return self.__family_person5

    @family_person5.setter
    def family_person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person5", None)
        self.__family_person5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_person7"):
                    opp_val = getattr(item, "family_person7", None)
                    
                    if opp_val == self:
                        setattr(item, "family_person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_person7"):
                    opp_val = getattr(item, "family_person7", None)
                    
                    setattr(item, "family_person7", self)
                    

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
            if hasattr(old_value, "family_person0"):
                opp_val = getattr(old_value, "family_person0", None)
                if opp_val == self:
                    setattr(old_value, "family_person0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person0"):
                opp_val = getattr(value, "family_person0", None)
                setattr(value, "family_person0", self)

    @property
    def family_person2(self):
        return self.__family_person2

    @family_person2.setter
    def family_person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person2", None)
        self.__family_person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person4"):
                opp_val = getattr(old_value, "family_person4", None)
                if opp_val == self:
                    setattr(old_value, "family_person4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person4"):
                opp_val = getattr(value, "family_person4", None)
                setattr(value, "family_person4", self)

    @property
    def family_person4(self):
        return self.__family_person4

    @family_person4.setter
    def family_person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person4", None)
        self.__family_person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person2"):
                opp_val = getattr(old_value, "family_person2", None)
                if opp_val == self:
                    setattr(old_value, "family_person2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person2"):
                opp_val = getattr(value, "family_person2", None)
                setattr(value, "family_person2", self)

    @property
    def family_person19(self):
        return self.__family_person19

    @family_person19.setter
    def family_person19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person19", None)
        self.__family_person19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family18"):
                opp_val = getattr(old_value, "family_Family18", None)
                if opp_val == self:
                    setattr(old_value, "family_Family18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family18"):
                opp_val = getattr(value, "family_Family18", None)
                setattr(value, "family_Family18", self)

    @property
    def family_person0(self):
        return self.__family_person0

    @family_person0.setter
    def family_person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person0", None)
        self.__family_person0 = value
        
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
    def family_person9(self):
        return self.__family_person9

    @family_person9.setter
    def family_person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_person__family_person9", None)
        self.__family_person9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_university"):
                    opp_val = getattr(item, "family_university", None)
                    
                    if opp_val == self:
                        setattr(item, "family_university", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_university"):
                    opp_val = getattr(item, "family_university", None)
                    
                    setattr(item, "family_university", self)
                    

class family_course:

    def __init__(self, name: str, family_course: "family_university" = None, family_course13: set["family_person"] = None):
        self.name = name
        self.family_course = family_course
        self.family_course13 = family_course13 if family_course13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_course13(self):
        return self.__family_course13

    @family_course13.setter
    def family_course13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_course__family_course13", None)
        self.__family_course13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_person14"):
                    opp_val = getattr(item, "family_person14", None)
                    
                    if opp_val == self:
                        setattr(item, "family_person14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_person14"):
                    opp_val = getattr(item, "family_person14", None)
                    
                    setattr(item, "family_person14", self)
                    

    @property
    def family_course(self):
        return self.__family_course

    @family_course.setter
    def family_course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_course__family_course", None)
        self.__family_course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_university11"):
                opp_val = getattr(old_value, "family_university11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_university11"):
                opp_val = getattr(value, "family_university11", None)
                if opp_val is None:
                    setattr(value, "family_university11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class family_university:

    def __init__(self, name: str, family_university: "family_person" = None, family_university11: set["family_course"] = None):
        self.name = name
        self.family_university = family_university
        self.family_university11 = family_university11 if family_university11 is not None else set()
        
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
        self.__family_university = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_person9"):
                opp_val = getattr(old_value, "family_person9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_person9"):
                opp_val = getattr(value, "family_person9", None)
                if opp_val is None:
                    setattr(value, "family_person9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_university11(self):
        return self.__family_university11

    @family_university11.setter
    def family_university11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_university__family_university11", None)
        self.__family_university11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_course"):
                    opp_val = getattr(item, "family_course", None)
                    
                    if opp_val == self:
                        setattr(item, "family_course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_course"):
                    opp_val = getattr(item, "family_course", None)
                    
                    setattr(item, "family_course", self)
                    
