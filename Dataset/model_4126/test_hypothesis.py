import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    assignment2::ExpMD,
    assignment2::ExpPM,
    assignment2::EObject,
    ExpMinusPlus,
    assignment2::ExpMultDiv,
    assignment2::ExpMinusPlus,
    assignment2::MathExp,
    assignment2::Model,
    ExpMD,
    assignment2::Div,
    assignment2::Mult,
    ExpPM,
    assignment2::Minus,
    assignment2::Plus,
    Primary,
    assignment2::Number,
    assignment2::Parenthesis,
    ExpMultDiv,
    assignment2::Exp,
    assignment2::Primary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_assignment2::expmd_is_not_abstract():
    assert not inspect.isabstract(assignment2::ExpMD)


def test_assignment2::expmd_constructor_exists():
    assert callable(assignment2::ExpMD.__init__)


def test_assignment2::expmd_constructor_args():
    sig = inspect.signature(assignment2::ExpMD.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::exppm_is_not_abstract():
    assert not inspect.isabstract(assignment2::ExpPM)


def test_assignment2::exppm_constructor_exists():
    assert callable(assignment2::ExpPM.__init__)


def test_assignment2::exppm_constructor_args():
    sig = inspect.signature(assignment2::ExpPM.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::eobject_is_not_abstract():
    assert not inspect.isabstract(assignment2::EObject)


def test_assignment2::eobject_constructor_exists():
    assert callable(assignment2::EObject.__init__)


def test_assignment2::eobject_constructor_args():
    sig = inspect.signature(assignment2::EObject.__init__)
    params = list(sig.parameters.keys())



def test_expminusplus_is_not_abstract():
    assert not inspect.isabstract(ExpMinusPlus)


def test_expminusplus_constructor_exists():
    assert callable(ExpMinusPlus.__init__)


def test_expminusplus_constructor_args():
    sig = inspect.signature(ExpMinusPlus.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::expmultdiv_is_not_abstract():
    assert not inspect.isabstract(assignment2::ExpMultDiv)


def test_assignment2::expmultdiv_constructor_exists():
    assert callable(assignment2::ExpMultDiv.__init__)


def test_assignment2::expmultdiv_constructor_args():
    sig = inspect.signature(assignment2::ExpMultDiv.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::expminusplus_is_not_abstract():
    assert not inspect.isabstract(assignment2::ExpMinusPlus)


def test_assignment2::expminusplus_constructor_exists():
    assert callable(assignment2::ExpMinusPlus.__init__)


def test_assignment2::expminusplus_constructor_args():
    sig = inspect.signature(assignment2::ExpMinusPlus.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::mathexp_is_not_abstract():
    assert not inspect.isabstract(assignment2::MathExp)


def test_assignment2::mathexp_constructor_exists():
    assert callable(assignment2::MathExp.__init__)


def test_assignment2::mathexp_constructor_args():
    sig = inspect.signature(assignment2::MathExp.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::model_is_not_abstract():
    assert not inspect.isabstract(assignment2::Model)


def test_assignment2::model_constructor_exists():
    assert callable(assignment2::Model.__init__)


def test_assignment2::model_constructor_args():
    sig = inspect.signature(assignment2::Model.__init__)
    params = list(sig.parameters.keys())



def test_expmd_is_not_abstract():
    assert not inspect.isabstract(ExpMD)


def test_expmd_constructor_exists():
    assert callable(ExpMD.__init__)


def test_expmd_constructor_args():
    sig = inspect.signature(ExpMD.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::div_is_not_abstract():
    assert not inspect.isabstract(assignment2::Div)


def test_assignment2::div_constructor_exists():
    assert callable(assignment2::Div.__init__)


def test_assignment2::div_constructor_args():
    sig = inspect.signature(assignment2::Div.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::mult_is_not_abstract():
    assert not inspect.isabstract(assignment2::Mult)


def test_assignment2::mult_constructor_exists():
    assert callable(assignment2::Mult.__init__)


def test_assignment2::mult_constructor_args():
    sig = inspect.signature(assignment2::Mult.__init__)
    params = list(sig.parameters.keys())



def test_exppm_is_not_abstract():
    assert not inspect.isabstract(ExpPM)


def test_exppm_constructor_exists():
    assert callable(ExpPM.__init__)


def test_exppm_constructor_args():
    sig = inspect.signature(ExpPM.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::minus_is_not_abstract():
    assert not inspect.isabstract(assignment2::Minus)


def test_assignment2::minus_constructor_exists():
    assert callable(assignment2::Minus.__init__)


def test_assignment2::minus_constructor_args():
    sig = inspect.signature(assignment2::Minus.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::plus_is_not_abstract():
    assert not inspect.isabstract(assignment2::Plus)


def test_assignment2::plus_constructor_exists():
    assert callable(assignment2::Plus.__init__)


def test_assignment2::plus_constructor_args():
    sig = inspect.signature(assignment2::Plus.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::number_is_not_abstract():
    assert not inspect.isabstract(assignment2::Number)


def test_assignment2::number_constructor_exists():
    assert callable(assignment2::Number.__init__)


def test_assignment2::number_constructor_args():
    sig = inspect.signature(assignment2::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_assignment2::number_has_value():
    assert hasattr(assignment2::Number, "value")
    descriptor = None
    for klass in assignment2::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_assignment2::parenthesis_is_not_abstract():
    assert not inspect.isabstract(assignment2::Parenthesis)


def test_assignment2::parenthesis_constructor_exists():
    assert callable(assignment2::Parenthesis.__init__)


def test_assignment2::parenthesis_constructor_args():
    sig = inspect.signature(assignment2::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_expmultdiv_is_not_abstract():
    assert not inspect.isabstract(ExpMultDiv)


def test_expmultdiv_constructor_exists():
    assert callable(ExpMultDiv.__init__)


def test_expmultdiv_constructor_args():
    sig = inspect.signature(ExpMultDiv.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::exp_is_not_abstract():
    assert not inspect.isabstract(assignment2::Exp)


def test_assignment2::exp_constructor_exists():
    assert callable(assignment2::Exp.__init__)


def test_assignment2::exp_constructor_args():
    sig = inspect.signature(assignment2::Exp.__init__)
    params = list(sig.parameters.keys())



def test_assignment2::primary_is_not_abstract():
    assert not inspect.isabstract(assignment2::Primary)


def test_assignment2::primary_constructor_exists():
    assert callable(assignment2::Primary.__init__)


def test_assignment2::primary_constructor_args():
    sig = inspect.signature(assignment2::Primary.__init__)
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
assignment2::ExpMD_strategy = st.builds(
    assignment2::ExpMD,
)
assignment2::ExpPM_strategy = st.builds(
    assignment2::ExpPM,
)
assignment2::EObject_strategy = st.builds(
    assignment2::EObject,
)
ExpMinusPlus_strategy = st.builds(
    ExpMinusPlus,
)
assignment2::ExpMultDiv_strategy = st.builds(
    assignment2::ExpMultDiv,
)
assignment2::ExpMinusPlus_strategy = st.builds(
    assignment2::ExpMinusPlus,
)
assignment2::MathExp_strategy = st.builds(
    assignment2::MathExp,
)
assignment2::Model_strategy = st.builds(
    assignment2::Model,
)
ExpMD_strategy = st.builds(
    ExpMD,
)
assignment2::Div_strategy = st.builds(
    assignment2::Div,
)
assignment2::Mult_strategy = st.builds(
    assignment2::Mult,
)
ExpPM_strategy = st.builds(
    ExpPM,
)
assignment2::Minus_strategy = st.builds(
    assignment2::Minus,
)
assignment2::Plus_strategy = st.builds(
    assignment2::Plus,
)
Primary_strategy = st.builds(
    Primary,
)
assignment2::Number_strategy = st.builds(
    assignment2::Number,
    value=
        st.integers()
)
assignment2::Parenthesis_strategy = st.builds(
    assignment2::Parenthesis,
)
ExpMultDiv_strategy = st.builds(
    ExpMultDiv,
)
assignment2::Exp_strategy = st.builds(
    assignment2::Exp,
)
assignment2::Primary_strategy = st.builds(
    assignment2::Primary,
)

@given(instance=assignment2::ExpMD_strategy)
@settings(max_examples=50)
def test_assignment2::expmd_instantiation(instance):
    assert isinstance(instance, assignment2::ExpMD)

@given(instance=assignment2::ExpPM_strategy)
@settings(max_examples=50)
def test_assignment2::exppm_instantiation(instance):
    assert isinstance(instance, assignment2::ExpPM)

@given(instance=assignment2::EObject_strategy)
@settings(max_examples=50)
def test_assignment2::eobject_instantiation(instance):
    assert isinstance(instance, assignment2::EObject)

@given(instance=ExpMinusPlus_strategy)
@settings(max_examples=50)
def test_expminusplus_instantiation(instance):
    assert isinstance(instance, ExpMinusPlus)

@given(instance=assignment2::ExpMultDiv_strategy)
@settings(max_examples=50)
def test_assignment2::expmultdiv_instantiation(instance):
    assert isinstance(instance, assignment2::ExpMultDiv)

@given(instance=assignment2::ExpMinusPlus_strategy)
@settings(max_examples=50)
def test_assignment2::expminusplus_instantiation(instance):
    assert isinstance(instance, assignment2::ExpMinusPlus)

@given(instance=assignment2::MathExp_strategy)
@settings(max_examples=50)
def test_assignment2::mathexp_instantiation(instance):
    assert isinstance(instance, assignment2::MathExp)

@given(instance=assignment2::Model_strategy)
@settings(max_examples=50)
def test_assignment2::model_instantiation(instance):
    assert isinstance(instance, assignment2::Model)

@given(instance=ExpMD_strategy)
@settings(max_examples=50)
def test_expmd_instantiation(instance):
    assert isinstance(instance, ExpMD)

@given(instance=assignment2::Div_strategy)
@settings(max_examples=50)
def test_assignment2::div_instantiation(instance):
    assert isinstance(instance, assignment2::Div)

@given(instance=assignment2::Mult_strategy)
@settings(max_examples=50)
def test_assignment2::mult_instantiation(instance):
    assert isinstance(instance, assignment2::Mult)

@given(instance=ExpPM_strategy)
@settings(max_examples=50)
def test_exppm_instantiation(instance):
    assert isinstance(instance, ExpPM)

@given(instance=assignment2::Minus_strategy)
@settings(max_examples=50)
def test_assignment2::minus_instantiation(instance):
    assert isinstance(instance, assignment2::Minus)

@given(instance=assignment2::Plus_strategy)
@settings(max_examples=50)
def test_assignment2::plus_instantiation(instance):
    assert isinstance(instance, assignment2::Plus)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=assignment2::Number_strategy)
@settings(max_examples=50)
def test_assignment2::number_instantiation(instance):
    assert isinstance(instance, assignment2::Number)

@given(instance=assignment2::Number_strategy)
def test_assignment2::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=assignment2::Number_strategy)
def test_assignment2::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=assignment2::Parenthesis_strategy)
@settings(max_examples=50)
def test_assignment2::parenthesis_instantiation(instance):
    assert isinstance(instance, assignment2::Parenthesis)

@given(instance=ExpMultDiv_strategy)
@settings(max_examples=50)
def test_expmultdiv_instantiation(instance):
    assert isinstance(instance, ExpMultDiv)

@given(instance=assignment2::Exp_strategy)
@settings(max_examples=50)
def test_assignment2::exp_instantiation(instance):
    assert isinstance(instance, assignment2::Exp)

@given(instance=assignment2::Primary_strategy)
@settings(max_examples=50)
def test_assignment2::primary_instantiation(instance):
    assert isinstance(instance, assignment2::Primary)
