####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
ESynchronizationKind: Enumeration = Enumeration(
    name="ESynchronizationKind",
    literals={
            EnumerationLiteral(name="VerticalSynchronization"),
			EnumerationLiteral(name="HorizontalSynchronization")
    }
)

# Classes
highlevelnets_marking_PlaceMarking = Class(name="highlevelnets_marking_PlaceMarking")
IEntityIdentifiable = Class(name="IEntityIdentifiable")
Place = Class(name="Place")
TokenMultiSet = Class(name="TokenMultiSet")
highlevelnets_marking_HighLevelPetriNetMarked = Class(name="highlevelnets_marking_HighLevelPetriNetMarked")
HighLevelPetriNet = Class(name="HighLevelPetriNet")
Marking = Class(name="Marking")
highlevelnets_tokentypes_TokenType = Class(name="highlevelnets_tokentypes_TokenType", is_abstract=True)
highlevelnets_tokentypes_TokenTypeAtomic = Class(name="highlevelnets_tokentypes_TokenTypeAtomic")
TokenType = Class(name="TokenType")
Atom = Class(name="Atom")
TokenAtomic = Class(name="TokenAtomic")
highlevelnets_tokentypes_TokenTypeElementNet = Class(name="highlevelnets_tokentypes_TokenTypeElementNet")
tokentypes_TokenType = Class(name="tokentypes_TokenType")
common_IDiagramHolder = Class(name="common_IDiagramHolder")
highlevelnets_marking_Marking = Class(name="highlevelnets_marking_Marking")
INetElement = Class(name="INetElement")
PlaceMarking = Class(name="PlaceMarking")
highlevelnets_tokentypes_TokenAtomic = Class(name="highlevelnets_tokentypes_TokenAtomic")
Token = Class(name="Token")
TokenTypeAtomic = Class(name="TokenTypeAtomic")
highlevelnets_tokentypes_TokenNet = Class(name="highlevelnets_tokentypes_TokenNet")
TokenTypeElementNet = Class(name="TokenTypeElementNet")
highlevelnets_tokentypes_TokenAttribute = Class(name="highlevelnets_tokentypes_TokenAttribute")
highlevelnets_tokentypes_ElementNetMarked = Class(name="highlevelnets_tokentypes_ElementNetMarked")
highlevelnets_tokentypes_Atom = Class(name="highlevelnets_tokentypes_Atom")
highlevelnets_tokenexpressions_TokenWeight = Class(name="highlevelnets_tokenexpressions_TokenWeight")
highlevelnets_tokenexpressions_TokenMultisetExpression = Class(name="highlevelnets_tokenexpressions_TokenMultisetExpression")
ElementNetMarked = Class(name="ElementNetMarked")
TokenNet = Class(name="TokenNet")
highlevelnets_tokentypes_Token = Class(name="highlevelnets_tokentypes_Token", is_abstract=True)
TokenAttribute = Class(name="TokenAttribute")
Monom = Class(name="Monom")
MonomConstant = Class(name="MonomConstant")
highlevelnets_tokenexpressions_Monom = Class(name="highlevelnets_tokenexpressions_Monom")
Variable = Class(name="Variable")
highlevelnets_tokenexpressions_TokenExpressionBinding = Class(name="highlevelnets_tokenexpressions_TokenExpressionBinding")
TokenVariadicExpression = Class(name="TokenVariadicExpression")
TokenBinding = Class(name="TokenBinding")
highlevelnets_tokenexpressions_TokenBinding = Class(name="highlevelnets_tokenexpressions_TokenBinding")
highlevelnets_tokenexpressions_MonomConstant = Class(name="highlevelnets_tokenexpressions_MonomConstant")
highlevelnets_tokenexpressions_NetConstant = Class(name="highlevelnets_tokenexpressions_NetConstant")
highlevelnets_tokenexpressions_TokenMultiSet = Class(name="highlevelnets_tokenexpressions_TokenMultiSet")
TokenWeight = Class(name="TokenWeight")
highlevelnets_tokenexpressions_Variable = Class(name="highlevelnets_tokenexpressions_Variable")
ContextVariable = Class(name="ContextVariable")
highlevelnets_tokenexpressions_TokenVariadicExpression = Class(name="highlevelnets_tokenexpressions_TokenVariadicExpression")
Arc = Class(name="Arc")
highlevelnets_hlpn_Place = Class(name="highlevelnets_hlpn_Place")
ArcPT = Class(name="ArcPT")
ArcTP = Class(name="ArcTP")
highlevelnets_hlpn_Transition = Class(name="highlevelnets_hlpn_Transition")
hlpn_Node = Class(name="hlpn_Node")
highlevelnets_hlpn_ArcPT = Class(name="highlevelnets_hlpn_ArcPT")
highlevelnets_hlpn_HighLevelPetriNet = Class(name="highlevelnets_hlpn_HighLevelPetriNet")
common_INetElement = Class(name="common_INetElement")
hlpn_ContextVariable = Class(name="hlpn_ContextVariable")
Node = Class(name="Node")
highlevelnets_hlpn_Node = Class(name="highlevelnets_hlpn_Node", is_abstract=True)
highlevelnets_hlpn_Arc = Class(name="highlevelnets_hlpn_Arc", is_abstract=True)
highlevelnets_npnets_NPnet = Class(name="highlevelnets_npnets_NPnet")
IDiagramHolder = Class(name="IDiagramHolder")
Transition = Class(name="Transition")
highlevelnets_hlpn_ArcTP = Class(name="highlevelnets_hlpn_ArcTP")
highlevelnets_hlpn_ContextVariable = Class(name="highlevelnets_hlpn_ContextVariable", is_abstract=True)
highlevelnets_npnets_TransitionSynchronized = Class(name="highlevelnets_npnets_TransitionSynchronized")
highlevelnets_common_INetElement = Class(name="highlevelnets_common_INetElement", is_abstract=True)
highlevelnets_common_IEntityIdentifiable = Class(name="highlevelnets_common_IEntityIdentifiable", is_abstract=True)
highlevelnets_common_IDiagramHolder = Class(name="highlevelnets_common_IDiagramHolder", is_abstract=True)
NPNDiagramNetSystem = Class(name="NPNDiagramNetSystem")
highlevelnets_npndiagrams_NPNDiagramNetSystem = Class(name="highlevelnets_npndiagrams_NPNDiagramNetSystem")
NetConstant = Class(name="NetConstant")
Synchronization = Class(name="Synchronization")
NPnetMarked = Class(name="NPnetMarked")
highlevelnets_npnets_NPnetMarked = Class(name="highlevelnets_npnets_NPnetMarked")
NPnet = Class(name="NPnet")
highlevelnets_npnets_Synchronization = Class(name="highlevelnets_npnets_Synchronization")
TransitionSynchronized = Class(name="TransitionSynchronized")
highlevelnets_npndiagrams_NPNSymbolArcPTSN = Class(name="highlevelnets_npndiagrams_NPNSymbolArcPTSN")
NPNSymbolTransitionSN = Class(name="NPNSymbolTransitionSN")
NPNSymbolPlaceSN = Class(name="NPNSymbolPlaceSN")
highlevelnets_npndiagrams_NPNSymbolArcTPSN = Class(name="highlevelnets_npndiagrams_NPNSymbolArcTPSN")
highlevelnets_npndiagrams_NPNSymbolNodeSN = Class(name="highlevelnets_npndiagrams_NPNSymbolNodeSN", is_abstract=True)
highlevelnets_npndiagrams_NPNSymbolArcSN = Class(name="highlevelnets_npndiagrams_NPNSymbolArcSN", is_abstract=True)
NPNSymbolNodeSN = Class(name="NPNSymbolNodeSN")
NPNSymbolArcSN = Class(name="NPNSymbolArcSN")
highlevelnets_npndiagrams_NPNSymbolPlaceSN = Class(name="highlevelnets_npndiagrams_NPNSymbolPlaceSN")
NPNSymbolArcPTSN = Class(name="NPNSymbolArcPTSN")
NPNSymbolArcTPSN = Class(name="NPNSymbolArcTPSN")
highlevelnets_npndiagrams_NPNSymbolTransitionSN = Class(name="highlevelnets_npndiagrams_NPNSymbolTransitionSN")

