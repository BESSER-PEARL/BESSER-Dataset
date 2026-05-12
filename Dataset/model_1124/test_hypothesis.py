import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BufferFunction,
    simulink_buffer_SharedDequeue,
    simulink_buffer_Dequeue,
    simulink_buffer_SharedEnqueue,
    simulink_buffer_SharedCheckQueue,
    simulink_buffer_CheckQueue,
    simulink_buffer_Enqueue,
    Action,
    EmbeddedFunction,
    simulink_buffer_BufferFunction,
    Event,
    Transition,
    Node,
    simulink_stateflow_Junction,
    simulink_stateflow_History,
    simulink_stateflow_State,
    Data,
    State,
    simulink_stateflow_Chart,
    stateflow_simulink_SimulinkFile,
    StateflowElement,
    simulink_stateflow_Node,
    simulink_stateflow_Transition,
    simulink_stateflow_Data,
    simulink_stateflow_Action,
    simulink_stateflow_EmbeddedFunction,
    simulink_stateflow_Event,
    simulink_stateflow_StateflowMachine,
    InPortBlock,
    simulink_EnablePort,
    simulink_TriggerPort,
    stateflow_simulink_ChartBlock,
    simulink_BusElement,
    Chart,
    PortBlock,
    StateflowMachine,
    SubSystem,
    simulink_SimulinkFile,
    Block,
    simulink_msglib_CommunicationSwitch,
    simulink_ChartBlock,
    simulink_UnitDelay,
    simulink_msglib_LinkLayer,
    simulink_LibraryReference,
    simulink_ZeroOrderHold,
    simulink_MiscBlock,
    simulink_DigitalClock,
    simulink_reconfiguration_FadingComponent,
    simulink_reconfiguration_MultiTargetControl,
    simulink_Constant,
    simulink_BusCreator,
    simulink_EmbeddedMatlabFunction,
    simulink_BusSelector,
    simulink_reconfiguration_MultiSourceControl,
    simulink_PortBlock,
    simulink_Parameter,
    simulink_Element,
    SimulinkFile,
    simulink_SimulinkLibrary,
    simulink_SimulinkModel,
    simulink_InPortBlock,
    simulink_OutPortBlock,
    Element,
    simulink_SimulinkContainer,
    simulink_Bus,
    simulink_Line,
    simulink_stateflow_StateflowElement,
    simulink_Block,
    simulink_SubSystem,
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



def test_simulink_buffer_shareddequeue_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_SharedDequeue)


def test_simulink_buffer_shareddequeue_constructor_exists():
    assert callable(simulink_buffer_SharedDequeue.__init__)


def test_simulink_buffer_shareddequeue_constructor_args():
    sig = inspect.signature(simulink_buffer_SharedDequeue.__init__)
    params = list(sig.parameters.keys())



def test_simulink_buffer_dequeue_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_Dequeue)


def test_simulink_buffer_dequeue_constructor_exists():
    assert callable(simulink_buffer_Dequeue.__init__)


def test_simulink_buffer_dequeue_constructor_args():
    sig = inspect.signature(simulink_buffer_Dequeue.__init__)
    params = list(sig.parameters.keys())



def test_simulink_buffer_sharedenqueue_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_SharedEnqueue)


def test_simulink_buffer_sharedenqueue_constructor_exists():
    assert callable(simulink_buffer_SharedEnqueue.__init__)


def test_simulink_buffer_sharedenqueue_constructor_args():
    sig = inspect.signature(simulink_buffer_SharedEnqueue.__init__)
    params = list(sig.parameters.keys())



def test_simulink_buffer_sharedcheckqueue_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_SharedCheckQueue)


def test_simulink_buffer_sharedcheckqueue_constructor_exists():
    assert callable(simulink_buffer_SharedCheckQueue.__init__)


def test_simulink_buffer_sharedcheckqueue_constructor_args():
    sig = inspect.signature(simulink_buffer_SharedCheckQueue.__init__)
    params = list(sig.parameters.keys())



def test_simulink_buffer_checkqueue_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_CheckQueue)


def test_simulink_buffer_checkqueue_constructor_exists():
    assert callable(simulink_buffer_CheckQueue.__init__)


def test_simulink_buffer_checkqueue_constructor_args():
    sig = inspect.signature(simulink_buffer_CheckQueue.__init__)
    params = list(sig.parameters.keys())



def test_simulink_buffer_enqueue_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_Enqueue)


def test_simulink_buffer_enqueue_constructor_exists():
    assert callable(simulink_buffer_Enqueue.__init__)


def test_simulink_buffer_enqueue_constructor_args():
    sig = inspect.signature(simulink_buffer_Enqueue.__init__)
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



def test_simulink_buffer_bufferfunction_is_not_abstract():
    assert not inspect.isabstract(simulink_buffer_BufferFunction)


def test_simulink_buffer_bufferfunction_constructor_exists():
    assert callable(simulink_buffer_BufferFunction.__init__)


def test_simulink_buffer_bufferfunction_constructor_args():
    sig = inspect.signature(simulink_buffer_BufferFunction.__init__)
    params = list(sig.parameters.keys())
    assert "bufferSize" in params, "Missing parameter 'bufferSize'"

def test_simulink_buffer_bufferfunction_has_bufferSize():
    assert hasattr(simulink_buffer_BufferFunction, "bufferSize")
    descriptor = None
    for klass in simulink_buffer_BufferFunction.__mro__:
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



def test_simulink_stateflow_junction_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Junction)


def test_simulink_stateflow_junction_constructor_exists():
    assert callable(simulink_stateflow_Junction.__init__)


def test_simulink_stateflow_junction_constructor_args():
    sig = inspect.signature(simulink_stateflow_Junction.__init__)
    params = list(sig.parameters.keys())



def test_simulink_stateflow_history_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_History)


def test_simulink_stateflow_history_constructor_exists():
    assert callable(simulink_stateflow_History.__init__)


def test_simulink_stateflow_history_constructor_args():
    sig = inspect.signature(simulink_stateflow_History.__init__)
    params = list(sig.parameters.keys())



def test_simulink_stateflow_state_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_State)


def test_simulink_stateflow_state_constructor_exists():
    assert callable(simulink_stateflow_State.__init__)


def test_simulink_stateflow_state_constructor_args():
    sig = inspect.signature(simulink_stateflow_State.__init__)
    params = list(sig.parameters.keys())
    assert "subStateType" in params, "Missing parameter 'subStateType'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_simulink_stateflow_state_has_subStateType():
    assert hasattr(simulink_stateflow_State, "subStateType")
    descriptor = None
    for klass in simulink_stateflow_State.__mro__:
        if "subStateType" in klass.__dict__:
            descriptor = klass.__dict__["subStateType"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_state_has_initial():
    assert hasattr(simulink_stateflow_State, "initial")
    descriptor = None
    for klass in simulink_stateflow_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_state_has_name():
    assert hasattr(simulink_stateflow_State, "name")
    descriptor = None
    for klass in simulink_stateflow_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_state_has_priority():
    assert hasattr(simulink_stateflow_State, "priority")
    descriptor = None
    for klass in simulink_stateflow_State.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
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



def test_simulink_stateflow_chart_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Chart)


