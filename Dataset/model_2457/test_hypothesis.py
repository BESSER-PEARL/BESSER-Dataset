import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    jpdl32_ReminderType,
    jpdl32_SubProcessType,
    jpdl32_VariableType,
    jpdl32_TimerType,
    jpdl32_TaskNodeType,
    jpdl32_TaskType,
    jpdl32_SwimlaneType,
    jpdl32_SuperStateType,
    jpdl32_StateType,
    jpdl32_StartStateType,
    jpdl32_ProcessStateType,
    jpdl32_ProcessDefinitionType,
    jpdl32_NodeType,
    jpdl32_MailNodeType,
    jpdl32_MailType,
    jpdl32_JoinType,
    jpdl32_ForkType,
    jpdl32_EndStateType,
    jpdl32_EStringToStringMapEntry,
    jpdl32_DocumentRoot,
    jpdl32_TransitionType,
    jpdl32_ExceptionHandlerType,
    jpdl32_EventType,
    jpdl32_Delegation,
    jpdl32_DecisionType,
    jpdl32_ScriptType,
    jpdl32_CreateTimerType,
    jpdl32_ConditionType,
    jpdl32_CancelTimerType,
    Delegation,
    jpdl32_AssignmentType,
    jpdl32_ActionType,
    BindingType,
    SignalType,
    TypeTypeMember1,
    ConfigType,
    PriorityTypeMember0,
    BooleanType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jpdl32_remindertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ReminderType)


def test_jpdl32_remindertype_constructor_exists():
    assert callable(jpdl32_ReminderType.__init__)


def test_jpdl32_remindertype_constructor_args():
    sig = inspect.signature(jpdl32_ReminderType.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "duedate" in params, "Missing parameter 'duedate'"

def test_jpdl32_remindertype_has_repeat():
    assert hasattr(jpdl32_ReminderType, "repeat")
    descriptor = None
    for klass in jpdl32_ReminderType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_remindertype_has_duedate():
    assert hasattr(jpdl32_ReminderType, "duedate")
    descriptor = None
    for klass in jpdl32_ReminderType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_subprocesstype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_SubProcessType)


def test_jpdl32_subprocesstype_constructor_exists():
    assert callable(jpdl32_SubProcessType.__init__)


def test_jpdl32_subprocesstype_constructor_args():
    sig = inspect.signature(jpdl32_SubProcessType.__init__)
    params = list(sig.parameters.keys())
    assert "binding" in params, "Missing parameter 'binding'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_jpdl32_subprocesstype_has_binding():
    assert hasattr(jpdl32_SubProcessType, "binding")
    descriptor = None
    for klass in jpdl32_SubProcessType.__mro__:
        if "binding" in klass.__dict__:
            descriptor = klass.__dict__["binding"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_subprocesstype_has_name():
    assert hasattr(jpdl32_SubProcessType, "name")
    descriptor = None
    for klass in jpdl32_SubProcessType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_subprocesstype_has_version():
    assert hasattr(jpdl32_SubProcessType, "version")
    descriptor = None
    for klass in jpdl32_SubProcessType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_variabletype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_VariableType)


def test_jpdl32_variabletype_constructor_exists():
    assert callable(jpdl32_VariableType.__init__)


