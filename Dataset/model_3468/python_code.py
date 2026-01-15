from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariabilityType(Enum):
    mandatory = "mandatory"
    optional = "optional"
    alternative = "alternative"
    or = "or"


############################################
# Definition of Classes
############################################

class featuremodel_EObject:

    pass
class AttributeValue:

    pass
class featuremodel_AttributeValueBoolean(AttributeValue):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class featuremodel_AttributeValueEObject(AttributeValue):

    pass
class featuremodel_AttributeValueString(AttributeValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class featuremodel_AttributeValueInt(AttributeValue):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class AttributeType:

    pass
class featuremodel_AttributeTypeBoolean(AttributeType):

    pass
class featuremodel_AttributeTypeString(AttributeType):

    pass
class featuremodel_AttributeTypeEObject(AttributeType):

    pass
class featuremodel_AttributeTypeInt(AttributeType):

    pass
class featuremodel_AttributeType(ABC):

    pass
class featuremodel_AttributeValue(ABC):

    pass
class featuremodel_Group:

    def __init__(self, id: str, lower: int, upper: int, featuremodel_Group: set["featuremodel_Feature"] = None, featuremodel_Group20: "featuremodel_Feature" = None):
        self.id = id
        self.lower = lower
        self.upper = upper
        self.featuremodel_Group = featuremodel_Group if featuremodel_Group is not None else set()
        self.featuremodel_Group20 = featuremodel_Group20
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def featuremodel_Group(self):
        return self.__featuremodel_Group

    @featuremodel_Group.setter
    def featuremodel_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Group__featuremodel_Group", None)
        self.__featuremodel_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodel_Feature11"):
                    opp_val = getattr(item, "featuremodel_Feature11", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodel_Feature11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodel_Feature11"):
                    opp_val = getattr(item, "featuremodel_Feature11", None)
                    
                    setattr(item, "featuremodel_Feature11", self)
                    

    @property
    def featuremodel_Group20(self):
        return self.__featuremodel_Group20

    @featuremodel_Group20.setter
    def featuremodel_Group20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Group__featuremodel_Group20", None)
        self.__featuremodel_Group20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Feature19"):
                opp_val = getattr(old_value, "featuremodel_Feature19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Feature19"):
                opp_val = getattr(value, "featuremodel_Feature19", None)
                if opp_val is None:
                    setattr(value, "featuremodel_Feature19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Rule:

    pass
class featuremodel_Constraint(Rule):

    def __init__(self, id: str, featuremodel_Constraint: "featuremodel_FeatureModel" = None, featuremodel_Constraint8: "featuremodel_Description" = None):
        self.id = id
        self.featuremodel_Constraint = featuremodel_Constraint
        self.featuremodel_Constraint8 = featuremodel_Constraint8
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def featuremodel_Constraint8(self):
        return self.__featuremodel_Constraint8

    @featuremodel_Constraint8.setter
    def featuremodel_Constraint8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Constraint__featuremodel_Constraint8", None)
        self.__featuremodel_Constraint8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Description9"):
                opp_val = getattr(old_value, "featuremodel_Description9", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Description9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Description9"):
                opp_val = getattr(value, "featuremodel_Description9", None)
                setattr(value, "featuremodel_Description9", self)

    @property
    def featuremodel_Constraint(self):
        return self.__featuremodel_Constraint

    @featuremodel_Constraint.setter
    def featuremodel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Constraint__featuremodel_Constraint", None)
        self.__featuremodel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_FeatureModel6"):
                opp_val = getattr(old_value, "featuremodel_FeatureModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_FeatureModel6"):
                opp_val = getattr(value, "featuremodel_FeatureModel6", None)
                if opp_val is None:
                    setattr(value, "featuremodel_FeatureModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getModel(self) -> str:
        # TODO: Implement getModel method
        pass

class featuremodel_Feature:

    def __init__(self, id: str, name: str, type: str, featuremodel_Feature: "featuremodel_FeatureModel" = None, featuremodel_Feature11: "featuremodel_Group" = None, featuremodel_Feature13: "featuremodel_Description" = None, featuremodel_Feature16: set["featuremodel_Attribute"] = None, featuremodel_Feature19: set["featuremodel_Group"] = None):
        self.id = id
        self.name = name
        self.type = type
        self.featuremodel_Feature = featuremodel_Feature
        self.featuremodel_Feature11 = featuremodel_Feature11
        self.featuremodel_Feature13 = featuremodel_Feature13
        self.featuremodel_Feature16 = featuremodel_Feature16 if featuremodel_Feature16 is not None else set()
        self.featuremodel_Feature19 = featuremodel_Feature19 if featuremodel_Feature19 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featuremodel_Feature16(self):
        return self.__featuremodel_Feature16

    @featuremodel_Feature16.setter
    def featuremodel_Feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Feature__featuremodel_Feature16", None)
        self.__featuremodel_Feature16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodel_Attribute17"):
                    opp_val = getattr(item, "featuremodel_Attribute17", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodel_Attribute17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodel_Attribute17"):
                    opp_val = getattr(item, "featuremodel_Attribute17", None)
                    
                    setattr(item, "featuremodel_Attribute17", self)
                    

    @property
    def featuremodel_Feature(self):
        return self.__featuremodel_Feature

    @featuremodel_Feature.setter
    def featuremodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Feature__featuremodel_Feature", None)
        self.__featuremodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_FeatureModel4"):
                opp_val = getattr(old_value, "featuremodel_FeatureModel4", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_FeatureModel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_FeatureModel4"):
                opp_val = getattr(value, "featuremodel_FeatureModel4", None)
                setattr(value, "featuremodel_FeatureModel4", self)

    @property
    def featuremodel_Feature19(self):
        return self.__featuremodel_Feature19

    @featuremodel_Feature19.setter
    def featuremodel_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Feature__featuremodel_Feature19", None)
        self.__featuremodel_Feature19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodel_Group20"):
                    opp_val = getattr(item, "featuremodel_Group20", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodel_Group20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodel_Group20"):
                    opp_val = getattr(item, "featuremodel_Group20", None)
                    
                    setattr(item, "featuremodel_Group20", self)
                    

    @property
    def featuremodel_Feature11(self):
        return self.__featuremodel_Feature11

    @featuremodel_Feature11.setter
    def featuremodel_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Feature__featuremodel_Feature11", None)
        self.__featuremodel_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Group"):
                opp_val = getattr(old_value, "featuremodel_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Group"):
                opp_val = getattr(value, "featuremodel_Group", None)
                if opp_val is None:
                    setattr(value, "featuremodel_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuremodel_Feature13(self):
        return self.__featuremodel_Feature13

    @featuremodel_Feature13.setter
    def featuremodel_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Feature__featuremodel_Feature13", None)
        self.__featuremodel_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Description14"):
                opp_val = getattr(old_value, "featuremodel_Description14", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Description14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Description14"):
                opp_val = getattr(value, "featuremodel_Description14", None)
                setattr(value, "featuremodel_Description14", self)

    def getModel(self) -> str:
        # TODO: Implement getModel method
        pass

    def getParentGroup(self) -> str:
        # TODO: Implement getParentGroup method
        pass

    def getVariabilityType(self) -> str:
        # TODO: Implement getVariabilityType method
        pass

    def getParent(self) -> str:
        # TODO: Implement getParent method
        pass

class featuremodel_Attribute:

    def __init__(self, id: str, name: str, setable: bool, featuremodel_Attribute: "featuremodel_FeatureModel" = None, featuremodel_Attribute17: "featuremodel_Feature" = None, featuremodel_Attribute22: "featuremodel_Description" = None, featuremodel_Attribute25: "featuremodel_AttributeValue" = None, featuremodel_Attribute27: "featuremodel_AttributeType" = None):
        self.id = id
        self.name = name
        self.setable = setable
        self.featuremodel_Attribute = featuremodel_Attribute
        self.featuremodel_Attribute17 = featuremodel_Attribute17
        self.featuremodel_Attribute22 = featuremodel_Attribute22
        self.featuremodel_Attribute25 = featuremodel_Attribute25
        self.featuremodel_Attribute27 = featuremodel_Attribute27
        
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
    def setable(self) -> bool:
        return self.__setable

    @setable.setter
    def setable(self, setable: bool):
        self.__setable = setable

    @property
    def featuremodel_Attribute27(self):
        return self.__featuremodel_Attribute27

    @featuremodel_Attribute27.setter
    def featuremodel_Attribute27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Attribute__featuremodel_Attribute27", None)
        self.__featuremodel_Attribute27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_AttributeType"):
                opp_val = getattr(old_value, "featuremodel_AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_AttributeType"):
                opp_val = getattr(value, "featuremodel_AttributeType", None)
                setattr(value, "featuremodel_AttributeType", self)

    @property
    def featuremodel_Attribute25(self):
        return self.__featuremodel_Attribute25

    @featuremodel_Attribute25.setter
    def featuremodel_Attribute25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Attribute__featuremodel_Attribute25", None)
        self.__featuremodel_Attribute25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_AttributeValue"):
                opp_val = getattr(old_value, "featuremodel_AttributeValue", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_AttributeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_AttributeValue"):
                opp_val = getattr(value, "featuremodel_AttributeValue", None)
                setattr(value, "featuremodel_AttributeValue", self)

    @property
    def featuremodel_Attribute17(self):
        return self.__featuremodel_Attribute17

    @featuremodel_Attribute17.setter
    def featuremodel_Attribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Attribute__featuremodel_Attribute17", None)
        self.__featuremodel_Attribute17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Feature16"):
                opp_val = getattr(old_value, "featuremodel_Feature16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Feature16"):
                opp_val = getattr(value, "featuremodel_Feature16", None)
                if opp_val is None:
                    setattr(value, "featuremodel_Feature16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuremodel_Attribute22(self):
        return self.__featuremodel_Attribute22

    @featuremodel_Attribute22.setter
    def featuremodel_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Attribute__featuremodel_Attribute22", None)
        self.__featuremodel_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Description23"):
                opp_val = getattr(old_value, "featuremodel_Description23", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Description23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Description23"):
                opp_val = getattr(value, "featuremodel_Description23", None)
                setattr(value, "featuremodel_Description23", self)

    @property
    def featuremodel_Attribute(self):
        return self.__featuremodel_Attribute

    @featuremodel_Attribute.setter
    def featuremodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Attribute__featuremodel_Attribute", None)
        self.__featuremodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_FeatureModel2"):
                opp_val = getattr(old_value, "featuremodel_FeatureModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_FeatureModel2"):
                opp_val = getattr(value, "featuremodel_FeatureModel2", None)
                if opp_val is None:
                    setattr(value, "featuremodel_FeatureModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featuremodel_Description:

    def __init__(self, id: str, text: str, featuremodel_Description: "featuremodel_FeatureModel" = None, featuremodel_Description9: "featuremodel_Constraint" = None, featuremodel_Description14: "featuremodel_Feature" = None, featuremodel_Description23: "featuremodel_Attribute" = None):
        self.id = id
        self.text = text
        self.featuremodel_Description = featuremodel_Description
        self.featuremodel_Description9 = featuremodel_Description9
        self.featuremodel_Description14 = featuremodel_Description14
        self.featuremodel_Description23 = featuremodel_Description23
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def featuremodel_Description23(self):
        return self.__featuremodel_Description23

    @featuremodel_Description23.setter
    def featuremodel_Description23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Description__featuremodel_Description23", None)
        self.__featuremodel_Description23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Attribute22"):
                opp_val = getattr(old_value, "featuremodel_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Attribute22"):
                opp_val = getattr(value, "featuremodel_Attribute22", None)
                setattr(value, "featuremodel_Attribute22", self)

    @property
    def featuremodel_Description14(self):
        return self.__featuremodel_Description14

    @featuremodel_Description14.setter
    def featuremodel_Description14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Description__featuremodel_Description14", None)
        self.__featuremodel_Description14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Feature13"):
                opp_val = getattr(old_value, "featuremodel_Feature13", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Feature13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Feature13"):
                opp_val = getattr(value, "featuremodel_Feature13", None)
                setattr(value, "featuremodel_Feature13", self)

    @property
    def featuremodel_Description(self):
        return self.__featuremodel_Description

    @featuremodel_Description.setter
    def featuremodel_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Description__featuremodel_Description", None)
        self.__featuremodel_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_FeatureModel"):
                opp_val = getattr(old_value, "featuremodel_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_FeatureModel"):
                opp_val = getattr(value, "featuremodel_FeatureModel", None)
                setattr(value, "featuremodel_FeatureModel", self)

    @property
    def featuremodel_Description9(self):
        return self.__featuremodel_Description9

    @featuremodel_Description9.setter
    def featuremodel_Description9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_Description__featuremodel_Description9", None)
        self.__featuremodel_Description9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Constraint8"):
                opp_val = getattr(old_value, "featuremodel_Constraint8", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Constraint8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Constraint8"):
                opp_val = getattr(value, "featuremodel_Constraint8", None)
                setattr(value, "featuremodel_Constraint8", self)

class featuremodel_FeatureModel:

    def __init__(self, id: str, version: str, featuremodel_FeatureModel: "featuremodel_Description" = None, featuremodel_FeatureModel2: set["featuremodel_Attribute"] = None, featuremodel_FeatureModel4: "featuremodel_Feature" = None, featuremodel_FeatureModel6: set["featuremodel_Constraint"] = None):
        self.id = id
        self.version = version
        self.featuremodel_FeatureModel = featuremodel_FeatureModel
        self.featuremodel_FeatureModel2 = featuremodel_FeatureModel2 if featuremodel_FeatureModel2 is not None else set()
        self.featuremodel_FeatureModel4 = featuremodel_FeatureModel4
        self.featuremodel_FeatureModel6 = featuremodel_FeatureModel6 if featuremodel_FeatureModel6 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def featuremodel_FeatureModel2(self):
        return self.__featuremodel_FeatureModel2

    @featuremodel_FeatureModel2.setter
    def featuremodel_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_FeatureModel__featuremodel_FeatureModel2", None)
        self.__featuremodel_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodel_Attribute"):
                    opp_val = getattr(item, "featuremodel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodel_Attribute"):
                    opp_val = getattr(item, "featuremodel_Attribute", None)
                    
                    setattr(item, "featuremodel_Attribute", self)
                    

    @property
    def featuremodel_FeatureModel6(self):
        return self.__featuremodel_FeatureModel6

    @featuremodel_FeatureModel6.setter
    def featuremodel_FeatureModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_FeatureModel__featuremodel_FeatureModel6", None)
        self.__featuremodel_FeatureModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodel_Constraint"):
                    opp_val = getattr(item, "featuremodel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodel_Constraint"):
                    opp_val = getattr(item, "featuremodel_Constraint", None)
                    
                    setattr(item, "featuremodel_Constraint", self)
                    

    @property
    def featuremodel_FeatureModel(self):
        return self.__featuremodel_FeatureModel

    @featuremodel_FeatureModel.setter
    def featuremodel_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_FeatureModel__featuremodel_FeatureModel", None)
        self.__featuremodel_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Description"):
                opp_val = getattr(old_value, "featuremodel_Description", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Description"):
                opp_val = getattr(value, "featuremodel_Description", None)
                setattr(value, "featuremodel_Description", self)

    @property
    def featuremodel_FeatureModel4(self):
        return self.__featuremodel_FeatureModel4

    @featuremodel_FeatureModel4.setter
    def featuremodel_FeatureModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodel_FeatureModel__featuremodel_FeatureModel4", None)
        self.__featuremodel_FeatureModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodel_Feature"):
                opp_val = getattr(old_value, "featuremodel_Feature", None)
                if opp_val == self:
                    setattr(old_value, "featuremodel_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodel_Feature"):
                opp_val = getattr(value, "featuremodel_Feature", None)
                setattr(value, "featuremodel_Feature", self)

class featuremodel_Rule:

    def __init__(self, language: str, code: str):
        self.language = language
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language
