import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    attackimpact_Model,
    attackimpact_EObject,
    attackimpact_Propagation,
    attackimpact_Vulnerability,
    attackimpact_Node,
    vulnerabilityType,
    propagationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attackimpact_model_is_not_abstract():
    assert not inspect.isabstract(attackimpact_Model)


def test_attackimpact_model_constructor_exists():
    assert callable(attackimpact_Model.__init__)


def test_attackimpact_model_constructor_args():
    sig = inspect.signature(attackimpact_Model.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_attackimpact_model_has_description():
    assert hasattr(attackimpact_Model, "description")
    descriptor = None
    for klass in attackimpact_Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_model_has_name():
    assert hasattr(attackimpact_Model, "name")
    descriptor = None
    for klass in attackimpact_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attackimpact_eobject_is_not_abstract():
    assert not inspect.isabstract(attackimpact_EObject)


def test_attackimpact_eobject_constructor_exists():
    assert callable(attackimpact_EObject.__init__)


def test_attackimpact_eobject_constructor_args():
    sig = inspect.signature(attackimpact_EObject.__init__)
    params = list(sig.parameters.keys())



def test_attackimpact_propagation_is_not_abstract():
    assert not inspect.isabstract(attackimpact_Propagation)


def test_attackimpact_propagation_constructor_exists():
    assert callable(attackimpact_Propagation.__init__)


def test_attackimpact_propagation_constructor_args():
    sig = inspect.signature(attackimpact_Propagation.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "tags" in params, "Missing parameter 'tags'"

def test_attackimpact_propagation_has_severity():
    assert hasattr(attackimpact_Propagation, "severity")
    descriptor = None
    for klass in attackimpact_Propagation.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_propagation_has_type():
    assert hasattr(attackimpact_Propagation, "type")
    descriptor = None
    for klass in attackimpact_Propagation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_propagation_has_tags():
    assert hasattr(attackimpact_Propagation, "tags")
    descriptor = None
    for klass in attackimpact_Propagation.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)



def test_attackimpact_vulnerability_is_not_abstract():
    assert not inspect.isabstract(attackimpact_Vulnerability)


def test_attackimpact_vulnerability_constructor_exists():
    assert callable(attackimpact_Vulnerability.__init__)


def test_attackimpact_vulnerability_constructor_args():
    sig = inspect.signature(attackimpact_Vulnerability.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_attackimpact_vulnerability_has_description():
    assert hasattr(attackimpact_Vulnerability, "description")
    descriptor = None
    for klass in attackimpact_Vulnerability.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_vulnerability_has_severity():
    assert hasattr(attackimpact_Vulnerability, "severity")
    descriptor = None
    for klass in attackimpact_Vulnerability.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_vulnerability_has_tags():
    assert hasattr(attackimpact_Vulnerability, "tags")
    descriptor = None
    for klass in attackimpact_Vulnerability.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_vulnerability_has_name():
    assert hasattr(attackimpact_Vulnerability, "name")
    descriptor = None
    for klass in attackimpact_Vulnerability.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_vulnerability_has_type():
    assert hasattr(attackimpact_Vulnerability, "type")
    descriptor = None
    for klass in attackimpact_Vulnerability.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_attackimpact_node_is_not_abstract():
    assert not inspect.isabstract(attackimpact_Node)


def test_attackimpact_node_constructor_exists():
    assert callable(attackimpact_Node.__init__)


def test_attackimpact_node_constructor_args():
    sig = inspect.signature(attackimpact_Node.__init__)
    params = list(sig.parameters.keys())
    assert "tags" in params, "Missing parameter 'tags'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "domains" in params, "Missing parameter 'domains'"

def test_attackimpact_node_has_tags():
    assert hasattr(attackimpact_Node, "tags")
    descriptor = None
    for klass in attackimpact_Node.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_node_has_name():
    assert hasattr(attackimpact_Node, "name")
    descriptor = None
    for klass in attackimpact_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_node_has_description():
    assert hasattr(attackimpact_Node, "description")
    descriptor = None
    for klass in attackimpact_Node.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact_node_has_domains():
    assert hasattr(attackimpact_Node, "domains")
    descriptor = None
    for klass in attackimpact_Node.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)

def test_vulnerabilitytype_exists():
    # Check that the Enumeration exists
    assert vulnerabilityType is not None

def test_vulnerabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in vulnerabilityType]
    expected_literals = [
        "ResourceAllocation",
        "Authentication",
        "Concurrency",
        "Isolation",
        "Timing",
        "Exposure",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in vulnerabilityType"

def test_propagationtype_exists():
    # Check that the Enumeration exists
    assert propagationType is not None

def test_propagationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in propagationType]
    expected_literals = [
        "processor",
        "dataFlow",
        "memory",
        "local",
        "bus",
        "data",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in propagationType"


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
attackimpact_Model_strategy = st.builds(
    attackimpact_Model,
    description=
        safe_text,
    name=
        safe_text
)
attackimpact_EObject_strategy = st.builds(
    attackimpact_EObject,
)
attackimpact_Propagation_strategy = st.builds(
    attackimpact_Propagation,
    severity=
        st.integers(),
    type=
        safe_text,
    tags=
        safe_text
)
attackimpact_Vulnerability_strategy = st.builds(
    attackimpact_Vulnerability,
    description=
        safe_text,
    severity=
        st.integers(),
    tags=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
attackimpact_Node_strategy = st.builds(
    attackimpact_Node,
    tags=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    domains=
        safe_text
)

@given(instance=attackimpact_Model_strategy)
@settings(max_examples=50)
def test_attackimpact_model_instantiation(instance):
    assert isinstance(instance, attackimpact_Model)



@given(instance=attackimpact_Model_strategy)
def test_attackimpact_model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=attackimpact_Model_strategy)
def test_attackimpact_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attackimpact_EObject_strategy)
@settings(max_examples=50)
def test_attackimpact_eobject_instantiation(instance):
    assert isinstance(instance, attackimpact_EObject)

@given(instance=attackimpact_Propagation_strategy)
@settings(max_examples=50)
def test_attackimpact_propagation_instantiation(instance):
    assert isinstance(instance, attackimpact_Propagation)



@given(instance=attackimpact_Propagation_strategy)
def test_attackimpact_propagation_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=attackimpact_Propagation_strategy)
def test_attackimpact_propagation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=attackimpact_Propagation_strategy)
def test_attackimpact_propagation_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=attackimpact_Vulnerability_strategy)
@settings(max_examples=50)
def test_attackimpact_vulnerability_instantiation(instance):
    assert isinstance(instance, attackimpact_Vulnerability)



@given(instance=attackimpact_Vulnerability_strategy)
def test_attackimpact_vulnerability_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=attackimpact_Vulnerability_strategy)
def test_attackimpact_vulnerability_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=attackimpact_Vulnerability_strategy)
def test_attackimpact_vulnerability_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original



@given(instance=attackimpact_Vulnerability_strategy)
def test_attackimpact_vulnerability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=attackimpact_Vulnerability_strategy)
def test_attackimpact_vulnerability_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=attackimpact_Node_strategy)
@settings(max_examples=50)
def test_attackimpact_node_instantiation(instance):
    assert isinstance(instance, attackimpact_Node)



@given(instance=attackimpact_Node_strategy)
def test_attackimpact_node_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original



@given(instance=attackimpact_Node_strategy)
def test_attackimpact_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=attackimpact_Node_strategy)
def test_attackimpact_node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=attackimpact_Node_strategy)
def test_attackimpact_node_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original
