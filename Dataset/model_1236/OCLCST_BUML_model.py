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
            EnumerationLiteral(name="identifier"),
			EnumerationLiteral(name="self"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="OclAny"),
			EnumerationLiteral(name="OclVoid"),
			EnumerationLiteral(name="OclInvalid"),
			EnumerationLiteral(name="OclMessage"),
			EnumerationLiteral(name="keyword"),
			EnumerationLiteral(name="UnlimitedNatural")
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

MessageExpKind: Enumeration = Enumeration(
    name="MessageExpKind",
    literals={
            EnumerationLiteral(name="hasSent"),
			EnumerationLiteral(name="sent")
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

# Classes
ContextDeclCS = Class(name="ContextDeclCS")
PackageDeclarationCS = Class(name="PackageDeclarationCS")
ocl_cst_CSTNode = Class(name="ocl::cst::CSTNode", is_abstract=True)
ocl_cst_PackageDeclarationCS = Class(name="ocl::cst::PackageDeclarationCS")
CSTNode = Class(name="CSTNode")
PathNameCS = Class(name="PathNameCS")
ocl_cst_PathNameCS = Class(name="ocl::cst::PathNameCS")
TypeCS = Class(name="TypeCS")
SimpleNameCS = Class(name="SimpleNameCS")
ocl_cst_TypeCS = Class(name="ocl::cst::TypeCS", is_abstract=True)
OCLExpressionCS = Class(name="OCLExpressionCS")
ocl_cst_OCLExpressionCS = Class(name="ocl::cst::OCLExpressionCS", is_abstract=True)
ocl_cst_SimpleNameCS = Class(name="ocl::cst::SimpleNameCS")
ocl_cst_ContextDeclCS = Class(name="ocl::cst::ContextDeclCS", is_abstract=True)
ocl_cst_PropertyContextCS = Class(name="ocl::cst::PropertyContextCS")
InvOrDefCS = Class(name="InvOrDefCS")
ocl_cst_InvOrDefCS = Class(name="ocl::cst::InvOrDefCS", is_abstract=True)
InitOrDerValueCS = Class(name="InitOrDerValueCS")
ocl_cst_InitOrDerValueCS = Class(name="ocl::cst::InitOrDerValueCS", is_abstract=True)
ocl_cst_ClassifierContextDeclCS = Class(name="ocl::cst::ClassifierContextDeclCS")
ocl_cst_DerValueCS = Class(name="ocl::cst::DerValueCS")
ocl_cst_InitValueCS = Class(name="ocl::cst::InitValueCS")
ocl_cst_OperationContextDeclCS = Class(name="ocl::cst::OperationContextDeclCS")
OperationCS = Class(name="OperationCS")
PrePostOrBodyDeclCS = Class(name="PrePostOrBodyDeclCS")
ocl_cst_OperationCS = Class(name="ocl::cst::OperationCS")
VariableCS = Class(name="VariableCS")
ocl_cst_VariableCS = Class(name="ocl::cst::VariableCS")
ocl_cst_PrePostOrBodyDeclCS = Class(name="ocl::cst::PrePostOrBodyDeclCS")
ocl_cst_CollectionTypeCS = Class(name="ocl::cst::CollectionTypeCS")
ocl_cst_InvCS = Class(name="ocl::cst::InvCS")
ocl_cst_DefCS = Class(name="ocl::cst::DefCS")
DefExpressionCS = Class(name="DefExpressionCS")
ocl_cst_DefExpressionCS = Class(name="ocl::cst::DefExpressionCS")
ocl_cst_VariableExpCS = Class(name="ocl::cst::VariableExpCS")
IsMarkedPreCS = Class(name="IsMarkedPreCS")
ocl_cst_IsMarkedPreCS = Class(name="ocl::cst::IsMarkedPreCS")
ocl_cst_PrimitiveTypeCS = Class(name="ocl::cst::PrimitiveTypeCS")
cst_SimpleNameCS = Class(name="cst::SimpleNameCS")
cst_TypeCS = Class(name="cst::TypeCS")
ocl_cst_TupleTypeCS = Class(name="ocl::cst::TupleTypeCS")
OCLMessageArgCS = Class(name="OCLMessageArgCS")
ocl_cst_LetExpCS = Class(name="ocl::cst::LetExpCS")
ocl_cst_IfExpCS = Class(name="ocl::cst::IfExpCS")
ocl_cst_MessageExpCS = Class(name="ocl::cst::MessageExpCS")
ocl_cst_PrimitiveLiteralExpCS = Class(name="ocl::cst::PrimitiveLiteralExpCS")
ocl_cst_IntegerLiteralExpCS = Class(name="ocl::cst::IntegerLiteralExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
ocl_cst_OCLMessageArgCS = Class(name="ocl::cst::OCLMessageArgCS")
ocl_cst_LiteralExpCS = Class(name="ocl::cst::LiteralExpCS", is_abstract=True)
ocl_cst_CollectionLiteralExpCS = Class(name="ocl::cst::CollectionLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
CollectionLiteralPartCS = Class(name="CollectionLiteralPartCS")
ocl_cst_CollectionLiteralPartCS = Class(name="ocl::cst::CollectionLiteralPartCS")
ocl_cst_TupleLiteralExpCS = Class(name="ocl::cst::TupleLiteralExpCS")
ocl_cst_UnlimitedNaturalLiteralExpCS = Class(name="ocl::cst::UnlimitedNaturalLiteralExpCS")
ocl_cst_RealLiteralExpCS = Class(name="ocl::cst::RealLiteralExpCS")
ocl_cst_StringLiteralExpCS = Class(name="ocl::cst::StringLiteralExpCS")
ocl_cst_BooleanLiteralExpCS = Class(name="ocl::cst::BooleanLiteralExpCS")
cst_PrimitiveLiteralExpCS = Class(name="cst::PrimitiveLiteralExpCS")
ocl_cst_NullLiteralExpCS = Class(name="ocl::cst::NullLiteralExpCS")
cst_LiteralExpCS = Class(name="cst::LiteralExpCS")
ocl_cst_InvalidLiteralExpCS = Class(name="ocl::cst::InvalidLiteralExpCS")
ocl_cst_CollectionRangeCS = Class(name="ocl::cst::CollectionRangeCS")
ocl_cst_CallExpCS = Class(name="ocl::cst::CallExpCS")
ocl_cst_OCLDocumentCS = Class(name="ocl::cst::OCLDocumentCS")
ocl_cst_LoopExpCS = Class(name="ocl::cst::LoopExpCS")
CallExpCS = Class(name="CallExpCS")
ocl_cst_IteratorExpCS = Class(name="ocl::cst::IteratorExpCS")
LoopExpCS = Class(name="LoopExpCS")
ocl_cst_IterateExpCS = Class(name="ocl::cst::IterateExpCS")
ocl_cst_FeatureCallExpCS = Class(name="ocl::cst::FeatureCallExpCS")
ocl_cst_OperationCallExpCS = Class(name="ocl::cst::OperationCallExpCS")
FeatureCallExpCS = Class(name="FeatureCallExpCS")

# ContextDeclCS class attributes and methods

# PackageDeclarationCS class attributes and methods

# ocl_cst_CSTNode class attributes and methods
ocl_cst_CSTNode_startOffset: Property = Property(name="startOffset", type=IntegerType)
ocl_cst_CSTNode_endOffset: Property = Property(name="endOffset", type=IntegerType)
ocl_cst_CSTNode_startToken: Property = Property(name="startToken", type=StringType)
ocl_cst_CSTNode_endToken: Property = Property(name="endToken", type=StringType)
ocl_cst_CSTNode_ast: Property = Property(name="ast", type=StringType)
ocl_cst_CSTNode.attributes={ocl_cst_CSTNode_startOffset, ocl_cst_CSTNode_endOffset, ocl_cst_CSTNode_endToken, ocl_cst_CSTNode_startToken, ocl_cst_CSTNode_ast}

# ocl_cst_PackageDeclarationCS class attributes and methods

# CSTNode class attributes and methods

# PathNameCS class attributes and methods

# ocl_cst_PathNameCS class attributes and methods

# TypeCS class attributes and methods

# SimpleNameCS class attributes and methods

# ocl_cst_TypeCS class attributes and methods

# OCLExpressionCS class attributes and methods

# ocl_cst_OCLExpressionCS class attributes and methods

# ocl_cst_SimpleNameCS class attributes and methods
ocl_cst_SimpleNameCS_value: Property = Property(name="value", type=StringType)
ocl_cst_SimpleNameCS_type: Property = Property(name="type", type=StringType)
ocl_cst_SimpleNameCS.attributes={ocl_cst_SimpleNameCS_value, ocl_cst_SimpleNameCS_type}

# ocl_cst_ContextDeclCS class attributes and methods

# ocl_cst_PropertyContextCS class attributes and methods

# InvOrDefCS class attributes and methods

# ocl_cst_InvOrDefCS class attributes and methods

# InitOrDerValueCS class attributes and methods

# ocl_cst_InitOrDerValueCS class attributes and methods

# ocl_cst_ClassifierContextDeclCS class attributes and methods

# ocl_cst_DerValueCS class attributes and methods

# ocl_cst_InitValueCS class attributes and methods

# ocl_cst_OperationContextDeclCS class attributes and methods

# OperationCS class attributes and methods

# PrePostOrBodyDeclCS class attributes and methods

# ocl_cst_OperationCS class attributes and methods

# VariableCS class attributes and methods

# ocl_cst_VariableCS class attributes and methods
ocl_cst_VariableCS_name: Property = Property(name="name", type=StringType)
ocl_cst_VariableCS.attributes={ocl_cst_VariableCS_name}

# ocl_cst_PrePostOrBodyDeclCS class attributes and methods
ocl_cst_PrePostOrBodyDeclCS_kind: Property = Property(name="kind", type=StringType)
ocl_cst_PrePostOrBodyDeclCS.attributes={ocl_cst_PrePostOrBodyDeclCS_kind}

# ocl_cst_CollectionTypeCS class attributes and methods
ocl_cst_CollectionTypeCS_collectionTypeIdentifier: Property = Property(name="collectionTypeIdentifier", type=StringType)
ocl_cst_CollectionTypeCS.attributes={ocl_cst_CollectionTypeCS_collectionTypeIdentifier}

# ocl_cst_InvCS class attributes and methods

# ocl_cst_DefCS class attributes and methods
ocl_cst_DefCS_static: Property = Property(name="static", type=BooleanType)
ocl_cst_DefCS.attributes={ocl_cst_DefCS_static}

# DefExpressionCS class attributes and methods

# ocl_cst_DefExpressionCS class attributes and methods

# ocl_cst_VariableExpCS class attributes and methods

# IsMarkedPreCS class attributes and methods

# ocl_cst_IsMarkedPreCS class attributes and methods

# ocl_cst_PrimitiveTypeCS class attributes and methods

# cst_SimpleNameCS class attributes and methods

# cst_TypeCS class attributes and methods

# ocl_cst_TupleTypeCS class attributes and methods

# OCLMessageArgCS class attributes and methods

# ocl_cst_LetExpCS class attributes and methods

# ocl_cst_IfExpCS class attributes and methods

# ocl_cst_MessageExpCS class attributes and methods
ocl_cst_MessageExpCS_kind: Property = Property(name="kind", type=StringType)
ocl_cst_MessageExpCS.attributes={ocl_cst_MessageExpCS_kind}

# ocl_cst_PrimitiveLiteralExpCS class attributes and methods
ocl_cst_PrimitiveLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
ocl_cst_PrimitiveLiteralExpCS.attributes={ocl_cst_PrimitiveLiteralExpCS_symbol}

# ocl_cst_IntegerLiteralExpCS class attributes and methods
ocl_cst_IntegerLiteralExpCS_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_cst_IntegerLiteralExpCS_extendedIntegerSymbol: Property = Property(name="extendedIntegerSymbol", type=StringType)
ocl_cst_IntegerLiteralExpCS_longSymbol: Property = Property(name="longSymbol", type=StringType)
ocl_cst_IntegerLiteralExpCS.attributes={ocl_cst_IntegerLiteralExpCS_longSymbol, ocl_cst_IntegerLiteralExpCS_integerSymbol, ocl_cst_IntegerLiteralExpCS_extendedIntegerSymbol}

# PrimitiveLiteralExpCS class attributes and methods

# ocl_cst_OCLMessageArgCS class attributes and methods

# ocl_cst_LiteralExpCS class attributes and methods

# ocl_cst_CollectionLiteralExpCS class attributes and methods
ocl_cst_CollectionLiteralExpCS_collectionType: Property = Property(name="collectionType", type=StringType)
ocl_cst_CollectionLiteralExpCS.attributes={ocl_cst_CollectionLiteralExpCS_collectionType}

# LiteralExpCS class attributes and methods

# CollectionLiteralPartCS class attributes and methods

# ocl_cst_CollectionLiteralPartCS class attributes and methods

# ocl_cst_TupleLiteralExpCS class attributes and methods

# ocl_cst_UnlimitedNaturalLiteralExpCS class attributes and methods
ocl_cst_UnlimitedNaturalLiteralExpCS_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
ocl_cst_UnlimitedNaturalLiteralExpCS_extendedIntegerSymbol: Property = Property(name="extendedIntegerSymbol", type=StringType)
ocl_cst_UnlimitedNaturalLiteralExpCS_longSymbol: Property = Property(name="longSymbol", type=StringType)
ocl_cst_UnlimitedNaturalLiteralExpCS.attributes={ocl_cst_UnlimitedNaturalLiteralExpCS_longSymbol, ocl_cst_UnlimitedNaturalLiteralExpCS_integerSymbol, ocl_cst_UnlimitedNaturalLiteralExpCS_extendedIntegerSymbol}

# ocl_cst_RealLiteralExpCS class attributes and methods
ocl_cst_RealLiteralExpCS_realSymbol: Property = Property(name="realSymbol", type=StringType)
ocl_cst_RealLiteralExpCS.attributes={ocl_cst_RealLiteralExpCS_realSymbol}

# ocl_cst_StringLiteralExpCS class attributes and methods
ocl_cst_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
ocl_cst_StringLiteralExpCS_unescapedStringSymbol: Property = Property(name="unescapedStringSymbol", type=StringType)
ocl_cst_StringLiteralExpCS.attributes={ocl_cst_StringLiteralExpCS_unescapedStringSymbol, ocl_cst_StringLiteralExpCS_stringSymbol}

# ocl_cst_BooleanLiteralExpCS class attributes and methods
ocl_cst_BooleanLiteralExpCS_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
ocl_cst_BooleanLiteralExpCS.attributes={ocl_cst_BooleanLiteralExpCS_booleanSymbol}

# cst_PrimitiveLiteralExpCS class attributes and methods

# ocl_cst_NullLiteralExpCS class attributes and methods

# cst_LiteralExpCS class attributes and methods

# ocl_cst_InvalidLiteralExpCS class attributes and methods

# ocl_cst_CollectionRangeCS class attributes and methods

# ocl_cst_CallExpCS class attributes and methods
ocl_cst_CallExpCS_accessor: Property = Property(name="accessor", type=StringType)
ocl_cst_CallExpCS.attributes={ocl_cst_CallExpCS_accessor}

# ocl_cst_OCLDocumentCS class attributes and methods

# ocl_cst_LoopExpCS class attributes and methods

# CallExpCS class attributes and methods

# ocl_cst_IteratorExpCS class attributes and methods

# LoopExpCS class attributes and methods

# ocl_cst_IterateExpCS class attributes and methods

# ocl_cst_FeatureCallExpCS class attributes and methods

# ocl_cst_OperationCallExpCS class attributes and methods
ocl_cst_OperationCallExpCS_isAtomic: Property = Property(name="isAtomic", type=StringType)
ocl_cst_OperationCallExpCS.attributes={ocl_cst_OperationCallExpCS_isAtomic}

# FeatureCallExpCS class attributes and methods

# Relationships
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
pathNameCS0: BinaryAssociation = BinaryAssociation(
    name="pathNameCS0",
    ends={
        Property(name="PathNameCS", type=ocl_cst_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PackageDeclarationCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNames5: BinaryAssociation = BinaryAssociation(
    name="simpleNames5",
    ends={
        Property(name="SimpleNameCS", type=ocl_cst_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PathNameCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathNameCS6: BinaryAssociation = BinaryAssociation(
    name="pathNameCS6",
    ends={
        Property(name="PathNameCS7", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS8: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS8",
    ends={
        Property(name="SimpleNameCS10", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS9", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS11: BinaryAssociation = BinaryAssociation(
    name="typeCS11",
    ends={
        Property(name="TypeCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS12", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints18: BinaryAssociation = BinaryAssociation(
    name="constraints18",
    ends={
        Property(name="InvOrDefCS", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS19", type=InvOrDefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS20: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS20",
    ends={
        Property(name="SimpleNameCS22", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS21", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints13: BinaryAssociation = BinaryAssociation(
    name="constraints13",
    ends={
        Property(name="InitOrDerValueCS", type=ocl_cst_PropertyContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PropertyContextCS14", type=InitOrDerValueCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionCS15: BinaryAssociation = BinaryAssociation(
    name="expressionCS15",
    ends={
        Property(name="OCLExpressionCS", type=ocl_cst_InitOrDerValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InitOrDerValueCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathNameCS16: BinaryAssociation = BinaryAssociation(
    name="pathNameCS16",
    ends={
        Property(name="PathNameCS17", type=ocl_cst_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_ClassifierContextDeclCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS23: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS23",
    ends={
        Property(name="SimpleNameCS24", type=ocl_cst_InvOrDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvOrDefCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationCS25: BinaryAssociation = BinaryAssociation(
    name="operationCS25",
    ends={
        Property(name="OperationCS", type=ocl_cst_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationContextDeclCS", type=OperationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prePostOrBodyDecls26: BinaryAssociation = BinaryAssociation(
    name="prePostOrBodyDecls26",
    ends={
        Property(name="PrePostOrBodyDeclCS", type=ocl_cst_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationContextDeclCS27", type=PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pathNameCS28: BinaryAssociation = BinaryAssociation(
    name="pathNameCS28",
    ends={
        Property(name="PathNameCS29", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS30: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS30",
    ends={
        Property(name="SimpleNameCS32", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS31", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters33: BinaryAssociation = BinaryAssociation(
    name="parameters33",
    ends={
        Property(name="VariableCS", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS34", type=VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS35: BinaryAssociation = BinaryAssociation(
    name="typeCS35",
    ends={
        Property(name="TypeCS37", type=ocl_cst_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OperationCS36", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS38: BinaryAssociation = BinaryAssociation(
    name="typeCS38",
    ends={
        Property(name="TypeCS39", type=ocl_cst_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression40: BinaryAssociation = BinaryAssociation(
    name="initExpression40",
    ends={
        Property(name="OCLExpressionCS42", type=ocl_cst_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableCS41", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS43: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS43",
    ends={
        Property(name="SimpleNameCS44", type=ocl_cst_PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PrePostOrBodyDeclCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCS45: BinaryAssociation = BinaryAssociation(
    name="expressionCS45",
    ends={
        Property(name="OCLExpressionCS47", type=ocl_cst_PrePostOrBodyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_PrePostOrBodyDeclCS46", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables66: BinaryAssociation = BinaryAssociation(
    name="variables66",
    ends={
        Property(name="VariableCS67", type=ocl_cst_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_TupleTypeCS", type=VariableCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressionCS48: BinaryAssociation = BinaryAssociation(
    name="expressionCS48",
    ends={
        Property(name="OCLExpressionCS49", type=ocl_cst_InvCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_InvCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defExpressionCS50: BinaryAssociation = BinaryAssociation(
    name="defExpressionCS50",
    ends={
        Property(name="DefExpressionCS", type=ocl_cst_DefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefCS", type=DefExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationCS51: BinaryAssociation = BinaryAssociation(
    name="operationCS51",
    ends={
        Property(name="OperationCS52", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS", type=OperationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableCS53: BinaryAssociation = BinaryAssociation(
    name="variableCS53",
    ends={
        Property(name="VariableCS55", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS54", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCS56: BinaryAssociation = BinaryAssociation(
    name="expressionCS56",
    ends={
        Property(name="OCLExpressionCS58", type=ocl_cst_DefExpressionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_DefExpressionCS57", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments59: BinaryAssociation = BinaryAssociation(
    name="arguments59",
    ends={
        Property(name="OCLExpressionCS60", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS61: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS61",
    ends={
        Property(name="SimpleNameCS63", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS62", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isMarkedPreCS64: BinaryAssociation = BinaryAssociation(
    name="isMarkedPreCS64",
    ends={
        Property(name="IsMarkedPreCS", type=ocl_cst_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_VariableExpCS65", type=IsMarkedPreCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments88: BinaryAssociation = BinaryAssociation(
    name="arguments88",
    ends={
        Property(name="OCLMessageArgCS", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS89", type=OCLMessageArgCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS68: BinaryAssociation = BinaryAssociation(
    name="typeCS68",
    ends={
        Property(name="TypeCS69", type=ocl_cst_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables70: BinaryAssociation = BinaryAssociation(
    name="variables70",
    ends={
        Property(name="VariableCS71", type=ocl_cst_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LetExpCS", type=VariableCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inExpression72: BinaryAssociation = BinaryAssociation(
    name="inExpression72",
    ends={
        Property(name="OCLExpressionCS74", type=ocl_cst_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LetExpCS73", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression75: BinaryAssociation = BinaryAssociation(
    name="thenExpression75",
    ends={
        Property(name="OCLExpressionCS76", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression77: BinaryAssociation = BinaryAssociation(
    name="elseExpression77",
    ends={
        Property(name="OCLExpressionCS79", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS78", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition80: BinaryAssociation = BinaryAssociation(
    name="condition80",
    ends={
        Property(name="OCLExpressionCS82", type=ocl_cst_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_IfExpCS81", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target83: BinaryAssociation = BinaryAssociation(
    name="target83",
    ends={
        Property(name="OCLExpressionCS84", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS85: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS85",
    ends={
        Property(name="SimpleNameCS87", type=ocl_cst_MessageExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_MessageExpCS86", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables98: BinaryAssociation = BinaryAssociation(
    name="variables98",
    ends={
        Property(name="VariableCS99", type=ocl_cst_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_TupleLiteralExpCS", type=VariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS90: BinaryAssociation = BinaryAssociation(
    name="typeCS90",
    ends={
        Property(name="TypeCS91", type=ocl_cst_OCLMessageArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLMessageArgCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression92: BinaryAssociation = BinaryAssociation(
    name="expression92",
    ends={
        Property(name="OCLExpressionCS94", type=ocl_cst_OCLMessageArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLMessageArgCS93", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionLiteralParts95: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts95",
    ends={
        Property(name="CollectionLiteralPartCS", type=ocl_cst_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionLiteralExpCS", type=CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionCS96: BinaryAssociation = BinaryAssociation(
    name="expressionCS96",
    ends={
        Property(name="OCLExpressionCS97", type=ocl_cst_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionLiteralPartCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source102: BinaryAssociation = BinaryAssociation(
    name="source102",
    ends={
        Property(name="OCLExpressionCS103", type=ocl_cst_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CallExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastExpressionCS100: BinaryAssociation = BinaryAssociation(
    name="lastExpressionCS100",
    ends={
        Property(name="OCLExpressionCS101", type=ocl_cst_CollectionRangeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CollectionRangeCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageDeclarations123: BinaryAssociation = BinaryAssociation(
    name="packageDeclarations123",
    ends={
        Property(name="PackageDeclarationCS124", type=ocl_cst_OCLDocumentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_OCLDocumentCS", type=PackageDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS104: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS104",
    ends={
        Property(name="SimpleNameCS106", type=ocl_cst_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_CallExpCS105", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable1107: BinaryAssociation = BinaryAssociation(
    name="variable1107",
    ends={
        Property(name="VariableCS108", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable2109: BinaryAssociation = BinaryAssociation(
    name="variable2109",
    ends={
        Property(name="VariableCS111", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS110", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body112: BinaryAssociation = BinaryAssociation(
    name="body112",
    ends={
        Property(name="OCLExpressionCS114", type=ocl_cst_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_LoopExpCS113", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathNameCS115: BinaryAssociation = BinaryAssociation(
    name="pathNameCS115",
    ends={
        Property(name="PathNameCS116", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments117: BinaryAssociation = BinaryAssociation(
    name="arguments117",
    ends={
        Property(name="OCLExpressionCS119", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS118", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isMarkedPreCS120: BinaryAssociation = BinaryAssociation(
    name="isMarkedPreCS120",
    ends={
        Property(name="IsMarkedPreCS122", type=ocl_cst_FeatureCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_cst_FeatureCallExpCS121", type=IsMarkedPreCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ocl_cst_PackageDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_PackageDeclarationCS)
gen_ocl_cst_PathNameCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_PathNameCS)
gen_ocl_cst_TypeCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_TypeCS)
gen_ocl_cst_OCLExpressionCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLExpressionCS)
gen_ocl_cst_SimpleNameCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_SimpleNameCS)
gen_ocl_cst_ContextDeclCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_ContextDeclCS)
gen_ocl_cst_PropertyContextCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_PropertyContextCS)
gen_ocl_cst_InitOrDerValueCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_InitOrDerValueCS)
gen_ocl_cst_ClassifierContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_ClassifierContextDeclCS)
gen_ocl_cst_DerValueCS_InitOrDerValueCS = Generalization(general=InitOrDerValueCS, specific=ocl_cst_DerValueCS)
gen_ocl_cst_InvOrDefCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_InvOrDefCS)
gen_ocl_cst_OperationContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=ocl_cst_OperationContextDeclCS)
gen_ocl_cst_OperationCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OperationCS)
gen_ocl_cst_VariableCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_VariableCS)
gen_ocl_cst_PrePostOrBodyDeclCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_PrePostOrBodyDeclCS)
gen_ocl_cst_CollectionTypeCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_CollectionTypeCS)
gen_ocl_cst_CollectionTypeCS_cst_TypeCS = Generalization(general=cst_TypeCS, specific=ocl_cst_CollectionTypeCS)
gen_ocl_cst_InitValueCS_InitOrDerValueCS = Generalization(general=InitOrDerValueCS, specific=ocl_cst_InitValueCS)
gen_ocl_cst_InvCS_InvOrDefCS = Generalization(general=InvOrDefCS, specific=ocl_cst_InvCS)
gen_ocl_cst_DefCS_InvOrDefCS = Generalization(general=InvOrDefCS, specific=ocl_cst_DefCS)
gen_ocl_cst_DefExpressionCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_DefExpressionCS)
gen_ocl_cst_VariableExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_VariableExpCS)
gen_ocl_cst_IsMarkedPreCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_IsMarkedPreCS)
gen_ocl_cst_PrimitiveTypeCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_PrimitiveTypeCS)
gen_ocl_cst_PrimitiveTypeCS_cst_TypeCS = Generalization(general=cst_TypeCS, specific=ocl_cst_PrimitiveTypeCS)
gen_ocl_cst_TupleTypeCS_TypeCS = Generalization(general=TypeCS, specific=ocl_cst_TupleTypeCS)
gen_ocl_cst_LetExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_LetExpCS)
gen_ocl_cst_IfExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_IfExpCS)
gen_ocl_cst_MessageExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_MessageExpCS)
gen_ocl_cst_PrimitiveLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_PrimitiveLiteralExpCS)
gen_ocl_cst_OCLMessageArgCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLMessageArgCS)
gen_ocl_cst_LiteralExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_LiteralExpCS)
gen_ocl_cst_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_CollectionLiteralExpCS)
gen_ocl_cst_CollectionLiteralPartCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_CollectionLiteralPartCS)
gen_ocl_cst_TupleLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=ocl_cst_TupleLiteralExpCS)
gen_ocl_cst_IntegerLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_IntegerLiteralExpCS)
gen_ocl_cst_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_UnlimitedNaturalLiteralExpCS)
gen_ocl_cst_RealLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_RealLiteralExpCS)
gen_ocl_cst_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=ocl_cst_StringLiteralExpCS)
gen_ocl_cst_BooleanLiteralExpCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_BooleanLiteralExpCS)
gen_ocl_cst_BooleanLiteralExpCS_cst_PrimitiveLiteralExpCS = Generalization(general=cst_PrimitiveLiteralExpCS, specific=ocl_cst_BooleanLiteralExpCS)
gen_ocl_cst_NullLiteralExpCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_NullLiteralExpCS)
gen_ocl_cst_NullLiteralExpCS_cst_LiteralExpCS = Generalization(general=cst_LiteralExpCS, specific=ocl_cst_NullLiteralExpCS)
gen_ocl_cst_InvalidLiteralExpCS_cst_SimpleNameCS = Generalization(general=cst_SimpleNameCS, specific=ocl_cst_InvalidLiteralExpCS)
gen_ocl_cst_InvalidLiteralExpCS_cst_LiteralExpCS = Generalization(general=cst_LiteralExpCS, specific=ocl_cst_InvalidLiteralExpCS)
gen_ocl_cst_CollectionRangeCS_CollectionLiteralPartCS = Generalization(general=CollectionLiteralPartCS, specific=ocl_cst_CollectionRangeCS)
gen_ocl_cst_CallExpCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=ocl_cst_CallExpCS)
gen_ocl_cst_OCLDocumentCS_CSTNode = Generalization(general=CSTNode, specific=ocl_cst_OCLDocumentCS)
gen_ocl_cst_LoopExpCS_CallExpCS = Generalization(general=CallExpCS, specific=ocl_cst_LoopExpCS)
gen_ocl_cst_IteratorExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=ocl_cst_IteratorExpCS)
gen_ocl_cst_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=ocl_cst_IterateExpCS)
gen_ocl_cst_FeatureCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=ocl_cst_FeatureCallExpCS)
gen_ocl_cst_OperationCallExpCS_FeatureCallExpCS = Generalization(general=FeatureCallExpCS, specific=ocl_cst_OperationCallExpCS)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ContextDeclCS, PackageDeclarationCS, ocl_cst_CSTNode, ocl_cst_PackageDeclarationCS, CSTNode, PathNameCS, ocl_cst_PathNameCS, TypeCS, SimpleNameCS, ocl_cst_TypeCS, OCLExpressionCS, ocl_cst_OCLExpressionCS, ocl_cst_SimpleNameCS, ocl_cst_ContextDeclCS, ocl_cst_PropertyContextCS, InvOrDefCS, ocl_cst_InvOrDefCS, InitOrDerValueCS, ocl_cst_InitOrDerValueCS, ocl_cst_ClassifierContextDeclCS, ocl_cst_DerValueCS, ocl_cst_InitValueCS, ocl_cst_OperationContextDeclCS, OperationCS, PrePostOrBodyDeclCS, ocl_cst_OperationCS, VariableCS, ocl_cst_VariableCS, ocl_cst_PrePostOrBodyDeclCS, ocl_cst_CollectionTypeCS, ocl_cst_InvCS, ocl_cst_DefCS, DefExpressionCS, ocl_cst_DefExpressionCS, ocl_cst_VariableExpCS, IsMarkedPreCS, ocl_cst_IsMarkedPreCS, ocl_cst_PrimitiveTypeCS, cst_SimpleNameCS, cst_TypeCS, ocl_cst_TupleTypeCS, OCLMessageArgCS, ocl_cst_LetExpCS, ocl_cst_IfExpCS, ocl_cst_MessageExpCS, ocl_cst_PrimitiveLiteralExpCS, ocl_cst_IntegerLiteralExpCS, PrimitiveLiteralExpCS, ocl_cst_OCLMessageArgCS, ocl_cst_LiteralExpCS, ocl_cst_CollectionLiteralExpCS, LiteralExpCS, CollectionLiteralPartCS, ocl_cst_CollectionLiteralPartCS, ocl_cst_TupleLiteralExpCS, ocl_cst_UnlimitedNaturalLiteralExpCS, ocl_cst_RealLiteralExpCS, ocl_cst_StringLiteralExpCS, ocl_cst_BooleanLiteralExpCS, cst_PrimitiveLiteralExpCS, ocl_cst_NullLiteralExpCS, cst_LiteralExpCS, ocl_cst_InvalidLiteralExpCS, ocl_cst_CollectionRangeCS, ocl_cst_CallExpCS, ocl_cst_OCLDocumentCS, ocl_cst_LoopExpCS, CallExpCS, ocl_cst_IteratorExpCS, LoopExpCS, ocl_cst_IterateExpCS, ocl_cst_FeatureCallExpCS, ocl_cst_OperationCallExpCS, FeatureCallExpCS, SimpleTypeEnum, PrePostOrBodyEnum, MessageExpKind, CollectionTypeIdentifierEnum, DotOrArrowEnum},
    associations={contextDecls1, packageDeclarationCS3, pathNameCS0, simpleNames5, pathNameCS6, simpleNameCS8, typeCS11, constraints18, simpleNameCS20, constraints13, expressionCS15, pathNameCS16, simpleNameCS23, operationCS25, prePostOrBodyDecls26, pathNameCS28, simpleNameCS30, parameters33, typeCS35, typeCS38, initExpression40, simpleNameCS43, expressionCS45, variables66, expressionCS48, defExpressionCS50, operationCS51, variableCS53, expressionCS56, arguments59, simpleNameCS61, isMarkedPreCS64, arguments88, typeCS68, variables70, inExpression72, thenExpression75, elseExpression77, condition80, target83, simpleNameCS85, variables98, typeCS90, expression92, collectionLiteralParts95, expressionCS96, source102, lastExpressionCS100, packageDeclarations123, simpleNameCS104, variable1107, variable2109, body112, pathNameCS115, arguments117, isMarkedPreCS120},
    generalizations={gen_ocl_cst_PackageDeclarationCS_CSTNode, gen_ocl_cst_PathNameCS_TypeCS, gen_ocl_cst_TypeCS_OCLExpressionCS, gen_ocl_cst_OCLExpressionCS_CSTNode, gen_ocl_cst_SimpleNameCS_OCLExpressionCS, gen_ocl_cst_ContextDeclCS_CSTNode, gen_ocl_cst_PropertyContextCS_ContextDeclCS, gen_ocl_cst_InitOrDerValueCS_CSTNode, gen_ocl_cst_ClassifierContextDeclCS_ContextDeclCS, gen_ocl_cst_DerValueCS_InitOrDerValueCS, gen_ocl_cst_InvOrDefCS_CSTNode, gen_ocl_cst_OperationContextDeclCS_ContextDeclCS, gen_ocl_cst_OperationCS_CSTNode, gen_ocl_cst_VariableCS_CSTNode, gen_ocl_cst_PrePostOrBodyDeclCS_CSTNode, gen_ocl_cst_CollectionTypeCS_cst_SimpleNameCS, gen_ocl_cst_CollectionTypeCS_cst_TypeCS, gen_ocl_cst_InitValueCS_InitOrDerValueCS, gen_ocl_cst_InvCS_InvOrDefCS, gen_ocl_cst_DefCS_InvOrDefCS, gen_ocl_cst_DefExpressionCS_CSTNode, gen_ocl_cst_VariableExpCS_OCLExpressionCS, gen_ocl_cst_IsMarkedPreCS_CSTNode, gen_ocl_cst_PrimitiveTypeCS_cst_SimpleNameCS, gen_ocl_cst_PrimitiveTypeCS_cst_TypeCS, gen_ocl_cst_TupleTypeCS_TypeCS, gen_ocl_cst_LetExpCS_OCLExpressionCS, gen_ocl_cst_IfExpCS_OCLExpressionCS, gen_ocl_cst_MessageExpCS_OCLExpressionCS, gen_ocl_cst_PrimitiveLiteralExpCS_LiteralExpCS, gen_ocl_cst_OCLMessageArgCS_CSTNode, gen_ocl_cst_LiteralExpCS_OCLExpressionCS, gen_ocl_cst_CollectionLiteralExpCS_LiteralExpCS, gen_ocl_cst_CollectionLiteralPartCS_CSTNode, gen_ocl_cst_TupleLiteralExpCS_LiteralExpCS, gen_ocl_cst_IntegerLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_RealLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_ocl_cst_BooleanLiteralExpCS_cst_SimpleNameCS, gen_ocl_cst_BooleanLiteralExpCS_cst_PrimitiveLiteralExpCS, gen_ocl_cst_NullLiteralExpCS_cst_SimpleNameCS, gen_ocl_cst_NullLiteralExpCS_cst_LiteralExpCS, gen_ocl_cst_InvalidLiteralExpCS_cst_SimpleNameCS, gen_ocl_cst_InvalidLiteralExpCS_cst_LiteralExpCS, gen_ocl_cst_CollectionRangeCS_CollectionLiteralPartCS, gen_ocl_cst_CallExpCS_OCLExpressionCS, gen_ocl_cst_OCLDocumentCS_CSTNode, gen_ocl_cst_LoopExpCS_CallExpCS, gen_ocl_cst_IteratorExpCS_LoopExpCS, gen_ocl_cst_IterateExpCS_LoopExpCS, gen_ocl_cst_FeatureCallExpCS_CallExpCS, gen_ocl_cst_OperationCallExpCS_FeatureCallExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)