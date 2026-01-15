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

# Classes
backtrackingContentAssistTest_Document = Class(name="backtrackingContentAssistTest::Document")
backtrackingContentAssistTest_PackageDeclaration = Class(name="backtrackingContentAssistTest::PackageDeclaration")
backtrackingContentAssistTest_ClassifierContextDecl = Class(name="backtrackingContentAssistTest::ClassifierContextDecl")
ContextDecl = Class(name="ContextDecl")
backtrackingContentAssistTest_ClassifierRef = Class(name="backtrackingContentAssistTest::ClassifierRef")
backtrackingContentAssistTest_Invariant = Class(name="backtrackingContentAssistTest::Invariant")
backtrackingContentAssistTest_ContextDecl = Class(name="backtrackingContentAssistTest::ContextDecl")
backtrackingContentAssistTest_Body = Class(name="backtrackingContentAssistTest::Body")
backtrackingContentAssistTest_Expression = Class(name="backtrackingContentAssistTest::Expression")
backtrackingContentAssistTest_Parameter = Class(name="backtrackingContentAssistTest::Parameter")
backtrackingContentAssistTest_TypeExp = Class(name="backtrackingContentAssistTest::TypeExp")
backtrackingContentAssistTest_Definition = Class(name="backtrackingContentAssistTest::Definition")
backtrackingContentAssistTest_OperationRef = Class(name="backtrackingContentAssistTest::OperationRef")
backtrackingContentAssistTest_Der = Class(name="backtrackingContentAssistTest::Der")
backtrackingContentAssistTest_Init = Class(name="backtrackingContentAssistTest::Init")
backtrackingContentAssistTest_OperationContextDecl = Class(name="backtrackingContentAssistTest::OperationContextDecl")
backtrackingContentAssistTest_PackageRef = Class(name="backtrackingContentAssistTest::PackageRef")
backtrackingContentAssistTest_Pre = Class(name="backtrackingContentAssistTest::Pre")
backtrackingContentAssistTest_Post = Class(name="backtrackingContentAssistTest::Post")
backtrackingContentAssistTest_QualifiedClassifierRef = Class(name="backtrackingContentAssistTest::QualifiedClassifierRef")
ClassifierRef = Class(name="ClassifierRef")
backtrackingContentAssistTest_QualifiedOperationRef = Class(name="backtrackingContentAssistTest::QualifiedOperationRef")
OperationRef = Class(name="OperationRef")
backtrackingContentAssistTest_PropertyContextDecl = Class(name="backtrackingContentAssistTest::PropertyContextDecl")
backtrackingContentAssistTest_PropertyRef = Class(name="backtrackingContentAssistTest::PropertyRef")
backtrackingContentAssistTest_SimplePackageRef = Class(name="backtrackingContentAssistTest::SimplePackageRef")
backtrackingContentAssistTest_SimplePropertyRef = Class(name="backtrackingContentAssistTest::SimplePropertyRef")
NavigatingExp = Class(name="NavigatingExp")
OclMessageArg = Class(name="OclMessageArg")
backtrackingContentAssistTest_NavigatingExp = Class(name="backtrackingContentAssistTest::NavigatingExp")
backtrackingContentAssistTest_OclMessageArg = Class(name="backtrackingContentAssistTest::OclMessageArg")
backtrackingContentAssistTest_QualifiedPropertyRef = Class(name="backtrackingContentAssistTest::QualifiedPropertyRef")
PropertyRef = Class(name="PropertyRef")
backtrackingContentAssistTest_QualifiedPackageRef = Class(name="backtrackingContentAssistTest::QualifiedPackageRef")
PackageRef = Class(name="PackageRef")
backtrackingContentAssistTest_SimpleClassifierRef = Class(name="backtrackingContentAssistTest::SimpleClassifierRef")
backtrackingContentAssistTest_SimpleOperationRef = Class(name="backtrackingContentAssistTest::SimpleOperationRef")
backtrackingContentAssistTest_CollectionLiteralExp = Class(name="backtrackingContentAssistTest::CollectionLiteralExp")
backtrackingContentAssistTest_CollectionLiteralPart = Class(name="backtrackingContentAssistTest::CollectionLiteralPart")
backtrackingContentAssistTest_PrimitiveType = Class(name="backtrackingContentAssistTest::PrimitiveType")
TypeExp = Class(name="TypeExp")
Expression = Class(name="Expression")
backtrackingContentAssistTest_CollectionType = Class(name="backtrackingContentAssistTest::CollectionType")
CollectionLiteralExp = Class(name="CollectionLiteralExp")
backtrackingContentAssistTest_TupleType = Class(name="backtrackingContentAssistTest::TupleType")
backtrackingContentAssistTest_tuplePart = Class(name="backtrackingContentAssistTest::tuplePart")
backtrackingContentAssistTest_TupleLiteralPart = Class(name="backtrackingContentAssistTest::TupleLiteralPart")
backtrackingContentAssistTest_PrimitiveLiteralExp = Class(name="backtrackingContentAssistTest::PrimitiveLiteralExp")
backtrackingContentAssistTest_TupleLiteralExp = Class(name="backtrackingContentAssistTest::TupleLiteralExp")
backtrackingContentAssistTest_InvalidLiteralExp = Class(name="backtrackingContentAssistTest::InvalidLiteralExp")
backtrackingContentAssistTest_NullLiteralExp = Class(name="backtrackingContentAssistTest::NullLiteralExp")
backtrackingContentAssistTest_iteratorVariable = Class(name="backtrackingContentAssistTest::iteratorVariable")
backtrackingContentAssistTest_NumberLiteralExp = Class(name="backtrackingContentAssistTest::NumberLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
backtrackingContentAssistTest_StringLiteralExp = Class(name="backtrackingContentAssistTest::StringLiteralExp")
backtrackingContentAssistTest_BooleanLiteralExp = Class(name="backtrackingContentAssistTest::BooleanLiteralExp")
backtrackingContentAssistTest_EObject = Class(name="backtrackingContentAssistTest::EObject")
backtrackingContentAssistTest_iteratorAccumulator = Class(name="backtrackingContentAssistTest::iteratorAccumulator")
backtrackingContentAssistTest_RoundBracketExp = Class(name="backtrackingContentAssistTest::RoundBracketExp")
backtrackingContentAssistTest_NameExp = Class(name="backtrackingContentAssistTest::NameExp")
backtrackingContentAssistTest_SelfExp = Class(name="backtrackingContentAssistTest::SelfExp")
backtrackingContentAssistTest_PathNameExp = Class(name="backtrackingContentAssistTest::PathNameExp")
NameExp = Class(name="NameExp")
backtrackingContentAssistTest_SquareBracketExp = Class(name="backtrackingContentAssistTest::SquareBracketExp")
backtrackingContentAssistTest_PreExp = Class(name="backtrackingContentAssistTest::PreExp")
backtrackingContentAssistTest_LetExp = Class(name="backtrackingContentAssistTest::LetExp")
backtrackingContentAssistTest_LetVariable = Class(name="backtrackingContentAssistTest::LetVariable")
backtrackingContentAssistTest_SimpleNameExp = Class(name="backtrackingContentAssistTest::SimpleNameExp")
backtrackingContentAssistTest_IfExp = Class(name="backtrackingContentAssistTest::IfExp")
backtrackingContentAssistTest_OclMessage = Class(name="backtrackingContentAssistTest::OclMessage")
backtrackingContentAssistTest_InfixExp = Class(name="backtrackingContentAssistTest::InfixExp")
backtrackingContentAssistTest_NestedExp = Class(name="backtrackingContentAssistTest::NestedExp")
backtrackingContentAssistTest_PrefixExp = Class(name="backtrackingContentAssistTest::PrefixExp")

# backtrackingContentAssistTest_Document class attributes and methods

# backtrackingContentAssistTest_PackageDeclaration class attributes and methods

# backtrackingContentAssistTest_ClassifierContextDecl class attributes and methods
backtrackingContentAssistTest_ClassifierContextDecl_selfName: Property = Property(name="selfName", type=StringType)
backtrackingContentAssistTest_ClassifierContextDecl.attributes={backtrackingContentAssistTest_ClassifierContextDecl_selfName}

# ContextDecl class attributes and methods

# backtrackingContentAssistTest_ClassifierRef class attributes and methods

# backtrackingContentAssistTest_Invariant class attributes and methods
backtrackingContentAssistTest_Invariant_constraintName: Property = Property(name="constraintName", type=StringType)
backtrackingContentAssistTest_Invariant.attributes={backtrackingContentAssistTest_Invariant_constraintName}

# backtrackingContentAssistTest_ContextDecl class attributes and methods

# backtrackingContentAssistTest_Body class attributes and methods
backtrackingContentAssistTest_Body_constraintName: Property = Property(name="constraintName", type=StringType)
backtrackingContentAssistTest_Body.attributes={backtrackingContentAssistTest_Body_constraintName}

# backtrackingContentAssistTest_Expression class attributes and methods

# backtrackingContentAssistTest_Parameter class attributes and methods
backtrackingContentAssistTest_Parameter_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_Parameter.attributes={backtrackingContentAssistTest_Parameter_name}

# backtrackingContentAssistTest_TypeExp class attributes and methods

# backtrackingContentAssistTest_Definition class attributes and methods
backtrackingContentAssistTest_Definition_static: Property = Property(name="static", type=BooleanType)
backtrackingContentAssistTest_Definition_constraintName: Property = Property(name="constraintName", type=StringType)
backtrackingContentAssistTest_Definition_constrainedName: Property = Property(name="constrainedName", type=StringType)
backtrackingContentAssistTest_Definition.attributes={backtrackingContentAssistTest_Definition_static, backtrackingContentAssistTest_Definition_constraintName, backtrackingContentAssistTest_Definition_constrainedName}

# backtrackingContentAssistTest_OperationRef class attributes and methods

# backtrackingContentAssistTest_Der class attributes and methods

# backtrackingContentAssistTest_Init class attributes and methods

# backtrackingContentAssistTest_OperationContextDecl class attributes and methods

# backtrackingContentAssistTest_PackageRef class attributes and methods

# backtrackingContentAssistTest_Pre class attributes and methods
backtrackingContentAssistTest_Pre_constraintName: Property = Property(name="constraintName", type=StringType)
backtrackingContentAssistTest_Pre.attributes={backtrackingContentAssistTest_Pre_constraintName}

# backtrackingContentAssistTest_Post class attributes and methods
backtrackingContentAssistTest_Post_constraintName: Property = Property(name="constraintName", type=StringType)
backtrackingContentAssistTest_Post.attributes={backtrackingContentAssistTest_Post_constraintName}

# backtrackingContentAssistTest_QualifiedClassifierRef class attributes and methods
backtrackingContentAssistTest_QualifiedClassifierRef_namespace: Property = Property(name="namespace", type=StringType)
backtrackingContentAssistTest_QualifiedClassifierRef.attributes={backtrackingContentAssistTest_QualifiedClassifierRef_namespace}

# ClassifierRef class attributes and methods

# backtrackingContentAssistTest_QualifiedOperationRef class attributes and methods
backtrackingContentAssistTest_QualifiedOperationRef_namespace: Property = Property(name="namespace", type=StringType)
backtrackingContentAssistTest_QualifiedOperationRef.attributes={backtrackingContentAssistTest_QualifiedOperationRef_namespace}

# OperationRef class attributes and methods

# backtrackingContentAssistTest_PropertyContextDecl class attributes and methods

# backtrackingContentAssistTest_PropertyRef class attributes and methods

# backtrackingContentAssistTest_SimplePackageRef class attributes and methods
backtrackingContentAssistTest_SimplePackageRef_package: Property = Property(name="package", type=StringType)
backtrackingContentAssistTest_SimplePackageRef.attributes={backtrackingContentAssistTest_SimplePackageRef_package}

# backtrackingContentAssistTest_SimplePropertyRef class attributes and methods
backtrackingContentAssistTest_SimplePropertyRef_feature: Property = Property(name="feature", type=StringType)
backtrackingContentAssistTest_SimplePropertyRef.attributes={backtrackingContentAssistTest_SimplePropertyRef_feature}

# NavigatingExp class attributes and methods

# OclMessageArg class attributes and methods

# backtrackingContentAssistTest_NavigatingExp class attributes and methods

# backtrackingContentAssistTest_OclMessageArg class attributes and methods

# backtrackingContentAssistTest_QualifiedPropertyRef class attributes and methods
backtrackingContentAssistTest_QualifiedPropertyRef_namespace: Property = Property(name="namespace", type=StringType)
backtrackingContentAssistTest_QualifiedPropertyRef.attributes={backtrackingContentAssistTest_QualifiedPropertyRef_namespace}

# PropertyRef class attributes and methods

# backtrackingContentAssistTest_QualifiedPackageRef class attributes and methods
backtrackingContentAssistTest_QualifiedPackageRef_namespace: Property = Property(name="namespace", type=StringType)
backtrackingContentAssistTest_QualifiedPackageRef.attributes={backtrackingContentAssistTest_QualifiedPackageRef_namespace}

# PackageRef class attributes and methods

# backtrackingContentAssistTest_SimpleClassifierRef class attributes and methods
backtrackingContentAssistTest_SimpleClassifierRef_classifier: Property = Property(name="classifier", type=StringType)
backtrackingContentAssistTest_SimpleClassifierRef.attributes={backtrackingContentAssistTest_SimpleClassifierRef_classifier}

# backtrackingContentAssistTest_SimpleOperationRef class attributes and methods
backtrackingContentAssistTest_SimpleOperationRef_operation: Property = Property(name="operation", type=StringType)
backtrackingContentAssistTest_SimpleOperationRef.attributes={backtrackingContentAssistTest_SimpleOperationRef_operation}

# backtrackingContentAssistTest_CollectionLiteralExp class attributes and methods

# backtrackingContentAssistTest_CollectionLiteralPart class attributes and methods

# backtrackingContentAssistTest_PrimitiveType class attributes and methods
backtrackingContentAssistTest_PrimitiveType_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_PrimitiveType.attributes={backtrackingContentAssistTest_PrimitiveType_name}

# TypeExp class attributes and methods

# Expression class attributes and methods

# backtrackingContentAssistTest_CollectionType class attributes and methods
backtrackingContentAssistTest_CollectionType_typeIdentifier: Property = Property(name="typeIdentifier", type=StringType)
backtrackingContentAssistTest_CollectionType.attributes={backtrackingContentAssistTest_CollectionType_typeIdentifier}

# CollectionLiteralExp class attributes and methods

# backtrackingContentAssistTest_TupleType class attributes and methods
backtrackingContentAssistTest_TupleType_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_TupleType.attributes={backtrackingContentAssistTest_TupleType_name}

# backtrackingContentAssistTest_tuplePart class attributes and methods
backtrackingContentAssistTest_tuplePart_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_tuplePart.attributes={backtrackingContentAssistTest_tuplePart_name}

# backtrackingContentAssistTest_TupleLiteralPart class attributes and methods
backtrackingContentAssistTest_TupleLiteralPart_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_TupleLiteralPart.attributes={backtrackingContentAssistTest_TupleLiteralPart_name}

# backtrackingContentAssistTest_PrimitiveLiteralExp class attributes and methods

# backtrackingContentAssistTest_TupleLiteralExp class attributes and methods

# backtrackingContentAssistTest_InvalidLiteralExp class attributes and methods

# backtrackingContentAssistTest_NullLiteralExp class attributes and methods

# backtrackingContentAssistTest_iteratorVariable class attributes and methods
backtrackingContentAssistTest_iteratorVariable_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_iteratorVariable.attributes={backtrackingContentAssistTest_iteratorVariable_name}

# backtrackingContentAssistTest_NumberLiteralExp class attributes and methods
backtrackingContentAssistTest_NumberLiteralExp_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_NumberLiteralExp.attributes={backtrackingContentAssistTest_NumberLiteralExp_name}

# PrimitiveLiteralExp class attributes and methods

# backtrackingContentAssistTest_StringLiteralExp class attributes and methods
backtrackingContentAssistTest_StringLiteralExp_values: Property = Property(name="values", type=StringType)
backtrackingContentAssistTest_StringLiteralExp.attributes={backtrackingContentAssistTest_StringLiteralExp_values}

# backtrackingContentAssistTest_BooleanLiteralExp class attributes and methods
backtrackingContentAssistTest_BooleanLiteralExp_isTrue: Property = Property(name="isTrue", type=BooleanType)
backtrackingContentAssistTest_BooleanLiteralExp.attributes={backtrackingContentAssistTest_BooleanLiteralExp_isTrue}

# backtrackingContentAssistTest_EObject class attributes and methods

# backtrackingContentAssistTest_iteratorAccumulator class attributes and methods
backtrackingContentAssistTest_iteratorAccumulator_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_iteratorAccumulator.attributes={backtrackingContentAssistTest_iteratorAccumulator_name}

# backtrackingContentAssistTest_RoundBracketExp class attributes and methods
backtrackingContentAssistTest_RoundBracketExp_pre: Property = Property(name="pre", type=BooleanType)
backtrackingContentAssistTest_RoundBracketExp.attributes={backtrackingContentAssistTest_RoundBracketExp_pre}

# backtrackingContentAssistTest_NameExp class attributes and methods

# backtrackingContentAssistTest_SelfExp class attributes and methods

# backtrackingContentAssistTest_PathNameExp class attributes and methods
backtrackingContentAssistTest_PathNameExp_namespace: Property = Property(name="namespace", type=StringType)
backtrackingContentAssistTest_PathNameExp.attributes={backtrackingContentAssistTest_PathNameExp_namespace}

# NameExp class attributes and methods

# backtrackingContentAssistTest_SquareBracketExp class attributes and methods
backtrackingContentAssistTest_SquareBracketExp_pre: Property = Property(name="pre", type=BooleanType)
backtrackingContentAssistTest_SquareBracketExp.attributes={backtrackingContentAssistTest_SquareBracketExp_pre}

# backtrackingContentAssistTest_PreExp class attributes and methods

# backtrackingContentAssistTest_LetExp class attributes and methods

# backtrackingContentAssistTest_LetVariable class attributes and methods
backtrackingContentAssistTest_LetVariable_name: Property = Property(name="name", type=StringType)
backtrackingContentAssistTest_LetVariable.attributes={backtrackingContentAssistTest_LetVariable_name}

# backtrackingContentAssistTest_SimpleNameExp class attributes and methods
backtrackingContentAssistTest_SimpleNameExp_element: Property = Property(name="element", type=StringType)
backtrackingContentAssistTest_SimpleNameExp.attributes={backtrackingContentAssistTest_SimpleNameExp_element}

# backtrackingContentAssistTest_IfExp class attributes and methods

# backtrackingContentAssistTest_OclMessage class attributes and methods
backtrackingContentAssistTest_OclMessage_op: Property = Property(name="op", type=StringType)
backtrackingContentAssistTest_OclMessage_messageName: Property = Property(name="messageName", type=StringType)
backtrackingContentAssistTest_OclMessage.attributes={backtrackingContentAssistTest_OclMessage_op, backtrackingContentAssistTest_OclMessage_messageName}

# backtrackingContentAssistTest_InfixExp class attributes and methods
backtrackingContentAssistTest_InfixExp_op: Property = Property(name="op", type=StringType)
backtrackingContentAssistTest_InfixExp.attributes={backtrackingContentAssistTest_InfixExp_op}

# backtrackingContentAssistTest_NestedExp class attributes and methods

# backtrackingContentAssistTest_PrefixExp class attributes and methods
backtrackingContentAssistTest_PrefixExp_op: Property = Property(name="op", type=StringType)
backtrackingContentAssistTest_PrefixExp.attributes={backtrackingContentAssistTest_PrefixExp_op}

# Relationships
classifier4: BinaryAssociation = BinaryAssociation(
    name="classifier4",
    ends={
        Property(name="backtrackingContentAssistTest_ClassifierRef", type=backtrackingContentAssistTest_ClassifierContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_ClassifierContextDecl", type=backtrackingContentAssistTest_ClassifierRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariants5: BinaryAssociation = BinaryAssociation(
    name="invariants5",
    ends={
        Property(name="backtrackingContentAssistTest_Invariant", type=backtrackingContentAssistTest_ClassifierContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_ClassifierContextDecl6", type=backtrackingContentAssistTest_Invariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="backtrackingContentAssistTest_PackageDeclaration", type=backtrackingContentAssistTest_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Document", type=backtrackingContentAssistTest_PackageDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contexts1: BinaryAssociation = BinaryAssociation(
    name="contexts1",
    ends={
        Property(name="backtrackingContentAssistTest_ContextDecl", type=backtrackingContentAssistTest_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Document2", type=backtrackingContentAssistTest_ContextDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression3: BinaryAssociation = BinaryAssociation(
    name="expression3",
    ends={
        Property(name="backtrackingContentAssistTest_Expression", type=backtrackingContentAssistTest_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Body", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="backtrackingContentAssistTest_Parameter", type=backtrackingContentAssistTest_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Definition10", type=backtrackingContentAssistTest_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp", type=backtrackingContentAssistTest_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Definition12", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="backtrackingContentAssistTest_Expression15", type=backtrackingContentAssistTest_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Definition14", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions7: BinaryAssociation = BinaryAssociation(
    name="definitions7",
    ends={
        Property(name="backtrackingContentAssistTest_Definition", type=backtrackingContentAssistTest_ClassifierContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_ClassifierContextDecl8", type=backtrackingContentAssistTest_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation23: BinaryAssociation = BinaryAssociation(
    name="operation23",
    ends={
        Property(name="backtrackingContentAssistTest_OperationRef", type=backtrackingContentAssistTest_OperationContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OperationContextDecl", type=backtrackingContentAssistTest_OperationRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="backtrackingContentAssistTest_Parameter26", type=backtrackingContentAssistTest_OperationContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OperationContextDecl25", type=backtrackingContentAssistTest_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp29", type=backtrackingContentAssistTest_OperationContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OperationContextDecl28", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="backtrackingContentAssistTest_Expression17", type=backtrackingContentAssistTest_Der, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Der", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression18: BinaryAssociation = BinaryAssociation(
    name="expression18",
    ends={
        Property(name="backtrackingContentAssistTest_Expression19", type=backtrackingContentAssistTest_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Init", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="backtrackingContentAssistTest_Expression22", type=backtrackingContentAssistTest_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Invariant21", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package37: BinaryAssociation = BinaryAssociation(
    name="package37",
    ends={
        Property(name="backtrackingContentAssistTest_PackageRef", type=backtrackingContentAssistTest_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PackageDeclaration38", type=backtrackingContentAssistTest_PackageRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contexts39: BinaryAssociation = BinaryAssociation(
    name="contexts39",
    ends={
        Property(name="backtrackingContentAssistTest_ContextDecl41", type=backtrackingContentAssistTest_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PackageDeclaration40", type=backtrackingContentAssistTest_ContextDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp44", type=backtrackingContentAssistTest_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Parameter43", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pres30: BinaryAssociation = BinaryAssociation(
    name="pres30",
    ends={
        Property(name="backtrackingContentAssistTest_Pre", type=backtrackingContentAssistTest_OperationContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OperationContextDecl31", type=backtrackingContentAssistTest_Pre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
posts32: BinaryAssociation = BinaryAssociation(
    name="posts32",
    ends={
        Property(name="backtrackingContentAssistTest_Post", type=backtrackingContentAssistTest_OperationContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OperationContextDecl33", type=backtrackingContentAssistTest_Post, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodies34: BinaryAssociation = BinaryAssociation(
    name="bodies34",
    ends={
        Property(name="backtrackingContentAssistTest_Body36", type=backtrackingContentAssistTest_OperationContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OperationContextDecl35", type=backtrackingContentAssistTest_Body, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
der58: BinaryAssociation = BinaryAssociation(
    name="der58",
    ends={
        Property(name="backtrackingContentAssistTest_PropertyContextDecl59", type=backtrackingContentAssistTest_Der, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="backtrackingContentAssistTest_Der60", type=backtrackingContentAssistTest_PropertyContextDecl, multiplicity=Multiplicity(1, 1))
    }
)
element61: BinaryAssociation = BinaryAssociation(
    name="element61",
    ends={
        Property(name="backtrackingContentAssistTest_ClassifierRef62", type=backtrackingContentAssistTest_QualifiedClassifierRef, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_QualifiedClassifierRef", type=backtrackingContentAssistTest_ClassifierRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression45: BinaryAssociation = BinaryAssociation(
    name="expression45",
    ends={
        Property(name="backtrackingContentAssistTest_Expression47", type=backtrackingContentAssistTest_Post, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Post46", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="backtrackingContentAssistTest_Expression50", type=backtrackingContentAssistTest_Pre, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_Pre49", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property51: BinaryAssociation = BinaryAssociation(
    name="property51",
    ends={
        Property(name="backtrackingContentAssistTest_PropertyRef", type=backtrackingContentAssistTest_PropertyContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PropertyContextDecl", type=backtrackingContentAssistTest_PropertyRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp54", type=backtrackingContentAssistTest_PropertyContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PropertyContextDecl53", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init55: BinaryAssociation = BinaryAssociation(
    name="init55",
    ends={
        Property(name="backtrackingContentAssistTest_Init57", type=backtrackingContentAssistTest_PropertyContextDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PropertyContextDecl56", type=backtrackingContentAssistTest_Init, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element63: BinaryAssociation = BinaryAssociation(
    name="element63",
    ends={
        Property(name="backtrackingContentAssistTest_OperationRef64", type=backtrackingContentAssistTest_QualifiedOperationRef, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_QualifiedOperationRef", type=backtrackingContentAssistTest_OperationRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type69: BinaryAssociation = BinaryAssociation(
    name="type69",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp70", type=backtrackingContentAssistTest_OclMessageArg, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OclMessageArg", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element65: BinaryAssociation = BinaryAssociation(
    name="element65",
    ends={
        Property(name="backtrackingContentAssistTest_PropertyRef66", type=backtrackingContentAssistTest_QualifiedPropertyRef, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_QualifiedPropertyRef", type=backtrackingContentAssistTest_PropertyRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element67: BinaryAssociation = BinaryAssociation(
    name="element67",
    ends={
        Property(name="backtrackingContentAssistTest_PackageRef68", type=backtrackingContentAssistTest_QualifiedPackageRef, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_QualifiedPackageRef", type=backtrackingContentAssistTest_PackageRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part71: BinaryAssociation = BinaryAssociation(
    name="part71",
    ends={
        Property(name="backtrackingContentAssistTest_tuplePart", type=backtrackingContentAssistTest_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_TupleType", type=backtrackingContentAssistTest_tuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type72: BinaryAssociation = BinaryAssociation(
    name="type72",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp74", type=backtrackingContentAssistTest_tuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_tuplePart73", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part82: BinaryAssociation = BinaryAssociation(
    name="part82",
    ends={
        Property(name="backtrackingContentAssistTest_TupleLiteralPart", type=backtrackingContentAssistTest_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_TupleLiteralExp", type=backtrackingContentAssistTest_TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp85", type=backtrackingContentAssistTest_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_TupleLiteralPart84", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionLiteralParts75: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts75",
    ends={
        Property(name="backtrackingContentAssistTest_CollectionLiteralPart", type=backtrackingContentAssistTest_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_CollectionLiteralExp", type=backtrackingContentAssistTest_CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression76: BinaryAssociation = BinaryAssociation(
    name="expression76",
    ends={
        Property(name="backtrackingContentAssistTest_Expression78", type=backtrackingContentAssistTest_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_CollectionLiteralPart77", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastExpression79: BinaryAssociation = BinaryAssociation(
    name="lastExpression79",
    ends={
        Property(name="backtrackingContentAssistTest_Expression81", type=backtrackingContentAssistTest_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_CollectionLiteralPart80", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type89: BinaryAssociation = BinaryAssociation(
    name="type89",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp90", type=backtrackingContentAssistTest_iteratorVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_iteratorVariable", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression86: BinaryAssociation = BinaryAssociation(
    name="initExpression86",
    ends={
        Property(name="backtrackingContentAssistTest_Expression88", type=backtrackingContentAssistTest_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_TupleLiteralPart87", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable197: BinaryAssociation = BinaryAssociation(
    name="variable197",
    ends={
        Property(name="backtrackingContentAssistTest_iteratorVariable99", type=backtrackingContentAssistTest_RoundBracketExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_RoundBracketExp98", type=backtrackingContentAssistTest_iteratorVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable2100: BinaryAssociation = BinaryAssociation(
    name="variable2100",
    ends={
        Property(name="backtrackingContentAssistTest_EObject", type=backtrackingContentAssistTest_RoundBracketExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_RoundBracketExp101", type=backtrackingContentAssistTest_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments102: BinaryAssociation = BinaryAssociation(
    name="arguments102",
    ends={
        Property(name="backtrackingContentAssistTest_Expression104", type=backtrackingContentAssistTest_RoundBracketExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_RoundBracketExp103", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type91: BinaryAssociation = BinaryAssociation(
    name="type91",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp92", type=backtrackingContentAssistTest_iteratorAccumulator, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_iteratorAccumulator", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression93: BinaryAssociation = BinaryAssociation(
    name="initExpression93",
    ends={
        Property(name="backtrackingContentAssistTest_Expression95", type=backtrackingContentAssistTest_iteratorAccumulator, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_iteratorAccumulator94", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name96: BinaryAssociation = BinaryAssociation(
    name="name96",
    ends={
        Property(name="backtrackingContentAssistTest_NameExp", type=backtrackingContentAssistTest_RoundBracketExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_RoundBracketExp", type=backtrackingContentAssistTest_NameExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name110: BinaryAssociation = BinaryAssociation(
    name="name110",
    ends={
        Property(name="backtrackingContentAssistTest_NameExp111", type=backtrackingContentAssistTest_PreExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PreExp", type=backtrackingContentAssistTest_NameExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name105: BinaryAssociation = BinaryAssociation(
    name="name105",
    ends={
        Property(name="backtrackingContentAssistTest_NameExp106", type=backtrackingContentAssistTest_SquareBracketExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_SquareBracketExp", type=backtrackingContentAssistTest_NameExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments107: BinaryAssociation = BinaryAssociation(
    name="arguments107",
    ends={
        Property(name="backtrackingContentAssistTest_Expression109", type=backtrackingContentAssistTest_SquareBracketExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_SquareBracketExp108", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression119: BinaryAssociation = BinaryAssociation(
    name="elseExpression119",
    ends={
        Property(name="backtrackingContentAssistTest_Expression121", type=backtrackingContentAssistTest_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_IfExp120", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable122: BinaryAssociation = BinaryAssociation(
    name="variable122",
    ends={
        Property(name="backtrackingContentAssistTest_LetVariable", type=backtrackingContentAssistTest_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_LetExp", type=backtrackingContentAssistTest_LetVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element112: BinaryAssociation = BinaryAssociation(
    name="element112",
    ends={
        Property(name="backtrackingContentAssistTest_NameExp113", type=backtrackingContentAssistTest_PathNameExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PathNameExp", type=backtrackingContentAssistTest_NameExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition114: BinaryAssociation = BinaryAssociation(
    name="condition114",
    ends={
        Property(name="backtrackingContentAssistTest_Expression115", type=backtrackingContentAssistTest_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_IfExp", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression116: BinaryAssociation = BinaryAssociation(
    name="thenExpression116",
    ends={
        Property(name="backtrackingContentAssistTest_Expression118", type=backtrackingContentAssistTest_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_IfExp117", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source132: BinaryAssociation = BinaryAssociation(
    name="source132",
    ends={
        Property(name="backtrackingContentAssistTest_Expression133", type=backtrackingContentAssistTest_InfixExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_InfixExp", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument134: BinaryAssociation = BinaryAssociation(
    name="argument134",
    ends={
        Property(name="backtrackingContentAssistTest_NavigatingExp", type=backtrackingContentAssistTest_InfixExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_InfixExp135", type=backtrackingContentAssistTest_NavigatingExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in123: BinaryAssociation = BinaryAssociation(
    name="in123",
    ends={
        Property(name="backtrackingContentAssistTest_Expression125", type=backtrackingContentAssistTest_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_LetExp124", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type126: BinaryAssociation = BinaryAssociation(
    name="type126",
    ends={
        Property(name="backtrackingContentAssistTest_TypeExp128", type=backtrackingContentAssistTest_LetVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_LetVariable127", type=backtrackingContentAssistTest_TypeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression129: BinaryAssociation = BinaryAssociation(
    name="initExpression129",
    ends={
        Property(name="backtrackingContentAssistTest_Expression131", type=backtrackingContentAssistTest_LetVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_LetVariable130", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source143: BinaryAssociation = BinaryAssociation(
    name="source143",
    ends={
        Property(name="backtrackingContentAssistTest_Expression144", type=backtrackingContentAssistTest_NestedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_NestedExp", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source136: BinaryAssociation = BinaryAssociation(
    name="source136",
    ends={
        Property(name="backtrackingContentAssistTest_Expression137", type=backtrackingContentAssistTest_OclMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OclMessage", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments138: BinaryAssociation = BinaryAssociation(
    name="arguments138",
    ends={
        Property(name="backtrackingContentAssistTest_OclMessageArg140", type=backtrackingContentAssistTest_OclMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_OclMessage139", type=backtrackingContentAssistTest_OclMessageArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source141: BinaryAssociation = BinaryAssociation(
    name="source141",
    ends={
        Property(name="backtrackingContentAssistTest_Expression142", type=backtrackingContentAssistTest_PrefixExp, multiplicity=Multiplicity(1, 1)),
        Property(name="backtrackingContentAssistTest_PrefixExp", type=backtrackingContentAssistTest_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_backtrackingContentAssistTest_ClassifierContextDecl_ContextDecl = Generalization(general=ContextDecl, specific=backtrackingContentAssistTest_ClassifierContextDecl)
gen_backtrackingContentAssistTest_OperationContextDecl_ContextDecl = Generalization(general=ContextDecl, specific=backtrackingContentAssistTest_OperationContextDecl)
gen_backtrackingContentAssistTest_QualifiedClassifierRef_ClassifierRef = Generalization(general=ClassifierRef, specific=backtrackingContentAssistTest_QualifiedClassifierRef)
gen_backtrackingContentAssistTest_QualifiedOperationRef_OperationRef = Generalization(general=OperationRef, specific=backtrackingContentAssistTest_QualifiedOperationRef)
gen_backtrackingContentAssistTest_PropertyContextDecl_ContextDecl = Generalization(general=ContextDecl, specific=backtrackingContentAssistTest_PropertyContextDecl)
gen_backtrackingContentAssistTest_SimplePackageRef_PackageRef = Generalization(general=PackageRef, specific=backtrackingContentAssistTest_SimplePackageRef)
gen_backtrackingContentAssistTest_SimplePropertyRef_PropertyRef = Generalization(general=PropertyRef, specific=backtrackingContentAssistTest_SimplePropertyRef)
gen_backtrackingContentAssistTest_Expression_NavigatingExp = Generalization(general=NavigatingExp, specific=backtrackingContentAssistTest_Expression)
gen_backtrackingContentAssistTest_Expression_OclMessageArg = Generalization(general=OclMessageArg, specific=backtrackingContentAssistTest_Expression)
gen_backtrackingContentAssistTest_QualifiedPropertyRef_PropertyRef = Generalization(general=PropertyRef, specific=backtrackingContentAssistTest_QualifiedPropertyRef)
gen_backtrackingContentAssistTest_QualifiedPackageRef_PackageRef = Generalization(general=PackageRef, specific=backtrackingContentAssistTest_QualifiedPackageRef)
gen_backtrackingContentAssistTest_SimpleClassifierRef_ClassifierRef = Generalization(general=ClassifierRef, specific=backtrackingContentAssistTest_SimpleClassifierRef)
gen_backtrackingContentAssistTest_SimpleOperationRef_OperationRef = Generalization(general=OperationRef, specific=backtrackingContentAssistTest_SimpleOperationRef)
gen_backtrackingContentAssistTest_CollectionLiteralExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_CollectionLiteralExp)
gen_backtrackingContentAssistTest_PrimitiveType_TypeExp = Generalization(general=TypeExp, specific=backtrackingContentAssistTest_PrimitiveType)
gen_backtrackingContentAssistTest_TypeExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_TypeExp)
gen_backtrackingContentAssistTest_CollectionType_TypeExp = Generalization(general=TypeExp, specific=backtrackingContentAssistTest_CollectionType)
gen_backtrackingContentAssistTest_CollectionType_CollectionLiteralExp = Generalization(general=CollectionLiteralExp, specific=backtrackingContentAssistTest_CollectionType)
gen_backtrackingContentAssistTest_TupleType_TypeExp = Generalization(general=TypeExp, specific=backtrackingContentAssistTest_TupleType)
gen_backtrackingContentAssistTest_PrimitiveLiteralExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_PrimitiveLiteralExp)
gen_backtrackingContentAssistTest_TupleLiteralExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_TupleLiteralExp)
gen_backtrackingContentAssistTest_InvalidLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=backtrackingContentAssistTest_InvalidLiteralExp)
gen_backtrackingContentAssistTest_NullLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=backtrackingContentAssistTest_NullLiteralExp)
gen_backtrackingContentAssistTest_NumberLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=backtrackingContentAssistTest_NumberLiteralExp)
gen_backtrackingContentAssistTest_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=backtrackingContentAssistTest_StringLiteralExp)
gen_backtrackingContentAssistTest_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=backtrackingContentAssistTest_BooleanLiteralExp)
gen_backtrackingContentAssistTest_RoundBracketExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_RoundBracketExp)
gen_backtrackingContentAssistTest_SelfExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_SelfExp)
gen_backtrackingContentAssistTest_NameExp_TypeExp = Generalization(general=TypeExp, specific=backtrackingContentAssistTest_NameExp)
gen_backtrackingContentAssistTest_PathNameExp_NameExp = Generalization(general=NameExp, specific=backtrackingContentAssistTest_PathNameExp)
gen_backtrackingContentAssistTest_SquareBracketExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_SquareBracketExp)
gen_backtrackingContentAssistTest_PreExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_PreExp)
gen_backtrackingContentAssistTest_LetExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_LetExp)
gen_backtrackingContentAssistTest_SimpleNameExp_NameExp = Generalization(general=NameExp, specific=backtrackingContentAssistTest_SimpleNameExp)
gen_backtrackingContentAssistTest_IfExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_IfExp)
gen_backtrackingContentAssistTest_OclMessage_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_OclMessage)
gen_backtrackingContentAssistTest_InfixExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_InfixExp)
gen_backtrackingContentAssistTest_NestedExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_NestedExp)
gen_backtrackingContentAssistTest_PrefixExp_Expression = Generalization(general=Expression, specific=backtrackingContentAssistTest_PrefixExp)

# Domain Model
domain_model = DomainModel(
    name="backtrackingContentAssistTest",
    types={backtrackingContentAssistTest_Document, backtrackingContentAssistTest_PackageDeclaration, backtrackingContentAssistTest_ClassifierContextDecl, ContextDecl, backtrackingContentAssistTest_ClassifierRef, backtrackingContentAssistTest_Invariant, backtrackingContentAssistTest_ContextDecl, backtrackingContentAssistTest_Body, backtrackingContentAssistTest_Expression, backtrackingContentAssistTest_Parameter, backtrackingContentAssistTest_TypeExp, backtrackingContentAssistTest_Definition, backtrackingContentAssistTest_OperationRef, backtrackingContentAssistTest_Der, backtrackingContentAssistTest_Init, backtrackingContentAssistTest_OperationContextDecl, backtrackingContentAssistTest_PackageRef, backtrackingContentAssistTest_Pre, backtrackingContentAssistTest_Post, backtrackingContentAssistTest_QualifiedClassifierRef, ClassifierRef, backtrackingContentAssistTest_QualifiedOperationRef, OperationRef, backtrackingContentAssistTest_PropertyContextDecl, backtrackingContentAssistTest_PropertyRef, backtrackingContentAssistTest_SimplePackageRef, backtrackingContentAssistTest_SimplePropertyRef, NavigatingExp, OclMessageArg, backtrackingContentAssistTest_NavigatingExp, backtrackingContentAssistTest_OclMessageArg, backtrackingContentAssistTest_QualifiedPropertyRef, PropertyRef, backtrackingContentAssistTest_QualifiedPackageRef, PackageRef, backtrackingContentAssistTest_SimpleClassifierRef, backtrackingContentAssistTest_SimpleOperationRef, backtrackingContentAssistTest_CollectionLiteralExp, backtrackingContentAssistTest_CollectionLiteralPart, backtrackingContentAssistTest_PrimitiveType, TypeExp, Expression, backtrackingContentAssistTest_CollectionType, CollectionLiteralExp, backtrackingContentAssistTest_TupleType, backtrackingContentAssistTest_tuplePart, backtrackingContentAssistTest_TupleLiteralPart, backtrackingContentAssistTest_PrimitiveLiteralExp, backtrackingContentAssistTest_TupleLiteralExp, backtrackingContentAssistTest_InvalidLiteralExp, backtrackingContentAssistTest_NullLiteralExp, backtrackingContentAssistTest_iteratorVariable, backtrackingContentAssistTest_NumberLiteralExp, PrimitiveLiteralExp, backtrackingContentAssistTest_StringLiteralExp, backtrackingContentAssistTest_BooleanLiteralExp, backtrackingContentAssistTest_EObject, backtrackingContentAssistTest_iteratorAccumulator, backtrackingContentAssistTest_RoundBracketExp, backtrackingContentAssistTest_NameExp, backtrackingContentAssistTest_SelfExp, backtrackingContentAssistTest_PathNameExp, NameExp, backtrackingContentAssistTest_SquareBracketExp, backtrackingContentAssistTest_PreExp, backtrackingContentAssistTest_LetExp, backtrackingContentAssistTest_LetVariable, backtrackingContentAssistTest_SimpleNameExp, backtrackingContentAssistTest_IfExp, backtrackingContentAssistTest_OclMessage, backtrackingContentAssistTest_InfixExp, backtrackingContentAssistTest_NestedExp, backtrackingContentAssistTest_PrefixExp},
    associations={classifier4, invariants5, packages0, contexts1, expression3, parameters9, type11, expression13, definitions7, operation23, parameters24, type27, expression16, expression18, expression20, package37, contexts39, type42, pres30, posts32, bodies34, der58, element61, expression45, expression48, property51, type52, init55, element63, type69, element65, element67, part71, type72, part82, type83, collectionLiteralParts75, expression76, lastExpression79, type89, initExpression86, variable197, variable2100, arguments102, type91, initExpression93, name96, name110, name105, arguments107, elseExpression119, variable122, element112, condition114, thenExpression116, source132, argument134, in123, type126, initExpression129, source143, source136, arguments138, source141},
    generalizations={gen_backtrackingContentAssistTest_ClassifierContextDecl_ContextDecl, gen_backtrackingContentAssistTest_OperationContextDecl_ContextDecl, gen_backtrackingContentAssistTest_QualifiedClassifierRef_ClassifierRef, gen_backtrackingContentAssistTest_QualifiedOperationRef_OperationRef, gen_backtrackingContentAssistTest_PropertyContextDecl_ContextDecl, gen_backtrackingContentAssistTest_SimplePackageRef_PackageRef, gen_backtrackingContentAssistTest_SimplePropertyRef_PropertyRef, gen_backtrackingContentAssistTest_Expression_NavigatingExp, gen_backtrackingContentAssistTest_Expression_OclMessageArg, gen_backtrackingContentAssistTest_QualifiedPropertyRef_PropertyRef, gen_backtrackingContentAssistTest_QualifiedPackageRef_PackageRef, gen_backtrackingContentAssistTest_SimpleClassifierRef_ClassifierRef, gen_backtrackingContentAssistTest_SimpleOperationRef_OperationRef, gen_backtrackingContentAssistTest_CollectionLiteralExp_Expression, gen_backtrackingContentAssistTest_PrimitiveType_TypeExp, gen_backtrackingContentAssistTest_TypeExp_Expression, gen_backtrackingContentAssistTest_CollectionType_TypeExp, gen_backtrackingContentAssistTest_CollectionType_CollectionLiteralExp, gen_backtrackingContentAssistTest_TupleType_TypeExp, gen_backtrackingContentAssistTest_PrimitiveLiteralExp_Expression, gen_backtrackingContentAssistTest_TupleLiteralExp_Expression, gen_backtrackingContentAssistTest_InvalidLiteralExp_PrimitiveLiteralExp, gen_backtrackingContentAssistTest_NullLiteralExp_PrimitiveLiteralExp, gen_backtrackingContentAssistTest_NumberLiteralExp_PrimitiveLiteralExp, gen_backtrackingContentAssistTest_StringLiteralExp_PrimitiveLiteralExp, gen_backtrackingContentAssistTest_BooleanLiteralExp_PrimitiveLiteralExp, gen_backtrackingContentAssistTest_RoundBracketExp_Expression, gen_backtrackingContentAssistTest_SelfExp_Expression, gen_backtrackingContentAssistTest_NameExp_TypeExp, gen_backtrackingContentAssistTest_PathNameExp_NameExp, gen_backtrackingContentAssistTest_SquareBracketExp_Expression, gen_backtrackingContentAssistTest_PreExp_Expression, gen_backtrackingContentAssistTest_LetExp_Expression, gen_backtrackingContentAssistTest_SimpleNameExp_NameExp, gen_backtrackingContentAssistTest_IfExp_Expression, gen_backtrackingContentAssistTest_OclMessage_Expression, gen_backtrackingContentAssistTest_InfixExp_Expression, gen_backtrackingContentAssistTest_NestedExp_Expression, gen_backtrackingContentAssistTest_PrefixExp_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)