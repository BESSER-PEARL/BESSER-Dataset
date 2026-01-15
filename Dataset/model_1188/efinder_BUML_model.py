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
OperatorKind: Enumeration = Enumeration(
    name="OperatorKind",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="IMPLIES"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="LESS_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_OR_EQUAL"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="DISTINCT"),
			EnumerationLiteral(name="AND")
    }
)

# Classes
ir_EFMetamodel = Class(name="ir::EFMetamodel")
ir_Constraint = Class(name="ir::Constraint", is_abstract=True)
ir_EFClass = Class(name="ir::EFClass")
ir_DerivedProperty = Class(name="ir::DerivedProperty", is_abstract=True)
ir_Operation = Class(name="ir::Operation", is_abstract=True)
ir_Specification = Class(name="ir::Specification")
ir_FeatureRef = Class(name="ir::FeatureRef", is_abstract=True)
ir_OperationFeatureRef = Class(name="ir::OperationFeatureRef", is_abstract=True)
FeatureRef = Class(name="FeatureRef")
ir_BuiltinOperationRef = Class(name="ir::BuiltinOperationRef")
OperationFeatureRef = Class(name="OperationFeatureRef")
ir_DefinedOperationRef = Class(name="ir::DefinedOperationRef")
ir_PropertyFeatureRef = Class(name="ir::PropertyFeatureRef", is_abstract=True)
ir_TupleFieldRef = Class(name="ir::TupleFieldRef")
PropertyFeatureRef = Class(name="PropertyFeatureRef")
ir_EFPrimitiveType = Class(name="ir::EFPrimitiveType")
ir_EFTupleType = Class(name="ir::EFTupleType")
ir_TypedElement = Class(name="ir::TypedElement", is_abstract=True)
ir_TypeRef = Class(name="ir::TypeRef", is_abstract=True)
ir_AbstractFunction = Class(name="ir::AbstractFunction", is_abstract=True)
TypedElement = Class(name="TypedElement")
ir_EFType = Class(name="ir::EFType", is_abstract=True)
AbstractFunction = Class(name="AbstractFunction")
ir_Parameter = Class(name="ir::Parameter")
ir_EFEnum = Class(name="ir::EFEnum")
EFType = Class(name="EFType")
ir_EClass = Class(name="ir::EClass")
ir_EEnum = Class(name="ir::EEnum")
ir_DerivedPropertyRef = Class(name="ir::DerivedPropertyRef")
ir_BuiltinPropertyRef = Class(name="ir::BuiltinPropertyRef")
ir_MetamodelFeatureRef = Class(name="ir::MetamodelFeatureRef")
ir_EStructuralFeature = Class(name="ir::EStructuralFeature")
ir_VariableDeclaration = Class(name="ir::VariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
ir_EFPackage = Class(name="ir::EFPackage")
ir_EPackage = Class(name="ir::EPackage")
ir_InvalidTypeRef = Class(name="ir::InvalidTypeRef")
ir_CollectionTypeRef = Class(name="ir::CollectionTypeRef", is_abstract=True)
ir_SetTypeRef = Class(name="ir::SetTypeRef")
CollectionTypeRef = Class(name="CollectionTypeRef")
ir_SequenceTypeRef = Class(name="ir::SequenceTypeRef")
ir_BagTypeRef = Class(name="ir::BagTypeRef")
ir_OrderedSetTypeRef = Class(name="ir::OrderedSetTypeRef")
ir_EFEnumLiteral = Class(name="ir::EFEnumLiteral")
ir_TupleTypeElement = Class(name="ir::TupleTypeElement")
ir_MetaTypeRef = Class(name="ir::MetaTypeRef")
TypeRef = Class(name="TypeRef")
ir_ocl_ModelElement = Class(name="ir::ocl::ModelElement")
ir_ocl_CallExp = Class(name="ir::ocl::CallExp", is_abstract=True)
ir_ocl_AbstractOperationCallExp = Class(name="ir::ocl::AbstractOperationCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
ir_ocl_OperationCallExp = Class(name="ir::ocl::OperationCallExp")
AbstractOperationCallExp = Class(name="AbstractOperationCallExp")
ocl_ir_OperationFeatureRef = Class(name="ocl::ir::OperationFeatureRef")
ir_ocl_WithContextVariable = Class(name="ir::ocl::WithContextVariable", is_abstract=True)
ocl_ir_VariableDeclaration = Class(name="ocl::ir::VariableDeclaration")
ir_ocl_OclInvariant = Class(name="ir::ocl::OclInvariant")
Constraint = Class(name="Constraint")
ocl_WithContextVariable = Class(name="ocl::WithContextVariable")
ocl_ir_EFClass = Class(name="ocl::ir::EFClass")
OclExpression = Class(name="OclExpression")
ir_ocl_OclDerivedProperty = Class(name="ir::ocl::OclDerivedProperty")
DerivedProperty = Class(name="DerivedProperty")
ir_ocl_OclOperation = Class(name="ir::ocl::OclOperation")
Operation = Class(name="Operation")
ir_ocl_OclExpression = Class(name="ir::ocl::OclExpression", is_abstract=True)
ocl_ir_TypeRef = Class(name="ocl::ir::TypeRef")
ir_ocl_Iterator = Class(name="ir::ocl::Iterator")
ir_ocl_IfExp = Class(name="ir::ocl::IfExp")
ir_ocl_LetExp = Class(name="ir::ocl::LetExp")
ir_ocl_PropertyCallExp = Class(name="ir::ocl::PropertyCallExp")
ocl_ir_PropertyFeatureRef = Class(name="ocl::ir::PropertyFeatureRef")
ir_ocl_CollectionCallExp = Class(name="ir::ocl::CollectionCallExp")
ir_ocl_LoopExp = Class(name="ir::ocl::LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
ir_ocl_IteratorExp = Class(name="ir::ocl::IteratorExp")
LoopExp = Class(name="LoopExp")
ir_ocl_IterateExp = Class(name="ir::ocl::IterateExp")
ir_ocl_VarExp = Class(name="ir::ocl::VarExp")
ir_ocl_LiteralExp = Class(name="ir::ocl::LiteralExp", is_abstract=True)
ir_ocl_OperatorCallExp = Class(name="ir::ocl::OperatorCallExp")
TuplePart = Class(name="TuplePart")
ir_ocl_TuplePart = Class(name="ir::ocl::TuplePart")
ir_ocl_EnumLiteralExp = Class(name="ir::ocl::EnumLiteralExp")
ocl_ir_MetaTypeRef = Class(name="ocl::ir::MetaTypeRef")
ocl_ir_EFEnumLiteral = Class(name="ocl::ir::EFEnumLiteral")
ir_ocl_BooleanLiteralExp = Class(name="ir::ocl::BooleanLiteralExp")
LiteralExp = Class(name="LiteralExp")
ir_ocl_StringLiteralExp = Class(name="ir::ocl::StringLiteralExp")
ir_ocl_IntegerLiteralExp = Class(name="ir::ocl::IntegerLiteralExp")
ir_ocl_RealLiteralExp = Class(name="ir::ocl::RealLiteralExp")
ir_ocl_OclUndefined = Class(name="ir::ocl::OclUndefined")
ir_ocl_OclInvalid = Class(name="ir::ocl::OclInvalid")
ir_ocl_TupleLiteralExp = Class(name="ir::ocl::TupleLiteralExp")
ocl_ir_EFTupleType = Class(name="ocl::ir::EFTupleType")
ir_ocl_CollectionLiteralExp = Class(name="ir::ocl::CollectionLiteralExp", is_abstract=True)
ir_ocl_SetLiteralExp = Class(name="ir::ocl::SetLiteralExp")
CollectionLiteralExp = Class(name="CollectionLiteralExp")
ir_ocl_OrderedSetLiteralExp = Class(name="ir::ocl::OrderedSetLiteralExp")
ir_ocl_SequenceLiteralExp = Class(name="ir::ocl::SequenceLiteralExp")
ir_ocl_BagLiteralExp = Class(name="ir::ocl::BagLiteralExp")
ir_ocl_UnsupportedExp = Class(name="ir::ocl::UnsupportedExp")
ir_ocl_OclAnyLibElement = Class(name="ir::ocl::OclAnyLibElement")

# ir_EFMetamodel class attributes and methods

# ir_Constraint class attributes and methods
ir_Constraint_name: Property = Property(name="name", type=StringType)
ir_Constraint.attributes={ir_Constraint_name}

# ir_EFClass class attributes and methods

# ir_DerivedProperty class attributes and methods

# ir_Operation class attributes and methods

# ir_Specification class attributes and methods

# ir_FeatureRef class attributes and methods

# ir_OperationFeatureRef class attributes and methods

# FeatureRef class attributes and methods

# ir_BuiltinOperationRef class attributes and methods

# OperationFeatureRef class attributes and methods

# ir_DefinedOperationRef class attributes and methods

# ir_PropertyFeatureRef class attributes and methods

# ir_TupleFieldRef class attributes and methods
ir_TupleFieldRef_name: Property = Property(name="name", type=StringType)
ir_TupleFieldRef.attributes={ir_TupleFieldRef_name}

# PropertyFeatureRef class attributes and methods

# ir_EFPrimitiveType class attributes and methods
ir_EFPrimitiveType_name: Property = Property(name="name", type=StringType)
ir_EFPrimitiveType.attributes={ir_EFPrimitiveType_name}

# ir_EFTupleType class attributes and methods
ir_EFTupleType_id: Property = Property(name="id", type=StringType)
ir_EFTupleType.attributes={ir_EFTupleType_id}

# ir_TypedElement class attributes and methods

# ir_TypeRef class attributes and methods

# ir_AbstractFunction class attributes and methods
ir_AbstractFunction_name: Property = Property(name="name", type=StringType)
ir_AbstractFunction.attributes={ir_AbstractFunction_name}

# TypedElement class attributes and methods

# ir_EFType class attributes and methods

# AbstractFunction class attributes and methods

# ir_Parameter class attributes and methods

# ir_EFEnum class attributes and methods

# EFType class attributes and methods

# ir_EClass class attributes and methods

# ir_EEnum class attributes and methods

# ir_DerivedPropertyRef class attributes and methods

# ir_BuiltinPropertyRef class attributes and methods

# ir_MetamodelFeatureRef class attributes and methods

# ir_EStructuralFeature class attributes and methods

# ir_VariableDeclaration class attributes and methods
ir_VariableDeclaration_name: Property = Property(name="name", type=StringType)
ir_VariableDeclaration.attributes={ir_VariableDeclaration_name}

# VariableDeclaration class attributes and methods

# ir_EFPackage class attributes and methods

# ir_EPackage class attributes and methods

# ir_InvalidTypeRef class attributes and methods

# ir_CollectionTypeRef class attributes and methods

# ir_SetTypeRef class attributes and methods

# CollectionTypeRef class attributes and methods

# ir_SequenceTypeRef class attributes and methods

# ir_BagTypeRef class attributes and methods

# ir_OrderedSetTypeRef class attributes and methods

# ir_EFEnumLiteral class attributes and methods
ir_EFEnumLiteral_name: Property = Property(name="name", type=StringType)
ir_EFEnumLiteral.attributes={ir_EFEnumLiteral_name}

# ir_TupleTypeElement class attributes and methods
ir_TupleTypeElement_name: Property = Property(name="name", type=StringType)
ir_TupleTypeElement.attributes={ir_TupleTypeElement_name}

# ir_MetaTypeRef class attributes and methods

# TypeRef class attributes and methods

# ir_ocl_ModelElement class attributes and methods

# ir_ocl_CallExp class attributes and methods

# ir_ocl_AbstractOperationCallExp class attributes and methods

# CallExp class attributes and methods

# ir_ocl_OperationCallExp class attributes and methods
ir_ocl_OperationCallExp_name: Property = Property(name="name", type=StringType)
ir_ocl_OperationCallExp.attributes={ir_ocl_OperationCallExp_name}

# AbstractOperationCallExp class attributes and methods

# ocl_ir_OperationFeatureRef class attributes and methods

# ir_ocl_WithContextVariable class attributes and methods

# ocl_ir_VariableDeclaration class attributes and methods

# ir_ocl_OclInvariant class attributes and methods

# Constraint class attributes and methods

# ocl_WithContextVariable class attributes and methods

# ocl_ir_EFClass class attributes and methods

# OclExpression class attributes and methods

# ir_ocl_OclDerivedProperty class attributes and methods

# DerivedProperty class attributes and methods

# ir_ocl_OclOperation class attributes and methods

# Operation class attributes and methods

# ir_ocl_OclExpression class attributes and methods

# ocl_ir_TypeRef class attributes and methods

# ir_ocl_Iterator class attributes and methods

# ir_ocl_IfExp class attributes and methods

# ir_ocl_LetExp class attributes and methods

# ir_ocl_PropertyCallExp class attributes and methods
ir_ocl_PropertyCallExp_name: Property = Property(name="name", type=StringType)
ir_ocl_PropertyCallExp.attributes={ir_ocl_PropertyCallExp_name}

# ocl_ir_PropertyFeatureRef class attributes and methods

# ir_ocl_CollectionCallExp class attributes and methods
ir_ocl_CollectionCallExp_name: Property = Property(name="name", type=StringType)
ir_ocl_CollectionCallExp.attributes={ir_ocl_CollectionCallExp_name}

# ir_ocl_LoopExp class attributes and methods

# Iterator class attributes and methods

# ir_ocl_IteratorExp class attributes and methods
ir_ocl_IteratorExp_name: Property = Property(name="name", type=StringType)
ir_ocl_IteratorExp.attributes={ir_ocl_IteratorExp_name}

# LoopExp class attributes and methods

# ir_ocl_IterateExp class attributes and methods

# ir_ocl_VarExp class attributes and methods

# ir_ocl_LiteralExp class attributes and methods

# ir_ocl_OperatorCallExp class attributes and methods
ir_ocl_OperatorCallExp_operator: Property = Property(name="operator", type=StringType)
ir_ocl_OperatorCallExp.attributes={ir_ocl_OperatorCallExp_operator}

# TuplePart class attributes and methods

# ir_ocl_TuplePart class attributes and methods
ir_ocl_TuplePart_name: Property = Property(name="name", type=StringType)
ir_ocl_TuplePart.attributes={ir_ocl_TuplePart_name}

# ir_ocl_EnumLiteralExp class attributes and methods

# ocl_ir_MetaTypeRef class attributes and methods

# ocl_ir_EFEnumLiteral class attributes and methods

# ir_ocl_BooleanLiteralExp class attributes and methods
ir_ocl_BooleanLiteralExp_value: Property = Property(name="value", type=BooleanType)
ir_ocl_BooleanLiteralExp.attributes={ir_ocl_BooleanLiteralExp_value}

# LiteralExp class attributes and methods

# ir_ocl_StringLiteralExp class attributes and methods
ir_ocl_StringLiteralExp_value: Property = Property(name="value", type=StringType)
ir_ocl_StringLiteralExp.attributes={ir_ocl_StringLiteralExp_value}

# ir_ocl_IntegerLiteralExp class attributes and methods
ir_ocl_IntegerLiteralExp_value: Property = Property(name="value", type=StringType)
ir_ocl_IntegerLiteralExp.attributes={ir_ocl_IntegerLiteralExp_value}

# ir_ocl_RealLiteralExp class attributes and methods
ir_ocl_RealLiteralExp_value: Property = Property(name="value", type=StringType)
ir_ocl_RealLiteralExp.attributes={ir_ocl_RealLiteralExp_value}

# ir_ocl_OclUndefined class attributes and methods

# ir_ocl_OclInvalid class attributes and methods

# ir_ocl_TupleLiteralExp class attributes and methods

# ocl_ir_EFTupleType class attributes and methods

# ir_ocl_CollectionLiteralExp class attributes and methods

# ir_ocl_SetLiteralExp class attributes and methods

# CollectionLiteralExp class attributes and methods

# ir_ocl_OrderedSetLiteralExp class attributes and methods

# ir_ocl_SequenceLiteralExp class attributes and methods

# ir_ocl_BagLiteralExp class attributes and methods

# ir_ocl_UnsupportedExp class attributes and methods
ir_ocl_UnsupportedExp_reason: Property = Property(name="reason", type=StringType)
ir_ocl_UnsupportedExp_description: Property = Property(name="description", type=StringType)
ir_ocl_UnsupportedExp.attributes={ir_ocl_UnsupportedExp_reason, ir_ocl_UnsupportedExp_description}

# ir_ocl_OclAnyLibElement class attributes and methods

# Relationships
metamodels0: BinaryAssociation = BinaryAssociation(
    name="metamodels0",
    ends={
        Property(name="ir_EFMetamodel", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification", type=ir_EFMetamodel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constaints1: BinaryAssociation = BinaryAssociation(
    name="constaints1",
    ends={
        Property(name="ir_Constraint", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification2", type=ir_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
temporary3: BinaryAssociation = BinaryAssociation(
    name="temporary3",
    ends={
        Property(name="ir_EFClass", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification4", type=ir_EFClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="ir_DerivedProperty", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification6", type=ir_DerivedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation17: BinaryAssociation = BinaryAssociation(
    name="operation17",
    ends={
        Property(name="ir_Operation18", type=ir_DefinedOperationRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_DefinedOperationRef", type=ir_Operation, multiplicity=Multiplicity(1, 1))
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="ir_EFTupleType20", type=ir_TupleFieldRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TupleFieldRef", type=ir_EFTupleType, multiplicity=Multiplicity(1, 1))
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="ir_Operation", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification8", type=ir_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveTypes9: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes9",
    ends={
        Property(name="ir_EFPrimitiveType", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification10", type=ir_EFPrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tupleTypes11: BinaryAssociation = BinaryAssociation(
    name="tupleTypes11",
    ends={
        Property(name="ir_EFTupleType", type=ir_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Specification12", type=ir_EFTupleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="ir_TypeRef", type=ir_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypedElement", type=ir_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context14: BinaryAssociation = BinaryAssociation(
    name="context14",
    ends={
        Property(name="ir_EFType", type=ir_AbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_AbstractFunction", type=ir_EFType, multiplicity=Multiplicity(0, 1))
    }
)
parameters15: BinaryAssociation = BinaryAssociation(
    name="parameters15",
    ends={
        Property(name="ir_Parameter", type=ir_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Operation16", type=ir_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes30: BinaryAssociation = BinaryAssociation(
    name="classes30",
    ends={
        Property(name="ir_EFClass32", type=ir_EFPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFPackage31", type=ir_EFClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerations33: BinaryAssociation = BinaryAssociation(
    name="enumerations33",
    ends={
        Property(name="ir_EFEnum", type=ir_EFPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFPackage34", type=ir_EFEnum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
klass35: BinaryAssociation = BinaryAssociation(
    name="klass35",
    ends={
        Property(name="ir_EClass", type=ir_EFClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFClass36", type=ir_EClass, multiplicity=Multiplicity(1, 1))
    }
)
enum_37: BinaryAssociation = BinaryAssociation(
    name="enum_37",
    ends={
        Property(name="ir_EEnum", type=ir_EFEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFEnum38", type=ir_EEnum, multiplicity=Multiplicity(1, 1))
    }
)
property21: BinaryAssociation = BinaryAssociation(
    name="property21",
    ends={
        Property(name="ir_DerivedProperty22", type=ir_DerivedPropertyRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_DerivedPropertyRef", type=ir_DerivedProperty, multiplicity=Multiplicity(1, 1))
    }
)
feature23: BinaryAssociation = BinaryAssociation(
    name="feature23",
    ends={
        Property(name="ir_EStructuralFeature", type=ir_MetamodelFeatureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_MetamodelFeatureRef", type=ir_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="ir_TypeRef25", type=ir_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableDeclaration", type=ir_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
roots26: BinaryAssociation = BinaryAssociation(
    name="roots26",
    ends={
        Property(name="ir_EFPackage", type=ir_EFMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFMetamodel27", type=ir_EFPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkg28: BinaryAssociation = BinaryAssociation(
    name="pkg28",
    ends={
        Property(name="ir_EPackage", type=ir_EFPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFPackage29", type=ir_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="ir_EFType47", type=ir_MetaTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_MetaTypeRef", type=ir_EFType, multiplicity=Multiplicity(1, 1))
    }
)
containedType48: BinaryAssociation = BinaryAssociation(
    name="containedType48",
    ends={
        Property(name="ir_TypeRef49", type=ir_CollectionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_CollectionTypeRef", type=ir_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literals39: BinaryAssociation = BinaryAssociation(
    name="literals39",
    ends={
        Property(name="ir_EFEnumLiteral", type=ir_EFEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFEnum40", type=ir_EFEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements41: BinaryAssociation = BinaryAssociation(
    name="elements41",
    ends={
        Property(name="ir_TupleTypeElement", type=ir_EFTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_EFTupleType42", type=ir_TupleTypeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="ir_TypeRef45", type=ir_TupleTypeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TupleTypeElement44", type=ir_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source59: BinaryAssociation = BinaryAssociation(
    name="source59",
    ends={
        Property(name="OclExpression60", type=ir_ocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_CallExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments61: BinaryAssociation = BinaryAssociation(
    name="arguments61",
    ends={
        Property(name="OclExpression62", type=ir_ocl_AbstractOperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_AbstractOperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextVariable50: BinaryAssociation = BinaryAssociation(
    name="contextVariable50",
    ends={
        Property(name="ocl_ir_VariableDeclaration", type=ir_ocl_WithContextVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_WithContextVariable", type=ocl_ir_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
klass51: BinaryAssociation = BinaryAssociation(
    name="klass51",
    ends={
        Property(name="ocl_ir_EFClass", type=ir_ocl_OclInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OclInvariant", type=ocl_ir_EFClass, multiplicity=Multiplicity(1, 1))
    }
)
expression52: BinaryAssociation = BinaryAssociation(
    name="expression52",
    ends={
        Property(name="OclExpression", type=ir_ocl_OclInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OclInvariant53", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body54: BinaryAssociation = BinaryAssociation(
    name="body54",
    ends={
        Property(name="OclExpression55", type=ir_ocl_OclDerivedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OclDerivedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body56: BinaryAssociation = BinaryAssociation(
    name="body56",
    ends={
        Property(name="OclExpression57", type=ir_ocl_OclOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OclOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type58: BinaryAssociation = BinaryAssociation(
    name="type58",
    ends={
        Property(name="ocl_ir_TypeRef", type=ir_ocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OclExpression", type=ocl_ir_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition74: BinaryAssociation = BinaryAssociation(
    name="condition74",
    ends={
        Property(name="OclExpression75", type=ir_ocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then76: BinaryAssociation = BinaryAssociation(
    name="then76",
    ends={
        Property(name="OclExpression78", type=ir_ocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_IfExp77", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else79: BinaryAssociation = BinaryAssociation(
    name="else79",
    ends={
        Property(name="OclExpression81", type=ir_ocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_IfExp80", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature63: BinaryAssociation = BinaryAssociation(
    name="feature63",
    ends={
        Property(name="ocl_ir_OperationFeatureRef", type=ir_ocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OperationCallExp", type=ocl_ir_OperationFeatureRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature64: BinaryAssociation = BinaryAssociation(
    name="feature64",
    ends={
        Property(name="ocl_ir_PropertyFeatureRef", type=ir_ocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_PropertyCallExp", type=ocl_ir_PropertyFeatureRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterators65: BinaryAssociation = BinaryAssociation(
    name="iterators65",
    ends={
        Property(name="Iterator", type=ir_ocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_LoopExp", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body66: BinaryAssociation = BinaryAssociation(
    name="body66",
    ends={
        Property(name="OclExpression68", type=ir_ocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_LoopExp67", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result69: BinaryAssociation = BinaryAssociation(
    name="result69",
    ends={
        Property(name="ocl_ir_VariableDeclaration70", type=ir_ocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_IterateExp", type=ocl_ir_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init71: BinaryAssociation = BinaryAssociation(
    name="init71",
    ends={
        Property(name="OclExpression73", type=ir_ocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_IterateExp72", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable92: BinaryAssociation = BinaryAssociation(
    name="variable92",
    ends={
        Property(name="ocl_ir_VariableDeclaration93", type=ir_ocl_VarExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_VarExp", type=ocl_ir_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
variable82: BinaryAssociation = BinaryAssociation(
    name="variable82",
    ends={
        Property(name="ocl_ir_VariableDeclaration83", type=ir_ocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_LetExp", type=ocl_ir_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init84: BinaryAssociation = BinaryAssociation(
    name="init84",
    ends={
        Property(name="OclExpression86", type=ir_ocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_LetExp85", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in87: BinaryAssociation = BinaryAssociation(
    name="in87",
    ends={
        Property(name="OclExpression89", type=ir_ocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_LetExp88", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument90: BinaryAssociation = BinaryAssociation(
    name="argument90",
    ends={
        Property(name="OclExpression91", type=ir_ocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_OperatorCallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts95: BinaryAssociation = BinaryAssociation(
    name="parts95",
    ends={
        Property(name="TuplePart", type=ir_ocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_TupleLiteralExp96", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value97: BinaryAssociation = BinaryAssociation(
    name="value97",
    ends={
        Property(name="OclExpression98", type=ir_ocl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_TuplePart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enum_99: BinaryAssociation = BinaryAssociation(
    name="enum_99",
    ends={
        Property(name="ocl_ir_MetaTypeRef", type=ir_ocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_EnumLiteralExp", type=ocl_ir_MetaTypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal100: BinaryAssociation = BinaryAssociation(
    name="literal100",
    ends={
        Property(name="ocl_ir_EFEnumLiteral", type=ir_ocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_EnumLiteralExp101", type=ocl_ir_EFEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
tupleType94: BinaryAssociation = BinaryAssociation(
    name="tupleType94",
    ends={
        Property(name="ocl_ir_EFTupleType", type=ir_ocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_TupleLiteralExp", type=ocl_ir_EFTupleType, multiplicity=Multiplicity(1, 1))
    }
)
parts102: BinaryAssociation = BinaryAssociation(
    name="parts102",
    ends={
        Property(name="OclExpression103", type=ir_ocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ocl_CollectionLiteralExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ir_OperationFeatureRef_FeatureRef = Generalization(general=FeatureRef, specific=ir_OperationFeatureRef)
gen_ir_BuiltinOperationRef_OperationFeatureRef = Generalization(general=OperationFeatureRef, specific=ir_BuiltinOperationRef)
gen_ir_DefinedOperationRef_OperationFeatureRef = Generalization(general=OperationFeatureRef, specific=ir_DefinedOperationRef)
gen_ir_PropertyFeatureRef_FeatureRef = Generalization(general=FeatureRef, specific=ir_PropertyFeatureRef)
gen_ir_TupleFieldRef_PropertyFeatureRef = Generalization(general=PropertyFeatureRef, specific=ir_TupleFieldRef)
gen_ir_AbstractFunction_TypedElement = Generalization(general=TypedElement, specific=ir_AbstractFunction)
gen_ir_DerivedProperty_AbstractFunction = Generalization(general=AbstractFunction, specific=ir_DerivedProperty)
gen_ir_Operation_AbstractFunction = Generalization(general=AbstractFunction, specific=ir_Operation)
gen_ir_EFClass_EFType = Generalization(general=EFType, specific=ir_EFClass)
gen_ir_EFPrimitiveType_EFType = Generalization(general=EFType, specific=ir_EFPrimitiveType)
gen_ir_EFEnum_EFType = Generalization(general=EFType, specific=ir_EFEnum)
gen_ir_DerivedPropertyRef_PropertyFeatureRef = Generalization(general=PropertyFeatureRef, specific=ir_DerivedPropertyRef)
gen_ir_BuiltinPropertyRef_PropertyFeatureRef = Generalization(general=PropertyFeatureRef, specific=ir_BuiltinPropertyRef)
gen_ir_MetamodelFeatureRef_PropertyFeatureRef = Generalization(general=PropertyFeatureRef, specific=ir_MetamodelFeatureRef)
gen_ir_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ir_Parameter)
gen_ir_InvalidTypeRef_TypeRef = Generalization(general=TypeRef, specific=ir_InvalidTypeRef)
gen_ir_CollectionTypeRef_TypeRef = Generalization(general=TypeRef, specific=ir_CollectionTypeRef)
gen_ir_SetTypeRef_CollectionTypeRef = Generalization(general=CollectionTypeRef, specific=ir_SetTypeRef)
gen_ir_SequenceTypeRef_CollectionTypeRef = Generalization(general=CollectionTypeRef, specific=ir_SequenceTypeRef)
gen_ir_BagTypeRef_CollectionTypeRef = Generalization(general=CollectionTypeRef, specific=ir_BagTypeRef)
gen_ir_OrderedSetTypeRef_CollectionTypeRef = Generalization(general=CollectionTypeRef, specific=ir_OrderedSetTypeRef)
gen_ir_EFTupleType_EFType = Generalization(general=EFType, specific=ir_EFTupleType)
gen_ir_MetaTypeRef_TypeRef = Generalization(general=TypeRef, specific=ir_MetaTypeRef)
gen_ir_ocl_ModelElement_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_ModelElement)
gen_ir_ocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_CallExp)
gen_ir_ocl_AbstractOperationCallExp_CallExp = Generalization(general=CallExp, specific=ir_ocl_AbstractOperationCallExp)
gen_ir_ocl_OperationCallExp_AbstractOperationCallExp = Generalization(general=AbstractOperationCallExp, specific=ir_ocl_OperationCallExp)
gen_ir_ocl_OclInvariant_Constraint = Generalization(general=Constraint, specific=ir_ocl_OclInvariant)
gen_ir_ocl_OclInvariant_ocl_WithContextVariable = Generalization(general=ocl_WithContextVariable, specific=ir_ocl_OclInvariant)
gen_ir_ocl_OclDerivedProperty_DerivedProperty = Generalization(general=DerivedProperty, specific=ir_ocl_OclDerivedProperty)
gen_ir_ocl_OclDerivedProperty_ocl_WithContextVariable = Generalization(general=ocl_WithContextVariable, specific=ir_ocl_OclDerivedProperty)
gen_ir_ocl_OclOperation_Operation = Generalization(general=Operation, specific=ir_ocl_OclOperation)
gen_ir_ocl_OclOperation_ocl_WithContextVariable = Generalization(general=ocl_WithContextVariable, specific=ir_ocl_OclOperation)
gen_ir_ocl_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ir_ocl_Iterator)
gen_ir_ocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_IfExp)
gen_ir_ocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_LetExp)
gen_ir_ocl_PropertyCallExp_CallExp = Generalization(general=CallExp, specific=ir_ocl_PropertyCallExp)
gen_ir_ocl_CollectionCallExp_AbstractOperationCallExp = Generalization(general=AbstractOperationCallExp, specific=ir_ocl_CollectionCallExp)
gen_ir_ocl_LoopExp_CallExp = Generalization(general=CallExp, specific=ir_ocl_LoopExp)
gen_ir_ocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=ir_ocl_IteratorExp)
gen_ir_ocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=ir_ocl_IterateExp)
gen_ir_ocl_VarExp_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_VarExp)
gen_ir_ocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_LiteralExp)
gen_ir_ocl_OperatorCallExp_CallExp = Generalization(general=CallExp, specific=ir_ocl_OperatorCallExp)
gen_ir_ocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_EnumLiteralExp)
gen_ir_ocl_BooleanLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_BooleanLiteralExp)
gen_ir_ocl_StringLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_StringLiteralExp)
gen_ir_ocl_IntegerLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_IntegerLiteralExp)
gen_ir_ocl_RealLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_RealLiteralExp)
gen_ir_ocl_OclUndefined_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_OclUndefined)
gen_ir_ocl_OclInvalid_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_OclInvalid)
gen_ir_ocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_TupleLiteralExp)
gen_ir_ocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ir_ocl_CollectionLiteralExp)
gen_ir_ocl_SetLiteralExp_CollectionLiteralExp = Generalization(general=CollectionLiteralExp, specific=ir_ocl_SetLiteralExp)
gen_ir_ocl_OrderedSetLiteralExp_CollectionLiteralExp = Generalization(general=CollectionLiteralExp, specific=ir_ocl_OrderedSetLiteralExp)
gen_ir_ocl_SequenceLiteralExp_CollectionLiteralExp = Generalization(general=CollectionLiteralExp, specific=ir_ocl_SequenceLiteralExp)
gen_ir_ocl_BagLiteralExp_CollectionLiteralExp = Generalization(general=CollectionLiteralExp, specific=ir_ocl_BagLiteralExp)
gen_ir_ocl_UnsupportedExp_OclExpression = Generalization(general=OclExpression, specific=ir_ocl_UnsupportedExp)

# Domain Model
domain_model = DomainModel(
    name="ir",
    types={ir_EFMetamodel, ir_Constraint, ir_EFClass, ir_DerivedProperty, ir_Operation, ir_Specification, ir_FeatureRef, ir_OperationFeatureRef, FeatureRef, ir_BuiltinOperationRef, OperationFeatureRef, ir_DefinedOperationRef, ir_PropertyFeatureRef, ir_TupleFieldRef, PropertyFeatureRef, ir_EFPrimitiveType, ir_EFTupleType, ir_TypedElement, ir_TypeRef, ir_AbstractFunction, TypedElement, ir_EFType, AbstractFunction, ir_Parameter, ir_EFEnum, EFType, ir_EClass, ir_EEnum, ir_DerivedPropertyRef, ir_BuiltinPropertyRef, ir_MetamodelFeatureRef, ir_EStructuralFeature, ir_VariableDeclaration, VariableDeclaration, ir_EFPackage, ir_EPackage, ir_InvalidTypeRef, ir_CollectionTypeRef, ir_SetTypeRef, CollectionTypeRef, ir_SequenceTypeRef, ir_BagTypeRef, ir_OrderedSetTypeRef, ir_EFEnumLiteral, ir_TupleTypeElement, ir_MetaTypeRef, TypeRef, ir_ocl_ModelElement, ir_ocl_CallExp, ir_ocl_AbstractOperationCallExp, CallExp, ir_ocl_OperationCallExp, AbstractOperationCallExp, ocl_ir_OperationFeatureRef, ir_ocl_WithContextVariable, ocl_ir_VariableDeclaration, ir_ocl_OclInvariant, Constraint, ocl_WithContextVariable, ocl_ir_EFClass, OclExpression, ir_ocl_OclDerivedProperty, DerivedProperty, ir_ocl_OclOperation, Operation, ir_ocl_OclExpression, ocl_ir_TypeRef, ir_ocl_Iterator, ir_ocl_IfExp, ir_ocl_LetExp, ir_ocl_PropertyCallExp, ocl_ir_PropertyFeatureRef, ir_ocl_CollectionCallExp, ir_ocl_LoopExp, Iterator, ir_ocl_IteratorExp, LoopExp, ir_ocl_IterateExp, ir_ocl_VarExp, ir_ocl_LiteralExp, ir_ocl_OperatorCallExp, TuplePart, ir_ocl_TuplePart, ir_ocl_EnumLiteralExp, ocl_ir_MetaTypeRef, ocl_ir_EFEnumLiteral, ir_ocl_BooleanLiteralExp, LiteralExp, ir_ocl_StringLiteralExp, ir_ocl_IntegerLiteralExp, ir_ocl_RealLiteralExp, ir_ocl_OclUndefined, ir_ocl_OclInvalid, ir_ocl_TupleLiteralExp, ocl_ir_EFTupleType, ir_ocl_CollectionLiteralExp, ir_ocl_SetLiteralExp, CollectionLiteralExp, ir_ocl_OrderedSetLiteralExp, ir_ocl_SequenceLiteralExp, ir_ocl_BagLiteralExp, ir_ocl_UnsupportedExp, ir_ocl_OclAnyLibElement, OperatorKind},
    associations={metamodels0, constaints1, temporary3, properties5, operation17, type19, operations7, primitiveTypes9, tupleTypes11, type13, context14, parameters15, classes30, enumerations33, klass35, enum_37, property21, feature23, type24, roots26, pkg28, type46, containedType48, literals39, elements41, type43, source59, arguments61, contextVariable50, klass51, expression52, body54, body56, type58, condition74, then76, else79, feature63, feature64, iterators65, body66, result69, init71, variable92, variable82, init84, in87, argument90, parts95, value97, enum_99, literal100, tupleType94, parts102},
    generalizations={gen_ir_OperationFeatureRef_FeatureRef, gen_ir_BuiltinOperationRef_OperationFeatureRef, gen_ir_DefinedOperationRef_OperationFeatureRef, gen_ir_PropertyFeatureRef_FeatureRef, gen_ir_TupleFieldRef_PropertyFeatureRef, gen_ir_AbstractFunction_TypedElement, gen_ir_DerivedProperty_AbstractFunction, gen_ir_Operation_AbstractFunction, gen_ir_EFClass_EFType, gen_ir_EFPrimitiveType_EFType, gen_ir_EFEnum_EFType, gen_ir_DerivedPropertyRef_PropertyFeatureRef, gen_ir_BuiltinPropertyRef_PropertyFeatureRef, gen_ir_MetamodelFeatureRef_PropertyFeatureRef, gen_ir_Parameter_VariableDeclaration, gen_ir_InvalidTypeRef_TypeRef, gen_ir_CollectionTypeRef_TypeRef, gen_ir_SetTypeRef_CollectionTypeRef, gen_ir_SequenceTypeRef_CollectionTypeRef, gen_ir_BagTypeRef_CollectionTypeRef, gen_ir_OrderedSetTypeRef_CollectionTypeRef, gen_ir_EFTupleType_EFType, gen_ir_MetaTypeRef_TypeRef, gen_ir_ocl_ModelElement_OclExpression, gen_ir_ocl_CallExp_OclExpression, gen_ir_ocl_AbstractOperationCallExp_CallExp, gen_ir_ocl_OperationCallExp_AbstractOperationCallExp, gen_ir_ocl_OclInvariant_Constraint, gen_ir_ocl_OclInvariant_ocl_WithContextVariable, gen_ir_ocl_OclDerivedProperty_DerivedProperty, gen_ir_ocl_OclDerivedProperty_ocl_WithContextVariable, gen_ir_ocl_OclOperation_Operation, gen_ir_ocl_OclOperation_ocl_WithContextVariable, gen_ir_ocl_Iterator_VariableDeclaration, gen_ir_ocl_IfExp_OclExpression, gen_ir_ocl_LetExp_OclExpression, gen_ir_ocl_PropertyCallExp_CallExp, gen_ir_ocl_CollectionCallExp_AbstractOperationCallExp, gen_ir_ocl_LoopExp_CallExp, gen_ir_ocl_IteratorExp_LoopExp, gen_ir_ocl_IterateExp_LoopExp, gen_ir_ocl_VarExp_OclExpression, gen_ir_ocl_LiteralExp_OclExpression, gen_ir_ocl_OperatorCallExp_CallExp, gen_ir_ocl_EnumLiteralExp_LiteralExp, gen_ir_ocl_BooleanLiteralExp_LiteralExp, gen_ir_ocl_StringLiteralExp_LiteralExp, gen_ir_ocl_IntegerLiteralExp_LiteralExp, gen_ir_ocl_RealLiteralExp_LiteralExp, gen_ir_ocl_OclUndefined_LiteralExp, gen_ir_ocl_OclInvalid_LiteralExp, gen_ir_ocl_TupleLiteralExp_LiteralExp, gen_ir_ocl_CollectionLiteralExp_LiteralExp, gen_ir_ocl_SetLiteralExp_CollectionLiteralExp, gen_ir_ocl_OrderedSetLiteralExp_CollectionLiteralExp, gen_ir_ocl_SequenceLiteralExp_CollectionLiteralExp, gen_ir_ocl_BagLiteralExp_CollectionLiteralExp, gen_ir_ocl_UnsupportedExp_OclExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)