def test_jpdl32_variabletype_constructor_args():
    sig = inspect.signature(jpdl32_VariableType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "access" in params, "Missing parameter 'access'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mappedName" in params, "Missing parameter 'mappedName'"

def test_jpdl32_variabletype_has_any():
    assert hasattr(jpdl32_VariableType, "any")
    descriptor = None
    for klass in jpdl32_VariableType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_variabletype_has_access():
    assert hasattr(jpdl32_VariableType, "access")
    descriptor = None
    for klass in jpdl32_VariableType.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_variabletype_has_name():
    assert hasattr(jpdl32_VariableType, "name")
    descriptor = None
    for klass in jpdl32_VariableType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_variabletype_has_mappedName():
    assert hasattr(jpdl32_VariableType, "mappedName")
    descriptor = None
    for klass in jpdl32_VariableType.__mro__:
        if "mappedName" in klass.__dict__:
            descriptor = klass.__dict__["mappedName"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_timertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_TimerType)


def test_jpdl32_timertype_constructor_exists():
    assert callable(jpdl32_TimerType.__init__)


def test_jpdl32_timertype_constructor_args():
    sig = inspect.signature(jpdl32_TimerType.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "transition" in params, "Missing parameter 'transition'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_timertype_has_repeat():
    assert hasattr(jpdl32_TimerType, "repeat")
    descriptor = None
    for klass in jpdl32_TimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_timertype_has_duedate():
    assert hasattr(jpdl32_TimerType, "duedate")
    descriptor = None
    for klass in jpdl32_TimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_timertype_has_transition():
    assert hasattr(jpdl32_TimerType, "transition")
    descriptor = None
    for klass in jpdl32_TimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_timertype_has_name():
    assert hasattr(jpdl32_TimerType, "name")
    descriptor = None
    for klass in jpdl32_TimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_tasknodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_TaskNodeType)


def test_jpdl32_tasknodetype_constructor_exists():
    assert callable(jpdl32_TaskNodeType.__init__)


def test_jpdl32_tasknodetype_constructor_args():
    sig = inspect.signature(jpdl32_TaskNodeType.__init__)
    params = list(sig.parameters.keys())
    assert "endTasks" in params, "Missing parameter 'endTasks'"
    assert "group" in params, "Missing parameter 'group'"
    assert "createTasks" in params, "Missing parameter 'createTasks'"
    assert "name" in params, "Missing parameter 'name'"
    assert "signal" in params, "Missing parameter 'signal'"
    assert "description" in params, "Missing parameter 'description'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32_tasknodetype_has_endTasks():
    assert hasattr(jpdl32_TaskNodeType, "endTasks")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "endTasks" in klass.__dict__:
            descriptor = klass.__dict__["endTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasknodetype_has_group():
    assert hasattr(jpdl32_TaskNodeType, "group")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasknodetype_has_createTasks():
    assert hasattr(jpdl32_TaskNodeType, "createTasks")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "createTasks" in klass.__dict__:
            descriptor = klass.__dict__["createTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasknodetype_has_name():
    assert hasattr(jpdl32_TaskNodeType, "name")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasknodetype_has_signal():
    assert hasattr(jpdl32_TaskNodeType, "signal")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasknodetype_has_description():
    assert hasattr(jpdl32_TaskNodeType, "description")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasknodetype_has_async_():
    assert hasattr(jpdl32_TaskNodeType, "async_")
    descriptor = None
    for klass in jpdl32_TaskNodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_tasktype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_TaskType)


def test_jpdl32_tasktype_constructor_exists():
    assert callable(jpdl32_TaskType.__init__)


def test_jpdl32_tasktype_constructor_args():
    sig = inspect.signature(jpdl32_TaskType.__init__)
    params = list(sig.parameters.keys())
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "description" in params, "Missing parameter 'description'"
    assert "blocking" in params, "Missing parameter 'blocking'"
    assert "signalling" in params, "Missing parameter 'signalling'"
    assert "notify" in params, "Missing parameter 'notify'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"
    assert "swimlane" in params, "Missing parameter 'swimlane'"
    assert "description1" in params, "Missing parameter 'description1'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_jpdl32_tasktype_has_duedate():
    assert hasattr(jpdl32_TaskType, "duedate")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_description():
    assert hasattr(jpdl32_TaskType, "description")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_blocking():
    assert hasattr(jpdl32_TaskType, "blocking")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "blocking" in klass.__dict__:
            descriptor = klass.__dict__["blocking"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_signalling():
    assert hasattr(jpdl32_TaskType, "signalling")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "signalling" in klass.__dict__:
            descriptor = klass.__dict__["signalling"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_notify():
    assert hasattr(jpdl32_TaskType, "notify")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "notify" in klass.__dict__:
            descriptor = klass.__dict__["notify"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_group():
    assert hasattr(jpdl32_TaskType, "group")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_name():
    assert hasattr(jpdl32_TaskType, "name")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_swimlane():
    assert hasattr(jpdl32_TaskType, "swimlane")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "swimlane" in klass.__dict__:
            descriptor = klass.__dict__["swimlane"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_description1():
    assert hasattr(jpdl32_TaskType, "description1")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_tasktype_has_priority():
    assert hasattr(jpdl32_TaskType, "priority")
    descriptor = None
    for klass in jpdl32_TaskType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_swimlanetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_SwimlaneType)


def test_jpdl32_swimlanetype_constructor_exists():
    assert callable(jpdl32_SwimlaneType.__init__)


def test_jpdl32_swimlanetype_constructor_args():
    sig = inspect.signature(jpdl32_SwimlaneType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_swimlanetype_has_name():
    assert hasattr(jpdl32_SwimlaneType, "name")
    descriptor = None
    for klass in jpdl32_SwimlaneType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_superstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_SuperStateType)


def test_jpdl32_superstatetype_constructor_exists():
    assert callable(jpdl32_SuperStateType.__init__)


def test_jpdl32_superstatetype_constructor_args():
    sig = inspect.signature(jpdl32_SuperStateType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_superstatetype_has_async_():
    assert hasattr(jpdl32_SuperStateType, "async_")
    descriptor = None
    for klass in jpdl32_SuperStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_superstatetype_has_group():
    assert hasattr(jpdl32_SuperStateType, "group")
    descriptor = None
    for klass in jpdl32_SuperStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_superstatetype_has_description():
    assert hasattr(jpdl32_SuperStateType, "description")
    descriptor = None
    for klass in jpdl32_SuperStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_superstatetype_has_name():
    assert hasattr(jpdl32_SuperStateType, "name")
    descriptor = None
    for klass in jpdl32_SuperStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_statetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_StateType)


def test_jpdl32_statetype_constructor_exists():
    assert callable(jpdl32_StateType.__init__)


def test_jpdl32_statetype_constructor_args():
    sig = inspect.signature(jpdl32_StateType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32_statetype_has_description():
    assert hasattr(jpdl32_StateType, "description")
    descriptor = None
    for klass in jpdl32_StateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_statetype_has_nodeContentElements():
    assert hasattr(jpdl32_StateType, "nodeContentElements")
    descriptor = None
    for klass in jpdl32_StateType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_statetype_has_name():
    assert hasattr(jpdl32_StateType, "name")
    descriptor = None
    for klass in jpdl32_StateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_statetype_has_async_():
    assert hasattr(jpdl32_StateType, "async_")
    descriptor = None
    for klass in jpdl32_StateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_startstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_StartStateType)


def test_jpdl32_startstatetype_constructor_exists():
    assert callable(jpdl32_StartStateType.__init__)


def test_jpdl32_startstatetype_constructor_args():
    sig = inspect.signature(jpdl32_StartStateType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_startstatetype_has_group():
    assert hasattr(jpdl32_StartStateType, "group")
    descriptor = None
    for klass in jpdl32_StartStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_startstatetype_has_description():
    assert hasattr(jpdl32_StartStateType, "description")
    descriptor = None
    for klass in jpdl32_StartStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_startstatetype_has_name():
    assert hasattr(jpdl32_StartStateType, "name")
    descriptor = None
    for klass in jpdl32_StartStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_processstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ProcessStateType)


def test_jpdl32_processstatetype_constructor_exists():
    assert callable(jpdl32_ProcessStateType.__init__)


def test_jpdl32_processstatetype_constructor_args():
    sig = inspect.signature(jpdl32_ProcessStateType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "binding" in params, "Missing parameter 'binding'"
    assert "group" in params, "Missing parameter 'group'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_processstatetype_has_async_():
    assert hasattr(jpdl32_ProcessStateType, "async_")
    descriptor = None
    for klass in jpdl32_ProcessStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_processstatetype_has_binding():
    assert hasattr(jpdl32_ProcessStateType, "binding")
    descriptor = None
    for klass in jpdl32_ProcessStateType.__mro__:
        if "binding" in klass.__dict__:
            descriptor = klass.__dict__["binding"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_processstatetype_has_group():
    assert hasattr(jpdl32_ProcessStateType, "group")
    descriptor = None
    for klass in jpdl32_ProcessStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_processstatetype_has_description():
    assert hasattr(jpdl32_ProcessStateType, "description")
    descriptor = None
    for klass in jpdl32_ProcessStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_processstatetype_has_name():
    assert hasattr(jpdl32_ProcessStateType, "name")
    descriptor = None
    for klass in jpdl32_ProcessStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ProcessDefinitionType)


def test_jpdl32_processdefinitiontype_constructor_exists():
    assert callable(jpdl32_ProcessDefinitionType.__init__)


def test_jpdl32_processdefinitiontype_constructor_args():
    sig = inspect.signature(jpdl32_ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl32_processdefinitiontype_has_description():
    assert hasattr(jpdl32_ProcessDefinitionType, "description")
    descriptor = None
    for klass in jpdl32_ProcessDefinitionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_processdefinitiontype_has_name():
    assert hasattr(jpdl32_ProcessDefinitionType, "name")
    descriptor = None
    for klass in jpdl32_ProcessDefinitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_processdefinitiontype_has_group():
    assert hasattr(jpdl32_ProcessDefinitionType, "group")
    descriptor = None
    for klass in jpdl32_ProcessDefinitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_nodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_NodeType)


def test_jpdl32_nodetype_constructor_exists():
    assert callable(jpdl32_NodeType.__init__)


def test_jpdl32_nodetype_constructor_args():
    sig = inspect.signature(jpdl32_NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32_nodetype_has_name():
    assert hasattr(jpdl32_NodeType, "name")
    descriptor = None
    for klass in jpdl32_NodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_nodetype_has_description():
    assert hasattr(jpdl32_NodeType, "description")
    descriptor = None
    for klass in jpdl32_NodeType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_nodetype_has_nodeContentElements():
    assert hasattr(jpdl32_NodeType, "nodeContentElements")
    descriptor = None
    for klass in jpdl32_NodeType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_nodetype_has_async_():
    assert hasattr(jpdl32_NodeType, "async_")
    descriptor = None
    for klass in jpdl32_NodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_mailnodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_MailNodeType)


def test_jpdl32_mailnodetype_constructor_exists():
    assert callable(jpdl32_MailNodeType.__init__)


def test_jpdl32_mailnodetype_constructor_args():
    sig = inspect.signature(jpdl32_MailNodeType.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "subject1" in params, "Missing parameter 'subject1'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "text1" in params, "Missing parameter 'text1'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "text" in params, "Missing parameter 'text'"
    assert "actors" in params, "Missing parameter 'actors'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "description" in params, "Missing parameter 'description'"
    assert "template" in params, "Missing parameter 'template'"

def test_jpdl32_mailnodetype_has_to():
    assert hasattr(jpdl32_MailNodeType, "to")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_subject1():
    assert hasattr(jpdl32_MailNodeType, "subject1")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "subject1" in klass.__dict__:
            descriptor = klass.__dict__["subject1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_async_():
    assert hasattr(jpdl32_MailNodeType, "async_")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_text1():
    assert hasattr(jpdl32_MailNodeType, "text1")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "text1" in klass.__dict__:
            descriptor = klass.__dict__["text1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_name():
    assert hasattr(jpdl32_MailNodeType, "name")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_group():
    assert hasattr(jpdl32_MailNodeType, "group")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_text():
    assert hasattr(jpdl32_MailNodeType, "text")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_actors():
    assert hasattr(jpdl32_MailNodeType, "actors")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_subject():
    assert hasattr(jpdl32_MailNodeType, "subject")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_description():
    assert hasattr(jpdl32_MailNodeType, "description")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailnodetype_has_template():
    assert hasattr(jpdl32_MailNodeType, "template")
    descriptor = None
    for klass in jpdl32_MailNodeType.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_mailtype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_MailType)


def test_jpdl32_mailtype_constructor_exists():
    assert callable(jpdl32_MailType.__init__)


def test_jpdl32_mailtype_constructor_args():
    sig = inspect.signature(jpdl32_MailType.__init__)
    params = list(sig.parameters.keys())
    assert "text1" in params, "Missing parameter 'text1'"
    assert "subject1" in params, "Missing parameter 'subject1'"
    assert "to" in params, "Missing parameter 'to'"
    assert "text" in params, "Missing parameter 'text'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "template" in params, "Missing parameter 'template'"
    assert "actors" in params, "Missing parameter 'actors'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl32_mailtype_has_text1():
    assert hasattr(jpdl32_MailType, "text1")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "text1" in klass.__dict__:
            descriptor = klass.__dict__["text1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_subject1():
    assert hasattr(jpdl32_MailType, "subject1")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "subject1" in klass.__dict__:
            descriptor = klass.__dict__["subject1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_to():
    assert hasattr(jpdl32_MailType, "to")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_text():
    assert hasattr(jpdl32_MailType, "text")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_async_():
    assert hasattr(jpdl32_MailType, "async_")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_subject():
    assert hasattr(jpdl32_MailType, "subject")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_template():
    assert hasattr(jpdl32_MailType, "template")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_actors():
    assert hasattr(jpdl32_MailType, "actors")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_name():
    assert hasattr(jpdl32_MailType, "name")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_mailtype_has_group():
    assert hasattr(jpdl32_MailType, "group")
    descriptor = None
    for klass in jpdl32_MailType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_jointype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_JoinType)


def test_jpdl32_jointype_constructor_exists():
    assert callable(jpdl32_JoinType.__init__)


def test_jpdl32_jointype_constructor_args():
    sig = inspect.signature(jpdl32_JoinType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"

def test_jpdl32_jointype_has_description():
    assert hasattr(jpdl32_JoinType, "description")
    descriptor = None
    for klass in jpdl32_JoinType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_jointype_has_async_():
    assert hasattr(jpdl32_JoinType, "async_")
    descriptor = None
    for klass in jpdl32_JoinType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_jointype_has_name():
    assert hasattr(jpdl32_JoinType, "name")
    descriptor = None
    for klass in jpdl32_JoinType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_jointype_has_nodeContentElements():
    assert hasattr(jpdl32_JoinType, "nodeContentElements")
    descriptor = None
    for klass in jpdl32_JoinType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_forktype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ForkType)


def test_jpdl32_forktype_constructor_exists():
    assert callable(jpdl32_ForkType.__init__)


def test_jpdl32_forktype_constructor_args():
    sig = inspect.signature(jpdl32_ForkType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "description" in params, "Missing parameter 'description'"

def test_jpdl32_forktype_has_group():
    assert hasattr(jpdl32_ForkType, "group")
    descriptor = None
    for klass in jpdl32_ForkType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_forktype_has_name():
    assert hasattr(jpdl32_ForkType, "name")
    descriptor = None
    for klass in jpdl32_ForkType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_forktype_has_async_():
    assert hasattr(jpdl32_ForkType, "async_")
    descriptor = None
    for klass in jpdl32_ForkType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_forktype_has_description():
    assert hasattr(jpdl32_ForkType, "description")
    descriptor = None
    for klass in jpdl32_ForkType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_endstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_EndStateType)


def test_jpdl32_endstatetype_constructor_exists():
    assert callable(jpdl32_EndStateType.__init__)


def test_jpdl32_endstatetype_constructor_args():
    sig = inspect.signature(jpdl32_EndStateType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "group" in params, "Missing parameter 'group'"
    assert "endCompleteProcess" in params, "Missing parameter 'endCompleteProcess'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_endstatetype_has_description():
    assert hasattr(jpdl32_EndStateType, "description")
    descriptor = None
    for klass in jpdl32_EndStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_endstatetype_has_group():
    assert hasattr(jpdl32_EndStateType, "group")
    descriptor = None
    for klass in jpdl32_EndStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_endstatetype_has_endCompleteProcess():
    assert hasattr(jpdl32_EndStateType, "endCompleteProcess")
    descriptor = None
    for klass in jpdl32_EndStateType.__mro__:
        if "endCompleteProcess" in klass.__dict__:
            descriptor = klass.__dict__["endCompleteProcess"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_endstatetype_has_name():
    assert hasattr(jpdl32_EndStateType, "name")
    descriptor = None
    for klass in jpdl32_EndStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(jpdl32_EStringToStringMapEntry)


def test_jpdl32_estringtostringmapentry_constructor_exists():
    assert callable(jpdl32_EStringToStringMapEntry.__init__)


def test_jpdl32_estringtostringmapentry_constructor_args():
    sig = inspect.signature(jpdl32_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpdl32_documentroot_is_not_abstract():
    assert not inspect.isabstract(jpdl32_DocumentRoot)


def test_jpdl32_documentroot_constructor_exists():
    assert callable(jpdl32_DocumentRoot.__init__)


def test_jpdl32_documentroot_constructor_args():
    sig = inspect.signature(jpdl32_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "recipients" in params, "Missing parameter 'recipients'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "description" in params, "Missing parameter 'description'"
    assert "to" in params, "Missing parameter 'to'"
    assert "template" in params, "Missing parameter 'template'"
    assert "text" in params, "Missing parameter 'text'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_jpdl32_documentroot_has_recipients():
    assert hasattr(jpdl32_DocumentRoot, "recipients")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "recipients" in klass.__dict__:
            descriptor = klass.__dict__["recipients"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_documentroot_has_subject():
    assert hasattr(jpdl32_DocumentRoot, "subject")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_documentroot_has_description():
    assert hasattr(jpdl32_DocumentRoot, "description")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_documentroot_has_to():
    assert hasattr(jpdl32_DocumentRoot, "to")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_documentroot_has_template():
    assert hasattr(jpdl32_DocumentRoot, "template")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_documentroot_has_text():
    assert hasattr(jpdl32_DocumentRoot, "text")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_documentroot_has_mixed():
    assert hasattr(jpdl32_DocumentRoot, "mixed")
    descriptor = None
    for klass in jpdl32_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_transitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_TransitionType)


def test_jpdl32_transitiontype_constructor_exists():
    assert callable(jpdl32_TransitionType.__init__)


def test_jpdl32_transitiontype_constructor_args():
    sig = inspect.signature(jpdl32_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "to" in params, "Missing parameter 'to'"

def test_jpdl32_transitiontype_has_description():
    assert hasattr(jpdl32_TransitionType, "description")
    descriptor = None
    for klass in jpdl32_TransitionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_transitiontype_has_name():
    assert hasattr(jpdl32_TransitionType, "name")
    descriptor = None
    for klass in jpdl32_TransitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_transitiontype_has_group():
    assert hasattr(jpdl32_TransitionType, "group")
    descriptor = None
    for klass in jpdl32_TransitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_transitiontype_has_to():
    assert hasattr(jpdl32_TransitionType, "to")
    descriptor = None
    for klass in jpdl32_TransitionType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_exceptionhandlertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ExceptionHandlerType)


def test_jpdl32_exceptionhandlertype_constructor_exists():
    assert callable(jpdl32_ExceptionHandlerType.__init__)


def test_jpdl32_exceptionhandlertype_constructor_args():
    sig = inspect.signature(jpdl32_ExceptionHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionClass" in params, "Missing parameter 'exceptionClass'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl32_exceptionhandlertype_has_exceptionClass():
    assert hasattr(jpdl32_ExceptionHandlerType, "exceptionClass")
    descriptor = None
    for klass in jpdl32_ExceptionHandlerType.__mro__:
        if "exceptionClass" in klass.__dict__:
            descriptor = klass.__dict__["exceptionClass"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_exceptionhandlertype_has_group():
    assert hasattr(jpdl32_ExceptionHandlerType, "group")
    descriptor = None
    for klass in jpdl32_ExceptionHandlerType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_eventtype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_EventType)


def test_jpdl32_eventtype_constructor_exists():
    assert callable(jpdl32_EventType.__init__)


def test_jpdl32_eventtype_constructor_args():
    sig = inspect.signature(jpdl32_EventType.__init__)
    params = list(sig.parameters.keys())
    assert "actionElements" in params, "Missing parameter 'actionElements'"
    assert "type" in params, "Missing parameter 'type'"

def test_jpdl32_eventtype_has_actionElements():
    assert hasattr(jpdl32_EventType, "actionElements")
    descriptor = None
    for klass in jpdl32_EventType.__mro__:
        if "actionElements" in klass.__dict__:
            descriptor = klass.__dict__["actionElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_eventtype_has_type():
    assert hasattr(jpdl32_EventType, "type")
    descriptor = None
    for klass in jpdl32_EventType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_delegation_is_not_abstract():
    assert not inspect.isabstract(jpdl32_Delegation)


def test_jpdl32_delegation_constructor_exists():
    assert callable(jpdl32_Delegation.__init__)


def test_jpdl32_delegation_constructor_args():
    sig = inspect.signature(jpdl32_Delegation.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "configType" in params, "Missing parameter 'configType'"

def test_jpdl32_delegation_has_any():
    assert hasattr(jpdl32_Delegation, "any")
    descriptor = None
    for klass in jpdl32_Delegation.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_delegation_has_mixed():
    assert hasattr(jpdl32_Delegation, "mixed")
    descriptor = None
    for klass in jpdl32_Delegation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_delegation_has_class_():
    assert hasattr(jpdl32_Delegation, "class_")
    descriptor = None
    for klass in jpdl32_Delegation.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_delegation_has_configType():
    assert hasattr(jpdl32_Delegation, "configType")
    descriptor = None
    for klass in jpdl32_Delegation.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_decisiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_DecisionType)


def test_jpdl32_decisiontype_constructor_exists():
    assert callable(jpdl32_DecisionType.__init__)


def test_jpdl32_decisiontype_constructor_args():
    sig = inspect.signature(jpdl32_DecisionType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_decisiontype_has_async_():
    assert hasattr(jpdl32_DecisionType, "async_")
    descriptor = None
    for klass in jpdl32_DecisionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_decisiontype_has_group():
    assert hasattr(jpdl32_DecisionType, "group")
    descriptor = None
    for klass in jpdl32_DecisionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_decisiontype_has_expression():
    assert hasattr(jpdl32_DecisionType, "expression")
    descriptor = None
    for klass in jpdl32_DecisionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_decisiontype_has_description():
    assert hasattr(jpdl32_DecisionType, "description")
    descriptor = None
    for klass in jpdl32_DecisionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_decisiontype_has_name():
    assert hasattr(jpdl32_DecisionType, "name")
    descriptor = None
    for klass in jpdl32_DecisionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_scripttype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ScriptType)


def test_jpdl32_scripttype_constructor_exists():
    assert callable(jpdl32_ScriptType.__init__)


def test_jpdl32_scripttype_constructor_args():
    sig = inspect.signature(jpdl32_ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_scripttype_has_acceptPropagatedEvents():
    assert hasattr(jpdl32_ScriptType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl32_ScriptType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_scripttype_has_mixed():
    assert hasattr(jpdl32_ScriptType, "mixed")
    descriptor = None
    for klass in jpdl32_ScriptType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_scripttype_has_any():
    assert hasattr(jpdl32_ScriptType, "any")
    descriptor = None
    for klass in jpdl32_ScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_scripttype_has_name():
    assert hasattr(jpdl32_ScriptType, "name")
    descriptor = None
    for klass in jpdl32_ScriptType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_createtimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_CreateTimerType)


def test_jpdl32_createtimertype_constructor_exists():
    assert callable(jpdl32_CreateTimerType.__init__)


def test_jpdl32_createtimertype_constructor_args():
    sig = inspect.signature(jpdl32_CreateTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "name" in params, "Missing parameter 'name'"
    assert "transition" in params, "Missing parameter 'transition'"
    assert "duedate" in params, "Missing parameter 'duedate'"

def test_jpdl32_createtimertype_has_repeat():
    assert hasattr(jpdl32_CreateTimerType, "repeat")
    descriptor = None
    for klass in jpdl32_CreateTimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_createtimertype_has_name():
    assert hasattr(jpdl32_CreateTimerType, "name")
    descriptor = None
    for klass in jpdl32_CreateTimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_createtimertype_has_transition():
    assert hasattr(jpdl32_CreateTimerType, "transition")
    descriptor = None
    for klass in jpdl32_CreateTimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_createtimertype_has_duedate():
    assert hasattr(jpdl32_CreateTimerType, "duedate")
    descriptor = None
    for klass in jpdl32_CreateTimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_conditiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ConditionType)


def test_jpdl32_conditiontype_constructor_exists():
    assert callable(jpdl32_ConditionType.__init__)


def test_jpdl32_conditiontype_constructor_args():
    sig = inspect.signature(jpdl32_ConditionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_jpdl32_conditiontype_has_any():
    assert hasattr(jpdl32_ConditionType, "any")
    descriptor = None
    for klass in jpdl32_ConditionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_conditiontype_has_group():
    assert hasattr(jpdl32_ConditionType, "group")
    descriptor = None
    for klass in jpdl32_ConditionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_conditiontype_has_mixed():
    assert hasattr(jpdl32_ConditionType, "mixed")
    descriptor = None
    for klass in jpdl32_ConditionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_conditiontype_has_expression():
    assert hasattr(jpdl32_ConditionType, "expression")
    descriptor = None
    for klass in jpdl32_ConditionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_canceltimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_CancelTimerType)


def test_jpdl32_canceltimertype_constructor_exists():
    assert callable(jpdl32_CancelTimerType.__init__)


def test_jpdl32_canceltimertype_constructor_args():
    sig = inspect.signature(jpdl32_CancelTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32_canceltimertype_has_name():
    assert hasattr(jpdl32_CancelTimerType, "name")
    descriptor = None
    for klass in jpdl32_CancelTimerType.__mro__:
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



def test_jpdl32_assignmenttype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_AssignmentType)


def test_jpdl32_assignmenttype_constructor_exists():
    assert callable(jpdl32_AssignmentType.__init__)


def test_jpdl32_assignmenttype_constructor_args():
    sig = inspect.signature(jpdl32_AssignmentType.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "actorId" in params, "Missing parameter 'actorId'"
    assert "pooledActors" in params, "Missing parameter 'pooledActors'"

def test_jpdl32_assignmenttype_has_expression():
    assert hasattr(jpdl32_AssignmentType, "expression")
    descriptor = None
    for klass in jpdl32_AssignmentType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_assignmenttype_has_actorId():
    assert hasattr(jpdl32_AssignmentType, "actorId")
    descriptor = None
    for klass in jpdl32_AssignmentType.__mro__:
        if "actorId" in klass.__dict__:
            descriptor = klass.__dict__["actorId"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_assignmenttype_has_pooledActors():
    assert hasattr(jpdl32_AssignmentType, "pooledActors")
    descriptor = None
    for klass in jpdl32_AssignmentType.__mro__:
        if "pooledActors" in klass.__dict__:
            descriptor = klass.__dict__["pooledActors"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32_actiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32_ActionType)


def test_jpdl32_actiontype_constructor_exists():
    assert callable(jpdl32_ActionType.__init__)


def test_jpdl32_actiontype_constructor_args():
    sig = inspect.signature(jpdl32_ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"
    assert "configType" in params, "Missing parameter 'configType'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "refName" in params, "Missing parameter 'refName'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32_actiontype_has_acceptPropagatedEvents():
    assert hasattr(jpdl32_ActionType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_mixed():
    assert hasattr(jpdl32_ActionType, "mixed")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_class_():
    assert hasattr(jpdl32_ActionType, "class_")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_any():
    assert hasattr(jpdl32_ActionType, "any")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_name():
    assert hasattr(jpdl32_ActionType, "name")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_configType():
    assert hasattr(jpdl32_ActionType, "configType")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_expression():
    assert hasattr(jpdl32_ActionType, "expression")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_refName():
    assert hasattr(jpdl32_ActionType, "refName")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "refName" in klass.__dict__:
            descriptor = klass.__dict__["refName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32_actiontype_has_async_():
    assert hasattr(jpdl32_ActionType, "async_")
    descriptor = None
    for klass in jpdl32_ActionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_bindingtype_exists():
    # Check that the Enumeration exists
    assert BindingType is not None

def test_bindingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingType]
    expected_literals = [
        "early",
        "late",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingType"

def test_signaltype_exists():
    # Check that the Enumeration exists
    assert SignalType is not None

def test_signaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalType]
    expected_literals = [
        "unsynchronized",
        "lastWait",
        "last",
        "firstWait",
        "first",
        "never",
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
        "nodeEnter",
        "taskCreate",
        "superstateEnter",
        "superstateLeave",
        "subprocessEnd",
        "processEnd",
        "afterSignal",
        "taskStart",
        "timerCreate",
        "taskEnd",
        "beforeSignal",
        "subprocessCreated",
        "nodeLeave",
        "processStart",
        "taskAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeTypeMember1"

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

def test_prioritytypemember0_exists():
    # Check that the Enumeration exists
    assert PriorityTypeMember0 is not None

def test_prioritytypemember0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityTypeMember0]
    expected_literals = [
        "highest",
        "lowest",
        "normal",
        "low",
        "high",
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
        "on",
        "no",
        "true",
        "yes",
        "false",
        "off",
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
jpdl32_ReminderType_strategy = st.builds(
    jpdl32_ReminderType,
    repeat=
        safe_text,
    duedate=
        safe_text
)
jpdl32_SubProcessType_strategy = st.builds(
    jpdl32_SubProcessType,
    binding=
        safe_text,
    name=
        safe_text,
    version=
        safe_text
)
jpdl32_VariableType_strategy = st.builds(
    jpdl32_VariableType,
    any=
        safe_text,
    access=
        safe_text,
    name=
        safe_text,
    mappedName=
        safe_text
)
jpdl32_TimerType_strategy = st.builds(
    jpdl32_TimerType,
    repeat=
        safe_text,
    duedate=
        safe_text,
    transition=
        safe_text,
    name=
        safe_text
)
jpdl32_TaskNodeType_strategy = st.builds(
    jpdl32_TaskNodeType,
    endTasks=
        safe_text,
    group=
        safe_text,
    createTasks=
        safe_text,
    name=
        safe_text,
    signal=
        safe_text,
    description=
        safe_text,
    async_=
        safe_text
)
jpdl32_TaskType_strategy = st.builds(
    jpdl32_TaskType,
    duedate=
        safe_text,
    description=
        safe_text,
    blocking=
        safe_text,
    signalling=
        safe_text,
    notify=
        safe_text,
    group=
        safe_text,
    name=
        safe_text,
    swimlane=
        safe_text,
    description1=
        safe_text,
    priority=
        safe_text
)
jpdl32_SwimlaneType_strategy = st.builds(
    jpdl32_SwimlaneType,
    name=
        safe_text
)
jpdl32_SuperStateType_strategy = st.builds(
    jpdl32_SuperStateType,
    async_=
        safe_text,
    group=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
jpdl32_StateType_strategy = st.builds(
    jpdl32_StateType,
    description=
        safe_text,
    nodeContentElements=
        safe_text,
    name=
        safe_text,
    async_=
        safe_text
)
jpdl32_StartStateType_strategy = st.builds(
    jpdl32_StartStateType,
    group=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
jpdl32_ProcessStateType_strategy = st.builds(
    jpdl32_ProcessStateType,
    async_=
        safe_text,
    binding=
        safe_text,
    group=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
jpdl32_ProcessDefinitionType_strategy = st.builds(
    jpdl32_ProcessDefinitionType,
    description=
        safe_text,
    name=
        safe_text,
    group=
        safe_text
)
jpdl32_NodeType_strategy = st.builds(
    jpdl32_NodeType,
    name=
        safe_text,
    description=
        safe_text,
    nodeContentElements=
        safe_text,
    async_=
        safe_text
)
jpdl32_MailNodeType_strategy = st.builds(
    jpdl32_MailNodeType,
    to=
        safe_text,
    subject1=
        safe_text,
    async_=
        safe_text,
    text1=
        safe_text,
    name=
        safe_text,
    group=
        safe_text,
    text=
        safe_text,
    actors=
        safe_text,
    subject=
        safe_text,
    description=
        safe_text,
    template=
        safe_text
)
jpdl32_MailType_strategy = st.builds(
    jpdl32_MailType,
    text1=
        safe_text,
    subject1=
        safe_text,
    to=
        safe_text,
    text=
        safe_text,
    async_=
        safe_text,
    subject=
        safe_text,
    template=
        safe_text,
    actors=
        safe_text,
    name=
        safe_text,
    group=
        safe_text
)
jpdl32_JoinType_strategy = st.builds(
    jpdl32_JoinType,
    description=
        safe_text,
    async_=
        safe_text,
    name=
        safe_text,
    nodeContentElements=
        safe_text
)
jpdl32_ForkType_strategy = st.builds(
    jpdl32_ForkType,
    group=
        safe_text,
    name=
        safe_text,
    async_=
        safe_text,
    description=
        safe_text
)
jpdl32_EndStateType_strategy = st.builds(
    jpdl32_EndStateType,
    description=
        safe_text,
    group=
        safe_text,
    endCompleteProcess=
        safe_text,
    name=
        safe_text
)
jpdl32_EStringToStringMapEntry_strategy = st.builds(
    jpdl32_EStringToStringMapEntry,
)
jpdl32_DocumentRoot_strategy = st.builds(
    jpdl32_DocumentRoot,
    recipients=
        safe_text,
    subject=
        safe_text,
    description=
        safe_text,
    to=
        safe_text,
    template=
        safe_text,
    text=
        safe_text,
    mixed=
        safe_text
)
jpdl32_TransitionType_strategy = st.builds(
    jpdl32_TransitionType,
    description=
        safe_text,
    name=
        safe_text,
    group=
        safe_text,
    to=
        safe_text
)
jpdl32_ExceptionHandlerType_strategy = st.builds(
    jpdl32_ExceptionHandlerType,
    exceptionClass=
        safe_text,
    group=
        safe_text
)
jpdl32_EventType_strategy = st.builds(
    jpdl32_EventType,
    actionElements=
        safe_text,
    type=
        safe_text
)
jpdl32_Delegation_strategy = st.builds(
    jpdl32_Delegation,
    any=
        safe_text,
    mixed=
        safe_text,
    class_=
        safe_text,
    configType=
        safe_text
)
jpdl32_DecisionType_strategy = st.builds(
    jpdl32_DecisionType,
    async_=
        safe_text,
    group=
        safe_text,
    expression=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
jpdl32_ScriptType_strategy = st.builds(
    jpdl32_ScriptType,
    acceptPropagatedEvents=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text,
    name=
        safe_text
)
jpdl32_CreateTimerType_strategy = st.builds(
    jpdl32_CreateTimerType,
    repeat=
        safe_text,
    name=
        safe_text,
    transition=
        safe_text,
    duedate=
        safe_text
)
jpdl32_ConditionType_strategy = st.builds(
    jpdl32_ConditionType,
    any=
        safe_text,
    group=
        safe_text,
    mixed=
        safe_text,
    expression=
        safe_text
)
jpdl32_CancelTimerType_strategy = st.builds(
    jpdl32_CancelTimerType,
    name=
        safe_text
)
Delegation_strategy = st.builds(
    Delegation,
)
jpdl32_AssignmentType_strategy = st.builds(
    jpdl32_AssignmentType,
    expression=
        safe_text,
    actorId=
        safe_text,
    pooledActors=
        safe_text
)
jpdl32_ActionType_strategy = st.builds(
    jpdl32_ActionType,
    acceptPropagatedEvents=
        safe_text,
    mixed=
        safe_text,
    class_=
        safe_text,
    any=
        safe_text,
    name=
        safe_text,
    configType=
        safe_text,
    expression=
        safe_text,
    refName=
        safe_text,
    async_=
        safe_text
)

@given(instance=jpdl32_ReminderType_strategy)
@settings(max_examples=50)
def test_jpdl32_remindertype_instantiation(instance):
    assert isinstance(instance, jpdl32_ReminderType)



@given(instance=jpdl32_ReminderType_strategy)
def test_jpdl32_remindertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=jpdl32_ReminderType_strategy)
def test_jpdl32_remindertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl32_SubProcessType_strategy)
@settings(max_examples=50)
def test_jpdl32_subprocesstype_instantiation(instance):
    assert isinstance(instance, jpdl32_SubProcessType)



@given(instance=jpdl32_SubProcessType_strategy)
def test_jpdl32_subprocesstype_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=jpdl32_SubProcessType_strategy)
def test_jpdl32_subprocesstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_SubProcessType_strategy)
def test_jpdl32_subprocesstype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=jpdl32_VariableType_strategy)
@settings(max_examples=50)
def test_jpdl32_variabletype_instantiation(instance):
    assert isinstance(instance, jpdl32_VariableType)



@given(instance=jpdl32_VariableType_strategy)
def test_jpdl32_variabletype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl32_VariableType_strategy)
def test_jpdl32_variabletype_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original



@given(instance=jpdl32_VariableType_strategy)
def test_jpdl32_variabletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_VariableType_strategy)
def test_jpdl32_variabletype_mappedName_setter(instance):
    original = instance.mappedName
    instance.mappedName = original
    assert instance.mappedName == original

@given(instance=jpdl32_TimerType_strategy)
@settings(max_examples=50)
def test_jpdl32_timertype_instantiation(instance):
    assert isinstance(instance, jpdl32_TimerType)



@given(instance=jpdl32_TimerType_strategy)
def test_jpdl32_timertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=jpdl32_TimerType_strategy)
def test_jpdl32_timertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original



@given(instance=jpdl32_TimerType_strategy)
def test_jpdl32_timertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original



@given(instance=jpdl32_TimerType_strategy)
def test_jpdl32_timertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_TaskNodeType_strategy)
@settings(max_examples=50)
def test_jpdl32_tasknodetype_instantiation(instance):
    assert isinstance(instance, jpdl32_TaskNodeType)



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_endTasks_setter(instance):
    original = instance.endTasks
    instance.endTasks = original
    assert instance.endTasks == original



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_createTasks_setter(instance):
    original = instance.createTasks
    instance.createTasks = original
    assert instance.createTasks == original



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_TaskNodeType_strategy)
def test_jpdl32_tasknodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32_TaskType_strategy)
@settings(max_examples=50)
def test_jpdl32_tasktype_instantiation(instance):
    assert isinstance(instance, jpdl32_TaskType)



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_blocking_setter(instance):
    original = instance.blocking
    instance.blocking = original
    assert instance.blocking == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_signalling_setter(instance):
    original = instance.signalling
    instance.signalling = original
    assert instance.signalling == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_notify_setter(instance):
    original = instance.notify
    instance.notify = original
    assert instance.notify == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_swimlane_setter(instance):
    original = instance.swimlane
    instance.swimlane = original
    assert instance.swimlane == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original



@given(instance=jpdl32_TaskType_strategy)
def test_jpdl32_tasktype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=jpdl32_SwimlaneType_strategy)
@settings(max_examples=50)
def test_jpdl32_swimlanetype_instantiation(instance):
    assert isinstance(instance, jpdl32_SwimlaneType)



@given(instance=jpdl32_SwimlaneType_strategy)
def test_jpdl32_swimlanetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_SuperStateType_strategy)
@settings(max_examples=50)
def test_jpdl32_superstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32_SuperStateType)



@given(instance=jpdl32_SuperStateType_strategy)
def test_jpdl32_superstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_SuperStateType_strategy)
def test_jpdl32_superstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_SuperStateType_strategy)
def test_jpdl32_superstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_SuperStateType_strategy)
def test_jpdl32_superstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_StateType_strategy)
@settings(max_examples=50)
def test_jpdl32_statetype_instantiation(instance):
    assert isinstance(instance, jpdl32_StateType)



@given(instance=jpdl32_StateType_strategy)
def test_jpdl32_statetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_StateType_strategy)
def test_jpdl32_statetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original



@given(instance=jpdl32_StateType_strategy)
def test_jpdl32_statetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_StateType_strategy)
def test_jpdl32_statetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32_StartStateType_strategy)
@settings(max_examples=50)
def test_jpdl32_startstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32_StartStateType)



@given(instance=jpdl32_StartStateType_strategy)
def test_jpdl32_startstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_StartStateType_strategy)
def test_jpdl32_startstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_StartStateType_strategy)
def test_jpdl32_startstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_ProcessStateType_strategy)
@settings(max_examples=50)
def test_jpdl32_processstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32_ProcessStateType)



