import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    projectDsl_Task,
    projectDsl_Employee,
    projectDsl_Project,
    projectDsl_Employees,
    projectDsl_Company,
    taskType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_projectdsl_task_is_not_abstract():
    assert not inspect.isabstract(projectDsl_Task)


def test_projectdsl_task_constructor_exists():
    assert callable(projectDsl_Task.__init__)


def test_projectdsl_task_constructor_args():
    sig = inspect.signature(projectDsl_Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_projectdsl_task_has_name():
    assert hasattr(projectDsl_Task, "name")
    descriptor = None
    for klass in projectDsl_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl_task_has_type():
    assert hasattr(projectDsl_Task, "type")
    descriptor = None
    for klass in projectDsl_Task.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_projectdsl_employee_is_not_abstract():
    assert not inspect.isabstract(projectDsl_Employee)


def test_projectdsl_employee_constructor_exists():
    assert callable(projectDsl_Employee.__init__)


def test_projectdsl_employee_constructor_args():
    sig = inspect.signature(projectDsl_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "name" in params, "Missing parameter 'name'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_projectdsl_employee_has_height():
    assert hasattr(projectDsl_Employee, "height")
    descriptor = None
    for klass in projectDsl_Employee.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl_employee_has_name():
    assert hasattr(projectDsl_Employee, "name")
    descriptor = None
    for klass in projectDsl_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl_employee_has_weight():
    assert hasattr(projectDsl_Employee, "weight")
    descriptor = None
    for klass in projectDsl_Employee.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_projectdsl_project_is_not_abstract():
    assert not inspect.isabstract(projectDsl_Project)


def test_projectdsl_project_constructor_exists():
    assert callable(projectDsl_Project.__init__)


def test_projectdsl_project_constructor_args():
    sig = inspect.signature(projectDsl_Project.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_projectdsl_project_has_type():
    assert hasattr(projectDsl_Project, "type")
    descriptor = None
    for klass in projectDsl_Project.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_projectdsl_project_has_name():
    assert hasattr(projectDsl_Project, "name")
    descriptor = None
    for klass in projectDsl_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_projectdsl_employees_is_not_abstract():
    assert not inspect.isabstract(projectDsl_Employees)


def test_projectdsl_employees_constructor_exists():
    assert callable(projectDsl_Employees.__init__)


def test_projectdsl_employees_constructor_args():
    sig = inspect.signature(projectDsl_Employees.__init__)
    params = list(sig.parameters.keys())



def test_projectdsl_company_is_not_abstract():
    assert not inspect.isabstract(projectDsl_Company)


def test_projectdsl_company_constructor_exists():
    assert callable(projectDsl_Company.__init__)


def test_projectdsl_company_constructor_args():
    sig = inspect.signature(projectDsl_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_projectdsl_company_has_name():
    assert hasattr(projectDsl_Company, "name")
    descriptor = None
    for klass in projectDsl_Company.__mro__:
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
        "development",
        "documentation",
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
projectDsl_Task_strategy = st.builds(
    projectDsl_Task,
    name=
        safe_text,
    type=
        safe_text
)
projectDsl_Employee_strategy = st.builds(
    projectDsl_Employee,
    height=
        st.integers(),
    name=
        safe_text,
    weight=
        st.integers()
)
projectDsl_Project_strategy = st.builds(
    projectDsl_Project,
    type=
        safe_text,
    name=
        safe_text
)
projectDsl_Employees_strategy = st.builds(
    projectDsl_Employees,
)
projectDsl_Company_strategy = st.builds(
    projectDsl_Company,
    name=
        safe_text
)

@given(instance=projectDsl_Task_strategy)
@settings(max_examples=50)
def test_projectdsl_task_instantiation(instance):
    assert isinstance(instance, projectDsl_Task)



@given(instance=projectDsl_Task_strategy)
def test_projectdsl_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=projectDsl_Task_strategy)
def test_projectdsl_task_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=projectDsl_Employee_strategy)
@settings(max_examples=50)
def test_projectdsl_employee_instantiation(instance):
    assert isinstance(instance, projectDsl_Employee)



@given(instance=projectDsl_Employee_strategy)
def test_projectdsl_employee_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=projectDsl_Employee_strategy)
def test_projectdsl_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=projectDsl_Employee_strategy)
def test_projectdsl_employee_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=projectDsl_Project_strategy)
@settings(max_examples=50)
def test_projectdsl_project_instantiation(instance):
    assert isinstance(instance, projectDsl_Project)



@given(instance=projectDsl_Project_strategy)
def test_projectdsl_project_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=projectDsl_Project_strategy)
def test_projectdsl_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=projectDsl_Employees_strategy)
@settings(max_examples=50)
def test_projectdsl_employees_instantiation(instance):
    assert isinstance(instance, projectDsl_Employees)

@given(instance=projectDsl_Company_strategy)
@settings(max_examples=50)
def test_projectdsl_company_instantiation(instance):
    assert isinstance(instance, projectDsl_Company)



@given(instance=projectDsl_Company_strategy)
def test_projectdsl_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
