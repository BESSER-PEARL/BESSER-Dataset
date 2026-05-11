import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Port,
    dslComponent::OutPort,
    dslComponent::InPort,
    dslComponent::Port,
    dslComponent::DocumElt,
    Vertex,
    dslComponent::InitialState,
    dslComponent::SimpleState,
    DocumElt,
    dslComponent::Edge,
    dslComponent::Vertex,
    dslComponent::StateMachine,
    dslComponent::Component,
    dslComponent::ControlSubsystem,
    dslComponent::Subsystem,
    dslComponent::WTComponents,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::outport_is_not_abstract():
    assert not inspect.isabstract(dslComponent::OutPort)


def test_dslcomponent::outport_constructor_exists():
    assert callable(dslComponent::OutPort.__init__)


def test_dslcomponent::outport_constructor_args():
    sig = inspect.signature(dslComponent::OutPort.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::inport_is_not_abstract():
    assert not inspect.isabstract(dslComponent::InPort)


def test_dslcomponent::inport_constructor_exists():
    assert callable(dslComponent::InPort.__init__)


def test_dslcomponent::inport_constructor_args():
    sig = inspect.signature(dslComponent::InPort.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::port_is_not_abstract():
    assert not inspect.isabstract(dslComponent::Port)


def test_dslcomponent::port_constructor_exists():
    assert callable(dslComponent::Port.__init__)


def test_dslcomponent::port_constructor_args():
    sig = inspect.signature(dslComponent::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent::port_has_name():
    assert hasattr(dslComponent::Port, "name")
    descriptor = None
    for klass in dslComponent::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent::documelt_is_not_abstract():
    assert not inspect.isabstract(dslComponent::DocumElt)


def test_dslcomponent::documelt_constructor_exists():
    assert callable(dslComponent::DocumElt.__init__)


def test_dslcomponent::documelt_constructor_args():
    sig = inspect.signature(dslComponent::DocumElt.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent::documelt_has_desc():
    assert hasattr(dslComponent::DocumElt, "desc")
    descriptor = None
    for klass in dslComponent::DocumElt.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent::documelt_has_name():
    assert hasattr(dslComponent::DocumElt, "name")
    descriptor = None
    for klass in dslComponent::DocumElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::initialstate_is_not_abstract():
    assert not inspect.isabstract(dslComponent::InitialState)


def test_dslcomponent::initialstate_constructor_exists():
    assert callable(dslComponent::InitialState.__init__)


def test_dslcomponent::initialstate_constructor_args():
    sig = inspect.signature(dslComponent::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::simplestate_is_not_abstract():
    assert not inspect.isabstract(dslComponent::SimpleState)


def test_dslcomponent::simplestate_constructor_exists():
    assert callable(dslComponent::SimpleState.__init__)


def test_dslcomponent::simplestate_constructor_args():
    sig = inspect.signature(dslComponent::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_documelt_is_not_abstract():
    assert not inspect.isabstract(DocumElt)


def test_documelt_constructor_exists():
    assert callable(DocumElt.__init__)


def test_documelt_constructor_args():
    sig = inspect.signature(DocumElt.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::edge_is_not_abstract():
    assert not inspect.isabstract(dslComponent::Edge)


def test_dslcomponent::edge_constructor_exists():
    assert callable(dslComponent::Edge.__init__)


def test_dslcomponent::edge_constructor_args():
    sig = inspect.signature(dslComponent::Edge.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::vertex_is_not_abstract():
    assert not inspect.isabstract(dslComponent::Vertex)


def test_dslcomponent::vertex_constructor_exists():
    assert callable(dslComponent::Vertex.__init__)


def test_dslcomponent::vertex_constructor_args():
    sig = inspect.signature(dslComponent::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent::statemachine_is_not_abstract():
    assert not inspect.isabstract(dslComponent::StateMachine)


def test_dslcomponent::statemachine_constructor_exists():
    assert callable(dslComponent::StateMachine.__init__)


def test_dslcomponent::statemachine_constructor_args():
    sig = inspect.signature(dslComponent::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent::statemachine_has_name():
    assert hasattr(dslComponent::StateMachine, "name")
    descriptor = None
    for klass in dslComponent::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent::component_is_not_abstract():
    assert not inspect.isabstract(dslComponent::Component)


def test_dslcomponent::component_constructor_exists():
    assert callable(dslComponent::Component.__init__)


def test_dslcomponent::component_constructor_args():
    sig = inspect.signature(dslComponent::Component.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent::component_has_id():
    assert hasattr(dslComponent::Component, "id")
    descriptor = None
    for klass in dslComponent::Component.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent::component_has_name():
    assert hasattr(dslComponent::Component, "name")
    descriptor = None
    for klass in dslComponent::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent::controlsubsystem_is_not_abstract():
    assert not inspect.isabstract(dslComponent::ControlSubsystem)


def test_dslcomponent::controlsubsystem_constructor_exists():
    assert callable(dslComponent::ControlSubsystem.__init__)


def test_dslcomponent::controlsubsystem_constructor_args():
    sig = inspect.signature(dslComponent::ControlSubsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent::controlsubsystem_has_name():
    assert hasattr(dslComponent::ControlSubsystem, "name")
    descriptor = None
    for klass in dslComponent::ControlSubsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent::subsystem_is_not_abstract():
    assert not inspect.isabstract(dslComponent::Subsystem)


def test_dslcomponent::subsystem_constructor_exists():
    assert callable(dslComponent::Subsystem.__init__)


def test_dslcomponent::subsystem_constructor_args():
    sig = inspect.signature(dslComponent::Subsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_dslcomponent::subsystem_has_name():
    assert hasattr(dslComponent::Subsystem, "name")
    descriptor = None
    for klass in dslComponent::Subsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent::subsystem_has_description():
    assert hasattr(dslComponent::Subsystem, "description")
    descriptor = None
    for klass in dslComponent::Subsystem.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent::wtcomponents_is_not_abstract():
    assert not inspect.isabstract(dslComponent::WTComponents)


def test_dslcomponent::wtcomponents_constructor_exists():
    assert callable(dslComponent::WTComponents.__init__)


def test_dslcomponent::wtcomponents_constructor_args():
    sig = inspect.signature(dslComponent::WTComponents.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "author" in params, "Missing parameter 'author'"

def test_dslcomponent::wtcomponents_has_id():
    assert hasattr(dslComponent::WTComponents, "id")
    descriptor = None
    for klass in dslComponent::WTComponents.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent::wtcomponents_has_author():
    assert hasattr(dslComponent::WTComponents, "author")
    descriptor = None
    for klass in dslComponent::WTComponents.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
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
Port_strategy = st.builds(
    Port,
)
dslComponent::OutPort_strategy = st.builds(
    dslComponent::OutPort,
)
dslComponent::InPort_strategy = st.builds(
    dslComponent::InPort,
)
dslComponent::Port_strategy = st.builds(
    dslComponent::Port,
    name=
        safe_text
)
dslComponent::DocumElt_strategy = st.builds(
    dslComponent::DocumElt,
    desc=
        safe_text,
    name=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
dslComponent::InitialState_strategy = st.builds(
    dslComponent::InitialState,
)
dslComponent::SimpleState_strategy = st.builds(
    dslComponent::SimpleState,
)
DocumElt_strategy = st.builds(
    DocumElt,
)
dslComponent::Edge_strategy = st.builds(
    dslComponent::Edge,
)
dslComponent::Vertex_strategy = st.builds(
    dslComponent::Vertex,
)
dslComponent::StateMachine_strategy = st.builds(
    dslComponent::StateMachine,
    name=
        safe_text
)
dslComponent::Component_strategy = st.builds(
    dslComponent::Component,
    id=
        safe_text,
    name=
        safe_text
)
dslComponent::ControlSubsystem_strategy = st.builds(
    dslComponent::ControlSubsystem,
    name=
        safe_text
)
dslComponent::Subsystem_strategy = st.builds(
    dslComponent::Subsystem,
    name=
        safe_text,
    description=
        safe_text
)
dslComponent::WTComponents_strategy = st.builds(
    dslComponent::WTComponents,
    id=
        safe_text,
    author=
        safe_text
)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=dslComponent::OutPort_strategy)
@settings(max_examples=50)
def test_dslcomponent::outport_instantiation(instance):
    assert isinstance(instance, dslComponent::OutPort)

@given(instance=dslComponent::InPort_strategy)
@settings(max_examples=50)
def test_dslcomponent::inport_instantiation(instance):
    assert isinstance(instance, dslComponent::InPort)

@given(instance=dslComponent::Port_strategy)
@settings(max_examples=50)
def test_dslcomponent::port_instantiation(instance):
    assert isinstance(instance, dslComponent::Port)

@given(instance=dslComponent::Port_strategy)
def test_dslcomponent::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dslComponent::Port_strategy)
def test_dslcomponent::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent::DocumElt_strategy)
@settings(max_examples=50)
def test_dslcomponent::documelt_instantiation(instance):
    assert isinstance(instance, dslComponent::DocumElt)

@given(instance=dslComponent::DocumElt_strategy)
def test_dslcomponent::documelt_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=dslComponent::DocumElt_strategy)
def test_dslcomponent::documelt_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=dslComponent::DocumElt_strategy)
def test_dslcomponent::documelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dslComponent::DocumElt_strategy)
def test_dslcomponent::documelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=dslComponent::InitialState_strategy)
@settings(max_examples=50)
def test_dslcomponent::initialstate_instantiation(instance):
    assert isinstance(instance, dslComponent::InitialState)

@given(instance=dslComponent::SimpleState_strategy)
@settings(max_examples=50)
def test_dslcomponent::simplestate_instantiation(instance):
    assert isinstance(instance, dslComponent::SimpleState)

@given(instance=DocumElt_strategy)
@settings(max_examples=50)
def test_documelt_instantiation(instance):
    assert isinstance(instance, DocumElt)

@given(instance=dslComponent::Edge_strategy)
@settings(max_examples=50)
def test_dslcomponent::edge_instantiation(instance):
    assert isinstance(instance, dslComponent::Edge)

@given(instance=dslComponent::Vertex_strategy)
@settings(max_examples=50)
def test_dslcomponent::vertex_instantiation(instance):
    assert isinstance(instance, dslComponent::Vertex)

@given(instance=dslComponent::StateMachine_strategy)
@settings(max_examples=50)
def test_dslcomponent::statemachine_instantiation(instance):
    assert isinstance(instance, dslComponent::StateMachine)

@given(instance=dslComponent::StateMachine_strategy)
def test_dslcomponent::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dslComponent::StateMachine_strategy)
def test_dslcomponent::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent::Component_strategy)
@settings(max_examples=50)
def test_dslcomponent::component_instantiation(instance):
    assert isinstance(instance, dslComponent::Component)

@given(instance=dslComponent::Component_strategy)
def test_dslcomponent::component_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dslComponent::Component_strategy)
def test_dslcomponent::component_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dslComponent::Component_strategy)
def test_dslcomponent::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dslComponent::Component_strategy)
def test_dslcomponent::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent::ControlSubsystem_strategy)
@settings(max_examples=50)
def test_dslcomponent::controlsubsystem_instantiation(instance):
    assert isinstance(instance, dslComponent::ControlSubsystem)

@given(instance=dslComponent::ControlSubsystem_strategy)
def test_dslcomponent::controlsubsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dslComponent::ControlSubsystem_strategy)
def test_dslcomponent::controlsubsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent::Subsystem_strategy)
@settings(max_examples=50)
def test_dslcomponent::subsystem_instantiation(instance):
    assert isinstance(instance, dslComponent::Subsystem)

@given(instance=dslComponent::Subsystem_strategy)
def test_dslcomponent::subsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dslComponent::Subsystem_strategy)
def test_dslcomponent::subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent::Subsystem_strategy)
def test_dslcomponent::subsystem_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=dslComponent::Subsystem_strategy)
def test_dslcomponent::subsystem_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=dslComponent::WTComponents_strategy)
@settings(max_examples=50)
def test_dslcomponent::wtcomponents_instantiation(instance):
    assert isinstance(instance, dslComponent::WTComponents)

@given(instance=dslComponent::WTComponents_strategy)
def test_dslcomponent::wtcomponents_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dslComponent::WTComponents_strategy)
def test_dslcomponent::wtcomponents_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dslComponent::WTComponents_strategy)
def test_dslcomponent::wtcomponents_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=dslComponent::WTComponents_strategy)
def test_dslcomponent::wtcomponents_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original
