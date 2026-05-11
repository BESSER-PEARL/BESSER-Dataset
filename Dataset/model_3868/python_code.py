from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class COREFeatureRelationshipType(Enum):
    Optional = "Optional"
    Mandatory = "Mandatory"
    XOR = "XOR"
    OR = "OR"
class COREFeatureSelectionStatus(Enum):
    NOT_SELECTED_NO_ACTION = "NOT_SELECTED_NO_ACTION"
    USER_SELECTED = "USER_SELECTED"
    AUTO_SELECTED = "AUTO_SELECTED"
    NOT_SELECTED_ACTION_REQUIRED = "NOT_SELECTED_ACTION_REQUIRED"
    WARNING_USER_SELECTED = "WARNING_USER_SELECTED"
    WARNING_AUTO_SELECTED = "WARNING_AUTO_SELECTED"
    REEXPOSE_USER_SELECTED = "REEXPOSE_USER_SELECTED"
    REEXPOSE_AUTO_SELECTED = "REEXPOSE_AUTO_SELECTED"


############################################
# Definition of Classes
############################################

class core_CORENamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class core_CORECompositionSpecification(ABC):

    pass
class core_COREInterface:

    pass
class COREModel:

    pass
class core_COREFeatureModel(COREModel):

    def __init__(self):
        
        pass
    def getLocalRoot(self) :
        # TODO: Implement getLocalRoot method
        pass

    def getGlobalRoot(self) :
        # TODO: Implement getGlobalRoot method
        pass

class core_COREImpactModel(COREModel):

    pass
class core_COREModelReuse:

    pass
class CORENamedElement:

    pass
class core_COREModelElement(CORENamedElement):

    pass
class core_COREConfiguration(CORENamedElement):

    pass
class core_COREConcern(CORENamedElement):

    pass
class core_COREMapping(ABC):

    pass
class CORECompositionSpecification:

    pass
class core_COREPattern(CORECompositionSpecification):

    pass
class core_COREBinding(CORECompositionSpecification):

    pass
class core_COREReuse:

    pass
class COREModelElement:

    pass
class core_COREImpactModelElement(COREModelElement):

    pass
class core_COREFeature(COREModelElement):

    def __init__(self, realizes: set["core_COREModel"] = None, core_COREFeature: set["core_COREReuse"] = None, COREFeature: "core_COREModel" = None, core_COREFeature21: "core_COREInterface" = None, core_COREFeature43: "core_COREConfiguration" = None, core_COREFeature46: "core_COREConfiguration" = None):
        self.realizes = realizes if realizes is not None else set()
        self.core_COREFeature = core_COREFeature if core_COREFeature is not None else set()
        self.COREFeature = COREFeature
        self.core_COREFeature21 = core_COREFeature21
        self.core_COREFeature43 = core_COREFeature43
        self.core_COREFeature46 = core_COREFeature46
        
        pass
    @property
    def core_COREFeature21(self):
        return self.__core_COREFeature21

    @core_COREFeature21.setter
    def core_COREFeature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature21", None)
        self.__core_COREFeature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREInterface20"):
                opp_val = getattr(old_value, "core_COREInterface20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREInterface20"):
                opp_val = getattr(value, "core_COREInterface20", None)
                if opp_val is None:
                    setattr(value, "core_COREInterface20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREFeature43(self):
        return self.__core_COREFeature43

    @core_COREFeature43.setter
    def core_COREFeature43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature43", None)
        self.__core_COREFeature43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREConfiguration42"):
                opp_val = getattr(old_value, "core_COREConfiguration42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREConfiguration42"):
                opp_val = getattr(value, "core_COREConfiguration42", None)
                if opp_val is None:
                    setattr(value, "core_COREConfiguration42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def COREFeature(self):
        return self.__COREFeature

    @COREFeature.setter
    def COREFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__COREFeature", None)
        self.__COREFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realizedBy"):
                opp_val = getattr(old_value, "realizedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realizedBy"):
                opp_val = getattr(value, "realizedBy", None)
                if opp_val is None:
                    setattr(value, "realizedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def realizes(self):
        return self.__realizes

    @realizes.setter
    def realizes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__realizes", None)
        self.__realizes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "COREModel"):
                    opp_val = getattr(item, "COREModel", None)
                    
                    if opp_val == self:
                        setattr(item, "COREModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "COREModel"):
                    opp_val = getattr(item, "COREModel", None)
                    
                    setattr(item, "COREModel", self)
                    

    @property
    def core_COREFeature46(self):
        return self.__core_COREFeature46

    @core_COREFeature46.setter
    def core_COREFeature46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature46", None)
        self.__core_COREFeature46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREConfiguration45"):
                opp_val = getattr(old_value, "core_COREConfiguration45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREConfiguration45"):
                opp_val = getattr(value, "core_COREConfiguration45", None)
                if opp_val is None:
                    setattr(value, "core_COREConfiguration45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREFeature(self):
        return self.__core_COREFeature

    @core_COREFeature.setter
    def core_COREFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature", None)
        self.__core_COREFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_COREReuse"):
                    opp_val = getattr(item, "core_COREReuse", None)
                    
                    if opp_val == self:
                        setattr(item, "core_COREReuse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_COREReuse"):
                    opp_val = getattr(item, "core_COREReuse", None)
                    
                    setattr(item, "core_COREReuse", self)
                    

    def addRealizedBy(self, core_model) :
        # TODO: Implement addRealizedBy method
        pass

    def AssociateReuse(self, core_reuse, core_reexposed, core_selected) :
        # TODO: Implement AssociateReuse method
        pass

    def addFeature(self, core_position, core_child_name, core_association) :
        # TODO: Implement addFeature method
        pass

    def changeParent(self, core_feature, core_new_association) :
        # TODO: Implement changeParent method
        pass

    def rename(self, core_core_feature_name):
        # TODO: Implement rename method
        pass

    def delete(self) :
        # TODO: Implement delete method
        pass

    def removeConstraint(self, core_feature) :
        # TODO: Implement removeConstraint method
        pass

    def excludes(self, core_feature) :
        # TODO: Implement excludes method
        pass

    def requires(self, core_feature) :
        # TODO: Implement requires method
        pass

    def changeLink(self, core_new_association) :
        # TODO: Implement changeLink method
        pass

class core_COREModel(CORENamedElement):

    pass