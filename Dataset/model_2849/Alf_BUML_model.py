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
ImportVisibilityIndicator: Enumeration = Enumeration(
    name="ImportVisibilityIndicator",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE")
    }
)

ParameterDirection: Enumeration = Enumeration(
    name="ParameterDirection",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

LinkOperation: Enumeration = Enumeration(
    name="LinkOperation",
    literals={
            EnumerationLiteral(name="CREATE_LINK"),
			EnumerationLiteral(name="DESTROY_LINK"),
			EnumerationLiteral(name="CLEAR_ASSOC")
    }
)

AffixOperator: Enumeration = Enumeration(
    name="AffixOperator",
    literals={
            EnumerationLiteral(name="INCR"),
			EnumerationLiteral(name="DECR")
    }
)

NumericUnaryOperator: Enumeration = Enumeration(
    name="NumericUnaryOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS")
    }
)

AdditiveOperator: Enumeration = Enumeration(
    name="AdditiveOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS")
    }
)

MultiplicativeOperator: Enumeration = Enumeration(
    name="MultiplicativeOperator",
    literals={
            EnumerationLiteral(name="REM"),
			EnumerationLiteral(name="STAR"),
			EnumerationLiteral(name="SLASH")
    }
)

ShiftOperator: Enumeration = Enumeration(
    name="ShiftOperator",
    literals={
            EnumerationLiteral(name="LSHIFT"),
			EnumerationLiteral(name="RSHIFT"),
			EnumerationLiteral(name="URSHIFT")
    }
)

ClassificationOperator: Enumeration = Enumeration(
    name="ClassificationOperator",
    literals={
            EnumerationLiteral(name="INSTANCEOF"),
			EnumerationLiteral(name="HASTYPE")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="GE")
    }
)

EqualityOperator: Enumeration = Enumeration(
    name="EqualityOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NE")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="MINUSASSIGN"),
			EnumerationLiteral(name="STARASSIGN"),
			EnumerationLiteral(name="SLASHASSIGN"),
			EnumerationLiteral(name="REMASSIGN"),
			EnumerationLiteral(name="ANSASSIGN"),
			EnumerationLiteral(name="ORASSIGN"),
			EnumerationLiteral(name="XORASSIGN"),
			EnumerationLiteral(name="LSHIFTASSIGN"),
			EnumerationLiteral(name="RSHIFTASSIGN"),
			EnumerationLiteral(name="URSHIFTASSIGN"),
			EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="PLUSASSIGN")
    }
)

# Classes
alf_StereotypeAnnotations = Class(name="alf::StereotypeAnnotations")
alf_NamespaceDefinition = Class(name="alf::NamespaceDefinition")
alf_BOOLEAN_LITERAL = Class(name="alf::BOOLEAN::LITERAL")
PRIMITIVE_LITERAL = Class(name="PRIMITIVE::LITERAL")
alf_NUMBER_LITERAL = Class(name="alf::NUMBER::LITERAL")
alf_INTEGER_LITERAL = Class(name="alf::INTEGER::LITERAL")
NUMBER_LITERAL = Class(name="NUMBER::LITERAL")
alf_UNLIMITED_NATURAL = Class(name="alf::UNLIMITED::NATURAL")
alf_STRING_LITERAL = Class(name="alf::STRING::LITERAL")
alf_StereotypeAnnotation = Class(name="alf::StereotypeAnnotation")
alf_UnitDefinition = Class(name="alf::UnitDefinition")
alf_NamespaceDeclaration = Class(name="alf::NamespaceDeclaration")
alf_ImportDeclaration = Class(name="alf::ImportDeclaration")
alf_PRIMITIVE_LITERAL = Class(name="alf::PRIMITIVE::LITERAL")
alf_Name = Class(name="alf::Name")
alf_ImportReference = Class(name="alf::ImportReference")
alf_QualifiedName = Class(name="alf::QualifiedName")
alf_TaggedValues = Class(name="alf::TaggedValues")
alf_TaggedValueList = Class(name="alf::TaggedValueList")
TaggedValues = Class(name="TaggedValues")
alf_TaggedValue = Class(name="alf::TaggedValue")
alf_ColonQualifiedNameCompletionOfImportReference = Class(name="alf::ColonQualifiedNameCompletionOfImportReference")
ImportReferenceQualifiedNameCompletion = Class(name="ImportReferenceQualifiedNameCompletion")
alf_VisibilityIndicator = Class(name="alf::VisibilityIndicator")
alf_ImportReferenceQualifiedNameCompletion = Class(name="alf::ImportReferenceQualifiedNameCompletion")
alf_AliasDefinition = Class(name="alf::AliasDefinition")
alf_PackagedElement = Class(name="alf::PackagedElement")
alf_PackageDeclaration = Class(name="alf::PackageDeclaration")
alf_PackageDefinition = Class(name="alf::PackageDefinition")
NamespaceDefinition = Class(name="NamespaceDefinition")
alf_PackageBody = Class(name="alf::PackageBody")
alf_ClassifierTemplateParameter = Class(name="alf::ClassifierTemplateParameter")
alf_PackageDefinitionOrStub = Class(name="alf::PackageDefinitionOrStub")
PackagedElementDefinition = Class(name="PackagedElementDefinition")
alf_QualifiedNameList = Class(name="alf::QualifiedNameList")
alf_PackagedElementDefinition = Class(name="alf::PackagedElementDefinition")
alf_ClassifierDefinition = Class(name="alf::ClassifierDefinition")
alf_ClassifierDefinitionOrStub = Class(name="alf::ClassifierDefinitionOrStub")
ClassMemberDefinition = Class(name="ClassMemberDefinition")
alf_ClassifierSignature = Class(name="alf::ClassifierSignature")
alf_TemplateParameters = Class(name="alf::TemplateParameters")
alf_SpecializationClause = Class(name="alf::SpecializationClause")
alf_ClassMember = Class(name="alf::ClassMember")
alf_ClassMemberDefinition = Class(name="alf::ClassMemberDefinition")
alf_ClassDeclaration = Class(name="alf::ClassDeclaration")
ActiveClassMemberDefinition = Class(name="ActiveClassMemberDefinition")
alf_ClassDefinition = Class(name="alf::ClassDefinition")
ClassifierDefinition = Class(name="ClassifierDefinition")
alf_ClassBody = Class(name="alf::ClassBody")
alf_ClassDefinitionOrStub = Class(name="alf::ClassDefinitionOrStub")
ClassifierDefinitionOrStub = Class(name="ClassifierDefinitionOrStub")
alf_ActiveClassMember = Class(name="alf::ActiveClassMember")
alf_BehaviorClause = Class(name="alf::BehaviorClause")
alf_Block = Class(name="alf::Block")
alf_ActiveClassDeclaration = Class(name="alf::ActiveClassDeclaration")
alf_ActiveClassDefinition = Class(name="alf::ActiveClassDefinition")
alf_ActiveClassBody = Class(name="alf::ActiveClassBody")
alf_ActiveClassDefinitionOrStub = Class(name="alf::ActiveClassDefinitionOrStub")
alf_DataTypeDefinition = Class(name="alf::DataTypeDefinition")
alf_StructuredBody = Class(name="alf::StructuredBody")
alf_DataTypeDefinitionOrStub = Class(name="alf::DataTypeDefinitionOrStub")
alf_ActiveClassMemberDefinition = Class(name="alf::ActiveClassMemberDefinition")
alf_DataTypeDeclaration = Class(name="alf::DataTypeDeclaration")
alf_AssociationDeclaration = Class(name="alf::AssociationDeclaration")
alf_AssociationDefinition = Class(name="alf::AssociationDefinition")
alf_AssociationDefinitionOrStub = Class(name="alf::AssociationDefinitionOrStub")
alf_StructuredMember = Class(name="alf::StructuredMember")
alf_PropertyDefinition = Class(name="alf::PropertyDefinition")
alf_EnumerationDefinitionOrStub = Class(name="alf::EnumerationDefinitionOrStub")
alf_EnumerationLiteralName = Class(name="alf::EnumerationLiteralName")
alf_SignalDeclaration = Class(name="alf::SignalDeclaration")
alf_EnumerationDeclaration = Class(name="alf::EnumerationDeclaration")
alf_EnumerationDefinition = Class(name="alf::EnumerationDefinition")
alf_EnumerationBody = Class(name="alf::EnumerationBody")
alf_ActivityDeclaration = Class(name="alf::ActivityDeclaration")
alf_FormalParameters = Class(name="alf::FormalParameters")
alf_SignalDefinition = Class(name="alf::SignalDefinition")
alf_FormalParameterList = Class(name="alf::FormalParameterList")
alf_SignalDefinitionOrStub = Class(name="alf::SignalDefinitionOrStub")
alf_FormalParameter = Class(name="alf::FormalParameter")
alf_TypePart = Class(name="alf::TypePart")
alf_ActivityDefinition = Class(name="alf::ActivityDefinition")
alf_ActivityDefinitionOrStub = Class(name="alf::ActivityDefinitionOrStub")
alf_AttributeDefinition = Class(name="alf::AttributeDefinition")
FeatureDefinitionOrStub = Class(name="FeatureDefinitionOrStub")
alf_AttributeInitializer = Class(name="alf::AttributeInitializer")
alf_InitializationExpression = Class(name="alf::InitializationExpression")
alf_FeatureDefinitionOrStub = Class(name="alf::FeatureDefinitionOrStub")
alf_ActiveFeatureDefinitionOrStub = Class(name="alf::ActiveFeatureDefinitionOrStub")
alf_PropertyDeclaration = Class(name="alf::PropertyDeclaration")
alf_UnlimitedNaturalLiteral = Class(name="alf::UnlimitedNaturalLiteral")
alf_TypeName = Class(name="alf::TypeName")
alf_Multiplicity = Class(name="alf::Multiplicity")
alf_MultiplicityRange = Class(name="alf::MultiplicityRange")
alf_OperationDefinitionOrStub = Class(name="alf::OperationDefinitionOrStub")
alf_ReceptionDefinition = Class(name="alf::ReceptionDefinition")
ActiveFeatureDefinitionOrStub = Class(name="ActiveFeatureDefinitionOrStub")
alf_SignalReceptionDeclaration = Class(name="alf::SignalReceptionDeclaration")
alf_OperationDeclaration = Class(name="alf::OperationDeclaration")
OperationDefinitionOrStub = Class(name="OperationDefinitionOrStub")
alf_RedefinitionClause = Class(name="alf::RedefinitionClause")
alf_NameBinding = Class(name="alf::NameBinding")
UnqualifiedName = Class(name="UnqualifiedName")
alf_TemplateBinding = Class(name="alf::TemplateBinding")
alf_SignalReceptionDefinitionOrStub = Class(name="alf::SignalReceptionDefinitionOrStub")
alf_UnqualifiedName = Class(name="alf::UnqualifiedName")
alf_ColonQualifiedNameCompletion = Class(name="alf::ColonQualifiedNameCompletion")
alf_NamedTemplateBinding = Class(name="alf::NamedTemplateBinding")
alf_TemplateParameterSubstitution = Class(name="alf::TemplateParameterSubstitution")
alf_Expression = Class(name="alf::Expression")
InitializationExpression = Class(name="InitializationExpression")
alf_QualifiedNameWithoutBinding = Class(name="alf::QualifiedNameWithoutBinding")
alf_ColonQualifiedNameCompletionWithoutBinding = Class(name="alf::ColonQualifiedNameCompletionWithoutBinding")
alf_PositionalTemplateBinding = Class(name="alf::PositionalTemplateBinding")
TemplateBinding = Class(name="TemplateBinding")
alf_PrimaryToExpressionCompletion = Class(name="alf::PrimaryToExpressionCompletion")
alf_PostfixExpressionCompletion = Class(name="alf::PostfixExpressionCompletion")
alf_PrimaryExpression = Class(name="alf::PrimaryExpression")
alf_UnaryExpression = Class(name="alf::UnaryExpression")
alf_ExpressionCompletion = Class(name="alf::ExpressionCompletion")
alf_NonNameExpression = Class(name="alf::NonNameExpression")
alf_NonNameUnaryExpression = Class(name="alf::NonNameUnaryExpression")
alf_NameToExpressionCompletion = Class(name="alf::NameToExpressionCompletion")
alf_NameToPrimaryExpression = Class(name="alf::NameToPrimaryExpression")
alf_SequenceConstructionExpressionCompletion = Class(name="alf::SequenceConstructionExpressionCompletion")
alf_BehaviorInvocation = Class(name="alf::BehaviorInvocation")
alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index = Class(name="alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index")
alf_Feature = Class(name="alf::Feature")
alf_NameOrPrimaryExpression = Class(name="alf::NameOrPrimaryExpression")
alf_BaseExpression = Class(name="alf::BaseExpression")
alf_ParenthesizedExpression = Class(name="alf::ParenthesizedExpression")
alf_PrimaryExpressionCompletion = Class(name="alf::PrimaryExpressionCompletion")
alf_LinkOperationCompletion = Class(name="alf::LinkOperationCompletion")
alf_ClassExtentExpressionCompletion = Class(name="alf::ClassExtentExpressionCompletion")
alf_ThisExpression = Class(name="alf::ThisExpression")
alf_Tuple = Class(name="alf::Tuple")
alf_FeatureInvocation = Class(name="alf::FeatureInvocation")
alf_SequenceOperationOrReductionOrExpansion = Class(name="alf::SequenceOperationOrReductionOrExpansion")
alf_Index = Class(name="alf::Index")
alf_LiteralExpression = Class(name="alf::LiteralExpression")
BaseExpression = Class(name="BaseExpression")
alf_NamedTupleExpressionList = Class(name="alf::NamedTupleExpressionList")
alf_PositionalTupleExpressionList = Class(name="alf::PositionalTupleExpressionList")
alf_PositionalTupleExpressionListCompletion = Class(name="alf::PositionalTupleExpressionListCompletion")
alf_NamedExpression = Class(name="alf::NamedExpression")
alf_LinkOperationTuple = Class(name="alf::LinkOperationTuple")
alf_SuperInvocationExpression = Class(name="alf::SuperInvocationExpression")
alf_IndexedNamedExpressionListCompletion = Class(name="alf::IndexedNamedExpressionListCompletion")
alf_InstanceCreationOrSequenceConstructionExpression = Class(name="alf::InstanceCreationOrSequenceConstructionExpression")
alf_IndexedNamedExpression = Class(name="alf::IndexedNamedExpression")
alf_SequenceAnyExpression = Class(name="alf::SequenceAnyExpression")
alf_SequenceElements = Class(name="alf::SequenceElements")
alf_SequenceElementListCompletion = Class(name="alf::SequenceElementListCompletion")
alf_SequenceInitializationExpression = Class(name="alf::SequenceInitializationExpression")
alf_SequenceElement = Class(name="alf::SequenceElement")
alf_MultiplicityIndicator = Class(name="alf::MultiplicityIndicator")
alf_EObject = Class(name="alf::EObject")
alf_PrefixExpression = Class(name="alf::PrefixExpression")
NonPostfixNonCastUnaryExpression = Class(name="NonPostfixNonCastUnaryExpression")
alf_PostfixOrCastExpression = Class(name="alf::PostfixOrCastExpression")
UnaryExpression = Class(name="UnaryExpression")
CastCompletion = Class(name="CastCompletion")
alf_NonNamePostfixOrCastExpression = Class(name="alf::NonNamePostfixOrCastExpression")
alf_PostfixOperation = Class(name="alf::PostfixOperation")
alf_NonPostfixNonCastUnaryExpression = Class(name="alf::NonPostfixNonCastUnaryExpression")
alf_BooleanNegationExpression = Class(name="alf::BooleanNegationExpression")
NonNameUnaryExpression = Class(name="NonNameUnaryExpression")
alf_NumericUnaryExpression = Class(name="alf::NumericUnaryExpression")
alf_CastCompletion = Class(name="alf::CastCompletion")
alf_IsolationExpression = Class(name="alf::IsolationExpression")
alf_MultiplicativeExpression = Class(name="alf::MultiplicativeExpression")
alf_MultiplicativeExpressionCompletion = Class(name="alf::MultiplicativeExpressionCompletion")
alf_BitStringComplementExpression = Class(name="alf::BitStringComplementExpression")
alf_AdditiveExpression = Class(name="alf::AdditiveExpression")
alf_AdditiveExpressionCompletion = Class(name="alf::AdditiveExpressionCompletion")
alf_ShiftExpression = Class(name="alf::ShiftExpression")
alf_RelationalExpression = Class(name="alf::RelationalExpression")
alf_RelationalExpressionCompletion = Class(name="alf::RelationalExpressionCompletion")
alf_ShiftExpressionCompletion = Class(name="alf::ShiftExpressionCompletion")
alf_ClassificationExpressionCompletion = Class(name="alf::ClassificationExpressionCompletion")
alf_EqualityExpression = Class(name="alf::EqualityExpression")
alf_EqualityExpressionCompletion = Class(name="alf::EqualityExpressionCompletion")
alf_ClassificationExpression = Class(name="alf::ClassificationExpression")
alf_AndExpression = Class(name="alf::AndExpression")
alf_AndExpressionCompletion = Class(name="alf::AndExpressionCompletion")
alf_ExclusiveOrExpression = Class(name="alf::ExclusiveOrExpression")
alf_ExclusiveOrExpressionCompletion = Class(name="alf::ExclusiveOrExpressionCompletion")
alf_InclusiveOrExpression = Class(name="alf::InclusiveOrExpression")
alf_InclusiveOrExpressionCompletion = Class(name="alf::InclusiveOrExpressionCompletion")
alf_ConditionalAndExpression = Class(name="alf::ConditionalAndExpression")
alf_ConditionalAndExpressionCompletion = Class(name="alf::ConditionalAndExpressionCompletion")
alf_ConditionalOrExpressionCompletion = Class(name="alf::ConditionalOrExpressionCompletion")
alf_ConditionalExpression = Class(name="alf::ConditionalExpression")
alf_ConditionalExpressionCompletion = Class(name="alf::ConditionalExpressionCompletion")
ExpressionCompletion = Class(name="ExpressionCompletion")
alf_ConditionalOrExpression = Class(name="alf::ConditionalOrExpression")
alf_StatementSequence = Class(name="alf::StatementSequence")
alf_DocumentedStatement = Class(name="alf::DocumentedStatement")
alf_Statement = Class(name="alf::Statement")
alf_AssignmentExpressionCompletion = Class(name="alf::AssignmentExpressionCompletion")
alf_Annotation = Class(name="alf::Annotation")
alf_NameList = Class(name="alf::NameList")
alf_InLineStatement = Class(name="alf::InLineStatement")
alf_AnnotatedStatement = Class(name="alf::AnnotatedStatement")
Statement = Class(name="Statement")
alf_Annotations = Class(name="alf::Annotations")
alf_BlockStatement = Class(name="alf::BlockStatement")
alf_EmptyStatement = Class(name="alf::EmptyStatement")
alf_LocalNameDeclarationOrExpressionStatement = Class(name="alf::LocalNameDeclarationOrExpressionStatement")
alf_LocalNameDeclarationStatementCompletion = Class(name="alf::LocalNameDeclarationStatementCompletion")
alf_LocalNameDeclarationStatement = Class(name="alf::LocalNameDeclarationStatement")
alf_InstanceInitializationExpression = Class(name="alf::InstanceInitializationExpression")
alf_IfStatement = Class(name="alf::IfStatement")
alf_SequentialClauses = Class(name="alf::SequentialClauses")
alf_FinalClause = Class(name="alf::FinalClause")
alf_ConcurrentClauses = Class(name="alf::ConcurrentClauses")
alf_NonFinalClause = Class(name="alf::NonFinalClause")
alf_SwitchStatement = Class(name="alf::SwitchStatement")
alf_SwitchClause = Class(name="alf::SwitchClause")
alf_SwitchDefaultClause = Class(name="alf::SwitchDefaultClause")
alf_SwitchCase = Class(name="alf::SwitchCase")
alf_NonEmptyStatementSequence = Class(name="alf::NonEmptyStatementSequence")
alf_WhileStatement = Class(name="alf::WhileStatement")
alf_DoStatement = Class(name="alf::DoStatement")
alf_ForStatement = Class(name="alf::ForStatement")
alf_ForControl = Class(name="alf::ForControl")
alf_BreakStatement = Class(name="alf::BreakStatement")
alf_ReturnStatement = Class(name="alf::ReturnStatement")
alf_AcceptStatement = Class(name="alf::AcceptStatement")
alf_LoopVariableDefinition = Class(name="alf::LoopVariableDefinition")
alf_CompoundAcceptStatementCompletion = Class(name="alf::CompoundAcceptStatementCompletion")
alf_AcceptBlock = Class(name="alf::AcceptBlock")
alf_AcceptClause = Class(name="alf::AcceptClause")
alf_SimpleAcceptStatementCompletion = Class(name="alf::SimpleAcceptStatementCompletion")
alf_ClassificationClause = Class(name="alf::ClassificationClause")
alf_ClassificationFromClause = Class(name="alf::ClassificationFromClause")
alf_ClassificationToClause = Class(name="alf::ClassificationToClause")
alf_ReclassifyAllClause = Class(name="alf::ReclassifyAllClause")
alf_ClassifyStatement = Class(name="alf::ClassifyStatement")

