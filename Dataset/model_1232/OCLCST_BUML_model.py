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
SimpleTypeEnum: Enumeration = Enumeration(
    name="SimpleTypeEnum",
    literals={
            EnumerationLiteral(name="keyword"),
			EnumerationLiteral(name="UnlimitedNatural"),
			EnumerationLiteral(name="identifier"),
			EnumerationLiteral(name="self"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="OclAny"),
			EnumerationLiteral(name="OclVoid"),
			EnumerationLiteral(name="Invalid"),
			EnumerationLiteral(name="OclMessage")
    }
)

PrePostOrBodyEnum: Enumeration = Enumeration(
    name="PrePostOrBodyEnum",
    literals={
            EnumerationLiteral(name="pre"),
			EnumerationLiteral(name="post"),
			EnumerationLiteral(name="body")
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

MessageExpKind: Enumeration = Enumeration(
    name="MessageExpKind",
    literals={
            EnumerationLiteral(name="hasSent"),
			EnumerationLiteral(name="sent")
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

# Classes
ocl_cst_CSTNode = Class(name="ocl::cst::CSTNode", is_abstract=True)
OCLExpressionCS = Class(name="OCLExpressionCS")
ocl_cst_OCLExpressionCS = Class(name="ocl::cst::OCLExpressionCS", is_abstract=True)
ocl_cst_ContextDeclCS = Class(name="ocl::cst::ContextDeclCS", is_abstract=True)
ocl_cst_PropertyContextCS = Class(name="ocl::cst::PropertyContextCS")
SimpleNameCS = Class(name="SimpleNameCS")
InitOrDerValueCS = Class(name="InitOrDerValueCS")
ocl_cst_SimpleNameCS = Class(name="ocl::cst::SimpleNameCS")
ocl_cst_PackageDeclarationCS = Class(name="ocl::cst::PackageDeclarationCS")
CSTNode = Class(name="CSTNode")
PathNameCS = Class(name="PathNameCS")
ContextDeclCS = Class(name="ContextDeclCS")
PackageDeclarationCS = Class(name="PackageDeclarationCS")
ocl_cst_PathNameCS = Class(name="ocl::cst::PathNameCS")
TypeCS = Class(name="TypeCS")
ocl_cst_TypeCS = Class(name="ocl::cst::TypeCS", is_abstract=True)
ocl_cst_InitOrDerValueCS = Class(name="ocl::cst::InitOrDerValueCS", is_abstract=True)
ocl_cst_ClassifierContextDeclCS = Class(name="ocl::cst::ClassifierContextDeclCS")
InvOrDefCS = Class(name="InvOrDefCS")
ocl_cst_OperationCS = Class(name="ocl::cst::OperationCS")
VariableCS = Class(name="VariableCS")
ocl_cst_InvOrDefCS = Class(name="ocl::cst::InvOrDefCS", is_abstract=True)
ocl_cst_OperationContextDeclCS = Class(name="ocl::cst::OperationContextDeclCS")
OperationCS = Class(name="OperationCS")
PrePostOrBodyDeclCS = Class(name="PrePostOrBodyDeclCS")
ocl_cst_DerValueCS = Class(name="ocl::cst::DerValueCS")
ocl_cst_VariableCS = Class(name="ocl::cst::VariableCS")
ocl_cst_PrePostOrBodyDeclCS = Class(name="ocl::cst::PrePostOrBodyDeclCS")
ocl_cst_DefExpressionCS = Class(name="ocl::cst::DefExpressionCS")
ocl_cst_VariableExpCS = Class(name="ocl::cst::VariableExpCS")
ocl_cst_InitValueCS = Class(name="ocl::cst::InitValueCS")
ocl_cst_InvCS = Class(name="ocl::cst::InvCS")
ocl_cst_DefCS = Class(name="ocl::cst::DefCS")
DefExpressionCS = Class(name="DefExpressionCS")
cst_TypeCS = Class(name="cst::TypeCS")
ocl_cst_TupleTypeCS = Class(name="ocl::cst::TupleTypeCS")
ocl_cst_CollectionTypeCS = Class(name="ocl::cst::CollectionTypeCS")
IsMarkedPreCS = Class(name="IsMarkedPreCS")
ocl_cst_IsMarkedPreCS = Class(name="ocl::cst::IsMarkedPreCS")
ocl_cst_PrimitiveTypeCS = Class(name="ocl::cst::PrimitiveTypeCS")
cst_SimpleNameCS = Class(name="cst::SimpleNameCS")
ocl_cst_MessageExpCS = Class(name="ocl::cst::MessageExpCS")
ocl_cst_LetExpCS = Class(name="ocl::cst::LetExpCS")
ocl_cst_IfExpCS = Class(name="ocl::cst::IfExpCS")
ocl_cst_CollectionLiteralExpCS = Class(name="ocl::cst::CollectionLiteralExpCS")
CollectionLiteralPartCS = Class(name="CollectionLiteralPartCS")
ocl_cst_CollectionLiteralPartCS = Class(name="ocl::cst::CollectionLiteralPartCS")
ocl_cst_TupleLiteralExpCS = Class(name="ocl::cst::TupleLiteralExpCS")
OCLMessageArgCS = Class(name="OCLMessageArgCS")
ocl_cst_OCLMessageArgCS = Class(name="ocl::cst::OCLMessageArgCS")
ocl_cst_LiteralExpCS = Class(name="ocl::cst::LiteralExpCS", is_abstract=True)
ocl_cst_EnumLiteralExpCS = Class(name="ocl::cst::EnumLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
ocl_cst_InvalidLiteralExpCS = Class(name="ocl::cst::InvalidLiteralExpCS")
ocl_cst_CollectionRangeCS = Class(name="ocl::cst::CollectionRangeCS")
ocl_cst_CallExpCS = Class(name="ocl::cst::CallExpCS")
ocl_cst_PrimitiveLiteralExpCS = Class(name="ocl::cst::PrimitiveLiteralExpCS")
ocl_cst_IntegerLiteralExpCS = Class(name="ocl::cst::IntegerLiteralExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
ocl_cst_UnlimitedNaturalLiteralExpCS = Class(name="ocl::cst::UnlimitedNaturalLiteralExpCS")
ocl_cst_RealLiteralExpCS = Class(name="ocl::cst::RealLiteralExpCS")
ocl_cst_StringLiteralExpCS = Class(name="ocl::cst::StringLiteralExpCS")
ocl_cst_BooleanLiteralExpCS = Class(name="ocl::cst::BooleanLiteralExpCS")
ocl_cst_NullLiteralExpCS = Class(name="ocl::cst::NullLiteralExpCS")
ocl_cst_OperationCallExpCS = Class(name="ocl::cst::OperationCallExpCS")
FeatureCallExpCS = Class(name="FeatureCallExpCS")
ocl_cst_StateExpCS = Class(name="ocl::cst::StateExpCS")
ocl_cst_OCLDocumentCS = Class(name="ocl::cst::OCLDocumentCS")
ocl_cst_LoopExpCS = Class(name="ocl::cst::LoopExpCS")
CallExpCS = Class(name="CallExpCS")
ocl_cst_IteratorExpCS = Class(name="ocl::cst::IteratorExpCS")
LoopExpCS = Class(name="LoopExpCS")
ocl_cst_IterateExpCS = Class(name="ocl::cst::IterateExpCS")
ocl_cst_FeatureCallExpCS = Class(name="ocl::cst::FeatureCallExpCS")

# ocl_cst_CSTNode class attributes and methods
ocl_cst_CSTNode_startOffset: Property = Property(name="startOffset", type=IntegerType)
ocl_cst_CSTNode_endOffset: Property = Property(name="endOffset", type=IntegerType)
ocl_cst_CSTNode_startToken: Property = Property(name="startToken", type=StringType)
ocl_cst_CSTNode_endToken: Property = Property(name="endToken", type=StringType)
ocl_cst_CSTNode_ast: Property = Property(name="ast", type=StringType)
ocl_cst_CSTNode.attributes={ocl_cst_CSTNode_endToken, ocl_cst_CSTNode_startOffset, ocl_cst_CSTNode_ast, ocl_cst_CSTNode_startToken, ocl_cst_CSTNode_endOffset}

# OCLExpressionCS class attributes and methods

# ocl_cst_OCLExpressionCS class attributes and methods

# ocl_cst_ContextDeclCS class attributes and methods

# ocl_cst_PropertyContextCS class attributes and methods

# SimpleNameCS class attributes and methods

# InitOrDerValueCS class attributes and methods

# ocl_cst_SimpleNameCS class attributes and methods
ocl_cst_SimpleNameCS_value: Property = Property(name="value", type=StringType)
ocl_cst_SimpleNameCS_type: Property = Property(name="type", type=StringType)
ocl_cst_SimpleNameCS.attributes={ocl_cst_SimpleNameCS_type, ocl_cst_SimpleNameCS_value}

# ocl_cst_PackageDeclarationCS class attributes and methods

# CSTNode class attributes and methods

# PathNameCS class attributes and methods

# ContextDeclCS class attributes and methods

# PackageDeclarationCS class attributes and methods

# ocl_cst_PathNameCS class attributes and methods
ocl_cst_PathNameCS_sequenceOfNames: Property = Property(name="sequenceOfNames", type=StringType)
ocl_cst_PathNameCS.attributes={ocl_cst_PathNameCS_sequenceOfNames}

# TypeCS class attributes and methods

# ocl_cst_TypeCS class attributes and methods

# ocl_cst_InitOrDerValueCS class attributes and methods

# ocl_cst_ClassifierContextDeclCS class attributes and methods

# InvOrDefCS class attributes and methods

# ocl_cst_OperationCS class attributes and methods

# VariableCS class attributes and methods

# ocl_cst_InvOrDefCS class attributes and methods

# ocl_cst_OperationContextDeclCS class attributes and methods

# OperationCS class attributes and methods

# PrePostOrBodyDeclCS class attributes and methods

# ocl_cst_DerValueCS class attributes and methods

# ocl_cst_VariableCS class attributes and methods
ocl_cst_VariableCS_name: Property = Property(name="name", type=StringType)
ocl_cst_VariableCS.attributes={ocl_cst_VariableCS_name}

# ocl_cst_PrePostOrBodyDeclCS class attributes and methods
ocl_cst_PrePostOrBodyDeclCS_kind: Property = Property(name="kind", type=StringType)
ocl_cst_PrePostOrBodyDeclCS.attributes={ocl_cst_PrePostOrBodyDeclCS_kind}

# ocl_cst_DefExpressionCS class attributes and methods

# ocl_cst_VariableExpCS class attributes and methods

# ocl_cst_InitValueCS class attributes and methods

# ocl_cst_InvCS class attributes and methods

# ocl_cst_DefCS class attributes and methods

# DefExpressionCS class attributes and methods

# cst_TypeCS class attributes and methods

# ocl_cst_TupleTypeCS class attributes and methods

# ocl_cst_CollectionTypeCS class attributes and methods
ocl_cst_CollectionTypeCS_collectionTypeIdentifier: Property = Property(name="collectionTypeIdentifier", type=StringType)
ocl_cst_CollectionTypeCS.attributes={ocl_cst_CollectionTypeCS_collectionTypeIdentifier}

# IsMarkedPreCS class attributes and methods

# ocl_cst_IsMarkedPreCS class attributes and methods
ocl_cst_IsMarkedPreCS_pre: Property = Property(name="pre", type=BooleanType)
ocl_cst_IsMarkedPreCS.attributes={ocl_cst_IsMarkedPreCS_pre}

# ocl_cst_PrimitiveTypeCS class attributes and methods

# cst_SimpleNameCS class attributes and methods

# ocl_cst_MessageExpCS class attributes and methods
ocl_cst_MessageExpCS_kind: Property = Property(name="kind", type=StringType)
ocl_cst_MessageExpCS.attributes={ocl_cst_MessageExpCS_kind}

# ocl_cst_LetExpCS class attributes and methods

# ocl_cst_IfExpCS class attributes and methods

# ocl_cst_CollectionLiteralExpCS class attributes and methods
ocl_cst_CollectionLiteralExpCS_collectionType: Property = Property(name="collectionType", type=StringType)
ocl_cst_CollectionLiteralExpCS.attributes={ocl_cst_CollectionLiteralExpCS_collectionType}

# CollectionLiteralPartCS class attributes and methods

# ocl_cst_CollectionLiteralPartCS class attributes and methods

# ocl_cst_TupleLiteralExpCS class attributes and methods

# OCLMessageArgCS class attributes and methods

# ocl_cst_OCLMessageArgCS class attributes and methods

# ocl_cst_LiteralExpCS class attributes and methods

# ocl_cst_EnumLiteralExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# ocl_cst_InvalidLiteralExpCS class attributes and methods
ocl_cst_InvalidLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_InvalidLiteralExpCS.attributes={ocl_cst_InvalidLiteralExpCS_symbol}

# ocl_cst_CollectionRangeCS class attributes and methods

# ocl_cst_CallExpCS class attributes and methods
ocl_cst_CallExpCS_accessor: Property = Property(name="accessor", type=StringType)
ocl_cst_CallExpCS.attributes={ocl_cst_CallExpCS_accessor}

# ocl_cst_PrimitiveLiteralExpCS class attributes and methods
ocl_cst_PrimitiveLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_PrimitiveLiteralExpCS.attributes={ocl_cst_PrimitiveLiteralExpCS_symbol}

# ocl_cst_IntegerLiteralExpCS class attributes and methods
ocl_cst_IntegerLiteralExpCS_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_cst_IntegerLiteralExpCS.attributes={ocl_cst_IntegerLiteralExpCS_integerSymbol}

# PrimitiveLiteralExpCS class attributes and methods

# ocl_cst_UnlimitedNaturalLiteralExpCS class attributes and methods
ocl_cst_UnlimitedNaturalLiteralExpCS_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_cst_UnlimitedNaturalLiteralExpCS.attributes={ocl_cst_UnlimitedNaturalLiteralExpCS_integerSymbol}

# ocl_cst_RealLiteralExpCS class attributes and methods
ocl_cst_RealLiteralExpCS_realSymbol: Property = Property(name="realSymbol", type=StringType)
ocl_cst_RealLiteralExpCS.attributes={ocl_cst_RealLiteralExpCS_realSymbol}

# ocl_cst_StringLiteralExpCS class attributes and methods
ocl_cst_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
ocl_cst_StringLiteralExpCS_unescapedStringSymbol: Property = Property(name="unescapedStringSymbol", type=StringType)
ocl_cst_StringLiteralExpCS.attributes={ocl_cst_StringLiteralExpCS_stringSymbol, ocl_cst_StringLiteralExpCS_unescapedStringSymbol}

# ocl_cst_BooleanLiteralExpCS class attributes and methods
ocl_cst_BooleanLiteralExpCS_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
ocl_cst_BooleanLiteralExpCS.attributes={ocl_cst_BooleanLiteralExpCS_booleanSymbol}

# ocl_cst_NullLiteralExpCS class attributes and methods
ocl_cst_NullLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_NullLiteralExpCS.attributes={ocl_cst_NullLiteralExpCS_symbol}

# ocl_cst_OperationCallExpCS class attributes and methods

# FeatureCallExpCS class attributes and methods

# ocl_cst_StateExpCS class attributes and methods
ocl_cst_StateExpCS_sequenceOfNames: Property = Property(name="sequenceOfNames", type=StringType)
ocl_cst_StateExpCS.attributes={ocl_cst_StateExpCS_sequenceOfNames}

# ocl_cst_OCLDocumentCS class attributes and methods

# ocl_cst_LoopExpCS class attributes and methods

# CallExpCS class attributes and methods

# ocl_cst_IteratorExpCS class attributes and methods

# LoopExpCS class attributes and methods

# ocl_cst_IterateExpCS class attributes and methods

# ocl_cst_FeatureCallExpCS class attributes and methods

# Relationships
pathNameCS5: BinaryAssociation = BinaryAssociation(
    name="pathNameCS5",
    ends={
        Property(name="PathNameCS6", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS7: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS7",
    ends={
        Property(name="SimpleNameCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS8", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS9: BinaryAssociation = BinaryAssociation(
    name="typeCS9",
    ends={
        Property(name="TypeCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS10", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initOrDerValueCS11: BinaryAssociation = BinaryAssociation(
    name="initOrDerValueCS11",
    ends={
        Property(name="InitOrDerValueCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS12", type=InitOrDerValueCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathNameCS0: BinaryAssociation = BinaryAssociation(
    name="pathNameCS0",
    ends={
        Property(name="PathNameCS", type=ocl_cst_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PackageDeclarationCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextDecls1: BinaryAssociation = BinaryAssociation(
    name="contextDecls1",
    ends={
        Property(name="ContextDeclCS", type=ocl_cst_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PackageDeclarationCS2", type=ContextDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageDeclarationCS3: BinaryAssociation = BinaryAssociation(
    name="packageDeclarationCS3",
    ends={
        Property(name="PackageDeclarationCS", type=ocl_cst_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PackageDeclarationCS4", type=PackageDeclarationCS, multiplicity=Multiplicity(0, 1))
    }
)
initOrDerValueCS13: BinaryAssociation = BinaryAssociation(
    name="initOrDerValueCS13",
    ends={
        Property(name="InitOrDerValueCS14", type=ocl_cst_InitOrDerValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InitOrDerValueCS", type=InitOrDerValueCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCS15: BinaryAssociation = BinaryAssociation(
    name="expressionCS15",
    ends={
        Property(name="OCLExpressionCS", type=ocl_cst_InitOrDerValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InitOrDerValueCS16", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints21: BinaryAssociation = BinaryAssociation(
    name="constraints21",
    ends={
        Property(name="InvOrDefCS23", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS22", type=InvOrDefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathNameCS17: BinaryAssociation = BinaryAssociation(
    name="pathNameCS17",
    ends={
        Property(name="PathNameCS18", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invOrDefCS19: BinaryAssociation = BinaryAssociation(
    name="invOrDefCS19",
    ends={
        Property(name="InvOrDefCS", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS20", type=InvOrDefCS, multiplicity=Multiplicity(0, 1))
    }
)
pathNameCS32: BinaryAssociation = BinaryAssociation(
    name="pathNameCS32",
    ends={
        Property(name="PathNameCS33", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS34: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS34",
    ends={
        Property(name="SimpleNameCS36", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS35", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters37: BinaryAssociation = BinaryAssociation(
    name="parameters37",
    ends={
        Property(name="VariableCS", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS38", type=VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS24: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS24",
    ends={
        Property(name="SimpleNameCS25", type=ocl_cst_InvOrDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvOrDefCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invOrDefCS26: BinaryAssociation = BinaryAssociation(
    name="invOrDefCS26",
    ends={
        Property(name="InvOrDefCS28", type=ocl_cst_InvOrDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvOrDefCS27", type=InvOrDefCS, multiplicity=Multiplicity(0, 1))
    }
)
operationCS29: BinaryAssociation = BinaryAssociation(
    name="operationCS29",
    ends={
        Property(name="OperationCS", type=ocl_cst_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationContextDeclCS", type=OperationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prePostOrBodyDecls30: BinaryAssociation = BinaryAssociation(
    name="prePostOrBodyDecls30",
    ends={
        Property(name="PrePostOrBodyDeclCS", type=ocl_cst_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationContextDeclCS31", type=PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
simpleNameCS47: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS47",
    ends={
        Property(name="SimpleNameCS48", type=ocl_cst_PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PrePostOrBodyDeclCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCS49: BinaryAssociation = BinaryAssociation(
    name="expressionCS49",
    ends={
        Property(name="OCLExpressionCS51", type=ocl_cst_PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PrePostOrBodyDeclCS50", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS39: BinaryAssociation = BinaryAssociation(
    name="typeCS39",
    ends={
        Property(name="TypeCS41", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS40", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS42: BinaryAssociation = BinaryAssociation(
    name="typeCS42",
    ends={
        Property(name="TypeCS43", type=ocl_cst_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression44: BinaryAssociation = BinaryAssociation(
    name="initExpression44",
    ends={
        Property(name="OCLExpressionCS46", type=ocl_cst_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableCS45", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationCS55: BinaryAssociation = BinaryAssociation(
    name="operationCS55",
    ends={
        Property(name="OperationCS56", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS", type=OperationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableCS57: BinaryAssociation = BinaryAssociation(
    name="variableCS57",
    ends={
        Property(name="VariableCS59", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS58", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCS60: BinaryAssociation = BinaryAssociation(
    name="expressionCS60",
    ends={
        Property(name="OCLExpressionCS62", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS61", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCS52: BinaryAssociation = BinaryAssociation(
    name="expressionCS52",
    ends={
        Property(name="OCLExpressionCS53", type=ocl_cst_InvCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defExpressionCS54: BinaryAssociation = BinaryAssociation(
    name="defExpressionCS54",
    ends={
        Property(name="DefExpressionCS", type=ocl_cst_DefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefCS", type=DefExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables70: BinaryAssociation = BinaryAssociation(
    name="variables70",
    ends={
        Property(name="VariableCS71", type=ocl_cst_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_TupleTypeCS", type=VariableCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arguments63: BinaryAssociation = BinaryAssociation(
    name="arguments63",
    ends={
        Property(name="OCLExpressionCS64", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS65: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS65",
    ends={
        Property(name="SimpleNameCS67", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS66", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isMarkedPreCS68: BinaryAssociation = BinaryAssociation(
    name="isMarkedPreCS68",
    ends={
        Property(name="IsMarkedPreCS", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS69", type=IsMarkedPreCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression79: BinaryAssociation = BinaryAssociation(
    name="thenExpression79",
    ends={
        Property(name="OCLExpressionCS80", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression81: BinaryAssociation = BinaryAssociation(
    name="elseExpression81",
    ends={
        Property(name="OCLExpressionCS83", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS82", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="OCLExpressionCS86", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS85", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target87: BinaryAssociation = BinaryAssociation(
    name="target87",
    ends={
        Property(name="OCLExpressionCS88", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS72: BinaryAssociation = BinaryAssociation(
    name="typeCS72",
    ends={
        Property(name="TypeCS73", type=ocl_cst_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables74: BinaryAssociation = BinaryAssociation(
    name="variables74",
    ends={
        Property(name="VariableCS75", type=ocl_cst_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LetExpCS", type=VariableCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inExpression76: BinaryAssociation = BinaryAssociation(
    name="inExpression76",
    ends={
        Property(name="OCLExpressionCS78", type=ocl_cst_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LetExpCS77", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathNameCS99: BinaryAssociation = BinaryAssociation(
    name="pathNameCS99",
    ends={
        Property(name="PathNameCS100", type=ocl_cst_EnumLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_EnumLiteralExpCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS101: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS101",
    ends={
        Property(name="SimpleNameCS103", type=ocl_cst_EnumLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_EnumLiteralExpCS102", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionLiteralParts104: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts104",
    ends={
        Property(name="CollectionLiteralPartCS", type=ocl_cst_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionLiteralExpCS", type=CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionCS105: BinaryAssociation = BinaryAssociation(
    name="expressionCS105",
    ends={
        Property(name="OCLExpressionCS106", type=ocl_cst_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionLiteralPartCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS89: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS89",
    ends={
        Property(name="SimpleNameCS91", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS90", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments92: BinaryAssociation = BinaryAssociation(
    name="arguments92",
    ends={
        Property(name="OCLMessageArgCS", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS93", type=OCLMessageArgCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS94: BinaryAssociation = BinaryAssociation(
    name="typeCS94",
    ends={
        Property(name="TypeCS95", type=ocl_cst_OCLMessageArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLMessageArgCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression96: BinaryAssociation = BinaryAssociation(
    name="expression96",
    ends={
        Property(name="OCLExpressionCS98", type=ocl_cst_OCLMessageArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLMessageArgCS97", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastExpressionCS109: BinaryAssociation = BinaryAssociation(
    name="lastExpressionCS109",
    ends={
        Property(name="OCLExpressionCS110", type=ocl_cst_CollectionRangeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionRangeCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source111: BinaryAssociation = BinaryAssociation(
    name="source111",
    ends={
        Property(name="OCLExpressionCS112", type=ocl_cst_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CallExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS113: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS113",
    ends={
        Property(name="SimpleNameCS115", type=ocl_cst_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CallExpCS114", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables107: BinaryAssociation = BinaryAssociation(
    name="variables107",
    ends={
        Property(name="VariableCS108", type=ocl_cst_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_TupleLiteralExpCS", type=VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments124: BinaryAssociation = BinaryAssociation(
    name="arguments124",
    ends={
        Property(name="OCLExpressionCS125", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isMarkedPreCS126: BinaryAssociation = BinaryAssociation(
    name="isMarkedPreCS126",
    ends={
        Property(name="IsMarkedPreCS128", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS127", type=IsMarkedPreCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageDeclarations129: BinaryAssociation = BinaryAssociation(
    name="packageDeclarations129",
    ends={
        Property(name="PackageDeclarationCS130", type=ocl_cst_OCLDocumentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLDocumentCS", type=PackageDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable1116: BinaryAssociation = BinaryAssociation(
    name="variable1116",
    ends={
        Property(name="VariableCS117", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable2118: BinaryAssociation = BinaryAssociation(
    name="variable2118",
    ends={
        Property(name="VariableCS120", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS119", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body121: BinaryAssociation = BinaryAssociation(
    name="body121",
    ends={
        Property(name="OCLExpressionCS123", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS122", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ocl_cst_TypeCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_TypeCS)
gen_ocl_cst_OCLExpressionCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLExpressionCS)
gen_ocl_cst_ContextDeclCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_ContextDeclCS)
gen_ocl_cst_PropertyContextCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_PropertyContextCS)
gen_ocl_cst_SimpleNameCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_SimpleNameCS)
gen_ocl_cst_PackageDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_PackageDeclarationCS)
gen_ocl_cst_PathNameCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_PathNameCS)
gen_ocl_cst_InitOrDerValueCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_InitOrDerValueCS)
gen_ocl_cst_ClassifierContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_ClassifierContextDeclCS)
gen_ocl_cst_OperationCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OperationCS)
gen_ocl_cst_InvOrDefCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_InvOrDefCS)
gen_ocl_cst_OperationContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_OperationContextDeclCS)
gen_ocl_cst_DerValueCS_InitOrDerValueCS = Generalization(general=InitOrDerValueCS, specific=ocl_cst_DerValueCS)
gen_ocl_cst_VariableCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_VariableCS)
gen_ocl_cst_PrePostOrBodyDeclCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_PrePostOrBodyDeclCS)
gen_ocl_cst_DefExpressionCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_DefExpressionCS)
gen_ocl_cst_VariableExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_VariableExpCS)
gen_ocl_cst_InitValueCS_InitOrDerValueCS = Generalization(general=InitOrDerValueCS, specific=ocl_cst_InitValueCS)
gen_ocl_cst_InvCS_InvOrDefCS = Generalization(general=InvOrDefCS, specific=ocl_cst_InvCS)
gen_ocl_cst_DefCS_InvOrDefCS = Generalization(general=InvOrDefCS, specific=ocl_cst_DefCS)
gen_ocl_cst_PrimitiveTypeCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_PrimitiveTypeCS)
gen_ocl_cst_PrimitiveTypeCS_cst_TypeCS = Generalization(general=cst_TypeCS, specific=ocl_cst_PrimitiveTypeCS)
gen_ocl_cst_TupleTypeCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_TupleTypeCS)
gen_ocl_cst_CollectionTypeCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_CollectionTypeCS)
gen_ocl_cst_IsMarkedPreCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_IsMarkedPreCS)
gen_ocl_cst_MessageExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_MessageExpCS)
gen_ocl_cst_LetExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_LetExpCS)
gen_ocl_cst_IfExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_IfExpCS)
gen_ocl_cst_EnumLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_EnumLiteralExpCS)
gen_ocl_cst_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_CollectionLiteralExpCS)
gen_ocl_cst_CollectionLiteralPartCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_CollectionLiteralPartCS)
gen_ocl_cst_TupleLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_TupleLiteralExpCS)
gen_ocl_cst_OCLMessageArgCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLMessageArgCS)
gen_ocl_cst_LiteralExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_LiteralExpCS)
gen_ocl_cst_NullLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_NullLiteralExpCS)
gen_ocl_cst_InvalidLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_InvalidLiteralExpCS)
gen_ocl_cst_CollectionRangeCS_CollectionLiteralPartCS = Generalization(general=CollectionLiteralPartCS, specific=ocl_cst_CollectionRangeCS)
gen_ocl_cst_CallExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_CallExpCS)
gen_ocl_cst_PrimitiveLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_PrimitiveLiteralExpCS)
gen_ocl_cst_IntegerLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_IntegerLiteralExpCS)
gen_ocl_cst_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_UnlimitedNaturalLiteralExpCS)
gen_ocl_cst_RealLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_RealLiteralExpCS)
gen_ocl_cst_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_StringLiteralExpCS)
gen_ocl_cst_BooleanLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_BooleanLiteralExpCS)
gen_ocl_cst_OperationCallExpCS_FeatureCallExpCS = Generalization(general=FeatureCallExpCS, specific=ocl_cst_OperationCallExpCS)
gen_ocl_cst_StateExpCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_StateExpCS)
gen_ocl_cst_OCLDocumentCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLDocumentCS)
gen_ocl_cst_LoopExpCS_CallExpCS = Generalization(general=CallExpCS, specific=ocl_cst_LoopExpCS)
gen_ocl_cst_IteratorExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=ocl_cst_IteratorExpCS)
gen_ocl_cst_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=ocl_cst_IterateExpCS)
gen_ocl_cst_FeatureCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=ocl_cst_FeatureCallExpCS)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ocl_cst_CSTNode, OCLExpressionCS, ocl_cst_OCLExpressionCS, ocl_cst_ContextDeclCS, ocl_cst_PropertyContextCS, SimpleNameCS, InitOrDerValueCS, ocl_cst_SimpleNameCS, ocl_cst_PackageDeclarationCS, CSTNode, PathNameCS, ContextDeclCS, PackageDeclarationCS, ocl_cst_PathNameCS, TypeCS, ocl_cst_TypeCS, ocl_cst_InitOrDerValueCS, ocl_cst_ClassifierContextDeclCS, InvOrDefCS, ocl_cst_OperationCS, VariableCS, ocl_cst_InvOrDefCS, ocl_cst_OperationContextDeclCS, OperationCS, PrePostOrBodyDeclCS, ocl_cst_DerValueCS, ocl_cst_VariableCS, ocl_cst_PrePostOrBodyDeclCS, ocl_cst_DefExpressionCS, ocl_cst_VariableExpCS, ocl_cst_InitValueCS, ocl_cst_InvCS, ocl_cst_DefCS, DefExpressionCS, cst_TypeCS, ocl_cst_TupleTypeCS, ocl_cst_CollectionTypeCS, IsMarkedPreCS, ocl_cst_IsMarkedPreCS, ocl_cst_PrimitiveTypeCS, cst_SimpleNameCS, ocl_cst_MessageExpCS, ocl_cst_LetExpCS, ocl_cst_IfExpCS, ocl_cst_CollectionLiteralExpCS, CollectionLiteralPartCS, ocl_cst_CollectionLiteralPartCS, ocl_cst_TupleLiteralExpCS, OCLMessageArgCS, ocl_cst_OCLMessageArgCS, ocl_cst_LiteralExpCS, ocl_cst_EnumLiteralExpCS, LiteralExpCS, ocl_cst_InvalidLiteralExpCS, ocl_cst_CollectionRangeCS, ocl_cst_CallExpCS, ocl_cst_PrimitiveLiteralExpCS, ocl_cst_IntegerLiteralExpCS, PrimitiveLiteralExpCS, ocl_cst_UnlimitedNaturalLiteralExpCS, ocl_cst_RealLiteralExpCS, ocl_cst_StringLiteralExpCS, ocl_cst_BooleanLiteralExpCS, ocl_cst_NullLiteralExpCS, ocl_cst_OperationCallExpCS, FeatureCallExpCS, ocl_cst_StateExpCS, ocl_cst_OCLDocumentCS, ocl_cst_LoopExpCS, CallExpCS, ocl_cst_IteratorExpCS, LoopExpCS, ocl_cst_IterateExpCS, ocl_cst_FeatureCallExpCS, SimpleTypeEnum, PrePostOrBodyEnum, CollectionTypeIdentifierEnum, MessageExpKind, DotOrArrowEnum},
    associations={pathNameCS5, simpleNameCS7, typeCS9, initOrDerValueCS11, pathNameCS0, contextDecls1, packageDeclarationCS3, initOrDerValueCS13, expressionCS15, constraints21, pathNameCS17, invOrDefCS19, pathNameCS32, simpleNameCS34, parameters37, simpleNameCS24, invOrDefCS26, operationCS29, prePostOrBodyDecls30, simpleNameCS47, expressionCS49, typeCS39, typeCS42, initExpression44, operationCS55, variableCS57, expressionCS60, expressionCS52, defExpressionCS54, variables70, arguments63, simpleNameCS65, isMarkedPreCS68, thenExpression79, elseExpression81, condition84, target87, typeCS72, variables74, inExpression76, pathNameCS99, simpleNameCS101, collectionLiteralParts104, expressionCS105, simpleNameCS89, arguments92, typeCS94, expression96, lastExpressionCS109, source111, simpleNameCS113, variables107, arguments124, isMarkedPreCS126, packageDeclarations129, variable1116, variable2118, body121},
    generalizations={gen_ocl_cst_TypeCS_OCLExpressionCS, gen_ocl_cst_OCLExpressionCS_CSTNode, gen_ocl_cst_ContextDeclCS_CSTNode, gen_ocl_cst_PropertyContextCS_ContextDeclCS, gen_ocl_cst_SimpleNameCS_OCLExpressionCS, gen_ocl_cst_PackageDeclarationCS_CSTNode, gen_ocl_cst_PathNameCS_TypeCS, gen_ocl_cst_InitOrDerValueCS_CSTNode, gen_ocl_cst_ClassifierContextDeclCS_ContextDeclCS, gen_ocl_cst_OperationCS_CSTNode, gen_ocl_cst_InvOrDefCS_CSTNode, gen_ocl_cst_OperationContextDeclCS_ContextDeclCS, gen_ocl_cst_DerValueCS_InitOrDerValueCS, gen_ocl_cst_VariableCS_CSTNode, gen_ocl_cst_PrePostOrBodyDeclCS_CSTNode, gen_ocl_cst_DefExpressionCS_CSTNode, gen_ocl_cst_VariableExpCS_OCLExpressionCS, gen_ocl_cst_InitValueCS_InitOrDerValueCS, gen_ocl_cst_InvCS_InvOrDefCS, gen_ocl_cst_DefCS_InvOrDefCS, gen_ocl_cst_PrimitiveTypeCS_cst_SimpleNameCS, gen_ocl_cst_PrimitiveTypeCS_cst_TypeCS, gen_ocl_cst_TupleTypeCS_TypeCS, gen_ocl_cst_CollectionTypeCS_TypeCS, gen_ocl_cst_IsMarkedPreCS_CSTNode, gen_ocl_cst_MessageExpCS_OCLExpressionCS, gen_ocl_cst_LetExpCS_OCLExpressionCS, gen_ocl_cst_IfExpCS_OCLExpressionCS, gen_ocl_cst_EnumLiteralExpCS_LiteralExpCS, gen_ocl_cst_CollectionLiteralExpCS_LiteralExpCS, gen_ocl_cst_CollectionLiteralPartCS_CSTNode, gen_ocl_cst_TupleLiteralExpCS_LiteralExpCS, gen_ocl_cst_OCLMessageArgCS_CSTNode, gen_ocl_cst_LiteralExpCS_OCLExpressionCS, gen_ocl_cst_NullLiteralExpCS_LiteralExpCS, gen_ocl_cst_InvalidLiteralExpCS_LiteralExpCS, gen_ocl_cst_CollectionRangeCS_CollectionLiteralPartCS, gen_ocl_cst_CallExpCS_OCLExpressionCS, gen_ocl_cst_PrimitiveLiteralExpCS_LiteralExpCS, gen_ocl_cst_IntegerLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_RealLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_BooleanLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_OperationCallExpCS_FeatureCallExpCS, gen_ocl_cst_StateExpCS_TypeCS, gen_ocl_cst_OCLDocumentCS_CSTNode, gen_ocl_cst_LoopExpCS_CallExpCS, gen_ocl_cst_IteratorExpCS_LoopExpCS, gen_ocl_cst_IterateExpCS_LoopExpCS, gen_ocl_cst_FeatureCallExpCS_CallExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)