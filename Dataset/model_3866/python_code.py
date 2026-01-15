from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class COREPartialityType(Enum):
    none = "none"
    public = "public"
    concern = "concern"
class COREFeatureRelationshipType(Enum):
    None = "None"
    Optional = "Optional"
    Mandatory = "Mandatory"
    XOR = "XOR"
    OR = "OR"
class COREVisibilityType(Enum):
    public = "public"
    concern = "concern"


############################################
# Definition of Classes
############################################

class core_COREImpactModelBinding:

    pass
class core_COREWeightedMapping:

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class core_COREModelCompositionSpecification(ABC):

    pass
class COREImpactModelElement:

    pass
class core_COREFeatureImpact(COREImpactModelElement):

    def __init__(self, relativeFeatureWeight: float, core_COREFeatureImpact: "core_COREFeature" = None):
        self.relativeFeatureWeight = relativeFeatureWeight
        self.core_COREFeatureImpact = core_COREFeatureImpact
        
    @property
    def relativeFeatureWeight(self) -> float:
        return self.__relativeFeatureWeight

    @relativeFeatureWeight.setter
    def relativeFeatureWeight(self, relativeFeatureWeight: float):
        self.__relativeFeatureWeight = relativeFeatureWeight

    @property
    def core_COREFeatureImpact(self):
        return self.__core_COREFeatureImpact

    @core_COREFeatureImpact.setter
    def core_COREFeatureImpact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeatureImpact__core_COREFeatureImpact", None)
        self.__core_COREFeatureImpact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeature93"):
                opp_val = getattr(old_value, "core_COREFeature93", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeature93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeature93"):
                opp_val = getattr(value, "core_COREFeature93", None)
                setattr(value, "core_COREFeature93", self)

class core_LayoutElement:

    def __init__(self, x: float, y: float, core_LayoutElement: "core_LayoutMap" = None):
        self.x = x
        self.y = y
        self.core_LayoutElement = core_LayoutElement
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def core_LayoutElement(self):
        return self.__core_LayoutElement

    @core_LayoutElement.setter
    def core_LayoutElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_LayoutElement__core_LayoutElement", None)
        self.__core_LayoutElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_LayoutMap85"):
                opp_val = getattr(old_value, "core_LayoutMap85", None)
                if opp_val == self:
                    setattr(old_value, "core_LayoutMap85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_LayoutMap85"):
                opp_val = getattr(value, "core_LayoutMap85", None)
                setattr(value, "core_LayoutMap85", self)

class core_EObject:

    pass
class core_LayoutMap:

    pass
class core_COREPattern(ABC):

    pass
class core_COREConfiguration:

    pass
class core_CORENamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class core_COREMapping(ABC):

    pass
class core_CORECompositionSpecification(ABC):

    pass
class core_COREBinding(ABC):

    pass
class COREModelElement:

    pass
class core_COREInterface:

    pass
class core_COREContribution:

    def __init__(self, relativeWeight: int, core_COREContribution: "core_COREImpactModel" = None, outgoing: "core_COREImpactModelElement" = None, COREContribution: "core_COREImpactModelElement" = None, COREContribution63: "core_COREImpactModelElement" = None, incoming: "core_COREImpactModelElement" = None):
        self.relativeWeight = relativeWeight
        self.core_COREContribution = core_COREContribution
        self.outgoing = outgoing
        self.COREContribution = COREContribution
        self.COREContribution63 = COREContribution63
        self.incoming = incoming
        
    @property
    def relativeWeight(self) -> int:
        return self.__relativeWeight

    @relativeWeight.setter
    def relativeWeight(self, relativeWeight: int):
        self.__relativeWeight = relativeWeight

    @property
    def core_COREContribution(self):
        return self.__core_COREContribution

    @core_COREContribution.setter
    def core_COREContribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__core_COREContribution", None)
        self.__core_COREContribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREImpactModel9"):
                opp_val = getattr(old_value, "core_COREImpactModel9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREImpactModel9"):
                opp_val = getattr(value, "core_COREImpactModel9", None)
                if opp_val is None:
                    setattr(value, "core_COREImpactModel9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def COREContribution(self):
        return self.__COREContribution

    @COREContribution.setter
    def COREContribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__COREContribution", None)
        self.__COREContribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def COREContribution63(self):
        return self.__COREContribution63

    @COREContribution63.setter
    def COREContribution63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__COREContribution63", None)
        self.__COREContribution63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impacts"):
                opp_val = getattr(old_value, "impacts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impacts"):
                opp_val = getattr(value, "impacts", None)
                if opp_val is None:
                    setattr(value, "impacts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "COREImpactModelElement82"):
                opp_val = getattr(old_value, "COREImpactModelElement82", None)
                if opp_val == self:
                    setattr(old_value, "COREImpactModelElement82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREImpactModelElement82"):
                opp_val = getattr(value, "COREImpactModelElement82", None)
                setattr(value, "COREImpactModelElement82", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "COREImpactModelElement"):
                opp_val = getattr(old_value, "COREImpactModelElement", None)
                if opp_val == self:
                    setattr(old_value, "COREImpactModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREImpactModelElement"):
                opp_val = getattr(value, "COREImpactModelElement", None)
                setattr(value, "COREImpactModelElement", self)

class core_LayoutContainerMap:

    pass
class core_COREImpactModelElement(COREModelElement):

    def __init__(self, scalingFactor: float, offset: float, core_COREImpactModelElement: "core_COREImpactModel" = None, core_COREImpactModelElement45: "core_COREInterface" = None, COREImpactModelElement: "core_COREContribution" = None, source: set["core_COREContribution"] = None, impacts: set["core_COREContribution"] = None, COREImpactModelElement82: "core_COREContribution" = None):
        self.scalingFactor = scalingFactor
        self.offset = offset
        self.core_COREImpactModelElement = core_COREImpactModelElement
        self.core_COREImpactModelElement45 = core_COREImpactModelElement45
        self.COREImpactModelElement = COREImpactModelElement
        self.source = source if source is not None else set()
        self.impacts = impacts if impacts is not None else set()
        self.COREImpactModelElement82 = COREImpactModelElement82
        
    @property
    def offset(self) -> float:
        return self.__offset

    @offset.setter
    def offset(self, offset: float):
        self.__offset = offset

    @property
    def scalingFactor(self) -> float:
        return self.__scalingFactor

    @scalingFactor.setter
    def scalingFactor(self, scalingFactor: float):
        self.__scalingFactor = scalingFactor

    @property
    def COREImpactModelElement(self):
        return self.__COREImpactModelElement

    @COREImpactModelElement.setter
    def COREImpactModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactModelElement__COREImpactModelElement", None)
        self.__COREImpactModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def core_COREImpactModelElement(self):
        return self.__core_COREImpactModelElement

    @core_COREImpactModelElement.setter
    def core_COREImpactModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactModelElement__core_COREImpactModelElement", None)
        self.__core_COREImpactModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREImpactModel"):
                opp_val = getattr(old_value, "core_COREImpactModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREImpactModel"):
                opp_val = getattr(value, "core_COREImpactModel", None)
                if opp_val is None:
                    setattr(value, "core_COREImpactModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def COREImpactModelElement82(self):
        return self.__COREImpactModelElement82

    @COREImpactModelElement82.setter
    def COREImpactModelElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactModelElement__COREImpactModelElement82", None)
        self.__COREImpactModelElement82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def impacts(self):
        return self.__impacts

    @impacts.setter
    def impacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactModelElement__impacts", None)
        self.__impacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "COREContribution63"):
                    opp_val = getattr(item, "COREContribution63", None)
                    
                    if opp_val == self:
                        setattr(item, "COREContribution63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "COREContribution63"):
                    opp_val = getattr(item, "COREContribution63", None)
                    
                    setattr(item, "COREContribution63", self)
                    

    @property
    def core_COREImpactModelElement45(self):
        return self.__core_COREImpactModelElement45

    @core_COREImpactModelElement45.setter
    def core_COREImpactModelElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactModelElement__core_COREImpactModelElement45", None)
        self.__core_COREImpactModelElement45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREInterface44"):
                opp_val = getattr(old_value, "core_COREInterface44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREInterface44"):
                opp_val = getattr(value, "core_COREInterface44", None)
                if opp_val is None:
                    setattr(value, "core_COREInterface44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactModelElement__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "COREContribution"):
                    opp_val = getattr(item, "COREContribution", None)
                    
                    if opp_val == self:
                        setattr(item, "COREContribution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "COREContribution"):
                    opp_val = getattr(item, "COREContribution", None)
                    
                    setattr(item, "COREContribution", self)
                    

class COREModel:

    pass
class core_COREFeatureModel(COREModel):

    pass
class core_COREImpactModel(COREModel):

    pass
class core_COREFeature(COREModelElement):

    def __init__(self, parentRelationship: str, COREFeature: "core_COREModel" = None, COREFeature25: "core_COREFeature" = None, children: "core_COREFeature" = None, core_COREFeature28: "core_COREFeature" = None, core_COREFeature26: set["core_COREFeature"] = None, core_COREFeature31: "core_COREFeature" = None, core_COREFeature29: set["core_COREFeature"] = None, realizes: set["core_COREModel"] = None, core_COREFeature: set["core_COREReuse"] = None, COREFeature22: "core_COREFeature" = None, parent: set["core_COREFeature"] = None, core_COREFeature36: "core_COREInterface" = None, core_COREFeature66: "core_COREConfiguration" = None, core_COREFeature69: "core_COREConfiguration" = None, core_COREFeature75: "core_COREFeatureModel" = None, core_COREFeature78: "core_COREFeatureModel" = None, core_COREFeature93: "core_COREFeatureImpact" = None):
        self.parentRelationship = parentRelationship
        self.COREFeature = COREFeature
        self.COREFeature25 = COREFeature25
        self.children = children
        self.core_COREFeature28 = core_COREFeature28
        self.core_COREFeature26 = core_COREFeature26 if core_COREFeature26 is not None else set()
        self.core_COREFeature31 = core_COREFeature31
        self.core_COREFeature29 = core_COREFeature29 if core_COREFeature29 is not None else set()
        self.realizes = realizes if realizes is not None else set()
        self.core_COREFeature = core_COREFeature if core_COREFeature is not None else set()
        self.COREFeature22 = COREFeature22
        self.parent = parent if parent is not None else set()
        self.core_COREFeature36 = core_COREFeature36
        self.core_COREFeature66 = core_COREFeature66
        self.core_COREFeature69 = core_COREFeature69
        self.core_COREFeature75 = core_COREFeature75
        self.core_COREFeature78 = core_COREFeature78
        self.core_COREFeature93 = core_COREFeature93
        
    @property
    def parentRelationship(self) -> str:
        return self.__parentRelationship

    @parentRelationship.setter
    def parentRelationship(self, parentRelationship: str):
        self.__parentRelationship = parentRelationship

    @property
    def core_COREFeature28(self):
        return self.__core_COREFeature28

    @core_COREFeature28.setter
    def core_COREFeature28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature28", None)
        self.__core_COREFeature28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeature26"):
                opp_val = getattr(old_value, "core_COREFeature26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeature26"):
                opp_val = getattr(value, "core_COREFeature26", None)
                if opp_val is None:
                    setattr(value, "core_COREFeature26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREFeature36(self):
        return self.__core_COREFeature36

    @core_COREFeature36.setter
    def core_COREFeature36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature36", None)
        self.__core_COREFeature36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREInterface35"):
                opp_val = getattr(old_value, "core_COREInterface35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREInterface35"):
                opp_val = getattr(value, "core_COREInterface35", None)
                if opp_val is None:
                    setattr(value, "core_COREInterface35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "COREFeature22"):
                    opp_val = getattr(item, "COREFeature22", None)
                    
                    if opp_val == self:
                        setattr(item, "COREFeature22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "COREFeature22"):
                    opp_val = getattr(item, "COREFeature22", None)
                    
                    setattr(item, "COREFeature22", self)
                    

    @property
    def COREFeature25(self):
        return self.__COREFeature25

    @COREFeature25.setter
    def COREFeature25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__COREFeature25", None)
        self.__COREFeature25 = value
        
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
                    

    @property
    def core_COREFeature26(self):
        return self.__core_COREFeature26

    @core_COREFeature26.setter
    def core_COREFeature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature26", None)
        self.__core_COREFeature26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_COREFeature28"):
                    opp_val = getattr(item, "core_COREFeature28", None)
                    
                    if opp_val == self:
                        setattr(item, "core_COREFeature28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_COREFeature28"):
                    opp_val = getattr(item, "core_COREFeature28", None)
                    
                    setattr(item, "core_COREFeature28", self)
                    

    @property
    def core_COREFeature93(self):
        return self.__core_COREFeature93

    @core_COREFeature93.setter
    def core_COREFeature93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature93", None)
        self.__core_COREFeature93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureImpact"):
                opp_val = getattr(old_value, "core_COREFeatureImpact", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeatureImpact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureImpact"):
                opp_val = getattr(value, "core_COREFeatureImpact", None)
                setattr(value, "core_COREFeatureImpact", self)

    @property
    def core_COREFeature29(self):
        return self.__core_COREFeature29

    @core_COREFeature29.setter
    def core_COREFeature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature29", None)
        self.__core_COREFeature29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_COREFeature31"):
                    opp_val = getattr(item, "core_COREFeature31", None)
                    
                    if opp_val == self:
                        setattr(item, "core_COREFeature31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_COREFeature31"):
                    opp_val = getattr(item, "core_COREFeature31", None)
                    
                    setattr(item, "core_COREFeature31", self)
                    

    @property
    def core_COREFeature75(self):
        return self.__core_COREFeature75

    @core_COREFeature75.setter
    def core_COREFeature75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature75", None)
        self.__core_COREFeature75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureModel74"):
                opp_val = getattr(old_value, "core_COREFeatureModel74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureModel74"):
                opp_val = getattr(value, "core_COREFeatureModel74", None)
                if opp_val is None:
                    setattr(value, "core_COREFeatureModel74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "COREFeature25"):
                opp_val = getattr(old_value, "COREFeature25", None)
                if opp_val == self:
                    setattr(old_value, "COREFeature25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREFeature25"):
                opp_val = getattr(value, "COREFeature25", None)
                setattr(value, "COREFeature25", self)

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
    def core_COREFeature78(self):
        return self.__core_COREFeature78

    @core_COREFeature78.setter
    def core_COREFeature78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature78", None)
        self.__core_COREFeature78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureModel77"):
                opp_val = getattr(old_value, "core_COREFeatureModel77", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeatureModel77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureModel77"):
                opp_val = getattr(value, "core_COREFeatureModel77", None)
                setattr(value, "core_COREFeatureModel77", self)

    @property
    def COREFeature22(self):
        return self.__COREFeature22

    @COREFeature22.setter
    def COREFeature22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__COREFeature22", None)
        self.__COREFeature22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
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
                if hasattr(item, "COREModel18"):
                    opp_val = getattr(item, "COREModel18", None)
                    
                    if opp_val == self:
                        setattr(item, "COREModel18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "COREModel18"):
                    opp_val = getattr(item, "COREModel18", None)
                    
                    setattr(item, "COREModel18", self)
                    

    @property
    def core_COREFeature31(self):
        return self.__core_COREFeature31

    @core_COREFeature31.setter
    def core_COREFeature31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature31", None)
        self.__core_COREFeature31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeature29"):
                opp_val = getattr(old_value, "core_COREFeature29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeature29"):
                opp_val = getattr(value, "core_COREFeature29", None)
                if opp_val is None:
                    setattr(value, "core_COREFeature29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREFeature66(self):
        return self.__core_COREFeature66

    @core_COREFeature66.setter
    def core_COREFeature66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature66", None)
        self.__core_COREFeature66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREConfiguration65"):
                opp_val = getattr(old_value, "core_COREConfiguration65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREConfiguration65"):
                opp_val = getattr(value, "core_COREConfiguration65", None)
                if opp_val is None:
                    setattr(value, "core_COREConfiguration65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREFeature69(self):
        return self.__core_COREFeature69

    @core_COREFeature69.setter
    def core_COREFeature69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature69", None)
        self.__core_COREFeature69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREConfiguration68"):
                opp_val = getattr(old_value, "core_COREConfiguration68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREConfiguration68"):
                opp_val = getattr(value, "core_COREConfiguration68", None)
                if opp_val is None:
                    setattr(value, "core_COREConfiguration68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_COREModelReuse:

    pass
class CORENamedElement:

    pass
class core_COREConcern(CORENamedElement):

    pass
class core_COREReuse(CORENamedElement):

    pass
class core_COREModelElement(CORENamedElement):

    def __init__(self, partiality: str, visibility: str, core_COREModelElement: "core_COREModel" = None, core_COREModelElement39: "core_COREInterface" = None, core_COREModelElement42: "core_COREInterface" = None):
        self.partiality = partiality
        self.visibility = visibility
        self.core_COREModelElement = core_COREModelElement
        self.core_COREModelElement39 = core_COREModelElement39
        self.core_COREModelElement42 = core_COREModelElement42
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def partiality(self) -> str:
        return self.__partiality

    @partiality.setter
    def partiality(self, partiality: str):
        self.__partiality = partiality

    @property
    def core_COREModelElement(self):
        return self.__core_COREModelElement

    @core_COREModelElement.setter
    def core_COREModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREModelElement__core_COREModelElement", None)
        self.__core_COREModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREModel2"):
                opp_val = getattr(old_value, "core_COREModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREModel2"):
                opp_val = getattr(value, "core_COREModel2", None)
                if opp_val is None:
                    setattr(value, "core_COREModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREModelElement39(self):
        return self.__core_COREModelElement39

    @core_COREModelElement39.setter
    def core_COREModelElement39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREModelElement__core_COREModelElement39", None)
        self.__core_COREModelElement39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREInterface38"):
                opp_val = getattr(old_value, "core_COREInterface38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREInterface38"):
                opp_val = getattr(value, "core_COREInterface38", None)
                if opp_val is None:
                    setattr(value, "core_COREInterface38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREModelElement42(self):
        return self.__core_COREModelElement42

    @core_COREModelElement42.setter
    def core_COREModelElement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREModelElement__core_COREModelElement42", None)
        self.__core_COREModelElement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREInterface41"):
                opp_val = getattr(old_value, "core_COREInterface41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREInterface41"):
                opp_val = getattr(value, "core_COREInterface41", None)
                if opp_val is None:
                    setattr(value, "core_COREInterface41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_COREModel(CORENamedElement):

    pass