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
            EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Set")
    }
)

# Classes
Class_ = Class(name="Class")
OCL_OclOperation = Class(name="OCL::OclOperation")
Operation = Class(name="Operation")
OclFeature = Class(name="OclFeature")
Variable = Class(name="Variable")
OclExpression = Class(name="OclExpression")
OCL_OclProperty = Class(name="OCL::OclProperty")
Property_ = Class(name="Property")
OCL_OclFeature = Class(name="OCL::OclFeature", is_abstract=True)
OCL_OclModuleElement = Class(name="OCL::OclModuleElement", is_abstract=True)
OclContextDefinition = Class(name="OclContextDefinition")
OCL_DefOclModuleElement = Class(name="OCL::DefOclModuleElement")
OclModuleElement = Class(name="OclModuleElement")
OCL_DeriveOclModuleElement = Class(name="OCL::DeriveOclModuleElement")
Parameter_ = Class(name="Parameter")
OCL_OclContextDefinition = Class(name="OCL::OclContextDefinition")
Element = Class(name="Element")
OCL_MultiplicityElement = Class(name="OCL::MultiplicityElement", is_abstract=True)
OCL_OclModule = Class(name="OCL::OclModule")
Package = Class(name="Package")
OCL_Invariant = Class(name="OCL::Invariant")
OCL_Comment = Class(name="OCL::Comment")
NamedElement = Class(name="NamedElement")
OCL_URIExtent = Class(name="OCL::URIExtent")
Extent = Class(name="Extent")
OCL_PrimitiveType = Class(name="OCL::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
OCL_IntegerType = Class(name="OCL::IntegerType")
PrimitiveType = Class(name="PrimitiveType")
OCL_RealType = Class(name="OCL::RealType")
OCL_BooleanType = Class(name="OCL::BooleanType")
OCL_StringType = Class(name="OCL::StringType")
OCL_TypedElement = Class(name="OCL::TypedElement", is_abstract=True)
Type = Class(name="Type")
OCL_EnumerationLiteral = Class(name="OCL::EnumerationLiteral")
OCL_Parameter = Class(name="OCL::Parameter")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
OCL_Type = Class(name="OCL::Type", is_abstract=True)
OCL_Package = Class(name="OCL::Package")
OCL_Object = Class(name="OCL::Object", is_abstract=True)
OCL_Extent = Class(name="OCL::Extent")
Object = Class(name="Object")
OCL_NamedElement = Class(name="OCL::NamedElement", is_abstract=True)
OCL_Enumeration = Class(name="OCL::Enumeration")
EnumerationLiteral = Class(name="EnumerationLiteral")
OCL_Tag = Class(name="OCL::Tag")
OCL_TupleType = Class(name="OCL::TupleType")
OCL_SetType = Class(name="OCL::SetType")
CollectionType = Class(name="CollectionType")
OCL_Element = Class(name="OCL::Element", is_abstract=True)
OCL_DataType = Class(name="OCL::DataType", is_abstract=True)
OCL_Operation = Class(name="OCL::Operation")
OCL_Property = Class(name="OCL::Property")
OCL_Class = Class(name="OCL::Class")
OCL_AnyType = Class(name="OCL::AnyType")
OCL_VoidType = Class(name="OCL::VoidType")
OCL_SequenceType = Class(name="OCL::SequenceType")
OCL_OrderedSetType = Class(name="OCL::OrderedSetType")
OCL_InvalidType = Class(name="OCL::InvalidType")
OCL_EnumLiteralExp = Class(name="OCL::EnumLiteralExp")
LiteralExp = Class(name="LiteralExp")
OCL_CollectionType = Class(name="OCL::CollectionType", is_abstract=True)
OCL_BagType = Class(name="OCL::BagType")
OCL_TupleLiteralPart = Class(name="OCL::TupleLiteralPart")
OCL_FeaturePropertyCall = Class(name="OCL::FeaturePropertyCall", is_abstract=True)
CallExp = Class(name="CallExp")
OCL_InvalidLiteralExp = Class(name="OCL::InvalidLiteralExp")
OCL_NullLiteralExp = Class(name="OCL::NullLiteralExp")
OCL_TupleLiteralExp = Class(name="OCL::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
OCL_CollectionRange = Class(name="OCL::CollectionRange")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
OCL_CollectionItem = Class(name="OCL::CollectionItem")
OCL_CollectionLiteralPart = Class(name="OCL::CollectionLiteralPart", is_abstract=True)
OCL_CollectionLiteralExp = Class(name="OCL::CollectionLiteralExp")
OCL_NumericLiteralExp = Class(name="OCL::NumericLiteralExp", is_abstract=True)
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
OCL_PrimitiveLiteralExp = Class(name="OCL::PrimitiveLiteralExp", is_abstract=True)
OCL_IterateExp = Class(name="OCL::IterateExp")
LoopExp = Class(name="LoopExp")
OCL_LiteralExp = Class(name="OCL::LiteralExp", is_abstract=True)
OCL_OperationCallExp = Class(name="OCL::OperationCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
OCL_CollectionOperationCallExp = Class(name="OCL::CollectionOperationCallExp")
OperationCallExp = Class(name="OperationCallExp")
OCL_OperatorCallExp = Class(name="OCL::OperatorCallExp")
OCL_IntegerLiteralExp = Class(name="OCL::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
OCL_StringLiteralExp = Class(name="OCL::StringLiteralExp")
OCL_IteratorExp = Class(name="OCL::IteratorExp")
OCL_LoopExp = Class(name="OCL::LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
OCL_Iterator = Class(name="OCL::Iterator")
OCL_VariableExp = Class(name="OCL::VariableExp")
OCL_PropertyCallExp = Class(name="OCL::PropertyCallExp")
OCL_Variable = Class(name="OCL::Variable")
OCL_LetExp = Class(name="OCL::LetExp")
OCL_IfExp = Class(name="OCL::IfExp")
OCL_OclExpression = Class(name="OCL::OclExpression", is_abstract=True)
OCL_CallExp = Class(name="OCL::CallExp", is_abstract=True)
OCL_BooleanLiteralExp = Class(name="OCL::BooleanLiteralExp")
OCL_RealLiteralExp = Class(name="OCL::RealLiteralExp")

# Class class attributes and methods

# OCL_OclOperation class attributes and methods

# Operation class attributes and methods

# OclFeature class attributes and methods

# Variable class attributes and methods

# OclExpression class attributes and methods

# OCL_OclProperty class attributes and methods

# Property class attributes and methods

# OCL_OclFeature class attributes and methods

# OCL_OclModuleElement class attributes and methods

# OclContextDefinition class attributes and methods

# OCL_DefOclModuleElement class attributes and methods

# OclModuleElement class attributes and methods

# OCL_DeriveOclModuleElement class attributes and methods

# Parameter class attributes and methods

# OCL_OclContextDefinition class attributes and methods

# Element class attributes and methods

# OCL_MultiplicityElement class attributes and methods
OCL_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
OCL_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
OCL_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
OCL_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
OCL_MultiplicityElement.attributes={OCL_MultiplicityElement_lower, OCL_MultiplicityElement_upper, OCL_MultiplicityElement_isUnique, OCL_MultiplicityElement_isOrdered}

# OCL_OclModule class attributes and methods

# Package class attributes and methods

# OCL_Invariant class attributes and methods
OCL_Invariant_name: Property = Property(name="name", type=StringType)
OCL_Invariant.attributes={OCL_Invariant_name}

# OCL_Comment class attributes and methods

# NamedElement class attributes and methods

# OCL_URIExtent class attributes and methods

# Extent class attributes and methods

# OCL_PrimitiveType class attributes and methods

# DataType class attributes and methods

# OCL_IntegerType class attributes and methods

# PrimitiveType class attributes and methods

# OCL_RealType class attributes and methods

# OCL_BooleanType class attributes and methods

# OCL_StringType class attributes and methods

# OCL_TypedElement class attributes and methods

# Type class attributes and methods

# OCL_EnumerationLiteral class attributes and methods

# OCL_Parameter class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# OCL_Type class attributes and methods

# OCL_Package class attributes and methods
OCL_Package_uri: Property = Property(name="uri", type=StringType)
OCL_Package.attributes={OCL_Package_uri}

# OCL_Object class attributes and methods

# OCL_Extent class attributes and methods

# Object class attributes and methods

# OCL_NamedElement class attributes and methods
OCL_NamedElement_name: Property = Property(name="name", type=StringType)
OCL_NamedElement.attributes={OCL_NamedElement_name}

# OCL_Enumeration class attributes and methods

# EnumerationLiteral class attributes and methods

# OCL_Tag class attributes and methods
OCL_Tag_value: Property = Property(name="value", type=StringType)
OCL_Tag_name: Property = Property(name="name", type=StringType)
OCL_Tag.attributes={OCL_Tag_value, OCL_Tag_name}

# OCL_TupleType class attributes and methods

# OCL_SetType class attributes and methods

# CollectionType class attributes and methods

# OCL_Element class attributes and methods

# OCL_DataType class attributes and methods

# OCL_Operation class attributes and methods

# OCL_Property class attributes and methods
OCL_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
OCL_Property_isDerived: Property = Property(name="isDerived", type=StringType)
OCL_Property_isComposite: Property = Property(name="isComposite", type=StringType)
OCL_Property_isId: Property = Property(name="isId", type=StringType)
OCL_Property_default: Property = Property(name="default", type=StringType)
OCL_Property.attributes={OCL_Property_isDerived, OCL_Property_isComposite, OCL_Property_default, OCL_Property_isReadOnly, OCL_Property_isId}

# OCL_Class class attributes and methods
OCL_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
OCL_Class.attributes={OCL_Class_isAbstract}

# OCL_AnyType class attributes and methods

# OCL_VoidType class attributes and methods

# OCL_SequenceType class attributes and methods

# OCL_OrderedSetType class attributes and methods

# OCL_InvalidType class attributes and methods

# OCL_EnumLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# OCL_CollectionType class attributes and methods

# OCL_BagType class attributes and methods

# OCL_TupleLiteralPart class attributes and methods

# OCL_FeaturePropertyCall class attributes and methods

# CallExp class attributes and methods

# OCL_InvalidLiteralExp class attributes and methods

# OCL_NullLiteralExp class attributes and methods

# OCL_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# OCL_CollectionRange class attributes and methods

# CollectionLiteralPart class attributes and methods

# OCL_CollectionItem class attributes and methods

# OCL_CollectionLiteralPart class attributes and methods

# OCL_CollectionLiteralExp class attributes and methods
OCL_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
OCL_CollectionLiteralExp.attributes={OCL_CollectionLiteralExp_kind}

# OCL_NumericLiteralExp class attributes and methods

# PrimitiveLiteralExp class attributes and methods

# OCL_PrimitiveLiteralExp class attributes and methods

# OCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# OCL_LiteralExp class attributes and methods

# OCL_OperationCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# OCL_CollectionOperationCallExp class attributes and methods

# OperationCallExp class attributes and methods

# OCL_OperatorCallExp class attributes and methods

# OCL_IntegerLiteralExp class attributes and methods
OCL_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
OCL_IntegerLiteralExp.attributes={OCL_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# OCL_StringLiteralExp class attributes and methods
OCL_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
OCL_StringLiteralExp.attributes={OCL_StringLiteralExp_stringSymbol}

# OCL_IteratorExp class attributes and methods

# OCL_LoopExp class attributes and methods

# Iterator class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_VariableExp class attributes and methods

# OCL_PropertyCallExp class attributes and methods

# OCL_Variable class attributes and methods

# OCL_LetExp class attributes and methods

# OCL_IfExp class attributes and methods

# OCL_OclExpression class attributes and methods

# OCL_CallExp class attributes and methods

# OCL_BooleanLiteralExp class attributes and methods
OCL_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
OCL_BooleanLiteralExp.attributes={OCL_BooleanLiteralExp_booleanSymbol}

# OCL_RealLiteralExp class attributes and methods
OCL_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
OCL_RealLiteralExp.attributes={OCL_RealLiteralExp_realSymbol}

# Relationships
contextElement17: BinaryAssociation = BinaryAssociation(
    name="contextElement17",
    ends={
        Property(name="Class", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclContextDefinition", type=Class_, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnVariable0: BinaryAssociation = BinaryAssociation(
    name="returnVariable0",
    ends={
        Property(name="Variable", type=OCL_OclOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclOperation", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body1: BinaryAssociation = BinaryAssociation(
    name="body1",
    ends={
        Property(name="OclExpression", type=OCL_OclOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclOperation2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable3: BinaryAssociation = BinaryAssociation(
    name="contextVariable3",
    ends={
        Property(name="Variable5", type=OCL_OclOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclOperation4", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body6: BinaryAssociation = BinaryAssociation(
    name="body6",
    ends={
        Property(name="OclExpression7", type=OCL_OclProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable8: BinaryAssociation = BinaryAssociation(
    name="contextVariable8",
    ends={
        Property(name="Variable10", type=OCL_OclProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclProperty9", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextDefinition11: BinaryAssociation = BinaryAssociation(
    name="contextDefinition11",
    ends={
        Property(name="OclContextDefinition", type=OCL_OclModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclModuleElement", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature12: BinaryAssociation = BinaryAssociation(
    name="feature12",
    ends={
        Property(name="OclFeature", type=OCL_DefOclModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_DefOclModuleElement", type=OclFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refAttr13: BinaryAssociation = BinaryAssociation(
    name="refAttr13",
    ends={
        Property(name="Parameter", type=OCL_DeriveOclModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_DeriveOclModuleElement", type=Parameter_, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
specification14: BinaryAssociation = BinaryAssociation(
    name="specification14",
    ends={
        Property(name="OclExpression16", type=OCL_DeriveOclModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_DeriveOclModuleElement15", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedElements18: BinaryAssociation = BinaryAssociation(
    name="ownedElements18",
    ends={
        Property(name="OclModuleElement", type=OCL_OclModule, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OclModule", type=OclModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification19: BinaryAssociation = BinaryAssociation(
    name="specification19",
    ends={
        Property(name="OclExpression20", type=OCL_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Invariant", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable21: BinaryAssociation = BinaryAssociation(
    name="contextVariable21",
    ends={
        Property(name="Variable23", type=OCL_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Invariant22", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotatedElement24: BinaryAssociation = BinaryAssociation(
    name="annotatedElement24",
    ends={
        Property(name="NamedElement", type=OCL_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="Type", type=OCL_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_TypedElement", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType26: BinaryAssociation = BinaryAssociation(
    name="ownedType26",
    ends={
        Property(name="Type27", type=OCL_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Package", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage28: BinaryAssociation = BinaryAssociation(
    name="nestedPackage28",
    ends={
        Property(name="Package", type=OCL_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Package29", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral30: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral30",
    ends={
        Property(name="EnumerationLiteral", type=OCL_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element31: BinaryAssociation = BinaryAssociation(
    name="element31",
    ends={
        Property(name="Element", type=OCL_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter32: BinaryAssociation = BinaryAssociation(
    name="ownedParameter32",
    ends={
        Property(name="Parameter33", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException34: BinaryAssociation = BinaryAssociation(
    name="raisedException34",
    ends={
        Property(name="Type36", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Operation35", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
opposite37: BinaryAssociation = BinaryAssociation(
    name="opposite37",
    ends={
        Property(name="Property", type=OCL_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute38: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute38",
    ends={
        Property(name="Property39", type=OCL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation40: BinaryAssociation = BinaryAssociation(
    name="ownedOperation40",
    ends={
        Property(name="Operation", type=OCL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Class41", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part59: BinaryAssociation = BinaryAssociation(
    name="part59",
    ends={
        Property(name="CollectionLiteralPart", type=OCL_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredEnumLiteral42: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral42",
    ends={
        Property(name="EnumerationLiteral43", type=OCL_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
elementType44: BinaryAssociation = BinaryAssociation(
    name="elementType44",
    ends={
        Property(name="Type45", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
value46: BinaryAssociation = BinaryAssociation(
    name="value46",
    ends={
        Property(name="OclExpression47", type=OCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_TupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute48: BinaryAssociation = BinaryAssociation(
    name="attribute48",
    ends={
        Property(name="Property50", type=OCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_TupleLiteralPart49", type=Property_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part51: BinaryAssociation = BinaryAssociation(
    name="part51",
    ends={
        Property(name="TupleLiteralPart", type=OCL_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first52: BinaryAssociation = BinaryAssociation(
    name="first52",
    ends={
        Property(name="OclExpression53", type=OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last54: BinaryAssociation = BinaryAssociation(
    name="last54",
    ends={
        Property(name="OclExpression56", type=OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_CollectionRange55", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item57: BinaryAssociation = BinaryAssociation(
    name="item57",
    ends={
        Property(name="OclExpression58", type=OCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindParameter70: BinaryAssociation = BinaryAssociation(
    name="bindParameter70",
    ends={
        Property(name="Parameter71", type=OCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Variable", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
result60: BinaryAssociation = BinaryAssociation(
    name="result60",
    ends={
        Property(name="Variable61", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument62: BinaryAssociation = BinaryAssociation(
    name="argument62",
    ends={
        Property(name="OclExpression63", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="OclExpression65", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator66: BinaryAssociation = BinaryAssociation(
    name="iterator66",
    ends={
        Property(name="Iterator", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_LoopExp67", type=Iterator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable68: BinaryAssociation = BinaryAssociation(
    name="referredVariable68",
    ends={
        Property(name="Variable69", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
initExpression72: BinaryAssociation = BinaryAssociation(
    name="initExpression72",
    ends={
        Property(name="OclExpression74", type=OCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_Variable73", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable75: BinaryAssociation = BinaryAssociation(
    name="variable75",
    ends={
        Property(name="Variable76", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_LetExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in77: BinaryAssociation = BinaryAssociation(
    name="in77",
    ends={
        Property(name="OclExpression79", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_LetExp78", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression80: BinaryAssociation = BinaryAssociation(
    name="elseExpression80",
    ends={
        Property(name="OclExpression81", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression82: BinaryAssociation = BinaryAssociation(
    name="thenExpression82",
    ends={
        Property(name="OclExpression84", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_IfExp83", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition85: BinaryAssociation = BinaryAssociation(
    name="condition85",
    ends={
        Property(name="OclExpression87", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_IfExp86", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source88: BinaryAssociation = BinaryAssociation(
    name="source88",
    ends={
        Property(name="OclExpression89", type=OCL_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_OCL_OclOperation_Operation = Generalization(general=Operation, specific=OCL_OclOperation)
gen_OCL_OclOperation_OclFeature = Generalization(general=OclFeature, specific=OCL_OclOperation)
gen_OCL_OclProperty_Property = Generalization(general=Property_, specific=OCL_OclProperty)
gen_OCL_OclProperty_OclFeature = Generalization(general=OclFeature, specific=OCL_OclProperty)
gen_OCL_DefOclModuleElement_OclModuleElement = Generalization(general=OclModuleElement, specific=OCL_DefOclModuleElement)
gen_OCL_DeriveOclModuleElement_OclModuleElement = Generalization(general=OclModuleElement, specific=OCL_DeriveOclModuleElement)
gen_OCL_OclContextDefinition_Element = Generalization(general=Element, specific=OCL_OclContextDefinition)
gen_OCL_OclModule_Package = Generalization(general=Package, specific=OCL_OclModule)
gen_OCL_Invariant_OclModuleElement = Generalization(general=OclModuleElement, specific=OCL_Invariant)
gen_OCL_Comment_Element = Generalization(general=Element, specific=OCL_Comment)
gen_OCL_URIExtent_Extent = Generalization(general=Extent, specific=OCL_URIExtent)
gen_OCL_PrimitiveType_DataType = Generalization(general=DataType, specific=OCL_PrimitiveType)
gen_OCL_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=OCL_IntegerType)
gen_OCL_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=OCL_RealType)
gen_OCL_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=OCL_BooleanType)
gen_OCL_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=OCL_StringType)
gen_OCL_TypedElement_NamedElement = Generalization(general=NamedElement, specific=OCL_TypedElement)
gen_OCL_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=OCL_EnumerationLiteral)
gen_OCL_Parameter_TypedElement = Generalization(general=TypedElement, specific=OCL_Parameter)
gen_OCL_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=OCL_Parameter)
gen_OCL_Type_NamedElement = Generalization(general=NamedElement, specific=OCL_Type)
gen_OCL_Package_NamedElement = Generalization(general=NamedElement, specific=OCL_Package)
gen_OCL_Extent_Object = Generalization(general=Object, specific=OCL_Extent)
gen_OCL_NamedElement_Element = Generalization(general=Element, specific=OCL_NamedElement)
gen_OCL_Enumeration_DataType = Generalization(general=DataType, specific=OCL_Enumeration)
gen_OCL_Tag_Element = Generalization(general=Element, specific=OCL_Tag)
gen_OCL_TupleType_DataType = Generalization(general=DataType, specific=OCL_TupleType)
gen_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=OCL_SetType)
gen_OCL_Element_Object = Generalization(general=Object, specific=OCL_Element)
gen_OCL_DataType_Type = Generalization(general=Type, specific=OCL_DataType)
gen_OCL_Operation_TypedElement = Generalization(general=TypedElement, specific=OCL_Operation)
gen_OCL_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=OCL_Operation)
gen_OCL_Property_TypedElement = Generalization(general=TypedElement, specific=OCL_Property)
gen_OCL_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=OCL_Property)
gen_OCL_Class_Type = Generalization(general=Type, specific=OCL_Class)
gen_OCL_AnyType_Class = Generalization(general=Class_, specific=OCL_AnyType)
gen_OCL_VoidType_Type = Generalization(general=Type, specific=OCL_VoidType)
gen_OCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=OCL_CollectionLiteralExp)
gen_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=OCL_SequenceType)
gen_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=OCL_OrderedSetType)
gen_OCL_InvalidType_Type = Generalization(general=Type, specific=OCL_InvalidType)
gen_OCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=OCL_EnumLiteralExp)
gen_OCL_CollectionType_DataType = Generalization(general=DataType, specific=OCL_CollectionType)
gen_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=OCL_BagType)
gen_OCL_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=OCL_TupleLiteralPart)
gen_OCL_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=OCL_FeaturePropertyCall)
gen_OCL_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=OCL_InvalidLiteralExp)
gen_OCL_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=OCL_NullLiteralExp)
gen_OCL_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=OCL_TupleLiteralExp)
gen_OCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=OCL_CollectionRange)
gen_OCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=OCL_CollectionItem)
gen_OCL_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=OCL_CollectionLiteralPart)
gen_OCL_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=OCL_NumericLiteralExp)
gen_OCL_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=OCL_PrimitiveLiteralExp)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LiteralExp)
gen_OCL_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=OCL_OperationCallExp)
gen_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_CollectionOperationCallExp)
gen_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_OperatorCallExp)
gen_OCL_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=OCL_IntegerLiteralExp)
gen_OCL_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=OCL_StringLiteralExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LoopExp_CallExp = Generalization(general=CallExp, specific=OCL_LoopExp)
gen_OCL_Iterator_Variable = Generalization(general=Variable, specific=OCL_Iterator)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=OCL_PropertyCallExp)
gen_OCL_Variable_TypedElement = Generalization(general=TypedElement, specific=OCL_Variable)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
gen_OCL_OclExpression_TypedElement = Generalization(general=TypedElement, specific=OCL_OclExpression)
gen_OCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=OCL_CallExp)
gen_OCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=OCL_BooleanLiteralExp)
gen_OCL_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=OCL_RealLiteralExp)

# Domain Model
domain_model = DomainModel(
    name="OCL",
    types={Class_, OCL_OclOperation, Operation, OclFeature, Variable, OclExpression, OCL_OclProperty, Property_, OCL_OclFeature, OCL_OclModuleElement, OclContextDefinition, OCL_DefOclModuleElement, OclModuleElement, OCL_DeriveOclModuleElement, Parameter_, OCL_OclContextDefinition, Element, OCL_MultiplicityElement, OCL_OclModule, Package, OCL_Invariant, OCL_Comment, NamedElement, OCL_URIExtent, Extent, OCL_PrimitiveType, DataType, OCL_IntegerType, PrimitiveType, OCL_RealType, OCL_BooleanType, OCL_StringType, OCL_TypedElement, Type, OCL_EnumerationLiteral, OCL_Parameter, TypedElement, MultiplicityElement, OCL_Type, OCL_Package, OCL_Object, OCL_Extent, Object, OCL_NamedElement, OCL_Enumeration, EnumerationLiteral, OCL_Tag, OCL_TupleType, OCL_SetType, CollectionType, OCL_Element, OCL_DataType, OCL_Operation, OCL_Property, OCL_Class, OCL_AnyType, OCL_VoidType, OCL_SequenceType, OCL_OrderedSetType, OCL_InvalidType, OCL_EnumLiteralExp, LiteralExp, OCL_CollectionType, OCL_BagType, OCL_TupleLiteralPart, OCL_FeaturePropertyCall, CallExp, OCL_InvalidLiteralExp, OCL_NullLiteralExp, OCL_TupleLiteralExp, TupleLiteralPart, OCL_CollectionRange, CollectionLiteralPart, OCL_CollectionItem, OCL_CollectionLiteralPart, OCL_CollectionLiteralExp, OCL_NumericLiteralExp, PrimitiveLiteralExp, OCL_PrimitiveLiteralExp, OCL_IterateExp, LoopExp, OCL_LiteralExp, OCL_OperationCallExp, FeaturePropertyCall, OCL_CollectionOperationCallExp, OperationCallExp, OCL_OperatorCallExp, OCL_IntegerLiteralExp, NumericLiteralExp, OCL_StringLiteralExp, OCL_IteratorExp, OCL_LoopExp, Iterator, OCL_Iterator, OCL_VariableExp, OCL_PropertyCallExp, OCL_Variable, OCL_LetExp, OCL_IfExp, OCL_OclExpression, OCL_CallExp, OCL_BooleanLiteralExp, OCL_RealLiteralExp, CollectionKind},
    associations={contextElement17, returnVariable0, body1, contextVariable3, body6, contextVariable8, contextDefinition11, feature12, refAttr13, specification14, ownedElements18, specification19, contextVariable21, annotatedElement24, type25, ownedType26, nestedPackage28, ownedLiteral30, element31, ownedParameter32, raisedException34, opposite37, ownedAttribute38, ownedOperation40, part59, referredEnumLiteral42, elementType44, value46, attribute48, part51, first52, last54, item57, bindParameter70, result60, argument62, body64, iterator66, referredVariable68, initExpression72, variable75, in77, elseExpression80, thenExpression82, condition85, source88},
    generalizations={gen_OCL_OclOperation_Operation, gen_OCL_OclOperation_OclFeature, gen_OCL_OclProperty_Property, gen_OCL_OclProperty_OclFeature, gen_OCL_DefOclModuleElement_OclModuleElement, gen_OCL_DeriveOclModuleElement_OclModuleElement, gen_OCL_OclContextDefinition_Element, gen_OCL_OclModule_Package, gen_OCL_Invariant_OclModuleElement, gen_OCL_Comment_Element, gen_OCL_URIExtent_Extent, gen_OCL_PrimitiveType_DataType, gen_OCL_IntegerType_PrimitiveType, gen_OCL_RealType_PrimitiveType, gen_OCL_BooleanType_PrimitiveType, gen_OCL_StringType_PrimitiveType, gen_OCL_TypedElement_NamedElement, gen_OCL_EnumerationLiteral_NamedElement, gen_OCL_Parameter_TypedElement, gen_OCL_Parameter_MultiplicityElement, gen_OCL_Type_NamedElement, gen_OCL_Package_NamedElement, gen_OCL_Extent_Object, gen_OCL_NamedElement_Element, gen_OCL_Enumeration_DataType, gen_OCL_Tag_Element, gen_OCL_TupleType_DataType, gen_OCL_SetType_CollectionType, gen_OCL_Element_Object, gen_OCL_DataType_Type, gen_OCL_Operation_TypedElement, gen_OCL_Operation_MultiplicityElement, gen_OCL_Property_TypedElement, gen_OCL_Property_MultiplicityElement, gen_OCL_Class_Type, gen_OCL_AnyType_Class, gen_OCL_VoidType_Type, gen_OCL_CollectionLiteralExp_LiteralExp, gen_OCL_SequenceType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_InvalidType_Type, gen_OCL_EnumLiteralExp_LiteralExp, gen_OCL_CollectionType_DataType, gen_OCL_BagType_CollectionType, gen_OCL_TupleLiteralPart_TypedElement, gen_OCL_FeaturePropertyCall_CallExp, gen_OCL_InvalidLiteralExp_LiteralExp, gen_OCL_NullLiteralExp_LiteralExp, gen_OCL_TupleLiteralExp_LiteralExp, gen_OCL_CollectionRange_CollectionLiteralPart, gen_OCL_CollectionItem_CollectionLiteralPart, gen_OCL_CollectionLiteralPart_TypedElement, gen_OCL_NumericLiteralExp_PrimitiveLiteralExp, gen_OCL_PrimitiveLiteralExp_LiteralExp, gen_OCL_IterateExp_LoopExp, gen_OCL_LiteralExp_OclExpression, gen_OCL_OperationCallExp_FeaturePropertyCall, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_IntegerLiteralExp_NumericLiteralExp, gen_OCL_StringLiteralExp_PrimitiveLiteralExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LoopExp_CallExp, gen_OCL_Iterator_Variable, gen_OCL_VariableExp_OclExpression, gen_OCL_PropertyCallExp_FeaturePropertyCall, gen_OCL_Variable_TypedElement, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_OclExpression_TypedElement, gen_OCL_CallExp_OclExpression, gen_OCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_OCL_RealLiteralExp_NumericLiteralExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)