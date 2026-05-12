import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Employee,
    CoachBusWithEDataType::Manager,
    CoachBusWithEDataType::SecurityGuard,
    CoachBusWithEDataType::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::manager_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Manager)


def test_coachbuswithedatatype::manager_constructor_exists():
    assert callable(CoachBusWithEDataType::Manager.__init__)


def test_coachbuswithedatatype::manager_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Manager.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::securityguard_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::SecurityGuard)


def test_coachbuswithedatatype::securityguard_constructor_exists():
    assert callable(CoachBusWithEDataType::SecurityGuard.__init__)


def test_coachbuswithedatatype::securityguard_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::SecurityGuard.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::employee_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Employee)


def test_coachbuswithedatatype::employee_constructor_exists():
    assert callable(CoachBusWithEDataType::Employee.__init__)


def test_coachbuswithedatatype::employee_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "baseSalary" in params, "Missing parameter 'baseSalary'"

def test_coachbuswithedatatype::employee_has_baseSalary():
    assert hasattr(CoachBusWithEDataType::Employee, "baseSalary")
    descriptor = None
    for klass in CoachBusWithEDataType::Employee.__mro__:
        if "baseSalary" in klass.__dict__:
            descriptor = klass.__dict__["baseSalary"]
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
Employee_strategy = st.builds(
    Employee,
)
CoachBusWithEDataType::Manager_strategy = st.builds(
    CoachBusWithEDataType::Manager,
)
CoachBusWithEDataType::SecurityGuard_strategy = st.builds(
    CoachBusWithEDataType::SecurityGuard,
)
CoachBusWithEDataType::Employee_strategy = st.builds(
    CoachBusWithEDataType::Employee,
    baseSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=CoachBusWithEDataType::Manager_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::manager_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Manager)

@given(instance=CoachBusWithEDataType::SecurityGuard_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::securityguard_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::SecurityGuard)

@given(instance=CoachBusWithEDataType::Employee_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::employee_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Employee)

@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_baseSalary_type(instance):
    assert isinstance(instance.baseSalary, float)


@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_baseSalary_setter(instance):
    original = instance.baseSalary
    instance.baseSalary = original
    assert instance.baseSalary == original
