import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Actor,
    adfg::AperiodicActor,
    Connection,
    adfg::LossyChannel,
    adfg::Channel,
    adfg::PeriodicActor,
    Port,
    adfg::InputPort,
    adfg::OutputPort,
    adfg::AffineRelation,
    adfg::Actor,
    adfg::Port,
    adfg::Connection,
    adfg::GraphConnection,
    adfg::Graph,
    adfg::Application,
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



def test_adfg::aperiodicactor_is_not_abstract():
    assert not inspect.isabstract(adfg::AperiodicActor)


def test_adfg::aperiodicactor_constructor_exists():
    assert callable(adfg::AperiodicActor.__init__)


def test_adfg::aperiodicactor_constructor_args():
    sig = inspect.signature(adfg::AperiodicActor.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "replenishmentPeriod" in params, "Missing parameter 'replenishmentPeriod'"

def test_adfg::aperiodicactor_has_capacity():
    assert hasattr(adfg::AperiodicActor, "capacity")
    descriptor = None
    for klass in adfg::AperiodicActor.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_adfg::aperiodicactor_has_replenishmentPeriod():
    assert hasattr(adfg::AperiodicActor, "replenishmentPeriod")
    descriptor = None
    for klass in adfg::AperiodicActor.__mro__:
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



def test_adfg::lossychannel_is_not_abstract():
    assert not inspect.isabstract(adfg::LossyChannel)


def test_adfg::lossychannel_constructor_exists():
    assert callable(adfg::LossyChannel.__init__)


def test_adfg::lossychannel_constructor_args():
    sig = inspect.signature(adfg::LossyChannel.__init__)
    params = list(sig.parameters.keys())



def test_adfg::channel_is_not_abstract():
    assert not inspect.isabstract(adfg::Channel)


def test_adfg::channel_constructor_exists():
    assert callable(adfg::Channel.__init__)


def test_adfg::channel_constructor_args():
    sig = inspect.signature(adfg::Channel.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"

def test_adfg::channel_has_initial():
    assert hasattr(adfg::Channel, "initial")
    descriptor = None
    for klass in adfg::Channel.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_adfg::periodicactor_is_not_abstract():
    assert not inspect.isabstract(adfg::PeriodicActor)


def test_adfg::periodicactor_constructor_exists():
    assert callable(adfg::PeriodicActor.__init__)


def test_adfg::periodicactor_constructor_args():
    sig = inspect.signature(adfg::PeriodicActor.__init__)
    params = list(sig.parameters.keys())
    assert "periodLowerBound" in params, "Missing parameter 'periodLowerBound'"
    assert "periodUpperBound" in params, "Missing parameter 'periodUpperBound'"
    assert "period" in params, "Missing parameter 'period'"
    assert "phase" in params, "Missing parameter 'phase'"
    assert "deadline" in params, "Missing parameter 'deadline'"
    assert "wcet" in params, "Missing parameter 'wcet'"

def test_adfg::periodicactor_has_periodLowerBound():
    assert hasattr(adfg::PeriodicActor, "periodLowerBound")
    descriptor = None
    for klass in adfg::PeriodicActor.__mro__:
        if "periodLowerBound" in klass.__dict__:
            descriptor = klass.__dict__["periodLowerBound"]
            break
    assert isinstance(descriptor, property)

def test_adfg::periodicactor_has_periodUpperBound():
    assert hasattr(adfg::PeriodicActor, "periodUpperBound")
    descriptor = None
    for klass in adfg::PeriodicActor.__mro__:
        if "periodUpperBound" in klass.__dict__:
            descriptor = klass.__dict__["periodUpperBound"]
            break
    assert isinstance(descriptor, property)

def test_adfg::periodicactor_has_period():
    assert hasattr(adfg::PeriodicActor, "period")
    descriptor = None
    for klass in adfg::PeriodicActor.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)

def test_adfg::periodicactor_has_phase():
    assert hasattr(adfg::PeriodicActor, "phase")
    descriptor = None
    for klass in adfg::PeriodicActor.__mro__:
        if "phase" in klass.__dict__:
            descriptor = klass.__dict__["phase"]
            break
    assert isinstance(descriptor, property)

def test_adfg::periodicactor_has_deadline():
    assert hasattr(adfg::PeriodicActor, "deadline")
    descriptor = None
    for klass in adfg::PeriodicActor.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)

