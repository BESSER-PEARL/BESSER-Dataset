import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CoachBusWithEDataType::Employee,
    Employee,
    CoachBusWithEDataType::Manager,
    CoachBusWithEDataType::SecurityGuard,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coachbuswithedatatype::employee_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Employee)


def test_coachbuswithedatatype::employee_constructor_exists():
    assert callable(CoachBusWithEDataType::Employee.__init__)


def test_coachbuswithedatatype::employee_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_coachbuswithedatatype::employee_has_id():
    assert hasattr(CoachBusWithEDataType::Employee, "id")
    descriptor = None
    for klass in CoachBusWithEDataType::Employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



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
CoachBusWithEDataType::Employee_strategy = st.builds(
    CoachBusWithEDataType::Employee,
    id=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
)
CoachBusWithEDataType::Manager_strategy = st.builds(
    CoachBusWithEDataType::Manager,
)
CoachBusWithEDataType::SecurityGuard_strategy = st.builds(
    CoachBusWithEDataType::SecurityGuard,
)

@given(instance=CoachBusWithEDataType::Employee_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::employee_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Employee)

@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

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
