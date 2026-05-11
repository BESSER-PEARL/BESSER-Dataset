import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    jpdl31::SubProcessType,
    jpdl31::VariableType,
    jpdl31::TransitionType,
    jpdl31::SuperStateType,
    jpdl31::StateType,
    jpdl31::StartStateType,
    jpdl31::TimerType,
    jpdl31::TaskNodeType,
    jpdl31::TaskType,
    jpdl31::SwimlaneType,
    jpdl31::ProcessDefinitionType,
    jpdl31::NodeType,
    jpdl31::ProcessStateType,
    jpdl31::EndStateType,
    jpdl31::JoinType,
    jpdl31::ForkType,
    jpdl31::EStringToStringMapEntry,
    jpdl31::DocumentRoot,
    jpdl31::TransitionType1,
    jpdl31::ExceptionHandlerType,
    jpdl31::EventType,
    jpdl31::Delegation,
    jpdl31::DecisionType,
    jpdl31::ScriptType,
    jpdl31::CreateTimerType,
    jpdl31::ConditionType,
    jpdl31::CancelTimerType,
    Delegation,
    jpdl31::AssignmentType,
    jpdl31::ActionType,
    BooleanType,
    PriorityTypeMember0,
    ConfigTypeType1,
    ConfigTypeType,
    SignalType,
    TypeTypeMember1,
    ConfigType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jpdl31::subprocesstype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::SubProcessType)


def test_jpdl31::subprocesstype_constructor_exists():
    assert callable(jpdl31::SubProcessType.__init__)


def test_jpdl31::subprocesstype_constructor_args():
    sig = inspect.signature(jpdl31::SubProcessType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_jpdl31::subprocesstype_has_name():
    assert hasattr(jpdl31::SubProcessType, "name")
    descriptor = None
    for klass in jpdl31::SubProcessType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::subprocesstype_has_version():
    assert hasattr(jpdl31::SubProcessType, "version")
    descriptor = None
    for klass in jpdl31::SubProcessType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::variabletype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::VariableType)


def test_jpdl31::variabletype_constructor_exists():
    assert callable(jpdl31::VariableType.__init__)


def test_jpdl31::variabletype_constructor_args():
    sig = inspect.signature(jpdl31::VariableType.__init__)
    params = list(sig.parameters.keys())
    assert "mappedName" in params, "Missing parameter 'mappedName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "any" in params, "Missing parameter 'any'"
    assert "access" in params, "Missing parameter 'access'"

def test_jpdl31::variabletype_has_mappedName():
    assert hasattr(jpdl31::VariableType, "mappedName")
    descriptor = None
    for klass in jpdl31::VariableType.__mro__:
        if "mappedName" in klass.__dict__:
            descriptor = klass.__dict__["mappedName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::variabletype_has_name():
    assert hasattr(jpdl31::VariableType, "name")
    descriptor = None
    for klass in jpdl31::VariableType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::variabletype_has_any():
    assert hasattr(jpdl31::VariableType, "any")
    descriptor = None
    for klass in jpdl31::VariableType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::variabletype_has_access():
    assert hasattr(jpdl31::VariableType, "access")
    descriptor = None
    for klass in jpdl31::VariableType.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::transitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::TransitionType)


def test_jpdl31::transitiontype_constructor_exists():
    assert callable(jpdl31::TransitionType.__init__)


def test_jpdl31::transitiontype_constructor_args():
    sig = inspect.signature(jpdl31::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::transitiontype_has_to():
    assert hasattr(jpdl31::TransitionType, "to")
    descriptor = None
    for klass in jpdl31::TransitionType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::transitiontype_has_group():
    assert hasattr(jpdl31::TransitionType, "group")
    descriptor = None
    for klass in jpdl31::TransitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::transitiontype_has_name():
    assert hasattr(jpdl31::TransitionType, "name")
    descriptor = None
    for klass in jpdl31::TransitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::superstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::SuperStateType)


def test_jpdl31::superstatetype_constructor_exists():
    assert callable(jpdl31::SuperStateType.__init__)


def test_jpdl31::superstatetype_constructor_args():
    sig = inspect.signature(jpdl31::SuperStateType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31::superstatetype_has_name():
    assert hasattr(jpdl31::SuperStateType, "name")
    descriptor = None
    for klass in jpdl31::SuperStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::superstatetype_has_async_():
    assert hasattr(jpdl31::SuperStateType, "async_")
    descriptor = None
    for klass in jpdl31::SuperStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::superstatetype_has_group():
    assert hasattr(jpdl31::SuperStateType, "group")
    descriptor = None
    for klass in jpdl31::SuperStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::statetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::StateType)


def test_jpdl31::statetype_constructor_exists():
    assert callable(jpdl31::StateType.__init__)


def test_jpdl31::statetype_constructor_args():
    sig = inspect.signature(jpdl31::StateType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"

def test_jpdl31::statetype_has_name():
    assert hasattr(jpdl31::StateType, "name")
    descriptor = None
    for klass in jpdl31::StateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::statetype_has_async_():
    assert hasattr(jpdl31::StateType, "async_")
    descriptor = None
    for klass in jpdl31::StateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::statetype_has_nodeContentElements():
    assert hasattr(jpdl31::StateType, "nodeContentElements")
    descriptor = None
    for klass in jpdl31::StateType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::startstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::StartStateType)


def test_jpdl31::startstatetype_constructor_exists():
    assert callable(jpdl31::StartStateType.__init__)


def test_jpdl31::startstatetype_constructor_args():
    sig = inspect.signature(jpdl31::StartStateType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::startstatetype_has_group():
    assert hasattr(jpdl31::StartStateType, "group")
    descriptor = None
    for klass in jpdl31::StartStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::startstatetype_has_name():
    assert hasattr(jpdl31::StartStateType, "name")
    descriptor = None
    for klass in jpdl31::StartStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::timertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::TimerType)


def test_jpdl31::timertype_constructor_exists():
    assert callable(jpdl31::TimerType.__init__)


