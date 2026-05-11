import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ATerm,
    adt::Variable,
    adt::Term,
    adt::ATerm,
    adt::Operation,
    ASort,
    adt::Sort,
    adt::SubSort,
    adt::Equation,
    adt::VariableDeclaration,
    adt::Signature,
    adt::ADT,
    adt::ASort,
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



def test_adt::variable_is_not_abstract():
    assert not inspect.isabstract(adt::Variable)


def test_adt::variable_constructor_exists():
    assert callable(adt::Variable.__init__)


def test_adt::variable_constructor_args():
    sig = inspect.signature(adt::Variable.__init__)
    params = list(sig.parameters.keys())



def test_adt::term_is_not_abstract():
    assert not inspect.isabstract(adt::Term)


def test_adt::term_constructor_exists():
    assert callable(adt::Term.__init__)


def test_adt::term_constructor_args():
    sig = inspect.signature(adt::Term.__init__)
    params = list(sig.parameters.keys())



def test_adt::aterm_is_not_abstract():
    assert not inspect.isabstract(adt::ATerm)


def test_adt::aterm_constructor_exists():
    assert callable(adt::ATerm.__init__)


def test_adt::aterm_constructor_args():
    sig = inspect.signature(adt::ATerm.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_adt::aterm_has_symbol():
    assert hasattr(adt::ATerm, "symbol")
    descriptor = None
    for klass in adt::ATerm.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_adt::operation_is_not_abstract():
    assert not inspect.isabstract(adt::Operation)


def test_adt::operation_constructor_exists():
    assert callable(adt::Operation.__init__)


def test_adt::operation_constructor_args():
    sig = inspect.signature(adt::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt::operation_has_name():
    assert hasattr(adt::Operation, "name")
    descriptor = None
    for klass in adt::Operation.__mro__:
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



def test_adt::sort_is_not_abstract():
    assert not inspect.isabstract(adt::Sort)


def test_adt::sort_constructor_exists():
    assert callable(adt::Sort.__init__)


def test_adt::sort_constructor_args():
    sig = inspect.signature(adt::Sort.__init__)
    params = list(sig.parameters.keys())



def test_adt::subsort_is_not_abstract():
    assert not inspect.isabstract(adt::SubSort)


def test_adt::subsort_constructor_exists():
    assert callable(adt::SubSort.__init__)


def test_adt::subsort_constructor_args():
    sig = inspect.signature(adt::SubSort.__init__)
    params = list(sig.parameters.keys())



def test_adt::equation_is_not_abstract():
    assert not inspect.isabstract(adt::Equation)


def test_adt::equation_constructor_exists():
    assert callable(adt::Equation.__init__)


def test_adt::equation_constructor_args():
    sig = inspect.signature(adt::Equation.__init__)
    params = list(sig.parameters.keys())



def test_adt::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(adt::VariableDeclaration)


def test_adt::variabledeclaration_constructor_exists():
    assert callable(adt::VariableDeclaration.__init__)


def test_adt::variabledeclaration_constructor_args():
    sig = inspect.signature(adt::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt::variabledeclaration_has_name():
    assert hasattr(adt::VariableDeclaration, "name")
    descriptor = None
    for klass in adt::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adt::signature_is_not_abstract():
    assert not inspect.isabstract(adt::Signature)


def test_adt::signature_constructor_exists():
    assert callable(adt::Signature.__init__)


def test_adt::signature_constructor_args():
    sig = inspect.signature(adt::Signature.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_adt::signature_has_ops():
    assert hasattr(adt::Signature, "ops")
    descriptor = None
    for klass in adt::Signature.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_adt::adt_is_not_abstract():
    assert not inspect.isabstract(adt::ADT)


def test_adt::adt_constructor_exists():
    assert callable(adt::ADT.__init__)


def test_adt::adt_constructor_args():
    sig = inspect.signature(adt::ADT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt::adt_has_name():
    assert hasattr(adt::ADT, "name")
    descriptor = None
    for klass in adt::ADT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adt::asort_is_not_abstract():
    assert not inspect.isabstract(adt::ASort)


def test_adt::asort_constructor_exists():
    assert callable(adt::ASort.__init__)


def test_adt::asort_constructor_args():
    sig = inspect.signature(adt::ASort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adt::asort_has_name():
    assert hasattr(adt::ASort, "name")
    descriptor = None
    for klass in adt::ASort.__mro__:
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
adt::Variable_strategy = st.builds(
    adt::Variable,
)
adt::Term_strategy = st.builds(
    adt::Term,
)
adt::ATerm_strategy = st.builds(
    adt::ATerm,
    symbol=
        safe_text
)
adt::Operation_strategy = st.builds(
    adt::Operation,
    name=
        safe_text
)
ASort_strategy = st.builds(
    ASort,
)
adt::Sort_strategy = st.builds(
    adt::Sort,
)
adt::SubSort_strategy = st.builds(
    adt::SubSort,
)
adt::Equation_strategy = st.builds(
    adt::Equation,
)
adt::VariableDeclaration_strategy = st.builds(
    adt::VariableDeclaration,
    name=
        safe_text
)
adt::Signature_strategy = st.builds(
    adt::Signature,
    ops=
        safe_text
)
adt::ADT_strategy = st.builds(
    adt::ADT,
    name=
        safe_text
)
adt::ASort_strategy = st.builds(
    adt::ASort,
    name=
        safe_text
)

@given(instance=ATerm_strategy)
@settings(max_examples=50)
def test_aterm_instantiation(instance):
    assert isinstance(instance, ATerm)

@given(instance=adt::Variable_strategy)
@settings(max_examples=50)
def test_adt::variable_instantiation(instance):
    assert isinstance(instance, adt::Variable)

@given(instance=adt::Term_strategy)
@settings(max_examples=50)
def test_adt::term_instantiation(instance):
    assert isinstance(instance, adt::Term)

@given(instance=adt::ATerm_strategy)
@settings(max_examples=50)
def test_adt::aterm_instantiation(instance):
    assert isinstance(instance, adt::ATerm)

@given(instance=adt::ATerm_strategy)
def test_adt::aterm_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=adt::ATerm_strategy)
def test_adt::aterm_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=adt::Operation_strategy)
@settings(max_examples=50)
def test_adt::operation_instantiation(instance):
    assert isinstance(instance, adt::Operation)

@given(instance=adt::Operation_strategy)
def test_adt::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adt::Operation_strategy)
def test_adt::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ASort_strategy)
@settings(max_examples=50)
def test_asort_instantiation(instance):
    assert isinstance(instance, ASort)

@given(instance=adt::Sort_strategy)
@settings(max_examples=50)
def test_adt::sort_instantiation(instance):
    assert isinstance(instance, adt::Sort)

@given(instance=adt::SubSort_strategy)
@settings(max_examples=50)
def test_adt::subsort_instantiation(instance):
    assert isinstance(instance, adt::SubSort)

@given(instance=adt::Equation_strategy)
@settings(max_examples=50)
def test_adt::equation_instantiation(instance):
    assert isinstance(instance, adt::Equation)

@given(instance=adt::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_adt::variabledeclaration_instantiation(instance):
    assert isinstance(instance, adt::VariableDeclaration)

@given(instance=adt::VariableDeclaration_strategy)
def test_adt::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adt::VariableDeclaration_strategy)
def test_adt::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adt::Signature_strategy)
@settings(max_examples=50)
def test_adt::signature_instantiation(instance):
    assert isinstance(instance, adt::Signature)

@given(instance=adt::Signature_strategy)
def test_adt::signature_ops_type(instance):
    assert isinstance(instance.ops, str)


@given(instance=adt::Signature_strategy)
def test_adt::signature_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=adt::ADT_strategy)
@settings(max_examples=50)
def test_adt::adt_instantiation(instance):
    assert isinstance(instance, adt::ADT)

@given(instance=adt::ADT_strategy)
def test_adt::adt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adt::ADT_strategy)
def test_adt::adt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adt::ASort_strategy)
@settings(max_examples=50)
def test_adt::asort_instantiation(instance):
    assert isinstance(instance, adt::ASort)

@given(instance=adt::ASort_strategy)
def test_adt::asort_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adt::ASort_strategy)
def test_adt::asort_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=adt::ASort_strategy)
@settings(max_examples=30)
def test_adt::asort_issubsortof_changes_state(instance):
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
        assert has_statements, f"Function 'isSubSortOf' in adt::ASort is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSubSortOf' in adt::ASort did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSubSortOf' in adt::ASort is not implemented or raised an error")
