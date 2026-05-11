import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    expression::Procedure,
    expression::ProcedureCall,
    expression::ExpressionList,
    Function,
    Expression,
    expression::EqualityExpression,
    expression::ThereIsIn,
    expression::UnaryExpression,
    expression::PointExpression,
    expression::PowExpression,
    expression::Apply,
    expression::Map,
    expression::LastIn,
    expression::Sum,
    expression::Reduce,
    expression::StructureExpression,
    expression::FirstIn,
    expression::Count,
    expression::AndExpression,
    expression::ForallIn,
    expression::DashExpression,
    expression::QualifierExpression,
    expression::FunctionCall,
    ExpressionRest,
    expression::OrExpression,
    expression::EObject,
    Term,
    expression::StringValue,
    expression::IntegerValue,
    expression::DoubleValue,
    expression::List,
    expression::Term,
    expression::KeyValuePairRest,
    KeyValuePairRest,
    expression::KeyValuePair,
    expression::ExpressionRest,
    Phrase,
    expression::StatementList,
    expression::Phrase,
    expression::Model,
    expression::Designator,
    AssignmentStatement,
    expression::SelfAssignmentStatement,
    expression::VariableAssignmentStatement,
    expression::Expression,
    Statement,
    expression::AssignmentStatement,
    expression::Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression::procedure_is_not_abstract():
    assert not inspect.isabstract(expression::Procedure)


def test_expression::procedure_constructor_exists():
    assert callable(expression::Procedure.__init__)


