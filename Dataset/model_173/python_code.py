from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ESynchronizationKind(Enum):
    VerticalSynchronization = "VerticalSynchronization"
    HorizontalSynchronization = "HorizontalSynchronization"


############################################
# Definition of Classes
############################################

class NPNSymbolPlaceSN:

    pass
class NPNSymbolTransitionSN:

    pass
class NPNSymbolArcTPSN:

    pass
class NPNSymbolArcPTSN:

    pass
class NPNSymbolArcSN:

    pass
class highlevelnets_npndiagrams_NPNSymbolArcPTSN(NPNSymbolArcSN):

    pass
class highlevelnets_npndiagrams_NPNSymbolArcTPSN(NPNSymbolArcSN):

    pass
class NPNSymbolTokenSN:

    pass
class highlevelnets_common_IEntityIdentifiable(ABC):

    def __init__(self, uuid: str):
        self.uuid = uuid
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

class NPNSymbolNodeSN:

    pass
class highlevelnets_npndiagrams_NPNSymbolPlaceSN(NPNSymbolNodeSN):

    pass
class highlevelnets_npndiagrams_NPNSymbolTransitionSN(NPNSymbolNodeSN):

    pass
class NPnetMarked:

    pass
class TransitionSynchronized:

    pass
class NPNDiagramNetSystem:

    pass
class Synchronization:

    pass
class NetConstant:

    pass
class NPnet:

    pass
class Transition:

    pass
class highlevelnets_npnets_TransitionSynchronized(Transition):

    pass
class ArcTP:

    pass
class ArcPT:

    pass
class Arc:

    pass
class highlevelnets_hlpn_ArcPT(Arc):

    pass
class highlevelnets_hlpn_ArcTP(Arc):

    def __init__(self, secondTimeConstraint: int, firstTimeConstraint: int, Transition82: "Transition" = None, Place85: "Place" = None, highlevelnets_hlpn_ArcTP: "TokenVariadicExpression" = None, Arc159: "highlevelnets_npndiagrams_NPNSymbolArcSN", hlpn61: "highlevelnets_hlpn_HighLevelPetriNet"):
        self.secondTimeConstraint = secondTimeConstraint
        self.firstTimeConstraint = firstTimeConstraint
        self.Transition82 = Transition82
        self.Place85 = Place85
        self.highlevelnets_hlpn_ArcTP = highlevelnets_hlpn_ArcTP
        
    @property
    def firstTimeConstraint(self) -> int:
        return self.__firstTimeConstraint

    @firstTimeConstraint.setter
    def firstTimeConstraint(self, firstTimeConstraint: int):
        self.__firstTimeConstraint = firstTimeConstraint

    @property
    def secondTimeConstraint(self) -> int:
        return self.__secondTimeConstraint

    @secondTimeConstraint.setter
    def secondTimeConstraint(self, secondTimeConstraint: int):
        self.__secondTimeConstraint = secondTimeConstraint

    @property
    def Transition82(self):
        return self.__Transition82

    @Transition82.setter
    def Transition82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_hlpn_ArcTP__Transition82", None)
        self.__Transition82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlpn83"):
                opp_val = getattr(old_value, "hlpn83", None)
                if opp_val == self:
                    setattr(old_value, "hlpn83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlpn83"):
                opp_val = getattr(value, "hlpn83", None)
                setattr(value, "hlpn83", self)

    @property
    def Place85(self):
        return self.__Place85

    @Place85.setter
    def Place85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_hlpn_ArcTP__Place85", None)
        self.__Place85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlpn86"):
                opp_val = getattr(old_value, "hlpn86", None)
                if opp_val == self:
                    setattr(old_value, "hlpn86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlpn86"):
                opp_val = getattr(value, "hlpn86", None)
                setattr(value, "hlpn86", self)

    @property
    def highlevelnets_hlpn_ArcTP(self):
        return self.__highlevelnets_hlpn_ArcTP

    @highlevelnets_hlpn_ArcTP.setter
    def highlevelnets_hlpn_ArcTP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_hlpn_ArcTP__highlevelnets_hlpn_ArcTP", None)
        self.__highlevelnets_hlpn_ArcTP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenVariadicExpression88"):
                opp_val = getattr(old_value, "TokenVariadicExpression88", None)
                if opp_val == self:
                    setattr(old_value, "TokenVariadicExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenVariadicExpression88"):
                opp_val = getattr(value, "TokenVariadicExpression88", None)
                setattr(value, "TokenVariadicExpression88", self)

