import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CoachBusWithEDataType_Employee,
    Employee,
    CoachBusWithEDataType_Manager,
    CoachBusWithEDataType_SecurityGuard,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coachbuswithedatatype_employee_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Employee)


def test_coachbuswithedatatype_employee_constructor_exists():
    assert callable(CoachBusWithEDataType_Employee.__init__)


def test_coachbuswithedatatype_employee_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_coachbuswithedatatype_employee_has_id():
    assert hasattr(CoachBusWithEDataType_Employee, "id")
    descriptor = None
    for klass in CoachBusWithEDataType_Employee.__mro__:
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



def test_coachbuswithedatatype_manager_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Manager)


def test_coachbuswithedatatype_manager_constructor_exists():
    assert callable(CoachBusWithEDataType_Manager.__init__)


def test_coachbuswithedatatype_manager_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Manager.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_securityguard_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_SecurityGuard)


def test_coachbuswithedatatype_securityguard_constructor_exists():
    assert callable(CoachBusWithEDataType_SecurityGuard.__init__)


def test_coachbuswithedatatype_securityguard_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_SecurityGuard.__init__)
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
CoachBusWithEDataType_Employee_strategy = st.builds(
    CoachBusWithEDataType_Employee,
    id=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
)
CoachBusWithEDataType_Manager_strategy = st.builds(
    CoachBusWithEDataType_Manager,
)
CoachBusWithEDataType_SecurityGuard_strategy = st.builds(
    CoachBusWithEDataType_SecurityGuard,
)

@given(instance=CoachBusWithEDataType_Employee_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_employee_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Employee)



@given(instance=CoachBusWithEDataType_Employee_strategy)
def test_coachbuswithedatatype_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=CoachBusWithEDataType_Manager_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_manager_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Manager)

@given(instance=CoachBusWithEDataType_SecurityGuard_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_securityguard_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_SecurityGuard)