def test_expression::procedure_constructor_args():
    sig = inspect.signature(expression::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_expression::procedurecall_is_not_abstract():
    assert not inspect.isabstract(expression::ProcedureCall)


def test_expression::procedurecall_constructor_exists():
    assert callable(expression::ProcedureCall.__init__)


def test_expression::procedurecall_constructor_args():
    sig = inspect.signature(expression::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expression::expressionlist_is_not_abstract():
    assert not inspect.isabstract(expression::ExpressionList)


def test_expression::expressionlist_constructor_exists():
    assert callable(expression::ExpressionList.__init__)


def test_expression::expressionlist_constructor_args():
    sig = inspect.signature(expression::ExpressionList.__init__)
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



def test_expression::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(expression::EqualityExpression)


def test_expression::equalityexpression_constructor_exists():
    assert callable(expression::EqualityExpression.__init__)


def test_expression::equalityexpression_constructor_args():
    sig = inspect.signature(expression::EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::equalityexpression_has_op():
    assert hasattr(expression::EqualityExpression, "op")
    descriptor = None
    for klass in expression::EqualityExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::thereisin_is_not_abstract():
    assert not inspect.isabstract(expression::ThereIsIn)


def test_expression::thereisin_constructor_exists():
    assert callable(expression::ThereIsIn.__init__)


def test_expression::thereisin_constructor_args():
    sig = inspect.signature(expression::ThereIsIn.__init__)
    params = list(sig.parameters.keys())



def test_expression::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression::UnaryExpression)


def test_expression::unaryexpression_constructor_exists():
    assert callable(expression::UnaryExpression.__init__)


def test_expression::unaryexpression_constructor_args():
    sig = inspect.signature(expression::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::pointexpression_is_not_abstract():
    assert not inspect.isabstract(expression::PointExpression)


def test_expression::pointexpression_constructor_exists():
    assert callable(expression::PointExpression.__init__)


def test_expression::pointexpression_constructor_args():
    sig = inspect.signature(expression::PointExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::pointexpression_has_op():
    assert hasattr(expression::PointExpression, "op")
    descriptor = None
    for klass in expression::PointExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::powexpression_is_not_abstract():
    assert not inspect.isabstract(expression::PowExpression)


def test_expression::powexpression_constructor_exists():
    assert callable(expression::PowExpression.__init__)


def test_expression::powexpression_constructor_args():
    sig = inspect.signature(expression::PowExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::powexpression_has_op():
    assert hasattr(expression::PowExpression, "op")
    descriptor = None
    for klass in expression::PowExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::apply_is_not_abstract():
    assert not inspect.isabstract(expression::Apply)


def test_expression::apply_constructor_exists():
    assert callable(expression::Apply.__init__)


def test_expression::apply_constructor_args():
    sig = inspect.signature(expression::Apply.__init__)
    params = list(sig.parameters.keys())



def test_expression::map_is_not_abstract():
    assert not inspect.isabstract(expression::Map)


def test_expression::map_constructor_exists():
    assert callable(expression::Map.__init__)


def test_expression::map_constructor_args():
    sig = inspect.signature(expression::Map.__init__)
    params = list(sig.parameters.keys())



def test_expression::lastin_is_not_abstract():
    assert not inspect.isabstract(expression::LastIn)


def test_expression::lastin_constructor_exists():
    assert callable(expression::LastIn.__init__)


def test_expression::lastin_constructor_args():
    sig = inspect.signature(expression::LastIn.__init__)
    params = list(sig.parameters.keys())



def test_expression::sum_is_not_abstract():
    assert not inspect.isabstract(expression::Sum)


def test_expression::sum_constructor_exists():
    assert callable(expression::Sum.__init__)


def test_expression::sum_constructor_args():
    sig = inspect.signature(expression::Sum.__init__)
    params = list(sig.parameters.keys())



def test_expression::reduce_is_not_abstract():
    assert not inspect.isabstract(expression::Reduce)


def test_expression::reduce_constructor_exists():
    assert callable(expression::Reduce.__init__)


def test_expression::reduce_constructor_args():
    sig = inspect.signature(expression::Reduce.__init__)
    params = list(sig.parameters.keys())



def test_expression::structureexpression_is_not_abstract():
    assert not inspect.isabstract(expression::StructureExpression)


def test_expression::structureexpression_constructor_exists():
    assert callable(expression::StructureExpression.__init__)


def test_expression::structureexpression_constructor_args():
    sig = inspect.signature(expression::StructureExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::firstin_is_not_abstract():
    assert not inspect.isabstract(expression::FirstIn)


def test_expression::firstin_constructor_exists():
    assert callable(expression::FirstIn.__init__)


def test_expression::firstin_constructor_args():
    sig = inspect.signature(expression::FirstIn.__init__)
    params = list(sig.parameters.keys())



def test_expression::count_is_not_abstract():
    assert not inspect.isabstract(expression::Count)


def test_expression::count_constructor_exists():
    assert callable(expression::Count.__init__)


def test_expression::count_constructor_args():
    sig = inspect.signature(expression::Count.__init__)
    params = list(sig.parameters.keys())



def test_expression::andexpression_is_not_abstract():
    assert not inspect.isabstract(expression::AndExpression)


def test_expression::andexpression_constructor_exists():
    assert callable(expression::AndExpression.__init__)


def test_expression::andexpression_constructor_args():
    sig = inspect.signature(expression::AndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::andexpression_has_op():
    assert hasattr(expression::AndExpression, "op")
    descriptor = None
    for klass in expression::AndExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::forallin_is_not_abstract():
    assert not inspect.isabstract(expression::ForallIn)


def test_expression::forallin_constructor_exists():
    assert callable(expression::ForallIn.__init__)


def test_expression::forallin_constructor_args():
    sig = inspect.signature(expression::ForallIn.__init__)
    params = list(sig.parameters.keys())



def test_expression::dashexpression_is_not_abstract():
    assert not inspect.isabstract(expression::DashExpression)


def test_expression::dashexpression_constructor_exists():
    assert callable(expression::DashExpression.__init__)


def test_expression::dashexpression_constructor_args():
    sig = inspect.signature(expression::DashExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::dashexpression_has_op():
    assert hasattr(expression::DashExpression, "op")
    descriptor = None
    for klass in expression::DashExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::qualifierexpression_is_not_abstract():
    assert not inspect.isabstract(expression::QualifierExpression)


def test_expression::qualifierexpression_constructor_exists():
    assert callable(expression::QualifierExpression.__init__)


def test_expression::qualifierexpression_constructor_args():
    sig = inspect.signature(expression::QualifierExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::qualifierexpression_has_op():
    assert hasattr(expression::QualifierExpression, "op")
    descriptor = None
    for klass in expression::QualifierExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::functioncall_is_not_abstract():
    assert not inspect.isabstract(expression::FunctionCall)


def test_expression::functioncall_constructor_exists():
    assert callable(expression::FunctionCall.__init__)


def test_expression::functioncall_constructor_args():
    sig = inspect.signature(expression::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionrest_is_not_abstract():
    assert not inspect.isabstract(ExpressionRest)


def test_expressionrest_constructor_exists():
    assert callable(ExpressionRest.__init__)


def test_expressionrest_constructor_args():
    sig = inspect.signature(ExpressionRest.__init__)
    params = list(sig.parameters.keys())



def test_expression::orexpression_is_not_abstract():
    assert not inspect.isabstract(expression::OrExpression)


def test_expression::orexpression_constructor_exists():
    assert callable(expression::OrExpression.__init__)


def test_expression::orexpression_constructor_args():
    sig = inspect.signature(expression::OrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::orexpression_has_op():
    assert hasattr(expression::OrExpression, "op")
    descriptor = None
    for klass in expression::OrExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::eobject_is_not_abstract():
    assert not inspect.isabstract(expression::EObject)


def test_expression::eobject_constructor_exists():
    assert callable(expression::EObject.__init__)


def test_expression::eobject_constructor_args():
    sig = inspect.signature(expression::EObject.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_expression::stringvalue_is_not_abstract():
    assert not inspect.isabstract(expression::StringValue)


def test_expression::stringvalue_constructor_exists():
    assert callable(expression::StringValue.__init__)


def test_expression::stringvalue_constructor_args():
    sig = inspect.signature(expression::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::stringvalue_has_value():
    assert hasattr(expression::StringValue, "value")
    descriptor = None
    for klass in expression::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::integervalue_is_not_abstract():
    assert not inspect.isabstract(expression::IntegerValue)


def test_expression::integervalue_constructor_exists():
    assert callable(expression::IntegerValue.__init__)


def test_expression::integervalue_constructor_args():
    sig = inspect.signature(expression::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::integervalue_has_value():
    assert hasattr(expression::IntegerValue, "value")
    descriptor = None
    for klass in expression::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::doublevalue_is_not_abstract():
    assert not inspect.isabstract(expression::DoubleValue)


def test_expression::doublevalue_constructor_exists():
    assert callable(expression::DoubleValue.__init__)


def test_expression::doublevalue_constructor_args():
    sig = inspect.signature(expression::DoubleValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::doublevalue_has_value():
    assert hasattr(expression::DoubleValue, "value")
    descriptor = None
    for klass in expression::DoubleValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::list_is_not_abstract():
    assert not inspect.isabstract(expression::List)


def test_expression::list_constructor_exists():
    assert callable(expression::List.__init__)


def test_expression::list_constructor_args():
    sig = inspect.signature(expression::List.__init__)
    params = list(sig.parameters.keys())



def test_expression::term_is_not_abstract():
    assert not inspect.isabstract(expression::Term)


def test_expression::term_constructor_exists():
    assert callable(expression::Term.__init__)


def test_expression::term_constructor_args():
    sig = inspect.signature(expression::Term.__init__)
    params = list(sig.parameters.keys())



def test_expression::keyvaluepairrest_is_not_abstract():
    assert not inspect.isabstract(expression::KeyValuePairRest)


def test_expression::keyvaluepairrest_constructor_exists():
    assert callable(expression::KeyValuePairRest.__init__)


def test_expression::keyvaluepairrest_constructor_args():
    sig = inspect.signature(expression::KeyValuePairRest.__init__)
    params = list(sig.parameters.keys())



def test_keyvaluepairrest_is_not_abstract():
    assert not inspect.isabstract(KeyValuePairRest)


def test_keyvaluepairrest_constructor_exists():
    assert callable(KeyValuePairRest.__init__)


def test_keyvaluepairrest_constructor_args():
    sig = inspect.signature(KeyValuePairRest.__init__)
    params = list(sig.parameters.keys())



def test_expression::keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(expression::KeyValuePair)


def test_expression::keyvaluepair_constructor_exists():
    assert callable(expression::KeyValuePair.__init__)


def test_expression::keyvaluepair_constructor_args():
    sig = inspect.signature(expression::KeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_expression::keyvaluepair_has_key():
    assert hasattr(expression::KeyValuePair, "key")
    descriptor = None
    for klass in expression::KeyValuePair.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_expression::expressionrest_is_not_abstract():
    assert not inspect.isabstract(expression::ExpressionRest)


def test_expression::expressionrest_constructor_exists():
    assert callable(expression::ExpressionRest.__init__)


def test_expression::expressionrest_constructor_args():
    sig = inspect.signature(expression::ExpressionRest.__init__)
    params = list(sig.parameters.keys())



def test_phrase_is_not_abstract():
    assert not inspect.isabstract(Phrase)


def test_phrase_constructor_exists():
    assert callable(Phrase.__init__)


def test_phrase_constructor_args():
    sig = inspect.signature(Phrase.__init__)
    params = list(sig.parameters.keys())



def test_expression::statementlist_is_not_abstract():
    assert not inspect.isabstract(expression::StatementList)


def test_expression::statementlist_constructor_exists():
    assert callable(expression::StatementList.__init__)


def test_expression::statementlist_constructor_args():
    sig = inspect.signature(expression::StatementList.__init__)
    params = list(sig.parameters.keys())



def test_expression::phrase_is_not_abstract():
    assert not inspect.isabstract(expression::Phrase)


def test_expression::phrase_constructor_exists():
    assert callable(expression::Phrase.__init__)


def test_expression::phrase_constructor_args():
    sig = inspect.signature(expression::Phrase.__init__)
    params = list(sig.parameters.keys())



def test_expression::model_is_not_abstract():
    assert not inspect.isabstract(expression::Model)


def test_expression::model_constructor_exists():
    assert callable(expression::Model.__init__)


def test_expression::model_constructor_args():
    sig = inspect.signature(expression::Model.__init__)
    params = list(sig.parameters.keys())



def test_expression::designator_is_not_abstract():
    assert not inspect.isabstract(expression::Designator)


def test_expression::designator_constructor_exists():
    assert callable(expression::Designator.__init__)


def test_expression::designator_constructor_args():
    sig = inspect.signature(expression::Designator.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression::selfassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(expression::SelfAssignmentStatement)


def test_expression::selfassignmentstatement_constructor_exists():
    assert callable(expression::SelfAssignmentStatement.__init__)


def test_expression::selfassignmentstatement_constructor_args():
    sig = inspect.signature(expression::SelfAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression::variableassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(expression::VariableAssignmentStatement)


def test_expression::variableassignmentstatement_constructor_exists():
    assert callable(expression::VariableAssignmentStatement.__init__)


def test_expression::variableassignmentstatement_constructor_args():
    sig = inspect.signature(expression::VariableAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_expression::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(expression::AssignmentStatement)


def test_expression::assignmentstatement_constructor_exists():
    assert callable(expression::AssignmentStatement.__init__)


def test_expression::assignmentstatement_constructor_args():
    sig = inspect.signature(expression::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression::statement_is_not_abstract():
    assert not inspect.isabstract(expression::Statement)


def test_expression::statement_constructor_exists():
    assert callable(expression::Statement.__init__)


def test_expression::statement_constructor_args():
    sig = inspect.signature(expression::Statement.__init__)
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
expression::Procedure_strategy = st.builds(
    expression::Procedure,
)
expression::ProcedureCall_strategy = st.builds(
    expression::ProcedureCall,
)
expression::ExpressionList_strategy = st.builds(
    expression::ExpressionList,
)
Function_strategy = st.builds(
    Function,
)
Expression_strategy = st.builds(
    Expression,
)
expression::EqualityExpression_strategy = st.builds(
    expression::EqualityExpression,
    op=
        safe_text
)
expression::ThereIsIn_strategy = st.builds(
    expression::ThereIsIn,
)
expression::UnaryExpression_strategy = st.builds(
    expression::UnaryExpression,
)
expression::PointExpression_strategy = st.builds(
    expression::PointExpression,
    op=
        safe_text
)
expression::PowExpression_strategy = st.builds(
    expression::PowExpression,
    op=
        safe_text
)
expression::Apply_strategy = st.builds(
    expression::Apply,
)
expression::Map_strategy = st.builds(
    expression::Map,
)
expression::LastIn_strategy = st.builds(
    expression::LastIn,
)
expression::Sum_strategy = st.builds(
    expression::Sum,
)
expression::Reduce_strategy = st.builds(
    expression::Reduce,
)
expression::StructureExpression_strategy = st.builds(
    expression::StructureExpression,
)
expression::FirstIn_strategy = st.builds(
    expression::FirstIn,
)
expression::Count_strategy = st.builds(
    expression::Count,
)
expression::AndExpression_strategy = st.builds(
    expression::AndExpression,
    op=
        safe_text
)
expression::ForallIn_strategy = st.builds(
    expression::ForallIn,
)
expression::DashExpression_strategy = st.builds(
    expression::DashExpression,
    op=
        safe_text
)
expression::QualifierExpression_strategy = st.builds(
    expression::QualifierExpression,
    op=
        safe_text
)
expression::FunctionCall_strategy = st.builds(
    expression::FunctionCall,
)
ExpressionRest_strategy = st.builds(
    ExpressionRest,
)
expression::OrExpression_strategy = st.builds(
    expression::OrExpression,
    op=
        safe_text
)
expression::EObject_strategy = st.builds(
    expression::EObject,
)
Term_strategy = st.builds(
    Term,
)
expression::StringValue_strategy = st.builds(
    expression::StringValue,
    value=
        safe_text
)
expression::IntegerValue_strategy = st.builds(
    expression::IntegerValue,
    value=
        st.integers()
)
expression::DoubleValue_strategy = st.builds(
    expression::DoubleValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expression::List_strategy = st.builds(
    expression::List,
)
expression::Term_strategy = st.builds(
    expression::Term,
)
expression::KeyValuePairRest_strategy = st.builds(
    expression::KeyValuePairRest,
)
KeyValuePairRest_strategy = st.builds(
    KeyValuePairRest,
)
expression::KeyValuePair_strategy = st.builds(
    expression::KeyValuePair,
    key=
        safe_text
)
expression::ExpressionRest_strategy = st.builds(
    expression::ExpressionRest,
)
Phrase_strategy = st.builds(
    Phrase,
)
expression::StatementList_strategy = st.builds(
    expression::StatementList,
)
expression::Phrase_strategy = st.builds(
    expression::Phrase,
)
expression::Model_strategy = st.builds(
    expression::Model,
)
expression::Designator_strategy = st.builds(
    expression::Designator,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
expression::SelfAssignmentStatement_strategy = st.builds(
    expression::SelfAssignmentStatement,
)
expression::VariableAssignmentStatement_strategy = st.builds(
    expression::VariableAssignmentStatement,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
expression::AssignmentStatement_strategy = st.builds(
    expression::AssignmentStatement,
)
expression::Statement_strategy = st.builds(
    expression::Statement,
)

@given(instance=expression::Procedure_strategy)
@settings(max_examples=50)
def test_expression::procedure_instantiation(instance):
    assert isinstance(instance, expression::Procedure)

@given(instance=expression::ProcedureCall_strategy)
@settings(max_examples=50)
def test_expression::procedurecall_instantiation(instance):
    assert isinstance(instance, expression::ProcedureCall)

@given(instance=expression::ExpressionList_strategy)
@settings(max_examples=50)
def test_expression::expressionlist_instantiation(instance):
    assert isinstance(instance, expression::ExpressionList)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression::EqualityExpression_strategy)
@settings(max_examples=50)
def test_expression::equalityexpression_instantiation(instance):
    assert isinstance(instance, expression::EqualityExpression)

@given(instance=expression::EqualityExpression_strategy)
def test_expression::equalityexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::EqualityExpression_strategy)
def test_expression::equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::ThereIsIn_strategy)
@settings(max_examples=50)
def test_expression::thereisin_instantiation(instance):
    assert isinstance(instance, expression::ThereIsIn)

@given(instance=expression::UnaryExpression_strategy)
@settings(max_examples=50)
def test_expression::unaryexpression_instantiation(instance):
    assert isinstance(instance, expression::UnaryExpression)

@given(instance=expression::PointExpression_strategy)
@settings(max_examples=50)
def test_expression::pointexpression_instantiation(instance):
    assert isinstance(instance, expression::PointExpression)

@given(instance=expression::PointExpression_strategy)
def test_expression::pointexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::PointExpression_strategy)
def test_expression::pointexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::PowExpression_strategy)
@settings(max_examples=50)
def test_expression::powexpression_instantiation(instance):
    assert isinstance(instance, expression::PowExpression)

@given(instance=expression::PowExpression_strategy)
def test_expression::powexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::PowExpression_strategy)
def test_expression::powexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::Apply_strategy)
@settings(max_examples=50)
def test_expression::apply_instantiation(instance):
    assert isinstance(instance, expression::Apply)

@given(instance=expression::Map_strategy)
@settings(max_examples=50)
def test_expression::map_instantiation(instance):
    assert isinstance(instance, expression::Map)

@given(instance=expression::LastIn_strategy)
@settings(max_examples=50)
def test_expression::lastin_instantiation(instance):
    assert isinstance(instance, expression::LastIn)

@given(instance=expression::Sum_strategy)
@settings(max_examples=50)
def test_expression::sum_instantiation(instance):
    assert isinstance(instance, expression::Sum)

@given(instance=expression::Reduce_strategy)
@settings(max_examples=50)
def test_expression::reduce_instantiation(instance):
    assert isinstance(instance, expression::Reduce)

@given(instance=expression::StructureExpression_strategy)
@settings(max_examples=50)
def test_expression::structureexpression_instantiation(instance):
    assert isinstance(instance, expression::StructureExpression)

@given(instance=expression::FirstIn_strategy)
@settings(max_examples=50)
def test_expression::firstin_instantiation(instance):
    assert isinstance(instance, expression::FirstIn)

@given(instance=expression::Count_strategy)
@settings(max_examples=50)
def test_expression::count_instantiation(instance):
    assert isinstance(instance, expression::Count)

@given(instance=expression::AndExpression_strategy)
@settings(max_examples=50)
def test_expression::andexpression_instantiation(instance):
    assert isinstance(instance, expression::AndExpression)

@given(instance=expression::AndExpression_strategy)
def test_expression::andexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::AndExpression_strategy)
def test_expression::andexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::ForallIn_strategy)
@settings(max_examples=50)
def test_expression::forallin_instantiation(instance):
    assert isinstance(instance, expression::ForallIn)

@given(instance=expression::DashExpression_strategy)
@settings(max_examples=50)
def test_expression::dashexpression_instantiation(instance):
    assert isinstance(instance, expression::DashExpression)

@given(instance=expression::DashExpression_strategy)
def test_expression::dashexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::DashExpression_strategy)
def test_expression::dashexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::QualifierExpression_strategy)
@settings(max_examples=50)
def test_expression::qualifierexpression_instantiation(instance):
    assert isinstance(instance, expression::QualifierExpression)

@given(instance=expression::QualifierExpression_strategy)
def test_expression::qualifierexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::QualifierExpression_strategy)
def test_expression::qualifierexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::FunctionCall_strategy)
@settings(max_examples=50)
def test_expression::functioncall_instantiation(instance):
    assert isinstance(instance, expression::FunctionCall)

@given(instance=ExpressionRest_strategy)
@settings(max_examples=50)
def test_expressionrest_instantiation(instance):
    assert isinstance(instance, ExpressionRest)

@given(instance=expression::OrExpression_strategy)
@settings(max_examples=50)
def test_expression::orexpression_instantiation(instance):
    assert isinstance(instance, expression::OrExpression)

@given(instance=expression::OrExpression_strategy)
def test_expression::orexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expression::OrExpression_strategy)
def test_expression::orexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression::EObject_strategy)
@settings(max_examples=50)
def test_expression::eobject_instantiation(instance):
    assert isinstance(instance, expression::EObject)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=expression::StringValue_strategy)
@settings(max_examples=50)
def test_expression::stringvalue_instantiation(instance):
    assert isinstance(instance, expression::StringValue)

@given(instance=expression::StringValue_strategy)
def test_expression::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expression::StringValue_strategy)
def test_expression::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::IntegerValue_strategy)
@settings(max_examples=50)
def test_expression::integervalue_instantiation(instance):
    assert isinstance(instance, expression::IntegerValue)

@given(instance=expression::IntegerValue_strategy)
def test_expression::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expression::IntegerValue_strategy)
def test_expression::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::DoubleValue_strategy)
@settings(max_examples=50)
def test_expression::doublevalue_instantiation(instance):
    assert isinstance(instance, expression::DoubleValue)

@given(instance=expression::DoubleValue_strategy)
def test_expression::doublevalue_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=expression::DoubleValue_strategy)
def test_expression::doublevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::List_strategy)
@settings(max_examples=50)
def test_expression::list_instantiation(instance):
    assert isinstance(instance, expression::List)

@given(instance=expression::Term_strategy)
@settings(max_examples=50)
def test_expression::term_instantiation(instance):
    assert isinstance(instance, expression::Term)

@given(instance=expression::KeyValuePairRest_strategy)
@settings(max_examples=50)
def test_expression::keyvaluepairrest_instantiation(instance):
    assert isinstance(instance, expression::KeyValuePairRest)

@given(instance=KeyValuePairRest_strategy)
@settings(max_examples=50)
def test_keyvaluepairrest_instantiation(instance):
    assert isinstance(instance, KeyValuePairRest)

@given(instance=expression::KeyValuePair_strategy)
@settings(max_examples=50)
def test_expression::keyvaluepair_instantiation(instance):
    assert isinstance(instance, expression::KeyValuePair)

@given(instance=expression::KeyValuePair_strategy)
def test_expression::keyvaluepair_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=expression::KeyValuePair_strategy)
def test_expression::keyvaluepair_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=expression::ExpressionRest_strategy)
@settings(max_examples=50)
def test_expression::expressionrest_instantiation(instance):
    assert isinstance(instance, expression::ExpressionRest)

