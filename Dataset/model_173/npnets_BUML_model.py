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
highlevelnets_marking_Marking = Class(name="highlevelnets::marking::Marking")
highlevelnets_marking_HighLevelPetriNetMarked = Class(name="highlevelnets::marking::HighLevelPetriNetMarked")
HighLevelPetriNet = Class(name="HighLevelPetriNet")
Marking = Class(name="Marking")
INetElement = Class(name="INetElement")
PlaceMarking = Class(name="PlaceMarking")
highlevelnets_marking_PlaceMarking = Class(name="highlevelnets::marking::PlaceMarking")
IEntityIdentifiable = Class(name="IEntityIdentifiable")
Place = Class(name="Place")
TokenMultiSet = Class(name="TokenMultiSet")
ElementNetMarked = Class(name="ElementNetMarked")
TokenNet = Class(name="TokenNet")
highlevelnets_tokentypes_TokenType = Class(name="highlevelnets::tokentypes::TokenType", is_abstract=True)
highlevelnets_tokentypes_TokenTypeAtomic = Class(name="highlevelnets::tokentypes::TokenTypeAtomic")
TokenType = Class(name="TokenType")
Atom = Class(name="Atom")
TokenAtomic = Class(name="TokenAtomic")
highlevelnets_tokentypes_TokenTypeElementNet = Class(name="highlevelnets::tokentypes::TokenTypeElementNet")
highlevelnets_tokentypes_TokenNet = Class(name="highlevelnets::tokentypes::TokenNet")
TokenTypeElementNet = Class(name="TokenTypeElementNet")
highlevelnets_tokentypes_TokenAttribute = Class(name="highlevelnets::tokentypes::TokenAttribute")
highlevelnets_tokentypes_Token = Class(name="highlevelnets::tokentypes::Token", is_abstract=True)
TokenAttribute = Class(name="TokenAttribute")
highlevelnets_tokentypes_TokenAtomic = Class(name="highlevelnets::tokentypes::TokenAtomic")
Token = Class(name="Token")
TokenTypeAtomic = Class(name="TokenTypeAtomic")
highlevelnets_tokenexpressions_TokenWeight = Class(name="highlevelnets::tokenexpressions::TokenWeight")
highlevelnets_tokenexpressions_TokenMultisetExpression = Class(name="highlevelnets::tokenexpressions::TokenMultisetExpression")
highlevelnets_tokentypes_ElementNetMarked = Class(name="highlevelnets::tokentypes::ElementNetMarked")
highlevelnets_tokentypes_Atom = Class(name="highlevelnets::tokentypes::Atom")
highlevelnets_tokenexpressions_Variable = Class(name="highlevelnets::tokenexpressions::Variable")
ContextVariable = Class(name="ContextVariable")
highlevelnets_tokenexpressions_TokenVariadicExpression = Class(name="highlevelnets::tokenexpressions::TokenVariadicExpression")
highlevelnets_tokenexpressions_TokenMultiSet = Class(name="highlevelnets::tokenexpressions::TokenMultiSet")
TokenWeight = Class(name="TokenWeight")
TokenVariadicExpression = Class(name="TokenVariadicExpression")
TokenBinding = Class(name="TokenBinding")
highlevelnets_tokenexpressions_TokenBinding = Class(name="highlevelnets::tokenexpressions::TokenBinding")
Monom = Class(name="Monom")
MonomConstant = Class(name="MonomConstant")
highlevelnets_tokenexpressions_Monom = Class(name="highlevelnets::tokenexpressions::Monom")
Variable = Class(name="Variable")
highlevelnets_tokenexpressions_TokenExpressionBinding = Class(name="highlevelnets::tokenexpressions::TokenExpressionBinding")
highlevelnets_hlpn_HighLevelPetriNet = Class(name="highlevelnets::hlpn::HighLevelPetriNet")
common_INetElement = Class(name="common::INetElement")
hlpn_ContextVariable = Class(name="hlpn::ContextVariable")
highlevelnets_tokenexpressions_MonomConstant = Class(name="highlevelnets::tokenexpressions::MonomConstant")
highlevelnets_tokenexpressions_NetConstant = Class(name="highlevelnets::tokenexpressions::NetConstant")
highlevelnets_hlpn_Transition = Class(name="highlevelnets::hlpn::Transition")
hlpn_Node = Class(name="hlpn::Node")
Node = Class(name="Node")
Arc = Class(name="Arc")
highlevelnets_hlpn_Place = Class(name="highlevelnets::hlpn::Place")
ArcPT = Class(name="ArcPT")
ArcTP = Class(name="ArcTP")
highlevelnets_hlpn_ArcPT = Class(name="highlevelnets::hlpn::ArcPT")
Transition = Class(name="Transition")
highlevelnets_hlpn_ArcTP = Class(name="highlevelnets::hlpn::ArcTP")
highlevelnets_hlpn_Arc = Class(name="highlevelnets::hlpn::Arc", is_abstract=True)
highlevelnets_npnets_NPnet = Class(name="highlevelnets::npnets::NPnet")
highlevelnets_hlpn_ContextVariable = Class(name="highlevelnets::hlpn::ContextVariable", is_abstract=True)
highlevelnets_hlpn_Node = Class(name="highlevelnets::hlpn::Node", is_abstract=True)
highlevelnets_npnets_NPnetMarked = Class(name="highlevelnets::npnets::NPnetMarked")
NPnet = Class(name="NPnet")
NetConstant = Class(name="NetConstant")
Synchronization = Class(name="Synchronization")
highlevelnets_npnets_TransitionSynchronized = Class(name="highlevelnets::npnets::TransitionSynchronized")
highlevelnets_common_INetElement = Class(name="highlevelnets::common::INetElement", is_abstract=True)
NPNDiagramNetSystem = Class(name="NPNDiagramNetSystem")
highlevelnets_npnets_Synchronization = Class(name="highlevelnets::npnets::Synchronization")
TransitionSynchronized = Class(name="TransitionSynchronized")
NPnetMarked = Class(name="NPnetMarked")
highlevelnets_npndiagrams_NPNDiagramNetSystem = Class(name="highlevelnets::npndiagrams::NPNDiagramNetSystem")
NPNSymbolNodeSN = Class(name="NPNSymbolNodeSN")
highlevelnets_common_IEntityIdentifiable = Class(name="highlevelnets::common::IEntityIdentifiable", is_abstract=True)
highlevelnets_npndiagrams_NPNDiagramNPNMarked = Class(name="highlevelnets::npndiagrams::NPNDiagramNPNMarked")
NPNSymbolTokenSN = Class(name="NPNSymbolTokenSN")
highlevelnets_npndiagrams_NPNSymbolTransitionSN = Class(name="highlevelnets::npndiagrams::NPNSymbolTransitionSN")
NPNSymbolArcSN = Class(name="NPNSymbolArcSN")
highlevelnets_npndiagrams_NPNSymbolPlaceSN = Class(name="highlevelnets::npndiagrams::NPNSymbolPlaceSN")
NPNSymbolArcPTSN = Class(name="NPNSymbolArcPTSN")
NPNSymbolArcTPSN = Class(name="NPNSymbolArcTPSN")
highlevelnets_npndiagrams_NPNSymbolNodeSN = Class(name="highlevelnets::npndiagrams::NPNSymbolNodeSN", is_abstract=True)
highlevelnets_npndiagrams_NPNSymbolArcPTSN = Class(name="highlevelnets::npndiagrams::NPNSymbolArcPTSN")
NPNSymbolTransitionSN = Class(name="NPNSymbolTransitionSN")
NPNSymbolPlaceSN = Class(name="NPNSymbolPlaceSN")
highlevelnets_npndiagrams_NPNSymbolArcTPSN = Class(name="highlevelnets::npndiagrams::NPNSymbolArcTPSN")
highlevelnets_npndiagrams_NPNSymbolTokenSN = Class(name="highlevelnets::npndiagrams::NPNSymbolTokenSN")
highlevelnets_npndiagrams_NPNSymbolArcSN = Class(name="highlevelnets::npndiagrams::NPNSymbolArcSN", is_abstract=True)

