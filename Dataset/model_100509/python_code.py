from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RequirementType(Enum):
    functional = "functional"
    technical = "technical"


############################################
# Definition of Classes
############################################

class requirement_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class requirement_EObject:

    pass
class NamedElement:

    pass
class requirement_Requirement(NamedElement):

    def __init__(self, id: str, status: str, createdOn: date, modifiedOn: date, version: int, statement: str, rationale: str, acceptanceCriteria: str, type: str, subtype: str, Requirement: "requirement_Category" = None, requirement_Requirement: set["requirement_EObject"] = None, requirements: "requirement_Category" = None):
        self.id = id
        self.status = status
        self.createdOn = createdOn
        self.modifiedOn = modifiedOn
        self.version = version
        self.statement = statement
        self.rationale = rationale
        self.acceptanceCriteria = acceptanceCriteria
        self.type = type
        self.subtype = subtype
        self.Requirement = Requirement
        self.requirement_Requirement = requirement_Requirement if requirement_Requirement is not None else set()
        self.requirements = requirements
        
        pass
    @property
    def createdOn(self):
        return self.__createdOn

    @createdOn.setter
    def createdOn(self, createdOn: date):
        self.__createdOn = createdOn


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def subtype(self):
        return self.__subtype

    @subtype.setter
    def subtype(self, subtype: str):
        self.__subtype = subtype


    @property
    def statement(self):
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement


    @property
    def rationale(self):
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def modifiedOn(self):
        return self.__modifiedOn

    @modifiedOn.setter
    def modifiedOn(self, modifiedOn: date):
        self.__modifiedOn = modifiedOn


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def acceptanceCriteria(self):
        return self.__acceptanceCriteria

    @acceptanceCriteria.setter
    def acceptanceCriteria(self, acceptanceCriteria: str):
        self.__acceptanceCriteria = acceptanceCriteria


    @property
    def Requirement(self):
        return self.__Requirement

    @Requirement.setter
    def Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Requirement__Requirement", None)
        self.__Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_Requirement(self):
        return self.__requirement_Requirement

    @requirement_Requirement.setter
    def requirement_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Requirement__requirement_Requirement", None)
        self.__requirement_Requirement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_EObject13"):
                    opp_val = getattr(item, "requirement_EObject13", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_EObject13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_EObject13"):
                    opp_val = getattr(item, "requirement_EObject13", None)
                    
                    setattr(item, "requirement_EObject13", self)
                    

    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Requirement__requirements", None)
        self.__requirements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category15"):
                opp_val = getattr(old_value, "Category15", None)
                if opp_val == self:
                    setattr(old_value, "Category15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category15"):
                opp_val = getattr(value, "Category15", None)
                setattr(value, "Category15", self)

class requirement_Category(NamedElement):

    def __init__(self, id: str, Category: "requirement_Repository" = None, mainCategories: "requirement_Repository" = None, Category9: "requirement_Category" = None, subCategories: "requirement_Category" = None, requirement_Category: set["requirement_EObject"] = None, category: set["requirement_Requirement"] = None, Category5: "requirement_Category" = None, parentCategory: set["requirement_Category"] = None, Category15: "requirement_Requirement" = None):
        self.id = id
        self.Category = Category
        self.mainCategories = mainCategories
        self.Category9 = Category9
        self.subCategories = subCategories
        self.requirement_Category = requirement_Category if requirement_Category is not None else set()
        self.category = category if category is not None else set()
        self.Category5 = Category5
        self.parentCategory = parentCategory if parentCategory is not None else set()
        self.Category15 = Category15
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__Category", None)
        self.__Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository"):
                opp_val = getattr(old_value, "repository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository"):
                opp_val = getattr(value, "repository", None)
                if opp_val is None:
                    setattr(value, "repository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_Category(self):
        return self.__requirement_Category

    @requirement_Category.setter
    def requirement_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__requirement_Category", None)
        self.__requirement_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_EObject11"):
                    opp_val = getattr(item, "requirement_EObject11", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_EObject11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_EObject11"):
                    opp_val = getattr(item, "requirement_EObject11", None)
                    
                    setattr(item, "requirement_EObject11", self)
                    

    @property
    def subCategories(self):
        return self.__subCategories

    @subCategories.setter
    def subCategories(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__subCategories", None)
        self.__subCategories = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category9"):
                opp_val = getattr(old_value, "Category9", None)
                if opp_val == self:
                    setattr(old_value, "Category9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category9"):
                opp_val = getattr(value, "Category9", None)
                setattr(value, "Category9", self)

    @property
    def mainCategories(self):
        return self.__mainCategories

    @mainCategories.setter
    def mainCategories(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__mainCategories", None)
        self.__mainCategories = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository"):
                opp_val = getattr(old_value, "Repository", None)
                if opp_val == self:
                    setattr(old_value, "Repository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository"):
                opp_val = getattr(value, "Repository", None)
                setattr(value, "Repository", self)

    @property
    def Category15(self):
        return self.__Category15

    @Category15.setter
    def Category15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__Category15", None)
        self.__Category15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements"):
                opp_val = getattr(old_value, "requirements", None)
                if opp_val == self:
                    setattr(old_value, "requirements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements"):
                opp_val = getattr(value, "requirements", None)
                setattr(value, "requirements", self)

    @property
    def Category5(self):
        return self.__Category5

    @Category5.setter
    def Category5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__Category5", None)
        self.__Category5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentCategory"):
                opp_val = getattr(old_value, "parentCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentCategory"):
                opp_val = getattr(value, "parentCategory", None)
                if opp_val is None:
                    setattr(value, "parentCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentCategory(self):
        return self.__parentCategory

    @parentCategory.setter
    def parentCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__parentCategory", None)
        self.__parentCategory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category5"):
                    opp_val = getattr(item, "Category5", None)
                    
                    if opp_val == self:
                        setattr(item, "Category5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category5"):
                    opp_val = getattr(item, "Category5", None)
                    
                    setattr(item, "Category5", self)
                    

    @property
    def Category9(self):
        return self.__Category9

    @Category9.setter
    def Category9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__Category9", None)
        self.__Category9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategories"):
                opp_val = getattr(old_value, "subCategories", None)
                if opp_val == self:
                    setattr(old_value, "subCategories", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategories"):
                opp_val = getattr(value, "subCategories", None)
                setattr(value, "subCategories", self)

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Category__category", None)
        self.__category = value if value is not None else set()
        
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
                    

class requirement_Repository(NamedElement):

    pass