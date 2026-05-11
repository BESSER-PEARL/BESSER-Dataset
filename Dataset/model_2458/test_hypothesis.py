import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    jpdl32::SubProcessType,
    jpdl32::ReminderType,
    jpdl32::TimerType,
    jpdl32::TaskNodeType,
    jpdl32::VariableType,
    jpdl32::SwimlaneType,
    jpdl32::SuperStateType,
    jpdl32::StateType,
    jpdl32::StartStateType,
    jpdl32::ProcessStateType,
    jpdl32::ProcessDefinitionType,
    jpdl32::TaskType,
    jpdl32::MailNodeType,
    jpdl32::MailType,
    jpdl32::JoinType,
    jpdl32::ForkType,
    jpdl32::EndStateType,
    jpdl32::NodeType,
    jpdl32::EStringToStringMapEntry,
    jpdl32::DocumentRoot,
    jpdl32::TransitionType,
    jpdl32::ExceptionHandlerType,
    jpdl32::EventType,
    jpdl32::Delegation,
    jpdl32::DecisionType,
    jpdl32::CreateTimerType,
    jpdl32::ScriptType,
    Delegation,
    jpdl32::AssignmentType,
    jpdl32::ConditionType,
    jpdl32::CancelTimerType,
    jpdl32::ActionType,
    ConfigType,
    PriorityTypeMember0,
    SignalType,
    BooleanType,
    TypeTypeMember1,
    BindingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jpdl32::subprocesstype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::SubProcessType)


def test_jpdl32::subprocesstype_constructor_exists():
    assert callable(jpdl32::SubProcessType.__init__)


def test_jpdl32::subprocesstype_constructor_args():
    sig = inspect.signature(jpdl32::SubProcessType.__init__)
    params = list(sig.parameters.keys())
    assert "binding" in params, "Missing parameter 'binding'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_jpdl32::subprocesstype_has_binding():
    assert hasattr(jpdl32::SubProcessType, "binding")
    descriptor = None
    for klass in jpdl32::SubProcessType.__mro__:
        if "binding" in klass.__dict__:
            descriptor = klass.__dict__["binding"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::subprocesstype_has_name():
    assert hasattr(jpdl32::SubProcessType, "name")
    descriptor = None
    for klass in jpdl32::SubProcessType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::subprocesstype_has_version():
    assert hasattr(jpdl32::SubProcessType, "version")
    descriptor = None
    for klass in jpdl32::SubProcessType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::remindertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ReminderType)


def test_jpdl32::remindertype_constructor_exists():
    assert callable(jpdl32::ReminderType.__init__)


def test_jpdl32::remindertype_constructor_args():
    sig = inspect.signature(jpdl32::ReminderType.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "duedate" in params, "Missing parameter 'duedate'"

def test_jpdl32::remindertype_has_repeat():
    assert hasattr(jpdl32::ReminderType, "repeat")
    descriptor = None
    for klass in jpdl32::ReminderType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::remindertype_has_duedate():
    assert hasattr(jpdl32::ReminderType, "duedate")
    descriptor = None
    for klass in jpdl32::ReminderType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::timertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::TimerType)


def test_jpdl32::timertype_constructor_exists():
    assert callable(jpdl32::TimerType.__init__)


def test_jpdl32::timertype_constructor_args():
    sig = inspect.signature(jpdl32::TimerType.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "transition" in params, "Missing parameter 'transition'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::timertype_has_repeat():
    assert hasattr(jpdl32::TimerType, "repeat")
    descriptor = None
    for klass in jpdl32::TimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::timertype_has_duedate():
    assert hasattr(jpdl32::TimerType, "duedate")
    descriptor = None
    for klass in jpdl32::TimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::timertype_has_transition():
    assert hasattr(jpdl32::TimerType, "transition")
    descriptor = None
    for klass in jpdl32::TimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::timertype_has_name():
    assert hasattr(jpdl32::TimerType, "name")
    descriptor = None
    for klass in jpdl32::TimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::tasknodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::TaskNodeType)


def test_jpdl32::tasknodetype_constructor_exists():
    assert callable(jpdl32::TaskNodeType.__init__)


