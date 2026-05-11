import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    chartDsl::Task,
    chartDsl::Project,
    chartDsl::Employee,
    chartDsl::Company,
    ProjectType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_chartdsl::task_is_not_abstract():
    assert not inspect.isabstract(chartDsl::Task)


def test_chartdsl::task_constructor_exists():
    assert callable(chartDsl::Task.__init__)


def test_chartdsl::task_constructor_args():
    sig = inspect.signature(chartDsl::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl::task_has_name():
    assert hasattr(chartDsl::Task, "name")
    descriptor = None
    for klass in chartDsl::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chartdsl::project_is_not_abstract():
    assert not inspect.isabstract(chartDsl::Project)


def test_chartdsl::project_constructor_exists():
    assert callable(chartDsl::Project.__init__)


def test_chartdsl::project_constructor_args():
    sig = inspect.signature(chartDsl::Project.__init__)
    params = list(sig.parameters.keys())
    assert "projectType" in params, "Missing parameter 'projectType'"
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl::project_has_projectType():
    assert hasattr(chartDsl::Project, "projectType")
    descriptor = None
    for klass in chartDsl::Project.__mro__:
        if "projectType" in klass.__dict__:
            descriptor = klass.__dict__["projectType"]
            break
    assert isinstance(descriptor, property)

def test_chartdsl::project_has_name():
    assert hasattr(chartDsl::Project, "name")
    descriptor = None
    for klass in chartDsl::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chartdsl::employee_is_not_abstract():
    assert not inspect.isabstract(chartDsl::Employee)


def test_chartdsl::employee_constructor_exists():
    assert callable(chartDsl::Employee.__init__)


def test_chartdsl::employee_constructor_args():
    sig = inspect.signature(chartDsl::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl::employee_has_name():
    assert hasattr(chartDsl::Employee, "name")
    descriptor = None
    for klass in chartDsl::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chartdsl::company_is_not_abstract():
    assert not inspect.isabstract(chartDsl::Company)


def test_chartdsl::company_constructor_exists():
    assert callable(chartDsl::Company.__init__)


def test_chartdsl::company_constructor_args():
    sig = inspect.signature(chartDsl::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_chartdsl::company_has_name():
    assert hasattr(chartDsl::Company, "name")
    descriptor = None
    for klass in chartDsl::Company.__mro__:
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
        "Development",
        "Regie",
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
chartDsl::Task_strategy = st.builds(
    chartDsl::Task,
    name=
        safe_text
)
chartDsl::Project_strategy = st.builds(
    chartDsl::Project,
    projectType=
        safe_text,
    name=
        safe_text
)
chartDsl::Employee_strategy = st.builds(
    chartDsl::Employee,
    name=
        safe_text
)
chartDsl::Company_strategy = st.builds(
    chartDsl::Company,
    name=
        safe_text
)

@given(instance=chartDsl::Task_strategy)
@settings(max_examples=50)
def test_chartdsl::task_instantiation(instance):
    assert isinstance(instance, chartDsl::Task)

@given(instance=chartDsl::Task_strategy)
def test_chartdsl::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=chartDsl::Task_strategy)
def test_chartdsl::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chartDsl::Project_strategy)
@settings(max_examples=50)
def test_chartdsl::project_instantiation(instance):
    assert isinstance(instance, chartDsl::Project)

@given(instance=chartDsl::Project_strategy)
def test_chartdsl::project_projectType_type(instance):
    assert isinstance(instance.projectType, str)


@given(instance=chartDsl::Project_strategy)
def test_chartdsl::project_projectType_setter(instance):
    original = instance.projectType
    instance.projectType = original
    assert instance.projectType == original

@given(instance=chartDsl::Project_strategy)
def test_chartdsl::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=chartDsl::Project_strategy)
def test_chartdsl::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chartDsl::Employee_strategy)
@settings(max_examples=50)
def test_chartdsl::employee_instantiation(instance):
    assert isinstance(instance, chartDsl::Employee)

@given(instance=chartDsl::Employee_strategy)
def test_chartdsl::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=chartDsl::Employee_strategy)
def test_chartdsl::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chartDsl::Company_strategy)
@settings(max_examples=50)
def test_chartdsl::company_instantiation(instance):
    assert isinstance(instance, chartDsl::Company)

@given(instance=chartDsl::Company_strategy)
def test_chartdsl::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=chartDsl::Company_strategy)
def test_chartdsl::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
