from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOperator(Enum):
    OR = "OR"
    AND = "AND"


############################################
# Definition of Classes
############################################

class requirements_editor_DocumentRoot:

    def __init__(self, name: str, requirements_editor_DocumentRoot: set["requirements_editor_Category"] = None, requirements_editor_DocumentRoot26: set["requirements_editor_Person"] = None):
        self.name = name
        self.requirements_editor_DocumentRoot = requirements_editor_DocumentRoot if requirements_editor_DocumentRoot is not None else set()
        self.requirements_editor_DocumentRoot26 = requirements_editor_DocumentRoot26 if requirements_editor_DocumentRoot26 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def requirements_editor_DocumentRoot26(self):
        return self.__requirements_editor_DocumentRoot26

    @requirements_editor_DocumentRoot26.setter
    def requirements_editor_DocumentRoot26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_DocumentRoot__requirements_editor_DocumentRoot26", None)
        self.__requirements_editor_DocumentRoot26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_editor_Person"):
                    opp_val = getattr(item, "requirements_editor_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_editor_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_editor_Person"):
                    opp_val = getattr(item, "requirements_editor_Person", None)
                    
                    setattr(item, "requirements_editor_Person", self)
                    

    @property
    def requirements_editor_DocumentRoot(self):
        return self.__requirements_editor_DocumentRoot

    @requirements_editor_DocumentRoot.setter
    def requirements_editor_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_DocumentRoot__requirements_editor_DocumentRoot", None)
        self.__requirements_editor_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_editor_Category24"):
                    opp_val = getattr(item, "requirements_editor_Category24", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_editor_Category24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_editor_Category24"):
                    opp_val = getattr(item, "requirements_editor_Category24", None)
                    
                    setattr(item, "requirements_editor_Category24", self)
                    

class Argument:

    pass
class requirements_editor_NOTOperator(Argument):

    pass
class requirements_editor_RequirementArgument(Argument):

    pass
class requirements_editor_BinaryOperatorArgument(Argument):

    def __init__(self, operator: str, requirements_editor_BinaryOperatorArgument: "requirements_editor_Argument" = None, requirements_editor_BinaryOperatorArgument19: "requirements_editor_Argument" = None):
        self.operator = operator
        self.requirements_editor_BinaryOperatorArgument = requirements_editor_BinaryOperatorArgument
        self.requirements_editor_BinaryOperatorArgument19 = requirements_editor_BinaryOperatorArgument19
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def requirements_editor_BinaryOperatorArgument19(self):
        return self.__requirements_editor_BinaryOperatorArgument19

    @requirements_editor_BinaryOperatorArgument19.setter
    def requirements_editor_BinaryOperatorArgument19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_BinaryOperatorArgument__requirements_editor_BinaryOperatorArgument19", None)
        self.__requirements_editor_BinaryOperatorArgument19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_Argument20"):
                opp_val = getattr(old_value, "requirements_editor_Argument20", None)
                if opp_val == self:
                    setattr(old_value, "requirements_editor_Argument20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_Argument20"):
                opp_val = getattr(value, "requirements_editor_Argument20", None)
                setattr(value, "requirements_editor_Argument20", self)

    @property
    def requirements_editor_BinaryOperatorArgument(self):
        return self.__requirements_editor_BinaryOperatorArgument

    @requirements_editor_BinaryOperatorArgument.setter
    def requirements_editor_BinaryOperatorArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_BinaryOperatorArgument__requirements_editor_BinaryOperatorArgument", None)
        self.__requirements_editor_BinaryOperatorArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_Argument17"):
                opp_val = getattr(old_value, "requirements_editor_Argument17", None)
                if opp_val == self:
                    setattr(old_value, "requirements_editor_Argument17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_Argument17"):
                opp_val = getattr(value, "requirements_editor_Argument17", None)
                setattr(value, "requirements_editor_Argument17", self)

class requirements_editor_Argument(ABC):

    pass
class SimpleDependency:

    pass
class requirements_editor_CValue(SimpleDependency):

    pass
class requirements_editor_ICost(SimpleDependency):

    pass
class requirements_editor_Refines(SimpleDependency):

    pass
class Dependency:

    pass
class requirements_editor_Requires(Dependency):

    pass
class requirements_editor_SimpleDependency(Dependency):

    def __init__(self, comment: str, requirements_editor_SimpleDependency: "requirements_editor_Requirement" = None):
        self.comment = comment
        self.requirements_editor_SimpleDependency = requirements_editor_SimpleDependency
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def requirements_editor_SimpleDependency(self):
        return self.__requirements_editor_SimpleDependency

    @requirements_editor_SimpleDependency.setter
    def requirements_editor_SimpleDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_SimpleDependency__requirements_editor_SimpleDependency", None)
        self.__requirements_editor_SimpleDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_Requirement14"):
                opp_val = getattr(old_value, "requirements_editor_Requirement14", None)
                if opp_val == self:
                    setattr(old_value, "requirements_editor_Requirement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_Requirement14"):
                opp_val = getattr(value, "requirements_editor_Requirement14", None)
                setattr(value, "requirements_editor_Requirement14", self)

class Requirement:

    pass
class requirements_editor_FunctionalRequirement(Requirement):

    pass
class requirements_editor_QualityRequirement(Requirement):

    pass
class Description:

    pass
class requirements_editor_TextualDescription(Description):

    def __init__(self, description: str):
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class requirements_editor_Category:

    def __init__(self, name: str, requirements_editor_Category: "requirements_editor_Category" = None, requirements_editor_Category4: set["requirements_editor_Category"] = None, personOwnsCategory: "requirements_editor_Person" = None, requirements_editor_Category9: set["requirements_editor_Requirement"] = None, Category: "requirements_editor_Person" = None, requirements_editor_Category24: "requirements_editor_DocumentRoot" = None):
        self.name = name
        self.requirements_editor_Category = requirements_editor_Category
        self.requirements_editor_Category4 = requirements_editor_Category4 if requirements_editor_Category4 is not None else set()
        self.personOwnsCategory = personOwnsCategory
        self.requirements_editor_Category9 = requirements_editor_Category9 if requirements_editor_Category9 is not None else set()
        self.Category = Category
        self.requirements_editor_Category24 = requirements_editor_Category24
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def requirements_editor_Category(self):
        return self.__requirements_editor_Category

    @requirements_editor_Category.setter
    def requirements_editor_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Category__requirements_editor_Category", None)
        self.__requirements_editor_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_Category4"):
                opp_val = getattr(old_value, "requirements_editor_Category4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_Category4"):
                opp_val = getattr(value, "requirements_editor_Category4", None)
                if opp_val is None:
                    setattr(value, "requirements_editor_Category4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_editor_Category4(self):
        return self.__requirements_editor_Category4

    @requirements_editor_Category4.setter
    def requirements_editor_Category4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Category__requirements_editor_Category4", None)
        self.__requirements_editor_Category4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_editor_Category"):
                    opp_val = getattr(item, "requirements_editor_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_editor_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_editor_Category"):
                    opp_val = getattr(item, "requirements_editor_Category", None)
                    
                    setattr(item, "requirements_editor_Category", self)
                    

    @property
    def personOwnsCategory(self):
        return self.__personOwnsCategory

    @personOwnsCategory.setter
    def personOwnsCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Category__personOwnsCategory", None)
        self.__personOwnsCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person7"):
                opp_val = getattr(old_value, "Person7", None)
                if opp_val == self:
                    setattr(old_value, "Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person7"):
                opp_val = getattr(value, "Person7", None)
                setattr(value, "Person7", self)

    @property
    def requirements_editor_Category24(self):
        return self.__requirements_editor_Category24

    @requirements_editor_Category24.setter
    def requirements_editor_Category24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Category__requirements_editor_Category24", None)
        self.__requirements_editor_Category24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_DocumentRoot"):
                opp_val = getattr(old_value, "requirements_editor_DocumentRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_DocumentRoot"):
                opp_val = getattr(value, "requirements_editor_DocumentRoot", None)
                if opp_val is None:
                    setattr(value, "requirements_editor_DocumentRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_editor_Category9(self):
        return self.__requirements_editor_Category9

    @requirements_editor_Category9.setter
    def requirements_editor_Category9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Category__requirements_editor_Category9", None)
        self.__requirements_editor_Category9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_editor_Requirement10"):
                    opp_val = getattr(item, "requirements_editor_Requirement10", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_editor_Requirement10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_editor_Requirement10"):
                    opp_val = getattr(item, "requirements_editor_Requirement10", None)
                    
                    setattr(item, "requirements_editor_Requirement10", self)
                    

    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Category__Category", None)
        self.__Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categoryOwnedBy"):
                opp_val = getattr(old_value, "categoryOwnedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categoryOwnedBy"):
                opp_val = getattr(value, "categoryOwnedBy", None)
                if opp_val is None:
                    setattr(value, "categoryOwnedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class requirements_editor_Dependency(ABC):

    pass
class requirements_editor_Person:

    def __init__(self, name: str, Person: "requirements_editor_Requirement" = None, Person7: "requirements_editor_Category" = None, requirementOwnedBy: set["requirements_editor_Requirement"] = None, categoryOwnedBy: set["requirements_editor_Category"] = None, requirements_editor_Person: "requirements_editor_DocumentRoot" = None):
        self.name = name
        self.Person = Person
        self.Person7 = Person7
        self.requirementOwnedBy = requirementOwnedBy if requirementOwnedBy is not None else set()
        self.categoryOwnedBy = categoryOwnedBy if categoryOwnedBy is not None else set()
        self.requirements_editor_Person = requirements_editor_Person
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personOwnsRequirement"):
                opp_val = getattr(old_value, "personOwnsRequirement", None)
                if opp_val == self:
                    setattr(old_value, "personOwnsRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personOwnsRequirement"):
                opp_val = getattr(value, "personOwnsRequirement", None)
                setattr(value, "personOwnsRequirement", self)

    @property
    def requirements_editor_Person(self):
        return self.__requirements_editor_Person

    @requirements_editor_Person.setter
    def requirements_editor_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Person__requirements_editor_Person", None)
        self.__requirements_editor_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_DocumentRoot26"):
                opp_val = getattr(old_value, "requirements_editor_DocumentRoot26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_DocumentRoot26"):
                opp_val = getattr(value, "requirements_editor_DocumentRoot26", None)
                if opp_val is None:
                    setattr(value, "requirements_editor_DocumentRoot26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def categoryOwnedBy(self):
        return self.__categoryOwnedBy

    @categoryOwnedBy.setter
    def categoryOwnedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Person__categoryOwnedBy", None)
        self.__categoryOwnedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    if opp_val == self:
                        setattr(item, "Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    setattr(item, "Category", self)
                    

    @property
    def Person7(self):
        return self.__Person7

    @Person7.setter
    def Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Person__Person7", None)
        self.__Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personOwnsCategory"):
                opp_val = getattr(old_value, "personOwnsCategory", None)
                if opp_val == self:
                    setattr(old_value, "personOwnsCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personOwnsCategory"):
                opp_val = getattr(value, "personOwnsCategory", None)
                setattr(value, "personOwnsCategory", self)

    @property
    def requirementOwnedBy(self):
        return self.__requirementOwnedBy

    @requirementOwnedBy.setter
    def requirementOwnedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Person__requirementOwnedBy", None)
        self.__requirementOwnedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    setattr(item, "Requirement", self)
                    

class requirements_editor_Description(ABC):

    pass
class requirements_editor_Requirement(ABC):

    def __init__(self, identifier: str, name: str, priority: int, isMandatory: bool, requirements_editor_Requirement: "requirements_editor_Description" = None, personOwnsRequirement: "requirements_editor_Person" = None, requirements_editor_Requirement3: set["requirements_editor_Dependency"] = None, requirements_editor_Requirement10: "requirements_editor_Category" = None, Requirement: "requirements_editor_Person" = None, requirements_editor_Requirement14: "requirements_editor_SimpleDependency" = None, requirements_editor_Requirement22: "requirements_editor_RequirementArgument" = None):
        self.identifier = identifier
        self.name = name
        self.priority = priority
        self.isMandatory = isMandatory
        self.requirements_editor_Requirement = requirements_editor_Requirement
        self.personOwnsRequirement = personOwnsRequirement
        self.requirements_editor_Requirement3 = requirements_editor_Requirement3 if requirements_editor_Requirement3 is not None else set()
        self.requirements_editor_Requirement10 = requirements_editor_Requirement10
        self.Requirement = Requirement
        self.requirements_editor_Requirement14 = requirements_editor_Requirement14
        self.requirements_editor_Requirement22 = requirements_editor_Requirement22
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def isMandatory(self):
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory


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
    def requirements_editor_Requirement22(self):
        return self.__requirements_editor_Requirement22

    @requirements_editor_Requirement22.setter
    def requirements_editor_Requirement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__requirements_editor_Requirement22", None)
        self.__requirements_editor_Requirement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_RequirementArgument"):
                opp_val = getattr(old_value, "requirements_editor_RequirementArgument", None)
                if opp_val == self:
                    setattr(old_value, "requirements_editor_RequirementArgument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_RequirementArgument"):
                opp_val = getattr(value, "requirements_editor_RequirementArgument", None)
                setattr(value, "requirements_editor_RequirementArgument", self)

    @property
    def requirements_editor_Requirement(self):
        return self.__requirements_editor_Requirement

    @requirements_editor_Requirement.setter
    def requirements_editor_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__requirements_editor_Requirement", None)
        self.__requirements_editor_Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_Description"):
                opp_val = getattr(old_value, "requirements_editor_Description", None)
                if opp_val == self:
                    setattr(old_value, "requirements_editor_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_Description"):
                opp_val = getattr(value, "requirements_editor_Description", None)
                setattr(value, "requirements_editor_Description", self)

    @property
    def requirements_editor_Requirement10(self):
        return self.__requirements_editor_Requirement10

    @requirements_editor_Requirement10.setter
    def requirements_editor_Requirement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__requirements_editor_Requirement10", None)
        self.__requirements_editor_Requirement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_Category9"):
                opp_val = getattr(old_value, "requirements_editor_Category9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_Category9"):
                opp_val = getattr(value, "requirements_editor_Category9", None)
                if opp_val is None:
                    setattr(value, "requirements_editor_Category9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_editor_Requirement14(self):
        return self.__requirements_editor_Requirement14

    @requirements_editor_Requirement14.setter
    def requirements_editor_Requirement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__requirements_editor_Requirement14", None)
        self.__requirements_editor_Requirement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_editor_SimpleDependency"):
                opp_val = getattr(old_value, "requirements_editor_SimpleDependency", None)
                if opp_val == self:
                    setattr(old_value, "requirements_editor_SimpleDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_editor_SimpleDependency"):
                opp_val = getattr(value, "requirements_editor_SimpleDependency", None)
                setattr(value, "requirements_editor_SimpleDependency", self)

    @property
    def personOwnsRequirement(self):
        return self.__personOwnsRequirement

    @personOwnsRequirement.setter
    def personOwnsRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__personOwnsRequirement", None)
        self.__personOwnsRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person"):
                opp_val = getattr(old_value, "Person", None)
                if opp_val == self:
                    setattr(old_value, "Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person"):
                opp_val = getattr(value, "Person", None)
                setattr(value, "Person", self)

    @property
    def requirements_editor_Requirement3(self):
        return self.__requirements_editor_Requirement3

    @requirements_editor_Requirement3.setter
    def requirements_editor_Requirement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__requirements_editor_Requirement3", None)
        self.__requirements_editor_Requirement3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_editor_Dependency"):
                    opp_val = getattr(item, "requirements_editor_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_editor_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_editor_Dependency"):
                    opp_val = getattr(item, "requirements_editor_Dependency", None)
                    
                    setattr(item, "requirements_editor_Dependency", self)
                    

    @property
    def Requirement(self):
        return self.__Requirement

    @Requirement.setter
    def Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_editor_Requirement__Requirement", None)
        self.__Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementOwnedBy"):
                opp_val = getattr(old_value, "requirementOwnedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementOwnedBy"):
                opp_val = getattr(value, "requirementOwnedBy", None)
                if opp_val is None:
                    setattr(value, "requirementOwnedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def findLeafNodes(self, requirements_editor_argument) :
        # TODO: Implement findLeafNodes method
        pass