def test_adfg::periodicactor_has_wcet():
    assert hasattr(adfg::PeriodicActor, "wcet")
    descriptor = None
    for klass in adfg::PeriodicActor.__mro__:
        if "wcet" in klass.__dict__:
            descriptor = klass.__dict__["wcet"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_adfg::inputport_is_not_abstract():
    assert not inspect.isabstract(adfg::InputPort)


def test_adfg::inputport_constructor_exists():
    assert callable(adfg::InputPort.__init__)


def test_adfg::inputport_constructor_args():
    sig = inspect.signature(adfg::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_adfg::outputport_is_not_abstract():
    assert not inspect.isabstract(adfg::OutputPort)


def test_adfg::outputport_constructor_exists():
    assert callable(adfg::OutputPort.__init__)


def test_adfg::outputport_constructor_args():
    sig = inspect.signature(adfg::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_adfg::affinerelation_is_not_abstract():
    assert not inspect.isabstract(adfg::AffineRelation)


def test_adfg::affinerelation_constructor_exists():
    assert callable(adfg::AffineRelation.__init__)


def test_adfg::affinerelation_constructor_args():
    sig = inspect.signature(adfg::AffineRelation.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"
    assert "n" in params, "Missing parameter 'n'"
    assert "phi" in params, "Missing parameter 'phi'"

def test_adfg::affinerelation_has_d():
    assert hasattr(adfg::AffineRelation, "d")
    descriptor = None
    for klass in adfg::AffineRelation.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_adfg::affinerelation_has_n():
    assert hasattr(adfg::AffineRelation, "n")
    descriptor = None
    for klass in adfg::AffineRelation.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_adfg::affinerelation_has_phi():
    assert hasattr(adfg::AffineRelation, "phi")
    descriptor = None
    for klass in adfg::AffineRelation.__mro__:
        if "phi" in klass.__dict__:
            descriptor = klass.__dict__["phi"]
            break
    assert isinstance(descriptor, property)



def test_adfg::actor_is_not_abstract():
    assert not inspect.isabstract(adfg::Actor)


def test_adfg::actor_constructor_exists():
    assert callable(adfg::Actor.__init__)


def test_adfg::actor_constructor_args():
    sig = inspect.signature(adfg::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"
    assert "procNumber" in params, "Missing parameter 'procNumber'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nbPorts" in params, "Missing parameter 'nbPorts'"

def test_adfg::actor_has_sourceCode():
    assert hasattr(adfg::Actor, "sourceCode")
    descriptor = None
    for klass in adfg::Actor.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)

def test_adfg::actor_has_procNumber():
    assert hasattr(adfg::Actor, "procNumber")
    descriptor = None
    for klass in adfg::Actor.__mro__:
        if "procNumber" in klass.__dict__:
            descriptor = klass.__dict__["procNumber"]
            break
    assert isinstance(descriptor, property)

def test_adfg::actor_has_priority():
    assert hasattr(adfg::Actor, "priority")
    descriptor = None
    for klass in adfg::Actor.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_adfg::actor_has_name():
    assert hasattr(adfg::Actor, "name")
    descriptor = None
    for klass in adfg::Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg::actor_has_nbPorts():
    assert hasattr(adfg::Actor, "nbPorts")
    descriptor = None
    for klass in adfg::Actor.__mro__:
        if "nbPorts" in klass.__dict__:
            descriptor = klass.__dict__["nbPorts"]
            break
    assert isinstance(descriptor, property)



def test_adfg::port_is_not_abstract():
    assert not inspect.isabstract(adfg::Port)


def test_adfg::port_constructor_exists():
    assert callable(adfg::Port.__init__)


def test_adfg::port_constructor_args():
    sig = inspect.signature(adfg::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "sequence" in params, "Missing parameter 'sequence'"

def test_adfg::port_has_name():
    assert hasattr(adfg::Port, "name")
    descriptor = None
    for klass in adfg::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg::port_has_type():
    assert hasattr(adfg::Port, "type")
    descriptor = None
    for klass in adfg::Port.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_adfg::port_has_sequence():
    assert hasattr(adfg::Port, "sequence")
    descriptor = None
    for klass in adfg::Port.__mro__:
        if "sequence" in klass.__dict__:
            descriptor = klass.__dict__["sequence"]
            break
    assert isinstance(descriptor, property)



def test_adfg::connection_is_not_abstract():
    assert not inspect.isabstract(adfg::Connection)


def test_adfg::connection_constructor_exists():
    assert callable(adfg::Connection.__init__)


def test_adfg::connection_constructor_args():
    sig = inspect.signature(adfg::Connection.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "id" in params, "Missing parameter 'id'"

def test_adfg::connection_has_size():
    assert hasattr(adfg::Connection, "size")
    descriptor = None
    for klass in adfg::Connection.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_adfg::connection_has_id():
    assert hasattr(adfg::Connection, "id")
    descriptor = None
    for klass in adfg::Connection.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_adfg::graphconnection_is_not_abstract():
    assert not inspect.isabstract(adfg::GraphConnection)


def test_adfg::graphconnection_constructor_exists():
    assert callable(adfg::GraphConnection.__init__)


def test_adfg::graphconnection_constructor_args():
    sig = inspect.signature(adfg::GraphConnection.__init__)
    params = list(sig.parameters.keys())



def test_adfg::graph_is_not_abstract():
    assert not inspect.isabstract(adfg::Graph)


def test_adfg::graph_constructor_exists():
    assert callable(adfg::Graph.__init__)


def test_adfg::graph_constructor_args():
    sig = inspect.signature(adfg::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "bufferingRequirements" in params, "Missing parameter 'bufferingRequirements'"
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"
    assert "nbBuffers" in params, "Missing parameter 'nbBuffers'"
    assert "nbActors" in params, "Missing parameter 'nbActors'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "processorUtilization" in params, "Missing parameter 'processorUtilization'"

def test_adfg::graph_has_bufferingRequirements():
    assert hasattr(adfg::Graph, "bufferingRequirements")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "bufferingRequirements" in klass.__dict__:
            descriptor = klass.__dict__["bufferingRequirements"]
            break
    assert isinstance(descriptor, property)

def test_adfg::graph_has_sourceCode():
    assert hasattr(adfg::Graph, "sourceCode")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)

def test_adfg::graph_has_nbBuffers():
    assert hasattr(adfg::Graph, "nbBuffers")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "nbBuffers" in klass.__dict__:
            descriptor = klass.__dict__["nbBuffers"]
            break
    assert isinstance(descriptor, property)

def test_adfg::graph_has_nbActors():
    assert hasattr(adfg::Graph, "nbActors")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "nbActors" in klass.__dict__:
            descriptor = klass.__dict__["nbActors"]
            break
    assert isinstance(descriptor, property)

def test_adfg::graph_has_name():
    assert hasattr(adfg::Graph, "name")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg::graph_has_id():
    assert hasattr(adfg::Graph, "id")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_adfg::graph_has_processorUtilization():
    assert hasattr(adfg::Graph, "processorUtilization")
    descriptor = None
    for klass in adfg::Graph.__mro__:
        if "processorUtilization" in klass.__dict__:
            descriptor = klass.__dict__["processorUtilization"]
            break
    assert isinstance(descriptor, property)



def test_adfg::application_is_not_abstract():
    assert not inspect.isabstract(adfg::Application)


def test_adfg::application_constructor_exists():
    assert callable(adfg::Application.__init__)


def test_adfg::application_constructor_args():
    sig = inspect.signature(adfg::Application.__init__)
    params = list(sig.parameters.keys())
    assert "dynamicChecking" in params, "Missing parameter 'dynamicChecking'"
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"
    assert "name" in params, "Missing parameter 'name'"
    assert "schedulingAlgorithm" in params, "Missing parameter 'schedulingAlgorithm'"
    assert "nbProcessors" in params, "Missing parameter 'nbProcessors'"
    assert "nbGraphs" in params, "Missing parameter 'nbGraphs'"

def test_adfg::application_has_dynamicChecking():
    assert hasattr(adfg::Application, "dynamicChecking")
    descriptor = None
    for klass in adfg::Application.__mro__:
        if "dynamicChecking" in klass.__dict__:
            descriptor = klass.__dict__["dynamicChecking"]
            break
    assert isinstance(descriptor, property)

def test_adfg::application_has_sourceCode():
    assert hasattr(adfg::Application, "sourceCode")
    descriptor = None
    for klass in adfg::Application.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)

def test_adfg::application_has_name():
    assert hasattr(adfg::Application, "name")
    descriptor = None
    for klass in adfg::Application.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adfg::application_has_schedulingAlgorithm():
    assert hasattr(adfg::Application, "schedulingAlgorithm")
    descriptor = None
    for klass in adfg::Application.__mro__:
        if "schedulingAlgorithm" in klass.__dict__:
            descriptor = klass.__dict__["schedulingAlgorithm"]
            break
    assert isinstance(descriptor, property)

def test_adfg::application_has_nbProcessors():
    assert hasattr(adfg::Application, "nbProcessors")
    descriptor = None
    for klass in adfg::Application.__mro__:
        if "nbProcessors" in klass.__dict__:
            descriptor = klass.__dict__["nbProcessors"]
            break
    assert isinstance(descriptor, property)

def test_adfg::application_has_nbGraphs():
    assert hasattr(adfg::Application, "nbGraphs")
    descriptor = None
    for klass in adfg::Application.__mro__:
        if "nbGraphs" in klass.__dict__:
            descriptor = klass.__dict__["nbGraphs"]
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
adfg::AperiodicActor_strategy = st.builds(
    adfg::AperiodicActor,
    capacity=
        safe_text,
    replenishmentPeriod=
        safe_text
)
Connection_strategy = st.builds(
    Connection,
)
adfg::LossyChannel_strategy = st.builds(
    adfg::LossyChannel,
)
adfg::Channel_strategy = st.builds(
    adfg::Channel,
    initial=
        st.integers()
)
adfg::PeriodicActor_strategy = st.builds(
    adfg::PeriodicActor,
    periodLowerBound=
        safe_text,
    periodUpperBound=
        safe_text,
    period=
        safe_text,
    phase=
        safe_text,
    deadline=
        safe_text,
    wcet=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
adfg::InputPort_strategy = st.builds(
    adfg::InputPort,
)
adfg::OutputPort_strategy = st.builds(
    adfg::OutputPort,
)
adfg::AffineRelation_strategy = st.builds(
    adfg::AffineRelation,
    d=
        st.integers(),
    n=
        st.integers(),
    phi=
        st.integers()
)
adfg::Actor_strategy = st.builds(
    adfg::Actor,
    sourceCode=
        safe_text,
    procNumber=
        st.integers(),
    priority=
        st.integers(),
    name=
        safe_text,
    nbPorts=
        st.integers()
)
adfg::Port_strategy = st.builds(
    adfg::Port,
    name=
        safe_text,
    type=
        safe_text,
    sequence=
        safe_text
)
adfg::Connection_strategy = st.builds(
    adfg::Connection,
    size=
        st.integers(),
    id=
        st.integers()
)
adfg::GraphConnection_strategy = st.builds(
    adfg::GraphConnection,
)
adfg::Graph_strategy = st.builds(
    adfg::Graph,
    bufferingRequirements=
        st.integers(),
    sourceCode=
        safe_text,
    nbBuffers=
        st.integers(),
    nbActors=
        st.integers(),
    name=
        safe_text,
    id=
        st.integers(),
    processorUtilization=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
adfg::Application_strategy = st.builds(
    adfg::Application,
    dynamicChecking=
        st.booleans(),
    sourceCode=
        safe_text,
    name=
        safe_text,
    schedulingAlgorithm=
        safe_text,
    nbProcessors=
        st.integers(),
    nbGraphs=
        st.integers()
)

@given(instance=Actor_strategy)
@settings(max_examples=50)
def test_actor_instantiation(instance):
    assert isinstance(instance, Actor)

@given(instance=adfg::AperiodicActor_strategy)
@settings(max_examples=50)
def test_adfg::aperiodicactor_instantiation(instance):
    assert isinstance(instance, adfg::AperiodicActor)

@given(instance=adfg::AperiodicActor_strategy)
def test_adfg::aperiodicactor_capacity_type(instance):
    assert isinstance(instance.capacity, str)


@given(instance=adfg::AperiodicActor_strategy)
def test_adfg::aperiodicactor_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=adfg::AperiodicActor_strategy)
def test_adfg::aperiodicactor_replenishmentPeriod_type(instance):
    assert isinstance(instance.replenishmentPeriod, str)


@given(instance=adfg::AperiodicActor_strategy)
def test_adfg::aperiodicactor_replenishmentPeriod_setter(instance):
    original = instance.replenishmentPeriod
    instance.replenishmentPeriod = original
    assert instance.replenishmentPeriod == original

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=adfg::LossyChannel_strategy)
@settings(max_examples=50)
def test_adfg::lossychannel_instantiation(instance):
    assert isinstance(instance, adfg::LossyChannel)

@given(instance=adfg::Channel_strategy)
@settings(max_examples=50)
def test_adfg::channel_instantiation(instance):
    assert isinstance(instance, adfg::Channel)

@given(instance=adfg::Channel_strategy)
def test_adfg::channel_initial_type(instance):
    assert isinstance(instance.initial, int)


@given(instance=adfg::Channel_strategy)
def test_adfg::channel_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=adfg::PeriodicActor_strategy)
@settings(max_examples=50)
def test_adfg::periodicactor_instantiation(instance):
    assert isinstance(instance, adfg::PeriodicActor)

@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_periodLowerBound_type(instance):
    assert isinstance(instance.periodLowerBound, str)


@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_periodLowerBound_setter(instance):
    original = instance.periodLowerBound
    instance.periodLowerBound = original
    assert instance.periodLowerBound == original

@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_periodUpperBound_type(instance):
    assert isinstance(instance.periodUpperBound, str)


@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_periodUpperBound_setter(instance):
    original = instance.periodUpperBound
    instance.periodUpperBound = original
    assert instance.periodUpperBound == original

@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_period_type(instance):
    assert isinstance(instance.period, str)


@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_phase_type(instance):
    assert isinstance(instance.phase, str)


@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_phase_setter(instance):
    original = instance.phase
    instance.phase = original
    assert instance.phase == original

@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_deadline_type(instance):
    assert isinstance(instance.deadline, str)


@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_wcet_type(instance):
    assert isinstance(instance.wcet, str)


@given(instance=adfg::PeriodicActor_strategy)
def test_adfg::periodicactor_wcet_setter(instance):
    original = instance.wcet
    instance.wcet = original
    assert instance.wcet == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=adfg::InputPort_strategy)
@settings(max_examples=50)
def test_adfg::inputport_instantiation(instance):
    assert isinstance(instance, adfg::InputPort)

@given(instance=adfg::OutputPort_strategy)
@settings(max_examples=50)
def test_adfg::outputport_instantiation(instance):
    assert isinstance(instance, adfg::OutputPort)

@given(instance=adfg::AffineRelation_strategy)
@settings(max_examples=50)
def test_adfg::affinerelation_instantiation(instance):
    assert isinstance(instance, adfg::AffineRelation)

@given(instance=adfg::AffineRelation_strategy)
def test_adfg::affinerelation_d_type(instance):
    assert isinstance(instance.d, int)


@given(instance=adfg::AffineRelation_strategy)
def test_adfg::affinerelation_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=adfg::AffineRelation_strategy)
def test_adfg::affinerelation_n_type(instance):
    assert isinstance(instance.n, int)


@given(instance=adfg::AffineRelation_strategy)
def test_adfg::affinerelation_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=adfg::AffineRelation_strategy)
def test_adfg::affinerelation_phi_type(instance):
    assert isinstance(instance.phi, int)


@given(instance=adfg::AffineRelation_strategy)
def test_adfg::affinerelation_phi_setter(instance):
    original = instance.phi
    instance.phi = original
    assert instance.phi == original

@given(instance=adfg::Actor_strategy)
@settings(max_examples=50)
def test_adfg::actor_instantiation(instance):
    assert isinstance(instance, adfg::Actor)

@given(instance=adfg::Actor_strategy)
def test_adfg::actor_sourceCode_type(instance):
    assert isinstance(instance.sourceCode, str)


@given(instance=adfg::Actor_strategy)
def test_adfg::actor_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original

@given(instance=adfg::Actor_strategy)
def test_adfg::actor_procNumber_type(instance):
    assert isinstance(instance.procNumber, int)


@given(instance=adfg::Actor_strategy)
def test_adfg::actor_procNumber_setter(instance):
    original = instance.procNumber
    instance.procNumber = original
    assert instance.procNumber == original

@given(instance=adfg::Actor_strategy)
def test_adfg::actor_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=adfg::Actor_strategy)
def test_adfg::actor_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=adfg::Actor_strategy)
def test_adfg::actor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adfg::Actor_strategy)
def test_adfg::actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adfg::Actor_strategy)
def test_adfg::actor_nbPorts_type(instance):
    assert isinstance(instance.nbPorts, int)


