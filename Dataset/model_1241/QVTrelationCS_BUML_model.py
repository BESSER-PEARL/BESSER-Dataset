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
qvtrelationcs_Variable = Class(name="qvtrelationcs::Variable")
qvtrelationcs_DomainCS = Class(name="qvtrelationcs::DomainCS")
AbstractDomainCS = Class(name="AbstractDomainCS")
qvtrelationcs_TypedModel = Class(name="qvtrelationcs::TypedModel")
qvtrelationcs_DomainPatternCS = Class(name="qvtrelationcs::DomainPatternCS")
qvtrelationcs_AbstractDomainCS = Class(name="qvtrelationcs::AbstractDomainCS", is_abstract=True)
ModelElementCS = Class(name="ModelElementCS")
Nameable = Class(name="Nameable")
qvtrelationcs_CollectionTemplateCS = Class(name="qvtrelationcs::CollectionTemplateCS")
TemplateCS = Class(name="TemplateCS")
qvtrelationcs_TemplateVariableCS = Class(name="qvtrelationcs::TemplateVariableCS", is_abstract=True)
qvtrelationcs_ElementTemplateCS = Class(name="qvtrelationcs::ElementTemplateCS")
qvtrelationcs_DefaultValueCS = Class(name="qvtrelationcs::DefaultValueCS")
qvtrelationcs_ExpCS = Class(name="qvtrelationcs::ExpCS")
qvtrelationcs_Class = Class(name="qvtrelationcs::Class")
qvtrelationcs_ModelDeclCS = Class(name="qvtrelationcs::ModelDeclCS")
NamedElementCS = Class(name="NamedElementCS")
qvtrelationcs_Namespace = Class(name="qvtrelationcs::Namespace")
qvtrelationcs_ObjectTemplateCS = Class(name="qvtrelationcs::ObjectTemplateCS")
qvtrelationcs_PropertyTemplateCS = Class(name="qvtrelationcs::PropertyTemplateCS")
qvtrelationcs_ParamDeclarationCS = Class(name="qvtrelationcs::ParamDeclarationCS")
TypedElementCS = Class(name="TypedElementCS")
qvtrelationcs_PatternCS = Class(name="qvtrelationcs::PatternCS")
qvtrelationcs_PredicateCS = Class(name="qvtrelationcs::PredicateCS")
qvtrelationcs_TemplateCS = Class(name="qvtrelationcs::TemplateCS", is_abstract=True)
TemplateVariableCS = Class(name="TemplateVariableCS")
qvtrelationcs_KeyDeclCS = Class(name="qvtrelationcs::KeyDeclCS")
qvtrelationcs_PathNameCS = Class(name="qvtrelationcs::PathNameCS")
qvtrelationcs_Property = Class(name="qvtrelationcs::Property")
qvtrelationcs_RelationCS = Class(name="qvtrelationcs::RelationCS")
Relation = Class(name="Relation")
qvtrelationcs_VarDeclarationCS = Class(name="qvtrelationcs::VarDeclarationCS")
qvtrelationcs_PrimitiveTypeDomainCS = Class(name="qvtrelationcs::PrimitiveTypeDomainCS")
qvtrelationcs_QueryCS = Class(name="qvtrelationcs::QueryCS")
ClassCS = Class(name="ClassCS")
qvtrelationcs_Transformation = Class(name="qvtrelationcs::Transformation")
ExpCS = Class(name="ExpCS")
qvtrelationcs_TypedRefCS = Class(name="qvtrelationcs::TypedRefCS")
qvtrelationcs_TopLevelCS = Class(name="qvtrelationcs::TopLevelCS")
RootPackageCS = Class(name="RootPackageCS")
qvtrelationcs_UnitCS = Class(name="qvtrelationcs::UnitCS")
qvtrelationcs_TransformationCS = Class(name="qvtrelationcs::TransformationCS")
qvtrelationcs_Element = Class(name="qvtrelationcs::Element")
qvtrelationcs_VarDeclarationIdCS = Class(name="qvtrelationcs::VarDeclarationIdCS")

# qvtrelationcs_Variable class attributes and methods

# qvtrelationcs_DomainCS class attributes and methods
qvtrelationcs_DomainCS_implementedBy: Property = Property(name="implementedBy", type=StringType)
qvtrelationcs_DomainCS_isCheckonly: Property = Property(name="isCheckonly", type=BooleanType)
qvtrelationcs_DomainCS_isEnforce: Property = Property(name="isEnforce", type=BooleanType)
qvtrelationcs_DomainCS_isReplace: Property = Property(name="isReplace", type=BooleanType)
qvtrelationcs_DomainCS.attributes={qvtrelationcs_DomainCS_isEnforce, qvtrelationcs_DomainCS_isReplace, qvtrelationcs_DomainCS_implementedBy, qvtrelationcs_DomainCS_isCheckonly}

