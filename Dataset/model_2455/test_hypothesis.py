import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    jpdl31_SubProcessType,
    jpdl31_VariableType,
    jpdl31_TransitionType,
    jpdl31_SuperStateType,
    jpdl31_StateType,
    jpdl31_StartStateType,
    jpdl31_TimerType,
    jpdl31_TaskNodeType,
    jpdl31_TaskType,
    jpdl31_SwimlaneType,
    jpdl31_ProcessDefinitionType,
    jpdl31_NodeType,
    jpdl31_ProcessStateType,
    jpdl31_EndStateType,
    jpdl31_JoinType,
    jpdl31_ForkType,
    jpdl31_EStringToStringMapEntry,
    jpdl31_DocumentRoot,
    jpdl31_TransitionType1,
    jpdl31_ExceptionHandlerType,
    jpdl31_EventType,
    jpdl31_Delegation,
    jpdl31_DecisionType,
    jpdl31_ScriptType,
    jpdl31_CreateTimerType,
    jpdl31_ConditionType,
    jpdl31_CancelTimerType,
    Delegation,
    jpdl31_AssignmentType,
    jpdl31_ActionType,
    ConfigTypeType1,
    ConfigType,
    SignalType,
    TypeTypeMember1,
    ConfigTypeType,
    PriorityTypeMember0,
    BooleanType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jpdl31_subprocesstype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_SubProcessType)


def test_jpdl31_subprocesstype_constructor_exists():
    assert callable(jpdl31_SubProcessType.__init__)


def test_jpdl31_subprocesstype_constructor_args():
    sig = inspect.signature(jpdl31_SubProcessType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_subprocesstype_has_version():
    assert hasattr(jpdl31_SubProcessType, "version")
    descriptor = None
    for klass in jpdl31_SubProcessType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_subprocesstype_has_name():
    assert hasattr(jpdl31_SubProcessType, "name")
    descriptor = None
    for klass in jpdl31_SubProcessType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_variabletype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_VariableType)


def test_jpdl31_variabletype_constructor_exists():
    assert callable(jpdl31_VariableType.__init__)


def test_jpdl31_variabletype_constructor_args():
    sig = inspect.signature(jpdl31_VariableType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "mappedName" in params, "Missing parameter 'mappedName'"
    assert "access" in params, "Missing parameter 'access'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_variabletype_has_any():
    assert hasattr(jpdl31_VariableType, "any")
    descriptor = None
    for klass in jpdl31_VariableType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_variabletype_has_mappedName():
    assert hasattr(jpdl31_VariableType, "mappedName")
    descriptor = None
    for klass in jpdl31_VariableType.__mro__:
        if "mappedName" in klass.__dict__:
            descriptor = klass.__dict__["mappedName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_variabletype_has_access():
    assert hasattr(jpdl31_VariableType, "access")
    descriptor = None
    for klass in jpdl31_VariableType.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_variabletype_has_name():
    assert hasattr(jpdl31_VariableType, "name")
    descriptor = None
    for klass in jpdl31_VariableType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_transitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_TransitionType)


def test_jpdl31_transitiontype_constructor_exists():
    assert callable(jpdl31_TransitionType.__init__)


def test_jpdl31_transitiontype_constructor_args():
    sig = inspect.signature(jpdl31_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_transitiontype_has_to():
    assert hasattr(jpdl31_TransitionType, "to")
    descriptor = None
    for klass in jpdl31_TransitionType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_transitiontype_has_group():
    assert hasattr(jpdl31_TransitionType, "group")
    descriptor = None
    for klass in jpdl31_TransitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_transitiontype_has_name():
    assert hasattr(jpdl31_TransitionType, "name")
    descriptor = None
    for klass in jpdl31_TransitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_superstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_SuperStateType)


def test_jpdl31_superstatetype_constructor_exists():
    assert callable(jpdl31_SuperStateType.__init__)


def test_jpdl31_superstatetype_constructor_args():
    sig = inspect.signature(jpdl31_SuperStateType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_superstatetype_has_group():
    assert hasattr(jpdl31_SuperStateType, "group")
    descriptor = None
    for klass in jpdl31_SuperStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_superstatetype_has_async_():
    assert hasattr(jpdl31_SuperStateType, "async_")
    descriptor = None
    for klass in jpdl31_SuperStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_superstatetype_has_name():
    assert hasattr(jpdl31_SuperStateType, "name")
    descriptor = None
    for klass in jpdl31_SuperStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_statetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_StateType)


def test_jpdl31_statetype_constructor_exists():
    assert callable(jpdl31_StateType.__init__)


def test_jpdl31_statetype_constructor_args():
    sig = inspect.signature(jpdl31_StateType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_statetype_has_async_():
    assert hasattr(jpdl31_StateType, "async_")
    descriptor = None
    for klass in jpdl31_StateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_statetype_has_nodeContentElements():
    assert hasattr(jpdl31_StateType, "nodeContentElements")
    descriptor = None
    for klass in jpdl31_StateType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_statetype_has_name():
    assert hasattr(jpdl31_StateType, "name")
    descriptor = None
    for klass in jpdl31_StateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_startstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_StartStateType)


def test_jpdl31_startstatetype_constructor_exists():
    assert callable(jpdl31_StartStateType.__init__)


def test_jpdl31_startstatetype_constructor_args():
    sig = inspect.signature(jpdl31_StartStateType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31_startstatetype_has_name():
    assert hasattr(jpdl31_StartStateType, "name")
    descriptor = None
    for klass in jpdl31_StartStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_startstatetype_has_group():
    assert hasattr(jpdl31_StartStateType, "group")
    descriptor = None
    for klass in jpdl31_StartStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_timertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_TimerType)


def test_jpdl31_timertype_constructor_exists():
    assert callable(jpdl31_TimerType.__init__)


def test_jpdl31_timertype_constructor_args():
    sig = inspect.signature(jpdl31_TimerType.__init__)
    params = list(sig.parameters.keys())
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "transition" in params, "Missing parameter 'transition'"

def test_jpdl31_timertype_has_duedate():
    assert hasattr(jpdl31_TimerType, "duedate")
    descriptor = None
    for klass in jpdl31_TimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_timertype_has_name():
    assert hasattr(jpdl31_TimerType, "name")
    descriptor = None
    for klass in jpdl31_TimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_timertype_has_repeat():
    assert hasattr(jpdl31_TimerType, "repeat")
    descriptor = None
    for klass in jpdl31_TimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_timertype_has_transition():
    assert hasattr(jpdl31_TimerType, "transition")
    descriptor = None
    for klass in jpdl31_TimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_tasknodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_TaskNodeType)


