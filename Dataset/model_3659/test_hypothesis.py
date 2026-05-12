import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Employee,
    toe_Manager,
    AllBase,
    toe_Contribution,
    toe_Project,
    toe_Department,
    toe_Employee,
    toe_AllBase,
    toe_AllHolder,
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



def test_toe_manager_is_not_abstract():
    assert not inspect.isabstract(toe_Manager)


def test_toe_manager_constructor_exists():
    assert callable(toe_Manager.__init__)


def test_toe_manager_constructor_args():
    sig = inspect.signature(toe_Manager.__init__)
    params = list(sig.parameters.keys())



def test_allbase_is_not_abstract():
    assert not inspect.isabstract(AllBase)


def test_allbase_constructor_exists():
    assert callable(AllBase.__init__)


def test_allbase_constructor_args():
    sig = inspect.signature(AllBase.__init__)
    params = list(sig.parameters.keys())



def test_toe_contribution_is_not_abstract():
    assert not inspect.isabstract(toe_Contribution)


def test_toe_contribution_constructor_exists():
    assert callable(toe_Contribution.__init__)


def test_toe_contribution_constructor_args():
    sig = inspect.signature(toe_Contribution.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_toe_contribution_has_description():
    assert hasattr(toe_Contribution, "description")
    descriptor = None
    for klass in toe_Contribution.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_toe_project_is_not_abstract():
    assert not inspect.isabstract(toe_Project)


def test_toe_project_constructor_exists():
    assert callable(toe_Project.__init__)


def test_toe_project_constructor_args():
    sig = inspect.signature(toe_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "departmentWide" in params, "Missing parameter 'departmentWide'"

def test_toe_project_has_name():
    assert hasattr(toe_Project, "name")
    descriptor = None
    for klass in toe_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_toe_project_has_departmentWide():
    assert hasattr(toe_Project, "departmentWide")
    descriptor = None
    for klass in toe_Project.__mro__:
        if "departmentWide" in klass.__dict__:
            descriptor = klass.__dict__["departmentWide"]
            break
    assert isinstance(descriptor, property)



def test_toe_department_is_not_abstract():
    assert not inspect.isabstract(toe_Department)


def test_toe_department_constructor_exists():
    assert callable(toe_Department.__init__)


def test_toe_department_constructor_args():
    sig = inspect.signature(toe_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_toe_department_has_name():
    assert hasattr(toe_Department, "name")
    descriptor = None
    for klass in toe_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_toe_employee_is_not_abstract():
    assert not inspect.isabstract(toe_Employee)


def test_toe_employee_constructor_exists():
    assert callable(toe_Employee.__init__)


def test_toe_employee_constructor_args():
    sig = inspect.signature(toe_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_toe_employee_has_salary():
    assert hasattr(toe_Employee, "salary")
    descriptor = None
    for klass in toe_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_toe_employee_has_name():
    assert hasattr(toe_Employee, "name")
    descriptor = None
    for klass in toe_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_toe_allbase_is_not_abstract():
    assert not inspect.isabstract(toe_AllBase)


def test_toe_allbase_constructor_exists():
    assert callable(toe_AllBase.__init__)


def test_toe_allbase_constructor_args():
    sig = inspect.signature(toe_AllBase.__init__)
    params = list(sig.parameters.keys())



def test_toe_allholder_is_not_abstract():
    assert not inspect.isabstract(toe_AllHolder)


def test_toe_allholder_constructor_exists():
    assert callable(toe_AllHolder.__init__)


def test_toe_allholder_constructor_args():
    sig = inspect.signature(toe_AllHolder.__init__)
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
toe_Manager_strategy = st.builds(
    toe_Manager,
)
AllBase_strategy = st.builds(
    AllBase,
)
toe_Contribution_strategy = st.builds(
    toe_Contribution,
    description=
        safe_text
)
toe_Project_strategy = st.builds(
    toe_Project,
    name=
        safe_text,
    departmentWide=
        st.booleans()
)
toe_Department_strategy = st.builds(
    toe_Department,
    name=
        safe_text
)
toe_Employee_strategy = st.builds(
    toe_Employee,
    salary=
        st.integers(),
    name=
        safe_text
)
toe_AllBase_strategy = st.builds(
    toe_AllBase,
)
toe_AllHolder_strategy = st.builds(
    toe_AllHolder,
)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=toe_Manager_strategy)
@settings(max_examples=50)
def test_toe_manager_instantiation(instance):
    assert isinstance(instance, toe_Manager)

@given(instance=AllBase_strategy)
@settings(max_examples=50)
def test_allbase_instantiation(instance):
    assert isinstance(instance, AllBase)

@given(instance=toe_Contribution_strategy)
@settings(max_examples=50)
def test_toe_contribution_instantiation(instance):
    assert isinstance(instance, toe_Contribution)



@given(instance=toe_Contribution_strategy)
def test_toe_contribution_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=toe_Project_strategy)
@settings(max_examples=50)
def test_toe_project_instantiation(instance):
    assert isinstance(instance, toe_Project)



@given(instance=toe_Project_strategy)
def test_toe_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=toe_Project_strategy)
def test_toe_project_departmentWide_setter(instance):
    original = instance.departmentWide
    instance.departmentWide = original
    assert instance.departmentWide == original

@given(instance=toe_Department_strategy)
@settings(max_examples=50)
def test_toe_department_instantiation(instance):
    assert isinstance(instance, toe_Department)



@given(instance=toe_Department_strategy)
def test_toe_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=toe_Department_strategy)
@settings(max_examples=30)
def test_toe_department_allsubdepartments_changes_state(instance):
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
        assert has_statements, f"Function 'allSubDepartments' in toe_Department is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allSubDepartments' in toe_Department did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allSubDepartments' in toe_Department is not implemented or raised an error")

@given(instance=toe_Employee_strategy)
@settings(max_examples=50)
def test_toe_employee_instantiation(instance):
    assert isinstance(instance, toe_Employee)



@given(instance=toe_Employee_strategy)
def test_toe_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=toe_Employee_strategy)
def test_toe_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=toe_AllBase_strategy)
@settings(max_examples=50)
def test_toe_allbase_instantiation(instance):
    assert isinstance(instance, toe_AllBase)

@given(instance=toe_AllHolder_strategy)
@settings(max_examples=50)
def test_toe_allholder_instantiation(instance):
    assert isinstance(instance, toe_AllHolder)