# highlevelnets_marking_Marking class attributes and methods

# highlevelnets_marking_HighLevelPetriNetMarked class attributes and methods

# HighLevelPetriNet class attributes and methods

# Marking class attributes and methods

# INetElement class attributes and methods

# PlaceMarking class attributes and methods

# highlevelnets_marking_PlaceMarking class attributes and methods

# IEntityIdentifiable class attributes and methods

# Place class attributes and methods

# TokenMultiSet class attributes and methods

# ElementNetMarked class attributes and methods

# TokenNet class attributes and methods

# highlevelnets_tokentypes_TokenType class attributes and methods

# highlevelnets_tokentypes_TokenTypeAtomic class attributes and methods

# TokenType class attributes and methods

# Atom class attributes and methods

# TokenAtomic class attributes and methods

# highlevelnets_tokentypes_TokenTypeElementNet class attributes and methods
highlevelnets_tokentypes_TokenTypeElementNet_m_createInstance: Method = Method(name="createInstance", parameters={})
highlevelnets_tokentypes_TokenTypeElementNet_m_getInstanceByID: Method = Method(name="getInstanceByID", parameters={Parameter(name='id')})
highlevelnets_tokentypes_TokenTypeElementNet.methods={highlevelnets_tokentypes_TokenTypeElementNet_m_createInstance, highlevelnets_tokentypes_TokenTypeElementNet_m_getInstanceByID}

# highlevelnets_tokentypes_TokenNet class attributes and methods

# TokenTypeElementNet class attributes and methods

# highlevelnets_tokentypes_TokenAttribute class attributes and methods
highlevelnets_tokentypes_TokenAttribute_type: Property = Property(name="type", type=StringType)
highlevelnets_tokentypes_TokenAttribute_name: Property = Property(name="name", type=StringType)
highlevelnets_tokentypes_TokenAttribute_value: Property = Property(name="value", type=StringType)
highlevelnets_tokentypes_TokenAttribute.attributes={highlevelnets_tokentypes_TokenAttribute_name, highlevelnets_tokentypes_TokenAttribute_value, highlevelnets_tokentypes_TokenAttribute_type}

# highlevelnets_tokentypes_Token class attributes and methods
highlevelnets_tokentypes_Token_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
highlevelnets_tokentypes_Token.methods={highlevelnets_tokentypes_Token_m_getType}

# TokenAttribute class attributes and methods

# highlevelnets_tokentypes_TokenAtomic class attributes and methods

# Token class attributes and methods

# TokenTypeAtomic class attributes and methods

# highlevelnets_tokenexpressions_TokenWeight class attributes and methods
highlevelnets_tokenexpressions_TokenWeight_weight: Property = Property(name="weight", type=StringType)
highlevelnets_tokenexpressions_TokenWeight.attributes={highlevelnets_tokenexpressions_TokenWeight_weight}

# highlevelnets_tokenexpressions_TokenMultisetExpression class attributes and methods

# highlevelnets_tokentypes_ElementNetMarked class attributes and methods

# highlevelnets_tokentypes_Atom class attributes and methods

# highlevelnets_tokenexpressions_Variable class attributes and methods
highlevelnets_tokenexpressions_Variable_name: Property = Property(name="name", type=StringType)
highlevelnets_tokenexpressions_Variable.attributes={highlevelnets_tokenexpressions_Variable_name}

# ContextVariable class attributes and methods

# highlevelnets_tokenexpressions_TokenVariadicExpression class attributes and methods

# highlevelnets_tokenexpressions_TokenMultiSet class attributes and methods

# TokenWeight class attributes and methods

# TokenVariadicExpression class attributes and methods

# TokenBinding class attributes and methods

# highlevelnets_tokenexpressions_TokenBinding class attributes and methods

