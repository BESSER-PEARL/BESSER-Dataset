from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FeatureType(Enum):
    OPTIONAL = "OPTIONAL"
    MANDATORY = "MANDATORY"
    SIMPLE = "SIMPLE"
class ValueType(Enum):
    FEATURE = "FEATURE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    NONE = "NONE"
    STRING = "STRING"
class ConfigState(Enum):
    UNDECIDED = "UNDECIDED"
    USER_SELECTED = "USER_SELECTED"
    USER_ELIMINATED = "USER_ELIMINATED"
class FeatureGroupType(Enum):
    XORGROUP = "XORGROUP"
    ORGROUP = "ORGROUP"
    SIMPLEGROUP = "SIMPLEGROUP"


############################################
# Definition of Classes
############################################

class Relation:

    pass
class specializationModel_RelationFeature(Relation):

    def __init__(self, lowerBound: int, upperBound: int, type: str, specializationModel_RelationFeature: "specializationModel_Feature" = None, specializationModel_RelationFeature29: "specializationModel_Feature" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.specializationModel_RelationFeature = specializationModel_RelationFeature
        self.specializationModel_RelationFeature29 = specializationModel_RelationFeature29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def specializationModel_RelationFeature(self):
        return self.__specializationModel_RelationFeature

    @specializationModel_RelationFeature.setter
    def specializationModel_RelationFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_RelationFeature__specializationModel_RelationFeature", None)
        self.__specializationModel_RelationFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature27"):
                opp_val = getattr(old_value, "specializationModel_Feature27", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_Feature27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature27"):
                opp_val = getattr(value, "specializationModel_Feature27", None)
                setattr(value, "specializationModel_Feature27", self)

    @property
    def specializationModel_RelationFeature29(self):
        return self.__specializationModel_RelationFeature29

    @specializationModel_RelationFeature29.setter
    def specializationModel_RelationFeature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_RelationFeature__specializationModel_RelationFeature29", None)
        self.__specializationModel_RelationFeature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature30"):
                opp_val = getattr(old_value, "specializationModel_Feature30", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_Feature30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature30"):
                opp_val = getattr(value, "specializationModel_Feature30", None)
                setattr(value, "specializationModel_Feature30", self)

class specializationModel_RelationFG(Relation):

    pass
class specializationModel_Node:

    pass
class specializationModel_TypedValue:

    def __init__(self, integerValue: str, stringValue: str, floatValue: str, specializationModel_TypedValue: "specializationModel_Feature" = None, specializationModel_TypedValue10: "specializationModel_Feature" = None):
        self.integerValue = integerValue
        self.stringValue = stringValue
        self.floatValue = floatValue
        self.specializationModel_TypedValue = specializationModel_TypedValue
        self.specializationModel_TypedValue10 = specializationModel_TypedValue10
        
    @property
    def floatValue(self) -> str:
        return self.__floatValue

    @floatValue.setter
    def floatValue(self, floatValue: str):
        self.__floatValue = floatValue

    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

    @property
    def integerValue(self) -> str:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue

    @property
    def specializationModel_TypedValue(self):
        return self.__specializationModel_TypedValue

    @specializationModel_TypedValue.setter
    def specializationModel_TypedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_TypedValue__specializationModel_TypedValue", None)
        self.__specializationModel_TypedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature"):
                opp_val = getattr(old_value, "specializationModel_Feature", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature"):
                opp_val = getattr(value, "specializationModel_Feature", None)
                setattr(value, "specializationModel_Feature", self)

    @property
    def specializationModel_TypedValue10(self):
        return self.__specializationModel_TypedValue10

    @specializationModel_TypedValue10.setter
    def specializationModel_TypedValue10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_TypedValue__specializationModel_TypedValue10", None)
        self.__specializationModel_TypedValue10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature11"):
                opp_val = getattr(old_value, "specializationModel_Feature11", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_Feature11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature11"):
                opp_val = getattr(value, "specializationModel_Feature11", None)
                setattr(value, "specializationModel_Feature11", self)

class Node:

    pass
class specializationModel_Feature(Node):

    def __init__(self, name: str, valueType: str, state: str, realName: str, specializationModel_Feature: "specializationModel_TypedValue" = None, specializationModel_Feature3: "specializationModel_Feature" = None, specializationModel_Feature1: "specializationModel_Feature" = None, specializationModel_Feature5: set["specializationModel_Node"] = None, specializationModel_Feature8: "specializationModel_Feature" = None, specializationModel_Feature6: set["specializationModel_Feature"] = None, specializationModel_Feature11: "specializationModel_TypedValue" = None, specializationModel_Feature17: "specializationModel_FeatureGroup" = None, specializationModel_Feature27: "specializationModel_RelationFeature" = None, specializationModel_Feature30: "specializationModel_RelationFeature" = None):
        self.name = name
        self.valueType = valueType
        self.state = state
        self.realName = realName
        self.specializationModel_Feature = specializationModel_Feature
        self.specializationModel_Feature3 = specializationModel_Feature3
        self.specializationModel_Feature1 = specializationModel_Feature1
        self.specializationModel_Feature5 = specializationModel_Feature5 if specializationModel_Feature5 is not None else set()
        self.specializationModel_Feature8 = specializationModel_Feature8
        self.specializationModel_Feature6 = specializationModel_Feature6 if specializationModel_Feature6 is not None else set()
        self.specializationModel_Feature11 = specializationModel_Feature11
        self.specializationModel_Feature17 = specializationModel_Feature17
        self.specializationModel_Feature27 = specializationModel_Feature27
        self.specializationModel_Feature30 = specializationModel_Feature30
        
    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def realName(self) -> str:
        return self.__realName

    @realName.setter
    def realName(self, realName: str):
        self.__realName = realName

    @property
    def specializationModel_Feature11(self):
        return self.__specializationModel_Feature11

    @specializationModel_Feature11.setter
    def specializationModel_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature11", None)
        self.__specializationModel_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_TypedValue10"):
                opp_val = getattr(old_value, "specializationModel_TypedValue10", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_TypedValue10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_TypedValue10"):
                opp_val = getattr(value, "specializationModel_TypedValue10", None)
                setattr(value, "specializationModel_TypedValue10", self)

    @property
    def specializationModel_Feature30(self):
        return self.__specializationModel_Feature30

    @specializationModel_Feature30.setter
    def specializationModel_Feature30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature30", None)
        self.__specializationModel_Feature30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_RelationFeature29"):
                opp_val = getattr(old_value, "specializationModel_RelationFeature29", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_RelationFeature29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_RelationFeature29"):
                opp_val = getattr(value, "specializationModel_RelationFeature29", None)
                setattr(value, "specializationModel_RelationFeature29", self)

    @property
    def specializationModel_Feature17(self):
        return self.__specializationModel_Feature17

    @specializationModel_Feature17.setter
    def specializationModel_Feature17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature17", None)
        self.__specializationModel_Feature17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_FeatureGroup"):
                opp_val = getattr(old_value, "specializationModel_FeatureGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_FeatureGroup"):
                opp_val = getattr(value, "specializationModel_FeatureGroup", None)
                if opp_val is None:
                    setattr(value, "specializationModel_FeatureGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specializationModel_Feature3(self):
        return self.__specializationModel_Feature3

    @specializationModel_Feature3.setter
    def specializationModel_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature3", None)
        self.__specializationModel_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature1"):
                opp_val = getattr(old_value, "specializationModel_Feature1", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_Feature1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature1"):
                opp_val = getattr(value, "specializationModel_Feature1", None)
                setattr(value, "specializationModel_Feature1", self)

    @property
    def specializationModel_Feature1(self):
        return self.__specializationModel_Feature1

    @specializationModel_Feature1.setter
    def specializationModel_Feature1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature1", None)
        self.__specializationModel_Feature1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature3"):
                opp_val = getattr(old_value, "specializationModel_Feature3", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_Feature3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature3"):
                opp_val = getattr(value, "specializationModel_Feature3", None)
                setattr(value, "specializationModel_Feature3", self)

    @property
    def specializationModel_Feature5(self):
        return self.__specializationModel_Feature5

    @specializationModel_Feature5.setter
    def specializationModel_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature5", None)
        self.__specializationModel_Feature5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "specializationModel_Node"):
                    opp_val = getattr(item, "specializationModel_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "specializationModel_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "specializationModel_Node"):
                    opp_val = getattr(item, "specializationModel_Node", None)
                    
                    setattr(item, "specializationModel_Node", self)
                    

    @property
    def specializationModel_Feature27(self):
        return self.__specializationModel_Feature27

    @specializationModel_Feature27.setter
    def specializationModel_Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature27", None)
        self.__specializationModel_Feature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_RelationFeature"):
                opp_val = getattr(old_value, "specializationModel_RelationFeature", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_RelationFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_RelationFeature"):
                opp_val = getattr(value, "specializationModel_RelationFeature", None)
                setattr(value, "specializationModel_RelationFeature", self)

    @property
    def specializationModel_Feature8(self):
        return self.__specializationModel_Feature8

    @specializationModel_Feature8.setter
    def specializationModel_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature8", None)
        self.__specializationModel_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_Feature6"):
                opp_val = getattr(old_value, "specializationModel_Feature6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_Feature6"):
                opp_val = getattr(value, "specializationModel_Feature6", None)
                if opp_val is None:
                    setattr(value, "specializationModel_Feature6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specializationModel_Feature6(self):
        return self.__specializationModel_Feature6

    @specializationModel_Feature6.setter
    def specializationModel_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature6", None)
        self.__specializationModel_Feature6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "specializationModel_Feature8"):
                    opp_val = getattr(item, "specializationModel_Feature8", None)
                    
                    if opp_val == self:
                        setattr(item, "specializationModel_Feature8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "specializationModel_Feature8"):
                    opp_val = getattr(item, "specializationModel_Feature8", None)
                    
                    setattr(item, "specializationModel_Feature8", self)
                    

    @property
    def specializationModel_Feature(self):
        return self.__specializationModel_Feature

    @specializationModel_Feature.setter
    def specializationModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Feature__specializationModel_Feature", None)
        self.__specializationModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializationModel_TypedValue"):
                opp_val = getattr(old_value, "specializationModel_TypedValue", None)
                if opp_val == self:
                    setattr(old_value, "specializationModel_TypedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializationModel_TypedValue"):
                opp_val = getattr(value, "specializationModel_TypedValue", None)
                setattr(value, "specializationModel_TypedValue", self)

class specializationModel_FeatureGroup(Node):

    def __init__(self, lowerBound: int, upperBound: int, type: str, specializationModel_FeatureGroup: set["specializationModel_Feature"] = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.specializationModel_FeatureGroup = specializationModel_FeatureGroup if specializationModel_FeatureGroup is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def specializationModel_FeatureGroup(self):
        return self.__specializationModel_FeatureGroup

    @specializationModel_FeatureGroup.setter
    def specializationModel_FeatureGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_FeatureGroup__specializationModel_FeatureGroup", None)
        self.__specializationModel_FeatureGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "specializationModel_Feature17"):
                    opp_val = getattr(item, "specializationModel_Feature17", None)
                    
                    if opp_val == self:
                        setattr(item, "specializationModel_Feature17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "specializationModel_Feature17"):
                    opp_val = getattr(item, "specializationModel_Feature17", None)
                    
                    setattr(item, "specializationModel_Feature17", self)
                    

class specializationModel_Relation:

    pass
class specializationModel_Project:

    def __init__(self, featureModelURI: str, nameConstraintsFile: str, nameConfigFile: str, numberOfProducts: int, infiniteDomain: bool, userConstraintsState: bool, specializationModel_Project: set["specializationModel_Node"] = None, specializationModel_Project15: set["specializationModel_Relation"] = None):
        self.featureModelURI = featureModelURI
        self.nameConstraintsFile = nameConstraintsFile
        self.nameConfigFile = nameConfigFile
        self.numberOfProducts = numberOfProducts
        self.infiniteDomain = infiniteDomain
        self.userConstraintsState = userConstraintsState
        self.specializationModel_Project = specializationModel_Project if specializationModel_Project is not None else set()
        self.specializationModel_Project15 = specializationModel_Project15 if specializationModel_Project15 is not None else set()
        
    @property
    def nameConfigFile(self) -> str:
        return self.__nameConfigFile

    @nameConfigFile.setter
    def nameConfigFile(self, nameConfigFile: str):
        self.__nameConfigFile = nameConfigFile

    @property
    def featureModelURI(self) -> str:
        return self.__featureModelURI

    @featureModelURI.setter
    def featureModelURI(self, featureModelURI: str):
        self.__featureModelURI = featureModelURI

    @property
    def userConstraintsState(self) -> bool:
        return self.__userConstraintsState

    @userConstraintsState.setter
    def userConstraintsState(self, userConstraintsState: bool):
        self.__userConstraintsState = userConstraintsState

    @property
    def nameConstraintsFile(self) -> str:
        return self.__nameConstraintsFile

    @nameConstraintsFile.setter
    def nameConstraintsFile(self, nameConstraintsFile: str):
        self.__nameConstraintsFile = nameConstraintsFile

    @property
    def infiniteDomain(self) -> bool:
        return self.__infiniteDomain

    @infiniteDomain.setter
    def infiniteDomain(self, infiniteDomain: bool):
        self.__infiniteDomain = infiniteDomain

    @property
    def numberOfProducts(self) -> int:
        return self.__numberOfProducts

    @numberOfProducts.setter
    def numberOfProducts(self, numberOfProducts: int):
        self.__numberOfProducts = numberOfProducts

    @property
    def specializationModel_Project(self):
        return self.__specializationModel_Project

    @specializationModel_Project.setter
    def specializationModel_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Project__specializationModel_Project", None)
        self.__specializationModel_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "specializationModel_Node13"):
                    opp_val = getattr(item, "specializationModel_Node13", None)
                    
                    if opp_val == self:
                        setattr(item, "specializationModel_Node13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "specializationModel_Node13"):
                    opp_val = getattr(item, "specializationModel_Node13", None)
                    
                    setattr(item, "specializationModel_Node13", self)
                    

    @property
    def specializationModel_Project15(self):
        return self.__specializationModel_Project15

    @specializationModel_Project15.setter
    def specializationModel_Project15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_specializationModel_Project__specializationModel_Project15", None)
        self.__specializationModel_Project15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "specializationModel_Relation"):
                    opp_val = getattr(item, "specializationModel_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "specializationModel_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "specializationModel_Relation"):
                    opp_val = getattr(item, "specializationModel_Relation", None)
                    
                    setattr(item, "specializationModel_Relation", self)
                    