# highlevelnets_marking_PlaceMarking class attributes and methods

# IEntityIdentifiable class attributes and methods

# Place class attributes and methods

# TokenMultiSet class attributes and methods

# highlevelnets_marking_HighLevelPetriNetMarked class attributes and methods

# HighLevelPetriNet class attributes and methods

# Marking class attributes and methods

# highlevelnets_tokentypes_TokenType class attributes and methods

# highlevelnets_tokentypes_TokenTypeAtomic class attributes and methods

# TokenType class attributes and methods

# Atom class attributes and methods

# TokenAtomic class attributes and methods

# highlevelnets_tokentypes_TokenTypeElementNet class attributes and methods
highlevelnets_tokentypes_TokenTypeElementNet_m_getInstanceByID: Method = Method(name="getInstanceByID", parameters={Parameter(name='highlevelnets_id', type=StringType)})
highlevelnets_tokentypes_TokenTypeElementNet_m_createInstance: Method = Method(name="createInstance", parameters={})
highlevelnets_tokentypes_TokenTypeElementNet.methods={highlevelnets_tokentypes_TokenTypeElementNet_m_getInstanceByID, highlevelnets_tokentypes_TokenTypeElementNet_m_createInstance}

# tokentypes_TokenType class attributes and methods

# common_IDiagramHolder class attributes and methods

# highlevelnets_marking_Marking class attributes and methods

# INetElement class attributes and methods

# PlaceMarking class attributes and methods

# highlevelnets_tokentypes_TokenAtomic class attributes and methods

# Token class attributes and methods

# TokenTypeAtomic class attributes and methods

# highlevelnets_tokentypes_TokenNet class attributes and methods

# TokenTypeElementNet class attributes and methods

# highlevelnets_tokentypes_TokenAttribute class attributes and methods
highlevelnets_tokentypes_TokenAttribute_type: Property = Property(name="type", type=StringType)
highlevelnets_tokentypes_TokenAttribute_name: Property = Property(name="name", type=StringType)
highlevelnets_tokentypes_TokenAttribute_value: Property = Property(name="value", type=StringType)
highlevelnets_tokentypes_TokenAttribute.attributes={highlevelnets_tokentypes_TokenAttribute_name, highlevelnets_tokentypes_TokenAttribute_type, highlevelnets_tokentypes_TokenAttribute_value}

# highlevelnets_tokentypes_ElementNetMarked class attributes and methods

# highlevelnets_tokentypes_Atom class attributes and methods

# highlevelnets_tokenexpressions_TokenWeight class attributes and methods
highlevelnets_tokenexpressions_TokenWeight_weight: Property = Property(name="weight", type=StringType)
highlevelnets_tokenexpressions_TokenWeight.attributes={highlevelnets_tokenexpressions_TokenWeight_weight}

# highlevelnets_tokenexpressions_TokenMultisetExpression class attributes and methods

# ElementNetMarked class attributes and methods

# TokenNet class attributes and methods

# highlevelnets_tokentypes_Token class attributes and methods
highlevelnets_tokentypes_Token_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
highlevelnets_tokentypes_Token.methods={highlevelnets_tokentypes_Token_m_getType}

# TokenAttribute class attributes and methods

# Monom class attributes and methods

# MonomConstant class attributes and methods

# highlevelnets_tokenexpressions_Monom class attributes and methods
highlevelnets_tokenexpressions_Monom_power: Property = Property(name="power", type=StringType)
highlevelnets_tokenexpressions_Monom.attributes={highlevelnets_tokenexpressions_Monom_power}

# Variable class attributes and methods

