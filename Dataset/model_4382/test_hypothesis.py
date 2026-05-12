import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    jcl_waters_Water,
    jcl_members_Member,
    jcl_conditions_ReturnCode,
    ReturnCode,
    conditions_PrimaryCondition,
    Operator,
    jcl_operators_UnaryOperator,
    PrimaryCondition,
    jcl_conditions_Only,
    jcl_conditions_NestedCondition,
    jcl_conditions_Even,
    jcl_conditions_Condition,
    jcl_references_ReferenceableElement,
    references_ElementReference,
    jcl_conditions_RelationalCondition,
    ReferenceableElement,
    Reference,
    jcl_references_ElementReference,
    jcl_references_Reference,
    conditions_ReturnCode,
    literals_Literal,
    jcl_literals_Literal,
    LogicOperator,
    jcl_operators_Or,
    jcl_operators_And,
    jcl_operators_LogicOperator,
    jcl_operators_RelationOperator,
    UnaryOperator,
    jcl_operators_Negate,
    PhraseableElement,
    jcl_operators_Operator,
    IdentifierReference,
    expressions_PrimaryExpression,
    jcl_references_IdentifierReference,
    jcl_literals_IntegerLiteral,
    PrimaryExpression,
    jcl_expressions_NestedExpression,
    RelationalExpressionChild,
    UnaryExpressionChild,
    jcl_expressions_PrimaryExpression,
    jcl_expressions_UnaryExpression,
    jcl_expressions_UnaryExpressionChild,
    And,
    Or,
    ConditionalOrExpressionChild,
    jcl_expressions_ConditionalAndExpressionChild,
    jcl_expressions_ConditionalAndExpression,
    ConditionalExpression,
    jcl_expressions_ConditionalOrExpressionChild,
    jcl_expressions_ConditionalOrExpression,
    RelationOperator,
    jcl_operators_NotEqual,
    jcl_operators_LessThan,
    jcl_operators_GreaterEqual,
    jcl_operators_Equal,
    jcl_operators_LessEqual,
    jcl_operators_GreaterThan,
    Expression,
    jcl_expressions_ConditionalExpression,
    ConditionalAndExpressionChild,
    jcl_expressions_RelationalExpressionChild,
    jcl_expressions_RelationalExpression,
    jcl_expressions_Expression,
    ExecuteProgram,
    commons_IncompleteElement,
    containers_JCLRoot,
    Member,
    jcl_containers_JCLRoot,
    Execute,
    jcl_statements_ExecuteProcedure,
    jcl_statements_ExecuteProgram,
    EndControl,
    statements_Statement,
    statements_StatementContainer,
    jcl_statements_Condition,
    jcl_statements_StatementContainer,
    Statement,
    jcl_statements_Output,
    jcl_statements_EndControl,
    jcl_statements_Command,
    jcl_statements_JCLLibrary,
    jcl_statements_Set,
    jcl_statements_Input,
    jcl_statements_Include,
    jcl_statements_Control,
    jcl_statements_Execute,
    members_Member,
    commons_NamedElement,
    jcl_procedures_Procedure,
    jcl_statements_Statement,
    jcl_containers_JobUnit,
    Condition,
    jcl_conditions_PrimaryCondition,
    Literal,
    jcl_literals_SpecialLiteral,
    jcl_literals_StringLiteral,
    jcl_commons_ProcedureStepElement,
    commons_ProcedureStepElement,
    jcl_expressions_Run,
    jcl_expressions_Abend,
    jcl_statements_DataDefinition,
    parameters_Parameter,
    jcl_parameters_Other,
    jcl_parameters_Condition,
    jcl_parameters_AccountInfo,
    jcl_parameters_Argument,
    jcl_parameters_AddressSpace,
    Parameter,
    jcl_parameters_TypeRun,
    jcl_parameters_JobClass,
    jcl_parameters_UserID,
    jcl_parameters_Bytes,
    jcl_parameters_Priority,
    jcl_parameters_DatasetName,
    jcl_parameters_Password,
    jcl_parameters_MessageLevel,
    jcl_parameters_MessageClass,
    jcl_parameters_Display,
    jcl_parameters_Parameter,
    Water,
    jcl_commons_IncompleteElement,
    jcl_commons_CommentableElement,
    jcl_commons_PhraseableElement,
    jcl_commons_NamedElement,
    AdressSpaceEnum,
    TypeRunEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jcl_waters_water_is_not_abstract():
    assert not inspect.isabstract(jcl_waters_Water)


def test_jcl_waters_water_constructor_exists():
    assert callable(jcl_waters_Water.__init__)