@given(instance=jpdl32_ProcessStateType_strategy)
def test_jpdl32_processstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_ProcessStateType_strategy)
def test_jpdl32_processstatetype_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=jpdl32_ProcessStateType_strategy)
def test_jpdl32_processstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_ProcessStateType_strategy)
def test_jpdl32_processstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_ProcessStateType_strategy)
def test_jpdl32_processstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_ProcessDefinitionType_strategy)
@settings(max_examples=50)
def test_jpdl32_processdefinitiontype_instantiation(instance):
    assert isinstance(instance, jpdl32_ProcessDefinitionType)



@given(instance=jpdl32_ProcessDefinitionType_strategy)
def test_jpdl32_processdefinitiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_ProcessDefinitionType_strategy)
def test_jpdl32_processdefinitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_ProcessDefinitionType_strategy)
def test_jpdl32_processdefinitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32_NodeType_strategy)
@settings(max_examples=50)
def test_jpdl32_nodetype_instantiation(instance):
    assert isinstance(instance, jpdl32_NodeType)



@given(instance=jpdl32_NodeType_strategy)
def test_jpdl32_nodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_NodeType_strategy)
def test_jpdl32_nodetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_NodeType_strategy)
def test_jpdl32_nodetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original



@given(instance=jpdl32_NodeType_strategy)
def test_jpdl32_nodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32_MailNodeType_strategy)
@settings(max_examples=50)
def test_jpdl32_mailnodetype_instantiation(instance):
    assert isinstance(instance, jpdl32_MailNodeType)



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_subject1_setter(instance):
    original = instance.subject1
    instance.subject1 = original
    assert instance.subject1 == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_text1_setter(instance):
    original = instance.text1
    instance.text1 = original
    assert instance.text1 == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_MailNodeType_strategy)