def test_jpdl31::timertype_constructor_args():
    sig = inspect.signature(jpdl31::TimerType.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "transition" in params, "Missing parameter 'transition'"
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::timertype_has_repeat():
    assert hasattr(jpdl31::TimerType, "repeat")
    descriptor = None
    for klass in jpdl31::TimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::timertype_has_transition():
    assert hasattr(jpdl31::TimerType, "transition")
    descriptor = None
    for klass in jpdl31::TimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::timertype_has_duedate():
    assert hasattr(jpdl31::TimerType, "duedate")
    descriptor = None
    for klass in jpdl31::TimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::timertype_has_name():
    assert hasattr(jpdl31::TimerType, "name")
    descriptor = None
    for klass in jpdl31::TimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::tasknodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::TaskNodeType)


def test_jpdl31::tasknodetype_constructor_exists():
    assert callable(jpdl31::TaskNodeType.__init__)


def test_jpdl31::tasknodetype_constructor_args():
    sig = inspect.signature(jpdl31::TaskNodeType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "signal" in params, "Missing parameter 'signal'"
    assert "name" in params, "Missing parameter 'name'"
    assert "endTasks" in params, "Missing parameter 'endTasks'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "createTasks" in params, "Missing parameter 'createTasks'"

def test_jpdl31::tasknodetype_has_group():
    assert hasattr(jpdl31::TaskNodeType, "group")
    descriptor = None
    for klass in jpdl31::TaskNodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasknodetype_has_signal():
    assert hasattr(jpdl31::TaskNodeType, "signal")
    descriptor = None
    for klass in jpdl31::TaskNodeType.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasknodetype_has_name():
    assert hasattr(jpdl31::TaskNodeType, "name")
    descriptor = None
    for klass in jpdl31::TaskNodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasknodetype_has_endTasks():
    assert hasattr(jpdl31::TaskNodeType, "endTasks")
    descriptor = None
    for klass in jpdl31::TaskNodeType.__mro__:
        if "endTasks" in klass.__dict__:
            descriptor = klass.__dict__["endTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasknodetype_has_async_():
    assert hasattr(jpdl31::TaskNodeType, "async_")
    descriptor = None
    for klass in jpdl31::TaskNodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasknodetype_has_createTasks():
    assert hasattr(jpdl31::TaskNodeType, "createTasks")
    descriptor = None
    for klass in jpdl31::TaskNodeType.__mro__:
        if "createTasks" in klass.__dict__:
            descriptor = klass.__dict__["createTasks"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::tasktype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::TaskType)


def test_jpdl31::tasktype_constructor_exists():
    assert callable(jpdl31::TaskType.__init__)


def test_jpdl31::tasktype_constructor_args():
    sig = inspect.signature(jpdl31::TaskType.__init__)
    params = list(sig.parameters.keys())
    assert "signalling" in params, "Missing parameter 'signalling'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "swimlane" in params, "Missing parameter 'swimlane'"
    assert "blocking" in params, "Missing parameter 'blocking'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31::tasktype_has_signalling():
    assert hasattr(jpdl31::TaskType, "signalling")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "signalling" in klass.__dict__:
            descriptor = klass.__dict__["signalling"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_description():
    assert hasattr(jpdl31::TaskType, "description")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_name():
    assert hasattr(jpdl31::TaskType, "name")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_duedate():
    assert hasattr(jpdl31::TaskType, "duedate")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_swimlane():
    assert hasattr(jpdl31::TaskType, "swimlane")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "swimlane" in klass.__dict__:
            descriptor = klass.__dict__["swimlane"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_blocking():
    assert hasattr(jpdl31::TaskType, "blocking")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "blocking" in klass.__dict__:
            descriptor = klass.__dict__["blocking"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_priority():
    assert hasattr(jpdl31::TaskType, "priority")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::tasktype_has_group():
    assert hasattr(jpdl31::TaskType, "group")
    descriptor = None
    for klass in jpdl31::TaskType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::swimlanetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::SwimlaneType)


def test_jpdl31::swimlanetype_constructor_exists():
    assert callable(jpdl31::SwimlaneType.__init__)


def test_jpdl31::swimlanetype_constructor_args():
    sig = inspect.signature(jpdl31::SwimlaneType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::swimlanetype_has_name():
    assert hasattr(jpdl31::SwimlaneType, "name")
    descriptor = None
    for klass in jpdl31::SwimlaneType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ProcessDefinitionType)


def test_jpdl31::processdefinitiontype_constructor_exists():
    assert callable(jpdl31::ProcessDefinitionType.__init__)


def test_jpdl31::processdefinitiontype_constructor_args():
    sig = inspect.signature(jpdl31::ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::processdefinitiontype_has_group():
    assert hasattr(jpdl31::ProcessDefinitionType, "group")
    descriptor = None
    for klass in jpdl31::ProcessDefinitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::processdefinitiontype_has_name():
    assert hasattr(jpdl31::ProcessDefinitionType, "name")
    descriptor = None
    for klass in jpdl31::ProcessDefinitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::nodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::NodeType)


def test_jpdl31::nodetype_constructor_exists():
    assert callable(jpdl31::NodeType.__init__)


def test_jpdl31::nodetype_constructor_args():
    sig = inspect.signature(jpdl31::NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"

def test_jpdl31::nodetype_has_async_():
    assert hasattr(jpdl31::NodeType, "async_")
    descriptor = None
    for klass in jpdl31::NodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::nodetype_has_name():
    assert hasattr(jpdl31::NodeType, "name")
    descriptor = None
    for klass in jpdl31::NodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::nodetype_has_nodeContentElements():
    assert hasattr(jpdl31::NodeType, "nodeContentElements")
    descriptor = None
    for klass in jpdl31::NodeType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::processstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ProcessStateType)


def test_jpdl31::processstatetype_constructor_exists():
    assert callable(jpdl31::ProcessStateType.__init__)


def test_jpdl31::processstatetype_constructor_args():
    sig = inspect.signature(jpdl31::ProcessStateType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31::processstatetype_has_name():
    assert hasattr(jpdl31::ProcessStateType, "name")
    descriptor = None
    for klass in jpdl31::ProcessStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::processstatetype_has_async_():
    assert hasattr(jpdl31::ProcessStateType, "async_")
    descriptor = None
    for klass in jpdl31::ProcessStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::processstatetype_has_group():
    assert hasattr(jpdl31::ProcessStateType, "group")
    descriptor = None
    for klass in jpdl31::ProcessStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::endstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::EndStateType)


def test_jpdl31::endstatetype_constructor_exists():
    assert callable(jpdl31::EndStateType.__init__)


def test_jpdl31::endstatetype_constructor_args():
    sig = inspect.signature(jpdl31::EndStateType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::endstatetype_has_group():
    assert hasattr(jpdl31::EndStateType, "group")
    descriptor = None
    for klass in jpdl31::EndStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::endstatetype_has_name():
    assert hasattr(jpdl31::EndStateType, "name")
    descriptor = None
    for klass in jpdl31::EndStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::jointype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::JoinType)


def test_jpdl31::jointype_constructor_exists():
    assert callable(jpdl31::JoinType.__init__)


def test_jpdl31::jointype_constructor_args():
    sig = inspect.signature(jpdl31::JoinType.__init__)
    params = list(sig.parameters.keys())
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::jointype_has_nodeContentElements():
    assert hasattr(jpdl31::JoinType, "nodeContentElements")
    descriptor = None
    for klass in jpdl31::JoinType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::jointype_has_async_():
    assert hasattr(jpdl31::JoinType, "async_")
    descriptor = None
    for klass in jpdl31::JoinType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::jointype_has_name():
    assert hasattr(jpdl31::JoinType, "name")
    descriptor = None
    for klass in jpdl31::JoinType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::forktype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ForkType)


def test_jpdl31::forktype_constructor_exists():
    assert callable(jpdl31::ForkType.__init__)


def test_jpdl31::forktype_constructor_args():
    sig = inspect.signature(jpdl31::ForkType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31::forktype_has_name():
    assert hasattr(jpdl31::ForkType, "name")
    descriptor = None
    for klass in jpdl31::ForkType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::forktype_has_async_():
    assert hasattr(jpdl31::ForkType, "async_")
    descriptor = None
    for klass in jpdl31::ForkType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::forktype_has_group():
    assert hasattr(jpdl31::ForkType, "group")
    descriptor = None
    for klass in jpdl31::ForkType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(jpdl31::EStringToStringMapEntry)


def test_jpdl31::estringtostringmapentry_constructor_exists():
    assert callable(jpdl31::EStringToStringMapEntry.__init__)


def test_jpdl31::estringtostringmapentry_constructor_args():
    sig = inspect.signature(jpdl31::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpdl31::documentroot_is_not_abstract():
    assert not inspect.isabstract(jpdl31::DocumentRoot)


def test_jpdl31::documentroot_constructor_exists():
    assert callable(jpdl31::DocumentRoot.__init__)


def test_jpdl31::documentroot_constructor_args():
    sig = inspect.signature(jpdl31::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_jpdl31::documentroot_has_mixed():
    assert hasattr(jpdl31::DocumentRoot, "mixed")
    descriptor = None
    for klass in jpdl31::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::transitiontype1_is_not_abstract():
    assert not inspect.isabstract(jpdl31::TransitionType1)


def test_jpdl31::transitiontype1_constructor_exists():
    assert callable(jpdl31::TransitionType1.__init__)


def test_jpdl31::transitiontype1_constructor_args():
    sig = inspect.signature(jpdl31::TransitionType1.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::transitiontype1_has_to():
    assert hasattr(jpdl31::TransitionType1, "to")
    descriptor = None
    for klass in jpdl31::TransitionType1.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::transitiontype1_has_group():
    assert hasattr(jpdl31::TransitionType1, "group")
    descriptor = None
    for klass in jpdl31::TransitionType1.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::transitiontype1_has_name():
    assert hasattr(jpdl31::TransitionType1, "name")
    descriptor = None
    for klass in jpdl31::TransitionType1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::exceptionhandlertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ExceptionHandlerType)


def test_jpdl31::exceptionhandlertype_constructor_exists():
    assert callable(jpdl31::ExceptionHandlerType.__init__)


def test_jpdl31::exceptionhandlertype_constructor_args():
    sig = inspect.signature(jpdl31::ExceptionHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "exceptionClass" in params, "Missing parameter 'exceptionClass'"

def test_jpdl31::exceptionhandlertype_has_group():
    assert hasattr(jpdl31::ExceptionHandlerType, "group")
    descriptor = None
    for klass in jpdl31::ExceptionHandlerType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::exceptionhandlertype_has_exceptionClass():
    assert hasattr(jpdl31::ExceptionHandlerType, "exceptionClass")
    descriptor = None
    for klass in jpdl31::ExceptionHandlerType.__mro__:
        if "exceptionClass" in klass.__dict__:
            descriptor = klass.__dict__["exceptionClass"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::eventtype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::EventType)


def test_jpdl31::eventtype_constructor_exists():
    assert callable(jpdl31::EventType.__init__)


def test_jpdl31::eventtype_constructor_args():
    sig = inspect.signature(jpdl31::EventType.__init__)
    params = list(sig.parameters.keys())
    assert "actionElements" in params, "Missing parameter 'actionElements'"
    assert "type" in params, "Missing parameter 'type'"

def test_jpdl31::eventtype_has_actionElements():
    assert hasattr(jpdl31::EventType, "actionElements")
    descriptor = None
    for klass in jpdl31::EventType.__mro__:
        if "actionElements" in klass.__dict__:
            descriptor = klass.__dict__["actionElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::eventtype_has_type():
    assert hasattr(jpdl31::EventType, "type")
    descriptor = None
    for klass in jpdl31::EventType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::delegation_is_not_abstract():
    assert not inspect.isabstract(jpdl31::Delegation)


def test_jpdl31::delegation_constructor_exists():
    assert callable(jpdl31::Delegation.__init__)


def test_jpdl31::delegation_constructor_args():
    sig = inspect.signature(jpdl31::Delegation.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "configType" in params, "Missing parameter 'configType'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_jpdl31::delegation_has_any():
    assert hasattr(jpdl31::Delegation, "any")
    descriptor = None
    for klass in jpdl31::Delegation.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::delegation_has_configType():
    assert hasattr(jpdl31::Delegation, "configType")
    descriptor = None
    for klass in jpdl31::Delegation.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::delegation_has_class_():
    assert hasattr(jpdl31::Delegation, "class_")
    descriptor = None
    for klass in jpdl31::Delegation.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::delegation_has_mixed():
    assert hasattr(jpdl31::Delegation, "mixed")
    descriptor = None
    for klass in jpdl31::Delegation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::decisiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::DecisionType)


def test_jpdl31::decisiontype_constructor_exists():
    assert callable(jpdl31::DecisionType.__init__)


def test_jpdl31::decisiontype_constructor_args():
    sig = inspect.signature(jpdl31::DecisionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_jpdl31::decisiontype_has_group():
    assert hasattr(jpdl31::DecisionType, "group")
    descriptor = None
    for klass in jpdl31::DecisionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::decisiontype_has_async_():
    assert hasattr(jpdl31::DecisionType, "async_")
    descriptor = None
    for klass in jpdl31::DecisionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::decisiontype_has_name():
    assert hasattr(jpdl31::DecisionType, "name")
    descriptor = None
    for klass in jpdl31::DecisionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::decisiontype_has_expression():
    assert hasattr(jpdl31::DecisionType, "expression")
    descriptor = None
    for klass in jpdl31::DecisionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::scripttype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ScriptType)


def test_jpdl31::scripttype_constructor_exists():
    assert callable(jpdl31::ScriptType.__init__)


def test_jpdl31::scripttype_constructor_args():
    sig = inspect.signature(jpdl31::ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_jpdl31::scripttype_has_any():
    assert hasattr(jpdl31::ScriptType, "any")
    descriptor = None
    for klass in jpdl31::ScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::scripttype_has_name():
    assert hasattr(jpdl31::ScriptType, "name")
    descriptor = None
    for klass in jpdl31::ScriptType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::scripttype_has_acceptPropagatedEvents():
    assert hasattr(jpdl31::ScriptType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl31::ScriptType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::scripttype_has_mixed():
    assert hasattr(jpdl31::ScriptType, "mixed")
    descriptor = None
    for klass in jpdl31::ScriptType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::createtimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::CreateTimerType)


def test_jpdl31::createtimertype_constructor_exists():
    assert callable(jpdl31::CreateTimerType.__init__)


def test_jpdl31::createtimertype_constructor_args():
    sig = inspect.signature(jpdl31::CreateTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "transition" in params, "Missing parameter 'transition'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::createtimertype_has_duedate():
    assert hasattr(jpdl31::CreateTimerType, "duedate")
    descriptor = None
    for klass in jpdl31::CreateTimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::createtimertype_has_repeat():
    assert hasattr(jpdl31::CreateTimerType, "repeat")
    descriptor = None
    for klass in jpdl31::CreateTimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::createtimertype_has_transition():
    assert hasattr(jpdl31::CreateTimerType, "transition")
    descriptor = None
    for klass in jpdl31::CreateTimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::createtimertype_has_name():
    assert hasattr(jpdl31::CreateTimerType, "name")
    descriptor = None
    for klass in jpdl31::CreateTimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::conditiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ConditionType)


def test_jpdl31::conditiontype_constructor_exists():
    assert callable(jpdl31::ConditionType.__init__)


def test_jpdl31::conditiontype_constructor_args():
    sig = inspect.signature(jpdl31::ConditionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl31::conditiontype_has_any():
    assert hasattr(jpdl31::ConditionType, "any")
    descriptor = None
    for klass in jpdl31::ConditionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::conditiontype_has_mixed():
    assert hasattr(jpdl31::ConditionType, "mixed")
    descriptor = None
    for klass in jpdl31::ConditionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::conditiontype_has_expression():
    assert hasattr(jpdl31::ConditionType, "expression")
    descriptor = None
    for klass in jpdl31::ConditionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::conditiontype_has_group():
    assert hasattr(jpdl31::ConditionType, "group")
    descriptor = None
    for klass in jpdl31::ConditionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::canceltimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::CancelTimerType)


def test_jpdl31::canceltimertype_constructor_exists():
    assert callable(jpdl31::CancelTimerType.__init__)


def test_jpdl31::canceltimertype_constructor_args():
    sig = inspect.signature(jpdl31::CancelTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl31::canceltimertype_has_name():
    assert hasattr(jpdl31::CancelTimerType, "name")
    descriptor = None
    for klass in jpdl31::CancelTimerType.__mro__:
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



def test_jpdl31::assignmenttype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::AssignmentType)


def test_jpdl31::assignmenttype_constructor_exists():
    assert callable(jpdl31::AssignmentType.__init__)


def test_jpdl31::assignmenttype_constructor_args():
    sig = inspect.signature(jpdl31::AssignmentType.__init__)
    params = list(sig.parameters.keys())
    assert "pooledActors" in params, "Missing parameter 'pooledActors'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "actorId" in params, "Missing parameter 'actorId'"

def test_jpdl31::assignmenttype_has_pooledActors():
    assert hasattr(jpdl31::AssignmentType, "pooledActors")
    descriptor = None
    for klass in jpdl31::AssignmentType.__mro__:
        if "pooledActors" in klass.__dict__:
            descriptor = klass.__dict__["pooledActors"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::assignmenttype_has_expression():
    assert hasattr(jpdl31::AssignmentType, "expression")
    descriptor = None
    for klass in jpdl31::AssignmentType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::assignmenttype_has_actorId():
    assert hasattr(jpdl31::AssignmentType, "actorId")
    descriptor = None
    for klass in jpdl31::AssignmentType.__mro__:
        if "actorId" in klass.__dict__:
            descriptor = klass.__dict__["actorId"]
            break
    assert isinstance(descriptor, property)



def test_jpdl31::actiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl31::ActionType)


def test_jpdl31::actiontype_constructor_exists():
    assert callable(jpdl31::ActionType.__init__)


def test_jpdl31::actiontype_constructor_args():
    sig = inspect.signature(jpdl31::ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "refName" in params, "Missing parameter 'refName'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "name" in params, "Missing parameter 'name'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "configType" in params, "Missing parameter 'configType'"

def test_jpdl31::actiontype_has_any():
    assert hasattr(jpdl31::ActionType, "any")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_refName():
    assert hasattr(jpdl31::ActionType, "refName")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "refName" in klass.__dict__:
            descriptor = klass.__dict__["refName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_async_():
    assert hasattr(jpdl31::ActionType, "async_")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_expression():
    assert hasattr(jpdl31::ActionType, "expression")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_acceptPropagatedEvents():
    assert hasattr(jpdl31::ActionType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_name():
    assert hasattr(jpdl31::ActionType, "name")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_class_():
    assert hasattr(jpdl31::ActionType, "class_")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_mixed():
    assert hasattr(jpdl31::ActionType, "mixed")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl31::actiontype_has_configType():
    assert hasattr(jpdl31::ActionType, "configType")
    descriptor = None
    for klass in jpdl31::ActionType.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_booleantype_exists():
    # Check that the Enumeration exists
    assert BooleanType is not None

def test_booleantype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanType]
    expected_literals = [
        "off",
        "false",
        "yes",
        "no",
        "true",
        "on",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanType"

def test_prioritytypemember0_exists():
    # Check that the Enumeration exists
    assert PriorityTypeMember0 is not None

def test_prioritytypemember0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityTypeMember0]
    expected_literals = [
        "lowest",
        "low",
        "highest",
        "normal",
        "high",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityTypeMember0"

def test_configtypetype1_exists():
    # Check that the Enumeration exists
    assert ConfigTypeType1 is not None

def test_configtypetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigTypeType1]
    expected_literals = [
        "field",
        "configurationProperty",
        "constructor",
        "bean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigTypeType1"

def test_configtypetype_exists():
    # Check that the Enumeration exists
    assert ConfigTypeType is not None

def test_configtypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigTypeType]
    expected_literals = [
        "constructor",
        "configurationProperty",
        "field",
        "bean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigTypeType"

def test_signaltype_exists():
    # Check that the Enumeration exists
    assert SignalType is not None

def test_signaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalType]
    expected_literals = [
        "firstWait",
        "first",
        "never",
        "last",
        "unsynchronized",
        "lastWait",
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
        "subprocessCreated",
        "nodeEnter",
        "timerCreate",
        "processEnd",
        "subprocessEnd",
        "processStart",
        "afterSignal",
        "taskStart",
        "superstateEnter",
        "superstateLeave",
        "taskEnd",
        "taskCreate",
        "nodeLeave",
        "beforeSignal",
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
        "field",
        "bean",
        "configurationProperty",
        "constructor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigType"


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
jpdl31::SubProcessType_strategy = st.builds(
    jpdl31::SubProcessType,
    name=
        safe_text,
    version=
        safe_text
)
jpdl31::VariableType_strategy = st.builds(
    jpdl31::VariableType,
    mappedName=
        safe_text,
    name=
        safe_text,
    any=
        safe_text,
    access=
        safe_text
)
jpdl31::TransitionType_strategy = st.builds(
    jpdl31::TransitionType,
    to=
        safe_text,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31::SuperStateType_strategy = st.builds(
    jpdl31::SuperStateType,
    name=
        safe_text,
    async_=
        safe_text,
    group=
        safe_text
)
jpdl31::StateType_strategy = st.builds(
    jpdl31::StateType,
    name=
        safe_text,
    async_=
        safe_text,
    nodeContentElements=
        safe_text
)
jpdl31::StartStateType_strategy = st.builds(
    jpdl31::StartStateType,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31::TimerType_strategy = st.builds(
    jpdl31::TimerType,
    repeat=
        safe_text,
    transition=
        safe_text,
    duedate=
        safe_text,
    name=
        safe_text
)
jpdl31::TaskNodeType_strategy = st.builds(
    jpdl31::TaskNodeType,
    group=
        safe_text,
    signal=
        safe_text,
    name=
        safe_text,
    endTasks=
        safe_text,
    async_=
        safe_text,
    createTasks=
        safe_text
)
jpdl31::TaskType_strategy = st.builds(
    jpdl31::TaskType,
    signalling=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    duedate=
        safe_text,
    swimlane=
        safe_text,
    blocking=
        safe_text,
    priority=
        safe_text,
    group=
        safe_text
)
jpdl31::SwimlaneType_strategy = st.builds(
    jpdl31::SwimlaneType,
    name=
        safe_text
)
jpdl31::ProcessDefinitionType_strategy = st.builds(
    jpdl31::ProcessDefinitionType,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31::NodeType_strategy = st.builds(
    jpdl31::NodeType,
    async_=
        safe_text,
    name=
        safe_text,
    nodeContentElements=
        safe_text
)
jpdl31::ProcessStateType_strategy = st.builds(
    jpdl31::ProcessStateType,
    name=
        safe_text,
    async_=
        safe_text,
    group=
        safe_text
)
jpdl31::EndStateType_strategy = st.builds(
    jpdl31::EndStateType,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31::JoinType_strategy = st.builds(
    jpdl31::JoinType,
    nodeContentElements=
        safe_text,
    async_=
        safe_text,
    name=
        safe_text
)
jpdl31::ForkType_strategy = st.builds(
    jpdl31::ForkType,
    name=
        safe_text,
    async_=
        safe_text,
    group=
        safe_text
)
jpdl31::EStringToStringMapEntry_strategy = st.builds(
    jpdl31::EStringToStringMapEntry,
)
jpdl31::DocumentRoot_strategy = st.builds(
    jpdl31::DocumentRoot,
    mixed=
        safe_text
)
jpdl31::TransitionType1_strategy = st.builds(
    jpdl31::TransitionType1,
    to=
        safe_text,
    group=
        safe_text,
    name=
        safe_text
)
jpdl31::ExceptionHandlerType_strategy = st.builds(
    jpdl31::ExceptionHandlerType,
    group=
        safe_text,
    exceptionClass=
        safe_text
)
jpdl31::EventType_strategy = st.builds(
    jpdl31::EventType,
    actionElements=
        safe_text,
    type=
        safe_text
)
jpdl31::Delegation_strategy = st.builds(
    jpdl31::Delegation,
    any=
        safe_text,
    configType=
        safe_text,
    class_=
        safe_text,
    mixed=
        safe_text
)
jpdl31::DecisionType_strategy = st.builds(
    jpdl31::DecisionType,
    group=
        safe_text,
    async_=
        safe_text,
    name=
        safe_text,
    expression=
        safe_text
)
jpdl31::ScriptType_strategy = st.builds(
    jpdl31::ScriptType,
    any=
        safe_text,
    name=
        safe_text,
    acceptPropagatedEvents=
        safe_text,
    mixed=
        safe_text
)
jpdl31::CreateTimerType_strategy = st.builds(
    jpdl31::CreateTimerType,
    duedate=
        safe_text,
    repeat=
        safe_text,
    transition=
        safe_text,
    name=
        safe_text
)
jpdl31::ConditionType_strategy = st.builds(
    jpdl31::ConditionType,
    any=
        safe_text,
    mixed=
        safe_text,
    expression=
        safe_text,
    group=
        safe_text
)
jpdl31::CancelTimerType_strategy = st.builds(
    jpdl31::CancelTimerType,
    name=
        safe_text
)
Delegation_strategy = st.builds(
    Delegation,
)
jpdl31::AssignmentType_strategy = st.builds(
    jpdl31::AssignmentType,
    pooledActors=
        safe_text,
    expression=
        safe_text,
    actorId=
        safe_text
)
jpdl31::ActionType_strategy = st.builds(
    jpdl31::ActionType,
    any=
        safe_text,
    refName=
        safe_text,
    async_=
        safe_text,
    expression=
        safe_text,
    acceptPropagatedEvents=
        safe_text,
    name=
        safe_text,
    class_=
        safe_text,
    mixed=
        safe_text,
    configType=
        safe_text
)

@given(instance=jpdl31::SubProcessType_strategy)
@settings(max_examples=50)
def test_jpdl31::subprocesstype_instantiation(instance):
    assert isinstance(instance, jpdl31::SubProcessType)

@given(instance=jpdl31::SubProcessType_strategy)
def test_jpdl31::subprocesstype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::SubProcessType_strategy)
def test_jpdl31::subprocesstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::SubProcessType_strategy)
def test_jpdl31::subprocesstype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=jpdl31::SubProcessType_strategy)
def test_jpdl31::subprocesstype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=jpdl31::VariableType_strategy)
@settings(max_examples=50)
def test_jpdl31::variabletype_instantiation(instance):
    assert isinstance(instance, jpdl31::VariableType)

@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_mappedName_type(instance):
    assert isinstance(instance.mappedName, str)


@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_mappedName_setter(instance):
    original = instance.mappedName
    instance.mappedName = original
    assert instance.mappedName == original

@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=jpdl31::VariableType_strategy)
def test_jpdl31::variabletype_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=jpdl31::TransitionType_strategy)
@settings(max_examples=50)
def test_jpdl31::transitiontype_instantiation(instance):
    assert isinstance(instance, jpdl31::TransitionType)

@given(instance=jpdl31::TransitionType_strategy)
def test_jpdl31::transitiontype_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jpdl31::TransitionType_strategy)
def test_jpdl31::transitiontype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl31::TransitionType_strategy)
def test_jpdl31::transitiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::TransitionType_strategy)
def test_jpdl31::transitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::TransitionType_strategy)
def test_jpdl31::transitiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::TransitionType_strategy)
def test_jpdl31::transitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::SuperStateType_strategy)
@settings(max_examples=50)
def test_jpdl31::superstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31::SuperStateType)

@given(instance=jpdl31::SuperStateType_strategy)
def test_jpdl31::superstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::SuperStateType_strategy)
def test_jpdl31::superstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::SuperStateType_strategy)
def test_jpdl31::superstatetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::SuperStateType_strategy)
def test_jpdl31::superstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::SuperStateType_strategy)
def test_jpdl31::superstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::SuperStateType_strategy)
def test_jpdl31::superstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::StateType_strategy)
@settings(max_examples=50)
def test_jpdl31::statetype_instantiation(instance):
    assert isinstance(instance, jpdl31::StateType)

