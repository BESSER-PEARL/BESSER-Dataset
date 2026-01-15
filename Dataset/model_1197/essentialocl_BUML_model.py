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
CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="Collection"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="OrderedSet")
    }
)

# Classes
essentialocl_types_BagType = Class(name="essentialocl::types::BagType")
CollectionType = Class(name="CollectionType")
essentialocl_types_TupleType = Class(name="essentialocl::types::TupleType")
Type = Class(name="Type")
essentialocl_types_TypeType = Class(name="essentialocl::types::TypeType")
essentialocl_types_OclLibrary = Class(name="essentialocl::types::OclLibrary")
OclLibrary = Class(name="OclLibrary")
essentialocl_types_CollectionType = Class(name="essentialocl::types::CollectionType")
types_essentialocl_Type = Class(name="types::essentialocl::Type")
essentialocl_types_InvalidType = Class(name="essentialocl::types::InvalidType")
essentialocl_types_OrderedSetType = Class(name="essentialocl::types::OrderedSetType")
essentialocl_types_SequenceType = Class(name="essentialocl::types::SequenceType")
TypeType = Class(name="TypeType")
essentialocl_types_SetType = Class(name="essentialocl::types::SetType")
essentialocl_types_VoidType = Class(name="essentialocl::types::VoidType")
SequenceType = Class(name="SequenceType")
types_essentialocl_PrimitiveType = Class(name="types::essentialocl::PrimitiveType")
AnyType = Class(name="AnyType")
VoidType = Class(name="VoidType")
InvalidType = Class(name="InvalidType")
expressions_essentialocl_Parameter = Class(name="expressions::essentialocl::Parameter")
essentialocl_expressions_UnlimitedNaturalExp = Class(name="essentialocl::expressions::UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
essentialocl_expressions_TypeLiteralExp = Class(name="essentialocl::expressions::TypeLiteralExp")
LiteralExp = Class(name="LiteralExp")
expressions_essentialocl_Type = Class(name="expressions::essentialocl::Type")
essentialocl_expressions_TupleLiteralPart = Class(name="essentialocl::expressions::TupleLiteralPart")
BagType = Class(name="BagType")
SetType = Class(name="SetType")
OrderedSetType = Class(name="OrderedSetType")
TupleType = Class(name="TupleType")
essentialocl_types_AnyType = Class(name="essentialocl::types::AnyType")
essentialocl_expressions_VariableExp = Class(name="essentialocl::expressions::VariableExp")
OclExpression = Class(name="OclExpression")
Variable = Class(name="Variable")
essentialocl_expressions_Variable = Class(name="essentialocl::expressions::Variable")
TypedElement = Class(name="TypedElement")
NamedElement = Class(name="NamedElement")
expressions_essentialocl_Operation = Class(name="expressions::essentialocl::Operation")
essentialocl_expressions_OclExpression = Class(name="essentialocl::expressions::OclExpression", is_abstract=True)
essentialocl_expressions_NumericLiteralExp = Class(name="essentialocl::expressions::NumericLiteralExp", is_abstract=True)
essentialocl_expressions_UndefinedLiteralExp = Class(name="essentialocl::expressions::UndefinedLiteralExp")
expressions_essentialocl_Property = Class(name="expressions::essentialocl::Property")
essentialocl_expressions_LoopExp = Class(name="essentialocl::expressions::LoopExp", is_abstract=True)
CallExp = Class(name="CallExp")
essentialocl_expressions_TupleLiteralExp = Class(name="essentialocl::expressions::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
essentialocl_expressions_StringLiteralExp = Class(name="essentialocl::expressions::StringLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
essentialocl_expressions_RealLiteralExp = Class(name="essentialocl::expressions::RealLiteralExp")
essentialocl_expressions_PropertyCallExp = Class(name="essentialocl::expressions::PropertyCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
essentialocl_expressions_PrimitiveLiteralExp = Class(name="essentialocl::expressions::PrimitiveLiteralExp", is_abstract=True)
essentialocl_expressions_OperationCallExp = Class(name="essentialocl::expressions::OperationCallExp")
essentialocl_expressions_FeatureCallExp = Class(name="essentialocl::expressions::FeatureCallExp", is_abstract=True)
essentialocl_expressions_LiteralExp = Class(name="essentialocl::expressions::LiteralExp", is_abstract=True)
essentialocl_expressions_LetExp = Class(name="essentialocl::expressions::LetExp")
essentialocl_expressions_IteratorExp = Class(name="essentialocl::expressions::IteratorExp")
LoopExp = Class(name="LoopExp")
essentialocl_expressions_IterateExp = Class(name="essentialocl::expressions::IterateExp")
essentialocl_expressions_InvalidLiteralExp = Class(name="essentialocl::expressions::InvalidLiteralExp")
essentialocl_expressions_IntegerLiteralExp = Class(name="essentialocl::expressions::IntegerLiteralExp")
essentialocl_expressions_IfExp = Class(name="essentialocl::expressions::IfExp")
essentialocl_expressions_EnumLiteralExp = Class(name="essentialocl::expressions::EnumLiteralExp")
expressions_essentialocl_EnumerationLiteral = Class(name="expressions::essentialocl::EnumerationLiteral")
essentialocl_expressions_ExpressionInOcl = Class(name="essentialocl::expressions::ExpressionInOcl")
Expression = Class(name="Expression")
essentialocl_expressions_BooleanLiteralExp = Class(name="essentialocl::expressions::BooleanLiteralExp")
essentialocl_expressions_CallExp = Class(name="essentialocl::expressions::CallExp", is_abstract=True)
essentialocl_expressions_CollectionItem = Class(name="essentialocl::expressions::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
essentialocl_expressions_CollectionLiteralExp = Class(name="essentialocl::expressions::CollectionLiteralExp")
essentialocl_expressions_CollectionLiteralPart = Class(name="essentialocl::expressions::CollectionLiteralPart", is_abstract=True)
essentialocl_expressions_CollectionRange = Class(name="essentialocl::expressions::CollectionRange")

# essentialocl_types_BagType class attributes and methods

# CollectionType class attributes and methods

# essentialocl_types_TupleType class attributes and methods

# Type class attributes and methods

# essentialocl_types_TypeType class attributes and methods

# essentialocl_types_OclLibrary class attributes and methods
essentialocl_types_OclLibrary_m_makeTupleType: Method = Method(name="makeTupleType", parameters={Parameter(name='atts')}, type=StringType)
essentialocl_types_OclLibrary_m_getCollectionType: Method = Method(name="getCollectionType", parameters={Parameter(name='elementType')}, type=StringType)
essentialocl_types_OclLibrary_m_getSequenceType: Method = Method(name="getSequenceType", parameters={Parameter(name='elementType')}, type=StringType)
essentialocl_types_OclLibrary_m_getBagType: Method = Method(name="getBagType", parameters={Parameter(name='elementType')}, type=StringType)
essentialocl_types_OclLibrary_m_getSetType: Method = Method(name="getSetType", parameters={Parameter(name='elementType')}, type=StringType)
essentialocl_types_OclLibrary_m_getOrderedSetType: Method = Method(name="getOrderedSetType", parameters={Parameter(name='elementType')}, type=StringType)
essentialocl_types_OclLibrary_m_getTypeType: Method = Method(name="getTypeType", parameters={Parameter(name='representedType')}, type=StringType)
essentialocl_types_OclLibrary.methods={essentialocl_types_OclLibrary_m_getSetType, essentialocl_types_OclLibrary_m_getTypeType, essentialocl_types_OclLibrary_m_getBagType, essentialocl_types_OclLibrary_m_getOrderedSetType, essentialocl_types_OclLibrary_m_getCollectionType, essentialocl_types_OclLibrary_m_makeTupleType, essentialocl_types_OclLibrary_m_getSequenceType}

# OclLibrary class attributes and methods

# essentialocl_types_CollectionType class attributes and methods
essentialocl_types_CollectionType_kind: Property = Property(name="kind", type=StringType)
essentialocl_types_CollectionType.attributes={essentialocl_types_CollectionType_kind}

# types_essentialocl_Type class attributes and methods

# essentialocl_types_InvalidType class attributes and methods

# essentialocl_types_OrderedSetType class attributes and methods

# essentialocl_types_SequenceType class attributes and methods

# TypeType class attributes and methods

# essentialocl_types_SetType class attributes and methods

# essentialocl_types_VoidType class attributes and methods

# SequenceType class attributes and methods

# types_essentialocl_PrimitiveType class attributes and methods

# AnyType class attributes and methods

# VoidType class attributes and methods

# InvalidType class attributes and methods

# expressions_essentialocl_Parameter class attributes and methods

# essentialocl_expressions_UnlimitedNaturalExp class attributes and methods
essentialocl_expressions_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
essentialocl_expressions_UnlimitedNaturalExp.attributes={essentialocl_expressions_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# essentialocl_expressions_TypeLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# expressions_essentialocl_Type class attributes and methods

# essentialocl_expressions_TupleLiteralPart class attributes and methods

# BagType class attributes and methods

# SetType class attributes and methods

# OrderedSetType class attributes and methods

# TupleType class attributes and methods

# essentialocl_types_AnyType class attributes and methods

# essentialocl_expressions_VariableExp class attributes and methods

# OclExpression class attributes and methods

# Variable class attributes and methods

# essentialocl_expressions_Variable class attributes and methods
essentialocl_expressions_Variable_m_asParameter: Method = Method(name="asParameter", parameters={}, type=StringType)
essentialocl_expressions_Variable_m_asProperty: Method = Method(name="asProperty", parameters={}, type=StringType)
essentialocl_expressions_Variable.methods={essentialocl_expressions_Variable_m_asParameter, essentialocl_expressions_Variable_m_asProperty}

# TypedElement class attributes and methods

# NamedElement class attributes and methods

# expressions_essentialocl_Operation class attributes and methods

# essentialocl_expressions_OclExpression class attributes and methods
essentialocl_expressions_OclExpression_m_withAtPre: Method = Method(name="withAtPre", parameters={}, type=StringType)
essentialocl_expressions_OclExpression_m_withAsSet: Method = Method(name="withAsSet", parameters={}, type=StringType)
essentialocl_expressions_OclExpression.methods={essentialocl_expressions_OclExpression_m_withAsSet, essentialocl_expressions_OclExpression_m_withAtPre}

# essentialocl_expressions_NumericLiteralExp class attributes and methods

# essentialocl_expressions_UndefinedLiteralExp class attributes and methods

# expressions_essentialocl_Property class attributes and methods

# essentialocl_expressions_LoopExp class attributes and methods

# CallExp class attributes and methods

# essentialocl_expressions_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# essentialocl_expressions_StringLiteralExp class attributes and methods
essentialocl_expressions_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
essentialocl_expressions_StringLiteralExp.attributes={essentialocl_expressions_StringLiteralExp_stringSymbol}

# PrimitiveLiteralExp class attributes and methods

# essentialocl_expressions_RealLiteralExp class attributes and methods
essentialocl_expressions_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
essentialocl_expressions_RealLiteralExp.attributes={essentialocl_expressions_RealLiteralExp_realSymbol}

# essentialocl_expressions_PropertyCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# essentialocl_expressions_PrimitiveLiteralExp class attributes and methods

# essentialocl_expressions_OperationCallExp class attributes and methods

# essentialocl_expressions_FeatureCallExp class attributes and methods

# essentialocl_expressions_LiteralExp class attributes and methods

# essentialocl_expressions_LetExp class attributes and methods

# essentialocl_expressions_IteratorExp class attributes and methods

# LoopExp class attributes and methods

# essentialocl_expressions_IterateExp class attributes and methods

# essentialocl_expressions_InvalidLiteralExp class attributes and methods

# essentialocl_expressions_IntegerLiteralExp class attributes and methods
essentialocl_expressions_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
essentialocl_expressions_IntegerLiteralExp.attributes={essentialocl_expressions_IntegerLiteralExp_integerSymbol}

# essentialocl_expressions_IfExp class attributes and methods

# essentialocl_expressions_EnumLiteralExp class attributes and methods

# expressions_essentialocl_EnumerationLiteral class attributes and methods

# essentialocl_expressions_ExpressionInOcl class attributes and methods

# Expression class attributes and methods

# essentialocl_expressions_BooleanLiteralExp class attributes and methods
essentialocl_expressions_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
essentialocl_expressions_BooleanLiteralExp.attributes={essentialocl_expressions_BooleanLiteralExp_booleanSymbol}

# essentialocl_expressions_CallExp class attributes and methods

# essentialocl_expressions_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# essentialocl_expressions_CollectionLiteralExp class attributes and methods
essentialocl_expressions_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
essentialocl_expressions_CollectionLiteralExp.attributes={essentialocl_expressions_CollectionLiteralExp_kind}

# essentialocl_expressions_CollectionLiteralPart class attributes and methods

# essentialocl_expressions_CollectionRange class attributes and methods

# Relationships
oclLibrary7: BinaryAssociation = BinaryAssociation(
    name="oclLibrary7",
    ends={
        Property(name="types9", type=essentialocl_types_VoidType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclLibrary8", type=OclLibrary, multiplicity=Multiplicity(1, 1))
    }
)
representedType10: BinaryAssociation = BinaryAssociation(
    name="representedType10",
    ends={
        Property(name="types_essentialocl_Type11", type=essentialocl_types_TypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_TypeType", type=types_essentialocl_Type, multiplicity=Multiplicity(0, 1))
    }
)
oclLibrary0: BinaryAssociation = BinaryAssociation(
    name="oclLibrary0",
    ends={
        Property(name="OclLibrary", type=essentialocl_types_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_TupleType", type=OclLibrary, multiplicity=Multiplicity(1, 1))
    }
)
elementType1: BinaryAssociation = BinaryAssociation(
    name="elementType1",
    ends={
        Property(name="types_essentialocl_Type", type=essentialocl_types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_CollectionType", type=types_essentialocl_Type, multiplicity=Multiplicity(0, 1))
    }
)
oclLibrary2: BinaryAssociation = BinaryAssociation(
    name="oclLibrary2",
    ends={
        Property(name="OclLibrary4", type=essentialocl_types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_CollectionType3", type=OclLibrary, multiplicity=Multiplicity(1, 1))
    }
)
oclLibrary5: BinaryAssociation = BinaryAssociation(
    name="oclLibrary5",
    ends={
        Property(name="types", type=essentialocl_types_InvalidType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclLibrary6", type=OclLibrary, multiplicity=Multiplicity(1, 1))
    }
)
oclInvalid26: BinaryAssociation = BinaryAssociation(
    name="oclInvalid26",
    ends={
        Property(name="types27", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="InvalidType", type=InvalidType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclType28: BinaryAssociation = BinaryAssociation(
    name="oclType28",
    ends={
        Property(name="TypeType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary29", type=TypeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclCollection30: BinaryAssociation = BinaryAssociation(
    name="oclCollection30",
    ends={
        Property(name="CollectionType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary31", type=CollectionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclSequence32: BinaryAssociation = BinaryAssociation(
    name="oclSequence32",
    ends={
        Property(name="SequenceType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary33", type=SequenceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclBoolean12: BinaryAssociation = BinaryAssociation(
    name="oclBoolean12",
    ends={
        Property(name="types_essentialocl_PrimitiveType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary", type=types_essentialocl_PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclString13: BinaryAssociation = BinaryAssociation(
    name="oclString13",
    ends={
        Property(name="types_essentialocl_PrimitiveType15", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary14", type=types_essentialocl_PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclInteger16: BinaryAssociation = BinaryAssociation(
    name="oclInteger16",
    ends={
        Property(name="types_essentialocl_PrimitiveType18", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary17", type=types_essentialocl_PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclReal19: BinaryAssociation = BinaryAssociation(
    name="oclReal19",
    ends={
        Property(name="types_essentialocl_PrimitiveType21", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary20", type=types_essentialocl_PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclAny22: BinaryAssociation = BinaryAssociation(
    name="oclAny22",
    ends={
        Property(name="AnyType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary23", type=AnyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclVoid24: BinaryAssociation = BinaryAssociation(
    name="oclVoid24",
    ends={
        Property(name="types25", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="VoidType", type=VoidType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representedParameter43: BinaryAssociation = BinaryAssociation(
    name="representedParameter43",
    ends={
        Property(name="expressions_essentialocl_Parameter", type=essentialocl_expressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_Variable", type=expressions_essentialocl_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
initExpression44: BinaryAssociation = BinaryAssociation(
    name="initExpression44",
    ends={
        Property(name="OclExpression", type=essentialocl_expressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_Variable45", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredType46: BinaryAssociation = BinaryAssociation(
    name="referredType46",
    ends={
        Property(name="expressions_essentialocl_Type", type=essentialocl_expressions_TypeLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_TypeLiteralExp", type=expressions_essentialocl_Type, multiplicity=Multiplicity(0, 1))
    }
)
oclBag34: BinaryAssociation = BinaryAssociation(
    name="oclBag34",
    ends={
        Property(name="BagType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary35", type=BagType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclSet36: BinaryAssociation = BinaryAssociation(
    name="oclSet36",
    ends={
        Property(name="SetType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary37", type=SetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclOrderedSet38: BinaryAssociation = BinaryAssociation(
    name="oclOrderedSet38",
    ends={
        Property(name="OrderedSetType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary39", type=OrderedSetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclTuple40: BinaryAssociation = BinaryAssociation(
    name="oclTuple40",
    ends={
        Property(name="TupleType", type=essentialocl_types_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_types_OclLibrary41", type=TupleType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
referredVariable42: BinaryAssociation = BinaryAssociation(
    name="referredVariable42",
    ends={
        Property(name="Variable", type=essentialocl_expressions_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredOperation59: BinaryAssociation = BinaryAssociation(
    name="referredOperation59",
    ends={
        Property(name="expressions_essentialocl_Operation", type=essentialocl_expressions_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_OperationCallExp60", type=expressions_essentialocl_Operation, multiplicity=Multiplicity(0, 1))
    }
)
oclLibrary61: BinaryAssociation = BinaryAssociation(
    name="oclLibrary61",
    ends={
        Property(name="OclLibrary62", type=essentialocl_expressions_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_OclExpression", type=OclLibrary, multiplicity=Multiplicity(0, 1))
    }
)
property47: BinaryAssociation = BinaryAssociation(
    name="property47",
    ends={
        Property(name="expressions_essentialocl_Property", type=essentialocl_expressions_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_TupleLiteralPart", type=expressions_essentialocl_Property, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value48: BinaryAssociation = BinaryAssociation(
    name="value48",
    ends={
        Property(name="OclExpression50", type=essentialocl_expressions_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_TupleLiteralPart49", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part51: BinaryAssociation = BinaryAssociation(
    name="part51",
    ends={
        Property(name="TupleLiteralPart", type=essentialocl_expressions_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredProperty52: BinaryAssociation = BinaryAssociation(
    name="referredProperty52",
    ends={
        Property(name="expressions_essentialocl_Property53", type=essentialocl_expressions_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_PropertyCallExp", type=expressions_essentialocl_Property, multiplicity=Multiplicity(0, 1))
    }
)
qualifier54: BinaryAssociation = BinaryAssociation(
    name="qualifier54",
    ends={
        Property(name="OclExpression56", type=essentialocl_expressions_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_PropertyCallExp55", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument57: BinaryAssociation = BinaryAssociation(
    name="argument57",
    ends={
        Property(name="OclExpression58", type=essentialocl_expressions_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenExpression77: BinaryAssociation = BinaryAssociation(
    name="thenExpression77",
    ends={
        Property(name="OclExpression79", type=essentialocl_expressions_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_IfExp78", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression80: BinaryAssociation = BinaryAssociation(
    name="elseExpression80",
    ends={
        Property(name="OclExpression82", type=essentialocl_expressions_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_IfExp81", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body63: BinaryAssociation = BinaryAssociation(
    name="body63",
    ends={
        Property(name="OclExpression64", type=essentialocl_expressions_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator65: BinaryAssociation = BinaryAssociation(
    name="iterator65",
    ends={
        Property(name="Variable67", type=essentialocl_expressions_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_LoopExp66", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in68: BinaryAssociation = BinaryAssociation(
    name="in68",
    ends={
        Property(name="OclExpression69", type=essentialocl_expressions_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable70: BinaryAssociation = BinaryAssociation(
    name="variable70",
    ends={
        Property(name="Variable72", type=essentialocl_expressions_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_LetExp71", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result73: BinaryAssociation = BinaryAssociation(
    name="result73",
    ends={
        Property(name="Variable74", type=essentialocl_expressions_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first93: BinaryAssociation = BinaryAssociation(
    name="first93",
    ends={
        Property(name="OclExpression94", type=essentialocl_expressions_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition75: BinaryAssociation = BinaryAssociation(
    name="condition75",
    ends={
        Property(name="OclExpression76", type=essentialocl_expressions_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last95: BinaryAssociation = BinaryAssociation(
    name="last95",
    ends={
        Property(name="OclExpression97", type=essentialocl_expressions_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_CollectionRange96", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredEnumLiteral98: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral98",
    ends={
        Property(name="expressions_essentialocl_EnumerationLiteral", type=essentialocl_expressions_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_EnumLiteralExp", type=expressions_essentialocl_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
sourceType83: BinaryAssociation = BinaryAssociation(
    name="sourceType83",
    ends={
        Property(name="expressions_essentialocl_Type84", type=essentialocl_expressions_FeatureCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_FeatureCallExp", type=expressions_essentialocl_Type, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression99: BinaryAssociation = BinaryAssociation(
    name="bodyExpression99",
    ends={
        Property(name="OclExpression100", type=essentialocl_expressions_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source85: BinaryAssociation = BinaryAssociation(
    name="source85",
    ends={
        Property(name="OclExpression86", type=essentialocl_expressions_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item87: BinaryAssociation = BinaryAssociation(
    name="item87",
    ends={
        Property(name="OclExpression88", type=essentialocl_expressions_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part89: BinaryAssociation = BinaryAssociation(
    name="part89",
    ends={
        Property(name="CollectionLiteralPart", type=essentialocl_expressions_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType90: BinaryAssociation = BinaryAssociation(
    name="elementType90",
    ends={
        Property(name="expressions_essentialocl_Type92", type=essentialocl_expressions_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_CollectionLiteralExp91", type=expressions_essentialocl_Type, multiplicity=Multiplicity(0, 1))
    }
)
context101: BinaryAssociation = BinaryAssociation(
    name="context101",
    ends={
        Property(name="Variable103", type=essentialocl_expressions_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_ExpressionInOcl102", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result104: BinaryAssociation = BinaryAssociation(
    name="result104",
    ends={
        Property(name="Variable106", type=essentialocl_expressions_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_ExpressionInOcl105", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter107: BinaryAssociation = BinaryAssociation(
    name="parameter107",
    ends={
        Property(name="Variable109", type=essentialocl_expressions_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_expressions_ExpressionInOcl108", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_essentialocl_types_BagType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_types_BagType)
gen_essentialocl_types_TupleType_Type = Generalization(general=Type, specific=essentialocl_types_TupleType)
gen_essentialocl_types_VoidType_Type = Generalization(general=Type, specific=essentialocl_types_VoidType)
gen_essentialocl_types_TypeType_Type = Generalization(general=Type, specific=essentialocl_types_TypeType)
gen_essentialocl_types_CollectionType_Type = Generalization(general=Type, specific=essentialocl_types_CollectionType)
gen_essentialocl_types_InvalidType_Type = Generalization(general=Type, specific=essentialocl_types_InvalidType)
gen_essentialocl_types_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_types_OrderedSetType)
gen_essentialocl_types_SequenceType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_types_SequenceType)
gen_essentialocl_types_SetType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_types_SetType)
gen_essentialocl_expressions_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_expressions_UnlimitedNaturalExp)
gen_essentialocl_expressions_TypeLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_TypeLiteralExp)
gen_essentialocl_expressions_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=essentialocl_expressions_TupleLiteralPart)
gen_essentialocl_types_AnyType_Type = Generalization(general=Type, specific=essentialocl_types_AnyType)
gen_essentialocl_expressions_VariableExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_expressions_VariableExp)
gen_essentialocl_expressions_Variable_TypedElement = Generalization(general=TypedElement, specific=essentialocl_expressions_Variable)
gen_essentialocl_expressions_Variable_NamedElement = Generalization(general=NamedElement, specific=essentialocl_expressions_Variable)
gen_essentialocl_expressions_OclExpression_TypedElement = Generalization(general=TypedElement, specific=essentialocl_expressions_OclExpression)
gen_essentialocl_expressions_OclExpression_NamedElement = Generalization(general=NamedElement, specific=essentialocl_expressions_OclExpression)
gen_essentialocl_expressions_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_expressions_NumericLiteralExp)
gen_essentialocl_expressions_UndefinedLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_UndefinedLiteralExp)
gen_essentialocl_expressions_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_TupleLiteralExp)
gen_essentialocl_expressions_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_expressions_StringLiteralExp)
gen_essentialocl_expressions_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_expressions_RealLiteralExp)
gen_essentialocl_expressions_PropertyCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=essentialocl_expressions_PropertyCallExp)
gen_essentialocl_expressions_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_PrimitiveLiteralExp)
gen_essentialocl_expressions_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=essentialocl_expressions_OperationCallExp)
gen_essentialocl_expressions_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=essentialocl_expressions_FeatureCallExp)
gen_essentialocl_expressions_LoopExp_CallExp = Generalization(general=CallExp, specific=essentialocl_expressions_LoopExp)
gen_essentialocl_expressions_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_expressions_LiteralExp)
gen_essentialocl_expressions_LetExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_expressions_LetExp)
gen_essentialocl_expressions_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=essentialocl_expressions_IteratorExp)
gen_essentialocl_expressions_IterateExp_LoopExp = Generalization(general=LoopExp, specific=essentialocl_expressions_IterateExp)
gen_essentialocl_expressions_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_InvalidLiteralExp)
gen_essentialocl_expressions_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_expressions_IntegerLiteralExp)
gen_essentialocl_expressions_IfExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_expressions_IfExp)
gen_essentialocl_expressions_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_EnumLiteralExp)
gen_essentialocl_expressions_ExpressionInOcl_Expression = Generalization(general=Expression, specific=essentialocl_expressions_ExpressionInOcl)
gen_essentialocl_expressions_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_expressions_BooleanLiteralExp)
gen_essentialocl_expressions_CallExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_expressions_CallExp)
gen_essentialocl_expressions_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=essentialocl_expressions_CollectionItem)
gen_essentialocl_expressions_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_expressions_CollectionLiteralExp)
gen_essentialocl_expressions_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=essentialocl_expressions_CollectionLiteralPart)
gen_essentialocl_expressions_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=essentialocl_expressions_CollectionRange)

# Domain Model
domain_model = DomainModel(
    name="essentialocl",
    types={essentialocl_types_BagType, CollectionType, essentialocl_types_TupleType, Type, essentialocl_types_TypeType, essentialocl_types_OclLibrary, OclLibrary, essentialocl_types_CollectionType, types_essentialocl_Type, essentialocl_types_InvalidType, essentialocl_types_OrderedSetType, essentialocl_types_SequenceType, TypeType, essentialocl_types_SetType, essentialocl_types_VoidType, SequenceType, types_essentialocl_PrimitiveType, AnyType, VoidType, InvalidType, expressions_essentialocl_Parameter, essentialocl_expressions_UnlimitedNaturalExp, NumericLiteralExp, essentialocl_expressions_TypeLiteralExp, LiteralExp, expressions_essentialocl_Type, essentialocl_expressions_TupleLiteralPart, BagType, SetType, OrderedSetType, TupleType, essentialocl_types_AnyType, essentialocl_expressions_VariableExp, OclExpression, Variable, essentialocl_expressions_Variable, TypedElement, NamedElement, expressions_essentialocl_Operation, essentialocl_expressions_OclExpression, essentialocl_expressions_NumericLiteralExp, essentialocl_expressions_UndefinedLiteralExp, expressions_essentialocl_Property, essentialocl_expressions_LoopExp, CallExp, essentialocl_expressions_TupleLiteralExp, TupleLiteralPart, essentialocl_expressions_StringLiteralExp, PrimitiveLiteralExp, essentialocl_expressions_RealLiteralExp, essentialocl_expressions_PropertyCallExp, FeatureCallExp, essentialocl_expressions_PrimitiveLiteralExp, essentialocl_expressions_OperationCallExp, essentialocl_expressions_FeatureCallExp, essentialocl_expressions_LiteralExp, essentialocl_expressions_LetExp, essentialocl_expressions_IteratorExp, LoopExp, essentialocl_expressions_IterateExp, essentialocl_expressions_InvalidLiteralExp, essentialocl_expressions_IntegerLiteralExp, essentialocl_expressions_IfExp, essentialocl_expressions_EnumLiteralExp, expressions_essentialocl_EnumerationLiteral, essentialocl_expressions_ExpressionInOcl, Expression, essentialocl_expressions_BooleanLiteralExp, essentialocl_expressions_CallExp, essentialocl_expressions_CollectionItem, CollectionLiteralPart, essentialocl_expressions_CollectionLiteralExp, essentialocl_expressions_CollectionLiteralPart, essentialocl_expressions_CollectionRange, CollectionKind},
    associations={oclLibrary7, representedType10, oclLibrary0, elementType1, oclLibrary2, oclLibrary5, oclInvalid26, oclType28, oclCollection30, oclSequence32, oclBoolean12, oclString13, oclInteger16, oclReal19, oclAny22, oclVoid24, representedParameter43, initExpression44, referredType46, oclBag34, oclSet36, oclOrderedSet38, oclTuple40, referredVariable42, referredOperation59, oclLibrary61, property47, value48, part51, referredProperty52, qualifier54, argument57, thenExpression77, elseExpression80, body63, iterator65, in68, variable70, result73, first93, condition75, last95, referredEnumLiteral98, sourceType83, bodyExpression99, source85, item87, part89, elementType90, context101, result104, parameter107},
    generalizations={gen_essentialocl_types_BagType_CollectionType, gen_essentialocl_types_TupleType_Type, gen_essentialocl_types_VoidType_Type, gen_essentialocl_types_TypeType_Type, gen_essentialocl_types_CollectionType_Type, gen_essentialocl_types_InvalidType_Type, gen_essentialocl_types_OrderedSetType_CollectionType, gen_essentialocl_types_SequenceType_CollectionType, gen_essentialocl_types_SetType_CollectionType, gen_essentialocl_expressions_UnlimitedNaturalExp_NumericLiteralExp, gen_essentialocl_expressions_TypeLiteralExp_LiteralExp, gen_essentialocl_expressions_TupleLiteralPart_TypedElement, gen_essentialocl_types_AnyType_Type, gen_essentialocl_expressions_VariableExp_OclExpression, gen_essentialocl_expressions_Variable_TypedElement, gen_essentialocl_expressions_Variable_NamedElement, gen_essentialocl_expressions_OclExpression_TypedElement, gen_essentialocl_expressions_OclExpression_NamedElement, gen_essentialocl_expressions_NumericLiteralExp_PrimitiveLiteralExp, gen_essentialocl_expressions_UndefinedLiteralExp_LiteralExp, gen_essentialocl_expressions_TupleLiteralExp_LiteralExp, gen_essentialocl_expressions_StringLiteralExp_PrimitiveLiteralExp, gen_essentialocl_expressions_RealLiteralExp_NumericLiteralExp, gen_essentialocl_expressions_PropertyCallExp_FeatureCallExp, gen_essentialocl_expressions_PrimitiveLiteralExp_LiteralExp, gen_essentialocl_expressions_OperationCallExp_FeatureCallExp, gen_essentialocl_expressions_FeatureCallExp_CallExp, gen_essentialocl_expressions_LoopExp_CallExp, gen_essentialocl_expressions_LiteralExp_OclExpression, gen_essentialocl_expressions_LetExp_OclExpression, gen_essentialocl_expressions_IteratorExp_LoopExp, gen_essentialocl_expressions_IterateExp_LoopExp, gen_essentialocl_expressions_InvalidLiteralExp_LiteralExp, gen_essentialocl_expressions_IntegerLiteralExp_NumericLiteralExp, gen_essentialocl_expressions_IfExp_OclExpression, gen_essentialocl_expressions_EnumLiteralExp_LiteralExp, gen_essentialocl_expressions_ExpressionInOcl_Expression, gen_essentialocl_expressions_BooleanLiteralExp_PrimitiveLiteralExp, gen_essentialocl_expressions_CallExp_OclExpression, gen_essentialocl_expressions_CollectionItem_CollectionLiteralPart, gen_essentialocl_expressions_CollectionLiteralExp_LiteralExp, gen_essentialocl_expressions_CollectionLiteralPart_TypedElement, gen_essentialocl_expressions_CollectionRange_CollectionLiteralPart},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)