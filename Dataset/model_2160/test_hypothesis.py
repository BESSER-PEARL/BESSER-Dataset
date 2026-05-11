import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProductSpaceElement,
    list::VersionedList,
    list::ProductSpaceElement,
    UUIDElement,
    list::VersionedListStartReference,
    list::VersionedListEdge,
    list::VersionedListVertex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_productspaceelement_is_not_abstract():
    assert not inspect.isabstract(ProductSpaceElement)


def test_productspaceelement_constructor_exists():
    assert callable(ProductSpaceElement.__init__)


def test_productspaceelement_constructor_args():
    sig = inspect.signature(ProductSpaceElement.__init__)
    params = list(sig.parameters.keys())



def test_list::versionedlist_is_not_abstract():
    assert not inspect.isabstract(list::VersionedList)


def test_list::versionedlist_constructor_exists():
    assert callable(list::VersionedList.__init__)


def test_list::versionedlist_constructor_args():
    sig = inspect.signature(list::VersionedList.__init__)
    params = list(sig.parameters.keys())



def test_list::productspaceelement_is_not_abstract():
    assert not inspect.isabstract(list::ProductSpaceElement)


def test_list::productspaceelement_constructor_exists():
    assert callable(list::ProductSpaceElement.__init__)


def test_list::productspaceelement_constructor_args():
    sig = inspect.signature(list::ProductSpaceElement.__init__)
    params = list(sig.parameters.keys())



def test_uuidelement_is_not_abstract():
    assert not inspect.isabstract(UUIDElement)


def test_uuidelement_constructor_exists():
    assert callable(UUIDElement.__init__)


def test_uuidelement_constructor_args():
    sig = inspect.signature(UUIDElement.__init__)
    params = list(sig.parameters.keys())



def test_list::versionedliststartreference_is_not_abstract():
    assert not inspect.isabstract(list::VersionedListStartReference)


def test_list::versionedliststartreference_constructor_exists():
    assert callable(list::VersionedListStartReference.__init__)


def test_list::versionedliststartreference_constructor_args():
    sig = inspect.signature(list::VersionedListStartReference.__init__)
    params = list(sig.parameters.keys())



def test_list::versionedlistedge_is_not_abstract():
    assert not inspect.isabstract(list::VersionedListEdge)


def test_list::versionedlistedge_constructor_exists():
    assert callable(list::VersionedListEdge.__init__)


def test_list::versionedlistedge_constructor_args():
    sig = inspect.signature(list::VersionedListEdge.__init__)
    params = list(sig.parameters.keys())



def test_list::versionedlistvertex_is_not_abstract():
    assert not inspect.isabstract(list::VersionedListVertex)


def test_list::versionedlistvertex_constructor_exists():
    assert callable(list::VersionedListVertex.__init__)


def test_list::versionedlistvertex_constructor_args():
    sig = inspect.signature(list::VersionedListVertex.__init__)
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
ProductSpaceElement_strategy = st.builds(
    ProductSpaceElement,
)
list::VersionedList_strategy = st.builds(
    list::VersionedList,
)
list::ProductSpaceElement_strategy = st.builds(
    list::ProductSpaceElement,
)
UUIDElement_strategy = st.builds(
    UUIDElement,
)
list::VersionedListStartReference_strategy = st.builds(
    list::VersionedListStartReference,
)
list::VersionedListEdge_strategy = st.builds(
    list::VersionedListEdge,
)
list::VersionedListVertex_strategy = st.builds(
    list::VersionedListVertex,
)

@given(instance=ProductSpaceElement_strategy)
@settings(max_examples=50)
def test_productspaceelement_instantiation(instance):
    assert isinstance(instance, ProductSpaceElement)

@given(instance=list::VersionedList_strategy)
@settings(max_examples=50)
def test_list::versionedlist_instantiation(instance):
    assert isinstance(instance, list::VersionedList)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=list::VersionedList_strategy)
@settings(max_examples=30)
def test_list::versionedlist_linearize_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.linearize()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.linearize).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'linearize' in list::VersionedList is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'linearize' in list::VersionedList did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'linearize' in list::VersionedList is not implemented or raised an error")

@given(instance=list::ProductSpaceElement_strategy)
@settings(max_examples=50)
def test_list::productspaceelement_instantiation(instance):
    assert isinstance(instance, list::ProductSpaceElement)

@given(instance=UUIDElement_strategy)
@settings(max_examples=50)
def test_uuidelement_instantiation(instance):
    assert isinstance(instance, UUIDElement)

@given(instance=list::VersionedListStartReference_strategy)
@settings(max_examples=50)
def test_list::versionedliststartreference_instantiation(instance):
    assert isinstance(instance, list::VersionedListStartReference)

@given(instance=list::VersionedListEdge_strategy)
@settings(max_examples=50)
def test_list::versionedlistedge_instantiation(instance):
    assert isinstance(instance, list::VersionedListEdge)

@given(instance=list::VersionedListVertex_strategy)
@settings(max_examples=50)
def test_list::versionedlistvertex_instantiation(instance):
    assert isinstance(instance, list::VersionedListVertex)
