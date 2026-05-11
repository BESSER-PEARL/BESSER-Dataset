import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    attacktree::Model,
    attacktree::EObject,
    attacktree::Vulnerability,
    attacktree::Node,
    propagationType,
    vulnerabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attacktree::model_is_not_abstract():
    assert not inspect.isabstract(attacktree::Model)


def test_attacktree::model_constructor_exists():
    assert callable(attacktree::Model.__init__)


def test_attacktree::model_constructor_args():
    sig = inspect.signature(attacktree::Model.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_attacktree::model_has_description():
    assert hasattr(attacktree::Model, "description")
    descriptor = None
    for klass in attacktree::Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::model_has_name():
    assert hasattr(attacktree::Model, "name")
    descriptor = None
    for klass in attacktree::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attacktree::eobject_is_not_abstract():
    assert not inspect.isabstract(attacktree::EObject)


def test_attacktree::eobject_constructor_exists():
    assert callable(attacktree::EObject.__init__)


def test_attacktree::eobject_constructor_args():
    sig = inspect.signature(attacktree::EObject.__init__)
    params = list(sig.parameters.keys())



def test_attacktree::vulnerability_is_not_abstract():
    assert not inspect.isabstract(attacktree::Vulnerability)


def test_attacktree::vulnerability_constructor_exists():
    assert callable(attacktree::Vulnerability.__init__)


def test_attacktree::vulnerability_constructor_args():
    sig = inspect.signature(attacktree::Vulnerability.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "severity" in params, "Missing parameter 'severity'"

def test_attacktree::vulnerability_has_name():
    assert hasattr(attacktree::Vulnerability, "name")
    descriptor = None
    for klass in attacktree::Vulnerability.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::vulnerability_has_tags():
    assert hasattr(attacktree::Vulnerability, "tags")
    descriptor = None
    for klass in attacktree::Vulnerability.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::vulnerability_has_description():
    assert hasattr(attacktree::Vulnerability, "description")
    descriptor = None
    for klass in attacktree::Vulnerability.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::vulnerability_has_type():
    assert hasattr(attacktree::Vulnerability, "type")
    descriptor = None
    for klass in attacktree::Vulnerability.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::vulnerability_has_severity():
    assert hasattr(attacktree::Vulnerability, "severity")
    descriptor = None
    for klass in attacktree::Vulnerability.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_attacktree::node_is_not_abstract():
    assert not inspect.isabstract(attacktree::Node)


def test_attacktree::node_constructor_exists():
    assert callable(attacktree::Node.__init__)


def test_attacktree::node_constructor_args():
    sig = inspect.signature(attacktree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "domains" in params, "Missing parameter 'domains'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "description" in params, "Missing parameter 'description'"

def test_attacktree::node_has_domains():
    assert hasattr(attacktree::Node, "domains")
    descriptor = None
    for klass in attacktree::Node.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::node_has_name():
    assert hasattr(attacktree::Node, "name")
    descriptor = None
    for klass in attacktree::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::node_has_tags():
    assert hasattr(attacktree::Node, "tags")
    descriptor = None
    for klass in attacktree::Node.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attacktree::node_has_description():
    assert hasattr(attacktree::Node, "description")
    descriptor = None
    for klass in attacktree::Node.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_propagationtype_exists():
    # Check that the Enumeration exists
    assert propagationType is not None

def test_propagationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in propagationType]
    expected_literals = [
        "local",
        "dataFlow",
        "processor",
        "data",
        "memory",
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
        "Isolation",
        "Authentication",
        "Concurrency",
        "ResourceAllocation",
        "Timing",
        "Exposure",
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
attacktree::Model_strategy = st.builds(
    attacktree::Model,
    description=
        safe_text,
    name=
        safe_text
)
attacktree::EObject_strategy = st.builds(
    attacktree::EObject,
)
attacktree::Vulnerability_strategy = st.builds(
    attacktree::Vulnerability,
    name=
        safe_text,
    tags=
        safe_text,
    description=
        safe_text,
    type=
        safe_text,
    severity=
        st.integers()
)
attacktree::Node_strategy = st.builds(
    attacktree::Node,
    domains=
        safe_text,
    name=
        safe_text,
    tags=
        safe_text,
    description=
        safe_text
)

@given(instance=attacktree::Model_strategy)
@settings(max_examples=50)
def test_attacktree::model_instantiation(instance):
    assert isinstance(instance, attacktree::Model)

@given(instance=attacktree::Model_strategy)
def test_attacktree::model_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=attacktree::Model_strategy)
def test_attacktree::model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=attacktree::Model_strategy)
def test_attacktree::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attacktree::Model_strategy)
def test_attacktree::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attacktree::EObject_strategy)
@settings(max_examples=50)
def test_attacktree::eobject_instantiation(instance):
    assert isinstance(instance, attacktree::EObject)

@given(instance=attacktree::Vulnerability_strategy)
@settings(max_examples=50)
def test_attacktree::vulnerability_instantiation(instance):
    assert isinstance(instance, attacktree::Vulnerability)

@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_severity_type(instance):
    assert isinstance(instance.severity, int)


@given(instance=attacktree::Vulnerability_strategy)
def test_attacktree::vulnerability_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=attacktree::Node_strategy)
@settings(max_examples=50)
def test_attacktree::node_instantiation(instance):
    assert isinstance(instance, attacktree::Node)

@given(instance=attacktree::Node_strategy)
def test_attacktree::node_domains_type(instance):
    assert isinstance(instance.domains, str)


@given(instance=attacktree::Node_strategy)
def test_attacktree::node_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original

@given(instance=attacktree::Node_strategy)
def test_attacktree::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attacktree::Node_strategy)
def test_attacktree::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attacktree::Node_strategy)
def test_attacktree::node_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=attacktree::Node_strategy)
def test_attacktree::node_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=attacktree::Node_strategy)
def test_attacktree::node_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=attacktree::Node_strategy)
def test_attacktree::node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
