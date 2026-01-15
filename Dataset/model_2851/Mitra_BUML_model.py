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
VisibilityModifier: Enumeration = Enumeration(
    name="VisibilityModifier",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private")
    }
)

ExecutionModifier: Enumeration = Enumeration(
    name="ExecutionModifier",
    literals={
            EnumerationLiteral(name="called"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="manual"),
			EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="confirm")
    }
)

PrimitiveTypeSpec: Enumeration = Enumeration(
    name="PrimitiveTypeSpec",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="any"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="real"),
			EnumerationLiteral(name="type")
    }
)

ParameterModifier: Enumeration = Enumeration(
    name="ParameterModifier",
    literals={
            EnumerationLiteral(name="use"),
			EnumerationLiteral(name="from"),
			EnumerationLiteral(name="into"),
			EnumerationLiteral(name="return"),
			EnumerationLiteral(name="create")
    }
)

CollectionTypeSpec: Enumeration = Enumeration(
    name="CollectionTypeSpec",
    literals={
            EnumerationLiteral(name="Collection"),
			EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="andsc"),
			EnumerationLiteral(name="orsc")
    }
)

EqualityOperator: Enumeration = Enumeration(
    name="EqualityOperator",
    literals={
            EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="geq")
    }
)

MathOperator: Enumeration = Enumeration(
    name="MathOperator",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="sub"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div")
    }
)

UnaryMathOperator: Enumeration = Enumeration(
    name="UnaryMathOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="set"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="sub")
    }
)

PPOperator: Enumeration = Enumeration(
    name="PPOperator",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="inc"),
			EnumerationLiteral(name="dec")
    }
)

AnnotationTargetSpec: Enumeration = Enumeration(
    name="AnnotationTargetSpec",
    literals={
            EnumerationLiteral(name="module"),
			EnumerationLiteral(name="rule"),
			EnumerationLiteral(name="parameter")
    }
)

# Classes
mitra_ModuleReference = Class(name="mitra::ModuleReference")
mitra_Module = Class(name="mitra::Module")
mitra_MetamodelDeclaration = Class(name="mitra::MetamodelDeclaration")
mitra_AnnotationsDefinition = Class(name="mitra::AnnotationsDefinition")
mitra_RuleDeclaration = Class(name="mitra::RuleDeclaration")
mitra_Property = Class(name="mitra::Property")
mitra_Annotation = Class(name="mitra::Annotation")
mitra_FormalParameter = Class(name="mitra::FormalParameter")
mitra_ReturnParameter = Class(name="mitra::ReturnParameter")
mitra_SimpleRuleReference = Class(name="mitra::SimpleRuleReference")
mitra_QualifiedParameterReference = Class(name="mitra::QualifiedParameterReference")
mitra_Trigger = Class(name="mitra::Trigger")
mitra_JavaSpec = Class(name="mitra::JavaSpec")
mitra_Block = Class(name="mitra::Block")
mitra_RuleReference = Class(name="mitra::RuleReference")
RuleReference = Class(name="RuleReference")
mitra_SimpleParameterReference = Class(name="mitra::SimpleParameterReference")
mitra_QualifiedRuleReference = Class(name="mitra::QualifiedRuleReference")
mitra_ParameterReference = Class(name="mitra::ParameterReference")
ParameterReference = Class(name="ParameterReference")
mitra_Parameter = Class(name="mitra::Parameter")
mitra_Type = Class(name="mitra::Type")
Parameter_ = Class(name="Parameter")
mitra_TypedVarDeclaration = Class(name="mitra::TypedVarDeclaration")
mitra_Expression = Class(name="mitra::Expression")
mitra_ReferenceType = Class(name="mitra::ReferenceType")
Type = Class(name="Type")
mitra_EClassifier = Class(name="mitra::EClassifier")
mitra_PrimitiveType = Class(name="mitra::PrimitiveType")
Statement = Class(name="Statement")
mitra_BlockStatement = Class(name="mitra::BlockStatement")
mitra_Statement = Class(name="mitra::Statement")
BlockStatement = Class(name="BlockStatement")
mitra_LocalVariableDeclarationStatement = Class(name="mitra::LocalVariableDeclarationStatement")
mitra_LocalVariableDeclaration = Class(name="mitra::LocalVariableDeclaration")
mitra_CollectionType = Class(name="mitra::CollectionType")
VarDeclaration = Class(name="VarDeclaration")
mitra_InferredVarDeclaration = Class(name="mitra::InferredVarDeclaration")
mitra_ExpressionStatement = Class(name="mitra::ExpressionStatement")
mitra_StatementExpression = Class(name="mitra::StatementExpression")
mitra_EmptyStatement = Class(name="mitra::EmptyStatement")
mitra_ReturnStatement = Class(name="mitra::ReturnStatement")
mitra_IfStatement = Class(name="mitra::IfStatement")
mitra_VarDeclaration = Class(name="mitra::VarDeclaration")
mitra_DoStatement = Class(name="mitra::DoStatement")
mitra_ForInit = Class(name="mitra::ForInit")
mitra_ForUpdate = Class(name="mitra::ForUpdate")
mitra_ForStatement = Class(name="mitra::ForStatement")
mitra_WhileStatement = Class(name="mitra::WhileStatement")
mitra_BreakStatement = Class(name="mitra::BreakStatement")
mitra_ThrowStatement = Class(name="mitra::ThrowStatement")
mitra_TryStatement = Class(name="mitra::TryStatement")
mitra_Catch = Class(name="mitra::Catch")
mitra_LoopVariable = Class(name="mitra::LoopVariable")
mitra_TerminalExpression = Class(name="mitra::TerminalExpression")
mitra_IntLiteral = Class(name="mitra::IntLiteral")
mitra_RealLiteral = Class(name="mitra::RealLiteral")
mitra_BooleanLiteral = Class(name="mitra::BooleanLiteral")
mitra_NullLiteral = Class(name="mitra::NullLiteral")
mitra_ClassInstanceCreationExpression = Class(name="mitra::ClassInstanceCreationExpression")
StatementExpression = Class(name="StatementExpression")
Expression = Class(name="Expression")
mitra_Literal = Class(name="mitra::Literal")
TerminalExpression = Class(name="TerminalExpression")
mitra_StringLiteral = Class(name="mitra::StringLiteral")
Literal = Class(name="Literal")
mitra_RuleInvocationSuper = Class(name="mitra::RuleInvocationSuper")
mitra_Feature = Class(name="mitra::Feature")
mitra_MethodInvocation = Class(name="mitra::MethodInvocation")
Feature = Class(name="Feature")
mitra_RuleInvocation = Class(name="mitra::RuleInvocation")
mitra_NativeOperationInvocation = Class(name="mitra::NativeOperationInvocation")
mitra_MetamodelFeature = Class(name="mitra::MetamodelFeature")
mitra_FeatureField = Class(name="mitra::FeatureField")
mitra_VariableAccess = Class(name="mitra::VariableAccess")
mitra_FeatureMethodInvocation = Class(name="mitra::FeatureMethodInvocation")
MethodInvocation = Class(name="MethodInvocation")
MetamodelFeature = Class(name="MetamodelFeature")
mitra_AnnotationDecl = Class(name="mitra::AnnotationDecl")
mitra_StaticAccess = Class(name="mitra::StaticAccess")
mitra_AnnotationPropertyDecl = Class(name="mitra::AnnotationPropertyDecl")
mitra_AnnotationProperty = Class(name="mitra::AnnotationProperty")
mitra_Assignment = Class(name="mitra::Assignment")
mitra_IteratorExpression = Class(name="mitra::IteratorExpression")
mitra_BooleanExpression = Class(name="mitra::BooleanExpression")
mitra_EqualityExpression = Class(name="mitra::EqualityExpression")
mitra_MathExpression = Class(name="mitra::MathExpression")
mitra_UnaryCastExpression = Class(name="mitra::UnaryCastExpression")
mitra_RelationalExpression = Class(name="mitra::RelationalExpression")
mitra_InstanceOfExpression = Class(name="mitra::InstanceOfExpression")
mitra_UnaryBooleanExpression = Class(name="mitra::UnaryBooleanExpression")
mitra_UnaryMathExpression = Class(name="mitra::UnaryMathExpression")