def test_jpdl31_tasknodetype_constructor_exists():
    assert callable(jpdl31_TaskNodeType.__init__)


def test_jpdl31_tasknodetype_constructor_args():
    sig = inspect.signature(jpdl31_TaskNodeType.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"
    assert "group" in params, "Missing parameter 'group'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "endTasks" in params, "Missing parameter 'endTasks'"
    assert "createTasks" in params, "Missing parameter 'createTasks'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_tasknodetype_has_signal():
    assert hasattr(jpdl31_TaskNodeType, "signal")
    descriptor = None
    for klass in jpdl31_TaskNodeType.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasknodetype_has_group():
    assert hasattr(jpdl31_TaskNodeType, "group")
    descriptor = None
    for klass in jpdl31_TaskNodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasknodetype_has_async_():
    assert hasattr(jpdl31_TaskNodeType, "async_")
    descriptor = None
    for klass in jpdl31_TaskNodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasknodetype_has_endTasks():
    assert hasattr(jpdl31_TaskNodeType, "endTasks")
    descriptor = None
    for klass in jpdl31_TaskNodeType.__mro__:
        if "endTasks" in klass.__dict__:
            descriptor = klass.__dict__["endTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasknodetype_has_createTasks():
    assert hasattr(jpdl31_TaskNodeType, "createTasks")
    descriptor = None
    for klass in jpdl31_TaskNodeType.__mro__:
        if "createTasks" in klass.__dict__:
            descriptor = klass.__dict__["createTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasknodetype_has_name():
    assert hasattr(jpdl31_TaskNodeType, "name")
    descriptor = None
    for klass in jpdl31_TaskNodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_tasktype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_TaskType)


def test_jpdl31_tasktype_constructor_exists():
    assert callable(jpdl31_TaskType.__init__)


def test_jpdl31_tasktype_constructor_args():
    sig = inspect.signature(jpdl31_TaskType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "group" in params, "Missing parameter 'group'"
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "swimlane" in params, "Missing parameter 'swimlane'"
    assert "blocking" in params, "Missing parameter 'blocking'"
    assert "name" in params, "Missing parameter 'name'"
    assert "signalling" in params, "Missing parameter 'signalling'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_jpdl31_tasktype_has_description():
    assert hasattr(jpdl31_TaskType, "description")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_group():
    assert hasattr(jpdl31_TaskType, "group")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_duedate():
    assert hasattr(jpdl31_TaskType, "duedate")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_swimlane():
    assert hasattr(jpdl31_TaskType, "swimlane")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "swimlane" in klass.__dict__:
            descriptor = klass.__dict__["swimlane"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_blocking():
    assert hasattr(jpdl31_TaskType, "blocking")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "blocking" in klass.__dict__:
            descriptor = klass.__dict__["blocking"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_name():
    assert hasattr(jpdl31_TaskType, "name")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_signalling():
    assert hasattr(jpdl31_TaskType, "signalling")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "signalling" in klass.__dict__:
            descriptor = klass.__dict__["signalling"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_tasktype_has_priority():
    assert hasattr(jpdl31_TaskType, "priority")
    descriptor = None
    for klass in jpdl31_TaskType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_swimlanetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_SwimlaneType)


def test_jpdl31_swimlanetype_constructor_exists():
    assert callable(jpdl31_SwimlaneType.__init__)


def test_jpdl31_swimlanetype_constructor_args():
    sig = inspect.signature(jpdl31_SwimlaneType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_swimlanetype_has_name():
    assert hasattr(jpdl31_SwimlaneType, "name")
    descriptor = None
    for klass in jpdl31_SwimlaneType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ProcessDefinitionType)


def test_jpdl31_processdefinitiontype_constructor_exists():
    assert callable(jpdl31_ProcessDefinitionType.__init__)


def test_jpdl31_processdefinitiontype_constructor_args():
    sig = inspect.signature(jpdl31_ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_processdefinitiontype_has_group():
    assert hasattr(jpdl31_ProcessDefinitionType, "group")
    descriptor = None
    for klass in jpdl31_ProcessDefinitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_processdefinitiontype_has_name():
    assert hasattr(jpdl31_ProcessDefinitionType, "name")
    descriptor = None
    for klass in jpdl31_ProcessDefinitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_nodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_NodeType)


def test_jpdl31_nodetype_constructor_exists():
    assert callable(jpdl31_NodeType.__init__)


def test_jpdl31_nodetype_constructor_args():
    sig = inspect.signature(jpdl31_NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl31_nodetype_has_nodeContentElements():
    assert hasattr(jpdl31_NodeType, "nodeContentElements")
    descriptor = None
    for klass in jpdl31_NodeType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_nodetype_has_name():
    assert hasattr(jpdl31_NodeType, "name")
    descriptor = None
    for klass in jpdl31_NodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_nodetype_has_async_():
    assert hasattr(jpdl31_NodeType, "async_")
    descriptor = None
    for klass in jpdl31_NodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_processstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ProcessStateType)


def test_jpdl31_processstatetype_constructor_exists():
    assert callable(jpdl31_ProcessStateType.__init__)


def test_jpdl31_processstatetype_constructor_args():
    sig = inspect.signature(jpdl31_ProcessStateType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31_processstatetype_has_async_():
    assert hasattr(jpdl31_ProcessStateType, "async_")
    descriptor = None
    for klass in jpdl31_ProcessStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_processstatetype_has_name():
    assert hasattr(jpdl31_ProcessStateType, "name")
    descriptor = None
    for klass in jpdl31_ProcessStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_processstatetype_has_group():
    assert hasattr(jpdl31_ProcessStateType, "group")
    descriptor = None
    for klass in jpdl31_ProcessStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_endstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_EndStateType)


def test_jpdl31_endstatetype_constructor_exists():
    assert callable(jpdl31_EndStateType.__init__)


def test_jpdl31_endstatetype_constructor_args():
    sig = inspect.signature(jpdl31_EndStateType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31_endstatetype_has_name():
    assert hasattr(jpdl31_EndStateType, "name")
    descriptor = None
    for klass in jpdl31_EndStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_endstatetype_has_group():
    assert hasattr(jpdl31_EndStateType, "group")
    descriptor = None
    for klass in jpdl31_EndStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_jointype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_JoinType)


def test_jpdl31_jointype_constructor_exists():
    assert callable(jpdl31_JoinType.__init__)


def test_jpdl31_jointype_constructor_args():
    sig = inspect.signature(jpdl31_JoinType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"

def test_jpdl31_jointype_has_async_():
    assert hasattr(jpdl31_JoinType, "async_")
    descriptor = None
    for klass in jpdl31_JoinType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_jointype_has_name():
    assert hasattr(jpdl31_JoinType, "name")
    descriptor = None
    for klass in jpdl31_JoinType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_jointype_has_nodeContentElements():
    assert hasattr(jpdl31_JoinType, "nodeContentElements")
    descriptor = None
    for klass in jpdl31_JoinType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_forktype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ForkType)


def test_jpdl31_forktype_constructor_exists():
    assert callable(jpdl31_ForkType.__init__)


def test_jpdl31_forktype_constructor_args():
    sig = inspect.signature(jpdl31_ForkType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl31_forktype_has_name():
    assert hasattr(jpdl31_ForkType, "name")
    descriptor = None
    for klass in jpdl31_ForkType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_forktype_has_group():
    assert hasattr(jpdl31_ForkType, "group")
    descriptor = None
    for klass in jpdl31_ForkType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_forktype_has_async_():
    assert hasattr(jpdl31_ForkType, "async_")
    descriptor = None
    for klass in jpdl31_ForkType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(jpdl31_EStringToStringMapEntry)


def test_jpdl31_estringtostringmapentry_constructor_exists():
    assert callable(jpdl31_EStringToStringMapEntry.__init__)


def test_jpdl31_estringtostringmapentry_constructor_args():
    sig = inspect.signature(jpdl31_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpdl31_documentroot_is_not_abstract():
    assert not inspect.isabstract(jpdl31_DocumentRoot)


def test_jpdl31_documentroot_constructor_exists():
    assert callable(jpdl31_DocumentRoot.__init__)


def test_jpdl31_documentroot_constructor_args():
    sig = inspect.signature(jpdl31_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_jpdl31_documentroot_has_mixed():
    assert hasattr(jpdl31_DocumentRoot, "mixed")
    descriptor = None
    for klass in jpdl31_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_transitiontype1_is_not_abstract():
    assert not inspect.isabstract(jpdl31_TransitionType1)


def test_jpdl31_transitiontype1_constructor_exists():
    assert callable(jpdl31_TransitionType1.__init__)


def test_jpdl31_transitiontype1_constructor_args():
    sig = inspect.signature(jpdl31_TransitionType1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "to" in params, "Missing parameter 'to'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31_transitiontype1_has_name():
    assert hasattr(jpdl31_TransitionType1, "name")
    descriptor = None
    for klass in jpdl31_TransitionType1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_transitiontype1_has_to():
    assert hasattr(jpdl31_TransitionType1, "to")
    descriptor = None
    for klass in jpdl31_TransitionType1.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_transitiontype1_has_group():
    assert hasattr(jpdl31_TransitionType1, "group")
    descriptor = None
    for klass in jpdl31_TransitionType1.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_exceptionhandlertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ExceptionHandlerType)


def test_jpdl31_exceptionhandlertype_constructor_exists():
    assert callable(jpdl31_ExceptionHandlerType.__init__)


def test_jpdl31_exceptionhandlertype_constructor_args():
    sig = inspect.signature(jpdl31_ExceptionHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionClass" in params, "Missing parameter 'exceptionClass'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31_exceptionhandlertype_has_exceptionClass():
    assert hasattr(jpdl31_ExceptionHandlerType, "exceptionClass")
    descriptor = None
    for klass in jpdl31_ExceptionHandlerType.__mro__:
        if "exceptionClass" in klass.__dict__:
            descriptor = klass.__dict__["exceptionClass"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_exceptionhandlertype_has_group():
    assert hasattr(jpdl31_ExceptionHandlerType, "group")
    descriptor = None
    for klass in jpdl31_ExceptionHandlerType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_eventtype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_EventType)


def test_jpdl31_eventtype_constructor_exists():
    assert callable(jpdl31_EventType.__init__)


def test_jpdl31_eventtype_constructor_args():
    sig = inspect.signature(jpdl31_EventType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "actionElements" in params, "Missing parameter 'actionElements'"

def test_jpdl31_eventtype_has_type():
    assert hasattr(jpdl31_EventType, "type")
    descriptor = None
    for klass in jpdl31_EventType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_eventtype_has_actionElements():
    assert hasattr(jpdl31_EventType, "actionElements")
    descriptor = None
    for klass in jpdl31_EventType.__mro__:
        if "actionElements" in klass.__dict__:
            descriptor = klass.__dict__["actionElements"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_delegation_is_not_abstract():
    assert not inspect.isabstract(jpdl31_Delegation)


def test_jpdl31_delegation_constructor_exists():
    assert callable(jpdl31_Delegation.__init__)


def test_jpdl31_delegation_constructor_args():
    sig = inspect.signature(jpdl31_Delegation.__init__)
    params = list(sig.parameters.keys())
    assert "configType" in params, "Missing parameter 'configType'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "any" in params, "Missing parameter 'any'"

def test_jpdl31_delegation_has_configType():
    assert hasattr(jpdl31_Delegation, "configType")
    descriptor = None
    for klass in jpdl31_Delegation.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_delegation_has_mixed():
    assert hasattr(jpdl31_Delegation, "mixed")
    descriptor = None
    for klass in jpdl31_Delegation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_delegation_has_class_():
    assert hasattr(jpdl31_Delegation, "class_")
    descriptor = None
    for klass in jpdl31_Delegation.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_delegation_has_any():
    assert hasattr(jpdl31_Delegation, "any")
    descriptor = None
    for klass in jpdl31_Delegation.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_decisiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_DecisionType)


def test_jpdl31_decisiontype_constructor_exists():
    assert callable(jpdl31_DecisionType.__init__)


def test_jpdl31_decisiontype_constructor_args():
    sig = inspect.signature(jpdl31_DecisionType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_jpdl31_decisiontype_has_name():
    assert hasattr(jpdl31_DecisionType, "name")
    descriptor = None
    for klass in jpdl31_DecisionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_decisiontype_has_group():
    assert hasattr(jpdl31_DecisionType, "group")
    descriptor = None
    for klass in jpdl31_DecisionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_decisiontype_has_async_():
    assert hasattr(jpdl31_DecisionType, "async_")
    descriptor = None
    for klass in jpdl31_DecisionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_decisiontype_has_expression():
    assert hasattr(jpdl31_DecisionType, "expression")
    descriptor = None
    for klass in jpdl31_DecisionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_scripttype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ScriptType)


def test_jpdl31_scripttype_constructor_exists():
    assert callable(jpdl31_ScriptType.__init__)


def test_jpdl31_scripttype_constructor_args():
    sig = inspect.signature(jpdl31_ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "any" in params, "Missing parameter 'any'"

def test_jpdl31_scripttype_has_name():
    assert hasattr(jpdl31_ScriptType, "name")
    descriptor = None
    for klass in jpdl31_ScriptType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_scripttype_has_mixed():
    assert hasattr(jpdl31_ScriptType, "mixed")
    descriptor = None
    for klass in jpdl31_ScriptType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_scripttype_has_acceptPropagatedEvents():
    assert hasattr(jpdl31_ScriptType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl31_ScriptType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_scripttype_has_any():
    assert hasattr(jpdl31_ScriptType, "any")
    descriptor = None
    for klass in jpdl31_ScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_createtimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_CreateTimerType)


def test_jpdl31_createtimertype_constructor_exists():
    assert callable(jpdl31_CreateTimerType.__init__)


def test_jpdl31_createtimertype_constructor_args():
    sig = inspect.signature(jpdl31_CreateTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "transition" in params, "Missing parameter 'transition'"
    assert "name" in params, "Missing parameter 'name'"
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "duedate" in params, "Missing parameter 'duedate'"

def test_jpdl31_createtimertype_has_transition():
    assert hasattr(jpdl31_CreateTimerType, "transition")
    descriptor = None
    for klass in jpdl31_CreateTimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_createtimertype_has_name():
    assert hasattr(jpdl31_CreateTimerType, "name")
    descriptor = None
    for klass in jpdl31_CreateTimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_createtimertype_has_repeat():
    assert hasattr(jpdl31_CreateTimerType, "repeat")
    descriptor = None
    for klass in jpdl31_CreateTimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_createtimertype_has_duedate():
    assert hasattr(jpdl31_CreateTimerType, "duedate")
    descriptor = None
    for klass in jpdl31_CreateTimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_conditiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ConditionType)


def test_jpdl31_conditiontype_constructor_exists():
    assert callable(jpdl31_ConditionType.__init__)


def test_jpdl31_conditiontype_constructor_args():
    sig = inspect.signature(jpdl31_ConditionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_jpdl31_conditiontype_has_group():
    assert hasattr(jpdl31_ConditionType, "group")
    descriptor = None
    for klass in jpdl31_ConditionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_conditiontype_has_any():
    assert hasattr(jpdl31_ConditionType, "any")
    descriptor = None
    for klass in jpdl31_ConditionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_conditiontype_has_mixed():
    assert hasattr(jpdl31_ConditionType, "mixed")
    descriptor = None
    for klass in jpdl31_ConditionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_conditiontype_has_expression():
    assert hasattr(jpdl31_ConditionType, "expression")
    descriptor = None
    for klass in jpdl31_ConditionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_canceltimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_CancelTimerType)


def test_jpdl31_canceltimertype_constructor_exists():
    assert callable(jpdl31_CancelTimerType.__init__)


def test_jpdl31_canceltimertype_constructor_args():
    sig = inspect.signature(jpdl31_CancelTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31_canceltimertype_has_name():
    assert hasattr(jpdl31_CancelTimerType, "name")
    descriptor = None
    for klass in jpdl31_CancelTimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_delegation_is_not_abstract():
    assert not inspect.isabstract(Delegation)


def test_delegation_constructor_exists():
    assert callable(Delegation.__init__)


def test_delegation_constructor_args():
    sig = inspect.signature(Delegation.__init__)
    params = list(sig.parameters.keys())



def test_jpdl31_assignmenttype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_AssignmentType)


def test_jpdl31_assignmenttype_constructor_exists():
    assert callable(jpdl31_AssignmentType.__init__)


def test_jpdl31_assignmenttype_constructor_args():
    sig = inspect.signature(jpdl31_AssignmentType.__init__)
    params = list(sig.parameters.keys())
    assert "actorId" in params, "Missing parameter 'actorId'"
    assert "pooledActors" in params, "Missing parameter 'pooledActors'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_jpdl31_assignmenttype_has_actorId():
    assert hasattr(jpdl31_AssignmentType, "actorId")
    descriptor = None
    for klass in jpdl31_AssignmentType.__mro__:
        if "actorId" in klass.__dict__:
            descriptor = klass.__dict__["actorId"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_assignmenttype_has_pooledActors():
    assert hasattr(jpdl31_AssignmentType, "pooledActors")
    descriptor = None
    for klass in jpdl31_AssignmentType.__mro__:
        if "pooledActors" in klass.__dict__:
            descriptor = klass.__dict__["pooledActors"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_assignmenttype_has_expression():
    assert hasattr(jpdl31_AssignmentType, "expression")
    descriptor = None
    for klass in jpdl31_AssignmentType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31_actiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31_ActionType)


def test_jpdl31_actiontype_constructor_exists():
    assert callable(jpdl31_ActionType.__init__)


def test_jpdl31_actiontype_constructor_args():
    sig = inspect.signature(jpdl31_ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "configType" in params, "Missing parameter 'configType'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "refName" in params, "Missing parameter 'refName'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"

def test_jpdl31_actiontype_has_configType():
    assert hasattr(jpdl31_ActionType, "configType")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_expression():
    assert hasattr(jpdl31_ActionType, "expression")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_refName():
    assert hasattr(jpdl31_ActionType, "refName")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "refName" in klass.__dict__:
            descriptor = klass.__dict__["refName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_class_():
    assert hasattr(jpdl31_ActionType, "class_")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_async_():
    assert hasattr(jpdl31_ActionType, "async_")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_mixed():
    assert hasattr(jpdl31_ActionType, "mixed")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_any():
    assert hasattr(jpdl31_ActionType, "any")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_name():
    assert hasattr(jpdl31_ActionType, "name")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31_actiontype_has_acceptPropagatedEvents():
    assert hasattr(jpdl31_ActionType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl31_ActionType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_configtypetype1_exists():
    # Check that the Enumeration exists
    assert ConfigTypeType1 is not None

def test_configtypetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigTypeType1]
    expected_literals = [
        "bean",
        "field",
        "configurationProperty",
        "constructor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigTypeType1"

def test_configtype_exists():
    # Check that the Enumeration exists
    assert ConfigType is not None

def test_configtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigType]
    expected_literals = [
        "bean",
        "configurationProperty",
        "field",
        "constructor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigType"

def test_signaltype_exists():
    # Check that the Enumeration exists
    assert SignalType is not None

def test_signaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalType]
    expected_literals = [
        "first",
        "firstWait",
        "lastWait",
        "never",
        "last",
        "unsynchronized",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalType"

def test_typetypemember1_exists():
    # Check that the Enumeration exists
    assert TypeTypeMember1 is not None

def test_typetypemember1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeTypeMember1]
    expected_literals = [
        "taskAssign",
        "taskCreate",
        "afterSignal",
        "nodeEnter",
        "subprocessCreated",
        "timerCreate",
        "superstateLeave",
        "taskStart",
        "nodeLeave",
        "taskEnd",
        "subprocessEnd",
        "superstateEnter",
        "processStart",
        "processEnd",
        "beforeSignal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeTypeMember1"

def test_configtypetype_exists():
    # Check that the Enumeration exists
    assert ConfigTypeType is not None

def test_configtypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigTypeType]
    expected_literals = [
        "constructor",
        "field",
        "configurationProperty",
        "bean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigTypeType"

def test_prioritytypemember0_exists():
    # Check that the Enumeration exists
    assert PriorityTypeMember0 is not None

def test_prioritytypemember0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityTypeMember0]
    expected_literals = [
        "normal",
        "lowest",
        "high",
        "highest",
        "low",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityTypeMember0"

def test_booleantype_exists():
    # Check that the Enumeration exists
    assert BooleanType is not None

def test_booleantype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanType]
    expected_literals = [
        "true",
        "on",
        "off",
        "false",
        "yes",
        "no",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanType"


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
jpdl31_SubProcessType_strategy = st.builds(
    jpdl31_SubProcessType,
    version=
        safe_text,
    name=
        safe_text
)
jpdl31_VariableType_strategy = st.builds(
    jpdl31_VariableType,
    any=
        safe_text,
    mappedName=
        safe_text,
    access=
        safe_text,
    name=
        safe_text
)
jpdl31_TransitionType_strategy = st.builds(
    jpdl31_TransitionType,
    to=
        safe_text,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31_SuperStateType_strategy = st.builds(
    jpdl31_SuperStateType,
    group=
        safe_text,
    async_=
        safe_text,
    name=
        safe_text
)
jpdl31_StateType_strategy = st.builds(
    jpdl31_StateType,
    async_=
        safe_text,
    nodeContentElements=
        safe_text,
    name=
        safe_text
)
jpdl31_StartStateType_strategy = st.builds(
    jpdl31_StartStateType,
    name=
        safe_text,
    group=
        safe_text
)
jpdl31_TimerType_strategy = st.builds(
    jpdl31_TimerType,
    duedate=
        safe_text,
    name=
        safe_text,
    repeat=
        safe_text,
    transition=
        safe_text
)
jpdl31_TaskNodeType_strategy = st.builds(
    jpdl31_TaskNodeType,
    signal=
        safe_text,
    group=
        safe_text,
    async_=
        safe_text,
    endTasks=
        safe_text,
    createTasks=
        safe_text,
    name=
        safe_text
)
jpdl31_TaskType_strategy = st.builds(
    jpdl31_TaskType,
    description=
        safe_text,
    group=
        safe_text,
    duedate=
        safe_text,
    swimlane=
        safe_text,
    blocking=
        safe_text,
    name=
        safe_text,
    signalling=
        safe_text,
    priority=
        safe_text
)
jpdl31_SwimlaneType_strategy = st.builds(
    jpdl31_SwimlaneType,
    name=
        safe_text
)
jpdl31_ProcessDefinitionType_strategy = st.builds(
    jpdl31_ProcessDefinitionType,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31_NodeType_strategy = st.builds(
    jpdl31_NodeType,
    nodeContentElements=
        safe_text,
    name=
        safe_text,
    async_=
        safe_text
)
jpdl31_ProcessStateType_strategy = st.builds(
    jpdl31_ProcessStateType,
    async_=
        safe_text,
    name=
        safe_text,
    group=
        safe_text
)
jpdl31_EndStateType_strategy = st.builds(
    jpdl31_EndStateType,
    name=
        safe_text,
    group=
        safe_text
)
jpdl31_JoinType_strategy = st.builds(
    jpdl31_JoinType,
    async_=
        safe_text,
    name=
        safe_text,
    nodeContentElements=
        safe_text
)
jpdl31_ForkType_strategy = st.builds(
    jpdl31_ForkType,
    name=
        safe_text,
    group=
        safe_text,
    async_=
        safe_text
)
jpdl31_EStringToStringMapEntry_strategy = st.builds(
    jpdl31_EStringToStringMapEntry,
)
jpdl31_DocumentRoot_strategy = st.builds(
    jpdl31_DocumentRoot,
    mixed=
        safe_text
)
jpdl31_TransitionType1_strategy = st.builds(
    jpdl31_TransitionType1,
    name=
        safe_text,
    to=
        safe_text,
    group=
        safe_text
)
jpdl31_ExceptionHandlerType_strategy = st.builds(
    jpdl31_ExceptionHandlerType,
    exceptionClass=
        safe_text,
    group=
        safe_text
)
jpdl31_EventType_strategy = st.builds(
    jpdl31_EventType,
    type=
        safe_text,
    actionElements=
        safe_text
)
jpdl31_Delegation_strategy = st.builds(
    jpdl31_Delegation,
    configType=
        safe_text,
    mixed=
        safe_text,
    class_=
        safe_text,
    any=
        safe_text
)
jpdl31_DecisionType_strategy = st.builds(
    jpdl31_DecisionType,
    name=
        safe_text,
    group=
        safe_text,
    async_=
        safe_text,
    expression=
        safe_text
)
jpdl31_ScriptType_strategy = st.builds(
    jpdl31_ScriptType,
    name=
        safe_text,
    mixed=
        safe_text,
    acceptPropagatedEvents=
        safe_text,
    any=
        safe_text
)
jpdl31_CreateTimerType_strategy = st.builds(
    jpdl31_CreateTimerType,
    transition=
        safe_text,
    name=
        safe_text,
    repeat=
        safe_text,
    duedate=
        safe_text
)
jpdl31_ConditionType_strategy = st.builds(
    jpdl31_ConditionType,
    group=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text,
    expression=
        safe_text
)
jpdl31_CancelTimerType_strategy = st.builds(
    jpdl31_CancelTimerType,
    name=
        safe_text
)
Delegation_strategy = st.builds(
    Delegation,
)
jpdl31_AssignmentType_strategy = st.builds(
    jpdl31_AssignmentType,
    actorId=
        safe_text,
    pooledActors=
        safe_text,
    expression=
        safe_text
)
jpdl31_ActionType_strategy = st.builds(
    jpdl31_ActionType,
    configType=
        safe_text,
    expression=
        safe_text,
    refName=
        safe_text,
    class_=
        safe_text,
    async_=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text,
    name=
        safe_text,
    acceptPropagatedEvents=
        safe_text
)

@given(instance=jpdl31_SubProcessType_strategy)
@settings(max_examples=50)
def test_jpdl31_subprocesstype_instantiation(instance):
    assert isinstance(instance, jpdl31_SubProcessType)



@given(instance=jpdl31_SubProcessType_strategy)
def test_jpdl31_subprocesstype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=jpdl31_SubProcessType_strategy)
def test_jpdl31_subprocesstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_VariableType_strategy)
@settings(max_examples=50)
def test_jpdl31_variabletype_instantiation(instance):
    assert isinstance(instance, jpdl31_VariableType)



@given(instance=jpdl31_VariableType_strategy)
def test_jpdl31_variabletype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl31_VariableType_strategy)
def test_jpdl31_variabletype_mappedName_setter(instance):
    original = instance.mappedName
    instance.mappedName = original
    assert instance.mappedName == original



@given(instance=jpdl31_VariableType_strategy)
def test_jpdl31_variabletype_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original



@given(instance=jpdl31_VariableType_strategy)
def test_jpdl31_variabletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_TransitionType_strategy)
@settings(max_examples=50)
def test_jpdl31_transitiontype_instantiation(instance):
    assert isinstance(instance, jpdl31_TransitionType)



@given(instance=jpdl31_TransitionType_strategy)
def test_jpdl31_transitiontype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=jpdl31_TransitionType_strategy)
def test_jpdl31_transitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_TransitionType_strategy)
def test_jpdl31_transitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_SuperStateType_strategy)
@settings(max_examples=50)
def test_jpdl31_superstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31_SuperStateType)



@given(instance=jpdl31_SuperStateType_strategy)
def test_jpdl31_superstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_SuperStateType_strategy)
def test_jpdl31_superstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_SuperStateType_strategy)
def test_jpdl31_superstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_StateType_strategy)
@settings(max_examples=50)
def test_jpdl31_statetype_instantiation(instance):
    assert isinstance(instance, jpdl31_StateType)



@given(instance=jpdl31_StateType_strategy)
def test_jpdl31_statetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_StateType_strategy)
def test_jpdl31_statetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original



@given(instance=jpdl31_StateType_strategy)
def test_jpdl31_statetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_StartStateType_strategy)
@settings(max_examples=50)
def test_jpdl31_startstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31_StartStateType)



@given(instance=jpdl31_StartStateType_strategy)
def test_jpdl31_startstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_StartStateType_strategy)
def test_jpdl31_startstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31_TimerType_strategy)
@settings(max_examples=50)
def test_jpdl31_timertype_instantiation(instance):
    assert isinstance(instance, jpdl31_TimerType)



@given(instance=jpdl31_TimerType_strategy)
def test_jpdl31_timertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original



@given(instance=jpdl31_TimerType_strategy)
def test_jpdl31_timertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_TimerType_strategy)
def test_jpdl31_timertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=jpdl31_TimerType_strategy)
def test_jpdl31_timertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=jpdl31_TaskNodeType_strategy)
@settings(max_examples=50)
def test_jpdl31_tasknodetype_instantiation(instance):
    assert isinstance(instance, jpdl31_TaskNodeType)



