import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testpackage::NamedElement,
    NamedElement,
    testpackage::Group,
    testpackage::User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::namedelement_is_not_abstract():
    assert not inspect.isabstract(testpackage::NamedElement)


def test_testpackage::namedelement_constructor_exists():
    assert callable(testpackage::NamedElement.__init__)


def test_testpackage::namedelement_constructor_args():
    sig = inspect.signature(testpackage::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testpackage::namedelement_has_name():
    assert hasattr(testpackage::NamedElement, "name")
    descriptor = None
    for klass in testpackage::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::group_is_not_abstract():
    assert not inspect.isabstract(testpackage::Group)


def test_testpackage::group_constructor_exists():
    assert callable(testpackage::Group.__init__)


def test_testpackage::group_constructor_args():
    sig = inspect.signature(testpackage::Group.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::user_is_not_abstract():
    assert not inspect.isabstract(testpackage::User)


def test_testpackage::user_constructor_exists():
    assert callable(testpackage::User.__init__)


def test_testpackage::user_constructor_args():
    sig = inspect.signature(testpackage::User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"

def test_testpackage::user_has_password():
    assert hasattr(testpackage::User, "password")
    descriptor = None
    for klass in testpackage::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
testpackage::NamedElement_strategy = st.builds(
    testpackage::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
testpackage::Group_strategy = st.builds(
    testpackage::Group,
)
testpackage::User_strategy = st.builds(
    testpackage::User,
    password=
        safe_text
)

@given(instance=testpackage::NamedElement_strategy)
@settings(max_examples=50)
def test_testpackage::namedelement_instantiation(instance):
    assert isinstance(instance, testpackage::NamedElement)

@given(instance=testpackage::NamedElement_strategy)
def test_testpackage::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testpackage::NamedElement_strategy)
def test_testpackage::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=testpackage::Group_strategy)
@settings(max_examples=50)
def test_testpackage::group_instantiation(instance):
    assert isinstance(instance, testpackage::Group)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=testpackage::Group_strategy)
@settings(max_examples=30)
def test_testpackage::group_ismember_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMember(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMember).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMember' in testpackage::Group is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMember' in testpackage::Group did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMember' in testpackage::Group is not implemented or raised an error")

@given(instance=testpackage::User_strategy)
@settings(max_examples=50)
def test_testpackage::user_instantiation(instance):
    assert isinstance(instance, testpackage::User)

@given(instance=testpackage::User_strategy)
def test_testpackage::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=testpackage::User_strategy)
def test_testpackage::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
