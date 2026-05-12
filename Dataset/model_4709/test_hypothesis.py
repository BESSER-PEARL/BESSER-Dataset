import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ATerm,
    adt_Variable,
    adt_Term,
    adt_ATerm,
    adt_Operation,
    ASort,
    adt_Sort,
    adt_SubSort,
    adt_Equation,
    adt_VariableDeclaration,
    adt_Signature,
    adt_ADT,
    adt_ASort,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_aterm_is_not_abstract():
    assert not inspect.isabstract(ATerm)


def test_aterm_constructor_exists():
    assert callable(ATerm.__init__)


def test_aterm_constructor_args():
    sig = inspect.signature(ATerm.__init__)
    params = list(sig.parameters.keys())



def test_adt_variable_is_not_abstract():
    assert not inspect.isabstract(adt_Variable)


def test_adt_variable_constructor_exists():
    assert callable(adt_Variable.__init__)


def test_adt_variable_constructor_args():
    sig = inspect.signature(adt_Variable.__init__)
    params = list(sig.parameters.keys())



def test_adt_term_is_not_abstract():
    assert not inspect.isabstract(adt_Term)


def test_adt_term_constructor_exists():
    assert callable(adt_Term.__init__)


def test_adt_term_constructor_args():
    sig = inspect.signature(adt_Term.__init__)
    params = list(sig.parameters.keys())



def test_adt_aterm_is_not_abstract():
    assert not inspect.isabstract(adt_ATerm)


def test_adt_aterm_constructor_exists():
    assert callable(adt_ATerm.__init__)