@given(instance=jpdl31_TaskNodeType_strategy)
def test_jpdl31_tasknodetype_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original



@given(instance=jpdl31_TaskNodeType_strategy)
def test_jpdl31_tasknodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_TaskNodeType_strategy)
def test_jpdl31_tasknodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_TaskNodeType_strategy)
def test_jpdl31_tasknodetype_endTasks_setter(instance):
    original = instance.endTasks
    instance.endTasks = original
    assert instance.endTasks == original



@given(instance=jpdl31_TaskNodeType_strategy)
def test_jpdl31_tasknodetype_createTasks_setter(instance):
    original = instance.createTasks
    instance.createTasks = original
    assert instance.createTasks == original



@given(instance=jpdl31_TaskNodeType_strategy)
def test_jpdl31_tasknodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_TaskType_strategy)
@settings(max_examples=50)
def test_jpdl31_tasktype_instantiation(instance):
    assert isinstance(instance, jpdl31_TaskType)



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_swimlane_setter(instance):
    original = instance.swimlane
    instance.swimlane = original
    assert instance.swimlane == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_blocking_setter(instance):
    original = instance.blocking
    instance.blocking = original
    assert instance.blocking == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_signalling_setter(instance):
    original = instance.signalling
    instance.signalling = original
    assert instance.signalling == original