def test_jcl_waters_water_constructor_args():
    sig = inspect.signature(jcl_waters_Water.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_waters_water_has_value():
    assert hasattr(jcl_waters_Water, "value")
    descriptor = None
    for klass in jcl_waters_Water.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_members_member_is_not_abstract():
    assert not inspect.isabstract(jcl_members_Member)


def test_jcl_members_member_constructor_exists():
    assert callable(jcl_members_Member.__init__)


def test_jcl_members_member_constructor_args():
    sig = inspect.signature(jcl_members_Member.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_returncode_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_ReturnCode)


def test_jcl_conditions_returncode_constructor_exists():
    assert callable(jcl_conditions_ReturnCode.__init__)


def test_jcl_conditions_returncode_constructor_args():
    sig = inspect.signature(jcl_conditions_ReturnCode.__init__)
    params = list(sig.parameters.keys())



def test_returncode_is_not_abstract():
    assert not inspect.isabstract(ReturnCode)


def test_returncode_constructor_exists():
    assert callable(ReturnCode.__init__)


def test_returncode_constructor_args():
    sig = inspect.signature(ReturnCode.__init__)
    params = list(sig.parameters.keys())



def test_conditions_primarycondition_is_not_abstract():
    assert not inspect.isabstract(conditions_PrimaryCondition)


def test_conditions_primarycondition_constructor_exists():
    assert callable(conditions_PrimaryCondition.__init__)


def test_conditions_primarycondition_constructor_args():
    sig = inspect.signature(conditions_PrimaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_UnaryOperator)


def test_jcl_operators_unaryoperator_constructor_exists():
    assert callable(jcl_operators_UnaryOperator.__init__)


def test_jcl_operators_unaryoperator_constructor_args():
    sig = inspect.signature(jcl_operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_primarycondition_is_not_abstract():
    assert not inspect.isabstract(PrimaryCondition)


def test_primarycondition_constructor_exists():
    assert callable(PrimaryCondition.__init__)


def test_primarycondition_constructor_args():
    sig = inspect.signature(PrimaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_only_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_Only)


def test_jcl_conditions_only_constructor_exists():
    assert callable(jcl_conditions_Only.__init__)


def test_jcl_conditions_only_constructor_args():
    sig = inspect.signature(jcl_conditions_Only.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_nestedcondition_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_NestedCondition)


def test_jcl_conditions_nestedcondition_constructor_exists():
    assert callable(jcl_conditions_NestedCondition.__init__)


def test_jcl_conditions_nestedcondition_constructor_args():
    sig = inspect.signature(jcl_conditions_NestedCondition.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_even_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_Even)


def test_jcl_conditions_even_constructor_exists():
    assert callable(jcl_conditions_Even.__init__)


def test_jcl_conditions_even_constructor_args():
    sig = inspect.signature(jcl_conditions_Even.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_condition_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_Condition)


def test_jcl_conditions_condition_constructor_exists():
    assert callable(jcl_conditions_Condition.__init__)


def test_jcl_conditions_condition_constructor_args():
    sig = inspect.signature(jcl_conditions_Condition.__init__)
    params = list(sig.parameters.keys())



def test_jcl_references_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(jcl_references_ReferenceableElement)


def test_jcl_references_referenceableelement_constructor_exists():
    assert callable(jcl_references_ReferenceableElement.__init__)


def test_jcl_references_referenceableelement_constructor_args():
    sig = inspect.signature(jcl_references_ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_references_elementreference_is_not_abstract():
    assert not inspect.isabstract(references_ElementReference)


def test_references_elementreference_constructor_exists():
    assert callable(references_ElementReference.__init__)


def test_references_elementreference_constructor_args():
    sig = inspect.signature(references_ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_relationalcondition_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_RelationalCondition)


def test_jcl_conditions_relationalcondition_constructor_exists():
    assert callable(jcl_conditions_RelationalCondition.__init__)


def test_jcl_conditions_relationalcondition_constructor_args():
    sig = inspect.signature(jcl_conditions_RelationalCondition.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_jcl_references_elementreference_is_not_abstract():
    assert not inspect.isabstract(jcl_references_ElementReference)


def test_jcl_references_elementreference_constructor_exists():
    assert callable(jcl_references_ElementReference.__init__)


def test_jcl_references_elementreference_constructor_args():
    sig = inspect.signature(jcl_references_ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_jcl_references_reference_is_not_abstract():
    assert not inspect.isabstract(jcl_references_Reference)


def test_jcl_references_reference_constructor_exists():
    assert callable(jcl_references_Reference.__init__)


def test_jcl_references_reference_constructor_args():
    sig = inspect.signature(jcl_references_Reference.__init__)
    params = list(sig.parameters.keys())



def test_conditions_returncode_is_not_abstract():
    assert not inspect.isabstract(conditions_ReturnCode)


def test_conditions_returncode_constructor_exists():
    assert callable(conditions_ReturnCode.__init__)


def test_conditions_returncode_constructor_args():
    sig = inspect.signature(conditions_ReturnCode.__init__)
    params = list(sig.parameters.keys())



def test_literals_literal_is_not_abstract():
    assert not inspect.isabstract(literals_Literal)


def test_literals_literal_constructor_exists():
    assert callable(literals_Literal.__init__)


def test_literals_literal_constructor_args():
    sig = inspect.signature(literals_Literal.__init__)
    params = list(sig.parameters.keys())



def test_jcl_literals_literal_is_not_abstract():
    assert not inspect.isabstract(jcl_literals_Literal)


def test_jcl_literals_literal_constructor_exists():
    assert callable(jcl_literals_Literal.__init__)


def test_jcl_literals_literal_constructor_args():
    sig = inspect.signature(jcl_literals_Literal.__init__)
    params = list(sig.parameters.keys())



def test_logicoperator_is_not_abstract():
    assert not inspect.isabstract(LogicOperator)


def test_logicoperator_constructor_exists():
    assert callable(LogicOperator.__init__)


def test_logicoperator_constructor_args():
    sig = inspect.signature(LogicOperator.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_or_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_Or)


def test_jcl_operators_or_constructor_exists():
    assert callable(jcl_operators_Or.__init__)


def test_jcl_operators_or_constructor_args():
    sig = inspect.signature(jcl_operators_Or.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_and_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_And)


def test_jcl_operators_and_constructor_exists():
    assert callable(jcl_operators_And.__init__)


def test_jcl_operators_and_constructor_args():
    sig = inspect.signature(jcl_operators_And.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_logicoperator_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_LogicOperator)


def test_jcl_operators_logicoperator_constructor_exists():
    assert callable(jcl_operators_LogicOperator.__init__)


def test_jcl_operators_logicoperator_constructor_args():
    sig = inspect.signature(jcl_operators_LogicOperator.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_relationoperator_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_RelationOperator)


def test_jcl_operators_relationoperator_constructor_exists():
    assert callable(jcl_operators_RelationOperator.__init__)


def test_jcl_operators_relationoperator_constructor_args():
    sig = inspect.signature(jcl_operators_RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_negate_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_Negate)


def test_jcl_operators_negate_constructor_exists():
    assert callable(jcl_operators_Negate.__init__)


def test_jcl_operators_negate_constructor_args():
    sig = inspect.signature(jcl_operators_Negate.__init__)
    params = list(sig.parameters.keys())



def test_phraseableelement_is_not_abstract():
    assert not inspect.isabstract(PhraseableElement)


def test_phraseableelement_constructor_exists():
    assert callable(PhraseableElement.__init__)


def test_phraseableelement_constructor_args():
    sig = inspect.signature(PhraseableElement.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_operator_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_Operator)


def test_jcl_operators_operator_constructor_exists():
    assert callable(jcl_operators_Operator.__init__)


def test_jcl_operators_operator_constructor_args():
    sig = inspect.signature(jcl_operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_expressions_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimaryExpression)


def test_expressions_primaryexpression_constructor_exists():
    assert callable(expressions_PrimaryExpression.__init__)


def test_expressions_primaryexpression_constructor_args():
    sig = inspect.signature(expressions_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_references_identifierreference_is_not_abstract():
    assert not inspect.isabstract(jcl_references_IdentifierReference)


def test_jcl_references_identifierreference_constructor_exists():
    assert callable(jcl_references_IdentifierReference.__init__)


def test_jcl_references_identifierreference_constructor_args():
    sig = inspect.signature(jcl_references_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_jcl_literals_integerliteral_is_not_abstract():
    assert not inspect.isabstract(jcl_literals_IntegerLiteral)


def test_jcl_literals_integerliteral_constructor_exists():
    assert callable(jcl_literals_IntegerLiteral.__init__)


def test_jcl_literals_integerliteral_constructor_args():
    sig = inspect.signature(jcl_literals_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_literals_integerliteral_has_value():
    assert hasattr(jcl_literals_IntegerLiteral, "value")
    descriptor = None
    for klass in jcl_literals_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_NestedExpression)


def test_jcl_expressions_nestedexpression_constructor_exists():
    assert callable(jcl_expressions_NestedExpression.__init__)


def test_jcl_expressions_nestedexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_relationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RelationalExpressionChild)


def test_relationalexpressionchild_constructor_exists():
    assert callable(RelationalExpressionChild.__init__)


def test_relationalexpressionchild_constructor_args():
    sig = inspect.signature(RelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpressionChild)


def test_unaryexpressionchild_constructor_exists():
    assert callable(UnaryExpressionChild.__init__)


def test_unaryexpressionchild_constructor_args():
    sig = inspect.signature(UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_PrimaryExpression)


def test_jcl_expressions_primaryexpression_constructor_exists():
    assert callable(jcl_expressions_PrimaryExpression.__init__)


def test_jcl_expressions_primaryexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_UnaryExpression)


def test_jcl_expressions_unaryexpression_constructor_exists():
    assert callable(jcl_expressions_UnaryExpression.__init__)


def test_jcl_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_UnaryExpressionChild)


def test_jcl_expressions_unaryexpressionchild_constructor_exists():
    assert callable(jcl_expressions_UnaryExpressionChild.__init__)


def test_jcl_expressions_unaryexpressionchild_constructor_args():
    sig = inspect.signature(jcl_expressions_UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_and_is_not_abstract():
    assert not inspect.isabstract(And)


def test_and_constructor_exists():
    assert callable(And.__init__)


def test_and_constructor_args():
    sig = inspect.signature(And.__init__)
    params = list(sig.parameters.keys())



def test_or_is_not_abstract():
    assert not inspect.isabstract(Or)


def test_or_constructor_exists():
    assert callable(Or.__init__)


def test_or_constructor_args():
    sig = inspect.signature(Or.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpressionChild)


def test_conditionalorexpressionchild_constructor_exists():
    assert callable(ConditionalOrExpressionChild.__init__)


def test_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_ConditionalAndExpressionChild)


def test_jcl_expressions_conditionalandexpressionchild_constructor_exists():
    assert callable(jcl_expressions_ConditionalAndExpressionChild.__init__)


def test_jcl_expressions_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(jcl_expressions_ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_ConditionalAndExpression)


def test_jcl_expressions_conditionalandexpression_constructor_exists():
    assert callable(jcl_expressions_ConditionalAndExpression.__init__)


def test_jcl_expressions_conditionalandexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalExpression)


def test_conditionalexpression_constructor_exists():
    assert callable(ConditionalExpression.__init__)


def test_conditionalexpression_constructor_args():
    sig = inspect.signature(ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_ConditionalOrExpressionChild)


def test_jcl_expressions_conditionalorexpressionchild_constructor_exists():
    assert callable(jcl_expressions_ConditionalOrExpressionChild.__init__)


def test_jcl_expressions_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(jcl_expressions_ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_ConditionalOrExpression)


def test_jcl_expressions_conditionalorexpression_constructor_exists():
    assert callable(jcl_expressions_ConditionalOrExpression.__init__)


def test_jcl_expressions_conditionalorexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_notequal_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_NotEqual)


def test_jcl_operators_notequal_constructor_exists():
    assert callable(jcl_operators_NotEqual.__init__)


def test_jcl_operators_notequal_constructor_args():
    sig = inspect.signature(jcl_operators_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_lessthan_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_LessThan)


def test_jcl_operators_lessthan_constructor_exists():
    assert callable(jcl_operators_LessThan.__init__)


def test_jcl_operators_lessthan_constructor_args():
    sig = inspect.signature(jcl_operators_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_greaterequal_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_GreaterEqual)


def test_jcl_operators_greaterequal_constructor_exists():
    assert callable(jcl_operators_GreaterEqual.__init__)


def test_jcl_operators_greaterequal_constructor_args():
    sig = inspect.signature(jcl_operators_GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_equal_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_Equal)


def test_jcl_operators_equal_constructor_exists():
    assert callable(jcl_operators_Equal.__init__)


def test_jcl_operators_equal_constructor_args():
    sig = inspect.signature(jcl_operators_Equal.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_lessequal_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_LessEqual)


def test_jcl_operators_lessequal_constructor_exists():
    assert callable(jcl_operators_LessEqual.__init__)


def test_jcl_operators_lessequal_constructor_args():
    sig = inspect.signature(jcl_operators_LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_jcl_operators_greaterthan_is_not_abstract():
    assert not inspect.isabstract(jcl_operators_GreaterThan)


def test_jcl_operators_greaterthan_constructor_exists():
    assert callable(jcl_operators_GreaterThan.__init__)


def test_jcl_operators_greaterthan_constructor_args():
    sig = inspect.signature(jcl_operators_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_ConditionalExpression)


def test_jcl_expressions_conditionalexpression_constructor_exists():
    assert callable(jcl_expressions_ConditionalExpression.__init__)


def test_jcl_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_relationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_RelationalExpressionChild)


def test_jcl_expressions_relationalexpressionchild_constructor_exists():
    assert callable(jcl_expressions_RelationalExpressionChild.__init__)


def test_jcl_expressions_relationalexpressionchild_constructor_args():
    sig = inspect.signature(jcl_expressions_RelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_RelationalExpression)


def test_jcl_expressions_relationalexpression_constructor_exists():
    assert callable(jcl_expressions_RelationalExpression.__init__)


def test_jcl_expressions_relationalexpression_constructor_args():
    sig = inspect.signature(jcl_expressions_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_Expression)


def test_jcl_expressions_expression_constructor_exists():
    assert callable(jcl_expressions_Expression.__init__)


def test_jcl_expressions_expression_constructor_args():
    sig = inspect.signature(jcl_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_executeprogram_is_not_abstract():
    assert not inspect.isabstract(ExecuteProgram)


def test_executeprogram_constructor_exists():
    assert callable(ExecuteProgram.__init__)


def test_executeprogram_constructor_args():
    sig = inspect.signature(ExecuteProgram.__init__)
    params = list(sig.parameters.keys())



def test_commons_incompleteelement_is_not_abstract():
    assert not inspect.isabstract(commons_IncompleteElement)


def test_commons_incompleteelement_constructor_exists():
    assert callable(commons_IncompleteElement.__init__)


def test_commons_incompleteelement_constructor_args():
    sig = inspect.signature(commons_IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_containers_jclroot_is_not_abstract():
    assert not inspect.isabstract(containers_JCLRoot)


def test_containers_jclroot_constructor_exists():
    assert callable(containers_JCLRoot.__init__)


def test_containers_jclroot_constructor_args():
    sig = inspect.signature(containers_JCLRoot.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_jcl_containers_jclroot_is_not_abstract():
    assert not inspect.isabstract(jcl_containers_JCLRoot)


def test_jcl_containers_jclroot_constructor_exists():
    assert callable(jcl_containers_JCLRoot.__init__)


def test_jcl_containers_jclroot_constructor_args():
    sig = inspect.signature(jcl_containers_JCLRoot.__init__)
    params = list(sig.parameters.keys())



def test_execute_is_not_abstract():
    assert not inspect.isabstract(Execute)


def test_execute_constructor_exists():
    assert callable(Execute.__init__)


def test_execute_constructor_args():
    sig = inspect.signature(Execute.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_executeprocedure_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_ExecuteProcedure)


def test_jcl_statements_executeprocedure_constructor_exists():
    assert callable(jcl_statements_ExecuteProcedure.__init__)


def test_jcl_statements_executeprocedure_constructor_args():
    sig = inspect.signature(jcl_statements_ExecuteProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "procedureName" in params, "Missing parameter 'procedureName'"

def test_jcl_statements_executeprocedure_has_procedureName():
    assert hasattr(jcl_statements_ExecuteProcedure, "procedureName")
    descriptor = None
    for klass in jcl_statements_ExecuteProcedure.__mro__:
        if "procedureName" in klass.__dict__:
            descriptor = klass.__dict__["procedureName"]
            break
    assert isinstance(descriptor, property)



def test_jcl_statements_executeprogram_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_ExecuteProgram)


def test_jcl_statements_executeprogram_constructor_exists():
    assert callable(jcl_statements_ExecuteProgram.__init__)


def test_jcl_statements_executeprogram_constructor_args():
    sig = inspect.signature(jcl_statements_ExecuteProgram.__init__)
    params = list(sig.parameters.keys())
    assert "programName" in params, "Missing parameter 'programName'"

def test_jcl_statements_executeprogram_has_programName():
    assert hasattr(jcl_statements_ExecuteProgram, "programName")
    descriptor = None
    for klass in jcl_statements_ExecuteProgram.__mro__:
        if "programName" in klass.__dict__:
            descriptor = klass.__dict__["programName"]
            break
    assert isinstance(descriptor, property)



def test_endcontrol_is_not_abstract():
    assert not inspect.isabstract(EndControl)


def test_endcontrol_constructor_exists():
    assert callable(EndControl.__init__)


def test_endcontrol_constructor_args():
    sig = inspect.signature(EndControl.__init__)
    params = list(sig.parameters.keys())



def test_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statements_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(statements_StatementContainer)


def test_statements_statementcontainer_constructor_exists():
    assert callable(statements_StatementContainer.__init__)


def test_statements_statementcontainer_constructor_args():
    sig = inspect.signature(statements_StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_condition_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Condition)


def test_jcl_statements_condition_constructor_exists():
    assert callable(jcl_statements_Condition.__init__)


def test_jcl_statements_condition_constructor_args():
    sig = inspect.signature(jcl_statements_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"
    assert "elseName" in params, "Missing parameter 'elseName'"

def test_jcl_statements_condition_has_endName():
    assert hasattr(jcl_statements_Condition, "endName")
    descriptor = None
    for klass in jcl_statements_Condition.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)

def test_jcl_statements_condition_has_elseName():
    assert hasattr(jcl_statements_Condition, "elseName")
    descriptor = None
    for klass in jcl_statements_Condition.__mro__:
        if "elseName" in klass.__dict__:
            descriptor = klass.__dict__["elseName"]
            break
    assert isinstance(descriptor, property)



def test_jcl_statements_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_StatementContainer)


def test_jcl_statements_statementcontainer_constructor_exists():
    assert callable(jcl_statements_StatementContainer.__init__)


def test_jcl_statements_statementcontainer_constructor_args():
    sig = inspect.signature(jcl_statements_StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_output_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Output)


def test_jcl_statements_output_constructor_exists():
    assert callable(jcl_statements_Output.__init__)


def test_jcl_statements_output_constructor_args():
    sig = inspect.signature(jcl_statements_Output.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_endcontrol_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_EndControl)


def test_jcl_statements_endcontrol_constructor_exists():
    assert callable(jcl_statements_EndControl.__init__)


def test_jcl_statements_endcontrol_constructor_args():
    sig = inspect.signature(jcl_statements_EndControl.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_command_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Command)


def test_jcl_statements_command_constructor_exists():
    assert callable(jcl_statements_Command.__init__)


def test_jcl_statements_command_constructor_args():
    sig = inspect.signature(jcl_statements_Command.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_statements_command_has_value():
    assert hasattr(jcl_statements_Command, "value")
    descriptor = None
    for klass in jcl_statements_Command.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_statements_jcllibrary_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_JCLLibrary)


def test_jcl_statements_jcllibrary_constructor_exists():
    assert callable(jcl_statements_JCLLibrary.__init__)


def test_jcl_statements_jcllibrary_constructor_args():
    sig = inspect.signature(jcl_statements_JCLLibrary.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_set_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Set)


def test_jcl_statements_set_constructor_exists():
    assert callable(jcl_statements_Set.__init__)


def test_jcl_statements_set_constructor_args():
    sig = inspect.signature(jcl_statements_Set.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_input_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Input)


def test_jcl_statements_input_constructor_exists():
    assert callable(jcl_statements_Input.__init__)


def test_jcl_statements_input_constructor_args():
    sig = inspect.signature(jcl_statements_Input.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_include_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Include)


def test_jcl_statements_include_constructor_exists():
    assert callable(jcl_statements_Include.__init__)


def test_jcl_statements_include_constructor_args():
    sig = inspect.signature(jcl_statements_Include.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_control_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Control)


def test_jcl_statements_control_constructor_exists():
    assert callable(jcl_statements_Control.__init__)


def test_jcl_statements_control_constructor_args():
    sig = inspect.signature(jcl_statements_Control.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"

def test_jcl_statements_control_has_endName():
    assert hasattr(jcl_statements_Control, "endName")
    descriptor = None
    for klass in jcl_statements_Control.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)



def test_jcl_statements_execute_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Execute)


def test_jcl_statements_execute_constructor_exists():
    assert callable(jcl_statements_Execute.__init__)


def test_jcl_statements_execute_constructor_args():
    sig = inspect.signature(jcl_statements_Execute.__init__)
    params = list(sig.parameters.keys())



def test_members_member_is_not_abstract():
    assert not inspect.isabstract(members_Member)


def test_members_member_constructor_exists():
    assert callable(members_Member.__init__)


def test_members_member_constructor_args():
    sig = inspect.signature(members_Member.__init__)
    params = list(sig.parameters.keys())



def test_commons_namedelement_is_not_abstract():
    assert not inspect.isabstract(commons_NamedElement)


def test_commons_namedelement_constructor_exists():
    assert callable(commons_NamedElement.__init__)


def test_commons_namedelement_constructor_args():
    sig = inspect.signature(commons_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jcl_procedures_procedure_is_not_abstract():
    assert not inspect.isabstract(jcl_procedures_Procedure)


def test_jcl_procedures_procedure_constructor_exists():
    assert callable(jcl_procedures_Procedure.__init__)


def test_jcl_procedures_procedure_constructor_args():
    sig = inspect.signature(jcl_procedures_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"

def test_jcl_procedures_procedure_has_endName():
    assert hasattr(jcl_procedures_Procedure, "endName")
    descriptor = None
    for klass in jcl_procedures_Procedure.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)



def test_jcl_statements_statement_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_Statement)


def test_jcl_statements_statement_constructor_exists():
    assert callable(jcl_statements_Statement.__init__)


def test_jcl_statements_statement_constructor_args():
    sig = inspect.signature(jcl_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_jcl_containers_jobunit_is_not_abstract():
    assert not inspect.isabstract(jcl_containers_JobUnit)


def test_jcl_containers_jobunit_constructor_exists():
    assert callable(jcl_containers_JobUnit.__init__)


def test_jcl_containers_jobunit_constructor_args():
    sig = inspect.signature(jcl_containers_JobUnit.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_jcl_conditions_primarycondition_is_not_abstract():
    assert not inspect.isabstract(jcl_conditions_PrimaryCondition)


def test_jcl_conditions_primarycondition_constructor_exists():
    assert callable(jcl_conditions_PrimaryCondition.__init__)


def test_jcl_conditions_primarycondition_constructor_args():
    sig = inspect.signature(jcl_conditions_PrimaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_jcl_literals_specialliteral_is_not_abstract():
    assert not inspect.isabstract(jcl_literals_SpecialLiteral)


def test_jcl_literals_specialliteral_constructor_exists():
    assert callable(jcl_literals_SpecialLiteral.__init__)


def test_jcl_literals_specialliteral_constructor_args():
    sig = inspect.signature(jcl_literals_SpecialLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_literals_specialliteral_has_value():
    assert hasattr(jcl_literals_SpecialLiteral, "value")
    descriptor = None
    for klass in jcl_literals_SpecialLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_literals_stringliteral_is_not_abstract():
    assert not inspect.isabstract(jcl_literals_StringLiteral)


def test_jcl_literals_stringliteral_constructor_exists():
    assert callable(jcl_literals_StringLiteral.__init__)


def test_jcl_literals_stringliteral_constructor_args():
    sig = inspect.signature(jcl_literals_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_literals_stringliteral_has_value():
    assert hasattr(jcl_literals_StringLiteral, "value")
    descriptor = None
    for klass in jcl_literals_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_commons_procedurestepelement_is_not_abstract():
    assert not inspect.isabstract(jcl_commons_ProcedureStepElement)


def test_jcl_commons_procedurestepelement_constructor_exists():
    assert callable(jcl_commons_ProcedureStepElement.__init__)


def test_jcl_commons_procedurestepelement_constructor_args():
    sig = inspect.signature(jcl_commons_ProcedureStepElement.__init__)
    params = list(sig.parameters.keys())
    assert "procStepName" in params, "Missing parameter 'procStepName'"

def test_jcl_commons_procedurestepelement_has_procStepName():
    assert hasattr(jcl_commons_ProcedureStepElement, "procStepName")
    descriptor = None
    for klass in jcl_commons_ProcedureStepElement.__mro__:
        if "procStepName" in klass.__dict__:
            descriptor = klass.__dict__["procStepName"]
            break
    assert isinstance(descriptor, property)



def test_commons_procedurestepelement_is_not_abstract():
    assert not inspect.isabstract(commons_ProcedureStepElement)


def test_commons_procedurestepelement_constructor_exists():
    assert callable(commons_ProcedureStepElement.__init__)


def test_commons_procedurestepelement_constructor_args():
    sig = inspect.signature(commons_ProcedureStepElement.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_run_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_Run)


def test_jcl_expressions_run_constructor_exists():
    assert callable(jcl_expressions_Run.__init__)


def test_jcl_expressions_run_constructor_args():
    sig = inspect.signature(jcl_expressions_Run.__init__)
    params = list(sig.parameters.keys())



def test_jcl_expressions_abend_is_not_abstract():
    assert not inspect.isabstract(jcl_expressions_Abend)


def test_jcl_expressions_abend_constructor_exists():
    assert callable(jcl_expressions_Abend.__init__)


def test_jcl_expressions_abend_constructor_args():
    sig = inspect.signature(jcl_expressions_Abend.__init__)
    params = list(sig.parameters.keys())



def test_jcl_statements_datadefinition_is_not_abstract():
    assert not inspect.isabstract(jcl_statements_DataDefinition)


def test_jcl_statements_datadefinition_constructor_exists():
    assert callable(jcl_statements_DataDefinition.__init__)


def test_jcl_statements_datadefinition_constructor_args():
    sig = inspect.signature(jcl_statements_DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parameters_parameter_is_not_abstract():
    assert not inspect.isabstract(parameters_Parameter)


def test_parameters_parameter_constructor_exists():
    assert callable(parameters_Parameter.__init__)


def test_parameters_parameter_constructor_args():
    sig = inspect.signature(parameters_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_jcl_parameters_other_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Other)


def test_jcl_parameters_other_constructor_exists():
    assert callable(jcl_parameters_Other.__init__)


def test_jcl_parameters_other_constructor_args():
    sig = inspect.signature(jcl_parameters_Other.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_other_has_value():
    assert hasattr(jcl_parameters_Other, "value")
    descriptor = None
    for klass in jcl_parameters_Other.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_condition_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Condition)


def test_jcl_parameters_condition_constructor_exists():
    assert callable(jcl_parameters_Condition.__init__)


def test_jcl_parameters_condition_constructor_args():
    sig = inspect.signature(jcl_parameters_Condition.__init__)
    params = list(sig.parameters.keys())



def test_jcl_parameters_accountinfo_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_AccountInfo)


def test_jcl_parameters_accountinfo_constructor_exists():
    assert callable(jcl_parameters_AccountInfo.__init__)


def test_jcl_parameters_accountinfo_constructor_args():
    sig = inspect.signature(jcl_parameters_AccountInfo.__init__)
    params = list(sig.parameters.keys())



def test_jcl_parameters_argument_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Argument)


def test_jcl_parameters_argument_constructor_exists():
    assert callable(jcl_parameters_Argument.__init__)


def test_jcl_parameters_argument_constructor_args():
    sig = inspect.signature(jcl_parameters_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_argument_has_value():
    assert hasattr(jcl_parameters_Argument, "value")
    descriptor = None
    for klass in jcl_parameters_Argument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_addressspace_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_AddressSpace)


def test_jcl_parameters_addressspace_constructor_exists():
    assert callable(jcl_parameters_AddressSpace.__init__)


def test_jcl_parameters_addressspace_constructor_args():
    sig = inspect.signature(jcl_parameters_AddressSpace.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_addressspace_has_value():
    assert hasattr(jcl_parameters_AddressSpace, "value")
    descriptor = None
    for klass in jcl_parameters_AddressSpace.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_jcl_parameters_typerun_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_TypeRun)


def test_jcl_parameters_typerun_constructor_exists():
    assert callable(jcl_parameters_TypeRun.__init__)


def test_jcl_parameters_typerun_constructor_args():
    sig = inspect.signature(jcl_parameters_TypeRun.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_typerun_has_value():
    assert hasattr(jcl_parameters_TypeRun, "value")
    descriptor = None
    for klass in jcl_parameters_TypeRun.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_jobclass_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_JobClass)


def test_jcl_parameters_jobclass_constructor_exists():
    assert callable(jcl_parameters_JobClass.__init__)


def test_jcl_parameters_jobclass_constructor_args():
    sig = inspect.signature(jcl_parameters_JobClass.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_jobclass_has_value():
    assert hasattr(jcl_parameters_JobClass, "value")
    descriptor = None
    for klass in jcl_parameters_JobClass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_userid_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_UserID)


def test_jcl_parameters_userid_constructor_exists():
    assert callable(jcl_parameters_UserID.__init__)


def test_jcl_parameters_userid_constructor_args():
    sig = inspect.signature(jcl_parameters_UserID.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_userid_has_value():
    assert hasattr(jcl_parameters_UserID, "value")
    descriptor = None
    for klass in jcl_parameters_UserID.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_bytes_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Bytes)


def test_jcl_parameters_bytes_constructor_exists():
    assert callable(jcl_parameters_Bytes.__init__)


def test_jcl_parameters_bytes_constructor_args():
    sig = inspect.signature(jcl_parameters_Bytes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_bytes_has_value():
    assert hasattr(jcl_parameters_Bytes, "value")
    descriptor = None
    for klass in jcl_parameters_Bytes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_priority_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Priority)


def test_jcl_parameters_priority_constructor_exists():
    assert callable(jcl_parameters_Priority.__init__)


def test_jcl_parameters_priority_constructor_args():
    sig = inspect.signature(jcl_parameters_Priority.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_priority_has_value():
    assert hasattr(jcl_parameters_Priority, "value")
    descriptor = None
    for klass in jcl_parameters_Priority.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_datasetname_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_DatasetName)


def test_jcl_parameters_datasetname_constructor_exists():
    assert callable(jcl_parameters_DatasetName.__init__)


def test_jcl_parameters_datasetname_constructor_args():
    sig = inspect.signature(jcl_parameters_DatasetName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_datasetname_has_value():
    assert hasattr(jcl_parameters_DatasetName, "value")
    descriptor = None
    for klass in jcl_parameters_DatasetName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_password_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Password)


def test_jcl_parameters_password_constructor_exists():
    assert callable(jcl_parameters_Password.__init__)


def test_jcl_parameters_password_constructor_args():
    sig = inspect.signature(jcl_parameters_Password.__init__)
    params = list(sig.parameters.keys())
    assert "new" in params, "Missing parameter 'new'"
    assert "old" in params, "Missing parameter 'old'"

def test_jcl_parameters_password_has_new():
    assert hasattr(jcl_parameters_Password, "new")
    descriptor = None
    for klass in jcl_parameters_Password.__mro__:
        if "new" in klass.__dict__:
            descriptor = klass.__dict__["new"]
            break
    assert isinstance(descriptor, property)

def test_jcl_parameters_password_has_old():
    assert hasattr(jcl_parameters_Password, "old")
    descriptor = None
    for klass in jcl_parameters_Password.__mro__:
        if "old" in klass.__dict__:
            descriptor = klass.__dict__["old"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_messagelevel_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_MessageLevel)


def test_jcl_parameters_messagelevel_constructor_exists():
    assert callable(jcl_parameters_MessageLevel.__init__)


def test_jcl_parameters_messagelevel_constructor_args():
    sig = inspect.signature(jcl_parameters_MessageLevel.__init__)
    params = list(sig.parameters.keys())
    assert "statements" in params, "Missing parameter 'statements'"
    assert "messages" in params, "Missing parameter 'messages'"

def test_jcl_parameters_messagelevel_has_statements():
    assert hasattr(jcl_parameters_MessageLevel, "statements")
    descriptor = None
    for klass in jcl_parameters_MessageLevel.__mro__:
        if "statements" in klass.__dict__:
            descriptor = klass.__dict__["statements"]
            break
    assert isinstance(descriptor, property)

def test_jcl_parameters_messagelevel_has_messages():
    assert hasattr(jcl_parameters_MessageLevel, "messages")
    descriptor = None
    for klass in jcl_parameters_MessageLevel.__mro__:
        if "messages" in klass.__dict__:
            descriptor = klass.__dict__["messages"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_messageclass_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_MessageClass)


def test_jcl_parameters_messageclass_constructor_exists():
    assert callable(jcl_parameters_MessageClass.__init__)


def test_jcl_parameters_messageclass_constructor_args():
    sig = inspect.signature(jcl_parameters_MessageClass.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_messageclass_has_value():
    assert hasattr(jcl_parameters_MessageClass, "value")
    descriptor = None
    for klass in jcl_parameters_MessageClass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_display_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Display)


def test_jcl_parameters_display_constructor_exists():
    assert callable(jcl_parameters_Display.__init__)


def test_jcl_parameters_display_constructor_args():
    sig = inspect.signature(jcl_parameters_Display.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jcl_parameters_display_has_value():
    assert hasattr(jcl_parameters_Display, "value")
    descriptor = None
    for klass in jcl_parameters_Display.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jcl_parameters_parameter_is_not_abstract():
    assert not inspect.isabstract(jcl_parameters_Parameter)


def test_jcl_parameters_parameter_constructor_exists():
    assert callable(jcl_parameters_Parameter.__init__)


def test_jcl_parameters_parameter_constructor_args():
    sig = inspect.signature(jcl_parameters_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_water_is_not_abstract():
    assert not inspect.isabstract(Water)


def test_water_constructor_exists():
    assert callable(Water.__init__)


def test_water_constructor_args():
    sig = inspect.signature(Water.__init__)
    params = list(sig.parameters.keys())



def test_jcl_commons_incompleteelement_is_not_abstract():
    assert not inspect.isabstract(jcl_commons_IncompleteElement)


def test_jcl_commons_incompleteelement_constructor_exists():
    assert callable(jcl_commons_IncompleteElement.__init__)


def test_jcl_commons_incompleteelement_constructor_args():
    sig = inspect.signature(jcl_commons_IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_jcl_commons_commentableelement_is_not_abstract():
    assert not inspect.isabstract(jcl_commons_CommentableElement)


def test_jcl_commons_commentableelement_constructor_exists():
    assert callable(jcl_commons_CommentableElement.__init__)


def test_jcl_commons_commentableelement_constructor_args():
    sig = inspect.signature(jcl_commons_CommentableElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_jcl_commons_commentableelement_has_comment():
    assert hasattr(jcl_commons_CommentableElement, "comment")
    descriptor = None
    for klass in jcl_commons_CommentableElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_jcl_commons_phraseableelement_is_not_abstract():
    assert not inspect.isabstract(jcl_commons_PhraseableElement)


def test_jcl_commons_phraseableelement_constructor_exists():
    assert callable(jcl_commons_PhraseableElement.__init__)


def test_jcl_commons_phraseableelement_constructor_args():
    sig = inspect.signature(jcl_commons_PhraseableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isPhrase" in params, "Missing parameter 'isPhrase'"

def test_jcl_commons_phraseableelement_has_isPhrase():
    assert hasattr(jcl_commons_PhraseableElement, "isPhrase")
    descriptor = None
    for klass in jcl_commons_PhraseableElement.__mro__:
        if "isPhrase" in klass.__dict__:
            descriptor = klass.__dict__["isPhrase"]
            break
    assert isinstance(descriptor, property)



def test_jcl_commons_namedelement_is_not_abstract():
    assert not inspect.isabstract(jcl_commons_NamedElement)


def test_jcl_commons_namedelement_constructor_exists():
    assert callable(jcl_commons_NamedElement.__init__)


def test_jcl_commons_namedelement_constructor_args():
    sig = inspect.signature(jcl_commons_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jcl_commons_namedelement_has_name():
    assert hasattr(jcl_commons_NamedElement, "name")
    descriptor = None
    for klass in jcl_commons_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adressspaceenum_exists():
    # Check that the Enumeration exists
    assert AdressSpaceEnum is not None

def test_adressspaceenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdressSpaceEnum]
    expected_literals = [
        "real",
        "virtual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdressSpaceEnum"

def test_typerunenum_exists():
    # Check that the Enumeration exists
    assert TypeRunEnum is not None

def test_typerunenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRunEnum]
    expected_literals = [
        "scan",
        "copy",
        "hold",
        "jclhold",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRunEnum"


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
jcl_waters_Water_strategy = st.builds(
    jcl_waters_Water,
    value=
        safe_text
)
jcl_members_Member_strategy = st.builds(
    jcl_members_Member,
)
jcl_conditions_ReturnCode_strategy = st.builds(
    jcl_conditions_ReturnCode,
)
ReturnCode_strategy = st.builds(
    ReturnCode,
)
conditions_PrimaryCondition_strategy = st.builds(
    conditions_PrimaryCondition,
)
Operator_strategy = st.builds(
    Operator,
)
jcl_operators_UnaryOperator_strategy = st.builds(
    jcl_operators_UnaryOperator,
)
PrimaryCondition_strategy = st.builds(
    PrimaryCondition,
)
jcl_conditions_Only_strategy = st.builds(
    jcl_conditions_Only,
)
jcl_conditions_NestedCondition_strategy = st.builds(
    jcl_conditions_NestedCondition,
)
jcl_conditions_Even_strategy = st.builds(
    jcl_conditions_Even,
)
jcl_conditions_Condition_strategy = st.builds(
    jcl_conditions_Condition,
)
jcl_references_ReferenceableElement_strategy = st.builds(
    jcl_references_ReferenceableElement,
)
references_ElementReference_strategy = st.builds(
    references_ElementReference,
)
jcl_conditions_RelationalCondition_strategy = st.builds(
    jcl_conditions_RelationalCondition,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
Reference_strategy = st.builds(
    Reference,
)
jcl_references_ElementReference_strategy = st.builds(
    jcl_references_ElementReference,
)
jcl_references_Reference_strategy = st.builds(
    jcl_references_Reference,
)
conditions_ReturnCode_strategy = st.builds(
    conditions_ReturnCode,
)
literals_Literal_strategy = st.builds(
    literals_Literal,
)
jcl_literals_Literal_strategy = st.builds(
    jcl_literals_Literal,
)
LogicOperator_strategy = st.builds(
    LogicOperator,
)
jcl_operators_Or_strategy = st.builds(
    jcl_operators_Or,
)
jcl_operators_And_strategy = st.builds(
    jcl_operators_And,
)
jcl_operators_LogicOperator_strategy = st.builds(
    jcl_operators_LogicOperator,
)
jcl_operators_RelationOperator_strategy = st.builds(
    jcl_operators_RelationOperator,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
jcl_operators_Negate_strategy = st.builds(
    jcl_operators_Negate,
)
PhraseableElement_strategy = st.builds(
    PhraseableElement,
)
jcl_operators_Operator_strategy = st.builds(
    jcl_operators_Operator,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
expressions_PrimaryExpression_strategy = st.builds(
    expressions_PrimaryExpression,
)
jcl_references_IdentifierReference_strategy = st.builds(
    jcl_references_IdentifierReference,
)
jcl_literals_IntegerLiteral_strategy = st.builds(
    jcl_literals_IntegerLiteral,
    value=
        st.integers()
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
jcl_expressions_NestedExpression_strategy = st.builds(
    jcl_expressions_NestedExpression,
)
RelationalExpressionChild_strategy = st.builds(
    RelationalExpressionChild,
)
UnaryExpressionChild_strategy = st.builds(
    UnaryExpressionChild,
)
jcl_expressions_PrimaryExpression_strategy = st.builds(
    jcl_expressions_PrimaryExpression,
)
jcl_expressions_UnaryExpression_strategy = st.builds(
    jcl_expressions_UnaryExpression,
)
jcl_expressions_UnaryExpressionChild_strategy = st.builds(
    jcl_expressions_UnaryExpressionChild,
)
And_strategy = st.builds(
    And,
)
Or_strategy = st.builds(
    Or,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
jcl_expressions_ConditionalAndExpressionChild_strategy = st.builds(
    jcl_expressions_ConditionalAndExpressionChild,
)
jcl_expressions_ConditionalAndExpression_strategy = st.builds(
    jcl_expressions_ConditionalAndExpression,
)
ConditionalExpression_strategy = st.builds(
    ConditionalExpression,
)
jcl_expressions_ConditionalOrExpressionChild_strategy = st.builds(
    jcl_expressions_ConditionalOrExpressionChild,
)
jcl_expressions_ConditionalOrExpression_strategy = st.builds(
    jcl_expressions_ConditionalOrExpression,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
jcl_operators_NotEqual_strategy = st.builds(
    jcl_operators_NotEqual,
)
jcl_operators_LessThan_strategy = st.builds(
    jcl_operators_LessThan,
)
jcl_operators_GreaterEqual_strategy = st.builds(
    jcl_operators_GreaterEqual,
)
jcl_operators_Equal_strategy = st.builds(
    jcl_operators_Equal,
)
jcl_operators_LessEqual_strategy = st.builds(
    jcl_operators_LessEqual,
)
jcl_operators_GreaterThan_strategy = st.builds(
    jcl_operators_GreaterThan,
)
Expression_strategy = st.builds(
    Expression,
)
jcl_expressions_ConditionalExpression_strategy = st.builds(
    jcl_expressions_ConditionalExpression,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
jcl_expressions_RelationalExpressionChild_strategy = st.builds(
    jcl_expressions_RelationalExpressionChild,
)
jcl_expressions_RelationalExpression_strategy = st.builds(
    jcl_expressions_RelationalExpression,
)
jcl_expressions_Expression_strategy = st.builds(
    jcl_expressions_Expression,
)
ExecuteProgram_strategy = st.builds(
    ExecuteProgram,
)
commons_IncompleteElement_strategy = st.builds(
    commons_IncompleteElement,
)
containers_JCLRoot_strategy = st.builds(
    containers_JCLRoot,
)
Member_strategy = st.builds(
    Member,
)
jcl_containers_JCLRoot_strategy = st.builds(
    jcl_containers_JCLRoot,
)
Execute_strategy = st.builds(
    Execute,
)
jcl_statements_ExecuteProcedure_strategy = st.builds(
    jcl_statements_ExecuteProcedure,
    procedureName=
        safe_text
)
jcl_statements_ExecuteProgram_strategy = st.builds(
    jcl_statements_ExecuteProgram,
    programName=
        safe_text
)
EndControl_strategy = st.builds(
    EndControl,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
statements_StatementContainer_strategy = st.builds(
    statements_StatementContainer,
)
jcl_statements_Condition_strategy = st.builds(
    jcl_statements_Condition,
    endName=
        safe_text,
    elseName=
        safe_text
)
jcl_statements_StatementContainer_strategy = st.builds(
    jcl_statements_StatementContainer,
)
Statement_strategy = st.builds(
    Statement,
)
jcl_statements_Output_strategy = st.builds(
    jcl_statements_Output,
)
jcl_statements_EndControl_strategy = st.builds(
    jcl_statements_EndControl,
)
jcl_statements_Command_strategy = st.builds(
    jcl_statements_Command,
    value=
        safe_text
)
jcl_statements_JCLLibrary_strategy = st.builds(
    jcl_statements_JCLLibrary,
)
jcl_statements_Set_strategy = st.builds(
    jcl_statements_Set,
)
jcl_statements_Input_strategy = st.builds(
    jcl_statements_Input,
)
jcl_statements_Include_strategy = st.builds(
    jcl_statements_Include,
)
jcl_statements_Control_strategy = st.builds(
    jcl_statements_Control,
    endName=
        safe_text
)
jcl_statements_Execute_strategy = st.builds(
    jcl_statements_Execute,
)
members_Member_strategy = st.builds(
    members_Member,
)
commons_NamedElement_strategy = st.builds(
    commons_NamedElement,
)
jcl_procedures_Procedure_strategy = st.builds(
    jcl_procedures_Procedure,
    endName=
        safe_text
)
jcl_statements_Statement_strategy = st.builds(
    jcl_statements_Statement,
)
jcl_containers_JobUnit_strategy = st.builds(
    jcl_containers_JobUnit,
)
Condition_strategy = st.builds(
    Condition,
)
jcl_conditions_PrimaryCondition_strategy = st.builds(
    jcl_conditions_PrimaryCondition,
)
Literal_strategy = st.builds(
    Literal,
)
jcl_literals_SpecialLiteral_strategy = st.builds(
    jcl_literals_SpecialLiteral,
    value=
        safe_text
)
jcl_literals_StringLiteral_strategy = st.builds(
    jcl_literals_StringLiteral,
    value=
        safe_text
)
jcl_commons_ProcedureStepElement_strategy = st.builds(
    jcl_commons_ProcedureStepElement,
    procStepName=
        safe_text
)
commons_ProcedureStepElement_strategy = st.builds(
    commons_ProcedureStepElement,
)
jcl_expressions_Run_strategy = st.builds(
    jcl_expressions_Run,
)
jcl_expressions_Abend_strategy = st.builds(
    jcl_expressions_Abend,
)
jcl_statements_DataDefinition_strategy = st.builds(
    jcl_statements_DataDefinition,
)
parameters_Parameter_strategy = st.builds(
    parameters_Parameter,
)
jcl_parameters_Other_strategy = st.builds(
    jcl_parameters_Other,
    value=
        safe_text
)
jcl_parameters_Condition_strategy = st.builds(
    jcl_parameters_Condition,
)
jcl_parameters_AccountInfo_strategy = st.builds(
    jcl_parameters_AccountInfo,
)
jcl_parameters_Argument_strategy = st.builds(
    jcl_parameters_Argument,
    value=
        safe_text
)
jcl_parameters_AddressSpace_strategy = st.builds(
    jcl_parameters_AddressSpace,
    value=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
jcl_parameters_TypeRun_strategy = st.builds(
    jcl_parameters_TypeRun,
    value=
        safe_text
)
jcl_parameters_JobClass_strategy = st.builds(
    jcl_parameters_JobClass,
    value=
        st.integers()
)
jcl_parameters_UserID_strategy = st.builds(
    jcl_parameters_UserID,
    value=
        safe_text
)
jcl_parameters_Bytes_strategy = st.builds(
    jcl_parameters_Bytes,
    value=
        st.integers()
)
jcl_parameters_Priority_strategy = st.builds(
    jcl_parameters_Priority,
    value=
        st.integers()
)
jcl_parameters_DatasetName_strategy = st.builds(
    jcl_parameters_DatasetName,
    value=
        safe_text
)
jcl_parameters_Password_strategy = st.builds(
    jcl_parameters_Password,
    new=
        safe_text,
    old=
        safe_text
)
jcl_parameters_MessageLevel_strategy = st.builds(
    jcl_parameters_MessageLevel,
    statements=
        st.integers(),
    messages=
        st.integers()
)
jcl_parameters_MessageClass_strategy = st.builds(
    jcl_parameters_MessageClass,
    value=
        safe_text
)
jcl_parameters_Display_strategy = st.builds(
    jcl_parameters_Display,
    value=
        safe_text
)
jcl_parameters_Parameter_strategy = st.builds(
    jcl_parameters_Parameter,
)
Water_strategy = st.builds(
    Water,
)
jcl_commons_IncompleteElement_strategy = st.builds(
    jcl_commons_IncompleteElement,
)
jcl_commons_CommentableElement_strategy = st.builds(
    jcl_commons_CommentableElement,
    comment=
        safe_text
)
jcl_commons_PhraseableElement_strategy = st.builds(
    jcl_commons_PhraseableElement,
    isPhrase=
        st.booleans()
)
jcl_commons_NamedElement_strategy = st.builds(
    jcl_commons_NamedElement,
    name=
        safe_text
)

@given(instance=jcl_waters_Water_strategy)
@settings(max_examples=50)
def test_jcl_waters_water_instantiation(instance):
    assert isinstance(instance, jcl_waters_Water)



@given(instance=jcl_waters_Water_strategy)
def test_jcl_waters_water_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_members_Member_strategy)
@settings(max_examples=50)
def test_jcl_members_member_instantiation(instance):
    assert isinstance(instance, jcl_members_Member)

@given(instance=jcl_conditions_ReturnCode_strategy)
@settings(max_examples=50)
def test_jcl_conditions_returncode_instantiation(instance):
    assert isinstance(instance, jcl_conditions_ReturnCode)

@given(instance=ReturnCode_strategy)
@settings(max_examples=50)
def test_returncode_instantiation(instance):
    assert isinstance(instance, ReturnCode)

@given(instance=conditions_PrimaryCondition_strategy)
@settings(max_examples=50)
def test_conditions_primarycondition_instantiation(instance):
    assert isinstance(instance, conditions_PrimaryCondition)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=jcl_operators_UnaryOperator_strategy)
@settings(max_examples=50)
def test_jcl_operators_unaryoperator_instantiation(instance):
    assert isinstance(instance, jcl_operators_UnaryOperator)

@given(instance=PrimaryCondition_strategy)
@settings(max_examples=50)
def test_primarycondition_instantiation(instance):
    assert isinstance(instance, PrimaryCondition)

@given(instance=jcl_conditions_Only_strategy)
@settings(max_examples=50)
def test_jcl_conditions_only_instantiation(instance):
    assert isinstance(instance, jcl_conditions_Only)

@given(instance=jcl_conditions_NestedCondition_strategy)
@settings(max_examples=50)
def test_jcl_conditions_nestedcondition_instantiation(instance):
    assert isinstance(instance, jcl_conditions_NestedCondition)

@given(instance=jcl_conditions_Even_strategy)
@settings(max_examples=50)
def test_jcl_conditions_even_instantiation(instance):
    assert isinstance(instance, jcl_conditions_Even)

@given(instance=jcl_conditions_Condition_strategy)
@settings(max_examples=50)
def test_jcl_conditions_condition_instantiation(instance):
    assert isinstance(instance, jcl_conditions_Condition)

@given(instance=jcl_references_ReferenceableElement_strategy)
@settings(max_examples=50)
def test_jcl_references_referenceableelement_instantiation(instance):
    assert isinstance(instance, jcl_references_ReferenceableElement)

@given(instance=references_ElementReference_strategy)
@settings(max_examples=50)
def test_references_elementreference_instantiation(instance):
    assert isinstance(instance, references_ElementReference)

@given(instance=jcl_conditions_RelationalCondition_strategy)
@settings(max_examples=50)
def test_jcl_conditions_relationalcondition_instantiation(instance):
    assert isinstance(instance, jcl_conditions_RelationalCondition)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=jcl_references_ElementReference_strategy)
@settings(max_examples=50)
def test_jcl_references_elementreference_instantiation(instance):
    assert isinstance(instance, jcl_references_ElementReference)

@given(instance=jcl_references_Reference_strategy)
@settings(max_examples=50)
def test_jcl_references_reference_instantiation(instance):
    assert isinstance(instance, jcl_references_Reference)

@given(instance=conditions_ReturnCode_strategy)
@settings(max_examples=50)
def test_conditions_returncode_instantiation(instance):
    assert isinstance(instance, conditions_ReturnCode)

@given(instance=literals_Literal_strategy)
@settings(max_examples=50)
def test_literals_literal_instantiation(instance):
    assert isinstance(instance, literals_Literal)

@given(instance=jcl_literals_Literal_strategy)
@settings(max_examples=50)
def test_jcl_literals_literal_instantiation(instance):
    assert isinstance(instance, jcl_literals_Literal)

@given(instance=LogicOperator_strategy)
@settings(max_examples=50)
def test_logicoperator_instantiation(instance):
    assert isinstance(instance, LogicOperator)

@given(instance=jcl_operators_Or_strategy)
@settings(max_examples=50)
def test_jcl_operators_or_instantiation(instance):
    assert isinstance(instance, jcl_operators_Or)

@given(instance=jcl_operators_And_strategy)
@settings(max_examples=50)
def test_jcl_operators_and_instantiation(instance):
    assert isinstance(instance, jcl_operators_And)

@given(instance=jcl_operators_LogicOperator_strategy)
@settings(max_examples=50)
def test_jcl_operators_logicoperator_instantiation(instance):
    assert isinstance(instance, jcl_operators_LogicOperator)

@given(instance=jcl_operators_RelationOperator_strategy)
@settings(max_examples=50)
def test_jcl_operators_relationoperator_instantiation(instance):
    assert isinstance(instance, jcl_operators_RelationOperator)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=jcl_operators_Negate_strategy)
@settings(max_examples=50)
def test_jcl_operators_negate_instantiation(instance):
    assert isinstance(instance, jcl_operators_Negate)

@given(instance=PhraseableElement_strategy)
@settings(max_examples=50)
def test_phraseableelement_instantiation(instance):
    assert isinstance(instance, PhraseableElement)

@given(instance=jcl_operators_Operator_strategy)
@settings(max_examples=50)
def test_jcl_operators_operator_instantiation(instance):
    assert isinstance(instance, jcl_operators_Operator)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=expressions_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_expressions_primaryexpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryExpression)

@given(instance=jcl_references_IdentifierReference_strategy)
@settings(max_examples=50)
def test_jcl_references_identifierreference_instantiation(instance):
    assert isinstance(instance, jcl_references_IdentifierReference)

@given(instance=jcl_literals_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_jcl_literals_integerliteral_instantiation(instance):
    assert isinstance(instance, jcl_literals_IntegerLiteral)



@given(instance=jcl_literals_IntegerLiteral_strategy)
def test_jcl_literals_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=jcl_expressions_NestedExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_nestedexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_NestedExpression)

@given(instance=RelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_relationalexpressionchild_instantiation(instance):
    assert isinstance(instance, RelationalExpressionChild)

@given(instance=UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryExpressionChild)

@given(instance=jcl_expressions_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_primaryexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_PrimaryExpression)

@given(instance=jcl_expressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_UnaryExpression)

@given(instance=jcl_expressions_UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_jcl_expressions_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, jcl_expressions_UnaryExpressionChild)

@given(instance=And_strategy)
@settings(max_examples=50)
def test_and_instantiation(instance):
    assert isinstance(instance, And)

@given(instance=Or_strategy)
@settings(max_examples=50)
def test_or_instantiation(instance):
    assert isinstance(instance, Or)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=jcl_expressions_ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_jcl_expressions_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, jcl_expressions_ConditionalAndExpressionChild)

@given(instance=jcl_expressions_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_ConditionalAndExpression)

@given(instance=ConditionalExpression_strategy)
@settings(max_examples=50)
def test_conditionalexpression_instantiation(instance):
    assert isinstance(instance, ConditionalExpression)

@given(instance=jcl_expressions_ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_jcl_expressions_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, jcl_expressions_ConditionalOrExpressionChild)

@given(instance=jcl_expressions_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_ConditionalOrExpression)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=jcl_operators_NotEqual_strategy)
@settings(max_examples=50)
def test_jcl_operators_notequal_instantiation(instance):
    assert isinstance(instance, jcl_operators_NotEqual)

@given(instance=jcl_operators_LessThan_strategy)
@settings(max_examples=50)
def test_jcl_operators_lessthan_instantiation(instance):
    assert isinstance(instance, jcl_operators_LessThan)

@given(instance=jcl_operators_GreaterEqual_strategy)
@settings(max_examples=50)
def test_jcl_operators_greaterequal_instantiation(instance):
    assert isinstance(instance, jcl_operators_GreaterEqual)

@given(instance=jcl_operators_Equal_strategy)
@settings(max_examples=50)
def test_jcl_operators_equal_instantiation(instance):
    assert isinstance(instance, jcl_operators_Equal)

@given(instance=jcl_operators_LessEqual_strategy)
@settings(max_examples=50)
def test_jcl_operators_lessequal_instantiation(instance):
    assert isinstance(instance, jcl_operators_LessEqual)

@given(instance=jcl_operators_GreaterThan_strategy)
@settings(max_examples=50)
def test_jcl_operators_greaterthan_instantiation(instance):
    assert isinstance(instance, jcl_operators_GreaterThan)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=jcl_expressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_ConditionalExpression)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=jcl_expressions_RelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_jcl_expressions_relationalexpressionchild_instantiation(instance):
    assert isinstance(instance, jcl_expressions_RelationalExpressionChild)

@given(instance=jcl_expressions_RelationalExpression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_relationalexpression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_RelationalExpression)

@given(instance=jcl_expressions_Expression_strategy)
@settings(max_examples=50)
def test_jcl_expressions_expression_instantiation(instance):
    assert isinstance(instance, jcl_expressions_Expression)

@given(instance=ExecuteProgram_strategy)
@settings(max_examples=50)
def test_executeprogram_instantiation(instance):
    assert isinstance(instance, ExecuteProgram)

@given(instance=commons_IncompleteElement_strategy)
@settings(max_examples=50)
def test_commons_incompleteelement_instantiation(instance):
    assert isinstance(instance, commons_IncompleteElement)

@given(instance=containers_JCLRoot_strategy)
@settings(max_examples=50)
def test_containers_jclroot_instantiation(instance):
    assert isinstance(instance, containers_JCLRoot)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=jcl_containers_JCLRoot_strategy)
@settings(max_examples=50)
def test_jcl_containers_jclroot_instantiation(instance):
    assert isinstance(instance, jcl_containers_JCLRoot)

@given(instance=Execute_strategy)
@settings(max_examples=50)
def test_execute_instantiation(instance):
    assert isinstance(instance, Execute)

@given(instance=jcl_statements_ExecuteProcedure_strategy)
@settings(max_examples=50)
def test_jcl_statements_executeprocedure_instantiation(instance):
    assert isinstance(instance, jcl_statements_ExecuteProcedure)



@given(instance=jcl_statements_ExecuteProcedure_strategy)
def test_jcl_statements_executeprocedure_procedureName_setter(instance):
    original = instance.procedureName
    instance.procedureName = original
    assert instance.procedureName == original

@given(instance=jcl_statements_ExecuteProgram_strategy)
@settings(max_examples=50)
def test_jcl_statements_executeprogram_instantiation(instance):
    assert isinstance(instance, jcl_statements_ExecuteProgram)



@given(instance=jcl_statements_ExecuteProgram_strategy)
def test_jcl_statements_executeprogram_programName_setter(instance):
    original = instance.programName
    instance.programName = original
    assert instance.programName == original

@given(instance=EndControl_strategy)
@settings(max_examples=50)
def test_endcontrol_instantiation(instance):
    assert isinstance(instance, EndControl)

@given(instance=statements_Statement_strategy)
@settings(max_examples=50)
def test_statements_statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)

@given(instance=statements_StatementContainer_strategy)
@settings(max_examples=50)
def test_statements_statementcontainer_instantiation(instance):
    assert isinstance(instance, statements_StatementContainer)

@given(instance=jcl_statements_Condition_strategy)
@settings(max_examples=50)
def test_jcl_statements_condition_instantiation(instance):
    assert isinstance(instance, jcl_statements_Condition)



@given(instance=jcl_statements_Condition_strategy)
def test_jcl_statements_condition_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original



@given(instance=jcl_statements_Condition_strategy)
def test_jcl_statements_condition_elseName_setter(instance):
    original = instance.elseName
    instance.elseName = original
    assert instance.elseName == original

@given(instance=jcl_statements_StatementContainer_strategy)
@settings(max_examples=50)
def test_jcl_statements_statementcontainer_instantiation(instance):
    assert isinstance(instance, jcl_statements_StatementContainer)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=jcl_statements_Output_strategy)
@settings(max_examples=50)
def test_jcl_statements_output_instantiation(instance):
    assert isinstance(instance, jcl_statements_Output)

@given(instance=jcl_statements_EndControl_strategy)
@settings(max_examples=50)
def test_jcl_statements_endcontrol_instantiation(instance):
    assert isinstance(instance, jcl_statements_EndControl)

@given(instance=jcl_statements_Command_strategy)
@settings(max_examples=50)
def test_jcl_statements_command_instantiation(instance):
    assert isinstance(instance, jcl_statements_Command)



@given(instance=jcl_statements_Command_strategy)
def test_jcl_statements_command_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_statements_JCLLibrary_strategy)
@settings(max_examples=50)
def test_jcl_statements_jcllibrary_instantiation(instance):
    assert isinstance(instance, jcl_statements_JCLLibrary)

@given(instance=jcl_statements_Set_strategy)
@settings(max_examples=50)
def test_jcl_statements_set_instantiation(instance):
    assert isinstance(instance, jcl_statements_Set)

@given(instance=jcl_statements_Input_strategy)
@settings(max_examples=50)
def test_jcl_statements_input_instantiation(instance):
    assert isinstance(instance, jcl_statements_Input)

@given(instance=jcl_statements_Include_strategy)
@settings(max_examples=50)
def test_jcl_statements_include_instantiation(instance):
    assert isinstance(instance, jcl_statements_Include)

@given(instance=jcl_statements_Control_strategy)
@settings(max_examples=50)
def test_jcl_statements_control_instantiation(instance):
    assert isinstance(instance, jcl_statements_Control)



@given(instance=jcl_statements_Control_strategy)
def test_jcl_statements_control_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original

@given(instance=jcl_statements_Execute_strategy)
@settings(max_examples=50)
def test_jcl_statements_execute_instantiation(instance):
    assert isinstance(instance, jcl_statements_Execute)

@given(instance=members_Member_strategy)
@settings(max_examples=50)
def test_members_member_instantiation(instance):
    assert isinstance(instance, members_Member)

@given(instance=commons_NamedElement_strategy)
@settings(max_examples=50)
def test_commons_namedelement_instantiation(instance):
    assert isinstance(instance, commons_NamedElement)

@given(instance=jcl_procedures_Procedure_strategy)
@settings(max_examples=50)
def test_jcl_procedures_procedure_instantiation(instance):
    assert isinstance(instance, jcl_procedures_Procedure)



@given(instance=jcl_procedures_Procedure_strategy)
def test_jcl_procedures_procedure_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original

@given(instance=jcl_statements_Statement_strategy)
@settings(max_examples=50)
def test_jcl_statements_statement_instantiation(instance):
    assert isinstance(instance, jcl_statements_Statement)

@given(instance=jcl_containers_JobUnit_strategy)
@settings(max_examples=50)
def test_jcl_containers_jobunit_instantiation(instance):
    assert isinstance(instance, jcl_containers_JobUnit)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=jcl_conditions_PrimaryCondition_strategy)
@settings(max_examples=50)
def test_jcl_conditions_primarycondition_instantiation(instance):
    assert isinstance(instance, jcl_conditions_PrimaryCondition)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=jcl_literals_SpecialLiteral_strategy)
@settings(max_examples=50)
def test_jcl_literals_specialliteral_instantiation(instance):
    assert isinstance(instance, jcl_literals_SpecialLiteral)



@given(instance=jcl_literals_SpecialLiteral_strategy)
def test_jcl_literals_specialliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_literals_StringLiteral_strategy)
@settings(max_examples=50)
def test_jcl_literals_stringliteral_instantiation(instance):
    assert isinstance(instance, jcl_literals_StringLiteral)



@given(instance=jcl_literals_StringLiteral_strategy)
def test_jcl_literals_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_commons_ProcedureStepElement_strategy)
@settings(max_examples=50)
def test_jcl_commons_procedurestepelement_instantiation(instance):
    assert isinstance(instance, jcl_commons_ProcedureStepElement)



@given(instance=jcl_commons_ProcedureStepElement_strategy)
def test_jcl_commons_procedurestepelement_procStepName_setter(instance):
    original = instance.procStepName
    instance.procStepName = original
    assert instance.procStepName == original

@given(instance=commons_ProcedureStepElement_strategy)
@settings(max_examples=50)
def test_commons_procedurestepelement_instantiation(instance):
    assert isinstance(instance, commons_ProcedureStepElement)

@given(instance=jcl_expressions_Run_strategy)
@settings(max_examples=50)
def test_jcl_expressions_run_instantiation(instance):
    assert isinstance(instance, jcl_expressions_Run)

@given(instance=jcl_expressions_Abend_strategy)
@settings(max_examples=50)
def test_jcl_expressions_abend_instantiation(instance):
    assert isinstance(instance, jcl_expressions_Abend)

@given(instance=jcl_statements_DataDefinition_strategy)
@settings(max_examples=50)
def test_jcl_statements_datadefinition_instantiation(instance):
    assert isinstance(instance, jcl_statements_DataDefinition)

@given(instance=parameters_Parameter_strategy)
@settings(max_examples=50)
def test_parameters_parameter_instantiation(instance):
    assert isinstance(instance, parameters_Parameter)

@given(instance=jcl_parameters_Other_strategy)
@settings(max_examples=50)
def test_jcl_parameters_other_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Other)



@given(instance=jcl_parameters_Other_strategy)
def test_jcl_parameters_other_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_Condition_strategy)
@settings(max_examples=50)
def test_jcl_parameters_condition_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Condition)

@given(instance=jcl_parameters_AccountInfo_strategy)
@settings(max_examples=50)
def test_jcl_parameters_accountinfo_instantiation(instance):
    assert isinstance(instance, jcl_parameters_AccountInfo)

@given(instance=jcl_parameters_Argument_strategy)
@settings(max_examples=50)
def test_jcl_parameters_argument_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Argument)



@given(instance=jcl_parameters_Argument_strategy)
def test_jcl_parameters_argument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_AddressSpace_strategy)
@settings(max_examples=50)
def test_jcl_parameters_addressspace_instantiation(instance):
    assert isinstance(instance, jcl_parameters_AddressSpace)



@given(instance=jcl_parameters_AddressSpace_strategy)
def test_jcl_parameters_addressspace_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=jcl_parameters_TypeRun_strategy)
@settings(max_examples=50)
def test_jcl_parameters_typerun_instantiation(instance):
    assert isinstance(instance, jcl_parameters_TypeRun)



@given(instance=jcl_parameters_TypeRun_strategy)
def test_jcl_parameters_typerun_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_JobClass_strategy)
@settings(max_examples=50)
def test_jcl_parameters_jobclass_instantiation(instance):
    assert isinstance(instance, jcl_parameters_JobClass)