# Monom class attributes and methods

# MonomConstant class attributes and methods

# highlevelnets_tokenexpressions_Monom class attributes and methods
highlevelnets_tokenexpressions_Monom_power: Property = Property(name="power", type=StringType)
highlevelnets_tokenexpressions_Monom.attributes={highlevelnets_tokenexpressions_Monom_power}

# Variable class attributes and methods

# highlevelnets_tokenexpressions_TokenExpressionBinding class attributes and methods

# highlevelnets_hlpn_HighLevelPetriNet class attributes and methods

# common_INetElement class attributes and methods

# hlpn_ContextVariable class attributes and methods

# highlevelnets_tokenexpressions_MonomConstant class attributes and methods
highlevelnets_tokenexpressions_MonomConstant_power: Property = Property(name="power", type=StringType)
highlevelnets_tokenexpressions_MonomConstant.attributes={highlevelnets_tokenexpressions_MonomConstant_power}

# highlevelnets_tokenexpressions_NetConstant class attributes and methods

# highlevelnets_hlpn_Transition class attributes and methods

# hlpn_Node class attributes and methods

# Node class attributes and methods

# Arc class attributes and methods

# highlevelnets_hlpn_Place class attributes and methods

# ArcPT class attributes and methods

# ArcTP class attributes and methods

# highlevelnets_hlpn_ArcPT class attributes and methods

# Transition class attributes and methods

# highlevelnets_hlpn_ArcTP class attributes and methods
highlevelnets_hlpn_ArcTP_secondTimeConstraint: Property = Property(name="secondTimeConstraint", type=IntegerType)
highlevelnets_hlpn_ArcTP_firstTimeConstraint: Property = Property(name="firstTimeConstraint", type=IntegerType)
highlevelnets_hlpn_ArcTP.attributes={highlevelnets_hlpn_ArcTP_firstTimeConstraint, highlevelnets_hlpn_ArcTP_secondTimeConstraint}

# highlevelnets_hlpn_Arc class attributes and methods

# highlevelnets_npnets_NPnet class attributes and methods

# highlevelnets_hlpn_ContextVariable class attributes and methods

# highlevelnets_hlpn_Node class attributes and methods
highlevelnets_hlpn_Node_firstTimeConstraint: Property = Property(name="firstTimeConstraint", type=IntegerType)
highlevelnets_hlpn_Node_secondTimeConstraint: Property = Property(name="secondTimeConstraint", type=IntegerType)
highlevelnets_hlpn_Node.attributes={highlevelnets_hlpn_Node_secondTimeConstraint, highlevelnets_hlpn_Node_firstTimeConstraint}

# highlevelnets_npnets_NPnetMarked class attributes and methods

# NPnet class attributes and methods

# NetConstant class attributes and methods

# Synchronization class attributes and methods

# highlevelnets_npnets_TransitionSynchronized class attributes and methods

# highlevelnets_common_INetElement class attributes and methods
highlevelnets_common_INetElement_name: Property = Property(name="name", type=StringType)
highlevelnets_common_INetElement_comment: Property = Property(name="comment", type=StringType)
highlevelnets_common_INetElement.attributes={highlevelnets_common_INetElement_name, highlevelnets_common_INetElement_comment}

# NPNDiagramNetSystem class attributes and methods

# highlevelnets_npnets_Synchronization class attributes and methods
highlevelnets_npnets_Synchronization_kind: Property = Property(name="kind", type=StringType)
highlevelnets_npnets_Synchronization_key: Property = Property(name="key", type=StringType)
highlevelnets_npnets_Synchronization.attributes={highlevelnets_npnets_Synchronization_key, highlevelnets_npnets_Synchronization_kind}

# TransitionSynchronized class attributes and methods

# NPnetMarked class attributes and methods

# highlevelnets_npndiagrams_NPNDiagramNetSystem class attributes and methods

# NPNSymbolNodeSN class attributes and methods

# highlevelnets_common_IEntityIdentifiable class attributes and methods
highlevelnets_common_IEntityIdentifiable_uuid: Property = Property(name="uuid", type=StringType)
highlevelnets_common_IEntityIdentifiable.attributes={highlevelnets_common_IEntityIdentifiable_uuid}

# highlevelnets_npndiagrams_NPNDiagramNPNMarked class attributes and methods

# NPNSymbolTokenSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolTransitionSN class attributes and methods

# NPNSymbolArcSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolPlaceSN class attributes and methods

# NPNSymbolArcPTSN class attributes and methods

# NPNSymbolArcTPSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolNodeSN class attributes and methods
highlevelnets_npndiagrams_NPNSymbolNodeSN_constraints: Property = Property(name="constraints", type=StringType)
highlevelnets_npndiagrams_NPNSymbolNodeSN.attributes={highlevelnets_npndiagrams_NPNSymbolNodeSN_constraints}

# highlevelnets_npndiagrams_NPNSymbolArcPTSN class attributes and methods

# NPNSymbolTransitionSN class attributes and methods

# NPNSymbolPlaceSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolArcTPSN class attributes and methods

# highlevelnets_npndiagrams_NPNSymbolTokenSN class attributes and methods
highlevelnets_npndiagrams_NPNSymbolTokenSN_constraints: Property = Property(name="constraints", type=StringType)
highlevelnets_npndiagrams_NPNSymbolTokenSN.attributes={highlevelnets_npndiagrams_NPNSymbolTokenSN_constraints}

# highlevelnets_npndiagrams_NPNSymbolArcSN class attributes and methods
highlevelnets_npndiagrams_NPNSymbolArcSN_bendpoints: Property = Property(name="bendpoints", type=StringType)
highlevelnets_npndiagrams_NPNSymbolArcSN.attributes={highlevelnets_npndiagrams_NPNSymbolArcSN_bendpoints}