@given(instance=jpdl31_TaskType_strategy)
def test_jpdl31_tasktype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=jpdl31_SwimlaneType_strategy)
@settings(max_examples=50)
def test_jpdl31_swimlanetype_instantiation(instance):
    assert isinstance(instance, jpdl31_SwimlaneType)



@given(instance=jpdl31_SwimlaneType_strategy)
def test_jpdl31_swimlanetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_ProcessDefinitionType_strategy)
@settings(max_examples=50)
def test_jpdl31_processdefinitiontype_instantiation(instance):
    assert isinstance(instance, jpdl31_ProcessDefinitionType)



@given(instance=jpdl31_ProcessDefinitionType_strategy)
def test_jpdl31_processdefinitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_ProcessDefinitionType_strategy)
def test_jpdl31_processdefinitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31_NodeType_strategy)
@settings(max_examples=50)
def test_jpdl31_nodetype_instantiation(instance):
    assert isinstance(instance, jpdl31_NodeType)



@given(instance=jpdl31_NodeType_strategy)
def test_jpdl31_nodetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original



@given(instance=jpdl31_NodeType_strategy)
def test_jpdl31_nodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_NodeType_strategy)
def test_jpdl31_nodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31_ProcessStateType_strategy)
@settings(max_examples=50)
def test_jpdl31_processstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31_ProcessStateType)



