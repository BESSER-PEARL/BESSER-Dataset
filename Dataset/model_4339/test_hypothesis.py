import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    expression_Procedure,
    expression_ProcedureCall,
    expression_ExpressionList,
    Function,
    Expression,
    expression_Sum,
    expression_PowExpression,
    expression_LastIn,
    expression_Apply,
    expression_EqualityExpression,
    expression_ThereIsIn,
    expression_PointExpression,
    expression_FirstIn,
    expression_ForallIn,
    expression_Count,
    expression_UnaryExpression,
    expression_StructureExpression,
    expression_DashExpression,
    expression_AndExpression,
    expression_QualifierExpression,
    expression_Map,
    expression_Reduce,
    expression_FunctionCall,
    ExpressionRest,
    expression_OrExpression,
    expression_EObject,
    Term,
    expression_IntegerValue,
    expression_StringValue,
    expression_DoubleValue,
    expression_List,
    expression_Term,
    expression_KeyValuePairRest,
    KeyValuePairRest,
    expression_KeyValuePair,
    expression_ExpressionRest,
    Phrase,
    expression_StatementList,
    expression_Phrase,
    expression_Model,
    expression_Designator,
    AssignmentStatement,
    expression_SelfAssignmentStatement,
    expression_VariableAssignmentStatement,
    expression_Expression,
    Statement,
    expression_AssignmentStatement,
    expression_Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_procedure_is_not_abstract():
    assert not inspect.isabstract(expression_Procedure)


def test_expression_procedure_constructor_exists():
    assert callable(expression_Procedure.__init__)


