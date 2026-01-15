from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class genealogy_Person:

    def __init__(self, name: str, age: int, alive: bool, Person: "genealogy_Person" = None, children: set["genealogy_Person"] = None, Person5: "genealogy_Person" = None, parents: set["genealogy_Person"] = None, genealogy_Person: "genealogy_Genealogy" = None):
        self.name = name
        self.age = age
        self.alive = alive
        self.Person = Person
        self.children = children if children is not None else set()
        self.Person5 = Person5
        self.parents = parents if parents is not None else set()
        self.genealogy_Person = genealogy_Person
        
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
    def alive(self) -> bool:
        return self.__alive

    @alive.setter
    def alive(self, alive: bool):
        self.__alive = alive

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genealogy_Person__children", None)
        self.__children = value if value is not None else set()
        
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
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genealogy_Person__Person", None)
        self.__Person = value
        
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
    def Person5(self):
        return self.__Person5

    @Person5.setter
    def Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genealogy_Person__Person5", None)
        self.__Person5 = value
        
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
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genealogy_Person__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person5"):
                    opp_val = getattr(item, "Person5", None)
                    
                    if opp_val == self:
                        setattr(item, "Person5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person5"):
                    opp_val = getattr(item, "Person5", None)
                    
                    setattr(item, "Person5", self)
                    

    @property
    def genealogy_Person(self):
        return self.__genealogy_Person

    @genealogy_Person.setter
    def genealogy_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genealogy_Person__genealogy_Person", None)
        self.__genealogy_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genealogy_Genealogy"):
                opp_val = getattr(old_value, "genealogy_Genealogy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genealogy_Genealogy"):
                opp_val = getattr(value, "genealogy_Genealogy", None)
                if opp_val is None:
                    setattr(value, "genealogy_Genealogy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class genealogy_Genealogy:

    pass