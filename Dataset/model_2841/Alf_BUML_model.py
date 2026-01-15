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
ParameterDirection: Enumeration = Enumeration(
    name="ParameterDirection",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

BooleanValue: Enumeration = Enumeration(
    name="BooleanValue",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

LinkOperationKind: Enumeration = Enumeration(
    name="LinkOperationKind",
    literals={
            EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="DESTROY"),
			EnumerationLiteral(name="CLEAR"),
			EnumerationLiteral(name="DESTROY_OBJECT")
    }
)

ForAllOrExistsOrOneOperator: Enumeration = Enumeration(
    name="ForAllOrExistsOrOneOperator",
    literals={
            EnumerationLiteral(name="FORALL"),
			EnumerationLiteral(name="EXISTS"),
			EnumerationLiteral(name="ONE")
    }
)

SelectOrRejectOperator: Enumeration = Enumeration(
    name="SelectOrRejectOperator",
    literals={
            EnumerationLiteral(name="SELECT"),
			EnumerationLiteral(name="REJECT")
    }
)

CollectOrIterateOperator: Enumeration = Enumeration(
    name="CollectOrIterateOperator",
    literals={
            EnumerationLiteral(name="COLLECT"),
			EnumerationLiteral(name="ITERATE")
    }
)

AnnotationKind: Enumeration = Enumeration(
    name="AnnotationKind",
    literals={
            EnumerationLiteral(name="ISOLATED"),
			EnumerationLiteral(name="DETERMINED"),
			EnumerationLiteral(name="ASSURED"),
			EnumerationLiteral(name="PARALLEL")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="PLUSASSIGN"),
			EnumerationLiteral(name="MINUSASSIGN"),
			EnumerationLiteral(name="MULTASSIGN"),
			EnumerationLiteral(name="MODASSIGN"),
			EnumerationLiteral(name="DIVASSIGN"),
			EnumerationLiteral(name="ANDASSIGN"),
			EnumerationLiteral(name="ORASSIGN"),
			EnumerationLiteral(name="XORASSIGN"),
			EnumerationLiteral(name="LSHIFTASSIGN"),
			EnumerationLiteral(name="RSHIFTASSIGN"),
			EnumerationLiteral(name="URSHIFTASSIGN")
    }
)

# Classes
alf_OperationDefinitionOrStub = Class(name="alf::OperationDefinitionOrStub")
alf_OperationDeclaration = Class(name="alf::OperationDeclaration")
alf_Block = Class(name="alf::Block")
alf_FormalParameters = Class(name="alf::FormalParameters")
alf_TypePart = Class(name="alf::TypePart")
alf_RedefinitionClause = Class(name="alf::RedefinitionClause")
alf_FormalParameterList = Class(name="alf::FormalParameterList")
alf_FormalParameter = Class(name="alf::FormalParameter")
alf_TypeName = Class(name="alf::TypeName")
alf_Multiplicity = Class(name="alf::Multiplicity")
alf_MultiplicityRange = Class(name="alf::MultiplicityRange")
alf_Operations = Class(name="alf::Operations")
alf_INTEGER_LITERAL_WITHOUT_SUFFIX = Class(name="alf::INTEGER::LITERAL::WITHOUT::SUFFIX")
NUMBER_LITERAL_WITHOUT_SUFFIX = Class(name="NUMBER::LITERAL::WITHOUT::SUFFIX")
alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX = Class(name="alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX")
alf_QualifiedNameWithBinding = Class(name="alf::QualifiedNameWithBinding")
alf_QualifiedNameList = Class(name="alf::QualifiedNameList")
alf_Test = Class(name="alf::Test")
alf_Expression = Class(name="alf::Expression")
alf_AssignmentCompletion = Class(name="alf::AssignmentCompletion")
alf_Statement = Class(name="alf::Statement")
alf_LITERAL = Class(name="alf::LITERAL")
ValueSpecification = Class(name="ValueSpecification")
alf_SuffixExpression = Class(name="alf::SuffixExpression")
alf_BOOLEAN_LITERAL = Class(name="alf::BOOLEAN::LITERAL")
LITERAL = Class(name="LITERAL")
alf_NUMBER_LITERAL = Class(name="alf::NUMBER::LITERAL")
alf_INTEGER_LITERAL = Class(name="alf::INTEGER::LITERAL")
NUMBER_LITERAL = Class(name="NUMBER::LITERAL")
alf_UNLIMITED_LITERAL = Class(name="alf::UNLIMITED::LITERAL")
alf_STRING_LITERAL = Class(name="alf::STRING::LITERAL")
alf_NameExpression = Class(name="alf::NameExpression")
NonLiteralValueSpecification = Class(name="NonLiteralValueSpecification")
alf_NUMBER_LITERAL_WITHOUT_SUFFIX = Class(name="alf::NUMBER::LITERAL::WITHOUT::SUFFIX")
alf_SequenceConstructionOrAccessCompletion = Class(name="alf::SequenceConstructionOrAccessCompletion")
alf_UnqualifiedName = Class(name="alf::UnqualifiedName")
alf_TemplateBinding = Class(name="alf::TemplateBinding")
alf_NamedTemplateBinding = Class(name="alf::NamedTemplateBinding")
alf_TupleElement = Class(name="alf::TupleElement")
SequenceElement = Class(name="SequenceElement")
alf_ConditionalTestExpression = Class(name="alf::ConditionalTestExpression")
Expression = Class(name="Expression")
alf_ConditionalOrExpression = Class(name="alf::ConditionalOrExpression")
alf_QualifiedNamePath = Class(name="alf::QualifiedNamePath")
alf_Tuple = Class(name="alf::Tuple")
alf_ConditionalAndExpression = Class(name="alf::ConditionalAndExpression")
alf_InclusiveOrExpression = Class(name="alf::InclusiveOrExpression")
alf_ExclusiveOrExpression = Class(name="alf::ExclusiveOrExpression")
alf_AndExpression = Class(name="alf::AndExpression")
alf_EqualityExpression = Class(name="alf::EqualityExpression")
alf_ClassificationExpression = Class(name="alf::ClassificationExpression")
alf_RelationalExpression = Class(name="alf::RelationalExpression")
alf_ShiftExpression = Class(name="alf::ShiftExpression")
alf_AdditiveExpression = Class(name="alf::AdditiveExpression")
alf_MultiplicativeExpression = Class(name="alf::MultiplicativeExpression")
alf_UnaryExpression = Class(name="alf::UnaryExpression")
alf_PrimaryExpression = Class(name="alf::PrimaryExpression")
alf_OperationCallExpression = Class(name="alf::OperationCallExpression")
SuffixExpression = Class(name="SuffixExpression")
alf_OperationCallExpressionWithoutDot = Class(name="alf::OperationCallExpressionWithoutDot")
alf_PropertyCallExpression = Class(name="alf::PropertyCallExpression")
alf_LinkOperationExpression = Class(name="alf::LinkOperationExpression")
alf_LinkOperationTuple = Class(name="alf::LinkOperationTuple")
alf_ValueSpecification = Class(name="alf::ValueSpecification")
alf_SequenceExpansionExpression = Class(name="alf::SequenceExpansionExpression")
alf_SequenceOperationExpression = Class(name="alf::SequenceOperationExpression")
alf_SequenceReductionExpression = Class(name="alf::SequenceReductionExpression")
alf_LinkOperationTupleElement = Class(name="alf::LinkOperationTupleElement")
alf_SelectOrRejectOperation = Class(name="alf::SelectOrRejectOperation")
SequenceExpansionExpression = Class(name="SequenceExpansionExpression")
alf_CollectOrIterateOperation = Class(name="alf::CollectOrIterateOperation")
alf_ForAllOrExistsOrOneOperation = Class(name="alf::ForAllOrExistsOrOneOperation")
alf_InstanceCreationExpression = Class(name="alf::InstanceCreationExpression")
alf_IsUniqueOperation = Class(name="alf::IsUniqueOperation")
alf_NonLiteralValueSpecification = Class(name="alf::NonLiteralValueSpecification")
alf_ParenthesizedExpression = Class(name="alf::ParenthesizedExpression")
alf_NullExpression = Class(name="alf::NullExpression")
alf_ThisExpression = Class(name="alf::ThisExpression")
alf_SuperInvocationExpression = Class(name="alf::SuperInvocationExpression")
alf_SequenceConstructionCompletion = Class(name="alf::SequenceConstructionCompletion")
alf_AccessCompletion = Class(name="alf::AccessCompletion")
alf_PartialSequenceConstructionCompletion = Class(name="alf::PartialSequenceConstructionCompletion")
alf_SequenceConstructionExpression = Class(name="alf::SequenceConstructionExpression")
alf_SequenceElement = Class(name="alf::SequenceElement")
alf_ClassExtentExpression = Class(name="alf::ClassExtentExpression")
alf_StatementSequence = Class(name="alf::StatementSequence")
alf_DocumentedStatement = Class(name="alf::DocumentedStatement")
alf_InlineStatement = Class(name="alf::InlineStatement")
Statement = Class(name="Statement")
alf_AnnotatedStatement = Class(name="alf::AnnotatedStatement")
alf_Annotation = Class(name="alf::Annotation")
alf_BlockStatement = Class(name="alf::BlockStatement")
alf_EmptyStatement = Class(name="alf::EmptyStatement")
alf_LocalNameDeclarationStatement = Class(name="alf::LocalNameDeclarationStatement")
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
alf_LoopVariableDefinition = Class(name="alf::LoopVariableDefinition")
alf_BreakStatement = Class(name="alf::BreakStatement")
alf_ReturnStatement = Class(name="alf::ReturnStatement")
alf_AcceptStatement = Class(name="alf::AcceptStatement")
alf_AcceptClause = Class(name="alf::AcceptClause")
alf_SimpleAcceptStatementCompletion = Class(name="alf::SimpleAcceptStatementCompletion")
alf_CompoundAcceptStatementCompletion = Class(name="alf::CompoundAcceptStatementCompletion")
alf_AcceptBlock = Class(name="alf::AcceptBlock")
alf_ClassifyStatement = Class(name="alf::ClassifyStatement")
alf_ClassificationClause = Class(name="alf::ClassificationClause")
alf_ClassificationFromClause = Class(name="alf::ClassificationFromClause")
alf_ClassificationToClause = Class(name="alf::ClassificationToClause")
alf_ReclassifyAllClause = Class(name="alf::ReclassifyAllClause")
alf_InvocationOrAssignementOrDeclarationStatement = Class(name="alf::InvocationOrAssignementOrDeclarationStatement")
alf_VariableDeclarationCompletion = Class(name="alf::VariableDeclarationCompletion")
alf_SuperInvocationStatement = Class(name="alf::SuperInvocationStatement")
alf_ThisInvocationStatement = Class(name="alf::ThisInvocationStatement")
alf_InstanceCreationInvocationStatement = Class(name="alf::InstanceCreationInvocationStatement")

