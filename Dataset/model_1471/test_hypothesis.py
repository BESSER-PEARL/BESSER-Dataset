import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::EStringToStringMapEntry,
    graph::DocumentRoot,
    graph::DependencyGraph,
    graph::DeploymentUnitType,
    graph::Dependency,
    graph::Cause,
    graph::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(graph::EStringToStringMapEntry)


def test_graph::estringtostringmapentry_constructor_exists():
    assert callable(graph::EStringToStringMapEntry.__init__)


def test_graph::estringtostringmapentry_constructor_args():
    sig = inspect.signature(graph::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_graph::documentroot_is_not_abstract():
    assert not inspect.isabstract(graph::DocumentRoot)


def test_graph::documentroot_constructor_exists():
    assert callable(graph::DocumentRoot.__init__)


def test_graph::documentroot_constructor_args():
    sig = inspect.signature(graph::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_graph::documentroot_has_mixed():
    assert hasattr(graph::DocumentRoot, "mixed")
    descriptor = None
    for klass in graph::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_graph::dependencygraph_is_not_abstract():
    assert not inspect.isabstract(graph::DependencyGraph)


def test_graph::dependencygraph_constructor_exists():
    assert callable(graph::DependencyGraph.__init__)


def test_graph::dependencygraph_constructor_args():
    sig = inspect.signature(graph::DependencyGraph.__init__)
    params = list(sig.parameters.keys())



def test_graph::deploymentunittype_is_not_abstract():
    assert not inspect.isabstract(graph::DeploymentUnitType)


def test_graph::deploymentunittype_constructor_exists():
    assert callable(graph::DeploymentUnitType.__init__)


def test_graph::deploymentunittype_constructor_args():
    sig = inspect.signature(graph::DeploymentUnitType.__init__)
    params = list(sig.parameters.keys())



def test_graph::dependency_is_not_abstract():
    assert not inspect.isabstract(graph::Dependency)


def test_graph::dependency_constructor_exists():
    assert callable(graph::Dependency.__init__)


def test_graph::dependency_constructor_args():
    sig = inspect.signature(graph::Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "locality" in params, "Missing parameter 'locality'"

def test_graph::dependency_has_id():
    assert hasattr(graph::Dependency, "id")
    descriptor = None
    for klass in graph::Dependency.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_graph::dependency_has_locality():
    assert hasattr(graph::Dependency, "locality")
    descriptor = None
    for klass in graph::Dependency.__mro__:
        if "locality" in klass.__dict__:
            descriptor = klass.__dict__["locality"]
            break
    assert isinstance(descriptor, property)



def test_graph::cause_is_not_abstract():
    assert not inspect.isabstract(graph::Cause)


def test_graph::cause_constructor_exists():
    assert callable(graph::Cause.__init__)


def test_graph::cause_constructor_args():
    sig = inspect.signature(graph::Cause.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_graph::cause_has_type():
    assert hasattr(graph::Cause, "type")
    descriptor = None
    for klass in graph::Cause.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graph::cause_has_name():
    assert hasattr(graph::Cause, "name")
    descriptor = None
    for klass in graph::Cause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graph::node_has_id():
    assert hasattr(graph::Node, "id")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
graph::EStringToStringMapEntry_strategy = st.builds(
    graph::EStringToStringMapEntry,
)
graph::DocumentRoot_strategy = st.builds(
    graph::DocumentRoot,
    mixed=
        safe_text
)
graph::DependencyGraph_strategy = st.builds(
    graph::DependencyGraph,
)
graph::DeploymentUnitType_strategy = st.builds(
    graph::DeploymentUnitType,
)
graph::Dependency_strategy = st.builds(
    graph::Dependency,
    id=
        safe_text,
    locality=
        safe_text
)
graph::Cause_strategy = st.builds(
    graph::Cause,
    type=
        safe_text,
    name=
        safe_text
)
graph::Node_strategy = st.builds(
    graph::Node,
    id=
        safe_text
)

@given(instance=graph::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_graph::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, graph::EStringToStringMapEntry)

@given(instance=graph::DocumentRoot_strategy)
@settings(max_examples=50)
def test_graph::documentroot_instantiation(instance):
    assert isinstance(instance, graph::DocumentRoot)

@given(instance=graph::DocumentRoot_strategy)
def test_graph::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=graph::DocumentRoot_strategy)
def test_graph::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=graph::DependencyGraph_strategy)
@settings(max_examples=50)
def test_graph::dependencygraph_instantiation(instance):
    assert isinstance(instance, graph::DependencyGraph)

@given(instance=graph::DeploymentUnitType_strategy)
@settings(max_examples=50)
def test_graph::deploymentunittype_instantiation(instance):
    assert isinstance(instance, graph::DeploymentUnitType)

@given(instance=graph::Dependency_strategy)
@settings(max_examples=50)
def test_graph::dependency_instantiation(instance):
    assert isinstance(instance, graph::Dependency)

@given(instance=graph::Dependency_strategy)
def test_graph::dependency_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=graph::Dependency_strategy)
def test_graph::dependency_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=graph::Dependency_strategy)
def test_graph::dependency_locality_type(instance):
    assert isinstance(instance.locality, str)


@given(instance=graph::Dependency_strategy)
def test_graph::dependency_locality_setter(instance):
    original = instance.locality
    instance.locality = original
    assert instance.locality == original

@given(instance=graph::Cause_strategy)
@settings(max_examples=50)
def test_graph::cause_instantiation(instance):
    assert isinstance(instance, graph::Cause)

@given(instance=graph::Cause_strategy)
def test_graph::cause_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::Cause_strategy)
def test_graph::cause_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph::Cause_strategy)
def test_graph::cause_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Cause_strategy)
def test_graph::cause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Node_strategy)
def test_graph::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=graph::Node_strategy)
def test_graph::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
