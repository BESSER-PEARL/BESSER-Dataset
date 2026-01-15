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
ExecutionType: Enumeration = Enumeration(
    name="ExecutionType",
    literals={
            EnumerationLiteral(name="unspecified"),
			EnumerationLiteral(name="search"),
			EnumerationLiteral(name="incremental")
    }
)

ParameterDirection: Enumeration = Enumeration(
    name="ParameterDirection",
    literals={
            EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out")
    }
)

CompareFeature: Enumeration = Enumeration(
    name="CompareFeature",
    literals={
            EnumerationLiteral(name="equality"),
			EnumerationLiteral(name="inequality")
    }
)

ClosureType: Enumeration = Enumeration(
    name="ClosureType",
    literals={
            EnumerationLiteral(name="original"),
			EnumerationLiteral(name="reflexive_transitive"),
			EnumerationLiteral(name="transitive")
    }
)

# Classes
vql_PatternImport = Class(name="vql::PatternImport")
vql_EPackage = Class(name="vql::EPackage")
vql_Pattern = Class(name="vql::Pattern")
vql_VQLImportSection = Class(name="vql::VQLImportSection")
XImportSection = Class(name="XImportSection")
vql_PackageImport = Class(name="vql::PackageImport")
vql_Annotation = Class(name="vql::Annotation")
vql_Modifiers = Class(name="vql::Modifiers")
vql_Variable = Class(name="vql::Variable")
vql_EClassifierConstraint = Class(name="vql::EClassifierConstraint")
Constraint = Class(name="Constraint")
UnaryTypeConstraint = Class(name="UnaryTypeConstraint")
vql_EnumValue = Class(name="vql::EnumValue")
ValueReference = Class(name="ValueReference")
vql_EEnum = Class(name="vql::EEnum")
vql_EEnumLiteral = Class(name="vql::EEnumLiteral")
vql_PatternModel = Class(name="vql::PatternModel")
vql_ClassType = Class(name="vql::ClassType")
EntityType = Class(name="EntityType")
vql_EClassifier = Class(name="vql::EClassifier")
vql_ReferenceType = Class(name="vql::ReferenceType")
RelationType = Class(name="RelationType")
vql_EStructuralFeature = Class(name="vql::EStructuralFeature")
vql_VariableReference = Class(name="vql::VariableReference")
vql_PatternBody = Class(name="vql::PatternBody")
vql_AnnotationParameter = Class(name="vql::AnnotationParameter")
vql_ValueReference = Class(name="vql::ValueReference")
vql_Expression = Class(name="vql::Expression")
Expression = Class(name="Expression")
vql_Type = Class(name="vql::Type")
vql_ComputationValue = Class(name="vql::ComputationValue")
vql_ParameterRef = Class(name="vql::ParameterRef")
Variable = Class(name="Variable")
vql_Parameter = Class(name="vql::Parameter")
vql_LocalVariable = Class(name="vql::LocalVariable")
vql_EntityType = Class(name="vql::EntityType")
Type = Class(name="Type")
vql_Constraint = Class(name="vql::Constraint")
vql_PatternCall = Class(name="vql::PatternCall")
CallableRelation = Class(name="CallableRelation")
vql_LiteralValueReference = Class(name="vql::LiteralValueReference")
vql_CheckConstraint = Class(name="vql::CheckConstraint")
vql_XExpression = Class(name="vql::XExpression")
vql_PathExpressionConstraint = Class(name="vql::PathExpressionConstraint")
vql_JavaType = Class(name="vql::JavaType")
vql_JvmDeclaredType = Class(name="vql::JvmDeclaredType")
vql_RelationType = Class(name="vql::RelationType")
vql_TypeCheckConstraint = Class(name="vql::TypeCheckConstraint")
vql_PatternCompositionConstraint = Class(name="vql::PatternCompositionConstraint")
vql_CallableRelation = Class(name="vql::CallableRelation", is_abstract=True)
vql_CompareConstraint = Class(name="vql::CompareConstraint")
vql_FunctionEvaluationValue = Class(name="vql::FunctionEvaluationValue")
ComputationValue = Class(name="ComputationValue")
vql_AggregatedValue = Class(name="vql::AggregatedValue")
vql_JvmType = Class(name="vql::JvmType")
vql_StringValue = Class(name="vql::StringValue")
LiteralValueReference = Class(name="LiteralValueReference")
vql_NumberValue = Class(name="vql::NumberValue")
vql_XNumberLiteral = Class(name="vql::XNumberLiteral")
vql_BoolValue = Class(name="vql::BoolValue")
vql_XBooleanLiteral = Class(name="vql::XBooleanLiteral")
vql_ListValue = Class(name="vql::ListValue")
vql_UnaryTypeConstraint = Class(name="vql::UnaryTypeConstraint", is_abstract=True)