@given(instance=jpdl31_ProcessStateType_strategy)
def test_jpdl31_processstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_ProcessStateType_strategy)
def test_jpdl31_processstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_ProcessStateType_strategy)
def test_jpdl31_processstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31_EndStateType_strategy)
@settings(max_examples=50)
def test_jpdl31_endstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31_EndStateType)



@given(instance=jpdl31_EndStateType_strategy)
def test_jpdl31_endstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_EndStateType_strategy)
def test_jpdl31_endstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31_JoinType_strategy)
@settings(max_examples=50)
def test_jpdl31_jointype_instantiation(instance):
    assert isinstance(instance, jpdl31_JoinType)



@given(instance=jpdl31_JoinType_strategy)
def test_jpdl31_jointype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_JoinType_strategy)
def test_jpdl31_jointype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_JoinType_strategy)
def test_jpdl31_jointype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl31_ForkType_strategy)
@settings(max_examples=50)
def test_jpdl31_forktype_instantiation(instance):
    assert isinstance(instance, jpdl31_ForkType)



@given(instance=jpdl31_ForkType_strategy)
def test_jpdl31_forktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_ForkType_strategy)
def test_jpdl31_forktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_ForkType_strategy)
def test_jpdl31_forktype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_jpdl31_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, jpdl31_EStringToStringMapEntry)