@given(instance=adfg::Actor_strategy)
def test_adfg::actor_nbPorts_setter(instance):
    original = instance.nbPorts
    instance.nbPorts = original
    assert instance.nbPorts == original

@given(instance=adfg::Port_strategy)
@settings(max_examples=50)
def test_adfg::port_instantiation(instance):
    assert isinstance(instance, adfg::Port)

@given(instance=adfg::Port_strategy)
def test_adfg::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adfg::Port_strategy)
def test_adfg::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adfg::Port_strategy)
def test_adfg::port_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=adfg::Port_strategy)
def test_adfg::port_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=adfg::Port_strategy)
def test_adfg::port_sequence_type(instance):
    assert isinstance(instance.sequence, str)


@given(instance=adfg::Port_strategy)
def test_adfg::port_sequence_setter(instance):
    original = instance.sequence
    instance.sequence = original
    assert instance.sequence == original

@given(instance=adfg::Connection_strategy)
@settings(max_examples=50)
def test_adfg::connection_instantiation(instance):
    assert isinstance(instance, adfg::Connection)

@given(instance=adfg::Connection_strategy)
def test_adfg::connection_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=adfg::Connection_strategy)
def test_adfg::connection_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=adfg::Connection_strategy)
def test_adfg::connection_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=adfg::Connection_strategy)
def test_adfg::connection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=adfg::GraphConnection_strategy)
@settings(max_examples=50)
def test_adfg::graphconnection_instantiation(instance):
    assert isinstance(instance, adfg::GraphConnection)

