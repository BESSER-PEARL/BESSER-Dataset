import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rosmodel::Package,
    rosmodel::Field,
    rosmodel::State,
    rosmodel::ActionServer,
    rosmodel::ActionClient,
    rosmodel::ServiceServer,
    rosmodel::ServiceClient,
    rosmodel::Subscriber,
    rosmodel::Publisher,
    rosmodel::ActionMessage,
    rosmodel::ServiceType,
    rosmodel::Message,
    rosmodel::Event,
    rosmodel::Action,
    rosmodel::Transition,
    rosmodel::Topic,
    rosmodel::Node,
    Datatype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rosmodel::package_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Package)


def test_rosmodel::package_constructor_exists():
    assert callable(rosmodel::Package.__init__)


def test_rosmodel::package_constructor_args():
    sig = inspect.signature(rosmodel::Package.__init__)
    params = list(sig.parameters.keys())
    assert "depends" in params, "Missing parameter 'depends'"
    assert "description" in params, "Missing parameter 'description'"
    assert "author" in params, "Missing parameter 'author'"
    assert "author_email" in params, "Missing parameter 'author_email'"
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::package_has_depends():
    assert hasattr(rosmodel::Package, "depends")
    descriptor = None
    for klass in rosmodel::Package.__mro__:
        if "depends" in klass.__dict__:
            descriptor = klass.__dict__["depends"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::package_has_description():
    assert hasattr(rosmodel::Package, "description")
    descriptor = None
    for klass in rosmodel::Package.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::package_has_author():
    assert hasattr(rosmodel::Package, "author")
    descriptor = None
    for klass in rosmodel::Package.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::package_has_author_email():
    assert hasattr(rosmodel::Package, "author_email")
    descriptor = None
    for klass in rosmodel::Package.__mro__:
        if "author_email" in klass.__dict__:
            descriptor = klass.__dict__["author_email"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::package_has_name():
    assert hasattr(rosmodel::Package, "name")
    descriptor = None
    for klass in rosmodel::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::field_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Field)


def test_rosmodel::field_constructor_exists():
    assert callable(rosmodel::Field.__init__)


def test_rosmodel::field_constructor_args():
    sig = inspect.signature(rosmodel::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rosmodel::field_has_name():
    assert hasattr(rosmodel::Field, "name")
    descriptor = None
    for klass in rosmodel::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::field_has_type():
    assert hasattr(rosmodel::Field, "type")
    descriptor = None
    for klass in rosmodel::Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::state_is_not_abstract():
    assert not inspect.isabstract(rosmodel::State)


def test_rosmodel::state_constructor_exists():
    assert callable(rosmodel::State.__init__)


def test_rosmodel::state_constructor_args():
    sig = inspect.signature(rosmodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::state_has_name():
    assert hasattr(rosmodel::State, "name")
    descriptor = None
    for klass in rosmodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::actionserver_is_not_abstract():
    assert not inspect.isabstract(rosmodel::ActionServer)


def test_rosmodel::actionserver_constructor_exists():
    assert callable(rosmodel::ActionServer.__init__)


def test_rosmodel::actionserver_constructor_args():
    sig = inspect.signature(rosmodel::ActionServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::actionserver_has_name():
    assert hasattr(rosmodel::ActionServer, "name")
    descriptor = None
    for klass in rosmodel::ActionServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::actionclient_is_not_abstract():
    assert not inspect.isabstract(rosmodel::ActionClient)


def test_rosmodel::actionclient_constructor_exists():
    assert callable(rosmodel::ActionClient.__init__)


def test_rosmodel::actionclient_constructor_args():
    sig = inspect.signature(rosmodel::ActionClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::actionclient_has_name():
    assert hasattr(rosmodel::ActionClient, "name")
    descriptor = None
    for klass in rosmodel::ActionClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::serviceserver_is_not_abstract():
    assert not inspect.isabstract(rosmodel::ServiceServer)


def test_rosmodel::serviceserver_constructor_exists():
    assert callable(rosmodel::ServiceServer.__init__)


def test_rosmodel::serviceserver_constructor_args():
    sig = inspect.signature(rosmodel::ServiceServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::serviceserver_has_name():
    assert hasattr(rosmodel::ServiceServer, "name")
    descriptor = None
    for klass in rosmodel::ServiceServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::serviceclient_is_not_abstract():
    assert not inspect.isabstract(rosmodel::ServiceClient)


def test_rosmodel::serviceclient_constructor_exists():
    assert callable(rosmodel::ServiceClient.__init__)


def test_rosmodel::serviceclient_constructor_args():
    sig = inspect.signature(rosmodel::ServiceClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::serviceclient_has_name():
    assert hasattr(rosmodel::ServiceClient, "name")
    descriptor = None
    for klass in rosmodel::ServiceClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::subscriber_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Subscriber)


def test_rosmodel::subscriber_constructor_exists():
    assert callable(rosmodel::Subscriber.__init__)


def test_rosmodel::subscriber_constructor_args():
    sig = inspect.signature(rosmodel::Subscriber.__init__)
    params = list(sig.parameters.keys())
    assert "queue_size" in params, "Missing parameter 'queue_size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "msg" in params, "Missing parameter 'msg'"

def test_rosmodel::subscriber_has_queue_size():
    assert hasattr(rosmodel::Subscriber, "queue_size")
    descriptor = None
    for klass in rosmodel::Subscriber.__mro__:
        if "queue_size" in klass.__dict__:
            descriptor = klass.__dict__["queue_size"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::subscriber_has_name():
    assert hasattr(rosmodel::Subscriber, "name")
    descriptor = None
    for klass in rosmodel::Subscriber.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::subscriber_has_msg():
    assert hasattr(rosmodel::Subscriber, "msg")
    descriptor = None
    for klass in rosmodel::Subscriber.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::publisher_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Publisher)


def test_rosmodel::publisher_constructor_exists():
    assert callable(rosmodel::Publisher.__init__)


def test_rosmodel::publisher_constructor_args():
    sig = inspect.signature(rosmodel::Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "queue_size" in params, "Missing parameter 'queue_size'"
    assert "msg" in params, "Missing parameter 'msg'"

def test_rosmodel::publisher_has_name():
    assert hasattr(rosmodel::Publisher, "name")
    descriptor = None
    for klass in rosmodel::Publisher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::publisher_has_queue_size():
    assert hasattr(rosmodel::Publisher, "queue_size")
    descriptor = None
    for klass in rosmodel::Publisher.__mro__:
        if "queue_size" in klass.__dict__:
            descriptor = klass.__dict__["queue_size"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::publisher_has_msg():
    assert hasattr(rosmodel::Publisher, "msg")
    descriptor = None
    for klass in rosmodel::Publisher.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::actionmessage_is_not_abstract():
    assert not inspect.isabstract(rosmodel::ActionMessage)


def test_rosmodel::actionmessage_constructor_exists():
    assert callable(rosmodel::ActionMessage.__init__)


def test_rosmodel::actionmessage_constructor_args():
    sig = inspect.signature(rosmodel::ActionMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::actionmessage_has_name():
    assert hasattr(rosmodel::ActionMessage, "name")
    descriptor = None
    for klass in rosmodel::ActionMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::servicetype_is_not_abstract():
    assert not inspect.isabstract(rosmodel::ServiceType)


def test_rosmodel::servicetype_constructor_exists():
    assert callable(rosmodel::ServiceType.__init__)


def test_rosmodel::servicetype_constructor_args():
    sig = inspect.signature(rosmodel::ServiceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::servicetype_has_name():
    assert hasattr(rosmodel::ServiceType, "name")
    descriptor = None
    for klass in rosmodel::ServiceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::message_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Message)


def test_rosmodel::message_constructor_exists():
    assert callable(rosmodel::Message.__init__)


def test_rosmodel::message_constructor_args():
    sig = inspect.signature(rosmodel::Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::message_has_name():
    assert hasattr(rosmodel::Message, "name")
    descriptor = None
    for klass in rosmodel::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::event_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Event)


def test_rosmodel::event_constructor_exists():
    assert callable(rosmodel::Event.__init__)


def test_rosmodel::event_constructor_args():
    sig = inspect.signature(rosmodel::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::event_has_name():
    assert hasattr(rosmodel::Event, "name")
    descriptor = None
    for klass in rosmodel::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::action_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Action)


def test_rosmodel::action_constructor_exists():
    assert callable(rosmodel::Action.__init__)


def test_rosmodel::action_constructor_args():
    sig = inspect.signature(rosmodel::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::action_has_name():
    assert hasattr(rosmodel::Action, "name")
    descriptor = None
    for klass in rosmodel::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::transition_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Transition)


def test_rosmodel::transition_constructor_exists():
    assert callable(rosmodel::Transition.__init__)


def test_rosmodel::transition_constructor_args():
    sig = inspect.signature(rosmodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::transition_has_name():
    assert hasattr(rosmodel::Transition, "name")
    descriptor = None
    for klass in rosmodel::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::topic_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Topic)


def test_rosmodel::topic_constructor_exists():
    assert callable(rosmodel::Topic.__init__)


def test_rosmodel::topic_constructor_args():
    sig = inspect.signature(rosmodel::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rosmodel::topic_has_name():
    assert hasattr(rosmodel::Topic, "name")
    descriptor = None
    for klass in rosmodel::Topic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rosmodel::node_is_not_abstract():
    assert not inspect.isabstract(rosmodel::Node)


def test_rosmodel::node_constructor_exists():
    assert callable(rosmodel::Node.__init__)


def test_rosmodel::node_constructor_args():
    sig = inspect.signature(rosmodel::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_rosmodel::node_has_name():
    assert hasattr(rosmodel::Node, "name")
    descriptor = None
    for klass in rosmodel::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rosmodel::node_has_frequency():
    assert hasattr(rosmodel::Node, "frequency")
    descriptor = None
    for klass in rosmodel::Node.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)

def test_datatype_exists():
    # Check that the Enumeration exists
    assert Datatype is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Datatype]
    expected_literals = [
        "msg",
        "float32",
        "string",
        "int8",
        "int32",
        "int64",
        "float64",
        "int16",
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
rosmodel::Package_strategy = st.builds(
    rosmodel::Package,
    depends=
        safe_text,
    description=
        safe_text,
    author=
        safe_text,
    author_email=
        safe_text,
    name=
        safe_text
)
rosmodel::Field_strategy = st.builds(
    rosmodel::Field,
    name=
        safe_text,
    type=
        safe_text
)
rosmodel::State_strategy = st.builds(
    rosmodel::State,
    name=
        safe_text
)
rosmodel::ActionServer_strategy = st.builds(
    rosmodel::ActionServer,
    name=
        safe_text
)
rosmodel::ActionClient_strategy = st.builds(
    rosmodel::ActionClient,
    name=
        safe_text
)
rosmodel::ServiceServer_strategy = st.builds(
    rosmodel::ServiceServer,
    name=
        safe_text
)
rosmodel::ServiceClient_strategy = st.builds(
    rosmodel::ServiceClient,
    name=
        safe_text
)
rosmodel::Subscriber_strategy = st.builds(
    rosmodel::Subscriber,
    queue_size=
        st.integers(),
    name=
        safe_text,
    msg=
        safe_text
)
rosmodel::Publisher_strategy = st.builds(
    rosmodel::Publisher,
    name=
        safe_text,
    queue_size=
        st.integers(),
    msg=
        safe_text
)
rosmodel::ActionMessage_strategy = st.builds(
    rosmodel::ActionMessage,
    name=
        safe_text
)
rosmodel::ServiceType_strategy = st.builds(
    rosmodel::ServiceType,
    name=
        safe_text
)
rosmodel::Message_strategy = st.builds(
    rosmodel::Message,
    name=
        safe_text
)
rosmodel::Event_strategy = st.builds(
    rosmodel::Event,
    name=
        safe_text
)
rosmodel::Action_strategy = st.builds(
    rosmodel::Action,
    name=
        safe_text
)
rosmodel::Transition_strategy = st.builds(
    rosmodel::Transition,
    name=
        safe_text
)
rosmodel::Topic_strategy = st.builds(
    rosmodel::Topic,
    name=
        safe_text
)
rosmodel::Node_strategy = st.builds(
    rosmodel::Node,
    name=
        safe_text,
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=rosmodel::Package_strategy)
@settings(max_examples=50)
def test_rosmodel::package_instantiation(instance):
    assert isinstance(instance, rosmodel::Package)

@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_depends_type(instance):
    assert isinstance(instance.depends, str)


@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original

@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_author_email_type(instance):
    assert isinstance(instance.author_email, str)


@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_author_email_setter(instance):
    original = instance.author_email
    instance.author_email = original
    assert instance.author_email == original

@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Package_strategy)
def test_rosmodel::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Field_strategy)
@settings(max_examples=50)
def test_rosmodel::field_instantiation(instance):
    assert isinstance(instance, rosmodel::Field)

@given(instance=rosmodel::Field_strategy)
def test_rosmodel::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Field_strategy)
def test_rosmodel::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Field_strategy)
def test_rosmodel::field_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rosmodel::Field_strategy)
def test_rosmodel::field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rosmodel::State_strategy)
@settings(max_examples=50)
def test_rosmodel::state_instantiation(instance):
    assert isinstance(instance, rosmodel::State)

@given(instance=rosmodel::State_strategy)
def test_rosmodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::State_strategy)
def test_rosmodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::ActionServer_strategy)
@settings(max_examples=50)
def test_rosmodel::actionserver_instantiation(instance):
    assert isinstance(instance, rosmodel::ActionServer)

@given(instance=rosmodel::ActionServer_strategy)
def test_rosmodel::actionserver_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::ActionServer_strategy)
def test_rosmodel::actionserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::ActionClient_strategy)
@settings(max_examples=50)
def test_rosmodel::actionclient_instantiation(instance):
    assert isinstance(instance, rosmodel::ActionClient)

