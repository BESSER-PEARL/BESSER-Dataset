import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BufferFunction,
    simulink::buffer::SharedCheckQueue,
    simulink::buffer::CheckQueue,
    simulink::buffer::SharedDequeue,
    simulink::buffer::SharedEnqueue,
    simulink::buffer::Dequeue,
    simulink::buffer::Enqueue,
    Action,
    EmbeddedFunction,
    simulink::buffer::BufferFunction,
    Event,
    Transition,
    Node,
    simulink::stateflow::History,
    simulink::stateflow::Junction,
    simulink::stateflow::State,
    Data,
    State,
    simulink::stateflow::Chart,
    stateflow::simulink::SimulinkFile,
    StateflowElement,
    simulink::stateflow::Node,
    simulink::stateflow::Transition,
    simulink::stateflow::EmbeddedFunction,
    simulink::stateflow::Data,
    simulink::stateflow::Event,
    simulink::stateflow::Action,
    simulink::stateflow::StateflowMachine,
    InPortBlock,
    simulink::EnablePort,
    simulink::TriggerPort,
    stateflow::simulink::ChartBlock,
    simulink::BusElement,
    Chart,
    PortBlock,
    StateflowMachine,
    SubSystem,
    simulink::SimulinkFile,
    Block,
    simulink::EmbeddedMatlabFunction,
    simulink::BusSelector,
    simulink::Constant,
    simulink::LibraryReference,
    simulink::ZeroOrderHold,
    simulink::reconfiguration::MultiSourceControl,
    simulink::MiscBlock,
    simulink::reconfiguration::MultiTargetControl,
    simulink::DigitalClock,
    simulink::ChartBlock,
    simulink::BusCreator,
    simulink::msglib::CommunicationSwitch,
    simulink::msglib::LinkLayer,
    simulink::UnitDelay,
    simulink::PortBlock,
    simulink::reconfiguration::FadingComponent,
    simulink::Parameter,
    simulink::Element,
    SimulinkFile,
    simulink::SimulinkLibrary,
    simulink::SimulinkModel,
    simulink::InPortBlock,
    simulink::OutPortBlock,
    Element,
    simulink::stateflow::StateflowElement,
    simulink::Bus,
    simulink::SimulinkContainer,
    simulink::Line,
    simulink::Block,
    simulink::SubSystem,
    SubStateType,
    TriggerEvent,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bufferfunction_is_not_abstract():
    assert not inspect.isabstract(BufferFunction)


def test_bufferfunction_constructor_exists():
    assert callable(BufferFunction.__init__)


def test_bufferfunction_constructor_args():
    sig = inspect.signature(BufferFunction.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::sharedcheckqueue_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::SharedCheckQueue)


def test_simulink::buffer::sharedcheckqueue_constructor_exists():
    assert callable(simulink::buffer::SharedCheckQueue.__init__)


def test_simulink::buffer::sharedcheckqueue_constructor_args():
    sig = inspect.signature(simulink::buffer::SharedCheckQueue.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::checkqueue_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::CheckQueue)


def test_simulink::buffer::checkqueue_constructor_exists():
    assert callable(simulink::buffer::CheckQueue.__init__)


def test_simulink::buffer::checkqueue_constructor_args():
    sig = inspect.signature(simulink::buffer::CheckQueue.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::shareddequeue_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::SharedDequeue)


def test_simulink::buffer::shareddequeue_constructor_exists():
    assert callable(simulink::buffer::SharedDequeue.__init__)


def test_simulink::buffer::shareddequeue_constructor_args():
    sig = inspect.signature(simulink::buffer::SharedDequeue.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::sharedenqueue_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::SharedEnqueue)


def test_simulink::buffer::sharedenqueue_constructor_exists():
    assert callable(simulink::buffer::SharedEnqueue.__init__)


def test_simulink::buffer::sharedenqueue_constructor_args():
    sig = inspect.signature(simulink::buffer::SharedEnqueue.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::dequeue_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::Dequeue)


def test_simulink::buffer::dequeue_constructor_exists():
    assert callable(simulink::buffer::Dequeue.__init__)


def test_simulink::buffer::dequeue_constructor_args():
    sig = inspect.signature(simulink::buffer::Dequeue.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::enqueue_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::Enqueue)


def test_simulink::buffer::enqueue_constructor_exists():
    assert callable(simulink::buffer::Enqueue.__init__)