def test_jpdl32_mailnodetype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=jpdl32_MailType_strategy)
@settings(max_examples=50)
def test_jpdl32_mailtype_instantiation(instance):
    assert isinstance(instance, jpdl32_MailType)



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_text1_setter(instance):
    original = instance.text1
    instance.text1 = original
    assert instance.text1 == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_subject1_setter(instance):
    original = instance.subject1
    instance.subject1 = original
    assert instance.subject1 == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_MailType_strategy)
def test_jpdl32_mailtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32_JoinType_strategy)
@settings(max_examples=50)
def test_jpdl32_jointype_instantiation(instance):
    assert isinstance(instance, jpdl32_JoinType)



@given(instance=jpdl32_JoinType_strategy)
def test_jpdl32_jointype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_JoinType_strategy)
def test_jpdl32_jointype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_JoinType_strategy)
def test_jpdl32_jointype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_JoinType_strategy)
def test_jpdl32_jointype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl32_ForkType_strategy)
@settings(max_examples=50)
def test_jpdl32_forktype_instantiation(instance):
    assert isinstance(instance, jpdl32_ForkType)



@given(instance=jpdl32_ForkType_strategy)
def test_jpdl32_forktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_ForkType_strategy)
def test_jpdl32_forktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_ForkType_strategy)
def test_jpdl32_forktype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_ForkType_strategy)
def test_jpdl32_forktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32_EndStateType_strategy)
@settings(max_examples=50)
def test_jpdl32_endstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32_EndStateType)