# highlevelnets_tokenexpressions_TokenExpressionBinding class attributes and methods

# TokenVariadicExpression class attributes and methods

# TokenBinding class attributes and methods

# highlevelnets_tokenexpressions_TokenBinding class attributes and methods

# highlevelnets_tokenexpressions_MonomConstant class attributes and methods
highlevelnets_tokenexpressions_MonomConstant_power: Property = Property(name="power", type=StringType)
highlevelnets_tokenexpressions_MonomConstant.attributes={highlevelnets_tokenexpressions_MonomConstant_power}

# highlevelnets_tokenexpressions_NetConstant class attributes and methods

# highlevelnets_tokenexpressions_TokenMultiSet class attributes and methods

# TokenWeight class attributes and methods

# highlevelnets_tokenexpressions_Variable class attributes and methods
highlevelnets_tokenexpressions_Variable_name: Property = Property(name="name", type=StringType)
highlevelnets_tokenexpressions_Variable.attributes={highlevelnets_tokenexpressions_Variable_name}

# ContextVariable class attributes and methods

# highlevelnets_tokenexpressions_TokenVariadicExpression class attributes and methods

# Arc class attributes and methods

# highlevelnets_hlpn_Place class attributes and methods

# ArcPT class attributes and methods

# ArcTP class attributes and methods

# highlevelnets_hlpn_Transition class attributes and methods

# hlpn_Node class attributes and methods

# highlevelnets_hlpn_ArcPT class attributes and methods

# highlevelnets_hlpn_HighLevelPetriNet class attributes and methods

# common_INetElement class attributes and methods

# hlpn_ContextVariable class attributes and methods

# Node class attributes and methods

# highlevelnets_hlpn_Node class attributes and methods

# highlevelnets_hlpn_Arc class attributes and methods

# highlevelnets_npnets_NPnet class attributes and methods

# IDiagramHolder class attributes and methods

# Transition class attributes and methods

# highlevelnets_hlpn_ArcTP class attributes and methods

# highlevelnets_hlpn_ContextVariable class attributes and methods

# highlevelnets_npnets_TransitionSynchronized class attributes and methods

# highlevelnets_common_INetElement class attributes and methods
highlevelnets_common_INetElement_name: Property = Property(name="name", type=StringType)
highlevelnets_common_INetElement_comment: Property = Property(name="comment", type=StringType)
highlevelnets_common_INetElement.attributes={highlevelnets_common_INetElement_comment, highlevelnets_common_INetElement_name}

# highlevelnets_common_IEntityIdentifiable class attributes and methods
highlevelnets_common_IEntityIdentifiable_id: Property = Property(name="id", type=StringType)
highlevelnets_common_IEntityIdentifiable.attributes={highlevelnets_common_IEntityIdentifiable_id}

# highlevelnets_common_IDiagramHolder class attributes and methods

# NPNDiagramNetSystem class attributes and methods

# highlevelnets_npndiagrams_NPNDiagramNetSystem class attributes and methods

# NetConstant class attributes and methods

# Synchronization class attributes and methods

# NPnetMarked class attributes and methods

# highlevelnets_npnets_NPnetMarked class attributes and methods

# NPnet class attributes and methods

# highlevelnets_npnets_Synchronization class attributes and methods
highlevelnets_npnets_Synchronization_kind: Property = Property(name="kind", type=StringType)
highlevelnets_npnets_Synchronization_key: Property = Property(name="key", type=StringType)
highlevelnets_npnets_Synchronization.attributes={highlevelnets_npnets_Synchronization_kind, highlevelnets_npnets_Synchronization_key}

# TransitionSynchronized class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolArcPTSN class attributes and methods

# NPNSymbolTransitionSN class attributes and methods

# NPNSymbolPlaceSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolArcTPSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolNodeSN class attributes and methods
highlevelnets_npndiagrams_NPNSymbolNodeSN_constraints: Property = Property(name="constraints", type=StringType)
highlevelnets_npndiagrams_NPNSymbolNodeSN.attributes={highlevelnets_npndiagrams_NPNSymbolNodeSN_constraints}

# highlevelnets_npndiagrams_NPNSymbolArcSN class attributes and methods
highlevelnets_npndiagrams_NPNSymbolArcSN_bendpoints: Property = Property(name="bendpoints", type=StringType)
highlevelnets_npndiagrams_NPNSymbolArcSN.attributes={highlevelnets_npndiagrams_NPNSymbolArcSN_bendpoints}

# NPNSymbolNodeSN class attributes and methods

# NPNSymbolArcSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolPlaceSN class attributes and methods

# NPNSymbolArcPTSN class attributes and methods

# NPNSymbolArcTPSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolTransitionSN class attributes and methods