def test_simulink::buffer::enqueue_constructor_args():
    sig = inspect.signature(simulink::buffer::Enqueue.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_embeddedfunction_is_not_abstract():
    assert not inspect.isabstract(EmbeddedFunction)


def test_embeddedfunction_constructor_exists():
    assert callable(EmbeddedFunction.__init__)


def test_embeddedfunction_constructor_args():
    sig = inspect.signature(EmbeddedFunction.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buffer::bufferfunction_is_not_abstract():
    assert not inspect.isabstract(simulink::buffer::BufferFunction)


def test_simulink::buffer::bufferfunction_constructor_exists():
    assert callable(simulink::buffer::BufferFunction.__init__)


def test_simulink::buffer::bufferfunction_constructor_args():
    sig = inspect.signature(simulink::buffer::BufferFunction.__init__)
    params = list(sig.parameters.keys())
    assert "bufferSize" in params, "Missing parameter 'bufferSize'"

def test_simulink::buffer::bufferfunction_has_bufferSize():
    assert hasattr(simulink::buffer::BufferFunction, "bufferSize")
    descriptor = None
    for klass in simulink::buffer::BufferFunction.__mro__:
        if "bufferSize" in klass.__dict__:
            descriptor = klass.__dict__["bufferSize"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::history_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::History)


def test_simulink::stateflow::history_constructor_exists():
    assert callable(simulink::stateflow::History.__init__)


def test_simulink::stateflow::history_constructor_args():
    sig = inspect.signature(simulink::stateflow::History.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::junction_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Junction)


def test_simulink::stateflow::junction_constructor_exists():
    assert callable(simulink::stateflow::Junction.__init__)


def test_simulink::stateflow::junction_constructor_args():
    sig = inspect.signature(simulink::stateflow::Junction.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::state_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::State)


def test_simulink::stateflow::state_constructor_exists():
    assert callable(simulink::stateflow::State.__init__)


def test_simulink::stateflow::state_constructor_args():
    sig = inspect.signature(simulink::stateflow::State.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "subStateType" in params, "Missing parameter 'subStateType'"
    assert "name" in params, "Missing parameter 'name'"

def test_simulink::stateflow::state_has_priority():
    assert hasattr(simulink::stateflow::State, "priority")
    descriptor = None
    for klass in simulink::stateflow::State.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::state_has_initial():
    assert hasattr(simulink::stateflow::State, "initial")
    descriptor = None
    for klass in simulink::stateflow::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::state_has_subStateType():
    assert hasattr(simulink::stateflow::State, "subStateType")
    descriptor = None
    for klass in simulink::stateflow::State.__mro__:
        if "subStateType" in klass.__dict__:
            descriptor = klass.__dict__["subStateType"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::state_has_name():
    assert hasattr(simulink::stateflow::State, "name")
    descriptor = None
    for klass in simulink::stateflow::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::chart_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Chart)


def test_simulink::stateflow::chart_constructor_exists():
    assert callable(simulink::stateflow::Chart.__init__)


def test_simulink::stateflow::chart_constructor_args():
    sig = inspect.signature(simulink::stateflow::Chart.__init__)
    params = list(sig.parameters.keys())



def test_stateflow::simulink::simulinkfile_is_not_abstract():
    assert not inspect.isabstract(stateflow::simulink::SimulinkFile)


def test_stateflow::simulink::simulinkfile_constructor_exists():
    assert callable(stateflow::simulink::SimulinkFile.__init__)


def test_stateflow::simulink::simulinkfile_constructor_args():
    sig = inspect.signature(stateflow::simulink::SimulinkFile.__init__)
    params = list(sig.parameters.keys())



def test_stateflowelement_is_not_abstract():
    assert not inspect.isabstract(StateflowElement)


def test_stateflowelement_constructor_exists():
    assert callable(StateflowElement.__init__)


def test_stateflowelement_constructor_args():
    sig = inspect.signature(StateflowElement.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::node_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Node)


def test_simulink::stateflow::node_constructor_exists():
    assert callable(simulink::stateflow::Node.__init__)


def test_simulink::stateflow::node_constructor_args():
    sig = inspect.signature(simulink::stateflow::Node.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::transition_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Transition)


def test_simulink::stateflow::transition_constructor_exists():
    assert callable(simulink::stateflow::Transition.__init__)


def test_simulink::stateflow::transition_constructor_args():
    sig = inspect.signature(simulink::stateflow::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_simulink::stateflow::transition_has_priority():
    assert hasattr(simulink::stateflow::Transition, "priority")
    descriptor = None
    for klass in simulink::stateflow::Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_simulink::stateflow::embeddedfunction_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::EmbeddedFunction)


def test_simulink::stateflow::embeddedfunction_constructor_exists():
    assert callable(simulink::stateflow::EmbeddedFunction.__init__)


def test_simulink::stateflow::embeddedfunction_constructor_args():
    sig = inspect.signature(simulink::stateflow::EmbeddedFunction.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_simulink::stateflow::embeddedfunction_has_code():
    assert hasattr(simulink::stateflow::EmbeddedFunction, "code")
    descriptor = None
    for klass in simulink::stateflow::EmbeddedFunction.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::embeddedfunction_has_name():
    assert hasattr(simulink::stateflow::EmbeddedFunction, "name")
    descriptor = None
    for klass in simulink::stateflow::EmbeddedFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink::stateflow::data_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Data)


def test_simulink::stateflow::data_constructor_exists():
    assert callable(simulink::stateflow::Data.__init__)


def test_simulink::stateflow::data_constructor_args():
    sig = inspect.signature(simulink::stateflow::Data.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"

def test_simulink::stateflow::data_has_type():
    assert hasattr(simulink::stateflow::Data, "type")
    descriptor = None
    for klass in simulink::stateflow::Data.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::data_has_value():
    assert hasattr(simulink::stateflow::Data, "value")
    descriptor = None
    for klass in simulink::stateflow::Data.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::data_has_name():
    assert hasattr(simulink::stateflow::Data, "name")
    descriptor = None
    for klass in simulink::stateflow::Data.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simulink::stateflow::data_has_size():
    assert hasattr(simulink::stateflow::Data, "size")
    descriptor = None
    for klass in simulink::stateflow::Data.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_simulink::stateflow::event_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Event)


def test_simulink::stateflow::event_constructor_exists():
    assert callable(simulink::stateflow::Event.__init__)


def test_simulink::stateflow::event_constructor_args():
    sig = inspect.signature(simulink::stateflow::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simulink::stateflow::event_has_name():
    assert hasattr(simulink::stateflow::Event, "name")
    descriptor = None
    for klass in simulink::stateflow::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink::stateflow::action_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::Action)


def test_simulink::stateflow::action_constructor_exists():
    assert callable(simulink::stateflow::Action.__init__)


def test_simulink::stateflow::action_constructor_args():
    sig = inspect.signature(simulink::stateflow::Action.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_simulink::stateflow::action_has_expression():
    assert hasattr(simulink::stateflow::Action, "expression")
    descriptor = None
    for klass in simulink::stateflow::Action.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_simulink::stateflow::stateflowmachine_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::StateflowMachine)


def test_simulink::stateflow::stateflowmachine_constructor_exists():
    assert callable(simulink::stateflow::StateflowMachine.__init__)


def test_simulink::stateflow::stateflowmachine_constructor_args():
    sig = inspect.signature(simulink::stateflow::StateflowMachine.__init__)
    params = list(sig.parameters.keys())



def test_inportblock_is_not_abstract():
    assert not inspect.isabstract(InPortBlock)


def test_inportblock_constructor_exists():
    assert callable(InPortBlock.__init__)


def test_inportblock_constructor_args():
    sig = inspect.signature(InPortBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink::enableport_is_not_abstract():
    assert not inspect.isabstract(simulink::EnablePort)


def test_simulink::enableport_constructor_exists():
    assert callable(simulink::EnablePort.__init__)


def test_simulink::enableport_constructor_args():
    sig = inspect.signature(simulink::EnablePort.__init__)
    params = list(sig.parameters.keys())



def test_simulink::triggerport_is_not_abstract():
    assert not inspect.isabstract(simulink::TriggerPort)


def test_simulink::triggerport_constructor_exists():
    assert callable(simulink::TriggerPort.__init__)


def test_simulink::triggerport_constructor_args():
    sig = inspect.signature(simulink::TriggerPort.__init__)
    params = list(sig.parameters.keys())
    assert "triggerInput" in params, "Missing parameter 'triggerInput'"

def test_simulink::triggerport_has_triggerInput():
    assert hasattr(simulink::TriggerPort, "triggerInput")
    descriptor = None
    for klass in simulink::TriggerPort.__mro__:
        if "triggerInput" in klass.__dict__:
            descriptor = klass.__dict__["triggerInput"]
            break
    assert isinstance(descriptor, property)



def test_stateflow::simulink::chartblock_is_not_abstract():
    assert not inspect.isabstract(stateflow::simulink::ChartBlock)


def test_stateflow::simulink::chartblock_constructor_exists():
    assert callable(stateflow::simulink::ChartBlock.__init__)


def test_stateflow::simulink::chartblock_constructor_args():
    sig = inspect.signature(stateflow::simulink::ChartBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buselement_is_not_abstract():
    assert not inspect.isabstract(simulink::BusElement)


def test_simulink::buselement_constructor_exists():
    assert callable(simulink::BusElement.__init__)


def test_simulink::buselement_constructor_args():
    sig = inspect.signature(simulink::BusElement.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_simulink::buselement_has_dimensions():
    assert hasattr(simulink::BusElement, "dimensions")
    descriptor = None
    for klass in simulink::BusElement.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)

def test_simulink::buselement_has_name():
    assert hasattr(simulink::BusElement, "name")
    descriptor = None
    for klass in simulink::BusElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simulink::buselement_has_type():
    assert hasattr(simulink::BusElement, "type")
    descriptor = None
    for klass in simulink::BusElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_chart_is_not_abstract():
    assert not inspect.isabstract(Chart)


def test_chart_constructor_exists():
    assert callable(Chart.__init__)


def test_chart_constructor_args():
    sig = inspect.signature(Chart.__init__)
    params = list(sig.parameters.keys())



def test_portblock_is_not_abstract():
    assert not inspect.isabstract(PortBlock)


def test_portblock_constructor_exists():
    assert callable(PortBlock.__init__)


def test_portblock_constructor_args():
    sig = inspect.signature(PortBlock.__init__)
    params = list(sig.parameters.keys())



def test_stateflowmachine_is_not_abstract():
    assert not inspect.isabstract(StateflowMachine)


def test_stateflowmachine_constructor_exists():
    assert callable(StateflowMachine.__init__)


def test_stateflowmachine_constructor_args():
    sig = inspect.signature(StateflowMachine.__init__)
    params = list(sig.parameters.keys())



def test_subsystem_is_not_abstract():
    assert not inspect.isabstract(SubSystem)


def test_subsystem_constructor_exists():
    assert callable(SubSystem.__init__)


def test_subsystem_constructor_args():
    sig = inspect.signature(SubSystem.__init__)
    params = list(sig.parameters.keys())



def test_simulink::simulinkfile_is_not_abstract():
    assert not inspect.isabstract(simulink::SimulinkFile)


def test_simulink::simulinkfile_constructor_exists():
    assert callable(simulink::SimulinkFile.__init__)


def test_simulink::simulinkfile_constructor_args():
    sig = inspect.signature(simulink::SimulinkFile.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_simulink::embeddedmatlabfunction_is_not_abstract():
    assert not inspect.isabstract(simulink::EmbeddedMatlabFunction)


def test_simulink::embeddedmatlabfunction_constructor_exists():
    assert callable(simulink::EmbeddedMatlabFunction.__init__)


def test_simulink::embeddedmatlabfunction_constructor_args():
    sig = inspect.signature(simulink::EmbeddedMatlabFunction.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_simulink::embeddedmatlabfunction_has_code():
    assert hasattr(simulink::EmbeddedMatlabFunction, "code")
    descriptor = None
    for klass in simulink::EmbeddedMatlabFunction.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_simulink::busselector_is_not_abstract():
    assert not inspect.isabstract(simulink::BusSelector)


def test_simulink::busselector_constructor_exists():
    assert callable(simulink::BusSelector.__init__)


def test_simulink::busselector_constructor_args():
    sig = inspect.signature(simulink::BusSelector.__init__)
    params = list(sig.parameters.keys())



def test_simulink::constant_is_not_abstract():
    assert not inspect.isabstract(simulink::Constant)


def test_simulink::constant_constructor_exists():
    assert callable(simulink::Constant.__init__)


def test_simulink::constant_constructor_args():
    sig = inspect.signature(simulink::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_simulink::constant_has_type():
    assert hasattr(simulink::Constant, "type")
    descriptor = None
    for klass in simulink::Constant.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink::constant_has_value():
    assert hasattr(simulink::Constant, "value")
    descriptor = None
    for klass in simulink::Constant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simulink::libraryreference_is_not_abstract():
    assert not inspect.isabstract(simulink::LibraryReference)


def test_simulink::libraryreference_constructor_exists():
    assert callable(simulink::LibraryReference.__init__)


def test_simulink::libraryreference_constructor_args():
    sig = inspect.signature(simulink::LibraryReference.__init__)
    params = list(sig.parameters.keys())



def test_simulink::zeroorderhold_is_not_abstract():
    assert not inspect.isabstract(simulink::ZeroOrderHold)


def test_simulink::zeroorderhold_constructor_exists():
    assert callable(simulink::ZeroOrderHold.__init__)


def test_simulink::zeroorderhold_constructor_args():
    sig = inspect.signature(simulink::ZeroOrderHold.__init__)
    params = list(sig.parameters.keys())
    assert "sampleTime" in params, "Missing parameter 'sampleTime'"

def test_simulink::zeroorderhold_has_sampleTime():
    assert hasattr(simulink::ZeroOrderHold, "sampleTime")
    descriptor = None
    for klass in simulink::ZeroOrderHold.__mro__:
        if "sampleTime" in klass.__dict__:
            descriptor = klass.__dict__["sampleTime"]
            break
    assert isinstance(descriptor, property)



def test_simulink::reconfiguration::multisourcecontrol_is_not_abstract():
    assert not inspect.isabstract(simulink::reconfiguration::MultiSourceControl)


def test_simulink::reconfiguration::multisourcecontrol_constructor_exists():
    assert callable(simulink::reconfiguration::MultiSourceControl.__init__)


def test_simulink::reconfiguration::multisourcecontrol_constructor_args():
    sig = inspect.signature(simulink::reconfiguration::MultiSourceControl.__init__)
    params = list(sig.parameters.keys())



def test_simulink::miscblock_is_not_abstract():
    assert not inspect.isabstract(simulink::MiscBlock)


def test_simulink::miscblock_constructor_exists():
    assert callable(simulink::MiscBlock.__init__)


def test_simulink::miscblock_constructor_args():
    sig = inspect.signature(simulink::MiscBlock.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simulink::miscblock_has_type():
    assert hasattr(simulink::MiscBlock, "type")
    descriptor = None
    for klass in simulink::MiscBlock.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simulink::reconfiguration::multitargetcontrol_is_not_abstract():
    assert not inspect.isabstract(simulink::reconfiguration::MultiTargetControl)


def test_simulink::reconfiguration::multitargetcontrol_constructor_exists():
    assert callable(simulink::reconfiguration::MultiTargetControl.__init__)


def test_simulink::reconfiguration::multitargetcontrol_constructor_args():
    sig = inspect.signature(simulink::reconfiguration::MultiTargetControl.__init__)
    params = list(sig.parameters.keys())



def test_simulink::digitalclock_is_not_abstract():
    assert not inspect.isabstract(simulink::DigitalClock)


def test_simulink::digitalclock_constructor_exists():
    assert callable(simulink::DigitalClock.__init__)


def test_simulink::digitalclock_constructor_args():
    sig = inspect.signature(simulink::DigitalClock.__init__)
    params = list(sig.parameters.keys())
    assert "sampleTime" in params, "Missing parameter 'sampleTime'"

def test_simulink::digitalclock_has_sampleTime():
    assert hasattr(simulink::DigitalClock, "sampleTime")
    descriptor = None
    for klass in simulink::DigitalClock.__mro__:
        if "sampleTime" in klass.__dict__:
            descriptor = klass.__dict__["sampleTime"]
            break
    assert isinstance(descriptor, property)



def test_simulink::chartblock_is_not_abstract():
    assert not inspect.isabstract(simulink::ChartBlock)


def test_simulink::chartblock_constructor_exists():
    assert callable(simulink::ChartBlock.__init__)


def test_simulink::chartblock_constructor_args():
    sig = inspect.signature(simulink::ChartBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink::buscreator_is_not_abstract():
    assert not inspect.isabstract(simulink::BusCreator)


def test_simulink::buscreator_constructor_exists():
    assert callable(simulink::BusCreator.__init__)


def test_simulink::buscreator_constructor_args():
    sig = inspect.signature(simulink::BusCreator.__init__)
    params = list(sig.parameters.keys())



def test_simulink::msglib::communicationswitch_is_not_abstract():
    assert not inspect.isabstract(simulink::msglib::CommunicationSwitch)


def test_simulink::msglib::communicationswitch_constructor_exists():
    assert callable(simulink::msglib::CommunicationSwitch.__init__)


def test_simulink::msglib::communicationswitch_constructor_args():
    sig = inspect.signature(simulink::msglib::CommunicationSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"

def test_simulink::msglib::communicationswitch_has_debug():
    assert hasattr(simulink::msglib::CommunicationSwitch, "debug")
    descriptor = None
    for klass in simulink::msglib::CommunicationSwitch.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_simulink::msglib::linklayer_is_not_abstract():
    assert not inspect.isabstract(simulink::msglib::LinkLayer)


def test_simulink::msglib::linklayer_constructor_exists():
    assert callable(simulink::msglib::LinkLayer.__init__)


def test_simulink::msglib::linklayer_constructor_args():
    sig = inspect.signature(simulink::msglib::LinkLayer.__init__)
    params = list(sig.parameters.keys())
    assert "delayMin" in params, "Missing parameter 'delayMin'"
    assert "delayMax" in params, "Missing parameter 'delayMax'"
    assert "messageRetransmission" in params, "Missing parameter 'messageRetransmission'"
    assert "bufferOverflowPossible" in params, "Missing parameter 'bufferOverflowPossible'"
    assert "messageLossProbability" in params, "Missing parameter 'messageLossProbability'"
    assert "messageMapping" in params, "Missing parameter 'messageMapping'"
    assert "bufferSize" in params, "Missing parameter 'bufferSize'"
    assert "sourceBufferSize" in params, "Missing parameter 'sourceBufferSize'"

def test_simulink::msglib::linklayer_has_delayMin():
    assert hasattr(simulink::msglib::LinkLayer, "delayMin")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "delayMin" in klass.__dict__:
            descriptor = klass.__dict__["delayMin"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_delayMax():
    assert hasattr(simulink::msglib::LinkLayer, "delayMax")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "delayMax" in klass.__dict__:
            descriptor = klass.__dict__["delayMax"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_messageRetransmission():
    assert hasattr(simulink::msglib::LinkLayer, "messageRetransmission")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "messageRetransmission" in klass.__dict__:
            descriptor = klass.__dict__["messageRetransmission"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_bufferOverflowPossible():
    assert hasattr(simulink::msglib::LinkLayer, "bufferOverflowPossible")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "bufferOverflowPossible" in klass.__dict__:
            descriptor = klass.__dict__["bufferOverflowPossible"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_messageLossProbability():
    assert hasattr(simulink::msglib::LinkLayer, "messageLossProbability")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "messageLossProbability" in klass.__dict__:
            descriptor = klass.__dict__["messageLossProbability"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_messageMapping():
    assert hasattr(simulink::msglib::LinkLayer, "messageMapping")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "messageMapping" in klass.__dict__:
            descriptor = klass.__dict__["messageMapping"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_bufferSize():
    assert hasattr(simulink::msglib::LinkLayer, "bufferSize")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "bufferSize" in klass.__dict__:
            descriptor = klass.__dict__["bufferSize"]
            break
    assert isinstance(descriptor, property)

def test_simulink::msglib::linklayer_has_sourceBufferSize():
    assert hasattr(simulink::msglib::LinkLayer, "sourceBufferSize")
    descriptor = None
    for klass in simulink::msglib::LinkLayer.__mro__:
        if "sourceBufferSize" in klass.__dict__:
            descriptor = klass.__dict__["sourceBufferSize"]
            break
    assert isinstance(descriptor, property)



def test_simulink::unitdelay_is_not_abstract():
    assert not inspect.isabstract(simulink::UnitDelay)


def test_simulink::unitdelay_constructor_exists():
    assert callable(simulink::UnitDelay.__init__)


def test_simulink::unitdelay_constructor_args():
    sig = inspect.signature(simulink::UnitDelay.__init__)
    params = list(sig.parameters.keys())



def test_simulink::portblock_is_not_abstract():
    assert not inspect.isabstract(simulink::PortBlock)


def test_simulink::portblock_constructor_exists():
    assert callable(simulink::PortBlock.__init__)


def test_simulink::portblock_constructor_args():
    sig = inspect.signature(simulink::PortBlock.__init__)
    params = list(sig.parameters.keys())
    assert "initialCondition" in params, "Missing parameter 'initialCondition'"
    assert "type" in params, "Missing parameter 'type'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_simulink::portblock_has_initialCondition():
    assert hasattr(simulink::PortBlock, "initialCondition")
    descriptor = None
    for klass in simulink::PortBlock.__mro__:
        if "initialCondition" in klass.__dict__:
            descriptor = klass.__dict__["initialCondition"]
            break
    assert isinstance(descriptor, property)

def test_simulink::portblock_has_type():
    assert hasattr(simulink::PortBlock, "type")
    descriptor = None
    for klass in simulink::PortBlock.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink::portblock_has_dimensions():
    assert hasattr(simulink::PortBlock, "dimensions")
    descriptor = None
    for klass in simulink::PortBlock.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_simulink::reconfiguration::fadingcomponent_is_not_abstract():
    assert not inspect.isabstract(simulink::reconfiguration::FadingComponent)


def test_simulink::reconfiguration::fadingcomponent_constructor_exists():
    assert callable(simulink::reconfiguration::FadingComponent.__init__)


def test_simulink::reconfiguration::fadingcomponent_constructor_args():
    sig = inspect.signature(simulink::reconfiguration::FadingComponent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_simulink::reconfiguration::fadingcomponent_has_time():
    assert hasattr(simulink::reconfiguration::FadingComponent, "time")
    descriptor = None
    for klass in simulink::reconfiguration::FadingComponent.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_simulink::parameter_is_not_abstract():
    assert not inspect.isabstract(simulink::Parameter)


def test_simulink::parameter_constructor_exists():
    assert callable(simulink::Parameter.__init__)


def test_simulink::parameter_constructor_args():
    sig = inspect.signature(simulink::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_simulink::parameter_has_value():
    assert hasattr(simulink::Parameter, "value")
    descriptor = None
    for klass in simulink::Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_simulink::parameter_has_type():
    assert hasattr(simulink::Parameter, "type")
    descriptor = None
    for klass in simulink::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink::parameter_has_name():
    assert hasattr(simulink::Parameter, "name")
    descriptor = None
    for klass in simulink::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink::element_is_not_abstract():
    assert not inspect.isabstract(simulink::Element)


def test_simulink::element_constructor_exists():
    assert callable(simulink::Element.__init__)


def test_simulink::element_constructor_args():
    sig = inspect.signature(simulink::Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simulink::element_has_id():
    assert hasattr(simulink::Element, "id")
    descriptor = None
    for klass in simulink::Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simulinkfile_is_not_abstract():
    assert not inspect.isabstract(SimulinkFile)


def test_simulinkfile_constructor_exists():
    assert callable(SimulinkFile.__init__)


def test_simulinkfile_constructor_args():
    sig = inspect.signature(SimulinkFile.__init__)
    params = list(sig.parameters.keys())



def test_simulink::simulinklibrary_is_not_abstract():
    assert not inspect.isabstract(simulink::SimulinkLibrary)


def test_simulink::simulinklibrary_constructor_exists():
    assert callable(simulink::SimulinkLibrary.__init__)


def test_simulink::simulinklibrary_constructor_args():
    sig = inspect.signature(simulink::SimulinkLibrary.__init__)
    params = list(sig.parameters.keys())



def test_simulink::simulinkmodel_is_not_abstract():
    assert not inspect.isabstract(simulink::SimulinkModel)


def test_simulink::simulinkmodel_constructor_exists():
    assert callable(simulink::SimulinkModel.__init__)


def test_simulink::simulinkmodel_constructor_args():
    sig = inspect.signature(simulink::SimulinkModel.__init__)
    params = list(sig.parameters.keys())



def test_simulink::inportblock_is_not_abstract():
    assert not inspect.isabstract(simulink::InPortBlock)


def test_simulink::inportblock_constructor_exists():
    assert callable(simulink::InPortBlock.__init__)


def test_simulink::inportblock_constructor_args():
    sig = inspect.signature(simulink::InPortBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink::outportblock_is_not_abstract():
    assert not inspect.isabstract(simulink::OutPortBlock)


def test_simulink::outportblock_constructor_exists():
    assert callable(simulink::OutPortBlock.__init__)


def test_simulink::outportblock_constructor_args():
    sig = inspect.signature(simulink::OutPortBlock.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_simulink::stateflow::stateflowelement_is_not_abstract():
    assert not inspect.isabstract(simulink::stateflow::StateflowElement)


def test_simulink::stateflow::stateflowelement_constructor_exists():
    assert callable(simulink::stateflow::StateflowElement.__init__)


def test_simulink::stateflow::stateflowelement_constructor_args():
    sig = inspect.signature(simulink::stateflow::StateflowElement.__init__)
    params = list(sig.parameters.keys())



def test_simulink::bus_is_not_abstract():
    assert not inspect.isabstract(simulink::Bus)


def test_simulink::bus_constructor_exists():
    assert callable(simulink::Bus.__init__)


def test_simulink::bus_constructor_args():
    sig = inspect.signature(simulink::Bus.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simulink::bus_has_name():
    assert hasattr(simulink::Bus, "name")
    descriptor = None
    for klass in simulink::Bus.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink::simulinkcontainer_is_not_abstract():
    assert not inspect.isabstract(simulink::SimulinkContainer)


def test_simulink::simulinkcontainer_constructor_exists():
    assert callable(simulink::SimulinkContainer.__init__)


def test_simulink::simulinkcontainer_constructor_args():
    sig = inspect.signature(simulink::SimulinkContainer.__init__)
    params = list(sig.parameters.keys())



def test_simulink::line_is_not_abstract():
    assert not inspect.isabstract(simulink::Line)


def test_simulink::line_constructor_exists():
    assert callable(simulink::Line.__init__)


def test_simulink::line_constructor_args():
    sig = inspect.signature(simulink::Line.__init__)
    params = list(sig.parameters.keys())



def test_simulink::block_is_not_abstract():
    assert not inspect.isabstract(simulink::Block)


def test_simulink::block_constructor_exists():
    assert callable(simulink::Block.__init__)


def test_simulink::block_constructor_args():
    sig = inspect.signature(simulink::Block.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simulink::block_has_name():
    assert hasattr(simulink::Block, "name")
    descriptor = None
    for klass in simulink::Block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink::subsystem_is_not_abstract():
    assert not inspect.isabstract(simulink::SubSystem)


def test_simulink::subsystem_constructor_exists():
    assert callable(simulink::SubSystem.__init__)


def test_simulink::subsystem_constructor_args():
    sig = inspect.signature(simulink::SubSystem.__init__)
    params = list(sig.parameters.keys())

def test_substatetype_exists():
    # Check that the Enumeration exists
    assert SubStateType is not None

def test_substatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubStateType]
    expected_literals = [
        "PARALLEL",
        "EXCLUSIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubStateType"

def test_triggerevent_exists():
    # Check that the Enumeration exists
    assert TriggerEvent is not None

def test_triggerevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerEvent]
    expected_literals = [
        "Rising",
        "Either",
        "Falling",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerEvent"

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "UINT32",
        "DOUBLE",
        "UINT16",
        "INT32",
        "BUS",
        "BOOLEAN",
        "SINGLE",
        "INHERIT",
        "INT8",
        "INT16",
        "UINT8",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
BufferFunction_strategy = st.builds(
    BufferFunction,
)
simulink::buffer::SharedCheckQueue_strategy = st.builds(
    simulink::buffer::SharedCheckQueue,
)
simulink::buffer::CheckQueue_strategy = st.builds(
    simulink::buffer::CheckQueue,
)
simulink::buffer::SharedDequeue_strategy = st.builds(
    simulink::buffer::SharedDequeue,
)
simulink::buffer::SharedEnqueue_strategy = st.builds(
    simulink::buffer::SharedEnqueue,
)
simulink::buffer::Dequeue_strategy = st.builds(
    simulink::buffer::Dequeue,
)
simulink::buffer::Enqueue_strategy = st.builds(
    simulink::buffer::Enqueue,
)
Action_strategy = st.builds(
    Action,
)
EmbeddedFunction_strategy = st.builds(
    EmbeddedFunction,
)
simulink::buffer::BufferFunction_strategy = st.builds(
    simulink::buffer::BufferFunction,
    bufferSize=
        st.integers()
)
Event_strategy = st.builds(
    Event,
)
Transition_strategy = st.builds(
    Transition,
)
Node_strategy = st.builds(
    Node,
)
simulink::stateflow::History_strategy = st.builds(
    simulink::stateflow::History,
)
simulink::stateflow::Junction_strategy = st.builds(
    simulink::stateflow::Junction,
)
simulink::stateflow::State_strategy = st.builds(
    simulink::stateflow::State,
    priority=
        st.integers(),
    initial=
        st.booleans(),
    subStateType=
        safe_text,
    name=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
State_strategy = st.builds(
    State,
)
simulink::stateflow::Chart_strategy = st.builds(
    simulink::stateflow::Chart,
)
stateflow::simulink::SimulinkFile_strategy = st.builds(
    stateflow::simulink::SimulinkFile,
)
StateflowElement_strategy = st.builds(
    StateflowElement,
)
simulink::stateflow::Node_strategy = st.builds(
    simulink::stateflow::Node,
)
simulink::stateflow::Transition_strategy = st.builds(
    simulink::stateflow::Transition,
    priority=
        st.integers()
)
simulink::stateflow::EmbeddedFunction_strategy = st.builds(
    simulink::stateflow::EmbeddedFunction,
    code=
        safe_text,
    name=
        safe_text
)
simulink::stateflow::Data_strategy = st.builds(
    simulink::stateflow::Data,
    type=
        safe_text,
    value=
        safe_text,
    name=
        safe_text,
    size=
        safe_text
)
simulink::stateflow::Event_strategy = st.builds(
    simulink::stateflow::Event,
    name=
        safe_text
)
simulink::stateflow::Action_strategy = st.builds(
    simulink::stateflow::Action,
    expression=
        safe_text
)
simulink::stateflow::StateflowMachine_strategy = st.builds(
    simulink::stateflow::StateflowMachine,
)
InPortBlock_strategy = st.builds(
    InPortBlock,
)
simulink::EnablePort_strategy = st.builds(
    simulink::EnablePort,
)
simulink::TriggerPort_strategy = st.builds(
    simulink::TriggerPort,
    triggerInput=
        safe_text
)
stateflow::simulink::ChartBlock_strategy = st.builds(
    stateflow::simulink::ChartBlock,
)
simulink::BusElement_strategy = st.builds(
    simulink::BusElement,
    dimensions=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
Chart_strategy = st.builds(
    Chart,
)
PortBlock_strategy = st.builds(
    PortBlock,
)
StateflowMachine_strategy = st.builds(
    StateflowMachine,
)
SubSystem_strategy = st.builds(
    SubSystem,
)
simulink::SimulinkFile_strategy = st.builds(
    simulink::SimulinkFile,
)
Block_strategy = st.builds(
    Block,
)
simulink::EmbeddedMatlabFunction_strategy = st.builds(
    simulink::EmbeddedMatlabFunction,
    code=
        safe_text
)
simulink::BusSelector_strategy = st.builds(
    simulink::BusSelector,
)
simulink::Constant_strategy = st.builds(
    simulink::Constant,
    type=
        safe_text,
    value=
        safe_text
)
simulink::LibraryReference_strategy = st.builds(
    simulink::LibraryReference,
)
simulink::ZeroOrderHold_strategy = st.builds(
    simulink::ZeroOrderHold,
    sampleTime=
        safe_text
)
simulink::reconfiguration::MultiSourceControl_strategy = st.builds(
    simulink::reconfiguration::MultiSourceControl,
)
simulink::MiscBlock_strategy = st.builds(
    simulink::MiscBlock,
    type=
        safe_text
)
simulink::reconfiguration::MultiTargetControl_strategy = st.builds(
    simulink::reconfiguration::MultiTargetControl,
)
simulink::DigitalClock_strategy = st.builds(
    simulink::DigitalClock,
    sampleTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
simulink::ChartBlock_strategy = st.builds(
    simulink::ChartBlock,
)
simulink::BusCreator_strategy = st.builds(
    simulink::BusCreator,
)
simulink::msglib::CommunicationSwitch_strategy = st.builds(
    simulink::msglib::CommunicationSwitch,
    debug=
        st.integers()
)
simulink::msglib::LinkLayer_strategy = st.builds(
    simulink::msglib::LinkLayer,
    delayMin=
        safe_text,
    delayMax=
        safe_text,
    messageRetransmission=
        st.booleans(),
    bufferOverflowPossible=
        st.booleans(),
    messageLossProbability=
        st.integers(),
    messageMapping=
        safe_text,
    bufferSize=
        st.integers(),
    sourceBufferSize=
        st.integers()
)
simulink::UnitDelay_strategy = st.builds(
    simulink::UnitDelay,
)
simulink::PortBlock_strategy = st.builds(
    simulink::PortBlock,
    initialCondition=
        safe_text,
    type=
        safe_text,
    dimensions=
        safe_text
)
simulink::reconfiguration::FadingComponent_strategy = st.builds(
    simulink::reconfiguration::FadingComponent,
    time=
        st.integers()
)
simulink::Parameter_strategy = st.builds(
    simulink::Parameter,
    value=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
simulink::Element_strategy = st.builds(
    simulink::Element,
    id=
        safe_text
)
SimulinkFile_strategy = st.builds(
    SimulinkFile,
)
simulink::SimulinkLibrary_strategy = st.builds(
    simulink::SimulinkLibrary,
)
simulink::SimulinkModel_strategy = st.builds(
    simulink::SimulinkModel,
)
simulink::InPortBlock_strategy = st.builds(
    simulink::InPortBlock,
)
simulink::OutPortBlock_strategy = st.builds(
    simulink::OutPortBlock,
)
Element_strategy = st.builds(
    Element,
)
simulink::stateflow::StateflowElement_strategy = st.builds(
    simulink::stateflow::StateflowElement,
)
simulink::Bus_strategy = st.builds(
    simulink::Bus,
    name=
        safe_text
)
simulink::SimulinkContainer_strategy = st.builds(
    simulink::SimulinkContainer,
)
simulink::Line_strategy = st.builds(
    simulink::Line,
)
simulink::Block_strategy = st.builds(
    simulink::Block,
    name=
        safe_text
)
simulink::SubSystem_strategy = st.builds(
    simulink::SubSystem,
)

@given(instance=BufferFunction_strategy)
@settings(max_examples=50)
def test_bufferfunction_instantiation(instance):
    assert isinstance(instance, BufferFunction)

@given(instance=simulink::buffer::SharedCheckQueue_strategy)
@settings(max_examples=50)
def test_simulink::buffer::sharedcheckqueue_instantiation(instance):
    assert isinstance(instance, simulink::buffer::SharedCheckQueue)

@given(instance=simulink::buffer::CheckQueue_strategy)
@settings(max_examples=50)
def test_simulink::buffer::checkqueue_instantiation(instance):
    assert isinstance(instance, simulink::buffer::CheckQueue)

@given(instance=simulink::buffer::SharedDequeue_strategy)
@settings(max_examples=50)
def test_simulink::buffer::shareddequeue_instantiation(instance):
    assert isinstance(instance, simulink::buffer::SharedDequeue)

@given(instance=simulink::buffer::SharedEnqueue_strategy)
@settings(max_examples=50)
def test_simulink::buffer::sharedenqueue_instantiation(instance):
    assert isinstance(instance, simulink::buffer::SharedEnqueue)

@given(instance=simulink::buffer::Dequeue_strategy)
@settings(max_examples=50)
def test_simulink::buffer::dequeue_instantiation(instance):
    assert isinstance(instance, simulink::buffer::Dequeue)

@given(instance=simulink::buffer::Enqueue_strategy)
@settings(max_examples=50)
def test_simulink::buffer::enqueue_instantiation(instance):
    assert isinstance(instance, simulink::buffer::Enqueue)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=EmbeddedFunction_strategy)
@settings(max_examples=50)
def test_embeddedfunction_instantiation(instance):
    assert isinstance(instance, EmbeddedFunction)

@given(instance=simulink::buffer::BufferFunction_strategy)
@settings(max_examples=50)
def test_simulink::buffer::bufferfunction_instantiation(instance):
    assert isinstance(instance, simulink::buffer::BufferFunction)

@given(instance=simulink::buffer::BufferFunction_strategy)
def test_simulink::buffer::bufferfunction_bufferSize_type(instance):
    assert isinstance(instance.bufferSize, int)


@given(instance=simulink::buffer::BufferFunction_strategy)
def test_simulink::buffer::bufferfunction_bufferSize_setter(instance):
    original = instance.bufferSize
    instance.bufferSize = original
    assert instance.bufferSize == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=simulink::stateflow::History_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::history_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::History)

@given(instance=simulink::stateflow::Junction_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::junction_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Junction)

@given(instance=simulink::stateflow::State_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::state_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::State)

@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_subStateType_type(instance):
    assert isinstance(instance.subStateType, str)


@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_subStateType_setter(instance):
    original = instance.subStateType
    instance.subStateType = original
    assert instance.subStateType == original

@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::stateflow::State_strategy)
def test_simulink::stateflow::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=simulink::stateflow::Chart_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::chart_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Chart)

@given(instance=stateflow::simulink::SimulinkFile_strategy)
@settings(max_examples=50)
def test_stateflow::simulink::simulinkfile_instantiation(instance):
    assert isinstance(instance, stateflow::simulink::SimulinkFile)

@given(instance=StateflowElement_strategy)
@settings(max_examples=50)
def test_stateflowelement_instantiation(instance):
    assert isinstance(instance, StateflowElement)

@given(instance=simulink::stateflow::Node_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::node_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Node)

@given(instance=simulink::stateflow::Transition_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::transition_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Transition)

@given(instance=simulink::stateflow::Transition_strategy)
def test_simulink::stateflow::transition_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=simulink::stateflow::Transition_strategy)
def test_simulink::stateflow::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=simulink::stateflow::EmbeddedFunction_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::embeddedfunction_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::EmbeddedFunction)

@given(instance=simulink::stateflow::EmbeddedFunction_strategy)
def test_simulink::stateflow::embeddedfunction_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=simulink::stateflow::EmbeddedFunction_strategy)
def test_simulink::stateflow::embeddedfunction_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=simulink::stateflow::EmbeddedFunction_strategy)
def test_simulink::stateflow::embeddedfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::stateflow::EmbeddedFunction_strategy)
def test_simulink::stateflow::embeddedfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::stateflow::Data_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::data_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Data)

@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=simulink::stateflow::Data_strategy)
def test_simulink::stateflow::data_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=simulink::stateflow::Event_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::event_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Event)

@given(instance=simulink::stateflow::Event_strategy)
def test_simulink::stateflow::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::stateflow::Event_strategy)
def test_simulink::stateflow::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::stateflow::Action_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::action_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::Action)

@given(instance=simulink::stateflow::Action_strategy)
def test_simulink::stateflow::action_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=simulink::stateflow::Action_strategy)
def test_simulink::stateflow::action_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=simulink::stateflow::StateflowMachine_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::stateflowmachine_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::StateflowMachine)

@given(instance=InPortBlock_strategy)
@settings(max_examples=50)
def test_inportblock_instantiation(instance):
    assert isinstance(instance, InPortBlock)

@given(instance=simulink::EnablePort_strategy)
@settings(max_examples=50)
def test_simulink::enableport_instantiation(instance):
    assert isinstance(instance, simulink::EnablePort)

@given(instance=simulink::TriggerPort_strategy)
@settings(max_examples=50)
def test_simulink::triggerport_instantiation(instance):
    assert isinstance(instance, simulink::TriggerPort)

@given(instance=simulink::TriggerPort_strategy)
def test_simulink::triggerport_triggerInput_type(instance):
    assert isinstance(instance.triggerInput, str)


@given(instance=simulink::TriggerPort_strategy)
def test_simulink::triggerport_triggerInput_setter(instance):
    original = instance.triggerInput
    instance.triggerInput = original
    assert instance.triggerInput == original

@given(instance=stateflow::simulink::ChartBlock_strategy)
@settings(max_examples=50)
def test_stateflow::simulink::chartblock_instantiation(instance):
    assert isinstance(instance, stateflow::simulink::ChartBlock)

@given(instance=simulink::BusElement_strategy)
@settings(max_examples=50)
def test_simulink::buselement_instantiation(instance):
    assert isinstance(instance, simulink::BusElement)

@given(instance=simulink::BusElement_strategy)
def test_simulink::buselement_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=simulink::BusElement_strategy)
def test_simulink::buselement_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=simulink::BusElement_strategy)
def test_simulink::buselement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::BusElement_strategy)
def test_simulink::buselement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::BusElement_strategy)
def test_simulink::buselement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simulink::BusElement_strategy)
def test_simulink::buselement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Chart_strategy)
@settings(max_examples=50)
def test_chart_instantiation(instance):
    assert isinstance(instance, Chart)

@given(instance=PortBlock_strategy)
@settings(max_examples=50)
def test_portblock_instantiation(instance):
    assert isinstance(instance, PortBlock)

@given(instance=StateflowMachine_strategy)
@settings(max_examples=50)
def test_stateflowmachine_instantiation(instance):
    assert isinstance(instance, StateflowMachine)

@given(instance=SubSystem_strategy)
@settings(max_examples=50)
def test_subsystem_instantiation(instance):
    assert isinstance(instance, SubSystem)

@given(instance=simulink::SimulinkFile_strategy)
@settings(max_examples=50)
def test_simulink::simulinkfile_instantiation(instance):
    assert isinstance(instance, simulink::SimulinkFile)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=simulink::EmbeddedMatlabFunction_strategy)
@settings(max_examples=50)
def test_simulink::embeddedmatlabfunction_instantiation(instance):
    assert isinstance(instance, simulink::EmbeddedMatlabFunction)

@given(instance=simulink::EmbeddedMatlabFunction_strategy)
def test_simulink::embeddedmatlabfunction_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=simulink::EmbeddedMatlabFunction_strategy)
def test_simulink::embeddedmatlabfunction_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=simulink::BusSelector_strategy)
@settings(max_examples=50)
def test_simulink::busselector_instantiation(instance):
    assert isinstance(instance, simulink::BusSelector)

@given(instance=simulink::Constant_strategy)
@settings(max_examples=50)
def test_simulink::constant_instantiation(instance):
    assert isinstance(instance, simulink::Constant)

@given(instance=simulink::Constant_strategy)
def test_simulink::constant_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simulink::Constant_strategy)
def test_simulink::constant_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink::Constant_strategy)
def test_simulink::constant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simulink::Constant_strategy)
def test_simulink::constant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simulink::LibraryReference_strategy)
@settings(max_examples=50)
def test_simulink::libraryreference_instantiation(instance):
    assert isinstance(instance, simulink::LibraryReference)

