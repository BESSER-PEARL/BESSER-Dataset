import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Participant,
    makingOf::conference::Person,
    conference::makingOf::Participant,
    conference::makingOf::Task,
    Day,
    conference::makingOf::Story,
    conference::Subject,
    Task,
    conference::makingOf::Day,
    Story,
    conference::Talk,
    conference::Location,
    conference::Day,
    conference::Person,
    conference::Track,
    conference::Conference,
    Attitude,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_participant_is_not_abstract():
    assert not inspect.isabstract(Participant)


def test_participant_constructor_exists():
    assert callable(Participant.__init__)


def test_participant_constructor_args():
    sig = inspect.signature(Participant.__init__)
    params = list(sig.parameters.keys())



def test_makingof::conference::person_is_not_abstract():
    assert not inspect.isabstract(makingOf::conference::Person)


def test_makingof::conference::person_constructor_exists():
    assert callable(makingOf::conference::Person.__init__)


def test_makingof::conference::person_constructor_args():
    sig = inspect.signature(makingOf::conference::Person.__init__)
    params = list(sig.parameters.keys())



def test_conference::makingof::participant_is_not_abstract():
    assert not inspect.isabstract(conference::makingOf::Participant)


def test_conference::makingof::participant_constructor_exists():
    assert callable(conference::makingOf::Participant.__init__)