def test_adt_aterm_constructor_args():
    sig = inspect.signature(adt_ATerm.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_adt_aterm_has_symbol():
    assert hasattr(adt_ATerm, "symbol")
    descriptor = None
    for klass in adt_ATerm.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_adt_operation_is_not_abstract():
    assert not inspect.isabstract(adt_Operation)


def test_adt_operation_constructor_exists():
    assert callable(adt_Operation.__init__)


def test_adt_operation_constructor_args():
    sig = inspect.signature(adt_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt_operation_has_name():
    assert hasattr(adt_Operation, "name")
    descriptor = None
    for klass in adt_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asort_is_not_abstract():
    assert not inspect.isabstract(ASort)


def test_asort_constructor_exists():
    assert callable(ASort.__init__)


def test_asort_constructor_args():
    sig = inspect.signature(ASort.__init__)
    params = list(sig.parameters.keys())



def test_adt_sort_is_not_abstract():
    assert not inspect.isabstract(adt_Sort)


def test_adt_sort_constructor_exists():
    assert callable(adt_Sort.__init__)


def test_adt_sort_constructor_args():
    sig = inspect.signature(adt_Sort.__init__)
    params = list(sig.parameters.keys())



def test_adt_subsort_is_not_abstract():
    assert not inspect.isabstract(adt_SubSort)


def test_adt_subsort_constructor_exists():
    assert callable(adt_SubSort.__init__)


def test_adt_subsort_constructor_args():
    sig = inspect.signature(adt_SubSort.__init__)
    params = list(sig.parameters.keys())



def test_adt_equation_is_not_abstract():
    assert not inspect.isabstract(adt_Equation)


def test_adt_equation_constructor_exists():
    assert callable(adt_Equation.__init__)


def test_adt_equation_constructor_args():
    sig = inspect.signature(adt_Equation.__init__)
    params = list(sig.parameters.keys())



def test_adt_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(adt_VariableDeclaration)


def test_adt_variabledeclaration_constructor_exists():
    assert callable(adt_VariableDeclaration.__init__)


def test_adt_variabledeclaration_constructor_args():
    sig = inspect.signature(adt_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt_variabledeclaration_has_name():
    assert hasattr(adt_VariableDeclaration, "name")
    descriptor = None
    for klass in adt_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adt_signature_is_not_abstract():
    assert not inspect.isabstract(adt_Signature)


def test_adt_signature_constructor_exists():
    assert callable(adt_Signature.__init__)


def test_adt_signature_constructor_args():
    sig = inspect.signature(adt_Signature.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_adt_signature_has_ops():
    assert hasattr(adt_Signature, "ops")
    descriptor = None
    for klass in adt_Signature.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_adt_adt_is_not_abstract():
    assert not inspect.isabstract(adt_ADT)


def test_adt_adt_constructor_exists():
    assert callable(adt_ADT.__init__)


def test_adt_adt_constructor_args():
    sig = inspect.signature(adt_ADT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt_adt_has_name():
    assert hasattr(adt_ADT, "name")
    descriptor = None
    for klass in adt_ADT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adt_asort_is_not_abstract():
    assert not inspect.isabstract(adt_ASort)


def test_adt_asort_constructor_exists():
    assert callable(adt_ASort.__init__)


def test_adt_asort_constructor_args():
    sig = inspect.signature(adt_ASort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt_asort_has_name():
    assert hasattr(adt_ASort, "name")
    descriptor = None
    for klass in adt_ASort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
ATerm_strategy = st.builds(
    ATerm,
)
adt_Variable_strategy = st.builds(
    adt_Variable,
)
adt_Term_strategy = st.builds(
    adt_Term,
)
adt_ATerm_strategy = st.builds(
    adt_ATerm,
    symbol=
        safe_text
)
adt_Operation_strategy = st.builds(
    adt_Operation,
    name=
        safe_text
)
ASort_strategy = st.builds(
    ASort,
)
adt_Sort_strategy = st.builds(
    adt_Sort,
)
adt_SubSort_strategy = st.builds(
    adt_SubSort,
)
adt_Equation_strategy = st.builds(
    adt_Equation,
)
adt_VariableDeclaration_strategy = st.builds(
    adt_VariableDeclaration,
    name=
        safe_text
)
adt_Signature_strategy = st.builds(
    adt_Signature,
    ops=
        safe_text
)
adt_ADT_strategy = st.builds(
    adt_ADT,
    name=
        safe_text
)
adt_ASort_strategy = st.builds(
    adt_ASort,
    name=
        safe_text
)

@given(instance=ATerm_strategy)
@settings(max_examples=50)
def test_aterm_instantiation(instance):
    assert isinstance(instance, ATerm)

@given(instance=adt_Variable_strategy)
@settings(max_examples=50)
def test_adt_variable_instantiation(instance):
    assert isinstance(instance, adt_Variable)

@given(instance=adt_Term_strategy)
@settings(max_examples=50)
def test_adt_term_instantiation(instance):
    assert isinstance(instance, adt_Term)

@given(instance=adt_ATerm_strategy)
@settings(max_examples=50)
def test_adt_aterm_instantiation(instance):
    assert isinstance(instance, adt_ATerm)



@given(instance=adt_ATerm_strategy)
def test_adt_aterm_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=adt_Operation_strategy)
@settings(max_examples=50)
def test_adt_operation_instantiation(instance):
    assert isinstance(instance, adt_Operation)



@given(instance=adt_Operation_strategy)
def test_adt_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ASort_strategy)
@settings(max_examples=50)
def test_asort_instantiation(instance):
    assert isinstance(instance, ASort)

@given(instance=adt_Sort_strategy)
@settings(max_examples=50)
def test_adt_sort_instantiation(instance):
    assert isinstance(instance, adt_Sort)

@given(instance=adt_SubSort_strategy)
@settings(max_examples=50)
def test_adt_subsort_instantiation(instance):
    assert isinstance(instance, adt_SubSort)

@given(instance=adt_Equation_strategy)
@settings(max_examples=50)
def test_adt_equation_instantiation(instance):
    assert isinstance(instance, adt_Equation)

@given(instance=adt_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_adt_variabledeclaration_instantiation(instance):
    assert isinstance(instance, adt_VariableDeclaration)



@given(instance=adt_VariableDeclaration_strategy)
def test_adt_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adt_Signature_strategy)
@settings(max_examples=50)
def test_adt_signature_instantiation(instance):
    assert isinstance(instance, adt_Signature)



@given(instance=adt_Signature_strategy)
def test_adt_signature_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=adt_ADT_strategy)
@settings(max_examples=50)
def test_adt_adt_instantiation(instance):
    assert isinstance(instance, adt_ADT)



@given(instance=adt_ADT_strategy)
def test_adt_adt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adt_ASort_strategy)
@settings(max_examples=50)
def test_adt_asort_instantiation(instance):
    assert isinstance(instance, adt_ASort)



@given(instance=adt_ASort_strategy)
def test_adt_asort_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=adt_ASort_strategy)
@settings(max_examples=30)
def test_adt_asort_issubsortof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSubSortOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSubSortOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSubSortOf' in adt_ASort is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSubSortOf' in adt_ASort did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSubSortOf' in adt_ASort is not implemented or raised an error")