def test_jpdl32::tasknodetype_constructor_args():
    sig = inspect.signature(jpdl32::TaskNodeType.__init__)
    params = list(sig.parameters.keys())
    assert "createTasks" in params, "Missing parameter 'createTasks'"
    assert "name" in params, "Missing parameter 'name'"
    assert "signal" in params, "Missing parameter 'signal'"
    assert "group" in params, "Missing parameter 'group'"
    assert "endTasks" in params, "Missing parameter 'endTasks'"
    assert "description" in params, "Missing parameter 'description'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32::tasknodetype_has_createTasks():
    assert hasattr(jpdl32::TaskNodeType, "createTasks")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "createTasks" in klass.__dict__:
            descriptor = klass.__dict__["createTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasknodetype_has_name():
    assert hasattr(jpdl32::TaskNodeType, "name")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasknodetype_has_signal():
    assert hasattr(jpdl32::TaskNodeType, "signal")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasknodetype_has_group():
    assert hasattr(jpdl32::TaskNodeType, "group")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasknodetype_has_endTasks():
    assert hasattr(jpdl32::TaskNodeType, "endTasks")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "endTasks" in klass.__dict__:
            descriptor = klass.__dict__["endTasks"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasknodetype_has_description():
    assert hasattr(jpdl32::TaskNodeType, "description")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasknodetype_has_async_():
    assert hasattr(jpdl32::TaskNodeType, "async_")
    descriptor = None
    for klass in jpdl32::TaskNodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::variabletype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::VariableType)


def test_jpdl32::variabletype_constructor_exists():
    assert callable(jpdl32::VariableType.__init__)


def test_jpdl32::variabletype_constructor_args():
    sig = inspect.signature(jpdl32::VariableType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mappedName" in params, "Missing parameter 'mappedName'"
    assert "access" in params, "Missing parameter 'access'"

def test_jpdl32::variabletype_has_name():
    assert hasattr(jpdl32::VariableType, "name")
    descriptor = None
    for klass in jpdl32::VariableType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::variabletype_has_any():
    assert hasattr(jpdl32::VariableType, "any")
    descriptor = None
    for klass in jpdl32::VariableType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::variabletype_has_mappedName():
    assert hasattr(jpdl32::VariableType, "mappedName")
    descriptor = None
    for klass in jpdl32::VariableType.__mro__:
        if "mappedName" in klass.__dict__:
            descriptor = klass.__dict__["mappedName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::variabletype_has_access():
    assert hasattr(jpdl32::VariableType, "access")
    descriptor = None
    for klass in jpdl32::VariableType.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::swimlanetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::SwimlaneType)


def test_jpdl32::swimlanetype_constructor_exists():
    assert callable(jpdl32::SwimlaneType.__init__)


def test_jpdl32::swimlanetype_constructor_args():
    sig = inspect.signature(jpdl32::SwimlaneType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::swimlanetype_has_name():
    assert hasattr(jpdl32::SwimlaneType, "name")
    descriptor = None
    for klass in jpdl32::SwimlaneType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::superstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::SuperStateType)


def test_jpdl32::superstatetype_constructor_exists():
    assert callable(jpdl32::SuperStateType.__init__)


def test_jpdl32::superstatetype_constructor_args():
    sig = inspect.signature(jpdl32::SuperStateType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::superstatetype_has_description():
    assert hasattr(jpdl32::SuperStateType, "description")
    descriptor = None
    for klass in jpdl32::SuperStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::superstatetype_has_async_():
    assert hasattr(jpdl32::SuperStateType, "async_")
    descriptor = None
    for klass in jpdl32::SuperStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::superstatetype_has_group():
    assert hasattr(jpdl32::SuperStateType, "group")
    descriptor = None
    for klass in jpdl32::SuperStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::superstatetype_has_name():
    assert hasattr(jpdl32::SuperStateType, "name")
    descriptor = None
    for klass in jpdl32::SuperStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::statetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::StateType)


def test_jpdl32::statetype_constructor_exists():
    assert callable(jpdl32::StateType.__init__)


def test_jpdl32::statetype_constructor_args():
    sig = inspect.signature(jpdl32::StateType.__init__)
    params = list(sig.parameters.keys())
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::statetype_has_nodeContentElements():
    assert hasattr(jpdl32::StateType, "nodeContentElements")
    descriptor = None
    for klass in jpdl32::StateType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::statetype_has_async_():
    assert hasattr(jpdl32::StateType, "async_")
    descriptor = None
    for klass in jpdl32::StateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::statetype_has_description():
    assert hasattr(jpdl32::StateType, "description")
    descriptor = None
    for klass in jpdl32::StateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::statetype_has_name():
    assert hasattr(jpdl32::StateType, "name")
    descriptor = None
    for klass in jpdl32::StateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::startstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::StartStateType)


def test_jpdl32::startstatetype_constructor_exists():
    assert callable(jpdl32::StartStateType.__init__)


def test_jpdl32::startstatetype_constructor_args():
    sig = inspect.signature(jpdl32::StartStateType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl32::startstatetype_has_name():
    assert hasattr(jpdl32::StartStateType, "name")
    descriptor = None
    for klass in jpdl32::StartStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::startstatetype_has_description():
    assert hasattr(jpdl32::StartStateType, "description")
    descriptor = None
    for klass in jpdl32::StartStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::startstatetype_has_group():
    assert hasattr(jpdl32::StartStateType, "group")
    descriptor = None
    for klass in jpdl32::StartStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::processstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ProcessStateType)


def test_jpdl32::processstatetype_constructor_exists():
    assert callable(jpdl32::ProcessStateType.__init__)


def test_jpdl32::processstatetype_constructor_args():
    sig = inspect.signature(jpdl32::ProcessStateType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "description" in params, "Missing parameter 'description'"
    assert "group" in params, "Missing parameter 'group'"
    assert "binding" in params, "Missing parameter 'binding'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::processstatetype_has_async_():
    assert hasattr(jpdl32::ProcessStateType, "async_")
    descriptor = None
    for klass in jpdl32::ProcessStateType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::processstatetype_has_description():
    assert hasattr(jpdl32::ProcessStateType, "description")
    descriptor = None
    for klass in jpdl32::ProcessStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::processstatetype_has_group():
    assert hasattr(jpdl32::ProcessStateType, "group")
    descriptor = None
    for klass in jpdl32::ProcessStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::processstatetype_has_binding():
    assert hasattr(jpdl32::ProcessStateType, "binding")
    descriptor = None
    for klass in jpdl32::ProcessStateType.__mro__:
        if "binding" in klass.__dict__:
            descriptor = klass.__dict__["binding"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::processstatetype_has_name():
    assert hasattr(jpdl32::ProcessStateType, "name")
    descriptor = None
    for klass in jpdl32::ProcessStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ProcessDefinitionType)


def test_jpdl32::processdefinitiontype_constructor_exists():
    assert callable(jpdl32::ProcessDefinitionType.__init__)


def test_jpdl32::processdefinitiontype_constructor_args():
    sig = inspect.signature(jpdl32::ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::processdefinitiontype_has_description():
    assert hasattr(jpdl32::ProcessDefinitionType, "description")
    descriptor = None
    for klass in jpdl32::ProcessDefinitionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::processdefinitiontype_has_group():
    assert hasattr(jpdl32::ProcessDefinitionType, "group")
    descriptor = None
    for klass in jpdl32::ProcessDefinitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::processdefinitiontype_has_name():
    assert hasattr(jpdl32::ProcessDefinitionType, "name")
    descriptor = None
    for klass in jpdl32::ProcessDefinitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::tasktype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::TaskType)


def test_jpdl32::tasktype_constructor_exists():
    assert callable(jpdl32::TaskType.__init__)


def test_jpdl32::tasktype_constructor_args():
    sig = inspect.signature(jpdl32::TaskType.__init__)
    params = list(sig.parameters.keys())
    assert "signalling" in params, "Missing parameter 'signalling'"
    assert "swimlane" in params, "Missing parameter 'swimlane'"
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "group" in params, "Missing parameter 'group'"
    assert "description" in params, "Missing parameter 'description'"
    assert "blocking" in params, "Missing parameter 'blocking'"
    assert "name" in params, "Missing parameter 'name'"
    assert "notify" in params, "Missing parameter 'notify'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "description1" in params, "Missing parameter 'description1'"

def test_jpdl32::tasktype_has_signalling():
    assert hasattr(jpdl32::TaskType, "signalling")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "signalling" in klass.__dict__:
            descriptor = klass.__dict__["signalling"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_swimlane():
    assert hasattr(jpdl32::TaskType, "swimlane")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "swimlane" in klass.__dict__:
            descriptor = klass.__dict__["swimlane"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_duedate():
    assert hasattr(jpdl32::TaskType, "duedate")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_group():
    assert hasattr(jpdl32::TaskType, "group")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_description():
    assert hasattr(jpdl32::TaskType, "description")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_blocking():
    assert hasattr(jpdl32::TaskType, "blocking")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "blocking" in klass.__dict__:
            descriptor = klass.__dict__["blocking"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_name():
    assert hasattr(jpdl32::TaskType, "name")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_notify():
    assert hasattr(jpdl32::TaskType, "notify")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "notify" in klass.__dict__:
            descriptor = klass.__dict__["notify"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_priority():
    assert hasattr(jpdl32::TaskType, "priority")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::tasktype_has_description1():
    assert hasattr(jpdl32::TaskType, "description1")
    descriptor = None
    for klass in jpdl32::TaskType.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::mailnodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::MailNodeType)


def test_jpdl32::mailnodetype_constructor_exists():
    assert callable(jpdl32::MailNodeType.__init__)


def test_jpdl32::mailnodetype_constructor_args():
    sig = inspect.signature(jpdl32::MailNodeType.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "description" in params, "Missing parameter 'description'"
    assert "text1" in params, "Missing parameter 'text1'"
    assert "template" in params, "Missing parameter 'template'"
    assert "name" in params, "Missing parameter 'name'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "actors" in params, "Missing parameter 'actors'"
    assert "subject1" in params, "Missing parameter 'subject1'"
    assert "text" in params, "Missing parameter 'text'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl32::mailnodetype_has_to():
    assert hasattr(jpdl32::MailNodeType, "to")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_subject():
    assert hasattr(jpdl32::MailNodeType, "subject")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_description():
    assert hasattr(jpdl32::MailNodeType, "description")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_text1():
    assert hasattr(jpdl32::MailNodeType, "text1")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "text1" in klass.__dict__:
            descriptor = klass.__dict__["text1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_template():
    assert hasattr(jpdl32::MailNodeType, "template")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_name():
    assert hasattr(jpdl32::MailNodeType, "name")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_async_():
    assert hasattr(jpdl32::MailNodeType, "async_")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_actors():
    assert hasattr(jpdl32::MailNodeType, "actors")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_subject1():
    assert hasattr(jpdl32::MailNodeType, "subject1")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "subject1" in klass.__dict__:
            descriptor = klass.__dict__["subject1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_text():
    assert hasattr(jpdl32::MailNodeType, "text")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailnodetype_has_group():
    assert hasattr(jpdl32::MailNodeType, "group")
    descriptor = None
    for klass in jpdl32::MailNodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::mailtype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::MailType)


def test_jpdl32::mailtype_constructor_exists():
    assert callable(jpdl32::MailType.__init__)


def test_jpdl32::mailtype_constructor_args():
    sig = inspect.signature(jpdl32::MailType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "text1" in params, "Missing parameter 'text1'"
    assert "name" in params, "Missing parameter 'name'"
    assert "actors" in params, "Missing parameter 'actors'"
    assert "subject1" in params, "Missing parameter 'subject1'"
    assert "template" in params, "Missing parameter 'template'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "group" in params, "Missing parameter 'group'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "to" in params, "Missing parameter 'to'"

def test_jpdl32::mailtype_has_text():
    assert hasattr(jpdl32::MailType, "text")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_text1():
    assert hasattr(jpdl32::MailType, "text1")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "text1" in klass.__dict__:
            descriptor = klass.__dict__["text1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_name():
    assert hasattr(jpdl32::MailType, "name")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_actors():
    assert hasattr(jpdl32::MailType, "actors")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_subject1():
    assert hasattr(jpdl32::MailType, "subject1")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "subject1" in klass.__dict__:
            descriptor = klass.__dict__["subject1"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_template():
    assert hasattr(jpdl32::MailType, "template")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_async_():
    assert hasattr(jpdl32::MailType, "async_")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_group():
    assert hasattr(jpdl32::MailType, "group")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_subject():
    assert hasattr(jpdl32::MailType, "subject")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::mailtype_has_to():
    assert hasattr(jpdl32::MailType, "to")
    descriptor = None
    for klass in jpdl32::MailType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::jointype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::JoinType)


def test_jpdl32::jointype_constructor_exists():
    assert callable(jpdl32::JoinType.__init__)


def test_jpdl32::jointype_constructor_args():
    sig = inspect.signature(jpdl32::JoinType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "description" in params, "Missing parameter 'description'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32::jointype_has_name():
    assert hasattr(jpdl32::JoinType, "name")
    descriptor = None
    for klass in jpdl32::JoinType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::jointype_has_nodeContentElements():
    assert hasattr(jpdl32::JoinType, "nodeContentElements")
    descriptor = None
    for klass in jpdl32::JoinType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::jointype_has_description():
    assert hasattr(jpdl32::JoinType, "description")
    descriptor = None
    for klass in jpdl32::JoinType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::jointype_has_async_():
    assert hasattr(jpdl32::JoinType, "async_")
    descriptor = None
    for klass in jpdl32::JoinType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::forktype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ForkType)


def test_jpdl32::forktype_constructor_exists():
    assert callable(jpdl32::ForkType.__init__)


def test_jpdl32::forktype_constructor_args():
    sig = inspect.signature(jpdl32::ForkType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "description" in params, "Missing parameter 'description'"
    assert "async_" in params, "Missing parameter 'async_'"

def test_jpdl32::forktype_has_name():
    assert hasattr(jpdl32::ForkType, "name")
    descriptor = None
    for klass in jpdl32::ForkType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::forktype_has_group():
    assert hasattr(jpdl32::ForkType, "group")
    descriptor = None
    for klass in jpdl32::ForkType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::forktype_has_description():
    assert hasattr(jpdl32::ForkType, "description")
    descriptor = None
    for klass in jpdl32::ForkType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::forktype_has_async_():
    assert hasattr(jpdl32::ForkType, "async_")
    descriptor = None
    for klass in jpdl32::ForkType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::endstatetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::EndStateType)


def test_jpdl32::endstatetype_constructor_exists():
    assert callable(jpdl32::EndStateType.__init__)


def test_jpdl32::endstatetype_constructor_args():
    sig = inspect.signature(jpdl32::EndStateType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "endCompleteProcess" in params, "Missing parameter 'endCompleteProcess'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_jpdl32::endstatetype_has_group():
    assert hasattr(jpdl32::EndStateType, "group")
    descriptor = None
    for klass in jpdl32::EndStateType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::endstatetype_has_endCompleteProcess():
    assert hasattr(jpdl32::EndStateType, "endCompleteProcess")
    descriptor = None
    for klass in jpdl32::EndStateType.__mro__:
        if "endCompleteProcess" in klass.__dict__:
            descriptor = klass.__dict__["endCompleteProcess"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::endstatetype_has_name():
    assert hasattr(jpdl32::EndStateType, "name")
    descriptor = None
    for klass in jpdl32::EndStateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::endstatetype_has_description():
    assert hasattr(jpdl32::EndStateType, "description")
    descriptor = None
    for klass in jpdl32::EndStateType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::nodetype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::NodeType)


def test_jpdl32::nodetype_constructor_exists():
    assert callable(jpdl32::NodeType.__init__)


def test_jpdl32::nodetype_constructor_args():
    sig = inspect.signature(jpdl32::NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "nodeContentElements" in params, "Missing parameter 'nodeContentElements'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_jpdl32::nodetype_has_async_():
    assert hasattr(jpdl32::NodeType, "async_")
    descriptor = None
    for klass in jpdl32::NodeType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::nodetype_has_nodeContentElements():
    assert hasattr(jpdl32::NodeType, "nodeContentElements")
    descriptor = None
    for klass in jpdl32::NodeType.__mro__:
        if "nodeContentElements" in klass.__dict__:
            descriptor = klass.__dict__["nodeContentElements"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::nodetype_has_name():
    assert hasattr(jpdl32::NodeType, "name")
    descriptor = None
    for klass in jpdl32::NodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::nodetype_has_description():
    assert hasattr(jpdl32::NodeType, "description")
    descriptor = None
    for klass in jpdl32::NodeType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(jpdl32::EStringToStringMapEntry)


def test_jpdl32::estringtostringmapentry_constructor_exists():
    assert callable(jpdl32::EStringToStringMapEntry.__init__)


def test_jpdl32::estringtostringmapentry_constructor_args():
    sig = inspect.signature(jpdl32::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpdl32::documentroot_is_not_abstract():
    assert not inspect.isabstract(jpdl32::DocumentRoot)


def test_jpdl32::documentroot_constructor_exists():
    assert callable(jpdl32::DocumentRoot.__init__)


def test_jpdl32::documentroot_constructor_args():
    sig = inspect.signature(jpdl32::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "template" in params, "Missing parameter 'template'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "recipients" in params, "Missing parameter 'recipients'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "text" in params, "Missing parameter 'text'"
    assert "to" in params, "Missing parameter 'to'"

def test_jpdl32::documentroot_has_description():
    assert hasattr(jpdl32::DocumentRoot, "description")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::documentroot_has_template():
    assert hasattr(jpdl32::DocumentRoot, "template")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::documentroot_has_subject():
    assert hasattr(jpdl32::DocumentRoot, "subject")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::documentroot_has_recipients():
    assert hasattr(jpdl32::DocumentRoot, "recipients")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "recipients" in klass.__dict__:
            descriptor = klass.__dict__["recipients"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::documentroot_has_mixed():
    assert hasattr(jpdl32::DocumentRoot, "mixed")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::documentroot_has_text():
    assert hasattr(jpdl32::DocumentRoot, "text")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::documentroot_has_to():
    assert hasattr(jpdl32::DocumentRoot, "to")
    descriptor = None
    for klass in jpdl32::DocumentRoot.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::transitiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::TransitionType)


def test_jpdl32::transitiontype_constructor_exists():
    assert callable(jpdl32::TransitionType.__init__)


def test_jpdl32::transitiontype_constructor_args():
    sig = inspect.signature(jpdl32::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"
    assert "to" in params, "Missing parameter 'to'"
    assert "description" in params, "Missing parameter 'description'"

def test_jpdl32::transitiontype_has_group():
    assert hasattr(jpdl32::TransitionType, "group")
    descriptor = None
    for klass in jpdl32::TransitionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::transitiontype_has_name():
    assert hasattr(jpdl32::TransitionType, "name")
    descriptor = None
    for klass in jpdl32::TransitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::transitiontype_has_to():
    assert hasattr(jpdl32::TransitionType, "to")
    descriptor = None
    for klass in jpdl32::TransitionType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::transitiontype_has_description():
    assert hasattr(jpdl32::TransitionType, "description")
    descriptor = None
    for klass in jpdl32::TransitionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::exceptionhandlertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ExceptionHandlerType)


def test_jpdl32::exceptionhandlertype_constructor_exists():
    assert callable(jpdl32::ExceptionHandlerType.__init__)


def test_jpdl32::exceptionhandlertype_constructor_args():
    sig = inspect.signature(jpdl32::ExceptionHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionClass" in params, "Missing parameter 'exceptionClass'"
    assert "group" in params, "Missing parameter 'group'"

def test_jpdl32::exceptionhandlertype_has_exceptionClass():
    assert hasattr(jpdl32::ExceptionHandlerType, "exceptionClass")
    descriptor = None
    for klass in jpdl32::ExceptionHandlerType.__mro__:
        if "exceptionClass" in klass.__dict__:
            descriptor = klass.__dict__["exceptionClass"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::exceptionhandlertype_has_group():
    assert hasattr(jpdl32::ExceptionHandlerType, "group")
    descriptor = None
    for klass in jpdl32::ExceptionHandlerType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::eventtype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::EventType)


def test_jpdl32::eventtype_constructor_exists():
    assert callable(jpdl32::EventType.__init__)


def test_jpdl32::eventtype_constructor_args():
    sig = inspect.signature(jpdl32::EventType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "actionElements" in params, "Missing parameter 'actionElements'"

def test_jpdl32::eventtype_has_type():
    assert hasattr(jpdl32::EventType, "type")
    descriptor = None
    for klass in jpdl32::EventType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::eventtype_has_actionElements():
    assert hasattr(jpdl32::EventType, "actionElements")
    descriptor = None
    for klass in jpdl32::EventType.__mro__:
        if "actionElements" in klass.__dict__:
            descriptor = klass.__dict__["actionElements"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::delegation_is_not_abstract():
    assert not inspect.isabstract(jpdl32::Delegation)


def test_jpdl32::delegation_constructor_exists():
    assert callable(jpdl32::Delegation.__init__)


def test_jpdl32::delegation_constructor_args():
    sig = inspect.signature(jpdl32::Delegation.__init__)
    params = list(sig.parameters.keys())
    assert "configType" in params, "Missing parameter 'configType'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_jpdl32::delegation_has_configType():
    assert hasattr(jpdl32::Delegation, "configType")
    descriptor = None
    for klass in jpdl32::Delegation.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::delegation_has_class_():
    assert hasattr(jpdl32::Delegation, "class_")
    descriptor = None
    for klass in jpdl32::Delegation.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::delegation_has_any():
    assert hasattr(jpdl32::Delegation, "any")
    descriptor = None
    for klass in jpdl32::Delegation.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::delegation_has_mixed():
    assert hasattr(jpdl32::Delegation, "mixed")
    descriptor = None
    for klass in jpdl32::Delegation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::decisiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::DecisionType)


def test_jpdl32::decisiontype_constructor_exists():
    assert callable(jpdl32::DecisionType.__init__)


def test_jpdl32::decisiontype_constructor_args():
    sig = inspect.signature(jpdl32::DecisionType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "description" in params, "Missing parameter 'description'"

def test_jpdl32::decisiontype_has_name():
    assert hasattr(jpdl32::DecisionType, "name")
    descriptor = None
    for klass in jpdl32::DecisionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::decisiontype_has_group():
    assert hasattr(jpdl32::DecisionType, "group")
    descriptor = None
    for klass in jpdl32::DecisionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::decisiontype_has_expression():
    assert hasattr(jpdl32::DecisionType, "expression")
    descriptor = None
    for klass in jpdl32::DecisionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::decisiontype_has_async_():
    assert hasattr(jpdl32::DecisionType, "async_")
    descriptor = None
    for klass in jpdl32::DecisionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::decisiontype_has_description():
    assert hasattr(jpdl32::DecisionType, "description")
    descriptor = None
    for klass in jpdl32::DecisionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::createtimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::CreateTimerType)


def test_jpdl32::createtimertype_constructor_exists():
    assert callable(jpdl32::CreateTimerType.__init__)


def test_jpdl32::createtimertype_constructor_args():
    sig = inspect.signature(jpdl32::CreateTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "duedate" in params, "Missing parameter 'duedate'"
    assert "transition" in params, "Missing parameter 'transition'"
    assert "name" in params, "Missing parameter 'name'"
    assert "repeat" in params, "Missing parameter 'repeat'"

def test_jpdl32::createtimertype_has_duedate():
    assert hasattr(jpdl32::CreateTimerType, "duedate")
    descriptor = None
    for klass in jpdl32::CreateTimerType.__mro__:
        if "duedate" in klass.__dict__:
            descriptor = klass.__dict__["duedate"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::createtimertype_has_transition():
    assert hasattr(jpdl32::CreateTimerType, "transition")
    descriptor = None
    for klass in jpdl32::CreateTimerType.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::createtimertype_has_name():
    assert hasattr(jpdl32::CreateTimerType, "name")
    descriptor = None
    for klass in jpdl32::CreateTimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::createtimertype_has_repeat():
    assert hasattr(jpdl32::CreateTimerType, "repeat")
    descriptor = None
    for klass in jpdl32::CreateTimerType.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::scripttype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ScriptType)


def test_jpdl32::scripttype_constructor_exists():
    assert callable(jpdl32::ScriptType.__init__)


def test_jpdl32::scripttype_constructor_args():
    sig = inspect.signature(jpdl32::ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::scripttype_has_acceptPropagatedEvents():
    assert hasattr(jpdl32::ScriptType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl32::ScriptType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::scripttype_has_mixed():
    assert hasattr(jpdl32::ScriptType, "mixed")
    descriptor = None
    for klass in jpdl32::ScriptType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::scripttype_has_any():
    assert hasattr(jpdl32::ScriptType, "any")
    descriptor = None
    for klass in jpdl32::ScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::scripttype_has_name():
    assert hasattr(jpdl32::ScriptType, "name")
    descriptor = None
    for klass in jpdl32::ScriptType.__mro__:
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



def test_jpdl32::assignmenttype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::AssignmentType)


def test_jpdl32::assignmenttype_constructor_exists():
    assert callable(jpdl32::AssignmentType.__init__)


def test_jpdl32::assignmenttype_constructor_args():
    sig = inspect.signature(jpdl32::AssignmentType.__init__)
    params = list(sig.parameters.keys())
    assert "actorId" in params, "Missing parameter 'actorId'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "pooledActors" in params, "Missing parameter 'pooledActors'"

def test_jpdl32::assignmenttype_has_actorId():
    assert hasattr(jpdl32::AssignmentType, "actorId")
    descriptor = None
    for klass in jpdl32::AssignmentType.__mro__:
        if "actorId" in klass.__dict__:
            descriptor = klass.__dict__["actorId"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::assignmenttype_has_expression():
    assert hasattr(jpdl32::AssignmentType, "expression")
    descriptor = None
    for klass in jpdl32::AssignmentType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::assignmenttype_has_pooledActors():
    assert hasattr(jpdl32::AssignmentType, "pooledActors")
    descriptor = None
    for klass in jpdl32::AssignmentType.__mro__:
        if "pooledActors" in klass.__dict__:
            descriptor = klass.__dict__["pooledActors"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::conditiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ConditionType)


def test_jpdl32::conditiontype_constructor_exists():
    assert callable(jpdl32::ConditionType.__init__)


def test_jpdl32::conditiontype_constructor_args():
    sig = inspect.signature(jpdl32::ConditionType.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"

def test_jpdl32::conditiontype_has_expression():
    assert hasattr(jpdl32::ConditionType, "expression")
    descriptor = None
    for klass in jpdl32::ConditionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::conditiontype_has_group():
    assert hasattr(jpdl32::ConditionType, "group")
    descriptor = None
    for klass in jpdl32::ConditionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::conditiontype_has_mixed():
    assert hasattr(jpdl32::ConditionType, "mixed")
    descriptor = None
    for klass in jpdl32::ConditionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::conditiontype_has_any():
    assert hasattr(jpdl32::ConditionType, "any")
    descriptor = None
    for klass in jpdl32::ConditionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::canceltimertype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::CancelTimerType)


def test_jpdl32::canceltimertype_constructor_exists():
    assert callable(jpdl32::CancelTimerType.__init__)


def test_jpdl32::canceltimertype_constructor_args():
    sig = inspect.signature(jpdl32::CancelTimerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpdl32::canceltimertype_has_name():
    assert hasattr(jpdl32::CancelTimerType, "name")
    descriptor = None
    for klass in jpdl32::CancelTimerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpdl32::actiontype_is_not_abstract():
    assert not inspect.isabstract(jpdl32::ActionType)


def test_jpdl32::actiontype_constructor_exists():
    assert callable(jpdl32::ActionType.__init__)


def test_jpdl32::actiontype_constructor_args():
    sig = inspect.signature(jpdl32::ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "acceptPropagatedEvents" in params, "Missing parameter 'acceptPropagatedEvents'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "refName" in params, "Missing parameter 'refName'"
    assert "any" in params, "Missing parameter 'any'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "configType" in params, "Missing parameter 'configType'"

def test_jpdl32::actiontype_has_class_():
    assert hasattr(jpdl32::ActionType, "class_")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_acceptPropagatedEvents():
    assert hasattr(jpdl32::ActionType, "acceptPropagatedEvents")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "acceptPropagatedEvents" in klass.__dict__:
            descriptor = klass.__dict__["acceptPropagatedEvents"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_expression():
    assert hasattr(jpdl32::ActionType, "expression")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_name():
    assert hasattr(jpdl32::ActionType, "name")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_mixed():
    assert hasattr(jpdl32::ActionType, "mixed")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_refName():
    assert hasattr(jpdl32::ActionType, "refName")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "refName" in klass.__dict__:
            descriptor = klass.__dict__["refName"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_any():
    assert hasattr(jpdl32::ActionType, "any")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_async_():
    assert hasattr(jpdl32::ActionType, "async_")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_jpdl32::actiontype_has_configType():
    assert hasattr(jpdl32::ActionType, "configType")
    descriptor = None
    for klass in jpdl32::ActionType.__mro__:
        if "configType" in klass.__dict__:
            descriptor = klass.__dict__["configType"]
            break
    assert isinstance(descriptor, property)

def test_configtype_exists():
    # Check that the Enumeration exists
    assert ConfigType is not None

def test_configtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigType]
    expected_literals = [
        "bean",
        "constructor",
        "field",
        "configurationProperty",
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
        "normal",
        "high",
        "low",
        "highest",
        "lowest",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityTypeMember0"

def test_signaltype_exists():
    # Check that the Enumeration exists
    assert SignalType is not None

def test_signaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalType]
    expected_literals = [
        "lastWait",
        "unsynchronized",
        "firstWait",
        "first",
        "never",
        "last",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalType"

def test_booleantype_exists():
    # Check that the Enumeration exists
    assert BooleanType is not None

def test_booleantype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanType]
    expected_literals = [
        "yes",
        "no",
        "on",
        "false",
        "off",
        "true",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanType"

def test_typetypemember1_exists():
    # Check that the Enumeration exists
    assert TypeTypeMember1 is not None

def test_typetypemember1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeTypeMember1]
    expected_literals = [
        "beforeSignal",
        "nodeEnter",
        "taskEnd",
        "nodeLeave",
        "subprocessCreated",
        "superstateLeave",
        "processEnd",
        "afterSignal",
        "superstateEnter",
        "taskCreate",
        "taskStart",
        "taskAssign",
        "timerCreate",
        "processStart",
        "subprocessEnd",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeTypeMember1"

def test_bindingtype_exists():
    # Check that the Enumeration exists
    assert BindingType is not None

def test_bindingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingType]
    expected_literals = [
        "late",
        "early",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingType"


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
jpdl32::SubProcessType_strategy = st.builds(
    jpdl32::SubProcessType,
    binding=
        safe_text,
    name=
        safe_text,
    version=
        safe_text
)
jpdl32::ReminderType_strategy = st.builds(
    jpdl32::ReminderType,
    repeat=
        safe_text,
    duedate=
        safe_text
)
jpdl32::TimerType_strategy = st.builds(
    jpdl32::TimerType,
    repeat=
        safe_text,
    duedate=
        safe_text,
    transition=
        safe_text,
    name=
        safe_text
)
jpdl32::TaskNodeType_strategy = st.builds(
    jpdl32::TaskNodeType,
    createTasks=
        safe_text,
    name=
        safe_text,
    signal=
        safe_text,
    group=
        safe_text,
    endTasks=
        safe_text,
    description=
        safe_text,
    async_=
        safe_text
)
jpdl32::VariableType_strategy = st.builds(
    jpdl32::VariableType,
    name=
        safe_text,
    any=
        safe_text,
    mappedName=
        safe_text,
    access=
        safe_text
)
jpdl32::SwimlaneType_strategy = st.builds(
    jpdl32::SwimlaneType,
    name=
        safe_text
)
jpdl32::SuperStateType_strategy = st.builds(
    jpdl32::SuperStateType,
    description=
        safe_text,
    async_=
        safe_text,
    group=
        safe_text,
    name=
        safe_text
)
jpdl32::StateType_strategy = st.builds(
    jpdl32::StateType,
    nodeContentElements=
        safe_text,
    async_=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
jpdl32::StartStateType_strategy = st.builds(
    jpdl32::StartStateType,
    name=
        safe_text,
    description=
        safe_text,
    group=
        safe_text
)
jpdl32::ProcessStateType_strategy = st.builds(
    jpdl32::ProcessStateType,
    async_=
        safe_text,
    description=
        safe_text,
    group=
        safe_text,
    binding=
        safe_text,
    name=
        safe_text
)
jpdl32::ProcessDefinitionType_strategy = st.builds(
    jpdl32::ProcessDefinitionType,
    description=
        safe_text,
    group=
        safe_text,
    name=
        safe_text
)
jpdl32::TaskType_strategy = st.builds(
    jpdl32::TaskType,
    signalling=
        safe_text,
    swimlane=
        safe_text,
    duedate=
        safe_text,
    group=
        safe_text,
    description=
        safe_text,
    blocking=
        safe_text,
    name=
        safe_text,
    notify=
        safe_text,
    priority=
        safe_text,
    description1=
        safe_text
)
jpdl32::MailNodeType_strategy = st.builds(
    jpdl32::MailNodeType,
    to=
        safe_text,
    subject=
        safe_text,
    description=
        safe_text,
    text1=
        safe_text,
    template=
        safe_text,
    name=
        safe_text,
    async_=
        safe_text,
    actors=
        safe_text,
    subject1=
        safe_text,
    text=
        safe_text,
    group=
        safe_text
)
jpdl32::MailType_strategy = st.builds(
    jpdl32::MailType,
    text=
        safe_text,
    text1=
        safe_text,
    name=
        safe_text,
    actors=
        safe_text,
    subject1=
        safe_text,
    template=
        safe_text,
    async_=
        safe_text,
    group=
        safe_text,
    subject=
        safe_text,
    to=
        safe_text
)
jpdl32::JoinType_strategy = st.builds(
    jpdl32::JoinType,
    name=
        safe_text,
    nodeContentElements=
        safe_text,
    description=
        safe_text,
    async_=
        safe_text
)
jpdl32::ForkType_strategy = st.builds(
    jpdl32::ForkType,
    name=
        safe_text,
    group=
        safe_text,
    description=
        safe_text,
    async_=
        safe_text
)
jpdl32::EndStateType_strategy = st.builds(
    jpdl32::EndStateType,
    group=
        safe_text,
    endCompleteProcess=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
jpdl32::NodeType_strategy = st.builds(
    jpdl32::NodeType,
    async_=
        safe_text,
    nodeContentElements=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
jpdl32::EStringToStringMapEntry_strategy = st.builds(
    jpdl32::EStringToStringMapEntry,
)
jpdl32::DocumentRoot_strategy = st.builds(
    jpdl32::DocumentRoot,
    description=
        safe_text,
    template=
        safe_text,
    subject=
        safe_text,
    recipients=
        safe_text,
    mixed=
        safe_text,
    text=
        safe_text,
    to=
        safe_text
)
jpdl32::TransitionType_strategy = st.builds(
    jpdl32::TransitionType,
    group=
        safe_text,
    name=
        safe_text,
    to=
        safe_text,
    description=
        safe_text
)
jpdl32::ExceptionHandlerType_strategy = st.builds(
    jpdl32::ExceptionHandlerType,
    exceptionClass=
        safe_text,
    group=
        safe_text
)
jpdl32::EventType_strategy = st.builds(
    jpdl32::EventType,
    type=
        safe_text,
    actionElements=
        safe_text
)
jpdl32::Delegation_strategy = st.builds(
    jpdl32::Delegation,
    configType=
        safe_text,
    class_=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text
)
jpdl32::DecisionType_strategy = st.builds(
    jpdl32::DecisionType,
    name=
        safe_text,
    group=
        safe_text,
    expression=
        safe_text,
    async_=
        safe_text,
    description=
        safe_text
)
jpdl32::CreateTimerType_strategy = st.builds(
    jpdl32::CreateTimerType,
    duedate=
        safe_text,
    transition=
        safe_text,
    name=
        safe_text,
    repeat=
        safe_text
)
jpdl32::ScriptType_strategy = st.builds(
    jpdl32::ScriptType,
    acceptPropagatedEvents=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text,
    name=
        safe_text
)
Delegation_strategy = st.builds(
    Delegation,
)
jpdl32::AssignmentType_strategy = st.builds(
    jpdl32::AssignmentType,
    actorId=
        safe_text,
    expression=
        safe_text,
    pooledActors=
        safe_text
)
jpdl32::ConditionType_strategy = st.builds(
    jpdl32::ConditionType,
    expression=
        safe_text,
    group=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text
)
jpdl32::CancelTimerType_strategy = st.builds(
    jpdl32::CancelTimerType,
    name=
        safe_text
)
jpdl32::ActionType_strategy = st.builds(
    jpdl32::ActionType,
    class_=
        safe_text,
    acceptPropagatedEvents=
        safe_text,
    expression=
        safe_text,
    name=
        safe_text,
    mixed=
        safe_text,
    refName=
        safe_text,
    any=
        safe_text,
    async_=
        safe_text,
    configType=
        safe_text
)

@given(instance=jpdl32::SubProcessType_strategy)
@settings(max_examples=50)
def test_jpdl32::subprocesstype_instantiation(instance):
    assert isinstance(instance, jpdl32::SubProcessType)

@given(instance=jpdl32::SubProcessType_strategy)
def test_jpdl32::subprocesstype_binding_type(instance):
    assert isinstance(instance.binding, str)


@given(instance=jpdl32::SubProcessType_strategy)
def test_jpdl32::subprocesstype_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original

@given(instance=jpdl32::SubProcessType_strategy)
def test_jpdl32::subprocesstype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::SubProcessType_strategy)
def test_jpdl32::subprocesstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::SubProcessType_strategy)
def test_jpdl32::subprocesstype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=jpdl32::SubProcessType_strategy)
def test_jpdl32::subprocesstype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=jpdl32::ReminderType_strategy)
@settings(max_examples=50)
def test_jpdl32::remindertype_instantiation(instance):
    assert isinstance(instance, jpdl32::ReminderType)

@given(instance=jpdl32::ReminderType_strategy)
def test_jpdl32::remindertype_repeat_type(instance):
    assert isinstance(instance.repeat, str)


@given(instance=jpdl32::ReminderType_strategy)
def test_jpdl32::remindertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=jpdl32::ReminderType_strategy)
def test_jpdl32::remindertype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl32::ReminderType_strategy)
def test_jpdl32::remindertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl32::TimerType_strategy)
@settings(max_examples=50)
def test_jpdl32::timertype_instantiation(instance):
    assert isinstance(instance, jpdl32::TimerType)

@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_repeat_type(instance):
    assert isinstance(instance.repeat, str)


@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_transition_type(instance):
    assert isinstance(instance.transition, str)


@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::TimerType_strategy)
def test_jpdl32::timertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::TaskNodeType_strategy)
@settings(max_examples=50)
def test_jpdl32::tasknodetype_instantiation(instance):
    assert isinstance(instance, jpdl32::TaskNodeType)

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_createTasks_type(instance):
    assert isinstance(instance.createTasks, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_createTasks_setter(instance):
    original = instance.createTasks
    instance.createTasks = original
    assert instance.createTasks == original

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_endTasks_type(instance):
    assert isinstance(instance.endTasks, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_endTasks_setter(instance):
    original = instance.endTasks
    instance.endTasks = original
    assert instance.endTasks == original

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::TaskNodeType_strategy)
def test_jpdl32::tasknodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::VariableType_strategy)
@settings(max_examples=50)
def test_jpdl32::variabletype_instantiation(instance):
    assert isinstance(instance, jpdl32::VariableType)

@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_mappedName_type(instance):
    assert isinstance(instance.mappedName, str)


@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_mappedName_setter(instance):
    original = instance.mappedName
    instance.mappedName = original
    assert instance.mappedName == original

@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=jpdl32::VariableType_strategy)
def test_jpdl32::variabletype_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=jpdl32::SwimlaneType_strategy)
@settings(max_examples=50)
def test_jpdl32::swimlanetype_instantiation(instance):
    assert isinstance(instance, jpdl32::SwimlaneType)

@given(instance=jpdl32::SwimlaneType_strategy)
def test_jpdl32::swimlanetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::SwimlaneType_strategy)
def test_jpdl32::swimlanetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::SuperStateType_strategy)
@settings(max_examples=50)
def test_jpdl32::superstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32::SuperStateType)

@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::SuperStateType_strategy)
def test_jpdl32::superstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::StateType_strategy)
@settings(max_examples=50)
def test_jpdl32::statetype_instantiation(instance):
    assert isinstance(instance, jpdl32::StateType)

@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_nodeContentElements_type(instance):
    assert isinstance(instance.nodeContentElements, str)


@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::StateType_strategy)
def test_jpdl32::statetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::StartStateType_strategy)
@settings(max_examples=50)
def test_jpdl32::startstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32::StartStateType)

@given(instance=jpdl32::StartStateType_strategy)
def test_jpdl32::startstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::StartStateType_strategy)
def test_jpdl32::startstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::StartStateType_strategy)
def test_jpdl32::startstatetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::StartStateType_strategy)
def test_jpdl32::startstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::StartStateType_strategy)
def test_jpdl32::startstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::StartStateType_strategy)
def test_jpdl32::startstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::ProcessStateType_strategy)
@settings(max_examples=50)
def test_jpdl32::processstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32::ProcessStateType)

