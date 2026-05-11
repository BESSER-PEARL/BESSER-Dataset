import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    profile::Constraint,
    profile::Resource,
    profile::PlatformProfile,
    ResourceTypes,
    ConstraintOperation,
    ConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_profile::constraint_is_not_abstract():
    assert not inspect.isabstract(profile::Constraint)


def test_profile::constraint_constructor_exists():
    assert callable(profile::Constraint.__init__)


def test_profile::constraint_constructor_args():
    sig = inspect.signature(profile::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"
    assert "bound" in params, "Missing parameter 'bound'"
    assert "type" in params, "Missing parameter 'type'"
    assert "isDerivation" in params, "Missing parameter 'isDerivation'"

def test_profile::constraint_has_operation():
    assert hasattr(profile::Constraint, "operation")
    descriptor = None
    for klass in profile::Constraint.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)

def test_profile::constraint_has_bound():
    assert hasattr(profile::Constraint, "bound")
    descriptor = None
    for klass in profile::Constraint.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)

def test_profile::constraint_has_type():
    assert hasattr(profile::Constraint, "type")
    descriptor = None
    for klass in profile::Constraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_profile::constraint_has_isDerivation():
    assert hasattr(profile::Constraint, "isDerivation")
    descriptor = None
    for klass in profile::Constraint.__mro__:
        if "isDerivation" in klass.__dict__:
            descriptor = klass.__dict__["isDerivation"]
            break
    assert isinstance(descriptor, property)



def test_profile::resource_is_not_abstract():
    assert not inspect.isabstract(profile::Resource)


def test_profile::resource_constructor_exists():
    assert callable(profile::Resource.__init__)


def test_profile::resource_constructor_args():
    sig = inspect.signature(profile::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_profile::resource_has_type():
    assert hasattr(profile::Resource, "type")
    descriptor = None
    for klass in profile::Resource.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_profile::resource_has_name():
    assert hasattr(profile::Resource, "name")
    descriptor = None
    for klass in profile::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_profile::platformprofile_is_not_abstract():
    assert not inspect.isabstract(profile::PlatformProfile)


def test_profile::platformprofile_constructor_exists():
    assert callable(profile::PlatformProfile.__init__)


def test_profile::platformprofile_constructor_args():
    sig = inspect.signature(profile::PlatformProfile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_profile::platformprofile_has_name():
    assert hasattr(profile::PlatformProfile, "name")
    descriptor = None
    for klass in profile::PlatformProfile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_resourcetypes_exists():
    # Check that the Enumeration exists
    assert ResourceTypes is not None

def test_resourcetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResourceTypes]
    expected_literals = [
        "port",
        "cpu",
        "power",
        "bandwidth",
        "memory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResourceTypes"

def test_constraintoperation_exists():
    # Check that the Enumeration exists
    assert ConstraintOperation is not None

def test_constraintoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintOperation]
    expected_literals = [
        "Greater",
        "Less",
        "Equal",
        "LessOrEqual",
        "GreaterOrEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintOperation"

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "Minimum",
        "Average",
        "Maximum",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintType"


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
profile::Constraint_strategy = st.builds(
    profile::Constraint,
    operation=
        safe_text,
    bound=
        st.integers(),
    type=
        safe_text,
    isDerivation=
        st.booleans()
)
profile::Resource_strategy = st.builds(
    profile::Resource,
    type=
        safe_text,
    name=
        safe_text
)
profile::PlatformProfile_strategy = st.builds(
    profile::PlatformProfile,
    name=
        safe_text
)

@given(instance=profile::Constraint_strategy)
@settings(max_examples=50)
def test_profile::constraint_instantiation(instance):
    assert isinstance(instance, profile::Constraint)

@given(instance=profile::Constraint_strategy)
def test_profile::constraint_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=profile::Constraint_strategy)
def test_profile::constraint_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=profile::Constraint_strategy)
def test_profile::constraint_bound_type(instance):
    assert isinstance(instance.bound, int)


@given(instance=profile::Constraint_strategy)
def test_profile::constraint_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=profile::Constraint_strategy)
def test_profile::constraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=profile::Constraint_strategy)
def test_profile::constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=profile::Constraint_strategy)
def test_profile::constraint_isDerivation_type(instance):
    assert isinstance(instance.isDerivation, bool)


@given(instance=profile::Constraint_strategy)
def test_profile::constraint_isDerivation_setter(instance):
    original = instance.isDerivation
    instance.isDerivation = original
    assert instance.isDerivation == original

@given(instance=profile::Resource_strategy)
@settings(max_examples=50)
def test_profile::resource_instantiation(instance):
    assert isinstance(instance, profile::Resource)

@given(instance=profile::Resource_strategy)
def test_profile::resource_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=profile::Resource_strategy)
def test_profile::resource_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=profile::Resource_strategy)
def test_profile::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=profile::Resource_strategy)
def test_profile::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=profile::PlatformProfile_strategy)
@settings(max_examples=50)
def test_profile::platformprofile_instantiation(instance):
    assert isinstance(instance, profile::PlatformProfile)

@given(instance=profile::PlatformProfile_strategy)
def test_profile::platformprofile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=profile::PlatformProfile_strategy)
def test_profile::platformprofile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