# mitra_ModuleReference class attributes and methods

# mitra_Module class attributes and methods
mitra_Module_packageName: Property = Property(name="packageName", type=StringType)
mitra_Module_name: Property = Property(name="name", type=StringType)
mitra_Module_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_Module.attributes={mitra_Module_name, mitra_Module_packageName}
mitra_Module.methods={mitra_Module_m_toString}

# mitra_MetamodelDeclaration class attributes and methods
mitra_MetamodelDeclaration_type: Property = Property(name="type", type=StringType)
mitra_MetamodelDeclaration_name: Property = Property(name="name", type=StringType)
mitra_MetamodelDeclaration_replaces: Property = Property(name="replaces", type=StringType)
mitra_MetamodelDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_MetamodelDeclaration.attributes={mitra_MetamodelDeclaration_replaces, mitra_MetamodelDeclaration_name, mitra_MetamodelDeclaration_type}
mitra_MetamodelDeclaration.methods={mitra_MetamodelDeclaration_m_toString}

# mitra_AnnotationsDefinition class attributes and methods

# mitra_RuleDeclaration class attributes and methods
mitra_RuleDeclaration_visibility: Property = Property(name="visibility", type=StringType)
mitra_RuleDeclaration_exec: Property = Property(name="exec", type=StringType)
mitra_RuleDeclaration_traced: Property = Property(name="traced", type=BooleanType)
mitra_RuleDeclaration_stealth: Property = Property(name="stealth", type=BooleanType)
mitra_RuleDeclaration_virtual: Property = Property(name="virtual", type=BooleanType)
mitra_RuleDeclaration_multi: Property = Property(name="multi", type=BooleanType)
mitra_RuleDeclaration_name: Property = Property(name="name", type=StringType)
mitra_RuleDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_RuleDeclaration.attributes={mitra_RuleDeclaration_multi, mitra_RuleDeclaration_stealth, mitra_RuleDeclaration_virtual, mitra_RuleDeclaration_visibility, mitra_RuleDeclaration_name, mitra_RuleDeclaration_exec, mitra_RuleDeclaration_traced}
mitra_RuleDeclaration.methods={mitra_RuleDeclaration_m_toString}

# mitra_Property class attributes and methods
mitra_Property_value: Property = Property(name="value", type=StringType)
mitra_Property_name: Property = Property(name="name", type=StringType)
mitra_Property_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_Property.attributes={mitra_Property_name, mitra_Property_value}
mitra_Property.methods={mitra_Property_m_toString}

# mitra_Annotation class attributes and methods

# mitra_FormalParameter class attributes and methods
mitra_FormalParameter_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_FormalParameter.methods={mitra_FormalParameter_m_toString}

# mitra_ReturnParameter class attributes and methods
mitra_ReturnParameter_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_ReturnParameter.methods={mitra_ReturnParameter_m_toString}

# mitra_SimpleRuleReference class attributes and methods
mitra_SimpleRuleReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_SimpleRuleReference.methods={mitra_SimpleRuleReference_m_toString}

# mitra_QualifiedParameterReference class attributes and methods
mitra_QualifiedParameterReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_QualifiedParameterReference.methods={mitra_QualifiedParameterReference_m_toString}

# mitra_Trigger class attributes and methods

# mitra_JavaSpec class attributes and methods

# mitra_Block class attributes and methods

# mitra_RuleReference class attributes and methods

# RuleReference class attributes and methods

# mitra_SimpleParameterReference class attributes and methods
mitra_SimpleParameterReference_name: Property = Property(name="name", type=StringType)
mitra_SimpleParameterReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_SimpleParameterReference.attributes={mitra_SimpleParameterReference_name}
mitra_SimpleParameterReference.methods={mitra_SimpleParameterReference_m_toString}

# mitra_QualifiedRuleReference class attributes and methods
mitra_QualifiedRuleReference_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_QualifiedRuleReference.methods={mitra_QualifiedRuleReference_m_toString}

# mitra_ParameterReference class attributes and methods

# ParameterReference class attributes and methods

# mitra_Parameter class attributes and methods
mitra_Parameter_modifier: Property = Property(name="modifier", type=StringType)
mitra_Parameter.attributes={mitra_Parameter_modifier}

# mitra_Type class attributes and methods

# Parameter class attributes and methods

# mitra_TypedVarDeclaration class attributes and methods

# mitra_Expression class attributes and methods

# mitra_ReferenceType class attributes and methods
mitra_ReferenceType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_ReferenceType.methods={mitra_ReferenceType_m_toString}

# Type class attributes and methods

# mitra_EClassifier class attributes and methods

# mitra_PrimitiveType class attributes and methods
mitra_PrimitiveType_primitiveType: Property = Property(name="primitiveType", type=StringType)
mitra_PrimitiveType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_PrimitiveType.attributes={mitra_PrimitiveType_primitiveType}
mitra_PrimitiveType.methods={mitra_PrimitiveType_m_toString}

# Statement class attributes and methods

# mitra_BlockStatement class attributes and methods

# mitra_Statement class attributes and methods

# BlockStatement class attributes and methods

# mitra_LocalVariableDeclarationStatement class attributes and methods

# mitra_LocalVariableDeclaration class attributes and methods

