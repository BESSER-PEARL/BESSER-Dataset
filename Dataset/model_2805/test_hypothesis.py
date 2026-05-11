import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    attackimpact::Model,
    attackimpact::EObject,
    attackimpact::Propagation,
    attackimpact::Vulnerability,
    attackimpact::Node,
    vulnerabilityType,
    propagationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attackimpact::model_is_not_abstract():
    assert not inspect.isabstract(attackimpact::Model)


def test_attackimpact::model_constructor_exists():
    assert callable(attackimpact::Model.__init__)


def test_attackimpact::model_constructor_args():
    sig = inspect.signature(attackimpact::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_attackimpact::model_has_name():
    assert hasattr(attackimpact::Model, "name")
    descriptor = None
    for klass in attackimpact::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::model_has_description():
    assert hasattr(attackimpact::Model, "description")
    descriptor = None
    for klass in attackimpact::Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_attackimpact::eobject_is_not_abstract():
    assert not inspect.isabstract(attackimpact::EObject)


def test_attackimpact::eobject_constructor_exists():
    assert callable(attackimpact::EObject.__init__)


def test_attackimpact::eobject_constructor_args():
    sig = inspect.signature(attackimpact::EObject.__init__)
    params = list(sig.parameters.keys())



def test_attackimpact::propagation_is_not_abstract():
    assert not inspect.isabstract(attackimpact::Propagation)


def test_attackimpact::propagation_constructor_exists():
    assert callable(attackimpact::Propagation.__init__)


def test_attackimpact::propagation_constructor_args():
    sig = inspect.signature(attackimpact::Propagation.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "type" in params, "Missing parameter 'type'"

def test_attackimpact::propagation_has_severity():
    assert hasattr(attackimpact::Propagation, "severity")
    descriptor = None
    for klass in attackimpact::Propagation.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::propagation_has_tags():
    assert hasattr(attackimpact::Propagation, "tags")
    descriptor = None
    for klass in attackimpact::Propagation.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::propagation_has_type():
    assert hasattr(attackimpact::Propagation, "type")
    descriptor = None
    for klass in attackimpact::Propagation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_attackimpact::vulnerability_is_not_abstract():
    assert not inspect.isabstract(attackimpact::Vulnerability)


def test_attackimpact::vulnerability_constructor_exists():
    assert callable(attackimpact::Vulnerability.__init__)


def test_attackimpact::vulnerability_constructor_args():
    sig = inspect.signature(attackimpact::Vulnerability.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "description" in params, "Missing parameter 'description'"

def test_attackimpact::vulnerability_has_name():
    assert hasattr(attackimpact::Vulnerability, "name")
    descriptor = None
    for klass in attackimpact::Vulnerability.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::vulnerability_has_severity():
    assert hasattr(attackimpact::Vulnerability, "severity")
    descriptor = None
    for klass in attackimpact::Vulnerability.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::vulnerability_has_type():
    assert hasattr(attackimpact::Vulnerability, "type")
    descriptor = None
    for klass in attackimpact::Vulnerability.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::vulnerability_has_tags():
    assert hasattr(attackimpact::Vulnerability, "tags")
    descriptor = None
    for klass in attackimpact::Vulnerability.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::vulnerability_has_description():
    assert hasattr(attackimpact::Vulnerability, "description")
    descriptor = None
    for klass in attackimpact::Vulnerability.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_attackimpact::node_is_not_abstract():
    assert not inspect.isabstract(attackimpact::Node)


def test_attackimpact::node_constructor_exists():
    assert callable(attackimpact::Node.__init__)


def test_attackimpact::node_constructor_args():
    sig = inspect.signature(attackimpact::Node.__init__)
    params = list(sig.parameters.keys())
    assert "domains" in params, "Missing parameter 'domains'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "description" in params, "Missing parameter 'description'"

def test_attackimpact::node_has_domains():
    assert hasattr(attackimpact::Node, "domains")
    descriptor = None
    for klass in attackimpact::Node.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::node_has_name():
    assert hasattr(attackimpact::Node, "name")
    descriptor = None
    for klass in attackimpact::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::node_has_tags():
    assert hasattr(attackimpact::Node, "tags")
    descriptor = None
    for klass in attackimpact::Node.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_attackimpact::node_has_description():
    assert hasattr(attackimpact::Node, "description")
    descriptor = None
    for klass in attackimpact::Node.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_vulnerabilitytype_exists():
    # Check that the Enumeration exists
    assert vulnerabilityType is not None

def test_vulnerabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in vulnerabilityType]
    expected_literals = [
        "Concurrency",
        "Isolation",
        "Timing",
        "ResourceAllocation",
        "Authentication",
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
        "memory",
        "dataFlow",
        "processor",
        "bus",
        "data",
        "local",
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
attackimpact::Model_strategy = st.builds(
    attackimpact::Model,
    name=
        safe_text,
    description=
        safe_text
)
attackimpact::EObject_strategy = st.builds(
    attackimpact::EObject,
)
attackimpact::Propagation_strategy = st.builds(
    attackimpact::Propagation,
    severity=
        st.integers(),
    tags=
        safe_text,
    type=
        safe_text
)
attackimpact::Vulnerability_strategy = st.builds(
    attackimpact::Vulnerability,
    name=
        safe_text,
    severity=
        st.integers(),
    type=
        safe_text,
    tags=
        safe_text,
    description=
        safe_text
)
attackimpact::Node_strategy = st.builds(
    attackimpact::Node,
    domains=
        safe_text,
    name=
        safe_text,
    tags=
        safe_text,
    description=
        safe_text
)

@given(instance=attackimpact::Model_strategy)
@settings(max_examples=50)
def test_attackimpact::model_instantiation(instance):
    assert isinstance(instance, attackimpact::Model)

@given(instance=attackimpact::Model_strategy)
def test_attackimpact::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attackimpact::Model_strategy)
def test_attackimpact::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attackimpact::Model_strategy)
def test_attackimpact::model_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=attackimpact::Model_strategy)
def test_attackimpact::model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=attackimpact::EObject_strategy)
@settings(max_examples=50)
def test_attackimpact::eobject_instantiation(instance):
    assert isinstance(instance, attackimpact::EObject)

@given(instance=attackimpact::Propagation_strategy)
@settings(max_examples=50)
def test_attackimpact::propagation_instantiation(instance):
    assert isinstance(instance, attackimpact::Propagation)

@given(instance=attackimpact::Propagation_strategy)
def test_attackimpact::propagation_severity_type(instance):
    assert isinstance(instance.severity, int)


@given(instance=attackimpact::Propagation_strategy)
def test_attackimpact::propagation_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=attackimpact::Propagation_strategy)
def test_attackimpact::propagation_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=attackimpact::Propagation_strategy)
def test_attackimpact::propagation_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=attackimpact::Propagation_strategy)
def test_attackimpact::propagation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=attackimpact::Propagation_strategy)
def test_attackimpact::propagation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=attackimpact::Vulnerability_strategy)
@settings(max_examples=50)
def test_attackimpact::vulnerability_instantiation(instance):
    assert isinstance(instance, attackimpact::Vulnerability)

@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_severity_type(instance):
    assert isinstance(instance.severity, int)


@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=attackimpact::Vulnerability_strategy)
def test_attackimpact::vulnerability_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=attackimpact::Node_strategy)
@settings(max_examples=50)
def test_attackimpact::node_instantiation(instance):
    assert isinstance(instance, attackimpact::Node)

@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_domains_type(instance):
    assert isinstance(instance.domains, str)


@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original

@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=attackimpact::Node_strategy)
def test_attackimpact::node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