@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_binding_type(instance):
    assert isinstance(instance.binding, str)


@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original

@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::ProcessStateType_strategy)
def test_jpdl32::processstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::ProcessDefinitionType_strategy)
@settings(max_examples=50)
def test_jpdl32::processdefinitiontype_instantiation(instance):
    assert isinstance(instance, jpdl32::ProcessDefinitionType)

@given(instance=jpdl32::ProcessDefinitionType_strategy)
def test_jpdl32::processdefinitiontype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::ProcessDefinitionType_strategy)
def test_jpdl32::processdefinitiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::ProcessDefinitionType_strategy)
def test_jpdl32::processdefinitiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::ProcessDefinitionType_strategy)
def test_jpdl32::processdefinitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::ProcessDefinitionType_strategy)
def test_jpdl32::processdefinitiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::ProcessDefinitionType_strategy)
def test_jpdl32::processdefinitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::TaskType_strategy)
@settings(max_examples=50)
def test_jpdl32::tasktype_instantiation(instance):
    assert isinstance(instance, jpdl32::TaskType)

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_signalling_type(instance):
    assert isinstance(instance.signalling, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_signalling_setter(instance):
    original = instance.signalling
    instance.signalling = original
    assert instance.signalling == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_swimlane_type(instance):
    assert isinstance(instance.swimlane, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_swimlane_setter(instance):
    original = instance.swimlane
    instance.swimlane = original
    assert instance.swimlane == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_blocking_type(instance):
    assert isinstance(instance.blocking, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_blocking_setter(instance):
    original = instance.blocking
    instance.blocking = original
    assert instance.blocking == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_notify_type(instance):
    assert isinstance(instance.notify, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_notify_setter(instance):
    original = instance.notify
    instance.notify = original
    assert instance.notify == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_description1_type(instance):
    assert isinstance(instance.description1, str)


@given(instance=jpdl32::TaskType_strategy)
def test_jpdl32::tasktype_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original

@given(instance=jpdl32::MailNodeType_strategy)
@settings(max_examples=50)
def test_jpdl32::mailnodetype_instantiation(instance):
    assert isinstance(instance, jpdl32::MailNodeType)

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_text1_type(instance):
    assert isinstance(instance.text1, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_text1_setter(instance):
    original = instance.text1
    instance.text1 = original
    assert instance.text1 == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_actors_type(instance):
    assert isinstance(instance.actors, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_subject1_type(instance):
    assert isinstance(instance.subject1, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_subject1_setter(instance):
    original = instance.subject1
    instance.subject1 = original
    assert instance.subject1 == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::MailNodeType_strategy)
def test_jpdl32::mailnodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::MailType_strategy)
@settings(max_examples=50)
def test_jpdl32::mailtype_instantiation(instance):
    assert isinstance(instance, jpdl32::MailType)

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_text1_type(instance):
    assert isinstance(instance.text1, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_text1_setter(instance):
    original = instance.text1
    instance.text1 = original
    assert instance.text1 == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_actors_type(instance):
    assert isinstance(instance.actors, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_subject1_type(instance):
    assert isinstance(instance.subject1, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_subject1_setter(instance):
    original = instance.subject1
    instance.subject1 = original
    assert instance.subject1 == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jpdl32::MailType_strategy)
def test_jpdl32::mailtype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl32::JoinType_strategy)
@settings(max_examples=50)
def test_jpdl32::jointype_instantiation(instance):
    assert isinstance(instance, jpdl32::JoinType)

@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_nodeContentElements_type(instance):
    assert isinstance(instance.nodeContentElements, str)


@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::JoinType_strategy)
def test_jpdl32::jointype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::ForkType_strategy)
@settings(max_examples=50)
def test_jpdl32::forktype_instantiation(instance):
    assert isinstance(instance, jpdl32::ForkType)

@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::ForkType_strategy)
def test_jpdl32::forktype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::EndStateType_strategy)
@settings(max_examples=50)
def test_jpdl32::endstatetype_instantiation(instance):
    assert isinstance(instance, jpdl32::EndStateType)

@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_endCompleteProcess_type(instance):
    assert isinstance(instance.endCompleteProcess, str)


@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_endCompleteProcess_setter(instance):
    original = instance.endCompleteProcess
    instance.endCompleteProcess = original
    assert instance.endCompleteProcess == original

@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::EndStateType_strategy)
def test_jpdl32::endstatetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::NodeType_strategy)
@settings(max_examples=50)
def test_jpdl32::nodetype_instantiation(instance):
    assert isinstance(instance, jpdl32::NodeType)