# alf_OperationDefinitionOrStub class attributes and methods

# alf_OperationDeclaration class attributes and methods
alf_OperationDeclaration_name: Property = Property(name="name", type=StringType)
alf_OperationDeclaration.attributes={alf_OperationDeclaration_name}

# alf_Block class attributes and methods

# alf_FormalParameters class attributes and methods

# alf_TypePart class attributes and methods

# alf_RedefinitionClause class attributes and methods

# alf_FormalParameterList class attributes and methods

# alf_FormalParameter class attributes and methods
alf_FormalParameter_direction: Property = Property(name="direction", type=StringType)
alf_FormalParameter_name: Property = Property(name="name", type=StringType)
alf_FormalParameter.attributes={alf_FormalParameter_direction, alf_FormalParameter_name}

# alf_TypeName class attributes and methods

# alf_Multiplicity class attributes and methods
alf_Multiplicity_ordered: Property = Property(name="ordered", type=BooleanType)
alf_Multiplicity_nonUnique: Property = Property(name="nonUnique", type=BooleanType)
alf_Multiplicity_sequence: Property = Property(name="sequence", type=BooleanType)
alf_Multiplicity.attributes={alf_Multiplicity_nonUnique, alf_Multiplicity_ordered, alf_Multiplicity_sequence}

# alf_MultiplicityRange class attributes and methods

# alf_Operations class attributes and methods
alf_Operations_imports: Property = Property(name="imports", type=StringType)
alf_Operations.attributes={alf_Operations_imports}

# alf_INTEGER_LITERAL_WITHOUT_SUFFIX class attributes and methods

# NUMBER_LITERAL_WITHOUT_SUFFIX class attributes and methods

# alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX class attributes and methods

# alf_QualifiedNameWithBinding class attributes and methods
alf_QualifiedNameWithBinding_id: Property = Property(name="id", type=StringType)
alf_QualifiedNameWithBinding.attributes={alf_QualifiedNameWithBinding_id}

# alf_QualifiedNameList class attributes and methods

# alf_Test class attributes and methods

# alf_Expression class attributes and methods

# alf_AssignmentCompletion class attributes and methods
alf_AssignmentCompletion_op: Property = Property(name="op", type=StringType)
alf_AssignmentCompletion.attributes={alf_AssignmentCompletion_op}

# alf_Statement class attributes and methods

# alf_LITERAL class attributes and methods

# ValueSpecification class attributes and methods

# alf_SuffixExpression class attributes and methods

# alf_BOOLEAN_LITERAL class attributes and methods
alf_BOOLEAN_LITERAL_value: Property = Property(name="value", type=StringType)
alf_BOOLEAN_LITERAL.attributes={alf_BOOLEAN_LITERAL_value}

# LITERAL class attributes and methods

# alf_NUMBER_LITERAL class attributes and methods
alf_NUMBER_LITERAL_value: Property = Property(name="value", type=StringType)
alf_NUMBER_LITERAL.attributes={alf_NUMBER_LITERAL_value}

# alf_INTEGER_LITERAL class attributes and methods

# NUMBER_LITERAL class attributes and methods

# alf_UNLIMITED_LITERAL class attributes and methods

# alf_STRING_LITERAL class attributes and methods
alf_STRING_LITERAL_value: Property = Property(name="value", type=StringType)
alf_STRING_LITERAL.attributes={alf_STRING_LITERAL_value}

# alf_NameExpression class attributes and methods
alf_NameExpression_prefixOp: Property = Property(name="prefixOp", type=StringType)
alf_NameExpression_postfixOp: Property = Property(name="postfixOp", type=StringType)
alf_NameExpression_id: Property = Property(name="id", type=StringType)
alf_NameExpression.attributes={alf_NameExpression_postfixOp, alf_NameExpression_id, alf_NameExpression_prefixOp}

# NonLiteralValueSpecification class attributes and methods

# alf_NUMBER_LITERAL_WITHOUT_SUFFIX class attributes and methods
alf_NUMBER_LITERAL_WITHOUT_SUFFIX_value: Property = Property(name="value", type=StringType)
alf_NUMBER_LITERAL_WITHOUT_SUFFIX.attributes={alf_NUMBER_LITERAL_WITHOUT_SUFFIX_value}

# alf_SequenceConstructionOrAccessCompletion class attributes and methods
alf_SequenceConstructionOrAccessCompletion_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_SequenceConstructionOrAccessCompletion.attributes={alf_SequenceConstructionOrAccessCompletion_multiplicityIndicator}

# alf_UnqualifiedName class attributes and methods
alf_UnqualifiedName_name: Property = Property(name="name", type=StringType)
alf_UnqualifiedName.attributes={alf_UnqualifiedName_name}

# alf_TemplateBinding class attributes and methods

# alf_NamedTemplateBinding class attributes and methods
alf_NamedTemplateBinding_formal: Property = Property(name="formal", type=StringType)
alf_NamedTemplateBinding.attributes={alf_NamedTemplateBinding_formal}

# alf_TupleElement class attributes and methods

# SequenceElement class attributes and methods

# alf_ConditionalTestExpression class attributes and methods

# Expression class attributes and methods

# alf_ConditionalOrExpression class attributes and methods

# alf_QualifiedNamePath class attributes and methods

# alf_Tuple class attributes and methods

# alf_ConditionalAndExpression class attributes and methods

# alf_InclusiveOrExpression class attributes and methods

# alf_ExclusiveOrExpression class attributes and methods

# alf_AndExpression class attributes and methods

# alf_EqualityExpression class attributes and methods
alf_EqualityExpression_op: Property = Property(name="op", type=StringType)
alf_EqualityExpression.attributes={alf_EqualityExpression_op}

# alf_ClassificationExpression class attributes and methods
alf_ClassificationExpression_op: Property = Property(name="op", type=StringType)
alf_ClassificationExpression.attributes={alf_ClassificationExpression_op}

# alf_RelationalExpression class attributes and methods
alf_RelationalExpression_op: Property = Property(name="op", type=StringType)
alf_RelationalExpression.attributes={alf_RelationalExpression_op}