@given(instance=simulink::ZeroOrderHold_strategy)
@settings(max_examples=50)
def test_simulink::zeroorderhold_instantiation(instance):
    assert isinstance(instance, simulink::ZeroOrderHold)

@given(instance=simulink::ZeroOrderHold_strategy)
def test_simulink::zeroorderhold_sampleTime_type(instance):
    assert isinstance(instance.sampleTime, str)


@given(instance=simulink::ZeroOrderHold_strategy)
def test_simulink::zeroorderhold_sampleTime_setter(instance):
    original = instance.sampleTime
    instance.sampleTime = original
    assert instance.sampleTime == original

@given(instance=simulink::reconfiguration::MultiSourceControl_strategy)
@settings(max_examples=50)
def test_simulink::reconfiguration::multisourcecontrol_instantiation(instance):
    assert isinstance(instance, simulink::reconfiguration::MultiSourceControl)

@given(instance=simulink::MiscBlock_strategy)
@settings(max_examples=50)
def test_simulink::miscblock_instantiation(instance):
    assert isinstance(instance, simulink::MiscBlock)

@given(instance=simulink::MiscBlock_strategy)
def test_simulink::miscblock_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simulink::MiscBlock_strategy)
def test_simulink::miscblock_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink::reconfiguration::MultiTargetControl_strategy)
@settings(max_examples=50)
def test_simulink::reconfiguration::multitargetcontrol_instantiation(instance):
    assert isinstance(instance, simulink::reconfiguration::MultiTargetControl)