@given(instance=jpdl32_EndStateType_strategy)
def test_jpdl32_endstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_EndStateType_strategy)
def test_jpdl32_endstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_EndStateType_strategy)
def test_jpdl32_endstatetype_endCompleteProcess_setter(instance):
    original = instance.endCompleteProcess
    instance.endCompleteProcess = original
    assert instance.endCompleteProcess == original



@given(instance=jpdl32_EndStateType_strategy)
def test_jpdl32_endstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_jpdl32_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, jpdl32_EStringToStringMapEntry)

@given(instance=jpdl32_DocumentRoot_strategy)
@settings(max_examples=50)
def test_jpdl32_documentroot_instantiation(instance):
    assert isinstance(instance, jpdl32_DocumentRoot)



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_recipients_setter(instance):
    original = instance.recipients
    instance.recipients = original
    assert instance.recipients == original



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=jpdl32_DocumentRoot_strategy)
def test_jpdl32_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl32_TransitionType_strategy)
@settings(max_examples=50)
def test_jpdl32_transitiontype_instantiation(instance):
    assert isinstance(instance, jpdl32_TransitionType)



@given(instance=jpdl32_TransitionType_strategy)
def test_jpdl32_transitiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_TransitionType_strategy)
def test_jpdl32_transitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_TransitionType_strategy)
def test_jpdl32_transitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_TransitionType_strategy)
def test_jpdl32_transitiontype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl32_ExceptionHandlerType_strategy)
@settings(max_examples=50)
def test_jpdl32_exceptionhandlertype_instantiation(instance):
    assert isinstance(instance, jpdl32_ExceptionHandlerType)



