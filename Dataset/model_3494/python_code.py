from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class feature_DefaultBinding:

    pass
class feature_Preference:

    pass
class FeatureDependency:

    pass
class feature_FeatureExclusion(FeatureDependency):

    pass
class feature_FeatureRequirement(FeatureDependency):

    pass
class FeatureGroup:

    pass
class feature_XorFeatureGroup(FeatureGroup):

    pass
class feature_OrFeatureGroup(FeatureGroup):

    pass
class feature_Invariant:

    pass
class feature_Option:

    pass
class UUIDElement:

    pass
class HybridElement:

    pass
class feature_FeatureDependency(HybridElement, UUIDElement):

    pass
class feature_Elimination(HybridElement):

    def __init__(self, defaultSelection: str, Elimination: "feature_Feature" = None, feature_Elimination61: "feature_DefaultBinding" = None, eliminations: "feature_Feature" = None, feature_Elimination: "feature_Invariant" = None):
        self.defaultSelection = defaultSelection
        self.Elimination = Elimination
        self.feature_Elimination61 = feature_Elimination61
        self.eliminations = eliminations
        self.feature_Elimination = feature_Elimination
        
    @property
    def defaultSelection(self) -> str:
        return self.__defaultSelection

    @defaultSelection.setter
    def defaultSelection(self, defaultSelection: str):
        self.__defaultSelection = defaultSelection

    @property
    def feature_Elimination61(self):
        return self.__feature_Elimination61

    @feature_Elimination61.setter
    def feature_Elimination61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Elimination__feature_Elimination61", None)
        self.__feature_Elimination61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_DefaultBinding62"):
                opp_val = getattr(old_value, "feature_DefaultBinding62", None)
                if opp_val == self:
                    setattr(old_value, "feature_DefaultBinding62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_DefaultBinding62"):
                opp_val = getattr(value, "feature_DefaultBinding62", None)
                setattr(value, "feature_DefaultBinding62", self)

    @property
    def eliminations(self):
        return self.__eliminations

    @eliminations.setter
    def eliminations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Elimination__eliminations", None)
        self.__eliminations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature57"):
                opp_val = getattr(old_value, "Feature57", None)
                if opp_val == self:
                    setattr(old_value, "Feature57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature57"):
                opp_val = getattr(value, "Feature57", None)
                setattr(value, "Feature57", self)

    @property
    def feature_Elimination(self):
        return self.__feature_Elimination

    @feature_Elimination.setter
    def feature_Elimination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Elimination__feature_Elimination", None)
        self.__feature_Elimination = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Invariant59"):
                opp_val = getattr(old_value, "feature_Invariant59", None)
                if opp_val == self:
                    setattr(old_value, "feature_Invariant59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Invariant59"):
                opp_val = getattr(value, "feature_Invariant59", None)
                setattr(value, "feature_Invariant59", self)

    @property
    def Elimination(self):
        return self.__Elimination

    @Elimination.setter
    def Elimination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Elimination__Elimination", None)
        self.__Elimination = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature16"):
                opp_val = getattr(old_value, "feature16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature16"):
                opp_val = getattr(value, "feature16", None)
                if opp_val is None:
                    setattr(value, "feature16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_Mandatory(HybridElement):

    pass
class feature_DisplayName(HybridElement):

    def __init__(self, displayName: str, DisplayName: "feature_Feature" = None, names: "feature_Feature" = None):
        self.displayName = displayName
        self.DisplayName = DisplayName
        self.names = names
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def names(self):
        return self.__names

    @names.setter
    def names(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_DisplayName__names", None)
        self.__names = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature23"):
                opp_val = getattr(old_value, "Feature23", None)
                if opp_val == self:
                    setattr(old_value, "Feature23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature23"):
                opp_val = getattr(value, "Feature23", None)
                setattr(value, "Feature23", self)

    @property
    def DisplayName(self):
        return self.__DisplayName

    @DisplayName.setter
    def DisplayName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_DisplayName__DisplayName", None)
        self.__DisplayName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_FeatureGroup(HybridElement, UUIDElement):

    pass
class feature_ChildRelationship(HybridElement):

    pass
class feature_GroupMembership(HybridElement):

    pass
class feature_Feature(HybridElement, UUIDElement):

    def __init__(self, transitiveEliminationState: str, Feature: "feature_FeatureModel" = None, features: "feature_FeatureModel" = None, child: set["feature_ChildRelationship"] = None, parentFeature: set["feature_FeatureGroup"] = None, groupedFeature: set["feature_GroupMembership"] = None, targetFeature: set["feature_FeatureDependency"] = None, sourceFeature: set["feature_FeatureDependency"] = None, feature14: "feature_Mandatory" = None, feature_Feature: "feature_Option" = None, feature: set["feature_DisplayName"] = None, parent: set["feature_ChildRelationship"] = None, Feature23: "feature_DisplayName" = None, Feature28: "feature_FeatureGroup" = None, feature16: set["feature_Elimination"] = None, feature18: set["feature_RootRelationship"] = None, feature_Feature21: "feature_Feature" = None, feature_Feature19: set["feature_Feature"] = None, Feature36: "feature_FeatureDependency" = None, Feature38: "feature_FeatureDependency" = None, Feature30: "feature_GroupMembership" = None, Feature47: "feature_ChildRelationship" = None, Feature49: "feature_ChildRelationship" = None, Feature55: "feature_Mandatory" = None, Feature45: "feature_RootRelationship" = None, Feature57: "feature_Elimination" = None):
        self.transitiveEliminationState = transitiveEliminationState
        self.Feature = Feature
        self.features = features
        self.child = child if child is not None else set()
        self.parentFeature = parentFeature if parentFeature is not None else set()
        self.groupedFeature = groupedFeature if groupedFeature is not None else set()
        self.targetFeature = targetFeature if targetFeature is not None else set()
        self.sourceFeature = sourceFeature if sourceFeature is not None else set()
        self.feature14 = feature14
        self.feature_Feature = feature_Feature
        self.feature = feature if feature is not None else set()
        self.parent = parent if parent is not None else set()
        self.Feature23 = Feature23
        self.Feature28 = Feature28
        self.feature16 = feature16 if feature16 is not None else set()
        self.feature18 = feature18 if feature18 is not None else set()
        self.feature_Feature21 = feature_Feature21
        self.feature_Feature19 = feature_Feature19 if feature_Feature19 is not None else set()
        self.Feature36 = Feature36
        self.Feature38 = Feature38
        self.Feature30 = Feature30
        self.Feature47 = Feature47
        self.Feature49 = Feature49
        self.Feature55 = Feature55
        self.Feature45 = Feature45
        self.Feature57 = Feature57
        
    @property
    def transitiveEliminationState(self) -> str:
        return self.__transitiveEliminationState

    @transitiveEliminationState.setter
    def transitiveEliminationState(self, transitiveEliminationState: str):
        self.__transitiveEliminationState = transitiveEliminationState

    @property
    def parentFeature(self):
        return self.__parentFeature

    @parentFeature.setter
    def parentFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__parentFeature", None)
        self.__parentFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureGroup"):
                    opp_val = getattr(item, "FeatureGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureGroup"):
                    opp_val = getattr(item, "FeatureGroup", None)
                    
                    setattr(item, "FeatureGroup", self)
                    

    @property
    def Feature57(self):
        return self.__Feature57

    @Feature57.setter
    def Feature57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature57", None)
        self.__Feature57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eliminations"):
                opp_val = getattr(old_value, "eliminations", None)
                if opp_val == self:
                    setattr(old_value, "eliminations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eliminations"):
                opp_val = getattr(value, "eliminations", None)
                setattr(value, "eliminations", self)

    @property
    def targetFeature(self):
        return self.__targetFeature

    @targetFeature.setter
    def targetFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__targetFeature", None)
        self.__targetFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureDependency"):
                    opp_val = getattr(item, "FeatureDependency", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureDependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureDependency"):
                    opp_val = getattr(item, "FeatureDependency", None)
                    
                    setattr(item, "FeatureDependency", self)
                    

    @property
    def Feature30(self):
        return self.__Feature30

    @Feature30.setter
    def Feature30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature30", None)
        self.__Feature30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupedBy"):
                opp_val = getattr(old_value, "groupedBy", None)
                if opp_val == self:
                    setattr(old_value, "groupedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupedBy"):
                opp_val = getattr(value, "groupedBy", None)
                setattr(value, "groupedBy", self)

    @property
    def feature_Feature(self):
        return self.__feature_Feature

    @feature_Feature.setter
    def feature_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature", None)
        self.__feature_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Option"):
                opp_val = getattr(old_value, "feature_Option", None)
                if opp_val == self:
                    setattr(old_value, "feature_Option", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Option"):
                opp_val = getattr(value, "feature_Option", None)
                setattr(value, "feature_Option", self)

    @property
    def Feature45(self):
        return self.__Feature45

    @Feature45.setter
    def Feature45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature45", None)
        self.__Feature45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingRoots"):
                opp_val = getattr(old_value, "incomingRoots", None)
                if opp_val == self:
                    setattr(old_value, "incomingRoots", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingRoots"):
                opp_val = getattr(value, "incomingRoots", None)
                setattr(value, "incomingRoots", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ChildRelationship"):
                    opp_val = getattr(item, "ChildRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "ChildRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ChildRelationship"):
                    opp_val = getattr(item, "ChildRelationship", None)
                    
                    setattr(item, "ChildRelationship", self)
                    

    @property
    def feature16(self):
        return self.__feature16

    @feature16.setter
    def feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature16", None)
        self.__feature16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elimination"):
                    opp_val = getattr(item, "Elimination", None)
                    
                    if opp_val == self:
                        setattr(item, "Elimination", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elimination"):
                    opp_val = getattr(item, "Elimination", None)
                    
                    setattr(item, "Elimination", self)
                    

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__child", None)
        self.__child = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ChildRelationship7"):
                    opp_val = getattr(item, "ChildRelationship7", None)
                    
                    if opp_val == self:
                        setattr(item, "ChildRelationship7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ChildRelationship7"):
                    opp_val = getattr(item, "ChildRelationship7", None)
                    
                    setattr(item, "ChildRelationship7", self)
                    

    @property
    def Feature28(self):
        return self.__Feature28

    @Feature28.setter
    def Feature28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature28", None)
        self.__Feature28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups"):
                opp_val = getattr(old_value, "groups", None)
                if opp_val == self:
                    setattr(old_value, "groups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups"):
                opp_val = getattr(value, "groups", None)
                setattr(value, "groups", self)

    @property
    def Feature49(self):
        return self.__Feature49

    @Feature49.setter
    def Feature49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature49", None)
        self.__Feature49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if opp_val == self:
                    setattr(old_value, "parents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                setattr(value, "parents", self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DisplayName"):
                    opp_val = getattr(item, "DisplayName", None)
                    
                    if opp_val == self:
                        setattr(item, "DisplayName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DisplayName"):
                    opp_val = getattr(item, "DisplayName", None)
                    
                    setattr(item, "DisplayName", self)
                    

    @property
    def feature14(self):
        return self.__feature14

    @feature14.setter
    def feature14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature14", None)
        self.__feature14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mandatory"):
                opp_val = getattr(old_value, "Mandatory", None)
                if opp_val == self:
                    setattr(old_value, "Mandatory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mandatory"):
                opp_val = getattr(value, "Mandatory", None)
                setattr(value, "Mandatory", self)

    @property
    def feature_Feature21(self):
        return self.__feature_Feature21

    @feature_Feature21.setter
    def feature_Feature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature21", None)
        self.__feature_Feature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Feature19"):
                opp_val = getattr(old_value, "feature_Feature19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Feature19"):
                opp_val = getattr(value, "feature_Feature19", None)
                if opp_val is None:
                    setattr(value, "feature_Feature19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature23(self):
        return self.__Feature23

    @Feature23.setter
    def Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature23", None)
        self.__Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "names"):
                opp_val = getattr(old_value, "names", None)
                if opp_val == self:
                    setattr(old_value, "names", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "names"):
                opp_val = getattr(value, "names", None)
                setattr(value, "names", self)

    @property
    def Feature47(self):
        return self.__Feature47

    @Feature47.setter
    def Feature47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature47", None)
        self.__Feature47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def Feature36(self):
        return self.__Feature36

    @Feature36.setter
    def Feature36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature36", None)
        self.__Feature36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingDependencies"):
                opp_val = getattr(old_value, "outgoingDependencies", None)
                if opp_val == self:
                    setattr(old_value, "outgoingDependencies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingDependencies"):
                opp_val = getattr(value, "outgoingDependencies", None)
                setattr(value, "outgoingDependencies", self)

    @property
    def Feature38(self):
        return self.__Feature38

    @Feature38.setter
    def Feature38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature38", None)
        self.__Feature38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingDependencies"):
                opp_val = getattr(old_value, "incomingDependencies", None)
                if opp_val == self:
                    setattr(old_value, "incomingDependencies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingDependencies"):
                opp_val = getattr(value, "incomingDependencies", None)
                setattr(value, "incomingDependencies", self)

    @property
    def feature_Feature19(self):
        return self.__feature_Feature19

    @feature_Feature19.setter
    def feature_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature19", None)
        self.__feature_Feature19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_Feature21"):
                    opp_val = getattr(item, "feature_Feature21", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_Feature21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_Feature21"):
                    opp_val = getattr(item, "feature_Feature21", None)
                    
                    setattr(item, "feature_Feature21", self)
                    

    @property
    def sourceFeature(self):
        return self.__sourceFeature

    @sourceFeature.setter
    def sourceFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__sourceFeature", None)
        self.__sourceFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureDependency12"):
                    opp_val = getattr(item, "FeatureDependency12", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureDependency12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureDependency12"):
                    opp_val = getattr(item, "FeatureDependency12", None)
                    
                    setattr(item, "FeatureDependency12", self)
                    

    @property
    def groupedFeature(self):
        return self.__groupedFeature

    @groupedFeature.setter
    def groupedFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__groupedFeature", None)
        self.__groupedFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GroupMembership"):
                    opp_val = getattr(item, "GroupMembership", None)
                    
                    if opp_val == self:
                        setattr(item, "GroupMembership", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GroupMembership"):
                    opp_val = getattr(item, "GroupMembership", None)
                    
                    setattr(item, "GroupMembership", self)
                    

    @property
    def feature18(self):
        return self.__feature18

    @feature18.setter
    def feature18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature18", None)
        self.__feature18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootRelationship"):
                    opp_val = getattr(item, "RootRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RootRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootRelationship"):
                    opp_val = getattr(item, "RootRelationship", None)
                    
                    setattr(item, "RootRelationship", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel"):
                opp_val = getattr(old_value, "featureModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel"):
                opp_val = getattr(value, "featureModel", None)
                if opp_val is None:
                    setattr(value, "featureModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel"):
                opp_val = getattr(old_value, "FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel"):
                opp_val = getattr(value, "FeatureModel", None)
                setattr(value, "FeatureModel", self)

    @property
    def Feature55(self):
        return self.__Feature55

    @Feature55.setter
    def Feature55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature55", None)
        self.__Feature55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mandatory"):
                opp_val = getattr(old_value, "mandatory", None)
                if opp_val == self:
                    setattr(old_value, "mandatory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mandatory"):
                opp_val = getattr(value, "mandatory", None)
                setattr(value, "mandatory", self)

class feature_RootRelationship(HybridElement):

    pass
class HybridDimension:

    pass
class feature_FeatureModel(HybridDimension):

    pass