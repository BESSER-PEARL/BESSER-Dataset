import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    myDsl_Operation,
    myDsl_Conditional,
    myDsl_Lambda,
    myDsl_Define,
    myDsl_Expression,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_operation_is_not_abstract():
    assert not inspect.isabstract(myDsl_Operation)


def test_mydsl_operation_constructor_exists():
    assert callable(myDsl_Operation.__init__)


def test_mydsl_operation_constructor_args():
    sig = inspect.signature(myDsl_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "value2" in params, "Missing parameter 'value2'"

def test_mydsl_operation_has_op():
    assert hasattr(myDsl_Operation, "op")
    descriptor = None
    for klass in myDsl_Operation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_operation_has_value2():
    assert hasattr(myDsl_Operation, "value2")
    descriptor = None
    for klass in myDsl_Operation.__mro__:
        if "value2" in klass.__dict__:
            descriptor = klass.__dict__["value2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_conditional_is_not_abstract():
    assert not inspect.isabstract(myDsl_Conditional)


def test_mydsl_conditional_constructor_exists():
    assert callable(myDsl_Conditional.__init__)


def test_mydsl_conditional_constructor_args():
    sig = inspect.signature(myDsl_Conditional.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value2" in params, "Missing parameter 'value2'"
    assert "value3" in params, "Missing parameter 'value3'"

def test_mydsl_conditional_has_name():
    assert hasattr(myDsl_Conditional, "name")
    descriptor = None
    for klass in myDsl_Conditional.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_conditional_has_value2():
    assert hasattr(myDsl_Conditional, "value2")
    descriptor = None
    for klass in myDsl_Conditional.__mro__:
        if "value2" in klass.__dict__:
            descriptor = klass.__dict__["value2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_conditional_has_value3():
    assert hasattr(myDsl_Conditional, "value3")
    descriptor = None
    for klass in myDsl_Conditional.__mro__:
        if "value3" in klass.__dict__:
            descriptor = klass.__dict__["value3"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_lambda_is_not_abstract():
    assert not inspect.isabstract(myDsl_Lambda)


def test_mydsl_lambda_constructor_exists():
    assert callable(myDsl_Lambda.__init__)


def test_mydsl_lambda_constructor_args():
    sig = inspect.signature(myDsl_Lambda.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_lambda_has_name():
    assert hasattr(myDsl_Lambda, "name")
    descriptor = None
    for klass in myDsl_Lambda.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_define_is_not_abstract():
    assert not inspect.isabstract(myDsl_Define)


def test_mydsl_define_constructor_exists():
    assert callable(myDsl_Define.__init__)


def test_mydsl_define_constructor_args():
    sig = inspect.signature(myDsl_Define.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_define_has_name():
    assert hasattr(myDsl_Define, "name")
    descriptor = None
    for klass in myDsl_Define.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_Expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_expression_has_value():
    assert hasattr(myDsl_Expression, "value")
    descriptor = None
    for klass in myDsl_Expression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
myDsl_Operation_strategy = st.builds(
    myDsl_Operation,
    op=
        safe_text,
    value2=
        st.integers()
)
myDsl_Conditional_strategy = st.builds(
    myDsl_Conditional,
    name=
        safe_text,
    value2=
        st.integers(),
    value3=
        st.integers()
)
myDsl_Lambda_strategy = st.builds(
    myDsl_Lambda,
    name=
        safe_text
)
myDsl_Define_strategy = st.builds(
    myDsl_Define,
    name=
        safe_text
)
myDsl_Expression_strategy = st.builds(
    myDsl_Expression,
    value=
        st.integers()
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=myDsl_Operation_strategy)
@settings(max_examples=50)
def test_mydsl_operation_instantiation(instance):
    assert isinstance(instance, myDsl_Operation)



@given(instance=myDsl_Operation_strategy)
def test_mydsl_operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=myDsl_Operation_strategy)
def test_mydsl_operation_value2_setter(instance):
    original = instance.value2
    instance.value2 = original
    assert instance.value2 == original

@given(instance=myDsl_Conditional_strategy)
@settings(max_examples=50)
def test_mydsl_conditional_instantiation(instance):
    assert isinstance(instance, myDsl_Conditional)



@given(instance=myDsl_Conditional_strategy)
def test_mydsl_conditional_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Conditional_strategy)
def test_mydsl_conditional_value2_setter(instance):
    original = instance.value2
    instance.value2 = original
    assert instance.value2 == original



@given(instance=myDsl_Conditional_strategy)
def test_mydsl_conditional_value3_setter(instance):
    original = instance.value3
    instance.value3 = original
    assert instance.value3 == original

@given(instance=myDsl_Lambda_strategy)
@settings(max_examples=50)
def test_mydsl_lambda_instantiation(instance):
    assert isinstance(instance, myDsl_Lambda)



@given(instance=myDsl_Lambda_strategy)
def test_mydsl_lambda_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Define_strategy)
@settings(max_examples=50)
def test_mydsl_define_instantiation(instance):
    assert isinstance(instance, myDsl_Define)



@given(instance=myDsl_Define_strategy)
def test_mydsl_define_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Expression)



@given(instance=myDsl_Expression_strategy)
def test_mydsl_expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