@given(instance=jpdl32_ExceptionHandlerType_strategy)
def test_jpdl32_exceptionhandlertype_exceptionClass_setter(instance):
    original = instance.exceptionClass
    instance.exceptionClass = original
    assert instance.exceptionClass == original



@given(instance=jpdl32_ExceptionHandlerType_strategy)
def test_jpdl32_exceptionhandlertype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32_EventType_strategy)
@settings(max_examples=50)
def test_jpdl32_eventtype_instantiation(instance):
    assert isinstance(instance, jpdl32_EventType)



@given(instance=jpdl32_EventType_strategy)
def test_jpdl32_eventtype_actionElements_setter(instance):
    original = instance.actionElements
    instance.actionElements = original
    assert instance.actionElements == original



@given(instance=jpdl32_EventType_strategy)
def test_jpdl32_eventtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jpdl32_Delegation_strategy)
@settings(max_examples=50)
def test_jpdl32_delegation_instantiation(instance):
    assert isinstance(instance, jpdl32_Delegation)



@given(instance=jpdl32_Delegation_strategy)
def test_jpdl32_delegation_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl32_Delegation_strategy)
def test_jpdl32_delegation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl32_Delegation_strategy)
def test_jpdl32_delegation_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=jpdl32_Delegation_strategy)
def test_jpdl32_delegation_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original