@given(instance=jpdl31_DocumentRoot_strategy)
@settings(max_examples=50)
def test_jpdl31_documentroot_instantiation(instance):
    assert isinstance(instance, jpdl31_DocumentRoot)



@given(instance=jpdl31_DocumentRoot_strategy)
def test_jpdl31_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl31_TransitionType1_strategy)
@settings(max_examples=50)
def test_jpdl31_transitiontype1_instantiation(instance):
    assert isinstance(instance, jpdl31_TransitionType1)



@given(instance=jpdl31_TransitionType1_strategy)
def test_jpdl31_transitiontype1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_TransitionType1_strategy)
def test_jpdl31_transitiontype1_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=jpdl31_TransitionType1_strategy)
def test_jpdl31_transitiontype1_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31_ExceptionHandlerType_strategy)
@settings(max_examples=50)
def test_jpdl31_exceptionhandlertype_instantiation(instance):
    assert isinstance(instance, jpdl31_ExceptionHandlerType)



@given(instance=jpdl31_ExceptionHandlerType_strategy)
def test_jpdl31_exceptionhandlertype_exceptionClass_setter(instance):
    original = instance.exceptionClass
    instance.exceptionClass = original
    assert instance.exceptionClass == original



@given(instance=jpdl31_ExceptionHandlerType_strategy)
def test_jpdl31_exceptionhandlertype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31_EventType_strategy)
@settings(max_examples=50)
def test_jpdl31_eventtype_instantiation(instance):
    assert isinstance(instance, jpdl31_EventType)



