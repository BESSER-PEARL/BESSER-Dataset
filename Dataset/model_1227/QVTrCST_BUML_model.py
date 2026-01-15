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
DefaultValueCS = Class(name="DefaultValueCS")
OperationCallExpCS = Class(name="OperationCallExpCS")
qvtrelation_cst_KeyDeclCS = Class(name="qvtrelation::cst::KeyDeclCS")
PathNameCS = Class(name="PathNameCS")
qvtrelation_cst_ModelDeclCS = Class(name="qvtrelation::cst::ModelDeclCS")
qvtrelation_cst_AbstractDomainCS = Class(name="qvtrelation::cst::AbstractDomainCS", is_abstract=True)
CSTNode = Class(name="CSTNode")
qvtrelation_cst_ObjectTemplateCS = Class(name="qvtrelation::cst::ObjectTemplateCS")
qvtrelation_cst_CollectionTemplateCS = Class(name="qvtrelation::cst::CollectionTemplateCS")
TemplateCS = Class(name="TemplateCS")
PropertyTemplateCS = Class(name="PropertyTemplateCS")
IdentifiedCS = Class(name="IdentifiedCS")
cst_qvtrelation_EClassifier = Class(name="cst::qvtrelation::EClassifier")
IdentifierCS = Class(name="IdentifierCS")
qvtrelation_cst_DefaultValueCS = Class(name="qvtrelation::cst::DefaultValueCS")
OCLExpressionCS = Class(name="OCLExpressionCS")
qvtrelation_cst_DomainCS = Class(name="qvtrelation::cst::DomainCS")
AbstractDomainCS = Class(name="AbstractDomainCS")
qvtrelation_cst_QueryCS = Class(name="qvtrelation::cst::QueryCS")
ParamDeclarationCS = Class(name="ParamDeclarationCS")
qvtrelation_cst_RelationCS = Class(name="qvtrelation::cst::RelationCS")
VarDeclarationCS = Class(name="VarDeclarationCS")
WhenCS = Class(name="WhenCS")
cst_qvtrelation_EClass = Class(name="cst::qvtrelation::EClass")
qvtrelation_cst_ParamDeclarationCS = Class(name="qvtrelation::cst::ParamDeclarationCS")
TypeCS = Class(name="TypeCS")
qvtrelation_cst_PrimitiveTypeDomainCS = Class(name="qvtrelation::cst::PrimitiveTypeDomainCS")
cst_TemplateVariableCS = Class(name="cst::TemplateVariableCS")
cst_AbstractDomainCS = Class(name="cst::AbstractDomainCS")
qvtrelation_cst_PropertyTemplateCS = Class(name="qvtrelation::cst::PropertyTemplateCS")
cst_qvtrelation_EStructuralFeature = Class(name="cst::qvtrelation::EStructuralFeature")
qvtrelation_cst_TransformationCS = Class(name="qvtrelation::cst::TransformationCS")
ModelDeclCS = Class(name="ModelDeclCS")
KeyDeclCS = Class(name="KeyDeclCS")
QueryCS = Class(name="QueryCS")
RelationCS = Class(name="RelationCS")
qvtrelation_cst_UnitCS = Class(name="qvtrelation::cst::UnitCS")
qvtrelation_cst_VarDeclarationCS = Class(name="qvtrelation::cst::VarDeclarationCS")
WhereCS = Class(name="WhereCS")
qvtrelation_cst_TemplateCS = Class(name="qvtrelation::cst::TemplateCS", is_abstract=True)
qvtrelation_cst_WhenCS = Class(name="qvtrelation::cst::WhenCS")
cst_OCLExpressionCS = Class(name="cst::OCLExpressionCS")
qvtrelation_cst_WhereCS = Class(name="qvtrelation::cst::WhereCS")
qvtrelation_cst_TemplateVariableCS = Class(name="qvtrelation::cst::TemplateVariableCS", is_abstract=True)
qvtrelation_cst_TopLevelCS = Class(name="qvtrelation::cst::TopLevelCS")
UnitCS = Class(name="UnitCS")
TransformationCS = Class(name="TransformationCS")