@given(instance=jcl_parameters_JobClass_strategy)
def test_jcl_parameters_jobclass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_UserID_strategy)
@settings(max_examples=50)
def test_jcl_parameters_userid_instantiation(instance):
    assert isinstance(instance, jcl_parameters_UserID)



@given(instance=jcl_parameters_UserID_strategy)
def test_jcl_parameters_userid_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_Bytes_strategy)
@settings(max_examples=50)
def test_jcl_parameters_bytes_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Bytes)



@given(instance=jcl_parameters_Bytes_strategy)
def test_jcl_parameters_bytes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_Priority_strategy)
@settings(max_examples=50)
def test_jcl_parameters_priority_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Priority)



@given(instance=jcl_parameters_Priority_strategy)
def test_jcl_parameters_priority_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_DatasetName_strategy)
@settings(max_examples=50)
def test_jcl_parameters_datasetname_instantiation(instance):
    assert isinstance(instance, jcl_parameters_DatasetName)



@given(instance=jcl_parameters_DatasetName_strategy)
def test_jcl_parameters_datasetname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_Password_strategy)
@settings(max_examples=50)
def test_jcl_parameters_password_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Password)



@given(instance=jcl_parameters_Password_strategy)
def test_jcl_parameters_password_new_setter(instance):
    original = instance.new
    instance.new = original
    assert instance.new == original



