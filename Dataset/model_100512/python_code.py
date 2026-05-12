from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeType(Enum):
    TextualValue = "TextualValue"
    NumericalValue = "NumericalValue"
    TemporalValue = "TemporalValue"
    Other = "Other"
class PrivilegeNature(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class AnnotationStatus(Enum):
    New = "New"
    Fixed = "Fixed"
    Invalid = "Invalid"
    Wontfix = "Wontfix"
    Duplicate = "Duplicate"
    Incomplete = "Incomplete"
class PriorityLevel(Enum):
    VeryHigh = "VeryHigh"
    High = "High"
    Normal = "Normal"
    Low = "Low"
    VeryLow = "VeryLow"


############################################
# Definition of Classes
############################################

class requirements_Annotation:

    def __init__(self, comment: str, author: str, annotation: str, date: date, status: str, id: str, requirements_Annotation: "requirements_AnnotableElement" = None):
        self.comment = comment
        self.author = author
        self.annotation = annotation
        self.date = date
        self.status = status
        self.id = id
        self.requirements_Annotation = requirements_Annotation
        
        pass
    @property
    def annotation(self):
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: str):
        self.__annotation = annotation


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def requirements_Annotation(self):
        return self.__requirements_Annotation

    @requirements_Annotation.setter
    def requirements_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Annotation__requirements_Annotation", None)
        self.__requirements_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_AnnotableElement"):
                opp_val = getattr(old_value, "requirements_AnnotableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_AnnotableElement"):
                opp_val = getattr(value, "requirements_AnnotableElement", None)
                if opp_val is None:
                    setattr(value, "requirements_AnnotableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class requirements_Privilege:

    def __init__(self, category: str, requirements_Privilege: "requirements_BasicElement" = None, requirements_Privilege24: "requirements_PrivilegeGroup" = None):
        self.category = category
        self.requirements_Privilege = requirements_Privilege
        self.requirements_Privilege24 = requirements_Privilege24
        
        pass
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def requirements_Privilege24(self):
        return self.__requirements_Privilege24

    @requirements_Privilege24.setter
    def requirements_Privilege24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Privilege__requirements_Privilege24", None)
        self.__requirements_Privilege24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_PrivilegeGroup23"):
                opp_val = getattr(old_value, "requirements_PrivilegeGroup23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_PrivilegeGroup23"):
                opp_val = getattr(value, "requirements_PrivilegeGroup23", None)
                if opp_val is None:
                    setattr(value, "requirements_PrivilegeGroup23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_Privilege(self):
        return self.__requirements_Privilege

    @requirements_Privilege.setter
    def requirements_Privilege(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Privilege__requirements_Privilege", None)
        self.__requirements_Privilege = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_BasicElement"):
                opp_val = getattr(old_value, "requirements_BasicElement", None)
                if opp_val == self:
                    setattr(old_value, "requirements_BasicElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_BasicElement"):
                opp_val = getattr(value, "requirements_BasicElement", None)
                setattr(value, "requirements_BasicElement", self)

class requirements_GoalStep:

    pass
class Organization:

    pass
class requirements_Process(Organization):

    pass
class requirements_RequirementsDefinition(Organization):

    def __init__(self, version: str, date: date):
        self.version = version
        self.date = date
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


class AnnotableElement:

    pass
class requirements_Agent(AnnotableElement):

    def __init__(self, isHuman: bool, responsible: set["requirements_Goal"] = None, Agent: "requirements_Goal" = None):
        self.isHuman = isHuman
        self.responsible = responsible if responsible is not None else set()
        self.Agent = Agent
        
        pass
    @property
    def isHuman(self):
        return self.__isHuman

    @isHuman.setter
    def isHuman(self, isHuman: bool):
        self.__isHuman = isHuman


    @property
    def Agent(self):
        return self.__Agent

    @Agent.setter
    def Agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Agent__Agent", None)
        self.__Agent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isResponsible"):
                opp_val = getattr(old_value, "isResponsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isResponsible"):
                opp_val = getattr(value, "isResponsible", None)
                if opp_val is None:
                    setattr(value, "isResponsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def responsible(self):
        return self.__responsible

    @responsible.setter
    def responsible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Agent__responsible", None)
        self.__responsible = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    setattr(item, "Goal", self)
                    

class requirements_Organization(AnnotableElement):

    pass
class requirements_Goal(AnnotableElement):

    def __init__(self, priority: str, synopsis: str, Goal: "requirements_Agent" = None, requirements_Goal: "requirements_Goal" = None, requirements_Goal11: set["requirements_Goal"] = None, isResponsible: set["requirements_Agent"] = None, requirements_Goal15: set["requirements_PrivilegeGroup"] = None, requirements_Goal17: set["requirements_GoalStep"] = None, requirements_Goal27: "requirements_GoalStep" = None):
        self.priority = priority
        self.synopsis = synopsis
        self.Goal = Goal
        self.requirements_Goal = requirements_Goal
        self.requirements_Goal11 = requirements_Goal11 if requirements_Goal11 is not None else set()
        self.isResponsible = isResponsible if isResponsible is not None else set()
        self.requirements_Goal15 = requirements_Goal15 if requirements_Goal15 is not None else set()
        self.requirements_Goal17 = requirements_Goal17 if requirements_Goal17 is not None else set()
        self.requirements_Goal27 = requirements_Goal27
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def synopsis(self):
        return self.__synopsis

    @synopsis.setter
    def synopsis(self, synopsis: str):
        self.__synopsis = synopsis


    @property
    def requirements_Goal15(self):
        return self.__requirements_Goal15

    @requirements_Goal15.setter
    def requirements_Goal15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__requirements_Goal15", None)
        self.__requirements_Goal15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_PrivilegeGroup"):
                    opp_val = getattr(item, "requirements_PrivilegeGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_PrivilegeGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_PrivilegeGroup"):
                    opp_val = getattr(item, "requirements_PrivilegeGroup", None)
                    
                    setattr(item, "requirements_PrivilegeGroup", self)
                    

    @property
    def requirements_Goal(self):
        return self.__requirements_Goal

    @requirements_Goal.setter
    def requirements_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__requirements_Goal", None)
        self.__requirements_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Goal11"):
                opp_val = getattr(old_value, "requirements_Goal11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Goal11"):
                opp_val = getattr(value, "requirements_Goal11", None)
                if opp_val is None:
                    setattr(value, "requirements_Goal11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_Goal17(self):
        return self.__requirements_Goal17

    @requirements_Goal17.setter
    def requirements_Goal17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__requirements_Goal17", None)
        self.__requirements_Goal17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_GoalStep"):
                    opp_val = getattr(item, "requirements_GoalStep", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_GoalStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_GoalStep"):
                    opp_val = getattr(item, "requirements_GoalStep", None)
                    
                    setattr(item, "requirements_GoalStep", self)
                    

    @property
    def requirements_Goal27(self):
        return self.__requirements_Goal27

    @requirements_Goal27.setter
    def requirements_Goal27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__requirements_Goal27", None)
        self.__requirements_Goal27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_GoalStep26"):
                opp_val = getattr(old_value, "requirements_GoalStep26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_GoalStep26"):
                opp_val = getattr(value, "requirements_GoalStep26", None)
                if opp_val is None:
                    setattr(value, "requirements_GoalStep26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_Goal11(self):
        return self.__requirements_Goal11

    @requirements_Goal11.setter
    def requirements_Goal11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__requirements_Goal11", None)
        self.__requirements_Goal11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_Goal"):
                    opp_val = getattr(item, "requirements_Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_Goal"):
                    opp_val = getattr(item, "requirements_Goal", None)
                    
                    setattr(item, "requirements_Goal", self)
                    

    @property
    def isResponsible(self):
        return self.__isResponsible

    @isResponsible.setter
    def isResponsible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__isResponsible", None)
        self.__isResponsible = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Agent"):
                    opp_val = getattr(item, "Agent", None)
                    
                    if opp_val == self:
                        setattr(item, "Agent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Agent"):
                    opp_val = getattr(item, "Agent", None)
                    
                    setattr(item, "Agent", self)
                    

    @property
    def Goal(self):
        return self.__Goal

    @Goal.setter
    def Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Goal__Goal", None)
        self.__Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsible"):
                opp_val = getattr(old_value, "responsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsible"):
                opp_val = getattr(value, "responsible", None)
                if opp_val is None:
                    setattr(value, "responsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BasicElement:

    pass
class requirements_AnnotableElement(BasicElement):

    pass
class requirements_Entity(BasicElement):

    pass
class ModelElement:

    pass
class requirements_PrivilegeGroup(ModelElement):

    def __init__(self, documentation: str, requirements_PrivilegeGroup: "requirements_Goal" = None, requirements_PrivilegeGroup20: "requirements_Entity" = None, requirements_PrivilegeGroup23: set["requirements_Privilege"] = None):
        self.documentation = documentation
        self.requirements_PrivilegeGroup = requirements_PrivilegeGroup
        self.requirements_PrivilegeGroup20 = requirements_PrivilegeGroup20
        self.requirements_PrivilegeGroup23 = requirements_PrivilegeGroup23 if requirements_PrivilegeGroup23 is not None else set()
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def requirements_PrivilegeGroup(self):
        return self.__requirements_PrivilegeGroup

    @requirements_PrivilegeGroup.setter
    def requirements_PrivilegeGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_PrivilegeGroup__requirements_PrivilegeGroup", None)
        self.__requirements_PrivilegeGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Goal15"):
                opp_val = getattr(old_value, "requirements_Goal15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Goal15"):
                opp_val = getattr(value, "requirements_Goal15", None)
                if opp_val is None:
                    setattr(value, "requirements_Goal15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements_PrivilegeGroup23(self):
        return self.__requirements_PrivilegeGroup23

    @requirements_PrivilegeGroup23.setter
    def requirements_PrivilegeGroup23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_PrivilegeGroup__requirements_PrivilegeGroup23", None)
        self.__requirements_PrivilegeGroup23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirements_Privilege24"):
                    opp_val = getattr(item, "requirements_Privilege24", None)
                    
                    if opp_val == self:
                        setattr(item, "requirements_Privilege24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirements_Privilege24"):
                    opp_val = getattr(item, "requirements_Privilege24", None)
                    
                    setattr(item, "requirements_Privilege24", self)
                    

    @property
    def requirements_PrivilegeGroup20(self):
        return self.__requirements_PrivilegeGroup20

    @requirements_PrivilegeGroup20.setter
    def requirements_PrivilegeGroup20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_PrivilegeGroup__requirements_PrivilegeGroup20", None)
        self.__requirements_PrivilegeGroup20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Entity21"):
                opp_val = getattr(old_value, "requirements_Entity21", None)
                if opp_val == self:
                    setattr(old_value, "requirements_Entity21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Entity21"):
                opp_val = getattr(value, "requirements_Entity21", None)
                setattr(value, "requirements_Entity21", self)

class requirements_BasicElement(ModelElement):

    def __init__(self, name: str, documentation: str, id: str, requirements_BasicElement: "requirements_Privilege" = None):
        self.name = name
        self.documentation = documentation
        self.id = id
        self.requirements_BasicElement = requirements_BasicElement
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def requirements_BasicElement(self):
        return self.__requirements_BasicElement

    @requirements_BasicElement.setter
    def requirements_BasicElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_BasicElement__requirements_BasicElement", None)
        self.__requirements_BasicElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Privilege"):
                opp_val = getattr(old_value, "requirements_Privilege", None)
                if opp_val == self:
                    setattr(old_value, "requirements_Privilege", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Privilege"):
                opp_val = getattr(value, "requirements_Privilege", None)
                setattr(value, "requirements_Privilege", self)

class requirements_ModelElement(ABC):

    pass
class requirements_RelationShip(BasicElement):

    def __init__(self, sourceMin: int, sourceMax: int, targetMin: int, targetMax: int, requirements_RelationShip: "requirements_Entity" = None, requirements_RelationShip7: "requirements_Entity" = None):
        self.sourceMin = sourceMin
        self.sourceMax = sourceMax
        self.targetMin = targetMin
        self.targetMax = targetMax
        self.requirements_RelationShip = requirements_RelationShip
        self.requirements_RelationShip7 = requirements_RelationShip7
        
        pass
    @property
    def targetMax(self):
        return self.__targetMax

    @targetMax.setter
    def targetMax(self, targetMax: int):
        self.__targetMax = targetMax


    @property
    def targetMin(self):
        return self.__targetMin

    @targetMin.setter
    def targetMin(self, targetMin: int):
        self.__targetMin = targetMin


    @property
    def sourceMax(self):
        return self.__sourceMax

    @sourceMax.setter
    def sourceMax(self, sourceMax: int):
        self.__sourceMax = sourceMax


    @property
    def sourceMin(self):
        return self.__sourceMin

    @sourceMin.setter
    def sourceMin(self, sourceMin: int):
        self.__sourceMin = sourceMin


    @property
    def requirements_RelationShip(self):
        return self.__requirements_RelationShip

    @requirements_RelationShip.setter
    def requirements_RelationShip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_RelationShip__requirements_RelationShip", None)
        self.__requirements_RelationShip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Entity5"):
                opp_val = getattr(old_value, "requirements_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "requirements_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Entity5"):
                opp_val = getattr(value, "requirements_Entity5", None)
                setattr(value, "requirements_Entity5", self)

    @property
    def requirements_RelationShip7(self):
        return self.__requirements_RelationShip7

    @requirements_RelationShip7.setter
    def requirements_RelationShip7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_RelationShip__requirements_RelationShip7", None)
        self.__requirements_RelationShip7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Entity8"):
                opp_val = getattr(old_value, "requirements_Entity8", None)
                if opp_val == self:
                    setattr(old_value, "requirements_Entity8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Entity8"):
                opp_val = getattr(value, "requirements_Entity8", None)
                setattr(value, "requirements_Entity8", self)

class requirements_Attribute(BasicElement):

    def __init__(self, type: str, requirements_Attribute: "requirements_Entity" = None):
        self.type = type
        self.requirements_Attribute = requirements_Attribute
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def requirements_Attribute(self):
        return self.__requirements_Attribute

    @requirements_Attribute.setter
    def requirements_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirements_Attribute__requirements_Attribute", None)
        self.__requirements_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements_Entity3"):
                opp_val = getattr(old_value, "requirements_Entity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements_Entity3"):
                opp_val = getattr(value, "requirements_Entity3", None)
                if opp_val is None:
                    setattr(value, "requirements_Entity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