# vql_PatternImport class attributes and methods
vql_PatternImport_packageName: Property = Property(name="packageName", type=StringType)
vql_PatternImport_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PatternImport.attributes={vql_PatternImport_packageName}
vql_PatternImport.methods={vql_PatternImport_m_toString}

# vql_EPackage class attributes and methods

# vql_Pattern class attributes and methods
vql_Pattern_name: Property = Property(name="name", type=StringType)
vql_Pattern_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Pattern.attributes={vql_Pattern_name}
vql_Pattern.methods={vql_Pattern_m_toString}

# vql_VQLImportSection class attributes and methods
vql_VQLImportSection_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_VQLImportSection.methods={vql_VQLImportSection_m_toString}

# XImportSection class attributes and methods

# vql_PackageImport class attributes and methods
vql_PackageImport_alias: Property = Property(name="alias", type=StringType)
vql_PackageImport_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PackageImport.attributes={vql_PackageImport_alias}
vql_PackageImport.methods={vql_PackageImport_m_toString}

# vql_Annotation class attributes and methods
vql_Annotation_name: Property = Property(name="name", type=StringType)
vql_Annotation_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Annotation.attributes={vql_Annotation_name}
vql_Annotation.methods={vql_Annotation_m_toString}

# vql_Modifiers class attributes and methods
vql_Modifiers_private: Property = Property(name="private", type=BooleanType)
vql_Modifiers_execution: Property = Property(name="execution", type=StringType)
vql_Modifiers_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Modifiers.attributes={vql_Modifiers_private, vql_Modifiers_execution}
vql_Modifiers.methods={vql_Modifiers_m_toString}

# vql_Variable class attributes and methods
vql_Variable_name: Property = Property(name="name", type=StringType)
vql_Variable_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Variable.attributes={vql_Variable_name}
vql_Variable.methods={vql_Variable_m_toString}

# vql_EClassifierConstraint class attributes and methods
vql_EClassifierConstraint_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_EClassifierConstraint.methods={vql_EClassifierConstraint_m_toString}

# Constraint class attributes and methods

# UnaryTypeConstraint class attributes and methods

# vql_EnumValue class attributes and methods
vql_EnumValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_EnumValue.methods={vql_EnumValue_m_toString}

# ValueReference class attributes and methods

# vql_EEnum class attributes and methods

# vql_EEnumLiteral class attributes and methods

# vql_PatternModel class attributes and methods
vql_PatternModel_packageName: Property = Property(name="packageName", type=StringType)
vql_PatternModel_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PatternModel.attributes={vql_PatternModel_packageName}
vql_PatternModel.methods={vql_PatternModel_m_toString}

# vql_ClassType class attributes and methods
vql_ClassType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_ClassType.methods={vql_ClassType_m_toString}

# EntityType class attributes and methods

# vql_EClassifier class attributes and methods

# vql_ReferenceType class attributes and methods
vql_ReferenceType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_ReferenceType.methods={vql_ReferenceType_m_toString}

# RelationType class attributes and methods

# vql_EStructuralFeature class attributes and methods

# vql_VariableReference class attributes and methods
vql_VariableReference_aggregator: Property = Property(name="aggregator", type=BooleanType)
vql_VariableReference_var: Property = Property(name="var", type=StringType)
vql_VariableReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_VariableReference.attributes={vql_VariableReference_aggregator, vql_VariableReference_var}
vql_VariableReference.methods={vql_VariableReference_m_toString}

# vql_PatternBody class attributes and methods
vql_PatternBody_name: Property = Property(name="name", type=StringType)
vql_PatternBody_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PatternBody.attributes={vql_PatternBody_name}
vql_PatternBody.methods={vql_PatternBody_m_toString}

