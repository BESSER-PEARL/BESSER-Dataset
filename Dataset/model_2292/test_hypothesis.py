import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    universityextended::administration::Event,
    universityextended::administration::Time,
    universityextended::administration::Room,
    Assistant,
    Professor,
    Event,
    universityextended::administration::Tutorial,
    universityextended::administration::Lecture,
    Student,
    universityextended::connection::Visits,
    universityextended::people::Person,
    Room,
    Time,
    Course,
    Visits,
    Person,
    universityextended::people::Student,
    universityextended::people::Professor,
    universityextended::University,
    universityextended::administration::Course,
    Tutorial,
    universityextended::people::Assistant,
    Lecture,
    SalaryRank,
    Motivation,
    Building,
    DayOfWeek,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_universityextended::administration::event_is_not_abstract():
    assert not inspect.isabstract(universityextended::administration::Event)


def test_universityextended::administration::event_constructor_exists():
    assert callable(universityextended::administration::Event.__init__)


def test_universityextended::administration::event_constructor_args():
    sig = inspect.signature(universityextended::administration::Event.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_universityextended::administration::event_has_title():
    assert hasattr(universityextended::administration::Event, "title")
    descriptor = None
    for klass in universityextended::administration::Event.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_universityextended::administration::time_is_not_abstract():
    assert not inspect.isabstract(universityextended::administration::Time)


def test_universityextended::administration::time_constructor_exists():
    assert callable(universityextended::administration::Time.__init__)


def test_universityextended::administration::time_constructor_args():
    sig = inspect.signature(universityextended::administration::Time.__init__)
    params = list(sig.parameters.keys())
    assert "endHour" in params, "Missing parameter 'endHour'"
    assert "startHour" in params, "Missing parameter 'startHour'"
    assert "day" in params, "Missing parameter 'day'"

def test_universityextended::administration::time_has_endHour():
    assert hasattr(universityextended::administration::Time, "endHour")
    descriptor = None
    for klass in universityextended::administration::Time.__mro__:
        if "endHour" in klass.__dict__:
            descriptor = klass.__dict__["endHour"]
            break
    assert isinstance(descriptor, property)

def test_universityextended::administration::time_has_startHour():
    assert hasattr(universityextended::administration::Time, "startHour")
    descriptor = None
    for klass in universityextended::administration::Time.__mro__:
        if "startHour" in klass.__dict__:
            descriptor = klass.__dict__["startHour"]
            break
    assert isinstance(descriptor, property)

def test_universityextended::administration::time_has_day():
    assert hasattr(universityextended::administration::Time, "day")
    descriptor = None
    for klass in universityextended::administration::Time.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)



def test_universityextended::administration::room_is_not_abstract():
    assert not inspect.isabstract(universityextended::administration::Room)


def test_universityextended::administration::room_constructor_exists():
    assert callable(universityextended::administration::Room.__init__)


def test_universityextended::administration::room_constructor_args():
    sig = inspect.signature(universityextended::administration::Room.__init__)
    params = list(sig.parameters.keys())
    assert "floor" in params, "Missing parameter 'floor'"
    assert "roomnumber" in params, "Missing parameter 'roomnumber'"
    assert "building" in params, "Missing parameter 'building'"

def test_universityextended::administration::room_has_floor():
    assert hasattr(universityextended::administration::Room, "floor")
    descriptor = None
    for klass in universityextended::administration::Room.__mro__:
        if "floor" in klass.__dict__:
            descriptor = klass.__dict__["floor"]
            break
    assert isinstance(descriptor, property)

def test_universityextended::administration::room_has_roomnumber():
    assert hasattr(universityextended::administration::Room, "roomnumber")
    descriptor = None
    for klass in universityextended::administration::Room.__mro__:
        if "roomnumber" in klass.__dict__:
            descriptor = klass.__dict__["roomnumber"]
            break
    assert isinstance(descriptor, property)

