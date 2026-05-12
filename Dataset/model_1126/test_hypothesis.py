import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rosmodel_Field,
    rosmodel_State,
    rosmodel_ActionServer,
    rosmodel_ActionClient,
    rosmodel_ServiceServer,
    rosmodel_ServiceClient,
    rosmodel_Subscriber,
    rosmodel_Publisher,
    rosmodel_ActionMessage,
    rosmodel_ServiceType,
    rosmodel_Message,
    rosmodel_Event,
    rosmodel_Action,
    rosmodel_Transition,
    rosmodel_Topic,
    rosmodel_Node,
    rosmodel_Package,
    Datatype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rosmodel_field_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Field)


def test_rosmodel_field_constructor_exists():
    assert callable(rosmodel_Field.__init__)


def test_rosmodel_field_constructor_args():
    sig = inspect.signature(rosmodel_Field.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_field_has_type():
    assert hasattr(rosmodel_Field, "type")
    descriptor = None
    for klass in rosmodel_Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_field_has_name():
    assert hasattr(rosmodel_Field, "name")
    descriptor = None
    for klass in rosmodel_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_state_is_not_abstract():
    assert not inspect.isabstract(rosmodel_State)


def test_rosmodel_state_constructor_exists():
    assert callable(rosmodel_State.__init__)


def test_rosmodel_state_constructor_args():
    sig = inspect.signature(rosmodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_state_has_name():
    assert hasattr(rosmodel_State, "name")
    descriptor = None
    for klass in rosmodel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_actionserver_is_not_abstract():
    assert not inspect.isabstract(rosmodel_ActionServer)


def test_rosmodel_actionserver_constructor_exists():
    assert callable(rosmodel_ActionServer.__init__)


def test_rosmodel_actionserver_constructor_args():
    sig = inspect.signature(rosmodel_ActionServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_actionserver_has_name():
    assert hasattr(rosmodel_ActionServer, "name")
    descriptor = None
    for klass in rosmodel_ActionServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_actionclient_is_not_abstract():
    assert not inspect.isabstract(rosmodel_ActionClient)


def test_rosmodel_actionclient_constructor_exists():
    assert callable(rosmodel_ActionClient.__init__)


def test_rosmodel_actionclient_constructor_args():
    sig = inspect.signature(rosmodel_ActionClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_actionclient_has_name():
    assert hasattr(rosmodel_ActionClient, "name")
    descriptor = None
    for klass in rosmodel_ActionClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_serviceserver_is_not_abstract():
    assert not inspect.isabstract(rosmodel_ServiceServer)


def test_rosmodel_serviceserver_constructor_exists():
    assert callable(rosmodel_ServiceServer.__init__)


def test_rosmodel_serviceserver_constructor_args():
    sig = inspect.signature(rosmodel_ServiceServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_serviceserver_has_name():
    assert hasattr(rosmodel_ServiceServer, "name")
    descriptor = None
    for klass in rosmodel_ServiceServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_serviceclient_is_not_abstract():
    assert not inspect.isabstract(rosmodel_ServiceClient)


def test_rosmodel_serviceclient_constructor_exists():
    assert callable(rosmodel_ServiceClient.__init__)


def test_rosmodel_serviceclient_constructor_args():
    sig = inspect.signature(rosmodel_ServiceClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_serviceclient_has_name():
    assert hasattr(rosmodel_ServiceClient, "name")
    descriptor = None
    for klass in rosmodel_ServiceClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_subscriber_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Subscriber)


def test_rosmodel_subscriber_constructor_exists():
    assert callable(rosmodel_Subscriber.__init__)


def test_rosmodel_subscriber_constructor_args():
    sig = inspect.signature(rosmodel_Subscriber.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "queue_size" in params, "Missing parameter 'queue_size'"
    assert "msg" in params, "Missing parameter 'msg'"

def test_rosmodel_subscriber_has_name():
    assert hasattr(rosmodel_Subscriber, "name")
    descriptor = None
    for klass in rosmodel_Subscriber.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_subscriber_has_queue_size():
    assert hasattr(rosmodel_Subscriber, "queue_size")
    descriptor = None
    for klass in rosmodel_Subscriber.__mro__:
        if "queue_size" in klass.__dict__:
            descriptor = klass.__dict__["queue_size"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_subscriber_has_msg():
    assert hasattr(rosmodel_Subscriber, "msg")
    descriptor = None
    for klass in rosmodel_Subscriber.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_publisher_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Publisher)


def test_rosmodel_publisher_constructor_exists():
    assert callable(rosmodel_Publisher.__init__)


def test_rosmodel_publisher_constructor_args():
    sig = inspect.signature(rosmodel_Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "msg" in params, "Missing parameter 'msg'"
    assert "queue_size" in params, "Missing parameter 'queue_size'"

def test_rosmodel_publisher_has_name():
    assert hasattr(rosmodel_Publisher, "name")
    descriptor = None
    for klass in rosmodel_Publisher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_publisher_has_msg():
    assert hasattr(rosmodel_Publisher, "msg")
    descriptor = None
    for klass in rosmodel_Publisher.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_publisher_has_queue_size():
    assert hasattr(rosmodel_Publisher, "queue_size")
    descriptor = None
    for klass in rosmodel_Publisher.__mro__:
        if "queue_size" in klass.__dict__:
            descriptor = klass.__dict__["queue_size"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_actionmessage_is_not_abstract():
    assert not inspect.isabstract(rosmodel_ActionMessage)


def test_rosmodel_actionmessage_constructor_exists():
    assert callable(rosmodel_ActionMessage.__init__)


def test_rosmodel_actionmessage_constructor_args():
    sig = inspect.signature(rosmodel_ActionMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_actionmessage_has_name():
    assert hasattr(rosmodel_ActionMessage, "name")
    descriptor = None
    for klass in rosmodel_ActionMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_servicetype_is_not_abstract():
    assert not inspect.isabstract(rosmodel_ServiceType)


def test_rosmodel_servicetype_constructor_exists():
    assert callable(rosmodel_ServiceType.__init__)


def test_rosmodel_servicetype_constructor_args():
    sig = inspect.signature(rosmodel_ServiceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_servicetype_has_name():
    assert hasattr(rosmodel_ServiceType, "name")
    descriptor = None
    for klass in rosmodel_ServiceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_message_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Message)


def test_rosmodel_message_constructor_exists():
    assert callable(rosmodel_Message.__init__)


def test_rosmodel_message_constructor_args():
    sig = inspect.signature(rosmodel_Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_message_has_name():
    assert hasattr(rosmodel_Message, "name")
    descriptor = None
    for klass in rosmodel_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_event_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Event)


def test_rosmodel_event_constructor_exists():
    assert callable(rosmodel_Event.__init__)


def test_rosmodel_event_constructor_args():
    sig = inspect.signature(rosmodel_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_event_has_name():
    assert hasattr(rosmodel_Event, "name")
    descriptor = None
    for klass in rosmodel_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_action_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Action)


def test_rosmodel_action_constructor_exists():
    assert callable(rosmodel_Action.__init__)


def test_rosmodel_action_constructor_args():
    sig = inspect.signature(rosmodel_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_action_has_name():
    assert hasattr(rosmodel_Action, "name")
    descriptor = None
    for klass in rosmodel_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_transition_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Transition)


def test_rosmodel_transition_constructor_exists():
    assert callable(rosmodel_Transition.__init__)


def test_rosmodel_transition_constructor_args():
    sig = inspect.signature(rosmodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_transition_has_name():
    assert hasattr(rosmodel_Transition, "name")
    descriptor = None
    for klass in rosmodel_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_topic_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Topic)


def test_rosmodel_topic_constructor_exists():
    assert callable(rosmodel_Topic.__init__)


def test_rosmodel_topic_constructor_args():
    sig = inspect.signature(rosmodel_Topic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_topic_has_name():
    assert hasattr(rosmodel_Topic, "name")
    descriptor = None
    for klass in rosmodel_Topic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_node_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Node)


def test_rosmodel_node_constructor_exists():
    assert callable(rosmodel_Node.__init__)


def test_rosmodel_node_constructor_args():
    sig = inspect.signature(rosmodel_Node.__init__)
    params = list(sig.parameters.keys())
    assert "frequency" in params, "Missing parameter 'frequency'"
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel_node_has_frequency():
    assert hasattr(rosmodel_Node, "frequency")
    descriptor = None
    for klass in rosmodel_Node.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_node_has_name():
    assert hasattr(rosmodel_Node, "name")
    descriptor = None
    for klass in rosmodel_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel_package_is_not_abstract():
    assert not inspect.isabstract(rosmodel_Package)


def test_rosmodel_package_constructor_exists():
    assert callable(rosmodel_Package.__init__)


def test_rosmodel_package_constructor_args():
    sig = inspect.signature(rosmodel_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "author_email" in params, "Missing parameter 'author_email'"
    assert "author" in params, "Missing parameter 'author'"
    assert "depends" in params, "Missing parameter 'depends'"
    assert "description" in params, "Missing parameter 'description'"

def test_rosmodel_package_has_name():
    assert hasattr(rosmodel_Package, "name")
    descriptor = None
    for klass in rosmodel_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_package_has_author_email():
    assert hasattr(rosmodel_Package, "author_email")
    descriptor = None
    for klass in rosmodel_Package.__mro__:
        if "author_email" in klass.__dict__:
            descriptor = klass.__dict__["author_email"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_package_has_author():
    assert hasattr(rosmodel_Package, "author")
    descriptor = None
    for klass in rosmodel_Package.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_package_has_depends():
    assert hasattr(rosmodel_Package, "depends")
    descriptor = None
    for klass in rosmodel_Package.__mro__:
        if "depends" in klass.__dict__:
            descriptor = klass.__dict__["depends"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel_package_has_description():
    assert hasattr(rosmodel_Package, "description")
    descriptor = None
    for klass in rosmodel_Package.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datatype_exists():
    # Check that the Enumeration exists
    assert Datatype is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Datatype]
    expected_literals = [
        "string",
        "float64",
        "msg",
        "int16",
        "int32",
        "int64",
        "float32",
        "int8",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Datatype"


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
rosmodel_Field_strategy = st.builds(
    rosmodel_Field,
    type=
        safe_text,
    name=
        safe_text
)
rosmodel_State_strategy = st.builds(
    rosmodel_State,
    name=
        safe_text
)
rosmodel_ActionServer_strategy = st.builds(
    rosmodel_ActionServer,
    name=
        safe_text
)
rosmodel_ActionClient_strategy = st.builds(
    rosmodel_ActionClient,
    name=
        safe_text
)
rosmodel_ServiceServer_strategy = st.builds(
    rosmodel_ServiceServer,
    name=
        safe_text
)
rosmodel_ServiceClient_strategy = st.builds(
    rosmodel_ServiceClient,
    name=
        safe_text
)
rosmodel_Subscriber_strategy = st.builds(
    rosmodel_Subscriber,
    name=
        safe_text,
    queue_size=
        st.integers(),
    msg=
        safe_text
)
rosmodel_Publisher_strategy = st.builds(
    rosmodel_Publisher,
    name=
        safe_text,
    msg=
        safe_text,
    queue_size=
        st.integers()
)
rosmodel_ActionMessage_strategy = st.builds(
    rosmodel_ActionMessage,
    name=
        safe_text
)
rosmodel_ServiceType_strategy = st.builds(
    rosmodel_ServiceType,
    name=
        safe_text
)
rosmodel_Message_strategy = st.builds(
    rosmodel_Message,
    name=
        safe_text
)
rosmodel_Event_strategy = st.builds(
    rosmodel_Event,
    name=
        safe_text
)
rosmodel_Action_strategy = st.builds(
    rosmodel_Action,
    name=
        safe_text
)
rosmodel_Transition_strategy = st.builds(
    rosmodel_Transition,
    name=
        safe_text
)
rosmodel_Topic_strategy = st.builds(
    rosmodel_Topic,
    name=
        safe_text
)
rosmodel_Node_strategy = st.builds(
    rosmodel_Node,
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
rosmodel_Package_strategy = st.builds(
    rosmodel_Package,
    name=
        safe_text,
    author_email=
        safe_text,
    author=
        safe_text,
    depends=
        safe_text,
    description=
        safe_text
)

@given(instance=rosmodel_Field_strategy)
@settings(max_examples=50)
def test_rosmodel_field_instantiation(instance):
    assert isinstance(instance, rosmodel_Field)



@given(instance=rosmodel_Field_strategy)
def test_rosmodel_field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rosmodel_Field_strategy)
def test_rosmodel_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_State_strategy)
@settings(max_examples=50)
def test_rosmodel_state_instantiation(instance):
    assert isinstance(instance, rosmodel_State)



@given(instance=rosmodel_State_strategy)
def test_rosmodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_ActionServer_strategy)
@settings(max_examples=50)
def test_rosmodel_actionserver_instantiation(instance):
    assert isinstance(instance, rosmodel_ActionServer)



@given(instance=rosmodel_ActionServer_strategy)
def test_rosmodel_actionserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_ActionClient_strategy)
@settings(max_examples=50)
def test_rosmodel_actionclient_instantiation(instance):
    assert isinstance(instance, rosmodel_ActionClient)



@given(instance=rosmodel_ActionClient_strategy)
def test_rosmodel_actionclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_ServiceServer_strategy)
@settings(max_examples=50)
def test_rosmodel_serviceserver_instantiation(instance):
    assert isinstance(instance, rosmodel_ServiceServer)



@given(instance=rosmodel_ServiceServer_strategy)
def test_rosmodel_serviceserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_ServiceClient_strategy)
@settings(max_examples=50)
def test_rosmodel_serviceclient_instantiation(instance):
    assert isinstance(instance, rosmodel_ServiceClient)



@given(instance=rosmodel_ServiceClient_strategy)
def test_rosmodel_serviceclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Subscriber_strategy)
@settings(max_examples=50)
def test_rosmodel_subscriber_instantiation(instance):
    assert isinstance(instance, rosmodel_Subscriber)



@given(instance=rosmodel_Subscriber_strategy)
def test_rosmodel_subscriber_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rosmodel_Subscriber_strategy)
def test_rosmodel_subscriber_queue_size_setter(instance):
    original = instance.queue_size
    instance.queue_size = original
    assert instance.queue_size == original



@given(instance=rosmodel_Subscriber_strategy)
def test_rosmodel_subscriber_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original

@given(instance=rosmodel_Publisher_strategy)
@settings(max_examples=50)
def test_rosmodel_publisher_instantiation(instance):
    assert isinstance(instance, rosmodel_Publisher)



@given(instance=rosmodel_Publisher_strategy)
def test_rosmodel_publisher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rosmodel_Publisher_strategy)
def test_rosmodel_publisher_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original



@given(instance=rosmodel_Publisher_strategy)
def test_rosmodel_publisher_queue_size_setter(instance):
    original = instance.queue_size
    instance.queue_size = original
    assert instance.queue_size == original

@given(instance=rosmodel_ActionMessage_strategy)
@settings(max_examples=50)
def test_rosmodel_actionmessage_instantiation(instance):
    assert isinstance(instance, rosmodel_ActionMessage)



@given(instance=rosmodel_ActionMessage_strategy)
def test_rosmodel_actionmessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_ServiceType_strategy)
@settings(max_examples=50)
def test_rosmodel_servicetype_instantiation(instance):
    assert isinstance(instance, rosmodel_ServiceType)



@given(instance=rosmodel_ServiceType_strategy)
def test_rosmodel_servicetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Message_strategy)
@settings(max_examples=50)
def test_rosmodel_message_instantiation(instance):
    assert isinstance(instance, rosmodel_Message)



@given(instance=rosmodel_Message_strategy)
def test_rosmodel_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Event_strategy)
@settings(max_examples=50)
def test_rosmodel_event_instantiation(instance):
    assert isinstance(instance, rosmodel_Event)



@given(instance=rosmodel_Event_strategy)
def test_rosmodel_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Action_strategy)
@settings(max_examples=50)
def test_rosmodel_action_instantiation(instance):
    assert isinstance(instance, rosmodel_Action)



