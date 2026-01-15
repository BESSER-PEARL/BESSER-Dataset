from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SingleFeatureConnection:

    pass
class FCORE_CardinalityConnection(SingleFeatureConnection):

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

class Influence:

    pass
class FeatureConstraint:

    pass
class Conncection:

    pass
class FCORE_Conncection(ABC):

    pass
class FCORE_Influence(Conncection):

    def __init__(self, contribution: float, Influence: "FCORE_Softgoal" = None, influence: "FCORE_Softgoal" = None):
        self.contribution = contribution
        self.Influence = Influence
        self.influence = influence
        
    @property
    def contribution(self) -> float:
        return self.__contribution

    @contribution.setter
    def contribution(self, contribution: float):
        self.__contribution = contribution

    @property
    def influence(self):
        return self.__influence

    @influence.setter
    def influence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Influence__influence", None)
        self.__influence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Softgoal"):
                opp_val = getattr(old_value, "Softgoal", None)
                if opp_val == self:
                    setattr(old_value, "Softgoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Softgoal"):
                opp_val = getattr(value, "Softgoal", None)
                setattr(value, "Softgoal", self)

    @property
    def Influence(self):
        return self.__Influence

    @Influence.setter
    def Influence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Influence__Influence", None)
        self.__Influence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softgoal"):
                opp_val = getattr(old_value, "softgoal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softgoal"):
                opp_val = getattr(value, "softgoal", None)
                if opp_val is None:
                    setattr(value, "softgoal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Feature:

    pass
class FCORE_SingleFeatureConnection(Conncection):

    pass
class FCORE_FeatureConstraint(Conncection):

    pass
class FCORE_Feature(ABC):

    def __init__(self, selected: bool, name: str, source: set["FCORE_AttributeConstraintConnection"] = None, FCORE_Feature: set["FCORE_Attribute"] = None, featureStart: set["FCORE_FeatureConstraint"] = None, featureEnd: set["FCORE_FeatureConstraint"] = None, feature: set["FCORE_InfluenceFeature"] = None, source39: set["FCORE_SingleFeatureConnection"] = None, source41: set["FCORE_FeatureToGroupConnection"] = None, Feature: "FCORE_FeatureConstraint" = None, Feature59: "FCORE_FeatureConstraint" = None, Feature66: "FCORE_SingleFeatureConnection" = None, Feature62: "FCORE_InfluenceFeature" = None, Feature69: "FCORE_FeatureToGroupConnection" = None, Feature75: "FCORE_AttributeConstraintConnection" = None):
        self.selected = selected
        self.name = name
        self.source = source if source is not None else set()
        self.FCORE_Feature = FCORE_Feature if FCORE_Feature is not None else set()
        self.featureStart = featureStart if featureStart is not None else set()
        self.featureEnd = featureEnd if featureEnd is not None else set()
        self.feature = feature if feature is not None else set()
        self.source39 = source39 if source39 is not None else set()
        self.source41 = source41 if source41 is not None else set()
        self.Feature = Feature
        self.Feature59 = Feature59
        self.Feature66 = Feature66
        self.Feature62 = Feature62
        self.Feature69 = Feature69
        self.Feature75 = Feature75
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeConstraintConnection"):
                    opp_val = getattr(item, "AttributeConstraintConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeConstraintConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeConstraintConnection"):
                    opp_val = getattr(item, "AttributeConstraintConnection", None)
                    
                    setattr(item, "AttributeConstraintConnection", self)
                    

    @property
    def featureEnd(self):
        return self.__featureEnd

    @featureEnd.setter
    def featureEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__featureEnd", None)
        self.__featureEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureConstraint36"):
                    opp_val = getattr(item, "FeatureConstraint36", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureConstraint36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureConstraint36"):
                    opp_val = getattr(item, "FeatureConstraint36", None)
                    
                    setattr(item, "FeatureConstraint36", self)
                    

    @property
    def Feature69(self):
        return self.__Feature69

    @Feature69.setter
    def Feature69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__Feature69", None)
        self.__Feature69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureToGroupConnections"):
                opp_val = getattr(old_value, "featureToGroupConnections", None)
                if opp_val == self:
                    setattr(old_value, "featureToGroupConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureToGroupConnections"):
                opp_val = getattr(value, "featureToGroupConnections", None)
                setattr(value, "featureToGroupConnections", self)

    @property
    def source41(self):
        return self.__source41

    @source41.setter
    def source41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__source41", None)
        self.__source41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureToGroupConnection"):
                    opp_val = getattr(item, "FeatureToGroupConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureToGroupConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureToGroupConnection"):
                    opp_val = getattr(item, "FeatureToGroupConnection", None)
                    
                    setattr(item, "FeatureToGroupConnection", self)
                    

    @property
    def source39(self):
        return self.__source39

    @source39.setter
    def source39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__source39", None)
        self.__source39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleFeatureConnection"):
                    opp_val = getattr(item, "SingleFeatureConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleFeatureConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleFeatureConnection"):
                    opp_val = getattr(item, "SingleFeatureConnection", None)
                    
                    setattr(item, "SingleFeatureConnection", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureConstraintsStarts"):
                opp_val = getattr(old_value, "featureConstraintsStarts", None)
                if opp_val == self:
                    setattr(old_value, "featureConstraintsStarts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureConstraintsStarts"):
                opp_val = getattr(value, "featureConstraintsStarts", None)
                setattr(value, "featureConstraintsStarts", self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InfluenceFeature"):
                    opp_val = getattr(item, "InfluenceFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "InfluenceFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InfluenceFeature"):
                    opp_val = getattr(item, "InfluenceFeature", None)
                    
                    setattr(item, "InfluenceFeature", self)
                    

    @property
    def Feature66(self):
        return self.__Feature66

    @Feature66.setter
    def Feature66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__Feature66", None)
        self.__Feature66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingSingleFeatureConnections"):
                opp_val = getattr(old_value, "outgoingSingleFeatureConnections", None)
                if opp_val == self:
                    setattr(old_value, "outgoingSingleFeatureConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingSingleFeatureConnections"):
                opp_val = getattr(value, "outgoingSingleFeatureConnections", None)
                setattr(value, "outgoingSingleFeatureConnections", self)

    @property
    def featureStart(self):
        return self.__featureStart

    @featureStart.setter
    def featureStart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__featureStart", None)
        self.__featureStart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureConstraint"):
                    opp_val = getattr(item, "FeatureConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureConstraint"):
                    opp_val = getattr(item, "FeatureConstraint", None)
                    
                    setattr(item, "FeatureConstraint", self)
                    

    @property
    def Feature59(self):
        return self.__Feature59

    @Feature59.setter
    def Feature59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__Feature59", None)
        self.__Feature59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureConstraintsEnds"):
                opp_val = getattr(old_value, "featureConstraintsEnds", None)
                if opp_val == self:
                    setattr(old_value, "featureConstraintsEnds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureConstraintsEnds"):
                opp_val = getattr(value, "featureConstraintsEnds", None)
                setattr(value, "featureConstraintsEnds", self)

    @property
    def Feature75(self):
        return self.__Feature75

    @Feature75.setter
    def Feature75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__Feature75", None)
        self.__Feature75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributeConstraints"):
                opp_val = getattr(old_value, "attributeConstraints", None)
                if opp_val == self:
                    setattr(old_value, "attributeConstraints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributeConstraints"):
                opp_val = getattr(value, "attributeConstraints", None)
                setattr(value, "attributeConstraints", self)

    @property
    def FCORE_Feature(self):
        return self.__FCORE_Feature

    @FCORE_Feature.setter
    def FCORE_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__FCORE_Feature", None)
        self.__FCORE_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FCORE_Attribute33"):
                    opp_val = getattr(item, "FCORE_Attribute33", None)
                    
                    if opp_val == self:
                        setattr(item, "FCORE_Attribute33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FCORE_Attribute33"):
                    opp_val = getattr(item, "FCORE_Attribute33", None)
                    
                    setattr(item, "FCORE_Attribute33", self)
                    

    @property
    def Feature62(self):
        return self.__Feature62

    @Feature62.setter
    def Feature62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Feature__Feature62", None)
        self.__Feature62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "influences"):
                opp_val = getattr(old_value, "influences", None)
                if opp_val == self:
                    setattr(old_value, "influences", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "influences"):
                opp_val = getattr(value, "influences", None)
                setattr(value, "influences", self)

class FCORE_AttributeConstraintConnection(Conncection):

    pass
class FCORE_GroupToFeatureConnection(Conncection):

    pass
class FCORE_FeatureToGroupConnection(Conncection):

    pass
class FCORE_OptionalConnection(SingleFeatureConnection):

    pass
class FCORE_MandatoryConnection(SingleFeatureConnection):

    pass
class FCORE_InfluenceAttribute(Influence):

    pass
class FCORE_ExcludesFeatureConstraint(FeatureConstraint):

    pass
class FCORE_RequiresFeatureConstraint(FeatureConstraint):

    pass
class FCORE_AttributeConstraint:

    def __init__(self, equation: str, FCORE_AttributeConstraint: "FCORE_FeatureModel" = None, target54: "FCORE_AttributeConstraintConnection" = None, AttributeConstraint: "FCORE_AttributeConstraintConnection" = None):
        self.equation = equation
        self.FCORE_AttributeConstraint = FCORE_AttributeConstraint
        self.target54 = target54
        self.AttributeConstraint = AttributeConstraint
        
    @property
    def equation(self) -> str:
        return self.__equation

    @equation.setter
    def equation(self, equation: str):
        self.__equation = equation

    @property
    def AttributeConstraint(self):
        return self.__AttributeConstraint

    @AttributeConstraint.setter
    def AttributeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_AttributeConstraint__AttributeConstraint", None)
        self.__AttributeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributeConstraintConnection"):
                opp_val = getattr(old_value, "attributeConstraintConnection", None)
                if opp_val == self:
                    setattr(old_value, "attributeConstraintConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributeConstraintConnection"):
                opp_val = getattr(value, "attributeConstraintConnection", None)
                setattr(value, "attributeConstraintConnection", self)

    @property
    def target54(self):
        return self.__target54

    @target54.setter
    def target54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_AttributeConstraint__target54", None)
        self.__target54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeConstraintConnection55"):
                opp_val = getattr(old_value, "AttributeConstraintConnection55", None)
                if opp_val == self:
                    setattr(old_value, "AttributeConstraintConnection55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeConstraintConnection55"):
                opp_val = getattr(value, "AttributeConstraintConnection55", None)
                setattr(value, "AttributeConstraintConnection55", self)

    @property
    def FCORE_AttributeConstraint(self):
        return self.__FCORE_AttributeConstraint

    @FCORE_AttributeConstraint.setter
    def FCORE_AttributeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_AttributeConstraint__FCORE_AttributeConstraint", None)
        self.__FCORE_AttributeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FCORE_FeatureModel10"):
                opp_val = getattr(old_value, "FCORE_FeatureModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FCORE_FeatureModel10"):
                opp_val = getattr(value, "FCORE_FeatureModel10", None)
                if opp_val is None:
                    setattr(value, "FCORE_FeatureModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FCORE_Attribute:

    def __init__(self, name: str, value: int, min: int, max: int, FCORE_Attribute: "FCORE_FeatureModel" = None, FCORE_Attribute33: "FCORE_Feature" = None, attribute: set["FCORE_InfluenceAttribute"] = None, Attribute: "FCORE_InfluenceAttribute" = None):
        self.name = name
        self.value = value
        self.min = min
        self.max = max
        self.FCORE_Attribute = FCORE_Attribute
        self.FCORE_Attribute33 = FCORE_Attribute33
        self.attribute = attribute if attribute is not None else set()
        self.Attribute = Attribute
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def FCORE_Attribute(self):
        return self.__FCORE_Attribute

    @FCORE_Attribute.setter
    def FCORE_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Attribute__FCORE_Attribute", None)
        self.__FCORE_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FCORE_FeatureModel8"):
                opp_val = getattr(old_value, "FCORE_FeatureModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FCORE_FeatureModel8"):
                opp_val = getattr(value, "FCORE_FeatureModel8", None)
                if opp_val is None:
                    setattr(value, "FCORE_FeatureModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FCORE_Attribute33(self):
        return self.__FCORE_Attribute33

    @FCORE_Attribute33.setter
    def FCORE_Attribute33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Attribute__FCORE_Attribute33", None)
        self.__FCORE_Attribute33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FCORE_Feature"):
                opp_val = getattr(old_value, "FCORE_Feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FCORE_Feature"):
                opp_val = getattr(value, "FCORE_Feature", None)
                if opp_val is None:
                    setattr(value, "FCORE_Feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "influences64"):
                opp_val = getattr(old_value, "influences64", None)
                if opp_val == self:
                    setattr(old_value, "influences64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "influences64"):
                opp_val = getattr(value, "influences64", None)
                setattr(value, "influences64", self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Attribute__attribute", None)
        self.__attribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InfluenceAttribute"):
                    opp_val = getattr(item, "InfluenceAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "InfluenceAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InfluenceAttribute"):
                    opp_val = getattr(item, "InfluenceAttribute", None)
                    
                    setattr(item, "InfluenceAttribute", self)
                    

class FCORE_FeatureGroup:

    def __init__(self, min: int, max: int, FCORE_FeatureGroup: "FCORE_FeatureModel" = None, target47: "FCORE_FeatureToGroupConnection" = None, source50: set["FCORE_GroupToFeatureConnection"] = None, FeatureGroup: "FCORE_FeatureToGroupConnection" = None, FeatureGroup72: "FCORE_GroupToFeatureConnection" = None):
        self.min = min
        self.max = max
        self.FCORE_FeatureGroup = FCORE_FeatureGroup
        self.target47 = target47
        self.source50 = source50 if source50 is not None else set()
        self.FeatureGroup = FeatureGroup
        self.FeatureGroup72 = FeatureGroup72
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def FeatureGroup72(self):
        return self.__FeatureGroup72

    @FeatureGroup72.setter
    def FeatureGroup72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_FeatureGroup__FeatureGroup72", None)
        self.__FeatureGroup72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupToFeatureConnections"):
                opp_val = getattr(old_value, "groupToFeatureConnections", None)
                if opp_val == self:
                    setattr(old_value, "groupToFeatureConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupToFeatureConnections"):
                opp_val = getattr(value, "groupToFeatureConnections", None)
                setattr(value, "groupToFeatureConnections", self)

    @property
    def FCORE_FeatureGroup(self):
        return self.__FCORE_FeatureGroup

    @FCORE_FeatureGroup.setter
    def FCORE_FeatureGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_FeatureGroup__FCORE_FeatureGroup", None)
        self.__FCORE_FeatureGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FCORE_FeatureModel6"):
                opp_val = getattr(old_value, "FCORE_FeatureModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FCORE_FeatureModel6"):
                opp_val = getattr(value, "FCORE_FeatureModel6", None)
                if opp_val is None:
                    setattr(value, "FCORE_FeatureModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target47(self):
        return self.__target47

    @target47.setter
    def target47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_FeatureGroup__target47", None)
        self.__target47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureToGroupConnection48"):
                opp_val = getattr(old_value, "FeatureToGroupConnection48", None)
                if opp_val == self:
                    setattr(old_value, "FeatureToGroupConnection48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureToGroupConnection48"):
                opp_val = getattr(value, "FeatureToGroupConnection48", None)
                setattr(value, "FeatureToGroupConnection48", self)

    @property
    def FeatureGroup(self):
        return self.__FeatureGroup

    @FeatureGroup.setter
    def FeatureGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_FeatureGroup__FeatureGroup", None)
        self.__FeatureGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureToGroupConnection"):
                opp_val = getattr(old_value, "featureToGroupConnection", None)
                if opp_val == self:
                    setattr(old_value, "featureToGroupConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureToGroupConnection"):
                opp_val = getattr(value, "featureToGroupConnection", None)
                setattr(value, "featureToGroupConnection", self)

    @property
    def source50(self):
        return self.__source50

    @source50.setter
    def source50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_FeatureGroup__source50", None)
        self.__source50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GroupToFeatureConnection51"):
                    opp_val = getattr(item, "GroupToFeatureConnection51", None)
                    
                    if opp_val == self:
                        setattr(item, "GroupToFeatureConnection51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GroupToFeatureConnection51"):
                    opp_val = getattr(item, "GroupToFeatureConnection51", None)
                    
                    setattr(item, "GroupToFeatureConnection51", self)
                    

class FCORE_SolitaryFeature(Feature):

    def __init__(self, min: int, max: int, FCORE_SolitaryFeature: "FCORE_FeatureModel" = None, target: "FCORE_SingleFeatureConnection" = None, SolitaryFeature: "FCORE_SingleFeatureConnection" = None):
        self.min = min
        self.max = max
        self.FCORE_SolitaryFeature = FCORE_SolitaryFeature
        self.target = target
        self.SolitaryFeature = SolitaryFeature
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def FCORE_SolitaryFeature(self):
        return self.__FCORE_SolitaryFeature

    @FCORE_SolitaryFeature.setter
    def FCORE_SolitaryFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_SolitaryFeature__FCORE_SolitaryFeature", None)
        self.__FCORE_SolitaryFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FCORE_FeatureModel4"):
                opp_val = getattr(old_value, "FCORE_FeatureModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FCORE_FeatureModel4"):
                opp_val = getattr(value, "FCORE_FeatureModel4", None)
                if opp_val is None:
                    setattr(value, "FCORE_FeatureModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SolitaryFeature(self):
        return self.__SolitaryFeature

    @SolitaryFeature.setter
    def SolitaryFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_SolitaryFeature__SolitaryFeature", None)
        self.__SolitaryFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingSingleFeatureConnection"):
                opp_val = getattr(old_value, "incomingSingleFeatureConnection", None)
                if opp_val == self:
                    setattr(old_value, "incomingSingleFeatureConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingSingleFeatureConnection"):
                opp_val = getattr(value, "incomingSingleFeatureConnection", None)
                setattr(value, "incomingSingleFeatureConnection", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_SolitaryFeature__target", None)
        self.__target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleFeatureConnection43"):
                opp_val = getattr(old_value, "SingleFeatureConnection43", None)
                if opp_val == self:
                    setattr(old_value, "SingleFeatureConnection43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleFeatureConnection43"):
                opp_val = getattr(value, "SingleFeatureConnection43", None)
                setattr(value, "SingleFeatureConnection43", self)

class FCORE_GroupFeature(Feature):

    pass
class FCORE_RootFeature(Feature):

    pass
class FCORE_FeatureModel:

    pass
class FCORE_InfluenceFeature(Influence):

    pass
class FCORE_Softgoal:

    def __init__(self, name: str, weighting: str, FCORE_Softgoal: "FCORE_FeatureModel" = None, softgoal: set["FCORE_Influence"] = None, Softgoal: "FCORE_Influence" = None):
        self.name = name
        self.weighting = weighting
        self.FCORE_Softgoal = FCORE_Softgoal
        self.softgoal = softgoal if softgoal is not None else set()
        self.Softgoal = Softgoal
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def weighting(self) -> str:
        return self.__weighting

    @weighting.setter
    def weighting(self, weighting: str):
        self.__weighting = weighting

    @property
    def Softgoal(self):
        return self.__Softgoal

    @Softgoal.setter
    def Softgoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Softgoal__Softgoal", None)
        self.__Softgoal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "influence"):
                opp_val = getattr(old_value, "influence", None)
                if opp_val == self:
                    setattr(old_value, "influence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "influence"):
                opp_val = getattr(value, "influence", None)
                setattr(value, "influence", self)

    @property
    def FCORE_Softgoal(self):
        return self.__FCORE_Softgoal

    @FCORE_Softgoal.setter
    def FCORE_Softgoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Softgoal__FCORE_Softgoal", None)
        self.__FCORE_Softgoal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FCORE_FeatureModel16"):
                opp_val = getattr(old_value, "FCORE_FeatureModel16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FCORE_FeatureModel16"):
                opp_val = getattr(value, "FCORE_FeatureModel16", None)
                if opp_val is None:
                    setattr(value, "FCORE_FeatureModel16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softgoal(self):
        return self.__softgoal

    @softgoal.setter
    def softgoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FCORE_Softgoal__softgoal", None)
        self.__softgoal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Influence"):
                    opp_val = getattr(item, "Influence", None)
                    
                    if opp_val == self:
                        setattr(item, "Influence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Influence"):
                    opp_val = getattr(item, "Influence", None)
                    
                    setattr(item, "Influence", self)
                    