# alf_StereotypeAnnotations class attributes and methods

# alf_NamespaceDefinition class attributes and methods

# alf_BOOLEAN_LITERAL class attributes and methods

# PRIMITIVE_LITERAL class attributes and methods

# alf_NUMBER_LITERAL class attributes and methods

# alf_INTEGER_LITERAL class attributes and methods

# NUMBER_LITERAL class attributes and methods

# alf_UNLIMITED_NATURAL class attributes and methods

# alf_STRING_LITERAL class attributes and methods

# alf_StereotypeAnnotation class attributes and methods

# alf_UnitDefinition class attributes and methods
alf_UnitDefinition_comment: Property = Property(name="comment", type=StringType)
alf_UnitDefinition.attributes={alf_UnitDefinition_comment}

# alf_NamespaceDeclaration class attributes and methods

# alf_ImportDeclaration class attributes and methods
alf_ImportDeclaration_visibility: Property = Property(name="visibility", type=StringType)
alf_ImportDeclaration.attributes={alf_ImportDeclaration_visibility}

# alf_PRIMITIVE_LITERAL class attributes and methods
alf_PRIMITIVE_LITERAL_value: Property = Property(name="value", type=StringType)
alf_PRIMITIVE_LITERAL.attributes={alf_PRIMITIVE_LITERAL_value}

# alf_Name class attributes and methods
alf_Name_id: Property = Property(name="id", type=StringType)
alf_Name.attributes={alf_Name_id}

# alf_ImportReference class attributes and methods
alf_ImportReference_star: Property = Property(name="star", type=BooleanType)
alf_ImportReference.attributes={alf_ImportReference_star}

# alf_QualifiedName class attributes and methods

# alf_TaggedValues class attributes and methods

# alf_TaggedValueList class attributes and methods

# TaggedValues class attributes and methods

# alf_TaggedValue class attributes and methods

# alf_ColonQualifiedNameCompletionOfImportReference class attributes and methods
alf_ColonQualifiedNameCompletionOfImportReference_star: Property = Property(name="star", type=BooleanType)
alf_ColonQualifiedNameCompletionOfImportReference.attributes={alf_ColonQualifiedNameCompletionOfImportReference_star}

# ImportReferenceQualifiedNameCompletion class attributes and methods

# alf_VisibilityIndicator class attributes and methods
alf_VisibilityIndicator_PUBLIC: Property = Property(name="PUBLIC", type=StringType)
alf_VisibilityIndicator_PRIVATE: Property = Property(name="PRIVATE", type=StringType)
alf_VisibilityIndicator_PROTECTED: Property = Property(name="PROTECTED", type=StringType)
alf_VisibilityIndicator.attributes={alf_VisibilityIndicator_PROTECTED, alf_VisibilityIndicator_PUBLIC, alf_VisibilityIndicator_PRIVATE}

# alf_ImportReferenceQualifiedNameCompletion class attributes and methods

# alf_AliasDefinition class attributes and methods

# alf_PackagedElement class attributes and methods
alf_PackagedElement_comment: Property = Property(name="comment", type=StringType)
alf_PackagedElement_importVisibilityIndicator: Property = Property(name="importVisibilityIndicator", type=StringType)
alf_PackagedElement.attributes={alf_PackagedElement_comment, alf_PackagedElement_importVisibilityIndicator}

# alf_PackageDeclaration class attributes and methods

# alf_PackageDefinition class attributes and methods

# NamespaceDefinition class attributes and methods

# alf_PackageBody class attributes and methods

# alf_ClassifierTemplateParameter class attributes and methods
alf_ClassifierTemplateParameter_comment: Property = Property(name="comment", type=StringType)
alf_ClassifierTemplateParameter.attributes={alf_ClassifierTemplateParameter_comment}

# alf_PackageDefinitionOrStub class attributes and methods

# PackagedElementDefinition class attributes and methods

# alf_QualifiedNameList class attributes and methods

# alf_PackagedElementDefinition class attributes and methods

# alf_ClassifierDefinition class attributes and methods

# alf_ClassifierDefinitionOrStub class attributes and methods

# ClassMemberDefinition class attributes and methods

# alf_ClassifierSignature class attributes and methods

# alf_TemplateParameters class attributes and methods

# alf_SpecializationClause class attributes and methods

# alf_ClassMember class attributes and methods
alf_ClassMember_comment: Property = Property(name="comment", type=StringType)
alf_ClassMember.attributes={alf_ClassMember_comment}

# alf_ClassMemberDefinition class attributes and methods

# alf_ClassDeclaration class attributes and methods
alf_ClassDeclaration_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
alf_ClassDeclaration.attributes={alf_ClassDeclaration_isAbstract}

# ActiveClassMemberDefinition class attributes and methods

# alf_ClassDefinition class attributes and methods

# ClassifierDefinition class attributes and methods

# alf_ClassBody class attributes and methods

# alf_ClassDefinitionOrStub class attributes and methods

# ClassifierDefinitionOrStub class attributes and methods

# alf_ActiveClassMember class attributes and methods
alf_ActiveClassMember_comment: Property = Property(name="comment", type=StringType)
alf_ActiveClassMember.attributes={alf_ActiveClassMember_comment}

# alf_BehaviorClause class attributes and methods

# alf_Block class attributes and methods

# alf_ActiveClassDeclaration class attributes and methods
alf_ActiveClassDeclaration_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
alf_ActiveClassDeclaration.attributes={alf_ActiveClassDeclaration_isAbstract}

# alf_ActiveClassDefinition class attributes and methods

# alf_ActiveClassBody class attributes and methods

# alf_ActiveClassDefinitionOrStub class attributes and methods

# alf_DataTypeDefinition class attributes and methods

# alf_StructuredBody class attributes and methods

# alf_DataTypeDefinitionOrStub class attributes and methods

# alf_ActiveClassMemberDefinition class attributes and methods

# alf_DataTypeDeclaration class attributes and methods
alf_DataTypeDeclaration_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
alf_DataTypeDeclaration.attributes={alf_DataTypeDeclaration_isAbstract}

# alf_AssociationDeclaration class attributes and methods
alf_AssociationDeclaration_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
alf_AssociationDeclaration.attributes={alf_AssociationDeclaration_isAbstract}

# alf_AssociationDefinition class attributes and methods

# alf_AssociationDefinitionOrStub class attributes and methods

# alf_StructuredMember class attributes and methods
alf_StructuredMember_comment: Property = Property(name="comment", type=StringType)
alf_StructuredMember_isPublic: Property = Property(name="isPublic", type=BooleanType)
alf_StructuredMember.attributes={alf_StructuredMember_comment, alf_StructuredMember_isPublic}

# alf_PropertyDefinition class attributes and methods

# alf_EnumerationDefinitionOrStub class attributes and methods

# alf_EnumerationLiteralName class attributes and methods
alf_EnumerationLiteralName_comment: Property = Property(name="comment", type=StringType)
alf_EnumerationLiteralName.attributes={alf_EnumerationLiteralName_comment}

# alf_SignalDeclaration class attributes and methods
alf_SignalDeclaration_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
alf_SignalDeclaration.attributes={alf_SignalDeclaration_isAbstract}

# alf_EnumerationDeclaration class attributes and methods

# alf_EnumerationDefinition class attributes and methods

# alf_EnumerationBody class attributes and methods

# alf_ActivityDeclaration class attributes and methods

# alf_FormalParameters class attributes and methods

# alf_SignalDefinition class attributes and methods

# alf_FormalParameterList class attributes and methods

# alf_SignalDefinitionOrStub class attributes and methods

# alf_FormalParameter class attributes and methods
alf_FormalParameter_comment: Property = Property(name="comment", type=StringType)
alf_FormalParameter_parameterDirection: Property = Property(name="parameterDirection", type=StringType)
alf_FormalParameter.attributes={alf_FormalParameter_parameterDirection, alf_FormalParameter_comment}

# alf_TypePart class attributes and methods

# alf_ActivityDefinition class attributes and methods

# alf_ActivityDefinitionOrStub class attributes and methods

# alf_AttributeDefinition class attributes and methods

# FeatureDefinitionOrStub class attributes and methods

# alf_AttributeInitializer class attributes and methods

# alf_InitializationExpression class attributes and methods

# alf_FeatureDefinitionOrStub class attributes and methods

# alf_ActiveFeatureDefinitionOrStub class attributes and methods

# alf_PropertyDeclaration class attributes and methods
alf_PropertyDeclaration_isComposite: Property = Property(name="isComposite", type=BooleanType)
alf_PropertyDeclaration.attributes={alf_PropertyDeclaration_isComposite}

# alf_UnlimitedNaturalLiteral class attributes and methods
alf_UnlimitedNaturalLiteral_star: Property = Property(name="star", type=BooleanType)
alf_UnlimitedNaturalLiteral.attributes={alf_UnlimitedNaturalLiteral_star}

# alf_TypeName class attributes and methods
alf_TypeName_any: Property = Property(name="any", type=BooleanType)
alf_TypeName.attributes={alf_TypeName_any}

# alf_Multiplicity class attributes and methods
alf_Multiplicity_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
alf_Multiplicity_isNonUnique: Property = Property(name="isNonUnique", type=BooleanType)
alf_Multiplicity_isSequence: Property = Property(name="isSequence", type=BooleanType)
alf_Multiplicity.attributes={alf_Multiplicity_isNonUnique, alf_Multiplicity_isOrdered, alf_Multiplicity_isSequence}

# alf_MultiplicityRange class attributes and methods

# alf_OperationDefinitionOrStub class attributes and methods

# alf_ReceptionDefinition class attributes and methods

# ActiveFeatureDefinitionOrStub class attributes and methods

# alf_SignalReceptionDeclaration class attributes and methods

# alf_OperationDeclaration class attributes and methods
alf_OperationDeclaration_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
alf_OperationDeclaration.attributes={alf_OperationDeclaration_isAbstract}

# OperationDefinitionOrStub class attributes and methods

# alf_RedefinitionClause class attributes and methods

# alf_NameBinding class attributes and methods

# UnqualifiedName class attributes and methods

# alf_TemplateBinding class attributes and methods

# alf_SignalReceptionDefinitionOrStub class attributes and methods

# alf_UnqualifiedName class attributes and methods

# alf_ColonQualifiedNameCompletion class attributes and methods

# alf_NamedTemplateBinding class attributes and methods

# alf_TemplateParameterSubstitution class attributes and methods

# alf_Expression class attributes and methods

# InitializationExpression class attributes and methods

# alf_QualifiedNameWithoutBinding class attributes and methods

# alf_ColonQualifiedNameCompletionWithoutBinding class attributes and methods

# alf_PositionalTemplateBinding class attributes and methods

# TemplateBinding class attributes and methods

# alf_PrimaryToExpressionCompletion class attributes and methods

# alf_PostfixExpressionCompletion class attributes and methods

# alf_PrimaryExpression class attributes and methods

# alf_UnaryExpression class attributes and methods

# alf_ExpressionCompletion class attributes and methods

# alf_NonNameExpression class attributes and methods

# alf_NonNameUnaryExpression class attributes and methods

# alf_NameToExpressionCompletion class attributes and methods

# alf_NameToPrimaryExpression class attributes and methods

# alf_SequenceConstructionExpressionCompletion class attributes and methods

# alf_BehaviorInvocation class attributes and methods

# alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index class attributes and methods

# alf_Feature class attributes and methods

# alf_NameOrPrimaryExpression class attributes and methods

# alf_BaseExpression class attributes and methods

# alf_ParenthesizedExpression class attributes and methods

# alf_PrimaryExpressionCompletion class attributes and methods

# alf_LinkOperationCompletion class attributes and methods
alf_LinkOperationCompletion_linkOperation: Property = Property(name="linkOperation", type=StringType)
alf_LinkOperationCompletion.attributes={alf_LinkOperationCompletion_linkOperation}

# alf_ClassExtentExpressionCompletion class attributes and methods

# alf_ThisExpression class attributes and methods

# alf_Tuple class attributes and methods

# alf_FeatureInvocation class attributes and methods

# alf_SequenceOperationOrReductionOrExpansion class attributes and methods
alf_SequenceOperationOrReductionOrExpansion_isReduce: Property = Property(name="isReduce", type=BooleanType)
alf_SequenceOperationOrReductionOrExpansion_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
alf_SequenceOperationOrReductionOrExpansion_id: Property = Property(name="id", type=StringType)
alf_SequenceOperationOrReductionOrExpansion.attributes={alf_SequenceOperationOrReductionOrExpansion_isReduce, alf_SequenceOperationOrReductionOrExpansion_id, alf_SequenceOperationOrReductionOrExpansion_isOrdered}

# alf_Index class attributes and methods

# alf_LiteralExpression class attributes and methods

# BaseExpression class attributes and methods

# alf_NamedTupleExpressionList class attributes and methods

# alf_PositionalTupleExpressionList class attributes and methods

# alf_PositionalTupleExpressionListCompletion class attributes and methods

# alf_NamedExpression class attributes and methods

# alf_LinkOperationTuple class attributes and methods

# alf_SuperInvocationExpression class attributes and methods

# alf_IndexedNamedExpressionListCompletion class attributes and methods

# alf_InstanceCreationOrSequenceConstructionExpression class attributes and methods

# alf_IndexedNamedExpression class attributes and methods

# alf_SequenceAnyExpression class attributes and methods

# alf_SequenceElements class attributes and methods

# alf_SequenceElementListCompletion class attributes and methods

# alf_SequenceInitializationExpression class attributes and methods
alf_SequenceInitializationExpression_isNew: Property = Property(name="isNew", type=BooleanType)
alf_SequenceInitializationExpression.attributes={alf_SequenceInitializationExpression_isNew}

# alf_SequenceElement class attributes and methods

# alf_MultiplicityIndicator class attributes and methods

# alf_EObject class attributes and methods

# alf_PrefixExpression class attributes and methods
alf_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
alf_PrefixExpression.attributes={alf_PrefixExpression_operator}

# NonPostfixNonCastUnaryExpression class attributes and methods

# alf_PostfixOrCastExpression class attributes and methods

# UnaryExpression class attributes and methods

# CastCompletion class attributes and methods

# alf_NonNamePostfixOrCastExpression class attributes and methods
alf_NonNamePostfixOrCastExpression_any: Property = Property(name="any", type=BooleanType)
alf_NonNamePostfixOrCastExpression.attributes={alf_NonNamePostfixOrCastExpression_any}