@given(instance=jpdl31_EventType_strategy)
def test_jpdl31_eventtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=jpdl31_EventType_strategy)
def test_jpdl31_eventtype_actionElements_setter(instance):
    original = instance.actionElements
    instance.actionElements = original
    assert instance.actionElements == original

@given(instance=jpdl31_Delegation_strategy)
@settings(max_examples=50)
def test_jpdl31_delegation_instantiation(instance):
    assert isinstance(instance, jpdl31_Delegation)



@given(instance=jpdl31_Delegation_strategy)
def test_jpdl31_delegation_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original



@given(instance=jpdl31_Delegation_strategy)
def test_jpdl31_delegation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl31_Delegation_strategy)
def test_jpdl31_delegation_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=jpdl31_Delegation_strategy)
def test_jpdl31_delegation_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31_DecisionType_strategy)
@settings(max_examples=50)
def test_jpdl31_decisiontype_instantiation(instance):
    assert isinstance(instance, jpdl31_DecisionType)



@given(instance=jpdl31_DecisionType_strategy)
def test_jpdl31_decisiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_DecisionType_strategy)
def test_jpdl31_decisiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_DecisionType_strategy)
def test_jpdl31_decisiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_DecisionType_strategy)
def test_jpdl31_decisiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31_ScriptType_strategy)
@settings(max_examples=50)
def test_jpdl31_scripttype_instantiation(instance):
    assert isinstance(instance, jpdl31_ScriptType)