@given(instance=jcl_parameters_Password_strategy)
def test_jcl_parameters_password_old_setter(instance):
    original = instance.old
    instance.old = original
    assert instance.old == original

@given(instance=jcl_parameters_MessageLevel_strategy)
@settings(max_examples=50)
def test_jcl_parameters_messagelevel_instantiation(instance):
    assert isinstance(instance, jcl_parameters_MessageLevel)



@given(instance=jcl_parameters_MessageLevel_strategy)
def test_jcl_parameters_messagelevel_statements_setter(instance):
    original = instance.statements
    instance.statements = original
    assert instance.statements == original



@given(instance=jcl_parameters_MessageLevel_strategy)
def test_jcl_parameters_messagelevel_messages_setter(instance):
    original = instance.messages
    instance.messages = original
    assert instance.messages == original

@given(instance=jcl_parameters_MessageClass_strategy)
@settings(max_examples=50)
def test_jcl_parameters_messageclass_instantiation(instance):
    assert isinstance(instance, jcl_parameters_MessageClass)



@given(instance=jcl_parameters_MessageClass_strategy)
def test_jcl_parameters_messageclass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_Display_strategy)
@settings(max_examples=50)
def test_jcl_parameters_display_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Display)



@given(instance=jcl_parameters_Display_strategy)
def test_jcl_parameters_display_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jcl_parameters_Parameter_strategy)
@settings(max_examples=50)
def test_jcl_parameters_parameter_instantiation(instance):
    assert isinstance(instance, jcl_parameters_Parameter)