def test_simulink_stateflow_chart_constructor_exists():
    assert callable(simulink_stateflow_Chart.__init__)


def test_simulink_stateflow_chart_constructor_args():
    sig = inspect.signature(simulink_stateflow_Chart.__init__)
    params = list(sig.parameters.keys())



def test_stateflow_simulink_simulinkfile_is_not_abstract():
    assert not inspect.isabstract(stateflow_simulink_SimulinkFile)


def test_stateflow_simulink_simulinkfile_constructor_exists():
    assert callable(stateflow_simulink_SimulinkFile.__init__)


def test_stateflow_simulink_simulinkfile_constructor_args():
    sig = inspect.signature(stateflow_simulink_SimulinkFile.__init__)
    params = list(sig.parameters.keys())



def test_stateflowelement_is_not_abstract():
    assert not inspect.isabstract(StateflowElement)


def test_stateflowelement_constructor_exists():
    assert callable(StateflowElement.__init__)


def test_stateflowelement_constructor_args():
    sig = inspect.signature(StateflowElement.__init__)
    params = list(sig.parameters.keys())



def test_simulink_stateflow_node_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Node)


def test_simulink_stateflow_node_constructor_exists():
    assert callable(simulink_stateflow_Node.__init__)


def test_simulink_stateflow_node_constructor_args():
    sig = inspect.signature(simulink_stateflow_Node.__init__)
    params = list(sig.parameters.keys())



def test_simulink_stateflow_transition_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Transition)


def test_simulink_stateflow_transition_constructor_exists():
    assert callable(simulink_stateflow_Transition.__init__)


def test_simulink_stateflow_transition_constructor_args():
    sig = inspect.signature(simulink_stateflow_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_simulink_stateflow_transition_has_priority():
    assert hasattr(simulink_stateflow_Transition, "priority")
    descriptor = None
    for klass in simulink_stateflow_Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_simulink_stateflow_data_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Data)


def test_simulink_stateflow_data_constructor_exists():
    assert callable(simulink_stateflow_Data.__init__)


def test_simulink_stateflow_data_constructor_args():
    sig = inspect.signature(simulink_stateflow_Data.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_simulink_stateflow_data_has_type():
    assert hasattr(simulink_stateflow_Data, "type")
    descriptor = None
    for klass in simulink_stateflow_Data.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_data_has_size():
    assert hasattr(simulink_stateflow_Data, "size")
    descriptor = None
    for klass in simulink_stateflow_Data.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_data_has_name():
    assert hasattr(simulink_stateflow_Data, "name")
    descriptor = None
    for klass in simulink_stateflow_Data.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_data_has_value():
    assert hasattr(simulink_stateflow_Data, "value")
    descriptor = None
    for klass in simulink_stateflow_Data.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simulink_stateflow_action_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Action)


def test_simulink_stateflow_action_constructor_exists():
    assert callable(simulink_stateflow_Action.__init__)


def test_simulink_stateflow_action_constructor_args():
    sig = inspect.signature(simulink_stateflow_Action.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_simulink_stateflow_action_has_expression():
    assert hasattr(simulink_stateflow_Action, "expression")
    descriptor = None
    for klass in simulink_stateflow_Action.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_simulink_stateflow_embeddedfunction_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_EmbeddedFunction)


def test_simulink_stateflow_embeddedfunction_constructor_exists():
    assert callable(simulink_stateflow_EmbeddedFunction.__init__)


def test_simulink_stateflow_embeddedfunction_constructor_args():
    sig = inspect.signature(simulink_stateflow_EmbeddedFunction.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_simulink_stateflow_embeddedfunction_has_code():
    assert hasattr(simulink_stateflow_EmbeddedFunction, "code")
    descriptor = None
    for klass in simulink_stateflow_EmbeddedFunction.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_simulink_stateflow_embeddedfunction_has_name():
    assert hasattr(simulink_stateflow_EmbeddedFunction, "name")
    descriptor = None
    for klass in simulink_stateflow_EmbeddedFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink_stateflow_event_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_Event)


def test_simulink_stateflow_event_constructor_exists():
    assert callable(simulink_stateflow_Event.__init__)


def test_simulink_stateflow_event_constructor_args():
    sig = inspect.signature(simulink_stateflow_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simulink_stateflow_event_has_name():
    assert hasattr(simulink_stateflow_Event, "name")
    descriptor = None
    for klass in simulink_stateflow_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink_stateflow_stateflowmachine_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_StateflowMachine)


def test_simulink_stateflow_stateflowmachine_constructor_exists():
    assert callable(simulink_stateflow_StateflowMachine.__init__)


def test_simulink_stateflow_stateflowmachine_constructor_args():
    sig = inspect.signature(simulink_stateflow_StateflowMachine.__init__)
    params = list(sig.parameters.keys())



def test_inportblock_is_not_abstract():
    assert not inspect.isabstract(InPortBlock)


def test_inportblock_constructor_exists():
    assert callable(InPortBlock.__init__)


