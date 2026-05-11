import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    projectDsl::Task,
    projectDsl::Employee,
    projectDsl::Project,
    projectDsl::Employees,
    projectDsl::Company,
    taskType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_projectdsl::task_is_not_abstract():
    assert not inspect.isabstract(projectDsl::Task)


def test_projectdsl::task_constructor_exists():
    assert callable(projectDsl::Task.__init__)


def test_projectdsl::task_constructor_args():
    sig = inspect.signature(projectDsl::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_projectdsl::task_has_name():
    assert hasattr(projectDsl::Task, "name")
    descriptor = None
    for klass in projectDsl::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl::task_has_type():
    assert hasattr(projectDsl::Task, "type")
    descriptor = None
    for klass in projectDsl::Task.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_projectdsl::employee_is_not_abstract():
    assert not inspect.isabstract(projectDsl::Employee)


def test_projectdsl::employee_constructor_exists():
    assert callable(projectDsl::Employee.__init__)


def test_projectdsl::employee_constructor_args():
    sig = inspect.signature(projectDsl::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "height" in params, "Missing parameter 'height'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_projectdsl::employee_has_name():
    assert hasattr(projectDsl::Employee, "name")
    descriptor = None
    for klass in projectDsl::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl::employee_has_height():
    assert hasattr(projectDsl::Employee, "height")
    descriptor = None
    for klass in projectDsl::Employee.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl::employee_has_weight():
    assert hasattr(projectDsl::Employee, "weight")
    descriptor = None
    for klass in projectDsl::Employee.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_projectdsl::project_is_not_abstract():
    assert not inspect.isabstract(projectDsl::Project)


def test_projectdsl::project_constructor_exists():
    assert callable(projectDsl::Project.__init__)


def test_projectdsl::project_constructor_args():
    sig = inspect.signature(projectDsl::Project.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_projectdsl::project_has_type():
    assert hasattr(projectDsl::Project, "type")
    descriptor = None
    for klass in projectDsl::Project.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl::project_has_name():
    assert hasattr(projectDsl::Project, "name")
    descriptor = None
    for klass in projectDsl::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_projectdsl::employees_is_not_abstract():
    assert not inspect.isabstract(projectDsl::Employees)


def test_projectdsl::employees_constructor_exists():
    assert callable(projectDsl::Employees.__init__)


def test_projectdsl::employees_constructor_args():
    sig = inspect.signature(projectDsl::Employees.__init__)
    params = list(sig.parameters.keys())



def test_projectdsl::company_is_not_abstract():
    assert not inspect.isabstract(projectDsl::Company)


def test_projectdsl::company_constructor_exists():
    assert callable(projectDsl::Company.__init__)


def test_projectdsl::company_constructor_args():
    sig = inspect.signature(projectDsl::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_projectdsl::company_has_name():
    assert hasattr(projectDsl::Company, "name")
    descriptor = None
    for klass in projectDsl::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tasktype_exists():
    # Check that the Enumeration exists
    assert taskType is not None

def test_tasktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in taskType]
    expected_literals = [
        "documentation",
        "development",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in taskType"


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
projectDsl::Task_strategy = st.builds(
    projectDsl::Task,
    name=
        safe_text,
    type=
        safe_text
)
projectDsl::Employee_strategy = st.builds(
    projectDsl::Employee,
    name=
        safe_text,
    height=
        st.integers(),
    weight=
        st.integers()
)
projectDsl::Project_strategy = st.builds(
    projectDsl::Project,
    type=
        safe_text,
    name=
        safe_text
)
projectDsl::Employees_strategy = st.builds(
    projectDsl::Employees,
)
projectDsl::Company_strategy = st.builds(
    projectDsl::Company,
    name=
        safe_text
)

@given(instance=projectDsl::Task_strategy)
@settings(max_examples=50)
def test_projectdsl::task_instantiation(instance):
    assert isinstance(instance, projectDsl::Task)

@given(instance=projectDsl::Task_strategy)
def test_projectdsl::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectDsl::Task_strategy)
def test_projectdsl::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectDsl::Task_strategy)
def test_projectdsl::task_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=projectDsl::Task_strategy)
def test_projectdsl::task_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=projectDsl::Employee_strategy)
@settings(max_examples=50)
def test_projectdsl::employee_instantiation(instance):
    assert isinstance(instance, projectDsl::Employee)

@given(instance=projectDsl::Employee_strategy)
def test_projectdsl::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectDsl::Employee_strategy)
def test_projectdsl::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectDsl::Employee_strategy)
def test_projectdsl::employee_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=projectDsl::Employee_strategy)
def test_projectdsl::employee_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=projectDsl::Employee_strategy)
def test_projectdsl::employee_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=projectDsl::Employee_strategy)
def test_projectdsl::employee_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=projectDsl::Project_strategy)
@settings(max_examples=50)
def test_projectdsl::project_instantiation(instance):
    assert isinstance(instance, projectDsl::Project)

@given(instance=projectDsl::Project_strategy)
def test_projectdsl::project_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=projectDsl::Project_strategy)
def test_projectdsl::project_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=projectDsl::Project_strategy)
def test_projectdsl::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectDsl::Project_strategy)
def test_projectdsl::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectDsl::Employees_strategy)
@settings(max_examples=50)
def test_projectdsl::employees_instantiation(instance):
    assert isinstance(instance, projectDsl::Employees)

@given(instance=projectDsl::Company_strategy)
@settings(max_examples=50)
def test_projectdsl::company_instantiation(instance):
    assert isinstance(instance, projectDsl::Company)

@given(instance=projectDsl::Company_strategy)
def test_projectdsl::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=projectDsl::Company_strategy)
def test_projectdsl::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