# Relationships
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
map0: BinaryAssociation = BinaryAssociation(
    name="map0",
    ends={
        Property(name="PlaceMarking", type=highlevelnets_marking_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_marking_Marking", type=PlaceMarking, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
elementNetMarkeds9: BinaryAssociation = BinaryAssociation(
    name="elementNetMarkeds9",
    ends={
        Property(name="tokentypes10", type=highlevelnets_tokentypes_TokenTypeElementNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementNetMarked", type=ElementNetMarked, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="tokentypes14", type=highlevelnets_tokentypes_TokenTypeElementNet, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenNet", type=TokenNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="tokentypes", type=highlevelnets_tokentypes_TokenTypeAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenAtomic", type=TokenAtomic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="tokentypes21", type=highlevelnets_tokentypes_TokenNet, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTypeElementNet", type=TokenTypeElementNet, multiplicity=Multiplicity(1, 1))
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="ElementNetMarked23", type=highlevelnets_tokentypes_TokenNet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_TokenNet", type=ElementNetMarked, multiplicity=Multiplicity(0, 1))
    }
)
attribute15: BinaryAssociation = BinaryAssociation(
    name="attribute15",
    ends={
        Property(name="TokenAttribute", type=highlevelnets_tokentypes_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_Token", type=TokenAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="tokentypes17", type=highlevelnets_tokentypes_TokenAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTypeAtomic", type=TokenTypeAtomic, multiplicity=Multiplicity(1, 1))
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="Atom19", type=highlevelnets_tokentypes_TokenAtomic, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_TokenAtomic", type=Atom, multiplicity=Multiplicity(1, 1))
    }
)
token29: BinaryAssociation = BinaryAssociation(
    name="token29",
    ends={
        Property(name="Token", type=highlevelnets_tokenexpressions_TokenWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenWeight", type=Token, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="tokentypes26", type=highlevelnets_tokentypes_ElementNetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTypeElementNet25", type=TokenTypeElementNet, multiplicity=Multiplicity(1, 1))
    }
)
marking27: BinaryAssociation = BinaryAssociation(
    name="marking27",
    ends={
        Property(name="Marking28", type=highlevelnets_tokentypes_ElementNetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokentypes_ElementNetMarked", type=Marking, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context38: BinaryAssociation = BinaryAssociation(
    name="context38",
    ends={
        Property(name="hlpn", type=highlevelnets_tokenexpressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ContextVariable", type=ContextVariable, multiplicity=Multiplicity(1, 1))
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="TokenType", type=highlevelnets_tokenexpressions_TokenMultisetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultisetExpression", type=TokenType, multiplicity=Multiplicity(1, 1))
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="TokenMultiSet33", type=highlevelnets_tokenexpressions_TokenMultisetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultisetExpression32", type=TokenMultiSet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
weight34: BinaryAssociation = BinaryAssociation(
    name="weight34",
    ends={
        Property(name="TokenWeight", type=highlevelnets_tokenexpressions_TokenMultiSet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultiSet", type=TokenWeight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="TokenType37", type=highlevelnets_tokenexpressions_TokenMultiSet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenMultiSet36", type=TokenType, multiplicity=Multiplicity(1, 1))
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="TokenVariadicExpression", type=highlevelnets_tokenexpressions_TokenExpressionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenExpressionBinding", type=TokenVariadicExpression, multiplicity=Multiplicity(1, 1))
    }
)
bindingTokens44: BinaryAssociation = BinaryAssociation(
    name="bindingTokens44",
    ends={
        Property(name="TokenBinding", type=highlevelnets_tokenexpressions_TokenExpressionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenExpressionBinding45", type=TokenBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monoms39: BinaryAssociation = BinaryAssociation(
    name="monoms39",
    ends={
        Property(name="Monom", type=highlevelnets_tokenexpressions_TokenVariadicExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenVariadicExpression", type=Monom, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
monomConstants40: BinaryAssociation = BinaryAssociation(
    name="monomConstants40",
    ends={
        Property(name="MonomConstant", type=highlevelnets_tokenexpressions_TokenVariadicExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenVariadicExpression41", type=MonomConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable42: BinaryAssociation = BinaryAssociation(
    name="variable42",
    ends={
        Property(name="Variable", type=highlevelnets_tokenexpressions_Monom, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_Monom", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
binding56: BinaryAssociation = BinaryAssociation(
    name="binding56",
    ends={
        Property(name="TokenBinding57", type=highlevelnets_tokenexpressions_NetConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_NetConstant", type=TokenBinding, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable46: BinaryAssociation = BinaryAssociation(
    name="variable46",
    ends={
        Property(name="Variable47", type=highlevelnets_tokenexpressions_TokenBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenBinding", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
value48: BinaryAssociation = BinaryAssociation(
    name="value48",
    ends={
        Property(name="Token50", type=highlevelnets_tokenexpressions_TokenBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_TokenBinding49", type=Token, multiplicity=Multiplicity(1, 1))
    }
)
constant51: BinaryAssociation = BinaryAssociation(
    name="constant51",
    ends={
        Property(name="Variable52", type=highlevelnets_tokenexpressions_MonomConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_MonomConstant", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="Token55", type=highlevelnets_tokenexpressions_MonomConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_tokenexpressions_MonomConstant54", type=Token, multiplicity=Multiplicity(1, 1))
    }
)
inArcs68: BinaryAssociation = BinaryAssociation(
    name="inArcs68",
    ends={
        Property(name="hlpn70", type=highlevelnets_hlpn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ArcPT69", type=ArcPT, multiplicity=Multiplicity(0, 9999))
    }
)
nodes58: BinaryAssociation = BinaryAssociation(
    name="nodes58",
    ends={
        Property(name="hlpn59", type=highlevelnets_hlpn_HighLevelPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="Node", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs60: BinaryAssociation = BinaryAssociation(
    name="arcs60",
    ends={
        Property(name="hlpn61", type=highlevelnets_hlpn_HighLevelPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="Arc", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outArcs62: BinaryAssociation = BinaryAssociation(
    name="outArcs62",
    ends={
        Property(name="hlpn63", type=highlevelnets_hlpn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ArcPT", type=ArcPT, multiplicity=Multiplicity(0, 9999))
    }
)
inArcs64: BinaryAssociation = BinaryAssociation(
    name="inArcs64",
    ends={
        Property(name="hlpn65", type=highlevelnets_hlpn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ArcTP", type=ArcTP, multiplicity=Multiplicity(0, 9999))
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="TokenType67", type=highlevelnets_hlpn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_hlpn_Place", type=TokenType, multiplicity=Multiplicity(1, 1))
    }
)
source81: BinaryAssociation = BinaryAssociation(
    name="source81",
    ends={
        Property(name="hlpn83", type=highlevelnets_hlpn_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition82", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
target84: BinaryAssociation = BinaryAssociation(
    name="target84",
    ends={
        Property(name="hlpn86", type=highlevelnets_hlpn_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="Place85", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
inscription87: BinaryAssociation = BinaryAssociation(
    name="inscription87",
    ends={
        Property(name="TokenVariadicExpression88", type=highlevelnets_hlpn_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_hlpn_ArcTP", type=TokenVariadicExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outArcs71: BinaryAssociation = BinaryAssociation(
    name="outArcs71",
    ends={
        Property(name="hlpn73", type=highlevelnets_hlpn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ArcTP72", type=ArcTP, multiplicity=Multiplicity(0, 9999))
    }
)
source74: BinaryAssociation = BinaryAssociation(
    name="source74",
    ends={
        Property(name="hlpn76", type=highlevelnets_hlpn_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="Place75", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
target77: BinaryAssociation = BinaryAssociation(
    name="target77",
    ends={
        Property(name="hlpn78", type=highlevelnets_hlpn_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
inscription79: BinaryAssociation = BinaryAssociation(
    name="inscription79",
    ends={
        Property(name="TokenVariadicExpression80", type=highlevelnets_hlpn_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_hlpn_ArcPT", type=TokenVariadicExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
net94: BinaryAssociation = BinaryAssociation(
    name="net94",
    ends={
        Property(name="hlpn96", type=highlevelnets_hlpn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="HighLevelPetriNet95", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
variables89: BinaryAssociation = BinaryAssociation(
    name="variables89",
    ends={
        Property(name="tokenexpressions", type=highlevelnets_hlpn_ContextVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable90", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net91: BinaryAssociation = BinaryAssociation(
    name="net91",
    ends={
        Property(name="hlpn93", type=highlevelnets_hlpn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="HighLevelPetriNet92", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
net109: BinaryAssociation = BinaryAssociation(
    name="net109",
    ends={
        Property(name="NPnet", type=highlevelnets_npnets_NPnetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnetMarked", type=NPnet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
marking110: BinaryAssociation = BinaryAssociation(
    name="marking110",
    ends={
        Property(name="Marking112", type=highlevelnets_npnets_NPnetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnetMarked111", type=Marking, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
netSystem97: BinaryAssociation = BinaryAssociation(
    name="netSystem97",
    ends={
        Property(name="HighLevelPetriNet98", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeElementNet99: BinaryAssociation = BinaryAssociation(
    name="typeElementNet99",
    ends={
        Property(name="TokenTypeElementNet101", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet100", type=TokenTypeElementNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeAtomic102: BinaryAssociation = BinaryAssociation(
    name="typeAtomic102",
    ends={
        Property(name="TokenTypeAtomic104", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet103", type=TokenTypeAtomic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
netConstants105: BinaryAssociation = BinaryAssociation(
    name="netConstants105",
    ends={
        Property(name="NetConstant", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet106", type=NetConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronizations107: BinaryAssociation = BinaryAssociation(
    name="synchronizations107",
    ends={
        Property(name="Synchronization", type=highlevelnets_npnets_NPnet, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnet108", type=Synchronization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronization116: BinaryAssociation = BinaryAssociation(
    name="synchronization116",
    ends={
        Property(name="npnets118", type=highlevelnets_npnets_TransitionSynchronized, multiplicity=Multiplicity(1, 1)),
        Property(name="Synchronization117", type=Synchronization, multiplicity=Multiplicity(0, 1))
    }
)
diagramNetSystem113: BinaryAssociation = BinaryAssociation(
    name="diagramNetSystem113",
    ends={
        Property(name="NPNDiagramNetSystem", type=highlevelnets_npnets_NPnetMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npnets_NPnetMarked114", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
involved115: BinaryAssociation = BinaryAssociation(
    name="involved115",
    ends={
        Property(name="npnets", type=highlevelnets_npnets_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="TransitionSynchronized", type=TransitionSynchronized, multiplicity=Multiplicity(0, 9999))
    }
)
model121: BinaryAssociation = BinaryAssociation(
    name="model121",
    ends={
        Property(name="NPnetMarked", type=highlevelnets_npndiagrams_NPNDiagramNPNMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNDiagramNPNMarked122", type=NPnetMarked, multiplicity=Multiplicity(1, 1))
    }
)
model123: BinaryAssociation = BinaryAssociation(
    name="model123",
    ends={
        Property(name="HighLevelPetriNet124", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNDiagramNetSystem", type=HighLevelPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
diagramNetSystem119: BinaryAssociation = BinaryAssociation(
    name="diagramNetSystem119",
    ends={
        Property(name="NPNDiagramNetSystem120", type=highlevelnets_npndiagrams_NPNDiagramNPNMarked, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNDiagramNPNMarked", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1))
    }
)
tokens132: BinaryAssociation = BinaryAssociation(
    name="tokens132",
    ends={
        Property(name="npndiagrams133", type=highlevelnets_npndiagrams_NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolTokenSN", type=NPNSymbolTokenSN, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outArcs134: BinaryAssociation = BinaryAssociation(
    name="outArcs134",
    ends={
        Property(name="npndiagrams136", type=highlevelnets_npndiagrams_NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolArcTPSN135", type=NPNSymbolArcTPSN, multiplicity=Multiplicity(0, 9999))
    }
)
nodes125: BinaryAssociation = BinaryAssociation(
    name="nodes125",
    ends={
        Property(name="npndiagrams", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolNodeSN", type=NPNSymbolNodeSN, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs126: BinaryAssociation = BinaryAssociation(
    name="arcs126",
    ends={
        Property(name="npndiagrams127", type=highlevelnets_npndiagrams_NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolArcSN", type=NPNSymbolArcSN, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outArcs128: BinaryAssociation = BinaryAssociation(
    name="outArcs128",
    ends={
        Property(name="npndiagrams129", type=highlevelnets_npndiagrams_NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolArcPTSN", type=NPNSymbolArcPTSN, multiplicity=Multiplicity(0, 9999))
    }
)
inArcs130: BinaryAssociation = BinaryAssociation(
    name="inArcs130",
    ends={
        Property(name="npndiagrams131", type=highlevelnets_npndiagrams_NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolArcTPSN", type=NPNSymbolArcTPSN, multiplicity=Multiplicity(0, 9999))
    }
)
source147: BinaryAssociation = BinaryAssociation(
    name="source147",
    ends={
        Property(name="npndiagrams149", type=highlevelnets_npndiagrams_NPNSymbolArcTPSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolTransitionSN148", type=NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1))
    }
)
diagram150: BinaryAssociation = BinaryAssociation(
    name="diagram150",
    ends={
        Property(name="npndiagrams152", type=highlevelnets_npndiagrams_NPNSymbolNodeSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNDiagramNetSystem151", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1))
    }
)
inArcs137: BinaryAssociation = BinaryAssociation(
    name="inArcs137",
    ends={
        Property(name="npndiagrams139", type=highlevelnets_npndiagrams_NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolArcPTSN138", type=NPNSymbolArcPTSN, multiplicity=Multiplicity(0, 9999))
    }
)
target140: BinaryAssociation = BinaryAssociation(
    name="target140",
    ends={
        Property(name="npndiagrams141", type=highlevelnets_npndiagrams_NPNSymbolArcPTSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolTransitionSN", type=NPNSymbolTransitionSN, multiplicity=Multiplicity(1, 1))
    }
)
source142: BinaryAssociation = BinaryAssociation(
    name="source142",
    ends={
        Property(name="npndiagrams143", type=highlevelnets_npndiagrams_NPNSymbolArcPTSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolPlaceSN", type=NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1))
    }
)
target144: BinaryAssociation = BinaryAssociation(
    name="target144",
    ends={
        Property(name="npndiagrams146", type=highlevelnets_npndiagrams_NPNSymbolArcTPSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolPlaceSN145", type=NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1))
    }
)
place160: BinaryAssociation = BinaryAssociation(
    name="place160",
    ends={
        Property(name="npndiagrams162", type=highlevelnets_npndiagrams_NPNSymbolTokenSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNSymbolPlaceSN161", type=NPNSymbolPlaceSN, multiplicity=Multiplicity(1, 1))
    }
)
model153: BinaryAssociation = BinaryAssociation(
    name="model153",
    ends={
        Property(name="Node154", type=highlevelnets_npndiagrams_NPNSymbolNodeSN, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNSymbolNodeSN", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
diagram155: BinaryAssociation = BinaryAssociation(
    name="diagram155",
    ends={
        Property(name="npndiagrams157", type=highlevelnets_npndiagrams_NPNSymbolArcSN, multiplicity=Multiplicity(1, 1)),
        Property(name="NPNDiagramNetSystem156", type=NPNDiagramNetSystem, multiplicity=Multiplicity(1, 1))
    }
)
model158: BinaryAssociation = BinaryAssociation(
    name="model158",
    ends={
        Property(name="Arc159", type=highlevelnets_npndiagrams_NPNSymbolArcSN, multiplicity=Multiplicity(1, 1)),
        Property(name="highlevelnets_npndiagrams_NPNSymbolArcSN", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_highlevelnets_marking_HighLevelPetriNetMarked_INetElement = Generalization(general=INetElement, specific=highlevelnets_marking_HighLevelPetriNetMarked)
gen_highlevelnets_marking_Marking_INetElement = Generalization(general=INetElement, specific=highlevelnets_marking_Marking)
gen_highlevelnets_marking_PlaceMarking_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_marking_PlaceMarking)
gen_highlevelnets_tokentypes_TokenType_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_TokenType)
gen_highlevelnets_tokentypes_TokenTypeAtomic_TokenType = Generalization(general=TokenType, specific=highlevelnets_tokentypes_TokenTypeAtomic)
gen_highlevelnets_tokentypes_TokenTypeElementNet_TokenType = Generalization(general=TokenType, specific=highlevelnets_tokentypes_TokenTypeElementNet)
gen_highlevelnets_tokentypes_TokenNet_Token = Generalization(general=Token, specific=highlevelnets_tokentypes_TokenNet)
gen_highlevelnets_tokentypes_TokenAttribute_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokentypes_TokenAttribute)
gen_highlevelnets_tokentypes_Token_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_Token)
gen_highlevelnets_tokentypes_TokenAtomic_Token = Generalization(general=Token, specific=highlevelnets_tokentypes_TokenAtomic)
gen_highlevelnets_tokenexpressions_TokenWeight_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenWeight)
gen_highlevelnets_tokenexpressions_TokenMultisetExpression_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenMultisetExpression)
gen_highlevelnets_tokentypes_ElementNetMarked_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_ElementNetMarked)
gen_highlevelnets_tokentypes_Atom_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokentypes_Atom)
gen_highlevelnets_tokenexpressions_Variable_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_Variable)
gen_highlevelnets_tokenexpressions_TokenVariadicExpression_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokenexpressions_TokenVariadicExpression)
gen_highlevelnets_tokenexpressions_TokenMultiSet_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenMultiSet)
gen_highlevelnets_tokenexpressions_TokenBinding_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenBinding)
gen_highlevelnets_tokenexpressions_Monom_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_Monom)
gen_highlevelnets_tokenexpressions_TokenExpressionBinding_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_TokenExpressionBinding)
gen_highlevelnets_tokenexpressions_NetConstant_INetElement = Generalization(general=INetElement, specific=highlevelnets_tokenexpressions_NetConstant)
gen_highlevelnets_hlpn_HighLevelPetriNet_common_INetElement = Generalization(general=common_INetElement, specific=highlevelnets_hlpn_HighLevelPetriNet)
gen_highlevelnets_hlpn_HighLevelPetriNet_hlpn_ContextVariable = Generalization(general=hlpn_ContextVariable, specific=highlevelnets_hlpn_HighLevelPetriNet)
gen_highlevelnets_tokenexpressions_MonomConstant_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_tokenexpressions_MonomConstant)
gen_highlevelnets_hlpn_Transition_hlpn_ContextVariable = Generalization(general=hlpn_ContextVariable, specific=highlevelnets_hlpn_Transition)
gen_highlevelnets_hlpn_Transition_hlpn_Node = Generalization(general=hlpn_Node, specific=highlevelnets_hlpn_Transition)
gen_highlevelnets_hlpn_Place_Node = Generalization(general=Node, specific=highlevelnets_hlpn_Place)
gen_highlevelnets_hlpn_ArcPT_Arc = Generalization(general=Arc, specific=highlevelnets_hlpn_ArcPT)
gen_highlevelnets_hlpn_ArcTP_Arc = Generalization(general=Arc, specific=highlevelnets_hlpn_ArcTP)
gen_highlevelnets_hlpn_Arc_INetElement = Generalization(general=INetElement, specific=highlevelnets_hlpn_Arc)
gen_highlevelnets_npnets_NPnet_INetElement = Generalization(general=INetElement, specific=highlevelnets_npnets_NPnet)
gen_highlevelnets_hlpn_ContextVariable_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_hlpn_ContextVariable)
gen_highlevelnets_hlpn_Node_INetElement = Generalization(general=INetElement, specific=highlevelnets_hlpn_Node)
gen_highlevelnets_npnets_NPnetMarked_INetElement = Generalization(general=INetElement, specific=highlevelnets_npnets_NPnetMarked)
gen_highlevelnets_npnets_TransitionSynchronized_Transition = Generalization(general=Transition, specific=highlevelnets_npnets_TransitionSynchronized)
gen_highlevelnets_common_INetElement_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_common_INetElement)
gen_highlevelnets_npnets_Synchronization_INetElement = Generalization(general=INetElement, specific=highlevelnets_npnets_Synchronization)
gen_highlevelnets_npndiagrams_NPNDiagramNetSystem_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNDiagramNetSystem)
gen_highlevelnets_npndiagrams_NPNDiagramNPNMarked_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNDiagramNPNMarked)
gen_highlevelnets_npndiagrams_NPNSymbolTransitionSN_NPNSymbolNodeSN = Generalization(general=NPNSymbolNodeSN, specific=highlevelnets_npndiagrams_NPNSymbolTransitionSN)
gen_highlevelnets_npndiagrams_NPNSymbolPlaceSN_NPNSymbolNodeSN = Generalization(general=NPNSymbolNodeSN, specific=highlevelnets_npndiagrams_NPNSymbolPlaceSN)
gen_highlevelnets_npndiagrams_NPNSymbolNodeSN_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNSymbolNodeSN)
gen_highlevelnets_npndiagrams_NPNSymbolArcPTSN_NPNSymbolArcSN = Generalization(general=NPNSymbolArcSN, specific=highlevelnets_npndiagrams_NPNSymbolArcPTSN)
gen_highlevelnets_npndiagrams_NPNSymbolArcTPSN_NPNSymbolArcSN = Generalization(general=NPNSymbolArcSN, specific=highlevelnets_npndiagrams_NPNSymbolArcTPSN)
gen_highlevelnets_npndiagrams_NPNSymbolTokenSN_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNSymbolTokenSN)
gen_highlevelnets_npndiagrams_NPNSymbolArcSN_IEntityIdentifiable = Generalization(general=IEntityIdentifiable, specific=highlevelnets_npndiagrams_NPNSymbolArcSN)

# Domain Model
domain_model = DomainModel(
    name="highlevelnets",
    types={highlevelnets_marking_Marking, highlevelnets_marking_HighLevelPetriNetMarked, HighLevelPetriNet, Marking, INetElement, PlaceMarking, highlevelnets_marking_PlaceMarking, IEntityIdentifiable, Place, TokenMultiSet, ElementNetMarked, TokenNet, highlevelnets_tokentypes_TokenType, highlevelnets_tokentypes_TokenTypeAtomic, TokenType, Atom, TokenAtomic, highlevelnets_tokentypes_TokenTypeElementNet, highlevelnets_tokentypes_TokenNet, TokenTypeElementNet, highlevelnets_tokentypes_TokenAttribute, highlevelnets_tokentypes_Token, TokenAttribute, highlevelnets_tokentypes_TokenAtomic, Token, TokenTypeAtomic, highlevelnets_tokenexpressions_TokenWeight, highlevelnets_tokenexpressions_TokenMultisetExpression, highlevelnets_tokentypes_ElementNetMarked, highlevelnets_tokentypes_Atom, highlevelnets_tokenexpressions_Variable, ContextVariable, highlevelnets_tokenexpressions_TokenVariadicExpression, highlevelnets_tokenexpressions_TokenMultiSet, TokenWeight, TokenVariadicExpression, TokenBinding, highlevelnets_tokenexpressions_TokenBinding, Monom, MonomConstant, highlevelnets_tokenexpressions_Monom, Variable, highlevelnets_tokenexpressions_TokenExpressionBinding, highlevelnets_hlpn_HighLevelPetriNet, common_INetElement, hlpn_ContextVariable, highlevelnets_tokenexpressions_MonomConstant, highlevelnets_tokenexpressions_NetConstant, highlevelnets_hlpn_Transition, hlpn_Node, Node, Arc, highlevelnets_hlpn_Place, ArcPT, ArcTP, highlevelnets_hlpn_ArcPT, Transition, highlevelnets_hlpn_ArcTP, highlevelnets_hlpn_Arc, highlevelnets_npnets_NPnet, highlevelnets_hlpn_ContextVariable, highlevelnets_hlpn_Node, highlevelnets_npnets_NPnetMarked, NPnet, NetConstant, Synchronization, highlevelnets_npnets_TransitionSynchronized, highlevelnets_common_INetElement, NPNDiagramNetSystem, highlevelnets_npnets_Synchronization, TransitionSynchronized, NPnetMarked, highlevelnets_npndiagrams_NPNDiagramNetSystem, NPNSymbolNodeSN, highlevelnets_common_IEntityIdentifiable, highlevelnets_npndiagrams_NPNDiagramNPNMarked, NPNSymbolTokenSN, highlevelnets_npndiagrams_NPNSymbolTransitionSN, NPNSymbolArcSN, highlevelnets_npndiagrams_NPNSymbolPlaceSN, NPNSymbolArcPTSN, NPNSymbolArcTPSN, highlevelnets_npndiagrams_NPNSymbolNodeSN, highlevelnets_npndiagrams_NPNSymbolArcPTSN, NPNSymbolTransitionSN, NPNSymbolPlaceSN, highlevelnets_npndiagrams_NPNSymbolArcTPSN, highlevelnets_npndiagrams_NPNSymbolTokenSN, highlevelnets_npndiagrams_NPNSymbolArcSN, ESynchronizationKind},
    associations={net4, marking5, map0, place1, marking2, elementNetMarkeds9, net11, tokenNets13, instance7, atom8, type20, value22, attribute15, type16, value18, token29, type24, marking27, context38, type30, value31, weight34, type35, expression43, bindingTokens44, monoms39, monomConstants40, variable42, binding56, variable46, value48, constant51, value53, inArcs68, nodes58, arcs60, outArcs62, inArcs64, type66, source81, target84, inscription87, outArcs71, source74, target77, inscription79, net94, variables89, net91, net109, marking110, netSystem97, typeElementNet99, typeAtomic102, netConstants105, synchronizations107, synchronization116, diagramNetSystem113, involved115, model121, model123, diagramNetSystem119, tokens132, outArcs134, nodes125, arcs126, outArcs128, inArcs130, source147, diagram150, inArcs137, target140, source142, target144, place160, model153, diagram155, model158},
    generalizations={gen_highlevelnets_marking_HighLevelPetriNetMarked_INetElement, gen_highlevelnets_marking_Marking_INetElement, gen_highlevelnets_marking_PlaceMarking_IEntityIdentifiable, gen_highlevelnets_tokentypes_TokenType_INetElement, gen_highlevelnets_tokentypes_TokenTypeAtomic_TokenType, gen_highlevelnets_tokentypes_TokenTypeElementNet_TokenType, gen_highlevelnets_tokentypes_TokenNet_Token, gen_highlevelnets_tokentypes_TokenAttribute_IEntityIdentifiable, gen_highlevelnets_tokentypes_Token_INetElement, gen_highlevelnets_tokentypes_TokenAtomic_Token, gen_highlevelnets_tokenexpressions_TokenWeight_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenMultisetExpression_IEntityIdentifiable, gen_highlevelnets_tokentypes_ElementNetMarked_INetElement, gen_highlevelnets_tokentypes_Atom_INetElement, gen_highlevelnets_tokenexpressions_Variable_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenVariadicExpression_INetElement, gen_highlevelnets_tokenexpressions_TokenMultiSet_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenBinding_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_Monom_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_TokenExpressionBinding_IEntityIdentifiable, gen_highlevelnets_tokenexpressions_NetConstant_INetElement, gen_highlevelnets_hlpn_HighLevelPetriNet_common_INetElement, gen_highlevelnets_hlpn_HighLevelPetriNet_hlpn_ContextVariable, gen_highlevelnets_tokenexpressions_MonomConstant_IEntityIdentifiable, gen_highlevelnets_hlpn_Transition_hlpn_ContextVariable, gen_highlevelnets_hlpn_Transition_hlpn_Node, gen_highlevelnets_hlpn_Place_Node, gen_highlevelnets_hlpn_ArcPT_Arc, gen_highlevelnets_hlpn_ArcTP_Arc, gen_highlevelnets_hlpn_Arc_INetElement, gen_highlevelnets_npnets_NPnet_INetElement, gen_highlevelnets_hlpn_ContextVariable_IEntityIdentifiable, gen_highlevelnets_hlpn_Node_INetElement, gen_highlevelnets_npnets_NPnetMarked_INetElement, gen_highlevelnets_npnets_TransitionSynchronized_Transition, gen_highlevelnets_common_INetElement_IEntityIdentifiable, gen_highlevelnets_npnets_Synchronization_INetElement, gen_highlevelnets_npndiagrams_NPNDiagramNetSystem_IEntityIdentifiable, gen_highlevelnets_npndiagrams_NPNDiagramNPNMarked_IEntityIdentifiable, gen_highlevelnets_npndiagrams_NPNSymbolTransitionSN_NPNSymbolNodeSN, gen_highlevelnets_npndiagrams_NPNSymbolPlaceSN_NPNSymbolNodeSN, gen_highlevelnets_npndiagrams_NPNSymbolNodeSN_IEntityIdentifiable, gen_highlevelnets_npndiagrams_NPNSymbolArcPTSN_NPNSymbolArcSN, gen_highlevelnets_npndiagrams_NPNSymbolArcTPSN_NPNSymbolArcSN, gen_highlevelnets_npndiagrams_NPNSymbolTokenSN_IEntityIdentifiable, gen_highlevelnets_npndiagrams_NPNSymbolArcSN_IEntityIdentifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)