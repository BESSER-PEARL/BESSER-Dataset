import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    attacktree_Model,
    attacktree_EObject,
    attacktree_Vulnerability,
    attacktree_Node,
    propagationType,
    vulnerabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attacktree_model_is_not_abstract():
    assert not inspect.isabstract(attacktree_Model)


def test_attacktree_model_constructor_exists():
    assert callable(attacktree_Model.__init__)


def test_attacktree_model_constructor_args():
    sig = inspect.signature(attacktree_Model.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_attacktree_model_has_description():
    assert hasattr(attacktree_Model, "description")
    descriptor = None
    for klass in attacktree_Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_model_has_name():
    assert hasattr(attacktree_Model, "name")
    descriptor = None
    for klass in attacktree_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attacktree_eobject_is_not_abstract():
    assert not inspect.isabstract(attacktree_EObject)


def test_attacktree_eobject_constructor_exists():
    assert callable(attacktree_EObject.__init__)


def test_attacktree_eobject_constructor_args():
    sig = inspect.signature(attacktree_EObject.__init__)
    params = list(sig.parameters.keys())



def test_attacktree_vulnerability_is_not_abstract():
    assert not inspect.isabstract(attacktree_Vulnerability)


def test_attacktree_vulnerability_constructor_exists():
    assert callable(attacktree_Vulnerability.__init__)


def test_attacktree_vulnerability_constructor_args():
    sig = inspect.signature(attacktree_Vulnerability.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"

def test_attacktree_vulnerability_has_severity():
    assert hasattr(attacktree_Vulnerability, "severity")
    descriptor = None
    for klass in attacktree_Vulnerability.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_vulnerability_has_tags():
    assert hasattr(attacktree_Vulnerability, "tags")
    descriptor = None
    for klass in attacktree_Vulnerability.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_vulnerability_has_name():
    assert hasattr(attacktree_Vulnerability, "name")
    descriptor = None
    for klass in attacktree_Vulnerability.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_vulnerability_has_type():
    assert hasattr(attacktree_Vulnerability, "type")
    descriptor = None
    for klass in attacktree_Vulnerability.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_vulnerability_has_description():
    assert hasattr(attacktree_Vulnerability, "description")
    descriptor = None
    for klass in attacktree_Vulnerability.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_attacktree_node_is_not_abstract():
    assert not inspect.isabstract(attacktree_Node)


def test_attacktree_node_constructor_exists():
    assert callable(attacktree_Node.__init__)


def test_attacktree_node_constructor_args():
    sig = inspect.signature(attacktree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "domains" in params, "Missing parameter 'domains'"

def test_attacktree_node_has_description():
    assert hasattr(attacktree_Node, "description")
    descriptor = None
    for klass in attacktree_Node.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_node_has_name():
    assert hasattr(attacktree_Node, "name")
    descriptor = None
    for klass in attacktree_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_node_has_tags():
    assert hasattr(attacktree_Node, "tags")
    descriptor = None
    for klass in attacktree_Node.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attacktree_node_has_domains():
    assert hasattr(attacktree_Node, "domains")
    descriptor = None
    for klass in attacktree_Node.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)

def test_propagationtype_exists():
    # Check that the Enumeration exists
    assert propagationType is not None

def test_propagationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in propagationType]
    expected_literals = [
        "processor",
        "data",
        "memory",
        "dataFlow",
        "local",
        "bus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in propagationType"

def test_vulnerabilitytype_exists():
    # Check that the Enumeration exists
    assert vulnerabilityType is not None

def test_vulnerabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in vulnerabilityType]
    expected_literals = [
        "Exposure",
        "Authentication",
        "Concurrency",
        "Isolation",
        "ResourceAllocation",
        "Timing",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in vulnerabilityType"


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
attacktree_Model_strategy = st.builds(
    attacktree_Model,
    description=
        safe_text,
    name=
        safe_text
)
attacktree_EObject_strategy = st.builds(
    attacktree_EObject,
)
attacktree_Vulnerability_strategy = st.builds(
    attacktree_Vulnerability,
    severity=
        st.integers(),
    tags=
        safe_text,
    name=
        safe_text,
    type=
        safe_text,
    description=
        safe_text
)
attacktree_Node_strategy = st.builds(
    attacktree_Node,
    description=
        safe_text,
    name=
        safe_text,
    tags=
        safe_text,
    domains=
        safe_text
)

@given(instance=attacktree_Model_strategy)
@settings(max_examples=50)
def test_attacktree_model_instantiation(instance):
    assert isinstance(instance, attacktree_Model)



@given(instance=attacktree_Model_strategy)
def test_attacktree_model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=attacktree_Model_strategy)
def test_attacktree_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attacktree_EObject_strategy)
@settings(max_examples=50)
def test_attacktree_eobject_instantiation(instance):
    assert isinstance(instance, attacktree_EObject)

@given(instance=attacktree_Vulnerability_strategy)
@settings(max_examples=50)
def test_attacktree_vulnerability_instantiation(instance):
    assert isinstance(instance, attacktree_Vulnerability)



@given(instance=attacktree_Vulnerability_strategy)
def test_attacktree_vulnerability_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=attacktree_Vulnerability_strategy)
def test_attacktree_vulnerability_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original



@given(instance=attacktree_Vulnerability_strategy)
def test_attacktree_vulnerability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=attacktree_Vulnerability_strategy)
def test_attacktree_vulnerability_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=attacktree_Vulnerability_strategy)
def test_attacktree_vulnerability_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=attacktree_Node_strategy)
@settings(max_examples=50)
def test_attacktree_node_instantiation(instance):
    assert isinstance(instance, attacktree_Node)



@given(instance=attacktree_Node_strategy)
def test_attacktree_node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=attacktree_Node_strategy)
def test_attacktree_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=attacktree_Node_strategy)
def test_attacktree_node_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original



@given(instance=attacktree_Node_strategy)
def test_attacktree_node_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original