def test_universityextended::administration::room_has_building():
    assert hasattr(universityextended::administration::Room, "building")
    descriptor = None
    for klass in universityextended::administration::Room.__mro__:
        if "building" in klass.__dict__:
            descriptor = klass.__dict__["building"]
            break
    assert isinstance(descriptor, property)



def test_assistant_is_not_abstract():
    assert not inspect.isabstract(Assistant)


def test_assistant_constructor_exists():
    assert callable(Assistant.__init__)


def test_assistant_constructor_args():
    sig = inspect.signature(Assistant.__init__)
    params = list(sig.parameters.keys())



def test_professor_is_not_abstract():
    assert not inspect.isabstract(Professor)


def test_professor_constructor_exists():
    assert callable(Professor.__init__)


def test_professor_constructor_args():
    sig = inspect.signature(Professor.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_universityextended::administration::tutorial_is_not_abstract():
    assert not inspect.isabstract(universityextended::administration::Tutorial)


def test_universityextended::administration::tutorial_constructor_exists():
    assert callable(universityextended::administration::Tutorial.__init__)


def test_universityextended::administration::tutorial_constructor_args():
    sig = inspect.signature(universityextended::administration::Tutorial.__init__)
    params = list(sig.parameters.keys())



def test_universityextended::administration::lecture_is_not_abstract():
    assert not inspect.isabstract(universityextended::administration::Lecture)


def test_universityextended::administration::lecture_constructor_exists():
    assert callable(universityextended::administration::Lecture.__init__)


def test_universityextended::administration::lecture_constructor_args():
    sig = inspect.signature(universityextended::administration::Lecture.__init__)
    params = list(sig.parameters.keys())
    assert "captions" in params, "Missing parameter 'captions'"

def test_universityextended::administration::lecture_has_captions():
    assert hasattr(universityextended::administration::Lecture, "captions")
    descriptor = None
    for klass in universityextended::administration::Lecture.__mro__:
        if "captions" in klass.__dict__:
            descriptor = klass.__dict__["captions"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_universityextended::connection::visits_is_not_abstract():
    assert not inspect.isabstract(universityextended::connection::Visits)


def test_universityextended::connection::visits_constructor_exists():
    assert callable(universityextended::connection::Visits.__init__)


def test_universityextended::connection::visits_constructor_args():
    sig = inspect.signature(universityextended::connection::Visits.__init__)
    params = list(sig.parameters.keys())
    assert "motivation" in params, "Missing parameter 'motivation'"

def test_universityextended::connection::visits_has_motivation():
    assert hasattr(universityextended::connection::Visits, "motivation")
    descriptor = None
    for klass in universityextended::connection::Visits.__mro__:
        if "motivation" in klass.__dict__:
            descriptor = klass.__dict__["motivation"]
            break
    assert isinstance(descriptor, property)



def test_universityextended::people::person_is_not_abstract():
    assert not inspect.isabstract(universityextended::people::Person)


def test_universityextended::people::person_constructor_exists():
    assert callable(universityextended::people::Person.__init__)


def test_universityextended::people::person_constructor_args():
    sig = inspect.signature(universityextended::people::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_universityextended::people::person_has_name():
    assert hasattr(universityextended::people::Person, "name")
    descriptor = None
    for klass in universityextended::people::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())



def test_time_is_not_abstract():
    assert not inspect.isabstract(Time)


def test_time_constructor_exists():
    assert callable(Time.__init__)


def test_time_constructor_args():
    sig = inspect.signature(Time.__init__)
    params = list(sig.parameters.keys())



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())



def test_visits_is_not_abstract():
    assert not inspect.isabstract(Visits)


def test_visits_constructor_exists():
    assert callable(Visits.__init__)


def test_visits_constructor_args():
    sig = inspect.signature(Visits.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_universityextended::people::student_is_not_abstract():
    assert not inspect.isabstract(universityextended::people::Student)


def test_universityextended::people::student_constructor_exists():
    assert callable(universityextended::people::Student.__init__)


def test_universityextended::people::student_constructor_args():
    sig = inspect.signature(universityextended::people::Student.__init__)
    params = list(sig.parameters.keys())
    assert "matriculationnumber" in params, "Missing parameter 'matriculationnumber'"

def test_universityextended::people::student_has_matriculationnumber():
    assert hasattr(universityextended::people::Student, "matriculationnumber")
    descriptor = None
    for klass in universityextended::people::Student.__mro__:
        if "matriculationnumber" in klass.__dict__:
            descriptor = klass.__dict__["matriculationnumber"]
            break
    assert isinstance(descriptor, property)



def test_universityextended::people::professor_is_not_abstract():
    assert not inspect.isabstract(universityextended::people::Professor)


def test_universityextended::people::professor_constructor_exists():
    assert callable(universityextended::people::Professor.__init__)


def test_universityextended::people::professor_constructor_args():
    sig = inspect.signature(universityextended::people::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"

def test_universityextended::people::professor_has_rank():
    assert hasattr(universityextended::people::Professor, "rank")
    descriptor = None
    for klass in universityextended::people::Professor.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_universityextended::university_is_not_abstract():
    assert not inspect.isabstract(universityextended::University)


def test_universityextended::university_constructor_exists():
    assert callable(universityextended::University.__init__)


def test_universityextended::university_constructor_args():
    sig = inspect.signature(universityextended::University.__init__)
    params = list(sig.parameters.keys())



def test_universityextended::administration::course_is_not_abstract():
    assert not inspect.isabstract(universityextended::administration::Course)


def test_universityextended::administration::course_constructor_exists():
    assert callable(universityextended::administration::Course.__init__)


def test_universityextended::administration::course_constructor_args():
    sig = inspect.signature(universityextended::administration::Course.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "endOfCourse" in params, "Missing parameter 'endOfCourse'"
    assert "startOfCourse" in params, "Missing parameter 'startOfCourse'"

def test_universityextended::administration::course_has_title():
    assert hasattr(universityextended::administration::Course, "title")
    descriptor = None
    for klass in universityextended::administration::Course.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_universityextended::administration::course_has_endOfCourse():
    assert hasattr(universityextended::administration::Course, "endOfCourse")
    descriptor = None
    for klass in universityextended::administration::Course.__mro__:
        if "endOfCourse" in klass.__dict__:
            descriptor = klass.__dict__["endOfCourse"]
            break
    assert isinstance(descriptor, property)

def test_universityextended::administration::course_has_startOfCourse():
    assert hasattr(universityextended::administration::Course, "startOfCourse")
    descriptor = None
    for klass in universityextended::administration::Course.__mro__:
        if "startOfCourse" in klass.__dict__:
            descriptor = klass.__dict__["startOfCourse"]
            break
    assert isinstance(descriptor, property)



def test_tutorial_is_not_abstract():
    assert not inspect.isabstract(Tutorial)


def test_tutorial_constructor_exists():
    assert callable(Tutorial.__init__)


def test_tutorial_constructor_args():
    sig = inspect.signature(Tutorial.__init__)
    params = list(sig.parameters.keys())



def test_universityextended::people::assistant_is_not_abstract():
    assert not inspect.isabstract(universityextended::people::Assistant)


def test_universityextended::people::assistant_constructor_exists():
    assert callable(universityextended::people::Assistant.__init__)


def test_universityextended::people::assistant_constructor_args():
    sig = inspect.signature(universityextended::people::Assistant.__init__)
    params = list(sig.parameters.keys())
    assert "isDoctoralCandidate" in params, "Missing parameter 'isDoctoralCandidate'"

def test_universityextended::people::assistant_has_isDoctoralCandidate():
    assert hasattr(universityextended::people::Assistant, "isDoctoralCandidate")
    descriptor = None
    for klass in universityextended::people::Assistant.__mro__:
        if "isDoctoralCandidate" in klass.__dict__:
            descriptor = klass.__dict__["isDoctoralCandidate"]
            break
    assert isinstance(descriptor, property)



def test_lecture_is_not_abstract():
    assert not inspect.isabstract(Lecture)


def test_lecture_constructor_exists():
    assert callable(Lecture.__init__)


def test_lecture_constructor_args():
    sig = inspect.signature(Lecture.__init__)
    params = list(sig.parameters.keys())

def test_salaryrank_exists():
    # Check that the Enumeration exists
    assert SalaryRank is not None

def test_salaryrank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SalaryRank]
    expected_literals = [
        "W2",
        "W1",
        "W3",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SalaryRank"

def test_motivation_exists():
    # Check that the Enumeration exists
    assert Motivation is not None

def test_motivation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Motivation]
    expected_literals = [
        "HIGH_INTEREST",
        "LOW_INTEREST",
        "AVERAGE_INTEREST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Motivation"

def test_building_exists():
    # Check that the Enumeration exists
    assert Building is not None

def test_building_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Building]
    expected_literals = [
        "D",
        "C",
        "H",
        "B",
        "G",
        "F",
        "A",
        "E",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Building"

def test_dayofweek_exists():
    # Check that the Enumeration exists
    assert DayOfWeek is not None

def test_dayofweek_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DayOfWeek]
    expected_literals = [
        "Thursday",
        "Wednesday",
        "Friday",
        "Monday",
        "Tuesday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DayOfWeek"


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
universityextended::administration::Event_strategy = st.builds(
    universityextended::administration::Event,
    title=
        safe_text
)
universityextended::administration::Time_strategy = st.builds(
    universityextended::administration::Time,
    endHour=
        st.integers(),
    startHour=
        st.integers(),
    day=
        safe_text
)
universityextended::administration::Room_strategy = st.builds(
    universityextended::administration::Room,
    floor=
        st.integers(),
    roomnumber=
        st.integers(),
    building=
        safe_text
)
Assistant_strategy = st.builds(
    Assistant,
)
Professor_strategy = st.builds(
    Professor,
)
Event_strategy = st.builds(
    Event,
)
universityextended::administration::Tutorial_strategy = st.builds(
    universityextended::administration::Tutorial,
)
universityextended::administration::Lecture_strategy = st.builds(
    universityextended::administration::Lecture,
    captions=
        safe_text
)
Student_strategy = st.builds(
    Student,
)
universityextended::connection::Visits_strategy = st.builds(
    universityextended::connection::Visits,
    motivation=
        safe_text
)
universityextended::people::Person_strategy = st.builds(
    universityextended::people::Person,
    name=
        safe_text
)
Room_strategy = st.builds(
    Room,
)
Time_strategy = st.builds(
    Time,
)
Course_strategy = st.builds(
    Course,
)
Visits_strategy = st.builds(
    Visits,
)
Person_strategy = st.builds(
    Person,
)
universityextended::people::Student_strategy = st.builds(
    universityextended::people::Student,
    matriculationnumber=
        safe_text
)
universityextended::people::Professor_strategy = st.builds(
    universityextended::people::Professor,
    rank=
        safe_text
)
universityextended::University_strategy = st.builds(
    universityextended::University,
)
universityextended::administration::Course_strategy = st.builds(
    universityextended::administration::Course,
    title=
        safe_text,
    endOfCourse=
        st.dates(),
    startOfCourse=
        st.dates()
)
Tutorial_strategy = st.builds(
    Tutorial,
)
universityextended::people::Assistant_strategy = st.builds(
    universityextended::people::Assistant,
    isDoctoralCandidate=
        st.booleans()
)
Lecture_strategy = st.builds(
    Lecture,
)

@given(instance=universityextended::administration::Event_strategy)
@settings(max_examples=50)
def test_universityextended::administration::event_instantiation(instance):
    assert isinstance(instance, universityextended::administration::Event)

@given(instance=universityextended::administration::Event_strategy)
def test_universityextended::administration::event_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=universityextended::administration::Event_strategy)
def test_universityextended::administration::event_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=universityextended::administration::Time_strategy)
@settings(max_examples=50)
def test_universityextended::administration::time_instantiation(instance):
    assert isinstance(instance, universityextended::administration::Time)

@given(instance=universityextended::administration::Time_strategy)
def test_universityextended::administration::time_endHour_type(instance):
    assert isinstance(instance.endHour, int)


@given(instance=universityextended::administration::Time_strategy)
def test_universityextended::administration::time_endHour_setter(instance):
    original = instance.endHour
    instance.endHour = original
    assert instance.endHour == original

@given(instance=universityextended::administration::Time_strategy)
def test_universityextended::administration::time_startHour_type(instance):
    assert isinstance(instance.startHour, int)


@given(instance=universityextended::administration::Time_strategy)
def test_universityextended::administration::time_startHour_setter(instance):
    original = instance.startHour
    instance.startHour = original
    assert instance.startHour == original

@given(instance=universityextended::administration::Time_strategy)
def test_universityextended::administration::time_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=universityextended::administration::Time_strategy)
def test_universityextended::administration::time_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=universityextended::administration::Room_strategy)
@settings(max_examples=50)
def test_universityextended::administration::room_instantiation(instance):
    assert isinstance(instance, universityextended::administration::Room)