# DefaultValueCS class attributes and methods

# OperationCallExpCS class attributes and methods

# qvtrelation_cst_KeyDeclCS class attributes and methods

# PathNameCS class attributes and methods

# qvtrelation_cst_ModelDeclCS class attributes and methods

# qvtrelation_cst_AbstractDomainCS class attributes and methods

# CSTNode class attributes and methods

# qvtrelation_cst_ObjectTemplateCS class attributes and methods

# qvtrelation_cst_CollectionTemplateCS class attributes and methods

# TemplateCS class attributes and methods

# PropertyTemplateCS class attributes and methods

# IdentifiedCS class attributes and methods

# cst_qvtrelation_EClassifier class attributes and methods

# IdentifierCS class attributes and methods

# qvtrelation_cst_DefaultValueCS class attributes and methods

# OCLExpressionCS class attributes and methods

# qvtrelation_cst_DomainCS class attributes and methods
qvtrelation_cst_DomainCS_replace: Property = Property(name="replace", type=BooleanType)
qvtrelation_cst_DomainCS_checkonly: Property = Property(name="checkonly", type=BooleanType)
qvtrelation_cst_DomainCS_enforce: Property = Property(name="enforce", type=BooleanType)
qvtrelation_cst_DomainCS.attributes={qvtrelation_cst_DomainCS_enforce, qvtrelation_cst_DomainCS_replace, qvtrelation_cst_DomainCS_checkonly}

# AbstractDomainCS class attributes and methods

# qvtrelation_cst_QueryCS class attributes and methods

# ParamDeclarationCS class attributes and methods

# qvtrelation_cst_RelationCS class attributes and methods
qvtrelation_cst_RelationCS_top: Property = Property(name="top", type=BooleanType)
qvtrelation_cst_RelationCS.attributes={qvtrelation_cst_RelationCS_top}

# VarDeclarationCS class attributes and methods

# WhenCS class attributes and methods

# cst_qvtrelation_EClass class attributes and methods

# qvtrelation_cst_ParamDeclarationCS class attributes and methods

# TypeCS class attributes and methods

# qvtrelation_cst_PrimitiveTypeDomainCS class attributes and methods

# cst_TemplateVariableCS class attributes and methods

# cst_AbstractDomainCS class attributes and methods

# qvtrelation_cst_PropertyTemplateCS class attributes and methods
qvtrelation_cst_PropertyTemplateCS_opposite: Property = Property(name="opposite", type=BooleanType)
qvtrelation_cst_PropertyTemplateCS.attributes={qvtrelation_cst_PropertyTemplateCS_opposite}

# cst_qvtrelation_EStructuralFeature class attributes and methods

# qvtrelation_cst_TransformationCS class attributes and methods

# ModelDeclCS class attributes and methods

# KeyDeclCS class attributes and methods

# QueryCS class attributes and methods

# RelationCS class attributes and methods

# qvtrelation_cst_UnitCS class attributes and methods

# qvtrelation_cst_VarDeclarationCS class attributes and methods

# WhereCS class attributes and methods

# qvtrelation_cst_TemplateCS class attributes and methods

# qvtrelation_cst_WhenCS class attributes and methods

# cst_OCLExpressionCS class attributes and methods

# qvtrelation_cst_WhereCS class attributes and methods

# qvtrelation_cst_TemplateVariableCS class attributes and methods

# qvtrelation_cst_TopLevelCS class attributes and methods

# UnitCS class attributes and methods

# TransformationCS class attributes and methods

