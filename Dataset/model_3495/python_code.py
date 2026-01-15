from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AggregationRules(Enum):
    Sum = "Sum"
    Product = "Product"
    AtLeastOnce = "AtLeastOnce"
    Minimum = "Minimum"
    Maximum = "Maximum"
class ScaleOrders(Enum):
    HigherIsBetter = "HigherIsBetter"
    LowerIsBetter = "LowerIsBetter"
    ExistenceIsBetter = "ExistenceIsBetter"
class FeatureTypes(Enum):
    GroupingFeature = "GroupingFeature"
    AbstractFeature = "AbstractFeature"
    InstanceFeature = "InstanceFeature"
class AttributeDomain(Enum):
    Continuous = "Continuous"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class ModifyRelationship:

    pass
class servicefeaturemodel_FeatureToAttributeModifyRelationship(ModifyRelationship):

    pass
class servicefeaturemodel_AttributeToAttributeModifyRelationship(ModifyRelationship):

    def __init__(self, triggerParameterName: str, servicefeaturemodel_AttributeToAttributeModifyRelationship: "servicefeaturemodel_Attribute" = None):
        self.triggerParameterName = triggerParameterName
        self.servicefeaturemodel_AttributeToAttributeModifyRelationship = servicefeaturemodel_AttributeToAttributeModifyRelationship
        
    @property
    def triggerParameterName(self) -> str:
        return self.__triggerParameterName

    @triggerParameterName.setter
    def triggerParameterName(self, triggerParameterName: str):
        self.__triggerParameterName = triggerParameterName

    @property
    def servicefeaturemodel_AttributeToAttributeModifyRelationship(self):
        return self.__servicefeaturemodel_AttributeToAttributeModifyRelationship

    @servicefeaturemodel_AttributeToAttributeModifyRelationship.setter
    def servicefeaturemodel_AttributeToAttributeModifyRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_AttributeToAttributeModifyRelationship__servicefeaturemodel_AttributeToAttributeModifyRelationship", None)
        self.__servicefeaturemodel_AttributeToAttributeModifyRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Attribute44"):
                opp_val = getattr(old_value, "servicefeaturemodel_Attribute44", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Attribute44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Attribute44"):
                opp_val = getattr(value, "servicefeaturemodel_Attribute44", None)
                setattr(value, "servicefeaturemodel_Attribute44", self)

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
    def stakeholderGroup(self) -> str:
        return self.__stakeholderGroup

    @stakeholderGroup.setter
    def stakeholderGroup(self, stakeholderGroup: str):
        self.__stakeholderGroup = stakeholderGroup

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

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

class servicefeaturemodel_Configuration:

    def __init__(self, name: str, id: str, description: str, servicefeaturemodel_Configuration: set["servicefeaturemodel_ServiceFeature"] = None, servicefeaturemodel_Configuration31: set["servicefeaturemodel_Preference"] = None, servicefeaturemodel_Configuration33: set["servicefeaturemodel_Attribute"] = None, servicefeaturemodel_Configuration39: "servicefeaturemodel_PossibleConfigurations" = None):
        self.name = name
        self.id = id
        self.description = description
        self.servicefeaturemodel_Configuration = servicefeaturemodel_Configuration if servicefeaturemodel_Configuration is not None else set()
        self.servicefeaturemodel_Configuration31 = servicefeaturemodel_Configuration31 if servicefeaturemodel_Configuration31 is not None else set()
        self.servicefeaturemodel_Configuration33 = servicefeaturemodel_Configuration33 if servicefeaturemodel_Configuration33 is not None else set()
        self.servicefeaturemodel_Configuration39 = servicefeaturemodel_Configuration39
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def servicefeaturemodel_Configuration33(self):
        return self.__servicefeaturemodel_Configuration33

    @servicefeaturemodel_Configuration33.setter
    def servicefeaturemodel_Configuration33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Configuration__servicefeaturemodel_Configuration33", None)
        self.__servicefeaturemodel_Configuration33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_Attribute34"):
                    opp_val = getattr(item, "servicefeaturemodel_Attribute34", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_Attribute34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_Attribute34"):
                    opp_val = getattr(item, "servicefeaturemodel_Attribute34", None)
                    
                    setattr(item, "servicefeaturemodel_Attribute34", self)
                    

    @property
    def servicefeaturemodel_Configuration39(self):
        return self.__servicefeaturemodel_Configuration39

    @servicefeaturemodel_Configuration39.setter
    def servicefeaturemodel_Configuration39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Configuration__servicefeaturemodel_Configuration39", None)
        self.__servicefeaturemodel_Configuration39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_PossibleConfigurations38"):
                opp_val = getattr(old_value, "servicefeaturemodel_PossibleConfigurations38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_PossibleConfigurations38"):
                opp_val = getattr(value, "servicefeaturemodel_PossibleConfigurations38", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_PossibleConfigurations38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "servicefeaturemodel_ServiceFeature29"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature29", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_ServiceFeature29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_ServiceFeature29"):
                    opp_val = getattr(item, "servicefeaturemodel_ServiceFeature29", None)
                    
                    setattr(item, "servicefeaturemodel_ServiceFeature29", self)
                    

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class Variant:

    pass
class servicefeaturemodel_XOR(Variant):

    pass
class servicefeaturemodel_OR(Variant):

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

class servicefeaturemodel_Requires:

    pass
class servicefeaturemodel_ModifyRelationship(ABC):

    def __init__(self, name: str, orderNumber: int, function: str, targetParameterName: str, servicefeaturemodel_ModifyRelationship: "servicefeaturemodel_Attribute" = None):
        self.name = name
        self.orderNumber = orderNumber
        self.function = function
        self.targetParameterName = targetParameterName
        self.servicefeaturemodel_ModifyRelationship = servicefeaturemodel_ModifyRelationship
        
    @property
    def targetParameterName(self) -> str:
        return self.__targetParameterName

    @targetParameterName.setter
    def targetParameterName(self, targetParameterName: str):
        self.__targetParameterName = targetParameterName

    @property
    def orderNumber(self) -> int:
        return self.__orderNumber

    @orderNumber.setter
    def orderNumber(self, orderNumber: int):
        self.__orderNumber = orderNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def servicefeaturemodel_ModifyRelationship(self):
        return self.__servicefeaturemodel_ModifyRelationship

    @servicefeaturemodel_ModifyRelationship.setter
    def servicefeaturemodel_ModifyRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ModifyRelationship__servicefeaturemodel_ModifyRelationship", None)
        self.__servicefeaturemodel_ModifyRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Attribute18"):
                opp_val = getattr(old_value, "servicefeaturemodel_Attribute18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Attribute18"):
                opp_val = getattr(value, "servicefeaturemodel_Attribute18", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_Attribute18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class servicefeaturemodel_AttributeType:

    def __init__(self, name: str, domain: str, aggregationRule: str, scaleOrder: str, toBeEvaluated: bool, description: str, customAttributeTypePriority: int, requirement: str, servicefeaturemodel_AttributeType: "servicefeaturemodel_Attribute" = None, servicefeaturemodel_AttributeType42: "servicefeaturemodel_AttributeTypes" = None):
        self.name = name
        self.domain = domain
        self.aggregationRule = aggregationRule
        self.scaleOrder = scaleOrder
        self.toBeEvaluated = toBeEvaluated
        self.description = description
        self.customAttributeTypePriority = customAttributeTypePriority
        self.requirement = requirement
        self.servicefeaturemodel_AttributeType = servicefeaturemodel_AttributeType
        self.servicefeaturemodel_AttributeType42 = servicefeaturemodel_AttributeType42
        
    @property
    def customAttributeTypePriority(self) -> int:
        return self.__customAttributeTypePriority

    @customAttributeTypePriority.setter
    def customAttributeTypePriority(self, customAttributeTypePriority: int):
        self.__customAttributeTypePriority = customAttributeTypePriority

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def aggregationRule(self) -> str:
        return self.__aggregationRule

    @aggregationRule.setter
    def aggregationRule(self, aggregationRule: str):
        self.__aggregationRule = aggregationRule

    @property
    def requirement(self) -> str:
        return self.__requirement

    @requirement.setter
    def requirement(self, requirement: str):
        self.__requirement = requirement

    @property
    def toBeEvaluated(self) -> bool:
        return self.__toBeEvaluated

    @toBeEvaluated.setter
    def toBeEvaluated(self, toBeEvaluated: bool):
        self.__toBeEvaluated = toBeEvaluated

    @property
    def scaleOrder(self) -> str:
        return self.__scaleOrder

    @scaleOrder.setter
    def scaleOrder(self, scaleOrder: str):
        self.__scaleOrder = scaleOrder

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
    def servicefeaturemodel_AttributeType42(self):
        return self.__servicefeaturemodel_AttributeType42

    @servicefeaturemodel_AttributeType42.setter
    def servicefeaturemodel_AttributeType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_AttributeType__servicefeaturemodel_AttributeType42", None)
        self.__servicefeaturemodel_AttributeType42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_AttributeTypes41"):
                opp_val = getattr(old_value, "servicefeaturemodel_AttributeTypes41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_AttributeTypes41"):
                opp_val = getattr(value, "servicefeaturemodel_AttributeTypes41", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_AttributeTypes41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ServiceFeature:

    pass
class servicefeaturemodel_MandatoryServiceFeature(ServiceFeature):

    pass
class servicefeaturemodel_OptionalServiceFeature(ServiceFeature):

    pass
class servicefeaturemodel_Excludes:

    pass
class servicefeaturemodel_ServiceFeatureDiagram:

    def __init__(self, name: str, description: str, id: str, servicefeaturemodel_ServiceFeatureDiagram: "servicefeaturemodel_Service" = None, servicefeaturemodel_ServiceFeatureDiagram26: set["servicefeaturemodel_ServiceFeature"] = None):
        self.name = name
        self.description = description
        self.id = id
        self.servicefeaturemodel_ServiceFeatureDiagram = servicefeaturemodel_ServiceFeatureDiagram
        self.servicefeaturemodel_ServiceFeatureDiagram26 = servicefeaturemodel_ServiceFeatureDiagram26 if servicefeaturemodel_ServiceFeatureDiagram26 is not None else set()
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def servicefeaturemodel_ServiceFeatureDiagram26(self):
        return self.__servicefeaturemodel_ServiceFeatureDiagram26

    @servicefeaturemodel_ServiceFeatureDiagram26.setter
    def servicefeaturemodel_ServiceFeatureDiagram26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeatureDiagram__servicefeaturemodel_ServiceFeatureDiagram26", None)
        self.__servicefeaturemodel_ServiceFeatureDiagram26 = value if value is not None else set()
        
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
                    

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class servicefeaturemodel_Variant(ABC):

    pass
class servicefeaturemodel_Attribute:

    def __init__(self, instantiationValue: str, id: str, servicefeaturemodel_Attribute: "servicefeaturemodel_ServiceFeature" = None, servicefeaturemodel_Attribute16: "servicefeaturemodel_AttributeType" = None, servicefeaturemodel_Attribute18: set["servicefeaturemodel_ModifyRelationship"] = None, servicefeaturemodel_Attribute34: "servicefeaturemodel_Configuration" = None, servicefeaturemodel_Attribute44: "servicefeaturemodel_AttributeToAttributeModifyRelationship" = None):
        self.instantiationValue = instantiationValue
        self.id = id
        self.servicefeaturemodel_Attribute = servicefeaturemodel_Attribute
        self.servicefeaturemodel_Attribute16 = servicefeaturemodel_Attribute16
        self.servicefeaturemodel_Attribute18 = servicefeaturemodel_Attribute18 if servicefeaturemodel_Attribute18 is not None else set()
        self.servicefeaturemodel_Attribute34 = servicefeaturemodel_Attribute34
        self.servicefeaturemodel_Attribute44 = servicefeaturemodel_Attribute44
        
    @property
    def instantiationValue(self) -> str:
        return self.__instantiationValue

    @instantiationValue.setter
    def instantiationValue(self, instantiationValue: str):
        self.__instantiationValue = instantiationValue

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def servicefeaturemodel_Attribute44(self):
        return self.__servicefeaturemodel_Attribute44

    @servicefeaturemodel_Attribute44.setter
    def servicefeaturemodel_Attribute44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Attribute__servicefeaturemodel_Attribute44", None)
        self.__servicefeaturemodel_Attribute44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_AttributeToAttributeModifyRelationship"):
                opp_val = getattr(old_value, "servicefeaturemodel_AttributeToAttributeModifyRelationship", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_AttributeToAttributeModifyRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_AttributeToAttributeModifyRelationship"):
                opp_val = getattr(value, "servicefeaturemodel_AttributeToAttributeModifyRelationship", None)
                setattr(value, "servicefeaturemodel_AttributeToAttributeModifyRelationship", self)

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

    @property
    def servicefeaturemodel_Attribute18(self):
        return self.__servicefeaturemodel_Attribute18

    @servicefeaturemodel_Attribute18.setter
    def servicefeaturemodel_Attribute18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Attribute__servicefeaturemodel_Attribute18", None)
        self.__servicefeaturemodel_Attribute18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicefeaturemodel_ModifyRelationship"):
                    opp_val = getattr(item, "servicefeaturemodel_ModifyRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "servicefeaturemodel_ModifyRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicefeaturemodel_ModifyRelationship"):
                    opp_val = getattr(item, "servicefeaturemodel_ModifyRelationship", None)
                    
                    setattr(item, "servicefeaturemodel_ModifyRelationship", self)
                    

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
    def servicefeaturemodel_Attribute34(self):
        return self.__servicefeaturemodel_Attribute34

    @servicefeaturemodel_Attribute34.setter
    def servicefeaturemodel_Attribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Attribute__servicefeaturemodel_Attribute34", None)
        self.__servicefeaturemodel_Attribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Configuration33"):
                opp_val = getattr(old_value, "servicefeaturemodel_Configuration33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Configuration33"):
                opp_val = getattr(value, "servicefeaturemodel_Configuration33", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_Configuration33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class servicefeaturemodel_ServiceFeature(ABC):

    def __init__(self, name: str, description: str, minAmount: int, maxAmount: int, mapsToGSMElement: bool, associatedGSMElement: str, id: str, featureType: str, required: bool, servicefeaturemodel_ServiceFeature: set["servicefeaturemodel_Attribute"] = None, servicefeaturemodel_ServiceFeature7: "servicefeaturemodel_Variant" = None, servicefeaturemodel_ServiceFeature9: set["servicefeaturemodel_Requires"] = None, servicefeaturemodel_ServiceFeature11: set["servicefeaturemodel_Excludes"] = None, servicefeaturemodel_ServiceFeature14: "servicefeaturemodel_ServiceFeature" = None, servicefeaturemodel_ServiceFeature12: set["servicefeaturemodel_ServiceFeature"] = None, servicefeaturemodel_ServiceFeature21: "servicefeaturemodel_Requires" = None, servicefeaturemodel_ServiceFeature24: "servicefeaturemodel_Excludes" = None, servicefeaturemodel_ServiceFeature27: "servicefeaturemodel_ServiceFeatureDiagram" = None, servicefeaturemodel_ServiceFeature29: "servicefeaturemodel_Configuration" = None, servicefeaturemodel_ServiceFeature46: "servicefeaturemodel_FeatureToAttributeModifyRelationship" = None):
        self.name = name
        self.description = description
        self.minAmount = minAmount
        self.maxAmount = maxAmount
        self.mapsToGSMElement = mapsToGSMElement
        self.associatedGSMElement = associatedGSMElement
        self.id = id
        self.featureType = featureType
        self.required = required
        self.servicefeaturemodel_ServiceFeature = servicefeaturemodel_ServiceFeature if servicefeaturemodel_ServiceFeature is not None else set()
        self.servicefeaturemodel_ServiceFeature7 = servicefeaturemodel_ServiceFeature7
        self.servicefeaturemodel_ServiceFeature9 = servicefeaturemodel_ServiceFeature9 if servicefeaturemodel_ServiceFeature9 is not None else set()
        self.servicefeaturemodel_ServiceFeature11 = servicefeaturemodel_ServiceFeature11 if servicefeaturemodel_ServiceFeature11 is not None else set()
        self.servicefeaturemodel_ServiceFeature14 = servicefeaturemodel_ServiceFeature14
        self.servicefeaturemodel_ServiceFeature12 = servicefeaturemodel_ServiceFeature12 if servicefeaturemodel_ServiceFeature12 is not None else set()
        self.servicefeaturemodel_ServiceFeature21 = servicefeaturemodel_ServiceFeature21
        self.servicefeaturemodel_ServiceFeature24 = servicefeaturemodel_ServiceFeature24
        self.servicefeaturemodel_ServiceFeature27 = servicefeaturemodel_ServiceFeature27
        self.servicefeaturemodel_ServiceFeature29 = servicefeaturemodel_ServiceFeature29
        self.servicefeaturemodel_ServiceFeature46 = servicefeaturemodel_ServiceFeature46
        
    @property
    def minAmount(self) -> int:
        return self.__minAmount

    @minAmount.setter
    def minAmount(self, minAmount: int):
        self.__minAmount = minAmount

    @property
    def maxAmount(self) -> int:
        return self.__maxAmount

    @maxAmount.setter
    def maxAmount(self, maxAmount: int):
        self.__maxAmount = maxAmount

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def associatedGSMElement(self) -> str:
        return self.__associatedGSMElement

    @associatedGSMElement.setter
    def associatedGSMElement(self, associatedGSMElement: str):
        self.__associatedGSMElement = associatedGSMElement

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mapsToGSMElement(self) -> bool:
        return self.__mapsToGSMElement

    @mapsToGSMElement.setter
    def mapsToGSMElement(self, mapsToGSMElement: bool):
        self.__mapsToGSMElement = mapsToGSMElement

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def featureType(self) -> str:
        return self.__featureType

    @featureType.setter
    def featureType(self, featureType: str):
        self.__featureType = featureType

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def servicefeaturemodel_ServiceFeature29(self):
        return self.__servicefeaturemodel_ServiceFeature29

    @servicefeaturemodel_ServiceFeature29.setter
    def servicefeaturemodel_ServiceFeature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature29", None)
        self.__servicefeaturemodel_ServiceFeature29 = value
        
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
    def servicefeaturemodel_ServiceFeature24(self):
        return self.__servicefeaturemodel_ServiceFeature24

    @servicefeaturemodel_ServiceFeature24.setter
    def servicefeaturemodel_ServiceFeature24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature24", None)
        self.__servicefeaturemodel_ServiceFeature24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Excludes23"):
                opp_val = getattr(old_value, "servicefeaturemodel_Excludes23", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Excludes23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Excludes23"):
                opp_val = getattr(value, "servicefeaturemodel_Excludes23", None)
                setattr(value, "servicefeaturemodel_Excludes23", self)

    @property
    def servicefeaturemodel_ServiceFeature46(self):
        return self.__servicefeaturemodel_ServiceFeature46

    @servicefeaturemodel_ServiceFeature46.setter
    def servicefeaturemodel_ServiceFeature46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature46", None)
        self.__servicefeaturemodel_ServiceFeature46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_FeatureToAttributeModifyRelationship"):
                opp_val = getattr(old_value, "servicefeaturemodel_FeatureToAttributeModifyRelationship", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_FeatureToAttributeModifyRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_FeatureToAttributeModifyRelationship"):
                opp_val = getattr(value, "servicefeaturemodel_FeatureToAttributeModifyRelationship", None)
                setattr(value, "servicefeaturemodel_FeatureToAttributeModifyRelationship", self)

    @property
    def servicefeaturemodel_ServiceFeature21(self):
        return self.__servicefeaturemodel_ServiceFeature21

    @servicefeaturemodel_ServiceFeature21.setter
    def servicefeaturemodel_ServiceFeature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature21", None)
        self.__servicefeaturemodel_ServiceFeature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_Requires20"):
                opp_val = getattr(old_value, "servicefeaturemodel_Requires20", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Requires20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Requires20"):
                opp_val = getattr(value, "servicefeaturemodel_Requires20", None)
                setattr(value, "servicefeaturemodel_Requires20", self)

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
    def servicefeaturemodel_ServiceFeature27(self):
        return self.__servicefeaturemodel_ServiceFeature27

    @servicefeaturemodel_ServiceFeature27.setter
    def servicefeaturemodel_ServiceFeature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_ServiceFeature__servicefeaturemodel_ServiceFeature27", None)
        self.__servicefeaturemodel_ServiceFeature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram26"):
                opp_val = getattr(old_value, "servicefeaturemodel_ServiceFeatureDiagram26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_ServiceFeatureDiagram26"):
                opp_val = getattr(value, "servicefeaturemodel_ServiceFeatureDiagram26", None)
                if opp_val is None:
                    setattr(value, "servicefeaturemodel_ServiceFeatureDiagram26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "servicefeaturemodel_Variant"):
                opp_val = getattr(old_value, "servicefeaturemodel_Variant", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_Variant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_Variant"):
                opp_val = getattr(value, "servicefeaturemodel_Variant", None)
                setattr(value, "servicefeaturemodel_Variant", self)

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
                    

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class servicefeaturemodel_AttributeTypes:

    pass
class servicefeaturemodel_PossibleConfigurations:

    pass
class servicefeaturemodel_Service:

    def __init__(self, description: str, id: str, name: str, servicefeaturemodel_Service: "servicefeaturemodel_ServiceFeatureDiagram" = None, servicefeaturemodel_Service2: "servicefeaturemodel_PossibleConfigurations" = None, servicefeaturemodel_Service4: "servicefeaturemodel_AttributeTypes" = None):
        self.description = description
        self.id = id
        self.name = name
        self.servicefeaturemodel_Service = servicefeaturemodel_Service
        self.servicefeaturemodel_Service2 = servicefeaturemodel_Service2
        self.servicefeaturemodel_Service4 = servicefeaturemodel_Service4
        
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
    def servicefeaturemodel_Service2(self):
        return self.__servicefeaturemodel_Service2

    @servicefeaturemodel_Service2.setter
    def servicefeaturemodel_Service2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_servicefeaturemodel_Service__servicefeaturemodel_Service2", None)
        self.__servicefeaturemodel_Service2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicefeaturemodel_PossibleConfigurations"):
                opp_val = getattr(old_value, "servicefeaturemodel_PossibleConfigurations", None)
                if opp_val == self:
                    setattr(old_value, "servicefeaturemodel_PossibleConfigurations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicefeaturemodel_PossibleConfigurations"):
                opp_val = getattr(value, "servicefeaturemodel_PossibleConfigurations", None)
                setattr(value, "servicefeaturemodel_PossibleConfigurations", self)

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
