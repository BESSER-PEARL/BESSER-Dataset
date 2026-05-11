import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DocumentElt,
    WT::DocumentElt,
    Port,
    WT::Port,
    Vertex,
    WT::SimpleState,
    WT::InitialState,
    WT::Subsystem,
    WT::WTComponents,
    WT::Edge,
    WT::Vertex,
    WT::StateMachine,
    WT::OutPort,
    WT::InPort,
    WT::Connector,
    WT::Component,
    WT::ControlSubsystem,
    WT::Architecture,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_documentelt_is_not_abstract():
    assert not inspect.isabstract(DocumentElt)


def test_documentelt_constructor_exists():
    assert callable(DocumentElt.__init__)


def test_documentelt_constructor_args():
    sig = inspect.signature(DocumentElt.__init__)
    params = list(sig.parameters.keys())



def test_wt::documentelt_is_not_abstract():
    assert not inspect.isabstract(WT::DocumentElt)


def test_wt::documentelt_constructor_exists():
    assert callable(WT::DocumentElt.__init__)


def test_wt::documentelt_constructor_args():
    sig = inspect.signature(WT::DocumentElt.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_wt::documentelt_has_description():
    assert hasattr(WT::DocumentElt, "description")
    descriptor = None
    for klass in WT::DocumentElt.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_wt::documentelt_has_name():
    assert hasattr(WT::DocumentElt, "name")
    descriptor = None
    for klass in WT::DocumentElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_wt::port_is_not_abstract():
    assert not inspect.isabstract(WT::Port)


def test_wt::port_constructor_exists():
    assert callable(WT::Port.__init__)


def test_wt::port_constructor_args():
    sig = inspect.signature(WT::Port.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"

def test_wt::port_has_label():
    assert hasattr(WT::Port, "label")
    descriptor = None
    for klass in WT::Port.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_wt::port_has_isPublic():
    assert hasattr(WT::Port, "isPublic")
    descriptor = None
    for klass in WT::Port.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_wt::simplestate_is_not_abstract():
    assert not inspect.isabstract(WT::SimpleState)


def test_wt::simplestate_constructor_exists():
    assert callable(WT::SimpleState.__init__)


def test_wt::simplestate_constructor_args():
    sig = inspect.signature(WT::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_wt::initialstate_is_not_abstract():
    assert not inspect.isabstract(WT::InitialState)


def test_wt::initialstate_constructor_exists():
    assert callable(WT::InitialState.__init__)


def test_wt::initialstate_constructor_args():
    sig = inspect.signature(WT::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_wt::subsystem_is_not_abstract():
    assert not inspect.isabstract(WT::Subsystem)


def test_wt::subsystem_constructor_exists():
    assert callable(WT::Subsystem.__init__)


def test_wt::subsystem_constructor_args():
    sig = inspect.signature(WT::Subsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wt::subsystem_has_name():
    assert hasattr(WT::Subsystem, "name")
    descriptor = None
    for klass in WT::Subsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wt::wtcomponents_is_not_abstract():
    assert not inspect.isabstract(WT::WTComponents)


def test_wt::wtcomponents_constructor_exists():
    assert callable(WT::WTComponents.__init__)


def test_wt::wtcomponents_constructor_args():
    sig = inspect.signature(WT::WTComponents.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wt::wtcomponents_has_name():
    assert hasattr(WT::WTComponents, "name")
    descriptor = None
    for klass in WT::WTComponents.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wt::edge_is_not_abstract():
    assert not inspect.isabstract(WT::Edge)


def test_wt::edge_constructor_exists():
    assert callable(WT::Edge.__init__)


def test_wt::edge_constructor_args():
    sig = inspect.signature(WT::Edge.__init__)
    params = list(sig.parameters.keys())



def test_wt::vertex_is_not_abstract():
    assert not inspect.isabstract(WT::Vertex)


def test_wt::vertex_constructor_exists():
    assert callable(WT::Vertex.__init__)


def test_wt::vertex_constructor_args():
    sig = inspect.signature(WT::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_wt::statemachine_is_not_abstract():
    assert not inspect.isabstract(WT::StateMachine)


def test_wt::statemachine_constructor_exists():
    assert callable(WT::StateMachine.__init__)


def test_wt::statemachine_constructor_args():
    sig = inspect.signature(WT::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"

def test_wt::statemachine_has_name():
    assert hasattr(WT::StateMachine, "name")
    descriptor = None
    for klass in WT::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wt::statemachine_has_isPublic():
    assert hasattr(WT::StateMachine, "isPublic")
    descriptor = None
    for klass in WT::StateMachine.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)



def test_wt::outport_is_not_abstract():
    assert not inspect.isabstract(WT::OutPort)


def test_wt::outport_constructor_exists():
    assert callable(WT::OutPort.__init__)


def test_wt::outport_constructor_args():
    sig = inspect.signature(WT::OutPort.__init__)
    params = list(sig.parameters.keys())



def test_wt::inport_is_not_abstract():
    assert not inspect.isabstract(WT::InPort)


def test_wt::inport_constructor_exists():
    assert callable(WT::InPort.__init__)


def test_wt::inport_constructor_args():
    sig = inspect.signature(WT::InPort.__init__)
    params = list(sig.parameters.keys())



def test_wt::connector_is_not_abstract():
    assert not inspect.isabstract(WT::Connector)


def test_wt::connector_constructor_exists():
    assert callable(WT::Connector.__init__)


def test_wt::connector_constructor_args():
    sig = inspect.signature(WT::Connector.__init__)
    params = list(sig.parameters.keys())



def test_wt::component_is_not_abstract():
    assert not inspect.isabstract(WT::Component)


def test_wt::component_constructor_exists():
    assert callable(WT::Component.__init__)


def test_wt::component_constructor_args():
    sig = inspect.signature(WT::Component.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_wt::component_has_label():
    assert hasattr(WT::Component, "label")
    descriptor = None
    for klass in WT::Component.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_wt::controlsubsystem_is_not_abstract():
    assert not inspect.isabstract(WT::ControlSubsystem)


def test_wt::controlsubsystem_constructor_exists():
    assert callable(WT::ControlSubsystem.__init__)


def test_wt::controlsubsystem_constructor_args():
    sig = inspect.signature(WT::ControlSubsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wt::controlsubsystem_has_name():
    assert hasattr(WT::ControlSubsystem, "name")
    descriptor = None
    for klass in WT::ControlSubsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wt::architecture_is_not_abstract():
    assert not inspect.isabstract(WT::Architecture)


def test_wt::architecture_constructor_exists():
    assert callable(WT::Architecture.__init__)


def test_wt::architecture_constructor_args():
    sig = inspect.signature(WT::Architecture.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wt::architecture_has_name():
    assert hasattr(WT::Architecture, "name")
    descriptor = None
    for klass in WT::Architecture.__mro__:
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
DocumentElt_strategy = st.builds(
    DocumentElt,
)
WT::DocumentElt_strategy = st.builds(
    WT::DocumentElt,
    description=
        safe_text,
    name=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
WT::Port_strategy = st.builds(
    WT::Port,
    label=
        safe_text,
    isPublic=
        st.booleans()
)
Vertex_strategy = st.builds(
    Vertex,
)
WT::SimpleState_strategy = st.builds(
    WT::SimpleState,
)
WT::InitialState_strategy = st.builds(
    WT::InitialState,
)
WT::Subsystem_strategy = st.builds(
    WT::Subsystem,
    name=
        safe_text
)
WT::WTComponents_strategy = st.builds(
    WT::WTComponents,
    name=
        safe_text
)
WT::Edge_strategy = st.builds(
    WT::Edge,
)
WT::Vertex_strategy = st.builds(
    WT::Vertex,
)
WT::StateMachine_strategy = st.builds(
    WT::StateMachine,
    name=
        safe_text,
    isPublic=
        st.booleans()
)
WT::OutPort_strategy = st.builds(
    WT::OutPort,
)
WT::InPort_strategy = st.builds(
    WT::InPort,
)
WT::Connector_strategy = st.builds(
    WT::Connector,
)
WT::Component_strategy = st.builds(
    WT::Component,
    label=
        safe_text
)
WT::ControlSubsystem_strategy = st.builds(
    WT::ControlSubsystem,
    name=
        safe_text
)
WT::Architecture_strategy = st.builds(
    WT::Architecture,
    name=
        safe_text
)

@given(instance=DocumentElt_strategy)
@settings(max_examples=50)
def test_documentelt_instantiation(instance):
    assert isinstance(instance, DocumentElt)

@given(instance=WT::DocumentElt_strategy)
@settings(max_examples=50)
def test_wt::documentelt_instantiation(instance):
    assert isinstance(instance, WT::DocumentElt)

@given(instance=WT::DocumentElt_strategy)
def test_wt::documentelt_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=WT::DocumentElt_strategy)
def test_wt::documentelt_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=WT::DocumentElt_strategy)
def test_wt::documentelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=WT::DocumentElt_strategy)
def test_wt::documentelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=WT::Port_strategy)
@settings(max_examples=50)
def test_wt::port_instantiation(instance):
    assert isinstance(instance, WT::Port)

@given(instance=WT::Port_strategy)
def test_wt::port_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=WT::Port_strategy)
def test_wt::port_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=WT::Port_strategy)
def test_wt::port_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=WT::Port_strategy)
def test_wt::port_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=WT::SimpleState_strategy)
@settings(max_examples=50)
def test_wt::simplestate_instantiation(instance):
    assert isinstance(instance, WT::SimpleState)

@given(instance=WT::InitialState_strategy)
@settings(max_examples=50)
def test_wt::initialstate_instantiation(instance):
    assert isinstance(instance, WT::InitialState)

@given(instance=WT::Subsystem_strategy)
@settings(max_examples=50)
def test_wt::subsystem_instantiation(instance):
    assert isinstance(instance, WT::Subsystem)

@given(instance=WT::Subsystem_strategy)
def test_wt::subsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=WT::Subsystem_strategy)
def test_wt::subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WT::WTComponents_strategy)
@settings(max_examples=50)
def test_wt::wtcomponents_instantiation(instance):
    assert isinstance(instance, WT::WTComponents)

@given(instance=WT::WTComponents_strategy)
def test_wt::wtcomponents_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=WT::WTComponents_strategy)
def test_wt::wtcomponents_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WT::Edge_strategy)
@settings(max_examples=50)
def test_wt::edge_instantiation(instance):
    assert isinstance(instance, WT::Edge)

