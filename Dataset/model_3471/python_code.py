from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeDomain(Enum):
    Continuous = "Continuous"
    Boolean = "Boolean"
class ScaleOrders(Enum):
    HigherIsBetter = "HigherIsBetter"
    LowerIsBetter = "LowerIsBetter"
    ExistenceIsBetter = "ExistenceIsBetter"
class FeatureTypes(Enum):
    GroupingFeature = "GroupingFeature"
    AbstractFeature = "AbstractFeature"
    InstanceFeature = "InstanceFeature"
class AggregationRules(Enum):
    Sum = "Sum"
    Product = "Product"
    AtLeastOnce = "AtLeastOnce"
    Minimum = "Minimum"
    Maximum = "Maximum"


############################################
# Definition of Classes
############################################

class servicefeaturemodel_Preference:

    def __init__(self, creationDate: date, description: str, value: float, stakeholderGroup: str, servicefeaturemodel_Preference: "servicefeaturemodel_Configuration" = None):
        self.creationDate = creationDate
        self.description = description
        self.value = value
        self.stakeholderGroup = stakeholderGroup
        self.servicefeaturemodel_Preference = servicefeaturemodel_Preference
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def stakeholderGroup(self) -> str:
        return self.__stakeholderGroup

    @stakeholderGroup.setter
    def stakeholderGroup(self, stakeholderGroup: str):
        self.__stakeholderGroup = stakeholderGroup

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def servicefeaturemodel_Preference(self):
        return self.__servicefeaturemodel_Preference

    @servicefeaturemodel_Preference.setter
    def servicefeaturemodel_Preference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Preference__servicefeaturemodel_Preference", None)
        self.__servicefeaturemodel_Preference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Configuration29"):
                opp_val = getattr(old_value, "servicefeaturemodel_Configuration29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Configuration29"):
                opp_val = getattr(value, "servicefeaturemodel_Configuration29", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_Configuration29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GroupRelationship:

    pass
class servicefeaturemodel_OR(GroupRelationship):

    def __init__(self, minFeaturesToChoose: int, maxFeaturesToChoose: int):
        self.minFeaturesToChoose = minFeaturesToChoose
        self.maxFeaturesToChoose = maxFeaturesToChoose
        
    @property
    def minFeaturesToChoose(self) -> int:
        return self.__minFeaturesToChoose

    @minFeaturesToChoose.setter
    def minFeaturesToChoose(self, minFeaturesToChoose: int):
        self.__minFeaturesToChoose = minFeaturesToChoose

    @property
    def maxFeaturesToChoose(self) -> int:
        return self.__maxFeaturesToChoose

    @maxFeaturesToChoose.setter
    def maxFeaturesToChoose(self, maxFeaturesToChoose: int):
        self.__maxFeaturesToChoose = maxFeaturesToChoose

class servicefeaturemodel_Configuration:

    def __init__(self, name: str, id: str, selected: bool, description: str, servicefeaturemodel_Configuration37: "servicefeaturemodel_Configurations" = None, servicefeaturemodel_Configuration: set["servicefeaturemodel_ServiceFeature"] = None, servicefeaturemodel_Configuration29: set["servicefeaturemodel_Preference"] = None, servicefeaturemodel_Configuration31: set["servicefeaturemodel_Attribute"] = None):
        self.name = name
        self.id = id
        self.selected = selected
        self.description = description
        self.servicefeaturemodel_Configuration37 = servicefeaturemodel_Configuration37
        self.servicefeaturemodel_Configuration = servicefeaturemodel_Configuration if servicefeaturemodel_Configuration is not None else set()
        self.servicefeaturemodel_Configuration29 = servicefeaturemodel_Configuration29 if servicefeaturemodel_Configuration29 is not None else set()
        self.servicefeaturemodel_Configuration31 = servicefeaturemodel_Configuration31 if servicefeaturemodel_Configuration31 is not None else set()
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def servicefeaturemodel_Configuration(self):
        return self.__servicefeaturemodel_Configuration

    @servicefeaturemodel_Configuration.setter
    def servicefeaturemodel_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Configuration__servicefeaturemodel_Configuration", None)
        self.__servicefeaturemodel_Configuration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature27"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature27", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_ServiceFeature27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature27"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature27", None)
                    
                    setattr(item, "servicefeaturemodel_ServiceFeature27", self)
                    

    @property
    def servicefeaturemodel_Configuration31(self):
        return self.__servicefeaturemodel_Configuration31

    @servicefeaturemodel_Configuration31.setter
    def servicefeaturemodel_Configuration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Configuration__servicefeaturemodel_Configuration31", None)
        self.__servicefeaturemodel_Configuration31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_Attribute32"):
                    opp_val = getattr(item, "servicefeaturemodel_Attribute32", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_Attribute32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_Attribute32"):
                    opp_val = getattr(item, "servicefeaturemodel_Attribute32", None)
                    
                    setattr(item, "servicefeaturemodel_Attribute32", self)
                    

    @property
    def servicefeaturemodel_Configuration37(self):
        return self.__servicefeaturemodel_Configuration37

    @servicefeaturemodel_Configuration37.setter
    def servicefeaturemodel_Configuration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Configuration__servicefeaturemodel_Configuration37", None)
        self.__servicefeaturemodel_Configuration37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Configurations36"):
                opp_val = getattr(old_value, "servicefeaturemodel_Configurations36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Configurations36"):
                opp_val = getattr(value, "servicefeaturemodel_Configurations36", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_Configurations36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def servicefeaturemodel_Configuration29(self):
        return self.__servicefeaturemodel_Configuration29

    @servicefeaturemodel_Configuration29.setter
    def servicefeaturemodel_Configuration29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Configuration__servicefeaturemodel_Configuration29", None)
        self.__servicefeaturemodel_Configuration29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_Preference"):
                    opp_val = getattr(item, "servicefeaturemodel_Preference", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_Preference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_Preference"):
                    opp_val = getattr(item, "servicefeaturemodel_Preference", None)
                    
                    setattr(item, "servicefeaturemodel_Preference", self)
                    

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class servicefeaturemodel_XOR(GroupRelationship):

    pass
class servicefeaturemodel_Requires:

    pass
class servicefeaturemodel_GroupRelationship(ABC):

    pass
class servicefeaturemodel_Attribute:

    def __init__(self, instantiationValue: str, id: str, servicefeaturemodel_Attribute16: "servicefeaturemodel_AttributeType" = None, servicefeaturemodel_Attribute: "servicefeaturemodel_ServiceFeature" = None, servicefeaturemodel_Attribute32: "servicefeaturemodel_Configuration" = None):
        self.instantiationValue = instantiationValue
        self.id = id
        self.servicefeaturemodel_Attribute16 = servicefeaturemodel_Attribute16
        self.servicefeaturemodel_Attribute = servicefeaturemodel_Attribute
        self.servicefeaturemodel_Attribute32 = servicefeaturemodel_Attribute32
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def instantiationValue(self) -> str:
        return self.__instantiationValue

    @instantiationValue.setter
    def instantiationValue(self, instantiationValue: str):
        self.__instantiationValue = instantiationValue

    @property
    def servicefeaturemodel_Attribute32(self):
        return self.__servicefeaturemodel_Attribute32

    @servicefeaturemodel_Attribute32.setter
    def servicefeaturemodel_Attribute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Attribute__servicefeaturemodel_Attribute32", None)
        self.__servicefeaturemodel_Attribute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Configuration31"):
                opp_val = getattr(old_value, "servicefeaturemodel_Configuration31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Configuration31"):
                opp_val = getattr(value, "servicefeaturemodel_Configuration31", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_Configuration31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def servicefeaturemodel_Attribute16(self):
        return self.__servicefeaturemodel_Attribute16

    @servicefeaturemodel_Attribute16.setter
    def servicefeaturemodel_Attribute16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Attribute__servicefeaturemodel_Attribute16", None)
        self.__servicefeaturemodel_Attribute16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_AttributeType"):
                opp_val = getattr(old_value, "servicefeaturemodel_AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_AttributeType"):
                opp_val = getattr(value, "servicefeaturemodel_AttributeType", None)
                setattr(value, "servicefeaturemodel_AttributeType", self)

    @property
    def servicefeaturemodel_Attribute(self):
        return self.__servicefeaturemodel_Attribute

    @servicefeaturemodel_Attribute.setter
    def servicefeaturemodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Attribute__servicefeaturemodel_Attribute", None)
        self.__servicefeaturemodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_ServiceFeature"):
                opp_val = getattr(old_value, "servicefeaturemodel_ServiceFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_ServiceFeature"):
                opp_val = getattr(value, "servicefeaturemodel_ServiceFeature", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_ServiceFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class servicefeaturemodel_ServiceFeature(ABC):

    def __init__(self, id: str, required: bool, requirementWeight: str, name: str, description: str, servicefeaturemodel_ServiceFeature9: set["servicefeaturemodel_Requires"] = None, servicefeaturemodel_ServiceFeature11: set["servicefeaturemodel_Excludes"] = None, servicefeaturemodel_ServiceFeature14: "servicefeaturemodel_ServiceFeature" = None, servicefeaturemodel_ServiceFeature12: set["servicefeaturemodel_ServiceFeature"] = None, servicefeaturemodel_ServiceFeature: set["servicefeaturemodel_Attribute"] = None, servicefeaturemodel_ServiceFeature7: "servicefeaturemodel_GroupRelationship" = None, servicefeaturemodel_ServiceFeature25: "servicefeaturemodel_ServiceFeatureDiagram" = None, servicefeaturemodel_ServiceFeature19: "servicefeaturemodel_Requires" = None, servicefeaturemodel_ServiceFeature22: "servicefeaturemodel_Excludes" = None, servicefeaturemodel_ServiceFeature27: "servicefeaturemodel_Configuration" = None):
        self.id = id
        self.required = required
        self.requirementWeight = requirementWeight
        self.name = name
        self.description = description
        self.servicefeaturemodel_ServiceFeature9 = servicefeaturemodel_ServiceFeature9 if servicefeaturemodel_ServiceFeature9 is not None else set()
        self.servicefeaturemodel_ServiceFeature11 = servicefeaturemodel_ServiceFeature11 if servicefeaturemodel_ServiceFeature11 is not None else set()
        self.servicefeaturemodel_ServiceFeature14 = servicefeaturemodel_ServiceFeature14
        self.servicefeaturemodel_ServiceFeature12 = servicefeaturemodel_ServiceFeature12 if servicefeaturemodel_ServiceFeature12 is not None else set()
        self.servicefeaturemodel_ServiceFeature = servicefeaturemodel_ServiceFeature if servicefeaturemodel_ServiceFeature is not None else set()
        self.servicefeaturemodel_ServiceFeature7 = servicefeaturemodel_ServiceFeature7
        self.servicefeaturemodel_ServiceFeature25 = servicefeaturemodel_ServiceFeature25
        self.servicefeaturemodel_ServiceFeature19 = servicefeaturemodel_ServiceFeature19
        self.servicefeaturemodel_ServiceFeature22 = servicefeaturemodel_ServiceFeature22
        self.servicefeaturemodel_ServiceFeature27 = servicefeaturemodel_ServiceFeature27
        
    @property
    def requirementWeight(self) -> str:
        return self.__requirementWeight

    @requirementWeight.setter
    def requirementWeight(self, requirementWeight: str):
        self.__requirementWeight = requirementWeight

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def servicefeaturemodel_ServiceFeature9(self):
        return self.__servicefeaturemodel_ServiceFeature9

    @servicefeaturemodel_ServiceFeature9.setter
    def servicefeaturemodel_ServiceFeature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature9", None)
        self.__servicefeaturemodel_ServiceFeature9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_Requires"):
                    opp_val = getattr(item, "servicefeaturemodel_Requires", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_Requires", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_Requires"):
                    opp_val = getattr(item, "servicefeaturemodel_Requires", None)
                    
                    setattr(item, "servicefeaturemodel_Requires", self)
                    

    @property
    def servicefeaturemodel_ServiceFeature7(self):
        return self.__servicefeaturemodel_ServiceFeature7

    @servicefeaturemodel_ServiceFeature7.setter
    def servicefeaturemodel_ServiceFeature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature7", None)
        self.__servicefeaturemodel_ServiceFeature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_GroupRelationship"):
                opp_val = getattr(old_value, "servicefeaturemodel_GroupRelationship", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_GroupRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_GroupRelationship"):
                opp_val = getattr(value, "servicefeaturemodel_GroupRelationship", None)
                setattr(value, "servicefeaturemodel_GroupRelationship", self)

    @property
    def servicefeaturemodel_ServiceFeature11(self):
        return self.__servicefeaturemodel_ServiceFeature11

    @servicefeaturemodel_ServiceFeature11.setter
    def servicefeaturemodel_ServiceFeature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature11", None)
        self.__servicefeaturemodel_ServiceFeature11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_Excludes"):
                    opp_val = getattr(item, "servicefeaturemodel_Excludes", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_Excludes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_Excludes"):
                    opp_val = getattr(item, "servicefeaturemodel_Excludes", None)
                    
                    setattr(item, "servicefeaturemodel_Excludes", self)
                    

    @property
    def servicefeaturemodel_ServiceFeature22(self):
        return self.__servicefeaturemodel_ServiceFeature22

    @servicefeaturemodel_ServiceFeature22.setter
    def servicefeaturemodel_ServiceFeature22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature22", None)
        self.__servicefeaturemodel_ServiceFeature22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Excludes21"):
                opp_val = getattr(old_value, "servicefeaturemodel_Excludes21", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Excludes21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Excludes21"):
                opp_val = getattr(value, "servicefeaturemodel_Excludes21", None)
                setattr(value, "servicefeaturemodel_Excludes21", self)

    @property
    def servicefeaturemodel_ServiceFeature27(self):
        return self.__servicefeaturemodel_ServiceFeature27

    @servicefeaturemodel_ServiceFeature27.setter
    def servicefeaturemodel_ServiceFeature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature27", None)
        self.__servicefeaturemodel_ServiceFeature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Configuration"):
                opp_val = getattr(old_value, "servicefeaturemodel_Configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Configuration"):
                opp_val = getattr(value, "servicefeaturemodel_Configuration", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_Configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def servicefeaturemodel_ServiceFeature12(self):
        return self.__servicefeaturemodel_ServiceFeature12

    @servicefeaturemodel_ServiceFeature12.setter
    def servicefeaturemodel_ServiceFeature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature12", None)
        self.__servicefeaturemodel_ServiceFeature12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature14"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature14", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_ServiceFeature14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature14"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature14", None)
                    
                    setattr(item, "servicefeaturemodel_ServiceFeature14", self)
                    

    @property
    def servicefeaturemodel_ServiceFeature25(self):
        return self.__servicefeaturemodel_ServiceFeature25

    @servicefeaturemodel_ServiceFeature25.setter
    def servicefeaturemodel_ServiceFeature25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature25", None)
        self.__servicefeaturemodel_ServiceFeature25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram24"):
                opp_val = getattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_ServiceFeatureDiagram24"):
                opp_val = getattr(value, "servicefeaturemodel_ServiceFeatureDiagram24", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_ServiceFeatureDiagram24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def servicefeaturemodel_ServiceFeature14(self):
        return self.__servicefeaturemodel_ServiceFeature14

    @servicefeaturemodel_ServiceFeature14.setter
    def servicefeaturemodel_ServiceFeature14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature14", None)
        self.__servicefeaturemodel_ServiceFeature14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_ServiceFeature12"):
                opp_val = getattr(old_value, "servicefeaturemodel_ServiceFeature12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_ServiceFeature12"):
                opp_val = getattr(value, "servicefeaturemodel_ServiceFeature12", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_ServiceFeature12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def servicefeaturemodel_ServiceFeature(self):
        return self.__servicefeaturemodel_ServiceFeature

    @servicefeaturemodel_ServiceFeature.setter
    def servicefeaturemodel_ServiceFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature", None)
        self.__servicefeaturemodel_ServiceFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_Attribute"):
                    opp_val = getattr(item, "servicefeaturemodel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_Attribute"):
                    opp_val = getattr(item, "servicefeaturemodel_Attribute", None)
                    
                    setattr(item, "servicefeaturemodel_Attribute", self)
                    

    @property
    def servicefeaturemodel_ServiceFeature19(self):
        return self.__servicefeaturemodel_ServiceFeature19

    @servicefeaturemodel_ServiceFeature19.setter
    def servicefeaturemodel_ServiceFeature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature19", None)
        self.__servicefeaturemodel_ServiceFeature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Requires18"):
                opp_val = getattr(old_value, "servicefeaturemodel_Requires18", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Requires18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Requires18"):
                opp_val = getattr(value, "servicefeaturemodel_Requires18", None)
                setattr(value, "servicefeaturemodel_Requires18", self)

class servicefeaturemodel_AttributeType:

    def __init__(self, requirementWeight: str, name: str, domain: str, aggregationRule: str, scaleOrder: str, toBeEvaluated: bool, description: str, customAttributeTypePriority: int, requirement: str, servicefeaturemodel_AttributeType: "servicefeaturemodel_Attribute" = None, servicefeaturemodel_AttributeType40: "servicefeaturemodel_AttributeTypes" = None):
        self.requirementWeight = requirementWeight
        self.name = name
        self.domain = domain
        self.aggregationRule = aggregationRule
        self.scaleOrder = scaleOrder
        self.toBeEvaluated = toBeEvaluated
        self.description = description
        self.customAttributeTypePriority = customAttributeTypePriority
        self.requirement = requirement
        self.servicefeaturemodel_AttributeType = servicefeaturemodel_AttributeType
        self.servicefeaturemodel_AttributeType40 = servicefeaturemodel_AttributeType40
        
    @property
    def aggregationRule(self) -> str:
        return self.__aggregationRule

    @aggregationRule.setter
    def aggregationRule(self, aggregationRule: str):
        self.__aggregationRule = aggregationRule

    @property
    def toBeEvaluated(self) -> bool:
        return self.__toBeEvaluated

    @toBeEvaluated.setter
    def toBeEvaluated(self, toBeEvaluated: bool):
        self.__toBeEvaluated = toBeEvaluated

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def requirement(self) -> str:
        return self.__requirement

    @requirement.setter
    def requirement(self, requirement: str):
        self.__requirement = requirement

    @property
    def scaleOrder(self) -> str:
        return self.__scaleOrder

    @scaleOrder.setter
    def scaleOrder(self, scaleOrder: str):
        self.__scaleOrder = scaleOrder

    @property
    def requirementWeight(self) -> str:
        return self.__requirementWeight

    @requirementWeight.setter
    def requirementWeight(self, requirementWeight: str):
        self.__requirementWeight = requirementWeight

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def customAttributeTypePriority(self) -> int:
        return self.__customAttributeTypePriority

    @customAttributeTypePriority.setter
    def customAttributeTypePriority(self, customAttributeTypePriority: int):
        self.__customAttributeTypePriority = customAttributeTypePriority

    @property
    def servicefeaturemodel_AttributeType(self):
        return self.__servicefeaturemodel_AttributeType

    @servicefeaturemodel_AttributeType.setter
    def servicefeaturemodel_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_AttributeType__servicefeaturemodel_AttributeType", None)
        self.__servicefeaturemodel_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Attribute16"):
                opp_val = getattr(old_value, "servicefeaturemodel_Attribute16", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Attribute16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Attribute16"):
                opp_val = getattr(value, "servicefeaturemodel_Attribute16", None)
                setattr(value, "servicefeaturemodel_Attribute16", self)

    @property
    def servicefeaturemodel_AttributeType40(self):
        return self.__servicefeaturemodel_AttributeType40

    @servicefeaturemodel_AttributeType40.setter
    def servicefeaturemodel_AttributeType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_AttributeType__servicefeaturemodel_AttributeType40", None)
        self.__servicefeaturemodel_AttributeType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_AttributeTypes39"):
                opp_val = getattr(old_value, "servicefeaturemodel_AttributeTypes39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_AttributeTypes39"):
                opp_val = getattr(value, "servicefeaturemodel_AttributeTypes39", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_AttributeTypes39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ServiceFeature:

    pass
class servicefeaturemodel_MandatoryServiceFeature(ServiceFeature):

    def __init__(self, featureTypes: str):
        self.featureTypes = featureTypes
        
    @property
    def featureTypes(self) -> str:
        return self.__featureTypes

    @featureTypes.setter
    def featureTypes(self, featureTypes: str):
        self.__featureTypes = featureTypes

class servicefeaturemodel_OptionalServiceFeature(ServiceFeature):

    def __init__(self, featureType: str, servicefeaturemodel_OptionalServiceFeature: "servicefeaturemodel_GroupRelationship" = None):
        self.featureType = featureType
        self.servicefeaturemodel_OptionalServiceFeature = servicefeaturemodel_OptionalServiceFeature
        
    @property
    def featureType(self) -> str:
        return self.__featureType

    @featureType.setter
    def featureType(self, featureType: str):
        self.__featureType = featureType

    @property
    def servicefeaturemodel_OptionalServiceFeature(self):
        return self.__servicefeaturemodel_OptionalServiceFeature

    @servicefeaturemodel_OptionalServiceFeature.setter
    def servicefeaturemodel_OptionalServiceFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_OptionalServiceFeature__servicefeaturemodel_OptionalServiceFeature", None)
        self.__servicefeaturemodel_OptionalServiceFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_GroupRelationship34"):
                opp_val = getattr(old_value, "servicefeaturemodel_GroupRelationship34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_GroupRelationship34"):
                opp_val = getattr(value, "servicefeaturemodel_GroupRelationship34", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_GroupRelationship34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class servicefeaturemodel_Excludes:

    pass
class servicefeaturemodel_AttributeTypes:

    pass
class servicefeaturemodel_Configurations:

    pass
class servicefeaturemodel_ServiceFeatureDiagram:

    def __init__(self, name: str, description: str, id: str, servicefeaturemodel_ServiceFeatureDiagram: "servicefeaturemodel_Service" = None, servicefeaturemodel_ServiceFeatureDiagram24: set["servicefeaturemodel_ServiceFeature"] = None):
        self.name = name
        self.description = description
        self.id = id
        self.servicefeaturemodel_ServiceFeatureDiagram = servicefeaturemodel_ServiceFeatureDiagram
        self.servicefeaturemodel_ServiceFeatureDiagram24 = servicefeaturemodel_ServiceFeatureDiagram24 if servicefeaturemodel_ServiceFeatureDiagram24 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def servicefeaturemodel_ServiceFeatureDiagram(self):
        return self.__servicefeaturemodel_ServiceFeatureDiagram

    @servicefeaturemodel_ServiceFeatureDiagram.setter
    def servicefeaturemodel_ServiceFeatureDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeatureDiagram__servicefeaturemodel_ServiceFeatureDiagram", None)
        self.__servicefeaturemodel_ServiceFeatureDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Service"):
                opp_val = getattr(old_value, "servicefeaturemodel_Service", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Service"):
                opp_val = getattr(value, "servicefeaturemodel_Service", None)
                setattr(value, "servicefeaturemodel_Service", self)

    @property
    def servicefeaturemodel_ServiceFeatureDiagram24(self):
        return self.__servicefeaturemodel_ServiceFeatureDiagram24

    @servicefeaturemodel_ServiceFeatureDiagram24.setter
    def servicefeaturemodel_ServiceFeatureDiagram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeatureDiagram__servicefeaturemodel_ServiceFeatureDiagram24", None)
        self.__servicefeaturemodel_ServiceFeatureDiagram24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature25"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature25", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_ServiceFeature25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature25"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature25", None)
                    
                    setattr(item, "servicefeaturemodel_ServiceFeature25", self)
                    

class servicefeaturemodel_Service:

    def __init__(self, description: str, id: str, name: str, servicefeaturemodel_Service: "servicefeaturemodel_ServiceFeatureDiagram" = None, servicefeaturemodel_Service2: "servicefeaturemodel_Configurations" = None, servicefeaturemodel_Service4: "servicefeaturemodel_AttributeTypes" = None):
        self.description = description
        self.id = id
        self.name = name
        self.servicefeaturemodel_Service = servicefeaturemodel_Service
        self.servicefeaturemodel_Service2 = servicefeaturemodel_Service2
        self.servicefeaturemodel_Service4 = servicefeaturemodel_Service4
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def servicefeaturemodel_Service(self):
        return self.__servicefeaturemodel_Service

    @servicefeaturemodel_Service.setter
    def servicefeaturemodel_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Service__servicefeaturemodel_Service", None)
        self.__servicefeaturemodel_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram"):
                opp_val = getattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_ServiceFeatureDiagram"):
                opp_val = getattr(value, "servicefeaturemodel_ServiceFeatureDiagram", None)
                setattr(value, "servicefeaturemodel_ServiceFeatureDiagram", self)

    @property
    def servicefeaturemodel_Service4(self):
        return self.__servicefeaturemodel_Service4

    @servicefeaturemodel_Service4.setter
    def servicefeaturemodel_Service4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Service__servicefeaturemodel_Service4", None)
        self.__servicefeaturemodel_Service4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_AttributeTypes"):
                opp_val = getattr(old_value, "servicefeaturemodel_AttributeTypes", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_AttributeTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_AttributeTypes"):
                opp_val = getattr(value, "servicefeaturemodel_AttributeTypes", None)
                setattr(value, "servicefeaturemodel_AttributeTypes", self)

    @property
    def servicefeaturemodel_Service2(self):
        return self.__servicefeaturemodel_Service2

    @servicefeaturemodel_Service2.setter
    def servicefeaturemodel_Service2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Service__servicefeaturemodel_Service2", None)
        self.__servicefeaturemodel_Service2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Configurations"):
                opp_val = getattr(old_value, "servicefeaturemodel_Configurations", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Configurations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Configurations"):
                opp_val = getattr(value, "servicefeaturemodel_Configurations", None)
                setattr(value, "servicefeaturemodel_Configurations", self)
