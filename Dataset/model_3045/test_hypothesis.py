import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    df::Expression,
    df::VarToPortMapEntry,
    df::PortToVarMapEntry,
    df::Tag,
    df::Pattern,
    Edge,
    df::Transition,
    df::Connection,
    df::Vertex,
    df::PortToEIntegerObjectMapEntry,
    df::MoC,
    Graph,
    df::FSM,
    df::EObject,
    df::Argument,
    Adaptable,
    df::Network,
    df::Type,
    Vertex,
    df::Instance,
    df::State,
    df::Actor,
    df::Port,
    df::Procedure,
    df::Var,
    Attributable,
    df::Entity,
    df::Action,
    df::Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_df::expression_is_not_abstract():
    assert not inspect.isabstract(df::Expression)


def test_df::expression_constructor_exists():
    assert callable(df::Expression.__init__)


def test_df::expression_constructor_args():
    sig = inspect.signature(df::Expression.__init__)
    params = list(sig.parameters.keys())



def test_df::vartoportmapentry_is_not_abstract():
    assert not inspect.isabstract(df::VarToPortMapEntry)


def test_df::vartoportmapentry_constructor_exists():
    assert callable(df::VarToPortMapEntry.__init__)


def test_df::vartoportmapentry_constructor_args():
    sig = inspect.signature(df::VarToPortMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_df::porttovarmapentry_is_not_abstract():
    assert not inspect.isabstract(df::PortToVarMapEntry)


def test_df::porttovarmapentry_constructor_exists():
    assert callable(df::PortToVarMapEntry.__init__)


def test_df::porttovarmapentry_constructor_args():
    sig = inspect.signature(df::PortToVarMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_df::tag_is_not_abstract():
    assert not inspect.isabstract(df::Tag)


def test_df::tag_constructor_exists():
    assert callable(df::Tag.__init__)


def test_df::tag_constructor_args():
    sig = inspect.signature(df::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"

def test_df::tag_has_identifiers():
    assert hasattr(df::Tag, "identifiers")
    descriptor = None
    for klass in df::Tag.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)



def test_df::pattern_is_not_abstract():
    assert not inspect.isabstract(df::Pattern)


def test_df::pattern_constructor_exists():
    assert callable(df::Pattern.__init__)


def test_df::pattern_constructor_args():
    sig = inspect.signature(df::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_df::transition_is_not_abstract():
    assert not inspect.isabstract(df::Transition)


def test_df::transition_constructor_exists():
    assert callable(df::Transition.__init__)


def test_df::transition_constructor_args():
    sig = inspect.signature(df::Transition.__init__)
    params = list(sig.parameters.keys())



def test_df::connection_is_not_abstract():
    assert not inspect.isabstract(df::Connection)


def test_df::connection_constructor_exists():
    assert callable(df::Connection.__init__)


def test_df::connection_constructor_args():
    sig = inspect.signature(df::Connection.__init__)
    params = list(sig.parameters.keys())



def test_df::vertex_is_not_abstract():
    assert not inspect.isabstract(df::Vertex)


def test_df::vertex_constructor_exists():
    assert callable(df::Vertex.__init__)


def test_df::vertex_constructor_args():
    sig = inspect.signature(df::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_df::porttoeintegerobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(df::PortToEIntegerObjectMapEntry)


def test_df::porttoeintegerobjectmapentry_constructor_exists():
    assert callable(df::PortToEIntegerObjectMapEntry.__init__)


def test_df::porttoeintegerobjectmapentry_constructor_args():
    sig = inspect.signature(df::PortToEIntegerObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_df::porttoeintegerobjectmapentry_has_value():
    assert hasattr(df::PortToEIntegerObjectMapEntry, "value")
    descriptor = None
    for klass in df::PortToEIntegerObjectMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_df::moc_is_not_abstract():
    assert not inspect.isabstract(df::MoC)


def test_df::moc_constructor_exists():
    assert callable(df::MoC.__init__)


def test_df::moc_constructor_args():
    sig = inspect.signature(df::MoC.__init__)
    params = list(sig.parameters.keys())



def test_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_df::fsm_is_not_abstract():
    assert not inspect.isabstract(df::FSM)


def test_df::fsm_constructor_exists():
    assert callable(df::FSM.__init__)


def test_df::fsm_constructor_args():
    sig = inspect.signature(df::FSM.__init__)
    params = list(sig.parameters.keys())



def test_df::eobject_is_not_abstract():
    assert not inspect.isabstract(df::EObject)


def test_df::eobject_constructor_exists():
    assert callable(df::EObject.__init__)


def test_df::eobject_constructor_args():
    sig = inspect.signature(df::EObject.__init__)
    params = list(sig.parameters.keys())



def test_df::argument_is_not_abstract():
    assert not inspect.isabstract(df::Argument)


def test_df::argument_constructor_exists():
    assert callable(df::Argument.__init__)


def test_df::argument_constructor_args():
    sig = inspect.signature(df::Argument.__init__)
    params = list(sig.parameters.keys())



def test_adaptable_is_not_abstract():
    assert not inspect.isabstract(Adaptable)


def test_adaptable_constructor_exists():
    assert callable(Adaptable.__init__)


def test_adaptable_constructor_args():
    sig = inspect.signature(Adaptable.__init__)
    params = list(sig.parameters.keys())



def test_df::network_is_not_abstract():
    assert not inspect.isabstract(df::Network)


def test_df::network_constructor_exists():
    assert callable(df::Network.__init__)


def test_df::network_constructor_args():
    sig = inspect.signature(df::Network.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "name" in params, "Missing parameter 'name'"

def test_df::network_has_fileName():
    assert hasattr(df::Network, "fileName")
    descriptor = None
    for klass in df::Network.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_df::network_has_name():
    assert hasattr(df::Network, "name")
    descriptor = None
    for klass in df::Network.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_df::type_is_not_abstract():
    assert not inspect.isabstract(df::Type)


def test_df::type_constructor_exists():
    assert callable(df::Type.__init__)


def test_df::type_constructor_args():
    sig = inspect.signature(df::Type.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_df::instance_is_not_abstract():
    assert not inspect.isabstract(df::Instance)


def test_df::instance_constructor_exists():
    assert callable(df::Instance.__init__)


def test_df::instance_constructor_args():
    sig = inspect.signature(df::Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_df::instance_has_name():
    assert hasattr(df::Instance, "name")
    descriptor = None
    for klass in df::Instance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_df::state_is_not_abstract():
    assert not inspect.isabstract(df::State)


def test_df::state_constructor_exists():
    assert callable(df::State.__init__)


def test_df::state_constructor_args():
    sig = inspect.signature(df::State.__init__)
    params = list(sig.parameters.keys())



def test_df::actor_is_not_abstract():
    assert not inspect.isabstract(df::Actor)


def test_df::actor_constructor_exists():
    assert callable(df::Actor.__init__)


def test_df::actor_constructor_args():
    sig = inspect.signature(df::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"
    assert "native" in params, "Missing parameter 'native'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_df::actor_has_name():
    assert hasattr(df::Actor, "name")
    descriptor = None
    for klass in df::Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df::actor_has_lineNumber():
    assert hasattr(df::Actor, "lineNumber")
    descriptor = None
    for klass in df::Actor.__mro__:
        if "lineNumber" in klass.__dict__:
            descriptor = klass.__dict__["lineNumber"]
            break
    assert isinstance(descriptor, property)

def test_df::actor_has_native():
    assert hasattr(df::Actor, "native")
    descriptor = None
    for klass in df::Actor.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_df::actor_has_fileName():
    assert hasattr(df::Actor, "fileName")
    descriptor = None
    for klass in df::Actor.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_df::port_is_not_abstract():
    assert not inspect.isabstract(df::Port)


def test_df::port_constructor_exists():
    assert callable(df::Port.__init__)


def test_df::port_constructor_args():
    sig = inspect.signature(df::Port.__init__)
    params = list(sig.parameters.keys())
    assert "numTokensConsumed" in params, "Missing parameter 'numTokensConsumed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numTokensProduced" in params, "Missing parameter 'numTokensProduced'"

def test_df::port_has_numTokensConsumed():
    assert hasattr(df::Port, "numTokensConsumed")
    descriptor = None
    for klass in df::Port.__mro__:
        if "numTokensConsumed" in klass.__dict__:
            descriptor = klass.__dict__["numTokensConsumed"]
            break
    assert isinstance(descriptor, property)

def test_df::port_has_name():
    assert hasattr(df::Port, "name")
    descriptor = None
    for klass in df::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df::port_has_numTokensProduced():
    assert hasattr(df::Port, "numTokensProduced")
    descriptor = None
    for klass in df::Port.__mro__:
        if "numTokensProduced" in klass.__dict__:
            descriptor = klass.__dict__["numTokensProduced"]
            break
    assert isinstance(descriptor, property)



def test_df::procedure_is_not_abstract():
    assert not inspect.isabstract(df::Procedure)


def test_df::procedure_constructor_exists():
    assert callable(df::Procedure.__init__)


def test_df::procedure_constructor_args():
    sig = inspect.signature(df::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_df::var_is_not_abstract():
    assert not inspect.isabstract(df::Var)


def test_df::var_constructor_exists():
    assert callable(df::Var.__init__)


def test_df::var_constructor_args():
    sig = inspect.signature(df::Var.__init__)
    params = list(sig.parameters.keys())



def test_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_df::entity_is_not_abstract():
    assert not inspect.isabstract(df::Entity)


def test_df::entity_constructor_exists():
    assert callable(df::Entity.__init__)


def test_df::entity_constructor_args():
    sig = inspect.signature(df::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "incomingPortMap" in params, "Missing parameter 'incomingPortMap'"
    assert "name" in params, "Missing parameter 'name'"
    assert "outgoingPortMap" in params, "Missing parameter 'outgoingPortMap'"

def test_df::entity_has_incomingPortMap():
    assert hasattr(df::Entity, "incomingPortMap")
    descriptor = None
    for klass in df::Entity.__mro__:
        if "incomingPortMap" in klass.__dict__:
            descriptor = klass.__dict__["incomingPortMap"]
            break
    assert isinstance(descriptor, property)

def test_df::entity_has_name():
    assert hasattr(df::Entity, "name")
    descriptor = None
    for klass in df::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df::entity_has_outgoingPortMap():
    assert hasattr(df::Entity, "outgoingPortMap")
    descriptor = None
    for klass in df::Entity.__mro__:
        if "outgoingPortMap" in klass.__dict__:
            descriptor = klass.__dict__["outgoingPortMap"]
            break
    assert isinstance(descriptor, property)



def test_df::action_is_not_abstract():
    assert not inspect.isabstract(df::Action)


def test_df::action_constructor_exists():
    assert callable(df::Action.__init__)


def test_df::action_constructor_args():
    sig = inspect.signature(df::Action.__init__)
    params = list(sig.parameters.keys())



def test_df::unit_is_not_abstract():
    assert not inspect.isabstract(df::Unit)


def test_df::unit_constructor_exists():
    assert callable(df::Unit.__init__)


def test_df::unit_constructor_args():
    sig = inspect.signature(df::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"

def test_df::unit_has_name():
    assert hasattr(df::Unit, "name")
    descriptor = None
    for klass in df::Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df::unit_has_fileName():
    assert hasattr(df::Unit, "fileName")
    descriptor = None
    for klass in df::Unit.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_df::unit_has_lineNumber():
    assert hasattr(df::Unit, "lineNumber")
    descriptor = None
    for klass in df::Unit.__mro__:
        if "lineNumber" in klass.__dict__:
            descriptor = klass.__dict__["lineNumber"]
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
df::Expression_strategy = st.builds(
    df::Expression,
)
df::VarToPortMapEntry_strategy = st.builds(
    df::VarToPortMapEntry,
)
df::PortToVarMapEntry_strategy = st.builds(
    df::PortToVarMapEntry,
)
df::Tag_strategy = st.builds(
    df::Tag,
    identifiers=
        safe_text
)
df::Pattern_strategy = st.builds(
    df::Pattern,
)
Edge_strategy = st.builds(
    Edge,
)
df::Transition_strategy = st.builds(
    df::Transition,
)
df::Connection_strategy = st.builds(
    df::Connection,
)
df::Vertex_strategy = st.builds(
    df::Vertex,
)
df::PortToEIntegerObjectMapEntry_strategy = st.builds(
    df::PortToEIntegerObjectMapEntry,
    value=
        safe_text
)
df::MoC_strategy = st.builds(
    df::MoC,
)
Graph_strategy = st.builds(
    Graph,
)
df::FSM_strategy = st.builds(
    df::FSM,
)
df::EObject_strategy = st.builds(
    df::EObject,
)
df::Argument_strategy = st.builds(
    df::Argument,
)
Adaptable_strategy = st.builds(
    Adaptable,
)
df::Network_strategy = st.builds(
    df::Network,
    fileName=
        safe_text,
    name=
        safe_text
)
df::Type_strategy = st.builds(
    df::Type,
)
Vertex_strategy = st.builds(
    Vertex,
)
df::Instance_strategy = st.builds(
    df::Instance,
    name=
        safe_text
)
df::State_strategy = st.builds(
    df::State,
)
df::Actor_strategy = st.builds(
    df::Actor,
    name=
        safe_text,
    lineNumber=
        st.integers(),
    native=
        st.booleans(),
    fileName=
        safe_text
)
df::Port_strategy = st.builds(
    df::Port,
    numTokensConsumed=
        st.integers(),
    name=
        safe_text,
    numTokensProduced=
        st.integers()
)
df::Procedure_strategy = st.builds(
    df::Procedure,
)
df::Var_strategy = st.builds(
    df::Var,
)
Attributable_strategy = st.builds(
    Attributable,
)
df::Entity_strategy = st.builds(
    df::Entity,
    incomingPortMap=
        safe_text,
    name=
        safe_text,
    outgoingPortMap=
        safe_text
)
df::Action_strategy = st.builds(
    df::Action,
)
df::Unit_strategy = st.builds(
    df::Unit,
    name=
        safe_text,
    fileName=
        safe_text,
    lineNumber=
        st.integers()
)

@given(instance=df::Expression_strategy)
@settings(max_examples=50)
def test_df::expression_instantiation(instance):
    assert isinstance(instance, df::Expression)

@given(instance=df::VarToPortMapEntry_strategy)
@settings(max_examples=50)
def test_df::vartoportmapentry_instantiation(instance):
    assert isinstance(instance, df::VarToPortMapEntry)

@given(instance=df::PortToVarMapEntry_strategy)
@settings(max_examples=50)
def test_df::porttovarmapentry_instantiation(instance):
    assert isinstance(instance, df::PortToVarMapEntry)

@given(instance=df::Tag_strategy)
@settings(max_examples=50)
def test_df::tag_instantiation(instance):
    assert isinstance(instance, df::Tag)

@given(instance=df::Tag_strategy)
def test_df::tag_identifiers_type(instance):
    assert isinstance(instance.identifiers, str)


@given(instance=df::Tag_strategy)
def test_df::tag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=df::Pattern_strategy)
@settings(max_examples=50)
def test_df::pattern_instantiation(instance):
    assert isinstance(instance, df::Pattern)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=df::Transition_strategy)
@settings(max_examples=50)
def test_df::transition_instantiation(instance):
    assert isinstance(instance, df::Transition)

@given(instance=df::Connection_strategy)
@settings(max_examples=50)
def test_df::connection_instantiation(instance):
    assert isinstance(instance, df::Connection)

@given(instance=df::Vertex_strategy)
@settings(max_examples=50)
def test_df::vertex_instantiation(instance):
    assert isinstance(instance, df::Vertex)

@given(instance=df::PortToEIntegerObjectMapEntry_strategy)
@settings(max_examples=50)
def test_df::porttoeintegerobjectmapentry_instantiation(instance):
    assert isinstance(instance, df::PortToEIntegerObjectMapEntry)

@given(instance=df::PortToEIntegerObjectMapEntry_strategy)
def test_df::porttoeintegerobjectmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=df::PortToEIntegerObjectMapEntry_strategy)
def test_df::porttoeintegerobjectmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=df::MoC_strategy)
@settings(max_examples=50)
def test_df::moc_instantiation(instance):
    assert isinstance(instance, df::MoC)

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=df::FSM_strategy)
@settings(max_examples=50)
def test_df::fsm_instantiation(instance):
    assert isinstance(instance, df::FSM)

@given(instance=df::EObject_strategy)
@settings(max_examples=50)
def test_df::eobject_instantiation(instance):
    assert isinstance(instance, df::EObject)

@given(instance=df::Argument_strategy)
@settings(max_examples=50)
def test_df::argument_instantiation(instance):
    assert isinstance(instance, df::Argument)

@given(instance=Adaptable_strategy)
@settings(max_examples=50)
def test_adaptable_instantiation(instance):
    assert isinstance(instance, Adaptable)

@given(instance=df::Network_strategy)
@settings(max_examples=50)
def test_df::network_instantiation(instance):
    assert isinstance(instance, df::Network)

@given(instance=df::Network_strategy)
def test_df::network_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=df::Network_strategy)
def test_df::network_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=df::Network_strategy)
def test_df::network_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=df::Network_strategy)
def test_df::network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df::Type_strategy)
@settings(max_examples=50)
def test_df::type_instantiation(instance):
    assert isinstance(instance, df::Type)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=df::Instance_strategy)
@settings(max_examples=50)
def test_df::instance_instantiation(instance):
    assert isinstance(instance, df::Instance)

@given(instance=df::Instance_strategy)
def test_df::instance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=df::Instance_strategy)
def test_df::instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df::State_strategy)
@settings(max_examples=50)
def test_df::state_instantiation(instance):
    assert isinstance(instance, df::State)

