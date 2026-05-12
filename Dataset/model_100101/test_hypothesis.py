import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    conference::Room,
    conference::Person,
    conference::Conference,
    conference::Site,
    conference::Topic,
    conference::Talk,
    TALK_TYPE,
    GENDER,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conference::room_is_not_abstract():
    assert not inspect.isabstract(conference::Room)


def test_conference::room_constructor_exists():
    assert callable(conference::Room.__init__)


def test_conference::room_constructor_args():
    sig = inspect.signature(conference::Room.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_conference::room_has_name():
    assert hasattr(conference::Room, "name")
    descriptor = None
    for klass in conference::Room.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_conference::room_has_capacity():
    assert hasattr(conference::Room, "capacity")
    descriptor = None
    for klass in conference::Room.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_conference::person_is_not_abstract():
    assert not inspect.isabstract(conference::Person)


def test_conference::person_constructor_exists():
    assert callable(conference::Person.__init__)


def test_conference::person_constructor_args():
    sig = inspect.signature(conference::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "eclipseCommiter" in params, "Missing parameter 'eclipseCommiter'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "isRegistered" in params, "Missing parameter 'isRegistered'"

def test_conference::person_has_age():
    assert hasattr(conference::Person, "age")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_conference::person_has_firstname():
    assert hasattr(conference::Person, "firstname")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_conference::person_has_eclipseCommiter():
    assert hasattr(conference::Person, "eclipseCommiter")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "eclipseCommiter" in klass.__dict__:
            descriptor = klass.__dict__["eclipseCommiter"]
            break
    assert isinstance(descriptor, property)

def test_conference::person_has_lastname():
    assert hasattr(conference::Person, "lastname")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_conference::person_has_gender():
    assert hasattr(conference::Person, "gender")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_conference::person_has_isRegistered():
    assert hasattr(conference::Person, "isRegistered")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "isRegistered" in klass.__dict__:
            descriptor = klass.__dict__["isRegistered"]
            break
    assert isinstance(descriptor, property)



def test_conference::conference_is_not_abstract():
    assert not inspect.isabstract(conference::Conference)


def test_conference::conference_constructor_exists():
    assert callable(conference::Conference.__init__)


def test_conference::conference_constructor_args():
    sig = inspect.signature(conference::Conference.__init__)
    params = list(sig.parameters.keys())
    assert "overview" in params, "Missing parameter 'overview'"
    assert "place" in params, "Missing parameter 'place'"
    assert "name" in params, "Missing parameter 'name'"

def test_conference::conference_has_overview():
    assert hasattr(conference::Conference, "overview")
    descriptor = None
    for klass in conference::Conference.__mro__:
        if "overview" in klass.__dict__:
            descriptor = klass.__dict__["overview"]
            break
    assert isinstance(descriptor, property)

def test_conference::conference_has_place():
    assert hasattr(conference::Conference, "place")
    descriptor = None
    for klass in conference::Conference.__mro__:
        if "place" in klass.__dict__:
            descriptor = klass.__dict__["place"]
            break
    assert isinstance(descriptor, property)

def test_conference::conference_has_name():
    assert hasattr(conference::Conference, "name")
    descriptor = None
    for klass in conference::Conference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::site_is_not_abstract():
    assert not inspect.isabstract(conference::Site)


def test_conference::site_constructor_exists():
    assert callable(conference::Site.__init__)


def test_conference::site_constructor_args():
    sig = inspect.signature(conference::Site.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"

def test_conference::site_has_documentation():
    assert hasattr(conference::Site, "documentation")
    descriptor = None
    for klass in conference::Site.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_conference::site_has_name():
    assert hasattr(conference::Site, "name")
    descriptor = None
    for klass in conference::Site.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::topic_is_not_abstract():
    assert not inspect.isabstract(conference::Topic)


def test_conference::topic_constructor_exists():
    assert callable(conference::Topic.__init__)


def test_conference::topic_constructor_args():
    sig = inspect.signature(conference::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "references" in params, "Missing parameter 'references'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "description" in params, "Missing parameter 'description'"

def test_conference::topic_has_references():
    assert hasattr(conference::Topic, "references")
    descriptor = None
    for klass in conference::Topic.__mro__:
        if "references" in klass.__dict__:
            descriptor = klass.__dict__["references"]
            break
    assert isinstance(descriptor, property)

def test_conference::topic_has_documentation():
    assert hasattr(conference::Topic, "documentation")
    descriptor = None
    for klass in conference::Topic.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_conference::topic_has_description():
    assert hasattr(conference::Topic, "description")
    descriptor = None
    for klass in conference::Topic.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_conference::talk_is_not_abstract():
    assert not inspect.isabstract(conference::Talk)


def test_conference::talk_constructor_exists():
    assert callable(conference::Talk.__init__)


def test_conference::talk_constructor_args():
    sig = inspect.signature(conference::Talk.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "type" in params, "Missing parameter 'type'"

def test_conference::talk_has_title():
    assert hasattr(conference::Talk, "title")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_conference::talk_has_documentation():
    assert hasattr(conference::Talk, "documentation")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_conference::talk_has_type():
    assert hasattr(conference::Talk, "type")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_talk_type_exists():
    # Check that the Enumeration exists
    assert TALK_TYPE is not None

def test_talk_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TALK_TYPE]
    expected_literals = [
        "CONFERENCE",
        "WORKSHOP",
        "DEMONSTRATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TALK_TYPE"

def test_gender_exists():
    # Check that the Enumeration exists
    assert GENDER is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GENDER]
    expected_literals = [
        "MALE",
        "FEMALE",
        "UNKNOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GENDER"


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
conference::Room_strategy = st.builds(
    conference::Room,
    name=
        safe_text,
    capacity=
        st.integers()
)
conference::Person_strategy = st.builds(
    conference::Person,
    age=
        st.integers(),
    firstname=
        safe_text,
    eclipseCommiter=
        st.booleans(),
    lastname=
        safe_text,
    gender=
        safe_text,
    isRegistered=
        st.booleans()
)
conference::Conference_strategy = st.builds(
    conference::Conference,
    overview=
        safe_text,
    place=
        safe_text,
    name=
        safe_text
)
conference::Site_strategy = st.builds(
    conference::Site,
    documentation=
        safe_text,
    name=
        safe_text
)
conference::Topic_strategy = st.builds(
    conference::Topic,
    references=
        safe_text,
    documentation=
        safe_text,
    description=
        safe_text
)
conference::Talk_strategy = st.builds(
    conference::Talk,
    title=
        safe_text,
    documentation=
        safe_text,
    type=
        safe_text
)

@given(instance=conference::Room_strategy)
@settings(max_examples=50)
def test_conference::room_instantiation(instance):
    assert isinstance(instance, conference::Room)

@given(instance=conference::Room_strategy)
def test_conference::room_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Room_strategy)
def test_conference::room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Room_strategy)
def test_conference::room_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=conference::Room_strategy)
def test_conference::room_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=conference::Person_strategy)
@settings(max_examples=50)
def test_conference::person_instantiation(instance):
    assert isinstance(instance, conference::Person)

@given(instance=conference::Person_strategy)
def test_conference::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=conference::Person_strategy)
def test_conference::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=conference::Person_strategy)
def test_conference::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=conference::Person_strategy)
def test_conference::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=conference::Person_strategy)
def test_conference::person_eclipseCommiter_type(instance):
    assert isinstance(instance.eclipseCommiter, bool)