def test_inportblock_constructor_args():
    sig = inspect.signature(InPortBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink_enableport_is_not_abstract():
    assert not inspect.isabstract(simulink_EnablePort)


def test_simulink_enableport_constructor_exists():
    assert callable(simulink_EnablePort.__init__)


def test_simulink_enableport_constructor_args():
    sig = inspect.signature(simulink_EnablePort.__init__)
    params = list(sig.parameters.keys())



def test_simulink_triggerport_is_not_abstract():
    assert not inspect.isabstract(simulink_TriggerPort)


def test_simulink_triggerport_constructor_exists():
    assert callable(simulink_TriggerPort.__init__)


def test_simulink_triggerport_constructor_args():
    sig = inspect.signature(simulink_TriggerPort.__init__)
    params = list(sig.parameters.keys())
    assert "triggerInput" in params, "Missing parameter 'triggerInput'"

def test_simulink_triggerport_has_triggerInput():
    assert hasattr(simulink_TriggerPort, "triggerInput")
    descriptor = None
    for klass in simulink_TriggerPort.__mro__:
        if "triggerInput" in klass.__dict__:
            descriptor = klass.__dict__["triggerInput"]
            break
    assert isinstance(descriptor, property)



def test_stateflow_simulink_chartblock_is_not_abstract():
    assert not inspect.isabstract(stateflow_simulink_ChartBlock)


def test_stateflow_simulink_chartblock_constructor_exists():
    assert callable(stateflow_simulink_ChartBlock.__init__)


def test_stateflow_simulink_chartblock_constructor_args():
    sig = inspect.signature(stateflow_simulink_ChartBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink_buselement_is_not_abstract():
    assert not inspect.isabstract(simulink_BusElement)


def test_simulink_buselement_constructor_exists():
    assert callable(simulink_BusElement.__init__)


def test_simulink_buselement_constructor_args():
    sig = inspect.signature(simulink_BusElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_simulink_buselement_has_type():
    assert hasattr(simulink_BusElement, "type")
    descriptor = None
    for klass in simulink_BusElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink_buselement_has_name():
    assert hasattr(simulink_BusElement, "name")
    descriptor = None
    for klass in simulink_BusElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simulink_buselement_has_dimensions():
    assert hasattr(simulink_BusElement, "dimensions")
    descriptor = None
    for klass in simulink_BusElement.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
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



def test_simulink_simulinkfile_is_not_abstract():
    assert not inspect.isabstract(simulink_SimulinkFile)


def test_simulink_simulinkfile_constructor_exists():
    assert callable(simulink_SimulinkFile.__init__)


def test_simulink_simulinkfile_constructor_args():
    sig = inspect.signature(simulink_SimulinkFile.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_simulink_msglib_communicationswitch_is_not_abstract():
    assert not inspect.isabstract(simulink_msglib_CommunicationSwitch)


def test_simulink_msglib_communicationswitch_constructor_exists():
    assert callable(simulink_msglib_CommunicationSwitch.__init__)


def test_simulink_msglib_communicationswitch_constructor_args():
    sig = inspect.signature(simulink_msglib_CommunicationSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"

def test_simulink_msglib_communicationswitch_has_debug():
    assert hasattr(simulink_msglib_CommunicationSwitch, "debug")
    descriptor = None
    for klass in simulink_msglib_CommunicationSwitch.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_simulink_chartblock_is_not_abstract():
    assert not inspect.isabstract(simulink_ChartBlock)


def test_simulink_chartblock_constructor_exists():
    assert callable(simulink_ChartBlock.__init__)


def test_simulink_chartblock_constructor_args():
    sig = inspect.signature(simulink_ChartBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink_unitdelay_is_not_abstract():
    assert not inspect.isabstract(simulink_UnitDelay)


def test_simulink_unitdelay_constructor_exists():
    assert callable(simulink_UnitDelay.__init__)


def test_simulink_unitdelay_constructor_args():
    sig = inspect.signature(simulink_UnitDelay.__init__)
    params = list(sig.parameters.keys())



def test_simulink_msglib_linklayer_is_not_abstract():
    assert not inspect.isabstract(simulink_msglib_LinkLayer)


def test_simulink_msglib_linklayer_constructor_exists():
    assert callable(simulink_msglib_LinkLayer.__init__)


def test_simulink_msglib_linklayer_constructor_args():
    sig = inspect.signature(simulink_msglib_LinkLayer.__init__)
    params = list(sig.parameters.keys())
    assert "messageMapping" in params, "Missing parameter 'messageMapping'"
    assert "messageLossProbability" in params, "Missing parameter 'messageLossProbability'"
    assert "bufferOverflowPossible" in params, "Missing parameter 'bufferOverflowPossible'"
    assert "delayMax" in params, "Missing parameter 'delayMax'"
    assert "messageRetransmission" in params, "Missing parameter 'messageRetransmission'"
    assert "sourceBufferSize" in params, "Missing parameter 'sourceBufferSize'"
    assert "delayMin" in params, "Missing parameter 'delayMin'"
    assert "bufferSize" in params, "Missing parameter 'bufferSize'"

def test_simulink_msglib_linklayer_has_messageMapping():
    assert hasattr(simulink_msglib_LinkLayer, "messageMapping")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "messageMapping" in klass.__dict__:
            descriptor = klass.__dict__["messageMapping"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_messageLossProbability():
    assert hasattr(simulink_msglib_LinkLayer, "messageLossProbability")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "messageLossProbability" in klass.__dict__:
            descriptor = klass.__dict__["messageLossProbability"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_bufferOverflowPossible():
    assert hasattr(simulink_msglib_LinkLayer, "bufferOverflowPossible")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "bufferOverflowPossible" in klass.__dict__:
            descriptor = klass.__dict__["bufferOverflowPossible"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_delayMax():
    assert hasattr(simulink_msglib_LinkLayer, "delayMax")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "delayMax" in klass.__dict__:
            descriptor = klass.__dict__["delayMax"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_messageRetransmission():
    assert hasattr(simulink_msglib_LinkLayer, "messageRetransmission")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "messageRetransmission" in klass.__dict__:
            descriptor = klass.__dict__["messageRetransmission"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_sourceBufferSize():
    assert hasattr(simulink_msglib_LinkLayer, "sourceBufferSize")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "sourceBufferSize" in klass.__dict__:
            descriptor = klass.__dict__["sourceBufferSize"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_delayMin():
    assert hasattr(simulink_msglib_LinkLayer, "delayMin")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "delayMin" in klass.__dict__:
            descriptor = klass.__dict__["delayMin"]
            break
    assert isinstance(descriptor, property)

def test_simulink_msglib_linklayer_has_bufferSize():
    assert hasattr(simulink_msglib_LinkLayer, "bufferSize")
    descriptor = None
    for klass in simulink_msglib_LinkLayer.__mro__:
        if "bufferSize" in klass.__dict__:
            descriptor = klass.__dict__["bufferSize"]
            break
    assert isinstance(descriptor, property)



def test_simulink_libraryreference_is_not_abstract():
    assert not inspect.isabstract(simulink_LibraryReference)


def test_simulink_libraryreference_constructor_exists():
    assert callable(simulink_LibraryReference.__init__)


def test_simulink_libraryreference_constructor_args():
    sig = inspect.signature(simulink_LibraryReference.__init__)
    params = list(sig.parameters.keys())



def test_simulink_zeroorderhold_is_not_abstract():
    assert not inspect.isabstract(simulink_ZeroOrderHold)


def test_simulink_zeroorderhold_constructor_exists():
    assert callable(simulink_ZeroOrderHold.__init__)


def test_simulink_zeroorderhold_constructor_args():
    sig = inspect.signature(simulink_ZeroOrderHold.__init__)
    params = list(sig.parameters.keys())
    assert "sampleTime" in params, "Missing parameter 'sampleTime'"

def test_simulink_zeroorderhold_has_sampleTime():
    assert hasattr(simulink_ZeroOrderHold, "sampleTime")
    descriptor = None
    for klass in simulink_ZeroOrderHold.__mro__:
        if "sampleTime" in klass.__dict__:
            descriptor = klass.__dict__["sampleTime"]
            break
    assert isinstance(descriptor, property)



def test_simulink_miscblock_is_not_abstract():
    assert not inspect.isabstract(simulink_MiscBlock)


def test_simulink_miscblock_constructor_exists():
    assert callable(simulink_MiscBlock.__init__)


def test_simulink_miscblock_constructor_args():
    sig = inspect.signature(simulink_MiscBlock.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simulink_miscblock_has_type():
    assert hasattr(simulink_MiscBlock, "type")
    descriptor = None
    for klass in simulink_MiscBlock.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simulink_digitalclock_is_not_abstract():
    assert not inspect.isabstract(simulink_DigitalClock)


def test_simulink_digitalclock_constructor_exists():
    assert callable(simulink_DigitalClock.__init__)


def test_simulink_digitalclock_constructor_args():
    sig = inspect.signature(simulink_DigitalClock.__init__)
    params = list(sig.parameters.keys())
    assert "sampleTime" in params, "Missing parameter 'sampleTime'"

def test_simulink_digitalclock_has_sampleTime():
    assert hasattr(simulink_DigitalClock, "sampleTime")
    descriptor = None
    for klass in simulink_DigitalClock.__mro__:
        if "sampleTime" in klass.__dict__:
            descriptor = klass.__dict__["sampleTime"]
            break
    assert isinstance(descriptor, property)



def test_simulink_reconfiguration_fadingcomponent_is_not_abstract():
    assert not inspect.isabstract(simulink_reconfiguration_FadingComponent)


def test_simulink_reconfiguration_fadingcomponent_constructor_exists():
    assert callable(simulink_reconfiguration_FadingComponent.__init__)


def test_simulink_reconfiguration_fadingcomponent_constructor_args():
    sig = inspect.signature(simulink_reconfiguration_FadingComponent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_simulink_reconfiguration_fadingcomponent_has_time():
    assert hasattr(simulink_reconfiguration_FadingComponent, "time")
    descriptor = None
    for klass in simulink_reconfiguration_FadingComponent.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_simulink_reconfiguration_multitargetcontrol_is_not_abstract():
    assert not inspect.isabstract(simulink_reconfiguration_MultiTargetControl)


def test_simulink_reconfiguration_multitargetcontrol_constructor_exists():
    assert callable(simulink_reconfiguration_MultiTargetControl.__init__)


def test_simulink_reconfiguration_multitargetcontrol_constructor_args():
    sig = inspect.signature(simulink_reconfiguration_MultiTargetControl.__init__)
    params = list(sig.parameters.keys())



def test_simulink_constant_is_not_abstract():
    assert not inspect.isabstract(simulink_Constant)


def test_simulink_constant_constructor_exists():
    assert callable(simulink_Constant.__init__)


def test_simulink_constant_constructor_args():
    sig = inspect.signature(simulink_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_simulink_constant_has_value():
    assert hasattr(simulink_Constant, "value")
    descriptor = None
    for klass in simulink_Constant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_simulink_constant_has_type():
    assert hasattr(simulink_Constant, "type")
    descriptor = None
    for klass in simulink_Constant.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simulink_buscreator_is_not_abstract():
    assert not inspect.isabstract(simulink_BusCreator)


def test_simulink_buscreator_constructor_exists():
    assert callable(simulink_BusCreator.__init__)


def test_simulink_buscreator_constructor_args():
    sig = inspect.signature(simulink_BusCreator.__init__)
    params = list(sig.parameters.keys())



def test_simulink_embeddedmatlabfunction_is_not_abstract():
    assert not inspect.isabstract(simulink_EmbeddedMatlabFunction)


def test_simulink_embeddedmatlabfunction_constructor_exists():
    assert callable(simulink_EmbeddedMatlabFunction.__init__)


def test_simulink_embeddedmatlabfunction_constructor_args():
    sig = inspect.signature(simulink_EmbeddedMatlabFunction.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_simulink_embeddedmatlabfunction_has_code():
    assert hasattr(simulink_EmbeddedMatlabFunction, "code")
    descriptor = None
    for klass in simulink_EmbeddedMatlabFunction.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_simulink_busselector_is_not_abstract():
    assert not inspect.isabstract(simulink_BusSelector)


def test_simulink_busselector_constructor_exists():
    assert callable(simulink_BusSelector.__init__)


def test_simulink_busselector_constructor_args():
    sig = inspect.signature(simulink_BusSelector.__init__)
    params = list(sig.parameters.keys())



def test_simulink_reconfiguration_multisourcecontrol_is_not_abstract():
    assert not inspect.isabstract(simulink_reconfiguration_MultiSourceControl)


def test_simulink_reconfiguration_multisourcecontrol_constructor_exists():
    assert callable(simulink_reconfiguration_MultiSourceControl.__init__)


def test_simulink_reconfiguration_multisourcecontrol_constructor_args():
    sig = inspect.signature(simulink_reconfiguration_MultiSourceControl.__init__)
    params = list(sig.parameters.keys())



def test_simulink_portblock_is_not_abstract():
    assert not inspect.isabstract(simulink_PortBlock)


def test_simulink_portblock_constructor_exists():
    assert callable(simulink_PortBlock.__init__)


def test_simulink_portblock_constructor_args():
    sig = inspect.signature(simulink_PortBlock.__init__)
    params = list(sig.parameters.keys())
    assert "initialCondition" in params, "Missing parameter 'initialCondition'"
    assert "type" in params, "Missing parameter 'type'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_simulink_portblock_has_initialCondition():
    assert hasattr(simulink_PortBlock, "initialCondition")
    descriptor = None
    for klass in simulink_PortBlock.__mro__:
        if "initialCondition" in klass.__dict__:
            descriptor = klass.__dict__["initialCondition"]
            break
    assert isinstance(descriptor, property)

def test_simulink_portblock_has_type():
    assert hasattr(simulink_PortBlock, "type")
    descriptor = None
    for klass in simulink_PortBlock.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink_portblock_has_dimensions():
    assert hasattr(simulink_PortBlock, "dimensions")
    descriptor = None
    for klass in simulink_PortBlock.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_simulink_parameter_is_not_abstract():
    assert not inspect.isabstract(simulink_Parameter)


def test_simulink_parameter_constructor_exists():
    assert callable(simulink_Parameter.__init__)


def test_simulink_parameter_constructor_args():
    sig = inspect.signature(simulink_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_simulink_parameter_has_name():
    assert hasattr(simulink_Parameter, "name")
    descriptor = None
    for klass in simulink_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simulink_parameter_has_type():
    assert hasattr(simulink_Parameter, "type")
    descriptor = None
    for klass in simulink_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simulink_parameter_has_value():
    assert hasattr(simulink_Parameter, "value")
    descriptor = None
    for klass in simulink_Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simulink_element_is_not_abstract():
    assert not inspect.isabstract(simulink_Element)


def test_simulink_element_constructor_exists():
    assert callable(simulink_Element.__init__)


def test_simulink_element_constructor_args():
    sig = inspect.signature(simulink_Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simulink_element_has_id():
    assert hasattr(simulink_Element, "id")
    descriptor = None
    for klass in simulink_Element.__mro__:
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



def test_simulink_simulinklibrary_is_not_abstract():
    assert not inspect.isabstract(simulink_SimulinkLibrary)


def test_simulink_simulinklibrary_constructor_exists():
    assert callable(simulink_SimulinkLibrary.__init__)


def test_simulink_simulinklibrary_constructor_args():
    sig = inspect.signature(simulink_SimulinkLibrary.__init__)
    params = list(sig.parameters.keys())



def test_simulink_simulinkmodel_is_not_abstract():
    assert not inspect.isabstract(simulink_SimulinkModel)


def test_simulink_simulinkmodel_constructor_exists():
    assert callable(simulink_SimulinkModel.__init__)


def test_simulink_simulinkmodel_constructor_args():
    sig = inspect.signature(simulink_SimulinkModel.__init__)
    params = list(sig.parameters.keys())



def test_simulink_inportblock_is_not_abstract():
    assert not inspect.isabstract(simulink_InPortBlock)


def test_simulink_inportblock_constructor_exists():
    assert callable(simulink_InPortBlock.__init__)


def test_simulink_inportblock_constructor_args():
    sig = inspect.signature(simulink_InPortBlock.__init__)
    params = list(sig.parameters.keys())



def test_simulink_outportblock_is_not_abstract():
    assert not inspect.isabstract(simulink_OutPortBlock)


def test_simulink_outportblock_constructor_exists():
    assert callable(simulink_OutPortBlock.__init__)


def test_simulink_outportblock_constructor_args():
    sig = inspect.signature(simulink_OutPortBlock.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_simulink_simulinkcontainer_is_not_abstract():
    assert not inspect.isabstract(simulink_SimulinkContainer)


def test_simulink_simulinkcontainer_constructor_exists():
    assert callable(simulink_SimulinkContainer.__init__)


def test_simulink_simulinkcontainer_constructor_args():
    sig = inspect.signature(simulink_SimulinkContainer.__init__)
    params = list(sig.parameters.keys())



def test_simulink_bus_is_not_abstract():
    assert not inspect.isabstract(simulink_Bus)


def test_simulink_bus_constructor_exists():
    assert callable(simulink_Bus.__init__)


def test_simulink_bus_constructor_args():
    sig = inspect.signature(simulink_Bus.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simulink_bus_has_name():
    assert hasattr(simulink_Bus, "name")
    descriptor = None
    for klass in simulink_Bus.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink_line_is_not_abstract():
    assert not inspect.isabstract(simulink_Line)


def test_simulink_line_constructor_exists():
    assert callable(simulink_Line.__init__)


def test_simulink_line_constructor_args():
    sig = inspect.signature(simulink_Line.__init__)
    params = list(sig.parameters.keys())



def test_simulink_stateflow_stateflowelement_is_not_abstract():
    assert not inspect.isabstract(simulink_stateflow_StateflowElement)


def test_simulink_stateflow_stateflowelement_constructor_exists():
    assert callable(simulink_stateflow_StateflowElement.__init__)


def test_simulink_stateflow_stateflowelement_constructor_args():
    sig = inspect.signature(simulink_stateflow_StateflowElement.__init__)
    params = list(sig.parameters.keys())



def test_simulink_block_is_not_abstract():
    assert not inspect.isabstract(simulink_Block)


def test_simulink_block_constructor_exists():
    assert callable(simulink_Block.__init__)


def test_simulink_block_constructor_args():
    sig = inspect.signature(simulink_Block.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simulink_block_has_name():
    assert hasattr(simulink_Block, "name")
    descriptor = None
    for klass in simulink_Block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simulink_subsystem_is_not_abstract():
    assert not inspect.isabstract(simulink_SubSystem)


def test_simulink_subsystem_constructor_exists():
    assert callable(simulink_SubSystem.__init__)


def test_simulink_subsystem_constructor_args():
    sig = inspect.signature(simulink_SubSystem.__init__)
    params = list(sig.parameters.keys())

def test_substatetype_exists():
    # Check that the Enumeration exists
    assert SubStateType is not None

def test_substatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubStateType]
    expected_literals = [
        "EXCLUSIVE",
        "PARALLEL",
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
        "Falling",
        "Either",
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
        "INT32",
        "INT8",
        "BUS",
        "UINT16",
        "SINGLE",
        "UINT32",
        "INT16",
        "BOOLEAN",
        "INHERIT",
        "UINT8",
        "DOUBLE",
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
simulink_buffer_SharedDequeue_strategy = st.builds(
    simulink_buffer_SharedDequeue,
)
simulink_buffer_Dequeue_strategy = st.builds(
    simulink_buffer_Dequeue,
)
simulink_buffer_SharedEnqueue_strategy = st.builds(
    simulink_buffer_SharedEnqueue,
)
simulink_buffer_SharedCheckQueue_strategy = st.builds(
    simulink_buffer_SharedCheckQueue,
)
simulink_buffer_CheckQueue_strategy = st.builds(
    simulink_buffer_CheckQueue,
)
simulink_buffer_Enqueue_strategy = st.builds(
    simulink_buffer_Enqueue,
)
Action_strategy = st.builds(
    Action,
)
EmbeddedFunction_strategy = st.builds(
    EmbeddedFunction,
)
simulink_buffer_BufferFunction_strategy = st.builds(
    simulink_buffer_BufferFunction,
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
simulink_stateflow_Junction_strategy = st.builds(
    simulink_stateflow_Junction,
)
simulink_stateflow_History_strategy = st.builds(
    simulink_stateflow_History,
)
simulink_stateflow_State_strategy = st.builds(
    simulink_stateflow_State,
    subStateType=
        safe_text,
    initial=
        st.booleans(),
    name=
        safe_text,
    priority=
        st.integers()
)
Data_strategy = st.builds(
    Data,
)
State_strategy = st.builds(
    State,
)
simulink_stateflow_Chart_strategy = st.builds(
    simulink_stateflow_Chart,
)
stateflow_simulink_SimulinkFile_strategy = st.builds(
    stateflow_simulink_SimulinkFile,
)
StateflowElement_strategy = st.builds(
    StateflowElement,
)
simulink_stateflow_Node_strategy = st.builds(
    simulink_stateflow_Node,
)
simulink_stateflow_Transition_strategy = st.builds(
    simulink_stateflow_Transition,
    priority=
        st.integers()
)
simulink_stateflow_Data_strategy = st.builds(
    simulink_stateflow_Data,
    type=
        safe_text,
    size=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
simulink_stateflow_Action_strategy = st.builds(
    simulink_stateflow_Action,
    expression=
        safe_text
)
simulink_stateflow_EmbeddedFunction_strategy = st.builds(
    simulink_stateflow_EmbeddedFunction,
    code=
        safe_text,
    name=
        safe_text
)
simulink_stateflow_Event_strategy = st.builds(
    simulink_stateflow_Event,
    name=
        safe_text
)
simulink_stateflow_StateflowMachine_strategy = st.builds(
    simulink_stateflow_StateflowMachine,
)
InPortBlock_strategy = st.builds(
    InPortBlock,
)
simulink_EnablePort_strategy = st.builds(
    simulink_EnablePort,
)
simulink_TriggerPort_strategy = st.builds(
    simulink_TriggerPort,
    triggerInput=
        safe_text
)
stateflow_simulink_ChartBlock_strategy = st.builds(
    stateflow_simulink_ChartBlock,
)
simulink_BusElement_strategy = st.builds(
    simulink_BusElement,
    type=
        safe_text,
    name=
        safe_text,
    dimensions=
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
simulink_SimulinkFile_strategy = st.builds(
    simulink_SimulinkFile,
)
Block_strategy = st.builds(
    Block,
)
simulink_msglib_CommunicationSwitch_strategy = st.builds(
    simulink_msglib_CommunicationSwitch,
    debug=
        st.integers()
)
simulink_ChartBlock_strategy = st.builds(
    simulink_ChartBlock,
)
simulink_UnitDelay_strategy = st.builds(
    simulink_UnitDelay,
)
simulink_msglib_LinkLayer_strategy = st.builds(
    simulink_msglib_LinkLayer,
    messageMapping=
        safe_text,
    messageLossProbability=
        st.integers(),
    bufferOverflowPossible=
        st.booleans(),
    delayMax=
        safe_text,
    messageRetransmission=
        st.booleans(),
    sourceBufferSize=
        st.integers(),
    delayMin=
        safe_text,
    bufferSize=
        st.integers()
)
simulink_LibraryReference_strategy = st.builds(
    simulink_LibraryReference,
)
simulink_ZeroOrderHold_strategy = st.builds(
    simulink_ZeroOrderHold,
    sampleTime=
        safe_text
)
simulink_MiscBlock_strategy = st.builds(
    simulink_MiscBlock,
    type=
        safe_text
)
simulink_DigitalClock_strategy = st.builds(
    simulink_DigitalClock,
    sampleTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
simulink_reconfiguration_FadingComponent_strategy = st.builds(
    simulink_reconfiguration_FadingComponent,
    time=
        st.integers()
)
simulink_reconfiguration_MultiTargetControl_strategy = st.builds(
    simulink_reconfiguration_MultiTargetControl,
)
simulink_Constant_strategy = st.builds(
    simulink_Constant,
    value=
        safe_text,
    type=
        safe_text
)
simulink_BusCreator_strategy = st.builds(
    simulink_BusCreator,
)
simulink_EmbeddedMatlabFunction_strategy = st.builds(
    simulink_EmbeddedMatlabFunction,
    code=
        safe_text
)
simulink_BusSelector_strategy = st.builds(
    simulink_BusSelector,
)
simulink_reconfiguration_MultiSourceControl_strategy = st.builds(
    simulink_reconfiguration_MultiSourceControl,
)
simulink_PortBlock_strategy = st.builds(
    simulink_PortBlock,
    initialCondition=
        safe_text,
    type=
        safe_text,
    dimensions=
        safe_text
)
simulink_Parameter_strategy = st.builds(
    simulink_Parameter,
    name=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
simulink_Element_strategy = st.builds(
    simulink_Element,
    id=
        safe_text
)
SimulinkFile_strategy = st.builds(
    SimulinkFile,
)
simulink_SimulinkLibrary_strategy = st.builds(
    simulink_SimulinkLibrary,
)
simulink_SimulinkModel_strategy = st.builds(
    simulink_SimulinkModel,
)
simulink_InPortBlock_strategy = st.builds(
    simulink_InPortBlock,
)
simulink_OutPortBlock_strategy = st.builds(
    simulink_OutPortBlock,
)
Element_strategy = st.builds(
    Element,
)
simulink_SimulinkContainer_strategy = st.builds(
    simulink_SimulinkContainer,
)
simulink_Bus_strategy = st.builds(
    simulink_Bus,
    name=
        safe_text
)
simulink_Line_strategy = st.builds(
    simulink_Line,
)
simulink_stateflow_StateflowElement_strategy = st.builds(
    simulink_stateflow_StateflowElement,
)
simulink_Block_strategy = st.builds(
    simulink_Block,
    name=
        safe_text
)
simulink_SubSystem_strategy = st.builds(
    simulink_SubSystem,
)

@given(instance=BufferFunction_strategy)
@settings(max_examples=50)
def test_bufferfunction_instantiation(instance):
    assert isinstance(instance, BufferFunction)

@given(instance=simulink_buffer_SharedDequeue_strategy)
@settings(max_examples=50)
def test_simulink_buffer_shareddequeue_instantiation(instance):
    assert isinstance(instance, simulink_buffer_SharedDequeue)

@given(instance=simulink_buffer_Dequeue_strategy)
@settings(max_examples=50)
def test_simulink_buffer_dequeue_instantiation(instance):
    assert isinstance(instance, simulink_buffer_Dequeue)

@given(instance=simulink_buffer_SharedEnqueue_strategy)
@settings(max_examples=50)
def test_simulink_buffer_sharedenqueue_instantiation(instance):
    assert isinstance(instance, simulink_buffer_SharedEnqueue)

@given(instance=simulink_buffer_SharedCheckQueue_strategy)
@settings(max_examples=50)
def test_simulink_buffer_sharedcheckqueue_instantiation(instance):
    assert isinstance(instance, simulink_buffer_SharedCheckQueue)

@given(instance=simulink_buffer_CheckQueue_strategy)
@settings(max_examples=50)
def test_simulink_buffer_checkqueue_instantiation(instance):
    assert isinstance(instance, simulink_buffer_CheckQueue)

@given(instance=simulink_buffer_Enqueue_strategy)
@settings(max_examples=50)
def test_simulink_buffer_enqueue_instantiation(instance):
    assert isinstance(instance, simulink_buffer_Enqueue)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=EmbeddedFunction_strategy)
@settings(max_examples=50)
def test_embeddedfunction_instantiation(instance):
    assert isinstance(instance, EmbeddedFunction)

@given(instance=simulink_buffer_BufferFunction_strategy)
@settings(max_examples=50)
def test_simulink_buffer_bufferfunction_instantiation(instance):
    assert isinstance(instance, simulink_buffer_BufferFunction)



@given(instance=simulink_buffer_BufferFunction_strategy)
def test_simulink_buffer_bufferfunction_bufferSize_setter(instance):
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

@given(instance=simulink_stateflow_Junction_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_junction_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Junction)

@given(instance=simulink_stateflow_History_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_history_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_History)

@given(instance=simulink_stateflow_State_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_state_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_State)



@given(instance=simulink_stateflow_State_strategy)
def test_simulink_stateflow_state_subStateType_setter(instance):
    original = instance.subStateType
    instance.subStateType = original
    assert instance.subStateType == original



@given(instance=simulink_stateflow_State_strategy)
def test_simulink_stateflow_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=simulink_stateflow_State_strategy)
def test_simulink_stateflow_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simulink_stateflow_State_strategy)
def test_simulink_stateflow_state_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=simulink_stateflow_Chart_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_chart_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Chart)

@given(instance=stateflow_simulink_SimulinkFile_strategy)
@settings(max_examples=50)
def test_stateflow_simulink_simulinkfile_instantiation(instance):
    assert isinstance(instance, stateflow_simulink_SimulinkFile)

@given(instance=StateflowElement_strategy)
@settings(max_examples=50)
def test_stateflowelement_instantiation(instance):
    assert isinstance(instance, StateflowElement)

@given(instance=simulink_stateflow_Node_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_node_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Node)

@given(instance=simulink_stateflow_Transition_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_transition_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Transition)



@given(instance=simulink_stateflow_Transition_strategy)
def test_simulink_stateflow_transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=simulink_stateflow_Data_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_data_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Data)



@given(instance=simulink_stateflow_Data_strategy)
def test_simulink_stateflow_data_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=simulink_stateflow_Data_strategy)
def test_simulink_stateflow_data_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=simulink_stateflow_Data_strategy)
def test_simulink_stateflow_data_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simulink_stateflow_Data_strategy)
def test_simulink_stateflow_data_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simulink_stateflow_Action_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_action_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Action)



@given(instance=simulink_stateflow_Action_strategy)
def test_simulink_stateflow_action_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=simulink_stateflow_EmbeddedFunction_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_embeddedfunction_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_EmbeddedFunction)



@given(instance=simulink_stateflow_EmbeddedFunction_strategy)
def test_simulink_stateflow_embeddedfunction_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=simulink_stateflow_EmbeddedFunction_strategy)
def test_simulink_stateflow_embeddedfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink_stateflow_Event_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_event_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_Event)



@given(instance=simulink_stateflow_Event_strategy)
def test_simulink_stateflow_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink_stateflow_StateflowMachine_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_stateflowmachine_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_StateflowMachine)

@given(instance=InPortBlock_strategy)
@settings(max_examples=50)
def test_inportblock_instantiation(instance):
    assert isinstance(instance, InPortBlock)

@given(instance=simulink_EnablePort_strategy)
@settings(max_examples=50)
def test_simulink_enableport_instantiation(instance):
    assert isinstance(instance, simulink_EnablePort)

@given(instance=simulink_TriggerPort_strategy)
@settings(max_examples=50)
def test_simulink_triggerport_instantiation(instance):
    assert isinstance(instance, simulink_TriggerPort)



@given(instance=simulink_TriggerPort_strategy)
def test_simulink_triggerport_triggerInput_setter(instance):
    original = instance.triggerInput
    instance.triggerInput = original
    assert instance.triggerInput == original

@given(instance=stateflow_simulink_ChartBlock_strategy)
@settings(max_examples=50)
def test_stateflow_simulink_chartblock_instantiation(instance):
    assert isinstance(instance, stateflow_simulink_ChartBlock)

@given(instance=simulink_BusElement_strategy)
@settings(max_examples=50)
def test_simulink_buselement_instantiation(instance):
    assert isinstance(instance, simulink_BusElement)



@given(instance=simulink_BusElement_strategy)
def test_simulink_buselement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=simulink_BusElement_strategy)
def test_simulink_buselement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simulink_BusElement_strategy)
def test_simulink_buselement_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

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

@given(instance=simulink_SimulinkFile_strategy)
@settings(max_examples=50)
def test_simulink_simulinkfile_instantiation(instance):
    assert isinstance(instance, simulink_SimulinkFile)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=simulink_msglib_CommunicationSwitch_strategy)
@settings(max_examples=50)
def test_simulink_msglib_communicationswitch_instantiation(instance):
    assert isinstance(instance, simulink_msglib_CommunicationSwitch)



@given(instance=simulink_msglib_CommunicationSwitch_strategy)
def test_simulink_msglib_communicationswitch_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=simulink_ChartBlock_strategy)
@settings(max_examples=50)
def test_simulink_chartblock_instantiation(instance):
    assert isinstance(instance, simulink_ChartBlock)

@given(instance=simulink_UnitDelay_strategy)
@settings(max_examples=50)
def test_simulink_unitdelay_instantiation(instance):
    assert isinstance(instance, simulink_UnitDelay)

@given(instance=simulink_msglib_LinkLayer_strategy)
@settings(max_examples=50)
def test_simulink_msglib_linklayer_instantiation(instance):
    assert isinstance(instance, simulink_msglib_LinkLayer)



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_messageMapping_setter(instance):
    original = instance.messageMapping
    instance.messageMapping = original
    assert instance.messageMapping == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_messageLossProbability_setter(instance):
    original = instance.messageLossProbability
    instance.messageLossProbability = original
    assert instance.messageLossProbability == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_bufferOverflowPossible_setter(instance):
    original = instance.bufferOverflowPossible
    instance.bufferOverflowPossible = original
    assert instance.bufferOverflowPossible == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_delayMax_setter(instance):
    original = instance.delayMax
    instance.delayMax = original
    assert instance.delayMax == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_messageRetransmission_setter(instance):
    original = instance.messageRetransmission
    instance.messageRetransmission = original
    assert instance.messageRetransmission == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_sourceBufferSize_setter(instance):
    original = instance.sourceBufferSize
    instance.sourceBufferSize = original
    assert instance.sourceBufferSize == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_delayMin_setter(instance):
    original = instance.delayMin
    instance.delayMin = original
    assert instance.delayMin == original



@given(instance=simulink_msglib_LinkLayer_strategy)
def test_simulink_msglib_linklayer_bufferSize_setter(instance):
    original = instance.bufferSize
    instance.bufferSize = original
    assert instance.bufferSize == original

@given(instance=simulink_LibraryReference_strategy)
@settings(max_examples=50)
def test_simulink_libraryreference_instantiation(instance):
    assert isinstance(instance, simulink_LibraryReference)

@given(instance=simulink_ZeroOrderHold_strategy)
@settings(max_examples=50)
def test_simulink_zeroorderhold_instantiation(instance):
    assert isinstance(instance, simulink_ZeroOrderHold)



@given(instance=simulink_ZeroOrderHold_strategy)
def test_simulink_zeroorderhold_sampleTime_setter(instance):
    original = instance.sampleTime
    instance.sampleTime = original
    assert instance.sampleTime == original

@given(instance=simulink_MiscBlock_strategy)
@settings(max_examples=50)
def test_simulink_miscblock_instantiation(instance):
    assert isinstance(instance, simulink_MiscBlock)



@given(instance=simulink_MiscBlock_strategy)
def test_simulink_miscblock_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink_DigitalClock_strategy)
@settings(max_examples=50)
def test_simulink_digitalclock_instantiation(instance):
    assert isinstance(instance, simulink_DigitalClock)



@given(instance=simulink_DigitalClock_strategy)
def test_simulink_digitalclock_sampleTime_setter(instance):
    original = instance.sampleTime
    instance.sampleTime = original
    assert instance.sampleTime == original

@given(instance=simulink_reconfiguration_FadingComponent_strategy)
@settings(max_examples=50)
def test_simulink_reconfiguration_fadingcomponent_instantiation(instance):
    assert isinstance(instance, simulink_reconfiguration_FadingComponent)



@given(instance=simulink_reconfiguration_FadingComponent_strategy)
def test_simulink_reconfiguration_fadingcomponent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=simulink_reconfiguration_MultiTargetControl_strategy)
@settings(max_examples=50)
def test_simulink_reconfiguration_multitargetcontrol_instantiation(instance):
    assert isinstance(instance, simulink_reconfiguration_MultiTargetControl)

@given(instance=simulink_Constant_strategy)
@settings(max_examples=50)
def test_simulink_constant_instantiation(instance):
    assert isinstance(instance, simulink_Constant)



@given(instance=simulink_Constant_strategy)
def test_simulink_constant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=simulink_Constant_strategy)
def test_simulink_constant_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simulink_BusCreator_strategy)
@settings(max_examples=50)
def test_simulink_buscreator_instantiation(instance):
    assert isinstance(instance, simulink_BusCreator)

@given(instance=simulink_EmbeddedMatlabFunction_strategy)
@settings(max_examples=50)
def test_simulink_embeddedmatlabfunction_instantiation(instance):
    assert isinstance(instance, simulink_EmbeddedMatlabFunction)



@given(instance=simulink_EmbeddedMatlabFunction_strategy)
def test_simulink_embeddedmatlabfunction_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=simulink_BusSelector_strategy)
@settings(max_examples=50)
def test_simulink_busselector_instantiation(instance):
    assert isinstance(instance, simulink_BusSelector)

@given(instance=simulink_reconfiguration_MultiSourceControl_strategy)
@settings(max_examples=50)
def test_simulink_reconfiguration_multisourcecontrol_instantiation(instance):
    assert isinstance(instance, simulink_reconfiguration_MultiSourceControl)

@given(instance=simulink_PortBlock_strategy)
@settings(max_examples=50)
def test_simulink_portblock_instantiation(instance):
    assert isinstance(instance, simulink_PortBlock)



@given(instance=simulink_PortBlock_strategy)
def test_simulink_portblock_initialCondition_setter(instance):
    original = instance.initialCondition
    instance.initialCondition = original
    assert instance.initialCondition == original



@given(instance=simulink_PortBlock_strategy)
def test_simulink_portblock_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=simulink_PortBlock_strategy)
def test_simulink_portblock_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=simulink_Parameter_strategy)
@settings(max_examples=50)
def test_simulink_parameter_instantiation(instance):
    assert isinstance(instance, simulink_Parameter)



@given(instance=simulink_Parameter_strategy)
def test_simulink_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simulink_Parameter_strategy)
def test_simulink_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=simulink_Parameter_strategy)
def test_simulink_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simulink_Element_strategy)
@settings(max_examples=50)
def test_simulink_element_instantiation(instance):
    assert isinstance(instance, simulink_Element)