@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_nodeContentElements_type(instance):
    assert isinstance(instance.nodeContentElements, str)


@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_nodeContentElements_setter(instance):
    original = instance.nodeContentElements
    instance.nodeContentElements = original
    assert instance.nodeContentElements == original

@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::NodeType_strategy)
def test_jpdl32::nodetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_jpdl32::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, jpdl32::EStringToStringMapEntry)

@given(instance=jpdl32::DocumentRoot_strategy)
@settings(max_examples=50)
def test_jpdl32::documentroot_instantiation(instance):
    assert isinstance(instance, jpdl32::DocumentRoot)

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_recipients_type(instance):
    assert isinstance(instance.recipients, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_recipients_setter(instance):
    original = instance.recipients
    instance.recipients = original
    assert instance.recipients == original

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jpdl32::DocumentRoot_strategy)
def test_jpdl32::documentroot_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl32::TransitionType_strategy)
@settings(max_examples=50)
def test_jpdl32::transitiontype_instantiation(instance):
    assert isinstance(instance, jpdl32::TransitionType)

@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::TransitionType_strategy)
def test_jpdl32::transitiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::ExceptionHandlerType_strategy)
@settings(max_examples=50)
def test_jpdl32::exceptionhandlertype_instantiation(instance):
    assert isinstance(instance, jpdl32::ExceptionHandlerType)