@given(instance=jpdl31::StateType_strategy)
def test_jpdl31::statetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::StateType_strategy)
def test_jpdl31::statetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::StateType_strategy)
def test_jpdl31::statetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::StateType_strategy)
def test_jpdl31::statetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::StateType_strategy)
def test_jpdl31::statetype_nodeContentElements_type(instance):
    assert isinstance(instance.nodeContentElements, str)


@given(instance=jpdl31::StateType_strategy)
def test_jpdl31::statetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl31::StartStateType_strategy)
@settings(max_examples=50)
def test_jpdl31::startstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31::StartStateType)

@given(instance=jpdl31::StartStateType_strategy)
def test_jpdl31::startstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::StartStateType_strategy)
def test_jpdl31::startstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::StartStateType_strategy)
def test_jpdl31::startstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::StartStateType_strategy)
def test_jpdl31::startstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::TimerType_strategy)
@settings(max_examples=50)
def test_jpdl31::timertype_instantiation(instance):
    assert isinstance(instance, jpdl31::TimerType)

@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_repeat_type(instance):
    assert isinstance(instance.repeat, str)


@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_transition_type(instance):
    assert isinstance(instance.transition, str)


@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::TimerType_strategy)
def test_jpdl31::timertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::TaskNodeType_strategy)
@settings(max_examples=50)
def test_jpdl31::tasknodetype_instantiation(instance):
    assert isinstance(instance, jpdl31::TaskNodeType)

