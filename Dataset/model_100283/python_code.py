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
class NPNSymbolTokenSN:

    pass
class NPNSymbolTransitionSN:

    pass
class NPnetMarked:

    pass
class NPNSymbolArcTPSN:

    pass
class NPNSymbolArcPTSN:

    pass
class NPNSymbolArcSN:

    pass
class highlevelnets_npndiagrams_NPNSymbolArcTPSN(NPNSymbolArcSN):

    pass
class highlevelnets_npndiagrams_NPNSymbolArcPTSN(NPNSymbolArcSN):

    pass
class NPNSymbolNodeSN:

    pass
class highlevelnets_npndiagrams_NPNSymbolTransitionSN(NPNSymbolNodeSN):

    pass
class highlevelnets_npndiagrams_NPNSymbolPlaceSN(NPNSymbolNodeSN):

    pass
class highlevelnets_common_IEntityIdentifiable(ABC):

    def __init__(self, uuid: str):
        self.uuid = uuid
        
        pass
    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid


class NPnet:

    pass
class Synchronization:

    pass
class TransitionSynchronized:

    pass
class NPNDiagramNetSystem:

    pass
class NetConstant:

    pass
class Transition:

    pass
class highlevelnets_npnets_TransitionSynchronized(Transition):

    pass
class hlpn_Node:

    pass
class Arc:

    pass
class highlevelnets_hlpn_ArcPT(Arc):

    pass
class highlevelnets_hlpn_ArcTP(Arc):

    pass
class Node:

    pass
class ArcTP:

    pass
class ArcPT:

    pass
class highlevelnets_hlpn_Place(Node):

    pass
class hlpn_ContextVariable:

    pass
class highlevelnets_hlpn_Transition(hlpn_Node, hlpn_ContextVariable):

    pass
class common_INetElement:

    pass
class highlevelnets_hlpn_HighLevelPetriNet(common_INetElement, hlpn_ContextVariable):

    pass
class MonomConstant:

    pass
class Monom:

    pass
class TokenBinding:

    pass
class TokenVariadicExpression:

    pass
class Variable:

    pass
class ContextVariable:

    pass
class TokenWeight:

    pass
class TokenAttribute:

    pass
class TokenTypeElementNet:

    pass
class TokenTypeAtomic:

    pass
class Token:

    pass
class highlevelnets_tokentypes_TokenNet(Token):

    pass
class highlevelnets_tokentypes_TokenAtomic(Token):

    pass
class TokenAtomic:

    pass
class Atom:

    pass
class TokenType:

    pass
class TokenNet:

    pass
class ElementNetMarked:

    pass
class highlevelnets_tokentypes_TokenTypeElementNet(TokenType):

    def __init__(self, type10: set["ElementNetMarked"] = None, highlevelnets_tokentypes_TokenTypeElementNet: "HighLevelPetriNet" = None, type14: set["TokenNet"] = None, TokenType: "highlevelnets_tokenexpressions_TokenMultisetExpression" = None, TokenType34: "highlevelnets_tokenexpressions_TokenMultiSet" = None, TokenType61: "highlevelnets_hlpn_Place" = None):
        self.type10 = type10 if type10 is not None else set()
        self.highlevelnets_tokentypes_TokenTypeElementNet = highlevelnets_tokentypes_TokenTypeElementNet
        self.type14 = type14 if type14 is not None else set()
        
        pass
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

    @property
    def type10(self):
        return self.__type10

    @type10.setter
    def type10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokentypes_TokenTypeElementNet__type10", None)
        self.__type10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementNetMarked"):
                    opp_val = getattr(item, "ElementNetMarked", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementNetMarked", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementNetMarked"):
                    opp_val = getattr(item, "ElementNetMarked", None)
                    
                    setattr(item, "ElementNetMarked", self)
                    

    @property
    def type14(self):
        return self.__type14

    @type14.setter
    def type14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokentypes_TokenTypeElementNet__type14", None)
        self.__type14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TokenNet"):
                    opp_val = getattr(item, "TokenNet", None)
                    
                    if opp_val == self:
                        setattr(item, "TokenNet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TokenNet"):
                    opp_val = getattr(item, "TokenNet", None)
                    
                    setattr(item, "TokenNet", self)
                    

    def createInstance(self):
        # TODO: Implement createInstance method
        pass

    def getInstanceByID(self, highlevelnets_id):
        # TODO: Implement getInstanceByID method
        pass

class Place:

    pass
class IEntityIdentifiable:

    pass