@given(instance=jpdl32::ExceptionHandlerType_strategy)
def test_jpdl32::exceptionhandlertype_exceptionClass_type(instance):
    assert isinstance(instance.exceptionClass, str)


@given(instance=jpdl32::ExceptionHandlerType_strategy)
def test_jpdl32::exceptionhandlertype_exceptionClass_setter(instance):
    original = instance.exceptionClass
    instance.exceptionClass = original
    assert instance.exceptionClass == original

@given(instance=jpdl32::ExceptionHandlerType_strategy)
def test_jpdl32::exceptionhandlertype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::ExceptionHandlerType_strategy)
def test_jpdl32::exceptionhandlertype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::EventType_strategy)
@settings(max_examples=50)
def test_jpdl32::eventtype_instantiation(instance):
    assert isinstance(instance, jpdl32::EventType)

@given(instance=jpdl32::EventType_strategy)
def test_jpdl32::eventtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jpdl32::EventType_strategy)
def test_jpdl32::eventtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jpdl32::EventType_strategy)
def test_jpdl32::eventtype_actionElements_type(instance):
    assert isinstance(instance.actionElements, str)


@given(instance=jpdl32::EventType_strategy)
def test_jpdl32::eventtype_actionElements_setter(instance):
    original = instance.actionElements
    instance.actionElements = original
    assert instance.actionElements == original