@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_endTasks_type(instance):
    assert isinstance(instance.endTasks, str)


@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_endTasks_setter(instance):
    original = instance.endTasks
    instance.endTasks = original
    assert instance.endTasks == original

@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_createTasks_type(instance):
    assert isinstance(instance.createTasks, str)


@given(instance=jpdl31::TaskNodeType_strategy)
def test_jpdl31::tasknodetype_createTasks_setter(instance):
    original = instance.createTasks
    instance.createTasks = original
    assert instance.createTasks == original

@given(instance=jpdl31::TaskType_strategy)
@settings(max_examples=50)
def test_jpdl31::tasktype_instantiation(instance):
    assert isinstance(instance, jpdl31::TaskType)

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_signalling_type(instance):
    assert isinstance(instance.signalling, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_signalling_setter(instance):
    original = instance.signalling
    instance.signalling = original
    assert instance.signalling == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_swimlane_type(instance):
    assert isinstance(instance.swimlane, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_swimlane_setter(instance):
    original = instance.swimlane
    instance.swimlane = original
    assert instance.swimlane == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_blocking_type(instance):
    assert isinstance(instance.blocking, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_blocking_setter(instance):
    original = instance.blocking
    instance.blocking = original
    assert instance.blocking == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::TaskType_strategy)
def test_jpdl31::tasktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::SwimlaneType_strategy)
@settings(max_examples=50)
def test_jpdl31::swimlanetype_instantiation(instance):
    assert isinstance(instance, jpdl31::SwimlaneType)

@given(instance=jpdl31::SwimlaneType_strategy)
def test_jpdl31::swimlanetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::SwimlaneType_strategy)
def test_jpdl31::swimlanetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ProcessDefinitionType_strategy)
@settings(max_examples=50)
def test_jpdl31::processdefinitiontype_instantiation(instance):
    assert isinstance(instance, jpdl31::ProcessDefinitionType)

