import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    profile_Constraint,
    profile_Resource,
    profile_PlatformProfile,
    ResourceTypes,
    ConstraintOperation,
    ConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_profile_constraint_is_not_abstract():
    assert not inspect.isabstract(profile_Constraint)


def test_profile_constraint_constructor_exists():
    assert callable(profile_Constraint.__init__)


def test_profile_constraint_constructor_args():
    sig = inspect.signature(profile_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivation" in params, "Missing parameter 'isDerivation'"
    assert "type" in params, "Missing parameter 'type'"
    assert "operation" in params, "Missing parameter 'operation'"
    assert "bound" in params, "Missing parameter 'bound'"

def test_profile_constraint_has_isDerivation():
    assert hasattr(profile_Constraint, "isDerivation")
    descriptor = None
    for klass in profile_Constraint.__mro__:
        if "isDerivation" in klass.__dict__:
            descriptor = klass.__dict__["isDerivation"]
            break
    assert isinstance(descriptor, property)

def test_profile_constraint_has_type():
    assert hasattr(profile_Constraint, "type")
    descriptor = None
    for klass in profile_Constraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_profile_constraint_has_operation():
    assert hasattr(profile_Constraint, "operation")
    descriptor = None
    for klass in profile_Constraint.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)

def test_profile_constraint_has_bound():
    assert hasattr(profile_Constraint, "bound")
    descriptor = None
    for klass in profile_Constraint.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_profile_resource_is_not_abstract():
    assert not inspect.isabstract(profile_Resource)


def test_profile_resource_constructor_exists():
    assert callable(profile_Resource.__init__)


def test_profile_resource_constructor_args():
    sig = inspect.signature(profile_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_profile_resource_has_name():
    assert hasattr(profile_Resource, "name")
    descriptor = None
    for klass in profile_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_profile_resource_has_type():
    assert hasattr(profile_Resource, "type")
    descriptor = None
    for klass in profile_Resource.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_profile_platformprofile_is_not_abstract():
    assert not inspect.isabstract(profile_PlatformProfile)


def test_profile_platformprofile_constructor_exists():
    assert callable(profile_PlatformProfile.__init__)


def test_profile_platformprofile_constructor_args():
    sig = inspect.signature(profile_PlatformProfile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_profile_platformprofile_has_name():
    assert hasattr(profile_PlatformProfile, "name")
    descriptor = None
    for klass in profile_PlatformProfile.__mro__:
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
        "cpu",
        "memory",
        "port",
        "bandwidth",
        "power",
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
        "LessOrEqual",
        "Greater",
        "Less",
        "Equal",
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
        "Maximum",
        "Minimum",
        "Average",
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
profile_Constraint_strategy = st.builds(
    profile_Constraint,
    isDerivation=
        st.booleans(),
    type=
        safe_text,
    operation=
        safe_text,
    bound=
        st.integers()
)
profile_Resource_strategy = st.builds(
    profile_Resource,
    name=
        safe_text,
    type=
        safe_text
)
profile_PlatformProfile_strategy = st.builds(
    profile_PlatformProfile,
    name=
        safe_text
)

@given(instance=profile_Constraint_strategy)
@settings(max_examples=50)
def test_profile_constraint_instantiation(instance):
    assert isinstance(instance, profile_Constraint)



@given(instance=profile_Constraint_strategy)
def test_profile_constraint_isDerivation_setter(instance):
    original = instance.isDerivation
    instance.isDerivation = original
    assert instance.isDerivation == original



@given(instance=profile_Constraint_strategy)
def test_profile_constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=profile_Constraint_strategy)
def test_profile_constraint_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original



@given(instance=profile_Constraint_strategy)
def test_profile_constraint_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=profile_Resource_strategy)
@settings(max_examples=50)
def test_profile_resource_instantiation(instance):
    assert isinstance(instance, profile_Resource)



@given(instance=profile_Resource_strategy)
def test_profile_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=profile_Resource_strategy)
def test_profile_resource_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=profile_PlatformProfile_strategy)
@settings(max_examples=50)
def test_profile_platformprofile_instantiation(instance):
    assert isinstance(instance, profile_PlatformProfile)



@given(instance=profile_PlatformProfile_strategy)
def test_profile_platformprofile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
