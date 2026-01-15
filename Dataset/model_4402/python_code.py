from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FeatureGroupType(Enum):
    XORGROUP = "XORGROUP"
    ORGROUP = "ORGROUP"
    SIMPLEGROUP = "SIMPLEGROUP"
class ValueType(Enum):
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    NONE = "NONE"
    STRING = "STRING"
    FEATURE = "FEATURE"
class FeatureType(Enum):
    OPTIONAL = "OPTIONAL"
    MANDATORY = "MANDATORY"
    SIMPLE = "SIMPLE"


############################################
# Definition of Classes
############################################

class Relation:

    pass
class featureModel_RelationFeature(Relation):

    def __init__(self, lowerBound: int, upperBound: int, type: str, featureModel_RelationFeature: "featureModel_Feature" = None, featureModel_RelationFeature29: "featureModel_Feature" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.featureModel_RelationFeature = featureModel_RelationFeature
        self.featureModel_RelationFeature29 = featureModel_RelationFeature29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def featureModel_RelationFeature(self):
        return self.__featureModel_RelationFeature

    @featureModel_RelationFeature.setter
    def featureModel_RelationFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_RelationFeature__featureModel_RelationFeature", None)
        self.__featureModel_RelationFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature27"):
                opp_val = getattr(old_value, "featureModel_Feature27", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature27"):
                opp_val = getattr(value, "featureModel_Feature27", None)
                setattr(value, "featureModel_Feature27", self)

    @property
    def featureModel_RelationFeature29(self):
        return self.__featureModel_RelationFeature29

    @featureModel_RelationFeature29.setter
    def featureModel_RelationFeature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_RelationFeature__featureModel_RelationFeature29", None)
        self.__featureModel_RelationFeature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature30"):
                opp_val = getattr(old_value, "featureModel_Feature30", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature30"):
                opp_val = getattr(value, "featureModel_Feature30", None)
                setattr(value, "featureModel_Feature30", self)

class featureModel_RelationFG(Relation):

    pass
class featureModel_Relation:

    pass
class featureModel_Project:

    def __init__(self, nameConfigFile: str, nameConstraintsFile: str, numberOfProducts: int, validatedOCL: bool, validatedTEF: bool, featureModel_Project: set["featureModel_Node"] = None, featureModel_Project15: set["featureModel_Relation"] = None):
        self.nameConfigFile = nameConfigFile
        self.nameConstraintsFile = nameConstraintsFile
        self.numberOfProducts = numberOfProducts
        self.validatedOCL = validatedOCL
        self.validatedTEF = validatedTEF
        self.featureModel_Project = featureModel_Project if featureModel_Project is not None else set()
        self.featureModel_Project15 = featureModel_Project15 if featureModel_Project15 is not None else set()
        
    @property
    def validatedOCL(self) -> bool:
        return self.__validatedOCL

    @validatedOCL.setter
    def validatedOCL(self, validatedOCL: bool):
        self.__validatedOCL = validatedOCL

    @property
    def validatedTEF(self) -> bool:
        return self.__validatedTEF

    @validatedTEF.setter
    def validatedTEF(self, validatedTEF: bool):
        self.__validatedTEF = validatedTEF

    @property
    def numberOfProducts(self) -> int:
        return self.__numberOfProducts

    @numberOfProducts.setter
    def numberOfProducts(self, numberOfProducts: int):
        self.__numberOfProducts = numberOfProducts

    @property
    def nameConfigFile(self) -> str:
        return self.__nameConfigFile

    @nameConfigFile.setter
    def nameConfigFile(self, nameConfigFile: str):
        self.__nameConfigFile = nameConfigFile

    @property
    def nameConstraintsFile(self) -> str:
        return self.__nameConstraintsFile

    @nameConstraintsFile.setter
    def nameConstraintsFile(self, nameConstraintsFile: str):
        self.__nameConstraintsFile = nameConstraintsFile

    @property
    def featureModel_Project15(self):
        return self.__featureModel_Project15

    @featureModel_Project15.setter
    def featureModel_Project15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Project__featureModel_Project15", None)
        self.__featureModel_Project15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Relation"):
                    opp_val = getattr(item, "featureModel_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Relation"):
                    opp_val = getattr(item, "featureModel_Relation", None)
                    
                    setattr(item, "featureModel_Relation", self)
                    

    @property
    def featureModel_Project(self):
        return self.__featureModel_Project

    @featureModel_Project.setter
    def featureModel_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Project__featureModel_Project", None)
        self.__featureModel_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Node13"):
                    opp_val = getattr(item, "featureModel_Node13", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Node13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Node13"):
                    opp_val = getattr(item, "featureModel_Node13", None)
                    
                    setattr(item, "featureModel_Node13", self)
                    

class featureModel_Node:

    pass
class featureModel_TypedValue:

    def __init__(self, integerValue: str, stringValue: str, floatValue: str, featureModel_TypedValue10: "featureModel_Feature" = None, featureModel_TypedValue: "featureModel_Feature" = None):
        self.integerValue = integerValue
        self.stringValue = stringValue
        self.floatValue = floatValue
        self.featureModel_TypedValue10 = featureModel_TypedValue10
        self.featureModel_TypedValue = featureModel_TypedValue
        
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
    def floatValue(self) -> str:
        return self.__floatValue

    @floatValue.setter
    def floatValue(self, floatValue: str):
        self.__floatValue = floatValue

    @property
    def featureModel_TypedValue(self):
        return self.__featureModel_TypedValue

    @featureModel_TypedValue.setter
    def featureModel_TypedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_TypedValue__featureModel_TypedValue", None)
        self.__featureModel_TypedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature"):
                opp_val = getattr(old_value, "featureModel_Feature", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature"):
                opp_val = getattr(value, "featureModel_Feature", None)
                setattr(value, "featureModel_Feature", self)

    @property
    def featureModel_TypedValue10(self):
        return self.__featureModel_TypedValue10

    @featureModel_TypedValue10.setter
    def featureModel_TypedValue10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_TypedValue__featureModel_TypedValue10", None)
        self.__featureModel_TypedValue10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature11"):
                opp_val = getattr(old_value, "featureModel_Feature11", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature11"):
                opp_val = getattr(value, "featureModel_Feature11", None)
                setattr(value, "featureModel_Feature11", self)

class Node:

    pass
class featureModel_FeatureGroup(Node):

    def __init__(self, lowerBound: int, upperBound: int, type: str, featureModel_FeatureGroup: set["featureModel_Feature"] = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.featureModel_FeatureGroup = featureModel_FeatureGroup if featureModel_FeatureGroup is not None else set()
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def featureModel_FeatureGroup(self):
        return self.__featureModel_FeatureGroup

    @featureModel_FeatureGroup.setter
    def featureModel_FeatureGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_FeatureGroup__featureModel_FeatureGroup", None)
        self.__featureModel_FeatureGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Feature17"):
                    opp_val = getattr(item, "featureModel_Feature17", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Feature17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Feature17"):
                    opp_val = getattr(item, "featureModel_Feature17", None)
                    
                    setattr(item, "featureModel_Feature17", self)
                    

class featureModel_Feature(Node):

    def __init__(self, name: str, valueType: str, featureModel_Feature11: "featureModel_TypedValue" = None, featureModel_Feature: "featureModel_TypedValue" = None, featureModel_Feature2: set["featureModel_Node"] = None, featureModel_Feature5: "featureModel_Feature" = None, featureModel_Feature3: "featureModel_Feature" = None, featureModel_Feature8: "featureModel_Feature" = None, featureModel_Feature6: set["featureModel_Feature"] = None, featureModel_Feature27: "featureModel_RelationFeature" = None, featureModel_Feature30: "featureModel_RelationFeature" = None, featureModel_Feature17: "featureModel_FeatureGroup" = None):
        self.name = name
        self.valueType = valueType
        self.featureModel_Feature11 = featureModel_Feature11
        self.featureModel_Feature = featureModel_Feature
        self.featureModel_Feature2 = featureModel_Feature2 if featureModel_Feature2 is not None else set()
        self.featureModel_Feature5 = featureModel_Feature5
        self.featureModel_Feature3 = featureModel_Feature3
        self.featureModel_Feature8 = featureModel_Feature8
        self.featureModel_Feature6 = featureModel_Feature6 if featureModel_Feature6 is not None else set()
        self.featureModel_Feature27 = featureModel_Feature27
        self.featureModel_Feature30 = featureModel_Feature30
        self.featureModel_Feature17 = featureModel_Feature17
        
    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureModel_Feature(self):
        return self.__featureModel_Feature

    @featureModel_Feature.setter
    def featureModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature", None)
        self.__featureModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_TypedValue"):
                opp_val = getattr(old_value, "featureModel_TypedValue", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_TypedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_TypedValue"):
                opp_val = getattr(value, "featureModel_TypedValue", None)
                setattr(value, "featureModel_TypedValue", self)

    @property
    def featureModel_Feature5(self):
        return self.__featureModel_Feature5

    @featureModel_Feature5.setter
    def featureModel_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature5", None)
        self.__featureModel_Feature5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature3"):
                opp_val = getattr(old_value, "featureModel_Feature3", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature3"):
                opp_val = getattr(value, "featureModel_Feature3", None)
                setattr(value, "featureModel_Feature3", self)

    @property
    def featureModel_Feature27(self):
        return self.__featureModel_Feature27

    @featureModel_Feature27.setter
    def featureModel_Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature27", None)
        self.__featureModel_Feature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_RelationFeature"):
                opp_val = getattr(old_value, "featureModel_RelationFeature", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_RelationFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_RelationFeature"):
                opp_val = getattr(value, "featureModel_RelationFeature", None)
                setattr(value, "featureModel_RelationFeature", self)

    @property
    def featureModel_Feature2(self):
        return self.__featureModel_Feature2

    @featureModel_Feature2.setter
    def featureModel_Feature2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature2", None)
        self.__featureModel_Feature2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Node"):
                    opp_val = getattr(item, "featureModel_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Node"):
                    opp_val = getattr(item, "featureModel_Node", None)
                    
                    setattr(item, "featureModel_Node", self)
                    

    @property
    def featureModel_Feature8(self):
        return self.__featureModel_Feature8

    @featureModel_Feature8.setter
    def featureModel_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature8", None)
        self.__featureModel_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature6"):
                opp_val = getattr(old_value, "featureModel_Feature6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature6"):
                opp_val = getattr(value, "featureModel_Feature6", None)
                if opp_val is None:
                    setattr(value, "featureModel_Feature6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature6(self):
        return self.__featureModel_Feature6

    @featureModel_Feature6.setter
    def featureModel_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature6", None)
        self.__featureModel_Feature6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Feature8"):
                    opp_val = getattr(item, "featureModel_Feature8", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Feature8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Feature8"):
                    opp_val = getattr(item, "featureModel_Feature8", None)
                    
                    setattr(item, "featureModel_Feature8", self)
                    

    @property
    def featureModel_Feature17(self):
        return self.__featureModel_Feature17

    @featureModel_Feature17.setter
    def featureModel_Feature17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature17", None)
        self.__featureModel_Feature17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_FeatureGroup"):
                opp_val = getattr(old_value, "featureModel_FeatureGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_FeatureGroup"):
                opp_val = getattr(value, "featureModel_FeatureGroup", None)
                if opp_val is None:
                    setattr(value, "featureModel_FeatureGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature3(self):
        return self.__featureModel_Feature3

    @featureModel_Feature3.setter
    def featureModel_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature3", None)
        self.__featureModel_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature5"):
                opp_val = getattr(old_value, "featureModel_Feature5", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature5"):
                opp_val = getattr(value, "featureModel_Feature5", None)
                setattr(value, "featureModel_Feature5", self)

    @property
    def featureModel_Feature30(self):
        return self.__featureModel_Feature30

    @featureModel_Feature30.setter
    def featureModel_Feature30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature30", None)
        self.__featureModel_Feature30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_RelationFeature29"):
                opp_val = getattr(old_value, "featureModel_RelationFeature29", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_RelationFeature29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_RelationFeature29"):
                opp_val = getattr(value, "featureModel_RelationFeature29", None)
                setattr(value, "featureModel_RelationFeature29", self)

    @property
    def featureModel_Feature11(self):
        return self.__featureModel_Feature11

    @featureModel_Feature11.setter
    def featureModel_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature11", None)
        self.__featureModel_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_TypedValue10"):
                opp_val = getattr(old_value, "featureModel_TypedValue10", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_TypedValue10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_TypedValue10"):
                opp_val = getattr(value, "featureModel_TypedValue10", None)
                setattr(value, "featureModel_TypedValue10", self)