def test_conference::makingof::participant_constructor_args():
    sig = inspect.signature(conference::makingOf::Participant.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "attitude" in params, "Missing parameter 'attitude'"

def test_conference::makingof::participant_has_age():
    assert hasattr(conference::makingOf::Participant, "age")
    descriptor = None
    for klass in conference::makingOf::Participant.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_conference::makingof::participant_has_attitude():
    assert hasattr(conference::makingOf::Participant, "attitude")
    descriptor = None
    for klass in conference::makingOf::Participant.__mro__:
        if "attitude" in klass.__dict__:
            descriptor = klass.__dict__["attitude"]
            break
    assert isinstance(descriptor, property)



def test_conference::makingof::task_is_not_abstract():
    assert not inspect.isabstract(conference::makingOf::Task)


def test_conference::makingof::task_constructor_exists():
    assert callable(conference::makingOf::Task.__init__)


def test_conference::makingof::task_constructor_args():
    sig = inspect.signature(conference::makingOf::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::makingof::task_has_name():
    assert hasattr(conference::makingOf::Task, "name")
    descriptor = None
    for klass in conference::makingOf::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_day_is_not_abstract():
    assert not inspect.isabstract(Day)


def test_day_constructor_exists():
    assert callable(Day.__init__)


def test_day_constructor_args():
    sig = inspect.signature(Day.__init__)
    params = list(sig.parameters.keys())



def test_conference::makingof::story_is_not_abstract():
    assert not inspect.isabstract(conference::makingOf::Story)


def test_conference::makingof::story_constructor_exists():
    assert callable(conference::makingOf::Story.__init__)


def test_conference::makingof::story_constructor_args():
    sig = inspect.signature(conference::makingOf::Story.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::makingof::story_has_name():
    assert hasattr(conference::makingOf::Story, "name")
    descriptor = None
    for klass in conference::makingOf::Story.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::subject_is_not_abstract():
    assert not inspect.isabstract(conference::Subject)


def test_conference::subject_constructor_exists():
    assert callable(conference::Subject.__init__)


def test_conference::subject_constructor_args():
    sig = inspect.signature(conference::Subject.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "isDone" in params, "Missing parameter 'isDone'"

def test_conference::subject_has_description():
    assert hasattr(conference::Subject, "description")
    descriptor = None
    for klass in conference::Subject.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_conference::subject_has_isDone():
    assert hasattr(conference::Subject, "isDone")
    descriptor = None
    for klass in conference::Subject.__mro__:
        if "isDone" in klass.__dict__:
            descriptor = klass.__dict__["isDone"]
            break
    assert isinstance(descriptor, property)



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_conference::makingof::day_is_not_abstract():
    assert not inspect.isabstract(conference::makingOf::Day)


def test_conference::makingof::day_constructor_exists():
    assert callable(conference::makingOf::Day.__init__)


def test_conference::makingof::day_constructor_args():
    sig = inspect.signature(conference::makingOf::Day.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::makingof::day_has_name():
    assert hasattr(conference::makingOf::Day, "name")
    descriptor = None
    for klass in conference::makingOf::Day.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_story_is_not_abstract():
    assert not inspect.isabstract(Story)


def test_story_constructor_exists():
    assert callable(Story.__init__)


def test_story_constructor_args():
    sig = inspect.signature(Story.__init__)
    params = list(sig.parameters.keys())



def test_conference::talk_is_not_abstract():
    assert not inspect.isabstract(conference::Talk)


def test_conference::talk_constructor_exists():
    assert callable(conference::Talk.__init__)


def test_conference::talk_constructor_args():
    sig = inspect.signature(conference::Talk.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "name" in params, "Missing parameter 'name'"
    assert "time" in params, "Missing parameter 'time'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_conference::talk_has_duration():
    assert hasattr(conference::Talk, "duration")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_conference::talk_has_name():
    assert hasattr(conference::Talk, "name")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_conference::talk_has_time():
    assert hasattr(conference::Talk, "time")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_conference::talk_has_abstract():
    assert hasattr(conference::Talk, "abstract")
    descriptor = None
    for klass in conference::Talk.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_conference::location_is_not_abstract():
    assert not inspect.isabstract(conference::Location)


def test_conference::location_constructor_exists():
    assert callable(conference::Location.__init__)


def test_conference::location_constructor_args():
    sig = inspect.signature(conference::Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::location_has_name():
    assert hasattr(conference::Location, "name")
    descriptor = None
    for klass in conference::Location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::day_is_not_abstract():
    assert not inspect.isabstract(conference::Day)


def test_conference::day_constructor_exists():
    assert callable(conference::Day.__init__)


def test_conference::day_constructor_args():
    sig = inspect.signature(conference::Day.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::day_has_name():
    assert hasattr(conference::Day, "name")
    descriptor = None
    for klass in conference::Day.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::person_is_not_abstract():
    assert not inspect.isabstract(conference::Person)


def test_conference::person_constructor_exists():
    assert callable(conference::Person.__init__)


def test_conference::person_constructor_args():
    sig = inspect.signature(conference::Person.__init__)
    params = list(sig.parameters.keys())
    assert "organisation" in params, "Missing parameter 'organisation'"
    assert "name" in params, "Missing parameter 'name'"

def test_conference::person_has_organisation():
    assert hasattr(conference::Person, "organisation")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "organisation" in klass.__dict__:
            descriptor = klass.__dict__["organisation"]
            break
    assert isinstance(descriptor, property)

def test_conference::person_has_name():
    assert hasattr(conference::Person, "name")
    descriptor = None
    for klass in conference::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::track_is_not_abstract():
    assert not inspect.isabstract(conference::Track)


def test_conference::track_constructor_exists():
    assert callable(conference::Track.__init__)


def test_conference::track_constructor_args():
    sig = inspect.signature(conference::Track.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::track_has_name():
    assert hasattr(conference::Track, "name")
    descriptor = None
    for klass in conference::Track.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conference::conference_is_not_abstract():
    assert not inspect.isabstract(conference::Conference)


def test_conference::conference_constructor_exists():
    assert callable(conference::Conference.__init__)


def test_conference::conference_constructor_args():
    sig = inspect.signature(conference::Conference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conference::conference_has_name():
    assert hasattr(conference::Conference, "name")
    descriptor = None
    for klass in conference::Conference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attitude_exists():
    # Check that the Enumeration exists
    assert Attitude is not None

def test_attitude_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Attitude]
    expected_literals = [
        "cool",
        "serious",
        "disgraceful",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Attitude"


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
Participant_strategy = st.builds(
    Participant,
)
makingOf::conference::Person_strategy = st.builds(
    makingOf::conference::Person,
)
conference::makingOf::Participant_strategy = st.builds(
    conference::makingOf::Participant,
    age=
        st.integers(),
    attitude=
        safe_text
)
conference::makingOf::Task_strategy = st.builds(
    conference::makingOf::Task,
    name=
        safe_text
)
Day_strategy = st.builds(
    Day,
)
conference::makingOf::Story_strategy = st.builds(
    conference::makingOf::Story,
    name=
        safe_text
)
conference::Subject_strategy = st.builds(
    conference::Subject,
    description=
        safe_text,
    isDone=
        st.booleans()
)
Task_strategy = st.builds(
    Task,
)
conference::makingOf::Day_strategy = st.builds(
    conference::makingOf::Day,
    name=
        safe_text
)
Story_strategy = st.builds(
    Story,
)
conference::Talk_strategy = st.builds(
    conference::Talk,
    duration=
        st.integers(),
    name=
        safe_text,
    time=
        safe_text,
    abstract=
        safe_text
)
conference::Location_strategy = st.builds(
    conference::Location,
    name=
        safe_text
)
conference::Day_strategy = st.builds(
    conference::Day,
    name=
        safe_text
)
conference::Person_strategy = st.builds(
    conference::Person,
    organisation=
        safe_text,
    name=
        safe_text
)
conference::Track_strategy = st.builds(
    conference::Track,
    name=
        safe_text
)
conference::Conference_strategy = st.builds(
    conference::Conference,
    name=
        safe_text
)

@given(instance=Participant_strategy)
@settings(max_examples=50)
def test_participant_instantiation(instance):
    assert isinstance(instance, Participant)

@given(instance=makingOf::conference::Person_strategy)
@settings(max_examples=50)
def test_makingof::conference::person_instantiation(instance):
    assert isinstance(instance, makingOf::conference::Person)

@given(instance=conference::makingOf::Participant_strategy)
@settings(max_examples=50)
def test_conference::makingof::participant_instantiation(instance):
    assert isinstance(instance, conference::makingOf::Participant)

@given(instance=conference::makingOf::Participant_strategy)
def test_conference::makingof::participant_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=conference::makingOf::Participant_strategy)
def test_conference::makingof::participant_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=conference::makingOf::Participant_strategy)
def test_conference::makingof::participant_attitude_type(instance):
    assert isinstance(instance.attitude, str)


@given(instance=conference::makingOf::Participant_strategy)
def test_conference::makingof::participant_attitude_setter(instance):
    original = instance.attitude
    instance.attitude = original
    assert instance.attitude == original

@given(instance=conference::makingOf::Task_strategy)
@settings(max_examples=50)
def test_conference::makingof::task_instantiation(instance):
    assert isinstance(instance, conference::makingOf::Task)

@given(instance=conference::makingOf::Task_strategy)
def test_conference::makingof::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::makingOf::Task_strategy)
def test_conference::makingof::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Day_strategy)
@settings(max_examples=50)
def test_day_instantiation(instance):
    assert isinstance(instance, Day)

@given(instance=conference::makingOf::Story_strategy)
@settings(max_examples=50)
def test_conference::makingof::story_instantiation(instance):
    assert isinstance(instance, conference::makingOf::Story)

@given(instance=conference::makingOf::Story_strategy)
def test_conference::makingof::story_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::makingOf::Story_strategy)
def test_conference::makingof::story_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Subject_strategy)
@settings(max_examples=50)
def test_conference::subject_instantiation(instance):
    assert isinstance(instance, conference::Subject)

@given(instance=conference::Subject_strategy)
def test_conference::subject_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=conference::Subject_strategy)
def test_conference::subject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=conference::Subject_strategy)
def test_conference::subject_isDone_type(instance):
    assert isinstance(instance.isDone, bool)


@given(instance=conference::Subject_strategy)
def test_conference::subject_isDone_setter(instance):
    original = instance.isDone
    instance.isDone = original
    assert instance.isDone == original

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=conference::makingOf::Day_strategy)
@settings(max_examples=50)
def test_conference::makingof::day_instantiation(instance):
    assert isinstance(instance, conference::makingOf::Day)

@given(instance=conference::makingOf::Day_strategy)
def test_conference::makingof::day_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::makingOf::Day_strategy)
def test_conference::makingof::day_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Story_strategy)
@settings(max_examples=50)
def test_story_instantiation(instance):
    assert isinstance(instance, Story)

