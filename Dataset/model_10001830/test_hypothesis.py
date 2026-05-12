import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Room,
    SessionType,
    Session,
    Serie,
    Event,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_room_has_name():
    assert hasattr(Room, "name")
    descriptor = None
    for klass in Room.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_room_has_id():
    assert hasattr(Room, "id")
    descriptor = None
    for klass in Room.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sessiontype_is_not_abstract():
    assert not inspect.isabstract(SessionType)


def test_sessiontype_constructor_exists():
    assert callable(SessionType.__init__)


def test_sessiontype_constructor_args():
    sig = inspect.signature(SessionType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_sessiontype_has_color():
    assert hasattr(SessionType, "color")
    descriptor = None
    for klass in SessionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_sessiontype_has_id():
    assert hasattr(SessionType, "id")
    descriptor = None
    for klass in SessionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sessiontype_has_name():
    assert hasattr(SessionType, "name")
    descriptor = None
    for klass in SessionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_session_is_not_abstract():
    assert not inspect.isabstract(Session)


def test_session_constructor_exists():
    assert callable(Session.__init__)


def test_session_constructor_args():
    sig = inspect.signature(Session.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "room" in params, "Missing parameter 'room'"
    assert "Events" in params, "Missing parameter 'Events'"
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_session_has_type():
    assert hasattr(Session, "type")
    descriptor = None
    for klass in Session.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_session_has_name():
    assert hasattr(Session, "name")
    descriptor = None
    for klass in Session.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_session_has_id():
    assert hasattr(Session, "id")
    descriptor = None
    for klass in Session.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_session_has_room():
    assert hasattr(Session, "room")
    descriptor = None
    for klass in Session.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_session_has_Events():
    assert hasattr(Session, "Events")
    descriptor = None
    for klass in Session.__mro__:
        if "Events" in klass.__dict__:
            descriptor = klass.__dict__["Events"]
            break
    assert isinstance(descriptor, property)

def test_session_has_start():
    assert hasattr(Session, "start")
    descriptor = None
    for klass in Session.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_session_has_end():
    assert hasattr(Session, "end")
    descriptor = None
    for klass in Session.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_serie_is_not_abstract():
    assert not inspect.isabstract(Serie)


def test_serie_constructor_exists():
    assert callable(Serie.__init__)


def test_serie_constructor_args():
    sig = inspect.signature(Serie.__init__)
    params = list(sig.parameters.keys())
    assert "Events" in params, "Missing parameter 'Events'"

def test_serie_has_Events():
    assert hasattr(Serie, "Events")
    descriptor = None
    for klass in Serie.__mro__:
        if "Events" in klass.__dict__:
            descriptor = klass.__dict__["Events"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "acronym" in params, "Missing parameter 'acronym'"

def test_event_has_attribute():
    assert hasattr(Event, "attribute")
    descriptor = None
    for klass in Event.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_event_has_id():
    assert hasattr(Event, "id")
    descriptor = None
    for klass in Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_event_has_name():
    assert hasattr(Event, "name")
    descriptor = None
    for klass in Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_event_has_edition():
    assert hasattr(Event, "edition")
    descriptor = None
    for klass in Event.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_event_has_acronym():
    assert hasattr(Event, "acronym")
    descriptor = None
    for klass in Event.__mro__:
        if "acronym" in klass.__dict__:
            descriptor = klass.__dict__["acronym"]
            break
    assert isinstance(descriptor, property)

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
Room_strategy = st.builds(
    Room,
    name=
        safe_text,
    id=
        st.integers()
)
SessionType_strategy = st.builds(
    SessionType,
    color=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
Session_strategy = st.builds(
    Session,
    type=
        st.none(),
    name=
        safe_text,
    id=
        st.integers(),
    room=
        st.none(),
    Events=
        st.none(),
    start=
        safe_text,
    end=
        safe_text
)
Serie_strategy = st.builds(
    Serie,
    Events=
        st.none()
)
Event_strategy = st.builds(
    Event,
    attribute=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text,
    edition=
        st.integers(),
    acronym=
        safe_text
)

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Room_strategy)
def test_room_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SessionType_strategy)
@settings(max_examples=50)
def test_sessiontype_instantiation(instance):
    assert isinstance(instance, SessionType)



@given(instance=SessionType_strategy)
def test_sessiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=SessionType_strategy)
def test_sessiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=SessionType_strategy)
def test_sessiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Session_strategy)
@settings(max_examples=50)
def test_session_instantiation(instance):
    assert isinstance(instance, Session)



@given(instance=Session_strategy)
def test_session_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Session_strategy)
def test_session_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Session_strategy)
def test_session_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Session_strategy)
def test_session_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=Session_strategy)
def test_session_Events_setter(instance):
    original = instance.Events
    instance.Events = original
    assert instance.Events == original



@given(instance=Session_strategy)
def test_session_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=Session_strategy)
def test_session_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=Serie_strategy)
@settings(max_examples=50)
def test_serie_instantiation(instance):
    assert isinstance(instance, Serie)



@given(instance=Serie_strategy)
def test_serie_Events_setter(instance):
    original = instance.Events
    instance.Events = original
    assert instance.Events == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_event_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Event_strategy)
def test_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Event_strategy)
def test_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Event_strategy)
def test_event_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original



@given(instance=Event_strategy)
def test_event_acronym_setter(instance):
    original = instance.acronym
    instance.acronym = original
    assert instance.acronym == original
