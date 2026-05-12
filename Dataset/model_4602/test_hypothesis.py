import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Actor,
    adfg_AperiodicActor,
    Connection,
    adfg_LossyChannel,
    adfg_Channel,
    adfg_PeriodicActor,
    Port,
    adfg_InputPort,
    adfg_OutputPort,
    adfg_AffineRelation,
    adfg_Actor,
    adfg_Port,
    adfg_Connection,
    adfg_GraphConnection,
    adfg_Graph,
    adfg_Application,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())



def test_adfg_aperiodicactor_is_not_abstract():
    assert not inspect.isabstract(adfg_AperiodicActor)


def test_adfg_aperiodicactor_constructor_exists():
    assert callable(adfg_AperiodicActor.__init__)


def test_adfg_aperiodicactor_constructor_args():
    sig = inspect.signature(adfg_AperiodicActor.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "replenishmentPeriod" in params, "Missing parameter 'replenishmentPeriod'"

def test_adfg_aperiodicactor_has_capacity():
    assert hasattr(adfg_AperiodicActor, "capacity")
    descriptor = None
    for klass in adfg_AperiodicActor.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_adfg_aperiodicactor_has_replenishmentPeriod():
    assert hasattr(adfg_AperiodicActor, "replenishmentPeriod")
    descriptor = None
    for klass in adfg_AperiodicActor.__mro__:
        if "replenishmentPeriod" in klass.__dict__:
            descriptor = klass.__dict__["replenishmentPeriod"]
            break
    assert isinstance(descriptor, property)



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_adfg_lossychannel_is_not_abstract():
    assert not inspect.isabstract(adfg_LossyChannel)


def test_adfg_lossychannel_constructor_exists():
    assert callable(adfg_LossyChannel.__init__)


def test_adfg_lossychannel_constructor_args():
    sig = inspect.signature(adfg_LossyChannel.__init__)
    params = list(sig.parameters.keys())



def test_adfg_channel_is_not_abstract():
    assert not inspect.isabstract(adfg_Channel)


def test_adfg_channel_constructor_exists():
    assert callable(adfg_Channel.__init__)


def test_adfg_channel_constructor_args():
    sig = inspect.signature(adfg_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"

def test_adfg_channel_has_initial():
    assert hasattr(adfg_Channel, "initial")
    descriptor = None
    for klass in adfg_Channel.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_adfg_periodicactor_is_not_abstract():
    assert not inspect.isabstract(adfg_PeriodicActor)


def test_adfg_periodicactor_constructor_exists():
    assert callable(adfg_PeriodicActor.__init__)


def test_adfg_periodicactor_constructor_args():
    sig = inspect.signature(adfg_PeriodicActor.__init__)
    params = list(sig.parameters.keys())
    assert "periodLowerBound" in params, "Missing parameter 'periodLowerBound'"
    assert "deadline" in params, "Missing parameter 'deadline'"
    assert "phase" in params, "Missing parameter 'phase'"
    assert "periodUpperBound" in params, "Missing parameter 'periodUpperBound'"
    assert "wcet" in params, "Missing parameter 'wcet'"
    assert "period" in params, "Missing parameter 'period'"

def test_adfg_periodicactor_has_periodLowerBound():
    assert hasattr(adfg_PeriodicActor, "periodLowerBound")
    descriptor = None
    for klass in adfg_PeriodicActor.__mro__:
        if "periodLowerBound" in klass.__dict__:
            descriptor = klass.__dict__["periodLowerBound"]
            break
    assert isinstance(descriptor, property)

def test_adfg_periodicactor_has_deadline():
    assert hasattr(adfg_PeriodicActor, "deadline")
    descriptor = None
    for klass in adfg_PeriodicActor.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)

def test_adfg_periodicactor_has_phase():
    assert hasattr(adfg_PeriodicActor, "phase")
    descriptor = None
    for klass in adfg_PeriodicActor.__mro__:
        if "phase" in klass.__dict__:
            descriptor = klass.__dict__["phase"]
            break
    assert isinstance(descriptor, property)

def test_adfg_periodicactor_has_periodUpperBound():
    assert hasattr(adfg_PeriodicActor, "periodUpperBound")
    descriptor = None
    for klass in adfg_PeriodicActor.__mro__:
        if "periodUpperBound" in klass.__dict__:
            descriptor = klass.__dict__["periodUpperBound"]
            break
    assert isinstance(descriptor, property)

def test_adfg_periodicactor_has_wcet():
    assert hasattr(adfg_PeriodicActor, "wcet")
    descriptor = None
    for klass in adfg_PeriodicActor.__mro__:
        if "wcet" in klass.__dict__:
            descriptor = klass.__dict__["wcet"]
            break
    assert isinstance(descriptor, property)

def test_adfg_periodicactor_has_period():
    assert hasattr(adfg_PeriodicActor, "period")
    descriptor = None
    for klass in adfg_PeriodicActor.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_adfg_inputport_is_not_abstract():
    assert not inspect.isabstract(adfg_InputPort)


def test_adfg_inputport_constructor_exists():
    assert callable(adfg_InputPort.__init__)


def test_adfg_inputport_constructor_args():
    sig = inspect.signature(adfg_InputPort.__init__)
    params = list(sig.parameters.keys())



def test_adfg_outputport_is_not_abstract():
    assert not inspect.isabstract(adfg_OutputPort)


def test_adfg_outputport_constructor_exists():
    assert callable(adfg_OutputPort.__init__)


def test_adfg_outputport_constructor_args():
    sig = inspect.signature(adfg_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_adfg_affinerelation_is_not_abstract():
    assert not inspect.isabstract(adfg_AffineRelation)


def test_adfg_affinerelation_constructor_exists():
    assert callable(adfg_AffineRelation.__init__)


def test_adfg_affinerelation_constructor_args():
    sig = inspect.signature(adfg_AffineRelation.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"
    assert "phi" in params, "Missing parameter 'phi'"
    assert "n" in params, "Missing parameter 'n'"

def test_adfg_affinerelation_has_d():
    assert hasattr(adfg_AffineRelation, "d")
    descriptor = None
    for klass in adfg_AffineRelation.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_adfg_affinerelation_has_phi():
    assert hasattr(adfg_AffineRelation, "phi")
    descriptor = None
    for klass in adfg_AffineRelation.__mro__:
        if "phi" in klass.__dict__:
            descriptor = klass.__dict__["phi"]
            break
    assert isinstance(descriptor, property)

def test_adfg_affinerelation_has_n():
    assert hasattr(adfg_AffineRelation, "n")
    descriptor = None
    for klass in adfg_AffineRelation.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_adfg_actor_is_not_abstract():
    assert not inspect.isabstract(adfg_Actor)


def test_adfg_actor_constructor_exists():
    assert callable(adfg_Actor.__init__)


def test_adfg_actor_constructor_args():
    sig = inspect.signature(adfg_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"
    assert "nbPorts" in params, "Missing parameter 'nbPorts'"
    assert "procNumber" in params, "Missing parameter 'procNumber'"

def test_adfg_actor_has_priority():
    assert hasattr(adfg_Actor, "priority")
    descriptor = None
    for klass in adfg_Actor.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_adfg_actor_has_name():
    assert hasattr(adfg_Actor, "name")
    descriptor = None
    for klass in adfg_Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg_actor_has_sourceCode():
    assert hasattr(adfg_Actor, "sourceCode")
    descriptor = None
    for klass in adfg_Actor.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)

def test_adfg_actor_has_nbPorts():
    assert hasattr(adfg_Actor, "nbPorts")
    descriptor = None
    for klass in adfg_Actor.__mro__:
        if "nbPorts" in klass.__dict__:
            descriptor = klass.__dict__["nbPorts"]
            break
    assert isinstance(descriptor, property)

def test_adfg_actor_has_procNumber():
    assert hasattr(adfg_Actor, "procNumber")
    descriptor = None
    for klass in adfg_Actor.__mro__:
        if "procNumber" in klass.__dict__:
            descriptor = klass.__dict__["procNumber"]
            break
    assert isinstance(descriptor, property)



def test_adfg_port_is_not_abstract():
    assert not inspect.isabstract(adfg_Port)


def test_adfg_port_constructor_exists():
    assert callable(adfg_Port.__init__)


def test_adfg_port_constructor_args():
    sig = inspect.signature(adfg_Port.__init__)
    params = list(sig.parameters.keys())
    assert "sequence" in params, "Missing parameter 'sequence'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_adfg_port_has_sequence():
    assert hasattr(adfg_Port, "sequence")
    descriptor = None
    for klass in adfg_Port.__mro__:
        if "sequence" in klass.__dict__:
            descriptor = klass.__dict__["sequence"]
            break
    assert isinstance(descriptor, property)

def test_adfg_port_has_type():
    assert hasattr(adfg_Port, "type")
    descriptor = None
    for klass in adfg_Port.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_adfg_port_has_name():
    assert hasattr(adfg_Port, "name")
    descriptor = None
    for klass in adfg_Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adfg_connection_is_not_abstract():
    assert not inspect.isabstract(adfg_Connection)


def test_adfg_connection_constructor_exists():
    assert callable(adfg_Connection.__init__)


def test_adfg_connection_constructor_args():
    sig = inspect.signature(adfg_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "size" in params, "Missing parameter 'size'"

def test_adfg_connection_has_id():
    assert hasattr(adfg_Connection, "id")
    descriptor = None
    for klass in adfg_Connection.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_adfg_connection_has_size():
    assert hasattr(adfg_Connection, "size")
    descriptor = None
    for klass in adfg_Connection.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_adfg_graphconnection_is_not_abstract():
    assert not inspect.isabstract(adfg_GraphConnection)


def test_adfg_graphconnection_constructor_exists():
    assert callable(adfg_GraphConnection.__init__)


def test_adfg_graphconnection_constructor_args():
    sig = inspect.signature(adfg_GraphConnection.__init__)
    params = list(sig.parameters.keys())



def test_adfg_graph_is_not_abstract():
    assert not inspect.isabstract(adfg_Graph)


def test_adfg_graph_constructor_exists():
    assert callable(adfg_Graph.__init__)


def test_adfg_graph_constructor_args():
    sig = inspect.signature(adfg_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nbBuffers" in params, "Missing parameter 'nbBuffers'"
    assert "id" in params, "Missing parameter 'id'"
    assert "processorUtilization" in params, "Missing parameter 'processorUtilization'"
    assert "bufferingRequirements" in params, "Missing parameter 'bufferingRequirements'"
    assert "nbActors" in params, "Missing parameter 'nbActors'"

def test_adfg_graph_has_sourceCode():
    assert hasattr(adfg_Graph, "sourceCode")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)

def test_adfg_graph_has_name():
    assert hasattr(adfg_Graph, "name")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg_graph_has_nbBuffers():
    assert hasattr(adfg_Graph, "nbBuffers")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "nbBuffers" in klass.__dict__:
            descriptor = klass.__dict__["nbBuffers"]
            break
    assert isinstance(descriptor, property)

def test_adfg_graph_has_id():
    assert hasattr(adfg_Graph, "id")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_adfg_graph_has_processorUtilization():
    assert hasattr(adfg_Graph, "processorUtilization")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "processorUtilization" in klass.__dict__:
            descriptor = klass.__dict__["processorUtilization"]
            break
    assert isinstance(descriptor, property)

def test_adfg_graph_has_bufferingRequirements():
    assert hasattr(adfg_Graph, "bufferingRequirements")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "bufferingRequirements" in klass.__dict__:
            descriptor = klass.__dict__["bufferingRequirements"]
            break
    assert isinstance(descriptor, property)

def test_adfg_graph_has_nbActors():
    assert hasattr(adfg_Graph, "nbActors")
    descriptor = None
    for klass in adfg_Graph.__mro__:
        if "nbActors" in klass.__dict__:
            descriptor = klass.__dict__["nbActors"]
            break
    assert isinstance(descriptor, property)



def test_adfg_application_is_not_abstract():
    assert not inspect.isabstract(adfg_Application)


def test_adfg_application_constructor_exists():
    assert callable(adfg_Application.__init__)


def test_adfg_application_constructor_args():
    sig = inspect.signature(adfg_Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"
    assert "nbProcessors" in params, "Missing parameter 'nbProcessors'"
    assert "dynamicChecking" in params, "Missing parameter 'dynamicChecking'"
    assert "nbGraphs" in params, "Missing parameter 'nbGraphs'"
    assert "schedulingAlgorithm" in params, "Missing parameter 'schedulingAlgorithm'"

def test_adfg_application_has_name():
    assert hasattr(adfg_Application, "name")
    descriptor = None
    for klass in adfg_Application.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg_application_has_sourceCode():
    assert hasattr(adfg_Application, "sourceCode")
    descriptor = None
    for klass in adfg_Application.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)

def test_adfg_application_has_nbProcessors():
    assert hasattr(adfg_Application, "nbProcessors")
    descriptor = None
    for klass in adfg_Application.__mro__:
        if "nbProcessors" in klass.__dict__:
            descriptor = klass.__dict__["nbProcessors"]
            break
    assert isinstance(descriptor, property)

def test_adfg_application_has_dynamicChecking():
    assert hasattr(adfg_Application, "dynamicChecking")
    descriptor = None
    for klass in adfg_Application.__mro__:
        if "dynamicChecking" in klass.__dict__:
            descriptor = klass.__dict__["dynamicChecking"]
            break
    assert isinstance(descriptor, property)

def test_adfg_application_has_nbGraphs():
    assert hasattr(adfg_Application, "nbGraphs")
    descriptor = None
    for klass in adfg_Application.__mro__:
        if "nbGraphs" in klass.__dict__:
            descriptor = klass.__dict__["nbGraphs"]
            break
    assert isinstance(descriptor, property)

def test_adfg_application_has_schedulingAlgorithm():
    assert hasattr(adfg_Application, "schedulingAlgorithm")
    descriptor = None
    for klass in adfg_Application.__mro__:
        if "schedulingAlgorithm" in klass.__dict__:
            descriptor = klass.__dict__["schedulingAlgorithm"]
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
Actor_strategy = st.builds(
    Actor,
)
adfg_AperiodicActor_strategy = st.builds(
    adfg_AperiodicActor,
    capacity=
        safe_text,
    replenishmentPeriod=
        safe_text
)
Connection_strategy = st.builds(
    Connection,
)
adfg_LossyChannel_strategy = st.builds(
    adfg_LossyChannel,
)
adfg_Channel_strategy = st.builds(
    adfg_Channel,
    initial=
        st.integers()
)
adfg_PeriodicActor_strategy = st.builds(
    adfg_PeriodicActor,
    periodLowerBound=
        safe_text,
    deadline=
        safe_text,
    phase=
        safe_text,
    periodUpperBound=
        safe_text,
    wcet=
        safe_text,
    period=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
adfg_InputPort_strategy = st.builds(
    adfg_InputPort,
)
adfg_OutputPort_strategy = st.builds(
    adfg_OutputPort,
)
adfg_AffineRelation_strategy = st.builds(
    adfg_AffineRelation,
    d=
        st.integers(),
    phi=
        st.integers(),
    n=
        st.integers()
)
adfg_Actor_strategy = st.builds(
    adfg_Actor,
    priority=
        st.integers(),
    name=
        safe_text,
    sourceCode=
        safe_text,
    nbPorts=
        st.integers(),
    procNumber=
        st.integers()
)
adfg_Port_strategy = st.builds(
    adfg_Port,
    sequence=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
adfg_Connection_strategy = st.builds(
    adfg_Connection,
    id=
        st.integers(),
    size=
        st.integers()
)
adfg_GraphConnection_strategy = st.builds(
    adfg_GraphConnection,
)
adfg_Graph_strategy = st.builds(
    adfg_Graph,
    sourceCode=
        safe_text,
    name=
        safe_text,
    nbBuffers=
        st.integers(),
    id=
        st.integers(),
    processorUtilization=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    bufferingRequirements=
        st.integers(),
    nbActors=
        st.integers()
)
adfg_Application_strategy = st.builds(
    adfg_Application,
    name=
        safe_text,
    sourceCode=
        safe_text,
    nbProcessors=
        st.integers(),
    dynamicChecking=
        st.booleans(),
    nbGraphs=
        st.integers(),
    schedulingAlgorithm=
        safe_text
)

@given(instance=Actor_strategy)
@settings(max_examples=50)
def test_actor_instantiation(instance):
    assert isinstance(instance, Actor)

@given(instance=adfg_AperiodicActor_strategy)
@settings(max_examples=50)
def test_adfg_aperiodicactor_instantiation(instance):
    assert isinstance(instance, adfg_AperiodicActor)



@given(instance=adfg_AperiodicActor_strategy)
def test_adfg_aperiodicactor_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=adfg_AperiodicActor_strategy)
def test_adfg_aperiodicactor_replenishmentPeriod_setter(instance):
    original = instance.replenishmentPeriod
    instance.replenishmentPeriod = original
    assert instance.replenishmentPeriod == original

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=adfg_LossyChannel_strategy)
@settings(max_examples=50)
def test_adfg_lossychannel_instantiation(instance):
    assert isinstance(instance, adfg_LossyChannel)

@given(instance=adfg_Channel_strategy)
@settings(max_examples=50)
def test_adfg_channel_instantiation(instance):
    assert isinstance(instance, adfg_Channel)



@given(instance=adfg_Channel_strategy)
def test_adfg_channel_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=adfg_PeriodicActor_strategy)
@settings(max_examples=50)
def test_adfg_periodicactor_instantiation(instance):
    assert isinstance(instance, adfg_PeriodicActor)



@given(instance=adfg_PeriodicActor_strategy)
def test_adfg_periodicactor_periodLowerBound_setter(instance):
    original = instance.periodLowerBound
    instance.periodLowerBound = original
    assert instance.periodLowerBound == original



@given(instance=adfg_PeriodicActor_strategy)
def test_adfg_periodicactor_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original



@given(instance=adfg_PeriodicActor_strategy)
def test_adfg_periodicactor_phase_setter(instance):
    original = instance.phase
    instance.phase = original
    assert instance.phase == original



@given(instance=adfg_PeriodicActor_strategy)
def test_adfg_periodicactor_periodUpperBound_setter(instance):
    original = instance.periodUpperBound
    instance.periodUpperBound = original
    assert instance.periodUpperBound == original



@given(instance=adfg_PeriodicActor_strategy)
def test_adfg_periodicactor_wcet_setter(instance):
    original = instance.wcet
    instance.wcet = original
    assert instance.wcet == original



@given(instance=adfg_PeriodicActor_strategy)
def test_adfg_periodicactor_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=adfg_InputPort_strategy)
@settings(max_examples=50)
def test_adfg_inputport_instantiation(instance):
    assert isinstance(instance, adfg_InputPort)

@given(instance=adfg_OutputPort_strategy)
@settings(max_examples=50)
def test_adfg_outputport_instantiation(instance):
    assert isinstance(instance, adfg_OutputPort)

@given(instance=adfg_AffineRelation_strategy)
@settings(max_examples=50)
def test_adfg_affinerelation_instantiation(instance):
    assert isinstance(instance, adfg_AffineRelation)



@given(instance=adfg_AffineRelation_strategy)
def test_adfg_affinerelation_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=adfg_AffineRelation_strategy)
def test_adfg_affinerelation_phi_setter(instance):
    original = instance.phi
    instance.phi = original
    assert instance.phi == original



@given(instance=adfg_AffineRelation_strategy)
def test_adfg_affinerelation_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=adfg_Actor_strategy)
@settings(max_examples=50)
def test_adfg_actor_instantiation(instance):
    assert isinstance(instance, adfg_Actor)



