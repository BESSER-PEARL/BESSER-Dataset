from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleIdentifier:

    pass
class feature_SimpleFeature(SimpleIdentifier):

    def __init__(self, valueString: str, feature_SimpleFeature8: "feature_SimpleOntologyTerm" = None, feature_SimpleFeature: "feature_FeatureSet" = None):
        self.valueString = valueString
        self.feature_SimpleFeature8 = feature_SimpleFeature8
        self.feature_SimpleFeature = feature_SimpleFeature
        
    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def feature_SimpleFeature(self):
        return self.__feature_SimpleFeature

    @feature_SimpleFeature.setter
    def feature_SimpleFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_SimpleFeature__feature_SimpleFeature", None)
        self.__feature_SimpleFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_FeatureSet"):
                opp_val = getattr(old_value, "feature_FeatureSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureSet"):
                opp_val = getattr(value, "feature_FeatureSet", None)
                if opp_val is None:
                    setattr(value, "feature_FeatureSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feature_SimpleFeature8(self):
        return self.__feature_SimpleFeature8

    @feature_SimpleFeature8.setter
    def feature_SimpleFeature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_SimpleFeature__feature_SimpleFeature8", None)
        self.__feature_SimpleFeature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_SimpleOntologyTerm9"):
                opp_val = getattr(old_value, "feature_SimpleOntologyTerm9", None)
                if opp_val == self:
                    setattr(old_value, "feature_SimpleOntologyTerm9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_SimpleOntologyTerm9"):
                opp_val = getattr(value, "feature_SimpleOntologyTerm9", None)
                setattr(value, "feature_SimpleOntologyTerm9", self)

class feature_Value:

    pass
class feature_EvidenceCode:

    pass
class feature_SimpleOntologyTerm:

    pass
class feature_SimpleIdentifier:

    pass
class SimpleFeature:

    pass
class feature_Feature(SimpleFeature):

    pass
class feature_FeatureSet(SimpleFeature):

    pass
class feature_AnnotatedSimpleFeature(SimpleFeature):

    pass