import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Condition,
    BoolExpr,
    calculatrice_Boolean,
    Calc,
    calculatrice_Condition,
    calculatrice_CalcExpr,
    calculatrice_BoolExpr,
    calculatrice_Calc,
    calculatrice_Calculatrice,
    CalcExpr,
    calculatrice_VarCall,
    calculatrice_Number,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_boolexpr_is_not_abstract():
    assert not inspect.isabstract(BoolExpr)


def test_boolexpr_constructor_exists():
    assert callable(BoolExpr.__init__)


def test_boolexpr_constructor_args():
    sig = inspect.signature(BoolExpr.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice_boolean_is_not_abstract():
    assert not inspect.isabstract(calculatrice_Boolean)


def test_calculatrice_boolean_constructor_exists():
    assert callable(calculatrice_Boolean.__init__)


def test_calculatrice_boolean_constructor_args():
    sig = inspect.signature(calculatrice_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "BoolValue" in params, "Missing parameter 'BoolValue'"

def test_calculatrice_boolean_has_BoolValue():
    assert hasattr(calculatrice_Boolean, "BoolValue")
    descriptor = None
    for klass in calculatrice_Boolean.__mro__:
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



def test_calculatrice_condition_is_not_abstract():
    assert not inspect.isabstract(calculatrice_Condition)


def test_calculatrice_condition_constructor_exists():
    assert callable(calculatrice_Condition.__init__)


def test_calculatrice_condition_constructor_args():
    sig = inspect.signature(calculatrice_Condition.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice_calcexpr_is_not_abstract():
    assert not inspect.isabstract(calculatrice_CalcExpr)


def test_calculatrice_calcexpr_constructor_exists():
    assert callable(calculatrice_CalcExpr.__init__)


def test_calculatrice_calcexpr_constructor_args():
    sig = inspect.signature(calculatrice_CalcExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_calculatrice_calcexpr_has_op():
    assert hasattr(calculatrice_CalcExpr, "op")
    descriptor = None
    for klass in calculatrice_CalcExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice_boolexpr_is_not_abstract():
    assert not inspect.isabstract(calculatrice_BoolExpr)


def test_calculatrice_boolexpr_constructor_exists():
    assert callable(calculatrice_BoolExpr.__init__)


def test_calculatrice_boolexpr_constructor_args():
    sig = inspect.signature(calculatrice_BoolExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_calculatrice_boolexpr_has_op():
    assert hasattr(calculatrice_BoolExpr, "op")
    descriptor = None
    for klass in calculatrice_BoolExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice_calc_is_not_abstract():
    assert not inspect.isabstract(calculatrice_Calc)


def test_calculatrice_calc_constructor_exists():
    assert callable(calculatrice_Calc.__init__)


def test_calculatrice_calc_constructor_args():
    sig = inspect.signature(calculatrice_Calc.__init__)
    params = list(sig.parameters.keys())
    assert "boolName" in params, "Missing parameter 'boolName'"
    assert "decl" in params, "Missing parameter 'decl'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_calculatrice_calc_has_boolName():
    assert hasattr(calculatrice_Calc, "boolName")
    descriptor = None
    for klass in calculatrice_Calc.__mro__:
        if "boolName" in klass.__dict__:
            descriptor = klass.__dict__["boolName"]
            break
    assert isinstance(descriptor, property)

def test_calculatrice_calc_has_decl():
    assert hasattr(calculatrice_Calc, "decl")
    descriptor = None
    for klass in calculatrice_Calc.__mro__:
        if "decl" in klass.__dict__:
            descriptor = klass.__dict__["decl"]
            break
    assert isinstance(descriptor, property)

def test_calculatrice_calc_has_varName():
    assert hasattr(calculatrice_Calc, "varName")
    descriptor = None
    for klass in calculatrice_Calc.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice_calculatrice_is_not_abstract():
    assert not inspect.isabstract(calculatrice_Calculatrice)


def test_calculatrice_calculatrice_constructor_exists():
    assert callable(calculatrice_Calculatrice.__init__)


def test_calculatrice_calculatrice_constructor_args():
    sig = inspect.signature(calculatrice_Calculatrice.__init__)
    params = list(sig.parameters.keys())



def test_calcexpr_is_not_abstract():
    assert not inspect.isabstract(CalcExpr)


def test_calcexpr_constructor_exists():
    assert callable(CalcExpr.__init__)


def test_calcexpr_constructor_args():
    sig = inspect.signature(CalcExpr.__init__)
    params = list(sig.parameters.keys())



def test_calculatrice_varcall_is_not_abstract():
    assert not inspect.isabstract(calculatrice_VarCall)


def test_calculatrice_varcall_constructor_exists():
    assert callable(calculatrice_VarCall.__init__)


def test_calculatrice_varcall_constructor_args():
    sig = inspect.signature(calculatrice_VarCall.__init__)
    params = list(sig.parameters.keys())
    assert "varCall" in params, "Missing parameter 'varCall'"

def test_calculatrice_varcall_has_varCall():
    assert hasattr(calculatrice_VarCall, "varCall")
    descriptor = None
    for klass in calculatrice_VarCall.__mro__:
        if "varCall" in klass.__dict__:
            descriptor = klass.__dict__["varCall"]
            break
    assert isinstance(descriptor, property)



def test_calculatrice_number_is_not_abstract():
    assert not inspect.isabstract(calculatrice_Number)


def test_calculatrice_number_constructor_exists():
    assert callable(calculatrice_Number.__init__)


def test_calculatrice_number_constructor_args():
    sig = inspect.signature(calculatrice_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "neg" in params, "Missing parameter 'neg'"

def test_calculatrice_number_has_value():
    assert hasattr(calculatrice_Number, "value")
    descriptor = None
    for klass in calculatrice_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_calculatrice_number_has_neg():
    assert hasattr(calculatrice_Number, "neg")
    descriptor = None
    for klass in calculatrice_Number.__mro__:
        if "neg" in klass.__dict__:
            descriptor = klass.__dict__["neg"]
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
Condition_strategy = st.builds(
    Condition,
)
BoolExpr_strategy = st.builds(
    BoolExpr,
)
calculatrice_Boolean_strategy = st.builds(
    calculatrice_Boolean,
    BoolValue=
        safe_text
)
Calc_strategy = st.builds(
    Calc,
)
calculatrice_Condition_strategy = st.builds(
    calculatrice_Condition,
)
calculatrice_CalcExpr_strategy = st.builds(
    calculatrice_CalcExpr,
    op=
        safe_text
)
calculatrice_BoolExpr_strategy = st.builds(
    calculatrice_BoolExpr,
    op=
        safe_text
)
calculatrice_Calc_strategy = st.builds(
    calculatrice_Calc,
    boolName=
        safe_text,
    decl=
        st.booleans(),
    varName=
        safe_text
)
calculatrice_Calculatrice_strategy = st.builds(
    calculatrice_Calculatrice,
)
CalcExpr_strategy = st.builds(
    CalcExpr,
)
calculatrice_VarCall_strategy = st.builds(
    calculatrice_VarCall,
    varCall=
        safe_text
)
calculatrice_Number_strategy = st.builds(
    calculatrice_Number,
    value=
        st.integers(),
    neg=
        st.booleans()
)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=BoolExpr_strategy)
@settings(max_examples=50)
def test_boolexpr_instantiation(instance):
    assert isinstance(instance, BoolExpr)

@given(instance=calculatrice_Boolean_strategy)
@settings(max_examples=50)
def test_calculatrice_boolean_instantiation(instance):
    assert isinstance(instance, calculatrice_Boolean)



@given(instance=calculatrice_Boolean_strategy)
def test_calculatrice_boolean_BoolValue_setter(instance):
    original = instance.BoolValue
    instance.BoolValue = original
    assert instance.BoolValue == original

@given(instance=Calc_strategy)
@settings(max_examples=50)
def test_calc_instantiation(instance):
    assert isinstance(instance, Calc)

@given(instance=calculatrice_Condition_strategy)
@settings(max_examples=50)
def test_calculatrice_condition_instantiation(instance):
    assert isinstance(instance, calculatrice_Condition)

@given(instance=calculatrice_CalcExpr_strategy)
@settings(max_examples=50)
def test_calculatrice_calcexpr_instantiation(instance):
    assert isinstance(instance, calculatrice_CalcExpr)



@given(instance=calculatrice_CalcExpr_strategy)
def test_calculatrice_calcexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=calculatrice_BoolExpr_strategy)
@settings(max_examples=50)
def test_calculatrice_boolexpr_instantiation(instance):
    assert isinstance(instance, calculatrice_BoolExpr)



@given(instance=calculatrice_BoolExpr_strategy)
def test_calculatrice_boolexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=calculatrice_Calc_strategy)
@settings(max_examples=50)
def test_calculatrice_calc_instantiation(instance):
    assert isinstance(instance, calculatrice_Calc)



@given(instance=calculatrice_Calc_strategy)
def test_calculatrice_calc_boolName_setter(instance):
    original = instance.boolName
    instance.boolName = original
    assert instance.boolName == original



@given(instance=calculatrice_Calc_strategy)
def test_calculatrice_calc_decl_setter(instance):
    original = instance.decl
    instance.decl = original
    assert instance.decl == original



@given(instance=calculatrice_Calc_strategy)
def test_calculatrice_calc_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=calculatrice_Calculatrice_strategy)
@settings(max_examples=50)
def test_calculatrice_calculatrice_instantiation(instance):
    assert isinstance(instance, calculatrice_Calculatrice)

@given(instance=CalcExpr_strategy)
@settings(max_examples=50)
def test_calcexpr_instantiation(instance):
    assert isinstance(instance, CalcExpr)

@given(instance=calculatrice_VarCall_strategy)
@settings(max_examples=50)
def test_calculatrice_varcall_instantiation(instance):
    assert isinstance(instance, calculatrice_VarCall)



@given(instance=calculatrice_VarCall_strategy)
def test_calculatrice_varcall_varCall_setter(instance):
    original = instance.varCall
    instance.varCall = original
    assert instance.varCall == original

@given(instance=calculatrice_Number_strategy)
@settings(max_examples=50)
def test_calculatrice_number_instantiation(instance):
    assert isinstance(instance, calculatrice_Number)



@given(instance=calculatrice_Number_strategy)
def test_calculatrice_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=calculatrice_Number_strategy)
def test_calculatrice_number_neg_setter(instance):
    original = instance.neg
    instance.neg = original
    assert instance.neg == original
