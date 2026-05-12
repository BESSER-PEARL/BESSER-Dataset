import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Instance,
    myDsl_Method,
    myDsl_Instance,
    myDsl_Classs,
    Expression,
    myDsl_Minus,
    myDsl_Let,
    myDsl_Var,
    myDsl_Div,
    myDsl_Num,
    myDsl_Mult,
    myDsl_Plus,
    myDsl_Expression,
    myDsl_MathExp,
    myDsl_Parameter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_method_is_not_abstract():
    assert not inspect.isabstract(myDsl_Method)


def test_mydsl_method_constructor_exists():
    assert callable(myDsl_Method.__init__)


def test_mydsl_method_constructor_args():
    sig = inspect.signature(myDsl_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_method_has_name():
    assert hasattr(myDsl_Method, "name")
    descriptor = None
    for klass in myDsl_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_instance_is_not_abstract():
    assert not inspect.isabstract(myDsl_Instance)


def test_mydsl_instance_constructor_exists():
    assert callable(myDsl_Instance.__init__)


def test_mydsl_instance_constructor_args():
    sig = inspect.signature(myDsl_Instance.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_classs_is_not_abstract():
    assert not inspect.isabstract(myDsl_Classs)


def test_mydsl_classs_constructor_exists():
    assert callable(myDsl_Classs.__init__)


def test_mydsl_classs_constructor_args():
    sig = inspect.signature(myDsl_Classs.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_minus_is_not_abstract():
    assert not inspect.isabstract(myDsl_Minus)


def test_mydsl_minus_constructor_exists():
    assert callable(myDsl_Minus.__init__)


def test_mydsl_minus_constructor_args():
    sig = inspect.signature(myDsl_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_let_is_not_abstract():
    assert not inspect.isabstract(myDsl_Let)


def test_mydsl_let_constructor_exists():
    assert callable(myDsl_Let.__init__)


def test_mydsl_let_constructor_args():
    sig = inspect.signature(myDsl_Let.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_let_has_id():
    assert hasattr(myDsl_Let, "id")
    descriptor = None
    for klass in myDsl_Let.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_var_is_not_abstract():
    assert not inspect.isabstract(myDsl_Var)


def test_mydsl_var_constructor_exists():
    assert callable(myDsl_Var.__init__)


def test_mydsl_var_constructor_args():
    sig = inspect.signature(myDsl_Var.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_var_has_id():
    assert hasattr(myDsl_Var, "id")
    descriptor = None
    for klass in myDsl_Var.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_div_is_not_abstract():
    assert not inspect.isabstract(myDsl_Div)


def test_mydsl_div_constructor_exists():
    assert callable(myDsl_Div.__init__)


def test_mydsl_div_constructor_args():
    sig = inspect.signature(myDsl_Div.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_num_is_not_abstract():
    assert not inspect.isabstract(myDsl_Num)


def test_mydsl_num_constructor_exists():
    assert callable(myDsl_Num.__init__)


def test_mydsl_num_constructor_args():
    sig = inspect.signature(myDsl_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_num_has_value():
    assert hasattr(myDsl_Num, "value")
    descriptor = None
    for klass in myDsl_Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_mult_is_not_abstract():
    assert not inspect.isabstract(myDsl_Mult)


def test_mydsl_mult_constructor_exists():
    assert callable(myDsl_Mult.__init__)


def test_mydsl_mult_constructor_args():
    sig = inspect.signature(myDsl_Mult.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_plus_is_not_abstract():
    assert not inspect.isabstract(myDsl_Plus)


def test_mydsl_plus_constructor_exists():
    assert callable(myDsl_Plus.__init__)


def test_mydsl_plus_constructor_args():
    sig = inspect.signature(myDsl_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_Expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_mathexp_is_not_abstract():
    assert not inspect.isabstract(myDsl_MathExp)


def test_mydsl_mathexp_constructor_exists():
    assert callable(myDsl_MathExp.__init__)


def test_mydsl_mathexp_constructor_args():
    sig = inspect.signature(myDsl_MathExp.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mydsl_mathexp_has_text():
    assert hasattr(myDsl_MathExp, "text")
    descriptor = None
    for klass in myDsl_MathExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_parameter_is_not_abstract():
    assert not inspect.isabstract(myDsl_Parameter)


def test_mydsl_parameter_constructor_exists():
    assert callable(myDsl_Parameter.__init__)


def test_mydsl_parameter_constructor_args():
    sig = inspect.signature(myDsl_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_parameter_has_name():
    assert hasattr(myDsl_Parameter, "name")
    descriptor = None
    for klass in myDsl_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
Instance_strategy = st.builds(
    Instance,
)
myDsl_Method_strategy = st.builds(
    myDsl_Method,
    name=
        safe_text
)
myDsl_Instance_strategy = st.builds(
    myDsl_Instance,
)
myDsl_Classs_strategy = st.builds(
    myDsl_Classs,
)
Expression_strategy = st.builds(
    Expression,
)
myDsl_Minus_strategy = st.builds(
    myDsl_Minus,
)
myDsl_Let_strategy = st.builds(
    myDsl_Let,
    id=
        safe_text
)
myDsl_Var_strategy = st.builds(
    myDsl_Var,
    id=
        safe_text
)
myDsl_Div_strategy = st.builds(
    myDsl_Div,
)
myDsl_Num_strategy = st.builds(
    myDsl_Num,
    value=
        st.integers()
)
myDsl_Mult_strategy = st.builds(
    myDsl_Mult,
)
myDsl_Plus_strategy = st.builds(
    myDsl_Plus,
)
myDsl_Expression_strategy = st.builds(
    myDsl_Expression,
)
myDsl_MathExp_strategy = st.builds(
    myDsl_MathExp,
    text=
        safe_text
)
myDsl_Parameter_strategy = st.builds(
    myDsl_Parameter,
    name=
        safe_text
)

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=myDsl_Method_strategy)
@settings(max_examples=50)
def test_mydsl_method_instantiation(instance):
    assert isinstance(instance, myDsl_Method)



@given(instance=myDsl_Method_strategy)
def test_mydsl_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Instance_strategy)
@settings(max_examples=50)
def test_mydsl_instance_instantiation(instance):
    assert isinstance(instance, myDsl_Instance)

@given(instance=myDsl_Classs_strategy)
@settings(max_examples=50)
def test_mydsl_classs_instantiation(instance):
    assert isinstance(instance, myDsl_Classs)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=myDsl_Minus_strategy)
@settings(max_examples=50)
def test_mydsl_minus_instantiation(instance):
    assert isinstance(instance, myDsl_Minus)

@given(instance=myDsl_Let_strategy)
@settings(max_examples=50)
def test_mydsl_let_instantiation(instance):
    assert isinstance(instance, myDsl_Let)



@given(instance=myDsl_Let_strategy)
def test_mydsl_let_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_Var_strategy)
@settings(max_examples=50)
def test_mydsl_var_instantiation(instance):
    assert isinstance(instance, myDsl_Var)



@given(instance=myDsl_Var_strategy)
def test_mydsl_var_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_Div_strategy)
@settings(max_examples=50)
def test_mydsl_div_instantiation(instance):
    assert isinstance(instance, myDsl_Div)

@given(instance=myDsl_Num_strategy)
@settings(max_examples=50)
def test_mydsl_num_instantiation(instance):
    assert isinstance(instance, myDsl_Num)



@given(instance=myDsl_Num_strategy)
def test_mydsl_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_Mult_strategy)
@settings(max_examples=50)
def test_mydsl_mult_instantiation(instance):
    assert isinstance(instance, myDsl_Mult)

@given(instance=myDsl_Plus_strategy)
@settings(max_examples=50)
def test_mydsl_plus_instantiation(instance):
    assert isinstance(instance, myDsl_Plus)

@given(instance=myDsl_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Expression)

@given(instance=myDsl_MathExp_strategy)
@settings(max_examples=50)
def test_mydsl_mathexp_instantiation(instance):
    assert isinstance(instance, myDsl_MathExp)



@given(instance=myDsl_MathExp_strategy)
def test_mydsl_mathexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=myDsl_Parameter_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_instantiation(instance):
    assert isinstance(instance, myDsl_Parameter)



@given(instance=myDsl_Parameter_strategy)
def test_mydsl_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