# alf_PostfixOperation class attributes and methods
alf_PostfixOperation_operator: Property = Property(name="operator", type=StringType)
alf_PostfixOperation.attributes={alf_PostfixOperation_operator}

# alf_NonPostfixNonCastUnaryExpression class attributes and methods

# alf_BooleanNegationExpression class attributes and methods

# NonNameUnaryExpression class attributes and methods

# alf_NumericUnaryExpression class attributes and methods
alf_NumericUnaryExpression_operator: Property = Property(name="operator", type=StringType)
alf_NumericUnaryExpression.attributes={alf_NumericUnaryExpression_operator}

# alf_CastCompletion class attributes and methods

# alf_IsolationExpression class attributes and methods

# alf_MultiplicativeExpression class attributes and methods

# alf_MultiplicativeExpressionCompletion class attributes and methods
alf_MultiplicativeExpressionCompletion_operator: Property = Property(name="operator", type=StringType)
alf_MultiplicativeExpressionCompletion.attributes={alf_MultiplicativeExpressionCompletion_operator}

# alf_BitStringComplementExpression class attributes and methods

# alf_AdditiveExpression class attributes and methods

# alf_AdditiveExpressionCompletion class attributes and methods
alf_AdditiveExpressionCompletion_operator: Property = Property(name="operator", type=StringType)
alf_AdditiveExpressionCompletion.attributes={alf_AdditiveExpressionCompletion_operator}

# alf_ShiftExpression class attributes and methods

# alf_RelationalExpression class attributes and methods

# alf_RelationalExpressionCompletion class attributes and methods
alf_RelationalExpressionCompletion_relationalOperator: Property = Property(name="relationalOperator", type=StringType)
alf_RelationalExpressionCompletion.attributes={alf_RelationalExpressionCompletion_relationalOperator}

# alf_ShiftExpressionCompletion class attributes and methods
alf_ShiftExpressionCompletion_operator: Property = Property(name="operator", type=StringType)
alf_ShiftExpressionCompletion.attributes={alf_ShiftExpressionCompletion_operator}

# alf_ClassificationExpressionCompletion class attributes and methods
alf_ClassificationExpressionCompletion_operator: Property = Property(name="operator", type=StringType)
alf_ClassificationExpressionCompletion.attributes={alf_ClassificationExpressionCompletion_operator}

# alf_EqualityExpression class attributes and methods

# alf_EqualityExpressionCompletion class attributes and methods
alf_EqualityExpressionCompletion_operator: Property = Property(name="operator", type=StringType)
alf_EqualityExpressionCompletion.attributes={alf_EqualityExpressionCompletion_operator}

# alf_ClassificationExpression class attributes and methods

# alf_AndExpression class attributes and methods

# alf_AndExpressionCompletion class attributes and methods

# alf_ExclusiveOrExpression class attributes and methods

# alf_ExclusiveOrExpressionCompletion class attributes and methods

# alf_InclusiveOrExpression class attributes and methods

# alf_InclusiveOrExpressionCompletion class attributes and methods

# alf_ConditionalAndExpression class attributes and methods

# alf_ConditionalAndExpressionCompletion class attributes and methods

# alf_ConditionalOrExpressionCompletion class attributes and methods

# alf_ConditionalExpression class attributes and methods

# alf_ConditionalExpressionCompletion class attributes and methods

# ExpressionCompletion class attributes and methods

# alf_ConditionalOrExpression class attributes and methods

# alf_StatementSequence class attributes and methods

# alf_DocumentedStatement class attributes and methods
alf_DocumentedStatement_comment: Property = Property(name="comment", type=StringType)
alf_DocumentedStatement.attributes={alf_DocumentedStatement_comment}

# alf_Statement class attributes and methods

# alf_AssignmentExpressionCompletion class attributes and methods
alf_AssignmentExpressionCompletion_operator: Property = Property(name="operator", type=StringType)
alf_AssignmentExpressionCompletion.attributes={alf_AssignmentExpressionCompletion_operator}

# alf_Annotation class attributes and methods
alf_Annotation_id: Property = Property(name="id", type=StringType)
alf_Annotation.attributes={alf_Annotation_id}

# alf_NameList class attributes and methods

# alf_InLineStatement class attributes and methods
alf_InLineStatement_id: Property = Property(name="id", type=StringType)
alf_InLineStatement.attributes={alf_InLineStatement_id}

# alf_AnnotatedStatement class attributes and methods

# Statement class attributes and methods

# alf_Annotations class attributes and methods

# alf_BlockStatement class attributes and methods

# alf_EmptyStatement class attributes and methods

# alf_LocalNameDeclarationOrExpressionStatement class attributes and methods

# alf_LocalNameDeclarationStatementCompletion class attributes and methods

# alf_LocalNameDeclarationStatement class attributes and methods

# alf_InstanceInitializationExpression class attributes and methods

# alf_IfStatement class attributes and methods

# alf_SequentialClauses class attributes and methods

# alf_FinalClause class attributes and methods

# alf_ConcurrentClauses class attributes and methods

# alf_NonFinalClause class attributes and methods

# alf_SwitchStatement class attributes and methods

# alf_SwitchClause class attributes and methods

# alf_SwitchDefaultClause class attributes and methods

# alf_SwitchCase class attributes and methods

# alf_NonEmptyStatementSequence class attributes and methods

# alf_WhileStatement class attributes and methods

# alf_DoStatement class attributes and methods

# alf_ForStatement class attributes and methods

# alf_ForControl class attributes and methods

# alf_BreakStatement class attributes and methods

# alf_ReturnStatement class attributes and methods

# alf_AcceptStatement class attributes and methods

# alf_LoopVariableDefinition class attributes and methods

# alf_CompoundAcceptStatementCompletion class attributes and methods

# alf_AcceptBlock class attributes and methods

# alf_AcceptClause class attributes and methods

# alf_SimpleAcceptStatementCompletion class attributes and methods

# alf_ClassificationClause class attributes and methods

# alf_ClassificationFromClause class attributes and methods

# alf_ClassificationToClause class attributes and methods

# alf_ReclassifyAllClause class attributes and methods

# alf_ClassifyStatement class attributes and methods