@given(instance=simulink::DigitalClock_strategy)
@settings(max_examples=50)
def test_simulink::digitalclock_instantiation(instance):
    assert isinstance(instance, simulink::DigitalClock)

@given(instance=simulink::DigitalClock_strategy)
def test_simulink::digitalclock_sampleTime_type(instance):
    assert isinstance(instance.sampleTime, float)


@given(instance=simulink::DigitalClock_strategy)
def test_simulink::digitalclock_sampleTime_setter(instance):
    original = instance.sampleTime
    instance.sampleTime = original
    assert instance.sampleTime == original

@given(instance=simulink::ChartBlock_strategy)
@settings(max_examples=50)
def test_simulink::chartblock_instantiation(instance):
    assert isinstance(instance, simulink::ChartBlock)

@given(instance=simulink::BusCreator_strategy)
@settings(max_examples=50)
def test_simulink::buscreator_instantiation(instance):
    assert isinstance(instance, simulink::BusCreator)

@given(instance=simulink::msglib::CommunicationSwitch_strategy)
@settings(max_examples=50)
def test_simulink::msglib::communicationswitch_instantiation(instance):
    assert isinstance(instance, simulink::msglib::CommunicationSwitch)

@given(instance=simulink::msglib::CommunicationSwitch_strategy)
def test_simulink::msglib::communicationswitch_debug_type(instance):
    assert isinstance(instance.debug, int)