@given(instance=jpdl32_DecisionType_strategy)
@settings(max_examples=50)
def test_jpdl32_decisiontype_instantiation(instance):
    assert isinstance(instance, jpdl32_DecisionType)



@given(instance=jpdl32_DecisionType_strategy)
def test_jpdl32_decisiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=jpdl32_DecisionType_strategy)
def test_jpdl32_decisiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_DecisionType_strategy)
def test_jpdl32_decisiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=jpdl32_DecisionType_strategy)
def test_jpdl32_decisiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=jpdl32_DecisionType_strategy)
def test_jpdl32_decisiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_ScriptType_strategy)
@settings(max_examples=50)
def test_jpdl32_scripttype_instantiation(instance):
    assert isinstance(instance, jpdl32_ScriptType)



@given(instance=jpdl32_ScriptType_strategy)
def test_jpdl32_scripttype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original



@given(instance=jpdl32_ScriptType_strategy)
def test_jpdl32_scripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl32_ScriptType_strategy)
def test_jpdl32_scripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl32_ScriptType_strategy)
def test_jpdl32_scripttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32_CreateTimerType_strategy)
@settings(max_examples=50)
def test_jpdl32_createtimertype_instantiation(instance):
    assert isinstance(instance, jpdl32_CreateTimerType)