@given(instance=jpdl31::ProcessDefinitionType_strategy)
def test_jpdl31::processdefinitiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::ProcessDefinitionType_strategy)
def test_jpdl31::processdefinitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::ProcessDefinitionType_strategy)
def test_jpdl31::processdefinitiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::ProcessDefinitionType_strategy)
def test_jpdl31::processdefinitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::NodeType_strategy)
@settings(max_examples=50)
def test_jpdl31::nodetype_instantiation(instance):
    assert isinstance(instance, jpdl31::NodeType)

@given(instance=jpdl31::NodeType_strategy)
def test_jpdl31::nodetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::NodeType_strategy)
def test_jpdl31::nodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::NodeType_strategy)
def test_jpdl31::nodetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::NodeType_strategy)
def test_jpdl31::nodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::NodeType_strategy)
def test_jpdl31::nodetype_nodeContentElements_type(instance):
    assert isinstance(instance.nodeContentElements, str)


@given(instance=jpdl31::NodeType_strategy)
def test_jpdl31::nodetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl31::ProcessStateType_strategy)
@settings(max_examples=50)
def test_jpdl31::processstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31::ProcessStateType)

@given(instance=jpdl31::ProcessStateType_strategy)
def test_jpdl31::processstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::ProcessStateType_strategy)
def test_jpdl31::processstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ProcessStateType_strategy)
def test_jpdl31::processstatetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::ProcessStateType_strategy)
def test_jpdl31::processstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::ProcessStateType_strategy)
def test_jpdl31::processstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::ProcessStateType_strategy)
def test_jpdl31::processstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::EndStateType_strategy)
@settings(max_examples=50)
def test_jpdl31::endstatetype_instantiation(instance):
    assert isinstance(instance, jpdl31::EndStateType)