@given(instance=simulink::msglib::CommunicationSwitch_strategy)
def test_simulink::msglib::communicationswitch_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=simulink::msglib::LinkLayer_strategy)
@settings(max_examples=50)
def test_simulink::msglib::linklayer_instantiation(instance):
    assert isinstance(instance, simulink::msglib::LinkLayer)

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_delayMin_type(instance):
    assert isinstance(instance.delayMin, str)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_delayMin_setter(instance):
    original = instance.delayMin
    instance.delayMin = original
    assert instance.delayMin == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_delayMax_type(instance):
    assert isinstance(instance.delayMax, str)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_delayMax_setter(instance):
    original = instance.delayMax
    instance.delayMax = original
    assert instance.delayMax == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_messageRetransmission_type(instance):
    assert isinstance(instance.messageRetransmission, bool)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_messageRetransmission_setter(instance):
    original = instance.messageRetransmission
    instance.messageRetransmission = original
    assert instance.messageRetransmission == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_bufferOverflowPossible_type(instance):
    assert isinstance(instance.bufferOverflowPossible, bool)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_bufferOverflowPossible_setter(instance):
    original = instance.bufferOverflowPossible
    instance.bufferOverflowPossible = original
    assert instance.bufferOverflowPossible == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_messageLossProbability_type(instance):
    assert isinstance(instance.messageLossProbability, int)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_messageLossProbability_setter(instance):
    original = instance.messageLossProbability
    instance.messageLossProbability = original
    assert instance.messageLossProbability == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_messageMapping_type(instance):
    assert isinstance(instance.messageMapping, str)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_messageMapping_setter(instance):
    original = instance.messageMapping
    instance.messageMapping = original
    assert instance.messageMapping == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_bufferSize_type(instance):
    assert isinstance(instance.bufferSize, int)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_bufferSize_setter(instance):
    original = instance.bufferSize
    instance.bufferSize = original
    assert instance.bufferSize == original

