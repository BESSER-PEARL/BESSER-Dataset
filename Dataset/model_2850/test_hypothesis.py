import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    alf_AcceptClause,
    alf_ReclassifyAllClause,
    alf_ClassificationToClause,
    alf_ClassificationFromClause,
    alf_ClassificationClause,
    alf_AcceptBlock,
    alf_CompoundAcceptStatementCompletion,
    alf_SimpleAcceptStatementCompletion,
    alf_NonEmptyStatementSequence,
    alf_SwitchCase,
    alf_SwitchDefaultClause,
    alf_SwitchClause,
    alf_LoopVariableDefinition,
    alf_ForControl,
    alf_LocalNameDeclarationStatementCompletion,
    alf_NonFinalClause,
    alf_ConcurrentClauses,
    alf_FinalClause,
    alf_SequentialClauses,
    alf_NameList,
    alf_Annotation,
    alf_ConditionalExpression,
    alf_ConditionalOrExpressionCompletion,
    alf_ConditionalOrExpression,
    alf_Annotations,
    Statement,
    alf_WhileStatement,
    alf_BlockStatement,
    alf_InLineStatement,
    alf_DoStatement,
    alf_LocalNameDeclarationOrExpressionStatement,
    alf_AcceptStatement,
    alf_BreakStatement,
    alf_ForStatement,
    alf_LocalNameDeclarationStatement,
    alf_IfStatement,
    alf_EmptyStatement,
    alf_ClassifyStatement,
    alf_ReturnStatement,
    alf_SwitchStatement,
    alf_AnnotatedStatement,
    alf_Statement,
    alf_DocumentedStatement,
    alf_StatementSequence,
    ExpressionCompletion,
    alf_AssignmentExpressionCompletion,
    alf_ConditionalExpressionCompletion,
    alf_AndExpression,
    alf_EqualityExpressionCompletion,
    alf_ConditionalAndExpressionCompletion,
    alf_ConditionalAndExpression,
    alf_InclusiveOrExpressionCompletion,
    alf_InclusiveOrExpression,
    alf_ExclusiveOrExpressionCompletion,
    alf_ExclusiveOrExpression,
    alf_AndExpressionCompletion,
    alf_ShiftExpressionCompletion,
    alf_ShiftExpression,
    alf_EqualityExpression,
    alf_ClassificationExpressionCompletion,
    alf_ClassificationExpression,
    alf_RelationalExpressionCompletion,
    alf_RelationalExpression,
    alf_AdditiveExpressionCompletion,
    alf_AdditiveExpression,
    alf_MultiplicativeExpressionCompletion,
    alf_MultiplicativeExpression,
    alf_CastCompletion,
    NonNameUnaryExpression,
    alf_NonNamePostfixOrCastExpression,
    CastCompletion,
    UnaryExpression,
    alf_NonPostfixNonCastUnaryExpression,
    alf_PostfixOrCastExpression,
    NonPostfixNonCastUnaryExpression,
    alf_BitStringComplementExpression,
    alf_NumericUnaryExpression,
    alf_IsolationExpression,
    alf_BooleanNegationExpression,
    alf_PrefixExpression,
    alf_PostfixOperation,
    alf_EObject,
    alf_SequenceElement,
    alf_SequenceElementListCompletion,
    alf_SequenceElements,
    alf_MultiplicityIndicator,
    alf_IndexedNamedExpression,
    alf_IndexedNamedExpressionListCompletion,
    alf_LinkOperationTuple,
    BaseExpression,
    alf_InstanceCreationOrSequenceConstructionExpression,
    alf_SuperInvocationExpression,
    alf_SequenceAnyExpression,
    alf_LiteralExpression,
    alf_Index,
    alf_NamedExpression,
    alf_PositionalTupleExpressionListCompletion,
    alf_PositionalTupleExpressionList,
    alf_NamedTupleExpressionList,
    alf_Tuple,
    alf_ThisExpression,
    alf_ExpressionCompletion,
    alf_UnaryExpression,
    InitializationExpression,
    alf_InstanceInitializationExpression,
    alf_SequenceInitializationExpression,
    alf_Expression,
    alf_SequenceOperationOrReductionOrExpansion,
    alf_FeatureInvocation,
    alf_Feature,
    alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index,
    alf_BehaviorInvocation,
    alf_SequenceConstructionExpressionCompletion,
    alf_ClassExtentExpressionCompletion,
    alf_LinkOperationCompletion,
    alf_PrimaryExpressionCompletion,
    alf_ParenthesizedExpression,
    alf_BaseExpression,
    alf_NameOrPrimaryExpression,
    alf_PrimaryExpression,
    alf_PostfixExpressionCompletion,
    alf_PrimaryToExpressionCompletion,
    alf_NameToPrimaryExpression,
    alf_NameToExpressionCompletion,
    alf_NonNameUnaryExpression,
    alf_NonNameExpression,
    alf_SignalReceptionDeclaration,
    alf_TemplateParameterSubstitution,
    TemplateBinding,
    alf_NamedTemplateBinding,
    alf_PositionalTemplateBinding,
    alf_ColonQualifiedNameCompletionWithoutBinding,
    alf_QualifiedNameWithoutBinding,
    alf_TemplateBinding,
    UnqualifiedName,
    alf_NameBinding,
    alf_ColonQualifiedNameCompletion,
    alf_UnqualifiedName,
    alf_InitializationExpression,
    ActiveFeatureDefinitionOrStub,
    alf_SignalReceptionDefinitionOrStub,
    alf_ReceptionDefinition,
    alf_AttributeInitializer,
    alf_RedefinitionClause,
    OperationDefinitionOrStub,
    alf_OperationDeclaration,
    alf_UnlimitedNaturalLiteral,
    alf_MultiplicityRange,
    alf_Multiplicity,
    alf_TypeName,
    alf_TypePart,
    alf_FormalParameters,
    FeatureDefinitionOrStub,
    alf_OperationDefinitionOrStub,
    alf_AttributeDefinition,
    alf_PropertyDeclaration,
    alf_FormalParameter,
    alf_FormalParameterList,
    alf_AssociationDeclaration,
    alf_PropertyDefinition,
    alf_ActivityDeclaration,
    alf_SignalDeclaration,
    alf_EnumerationLiteralName,
    alf_EnumerationBody,
    alf_EnumerationDeclaration,
    alf_ActiveClassBody,
    alf_StructuredMember,
    alf_StructuredBody,
    alf_DataTypeDeclaration,
    alf_ActiveClassMemberDefinition,
    alf_Block,
    alf_BehaviorClause,
    alf_ActiveClassMember,
    alf_PackagedElementDefinition,
    alf_ActiveClassDeclaration,
    alf_PackagedElement,
    ActiveClassMemberDefinition,
    alf_ActiveFeatureDefinitionOrStub,
    alf_ClassMemberDefinition,
    alf_ClassMember,
    ClassifierDefinitionOrStub,
    alf_ActivityDefinitionOrStub,
    alf_AssociationDefinitionOrStub,
    alf_ActiveClassDefinitionOrStub,
    alf_DataTypeDefinitionOrStub,
    alf_SignalDefinitionOrStub,
    alf_EnumerationDefinitionOrStub,
    alf_ClassDefinitionOrStub,
    alf_ClassBody,
    ClassifierDefinition,
    alf_SignalDefinition,
    alf_DataTypeDefinition,
    alf_ActivityDefinition,
    alf_EnumerationDefinition,
    alf_ActiveClassDefinition,
    alf_AssociationDefinition,
    alf_ClassDefinition,
    alf_ClassDeclaration,
    alf_ClassifierTemplateParameter,
    alf_SpecializationClause,
    PackagedElementDefinition,
    alf_PackageDefinitionOrStub,
    alf_TemplateParameters,
    alf_PackageBody,
    alf_ClassifierSignature,
    ClassMemberDefinition,
    alf_ClassifierDefinitionOrStub,
    alf_FeatureDefinitionOrStub,
    NamespaceDefinition,
    alf_ClassifierDefinition,
    alf_PackageDefinition,
    alf_PackageDeclaration,
    alf_VisibilityIndicator,
    ImportReferenceQualifiedNameCompletion,
    alf_ColonQualifiedNameCompletionOfImportReference,
    alf_AliasDefinition,
    alf_ImportReferenceQualifiedNameCompletion,
    alf_Name,
    alf_PRIMITIVE_LITERAL,
    alf_TaggedValue,
    TaggedValues,
    alf_QualifiedNameList,
    alf_TaggedValueList,
    alf_TaggedValues,
    alf_QualifiedName,
    alf_StereotypeAnnotation,
    NUMBER_LITERAL,
    alf_UNLIMITED_NATURAL,
    alf_INTEGER_LITERAL,
    PRIMITIVE_LITERAL,
    alf_STRING_LITERAL,
    alf_NUMBER_LITERAL,
    alf_BOOLEAN_LITERAL,
    alf_NamespaceDefinition,
    alf_StereotypeAnnotations,
    alf_ImportDeclaration,
    alf_NamespaceDeclaration,
    alf_UnitDefinition,
    alf_ImportReference,
    MultiplicativeOperator,
    LinkOperation,
    ShiftOperator,
    AffixOperator,
    RelationalOperator,
    EqualityOperator,
    AssignmentOperator,
    AdditiveOperator,
    ImportVisibilityIndicator,
    ParameterDirection,
    NumericUnaryOperator,
    ClassificationOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_alf_acceptclause_is_not_abstract():
    assert not inspect.isabstract(alf_AcceptClause)


def test_alf_acceptclause_constructor_exists():
    assert callable(alf_AcceptClause.__init__)


