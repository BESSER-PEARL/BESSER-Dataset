import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Employee,
    toe::Manager,
    AllBase,
    toe::Project,
    toe::Department,
    toe::Contribution,
    toe::Employee,
    toe::AllBase,
    toe::AllHolder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_toe::manager_is_not_abstract():
    assert not inspect.isabstract(toe::Manager)


def test_toe::manager_constructor_exists():
    assert callable(toe::Manager.__init__)


def test_toe::manager_constructor_args():
    sig = inspect.signature(toe::Manager.__init__)
    params = list(sig.parameters.keys())



def test_allbase_is_not_abstract():
    assert not inspect.isabstract(AllBase)


def test_allbase_constructor_exists():
    assert callable(AllBase.__init__)


def test_allbase_constructor_args():
    sig = inspect.signature(AllBase.__init__)
    params = list(sig.parameters.keys())



def test_toe::project_is_not_abstract():
    assert not inspect.isabstract(toe::Project)


def test_toe::project_constructor_exists():
    assert callable(toe::Project.__init__)


def test_toe::project_constructor_args():
    sig = inspect.signature(toe::Project.__init__)
    params = list(sig.parameters.keys())
    assert "departmentWide" in params, "Missing parameter 'departmentWide'"
    assert "name" in params, "Missing parameter 'name'"

def test_toe::project_has_departmentWide():
    assert hasattr(toe::Project, "departmentWide")
    descriptor = None
    for klass in toe::Project.__mro__:
        if "departmentWide" in klass.__dict__:
            descriptor = klass.__dict__["departmentWide"]
            break
    assert isinstance(descriptor, property)

def test_toe::project_has_name():
    assert hasattr(toe::Project, "name")
    descriptor = None
    for klass in toe::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_toe::department_is_not_abstract():
    assert not inspect.isabstract(toe::Department)


def test_toe::department_constructor_exists():
    assert callable(toe::Department.__init__)


def test_toe::department_constructor_args():
    sig = inspect.signature(toe::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_toe::department_has_name():
    assert hasattr(toe::Department, "name")
    descriptor = None
    for klass in toe::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_toe::contribution_is_not_abstract():
    assert not inspect.isabstract(toe::Contribution)


def test_toe::contribution_constructor_exists():
    assert callable(toe::Contribution.__init__)


def test_toe::contribution_constructor_args():
    sig = inspect.signature(toe::Contribution.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_toe::contribution_has_description():
    assert hasattr(toe::Contribution, "description")
    descriptor = None
    for klass in toe::Contribution.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_toe::employee_is_not_abstract():
    assert not inspect.isabstract(toe::Employee)


def test_toe::employee_constructor_exists():
    assert callable(toe::Employee.__init__)


def test_toe::employee_constructor_args():
    sig = inspect.signature(toe::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_toe::employee_has_salary():
    assert hasattr(toe::Employee, "salary")
    descriptor = None
    for klass in toe::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_toe::employee_has_name():
    assert hasattr(toe::Employee, "name")
    descriptor = None
    for klass in toe::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_toe::allbase_is_not_abstract():
    assert not inspect.isabstract(toe::AllBase)


def test_toe::allbase_constructor_exists():
    assert callable(toe::AllBase.__init__)


def test_toe::allbase_constructor_args():
    sig = inspect.signature(toe::AllBase.__init__)
    params = list(sig.parameters.keys())



def test_toe::allholder_is_not_abstract():
    assert not inspect.isabstract(toe::AllHolder)


def test_toe::allholder_constructor_exists():
    assert callable(toe::AllHolder.__init__)


def test_toe::allholder_constructor_args():
    sig = inspect.signature(toe::AllHolder.__init__)
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
Employee_strategy = st.builds(
    Employee,
)
toe::Manager_strategy = st.builds(
    toe::Manager,
)
AllBase_strategy = st.builds(
    AllBase,
)
toe::Project_strategy = st.builds(
    toe::Project,
    departmentWide=
        st.booleans(),
    name=
        safe_text
)
toe::Department_strategy = st.builds(
    toe::Department,
    name=
        safe_text
)
toe::Contribution_strategy = st.builds(
    toe::Contribution,
    description=
        safe_text
)
toe::Employee_strategy = st.builds(
    toe::Employee,
    salary=
        st.integers(),
    name=
        safe_text
)
toe::AllBase_strategy = st.builds(
    toe::AllBase,
)
toe::AllHolder_strategy = st.builds(
    toe::AllHolder,
)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=toe::Manager_strategy)
@settings(max_examples=50)
def test_toe::manager_instantiation(instance):
    assert isinstance(instance, toe::Manager)

@given(instance=AllBase_strategy)
@settings(max_examples=50)
def test_allbase_instantiation(instance):
    assert isinstance(instance, AllBase)

@given(instance=toe::Project_strategy)
@settings(max_examples=50)
def test_toe::project_instantiation(instance):
    assert isinstance(instance, toe::Project)

@given(instance=toe::Project_strategy)
def test_toe::project_departmentWide_type(instance):
    assert isinstance(instance.departmentWide, bool)


@given(instance=toe::Project_strategy)
def test_toe::project_departmentWide_setter(instance):
    original = instance.departmentWide
    instance.departmentWide = original
    assert instance.departmentWide == original

@given(instance=toe::Project_strategy)
def test_toe::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=toe::Project_strategy)
def test_toe::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=toe::Department_strategy)
@settings(max_examples=50)
def test_toe::department_instantiation(instance):
    assert isinstance(instance, toe::Department)

@given(instance=toe::Department_strategy)
def test_toe::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=toe::Department_strategy)
def test_toe::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=toe::Department_strategy)
@settings(max_examples=30)
def test_toe::department_allsubdepartments_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allSubDepartments()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allSubDepartments).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allSubDepartments' in toe::Department is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allSubDepartments' in toe::Department did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allSubDepartments' in toe::Department is not implemented or raised an error")

@given(instance=toe::Contribution_strategy)
@settings(max_examples=50)
def test_toe::contribution_instantiation(instance):
    assert isinstance(instance, toe::Contribution)

@given(instance=toe::Contribution_strategy)
def test_toe::contribution_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=toe::Contribution_strategy)
def test_toe::contribution_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=toe::Employee_strategy)
@settings(max_examples=50)
def test_toe::employee_instantiation(instance):
    assert isinstance(instance, toe::Employee)

@given(instance=toe::Employee_strategy)
def test_toe::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=toe::Employee_strategy)
def test_toe::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=toe::Employee_strategy)
def test_toe::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=toe::Employee_strategy)
def test_toe::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=toe::AllBase_strategy)
@settings(max_examples=50)
def test_toe::allbase_instantiation(instance):
    assert isinstance(instance, toe::AllBase)

@given(instance=toe::AllHolder_strategy)
@settings(max_examples=50)
def test_toe::allholder_instantiation(instance):
    assert isinstance(instance, toe::AllHolder)