@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_sourceBufferSize_type(instance):
    assert isinstance(instance.sourceBufferSize, int)


@given(instance=simulink::msglib::LinkLayer_strategy)
def test_simulink::msglib::linklayer_sourceBufferSize_setter(instance):
    original = instance.sourceBufferSize
    instance.sourceBufferSize = original
    assert instance.sourceBufferSize == original

@given(instance=simulink::UnitDelay_strategy)
@settings(max_examples=50)
def test_simulink::unitdelay_instantiation(instance):
    assert isinstance(instance, simulink::UnitDelay)

@given(instance=simulink::PortBlock_strategy)
@settings(max_examples=50)
def test_simulink::portblock_instantiation(instance):
    assert isinstance(instance, simulink::PortBlock)

@given(instance=simulink::PortBlock_strategy)
def test_simulink::portblock_initialCondition_type(instance):
    assert isinstance(instance.initialCondition, str)


@given(instance=simulink::PortBlock_strategy)
def test_simulink::portblock_initialCondition_setter(instance):
    original = instance.initialCondition
    instance.initialCondition = original
    assert instance.initialCondition == original

@given(instance=simulink::PortBlock_strategy)
def test_simulink::portblock_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simulink::PortBlock_strategy)
def test_simulink::portblock_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink::PortBlock_strategy)
def test_simulink::portblock_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=simulink::PortBlock_strategy)
def test_simulink::portblock_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=simulink::reconfiguration::FadingComponent_strategy)
@settings(max_examples=50)
def test_simulink::reconfiguration::fadingcomponent_instantiation(instance):
    assert isinstance(instance, simulink::reconfiguration::FadingComponent)

