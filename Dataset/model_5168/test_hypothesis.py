import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BoolExpr,
    calculatrice::Boolean,
    Calc,
    calculatrice::Condition,
    calculatrice::CalcExpr,
    calculatrice::Calc,
    calculatrice::Calculatrice,
    CalcExpr,
    calculatrice::VarCall,
    calculatrice::Number,
    Condition,
    calculatrice::BoolExpr,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_boolexpr_is_not_abstract():
    assert not inspect.isabstract(BoolExpr)


def test_boolexpr_constructor_exists():
    assert callable(BoolExpr.__init__)


def test_boolexpr_constructor_args():
    sig = inspect.signature(BoolExpr.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice::boolean_is_not_abstract():
    assert not inspect.isabstract(calculatrice::Boolean)


def test_calculatrice::boolean_constructor_exists():
    assert callable(calculatrice::Boolean.__init__)


def test_calculatrice::boolean_constructor_args():
    sig = inspect.signature(calculatrice::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "BoolValue" in params, "Missing parameter 'BoolValue'"

def test_calculatrice::boolean_has_BoolValue():
    assert hasattr(calculatrice::Boolean, "BoolValue")
    descriptor = None
    for klass in calculatrice::Boolean.__mro__:
        if "BoolValue" in klass.__dict__:
            descriptor = klass.__dict__["BoolValue"]
            break
    assert isinstance(descriptor, property)



def test_calc_is_not_abstract():
    assert not inspect.isabstract(Calc)


def test_calc_constructor_exists():
    assert callable(Calc.__init__)


def test_calc_constructor_args():
    sig = inspect.signature(Calc.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice::condition_is_not_abstract():
    assert not inspect.isabstract(calculatrice::Condition)


def test_calculatrice::condition_constructor_exists():
    assert callable(calculatrice::Condition.__init__)


def test_calculatrice::condition_constructor_args():
    sig = inspect.signature(calculatrice::Condition.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice::calcexpr_is_not_abstract():
    assert not inspect.isabstract(calculatrice::CalcExpr)


def test_calculatrice::calcexpr_constructor_exists():
    assert callable(calculatrice::CalcExpr.__init__)


def test_calculatrice::calcexpr_constructor_args():
    sig = inspect.signature(calculatrice::CalcExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_calculatrice::calcexpr_has_op():
    assert hasattr(calculatrice::CalcExpr, "op")
    descriptor = None
    for klass in calculatrice::CalcExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice::calc_is_not_abstract():
    assert not inspect.isabstract(calculatrice::Calc)


def test_calculatrice::calc_constructor_exists():
    assert callable(calculatrice::Calc.__init__)


def test_calculatrice::calc_constructor_args():
    sig = inspect.signature(calculatrice::Calc.__init__)
    params = list(sig.parameters.keys())
    assert "boolName" in params, "Missing parameter 'boolName'"
    assert "varName" in params, "Missing parameter 'varName'"
    assert "decl" in params, "Missing parameter 'decl'"

def test_calculatrice::calc_has_boolName():
    assert hasattr(calculatrice::Calc, "boolName")
    descriptor = None
    for klass in calculatrice::Calc.__mro__:
        if "boolName" in klass.__dict__:
            descriptor = klass.__dict__["boolName"]
            break
    assert isinstance(descriptor, property)

def test_calculatrice::calc_has_varName():
    assert hasattr(calculatrice::Calc, "varName")
    descriptor = None
    for klass in calculatrice::Calc.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_calculatrice::calc_has_decl():
    assert hasattr(calculatrice::Calc, "decl")
    descriptor = None
    for klass in calculatrice::Calc.__mro__:
        if "decl" in klass.__dict__:
            descriptor = klass.__dict__["decl"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice::calculatrice_is_not_abstract():
    assert not inspect.isabstract(calculatrice::Calculatrice)


def test_calculatrice::calculatrice_constructor_exists():
    assert callable(calculatrice::Calculatrice.__init__)


def test_calculatrice::calculatrice_constructor_args():
    sig = inspect.signature(calculatrice::Calculatrice.__init__)
    params = list(sig.parameters.keys())



def test_calcexpr_is_not_abstract():
    assert not inspect.isabstract(CalcExpr)


def test_calcexpr_constructor_exists():
    assert callable(CalcExpr.__init__)


def test_calcexpr_constructor_args():
    sig = inspect.signature(CalcExpr.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice::varcall_is_not_abstract():
    assert not inspect.isabstract(calculatrice::VarCall)


def test_calculatrice::varcall_constructor_exists():
    assert callable(calculatrice::VarCall.__init__)


def test_calculatrice::varcall_constructor_args():
    sig = inspect.signature(calculatrice::VarCall.__init__)
    params = list(sig.parameters.keys())
    assert "varCall" in params, "Missing parameter 'varCall'"

def test_calculatrice::varcall_has_varCall():
    assert hasattr(calculatrice::VarCall, "varCall")
    descriptor = None
    for klass in calculatrice::VarCall.__mro__:
        if "varCall" in klass.__dict__:
            descriptor = klass.__dict__["varCall"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice::number_is_not_abstract():
    assert not inspect.isabstract(calculatrice::Number)


def test_calculatrice::number_constructor_exists():
    assert callable(calculatrice::Number.__init__)


def test_calculatrice::number_constructor_args():
    sig = inspect.signature(calculatrice::Number.__init__)
    params = list(sig.parameters.keys())
    assert "neg" in params, "Missing parameter 'neg'"
    assert "value" in params, "Missing parameter 'value'"

def test_calculatrice::number_has_neg():
    assert hasattr(calculatrice::Number, "neg")
    descriptor = None
    for klass in calculatrice::Number.__mro__:
        if "neg" in klass.__dict__:
            descriptor = klass.__dict__["neg"]
            break
    assert isinstance(descriptor, property)

def test_calculatrice::number_has_value():
    assert hasattr(calculatrice::Number, "value")
    descriptor = None
    for klass in calculatrice::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice::boolexpr_is_not_abstract():
    assert not inspect.isabstract(calculatrice::BoolExpr)


def test_calculatrice::boolexpr_constructor_exists():
    assert callable(calculatrice::BoolExpr.__init__)


def test_calculatrice::boolexpr_constructor_args():
    sig = inspect.signature(calculatrice::BoolExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_calculatrice::boolexpr_has_op():
    assert hasattr(calculatrice::BoolExpr, "op")
    descriptor = None
    for klass in calculatrice::BoolExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
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
BoolExpr_strategy = st.builds(
    BoolExpr,
)
calculatrice::Boolean_strategy = st.builds(
    calculatrice::Boolean,
    BoolValue=
        safe_text
)
Calc_strategy = st.builds(
    Calc,
)
calculatrice::Condition_strategy = st.builds(
    calculatrice::Condition,
)
calculatrice::CalcExpr_strategy = st.builds(
    calculatrice::CalcExpr,
    op=
        safe_text
)
calculatrice::Calc_strategy = st.builds(
    calculatrice::Calc,
    boolName=
        safe_text,
    varName=
        safe_text,
    decl=
        st.booleans()
)
calculatrice::Calculatrice_strategy = st.builds(
    calculatrice::Calculatrice,
)
CalcExpr_strategy = st.builds(
    CalcExpr,
)
calculatrice::VarCall_strategy = st.builds(
    calculatrice::VarCall,
    varCall=
        safe_text
)
calculatrice::Number_strategy = st.builds(
    calculatrice::Number,
    neg=
        st.booleans(),
    value=
        st.integers()
)
Condition_strategy = st.builds(
    Condition,
)
calculatrice::BoolExpr_strategy = st.builds(
    calculatrice::BoolExpr,
    op=
        safe_text
)

@given(instance=BoolExpr_strategy)
@settings(max_examples=50)
def test_boolexpr_instantiation(instance):
    assert isinstance(instance, BoolExpr)

@given(instance=calculatrice::Boolean_strategy)
@settings(max_examples=50)
def test_calculatrice::boolean_instantiation(instance):
    assert isinstance(instance, calculatrice::Boolean)

@given(instance=calculatrice::Boolean_strategy)
def test_calculatrice::boolean_BoolValue_type(instance):
    assert isinstance(instance.BoolValue, str)


@given(instance=calculatrice::Boolean_strategy)
def test_calculatrice::boolean_BoolValue_setter(instance):
    original = instance.BoolValue
    instance.BoolValue = original
    assert instance.BoolValue == original

@given(instance=Calc_strategy)
@settings(max_examples=50)
def test_calc_instantiation(instance):
    assert isinstance(instance, Calc)

@given(instance=calculatrice::Condition_strategy)
@settings(max_examples=50)
def test_calculatrice::condition_instantiation(instance):
    assert isinstance(instance, calculatrice::Condition)

@given(instance=calculatrice::CalcExpr_strategy)
@settings(max_examples=50)
def test_calculatrice::calcexpr_instantiation(instance):
    assert isinstance(instance, calculatrice::CalcExpr)

@given(instance=calculatrice::CalcExpr_strategy)
def test_calculatrice::calcexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=calculatrice::CalcExpr_strategy)
def test_calculatrice::calcexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=calculatrice::Calc_strategy)
@settings(max_examples=50)
def test_calculatrice::calc_instantiation(instance):
    assert isinstance(instance, calculatrice::Calc)

@given(instance=calculatrice::Calc_strategy)
def test_calculatrice::calc_boolName_type(instance):
    assert isinstance(instance.boolName, str)


@given(instance=calculatrice::Calc_strategy)
def test_calculatrice::calc_boolName_setter(instance):
    original = instance.boolName
    instance.boolName = original
    assert instance.boolName == original

@given(instance=calculatrice::Calc_strategy)
def test_calculatrice::calc_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=calculatrice::Calc_strategy)
def test_calculatrice::calc_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=calculatrice::Calc_strategy)
def test_calculatrice::calc_decl_type(instance):
    assert isinstance(instance.decl, bool)


@given(instance=calculatrice::Calc_strategy)
def test_calculatrice::calc_decl_setter(instance):
    original = instance.decl
    instance.decl = original
    assert instance.decl == original

@given(instance=calculatrice::Calculatrice_strategy)
@settings(max_examples=50)
def test_calculatrice::calculatrice_instantiation(instance):
    assert isinstance(instance, calculatrice::Calculatrice)

@given(instance=CalcExpr_strategy)
@settings(max_examples=50)
def test_calcexpr_instantiation(instance):
    assert isinstance(instance, CalcExpr)

@given(instance=calculatrice::VarCall_strategy)
@settings(max_examples=50)
def test_calculatrice::varcall_instantiation(instance):
    assert isinstance(instance, calculatrice::VarCall)

@given(instance=calculatrice::VarCall_strategy)
def test_calculatrice::varcall_varCall_type(instance):
    assert isinstance(instance.varCall, str)


@given(instance=calculatrice::VarCall_strategy)
def test_calculatrice::varcall_varCall_setter(instance):
    original = instance.varCall
    instance.varCall = original
    assert instance.varCall == original

@given(instance=calculatrice::Number_strategy)
@settings(max_examples=50)
def test_calculatrice::number_instantiation(instance):
    assert isinstance(instance, calculatrice::Number)

@given(instance=calculatrice::Number_strategy)
def test_calculatrice::number_neg_type(instance):
    assert isinstance(instance.neg, bool)


@given(instance=calculatrice::Number_strategy)
def test_calculatrice::number_neg_setter(instance):
    original = instance.neg
    instance.neg = original
    assert instance.neg == original

@given(instance=calculatrice::Number_strategy)
def test_calculatrice::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=calculatrice::Number_strategy)
def test_calculatrice::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=calculatrice::BoolExpr_strategy)
@settings(max_examples=50)
def test_calculatrice::boolexpr_instantiation(instance):
    assert isinstance(instance, calculatrice::BoolExpr)

@given(instance=calculatrice::BoolExpr_strategy)
def test_calculatrice::boolexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=calculatrice::BoolExpr_strategy)
def test_calculatrice::boolexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original
