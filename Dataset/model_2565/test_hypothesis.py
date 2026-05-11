import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eCoreContainemntTree::EObject,
    eCoreContainemntTree::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecorecontainemnttree::eobject_is_not_abstract():
    assert not inspect.isabstract(eCoreContainemntTree::EObject)


def test_ecorecontainemnttree::eobject_constructor_exists():
    assert callable(eCoreContainemntTree::EObject.__init__)


def test_ecorecontainemnttree::eobject_constructor_args():
    sig = inspect.signature(eCoreContainemntTree::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorecontainemnttree::node_is_not_abstract():
    assert not inspect.isabstract(eCoreContainemntTree::Node)


def test_ecorecontainemnttree::node_constructor_exists():
    assert callable(eCoreContainemntTree::Node.__init__)


def test_ecorecontainemnttree::node_constructor_args():
    sig = inspect.signature(eCoreContainemntTree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecorecontainemnttree::node_has_name():
    assert hasattr(eCoreContainemntTree::Node, "name")
    descriptor = None
    for klass in eCoreContainemntTree::Node.__mro__:
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
eCoreContainemntTree::EObject_strategy = st.builds(
    eCoreContainemntTree::EObject,
)
eCoreContainemntTree::Node_strategy = st.builds(
    eCoreContainemntTree::Node,
    name=
        safe_text
)

@given(instance=eCoreContainemntTree::EObject_strategy)
@settings(max_examples=50)
def test_ecorecontainemnttree::eobject_instantiation(instance):
    assert isinstance(instance, eCoreContainemntTree::EObject)

@given(instance=eCoreContainemntTree::Node_strategy)
@settings(max_examples=50)
def test_ecorecontainemnttree::node_instantiation(instance):
    assert isinstance(instance, eCoreContainemntTree::Node)

@given(instance=eCoreContainemntTree::Node_strategy)
def test_ecorecontainemnttree::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eCoreContainemntTree::Node_strategy)
def test_ecorecontainemnttree::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