# mitra_CollectionType class attributes and methods
mitra_CollectionType_collectionType: Property = Property(name="collectionType", type=StringType)
mitra_CollectionType_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_CollectionType.attributes={mitra_CollectionType_collectionType}
mitra_CollectionType.methods={mitra_CollectionType_m_toString}

# VarDeclaration class attributes and methods

# mitra_InferredVarDeclaration class attributes and methods

# mitra_ExpressionStatement class attributes and methods

# mitra_StatementExpression class attributes and methods

# mitra_EmptyStatement class attributes and methods

# mitra_ReturnStatement class attributes and methods

# mitra_IfStatement class attributes and methods

# mitra_VarDeclaration class attributes and methods
mitra_VarDeclaration_name: Property = Property(name="name", type=StringType)
mitra_VarDeclaration.attributes={mitra_VarDeclaration_name}

# mitra_DoStatement class attributes and methods

# mitra_ForInit class attributes and methods

# mitra_ForUpdate class attributes and methods

# mitra_ForStatement class attributes and methods

# mitra_WhileStatement class attributes and methods

# mitra_BreakStatement class attributes and methods

# mitra_ThrowStatement class attributes and methods

# mitra_TryStatement class attributes and methods

# mitra_Catch class attributes and methods

# mitra_LoopVariable class attributes and methods

# mitra_TerminalExpression class attributes and methods

# mitra_IntLiteral class attributes and methods
mitra_IntLiteral_intValue: Property = Property(name="intValue", type=IntegerType)
mitra_IntLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_IntLiteral.attributes={mitra_IntLiteral_intValue}
mitra_IntLiteral.methods={mitra_IntLiteral_m_toString}

# mitra_RealLiteral class attributes and methods
mitra_RealLiteral_floatValue: Property = Property(name="floatValue", type=StringType)
mitra_RealLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_RealLiteral.attributes={mitra_RealLiteral_floatValue}
mitra_RealLiteral.methods={mitra_RealLiteral_m_toString}

# mitra_BooleanLiteral class attributes and methods
mitra_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=BooleanType)
mitra_BooleanLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_BooleanLiteral.attributes={mitra_BooleanLiteral_booleanValue}
mitra_BooleanLiteral.methods={mitra_BooleanLiteral_m_toString}

# mitra_NullLiteral class attributes and methods

# mitra_ClassInstanceCreationExpression class attributes and methods

# StatementExpression class attributes and methods

# Expression class attributes and methods

# mitra_Literal class attributes and methods

# TerminalExpression class attributes and methods

# mitra_StringLiteral class attributes and methods
mitra_StringLiteral_stringValue: Property = Property(name="stringValue", type=StringType)
mitra_StringLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_StringLiteral.attributes={mitra_StringLiteral_stringValue}
mitra_StringLiteral.methods={mitra_StringLiteral_m_toString}

# Literal class attributes and methods

# mitra_RuleInvocationSuper class attributes and methods
mitra_RuleInvocationSuper_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_RuleInvocationSuper.methods={mitra_RuleInvocationSuper_m_toString}

# mitra_Feature class attributes and methods
mitra_Feature_name: Property = Property(name="name", type=StringType)
mitra_Feature_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_Feature.attributes={mitra_Feature_name}
mitra_Feature.methods={mitra_Feature_m_toString}

# mitra_MethodInvocation class attributes and methods

# Feature class attributes and methods

# mitra_RuleInvocation class attributes and methods
mitra_RuleInvocation_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_RuleInvocation.methods={mitra_RuleInvocation_m_toString}

# mitra_NativeOperationInvocation class attributes and methods

# mitra_MetamodelFeature class attributes and methods

# mitra_FeatureField class attributes and methods

# mitra_VariableAccess class attributes and methods
mitra_VariableAccess_prefixOperator: Property = Property(name="prefixOperator", type=StringType)
mitra_VariableAccess_postfixOperator: Property = Property(name="postfixOperator", type=StringType)
mitra_VariableAccess_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
mitra_VariableAccess.attributes={mitra_VariableAccess_prefixOperator, mitra_VariableAccess_postfixOperator}
mitra_VariableAccess.methods={mitra_VariableAccess_m_toString}

# mitra_FeatureMethodInvocation class attributes and methods

# MethodInvocation class attributes and methods

# MetamodelFeature class attributes and methods

# mitra_AnnotationDecl class attributes and methods
mitra_AnnotationDecl_name: Property = Property(name="name", type=StringType)
mitra_AnnotationDecl_targets: Property = Property(name="targets", type=StringType)
mitra_AnnotationDecl_many: Property = Property(name="many", type=BooleanType)
mitra_AnnotationDecl_required: Property = Property(name="required", type=BooleanType)
mitra_AnnotationDecl.attributes={mitra_AnnotationDecl_many, mitra_AnnotationDecl_required, mitra_AnnotationDecl_name, mitra_AnnotationDecl_targets}

# mitra_StaticAccess class attributes and methods

# mitra_AnnotationPropertyDecl class attributes and methods
mitra_AnnotationPropertyDecl_name: Property = Property(name="name", type=StringType)
mitra_AnnotationPropertyDecl_required: Property = Property(name="required", type=BooleanType)
mitra_AnnotationPropertyDecl.attributes={mitra_AnnotationPropertyDecl_name, mitra_AnnotationPropertyDecl_required}

# mitra_AnnotationProperty class attributes and methods

# mitra_Assignment class attributes and methods
mitra_Assignment_operator: Property = Property(name="operator", type=StringType)
mitra_Assignment.attributes={mitra_Assignment_operator}

# mitra_IteratorExpression class attributes and methods

# mitra_BooleanExpression class attributes and methods
mitra_BooleanExpression_op: Property = Property(name="op", type=StringType)
mitra_BooleanExpression.attributes={mitra_BooleanExpression_op}

# mitra_EqualityExpression class attributes and methods
mitra_EqualityExpression_op: Property = Property(name="op", type=StringType)
mitra_EqualityExpression.attributes={mitra_EqualityExpression_op}

# mitra_MathExpression class attributes and methods
mitra_MathExpression_op: Property = Property(name="op", type=StringType)
mitra_MathExpression.attributes={mitra_MathExpression_op}

# mitra_UnaryCastExpression class attributes and methods

# mitra_RelationalExpression class attributes and methods
mitra_RelationalExpression_op: Property = Property(name="op", type=StringType)
mitra_RelationalExpression.attributes={mitra_RelationalExpression_op}

# mitra_InstanceOfExpression class attributes and methods

# mitra_UnaryBooleanExpression class attributes and methods