@given(instance=adfg::Graph_strategy)
@settings(max_examples=50)
def test_adfg::graph_instantiation(instance):
    assert isinstance(instance, adfg::Graph)

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_bufferingRequirements_type(instance):
    assert isinstance(instance.bufferingRequirements, int)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_bufferingRequirements_setter(instance):
    original = instance.bufferingRequirements
    instance.bufferingRequirements = original
    assert instance.bufferingRequirements == original

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_sourceCode_type(instance):
    assert isinstance(instance.sourceCode, str)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_nbBuffers_type(instance):
    assert isinstance(instance.nbBuffers, int)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_nbBuffers_setter(instance):
    original = instance.nbBuffers
    instance.nbBuffers = original
    assert instance.nbBuffers == original

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_nbActors_type(instance):
    assert isinstance(instance.nbActors, int)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_nbActors_setter(instance):
    original = instance.nbActors
    instance.nbActors = original
    assert instance.nbActors == original

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=adfg::Graph_strategy)
def test_adfg::graph_processorUtilization_type(instance):
    assert isinstance(instance.processorUtilization, float)


@given(instance=adfg::Graph_strategy)
def test_adfg::graph_processorUtilization_setter(instance):
    original = instance.processorUtilization
    instance.processorUtilization = original
    assert instance.processorUtilization == original