@given(instance=jpdl31::EndStateType_strategy)
def test_jpdl31::endstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::EndStateType_strategy)
def test_jpdl31::endstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::EndStateType_strategy)
def test_jpdl31::endstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::EndStateType_strategy)
def test_jpdl31::endstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::JoinType_strategy)
@settings(max_examples=50)
def test_jpdl31::jointype_instantiation(instance):
    assert isinstance(instance, jpdl31::JoinType)

@given(instance=jpdl31::JoinType_strategy)
def test_jpdl31::jointype_nodeContentElements_type(instance):
    assert isinstance(instance.nodeContentElements, str)


@given(instance=jpdl31::JoinType_strategy)
def test_jpdl31::jointype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl31::JoinType_strategy)
def test_jpdl31::jointype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::JoinType_strategy)
def test_jpdl31::jointype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::JoinType_strategy)
def test_jpdl31::jointype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::JoinType_strategy)
def test_jpdl31::jointype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ForkType_strategy)
@settings(max_examples=50)
def test_jpdl31::forktype_instantiation(instance):
    assert isinstance(instance, jpdl31::ForkType)

@given(instance=jpdl31::ForkType_strategy)
def test_jpdl31::forktype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::ForkType_strategy)
def test_jpdl31::forktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ForkType_strategy)
def test_jpdl31::forktype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::ForkType_strategy)
def test_jpdl31::forktype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::ForkType_strategy)
def test_jpdl31::forktype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::ForkType_strategy)
def test_jpdl31::forktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_jpdl31::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, jpdl31::EStringToStringMapEntry)