@given(instance=rosmodel::ActionClient_strategy)
def test_rosmodel::actionclient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::ActionClient_strategy)
def test_rosmodel::actionclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::ServiceServer_strategy)
@settings(max_examples=50)
def test_rosmodel::serviceserver_instantiation(instance):
    assert isinstance(instance, rosmodel::ServiceServer)

@given(instance=rosmodel::ServiceServer_strategy)
def test_rosmodel::serviceserver_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::ServiceServer_strategy)
def test_rosmodel::serviceserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::ServiceClient_strategy)
@settings(max_examples=50)
def test_rosmodel::serviceclient_instantiation(instance):
    assert isinstance(instance, rosmodel::ServiceClient)

@given(instance=rosmodel::ServiceClient_strategy)
def test_rosmodel::serviceclient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::ServiceClient_strategy)
def test_rosmodel::serviceclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Subscriber_strategy)
@settings(max_examples=50)
def test_rosmodel::subscriber_instantiation(instance):
    assert isinstance(instance, rosmodel::Subscriber)

@given(instance=rosmodel::Subscriber_strategy)
def test_rosmodel::subscriber_queue_size_type(instance):
    assert isinstance(instance.queue_size, int)


@given(instance=rosmodel::Subscriber_strategy)
def test_rosmodel::subscriber_queue_size_setter(instance):
    original = instance.queue_size
    instance.queue_size = original
    assert instance.queue_size == original