# Relationships
modelId9: BinaryAssociation = BinaryAssociation(
    name="modelId9",
    ends={
        Property(name="IdentifierCS10", type=qvtrelation_cst_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_DomainCS", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
template11: BinaryAssociation = BinaryAssociation(
    name="template11",
    ends={
        Property(name="TemplateCS", type=qvtrelation_cst_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_DomainCS12", type=TemplateCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue13: BinaryAssociation = BinaryAssociation(
    name="defaultValue13",
    ends={
        Property(name="DefaultValueCS", type=qvtrelation_cst_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_DomainCS14", type=DefaultValueCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedBy15: BinaryAssociation = BinaryAssociation(
    name="implementedBy15",
    ends={
        Property(name="OperationCallExpCS", type=qvtrelation_cst_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_DomainCS16", type=OperationCallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classId17: BinaryAssociation = BinaryAssociation(
    name="classId17",
    ends={
        Property(name="PathNameCS", type=qvtrelation_cst_KeyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_KeyDeclCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyId18: BinaryAssociation = BinaryAssociation(
    name="propertyId18",
    ends={
        Property(name="IdentifiedCS20", type=qvtrelation_cst_KeyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_KeyDeclCS19", type=IdentifiedCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelId21: BinaryAssociation = BinaryAssociation(
    name="modelId21",
    ends={
        Property(name="IdentifierCS22", type=qvtrelation_cst_ModelDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_ModelDeclCS", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metaModelId23: BinaryAssociation = BinaryAssociation(
    name="metaModelId23",
    ends={
        Property(name="IdentifierCS25", type=qvtrelation_cst_ModelDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_ModelDeclCS24", type=IdentifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyTemplate26: BinaryAssociation = BinaryAssociation(
    name="propertyTemplate26",
    ends={
        Property(name="PropertyTemplateCS", type=qvtrelation_cst_ObjectTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_ObjectTemplateCS", type=PropertyTemplateCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberIdentifier0: BinaryAssociation = BinaryAssociation(
    name="memberIdentifier0",
    ends={
        Property(name="IdentifiedCS", type=qvtrelation_cst_CollectionTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_CollectionTemplateCS", type=IdentifiedCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
referredCollectionType1: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType1",
    ends={
        Property(name="cst_qvtrelation_EClassifier", type=qvtrelation_cst_CollectionTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_CollectionTemplateCS2", type=cst_qvtrelation_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
restIdentifier3: BinaryAssociation = BinaryAssociation(
    name="restIdentifier3",
    ends={
        Property(name="IdentifierCS", type=qvtrelation_cst_CollectionTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_CollectionTemplateCS4", type=IdentifierCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier5: BinaryAssociation = BinaryAssociation(
    name="identifier5",
    ends={
        Property(name="IdentifierCS6", type=qvtrelation_cst_DefaultValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_DefaultValueCS", type=IdentifierCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialiser7: BinaryAssociation = BinaryAssociation(
    name="initialiser7",
    ends={
        Property(name="OCLExpressionCS", type=qvtrelation_cst_DefaultValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_DefaultValueCS8", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pathName40: BinaryAssociation = BinaryAssociation(
    name="pathName40",
    ends={
        Property(name="PathNameCS41", type=qvtrelation_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_QueryCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputParamDeclaration42: BinaryAssociation = BinaryAssociation(
    name="inputParamDeclaration42",
    ends={
        Property(name="ParamDeclarationCS", type=qvtrelation_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_QueryCS43", type=ParamDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oclExpression44: BinaryAssociation = BinaryAssociation(
    name="oclExpression44",
    ends={
        Property(name="OCLExpressionCS46", type=qvtrelation_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_QueryCS45", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="TypeCS49", type=qvtrelation_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_QueryCS48", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier50: BinaryAssociation = BinaryAssociation(
    name="identifier50",
    ends={
        Property(name="IdentifierCS51", type=qvtrelation_cst_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_RelationCS", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overrides52: BinaryAssociation = BinaryAssociation(
    name="overrides52",
    ends={
        Property(name="IdentifierCS54", type=qvtrelation_cst_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_RelationCS53", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDeclaration55: BinaryAssociation = BinaryAssociation(
    name="varDeclaration55",
    ends={
        Property(name="VarDeclarationCS", type=qvtrelation_cst_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_RelationCS56", type=VarDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain57: BinaryAssociation = BinaryAssociation(
    name="domain57",
    ends={
        Property(name="AbstractDomainCS", type=qvtrelation_cst_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_RelationCS58", type=AbstractDomainCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when59: BinaryAssociation = BinaryAssociation(
    name="when59",
    ends={
        Property(name="WhenCS", type=qvtrelation_cst_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_RelationCS60", type=WhenCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredClass27: BinaryAssociation = BinaryAssociation(
    name="referredClass27",
    ends={
        Property(name="cst_qvtrelation_EClass", type=qvtrelation_cst_ObjectTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_ObjectTemplateCS28", type=cst_qvtrelation_EClass, multiplicity=Multiplicity(0, 1))
    }
)
identifier29: BinaryAssociation = BinaryAssociation(
    name="identifier29",
    ends={
        Property(name="IdentifierCS30", type=qvtrelation_cst_ParamDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_ParamDeclarationCS", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="TypeCS", type=qvtrelation_cst_ParamDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_ParamDeclarationCS32", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyId33: BinaryAssociation = BinaryAssociation(
    name="propertyId33",
    ends={
        Property(name="IdentifiedCS34", type=qvtrelation_cst_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_PropertyTemplateCS", type=IdentifiedCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpression35: BinaryAssociation = BinaryAssociation(
    name="oclExpression35",
    ends={
        Property(name="OCLExpressionCS37", type=qvtrelation_cst_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_PropertyTemplateCS36", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredProperty38: BinaryAssociation = BinaryAssociation(
    name="referredProperty38",
    ends={
        Property(name="cst_qvtrelation_EStructuralFeature", type=qvtrelation_cst_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_PropertyTemplateCS39", type=cst_qvtrelation_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
transformation68: BinaryAssociation = BinaryAssociation(
    name="transformation68",
    ends={
        Property(name="TransformationCS", type=qvtrelation_cst_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TopLevelCS69", type=TransformationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelDecl70: BinaryAssociation = BinaryAssociation(
    name="modelDecl70",
    ends={
        Property(name="ModelDeclCS", type=qvtrelation_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TransformationCS", type=ModelDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends71: BinaryAssociation = BinaryAssociation(
    name="extends71",
    ends={
        Property(name="IdentifierCS73", type=qvtrelation_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TransformationCS72", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier74: BinaryAssociation = BinaryAssociation(
    name="identifier74",
    ends={
        Property(name="IdentifierCS76", type=qvtrelation_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TransformationCS75", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyDecl77: BinaryAssociation = BinaryAssociation(
    name="keyDecl77",
    ends={
        Property(name="KeyDeclCS", type=qvtrelation_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TransformationCS78", type=KeyDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query79: BinaryAssociation = BinaryAssociation(
    name="query79",
    ends={
        Property(name="QueryCS", type=qvtrelation_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TransformationCS80", type=QueryCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation81: BinaryAssociation = BinaryAssociation(
    name="relation81",
    ends={
        Property(name="RelationCS", type=qvtrelation_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TransformationCS82", type=RelationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier83: BinaryAssociation = BinaryAssociation(
    name="identifier83",
    ends={
        Property(name="IdentifierCS84", type=qvtrelation_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_UnitCS", type=IdentifierCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
varDeclarationId85: BinaryAssociation = BinaryAssociation(
    name="varDeclarationId85",
    ends={
        Property(name="IdentifierCS86", type=qvtrelation_cst_VarDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_VarDeclarationCS", type=IdentifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where61: BinaryAssociation = BinaryAssociation(
    name="where61",
    ends={
        Property(name="WhereCS", type=qvtrelation_cst_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_RelationCS62", type=WhereCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type87: BinaryAssociation = BinaryAssociation(
    name="type87",
    ends={
        Property(name="TypeCS89", type=qvtrelation_cst_VarDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_VarDeclarationCS88", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr90: BinaryAssociation = BinaryAssociation(
    name="expr90",
    ends={
        Property(name="OCLExpressionCS91", type=qvtrelation_cst_WhenCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_WhenCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
guardExpression63: BinaryAssociation = BinaryAssociation(
    name="guardExpression63",
    ends={
        Property(name="OCLExpressionCS64", type=qvtrelation_cst_TemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TemplateCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr92: BinaryAssociation = BinaryAssociation(
    name="expr92",
    ends={
        Property(name="OCLExpressionCS93", type=qvtrelation_cst_WhereCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_WhereCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="TypeCS66", type=qvtrelation_cst_TemplateVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TemplateVariableCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importClause67: BinaryAssociation = BinaryAssociation(
    name="importClause67",
    ends={
        Property(name="UnitCS", type=qvtrelation_cst_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_cst_TopLevelCS", type=UnitCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_qvtrelation_cst_KeyDeclCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_KeyDeclCS)
gen_qvtrelation_cst_ModelDeclCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_ModelDeclCS)
gen_qvtrelation_cst_AbstractDomainCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_AbstractDomainCS)
gen_qvtrelation_cst_ObjectTemplateCS_TemplateCS = Generalization(general=TemplateCS, specific=qvtrelation_cst_ObjectTemplateCS)
gen_qvtrelation_cst_CollectionTemplateCS_TemplateCS = Generalization(general=TemplateCS, specific=qvtrelation_cst_CollectionTemplateCS)
gen_qvtrelation_cst_DefaultValueCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_DefaultValueCS)
gen_qvtrelation_cst_DomainCS_AbstractDomainCS = Generalization(general=AbstractDomainCS, specific=qvtrelation_cst_DomainCS)
gen_qvtrelation_cst_QueryCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_QueryCS)
gen_qvtrelation_cst_RelationCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_RelationCS)
gen_qvtrelation_cst_ParamDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_ParamDeclarationCS)
gen_qvtrelation_cst_PrimitiveTypeDomainCS_cst_TemplateVariableCS = Generalization(general=cst_TemplateVariableCS, specific=qvtrelation_cst_PrimitiveTypeDomainCS)
gen_qvtrelation_cst_PrimitiveTypeDomainCS_cst_AbstractDomainCS = Generalization(general=cst_AbstractDomainCS, specific=qvtrelation_cst_PrimitiveTypeDomainCS)
gen_qvtrelation_cst_PropertyTemplateCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_PropertyTemplateCS)
gen_qvtrelation_cst_TransformationCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_TransformationCS)
gen_qvtrelation_cst_UnitCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_UnitCS)
gen_qvtrelation_cst_VarDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_VarDeclarationCS)
gen_qvtrelation_cst_TemplateCS_cst_TemplateVariableCS = Generalization(general=cst_TemplateVariableCS, specific=qvtrelation_cst_TemplateCS)
gen_qvtrelation_cst_WhenCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_WhenCS)
gen_qvtrelation_cst_TemplateCS_cst_OCLExpressionCS = Generalization(general=cst_OCLExpressionCS, specific=qvtrelation_cst_TemplateCS)
gen_qvtrelation_cst_WhereCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_WhereCS)
gen_qvtrelation_cst_TemplateVariableCS_IdentifiedCS = Generalization(general=IdentifiedCS, specific=qvtrelation_cst_TemplateVariableCS)
gen_qvtrelation_cst_TopLevelCS_CSTNode = Generalization(general=CSTNode, specific=qvtrelation_cst_TopLevelCS)

# Domain Model
domain_model = DomainModel(
    name="qvtrelation",
    types={DefaultValueCS, OperationCallExpCS, qvtrelation_cst_KeyDeclCS, PathNameCS, qvtrelation_cst_ModelDeclCS, qvtrelation_cst_AbstractDomainCS, CSTNode, qvtrelation_cst_ObjectTemplateCS, qvtrelation_cst_CollectionTemplateCS, TemplateCS, PropertyTemplateCS, IdentifiedCS, cst_qvtrelation_EClassifier, IdentifierCS, qvtrelation_cst_DefaultValueCS, OCLExpressionCS, qvtrelation_cst_DomainCS, AbstractDomainCS, qvtrelation_cst_QueryCS, ParamDeclarationCS, qvtrelation_cst_RelationCS, VarDeclarationCS, WhenCS, cst_qvtrelation_EClass, qvtrelation_cst_ParamDeclarationCS, TypeCS, qvtrelation_cst_PrimitiveTypeDomainCS, cst_TemplateVariableCS, cst_AbstractDomainCS, qvtrelation_cst_PropertyTemplateCS, cst_qvtrelation_EStructuralFeature, qvtrelation_cst_TransformationCS, ModelDeclCS, KeyDeclCS, QueryCS, RelationCS, qvtrelation_cst_UnitCS, qvtrelation_cst_VarDeclarationCS, WhereCS, qvtrelation_cst_TemplateCS, qvtrelation_cst_WhenCS, cst_OCLExpressionCS, qvtrelation_cst_WhereCS, qvtrelation_cst_TemplateVariableCS, qvtrelation_cst_TopLevelCS, UnitCS, TransformationCS},
    associations={modelId9, template11, defaultValue13, implementedBy15, classId17, propertyId18, modelId21, metaModelId23, propertyTemplate26, memberIdentifier0, referredCollectionType1, restIdentifier3, identifier5, initialiser7, pathName40, inputParamDeclaration42, oclExpression44, type47, identifier50, overrides52, varDeclaration55, domain57, when59, referredClass27, identifier29, type31, propertyId33, oclExpression35, referredProperty38, transformation68, modelDecl70, extends71, identifier74, keyDecl77, query79, relation81, identifier83, varDeclarationId85, where61, type87, expr90, guardExpression63, expr92, type65, importClause67},
    generalizations={gen_qvtrelation_cst_KeyDeclCS_CSTNode, gen_qvtrelation_cst_ModelDeclCS_CSTNode, gen_qvtrelation_cst_AbstractDomainCS_CSTNode, gen_qvtrelation_cst_ObjectTemplateCS_TemplateCS, gen_qvtrelation_cst_CollectionTemplateCS_TemplateCS, gen_qvtrelation_cst_DefaultValueCS_CSTNode, gen_qvtrelation_cst_DomainCS_AbstractDomainCS, gen_qvtrelation_cst_QueryCS_CSTNode, gen_qvtrelation_cst_RelationCS_CSTNode, gen_qvtrelation_cst_ParamDeclarationCS_CSTNode, gen_qvtrelation_cst_PrimitiveTypeDomainCS_cst_TemplateVariableCS, gen_qvtrelation_cst_PrimitiveTypeDomainCS_cst_AbstractDomainCS, gen_qvtrelation_cst_PropertyTemplateCS_CSTNode, gen_qvtrelation_cst_TransformationCS_CSTNode, gen_qvtrelation_cst_UnitCS_CSTNode, gen_qvtrelation_cst_VarDeclarationCS_CSTNode, gen_qvtrelation_cst_TemplateCS_cst_TemplateVariableCS, gen_qvtrelation_cst_WhenCS_CSTNode, gen_qvtrelation_cst_TemplateCS_cst_OCLExpressionCS, gen_qvtrelation_cst_WhereCS_CSTNode, gen_qvtrelation_cst_TemplateVariableCS_IdentifiedCS, gen_qvtrelation_cst_TopLevelCS_CSTNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)