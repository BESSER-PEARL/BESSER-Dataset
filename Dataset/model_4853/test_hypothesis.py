import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Unit,
    units::UnitMultiplication,
    units::Unit,
    units::UnitRepository,
    units::BaseUnit,
    units::UnitCarryingElement,
    units::UnitLiteral,
    units::UnitPower,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_units::unitmultiplication_is_not_abstract():
    assert not inspect.isabstract(units::UnitMultiplication)


def test_units::unitmultiplication_constructor_exists():
    assert callable(units::UnitMultiplication.__init__)


def test_units::unitmultiplication_constructor_args():
    sig = inspect.signature(units::UnitMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_units::unit_is_not_abstract():
    assert not inspect.isabstract(units::Unit)


def test_units::unit_constructor_exists():
    assert callable(units::Unit.__init__)


def test_units::unit_constructor_args():
    sig = inspect.signature(units::Unit.__init__)
    params = list(sig.parameters.keys())



def test_units::unitrepository_is_not_abstract():
    assert not inspect.isabstract(units::UnitRepository)


def test_units::unitrepository_constructor_exists():
    assert callable(units::UnitRepository.__init__)


def test_units::unitrepository_constructor_args():
    sig = inspect.signature(units::UnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_units::baseunit_is_not_abstract():
    assert not inspect.isabstract(units::BaseUnit)


def test_units::baseunit_constructor_exists():
    assert callable(units::BaseUnit.__init__)


def test_units::baseunit_constructor_args():
    sig = inspect.signature(units::BaseUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_units::baseunit_has_name():
    assert hasattr(units::BaseUnit, "name")
    descriptor = None
    for klass in units::BaseUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_units::unitcarryingelement_is_not_abstract():
    assert not inspect.isabstract(units::UnitCarryingElement)


def test_units::unitcarryingelement_constructor_exists():
    assert callable(units::UnitCarryingElement.__init__)


def test_units::unitcarryingelement_constructor_args():
    sig = inspect.signature(units::UnitCarryingElement.__init__)
    params = list(sig.parameters.keys())
    assert "unitSpecification" in params, "Missing parameter 'unitSpecification'"

def test_units::unitcarryingelement_has_unitSpecification():
    assert hasattr(units::UnitCarryingElement, "unitSpecification")
    descriptor = None
    for klass in units::UnitCarryingElement.__mro__:
        if "unitSpecification" in klass.__dict__:
            descriptor = klass.__dict__["unitSpecification"]
            break
    assert isinstance(descriptor, property)



def test_units::unitliteral_is_not_abstract():
    assert not inspect.isabstract(units::UnitLiteral)


def test_units::unitliteral_constructor_exists():
    assert callable(units::UnitLiteral.__init__)


def test_units::unitliteral_constructor_args():
    sig = inspect.signature(units::UnitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_units::unitpower_is_not_abstract():
    assert not inspect.isabstract(units::UnitPower)


def test_units::unitpower_constructor_exists():
    assert callable(units::UnitPower.__init__)


def test_units::unitpower_constructor_args():
    sig = inspect.signature(units::UnitPower.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"

def test_units::unitpower_has_exponent():
    assert hasattr(units::UnitPower, "exponent")
    descriptor = None
    for klass in units::UnitPower.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
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
Unit_strategy = st.builds(
    Unit,
)
units::UnitMultiplication_strategy = st.builds(
    units::UnitMultiplication,
)
units::Unit_strategy = st.builds(
    units::Unit,
)
units::UnitRepository_strategy = st.builds(
    units::UnitRepository,
)
units::BaseUnit_strategy = st.builds(
    units::BaseUnit,
    name=
        safe_text
)
units::UnitCarryingElement_strategy = st.builds(
    units::UnitCarryingElement,
    unitSpecification=
        safe_text
)
units::UnitLiteral_strategy = st.builds(
    units::UnitLiteral,
)
units::UnitPower_strategy = st.builds(
    units::UnitPower,
    exponent=
        st.integers()
)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=units::UnitMultiplication_strategy)
@settings(max_examples=50)
def test_units::unitmultiplication_instantiation(instance):
    assert isinstance(instance, units::UnitMultiplication)

@given(instance=units::Unit_strategy)
@settings(max_examples=50)
def test_units::unit_instantiation(instance):
    assert isinstance(instance, units::Unit)

@given(instance=units::UnitRepository_strategy)
@settings(max_examples=50)
def test_units::unitrepository_instantiation(instance):
    assert isinstance(instance, units::UnitRepository)

@given(instance=units::BaseUnit_strategy)
@settings(max_examples=50)
def test_units::baseunit_instantiation(instance):
    assert isinstance(instance, units::BaseUnit)

@given(instance=units::BaseUnit_strategy)
def test_units::baseunit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=units::BaseUnit_strategy)
def test_units::baseunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=units::UnitCarryingElement_strategy)
@settings(max_examples=50)
def test_units::unitcarryingelement_instantiation(instance):
    assert isinstance(instance, units::UnitCarryingElement)

@given(instance=units::UnitCarryingElement_strategy)
def test_units::unitcarryingelement_unitSpecification_type(instance):
    assert isinstance(instance.unitSpecification, str)


@given(instance=units::UnitCarryingElement_strategy)
def test_units::unitcarryingelement_unitSpecification_setter(instance):
    original = instance.unitSpecification
    instance.unitSpecification = original
    assert instance.unitSpecification == original

@given(instance=units::UnitLiteral_strategy)
@settings(max_examples=50)
def test_units::unitliteral_instantiation(instance):
    assert isinstance(instance, units::UnitLiteral)

@given(instance=units::UnitPower_strategy)
@settings(max_examples=50)
def test_units::unitpower_instantiation(instance):
    assert isinstance(instance, units::UnitPower)

@given(instance=units::UnitPower_strategy)
def test_units::unitpower_exponent_type(instance):
    assert isinstance(instance.exponent, int)


@given(instance=units::UnitPower_strategy)
def test_units::unitpower_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original
