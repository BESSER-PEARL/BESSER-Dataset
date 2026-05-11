import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Unit,
    units::pc::UnitPower,
    units::pc::UnitMultiplication,
    units::pc::UnitRepository,
    units::pc::EObject,
    units::pc::Pointcut,
    units::pc::UnitLiteral,
    units::pc::BaseUnit,
    units::pc::Unit,
    units::pc::UnitCarryingElement,
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



def test_units::pc::unitpower_is_not_abstract():
    assert not inspect.isabstract(units::pc::UnitPower)


def test_units::pc::unitpower_constructor_exists():
    assert callable(units::pc::UnitPower.__init__)


def test_units::pc::unitpower_constructor_args():
    sig = inspect.signature(units::pc::UnitPower.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"

def test_units::pc::unitpower_has_exponent():
    assert hasattr(units::pc::UnitPower, "exponent")
    descriptor = None
    for klass in units::pc::UnitPower.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)



def test_units::pc::unitmultiplication_is_not_abstract():
    assert not inspect.isabstract(units::pc::UnitMultiplication)


def test_units::pc::unitmultiplication_constructor_exists():
    assert callable(units::pc::UnitMultiplication.__init__)


def test_units::pc::unitmultiplication_constructor_args():
    sig = inspect.signature(units::pc::UnitMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_units::pc::unitrepository_is_not_abstract():
    assert not inspect.isabstract(units::pc::UnitRepository)


def test_units::pc::unitrepository_constructor_exists():
    assert callable(units::pc::UnitRepository.__init__)


def test_units::pc::unitrepository_constructor_args():
    sig = inspect.signature(units::pc::UnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_units::pc::eobject_is_not_abstract():
    assert not inspect.isabstract(units::pc::EObject)


def test_units::pc::eobject_constructor_exists():
    assert callable(units::pc::EObject.__init__)


def test_units::pc::eobject_constructor_args():
    sig = inspect.signature(units::pc::EObject.__init__)
    params = list(sig.parameters.keys())



def test_units::pc::pointcut_is_not_abstract():
    assert not inspect.isabstract(units::pc::Pointcut)


def test_units::pc::pointcut_constructor_exists():
    assert callable(units::pc::Pointcut.__init__)


def test_units::pc::pointcut_constructor_args():
    sig = inspect.signature(units::pc::Pointcut.__init__)
    params = list(sig.parameters.keys())



def test_units::pc::unitliteral_is_not_abstract():
    assert not inspect.isabstract(units::pc::UnitLiteral)


def test_units::pc::unitliteral_constructor_exists():
    assert callable(units::pc::UnitLiteral.__init__)


def test_units::pc::unitliteral_constructor_args():
    sig = inspect.signature(units::pc::UnitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_units::pc::baseunit_is_not_abstract():
    assert not inspect.isabstract(units::pc::BaseUnit)


def test_units::pc::baseunit_constructor_exists():
    assert callable(units::pc::BaseUnit.__init__)


def test_units::pc::baseunit_constructor_args():
    sig = inspect.signature(units::pc::BaseUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_units::pc::baseunit_has_name():
    assert hasattr(units::pc::BaseUnit, "name")
    descriptor = None
    for klass in units::pc::BaseUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_units::pc::unit_is_not_abstract():
    assert not inspect.isabstract(units::pc::Unit)


def test_units::pc::unit_constructor_exists():
    assert callable(units::pc::Unit.__init__)


def test_units::pc::unit_constructor_args():
    sig = inspect.signature(units::pc::Unit.__init__)
    params = list(sig.parameters.keys())



def test_units::pc::unitcarryingelement_is_not_abstract():
    assert not inspect.isabstract(units::pc::UnitCarryingElement)


def test_units::pc::unitcarryingelement_constructor_exists():
    assert callable(units::pc::UnitCarryingElement.__init__)


def test_units::pc::unitcarryingelement_constructor_args():
    sig = inspect.signature(units::pc::UnitCarryingElement.__init__)
    params = list(sig.parameters.keys())
    assert "unitSpecification" in params, "Missing parameter 'unitSpecification'"

def test_units::pc::unitcarryingelement_has_unitSpecification():
    assert hasattr(units::pc::UnitCarryingElement, "unitSpecification")
    descriptor = None
    for klass in units::pc::UnitCarryingElement.__mro__:
        if "unitSpecification" in klass.__dict__:
            descriptor = klass.__dict__["unitSpecification"]
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
units::pc::UnitPower_strategy = st.builds(
    units::pc::UnitPower,
    exponent=
        st.integers()
)
units::pc::UnitMultiplication_strategy = st.builds(
    units::pc::UnitMultiplication,
)
units::pc::UnitRepository_strategy = st.builds(
    units::pc::UnitRepository,
)
units::pc::EObject_strategy = st.builds(
    units::pc::EObject,
)
units::pc::Pointcut_strategy = st.builds(
    units::pc::Pointcut,
)
units::pc::UnitLiteral_strategy = st.builds(
    units::pc::UnitLiteral,
)
units::pc::BaseUnit_strategy = st.builds(
    units::pc::BaseUnit,
    name=
        safe_text
)
units::pc::Unit_strategy = st.builds(
    units::pc::Unit,
)
units::pc::UnitCarryingElement_strategy = st.builds(
    units::pc::UnitCarryingElement,
    unitSpecification=
        safe_text
)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=units::pc::UnitPower_strategy)
@settings(max_examples=50)
def test_units::pc::unitpower_instantiation(instance):
    assert isinstance(instance, units::pc::UnitPower)

@given(instance=units::pc::UnitPower_strategy)
def test_units::pc::unitpower_exponent_type(instance):
    assert isinstance(instance.exponent, int)


@given(instance=units::pc::UnitPower_strategy)
def test_units::pc::unitpower_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original

@given(instance=units::pc::UnitMultiplication_strategy)
@settings(max_examples=50)
def test_units::pc::unitmultiplication_instantiation(instance):
    assert isinstance(instance, units::pc::UnitMultiplication)

@given(instance=units::pc::UnitRepository_strategy)
@settings(max_examples=50)
def test_units::pc::unitrepository_instantiation(instance):
    assert isinstance(instance, units::pc::UnitRepository)

@given(instance=units::pc::EObject_strategy)
@settings(max_examples=50)
def test_units::pc::eobject_instantiation(instance):
    assert isinstance(instance, units::pc::EObject)

@given(instance=units::pc::Pointcut_strategy)
@settings(max_examples=50)
def test_units::pc::pointcut_instantiation(instance):
    assert isinstance(instance, units::pc::Pointcut)

@given(instance=units::pc::UnitLiteral_strategy)
@settings(max_examples=50)
def test_units::pc::unitliteral_instantiation(instance):
    assert isinstance(instance, units::pc::UnitLiteral)

@given(instance=units::pc::BaseUnit_strategy)
@settings(max_examples=50)
def test_units::pc::baseunit_instantiation(instance):
    assert isinstance(instance, units::pc::BaseUnit)

@given(instance=units::pc::BaseUnit_strategy)
def test_units::pc::baseunit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=units::pc::BaseUnit_strategy)
def test_units::pc::baseunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=units::pc::Unit_strategy)
@settings(max_examples=50)
def test_units::pc::unit_instantiation(instance):
    assert isinstance(instance, units::pc::Unit)

@given(instance=units::pc::UnitCarryingElement_strategy)
@settings(max_examples=50)
def test_units::pc::unitcarryingelement_instantiation(instance):
    assert isinstance(instance, units::pc::UnitCarryingElement)

@given(instance=units::pc::UnitCarryingElement_strategy)
def test_units::pc::unitcarryingelement_unitSpecification_type(instance):
    assert isinstance(instance.unitSpecification, str)


@given(instance=units::pc::UnitCarryingElement_strategy)
def test_units::pc::unitcarryingelement_unitSpecification_setter(instance):
    original = instance.unitSpecification
    instance.unitSpecification = original
    assert instance.unitSpecification == original