@given(instance=df::Actor_strategy)
@settings(max_examples=50)
def test_df::actor_instantiation(instance):
    assert isinstance(instance, df::Actor)

@given(instance=df::Actor_strategy)
def test_df::actor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=df::Actor_strategy)
def test_df::actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df::Actor_strategy)
def test_df::actor_lineNumber_type(instance):
    assert isinstance(instance.lineNumber, int)


@given(instance=df::Actor_strategy)
def test_df::actor_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original

@given(instance=df::Actor_strategy)
def test_df::actor_native_type(instance):
    assert isinstance(instance.native, bool)


@given(instance=df::Actor_strategy)
def test_df::actor_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=df::Actor_strategy)
def test_df::actor_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=df::Actor_strategy)
def test_df::actor_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=df::Port_strategy)
@settings(max_examples=50)
def test_df::port_instantiation(instance):
    assert isinstance(instance, df::Port)

@given(instance=df::Port_strategy)
def test_df::port_numTokensConsumed_type(instance):
    assert isinstance(instance.numTokensConsumed, int)


@given(instance=df::Port_strategy)
def test_df::port_numTokensConsumed_setter(instance):
    original = instance.numTokensConsumed
    instance.numTokensConsumed = original
    assert instance.numTokensConsumed == original

@given(instance=df::Port_strategy)
def test_df::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=df::Port_strategy)
def test_df::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df::Port_strategy)
def test_df::port_numTokensProduced_type(instance):
    assert isinstance(instance.numTokensProduced, int)