@given(instance=simulink::reconfiguration::FadingComponent_strategy)
def test_simulink::reconfiguration::fadingcomponent_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=simulink::reconfiguration::FadingComponent_strategy)
def test_simulink::reconfiguration::fadingcomponent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=simulink::Parameter_strategy)
@settings(max_examples=50)
def test_simulink::parameter_instantiation(instance):
    assert isinstance(instance, simulink::Parameter)

@given(instance=simulink::Parameter_strategy)
def test_simulink::parameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simulink::Parameter_strategy)
def test_simulink::parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simulink::Parameter_strategy)
def test_simulink::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simulink::Parameter_strategy)
def test_simulink::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink::Parameter_strategy)
def test_simulink::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::Parameter_strategy)
def test_simulink::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::Element_strategy)
@settings(max_examples=50)
def test_simulink::element_instantiation(instance):
    assert isinstance(instance, simulink::Element)

@given(instance=simulink::Element_strategy)
def test_simulink::element_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=simulink::Element_strategy)
def test_simulink::element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimulinkFile_strategy)
@settings(max_examples=50)
def test_simulinkfile_instantiation(instance):
    assert isinstance(instance, SimulinkFile)

@given(instance=simulink::SimulinkLibrary_strategy)
@settings(max_examples=50)
def test_simulink::simulinklibrary_instantiation(instance):
    assert isinstance(instance, simulink::SimulinkLibrary)

