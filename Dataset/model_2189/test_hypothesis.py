import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeMapItem,
    TreeMapViewer::TreeMapContainer,
    TreeMapViewer::TreeMapItem,
    TreeMapViewer::TreeMapViewer,
    TreeMapType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treemapitem_is_not_abstract():
    assert not inspect.isabstract(TreeMapItem)


def test_treemapitem_constructor_exists():
    assert callable(TreeMapItem.__init__)


def test_treemapitem_constructor_args():
    sig = inspect.signature(TreeMapItem.__init__)
    params = list(sig.parameters.keys())



def test_treemapviewer::treemapcontainer_is_not_abstract():
    assert not inspect.isabstract(TreeMapViewer::TreeMapContainer)


def test_treemapviewer::treemapcontainer_constructor_exists():
    assert callable(TreeMapViewer::TreeMapContainer.__init__)


def test_treemapviewer::treemapcontainer_constructor_args():
    sig = inspect.signature(TreeMapViewer::TreeMapContainer.__init__)
    params = list(sig.parameters.keys())



def test_treemapviewer::treemapitem_is_not_abstract():
    assert not inspect.isabstract(TreeMapViewer::TreeMapItem)


def test_treemapviewer::treemapitem_constructor_exists():
    assert callable(TreeMapViewer::TreeMapItem.__init__)


def test_treemapviewer::treemapitem_constructor_args():
    sig = inspect.signature(TreeMapViewer::TreeMapItem.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "value" in params, "Missing parameter 'value'"

def test_treemapviewer::treemapitem_has_label():
    assert hasattr(TreeMapViewer::TreeMapItem, "label")
    descriptor = None
    for klass in TreeMapViewer::TreeMapItem.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_treemapviewer::treemapitem_has_value():
    assert hasattr(TreeMapViewer::TreeMapItem, "value")
    descriptor = None
    for klass in TreeMapViewer::TreeMapItem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_treemapviewer::treemapviewer_is_not_abstract():
    assert not inspect.isabstract(TreeMapViewer::TreeMapViewer)


def test_treemapviewer::treemapviewer_constructor_exists():
    assert callable(TreeMapViewer::TreeMapViewer.__init__)


def test_treemapviewer::treemapviewer_constructor_args():
    sig = inspect.signature(TreeMapViewer::TreeMapViewer.__init__)
    params = list(sig.parameters.keys())
    assert "childLayoutStrategy" in params, "Missing parameter 'childLayoutStrategy'"

def test_treemapviewer::treemapviewer_has_childLayoutStrategy():
    assert hasattr(TreeMapViewer::TreeMapViewer, "childLayoutStrategy")
    descriptor = None
    for klass in TreeMapViewer::TreeMapViewer.__mro__:
        if "childLayoutStrategy" in klass.__dict__:
            descriptor = klass.__dict__["childLayoutStrategy"]
            break
    assert isinstance(descriptor, property)

def test_treemaptype_exists():
    # Check that the Enumeration exists
    assert TreeMapType is not None

def test_treemaptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeMapType]
    expected_literals = [
        "Ordred",
        "Quantum",
        "Linear",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeMapType"


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
TreeMapItem_strategy = st.builds(
    TreeMapItem,
)
TreeMapViewer::TreeMapContainer_strategy = st.builds(
    TreeMapViewer::TreeMapContainer,
)
TreeMapViewer::TreeMapItem_strategy = st.builds(
    TreeMapViewer::TreeMapItem,
    label=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
TreeMapViewer::TreeMapViewer_strategy = st.builds(
    TreeMapViewer::TreeMapViewer,
    childLayoutStrategy=
        safe_text
)

@given(instance=TreeMapItem_strategy)
@settings(max_examples=50)
def test_treemapitem_instantiation(instance):
    assert isinstance(instance, TreeMapItem)

@given(instance=TreeMapViewer::TreeMapContainer_strategy)
@settings(max_examples=50)
def test_treemapviewer::treemapcontainer_instantiation(instance):
    assert isinstance(instance, TreeMapViewer::TreeMapContainer)

@given(instance=TreeMapViewer::TreeMapItem_strategy)
@settings(max_examples=50)
def test_treemapviewer::treemapitem_instantiation(instance):
    assert isinstance(instance, TreeMapViewer::TreeMapItem)

@given(instance=TreeMapViewer::TreeMapItem_strategy)
def test_treemapviewer::treemapitem_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=TreeMapViewer::TreeMapItem_strategy)
def test_treemapviewer::treemapitem_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=TreeMapViewer::TreeMapItem_strategy)
def test_treemapviewer::treemapitem_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=TreeMapViewer::TreeMapItem_strategy)
def test_treemapviewer::treemapitem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TreeMapViewer::TreeMapViewer_strategy)
@settings(max_examples=50)
def test_treemapviewer::treemapviewer_instantiation(instance):
    assert isinstance(instance, TreeMapViewer::TreeMapViewer)

@given(instance=TreeMapViewer::TreeMapViewer_strategy)
def test_treemapviewer::treemapviewer_childLayoutStrategy_type(instance):
    assert isinstance(instance.childLayoutStrategy, str)


@given(instance=TreeMapViewer::TreeMapViewer_strategy)
def test_treemapviewer::treemapviewer_childLayoutStrategy_setter(instance):
    original = instance.childLayoutStrategy
    instance.childLayoutStrategy = original
    assert instance.childLayoutStrategy == original
