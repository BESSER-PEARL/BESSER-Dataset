import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Statement,
    simple_lang_IfStatement,
    simple_lang_ExpressionStatement,
    FeatureCallExpression,
    simple_lang_PropertyCallExpression,
    simple_lang_MethodCallExpression,
    simple_lang_AssignmentStatement,
    simple_lang_WhileStatement,
    BinaryExpression,
    simple_lang_ArithmeticExpression,
    simple_lang_ComparisonExpression,
    simple_lang_LogicalExpression,
    Expression,
    simple_lang_FeatureCallExpression,
    simple_lang_BinaryExpression,
    simple_lang_Type,
    simple_lang_Expression,
    simple_lang_Statement,
    simple_lang_SimpleLang,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_ifstatement_is_not_abstract():
    assert not inspect.isabstract(simple_lang_IfStatement)


def test_simple_lang_ifstatement_constructor_exists():
    assert callable(simple_lang_IfStatement.__init__)


def test_simple_lang_ifstatement_constructor_args():
    sig = inspect.signature(simple_lang_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(simple_lang_ExpressionStatement)


def test_simple_lang_expressionstatement_constructor_exists():
    assert callable(simple_lang_ExpressionStatement.__init__)


def test_simple_lang_expressionstatement_constructor_args():
    sig = inspect.signature(simple_lang_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_PropertyCallExpression)


def test_simple_lang_propertycallexpression_constructor_exists():
    assert callable(simple_lang_PropertyCallExpression.__init__)


def test_simple_lang_propertycallexpression_constructor_args():
    sig = inspect.signature(simple_lang_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_MethodCallExpression)


def test_simple_lang_methodcallexpression_constructor_exists():
    assert callable(simple_lang_MethodCallExpression.__init__)


def test_simple_lang_methodcallexpression_constructor_args():
    sig = inspect.signature(simple_lang_MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(simple_lang_AssignmentStatement)


def test_simple_lang_assignmentstatement_constructor_exists():
    assert callable(simple_lang_AssignmentStatement.__init__)


def test_simple_lang_assignmentstatement_constructor_args():
    sig = inspect.signature(simple_lang_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_whilestatement_is_not_abstract():
    assert not inspect.isabstract(simple_lang_WhileStatement)


def test_simple_lang_whilestatement_constructor_exists():
    assert callable(simple_lang_WhileStatement.__init__)


def test_simple_lang_whilestatement_constructor_args():
    sig = inspect.signature(simple_lang_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_ArithmeticExpression)


def test_simple_lang_arithmeticexpression_constructor_exists():
    assert callable(simple_lang_ArithmeticExpression.__init__)


def test_simple_lang_arithmeticexpression_constructor_args():
    sig = inspect.signature(simple_lang_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_ComparisonExpression)


def test_simple_lang_comparisonexpression_constructor_exists():
    assert callable(simple_lang_ComparisonExpression.__init__)


def test_simple_lang_comparisonexpression_constructor_args():
    sig = inspect.signature(simple_lang_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_LogicalExpression)


def test_simple_lang_logicalexpression_constructor_exists():
    assert callable(simple_lang_LogicalExpression.__init__)


def test_simple_lang_logicalexpression_constructor_args():
    sig = inspect.signature(simple_lang_LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_FeatureCallExpression)


def test_simple_lang_featurecallexpression_constructor_exists():
    assert callable(simple_lang_FeatureCallExpression.__init__)


def test_simple_lang_featurecallexpression_constructor_args():
    sig = inspect.signature(simple_lang_FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simple_lang_featurecallexpression_has_name():
    assert hasattr(simple_lang_FeatureCallExpression, "name")
    descriptor = None
    for klass in simple_lang_FeatureCallExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple_lang_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_BinaryExpression)


def test_simple_lang_binaryexpression_constructor_exists():
    assert callable(simple_lang_BinaryExpression.__init__)


def test_simple_lang_binaryexpression_constructor_args():
    sig = inspect.signature(simple_lang_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_simple_lang_binaryexpression_has_operator():
    assert hasattr(simple_lang_BinaryExpression, "operator")
    descriptor = None
    for klass in simple_lang_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_simple_lang_type_is_not_abstract():
    assert not inspect.isabstract(simple_lang_Type)


def test_simple_lang_type_constructor_exists():
    assert callable(simple_lang_Type.__init__)


def test_simple_lang_type_constructor_args():
    sig = inspect.signature(simple_lang_Type.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_expression_is_not_abstract():
    assert not inspect.isabstract(simple_lang_Expression)


def test_simple_lang_expression_constructor_exists():
    assert callable(simple_lang_Expression.__init__)


def test_simple_lang_expression_constructor_args():
    sig = inspect.signature(simple_lang_Expression.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_statement_is_not_abstract():
    assert not inspect.isabstract(simple_lang_Statement)


def test_simple_lang_statement_constructor_exists():
    assert callable(simple_lang_Statement.__init__)


def test_simple_lang_statement_constructor_args():
    sig = inspect.signature(simple_lang_Statement.__init__)
    params = list(sig.parameters.keys())



def test_simple_lang_simplelang_is_not_abstract():
    assert not inspect.isabstract(simple_lang_SimpleLang)


def test_simple_lang_simplelang_constructor_exists():
    assert callable(simple_lang_SimpleLang.__init__)


def test_simple_lang_simplelang_constructor_args():
    sig = inspect.signature(simple_lang_SimpleLang.__init__)
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
Statement_strategy = st.builds(
    Statement,
)
simple_lang_IfStatement_strategy = st.builds(
    simple_lang_IfStatement,
)
simple_lang_ExpressionStatement_strategy = st.builds(
    simple_lang_ExpressionStatement,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
simple_lang_PropertyCallExpression_strategy = st.builds(
    simple_lang_PropertyCallExpression,
)
simple_lang_MethodCallExpression_strategy = st.builds(
    simple_lang_MethodCallExpression,
)
simple_lang_AssignmentStatement_strategy = st.builds(
    simple_lang_AssignmentStatement,
)
simple_lang_WhileStatement_strategy = st.builds(
    simple_lang_WhileStatement,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
simple_lang_ArithmeticExpression_strategy = st.builds(
    simple_lang_ArithmeticExpression,
)
simple_lang_ComparisonExpression_strategy = st.builds(
    simple_lang_ComparisonExpression,
)
simple_lang_LogicalExpression_strategy = st.builds(
    simple_lang_LogicalExpression,
)
Expression_strategy = st.builds(
    Expression,
)
simple_lang_FeatureCallExpression_strategy = st.builds(
    simple_lang_FeatureCallExpression,
    name=
        safe_text
)
simple_lang_BinaryExpression_strategy = st.builds(
    simple_lang_BinaryExpression,
    operator=
        safe_text
)
simple_lang_Type_strategy = st.builds(
    simple_lang_Type,
)
simple_lang_Expression_strategy = st.builds(
    simple_lang_Expression,
)
simple_lang_Statement_strategy = st.builds(
    simple_lang_Statement,
)
simple_lang_SimpleLang_strategy = st.builds(
    simple_lang_SimpleLang,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simple_lang_IfStatement_strategy)
@settings(max_examples=50)
def test_simple_lang_ifstatement_instantiation(instance):
    assert isinstance(instance, simple_lang_IfStatement)

@given(instance=simple_lang_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_simple_lang_expressionstatement_instantiation(instance):
    assert isinstance(instance, simple_lang_ExpressionStatement)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=simple_lang_PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_propertycallexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_PropertyCallExpression)

@given(instance=simple_lang_MethodCallExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_methodcallexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_MethodCallExpression)

@given(instance=simple_lang_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_simple_lang_assignmentstatement_instantiation(instance):
    assert isinstance(instance, simple_lang_AssignmentStatement)

@given(instance=simple_lang_WhileStatement_strategy)
@settings(max_examples=50)
def test_simple_lang_whilestatement_instantiation(instance):
    assert isinstance(instance, simple_lang_WhileStatement)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=simple_lang_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_ArithmeticExpression)

@given(instance=simple_lang_ComparisonExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_comparisonexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_ComparisonExpression)

@given(instance=simple_lang_LogicalExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_logicalexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_LogicalExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=simple_lang_FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_featurecallexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_FeatureCallExpression)



@given(instance=simple_lang_FeatureCallExpression_strategy)
def test_simple_lang_featurecallexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simple_lang_BinaryExpression_strategy)
@settings(max_examples=50)
def test_simple_lang_binaryexpression_instantiation(instance):
    assert isinstance(instance, simple_lang_BinaryExpression)



@given(instance=simple_lang_BinaryExpression_strategy)
def test_simple_lang_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=simple_lang_Type_strategy)
@settings(max_examples=50)
def test_simple_lang_type_instantiation(instance):
    assert isinstance(instance, simple_lang_Type)

@given(instance=simple_lang_Expression_strategy)
@settings(max_examples=50)
def test_simple_lang_expression_instantiation(instance):
    assert isinstance(instance, simple_lang_Expression)

@given(instance=simple_lang_Statement_strategy)
@settings(max_examples=50)
def test_simple_lang_statement_instantiation(instance):
    assert isinstance(instance, simple_lang_Statement)

@given(instance=simple_lang_SimpleLang_strategy)
@settings(max_examples=50)
def test_simple_lang_simplelang_instantiation(instance):
    assert isinstance(instance, simple_lang_SimpleLang)