class highlevelnets_tokenexpressions_Variable(IEntityIdentifiable):

    def __init__(self, name: str, variables: "ContextVariable" = None):
        self.name = name
        self.variables = variables
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_Variable__variables", None)
        self.__variables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContextVariable"):
                opp_val = getattr(old_value, "ContextVariable", None)
                if opp_val == self:
                    setattr(old_value, "ContextVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContextVariable"):
                opp_val = getattr(value, "ContextVariable", None)
                setattr(value, "ContextVariable", self)

class highlevelnets_tokentypes_TokenAttribute(IEntityIdentifiable):

    def __init__(self, type: str, name: str, value: str):
        self.type = type
        self.name = name
        self.value = value
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class highlevelnets_tokenexpressions_TokenWeight(IEntityIdentifiable):

    def __init__(self, weight: str, highlevelnets_tokenexpressions_TokenWeight: "Token" = None):
        self.weight = weight
        self.highlevelnets_tokenexpressions_TokenWeight = highlevelnets_tokenexpressions_TokenWeight
        
        pass
    @property
    def weight(self):
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

class highlevelnets_tokenexpressions_TokenExpressionBinding(IEntityIdentifiable):

    pass
class highlevelnets_tokenexpressions_Monom(IEntityIdentifiable):

    def __init__(self, power: str, highlevelnets_tokenexpressions_Monom: "Variable" = None):
        self.power = power
        self.highlevelnets_tokenexpressions_Monom = highlevelnets_tokenexpressions_Monom
        
        pass
    @property
    def power(self):
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

class highlevelnets_npndiagrams_NPNSymbolTokenSN(IEntityIdentifiable):

    def __init__(self, constraints: str, tokens: "NPNSymbolPlaceSN" = None):
        self.constraints = constraints
        self.tokens = tokens
        
        pass
    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints


    @property
    def tokens(self):
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolTokenSN__tokens", None)
        self.__tokens = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NPNSymbolPlaceSN149"):
                opp_val = getattr(old_value, "NPNSymbolPlaceSN149", None)
                if opp_val == self:
                    setattr(old_value, "NPNSymbolPlaceSN149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NPNSymbolPlaceSN149"):
                opp_val = getattr(value, "NPNSymbolPlaceSN149", None)
                setattr(value, "NPNSymbolPlaceSN149", self)

class highlevelnets_npndiagrams_NPNSymbolNodeSN(IEntityIdentifiable):

    def __init__(self, constraints: str, nodes139: "NPNDiagramNetSystem" = None, highlevelnets_npndiagrams_NPNSymbolNodeSN: "Node" = None):
        self.constraints = constraints
        self.nodes139 = nodes139
        self.highlevelnets_npndiagrams_NPNSymbolNodeSN = highlevelnets_npndiagrams_NPNSymbolNodeSN
        
        pass
    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints


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
            if hasattr(old_value, "Node142"):
                opp_val = getattr(old_value, "Node142", None)
                if opp_val == self:
                    setattr(old_value, "Node142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node142"):
                opp_val = getattr(value, "Node142", None)
                setattr(value, "Node142", self)

    @property
    def nodes139(self):
        return self.__nodes139

    @nodes139.setter
    def nodes139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolNodeSN__nodes139", None)
        self.__nodes139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NPNDiagramNetSystem140"):
                opp_val = getattr(old_value, "NPNDiagramNetSystem140", None)
                if opp_val == self:
                    setattr(old_value, "NPNDiagramNetSystem140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NPNDiagramNetSystem140"):
                opp_val = getattr(value, "NPNDiagramNetSystem140", None)
                setattr(value, "NPNDiagramNetSystem140", self)

class highlevelnets_common_INetElement(IEntityIdentifiable):

    def __init__(self, name: str, comment: str):
        self.name = name
        self.comment = comment
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class highlevelnets_npndiagrams_NPNDiagramNPNMarked(IEntityIdentifiable):

    pass
class highlevelnets_tokenexpressions_TokenBinding(IEntityIdentifiable):

    pass
class highlevelnets_tokenexpressions_MonomConstant(IEntityIdentifiable):

    def __init__(self, power: str, highlevelnets_tokenexpressions_MonomConstant51: "Token" = None, highlevelnets_tokenexpressions_MonomConstant: "Variable" = None):
        self.power = power
        self.highlevelnets_tokenexpressions_MonomConstant51 = highlevelnets_tokenexpressions_MonomConstant51
        self.highlevelnets_tokenexpressions_MonomConstant = highlevelnets_tokenexpressions_MonomConstant
        
        pass
    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power: str):
        self.__power = power


    @property
    def highlevelnets_tokenexpressions_MonomConstant51(self):
        return self.__highlevelnets_tokenexpressions_MonomConstant51

    @highlevelnets_tokenexpressions_MonomConstant51.setter
    def highlevelnets_tokenexpressions_MonomConstant51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_tokenexpressions_MonomConstant__highlevelnets_tokenexpressions_MonomConstant51", None)
        self.__highlevelnets_tokenexpressions_MonomConstant51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Token52"):
                opp_val = getattr(old_value, "Token52", None)
                if opp_val == self:
                    setattr(old_value, "Token52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Token52"):
                opp_val = getattr(value, "Token52", None)
                setattr(value, "Token52", self)

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
            if hasattr(old_value, "Variable49"):
                opp_val = getattr(old_value, "Variable49", None)
                if opp_val == self:
                    setattr(old_value, "Variable49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable49"):
                opp_val = getattr(value, "Variable49", None)
                setattr(value, "Variable49", self)