# alf_ShiftExpression class attributes and methods
alf_ShiftExpression_op: Property = Property(name="op", type=StringType)
alf_ShiftExpression.attributes={alf_ShiftExpression_op}

# alf_AdditiveExpression class attributes and methods
alf_AdditiveExpression_op: Property = Property(name="op", type=StringType)
alf_AdditiveExpression.attributes={alf_AdditiveExpression_op}

# alf_MultiplicativeExpression class attributes and methods
alf_MultiplicativeExpression_op: Property = Property(name="op", type=StringType)
alf_MultiplicativeExpression.attributes={alf_MultiplicativeExpression_op}

# alf_UnaryExpression class attributes and methods
alf_UnaryExpression_op: Property = Property(name="op", type=StringType)
alf_UnaryExpression.attributes={alf_UnaryExpression_op}

# alf_PrimaryExpression class attributes and methods

# alf_OperationCallExpression class attributes and methods
alf_OperationCallExpression_operationName: Property = Property(name="operationName", type=StringType)
alf_OperationCallExpression.attributes={alf_OperationCallExpression_operationName}

# SuffixExpression class attributes and methods

# alf_OperationCallExpressionWithoutDot class attributes and methods
alf_OperationCallExpressionWithoutDot_operationName: Property = Property(name="operationName", type=StringType)
alf_OperationCallExpressionWithoutDot.attributes={alf_OperationCallExpressionWithoutDot_operationName}

# alf_PropertyCallExpression class attributes and methods
alf_PropertyCallExpression_propertyName: Property = Property(name="propertyName", type=StringType)
alf_PropertyCallExpression.attributes={alf_PropertyCallExpression_propertyName}

# alf_LinkOperationExpression class attributes and methods
alf_LinkOperationExpression_kind: Property = Property(name="kind", type=StringType)
alf_LinkOperationExpression.attributes={alf_LinkOperationExpression_kind}

# alf_LinkOperationTuple class attributes and methods

# alf_ValueSpecification class attributes and methods

# alf_SequenceExpansionExpression class attributes and methods

# alf_SequenceOperationExpression class attributes and methods
alf_SequenceOperationExpression_operationName: Property = Property(name="operationName", type=StringType)
alf_SequenceOperationExpression.attributes={alf_SequenceOperationExpression_operationName}

# alf_SequenceReductionExpression class attributes and methods
alf_SequenceReductionExpression_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
alf_SequenceReductionExpression.attributes={alf_SequenceReductionExpression_isOrdered}

# alf_LinkOperationTupleElement class attributes and methods
alf_LinkOperationTupleElement_objectOrRole: Property = Property(name="objectOrRole", type=StringType)
alf_LinkOperationTupleElement.attributes={alf_LinkOperationTupleElement_objectOrRole}

# alf_SelectOrRejectOperation class attributes and methods
alf_SelectOrRejectOperation_op: Property = Property(name="op", type=StringType)
alf_SelectOrRejectOperation_expr1: Property = Property(name="expr1", type=StringType)
alf_SelectOrRejectOperation_expr2: Property = Property(name="expr2", type=StringType)
alf_SelectOrRejectOperation_expr3: Property = Property(name="expr3", type=StringType)
alf_SelectOrRejectOperation_expr4: Property = Property(name="expr4", type=StringType)
alf_SelectOrRejectOperation.attributes={alf_SelectOrRejectOperation_expr1, alf_SelectOrRejectOperation_expr3, alf_SelectOrRejectOperation_expr4, alf_SelectOrRejectOperation_expr2, alf_SelectOrRejectOperation_op}

# SequenceExpansionExpression class attributes and methods

# alf_CollectOrIterateOperation class attributes and methods
alf_CollectOrIterateOperation_op: Property = Property(name="op", type=StringType)
alf_CollectOrIterateOperation_expr1: Property = Property(name="expr1", type=StringType)
alf_CollectOrIterateOperation_expr2: Property = Property(name="expr2", type=StringType)
alf_CollectOrIterateOperation_expr3: Property = Property(name="expr3", type=StringType)
alf_CollectOrIterateOperation_expr4: Property = Property(name="expr4", type=StringType)
alf_CollectOrIterateOperation.attributes={alf_CollectOrIterateOperation_op, alf_CollectOrIterateOperation_expr3, alf_CollectOrIterateOperation_expr1, alf_CollectOrIterateOperation_expr2, alf_CollectOrIterateOperation_expr4}

# alf_ForAllOrExistsOrOneOperation class attributes and methods
alf_ForAllOrExistsOrOneOperation_op: Property = Property(name="op", type=StringType)
alf_ForAllOrExistsOrOneOperation_expr1: Property = Property(name="expr1", type=StringType)
alf_ForAllOrExistsOrOneOperation_expr2: Property = Property(name="expr2", type=StringType)
alf_ForAllOrExistsOrOneOperation_expr3: Property = Property(name="expr3", type=StringType)
alf_ForAllOrExistsOrOneOperation_expr4: Property = Property(name="expr4", type=StringType)
alf_ForAllOrExistsOrOneOperation.attributes={alf_ForAllOrExistsOrOneOperation_op, alf_ForAllOrExistsOrOneOperation_expr1, alf_ForAllOrExistsOrOneOperation_expr2, alf_ForAllOrExistsOrOneOperation_expr3, alf_ForAllOrExistsOrOneOperation_expr4}

# alf_InstanceCreationExpression class attributes and methods

# alf_IsUniqueOperation class attributes and methods
alf_IsUniqueOperation_name: Property = Property(name="name", type=StringType)
alf_IsUniqueOperation.attributes={alf_IsUniqueOperation_name}

# alf_NonLiteralValueSpecification class attributes and methods

# alf_ParenthesizedExpression class attributes and methods

# alf_NullExpression class attributes and methods

# alf_ThisExpression class attributes and methods

# alf_SuperInvocationExpression class attributes and methods
alf_SuperInvocationExpression_className: Property = Property(name="className", type=StringType)
alf_SuperInvocationExpression.attributes={alf_SuperInvocationExpression_className}

# alf_SequenceConstructionCompletion class attributes and methods
alf_SequenceConstructionCompletion_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_SequenceConstructionCompletion.attributes={alf_SequenceConstructionCompletion_multiplicityIndicator}

# alf_AccessCompletion class attributes and methods

# alf_PartialSequenceConstructionCompletion class attributes and methods

# alf_SequenceConstructionExpression class attributes and methods

# alf_SequenceElement class attributes and methods

# alf_ClassExtentExpression class attributes and methods

# alf_StatementSequence class attributes and methods

# alf_DocumentedStatement class attributes and methods
alf_DocumentedStatement_comment: Property = Property(name="comment", type=StringType)
alf_DocumentedStatement.attributes={alf_DocumentedStatement_comment}

# alf_InlineStatement class attributes and methods
alf_InlineStatement_langageName: Property = Property(name="langageName", type=StringType)
alf_InlineStatement_body: Property = Property(name="body", type=StringType)
alf_InlineStatement.attributes={alf_InlineStatement_langageName, alf_InlineStatement_body}

# Statement class attributes and methods

# alf_AnnotatedStatement class attributes and methods

# alf_Annotation class attributes and methods
alf_Annotation_kind: Property = Property(name="kind", type=StringType)
alf_Annotation_args: Property = Property(name="args", type=StringType)
alf_Annotation.attributes={alf_Annotation_kind, alf_Annotation_args}

# alf_BlockStatement class attributes and methods

# alf_EmptyStatement class attributes and methods

# alf_LocalNameDeclarationStatement class attributes and methods
alf_LocalNameDeclarationStatement_varName: Property = Property(name="varName", type=StringType)
alf_LocalNameDeclarationStatement_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_LocalNameDeclarationStatement.attributes={alf_LocalNameDeclarationStatement_multiplicityIndicator, alf_LocalNameDeclarationStatement_varName}

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

# alf_LoopVariableDefinition class attributes and methods
alf_LoopVariableDefinition_name: Property = Property(name="name", type=StringType)
alf_LoopVariableDefinition.attributes={alf_LoopVariableDefinition_name}

# alf_BreakStatement class attributes and methods

# alf_ReturnStatement class attributes and methods

# alf_AcceptStatement class attributes and methods

# alf_AcceptClause class attributes and methods
alf_AcceptClause_name: Property = Property(name="name", type=StringType)
alf_AcceptClause.attributes={alf_AcceptClause_name}