@given(instance=simulink::SimulinkModel_strategy)
@settings(max_examples=50)
def test_simulink::simulinkmodel_instantiation(instance):
    assert isinstance(instance, simulink::SimulinkModel)

@given(instance=simulink::InPortBlock_strategy)
@settings(max_examples=50)
def test_simulink::inportblock_instantiation(instance):
    assert isinstance(instance, simulink::InPortBlock)

@given(instance=simulink::OutPortBlock_strategy)
@settings(max_examples=50)
def test_simulink::outportblock_instantiation(instance):
    assert isinstance(instance, simulink::OutPortBlock)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=simulink::stateflow::StateflowElement_strategy)
@settings(max_examples=50)
def test_simulink::stateflow::stateflowelement_instantiation(instance):
    assert isinstance(instance, simulink::stateflow::StateflowElement)

@given(instance=simulink::Bus_strategy)
@settings(max_examples=50)
def test_simulink::bus_instantiation(instance):
    assert isinstance(instance, simulink::Bus)

@given(instance=simulink::Bus_strategy)
def test_simulink::bus_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::Bus_strategy)
def test_simulink::bus_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::SimulinkContainer_strategy)
@settings(max_examples=50)
def test_simulink::simulinkcontainer_instantiation(instance):
    assert isinstance(instance, simulink::SimulinkContainer)

@given(instance=simulink::Line_strategy)
@settings(max_examples=50)
def test_simulink::line_instantiation(instance):
    assert isinstance(instance, simulink::Line)

@given(instance=simulink::Block_strategy)
@settings(max_examples=50)
def test_simulink::block_instantiation(instance):
    assert isinstance(instance, simulink::Block)

@given(instance=simulink::Block_strategy)
def test_simulink::block_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simulink::Block_strategy)
def test_simulink::block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink::SubSystem_strategy)
@settings(max_examples=50)
def test_simulink::subsystem_instantiation(instance):
    assert isinstance(instance, simulink::SubSystem)