@given(instance=jpdl32::Delegation_strategy)
@settings(max_examples=50)
def test_jpdl32::delegation_instantiation(instance):
    assert isinstance(instance, jpdl32::Delegation)

@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_configType_type(instance):
    assert isinstance(instance.configType, str)


@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original

@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl32::Delegation_strategy)
def test_jpdl32::delegation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl32::DecisionType_strategy)
@settings(max_examples=50)
def test_jpdl32::decisiontype_instantiation(instance):
    assert isinstance(instance, jpdl32::DecisionType)

@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=jpdl32::DecisionType_strategy)
def test_jpdl32::decisiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=jpdl32::CreateTimerType_strategy)
@settings(max_examples=50)
def test_jpdl32::createtimertype_instantiation(instance):
    assert isinstance(instance, jpdl32::CreateTimerType)

@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_duedate_type(instance):
    assert isinstance(instance.duedate, str)


@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_duedate_setter(instance):
    original = instance.duedate
    instance.duedate = original
    assert instance.duedate == original

@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_transition_type(instance):
    assert isinstance(instance.transition, str)


@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_repeat_type(instance):
    assert isinstance(instance.repeat, str)


@given(instance=jpdl32::CreateTimerType_strategy)
def test_jpdl32::createtimertype_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=jpdl32::ScriptType_strategy)
@settings(max_examples=50)
def test_jpdl32::scripttype_instantiation(instance):
    assert isinstance(instance, jpdl32::ScriptType)