# Relationships
map0: BinaryAssociation = BinaryAssociation(
    name="map0",
    ends={
        Property(name="highlevelnets_marking_Marking", type=PlaceMarking, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PlaceMarking", type=highlevelnets_marking_Marking, multiplicity=Multiplicity(1, 1))
    }
)
place1: BinaryAssociation = BinaryAssociation(
    name="place1",
    ends={
        Property(name="Place", type=highlevelnets_marking_PlaceMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_marking_PlaceMarking", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
marking2: BinaryAssociation = BinaryAssociation(
    name="marking2",
    ends={
        Property(name="TokenMultiSet", type=highlevelnets_marking_PlaceMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_marking_PlaceMarking3", type=TokenMultiSet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
net4: BinaryAssociation = BinaryAssociation(
    name="net4",
    ends={
        Property(name="HighLevelPetriNet", type=highlevelnets_marking_HighLevelPetriNetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_marking_HighLevelPetriNetMarked", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
marking5: BinaryAssociation = BinaryAssociation(
    name="marking5",
    ends={
        Property(name="Marking", type=highlevelnets_marking_HighLevelPetriNetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_marking_HighLevelPetriNetMarked6", type=Marking, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instance7: BinaryAssociation = BinaryAssociation(
    name="instance7",
    ends={
        Property(name="Atom", type=highlevelnets_tokentypes_TokenTypeAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_TokenTypeAtomic", type=Atom, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
atom8: BinaryAssociation = BinaryAssociation(
    name="atom8",
    ends={
        Property(name="TokenAtomic", type=highlevelnets_tokentypes_TokenTypeAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=TokenAtomic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="TokenTypeAtomic", type=highlevelnets_tokentypes_TokenAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="atom", type=TokenTypeAtomic, multiplicity=Multiplicity(1, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="Atom18", type=highlevelnets_tokentypes_TokenAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_TokenAtomic", type=Atom, multiplicity=Multiplicity(1, 1))
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="TokenTypeElementNet", type=highlevelnets_tokentypes_TokenNet, multiplicity=Multiplicity(1, 1)),
        Property(name="tokenNets", type=TokenTypeElementNet, multiplicity=Multiplicity(1, 1))
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="ElementNetMarked21", type=highlevelnets_tokentypes_TokenNet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_TokenNet", type=ElementNetMarked, multiplicity=Multiplicity(0, 1))
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="TokenTypeElementNet23", type=highlevelnets_tokentypes_ElementNetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="elementNetMarkeds", type=TokenTypeElementNet, multiplicity=Multiplicity(1, 1))
    }
)
marking24: BinaryAssociation = BinaryAssociation(
    name="marking24",
    ends={
        Property(name="Marking25", type=highlevelnets_tokentypes_ElementNetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_ElementNetMarked", type=Marking, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
token26: BinaryAssociation = BinaryAssociation(
    name="token26",
    ends={
        Property(name="Token", type=highlevelnets_tokenexpressions_TokenWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenWeight", type=Token, multiplicity=Multiplicity(1, 1))
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="TokenType", type=highlevelnets_tokenexpressions_TokenMultisetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultisetExpression", type=TokenType, multiplicity=Multiplicity(1, 1))
    }
)
elementNetMarkeds9: BinaryAssociation = BinaryAssociation(
    name="elementNetMarkeds9",
    ends={
        Property(name="ElementNetMarked", type=highlevelnets_tokentypes_TokenTypeElementNet, multiplicity=Multiplicity(1, 1)),
        Property(name="type10", type=ElementNetMarked, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net11: BinaryAssociation = BinaryAssociation(
    name="net11",
    ends={
        Property(name="HighLevelPetriNet12", type=highlevelnets_tokentypes_TokenTypeElementNet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_TokenTypeElementNet", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tokenNets13: BinaryAssociation = BinaryAssociation(
    name="tokenNets13",
    ends={
        Property(name="TokenNet", type=highlevelnets_tokentypes_TokenTypeElementNet, multiplicity=Multiplicity(1, 1)),
        Property(name="type14", type=TokenNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute15: BinaryAssociation = BinaryAssociation(
    name="attribute15",
    ends={
        Property(name="TokenAttribute", type=highlevelnets_tokentypes_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_Token", type=TokenAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monoms36: BinaryAssociation = BinaryAssociation(
    name="monoms36",
    ends={
        Property(name="Monom", type=highlevelnets_tokenexpressions_TokenVariadicExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenVariadicExpression", type=Monom, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
monomConstants37: BinaryAssociation = BinaryAssociation(
    name="monomConstants37",
    ends={
        Property(name="MonomConstant", type=highlevelnets_tokenexpressions_TokenVariadicExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenVariadicExpression38", type=MonomConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable39: BinaryAssociation = BinaryAssociation(
    name="variable39",
    ends={
        Property(name="Variable", type=highlevelnets_tokenexpressions_Monom, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_Monom", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression40: BinaryAssociation = BinaryAssociation(
    name="expression40",
    ends={
        Property(name="TokenVariadicExpression", type=highlevelnets_tokenexpressions_TokenExpressionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenExpressionBinding", type=TokenVariadicExpression, multiplicity=Multiplicity(1, 1))
    }
)
bindingTokens41: BinaryAssociation = BinaryAssociation(
    name="bindingTokens41",
    ends={
        Property(name="TokenBinding", type=highlevelnets_tokenexpressions_TokenExpressionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenExpressionBinding42", type=TokenBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable43: BinaryAssociation = BinaryAssociation(
    name="variable43",
    ends={
        Property(name="Variable44", type=highlevelnets_tokenexpressions_TokenBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenBinding", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
value45: BinaryAssociation = BinaryAssociation(
    name="value45",
    ends={
        Property(name="Token47", type=highlevelnets_tokenexpressions_TokenBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenBinding46", type=Token, multiplicity=Multiplicity(1, 1))
    }
)
constant48: BinaryAssociation = BinaryAssociation(
    name="constant48",
    ends={
        Property(name="Variable49", type=highlevelnets_tokenexpressions_MonomConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_MonomConstant", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
value50: BinaryAssociation = BinaryAssociation(
    name="value50",
    ends={
        Property(name="Token52", type=highlevelnets_tokenexpressions_MonomConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_MonomConstant51", type=Token, multiplicity=Multiplicity(1, 1))
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="TokenMultiSet30", type=highlevelnets_tokenexpressions_TokenMultisetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultisetExpression29", type=TokenMultiSet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
weight31: BinaryAssociation = BinaryAssociation(
    name="weight31",
    ends={
        Property(name="TokenWeight", type=highlevelnets_tokenexpressions_TokenMultiSet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultiSet", type=TokenWeight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type32: BinaryAssociation = BinaryAssociation(
    name="type32",
    ends={
        Property(name="TokenType34", type=highlevelnets_tokenexpressions_TokenMultiSet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultiSet33", type=TokenType, multiplicity=Multiplicity(1, 1))
    }
)
context35: BinaryAssociation = BinaryAssociation(
    name="context35",
    ends={
        Property(name="ContextVariable", type=highlevelnets_tokenexpressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=ContextVariable, multiplicity=Multiplicity(1, 1))
    }
)
arcs56: BinaryAssociation = BinaryAssociation(
    name="arcs56",
    ends={
        Property(name="Arc", type=highlevelnets_hlpn_HighLevelPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net57", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outArcs58: BinaryAssociation = BinaryAssociation(
    name="outArcs58",
    ends={
        Property(name="ArcPT", type=highlevelnets_hlpn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ArcPT, multiplicity=Multiplicity(0, 9999))
    }
)
inArcs59: BinaryAssociation = BinaryAssociation(
    name="inArcs59",
    ends={
        Property(name="ArcTP", type=highlevelnets_hlpn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ArcTP, multiplicity=Multiplicity(0, 9999))
    }
)
type60: BinaryAssociation = BinaryAssociation(
    name="type60",
    ends={
        Property(name="TokenType61", type=highlevelnets_hlpn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_hlpn_Place", type=TokenType, multiplicity=Multiplicity(1, 1))
    }
)
inArcs62: BinaryAssociation = BinaryAssociation(
    name="inArcs62",
    ends={
        Property(name="ArcPT64", type=highlevelnets_hlpn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="target63", type=ArcPT, multiplicity=Multiplicity(0, 9999))
    }
)
outArcs65: BinaryAssociation = BinaryAssociation(
    name="outArcs65",
    ends={
        Property(name="ArcTP67", type=highlevelnets_hlpn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="source66", type=ArcTP, multiplicity=Multiplicity(0, 9999))
    }
)
binding53: BinaryAssociation = BinaryAssociation(
    name="binding53",
    ends={
        Property(name="TokenBinding54", type=highlevelnets_tokenexpressions_NetConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_NetConstant", type=TokenBinding, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodes55: BinaryAssociation = BinaryAssociation(
    name="nodes55",
    ends={
        Property(name="Node", type=highlevelnets_hlpn_HighLevelPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables81: BinaryAssociation = BinaryAssociation(
    name="variables81",
    ends={
        Property(name="Variable82", type=highlevelnets_hlpn_ContextVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net83: BinaryAssociation = BinaryAssociation(
    name="net83",
    ends={
        Property(name="HighLevelPetriNet84", type=highlevelnets_hlpn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
net85: BinaryAssociation = BinaryAssociation(
    name="net85",
    ends={
        Property(name="HighLevelPetriNet86", type=highlevelnets_hlpn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
netSystem87: BinaryAssociation = BinaryAssociation(
    name="netSystem87",
    ends={
        Property(name="HighLevelPetriNet88", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeElementNet89: BinaryAssociation = BinaryAssociation(
    name="typeElementNet89",
    ends={
        Property(name="TokenTypeElementNet91", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet90", type=TokenTypeElementNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeAtomic92: BinaryAssociation = BinaryAssociation(
    name="typeAtomic92",
    ends={
        Property(name="TokenTypeAtomic94", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet93", type=TokenTypeAtomic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source68: BinaryAssociation = BinaryAssociation(
    name="source68",
    ends={
        Property(name="Place69", type=highlevelnets_hlpn_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="outArcs", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
target70: BinaryAssociation = BinaryAssociation(
    name="target70",
    ends={
        Property(name="Transition", type=highlevelnets_hlpn_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="inArcs", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
inscription71: BinaryAssociation = BinaryAssociation(
    name="inscription71",
    ends={
        Property(name="TokenVariadicExpression72", type=highlevelnets_hlpn_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_hlpn_ArcPT", type=TokenVariadicExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source73: BinaryAssociation = BinaryAssociation(
    name="source73",
    ends={
        Property(name="Transition75", type=highlevelnets_hlpn_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="outArcs74", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
target76: BinaryAssociation = BinaryAssociation(
    name="target76",
    ends={
        Property(name="Place78", type=highlevelnets_hlpn_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="inArcs77", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
inscription79: BinaryAssociation = BinaryAssociation(
    name="inscription79",
    ends={
        Property(name="TokenVariadicExpression80", type=highlevelnets_hlpn_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_hlpn_ArcTP", type=TokenVariadicExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
synchronization105: BinaryAssociation = BinaryAssociation(
    name="synchronization105",
    ends={
        Property(name="Synchronization106", type=highlevelnets_npnets_TransitionSynchronized, multiplicity=Multiplicity(1, 1)),
        Property(name="involved", type=Synchronization, multiplicity=Multiplicity(0, 1))
    }
)
diagram107: BinaryAssociation = BinaryAssociation(
    name="diagram107",
    ends={
        Property(name="NPNDiagramNetSystem", type=highlevelnets_common_IDiagramHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="host108", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
host109: BinaryAssociation = BinaryAssociation(
    name="host109",
    ends={
        Property(name="IDiagramHolder", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=IDiagramHolder, multiplicity=Multiplicity(1, 1))
    }
)
netConstants95: BinaryAssociation = BinaryAssociation(
    name="netConstants95",
    ends={
        Property(name="NetConstant", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet96", type=NetConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronizations97: BinaryAssociation = BinaryAssociation(
    name="synchronizations97",
    ends={
        Property(name="Synchronization", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet98", type=Synchronization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
host99: BinaryAssociation = BinaryAssociation(
    name="host99",
    ends={
        Property(name="NPnetMarked", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="net100", type=NPnetMarked, multiplicity=Multiplicity(1, 1))
    }
)
net101: BinaryAssociation = BinaryAssociation(
    name="net101",
    ends={
        Property(name="NPnet", type=highlevelnets_npnets_NPnetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="host", type=NPnet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
marking102: BinaryAssociation = BinaryAssociation(
    name="marking102",
    ends={
        Property(name="Marking103", type=highlevelnets_npnets_NPnetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnetMarked", type=Marking, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
involved104: BinaryAssociation = BinaryAssociation(
    name="involved104",
    ends={
        Property(name="TransitionSynchronized", type=highlevelnets_npnets_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronization", type=TransitionSynchronized, multiplicity=Multiplicity(0, 9999))
    }
)
target126: BinaryAssociation = BinaryAssociation(
    name="target126",
    ends={
        Property(name="NPNSymbolTransitionSN", type=highlevelnets_npndiagrams_NPNSymbolArcPTSN, multiplicity=Multiplicity(1, 1)),
        Property(name="inArcs127", type=NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1))
    }
)
source128: BinaryAssociation = BinaryAssociation(
    name="source128",
    ends={
        Property(name="NPNSymbolPlaceSN", type=highlevelnets_npndiagrams_NPNSymbolArcPTSN, multiplicity=Multiplicity(1, 1)),
        Property(name="outArcs129", type=NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1))
    }
)
target130: BinaryAssociation = BinaryAssociation(
    name="target130",
    ends={
        Property(name="NPNSymbolPlaceSN132", type=highlevelnets_npndiagrams_NPNSymbolArcTPSN, multiplicity=Multiplicity(1, 1)),
        Property(name="inArcs131", type=NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1))
    }
)
source133: BinaryAssociation = BinaryAssociation(
    name="source133",
    ends={
        Property(name="NPNSymbolTransitionSN135", type=highlevelnets_npndiagrams_NPNSymbolArcTPSN, multiplicity=Multiplicity(1, 1)),
        Property(name="outArcs134", type=NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1))
    }
)
diagram136: BinaryAssociation = BinaryAssociation(
    name="diagram136",
    ends={
        Property(name="NPNDiagramNetSystem138", type=highlevelnets_npndiagrams_NPNSymbolNodeSN, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes137", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1))
    }
)
model139: BinaryAssociation = BinaryAssociation(
    name="model139",
    ends={
        Property(name="Node140", type=highlevelnets_npndiagrams_NPNSymbolNodeSN, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNSymbolNodeSN", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
diagram141: BinaryAssociation = BinaryAssociation(
    name="diagram141",
    ends={
        Property(name="NPNDiagramNetSystem143", type=highlevelnets_npndiagrams_NPNSymbolArcSN, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs142", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1))
    }
)
model144: BinaryAssociation = BinaryAssociation(
    name="model144",
    ends={
        Property(name="Arc145", type=highlevelnets_npndiagrams_NPNSymbolArcSN, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNSymbolArcSN", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
nodes110: BinaryAssociation = BinaryAssociation(
    name="nodes110",
    ends={
        Property(name="NPNSymbolNodeSN", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram111", type=NPNSymbolNodeSN, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs112: BinaryAssociation = BinaryAssociation(
    name="arcs112",
    ends={
        Property(name="NPNSymbolArcSN", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram113", type=NPNSymbolArcSN, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model114: BinaryAssociation = BinaryAssociation(
    name="model114",
    ends={
        Property(name="HighLevelPetriNet115", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNDiagramNetSystem", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outArcs116: BinaryAssociation = BinaryAssociation(
    name="outArcs116",
    ends={
        Property(name="NPNSymbolArcPTSN", type=highlevelnets_npndiagrams_NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1)),
        Property(name="source117", type=NPNSymbolArcPTSN, multiplicity=Multiplicity(0, 9999))
    }
)
inArcs118: BinaryAssociation = BinaryAssociation(
    name="inArcs118",
    ends={
        Property(name="NPNSymbolArcTPSN", type=highlevelnets_npndiagrams_NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1)),
        Property(name="target119", type=NPNSymbolArcTPSN, multiplicity=Multiplicity(0, 9999))
    }
)
outArcs120: BinaryAssociation = BinaryAssociation(
    name="outArcs120",
    ends={
        Property(name="NPNSymbolArcTPSN122", type=highlevelnets_npndiagrams_NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1)),
        Property(name="source121", type=NPNSymbolArcTPSN, multiplicity=Multiplicity(0, 9999))
    }
)
inArcs123: BinaryAssociation = BinaryAssociation(
    name="inArcs123",
    ends={
        Property(name="NPNSymbolArcPTSN125", type=highlevelnets_npndiagrams_NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1)),
        Property(name="target124", type=NPNSymbolArcPTSN, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_highlevelnets_marking_PlaceMarking_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_marking_PlaceMarking)
gen_highlevelnets_marking_HighLevelPetriNetMarked_INetElement = Generalization(general=INetElement, specific=highlevelnets_marking_HighLevelPetriNetMarked)
gen_highlevelnets_tokentypes_TokenType_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_TokenType)
gen_highlevelnets_tokentypes_TokenTypeAtomic_TokenType = Generalization(general=TokenType, specific=highlevelnets_tokentypes_TokenTypeAtomic)
gen_highlevelnets_tokentypes_TokenTypeElementNet_tokentypes_TokenType = Generalization(general=tokentypes_TokenType, specific=highlevelnets_tokentypes_TokenTypeElementNet)
gen_highlevelnets_tokentypes_TokenTypeElementNet_common_IDiagramHolder = Generalization(general=common_IDiagramHolder, specific=highlevelnets_tokentypes_TokenTypeElementNet)
gen_highlevelnets_marking_Marking_INetElement = Generalization(general=INetElement, specific=highlevelnets_marking_Marking)
gen_highlevelnets_tokentypes_TokenAtomic_Token = Generalization(general=Token, specific=highlevelnets_tokentypes_TokenAtomic)
gen_highlevelnets_tokentypes_TokenNet_Token = Generalization(general=Token, specific=highlevelnets_tokentypes_TokenNet)
gen_highlevelnets_tokentypes_TokenAttribute_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokentypes_TokenAttribute)
gen_highlevelnets_tokentypes_ElementNetMarked_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_ElementNetMarked)
gen_highlevelnets_tokentypes_Atom_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_Atom)
gen_highlevelnets_tokenexpressions_TokenWeight_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenWeight)
gen_highlevelnets_tokenexpressions_TokenMultisetExpression_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenMultisetExpression)
gen_highlevelnets_tokentypes_Token_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_Token)
gen_highlevelnets_tokenexpressions_TokenVariadicExpression_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokenexpressions_TokenVariadicExpression)
gen_highlevelnets_tokenexpressions_Monom_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_Monom)
gen_highlevelnets_tokenexpressions_TokenExpressionBinding_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenExpressionBinding)
gen_highlevelnets_tokenexpressions_TokenBinding_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenBinding)
gen_highlevelnets_tokenexpressions_MonomConstant_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_MonomConstant)
gen_highlevelnets_tokenexpressions_TokenMultiSet_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenMultiSet)
gen_highlevelnets_tokenexpressions_Variable_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_Variable)
gen_highlevelnets_hlpn_Place_Node = Generalization(general=Node, specific=highlevelnets_hlpn_Place)
gen_highlevelnets_hlpn_Transition_hlpn_ContextVariable = Generalization(general=hlpn_ContextVariable, specific=highlevelnets_hlpn_Transition)
gen_highlevelnets_hlpn_Transition_hlpn_Node = Generalization(general=hlpn_Node, specific=highlevelnets_hlpn_Transition)
gen_highlevelnets_hlpn_ArcPT_Arc = Generalization(general=Arc, specific=highlevelnets_hlpn_ArcPT)
gen_highlevelnets_tokenexpressions_NetConstant_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokenexpressions_NetConstant)
gen_highlevelnets_hlpn_HighLevelPetriNet_common_INetElement = Generalization(general=common_INetElement, specific=highlevelnets_hlpn_HighLevelPetriNet)
gen_highlevelnets_hlpn_HighLevelPetriNet_hlpn_ContextVariable = Generalization(general=hlpn_ContextVariable, specific=highlevelnets_hlpn_HighLevelPetriNet)
gen_highlevelnets_hlpn_Node_INetElement = Generalization(general=INetElement, specific=highlevelnets_hlpn_Node)
gen_highlevelnets_hlpn_Arc_INetElement = Generalization(general=INetElement, specific=highlevelnets_hlpn_Arc)
gen_highlevelnets_npnets_NPnet_IDiagramHolder = Generalization(general=IDiagramHolder, specific=highlevelnets_npnets_NPnet)
gen_highlevelnets_hlpn_ArcTP_Arc = Generalization(general=Arc, specific=highlevelnets_hlpn_ArcTP)
gen_highlevelnets_hlpn_ContextVariable_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_hlpn_ContextVariable)
gen_highlevelnets_npnets_TransitionSynchronized_Transition = Generalization(general=Transition, specific=highlevelnets_npnets_TransitionSynchronized)
gen_highlevelnets_common_INetElement_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_common_INetElement)
gen_highlevelnets_common_IDiagramHolder_INetElement = Generalization(general=INetElement, specific=highlevelnets_common_IDiagramHolder)
gen_highlevelnets_npndiagrams_NPNDiagramNetSystem_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNDiagramNetSystem)
gen_highlevelnets_npnets_NPnetMarked_INetElement = Generalization(general=INetElement, specific=highlevelnets_npnets_NPnetMarked)
gen_highlevelnets_npnets_Synchronization_INetElement = Generalization(general=INetElement, specific=highlevelnets_npnets_Synchronization)
gen_highlevelnets_npndiagrams_NPNSymbolArcPTSN_NPNSymbolArcSN = Generalization(general=NPNSymbolArcSN, specific=highlevelnets_npndiagrams_NPNSymbolArcPTSN)
gen_highlevelnets_npndiagrams_NPNSymbolArcTPSN_NPNSymbolArcSN = Generalization(general=NPNSymbolArcSN, specific=highlevelnets_npndiagrams_NPNSymbolArcTPSN)
gen_highlevelnets_npndiagrams_NPNSymbolNodeSN_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNSymbolNodeSN)
gen_highlevelnets_npndiagrams_NPNSymbolArcSN_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNSymbolArcSN)
gen_highlevelnets_npndiagrams_NPNSymbolPlaceSN_NPNSymbolNodeSN = Generalization(general=NPNSymbolNodeSN, specific=highlevelnets_npndiagrams_NPNSymbolPlaceSN)
gen_highlevelnets_npndiagrams_NPNSymbolTransitionSN_NPNSymbolNodeSN = Generalization(general=NPNSymbolNodeSN, specific=highlevelnets_npndiagrams_NPNSymbolTransitionSN)

# Domain Model
domain_model = DomainModel(
    name="highlevelnets",
    types={highlevelnets_marking_PlaceMarking, IEntityIdentifiable, Place, TokenMultiSet, highlevelnets_marking_HighLevelPetriNetMarked, HighLevelPetriNet, Marking, highlevelnets_tokentypes_TokenType, highlevelnets_tokentypes_TokenTypeAtomic, TokenType, Atom, TokenAtomic, highlevelnets_tokentypes_TokenTypeElementNet, tokentypes_TokenType, common_IDiagramHolder, highlevelnets_marking_Marking, INetElement, PlaceMarking, highlevelnets_tokentypes_TokenAtomic, Token, TokenTypeAtomic, highlevelnets_tokentypes_TokenNet, TokenTypeElementNet, highlevelnets_tokentypes_TokenAttribute, highlevelnets_tokentypes_ElementNetMarked, highlevelnets_tokentypes_Atom, highlevelnets_tokenexpressions_TokenWeight, highlevelnets_tokenexpressions_TokenMultisetExpression, ElementNetMarked, TokenNet, highlevelnets_tokentypes_Token, TokenAttribute, Monom, MonomConstant, highlevelnets_tokenexpressions_Monom, Variable, highlevelnets_tokenexpressions_TokenExpressionBinding, TokenVariadicExpression, TokenBinding, highlevelnets_tokenexpressions_TokenBinding, highlevelnets_tokenexpressions_MonomConstant, highlevelnets_tokenexpressions_NetConstant, highlevelnets_tokenexpressions_TokenMultiSet, TokenWeight, highlevelnets_tokenexpressions_Variable, ContextVariable, highlevelnets_tokenexpressions_TokenVariadicExpression, Arc, highlevelnets_hlpn_Place, ArcPT, ArcTP, highlevelnets_hlpn_Transition, hlpn_Node, highlevelnets_hlpn_ArcPT, highlevelnets_hlpn_HighLevelPetriNet, common_INetElement, hlpn_ContextVariable, Node, highlevelnets_hlpn_Node, highlevelnets_hlpn_Arc, highlevelnets_npnets_NPnet, IDiagramHolder, Transition, highlevelnets_hlpn_ArcTP, highlevelnets_hlpn_ContextVariable, highlevelnets_npnets_TransitionSynchronized, highlevelnets_common_INetElement, highlevelnets_common_IEntityIdentifiable, highlevelnets_common_IDiagramHolder, NPNDiagramNetSystem, highlevelnets_npndiagrams_NPNDiagramNetSystem, NetConstant, Synchronization, NPnetMarked, highlevelnets_npnets_NPnetMarked, NPnet, highlevelnets_npnets_Synchronization, TransitionSynchronized, highlevelnets_npndiagrams_NPNSymbolArcPTSN, NPNSymbolTransitionSN, NPNSymbolPlaceSN, highlevelnets_npndiagrams_NPNSymbolArcTPSN, highlevelnets_npndiagrams_NPNSymbolNodeSN, highlevelnets_npndiagrams_NPNSymbolArcSN, NPNSymbolNodeSN, NPNSymbolArcSN, highlevelnets_npndiagrams_NPNSymbolPlaceSN, NPNSymbolArcPTSN, NPNSymbolArcTPSN, highlevelnets_npndiagrams_NPNSymbolTransitionSN, ESynchronizationKind},
    associations={map0, place1, marking2, net4, marking5, instance7, atom8, type16, value17, type19, value20, type22, marking24, token26, type27, elementNetMarkeds9, net11, tokenNets13, attribute15, monoms36, monomConstants37, variable39, expression40, bindingTokens41, variable43, value45, constant48, value50, value28, weight31, type32, context35, arcs56, outArcs58, inArcs59, type60, inArcs62, outArcs65, binding53, nodes55, variables81, net83, net85, netSystem87, typeElementNet89, typeAtomic92, source68, target70, inscription71, source73, target76, inscription79, synchronization105, diagram107, host109, netConstants95, synchronizations97, host99, net101, marking102, involved104, target126, source128, target130, source133, diagram136, model139, diagram141, model144, nodes110, arcs112, model114, outArcs116, inArcs118, outArcs120, inArcs123},
    generalizations={gen_highlevelnets_marking_PlaceMarking_IEntityIdentifiable, gen_highlevelnets_marking_HighLevelPetriNetMarked_INetElement, gen_highlevelnets_tokentypes_TokenType_INetElement, gen_highlevelnets_tokentypes_TokenTypeAtomic_TokenType, gen_highlevelnets_tokentypes_TokenTypeElementNet_tokentypes_TokenType, gen_highlevelnets_tokentypes_TokenTypeElementNet_common_IDiagramHolder, gen_highlevelnets_marking_Marking_INetElement, gen_highlevelnets_tokentypes_TokenAtomic_Token, gen_highlevelnets_tokentypes_TokenNet_Token, gen_highlevelnets_tokentypes_TokenAttribute_IEntityIdentifiable, gen_highlevelnets_tokentypes_ElementNetMarked_INetElement, gen_highlevelnets_tokentypes_Atom_INetElement, gen_highlevelnets_tokenexpressions_TokenWeight_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenMultisetExpression_IEntityIdentifiable, gen_highlevelnets_tokentypes_Token_INetElement, gen_highlevelnets_tokenexpressions_TokenVariadicExpression_INetElement, gen_highlevelnets_tokenexpressions_Monom_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenExpressionBinding_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenBinding_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_MonomConstant_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenMultiSet_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_Variable_IEntityIdentifiable, gen_highlevelnets_hlpn_Place_Node, gen_highlevelnets_hlpn_Transition_hlpn_ContextVariable, gen_highlevelnets_hlpn_Transition_hlpn_Node, gen_highlevelnets_hlpn_ArcPT_Arc, gen_highlevelnets_tokenexpressions_NetConstant_INetElement, gen_highlevelnets_hlpn_HighLevelPetriNet_common_INetElement, gen_highlevelnets_hlpn_HighLevelPetriNet_hlpn_ContextVariable, gen_highlevelnets_hlpn_Node_INetElement, gen_highlevelnets_hlpn_Arc_INetElement, gen_highlevelnets_npnets_NPnet_IDiagramHolder, gen_highlevelnets_hlpn_ArcTP_Arc, gen_highlevelnets_hlpn_ContextVariable_IEntityIdentifiable, gen_highlevelnets_npnets_TransitionSynchronized_Transition, gen_highlevelnets_common_INetElement_IEntityIdentifiable, gen_highlevelnets_common_IDiagramHolder_INetElement, gen_highlevelnets_npndiagrams_NPNDiagramNetSystem_IEntityIdentifiable, gen_highlevelnets_npnets_NPnetMarked_INetElement, gen_highlevelnets_npnets_Synchronization_INetElement, gen_highlevelnets_npndiagrams_NPNSymbolArcPTSN_NPNSymbolArcSN, gen_highlevelnets_npndiagrams_NPNSymbolArcTPSN_NPNSymbolArcSN, gen_highlevelnets_npndiagrams_NPNSymbolNodeSN_IEntityIdentifiable, gen_highlevelnets_npndiagrams_NPNSymbolArcSN_IEntityIdentifiable, gen_highlevelnets_npndiagrams_NPNSymbolPlaceSN_NPNSymbolNodeSN, gen_highlevelnets_npndiagrams_NPNSymbolTransitionSN_NPNSymbolNodeSN},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)