@given(instance=WT::Vertex_strategy)
@settings(max_examples=50)
def test_wt::vertex_instantiation(instance):
    assert isinstance(instance, WT::Vertex)

@given(instance=WT::StateMachine_strategy)
@settings(max_examples=50)
def test_wt::statemachine_instantiation(instance):
    assert isinstance(instance, WT::StateMachine)

@given(instance=WT::StateMachine_strategy)
def test_wt::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=WT::StateMachine_strategy)
def test_wt::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WT::StateMachine_strategy)
def test_wt::statemachine_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=WT::StateMachine_strategy)
def test_wt::statemachine_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=WT::OutPort_strategy)
@settings(max_examples=50)
def test_wt::outport_instantiation(instance):
    assert isinstance(instance, WT::OutPort)

@given(instance=WT::InPort_strategy)
@settings(max_examples=50)
def test_wt::inport_instantiation(instance):
    assert isinstance(instance, WT::InPort)

@given(instance=WT::Connector_strategy)
@settings(max_examples=50)
def test_wt::connector_instantiation(instance):
    assert isinstance(instance, WT::Connector)

@given(instance=WT::Component_strategy)
@settings(max_examples=50)
def test_wt::component_instantiation(instance):
    assert isinstance(instance, WT::Component)

@given(instance=WT::Component_strategy)
def test_wt::component_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=WT::Component_strategy)
def test_wt::component_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=WT::ControlSubsystem_strategy)
@settings(max_examples=50)
def test_wt::controlsubsystem_instantiation(instance):
    assert isinstance(instance, WT::ControlSubsystem)

@given(instance=WT::ControlSubsystem_strategy)
def test_wt::controlsubsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=WT::ControlSubsystem_strategy)
def test_wt::controlsubsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WT::Architecture_strategy)
@settings(max_examples=50)
def test_wt::architecture_instantiation(instance):
    assert isinstance(instance, WT::Architecture)

@given(instance=WT::Architecture_strategy)
def test_wt::architecture_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=WT::Architecture_strategy)
def test_wt::architecture_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
