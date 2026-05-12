import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    PlanDAO,
    PatientDAO,
    PatientBO,
    StateDAO1,
    PatientTO,
    StateDAO,
    EnrollPatient_Controller,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_plandao_is_not_abstract():
    assert not inspect.isabstract(PlanDAO)


def test_plandao_constructor_exists():
    assert callable(PlanDAO.__init__)


def test_plandao_constructor_args():
    sig = inspect.signature(PlanDAO.__init__)
    params = list(sig.parameters.keys())



def test_patientdao_is_not_abstract():
    assert not inspect.isabstract(PatientDAO)


def test_patientdao_constructor_exists():
    assert callable(PatientDAO.__init__)


def test_patientdao_constructor_args():
    sig = inspect.signature(PatientDAO.__init__)
    params = list(sig.parameters.keys())



def test_patientbo_is_not_abstract():
    assert not inspect.isabstract(PatientBO)


def test_patientbo_constructor_exists():
    assert callable(PatientBO.__init__)


def test_patientbo_constructor_args():
    sig = inspect.signature(PatientBO.__init__)
    params = list(sig.parameters.keys())



def test_statedao1_is_not_abstract():
    assert not inspect.isabstract(StateDAO1)


def test_statedao1_constructor_exists():
    assert callable(StateDAO1.__init__)


def test_statedao1_constructor_args():
    sig = inspect.signature(StateDAO1.__init__)
    params = list(sig.parameters.keys())



def test_patientto_is_not_abstract():
    assert not inspect.isabstract(PatientTO)


def test_patientto_constructor_exists():
    assert callable(PatientTO.__init__)


def test_patientto_constructor_args():
    sig = inspect.signature(PatientTO.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "plan_id" in params, "Missing parameter 'plan_id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "state_id" in params, "Missing parameter 'state_id'"
    assert "patient_id" in params, "Missing parameter 'patient_id'"
    assert "first_name" in params, "Missing parameter 'first_name'"

def test_patientto_has_password():
    assert hasattr(PatientTO, "password")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_date_of_birth():
    assert hasattr(PatientTO, "date_of_birth")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "date_of_birth" in klass.__dict__:
            descriptor = klass.__dict__["date_of_birth"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_last_name():
    assert hasattr(PatientTO, "last_name")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "last_name" in klass.__dict__:
            descriptor = klass.__dict__["last_name"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_plan_id():
    assert hasattr(PatientTO, "plan_id")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "plan_id" in klass.__dict__:
            descriptor = klass.__dict__["plan_id"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_email():
    assert hasattr(PatientTO, "email")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_contact_no():
    assert hasattr(PatientTO, "contact_no")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "contact_no" in klass.__dict__:
            descriptor = klass.__dict__["contact_no"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_state_id():
    assert hasattr(PatientTO, "state_id")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "state_id" in klass.__dict__:
            descriptor = klass.__dict__["state_id"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_patient_id():
    assert hasattr(PatientTO, "patient_id")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "patient_id" in klass.__dict__:
            descriptor = klass.__dict__["patient_id"]
            break
    assert isinstance(descriptor, property)

def test_patientto_has_first_name():
    assert hasattr(PatientTO, "first_name")
    descriptor = None
    for klass in PatientTO.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)



def test_statedao_is_not_abstract():
    assert not inspect.isabstract(StateDAO)


def test_statedao_constructor_exists():
    assert callable(StateDAO.__init__)


def test_statedao_constructor_args():
    sig = inspect.signature(StateDAO.__init__)
    params = list(sig.parameters.keys())



def test_enrollpatient_controller_is_not_abstract():
    assert not inspect.isabstract(EnrollPatient_Controller)


def test_enrollpatient_controller_constructor_exists():
    assert callable(EnrollPatient_Controller.__init__)


def test_enrollpatient_controller_constructor_args():
    sig = inspect.signature(EnrollPatient_Controller.__init__)
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
Class_strategy = st.builds(
    Class,
)
PlanDAO_strategy = st.builds(
    PlanDAO,
)
PatientDAO_strategy = st.builds(
    PatientDAO,
)
PatientBO_strategy = st.builds(
    PatientBO,
)
StateDAO1_strategy = st.builds(
    StateDAO1,
)
PatientTO_strategy = st.builds(
    PatientTO,
    password=
        safe_text,
    date_of_birth=
        st.dates(),
    last_name=
        safe_text,
    plan_id=
        st.integers(),
    email=
        safe_text,
    contact_no=
        st.integers(),
    state_id=
        st.integers(),
    patient_id=
        st.integers(),
    first_name=
        safe_text
)
StateDAO_strategy = st.builds(
    StateDAO,
)
EnrollPatient_Controller_strategy = st.builds(
    EnrollPatient_Controller,
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=PlanDAO_strategy)
@settings(max_examples=50)
def test_plandao_instantiation(instance):
    assert isinstance(instance, PlanDAO)

@given(instance=PatientDAO_strategy)
@settings(max_examples=50)
def test_patientdao_instantiation(instance):
    assert isinstance(instance, PatientDAO)

@given(instance=PatientBO_strategy)
@settings(max_examples=50)
def test_patientbo_instantiation(instance):
    assert isinstance(instance, PatientBO)

@given(instance=StateDAO1_strategy)
@settings(max_examples=50)
def test_statedao1_instantiation(instance):
    assert isinstance(instance, StateDAO1)

@given(instance=PatientTO_strategy)
@settings(max_examples=50)
def test_patientto_instantiation(instance):
    assert isinstance(instance, PatientTO)



@given(instance=PatientTO_strategy)
def test_patientto_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=PatientTO_strategy)
def test_patientto_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original



@given(instance=PatientTO_strategy)
def test_patientto_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=PatientTO_strategy)
def test_patientto_plan_id_setter(instance):
    original = instance.plan_id
    instance.plan_id = original
    assert instance.plan_id == original



@given(instance=PatientTO_strategy)
def test_patientto_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=PatientTO_strategy)
def test_patientto_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=PatientTO_strategy)
def test_patientto_state_id_setter(instance):
    original = instance.state_id
    instance.state_id = original
    assert instance.state_id == original



@given(instance=PatientTO_strategy)
def test_patientto_patient_id_setter(instance):
    original = instance.patient_id
    instance.patient_id = original
    assert instance.patient_id == original



@given(instance=PatientTO_strategy)
def test_patientto_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original

@given(instance=StateDAO_strategy)
@settings(max_examples=50)
def test_statedao_instantiation(instance):
    assert isinstance(instance, StateDAO)

@given(instance=EnrollPatient_Controller_strategy)
@settings(max_examples=50)
def test_enrollpatient_controller_instantiation(instance):
    assert isinstance(instance, EnrollPatient_Controller)
