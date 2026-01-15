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
PrePostOrBodyEnum: Enumeration = Enumeration(
    name="PrePostOrBodyEnum",
    literals={
            EnumerationLiteral(name="pre"),
			EnumerationLiteral(name="post"),
			EnumerationLiteral(name="body")
    }
)

SimpleTypeEnum: Enumeration = Enumeration(
    name="SimpleTypeEnum",
    literals={
            EnumerationLiteral(name="identifier"),
			EnumerationLiteral(name="self"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="OclAny"),
			EnumerationLiteral(name="OclVoid"),
			EnumerationLiteral(name="Invalid"),
			EnumerationLiteral(name="OclMessage"),
			EnumerationLiteral(name="keyword")
    }
)

CollectionTypeIdentifierEnum: Enumeration = Enumeration(
    name="CollectionTypeIdentifierEnum",
    literals={
            EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="Collection"),
			EnumerationLiteral(name="OrderedSet")
    }
)

DotOrArrowEnum: Enumeration = Enumeration(
    name="DotOrArrowEnum",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="arrow")
    }
)

MessageExpKind: Enumeration = Enumeration(
    name="MessageExpKind",
    literals={
            EnumerationLiteral(name="hasSent"),
			EnumerationLiteral(name="sent")
    }
)

# Classes
ocl_cst_ContextDeclCS = Class(name="ocl::cst::ContextDeclCS", is_abstract=True)
ocl_cst_PropertyContextCS = Class(name="ocl::cst::PropertyContextCS")
SimpleNameCS = Class(name="SimpleNameCS")
TypeCS = Class(name="TypeCS")
InitOrDerValueCS = Class(name="InitOrDerValueCS")
ocl_cst_CSTNode = Class(name="ocl::cst::CSTNode", is_abstract=True)
ocl_cst_PackageDeclarationCS = Class(name="ocl::cst::PackageDeclarationCS")
CSTNode = Class(name="CSTNode")
PathNameCS = Class(name="PathNameCS")
ContextDeclCS = Class(name="ContextDeclCS")
ocl_cst_InitOrDerValueCS = Class(name="ocl::cst::InitOrDerValueCS", is_abstract=True)
ocl_cst_DerValueCS = Class(name="ocl::cst::DerValueCS")
ocl_cst_InitValueCS = Class(name="ocl::cst::InitValueCS")
ocl_cst_InvOrDefCS = Class(name="ocl::cst::InvOrDefCS", is_abstract=True)
ocl_cst_ClassifierContextDeclCS = Class(name="ocl::cst::ClassifierContextDeclCS")
ocl_cst_InvCS = Class(name="ocl::cst::InvCS")
InvOrDefCS = Class(name="InvOrDefCS")
ocl_cst_OperationContextDeclCS = Class(name="ocl::cst::OperationContextDeclCS")
OperationCS = Class(name="OperationCS")
ocl_cst_DefCS = Class(name="ocl::cst::DefCS")
DefExpressionCS = Class(name="DefExpressionCS")
PrePostOrBodyDeclCS = Class(name="PrePostOrBodyDeclCS")
ocl_cst_DefExpressionCS = Class(name="ocl::cst::DefExpressionCS")
ocl_cst_PrePostOrBodyDeclCS = Class(name="ocl::cst::PrePostOrBodyDeclCS")
OCLExpressionCS = Class(name="OCLExpressionCS")
ocl_cst_OperationCS = Class(name="ocl::cst::OperationCS")
VariableCS = Class(name="VariableCS")
ocl_cst_SimpleNameCS = Class(name="ocl::cst::SimpleNameCS")
ocl_cst_TypeCS = Class(name="ocl::cst::TypeCS", is_abstract=True)
ocl_cst_PrimitiveTypeCS = Class(name="ocl::cst::PrimitiveTypeCS")
cst_SimpleNameCS = Class(name="cst::SimpleNameCS")
cst_TypeCS = Class(name="cst::TypeCS")
ocl_cst_TupleTypeCS = Class(name="ocl::cst::TupleTypeCS")
ocl_cst_CollectionTypeCS = Class(name="ocl::cst::CollectionTypeCS")
ocl_cst_OCLExpressionCS = Class(name="ocl::cst::OCLExpressionCS", is_abstract=True)
ocl_cst_PathNameCS = Class(name="ocl::cst::PathNameCS")
ocl_cst_LetExpCS = Class(name="ocl::cst::LetExpCS")
ocl_cst_VariableExpCS = Class(name="ocl::cst::VariableExpCS")
ocl_cst_IfExpCS = Class(name="ocl::cst::IfExpCS")
IsMarkedPreCS = Class(name="IsMarkedPreCS")
CollectionLiteralPartCS = Class(name="CollectionLiteralPartCS")
ocl_cst_MessageExpCS = Class(name="ocl::cst::MessageExpCS")
OCLMessageArgCS = Class(name="OCLMessageArgCS")
ocl_cst_OCLMessageArgCS = Class(name="ocl::cst::OCLMessageArgCS")
ocl_cst_VariableCS = Class(name="ocl::cst::VariableCS")
ocl_cst_LiteralExpCS = Class(name="ocl::cst::LiteralExpCS", is_abstract=True)
ocl_cst_EnumLiteralExpCS = Class(name="ocl::cst::EnumLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
ocl_cst_CollectionLiteralExpCS = Class(name="ocl::cst::CollectionLiteralExpCS")
ocl_cst_TupleLiteralExpCS = Class(name="ocl::cst::TupleLiteralExpCS")
ocl_cst_PrimitiveLiteralExpCS = Class(name="ocl::cst::PrimitiveLiteralExpCS")
ocl_cst_IntegerLiteralExpCS = Class(name="ocl::cst::IntegerLiteralExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
ocl_cst_RealLiteralExpCS = Class(name="ocl::cst::RealLiteralExpCS")
ocl_cst_StringLiteralExpCS = Class(name="ocl::cst::StringLiteralExpCS")
ocl_cst_BooleanLiteralExpCS = Class(name="ocl::cst::BooleanLiteralExpCS")
ocl_cst_NullLiteralExpCS = Class(name="ocl::cst::NullLiteralExpCS")
ocl_cst_InvalidLiteralExpCS = Class(name="ocl::cst::InvalidLiteralExpCS")
ocl_cst_CollectionLiteralPartCS = Class(name="ocl::cst::CollectionLiteralPartCS")
ocl_cst_CollectionRangeCS = Class(name="ocl::cst::CollectionRangeCS")
ocl_cst_CallExpCS = Class(name="ocl::cst::CallExpCS")
ocl_cst_LoopExpCS = Class(name="ocl::cst::LoopExpCS")
CallExpCS = Class(name="CallExpCS")
ocl_cst_IteratorExpCS = Class(name="ocl::cst::IteratorExpCS")
LoopExpCS = Class(name="LoopExpCS")
ocl_cst_IterateExpCS = Class(name="ocl::cst::IterateExpCS")
ocl_cst_FeatureCallExpCS = Class(name="ocl::cst::FeatureCallExpCS")
ocl_cst_OperationCallExpCS = Class(name="ocl::cst::OperationCallExpCS")
FeatureCallExpCS = Class(name="FeatureCallExpCS")
ocl_cst_IsMarkedPreCS = Class(name="ocl::cst::IsMarkedPreCS")
ocl_cst_StateExpCS = Class(name="ocl::cst::StateExpCS")

# ocl_cst_ContextDeclCS class attributes and methods

# ocl_cst_PropertyContextCS class attributes and methods

# SimpleNameCS class attributes and methods

# TypeCS class attributes and methods

# InitOrDerValueCS class attributes and methods

# ocl_cst_CSTNode class attributes and methods
ocl_cst_CSTNode_startOffset: Property = Property(name="startOffset", type=IntegerType)
ocl_cst_CSTNode_endOffset: Property = Property(name="endOffset", type=IntegerType)
ocl_cst_CSTNode.attributes={ocl_cst_CSTNode_endOffset, ocl_cst_CSTNode_startOffset}

# ocl_cst_PackageDeclarationCS class attributes and methods

# CSTNode class attributes and methods

# PathNameCS class attributes and methods

# ContextDeclCS class attributes and methods

# ocl_cst_InitOrDerValueCS class attributes and methods

# ocl_cst_DerValueCS class attributes and methods

# ocl_cst_InitValueCS class attributes and methods

# ocl_cst_InvOrDefCS class attributes and methods

# ocl_cst_ClassifierContextDeclCS class attributes and methods

# ocl_cst_InvCS class attributes and methods

# InvOrDefCS class attributes and methods

# ocl_cst_OperationContextDeclCS class attributes and methods

# OperationCS class attributes and methods

# ocl_cst_DefCS class attributes and methods

# DefExpressionCS class attributes and methods

# PrePostOrBodyDeclCS class attributes and methods

# ocl_cst_DefExpressionCS class attributes and methods

# ocl_cst_PrePostOrBodyDeclCS class attributes and methods
ocl_cst_PrePostOrBodyDeclCS_kind: Property = Property(name="kind", type=StringType)
ocl_cst_PrePostOrBodyDeclCS.attributes={ocl_cst_PrePostOrBodyDeclCS_kind}

# OCLExpressionCS class attributes and methods

# ocl_cst_OperationCS class attributes and methods

# VariableCS class attributes and methods

# ocl_cst_SimpleNameCS class attributes and methods
ocl_cst_SimpleNameCS_value: Property = Property(name="value", type=StringType)
ocl_cst_SimpleNameCS_type: Property = Property(name="type", type=StringType)
ocl_cst_SimpleNameCS.attributes={ocl_cst_SimpleNameCS_type, ocl_cst_SimpleNameCS_value}

# ocl_cst_TypeCS class attributes and methods

# ocl_cst_PrimitiveTypeCS class attributes and methods

# cst_SimpleNameCS class attributes and methods

# cst_TypeCS class attributes and methods

# ocl_cst_TupleTypeCS class attributes and methods

# ocl_cst_CollectionTypeCS class attributes and methods
ocl_cst_CollectionTypeCS_collectionTypeIdentifier: Property = Property(name="collectionTypeIdentifier", type=StringType)
ocl_cst_CollectionTypeCS.attributes={ocl_cst_CollectionTypeCS_collectionTypeIdentifier}

# ocl_cst_OCLExpressionCS class attributes and methods

# ocl_cst_PathNameCS class attributes and methods
ocl_cst_PathNameCS_sequenceOfNames: Property = Property(name="sequenceOfNames", type=StringType)
ocl_cst_PathNameCS.attributes={ocl_cst_PathNameCS_sequenceOfNames}

# ocl_cst_LetExpCS class attributes and methods

# ocl_cst_VariableExpCS class attributes and methods

# ocl_cst_IfExpCS class attributes and methods

# IsMarkedPreCS class attributes and methods

# CollectionLiteralPartCS class attributes and methods

# ocl_cst_MessageExpCS class attributes and methods
ocl_cst_MessageExpCS_kind: Property = Property(name="kind", type=StringType)
ocl_cst_MessageExpCS.attributes={ocl_cst_MessageExpCS_kind}

# OCLMessageArgCS class attributes and methods

# ocl_cst_OCLMessageArgCS class attributes and methods

# ocl_cst_VariableCS class attributes and methods
ocl_cst_VariableCS_name: Property = Property(name="name", type=StringType)
ocl_cst_VariableCS.attributes={ocl_cst_VariableCS_name}

# ocl_cst_LiteralExpCS class attributes and methods

# ocl_cst_EnumLiteralExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# ocl_cst_CollectionLiteralExpCS class attributes and methods
ocl_cst_CollectionLiteralExpCS_collectionType: Property = Property(name="collectionType", type=StringType)
ocl_cst_CollectionLiteralExpCS.attributes={ocl_cst_CollectionLiteralExpCS_collectionType}

# ocl_cst_TupleLiteralExpCS class attributes and methods

# ocl_cst_PrimitiveLiteralExpCS class attributes and methods
ocl_cst_PrimitiveLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_PrimitiveLiteralExpCS.attributes={ocl_cst_PrimitiveLiteralExpCS_symbol}

# ocl_cst_IntegerLiteralExpCS class attributes and methods
ocl_cst_IntegerLiteralExpCS_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_cst_IntegerLiteralExpCS.attributes={ocl_cst_IntegerLiteralExpCS_integerSymbol}

# PrimitiveLiteralExpCS class attributes and methods

# ocl_cst_RealLiteralExpCS class attributes and methods
ocl_cst_RealLiteralExpCS_realSymbol: Property = Property(name="realSymbol", type=StringType)
ocl_cst_RealLiteralExpCS.attributes={ocl_cst_RealLiteralExpCS_realSymbol}

# ocl_cst_StringLiteralExpCS class attributes and methods
ocl_cst_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
ocl_cst_StringLiteralExpCS.attributes={ocl_cst_StringLiteralExpCS_stringSymbol}

# ocl_cst_BooleanLiteralExpCS class attributes and methods
ocl_cst_BooleanLiteralExpCS_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
ocl_cst_BooleanLiteralExpCS.attributes={ocl_cst_BooleanLiteralExpCS_booleanSymbol}

# ocl_cst_NullLiteralExpCS class attributes and methods
ocl_cst_NullLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_NullLiteralExpCS.attributes={ocl_cst_NullLiteralExpCS_symbol}

# ocl_cst_InvalidLiteralExpCS class attributes and methods
ocl_cst_InvalidLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_InvalidLiteralExpCS.attributes={ocl_cst_InvalidLiteralExpCS_symbol}

# ocl_cst_CollectionLiteralPartCS class attributes and methods

# ocl_cst_CollectionRangeCS class attributes and methods

# ocl_cst_CallExpCS class attributes and methods
ocl_cst_CallExpCS_accessor: Property = Property(name="accessor", type=StringType)
ocl_cst_CallExpCS.attributes={ocl_cst_CallExpCS_accessor}

# ocl_cst_LoopExpCS class attributes and methods

# CallExpCS class attributes and methods

# ocl_cst_IteratorExpCS class attributes and methods

# LoopExpCS class attributes and methods

# ocl_cst_IterateExpCS class attributes and methods

# ocl_cst_FeatureCallExpCS class attributes and methods

# ocl_cst_OperationCallExpCS class attributes and methods

# FeatureCallExpCS class attributes and methods

# ocl_cst_IsMarkedPreCS class attributes and methods
ocl_cst_IsMarkedPreCS_pre: Property = Property(name="pre", type=BooleanType)
ocl_cst_IsMarkedPreCS.attributes={ocl_cst_IsMarkedPreCS_pre}

# ocl_cst_StateExpCS class attributes and methods
ocl_cst_StateExpCS_sequenceOfNames: Property = Property(name="sequenceOfNames", type=StringType)
ocl_cst_StateExpCS.attributes={ocl_cst_StateExpCS_sequenceOfNames}

# Relationships
pathNameCS3: BinaryAssociation = BinaryAssociation(
    name="pathNameCS3",
    ends={
        Property(name="PathNameCS4", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS", type=PathNameCS, multiplicity=Multiplicity(0, 1))
    }
)
simpleNameCS5: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS5",
    ends={
        Property(name="SimpleNameCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS6", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
typeCS7: BinaryAssociation = BinaryAssociation(
    name="typeCS7",
    ends={
        Property(name="TypeCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS8", type=TypeCS, multiplicity=Multiplicity(0, 1))
    }
)
initOrDerValueCS9: BinaryAssociation = BinaryAssociation(
    name="initOrDerValueCS9",
    ends={
        Property(name="InitOrDerValueCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS10", type=InitOrDerValueCS, multiplicity=Multiplicity(0, 1))
    }
)
pathNameCS0: BinaryAssociation = BinaryAssociation(
    name="pathNameCS0",
    ends={
        Property(name="PathNameCS", type=ocl_cst_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PackageDeclarationCS", type=PathNameCS, multiplicity=Multiplicity(0, 1))
    }
)
contextDecls1: BinaryAssociation = BinaryAssociation(
    name="contextDecls1",
    ends={
        Property(name="ContextDeclCS", type=ocl_cst_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PackageDeclarationCS2", type=ContextDeclCS, multiplicity=Multiplicity(0, 9999))
    }
)
initOrDerValueCS32: BinaryAssociation = BinaryAssociation(
    name="initOrDerValueCS32",
    ends={
        Property(name="InitOrDerValueCS33", type=ocl_cst_InitOrDerValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InitOrDerValueCS", type=InitOrDerValueCS, multiplicity=Multiplicity(0, 1))
    }
)
expressionCS34: BinaryAssociation = BinaryAssociation(
    name="expressionCS34",
    ends={
        Property(name="OCLExpressionCS36", type=ocl_cst_InitOrDerValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InitOrDerValueCS35", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
simpleNameCS37: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS37",
    ends={
        Property(name="SimpleNameCS38", type=ocl_cst_InvOrDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvOrDefCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
invOrDefCS39: BinaryAssociation = BinaryAssociation(
    name="invOrDefCS39",
    ends={
        Property(name="InvOrDefCS41", type=ocl_cst_InvOrDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvOrDefCS40", type=InvOrDefCS, multiplicity=Multiplicity(0, 1))
    }
)
pathNameCS11: BinaryAssociation = BinaryAssociation(
    name="pathNameCS11",
    ends={
        Property(name="PathNameCS12", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS", type=PathNameCS, multiplicity=Multiplicity(0, 1))
    }
)
invOrDefCS13: BinaryAssociation = BinaryAssociation(
    name="invOrDefCS13",
    ends={
        Property(name="InvOrDefCS", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS14", type=InvOrDefCS, multiplicity=Multiplicity(0, 1))
    }
)
expressionCS42: BinaryAssociation = BinaryAssociation(
    name="expressionCS42",
    ends={
        Property(name="OCLExpressionCS43", type=ocl_cst_InvCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
operationCS15: BinaryAssociation = BinaryAssociation(
    name="operationCS15",
    ends={
        Property(name="OperationCS", type=ocl_cst_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationContextDeclCS", type=OperationCS, multiplicity=Multiplicity(0, 1))
    }
)
defExpressionCS44: BinaryAssociation = BinaryAssociation(
    name="defExpressionCS44",
    ends={
        Property(name="DefExpressionCS", type=ocl_cst_DefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefCS", type=DefExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
prePostOrBodyDecls16: BinaryAssociation = BinaryAssociation(
    name="prePostOrBodyDecls16",
    ends={
        Property(name="PrePostOrBodyDeclCS", type=ocl_cst_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationContextDeclCS17", type=PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 9999))
    }
)
operationCS45: BinaryAssociation = BinaryAssociation(
    name="operationCS45",
    ends={
        Property(name="OperationCS46", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS", type=OperationCS, multiplicity=Multiplicity(0, 1))
    }
)
simpleNameCS18: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS18",
    ends={
        Property(name="SimpleNameCS19", type=ocl_cst_PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PrePostOrBodyDeclCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
variableCS47: BinaryAssociation = BinaryAssociation(
    name="variableCS47",
    ends={
        Property(name="VariableCS49", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS48", type=VariableCS, multiplicity=Multiplicity(0, 1))
    }
)
expressionCS20: BinaryAssociation = BinaryAssociation(
    name="expressionCS20",
    ends={
        Property(name="OCLExpressionCS", type=ocl_cst_PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PrePostOrBodyDeclCS21", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
expressionCS50: BinaryAssociation = BinaryAssociation(
    name="expressionCS50",
    ends={
        Property(name="OCLExpressionCS52", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS51", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
pathNameCS22: BinaryAssociation = BinaryAssociation(
    name="pathNameCS22",
    ends={
        Property(name="PathNameCS23", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS", type=PathNameCS, multiplicity=Multiplicity(0, 1))
    }
)
simpleNameCS24: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS24",
    ends={
        Property(name="SimpleNameCS26", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS25", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
parameters27: BinaryAssociation = BinaryAssociation(
    name="parameters27",
    ends={
        Property(name="VariableCS", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS28", type=VariableCS, multiplicity=Multiplicity(0, 9999))
    }
)
typeCS29: BinaryAssociation = BinaryAssociation(
    name="typeCS29",
    ends={
        Property(name="TypeCS31", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS30", type=TypeCS, multiplicity=Multiplicity(0, 1))
    }
)
elseExpression71: BinaryAssociation = BinaryAssociation(
    name="elseExpression71",
    ends={
        Property(name="OCLExpressionCS73", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS72", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition74: BinaryAssociation = BinaryAssociation(
    name="condition74",
    ends={
        Property(name="OCLExpressionCS76", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS75", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables60: BinaryAssociation = BinaryAssociation(
    name="variables60",
    ends={
        Property(name="VariableCS61", type=ocl_cst_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_TupleTypeCS", type=VariableCS, multiplicity=Multiplicity(1, 9999))
    }
)
typeCS62: BinaryAssociation = BinaryAssociation(
    name="typeCS62",
    ends={
        Property(name="TypeCS63", type=ocl_cst_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1))
    }
)
variables64: BinaryAssociation = BinaryAssociation(
    name="variables64",
    ends={
        Property(name="VariableCS65", type=ocl_cst_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LetExpCS", type=VariableCS, multiplicity=Multiplicity(1, 9999))
    }
)
inExpression66: BinaryAssociation = BinaryAssociation(
    name="inExpression66",
    ends={
        Property(name="OCLExpressionCS68", type=ocl_cst_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LetExpCS67", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
arguments53: BinaryAssociation = BinaryAssociation(
    name="arguments53",
    ends={
        Property(name="OCLExpressionCS54", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999))
    }
)
simpleNameCS55: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS55",
    ends={
        Property(name="SimpleNameCS57", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS56", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
thenExpression69: BinaryAssociation = BinaryAssociation(
    name="thenExpression69",
    ends={
        Property(name="OCLExpressionCS70", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
isMarkedPreCS58: BinaryAssociation = BinaryAssociation(
    name="isMarkedPreCS58",
    ends={
        Property(name="IsMarkedPreCS", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS59", type=IsMarkedPreCS, multiplicity=Multiplicity(0, 1))
    }
)
collectionLiteralParts99: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts99",
    ends={
        Property(name="CollectionLiteralPartCS", type=ocl_cst_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionLiteralExpCS", type=CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999))
    }
)
target77: BinaryAssociation = BinaryAssociation(
    name="target77",
    ends={
        Property(name="OCLExpressionCS78", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS79: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS79",
    ends={
        Property(name="SimpleNameCS81", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS80", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
arguments82: BinaryAssociation = BinaryAssociation(
    name="arguments82",
    ends={
        Property(name="OCLMessageArgCS", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS83", type=OCLMessageArgCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS84: BinaryAssociation = BinaryAssociation(
    name="typeCS84",
    ends={
        Property(name="TypeCS85", type=ocl_cst_OCLMessageArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLMessageArgCS", type=TypeCS, multiplicity=Multiplicity(0, 1))
    }
)
expression86: BinaryAssociation = BinaryAssociation(
    name="expression86",
    ends={
        Property(name="OCLExpressionCS88", type=ocl_cst_OCLMessageArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLMessageArgCS87", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
typeCS89: BinaryAssociation = BinaryAssociation(
    name="typeCS89",
    ends={
        Property(name="TypeCS90", type=ocl_cst_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableCS", type=TypeCS, multiplicity=Multiplicity(0, 1))
    }
)
initExpression91: BinaryAssociation = BinaryAssociation(
    name="initExpression91",
    ends={
        Property(name="OCLExpressionCS93", type=ocl_cst_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableCS92", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
pathNameCS94: BinaryAssociation = BinaryAssociation(
    name="pathNameCS94",
    ends={
        Property(name="PathNameCS95", type=ocl_cst_EnumLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_EnumLiteralExpCS", type=PathNameCS, multiplicity=Multiplicity(0, 1))
    }
)
simpleNameCS96: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS96",
    ends={
        Property(name="SimpleNameCS98", type=ocl_cst_EnumLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_EnumLiteralExpCS97", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
simpleNameCS108: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS108",
    ends={
        Property(name="SimpleNameCS110", type=ocl_cst_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CallExpCS109", type=SimpleNameCS, multiplicity=Multiplicity(0, 1))
    }
)
variables100: BinaryAssociation = BinaryAssociation(
    name="variables100",
    ends={
        Property(name="VariableCS101", type=ocl_cst_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_TupleLiteralExpCS", type=VariableCS, multiplicity=Multiplicity(0, 9999))
    }
)
expressionCS102: BinaryAssociation = BinaryAssociation(
    name="expressionCS102",
    ends={
        Property(name="OCLExpressionCS103", type=ocl_cst_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionLiteralPartCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
lastExpressionCS104: BinaryAssociation = BinaryAssociation(
    name="lastExpressionCS104",
    ends={
        Property(name="OCLExpressionCS105", type=ocl_cst_CollectionRangeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionRangeCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
source106: BinaryAssociation = BinaryAssociation(
    name="source106",
    ends={
        Property(name="OCLExpressionCS107", type=ocl_cst_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CallExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
variable1111: BinaryAssociation = BinaryAssociation(
    name="variable1111",
    ends={
        Property(name="VariableCS112", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1))
    }
)
variable2113: BinaryAssociation = BinaryAssociation(
    name="variable2113",
    ends={
        Property(name="VariableCS115", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS114", type=VariableCS, multiplicity=Multiplicity(0, 1))
    }
)
body116: BinaryAssociation = BinaryAssociation(
    name="body116",
    ends={
        Property(name="OCLExpressionCS118", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS117", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
arguments119: BinaryAssociation = BinaryAssociation(
    name="arguments119",
    ends={
        Property(name="OCLExpressionCS120", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999))
    }
)
isMarkedPreCS121: BinaryAssociation = BinaryAssociation(
    name="isMarkedPreCS121",
    ends={
        Property(name="IsMarkedPreCS123", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS122", type=IsMarkedPreCS, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ocl_cst_ContextDeclCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_ContextDeclCS)
gen_ocl_cst_PropertyContextCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_PropertyContextCS)
gen_ocl_cst_PackageDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_PackageDeclarationCS)
gen_ocl_cst_InitOrDerValueCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_InitOrDerValueCS)
gen_ocl_cst_DerValueCS_InitOrDerValueCS = Generalization(general=InitOrDerValueCS, specific=ocl_cst_DerValueCS)
gen_ocl_cst_InitValueCS_InitOrDerValueCS = Generalization(general=InitOrDerValueCS, specific=ocl_cst_InitValueCS)
gen_ocl_cst_InvOrDefCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_InvOrDefCS)
gen_ocl_cst_ClassifierContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_ClassifierContextDeclCS)
gen_ocl_cst_InvCS_InvOrDefCS = Generalization(general=InvOrDefCS, specific=ocl_cst_InvCS)
gen_ocl_cst_OperationContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_OperationContextDeclCS)
gen_ocl_cst_DefCS_InvOrDefCS = Generalization(general=InvOrDefCS, specific=ocl_cst_DefCS)
gen_ocl_cst_DefExpressionCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_DefExpressionCS)
gen_ocl_cst_PrePostOrBodyDeclCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_PrePostOrBodyDeclCS)
gen_ocl_cst_OperationCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OperationCS)
gen_ocl_cst_SimpleNameCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_SimpleNameCS)
gen_ocl_cst_TypeCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_TypeCS)
gen_ocl_cst_PrimitiveTypeCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_PrimitiveTypeCS)
gen_ocl_cst_PrimitiveTypeCS_cst_TypeCS = Generalization(general=cst_TypeCS, specific=ocl_cst_PrimitiveTypeCS)
gen_ocl_cst_TupleTypeCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_TupleTypeCS)
gen_ocl_cst_CollectionTypeCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_CollectionTypeCS)
gen_ocl_cst_OCLExpressionCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLExpressionCS)
gen_ocl_cst_PathNameCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_PathNameCS)
gen_ocl_cst_LetExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_LetExpCS)
gen_ocl_cst_VariableExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_VariableExpCS)
gen_ocl_cst_IfExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_IfExpCS)
gen_ocl_cst_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_CollectionLiteralExpCS)
gen_ocl_cst_MessageExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_MessageExpCS)
gen_ocl_cst_OCLMessageArgCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLMessageArgCS)
gen_ocl_cst_VariableCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_VariableCS)
gen_ocl_cst_LiteralExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_LiteralExpCS)
gen_ocl_cst_EnumLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_EnumLiteralExpCS)
gen_ocl_cst_TupleLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_TupleLiteralExpCS)
gen_ocl_cst_PrimitiveLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_PrimitiveLiteralExpCS)
gen_ocl_cst_IntegerLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_IntegerLiteralExpCS)
gen_ocl_cst_RealLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_RealLiteralExpCS)
gen_ocl_cst_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_StringLiteralExpCS)
gen_ocl_cst_BooleanLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_BooleanLiteralExpCS)
gen_ocl_cst_NullLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_NullLiteralExpCS)
gen_ocl_cst_InvalidLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_InvalidLiteralExpCS)
gen_ocl_cst_CollectionLiteralPartCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_CollectionLiteralPartCS)
gen_ocl_cst_CollectionRangeCS_CollectionLiteralPartCS = Generalization(general=CollectionLiteralPartCS, specific=ocl_cst_CollectionRangeCS)
gen_ocl_cst_CallExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_CallExpCS)
gen_ocl_cst_LoopExpCS_CallExpCS = Generalization(general=CallExpCS, specific=ocl_cst_LoopExpCS)
gen_ocl_cst_IteratorExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=ocl_cst_IteratorExpCS)
gen_ocl_cst_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=ocl_cst_IterateExpCS)
gen_ocl_cst_FeatureCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=ocl_cst_FeatureCallExpCS)
gen_ocl_cst_OperationCallExpCS_FeatureCallExpCS = Generalization(general=FeatureCallExpCS, specific=ocl_cst_OperationCallExpCS)
gen_ocl_cst_IsMarkedPreCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_IsMarkedPreCS)
gen_ocl_cst_StateExpCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_StateExpCS)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ocl_cst_ContextDeclCS, ocl_cst_PropertyContextCS, SimpleNameCS, TypeCS, InitOrDerValueCS, ocl_cst_CSTNode, ocl_cst_PackageDeclarationCS, CSTNode, PathNameCS, ContextDeclCS, ocl_cst_InitOrDerValueCS, ocl_cst_DerValueCS, ocl_cst_InitValueCS, ocl_cst_InvOrDefCS, ocl_cst_ClassifierContextDeclCS, ocl_cst_InvCS, InvOrDefCS, ocl_cst_OperationContextDeclCS, OperationCS, ocl_cst_DefCS, DefExpressionCS, PrePostOrBodyDeclCS, ocl_cst_DefExpressionCS, ocl_cst_PrePostOrBodyDeclCS, OCLExpressionCS, ocl_cst_OperationCS, VariableCS, ocl_cst_SimpleNameCS, ocl_cst_TypeCS, ocl_cst_PrimitiveTypeCS, cst_SimpleNameCS, cst_TypeCS, ocl_cst_TupleTypeCS, ocl_cst_CollectionTypeCS, ocl_cst_OCLExpressionCS, ocl_cst_PathNameCS, ocl_cst_LetExpCS, ocl_cst_VariableExpCS, ocl_cst_IfExpCS, IsMarkedPreCS, CollectionLiteralPartCS, ocl_cst_MessageExpCS, OCLMessageArgCS, ocl_cst_OCLMessageArgCS, ocl_cst_VariableCS, ocl_cst_LiteralExpCS, ocl_cst_EnumLiteralExpCS, LiteralExpCS, ocl_cst_CollectionLiteralExpCS, ocl_cst_TupleLiteralExpCS, ocl_cst_PrimitiveLiteralExpCS, ocl_cst_IntegerLiteralExpCS, PrimitiveLiteralExpCS, ocl_cst_RealLiteralExpCS, ocl_cst_StringLiteralExpCS, ocl_cst_BooleanLiteralExpCS, ocl_cst_NullLiteralExpCS, ocl_cst_InvalidLiteralExpCS, ocl_cst_CollectionLiteralPartCS, ocl_cst_CollectionRangeCS, ocl_cst_CallExpCS, ocl_cst_LoopExpCS, CallExpCS, ocl_cst_IteratorExpCS, LoopExpCS, ocl_cst_IterateExpCS, ocl_cst_FeatureCallExpCS, ocl_cst_OperationCallExpCS, FeatureCallExpCS, ocl_cst_IsMarkedPreCS, ocl_cst_StateExpCS, PrePostOrBodyEnum, SimpleTypeEnum, CollectionTypeIdentifierEnum, DotOrArrowEnum, MessageExpKind},
    associations={pathNameCS3, simpleNameCS5, typeCS7, initOrDerValueCS9, pathNameCS0, contextDecls1, initOrDerValueCS32, expressionCS34, simpleNameCS37, invOrDefCS39, pathNameCS11, invOrDefCS13, expressionCS42, operationCS15, defExpressionCS44, prePostOrBodyDecls16, operationCS45, simpleNameCS18, variableCS47, expressionCS20, expressionCS50, pathNameCS22, simpleNameCS24, parameters27, typeCS29, elseExpression71, condition74, variables60, typeCS62, variables64, inExpression66, arguments53, simpleNameCS55, thenExpression69, isMarkedPreCS58, collectionLiteralParts99, target77, simpleNameCS79, arguments82, typeCS84, expression86, typeCS89, initExpression91, pathNameCS94, simpleNameCS96, simpleNameCS108, variables100, expressionCS102, lastExpressionCS104, source106, variable1111, variable2113, body116, arguments119, isMarkedPreCS121},
    generalizations={gen_ocl_cst_ContextDeclCS_CSTNode, gen_ocl_cst_PropertyContextCS_ContextDeclCS, gen_ocl_cst_PackageDeclarationCS_CSTNode, gen_ocl_cst_InitOrDerValueCS_CSTNode, gen_ocl_cst_DerValueCS_InitOrDerValueCS, gen_ocl_cst_InitValueCS_InitOrDerValueCS, gen_ocl_cst_InvOrDefCS_CSTNode, gen_ocl_cst_ClassifierContextDeclCS_ContextDeclCS, gen_ocl_cst_InvCS_InvOrDefCS, gen_ocl_cst_OperationContextDeclCS_ContextDeclCS, gen_ocl_cst_DefCS_InvOrDefCS, gen_ocl_cst_DefExpressionCS_CSTNode, gen_ocl_cst_PrePostOrBodyDeclCS_CSTNode, gen_ocl_cst_OperationCS_CSTNode, gen_ocl_cst_SimpleNameCS_OCLExpressionCS, gen_ocl_cst_TypeCS_OCLExpressionCS, gen_ocl_cst_PrimitiveTypeCS_cst_SimpleNameCS, gen_ocl_cst_PrimitiveTypeCS_cst_TypeCS, gen_ocl_cst_TupleTypeCS_TypeCS, gen_ocl_cst_CollectionTypeCS_TypeCS, gen_ocl_cst_OCLExpressionCS_CSTNode, gen_ocl_cst_PathNameCS_TypeCS, gen_ocl_cst_LetExpCS_OCLExpressionCS, gen_ocl_cst_VariableExpCS_OCLExpressionCS, gen_ocl_cst_IfExpCS_OCLExpressionCS, gen_ocl_cst_CollectionLiteralExpCS_LiteralExpCS, gen_ocl_cst_MessageExpCS_OCLExpressionCS, gen_ocl_cst_OCLMessageArgCS_CSTNode, gen_ocl_cst_VariableCS_CSTNode, gen_ocl_cst_LiteralExpCS_OCLExpressionCS, gen_ocl_cst_EnumLiteralExpCS_LiteralExpCS, gen_ocl_cst_TupleLiteralExpCS_LiteralExpCS, gen_ocl_cst_PrimitiveLiteralExpCS_LiteralExpCS, gen_ocl_cst_IntegerLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_RealLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_BooleanLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_NullLiteralExpCS_LiteralExpCS, gen_ocl_cst_InvalidLiteralExpCS_LiteralExpCS, gen_ocl_cst_CollectionLiteralPartCS_CSTNode, gen_ocl_cst_CollectionRangeCS_CollectionLiteralPartCS, gen_ocl_cst_CallExpCS_OCLExpressionCS, gen_ocl_cst_LoopExpCS_CallExpCS, gen_ocl_cst_IteratorExpCS_LoopExpCS, gen_ocl_cst_IterateExpCS_LoopExpCS, gen_ocl_cst_FeatureCallExpCS_CallExpCS, gen_ocl_cst_OperationCallExpCS_FeatureCallExpCS, gen_ocl_cst_IsMarkedPreCS_CSTNode, gen_ocl_cst_StateExpCS_TypeCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)