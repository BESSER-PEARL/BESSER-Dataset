import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    units::UnitRepository,
    Unit,
    units::UnitDivision,
    units::UnitPower,
    units::UnitMultiplication,
    units::BaseUnit,
    units::Unit,
    units::UnitCarryingElement,
    UnitNames,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_units::unitrepository_is_not_abstract():
    assert not inspect.isabstract(units::UnitRepository)


def test_units::unitrepository_constructor_exists():
    assert callable(units::UnitRepository.__init__)


def test_units::unitrepository_constructor_args():
    sig = inspect.signature(units::UnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_units::unitdivision_is_not_abstract():
    assert not inspect.isabstract(units::UnitDivision)


def test_units::unitdivision_constructor_exists():
    assert callable(units::UnitDivision.__init__)


def test_units::unitdivision_constructor_args():
    sig = inspect.signature(units::UnitDivision.__init__)
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



def test_units::unitmultiplication_is_not_abstract():
    assert not inspect.isabstract(units::UnitMultiplication)


def test_units::unitmultiplication_constructor_exists():
    assert callable(units::UnitMultiplication.__init__)


def test_units::unitmultiplication_constructor_args():
    sig = inspect.signature(units::UnitMultiplication.__init__)
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



def test_units::unit_is_not_abstract():
    assert not inspect.isabstract(units::Unit)


def test_units::unit_constructor_exists():
    assert callable(units::Unit.__init__)


def test_units::unit_constructor_args():
    sig = inspect.signature(units::Unit.__init__)
    params = list(sig.parameters.keys())



def test_units::unitcarryingelement_is_not_abstract():
    assert not inspect.isabstract(units::UnitCarryingElement)


def test_units::unitcarryingelement_constructor_exists():
    assert callable(units::UnitCarryingElement.__init__)


def test_units::unitcarryingelement_constructor_args():
    sig = inspect.signature(units::UnitCarryingElement.__init__)
    params = list(sig.parameters.keys())

def test_unitnames_exists():
    # Check that the Enumeration exists
    assert UnitNames is not None

def test_unitnames_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnitNames]
    expected_literals = [
        "SECOND",
        "METER",
        "BYTE",
        "UNITLESS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnitNames"


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
units::UnitRepository_strategy = st.builds(
    units::UnitRepository,
)
Unit_strategy = st.builds(
    Unit,
)
units::UnitDivision_strategy = st.builds(
    units::UnitDivision,
)
units::UnitPower_strategy = st.builds(
    units::UnitPower,
    exponent=
        st.integers()
)
units::UnitMultiplication_strategy = st.builds(
    units::UnitMultiplication,
)
units::BaseUnit_strategy = st.builds(
    units::BaseUnit,
    name=
        safe_text
)
units::Unit_strategy = st.builds(
    units::Unit,
)
units::UnitCarryingElement_strategy = st.builds(
    units::UnitCarryingElement,
)

@given(instance=units::UnitRepository_strategy)
@settings(max_examples=50)
def test_units::unitrepository_instantiation(instance):
    assert isinstance(instance, units::UnitRepository)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=units::UnitDivision_strategy)
@settings(max_examples=50)
def test_units::unitdivision_instantiation(instance):
    assert isinstance(instance, units::UnitDivision)

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

@given(instance=units::UnitMultiplication_strategy)
@settings(max_examples=50)
def test_units::unitmultiplication_instantiation(instance):
    assert isinstance(instance, units::UnitMultiplication)

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

@given(instance=units::Unit_strategy)
@settings(max_examples=50)
def test_units::unit_instantiation(instance):
    assert isinstance(instance, units::Unit)

@given(instance=units::UnitCarryingElement_strategy)
@settings(max_examples=50)
def test_units::unitcarryingelement_instantiation(instance):
    assert isinstance(instance, units::UnitCarryingElement)