# vql_AnnotationParameter class attributes and methods
vql_AnnotationParameter_name: Property = Property(name="name", type=StringType)
vql_AnnotationParameter_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_AnnotationParameter.attributes={vql_AnnotationParameter_name}
vql_AnnotationParameter.methods={vql_AnnotationParameter_m_toString}

# vql_ValueReference class attributes and methods
vql_ValueReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_ValueReference.methods={vql_ValueReference_m_toString}

# vql_Expression class attributes and methods
vql_Expression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Expression.methods={vql_Expression_m_toString}

# Expression class attributes and methods

# vql_Type class attributes and methods
vql_Type_typename: Property = Property(name="typename", type=StringType)
vql_Type_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Type.attributes={vql_Type_typename}
vql_Type.methods={vql_Type_m_toString}

# vql_ComputationValue class attributes and methods
vql_ComputationValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_ComputationValue.methods={vql_ComputationValue_m_toString}

# vql_ParameterRef class attributes and methods
vql_ParameterRef_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_ParameterRef.methods={vql_ParameterRef_m_toString}

# Variable class attributes and methods

# vql_Parameter class attributes and methods
vql_Parameter_direction: Property = Property(name="direction", type=StringType)
vql_Parameter_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_Parameter.attributes={vql_Parameter_direction}
vql_Parameter.methods={vql_Parameter_m_toString}

# vql_LocalVariable class attributes and methods
vql_LocalVariable_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_LocalVariable.methods={vql_LocalVariable_m_toString}

# vql_EntityType class attributes and methods

# Type class attributes and methods

# vql_Constraint class attributes and methods

# vql_PatternCall class attributes and methods
vql_PatternCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PatternCall.methods={vql_PatternCall_m_toString}

# CallableRelation class attributes and methods

# vql_LiteralValueReference class attributes and methods
vql_LiteralValueReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_LiteralValueReference.methods={vql_LiteralValueReference_m_toString}

# vql_CheckConstraint class attributes and methods
vql_CheckConstraint_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_CheckConstraint.methods={vql_CheckConstraint_m_toString}

# vql_XExpression class attributes and methods

# vql_PathExpressionConstraint class attributes and methods
vql_PathExpressionConstraint_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PathExpressionConstraint.methods={vql_PathExpressionConstraint_m_toString}

# vql_JavaType class attributes and methods
vql_JavaType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_JavaType.methods={vql_JavaType_m_toString}

# vql_JvmDeclaredType class attributes and methods

# vql_RelationType class attributes and methods
vql_RelationType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_RelationType.methods={vql_RelationType_m_toString}

# vql_TypeCheckConstraint class attributes and methods
vql_TypeCheckConstraint_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_TypeCheckConstraint.methods={vql_TypeCheckConstraint_m_toString}

# vql_PatternCompositionConstraint class attributes and methods
vql_PatternCompositionConstraint_negative: Property = Property(name="negative", type=BooleanType)
vql_PatternCompositionConstraint_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_PatternCompositionConstraint.attributes={vql_PatternCompositionConstraint_negative}
vql_PatternCompositionConstraint.methods={vql_PatternCompositionConstraint_m_toString}

# vql_CallableRelation class attributes and methods
vql_CallableRelation_transitive: Property = Property(name="transitive", type=StringType)
vql_CallableRelation.attributes={vql_CallableRelation_transitive}

# vql_CompareConstraint class attributes and methods
vql_CompareConstraint_feature: Property = Property(name="feature", type=StringType)
vql_CompareConstraint_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_CompareConstraint.attributes={vql_CompareConstraint_feature}
vql_CompareConstraint.methods={vql_CompareConstraint_m_toString}

# vql_FunctionEvaluationValue class attributes and methods
vql_FunctionEvaluationValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_FunctionEvaluationValue.methods={vql_FunctionEvaluationValue_m_toString}

# ComputationValue class attributes and methods

# vql_AggregatedValue class attributes and methods
vql_AggregatedValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_AggregatedValue.methods={vql_AggregatedValue_m_toString}

# vql_JvmType class attributes and methods