@given(instance=Phrase_strategy)
@settings(max_examples=50)
def test_phrase_instantiation(instance):
    assert isinstance(instance, Phrase)

@given(instance=expression::StatementList_strategy)
@settings(max_examples=50)
def test_expression::statementlist_instantiation(instance):
    assert isinstance(instance, expression::StatementList)

@given(instance=expression::Phrase_strategy)
@settings(max_examples=50)
def test_expression::phrase_instantiation(instance):
    assert isinstance(instance, expression::Phrase)

@given(instance=expression::Model_strategy)
@settings(max_examples=50)
def test_expression::model_instantiation(instance):
    assert isinstance(instance, expression::Model)

@given(instance=expression::Designator_strategy)
@settings(max_examples=50)
def test_expression::designator_instantiation(instance):
    assert isinstance(instance, expression::Designator)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=expression::SelfAssignmentStatement_strategy)
@settings(max_examples=50)
def test_expression::selfassignmentstatement_instantiation(instance):
    assert isinstance(instance, expression::SelfAssignmentStatement)

@given(instance=expression::VariableAssignmentStatement_strategy)
@settings(max_examples=50)
def test_expression::variableassignmentstatement_instantiation(instance):
    assert isinstance(instance, expression::VariableAssignmentStatement)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=expression::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_expression::assignmentstatement_instantiation(instance):
    assert isinstance(instance, expression::AssignmentStatement)

@given(instance=expression::Statement_strategy)
@settings(max_examples=50)
def test_expression::statement_instantiation(instance):
    assert isinstance(instance, expression::Statement)
