import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::EStringToStringMapEntry,
    graph::DocumentRoot,
    graph::EnvironmentGraph,
    graph::Cause,
    graph::Node,
    graph::Dependency,
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



def test_graph::environmentgraph_is_not_abstract():
    assert not inspect.isabstract(graph::EnvironmentGraph)


def test_graph::environmentgraph_constructor_exists():
    assert callable(graph::EnvironmentGraph.__init__)


def test_graph::environmentgraph_constructor_args():
    sig = inspect.signature(graph::EnvironmentGraph.__init__)
    params = list(sig.parameters.keys())



def test_graph::cause_is_not_abstract():
    assert not inspect.isabstract(graph::Cause)


def test_graph::cause_constructor_exists():
    assert callable(graph::Cause.__init__)


def test_graph::cause_constructor_args():
    sig = inspect.signature(graph::Cause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "type" in params, "Missing parameter 'type'"

def test_graph::cause_has_name():
    assert hasattr(graph::Cause, "name")
    descriptor = None
    for klass in graph::Cause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graph::cause_has_version():
    assert hasattr(graph::Cause, "version")
    descriptor = None
    for klass in graph::Cause.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_graph::cause_has_type():
    assert hasattr(graph::Cause, "type")
    descriptor = None
    for klass in graph::Cause.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
    assert "containerName" in params, "Missing parameter 'containerName'"
    assert "nodeName" in params, "Missing parameter 'nodeName'"
    assert "unitName" in params, "Missing parameter 'unitName'"
    assert "unitVersion" in params, "Missing parameter 'unitVersion'"

def test_graph::node_has_id():
    assert hasattr(graph::Node, "id")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_containerName():
    assert hasattr(graph::Node, "containerName")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "containerName" in klass.__dict__:
            descriptor = klass.__dict__["containerName"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_nodeName():
    assert hasattr(graph::Node, "nodeName")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "nodeName" in klass.__dict__:
            descriptor = klass.__dict__["nodeName"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_unitName():
    assert hasattr(graph::Node, "unitName")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "unitName" in klass.__dict__:
            descriptor = klass.__dict__["unitName"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_unitVersion():
    assert hasattr(graph::Node, "unitVersion")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "unitVersion" in klass.__dict__:
            descriptor = klass.__dict__["unitVersion"]
            break
    assert isinstance(descriptor, property)



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
graph::EnvironmentGraph_strategy = st.builds(
    graph::EnvironmentGraph,
)
graph::Cause_strategy = st.builds(
    graph::Cause,
    name=
        safe_text,
    version=
        safe_text,
    type=
        safe_text
)
graph::Node_strategy = st.builds(
    graph::Node,
    id=
        safe_text,
    containerName=
        safe_text,
    nodeName=
        safe_text,
    unitName=
        safe_text,
    unitVersion=
        safe_text
)
graph::Dependency_strategy = st.builds(
    graph::Dependency,
    id=
        safe_text,
    locality=
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

@given(instance=graph::EnvironmentGraph_strategy)
@settings(max_examples=50)
def test_graph::environmentgraph_instantiation(instance):
    assert isinstance(instance, graph::EnvironmentGraph)

@given(instance=graph::Cause_strategy)
@settings(max_examples=50)
def test_graph::cause_instantiation(instance):
    assert isinstance(instance, graph::Cause)

@given(instance=graph::Cause_strategy)
def test_graph::cause_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Cause_strategy)
def test_graph::cause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Cause_strategy)
def test_graph::cause_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=graph::Cause_strategy)
def test_graph::cause_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=graph::Cause_strategy)
def test_graph::cause_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::Cause_strategy)
def test_graph::cause_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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

@given(instance=graph::Node_strategy)
def test_graph::node_containerName_type(instance):
    assert isinstance(instance.containerName, str)


@given(instance=graph::Node_strategy)
def test_graph::node_containerName_setter(instance):
    original = instance.containerName
    instance.containerName = original
    assert instance.containerName == original

@given(instance=graph::Node_strategy)
def test_graph::node_nodeName_type(instance):
    assert isinstance(instance.nodeName, str)


@given(instance=graph::Node_strategy)
def test_graph::node_nodeName_setter(instance):
    original = instance.nodeName
    instance.nodeName = original
    assert instance.nodeName == original

@given(instance=graph::Node_strategy)
def test_graph::node_unitName_type(instance):
    assert isinstance(instance.unitName, str)


@given(instance=graph::Node_strategy)
def test_graph::node_unitName_setter(instance):
    original = instance.unitName
    instance.unitName = original
    assert instance.unitName == original

@given(instance=graph::Node_strategy)
def test_graph::node_unitVersion_type(instance):
    assert isinstance(instance.unitVersion, str)


@given(instance=graph::Node_strategy)
def test_graph::node_unitVersion_setter(instance):
    original = instance.unitVersion
    instance.unitVersion = original
    assert instance.unitVersion == original

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