@given(instance=conference::Person_strategy)
def test_conference::person_eclipseCommiter_setter(instance):
    original = instance.eclipseCommiter
    instance.eclipseCommiter = original
    assert instance.eclipseCommiter == original

@given(instance=conference::Person_strategy)
def test_conference::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=conference::Person_strategy)
def test_conference::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=conference::Person_strategy)
def test_conference::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=conference::Person_strategy)
def test_conference::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=conference::Person_strategy)
def test_conference::person_isRegistered_type(instance):
    assert isinstance(instance.isRegistered, bool)


@given(instance=conference::Person_strategy)
def test_conference::person_isRegistered_setter(instance):
    original = instance.isRegistered
    instance.isRegistered = original
    assert instance.isRegistered == original

@given(instance=conference::Conference_strategy)
@settings(max_examples=50)
def test_conference::conference_instantiation(instance):
    assert isinstance(instance, conference::Conference)

@given(instance=conference::Conference_strategy)
def test_conference::conference_overview_type(instance):
    assert isinstance(instance.overview, str)


@given(instance=conference::Conference_strategy)
def test_conference::conference_overview_setter(instance):
    original = instance.overview
    instance.overview = original
    assert instance.overview == original

@given(instance=conference::Conference_strategy)
def test_conference::conference_place_type(instance):
    assert isinstance(instance.place, str)


@given(instance=conference::Conference_strategy)
def test_conference::conference_place_setter(instance):
    original = instance.place
    instance.place = original
    assert instance.place == original

@given(instance=conference::Conference_strategy)
def test_conference::conference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Conference_strategy)
def test_conference::conference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Site_strategy)
@settings(max_examples=50)
def test_conference::site_instantiation(instance):
    assert isinstance(instance, conference::Site)

@given(instance=conference::Site_strategy)
def test_conference::site_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=conference::Site_strategy)
def test_conference::site_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=conference::Site_strategy)
def test_conference::site_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Site_strategy)
def test_conference::site_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Topic_strategy)
@settings(max_examples=50)
def test_conference::topic_instantiation(instance):
    assert isinstance(instance, conference::Topic)

@given(instance=conference::Topic_strategy)
def test_conference::topic_references_type(instance):
    assert isinstance(instance.references, str)


@given(instance=conference::Topic_strategy)
def test_conference::topic_references_setter(instance):
    original = instance.references
    instance.references = original
    assert instance.references == original

@given(instance=conference::Topic_strategy)
def test_conference::topic_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=conference::Topic_strategy)
def test_conference::topic_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=conference::Topic_strategy)
def test_conference::topic_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=conference::Topic_strategy)
def test_conference::topic_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=conference::Talk_strategy)
@settings(max_examples=50)
def test_conference::talk_instantiation(instance):
    assert isinstance(instance, conference::Talk)

@given(instance=conference::Talk_strategy)
def test_conference::talk_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=conference::Talk_strategy)
def test_conference::talk_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=conference::Talk_strategy)
def test_conference::talk_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=conference::Talk_strategy)
def test_conference::talk_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=conference::Talk_strategy)
def test_conference::talk_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=conference::Talk_strategy)
def test_conference::talk_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
