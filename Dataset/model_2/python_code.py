from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Confidentiality(Enum):
    UNKNOWN = "UNKNOWN"
    LOW = "LOW"
    HIGH = "HIGH"
class NodeType(Enum):
    internal = "internal"
    input = "input"
    output = "output"
    inout = "inout"


############################################
# Definition of Classes
############################################

class ArcToTransition:

    pass
class ptnetLoLA_ArcToTransitionExt(ArcToTransition):

    def __init__(self, probability: float):
        self.probability = probability
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

class ArcToPlace:

    pass
class ptnetLoLA_ArcToPlaceExt(ArcToPlace):

    def __init__(self, probability: float):
        self.probability = probability
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

class Place:

    pass
class ptnetLoLA_PlaceExt(Place):

    def __init__(self, probability: float, isStart: bool):
        self.probability = probability
        self.isStart = isStart
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def isStart(self) -> bool:
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart

class Transition:

    pass
class ptnetLoLA_TransitionExt(Transition):

    def __init__(self, probability: float, minTime: int, cost: float, maxTime: int, confidentiality: str):
        self.probability = probability
        self.minTime = minTime
        self.cost = cost
        self.maxTime = maxTime
        self.confidentiality = confidentiality
        
    @property
    def confidentiality(self) -> str:
        return self.__confidentiality

    @confidentiality.setter
    def confidentiality(self, confidentiality: str):
        self.__confidentiality = confidentiality

    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def cost(self) -> float:
        return self.__cost

    @cost.setter
    def cost(self, cost: float):
        self.__cost = cost

    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

class Arc:

    pass
class ptnetLoLA_ArcToTransition(Arc):

    pass
class ptnetLoLA_ArcToPlace(Arc):

    pass
class PlaceReference:

    pass
class ptnetLoLA_PlaceReference:

    pass