@given(instance=Water_strategy)
@settings(max_examples=50)
def test_water_instantiation(instance):
    assert isinstance(instance, Water)

@given(instance=jcl_commons_IncompleteElement_strategy)
@settings(max_examples=50)
def test_jcl_commons_incompleteelement_instantiation(instance):
    assert isinstance(instance, jcl_commons_IncompleteElement)

@given(instance=jcl_commons_CommentableElement_strategy)
@settings(max_examples=50)
def test_jcl_commons_commentableelement_instantiation(instance):
    assert isinstance(instance, jcl_commons_CommentableElement)



@given(instance=jcl_commons_CommentableElement_strategy)
def test_jcl_commons_commentableelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=jcl_commons_PhraseableElement_strategy)
@settings(max_examples=50)
def test_jcl_commons_phraseableelement_instantiation(instance):
    assert isinstance(instance, jcl_commons_PhraseableElement)



@given(instance=jcl_commons_PhraseableElement_strategy)
def test_jcl_commons_phraseableelement_isPhrase_setter(instance):
    original = instance.isPhrase
    instance.isPhrase = original
    assert instance.isPhrase == original

@given(instance=jcl_commons_NamedElement_strategy)
@settings(max_examples=50)
def test_jcl_commons_namedelement_instantiation(instance):
    assert isinstance(instance, jcl_commons_NamedElement)



@given(instance=jcl_commons_NamedElement_strategy)
def test_jcl_commons_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