@given(instance=universityextended::administration::Room_strategy)
def test_universityextended::administration::room_floor_type(instance):
    assert isinstance(instance.floor, int)


@given(instance=universityextended::administration::Room_strategy)
def test_universityextended::administration::room_floor_setter(instance):
    original = instance.floor
    instance.floor = original
    assert instance.floor == original

@given(instance=universityextended::administration::Room_strategy)
def test_universityextended::administration::room_roomnumber_type(instance):
    assert isinstance(instance.roomnumber, int)


@given(instance=universityextended::administration::Room_strategy)
def test_universityextended::administration::room_roomnumber_setter(instance):
    original = instance.roomnumber
    instance.roomnumber = original
    assert instance.roomnumber == original

@given(instance=universityextended::administration::Room_strategy)
def test_universityextended::administration::room_building_type(instance):
    assert isinstance(instance.building, str)


@given(instance=universityextended::administration::Room_strategy)
def test_universityextended::administration::room_building_setter(instance):
    original = instance.building
    instance.building = original
    assert instance.building == original

@given(instance=Assistant_strategy)
@settings(max_examples=50)
def test_assistant_instantiation(instance):
    assert isinstance(instance, Assistant)

@given(instance=Professor_strategy)
@settings(max_examples=50)
def test_professor_instantiation(instance):
    assert isinstance(instance, Professor)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=universityextended::administration::Tutorial_strategy)