@given(instance=jpdl31_ScriptType_strategy)
def test_jpdl31_scripttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_ScriptType_strategy)
def test_jpdl31_scripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl31_ScriptType_strategy)
def test_jpdl31_scripttype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original



@given(instance=jpdl31_ScriptType_strategy)
def test_jpdl31_scripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31_CreateTimerType_strategy)
@settings(max_examples=50)
def test_jpdl31_createtimertype_instantiation(instance):
    assert isinstance(instance, jpdl31_CreateTimerType)



@given(instance=jpdl31_CreateTimerType_strategy)
def test_jpdl31_createtimertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original



@given(instance=jpdl31_CreateTimerType_strategy)
def test_jpdl31_createtimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_CreateTimerType_strategy)
def test_jpdl31_createtimertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=jpdl31_CreateTimerType_strategy)
def test_jpdl31_createtimertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl31_ConditionType_strategy)
@settings(max_examples=50)
def test_jpdl31_conditiontype_instantiation(instance):
    assert isinstance(instance, jpdl31_ConditionType)



@given(instance=jpdl31_ConditionType_strategy)
def test_jpdl31_conditiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl31_ConditionType_strategy)
def test_jpdl31_conditiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl31_ConditionType_strategy)
def test_jpdl31_conditiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl31_ConditionType_strategy)
def test_jpdl31_conditiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31_CancelTimerType_strategy)
@settings(max_examples=50)
def test_jpdl31_canceltimertype_instantiation(instance):
    assert isinstance(instance, jpdl31_CancelTimerType)



@given(instance=jpdl31_CancelTimerType_strategy)
def test_jpdl31_canceltimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Delegation_strategy)
@settings(max_examples=50)
def test_delegation_instantiation(instance):
    assert isinstance(instance, Delegation)

@given(instance=jpdl31_AssignmentType_strategy)
@settings(max_examples=50)
def test_jpdl31_assignmenttype_instantiation(instance):
    assert isinstance(instance, jpdl31_AssignmentType)



@given(instance=jpdl31_AssignmentType_strategy)
def test_jpdl31_assignmenttype_actorId_setter(instance):
    original = instance.actorId
    instance.actorId = original
    assert instance.actorId == original



@given(instance=jpdl31_AssignmentType_strategy)
def test_jpdl31_assignmenttype_pooledActors_setter(instance):
    original = instance.pooledActors
    instance.pooledActors = original
    assert instance.pooledActors == original



@given(instance=jpdl31_AssignmentType_strategy)
def test_jpdl31_assignmenttype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31_ActionType_strategy)
@settings(max_examples=50)
def test_jpdl31_actiontype_instantiation(instance):
    assert isinstance(instance, jpdl31_ActionType)



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_refName_setter(instance):
    original = instance.refName
    instance.refName = original
    assert instance.refName == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl31_ActionType_strategy)
def test_jpdl31_actiontype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original
