import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    chartDsl_Task,
    chartDsl_Project,
    chartDsl_Employee,
    chartDsl_Company,
    ProjectType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_chartdsl_task_is_not_abstract():
    assert not inspect.isabstract(chartDsl_Task)


def test_chartdsl_task_constructor_exists():
    assert callable(chartDsl_Task.__init__)


def test_chartdsl_task_constructor_args():
    sig = inspect.signature(chartDsl_Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl_task_has_name():
    assert hasattr(chartDsl_Task, "name")
    descriptor = None
    for klass in chartDsl_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chartdsl_project_is_not_abstract():
    assert not inspect.isabstract(chartDsl_Project)


def test_chartdsl_project_constructor_exists():
    assert callable(chartDsl_Project.__init__)


def test_chartdsl_project_constructor_args():
    sig = inspect.signature(chartDsl_Project.__init__)
    params = list(sig.parameters.keys())
    assert "projectType" in params, "Missing parameter 'projectType'"
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl_project_has_projectType():
    assert hasattr(chartDsl_Project, "projectType")
    descriptor = None
    for klass in chartDsl_Project.__mro__:
        if "projectType" in klass.__dict__:
            descriptor = klass.__dict__["projectType"]
            break
    assert isinstance(descriptor, property)

def test_chartdsl_project_has_name():
    assert hasattr(chartDsl_Project, "name")
    descriptor = None
    for klass in chartDsl_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chartdsl_employee_is_not_abstract():
    assert not inspect.isabstract(chartDsl_Employee)


def test_chartdsl_employee_constructor_exists():
    assert callable(chartDsl_Employee.__init__)


def test_chartdsl_employee_constructor_args():
    sig = inspect.signature(chartDsl_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl_employee_has_name():
    assert hasattr(chartDsl_Employee, "name")
    descriptor = None
    for klass in chartDsl_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chartdsl_company_is_not_abstract():
    assert not inspect.isabstract(chartDsl_Company)


def test_chartdsl_company_constructor_exists():
    assert callable(chartDsl_Company.__init__)


def test_chartdsl_company_constructor_args():
    sig = inspect.signature(chartDsl_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl_company_has_name():
    assert hasattr(chartDsl_Company, "name")
    descriptor = None
    for klass in chartDsl_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_projecttype_exists():
    # Check that the Enumeration exists
    assert ProjectType is not None

def test_projecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProjectType]
    expected_literals = [
        "Regie",
        "Development",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProjectType"


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
chartDsl_Task_strategy = st.builds(
    chartDsl_Task,
    name=
        safe_text
)
chartDsl_Project_strategy = st.builds(
    chartDsl_Project,
    projectType=
        safe_text,
    name=
        safe_text
)
chartDsl_Employee_strategy = st.builds(
    chartDsl_Employee,
    name=
        safe_text
)
chartDsl_Company_strategy = st.builds(
    chartDsl_Company,
    name=
        safe_text
)

@given(instance=chartDsl_Task_strategy)
@settings(max_examples=50)
def test_chartdsl_task_instantiation(instance):
    assert isinstance(instance, chartDsl_Task)



@given(instance=chartDsl_Task_strategy)
def test_chartdsl_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chartDsl_Project_strategy)
@settings(max_examples=50)
def test_chartdsl_project_instantiation(instance):
    assert isinstance(instance, chartDsl_Project)



@given(instance=chartDsl_Project_strategy)
def test_chartdsl_project_projectType_setter(instance):
    original = instance.projectType
    instance.projectType = original
    assert instance.projectType == original



@given(instance=chartDsl_Project_strategy)
def test_chartdsl_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chartDsl_Employee_strategy)
@settings(max_examples=50)
def test_chartdsl_employee_instantiation(instance):
    assert isinstance(instance, chartDsl_Employee)



@given(instance=chartDsl_Employee_strategy)
def test_chartdsl_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chartDsl_Company_strategy)
@settings(max_examples=50)
def test_chartdsl_company_instantiation(instance):
    assert isinstance(instance, chartDsl_Company)



@given(instance=chartDsl_Company_strategy)
def test_chartdsl_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
