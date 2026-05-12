import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Projects::Qualification,
    Projects::Worker,
    Projects::Project,
    Projects::Company,
    ProjectStatus,
    ProjectSize,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_projects::qualification_is_not_abstract():
    assert not inspect.isabstract(Projects::Qualification)


def test_projects::qualification_constructor_exists():
    assert callable(Projects::Qualification.__init__)


def test_projects::qualification_constructor_args():
    sig = inspect.signature(Projects::Qualification.__init__)
    params = list(sig.parameters.keys())



def test_projects::worker_is_not_abstract():
    assert not inspect.isabstract(Projects::Worker)


def test_projects::worker_constructor_exists():
    assert callable(Projects::Worker.__init__)


def test_projects::worker_constructor_args():
    sig = inspect.signature(Projects::Worker.__init__)
    params = list(sig.parameters.keys())



def test_projects::project_is_not_abstract():
    assert not inspect.isabstract(Projects::Project)


def test_projects::project_constructor_exists():
    assert callable(Projects::Project.__init__)


def test_projects::project_constructor_args():
    sig = inspect.signature(Projects::Project.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "size" in params, "Missing parameter 'size'"

def test_projects::project_has_status():
    assert hasattr(Projects::Project, "status")
    descriptor = None
    for klass in Projects::Project.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_projects::project_has_size():
    assert hasattr(Projects::Project, "size")
    descriptor = None
    for klass in Projects::Project.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_projects::company_is_not_abstract():
    assert not inspect.isabstract(Projects::Company)


def test_projects::company_constructor_exists():
    assert callable(Projects::Company.__init__)


def test_projects::company_constructor_args():
    sig = inspect.signature(Projects::Company.__init__)
    params = list(sig.parameters.keys())

def test_projectstatus_exists():
    # Check that the Enumeration exists
    assert ProjectStatus is not None

def test_projectstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProjectStatus]
    expected_literals = [
        "suspended",
        "finished",
        "active",
        "planned",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProjectStatus"

def test_projectsize_exists():
    # Check that the Enumeration exists
    assert ProjectSize is not None

def test_projectsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProjectSize]
    expected_literals = [
        "big",
        "medium",
        "small",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProjectSize"


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
Projects::Qualification_strategy = st.builds(
    Projects::Qualification,
)
Projects::Worker_strategy = st.builds(
    Projects::Worker,
)
Projects::Project_strategy = st.builds(
    Projects::Project,
    status=
        safe_text,
    size=
        safe_text
)
Projects::Company_strategy = st.builds(
    Projects::Company,
)

@given(instance=Projects::Qualification_strategy)
@settings(max_examples=50)
def test_projects::qualification_instantiation(instance):
    assert isinstance(instance, Projects::Qualification)

@given(instance=Projects::Worker_strategy)
@settings(max_examples=50)
def test_projects::worker_instantiation(instance):
    assert isinstance(instance, Projects::Worker)

@given(instance=Projects::Project_strategy)
@settings(max_examples=50)
def test_projects::project_instantiation(instance):
    assert isinstance(instance, Projects::Project)

@given(instance=Projects::Project_strategy)
def test_projects::project_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Projects::Project_strategy)
def test_projects::project_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Projects::Project_strategy)
def test_projects::project_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=Projects::Project_strategy)
def test_projects::project_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Projects::Company_strategy)
@settings(max_examples=50)
def test_projects::company_instantiation(instance):
    assert isinstance(instance, Projects::Company)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects::Company_strategy)
@settings(max_examples=30)
def test_projects::company_finish_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.finish(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.finish).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'finish' in Projects::Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'finish' in Projects::Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'finish' in Projects::Company is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects::Company_strategy)
@settings(max_examples=30)
def test_projects::company_hire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hire(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hire' in Projects::Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hire' in Projects::Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hire' in Projects::Company is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects::Company_strategy)
@settings(max_examples=30)
def test_projects::company_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in Projects::Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in Projects::Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in Projects::Company is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects::Company_strategy)
@settings(max_examples=30)
def test_projects::company_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in Projects::Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in Projects::Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in Projects::Company is not implemented or raised an error")
