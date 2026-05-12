import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_EStringToStringMapEntry,
    graph_DocumentRoot,
    graph_EnvironmentGraph,
    graph_Cause,
    graph_Node,
    graph_Dependency,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(graph_EStringToStringMapEntry)


def test_graph_estringtostringmapentry_constructor_exists():
    assert callable(graph_EStringToStringMapEntry.__init__)


def test_graph_estringtostringmapentry_constructor_args():
    sig = inspect.signature(graph_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_graph_documentroot_is_not_abstract():
    assert not inspect.isabstract(graph_DocumentRoot)


def test_graph_documentroot_constructor_exists():
    assert callable(graph_DocumentRoot.__init__)


def test_graph_documentroot_constructor_args():
    sig = inspect.signature(graph_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_graph_documentroot_has_mixed():
    assert hasattr(graph_DocumentRoot, "mixed")
    descriptor = None
    for klass in graph_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_graph_environmentgraph_is_not_abstract():
    assert not inspect.isabstract(graph_EnvironmentGraph)


def test_graph_environmentgraph_constructor_exists():
    assert callable(graph_EnvironmentGraph.__init__)


def test_graph_environmentgraph_constructor_args():
    sig = inspect.signature(graph_EnvironmentGraph.__init__)
    params = list(sig.parameters.keys())



def test_graph_cause_is_not_abstract():
    assert not inspect.isabstract(graph_Cause)


def test_graph_cause_constructor_exists():
    assert callable(graph_Cause.__init__)


def test_graph_cause_constructor_args():
    sig = inspect.signature(graph_Cause.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_graph_cause_has_version():
    assert hasattr(graph_Cause, "version")
    descriptor = None
    for klass in graph_Cause.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_graph_cause_has_name():
    assert hasattr(graph_Cause, "name")
    descriptor = None
    for klass in graph_Cause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graph_cause_has_type():
    assert hasattr(graph_Cause, "type")
    descriptor = None
    for klass in graph_Cause.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "unitName" in params, "Missing parameter 'unitName'"
    assert "nodeName" in params, "Missing parameter 'nodeName'"
    assert "containerName" in params, "Missing parameter 'containerName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "unitVersion" in params, "Missing parameter 'unitVersion'"

def test_graph_node_has_unitName():
    assert hasattr(graph_Node, "unitName")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "unitName" in klass.__dict__:
            descriptor = klass.__dict__["unitName"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_nodeName():
    assert hasattr(graph_Node, "nodeName")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "nodeName" in klass.__dict__:
            descriptor = klass.__dict__["nodeName"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_containerName():
    assert hasattr(graph_Node, "containerName")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "containerName" in klass.__dict__:
            descriptor = klass.__dict__["containerName"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_id():
    assert hasattr(graph_Node, "id")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_unitVersion():
    assert hasattr(graph_Node, "unitVersion")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "unitVersion" in klass.__dict__:
            descriptor = klass.__dict__["unitVersion"]
            break
    assert isinstance(descriptor, property)



def test_graph_dependency_is_not_abstract():
    assert not inspect.isabstract(graph_Dependency)


def test_graph_dependency_constructor_exists():
    assert callable(graph_Dependency.__init__)


def test_graph_dependency_constructor_args():
    sig = inspect.signature(graph_Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "locality" in params, "Missing parameter 'locality'"
    assert "id" in params, "Missing parameter 'id'"

def test_graph_dependency_has_locality():
    assert hasattr(graph_Dependency, "locality")
    descriptor = None
    for klass in graph_Dependency.__mro__:
        if "locality" in klass.__dict__:
            descriptor = klass.__dict__["locality"]
            break
    assert isinstance(descriptor, property)

def test_graph_dependency_has_id():
    assert hasattr(graph_Dependency, "id")
    descriptor = None
    for klass in graph_Dependency.__mro__:
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
graph_EStringToStringMapEntry_strategy = st.builds(
    graph_EStringToStringMapEntry,
)
graph_DocumentRoot_strategy = st.builds(
    graph_DocumentRoot,
    mixed=
        safe_text
)
graph_EnvironmentGraph_strategy = st.builds(
    graph_EnvironmentGraph,
)
graph_Cause_strategy = st.builds(
    graph_Cause,
    version=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
graph_Node_strategy = st.builds(
    graph_Node,
    unitName=
        safe_text,
    nodeName=
        safe_text,
    containerName=
        safe_text,
    id=
        safe_text,
    unitVersion=
        safe_text
)
graph_Dependency_strategy = st.builds(
    graph_Dependency,
    locality=
        safe_text,
    id=
        safe_text
)

@given(instance=graph_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_graph_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, graph_EStringToStringMapEntry)

@given(instance=graph_DocumentRoot_strategy)
@settings(max_examples=50)
def test_graph_documentroot_instantiation(instance):
    assert isinstance(instance, graph_DocumentRoot)



@given(instance=graph_DocumentRoot_strategy)
def test_graph_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=graph_EnvironmentGraph_strategy)
@settings(max_examples=50)
def test_graph_environmentgraph_instantiation(instance):
    assert isinstance(instance, graph_EnvironmentGraph)

@given(instance=graph_Cause_strategy)
@settings(max_examples=50)
def test_graph_cause_instantiation(instance):
    assert isinstance(instance, graph_Cause)



@given(instance=graph_Cause_strategy)
def test_graph_cause_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=graph_Cause_strategy)
def test_graph_cause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graph_Cause_strategy)
def test_graph_cause_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)



@given(instance=graph_Node_strategy)
def test_graph_node_unitName_setter(instance):
    original = instance.unitName
    instance.unitName = original
    assert instance.unitName == original



@given(instance=graph_Node_strategy)
def test_graph_node_nodeName_setter(instance):
    original = instance.nodeName
    instance.nodeName = original
    assert instance.nodeName == original



@given(instance=graph_Node_strategy)
def test_graph_node_containerName_setter(instance):
    original = instance.containerName
    instance.containerName = original
    assert instance.containerName == original



@given(instance=graph_Node_strategy)
def test_graph_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=graph_Node_strategy)
def test_graph_node_unitVersion_setter(instance):
    original = instance.unitVersion
    instance.unitVersion = original
    assert instance.unitVersion == original

@given(instance=graph_Dependency_strategy)
@settings(max_examples=50)
def test_graph_dependency_instantiation(instance):
    assert isinstance(instance, graph_Dependency)



@given(instance=graph_Dependency_strategy)
def test_graph_dependency_locality_setter(instance):
    original = instance.locality
    instance.locality = original
    assert instance.locality == original



@given(instance=graph_Dependency_strategy)
def test_graph_dependency_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