@given(instance=adfg::Application_strategy)
@settings(max_examples=50)
def test_adfg::application_instantiation(instance):
    assert isinstance(instance, adfg::Application)

@given(instance=adfg::Application_strategy)
def test_adfg::application_dynamicChecking_type(instance):
    assert isinstance(instance.dynamicChecking, bool)


@given(instance=adfg::Application_strategy)
def test_adfg::application_dynamicChecking_setter(instance):
    original = instance.dynamicChecking
    instance.dynamicChecking = original
    assert instance.dynamicChecking == original

@given(instance=adfg::Application_strategy)
def test_adfg::application_sourceCode_type(instance):
    assert isinstance(instance.sourceCode, str)


@given(instance=adfg::Application_strategy)
def test_adfg::application_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original

@given(instance=adfg::Application_strategy)
def test_adfg::application_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adfg::Application_strategy)
def test_adfg::application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adfg::Application_strategy)
def test_adfg::application_schedulingAlgorithm_type(instance):
    assert isinstance(instance.schedulingAlgorithm, str)


@given(instance=adfg::Application_strategy)
def test_adfg::application_schedulingAlgorithm_setter(instance):
    original = instance.schedulingAlgorithm
    instance.schedulingAlgorithm = original
    assert instance.schedulingAlgorithm == original

@given(instance=adfg::Application_strategy)
def test_adfg::application_nbProcessors_type(instance):
    assert isinstance(instance.nbProcessors, int)


@given(instance=adfg::Application_strategy)
def test_adfg::application_nbProcessors_setter(instance):
    original = instance.nbProcessors
    instance.nbProcessors = original
    assert instance.nbProcessors == original

@given(instance=adfg::Application_strategy)
def test_adfg::application_nbGraphs_type(instance):
    assert isinstance(instance.nbGraphs, int)


@given(instance=adfg::Application_strategy)
def test_adfg::application_nbGraphs_setter(instance):
    original = instance.nbGraphs
    instance.nbGraphs = original
    assert instance.nbGraphs == original