@given(instance=adfg_Actor_strategy)
def test_adfg_actor_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=adfg_Actor_strategy)
def test_adfg_actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adfg_Actor_strategy)
def test_adfg_actor_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original



@given(instance=adfg_Actor_strategy)
def test_adfg_actor_nbPorts_setter(instance):
    original = instance.nbPorts
    instance.nbPorts = original
    assert instance.nbPorts == original



@given(instance=adfg_Actor_strategy)
def test_adfg_actor_procNumber_setter(instance):
    original = instance.procNumber
    instance.procNumber = original
    assert instance.procNumber == original

@given(instance=adfg_Port_strategy)
@settings(max_examples=50)
def test_adfg_port_instantiation(instance):
    assert isinstance(instance, adfg_Port)



@given(instance=adfg_Port_strategy)
def test_adfg_port_sequence_setter(instance):
    original = instance.sequence
    instance.sequence = original
    assert instance.sequence == original



@given(instance=adfg_Port_strategy)
def test_adfg_port_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=adfg_Port_strategy)
def test_adfg_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adfg_Connection_strategy)
@settings(max_examples=50)
def test_adfg_connection_instantiation(instance):
    assert isinstance(instance, adfg_Connection)



@given(instance=adfg_Connection_strategy)
def test_adfg_connection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=adfg_Connection_strategy)
def test_adfg_connection_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=adfg_GraphConnection_strategy)
@settings(max_examples=50)
def test_adfg_graphconnection_instantiation(instance):
    assert isinstance(instance, adfg_GraphConnection)