@settings(max_examples=50)
def test_universityextended::administration::tutorial_instantiation(instance):
    assert isinstance(instance, universityextended::administration::Tutorial)

@given(instance=universityextended::administration::Lecture_strategy)
@settings(max_examples=50)
def test_universityextended::administration::lecture_instantiation(instance):
    assert isinstance(instance, universityextended::administration::Lecture)

@given(instance=universityextended::administration::Lecture_strategy)
def test_universityextended::administration::lecture_captions_type(instance):
    assert isinstance(instance.captions, str)


@given(instance=universityextended::administration::Lecture_strategy)
def test_universityextended::administration::lecture_captions_setter(instance):
    original = instance.captions
    instance.captions = original
    assert instance.captions == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)

@given(instance=universityextended::connection::Visits_strategy)
@settings(max_examples=50)
def test_universityextended::connection::visits_instantiation(instance):
    assert isinstance(instance, universityextended::connection::Visits)

@given(instance=universityextended::connection::Visits_strategy)
def test_universityextended::connection::visits_motivation_type(instance):
    assert isinstance(instance.motivation, str)


@given(instance=universityextended::connection::Visits_strategy)
def test_universityextended::connection::visits_motivation_setter(instance):
    original = instance.motivation
    instance.motivation = original
    assert instance.motivation == original