# alf_SimpleAcceptStatementCompletion class attributes and methods

# alf_CompoundAcceptStatementCompletion class attributes and methods

# alf_AcceptBlock class attributes and methods

# alf_ClassifyStatement class attributes and methods

# alf_ClassificationClause class attributes and methods

# alf_ClassificationFromClause class attributes and methods

# alf_ClassificationToClause class attributes and methods

# alf_ReclassifyAllClause class attributes and methods

# alf_InvocationOrAssignementOrDeclarationStatement class attributes and methods

# alf_VariableDeclarationCompletion class attributes and methods
alf_VariableDeclarationCompletion_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_VariableDeclarationCompletion_variableName: Property = Property(name="variableName", type=StringType)
alf_VariableDeclarationCompletion.attributes={alf_VariableDeclarationCompletion_multiplicityIndicator, alf_VariableDeclarationCompletion_variableName}

# alf_SuperInvocationStatement class attributes and methods

# alf_ThisInvocationStatement class attributes and methods

# alf_InstanceCreationInvocationStatement class attributes and methods

# Relationships
operations0: BinaryAssociation = BinaryAssociation(
    name="operations0",
    ends={
        Property(name="alf_OperationDefinitionOrStub", type=alf_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Operations", type=alf_OperationDefinitionOrStub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration1: BinaryAssociation = BinaryAssociation(
    name="declaration1",
    ends={
        Property(name="alf_OperationDeclaration", type=alf_OperationDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDefinitionOrStub2", type=alf_OperationDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body3: BinaryAssociation = BinaryAssociation(
    name="body3",
    ends={
        Property(name="alf_Block", type=alf_OperationDefinitionOrStub, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDefinitionOrStub4", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters5: BinaryAssociation = BinaryAssociation(
    name="formalParameters5",
    ends={
        Property(name="alf_FormalParameters", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration6", type=alf_FormalParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType7: BinaryAssociation = BinaryAssociation(
    name="returnType7",
    ends={
        Property(name="alf_TypePart", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration8", type=alf_TypePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinition9: BinaryAssociation = BinaryAssociation(
    name="redefinition9",
    ends={
        Property(name="alf_RedefinitionClause", type=alf_OperationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationDeclaration10", type=alf_RedefinitionClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList11: BinaryAssociation = BinaryAssociation(
    name="formalParameterList11",
    ends={
        Property(name="alf_FormalParameterList", type=alf_FormalParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameters12", type=alf_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameter13: BinaryAssociation = BinaryAssociation(
    name="formalParameter13",
    ends={
        Property(name="alf_FormalParameter", type=alf_FormalParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameterList14", type=alf_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="alf_TypePart17", type=alf_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FormalParameter16", type=alf_TypePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName18: BinaryAssociation = BinaryAssociation(
    name="typeName18",
    ends={
        Property(name="alf_TypeName", type=alf_TypePart, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TypePart19", type=alf_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity20: BinaryAssociation = BinaryAssociation(
    name="multiplicity20",
    ends={
        Property(name="alf_Multiplicity", type=alf_TypePart, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TypePart21", type=alf_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range22: BinaryAssociation = BinaryAssociation(
    name="range22",
    ends={
        Property(name="alf_MultiplicityRange", type=alf_Multiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Multiplicity23", type=alf_MultiplicityRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName29: BinaryAssociation = BinaryAssociation(
    name="qualifiedName29",
    ends={
        Property(name="alf_QualifiedNameWithBinding", type=alf_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TypeName30", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedOperations31: BinaryAssociation = BinaryAssociation(
    name="redefinedOperations31",
    ends={
        Property(name="alf_QualifiedNameList", type=alf_RedefinitionClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RedefinitionClause32", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression33: BinaryAssociation = BinaryAssociation(
    name="expression33",
    ends={
        Property(name="alf_Expression", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test", type=alf_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignExpression34: BinaryAssociation = BinaryAssociation(
    name="assignExpression34",
    ends={
        Property(name="alf_AssignmentCompletion", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test35", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements36: BinaryAssociation = BinaryAssociation(
    name="statements36",
    ends={
        Property(name="alf_Statement", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test37", type=alf_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block38: BinaryAssociation = BinaryAssociation(
    name="block38",
    ends={
        Property(name="alf_Block40", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test39", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix41: BinaryAssociation = BinaryAssociation(
    name="suffix41",
    ends={
        Property(name="alf_SuffixExpression", type=alf_LITERAL, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LITERAL", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lower24: BinaryAssociation = BinaryAssociation(
    name="lower24",
    ends={
        Property(name="alf_NUMBER_LITERAL_WITHOUT_SUFFIX", type=alf_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicityRange25", type=alf_NUMBER_LITERAL_WITHOUT_SUFFIX, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upper26: BinaryAssociation = BinaryAssociation(
    name="upper26",
    ends={
        Property(name="alf_NUMBER_LITERAL_WITHOUT_SUFFIX28", type=alf_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicityRange27", type=alf_NUMBER_LITERAL_WITHOUT_SUFFIX, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceConstructionCompletion45: BinaryAssociation = BinaryAssociation(
    name="sequenceConstructionCompletion45",
    ends={
        Property(name="alf_SequenceConstructionOrAccessCompletion", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression46", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix47: BinaryAssociation = BinaryAssociation(
    name="suffix47",
    ends={
        Property(name="alf_SuffixExpression49", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression48", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespace50: BinaryAssociation = BinaryAssociation(
    name="namespace50",
    ends={
        Property(name="alf_UnqualifiedName", type=alf_QualifiedNamePath, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNamePath51", type=alf_UnqualifiedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateBinding52: BinaryAssociation = BinaryAssociation(
    name="templateBinding52",
    ends={
        Property(name="alf_TemplateBinding", type=alf_UnqualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnqualifiedName53", type=alf_TemplateBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings54: BinaryAssociation = BinaryAssociation(
    name="bindings54",
    ends={
        Property(name="alf_NamedTemplateBinding", type=alf_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TemplateBinding55", type=alf_NamedTemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actual56: BinaryAssociation = BinaryAssociation(
    name="actual56",
    ends={
        Property(name="alf_QualifiedNameWithBinding58", type=alf_NamedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NamedTemplateBinding57", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binding59: BinaryAssociation = BinaryAssociation(
    name="binding59",
    ends={
        Property(name="alf_TemplateBinding61", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameWithBinding60", type=alf_TemplateBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remaining63: BinaryAssociation = BinaryAssociation(
    name="remaining63",
    ends={
        Property(name="alf_QualifiedNameWithBinding64", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameWithBinding62", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tupleElements65: BinaryAssociation = BinaryAssociation(
    name="tupleElements65",
    ends={
        Property(name="alf_TupleElement", type=alf_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Tuple66", type=alf_TupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument67: BinaryAssociation = BinaryAssociation(
    name="argument67",
    ends={
        Property(name="alf_Expression69", type=alf_TupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TupleElement68", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp70: BinaryAssociation = BinaryAssociation(
    name="exp70",
    ends={
        Property(name="alf_ConditionalOrExpression", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalTestExpression", type=alf_ConditionalOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenTrue72: BinaryAssociation = BinaryAssociation(
    name="whenTrue72",
    ends={
        Property(name="alf_ConditionalTestExpression73", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalTestExpression71", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path42: BinaryAssociation = BinaryAssociation(
    name="path42",
    ends={
        Property(name="alf_QualifiedNamePath", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression", type=alf_QualifiedNamePath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invocationCompletion43: BinaryAssociation = BinaryAssociation(
    name="invocationCompletion43",
    ends={
        Property(name="alf_Tuple", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression44", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp77: BinaryAssociation = BinaryAssociation(
    name="exp77",
    ends={
        Property(name="alf_ConditionalAndExpression", type=alf_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalOrExpression78", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp79: BinaryAssociation = BinaryAssociation(
    name="exp79",
    ends={
        Property(name="alf_InclusiveOrExpression", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalAndExpression80", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp81: BinaryAssociation = BinaryAssociation(
    name="exp81",
    ends={
        Property(name="alf_ExclusiveOrExpression", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InclusiveOrExpression82", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp83: BinaryAssociation = BinaryAssociation(
    name="exp83",
    ends={
        Property(name="alf_AndExpression", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExclusiveOrExpression84", type=alf_AndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp85: BinaryAssociation = BinaryAssociation(
    name="exp85",
    ends={
        Property(name="alf_EqualityExpression", type=alf_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AndExpression86", type=alf_EqualityExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp87: BinaryAssociation = BinaryAssociation(
    name="exp87",
    ends={
        Property(name="alf_ClassificationExpression", type=alf_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EqualityExpression88", type=alf_ClassificationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp89: BinaryAssociation = BinaryAssociation(
    name="exp89",
    ends={
        Property(name="alf_RelationalExpression", type=alf_ClassificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpression90", type=alf_RelationalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenFalse75: BinaryAssociation = BinaryAssociation(
    name="whenFalse75",
    ends={
        Property(name="alf_ConditionalTestExpression76", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalTestExpression74", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left94: BinaryAssociation = BinaryAssociation(
    name="left94",
    ends={
        Property(name="alf_ShiftExpression", type=alf_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpression95", type=alf_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right96: BinaryAssociation = BinaryAssociation(
    name="right96",
    ends={
        Property(name="alf_ShiftExpression98", type=alf_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpression97", type=alf_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp99: BinaryAssociation = BinaryAssociation(
    name="exp99",
    ends={
        Property(name="alf_AdditiveExpression", type=alf_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ShiftExpression100", type=alf_AdditiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp101: BinaryAssociation = BinaryAssociation(
    name="exp101",
    ends={
        Property(name="alf_MultiplicativeExpression", type=alf_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AdditiveExpression102", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp103: BinaryAssociation = BinaryAssociation(
    name="exp103",
    ends={
        Property(name="alf_UnaryExpression", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicativeExpression104", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp105: BinaryAssociation = BinaryAssociation(
    name="exp105",
    ends={
        Property(name="alf_PrimaryExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnaryExpression106", type=alf_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName91: BinaryAssociation = BinaryAssociation(
    name="typeName91",
    ends={
        Property(name="alf_NameExpression93", type=alf_ClassificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpression92", type=alf_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple109: BinaryAssociation = BinaryAssociation(
    name="tuple109",
    ends={
        Property(name="alf_Tuple110", type=alf_OperationCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationCallExpression", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix111: BinaryAssociation = BinaryAssociation(
    name="suffix111",
    ends={
        Property(name="alf_SuffixExpression113", type=alf_OperationCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationCallExpression112", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple114: BinaryAssociation = BinaryAssociation(
    name="tuple114",
    ends={
        Property(name="alf_Tuple115", type=alf_OperationCallExpressionWithoutDot, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationCallExpressionWithoutDot", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix116: BinaryAssociation = BinaryAssociation(
    name="suffix116",
    ends={
        Property(name="alf_SuffixExpression118", type=alf_OperationCallExpressionWithoutDot, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationCallExpressionWithoutDot117", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index119: BinaryAssociation = BinaryAssociation(
    name="index119",
    ends={
        Property(name="alf_Expression120", type=alf_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyCallExpression", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix121: BinaryAssociation = BinaryAssociation(
    name="suffix121",
    ends={
        Property(name="alf_SuffixExpression123", type=alf_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyCallExpression122", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple124: BinaryAssociation = BinaryAssociation(
    name="tuple124",
    ends={
        Property(name="alf_LinkOperationTuple", type=alf_LinkOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationExpression", type=alf_LinkOperationTuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prefix107: BinaryAssociation = BinaryAssociation(
    name="prefix107",
    ends={
        Property(name="alf_ValueSpecification", type=alf_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpression108", type=alf_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkOperationTupleElement125: BinaryAssociation = BinaryAssociation(
    name="linkOperationTupleElement125",
    ends={
        Property(name="alf_LinkOperationTuple126", type=alf_LinkOperationTupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="alf_LinkOperationTupleElement", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1))
    }
)
roleIndex127: BinaryAssociation = BinaryAssociation(
    name="roleIndex127",
    ends={
        Property(name="alf_Expression129", type=alf_LinkOperationTupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTupleElement128", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectValueSpec130: BinaryAssociation = BinaryAssociation(
    name="objectValueSpec130",
    ends={
        Property(name="alf_ValueSpecification132", type=alf_LinkOperationTupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTupleElement131", type=alf_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple133: BinaryAssociation = BinaryAssociation(
    name="tuple133",
    ends={
        Property(name="alf_Tuple134", type=alf_SequenceOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationExpression", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix135: BinaryAssociation = BinaryAssociation(
    name="suffix135",
    ends={
        Property(name="alf_SuffixExpression137", type=alf_SequenceOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationExpression136", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behavior138: BinaryAssociation = BinaryAssociation(
    name="behavior138",
    ends={
        Property(name="alf_QualifiedNameWithBinding139", type=alf_SequenceReductionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceReductionExpression", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix140: BinaryAssociation = BinaryAssociation(
    name="suffix140",
    ends={
        Property(name="alf_SuffixExpression142", type=alf_SequenceReductionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceReductionExpression141", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix143: BinaryAssociation = BinaryAssociation(
    name="suffix143",
    ends={
        Property(name="alf_SuffixExpression144", type=alf_SequenceExpansionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceExpansionExpression", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr145: BinaryAssociation = BinaryAssociation(
    name="expr145",
    ends={
        Property(name="alf_Expression146", type=alf_IsUniqueOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IsUniqueOperation", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expOrTypeCast147: BinaryAssociation = BinaryAssociation(
    name="expOrTypeCast147",
    ends={
        Property(name="alf_Expression148", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
casted149: BinaryAssociation = BinaryAssociation(
    name="casted149",
    ends={
        Property(name="alf_NonLiteralValueSpecification", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression150", type=alf_NonLiteralValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix151: BinaryAssociation = BinaryAssociation(
    name="suffix151",
    ends={
        Property(name="alf_SuffixExpression153", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression152", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix154: BinaryAssociation = BinaryAssociation(
    name="suffix154",
    ends={
        Property(name="alf_SuffixExpression155", type=alf_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisExpression", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationCallWithoutDot156: BinaryAssociation = BinaryAssociation(
    name="operationCallWithoutDot156",
    ends={
        Property(name="alf_OperationCallExpressionWithoutDot157", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationExpression", type=alf_OperationCallExpressionWithoutDot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationCall158: BinaryAssociation = BinaryAssociation(
    name="operationCall158",
    ends={
        Property(name="alf_OperationCallExpression160", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationExpression159", type=alf_OperationCallExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructor161: BinaryAssociation = BinaryAssociation(
    name="constructor161",
    ends={
        Property(name="alf_QualifiedNameWithBinding162", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple163: BinaryAssociation = BinaryAssociation(
    name="tuple163",
    ends={
        Property(name="alf_Tuple165", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression164", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceConstuctionCompletion166: BinaryAssociation = BinaryAssociation(
    name="sequenceConstuctionCompletion166",
    ends={
        Property(name="alf_SequenceConstructionCompletion", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression167", type=alf_SequenceConstructionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix168: BinaryAssociation = BinaryAssociation(
    name="suffix168",
    ends={
        Property(name="alf_SuffixExpression170", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression169", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessCompletion171: BinaryAssociation = BinaryAssociation(
    name="accessCompletion171",
    ends={
        Property(name="alf_AccessCompletion", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionOrAccessCompletion172", type=alf_AccessCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceCompletion173: BinaryAssociation = BinaryAssociation(
    name="sequenceCompletion173",
    ends={
        Property(name="alf_PartialSequenceConstructionCompletion", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionOrAccessCompletion174", type=alf_PartialSequenceConstructionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression175: BinaryAssociation = BinaryAssociation(
    name="expression175",
    ends={
        Property(name="alf_SequenceConstructionExpression", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionOrAccessCompletion176", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessIndex177: BinaryAssociation = BinaryAssociation(
    name="accessIndex177",
    ends={
        Property(name="alf_Expression179", type=alf_AccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AccessCompletion178", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression180: BinaryAssociation = BinaryAssociation(
    name="expression180",
    ends={
        Property(name="alf_SequenceConstructionExpression182", type=alf_PartialSequenceConstructionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PartialSequenceConstructionCompletion181", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression183: BinaryAssociation = BinaryAssociation(
    name="expression183",
    ends={
        Property(name="alf_SequenceConstructionExpression185", type=alf_SequenceConstructionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionCompletion184", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceElement186: BinaryAssociation = BinaryAssociation(
    name="sequenceElement186",
    ends={
        Property(name="alf_SequenceElement", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionExpression187", type=alf_SequenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rangeUpper188: BinaryAssociation = BinaryAssociation(
    name="rangeUpper188",
    ends={
        Property(name="alf_Expression190", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionExpression189", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence191: BinaryAssociation = BinaryAssociation(
    name="sequence191",
    ends={
        Property(name="alf_StatementSequence", type=alf_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Block192", type=alf_StatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements193: BinaryAssociation = BinaryAssociation(
    name="statements193",
    ends={
        Property(name="alf_DocumentedStatement", type=alf_StatementSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StatementSequence194", type=alf_DocumentedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation195: BinaryAssociation = BinaryAssociation(
    name="annotation195",
    ends={
        Property(name="alf_Annotation", type=alf_AnnotatedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AnnotatedStatement", type=alf_Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block196: BinaryAssociation = BinaryAssociation(
    name="block196",
    ends={
        Property(name="alf_Block198", type=alf_AnnotatedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AnnotatedStatement197", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement199: BinaryAssociation = BinaryAssociation(
    name="statement199",
    ends={
        Property(name="alf_Statement201", type=alf_DocumentedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DocumentedStatement200", type=alf_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block202: BinaryAssociation = BinaryAssociation(
    name="block202",
    ends={
        Property(name="alf_Block203", type=alf_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BlockStatement", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type204: BinaryAssociation = BinaryAssociation(
    name="type204",
    ends={
        Property(name="alf_QualifiedNameWithBinding205", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init206: BinaryAssociation = BinaryAssociation(
    name="init206",
    ends={
        Property(name="alf_Expression208", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement207", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequentialClausses209: BinaryAssociation = BinaryAssociation(
    name="sequentialClausses209",
    ends={
        Property(name="alf_SequentialClauses", type=alf_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IfStatement", type=alf_SequentialClauses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalClause210: BinaryAssociation = BinaryAssociation(
    name="finalClause210",
    ends={
        Property(name="alf_FinalClause", type=alf_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IfStatement211", type=alf_FinalClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conccurentClauses212: BinaryAssociation = BinaryAssociation(
    name="conccurentClauses212",
    ends={
        Property(name="alf_ConcurrentClauses", type=alf_SequentialClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequentialClauses213", type=alf_ConcurrentClauses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonFinalClause214: BinaryAssociation = BinaryAssociation(
    name="nonFinalClause214",
    ends={
        Property(name="alf_NonFinalClause", type=alf_ConcurrentClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConcurrentClauses215", type=alf_NonFinalClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition216: BinaryAssociation = BinaryAssociation(
    name="condition216",
    ends={
        Property(name="alf_Expression218", type=alf_NonFinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonFinalClause217", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block219: BinaryAssociation = BinaryAssociation(
    name="block219",
    ends={
        Property(name="alf_Block221", type=alf_NonFinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonFinalClause220", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block222: BinaryAssociation = BinaryAssociation(
    name="block222",
    ends={
        Property(name="alf_Block224", type=alf_FinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FinalClause223", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression225: BinaryAssociation = BinaryAssociation(
    name="expression225",
    ends={
        Property(name="alf_Expression226", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchClause227: BinaryAssociation = BinaryAssociation(
    name="switchClause227",
    ends={
        Property(name="alf_SwitchClause", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement228", type=alf_SwitchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultClause229: BinaryAssociation = BinaryAssociation(
    name="defaultClause229",
    ends={
        Property(name="alf_SwitchDefaultClause", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement230", type=alf_SwitchDefaultClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchCase231: BinaryAssociation = BinaryAssociation(
    name="switchCase231",
    ends={
        Property(name="alf_SwitchCase", type=alf_SwitchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchClause232", type=alf_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementSequence233: BinaryAssociation = BinaryAssociation(
    name="statementSequence233",
    ends={
        Property(name="alf_NonEmptyStatementSequence", type=alf_SwitchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchClause234", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression235: BinaryAssociation = BinaryAssociation(
    name="expression235",
    ends={
        Property(name="alf_Expression237", type=alf_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchCase236", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementSequence238: BinaryAssociation = BinaryAssociation(
    name="statementSequence238",
    ends={
        Property(name="alf_NonEmptyStatementSequence240", type=alf_SwitchDefaultClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchDefaultClause239", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement241: BinaryAssociation = BinaryAssociation(
    name="statement241",
    ends={
        Property(name="alf_DocumentedStatement243", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonEmptyStatementSequence242", type=alf_DocumentedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition244: BinaryAssociation = BinaryAssociation(
    name="condition244",
    ends={
        Property(name="alf_Expression245", type=alf_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_WhileStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block246: BinaryAssociation = BinaryAssociation(
    name="block246",
    ends={
        Property(name="alf_Block248", type=alf_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_WhileStatement247", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block249: BinaryAssociation = BinaryAssociation(
    name="block249",
    ends={
        Property(name="alf_Block250", type=alf_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DoStatement", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition251: BinaryAssociation = BinaryAssociation(
    name="condition251",
    ends={
        Property(name="alf_Expression253", type=alf_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DoStatement252", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
control254: BinaryAssociation = BinaryAssociation(
    name="control254",
    ends={
        Property(name="alf_ForControl", type=alf_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForStatement", type=alf_ForControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block255: BinaryAssociation = BinaryAssociation(
    name="block255",
    ends={
        Property(name="alf_Block257", type=alf_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForStatement256", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopVariableDefinition258: BinaryAssociation = BinaryAssociation(
    name="loopVariableDefinition258",
    ends={
        Property(name="alf_LoopVariableDefinition", type=alf_ForControl, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForControl259", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1260: BinaryAssociation = BinaryAssociation(
    name="expression1260",
    ends={
        Property(name="alf_Expression262", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition261", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2263: BinaryAssociation = BinaryAssociation(
    name="expression2263",
    ends={
        Property(name="alf_Expression265", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition264", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression266: BinaryAssociation = BinaryAssociation(
    name="expression266",
    ends={
        Property(name="alf_Expression267", type=alf_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ReturnStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clause268: BinaryAssociation = BinaryAssociation(
    name="clause268",
    ends={
        Property(name="alf_AcceptClause", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement", type=alf_AcceptClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleAccept269: BinaryAssociation = BinaryAssociation(
    name="simpleAccept269",
    ends={
        Property(name="alf_SimpleAcceptStatementCompletion", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement270", type=alf_SimpleAcceptStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compoundAccept271: BinaryAssociation = BinaryAssociation(
    name="compoundAccept271",
    ends={
        Property(name="alf_CompoundAcceptStatementCompletion", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement272", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block273: BinaryAssociation = BinaryAssociation(
    name="block273",
    ends={
        Property(name="alf_Block275", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_CompoundAcceptStatementCompletion274", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acceptBlock276: BinaryAssociation = BinaryAssociation(
    name="acceptBlock276",
    ends={
        Property(name="alf_AcceptBlock", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_CompoundAcceptStatementCompletion277", type=alf_AcceptBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause278: BinaryAssociation = BinaryAssociation(
    name="clause278",
    ends={
        Property(name="alf_AcceptClause280", type=alf_AcceptBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptBlock279", type=alf_AcceptClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block281: BinaryAssociation = BinaryAssociation(
    name="block281",
    ends={
        Property(name="alf_Block283", type=alf_AcceptBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptBlock282", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList284: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList284",
    ends={
        Property(name="alf_QualifiedNameList286", type=alf_AcceptClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptClause285", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression287: BinaryAssociation = BinaryAssociation(
    name="expression287",
    ends={
        Property(name="alf_Expression288", type=alf_ClassifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifyStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clause289: BinaryAssociation = BinaryAssociation(
    name="clause289",
    ends={
        Property(name="alf_ClassificationClause", type=alf_ClassifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifyStatement290", type=alf_ClassificationClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifyFromClause291: BinaryAssociation = BinaryAssociation(
    name="classifyFromClause291",
    ends={
        Property(name="alf_ClassificationFromClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause292", type=alf_ClassificationFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifyToClause293: BinaryAssociation = BinaryAssociation(
    name="classifyToClause293",
    ends={
        Property(name="alf_ClassificationToClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause294", type=alf_ClassificationToClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reclassyAllClause295: BinaryAssociation = BinaryAssociation(
    name="reclassyAllClause295",
    ends={
        Property(name="alf_ReclassifyAllClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause296", type=alf_ReclassifyAllClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList297: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList297",
    ends={
        Property(name="alf_QualifiedNameList299", type=alf_ClassificationFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationFromClause298", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList300: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList300",
    ends={
        Property(name="alf_QualifiedNameList302", type=alf_ClassificationToClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationToClause301", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName303: BinaryAssociation = BinaryAssociation(
    name="qualifiedName303",
    ends={
        Property(name="alf_QualifiedNameWithBinding305", type=alf_QualifiedNameList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameList304", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typePart_OR_assignedPart_OR_invocationPart306: BinaryAssociation = BinaryAssociation(
    name="typePart_OR_assignedPart_OR_invocationPart306",
    ends={
        Property(name="alf_NameExpression307", type=alf_InvocationOrAssignementOrDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InvocationOrAssignementOrDeclarationStatement", type=alf_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarationCompletion308: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationCompletion308",
    ends={
        Property(name="alf_VariableDeclarationCompletion", type=alf_InvocationOrAssignementOrDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InvocationOrAssignementOrDeclarationStatement309", type=alf_VariableDeclarationCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignmentCompletion310: BinaryAssociation = BinaryAssociation(
    name="assignmentCompletion310",
    ends={
        Property(name="alf_AssignmentCompletion312", type=alf_InvocationOrAssignementOrDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InvocationOrAssignementOrDeclarationStatement311", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
_super313: BinaryAssociation = BinaryAssociation(
    name="_super313",
    ends={
        Property(name="alf_SuperInvocationExpression314", type=alf_SuperInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationStatement", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
_this315: BinaryAssociation = BinaryAssociation(
    name="_this315",
    ends={
        Property(name="alf_ThisExpression316", type=alf_ThisInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisInvocationStatement", type=alf_ThisExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignmentCompletion317: BinaryAssociation = BinaryAssociation(
    name="assignmentCompletion317",
    ends={
        Property(name="alf_AssignmentCompletion319", type=alf_ThisInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisInvocationStatement318", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
_new320: BinaryAssociation = BinaryAssociation(
    name="_new320",
    ends={
        Property(name="alf_InstanceCreationExpression321", type=alf_InstanceCreationInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationInvocationStatement", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initValue322: BinaryAssociation = BinaryAssociation(
    name="initValue322",
    ends={
        Property(name="alf_AssignmentCompletion324", type=alf_VariableDeclarationCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_VariableDeclarationCompletion323", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightHandSide325: BinaryAssociation = BinaryAssociation(
    name="rightHandSide325",
    ends={
        Property(name="alf_Expression327", type=alf_AssignmentCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssignmentCompletion326", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_alf_INTEGER_LITERAL_WITHOUT_SUFFIX_NUMBER_LITERAL_WITHOUT_SUFFIX = Generalization(general=NUMBER_LITERAL_WITHOUT_SUFFIX, specific=alf_INTEGER_LITERAL_WITHOUT_SUFFIX)
gen_alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX_NUMBER_LITERAL_WITHOUT_SUFFIX = Generalization(general=NUMBER_LITERAL_WITHOUT_SUFFIX, specific=alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX)
gen_alf_LITERAL_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_LITERAL)
gen_alf_BOOLEAN_LITERAL_LITERAL = Generalization(general=LITERAL, specific=alf_BOOLEAN_LITERAL)
gen_alf_NUMBER_LITERAL_LITERAL = Generalization(general=LITERAL, specific=alf_NUMBER_LITERAL)
gen_alf_INTEGER_LITERAL_NUMBER_LITERAL = Generalization(general=NUMBER_LITERAL, specific=alf_INTEGER_LITERAL)
gen_alf_UNLIMITED_LITERAL_NUMBER_LITERAL = Generalization(general=NUMBER_LITERAL, specific=alf_UNLIMITED_LITERAL)
gen_alf_STRING_LITERAL_LITERAL = Generalization(general=LITERAL, specific=alf_STRING_LITERAL)
gen_alf_NameExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_NameExpression)
gen_alf_NameExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_NameExpression)
gen_alf_Expression_SequenceElement = Generalization(general=SequenceElement, specific=alf_Expression)
gen_alf_ConditionalTestExpression_Expression = Generalization(general=Expression, specific=alf_ConditionalTestExpression)
gen_alf_OperationCallExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_OperationCallExpression)
gen_alf_PropertyCallExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_PropertyCallExpression)
gen_alf_LinkOperationExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_LinkOperationExpression)
gen_alf_SequenceExpansionExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_SequenceExpansionExpression)
gen_alf_SequenceOperationExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_SequenceOperationExpression)
gen_alf_SequenceReductionExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_SequenceReductionExpression)
gen_alf_SelectOrRejectOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_SelectOrRejectOperation)
gen_alf_CollectOrIterateOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_CollectOrIterateOperation)
gen_alf_ForAllOrExistsOrOneOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_ForAllOrExistsOrOneOperation)
gen_alf_IsUniqueOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_IsUniqueOperation)
gen_alf_ParenthesizedExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_ParenthesizedExpression)
gen_alf_ParenthesizedExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_ParenthesizedExpression)
gen_alf_NullExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_NullExpression)
gen_alf_ThisExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_ThisExpression)
gen_alf_ThisExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_ThisExpression)
gen_alf_SuperInvocationExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_SuperInvocationExpression)
gen_alf_SuperInvocationExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_SuperInvocationExpression)
gen_alf_InstanceCreationExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_InstanceCreationExpression)
gen_alf_InstanceCreationExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_InstanceCreationExpression)
gen_alf_SequenceConstructionExpression_SequenceElement = Generalization(general=SequenceElement, specific=alf_SequenceConstructionExpression)
gen_alf_InlineStatement_Statement = Generalization(general=Statement, specific=alf_InlineStatement)
gen_alf_AnnotatedStatement_Statement = Generalization(general=Statement, specific=alf_AnnotatedStatement)
gen_alf_BlockStatement_Statement = Generalization(general=Statement, specific=alf_BlockStatement)
gen_alf_EmptyStatement_Statement = Generalization(general=Statement, specific=alf_EmptyStatement)
gen_alf_LocalNameDeclarationStatement_Statement = Generalization(general=Statement, specific=alf_LocalNameDeclarationStatement)
gen_alf_IfStatement_Statement = Generalization(general=Statement, specific=alf_IfStatement)
gen_alf_SwitchStatement_Statement = Generalization(general=Statement, specific=alf_SwitchStatement)
gen_alf_WhileStatement_Statement = Generalization(general=Statement, specific=alf_WhileStatement)
gen_alf_DoStatement_Statement = Generalization(general=Statement, specific=alf_DoStatement)
gen_alf_ForStatement_Statement = Generalization(general=Statement, specific=alf_ForStatement)
gen_alf_BreakStatement_Statement = Generalization(general=Statement, specific=alf_BreakStatement)
gen_alf_ReturnStatement_Statement = Generalization(general=Statement, specific=alf_ReturnStatement)
gen_alf_AcceptStatement_Statement = Generalization(general=Statement, specific=alf_AcceptStatement)
gen_alf_ClassifyStatement_Statement = Generalization(general=Statement, specific=alf_ClassifyStatement)
gen_alf_InvocationOrAssignementOrDeclarationStatement_Statement = Generalization(general=Statement, specific=alf_InvocationOrAssignementOrDeclarationStatement)
gen_alf_SuperInvocationStatement_Statement = Generalization(general=Statement, specific=alf_SuperInvocationStatement)
gen_alf_ThisInvocationStatement_Statement = Generalization(general=Statement, specific=alf_ThisInvocationStatement)
gen_alf_InstanceCreationInvocationStatement_Statement = Generalization(general=Statement, specific=alf_InstanceCreationInvocationStatement)

# Domain Model
domain_model = DomainModel(
    name="alf",
    types={alf_OperationDefinitionOrStub, alf_OperationDeclaration, alf_Block, alf_FormalParameters, alf_TypePart, alf_RedefinitionClause, alf_FormalParameterList, alf_FormalParameter, alf_TypeName, alf_Multiplicity, alf_MultiplicityRange, alf_Operations, alf_INTEGER_LITERAL_WITHOUT_SUFFIX, NUMBER_LITERAL_WITHOUT_SUFFIX, alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX, alf_QualifiedNameWithBinding, alf_QualifiedNameList, alf_Test, alf_Expression, alf_AssignmentCompletion, alf_Statement, alf_LITERAL, ValueSpecification, alf_SuffixExpression, alf_BOOLEAN_LITERAL, LITERAL, alf_NUMBER_LITERAL, alf_INTEGER_LITERAL, NUMBER_LITERAL, alf_UNLIMITED_LITERAL, alf_STRING_LITERAL, alf_NameExpression, NonLiteralValueSpecification, alf_NUMBER_LITERAL_WITHOUT_SUFFIX, alf_SequenceConstructionOrAccessCompletion, alf_UnqualifiedName, alf_TemplateBinding, alf_NamedTemplateBinding, alf_TupleElement, SequenceElement, alf_ConditionalTestExpression, Expression, alf_ConditionalOrExpression, alf_QualifiedNamePath, alf_Tuple, alf_ConditionalAndExpression, alf_InclusiveOrExpression, alf_ExclusiveOrExpression, alf_AndExpression, alf_EqualityExpression, alf_ClassificationExpression, alf_RelationalExpression, alf_ShiftExpression, alf_AdditiveExpression, alf_MultiplicativeExpression, alf_UnaryExpression, alf_PrimaryExpression, alf_OperationCallExpression, SuffixExpression, alf_OperationCallExpressionWithoutDot, alf_PropertyCallExpression, alf_LinkOperationExpression, alf_LinkOperationTuple, alf_ValueSpecification, alf_SequenceExpansionExpression, alf_SequenceOperationExpression, alf_SequenceReductionExpression, alf_LinkOperationTupleElement, alf_SelectOrRejectOperation, SequenceExpansionExpression, alf_CollectOrIterateOperation, alf_ForAllOrExistsOrOneOperation, alf_InstanceCreationExpression, alf_IsUniqueOperation, alf_NonLiteralValueSpecification, alf_ParenthesizedExpression, alf_NullExpression, alf_ThisExpression, alf_SuperInvocationExpression, alf_SequenceConstructionCompletion, alf_AccessCompletion, alf_PartialSequenceConstructionCompletion, alf_SequenceConstructionExpression, alf_SequenceElement, alf_ClassExtentExpression, alf_StatementSequence, alf_DocumentedStatement, alf_InlineStatement, Statement, alf_AnnotatedStatement, alf_Annotation, alf_BlockStatement, alf_EmptyStatement, alf_LocalNameDeclarationStatement, alf_IfStatement, alf_SequentialClauses, alf_FinalClause, alf_ConcurrentClauses, alf_NonFinalClause, alf_SwitchStatement, alf_SwitchClause, alf_SwitchDefaultClause, alf_SwitchCase, alf_NonEmptyStatementSequence, alf_WhileStatement, alf_DoStatement, alf_ForStatement, alf_ForControl, alf_LoopVariableDefinition, alf_BreakStatement, alf_ReturnStatement, alf_AcceptStatement, alf_AcceptClause, alf_SimpleAcceptStatementCompletion, alf_CompoundAcceptStatementCompletion, alf_AcceptBlock, alf_ClassifyStatement, alf_ClassificationClause, alf_ClassificationFromClause, alf_ClassificationToClause, alf_ReclassifyAllClause, alf_InvocationOrAssignementOrDeclarationStatement, alf_VariableDeclarationCompletion, alf_SuperInvocationStatement, alf_ThisInvocationStatement, alf_InstanceCreationInvocationStatement, ParameterDirection, BooleanValue, LinkOperationKind, ForAllOrExistsOrOneOperator, SelectOrRejectOperator, CollectOrIterateOperator, AnnotationKind, AssignmentOperator},
    associations={operations0, declaration1, body3, formalParameters5, returnType7, redefinition9, formalParameterList11, formalParameter13, type15, typeName18, multiplicity20, range22, qualifiedName29, redefinedOperations31, expression33, assignExpression34, statements36, block38, suffix41, lower24, upper26, sequenceConstructionCompletion45, suffix47, namespace50, templateBinding52, bindings54, actual56, binding59, remaining63, tupleElements65, argument67, exp70, whenTrue72, path42, invocationCompletion43, exp77, exp79, exp81, exp83, exp85, exp87, exp89, whenFalse75, left94, right96, exp99, exp101, exp103, exp105, typeName91, tuple109, suffix111, tuple114, suffix116, index119, suffix121, tuple124, prefix107, linkOperationTupleElement125, roleIndex127, objectValueSpec130, tuple133, suffix135, behavior138, suffix140, suffix143, expr145, expOrTypeCast147, casted149, suffix151, suffix154, operationCallWithoutDot156, operationCall158, constructor161, tuple163, sequenceConstuctionCompletion166, suffix168, accessCompletion171, sequenceCompletion173, expression175, accessIndex177, expression180, expression183, sequenceElement186, rangeUpper188, sequence191, statements193, annotation195, block196, statement199, block202, type204, init206, sequentialClausses209, finalClause210, conccurentClauses212, nonFinalClause214, condition216, block219, block222, expression225, switchClause227, defaultClause229, switchCase231, statementSequence233, expression235, statementSequence238, statement241, condition244, block246, block249, condition251, control254, block255, loopVariableDefinition258, expression1260, expression2263, expression266, clause268, simpleAccept269, compoundAccept271, block273, acceptBlock276, clause278, block281, qualifiedNameList284, expression287, clause289, classifyFromClause291, classifyToClause293, reclassyAllClause295, qualifiedNameList297, qualifiedNameList300, qualifiedName303, typePart_OR_assignedPart_OR_invocationPart306, variableDeclarationCompletion308, assignmentCompletion310, _super313, _this315, assignmentCompletion317, _new320, initValue322, rightHandSide325},
    generalizations={gen_alf_INTEGER_LITERAL_WITHOUT_SUFFIX_NUMBER_LITERAL_WITHOUT_SUFFIX, gen_alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX_NUMBER_LITERAL_WITHOUT_SUFFIX, gen_alf_LITERAL_ValueSpecification, gen_alf_BOOLEAN_LITERAL_LITERAL, gen_alf_NUMBER_LITERAL_LITERAL, gen_alf_INTEGER_LITERAL_NUMBER_LITERAL, gen_alf_UNLIMITED_LITERAL_NUMBER_LITERAL, gen_alf_STRING_LITERAL_LITERAL, gen_alf_NameExpression_ValueSpecification, gen_alf_NameExpression_NonLiteralValueSpecification, gen_alf_Expression_SequenceElement, gen_alf_ConditionalTestExpression_Expression, gen_alf_OperationCallExpression_SuffixExpression, gen_alf_PropertyCallExpression_SuffixExpression, gen_alf_LinkOperationExpression_SuffixExpression, gen_alf_SequenceExpansionExpression_SuffixExpression, gen_alf_SequenceOperationExpression_SuffixExpression, gen_alf_SequenceReductionExpression_SuffixExpression, gen_alf_SelectOrRejectOperation_SequenceExpansionExpression, gen_alf_CollectOrIterateOperation_SequenceExpansionExpression, gen_alf_ForAllOrExistsOrOneOperation_SequenceExpansionExpression, gen_alf_IsUniqueOperation_SequenceExpansionExpression, gen_alf_ParenthesizedExpression_ValueSpecification, gen_alf_ParenthesizedExpression_NonLiteralValueSpecification, gen_alf_NullExpression_ValueSpecification, gen_alf_ThisExpression_ValueSpecification, gen_alf_ThisExpression_NonLiteralValueSpecification, gen_alf_SuperInvocationExpression_ValueSpecification, gen_alf_SuperInvocationExpression_NonLiteralValueSpecification, gen_alf_InstanceCreationExpression_ValueSpecification, gen_alf_InstanceCreationExpression_NonLiteralValueSpecification, gen_alf_SequenceConstructionExpression_SequenceElement, gen_alf_InlineStatement_Statement, gen_alf_AnnotatedStatement_Statement, gen_alf_BlockStatement_Statement, gen_alf_EmptyStatement_Statement, gen_alf_LocalNameDeclarationStatement_Statement, gen_alf_IfStatement_Statement, gen_alf_SwitchStatement_Statement, gen_alf_WhileStatement_Statement, gen_alf_DoStatement_Statement, gen_alf_ForStatement_Statement, gen_alf_BreakStatement_Statement, gen_alf_ReturnStatement_Statement, gen_alf_AcceptStatement_Statement, gen_alf_ClassifyStatement_Statement, gen_alf_InvocationOrAssignementOrDeclarationStatement_Statement, gen_alf_SuperInvocationStatement_Statement, gen_alf_ThisInvocationStatement_Statement, gen_alf_InstanceCreationInvocationStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)