@given(instance=adfg_Graph_strategy)
@settings(max_examples=50)
def test_adfg_graph_instantiation(instance):
    assert isinstance(instance, adfg_Graph)



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_nbBuffers_setter(instance):
    original = instance.nbBuffers
    instance.nbBuffers = original
    assert instance.nbBuffers == original



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_processorUtilization_setter(instance):
    original = instance.processorUtilization
    instance.processorUtilization = original
    assert instance.processorUtilization == original



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_bufferingRequirements_setter(instance):
    original = instance.bufferingRequirements
    instance.bufferingRequirements = original
    assert instance.bufferingRequirements == original



@given(instance=adfg_Graph_strategy)
def test_adfg_graph_nbActors_setter(instance):
    original = instance.nbActors
    instance.nbActors = original
    assert instance.nbActors == original

@given(instance=adfg_Application_strategy)
@settings(max_examples=50)
def test_adfg_application_instantiation(instance):
    assert isinstance(instance, adfg_Application)



@given(instance=adfg_Application_strategy)
def test_adfg_application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adfg_Application_strategy)
def test_adfg_application_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original



@given(instance=adfg_Application_strategy)
def test_adfg_application_nbProcessors_setter(instance):
    original = instance.nbProcessors
    instance.nbProcessors = original
    assert instance.nbProcessors == original



@given(instance=adfg_Application_strategy)
def test_adfg_application_dynamicChecking_setter(instance):
    original = instance.dynamicChecking
    instance.dynamicChecking = original
    assert instance.dynamicChecking == original



@given(instance=adfg_Application_strategy)
def test_adfg_application_nbGraphs_setter(instance):
    original = instance.nbGraphs
    instance.nbGraphs = original
    assert instance.nbGraphs == original



@given(instance=adfg_Application_strategy)
def test_adfg_application_schedulingAlgorithm_setter(instance):
    original = instance.schedulingAlgorithm
    instance.schedulingAlgorithm = original
    assert instance.schedulingAlgorithm == original
