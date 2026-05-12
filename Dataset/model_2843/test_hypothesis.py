import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    alf_VariableDeclarationCompletion,
    alf_ReclassifyAllClause,
    alf_ClassificationToClause,
    alf_ClassificationFromClause,
    alf_ClassificationClause,
    alf_QualifiedNameList,
    alf_AcceptBlock,
    alf_CompoundAcceptStatementCompletion,
    alf_SimpleAcceptStatementCompletion,
    alf_AcceptClause,
    alf_LoopVariableDefinition,
    alf_ForControl,
    alf_NonEmptyStatementSequence,
    alf_SwitchCase,
    alf_SwitchDefaultClause,
    alf_SwitchClause,
    alf_NonFinalClause,
    alf_ConcurrentClauses,
    alf_FinalClause,
    alf_SequentialClauses,
    alf_Annotation,
    Statement,
    alf_ThisInvocationStatement,
    alf_EmptyStatement,
    alf_BreakStatement,
    alf_ForStatement,
    alf_BlockStatement,
    alf_AcceptStatement,
    alf_AnnotatedStatement,
    alf_SwitchStatement,
    alf_InvocationOrAssignementOrDeclarationStatement,
    alf_ReturnStatement,
    alf_SuperInvocationStatement,
    alf_ClassifyStatement,
    alf_WhileStatement,
    alf_DoStatement,
    alf_IfStatement,
    alf_InstanceCreationInvocationStatement,
    alf_InlineStatement,
    alf_DocumentedStatement,
    alf_StatementSequence,
    alf_SequenceElement,
    alf_LocalNameDeclarationStatement,
    alf_PartialSequenceConstructionCompletion,
    alf_AccessCompletion,
    alf_InstanceCreationTupleElement,
    alf_InstanceCreationTuple,
    alf_NonLiteralValueSpecification,
    SequenceExpansionExpression,
    alf_IsUniqueOperation,
    alf_ForAllOrExistsOrOneOperation,
    alf_CollectOrIterateOperation,
    alf_SelectOrRejectOperation,
    alf_LinkOperationTupleElement,
    alf_LinkOperationTuple,
    SuffixExpression,
    alf_LinkOperationExpression,
    alf_ClassExtentExpression,
    alf_SequenceExpansionExpression,
    alf_SequenceOperationExpression,
    alf_SequenceReductionExpression,
    alf_PropertyCallExpression,
    alf_OperationCallExpression,
    alf_ValueSpecification,
    alf_PrimaryExpression,
    alf_UnaryExpression,
    alf_MultiplicativeExpression,
    alf_AdditiveExpression,
    alf_ShiftExpression,
    alf_ClassificationExpression,
    alf_EqualityExpression,
    alf_AndExpression,
    alf_ExclusiveOrExpression,
    alf_InclusiveOrExpression,
    alf_ConditionalAndExpression,
    alf_ConditionalOrExpression,
    Expression,
    alf_ConditionalTestExpression,
    SequenceElement,
    alf_SequenceConstructionExpression,
    alf_TupleElement,
    alf_QualifiedNameWithBinding,
    alf_NamedTemplateBinding,
    alf_RelationalExpression,
    alf_TemplateBinding,
    alf_UnqualifiedName,
    alf_SuffixExpression,
    alf_SequenceConstructionOrAccessCompletion,
    alf_Tuple,
    alf_QualifiedNamePath,
    NonLiteralValueSpecification,
    NUMBER_LITERAL,
    alf_UNLIMITED_LITERAL,
    alf_INTEGER_LITERAL,
    ValueSpecification,
    alf_NameExpression,
    alf_ThisExpression,
    alf_NullExpression,
    alf_SuperInvocationExpression,
    alf_ParenthesizedExpression,
    alf_InstanceCreationExpression,
    alf_LITERAL,
    alf_Block,
    alf_Statement,
    alf_AssignmentCompletion,
    alf_Expression,
    alf_Test,
    LITERAL,
    alf_NUMBER_LITERAL,
    alf_STRING_LITERAL,
    alf_BOOLEAN_LITERAL,
    LinkOperationKind,
    CollectOrIterateOperator,
    BooleanValue,
    ForAllOrExistsOrOneOperator,
    AssignmentOperator,
    SelectOrRejectOperator,
    AnnotationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_alf_variabledeclarationcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_VariableDeclarationCompletion)


def test_alf_variabledeclarationcompletion_constructor_exists():
    assert callable(alf_VariableDeclarationCompletion.__init__)


def test_alf_variabledeclarationcompletion_constructor_args():
    sig = inspect.signature(alf_VariableDeclarationCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"

def test_alf_variabledeclarationcompletion_has_variableName():
    assert hasattr(alf_VariableDeclarationCompletion, "variableName")
    descriptor = None
    for klass in alf_VariableDeclarationCompletion.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_alf_variabledeclarationcompletion_has_multiplicityIndicator():
    assert hasattr(alf_VariableDeclarationCompletion, "multiplicityIndicator")
    descriptor = None
    for klass in alf_VariableDeclarationCompletion.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)



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



def test_alf_qualifiednamelist_is_not_abstract():
    assert not inspect.isabstract(alf_QualifiedNameList)


def test_alf_qualifiednamelist_constructor_exists():
    assert callable(alf_QualifiedNameList.__init__)


def test_alf_qualifiednamelist_constructor_args():
    sig = inspect.signature(alf_QualifiedNameList.__init__)
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



def test_alf_acceptclause_is_not_abstract():
    assert not inspect.isabstract(alf_AcceptClause)


def test_alf_acceptclause_constructor_exists():
    assert callable(alf_AcceptClause.__init__)