# Relationships
stereotypeAnnotations3: BinaryAssociation = BinaryAssociation(
    name="stereotypeAnnotations3",
    ends={
        Property(name="alf_StereotypeAnnotations", type=alf_UnitDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnitDefinition4", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namesapceDefinition5: BinaryAssociation = BinaryAssociation(
    name="namesapceDefinition5",
    ends={
        Property(name="alf_NamespaceDefinition", type=alf_UnitDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnitDefinition6", type=alf_NamespaceDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespaceDeclaration0: BinaryAssociation = BinaryAssociation(
    name="namespaceDeclaration0",
    ends={
        Property(name="alf_NamespaceDeclaration", type=alf_UnitDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnitDefinition", type=alf_NamespaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importDeclarations1: BinaryAssociation = BinaryAssociation(
    name="importDeclarations1",
    ends={
        Property(name="alf_ImportDeclaration", type=alf_UnitDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnitDefinition2", type=alf_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taggedValue13: BinaryAssociation = BinaryAssociation(
    name="taggedValue13",
    ends={
        Property(name="alf_TaggedValue", type=alf_TaggedValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TaggedValueList", type=alf_TaggedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name14: BinaryAssociation = BinaryAssociation(
    name="name14",
    ends={
        Property(name="alf_Name", type=alf_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TaggedValue15", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="alf_PRIMITIVE_LITERAL", type=alf_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TaggedValue17", type=alf_PRIMITIVE_LITERAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName18: BinaryAssociation = BinaryAssociation(
    name="qualifiedName18",
    ends={
        Property(name="alf_QualifiedName20", type=alf_NamespaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NamespaceDeclaration19", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importReference21: BinaryAssociation = BinaryAssociation(
    name="importReference21",
    ends={
        Property(name="alf_ImportReference", type=alf_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ImportDeclaration22", type=alf_ImportReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation7: BinaryAssociation = BinaryAssociation(
    name="annotation7",
    ends={
        Property(name="alf_StereotypeAnnotation", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StereotypeAnnotations8", type=alf_StereotypeAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotypeName9: BinaryAssociation = BinaryAssociation(
    name="stereotypeName9",
    ends={
        Property(name="alf_QualifiedName", type=alf_StereotypeAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StereotypeAnnotation10", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
taggedValues11: BinaryAssociation = BinaryAssociation(
    name="taggedValues11",
    ends={
        Property(name="alf_TaggedValues", type=alf_StereotypeAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StereotypeAnnotation12", type=alf_TaggedValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name30: BinaryAssociation = BinaryAssociation(
    name="name30",
    ends={
        Property(name="alf_Name31", type=alf_ColonQualifiedNameCompletionOfImportReference, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ColonQualifiedNameCompletionOfImportReference", type=alf_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alias32: BinaryAssociation = BinaryAssociation(
    name="alias32",
    ends={
        Property(name="alf_AliasDefinition34", type=alf_ColonQualifiedNameCompletionOfImportReference, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ColonQualifiedNameCompletionOfImportReference33", type=alf_AliasDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias35: BinaryAssociation = BinaryAssociation(
    name="alias35",
    ends={
        Property(name="alf_Name37", type=alf_AliasDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AliasDefinition36", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name23: BinaryAssociation = BinaryAssociation(
    name="name23",
    ends={
        Property(name="alf_Name25", type=alf_ImportReference, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ImportReference24", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completion26: BinaryAssociation = BinaryAssociation(
    name="completion26",
    ends={
        Property(name="alf_ImportReferenceQualifiedNameCompletion", type=alf_ImportReference, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ImportReference27", type=alf_ImportReferenceQualifiedNameCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias28: BinaryAssociation = BinaryAssociation(
    name="alias28",
    ends={
        Property(name="alf_AliasDefinition", type=alf_ImportReference, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ImportReference29", type=alf_AliasDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration44: BinaryAssociation = BinaryAssociation(
    name="declaration44",
    ends={
        Property(name="alf_PackageDeclaration45", type=alf_PackageDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackageDefinitionOrStub", type=alf_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body46: BinaryAssociation = BinaryAssociation(
    name="body46",
    ends={
        Property(name="alf_PackageBody48", type=alf_PackageDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackageDefinitionOrStub47", type=alf_PackageBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packagedElement49: BinaryAssociation = BinaryAssociation(
    name="packagedElement49",
    ends={
        Property(name="alf_PackagedElement", type=alf_PackageBody, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackageBody50", type=alf_PackagedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotypeAnnotations51: BinaryAssociation = BinaryAssociation(
    name="stereotypeAnnotations51",
    ends={
        Property(name="alf_StereotypeAnnotations53", type=alf_PackagedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackagedElement52", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name38: BinaryAssociation = BinaryAssociation(
    name="name38",
    ends={
        Property(name="alf_Name39", type=alf_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackageDeclaration", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration40: BinaryAssociation = BinaryAssociation(
    name="declaration40",
    ends={
        Property(name="alf_PackageDeclaration41", type=alf_PackageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackageDefinition", type=alf_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body42: BinaryAssociation = BinaryAssociation(
    name="body42",
    ends={
        Property(name="alf_PackageBody", type=alf_PackageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackageDefinition43", type=alf_PackageBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierTemplateParameter62: BinaryAssociation = BinaryAssociation(
    name="classifierTemplateParameter62",
    ends={
        Property(name="alf_ClassifierTemplateParameter", type=alf_TemplateParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TemplateParameters63", type=alf_ClassifierTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name64: BinaryAssociation = BinaryAssociation(
    name="name64",
    ends={
        Property(name="alf_Name66", type=alf_ClassifierTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifierTemplateParameter65", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName67: BinaryAssociation = BinaryAssociation(
    name="qualifiedName67",
    ends={
        Property(name="alf_QualifiedName69", type=alf_ClassifierTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifierTemplateParameter68", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList70: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList70",
    ends={
        Property(name="alf_QualifiedNameList", type=alf_SpecializationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SpecializationClause71", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packagedElementDefinition54: BinaryAssociation = BinaryAssociation(
    name="packagedElementDefinition54",
    ends={
        Property(name="alf_PackagedElementDefinition", type=alf_PackagedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PackagedElement55", type=alf_PackagedElementDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name56: BinaryAssociation = BinaryAssociation(
    name="name56",
    ends={
        Property(name="alf_Name57", type=alf_ClassifierSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifierSignature", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateParameters58: BinaryAssociation = BinaryAssociation(
    name="templateParameters58",
    ends={
        Property(name="alf_TemplateParameters", type=alf_ClassifierSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifierSignature59", type=alf_TemplateParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specializationClause60: BinaryAssociation = BinaryAssociation(
    name="specializationClause60",
    ends={
        Property(name="alf_SpecializationClause", type=alf_ClassifierSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifierSignature61", type=alf_SpecializationClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classBody80: BinaryAssociation = BinaryAssociation(
    name="classBody80",
    ends={
        Property(name="alf_ClassBody82", type=alf_ClassDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassDefinitionOrStub81", type=alf_ClassBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classMember83: BinaryAssociation = BinaryAssociation(
    name="classMember83",
    ends={
        Property(name="alf_ClassMember", type=alf_ClassBody, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassBody84", type=alf_ClassMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotypeAnnotations85: BinaryAssociation = BinaryAssociation(
    name="stereotypeAnnotations85",
    ends={
        Property(name="alf_StereotypeAnnotations87", type=alf_ClassMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassMember86", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibilityIndicator88: BinaryAssociation = BinaryAssociation(
    name="visibilityIndicator88",
    ends={
        Property(name="alf_VisibilityIndicator", type=alf_ClassMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassMember89", type=alf_VisibilityIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classMemberDefinition90: BinaryAssociation = BinaryAssociation(
    name="classMemberDefinition90",
    ends={
        Property(name="alf_ClassMemberDefinition", type=alf_ClassMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassMember91", type=alf_ClassMemberDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierSignature72: BinaryAssociation = BinaryAssociation(
    name="classifierSignature72",
    ends={
        Property(name="alf_ClassifierSignature73", type=alf_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassDeclaration", type=alf_ClassifierSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classDeclaration74: BinaryAssociation = BinaryAssociation(
    name="classDeclaration74",
    ends={
        Property(name="alf_ClassDeclaration75", type=alf_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassDefinition", type=alf_ClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classBody76: BinaryAssociation = BinaryAssociation(
    name="classBody76",
    ends={
        Property(name="alf_ClassBody", type=alf_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassDefinition77", type=alf_ClassBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classDeclaration78: BinaryAssociation = BinaryAssociation(
    name="classDeclaration78",
    ends={
        Property(name="alf_ClassDeclaration79", type=alf_ClassDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassDefinitionOrStub", type=alf_ClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activeClassDeclaration98: BinaryAssociation = BinaryAssociation(
    name="activeClassDeclaration98",
    ends={
        Property(name="alf_ActiveClassDeclaration99", type=alf_ActiveClassDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassDefinitionOrStub", type=alf_ActiveClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activeClassBody100: BinaryAssociation = BinaryAssociation(
    name="activeClassBody100",
    ends={
        Property(name="alf_ActiveClassBody102", type=alf_ActiveClassDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassDefinitionOrStub101", type=alf_ActiveClassBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activeClassMember103: BinaryAssociation = BinaryAssociation(
    name="activeClassMember103",
    ends={
        Property(name="alf_ActiveClassMember", type=alf_ActiveClassBody, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassBody104", type=alf_ActiveClassMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorClasue105: BinaryAssociation = BinaryAssociation(
    name="behaviorClasue105",
    ends={
        Property(name="alf_BehaviorClause", type=alf_ActiveClassBody, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassBody106", type=alf_BehaviorClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block107: BinaryAssociation = BinaryAssociation(
    name="block107",
    ends={
        Property(name="alf_Block", type=alf_BehaviorClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BehaviorClause108", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierSignature92: BinaryAssociation = BinaryAssociation(
    name="classifierSignature92",
    ends={
        Property(name="alf_ClassifierSignature93", type=alf_ActiveClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassDeclaration", type=alf_ClassifierSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activeClassDeclaration94: BinaryAssociation = BinaryAssociation(
    name="activeClassDeclaration94",
    ends={
        Property(name="alf_ActiveClassDeclaration95", type=alf_ActiveClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassDefinition", type=alf_ActiveClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activeClassBody96: BinaryAssociation = BinaryAssociation(
    name="activeClassBody96",
    ends={
        Property(name="alf_ActiveClassBody", type=alf_ActiveClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassDefinition97", type=alf_ActiveClassBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierSignature120: BinaryAssociation = BinaryAssociation(
    name="classifierSignature120",
    ends={
        Property(name="alf_ClassifierSignature121", type=alf_DataTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DataTypeDeclaration", type=alf_ClassifierSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataTypeDeclaration122: BinaryAssociation = BinaryAssociation(
    name="dataTypeDeclaration122",
    ends={
        Property(name="alf_DataTypeDeclaration123", type=alf_DataTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DataTypeDefinition", type=alf_DataTypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structureBody124: BinaryAssociation = BinaryAssociation(
    name="structureBody124",
    ends={
        Property(name="alf_StructuredBody", type=alf_DataTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DataTypeDefinition125", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataTypeDeclaration126: BinaryAssociation = BinaryAssociation(
    name="dataTypeDeclaration126",
    ends={
        Property(name="alf_DataTypeDeclaration127", type=alf_DataTypeDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DataTypeDefinitionOrStub", type=alf_DataTypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structureBody128: BinaryAssociation = BinaryAssociation(
    name="structureBody128",
    ends={
        Property(name="alf_StructuredBody130", type=alf_DataTypeDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DataTypeDefinitionOrStub129", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name109: BinaryAssociation = BinaryAssociation(
    name="name109",
    ends={
        Property(name="alf_Name111", type=alf_BehaviorClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BehaviorClause110", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stereotypeAnnotations112: BinaryAssociation = BinaryAssociation(
    name="stereotypeAnnotations112",
    ends={
        Property(name="alf_StereotypeAnnotations114", type=alf_ActiveClassMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassMember113", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibilityIndicator115: BinaryAssociation = BinaryAssociation(
    name="visibilityIndicator115",
    ends={
        Property(name="alf_VisibilityIndicator117", type=alf_ActiveClassMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassMember116", type=alf_VisibilityIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activeClassMemberDefinition118: BinaryAssociation = BinaryAssociation(
    name="activeClassMemberDefinition118",
    ends={
        Property(name="alf_ActiveClassMemberDefinition", type=alf_ActiveClassMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActiveClassMember119", type=alf_ActiveClassMemberDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierSignature138: BinaryAssociation = BinaryAssociation(
    name="classifierSignature138",
    ends={
        Property(name="alf_ClassifierSignature139", type=alf_AssociationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssociationDeclaration", type=alf_ClassifierSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associationDeclaration140: BinaryAssociation = BinaryAssociation(
    name="associationDeclaration140",
    ends={
        Property(name="alf_AssociationDeclaration141", type=alf_AssociationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssociationDefinition", type=alf_AssociationDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredBody142: BinaryAssociation = BinaryAssociation(
    name="structuredBody142",
    ends={
        Property(name="alf_StructuredBody144", type=alf_AssociationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssociationDefinition143", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associationDeclaration145: BinaryAssociation = BinaryAssociation(
    name="associationDeclaration145",
    ends={
        Property(name="alf_AssociationDeclaration146", type=alf_AssociationDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssociationDefinitionOrStub", type=alf_AssociationDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredMember131: BinaryAssociation = BinaryAssociation(
    name="structuredMember131",
    ends={
        Property(name="alf_StructuredMember", type=alf_StructuredBody, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StructuredBody132", type=alf_StructuredMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
streotypeAnnotations133: BinaryAssociation = BinaryAssociation(
    name="streotypeAnnotations133",
    ends={
        Property(name="alf_StereotypeAnnotations135", type=alf_StructuredMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StructuredMember134", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyDefinition136: BinaryAssociation = BinaryAssociation(
    name="propertyDefinition136",
    ends={
        Property(name="alf_PropertyDefinition", type=alf_StructuredMember, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StructuredMember137", type=alf_PropertyDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationDeclaration159: BinaryAssociation = BinaryAssociation(
    name="enumerationDeclaration159",
    ends={
        Property(name="alf_EnumerationDeclaration160", type=alf_EnumerationDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationDefinitionOrStub", type=alf_EnumerationDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationBody161: BinaryAssociation = BinaryAssociation(
    name="enumerationBody161",
    ends={
        Property(name="alf_EnumerationBody163", type=alf_EnumerationDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationDefinitionOrStub162", type=alf_EnumerationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationLiteralName164: BinaryAssociation = BinaryAssociation(
    name="enumerationLiteralName164",
    ends={
        Property(name="alf_EnumerationLiteralName", type=alf_EnumerationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationBody165", type=alf_EnumerationLiteralName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name166: BinaryAssociation = BinaryAssociation(
    name="name166",
    ends={
        Property(name="alf_Name168", type=alf_EnumerationLiteralName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationLiteralName167", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredBody147: BinaryAssociation = BinaryAssociation(
    name="structuredBody147",
    ends={
        Property(name="alf_StructuredBody149", type=alf_AssociationDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssociationDefinitionOrStub148", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name150: BinaryAssociation = BinaryAssociation(
    name="name150",
    ends={
        Property(name="alf_Name151", type=alf_EnumerationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationDeclaration", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specializationClause152: BinaryAssociation = BinaryAssociation(
    name="specializationClause152",
    ends={
        Property(name="alf_SpecializationClause154", type=alf_EnumerationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationDeclaration153", type=alf_SpecializationClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationClause155: BinaryAssociation = BinaryAssociation(
    name="enumerationClause155",
    ends={
        Property(name="alf_EnumerationDeclaration156", type=alf_EnumerationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationDefinition", type=alf_EnumerationDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationBody157: BinaryAssociation = BinaryAssociation(
    name="enumerationBody157",
    ends={
        Property(name="alf_EnumerationBody", type=alf_EnumerationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EnumerationDefinition158", type=alf_EnumerationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signalDeclaration176: BinaryAssociation = BinaryAssociation(
    name="signalDeclaration176",
    ends={
        Property(name="alf_SignalDeclaration177", type=alf_SignalDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalDefinitionOrStub", type=alf_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredBody178: BinaryAssociation = BinaryAssociation(
    name="structuredBody178",
    ends={
        Property(name="alf_StructuredBody180", type=alf_SignalDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalDefinitionOrStub179", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name181: BinaryAssociation = BinaryAssociation(
    name="name181",
    ends={
        Property(name="alf_Name182", type=alf_ActivityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDeclaration", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateParameters183: BinaryAssociation = BinaryAssociation(
    name="templateParameters183",
    ends={
        Property(name="alf_TemplateParameters185", type=alf_ActivityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDeclaration184", type=alf_TemplateParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters186: BinaryAssociation = BinaryAssociation(
    name="formalParameters186",
    ends={
        Property(name="alf_FormalParameters", type=alf_ActivityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDeclaration187", type=alf_FormalParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierSignature169: BinaryAssociation = BinaryAssociation(
    name="classifierSignature169",
    ends={
        Property(name="alf_ClassifierSignature170", type=alf_SignalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalDeclaration", type=alf_ClassifierSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signalDeclaration171: BinaryAssociation = BinaryAssociation(
    name="signalDeclaration171",
    ends={
        Property(name="alf_SignalDeclaration172", type=alf_SignalDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalDefinition", type=alf_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredBody173: BinaryAssociation = BinaryAssociation(
    name="structuredBody173",
    ends={
        Property(name="alf_StructuredBody175", type=alf_SignalDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalDefinition174", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList200: BinaryAssociation = BinaryAssociation(
    name="formalParameterList200",
    ends={
        Property(name="alf_FormalParameterList", type=alf_FormalParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameters201", type=alf_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameter202: BinaryAssociation = BinaryAssociation(
    name="formalParameter202",
    ends={
        Property(name="alf_FormalParameter", type=alf_FormalParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameterList203", type=alf_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotypeAnnotations204: BinaryAssociation = BinaryAssociation(
    name="stereotypeAnnotations204",
    ends={
        Property(name="alf_StereotypeAnnotations206", type=alf_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameter205", type=alf_StereotypeAnnotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typePart188: BinaryAssociation = BinaryAssociation(
    name="typePart188",
    ends={
        Property(name="alf_TypePart", type=alf_ActivityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDeclaration189", type=alf_TypePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activityDeclaration190: BinaryAssociation = BinaryAssociation(
    name="activityDeclaration190",
    ends={
        Property(name="alf_ActivityDeclaration191", type=alf_ActivityDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDefinition", type=alf_ActivityDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block192: BinaryAssociation = BinaryAssociation(
    name="block192",
    ends={
        Property(name="alf_Block194", type=alf_ActivityDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDefinition193", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activityDeclaration195: BinaryAssociation = BinaryAssociation(
    name="activityDeclaration195",
    ends={
        Property(name="alf_ActivityDeclaration196", type=alf_ActivityDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDefinitionOrStub", type=alf_ActivityDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block197: BinaryAssociation = BinaryAssociation(
    name="block197",
    ends={
        Property(name="alf_Block199", type=alf_ActivityDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ActivityDefinitionOrStub198", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyDeclaration215: BinaryAssociation = BinaryAssociation(
    name="propertyDeclaration215",
    ends={
        Property(name="alf_PropertyDeclaration216", type=alf_AttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AttributeDefinition", type=alf_PropertyDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeInitializer217: BinaryAssociation = BinaryAssociation(
    name="attributeInitializer217",
    ends={
        Property(name="alf_AttributeInitializer", type=alf_AttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AttributeDefinition218", type=alf_AttributeInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializationExpression219: BinaryAssociation = BinaryAssociation(
    name="initializationExpression219",
    ends={
        Property(name="alf_InitializationExpression", type=alf_AttributeInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AttributeInitializer220", type=alf_InitializationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name221: BinaryAssociation = BinaryAssociation(
    name="name221",
    ends={
        Property(name="alf_Name223", type=alf_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyDeclaration222", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name207: BinaryAssociation = BinaryAssociation(
    name="name207",
    ends={
        Property(name="alf_Name209", type=alf_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameter208", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typePart210: BinaryAssociation = BinaryAssociation(
    name="typePart210",
    ends={
        Property(name="alf_TypePart212", type=alf_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameter211", type=alf_TypePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyDeclaration213: BinaryAssociation = BinaryAssociation(
    name="propertyDeclaration213",
    ends={
        Property(name="alf_PropertyDeclaration", type=alf_PropertyDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyDefinition214", type=alf_PropertyDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicityRange234: BinaryAssociation = BinaryAssociation(
    name="multiplicityRange234",
    ends={
        Property(name="alf_Multiplicity235", type=alf_MultiplicityRange, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="alf_MultiplicityRange", type=alf_Multiplicity, multiplicity=Multiplicity(1, 1))
    }
)
lower236: BinaryAssociation = BinaryAssociation(
    name="lower236",
    ends={
        Property(name="alf_INTEGER_LITERAL", type=alf_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicityRange237", type=alf_INTEGER_LITERAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upper238: BinaryAssociation = BinaryAssociation(
    name="upper238",
    ends={
        Property(name="alf_UnlimitedNaturalLiteral", type=alf_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicityRange239", type=alf_UnlimitedNaturalLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer240: BinaryAssociation = BinaryAssociation(
    name="integer240",
    ends={
        Property(name="alf_INTEGER_LITERAL242", type=alf_UnlimitedNaturalLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnlimitedNaturalLiteral241", type=alf_INTEGER_LITERAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typePart224: BinaryAssociation = BinaryAssociation(
    name="typePart224",
    ends={
        Property(name="alf_TypePart226", type=alf_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyDeclaration225", type=alf_TypePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName227: BinaryAssociation = BinaryAssociation(
    name="typeName227",
    ends={
        Property(name="alf_TypeName", type=alf_TypePart, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TypePart228", type=alf_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity229: BinaryAssociation = BinaryAssociation(
    name="multiplicity229",
    ends={
        Property(name="alf_Multiplicity", type=alf_TypePart, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TypePart230", type=alf_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName231: BinaryAssociation = BinaryAssociation(
    name="qualifiedName231",
    ends={
        Property(name="alf_QualifiedName233", type=alf_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TypeName232", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList256: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList256",
    ends={
        Property(name="alf_QualifiedNameList258", type=alf_RedefinitionClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RedefinitionClause257", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receptionName259: BinaryAssociation = BinaryAssociation(
    name="receptionName259",
    ends={
        Property(name="alf_QualifiedName260", type=alf_ReceptionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ReceptionDefinition", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signalName261: BinaryAssociation = BinaryAssociation(
    name="signalName261",
    ends={
        Property(name="alf_Name262", type=alf_SignalReceptionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalReceptionDeclaration", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name243: BinaryAssociation = BinaryAssociation(
    name="name243",
    ends={
        Property(name="alf_Name244", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters245: BinaryAssociation = BinaryAssociation(
    name="formalParameters245",
    ends={
        Property(name="alf_FormalParameters247", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration246", type=alf_FormalParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typePart248: BinaryAssociation = BinaryAssociation(
    name="typePart248",
    ends={
        Property(name="alf_TypePart250", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration249", type=alf_TypePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinitionClause251: BinaryAssociation = BinaryAssociation(
    name="redefinitionClause251",
    ends={
        Property(name="alf_RedefinitionClause", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration252", type=alf_RedefinitionClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block253: BinaryAssociation = BinaryAssociation(
    name="block253",
    ends={
        Property(name="alf_Block255", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration254", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameCompletion273: BinaryAssociation = BinaryAssociation(
    name="nameCompletion273",
    ends={
        Property(name="alf_ColonQualifiedNameCompletion", type=alf_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedName274", type=alf_ColonQualifiedNameCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedBindings275: BinaryAssociation = BinaryAssociation(
    name="namedBindings275",
    ends={
        Property(name="alf_NameBinding", type=alf_ColonQualifiedNameCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ColonQualifiedNameCompletion276", type=alf_NameBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name277: BinaryAssociation = BinaryAssociation(
    name="name277",
    ends={
        Property(name="alf_Name279", type=alf_NameBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameBinding278", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding280: BinaryAssociation = BinaryAssociation(
    name="templateBinding280",
    ends={
        Property(name="alf_TemplateBinding", type=alf_NameBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameBinding281", type=alf_TemplateBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specializationClause263: BinaryAssociation = BinaryAssociation(
    name="specializationClause263",
    ends={
        Property(name="alf_SpecializationClause265", type=alf_SignalReceptionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalReceptionDeclaration264", type=alf_SpecializationClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signalReceptionOrDeclaration266: BinaryAssociation = BinaryAssociation(
    name="signalReceptionOrDeclaration266",
    ends={
        Property(name="alf_SignalReceptionDeclaration267", type=alf_SignalReceptionDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalReceptionDefinitionOrStub", type=alf_SignalReceptionDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredBody268: BinaryAssociation = BinaryAssociation(
    name="structuredBody268",
    ends={
        Property(name="alf_StructuredBody270", type=alf_SignalReceptionDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SignalReceptionDefinitionOrStub269", type=alf_StructuredBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unqualified271: BinaryAssociation = BinaryAssociation(
    name="unqualified271",
    ends={
        Property(name="alf_UnqualifiedName", type=alf_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedName272", type=alf_UnqualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateParameterSubstitution291: BinaryAssociation = BinaryAssociation(
    name="templateParameterSubstitution291",
    ends={
        Property(name="alf_TemplateParameterSubstitution", type=alf_NamedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NamedTemplateBinding", type=alf_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name292: BinaryAssociation = BinaryAssociation(
    name="name292",
    ends={
        Property(name="alf_Name294", type=alf_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TemplateParameterSubstitution293", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName295: BinaryAssociation = BinaryAssociation(
    name="qualifiedName295",
    ends={
        Property(name="alf_QualifiedName297", type=alf_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TemplateParameterSubstitution296", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unqualified282: BinaryAssociation = BinaryAssociation(
    name="unqualified282",
    ends={
        Property(name="alf_Name283", type=alf_QualifiedNameWithoutBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameWithoutBinding", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameCompletion284: BinaryAssociation = BinaryAssociation(
    name="nameCompletion284",
    ends={
        Property(name="alf_ColonQualifiedNameCompletionWithoutBinding", type=alf_QualifiedNameWithoutBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameWithoutBinding285", type=alf_ColonQualifiedNameCompletionWithoutBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names286: BinaryAssociation = BinaryAssociation(
    name="names286",
    ends={
        Property(name="alf_Name288", type=alf_ColonQualifiedNameCompletionWithoutBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ColonQualifiedNameCompletionWithoutBinding287", type=alf_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiedName289: BinaryAssociation = BinaryAssociation(
    name="qualifiedName289",
    ends={
        Property(name="alf_QualifiedName290", type=alf_PositionalTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PositionalTemplateBinding", type=alf_QualifiedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryToExpressionCompletion306: BinaryAssociation = BinaryAssociation(
    name="primaryToExpressionCompletion306",
    ends={
        Property(name="alf_PrimaryToExpressionCompletion", type=alf_NameToExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameToExpressionCompletion307", type=alf_PrimaryToExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postFixExpressionCompletion308: BinaryAssociation = BinaryAssociation(
    name="postFixExpressionCompletion308",
    ends={
        Property(name="alf_PostfixExpressionCompletion", type=alf_PrimaryToExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryToExpressionCompletion309", type=alf_PostfixExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCompletion310: BinaryAssociation = BinaryAssociation(
    name="expressionCompletion310",
    ends={
        Property(name="alf_ExpressionCompletion312", type=alf_PrimaryToExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryToExpressionCompletion311", type=alf_ExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression313: BinaryAssociation = BinaryAssociation(
    name="expression313",
    ends={
        Property(name="alf_Expression315", type=alf_ExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExpressionCompletion314", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression298: BinaryAssociation = BinaryAssociation(
    name="unaryExpression298",
    ends={
        Property(name="alf_UnaryExpression", type=alf_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Expression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCompletion299: BinaryAssociation = BinaryAssociation(
    name="expressionCompletion299",
    ends={
        Property(name="alf_ExpressionCompletion", type=alf_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Expression300", type=alf_ExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonNameUnaryExpression301: BinaryAssociation = BinaryAssociation(
    name="nonNameUnaryExpression301",
    ends={
        Property(name="alf_NonNameUnaryExpression", type=alf_NonNameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNameExpression", type=alf_NonNameUnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionCompletion302: BinaryAssociation = BinaryAssociation(
    name="expressionCompletion302",
    ends={
        Property(name="alf_ExpressionCompletion304", type=alf_NonNameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNameExpression303", type=alf_ExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameToPrimary305: BinaryAssociation = BinaryAssociation(
    name="nameToPrimary305",
    ends={
        Property(name="alf_NameToPrimaryExpression", type=alf_NameToExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameToExpressionCompletion", type=alf_NameToPrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceConstructionCompletion327: BinaryAssociation = BinaryAssociation(
    name="sequenceConstructionCompletion327",
    ends={
        Property(name="alf_SequenceConstructionExpressionCompletion", type=alf_NameToPrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameToPrimaryExpression328", type=alf_SequenceConstructionExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behaviorInvocation329: BinaryAssociation = BinaryAssociation(
    name="behaviorInvocation329",
    ends={
        Property(name="alf_BehaviorInvocation", type=alf_NameToPrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameToPrimaryExpression330", type=alf_BehaviorInvocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content331: BinaryAssociation = BinaryAssociation(
    name="content331",
    ends={
        Property(name="alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index", type=alf_PrimaryExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpressionCompletion332", type=alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature333: BinaryAssociation = BinaryAssociation(
    name="feature333",
    ends={
        Property(name="alf_Feature", type=alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index334", type=alf_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameOrPrimaryExpression316: BinaryAssociation = BinaryAssociation(
    name="nameOrPrimaryExpression316",
    ends={
        Property(name="alf_NameOrPrimaryExpression", type=alf_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpression", type=alf_NameOrPrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseExpression317: BinaryAssociation = BinaryAssociation(
    name="baseExpression317",
    ends={
        Property(name="alf_BaseExpression", type=alf_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpression318", type=alf_BaseExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parenthesizedExpression319: BinaryAssociation = BinaryAssociation(
    name="parenthesizedExpression319",
    ends={
        Property(name="alf_ParenthesizedExpression", type=alf_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpression320", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpressionCompletion321: BinaryAssociation = BinaryAssociation(
    name="primaryExpressionCompletion321",
    ends={
        Property(name="alf_PrimaryExpressionCompletion", type=alf_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpression322", type=alf_PrimaryExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkOperationCompletion323: BinaryAssociation = BinaryAssociation(
    name="linkOperationCompletion323",
    ends={
        Property(name="alf_LinkOperationCompletion", type=alf_NameToPrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameToPrimaryExpression324", type=alf_LinkOperationCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classExtentExpressionCompletion325: BinaryAssociation = BinaryAssociation(
    name="classExtentExpressionCompletion325",
    ends={
        Property(name="alf_ClassExtentExpressionCompletion", type=alf_NameToPrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameToPrimaryExpression326", type=alf_ClassExtentExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameToPrimaryExpression346: BinaryAssociation = BinaryAssociation(
    name="nameToPrimaryExpression346",
    ends={
        Property(name="alf_NameToPrimaryExpression348", type=alf_NameOrPrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameOrPrimaryExpression347", type=alf_NameToPrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple349: BinaryAssociation = BinaryAssociation(
    name="tuple349",
    ends={
        Property(name="alf_Tuple", type=alf_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisExpression", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression350: BinaryAssociation = BinaryAssociation(
    name="expression350",
    ends={
        Property(name="alf_Expression352", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression351", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name353: BinaryAssociation = BinaryAssociation(
    name="name353",
    ends={
        Property(name="alf_Name355", type=alf_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Feature354", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureInvocation335: BinaryAssociation = BinaryAssociation(
    name="featureInvocation335",
    ends={
        Property(name="alf_FeatureInvocation", type=alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index336", type=alf_FeatureInvocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceOperationOrReductionOrExpansion337: BinaryAssociation = BinaryAssociation(
    name="sequenceOperationOrReductionOrExpansion337",
    ends={
        Property(name="alf_SequenceOperationOrReductionOrExpansion", type=alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338", type=alf_SequenceOperationOrReductionOrExpansion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index339: BinaryAssociation = BinaryAssociation(
    name="index339",
    ends={
        Property(name="alf_Index", type=alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index340", type=alf_Index, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression341: BinaryAssociation = BinaryAssociation(
    name="expression341",
    ends={
        Property(name="alf_PRIMITIVE_LITERAL342", type=alf_LiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LiteralExpression", type=alf_PRIMITIVE_LITERAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
potentiallyAmbiguousQualifiedName343: BinaryAssociation = BinaryAssociation(
    name="potentiallyAmbiguousQualifiedName343",
    ends={
        Property(name="alf_QualifiedNameWithoutBinding345", type=alf_NameOrPrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameOrPrimaryExpression344", type=alf_QualifiedNameWithoutBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedExpression365: BinaryAssociation = BinaryAssociation(
    name="namedExpression365",
    ends={
        Property(name="alf_NamedTupleExpressionList366", type=alf_NamedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="alf_NamedExpression", type=alf_NamedTupleExpressionList, multiplicity=Multiplicity(1, 1))
    }
)
name367: BinaryAssociation = BinaryAssociation(
    name="name367",
    ends={
        Property(name="alf_Name369", type=alf_NamedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NamedExpression368", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression370: BinaryAssociation = BinaryAssociation(
    name="expression370",
    ends={
        Property(name="alf_Expression372", type=alf_NamedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NamedExpression371", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple373: BinaryAssociation = BinaryAssociation(
    name="tuple373",
    ends={
        Property(name="alf_Tuple375", type=alf_BehaviorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BehaviorInvocation374", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedTupleExpressionList356: BinaryAssociation = BinaryAssociation(
    name="namedTupleExpressionList356",
    ends={
        Property(name="alf_NamedTupleExpressionList", type=alf_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Tuple357", type=alf_NamedTupleExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positionalTupleExpressionList358: BinaryAssociation = BinaryAssociation(
    name="positionalTupleExpressionList358",
    ends={
        Property(name="alf_PositionalTupleExpressionList", type=alf_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Tuple359", type=alf_PositionalTupleExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression360: BinaryAssociation = BinaryAssociation(
    name="expression360",
    ends={
        Property(name="alf_Expression362", type=alf_PositionalTupleExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PositionalTupleExpressionList361", type=alf_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression363: BinaryAssociation = BinaryAssociation(
    name="expression363",
    ends={
        Property(name="alf_Expression364", type=alf_PositionalTupleExpressionListCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PositionalTupleExpressionListCompletion", type=alf_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple389: BinaryAssociation = BinaryAssociation(
    name="tuple389",
    ends={
        Property(name="alf_Tuple391", type=alf_InstanceCreationOrSequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationOrSequenceConstructionExpression390", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkOperationTuple392: BinaryAssociation = BinaryAssociation(
    name="linkOperationTuple392",
    ends={
        Property(name="alf_LinkOperationTuple", type=alf_LinkOperationCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationCompletion393", type=alf_LinkOperationTuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple376: BinaryAssociation = BinaryAssociation(
    name="tuple376",
    ends={
        Property(name="alf_Tuple378", type=alf_FeatureInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FeatureInvocation377", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name394: BinaryAssociation = BinaryAssociation(
    name="name394",
    ends={
        Property(name="alf_Name396", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple395", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index397: BinaryAssociation = BinaryAssociation(
    name="index397",
    ends={
        Property(name="alf_Index399", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple398", type=alf_Index, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName379: BinaryAssociation = BinaryAssociation(
    name="qualifiedName379",
    ends={
        Property(name="alf_QualifiedName380", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationExpression", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexNamedExpressionListCompletion400: BinaryAssociation = BinaryAssociation(
    name="indexNamedExpressionListCompletion400",
    ends={
        Property(name="alf_IndexedNamedExpressionListCompletion", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple401", type=alf_IndexedNamedExpressionListCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple381: BinaryAssociation = BinaryAssociation(
    name="tuple381",
    ends={
        Property(name="alf_Tuple383", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationExpression382", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName384: BinaryAssociation = BinaryAssociation(
    name="qualifiedName384",
    ends={
        Property(name="alf_QualifiedName385", type=alf_InstanceCreationOrSequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationOrSequenceConstructionExpression", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceConstructionExpressionCompletion386: BinaryAssociation = BinaryAssociation(
    name="sequenceConstructionExpressionCompletion386",
    ends={
        Property(name="alf_SequenceConstructionExpressionCompletion388", type=alf_InstanceCreationOrSequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationOrSequenceConstructionExpression387", type=alf_SequenceConstructionExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameToExpressionCompletion411: BinaryAssociation = BinaryAssociation(
    name="nameToExpressionCompletion411",
    ends={
        Property(name="alf_NameToExpressionCompletion413", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple412", type=alf_NameToExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positionalTupleExpressionList414: BinaryAssociation = BinaryAssociation(
    name="positionalTupleExpressionList414",
    ends={
        Property(name="alf_PositionalTupleExpressionList416", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple415", type=alf_PositionalTupleExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression417: BinaryAssociation = BinaryAssociation(
    name="expression417",
    ends={
        Property(name="alf_Expression419", type=alf_IndexedNamedExpressionListCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IndexedNamedExpressionListCompletion418", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexedNamedExpression420: BinaryAssociation = BinaryAssociation(
    name="indexedNamedExpression420",
    ends={
        Property(name="alf_IndexedNamedExpression", type=alf_IndexedNamedExpressionListCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IndexedNamedExpressionListCompletion421", type=alf_IndexedNamedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name422: BinaryAssociation = BinaryAssociation(
    name="name422",
    ends={
        Property(name="alf_Name424", type=alf_IndexedNamedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IndexedNamedExpression423", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index425: BinaryAssociation = BinaryAssociation(
    name="index425",
    ends={
        Property(name="alf_Index427", type=alf_IndexedNamedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IndexedNamedExpression426", type=alf_Index, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression428: BinaryAssociation = BinaryAssociation(
    name="expression428",
    ends={
        Property(name="alf_Expression430", type=alf_IndexedNamedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IndexedNamedExpression429", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryToExpressionCompletion402: BinaryAssociation = BinaryAssociation(
    name="primaryToExpressionCompletion402",
    ends={
        Property(name="alf_PrimaryToExpressionCompletion404", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple403", type=alf_PrimaryToExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceConstructionExpressionCompletion431: BinaryAssociation = BinaryAssociation(
    name="sequenceConstructionExpressionCompletion431",
    ends={
        Property(name="alf_SequenceConstructionExpressionCompletion432", type=alf_SequenceAnyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceAnyExpression", type=alf_SequenceConstructionExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positionalTupleExpressionListCompletion405: BinaryAssociation = BinaryAssociation(
    name="positionalTupleExpressionListCompletion405",
    ends={
        Property(name="alf_PositionalTupleExpressionListCompletion407", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple406", type=alf_PositionalTupleExpressionListCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexedNamedExpressionListCompletion408: BinaryAssociation = BinaryAssociation(
    name="indexedNamedExpressionListCompletion408",
    ends={
        Property(name="alf_IndexedNamedExpressionListCompletion410", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple409", type=alf_IndexedNamedExpressionListCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceElements435: BinaryAssociation = BinaryAssociation(
    name="sequenceElements435",
    ends={
        Property(name="alf_SequenceElements", type=alf_SequenceConstructionExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionExpressionCompletion436", type=alf_SequenceElements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1437: BinaryAssociation = BinaryAssociation(
    name="expression1437",
    ends={
        Property(name="alf_Expression439", type=alf_SequenceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElements438", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2440: BinaryAssociation = BinaryAssociation(
    name="expression2440",
    ends={
        Property(name="alf_Expression442", type=alf_SequenceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElements441", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceElementListCompletion443: BinaryAssociation = BinaryAssociation(
    name="sequenceElementListCompletion443",
    ends={
        Property(name="alf_SequenceElementListCompletion", type=alf_SequenceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElements444", type=alf_SequenceElementListCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceInitializationExpression445: BinaryAssociation = BinaryAssociation(
    name="sequenceInitializationExpression445",
    ends={
        Property(name="alf_SequenceInitializationExpression", type=alf_SequenceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElements446", type=alf_SequenceInitializationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceElement447: BinaryAssociation = BinaryAssociation(
    name="sequenceElement447",
    ends={
        Property(name="alf_SequenceElement", type=alf_SequenceElementListCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElementListCompletion448", type=alf_SequenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceElements455: BinaryAssociation = BinaryAssociation(
    name="sequenceElements455",
    ends={
        Property(name="alf_SequenceInitializationExpression456", type=alf_SequenceElements, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="alf_SequenceElements457", type=alf_SequenceInitializationExpression, multiplicity=Multiplicity(1, 1))
    }
)
multiplicityIndicator433: BinaryAssociation = BinaryAssociation(
    name="multiplicityIndicator433",
    ends={
        Property(name="alf_MultiplicityIndicator", type=alf_SequenceConstructionExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionExpressionCompletion434", type=alf_MultiplicityIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression458: BinaryAssociation = BinaryAssociation(
    name="expression458",
    ends={
        Property(name="alf_Expression460", type=alf_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Index459", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName461: BinaryAssociation = BinaryAssociation(
    name="qualifiedName461",
    ends={
        Property(name="alf_EObject", type=alf_SequenceOperationOrReductionOrExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationOrReductionOrExpansion462", type=alf_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple463: BinaryAssociation = BinaryAssociation(
    name="tuple463",
    ends={
        Property(name="alf_Tuple465", type=alf_SequenceOperationOrReductionOrExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationOrReductionOrExpansion464", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding466: BinaryAssociation = BinaryAssociation(
    name="templateBinding466",
    ends={
        Property(name="alf_TemplateBinding468", type=alf_SequenceOperationOrReductionOrExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationOrReductionOrExpansion467", type=alf_TemplateBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name469: BinaryAssociation = BinaryAssociation(
    name="name469",
    ends={
        Property(name="alf_Name471", type=alf_SequenceOperationOrReductionOrExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationOrReductionOrExpansion470", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression449: BinaryAssociation = BinaryAssociation(
    name="expression449",
    ends={
        Property(name="alf_Expression451", type=alf_SequenceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElement450", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression472: BinaryAssociation = BinaryAssociation(
    name="expression472",
    ends={
        Property(name="alf_Expression474", type=alf_SequenceOperationOrReductionOrExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationOrReductionOrExpansion473", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceInitializationExpression452: BinaryAssociation = BinaryAssociation(
    name="sequenceInitializationExpression452",
    ends={
        Property(name="alf_SequenceInitializationExpression454", type=alf_SequenceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceElement453", type=alf_SequenceInitializationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpression480: BinaryAssociation = BinaryAssociation(
    name="primaryExpression480",
    ends={
        Property(name="alf_PrimaryExpression481", type=alf_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrefixExpression", type=alf_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonNamePostfixOrCastExpression482: BinaryAssociation = BinaryAssociation(
    name="nonNamePostfixOrCastExpression482",
    ends={
        Property(name="alf_NonNamePostfixOrCastExpression", type=alf_PostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PostfixOrCastExpression", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameOrPrimaryExpression483: BinaryAssociation = BinaryAssociation(
    name="nameOrPrimaryExpression483",
    ends={
        Property(name="alf_NameOrPrimaryExpression485", type=alf_PostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PostfixOrCastExpression484", type=alf_NameOrPrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postFixExpressionCompletion486: BinaryAssociation = BinaryAssociation(
    name="postFixExpressionCompletion486",
    ends={
        Property(name="alf_PostfixExpressionCompletion488", type=alf_PostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PostfixOrCastExpression487", type=alf_PostfixExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpressionCompletion475: BinaryAssociation = BinaryAssociation(
    name="primaryExpressionCompletion475",
    ends={
        Property(name="alf_PrimaryExpressionCompletion477", type=alf_PostfixExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PostfixExpressionCompletion476", type=alf_PrimaryExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfixOperation478: BinaryAssociation = BinaryAssociation(
    name="postfixOperation478",
    ends={
        Property(name="alf_PostfixOperation", type=alf_PostfixExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PostfixExpressionCompletion479", type=alf_PostfixOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castCompletion489: BinaryAssociation = BinaryAssociation(
    name="castCompletion489",
    ends={
        Property(name="alf_CastCompletion", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression490", type=alf_CastCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
potentiallyAmbiguousQualifiedName491: BinaryAssociation = BinaryAssociation(
    name="potentiallyAmbiguousQualifiedName491",
    ends={
        Property(name="alf_QualifiedNameWithoutBinding493", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression492", type=alf_QualifiedNameWithoutBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postifixExpressionCompletion494: BinaryAssociation = BinaryAssociation(
    name="postifixExpressionCompletion494",
    ends={
        Property(name="alf_PostfixExpressionCompletion496", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression495", type=alf_PostfixExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameToExpressionCompletion497: BinaryAssociation = BinaryAssociation(
    name="nameToExpressionCompletion497",
    ends={
        Property(name="alf_NameToExpressionCompletion499", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression498", type=alf_NameToExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfixExpressionCompletion500: BinaryAssociation = BinaryAssociation(
    name="postfixExpressionCompletion500",
    ends={
        Property(name="alf_PostfixExpressionCompletion502", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression501", type=alf_PostfixExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonNameExpression503: BinaryAssociation = BinaryAssociation(
    name="nonNameExpression503",
    ends={
        Property(name="alf_NonNameExpression505", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression504", type=alf_NonNameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseExpression506: BinaryAssociation = BinaryAssociation(
    name="baseExpression506",
    ends={
        Property(name="alf_BaseExpression508", type=alf_NonNamePostfixOrCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonNamePostfixOrCastExpression507", type=alf_BaseExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression513: BinaryAssociation = BinaryAssociation(
    name="unaryExpression513",
    ends={
        Property(name="alf_UnaryExpression514", type=alf_NumericUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NumericUnaryExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression515: BinaryAssociation = BinaryAssociation(
    name="unaryExpression515",
    ends={
        Property(name="alf_UnaryExpression516", type=alf_IsolationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IsolationExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression517: BinaryAssociation = BinaryAssociation(
    name="unaryExpression517",
    ends={
        Property(name="alf_UnaryExpression518", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicativeExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicativeExpressionCompletion519: BinaryAssociation = BinaryAssociation(
    name="multiplicativeExpressionCompletion519",
    ends={
        Property(name="alf_MultiplicativeExpressionCompletion", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicativeExpression520", type=alf_MultiplicativeExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression509: BinaryAssociation = BinaryAssociation(
    name="unaryExpression509",
    ends={
        Property(name="alf_UnaryExpression510", type=alf_BooleanNegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BooleanNegationExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression511: BinaryAssociation = BinaryAssociation(
    name="unaryExpression511",
    ends={
        Property(name="alf_UnaryExpression512", type=alf_BitStringComplementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BitStringComplementExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression524: BinaryAssociation = BinaryAssociation(
    name="unaryExpression524",
    ends={
        Property(name="alf_UnaryExpression525", type=alf_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AdditiveExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additiveExpressionCompletion526: BinaryAssociation = BinaryAssociation(
    name="additiveExpressionCompletion526",
    ends={
        Property(name="alf_AdditiveExpressionCompletion", type=alf_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AdditiveExpression527", type=alf_AdditiveExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicativeExpressionCompletion528: BinaryAssociation = BinaryAssociation(
    name="multiplicativeExpressionCompletion528",
    ends={
        Property(name="alf_MultiplicativeExpressionCompletion530", type=alf_AdditiveExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AdditiveExpressionCompletion529", type=alf_MultiplicativeExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicativeExpression531: BinaryAssociation = BinaryAssociation(
    name="multiplicativeExpression531",
    ends={
        Property(name="alf_MultiplicativeExpression533", type=alf_AdditiveExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AdditiveExpressionCompletion532", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression534: BinaryAssociation = BinaryAssociation(
    name="unaryExpression534",
    ends={
        Property(name="alf_UnaryExpression535", type=alf_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ShiftExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression521: BinaryAssociation = BinaryAssociation(
    name="unaryExpression521",
    ends={
        Property(name="alf_UnaryExpression523", type=alf_MultiplicativeExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicativeExpressionCompletion522", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additiveExpression541: BinaryAssociation = BinaryAssociation(
    name="additiveExpression541",
    ends={
        Property(name="alf_AdditiveExpression543", type=alf_ShiftExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ShiftExpressionCompletion542", type=alf_AdditiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression544: BinaryAssociation = BinaryAssociation(
    name="unaryExpression544",
    ends={
        Property(name="alf_UnaryExpression545", type=alf_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationalExpressionCompletion546: BinaryAssociation = BinaryAssociation(
    name="relationalExpressionCompletion546",
    ends={
        Property(name="alf_RelationalExpressionCompletion", type=alf_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpression547", type=alf_RelationalExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shiftExpressionCompletion548: BinaryAssociation = BinaryAssociation(
    name="shiftExpressionCompletion548",
    ends={
        Property(name="alf_ShiftExpressionCompletion550", type=alf_RelationalExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpressionCompletion549", type=alf_ShiftExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shiftExpression551: BinaryAssociation = BinaryAssociation(
    name="shiftExpression551",
    ends={
        Property(name="alf_ShiftExpression553", type=alf_RelationalExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpressionCompletion552", type=alf_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shiftExpressionCompletion536: BinaryAssociation = BinaryAssociation(
    name="shiftExpressionCompletion536",
    ends={
        Property(name="alf_ShiftExpressionCompletion", type=alf_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ShiftExpression537", type=alf_ShiftExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additiveExpressionCompletion538: BinaryAssociation = BinaryAssociation(
    name="additiveExpressionCompletion538",
    ends={
        Property(name="alf_AdditiveExpressionCompletion540", type=alf_ShiftExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ShiftExpressionCompletion539", type=alf_AdditiveExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationExpressionCompletion556: BinaryAssociation = BinaryAssociation(
    name="classificationExpressionCompletion556",
    ends={
        Property(name="alf_ClassificationExpressionCompletion", type=alf_ClassificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpression557", type=alf_ClassificationExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationalExpressionCompletion558: BinaryAssociation = BinaryAssociation(
    name="relationalExpressionCompletion558",
    ends={
        Property(name="alf_RelationalExpressionCompletion560", type=alf_ClassificationExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpressionCompletion559", type=alf_RelationalExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name561: BinaryAssociation = BinaryAssociation(
    name="name561",
    ends={
        Property(name="alf_QualifiedName563", type=alf_ClassificationExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpressionCompletion562", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression564: BinaryAssociation = BinaryAssociation(
    name="unaryExpression564",
    ends={
        Property(name="alf_UnaryExpression565", type=alf_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EqualityExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationExpressionCompletion566: BinaryAssociation = BinaryAssociation(
    name="classificationExpressionCompletion566",
    ends={
        Property(name="alf_ClassificationExpressionCompletion568", type=alf_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EqualityExpression567", type=alf_ClassificationExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression554: BinaryAssociation = BinaryAssociation(
    name="unaryExpression554",
    ends={
        Property(name="alf_UnaryExpression555", type=alf_ClassificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression574: BinaryAssociation = BinaryAssociation(
    name="unaryExpression574",
    ends={
        Property(name="alf_UnaryExpression575", type=alf_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AndExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
andExpressionCompletion576: BinaryAssociation = BinaryAssociation(
    name="andExpressionCompletion576",
    ends={
        Property(name="alf_AndExpressionCompletion", type=alf_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AndExpression577", type=alf_AndExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equalityExpressionCompletion578: BinaryAssociation = BinaryAssociation(
    name="equalityExpressionCompletion578",
    ends={
        Property(name="alf_EqualityExpressionCompletion580", type=alf_AndExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AndExpressionCompletion579", type=alf_EqualityExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equalityExpression581: BinaryAssociation = BinaryAssociation(
    name="equalityExpression581",
    ends={
        Property(name="alf_EqualityExpression583", type=alf_AndExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AndExpressionCompletion582", type=alf_EqualityExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression584: BinaryAssociation = BinaryAssociation(
    name="unaryExpression584",
    ends={
        Property(name="alf_UnaryExpression585", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExclusiveOrExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusiveOrExpressionCompletion586: BinaryAssociation = BinaryAssociation(
    name="exclusiveOrExpressionCompletion586",
    ends={
        Property(name="alf_ExclusiveOrExpressionCompletion", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExclusiveOrExpression587", type=alf_ExclusiveOrExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationExpressionCompletion569: BinaryAssociation = BinaryAssociation(
    name="classificationExpressionCompletion569",
    ends={
        Property(name="alf_ClassificationExpressionCompletion570", type=alf_EqualityExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EqualityExpressionCompletion", type=alf_ClassificationExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationExpression571: BinaryAssociation = BinaryAssociation(
    name="classificationExpression571",
    ends={
        Property(name="alf_ClassificationExpression573", type=alf_EqualityExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EqualityExpressionCompletion572", type=alf_ClassificationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression594: BinaryAssociation = BinaryAssociation(
    name="unaryExpression594",
    ends={
        Property(name="alf_UnaryExpression595", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InclusiveOrExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusiveOrExpressionCompletion596: BinaryAssociation = BinaryAssociation(
    name="inclusiveOrExpressionCompletion596",
    ends={
        Property(name="alf_InclusiveOrExpressionCompletion", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InclusiveOrExpression597", type=alf_InclusiveOrExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusiveOrExpressionCompletion598: BinaryAssociation = BinaryAssociation(
    name="exclusiveOrExpressionCompletion598",
    ends={
        Property(name="alf_ExclusiveOrExpressionCompletion600", type=alf_InclusiveOrExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InclusiveOrExpressionCompletion599", type=alf_ExclusiveOrExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusiveOrExpression601: BinaryAssociation = BinaryAssociation(
    name="exclusiveOrExpression601",
    ends={
        Property(name="alf_ExclusiveOrExpression603", type=alf_InclusiveOrExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InclusiveOrExpressionCompletion602", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression604: BinaryAssociation = BinaryAssociation(
    name="unaryExpression604",
    ends={
        Property(name="alf_UnaryExpression605", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalAndExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalAndExpressionCompletion606: BinaryAssociation = BinaryAssociation(
    name="conditionalAndExpressionCompletion606",
    ends={
        Property(name="alf_ConditionalAndExpressionCompletion", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalAndExpression607", type=alf_ConditionalAndExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
andExpressionCompletion588: BinaryAssociation = BinaryAssociation(
    name="andExpressionCompletion588",
    ends={
        Property(name="alf_AndExpressionCompletion590", type=alf_ExclusiveOrExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExclusiveOrExpressionCompletion589", type=alf_AndExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
andExpression591: BinaryAssociation = BinaryAssociation(
    name="andExpression591",
    ends={
        Property(name="alf_AndExpression593", type=alf_ExclusiveOrExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExclusiveOrExpressionCompletion592", type=alf_AndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalOrExpressionCompletion616: BinaryAssociation = BinaryAssociation(
    name="conditionalOrExpressionCompletion616",
    ends={
        Property(name="alf_ConditionalOrExpressionCompletion", type=alf_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalOrExpression617", type=alf_ConditionalOrExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalAndExpressionCompletion618: BinaryAssociation = BinaryAssociation(
    name="conditionalAndExpressionCompletion618",
    ends={
        Property(name="alf_ConditionalAndExpressionCompletion620", type=alf_ConditionalOrExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalOrExpressionCompletion619", type=alf_ConditionalAndExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalAndExpression621: BinaryAssociation = BinaryAssociation(
    name="conditionalAndExpression621",
    ends={
        Property(name="alf_ConditionalAndExpression623", type=alf_ConditionalOrExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalOrExpressionCompletion622", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression624: BinaryAssociation = BinaryAssociation(
    name="unaryExpression624",
    ends={
        Property(name="alf_UnaryExpression625", type=alf_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalExpressionCompletion626: BinaryAssociation = BinaryAssociation(
    name="conditionalExpressionCompletion626",
    ends={
        Property(name="alf_ConditionalExpressionCompletion", type=alf_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalExpression627", type=alf_ConditionalExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalOrExpressionCompletion628: BinaryAssociation = BinaryAssociation(
    name="conditionalOrExpressionCompletion628",
    ends={
        Property(name="alf_ConditionalOrExpressionCompletion630", type=alf_ConditionalExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalExpressionCompletion629", type=alf_ConditionalOrExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusiveOrExpressionCompletion608: BinaryAssociation = BinaryAssociation(
    name="inclusiveOrExpressionCompletion608",
    ends={
        Property(name="alf_InclusiveOrExpressionCompletion610", type=alf_ConditionalAndExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalAndExpressionCompletion609", type=alf_InclusiveOrExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusiveOrExpression611: BinaryAssociation = BinaryAssociation(
    name="inclusiveOrExpression611",
    ends={
        Property(name="alf_InclusiveOrExpression613", type=alf_ConditionalAndExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalAndExpressionCompletion612", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpression614: BinaryAssociation = BinaryAssociation(
    name="unaryExpression614",
    ends={
        Property(name="alf_UnaryExpression615", type=alf_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalOrExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentStatement634: BinaryAssociation = BinaryAssociation(
    name="documentStatement634",
    ends={
        Property(name="alf_DocumentedStatement", type=alf_StatementSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StatementSequence", type=alf_DocumentedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement635: BinaryAssociation = BinaryAssociation(
    name="statement635",
    ends={
        Property(name="alf_Statement", type=alf_DocumentedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DocumentedStatement636", type=alf_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalExpression631: BinaryAssociation = BinaryAssociation(
    name="conditionalExpression631",
    ends={
        Property(name="alf_ConditionalExpression633", type=alf_ConditionalExpressionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalExpressionCompletion632", type=alf_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement641: BinaryAssociation = BinaryAssociation(
    name="statement641",
    ends={
        Property(name="alf_Statement643", type=alf_AnnotatedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AnnotatedStatement642", type=alf_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation644: BinaryAssociation = BinaryAssociation(
    name="annotation644",
    ends={
        Property(name="alf_Annotation", type=alf_Annotations, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Annotations645", type=alf_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameList646: BinaryAssociation = BinaryAssociation(
    name="nameList646",
    ends={
        Property(name="alf_NameList", type=alf_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Annotation647", type=alf_NameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name648: BinaryAssociation = BinaryAssociation(
    name="name648",
    ends={
        Property(name="alf_Name650", type=alf_NameList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameList649", type=alf_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name651: BinaryAssociation = BinaryAssociation(
    name="name651",
    ends={
        Property(name="alf_Name652", type=alf_InLineStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InLineStatement", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementSequence637: BinaryAssociation = BinaryAssociation(
    name="statementSequence637",
    ends={
        Property(name="alf_StatementSequence639", type=alf_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Block638", type=alf_StatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations640: BinaryAssociation = BinaryAssociation(
    name="annotations640",
    ends={
        Property(name="alf_Annotations", type=alf_AnnotatedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AnnotatedStatement", type=alf_Annotations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
potentiallyAmbiguousName655: BinaryAssociation = BinaryAssociation(
    name="potentiallyAmbiguousName655",
    ends={
        Property(name="alf_QualifiedName656", type=alf_LocalNameDeclarationOrExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationOrExpressionStatement", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block653: BinaryAssociation = BinaryAssociation(
    name="block653",
    ends={
        Property(name="alf_Block654", type=alf_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BlockStatement", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicaityIndicator657: BinaryAssociation = BinaryAssociation(
    name="multiplicaityIndicator657",
    ends={
        Property(name="alf_MultiplicityIndicator659", type=alf_LocalNameDeclarationOrExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationOrExpressionStatement658", type=alf_MultiplicityIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name660: BinaryAssociation = BinaryAssociation(
    name="name660",
    ends={
        Property(name="alf_Name662", type=alf_LocalNameDeclarationOrExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationOrExpressionStatement661", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localNameDeclarationCompletion663: BinaryAssociation = BinaryAssociation(
    name="localNameDeclarationCompletion663",
    ends={
        Property(name="alf_LocalNameDeclarationStatementCompletion", type=alf_LocalNameDeclarationOrExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationOrExpressionStatement664", type=alf_LocalNameDeclarationStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameToExpressionCompletion665: BinaryAssociation = BinaryAssociation(
    name="nameToExpressionCompletion665",
    ends={
        Property(name="alf_NameToExpressionCompletion667", type=alf_LocalNameDeclarationOrExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationOrExpressionStatement666", type=alf_NameToExpressionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonNameExpression668: BinaryAssociation = BinaryAssociation(
    name="nonNameExpression668",
    ends={
        Property(name="alf_NonNameExpression670", type=alf_LocalNameDeclarationOrExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationOrExpressionStatement669", type=alf_NonNameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name671: BinaryAssociation = BinaryAssociation(
    name="name671",
    ends={
        Property(name="alf_Name672", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName673: BinaryAssociation = BinaryAssociation(
    name="typeName673",
    ends={
        Property(name="alf_TypeName675", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement674", type=alf_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicityIndicator676: BinaryAssociation = BinaryAssociation(
    name="multiplicityIndicator676",
    ends={
        Property(name="alf_MultiplicityIndicator678", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement677", type=alf_MultiplicityIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializationExpression682: BinaryAssociation = BinaryAssociation(
    name="initializationExpression682",
    ends={
        Property(name="alf_LocalNameDeclarationStatementCompletion683", type=alf_InitializationExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="alf_InitializationExpression684", type=alf_LocalNameDeclarationStatementCompletion, multiplicity=Multiplicity(1, 1))
    }
)
tuple685: BinaryAssociation = BinaryAssociation(
    name="tuple685",
    ends={
        Property(name="alf_Tuple686", type=alf_InstanceInitializationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceInitializationExpression", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequentialClauses687: BinaryAssociation = BinaryAssociation(
    name="sequentialClauses687",
    ends={
        Property(name="alf_SequentialClauses", type=alf_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IfStatement", type=alf_SequentialClauses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalClause688: BinaryAssociation = BinaryAssociation(
    name="finalClause688",
    ends={
        Property(name="alf_FinalClause", type=alf_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IfStatement689", type=alf_FinalClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concurrentClauses690: BinaryAssociation = BinaryAssociation(
    name="concurrentClauses690",
    ends={
        Property(name="alf_ConcurrentClauses", type=alf_SequentialClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequentialClauses691", type=alf_ConcurrentClauses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonFinalClause692: BinaryAssociation = BinaryAssociation(
    name="nonFinalClause692",
    ends={
        Property(name="alf_NonFinalClause", type=alf_ConcurrentClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConcurrentClauses693", type=alf_NonFinalClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression694: BinaryAssociation = BinaryAssociation(
    name="expression694",
    ends={
        Property(name="alf_Expression696", type=alf_NonFinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonFinalClause695", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localNameDeclarationCompletion679: BinaryAssociation = BinaryAssociation(
    name="localNameDeclarationCompletion679",
    ends={
        Property(name="alf_LocalNameDeclarationStatementCompletion681", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement680", type=alf_LocalNameDeclarationStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block700: BinaryAssociation = BinaryAssociation(
    name="block700",
    ends={
        Property(name="alf_Block702", type=alf_FinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FinalClause701", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression703: BinaryAssociation = BinaryAssociation(
    name="expression703",
    ends={
        Property(name="alf_Expression704", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchClause705: BinaryAssociation = BinaryAssociation(
    name="switchClause705",
    ends={
        Property(name="alf_SwitchClause", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement706", type=alf_SwitchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultClause707: BinaryAssociation = BinaryAssociation(
    name="defaultClause707",
    ends={
        Property(name="alf_SwitchDefaultClause", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement708", type=alf_SwitchDefaultClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchCase709: BinaryAssociation = BinaryAssociation(
    name="switchCase709",
    ends={
        Property(name="alf_SwitchCase", type=alf_SwitchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchClause710", type=alf_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementSequence711: BinaryAssociation = BinaryAssociation(
    name="statementSequence711",
    ends={
        Property(name="alf_NonEmptyStatementSequence", type=alf_SwitchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchClause712", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression713: BinaryAssociation = BinaryAssociation(
    name="expression713",
    ends={
        Property(name="alf_Expression715", type=alf_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchCase714", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block697: BinaryAssociation = BinaryAssociation(
    name="block697",
    ends={
        Property(name="alf_Block699", type=alf_NonFinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonFinalClause698", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement719: BinaryAssociation = BinaryAssociation(
    name="statement719",
    ends={
        Property(name="alf_DocumentedStatement721", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonEmptyStatementSequence720", type=alf_DocumentedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression722: BinaryAssociation = BinaryAssociation(
    name="expression722",
    ends={
        Property(name="alf_Expression723", type=alf_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_WhileStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block724: BinaryAssociation = BinaryAssociation(
    name="block724",
    ends={
        Property(name="alf_Block726", type=alf_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_WhileStatement725", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block727: BinaryAssociation = BinaryAssociation(
    name="block727",
    ends={
        Property(name="alf_Block728", type=alf_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DoStatement", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression729: BinaryAssociation = BinaryAssociation(
    name="expression729",
    ends={
        Property(name="alf_Expression731", type=alf_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DoStatement730", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forControl732: BinaryAssociation = BinaryAssociation(
    name="forControl732",
    ends={
        Property(name="alf_ForControl", type=alf_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForStatement", type=alf_ForControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block733: BinaryAssociation = BinaryAssociation(
    name="block733",
    ends={
        Property(name="alf_Block735", type=alf_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForStatement734", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementSequence716: BinaryAssociation = BinaryAssociation(
    name="statementSequence716",
    ends={
        Property(name="alf_NonEmptyStatementSequence718", type=alf_SwitchDefaultClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchDefaultClause717", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name738: BinaryAssociation = BinaryAssociation(
    name="name738",
    ends={
        Property(name="alf_Name740", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition739", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1741: BinaryAssociation = BinaryAssociation(
    name="expression1741",
    ends={
        Property(name="alf_Expression743", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition742", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2744: BinaryAssociation = BinaryAssociation(
    name="expression2744",
    ends={
        Property(name="alf_Expression746", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition745", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName747: BinaryAssociation = BinaryAssociation(
    name="typeName747",
    ends={
        Property(name="alf_QualifiedName749", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition748", type=alf_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression3750: BinaryAssociation = BinaryAssociation(
    name="expression3750",
    ends={
        Property(name="alf_Expression752", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition751", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression753: BinaryAssociation = BinaryAssociation(
    name="expression753",
    ends={
        Property(name="alf_Expression754", type=alf_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ReturnStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopVariableDefinition736: BinaryAssociation = BinaryAssociation(
    name="loopVariableDefinition736",
    ends={
        Property(name="alf_LoopVariableDefinition", type=alf_ForControl, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForControl737", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compoundCompletion758: BinaryAssociation = BinaryAssociation(
    name="compoundCompletion758",
    ends={
        Property(name="alf_CompoundAcceptStatementCompletion", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement759", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block760: BinaryAssociation = BinaryAssociation(
    name="block760",
    ends={
        Property(name="alf_Block762", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_CompoundAcceptStatementCompletion761", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acceptBlock763: BinaryAssociation = BinaryAssociation(
    name="acceptBlock763",
    ends={
        Property(name="alf_AcceptBlock", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_CompoundAcceptStatementCompletion764", type=alf_AcceptBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acceptClause765: BinaryAssociation = BinaryAssociation(
    name="acceptClause765",
    ends={
        Property(name="alf_AcceptClause767", type=alf_AcceptBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptBlock766", type=alf_AcceptClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block768: BinaryAssociation = BinaryAssociation(
    name="block768",
    ends={
        Property(name="alf_Block770", type=alf_AcceptBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptBlock769", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name771: BinaryAssociation = BinaryAssociation(
    name="name771",
    ends={
        Property(name="alf_Name773", type=alf_AcceptClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptClause772", type=alf_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList774: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList774",
    ends={
        Property(name="alf_QualifiedNameList776", type=alf_AcceptClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptClause775", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acceptClause755: BinaryAssociation = BinaryAssociation(
    name="acceptClause755",
    ends={
        Property(name="alf_AcceptClause", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement", type=alf_AcceptClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleCompletion756: BinaryAssociation = BinaryAssociation(
    name="simpleCompletion756",
    ends={
        Property(name="alf_SimpleAcceptStatementCompletion", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement757", type=alf_SimpleAcceptStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationClause779: BinaryAssociation = BinaryAssociation(
    name="classificationClause779",
    ends={
        Property(name="alf_ClassificationClause", type=alf_ClassifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifyStatement780", type=alf_ClassificationClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationFromClause781: BinaryAssociation = BinaryAssociation(
    name="classificationFromClause781",
    ends={
        Property(name="alf_ClassificationFromClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause782", type=alf_ClassificationFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classificationToClause783: BinaryAssociation = BinaryAssociation(
    name="classificationToClause783",
    ends={
        Property(name="alf_ClassificationToClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause784", type=alf_ClassificationToClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reclassifyAllClause785: BinaryAssociation = BinaryAssociation(
    name="reclassifyAllClause785",
    ends={
        Property(name="alf_ReclassifyAllClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause786", type=alf_ReclassifyAllClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList787: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList787",
    ends={
        Property(name="alf_QualifiedNameList789", type=alf_ClassificationFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationFromClause788", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList790: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList790",
    ends={
        Property(name="alf_QualifiedNameList792", type=alf_ClassificationToClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationToClause791", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression777: BinaryAssociation = BinaryAssociation(
    name="expression777",
    ends={
        Property(name="alf_Expression778", type=alf_ClassifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifyStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName793: BinaryAssociation = BinaryAssociation(
    name="qualifiedName793",
    ends={
        Property(name="alf_QualifiedName795", type=alf_QualifiedNameList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameList794", type=alf_QualifiedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_alf_BOOLEAN_LITERAL_PRIMITIVE_LITERAL = Generalization(general=PRIMITIVE_LITERAL, specific=alf_BOOLEAN_LITERAL)
gen_alf_NUMBER_LITERAL_PRIMITIVE_LITERAL = Generalization(general=PRIMITIVE_LITERAL, specific=alf_NUMBER_LITERAL)
gen_alf_INTEGER_LITERAL_NUMBER_LITERAL = Generalization(general=NUMBER_LITERAL, specific=alf_INTEGER_LITERAL)
gen_alf_UNLIMITED_NATURAL_NUMBER_LITERAL = Generalization(general=NUMBER_LITERAL, specific=alf_UNLIMITED_NATURAL)
gen_alf_STRING_LITERAL_PRIMITIVE_LITERAL = Generalization(general=PRIMITIVE_LITERAL, specific=alf_STRING_LITERAL)
gen_alf_TaggedValueList_TaggedValues = Generalization(general=TaggedValues, specific=alf_TaggedValueList)
gen_alf_ColonQualifiedNameCompletionOfImportReference_ImportReferenceQualifiedNameCompletion = Generalization(general=ImportReferenceQualifiedNameCompletion, specific=alf_ColonQualifiedNameCompletionOfImportReference)
gen_alf_PackageDefinition_NamespaceDefinition = Generalization(general=NamespaceDefinition, specific=alf_PackageDefinition)
gen_alf_PackageDefinitionOrStub_PackagedElementDefinition = Generalization(general=PackagedElementDefinition, specific=alf_PackageDefinitionOrStub)
gen_alf_ClassifierDefinition_NamespaceDefinition = Generalization(general=NamespaceDefinition, specific=alf_ClassifierDefinition)
gen_alf_ClassifierDefinitionOrStub_PackagedElementDefinition = Generalization(general=PackagedElementDefinition, specific=alf_ClassifierDefinitionOrStub)
gen_alf_ClassifierDefinitionOrStub_ClassMemberDefinition = Generalization(general=ClassMemberDefinition, specific=alf_ClassifierDefinitionOrStub)
gen_alf_ClassDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_ClassDefinition)
gen_alf_ClassDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_ClassDefinitionOrStub)
gen_alf_ActiveClassDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_ActiveClassDefinitionOrStub)
gen_alf_ClassMemberDefinition_ActiveClassMemberDefinition = Generalization(general=ActiveClassMemberDefinition, specific=alf_ClassMemberDefinition)
gen_alf_ActiveClassDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_ActiveClassDefinition)
gen_alf_DataTypeDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_DataTypeDefinition)
gen_alf_DataTypeDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_DataTypeDefinitionOrStub)
gen_alf_AssociationDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_AssociationDefinition)
gen_alf_AssociationDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_AssociationDefinitionOrStub)
gen_alf_EnumerationDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_EnumerationDefinitionOrStub)
gen_alf_EnumerationDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_EnumerationDefinition)
gen_alf_SignalDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_SignalDefinition)
gen_alf_SignalDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_SignalDefinitionOrStub)
gen_alf_ActivityDefinition_ClassifierDefinition = Generalization(general=ClassifierDefinition, specific=alf_ActivityDefinition)
gen_alf_ActivityDefinitionOrStub_ClassifierDefinitionOrStub = Generalization(general=ClassifierDefinitionOrStub, specific=alf_ActivityDefinitionOrStub)
gen_alf_AttributeDefinition_FeatureDefinitionOrStub = Generalization(general=FeatureDefinitionOrStub, specific=alf_AttributeDefinition)
gen_alf_FeatureDefinitionOrStub_ClassMemberDefinition = Generalization(general=ClassMemberDefinition, specific=alf_FeatureDefinitionOrStub)
gen_alf_ActiveFeatureDefinitionOrStub_ActiveClassMemberDefinition = Generalization(general=ActiveClassMemberDefinition, specific=alf_ActiveFeatureDefinitionOrStub)
gen_alf_OperationDefinitionOrStub_FeatureDefinitionOrStub = Generalization(general=FeatureDefinitionOrStub, specific=alf_OperationDefinitionOrStub)
gen_alf_ReceptionDefinition_ActiveFeatureDefinitionOrStub = Generalization(general=ActiveFeatureDefinitionOrStub, specific=alf_ReceptionDefinition)
gen_alf_OperationDeclaration_OperationDefinitionOrStub = Generalization(general=OperationDefinitionOrStub, specific=alf_OperationDeclaration)
gen_alf_NameBinding_UnqualifiedName = Generalization(general=UnqualifiedName, specific=alf_NameBinding)
gen_alf_SignalReceptionDefinitionOrStub_ActiveFeatureDefinitionOrStub = Generalization(general=ActiveFeatureDefinitionOrStub, specific=alf_SignalReceptionDefinitionOrStub)
gen_alf_NamedTemplateBinding_TemplateBinding = Generalization(general=TemplateBinding, specific=alf_NamedTemplateBinding)
gen_alf_Expression_InitializationExpression = Generalization(general=InitializationExpression, specific=alf_Expression)
gen_alf_PositionalTemplateBinding_TemplateBinding = Generalization(general=TemplateBinding, specific=alf_PositionalTemplateBinding)
gen_alf_ThisExpression_BaseExpression = Generalization(general=BaseExpression, specific=alf_ThisExpression)
gen_alf_LiteralExpression_BaseExpression = Generalization(general=BaseExpression, specific=alf_LiteralExpression)
gen_alf_SuperInvocationExpression_BaseExpression = Generalization(general=BaseExpression, specific=alf_SuperInvocationExpression)
gen_alf_InstanceCreationOrSequenceConstructionExpression_BaseExpression = Generalization(general=BaseExpression, specific=alf_InstanceCreationOrSequenceConstructionExpression)
gen_alf_SequenceAnyExpression_BaseExpression = Generalization(general=BaseExpression, specific=alf_SequenceAnyExpression)
gen_alf_SequenceInitializationExpression_InitializationExpression = Generalization(general=InitializationExpression, specific=alf_SequenceInitializationExpression)
gen_alf_PrefixExpression_NonPostfixNonCastUnaryExpression = Generalization(general=NonPostfixNonCastUnaryExpression, specific=alf_PrefixExpression)
gen_alf_PostfixOrCastExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=alf_PostfixOrCastExpression)
gen_alf_PostfixOrCastExpression_CastCompletion = Generalization(general=CastCompletion, specific=alf_PostfixOrCastExpression)
gen_alf_NonPostfixNonCastUnaryExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=alf_NonPostfixNonCastUnaryExpression)
gen_alf_NonPostfixNonCastUnaryExpression_NonNameUnaryExpression = Generalization(general=NonNameUnaryExpression, specific=alf_NonPostfixNonCastUnaryExpression)
gen_alf_BooleanNegationExpression_NonPostfixNonCastUnaryExpression = Generalization(general=NonPostfixNonCastUnaryExpression, specific=alf_BooleanNegationExpression)
gen_alf_NonNamePostfixOrCastExpression_NonNameUnaryExpression = Generalization(general=NonNameUnaryExpression, specific=alf_NonNamePostfixOrCastExpression)
gen_alf_NumericUnaryExpression_NonPostfixNonCastUnaryExpression = Generalization(general=NonPostfixNonCastUnaryExpression, specific=alf_NumericUnaryExpression)
gen_alf_IsolationExpression_NonPostfixNonCastUnaryExpression = Generalization(general=NonPostfixNonCastUnaryExpression, specific=alf_IsolationExpression)
gen_alf_IsolationExpression_CastCompletion = Generalization(general=CastCompletion, specific=alf_IsolationExpression)
gen_alf_BooleanNegationExpression_CastCompletion = Generalization(general=CastCompletion, specific=alf_BooleanNegationExpression)
gen_alf_BitStringComplementExpression_NonPostfixNonCastUnaryExpression = Generalization(general=NonPostfixNonCastUnaryExpression, specific=alf_BitStringComplementExpression)
gen_alf_BitStringComplementExpression_CastCompletion = Generalization(general=CastCompletion, specific=alf_BitStringComplementExpression)
gen_alf_ConditionalExpressionCompletion_ExpressionCompletion = Generalization(general=ExpressionCompletion, specific=alf_ConditionalExpressionCompletion)
gen_alf_AssignmentExpressionCompletion_ExpressionCompletion = Generalization(general=ExpressionCompletion, specific=alf_AssignmentExpressionCompletion)
gen_alf_InLineStatement_Statement = Generalization(general=Statement, specific=alf_InLineStatement)
gen_alf_AnnotatedStatement_Statement = Generalization(general=Statement, specific=alf_AnnotatedStatement)
gen_alf_BlockStatement_Statement = Generalization(general=Statement, specific=alf_BlockStatement)
gen_alf_EmptyStatement_Statement = Generalization(general=Statement, specific=alf_EmptyStatement)
gen_alf_LocalNameDeclarationOrExpressionStatement_Statement = Generalization(general=Statement, specific=alf_LocalNameDeclarationOrExpressionStatement)
gen_alf_LocalNameDeclarationStatement_Statement = Generalization(general=Statement, specific=alf_LocalNameDeclarationStatement)
gen_alf_InstanceInitializationExpression_InitializationExpression = Generalization(general=InitializationExpression, specific=alf_InstanceInitializationExpression)
gen_alf_IfStatement_Statement = Generalization(general=Statement, specific=alf_IfStatement)
gen_alf_SwitchStatement_Statement = Generalization(general=Statement, specific=alf_SwitchStatement)
gen_alf_WhileStatement_Statement = Generalization(general=Statement, specific=alf_WhileStatement)
gen_alf_DoStatement_Statement = Generalization(general=Statement, specific=alf_DoStatement)
gen_alf_ForStatement_Statement = Generalization(general=Statement, specific=alf_ForStatement)
gen_alf_BreakStatement_Statement = Generalization(general=Statement, specific=alf_BreakStatement)
gen_alf_ReturnStatement_Statement = Generalization(general=Statement, specific=alf_ReturnStatement)
gen_alf_AcceptStatement_Statement = Generalization(general=Statement, specific=alf_AcceptStatement)
gen_alf_QualifiedNameList_TaggedValues = Generalization(general=TaggedValues, specific=alf_QualifiedNameList)
gen_alf_ClassifyStatement_Statement = Generalization(general=Statement, specific=alf_ClassifyStatement)

# Domain Model
domain_model = DomainModel(
    name="alf",
    types={alf_StereotypeAnnotations, alf_NamespaceDefinition, alf_BOOLEAN_LITERAL, PRIMITIVE_LITERAL, alf_NUMBER_LITERAL, alf_INTEGER_LITERAL, NUMBER_LITERAL, alf_UNLIMITED_NATURAL, alf_STRING_LITERAL, alf_StereotypeAnnotation, alf_UnitDefinition, alf_NamespaceDeclaration, alf_ImportDeclaration, alf_PRIMITIVE_LITERAL, alf_Name, alf_ImportReference, alf_QualifiedName, alf_TaggedValues, alf_TaggedValueList, TaggedValues, alf_TaggedValue, alf_ColonQualifiedNameCompletionOfImportReference, ImportReferenceQualifiedNameCompletion, alf_VisibilityIndicator, alf_ImportReferenceQualifiedNameCompletion, alf_AliasDefinition, alf_PackagedElement, alf_PackageDeclaration, alf_PackageDefinition, NamespaceDefinition, alf_PackageBody, alf_ClassifierTemplateParameter, alf_PackageDefinitionOrStub, PackagedElementDefinition, alf_QualifiedNameList, alf_PackagedElementDefinition, alf_ClassifierDefinition, alf_ClassifierDefinitionOrStub, ClassMemberDefinition, alf_ClassifierSignature, alf_TemplateParameters, alf_SpecializationClause, alf_ClassMember, alf_ClassMemberDefinition, alf_ClassDeclaration, ActiveClassMemberDefinition, alf_ClassDefinition, ClassifierDefinition, alf_ClassBody, alf_ClassDefinitionOrStub, ClassifierDefinitionOrStub, alf_ActiveClassMember, alf_BehaviorClause, alf_Block, alf_ActiveClassDeclaration, alf_ActiveClassDefinition, alf_ActiveClassBody, alf_ActiveClassDefinitionOrStub, alf_DataTypeDefinition, alf_StructuredBody, alf_DataTypeDefinitionOrStub, alf_ActiveClassMemberDefinition, alf_DataTypeDeclaration, alf_AssociationDeclaration, alf_AssociationDefinition, alf_AssociationDefinitionOrStub, alf_StructuredMember, alf_PropertyDefinition, alf_EnumerationDefinitionOrStub, alf_EnumerationLiteralName, alf_SignalDeclaration, alf_EnumerationDeclaration, alf_EnumerationDefinition, alf_EnumerationBody, alf_ActivityDeclaration, alf_FormalParameters, alf_SignalDefinition, alf_FormalParameterList, alf_SignalDefinitionOrStub, alf_FormalParameter, alf_TypePart, alf_ActivityDefinition, alf_ActivityDefinitionOrStub, alf_AttributeDefinition, FeatureDefinitionOrStub, alf_AttributeInitializer, alf_InitializationExpression, alf_FeatureDefinitionOrStub, alf_ActiveFeatureDefinitionOrStub, alf_PropertyDeclaration, alf_UnlimitedNaturalLiteral, alf_TypeName, alf_Multiplicity, alf_MultiplicityRange, alf_OperationDefinitionOrStub, alf_ReceptionDefinition, ActiveFeatureDefinitionOrStub, alf_SignalReceptionDeclaration, alf_OperationDeclaration, OperationDefinitionOrStub, alf_RedefinitionClause, alf_NameBinding, UnqualifiedName, alf_TemplateBinding, alf_SignalReceptionDefinitionOrStub, alf_UnqualifiedName, alf_ColonQualifiedNameCompletion, alf_NamedTemplateBinding, alf_TemplateParameterSubstitution, alf_Expression, InitializationExpression, alf_QualifiedNameWithoutBinding, alf_ColonQualifiedNameCompletionWithoutBinding, alf_PositionalTemplateBinding, TemplateBinding, alf_PrimaryToExpressionCompletion, alf_PostfixExpressionCompletion, alf_PrimaryExpression, alf_UnaryExpression, alf_ExpressionCompletion, alf_NonNameExpression, alf_NonNameUnaryExpression, alf_NameToExpressionCompletion, alf_NameToPrimaryExpression, alf_SequenceConstructionExpressionCompletion, alf_BehaviorInvocation, alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index, alf_Feature, alf_NameOrPrimaryExpression, alf_BaseExpression, alf_ParenthesizedExpression, alf_PrimaryExpressionCompletion, alf_LinkOperationCompletion, alf_ClassExtentExpressionCompletion, alf_ThisExpression, alf_Tuple, alf_FeatureInvocation, alf_SequenceOperationOrReductionOrExpansion, alf_Index, alf_LiteralExpression, BaseExpression, alf_NamedTupleExpressionList, alf_PositionalTupleExpressionList, alf_PositionalTupleExpressionListCompletion, alf_NamedExpression, alf_LinkOperationTuple, alf_SuperInvocationExpression, alf_IndexedNamedExpressionListCompletion, alf_InstanceCreationOrSequenceConstructionExpression, alf_IndexedNamedExpression, alf_SequenceAnyExpression, alf_SequenceElements, alf_SequenceElementListCompletion, alf_SequenceInitializationExpression, alf_SequenceElement, alf_MultiplicityIndicator, alf_EObject, alf_PrefixExpression, NonPostfixNonCastUnaryExpression, alf_PostfixOrCastExpression, UnaryExpression, CastCompletion, alf_NonNamePostfixOrCastExpression, alf_PostfixOperation, alf_NonPostfixNonCastUnaryExpression, alf_BooleanNegationExpression, NonNameUnaryExpression, alf_NumericUnaryExpression, alf_CastCompletion, alf_IsolationExpression, alf_MultiplicativeExpression, alf_MultiplicativeExpressionCompletion, alf_BitStringComplementExpression, alf_AdditiveExpression, alf_AdditiveExpressionCompletion, alf_ShiftExpression, alf_RelationalExpression, alf_RelationalExpressionCompletion, alf_ShiftExpressionCompletion, alf_ClassificationExpressionCompletion, alf_EqualityExpression, alf_EqualityExpressionCompletion, alf_ClassificationExpression, alf_AndExpression, alf_AndExpressionCompletion, alf_ExclusiveOrExpression, alf_ExclusiveOrExpressionCompletion, alf_InclusiveOrExpression, alf_InclusiveOrExpressionCompletion, alf_ConditionalAndExpression, alf_ConditionalAndExpressionCompletion, alf_ConditionalOrExpressionCompletion, alf_ConditionalExpression, alf_ConditionalExpressionCompletion, ExpressionCompletion, alf_ConditionalOrExpression, alf_StatementSequence, alf_DocumentedStatement, alf_Statement, alf_AssignmentExpressionCompletion, alf_Annotation, alf_NameList, alf_InLineStatement, alf_AnnotatedStatement, Statement, alf_Annotations, alf_BlockStatement, alf_EmptyStatement, alf_LocalNameDeclarationOrExpressionStatement, alf_LocalNameDeclarationStatementCompletion, alf_LocalNameDeclarationStatement, alf_InstanceInitializationExpression, alf_IfStatement, alf_SequentialClauses, alf_FinalClause, alf_ConcurrentClauses, alf_NonFinalClause, alf_SwitchStatement, alf_SwitchClause, alf_SwitchDefaultClause, alf_SwitchCase, alf_NonEmptyStatementSequence, alf_WhileStatement, alf_DoStatement, alf_ForStatement, alf_ForControl, alf_BreakStatement, alf_ReturnStatement, alf_AcceptStatement, alf_LoopVariableDefinition, alf_CompoundAcceptStatementCompletion, alf_AcceptBlock, alf_AcceptClause, alf_SimpleAcceptStatementCompletion, alf_ClassificationClause, alf_ClassificationFromClause, alf_ClassificationToClause, alf_ReclassifyAllClause, alf_ClassifyStatement, ImportVisibilityIndicator, ParameterDirection, LinkOperation, AffixOperator, NumericUnaryOperator, AdditiveOperator, MultiplicativeOperator, ShiftOperator, ClassificationOperator, RelationalOperator, EqualityOperator, AssignmentOperator},
    associations={stereotypeAnnotations3, namesapceDefinition5, namespaceDeclaration0, importDeclarations1, taggedValue13, name14, value16, qualifiedName18, importReference21, annotation7, stereotypeName9, taggedValues11, name30, alias32, alias35, name23, completion26, alias28, declaration44, body46, packagedElement49, stereotypeAnnotations51, name38, declaration40, body42, classifierTemplateParameter62, name64, qualifiedName67, qualifiedNameList70, packagedElementDefinition54, name56, templateParameters58, specializationClause60, classBody80, classMember83, stereotypeAnnotations85, visibilityIndicator88, classMemberDefinition90, classifierSignature72, classDeclaration74, classBody76, classDeclaration78, activeClassDeclaration98, activeClassBody100, activeClassMember103, behaviorClasue105, block107, classifierSignature92, activeClassDeclaration94, activeClassBody96, classifierSignature120, dataTypeDeclaration122, structureBody124, dataTypeDeclaration126, structureBody128, name109, stereotypeAnnotations112, visibilityIndicator115, activeClassMemberDefinition118, classifierSignature138, associationDeclaration140, structuredBody142, associationDeclaration145, structuredMember131, streotypeAnnotations133, propertyDefinition136, enumerationDeclaration159, enumerationBody161, enumerationLiteralName164, name166, structuredBody147, name150, specializationClause152, enumerationClause155, enumerationBody157, signalDeclaration176, structuredBody178, name181, templateParameters183, formalParameters186, classifierSignature169, signalDeclaration171, structuredBody173, formalParameterList200, formalParameter202, stereotypeAnnotations204, typePart188, activityDeclaration190, block192, activityDeclaration195, block197, propertyDeclaration215, attributeInitializer217, initializationExpression219, name221, name207, typePart210, propertyDeclaration213, multiplicityRange234, lower236, upper238, integer240, typePart224, typeName227, multiplicity229, qualifiedName231, qualifiedNameList256, receptionName259, signalName261, name243, formalParameters245, typePart248, redefinitionClause251, block253, nameCompletion273, namedBindings275, name277, templateBinding280, specializationClause263, signalReceptionOrDeclaration266, structuredBody268, unqualified271, templateParameterSubstitution291, name292, qualifiedName295, unqualified282, nameCompletion284, names286, qualifiedName289, primaryToExpressionCompletion306, postFixExpressionCompletion308, expressionCompletion310, expression313, unaryExpression298, expressionCompletion299, nonNameUnaryExpression301, expressionCompletion302, nameToPrimary305, sequenceConstructionCompletion327, behaviorInvocation329, content331, feature333, nameOrPrimaryExpression316, baseExpression317, parenthesizedExpression319, primaryExpressionCompletion321, linkOperationCompletion323, classExtentExpressionCompletion325, nameToPrimaryExpression346, tuple349, expression350, name353, featureInvocation335, sequenceOperationOrReductionOrExpansion337, index339, expression341, potentiallyAmbiguousQualifiedName343, namedExpression365, name367, expression370, tuple373, namedTupleExpressionList356, positionalTupleExpressionList358, expression360, expression363, tuple389, linkOperationTuple392, tuple376, name394, index397, qualifiedName379, indexNamedExpressionListCompletion400, tuple381, qualifiedName384, sequenceConstructionExpressionCompletion386, nameToExpressionCompletion411, positionalTupleExpressionList414, expression417, indexedNamedExpression420, name422, index425, expression428, primaryToExpressionCompletion402, sequenceConstructionExpressionCompletion431, positionalTupleExpressionListCompletion405, indexedNamedExpressionListCompletion408, sequenceElements435, expression1437, expression2440, sequenceElementListCompletion443, sequenceInitializationExpression445, sequenceElement447, sequenceElements455, multiplicityIndicator433, expression458, qualifiedName461, tuple463, templateBinding466, name469, expression449, expression472, sequenceInitializationExpression452, primaryExpression480, nonNamePostfixOrCastExpression482, nameOrPrimaryExpression483, postFixExpressionCompletion486, primaryExpressionCompletion475, postfixOperation478, castCompletion489, potentiallyAmbiguousQualifiedName491, postifixExpressionCompletion494, nameToExpressionCompletion497, postfixExpressionCompletion500, nonNameExpression503, baseExpression506, unaryExpression513, unaryExpression515, unaryExpression517, multiplicativeExpressionCompletion519, unaryExpression509, unaryExpression511, unaryExpression524, additiveExpressionCompletion526, multiplicativeExpressionCompletion528, multiplicativeExpression531, unaryExpression534, unaryExpression521, additiveExpression541, unaryExpression544, relationalExpressionCompletion546, shiftExpressionCompletion548, shiftExpression551, shiftExpressionCompletion536, additiveExpressionCompletion538, classificationExpressionCompletion556, relationalExpressionCompletion558, name561, unaryExpression564, classificationExpressionCompletion566, unaryExpression554, unaryExpression574, andExpressionCompletion576, equalityExpressionCompletion578, equalityExpression581, unaryExpression584, exclusiveOrExpressionCompletion586, classificationExpressionCompletion569, classificationExpression571, unaryExpression594, inclusiveOrExpressionCompletion596, exclusiveOrExpressionCompletion598, exclusiveOrExpression601, unaryExpression604, conditionalAndExpressionCompletion606, andExpressionCompletion588, andExpression591, conditionalOrExpressionCompletion616, conditionalAndExpressionCompletion618, conditionalAndExpression621, unaryExpression624, conditionalExpressionCompletion626, conditionalOrExpressionCompletion628, inclusiveOrExpressionCompletion608, inclusiveOrExpression611, unaryExpression614, documentStatement634, statement635, conditionalExpression631, statement641, annotation644, nameList646, name648, name651, statementSequence637, annotations640, potentiallyAmbiguousName655, block653, multiplicaityIndicator657, name660, localNameDeclarationCompletion663, nameToExpressionCompletion665, nonNameExpression668, name671, typeName673, multiplicityIndicator676, initializationExpression682, tuple685, sequentialClauses687, finalClause688, concurrentClauses690, nonFinalClause692, expression694, localNameDeclarationCompletion679, block700, expression703, switchClause705, defaultClause707, switchCase709, statementSequence711, expression713, block697, statement719, expression722, block724, block727, expression729, forControl732, block733, statementSequence716, name738, expression1741, expression2744, typeName747, expression3750, expression753, loopVariableDefinition736, compoundCompletion758, block760, acceptBlock763, acceptClause765, block768, name771, qualifiedNameList774, acceptClause755, simpleCompletion756, classificationClause779, classificationFromClause781, classificationToClause783, reclassifyAllClause785, qualifiedNameList787, qualifiedNameList790, expression777, qualifiedName793},
    generalizations={gen_alf_BOOLEAN_LITERAL_PRIMITIVE_LITERAL, gen_alf_NUMBER_LITERAL_PRIMITIVE_LITERAL, gen_alf_INTEGER_LITERAL_NUMBER_LITERAL, gen_alf_UNLIMITED_NATURAL_NUMBER_LITERAL, gen_alf_STRING_LITERAL_PRIMITIVE_LITERAL, gen_alf_TaggedValueList_TaggedValues, gen_alf_ColonQualifiedNameCompletionOfImportReference_ImportReferenceQualifiedNameCompletion, gen_alf_PackageDefinition_NamespaceDefinition, gen_alf_PackageDefinitionOrStub_PackagedElementDefinition, gen_alf_ClassifierDefinition_NamespaceDefinition, gen_alf_ClassifierDefinitionOrStub_PackagedElementDefinition, gen_alf_ClassifierDefinitionOrStub_ClassMemberDefinition, gen_alf_ClassDefinition_ClassifierDefinition, gen_alf_ClassDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_ActiveClassDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_ClassMemberDefinition_ActiveClassMemberDefinition, gen_alf_ActiveClassDefinition_ClassifierDefinition, gen_alf_DataTypeDefinition_ClassifierDefinition, gen_alf_DataTypeDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_AssociationDefinition_ClassifierDefinition, gen_alf_AssociationDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_EnumerationDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_EnumerationDefinition_ClassifierDefinition, gen_alf_SignalDefinition_ClassifierDefinition, gen_alf_SignalDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_ActivityDefinition_ClassifierDefinition, gen_alf_ActivityDefinitionOrStub_ClassifierDefinitionOrStub, gen_alf_AttributeDefinition_FeatureDefinitionOrStub, gen_alf_FeatureDefinitionOrStub_ClassMemberDefinition, gen_alf_ActiveFeatureDefinitionOrStub_ActiveClassMemberDefinition, gen_alf_OperationDefinitionOrStub_FeatureDefinitionOrStub, gen_alf_ReceptionDefinition_ActiveFeatureDefinitionOrStub, gen_alf_OperationDeclaration_OperationDefinitionOrStub, gen_alf_NameBinding_UnqualifiedName, gen_alf_SignalReceptionDefinitionOrStub_ActiveFeatureDefinitionOrStub, gen_alf_NamedTemplateBinding_TemplateBinding, gen_alf_Expression_InitializationExpression, gen_alf_PositionalTemplateBinding_TemplateBinding, gen_alf_ThisExpression_BaseExpression, gen_alf_LiteralExpression_BaseExpression, gen_alf_SuperInvocationExpression_BaseExpression, gen_alf_InstanceCreationOrSequenceConstructionExpression_BaseExpression, gen_alf_SequenceAnyExpression_BaseExpression, gen_alf_SequenceInitializationExpression_InitializationExpression, gen_alf_PrefixExpression_NonPostfixNonCastUnaryExpression, gen_alf_PostfixOrCastExpression_UnaryExpression, gen_alf_PostfixOrCastExpression_CastCompletion, gen_alf_NonPostfixNonCastUnaryExpression_UnaryExpression, gen_alf_NonPostfixNonCastUnaryExpression_NonNameUnaryExpression, gen_alf_BooleanNegationExpression_NonPostfixNonCastUnaryExpression, gen_alf_NonNamePostfixOrCastExpression_NonNameUnaryExpression, gen_alf_NumericUnaryExpression_NonPostfixNonCastUnaryExpression, gen_alf_IsolationExpression_NonPostfixNonCastUnaryExpression, gen_alf_IsolationExpression_CastCompletion, gen_alf_BooleanNegationExpression_CastCompletion, gen_alf_BitStringComplementExpression_NonPostfixNonCastUnaryExpression, gen_alf_BitStringComplementExpression_CastCompletion, gen_alf_ConditionalExpressionCompletion_ExpressionCompletion, gen_alf_AssignmentExpressionCompletion_ExpressionCompletion, gen_alf_InLineStatement_Statement, gen_alf_AnnotatedStatement_Statement, gen_alf_BlockStatement_Statement, gen_alf_EmptyStatement_Statement, gen_alf_LocalNameDeclarationOrExpressionStatement_Statement, gen_alf_LocalNameDeclarationStatement_Statement, gen_alf_InstanceInitializationExpression_InitializationExpression, gen_alf_IfStatement_Statement, gen_alf_SwitchStatement_Statement, gen_alf_WhileStatement_Statement, gen_alf_DoStatement_Statement, gen_alf_ForStatement_Statement, gen_alf_BreakStatement_Statement, gen_alf_ReturnStatement_Statement, gen_alf_AcceptStatement_Statement, gen_alf_QualifiedNameList_TaggedValues, gen_alf_ClassifyStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)