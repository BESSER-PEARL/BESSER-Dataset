import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PropertyKeyContainer,
    behaviour::TaskDescriptor,
    behaviour::CapabilityProperties,
    behaviour::Capability,
    behaviour::Robot,
    behaviour::DetectedObject,
    behaviour::RobotCollaboration,
    behaviour::Task,
    CommunicationAction,
    behaviour::BroadcastCommunication,
    behaviour::MulticastCommunication,
    behaviour::UnicastCommunication,
    Action,
    behaviour::CommunicationAction,
    behaviour::MeasureValue,
    behaviour::AreaObject,
    behaviour::Property,
    NamedElement,
    behaviour::Action,
    behaviour::MessageRepository,
    behaviour::Message,
    behaviour::BehaviouralPropertyKeyContainer,
    behaviour::TaskRequirement,
    behaviour::TaskExecution,
    behaviour::DynamicRobot,
    behaviour::BehaviourContainer,
    RobotStatus,
    TaskExecutionStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_propertykeycontainer_is_not_abstract():
    assert not inspect.isabstract(PropertyKeyContainer)


def test_propertykeycontainer_constructor_exists():
    assert callable(PropertyKeyContainer.__init__)


def test_propertykeycontainer_constructor_args():
    sig = inspect.signature(PropertyKeyContainer.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::taskdescriptor_is_not_abstract():
    assert not inspect.isabstract(behaviour::TaskDescriptor)


def test_behaviour::taskdescriptor_constructor_exists():
    assert callable(behaviour::TaskDescriptor.__init__)


def test_behaviour::taskdescriptor_constructor_args():
    sig = inspect.signature(behaviour::TaskDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::capabilityproperties_is_not_abstract():
    assert not inspect.isabstract(behaviour::CapabilityProperties)


def test_behaviour::capabilityproperties_constructor_exists():
    assert callable(behaviour::CapabilityProperties.__init__)


def test_behaviour::capabilityproperties_constructor_args():
    sig = inspect.signature(behaviour::CapabilityProperties.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::capability_is_not_abstract():
    assert not inspect.isabstract(behaviour::Capability)


def test_behaviour::capability_constructor_exists():
    assert callable(behaviour::Capability.__init__)


def test_behaviour::capability_constructor_args():
    sig = inspect.signature(behaviour::Capability.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::robot_is_not_abstract():
    assert not inspect.isabstract(behaviour::Robot)


def test_behaviour::robot_constructor_exists():
    assert callable(behaviour::Robot.__init__)


def test_behaviour::robot_constructor_args():
    sig = inspect.signature(behaviour::Robot.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::detectedobject_is_not_abstract():
    assert not inspect.isabstract(behaviour::DetectedObject)


def test_behaviour::detectedobject_constructor_exists():
    assert callable(behaviour::DetectedObject.__init__)


def test_behaviour::detectedobject_constructor_args():
    sig = inspect.signature(behaviour::DetectedObject.__init__)
    params = list(sig.parameters.keys())
    assert "obstacle" in params, "Missing parameter 'obstacle'"

def test_behaviour::detectedobject_has_obstacle():
    assert hasattr(behaviour::DetectedObject, "obstacle")
    descriptor = None
    for klass in behaviour::DetectedObject.__mro__:
        if "obstacle" in klass.__dict__:
            descriptor = klass.__dict__["obstacle"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::robotcollaboration_is_not_abstract():
    assert not inspect.isabstract(behaviour::RobotCollaboration)


def test_behaviour::robotcollaboration_constructor_exists():
    assert callable(behaviour::RobotCollaboration.__init__)


def test_behaviour::robotcollaboration_constructor_args():
    sig = inspect.signature(behaviour::RobotCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::task_is_not_abstract():
    assert not inspect.isabstract(behaviour::Task)


def test_behaviour::task_constructor_exists():
    assert callable(behaviour::Task.__init__)


def test_behaviour::task_constructor_args():
    sig = inspect.signature(behaviour::Task.__init__)
    params = list(sig.parameters.keys())



def test_communicationaction_is_not_abstract():
    assert not inspect.isabstract(CommunicationAction)


def test_communicationaction_constructor_exists():
    assert callable(CommunicationAction.__init__)


def test_communicationaction_constructor_args():
    sig = inspect.signature(CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::broadcastcommunication_is_not_abstract():
    assert not inspect.isabstract(behaviour::BroadcastCommunication)


def test_behaviour::broadcastcommunication_constructor_exists():
    assert callable(behaviour::BroadcastCommunication.__init__)


def test_behaviour::broadcastcommunication_constructor_args():
    sig = inspect.signature(behaviour::BroadcastCommunication.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::multicastcommunication_is_not_abstract():
    assert not inspect.isabstract(behaviour::MulticastCommunication)


def test_behaviour::multicastcommunication_constructor_exists():
    assert callable(behaviour::MulticastCommunication.__init__)


def test_behaviour::multicastcommunication_constructor_args():
    sig = inspect.signature(behaviour::MulticastCommunication.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::unicastcommunication_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnicastCommunication)


def test_behaviour::unicastcommunication_constructor_exists():
    assert callable(behaviour::UnicastCommunication.__init__)


def test_behaviour::unicastcommunication_constructor_args():
    sig = inspect.signature(behaviour::UnicastCommunication.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::communicationaction_is_not_abstract():
    assert not inspect.isabstract(behaviour::CommunicationAction)


def test_behaviour::communicationaction_constructor_exists():
    assert callable(behaviour::CommunicationAction.__init__)


def test_behaviour::communicationaction_constructor_args():
    sig = inspect.signature(behaviour::CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::measurevalue_is_not_abstract():
    assert not inspect.isabstract(behaviour::MeasureValue)


def test_behaviour::measurevalue_constructor_exists():
    assert callable(behaviour::MeasureValue.__init__)


def test_behaviour::measurevalue_constructor_args():
    sig = inspect.signature(behaviour::MeasureValue.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::areaobject_is_not_abstract():
    assert not inspect.isabstract(behaviour::AreaObject)


def test_behaviour::areaobject_constructor_exists():
    assert callable(behaviour::AreaObject.__init__)


def test_behaviour::areaobject_constructor_args():
    sig = inspect.signature(behaviour::AreaObject.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::property_is_not_abstract():
    assert not inspect.isabstract(behaviour::Property)


def test_behaviour::property_constructor_exists():
    assert callable(behaviour::Property.__init__)


def test_behaviour::property_constructor_args():
    sig = inspect.signature(behaviour::Property.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::action_is_not_abstract():
    assert not inspect.isabstract(behaviour::Action)


def test_behaviour::action_constructor_exists():
    assert callable(behaviour::Action.__init__)


def test_behaviour::action_constructor_args():
    sig = inspect.signature(behaviour::Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::messagerepository_is_not_abstract():
    assert not inspect.isabstract(behaviour::MessageRepository)


def test_behaviour::messagerepository_constructor_exists():
    assert callable(behaviour::MessageRepository.__init__)


def test_behaviour::messagerepository_constructor_args():
    sig = inspect.signature(behaviour::MessageRepository.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::message_is_not_abstract():
    assert not inspect.isabstract(behaviour::Message)


def test_behaviour::message_constructor_exists():
    assert callable(behaviour::Message.__init__)


def test_behaviour::message_constructor_args():
    sig = inspect.signature(behaviour::Message.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "needResponse" in params, "Missing parameter 'needResponse'"

def test_behaviour::message_has_timestamp():
    assert hasattr(behaviour::Message, "timestamp")
    descriptor = None
    for klass in behaviour::Message.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::message_has_needResponse():
    assert hasattr(behaviour::Message, "needResponse")
    descriptor = None
    for klass in behaviour::Message.__mro__:
        if "needResponse" in klass.__dict__:
            descriptor = klass.__dict__["needResponse"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::behaviouralpropertykeycontainer_is_not_abstract():
    assert not inspect.isabstract(behaviour::BehaviouralPropertyKeyContainer)


def test_behaviour::behaviouralpropertykeycontainer_constructor_exists():
    assert callable(behaviour::BehaviouralPropertyKeyContainer.__init__)


def test_behaviour::behaviouralpropertykeycontainer_constructor_args():
    sig = inspect.signature(behaviour::BehaviouralPropertyKeyContainer.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::taskrequirement_is_not_abstract():
    assert not inspect.isabstract(behaviour::TaskRequirement)


def test_behaviour::taskrequirement_constructor_exists():
    assert callable(behaviour::TaskRequirement.__init__)


def test_behaviour::taskrequirement_constructor_args():
    sig = inspect.signature(behaviour::TaskRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "participants" in params, "Missing parameter 'participants'"

def test_behaviour::taskrequirement_has_participants():
    assert hasattr(behaviour::TaskRequirement, "participants")
    descriptor = None
    for klass in behaviour::TaskRequirement.__mro__:
        if "participants" in klass.__dict__:
            descriptor = klass.__dict__["participants"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::taskexecution_is_not_abstract():
    assert not inspect.isabstract(behaviour::TaskExecution)


def test_behaviour::taskexecution_constructor_exists():
    assert callable(behaviour::TaskExecution.__init__)


def test_behaviour::taskexecution_constructor_args():
    sig = inspect.signature(behaviour::TaskExecution.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_behaviour::taskexecution_has_status():
    assert hasattr(behaviour::TaskExecution, "status")
    descriptor = None
    for klass in behaviour::TaskExecution.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::dynamicrobot_is_not_abstract():
    assert not inspect.isabstract(behaviour::DynamicRobot)


def test_behaviour::dynamicrobot_constructor_exists():
    assert callable(behaviour::DynamicRobot.__init__)


def test_behaviour::dynamicrobot_constructor_args():
    sig = inspect.signature(behaviour::DynamicRobot.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_behaviour::dynamicrobot_has_status():
    assert hasattr(behaviour::DynamicRobot, "status")
    descriptor = None
    for klass in behaviour::DynamicRobot.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::behaviourcontainer_is_not_abstract():
    assert not inspect.isabstract(behaviour::BehaviourContainer)


def test_behaviour::behaviourcontainer_constructor_exists():
    assert callable(behaviour::BehaviourContainer.__init__)


def test_behaviour::behaviourcontainer_constructor_args():
    sig = inspect.signature(behaviour::BehaviourContainer.__init__)
    params = list(sig.parameters.keys())

def test_robotstatus_exists():
    # Check that the Enumeration exists
    assert RobotStatus is not None

def test_robotstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RobotStatus]
    expected_literals = [
        "Waiting",
        "Ready",
        "Executing",
        "TurnedOff",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RobotStatus"

def test_taskexecutionstatus_exists():
    # Check that the Enumeration exists
    assert TaskExecutionStatus is not None

def test_taskexecutionstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TaskExecutionStatus]
    expected_literals = [
        "Finished",
        "InProgress",
        "Suspended",
        "Waiting",
        "Ready",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TaskExecutionStatus"


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
PropertyKeyContainer_strategy = st.builds(
    PropertyKeyContainer,
)
behaviour::TaskDescriptor_strategy = st.builds(
    behaviour::TaskDescriptor,
)
behaviour::CapabilityProperties_strategy = st.builds(
    behaviour::CapabilityProperties,
)
behaviour::Capability_strategy = st.builds(
    behaviour::Capability,
)
behaviour::Robot_strategy = st.builds(
    behaviour::Robot,
)
behaviour::DetectedObject_strategy = st.builds(
    behaviour::DetectedObject,
    obstacle=
        st.booleans()
)
behaviour::RobotCollaboration_strategy = st.builds(
    behaviour::RobotCollaboration,
)
behaviour::Task_strategy = st.builds(
    behaviour::Task,
)
CommunicationAction_strategy = st.builds(
    CommunicationAction,
)
behaviour::BroadcastCommunication_strategy = st.builds(
    behaviour::BroadcastCommunication,
)
behaviour::MulticastCommunication_strategy = st.builds(
    behaviour::MulticastCommunication,
)
behaviour::UnicastCommunication_strategy = st.builds(
    behaviour::UnicastCommunication,
)
Action_strategy = st.builds(
    Action,
)
behaviour::CommunicationAction_strategy = st.builds(
    behaviour::CommunicationAction,
)
behaviour::MeasureValue_strategy = st.builds(
    behaviour::MeasureValue,
)
behaviour::AreaObject_strategy = st.builds(
    behaviour::AreaObject,
)
behaviour::Property_strategy = st.builds(
    behaviour::Property,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behaviour::Action_strategy = st.builds(
    behaviour::Action,
)
behaviour::MessageRepository_strategy = st.builds(
    behaviour::MessageRepository,
)
behaviour::Message_strategy = st.builds(
    behaviour::Message,
    timestamp=
        st.dates(),
    needResponse=
        st.booleans()
)
behaviour::BehaviouralPropertyKeyContainer_strategy = st.builds(
    behaviour::BehaviouralPropertyKeyContainer,
)
behaviour::TaskRequirement_strategy = st.builds(
    behaviour::TaskRequirement,
    participants=
        st.integers()
)
behaviour::TaskExecution_strategy = st.builds(
    behaviour::TaskExecution,
    status=
        safe_text
)
behaviour::DynamicRobot_strategy = st.builds(
    behaviour::DynamicRobot,
    status=
        safe_text
)
behaviour::BehaviourContainer_strategy = st.builds(
    behaviour::BehaviourContainer,
)

@given(instance=PropertyKeyContainer_strategy)
@settings(max_examples=50)
def test_propertykeycontainer_instantiation(instance):
    assert isinstance(instance, PropertyKeyContainer)

@given(instance=behaviour::TaskDescriptor_strategy)
@settings(max_examples=50)
def test_behaviour::taskdescriptor_instantiation(instance):
    assert isinstance(instance, behaviour::TaskDescriptor)

@given(instance=behaviour::CapabilityProperties_strategy)
@settings(max_examples=50)
def test_behaviour::capabilityproperties_instantiation(instance):
    assert isinstance(instance, behaviour::CapabilityProperties)

@given(instance=behaviour::Capability_strategy)
@settings(max_examples=50)
def test_behaviour::capability_instantiation(instance):
    assert isinstance(instance, behaviour::Capability)

@given(instance=behaviour::Robot_strategy)
@settings(max_examples=50)
def test_behaviour::robot_instantiation(instance):
    assert isinstance(instance, behaviour::Robot)

@given(instance=behaviour::DetectedObject_strategy)
@settings(max_examples=50)
def test_behaviour::detectedobject_instantiation(instance):
    assert isinstance(instance, behaviour::DetectedObject)

@given(instance=behaviour::DetectedObject_strategy)
def test_behaviour::detectedobject_obstacle_type(instance):
    assert isinstance(instance.obstacle, bool)


@given(instance=behaviour::DetectedObject_strategy)
def test_behaviour::detectedobject_obstacle_setter(instance):
    original = instance.obstacle
    instance.obstacle = original
    assert instance.obstacle == original

@given(instance=behaviour::RobotCollaboration_strategy)
@settings(max_examples=50)
def test_behaviour::robotcollaboration_instantiation(instance):
    assert isinstance(instance, behaviour::RobotCollaboration)

@given(instance=behaviour::Task_strategy)
@settings(max_examples=50)
def test_behaviour::task_instantiation(instance):
    assert isinstance(instance, behaviour::Task)

@given(instance=CommunicationAction_strategy)
@settings(max_examples=50)
def test_communicationaction_instantiation(instance):
    assert isinstance(instance, CommunicationAction)

@given(instance=behaviour::BroadcastCommunication_strategy)
@settings(max_examples=50)
def test_behaviour::broadcastcommunication_instantiation(instance):
    assert isinstance(instance, behaviour::BroadcastCommunication)

@given(instance=behaviour::MulticastCommunication_strategy)
@settings(max_examples=50)
def test_behaviour::multicastcommunication_instantiation(instance):
    assert isinstance(instance, behaviour::MulticastCommunication)

@given(instance=behaviour::UnicastCommunication_strategy)
@settings(max_examples=50)
def test_behaviour::unicastcommunication_instantiation(instance):
    assert isinstance(instance, behaviour::UnicastCommunication)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=behaviour::CommunicationAction_strategy)
@settings(max_examples=50)
def test_behaviour::communicationaction_instantiation(instance):
    assert isinstance(instance, behaviour::CommunicationAction)

@given(instance=behaviour::MeasureValue_strategy)
@settings(max_examples=50)
def test_behaviour::measurevalue_instantiation(instance):
    assert isinstance(instance, behaviour::MeasureValue)

@given(instance=behaviour::AreaObject_strategy)
@settings(max_examples=50)
def test_behaviour::areaobject_instantiation(instance):
    assert isinstance(instance, behaviour::AreaObject)

@given(instance=behaviour::Property_strategy)
@settings(max_examples=50)
def test_behaviour::property_instantiation(instance):
    assert isinstance(instance, behaviour::Property)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behaviour::Action_strategy)
@settings(max_examples=50)
def test_behaviour::action_instantiation(instance):
    assert isinstance(instance, behaviour::Action)

@given(instance=behaviour::MessageRepository_strategy)
@settings(max_examples=50)
def test_behaviour::messagerepository_instantiation(instance):
    assert isinstance(instance, behaviour::MessageRepository)

@given(instance=behaviour::Message_strategy)
@settings(max_examples=50)
def test_behaviour::message_instantiation(instance):
    assert isinstance(instance, behaviour::Message)

@given(instance=behaviour::Message_strategy)
def test_behaviour::message_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=behaviour::Message_strategy)
def test_behaviour::message_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=behaviour::Message_strategy)
def test_behaviour::message_needResponse_type(instance):
    assert isinstance(instance.needResponse, bool)


@given(instance=behaviour::Message_strategy)
def test_behaviour::message_needResponse_setter(instance):
    original = instance.needResponse
    instance.needResponse = original
    assert instance.needResponse == original

@given(instance=behaviour::BehaviouralPropertyKeyContainer_strategy)
@settings(max_examples=50)
def test_behaviour::behaviouralpropertykeycontainer_instantiation(instance):
    assert isinstance(instance, behaviour::BehaviouralPropertyKeyContainer)

@given(instance=behaviour::TaskRequirement_strategy)
@settings(max_examples=50)
def test_behaviour::taskrequirement_instantiation(instance):
    assert isinstance(instance, behaviour::TaskRequirement)

@given(instance=behaviour::TaskRequirement_strategy)
def test_behaviour::taskrequirement_participants_type(instance):
    assert isinstance(instance.participants, int)


@given(instance=behaviour::TaskRequirement_strategy)
def test_behaviour::taskrequirement_participants_setter(instance):
    original = instance.participants
    instance.participants = original
    assert instance.participants == original

@given(instance=behaviour::TaskExecution_strategy)
@settings(max_examples=50)
def test_behaviour::taskexecution_instantiation(instance):
    assert isinstance(instance, behaviour::TaskExecution)

@given(instance=behaviour::TaskExecution_strategy)
def test_behaviour::taskexecution_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=behaviour::TaskExecution_strategy)
def test_behaviour::taskexecution_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=behaviour::DynamicRobot_strategy)
@settings(max_examples=50)
def test_behaviour::dynamicrobot_instantiation(instance):
    assert isinstance(instance, behaviour::DynamicRobot)

@given(instance=behaviour::DynamicRobot_strategy)
def test_behaviour::dynamicrobot_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=behaviour::DynamicRobot_strategy)
def test_behaviour::dynamicrobot_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=behaviour::BehaviourContainer_strategy)
@settings(max_examples=50)
def test_behaviour::behaviourcontainer_instantiation(instance):
    assert isinstance(instance, behaviour::BehaviourContainer)