@given(instance=universityextended::people::Person_strategy)
@settings(max_examples=50)
def test_universityextended::people::person_instantiation(instance):
    assert isinstance(instance, universityextended::people::Person)

@given(instance=universityextended::people::Person_strategy)
def test_universityextended::people::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=universityextended::people::Person_strategy)
def test_universityextended::people::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)

@given(instance=Time_strategy)
@settings(max_examples=50)
def test_time_instantiation(instance):
    assert isinstance(instance, Time)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)

@given(instance=Visits_strategy)
@settings(max_examples=50)
def test_visits_instantiation(instance):
    assert isinstance(instance, Visits)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=universityextended::people::Student_strategy)
@settings(max_examples=50)
def test_universityextended::people::student_instantiation(instance):
    assert isinstance(instance, universityextended::people::Student)

@given(instance=universityextended::people::Student_strategy)
def test_universityextended::people::student_matriculationnumber_type(instance):
    assert isinstance(instance.matriculationnumber, str)


@given(instance=universityextended::people::Student_strategy)
def test_universityextended::people::student_matriculationnumber_setter(instance):
    original = instance.matriculationnumber
    instance.matriculationnumber = original
    assert instance.matriculationnumber == original

@given(instance=universityextended::people::Professor_strategy)
@settings(max_examples=50)
def test_universityextended::people::professor_instantiation(instance):
    assert isinstance(instance, universityextended::people::Professor)