# AbstractDomainCS class attributes and methods

# qvtrelationcs_TypedModel class attributes and methods

# qvtrelationcs_DomainPatternCS class attributes and methods

# qvtrelationcs_AbstractDomainCS class attributes and methods

# ModelElementCS class attributes and methods

# Nameable class attributes and methods

# qvtrelationcs_CollectionTemplateCS class attributes and methods

# TemplateCS class attributes and methods

# qvtrelationcs_TemplateVariableCS class attributes and methods

# qvtrelationcs_ElementTemplateCS class attributes and methods

# qvtrelationcs_DefaultValueCS class attributes and methods

# qvtrelationcs_ExpCS class attributes and methods

# qvtrelationcs_Class class attributes and methods

# qvtrelationcs_ModelDeclCS class attributes and methods

# NamedElementCS class attributes and methods

# qvtrelationcs_Namespace class attributes and methods

# qvtrelationcs_ObjectTemplateCS class attributes and methods

# qvtrelationcs_PropertyTemplateCS class attributes and methods

# qvtrelationcs_ParamDeclarationCS class attributes and methods

# TypedElementCS class attributes and methods

# qvtrelationcs_PatternCS class attributes and methods

# qvtrelationcs_PredicateCS class attributes and methods

# qvtrelationcs_TemplateCS class attributes and methods

# TemplateVariableCS class attributes and methods

# qvtrelationcs_KeyDeclCS class attributes and methods

# qvtrelationcs_PathNameCS class attributes and methods

# qvtrelationcs_Property class attributes and methods

# qvtrelationcs_RelationCS class attributes and methods
qvtrelationcs_RelationCS_isDefault: Property = Property(name="isDefault", type=BooleanType)
qvtrelationcs_RelationCS_isTop: Property = Property(name="isTop", type=BooleanType)
qvtrelationcs_RelationCS.attributes={qvtrelationcs_RelationCS_isTop, qvtrelationcs_RelationCS_isDefault}

# Relation class attributes and methods

# qvtrelationcs_VarDeclarationCS class attributes and methods

# qvtrelationcs_PrimitiveTypeDomainCS class attributes and methods

# qvtrelationcs_QueryCS class attributes and methods

# ClassCS class attributes and methods

# qvtrelationcs_Transformation class attributes and methods

# ExpCS class attributes and methods

# qvtrelationcs_TypedRefCS class attributes and methods

# qvtrelationcs_TopLevelCS class attributes and methods

# RootPackageCS class attributes and methods

# qvtrelationcs_UnitCS class attributes and methods

# qvtrelationcs_TransformationCS class attributes and methods

# qvtrelationcs_Element class attributes and methods

# qvtrelationcs_VarDeclarationIdCS class attributes and methods