@given(instance=rosmodel_Action_strategy)
def test_rosmodel_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Transition_strategy)
@settings(max_examples=50)
def test_rosmodel_transition_instantiation(instance):
    assert isinstance(instance, rosmodel_Transition)



@given(instance=rosmodel_Transition_strategy)
def test_rosmodel_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Topic_strategy)
@settings(max_examples=50)
def test_rosmodel_topic_instantiation(instance):
    assert isinstance(instance, rosmodel_Topic)



@given(instance=rosmodel_Topic_strategy)
def test_rosmodel_topic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Node_strategy)
@settings(max_examples=50)
def test_rosmodel_node_instantiation(instance):
    assert isinstance(instance, rosmodel_Node)



@given(instance=rosmodel_Node_strategy)
def test_rosmodel_node_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original



@given(instance=rosmodel_Node_strategy)
def test_rosmodel_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel_Package_strategy)
@settings(max_examples=50)
def test_rosmodel_package_instantiation(instance):
    assert isinstance(instance, rosmodel_Package)



@given(instance=rosmodel_Package_strategy)
def test_rosmodel_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rosmodel_Package_strategy)
def test_rosmodel_package_author_email_setter(instance):
    original = instance.author_email
    instance.author_email = original
    assert instance.author_email == original



@given(instance=rosmodel_Package_strategy)
def test_rosmodel_package_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=rosmodel_Package_strategy)
def test_rosmodel_package_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original



@given(instance=rosmodel_Package_strategy)
def test_rosmodel_package_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