@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_acceptPropagatedEvents_type(instance):
    assert isinstance(instance.acceptPropagatedEvents, str)


@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original

@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::ScriptType_strategy)
def test_jpdl32::scripttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Delegation_strategy)
@settings(max_examples=50)
def test_delegation_instantiation(instance):
    assert isinstance(instance, Delegation)

@given(instance=jpdl32::AssignmentType_strategy)
@settings(max_examples=50)
def test_jpdl32::assignmenttype_instantiation(instance):
    assert isinstance(instance, jpdl32::AssignmentType)

@given(instance=jpdl32::AssignmentType_strategy)
def test_jpdl32::assignmenttype_actorId_type(instance):
    assert isinstance(instance.actorId, str)


@given(instance=jpdl32::AssignmentType_strategy)
def test_jpdl32::assignmenttype_actorId_setter(instance):
    original = instance.actorId
    instance.actorId = original
    assert instance.actorId == original

@given(instance=jpdl32::AssignmentType_strategy)
def test_jpdl32::assignmenttype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl32::AssignmentType_strategy)
def test_jpdl32::assignmenttype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl32::AssignmentType_strategy)
def test_jpdl32::assignmenttype_pooledActors_type(instance):
    assert isinstance(instance.pooledActors, str)


@given(instance=jpdl32::AssignmentType_strategy)
def test_jpdl32::assignmenttype_pooledActors_setter(instance):
    original = instance.pooledActors
    instance.pooledActors = original
    assert instance.pooledActors == original

