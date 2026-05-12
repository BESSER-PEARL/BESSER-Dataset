import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dslComponent_Port,
    Port,
    dslComponent_OutPort,
    dslComponent_InPort,
    dslComponent_DocumElt,
    dslComponent_Component,
    dslComponent_ControlSubsystem,
    Vertex,
    dslComponent_InitialState,
    dslComponent_SimpleState,
    dslComponent_Subsystem,
    DocumElt,
    dslComponent_Edge,
    dslComponent_Vertex,
    dslComponent_StateMachine,
    dslComponent_WTComponents,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dslcomponent_port_is_not_abstract():
    assert not inspect.isabstract(dslComponent_Port)


def test_dslcomponent_port_constructor_exists():
    assert callable(dslComponent_Port.__init__)


def test_dslcomponent_port_constructor_args():
    sig = inspect.signature(dslComponent_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent_port_has_name():
    assert hasattr(dslComponent_Port, "name")
    descriptor = None
    for klass in dslComponent_Port.__mro__:
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



def test_dslcomponent_outport_is_not_abstract():
    assert not inspect.isabstract(dslComponent_OutPort)


def test_dslcomponent_outport_constructor_exists():
    assert callable(dslComponent_OutPort.__init__)


def test_dslcomponent_outport_constructor_args():
    sig = inspect.signature(dslComponent_OutPort.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_inport_is_not_abstract():
    assert not inspect.isabstract(dslComponent_InPort)


def test_dslcomponent_inport_constructor_exists():
    assert callable(dslComponent_InPort.__init__)


def test_dslcomponent_inport_constructor_args():
    sig = inspect.signature(dslComponent_InPort.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_documelt_is_not_abstract():
    assert not inspect.isabstract(dslComponent_DocumElt)


def test_dslcomponent_documelt_constructor_exists():
    assert callable(dslComponent_DocumElt.__init__)


def test_dslcomponent_documelt_constructor_args():
    sig = inspect.signature(dslComponent_DocumElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_dslcomponent_documelt_has_name():
    assert hasattr(dslComponent_DocumElt, "name")
    descriptor = None
    for klass in dslComponent_DocumElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent_documelt_has_desc():
    assert hasattr(dslComponent_DocumElt, "desc")
    descriptor = None
    for klass in dslComponent_DocumElt.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent_component_is_not_abstract():
    assert not inspect.isabstract(dslComponent_Component)


def test_dslcomponent_component_constructor_exists():
    assert callable(dslComponent_Component.__init__)


def test_dslcomponent_component_constructor_args():
    sig = inspect.signature(dslComponent_Component.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent_component_has_id():
    assert hasattr(dslComponent_Component, "id")
    descriptor = None
    for klass in dslComponent_Component.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent_component_has_name():
    assert hasattr(dslComponent_Component, "name")
    descriptor = None
    for klass in dslComponent_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent_controlsubsystem_is_not_abstract():
    assert not inspect.isabstract(dslComponent_ControlSubsystem)


def test_dslcomponent_controlsubsystem_constructor_exists():
    assert callable(dslComponent_ControlSubsystem.__init__)


def test_dslcomponent_controlsubsystem_constructor_args():
    sig = inspect.signature(dslComponent_ControlSubsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent_controlsubsystem_has_name():
    assert hasattr(dslComponent_ControlSubsystem, "name")
    descriptor = None
    for klass in dslComponent_ControlSubsystem.__mro__:
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



def test_dslcomponent_initialstate_is_not_abstract():
    assert not inspect.isabstract(dslComponent_InitialState)


def test_dslcomponent_initialstate_constructor_exists():
    assert callable(dslComponent_InitialState.__init__)


def test_dslcomponent_initialstate_constructor_args():
    sig = inspect.signature(dslComponent_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_simplestate_is_not_abstract():
    assert not inspect.isabstract(dslComponent_SimpleState)


def test_dslcomponent_simplestate_constructor_exists():
    assert callable(dslComponent_SimpleState.__init__)


def test_dslcomponent_simplestate_constructor_args():
    sig = inspect.signature(dslComponent_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_subsystem_is_not_abstract():
    assert not inspect.isabstract(dslComponent_Subsystem)


def test_dslcomponent_subsystem_constructor_exists():
    assert callable(dslComponent_Subsystem.__init__)


def test_dslcomponent_subsystem_constructor_args():
    sig = inspect.signature(dslComponent_Subsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_dslcomponent_subsystem_has_name():
    assert hasattr(dslComponent_Subsystem, "name")
    descriptor = None
    for klass in dslComponent_Subsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent_subsystem_has_description():
    assert hasattr(dslComponent_Subsystem, "description")
    descriptor = None
    for klass in dslComponent_Subsystem.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_documelt_is_not_abstract():
    assert not inspect.isabstract(DocumElt)


def test_documelt_constructor_exists():
    assert callable(DocumElt.__init__)


def test_documelt_constructor_args():
    sig = inspect.signature(DocumElt.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_edge_is_not_abstract():
    assert not inspect.isabstract(dslComponent_Edge)


def test_dslcomponent_edge_constructor_exists():
    assert callable(dslComponent_Edge.__init__)


def test_dslcomponent_edge_constructor_args():
    sig = inspect.signature(dslComponent_Edge.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_vertex_is_not_abstract():
    assert not inspect.isabstract(dslComponent_Vertex)


def test_dslcomponent_vertex_constructor_exists():
    assert callable(dslComponent_Vertex.__init__)


def test_dslcomponent_vertex_constructor_args():
    sig = inspect.signature(dslComponent_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_dslcomponent_statemachine_is_not_abstract():
    assert not inspect.isabstract(dslComponent_StateMachine)


def test_dslcomponent_statemachine_constructor_exists():
    assert callable(dslComponent_StateMachine.__init__)


def test_dslcomponent_statemachine_constructor_args():
    sig = inspect.signature(dslComponent_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dslcomponent_statemachine_has_name():
    assert hasattr(dslComponent_StateMachine, "name")
    descriptor = None
    for klass in dslComponent_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dslcomponent_wtcomponents_is_not_abstract():
    assert not inspect.isabstract(dslComponent_WTComponents)


def test_dslcomponent_wtcomponents_constructor_exists():
    assert callable(dslComponent_WTComponents.__init__)


def test_dslcomponent_wtcomponents_constructor_args():
    sig = inspect.signature(dslComponent_WTComponents.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "author" in params, "Missing parameter 'author'"

def test_dslcomponent_wtcomponents_has_id():
    assert hasattr(dslComponent_WTComponents, "id")
    descriptor = None
    for klass in dslComponent_WTComponents.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dslcomponent_wtcomponents_has_author():
    assert hasattr(dslComponent_WTComponents, "author")
    descriptor = None
    for klass in dslComponent_WTComponents.__mro__:
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
dslComponent_Port_strategy = st.builds(
    dslComponent_Port,
    name=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
dslComponent_OutPort_strategy = st.builds(
    dslComponent_OutPort,
)
dslComponent_InPort_strategy = st.builds(
    dslComponent_InPort,
)
dslComponent_DocumElt_strategy = st.builds(
    dslComponent_DocumElt,
    name=
        safe_text,
    desc=
        safe_text
)
dslComponent_Component_strategy = st.builds(
    dslComponent_Component,
    id=
        safe_text,
    name=
        safe_text
)
dslComponent_ControlSubsystem_strategy = st.builds(
    dslComponent_ControlSubsystem,
    name=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
dslComponent_InitialState_strategy = st.builds(
    dslComponent_InitialState,
)
dslComponent_SimpleState_strategy = st.builds(
    dslComponent_SimpleState,
)
dslComponent_Subsystem_strategy = st.builds(
    dslComponent_Subsystem,
    name=
        safe_text,
    description=
        safe_text
)
DocumElt_strategy = st.builds(
    DocumElt,
)
dslComponent_Edge_strategy = st.builds(
    dslComponent_Edge,
)
dslComponent_Vertex_strategy = st.builds(
    dslComponent_Vertex,
)
dslComponent_StateMachine_strategy = st.builds(
    dslComponent_StateMachine,
    name=
        safe_text
)
dslComponent_WTComponents_strategy = st.builds(
    dslComponent_WTComponents,
    id=
        safe_text,
    author=
        safe_text
)

@given(instance=dslComponent_Port_strategy)
@settings(max_examples=50)
def test_dslcomponent_port_instantiation(instance):
    assert isinstance(instance, dslComponent_Port)



@given(instance=dslComponent_Port_strategy)
def test_dslcomponent_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=dslComponent_OutPort_strategy)
@settings(max_examples=50)
def test_dslcomponent_outport_instantiation(instance):
    assert isinstance(instance, dslComponent_OutPort)

@given(instance=dslComponent_InPort_strategy)
@settings(max_examples=50)
def test_dslcomponent_inport_instantiation(instance):
    assert isinstance(instance, dslComponent_InPort)

@given(instance=dslComponent_DocumElt_strategy)
@settings(max_examples=50)
def test_dslcomponent_documelt_instantiation(instance):
    assert isinstance(instance, dslComponent_DocumElt)



@given(instance=dslComponent_DocumElt_strategy)
def test_dslcomponent_documelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dslComponent_DocumElt_strategy)
def test_dslcomponent_documelt_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=dslComponent_Component_strategy)
@settings(max_examples=50)
def test_dslcomponent_component_instantiation(instance):
    assert isinstance(instance, dslComponent_Component)



@given(instance=dslComponent_Component_strategy)
def test_dslcomponent_component_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dslComponent_Component_strategy)
def test_dslcomponent_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent_ControlSubsystem_strategy)
@settings(max_examples=50)
def test_dslcomponent_controlsubsystem_instantiation(instance):
    assert isinstance(instance, dslComponent_ControlSubsystem)



@given(instance=dslComponent_ControlSubsystem_strategy)
def test_dslcomponent_controlsubsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=dslComponent_InitialState_strategy)
@settings(max_examples=50)
def test_dslcomponent_initialstate_instantiation(instance):
    assert isinstance(instance, dslComponent_InitialState)

@given(instance=dslComponent_SimpleState_strategy)
@settings(max_examples=50)
def test_dslcomponent_simplestate_instantiation(instance):
    assert isinstance(instance, dslComponent_SimpleState)

@given(instance=dslComponent_Subsystem_strategy)
@settings(max_examples=50)
def test_dslcomponent_subsystem_instantiation(instance):
    assert isinstance(instance, dslComponent_Subsystem)



@given(instance=dslComponent_Subsystem_strategy)
def test_dslcomponent_subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dslComponent_Subsystem_strategy)
def test_dslcomponent_subsystem_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=DocumElt_strategy)
@settings(max_examples=50)
def test_documelt_instantiation(instance):
    assert isinstance(instance, DocumElt)

@given(instance=dslComponent_Edge_strategy)
@settings(max_examples=50)
def test_dslcomponent_edge_instantiation(instance):
    assert isinstance(instance, dslComponent_Edge)

@given(instance=dslComponent_Vertex_strategy)
@settings(max_examples=50)
def test_dslcomponent_vertex_instantiation(instance):
    assert isinstance(instance, dslComponent_Vertex)

@given(instance=dslComponent_StateMachine_strategy)
@settings(max_examples=50)
def test_dslcomponent_statemachine_instantiation(instance):
    assert isinstance(instance, dslComponent_StateMachine)



@given(instance=dslComponent_StateMachine_strategy)
def test_dslcomponent_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dslComponent_WTComponents_strategy)
@settings(max_examples=50)
def test_dslcomponent_wtcomponents_instantiation(instance):
    assert isinstance(instance, dslComponent_WTComponents)



@given(instance=dslComponent_WTComponents_strategy)
def test_dslcomponent_wtcomponents_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dslComponent_WTComponents_strategy)
def test_dslcomponent_wtcomponents_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original
