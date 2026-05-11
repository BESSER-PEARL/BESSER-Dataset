import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    noreflectioncompany::Employee,
    noreflectioncompany::Company,
    CompanySizeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_noreflectioncompany::employee_is_not_abstract():
    assert not inspect.isabstract(noreflectioncompany::Employee)


def test_noreflectioncompany::employee_constructor_exists():
    assert callable(noreflectioncompany::Employee.__init__)


def test_noreflectioncompany::employee_constructor_args():
    sig = inspect.signature(noreflectioncompany::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "hasNameAsAttribute" in params, "Missing parameter 'hasNameAsAttribute'"
    assert "name" in params, "Missing parameter 'name'"

def test_noreflectioncompany::employee_has_hasNameAsAttribute():
    assert hasattr(noreflectioncompany::Employee, "hasNameAsAttribute")
    descriptor = None
    for klass in noreflectioncompany::Employee.__mro__:
        if "hasNameAsAttribute" in klass.__dict__:
            descriptor = klass.__dict__["hasNameAsAttribute"]
            break
    assert isinstance(descriptor, property)

def test_noreflectioncompany::employee_has_name():
    assert hasattr(noreflectioncompany::Employee, "name")
    descriptor = None
    for klass in noreflectioncompany::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_noreflectioncompany::company_is_not_abstract():
    assert not inspect.isabstract(noreflectioncompany::Company)


def test_noreflectioncompany::company_constructor_exists():
    assert callable(noreflectioncompany::Company.__init__)


def test_noreflectioncompany::company_constructor_args():
    sig = inspect.signature(noreflectioncompany::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"

def test_noreflectioncompany::company_has_name():
    assert hasattr(noreflectioncompany::Company, "name")
    descriptor = None
    for klass in noreflectioncompany::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_noreflectioncompany::company_has_size():
    assert hasattr(noreflectioncompany::Company, "size")
    descriptor = None
    for klass in noreflectioncompany::Company.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_companysizekind_exists():
    # Check that the Enumeration exists
    assert CompanySizeKind is not None

def test_companysizekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompanySizeKind]
    expected_literals = [
        "small",
        "large",
        "medium",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompanySizeKind"


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
noreflectioncompany::Employee_strategy = st.builds(
    noreflectioncompany::Employee,
    hasNameAsAttribute=
        st.booleans(),
    name=
        safe_text
)
noreflectioncompany::Company_strategy = st.builds(
    noreflectioncompany::Company,
    name=
        safe_text,
    size=
        safe_text
)

@given(instance=noreflectioncompany::Employee_strategy)
@settings(max_examples=50)
def test_noreflectioncompany::employee_instantiation(instance):
    assert isinstance(instance, noreflectioncompany::Employee)

@given(instance=noreflectioncompany::Employee_strategy)
def test_noreflectioncompany::employee_hasNameAsAttribute_type(instance):
    assert isinstance(instance.hasNameAsAttribute, bool)


@given(instance=noreflectioncompany::Employee_strategy)
def test_noreflectioncompany::employee_hasNameAsAttribute_setter(instance):
    original = instance.hasNameAsAttribute
    instance.hasNameAsAttribute = original
    assert instance.hasNameAsAttribute == original

@given(instance=noreflectioncompany::Employee_strategy)
def test_noreflectioncompany::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=noreflectioncompany::Employee_strategy)
def test_noreflectioncompany::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=noreflectioncompany::Employee_strategy)
@settings(max_examples=30)
def test_noreflectioncompany::employee_nomanagerimpliesdirectreports_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.noManagerImpliesDirectReports(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.noManagerImpliesDirectReports).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'noManagerImpliesDirectReports' in noreflectioncompany::Employee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'noManagerImpliesDirectReports' in noreflectioncompany::Employee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'noManagerImpliesDirectReports' in noreflectioncompany::Employee is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=noreflectioncompany::Employee_strategy)
@settings(max_examples=30)
def test_noreflectioncompany::employee_reportsto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reportsTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reportsTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reportsTo' in noreflectioncompany::Employee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reportsTo' in noreflectioncompany::Employee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reportsTo' in noreflectioncompany::Employee is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=noreflectioncompany::Employee_strategy)
@settings(max_examples=30)
def test_noreflectioncompany::employee_hasnameasoperation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasNameAsOperation()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasNameAsOperation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasNameAsOperation' in noreflectioncompany::Employee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasNameAsOperation' in noreflectioncompany::Employee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasNameAsOperation' in noreflectioncompany::Employee is not implemented or raised an error")

@given(instance=noreflectioncompany::Company_strategy)
@settings(max_examples=50)
def test_noreflectioncompany::company_instantiation(instance):
    assert isinstance(instance, noreflectioncompany::Company)

@given(instance=noreflectioncompany::Company_strategy)
def test_noreflectioncompany::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=noreflectioncompany::Company_strategy)
def test_noreflectioncompany::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=noreflectioncompany::Company_strategy)
def test_noreflectioncompany::company_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=noreflectioncompany::Company_strategy)
def test_noreflectioncompany::company_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=noreflectioncompany::Company_strategy)
@settings(max_examples=30)
def test_noreflectioncompany::company_dummyinvariant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dummyInvariant(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dummyInvariant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dummyInvariant' in noreflectioncompany::Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dummyInvariant' in noreflectioncompany::Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dummyInvariant' in noreflectioncompany::Company is not implemented or raised an error")