@given(instance=jpdl32::ConditionType_strategy)
@settings(max_examples=50)
def test_jpdl32::conditiontype_instantiation(instance):
    assert isinstance(instance, jpdl32::ConditionType)

@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl32::ConditionType_strategy)
def test_jpdl32::conditiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl32::CancelTimerType_strategy)
@settings(max_examples=50)
def test_jpdl32::canceltimertype_instantiation(instance):
    assert isinstance(instance, jpdl32::CancelTimerType)

@given(instance=jpdl32::CancelTimerType_strategy)
def test_jpdl32::canceltimertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::CancelTimerType_strategy)
def test_jpdl32::canceltimertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::ActionType_strategy)
@settings(max_examples=50)
def test_jpdl32::actiontype_instantiation(instance):
    assert isinstance(instance, jpdl32::ActionType)

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_acceptPropagatedEvents_type(instance):
    assert isinstance(instance.acceptPropagatedEvents, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_acceptPropagatedEvents_setter(instance):
    original = instance.acceptPropagatedEvents
    instance.acceptPropagatedEvents = original
    assert instance.acceptPropagatedEvents == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_refName_type(instance):
    assert isinstance(instance.refName, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_refName_setter(instance):
    original = instance.refName
    instance.refName = original
    assert instance.refName == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_async__type(instance):
    assert isinstance(instance.async_, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_configType_type(instance):
    assert isinstance(instance.configType, str)


@given(instance=jpdl32::ActionType_strategy)
def test_jpdl32::actiontype_configType_setter(instance):
    original = instance.configType
    instance.configType = original
    assert instance.configType == original
