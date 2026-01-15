from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class featureDiagram_FeatureElement:

    pass
class Operator:

    pass
class featureDiagram_Or(Operator):

    pass
class featureDiagram_Mandatory(Operator):

    pass
class featureDiagram_Alternative(Operator):

    pass
class featureDiagram_Opt(Operator):

    pass
class Constraint:

    pass
class featureDiagram_Mutex(Constraint):

    pass
class featureDiagram_Require(Constraint):

    pass
class featureDiagram_Card(Operator):

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max
        
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

class featureDiagram_EObject:

    pass
class Feature:

    pass
class featureDiagram_PrimitiveFeature(Feature):

    pass
class FeatureElement:

    pass
class featureDiagram_Operator(FeatureElement):

    def __init__(self, name: str, Operator: "featureDiagram_Feature" = None, Operator10: "featureDiagram_Feature" = None, operator: "featureDiagram_Feature" = None, owningOperator: set["featureDiagram_Feature"] = None):
        self.name = name
        self.Operator = Operator
        self.Operator10 = Operator10
        self.operator = operator
        self.owningOperator = owningOperator if owningOperator is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningOperator(self):
        return self.__owningOperator

    @owningOperator.setter
    def owningOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Operator__owningOperator", None)
        self.__owningOperator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature23"):
                    opp_val = getattr(item, "Feature23", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature23"):
                    opp_val = getattr(item, "Feature23", None)
                    
                    setattr(item, "Feature23", self)
                    

    @property
    def Operator10(self):
        return self.__Operator10

    @Operator10.setter
    def Operator10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Operator__Operator10", None)
        self.__Operator10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features9"):
                opp_val = getattr(old_value, "features9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features9"):
                opp_val = getattr(value, "features9", None)
                if opp_val is None:
                    setattr(value, "features9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Operator__operator", None)
        self.__operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature21"):
                opp_val = getattr(old_value, "Feature21", None)
                if opp_val == self:
                    setattr(old_value, "Feature21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature21"):
                opp_val = getattr(value, "Feature21", None)
                setattr(value, "Feature21", self)

    @property
    def Operator(self):
        return self.__Operator

    @Operator.setter
    def Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Operator__Operator", None)
        self.__Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFeature"):
                opp_val = getattr(old_value, "owningFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFeature"):
                opp_val = getattr(value, "owningFeature", None)
                if opp_val is None:
                    setattr(value, "owningFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featureDiagram_Constraint(FeatureElement):

    pass
class featureDiagram_Attribute(FeatureElement):

    def __init__(self, name: str, value: str, type: str, Attribute: "featureDiagram_Feature" = None, attributes: "featureDiagram_Feature" = None):
        self.name = name
        self.value = value
        self.type = type
        self.Attribute = Attribute
        self.attributes = attributes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFeature7"):
                opp_val = getattr(old_value, "owningFeature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFeature7"):
                opp_val = getattr(value, "owningFeature7", None)
                if opp_val is None:
                    setattr(value, "owningFeature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature26"):
                opp_val = getattr(old_value, "Feature26", None)
                if opp_val == self:
                    setattr(old_value, "Feature26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature26"):
                opp_val = getattr(value, "Feature26", None)
                setattr(value, "Feature26", self)

class featureDiagram_FeatureDiagram(FeatureElement):

    def __init__(self, graphTypeTree: bool, owningFeatureDiagram: set["featureDiagram_Feature"] = None, featureDiagram_FeatureDiagram: "featureDiagram_Feature" = None, featureDiagram_FeatureDiagram3: set["featureDiagram_ConstraintEdge"] = None, FeatureDiagram: "featureDiagram_Feature" = None):
        self.graphTypeTree = graphTypeTree
        self.owningFeatureDiagram = owningFeatureDiagram if owningFeatureDiagram is not None else set()
        self.featureDiagram_FeatureDiagram = featureDiagram_FeatureDiagram
        self.featureDiagram_FeatureDiagram3 = featureDiagram_FeatureDiagram3 if featureDiagram_FeatureDiagram3 is not None else set()
        self.FeatureDiagram = FeatureDiagram
        
    @property
    def graphTypeTree(self) -> bool:
        return self.__graphTypeTree

    @graphTypeTree.setter
    def graphTypeTree(self, graphTypeTree: bool):
        self.__graphTypeTree = graphTypeTree

    @property
    def featureDiagram_FeatureDiagram3(self):
        return self.__featureDiagram_FeatureDiagram3

    @featureDiagram_FeatureDiagram3.setter
    def featureDiagram_FeatureDiagram3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_FeatureDiagram__featureDiagram_FeatureDiagram3", None)
        self.__featureDiagram_FeatureDiagram3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureDiagram_ConstraintEdge"):
                    opp_val = getattr(item, "featureDiagram_ConstraintEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "featureDiagram_ConstraintEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureDiagram_ConstraintEdge"):
                    opp_val = getattr(item, "featureDiagram_ConstraintEdge", None)
                    
                    setattr(item, "featureDiagram_ConstraintEdge", self)
                    

    @property
    def featureDiagram_FeatureDiagram(self):
        return self.__featureDiagram_FeatureDiagram

    @featureDiagram_FeatureDiagram.setter
    def featureDiagram_FeatureDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_FeatureDiagram__featureDiagram_FeatureDiagram", None)
        self.__featureDiagram_FeatureDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_Feature"):
                opp_val = getattr(old_value, "featureDiagram_Feature", None)
                if opp_val == self:
                    setattr(old_value, "featureDiagram_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_Feature"):
                opp_val = getattr(value, "featureDiagram_Feature", None)
                setattr(value, "featureDiagram_Feature", self)

    @property
    def FeatureDiagram(self):
        return self.__FeatureDiagram

    @FeatureDiagram.setter
    def FeatureDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_FeatureDiagram__FeatureDiagram", None)
        self.__FeatureDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

    @property
    def owningFeatureDiagram(self):
        return self.__owningFeatureDiagram

    @owningFeatureDiagram.setter
    def owningFeatureDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_FeatureDiagram__owningFeatureDiagram", None)
        self.__owningFeatureDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

class featureDiagram_ConstraintEdge(FeatureElement):

    pass
class featureDiagram_Feature(FeatureElement):

    def __init__(self, name: str, selected: bool, Feature: "featureDiagram_FeatureDiagram" = None, featureDiagram_Feature: "featureDiagram_FeatureDiagram" = None, featureDiagram_Feature15: "featureDiagram_ConstraintEdge" = None, features: "featureDiagram_FeatureDiagram" = None, owningFeature: set["featureDiagram_Operator"] = None, owningFeature7: set["featureDiagram_Attribute"] = None, features9: set["featureDiagram_Operator"] = None, featureDiagram_Feature12: set["featureDiagram_EObject"] = None, featureDiagram_Feature19: "featureDiagram_ConstraintEdge" = None, Feature21: "featureDiagram_Operator" = None, Feature23: "featureDiagram_Operator" = None, Feature26: "featureDiagram_Attribute" = None):
        self.name = name
        self.selected = selected
        self.Feature = Feature
        self.featureDiagram_Feature = featureDiagram_Feature
        self.featureDiagram_Feature15 = featureDiagram_Feature15
        self.features = features
        self.owningFeature = owningFeature if owningFeature is not None else set()
        self.owningFeature7 = owningFeature7 if owningFeature7 is not None else set()
        self.features9 = features9 if features9 is not None else set()
        self.featureDiagram_Feature12 = featureDiagram_Feature12 if featureDiagram_Feature12 is not None else set()
        self.featureDiagram_Feature19 = featureDiagram_Feature19
        self.Feature21 = Feature21
        self.Feature23 = Feature23
        self.Feature26 = Feature26
        
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
    def featureDiagram_Feature19(self):
        return self.__featureDiagram_Feature19

    @featureDiagram_Feature19.setter
    def featureDiagram_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature19", None)
        self.__featureDiagram_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_ConstraintEdge18"):
                opp_val = getattr(old_value, "featureDiagram_ConstraintEdge18", None)
                if opp_val == self:
                    setattr(old_value, "featureDiagram_ConstraintEdge18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_ConstraintEdge18"):
                opp_val = getattr(value, "featureDiagram_ConstraintEdge18", None)
                setattr(value, "featureDiagram_ConstraintEdge18", self)

    @property
    def featureDiagram_Feature(self):
        return self.__featureDiagram_Feature

    @featureDiagram_Feature.setter
    def featureDiagram_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature", None)
        self.__featureDiagram_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_FeatureDiagram"):
                opp_val = getattr(old_value, "featureDiagram_FeatureDiagram", None)
                if opp_val == self:
                    setattr(old_value, "featureDiagram_FeatureDiagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_FeatureDiagram"):
                opp_val = getattr(value, "featureDiagram_FeatureDiagram", None)
                setattr(value, "featureDiagram_FeatureDiagram", self)

    @property
    def Feature23(self):
        return self.__Feature23

    @Feature23.setter
    def Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature23", None)
        self.__Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningOperator"):
                opp_val = getattr(old_value, "owningOperator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningOperator"):
                opp_val = getattr(value, "owningOperator", None)
                if opp_val is None:
                    setattr(value, "owningOperator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningFeature(self):
        return self.__owningFeature

    @owningFeature.setter
    def owningFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__owningFeature", None)
        self.__owningFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operator"):
                    opp_val = getattr(item, "Operator", None)
                    
                    if opp_val == self:
                        setattr(item, "Operator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operator"):
                    opp_val = getattr(item, "Operator", None)
                    
                    setattr(item, "Operator", self)
                    

    @property
    def Feature21(self):
        return self.__Feature21

    @Feature21.setter
    def Feature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature21", None)
        self.__Feature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operator"):
                opp_val = getattr(old_value, "operator", None)
                if opp_val == self:
                    setattr(old_value, "operator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operator"):
                opp_val = getattr(value, "operator", None)
                setattr(value, "operator", self)

    @property
    def owningFeature7(self):
        return self.__owningFeature7

    @owningFeature7.setter
    def owningFeature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__owningFeature7", None)
        self.__owningFeature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFeatureDiagram"):
                opp_val = getattr(old_value, "owningFeatureDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFeatureDiagram"):
                opp_val = getattr(value, "owningFeatureDiagram", None)
                if opp_val is None:
                    setattr(value, "owningFeatureDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature26(self):
        return self.__Feature26

    @Feature26.setter
    def Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature26", None)
        self.__Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

    @property
    def features9(self):
        return self.__features9

    @features9.setter
    def features9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__features9", None)
        self.__features9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operator10"):
                    opp_val = getattr(item, "Operator10", None)
                    
                    if opp_val == self:
                        setattr(item, "Operator10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operator10"):
                    opp_val = getattr(item, "Operator10", None)
                    
                    setattr(item, "Operator10", self)
                    

    @property
    def featureDiagram_Feature15(self):
        return self.__featureDiagram_Feature15

    @featureDiagram_Feature15.setter
    def featureDiagram_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature15", None)
        self.__featureDiagram_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_ConstraintEdge14"):
                opp_val = getattr(old_value, "featureDiagram_ConstraintEdge14", None)
                if opp_val == self:
                    setattr(old_value, "featureDiagram_ConstraintEdge14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_ConstraintEdge14"):
                opp_val = getattr(value, "featureDiagram_ConstraintEdge14", None)
                setattr(value, "featureDiagram_ConstraintEdge14", self)

    @property
    def featureDiagram_Feature12(self):
        return self.__featureDiagram_Feature12

    @featureDiagram_Feature12.setter
    def featureDiagram_Feature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature12", None)
        self.__featureDiagram_Feature12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureDiagram_EObject"):
                    opp_val = getattr(item, "featureDiagram_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "featureDiagram_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureDiagram_EObject"):
                    opp_val = getattr(item, "featureDiagram_EObject", None)
                    
                    setattr(item, "featureDiagram_EObject", self)
                    

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureDiagram"):
                opp_val = getattr(old_value, "FeatureDiagram", None)
                if opp_val == self:
                    setattr(old_value, "FeatureDiagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureDiagram"):
                opp_val = getattr(value, "FeatureDiagram", None)
                setattr(value, "FeatureDiagram", self)
