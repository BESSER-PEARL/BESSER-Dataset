import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    eCoreContainemntTree_EObject,
    eCoreContainemntTree_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecorecontainemnttree_eobject_is_not_abstract():
    assert not inspect.isabstract(eCoreContainemntTree_EObject)


def test_ecorecontainemnttree_eobject_constructor_exists():
    assert callable(eCoreContainemntTree_EObject.__init__)


def test_ecorecontainemnttree_eobject_constructor_args():
    sig = inspect.signature(eCoreContainemntTree_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorecontainemnttree_node_is_not_abstract():
    assert not inspect.isabstract(eCoreContainemntTree_Node)


def test_ecorecontainemnttree_node_constructor_exists():
    assert callable(eCoreContainemntTree_Node.__init__)


def test_ecorecontainemnttree_node_constructor_args():
    sig = inspect.signature(eCoreContainemntTree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecorecontainemnttree_node_has_name():
    assert hasattr(eCoreContainemntTree_Node, "name")
    descriptor = None
    for klass in eCoreContainemntTree_Node.__mro__:
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
eCoreContainemntTree_EObject_strategy = st.builds(
    eCoreContainemntTree_EObject,
)
eCoreContainemntTree_Node_strategy = st.builds(
    eCoreContainemntTree_Node,
    name=
        safe_text
)

@given(instance=eCoreContainemntTree_EObject_strategy)
@settings(max_examples=50)
def test_ecorecontainemnttree_eobject_instantiation(instance):
    assert isinstance(instance, eCoreContainemntTree_EObject)

@given(instance=eCoreContainemntTree_Node_strategy)
@settings(max_examples=50)
def test_ecorecontainemnttree_node_instantiation(instance):
    assert isinstance(instance, eCoreContainemntTree_Node)



@given(instance=eCoreContainemntTree_Node_strategy)
def test_ecorecontainemnttree_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