def test_alf_acceptclause_constructor_args():
    sig = inspect.signature(alf_AcceptClause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf_acceptclause_has_name():
    assert hasattr(alf_AcceptClause, "name")
    descriptor = None
    for klass in alf_AcceptClause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf_loopvariabledefinition_is_not_abstract():
    assert not inspect.isabstract(alf_LoopVariableDefinition)


def test_alf_loopvariabledefinition_constructor_exists():
    assert callable(alf_LoopVariableDefinition.__init__)


def test_alf_loopvariabledefinition_constructor_args():
    sig = inspect.signature(alf_LoopVariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf_loopvariabledefinition_has_name():
    assert hasattr(alf_LoopVariableDefinition, "name")
    descriptor = None
    for klass in alf_LoopVariableDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf_forcontrol_is_not_abstract():
    assert not inspect.isabstract(alf_ForControl)


def test_alf_forcontrol_constructor_exists():
    assert callable(alf_ForControl.__init__)


def test_alf_forcontrol_constructor_args():
    sig = inspect.signature(alf_ForControl.__init__)
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



def test_alf_annotation_is_not_abstract():
    assert not inspect.isabstract(alf_Annotation)


def test_alf_annotation_constructor_exists():
    assert callable(alf_Annotation.__init__)


def test_alf_annotation_constructor_args():
    sig = inspect.signature(alf_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_alf_annotation_has_args():
    assert hasattr(alf_Annotation, "args")
    descriptor = None
    for klass in alf_Annotation.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)

def test_alf_annotation_has_kind():
    assert hasattr(alf_Annotation, "kind")
    descriptor = None
    for klass in alf_Annotation.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf_thisinvocationstatement_is_not_abstract():
    assert not inspect.isabstract(alf_ThisInvocationStatement)


def test_alf_thisinvocationstatement_constructor_exists():
    assert callable(alf_ThisInvocationStatement.__init__)


def test_alf_thisinvocationstatement_constructor_args():
    sig = inspect.signature(alf_ThisInvocationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_emptystatement_is_not_abstract():
    assert not inspect.isabstract(alf_EmptyStatement)


def test_alf_emptystatement_constructor_exists():
    assert callable(alf_EmptyStatement.__init__)


def test_alf_emptystatement_constructor_args():
    sig = inspect.signature(alf_EmptyStatement.__init__)
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



def test_alf_blockstatement_is_not_abstract():
    assert not inspect.isabstract(alf_BlockStatement)


def test_alf_blockstatement_constructor_exists():
    assert callable(alf_BlockStatement.__init__)


def test_alf_blockstatement_constructor_args():
    sig = inspect.signature(alf_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_acceptstatement_is_not_abstract():
    assert not inspect.isabstract(alf_AcceptStatement)


def test_alf_acceptstatement_constructor_exists():
    assert callable(alf_AcceptStatement.__init__)


def test_alf_acceptstatement_constructor_args():
    sig = inspect.signature(alf_AcceptStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_annotatedstatement_is_not_abstract():
    assert not inspect.isabstract(alf_AnnotatedStatement)


def test_alf_annotatedstatement_constructor_exists():
    assert callable(alf_AnnotatedStatement.__init__)


def test_alf_annotatedstatement_constructor_args():
    sig = inspect.signature(alf_AnnotatedStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_switchstatement_is_not_abstract():
    assert not inspect.isabstract(alf_SwitchStatement)


def test_alf_switchstatement_constructor_exists():
    assert callable(alf_SwitchStatement.__init__)


def test_alf_switchstatement_constructor_args():
    sig = inspect.signature(alf_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_invocationorassignementordeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(alf_InvocationOrAssignementOrDeclarationStatement)


def test_alf_invocationorassignementordeclarationstatement_constructor_exists():
    assert callable(alf_InvocationOrAssignementOrDeclarationStatement.__init__)


def test_alf_invocationorassignementordeclarationstatement_constructor_args():
    sig = inspect.signature(alf_InvocationOrAssignementOrDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_returnstatement_is_not_abstract():
    assert not inspect.isabstract(alf_ReturnStatement)


def test_alf_returnstatement_constructor_exists():
    assert callable(alf_ReturnStatement.__init__)


def test_alf_returnstatement_constructor_args():
    sig = inspect.signature(alf_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_superinvocationstatement_is_not_abstract():
    assert not inspect.isabstract(alf_SuperInvocationStatement)


def test_alf_superinvocationstatement_constructor_exists():
    assert callable(alf_SuperInvocationStatement.__init__)


def test_alf_superinvocationstatement_constructor_args():
    sig = inspect.signature(alf_SuperInvocationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_classifystatement_is_not_abstract():
    assert not inspect.isabstract(alf_ClassifyStatement)


def test_alf_classifystatement_constructor_exists():
    assert callable(alf_ClassifyStatement.__init__)


def test_alf_classifystatement_constructor_args():
    sig = inspect.signature(alf_ClassifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_whilestatement_is_not_abstract():
    assert not inspect.isabstract(alf_WhileStatement)


def test_alf_whilestatement_constructor_exists():
    assert callable(alf_WhileStatement.__init__)


def test_alf_whilestatement_constructor_args():
    sig = inspect.signature(alf_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_dostatement_is_not_abstract():
    assert not inspect.isabstract(alf_DoStatement)


def test_alf_dostatement_constructor_exists():
    assert callable(alf_DoStatement.__init__)


def test_alf_dostatement_constructor_args():
    sig = inspect.signature(alf_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_ifstatement_is_not_abstract():
    assert not inspect.isabstract(alf_IfStatement)


def test_alf_ifstatement_constructor_exists():
    assert callable(alf_IfStatement.__init__)


def test_alf_ifstatement_constructor_args():
    sig = inspect.signature(alf_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_instancecreationinvocationstatement_is_not_abstract():
    assert not inspect.isabstract(alf_InstanceCreationInvocationStatement)


def test_alf_instancecreationinvocationstatement_constructor_exists():
    assert callable(alf_InstanceCreationInvocationStatement.__init__)


def test_alf_instancecreationinvocationstatement_constructor_args():
    sig = inspect.signature(alf_InstanceCreationInvocationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf_inlinestatement_is_not_abstract():
    assert not inspect.isabstract(alf_InlineStatement)


def test_alf_inlinestatement_constructor_exists():
    assert callable(alf_InlineStatement.__init__)


def test_alf_inlinestatement_constructor_args():
    sig = inspect.signature(alf_InlineStatement.__init__)
    params = list(sig.parameters.keys())
    assert "langageName" in params, "Missing parameter 'langageName'"
    assert "body" in params, "Missing parameter 'body'"

def test_alf_inlinestatement_has_langageName():
    assert hasattr(alf_InlineStatement, "langageName")
    descriptor = None
    for klass in alf_InlineStatement.__mro__:
        if "langageName" in klass.__dict__:
            descriptor = klass.__dict__["langageName"]
            break
    assert isinstance(descriptor, property)

def test_alf_inlinestatement_has_body():
    assert hasattr(alf_InlineStatement, "body")
    descriptor = None
    for klass in alf_InlineStatement.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



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



def test_alf_sequenceelement_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceElement)


def test_alf_sequenceelement_constructor_exists():
    assert callable(alf_SequenceElement.__init__)


def test_alf_sequenceelement_constructor_args():
    sig = inspect.signature(alf_SequenceElement.__init__)
    params = list(sig.parameters.keys())



def test_alf_localnamedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(alf_LocalNameDeclarationStatement)


def test_alf_localnamedeclarationstatement_constructor_exists():
    assert callable(alf_LocalNameDeclarationStatement.__init__)


def test_alf_localnamedeclarationstatement_constructor_args():
    sig = inspect.signature(alf_LocalNameDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_alf_localnamedeclarationstatement_has_multiplicityIndicator():
    assert hasattr(alf_LocalNameDeclarationStatement, "multiplicityIndicator")
    descriptor = None
    for klass in alf_LocalNameDeclarationStatement.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)

def test_alf_localnamedeclarationstatement_has_varName():
    assert hasattr(alf_LocalNameDeclarationStatement, "varName")
    descriptor = None
    for klass in alf_LocalNameDeclarationStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_alf_partialsequenceconstructioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf_PartialSequenceConstructionCompletion)


def test_alf_partialsequenceconstructioncompletion_constructor_exists():
    assert callable(alf_PartialSequenceConstructionCompletion.__init__)


def test_alf_partialsequenceconstructioncompletion_constructor_args():
    sig = inspect.signature(alf_PartialSequenceConstructionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_accesscompletion_is_not_abstract():
    assert not inspect.isabstract(alf_AccessCompletion)


def test_alf_accesscompletion_constructor_exists():
    assert callable(alf_AccessCompletion.__init__)


def test_alf_accesscompletion_constructor_args():
    sig = inspect.signature(alf_AccessCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf_instancecreationtupleelement_is_not_abstract():
    assert not inspect.isabstract(alf_InstanceCreationTupleElement)


def test_alf_instancecreationtupleelement_constructor_exists():
    assert callable(alf_InstanceCreationTupleElement.__init__)


def test_alf_instancecreationtupleelement_constructor_args():
    sig = inspect.signature(alf_InstanceCreationTupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"

def test_alf_instancecreationtupleelement_has_role():
    assert hasattr(alf_InstanceCreationTupleElement, "role")
    descriptor = None
    for klass in alf_InstanceCreationTupleElement.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_alf_instancecreationtuple_is_not_abstract():
    assert not inspect.isabstract(alf_InstanceCreationTuple)


def test_alf_instancecreationtuple_constructor_exists():
    assert callable(alf_InstanceCreationTuple.__init__)


def test_alf_instancecreationtuple_constructor_args():
    sig = inspect.signature(alf_InstanceCreationTuple.__init__)
    params = list(sig.parameters.keys())



def test_alf_nonliteralvaluespecification_is_not_abstract():
    assert not inspect.isabstract(alf_NonLiteralValueSpecification)


def test_alf_nonliteralvaluespecification_constructor_exists():
    assert callable(alf_NonLiteralValueSpecification.__init__)


def test_alf_nonliteralvaluespecification_constructor_args():
    sig = inspect.signature(alf_NonLiteralValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_sequenceexpansionexpression_is_not_abstract():
    assert not inspect.isabstract(SequenceExpansionExpression)


def test_sequenceexpansionexpression_constructor_exists():
    assert callable(SequenceExpansionExpression.__init__)


def test_sequenceexpansionexpression_constructor_args():
    sig = inspect.signature(SequenceExpansionExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_isuniqueoperation_is_not_abstract():
    assert not inspect.isabstract(alf_IsUniqueOperation)


def test_alf_isuniqueoperation_constructor_exists():
    assert callable(alf_IsUniqueOperation.__init__)


def test_alf_isuniqueoperation_constructor_args():
    sig = inspect.signature(alf_IsUniqueOperation.__init__)
    params = list(sig.parameters.keys())



def test_alf_forallorexistsoroneoperation_is_not_abstract():
    assert not inspect.isabstract(alf_ForAllOrExistsOrOneOperation)


def test_alf_forallorexistsoroneoperation_constructor_exists():
    assert callable(alf_ForAllOrExistsOrOneOperation.__init__)


def test_alf_forallorexistsoroneoperation_constructor_args():
    sig = inspect.signature(alf_ForAllOrExistsOrOneOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_forallorexistsoroneoperation_has_op():
    assert hasattr(alf_ForAllOrExistsOrOneOperation, "op")
    descriptor = None
    for klass in alf_ForAllOrExistsOrOneOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_collectoriterateoperation_is_not_abstract():
    assert not inspect.isabstract(alf_CollectOrIterateOperation)


def test_alf_collectoriterateoperation_constructor_exists():
    assert callable(alf_CollectOrIterateOperation.__init__)


def test_alf_collectoriterateoperation_constructor_args():
    sig = inspect.signature(alf_CollectOrIterateOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_collectoriterateoperation_has_op():
    assert hasattr(alf_CollectOrIterateOperation, "op")
    descriptor = None
    for klass in alf_CollectOrIterateOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_selectorrejectoperation_is_not_abstract():
    assert not inspect.isabstract(alf_SelectOrRejectOperation)


def test_alf_selectorrejectoperation_constructor_exists():
    assert callable(alf_SelectOrRejectOperation.__init__)


def test_alf_selectorrejectoperation_constructor_args():
    sig = inspect.signature(alf_SelectOrRejectOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_selectorrejectoperation_has_op():
    assert hasattr(alf_SelectOrRejectOperation, "op")
    descriptor = None
    for klass in alf_SelectOrRejectOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_linkoperationtupleelement_is_not_abstract():
    assert not inspect.isabstract(alf_LinkOperationTupleElement)


def test_alf_linkoperationtupleelement_constructor_exists():
    assert callable(alf_LinkOperationTupleElement.__init__)


def test_alf_linkoperationtupleelement_constructor_args():
    sig = inspect.signature(alf_LinkOperationTupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"

def test_alf_linkoperationtupleelement_has_role():
    assert hasattr(alf_LinkOperationTupleElement, "role")
    descriptor = None
    for klass in alf_LinkOperationTupleElement.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_alf_linkoperationtuple_is_not_abstract():
    assert not inspect.isabstract(alf_LinkOperationTuple)


def test_alf_linkoperationtuple_constructor_exists():
    assert callable(alf_LinkOperationTuple.__init__)


def test_alf_linkoperationtuple_constructor_args():
    sig = inspect.signature(alf_LinkOperationTuple.__init__)
    params = list(sig.parameters.keys())



def test_suffixexpression_is_not_abstract():
    assert not inspect.isabstract(SuffixExpression)


def test_suffixexpression_constructor_exists():
    assert callable(SuffixExpression.__init__)


def test_suffixexpression_constructor_args():
    sig = inspect.signature(SuffixExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_linkoperationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_LinkOperationExpression)


def test_alf_linkoperationexpression_constructor_exists():
    assert callable(alf_LinkOperationExpression.__init__)


def test_alf_linkoperationexpression_constructor_args():
    sig = inspect.signature(alf_LinkOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_alf_linkoperationexpression_has_kind():
    assert hasattr(alf_LinkOperationExpression, "kind")
    descriptor = None
    for klass in alf_LinkOperationExpression.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_alf_classextentexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ClassExtentExpression)


def test_alf_classextentexpression_constructor_exists():
    assert callable(alf_ClassExtentExpression.__init__)


def test_alf_classextentexpression_constructor_args():
    sig = inspect.signature(alf_ClassExtentExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceexpansionexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceExpansionExpression)


def test_alf_sequenceexpansionexpression_constructor_exists():
    assert callable(alf_SequenceExpansionExpression.__init__)


def test_alf_sequenceexpansionexpression_constructor_args():
    sig = inspect.signature(alf_SequenceExpansionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf_sequenceexpansionexpression_has_name():
    assert hasattr(alf_SequenceExpansionExpression, "name")
    descriptor = None
    for klass in alf_SequenceExpansionExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf_sequenceoperationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceOperationExpression)


def test_alf_sequenceoperationexpression_constructor_exists():
    assert callable(alf_SequenceOperationExpression.__init__)


def test_alf_sequenceoperationexpression_constructor_args():
    sig = inspect.signature(alf_SequenceOperationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequencereductionexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceReductionExpression)


def test_alf_sequencereductionexpression_constructor_exists():
    assert callable(alf_SequenceReductionExpression.__init__)


def test_alf_sequencereductionexpression_constructor_args():
    sig = inspect.signature(alf_SequenceReductionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_alf_sequencereductionexpression_has_isOrdered():
    assert hasattr(alf_SequenceReductionExpression, "isOrdered")
    descriptor = None
    for klass in alf_SequenceReductionExpression.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_alf_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(alf_PropertyCallExpression)


def test_alf_propertycallexpression_constructor_exists():
    assert callable(alf_PropertyCallExpression.__init__)


def test_alf_propertycallexpression_constructor_args():
    sig = inspect.signature(alf_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_alf_propertycallexpression_has_propertyName():
    assert hasattr(alf_PropertyCallExpression, "propertyName")
    descriptor = None
    for klass in alf_PropertyCallExpression.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_alf_operationcallexpression_is_not_abstract():
    assert not inspect.isabstract(alf_OperationCallExpression)


def test_alf_operationcallexpression_constructor_exists():
    assert callable(alf_OperationCallExpression.__init__)


def test_alf_operationcallexpression_constructor_args():
    sig = inspect.signature(alf_OperationCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_alf_operationcallexpression_has_operationName():
    assert hasattr(alf_OperationCallExpression, "operationName")
    descriptor = None
    for klass in alf_OperationCallExpression.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_alf_valuespecification_is_not_abstract():
    assert not inspect.isabstract(alf_ValueSpecification)


def test_alf_valuespecification_constructor_exists():
    assert callable(alf_ValueSpecification.__init__)


def test_alf_valuespecification_constructor_args():
    sig = inspect.signature(alf_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_alf_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_PrimaryExpression)


def test_alf_primaryexpression_constructor_exists():
    assert callable(alf_PrimaryExpression.__init__)


def test_alf_primaryexpression_constructor_args():
    sig = inspect.signature(alf_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf_UnaryExpression)


def test_alf_unaryexpression_constructor_exists():
    assert callable(alf_UnaryExpression.__init__)


def test_alf_unaryexpression_constructor_args():
    sig = inspect.signature(alf_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_unaryexpression_has_op():
    assert hasattr(alf_UnaryExpression, "op")
    descriptor = None
    for klass in alf_UnaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(alf_MultiplicativeExpression)


def test_alf_multiplicativeexpression_constructor_exists():
    assert callable(alf_MultiplicativeExpression.__init__)


def test_alf_multiplicativeexpression_constructor_args():
    sig = inspect.signature(alf_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_multiplicativeexpression_has_op():
    assert hasattr(alf_MultiplicativeExpression, "op")
    descriptor = None
    for klass in alf_MultiplicativeExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(alf_AdditiveExpression)


def test_alf_additiveexpression_constructor_exists():
    assert callable(alf_AdditiveExpression.__init__)


def test_alf_additiveexpression_constructor_args():
    sig = inspect.signature(alf_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_additiveexpression_has_op():
    assert hasattr(alf_AdditiveExpression, "op")
    descriptor = None
    for klass in alf_AdditiveExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ShiftExpression)


def test_alf_shiftexpression_constructor_exists():
    assert callable(alf_ShiftExpression.__init__)


def test_alf_shiftexpression_constructor_args():
    sig = inspect.signature(alf_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_shiftexpression_has_op():
    assert hasattr(alf_ShiftExpression, "op")
    descriptor = None
    for klass in alf_ShiftExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_classificationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ClassificationExpression)


def test_alf_classificationexpression_constructor_exists():
    assert callable(alf_ClassificationExpression.__init__)


def test_alf_classificationexpression_constructor_args():
    sig = inspect.signature(alf_ClassificationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_classificationexpression_has_op():
    assert hasattr(alf_ClassificationExpression, "op")
    descriptor = None
    for klass in alf_ClassificationExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(alf_EqualityExpression)


def test_alf_equalityexpression_constructor_exists():
    assert callable(alf_EqualityExpression.__init__)


def test_alf_equalityexpression_constructor_args():
    sig = inspect.signature(alf_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_equalityexpression_has_op():
    assert hasattr(alf_EqualityExpression, "op")
    descriptor = None
    for klass in alf_EqualityExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_andexpression_is_not_abstract():
    assert not inspect.isabstract(alf_AndExpression)


def test_alf_andexpression_constructor_exists():
    assert callable(alf_AndExpression.__init__)


def test_alf_andexpression_constructor_args():
    sig = inspect.signature(alf_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ExclusiveOrExpression)


def test_alf_exclusiveorexpression_constructor_exists():
    assert callable(alf_ExclusiveOrExpression.__init__)


def test_alf_exclusiveorexpression_constructor_args():
    sig = inspect.signature(alf_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf_InclusiveOrExpression)


def test_alf_inclusiveorexpression_constructor_exists():
    assert callable(alf_InclusiveOrExpression.__init__)


def test_alf_inclusiveorexpression_constructor_args():
    sig = inspect.signature(alf_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalAndExpression)


def test_alf_conditionalandexpression_constructor_exists():
    assert callable(alf_ConditionalAndExpression.__init__)


def test_alf_conditionalandexpression_constructor_args():
    sig = inspect.signature(alf_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalOrExpression)


def test_alf_conditionalorexpression_constructor_exists():
    assert callable(alf_ConditionalOrExpression.__init__)


def test_alf_conditionalorexpression_constructor_args():
    sig = inspect.signature(alf_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_alf_conditionaltestexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ConditionalTestExpression)


def test_alf_conditionaltestexpression_constructor_exists():
    assert callable(alf_ConditionalTestExpression.__init__)


def test_alf_conditionaltestexpression_constructor_args():
    sig = inspect.signature(alf_ConditionalTestExpression.__init__)
    params = list(sig.parameters.keys())



def test_sequenceelement_is_not_abstract():
    assert not inspect.isabstract(SequenceElement)


def test_sequenceelement_constructor_exists():
    assert callable(SequenceElement.__init__)


def test_sequenceelement_constructor_args():
    sig = inspect.signature(SequenceElement.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceconstructionexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceConstructionExpression)


def test_alf_sequenceconstructionexpression_constructor_exists():
    assert callable(alf_SequenceConstructionExpression.__init__)


def test_alf_sequenceconstructionexpression_constructor_args():
    sig = inspect.signature(alf_SequenceConstructionExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_tupleelement_is_not_abstract():
    assert not inspect.isabstract(alf_TupleElement)


def test_alf_tupleelement_constructor_exists():
    assert callable(alf_TupleElement.__init__)


def test_alf_tupleelement_constructor_args():
    sig = inspect.signature(alf_TupleElement.__init__)
    params = list(sig.parameters.keys())



def test_alf_qualifiednamewithbinding_is_not_abstract():
    assert not inspect.isabstract(alf_QualifiedNameWithBinding)


def test_alf_qualifiednamewithbinding_constructor_exists():
    assert callable(alf_QualifiedNameWithBinding.__init__)


def test_alf_qualifiednamewithbinding_constructor_args():
    sig = inspect.signature(alf_QualifiedNameWithBinding.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf_qualifiednamewithbinding_has_id():
    assert hasattr(alf_QualifiedNameWithBinding, "id")
    descriptor = None
    for klass in alf_QualifiedNameWithBinding.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf_namedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(alf_NamedTemplateBinding)


def test_alf_namedtemplatebinding_constructor_exists():
    assert callable(alf_NamedTemplateBinding.__init__)


def test_alf_namedtemplatebinding_constructor_args():
    sig = inspect.signature(alf_NamedTemplateBinding.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"

def test_alf_namedtemplatebinding_has_formal():
    assert hasattr(alf_NamedTemplateBinding, "formal")
    descriptor = None
    for klass in alf_NamedTemplateBinding.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_alf_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(alf_RelationalExpression)


def test_alf_relationalexpression_constructor_exists():
    assert callable(alf_RelationalExpression.__init__)


def test_alf_relationalexpression_constructor_args():
    sig = inspect.signature(alf_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_relationalexpression_has_op():
    assert hasattr(alf_RelationalExpression, "op")
    descriptor = None
    for klass in alf_RelationalExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_templatebinding_is_not_abstract():
    assert not inspect.isabstract(alf_TemplateBinding)


def test_alf_templatebinding_constructor_exists():
    assert callable(alf_TemplateBinding.__init__)


def test_alf_templatebinding_constructor_args():
    sig = inspect.signature(alf_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf_unqualifiedname_is_not_abstract():
    assert not inspect.isabstract(alf_UnqualifiedName)


def test_alf_unqualifiedname_constructor_exists():
    assert callable(alf_UnqualifiedName.__init__)


def test_alf_unqualifiedname_constructor_args():
    sig = inspect.signature(alf_UnqualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf_unqualifiedname_has_name():
    assert hasattr(alf_UnqualifiedName, "name")
    descriptor = None
    for klass in alf_UnqualifiedName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf_suffixexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SuffixExpression)


def test_alf_suffixexpression_constructor_exists():
    assert callable(alf_SuffixExpression.__init__)


def test_alf_suffixexpression_constructor_args():
    sig = inspect.signature(alf_SuffixExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_sequenceconstructionoraccesscompletion_is_not_abstract():
    assert not inspect.isabstract(alf_SequenceConstructionOrAccessCompletion)


def test_alf_sequenceconstructionoraccesscompletion_constructor_exists():
    assert callable(alf_SequenceConstructionOrAccessCompletion.__init__)


def test_alf_sequenceconstructionoraccesscompletion_constructor_args():
    sig = inspect.signature(alf_SequenceConstructionOrAccessCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"

def test_alf_sequenceconstructionoraccesscompletion_has_multiplicityIndicator():
    assert hasattr(alf_SequenceConstructionOrAccessCompletion, "multiplicityIndicator")
    descriptor = None
    for klass in alf_SequenceConstructionOrAccessCompletion.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)



def test_alf_tuple_is_not_abstract():
    assert not inspect.isabstract(alf_Tuple)


def test_alf_tuple_constructor_exists():
    assert callable(alf_Tuple.__init__)


def test_alf_tuple_constructor_args():
    sig = inspect.signature(alf_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_alf_qualifiednamepath_is_not_abstract():
    assert not inspect.isabstract(alf_QualifiedNamePath)


def test_alf_qualifiednamepath_constructor_exists():
    assert callable(alf_QualifiedNamePath.__init__)


def test_alf_qualifiednamepath_constructor_args():
    sig = inspect.signature(alf_QualifiedNamePath.__init__)
    params = list(sig.parameters.keys())



def test_nonliteralvaluespecification_is_not_abstract():
    assert not inspect.isabstract(NonLiteralValueSpecification)


def test_nonliteralvaluespecification_constructor_exists():
    assert callable(NonLiteralValueSpecification.__init__)


def test_nonliteralvaluespecification_constructor_args():
    sig = inspect.signature(NonLiteralValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_number_literal_is_not_abstract():
    assert not inspect.isabstract(NUMBER_LITERAL)


def test_number_literal_constructor_exists():
    assert callable(NUMBER_LITERAL.__init__)


def test_number_literal_constructor_args():
    sig = inspect.signature(NUMBER_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_unlimited_literal_is_not_abstract():
    assert not inspect.isabstract(alf_UNLIMITED_LITERAL)


def test_alf_unlimited_literal_constructor_exists():
    assert callable(alf_UNLIMITED_LITERAL.__init__)


def test_alf_unlimited_literal_constructor_args():
    sig = inspect.signature(alf_UNLIMITED_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_integer_literal_is_not_abstract():
    assert not inspect.isabstract(alf_INTEGER_LITERAL)


def test_alf_integer_literal_constructor_exists():
    assert callable(alf_INTEGER_LITERAL.__init__)


def test_alf_integer_literal_constructor_args():
    sig = inspect.signature(alf_INTEGER_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_alf_nameexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NameExpression)


def test_alf_nameexpression_constructor_exists():
    assert callable(alf_NameExpression.__init__)


def test_alf_nameexpression_constructor_args():
    sig = inspect.signature(alf_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "postfixOp" in params, "Missing parameter 'postfixOp'"
    assert "prefixOp" in params, "Missing parameter 'prefixOp'"
    assert "id" in params, "Missing parameter 'id'"

def test_alf_nameexpression_has_postfixOp():
    assert hasattr(alf_NameExpression, "postfixOp")
    descriptor = None
    for klass in alf_NameExpression.__mro__:
        if "postfixOp" in klass.__dict__:
            descriptor = klass.__dict__["postfixOp"]
            break
    assert isinstance(descriptor, property)

def test_alf_nameexpression_has_prefixOp():
    assert hasattr(alf_NameExpression, "prefixOp")
    descriptor = None
    for klass in alf_NameExpression.__mro__:
        if "prefixOp" in klass.__dict__:
            descriptor = klass.__dict__["prefixOp"]
            break
    assert isinstance(descriptor, property)

def test_alf_nameexpression_has_id():
    assert hasattr(alf_NameExpression, "id")
    descriptor = None
    for klass in alf_NameExpression.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf_thisexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ThisExpression)


def test_alf_thisexpression_constructor_exists():
    assert callable(alf_ThisExpression.__init__)


def test_alf_thisexpression_constructor_args():
    sig = inspect.signature(alf_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_nullexpression_is_not_abstract():
    assert not inspect.isabstract(alf_NullExpression)


def test_alf_nullexpression_constructor_exists():
    assert callable(alf_NullExpression.__init__)


def test_alf_nullexpression_constructor_args():
    sig = inspect.signature(alf_NullExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_superinvocationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_SuperInvocationExpression)


def test_alf_superinvocationexpression_constructor_exists():
    assert callable(alf_SuperInvocationExpression.__init__)


def test_alf_superinvocationexpression_constructor_args():
    sig = inspect.signature(alf_SuperInvocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(alf_ParenthesizedExpression)


def test_alf_parenthesizedexpression_constructor_exists():
    assert callable(alf_ParenthesizedExpression.__init__)


def test_alf_parenthesizedexpression_constructor_args():
    sig = inspect.signature(alf_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_instancecreationexpression_is_not_abstract():
    assert not inspect.isabstract(alf_InstanceCreationExpression)


def test_alf_instancecreationexpression_constructor_exists():
    assert callable(alf_InstanceCreationExpression.__init__)


def test_alf_instancecreationexpression_constructor_args():
    sig = inspect.signature(alf_InstanceCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf_literal_is_not_abstract():
    assert not inspect.isabstract(alf_LITERAL)


def test_alf_literal_constructor_exists():
    assert callable(alf_LITERAL.__init__)


def test_alf_literal_constructor_args():
    sig = inspect.signature(alf_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_block_is_not_abstract():
    assert not inspect.isabstract(alf_Block)


def test_alf_block_constructor_exists():
    assert callable(alf_Block.__init__)


def test_alf_block_constructor_args():
    sig = inspect.signature(alf_Block.__init__)
    params = list(sig.parameters.keys())



def test_alf_statement_is_not_abstract():
    assert not inspect.isabstract(alf_Statement)


def test_alf_statement_constructor_exists():
    assert callable(alf_Statement.__init__)


def test_alf_statement_constructor_args():
    sig = inspect.signature(alf_Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf_assignmentcompletion_is_not_abstract():
    assert not inspect.isabstract(alf_AssignmentCompletion)


def test_alf_assignmentcompletion_constructor_exists():
    assert callable(alf_AssignmentCompletion.__init__)


def test_alf_assignmentcompletion_constructor_args():
    sig = inspect.signature(alf_AssignmentCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf_assignmentcompletion_has_op():
    assert hasattr(alf_AssignmentCompletion, "op")
    descriptor = None
    for klass in alf_AssignmentCompletion.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf_expression_is_not_abstract():
    assert not inspect.isabstract(alf_Expression)


def test_alf_expression_constructor_exists():
    assert callable(alf_Expression.__init__)


def test_alf_expression_constructor_args():
    sig = inspect.signature(alf_Expression.__init__)
    params = list(sig.parameters.keys())



def test_alf_test_is_not_abstract():
    assert not inspect.isabstract(alf_Test)


def test_alf_test_constructor_exists():
    assert callable(alf_Test.__init__)


def test_alf_test_constructor_args():
    sig = inspect.signature(alf_Test.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(LITERAL)


def test_literal_constructor_exists():
    assert callable(LITERAL.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf_number_literal_is_not_abstract():
    assert not inspect.isabstract(alf_NUMBER_LITERAL)


def test_alf_number_literal_constructor_exists():
    assert callable(alf_NUMBER_LITERAL.__init__)


def test_alf_number_literal_constructor_args():
    sig = inspect.signature(alf_NUMBER_LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf_number_literal_has_value():
    assert hasattr(alf_NUMBER_LITERAL, "value")
    descriptor = None
    for klass in alf_NUMBER_LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alf_string_literal_is_not_abstract():
    assert not inspect.isabstract(alf_STRING_LITERAL)


def test_alf_string_literal_constructor_exists():
    assert callable(alf_STRING_LITERAL.__init__)


def test_alf_string_literal_constructor_args():
    sig = inspect.signature(alf_STRING_LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf_string_literal_has_value():
    assert hasattr(alf_STRING_LITERAL, "value")
    descriptor = None
    for klass in alf_STRING_LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alf_boolean_literal_is_not_abstract():
    assert not inspect.isabstract(alf_BOOLEAN_LITERAL)


def test_alf_boolean_literal_constructor_exists():
    assert callable(alf_BOOLEAN_LITERAL.__init__)


def test_alf_boolean_literal_constructor_args():
    sig = inspect.signature(alf_BOOLEAN_LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf_boolean_literal_has_value():
    assert hasattr(alf_BOOLEAN_LITERAL, "value")
    descriptor = None
    for klass in alf_BOOLEAN_LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_linkoperationkind_exists():
    # Check that the Enumeration exists
    assert LinkOperationKind is not None

def test_linkoperationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkOperationKind]
    expected_literals = [
        "DESTROY",
        "CREATE",
        "CLEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkOperationKind"

def test_collectoriterateoperator_exists():
    # Check that the Enumeration exists
    assert CollectOrIterateOperator is not None

def test_collectoriterateoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectOrIterateOperator]
    expected_literals = [
        "COLLECT",
        "ITERATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectOrIterateOperator"

def test_booleanvalue_exists():
    # Check that the Enumeration exists
    assert BooleanValue is not None

def test_booleanvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanValue]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanValue"

def test_forallorexistsoroneoperator_exists():
    # Check that the Enumeration exists
    assert ForAllOrExistsOrOneOperator is not None

def test_forallorexistsoroneoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ForAllOrExistsOrOneOperator]
    expected_literals = [
        "FORALL",
        "EXISTS",
        "ONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ForAllOrExistsOrOneOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "MINUSASSIGN",
        "PLUSASSIGN",
        "URSHIFTASSIGN",
        "ANDASSIGN",
        "LSHIFTASSIGN",
        "ORASSIGN",
        "RSHIFTASSIGN",
        "XORASSIGN",
        "ASSIGN",
        "MODASSIGN",
        "DIVASSIGN",
        "MULTASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_selectorrejectoperator_exists():
    # Check that the Enumeration exists
    assert SelectOrRejectOperator is not None

def test_selectorrejectoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectOrRejectOperator]
    expected_literals = [
        "SELECT",
        "REJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectOrRejectOperator"

def test_annotationkind_exists():
    # Check that the Enumeration exists
    assert AnnotationKind is not None

def test_annotationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnnotationKind]
    expected_literals = [
        "PARALLEL",
        "ASSURED",
        "ISOLATED",
        "DETERMINED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnnotationKind"


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
alf_VariableDeclarationCompletion_strategy = st.builds(
    alf_VariableDeclarationCompletion,
    variableName=
        safe_text,
    multiplicityIndicator=
        st.booleans()
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
alf_QualifiedNameList_strategy = st.builds(
    alf_QualifiedNameList,
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
alf_AcceptClause_strategy = st.builds(
    alf_AcceptClause,
    name=
        safe_text
)
alf_LoopVariableDefinition_strategy = st.builds(
    alf_LoopVariableDefinition,
    name=
        safe_text
)
alf_ForControl_strategy = st.builds(
    alf_ForControl,
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
alf_Annotation_strategy = st.builds(
    alf_Annotation,
    args=
        safe_text,
    kind=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
alf_ThisInvocationStatement_strategy = st.builds(
    alf_ThisInvocationStatement,
)
alf_EmptyStatement_strategy = st.builds(
    alf_EmptyStatement,
)
alf_BreakStatement_strategy = st.builds(
    alf_BreakStatement,
)
alf_ForStatement_strategy = st.builds(
    alf_ForStatement,
)
alf_BlockStatement_strategy = st.builds(
    alf_BlockStatement,
)
alf_AcceptStatement_strategy = st.builds(
    alf_AcceptStatement,
)
alf_AnnotatedStatement_strategy = st.builds(
    alf_AnnotatedStatement,
)
alf_SwitchStatement_strategy = st.builds(
    alf_SwitchStatement,
)
alf_InvocationOrAssignementOrDeclarationStatement_strategy = st.builds(
    alf_InvocationOrAssignementOrDeclarationStatement,
)
alf_ReturnStatement_strategy = st.builds(
    alf_ReturnStatement,
)
alf_SuperInvocationStatement_strategy = st.builds(
    alf_SuperInvocationStatement,
)
alf_ClassifyStatement_strategy = st.builds(
    alf_ClassifyStatement,
)
alf_WhileStatement_strategy = st.builds(
    alf_WhileStatement,
)
alf_DoStatement_strategy = st.builds(
    alf_DoStatement,
)
alf_IfStatement_strategy = st.builds(
    alf_IfStatement,
)
alf_InstanceCreationInvocationStatement_strategy = st.builds(
    alf_InstanceCreationInvocationStatement,
)
alf_InlineStatement_strategy = st.builds(
    alf_InlineStatement,
    langageName=
        safe_text,
    body=
        safe_text
)
alf_DocumentedStatement_strategy = st.builds(
    alf_DocumentedStatement,
    comment=
        safe_text
)
alf_StatementSequence_strategy = st.builds(
    alf_StatementSequence,
)
alf_SequenceElement_strategy = st.builds(
    alf_SequenceElement,
)
alf_LocalNameDeclarationStatement_strategy = st.builds(
    alf_LocalNameDeclarationStatement,
    multiplicityIndicator=
        st.booleans(),
    varName=
        safe_text
)
alf_PartialSequenceConstructionCompletion_strategy = st.builds(
    alf_PartialSequenceConstructionCompletion,
)
alf_AccessCompletion_strategy = st.builds(
    alf_AccessCompletion,
)
alf_InstanceCreationTupleElement_strategy = st.builds(
    alf_InstanceCreationTupleElement,
    role=
        safe_text
)
alf_InstanceCreationTuple_strategy = st.builds(
    alf_InstanceCreationTuple,
)
alf_NonLiteralValueSpecification_strategy = st.builds(
    alf_NonLiteralValueSpecification,
)
SequenceExpansionExpression_strategy = st.builds(
    SequenceExpansionExpression,
)
alf_IsUniqueOperation_strategy = st.builds(
    alf_IsUniqueOperation,
)
alf_ForAllOrExistsOrOneOperation_strategy = st.builds(
    alf_ForAllOrExistsOrOneOperation,
    op=
        safe_text
)
alf_CollectOrIterateOperation_strategy = st.builds(
    alf_CollectOrIterateOperation,
    op=
        safe_text
)
alf_SelectOrRejectOperation_strategy = st.builds(
    alf_SelectOrRejectOperation,
    op=
        safe_text
)
alf_LinkOperationTupleElement_strategy = st.builds(
    alf_LinkOperationTupleElement,
    role=
        safe_text
)
alf_LinkOperationTuple_strategy = st.builds(
    alf_LinkOperationTuple,
)
SuffixExpression_strategy = st.builds(
    SuffixExpression,
)
alf_LinkOperationExpression_strategy = st.builds(
    alf_LinkOperationExpression,
    kind=
        safe_text
)
alf_ClassExtentExpression_strategy = st.builds(
    alf_ClassExtentExpression,
)
alf_SequenceExpansionExpression_strategy = st.builds(
    alf_SequenceExpansionExpression,
    name=
        safe_text
)
alf_SequenceOperationExpression_strategy = st.builds(
    alf_SequenceOperationExpression,
)
alf_SequenceReductionExpression_strategy = st.builds(
    alf_SequenceReductionExpression,
    isOrdered=
        st.booleans()
)
alf_PropertyCallExpression_strategy = st.builds(
    alf_PropertyCallExpression,
    propertyName=
        safe_text
)
alf_OperationCallExpression_strategy = st.builds(
    alf_OperationCallExpression,
    operationName=
        safe_text
)
alf_ValueSpecification_strategy = st.builds(
    alf_ValueSpecification,
)
alf_PrimaryExpression_strategy = st.builds(
    alf_PrimaryExpression,
)
alf_UnaryExpression_strategy = st.builds(
    alf_UnaryExpression,
    op=
        safe_text
)
alf_MultiplicativeExpression_strategy = st.builds(
    alf_MultiplicativeExpression,
    op=
        safe_text
)
alf_AdditiveExpression_strategy = st.builds(
    alf_AdditiveExpression,
    op=
        safe_text
)
alf_ShiftExpression_strategy = st.builds(
    alf_ShiftExpression,
    op=
        safe_text
)
alf_ClassificationExpression_strategy = st.builds(
    alf_ClassificationExpression,
    op=
        safe_text
)
alf_EqualityExpression_strategy = st.builds(
    alf_EqualityExpression,
    op=
        safe_text
)
alf_AndExpression_strategy = st.builds(
    alf_AndExpression,
)
alf_ExclusiveOrExpression_strategy = st.builds(
    alf_ExclusiveOrExpression,
)
alf_InclusiveOrExpression_strategy = st.builds(
    alf_InclusiveOrExpression,
)
alf_ConditionalAndExpression_strategy = st.builds(
    alf_ConditionalAndExpression,
)
alf_ConditionalOrExpression_strategy = st.builds(
    alf_ConditionalOrExpression,
)
Expression_strategy = st.builds(
    Expression,
)
alf_ConditionalTestExpression_strategy = st.builds(
    alf_ConditionalTestExpression,
)
SequenceElement_strategy = st.builds(
    SequenceElement,
)
alf_SequenceConstructionExpression_strategy = st.builds(
    alf_SequenceConstructionExpression,
)
alf_TupleElement_strategy = st.builds(
    alf_TupleElement,
)
alf_QualifiedNameWithBinding_strategy = st.builds(
    alf_QualifiedNameWithBinding,
    id=
        safe_text
)
alf_NamedTemplateBinding_strategy = st.builds(
    alf_NamedTemplateBinding,
    formal=
        safe_text
)
alf_RelationalExpression_strategy = st.builds(
    alf_RelationalExpression,
    op=
        safe_text
)
alf_TemplateBinding_strategy = st.builds(
    alf_TemplateBinding,
)
alf_UnqualifiedName_strategy = st.builds(
    alf_UnqualifiedName,
    name=
        safe_text
)
alf_SuffixExpression_strategy = st.builds(
    alf_SuffixExpression,
)
alf_SequenceConstructionOrAccessCompletion_strategy = st.builds(
    alf_SequenceConstructionOrAccessCompletion,
    multiplicityIndicator=
        st.booleans()
)
alf_Tuple_strategy = st.builds(
    alf_Tuple,
)
alf_QualifiedNamePath_strategy = st.builds(
    alf_QualifiedNamePath,
)
NonLiteralValueSpecification_strategy = st.builds(
    NonLiteralValueSpecification,
)
NUMBER_LITERAL_strategy = st.builds(
    NUMBER_LITERAL,
)
alf_UNLIMITED_LITERAL_strategy = st.builds(
    alf_UNLIMITED_LITERAL,
)
alf_INTEGER_LITERAL_strategy = st.builds(
    alf_INTEGER_LITERAL,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
alf_NameExpression_strategy = st.builds(
    alf_NameExpression,
    postfixOp=
        safe_text,
    prefixOp=
        safe_text,
    id=
        safe_text
)
alf_ThisExpression_strategy = st.builds(
    alf_ThisExpression,
)
alf_NullExpression_strategy = st.builds(
    alf_NullExpression,
)
alf_SuperInvocationExpression_strategy = st.builds(
    alf_SuperInvocationExpression,
)
alf_ParenthesizedExpression_strategy = st.builds(
    alf_ParenthesizedExpression,
)
alf_InstanceCreationExpression_strategy = st.builds(
    alf_InstanceCreationExpression,
)
alf_LITERAL_strategy = st.builds(
    alf_LITERAL,
)
alf_Block_strategy = st.builds(
    alf_Block,
)
alf_Statement_strategy = st.builds(
    alf_Statement,
)
alf_AssignmentCompletion_strategy = st.builds(
    alf_AssignmentCompletion,
    op=
        safe_text
)
alf_Expression_strategy = st.builds(
    alf_Expression,
)
alf_Test_strategy = st.builds(
    alf_Test,
)
LITERAL_strategy = st.builds(
    LITERAL,
)
alf_NUMBER_LITERAL_strategy = st.builds(
    alf_NUMBER_LITERAL,
    value=
        safe_text
)
alf_STRING_LITERAL_strategy = st.builds(
    alf_STRING_LITERAL,
    value=
        safe_text
)
alf_BOOLEAN_LITERAL_strategy = st.builds(
    alf_BOOLEAN_LITERAL,
    value=
        safe_text
)

@given(instance=alf_VariableDeclarationCompletion_strategy)
@settings(max_examples=50)
def test_alf_variabledeclarationcompletion_instantiation(instance):
    assert isinstance(instance, alf_VariableDeclarationCompletion)



@given(instance=alf_VariableDeclarationCompletion_strategy)
def test_alf_variabledeclarationcompletion_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=alf_VariableDeclarationCompletion_strategy)
def test_alf_variabledeclarationcompletion_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original

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

@given(instance=alf_QualifiedNameList_strategy)
@settings(max_examples=50)
def test_alf_qualifiednamelist_instantiation(instance):
    assert isinstance(instance, alf_QualifiedNameList)

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

@given(instance=alf_AcceptClause_strategy)
@settings(max_examples=50)
def test_alf_acceptclause_instantiation(instance):
    assert isinstance(instance, alf_AcceptClause)



@given(instance=alf_AcceptClause_strategy)
def test_alf_acceptclause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf_LoopVariableDefinition_strategy)
@settings(max_examples=50)
def test_alf_loopvariabledefinition_instantiation(instance):
    assert isinstance(instance, alf_LoopVariableDefinition)



@given(instance=alf_LoopVariableDefinition_strategy)
def test_alf_loopvariabledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf_ForControl_strategy)
@settings(max_examples=50)
def test_alf_forcontrol_instantiation(instance):
    assert isinstance(instance, alf_ForControl)

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

@given(instance=alf_Annotation_strategy)
@settings(max_examples=50)
def test_alf_annotation_instantiation(instance):
    assert isinstance(instance, alf_Annotation)



@given(instance=alf_Annotation_strategy)
def test_alf_annotation_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original



@given(instance=alf_Annotation_strategy)
def test_alf_annotation_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=alf_ThisInvocationStatement_strategy)
@settings(max_examples=50)
def test_alf_thisinvocationstatement_instantiation(instance):
    assert isinstance(instance, alf_ThisInvocationStatement)

@given(instance=alf_EmptyStatement_strategy)
@settings(max_examples=50)
def test_alf_emptystatement_instantiation(instance):
    assert isinstance(instance, alf_EmptyStatement)

@given(instance=alf_BreakStatement_strategy)
@settings(max_examples=50)
def test_alf_breakstatement_instantiation(instance):
    assert isinstance(instance, alf_BreakStatement)

@given(instance=alf_ForStatement_strategy)
@settings(max_examples=50)
def test_alf_forstatement_instantiation(instance):
    assert isinstance(instance, alf_ForStatement)

@given(instance=alf_BlockStatement_strategy)
@settings(max_examples=50)
def test_alf_blockstatement_instantiation(instance):
    assert isinstance(instance, alf_BlockStatement)

@given(instance=alf_AcceptStatement_strategy)
@settings(max_examples=50)
def test_alf_acceptstatement_instantiation(instance):
    assert isinstance(instance, alf_AcceptStatement)

@given(instance=alf_AnnotatedStatement_strategy)
@settings(max_examples=50)
def test_alf_annotatedstatement_instantiation(instance):
    assert isinstance(instance, alf_AnnotatedStatement)

@given(instance=alf_SwitchStatement_strategy)
@settings(max_examples=50)
def test_alf_switchstatement_instantiation(instance):
    assert isinstance(instance, alf_SwitchStatement)

@given(instance=alf_InvocationOrAssignementOrDeclarationStatement_strategy)
@settings(max_examples=50)
def test_alf_invocationorassignementordeclarationstatement_instantiation(instance):
    assert isinstance(instance, alf_InvocationOrAssignementOrDeclarationStatement)

@given(instance=alf_ReturnStatement_strategy)
@settings(max_examples=50)
def test_alf_returnstatement_instantiation(instance):
    assert isinstance(instance, alf_ReturnStatement)

@given(instance=alf_SuperInvocationStatement_strategy)
@settings(max_examples=50)
def test_alf_superinvocationstatement_instantiation(instance):
    assert isinstance(instance, alf_SuperInvocationStatement)

@given(instance=alf_ClassifyStatement_strategy)
@settings(max_examples=50)
def test_alf_classifystatement_instantiation(instance):
    assert isinstance(instance, alf_ClassifyStatement)

@given(instance=alf_WhileStatement_strategy)
@settings(max_examples=50)
def test_alf_whilestatement_instantiation(instance):
    assert isinstance(instance, alf_WhileStatement)

@given(instance=alf_DoStatement_strategy)
@settings(max_examples=50)
def test_alf_dostatement_instantiation(instance):
    assert isinstance(instance, alf_DoStatement)

@given(instance=alf_IfStatement_strategy)
@settings(max_examples=50)
def test_alf_ifstatement_instantiation(instance):
    assert isinstance(instance, alf_IfStatement)

@given(instance=alf_InstanceCreationInvocationStatement_strategy)
@settings(max_examples=50)
def test_alf_instancecreationinvocationstatement_instantiation(instance):
    assert isinstance(instance, alf_InstanceCreationInvocationStatement)

@given(instance=alf_InlineStatement_strategy)
@settings(max_examples=50)
def test_alf_inlinestatement_instantiation(instance):
    assert isinstance(instance, alf_InlineStatement)



@given(instance=alf_InlineStatement_strategy)
def test_alf_inlinestatement_langageName_setter(instance):
    original = instance.langageName
    instance.langageName = original
    assert instance.langageName == original



@given(instance=alf_InlineStatement_strategy)
def test_alf_inlinestatement_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

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

@given(instance=alf_SequenceElement_strategy)
@settings(max_examples=50)
def test_alf_sequenceelement_instantiation(instance):
    assert isinstance(instance, alf_SequenceElement)

@given(instance=alf_LocalNameDeclarationStatement_strategy)
@settings(max_examples=50)
def test_alf_localnamedeclarationstatement_instantiation(instance):
    assert isinstance(instance, alf_LocalNameDeclarationStatement)



@given(instance=alf_LocalNameDeclarationStatement_strategy)
def test_alf_localnamedeclarationstatement_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original



@given(instance=alf_LocalNameDeclarationStatement_strategy)
def test_alf_localnamedeclarationstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=alf_PartialSequenceConstructionCompletion_strategy)
@settings(max_examples=50)
def test_alf_partialsequenceconstructioncompletion_instantiation(instance):
    assert isinstance(instance, alf_PartialSequenceConstructionCompletion)

@given(instance=alf_AccessCompletion_strategy)
@settings(max_examples=50)
def test_alf_accesscompletion_instantiation(instance):
    assert isinstance(instance, alf_AccessCompletion)

@given(instance=alf_InstanceCreationTupleElement_strategy)
@settings(max_examples=50)
def test_alf_instancecreationtupleelement_instantiation(instance):
    assert isinstance(instance, alf_InstanceCreationTupleElement)



@given(instance=alf_InstanceCreationTupleElement_strategy)
def test_alf_instancecreationtupleelement_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=alf_InstanceCreationTuple_strategy)
@settings(max_examples=50)
def test_alf_instancecreationtuple_instantiation(instance):
    assert isinstance(instance, alf_InstanceCreationTuple)

@given(instance=alf_NonLiteralValueSpecification_strategy)
@settings(max_examples=50)
def test_alf_nonliteralvaluespecification_instantiation(instance):
    assert isinstance(instance, alf_NonLiteralValueSpecification)

@given(instance=SequenceExpansionExpression_strategy)
@settings(max_examples=50)
def test_sequenceexpansionexpression_instantiation(instance):
    assert isinstance(instance, SequenceExpansionExpression)

@given(instance=alf_IsUniqueOperation_strategy)
@settings(max_examples=50)
def test_alf_isuniqueoperation_instantiation(instance):
    assert isinstance(instance, alf_IsUniqueOperation)

@given(instance=alf_ForAllOrExistsOrOneOperation_strategy)
@settings(max_examples=50)
def test_alf_forallorexistsoroneoperation_instantiation(instance):
    assert isinstance(instance, alf_ForAllOrExistsOrOneOperation)



@given(instance=alf_ForAllOrExistsOrOneOperation_strategy)
def test_alf_forallorexistsoroneoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_CollectOrIterateOperation_strategy)
@settings(max_examples=50)
def test_alf_collectoriterateoperation_instantiation(instance):
    assert isinstance(instance, alf_CollectOrIterateOperation)



@given(instance=alf_CollectOrIterateOperation_strategy)
def test_alf_collectoriterateoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_SelectOrRejectOperation_strategy)
@settings(max_examples=50)
def test_alf_selectorrejectoperation_instantiation(instance):
    assert isinstance(instance, alf_SelectOrRejectOperation)



@given(instance=alf_SelectOrRejectOperation_strategy)
def test_alf_selectorrejectoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_LinkOperationTupleElement_strategy)
@settings(max_examples=50)
def test_alf_linkoperationtupleelement_instantiation(instance):
    assert isinstance(instance, alf_LinkOperationTupleElement)



@given(instance=alf_LinkOperationTupleElement_strategy)
def test_alf_linkoperationtupleelement_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=alf_LinkOperationTuple_strategy)
@settings(max_examples=50)
def test_alf_linkoperationtuple_instantiation(instance):
    assert isinstance(instance, alf_LinkOperationTuple)

@given(instance=SuffixExpression_strategy)
@settings(max_examples=50)
def test_suffixexpression_instantiation(instance):
    assert isinstance(instance, SuffixExpression)

@given(instance=alf_LinkOperationExpression_strategy)
@settings(max_examples=50)
def test_alf_linkoperationexpression_instantiation(instance):
    assert isinstance(instance, alf_LinkOperationExpression)



@given(instance=alf_LinkOperationExpression_strategy)
def test_alf_linkoperationexpression_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=alf_ClassExtentExpression_strategy)
@settings(max_examples=50)
def test_alf_classextentexpression_instantiation(instance):
    assert isinstance(instance, alf_ClassExtentExpression)

@given(instance=alf_SequenceExpansionExpression_strategy)
@settings(max_examples=50)
def test_alf_sequenceexpansionexpression_instantiation(instance):
    assert isinstance(instance, alf_SequenceExpansionExpression)



@given(instance=alf_SequenceExpansionExpression_strategy)
def test_alf_sequenceexpansionexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf_SequenceOperationExpression_strategy)
@settings(max_examples=50)
def test_alf_sequenceoperationexpression_instantiation(instance):
    assert isinstance(instance, alf_SequenceOperationExpression)

@given(instance=alf_SequenceReductionExpression_strategy)
@settings(max_examples=50)
def test_alf_sequencereductionexpression_instantiation(instance):
    assert isinstance(instance, alf_SequenceReductionExpression)



@given(instance=alf_SequenceReductionExpression_strategy)
def test_alf_sequencereductionexpression_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=alf_PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_alf_propertycallexpression_instantiation(instance):
    assert isinstance(instance, alf_PropertyCallExpression)



@given(instance=alf_PropertyCallExpression_strategy)
def test_alf_propertycallexpression_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=alf_OperationCallExpression_strategy)
@settings(max_examples=50)
def test_alf_operationcallexpression_instantiation(instance):
    assert isinstance(instance, alf_OperationCallExpression)



@given(instance=alf_OperationCallExpression_strategy)
def test_alf_operationcallexpression_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=alf_ValueSpecification_strategy)
@settings(max_examples=50)
def test_alf_valuespecification_instantiation(instance):
    assert isinstance(instance, alf_ValueSpecification)

@given(instance=alf_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf_primaryexpression_instantiation(instance):
    assert isinstance(instance, alf_PrimaryExpression)

@given(instance=alf_UnaryExpression_strategy)
@settings(max_examples=50)
def test_alf_unaryexpression_instantiation(instance):
    assert isinstance(instance, alf_UnaryExpression)



@given(instance=alf_UnaryExpression_strategy)
def test_alf_unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_alf_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, alf_MultiplicativeExpression)



@given(instance=alf_MultiplicativeExpression_strategy)
def test_alf_multiplicativeexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_alf_additiveexpression_instantiation(instance):
    assert isinstance(instance, alf_AdditiveExpression)



@given(instance=alf_AdditiveExpression_strategy)
def test_alf_additiveexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_ShiftExpression_strategy)
@settings(max_examples=50)
def test_alf_shiftexpression_instantiation(instance):
    assert isinstance(instance, alf_ShiftExpression)



@given(instance=alf_ShiftExpression_strategy)
def test_alf_shiftexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_ClassificationExpression_strategy)
@settings(max_examples=50)
def test_alf_classificationexpression_instantiation(instance):
    assert isinstance(instance, alf_ClassificationExpression)



@given(instance=alf_ClassificationExpression_strategy)
def test_alf_classificationexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_EqualityExpression_strategy)
@settings(max_examples=50)
def test_alf_equalityexpression_instantiation(instance):
    assert isinstance(instance, alf_EqualityExpression)



@given(instance=alf_EqualityExpression_strategy)
def test_alf_equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_AndExpression_strategy)
@settings(max_examples=50)
def test_alf_andexpression_instantiation(instance):
    assert isinstance(instance, alf_AndExpression)

@given(instance=alf_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf_ExclusiveOrExpression)

@given(instance=alf_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf_InclusiveOrExpression)

@given(instance=alf_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_alf_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, alf_ConditionalAndExpression)

@given(instance=alf_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_alf_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, alf_ConditionalOrExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=alf_ConditionalTestExpression_strategy)
@settings(max_examples=50)
def test_alf_conditionaltestexpression_instantiation(instance):
    assert isinstance(instance, alf_ConditionalTestExpression)

@given(instance=SequenceElement_strategy)
@settings(max_examples=50)
def test_sequenceelement_instantiation(instance):
    assert isinstance(instance, SequenceElement)

@given(instance=alf_SequenceConstructionExpression_strategy)
@settings(max_examples=50)
def test_alf_sequenceconstructionexpression_instantiation(instance):
    assert isinstance(instance, alf_SequenceConstructionExpression)

@given(instance=alf_TupleElement_strategy)
@settings(max_examples=50)
def test_alf_tupleelement_instantiation(instance):
    assert isinstance(instance, alf_TupleElement)

@given(instance=alf_QualifiedNameWithBinding_strategy)
@settings(max_examples=50)
def test_alf_qualifiednamewithbinding_instantiation(instance):
    assert isinstance(instance, alf_QualifiedNameWithBinding)



@given(instance=alf_QualifiedNameWithBinding_strategy)
def test_alf_qualifiednamewithbinding_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf_NamedTemplateBinding_strategy)
@settings(max_examples=50)
def test_alf_namedtemplatebinding_instantiation(instance):
    assert isinstance(instance, alf_NamedTemplateBinding)



@given(instance=alf_NamedTemplateBinding_strategy)
def test_alf_namedtemplatebinding_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=alf_RelationalExpression_strategy)
@settings(max_examples=50)
def test_alf_relationalexpression_instantiation(instance):
    assert isinstance(instance, alf_RelationalExpression)



@given(instance=alf_RelationalExpression_strategy)
def test_alf_relationalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_TemplateBinding_strategy)
@settings(max_examples=50)
def test_alf_templatebinding_instantiation(instance):
    assert isinstance(instance, alf_TemplateBinding)

@given(instance=alf_UnqualifiedName_strategy)
@settings(max_examples=50)
def test_alf_unqualifiedname_instantiation(instance):
    assert isinstance(instance, alf_UnqualifiedName)



@given(instance=alf_UnqualifiedName_strategy)
def test_alf_unqualifiedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf_SuffixExpression_strategy)
@settings(max_examples=50)
def test_alf_suffixexpression_instantiation(instance):
    assert isinstance(instance, alf_SuffixExpression)

@given(instance=alf_SequenceConstructionOrAccessCompletion_strategy)
@settings(max_examples=50)
def test_alf_sequenceconstructionoraccesscompletion_instantiation(instance):
    assert isinstance(instance, alf_SequenceConstructionOrAccessCompletion)



@given(instance=alf_SequenceConstructionOrAccessCompletion_strategy)
def test_alf_sequenceconstructionoraccesscompletion_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original

@given(instance=alf_Tuple_strategy)
@settings(max_examples=50)
def test_alf_tuple_instantiation(instance):
    assert isinstance(instance, alf_Tuple)

@given(instance=alf_QualifiedNamePath_strategy)
@settings(max_examples=50)
def test_alf_qualifiednamepath_instantiation(instance):
    assert isinstance(instance, alf_QualifiedNamePath)

@given(instance=NonLiteralValueSpecification_strategy)
@settings(max_examples=50)
def test_nonliteralvaluespecification_instantiation(instance):
    assert isinstance(instance, NonLiteralValueSpecification)

@given(instance=NUMBER_LITERAL_strategy)
@settings(max_examples=50)
def test_number_literal_instantiation(instance):
    assert isinstance(instance, NUMBER_LITERAL)

@given(instance=alf_UNLIMITED_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_unlimited_literal_instantiation(instance):
    assert isinstance(instance, alf_UNLIMITED_LITERAL)

@given(instance=alf_INTEGER_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_integer_literal_instantiation(instance):
    assert isinstance(instance, alf_INTEGER_LITERAL)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=alf_NameExpression_strategy)
@settings(max_examples=50)
def test_alf_nameexpression_instantiation(instance):
    assert isinstance(instance, alf_NameExpression)



@given(instance=alf_NameExpression_strategy)
def test_alf_nameexpression_postfixOp_setter(instance):
    original = instance.postfixOp
    instance.postfixOp = original
    assert instance.postfixOp == original



@given(instance=alf_NameExpression_strategy)
def test_alf_nameexpression_prefixOp_setter(instance):
    original = instance.prefixOp
    instance.prefixOp = original
    assert instance.prefixOp == original



@given(instance=alf_NameExpression_strategy)
def test_alf_nameexpression_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf_ThisExpression_strategy)
@settings(max_examples=50)
def test_alf_thisexpression_instantiation(instance):
    assert isinstance(instance, alf_ThisExpression)

@given(instance=alf_NullExpression_strategy)
@settings(max_examples=50)
def test_alf_nullexpression_instantiation(instance):
    assert isinstance(instance, alf_NullExpression)

@given(instance=alf_SuperInvocationExpression_strategy)
@settings(max_examples=50)
def test_alf_superinvocationexpression_instantiation(instance):
    assert isinstance(instance, alf_SuperInvocationExpression)

@given(instance=alf_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_alf_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, alf_ParenthesizedExpression)

@given(instance=alf_InstanceCreationExpression_strategy)
@settings(max_examples=50)
def test_alf_instancecreationexpression_instantiation(instance):
    assert isinstance(instance, alf_InstanceCreationExpression)

@given(instance=alf_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_literal_instantiation(instance):
    assert isinstance(instance, alf_LITERAL)

@given(instance=alf_Block_strategy)
@settings(max_examples=50)
def test_alf_block_instantiation(instance):
    assert isinstance(instance, alf_Block)

@given(instance=alf_Statement_strategy)
@settings(max_examples=50)
def test_alf_statement_instantiation(instance):
    assert isinstance(instance, alf_Statement)

@given(instance=alf_AssignmentCompletion_strategy)
@settings(max_examples=50)
def test_alf_assignmentcompletion_instantiation(instance):
    assert isinstance(instance, alf_AssignmentCompletion)



@given(instance=alf_AssignmentCompletion_strategy)
def test_alf_assignmentcompletion_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf_Expression_strategy)
@settings(max_examples=50)
def test_alf_expression_instantiation(instance):
    assert isinstance(instance, alf_Expression)

@given(instance=alf_Test_strategy)
@settings(max_examples=50)
def test_alf_test_instantiation(instance):
    assert isinstance(instance, alf_Test)

@given(instance=LITERAL_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, LITERAL)

@given(instance=alf_NUMBER_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_number_literal_instantiation(instance):
    assert isinstance(instance, alf_NUMBER_LITERAL)



@given(instance=alf_NUMBER_LITERAL_strategy)
def test_alf_number_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf_STRING_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_string_literal_instantiation(instance):
    assert isinstance(instance, alf_STRING_LITERAL)



@given(instance=alf_STRING_LITERAL_strategy)
def test_alf_string_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf_BOOLEAN_LITERAL_strategy)
@settings(max_examples=50)
def test_alf_boolean_literal_instantiation(instance):
    assert isinstance(instance, alf_BOOLEAN_LITERAL)



@given(instance=alf_BOOLEAN_LITERAL_strategy)
def test_alf_boolean_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
