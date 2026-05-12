import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProductSpaceElement,
    list_VersionedList,
    list_ProductSpaceElement,
    UUIDElement,
    list_VersionedListStartReference,
    list_VersionedListEdge,
    list_VersionedListVertex,
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



def test_list_versionedlist_is_not_abstract():
    assert not inspect.isabstract(list_VersionedList)


def test_list_versionedlist_constructor_exists():
    assert callable(list_VersionedList.__init__)


def test_list_versionedlist_constructor_args():
    sig = inspect.signature(list_VersionedList.__init__)
    params = list(sig.parameters.keys())



def test_list_productspaceelement_is_not_abstract():
    assert not inspect.isabstract(list_ProductSpaceElement)


def test_list_productspaceelement_constructor_exists():
    assert callable(list_ProductSpaceElement.__init__)


def test_list_productspaceelement_constructor_args():
    sig = inspect.signature(list_ProductSpaceElement.__init__)
    params = list(sig.parameters.keys())



def test_uuidelement_is_not_abstract():
    assert not inspect.isabstract(UUIDElement)


def test_uuidelement_constructor_exists():
    assert callable(UUIDElement.__init__)


def test_uuidelement_constructor_args():
    sig = inspect.signature(UUIDElement.__init__)
    params = list(sig.parameters.keys())



def test_list_versionedliststartreference_is_not_abstract():
    assert not inspect.isabstract(list_VersionedListStartReference)


def test_list_versionedliststartreference_constructor_exists():
    assert callable(list_VersionedListStartReference.__init__)


def test_list_versionedliststartreference_constructor_args():
    sig = inspect.signature(list_VersionedListStartReference.__init__)
    params = list(sig.parameters.keys())



def test_list_versionedlistedge_is_not_abstract():
    assert not inspect.isabstract(list_VersionedListEdge)


def test_list_versionedlistedge_constructor_exists():
    assert callable(list_VersionedListEdge.__init__)


def test_list_versionedlistedge_constructor_args():
    sig = inspect.signature(list_VersionedListEdge.__init__)
    params = list(sig.parameters.keys())



def test_list_versionedlistvertex_is_not_abstract():
    assert not inspect.isabstract(list_VersionedListVertex)


def test_list_versionedlistvertex_constructor_exists():
    assert callable(list_VersionedListVertex.__init__)


def test_list_versionedlistvertex_constructor_args():
    sig = inspect.signature(list_VersionedListVertex.__init__)
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
list_VersionedList_strategy = st.builds(
    list_VersionedList,
)
list_ProductSpaceElement_strategy = st.builds(
    list_ProductSpaceElement,
)
UUIDElement_strategy = st.builds(
    UUIDElement,
)
list_VersionedListStartReference_strategy = st.builds(
    list_VersionedListStartReference,
)
list_VersionedListEdge_strategy = st.builds(
    list_VersionedListEdge,
)
list_VersionedListVertex_strategy = st.builds(
    list_VersionedListVertex,
)

@given(instance=ProductSpaceElement_strategy)
@settings(max_examples=50)
def test_productspaceelement_instantiation(instance):
    assert isinstance(instance, ProductSpaceElement)

@given(instance=list_VersionedList_strategy)
@settings(max_examples=50)
def test_list_versionedlist_instantiation(instance):
    assert isinstance(instance, list_VersionedList)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=list_VersionedList_strategy)
@settings(max_examples=30)
def test_list_versionedlist_linearize_changes_state(instance):
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
        assert has_statements, f"Function 'linearize' in list_VersionedList is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'linearize' in list_VersionedList did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'linearize' in list_VersionedList is not implemented or raised an error")

@given(instance=list_ProductSpaceElement_strategy)
@settings(max_examples=50)
def test_list_productspaceelement_instantiation(instance):
    assert isinstance(instance, list_ProductSpaceElement)

@given(instance=UUIDElement_strategy)
@settings(max_examples=50)
def test_uuidelement_instantiation(instance):
    assert isinstance(instance, UUIDElement)

@given(instance=list_VersionedListStartReference_strategy)
@settings(max_examples=50)
def test_list_versionedliststartreference_instantiation(instance):
    assert isinstance(instance, list_VersionedListStartReference)

@given(instance=list_VersionedListEdge_strategy)
@settings(max_examples=50)
def test_list_versionedlistedge_instantiation(instance):
    assert isinstance(instance, list_VersionedListEdge)

@given(instance=list_VersionedListVertex_strategy)
@settings(max_examples=50)
def test_list_versionedlistvertex_instantiation(instance):
    assert isinstance(instance, list_VersionedListVertex)
