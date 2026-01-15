from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Feature:

    pass
class featuretree_TreeFeature(Feature):

    def __init__(self, mandatory: bool, featuretree_TreeFeature: "featuretree_FeatureTree" = None, featuretree_TreeFeature3: "featuretree_TreeFeature" = None, featuretree_TreeFeature1: set["featuretree_TreeFeature"] = None):
        self.mandatory = mandatory
        self.featuretree_TreeFeature = featuretree_TreeFeature
        self.featuretree_TreeFeature3 = featuretree_TreeFeature3
        self.featuretree_TreeFeature1 = featuretree_TreeFeature1 if featuretree_TreeFeature1 is not None else set()
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def featuretree_TreeFeature(self):
        return self.__featuretree_TreeFeature

    @featuretree_TreeFeature.setter
    def featuretree_TreeFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuretree_TreeFeature__featuretree_TreeFeature", None)
        self.__featuretree_TreeFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuretree_FeatureTree"):
                opp_val = getattr(old_value, "featuretree_FeatureTree", None)
                if opp_val == self:
                    setattr(old_value, "featuretree_FeatureTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuretree_FeatureTree"):
                opp_val = getattr(value, "featuretree_FeatureTree", None)
                setattr(value, "featuretree_FeatureTree", self)

    @property
    def featuretree_TreeFeature3(self):
        return self.__featuretree_TreeFeature3

    @featuretree_TreeFeature3.setter
    def featuretree_TreeFeature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuretree_TreeFeature__featuretree_TreeFeature3", None)
        self.__featuretree_TreeFeature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuretree_TreeFeature1"):
                opp_val = getattr(old_value, "featuretree_TreeFeature1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuretree_TreeFeature1"):
                opp_val = getattr(value, "featuretree_TreeFeature1", None)
                if opp_val is None:
                    setattr(value, "featuretree_TreeFeature1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuretree_TreeFeature1(self):
        return self.__featuretree_TreeFeature1

    @featuretree_TreeFeature1.setter
    def featuretree_TreeFeature1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuretree_TreeFeature__featuretree_TreeFeature1", None)
        self.__featuretree_TreeFeature1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuretree_TreeFeature3"):
                    opp_val = getattr(item, "featuretree_TreeFeature3", None)
                    
                    if opp_val == self:
                        setattr(item, "featuretree_TreeFeature3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuretree_TreeFeature3"):
                    opp_val = getattr(item, "featuretree_TreeFeature3", None)
                    
                    setattr(item, "featuretree_TreeFeature3", self)
                    

class core_ITopLevelElement:

    pass
class features_IFeatureDomain:

    pass
class core_AbstractModelElement:

    pass
class featuretree_FeatureTree(features_IFeatureDomain, core_ITopLevelElement, core_AbstractModelElement):

    pass