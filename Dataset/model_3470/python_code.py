from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Constraint:

    pass
class featureDiagram_Mutex(Constraint):

    pass
class featureDiagram_Require(Constraint):

    pass
class Operator:

    pass
class featureDiagram_Card(Operator):

    pass
class featureDiagram_Xor(Operator):

    pass
class featureDiagram_Or(Operator):

    pass
class featureDiagram_And(Operator):

    pass
class featureDiagram_Opt(Operator):

    pass
class Feature:

    pass
class featureDiagram_PrimitiveFeature(Feature):

    pass
class featureDiagram_Model:

    def __init__(self, name: str, featureDiagram_Model: "featureDiagram_Feature" = None):
        self.name = name
        self.featureDiagram_Model = featureDiagram_Model
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureDiagram_Model(self):
        return self.__featureDiagram_Model

    @featureDiagram_Model.setter
    def featureDiagram_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Model__featureDiagram_Model", None)
        self.__featureDiagram_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_Feature7"):
                opp_val = getattr(old_value, "featureDiagram_Feature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_Feature7"):
                opp_val = getattr(value, "featureDiagram_Feature7", None)
                if opp_val is None:
                    setattr(value, "featureDiagram_Feature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featureDiagram_Operator(ABC):

    pass
class featureDiagram_Constraint(ABC):

    pass
class featureDiagram_Feature:

    def __init__(self, name: str, selected: str, optional: str, featureDiagram_Feature: "featureDiagram_FeatureDiagram" = None, Feature: "featureDiagram_FeatureDiagram" = None, featureDiagram_Feature16: "featureDiagram_ConstraintEdge" = None, featureDiagram_Feature20: "featureDiagram_ConstraintEdge" = None, features: "featureDiagram_FeatureDiagram" = None, owningFeature: "featureDiagram_Operator" = None, featureDiagram_Feature7: set["featureDiagram_Model"] = None, Feature10: "featureDiagram_Feature" = None, parents: set["featureDiagram_Feature"] = None, Feature13: "featureDiagram_Feature" = None, children: set["featureDiagram_Feature"] = None, Feature22: "featureDiagram_Operator" = None):
        self.name = name
        self.selected = selected
        self.optional = optional
        self.featureDiagram_Feature = featureDiagram_Feature
        self.Feature = Feature
        self.featureDiagram_Feature16 = featureDiagram_Feature16
        self.featureDiagram_Feature20 = featureDiagram_Feature20
        self.features = features
        self.owningFeature = owningFeature
        self.featureDiagram_Feature7 = featureDiagram_Feature7 if featureDiagram_Feature7 is not None else set()
        self.Feature10 = Feature10
        self.parents = parents if parents is not None else set()
        self.Feature13 = Feature13
        self.children = children if children is not None else set()
        self.Feature22 = Feature22
        
    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureDiagram_Feature16(self):
        return self.__featureDiagram_Feature16

    @featureDiagram_Feature16.setter
    def featureDiagram_Feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature16", None)
        self.__featureDiagram_Feature16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_ConstraintEdge15"):
                opp_val = getattr(old_value, "featureDiagram_ConstraintEdge15", None)
                if opp_val == self:
                    setattr(old_value, "featureDiagram_ConstraintEdge15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_ConstraintEdge15"):
                opp_val = getattr(value, "featureDiagram_ConstraintEdge15", None)
                setattr(value, "featureDiagram_ConstraintEdge15", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature13"):
                    opp_val = getattr(item, "Feature13", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature13"):
                    opp_val = getattr(item, "Feature13", None)
                    
                    setattr(item, "Feature13", self)
                    

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
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature10"):
                    opp_val = getattr(item, "Feature10", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature10"):
                    opp_val = getattr(item, "Feature10", None)
                    
                    setattr(item, "Feature10", self)
                    

    @property
    def featureDiagram_Feature7(self):
        return self.__featureDiagram_Feature7

    @featureDiagram_Feature7.setter
    def featureDiagram_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature7", None)
        self.__featureDiagram_Feature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureDiagram_Model"):
                    opp_val = getattr(item, "featureDiagram_Model", None)
                    
                    if opp_val == self:
                        setattr(item, "featureDiagram_Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureDiagram_Model"):
                    opp_val = getattr(item, "featureDiagram_Model", None)
                    
                    setattr(item, "featureDiagram_Model", self)
                    

    @property
    def featureDiagram_Feature20(self):
        return self.__featureDiagram_Feature20

    @featureDiagram_Feature20.setter
    def featureDiagram_Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__featureDiagram_Feature20", None)
        self.__featureDiagram_Feature20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureDiagram_ConstraintEdge19"):
                opp_val = getattr(old_value, "featureDiagram_ConstraintEdge19", None)
                if opp_val == self:
                    setattr(old_value, "featureDiagram_ConstraintEdge19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureDiagram_ConstraintEdge19"):
                opp_val = getattr(value, "featureDiagram_ConstraintEdge19", None)
                setattr(value, "featureDiagram_ConstraintEdge19", self)

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
    def owningFeature(self):
        return self.__owningFeature

    @owningFeature.setter
    def owningFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__owningFeature", None)
        self.__owningFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operator"):
                opp_val = getattr(old_value, "Operator", None)
                if opp_val == self:
                    setattr(old_value, "Operator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operator"):
                opp_val = getattr(value, "Operator", None)
                setattr(value, "Operator", self)

    @property
    def Feature10(self):
        return self.__Feature10

    @Feature10.setter
    def Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature10", None)
        self.__Feature10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                if opp_val is None:
                    setattr(value, "parents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    @property
    def Feature13(self):
        return self.__Feature13

    @Feature13.setter
    def Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature13", None)
        self.__Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature22(self):
        return self.__Feature22

    @Feature22.setter
    def Feature22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureDiagram_Feature__Feature22", None)
        self.__Feature22 = value
        
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

class featureDiagram_FeatureDiagram:

    def __init__(self, graphTypeTree: str, featureDiagram_FeatureDiagram: "featureDiagram_Feature" = None, featureDiagram_FeatureDiagram3: set["featureDiagram_ConstraintEdge"] = None, owningFeatureDiagram: set["featureDiagram_Feature"] = None, FeatureDiagram: "featureDiagram_Feature" = None):
        self.graphTypeTree = graphTypeTree
        self.featureDiagram_FeatureDiagram = featureDiagram_FeatureDiagram
        self.featureDiagram_FeatureDiagram3 = featureDiagram_FeatureDiagram3 if featureDiagram_FeatureDiagram3 is not None else set()
        self.owningFeatureDiagram = owningFeatureDiagram if owningFeatureDiagram is not None else set()
        self.FeatureDiagram = FeatureDiagram
        
    @property
    def graphTypeTree(self) -> str:
        return self.__graphTypeTree

    @graphTypeTree.setter
    def graphTypeTree(self, graphTypeTree: str):
        self.__graphTypeTree = graphTypeTree

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
                    

class featureDiagram_ConstraintEdge:

    pass