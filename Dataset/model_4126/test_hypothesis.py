import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    assignment2_ExpMD,
    assignment2_ExpPM,
    assignment2_EObject,
    ExpMinusPlus,
    assignment2_ExpMultDiv,
    assignment2_ExpMinusPlus,
    assignment2_MathExp,
    assignment2_Model,
    ExpMD,
    assignment2_Div,
    assignment2_Mult,
    ExpPM,
    assignment2_Minus,
    assignment2_Plus,
    Primary,
    assignment2_Number,
    assignment2_Parenthesis,
    ExpMultDiv,
    assignment2_Exp,
    assignment2_Primary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_assignment2_expmd_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpMD)


def test_assignment2_expmd_constructor_exists():
    assert callable(assignment2_ExpMD.__init__)


def test_assignment2_expmd_constructor_args():
    sig = inspect.signature(assignment2_ExpMD.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_exppm_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpPM)


def test_assignment2_exppm_constructor_exists():
    assert callable(assignment2_ExpPM.__init__)


def test_assignment2_exppm_constructor_args():
    sig = inspect.signature(assignment2_ExpPM.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_eobject_is_not_abstract():
    assert not inspect.isabstract(assignment2_EObject)


def test_assignment2_eobject_constructor_exists():
    assert callable(assignment2_EObject.__init__)


def test_assignment2_eobject_constructor_args():
    sig = inspect.signature(assignment2_EObject.__init__)
    params = list(sig.parameters.keys())



def test_expminusplus_is_not_abstract():
    assert not inspect.isabstract(ExpMinusPlus)


def test_expminusplus_constructor_exists():
    assert callable(ExpMinusPlus.__init__)


def test_expminusplus_constructor_args():
    sig = inspect.signature(ExpMinusPlus.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_expmultdiv_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpMultDiv)


def test_assignment2_expmultdiv_constructor_exists():
    assert callable(assignment2_ExpMultDiv.__init__)


def test_assignment2_expmultdiv_constructor_args():
    sig = inspect.signature(assignment2_ExpMultDiv.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_expminusplus_is_not_abstract():
    assert not inspect.isabstract(assignment2_ExpMinusPlus)


def test_assignment2_expminusplus_constructor_exists():
    assert callable(assignment2_ExpMinusPlus.__init__)


def test_assignment2_expminusplus_constructor_args():
    sig = inspect.signature(assignment2_ExpMinusPlus.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_mathexp_is_not_abstract():
    assert not inspect.isabstract(assignment2_MathExp)


def test_assignment2_mathexp_constructor_exists():
    assert callable(assignment2_MathExp.__init__)


def test_assignment2_mathexp_constructor_args():
    sig = inspect.signature(assignment2_MathExp.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_model_is_not_abstract():
    assert not inspect.isabstract(assignment2_Model)


def test_assignment2_model_constructor_exists():
    assert callable(assignment2_Model.__init__)


def test_assignment2_model_constructor_args():
    sig = inspect.signature(assignment2_Model.__init__)
    params = list(sig.parameters.keys())



def test_expmd_is_not_abstract():
    assert not inspect.isabstract(ExpMD)


def test_expmd_constructor_exists():
    assert callable(ExpMD.__init__)


def test_expmd_constructor_args():
    sig = inspect.signature(ExpMD.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_div_is_not_abstract():
    assert not inspect.isabstract(assignment2_Div)


def test_assignment2_div_constructor_exists():
    assert callable(assignment2_Div.__init__)


def test_assignment2_div_constructor_args():
    sig = inspect.signature(assignment2_Div.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_mult_is_not_abstract():
    assert not inspect.isabstract(assignment2_Mult)


def test_assignment2_mult_constructor_exists():
    assert callable(assignment2_Mult.__init__)


def test_assignment2_mult_constructor_args():
    sig = inspect.signature(assignment2_Mult.__init__)
    params = list(sig.parameters.keys())



def test_exppm_is_not_abstract():
    assert not inspect.isabstract(ExpPM)


def test_exppm_constructor_exists():
    assert callable(ExpPM.__init__)


def test_exppm_constructor_args():
    sig = inspect.signature(ExpPM.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_minus_is_not_abstract():
    assert not inspect.isabstract(assignment2_Minus)


def test_assignment2_minus_constructor_exists():
    assert callable(assignment2_Minus.__init__)


def test_assignment2_minus_constructor_args():
    sig = inspect.signature(assignment2_Minus.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_plus_is_not_abstract():
    assert not inspect.isabstract(assignment2_Plus)


def test_assignment2_plus_constructor_exists():
    assert callable(assignment2_Plus.__init__)


def test_assignment2_plus_constructor_args():
    sig = inspect.signature(assignment2_Plus.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_number_is_not_abstract():
    assert not inspect.isabstract(assignment2_Number)


def test_assignment2_number_constructor_exists():
    assert callable(assignment2_Number.__init__)


def test_assignment2_number_constructor_args():
    sig = inspect.signature(assignment2_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_assignment2_number_has_value():
    assert hasattr(assignment2_Number, "value")
    descriptor = None
    for klass in assignment2_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_assignment2_parenthesis_is_not_abstract():
    assert not inspect.isabstract(assignment2_Parenthesis)


def test_assignment2_parenthesis_constructor_exists():
    assert callable(assignment2_Parenthesis.__init__)


def test_assignment2_parenthesis_constructor_args():
    sig = inspect.signature(assignment2_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_expmultdiv_is_not_abstract():
    assert not inspect.isabstract(ExpMultDiv)


def test_expmultdiv_constructor_exists():
    assert callable(ExpMultDiv.__init__)


def test_expmultdiv_constructor_args():
    sig = inspect.signature(ExpMultDiv.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_exp_is_not_abstract():
    assert not inspect.isabstract(assignment2_Exp)


def test_assignment2_exp_constructor_exists():
    assert callable(assignment2_Exp.__init__)


def test_assignment2_exp_constructor_args():
    sig = inspect.signature(assignment2_Exp.__init__)
    params = list(sig.parameters.keys())



def test_assignment2_primary_is_not_abstract():
    assert not inspect.isabstract(assignment2_Primary)


def test_assignment2_primary_constructor_exists():
    assert callable(assignment2_Primary.__init__)


def test_assignment2_primary_constructor_args():
    sig = inspect.signature(assignment2_Primary.__init__)
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
assignment2_ExpMD_strategy = st.builds(
    assignment2_ExpMD,
)
assignment2_ExpPM_strategy = st.builds(
    assignment2_ExpPM,
)
assignment2_EObject_strategy = st.builds(
    assignment2_EObject,
)
ExpMinusPlus_strategy = st.builds(
    ExpMinusPlus,
)
assignment2_ExpMultDiv_strategy = st.builds(
    assignment2_ExpMultDiv,
)
assignment2_ExpMinusPlus_strategy = st.builds(
    assignment2_ExpMinusPlus,
)
assignment2_MathExp_strategy = st.builds(
    assignment2_MathExp,
)
assignment2_Model_strategy = st.builds(
    assignment2_Model,
)
ExpMD_strategy = st.builds(
    ExpMD,
)
assignment2_Div_strategy = st.builds(
    assignment2_Div,
)
assignment2_Mult_strategy = st.builds(
    assignment2_Mult,
)
ExpPM_strategy = st.builds(
    ExpPM,
)
assignment2_Minus_strategy = st.builds(
    assignment2_Minus,
)
assignment2_Plus_strategy = st.builds(
    assignment2_Plus,
)
Primary_strategy = st.builds(
    Primary,
)
assignment2_Number_strategy = st.builds(
    assignment2_Number,
    value=
        st.integers()
)
assignment2_Parenthesis_strategy = st.builds(
    assignment2_Parenthesis,
)
ExpMultDiv_strategy = st.builds(
    ExpMultDiv,
)
assignment2_Exp_strategy = st.builds(
    assignment2_Exp,
)
assignment2_Primary_strategy = st.builds(
    assignment2_Primary,
)

@given(instance=assignment2_ExpMD_strategy)
@settings(max_examples=50)
def test_assignment2_expmd_instantiation(instance):
    assert isinstance(instance, assignment2_ExpMD)

@given(instance=assignment2_ExpPM_strategy)
@settings(max_examples=50)
def test_assignment2_exppm_instantiation(instance):
    assert isinstance(instance, assignment2_ExpPM)

@given(instance=assignment2_EObject_strategy)
@settings(max_examples=50)
def test_assignment2_eobject_instantiation(instance):
    assert isinstance(instance, assignment2_EObject)

@given(instance=ExpMinusPlus_strategy)
@settings(max_examples=50)
def test_expminusplus_instantiation(instance):
    assert isinstance(instance, ExpMinusPlus)

@given(instance=assignment2_ExpMultDiv_strategy)
@settings(max_examples=50)
def test_assignment2_expmultdiv_instantiation(instance):
    assert isinstance(instance, assignment2_ExpMultDiv)

@given(instance=assignment2_ExpMinusPlus_strategy)
@settings(max_examples=50)
def test_assignment2_expminusplus_instantiation(instance):
    assert isinstance(instance, assignment2_ExpMinusPlus)

@given(instance=assignment2_MathExp_strategy)
@settings(max_examples=50)
def test_assignment2_mathexp_instantiation(instance):
    assert isinstance(instance, assignment2_MathExp)

@given(instance=assignment2_Model_strategy)
@settings(max_examples=50)
def test_assignment2_model_instantiation(instance):
    assert isinstance(instance, assignment2_Model)

@given(instance=ExpMD_strategy)
@settings(max_examples=50)
def test_expmd_instantiation(instance):
    assert isinstance(instance, ExpMD)

@given(instance=assignment2_Div_strategy)
@settings(max_examples=50)
def test_assignment2_div_instantiation(instance):
    assert isinstance(instance, assignment2_Div)

@given(instance=assignment2_Mult_strategy)
@settings(max_examples=50)
def test_assignment2_mult_instantiation(instance):
    assert isinstance(instance, assignment2_Mult)

@given(instance=ExpPM_strategy)
@settings(max_examples=50)
def test_exppm_instantiation(instance):
    assert isinstance(instance, ExpPM)

@given(instance=assignment2_Minus_strategy)
@settings(max_examples=50)
def test_assignment2_minus_instantiation(instance):
    assert isinstance(instance, assignment2_Minus)

@given(instance=assignment2_Plus_strategy)
@settings(max_examples=50)
def test_assignment2_plus_instantiation(instance):
    assert isinstance(instance, assignment2_Plus)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=assignment2_Number_strategy)
@settings(max_examples=50)
def test_assignment2_number_instantiation(instance):
    assert isinstance(instance, assignment2_Number)



@given(instance=assignment2_Number_strategy)
def test_assignment2_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=assignment2_Parenthesis_strategy)
@settings(max_examples=50)
def test_assignment2_parenthesis_instantiation(instance):
    assert isinstance(instance, assignment2_Parenthesis)

@given(instance=ExpMultDiv_strategy)
@settings(max_examples=50)
def test_expmultdiv_instantiation(instance):
    assert isinstance(instance, ExpMultDiv)

@given(instance=assignment2_Exp_strategy)
@settings(max_examples=50)
def test_assignment2_exp_instantiation(instance):
    assert isinstance(instance, assignment2_Exp)

@given(instance=assignment2_Primary_strategy)
@settings(max_examples=50)
def test_assignment2_primary_instantiation(instance):
    assert isinstance(instance, assignment2_Primary)
