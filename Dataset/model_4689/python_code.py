from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person:

    pass
class basicfamily_Man(Person):

    pass
class basicfamily_Woman(Person):

    pass
class basicfamily_Relation:

    def __init__(self, description: str, basicfamily_Relation: "basicfamily_Family" = None, basicfamily_Relation14: "basicfamily_Person" = None, basicfamily_Relation16: "basicfamily_Person" = None, basicfamily_Relation19: "basicfamily_Person" = None):
        self.description = description
        self.basicfamily_Relation = basicfamily_Relation
        self.basicfamily_Relation14 = basicfamily_Relation14
        self.basicfamily_Relation16 = basicfamily_Relation16
        self.basicfamily_Relation19 = basicfamily_Relation19
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def basicfamily_Relation19(self):
        return self.__basicfamily_Relation19

    @basicfamily_Relation19.setter
    def basicfamily_Relation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Relation__basicfamily_Relation19", None)
        self.__basicfamily_Relation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Person20"):
                opp_val = getattr(old_value, "basicfamily_Person20", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Person20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Person20"):
                opp_val = getattr(value, "basicfamily_Person20", None)
                setattr(value, "basicfamily_Person20", self)

    @property
    def basicfamily_Relation14(self):
        return self.__basicfamily_Relation14

    @basicfamily_Relation14.setter
    def basicfamily_Relation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Relation__basicfamily_Relation14", None)
        self.__basicfamily_Relation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Person13"):
                opp_val = getattr(old_value, "basicfamily_Person13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Person13"):
                opp_val = getattr(value, "basicfamily_Person13", None)
                if opp_val is None:
                    setattr(value, "basicfamily_Person13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basicfamily_Relation(self):
        return self.__basicfamily_Relation

    @basicfamily_Relation.setter
    def basicfamily_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Relation__basicfamily_Relation", None)
        self.__basicfamily_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Family2"):
                opp_val = getattr(old_value, "basicfamily_Family2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Family2"):
                opp_val = getattr(value, "basicfamily_Family2", None)
                if opp_val is None:
                    setattr(value, "basicfamily_Family2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basicfamily_Relation16(self):
        return self.__basicfamily_Relation16

    @basicfamily_Relation16.setter
    def basicfamily_Relation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Relation__basicfamily_Relation16", None)
        self.__basicfamily_Relation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Person17"):
                opp_val = getattr(old_value, "basicfamily_Person17", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Person17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Person17"):
                opp_val = getattr(value, "basicfamily_Person17", None)
                setattr(value, "basicfamily_Person17", self)

class basicfamily_Person:

    def __init__(self, name: str, birthDate: date, basicfamily_Person: "basicfamily_Family" = None, Person: "basicfamily_Person" = None, children: set["basicfamily_Person"] = None, Person7: "basicfamily_Person" = None, parents: set["basicfamily_Person"] = None, basicfamily_Person9: "basicfamily_Woman" = None, basicfamily_Person11: "basicfamily_Man" = None, basicfamily_Person13: set["basicfamily_Relation"] = None, basicfamily_Person17: "basicfamily_Relation" = None, basicfamily_Person20: "basicfamily_Relation" = None):
        self.name = name
        self.birthDate = birthDate
        self.basicfamily_Person = basicfamily_Person
        self.Person = Person
        self.children = children if children is not None else set()
        self.Person7 = Person7
        self.parents = parents if parents is not None else set()
        self.basicfamily_Person9 = basicfamily_Person9
        self.basicfamily_Person11 = basicfamily_Person11
        self.basicfamily_Person13 = basicfamily_Person13 if basicfamily_Person13 is not None else set()
        self.basicfamily_Person17 = basicfamily_Person17
        self.basicfamily_Person20 = basicfamily_Person20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def birthDate(self) -> date:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: date):
        self.__birthDate = birthDate

    @property
    def basicfamily_Person17(self):
        return self.__basicfamily_Person17

    @basicfamily_Person17.setter
    def basicfamily_Person17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person17", None)
        self.__basicfamily_Person17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Relation16"):
                opp_val = getattr(old_value, "basicfamily_Relation16", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Relation16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Relation16"):
                opp_val = getattr(value, "basicfamily_Relation16", None)
                setattr(value, "basicfamily_Relation16", self)

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person7"):
                    opp_val = getattr(item, "Person7", None)
                    
                    if opp_val == self:
                        setattr(item, "Person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person7"):
                    opp_val = getattr(item, "Person7", None)
                    
                    setattr(item, "Person7", self)
                    

    @property
    def basicfamily_Person9(self):
        return self.__basicfamily_Person9

    @basicfamily_Person9.setter
    def basicfamily_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person9", None)
        self.__basicfamily_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Woman"):
                opp_val = getattr(old_value, "basicfamily_Woman", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Woman", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Woman"):
                opp_val = getattr(value, "basicfamily_Woman", None)
                setattr(value, "basicfamily_Woman", self)

    @property
    def Person7(self):
        return self.__Person7

    @Person7.setter
    def Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__Person7", None)
        self.__Person7 = value
        
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
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__Person", None)
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
    def basicfamily_Person11(self):
        return self.__basicfamily_Person11

    @basicfamily_Person11.setter
    def basicfamily_Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person11", None)
        self.__basicfamily_Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Man"):
                opp_val = getattr(old_value, "basicfamily_Man", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Man", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Man"):
                opp_val = getattr(value, "basicfamily_Man", None)
                setattr(value, "basicfamily_Man", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__children", None)
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
    def basicfamily_Person(self):
        return self.__basicfamily_Person

    @basicfamily_Person.setter
    def basicfamily_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person", None)
        self.__basicfamily_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Family"):
                opp_val = getattr(old_value, "basicfamily_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Family"):
                opp_val = getattr(value, "basicfamily_Family", None)
                if opp_val is None:
                    setattr(value, "basicfamily_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basicfamily_Person20(self):
        return self.__basicfamily_Person20

    @basicfamily_Person20.setter
    def basicfamily_Person20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person20", None)
        self.__basicfamily_Person20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Relation19"):
                opp_val = getattr(old_value, "basicfamily_Relation19", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Relation19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Relation19"):
                opp_val = getattr(value, "basicfamily_Relation19", None)
                setattr(value, "basicfamily_Relation19", self)

    @property
    def basicfamily_Person13(self):
        return self.__basicfamily_Person13

    @basicfamily_Person13.setter
    def basicfamily_Person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person13", None)
        self.__basicfamily_Person13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicfamily_Relation14"):
                    opp_val = getattr(item, "basicfamily_Relation14", None)
                    
                    if opp_val == self:
                        setattr(item, "basicfamily_Relation14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicfamily_Relation14"):
                    opp_val = getattr(item, "basicfamily_Relation14", None)
                    
                    setattr(item, "basicfamily_Relation14", self)
                    

class basicfamily_Family:

    def __init__(self, name: str, basicfamily_Family: set["basicfamily_Person"] = None, basicfamily_Family2: set["basicfamily_Relation"] = None):
        self.name = name
        self.basicfamily_Family = basicfamily_Family if basicfamily_Family is not None else set()
        self.basicfamily_Family2 = basicfamily_Family2 if basicfamily_Family2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basicfamily_Family(self):
        return self.__basicfamily_Family

    @basicfamily_Family.setter
    def basicfamily_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Family__basicfamily_Family", None)
        self.__basicfamily_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicfamily_Person"):
                    opp_val = getattr(item, "basicfamily_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "basicfamily_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicfamily_Person"):
                    opp_val = getattr(item, "basicfamily_Person", None)
                    
                    setattr(item, "basicfamily_Person", self)
                    

    @property
    def basicfamily_Family2(self):
        return self.__basicfamily_Family2

    @basicfamily_Family2.setter
    def basicfamily_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Family__basicfamily_Family2", None)
        self.__basicfamily_Family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicfamily_Relation"):
                    opp_val = getattr(item, "basicfamily_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "basicfamily_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicfamily_Relation"):
                    opp_val = getattr(item, "basicfamily_Relation", None)
                    
                    setattr(item, "basicfamily_Relation", self)
                    
