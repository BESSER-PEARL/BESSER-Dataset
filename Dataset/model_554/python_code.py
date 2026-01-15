from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_Pet:

    def __init__(self, name: str, family_Pet: "family_Family" = None):
        self.name = name
        self.family_Pet = family_Pet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_Pet(self):
        return self.__family_Pet

    @family_Pet.setter
    def family_Pet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Pet__family_Pet", None)
        self.__family_Pet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family4"):
                opp_val = getattr(old_value, "family_Family4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family4"):
                opp_val = getattr(value, "family_Family4", None)
                if opp_val is None:
                    setattr(value, "family_Family4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class family_Person:

    def __init__(self, name: str, family_Person: "family_Family" = None, Person: "family_Person" = None, parents: set["family_Person"] = None, family_Person9: "family_Person" = None, family_Person7: "family_Person" = None, Person12: "family_Person" = None, children: set["family_Person"] = None):
        self.name = name
        self.family_Person = family_Person
        self.Person = Person
        self.parents = parents if parents is not None else set()
        self.family_Person9 = family_Person9
        self.family_Person7 = family_Person7
        self.Person12 = Person12
        self.children = children if children is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_Person9(self):
        return self.__family_Person9

    @family_Person9.setter
    def family_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person9", None)
        self.__family_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person7"):
                opp_val = getattr(old_value, "family_Person7", None)
                if opp_val == self:
                    setattr(old_value, "family_Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person7"):
                opp_val = getattr(value, "family_Person7", None)
                setattr(value, "family_Person7", self)

    @property
    def family_Person7(self):
        return self.__family_Person7

    @family_Person7.setter
    def family_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person7", None)
        self.__family_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person9"):
                opp_val = getattr(old_value, "family_Person9", None)
                if opp_val == self:
                    setattr(old_value, "family_Person9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person9"):
                opp_val = getattr(value, "family_Person9", None)
                setattr(value, "family_Person9", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                if opp_val is None:
                    setattr(value, "parents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person12(self):
        return self.__Person12

    @Person12.setter
    def Person12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__Person12", None)
        self.__Person12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def family_Person(self):
        return self.__family_Person

    @family_Person.setter
    def family_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person", None)
        self.__family_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family2"):
                opp_val = getattr(old_value, "family_Family2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family2"):
                opp_val = getattr(value, "family_Family2", None)
                if opp_val is None:
                    setattr(value, "family_Family2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person12"):
                    opp_val = getattr(item, "Person12", None)
                    
                    if opp_val == self:
                        setattr(item, "Person12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person12"):
                    opp_val = getattr(item, "Person12", None)
                    
                    setattr(item, "Person12", self)
                    

class family_Family:

    pass
class family_Model:

    pass