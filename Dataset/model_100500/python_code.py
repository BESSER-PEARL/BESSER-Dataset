from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryOperator:

    pass
class newP_OrOperator(BinaryOperator):

    pass
class newP_AndOperartor(BinaryOperator):

    pass
class UnaryOperator:

    pass
class newP_BinaryOperator(UnaryOperator):

    pass
class newP_NotOperator(UnaryOperator):

    pass
class SimpleDependency:

    pass
class newP_ICost(SimpleDependency):

    pass
class newP_Refines(SimpleDependency):

    pass
class newP_CValue(SimpleDependency):

    pass
class newP_Person:

    def __init__(self, firstName: str, lastName: str, newP_Person13: set["newP_Category"] = None, newP_Person16: set["newP_Requirement"] = None, newP_Person: "newP_Specification" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.newP_Person13 = newP_Person13 if newP_Person13 is not None else set()
        self.newP_Person16 = newP_Person16 if newP_Person16 is not None else set()
        self.newP_Person = newP_Person
        
        pass
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def newP_Person16(self):
        return self.__newP_Person16

    @newP_Person16.setter
    def newP_Person16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Person__newP_Person16", None)
        self.__newP_Person16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Requirement17"):
                    opp_val = getattr(item, "newP_Requirement17", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Requirement17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Requirement17"):
                    opp_val = getattr(item, "newP_Requirement17", None)
                    
                    setattr(item, "newP_Requirement17", self)
                    

    @property
    def newP_Person13(self):
        return self.__newP_Person13

    @newP_Person13.setter
    def newP_Person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Person__newP_Person13", None)
        self.__newP_Person13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Category14"):
                    opp_val = getattr(item, "newP_Category14", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Category14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Category14"):
                    opp_val = getattr(item, "newP_Category14", None)
                    
                    setattr(item, "newP_Category14", self)
                    

    @property
    def newP_Person(self):
        return self.__newP_Person

    @newP_Person.setter
    def newP_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Person__newP_Person", None)
        self.__newP_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Specification11"):
                opp_val = getattr(old_value, "newP_Specification11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Specification11"):
                opp_val = getattr(value, "newP_Specification11", None)
                if opp_val is None:
                    setattr(value, "newP_Specification11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class newP_Specification:

    def __init__(self, name: str, newP_Specification: set["newP_Category"] = None, newP_Specification11: set["newP_Person"] = None):
        self.name = name
        self.newP_Specification = newP_Specification if newP_Specification is not None else set()
        self.newP_Specification11 = newP_Specification11 if newP_Specification11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def newP_Specification11(self):
        return self.__newP_Specification11

    @newP_Specification11.setter
    def newP_Specification11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Specification__newP_Specification11", None)
        self.__newP_Specification11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Person"):
                    opp_val = getattr(item, "newP_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Person"):
                    opp_val = getattr(item, "newP_Person", None)
                    
                    setattr(item, "newP_Person", self)
                    

    @property
    def newP_Specification(self):
        return self.__newP_Specification

    @newP_Specification.setter
    def newP_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Specification__newP_Specification", None)
        self.__newP_Specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Category9"):
                    opp_val = getattr(item, "newP_Category9", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Category9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Category9"):
                    opp_val = getattr(item, "newP_Category9", None)
                    
                    setattr(item, "newP_Category9", self)
                    

class newP_Category:

    def __init__(self, name: str, newP_Category14: "newP_Person" = None, newP_Category: set["newP_Requirement"] = None, newP_Category7: "newP_Category" = None, newP_Category5: set["newP_Category"] = None, newP_Category9: "newP_Specification" = None):
        self.name = name
        self.newP_Category14 = newP_Category14
        self.newP_Category = newP_Category if newP_Category is not None else set()
        self.newP_Category7 = newP_Category7
        self.newP_Category5 = newP_Category5 if newP_Category5 is not None else set()
        self.newP_Category9 = newP_Category9
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def newP_Category9(self):
        return self.__newP_Category9

    @newP_Category9.setter
    def newP_Category9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Category__newP_Category9", None)
        self.__newP_Category9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Specification"):
                opp_val = getattr(old_value, "newP_Specification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Specification"):
                opp_val = getattr(value, "newP_Specification", None)
                if opp_val is None:
                    setattr(value, "newP_Specification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def newP_Category7(self):
        return self.__newP_Category7

    @newP_Category7.setter
    def newP_Category7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Category__newP_Category7", None)
        self.__newP_Category7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Category5"):
                opp_val = getattr(old_value, "newP_Category5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Category5"):
                opp_val = getattr(value, "newP_Category5", None)
                if opp_val is None:
                    setattr(value, "newP_Category5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def newP_Category(self):
        return self.__newP_Category

    @newP_Category.setter
    def newP_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Category__newP_Category", None)
        self.__newP_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Requirement4"):
                    opp_val = getattr(item, "newP_Requirement4", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Requirement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Requirement4"):
                    opp_val = getattr(item, "newP_Requirement4", None)
                    
                    setattr(item, "newP_Requirement4", self)
                    

    @property
    def newP_Category5(self):
        return self.__newP_Category5

    @newP_Category5.setter
    def newP_Category5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Category__newP_Category5", None)
        self.__newP_Category5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Category7"):
                    opp_val = getattr(item, "newP_Category7", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Category7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Category7"):
                    opp_val = getattr(item, "newP_Category7", None)
                    
                    setattr(item, "newP_Category7", self)
                    

    @property
    def newP_Category14(self):
        return self.__newP_Category14

    @newP_Category14.setter
    def newP_Category14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Category__newP_Category14", None)
        self.__newP_Category14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Person13"):
                opp_val = getattr(old_value, "newP_Person13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Person13"):
                opp_val = getattr(value, "newP_Person13", None)
                if opp_val is None:
                    setattr(value, "newP_Person13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Description:

    pass
class newP_TextDescription(Description):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class Requirement:

    pass
class newP_QualityRequirement(Requirement):

    pass
class newP_FunctionalRequirement(Requirement):

    pass
class Dependency:

    pass
class newP_SimpleDependency(Dependency):

    def __init__(self, name: str, newP_SimpleDependency: "newP_RequirementTerm" = None):
        self.name = name
        self.newP_SimpleDependency = newP_SimpleDependency
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def newP_SimpleDependency(self):
        return self.__newP_SimpleDependency

    @newP_SimpleDependency.setter
    def newP_SimpleDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_SimpleDependency__newP_SimpleDependency", None)
        self.__newP_SimpleDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_RequirementTerm"):
                opp_val = getattr(old_value, "newP_RequirementTerm", None)
                if opp_val == self:
                    setattr(old_value, "newP_RequirementTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_RequirementTerm"):
                opp_val = getattr(value, "newP_RequirementTerm", None)
                setattr(value, "newP_RequirementTerm", self)

class newP_Requires(Dependency):

    def __init__(self, name: str, newP_Requires: "newP_Term" = None):
        self.name = name
        self.newP_Requires = newP_Requires
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def newP_Requires(self):
        return self.__newP_Requires

    @newP_Requires.setter
    def newP_Requires(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Requires__newP_Requires", None)
        self.__newP_Requires = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Term20"):
                opp_val = getattr(old_value, "newP_Term20", None)
                if opp_val == self:
                    setattr(old_value, "newP_Term20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Term20"):
                opp_val = getattr(value, "newP_Term20", None)
                setattr(value, "newP_Term20", self)

class Term:

    pass
class newP_RequirementTerm(Term):

    pass
class newP_UnaryOperator(Term):

    def __init__(self, name: str, newP_UnaryOperator: "newP_Term" = None):
        self.name = name
        self.newP_UnaryOperator = newP_UnaryOperator
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def newP_UnaryOperator(self):
        return self.__newP_UnaryOperator

    @newP_UnaryOperator.setter
    def newP_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_UnaryOperator__newP_UnaryOperator", None)
        self.__newP_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Term"):
                opp_val = getattr(old_value, "newP_Term", None)
                if opp_val == self:
                    setattr(old_value, "newP_Term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Term"):
                opp_val = getattr(value, "newP_Term", None)
                setattr(value, "newP_Term", self)

class newP_Term(ABC):

    pass
class newP_Dependency(ABC):

    pass
class newP_Description(ABC):

    pass
class newP_Requirement(ABC):

    def __init__(self, name: str, identifier: str, priority: int, mandatory: bool, newP_Requirement: set["newP_Description"] = None, newP_Requirement17: "newP_Person" = None, newP_Requirement2: set["newP_Dependency"] = None, newP_Requirement4: "newP_Category" = None, newP_Requirement26: "newP_RequirementTerm" = None):
        self.name = name
        self.identifier = identifier
        self.priority = priority
        self.mandatory = mandatory
        self.newP_Requirement = newP_Requirement if newP_Requirement is not None else set()
        self.newP_Requirement17 = newP_Requirement17
        self.newP_Requirement2 = newP_Requirement2 if newP_Requirement2 is not None else set()
        self.newP_Requirement4 = newP_Requirement4
        self.newP_Requirement26 = newP_Requirement26
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mandatory(self):
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def newP_Requirement17(self):
        return self.__newP_Requirement17

    @newP_Requirement17.setter
    def newP_Requirement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Requirement__newP_Requirement17", None)
        self.__newP_Requirement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Person16"):
                opp_val = getattr(old_value, "newP_Person16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Person16"):
                opp_val = getattr(value, "newP_Person16", None)
                if opp_val is None:
                    setattr(value, "newP_Person16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def newP_Requirement(self):
        return self.__newP_Requirement

    @newP_Requirement.setter
    def newP_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Requirement__newP_Requirement", None)
        self.__newP_Requirement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Description"):
                    opp_val = getattr(item, "newP_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Description"):
                    opp_val = getattr(item, "newP_Description", None)
                    
                    setattr(item, "newP_Description", self)
                    

    @property
    def newP_Requirement4(self):
        return self.__newP_Requirement4

    @newP_Requirement4.setter
    def newP_Requirement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Requirement__newP_Requirement4", None)
        self.__newP_Requirement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_Category"):
                opp_val = getattr(old_value, "newP_Category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_Category"):
                opp_val = getattr(value, "newP_Category", None)
                if opp_val is None:
                    setattr(value, "newP_Category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def newP_Requirement26(self):
        return self.__newP_Requirement26

    @newP_Requirement26.setter
    def newP_Requirement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Requirement__newP_Requirement26", None)
        self.__newP_Requirement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newP_RequirementTerm25"):
                opp_val = getattr(old_value, "newP_RequirementTerm25", None)
                if opp_val == self:
                    setattr(old_value, "newP_RequirementTerm25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newP_RequirementTerm25"):
                opp_val = getattr(value, "newP_RequirementTerm25", None)
                setattr(value, "newP_RequirementTerm25", self)

    @property
    def newP_Requirement2(self):
        return self.__newP_Requirement2

    @newP_Requirement2.setter
    def newP_Requirement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newP_Requirement__newP_Requirement2", None)
        self.__newP_Requirement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "newP_Dependency"):
                    opp_val = getattr(item, "newP_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "newP_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "newP_Dependency"):
                    opp_val = getattr(item, "newP_Dependency", None)
                    
                    setattr(item, "newP_Dependency", self)
                    