@given(instance=jpdl31::DocumentRoot_strategy)
@settings(max_examples=50)
def test_jpdl31::documentroot_instantiation(instance):
    assert isinstance(instance, jpdl31::DocumentRoot)

@given(instance=jpdl31::DocumentRoot_strategy)
def test_jpdl31::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl31::DocumentRoot_strategy)
def test_jpdl31::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl31::TransitionType1_strategy)
@settings(max_examples=50)
def test_jpdl31::transitiontype1_instantiation(instance):
    assert isinstance(instance, jpdl31::TransitionType1)

@given(instance=jpdl31::TransitionType1_strategy)
def test_jpdl31::transitiontype1_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jpdl31::TransitionType1_strategy)
def test_jpdl31::transitiontype1_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl31::TransitionType1_strategy)
def test_jpdl31::transitiontype1_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::TransitionType1_strategy)
def test_jpdl31::transitiontype1_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::TransitionType1_strategy)
def test_jpdl31::transitiontype1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::TransitionType1_strategy)
def test_jpdl31::transitiontype1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ExceptionHandlerType_strategy)
@settings(max_examples=50)
def test_jpdl31::exceptionhandlertype_instantiation(instance):
    assert isinstance(instance, jpdl31::ExceptionHandlerType)

@given(instance=jpdl31::ExceptionHandlerType_strategy)
def test_jpdl31::exceptionhandlertype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::ExceptionHandlerType_strategy)
def test_jpdl31::exceptionhandlertype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::ExceptionHandlerType_strategy)
def test_jpdl31::exceptionhandlertype_exceptionClass_type(instance):
    assert isinstance(instance.exceptionClass, str)


