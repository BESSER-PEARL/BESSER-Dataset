import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TreeMapItem,
    TreeMapViewer_TreeMapContainer,
    TreeMapViewer_TreeMapItem,
    TreeMapViewer_TreeMapViewer,
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



def test_treemapviewer_treemapcontainer_is_not_abstract():
    assert not inspect.isabstract(TreeMapViewer_TreeMapContainer)


def test_treemapviewer_treemapcontainer_constructor_exists():
    assert callable(TreeMapViewer_TreeMapContainer.__init__)


def test_treemapviewer_treemapcontainer_constructor_args():
    sig = inspect.signature(TreeMapViewer_TreeMapContainer.__init__)
    params = list(sig.parameters.keys())



def test_treemapviewer_treemapitem_is_not_abstract():
    assert not inspect.isabstract(TreeMapViewer_TreeMapItem)


def test_treemapviewer_treemapitem_constructor_exists():
    assert callable(TreeMapViewer_TreeMapItem.__init__)


def test_treemapviewer_treemapitem_constructor_args():
    sig = inspect.signature(TreeMapViewer_TreeMapItem.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "label" in params, "Missing parameter 'label'"

def test_treemapviewer_treemapitem_has_value():
    assert hasattr(TreeMapViewer_TreeMapItem, "value")
    descriptor = None
    for klass in TreeMapViewer_TreeMapItem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_treemapviewer_treemapitem_has_label():
    assert hasattr(TreeMapViewer_TreeMapItem, "label")
    descriptor = None
    for klass in TreeMapViewer_TreeMapItem.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_treemapviewer_treemapviewer_is_not_abstract():
    assert not inspect.isabstract(TreeMapViewer_TreeMapViewer)


def test_treemapviewer_treemapviewer_constructor_exists():
    assert callable(TreeMapViewer_TreeMapViewer.__init__)


def test_treemapviewer_treemapviewer_constructor_args():
    sig = inspect.signature(TreeMapViewer_TreeMapViewer.__init__)
    params = list(sig.parameters.keys())
    assert "childLayoutStrategy" in params, "Missing parameter 'childLayoutStrategy'"

def test_treemapviewer_treemapviewer_has_childLayoutStrategy():
    assert hasattr(TreeMapViewer_TreeMapViewer, "childLayoutStrategy")
    descriptor = None
    for klass in TreeMapViewer_TreeMapViewer.__mro__:
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
        "Linear",
        "Quantum",
        "Ordred",
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
TreeMapViewer_TreeMapContainer_strategy = st.builds(
    TreeMapViewer_TreeMapContainer,
)
TreeMapViewer_TreeMapItem_strategy = st.builds(
    TreeMapViewer_TreeMapItem,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    label=
        safe_text
)
TreeMapViewer_TreeMapViewer_strategy = st.builds(
    TreeMapViewer_TreeMapViewer,
    childLayoutStrategy=
        safe_text
)

@given(instance=TreeMapItem_strategy)
@settings(max_examples=50)
def test_treemapitem_instantiation(instance):
    assert isinstance(instance, TreeMapItem)

@given(instance=TreeMapViewer_TreeMapContainer_strategy)
@settings(max_examples=50)
def test_treemapviewer_treemapcontainer_instantiation(instance):
    assert isinstance(instance, TreeMapViewer_TreeMapContainer)

@given(instance=TreeMapViewer_TreeMapItem_strategy)
@settings(max_examples=50)
def test_treemapviewer_treemapitem_instantiation(instance):
    assert isinstance(instance, TreeMapViewer_TreeMapItem)



@given(instance=TreeMapViewer_TreeMapItem_strategy)
def test_treemapviewer_treemapitem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=TreeMapViewer_TreeMapItem_strategy)
def test_treemapviewer_treemapitem_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=TreeMapViewer_TreeMapViewer_strategy)
@settings(max_examples=50)
def test_treemapviewer_treemapviewer_instantiation(instance):
    assert isinstance(instance, TreeMapViewer_TreeMapViewer)



@given(instance=TreeMapViewer_TreeMapViewer_strategy)
def test_treemapviewer_treemapviewer_childLayoutStrategy_setter(instance):
    original = instance.childLayoutStrategy
    instance.childLayoutStrategy = original
    assert instance.childLayoutStrategy == original