class highlevelnets_npndiagrams_NPNDiagramNetSystem(IEntityIdentifiable):

    pass
class highlevelnets_hlpn_ContextVariable(IEntityIdentifiable):

    pass
class highlevelnets_npndiagrams_NPNSymbolArcSN(IEntityIdentifiable):

    def __init__(self, bendpoints: str, arcs144: "NPNDiagramNetSystem" = None, highlevelnets_npndiagrams_NPNSymbolArcSN: "Arc" = None):
        self.bendpoints = bendpoints
        self.arcs144 = arcs144
        self.highlevelnets_npndiagrams_NPNSymbolArcSN = highlevelnets_npndiagrams_NPNSymbolArcSN
        
        pass
    @property
    def bendpoints(self):
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
            if hasattr(old_value, "Arc147"):
                opp_val = getattr(old_value, "Arc147", None)
                if opp_val == self:
                    setattr(old_value, "Arc147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arc147"):
                opp_val = getattr(value, "Arc147", None)
                setattr(value, "Arc147", self)

    @property
    def arcs144(self):
        return self.__arcs144

    @arcs144.setter
    def arcs144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npndiagrams_NPNSymbolArcSN__arcs144", None)
        self.__arcs144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NPNDiagramNetSystem145"):
                opp_val = getattr(old_value, "NPNDiagramNetSystem145", None)
                if opp_val == self:
                    setattr(old_value, "NPNDiagramNetSystem145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NPNDiagramNetSystem145"):
                opp_val = getattr(value, "NPNDiagramNetSystem145", None)
                setattr(value, "NPNDiagramNetSystem145", self)

class highlevelnets_tokenexpressions_TokenMultiSet(IEntityIdentifiable):

    pass
class highlevelnets_tokenexpressions_TokenMultisetExpression(IEntityIdentifiable):

    pass
class highlevelnets_marking_PlaceMarking(IEntityIdentifiable):

    pass
class highlevelnets_tokentypes_TokenTypeAtomic(TokenType):

    pass
class Marking:

    pass
class HighLevelPetriNet:

    pass
class TokenMultiSet:

    pass
class PlaceMarking:

    pass
class INetElement:

    pass
class highlevelnets_tokenexpressions_TokenVariadicExpression(INetElement):

    pass
class highlevelnets_npnets_Synchronization(INetElement):

    def __init__(self, kind: str, key: str, synchronization: set["TransitionSynchronized"] = None):
        self.kind = kind
        self.key = key
        self.synchronization = synchronization if synchronization is not None else set()
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def synchronization(self):
        return self.__synchronization

    @synchronization.setter
    def synchronization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_highlevelnets_npnets_Synchronization__synchronization", None)
        self.__synchronization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionSynchronized"):
                    opp_val = getattr(item, "TransitionSynchronized", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionSynchronized", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionSynchronized"):
                    opp_val = getattr(item, "TransitionSynchronized", None)
                    
                    setattr(item, "TransitionSynchronized", self)
                    

class highlevelnets_tokentypes_ElementNetMarked(INetElement):

    pass
class highlevelnets_tokenexpressions_NetConstant(INetElement):

    pass
class highlevelnets_tokentypes_Token(INetElement):

    def __init__(self, highlevelnets_tokentypes_Token: set["TokenAttribute"] = None):
        self.highlevelnets_tokentypes_Token = highlevelnets_tokentypes_Token if highlevelnets_tokentypes_Token is not None else set()
        
        pass
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
                    

    def getType(self) :
        # TODO: Implement getType method
        pass

class highlevelnets_npnets_NPnet(INetElement):

    pass
class highlevelnets_tokentypes_Atom(INetElement):

    pass
class highlevelnets_marking_HighLevelPetriNetMarked(INetElement):

    pass
class highlevelnets_hlpn_Arc(INetElement):

    pass
class highlevelnets_npnets_NPnetMarked(INetElement):

    pass
class highlevelnets_hlpn_Node(INetElement):

    pass
class highlevelnets_tokentypes_TokenType(INetElement):

    pass
class highlevelnets_marking_Marking(INetElement):

    pass