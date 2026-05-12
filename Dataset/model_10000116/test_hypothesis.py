import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HARDWARE,
    OWNER,
    HOME_SECURITY,
    POLICE_DEPARTMENT,
    SYSTEM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hardware_is_not_abstract():
    assert not inspect.isabstract(HARDWARE)


def test_hardware_constructor_exists():
    assert callable(HARDWARE.__init__)


def test_hardware_constructor_args():
    sig = inspect.signature(HARDWARE.__init__)
    params = list(sig.parameters.keys())



def test_owner_is_not_abstract():
    assert not inspect.isabstract(OWNER)


def test_owner_constructor_exists():
    assert callable(OWNER.__init__)


def test_owner_constructor_args():
    sig = inspect.signature(OWNER.__init__)
    params = list(sig.parameters.keys())



def test_home_security_is_not_abstract():
    assert not inspect.isabstract(HOME_SECURITY)


def test_home_security_constructor_exists():
    assert callable(HOME_SECURITY.__init__)


def test_home_security_constructor_args():
    sig = inspect.signature(HOME_SECURITY.__init__)
    params = list(sig.parameters.keys())



def test_police_department_is_not_abstract():
    assert not inspect.isabstract(POLICE_DEPARTMENT)


def test_police_department_constructor_exists():
    assert callable(POLICE_DEPARTMENT.__init__)


def test_police_department_constructor_args():
    sig = inspect.signature(POLICE_DEPARTMENT.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(SYSTEM)


def test_system_constructor_exists():
    assert callable(SYSTEM.__init__)


def test_system_constructor_args():
    sig = inspect.signature(SYSTEM.__init__)
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
HARDWARE_strategy = st.builds(
    HARDWARE,
)
OWNER_strategy = st.builds(
    OWNER,
)
HOME_SECURITY_strategy = st.builds(
    HOME_SECURITY,
)
POLICE_DEPARTMENT_strategy = st.builds(
    POLICE_DEPARTMENT,
)
SYSTEM_strategy = st.builds(
    SYSTEM,
)

@given(instance=HARDWARE_strategy)
@settings(max_examples=50)
def test_hardware_instantiation(instance):
    assert isinstance(instance, HARDWARE)

@given(instance=OWNER_strategy)
@settings(max_examples=50)
def test_owner_instantiation(instance):
    assert isinstance(instance, OWNER)

@given(instance=HOME_SECURITY_strategy)
@settings(max_examples=50)
def test_home_security_instantiation(instance):
    assert isinstance(instance, HOME_SECURITY)

@given(instance=POLICE_DEPARTMENT_strategy)
@settings(max_examples=50)
def test_police_department_instantiation(instance):
    assert isinstance(instance, POLICE_DEPARTMENT)

@given(instance=SYSTEM_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, SYSTEM)