@given(instance=rosmodel::Subscriber_strategy)
def test_rosmodel::subscriber_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Subscriber_strategy)
def test_rosmodel::subscriber_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Subscriber_strategy)
def test_rosmodel::subscriber_msg_type(instance):
    assert isinstance(instance.msg, str)


@given(instance=rosmodel::Subscriber_strategy)
def test_rosmodel::subscriber_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original

@given(instance=rosmodel::Publisher_strategy)
@settings(max_examples=50)
def test_rosmodel::publisher_instantiation(instance):
    assert isinstance(instance, rosmodel::Publisher)

@given(instance=rosmodel::Publisher_strategy)
def test_rosmodel::publisher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Publisher_strategy)
def test_rosmodel::publisher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Publisher_strategy)
def test_rosmodel::publisher_queue_size_type(instance):
    assert isinstance(instance.queue_size, int)


@given(instance=rosmodel::Publisher_strategy)
def test_rosmodel::publisher_queue_size_setter(instance):
    original = instance.queue_size
    instance.queue_size = original
    assert instance.queue_size == original

@given(instance=rosmodel::Publisher_strategy)
def test_rosmodel::publisher_msg_type(instance):
    assert isinstance(instance.msg, str)


@given(instance=rosmodel::Publisher_strategy)
def test_rosmodel::publisher_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original