# mitra_UnaryMathExpression class attributes and methods
mitra_UnaryMathExpression_op: Property = Property(name="op", type=StringType)
mitra_UnaryMathExpression.attributes={mitra_UnaryMathExpression_op}

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="mitra_ModuleReference", type=mitra_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Module", type=mitra_ModuleReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodelDeclarations1: BinaryAssociation = BinaryAssociation(
    name="metamodelDeclarations1",
    ends={
        Property(name="mitra_MetamodelDeclaration", type=mitra_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Module2", type=mitra_MetamodelDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationDefinitions3: BinaryAssociation = BinaryAssociation(
    name="annotationDefinitions3",
    ends={
        Property(name="mitra_AnnotationsDefinition", type=mitra_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Module4", type=mitra_AnnotationsDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ruleDeclarations5: BinaryAssociation = BinaryAssociation(
    name="ruleDeclarations5",
    ends={
        Property(name="mitra_RuleDeclaration", type=mitra_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Module6", type=mitra_RuleDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module7: BinaryAssociation = BinaryAssociation(
    name="module7",
    ends={
        Property(name="mitra_Module9", type=mitra_ModuleReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ModuleReference8", type=mitra_Module, multiplicity=Multiplicity(0, 1))
    }
)
properties10: BinaryAssociation = BinaryAssociation(
    name="properties10",
    ends={
        Property(name="mitra_Property", type=mitra_MetamodelDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_MetamodelDeclaration11", type=mitra_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations12: BinaryAssociation = BinaryAssociation(
    name="annotations12",
    ends={
        Property(name="mitra_Annotation", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration13", type=mitra_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameters14: BinaryAssociation = BinaryAssociation(
    name="formalParameters14",
    ends={
        Property(name="mitra_FormalParameter", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration15", type=mitra_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnParameters16: BinaryAssociation = BinaryAssociation(
    name="returnParameters16",
    ends={
        Property(name="mitra_ReturnParameter", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration17", type=mitra_ReturnParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedRules18: BinaryAssociation = BinaryAssociation(
    name="implementedRules18",
    ends={
        Property(name="mitra_SimpleRuleReference", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration19", type=mitra_SimpleRuleReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overriddenRule20: BinaryAssociation = BinaryAssociation(
    name="overriddenRule20",
    ends={
        Property(name="mitra_SimpleRuleReference22", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration21", type=mitra_SimpleRuleReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterReferences39: BinaryAssociation = BinaryAssociation(
    name="parameterReferences39",
    ends={
        Property(name="mitra_QualifiedParameterReference", type=mitra_QualifiedRuleReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_QualifiedRuleReference", type=mitra_QualifiedParameterReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
excludingRules23: BinaryAssociation = BinaryAssociation(
    name="excludingRules23",
    ends={
        Property(name="mitra_SimpleRuleReference25", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration24", type=mitra_SimpleRuleReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger26: BinaryAssociation = BinaryAssociation(
    name="trigger26",
    ends={
        Property(name="mitra_Trigger", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration27", type=mitra_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javaSpec28: BinaryAssociation = BinaryAssociation(
    name="javaSpec28",
    ends={
        Property(name="mitra_JavaSpec", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration29", type=mitra_JavaSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body30: BinaryAssociation = BinaryAssociation(
    name="body30",
    ends={
        Property(name="mitra_Block", type=mitra_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleDeclaration31", type=mitra_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ruleDeclaration32: BinaryAssociation = BinaryAssociation(
    name="ruleDeclaration32",
    ends={
        Property(name="mitra_RuleDeclaration33", type=mitra_RuleReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleReference", type=mitra_RuleDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
parameterReferences34: BinaryAssociation = BinaryAssociation(
    name="parameterReferences34",
    ends={
        Property(name="mitra_SimpleParameterReference", type=mitra_SimpleRuleReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_SimpleRuleReference35", type=mitra_SimpleParameterReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnReferences36: BinaryAssociation = BinaryAssociation(
    name="returnReferences36",
    ends={
        Property(name="mitra_SimpleParameterReference38", type=mitra_SimpleRuleReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_SimpleRuleReference37", type=mitra_SimpleParameterReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties55: BinaryAssociation = BinaryAssociation(
    name="properties55",
    ends={
        Property(name="mitra_Property57", type=mitra_JavaSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_JavaSpec56", type=mitra_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnReferences40: BinaryAssociation = BinaryAssociation(
    name="returnReferences40",
    ends={
        Property(name="mitra_QualifiedParameterReference42", type=mitra_QualifiedRuleReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_QualifiedRuleReference41", type=mitra_QualifiedParameterReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations58: BinaryAssociation = BinaryAssociation(
    name="annotations58",
    ends={
        Property(name="mitra_Annotation59", type=mitra_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Parameter", type=mitra_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="mitra_Type", type=mitra_SimpleParameterReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_SimpleParameterReference44", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vardecl60: BinaryAssociation = BinaryAssociation(
    name="vardecl60",
    ends={
        Property(name="mitra_TypedVarDeclaration62", type=mitra_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Parameter61", type=mitra_TypedVarDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vardecl45: BinaryAssociation = BinaryAssociation(
    name="vardecl45",
    ends={
        Property(name="mitra_TypedVarDeclaration", type=mitra_QualifiedParameterReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_QualifiedParameterReference46", type=mitra_TypedVarDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggerRules47: BinaryAssociation = BinaryAssociation(
    name="triggerRules47",
    ends={
        Property(name="mitra_QualifiedRuleReference49", type=mitra_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Trigger48", type=mitra_QualifiedRuleReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
with50: BinaryAssociation = BinaryAssociation(
    name="with50",
    ends={
        Property(name="mitra_Block52", type=mitra_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Trigger51", type=mitra_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when53: BinaryAssociation = BinaryAssociation(
    name="when53",
    ends={
        Property(name="mitra_Expression", type=mitra_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Trigger54", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metamodelDeclaration63: BinaryAssociation = BinaryAssociation(
    name="metamodelDeclaration63",
    ends={
        Property(name="mitra_MetamodelDeclaration64", type=mitra_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ReferenceType", type=mitra_MetamodelDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier65: BinaryAssociation = BinaryAssociation(
    name="eClassifier65",
    ends={
        Property(name="mitra_EClassifier", type=mitra_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ReferenceType66", type=mitra_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
typePar67: BinaryAssociation = BinaryAssociation(
    name="typePar67",
    ends={
        Property(name="mitra_Type68", type=mitra_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_CollectionType", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements69: BinaryAssociation = BinaryAssociation(
    name="statements69",
    ends={
        Property(name="mitra_BlockStatement", type=mitra_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Block70", type=mitra_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariableDeclaration71: BinaryAssociation = BinaryAssociation(
    name="localVariableDeclaration71",
    ends={
        Property(name="mitra_LocalVariableDeclaration", type=mitra_LocalVariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_LocalVariableDeclarationStatement", type=mitra_LocalVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementExpression80: BinaryAssociation = BinaryAssociation(
    name="statementExpression80",
    ends={
        Property(name="mitra_StatementExpression", type=mitra_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ExpressionStatement", type=mitra_StatementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression81: BinaryAssociation = BinaryAssociation(
    name="expression81",
    ends={
        Property(name="mitra_Expression82", type=mitra_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ReturnStatement", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression83: BinaryAssociation = BinaryAssociation(
    name="expression83",
    ends={
        Property(name="mitra_Expression84", type=mitra_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_IfStatement", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueStatement85: BinaryAssociation = BinaryAssociation(
    name="trueStatement85",
    ends={
        Property(name="mitra_Statement", type=mitra_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_IfStatement86", type=mitra_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vardecl72: BinaryAssociation = BinaryAssociation(
    name="vardecl72",
    ends={
        Property(name="mitra_TypedVarDeclaration74", type=mitra_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_LocalVariableDeclaration73", type=mitra_TypedVarDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement87: BinaryAssociation = BinaryAssociation(
    name="elseStatement87",
    ends={
        Property(name="mitra_Statement89", type=mitra_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_IfStatement88", type=mitra_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression75: BinaryAssociation = BinaryAssociation(
    name="expression75",
    ends={
        Property(name="mitra_Expression77", type=mitra_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_LocalVariableDeclaration76", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type78: BinaryAssociation = BinaryAssociation(
    name="type78",
    ends={
        Property(name="mitra_Type79", type=mitra_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_VarDeclaration", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression90: BinaryAssociation = BinaryAssociation(
    name="expression90",
    ends={
        Property(name="mitra_Expression91", type=mitra_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_WhileStatement", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement92: BinaryAssociation = BinaryAssociation(
    name="statement92",
    ends={
        Property(name="mitra_Statement94", type=mitra_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_WhileStatement93", type=mitra_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement95: BinaryAssociation = BinaryAssociation(
    name="statement95",
    ends={
        Property(name="mitra_Statement96", type=mitra_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_DoStatement", type=mitra_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression97: BinaryAssociation = BinaryAssociation(
    name="expression97",
    ends={
        Property(name="mitra_Expression99", type=mitra_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_DoStatement98", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementExpressions100: BinaryAssociation = BinaryAssociation(
    name="statementExpressions100",
    ends={
        Property(name="mitra_StatementExpression101", type=mitra_ForInit, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForInit", type=mitra_StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varDeclarations102: BinaryAssociation = BinaryAssociation(
    name="varDeclarations102",
    ends={
        Property(name="mitra_LocalVariableDeclaration104", type=mitra_ForInit, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForInit103", type=mitra_LocalVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementExpression105: BinaryAssociation = BinaryAssociation(
    name="statementExpression105",
    ends={
        Property(name="mitra_StatementExpression106", type=mitra_ForUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForUpdate", type=mitra_StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forUpdate114: BinaryAssociation = BinaryAssociation(
    name="forUpdate114",
    ends={
        Property(name="mitra_ForUpdate116", type=mitra_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForStatement115", type=mitra_ForUpdate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement117: BinaryAssociation = BinaryAssociation(
    name="statement117",
    ends={
        Property(name="mitra_Statement119", type=mitra_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForStatement118", type=mitra_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vardecl120: BinaryAssociation = BinaryAssociation(
    name="vardecl120",
    ends={
        Property(name="mitra_VarDeclaration122", type=mitra_LoopVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_LoopVariable121", type=mitra_VarDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression123: BinaryAssociation = BinaryAssociation(
    name="expression123",
    ends={
        Property(name="mitra_Expression124", type=mitra_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ThrowStatement", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBlock125: BinaryAssociation = BinaryAssociation(
    name="tryBlock125",
    ends={
        Property(name="mitra_Block126", type=mitra_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_TryStatement", type=mitra_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catches127: BinaryAssociation = BinaryAssociation(
    name="catches127",
    ends={
        Property(name="mitra_Catch", type=mitra_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_TryStatement128", type=mitra_Catch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable107: BinaryAssociation = BinaryAssociation(
    name="loopVariable107",
    ends={
        Property(name="mitra_LoopVariable", type=mitra_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForStatement", type=mitra_LoopVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression108: BinaryAssociation = BinaryAssociation(
    name="expression108",
    ends={
        Property(name="mitra_Expression110", type=mitra_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForStatement109", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forInit111: BinaryAssociation = BinaryAssociation(
    name="forInit111",
    ends={
        Property(name="mitra_ForInit113", type=mitra_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ForStatement112", type=mitra_ForInit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block135: BinaryAssociation = BinaryAssociation(
    name="block135",
    ends={
        Property(name="mitra_Block137", type=mitra_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Catch136", type=mitra_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyBlock129: BinaryAssociation = BinaryAssociation(
    name="finallyBlock129",
    ends={
        Property(name="mitra_Block131", type=mitra_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_TryStatement130", type=mitra_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameter132: BinaryAssociation = BinaryAssociation(
    name="formalParameter132",
    ends={
        Property(name="mitra_FormalParameter134", type=mitra_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Catch133", type=mitra_FormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ruleDeclaration143: BinaryAssociation = BinaryAssociation(
    name="ruleDeclaration143",
    ends={
        Property(name="mitra_RuleDeclaration144", type=mitra_RuleInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleInvocation", type=mitra_RuleDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
arguments145: BinaryAssociation = BinaryAssociation(
    name="arguments145",
    ends={
        Property(name="mitra_Expression147", type=mitra_RuleInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RuleInvocation146", type=mitra_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments148: BinaryAssociation = BinaryAssociation(
    name="arguments148",
    ends={
        Property(name="mitra_Expression149", type=mitra_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_MethodInvocation", type=mitra_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type138: BinaryAssociation = BinaryAssociation(
    name="type138",
    ends={
        Property(name="mitra_Type139", type=mitra_ClassInstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ClassInstanceCreationExpression", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments140: BinaryAssociation = BinaryAssociation(
    name="arguments140",
    ends={
        Property(name="mitra_Expression142", type=mitra_ClassInstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_ClassInstanceCreationExpression141", type=mitra_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="mitra_Expression153", type=mitra_FeatureField, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_FeatureField", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable154: BinaryAssociation = BinaryAssociation(
    name="variable154",
    ends={
        Property(name="mitra_VarDeclaration155", type=mitra_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_VariableAccess", type=mitra_VarDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
features156: BinaryAssociation = BinaryAssociation(
    name="features156",
    ends={
        Property(name="mitra_Feature", type=mitra_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_VariableAccess157", type=mitra_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default158: BinaryAssociation = BinaryAssociation(
    name="default158",
    ends={
        Property(name="mitra_Expression160", type=mitra_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_VariableAccess159", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression150: BinaryAssociation = BinaryAssociation(
    name="expression150",
    ends={
        Property(name="mitra_Expression151", type=mitra_FeatureMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_FeatureMethodInvocation", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type163: BinaryAssociation = BinaryAssociation(
    name="type163",
    ends={
        Property(name="mitra_Type165", type=mitra_StaticAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_StaticAccess164", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features166: BinaryAssociation = BinaryAssociation(
    name="features166",
    ends={
        Property(name="mitra_Feature168", type=mitra_StaticAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_StaticAccess167", type=mitra_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationDecls169: BinaryAssociation = BinaryAssociation(
    name="annotationDecls169",
    ends={
        Property(name="mitra_AnnotationDecl", type=mitra_AnnotationsDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationsDefinition170", type=mitra_AnnotationDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valuetype171: BinaryAssociation = BinaryAssociation(
    name="valuetype171",
    ends={
        Property(name="mitra_PrimitiveType", type=mitra_AnnotationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationDecl172", type=mitra_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="mitra_Expression162", type=mitra_StaticAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_StaticAccess", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyDecls175: BinaryAssociation = BinaryAssociation(
    name="propertyDecls175",
    ends={
        Property(name="mitra_AnnotationPropertyDecl", type=mitra_AnnotationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationDecl176", type=mitra_AnnotationPropertyDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default173: BinaryAssociation = BinaryAssociation(
    name="default173",
    ends={
        Property(name="mitra_Literal", type=mitra_AnnotationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationDecl174", type=mitra_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type177: BinaryAssociation = BinaryAssociation(
    name="type177",
    ends={
        Property(name="mitra_PrimitiveType179", type=mitra_AnnotationPropertyDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationPropertyDecl178", type=mitra_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default180: BinaryAssociation = BinaryAssociation(
    name="default180",
    ends={
        Property(name="mitra_Literal182", type=mitra_AnnotationPropertyDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationPropertyDecl181", type=mitra_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decl183: BinaryAssociation = BinaryAssociation(
    name="decl183",
    ends={
        Property(name="mitra_AnnotationDecl185", type=mitra_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Annotation184", type=mitra_AnnotationDecl, multiplicity=Multiplicity(0, 1))
    }
)
values186: BinaryAssociation = BinaryAssociation(
    name="values186",
    ends={
        Property(name="mitra_Literal188", type=mitra_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Annotation187", type=mitra_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties189: BinaryAssociation = BinaryAssociation(
    name="properties189",
    ends={
        Property(name="mitra_AnnotationProperty", type=mitra_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Annotation190", type=mitra_AnnotationProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decl191: BinaryAssociation = BinaryAssociation(
    name="decl191",
    ends={
        Property(name="mitra_AnnotationPropertyDecl193", type=mitra_AnnotationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationProperty192", type=mitra_AnnotationPropertyDecl, multiplicity=Multiplicity(0, 1))
    }
)
value194: BinaryAssociation = BinaryAssociation(
    name="value194",
    ends={
        Property(name="mitra_Literal196", type=mitra_AnnotationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_AnnotationProperty195", type=mitra_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable202: BinaryAssociation = BinaryAssociation(
    name="variable202",
    ends={
        Property(name="mitra_LoopVariable203", type=mitra_IteratorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_IteratorExpression", type=mitra_LoopVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression204: BinaryAssociation = BinaryAssociation(
    name="expression204",
    ends={
        Property(name="mitra_Expression206", type=mitra_IteratorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_IteratorExpression205", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs207: BinaryAssociation = BinaryAssociation(
    name="lhs207",
    ends={
        Property(name="mitra_Expression208", type=mitra_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_BooleanExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs209: BinaryAssociation = BinaryAssociation(
    name="rhs209",
    ends={
        Property(name="mitra_Expression211", type=mitra_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_BooleanExpression210", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs212: BinaryAssociation = BinaryAssociation(
    name="lhs212",
    ends={
        Property(name="mitra_Expression213", type=mitra_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_EqualityExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs197: BinaryAssociation = BinaryAssociation(
    name="lhs197",
    ends={
        Property(name="mitra_VariableAccess198", type=mitra_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Assignment", type=mitra_VariableAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs217: BinaryAssociation = BinaryAssociation(
    name="lhs217",
    ends={
        Property(name="mitra_Expression218", type=mitra_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RelationalExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression199: BinaryAssociation = BinaryAssociation(
    name="expression199",
    ends={
        Property(name="mitra_Expression201", type=mitra_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_Assignment200", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs219: BinaryAssociation = BinaryAssociation(
    name="rhs219",
    ends={
        Property(name="mitra_Expression221", type=mitra_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_RelationalExpression220", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs222: BinaryAssociation = BinaryAssociation(
    name="lhs222",
    ends={
        Property(name="mitra_Expression223", type=mitra_MathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_MathExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs224: BinaryAssociation = BinaryAssociation(
    name="rhs224",
    ends={
        Property(name="mitra_Expression226", type=mitra_MathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_MathExpression225", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type227: BinaryAssociation = BinaryAssociation(
    name="type227",
    ends={
        Property(name="mitra_Type228", type=mitra_UnaryCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_UnaryCastExpression", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression229: BinaryAssociation = BinaryAssociation(
    name="expression229",
    ends={
        Property(name="mitra_Expression231", type=mitra_UnaryCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_UnaryCastExpression230", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs214: BinaryAssociation = BinaryAssociation(
    name="rhs214",
    ends={
        Property(name="mitra_Expression216", type=mitra_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_EqualityExpression215", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression234: BinaryAssociation = BinaryAssociation(
    name="expression234",
    ends={
        Property(name="mitra_Expression235", type=mitra_UnaryMathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_UnaryMathExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression236: BinaryAssociation = BinaryAssociation(
    name="expression236",
    ends={
        Property(name="mitra_Expression237", type=mitra_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_InstanceOfExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type238: BinaryAssociation = BinaryAssociation(
    name="type238",
    ends={
        Property(name="mitra_Type240", type=mitra_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_InstanceOfExpression239", type=mitra_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="mitra_Expression233", type=mitra_UnaryBooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mitra_UnaryBooleanExpression", type=mitra_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mitra_SimpleRuleReference_RuleReference = Generalization(general=RuleReference, specific=mitra_SimpleRuleReference)
gen_mitra_QualifiedRuleReference_RuleReference = Generalization(general=RuleReference, specific=mitra_QualifiedRuleReference)
gen_mitra_SimpleParameterReference_ParameterReference = Generalization(general=ParameterReference, specific=mitra_SimpleParameterReference)
gen_mitra_QualifiedParameterReference_ParameterReference = Generalization(general=ParameterReference, specific=mitra_QualifiedParameterReference)
gen_mitra_FormalParameter_Parameter = Generalization(general=Parameter_, specific=mitra_FormalParameter)
gen_mitra_ReferenceType_Type = Generalization(general=Type, specific=mitra_ReferenceType)
gen_mitra_PrimitiveType_Type = Generalization(general=Type, specific=mitra_PrimitiveType)
gen_mitra_ReturnParameter_Parameter = Generalization(general=Parameter_, specific=mitra_ReturnParameter)
gen_mitra_Block_Statement = Generalization(general=Statement, specific=mitra_Block)
gen_mitra_Statement_BlockStatement = Generalization(general=BlockStatement, specific=mitra_Statement)
gen_mitra_LocalVariableDeclarationStatement_BlockStatement = Generalization(general=BlockStatement, specific=mitra_LocalVariableDeclarationStatement)
gen_mitra_CollectionType_Type = Generalization(general=Type, specific=mitra_CollectionType)
gen_mitra_TypedVarDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=mitra_TypedVarDeclaration)
gen_mitra_InferredVarDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=mitra_InferredVarDeclaration)
gen_mitra_ExpressionStatement_Statement = Generalization(general=Statement, specific=mitra_ExpressionStatement)
gen_mitra_EmptyStatement_Statement = Generalization(general=Statement, specific=mitra_EmptyStatement)
gen_mitra_ReturnStatement_Statement = Generalization(general=Statement, specific=mitra_ReturnStatement)
gen_mitra_IfStatement_Statement = Generalization(general=Statement, specific=mitra_IfStatement)
gen_mitra_DoStatement_Statement = Generalization(general=Statement, specific=mitra_DoStatement)
gen_mitra_ForStatement_Statement = Generalization(general=Statement, specific=mitra_ForStatement)
gen_mitra_WhileStatement_Statement = Generalization(general=Statement, specific=mitra_WhileStatement)
gen_mitra_BreakStatement_Statement = Generalization(general=Statement, specific=mitra_BreakStatement)
gen_mitra_ThrowStatement_Statement = Generalization(general=Statement, specific=mitra_ThrowStatement)
gen_mitra_TryStatement_Statement = Generalization(general=Statement, specific=mitra_TryStatement)
gen_mitra_IntLiteral_Literal = Generalization(general=Literal, specific=mitra_IntLiteral)
gen_mitra_RealLiteral_Literal = Generalization(general=Literal, specific=mitra_RealLiteral)
gen_mitra_BooleanLiteral_Literal = Generalization(general=Literal, specific=mitra_BooleanLiteral)
gen_mitra_NullLiteral_Literal = Generalization(general=Literal, specific=mitra_NullLiteral)
gen_mitra_ClassInstanceCreationExpression_StatementExpression = Generalization(general=StatementExpression, specific=mitra_ClassInstanceCreationExpression)
gen_mitra_ClassInstanceCreationExpression_TerminalExpression = Generalization(general=TerminalExpression, specific=mitra_ClassInstanceCreationExpression)
gen_mitra_TerminalExpression_Expression = Generalization(general=Expression, specific=mitra_TerminalExpression)
gen_mitra_Literal_TerminalExpression = Generalization(general=TerminalExpression, specific=mitra_Literal)
gen_mitra_StringLiteral_Literal = Generalization(general=Literal, specific=mitra_StringLiteral)
gen_mitra_RuleInvocation_StatementExpression = Generalization(general=StatementExpression, specific=mitra_RuleInvocation)
gen_mitra_RuleInvocation_TerminalExpression = Generalization(general=TerminalExpression, specific=mitra_RuleInvocation)
gen_mitra_RuleInvocationSuper_StatementExpression = Generalization(general=StatementExpression, specific=mitra_RuleInvocationSuper)
gen_mitra_RuleInvocationSuper_TerminalExpression = Generalization(general=TerminalExpression, specific=mitra_RuleInvocationSuper)
gen_mitra_MethodInvocation_Feature = Generalization(general=Feature, specific=mitra_MethodInvocation)
gen_mitra_NativeOperationInvocation_MethodInvocation = Generalization(general=MethodInvocation, specific=mitra_NativeOperationInvocation)
gen_mitra_FeatureField_Feature = Generalization(general=Feature, specific=mitra_FeatureField)
gen_mitra_FeatureField_MetamodelFeature = Generalization(general=MetamodelFeature, specific=mitra_FeatureField)
gen_mitra_VariableAccess_StatementExpression = Generalization(general=StatementExpression, specific=mitra_VariableAccess)
gen_mitra_VariableAccess_TerminalExpression = Generalization(general=TerminalExpression, specific=mitra_VariableAccess)
gen_mitra_FeatureMethodInvocation_MethodInvocation = Generalization(general=MethodInvocation, specific=mitra_FeatureMethodInvocation)
gen_mitra_FeatureMethodInvocation_MetamodelFeature = Generalization(general=MetamodelFeature, specific=mitra_FeatureMethodInvocation)
gen_mitra_StaticAccess_StatementExpression = Generalization(general=StatementExpression, specific=mitra_StaticAccess)
gen_mitra_StaticAccess_TerminalExpression = Generalization(general=TerminalExpression, specific=mitra_StaticAccess)
gen_mitra_Assignment_StatementExpression = Generalization(general=StatementExpression, specific=mitra_Assignment)
gen_mitra_IteratorExpression_Expression = Generalization(general=Expression, specific=mitra_IteratorExpression)
gen_mitra_BooleanExpression_Expression = Generalization(general=Expression, specific=mitra_BooleanExpression)
gen_mitra_EqualityExpression_Expression = Generalization(general=Expression, specific=mitra_EqualityExpression)
gen_mitra_MathExpression_Expression = Generalization(general=Expression, specific=mitra_MathExpression)
gen_mitra_UnaryCastExpression_Expression = Generalization(general=Expression, specific=mitra_UnaryCastExpression)
gen_mitra_RelationalExpression_Expression = Generalization(general=Expression, specific=mitra_RelationalExpression)
gen_mitra_InstanceOfExpression_Expression = Generalization(general=Expression, specific=mitra_InstanceOfExpression)
gen_mitra_UnaryBooleanExpression_Expression = Generalization(general=Expression, specific=mitra_UnaryBooleanExpression)
gen_mitra_UnaryMathExpression_Expression = Generalization(general=Expression, specific=mitra_UnaryMathExpression)

# Domain Model
domain_model = DomainModel(
    name="mitra",
    types={mitra_ModuleReference, mitra_Module, mitra_MetamodelDeclaration, mitra_AnnotationsDefinition, mitra_RuleDeclaration, mitra_Property, mitra_Annotation, mitra_FormalParameter, mitra_ReturnParameter, mitra_SimpleRuleReference, mitra_QualifiedParameterReference, mitra_Trigger, mitra_JavaSpec, mitra_Block, mitra_RuleReference, RuleReference, mitra_SimpleParameterReference, mitra_QualifiedRuleReference, mitra_ParameterReference, ParameterReference, mitra_Parameter, mitra_Type, Parameter_, mitra_TypedVarDeclaration, mitra_Expression, mitra_ReferenceType, Type, mitra_EClassifier, mitra_PrimitiveType, Statement, mitra_BlockStatement, mitra_Statement, BlockStatement, mitra_LocalVariableDeclarationStatement, mitra_LocalVariableDeclaration, mitra_CollectionType, VarDeclaration, mitra_InferredVarDeclaration, mitra_ExpressionStatement, mitra_StatementExpression, mitra_EmptyStatement, mitra_ReturnStatement, mitra_IfStatement, mitra_VarDeclaration, mitra_DoStatement, mitra_ForInit, mitra_ForUpdate, mitra_ForStatement, mitra_WhileStatement, mitra_BreakStatement, mitra_ThrowStatement, mitra_TryStatement, mitra_Catch, mitra_LoopVariable, mitra_TerminalExpression, mitra_IntLiteral, mitra_RealLiteral, mitra_BooleanLiteral, mitra_NullLiteral, mitra_ClassInstanceCreationExpression, StatementExpression, Expression, mitra_Literal, TerminalExpression, mitra_StringLiteral, Literal, mitra_RuleInvocationSuper, mitra_Feature, mitra_MethodInvocation, Feature, mitra_RuleInvocation, mitra_NativeOperationInvocation, mitra_MetamodelFeature, mitra_FeatureField, mitra_VariableAccess, mitra_FeatureMethodInvocation, MethodInvocation, MetamodelFeature, mitra_AnnotationDecl, mitra_StaticAccess, mitra_AnnotationPropertyDecl, mitra_AnnotationProperty, mitra_Assignment, mitra_IteratorExpression, mitra_BooleanExpression, mitra_EqualityExpression, mitra_MathExpression, mitra_UnaryCastExpression, mitra_RelationalExpression, mitra_InstanceOfExpression, mitra_UnaryBooleanExpression, mitra_UnaryMathExpression, VisibilityModifier, ExecutionModifier, PrimitiveTypeSpec, ParameterModifier, CollectionTypeSpec, BooleanOperator, EqualityOperator, RelationalOperator, MathOperator, UnaryMathOperator, AssignmentOperator, PPOperator, AnnotationTargetSpec},
    associations={imports0, metamodelDeclarations1, annotationDefinitions3, ruleDeclarations5, module7, properties10, annotations12, formalParameters14, returnParameters16, implementedRules18, overriddenRule20, parameterReferences39, excludingRules23, trigger26, javaSpec28, body30, ruleDeclaration32, parameterReferences34, returnReferences36, properties55, returnReferences40, annotations58, type43, vardecl60, vardecl45, triggerRules47, with50, when53, metamodelDeclaration63, eClassifier65, typePar67, statements69, localVariableDeclaration71, statementExpression80, expression81, expression83, trueStatement85, vardecl72, elseStatement87, expression75, type78, expression90, statement92, statement95, expression97, statementExpressions100, varDeclarations102, statementExpression105, forUpdate114, statement117, vardecl120, expression123, tryBlock125, catches127, loopVariable107, expression108, forInit111, block135, finallyBlock129, formalParameter132, ruleDeclaration143, arguments145, arguments148, type138, arguments140, expression152, variable154, features156, default158, expression150, type163, features166, annotationDecls169, valuetype171, expression161, propertyDecls175, default173, type177, default180, decl183, values186, properties189, decl191, value194, variable202, expression204, lhs207, rhs209, lhs212, lhs197, lhs217, expression199, rhs219, lhs222, rhs224, type227, expression229, rhs214, expression234, expression236, type238, expression232},
    generalizations={gen_mitra_SimpleRuleReference_RuleReference, gen_mitra_QualifiedRuleReference_RuleReference, gen_mitra_SimpleParameterReference_ParameterReference, gen_mitra_QualifiedParameterReference_ParameterReference, gen_mitra_FormalParameter_Parameter, gen_mitra_ReferenceType_Type, gen_mitra_PrimitiveType_Type, gen_mitra_ReturnParameter_Parameter, gen_mitra_Block_Statement, gen_mitra_Statement_BlockStatement, gen_mitra_LocalVariableDeclarationStatement_BlockStatement, gen_mitra_CollectionType_Type, gen_mitra_TypedVarDeclaration_VarDeclaration, gen_mitra_InferredVarDeclaration_VarDeclaration, gen_mitra_ExpressionStatement_Statement, gen_mitra_EmptyStatement_Statement, gen_mitra_ReturnStatement_Statement, gen_mitra_IfStatement_Statement, gen_mitra_DoStatement_Statement, gen_mitra_ForStatement_Statement, gen_mitra_WhileStatement_Statement, gen_mitra_BreakStatement_Statement, gen_mitra_ThrowStatement_Statement, gen_mitra_TryStatement_Statement, gen_mitra_IntLiteral_Literal, gen_mitra_RealLiteral_Literal, gen_mitra_BooleanLiteral_Literal, gen_mitra_NullLiteral_Literal, gen_mitra_ClassInstanceCreationExpression_StatementExpression, gen_mitra_ClassInstanceCreationExpression_TerminalExpression, gen_mitra_TerminalExpression_Expression, gen_mitra_Literal_TerminalExpression, gen_mitra_StringLiteral_Literal, gen_mitra_RuleInvocation_StatementExpression, gen_mitra_RuleInvocation_TerminalExpression, gen_mitra_RuleInvocationSuper_StatementExpression, gen_mitra_RuleInvocationSuper_TerminalExpression, gen_mitra_MethodInvocation_Feature, gen_mitra_NativeOperationInvocation_MethodInvocation, gen_mitra_FeatureField_Feature, gen_mitra_FeatureField_MetamodelFeature, gen_mitra_VariableAccess_StatementExpression, gen_mitra_VariableAccess_TerminalExpression, gen_mitra_FeatureMethodInvocation_MethodInvocation, gen_mitra_FeatureMethodInvocation_MetamodelFeature, gen_mitra_StaticAccess_StatementExpression, gen_mitra_StaticAccess_TerminalExpression, gen_mitra_Assignment_StatementExpression, gen_mitra_IteratorExpression_Expression, gen_mitra_BooleanExpression_Expression, gen_mitra_EqualityExpression_Expression, gen_mitra_MathExpression_Expression, gen_mitra_UnaryCastExpression_Expression, gen_mitra_RelationalExpression_Expression, gen_mitra_InstanceOfExpression_Expression, gen_mitra_UnaryBooleanExpression_Expression, gen_mitra_UnaryMathExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)