def test_alf_acceptclause_constructor_args():
    sig = inspect.signature(alf_AcceptClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_reclassifyallclause_is_not_abstract():
    assert not inspect.isabstract(alf_ReclassifyAllClause)


def test_alf_reclassifyallclause_constructor_exists():
    assert callable(alf_ReclassifyAllClause.__init__)


def test_alf_reclassifyallclause_constructor_args():
    sig = inspect.signature(alf_ReclassifyAllClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_classificationtoclause_is_not_abstract():
    assert not inspect.isabstract(alf_ClassificationToClause)


def test_alf_classificationtoclause_constructor_exists():
    assert callable(alf_ClassificationToClause.__init__)


def test_alf_classificationtoclause_constructor_args():
    sig = inspect.signature(alf_ClassificationToClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_classificationfromclause_is_not_abstract():
    assert not inspect.isabstract(alf_ClassificationFromClause)


def test_alf_classificationfromclause_constructor_exists():
    assert callable(alf_ClassificationFromClause.__init__)


def test_alf_classificationfromclause_constructor_args():
    sig = inspect.signature(alf_ClassificationFromClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_classificationclause_is_not_abstract():
    assert not inspect.isabstract(alf_ClassificationClause)


def test_alf_classificationclause_constructor_exists():
    assert callable(alf_ClassificationClause.__init__)


def test_alf_classificationclause_constructor_args():
    sig = inspect.signature(alf_ClassificationClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_acceptblock_is_not_abstract():
    assert not inspect.isabstract(alf_AcceptBlock)


def test_alf_acceptblock_constructor_exists():
    assert callable(alf_AcceptBlock.__init__)


def test_alf_acceptblock_constructor_args():
    sig = inspect.signature(alf_AcceptBlock.__init__)
    params = list(sig.parameters.keys())



def test_alf_compoundacceptstatementcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_CompoundAcceptStatementCompletion)


def test_alf_compoundacceptstatementcompletion_constructor_exists():
    assert callable(alf_CompoundAcceptStatementCompletion.__init__)


def test_alf_compoundacceptstatementcompletion_constructor_args():
    sig = inspect.signature(alf_CompoundAcceptStatementCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_simpleacceptstatementcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_SimpleAcceptStatementCompletion)


def test_alf_simpleacceptstatementcompletion_constructor_exists():
    assert callable(alf_SimpleAcceptStatementCompletion.__init__)


def test_alf_simpleacceptstatementcompletion_constructor_args():
    sig = inspect.signature(alf_SimpleAcceptStatementCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonemptystatementsequence_is_not_abstract():
    assert not inspect.isabstract(alf_NonEmptyStatementSequence)


def test_alf_nonemptystatementsequence_constructor_exists():
    assert callable(alf_NonEmptyStatementSequence.__init__)


def test_alf_nonemptystatementsequence_constructor_args():
    sig = inspect.signature(alf_NonEmptyStatementSequence.__init__)
    params = list(sig.parameters.keys())



def test_alf_switchcase_is_not_abstract():
    assert not inspect.isabstract(alf_SwitchCase)


def test_alf_switchcase_constructor_exists():
    assert callable(alf_SwitchCase.__init__)


def test_alf_switchcase_constructor_args():
    sig = inspect.signature(alf_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_alf_switchdefaultclause_is_not_abstract():
    assert not inspect.isabstract(alf_SwitchDefaultClause)


def test_alf_switchdefaultclause_constructor_exists():
    assert callable(alf_SwitchDefaultClause.__init__)


def test_alf_switchdefaultclause_constructor_args():
    sig = inspect.signature(alf_SwitchDefaultClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_switchclause_is_not_abstract():
    assert not inspect.isabstract(alf_SwitchClause)


def test_alf_switchclause_constructor_exists():
    assert callable(alf_SwitchClause.__init__)


def test_alf_switchclause_constructor_args():
    sig = inspect.signature(alf_SwitchClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_loopvariabledefinition_is_not_abstract():
    assert not inspect.isabstract(alf_LoopVariableDefinition)


def test_alf_loopvariabledefinition_constructor_exists():
    assert callable(alf_LoopVariableDefinition.__init__)


def test_alf_loopvariabledefinition_constructor_args():
    sig = inspect.signature(alf_LoopVariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_forcontrol_is_not_abstract():
    assert not inspect.isabstract(alf_ForControl)


def test_alf_forcontrol_constructor_exists():
    assert callable(alf_ForControl.__init__)


def test_alf_forcontrol_constructor_args():
    sig = inspect.signature(alf_ForControl.__init__)
    params = list(sig.parameters.keys())



def test_alf_localnamedeclarationstatementcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_LocalNameDeclarationStatementCompletion)


def test_alf_localnamedeclarationstatementcompletion_constructor_exists():
    assert callable(alf_LocalNameDeclarationStatementCompletion.__init__)


def test_alf_localnamedeclarationstatementcompletion_constructor_args():
    sig = inspect.signature(alf_LocalNameDeclarationStatementCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonfinalclause_is_not_abstract():
    assert not inspect.isabstract(alf_NonFinalClause)


def test_alf_nonfinalclause_constructor_exists():
    assert callable(alf_NonFinalClause.__init__)


def test_alf_nonfinalclause_constructor_args():
    sig = inspect.signature(alf_NonFinalClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_concurrentclauses_is_not_abstract():
    assert not inspect.isabstract(alf_ConcurrentClauses)


def test_alf_concurrentclauses_constructor_exists():
    assert callable(alf_ConcurrentClauses.__init__)


def test_alf_concurrentclauses_constructor_args():
    sig = inspect.signature(alf_ConcurrentClauses.__init__)
    params = list(sig.parameters.keys())



def test_alf_finalclause_is_not_abstract():
    assert not inspect.isabstract(alf_FinalClause)


def test_alf_finalclause_constructor_exists():
    assert callable(alf_FinalClause.__init__)


def test_alf_finalclause_constructor_args():
    sig = inspect.signature(alf_FinalClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequentialclauses_is_not_abstract():
    assert not inspect.isabstract(alf_SequentialClauses)


def test_alf_sequentialclauses_constructor_exists():
    assert callable(alf_SequentialClauses.__init__)


def test_alf_sequentialclauses_constructor_args():
    sig = inspect.signature(alf_SequentialClauses.__init__)
    params = list(sig.parameters.keys())



def test_alf_namelist_is_not_abstract():
    assert not inspect.isabstract(alf_NameList)


def test_alf_namelist_constructor_exists():
    assert callable(alf_NameList.__init__)


def test_alf_namelist_constructor_args():
    sig = inspect.signature(alf_NameList.__init__)
    params = list(sig.parameters.keys())



def test_alf_annotation_is_not_abstract():
    assert not inspect.isabstract(alf_Annotation)


def test_alf_annotation_constructor_exists():
    assert callable(alf_Annotation.__init__)


def test_alf_annotation_constructor_args():
    sig = inspect.signature(alf_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf_annotation_has_id():
    assert hasattr(alf_Annotation, "id")
    descriptor = None
    for klass in alf_Annotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalExpression)


def test_alf_conditionalexpression_constructor_exists():
    assert callable(alf_ConditionalExpression.__init__)


def test_alf_conditionalexpression_constructor_args():
    sig = inspect.signature(alf_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_conditionalorexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalOrExpressionCompletion)


def test_alf_conditionalorexpressioncompletion_constructor_exists():
    assert callable(alf_ConditionalOrExpressionCompletion.__init__)


def test_alf_conditionalorexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ConditionalOrExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalOrExpression)


def test_alf_conditionalorexpression_constructor_exists():
    assert callable(alf_ConditionalOrExpression.__init__)


def test_alf_conditionalorexpression_constructor_args():
    sig = inspect.signature(alf_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_annotations_is_not_abstract():
    assert not inspect.isabstract(alf_Annotations)


def test_alf_annotations_constructor_exists():
    assert callable(alf_Annotations.__init__)


def test_alf_annotations_constructor_args():
    sig = inspect.signature(alf_Annotations.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf_whilestatement_is_not_abstract():
    assert not inspect.isabstract(alf_WhileStatement)


def test_alf_whilestatement_constructor_exists():
    assert callable(alf_WhileStatement.__init__)


def test_alf_whilestatement_constructor_args():
    sig = inspect.signature(alf_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_blockstatement_is_not_abstract():
    assert not inspect.isabstract(alf_BlockStatement)


def test_alf_blockstatement_constructor_exists():
    assert callable(alf_BlockStatement.__init__)


def test_alf_blockstatement_constructor_args():
    sig = inspect.signature(alf_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_inlinestatement_is_not_abstract():
    assert not inspect.isabstract(alf_InLineStatement)


def test_alf_inlinestatement_constructor_exists():
    assert callable(alf_InLineStatement.__init__)


def test_alf_inlinestatement_constructor_args():
    sig = inspect.signature(alf_InLineStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf_inlinestatement_has_id():
    assert hasattr(alf_InLineStatement, "id")
    descriptor = None
    for klass in alf_InLineStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf_dostatement_is_not_abstract():
    assert not inspect.isabstract(alf_DoStatement)


def test_alf_dostatement_constructor_exists():
    assert callable(alf_DoStatement.__init__)


def test_alf_dostatement_constructor_args():
    sig = inspect.signature(alf_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_localnamedeclarationorexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(alf_LocalNameDeclarationOrExpressionStatement)


def test_alf_localnamedeclarationorexpressionstatement_constructor_exists():
    assert callable(alf_LocalNameDeclarationOrExpressionStatement.__init__)


def test_alf_localnamedeclarationorexpressionstatement_constructor_args():
    sig = inspect.signature(alf_LocalNameDeclarationOrExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_acceptstatement_is_not_abstract():
    assert not inspect.isabstract(alf_AcceptStatement)


def test_alf_acceptstatement_constructor_exists():
    assert callable(alf_AcceptStatement.__init__)


def test_alf_acceptstatement_constructor_args():
    sig = inspect.signature(alf_AcceptStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_breakstatement_is_not_abstract():
    assert not inspect.isabstract(alf_BreakStatement)


def test_alf_breakstatement_constructor_exists():
    assert callable(alf_BreakStatement.__init__)


def test_alf_breakstatement_constructor_args():
    sig = inspect.signature(alf_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_forstatement_is_not_abstract():
    assert not inspect.isabstract(alf_ForStatement)


def test_alf_forstatement_constructor_exists():
    assert callable(alf_ForStatement.__init__)


def test_alf_forstatement_constructor_args():
    sig = inspect.signature(alf_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_localnamedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(alf_LocalNameDeclarationStatement)


def test_alf_localnamedeclarationstatement_constructor_exists():
    assert callable(alf_LocalNameDeclarationStatement.__init__)


def test_alf_localnamedeclarationstatement_constructor_args():
    sig = inspect.signature(alf_LocalNameDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_ifstatement_is_not_abstract():
    assert not inspect.isabstract(alf_IfStatement)


def test_alf_ifstatement_constructor_exists():
    assert callable(alf_IfStatement.__init__)


def test_alf_ifstatement_constructor_args():
    sig = inspect.signature(alf_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_emptystatement_is_not_abstract():
    assert not inspect.isabstract(alf_EmptyStatement)


def test_alf_emptystatement_constructor_exists():
    assert callable(alf_EmptyStatement.__init__)


def test_alf_emptystatement_constructor_args():
    sig = inspect.signature(alf_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_classifystatement_is_not_abstract():
    assert not inspect.isabstract(alf_ClassifyStatement)


def test_alf_classifystatement_constructor_exists():
    assert callable(alf_ClassifyStatement.__init__)


def test_alf_classifystatement_constructor_args():
    sig = inspect.signature(alf_ClassifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_returnstatement_is_not_abstract():
    assert not inspect.isabstract(alf_ReturnStatement)


def test_alf_returnstatement_constructor_exists():
    assert callable(alf_ReturnStatement.__init__)


def test_alf_returnstatement_constructor_args():
    sig = inspect.signature(alf_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_switchstatement_is_not_abstract():
    assert not inspect.isabstract(alf_SwitchStatement)


def test_alf_switchstatement_constructor_exists():
    assert callable(alf_SwitchStatement.__init__)


def test_alf_switchstatement_constructor_args():
    sig = inspect.signature(alf_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_annotatedstatement_is_not_abstract():
    assert not inspect.isabstract(alf_AnnotatedStatement)


def test_alf_annotatedstatement_constructor_exists():
    assert callable(alf_AnnotatedStatement.__init__)


def test_alf_annotatedstatement_constructor_args():
    sig = inspect.signature(alf_AnnotatedStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_statement_is_not_abstract():
    assert not inspect.isabstract(alf_Statement)


def test_alf_statement_constructor_exists():
    assert callable(alf_Statement.__init__)


def test_alf_statement_constructor_args():
    sig = inspect.signature(alf_Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf_documentedstatement_is_not_abstract():
    assert not inspect.isabstract(alf_DocumentedStatement)


def test_alf_documentedstatement_constructor_exists():
    assert callable(alf_DocumentedStatement.__init__)


def test_alf_documentedstatement_constructor_args():
    sig = inspect.signature(alf_DocumentedStatement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_documentedstatement_has_comment():
    assert hasattr(alf_DocumentedStatement, "comment")
    descriptor = None
    for klass in alf_DocumentedStatement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf_statementsequence_is_not_abstract():
    assert not inspect.isabstract(alf_StatementSequence)


def test_alf_statementsequence_constructor_exists():
    assert callable(alf_StatementSequence.__init__)


def test_alf_statementsequence_constructor_args():
    sig = inspect.signature(alf_StatementSequence.__init__)
    params = list(sig.parameters.keys())



def test_expressioncompletion_is_not_abstract():
    assert not inspect.isabstract(ExpressionCompletion)


def test_expressioncompletion_constructor_exists():
    assert callable(ExpressionCompletion.__init__)


def test_expressioncompletion_constructor_args():
    sig = inspect.signature(ExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_assignmentexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_AssignmentExpressionCompletion)


def test_alf_assignmentexpressioncompletion_constructor_exists():
    assert callable(alf_AssignmentExpressionCompletion.__init__)


def test_alf_assignmentexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_AssignmentExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_assignmentexpressioncompletion_has_operator():
    assert hasattr(alf_AssignmentExpressionCompletion, "operator")
    descriptor = None
    for klass in alf_AssignmentExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_conditionalexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalExpressionCompletion)


def test_alf_conditionalexpressioncompletion_constructor_exists():
    assert callable(alf_ConditionalExpressionCompletion.__init__)


def test_alf_conditionalexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ConditionalExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_andexpression_is_not_abstract():
    assert not inspect.isabstract(alf_AndExpression)


def test_alf_andexpression_constructor_exists():
    assert callable(alf_AndExpression.__init__)


def test_alf_andexpression_constructor_args():
    sig = inspect.signature(alf_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_equalityexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_EqualityExpressionCompletion)


def test_alf_equalityexpressioncompletion_constructor_exists():
    assert callable(alf_EqualityExpressionCompletion.__init__)


def test_alf_equalityexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_EqualityExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_equalityexpressioncompletion_has_operator():
    assert hasattr(alf_EqualityExpressionCompletion, "operator")
    descriptor = None
    for klass in alf_EqualityExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_conditionalandexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalAndExpressionCompletion)


def test_alf_conditionalandexpressioncompletion_constructor_exists():
    assert callable(alf_ConditionalAndExpressionCompletion.__init__)


def test_alf_conditionalandexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ConditionalAndExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalAndExpression)


def test_alf_conditionalandexpression_constructor_exists():
    assert callable(alf_ConditionalAndExpression.__init__)


def test_alf_conditionalandexpression_constructor_args():
    sig = inspect.signature(alf_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_inclusiveorexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_InclusiveOrExpressionCompletion)


def test_alf_inclusiveorexpressioncompletion_constructor_exists():
    assert callable(alf_InclusiveOrExpressionCompletion.__init__)


def test_alf_inclusiveorexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_InclusiveOrExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf_InclusiveOrExpression)


def test_alf_inclusiveorexpression_constructor_exists():
    assert callable(alf_InclusiveOrExpression.__init__)


def test_alf_inclusiveorexpression_constructor_args():
    sig = inspect.signature(alf_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_exclusiveorexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ExclusiveOrExpressionCompletion)


def test_alf_exclusiveorexpressioncompletion_constructor_exists():
    assert callable(alf_ExclusiveOrExpressionCompletion.__init__)


def test_alf_exclusiveorexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ExclusiveOrExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ExclusiveOrExpression)


def test_alf_exclusiveorexpression_constructor_exists():
    assert callable(alf_ExclusiveOrExpression.__init__)


def test_alf_exclusiveorexpression_constructor_args():
    sig = inspect.signature(alf_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_andexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_AndExpressionCompletion)


def test_alf_andexpressioncompletion_constructor_exists():
    assert callable(alf_AndExpressionCompletion.__init__)


def test_alf_andexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_AndExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_shiftexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ShiftExpressionCompletion)


def test_alf_shiftexpressioncompletion_constructor_exists():
    assert callable(alf_ShiftExpressionCompletion.__init__)


def test_alf_shiftexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ShiftExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_shiftexpressioncompletion_has_operator():
    assert hasattr(alf_ShiftExpressionCompletion, "operator")
    descriptor = None
    for klass in alf_ShiftExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ShiftExpression)


def test_alf_shiftexpression_constructor_exists():
    assert callable(alf_ShiftExpression.__init__)


def test_alf_shiftexpression_constructor_args():
    sig = inspect.signature(alf_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(alf_EqualityExpression)


def test_alf_equalityexpression_constructor_exists():
    assert callable(alf_EqualityExpression.__init__)


def test_alf_equalityexpression_constructor_args():
    sig = inspect.signature(alf_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_classificationexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ClassificationExpressionCompletion)


def test_alf_classificationexpressioncompletion_constructor_exists():
    assert callable(alf_ClassificationExpressionCompletion.__init__)


def test_alf_classificationexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ClassificationExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_classificationexpressioncompletion_has_operator():
    assert hasattr(alf_ClassificationExpressionCompletion, "operator")
    descriptor = None
    for klass in alf_ClassificationExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_classificationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ClassificationExpression)


def test_alf_classificationexpression_constructor_exists():
    assert callable(alf_ClassificationExpression.__init__)


def test_alf_classificationexpression_constructor_args():
    sig = inspect.signature(alf_ClassificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_relationalexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_RelationalExpressionCompletion)


def test_alf_relationalexpressioncompletion_constructor_exists():
    assert callable(alf_RelationalExpressionCompletion.__init__)


def test_alf_relationalexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_RelationalExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "relationalOperator" in params, "Missing parameter 'relationalOperator'"

def test_alf_relationalexpressioncompletion_has_relationalOperator():
    assert hasattr(alf_RelationalExpressionCompletion, "relationalOperator")
    descriptor = None
    for klass in alf_RelationalExpressionCompletion.__mro__:
        if "relationalOperator" in klass.__dict__:
            descriptor = klass.__dict__["relationalOperator"]
            break
    assert isinstance(descriptor, property)



def test_alf_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(alf_RelationalExpression)


def test_alf_relationalexpression_constructor_exists():
    assert callable(alf_RelationalExpression.__init__)


def test_alf_relationalexpression_constructor_args():
    sig = inspect.signature(alf_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_additiveexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_AdditiveExpressionCompletion)


def test_alf_additiveexpressioncompletion_constructor_exists():
    assert callable(alf_AdditiveExpressionCompletion.__init__)


def test_alf_additiveexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_AdditiveExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_additiveexpressioncompletion_has_operator():
    assert hasattr(alf_AdditiveExpressionCompletion, "operator")
    descriptor = None
    for klass in alf_AdditiveExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(alf_AdditiveExpression)


def test_alf_additiveexpression_constructor_exists():
    assert callable(alf_AdditiveExpression.__init__)


def test_alf_additiveexpression_constructor_args():
    sig = inspect.signature(alf_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_multiplicativeexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_MultiplicativeExpressionCompletion)


def test_alf_multiplicativeexpressioncompletion_constructor_exists():
    assert callable(alf_MultiplicativeExpressionCompletion.__init__)


def test_alf_multiplicativeexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_MultiplicativeExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_multiplicativeexpressioncompletion_has_operator():
    assert hasattr(alf_MultiplicativeExpressionCompletion, "operator")
    descriptor = None
    for klass in alf_MultiplicativeExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(alf_MultiplicativeExpression)


def test_alf_multiplicativeexpression_constructor_exists():
    assert callable(alf_MultiplicativeExpression.__init__)


def test_alf_multiplicativeexpression_constructor_args():
    sig = inspect.signature(alf_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_castcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_CastCompletion)


def test_alf_castcompletion_constructor_exists():
    assert callable(alf_CastCompletion.__init__)


def test_alf_castcompletion_constructor_args():
    sig = inspect.signature(alf_CastCompletion.__init__)
    params = list(sig.parameters.keys())



def test_nonnameunaryexpression_is_not_abstract():
    assert not inspect.isabstract(NonNameUnaryExpression)


def test_nonnameunaryexpression_constructor_exists():
    assert callable(NonNameUnaryExpression.__init__)


def test_nonnameunaryexpression_constructor_args():
    sig = inspect.signature(NonNameUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonnamepostfixorcastexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NonNamePostfixOrCastExpression)


def test_alf_nonnamepostfixorcastexpression_constructor_exists():
    assert callable(alf_NonNamePostfixOrCastExpression.__init__)


def test_alf_nonnamepostfixorcastexpression_constructor_args():
    sig = inspect.signature(alf_NonNamePostfixOrCastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_alf_nonnamepostfixorcastexpression_has_any():
    assert hasattr(alf_NonNamePostfixOrCastExpression, "any")
    descriptor = None
    for klass in alf_NonNamePostfixOrCastExpression.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_castcompletion_is_not_abstract():
    assert not inspect.isabstract(CastCompletion)


def test_castcompletion_constructor_exists():
    assert callable(CastCompletion.__init__)


def test_castcompletion_constructor_args():
    sig = inspect.signature(CastCompletion.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonpostfixnoncastunaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NonPostfixNonCastUnaryExpression)


def test_alf_nonpostfixnoncastunaryexpression_constructor_exists():
    assert callable(alf_NonPostfixNonCastUnaryExpression.__init__)


def test_alf_nonpostfixnoncastunaryexpression_constructor_args():
    sig = inspect.signature(alf_NonPostfixNonCastUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_postfixorcastexpression_is_not_abstract():
    assert not inspect.isabstract(alf_PostfixOrCastExpression)


def test_alf_postfixorcastexpression_constructor_exists():
    assert callable(alf_PostfixOrCastExpression.__init__)


def test_alf_postfixorcastexpression_constructor_args():
    sig = inspect.signature(alf_PostfixOrCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_nonpostfixnoncastunaryexpression_is_not_abstract():
    assert not inspect.isabstract(NonPostfixNonCastUnaryExpression)


def test_nonpostfixnoncastunaryexpression_constructor_exists():
    assert callable(NonPostfixNonCastUnaryExpression.__init__)


def test_nonpostfixnoncastunaryexpression_constructor_args():
    sig = inspect.signature(NonPostfixNonCastUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_bitstringcomplementexpression_is_not_abstract():
    assert not inspect.isabstract(alf_BitStringComplementExpression)


def test_alf_bitstringcomplementexpression_constructor_exists():
    assert callable(alf_BitStringComplementExpression.__init__)


def test_alf_bitstringcomplementexpression_constructor_args():
    sig = inspect.signature(alf_BitStringComplementExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_numericunaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NumericUnaryExpression)


def test_alf_numericunaryexpression_constructor_exists():
    assert callable(alf_NumericUnaryExpression.__init__)


def test_alf_numericunaryexpression_constructor_args():
    sig = inspect.signature(alf_NumericUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_numericunaryexpression_has_operator():
    assert hasattr(alf_NumericUnaryExpression, "operator")
    descriptor = None
    for klass in alf_NumericUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_isolationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_IsolationExpression)


def test_alf_isolationexpression_constructor_exists():
    assert callable(alf_IsolationExpression.__init__)


def test_alf_isolationexpression_constructor_args():
    sig = inspect.signature(alf_IsolationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_booleannegationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_BooleanNegationExpression)


def test_alf_booleannegationexpression_constructor_exists():
    assert callable(alf_BooleanNegationExpression.__init__)


def test_alf_booleannegationexpression_constructor_args():
    sig = inspect.signature(alf_BooleanNegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(alf_PrefixExpression)


def test_alf_prefixexpression_constructor_exists():
    assert callable(alf_PrefixExpression.__init__)


def test_alf_prefixexpression_constructor_args():
    sig = inspect.signature(alf_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_prefixexpression_has_operator():
    assert hasattr(alf_PrefixExpression, "operator")
    descriptor = None
    for klass in alf_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_postfixoperation_is_not_abstract():
    assert not inspect.isabstract(alf_PostfixOperation)


def test_alf_postfixoperation_constructor_exists():
    assert callable(alf_PostfixOperation.__init__)


def test_alf_postfixoperation_constructor_args():
    sig = inspect.signature(alf_PostfixOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf_postfixoperation_has_operator():
    assert hasattr(alf_PostfixOperation, "operator")
    descriptor = None
    for klass in alf_PostfixOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf_eobject_is_not_abstract():
    assert not inspect.isabstract(alf_EObject)


def test_alf_eobject_constructor_exists():
    assert callable(alf_EObject.__init__)


def test_alf_eobject_constructor_args():
    sig = inspect.signature(alf_EObject.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceelement_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceElement)


def test_alf_sequenceelement_constructor_exists():
    assert callable(alf_SequenceElement.__init__)


def test_alf_sequenceelement_constructor_args():
    sig = inspect.signature(alf_SequenceElement.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceelementlistcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceElementListCompletion)


def test_alf_sequenceelementlistcompletion_constructor_exists():
    assert callable(alf_SequenceElementListCompletion.__init__)


def test_alf_sequenceelementlistcompletion_constructor_args():
    sig = inspect.signature(alf_SequenceElementListCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceelements_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceElements)


def test_alf_sequenceelements_constructor_exists():
    assert callable(alf_SequenceElements.__init__)


def test_alf_sequenceelements_constructor_args():
    sig = inspect.signature(alf_SequenceElements.__init__)
    params = list(sig.parameters.keys())



def test_alf_multiplicityindicator_is_not_abstract():
    assert not inspect.isabstract(alf_MultiplicityIndicator)


def test_alf_multiplicityindicator_constructor_exists():
    assert callable(alf_MultiplicityIndicator.__init__)


def test_alf_multiplicityindicator_constructor_args():
    sig = inspect.signature(alf_MultiplicityIndicator.__init__)
    params = list(sig.parameters.keys())



def test_alf_indexednamedexpression_is_not_abstract():
    assert not inspect.isabstract(alf_IndexedNamedExpression)


def test_alf_indexednamedexpression_constructor_exists():
    assert callable(alf_IndexedNamedExpression.__init__)


def test_alf_indexednamedexpression_constructor_args():
    sig = inspect.signature(alf_IndexedNamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_indexednamedexpressionlistcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_IndexedNamedExpressionListCompletion)


def test_alf_indexednamedexpressionlistcompletion_constructor_exists():
    assert callable(alf_IndexedNamedExpressionListCompletion.__init__)


def test_alf_indexednamedexpressionlistcompletion_constructor_args():
    sig = inspect.signature(alf_IndexedNamedExpressionListCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_linkoperationtuple_is_not_abstract():
    assert not inspect.isabstract(alf_LinkOperationTuple)


def test_alf_linkoperationtuple_constructor_exists():
    assert callable(alf_LinkOperationTuple.__init__)


def test_alf_linkoperationtuple_constructor_args():
    sig = inspect.signature(alf_LinkOperationTuple.__init__)
    params = list(sig.parameters.keys())



def test_baseexpression_is_not_abstract():
    assert not inspect.isabstract(BaseExpression)


def test_baseexpression_constructor_exists():
    assert callable(BaseExpression.__init__)


def test_baseexpression_constructor_args():
    sig = inspect.signature(BaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_instancecreationorsequenceconstructionexpression_is_not_abstract():
    assert not inspect.isabstract(alf_InstanceCreationOrSequenceConstructionExpression)


def test_alf_instancecreationorsequenceconstructionexpression_constructor_exists():
    assert callable(alf_InstanceCreationOrSequenceConstructionExpression.__init__)


def test_alf_instancecreationorsequenceconstructionexpression_constructor_args():
    sig = inspect.signature(alf_InstanceCreationOrSequenceConstructionExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_superinvocationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SuperInvocationExpression)


def test_alf_superinvocationexpression_constructor_exists():
    assert callable(alf_SuperInvocationExpression.__init__)


def test_alf_superinvocationexpression_constructor_args():
    sig = inspect.signature(alf_SuperInvocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceanyexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceAnyExpression)


def test_alf_sequenceanyexpression_constructor_exists():
    assert callable(alf_SequenceAnyExpression.__init__)


def test_alf_sequenceanyexpression_constructor_args():
    sig = inspect.signature(alf_SequenceAnyExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_literalexpression_is_not_abstract():
    assert not inspect.isabstract(alf_LiteralExpression)


def test_alf_literalexpression_constructor_exists():
    assert callable(alf_LiteralExpression.__init__)


def test_alf_literalexpression_constructor_args():
    sig = inspect.signature(alf_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_index_is_not_abstract():
    assert not inspect.isabstract(alf_Index)


def test_alf_index_constructor_exists():
    assert callable(alf_Index.__init__)


def test_alf_index_constructor_args():
    sig = inspect.signature(alf_Index.__init__)
    params = list(sig.parameters.keys())



def test_alf_namedexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NamedExpression)


def test_alf_namedexpression_constructor_exists():
    assert callable(alf_NamedExpression.__init__)


def test_alf_namedexpression_constructor_args():
    sig = inspect.signature(alf_NamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_positionaltupleexpressionlistcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_PositionalTupleExpressionListCompletion)


def test_alf_positionaltupleexpressionlistcompletion_constructor_exists():
    assert callable(alf_PositionalTupleExpressionListCompletion.__init__)


def test_alf_positionaltupleexpressionlistcompletion_constructor_args():
    sig = inspect.signature(alf_PositionalTupleExpressionListCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_positionaltupleexpressionlist_is_not_abstract():
    assert not inspect.isabstract(alf_PositionalTupleExpressionList)


def test_alf_positionaltupleexpressionlist_constructor_exists():
    assert callable(alf_PositionalTupleExpressionList.__init__)


def test_alf_positionaltupleexpressionlist_constructor_args():
    sig = inspect.signature(alf_PositionalTupleExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_alf_namedtupleexpressionlist_is_not_abstract():
    assert not inspect.isabstract(alf_NamedTupleExpressionList)


def test_alf_namedtupleexpressionlist_constructor_exists():
    assert callable(alf_NamedTupleExpressionList.__init__)


def test_alf_namedtupleexpressionlist_constructor_args():
    sig = inspect.signature(alf_NamedTupleExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_alf_tuple_is_not_abstract():
    assert not inspect.isabstract(alf_Tuple)


def test_alf_tuple_constructor_exists():
    assert callable(alf_Tuple.__init__)


def test_alf_tuple_constructor_args():
    sig = inspect.signature(alf_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_alf_thisexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ThisExpression)


def test_alf_thisexpression_constructor_exists():
    assert callable(alf_ThisExpression.__init__)


def test_alf_thisexpression_constructor_args():
    sig = inspect.signature(alf_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_expressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ExpressionCompletion)


def test_alf_expressioncompletion_constructor_exists():
    assert callable(alf_ExpressionCompletion.__init__)


def test_alf_expressioncompletion_constructor_args():
    sig = inspect.signature(alf_ExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_UnaryExpression)


def test_alf_unaryexpression_constructor_exists():
    assert callable(alf_UnaryExpression.__init__)


def test_alf_unaryexpression_constructor_args():
    sig = inspect.signature(alf_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_initializationexpression_is_not_abstract():
    assert not inspect.isabstract(InitializationExpression)


def test_initializationexpression_constructor_exists():
    assert callable(InitializationExpression.__init__)


def test_initializationexpression_constructor_args():
    sig = inspect.signature(InitializationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_instanceinitializationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_InstanceInitializationExpression)


def test_alf_instanceinitializationexpression_constructor_exists():
    assert callable(alf_InstanceInitializationExpression.__init__)


def test_alf_instanceinitializationexpression_constructor_args():
    sig = inspect.signature(alf_InstanceInitializationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceinitializationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceInitializationExpression)


def test_alf_sequenceinitializationexpression_constructor_exists():
    assert callable(alf_SequenceInitializationExpression.__init__)


def test_alf_sequenceinitializationexpression_constructor_args():
    sig = inspect.signature(alf_SequenceInitializationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNew" in params, "Missing parameter 'isNew'"

def test_alf_sequenceinitializationexpression_has_isNew():
    assert hasattr(alf_SequenceInitializationExpression, "isNew")
    descriptor = None
    for klass in alf_SequenceInitializationExpression.__mro__:
        if "isNew" in klass.__dict__:
            descriptor = klass.__dict__["isNew"]
            break
    assert isinstance(descriptor, property)



def test_alf_expression_is_not_abstract():
    assert not inspect.isabstract(alf_Expression)


def test_alf_expression_constructor_exists():
    assert callable(alf_Expression.__init__)


def test_alf_expression_constructor_args():
    sig = inspect.signature(alf_Expression.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceoperationorreductionorexpansion_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceOperationOrReductionOrExpansion)


def test_alf_sequenceoperationorreductionorexpansion_constructor_exists():
    assert callable(alf_SequenceOperationOrReductionOrExpansion.__init__)


def test_alf_sequenceoperationorreductionorexpansion_constructor_args():
    sig = inspect.signature(alf_SequenceOperationOrReductionOrExpansion.__init__)
    params = list(sig.parameters.keys())
    assert "isReduce" in params, "Missing parameter 'isReduce'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "id" in params, "Missing parameter 'id'"

def test_alf_sequenceoperationorreductionorexpansion_has_isReduce():
    assert hasattr(alf_SequenceOperationOrReductionOrExpansion, "isReduce")
    descriptor = None
    for klass in alf_SequenceOperationOrReductionOrExpansion.__mro__:
        if "isReduce" in klass.__dict__:
            descriptor = klass.__dict__["isReduce"]
            break
    assert isinstance(descriptor, property)

def test_alf_sequenceoperationorreductionorexpansion_has_isOrdered():
    assert hasattr(alf_SequenceOperationOrReductionOrExpansion, "isOrdered")
    descriptor = None
    for klass in alf_SequenceOperationOrReductionOrExpansion.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_alf_sequenceoperationorreductionorexpansion_has_id():
    assert hasattr(alf_SequenceOperationOrReductionOrExpansion, "id")
    descriptor = None
    for klass in alf_SequenceOperationOrReductionOrExpansion.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf_featureinvocation_is_not_abstract():
    assert not inspect.isabstract(alf_FeatureInvocation)


def test_alf_featureinvocation_constructor_exists():
    assert callable(alf_FeatureInvocation.__init__)


def test_alf_featureinvocation_constructor_args():
    sig = inspect.signature(alf_FeatureInvocation.__init__)
    params = list(sig.parameters.keys())



def test_alf_feature_is_not_abstract():
    assert not inspect.isabstract(alf_Feature)


def test_alf_feature_constructor_exists():
    assert callable(alf_Feature.__init__)


def test_alf_feature_constructor_args():
    sig = inspect.signature(alf_Feature.__init__)
    params = list(sig.parameters.keys())



def test_alf_feature_or_sequenceoperationorreductionorexpansion_or_index_is_not_abstract():
    assert not inspect.isabstract(alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index)


def test_alf_feature_or_sequenceoperationorreductionorexpansion_or_index_constructor_exists():
    assert callable(alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index.__init__)


def test_alf_feature_or_sequenceoperationorreductionorexpansion_or_index_constructor_args():
    sig = inspect.signature(alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index.__init__)
    params = list(sig.parameters.keys())



def test_alf_behaviorinvocation_is_not_abstract():
    assert not inspect.isabstract(alf_BehaviorInvocation)


def test_alf_behaviorinvocation_constructor_exists():
    assert callable(alf_BehaviorInvocation.__init__)


def test_alf_behaviorinvocation_constructor_args():
    sig = inspect.signature(alf_BehaviorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceconstructionexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceConstructionExpressionCompletion)


def test_alf_sequenceconstructionexpressioncompletion_constructor_exists():
    assert callable(alf_SequenceConstructionExpressionCompletion.__init__)


def test_alf_sequenceconstructionexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_SequenceConstructionExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_classextentexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ClassExtentExpressionCompletion)


def test_alf_classextentexpressioncompletion_constructor_exists():
    assert callable(alf_ClassExtentExpressionCompletion.__init__)


def test_alf_classextentexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_ClassExtentExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_linkoperationcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_LinkOperationCompletion)


def test_alf_linkoperationcompletion_constructor_exists():
    assert callable(alf_LinkOperationCompletion.__init__)


def test_alf_linkoperationcompletion_constructor_args():
    sig = inspect.signature(alf_LinkOperationCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "linkOperation" in params, "Missing parameter 'linkOperation'"

def test_alf_linkoperationcompletion_has_linkOperation():
    assert hasattr(alf_LinkOperationCompletion, "linkOperation")
    descriptor = None
    for klass in alf_LinkOperationCompletion.__mro__:
        if "linkOperation" in klass.__dict__:
            descriptor = klass.__dict__["linkOperation"]
            break
    assert isinstance(descriptor, property)



def test_alf_primaryexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_PrimaryExpressionCompletion)


def test_alf_primaryexpressioncompletion_constructor_exists():
    assert callable(alf_PrimaryExpressionCompletion.__init__)


def test_alf_primaryexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_PrimaryExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ParenthesizedExpression)


def test_alf_parenthesizedexpression_constructor_exists():
    assert callable(alf_ParenthesizedExpression.__init__)


def test_alf_parenthesizedexpression_constructor_args():
    sig = inspect.signature(alf_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_baseexpression_is_not_abstract():
    assert not inspect.isabstract(alf_BaseExpression)


def test_alf_baseexpression_constructor_exists():
    assert callable(alf_BaseExpression.__init__)


def test_alf_baseexpression_constructor_args():
    sig = inspect.signature(alf_BaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_nameorprimaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NameOrPrimaryExpression)


def test_alf_nameorprimaryexpression_constructor_exists():
    assert callable(alf_NameOrPrimaryExpression.__init__)


def test_alf_nameorprimaryexpression_constructor_args():
    sig = inspect.signature(alf_NameOrPrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_PrimaryExpression)


def test_alf_primaryexpression_constructor_exists():
    assert callable(alf_PrimaryExpression.__init__)


def test_alf_primaryexpression_constructor_args():
    sig = inspect.signature(alf_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_postfixexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_PostfixExpressionCompletion)


def test_alf_postfixexpressioncompletion_constructor_exists():
    assert callable(alf_PostfixExpressionCompletion.__init__)


def test_alf_postfixexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_PostfixExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_primarytoexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_PrimaryToExpressionCompletion)


def test_alf_primarytoexpressioncompletion_constructor_exists():
    assert callable(alf_PrimaryToExpressionCompletion.__init__)


def test_alf_primarytoexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_PrimaryToExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_nametoprimaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NameToPrimaryExpression)


def test_alf_nametoprimaryexpression_constructor_exists():
    assert callable(alf_NameToPrimaryExpression.__init__)


def test_alf_nametoprimaryexpression_constructor_args():
    sig = inspect.signature(alf_NameToPrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_nametoexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_NameToExpressionCompletion)


def test_alf_nametoexpressioncompletion_constructor_exists():
    assert callable(alf_NameToExpressionCompletion.__init__)


def test_alf_nametoexpressioncompletion_constructor_args():
    sig = inspect.signature(alf_NameToExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonnameunaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NonNameUnaryExpression)


def test_alf_nonnameunaryexpression_constructor_exists():
    assert callable(alf_NonNameUnaryExpression.__init__)


def test_alf_nonnameunaryexpression_constructor_args():
    sig = inspect.signature(alf_NonNameUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonnameexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NonNameExpression)


def test_alf_nonnameexpression_constructor_exists():
    assert callable(alf_NonNameExpression.__init__)


def test_alf_nonnameexpression_constructor_args():
    sig = inspect.signature(alf_NonNameExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_signalreceptiondeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_SignalReceptionDeclaration)


def test_alf_signalreceptiondeclaration_constructor_exists():
    assert callable(alf_SignalReceptionDeclaration.__init__)


def test_alf_signalreceptiondeclaration_constructor_args():
    sig = inspect.signature(alf_SignalReceptionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(alf_TemplateParameterSubstitution)


def test_alf_templateparametersubstitution_constructor_exists():
    assert callable(alf_TemplateParameterSubstitution.__init__)


def test_alf_templateparametersubstitution_constructor_args():
    sig = inspect.signature(alf_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_templatebinding_is_not_abstract():
    assert not inspect.isabstract(TemplateBinding)


def test_templatebinding_constructor_exists():
    assert callable(TemplateBinding.__init__)


def test_templatebinding_constructor_args():
    sig = inspect.signature(TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_namedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(alf_NamedTemplateBinding)


def test_alf_namedtemplatebinding_constructor_exists():
    assert callable(alf_NamedTemplateBinding.__init__)


def test_alf_namedtemplatebinding_constructor_args():
    sig = inspect.signature(alf_NamedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_positionaltemplatebinding_is_not_abstract():
    assert not inspect.isabstract(alf_PositionalTemplateBinding)


def test_alf_positionaltemplatebinding_constructor_exists():
    assert callable(alf_PositionalTemplateBinding.__init__)


def test_alf_positionaltemplatebinding_constructor_args():
    sig = inspect.signature(alf_PositionalTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_colonqualifiednamecompletionwithoutbinding_is_not_abstract():
    assert not inspect.isabstract(alf_ColonQualifiedNameCompletionWithoutBinding)


def test_alf_colonqualifiednamecompletionwithoutbinding_constructor_exists():
    assert callable(alf_ColonQualifiedNameCompletionWithoutBinding.__init__)


def test_alf_colonqualifiednamecompletionwithoutbinding_constructor_args():
    sig = inspect.signature(alf_ColonQualifiedNameCompletionWithoutBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_qualifiednamewithoutbinding_is_not_abstract():
    assert not inspect.isabstract(alf_QualifiedNameWithoutBinding)


def test_alf_qualifiednamewithoutbinding_constructor_exists():
    assert callable(alf_QualifiedNameWithoutBinding.__init__)


def test_alf_qualifiednamewithoutbinding_constructor_args():
    sig = inspect.signature(alf_QualifiedNameWithoutBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_templatebinding_is_not_abstract():
    assert not inspect.isabstract(alf_TemplateBinding)


def test_alf_templatebinding_constructor_exists():
    assert callable(alf_TemplateBinding.__init__)


def test_alf_templatebinding_constructor_args():
    sig = inspect.signature(alf_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_unqualifiedname_is_not_abstract():
    assert not inspect.isabstract(UnqualifiedName)


def test_unqualifiedname_constructor_exists():
    assert callable(UnqualifiedName.__init__)


def test_unqualifiedname_constructor_args():
    sig = inspect.signature(UnqualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_alf_namebinding_is_not_abstract():
    assert not inspect.isabstract(alf_NameBinding)


def test_alf_namebinding_constructor_exists():
    assert callable(alf_NameBinding.__init__)


def test_alf_namebinding_constructor_args():
    sig = inspect.signature(alf_NameBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_colonqualifiednamecompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ColonQualifiedNameCompletion)


def test_alf_colonqualifiednamecompletion_constructor_exists():
    assert callable(alf_ColonQualifiedNameCompletion.__init__)


def test_alf_colonqualifiednamecompletion_constructor_args():
    sig = inspect.signature(alf_ColonQualifiedNameCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_unqualifiedname_is_not_abstract():
    assert not inspect.isabstract(alf_UnqualifiedName)


def test_alf_unqualifiedname_constructor_exists():
    assert callable(alf_UnqualifiedName.__init__)


def test_alf_unqualifiedname_constructor_args():
    sig = inspect.signature(alf_UnqualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_alf_initializationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_InitializationExpression)


def test_alf_initializationexpression_constructor_exists():
    assert callable(alf_InitializationExpression.__init__)


def test_alf_initializationexpression_constructor_args():
    sig = inspect.signature(alf_InitializationExpression.__init__)
    params = list(sig.parameters.keys())



def test_activefeaturedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(ActiveFeatureDefinitionOrStub)


def test_activefeaturedefinitionorstub_constructor_exists():
    assert callable(ActiveFeatureDefinitionOrStub.__init__)


def test_activefeaturedefinitionorstub_constructor_args():
    sig = inspect.signature(ActiveFeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_signalreceptiondefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_SignalReceptionDefinitionOrStub)


def test_alf_signalreceptiondefinitionorstub_constructor_exists():
    assert callable(alf_SignalReceptionDefinitionOrStub.__init__)


def test_alf_signalreceptiondefinitionorstub_constructor_args():
    sig = inspect.signature(alf_SignalReceptionDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_receptiondefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ReceptionDefinition)


def test_alf_receptiondefinition_constructor_exists():
    assert callable(alf_ReceptionDefinition.__init__)


def test_alf_receptiondefinition_constructor_args():
    sig = inspect.signature(alf_ReceptionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_attributeinitializer_is_not_abstract():
    assert not inspect.isabstract(alf_AttributeInitializer)


def test_alf_attributeinitializer_constructor_exists():
    assert callable(alf_AttributeInitializer.__init__)


def test_alf_attributeinitializer_constructor_args():
    sig = inspect.signature(alf_AttributeInitializer.__init__)
    params = list(sig.parameters.keys())



def test_alf_redefinitionclause_is_not_abstract():
    assert not inspect.isabstract(alf_RedefinitionClause)


def test_alf_redefinitionclause_constructor_exists():
    assert callable(alf_RedefinitionClause.__init__)


def test_alf_redefinitionclause_constructor_args():
    sig = inspect.signature(alf_RedefinitionClause.__init__)
    params = list(sig.parameters.keys())



def test_operationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(OperationDefinitionOrStub)


def test_operationdefinitionorstub_constructor_exists():
    assert callable(OperationDefinitionOrStub.__init__)


def test_operationdefinitionorstub_constructor_args():
    sig = inspect.signature(OperationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_operationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_OperationDeclaration)


def test_alf_operationdeclaration_constructor_exists():
    assert callable(alf_OperationDeclaration.__init__)


def test_alf_operationdeclaration_constructor_args():
    sig = inspect.signature(alf_OperationDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf_operationdeclaration_has_isAbstract():
    assert hasattr(alf_OperationDeclaration, "isAbstract")
    descriptor = None
    for klass in alf_OperationDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf_unlimitednaturalliteral_is_not_abstract():
    assert not inspect.isabstract(alf_UnlimitedNaturalLiteral)


def test_alf_unlimitednaturalliteral_constructor_exists():
    assert callable(alf_UnlimitedNaturalLiteral.__init__)


def test_alf_unlimitednaturalliteral_constructor_args():
    sig = inspect.signature(alf_UnlimitedNaturalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_alf_unlimitednaturalliteral_has_star():
    assert hasattr(alf_UnlimitedNaturalLiteral, "star")
    descriptor = None
    for klass in alf_UnlimitedNaturalLiteral.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_alf_multiplicityrange_is_not_abstract():
    assert not inspect.isabstract(alf_MultiplicityRange)


def test_alf_multiplicityrange_constructor_exists():
    assert callable(alf_MultiplicityRange.__init__)


def test_alf_multiplicityrange_constructor_args():
    sig = inspect.signature(alf_MultiplicityRange.__init__)
    params = list(sig.parameters.keys())



def test_alf_multiplicity_is_not_abstract():
    assert not inspect.isabstract(alf_Multiplicity)


def test_alf_multiplicity_constructor_exists():
    assert callable(alf_Multiplicity.__init__)


def test_alf_multiplicity_constructor_args():
    sig = inspect.signature(alf_Multiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isSequence" in params, "Missing parameter 'isSequence'"
    assert "isNonUnique" in params, "Missing parameter 'isNonUnique'"

def test_alf_multiplicity_has_isOrdered():
    assert hasattr(alf_Multiplicity, "isOrdered")
    descriptor = None
    for klass in alf_Multiplicity.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_alf_multiplicity_has_isSequence():
    assert hasattr(alf_Multiplicity, "isSequence")
    descriptor = None
    for klass in alf_Multiplicity.__mro__:
        if "isSequence" in klass.__dict__:
            descriptor = klass.__dict__["isSequence"]
            break
    assert isinstance(descriptor, property)

def test_alf_multiplicity_has_isNonUnique():
    assert hasattr(alf_Multiplicity, "isNonUnique")
    descriptor = None
    for klass in alf_Multiplicity.__mro__:
        if "isNonUnique" in klass.__dict__:
            descriptor = klass.__dict__["isNonUnique"]
            break
    assert isinstance(descriptor, property)



def test_alf_typename_is_not_abstract():
    assert not inspect.isabstract(alf_TypeName)


def test_alf_typename_constructor_exists():
    assert callable(alf_TypeName.__init__)


def test_alf_typename_constructor_args():
    sig = inspect.signature(alf_TypeName.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_alf_typename_has_any():
    assert hasattr(alf_TypeName, "any")
    descriptor = None
    for klass in alf_TypeName.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_alf_typepart_is_not_abstract():
    assert not inspect.isabstract(alf_TypePart)


def test_alf_typepart_constructor_exists():
    assert callable(alf_TypePart.__init__)


def test_alf_typepart_constructor_args():
    sig = inspect.signature(alf_TypePart.__init__)
    params = list(sig.parameters.keys())



def test_alf_formalparameters_is_not_abstract():
    assert not inspect.isabstract(alf_FormalParameters)


def test_alf_formalparameters_constructor_exists():
    assert callable(alf_FormalParameters.__init__)


def test_alf_formalparameters_constructor_args():
    sig = inspect.signature(alf_FormalParameters.__init__)
    params = list(sig.parameters.keys())



def test_featuredefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(FeatureDefinitionOrStub)


def test_featuredefinitionorstub_constructor_exists():
    assert callable(FeatureDefinitionOrStub.__init__)


def test_featuredefinitionorstub_constructor_args():
    sig = inspect.signature(FeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_operationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_OperationDefinitionOrStub)


def test_alf_operationdefinitionorstub_constructor_exists():
    assert callable(alf_OperationDefinitionOrStub.__init__)


def test_alf_operationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf_OperationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(alf_AttributeDefinition)


def test_alf_attributedefinition_constructor_exists():
    assert callable(alf_AttributeDefinition.__init__)


def test_alf_attributedefinition_constructor_args():
    sig = inspect.signature(alf_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_PropertyDeclaration)


def test_alf_propertydeclaration_constructor_exists():
    assert callable(alf_PropertyDeclaration.__init__)


def test_alf_propertydeclaration_constructor_args():
    sig = inspect.signature(alf_PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_alf_propertydeclaration_has_isComposite():
    assert hasattr(alf_PropertyDeclaration, "isComposite")
    descriptor = None
    for klass in alf_PropertyDeclaration.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_alf_formalparameter_is_not_abstract():
    assert not inspect.isabstract(alf_FormalParameter)


def test_alf_formalparameter_constructor_exists():
    assert callable(alf_FormalParameter.__init__)


def test_alf_formalparameter_constructor_args():
    sig = inspect.signature(alf_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterDirection" in params, "Missing parameter 'parameterDirection'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_formalparameter_has_parameterDirection():
    assert hasattr(alf_FormalParameter, "parameterDirection")
    descriptor = None
    for klass in alf_FormalParameter.__mro__:
        if "parameterDirection" in klass.__dict__:
            descriptor = klass.__dict__["parameterDirection"]
            break
    assert isinstance(descriptor, property)

def test_alf_formalparameter_has_comment():
    assert hasattr(alf_FormalParameter, "comment")
    descriptor = None
    for klass in alf_FormalParameter.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(alf_FormalParameterList)


def test_alf_formalparameterlist_constructor_exists():
    assert callable(alf_FormalParameterList.__init__)


def test_alf_formalparameterlist_constructor_args():
    sig = inspect.signature(alf_FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_alf_associationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_AssociationDeclaration)


def test_alf_associationdeclaration_constructor_exists():
    assert callable(alf_AssociationDeclaration.__init__)


def test_alf_associationdeclaration_constructor_args():
    sig = inspect.signature(alf_AssociationDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf_associationdeclaration_has_isAbstract():
    assert hasattr(alf_AssociationDeclaration, "isAbstract")
    descriptor = None
    for klass in alf_AssociationDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf_propertydefinition_is_not_abstract():
    assert not inspect.isabstract(alf_PropertyDefinition)


def test_alf_propertydefinition_constructor_exists():
    assert callable(alf_PropertyDefinition.__init__)


def test_alf_propertydefinition_constructor_args():
    sig = inspect.signature(alf_PropertyDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_activitydeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_ActivityDeclaration)


def test_alf_activitydeclaration_constructor_exists():
    assert callable(alf_ActivityDeclaration.__init__)


def test_alf_activitydeclaration_constructor_args():
    sig = inspect.signature(alf_ActivityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf_signaldeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_SignalDeclaration)


def test_alf_signaldeclaration_constructor_exists():
    assert callable(alf_SignalDeclaration.__init__)


def test_alf_signaldeclaration_constructor_args():
    sig = inspect.signature(alf_SignalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf_signaldeclaration_has_isAbstract():
    assert hasattr(alf_SignalDeclaration, "isAbstract")
    descriptor = None
    for klass in alf_SignalDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf_enumerationliteralname_is_not_abstract():
    assert not inspect.isabstract(alf_EnumerationLiteralName)


def test_alf_enumerationliteralname_constructor_exists():
    assert callable(alf_EnumerationLiteralName.__init__)


def test_alf_enumerationliteralname_constructor_args():
    sig = inspect.signature(alf_EnumerationLiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_enumerationliteralname_has_comment():
    assert hasattr(alf_EnumerationLiteralName, "comment")
    descriptor = None
    for klass in alf_EnumerationLiteralName.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf_enumerationbody_is_not_abstract():
    assert not inspect.isabstract(alf_EnumerationBody)


def test_alf_enumerationbody_constructor_exists():
    assert callable(alf_EnumerationBody.__init__)


def test_alf_enumerationbody_constructor_args():
    sig = inspect.signature(alf_EnumerationBody.__init__)
    params = list(sig.parameters.keys())



def test_alf_enumerationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_EnumerationDeclaration)


def test_alf_enumerationdeclaration_constructor_exists():
    assert callable(alf_EnumerationDeclaration.__init__)


def test_alf_enumerationdeclaration_constructor_args():
    sig = inspect.signature(alf_EnumerationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf_activeclassbody_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveClassBody)


def test_alf_activeclassbody_constructor_exists():
    assert callable(alf_ActiveClassBody.__init__)


def test_alf_activeclassbody_constructor_args():
    sig = inspect.signature(alf_ActiveClassBody.__init__)
    params = list(sig.parameters.keys())



def test_alf_structuredmember_is_not_abstract():
    assert not inspect.isabstract(alf_StructuredMember)


def test_alf_structuredmember_constructor_exists():
    assert callable(alf_StructuredMember.__init__)


def test_alf_structuredmember_constructor_args():
    sig = inspect.signature(alf_StructuredMember.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"

def test_alf_structuredmember_has_comment():
    assert hasattr(alf_StructuredMember, "comment")
    descriptor = None
    for klass in alf_StructuredMember.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_alf_structuredmember_has_isPublic():
    assert hasattr(alf_StructuredMember, "isPublic")
    descriptor = None
    for klass in alf_StructuredMember.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)



def test_alf_structuredbody_is_not_abstract():
    assert not inspect.isabstract(alf_StructuredBody)


def test_alf_structuredbody_constructor_exists():
    assert callable(alf_StructuredBody.__init__)


def test_alf_structuredbody_constructor_args():
    sig = inspect.signature(alf_StructuredBody.__init__)
    params = list(sig.parameters.keys())



def test_alf_datatypedeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_DataTypeDeclaration)


def test_alf_datatypedeclaration_constructor_exists():
    assert callable(alf_DataTypeDeclaration.__init__)


def test_alf_datatypedeclaration_constructor_args():
    sig = inspect.signature(alf_DataTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf_datatypedeclaration_has_isAbstract():
    assert hasattr(alf_DataTypeDeclaration, "isAbstract")
    descriptor = None
    for klass in alf_DataTypeDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf_activeclassmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveClassMemberDefinition)


def test_alf_activeclassmemberdefinition_constructor_exists():
    assert callable(alf_ActiveClassMemberDefinition.__init__)


def test_alf_activeclassmemberdefinition_constructor_args():
    sig = inspect.signature(alf_ActiveClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_block_is_not_abstract():
    assert not inspect.isabstract(alf_Block)


def test_alf_block_constructor_exists():
    assert callable(alf_Block.__init__)


def test_alf_block_constructor_args():
    sig = inspect.signature(alf_Block.__init__)
    params = list(sig.parameters.keys())



def test_alf_behaviorclause_is_not_abstract():
    assert not inspect.isabstract(alf_BehaviorClause)


def test_alf_behaviorclause_constructor_exists():
    assert callable(alf_BehaviorClause.__init__)


def test_alf_behaviorclause_constructor_args():
    sig = inspect.signature(alf_BehaviorClause.__init__)
    params = list(sig.parameters.keys())



def test_alf_activeclassmember_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveClassMember)


def test_alf_activeclassmember_constructor_exists():
    assert callable(alf_ActiveClassMember.__init__)


def test_alf_activeclassmember_constructor_args():
    sig = inspect.signature(alf_ActiveClassMember.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_activeclassmember_has_comment():
    assert hasattr(alf_ActiveClassMember, "comment")
    descriptor = None
    for klass in alf_ActiveClassMember.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf_packagedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_PackagedElementDefinition)


def test_alf_packagedelementdefinition_constructor_exists():
    assert callable(alf_PackagedElementDefinition.__init__)


def test_alf_packagedelementdefinition_constructor_args():
    sig = inspect.signature(alf_PackagedElementDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_activeclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveClassDeclaration)


def test_alf_activeclassdeclaration_constructor_exists():
    assert callable(alf_ActiveClassDeclaration.__init__)


def test_alf_activeclassdeclaration_constructor_args():
    sig = inspect.signature(alf_ActiveClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf_activeclassdeclaration_has_isAbstract():
    assert hasattr(alf_ActiveClassDeclaration, "isAbstract")
    descriptor = None
    for klass in alf_ActiveClassDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf_packagedelement_is_not_abstract():
    assert not inspect.isabstract(alf_PackagedElement)


def test_alf_packagedelement_constructor_exists():
    assert callable(alf_PackagedElement.__init__)


def test_alf_packagedelement_constructor_args():
    sig = inspect.signature(alf_PackagedElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "importVisibilityIndicator" in params, "Missing parameter 'importVisibilityIndicator'"

def test_alf_packagedelement_has_comment():
    assert hasattr(alf_PackagedElement, "comment")
    descriptor = None
    for klass in alf_PackagedElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_alf_packagedelement_has_importVisibilityIndicator():
    assert hasattr(alf_PackagedElement, "importVisibilityIndicator")
    descriptor = None
    for klass in alf_PackagedElement.__mro__:
        if "importVisibilityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["importVisibilityIndicator"]
            break
    assert isinstance(descriptor, property)



def test_activeclassmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(ActiveClassMemberDefinition)


def test_activeclassmemberdefinition_constructor_exists():
    assert callable(ActiveClassMemberDefinition.__init__)


def test_activeclassmemberdefinition_constructor_args():
    sig = inspect.signature(ActiveClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_activefeaturedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveFeatureDefinitionOrStub)


def test_alf_activefeaturedefinitionorstub_constructor_exists():
    assert callable(alf_ActiveFeatureDefinitionOrStub.__init__)


def test_alf_activefeaturedefinitionorstub_constructor_args():
    sig = inspect.signature(alf_ActiveFeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_classmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ClassMemberDefinition)


def test_alf_classmemberdefinition_constructor_exists():
    assert callable(alf_ClassMemberDefinition.__init__)


def test_alf_classmemberdefinition_constructor_args():
    sig = inspect.signature(alf_ClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_classmember_is_not_abstract():
    assert not inspect.isabstract(alf_ClassMember)


def test_alf_classmember_constructor_exists():
    assert callable(alf_ClassMember.__init__)


def test_alf_classmember_constructor_args():
    sig = inspect.signature(alf_ClassMember.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_classmember_has_comment():
    assert hasattr(alf_ClassMember, "comment")
    descriptor = None
    for klass in alf_ClassMember.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_classifierdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(ClassifierDefinitionOrStub)


def test_classifierdefinitionorstub_constructor_exists():
    assert callable(ClassifierDefinitionOrStub.__init__)


def test_classifierdefinitionorstub_constructor_args():
    sig = inspect.signature(ClassifierDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_activitydefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_ActivityDefinitionOrStub)


def test_alf_activitydefinitionorstub_constructor_exists():
    assert callable(alf_ActivityDefinitionOrStub.__init__)


def test_alf_activitydefinitionorstub_constructor_args():
    sig = inspect.signature(alf_ActivityDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_associationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_AssociationDefinitionOrStub)


def test_alf_associationdefinitionorstub_constructor_exists():
    assert callable(alf_AssociationDefinitionOrStub.__init__)


def test_alf_associationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf_AssociationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_activeclassdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveClassDefinitionOrStub)


def test_alf_activeclassdefinitionorstub_constructor_exists():
    assert callable(alf_ActiveClassDefinitionOrStub.__init__)


def test_alf_activeclassdefinitionorstub_constructor_args():
    sig = inspect.signature(alf_ActiveClassDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_datatypedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_DataTypeDefinitionOrStub)


def test_alf_datatypedefinitionorstub_constructor_exists():
    assert callable(alf_DataTypeDefinitionOrStub.__init__)


def test_alf_datatypedefinitionorstub_constructor_args():
    sig = inspect.signature(alf_DataTypeDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_signaldefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_SignalDefinitionOrStub)


def test_alf_signaldefinitionorstub_constructor_exists():
    assert callable(alf_SignalDefinitionOrStub.__init__)


def test_alf_signaldefinitionorstub_constructor_args():
    sig = inspect.signature(alf_SignalDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_enumerationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_EnumerationDefinitionOrStub)


def test_alf_enumerationdefinitionorstub_constructor_exists():
    assert callable(alf_EnumerationDefinitionOrStub.__init__)


def test_alf_enumerationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf_EnumerationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_classdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_ClassDefinitionOrStub)


def test_alf_classdefinitionorstub_constructor_exists():
    assert callable(alf_ClassDefinitionOrStub.__init__)


def test_alf_classdefinitionorstub_constructor_args():
    sig = inspect.signature(alf_ClassDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_classbody_is_not_abstract():
    assert not inspect.isabstract(alf_ClassBody)


def test_alf_classbody_constructor_exists():
    assert callable(alf_ClassBody.__init__)


def test_alf_classbody_constructor_args():
    sig = inspect.signature(alf_ClassBody.__init__)
    params = list(sig.parameters.keys())



def test_classifierdefinition_is_not_abstract():
    assert not inspect.isabstract(ClassifierDefinition)


def test_classifierdefinition_constructor_exists():
    assert callable(ClassifierDefinition.__init__)


def test_classifierdefinition_constructor_args():
    sig = inspect.signature(ClassifierDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_signaldefinition_is_not_abstract():
    assert not inspect.isabstract(alf_SignalDefinition)


def test_alf_signaldefinition_constructor_exists():
    assert callable(alf_SignalDefinition.__init__)


def test_alf_signaldefinition_constructor_args():
    sig = inspect.signature(alf_SignalDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(alf_DataTypeDefinition)


def test_alf_datatypedefinition_constructor_exists():
    assert callable(alf_DataTypeDefinition.__init__)


def test_alf_datatypedefinition_constructor_args():
    sig = inspect.signature(alf_DataTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_activitydefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ActivityDefinition)


def test_alf_activitydefinition_constructor_exists():
    assert callable(alf_ActivityDefinition.__init__)


def test_alf_activitydefinition_constructor_args():
    sig = inspect.signature(alf_ActivityDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_enumerationdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_EnumerationDefinition)


def test_alf_enumerationdefinition_constructor_exists():
    assert callable(alf_EnumerationDefinition.__init__)


def test_alf_enumerationdefinition_constructor_args():
    sig = inspect.signature(alf_EnumerationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_activeclassdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ActiveClassDefinition)


def test_alf_activeclassdefinition_constructor_exists():
    assert callable(alf_ActiveClassDefinition.__init__)


def test_alf_activeclassdefinition_constructor_args():
    sig = inspect.signature(alf_ActiveClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_associationdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_AssociationDefinition)


def test_alf_associationdefinition_constructor_exists():
    assert callable(alf_AssociationDefinition.__init__)


def test_alf_associationdefinition_constructor_args():
    sig = inspect.signature(alf_AssociationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_classdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ClassDefinition)


def test_alf_classdefinition_constructor_exists():
    assert callable(alf_ClassDefinition.__init__)


def test_alf_classdefinition_constructor_args():
    sig = inspect.signature(alf_ClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_ClassDeclaration)


def test_alf_classdeclaration_constructor_exists():
    assert callable(alf_ClassDeclaration.__init__)


def test_alf_classdeclaration_constructor_args():
    sig = inspect.signature(alf_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf_classdeclaration_has_isAbstract():
    assert hasattr(alf_ClassDeclaration, "isAbstract")
    descriptor = None
    for klass in alf_ClassDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf_classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(alf_ClassifierTemplateParameter)


def test_alf_classifiertemplateparameter_constructor_exists():
    assert callable(alf_ClassifierTemplateParameter.__init__)


def test_alf_classifiertemplateparameter_constructor_args():
    sig = inspect.signature(alf_ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_classifiertemplateparameter_has_comment():
    assert hasattr(alf_ClassifierTemplateParameter, "comment")
    descriptor = None
    for klass in alf_ClassifierTemplateParameter.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf_specializationclause_is_not_abstract():
    assert not inspect.isabstract(alf_SpecializationClause)


def test_alf_specializationclause_constructor_exists():
    assert callable(alf_SpecializationClause.__init__)


def test_alf_specializationclause_constructor_args():
    sig = inspect.signature(alf_SpecializationClause.__init__)
    params = list(sig.parameters.keys())



def test_packagedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(PackagedElementDefinition)


def test_packagedelementdefinition_constructor_exists():
    assert callable(PackagedElementDefinition.__init__)


def test_packagedelementdefinition_constructor_args():
    sig = inspect.signature(PackagedElementDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_packagedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_PackageDefinitionOrStub)


def test_alf_packagedefinitionorstub_constructor_exists():
    assert callable(alf_PackageDefinitionOrStub.__init__)


def test_alf_packagedefinitionorstub_constructor_args():
    sig = inspect.signature(alf_PackageDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_templateparameters_is_not_abstract():
    assert not inspect.isabstract(alf_TemplateParameters)


def test_alf_templateparameters_constructor_exists():
    assert callable(alf_TemplateParameters.__init__)


def test_alf_templateparameters_constructor_args():
    sig = inspect.signature(alf_TemplateParameters.__init__)
    params = list(sig.parameters.keys())



def test_alf_packagebody_is_not_abstract():
    assert not inspect.isabstract(alf_PackageBody)


def test_alf_packagebody_constructor_exists():
    assert callable(alf_PackageBody.__init__)


def test_alf_packagebody_constructor_args():
    sig = inspect.signature(alf_PackageBody.__init__)
    params = list(sig.parameters.keys())



def test_alf_classifiersignature_is_not_abstract():
    assert not inspect.isabstract(alf_ClassifierSignature)


def test_alf_classifiersignature_constructor_exists():
    assert callable(alf_ClassifierSignature.__init__)


def test_alf_classifiersignature_constructor_args():
    sig = inspect.signature(alf_ClassifierSignature.__init__)
    params = list(sig.parameters.keys())



def test_classmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(ClassMemberDefinition)


def test_classmemberdefinition_constructor_exists():
    assert callable(ClassMemberDefinition.__init__)


def test_classmemberdefinition_constructor_args():
    sig = inspect.signature(ClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_classifierdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_ClassifierDefinitionOrStub)


def test_alf_classifierdefinitionorstub_constructor_exists():
    assert callable(alf_ClassifierDefinitionOrStub.__init__)


def test_alf_classifierdefinitionorstub_constructor_args():
    sig = inspect.signature(alf_ClassifierDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf_featuredefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf_FeatureDefinitionOrStub)


def test_alf_featuredefinitionorstub_constructor_exists():
    assert callable(alf_FeatureDefinitionOrStub.__init__)


def test_alf_featuredefinitionorstub_constructor_args():
    sig = inspect.signature(alf_FeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(NamespaceDefinition)


def test_namespacedefinition_constructor_exists():
    assert callable(NamespaceDefinition.__init__)


def test_namespacedefinition_constructor_args():
    sig = inspect.signature(NamespaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_classifierdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_ClassifierDefinition)


def test_alf_classifierdefinition_constructor_exists():
    assert callable(alf_ClassifierDefinition.__init__)


def test_alf_classifierdefinition_constructor_args():
    sig = inspect.signature(alf_ClassifierDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_packagedefinition_is_not_abstract():
    assert not inspect.isabstract(alf_PackageDefinition)


def test_alf_packagedefinition_constructor_exists():
    assert callable(alf_PackageDefinition.__init__)


def test_alf_packagedefinition_constructor_args():
    sig = inspect.signature(alf_PackageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_PackageDeclaration)


def test_alf_packagedeclaration_constructor_exists():
    assert callable(alf_PackageDeclaration.__init__)


def test_alf_packagedeclaration_constructor_args():
    sig = inspect.signature(alf_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf_visibilityindicator_is_not_abstract():
    assert not inspect.isabstract(alf_VisibilityIndicator)


def test_alf_visibilityindicator_constructor_exists():
    assert callable(alf_VisibilityIndicator.__init__)


def test_alf_visibilityindicator_constructor_args():
    sig = inspect.signature(alf_VisibilityIndicator.__init__)
    params = list(sig.parameters.keys())
    assert "PRIVATE" in params, "Missing parameter 'PRIVATE'"
    assert "PROTECTED" in params, "Missing parameter 'PROTECTED'"
    assert "PUBLIC" in params, "Missing parameter 'PUBLIC'"

def test_alf_visibilityindicator_has_PRIVATE():
    assert hasattr(alf_VisibilityIndicator, "PRIVATE")
    descriptor = None
    for klass in alf_VisibilityIndicator.__mro__:
        if "PRIVATE" in klass.__dict__:
            descriptor = klass.__dict__["PRIVATE"]
            break
    assert isinstance(descriptor, property)

def test_alf_visibilityindicator_has_PROTECTED():
    assert hasattr(alf_VisibilityIndicator, "PROTECTED")
    descriptor = None
    for klass in alf_VisibilityIndicator.__mro__:
        if "PROTECTED" in klass.__dict__:
            descriptor = klass.__dict__["PROTECTED"]
            break
    assert isinstance(descriptor, property)

def test_alf_visibilityindicator_has_PUBLIC():
    assert hasattr(alf_VisibilityIndicator, "PUBLIC")
    descriptor = None
    for klass in alf_VisibilityIndicator.__mro__:
        if "PUBLIC" in klass.__dict__:
            descriptor = klass.__dict__["PUBLIC"]
            break
    assert isinstance(descriptor, property)



def test_importreferencequalifiednamecompletion_is_not_abstract():
    assert not inspect.isabstract(ImportReferenceQualifiedNameCompletion)


def test_importreferencequalifiednamecompletion_constructor_exists():
    assert callable(ImportReferenceQualifiedNameCompletion.__init__)


def test_importreferencequalifiednamecompletion_constructor_args():
    sig = inspect.signature(ImportReferenceQualifiedNameCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_colonqualifiednamecompletionofimportreference_is_not_abstract():
    assert not inspect.isabstract(alf_ColonQualifiedNameCompletionOfImportReference)


def test_alf_colonqualifiednamecompletionofimportreference_constructor_exists():
    assert callable(alf_ColonQualifiedNameCompletionOfImportReference.__init__)


def test_alf_colonqualifiednamecompletionofimportreference_constructor_args():
    sig = inspect.signature(alf_ColonQualifiedNameCompletionOfImportReference.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_alf_colonqualifiednamecompletionofimportreference_has_star():
    assert hasattr(alf_ColonQualifiedNameCompletionOfImportReference, "star")
    descriptor = None
    for klass in alf_ColonQualifiedNameCompletionOfImportReference.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_alf_aliasdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_AliasDefinition)


def test_alf_aliasdefinition_constructor_exists():
    assert callable(alf_AliasDefinition.__init__)


def test_alf_aliasdefinition_constructor_args():
    sig = inspect.signature(alf_AliasDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_importreferencequalifiednamecompletion_is_not_abstract():
    assert not inspect.isabstract(alf_ImportReferenceQualifiedNameCompletion)


def test_alf_importreferencequalifiednamecompletion_constructor_exists():
    assert callable(alf_ImportReferenceQualifiedNameCompletion.__init__)


def test_alf_importreferencequalifiednamecompletion_constructor_args():
    sig = inspect.signature(alf_ImportReferenceQualifiedNameCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_name_is_not_abstract():
    assert not inspect.isabstract(alf_Name)


def test_alf_name_constructor_exists():
    assert callable(alf_Name.__init__)


def test_alf_name_constructor_args():
    sig = inspect.signature(alf_Name.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf_name_has_id():
    assert hasattr(alf_Name, "id")
    descriptor = None
    for klass in alf_Name.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf_primitive_literal_is_not_abstract():
    assert not inspect.isabstract(alf_PRIMITIVE_LITERAL)


def test_alf_primitive_literal_constructor_exists():
    assert callable(alf_PRIMITIVE_LITERAL.__init__)


def test_alf_primitive_literal_constructor_args():
    sig = inspect.signature(alf_PRIMITIVE_LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf_primitive_literal_has_value():
    assert hasattr(alf_PRIMITIVE_LITERAL, "value")
    descriptor = None
    for klass in alf_PRIMITIVE_LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alf_taggedvalue_is_not_abstract():
    assert not inspect.isabstract(alf_TaggedValue)


def test_alf_taggedvalue_constructor_exists():
    assert callable(alf_TaggedValue.__init__)


def test_alf_taggedvalue_constructor_args():
    sig = inspect.signature(alf_TaggedValue.__init__)
    params = list(sig.parameters.keys())



def test_taggedvalues_is_not_abstract():
    assert not inspect.isabstract(TaggedValues)


def test_taggedvalues_constructor_exists():
    assert callable(TaggedValues.__init__)


def test_taggedvalues_constructor_args():
    sig = inspect.signature(TaggedValues.__init__)
    params = list(sig.parameters.keys())



def test_alf_qualifiednamelist_is_not_abstract():
    assert not inspect.isabstract(alf_QualifiedNameList)


def test_alf_qualifiednamelist_constructor_exists():
    assert callable(alf_QualifiedNameList.__init__)


def test_alf_qualifiednamelist_constructor_args():
    sig = inspect.signature(alf_QualifiedNameList.__init__)
    params = list(sig.parameters.keys())



def test_alf_taggedvaluelist_is_not_abstract():
    assert not inspect.isabstract(alf_TaggedValueList)


def test_alf_taggedvaluelist_constructor_exists():
    assert callable(alf_TaggedValueList.__init__)


def test_alf_taggedvaluelist_constructor_args():
    sig = inspect.signature(alf_TaggedValueList.__init__)
    params = list(sig.parameters.keys())



def test_alf_taggedvalues_is_not_abstract():
    assert not inspect.isabstract(alf_TaggedValues)


def test_alf_taggedvalues_constructor_exists():
    assert callable(alf_TaggedValues.__init__)


def test_alf_taggedvalues_constructor_args():
    sig = inspect.signature(alf_TaggedValues.__init__)
    params = list(sig.parameters.keys())



def test_alf_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(alf_QualifiedName)


def test_alf_qualifiedname_constructor_exists():
    assert callable(alf_QualifiedName.__init__)


def test_alf_qualifiedname_constructor_args():
    sig = inspect.signature(alf_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_alf_stereotypeannotation_is_not_abstract():
    assert not inspect.isabstract(alf_StereotypeAnnotation)


def test_alf_stereotypeannotation_constructor_exists():
    assert callable(alf_StereotypeAnnotation.__init__)


def test_alf_stereotypeannotation_constructor_args():
    sig = inspect.signature(alf_StereotypeAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_number_literal_is_not_abstract():
    assert not inspect.isabstract(NUMBER_LITERAL)


def test_number_literal_constructor_exists():
    assert callable(NUMBER_LITERAL.__init__)


def test_number_literal_constructor_args():
    sig = inspect.signature(NUMBER_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_unlimited_natural_is_not_abstract():
    assert not inspect.isabstract(alf_UNLIMITED_NATURAL)


def test_alf_unlimited_natural_constructor_exists():
    assert callable(alf_UNLIMITED_NATURAL.__init__)


def test_alf_unlimited_natural_constructor_args():
    sig = inspect.signature(alf_UNLIMITED_NATURAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_integer_literal_is_not_abstract():
    assert not inspect.isabstract(alf_INTEGER_LITERAL)


def test_alf_integer_literal_constructor_exists():
    assert callable(alf_INTEGER_LITERAL.__init__)


def test_alf_integer_literal_constructor_args():
    sig = inspect.signature(alf_INTEGER_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_primitive_literal_is_not_abstract():
    assert not inspect.isabstract(PRIMITIVE_LITERAL)


def test_primitive_literal_constructor_exists():
    assert callable(PRIMITIVE_LITERAL.__init__)


def test_primitive_literal_constructor_args():
    sig = inspect.signature(PRIMITIVE_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_string_literal_is_not_abstract():
    assert not inspect.isabstract(alf_STRING_LITERAL)


def test_alf_string_literal_constructor_exists():
    assert callable(alf_STRING_LITERAL.__init__)


def test_alf_string_literal_constructor_args():
    sig = inspect.signature(alf_STRING_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_number_literal_is_not_abstract():
    assert not inspect.isabstract(alf_NUMBER_LITERAL)


def test_alf_number_literal_constructor_exists():
    assert callable(alf_NUMBER_LITERAL.__init__)


def test_alf_number_literal_constructor_args():
    sig = inspect.signature(alf_NUMBER_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_boolean_literal_is_not_abstract():
    assert not inspect.isabstract(alf_BOOLEAN_LITERAL)


def test_alf_boolean_literal_constructor_exists():
    assert callable(alf_BOOLEAN_LITERAL.__init__)


def test_alf_boolean_literal_constructor_args():
    sig = inspect.signature(alf_BOOLEAN_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(alf_NamespaceDefinition)


def test_alf_namespacedefinition_constructor_exists():
    assert callable(alf_NamespaceDefinition.__init__)


def test_alf_namespacedefinition_constructor_args():
    sig = inspect.signature(alf_NamespaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf_stereotypeannotations_is_not_abstract():
    assert not inspect.isabstract(alf_StereotypeAnnotations)


def test_alf_stereotypeannotations_constructor_exists():
    assert callable(alf_StereotypeAnnotations.__init__)


def test_alf_stereotypeannotations_constructor_args():
    sig = inspect.signature(alf_StereotypeAnnotations.__init__)
    params = list(sig.parameters.keys())



def test_alf_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_ImportDeclaration)


def test_alf_importdeclaration_constructor_exists():
    assert callable(alf_ImportDeclaration.__init__)


def test_alf_importdeclaration_constructor_args():
    sig = inspect.signature(alf_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_alf_importdeclaration_has_visibility():
    assert hasattr(alf_ImportDeclaration, "visibility")
    descriptor = None
    for klass in alf_ImportDeclaration.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_alf_namespacedeclaration_is_not_abstract():
    assert not inspect.isabstract(alf_NamespaceDeclaration)


def test_alf_namespacedeclaration_constructor_exists():
    assert callable(alf_NamespaceDeclaration.__init__)


def test_alf_namespacedeclaration_constructor_args():
    sig = inspect.signature(alf_NamespaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf_unitdefinition_is_not_abstract():
    assert not inspect.isabstract(alf_UnitDefinition)


def test_alf_unitdefinition_constructor_exists():
    assert callable(alf_UnitDefinition.__init__)


def test_alf_unitdefinition_constructor_args():
    sig = inspect.signature(alf_UnitDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf_unitdefinition_has_comment():
    assert hasattr(alf_UnitDefinition, "comment")
    descriptor = None
    for klass in alf_UnitDefinition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf_importreference_is_not_abstract():
    assert not inspect.isabstract(alf_ImportReference)


def test_alf_importreference_constructor_exists():
    assert callable(alf_ImportReference.__init__)


def test_alf_importreference_constructor_args():
    sig = inspect.signature(alf_ImportReference.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_alf_importreference_has_star():
    assert hasattr(alf_ImportReference, "star")
    descriptor = None
    for klass in alf_ImportReference.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "SLASH",
        "REM",
        "STAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_linkoperation_exists():
    # Check that the Enumeration exists
    assert LinkOperation is not None

def test_linkoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkOperation]
    expected_literals = [
        "CLEAR_ASSOC",
        "DESTROY_LINK",
        "CREATE_LINK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkOperation"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "LSHIFT",
        "URSHIFT",
        "RSHIFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_affixoperator_exists():
    # Check that the Enumeration exists
    assert AffixOperator is not None

def test_affixoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AffixOperator]
    expected_literals = [
        "INCR",
        "DECR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AffixOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "GT",
        "GE",
        "LE",
        "LT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_equalityoperator_exists():
    # Check that the Enumeration exists
    assert EqualityOperator is not None

def test_equalityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityOperator]
    expected_literals = [
        "EQ",
        "NE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "PLUSASSIGN",
        "ORASSIGN",
        "STARASSIGN",
        "RSHIFTASSIGN",
        "ASSIGN",
        "SLASHASSIGN",
        "REMASSIGN",
        "XORASSIGN",
        "ANSASSIGN",
        "URSHIFTASSIGN",
        "MINUSASSIGN",
        "LSHIFTASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "MINUS",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_importvisibilityindicator_exists():
    # Check that the Enumeration exists
    assert ImportVisibilityIndicator is not None

def test_importvisibilityindicator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportVisibilityIndicator]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportVisibilityIndicator"

def test_parameterdirection_exists():
    # Check that the Enumeration exists
    assert ParameterDirection is not None

def test_parameterdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirection]
    expected_literals = [
        "INOUT",
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirection"

def test_numericunaryoperator_exists():
    # Check that the Enumeration exists
    assert NumericUnaryOperator is not None

def test_numericunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericUnaryOperator]
    expected_literals = [
        "MINUS",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericUnaryOperator"

def test_classificationoperator_exists():
    # Check that the Enumeration exists
    assert ClassificationOperator is not None

def test_classificationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClassificationOperator]
    expected_literals = [
        "INSTANCEOF",
        "HASTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClassificationOperator"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
alf_AcceptClause_strategy = st.builds(
    alf_AcceptClause,
)
alf_ReclassifyAllClause_strategy = st.builds(
    alf_ReclassifyAllClause,
)
alf_ClassificationToClause_strategy = st.builds(
    alf_ClassificationToClause,
)
alf_ClassificationFromClause_strategy = st.builds(
    alf_ClassificationFromClause,
)
alf_ClassificationClause_strategy = st.builds(
    alf_ClassificationClause,
)
alf_AcceptBlock_strategy = st.builds(
    alf_AcceptBlock,
)
alf_CompoundAcceptStatementCompletion_strategy = st.builds(
    alf_CompoundAcceptStatementCompletion,
)
alf_SimpleAcceptStatementCompletion_strategy = st.builds(
    alf_SimpleAcceptStatementCompletion,
)
alf_NonEmptyStatementSequence_strategy = st.builds(
    alf_NonEmptyStatementSequence,
)
alf_SwitchCase_strategy = st.builds(
    alf_SwitchCase,
)
alf_SwitchDefaultClause_strategy = st.builds(
    alf_SwitchDefaultClause,
)
alf_SwitchClause_strategy = st.builds(
    alf_SwitchClause,
)
alf_LoopVariableDefinition_strategy = st.builds(
    alf_LoopVariableDefinition,
)
alf_ForControl_strategy = st.builds(
    alf_ForControl,
)
alf_LocalNameDeclarationStatementCompletion_strategy = st.builds(
    alf_LocalNameDeclarationStatementCompletion,
)
alf_NonFinalClause_strategy = st.builds(
    alf_NonFinalClause,
)
alf_ConcurrentClauses_strategy = st.builds(
    alf_ConcurrentClauses,
)
alf_FinalClause_strategy = st.builds(
    alf_FinalClause,
)
alf_SequentialClauses_strategy = st.builds(
    alf_SequentialClauses,
)
alf_NameList_strategy = st.builds(
    alf_NameList,
)
alf_Annotation_strategy = st.builds(
    alf_Annotation,
    id=
        safe_text
)
alf_ConditionalExpression_strategy = st.builds(
    alf_ConditionalExpression,
)
alf_ConditionalOrExpressionCompletion_strategy = st.builds(
    alf_ConditionalOrExpressionCompletion,
)
alf_ConditionalOrExpression_strategy = st.builds(
    alf_ConditionalOrExpression,
)
alf_Annotations_strategy = st.builds(
    alf_Annotations,
)
Statement_strategy = st.builds(
    Statement,
)
alf_WhileStatement_strategy = st.builds(
    alf_WhileStatement,
)
alf_BlockStatement_strategy = st.builds(
    alf_BlockStatement,
)
alf_InLineStatement_strategy = st.builds(
    alf_InLineStatement,
    id=
        safe_text
)
alf_DoStatement_strategy = st.builds(
    alf_DoStatement,
)
alf_LocalNameDeclarationOrExpressionStatement_strategy = st.builds(
    alf_LocalNameDeclarationOrExpressionStatement,
)
alf_AcceptStatement_strategy = st.builds(
    alf_AcceptStatement,
)
alf_BreakStatement_strategy = st.builds(
    alf_BreakStatement,
)
alf_ForStatement_strategy = st.builds(
    alf_ForStatement,
)
alf_LocalNameDeclarationStatement_strategy = st.builds(
    alf_LocalNameDeclarationStatement,
)
alf_IfStatement_strategy = st.builds(
    alf_IfStatement,
)
alf_EmptyStatement_strategy = st.builds(
    alf_EmptyStatement,
)
alf_ClassifyStatement_strategy = st.builds(
    alf_ClassifyStatement,
)
alf_ReturnStatement_strategy = st.builds(
    alf_ReturnStatement,
)
alf_SwitchStatement_strategy = st.builds(
    alf_SwitchStatement,
)
alf_AnnotatedStatement_strategy = st.builds(
    alf_AnnotatedStatement,
)
alf_Statement_strategy = st.builds(
    alf_Statement,
)
alf_DocumentedStatement_strategy = st.builds(
    alf_DocumentedStatement,
    comment=
        safe_text
)
alf_StatementSequence_strategy = st.builds(
    alf_StatementSequence,
)
ExpressionCompletion_strategy = st.builds(
    ExpressionCompletion,
)
alf_AssignmentExpressionCompletion_strategy = st.builds(
    alf_AssignmentExpressionCompletion,
    operator=
        safe_text
)
alf_ConditionalExpressionCompletion_strategy = st.builds(
    alf_ConditionalExpressionCompletion,
)
alf_AndExpression_strategy = st.builds(
    alf_AndExpression,
)
alf_EqualityExpressionCompletion_strategy = st.builds(
    alf_EqualityExpressionCompletion,
    operator=
        safe_text
)
alf_ConditionalAndExpressionCompletion_strategy = st.builds(
    alf_ConditionalAndExpressionCompletion,
)
alf_ConditionalAndExpression_strategy = st.builds(
    alf_ConditionalAndExpression,
)
alf_InclusiveOrExpressionCompletion_strategy = st.builds(
    alf_InclusiveOrExpressionCompletion,
)
alf_InclusiveOrExpression_strategy = st.builds(
    alf_InclusiveOrExpression,
)
alf_ExclusiveOrExpressionCompletion_strategy = st.builds(
    alf_ExclusiveOrExpressionCompletion,
)
alf_ExclusiveOrExpression_strategy = st.builds(
    alf_ExclusiveOrExpression,
)
alf_AndExpressionCompletion_strategy = st.builds(
    alf_AndExpressionCompletion,
)
alf_ShiftExpressionCompletion_strategy = st.builds(
    alf_ShiftExpressionCompletion,
    operator=
        safe_text
)
alf_ShiftExpression_strategy = st.builds(
    alf_ShiftExpression,
)
alf_EqualityExpression_strategy = st.builds(
    alf_EqualityExpression,
)
alf_ClassificationExpressionCompletion_strategy = st.builds(
    alf_ClassificationExpressionCompletion,
    operator=
        safe_text
)
alf_ClassificationExpression_strategy = st.builds(
    alf_ClassificationExpression,
)
alf_RelationalExpressionCompletion_strategy = st.builds(
    alf_RelationalExpressionCompletion,
    relationalOperator=
        safe_text
)
alf_RelationalExpression_strategy = st.builds(
    alf_RelationalExpression,
)
alf_AdditiveExpressionCompletion_strategy = st.builds(
    alf_AdditiveExpressionCompletion,
    operator=
        safe_text
)
alf_AdditiveExpression_strategy = st.builds(
    alf_AdditiveExpression,
)
alf_MultiplicativeExpressionCompletion_strategy = st.builds(
    alf_MultiplicativeExpressionCompletion,
    operator=
        safe_text
)
alf_MultiplicativeExpression_strategy = st.builds(
    alf_MultiplicativeExpression,
)
alf_CastCompletion_strategy = st.builds(
    alf_CastCompletion,
)
NonNameUnaryExpression_strategy = st.builds(
    NonNameUnaryExpression,
)
alf_NonNamePostfixOrCastExpression_strategy = st.builds(
    alf_NonNamePostfixOrCastExpression,
    any=
        st.booleans()
)
CastCompletion_strategy = st.builds(
    CastCompletion,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
alf_NonPostfixNonCastUnaryExpression_strategy = st.builds(
    alf_NonPostfixNonCastUnaryExpression,
)
alf_PostfixOrCastExpression_strategy = st.builds(
    alf_PostfixOrCastExpression,
)
NonPostfixNonCastUnaryExpression_strategy = st.builds(
    NonPostfixNonCastUnaryExpression,
)
alf_BitStringComplementExpression_strategy = st.builds(
    alf_BitStringComplementExpression,
)
alf_NumericUnaryExpression_strategy = st.builds(
    alf_NumericUnaryExpression,
    operator=
        safe_text
)
alf_IsolationExpression_strategy = st.builds(
    alf_IsolationExpression,
)
alf_BooleanNegationExpression_strategy = st.builds(
    alf_BooleanNegationExpression,
)
alf_PrefixExpression_strategy = st.builds(
    alf_PrefixExpression,
    operator=
        safe_text
)
alf_PostfixOperation_strategy = st.builds(
    alf_PostfixOperation,
    operator=
        safe_text
)
alf_EObject_strategy = st.builds(
    alf_EObject,
)
alf_SequenceElement_strategy = st.builds(
    alf_SequenceElement,
)
alf_SequenceElementListCompletion_strategy = st.builds(
    alf_SequenceElementListCompletion,
)
alf_SequenceElements_strategy = st.builds(
    alf_SequenceElements,
)
alf_MultiplicityIndicator_strategy = st.builds(
    alf_MultiplicityIndicator,
)
alf_IndexedNamedExpression_strategy = st.builds(
    alf_IndexedNamedExpression,
)
alf_IndexedNamedExpressionListCompletion_strategy = st.builds(
    alf_IndexedNamedExpressionListCompletion,
)
alf_LinkOperationTuple_strategy = st.builds(
    alf_LinkOperationTuple,
)
BaseExpression_strategy = st.builds(
    BaseExpression,
)
alf_InstanceCreationOrSequenceConstructionExpression_strategy = st.builds(
    alf_InstanceCreationOrSequenceConstructionExpression,
)
alf_SuperInvocationExpression_strategy = st.builds(
    alf_SuperInvocationExpression,
)
alf_SequenceAnyExpression_strategy = st.builds(
    alf_SequenceAnyExpression,
)
alf_LiteralExpression_strategy = st.builds(
    alf_LiteralExpression,
)
alf_Index_strategy = st.builds(
    alf_Index,
)
alf_NamedExpression_strategy = st.builds(
    alf_NamedExpression,
)
alf_PositionalTupleExpressionListCompletion_strategy = st.builds(
    alf_PositionalTupleExpressionListCompletion,
)
alf_PositionalTupleExpressionList_strategy = st.builds(
    alf_PositionalTupleExpressionList,
)
alf_NamedTupleExpressionList_strategy = st.builds(
    alf_NamedTupleExpressionList,
)
alf_Tuple_strategy = st.builds(
    alf_Tuple,
)
alf_ThisExpression_strategy = st.builds(
    alf_ThisExpression,
)
alf_ExpressionCompletion_strategy = st.builds(
    alf_ExpressionCompletion,
)
alf_UnaryExpression_strategy = st.builds(
    alf_UnaryExpression,
)
InitializationExpression_strategy = st.builds(
    InitializationExpression,
)
alf_InstanceInitializationExpression_strategy = st.builds(
    alf_InstanceInitializationExpression,
)
alf_SequenceInitializationExpression_strategy = st.builds(
    alf_SequenceInitializationExpression,
    isNew=
        st.booleans()
)
alf_Expression_strategy = st.builds(
    alf_Expression,
)
alf_SequenceOperationOrReductionOrExpansion_strategy = st.builds(
    alf_SequenceOperationOrReductionOrExpansion,
    isReduce=
        st.booleans(),
    isOrdered=
        st.booleans(),
    id=
        safe_text
)
alf_FeatureInvocation_strategy = st.builds(
    alf_FeatureInvocation,
)
alf_Feature_strategy = st.builds(
    alf_Feature,
)
alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index_strategy = st.builds(
    alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index,
)
alf_BehaviorInvocation_strategy = st.builds(
    alf_BehaviorInvocation,
)
alf_SequenceConstructionExpressionCompletion_strategy = st.builds(
    alf_SequenceConstructionExpressionCompletion,
)
alf_ClassExtentExpressionCompletion_strategy = st.builds(
    alf_ClassExtentExpressionCompletion,
)
alf_LinkOperationCompletion_strategy = st.builds(
    alf_LinkOperationCompletion,
    linkOperation=
        safe_text
)
alf_PrimaryExpressionCompletion_strategy = st.builds(
    alf_PrimaryExpressionCompletion,
)
alf_ParenthesizedExpression_strategy = st.builds(
    alf_ParenthesizedExpression,
)
alf_BaseExpression_strategy = st.builds(
    alf_BaseExpression,
)
alf_NameOrPrimaryExpression_strategy = st.builds(
    alf_NameOrPrimaryExpression,
)
alf_PrimaryExpression_strategy = st.builds(
    alf_PrimaryExpression,
)
alf_PostfixExpressionCompletion_strategy = st.builds(
    alf_PostfixExpressionCompletion,
)
alf_PrimaryToExpressionCompletion_strategy = st.builds(
    alf_PrimaryToExpressionCompletion,
)
alf_NameToPrimaryExpression_strategy = st.builds(
    alf_NameToPrimaryExpression,
)
alf_NameToExpressionCompletion_strategy = st.builds(
    alf_NameToExpressionCompletion,
)
alf_NonNameUnaryExpression_strategy = st.builds(
    alf_NonNameUnaryExpression,
)
alf_NonNameExpression_strategy = st.builds(
    alf_NonNameExpression,
)
alf_SignalReceptionDeclaration_strategy = st.builds(
    alf_SignalReceptionDeclaration,
)
alf_TemplateParameterSubstitution_strategy = st.builds(
    alf_TemplateParameterSubstitution,
)
TemplateBinding_strategy = st.builds(
    TemplateBinding,
)
alf_NamedTemplateBinding_strategy = st.builds(
    alf_NamedTemplateBinding,
)
alf_PositionalTemplateBinding_strategy = st.builds(
    alf_PositionalTemplateBinding,
)
alf_ColonQualifiedNameCompletionWithoutBinding_strategy = st.builds(
    alf_ColonQualifiedNameCompletionWithoutBinding,
)
alf_QualifiedNameWithoutBinding_strategy = st.builds(
    alf_QualifiedNameWithoutBinding,
)
alf_TemplateBinding_strategy = st.builds(
    alf_TemplateBinding,
)
UnqualifiedName_strategy = st.builds(
    UnqualifiedName,
)
alf_NameBinding_strategy = st.builds(
    alf_NameBinding,
)
alf_ColonQualifiedNameCompletion_strategy = st.builds(
    alf_ColonQualifiedNameCompletion,
)
alf_UnqualifiedName_strategy = st.builds(
    alf_UnqualifiedName,
)
alf_InitializationExpression_strategy = st.builds(
    alf_InitializationExpression,
)
ActiveFeatureDefinitionOrStub_strategy = st.builds(
    ActiveFeatureDefinitionOrStub,
)
alf_SignalReceptionDefinitionOrStub_strategy = st.builds(
    alf_SignalReceptionDefinitionOrStub,
)
alf_ReceptionDefinition_strategy = st.builds(
    alf_ReceptionDefinition,
)
alf_AttributeInitializer_strategy = st.builds(
    alf_AttributeInitializer,
)
alf_RedefinitionClause_strategy = st.builds(
    alf_RedefinitionClause,
)
OperationDefinitionOrStub_strategy = st.builds(
    OperationDefinitionOrStub,
)
alf_OperationDeclaration_strategy = st.builds(
    alf_OperationDeclaration,
    isAbstract=
        st.booleans()
)
alf_UnlimitedNaturalLiteral_strategy = st.builds(
    alf_UnlimitedNaturalLiteral,
    star=
        st.booleans()
)
alf_MultiplicityRange_strategy = st.builds(
    alf_MultiplicityRange,
)
alf_Multiplicity_strategy = st.builds(
    alf_Multiplicity,
    isOrdered=
        st.booleans(),
    isSequence=
        st.booleans(),
    isNonUnique=
        st.booleans()
)
alf_TypeName_strategy = st.builds(
    alf_TypeName,
    any=
        st.booleans()
)
alf_TypePart_strategy = st.builds(
    alf_TypePart,
)
alf_FormalParameters_strategy = st.builds(
    alf_FormalParameters,
)
FeatureDefinitionOrStub_strategy = st.builds(
    FeatureDefinitionOrStub,
)
alf_OperationDefinitionOrStub_strategy = st.builds(
    alf_OperationDefinitionOrStub,
)
alf_AttributeDefinition_strategy = st.builds(
    alf_AttributeDefinition,
)
alf_PropertyDeclaration_strategy = st.builds(
    alf_PropertyDeclaration,
    isComposite=
        st.booleans()
)
alf_FormalParameter_strategy = st.builds(
    alf_FormalParameter,
    parameterDirection=
        safe_text,
    comment=
        safe_text
)
alf_FormalParameterList_strategy = st.builds(
    alf_FormalParameterList,
)
alf_AssociationDeclaration_strategy = st.builds(
    alf_AssociationDeclaration,
    isAbstract=
        st.booleans()
)
alf_PropertyDefinition_strategy = st.builds(
    alf_PropertyDefinition,
)
alf_ActivityDeclaration_strategy = st.builds(
    alf_ActivityDeclaration,
)
alf_SignalDeclaration_strategy = st.builds(
    alf_SignalDeclaration,
    isAbstract=
        st.booleans()
)
alf_EnumerationLiteralName_strategy = st.builds(
    alf_EnumerationLiteralName,
    comment=
        safe_text
)
alf_EnumerationBody_strategy = st.builds(
    alf_EnumerationBody,
)
alf_EnumerationDeclaration_strategy = st.builds(
    alf_EnumerationDeclaration,
)
alf_ActiveClassBody_strategy = st.builds(
    alf_ActiveClassBody,
)
alf_StructuredMember_strategy = st.builds(
    alf_StructuredMember,
    comment=
        safe_text,
    isPublic=
        st.booleans()
)
alf_StructuredBody_strategy = st.builds(
    alf_StructuredBody,
)
alf_DataTypeDeclaration_strategy = st.builds(
    alf_DataTypeDeclaration,
    isAbstract=
        st.booleans()
)
alf_ActiveClassMemberDefinition_strategy = st.builds(
    alf_ActiveClassMemberDefinition,
)
alf_Block_strategy = st.builds(
    alf_Block,
)
alf_BehaviorClause_strategy = st.builds(
    alf_BehaviorClause,
)
alf_ActiveClassMember_strategy = st.builds(
    alf_ActiveClassMember,
    comment=
        safe_text
)
alf_PackagedElementDefinition_strategy = st.builds(
    alf_PackagedElementDefinition,
)
alf_ActiveClassDeclaration_strategy = st.builds(
    alf_ActiveClassDeclaration,
    isAbstract=
        st.booleans()
)
alf_PackagedElement_strategy = st.builds(
    alf_PackagedElement,
    comment=
        safe_text,
    importVisibilityIndicator=
        safe_text
)
ActiveClassMemberDefinition_strategy = st.builds(
    ActiveClassMemberDefinition,
)
alf_ActiveFeatureDefinitionOrStub_strategy = st.builds(
    alf_ActiveFeatureDefinitionOrStub,
)
alf_ClassMemberDefinition_strategy = st.builds(
    alf_ClassMemberDefinition,
)
alf_ClassMember_strategy = st.builds(
    alf_ClassMember,
    comment=
        safe_text
)
ClassifierDefinitionOrStub_strategy = st.builds(
    ClassifierDefinitionOrStub,
)
alf_ActivityDefinitionOrStub_strategy = st.builds(
    alf_ActivityDefinitionOrStub,
)
alf_AssociationDefinitionOrStub_strategy = st.builds(
    alf_AssociationDefinitionOrStub,
)
alf_ActiveClassDefinitionOrStub_strategy = st.builds(
    alf_ActiveClassDefinitionOrStub,
)
alf_DataTypeDefinitionOrStub_strategy = st.builds(
    alf_DataTypeDefinitionOrStub,
)
alf_SignalDefinitionOrStub_strategy = st.builds(
    alf_SignalDefinitionOrStub,
)
alf_EnumerationDefinitionOrStub_strategy = st.builds(
    alf_EnumerationDefinitionOrStub,
)
alf_ClassDefinitionOrStub_strategy = st.builds(
    alf_ClassDefinitionOrStub,
)
alf_ClassBody_strategy = st.builds(
    alf_ClassBody,
)
ClassifierDefinition_strategy = st.builds(
    ClassifierDefinition,
)
alf_SignalDefinition_strategy = st.builds(
    alf_SignalDefinition,
)
alf_DataTypeDefinition_strategy = st.builds(
    alf_DataTypeDefinition,
)
alf_ActivityDefinition_strategy = st.builds(
    alf_ActivityDefinition,
)
alf_EnumerationDefinition_strategy = st.builds(
    alf_EnumerationDefinition,
)
alf_ActiveClassDefinition_strategy = st.builds(
    alf_ActiveClassDefinition,
)
alf_AssociationDefinition_strategy = st.builds(
    alf_AssociationDefinition,
)
alf_ClassDefinition_strategy = st.builds(
    alf_ClassDefinition,
)
alf_ClassDeclaration_strategy = st.builds(
    alf_ClassDeclaration,
    isAbstract=
        st.booleans()
)
alf_ClassifierTemplateParameter_strategy = st.builds(
    alf_ClassifierTemplateParameter,
    comment=
        safe_text
)
alf_SpecializationClause_strategy = st.builds(
    alf_SpecializationClause,
)
PackagedElementDefinition_strategy = st.builds(
    PackagedElementDefinition,
)
alf_PackageDefinitionOrStub_strategy = st.builds(
    alf_PackageDefinitionOrStub,
)
alf_TemplateParameters_strategy = st.builds(
    alf_TemplateParameters,
)
alf_PackageBody_strategy = st.builds(
    alf_PackageBody,
)
alf_ClassifierSignature_strategy = st.builds(
    alf_ClassifierSignature,
)
ClassMemberDefinition_strategy = st.builds(
    ClassMemberDefinition,
)
alf_ClassifierDefinitionOrStub_strategy = st.builds(
    alf_ClassifierDefinitionOrStub,
)
alf_FeatureDefinitionOrStub_strategy = st.builds(
    alf_FeatureDefinitionOrStub,
)
NamespaceDefinition_strategy = st.builds(
    NamespaceDefinition,
)
alf_ClassifierDefinition_strategy = st.builds(
    alf_ClassifierDefinition,
)
alf_PackageDefinition_strategy = st.builds(
    alf_PackageDefinition,
)
alf_PackageDeclaration_strategy = st.builds(
    alf_PackageDeclaration,
)
alf_VisibilityIndicator_strategy = st.builds(
    alf_VisibilityIndicator,
    PRIVATE=
        safe_text,
    PROTECTED=
        safe_text,
    PUBLIC=
        safe_text
)
ImportReferenceQualifiedNameCompletion_strategy = st.builds(
    ImportReferenceQualifiedNameCompletion,
)
alf_ColonQualifiedNameCompletionOfImportReference_strategy = st.builds(
    alf_ColonQualifiedNameCompletionOfImportReference,
    star=
        st.booleans()
)
alf_AliasDefinition_strategy = st.builds(
    alf_AliasDefinition,
)
alf_ImportReferenceQualifiedNameCompletion_strategy = st.builds(
    alf_ImportReferenceQualifiedNameCompletion,
)
alf_Name_strategy = st.builds(
    alf_Name,
    id=
        safe_text
)
alf_PRIMITIVE_LITERAL_strategy = st.builds(
    alf_PRIMITIVE_LITERAL,
    value=
        safe_text
)
alf_TaggedValue_strategy = st.builds(
    alf_TaggedValue,
)
TaggedValues_strategy = st.builds(
    TaggedValues,
)
alf_QualifiedNameList_strategy = st.builds(
    alf_QualifiedNameList,
)
alf_TaggedValueList_strategy = st.builds(
    alf_TaggedValueList,
)
alf_TaggedValues_strategy = st.builds(
    alf_TaggedValues,
)
alf_QualifiedName_strategy = st.builds(
    alf_QualifiedName,
)
alf_StereotypeAnnotation_strategy = st.builds(
    alf_StereotypeAnnotation,
)
NUMBER_LITERAL_strategy = st.builds(
    NUMBER_LITERAL,
)
alf_UNLIMITED_NATURAL_strategy = st.builds(
    alf_UNLIMITED_NATURAL,
)
alf_INTEGER_LITERAL_strategy = st.builds(
    alf_INTEGER_LITERAL,
)
PRIMITIVE_LITERAL_strategy = st.builds(
    PRIMITIVE_LITERAL,
)
alf_STRING_LITERAL_strategy = st.builds(
    alf_STRING_LITERAL,
)
alf_NUMBER_LITERAL_strategy = st.builds(
    alf_NUMBER_LITERAL,
)
alf_BOOLEAN_LITERAL_strategy = st.builds(
    alf_BOOLEAN_LITERAL,
)
alf_NamespaceDefinition_strategy = st.builds(
    alf_NamespaceDefinition,
)
alf_StereotypeAnnotations_strategy = st.builds(
    alf_StereotypeAnnotations,
)
alf_ImportDeclaration_strategy = st.builds(
    alf_ImportDeclaration,
    visibility=
        safe_text
)
alf_NamespaceDeclaration_strategy = st.builds(
    alf_NamespaceDeclaration,
)
alf_UnitDefinition_strategy = st.builds(
    alf_UnitDefinition,
    comment=
        safe_text
)
alf_ImportReference_strategy = st.builds(
    alf_ImportReference,
    star=
        st.booleans()
)

@given(instance=alf_AcceptClause_strategy)
@settings(max_examples=50)
def test_alf_acceptclause_instantiation(instance):
    assert isinstance(instance, alf_AcceptClause)

@given(instance=alf_ReclassifyAllClause_strategy)
@settings(max_examples=50)
def test_alf_reclassifyallclause_instantiation(instance):
    assert isinstance(instance, alf_ReclassifyAllClause)

@given(instance=alf_ClassificationToClause_strategy)
@settings(max_examples=50)
def test_alf_classificationtoclause_instantiation(instance):
    assert isinstance(instance, alf_ClassificationToClause)

@given(instance=alf_ClassificationFromClause_strategy)
@settings(max_examples=50)
def test_alf_classificationfromclause_instantiation(instance):
    assert isinstance(instance, alf_ClassificationFromClause)

@given(instance=alf_ClassificationClause_strategy)
@settings(max_examples=50)
def test_alf_classificationclause_instantiation(instance):
    assert isinstance(instance, alf_ClassificationClause)

@given(instance=alf_AcceptBlock_strategy)
@settings(max_examples=50)
def test_alf_acceptblock_instantiation(instance):
    assert isinstance(instance, alf_AcceptBlock)

@given(instance=alf_CompoundAcceptStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf_compoundacceptstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf_CompoundAcceptStatementCompletion)

@given(instance=alf_SimpleAcceptStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf_simpleacceptstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf_SimpleAcceptStatementCompletion)

@given(instance=alf_NonEmptyStatementSequence_strategy)
@settings(max_examples=50)
def test_alf_nonemptystatementsequence_instantiation(instance):
    assert isinstance(instance, alf_NonEmptyStatementSequence)

@given(instance=alf_SwitchCase_strategy)
@settings(max_examples=50)
def test_alf_switchcase_instantiation(instance):
    assert isinstance(instance, alf_SwitchCase)

@given(instance=alf_SwitchDefaultClause_strategy)
@settings(max_examples=50)
def test_alf_switchdefaultclause_instantiation(instance):
    assert isinstance(instance, alf_SwitchDefaultClause)

@given(instance=alf_SwitchClause_strategy)
@settings(max_examples=50)
def test_alf_switchclause_instantiation(instance):
    assert isinstance(instance, alf_SwitchClause)

@given(instance=alf_LoopVariableDefinition_strategy)
@settings(max_examples=50)
def test_alf_loopvariabledefinition_instantiation(instance):
    assert isinstance(instance, alf_LoopVariableDefinition)

@given(instance=alf_ForControl_strategy)
@settings(max_examples=50)
def test_alf_forcontrol_instantiation(instance):
    assert isinstance(instance, alf_ForControl)

@given(instance=alf_LocalNameDeclarationStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf_localnamedeclarationstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf_LocalNameDeclarationStatementCompletion)

@given(instance=alf_NonFinalClause_strategy)
@settings(max_examples=50)
def test_alf_nonfinalclause_instantiation(instance):
    assert isinstance(instance, alf_NonFinalClause)

@given(instance=alf_ConcurrentClauses_strategy)
@settings(max_examples=50)
def test_alf_concurrentclauses_instantiation(instance):
    assert isinstance(instance, alf_ConcurrentClauses)

@given(instance=alf_FinalClause_strategy)
@settings(max_examples=50)
def test_alf_finalclause_instantiation(instance):
    assert isinstance(instance, alf_FinalClause)

@given(instance=alf_SequentialClauses_strategy)
@settings(max_examples=50)
def test_alf_sequentialclauses_instantiation(instance):
    assert isinstance(instance, alf_SequentialClauses)

@given(instance=alf_NameList_strategy)
@settings(max_examples=50)
def test_alf_namelist_instantiation(instance):
    assert isinstance(instance, alf_NameList)

@given(instance=alf_Annotation_strategy)
@settings(max_examples=50)
def test_alf_annotation_instantiation(instance):
    assert isinstance(instance, alf_Annotation)



@given(instance=alf_Annotation_strategy)
def test_alf_annotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_alf_conditionalexpression_instantiation(instance):
    assert isinstance(instance, alf_ConditionalExpression)

@given(instance=alf_ConditionalOrExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_conditionalorexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ConditionalOrExpressionCompletion)

@given(instance=alf_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_alf_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, alf_ConditionalOrExpression)

@given(instance=alf_Annotations_strategy)
@settings(max_examples=50)
def test_alf_annotations_instantiation(instance):
    assert isinstance(instance, alf_Annotations)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=alf_WhileStatement_strategy)
@settings(max_examples=50)
def test_alf_whilestatement_instantiation(instance):
    assert isinstance(instance, alf_WhileStatement)

@given(instance=alf_BlockStatement_strategy)
@settings(max_examples=50)
def test_alf_blockstatement_instantiation(instance):
    assert isinstance(instance, alf_BlockStatement)

@given(instance=alf_InLineStatement_strategy)
@settings(max_examples=50)
def test_alf_inlinestatement_instantiation(instance):
    assert isinstance(instance, alf_InLineStatement)



@given(instance=alf_InLineStatement_strategy)
def test_alf_inlinestatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf_DoStatement_strategy)
@settings(max_examples=50)
def test_alf_dostatement_instantiation(instance):
    assert isinstance(instance, alf_DoStatement)

@given(instance=alf_LocalNameDeclarationOrExpressionStatement_strategy)
@settings(max_examples=50)
def test_alf_localnamedeclarationorexpressionstatement_instantiation(instance):
    assert isinstance(instance, alf_LocalNameDeclarationOrExpressionStatement)

@given(instance=alf_AcceptStatement_strategy)
@settings(max_examples=50)
def test_alf_acceptstatement_instantiation(instance):
    assert isinstance(instance, alf_AcceptStatement)

@given(instance=alf_BreakStatement_strategy)
@settings(max_examples=50)
def test_alf_breakstatement_instantiation(instance):
    assert isinstance(instance, alf_BreakStatement)

@given(instance=alf_ForStatement_strategy)
@settings(max_examples=50)
def test_alf_forstatement_instantiation(instance):
    assert isinstance(instance, alf_ForStatement)

@given(instance=alf_LocalNameDeclarationStatement_strategy)
@settings(max_examples=50)
def test_alf_localnamedeclarationstatement_instantiation(instance):
    assert isinstance(instance, alf_LocalNameDeclarationStatement)

@given(instance=alf_IfStatement_strategy)
@settings(max_examples=50)
def test_alf_ifstatement_instantiation(instance):
    assert isinstance(instance, alf_IfStatement)

@given(instance=alf_EmptyStatement_strategy)
@settings(max_examples=50)
def test_alf_emptystatement_instantiation(instance):
    assert isinstance(instance, alf_EmptyStatement)

@given(instance=alf_ClassifyStatement_strategy)
@settings(max_examples=50)
def test_alf_classifystatement_instantiation(instance):
    assert isinstance(instance, alf_ClassifyStatement)

@given(instance=alf_ReturnStatement_strategy)
@settings(max_examples=50)
def test_alf_returnstatement_instantiation(instance):
    assert isinstance(instance, alf_ReturnStatement)

@given(instance=alf_SwitchStatement_strategy)
@settings(max_examples=50)
def test_alf_switchstatement_instantiation(instance):
    assert isinstance(instance, alf_SwitchStatement)

@given(instance=alf_AnnotatedStatement_strategy)
@settings(max_examples=50)
def test_alf_annotatedstatement_instantiation(instance):
    assert isinstance(instance, alf_AnnotatedStatement)

@given(instance=alf_Statement_strategy)
@settings(max_examples=50)
def test_alf_statement_instantiation(instance):
    assert isinstance(instance, alf_Statement)

@given(instance=alf_DocumentedStatement_strategy)
@settings(max_examples=50)
def test_alf_documentedstatement_instantiation(instance):
    assert isinstance(instance, alf_DocumentedStatement)



@given(instance=alf_DocumentedStatement_strategy)
def test_alf_documentedstatement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf_StatementSequence_strategy)
@settings(max_examples=50)
def test_alf_statementsequence_instantiation(instance):
    assert isinstance(instance, alf_StatementSequence)

@given(instance=ExpressionCompletion_strategy)
@settings(max_examples=50)
def test_expressioncompletion_instantiation(instance):
    assert isinstance(instance, ExpressionCompletion)

@given(instance=alf_AssignmentExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_assignmentexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_AssignmentExpressionCompletion)



@given(instance=alf_AssignmentExpressionCompletion_strategy)
def test_alf_assignmentexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_ConditionalExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_conditionalexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ConditionalExpressionCompletion)

@given(instance=alf_AndExpression_strategy)
@settings(max_examples=50)
def test_alf_andexpression_instantiation(instance):
    assert isinstance(instance, alf_AndExpression)

@given(instance=alf_EqualityExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_equalityexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_EqualityExpressionCompletion)



@given(instance=alf_EqualityExpressionCompletion_strategy)
def test_alf_equalityexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_ConditionalAndExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_conditionalandexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ConditionalAndExpressionCompletion)

@given(instance=alf_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_alf_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, alf_ConditionalAndExpression)

@given(instance=alf_InclusiveOrExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_inclusiveorexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_InclusiveOrExpressionCompletion)

@given(instance=alf_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf_InclusiveOrExpression)

@given(instance=alf_ExclusiveOrExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_exclusiveorexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ExclusiveOrExpressionCompletion)

@given(instance=alf_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf_ExclusiveOrExpression)

@given(instance=alf_AndExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_andexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_AndExpressionCompletion)

@given(instance=alf_ShiftExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_shiftexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ShiftExpressionCompletion)



@given(instance=alf_ShiftExpressionCompletion_strategy)
def test_alf_shiftexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_ShiftExpression_strategy)
@settings(max_examples=50)
def test_alf_shiftexpression_instantiation(instance):
    assert isinstance(instance, alf_ShiftExpression)

@given(instance=alf_EqualityExpression_strategy)
@settings(max_examples=50)
def test_alf_equalityexpression_instantiation(instance):
    assert isinstance(instance, alf_EqualityExpression)

@given(instance=alf_ClassificationExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_classificationexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ClassificationExpressionCompletion)



@given(instance=alf_ClassificationExpressionCompletion_strategy)
def test_alf_classificationexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_ClassificationExpression_strategy)
@settings(max_examples=50)
def test_alf_classificationexpression_instantiation(instance):
    assert isinstance(instance, alf_ClassificationExpression)

@given(instance=alf_RelationalExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_relationalexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_RelationalExpressionCompletion)



@given(instance=alf_RelationalExpressionCompletion_strategy)
def test_alf_relationalexpressioncompletion_relationalOperator_setter(instance):
    original = instance.relationalOperator
    instance.relationalOperator = original
    assert instance.relationalOperator == original

@given(instance=alf_RelationalExpression_strategy)
@settings(max_examples=50)
def test_alf_relationalexpression_instantiation(instance):
    assert isinstance(instance, alf_RelationalExpression)

@given(instance=alf_AdditiveExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_additiveexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_AdditiveExpressionCompletion)



@given(instance=alf_AdditiveExpressionCompletion_strategy)
def test_alf_additiveexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_alf_additiveexpression_instantiation(instance):
    assert isinstance(instance, alf_AdditiveExpression)

@given(instance=alf_MultiplicativeExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_multiplicativeexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_MultiplicativeExpressionCompletion)



@given(instance=alf_MultiplicativeExpressionCompletion_strategy)
def test_alf_multiplicativeexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_alf_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, alf_MultiplicativeExpression)

@given(instance=alf_CastCompletion_strategy)
@settings(max_examples=50)
def test_alf_castcompletion_instantiation(instance):
    assert isinstance(instance, alf_CastCompletion)

@given(instance=NonNameUnaryExpression_strategy)
@settings(max_examples=50)
def test_nonnameunaryexpression_instantiation(instance):
    assert isinstance(instance, NonNameUnaryExpression)

@given(instance=alf_NonNamePostfixOrCastExpression_strategy)
@settings(max_examples=50)
def test_alf_nonnamepostfixorcastexpression_instantiation(instance):
    assert isinstance(instance, alf_NonNamePostfixOrCastExpression)



@given(instance=alf_NonNamePostfixOrCastExpression_strategy)
def test_alf_nonnamepostfixorcastexpression_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=CastCompletion_strategy)
@settings(max_examples=50)
def test_castcompletion_instantiation(instance):
    assert isinstance(instance, CastCompletion)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=alf_NonPostfixNonCastUnaryExpression_strategy)
@settings(max_examples=50)
def test_alf_nonpostfixnoncastunaryexpression_instantiation(instance):
    assert isinstance(instance, alf_NonPostfixNonCastUnaryExpression)

@given(instance=alf_PostfixOrCastExpression_strategy)
@settings(max_examples=50)
def test_alf_postfixorcastexpression_instantiation(instance):
    assert isinstance(instance, alf_PostfixOrCastExpression)

@given(instance=NonPostfixNonCastUnaryExpression_strategy)
@settings(max_examples=50)
def test_nonpostfixnoncastunaryexpression_instantiation(instance):
    assert isinstance(instance, NonPostfixNonCastUnaryExpression)

@given(instance=alf_BitStringComplementExpression_strategy)
@settings(max_examples=50)
def test_alf_bitstringcomplementexpression_instantiation(instance):
    assert isinstance(instance, alf_BitStringComplementExpression)

@given(instance=alf_NumericUnaryExpression_strategy)
@settings(max_examples=50)
def test_alf_numericunaryexpression_instantiation(instance):
    assert isinstance(instance, alf_NumericUnaryExpression)



@given(instance=alf_NumericUnaryExpression_strategy)
def test_alf_numericunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_IsolationExpression_strategy)
@settings(max_examples=50)
def test_alf_isolationexpression_instantiation(instance):
    assert isinstance(instance, alf_IsolationExpression)

@given(instance=alf_BooleanNegationExpression_strategy)
@settings(max_examples=50)
def test_alf_booleannegationexpression_instantiation(instance):
    assert isinstance(instance, alf_BooleanNegationExpression)

@given(instance=alf_PrefixExpression_strategy)
@settings(max_examples=50)
def test_alf_prefixexpression_instantiation(instance):
    assert isinstance(instance, alf_PrefixExpression)



@given(instance=alf_PrefixExpression_strategy)
def test_alf_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_PostfixOperation_strategy)
@settings(max_examples=50)
def test_alf_postfixoperation_instantiation(instance):
    assert isinstance(instance, alf_PostfixOperation)



@given(instance=alf_PostfixOperation_strategy)
def test_alf_postfixoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf_EObject_strategy)
@settings(max_examples=50)
def test_alf_eobject_instantiation(instance):
    assert isinstance(instance, alf_EObject)

@given(instance=alf_SequenceElement_strategy)
@settings(max_examples=50)
def test_alf_sequenceelement_instantiation(instance):
    assert isinstance(instance, alf_SequenceElement)

@given(instance=alf_SequenceElementListCompletion_strategy)
@settings(max_examples=50)
def test_alf_sequenceelementlistcompletion_instantiation(instance):
    assert isinstance(instance, alf_SequenceElementListCompletion)

@given(instance=alf_SequenceElements_strategy)
@settings(max_examples=50)
def test_alf_sequenceelements_instantiation(instance):
    assert isinstance(instance, alf_SequenceElements)

@given(instance=alf_MultiplicityIndicator_strategy)
@settings(max_examples=50)
def test_alf_multiplicityindicator_instantiation(instance):
    assert isinstance(instance, alf_MultiplicityIndicator)

@given(instance=alf_IndexedNamedExpression_strategy)
@settings(max_examples=50)
def test_alf_indexednamedexpression_instantiation(instance):
    assert isinstance(instance, alf_IndexedNamedExpression)

@given(instance=alf_IndexedNamedExpressionListCompletion_strategy)
@settings(max_examples=50)
def test_alf_indexednamedexpressionlistcompletion_instantiation(instance):
    assert isinstance(instance, alf_IndexedNamedExpressionListCompletion)

@given(instance=alf_LinkOperationTuple_strategy)
@settings(max_examples=50)
def test_alf_linkoperationtuple_instantiation(instance):
    assert isinstance(instance, alf_LinkOperationTuple)

@given(instance=BaseExpression_strategy)
@settings(max_examples=50)
def test_baseexpression_instantiation(instance):
    assert isinstance(instance, BaseExpression)

@given(instance=alf_InstanceCreationOrSequenceConstructionExpression_strategy)
@settings(max_examples=50)
def test_alf_instancecreationorsequenceconstructionexpression_instantiation(instance):
    assert isinstance(instance, alf_InstanceCreationOrSequenceConstructionExpression)

@given(instance=alf_SuperInvocationExpression_strategy)
@settings(max_examples=50)
def test_alf_superinvocationexpression_instantiation(instance):
    assert isinstance(instance, alf_SuperInvocationExpression)

@given(instance=alf_SequenceAnyExpression_strategy)
@settings(max_examples=50)
def test_alf_sequenceanyexpression_instantiation(instance):
    assert isinstance(instance, alf_SequenceAnyExpression)

@given(instance=alf_LiteralExpression_strategy)
@settings(max_examples=50)
def test_alf_literalexpression_instantiation(instance):
    assert isinstance(instance, alf_LiteralExpression)

@given(instance=alf_Index_strategy)
@settings(max_examples=50)
def test_alf_index_instantiation(instance):
    assert isinstance(instance, alf_Index)

@given(instance=alf_NamedExpression_strategy)
@settings(max_examples=50)
def test_alf_namedexpression_instantiation(instance):
    assert isinstance(instance, alf_NamedExpression)

@given(instance=alf_PositionalTupleExpressionListCompletion_strategy)
@settings(max_examples=50)
def test_alf_positionaltupleexpressionlistcompletion_instantiation(instance):
    assert isinstance(instance, alf_PositionalTupleExpressionListCompletion)

@given(instance=alf_PositionalTupleExpressionList_strategy)
@settings(max_examples=50)
def test_alf_positionaltupleexpressionlist_instantiation(instance):
    assert isinstance(instance, alf_PositionalTupleExpressionList)

@given(instance=alf_NamedTupleExpressionList_strategy)
@settings(max_examples=50)
def test_alf_namedtupleexpressionlist_instantiation(instance):
    assert isinstance(instance, alf_NamedTupleExpressionList)

@given(instance=alf_Tuple_strategy)
@settings(max_examples=50)
def test_alf_tuple_instantiation(instance):
    assert isinstance(instance, alf_Tuple)

@given(instance=alf_ThisExpression_strategy)
@settings(max_examples=50)
def test_alf_thisexpression_instantiation(instance):
    assert isinstance(instance, alf_ThisExpression)

@given(instance=alf_ExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_expressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ExpressionCompletion)

@given(instance=alf_UnaryExpression_strategy)
@settings(max_examples=50)
def test_alf_unaryexpression_instantiation(instance):
    assert isinstance(instance, alf_UnaryExpression)

@given(instance=InitializationExpression_strategy)
@settings(max_examples=50)
def test_initializationexpression_instantiation(instance):
    assert isinstance(instance, InitializationExpression)

@given(instance=alf_InstanceInitializationExpression_strategy)
@settings(max_examples=50)
def test_alf_instanceinitializationexpression_instantiation(instance):
    assert isinstance(instance, alf_InstanceInitializationExpression)

@given(instance=alf_SequenceInitializationExpression_strategy)
@settings(max_examples=50)
def test_alf_sequenceinitializationexpression_instantiation(instance):
    assert isinstance(instance, alf_SequenceInitializationExpression)



@given(instance=alf_SequenceInitializationExpression_strategy)
def test_alf_sequenceinitializationexpression_isNew_setter(instance):
    original = instance.isNew
    instance.isNew = original
    assert instance.isNew == original

@given(instance=alf_Expression_strategy)
@settings(max_examples=50)
def test_alf_expression_instantiation(instance):
    assert isinstance(instance, alf_Expression)

@given(instance=alf_SequenceOperationOrReductionOrExpansion_strategy)
@settings(max_examples=50)
def test_alf_sequenceoperationorreductionorexpansion_instantiation(instance):
    assert isinstance(instance, alf_SequenceOperationOrReductionOrExpansion)



@given(instance=alf_SequenceOperationOrReductionOrExpansion_strategy)
def test_alf_sequenceoperationorreductionorexpansion_isReduce_setter(instance):
    original = instance.isReduce
    instance.isReduce = original
    assert instance.isReduce == original



@given(instance=alf_SequenceOperationOrReductionOrExpansion_strategy)
def test_alf_sequenceoperationorreductionorexpansion_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=alf_SequenceOperationOrReductionOrExpansion_strategy)
def test_alf_sequenceoperationorreductionorexpansion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf_FeatureInvocation_strategy)
@settings(max_examples=50)
def test_alf_featureinvocation_instantiation(instance):
    assert isinstance(instance, alf_FeatureInvocation)

@given(instance=alf_Feature_strategy)
@settings(max_examples=50)
def test_alf_feature_instantiation(instance):
    assert isinstance(instance, alf_Feature)

@given(instance=alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index_strategy)
@settings(max_examples=50)
def test_alf_feature_or_sequenceoperationorreductionorexpansion_or_index_instantiation(instance):
    assert isinstance(instance, alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index)

@given(instance=alf_BehaviorInvocation_strategy)
@settings(max_examples=50)
def test_alf_behaviorinvocation_instantiation(instance):
    assert isinstance(instance, alf_BehaviorInvocation)

@given(instance=alf_SequenceConstructionExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_sequenceconstructionexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_SequenceConstructionExpressionCompletion)

@given(instance=alf_ClassExtentExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_classextentexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_ClassExtentExpressionCompletion)

@given(instance=alf_LinkOperationCompletion_strategy)
@settings(max_examples=50)
def test_alf_linkoperationcompletion_instantiation(instance):
    assert isinstance(instance, alf_LinkOperationCompletion)



@given(instance=alf_LinkOperationCompletion_strategy)
def test_alf_linkoperationcompletion_linkOperation_setter(instance):
    original = instance.linkOperation
    instance.linkOperation = original
    assert instance.linkOperation == original

@given(instance=alf_PrimaryExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_primaryexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_PrimaryExpressionCompletion)

@given(instance=alf_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_alf_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, alf_ParenthesizedExpression)

@given(instance=alf_BaseExpression_strategy)
@settings(max_examples=50)
def test_alf_baseexpression_instantiation(instance):
    assert isinstance(instance, alf_BaseExpression)

@given(instance=alf_NameOrPrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf_nameorprimaryexpression_instantiation(instance):
    assert isinstance(instance, alf_NameOrPrimaryExpression)

@given(instance=alf_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf_primaryexpression_instantiation(instance):
    assert isinstance(instance, alf_PrimaryExpression)

@given(instance=alf_PostfixExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_postfixexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_PostfixExpressionCompletion)

@given(instance=alf_PrimaryToExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_primarytoexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_PrimaryToExpressionCompletion)

@given(instance=alf_NameToPrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf_nametoprimaryexpression_instantiation(instance):
    assert isinstance(instance, alf_NameToPrimaryExpression)

@given(instance=alf_NameToExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf_nametoexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf_NameToExpressionCompletion)

@given(instance=alf_NonNameUnaryExpression_strategy)
@settings(max_examples=50)
def test_alf_nonnameunaryexpression_instantiation(instance):
    assert isinstance(instance, alf_NonNameUnaryExpression)

@given(instance=alf_NonNameExpression_strategy)
@settings(max_examples=50)
def test_alf_nonnameexpression_instantiation(instance):
    assert isinstance(instance, alf_NonNameExpression)

@given(instance=alf_SignalReceptionDeclaration_strategy)
@settings(max_examples=50)
def test_alf_signalreceptiondeclaration_instantiation(instance):
    assert isinstance(instance, alf_SignalReceptionDeclaration)

@given(instance=alf_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_alf_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, alf_TemplateParameterSubstitution)

@given(instance=TemplateBinding_strategy)
@settings(max_examples=50)
def test_templatebinding_instantiation(instance):
    assert isinstance(instance, TemplateBinding)

@given(instance=alf_NamedTemplateBinding_strategy)
@settings(max_examples=50)
def test_alf_namedtemplatebinding_instantiation(instance):
    assert isinstance(instance, alf_NamedTemplateBinding)

@given(instance=alf_PositionalTemplateBinding_strategy)
@settings(max_examples=50)
def test_alf_positionaltemplatebinding_instantiation(instance):
    assert isinstance(instance, alf_PositionalTemplateBinding)

@given(instance=alf_ColonQualifiedNameCompletionWithoutBinding_strategy)
@settings(max_examples=50)
def test_alf_colonqualifiednamecompletionwithoutbinding_instantiation(instance):
    assert isinstance(instance, alf_ColonQualifiedNameCompletionWithoutBinding)

@given(instance=alf_QualifiedNameWithoutBinding_strategy)
@settings(max_examples=50)
def test_alf_qualifiednamewithoutbinding_instantiation(instance):
    assert isinstance(instance, alf_QualifiedNameWithoutBinding)

@given(instance=alf_TemplateBinding_strategy)
@settings(max_examples=50)
def test_alf_templatebinding_instantiation(instance):
    assert isinstance(instance, alf_TemplateBinding)

@given(instance=UnqualifiedName_strategy)
@settings(max_examples=50)
def test_unqualifiedname_instantiation(instance):
    assert isinstance(instance, UnqualifiedName)

@given(instance=alf_NameBinding_strategy)
@settings(max_examples=50)
def test_alf_namebinding_instantiation(instance):
    assert isinstance(instance, alf_NameBinding)

@given(instance=alf_ColonQualifiedNameCompletion_strategy)
@settings(max_examples=50)
def test_alf_colonqualifiednamecompletion_instantiation(instance):
    assert isinstance(instance, alf_ColonQualifiedNameCompletion)

@given(instance=alf_UnqualifiedName_strategy)
@settings(max_examples=50)
def test_alf_unqualifiedname_instantiation(instance):
    assert isinstance(instance, alf_UnqualifiedName)

@given(instance=alf_InitializationExpression_strategy)
@settings(max_examples=50)
def test_alf_initializationexpression_instantiation(instance):
    assert isinstance(instance, alf_InitializationExpression)

@given(instance=ActiveFeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_activefeaturedefinitionorstub_instantiation(instance):
    assert isinstance(instance, ActiveFeatureDefinitionOrStub)

@given(instance=alf_SignalReceptionDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_signalreceptiondefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_SignalReceptionDefinitionOrStub)

@given(instance=alf_ReceptionDefinition_strategy)
@settings(max_examples=50)
def test_alf_receptiondefinition_instantiation(instance):
    assert isinstance(instance, alf_ReceptionDefinition)

@given(instance=alf_AttributeInitializer_strategy)
@settings(max_examples=50)
def test_alf_attributeinitializer_instantiation(instance):
    assert isinstance(instance, alf_AttributeInitializer)

@given(instance=alf_RedefinitionClause_strategy)
@settings(max_examples=50)
def test_alf_redefinitionclause_instantiation(instance):
    assert isinstance(instance, alf_RedefinitionClause)

@given(instance=OperationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_operationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, OperationDefinitionOrStub)

@given(instance=alf_OperationDeclaration_strategy)
@settings(max_examples=50)
def test_alf_operationdeclaration_instantiation(instance):
    assert isinstance(instance, alf_OperationDeclaration)



@given(instance=alf_OperationDeclaration_strategy)
def test_alf_operationdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf_UnlimitedNaturalLiteral_strategy)
@settings(max_examples=50)
def test_alf_unlimitednaturalliteral_instantiation(instance):
    assert isinstance(instance, alf_UnlimitedNaturalLiteral)



@given(instance=alf_UnlimitedNaturalLiteral_strategy)
def test_alf_unlimitednaturalliteral_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=alf_MultiplicityRange_strategy)
@settings(max_examples=50)
def test_alf_multiplicityrange_instantiation(instance):
    assert isinstance(instance, alf_MultiplicityRange)

@given(instance=alf_Multiplicity_strategy)
@settings(max_examples=50)
def test_alf_multiplicity_instantiation(instance):
    assert isinstance(instance, alf_Multiplicity)



@given(instance=alf_Multiplicity_strategy)
def test_alf_multiplicity_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=alf_Multiplicity_strategy)
def test_alf_multiplicity_isSequence_setter(instance):
    original = instance.isSequence
    instance.isSequence = original
    assert instance.isSequence == original



@given(instance=alf_Multiplicity_strategy)
def test_alf_multiplicity_isNonUnique_setter(instance):
    original = instance.isNonUnique
    instance.isNonUnique = original
    assert instance.isNonUnique == original

@given(instance=alf_TypeName_strategy)
@settings(max_examples=50)
def test_alf_typename_instantiation(instance):
    assert isinstance(instance, alf_TypeName)



@given(instance=alf_TypeName_strategy)
def test_alf_typename_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=alf_TypePart_strategy)
@settings(max_examples=50)
def test_alf_typepart_instantiation(instance):
    assert isinstance(instance, alf_TypePart)

@given(instance=alf_FormalParameters_strategy)
@settings(max_examples=50)
def test_alf_formalparameters_instantiation(instance):
    assert isinstance(instance, alf_FormalParameters)

@given(instance=FeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_featuredefinitionorstub_instantiation(instance):
    assert isinstance(instance, FeatureDefinitionOrStub)

@given(instance=alf_OperationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_operationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_OperationDefinitionOrStub)

@given(instance=alf_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_alf_attributedefinition_instantiation(instance):
    assert isinstance(instance, alf_AttributeDefinition)

@given(instance=alf_PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_alf_propertydeclaration_instantiation(instance):
    assert isinstance(instance, alf_PropertyDeclaration)



@given(instance=alf_PropertyDeclaration_strategy)
def test_alf_propertydeclaration_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=alf_FormalParameter_strategy)
@settings(max_examples=50)
def test_alf_formalparameter_instantiation(instance):
    assert isinstance(instance, alf_FormalParameter)



@given(instance=alf_FormalParameter_strategy)
def test_alf_formalparameter_parameterDirection_setter(instance):
    original = instance.parameterDirection
    instance.parameterDirection = original
    assert instance.parameterDirection == original



@given(instance=alf_FormalParameter_strategy)
def test_alf_formalparameter_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf_FormalParameterList_strategy)
@settings(max_examples=50)
def test_alf_formalparameterlist_instantiation(instance):
    assert isinstance(instance, alf_FormalParameterList)

@given(instance=alf_AssociationDeclaration_strategy)
@settings(max_examples=50)
def test_alf_associationdeclaration_instantiation(instance):
    assert isinstance(instance, alf_AssociationDeclaration)



@given(instance=alf_AssociationDeclaration_strategy)
def test_alf_associationdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf_PropertyDefinition_strategy)
@settings(max_examples=50)
def test_alf_propertydefinition_instantiation(instance):
    assert isinstance(instance, alf_PropertyDefinition)

@given(instance=alf_ActivityDeclaration_strategy)
@settings(max_examples=50)
def test_alf_activitydeclaration_instantiation(instance):
    assert isinstance(instance, alf_ActivityDeclaration)

@given(instance=alf_SignalDeclaration_strategy)
@settings(max_examples=50)
def test_alf_signaldeclaration_instantiation(instance):
    assert isinstance(instance, alf_SignalDeclaration)



@given(instance=alf_SignalDeclaration_strategy)
def test_alf_signaldeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf_EnumerationLiteralName_strategy)
@settings(max_examples=50)
def test_alf_enumerationliteralname_instantiation(instance):
    assert isinstance(instance, alf_EnumerationLiteralName)



@given(instance=alf_EnumerationLiteralName_strategy)
def test_alf_enumerationliteralname_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf_EnumerationBody_strategy)
@settings(max_examples=50)
def test_alf_enumerationbody_instantiation(instance):
    assert isinstance(instance, alf_EnumerationBody)

@given(instance=alf_EnumerationDeclaration_strategy)
@settings(max_examples=50)
def test_alf_enumerationdeclaration_instantiation(instance):
    assert isinstance(instance, alf_EnumerationDeclaration)

@given(instance=alf_ActiveClassBody_strategy)
@settings(max_examples=50)
def test_alf_activeclassbody_instantiation(instance):
    assert isinstance(instance, alf_ActiveClassBody)

@given(instance=alf_StructuredMember_strategy)
@settings(max_examples=50)
def test_alf_structuredmember_instantiation(instance):
    assert isinstance(instance, alf_StructuredMember)



@given(instance=alf_StructuredMember_strategy)
def test_alf_structuredmember_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=alf_StructuredMember_strategy)
def test_alf_structuredmember_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=alf_StructuredBody_strategy)
@settings(max_examples=50)
def test_alf_structuredbody_instantiation(instance):
    assert isinstance(instance, alf_StructuredBody)

@given(instance=alf_DataTypeDeclaration_strategy)
@settings(max_examples=50)
def test_alf_datatypedeclaration_instantiation(instance):
    assert isinstance(instance, alf_DataTypeDeclaration)



@given(instance=alf_DataTypeDeclaration_strategy)
def test_alf_datatypedeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf_ActiveClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_alf_activeclassmemberdefinition_instantiation(instance):
    assert isinstance(instance, alf_ActiveClassMemberDefinition)

@given(instance=alf_Block_strategy)
@settings(max_examples=50)
def test_alf_block_instantiation(instance):
    assert isinstance(instance, alf_Block)

@given(instance=alf_BehaviorClause_strategy)
@settings(max_examples=50)
def test_alf_behaviorclause_instantiation(instance):
    assert isinstance(instance, alf_BehaviorClause)

@given(instance=alf_ActiveClassMember_strategy)
@settings(max_examples=50)
def test_alf_activeclassmember_instantiation(instance):
    assert isinstance(instance, alf_ActiveClassMember)



@given(instance=alf_ActiveClassMember_strategy)
def test_alf_activeclassmember_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf_PackagedElementDefinition_strategy)
@settings(max_examples=50)
def test_alf_packagedelementdefinition_instantiation(instance):
    assert isinstance(instance, alf_PackagedElementDefinition)

@given(instance=alf_ActiveClassDeclaration_strategy)
@settings(max_examples=50)
def test_alf_activeclassdeclaration_instantiation(instance):
    assert isinstance(instance, alf_ActiveClassDeclaration)



@given(instance=alf_ActiveClassDeclaration_strategy)
def test_alf_activeclassdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf_PackagedElement_strategy)
@settings(max_examples=50)
def test_alf_packagedelement_instantiation(instance):
    assert isinstance(instance, alf_PackagedElement)



@given(instance=alf_PackagedElement_strategy)
def test_alf_packagedelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=alf_PackagedElement_strategy)
def test_alf_packagedelement_importVisibilityIndicator_setter(instance):
    original = instance.importVisibilityIndicator
    instance.importVisibilityIndicator = original
    assert instance.importVisibilityIndicator == original

@given(instance=ActiveClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_activeclassmemberdefinition_instantiation(instance):
    assert isinstance(instance, ActiveClassMemberDefinition)

@given(instance=alf_ActiveFeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_activefeaturedefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_ActiveFeatureDefinitionOrStub)

@given(instance=alf_ClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_alf_classmemberdefinition_instantiation(instance):
    assert isinstance(instance, alf_ClassMemberDefinition)

@given(instance=alf_ClassMember_strategy)
@settings(max_examples=50)
def test_alf_classmember_instantiation(instance):
    assert isinstance(instance, alf_ClassMember)



@given(instance=alf_ClassMember_strategy)
def test_alf_classmember_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ClassifierDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_classifierdefinitionorstub_instantiation(instance):
    assert isinstance(instance, ClassifierDefinitionOrStub)

@given(instance=alf_ActivityDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_activitydefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_ActivityDefinitionOrStub)

@given(instance=alf_AssociationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_associationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_AssociationDefinitionOrStub)

@given(instance=alf_ActiveClassDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_activeclassdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_ActiveClassDefinitionOrStub)

@given(instance=alf_DataTypeDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_datatypedefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_DataTypeDefinitionOrStub)

@given(instance=alf_SignalDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_signaldefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_SignalDefinitionOrStub)

@given(instance=alf_EnumerationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_enumerationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_EnumerationDefinitionOrStub)

@given(instance=alf_ClassDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_classdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_ClassDefinitionOrStub)

@given(instance=alf_ClassBody_strategy)
@settings(max_examples=50)
def test_alf_classbody_instantiation(instance):
    assert isinstance(instance, alf_ClassBody)

@given(instance=ClassifierDefinition_strategy)
@settings(max_examples=50)
def test_classifierdefinition_instantiation(instance):
    assert isinstance(instance, ClassifierDefinition)

@given(instance=alf_SignalDefinition_strategy)
@settings(max_examples=50)
def test_alf_signaldefinition_instantiation(instance):
    assert isinstance(instance, alf_SignalDefinition)

@given(instance=alf_DataTypeDefinition_strategy)
@settings(max_examples=50)
def test_alf_datatypedefinition_instantiation(instance):
    assert isinstance(instance, alf_DataTypeDefinition)

@given(instance=alf_ActivityDefinition_strategy)
@settings(max_examples=50)
def test_alf_activitydefinition_instantiation(instance):
    assert isinstance(instance, alf_ActivityDefinition)

@given(instance=alf_EnumerationDefinition_strategy)
@settings(max_examples=50)
def test_alf_enumerationdefinition_instantiation(instance):
    assert isinstance(instance, alf_EnumerationDefinition)

@given(instance=alf_ActiveClassDefinition_strategy)
@settings(max_examples=50)
def test_alf_activeclassdefinition_instantiation(instance):
    assert isinstance(instance, alf_ActiveClassDefinition)

@given(instance=alf_AssociationDefinition_strategy)
@settings(max_examples=50)
def test_alf_associationdefinition_instantiation(instance):
    assert isinstance(instance, alf_AssociationDefinition)

@given(instance=alf_ClassDefinition_strategy)
@settings(max_examples=50)
def test_alf_classdefinition_instantiation(instance):
    assert isinstance(instance, alf_ClassDefinition)

@given(instance=alf_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_alf_classdeclaration_instantiation(instance):
    assert isinstance(instance, alf_ClassDeclaration)



@given(instance=alf_ClassDeclaration_strategy)
def test_alf_classdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf_ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_alf_classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, alf_ClassifierTemplateParameter)



@given(instance=alf_ClassifierTemplateParameter_strategy)
def test_alf_classifiertemplateparameter_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf_SpecializationClause_strategy)
@settings(max_examples=50)
def test_alf_specializationclause_instantiation(instance):
    assert isinstance(instance, alf_SpecializationClause)

@given(instance=PackagedElementDefinition_strategy)
@settings(max_examples=50)
def test_packagedelementdefinition_instantiation(instance):
    assert isinstance(instance, PackagedElementDefinition)

@given(instance=alf_PackageDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_packagedefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_PackageDefinitionOrStub)

@given(instance=alf_TemplateParameters_strategy)
@settings(max_examples=50)
def test_alf_templateparameters_instantiation(instance):
    assert isinstance(instance, alf_TemplateParameters)

@given(instance=alf_PackageBody_strategy)
@settings(max_examples=50)
def test_alf_packagebody_instantiation(instance):
    assert isinstance(instance, alf_PackageBody)

@given(instance=alf_ClassifierSignature_strategy)
@settings(max_examples=50)
def test_alf_classifiersignature_instantiation(instance):
    assert isinstance(instance, alf_ClassifierSignature)

@given(instance=ClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_classmemberdefinition_instantiation(instance):
    assert isinstance(instance, ClassMemberDefinition)

@given(instance=alf_ClassifierDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_classifierdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_ClassifierDefinitionOrStub)

@given(instance=alf_FeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf_featuredefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf_FeatureDefinitionOrStub)

@given(instance=NamespaceDefinition_strategy)
@settings(max_examples=50)
def test_namespacedefinition_instantiation(instance):
    assert isinstance(instance, NamespaceDefinition)

@given(instance=alf_ClassifierDefinition_strategy)
@settings(max_examples=50)
def test_alf_classifierdefinition_instantiation(instance):
    assert isinstance(instance, alf_ClassifierDefinition)

@given(instance=alf_PackageDefinition_strategy)
@settings(max_examples=50)
def test_alf_packagedefinition_instantiation(instance):
    assert isinstance(instance, alf_PackageDefinition)

@given(instance=alf_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_alf_packagedeclaration_instantiation(instance):
    assert isinstance(instance, alf_PackageDeclaration)

@given(instance=alf_VisibilityIndicator_strategy)
@settings(max_examples=50)
def test_alf_visibilityindicator_instantiation(instance):
    assert isinstance(instance, alf_VisibilityIndicator)



@given(instance=alf_VisibilityIndicator_strategy)
def test_alf_visibilityindicator_PRIVATE_setter(instance):
    original = instance.PRIVATE
    instance.PRIVATE = original
    assert instance.PRIVATE == original



@given(instance=alf_VisibilityIndicator_strategy)
def test_alf_visibilityindicator_PROTECTED_setter(instance):
    original = instance.PROTECTED
    instance.PROTECTED = original
    assert instance.PROTECTED == original



@given(instance=alf_VisibilityIndicator_strategy)
def test_alf_visibilityindicator_PUBLIC_setter(instance):
    original = instance.PUBLIC
    instance.PUBLIC = original
    assert instance.PUBLIC == original

@given(instance=ImportReferenceQualifiedNameCompletion_strategy)
@settings(max_examples=50)
def test_importreferencequalifiednamecompletion_instantiation(instance):
    assert isinstance(instance, ImportReferenceQualifiedNameCompletion)

@given(instance=alf_ColonQualifiedNameCompletionOfImportReference_strategy)
@settings(max_examples=50)
def test_alf_colonqualifiednamecompletionofimportreference_instantiation(instance):
    assert isinstance(instance, alf_ColonQualifiedNameCompletionOfImportReference)



@given(instance=alf_ColonQualifiedNameCompletionOfImportReference_strategy)
def test_alf_colonqualifiednamecompletionofimportreference_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=alf_AliasDefinition_strategy)
@settings(max_examples=50)
def test_alf_aliasdefinition_instantiation(instance):
    assert isinstance(instance, alf_AliasDefinition)

@given(instance=alf_ImportReferenceQualifiedNameCompletion_strategy)
@settings(max_examples=50)
def test_alf_importreferencequalifiednamecompletion_instantiation(instance):
    assert isinstance(instance, alf_ImportReferenceQualifiedNameCompletion)

@given(instance=alf_Name_strategy)
@settings(max_examples=50)
def test_alf_name_instantiation(instance):
    assert isinstance(instance, alf_Name)



@given(instance=alf_Name_strategy)
def test_alf_name_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf_PRIMITIVE_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_primitive_literal_instantiation(instance):
    assert isinstance(instance, alf_PRIMITIVE_LITERAL)



@given(instance=alf_PRIMITIVE_LITERAL_strategy)
def test_alf_primitive_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf_TaggedValue_strategy)
@settings(max_examples=50)
def test_alf_taggedvalue_instantiation(instance):
    assert isinstance(instance, alf_TaggedValue)

@given(instance=TaggedValues_strategy)
@settings(max_examples=50)
def test_taggedvalues_instantiation(instance):
    assert isinstance(instance, TaggedValues)

@given(instance=alf_QualifiedNameList_strategy)
@settings(max_examples=50)
def test_alf_qualifiednamelist_instantiation(instance):
    assert isinstance(instance, alf_QualifiedNameList)

@given(instance=alf_TaggedValueList_strategy)
@settings(max_examples=50)
def test_alf_taggedvaluelist_instantiation(instance):
    assert isinstance(instance, alf_TaggedValueList)

@given(instance=alf_TaggedValues_strategy)
@settings(max_examples=50)
def test_alf_taggedvalues_instantiation(instance):
    assert isinstance(instance, alf_TaggedValues)

@given(instance=alf_QualifiedName_strategy)
@settings(max_examples=50)
def test_alf_qualifiedname_instantiation(instance):
    assert isinstance(instance, alf_QualifiedName)

@given(instance=alf_StereotypeAnnotation_strategy)
@settings(max_examples=50)
def test_alf_stereotypeannotation_instantiation(instance):
    assert isinstance(instance, alf_StereotypeAnnotation)

@given(instance=NUMBER_LITERAL_strategy)
@settings(max_examples=50)
def test_number_literal_instantiation(instance):
    assert isinstance(instance, NUMBER_LITERAL)

@given(instance=alf_UNLIMITED_NATURAL_strategy)
@settings(max_examples=50)
def test_alf_unlimited_natural_instantiation(instance):
    assert isinstance(instance, alf_UNLIMITED_NATURAL)

@given(instance=alf_INTEGER_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_integer_literal_instantiation(instance):
    assert isinstance(instance, alf_INTEGER_LITERAL)

@given(instance=PRIMITIVE_LITERAL_strategy)
@settings(max_examples=50)
def test_primitive_literal_instantiation(instance):
    assert isinstance(instance, PRIMITIVE_LITERAL)

@given(instance=alf_STRING_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_string_literal_instantiation(instance):
    assert isinstance(instance, alf_STRING_LITERAL)

@given(instance=alf_NUMBER_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_number_literal_instantiation(instance):
    assert isinstance(instance, alf_NUMBER_LITERAL)

@given(instance=alf_BOOLEAN_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_boolean_literal_instantiation(instance):
    assert isinstance(instance, alf_BOOLEAN_LITERAL)

@given(instance=alf_NamespaceDefinition_strategy)
@settings(max_examples=50)
def test_alf_namespacedefinition_instantiation(instance):
    assert isinstance(instance, alf_NamespaceDefinition)

@given(instance=alf_StereotypeAnnotations_strategy)
@settings(max_examples=50)
def test_alf_stereotypeannotations_instantiation(instance):
    assert isinstance(instance, alf_StereotypeAnnotations)

@given(instance=alf_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_alf_importdeclaration_instantiation(instance):
    assert isinstance(instance, alf_ImportDeclaration)



@given(instance=alf_ImportDeclaration_strategy)
def test_alf_importdeclaration_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=alf_NamespaceDeclaration_strategy)
@settings(max_examples=50)
def test_alf_namespacedeclaration_instantiation(instance):
    assert isinstance(instance, alf_NamespaceDeclaration)

@given(instance=alf_UnitDefinition_strategy)
@settings(max_examples=50)
def test_alf_unitdefinition_instantiation(instance):
    assert isinstance(instance, alf_UnitDefinition)



@given(instance=alf_UnitDefinition_strategy)
def test_alf_unitdefinition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf_ImportReference_strategy)
@settings(max_examples=50)
def test_alf_importreference_instantiation(instance):
    assert isinstance(instance, alf_ImportReference)



@given(instance=alf_ImportReference_strategy)
def test_alf_importreference_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original