class Node:

    pass
class highlevelnets_hlpn_Place(Node):

    pass
class hlpn_Node:

    pass
class hlpn_ContextVariable:

    pass
class highlevelnets_hlpn_Transition(hlpn_Node, hlpn_ContextVariable):

    pass
class common_INetElement:

    pass
class highlevelnets_hlpn_HighLevelPetriNet(common_INetElement, hlpn_ContextVariable):

    pass
class Variable:

    pass
class MonomConstant:

    pass
class Monom:

    pass
class TokenBinding:

    pass
class TokenVariadicExpression:

    pass
class TokenWeight:

    pass
class ContextVariable:

    pass
class TokenTypeAtomic:

    pass
class Token:

    pass
class highlevelnets_tokentypes_TokenAtomic(Token):

    pass
class TokenAttribute:

    pass
class TokenTypeElementNet:

    pass
class highlevelnets_tokentypes_TokenNet(Token):

    pass
class TokenAtomic:

    pass
class Atom:

    pass
class TokenType:

    pass
class highlevelnets_tokentypes_TokenTypeElementNet(TokenType):

    def __init__(self, ElementNetMarked: set["ElementNetMarked"] = None, highlevelnets_tokentypes_TokenTypeElementNet: "HighLevelPetriNet" = None, TokenNet: set["TokenNet"] = None, TokenType: "highlevelnets_tokenexpressions_TokenMultisetExpression", TokenType67: "highlevelnets_hlpn_Place", TokenType37: "highlevelnets_tokenexpressions_TokenMultiSet"):
        self.ElementNetMarked = ElementNetMarked if ElementNetMarked is not None else set()
        self.highlevelnets_tokentypes_TokenTypeElementNet = highlevelnets_tokentypes_TokenTypeElementNet
        self.TokenNet = TokenNet if TokenNet is not None else set()
        
    @property
    def ElementNetMarked(self):
        return self.__ElementNetMarked

    @ElementNetMarked.setter
    def ElementNetMarked(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokentypes_TokenTypeElementNet__ElementNetMarked", None)
        self.__ElementNetMarked = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tokentypes10"):
                    opp_val = getattr(item, "tokentypes10", None)
                    
                    if opp_val == self:
                        setattr(item, "tokentypes10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tokentypes10"):
                    opp_val = getattr(item, "tokentypes10", None)
                    
                    setattr(item, "tokentypes10", self)
                    

    @property
    def TokenNet(self):
        return self.__TokenNet

    @TokenNet.setter
    def TokenNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokentypes_TokenTypeElementNet__TokenNet", None)
        self.__TokenNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tokentypes14"):
                    opp_val = getattr(item, "tokentypes14", None)
                    
                    if opp_val == self:
                        setattr(item, "tokentypes14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tokentypes14"):
                    opp_val = getattr(item, "tokentypes14", None)
                    
                    setattr(item, "tokentypes14", self)
                    

    @property
    def highlevelnets_tokentypes_TokenTypeElementNet(self):
        return self.__highlevelnets_tokentypes_TokenTypeElementNet

    @highlevelnets_tokentypes_TokenTypeElementNet.setter
    def highlevelnets_tokentypes_TokenTypeElementNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokentypes_TokenTypeElementNet__highlevelnets_tokentypes_TokenTypeElementNet", None)
        self.__highlevelnets_tokentypes_TokenTypeElementNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HighLevelPetriNet12"):
                opp_val = getattr(old_value, "HighLevelPetriNet12", None)
                if opp_val == self:
                    setattr(old_value, "HighLevelPetriNet12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HighLevelPetriNet12"):
                opp_val = getattr(value, "HighLevelPetriNet12", None)
                setattr(value, "HighLevelPetriNet12", self)

    def createInstance(self):
        # TODO: Implement createInstance method
        pass

    def getInstanceByID(self, id: int):
        # TODO: Implement getInstanceByID method
        pass

class highlevelnets_tokentypes_TokenTypeAtomic(TokenType):

    pass
class TokenNet:

    pass
class ElementNetMarked:

    pass
class TokenMultiSet:

    pass
class Place:

    pass
class IEntityIdentifiable:

    pass
class highlevelnets_tokenexpressions_TokenBinding(IEntityIdentifiable):

    pass
class highlevelnets_common_INetElement(IEntityIdentifiable):

    def __init__(self, name: str, comment: str):
        self.name = name
        self.comment = comment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class highlevelnets_tokenexpressions_TokenExpressionBinding(IEntityIdentifiable):

    pass
class highlevelnets_tokenexpressions_TokenMultisetExpression(IEntityIdentifiable):

    pass
class highlevelnets_npndiagrams_NPNSymbolNodeSN(IEntityIdentifiable):

    def __init__(self, constraints: str, NPNDiagramNetSystem151: "NPNDiagramNetSystem" = None, highlevelnets_npndiagrams_NPNSymbolNodeSN: "Node" = None):
        self.constraints = constraints
        self.NPNDiagramNetSystem151 = NPNDiagramNetSystem151
        self.highlevelnets_npndiagrams_NPNSymbolNodeSN = highlevelnets_npndiagrams_NPNSymbolNodeSN
        
    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def NPNDiagramNetSystem151(self):
        return self.__NPNDiagramNetSystem151

    @NPNDiagramNetSystem151.setter
    def NPNDiagramNetSystem151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolNodeSN__NPNDiagramNetSystem151", None)
        self.__NPNDiagramNetSystem151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "npndiagrams152"):
                opp_val = getattr(old_value, "npndiagrams152", None)
                if opp_val == self:
                    setattr(old_value, "npndiagrams152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "npndiagrams152"):
                opp_val = getattr(value, "npndiagrams152", None)
                setattr(value, "npndiagrams152", self)

    @property
    def highlevelnets_npndiagrams_NPNSymbolNodeSN(self):
        return self.__highlevelnets_npndiagrams_NPNSymbolNodeSN

    @highlevelnets_npndiagrams_NPNSymbolNodeSN.setter
    def highlevelnets_npndiagrams_NPNSymbolNodeSN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolNodeSN__highlevelnets_npndiagrams_NPNSymbolNodeSN", None)
        self.__highlevelnets_npndiagrams_NPNSymbolNodeSN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node154"):
                opp_val = getattr(old_value, "Node154", None)
                if opp_val == self:
                    setattr(old_value, "Node154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node154"):
                opp_val = getattr(value, "Node154", None)
                setattr(value, "Node154", self)

class highlevelnets_tokenexpressions_TokenWeight(IEntityIdentifiable):

    def __init__(self, weight: str, highlevelnets_tokenexpressions_TokenWeight: "Token" = None):
        self.weight = weight
        self.highlevelnets_tokenexpressions_TokenWeight = highlevelnets_tokenexpressions_TokenWeight
        
    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def highlevelnets_tokenexpressions_TokenWeight(self):
        return self.__highlevelnets_tokenexpressions_TokenWeight

    @highlevelnets_tokenexpressions_TokenWeight.setter
    def highlevelnets_tokenexpressions_TokenWeight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_TokenWeight__highlevelnets_tokenexpressions_TokenWeight", None)
        self.__highlevelnets_tokenexpressions_TokenWeight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Token"):
                opp_val = getattr(old_value, "Token", None)
                if opp_val == self:
                    setattr(old_value, "Token", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Token"):
                opp_val = getattr(value, "Token", None)
                setattr(value, "Token", self)

class highlevelnets_tokenexpressions_Monom(IEntityIdentifiable):

    def __init__(self, power: str, highlevelnets_tokenexpressions_Monom: "Variable" = None):
        self.power = power
        self.highlevelnets_tokenexpressions_Monom = highlevelnets_tokenexpressions_Monom
        
    @property
    def power(self) -> str:
        return self.__power

    @power.setter
    def power(self, power: str):
        self.__power = power

    @property
    def highlevelnets_tokenexpressions_Monom(self):
        return self.__highlevelnets_tokenexpressions_Monom

    @highlevelnets_tokenexpressions_Monom.setter
    def highlevelnets_tokenexpressions_Monom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_Monom__highlevelnets_tokenexpressions_Monom", None)
        self.__highlevelnets_tokenexpressions_Monom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable"):
                opp_val = getattr(old_value, "Variable", None)
                if opp_val == self:
                    setattr(old_value, "Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable"):
                opp_val = getattr(value, "Variable", None)
                setattr(value, "Variable", self)

class highlevelnets_npndiagrams_NPNSymbolArcSN(IEntityIdentifiable):

    def __init__(self, bendpoints: str, NPNDiagramNetSystem156: "NPNDiagramNetSystem" = None, highlevelnets_npndiagrams_NPNSymbolArcSN: "Arc" = None):
        self.bendpoints = bendpoints
        self.NPNDiagramNetSystem156 = NPNDiagramNetSystem156
        self.highlevelnets_npndiagrams_NPNSymbolArcSN = highlevelnets_npndiagrams_NPNSymbolArcSN
        
    @property
    def bendpoints(self) -> str:
        return self.__bendpoints

    @bendpoints.setter
    def bendpoints(self, bendpoints: str):
        self.__bendpoints = bendpoints

    @property
    def highlevelnets_npndiagrams_NPNSymbolArcSN(self):
        return self.__highlevelnets_npndiagrams_NPNSymbolArcSN

    @highlevelnets_npndiagrams_NPNSymbolArcSN.setter
    def highlevelnets_npndiagrams_NPNSymbolArcSN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolArcSN__highlevelnets_npndiagrams_NPNSymbolArcSN", None)
        self.__highlevelnets_npndiagrams_NPNSymbolArcSN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arc159"):
                opp_val = getattr(old_value, "Arc159", None)
                if opp_val == self:
                    setattr(old_value, "Arc159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arc159"):
                opp_val = getattr(value, "Arc159", None)
                setattr(value, "Arc159", self)

    @property
    def NPNDiagramNetSystem156(self):
        return self.__NPNDiagramNetSystem156

    @NPNDiagramNetSystem156.setter
    def NPNDiagramNetSystem156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolArcSN__NPNDiagramNetSystem156", None)
        self.__NPNDiagramNetSystem156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "npndiagrams157"):
                opp_val = getattr(old_value, "npndiagrams157", None)
                if opp_val == self:
                    setattr(old_value, "npndiagrams157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "npndiagrams157"):
                opp_val = getattr(value, "npndiagrams157", None)
                setattr(value, "npndiagrams157", self)

class highlevelnets_tokenexpressions_Variable(IEntityIdentifiable):

    def __init__(self, name: str, ContextVariable: "ContextVariable" = None):
        self.name = name
        self.ContextVariable = ContextVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ContextVariable(self):
        return self.__ContextVariable

    @ContextVariable.setter
    def ContextVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_Variable__ContextVariable", None)
        self.__ContextVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlpn"):
                opp_val = getattr(old_value, "hlpn", None)
                if opp_val == self:
                    setattr(old_value, "hlpn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlpn"):
                opp_val = getattr(value, "hlpn", None)
                setattr(value, "hlpn", self)

class highlevelnets_npndiagrams_NPNDiagramNPNMarked(IEntityIdentifiable):

    pass
class highlevelnets_tokentypes_TokenAttribute(IEntityIdentifiable):

    def __init__(self, type: str, name: str, value: str):
        self.type = type
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class highlevelnets_tokenexpressions_MonomConstant(IEntityIdentifiable):

    def __init__(self, power: str, highlevelnets_tokenexpressions_MonomConstant: "Variable" = None, highlevelnets_tokenexpressions_MonomConstant54: "Token" = None):
        self.power = power
        self.highlevelnets_tokenexpressions_MonomConstant = highlevelnets_tokenexpressions_MonomConstant
        self.highlevelnets_tokenexpressions_MonomConstant54 = highlevelnets_tokenexpressions_MonomConstant54
        
    @property
    def power(self) -> str:
        return self.__power

    @power.setter
    def power(self, power: str):
        self.__power = power

    @property
    def highlevelnets_tokenexpressions_MonomConstant54(self):
        return self.__highlevelnets_tokenexpressions_MonomConstant54

    @highlevelnets_tokenexpressions_MonomConstant54.setter
    def highlevelnets_tokenexpressions_MonomConstant54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_MonomConstant__highlevelnets_tokenexpressions_MonomConstant54", None)
        self.__highlevelnets_tokenexpressions_MonomConstant54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Token55"):
                opp_val = getattr(old_value, "Token55", None)
                if opp_val == self:
                    setattr(old_value, "Token55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Token55"):
                opp_val = getattr(value, "Token55", None)
                setattr(value, "Token55", self)

    @property
    def highlevelnets_tokenexpressions_MonomConstant(self):
        return self.__highlevelnets_tokenexpressions_MonomConstant

    @highlevelnets_tokenexpressions_MonomConstant.setter
    def highlevelnets_tokenexpressions_MonomConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_MonomConstant__highlevelnets_tokenexpressions_MonomConstant", None)
        self.__highlevelnets_tokenexpressions_MonomConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable52"):
                opp_val = getattr(old_value, "Variable52", None)
                if opp_val == self:
                    setattr(old_value, "Variable52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable52"):
                opp_val = getattr(value, "Variable52", None)
                setattr(value, "Variable52", self)

class highlevelnets_npndiagrams_NPNSymbolTokenSN(IEntityIdentifiable):

    def __init__(self, constraints: str, NPNSymbolPlaceSN161: "NPNSymbolPlaceSN" = None):
        self.constraints = constraints
        self.NPNSymbolPlaceSN161 = NPNSymbolPlaceSN161
        
    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def NPNSymbolPlaceSN161(self):
        return self.__NPNSymbolPlaceSN161

    @NPNSymbolPlaceSN161.setter
    def NPNSymbolPlaceSN161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolTokenSN__NPNSymbolPlaceSN161", None)
        self.__NPNSymbolPlaceSN161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "npndiagrams162"):
                opp_val = getattr(old_value, "npndiagrams162", None)
                if opp_val == self:
                    setattr(old_value, "npndiagrams162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "npndiagrams162"):
                opp_val = getattr(value, "npndiagrams162", None)
                setattr(value, "npndiagrams162", self)

class highlevelnets_tokenexpressions_TokenMultiSet(IEntityIdentifiable):

    pass
class highlevelnets_npndiagrams_NPNDiagramNetSystem(IEntityIdentifiable):

    pass
class highlevelnets_hlpn_ContextVariable(IEntityIdentifiable):

    pass
class highlevelnets_marking_PlaceMarking(IEntityIdentifiable):

    pass
class PlaceMarking:

    pass
class INetElement:

    pass
class highlevelnets_hlpn_Arc(INetElement):

    pass
class highlevelnets_tokentypes_Atom(INetElement):

    pass
class highlevelnets_hlpn_Node(INetElement):

    def __init__(self, firstTimeConstraint: int, secondTimeConstraint: int, HighLevelPetriNet92: "HighLevelPetriNet" = None):
        self.firstTimeConstraint = firstTimeConstraint
        self.secondTimeConstraint = secondTimeConstraint
        self.HighLevelPetriNet92 = HighLevelPetriNet92
        
    @property
    def secondTimeConstraint(self) -> int:
        return self.__secondTimeConstraint

    @secondTimeConstraint.setter
    def secondTimeConstraint(self, secondTimeConstraint: int):
        self.__secondTimeConstraint = secondTimeConstraint

    @property
    def firstTimeConstraint(self) -> int:
        return self.__firstTimeConstraint

    @firstTimeConstraint.setter
    def firstTimeConstraint(self, firstTimeConstraint: int):
        self.__firstTimeConstraint = firstTimeConstraint

    @property
    def HighLevelPetriNet92(self):
        return self.__HighLevelPetriNet92

    @HighLevelPetriNet92.setter
    def HighLevelPetriNet92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_hlpn_Node__HighLevelPetriNet92", None)
        self.__HighLevelPetriNet92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlpn93"):
                opp_val = getattr(old_value, "hlpn93", None)
                if opp_val == self:
                    setattr(old_value, "hlpn93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlpn93"):
                opp_val = getattr(value, "hlpn93", None)
                setattr(value, "hlpn93", self)

class highlevelnets_tokentypes_TokenType(INetElement):

    pass
class highlevelnets_npnets_NPnetMarked(INetElement):

    pass
class highlevelnets_tokentypes_ElementNetMarked(INetElement):

    pass
class highlevelnets_tokenexpressions_NetConstant(INetElement):

    pass
class highlevelnets_tokenexpressions_TokenVariadicExpression(INetElement):

    pass
class highlevelnets_npnets_NPnet(INetElement):

    pass
class highlevelnets_tokentypes_Token(INetElement):

    def __init__(self, highlevelnets_tokentypes_Token: set["TokenAttribute"] = None):
        self.highlevelnets_tokentypes_Token = highlevelnets_tokentypes_Token if highlevelnets_tokentypes_Token is not None else set()
        
    @property
    def highlevelnets_tokentypes_Token(self):
        return self.__highlevelnets_tokentypes_Token

    @highlevelnets_tokentypes_Token.setter
    def highlevelnets_tokentypes_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokentypes_Token__highlevelnets_tokentypes_Token", None)
        self.__highlevelnets_tokentypes_Token = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TokenAttribute"):
                    opp_val = getattr(item, "TokenAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "TokenAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TokenAttribute"):
                    opp_val = getattr(item, "TokenAttribute", None)
                    
                    setattr(item, "TokenAttribute", self)
                    

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class highlevelnets_npnets_Synchronization(INetElement):

    def __init__(self, kind: str, key: str, TransitionSynchronized: set["TransitionSynchronized"] = None):
        self.kind = kind
        self.key = key
        self.TransitionSynchronized = TransitionSynchronized if TransitionSynchronized is not None else set()
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def TransitionSynchronized(self):
        return self.__TransitionSynchronized

    @TransitionSynchronized.setter
    def TransitionSynchronized(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npnets_Synchronization__TransitionSynchronized", None)
        self.__TransitionSynchronized = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "npnets"):
                    opp_val = getattr(item, "npnets", None)
                    
                    if opp_val == self:
                        setattr(item, "npnets", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "npnets"):
                    opp_val = getattr(item, "npnets", None)
                    
                    setattr(item, "npnets", self)
                    

class Marking:

    pass
class HighLevelPetriNet:

    pass
class highlevelnets_marking_HighLevelPetriNetMarked(INetElement):

    pass
class highlevelnets_marking_Marking(INetElement):

    pass