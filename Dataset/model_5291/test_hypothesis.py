import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryCalculator::BinaryCalculator,
    BinaryCalculator::Model,
    BitSeq,
    BinaryCalculator::Bit,
    BinaryCalculator::L,
    BinaryCalculator::Value,
    BinaryCalculator::BitSeq,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binarycalculator::binarycalculator_is_not_abstract():
    assert not inspect.isabstract(BinaryCalculator::BinaryCalculator)


def test_binarycalculator::binarycalculator_constructor_exists():
    assert callable(BinaryCalculator::BinaryCalculator.__init__)


def test_binarycalculator::binarycalculator_constructor_args():
    sig = inspect.signature(BinaryCalculator::BinaryCalculator.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_binarycalculator::binarycalculator_has_description():
    assert hasattr(BinaryCalculator::BinaryCalculator, "description")
    descriptor = None
    for klass in BinaryCalculator::BinaryCalculator.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_binarycalculator::model_is_not_abstract():
    assert not inspect.isabstract(BinaryCalculator::Model)


def test_binarycalculator::model_constructor_exists():
    assert callable(BinaryCalculator::Model.__init__)


def test_binarycalculator::model_constructor_args():
    sig = inspect.signature(BinaryCalculator::Model.__init__)
    params = list(sig.parameters.keys())



def test_bitseq_is_not_abstract():
    assert not inspect.isabstract(BitSeq)


def test_bitseq_constructor_exists():
    assert callable(BitSeq.__init__)


def test_bitseq_constructor_args():
    sig = inspect.signature(BitSeq.__init__)
    params = list(sig.parameters.keys())



def test_binarycalculator::bit_is_not_abstract():
    assert not inspect.isabstract(BinaryCalculator::Bit)


def test_binarycalculator::bit_constructor_exists():
    assert callable(BinaryCalculator::Bit.__init__)


def test_binarycalculator::bit_constructor_args():
    sig = inspect.signature(BinaryCalculator::Bit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_binarycalculator::bit_has_value():
    assert hasattr(BinaryCalculator::Bit, "value")
    descriptor = None
    for klass in BinaryCalculator::Bit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_binarycalculator::l_is_not_abstract():
    assert not inspect.isabstract(BinaryCalculator::L)


def test_binarycalculator::l_constructor_exists():
    assert callable(BinaryCalculator::L.__init__)


def test_binarycalculator::l_constructor_args():
    sig = inspect.signature(BinaryCalculator::L.__init__)
    params = list(sig.parameters.keys())



def test_binarycalculator::value_is_not_abstract():
    assert not inspect.isabstract(BinaryCalculator::Value)


def test_binarycalculator::value_constructor_exists():
    assert callable(BinaryCalculator::Value.__init__)


def test_binarycalculator::value_constructor_args():
    sig = inspect.signature(BinaryCalculator::Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_binarycalculator::value_has_value():
    assert hasattr(BinaryCalculator::Value, "value")
    descriptor = None
    for klass in BinaryCalculator::Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_binarycalculator::bitseq_is_not_abstract():
    assert not inspect.isabstract(BinaryCalculator::BitSeq)


def test_binarycalculator::bitseq_constructor_exists():
    assert callable(BinaryCalculator::BitSeq.__init__)


def test_binarycalculator::bitseq_constructor_args():
    sig = inspect.signature(BinaryCalculator::BitSeq.__init__)
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
BinaryCalculator::BinaryCalculator_strategy = st.builds(
    BinaryCalculator::BinaryCalculator,
    description=
        safe_text
)
BinaryCalculator::Model_strategy = st.builds(
    BinaryCalculator::Model,
)
BitSeq_strategy = st.builds(
    BitSeq,
)
BinaryCalculator::Bit_strategy = st.builds(
    BinaryCalculator::Bit,
    value=
        safe_text
)
BinaryCalculator::L_strategy = st.builds(
    BinaryCalculator::L,
)
BinaryCalculator::Value_strategy = st.builds(
    BinaryCalculator::Value,
    value=
        safe_text
)
BinaryCalculator::BitSeq_strategy = st.builds(
    BinaryCalculator::BitSeq,
)

@given(instance=BinaryCalculator::BinaryCalculator_strategy)
@settings(max_examples=50)
def test_binarycalculator::binarycalculator_instantiation(instance):
    assert isinstance(instance, BinaryCalculator::BinaryCalculator)

@given(instance=BinaryCalculator::BinaryCalculator_strategy)
def test_binarycalculator::binarycalculator_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=BinaryCalculator::BinaryCalculator_strategy)
def test_binarycalculator::binarycalculator_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=BinaryCalculator::Model_strategy)
@settings(max_examples=50)
def test_binarycalculator::model_instantiation(instance):
    assert isinstance(instance, BinaryCalculator::Model)

@given(instance=BitSeq_strategy)
@settings(max_examples=50)
def test_bitseq_instantiation(instance):
    assert isinstance(instance, BitSeq)

@given(instance=BinaryCalculator::Bit_strategy)
@settings(max_examples=50)
def test_binarycalculator::bit_instantiation(instance):
    assert isinstance(instance, BinaryCalculator::Bit)

@given(instance=BinaryCalculator::Bit_strategy)
def test_binarycalculator::bit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=BinaryCalculator::Bit_strategy)
def test_binarycalculator::bit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BinaryCalculator::L_strategy)
@settings(max_examples=50)
def test_binarycalculator::l_instantiation(instance):
    assert isinstance(instance, BinaryCalculator::L)

@given(instance=BinaryCalculator::Value_strategy)
@settings(max_examples=50)
def test_binarycalculator::value_instantiation(instance):
    assert isinstance(instance, BinaryCalculator::Value)

@given(instance=BinaryCalculator::Value_strategy)
def test_binarycalculator::value_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=BinaryCalculator::Value_strategy)
def test_binarycalculator::value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BinaryCalculator::BitSeq_strategy)
@settings(max_examples=50)
def test_binarycalculator::bitseq_instantiation(instance):
    assert isinstance(instance, BinaryCalculator::BitSeq)
