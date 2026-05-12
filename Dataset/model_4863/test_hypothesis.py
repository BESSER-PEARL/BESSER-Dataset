import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    units_UnitRepository,
    Unit,
    units_UnitPower,
    units_UnitMultiplication,
    units_BaseUnit,
    units_Unit,
    units_UnitCarryingElement,
    units_UnitDivision,
    UnitNames,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_units_unitrepository_is_not_abstract():
    assert not inspect.isabstract(units_UnitRepository)


def test_units_unitrepository_constructor_exists():
    assert callable(units_UnitRepository.__init__)


def test_units_unitrepository_constructor_args():
    sig = inspect.signature(units_UnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_units_unitpower_is_not_abstract():
    assert not inspect.isabstract(units_UnitPower)


def test_units_unitpower_constructor_exists():
    assert callable(units_UnitPower.__init__)


def test_units_unitpower_constructor_args():
    sig = inspect.signature(units_UnitPower.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"

def test_units_unitpower_has_exponent():
    assert hasattr(units_UnitPower, "exponent")
    descriptor = None
    for klass in units_UnitPower.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)



def test_units_unitmultiplication_is_not_abstract():
    assert not inspect.isabstract(units_UnitMultiplication)


def test_units_unitmultiplication_constructor_exists():
    assert callable(units_UnitMultiplication.__init__)


def test_units_unitmultiplication_constructor_args():
    sig = inspect.signature(units_UnitMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_units_baseunit_is_not_abstract():
    assert not inspect.isabstract(units_BaseUnit)


def test_units_baseunit_constructor_exists():
    assert callable(units_BaseUnit.__init__)


def test_units_baseunit_constructor_args():
    sig = inspect.signature(units_BaseUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_units_baseunit_has_name():
    assert hasattr(units_BaseUnit, "name")
    descriptor = None
    for klass in units_BaseUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_units_unit_is_not_abstract():
    assert not inspect.isabstract(units_Unit)


def test_units_unit_constructor_exists():
    assert callable(units_Unit.__init__)


def test_units_unit_constructor_args():
    sig = inspect.signature(units_Unit.__init__)
    params = list(sig.parameters.keys())



def test_units_unitcarryingelement_is_not_abstract():
    assert not inspect.isabstract(units_UnitCarryingElement)


def test_units_unitcarryingelement_constructor_exists():
    assert callable(units_UnitCarryingElement.__init__)


def test_units_unitcarryingelement_constructor_args():
    sig = inspect.signature(units_UnitCarryingElement.__init__)
    params = list(sig.parameters.keys())



def test_units_unitdivision_is_not_abstract():
    assert not inspect.isabstract(units_UnitDivision)


def test_units_unitdivision_constructor_exists():
    assert callable(units_UnitDivision.__init__)


def test_units_unitdivision_constructor_args():
    sig = inspect.signature(units_UnitDivision.__init__)
    params = list(sig.parameters.keys())

def test_unitnames_exists():
    # Check that the Enumeration exists
    assert UnitNames is not None

def test_unitnames_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnitNames]
    expected_literals = [
        "BYTE",
        "UNITLESS",
        "SECOND",
        "METER",
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
units_UnitRepository_strategy = st.builds(
    units_UnitRepository,
)
Unit_strategy = st.builds(
    Unit,
)
units_UnitPower_strategy = st.builds(
    units_UnitPower,
    exponent=
        st.integers()
)
units_UnitMultiplication_strategy = st.builds(
    units_UnitMultiplication,
)
units_BaseUnit_strategy = st.builds(
    units_BaseUnit,
    name=
        safe_text
)
units_Unit_strategy = st.builds(
    units_Unit,
)
units_UnitCarryingElement_strategy = st.builds(
    units_UnitCarryingElement,
)
units_UnitDivision_strategy = st.builds(
    units_UnitDivision,
)

@given(instance=units_UnitRepository_strategy)
@settings(max_examples=50)
def test_units_unitrepository_instantiation(instance):
    assert isinstance(instance, units_UnitRepository)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=units_UnitPower_strategy)
@settings(max_examples=50)
def test_units_unitpower_instantiation(instance):
    assert isinstance(instance, units_UnitPower)



@given(instance=units_UnitPower_strategy)
def test_units_unitpower_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original

@given(instance=units_UnitMultiplication_strategy)
@settings(max_examples=50)
def test_units_unitmultiplication_instantiation(instance):
    assert isinstance(instance, units_UnitMultiplication)

@given(instance=units_BaseUnit_strategy)
@settings(max_examples=50)
def test_units_baseunit_instantiation(instance):
    assert isinstance(instance, units_BaseUnit)



@given(instance=units_BaseUnit_strategy)
def test_units_baseunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=units_Unit_strategy)
@settings(max_examples=50)
def test_units_unit_instantiation(instance):
    assert isinstance(instance, units_Unit)

@given(instance=units_UnitCarryingElement_strategy)
@settings(max_examples=50)
def test_units_unitcarryingelement_instantiation(instance):
    assert isinstance(instance, units_UnitCarryingElement)

@given(instance=units_UnitDivision_strategy)
@settings(max_examples=50)
def test_units_unitdivision_instantiation(instance):
    assert isinstance(instance, units_UnitDivision)