@given(instance=simulink_Element_strategy)
def test_simulink_element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimulinkFile_strategy)
@settings(max_examples=50)
def test_simulinkfile_instantiation(instance):
    assert isinstance(instance, SimulinkFile)

@given(instance=simulink_SimulinkLibrary_strategy)
@settings(max_examples=50)
def test_simulink_simulinklibrary_instantiation(instance):
    assert isinstance(instance, simulink_SimulinkLibrary)

@given(instance=simulink_SimulinkModel_strategy)
@settings(max_examples=50)
def test_simulink_simulinkmodel_instantiation(instance):
    assert isinstance(instance, simulink_SimulinkModel)

@given(instance=simulink_InPortBlock_strategy)
@settings(max_examples=50)
def test_simulink_inportblock_instantiation(instance):
    assert isinstance(instance, simulink_InPortBlock)

@given(instance=simulink_OutPortBlock_strategy)
@settings(max_examples=50)
def test_simulink_outportblock_instantiation(instance):
    assert isinstance(instance, simulink_OutPortBlock)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=simulink_SimulinkContainer_strategy)
@settings(max_examples=50)
def test_simulink_simulinkcontainer_instantiation(instance):
    assert isinstance(instance, simulink_SimulinkContainer)

@given(instance=simulink_Bus_strategy)
@settings(max_examples=50)
def test_simulink_bus_instantiation(instance):
    assert isinstance(instance, simulink_Bus)



@given(instance=simulink_Bus_strategy)
def test_simulink_bus_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink_Line_strategy)
@settings(max_examples=50)
def test_simulink_line_instantiation(instance):
    assert isinstance(instance, simulink_Line)

@given(instance=simulink_stateflow_StateflowElement_strategy)
@settings(max_examples=50)
def test_simulink_stateflow_stateflowelement_instantiation(instance):
    assert isinstance(instance, simulink_stateflow_StateflowElement)

@given(instance=simulink_Block_strategy)
@settings(max_examples=50)
def test_simulink_block_instantiation(instance):
    assert isinstance(instance, simulink_Block)



@given(instance=simulink_Block_strategy)
def test_simulink_block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simulink_SubSystem_strategy)
@settings(max_examples=50)
def test_simulink_subsystem_instantiation(instance):
    assert isinstance(instance, simulink_SubSystem)