class ptnetLoLA_RefMarkedPlace(PlaceReference):

    def __init__(self, token: int, ptnetLoLA_RefMarkedPlace: "ptnetLoLA_Marking" = None):
        self.token = token
        self.ptnetLoLA_RefMarkedPlace = ptnetLoLA_RefMarkedPlace
        
    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def ptnetLoLA_RefMarkedPlace(self):
        return self.__ptnetLoLA_RefMarkedPlace

    @ptnetLoLA_RefMarkedPlace.setter
    def ptnetLoLA_RefMarkedPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_RefMarkedPlace__ptnetLoLA_RefMarkedPlace", None)
        self.__ptnetLoLA_RefMarkedPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_Marking18"):
                opp_val = getattr(old_value, "ptnetLoLA_Marking18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_Marking18"):
                opp_val = getattr(value, "ptnetLoLA_Marking18", None)
                if opp_val is None:
                    setattr(value, "ptnetLoLA_Marking18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ptnetLoLA_Node:

    def __init__(self, name: str, type: str, ptnetLoLA_Node: "ptnetLoLA_Annotation" = None, target: set["ptnetLoLA_Arc"] = None, source: set["ptnetLoLA_Arc"] = None, Node: "ptnetLoLA_Arc" = None, Node23: "ptnetLoLA_Arc" = None):
        self.name = name
        self.type = type
        self.ptnetLoLA_Node = ptnetLoLA_Node
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node = Node
        self.Node23 = Node23
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def Node23(self):
        return self.__Node23

    @Node23.setter
    def Node23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Node__Node23", None)
        self.__Node23 = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc16"):
                    opp_val = getattr(item, "Arc16", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc16"):
                    opp_val = getattr(item, "Arc16", None)
                    
                    setattr(item, "Arc16", self)
                    

    @property
    def ptnetLoLA_Node(self):
        return self.__ptnetLoLA_Node

    @ptnetLoLA_Node.setter
    def ptnetLoLA_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Node__ptnetLoLA_Node", None)
        self.__ptnetLoLA_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_Annotation13"):
                opp_val = getattr(old_value, "ptnetLoLA_Annotation13", None)
                if opp_val == self:
                    setattr(old_value, "ptnetLoLA_Annotation13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_Annotation13"):
                opp_val = getattr(value, "ptnetLoLA_Annotation13", None)
                setattr(value, "ptnetLoLA_Annotation13", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Node__Node", None)
        self.__Node = value
        
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

class ptnetLoLA_Marking:

    pass
class ptnetLoLA_PtNet:

    pass
class Node:

    pass
class ptnetLoLA_Transition(Node):

    pass
class ptnetLoLA_Place(Node):

    def __init__(self, token: int, finalMarking: int, ptnetLoLA_Place: "ptnetLoLA_PtNet" = None, ptnetLoLA_Place20: "ptnetLoLA_PlaceReference" = None):
        self.token = token
        self.finalMarking = finalMarking
        self.ptnetLoLA_Place = ptnetLoLA_Place
        self.ptnetLoLA_Place20 = ptnetLoLA_Place20
        
    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def finalMarking(self) -> int:
        return self.__finalMarking

    @finalMarking.setter
    def finalMarking(self, finalMarking: int):
        self.__finalMarking = finalMarking

    @property
    def ptnetLoLA_Place20(self):
        return self.__ptnetLoLA_Place20

    @ptnetLoLA_Place20.setter
    def ptnetLoLA_Place20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Place__ptnetLoLA_Place20", None)
        self.__ptnetLoLA_Place20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_PlaceReference"):
                opp_val = getattr(old_value, "ptnetLoLA_PlaceReference", None)
                if opp_val == self:
                    setattr(old_value, "ptnetLoLA_PlaceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_PlaceReference"):
                opp_val = getattr(value, "ptnetLoLA_PlaceReference", None)
                setattr(value, "ptnetLoLA_PlaceReference", self)

    @property
    def ptnetLoLA_Place(self):
        return self.__ptnetLoLA_Place

    @ptnetLoLA_Place.setter
    def ptnetLoLA_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Place__ptnetLoLA_Place", None)
        self.__ptnetLoLA_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_PtNet"):
                opp_val = getattr(old_value, "ptnetLoLA_PtNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_PtNet"):
                opp_val = getattr(value, "ptnetLoLA_PtNet", None)
                if opp_val is None:
                    setattr(value, "ptnetLoLA_PtNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ptnetLoLA_Arc:

    def __init__(self, weight: int, ptnetLoLA_Arc: "ptnetLoLA_PtNet" = None, Arc: "ptnetLoLA_Node" = None, Arc16: "ptnetLoLA_Node" = None, outgoing: "ptnetLoLA_Node" = None, incoming: "ptnetLoLA_Node" = None):
        self.weight = weight
        self.ptnetLoLA_Arc = ptnetLoLA_Arc
        self.Arc = Arc
        self.Arc16 = Arc16
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Arc__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node23"):
                opp_val = getattr(old_value, "Node23", None)
                if opp_val == self:
                    setattr(old_value, "Node23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node23"):
                opp_val = getattr(value, "Node23", None)
                setattr(value, "Node23", self)

    @property
    def Arc16(self):
        return self.__Arc16

    @Arc16.setter
    def Arc16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Arc__Arc16", None)
        self.__Arc16 = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Arc__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def ptnetLoLA_Arc(self):
        return self.__ptnetLoLA_Arc

    @ptnetLoLA_Arc.setter
    def ptnetLoLA_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Arc__ptnetLoLA_Arc", None)
        self.__ptnetLoLA_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_PtNet8"):
                opp_val = getattr(old_value, "ptnetLoLA_PtNet8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_PtNet8"):
                opp_val = getattr(value, "ptnetLoLA_PtNet8", None)
                if opp_val is None:
                    setattr(value, "ptnetLoLA_PtNet8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ptnetLoLA_Annotation:

    def __init__(self, text: str, ptnetLoLA_Annotation: "ptnetLoLA_PtNet" = None, ptnetLoLA_Annotation13: "ptnetLoLA_Node" = None):
        self.text = text
        self.ptnetLoLA_Annotation = ptnetLoLA_Annotation
        self.ptnetLoLA_Annotation13 = ptnetLoLA_Annotation13
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ptnetLoLA_Annotation(self):
        return self.__ptnetLoLA_Annotation

    @ptnetLoLA_Annotation.setter
    def ptnetLoLA_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Annotation__ptnetLoLA_Annotation", None)
        self.__ptnetLoLA_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_PtNet6"):
                opp_val = getattr(old_value, "ptnetLoLA_PtNet6", None)
                if opp_val == self:
                    setattr(old_value, "ptnetLoLA_PtNet6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_PtNet6"):
                opp_val = getattr(value, "ptnetLoLA_PtNet6", None)
                setattr(value, "ptnetLoLA_PtNet6", self)

    @property
    def ptnetLoLA_Annotation13(self):
        return self.__ptnetLoLA_Annotation13

    @ptnetLoLA_Annotation13.setter
    def ptnetLoLA_Annotation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnetLoLA_Annotation__ptnetLoLA_Annotation13", None)
        self.__ptnetLoLA_Annotation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptnetLoLA_Node"):
                opp_val = getattr(old_value, "ptnetLoLA_Node", None)
                if opp_val == self:
                    setattr(old_value, "ptnetLoLA_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptnetLoLA_Node"):
                opp_val = getattr(value, "ptnetLoLA_Node", None)
                setattr(value, "ptnetLoLA_Node", self)