@given(instance=df::Port_strategy)
def test_df::port_numTokensProduced_setter(instance):
    original = instance.numTokensProduced
    instance.numTokensProduced = original
    assert instance.numTokensProduced == original

@given(instance=df::Procedure_strategy)
@settings(max_examples=50)
def test_df::procedure_instantiation(instance):
    assert isinstance(instance, df::Procedure)

@given(instance=df::Var_strategy)
@settings(max_examples=50)
def test_df::var_instantiation(instance):
    assert isinstance(instance, df::Var)

@given(instance=Attributable_strategy)
@settings(max_examples=50)
def test_attributable_instantiation(instance):
    assert isinstance(instance, Attributable)

@given(instance=df::Entity_strategy)
@settings(max_examples=50)
def test_df::entity_instantiation(instance):
    assert isinstance(instance, df::Entity)

@given(instance=df::Entity_strategy)
def test_df::entity_incomingPortMap_type(instance):
    assert isinstance(instance.incomingPortMap, str)


@given(instance=df::Entity_strategy)
def test_df::entity_incomingPortMap_setter(instance):
    original = instance.incomingPortMap
    instance.incomingPortMap = original
    assert instance.incomingPortMap == original

@given(instance=df::Entity_strategy)
def test_df::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=df::Entity_strategy)
def test_df::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df::Entity_strategy)
def test_df::entity_outgoingPortMap_type(instance):
    assert isinstance(instance.outgoingPortMap, str)


@given(instance=df::Entity_strategy)
def test_df::entity_outgoingPortMap_setter(instance):
    original = instance.outgoingPortMap
    instance.outgoingPortMap = original
    assert instance.outgoingPortMap == original

@given(instance=df::Action_strategy)
@settings(max_examples=50)
def test_df::action_instantiation(instance):
    assert isinstance(instance, df::Action)

@given(instance=df::Unit_strategy)
@settings(max_examples=50)
def test_df::unit_instantiation(instance):
    assert isinstance(instance, df::Unit)

@given(instance=df::Unit_strategy)
def test_df::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=df::Unit_strategy)
def test_df::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df::Unit_strategy)
def test_df::unit_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=df::Unit_strategy)
def test_df::unit_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=df::Unit_strategy)
def test_df::unit_lineNumber_type(instance):
    assert isinstance(instance.lineNumber, int)


@given(instance=df::Unit_strategy)
def test_df::unit_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original