@given(instance=universityextended::people::Professor_strategy)
def test_universityextended::people::professor_rank_type(instance):
    assert isinstance(instance.rank, str)


@given(instance=universityextended::people::Professor_strategy)
def test_universityextended::people::professor_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=universityextended::University_strategy)
@settings(max_examples=50)
def test_universityextended::university_instantiation(instance):
    assert isinstance(instance, universityextended::University)

@given(instance=universityextended::administration::Course_strategy)
@settings(max_examples=50)
def test_universityextended::administration::course_instantiation(instance):
    assert isinstance(instance, universityextended::administration::Course)

@given(instance=universityextended::administration::Course_strategy)
def test_universityextended::administration::course_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=universityextended::administration::Course_strategy)
def test_universityextended::administration::course_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=universityextended::administration::Course_strategy)
def test_universityextended::administration::course_endOfCourse_type(instance):
    assert isinstance(instance.endOfCourse, date)


@given(instance=universityextended::administration::Course_strategy)
def test_universityextended::administration::course_endOfCourse_setter(instance):
    original = instance.endOfCourse
    instance.endOfCourse = original
    assert instance.endOfCourse == original

@given(instance=universityextended::administration::Course_strategy)
def test_universityextended::administration::course_startOfCourse_type(instance):
    assert isinstance(instance.startOfCourse, date)


@given(instance=universityextended::administration::Course_strategy)
def test_universityextended::administration::course_startOfCourse_setter(instance):
    original = instance.startOfCourse
    instance.startOfCourse = original
    assert instance.startOfCourse == original

@given(instance=Tutorial_strategy)
@settings(max_examples=50)
def test_tutorial_instantiation(instance):
    assert isinstance(instance, Tutorial)

@given(instance=universityextended::people::Assistant_strategy)
@settings(max_examples=50)
def test_universityextended::people::assistant_instantiation(instance):
    assert isinstance(instance, universityextended::people::Assistant)

@given(instance=universityextended::people::Assistant_strategy)
def test_universityextended::people::assistant_isDoctoralCandidate_type(instance):
    assert isinstance(instance.isDoctoralCandidate, bool)


@given(instance=universityextended::people::Assistant_strategy)
def test_universityextended::people::assistant_isDoctoralCandidate_setter(instance):
    original = instance.isDoctoralCandidate
    instance.isDoctoralCandidate = original
    assert instance.isDoctoralCandidate == original

@given(instance=Lecture_strategy)
@settings(max_examples=50)
def test_lecture_instantiation(instance):
    assert isinstance(instance, Lecture)
