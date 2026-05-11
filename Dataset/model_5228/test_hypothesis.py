import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    projectPlanning::Assignment,
    projectPlanning::Rating,
    projectPlanning::Project,
    projectPlanning::Employee,
    projectPlanning::Capability,
    projectPlanning::ProjectPlan,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_projectplanning::assignment_is_not_abstract():
    assert not inspect.isabstract(projectPlanning::Assignment)


def test_projectplanning::assignment_constructor_exists():
    assert callable(projectPlanning::Assignment.__init__)


def test_projectplanning::assignment_constructor_args():
    sig = inspect.signature(projectPlanning::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_projectplanning::rating_is_not_abstract():
    assert not inspect.isabstract(projectPlanning::Rating)


def test_projectplanning::rating_constructor_exists():
    assert callable(projectPlanning::Rating.__init__)


def test_projectplanning::rating_constructor_args():
    sig = inspect.signature(projectPlanning::Rating.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"

def test_projectplanning::rating_has_rating():
    assert hasattr(projectPlanning::Rating, "rating")
    descriptor = None
    for klass in projectPlanning::Rating.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_projectplanning::project_is_not_abstract():
    assert not inspect.isabstract(projectPlanning::Project)


def test_projectplanning::project_constructor_exists():
    assert callable(projectPlanning::Project.__init__)


def test_projectplanning::project_constructor_args():
    sig = inspect.signature(projectPlanning::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "requiresResources" in params, "Missing parameter 'requiresResources'"

def test_projectplanning::project_has_name():
    assert hasattr(projectPlanning::Project, "name")
    descriptor = None
    for klass in projectPlanning::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projectplanning::project_has_requiresResources():
    assert hasattr(projectPlanning::Project, "requiresResources")
    descriptor = None
    for klass in projectPlanning::Project.__mro__:
        if "requiresResources" in klass.__dict__:
            descriptor = klass.__dict__["requiresResources"]
            break
    assert isinstance(descriptor, property)



def test_projectplanning::employee_is_not_abstract():
    assert not inspect.isabstract(projectPlanning::Employee)


def test_projectplanning::employee_constructor_exists():
    assert callable(projectPlanning::Employee.__init__)


def test_projectplanning::employee_constructor_args():
    sig = inspect.signature(projectPlanning::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hasResource" in params, "Missing parameter 'hasResource'"

def test_projectplanning::employee_has_name():
    assert hasattr(projectPlanning::Employee, "name")
    descriptor = None
    for klass in projectPlanning::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projectplanning::employee_has_hasResource():
    assert hasattr(projectPlanning::Employee, "hasResource")
    descriptor = None
    for klass in projectPlanning::Employee.__mro__:
        if "hasResource" in klass.__dict__:
            descriptor = klass.__dict__["hasResource"]
            break
    assert isinstance(descriptor, property)



def test_projectplanning::capability_is_not_abstract():
    assert not inspect.isabstract(projectPlanning::Capability)


def test_projectplanning::capability_constructor_exists():
    assert callable(projectPlanning::Capability.__init__)


def test_projectplanning::capability_constructor_args():
    sig = inspect.signature(projectPlanning::Capability.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_projectplanning::capability_has_name():
    assert hasattr(projectPlanning::Capability, "name")
    descriptor = None
    for klass in projectPlanning::Capability.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_projectplanning::projectplan_is_not_abstract():
    assert not inspect.isabstract(projectPlanning::ProjectPlan)


def test_projectplanning::projectplan_constructor_exists():
    assert callable(projectPlanning::ProjectPlan.__init__)


def test_projectplanning::projectplan_constructor_args():
    sig = inspect.signature(projectPlanning::ProjectPlan.__init__)
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
projectPlanning::Assignment_strategy = st.builds(
    projectPlanning::Assignment,
)
projectPlanning::Rating_strategy = st.builds(
    projectPlanning::Rating,
    rating=
        st.integers()
)
projectPlanning::Project_strategy = st.builds(
    projectPlanning::Project,
    name=
        safe_text,
    requiresResources=
        st.integers()
)
projectPlanning::Employee_strategy = st.builds(
    projectPlanning::Employee,
    name=
        safe_text,
    hasResource=
        st.integers()
)
projectPlanning::Capability_strategy = st.builds(
    projectPlanning::Capability,
    name=
        safe_text
)
projectPlanning::ProjectPlan_strategy = st.builds(
    projectPlanning::ProjectPlan,
)

@given(instance=projectPlanning::Assignment_strategy)
@settings(max_examples=50)
def test_projectplanning::assignment_instantiation(instance):
    assert isinstance(instance, projectPlanning::Assignment)

@given(instance=projectPlanning::Rating_strategy)
@settings(max_examples=50)
def test_projectplanning::rating_instantiation(instance):
    assert isinstance(instance, projectPlanning::Rating)

@given(instance=projectPlanning::Rating_strategy)
def test_projectplanning::rating_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=projectPlanning::Rating_strategy)
def test_projectplanning::rating_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=projectPlanning::Project_strategy)
@settings(max_examples=50)
def test_projectplanning::project_instantiation(instance):
    assert isinstance(instance, projectPlanning::Project)

@given(instance=projectPlanning::Project_strategy)
def test_projectplanning::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectPlanning::Project_strategy)
def test_projectplanning::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectPlanning::Project_strategy)
def test_projectplanning::project_requiresResources_type(instance):
    assert isinstance(instance.requiresResources, int)


@given(instance=projectPlanning::Project_strategy)
def test_projectplanning::project_requiresResources_setter(instance):
    original = instance.requiresResources
    instance.requiresResources = original
    assert instance.requiresResources == original

@given(instance=projectPlanning::Employee_strategy)
@settings(max_examples=50)
def test_projectplanning::employee_instantiation(instance):
    assert isinstance(instance, projectPlanning::Employee)

@given(instance=projectPlanning::Employee_strategy)
def test_projectplanning::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectPlanning::Employee_strategy)
def test_projectplanning::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectPlanning::Employee_strategy)
def test_projectplanning::employee_hasResource_type(instance):
    assert isinstance(instance.hasResource, int)


@given(instance=projectPlanning::Employee_strategy)
def test_projectplanning::employee_hasResource_setter(instance):
    original = instance.hasResource
    instance.hasResource = original
    assert instance.hasResource == original

@given(instance=projectPlanning::Capability_strategy)
@settings(max_examples=50)
def test_projectplanning::capability_instantiation(instance):
    assert isinstance(instance, projectPlanning::Capability)

@given(instance=projectPlanning::Capability_strategy)
def test_projectplanning::capability_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectPlanning::Capability_strategy)
def test_projectplanning::capability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectPlanning::ProjectPlan_strategy)
@settings(max_examples=50)
def test_projectplanning::projectplan_instantiation(instance):
    assert isinstance(instance, projectPlanning::ProjectPlan)