@given(instance=jpdl32_CreateTimerType_strategy)
def test_jpdl32_createtimertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=jpdl32_CreateTimerType_strategy)
def test_jpdl32_createtimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_CreateTimerType_strategy)
def test_jpdl32_createtimertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original



@given(instance=jpdl32_CreateTimerType_strategy)
def test_jpdl32_createtimertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl32_ConditionType_strategy)
@settings(max_examples=50)
def test_jpdl32_conditiontype_instantiation(instance):
    assert isinstance(instance, jpdl32_ConditionType)



@given(instance=jpdl32_ConditionType_strategy)
def test_jpdl32_conditiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl32_ConditionType_strategy)
def test_jpdl32_conditiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=jpdl32_ConditionType_strategy)
def test_jpdl32_conditiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl32_ConditionType_strategy)
def test_jpdl32_conditiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl32_CancelTimerType_strategy)
@settings(max_examples=50)
def test_jpdl32_canceltimertype_instantiation(instance):
    assert isinstance(instance, jpdl32_CancelTimerType)



@given(instance=jpdl32_CancelTimerType_strategy)
def test_jpdl32_canceltimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Delegation_strategy)
@settings(max_examples=50)
def test_delegation_instantiation(instance):
    assert isinstance(instance, Delegation)

@given(instance=jpdl32_AssignmentType_strategy)
@settings(max_examples=50)
def test_jpdl32_assignmenttype_instantiation(instance):
    assert isinstance(instance, jpdl32_AssignmentType)



@given(instance=jpdl32_AssignmentType_strategy)
def test_jpdl32_assignmenttype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=jpdl32_AssignmentType_strategy)
def test_jpdl32_assignmenttype_actorId_setter(instance):
    original = instance.actorId
    instance.actorId = original
    assert instance.actorId == original



@given(instance=jpdl32_AssignmentType_strategy)
def test_jpdl32_assignmenttype_pooledActors_setter(instance):
    original = instance.pooledActors
    instance.pooledActors = original
    assert instance.pooledActors == original

@given(instance=jpdl32_ActionType_strategy)
@settings(max_examples=50)
def test_jpdl32_actiontype_instantiation(instance):
    assert isinstance(instance, jpdl32_ActionType)



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_refName_setter(instance):
    original = instance.refName
    instance.refName = original
    assert instance.refName == original



@given(instance=jpdl32_ActionType_strategy)
def test_jpdl32_actiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original
