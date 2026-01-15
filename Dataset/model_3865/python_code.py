from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class COREVisibilityType(Enum):
    public = "public"
    concern = "concern"
class COREFeatureRelationshipType(Enum):
    None = "None"
    Optional = "Optional"
    Mandatory = "Mandatory"
    XOR = "XOR"
    OR = "OR"
class COREPartialityType(Enum):
    none = "none"
    public = "public"
    concern = "concern"


############################################
# Definition of Classes
############################################

class COREConfiguration:

    pass
class core_COREImpactModelBinding:

    pass
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
            if hasattr(old_value, "core_LayoutMap96"):
                opp_val = getattr(old_value, "core_LayoutMap96", None)
                if opp_val == self:
                    setattr(old_value, "core_LayoutMap96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_LayoutMap96"):
                opp_val = getattr(value, "core_LayoutMap96", None)
                setattr(value, "core_LayoutMap96", self)

class core_EObject:

    pass
class core_LayoutMap:

    pass
class core_COREModelCompositionSpecification(ABC):

    pass
class core_COREWeightedMapping:

    def __init__(self, weight: int, core_COREWeightedMapping: "core_COREFeatureImpactNode" = None):
        self.weight = weight
        self.core_COREWeightedMapping = core_COREWeightedMapping
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def core_COREWeightedMapping(self):
        return self.__core_COREWeightedMapping

    @core_COREWeightedMapping.setter
    def core_COREWeightedMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREWeightedMapping__core_COREWeightedMapping", None)
        self.__core_COREWeightedMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureImpactNode106"):
                opp_val = getattr(old_value, "core_COREFeatureImpactNode106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureImpactNode106"):
                opp_val = getattr(value, "core_COREFeatureImpactNode106", None)
                if opp_val is None:
                    setattr(value, "core_COREFeatureImpactNode106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class COREImpactNode:

    pass
class core_COREFeatureImpactNode(COREImpactNode):

    def __init__(self, relativeFeatureWeight: int, core_COREFeatureImpactNode: "core_COREFeature" = None, core_COREFeatureImpactNode106: set["core_COREWeightedMapping"] = None):
        self.relativeFeatureWeight = relativeFeatureWeight
        self.core_COREFeatureImpactNode = core_COREFeatureImpactNode
        self.core_COREFeatureImpactNode106 = core_COREFeatureImpactNode106 if core_COREFeatureImpactNode106 is not None else set()
        
    @property
    def relativeFeatureWeight(self) -> int:
        return self.__relativeFeatureWeight

    @relativeFeatureWeight.setter
    def relativeFeatureWeight(self, relativeFeatureWeight: int):
        self.__relativeFeatureWeight = relativeFeatureWeight

    @property
    def core_COREFeatureImpactNode(self):
        return self.__core_COREFeatureImpactNode

    @core_COREFeatureImpactNode.setter
    def core_COREFeatureImpactNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeatureImpactNode__core_COREFeatureImpactNode", None)
        self.__core_COREFeatureImpactNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeature104"):
                opp_val = getattr(old_value, "core_COREFeature104", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeature104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeature104"):
                opp_val = getattr(value, "core_COREFeature104", None)
                setattr(value, "core_COREFeature104", self)

    @property
    def core_COREFeatureImpactNode106(self):
        return self.__core_COREFeatureImpactNode106

    @core_COREFeatureImpactNode106.setter
    def core_COREFeatureImpactNode106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeatureImpactNode__core_COREFeatureImpactNode106", None)
        self.__core_COREFeatureImpactNode106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_COREWeightedMapping"):
                    opp_val = getattr(item, "core_COREWeightedMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "core_COREWeightedMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_COREWeightedMapping"):
                    opp_val = getattr(item, "core_COREWeightedMapping", None)
                    
                    setattr(item, "core_COREWeightedMapping", self)
                    

class core_COREPattern(ABC):

    pass
class core_COREReuseConfiguration(COREConfiguration):

    pass
class core_COREConfiguration(ABC):

    pass
class core_COREConcernConfiguration(COREConfiguration):

    pass
class core_CORECompositionSpecification(ABC):

    pass
class core_COREBinding(ABC):

    pass
class core_CORERelativity_Opt2:

    def __init__(self, probabilisticValue: float, CORERelativity_Opt2: "core_COREFeature" = None, CORERelativity_Opt236: "core_COREFeature" = None, core_CORERelativity_Opt2: "core_COREFeatureModel" = None, incoming120: "core_COREFeature" = None, outgoing117: "core_COREFeature" = None):
        self.probabilisticValue = probabilisticValue
        self.CORERelativity_Opt2 = CORERelativity_Opt2
        self.CORERelativity_Opt236 = CORERelativity_Opt236
        self.core_CORERelativity_Opt2 = core_CORERelativity_Opt2
        self.incoming120 = incoming120
        self.outgoing117 = outgoing117
        
    @property
    def probabilisticValue(self) -> float:
        return self.__probabilisticValue

    @probabilisticValue.setter
    def probabilisticValue(self, probabilisticValue: float):
        self.__probabilisticValue = probabilisticValue

    @property
    def CORERelativity_Opt236(self):
        return self.__CORERelativity_Opt236

    @CORERelativity_Opt236.setter
    def CORERelativity_Opt236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity_Opt2__CORERelativity_Opt236", None)
        self.__CORERelativity_Opt236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                if opp_val is None:
                    setattr(value, "features", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CORERelativity_Opt2(self):
        return self.__CORERelativity_Opt2

    @CORERelativity_Opt2.setter
    def CORERelativity_Opt2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity_Opt2__CORERelativity_Opt2", None)
        self.__CORERelativity_Opt2 = value
        
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
    def incoming120(self):
        return self.__incoming120

    @incoming120.setter
    def incoming120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity_Opt2__incoming120", None)
        self.__incoming120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "COREFeature121"):
                opp_val = getattr(old_value, "COREFeature121", None)
                if opp_val == self:
                    setattr(old_value, "COREFeature121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREFeature121"):
                opp_val = getattr(value, "COREFeature121", None)
                setattr(value, "COREFeature121", self)

    @property
    def outgoing117(self):
        return self.__outgoing117

    @outgoing117.setter
    def outgoing117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity_Opt2__outgoing117", None)
        self.__outgoing117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "COREFeature118"):
                opp_val = getattr(old_value, "COREFeature118", None)
                if opp_val == self:
                    setattr(old_value, "COREFeature118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREFeature118"):
                opp_val = getattr(value, "COREFeature118", None)
                setattr(value, "COREFeature118", self)

    @property
    def core_CORERelativity_Opt2(self):
        return self.__core_CORERelativity_Opt2

    @core_CORERelativity_Opt2.setter
    def core_CORERelativity_Opt2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity_Opt2__core_CORERelativity_Opt2", None)
        self.__core_CORERelativity_Opt2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureModel87"):
                opp_val = getattr(old_value, "core_COREFeatureModel87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureModel87"):
                opp_val = getattr(value, "core_COREFeatureModel87", None)
                if opp_val is None:
                    setattr(value, "core_COREFeatureModel87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class core_COREContribution:

    def __init__(self, relativeWeight: int, core_COREContribution: "core_COREImpactModel" = None, COREContribution: "core_COREImpactNode" = None, COREContribution65: "core_COREImpactNode" = None, outgoing: "core_COREImpactNode" = None, incoming: "core_COREImpactNode" = None):
        self.relativeWeight = relativeWeight
        self.core_COREContribution = core_COREContribution
        self.COREContribution = COREContribution
        self.COREContribution65 = COREContribution65
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def relativeWeight(self) -> int:
        return self.__relativeWeight

    @relativeWeight.setter
    def relativeWeight(self, relativeWeight: int):
        self.__relativeWeight = relativeWeight

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
            if hasattr(old_value, "COREImpactNode"):
                opp_val = getattr(old_value, "COREImpactNode", None)
                if opp_val == self:
                    setattr(old_value, "COREImpactNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREImpactNode"):
                opp_val = getattr(value, "COREImpactNode", None)
                setattr(value, "COREImpactNode", self)

    @property
    def COREContribution65(self):
        return self.__COREContribution65

    @COREContribution65.setter
    def COREContribution65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__COREContribution65", None)
        self.__COREContribution65 = value
        
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
    def COREContribution(self):
        return self.__COREContribution

    @COREContribution.setter
    def COREContribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__COREContribution", None)
        self.__COREContribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source63"):
                opp_val = getattr(old_value, "source63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source63"):
                opp_val = getattr(value, "source63", None)
                if opp_val is None:
                    setattr(value, "source63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREContribution__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "COREImpactNode93"):
                opp_val = getattr(old_value, "COREImpactNode93", None)
                if opp_val == self:
                    setattr(old_value, "COREImpactNode93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "COREImpactNode93"):
                opp_val = getattr(value, "COREImpactNode93", None)
                setattr(value, "COREImpactNode93", self)

class core_LayoutContainerMap:

    pass
class COREModel:

    pass
class core_COREImpactModel(COREModel):

    pass
class core_COREModelReuse:

    pass
class CORENamedElement:

    pass
class core_COREConcern(CORENamedElement):

    pass
class core_COREModelElement(CORENamedElement):

    def __init__(self, partiality: str, visibility: str, core_COREModelElement: "core_COREModel" = None, core_COREModelElement42: "core_COREInterface" = None, core_COREModelElement45: "core_COREInterface" = None):
        self.partiality = partiality
        self.visibility = visibility
        self.core_COREModelElement = core_COREModelElement
        self.core_COREModelElement42 = core_COREModelElement42
        self.core_COREModelElement45 = core_COREModelElement45
        
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
    def core_COREModelElement45(self):
        return self.__core_COREModelElement45

    @core_COREModelElement45.setter
    def core_COREModelElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREModelElement__core_COREModelElement45", None)
        self.__core_COREModelElement45 = value
        
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

class core_COREReuse(CORENamedElement):

    pass
class COREModelElement:

    pass
class core_COREFeature(COREModelElement):

    def __init__(self, parentRelationship: str, realizes: set["core_COREModel"] = None, core_COREFeature: set["core_COREReuse"] = None, COREFeature: "core_COREModel" = None, core_COREFeature39: "core_COREInterface" = None, COREFeature22: "core_COREFeature" = None, parent: set["core_COREFeature"] = None, COREFeature25: "core_COREFeature" = None, children: "core_COREFeature" = None, core_COREFeature28: "core_COREFeature" = None, core_COREFeature26: set["core_COREFeature"] = None, core_COREFeature31: "core_COREFeature" = None, core_COREFeature29: set["core_COREFeature"] = None, core_COREFeature33: set["core_CORERelativity"] = None, source: set["core_CORERelativity_Opt2"] = None, features: set["core_CORERelativity_Opt2"] = None, core_COREFeature71: "core_COREConfiguration" = None, core_COREFeature77: "core_COREFeatureModel" = None, core_COREFeature80: "core_COREFeatureModel" = None, core_COREFeature68: "core_COREConfiguration" = None, core_COREFeature104: "core_COREFeatureImpactNode" = None, COREFeature121: "core_CORERelativity_Opt2" = None, core_COREFeature115: "core_CORERelativity" = None, COREFeature118: "core_CORERelativity_Opt2" = None):
        self.parentRelationship = parentRelationship
        self.realizes = realizes if realizes is not None else set()
        self.core_COREFeature = core_COREFeature if core_COREFeature is not None else set()
        self.COREFeature = COREFeature
        self.core_COREFeature39 = core_COREFeature39
        self.COREFeature22 = COREFeature22
        self.parent = parent if parent is not None else set()
        self.COREFeature25 = COREFeature25
        self.children = children
        self.core_COREFeature28 = core_COREFeature28
        self.core_COREFeature26 = core_COREFeature26 if core_COREFeature26 is not None else set()
        self.core_COREFeature31 = core_COREFeature31
        self.core_COREFeature29 = core_COREFeature29 if core_COREFeature29 is not None else set()
        self.core_COREFeature33 = core_COREFeature33 if core_COREFeature33 is not None else set()
        self.source = source if source is not None else set()
        self.features = features if features is not None else set()
        self.core_COREFeature71 = core_COREFeature71
        self.core_COREFeature77 = core_COREFeature77
        self.core_COREFeature80 = core_COREFeature80
        self.core_COREFeature68 = core_COREFeature68
        self.core_COREFeature104 = core_COREFeature104
        self.COREFeature121 = COREFeature121
        self.core_COREFeature115 = core_COREFeature115
        self.COREFeature118 = COREFeature118
        
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
    def COREFeature118(self):
        return self.__COREFeature118

    @COREFeature118.setter
    def COREFeature118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__COREFeature118", None)
        self.__COREFeature118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing117"):
                opp_val = getattr(old_value, "outgoing117", None)
                if opp_val == self:
                    setattr(old_value, "outgoing117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing117"):
                opp_val = getattr(value, "outgoing117", None)
                setattr(value, "outgoing117", self)

    @property
    def core_COREFeature39(self):
        return self.__core_COREFeature39

    @core_COREFeature39.setter
    def core_COREFeature39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature39", None)
        self.__core_COREFeature39 = value
        
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
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__features", None)
        self.__features = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CORERelativity_Opt236"):
                    opp_val = getattr(item, "CORERelativity_Opt236", None)
                    
                    if opp_val == self:
                        setattr(item, "CORERelativity_Opt236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CORERelativity_Opt236"):
                    opp_val = getattr(item, "CORERelativity_Opt236", None)
                    
                    setattr(item, "CORERelativity_Opt236", self)
                    

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
    def core_COREFeature104(self):
        return self.__core_COREFeature104

    @core_COREFeature104.setter
    def core_COREFeature104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature104", None)
        self.__core_COREFeature104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureImpactNode"):
                opp_val = getattr(old_value, "core_COREFeatureImpactNode", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeatureImpactNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureImpactNode"):
                opp_val = getattr(value, "core_COREFeatureImpactNode", None)
                setattr(value, "core_COREFeatureImpactNode", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CORERelativity_Opt2"):
                    opp_val = getattr(item, "CORERelativity_Opt2", None)
                    
                    if opp_val == self:
                        setattr(item, "CORERelativity_Opt2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CORERelativity_Opt2"):
                    opp_val = getattr(item, "CORERelativity_Opt2", None)
                    
                    setattr(item, "CORERelativity_Opt2", self)
                    

    @property
    def core_COREFeature71(self):
        return self.__core_COREFeature71

    @core_COREFeature71.setter
    def core_COREFeature71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature71", None)
        self.__core_COREFeature71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREConfiguration70"):
                opp_val = getattr(old_value, "core_COREConfiguration70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREConfiguration70"):
                opp_val = getattr(value, "core_COREConfiguration70", None)
                if opp_val is None:
                    setattr(value, "core_COREConfiguration70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def COREFeature121(self):
        return self.__COREFeature121

    @COREFeature121.setter
    def COREFeature121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__COREFeature121", None)
        self.__COREFeature121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming120"):
                opp_val = getattr(old_value, "incoming120", None)
                if opp_val == self:
                    setattr(old_value, "incoming120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming120"):
                opp_val = getattr(value, "incoming120", None)
                setattr(value, "incoming120", self)

    @property
    def core_COREFeature68(self):
        return self.__core_COREFeature68

    @core_COREFeature68.setter
    def core_COREFeature68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature68", None)
        self.__core_COREFeature68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREConfiguration67"):
                opp_val = getattr(old_value, "core_COREConfiguration67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREConfiguration67"):
                opp_val = getattr(value, "core_COREConfiguration67", None)
                if opp_val is None:
                    setattr(value, "core_COREConfiguration67", set([self]))
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
    def core_COREFeature80(self):
        return self.__core_COREFeature80

    @core_COREFeature80.setter
    def core_COREFeature80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature80", None)
        self.__core_COREFeature80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureModel79"):
                opp_val = getattr(old_value, "core_COREFeatureModel79", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeatureModel79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureModel79"):
                opp_val = getattr(value, "core_COREFeatureModel79", None)
                setattr(value, "core_COREFeatureModel79", self)

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
    def core_COREFeature33(self):
        return self.__core_COREFeature33

    @core_COREFeature33.setter
    def core_COREFeature33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature33", None)
        self.__core_COREFeature33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_CORERelativity"):
                    opp_val = getattr(item, "core_CORERelativity", None)
                    
                    if opp_val == self:
                        setattr(item, "core_CORERelativity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_CORERelativity"):
                    opp_val = getattr(item, "core_CORERelativity", None)
                    
                    setattr(item, "core_CORERelativity", self)
                    

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
    def core_COREFeature77(self):
        return self.__core_COREFeature77

    @core_COREFeature77.setter
    def core_COREFeature77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature77", None)
        self.__core_COREFeature77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeatureModel76"):
                opp_val = getattr(old_value, "core_COREFeatureModel76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeatureModel76"):
                opp_val = getattr(value, "core_COREFeatureModel76", None)
                if opp_val is None:
                    setattr(value, "core_COREFeatureModel76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_COREFeature115(self):
        return self.__core_COREFeature115

    @core_COREFeature115.setter
    def core_COREFeature115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREFeature__core_COREFeature115", None)
        self.__core_COREFeature115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_CORERelativity114"):
                opp_val = getattr(old_value, "core_CORERelativity114", None)
                if opp_val == self:
                    setattr(old_value, "core_CORERelativity114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_CORERelativity114"):
                opp_val = getattr(value, "core_CORERelativity114", None)
                setattr(value, "core_CORERelativity114", self)

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
                    

class core_CORERelativity(COREModelElement):

    def __init__(self, probabilisticValue: float, core_CORERelativity: "core_COREFeature" = None, core_CORERelativity114: "core_COREFeature" = None):
        self.probabilisticValue = probabilisticValue
        self.core_CORERelativity = core_CORERelativity
        self.core_CORERelativity114 = core_CORERelativity114
        
    @property
    def probabilisticValue(self) -> float:
        return self.__probabilisticValue

    @probabilisticValue.setter
    def probabilisticValue(self, probabilisticValue: float):
        self.__probabilisticValue = probabilisticValue

    @property
    def core_CORERelativity114(self):
        return self.__core_CORERelativity114

    @core_CORERelativity114.setter
    def core_CORERelativity114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity__core_CORERelativity114", None)
        self.__core_CORERelativity114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeature115"):
                opp_val = getattr(old_value, "core_COREFeature115", None)
                if opp_val == self:
                    setattr(old_value, "core_COREFeature115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeature115"):
                opp_val = getattr(value, "core_COREFeature115", None)
                setattr(value, "core_COREFeature115", self)

    @property
    def core_CORERelativity(self):
        return self.__core_CORERelativity

    @core_CORERelativity.setter
    def core_CORERelativity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CORERelativity__core_CORERelativity", None)
        self.__core_CORERelativity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREFeature33"):
                opp_val = getattr(old_value, "core_COREFeature33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREFeature33"):
                opp_val = getattr(value, "core_COREFeature33", None)
                if opp_val is None:
                    setattr(value, "core_COREFeature33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_COREImpactNode(COREModelElement):

    def __init__(self, scalingFactor: float, offset: float, core_COREImpactNode: "core_COREImpactModel" = None, core_COREImpactNode48: "core_COREInterface" = None, source63: set["core_COREContribution"] = None, impacts: set["core_COREContribution"] = None, COREImpactNode: "core_COREContribution" = None, COREImpactNode93: "core_COREContribution" = None):
        self.scalingFactor = scalingFactor
        self.offset = offset
        self.core_COREImpactNode = core_COREImpactNode
        self.core_COREImpactNode48 = core_COREImpactNode48
        self.source63 = source63 if source63 is not None else set()
        self.impacts = impacts if impacts is not None else set()
        self.COREImpactNode = COREImpactNode
        self.COREImpactNode93 = COREImpactNode93
        
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
    def COREImpactNode93(self):
        return self.__COREImpactNode93

    @COREImpactNode93.setter
    def COREImpactNode93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactNode__COREImpactNode93", None)
        self.__COREImpactNode93 = value
        
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
    def core_COREImpactNode(self):
        return self.__core_COREImpactNode

    @core_COREImpactNode.setter
    def core_COREImpactNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactNode__core_COREImpactNode", None)
        self.__core_COREImpactNode = value
        
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
    def source63(self):
        return self.__source63

    @source63.setter
    def source63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactNode__source63", None)
        self.__source63 = value if value is not None else set()
        
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
                    

    @property
    def core_COREImpactNode48(self):
        return self.__core_COREImpactNode48

    @core_COREImpactNode48.setter
    def core_COREImpactNode48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactNode__core_COREImpactNode48", None)
        self.__core_COREImpactNode48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_COREInterface47"):
                opp_val = getattr(old_value, "core_COREInterface47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_COREInterface47"):
                opp_val = getattr(value, "core_COREInterface47", None)
                if opp_val is None:
                    setattr(value, "core_COREInterface47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def COREImpactNode(self):
        return self.__COREImpactNode

    @COREImpactNode.setter
    def COREImpactNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactNode__COREImpactNode", None)
        self.__COREImpactNode = value
        
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
    def impacts(self):
        return self.__impacts

    @impacts.setter
    def impacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_COREImpactNode__impacts", None)
        self.__impacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "COREContribution65"):
                    opp_val = getattr(item, "COREContribution65", None)
                    
                    if opp_val == self:
                        setattr(item, "COREContribution65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "COREContribution65"):
                    opp_val = getattr(item, "COREContribution65", None)
                    
                    setattr(item, "COREContribution65", self)
                    

class core_COREFeatureModel(COREModel):

    pass
class core_COREInterface:

    pass
class core_COREModel(CORENamedElement):

    pass