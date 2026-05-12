import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    df_Expression,
    df_VarToPortMapEntry,
    df_PortToVarMapEntry,
    df_Tag,
    df_Pattern,
    Edge,
    df_Transition,
    df_Connection,
    df_Vertex,
    df_PortToEIntegerObjectMapEntry,
    df_MoC,
    Graph,
    df_FSM,
    df_EObject,
    df_Argument,
    Adaptable,
    df_Network,
    df_Type,
    Vertex,
    df_Actor,
    df_State,
    df_Instance,
    df_Port,
    df_Procedure,
    df_Var,
    Attributable,
    df_Action,
    df_Entity,
    df_Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_df_expression_is_not_abstract():
    assert not inspect.isabstract(df_Expression)


def test_df_expression_constructor_exists():
    assert callable(df_Expression.__init__)


def test_df_expression_constructor_args():
    sig = inspect.signature(df_Expression.__init__)
    params = list(sig.parameters.keys())



def test_df_vartoportmapentry_is_not_abstract():
    assert not inspect.isabstract(df_VarToPortMapEntry)


def test_df_vartoportmapentry_constructor_exists():
    assert callable(df_VarToPortMapEntry.__init__)


def test_df_vartoportmapentry_constructor_args():
    sig = inspect.signature(df_VarToPortMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_df_porttovarmapentry_is_not_abstract():
    assert not inspect.isabstract(df_PortToVarMapEntry)


def test_df_porttovarmapentry_constructor_exists():
    assert callable(df_PortToVarMapEntry.__init__)


def test_df_porttovarmapentry_constructor_args():
    sig = inspect.signature(df_PortToVarMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_df_tag_is_not_abstract():
    assert not inspect.isabstract(df_Tag)


def test_df_tag_constructor_exists():
    assert callable(df_Tag.__init__)


def test_df_tag_constructor_args():
    sig = inspect.signature(df_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"

def test_df_tag_has_identifiers():
    assert hasattr(df_Tag, "identifiers")
    descriptor = None
    for klass in df_Tag.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)



def test_df_pattern_is_not_abstract():
    assert not inspect.isabstract(df_Pattern)


def test_df_pattern_constructor_exists():
    assert callable(df_Pattern.__init__)


def test_df_pattern_constructor_args():
    sig = inspect.signature(df_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_df_transition_is_not_abstract():
    assert not inspect.isabstract(df_Transition)


def test_df_transition_constructor_exists():
    assert callable(df_Transition.__init__)


def test_df_transition_constructor_args():
    sig = inspect.signature(df_Transition.__init__)
    params = list(sig.parameters.keys())



def test_df_connection_is_not_abstract():
    assert not inspect.isabstract(df_Connection)


def test_df_connection_constructor_exists():
    assert callable(df_Connection.__init__)


def test_df_connection_constructor_args():
    sig = inspect.signature(df_Connection.__init__)
    params = list(sig.parameters.keys())



def test_df_vertex_is_not_abstract():
    assert not inspect.isabstract(df_Vertex)


def test_df_vertex_constructor_exists():
    assert callable(df_Vertex.__init__)


def test_df_vertex_constructor_args():
    sig = inspect.signature(df_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_df_porttoeintegerobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(df_PortToEIntegerObjectMapEntry)


def test_df_porttoeintegerobjectmapentry_constructor_exists():
    assert callable(df_PortToEIntegerObjectMapEntry.__init__)


def test_df_porttoeintegerobjectmapentry_constructor_args():
    sig = inspect.signature(df_PortToEIntegerObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_df_porttoeintegerobjectmapentry_has_value():
    assert hasattr(df_PortToEIntegerObjectMapEntry, "value")
    descriptor = None
    for klass in df_PortToEIntegerObjectMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_df_moc_is_not_abstract():
    assert not inspect.isabstract(df_MoC)


def test_df_moc_constructor_exists():
    assert callable(df_MoC.__init__)


def test_df_moc_constructor_args():
    sig = inspect.signature(df_MoC.__init__)
    params = list(sig.parameters.keys())



def test_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_df_fsm_is_not_abstract():
    assert not inspect.isabstract(df_FSM)


def test_df_fsm_constructor_exists():
    assert callable(df_FSM.__init__)


def test_df_fsm_constructor_args():
    sig = inspect.signature(df_FSM.__init__)
    params = list(sig.parameters.keys())



def test_df_eobject_is_not_abstract():
    assert not inspect.isabstract(df_EObject)


def test_df_eobject_constructor_exists():
    assert callable(df_EObject.__init__)


def test_df_eobject_constructor_args():
    sig = inspect.signature(df_EObject.__init__)
    params = list(sig.parameters.keys())



def test_df_argument_is_not_abstract():
    assert not inspect.isabstract(df_Argument)


def test_df_argument_constructor_exists():
    assert callable(df_Argument.__init__)


def test_df_argument_constructor_args():
    sig = inspect.signature(df_Argument.__init__)
    params = list(sig.parameters.keys())



def test_adaptable_is_not_abstract():
    assert not inspect.isabstract(Adaptable)


def test_adaptable_constructor_exists():
    assert callable(Adaptable.__init__)


def test_adaptable_constructor_args():
    sig = inspect.signature(Adaptable.__init__)
    params = list(sig.parameters.keys())



def test_df_network_is_not_abstract():
    assert not inspect.isabstract(df_Network)


def test_df_network_constructor_exists():
    assert callable(df_Network.__init__)


def test_df_network_constructor_args():
    sig = inspect.signature(df_Network.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "name" in params, "Missing parameter 'name'"

def test_df_network_has_fileName():
    assert hasattr(df_Network, "fileName")
    descriptor = None
    for klass in df_Network.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_df_network_has_name():
    assert hasattr(df_Network, "name")
    descriptor = None
    for klass in df_Network.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_df_type_is_not_abstract():
    assert not inspect.isabstract(df_Type)


def test_df_type_constructor_exists():
    assert callable(df_Type.__init__)


def test_df_type_constructor_args():
    sig = inspect.signature(df_Type.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_df_actor_is_not_abstract():
    assert not inspect.isabstract(df_Actor)


def test_df_actor_constructor_exists():
    assert callable(df_Actor.__init__)


def test_df_actor_constructor_args():
    sig = inspect.signature(df_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "native" in params, "Missing parameter 'native'"
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_df_actor_has_fileName():
    assert hasattr(df_Actor, "fileName")
    descriptor = None
    for klass in df_Actor.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_df_actor_has_native():
    assert hasattr(df_Actor, "native")
    descriptor = None
    for klass in df_Actor.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_df_actor_has_lineNumber():
    assert hasattr(df_Actor, "lineNumber")
    descriptor = None
    for klass in df_Actor.__mro__:
        if "lineNumber" in klass.__dict__:
            descriptor = klass.__dict__["lineNumber"]
            break
    assert isinstance(descriptor, property)

def test_df_actor_has_name():
    assert hasattr(df_Actor, "name")
    descriptor = None
    for klass in df_Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_df_state_is_not_abstract():
    assert not inspect.isabstract(df_State)


def test_df_state_constructor_exists():
    assert callable(df_State.__init__)


def test_df_state_constructor_args():
    sig = inspect.signature(df_State.__init__)
    params = list(sig.parameters.keys())



def test_df_instance_is_not_abstract():
    assert not inspect.isabstract(df_Instance)


def test_df_instance_constructor_exists():
    assert callable(df_Instance.__init__)


def test_df_instance_constructor_args():
    sig = inspect.signature(df_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_df_instance_has_name():
    assert hasattr(df_Instance, "name")
    descriptor = None
    for klass in df_Instance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_df_port_is_not_abstract():
    assert not inspect.isabstract(df_Port)


def test_df_port_constructor_exists():
    assert callable(df_Port.__init__)


def test_df_port_constructor_args():
    sig = inspect.signature(df_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numTokensConsumed" in params, "Missing parameter 'numTokensConsumed'"
    assert "numTokensProduced" in params, "Missing parameter 'numTokensProduced'"

def test_df_port_has_name():
    assert hasattr(df_Port, "name")
    descriptor = None
    for klass in df_Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df_port_has_numTokensConsumed():
    assert hasattr(df_Port, "numTokensConsumed")
    descriptor = None
    for klass in df_Port.__mro__:
        if "numTokensConsumed" in klass.__dict__:
            descriptor = klass.__dict__["numTokensConsumed"]
            break
    assert isinstance(descriptor, property)

def test_df_port_has_numTokensProduced():
    assert hasattr(df_Port, "numTokensProduced")
    descriptor = None
    for klass in df_Port.__mro__:
        if "numTokensProduced" in klass.__dict__:
            descriptor = klass.__dict__["numTokensProduced"]
            break
    assert isinstance(descriptor, property)



def test_df_procedure_is_not_abstract():
    assert not inspect.isabstract(df_Procedure)


def test_df_procedure_constructor_exists():
    assert callable(df_Procedure.__init__)


def test_df_procedure_constructor_args():
    sig = inspect.signature(df_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_df_var_is_not_abstract():
    assert not inspect.isabstract(df_Var)


def test_df_var_constructor_exists():
    assert callable(df_Var.__init__)


def test_df_var_constructor_args():
    sig = inspect.signature(df_Var.__init__)
    params = list(sig.parameters.keys())



def test_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_df_action_is_not_abstract():
    assert not inspect.isabstract(df_Action)


def test_df_action_constructor_exists():
    assert callable(df_Action.__init__)


def test_df_action_constructor_args():
    sig = inspect.signature(df_Action.__init__)
    params = list(sig.parameters.keys())



def test_df_entity_is_not_abstract():
    assert not inspect.isabstract(df_Entity)


def test_df_entity_constructor_exists():
    assert callable(df_Entity.__init__)


def test_df_entity_constructor_args():
    sig = inspect.signature(df_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "outgoingPortMap" in params, "Missing parameter 'outgoingPortMap'"
    assert "name" in params, "Missing parameter 'name'"
    assert "incomingPortMap" in params, "Missing parameter 'incomingPortMap'"

def test_df_entity_has_outgoingPortMap():
    assert hasattr(df_Entity, "outgoingPortMap")
    descriptor = None
    for klass in df_Entity.__mro__:
        if "outgoingPortMap" in klass.__dict__:
            descriptor = klass.__dict__["outgoingPortMap"]
            break
    assert isinstance(descriptor, property)

def test_df_entity_has_name():
    assert hasattr(df_Entity, "name")
    descriptor = None
    for klass in df_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df_entity_has_incomingPortMap():
    assert hasattr(df_Entity, "incomingPortMap")
    descriptor = None
    for klass in df_Entity.__mro__:
        if "incomingPortMap" in klass.__dict__:
            descriptor = klass.__dict__["incomingPortMap"]
            break
    assert isinstance(descriptor, property)



def test_df_unit_is_not_abstract():
    assert not inspect.isabstract(df_Unit)


def test_df_unit_constructor_exists():
    assert callable(df_Unit.__init__)


def test_df_unit_constructor_args():
    sig = inspect.signature(df_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_df_unit_has_lineNumber():
    assert hasattr(df_Unit, "lineNumber")
    descriptor = None
    for klass in df_Unit.__mro__:
        if "lineNumber" in klass.__dict__:
            descriptor = klass.__dict__["lineNumber"]
            break
    assert isinstance(descriptor, property)

def test_df_unit_has_name():
    assert hasattr(df_Unit, "name")
    descriptor = None
    for klass in df_Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_df_unit_has_fileName():
    assert hasattr(df_Unit, "fileName")
    descriptor = None
    for klass in df_Unit.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
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
df_Expression_strategy = st.builds(
    df_Expression,
)
df_VarToPortMapEntry_strategy = st.builds(
    df_VarToPortMapEntry,
)
df_PortToVarMapEntry_strategy = st.builds(
    df_PortToVarMapEntry,
)
df_Tag_strategy = st.builds(
    df_Tag,
    identifiers=
        safe_text
)
df_Pattern_strategy = st.builds(
    df_Pattern,
)
Edge_strategy = st.builds(
    Edge,
)
df_Transition_strategy = st.builds(
    df_Transition,
)
df_Connection_strategy = st.builds(
    df_Connection,
)
df_Vertex_strategy = st.builds(
    df_Vertex,
)
df_PortToEIntegerObjectMapEntry_strategy = st.builds(
    df_PortToEIntegerObjectMapEntry,
    value=
        safe_text
)
df_MoC_strategy = st.builds(
    df_MoC,
)
Graph_strategy = st.builds(
    Graph,
)
df_FSM_strategy = st.builds(
    df_FSM,
)
df_EObject_strategy = st.builds(
    df_EObject,
)
df_Argument_strategy = st.builds(
    df_Argument,
)
Adaptable_strategy = st.builds(
    Adaptable,
)
df_Network_strategy = st.builds(
    df_Network,
    fileName=
        safe_text,
    name=
        safe_text
)
df_Type_strategy = st.builds(
    df_Type,
)
Vertex_strategy = st.builds(
    Vertex,
)
df_Actor_strategy = st.builds(
    df_Actor,
    fileName=
        safe_text,
    native=
        st.booleans(),
    lineNumber=
        st.integers(),
    name=
        safe_text
)
df_State_strategy = st.builds(
    df_State,
)
df_Instance_strategy = st.builds(
    df_Instance,
    name=
        safe_text
)
df_Port_strategy = st.builds(
    df_Port,
    name=
        safe_text,
    numTokensConsumed=
        st.integers(),
    numTokensProduced=
        st.integers()
)
df_Procedure_strategy = st.builds(
    df_Procedure,
)
df_Var_strategy = st.builds(
    df_Var,
)
Attributable_strategy = st.builds(
    Attributable,
)
df_Action_strategy = st.builds(
    df_Action,
)
df_Entity_strategy = st.builds(
    df_Entity,
    outgoingPortMap=
        safe_text,
    name=
        safe_text,
    incomingPortMap=
        safe_text
)
df_Unit_strategy = st.builds(
    df_Unit,
    lineNumber=
        st.integers(),
    name=
        safe_text,
    fileName=
        safe_text
)

@given(instance=df_Expression_strategy)
@settings(max_examples=50)
def test_df_expression_instantiation(instance):
    assert isinstance(instance, df_Expression)

@given(instance=df_VarToPortMapEntry_strategy)
@settings(max_examples=50)
def test_df_vartoportmapentry_instantiation(instance):
    assert isinstance(instance, df_VarToPortMapEntry)

@given(instance=df_PortToVarMapEntry_strategy)
@settings(max_examples=50)
def test_df_porttovarmapentry_instantiation(instance):
    assert isinstance(instance, df_PortToVarMapEntry)

@given(instance=df_Tag_strategy)
@settings(max_examples=50)
def test_df_tag_instantiation(instance):
    assert isinstance(instance, df_Tag)



@given(instance=df_Tag_strategy)
def test_df_tag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=df_Pattern_strategy)
@settings(max_examples=50)
def test_df_pattern_instantiation(instance):
    assert isinstance(instance, df_Pattern)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=df_Transition_strategy)
@settings(max_examples=50)
def test_df_transition_instantiation(instance):
    assert isinstance(instance, df_Transition)

@given(instance=df_Connection_strategy)
@settings(max_examples=50)
def test_df_connection_instantiation(instance):
    assert isinstance(instance, df_Connection)

@given(instance=df_Vertex_strategy)
@settings(max_examples=50)
def test_df_vertex_instantiation(instance):
    assert isinstance(instance, df_Vertex)

@given(instance=df_PortToEIntegerObjectMapEntry_strategy)
@settings(max_examples=50)
def test_df_porttoeintegerobjectmapentry_instantiation(instance):
    assert isinstance(instance, df_PortToEIntegerObjectMapEntry)



@given(instance=df_PortToEIntegerObjectMapEntry_strategy)
def test_df_porttoeintegerobjectmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=df_MoC_strategy)
@settings(max_examples=50)
def test_df_moc_instantiation(instance):
    assert isinstance(instance, df_MoC)

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=df_FSM_strategy)
@settings(max_examples=50)
def test_df_fsm_instantiation(instance):
    assert isinstance(instance, df_FSM)

@given(instance=df_EObject_strategy)
@settings(max_examples=50)
def test_df_eobject_instantiation(instance):
    assert isinstance(instance, df_EObject)

@given(instance=df_Argument_strategy)
@settings(max_examples=50)
def test_df_argument_instantiation(instance):
    assert isinstance(instance, df_Argument)

@given(instance=Adaptable_strategy)
@settings(max_examples=50)
def test_adaptable_instantiation(instance):
    assert isinstance(instance, Adaptable)

@given(instance=df_Network_strategy)
@settings(max_examples=50)
def test_df_network_instantiation(instance):
    assert isinstance(instance, df_Network)



@given(instance=df_Network_strategy)
def test_df_network_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=df_Network_strategy)
def test_df_network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df_Type_strategy)
@settings(max_examples=50)
def test_df_type_instantiation(instance):
    assert isinstance(instance, df_Type)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=df_Actor_strategy)
@settings(max_examples=50)
def test_df_actor_instantiation(instance):
    assert isinstance(instance, df_Actor)



@given(instance=df_Actor_strategy)
def test_df_actor_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=df_Actor_strategy)
def test_df_actor_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=df_Actor_strategy)
def test_df_actor_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original



@given(instance=df_Actor_strategy)
def test_df_actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df_State_strategy)
@settings(max_examples=50)
def test_df_state_instantiation(instance):
    assert isinstance(instance, df_State)

@given(instance=df_Instance_strategy)
@settings(max_examples=50)
def test_df_instance_instantiation(instance):
    assert isinstance(instance, df_Instance)



@given(instance=df_Instance_strategy)
def test_df_instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=df_Port_strategy)
@settings(max_examples=50)
def test_df_port_instantiation(instance):
    assert isinstance(instance, df_Port)



@given(instance=df_Port_strategy)
def test_df_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=df_Port_strategy)
def test_df_port_numTokensConsumed_setter(instance):
    original = instance.numTokensConsumed
    instance.numTokensConsumed = original
    assert instance.numTokensConsumed == original



@given(instance=df_Port_strategy)
def test_df_port_numTokensProduced_setter(instance):
    original = instance.numTokensProduced
    instance.numTokensProduced = original
    assert instance.numTokensProduced == original

@given(instance=df_Procedure_strategy)
@settings(max_examples=50)
def test_df_procedure_instantiation(instance):
    assert isinstance(instance, df_Procedure)

@given(instance=df_Var_strategy)
@settings(max_examples=50)
def test_df_var_instantiation(instance):
    assert isinstance(instance, df_Var)

@given(instance=Attributable_strategy)
@settings(max_examples=50)
def test_attributable_instantiation(instance):
    assert isinstance(instance, Attributable)

@given(instance=df_Action_strategy)
@settings(max_examples=50)
def test_df_action_instantiation(instance):
    assert isinstance(instance, df_Action)

@given(instance=df_Entity_strategy)
@settings(max_examples=50)
def test_df_entity_instantiation(instance):
    assert isinstance(instance, df_Entity)



@given(instance=df_Entity_strategy)
def test_df_entity_outgoingPortMap_setter(instance):
    original = instance.outgoingPortMap
    instance.outgoingPortMap = original
    assert instance.outgoingPortMap == original



@given(instance=df_Entity_strategy)
def test_df_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=df_Entity_strategy)
def test_df_entity_incomingPortMap_setter(instance):
    original = instance.incomingPortMap
    instance.incomingPortMap = original
    assert instance.incomingPortMap == original

@given(instance=df_Unit_strategy)
@settings(max_examples=50)
def test_df_unit_instantiation(instance):
    assert isinstance(instance, df_Unit)



@given(instance=df_Unit_strategy)
def test_df_unit_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original



@given(instance=df_Unit_strategy)
def test_df_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=df_Unit_strategy)
def test_df_unit_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original