# vql_StringValue class attributes and methods
vql_StringValue_value: Property = Property(name="value", type=StringType)
vql_StringValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_StringValue.attributes={vql_StringValue_value}
vql_StringValue.methods={vql_StringValue_m_toString}

# LiteralValueReference class attributes and methods

# vql_NumberValue class attributes and methods
vql_NumberValue_negative: Property = Property(name="negative", type=BooleanType)
vql_NumberValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_NumberValue.attributes={vql_NumberValue_negative}
vql_NumberValue.methods={vql_NumberValue_m_toString}

# vql_XNumberLiteral class attributes and methods

# vql_BoolValue class attributes and methods
vql_BoolValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_BoolValue.methods={vql_BoolValue_m_toString}

# vql_XBooleanLiteral class attributes and methods

# vql_ListValue class attributes and methods
vql_ListValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
vql_ListValue.methods={vql_ListValue_m_toString}

# vql_UnaryTypeConstraint class attributes and methods

# Relationships
patternImport1: BinaryAssociation = BinaryAssociation(
    name="patternImport1",
    ends={
        Property(name="vql_PatternImport", type=vql_VQLImportSection, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_VQLImportSection2", type=vql_PatternImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage3: BinaryAssociation = BinaryAssociation(
    name="ePackage3",
    ends={
        Property(name="vql_EPackage", type=vql_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PackageImport4", type=vql_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
pattern5: BinaryAssociation = BinaryAssociation(
    name="pattern5",
    ends={
        Property(name="vql_Pattern", type=vql_PatternImport, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternImport6", type=vql_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
packageImport0: BinaryAssociation = BinaryAssociation(
    name="packageImport0",
    ends={
        Property(name="vql_PackageImport", type=vql_VQLImportSection, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_VQLImportSection", type=vql_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refname22: BinaryAssociation = BinaryAssociation(
    name="refname22",
    ends={
        Property(name="vql_EStructuralFeature", type=vql_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_ReferenceType", type=vql_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
annotations23: BinaryAssociation = BinaryAssociation(
    name="annotations23",
    ends={
        Property(name="vql_Annotation", type=vql_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_Pattern24", type=vql_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers25: BinaryAssociation = BinaryAssociation(
    name="modifiers25",
    ends={
        Property(name="vql_Modifiers", type=vql_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_Pattern26", type=vql_Modifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters27: BinaryAssociation = BinaryAssociation(
    name="parameters27",
    ends={
        Property(name="vql_Variable", type=vql_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_Pattern28", type=vql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patterns7: BinaryAssociation = BinaryAssociation(
    name="patterns7",
    ends={
        Property(name="vql_Pattern9", type=vql_PatternImport, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternImport8", type=vql_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration10: BinaryAssociation = BinaryAssociation(
    name="enumeration10",
    ends={
        Property(name="vql_EEnum", type=vql_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_EnumValue", type=vql_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
literal11: BinaryAssociation = BinaryAssociation(
    name="literal11",
    ends={
        Property(name="vql_EEnumLiteral", type=vql_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_EnumValue12", type=vql_EEnumLiteral, multiplicity=Multiplicity(0, 1))
    }
)
importPackages13: BinaryAssociation = BinaryAssociation(
    name="importPackages13",
    ends={
        Property(name="vql_VQLImportSection14", type=vql_PatternModel, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternModel", type=vql_VQLImportSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns15: BinaryAssociation = BinaryAssociation(
    name="patterns15",
    ends={
        Property(name="vql_Pattern17", type=vql_PatternModel, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternModel16", type=vql_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel18: BinaryAssociation = BinaryAssociation(
    name="metamodel18",
    ends={
        Property(name="vql_PackageImport19", type=vql_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_ClassType", type=vql_PackageImport, multiplicity=Multiplicity(0, 1))
    }
)
classname20: BinaryAssociation = BinaryAssociation(
    name="classname20",
    ends={
        Property(name="vql_EClassifier", type=vql_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_ClassType21", type=vql_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
variable37: BinaryAssociation = BinaryAssociation(
    name="variable37",
    ends={
        Property(name="vql_Variable38", type=vql_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_VariableReference", type=vql_Variable, multiplicity=Multiplicity(0, 1))
    }
)
bodies29: BinaryAssociation = BinaryAssociation(
    name="bodies29",
    ends={
        Property(name="vql_PatternBody", type=vql_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_Pattern30", type=vql_PatternBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="vql_AnnotationParameter", type=vql_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_Annotation32", type=vql_AnnotationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value33: BinaryAssociation = BinaryAssociation(
    name="value33",
    ends={
        Property(name="vql_ValueReference", type=vql_AnnotationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_AnnotationParameter34", type=vql_ValueReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="vql_Type", type=vql_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_Variable36", type=vql_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredParam49: BinaryAssociation = BinaryAssociation(
    name="referredParam49",
    ends={
        Property(name="vql_Variable50", type=vql_ParameterRef, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_ParameterRef", type=vql_Variable, multiplicity=Multiplicity(0, 1))
    }
)
constraints39: BinaryAssociation = BinaryAssociation(
    name="constraints39",
    ends={
        Property(name="vql_Constraint", type=vql_PatternBody, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternBody40", type=vql_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables41: BinaryAssociation = BinaryAssociation(
    name="variables41",
    ends={
        Property(name="vql_Variable43", type=vql_PatternBody, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternBody42", type=vql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patternRef44: BinaryAssociation = BinaryAssociation(
    name="patternRef44",
    ends={
        Property(name="vql_Pattern45", type=vql_PatternCall, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternCall", type=vql_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
parameters46: BinaryAssociation = BinaryAssociation(
    name="parameters46",
    ends={
        Property(name="vql_ValueReference48", type=vql_PatternCall, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternCall47", type=vql_ValueReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression58: BinaryAssociation = BinaryAssociation(
    name="expression58",
    ends={
        Property(name="vql_XExpression", type=vql_CheckConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_CheckConstraint", type=vql_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edgeTypes59: BinaryAssociation = BinaryAssociation(
    name="edgeTypes59",
    ends={
        Property(name="vql_ReferenceType60", type=vql_PathExpressionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PathExpressionConstraint", type=vql_ReferenceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceType61: BinaryAssociation = BinaryAssociation(
    name="sourceType61",
    ends={
        Property(name="vql_ClassType63", type=vql_PathExpressionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PathExpressionConstraint62", type=vql_ClassType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src64: BinaryAssociation = BinaryAssociation(
    name="src64",
    ends={
        Property(name="vql_VariableReference66", type=vql_PathExpressionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PathExpressionConstraint65", type=vql_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classRef51: BinaryAssociation = BinaryAssociation(
    name="classRef51",
    ends={
        Property(name="vql_JvmDeclaredType", type=vql_JavaType, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_JavaType", type=vql_JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
call52: BinaryAssociation = BinaryAssociation(
    name="call52",
    ends={
        Property(name="vql_CallableRelation", type=vql_PatternCompositionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PatternCompositionConstraint", type=vql_CallableRelation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand53: BinaryAssociation = BinaryAssociation(
    name="leftOperand53",
    ends={
        Property(name="vql_ValueReference54", type=vql_CompareConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_CompareConstraint", type=vql_ValueReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand55: BinaryAssociation = BinaryAssociation(
    name="rightOperand55",
    ends={
        Property(name="vql_ValueReference57", type=vql_CompareConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_CompareConstraint56", type=vql_ValueReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values72: BinaryAssociation = BinaryAssociation(
    name="values72",
    ends={
        Property(name="vql_ValueReference73", type=vql_ListValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_ListValue", type=vql_ValueReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="vql_XExpression75", type=vql_FunctionEvaluationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_FunctionEvaluationValue", type=vql_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregator76: BinaryAssociation = BinaryAssociation(
    name="aggregator76",
    ends={
        Property(name="vql_JvmDeclaredType77", type=vql_AggregatedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_AggregatedValue", type=vql_JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
call78: BinaryAssociation = BinaryAssociation(
    name="call78",
    ends={
        Property(name="vql_CallableRelation80", type=vql_AggregatedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_AggregatedValue79", type=vql_CallableRelation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType81: BinaryAssociation = BinaryAssociation(
    name="aggregateType81",
    ends={
        Property(name="vql_JvmType", type=vql_AggregatedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_AggregatedValue82", type=vql_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
dst67: BinaryAssociation = BinaryAssociation(
    name="dst67",
    ends={
        Property(name="vql_ValueReference69", type=vql_PathExpressionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_PathExpressionConstraint68", type=vql_ValueReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value70: BinaryAssociation = BinaryAssociation(
    name="value70",
    ends={
        Property(name="vql_XNumberLiteral", type=vql_NumberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_NumberValue", type=vql_XNumberLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="vql_XBooleanLiteral", type=vql_BoolValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_BoolValue", type=vql_XBooleanLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="vql_EntityType", type=vql_UnaryTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_UnaryTypeConstraint", type=vql_EntityType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var84: BinaryAssociation = BinaryAssociation(
    name="var84",
    ends={
        Property(name="vql_VariableReference86", type=vql_UnaryTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vql_UnaryTypeConstraint85", type=vql_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_vql_VQLImportSection_XImportSection = Generalization(general=XImportSection, specific=vql_VQLImportSection)
gen_vql_EClassifierConstraint_Constraint = Generalization(general=Constraint, specific=vql_EClassifierConstraint)
gen_vql_EClassifierConstraint_UnaryTypeConstraint = Generalization(general=UnaryTypeConstraint, specific=vql_EClassifierConstraint)
gen_vql_EnumValue_ValueReference = Generalization(general=ValueReference, specific=vql_EnumValue)
gen_vql_ClassType_EntityType = Generalization(general=EntityType, specific=vql_ClassType)
gen_vql_ReferenceType_RelationType = Generalization(general=RelationType, specific=vql_ReferenceType)
gen_vql_VariableReference_ValueReference = Generalization(general=ValueReference, specific=vql_VariableReference)
gen_vql_Variable_Expression = Generalization(general=Expression, specific=vql_Variable)
gen_vql_ComputationValue_ValueReference = Generalization(general=ValueReference, specific=vql_ComputationValue)
gen_vql_ParameterRef_Variable = Generalization(general=Variable, specific=vql_ParameterRef)
gen_vql_Parameter_Variable = Generalization(general=Variable, specific=vql_Parameter)
gen_vql_LocalVariable_Variable = Generalization(general=Variable, specific=vql_LocalVariable)
gen_vql_EntityType_Type = Generalization(general=Type, specific=vql_EntityType)
gen_vql_PatternCall_CallableRelation = Generalization(general=CallableRelation, specific=vql_PatternCall)
gen_vql_ValueReference_Expression = Generalization(general=Expression, specific=vql_ValueReference)
gen_vql_LiteralValueReference_ValueReference = Generalization(general=ValueReference, specific=vql_LiteralValueReference)
gen_vql_CheckConstraint_Constraint = Generalization(general=Constraint, specific=vql_CheckConstraint)
gen_vql_PathExpressionConstraint_Constraint = Generalization(general=Constraint, specific=vql_PathExpressionConstraint)
gen_vql_PathExpressionConstraint_CallableRelation = Generalization(general=CallableRelation, specific=vql_PathExpressionConstraint)
gen_vql_JavaType_EntityType = Generalization(general=EntityType, specific=vql_JavaType)
gen_vql_RelationType_Type = Generalization(general=Type, specific=vql_RelationType)
gen_vql_TypeCheckConstraint_Constraint = Generalization(general=Constraint, specific=vql_TypeCheckConstraint)
gen_vql_TypeCheckConstraint_UnaryTypeConstraint = Generalization(general=UnaryTypeConstraint, specific=vql_TypeCheckConstraint)
gen_vql_PatternCompositionConstraint_Constraint = Generalization(general=Constraint, specific=vql_PatternCompositionConstraint)
gen_vql_CompareConstraint_Constraint = Generalization(general=Constraint, specific=vql_CompareConstraint)
gen_vql_FunctionEvaluationValue_ComputationValue = Generalization(general=ComputationValue, specific=vql_FunctionEvaluationValue)
gen_vql_AggregatedValue_ComputationValue = Generalization(general=ComputationValue, specific=vql_AggregatedValue)
gen_vql_StringValue_LiteralValueReference = Generalization(general=LiteralValueReference, specific=vql_StringValue)
gen_vql_NumberValue_LiteralValueReference = Generalization(general=LiteralValueReference, specific=vql_NumberValue)
gen_vql_BoolValue_LiteralValueReference = Generalization(general=LiteralValueReference, specific=vql_BoolValue)
gen_vql_ListValue_LiteralValueReference = Generalization(general=LiteralValueReference, specific=vql_ListValue)
gen_vql_UnaryTypeConstraint_CallableRelation = Generalization(general=CallableRelation, specific=vql_UnaryTypeConstraint)

# Domain Model
domain_model = DomainModel(
    name="vql",
    types={vql_PatternImport, vql_EPackage, vql_Pattern, vql_VQLImportSection, XImportSection, vql_PackageImport, vql_Annotation, vql_Modifiers, vql_Variable, vql_EClassifierConstraint, Constraint, UnaryTypeConstraint, vql_EnumValue, ValueReference, vql_EEnum, vql_EEnumLiteral, vql_PatternModel, vql_ClassType, EntityType, vql_EClassifier, vql_ReferenceType, RelationType, vql_EStructuralFeature, vql_VariableReference, vql_PatternBody, vql_AnnotationParameter, vql_ValueReference, vql_Expression, Expression, vql_Type, vql_ComputationValue, vql_ParameterRef, Variable, vql_Parameter, vql_LocalVariable, vql_EntityType, Type, vql_Constraint, vql_PatternCall, CallableRelation, vql_LiteralValueReference, vql_CheckConstraint, vql_XExpression, vql_PathExpressionConstraint, vql_JavaType, vql_JvmDeclaredType, vql_RelationType, vql_TypeCheckConstraint, vql_PatternCompositionConstraint, vql_CallableRelation, vql_CompareConstraint, vql_FunctionEvaluationValue, ComputationValue, vql_AggregatedValue, vql_JvmType, vql_StringValue, LiteralValueReference, vql_NumberValue, vql_XNumberLiteral, vql_BoolValue, vql_XBooleanLiteral, vql_ListValue, vql_UnaryTypeConstraint, ExecutionType, ParameterDirection, CompareFeature, ClosureType},
    associations={patternImport1, ePackage3, pattern5, packageImport0, refname22, annotations23, modifiers25, parameters27, patterns7, enumeration10, literal11, importPackages13, patterns15, metamodel18, classname20, variable37, bodies29, parameters31, value33, type35, referredParam49, constraints39, variables41, patternRef44, parameters46, expression58, edgeTypes59, sourceType61, src64, classRef51, call52, leftOperand53, rightOperand55, values72, expression74, aggregator76, call78, aggregateType81, dst67, value70, value71, type83, var84},
    generalizations={gen_vql_VQLImportSection_XImportSection, gen_vql_EClassifierConstraint_Constraint, gen_vql_EClassifierConstraint_UnaryTypeConstraint, gen_vql_EnumValue_ValueReference, gen_vql_ClassType_EntityType, gen_vql_ReferenceType_RelationType, gen_vql_VariableReference_ValueReference, gen_vql_Variable_Expression, gen_vql_ComputationValue_ValueReference, gen_vql_ParameterRef_Variable, gen_vql_Parameter_Variable, gen_vql_LocalVariable_Variable, gen_vql_EntityType_Type, gen_vql_PatternCall_CallableRelation, gen_vql_ValueReference_Expression, gen_vql_LiteralValueReference_ValueReference, gen_vql_CheckConstraint_Constraint, gen_vql_PathExpressionConstraint_Constraint, gen_vql_PathExpressionConstraint_CallableRelation, gen_vql_JavaType_EntityType, gen_vql_RelationType_Type, gen_vql_TypeCheckConstraint_Constraint, gen_vql_TypeCheckConstraint_UnaryTypeConstraint, gen_vql_PatternCompositionConstraint_Constraint, gen_vql_CompareConstraint_Constraint, gen_vql_FunctionEvaluationValue_ComputationValue, gen_vql_AggregatedValue_ComputationValue, gen_vql_StringValue_LiteralValueReference, gen_vql_NumberValue_LiteralValueReference, gen_vql_BoolValue_LiteralValueReference, gen_vql_ListValue_LiteralValueReference, gen_vql_UnaryTypeConstraint_CallableRelation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)