def test_expression_procedure_constructor_args():
    sig = inspect.signature(expression_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_expression_procedurecall_is_not_abstract():
    assert not inspect.isabstract(expression_ProcedureCall)


def test_expression_procedurecall_constructor_exists():
    assert callable(expression_ProcedureCall.__init__)


def test_expression_procedurecall_constructor_args():
    sig = inspect.signature(expression_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expression_expressionlist_is_not_abstract():
    assert not inspect.isabstract(expression_ExpressionList)


def test_expression_expressionlist_constructor_exists():
    assert callable(expression_ExpressionList.__init__)


def test_expression_expressionlist_constructor_args():
    sig = inspect.signature(expression_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_sum_is_not_abstract():
    assert not inspect.isabstract(expression_Sum)


def test_expression_sum_constructor_exists():
    assert callable(expression_Sum.__init__)


def test_expression_sum_constructor_args():
    sig = inspect.signature(expression_Sum.__init__)
    params = list(sig.parameters.keys())



def test_expression_powexpression_is_not_abstract():
    assert not inspect.isabstract(expression_PowExpression)


def test_expression_powexpression_constructor_exists():
    assert callable(expression_PowExpression.__init__)


def test_expression_powexpression_constructor_args():
    sig = inspect.signature(expression_PowExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_powexpression_has_op():
    assert hasattr(expression_PowExpression, "op")
    descriptor = None
    for klass in expression_PowExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_lastin_is_not_abstract():
    assert not inspect.isabstract(expression_LastIn)


def test_expression_lastin_constructor_exists():
    assert callable(expression_LastIn.__init__)


def test_expression_lastin_constructor_args():
    sig = inspect.signature(expression_LastIn.__init__)
    params = list(sig.parameters.keys())



def test_expression_apply_is_not_abstract():
    assert not inspect.isabstract(expression_Apply)


def test_expression_apply_constructor_exists():
    assert callable(expression_Apply.__init__)


def test_expression_apply_constructor_args():
    sig = inspect.signature(expression_Apply.__init__)
    params = list(sig.parameters.keys())



def test_expression_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(expression_EqualityExpression)


def test_expression_equalityexpression_constructor_exists():
    assert callable(expression_EqualityExpression.__init__)


def test_expression_equalityexpression_constructor_args():
    sig = inspect.signature(expression_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_equalityexpression_has_op():
    assert hasattr(expression_EqualityExpression, "op")
    descriptor = None
    for klass in expression_EqualityExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_thereisin_is_not_abstract():
    assert not inspect.isabstract(expression_ThereIsIn)


def test_expression_thereisin_constructor_exists():
    assert callable(expression_ThereIsIn.__init__)


def test_expression_thereisin_constructor_args():
    sig = inspect.signature(expression_ThereIsIn.__init__)
    params = list(sig.parameters.keys())



def test_expression_pointexpression_is_not_abstract():
    assert not inspect.isabstract(expression_PointExpression)


def test_expression_pointexpression_constructor_exists():
    assert callable(expression_PointExpression.__init__)


def test_expression_pointexpression_constructor_args():
    sig = inspect.signature(expression_PointExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_pointexpression_has_op():
    assert hasattr(expression_PointExpression, "op")
    descriptor = None
    for klass in expression_PointExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_firstin_is_not_abstract():
    assert not inspect.isabstract(expression_FirstIn)


def test_expression_firstin_constructor_exists():
    assert callable(expression_FirstIn.__init__)


def test_expression_firstin_constructor_args():
    sig = inspect.signature(expression_FirstIn.__init__)
    params = list(sig.parameters.keys())



def test_expression_forallin_is_not_abstract():
    assert not inspect.isabstract(expression_ForallIn)


def test_expression_forallin_constructor_exists():
    assert callable(expression_ForallIn.__init__)


def test_expression_forallin_constructor_args():
    sig = inspect.signature(expression_ForallIn.__init__)
    params = list(sig.parameters.keys())



def test_expression_count_is_not_abstract():
    assert not inspect.isabstract(expression_Count)


def test_expression_count_constructor_exists():
    assert callable(expression_Count.__init__)


def test_expression_count_constructor_args():
    sig = inspect.signature(expression_Count.__init__)
    params = list(sig.parameters.keys())



def test_expression_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression_UnaryExpression)


def test_expression_unaryexpression_constructor_exists():
    assert callable(expression_UnaryExpression.__init__)


def test_expression_unaryexpression_constructor_args():
    sig = inspect.signature(expression_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_structureexpression_is_not_abstract():
    assert not inspect.isabstract(expression_StructureExpression)


def test_expression_structureexpression_constructor_exists():
    assert callable(expression_StructureExpression.__init__)


def test_expression_structureexpression_constructor_args():
    sig = inspect.signature(expression_StructureExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_dashexpression_is_not_abstract():
    assert not inspect.isabstract(expression_DashExpression)


def test_expression_dashexpression_constructor_exists():
    assert callable(expression_DashExpression.__init__)


def test_expression_dashexpression_constructor_args():
    sig = inspect.signature(expression_DashExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_dashexpression_has_op():
    assert hasattr(expression_DashExpression, "op")
    descriptor = None
    for klass in expression_DashExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_andexpression_is_not_abstract():
    assert not inspect.isabstract(expression_AndExpression)


def test_expression_andexpression_constructor_exists():
    assert callable(expression_AndExpression.__init__)


def test_expression_andexpression_constructor_args():
    sig = inspect.signature(expression_AndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_andexpression_has_op():
    assert hasattr(expression_AndExpression, "op")
    descriptor = None
    for klass in expression_AndExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_qualifierexpression_is_not_abstract():
    assert not inspect.isabstract(expression_QualifierExpression)


def test_expression_qualifierexpression_constructor_exists():
    assert callable(expression_QualifierExpression.__init__)


def test_expression_qualifierexpression_constructor_args():
    sig = inspect.signature(expression_QualifierExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_qualifierexpression_has_op():
    assert hasattr(expression_QualifierExpression, "op")
    descriptor = None
    for klass in expression_QualifierExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_map_is_not_abstract():
    assert not inspect.isabstract(expression_Map)


def test_expression_map_constructor_exists():
    assert callable(expression_Map.__init__)


def test_expression_map_constructor_args():
    sig = inspect.signature(expression_Map.__init__)
    params = list(sig.parameters.keys())



def test_expression_reduce_is_not_abstract():
    assert not inspect.isabstract(expression_Reduce)


def test_expression_reduce_constructor_exists():
    assert callable(expression_Reduce.__init__)


def test_expression_reduce_constructor_args():
    sig = inspect.signature(expression_Reduce.__init__)
    params = list(sig.parameters.keys())



def test_expression_functioncall_is_not_abstract():
    assert not inspect.isabstract(expression_FunctionCall)


def test_expression_functioncall_constructor_exists():
    assert callable(expression_FunctionCall.__init__)


def test_expression_functioncall_constructor_args():
    sig = inspect.signature(expression_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionrest_is_not_abstract():
    assert not inspect.isabstract(ExpressionRest)


def test_expressionrest_constructor_exists():
    assert callable(ExpressionRest.__init__)


def test_expressionrest_constructor_args():
    sig = inspect.signature(ExpressionRest.__init__)
    params = list(sig.parameters.keys())



def test_expression_orexpression_is_not_abstract():
    assert not inspect.isabstract(expression_OrExpression)


def test_expression_orexpression_constructor_exists():
    assert callable(expression_OrExpression.__init__)


def test_expression_orexpression_constructor_args():
    sig = inspect.signature(expression_OrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_orexpression_has_op():
    assert hasattr(expression_OrExpression, "op")
    descriptor = None
    for klass in expression_OrExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_eobject_is_not_abstract():
    assert not inspect.isabstract(expression_EObject)


def test_expression_eobject_constructor_exists():
    assert callable(expression_EObject.__init__)


def test_expression_eobject_constructor_args():
    sig = inspect.signature(expression_EObject.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_expression_integervalue_is_not_abstract():
    assert not inspect.isabstract(expression_IntegerValue)


def test_expression_integervalue_constructor_exists():
    assert callable(expression_IntegerValue.__init__)


def test_expression_integervalue_constructor_args():
    sig = inspect.signature(expression_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_integervalue_has_value():
    assert hasattr(expression_IntegerValue, "value")
    descriptor = None
    for klass in expression_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_stringvalue_is_not_abstract():
    assert not inspect.isabstract(expression_StringValue)


def test_expression_stringvalue_constructor_exists():
    assert callable(expression_StringValue.__init__)


def test_expression_stringvalue_constructor_args():
    sig = inspect.signature(expression_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_stringvalue_has_value():
    assert hasattr(expression_StringValue, "value")
    descriptor = None
    for klass in expression_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_doublevalue_is_not_abstract():
    assert not inspect.isabstract(expression_DoubleValue)


def test_expression_doublevalue_constructor_exists():
    assert callable(expression_DoubleValue.__init__)


def test_expression_doublevalue_constructor_args():
    sig = inspect.signature(expression_DoubleValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_doublevalue_has_value():
    assert hasattr(expression_DoubleValue, "value")
    descriptor = None
    for klass in expression_DoubleValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_list_is_not_abstract():
    assert not inspect.isabstract(expression_List)


def test_expression_list_constructor_exists():
    assert callable(expression_List.__init__)


def test_expression_list_constructor_args():
    sig = inspect.signature(expression_List.__init__)
    params = list(sig.parameters.keys())



def test_expression_term_is_not_abstract():
    assert not inspect.isabstract(expression_Term)


def test_expression_term_constructor_exists():
    assert callable(expression_Term.__init__)


def test_expression_term_constructor_args():
    sig = inspect.signature(expression_Term.__init__)
    params = list(sig.parameters.keys())



def test_expression_keyvaluepairrest_is_not_abstract():
    assert not inspect.isabstract(expression_KeyValuePairRest)


def test_expression_keyvaluepairrest_constructor_exists():
    assert callable(expression_KeyValuePairRest.__init__)


def test_expression_keyvaluepairrest_constructor_args():
    sig = inspect.signature(expression_KeyValuePairRest.__init__)
    params = list(sig.parameters.keys())



def test_keyvaluepairrest_is_not_abstract():
    assert not inspect.isabstract(KeyValuePairRest)


def test_keyvaluepairrest_constructor_exists():
    assert callable(KeyValuePairRest.__init__)


def test_keyvaluepairrest_constructor_args():
    sig = inspect.signature(KeyValuePairRest.__init__)
    params = list(sig.parameters.keys())



def test_expression_keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(expression_KeyValuePair)


def test_expression_keyvaluepair_constructor_exists():
    assert callable(expression_KeyValuePair.__init__)


def test_expression_keyvaluepair_constructor_args():
    sig = inspect.signature(expression_KeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_expression_keyvaluepair_has_key():
    assert hasattr(expression_KeyValuePair, "key")
    descriptor = None
    for klass in expression_KeyValuePair.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_expression_expressionrest_is_not_abstract():
    assert not inspect.isabstract(expression_ExpressionRest)


def test_expression_expressionrest_constructor_exists():
    assert callable(expression_ExpressionRest.__init__)


def test_expression_expressionrest_constructor_args():
    sig = inspect.signature(expression_ExpressionRest.__init__)
    params = list(sig.parameters.keys())



def test_phrase_is_not_abstract():
    assert not inspect.isabstract(Phrase)


def test_phrase_constructor_exists():
    assert callable(Phrase.__init__)


def test_phrase_constructor_args():
    sig = inspect.signature(Phrase.__init__)
    params = list(sig.parameters.keys())



def test_expression_statementlist_is_not_abstract():
    assert not inspect.isabstract(expression_StatementList)


def test_expression_statementlist_constructor_exists():
    assert callable(expression_StatementList.__init__)


def test_expression_statementlist_constructor_args():
    sig = inspect.signature(expression_StatementList.__init__)
    params = list(sig.parameters.keys())



def test_expression_phrase_is_not_abstract():
    assert not inspect.isabstract(expression_Phrase)


def test_expression_phrase_constructor_exists():
    assert callable(expression_Phrase.__init__)


def test_expression_phrase_constructor_args():
    sig = inspect.signature(expression_Phrase.__init__)
    params = list(sig.parameters.keys())



def test_expression_model_is_not_abstract():
    assert not inspect.isabstract(expression_Model)


def test_expression_model_constructor_exists():
    assert callable(expression_Model.__init__)


def test_expression_model_constructor_args():
    sig = inspect.signature(expression_Model.__init__)
    params = list(sig.parameters.keys())



def test_expression_designator_is_not_abstract():
    assert not inspect.isabstract(expression_Designator)


def test_expression_designator_constructor_exists():
    assert callable(expression_Designator.__init__)


def test_expression_designator_constructor_args():
    sig = inspect.signature(expression_Designator.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_selfassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(expression_SelfAssignmentStatement)


def test_expression_selfassignmentstatement_constructor_exists():
    assert callable(expression_SelfAssignmentStatement.__init__)


def test_expression_selfassignmentstatement_constructor_args():
    sig = inspect.signature(expression_SelfAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_variableassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(expression_VariableAssignmentStatement)


def test_expression_variableassignmentstatement_constructor_exists():
    assert callable(expression_VariableAssignmentStatement.__init__)


def test_expression_variableassignmentstatement_constructor_args():
    sig = inspect.signature(expression_VariableAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_expression_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(expression_AssignmentStatement)


def test_expression_assignmentstatement_constructor_exists():
    assert callable(expression_AssignmentStatement.__init__)


def test_expression_assignmentstatement_constructor_args():
    sig = inspect.signature(expression_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_statement_is_not_abstract():
    assert not inspect.isabstract(expression_Statement)


def test_expression_statement_constructor_exists():
    assert callable(expression_Statement.__init__)


def test_expression_statement_constructor_args():
    sig = inspect.signature(expression_Statement.__init__)
    params = list(sig.parameters.keys())


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
expression_Procedure_strategy = st.builds(
    expression_Procedure,
)
expression_ProcedureCall_strategy = st.builds(
    expression_ProcedureCall,
)
expression_ExpressionList_strategy = st.builds(
    expression_ExpressionList,
)
Function_strategy = st.builds(
    Function,
)
Expression_strategy = st.builds(
    Expression,
)
expression_Sum_strategy = st.builds(
    expression_Sum,
)
expression_PowExpression_strategy = st.builds(
    expression_PowExpression,
    op=
        safe_text
)
expression_LastIn_strategy = st.builds(
    expression_LastIn,
)
expression_Apply_strategy = st.builds(
    expression_Apply,
)
expression_EqualityExpression_strategy = st.builds(
    expression_EqualityExpression,
    op=
        safe_text
)
expression_ThereIsIn_strategy = st.builds(
    expression_ThereIsIn,
)
expression_PointExpression_strategy = st.builds(
    expression_PointExpression,
    op=
        safe_text
)
expression_FirstIn_strategy = st.builds(
    expression_FirstIn,
)
expression_ForallIn_strategy = st.builds(
    expression_ForallIn,
)
expression_Count_strategy = st.builds(
    expression_Count,
)
expression_UnaryExpression_strategy = st.builds(
    expression_UnaryExpression,
)
expression_StructureExpression_strategy = st.builds(
    expression_StructureExpression,
)
expression_DashExpression_strategy = st.builds(
    expression_DashExpression,
    op=
        safe_text
)
expression_AndExpression_strategy = st.builds(
    expression_AndExpression,
    op=
        safe_text
)
expression_QualifierExpression_strategy = st.builds(
    expression_QualifierExpression,
    op=
        safe_text
)
expression_Map_strategy = st.builds(
    expression_Map,
)
expression_Reduce_strategy = st.builds(
    expression_Reduce,
)
expression_FunctionCall_strategy = st.builds(
    expression_FunctionCall,
)
ExpressionRest_strategy = st.builds(
    ExpressionRest,
)
expression_OrExpression_strategy = st.builds(
    expression_OrExpression,
    op=
        safe_text
)
expression_EObject_strategy = st.builds(
    expression_EObject,
)
Term_strategy = st.builds(
    Term,
)
expression_IntegerValue_strategy = st.builds(
    expression_IntegerValue,
    value=
        st.integers()
)
expression_StringValue_strategy = st.builds(
    expression_StringValue,
    value=
        safe_text
)
expression_DoubleValue_strategy = st.builds(
    expression_DoubleValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expression_List_strategy = st.builds(
    expression_List,
)
expression_Term_strategy = st.builds(
    expression_Term,
)
expression_KeyValuePairRest_strategy = st.builds(
    expression_KeyValuePairRest,
)
KeyValuePairRest_strategy = st.builds(
    KeyValuePairRest,
)
expression_KeyValuePair_strategy = st.builds(
    expression_KeyValuePair,
    key=
        safe_text
)
expression_ExpressionRest_strategy = st.builds(
    expression_ExpressionRest,
)
Phrase_strategy = st.builds(
    Phrase,
)
expression_StatementList_strategy = st.builds(
    expression_StatementList,
)
expression_Phrase_strategy = st.builds(
    expression_Phrase,
)
expression_Model_strategy = st.builds(
    expression_Model,
)
expression_Designator_strategy = st.builds(
    expression_Designator,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
expression_SelfAssignmentStatement_strategy = st.builds(
    expression_SelfAssignmentStatement,
)
expression_VariableAssignmentStatement_strategy = st.builds(
    expression_VariableAssignmentStatement,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
expression_AssignmentStatement_strategy = st.builds(
    expression_AssignmentStatement,
)
expression_Statement_strategy = st.builds(
    expression_Statement,
)

@given(instance=expression_Procedure_strategy)
@settings(max_examples=50)
def test_expression_procedure_instantiation(instance):
    assert isinstance(instance, expression_Procedure)

@given(instance=expression_ProcedureCall_strategy)
@settings(max_examples=50)
def test_expression_procedurecall_instantiation(instance):
    assert isinstance(instance, expression_ProcedureCall)

@given(instance=expression_ExpressionList_strategy)
@settings(max_examples=50)
def test_expression_expressionlist_instantiation(instance):
    assert isinstance(instance, expression_ExpressionList)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression_Sum_strategy)
@settings(max_examples=50)
def test_expression_sum_instantiation(instance):
    assert isinstance(instance, expression_Sum)

@given(instance=expression_PowExpression_strategy)
@settings(max_examples=50)
def test_expression_powexpression_instantiation(instance):
    assert isinstance(instance, expression_PowExpression)



@given(instance=expression_PowExpression_strategy)
def test_expression_powexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_LastIn_strategy)
@settings(max_examples=50)
def test_expression_lastin_instantiation(instance):
    assert isinstance(instance, expression_LastIn)

@given(instance=expression_Apply_strategy)
@settings(max_examples=50)
def test_expression_apply_instantiation(instance):
    assert isinstance(instance, expression_Apply)

@given(instance=expression_EqualityExpression_strategy)
@settings(max_examples=50)
def test_expression_equalityexpression_instantiation(instance):
    assert isinstance(instance, expression_EqualityExpression)



@given(instance=expression_EqualityExpression_strategy)
def test_expression_equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_ThereIsIn_strategy)
@settings(max_examples=50)
def test_expression_thereisin_instantiation(instance):
    assert isinstance(instance, expression_ThereIsIn)

@given(instance=expression_PointExpression_strategy)
@settings(max_examples=50)
def test_expression_pointexpression_instantiation(instance):
    assert isinstance(instance, expression_PointExpression)



@given(instance=expression_PointExpression_strategy)
def test_expression_pointexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_FirstIn_strategy)
@settings(max_examples=50)
def test_expression_firstin_instantiation(instance):
    assert isinstance(instance, expression_FirstIn)

@given(instance=expression_ForallIn_strategy)
@settings(max_examples=50)
def test_expression_forallin_instantiation(instance):
    assert isinstance(instance, expression_ForallIn)

@given(instance=expression_Count_strategy)
@settings(max_examples=50)
def test_expression_count_instantiation(instance):
    assert isinstance(instance, expression_Count)

@given(instance=expression_UnaryExpression_strategy)
@settings(max_examples=50)
def test_expression_unaryexpression_instantiation(instance):
    assert isinstance(instance, expression_UnaryExpression)

@given(instance=expression_StructureExpression_strategy)
@settings(max_examples=50)
def test_expression_structureexpression_instantiation(instance):
    assert isinstance(instance, expression_StructureExpression)

@given(instance=expression_DashExpression_strategy)
@settings(max_examples=50)
def test_expression_dashexpression_instantiation(instance):
    assert isinstance(instance, expression_DashExpression)



@given(instance=expression_DashExpression_strategy)
def test_expression_dashexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_AndExpression_strategy)
@settings(max_examples=50)
def test_expression_andexpression_instantiation(instance):
    assert isinstance(instance, expression_AndExpression)



@given(instance=expression_AndExpression_strategy)
def test_expression_andexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_QualifierExpression_strategy)
@settings(max_examples=50)
def test_expression_qualifierexpression_instantiation(instance):
    assert isinstance(instance, expression_QualifierExpression)



@given(instance=expression_QualifierExpression_strategy)
def test_expression_qualifierexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_Map_strategy)
@settings(max_examples=50)
def test_expression_map_instantiation(instance):
    assert isinstance(instance, expression_Map)

@given(instance=expression_Reduce_strategy)
@settings(max_examples=50)
def test_expression_reduce_instantiation(instance):
    assert isinstance(instance, expression_Reduce)

@given(instance=expression_FunctionCall_strategy)
@settings(max_examples=50)
def test_expression_functioncall_instantiation(instance):
    assert isinstance(instance, expression_FunctionCall)

@given(instance=ExpressionRest_strategy)
@settings(max_examples=50)
def test_expressionrest_instantiation(instance):
    assert isinstance(instance, ExpressionRest)

@given(instance=expression_OrExpression_strategy)
@settings(max_examples=50)
def test_expression_orexpression_instantiation(instance):
    assert isinstance(instance, expression_OrExpression)



@given(instance=expression_OrExpression_strategy)
def test_expression_orexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_EObject_strategy)
@settings(max_examples=50)
def test_expression_eobject_instantiation(instance):
    assert isinstance(instance, expression_EObject)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=expression_IntegerValue_strategy)
@settings(max_examples=50)
def test_expression_integervalue_instantiation(instance):
    assert isinstance(instance, expression_IntegerValue)



@given(instance=expression_IntegerValue_strategy)
def test_expression_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_StringValue_strategy)
@settings(max_examples=50)
def test_expression_stringvalue_instantiation(instance):
    assert isinstance(instance, expression_StringValue)



@given(instance=expression_StringValue_strategy)
def test_expression_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_DoubleValue_strategy)
@settings(max_examples=50)
def test_expression_doublevalue_instantiation(instance):
    assert isinstance(instance, expression_DoubleValue)



@given(instance=expression_DoubleValue_strategy)
def test_expression_doublevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_List_strategy)
@settings(max_examples=50)
def test_expression_list_instantiation(instance):
    assert isinstance(instance, expression_List)

@given(instance=expression_Term_strategy)
@settings(max_examples=50)
def test_expression_term_instantiation(instance):
    assert isinstance(instance, expression_Term)

@given(instance=expression_KeyValuePairRest_strategy)
@settings(max_examples=50)
def test_expression_keyvaluepairrest_instantiation(instance):
    assert isinstance(instance, expression_KeyValuePairRest)

@given(instance=KeyValuePairRest_strategy)
@settings(max_examples=50)
def test_keyvaluepairrest_instantiation(instance):
    assert isinstance(instance, KeyValuePairRest)

@given(instance=expression_KeyValuePair_strategy)
@settings(max_examples=50)
def test_expression_keyvaluepair_instantiation(instance):
    assert isinstance(instance, expression_KeyValuePair)



@given(instance=expression_KeyValuePair_strategy)
def test_expression_keyvaluepair_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=expression_ExpressionRest_strategy)
@settings(max_examples=50)
def test_expression_expressionrest_instantiation(instance):
    assert isinstance(instance, expression_ExpressionRest)

@given(instance=Phrase_strategy)
@settings(max_examples=50)
def test_phrase_instantiation(instance):
    assert isinstance(instance, Phrase)

@given(instance=expression_StatementList_strategy)
@settings(max_examples=50)
def test_expression_statementlist_instantiation(instance):
    assert isinstance(instance, expression_StatementList)

@given(instance=expression_Phrase_strategy)
@settings(max_examples=50)
def test_expression_phrase_instantiation(instance):
    assert isinstance(instance, expression_Phrase)

@given(instance=expression_Model_strategy)
@settings(max_examples=50)
def test_expression_model_instantiation(instance):
    assert isinstance(instance, expression_Model)

@given(instance=expression_Designator_strategy)
@settings(max_examples=50)
def test_expression_designator_instantiation(instance):
    assert isinstance(instance, expression_Designator)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=expression_SelfAssignmentStatement_strategy)
@settings(max_examples=50)
def test_expression_selfassignmentstatement_instantiation(instance):
    assert isinstance(instance, expression_SelfAssignmentStatement)

@given(instance=expression_VariableAssignmentStatement_strategy)
@settings(max_examples=50)
def test_expression_variableassignmentstatement_instantiation(instance):
    assert isinstance(instance, expression_VariableAssignmentStatement)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=expression_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_expression_assignmentstatement_instantiation(instance):
    assert isinstance(instance, expression_AssignmentStatement)

@given(instance=expression_Statement_strategy)
@settings(max_examples=50)
def test_expression_statement_instantiation(instance):
    assert isinstance(instance, expression_Statement)