@given(instance=jpdl31::ExceptionHandlerType_strategy)
def test_jpdl31::exceptionhandlertype_exceptionClass_setter(instance):
    original = instance.exceptionClass
    instance.exceptionClass = original
    assert instance.exceptionClass == original

@given(instance=jpdl31::EventType_strategy)
@settings(max_examples=50)
def test_jpdl31::eventtype_instantiation(instance):
    assert isinstance(instance, jpdl31::EventType)

@given(instance=jpdl31::EventType_strategy)
def test_jpdl31::eventtype_actionElements_type(instance):
    assert isinstance(instance.actionElements, str)


@given(instance=jpdl31::EventType_strategy)
def test_jpdl31::eventtype_actionElements_setter(instance):
    original = instance.actionElements
    instance.actionElements = original
    assert instance.actionElements == original

@given(instance=jpdl31::EventType_strategy)
def test_jpdl31::eventtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jpdl31::EventType_strategy)
def test_jpdl31::eventtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jpdl31::Delegation_strategy)
@settings(max_examples=50)
def test_jpdl31::delegation_instantiation(instance):
    assert isinstance(instance, jpdl31::Delegation)

@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_configType_type(instance):
    assert isinstance(instance.configType, str)


@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original

@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl31::Delegation_strategy)
def test_jpdl31::delegation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl31::DecisionType_strategy)
@settings(max_examples=50)
def test_jpdl31::decisiontype_instantiation(instance):
    assert isinstance(instance, jpdl31::DecisionType)

@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl31::DecisionType_strategy)
def test_jpdl31::decisiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31::ScriptType_strategy)
@settings(max_examples=50)
def test_jpdl31::scripttype_instantiation(instance):
    assert isinstance(instance, jpdl31::ScriptType)

@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_acceptPropagatedEvents_type(instance):
    assert isinstance(instance.acceptPropagatedEvents, str)


@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original

@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl31::ScriptType_strategy)
def test_jpdl31::scripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl31::CreateTimerType_strategy)
@settings(max_examples=50)
def test_jpdl31::createtimertype_instantiation(instance):
    assert isinstance(instance, jpdl31::CreateTimerType)

@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_repeat_type(instance):
    assert isinstance(instance.repeat, str)


@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_transition_type(instance):
    assert isinstance(instance.transition, str)


@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::CreateTimerType_strategy)
def test_jpdl31::createtimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ConditionType_strategy)
@settings(max_examples=50)
def test_jpdl31::conditiontype_instantiation(instance):
    assert isinstance(instance, jpdl31::ConditionType)

@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl31::ConditionType_strategy)
def test_jpdl31::conditiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl31::CancelTimerType_strategy)
@settings(max_examples=50)
def test_jpdl31::canceltimertype_instantiation(instance):
    assert isinstance(instance, jpdl31::CancelTimerType)

@given(instance=jpdl31::CancelTimerType_strategy)
def test_jpdl31::canceltimertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::CancelTimerType_strategy)
def test_jpdl31::canceltimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Delegation_strategy)
@settings(max_examples=50)
def test_delegation_instantiation(instance):
    assert isinstance(instance, Delegation)

@given(instance=jpdl31::AssignmentType_strategy)
@settings(max_examples=50)
def test_jpdl31::assignmenttype_instantiation(instance):
    assert isinstance(instance, jpdl31::AssignmentType)

@given(instance=jpdl31::AssignmentType_strategy)
def test_jpdl31::assignmenttype_pooledActors_type(instance):
    assert isinstance(instance.pooledActors, str)


@given(instance=jpdl31::AssignmentType_strategy)
def test_jpdl31::assignmenttype_pooledActors_setter(instance):
    original = instance.pooledActors
    instance.pooledActors = original
    assert instance.pooledActors == original

@given(instance=jpdl31::AssignmentType_strategy)
def test_jpdl31::assignmenttype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl31::AssignmentType_strategy)
def test_jpdl31::assignmenttype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31::AssignmentType_strategy)
def test_jpdl31::assignmenttype_actorId_type(instance):
    assert isinstance(instance.actorId, str)


@given(instance=jpdl31::AssignmentType_strategy)
def test_jpdl31::assignmenttype_actorId_setter(instance):
    original = instance.actorId
    instance.actorId = original
    assert instance.actorId == original

@given(instance=jpdl31::ActionType_strategy)
@settings(max_examples=50)
def test_jpdl31::actiontype_instantiation(instance):
    assert isinstance(instance, jpdl31::ActionType)

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_refName_type(instance):
    assert isinstance(instance.refName, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_refName_setter(instance):
    original = instance.refName
    instance.refName = original
    assert instance.refName == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_acceptPropagatedEvents_type(instance):
    assert isinstance(instance.acceptPropagatedEvents, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_configType_type(instance):
    assert isinstance(instance.configType, str)


@given(instance=jpdl31::ActionType_strategy)
def test_jpdl31::actiontype_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original