# Relationships
propertyId4: BinaryAssociation = BinaryAssociation(
    name="propertyId4",
    ends={
        Property(name="qvtrelationcs_Variable", type=qvtrelationcs_DefaultValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DefaultValueCS5", type=qvtrelationcs_Variable, multiplicity=Multiplicity(1, 1))
    }
)
modelId6: BinaryAssociation = BinaryAssociation(
    name="modelId6",
    ends={
        Property(name="qvtrelationcs_TypedModel", type=qvtrelationcs_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DomainCS", type=qvtrelationcs_TypedModel, multiplicity=Multiplicity(0, 1))
    }
)
ownedPattern7: BinaryAssociation = BinaryAssociation(
    name="ownedPattern7",
    ends={
        Property(name="qvtrelationcs_DomainPatternCS", type=qvtrelationcs_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DomainCS8", type=qvtrelationcs_DomainPatternCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDefaultValues9: BinaryAssociation = BinaryAssociation(
    name="ownedDefaultValues9",
    ends={
        Property(name="qvtrelationcs_DefaultValueCS11", type=qvtrelationcs_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DomainCS10", type=qvtrelationcs_DefaultValueCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemberIdentifiers0: BinaryAssociation = BinaryAssociation(
    name="ownedMemberIdentifiers0",
    ends={
        Property(name="qvtrelationcs_TemplateVariableCS", type=qvtrelationcs_CollectionTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_CollectionTemplateCS", type=qvtrelationcs_TemplateVariableCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedRestIdentifier1: BinaryAssociation = BinaryAssociation(
    name="ownedRestIdentifier1",
    ends={
        Property(name="qvtrelationcs_ElementTemplateCS", type=qvtrelationcs_CollectionTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_CollectionTemplateCS2", type=qvtrelationcs_ElementTemplateCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedInitExpression3: BinaryAssociation = BinaryAssociation(
    name="ownedInitExpression3",
    ends={
        Property(name="qvtrelationcs_ExpCS", type=qvtrelationcs_DefaultValueCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DefaultValueCS", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classId26: BinaryAssociation = BinaryAssociation(
    name="classId26",
    ends={
        Property(name="qvtrelationcs_Class", type=qvtrelationcs_KeyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_KeyDeclCS27", type=qvtrelationcs_Class, multiplicity=Multiplicity(0, 1))
    }
)
metamodelIds28: BinaryAssociation = BinaryAssociation(
    name="metamodelIds28",
    ends={
        Property(name="qvtrelationcs_Namespace", type=qvtrelationcs_ModelDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_ModelDeclCS", type=qvtrelationcs_Namespace, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPropertyTemplates29: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyTemplates29",
    ends={
        Property(name="PropertyTemplateCS", type=qvtrelationcs_ObjectTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningObjectTemplate", type=qvtrelationcs_PropertyTemplateCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPredicates30: BinaryAssociation = BinaryAssociation(
    name="ownedPredicates30",
    ends={
        Property(name="qvtrelationcs_PredicateCS", type=qvtrelationcs_PatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_PatternCS", type=qvtrelationcs_PredicateCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedImplementedBy12: BinaryAssociation = BinaryAssociation(
    name="ownedImplementedBy12",
    ends={
        Property(name="qvtrelationcs_ExpCS14", type=qvtrelationcs_DomainCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DomainCS13", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTemplate15: BinaryAssociation = BinaryAssociation(
    name="ownedTemplate15",
    ends={
        Property(name="qvtrelationcs_TemplateCS", type=qvtrelationcs_DomainPatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_DomainPatternCS16", type=qvtrelationcs_TemplateCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier17: BinaryAssociation = BinaryAssociation(
    name="identifier17",
    ends={
        Property(name="qvtrelationcs_Variable19", type=qvtrelationcs_ElementTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_ElementTemplateCS18", type=qvtrelationcs_Variable, multiplicity=Multiplicity(0, 1))
    }
)
ownedPathName20: BinaryAssociation = BinaryAssociation(
    name="ownedPathName20",
    ends={
        Property(name="qvtrelationcs_PathNameCS", type=qvtrelationcs_KeyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_KeyDeclCS", type=qvtrelationcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyIds21: BinaryAssociation = BinaryAssociation(
    name="propertyIds21",
    ends={
        Property(name="qvtrelationcs_Property", type=qvtrelationcs_KeyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_KeyDeclCS22", type=qvtrelationcs_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOppositePropertyIds23: BinaryAssociation = BinaryAssociation(
    name="ownedOppositePropertyIds23",
    ends={
        Property(name="qvtrelationcs_PathNameCS25", type=qvtrelationcs_KeyDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_KeyDeclCS24", type=qvtrelationcs_PathNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpression44: BinaryAssociation = BinaryAssociation(
    name="ownedExpression44",
    ends={
        Property(name="qvtrelationcs_ExpCS46", type=qvtrelationcs_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_QueryCS45", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overrides47: BinaryAssociation = BinaryAssociation(
    name="overrides47",
    ends={
        Property(name="Relation", type=qvtrelationcs_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_RelationCS", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
ownedVarDeclarations48: BinaryAssociation = BinaryAssociation(
    name="ownedVarDeclarations48",
    ends={
        Property(name="qvtrelationcs_VarDeclarationCS", type=qvtrelationcs_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_RelationCS49", type=qvtrelationcs_VarDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDomains50: BinaryAssociation = BinaryAssociation(
    name="ownedDomains50",
    ends={
        Property(name="qvtrelationcs_AbstractDomainCS", type=qvtrelationcs_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_RelationCS51", type=qvtrelationcs_AbstractDomainCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedCondition31: BinaryAssociation = BinaryAssociation(
    name="ownedCondition31",
    ends={
        Property(name="qvtrelationcs_ExpCS33", type=qvtrelationcs_PredicateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_PredicateCS32", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningObjectTemplate34: BinaryAssociation = BinaryAssociation(
    name="owningObjectTemplate34",
    ends={
        Property(name="ObjectTemplateCS", type=qvtrelationcs_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPropertyTemplates", type=qvtrelationcs_ObjectTemplateCS, multiplicity=Multiplicity(0, 1))
    }
)
propertyId35: BinaryAssociation = BinaryAssociation(
    name="propertyId35",
    ends={
        Property(name="qvtrelationcs_Property36", type=qvtrelationcs_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_PropertyTemplateCS", type=qvtrelationcs_Property, multiplicity=Multiplicity(0, 1))
    }
)
ownedOppositePropertyId37: BinaryAssociation = BinaryAssociation(
    name="ownedOppositePropertyId37",
    ends={
        Property(name="qvtrelationcs_PathNameCS39", type=qvtrelationcs_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_PropertyTemplateCS38", type=qvtrelationcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExpression40: BinaryAssociation = BinaryAssociation(
    name="ownedExpression40",
    ends={
        Property(name="qvtrelationcs_ExpCS42", type=qvtrelationcs_PropertyTemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_PropertyTemplateCS41", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameters43: BinaryAssociation = BinaryAssociation(
    name="ownedParameters43",
    ends={
        Property(name="qvtrelationcs_ParamDeclarationCS", type=qvtrelationcs_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_QueryCS", type=qvtrelationcs_ParamDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedModelDecls66: BinaryAssociation = BinaryAssociation(
    name="ownedModelDecls66",
    ends={
        Property(name="qvtrelationcs_ModelDeclCS68", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TransformationCS67", type=qvtrelationcs_ModelDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends69: BinaryAssociation = BinaryAssociation(
    name="extends69",
    ends={
        Property(name="qvtrelationcs_Transformation", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TransformationCS70", type=qvtrelationcs_Transformation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedKeyDecls71: BinaryAssociation = BinaryAssociation(
    name="ownedKeyDecls71",
    ends={
        Property(name="qvtrelationcs_KeyDeclCS73", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TransformationCS72", type=qvtrelationcs_KeyDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPathName74: BinaryAssociation = BinaryAssociation(
    name="ownedPathName74",
    ends={
        Property(name="qvtrelationcs_PathNameCS76", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TransformationCS75", type=qvtrelationcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedQueries77: BinaryAssociation = BinaryAssociation(
    name="ownedQueries77",
    ends={
        Property(name="qvtrelationcs_QueryCS79", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TransformationCS78", type=qvtrelationcs_QueryCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRelations80: BinaryAssociation = BinaryAssociation(
    name="ownedRelations80",
    ends={
        Property(name="qvtrelationcs_RelationCS82", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TransformationCS81", type=qvtrelationcs_RelationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedWhen52: BinaryAssociation = BinaryAssociation(
    name="ownedWhen52",
    ends={
        Property(name="qvtrelationcs_PatternCS54", type=qvtrelationcs_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_RelationCS53", type=qvtrelationcs_PatternCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedWhere55: BinaryAssociation = BinaryAssociation(
    name="ownedWhere55",
    ends={
        Property(name="qvtrelationcs_PatternCS57", type=qvtrelationcs_RelationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_RelationCS56", type=qvtrelationcs_PatternCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedGuardExpression58: BinaryAssociation = BinaryAssociation(
    name="ownedGuardExpression58",
    ends={
        Property(name="qvtrelationcs_ExpCS60", type=qvtrelationcs_TemplateCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TemplateCS59", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType61: BinaryAssociation = BinaryAssociation(
    name="ownedType61",
    ends={
        Property(name="qvtrelationcs_TypedRefCS", type=qvtrelationcs_TemplateVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TemplateVariableCS62", type=qvtrelationcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedImportClauses63: BinaryAssociation = BinaryAssociation(
    name="ownedImportClauses63",
    ends={
        Property(name="qvtrelationcs_UnitCS", type=qvtrelationcs_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TopLevelCS", type=qvtrelationcs_UnitCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransformations64: BinaryAssociation = BinaryAssociation(
    name="ownedTransformations64",
    ends={
        Property(name="qvtrelationcs_TransformationCS", type=qvtrelationcs_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_TopLevelCS65", type=qvtrelationcs_TransformationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers83: BinaryAssociation = BinaryAssociation(
    name="identifiers83",
    ends={
        Property(name="qvtrelationcs_Element", type=qvtrelationcs_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_UnitCS84", type=qvtrelationcs_Element, multiplicity=Multiplicity(1, 9999))
    }
)
ownedInitExpression85: BinaryAssociation = BinaryAssociation(
    name="ownedInitExpression85",
    ends={
        Property(name="qvtrelationcs_ExpCS87", type=qvtrelationcs_VarDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_VarDeclarationCS86", type=qvtrelationcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType88: BinaryAssociation = BinaryAssociation(
    name="ownedType88",
    ends={
        Property(name="qvtrelationcs_TypedRefCS90", type=qvtrelationcs_VarDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_VarDeclarationCS89", type=qvtrelationcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedVarDeclarationIds91: BinaryAssociation = BinaryAssociation(
    name="ownedVarDeclarationIds91",
    ends={
        Property(name="qvtrelationcs_VarDeclarationIdCS", type=qvtrelationcs_VarDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelationcs_VarDeclarationCS92", type=qvtrelationcs_VarDeclarationIdCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_qvtrelationcs_DomainCS_AbstractDomainCS = Generalization(general=AbstractDomainCS, specific=qvtrelationcs_DomainCS)
gen_qvtrelationcs_AbstractDomainCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_AbstractDomainCS)
gen_qvtrelationcs_AbstractDomainCS_Nameable = Generalization(general=Nameable, specific=qvtrelationcs_AbstractDomainCS)
gen_qvtrelationcs_CollectionTemplateCS_TemplateCS = Generalization(general=TemplateCS, specific=qvtrelationcs_CollectionTemplateCS)
gen_qvtrelationcs_DefaultValueCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_DefaultValueCS)
gen_qvtrelationcs_ModelDeclCS_NamedElementCS = Generalization(general=NamedElementCS, specific=qvtrelationcs_ModelDeclCS)
gen_qvtrelationcs_ObjectTemplateCS_TemplateCS = Generalization(general=TemplateCS, specific=qvtrelationcs_ObjectTemplateCS)
gen_qvtrelationcs_ParamDeclarationCS_TypedElementCS = Generalization(general=TypedElementCS, specific=qvtrelationcs_ParamDeclarationCS)
gen_qvtrelationcs_PatternCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_PatternCS)
gen_qvtrelationcs_DomainPatternCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_DomainPatternCS)
gen_qvtrelationcs_ElementTemplateCS_TemplateVariableCS = Generalization(general=TemplateVariableCS, specific=qvtrelationcs_ElementTemplateCS)
gen_qvtrelationcs_KeyDeclCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_KeyDeclCS)
gen_qvtrelationcs_RelationCS_NamedElementCS = Generalization(general=NamedElementCS, specific=qvtrelationcs_RelationCS)
gen_qvtrelationcs_PredicateCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_PredicateCS)
gen_qvtrelationcs_PrimitiveTypeDomainCS_TemplateVariableCS = Generalization(general=TemplateVariableCS, specific=qvtrelationcs_PrimitiveTypeDomainCS)
gen_qvtrelationcs_PrimitiveTypeDomainCS_AbstractDomainCS = Generalization(general=AbstractDomainCS, specific=qvtrelationcs_PrimitiveTypeDomainCS)
gen_qvtrelationcs_PropertyTemplateCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_PropertyTemplateCS)
gen_qvtrelationcs_QueryCS_TypedElementCS = Generalization(general=TypedElementCS, specific=qvtrelationcs_QueryCS)
gen_qvtrelationcs_TransformationCS_ClassCS = Generalization(general=ClassCS, specific=qvtrelationcs_TransformationCS)
gen_qvtrelationcs_TemplateCS_ExpCS = Generalization(general=ExpCS, specific=qvtrelationcs_TemplateCS)
gen_qvtrelationcs_TemplateCS_TemplateVariableCS = Generalization(general=TemplateVariableCS, specific=qvtrelationcs_TemplateCS)
gen_qvtrelationcs_TemplateVariableCS_NamedElementCS = Generalization(general=NamedElementCS, specific=qvtrelationcs_TemplateVariableCS)
gen_qvtrelationcs_TopLevelCS_RootPackageCS = Generalization(general=RootPackageCS, specific=qvtrelationcs_TopLevelCS)
gen_qvtrelationcs_UnitCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_UnitCS)
gen_qvtrelationcs_VarDeclarationCS_ModelElementCS = Generalization(general=ModelElementCS, specific=qvtrelationcs_VarDeclarationCS)
gen_qvtrelationcs_VarDeclarationIdCS_NamedElementCS = Generalization(general=NamedElementCS, specific=qvtrelationcs_VarDeclarationIdCS)

# Domain Model
domain_model = DomainModel(
    name="qvtrelationcs",
    types={qvtrelationcs_Variable, qvtrelationcs_DomainCS, AbstractDomainCS, qvtrelationcs_TypedModel, qvtrelationcs_DomainPatternCS, qvtrelationcs_AbstractDomainCS, ModelElementCS, Nameable, qvtrelationcs_CollectionTemplateCS, TemplateCS, qvtrelationcs_TemplateVariableCS, qvtrelationcs_ElementTemplateCS, qvtrelationcs_DefaultValueCS, qvtrelationcs_ExpCS, qvtrelationcs_Class, qvtrelationcs_ModelDeclCS, NamedElementCS, qvtrelationcs_Namespace, qvtrelationcs_ObjectTemplateCS, qvtrelationcs_PropertyTemplateCS, qvtrelationcs_ParamDeclarationCS, TypedElementCS, qvtrelationcs_PatternCS, qvtrelationcs_PredicateCS, qvtrelationcs_TemplateCS, TemplateVariableCS, qvtrelationcs_KeyDeclCS, qvtrelationcs_PathNameCS, qvtrelationcs_Property, qvtrelationcs_RelationCS, Relation, qvtrelationcs_VarDeclarationCS, qvtrelationcs_PrimitiveTypeDomainCS, qvtrelationcs_QueryCS, ClassCS, qvtrelationcs_Transformation, ExpCS, qvtrelationcs_TypedRefCS, qvtrelationcs_TopLevelCS, RootPackageCS, qvtrelationcs_UnitCS, qvtrelationcs_TransformationCS, qvtrelationcs_Element, qvtrelationcs_VarDeclarationIdCS},
    associations={propertyId4, modelId6, ownedPattern7, ownedDefaultValues9, ownedMemberIdentifiers0, ownedRestIdentifier1, ownedInitExpression3, classId26, metamodelIds28, ownedPropertyTemplates29, ownedPredicates30, ownedImplementedBy12, ownedTemplate15, identifier17, ownedPathName20, propertyIds21, ownedOppositePropertyIds23, ownedExpression44, overrides47, ownedVarDeclarations48, ownedDomains50, ownedCondition31, owningObjectTemplate34, propertyId35, ownedOppositePropertyId37, ownedExpression40, ownedParameters43, ownedModelDecls66, extends69, ownedKeyDecls71, ownedPathName74, ownedQueries77, ownedRelations80, ownedWhen52, ownedWhere55, ownedGuardExpression58, ownedType61, ownedImportClauses63, ownedTransformations64, identifiers83, ownedInitExpression85, ownedType88, ownedVarDeclarationIds91},
    generalizations={gen_qvtrelationcs_DomainCS_AbstractDomainCS, gen_qvtrelationcs_AbstractDomainCS_ModelElementCS, gen_qvtrelationcs_AbstractDomainCS_Nameable, gen_qvtrelationcs_CollectionTemplateCS_TemplateCS, gen_qvtrelationcs_DefaultValueCS_ModelElementCS, gen_qvtrelationcs_ModelDeclCS_NamedElementCS, gen_qvtrelationcs_ObjectTemplateCS_TemplateCS, gen_qvtrelationcs_ParamDeclarationCS_TypedElementCS, gen_qvtrelationcs_PatternCS_ModelElementCS, gen_qvtrelationcs_DomainPatternCS_ModelElementCS, gen_qvtrelationcs_ElementTemplateCS_TemplateVariableCS, gen_qvtrelationcs_KeyDeclCS_ModelElementCS, gen_qvtrelationcs_RelationCS_NamedElementCS, gen_qvtrelationcs_PredicateCS_ModelElementCS, gen_qvtrelationcs_PrimitiveTypeDomainCS_TemplateVariableCS, gen_qvtrelationcs_PrimitiveTypeDomainCS_AbstractDomainCS, gen_qvtrelationcs_PropertyTemplateCS_ModelElementCS, gen_qvtrelationcs_QueryCS_TypedElementCS, gen_qvtrelationcs_TransformationCS_ClassCS, gen_qvtrelationcs_TemplateCS_ExpCS, gen_qvtrelationcs_TemplateCS_TemplateVariableCS, gen_qvtrelationcs_TemplateVariableCS_NamedElementCS, gen_qvtrelationcs_TopLevelCS_RootPackageCS, gen_qvtrelationcs_UnitCS_ModelElementCS, gen_qvtrelationcs_VarDeclarationCS_ModelElementCS, gen_qvtrelationcs_VarDeclarationIdCS_NamedElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)