@given(instance=rosmodel::ActionMessage_strategy)
@settings(max_examples=50)
def test_rosmodel::actionmessage_instantiation(instance):
    assert isinstance(instance, rosmodel::ActionMessage)

@given(instance=rosmodel::ActionMessage_strategy)
def test_rosmodel::actionmessage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::ActionMessage_strategy)
def test_rosmodel::actionmessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::ServiceType_strategy)
@settings(max_examples=50)
def test_rosmodel::servicetype_instantiation(instance):
    assert isinstance(instance, rosmodel::ServiceType)

@given(instance=rosmodel::ServiceType_strategy)
def test_rosmodel::servicetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::ServiceType_strategy)
def test_rosmodel::servicetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Message_strategy)
@settings(max_examples=50)
def test_rosmodel::message_instantiation(instance):
    assert isinstance(instance, rosmodel::Message)

@given(instance=rosmodel::Message_strategy)
def test_rosmodel::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Message_strategy)
def test_rosmodel::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Event_strategy)
@settings(max_examples=50)
def test_rosmodel::event_instantiation(instance):
    assert isinstance(instance, rosmodel::Event)

@given(instance=rosmodel::Event_strategy)
def test_rosmodel::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Event_strategy)
def test_rosmodel::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Action_strategy)
@settings(max_examples=50)
def test_rosmodel::action_instantiation(instance):
    assert isinstance(instance, rosmodel::Action)

@given(instance=rosmodel::Action_strategy)
def test_rosmodel::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Action_strategy)
def test_rosmodel::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Transition_strategy)
@settings(max_examples=50)
def test_rosmodel::transition_instantiation(instance):
    assert isinstance(instance, rosmodel::Transition)

@given(instance=rosmodel::Transition_strategy)
def test_rosmodel::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Transition_strategy)
def test_rosmodel::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Topic_strategy)
@settings(max_examples=50)
def test_rosmodel::topic_instantiation(instance):
    assert isinstance(instance, rosmodel::Topic)

@given(instance=rosmodel::Topic_strategy)
def test_rosmodel::topic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Topic_strategy)
def test_rosmodel::topic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Node_strategy)
@settings(max_examples=50)
def test_rosmodel::node_instantiation(instance):
    assert isinstance(instance, rosmodel::Node)

@given(instance=rosmodel::Node_strategy)
def test_rosmodel::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rosmodel::Node_strategy)
def test_rosmodel::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rosmodel::Node_strategy)
def test_rosmodel::node_frequency_type(instance):
    assert isinstance(instance.frequency, float)


@given(instance=rosmodel::Node_strategy)
def test_rosmodel::node_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original
