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
			EnumerationLiteral(name="CLEAR")
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

ForAllOrExistsOrOneOperator: Enumeration = Enumeration(
    name="ForAllOrExistsOrOneOperator",
    literals={
            EnumerationLiteral(name="FORALL"),
			EnumerationLiteral(name="EXISTS"),
			EnumerationLiteral(name="ONE")
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
alf_Block = Class(name="alf::Block")
alf_LITERAL = Class(name="alf::LITERAL")
ValueSpecification = Class(name="ValueSpecification")
alf_BOOLEAN_LITERAL = Class(name="alf::BOOLEAN::LITERAL")
LITERAL = Class(name="LITERAL")
alf_NUMBER_LITERAL = Class(name="alf::NUMBER::LITERAL")
alf_INTEGER_LITERAL = Class(name="alf::INTEGER::LITERAL")
NUMBER_LITERAL = Class(name="NUMBER::LITERAL")
alf_UNLIMITED_LITERAL = Class(name="alf::UNLIMITED::LITERAL")
alf_STRING_LITERAL = Class(name="alf::STRING::LITERAL")
alf_Test = Class(name="alf::Test")
alf_Expression = Class(name="alf::Expression")
alf_AssignmentCompletion = Class(name="alf::AssignmentCompletion")
alf_Statement = Class(name="alf::Statement")
alf_NamedTemplateBinding = Class(name="alf::NamedTemplateBinding")
alf_QualifiedNameWithBinding = Class(name="alf::QualifiedNameWithBinding")
alf_TupleElement = Class(name="alf::TupleElement")
alf_NameExpression = Class(name="alf::NameExpression")
NonLiteralValueSpecification = Class(name="NonLiteralValueSpecification")
alf_QualifiedNamePath = Class(name="alf::QualifiedNamePath")
alf_Tuple = Class(name="alf::Tuple")
alf_SequenceConstructionOrAccessCompletion = Class(name="alf::SequenceConstructionOrAccessCompletion")
alf_SuffixExpression = Class(name="alf::SuffixExpression")
alf_UnqualifiedName = Class(name="alf::UnqualifiedName")
alf_TemplateBinding = Class(name="alf::TemplateBinding")
alf_EqualityExpression = Class(name="alf::EqualityExpression")
alf_ClassificationExpression = Class(name="alf::ClassificationExpression")
alf_RelationalExpression = Class(name="alf::RelationalExpression")
alf_ShiftExpression = Class(name="alf::ShiftExpression")
SequenceElement = Class(name="SequenceElement")
alf_ConditionalTestExpression = Class(name="alf::ConditionalTestExpression")
Expression = Class(name="Expression")
alf_ConditionalOrExpression = Class(name="alf::ConditionalOrExpression")
alf_ConditionalAndExpression = Class(name="alf::ConditionalAndExpression")
alf_InclusiveOrExpression = Class(name="alf::InclusiveOrExpression")
alf_ExclusiveOrExpression = Class(name="alf::ExclusiveOrExpression")
alf_AndExpression = Class(name="alf::AndExpression")
alf_OperationCallExpression = Class(name="alf::OperationCallExpression")
SuffixExpression = Class(name="SuffixExpression")
alf_PropertyCallExpression = Class(name="alf::PropertyCallExpression")
alf_LinkOperationExpression = Class(name="alf::LinkOperationExpression")
alf_LinkOperationTuple = Class(name="alf::LinkOperationTuple")
alf_AdditiveExpression = Class(name="alf::AdditiveExpression")
alf_MultiplicativeExpression = Class(name="alf::MultiplicativeExpression")
alf_UnaryExpression = Class(name="alf::UnaryExpression")
alf_PrimaryExpression = Class(name="alf::PrimaryExpression")
alf_ValueSpecification = Class(name="alf::ValueSpecification")
alf_SequenceReductionExpression = Class(name="alf::SequenceReductionExpression")
alf_SequenceExpansionExpression = Class(name="alf::SequenceExpansionExpression")
alf_LinkOperationTupleElement = Class(name="alf::LinkOperationTupleElement")
alf_SequenceOperationExpression = Class(name="alf::SequenceOperationExpression")
alf_NullExpression = Class(name="alf::NullExpression")
alf_ThisExpression = Class(name="alf::ThisExpression")
alf_SuperInvocationExpression = Class(name="alf::SuperInvocationExpression")
alf_SelectOrRejectOperation = Class(name="alf::SelectOrRejectOperation")
SequenceExpansionExpression = Class(name="SequenceExpansionExpression")
alf_CollectOrIterateOperation = Class(name="alf::CollectOrIterateOperation")
alf_ForAllOrExistsOrOneOperation = Class(name="alf::ForAllOrExistsOrOneOperation")
alf_IsUniqueOperation = Class(name="alf::IsUniqueOperation")
alf_NonLiteralValueSpecification = Class(name="alf::NonLiteralValueSpecification")
alf_ParenthesizedExpression = Class(name="alf::ParenthesizedExpression")
alf_PartialSequenceConstructionCompletion = Class(name="alf::PartialSequenceConstructionCompletion")
alf_SequenceConstructionExpression = Class(name="alf::SequenceConstructionExpression")
alf_SequenceElement = Class(name="alf::SequenceElement")
alf_ClassExtentExpression = Class(name="alf::ClassExtentExpression")
alf_InstanceCreationExpression = Class(name="alf::InstanceCreationExpression")
alf_InstanceCreationTuple = Class(name="alf::InstanceCreationTuple")
alf_InstanceCreationTupleElement = Class(name="alf::InstanceCreationTupleElement")
alf_AccessCompletion = Class(name="alf::AccessCompletion")
alf_BlockStatement = Class(name="alf::BlockStatement")
alf_EmptyStatement = Class(name="alf::EmptyStatement")
alf_LocalNameDeclarationStatement = Class(name="alf::LocalNameDeclarationStatement")
alf_StatementSequence = Class(name="alf::StatementSequence")
alf_DocumentedStatement = Class(name="alf::DocumentedStatement")
alf_InlineStatement = Class(name="alf::InlineStatement")
Statement = Class(name="Statement")
alf_AnnotatedStatement = Class(name="alf::AnnotatedStatement")
alf_Annotation = Class(name="alf::Annotation")
alf_SwitchStatement = Class(name="alf::SwitchStatement")
alf_SwitchClause = Class(name="alf::SwitchClause")
alf_SwitchDefaultClause = Class(name="alf::SwitchDefaultClause")
alf_SwitchCase = Class(name="alf::SwitchCase")
alf_NonEmptyStatementSequence = Class(name="alf::NonEmptyStatementSequence")
alf_IfStatement = Class(name="alf::IfStatement")
alf_SequentialClauses = Class(name="alf::SequentialClauses")
alf_FinalClause = Class(name="alf::FinalClause")
alf_ConcurrentClauses = Class(name="alf::ConcurrentClauses")
alf_NonFinalClause = Class(name="alf::NonFinalClause")
alf_ForStatement = Class(name="alf::ForStatement")
alf_ForControl = Class(name="alf::ForControl")
alf_LoopVariableDefinition = Class(name="alf::LoopVariableDefinition")
alf_WhileStatement = Class(name="alf::WhileStatement")
alf_DoStatement = Class(name="alf::DoStatement")
alf_AcceptBlock = Class(name="alf::AcceptBlock")
alf_QualifiedNameList = Class(name="alf::QualifiedNameList")
alf_ClassifyStatement = Class(name="alf::ClassifyStatement")
alf_ClassificationClause = Class(name="alf::ClassificationClause")
alf_BreakStatement = Class(name="alf::BreakStatement")
alf_ReturnStatement = Class(name="alf::ReturnStatement")
alf_AcceptStatement = Class(name="alf::AcceptStatement")
alf_AcceptClause = Class(name="alf::AcceptClause")
alf_SimpleAcceptStatementCompletion = Class(name="alf::SimpleAcceptStatementCompletion")
alf_CompoundAcceptStatementCompletion = Class(name="alf::CompoundAcceptStatementCompletion")
alf_VariableDeclarationCompletion = Class(name="alf::VariableDeclarationCompletion")
alf_SuperInvocationStatement = Class(name="alf::SuperInvocationStatement")
alf_ThisInvocationStatement = Class(name="alf::ThisInvocationStatement")
alf_InstanceCreationInvocationStatement = Class(name="alf::InstanceCreationInvocationStatement")
alf_ClassificationFromClause = Class(name="alf::ClassificationFromClause")
alf_ClassificationToClause = Class(name="alf::ClassificationToClause")
alf_ReclassifyAllClause = Class(name="alf::ReclassifyAllClause")
alf_InvocationOrAssignementOrDeclarationStatement = Class(name="alf::InvocationOrAssignementOrDeclarationStatement")

# alf_Block class attributes and methods

# alf_LITERAL class attributes and methods

# ValueSpecification class attributes and methods

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

# alf_Test class attributes and methods

# alf_Expression class attributes and methods

# alf_AssignmentCompletion class attributes and methods
alf_AssignmentCompletion_op: Property = Property(name="op", type=StringType)
alf_AssignmentCompletion.attributes={alf_AssignmentCompletion_op}

# alf_Statement class attributes and methods

# alf_NamedTemplateBinding class attributes and methods
alf_NamedTemplateBinding_formal: Property = Property(name="formal", type=StringType)
alf_NamedTemplateBinding.attributes={alf_NamedTemplateBinding_formal}

# alf_QualifiedNameWithBinding class attributes and methods
alf_QualifiedNameWithBinding_id: Property = Property(name="id", type=StringType)
alf_QualifiedNameWithBinding.attributes={alf_QualifiedNameWithBinding_id}

# alf_TupleElement class attributes and methods

# alf_NameExpression class attributes and methods
alf_NameExpression_prefixOp: Property = Property(name="prefixOp", type=StringType)
alf_NameExpression_id: Property = Property(name="id", type=StringType)
alf_NameExpression_postfixOp: Property = Property(name="postfixOp", type=StringType)
alf_NameExpression.attributes={alf_NameExpression_postfixOp, alf_NameExpression_id, alf_NameExpression_prefixOp}

# NonLiteralValueSpecification class attributes and methods

# alf_QualifiedNamePath class attributes and methods

# alf_Tuple class attributes and methods

# alf_SequenceConstructionOrAccessCompletion class attributes and methods
alf_SequenceConstructionOrAccessCompletion_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_SequenceConstructionOrAccessCompletion.attributes={alf_SequenceConstructionOrAccessCompletion_multiplicityIndicator}

# alf_SuffixExpression class attributes and methods

# alf_UnqualifiedName class attributes and methods
alf_UnqualifiedName_name: Property = Property(name="name", type=StringType)
alf_UnqualifiedName.attributes={alf_UnqualifiedName_name}

# alf_TemplateBinding class attributes and methods

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

# SequenceElement class attributes and methods

# alf_ConditionalTestExpression class attributes and methods

# Expression class attributes and methods

# alf_ConditionalOrExpression class attributes and methods

# alf_ConditionalAndExpression class attributes and methods

# alf_InclusiveOrExpression class attributes and methods

# alf_ExclusiveOrExpression class attributes and methods

# alf_AndExpression class attributes and methods

# alf_OperationCallExpression class attributes and methods
alf_OperationCallExpression_operationName: Property = Property(name="operationName", type=StringType)
alf_OperationCallExpression.attributes={alf_OperationCallExpression_operationName}

# SuffixExpression class attributes and methods

# alf_PropertyCallExpression class attributes and methods
alf_PropertyCallExpression_propertyName: Property = Property(name="propertyName", type=StringType)
alf_PropertyCallExpression.attributes={alf_PropertyCallExpression_propertyName}

# alf_LinkOperationExpression class attributes and methods
alf_LinkOperationExpression_kind: Property = Property(name="kind", type=StringType)
alf_LinkOperationExpression.attributes={alf_LinkOperationExpression_kind}

# alf_LinkOperationTuple class attributes and methods

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

# alf_ValueSpecification class attributes and methods

# alf_SequenceReductionExpression class attributes and methods
alf_SequenceReductionExpression_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
alf_SequenceReductionExpression.attributes={alf_SequenceReductionExpression_isOrdered}

# alf_SequenceExpansionExpression class attributes and methods
alf_SequenceExpansionExpression_name: Property = Property(name="name", type=StringType)
alf_SequenceExpansionExpression.attributes={alf_SequenceExpansionExpression_name}

# alf_LinkOperationTupleElement class attributes and methods
alf_LinkOperationTupleElement_role: Property = Property(name="role", type=StringType)
alf_LinkOperationTupleElement.attributes={alf_LinkOperationTupleElement_role}

# alf_SequenceOperationExpression class attributes and methods

# alf_NullExpression class attributes and methods

# alf_ThisExpression class attributes and methods

# alf_SuperInvocationExpression class attributes and methods

# alf_SelectOrRejectOperation class attributes and methods
alf_SelectOrRejectOperation_op: Property = Property(name="op", type=StringType)
alf_SelectOrRejectOperation.attributes={alf_SelectOrRejectOperation_op}

# SequenceExpansionExpression class attributes and methods

# alf_CollectOrIterateOperation class attributes and methods
alf_CollectOrIterateOperation_op: Property = Property(name="op", type=StringType)
alf_CollectOrIterateOperation.attributes={alf_CollectOrIterateOperation_op}

# alf_ForAllOrExistsOrOneOperation class attributes and methods
alf_ForAllOrExistsOrOneOperation_op: Property = Property(name="op", type=StringType)
alf_ForAllOrExistsOrOneOperation.attributes={alf_ForAllOrExistsOrOneOperation_op}

# alf_IsUniqueOperation class attributes and methods

# alf_NonLiteralValueSpecification class attributes and methods

# alf_ParenthesizedExpression class attributes and methods

# alf_PartialSequenceConstructionCompletion class attributes and methods

# alf_SequenceConstructionExpression class attributes and methods

# alf_SequenceElement class attributes and methods

# alf_ClassExtentExpression class attributes and methods

# alf_InstanceCreationExpression class attributes and methods

# alf_InstanceCreationTuple class attributes and methods

# alf_InstanceCreationTupleElement class attributes and methods
alf_InstanceCreationTupleElement_role: Property = Property(name="role", type=StringType)
alf_InstanceCreationTupleElement.attributes={alf_InstanceCreationTupleElement_role}

# alf_AccessCompletion class attributes and methods

# alf_BlockStatement class attributes and methods

# alf_EmptyStatement class attributes and methods

# alf_LocalNameDeclarationStatement class attributes and methods
alf_LocalNameDeclarationStatement_varName: Property = Property(name="varName", type=StringType)
alf_LocalNameDeclarationStatement_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_LocalNameDeclarationStatement.attributes={alf_LocalNameDeclarationStatement_varName, alf_LocalNameDeclarationStatement_multiplicityIndicator}

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
alf_Annotation_args: Property = Property(name="args", type=StringType)
alf_Annotation_kind: Property = Property(name="kind", type=StringType)
alf_Annotation.attributes={alf_Annotation_kind, alf_Annotation_args}

# alf_SwitchStatement class attributes and methods

# alf_SwitchClause class attributes and methods

# alf_SwitchDefaultClause class attributes and methods

# alf_SwitchCase class attributes and methods

# alf_NonEmptyStatementSequence class attributes and methods

# alf_IfStatement class attributes and methods

# alf_SequentialClauses class attributes and methods

# alf_FinalClause class attributes and methods

# alf_ConcurrentClauses class attributes and methods

# alf_NonFinalClause class attributes and methods

# alf_ForStatement class attributes and methods

# alf_ForControl class attributes and methods

# alf_LoopVariableDefinition class attributes and methods
alf_LoopVariableDefinition_name: Property = Property(name="name", type=StringType)
alf_LoopVariableDefinition.attributes={alf_LoopVariableDefinition_name}

# alf_WhileStatement class attributes and methods

# alf_DoStatement class attributes and methods

# alf_AcceptBlock class attributes and methods

# alf_QualifiedNameList class attributes and methods

# alf_ClassifyStatement class attributes and methods

# alf_ClassificationClause class attributes and methods

# alf_BreakStatement class attributes and methods

# alf_ReturnStatement class attributes and methods

# alf_AcceptStatement class attributes and methods

# alf_AcceptClause class attributes and methods
alf_AcceptClause_name: Property = Property(name="name", type=StringType)
alf_AcceptClause.attributes={alf_AcceptClause_name}

# alf_SimpleAcceptStatementCompletion class attributes and methods

# alf_CompoundAcceptStatementCompletion class attributes and methods

# alf_VariableDeclarationCompletion class attributes and methods
alf_VariableDeclarationCompletion_multiplicityIndicator: Property = Property(name="multiplicityIndicator", type=BooleanType)
alf_VariableDeclarationCompletion_variableName: Property = Property(name="variableName", type=StringType)
alf_VariableDeclarationCompletion.attributes={alf_VariableDeclarationCompletion_variableName, alf_VariableDeclarationCompletion_multiplicityIndicator}

# alf_SuperInvocationStatement class attributes and methods

# alf_ThisInvocationStatement class attributes and methods

# alf_InstanceCreationInvocationStatement class attributes and methods

# alf_ClassificationFromClause class attributes and methods

# alf_ClassificationToClause class attributes and methods

# alf_ReclassifyAllClause class attributes and methods

# alf_InvocationOrAssignementOrDeclarationStatement class attributes and methods

# Relationships
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="alf_Block", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test6", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="alf_Expression", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test", type=alf_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignExpression1: BinaryAssociation = BinaryAssociation(
    name="assignExpression1",
    ends={
        Property(name="alf_AssignmentCompletion", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test2", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements3: BinaryAssociation = BinaryAssociation(
    name="statements3",
    ends={
        Property(name="alf_Statement", type=alf_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Test4", type=alf_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateBinding16: BinaryAssociation = BinaryAssociation(
    name="templateBinding16",
    ends={
        Property(name="alf_TemplateBinding", type=alf_UnqualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnqualifiedName17", type=alf_TemplateBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings18: BinaryAssociation = BinaryAssociation(
    name="bindings18",
    ends={
        Property(name="alf_NamedTemplateBinding", type=alf_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TemplateBinding19", type=alf_NamedTemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actual20: BinaryAssociation = BinaryAssociation(
    name="actual20",
    ends={
        Property(name="alf_QualifiedNameWithBinding", type=alf_NamedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NamedTemplateBinding21", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binding22: BinaryAssociation = BinaryAssociation(
    name="binding22",
    ends={
        Property(name="alf_TemplateBinding24", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameWithBinding23", type=alf_TemplateBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remaining26: BinaryAssociation = BinaryAssociation(
    name="remaining26",
    ends={
        Property(name="alf_QualifiedNameWithBinding27", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameWithBinding25", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tupleElements28: BinaryAssociation = BinaryAssociation(
    name="tupleElements28",
    ends={
        Property(name="alf_TupleElement", type=alf_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Tuple29", type=alf_TupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument30: BinaryAssociation = BinaryAssociation(
    name="argument30",
    ends={
        Property(name="alf_Expression32", type=alf_TupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_TupleElement31", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path7: BinaryAssociation = BinaryAssociation(
    name="path7",
    ends={
        Property(name="alf_QualifiedNamePath", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression", type=alf_QualifiedNamePath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invocationCompletion8: BinaryAssociation = BinaryAssociation(
    name="invocationCompletion8",
    ends={
        Property(name="alf_Tuple", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression9", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceConstructionCompletion10: BinaryAssociation = BinaryAssociation(
    name="sequenceConstructionCompletion10",
    ends={
        Property(name="alf_SequenceConstructionOrAccessCompletion", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression11", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix12: BinaryAssociation = BinaryAssociation(
    name="suffix12",
    ends={
        Property(name="alf_SuffixExpression", type=alf_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NameExpression13", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespace14: BinaryAssociation = BinaryAssociation(
    name="namespace14",
    ends={
        Property(name="alf_UnqualifiedName", type=alf_QualifiedNamePath, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNamePath15", type=alf_UnqualifiedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp48: BinaryAssociation = BinaryAssociation(
    name="exp48",
    ends={
        Property(name="alf_EqualityExpression", type=alf_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AndExpression49", type=alf_EqualityExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp50: BinaryAssociation = BinaryAssociation(
    name="exp50",
    ends={
        Property(name="alf_ClassificationExpression", type=alf_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_EqualityExpression51", type=alf_ClassificationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp52: BinaryAssociation = BinaryAssociation(
    name="exp52",
    ends={
        Property(name="alf_RelationalExpression", type=alf_ClassificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpression53", type=alf_RelationalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName54: BinaryAssociation = BinaryAssociation(
    name="typeName54",
    ends={
        Property(name="alf_NameExpression56", type=alf_ClassificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationExpression55", type=alf_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="alf_ShiftExpression", type=alf_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpression58", type=alf_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp33: BinaryAssociation = BinaryAssociation(
    name="exp33",
    ends={
        Property(name="alf_ConditionalOrExpression", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalTestExpression", type=alf_ConditionalOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenTrue35: BinaryAssociation = BinaryAssociation(
    name="whenTrue35",
    ends={
        Property(name="alf_ConditionalTestExpression36", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalTestExpression34", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenFalse38: BinaryAssociation = BinaryAssociation(
    name="whenFalse38",
    ends={
        Property(name="alf_ConditionalTestExpression39", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalTestExpression37", type=alf_ConditionalTestExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp40: BinaryAssociation = BinaryAssociation(
    name="exp40",
    ends={
        Property(name="alf_ConditionalAndExpression", type=alf_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalOrExpression41", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp42: BinaryAssociation = BinaryAssociation(
    name="exp42",
    ends={
        Property(name="alf_InclusiveOrExpression", type=alf_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConditionalAndExpression43", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp44: BinaryAssociation = BinaryAssociation(
    name="exp44",
    ends={
        Property(name="alf_ExclusiveOrExpression", type=alf_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InclusiveOrExpression45", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp46: BinaryAssociation = BinaryAssociation(
    name="exp46",
    ends={
        Property(name="alf_AndExpression", type=alf_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ExclusiveOrExpression47", type=alf_AndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prefix70: BinaryAssociation = BinaryAssociation(
    name="prefix70",
    ends={
        Property(name="alf_ValueSpecification", type=alf_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PrimaryExpression71", type=alf_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple72: BinaryAssociation = BinaryAssociation(
    name="tuple72",
    ends={
        Property(name="alf_Tuple73", type=alf_OperationCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationCallExpression", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix74: BinaryAssociation = BinaryAssociation(
    name="suffix74",
    ends={
        Property(name="alf_SuffixExpression76", type=alf_OperationCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_OperationCallExpression75", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index77: BinaryAssociation = BinaryAssociation(
    name="index77",
    ends={
        Property(name="alf_Expression78", type=alf_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyCallExpression", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix79: BinaryAssociation = BinaryAssociation(
    name="suffix79",
    ends={
        Property(name="alf_SuffixExpression81", type=alf_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PropertyCallExpression80", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="alf_ShiftExpression61", type=alf_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_RelationalExpression60", type=alf_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp62: BinaryAssociation = BinaryAssociation(
    name="exp62",
    ends={
        Property(name="alf_AdditiveExpression", type=alf_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ShiftExpression63", type=alf_AdditiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp64: BinaryAssociation = BinaryAssociation(
    name="exp64",
    ends={
        Property(name="alf_MultiplicativeExpression", type=alf_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AdditiveExpression65", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp66: BinaryAssociation = BinaryAssociation(
    name="exp66",
    ends={
        Property(name="alf_UnaryExpression", type=alf_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_MultiplicativeExpression67", type=alf_UnaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp68: BinaryAssociation = BinaryAssociation(
    name="exp68",
    ends={
        Property(name="alf_PrimaryExpression", type=alf_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_UnaryExpression69", type=alf_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationName91: BinaryAssociation = BinaryAssociation(
    name="operationName91",
    ends={
        Property(name="alf_SequenceOperationExpression", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="alf_QualifiedNameWithBinding92", type=alf_SequenceOperationExpression, multiplicity=Multiplicity(1, 1))
    }
)
tuple93: BinaryAssociation = BinaryAssociation(
    name="tuple93",
    ends={
        Property(name="alf_Tuple95", type=alf_SequenceOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationExpression94", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix96: BinaryAssociation = BinaryAssociation(
    name="suffix96",
    ends={
        Property(name="alf_SuffixExpression98", type=alf_SequenceOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceOperationExpression97", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behavior99: BinaryAssociation = BinaryAssociation(
    name="behavior99",
    ends={
        Property(name="alf_QualifiedNameWithBinding100", type=alf_SequenceReductionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceReductionExpression", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix101: BinaryAssociation = BinaryAssociation(
    name="suffix101",
    ends={
        Property(name="alf_SuffixExpression103", type=alf_SequenceReductionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceReductionExpression102", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr104: BinaryAssociation = BinaryAssociation(
    name="expr104",
    ends={
        Property(name="alf_Expression105", type=alf_SequenceExpansionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceExpansionExpression", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix106: BinaryAssociation = BinaryAssociation(
    name="suffix106",
    ends={
        Property(name="alf_SuffixExpression108", type=alf_SequenceExpansionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceExpansionExpression107", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple82: BinaryAssociation = BinaryAssociation(
    name="tuple82",
    ends={
        Property(name="alf_LinkOperationTuple", type=alf_LinkOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationExpression", type=alf_LinkOperationTuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkOperationTupleElement83: BinaryAssociation = BinaryAssociation(
    name="linkOperationTupleElement83",
    ends={
        Property(name="alf_LinkOperationTupleElement", type=alf_LinkOperationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTuple84", type=alf_LinkOperationTupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roleIndex85: BinaryAssociation = BinaryAssociation(
    name="roleIndex85",
    ends={
        Property(name="alf_Expression87", type=alf_LinkOperationTupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTupleElement86", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object88: BinaryAssociation = BinaryAssociation(
    name="object88",
    ends={
        Property(name="alf_Expression90", type=alf_LinkOperationTupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LinkOperationTupleElement89", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expOrTypeCast109: BinaryAssociation = BinaryAssociation(
    name="expOrTypeCast109",
    ends={
        Property(name="alf_Expression110", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
casted111: BinaryAssociation = BinaryAssociation(
    name="casted111",
    ends={
        Property(name="alf_NonLiteralValueSpecification", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression112", type=alf_NonLiteralValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix113: BinaryAssociation = BinaryAssociation(
    name="suffix113",
    ends={
        Property(name="alf_SuffixExpression115", type=alf_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ParenthesizedExpression114", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix116: BinaryAssociation = BinaryAssociation(
    name="suffix116",
    ends={
        Property(name="alf_SuffixExpression117", type=alf_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisExpression", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple118: BinaryAssociation = BinaryAssociation(
    name="tuple118",
    ends={
        Property(name="alf_Tuple119", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationExpression", type=alf_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceCompletion137: BinaryAssociation = BinaryAssociation(
    name="sequenceCompletion137",
    ends={
        Property(name="alf_PartialSequenceConstructionCompletion", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionOrAccessCompletion138", type=alf_PartialSequenceConstructionCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression139: BinaryAssociation = BinaryAssociation(
    name="expression139",
    ends={
        Property(name="alf_SequenceConstructionExpression", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionOrAccessCompletion140", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessIndex141: BinaryAssociation = BinaryAssociation(
    name="accessIndex141",
    ends={
        Property(name="alf_Expression143", type=alf_AccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AccessCompletion142", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression144: BinaryAssociation = BinaryAssociation(
    name="expression144",
    ends={
        Property(name="alf_SequenceConstructionExpression146", type=alf_PartialSequenceConstructionCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_PartialSequenceConstructionCompletion145", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceElement147: BinaryAssociation = BinaryAssociation(
    name="sequenceElement147",
    ends={
        Property(name="alf_SequenceElement", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionExpression148", type=alf_SequenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rangeUpper149: BinaryAssociation = BinaryAssociation(
    name="rangeUpper149",
    ends={
        Property(name="alf_Expression151", type=alf_SequenceConstructionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionExpression150", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationName120: BinaryAssociation = BinaryAssociation(
    name="operationName120",
    ends={
        Property(name="alf_QualifiedNameWithBinding122", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationExpression121", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructor123: BinaryAssociation = BinaryAssociation(
    name="constructor123",
    ends={
        Property(name="alf_QualifiedNameWithBinding124", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple125: BinaryAssociation = BinaryAssociation(
    name="tuple125",
    ends={
        Property(name="alf_InstanceCreationTuple", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression126", type=alf_InstanceCreationTuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffix127: BinaryAssociation = BinaryAssociation(
    name="suffix127",
    ends={
        Property(name="alf_SuffixExpression129", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationExpression128", type=alf_SuffixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceCreationTupleElement130: BinaryAssociation = BinaryAssociation(
    name="instanceCreationTupleElement130",
    ends={
        Property(name="alf_InstanceCreationTupleElement", type=alf_InstanceCreationTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationTuple131", type=alf_InstanceCreationTupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object132: BinaryAssociation = BinaryAssociation(
    name="object132",
    ends={
        Property(name="alf_Expression134", type=alf_InstanceCreationTupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationTupleElement133", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessCompletion135: BinaryAssociation = BinaryAssociation(
    name="accessCompletion135",
    ends={
        Property(name="alf_AccessCompletion", type=alf_SequenceConstructionOrAccessCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequenceConstructionOrAccessCompletion136", type=alf_AccessCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block163: BinaryAssociation = BinaryAssociation(
    name="block163",
    ends={
        Property(name="alf_Block164", type=alf_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_BlockStatement", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type165: BinaryAssociation = BinaryAssociation(
    name="type165",
    ends={
        Property(name="alf_QualifiedNameWithBinding166", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init167: BinaryAssociation = BinaryAssociation(
    name="init167",
    ends={
        Property(name="alf_SequenceElement169", type=alf_LocalNameDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LocalNameDeclarationStatement168", type=alf_SequenceElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence152: BinaryAssociation = BinaryAssociation(
    name="sequence152",
    ends={
        Property(name="alf_StatementSequence", type=alf_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_Block153", type=alf_StatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements154: BinaryAssociation = BinaryAssociation(
    name="statements154",
    ends={
        Property(name="alf_DocumentedStatement", type=alf_StatementSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_StatementSequence155", type=alf_DocumentedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement156: BinaryAssociation = BinaryAssociation(
    name="statement156",
    ends={
        Property(name="alf_Statement158", type=alf_DocumentedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DocumentedStatement157", type=alf_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation159: BinaryAssociation = BinaryAssociation(
    name="annotation159",
    ends={
        Property(name="alf_Annotation", type=alf_AnnotatedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AnnotatedStatement", type=alf_Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement160: BinaryAssociation = BinaryAssociation(
    name="statement160",
    ends={
        Property(name="alf_Statement162", type=alf_AnnotatedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AnnotatedStatement161", type=alf_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block183: BinaryAssociation = BinaryAssociation(
    name="block183",
    ends={
        Property(name="alf_Block185", type=alf_FinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_FinalClause184", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression186: BinaryAssociation = BinaryAssociation(
    name="expression186",
    ends={
        Property(name="alf_Expression187", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchClause188: BinaryAssociation = BinaryAssociation(
    name="switchClause188",
    ends={
        Property(name="alf_SwitchClause", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement189", type=alf_SwitchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultClause190: BinaryAssociation = BinaryAssociation(
    name="defaultClause190",
    ends={
        Property(name="alf_SwitchDefaultClause", type=alf_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchStatement191", type=alf_SwitchDefaultClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchCase192: BinaryAssociation = BinaryAssociation(
    name="switchCase192",
    ends={
        Property(name="alf_SwitchCase", type=alf_SwitchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchClause193", type=alf_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementSequence194: BinaryAssociation = BinaryAssociation(
    name="statementSequence194",
    ends={
        Property(name="alf_NonEmptyStatementSequence", type=alf_SwitchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchClause195", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequentialClausses170: BinaryAssociation = BinaryAssociation(
    name="sequentialClausses170",
    ends={
        Property(name="alf_SequentialClauses", type=alf_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IfStatement", type=alf_SequentialClauses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalClause171: BinaryAssociation = BinaryAssociation(
    name="finalClause171",
    ends={
        Property(name="alf_FinalClause", type=alf_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_IfStatement172", type=alf_FinalClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conccurentClauses173: BinaryAssociation = BinaryAssociation(
    name="conccurentClauses173",
    ends={
        Property(name="alf_ConcurrentClauses", type=alf_SequentialClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SequentialClauses174", type=alf_ConcurrentClauses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonFinalClause175: BinaryAssociation = BinaryAssociation(
    name="nonFinalClause175",
    ends={
        Property(name="alf_NonFinalClause", type=alf_ConcurrentClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ConcurrentClauses176", type=alf_NonFinalClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition177: BinaryAssociation = BinaryAssociation(
    name="condition177",
    ends={
        Property(name="alf_Expression179", type=alf_NonFinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonFinalClause178", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block180: BinaryAssociation = BinaryAssociation(
    name="block180",
    ends={
        Property(name="alf_Block182", type=alf_NonFinalClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonFinalClause181", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
control215: BinaryAssociation = BinaryAssociation(
    name="control215",
    ends={
        Property(name="alf_ForControl", type=alf_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForStatement", type=alf_ForControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block216: BinaryAssociation = BinaryAssociation(
    name="block216",
    ends={
        Property(name="alf_Block218", type=alf_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForStatement217", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopVariableDefinition219: BinaryAssociation = BinaryAssociation(
    name="loopVariableDefinition219",
    ends={
        Property(name="alf_LoopVariableDefinition", type=alf_ForControl, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ForControl220", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1221: BinaryAssociation = BinaryAssociation(
    name="expression1221",
    ends={
        Property(name="alf_Expression223", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition222", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2224: BinaryAssociation = BinaryAssociation(
    name="expression2224",
    ends={
        Property(name="alf_Expression226", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition225", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type227: BinaryAssociation = BinaryAssociation(
    name="type227",
    ends={
        Property(name="alf_QualifiedNameWithBinding229", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition228", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression196: BinaryAssociation = BinaryAssociation(
    name="expression196",
    ends={
        Property(name="alf_Expression198", type=alf_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchCase197", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementSequence199: BinaryAssociation = BinaryAssociation(
    name="statementSequence199",
    ends={
        Property(name="alf_NonEmptyStatementSequence201", type=alf_SwitchDefaultClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SwitchDefaultClause200", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement202: BinaryAssociation = BinaryAssociation(
    name="statement202",
    ends={
        Property(name="alf_DocumentedStatement204", type=alf_NonEmptyStatementSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_NonEmptyStatementSequence203", type=alf_DocumentedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition205: BinaryAssociation = BinaryAssociation(
    name="condition205",
    ends={
        Property(name="alf_Expression206", type=alf_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_WhileStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block207: BinaryAssociation = BinaryAssociation(
    name="block207",
    ends={
        Property(name="alf_Block209", type=alf_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_WhileStatement208", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block210: BinaryAssociation = BinaryAssociation(
    name="block210",
    ends={
        Property(name="alf_Block211", type=alf_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DoStatement", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition212: BinaryAssociation = BinaryAssociation(
    name="condition212",
    ends={
        Property(name="alf_Expression214", type=alf_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_DoStatement213", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acceptBlock243: BinaryAssociation = BinaryAssociation(
    name="acceptBlock243",
    ends={
        Property(name="alf_AcceptBlock", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_CompoundAcceptStatementCompletion244", type=alf_AcceptBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause245: BinaryAssociation = BinaryAssociation(
    name="clause245",
    ends={
        Property(name="alf_AcceptClause247", type=alf_AcceptBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptBlock246", type=alf_AcceptClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block248: BinaryAssociation = BinaryAssociation(
    name="block248",
    ends={
        Property(name="alf_Block250", type=alf_AcceptBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptBlock249", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList251: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList251",
    ends={
        Property(name="alf_QualifiedNameList", type=alf_AcceptClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptClause252", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression253: BinaryAssociation = BinaryAssociation(
    name="expression253",
    ends={
        Property(name="alf_Expression254", type=alf_ClassifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifyStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clause255: BinaryAssociation = BinaryAssociation(
    name="clause255",
    ends={
        Property(name="alf_ClassificationClause", type=alf_ClassifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassifyStatement256", type=alf_ClassificationClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression230: BinaryAssociation = BinaryAssociation(
    name="expression230",
    ends={
        Property(name="alf_Expression232", type=alf_LoopVariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_LoopVariableDefinition231", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression233: BinaryAssociation = BinaryAssociation(
    name="expression233",
    ends={
        Property(name="alf_Expression234", type=alf_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ReturnStatement", type=alf_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clause235: BinaryAssociation = BinaryAssociation(
    name="clause235",
    ends={
        Property(name="alf_AcceptClause", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement", type=alf_AcceptClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleAccept236: BinaryAssociation = BinaryAssociation(
    name="simpleAccept236",
    ends={
        Property(name="alf_SimpleAcceptStatementCompletion", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement237", type=alf_SimpleAcceptStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compoundAccept238: BinaryAssociation = BinaryAssociation(
    name="compoundAccept238",
    ends={
        Property(name="alf_CompoundAcceptStatementCompletion", type=alf_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AcceptStatement239", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block240: BinaryAssociation = BinaryAssociation(
    name="block240",
    ends={
        Property(name="alf_Block242", type=alf_CompoundAcceptStatementCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_CompoundAcceptStatementCompletion241", type=alf_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarationCompletion274: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationCompletion274",
    ends={
        Property(name="alf_VariableDeclarationCompletion", type=alf_InvocationOrAssignementOrDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InvocationOrAssignementOrDeclarationStatement275", type=alf_VariableDeclarationCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignmentCompletion276: BinaryAssociation = BinaryAssociation(
    name="assignmentCompletion276",
    ends={
        Property(name="alf_AssignmentCompletion278", type=alf_InvocationOrAssignementOrDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InvocationOrAssignementOrDeclarationStatement277", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
_super279: BinaryAssociation = BinaryAssociation(
    name="_super279",
    ends={
        Property(name="alf_SuperInvocationExpression280", type=alf_SuperInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_SuperInvocationStatement", type=alf_SuperInvocationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
_this281: BinaryAssociation = BinaryAssociation(
    name="_this281",
    ends={
        Property(name="alf_ThisExpression282", type=alf_ThisInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisInvocationStatement", type=alf_ThisExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignmentCompletion283: BinaryAssociation = BinaryAssociation(
    name="assignmentCompletion283",
    ends={
        Property(name="alf_AssignmentCompletion285", type=alf_ThisInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ThisInvocationStatement284", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
_new286: BinaryAssociation = BinaryAssociation(
    name="_new286",
    ends={
        Property(name="alf_InstanceCreationExpression287", type=alf_InstanceCreationInvocationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InstanceCreationInvocationStatement", type=alf_InstanceCreationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifyFromClause257: BinaryAssociation = BinaryAssociation(
    name="classifyFromClause257",
    ends={
        Property(name="alf_ClassificationFromClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause258", type=alf_ClassificationFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifyToClause259: BinaryAssociation = BinaryAssociation(
    name="classifyToClause259",
    ends={
        Property(name="alf_ClassificationToClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause260", type=alf_ClassificationToClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reclassyAllClause261: BinaryAssociation = BinaryAssociation(
    name="reclassyAllClause261",
    ends={
        Property(name="alf_ReclassifyAllClause", type=alf_ClassificationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationClause262", type=alf_ReclassifyAllClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList263: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList263",
    ends={
        Property(name="alf_QualifiedNameList265", type=alf_ClassificationFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationFromClause264", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedNameList266: BinaryAssociation = BinaryAssociation(
    name="qualifiedNameList266",
    ends={
        Property(name="alf_QualifiedNameList268", type=alf_ClassificationToClause, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_ClassificationToClause267", type=alf_QualifiedNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedName269: BinaryAssociation = BinaryAssociation(
    name="qualifiedName269",
    ends={
        Property(name="alf_QualifiedNameWithBinding271", type=alf_QualifiedNameList, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_QualifiedNameList270", type=alf_QualifiedNameWithBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typePart_OR_assignedPart_OR_invocationPart272: BinaryAssociation = BinaryAssociation(
    name="typePart_OR_assignedPart_OR_invocationPart272",
    ends={
        Property(name="alf_NameExpression273", type=alf_InvocationOrAssignementOrDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_InvocationOrAssignementOrDeclarationStatement", type=alf_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initValue288: BinaryAssociation = BinaryAssociation(
    name="initValue288",
    ends={
        Property(name="alf_AssignmentCompletion290", type=alf_VariableDeclarationCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_VariableDeclarationCompletion289", type=alf_AssignmentCompletion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightHandSide291: BinaryAssociation = BinaryAssociation(
    name="rightHandSide291",
    ends={
        Property(name="alf_SequenceElement293", type=alf_AssignmentCompletion, multiplicity=Multiplicity(1, 1)),
        Property(name="alf_AssignmentCompletion292", type=alf_SequenceElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
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
gen_alf_SequenceReductionExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_SequenceReductionExpression)
gen_alf_SequenceExpansionExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_SequenceExpansionExpression)
gen_alf_SequenceOperationExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_SequenceOperationExpression)
gen_alf_ParenthesizedExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_ParenthesizedExpression)
gen_alf_NullExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_NullExpression)
gen_alf_ThisExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_ThisExpression)
gen_alf_ThisExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_ThisExpression)
gen_alf_SuperInvocationExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_SuperInvocationExpression)
gen_alf_SuperInvocationExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_SuperInvocationExpression)
gen_alf_SelectOrRejectOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_SelectOrRejectOperation)
gen_alf_CollectOrIterateOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_CollectOrIterateOperation)
gen_alf_ForAllOrExistsOrOneOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_ForAllOrExistsOrOneOperation)
gen_alf_IsUniqueOperation_SequenceExpansionExpression = Generalization(general=SequenceExpansionExpression, specific=alf_IsUniqueOperation)
gen_alf_ParenthesizedExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_ParenthesizedExpression)
gen_alf_SequenceConstructionExpression_SequenceElement = Generalization(general=SequenceElement, specific=alf_SequenceConstructionExpression)
gen_alf_ClassExtentExpression_SuffixExpression = Generalization(general=SuffixExpression, specific=alf_ClassExtentExpression)
gen_alf_InstanceCreationExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=alf_InstanceCreationExpression)
gen_alf_InstanceCreationExpression_NonLiteralValueSpecification = Generalization(general=NonLiteralValueSpecification, specific=alf_InstanceCreationExpression)
gen_alf_BlockStatement_Statement = Generalization(general=Statement, specific=alf_BlockStatement)
gen_alf_EmptyStatement_Statement = Generalization(general=Statement, specific=alf_EmptyStatement)
gen_alf_LocalNameDeclarationStatement_Statement = Generalization(general=Statement, specific=alf_LocalNameDeclarationStatement)
gen_alf_InlineStatement_Statement = Generalization(general=Statement, specific=alf_InlineStatement)
gen_alf_AnnotatedStatement_Statement = Generalization(general=Statement, specific=alf_AnnotatedStatement)
gen_alf_SwitchStatement_Statement = Generalization(general=Statement, specific=alf_SwitchStatement)
gen_alf_IfStatement_Statement = Generalization(general=Statement, specific=alf_IfStatement)
gen_alf_ForStatement_Statement = Generalization(general=Statement, specific=alf_ForStatement)
gen_alf_WhileStatement_Statement = Generalization(general=Statement, specific=alf_WhileStatement)
gen_alf_DoStatement_Statement = Generalization(general=Statement, specific=alf_DoStatement)
gen_alf_ClassifyStatement_Statement = Generalization(general=Statement, specific=alf_ClassifyStatement)
gen_alf_BreakStatement_Statement = Generalization(general=Statement, specific=alf_BreakStatement)
gen_alf_ReturnStatement_Statement = Generalization(general=Statement, specific=alf_ReturnStatement)
gen_alf_AcceptStatement_Statement = Generalization(general=Statement, specific=alf_AcceptStatement)
gen_alf_SuperInvocationStatement_Statement = Generalization(general=Statement, specific=alf_SuperInvocationStatement)
gen_alf_ThisInvocationStatement_Statement = Generalization(general=Statement, specific=alf_ThisInvocationStatement)
gen_alf_InstanceCreationInvocationStatement_Statement = Generalization(general=Statement, specific=alf_InstanceCreationInvocationStatement)
gen_alf_InvocationOrAssignementOrDeclarationStatement_Statement = Generalization(general=Statement, specific=alf_InvocationOrAssignementOrDeclarationStatement)

# Domain Model
domain_model = DomainModel(
    name="alf",
    types={alf_Block, alf_LITERAL, ValueSpecification, alf_BOOLEAN_LITERAL, LITERAL, alf_NUMBER_LITERAL, alf_INTEGER_LITERAL, NUMBER_LITERAL, alf_UNLIMITED_LITERAL, alf_STRING_LITERAL, alf_Test, alf_Expression, alf_AssignmentCompletion, alf_Statement, alf_NamedTemplateBinding, alf_QualifiedNameWithBinding, alf_TupleElement, alf_NameExpression, NonLiteralValueSpecification, alf_QualifiedNamePath, alf_Tuple, alf_SequenceConstructionOrAccessCompletion, alf_SuffixExpression, alf_UnqualifiedName, alf_TemplateBinding, alf_EqualityExpression, alf_ClassificationExpression, alf_RelationalExpression, alf_ShiftExpression, SequenceElement, alf_ConditionalTestExpression, Expression, alf_ConditionalOrExpression, alf_ConditionalAndExpression, alf_InclusiveOrExpression, alf_ExclusiveOrExpression, alf_AndExpression, alf_OperationCallExpression, SuffixExpression, alf_PropertyCallExpression, alf_LinkOperationExpression, alf_LinkOperationTuple, alf_AdditiveExpression, alf_MultiplicativeExpression, alf_UnaryExpression, alf_PrimaryExpression, alf_ValueSpecification, alf_SequenceReductionExpression, alf_SequenceExpansionExpression, alf_LinkOperationTupleElement, alf_SequenceOperationExpression, alf_NullExpression, alf_ThisExpression, alf_SuperInvocationExpression, alf_SelectOrRejectOperation, SequenceExpansionExpression, alf_CollectOrIterateOperation, alf_ForAllOrExistsOrOneOperation, alf_IsUniqueOperation, alf_NonLiteralValueSpecification, alf_ParenthesizedExpression, alf_PartialSequenceConstructionCompletion, alf_SequenceConstructionExpression, alf_SequenceElement, alf_ClassExtentExpression, alf_InstanceCreationExpression, alf_InstanceCreationTuple, alf_InstanceCreationTupleElement, alf_AccessCompletion, alf_BlockStatement, alf_EmptyStatement, alf_LocalNameDeclarationStatement, alf_StatementSequence, alf_DocumentedStatement, alf_InlineStatement, Statement, alf_AnnotatedStatement, alf_Annotation, alf_SwitchStatement, alf_SwitchClause, alf_SwitchDefaultClause, alf_SwitchCase, alf_NonEmptyStatementSequence, alf_IfStatement, alf_SequentialClauses, alf_FinalClause, alf_ConcurrentClauses, alf_NonFinalClause, alf_ForStatement, alf_ForControl, alf_LoopVariableDefinition, alf_WhileStatement, alf_DoStatement, alf_AcceptBlock, alf_QualifiedNameList, alf_ClassifyStatement, alf_ClassificationClause, alf_BreakStatement, alf_ReturnStatement, alf_AcceptStatement, alf_AcceptClause, alf_SimpleAcceptStatementCompletion, alf_CompoundAcceptStatementCompletion, alf_VariableDeclarationCompletion, alf_SuperInvocationStatement, alf_ThisInvocationStatement, alf_InstanceCreationInvocationStatement, alf_ClassificationFromClause, alf_ClassificationToClause, alf_ReclassifyAllClause, alf_InvocationOrAssignementOrDeclarationStatement, BooleanValue, LinkOperationKind, SelectOrRejectOperator, CollectOrIterateOperator, ForAllOrExistsOrOneOperator, AnnotationKind, AssignmentOperator},
    associations={block5, expression0, assignExpression1, statements3, templateBinding16, bindings18, actual20, binding22, remaining26, tupleElements28, argument30, path7, invocationCompletion8, sequenceConstructionCompletion10, suffix12, namespace14, exp48, exp50, exp52, typeName54, left57, exp33, whenTrue35, whenFalse38, exp40, exp42, exp44, exp46, prefix70, tuple72, suffix74, index77, suffix79, right59, exp62, exp64, exp66, exp68, operationName91, tuple93, suffix96, behavior99, suffix101, expr104, suffix106, tuple82, linkOperationTupleElement83, roleIndex85, object88, expOrTypeCast109, casted111, suffix113, suffix116, tuple118, sequenceCompletion137, expression139, accessIndex141, expression144, sequenceElement147, rangeUpper149, operationName120, constructor123, tuple125, suffix127, instanceCreationTupleElement130, object132, accessCompletion135, block163, type165, init167, sequence152, statements154, statement156, annotation159, statement160, block183, expression186, switchClause188, defaultClause190, switchCase192, statementSequence194, sequentialClausses170, finalClause171, conccurentClauses173, nonFinalClause175, condition177, block180, control215, block216, loopVariableDefinition219, expression1221, expression2224, type227, expression196, statementSequence199, statement202, condition205, block207, block210, condition212, acceptBlock243, clause245, block248, qualifiedNameList251, expression253, clause255, expression230, expression233, clause235, simpleAccept236, compoundAccept238, block240, variableDeclarationCompletion274, assignmentCompletion276, _super279, _this281, assignmentCompletion283, _new286, classifyFromClause257, classifyToClause259, reclassyAllClause261, qualifiedNameList263, qualifiedNameList266, qualifiedName269, typePart_OR_assignedPart_OR_invocationPart272, initValue288, rightHandSide291},
    generalizations={gen_alf_LITERAL_ValueSpecification, gen_alf_BOOLEAN_LITERAL_LITERAL, gen_alf_NUMBER_LITERAL_LITERAL, gen_alf_INTEGER_LITERAL_NUMBER_LITERAL, gen_alf_UNLIMITED_LITERAL_NUMBER_LITERAL, gen_alf_STRING_LITERAL_LITERAL, gen_alf_NameExpression_ValueSpecification, gen_alf_NameExpression_NonLiteralValueSpecification, gen_alf_Expression_SequenceElement, gen_alf_ConditionalTestExpression_Expression, gen_alf_OperationCallExpression_SuffixExpression, gen_alf_PropertyCallExpression_SuffixExpression, gen_alf_LinkOperationExpression_SuffixExpression, gen_alf_SequenceReductionExpression_SuffixExpression, gen_alf_SequenceExpansionExpression_SuffixExpression, gen_alf_SequenceOperationExpression_SuffixExpression, gen_alf_ParenthesizedExpression_NonLiteralValueSpecification, gen_alf_NullExpression_ValueSpecification, gen_alf_ThisExpression_ValueSpecification, gen_alf_ThisExpression_NonLiteralValueSpecification, gen_alf_SuperInvocationExpression_ValueSpecification, gen_alf_SuperInvocationExpression_NonLiteralValueSpecification, gen_alf_SelectOrRejectOperation_SequenceExpansionExpression, gen_alf_CollectOrIterateOperation_SequenceExpansionExpression, gen_alf_ForAllOrExistsOrOneOperation_SequenceExpansionExpression, gen_alf_IsUniqueOperation_SequenceExpansionExpression, gen_alf_ParenthesizedExpression_ValueSpecification, gen_alf_SequenceConstructionExpression_SequenceElement, gen_alf_ClassExtentExpression_SuffixExpression, gen_alf_InstanceCreationExpression_ValueSpecification, gen_alf_InstanceCreationExpression_NonLiteralValueSpecification, gen_alf_BlockStatement_Statement, gen_alf_EmptyStatement_Statement, gen_alf_LocalNameDeclarationStatement_Statement, gen_alf_InlineStatement_Statement, gen_alf_AnnotatedStatement_Statement, gen_alf_SwitchStatement_Statement, gen_alf_IfStatement_Statement, gen_alf_ForStatement_Statement, gen_alf_WhileStatement_Statement, gen_alf_DoStatement_Statement, gen_alf_ClassifyStatement_Statement, gen_alf_BreakStatement_Statement, gen_alf_ReturnStatement_Statement, gen_alf_AcceptStatement_Statement, gen_alf_SuperInvocationStatement_Statement, gen_alf_ThisInvocationStatement_Statement, gen_alf_InstanceCreationInvocationStatement_Statement, gen_alf_InvocationOrAssignementOrDeclarationStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)