@given(instance=conference::Talk_strategy)
@settings(max_examples=50)
def test_conference::talk_instantiation(instance):
    assert isinstance(instance, conference::Talk)

@given(instance=conference::Talk_strategy)
def test_conference::talk_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=conference::Talk_strategy)
def test_conference::talk_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=conference::Talk_strategy)
def test_conference::talk_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Talk_strategy)
def test_conference::talk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Talk_strategy)
def test_conference::talk_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=conference::Talk_strategy)
def test_conference::talk_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=conference::Talk_strategy)
def test_conference::talk_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=conference::Talk_strategy)
def test_conference::talk_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=conference::Location_strategy)
@settings(max_examples=50)
def test_conference::location_instantiation(instance):
    assert isinstance(instance, conference::Location)

@given(instance=conference::Location_strategy)
def test_conference::location_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Location_strategy)
def test_conference::location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Day_strategy)
@settings(max_examples=50)
def test_conference::day_instantiation(instance):
    assert isinstance(instance, conference::Day)

@given(instance=conference::Day_strategy)
def test_conference::day_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Day_strategy)
def test_conference::day_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Person_strategy)
@settings(max_examples=50)
def test_conference::person_instantiation(instance):
    assert isinstance(instance, conference::Person)

@given(instance=conference::Person_strategy)
def test_conference::person_organisation_type(instance):
    assert isinstance(instance.organisation, str)


@given(instance=conference::Person_strategy)
def test_conference::person_organisation_setter(instance):
    original = instance.organisation
    instance.organisation = original
    assert instance.organisation == original

@given(instance=conference::Person_strategy)
def test_conference::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Person_strategy)
def test_conference::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Track_strategy)
@settings(max_examples=50)
def test_conference::track_instantiation(instance):
    assert isinstance(instance, conference::Track)

@given(instance=conference::Track_strategy)
def test_conference::track_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Track_strategy)
def test_conference::track_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conference::Conference_strategy)
@settings(max_examples=50)
def test_conference::conference_instantiation(instance):
    assert isinstance(instance, conference::Conference)

@given(instance=conference::Conference_strategy)
def test_conference::conference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conference::Conference_strategy)
def test_conference::conference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
