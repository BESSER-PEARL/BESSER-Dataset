import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    course::TA,
    course::Lecturer,
    course::CourseCoordinator,
    course::Student,
    course::TimetableEntry,
    course::Organisation,
    course::CourseInstance,
    course::StudyProgram,
    course::Course,
    course::Department,
    course::Person,
    course::Timetable,
    course::CourseWork,
    course::Evaluation,
    course::Faculty,
    course::University,
    DayOfWeek,
    TypeOfInstruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_course::ta_is_not_abstract():
    assert not inspect.isabstract(course::TA)


def test_course::ta_constructor_exists():
    assert callable(course::TA.__init__)


def test_course::ta_constructor_args():
    sig = inspect.signature(course::TA.__init__)
    params = list(sig.parameters.keys())



def test_course::lecturer_is_not_abstract():
    assert not inspect.isabstract(course::Lecturer)


def test_course::lecturer_constructor_exists():
    assert callable(course::Lecturer.__init__)


def test_course::lecturer_constructor_args():
    sig = inspect.signature(course::Lecturer.__init__)
    params = list(sig.parameters.keys())



def test_course::coursecoordinator_is_not_abstract():
    assert not inspect.isabstract(course::CourseCoordinator)


def test_course::coursecoordinator_constructor_exists():
    assert callable(course::CourseCoordinator.__init__)


def test_course::coursecoordinator_constructor_args():
    sig = inspect.signature(course::CourseCoordinator.__init__)
    params = list(sig.parameters.keys())



def test_course::student_is_not_abstract():
    assert not inspect.isabstract(course::Student)


def test_course::student_constructor_exists():
    assert callable(course::Student.__init__)


def test_course::student_constructor_args():
    sig = inspect.signature(course::Student.__init__)
    params = list(sig.parameters.keys())



def test_course::timetableentry_is_not_abstract():
    assert not inspect.isabstract(course::TimetableEntry)


def test_course::timetableentry_constructor_exists():
    assert callable(course::TimetableEntry.__init__)


def test_course::timetableentry_constructor_args():
    sig = inspect.signature(course::TimetableEntry.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "day" in params, "Missing parameter 'day'"
    assert "time" in params, "Missing parameter 'time'"
    assert "room" in params, "Missing parameter 'room'"

def test_course::timetableentry_has_type():
    assert hasattr(course::TimetableEntry, "type")
    descriptor = None
    for klass in course::TimetableEntry.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_course::timetableentry_has_day():
    assert hasattr(course::TimetableEntry, "day")
    descriptor = None
    for klass in course::TimetableEntry.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_course::timetableentry_has_time():
    assert hasattr(course::TimetableEntry, "time")
    descriptor = None
    for klass in course::TimetableEntry.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_course::timetableentry_has_room():
    assert hasattr(course::TimetableEntry, "room")
    descriptor = None
    for klass in course::TimetableEntry.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)



def test_course::organisation_is_not_abstract():
    assert not inspect.isabstract(course::Organisation)


def test_course::organisation_constructor_exists():
    assert callable(course::Organisation.__init__)


def test_course::organisation_constructor_args():
    sig = inspect.signature(course::Organisation.__init__)
    params = list(sig.parameters.keys())



def test_course::courseinstance_is_not_abstract():
    assert not inspect.isabstract(course::CourseInstance)


def test_course::courseinstance_constructor_exists():
    assert callable(course::CourseInstance.__init__)


def test_course::courseinstance_constructor_args():
    sig = inspect.signature(course::CourseInstance.__init__)
    params = list(sig.parameters.keys())



def test_course::studyprogram_is_not_abstract():
    assert not inspect.isabstract(course::StudyProgram)


def test_course::studyprogram_constructor_exists():
    assert callable(course::StudyProgram.__init__)


def test_course::studyprogram_constructor_args():
    sig = inspect.signature(course::StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_course::studyprogram_has_code():
    assert hasattr(course::StudyProgram, "code")
    descriptor = None
    for klass in course::StudyProgram.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_course::course_is_not_abstract():
    assert not inspect.isabstract(course::Course)


def test_course::course_constructor_exists():
    assert callable(course::Course.__init__)


def test_course::course_constructor_args():
    sig = inspect.signature(course::Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "content" in params, "Missing parameter 'content'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_course::course_has_credits():
    assert hasattr(course::Course, "credits")
    descriptor = None
    for klass in course::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_course::course_has_content():
    assert hasattr(course::Course, "content")
    descriptor = None
    for klass in course::Course.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_course::course_has_code():
    assert hasattr(course::Course, "code")
    descriptor = None
    for klass in course::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_course::course_has_name():
    assert hasattr(course::Course, "name")
    descriptor = None
    for klass in course::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_course::department_is_not_abstract():
    assert not inspect.isabstract(course::Department)


def test_course::department_constructor_exists():
    assert callable(course::Department.__init__)


def test_course::department_constructor_args():
    sig = inspect.signature(course::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_course::department_has_name():
    assert hasattr(course::Department, "name")
    descriptor = None
    for klass in course::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_course::department_has_shortName():
    assert hasattr(course::Department, "shortName")
    descriptor = None
    for klass in course::Department.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)



def test_course::person_is_not_abstract():
    assert not inspect.isabstract(course::Person)


def test_course::person_constructor_exists():
    assert callable(course::Person.__init__)


def test_course::person_constructor_args():
    sig = inspect.signature(course::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_course::person_has_name():
    assert hasattr(course::Person, "name")
    descriptor = None
    for klass in course::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_course::timetable_is_not_abstract():
    assert not inspect.isabstract(course::Timetable)


def test_course::timetable_constructor_exists():
    assert callable(course::Timetable.__init__)


def test_course::timetable_constructor_args():
    sig = inspect.signature(course::Timetable.__init__)
    params = list(sig.parameters.keys())



def test_course::coursework_is_not_abstract():
    assert not inspect.isabstract(course::CourseWork)


def test_course::coursework_constructor_exists():
    assert callable(course::CourseWork.__init__)


def test_course::coursework_constructor_args():
    sig = inspect.signature(course::CourseWork.__init__)
    params = list(sig.parameters.keys())
    assert "lectureHours" in params, "Missing parameter 'lectureHours'"
    assert "labHours" in params, "Missing parameter 'labHours'"

def test_course::coursework_has_lectureHours():
    assert hasattr(course::CourseWork, "lectureHours")
    descriptor = None
    for klass in course::CourseWork.__mro__:
        if "lectureHours" in klass.__dict__:
            descriptor = klass.__dict__["lectureHours"]
            break
    assert isinstance(descriptor, property)

def test_course::coursework_has_labHours():
    assert hasattr(course::CourseWork, "labHours")
    descriptor = None
    for klass in course::CourseWork.__mro__:
        if "labHours" in klass.__dict__:
            descriptor = klass.__dict__["labHours"]
            break
    assert isinstance(descriptor, property)



def test_course::evaluation_is_not_abstract():
    assert not inspect.isabstract(course::Evaluation)


def test_course::evaluation_constructor_exists():
    assert callable(course::Evaluation.__init__)


def test_course::evaluation_constructor_args():
    sig = inspect.signature(course::Evaluation.__init__)
    params = list(sig.parameters.keys())
    assert "exam" in params, "Missing parameter 'exam'"
    assert "assigments" in params, "Missing parameter 'assigments'"
    assert "project" in params, "Missing parameter 'project'"

def test_course::evaluation_has_exam():
    assert hasattr(course::Evaluation, "exam")
    descriptor = None
    for klass in course::Evaluation.__mro__:
        if "exam" in klass.__dict__:
            descriptor = klass.__dict__["exam"]
            break
    assert isinstance(descriptor, property)

def test_course::evaluation_has_assigments():
    assert hasattr(course::Evaluation, "assigments")
    descriptor = None
    for klass in course::Evaluation.__mro__:
        if "assigments" in klass.__dict__:
            descriptor = klass.__dict__["assigments"]
            break
    assert isinstance(descriptor, property)

def test_course::evaluation_has_project():
    assert hasattr(course::Evaluation, "project")
    descriptor = None
    for klass in course::Evaluation.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)



def test_course::faculty_is_not_abstract():
    assert not inspect.isabstract(course::Faculty)


def test_course::faculty_constructor_exists():
    assert callable(course::Faculty.__init__)


def test_course::faculty_constructor_args():
    sig = inspect.signature(course::Faculty.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_course::faculty_has_shortName():
    assert hasattr(course::Faculty, "shortName")
    descriptor = None
    for klass in course::Faculty.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_course::faculty_has_name():
    assert hasattr(course::Faculty, "name")
    descriptor = None
    for klass in course::Faculty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_course::university_is_not_abstract():
    assert not inspect.isabstract(course::University)


def test_course::university_constructor_exists():
    assert callable(course::University.__init__)


def test_course::university_constructor_args():
    sig = inspect.signature(course::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_course::university_has_name():
    assert hasattr(course::University, "name")
    descriptor = None
    for klass in course::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dayofweek_exists():
    # Check that the Enumeration exists
    assert DayOfWeek is not None

def test_dayofweek_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DayOfWeek]
    expected_literals = [
        "Tuesday",
        "Monday",
        "Thursday",
        "Friday",
        "Wednesday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DayOfWeek"

def test_typeofinstruction_exists():
    # Check that the Enumeration exists
    assert TypeOfInstruction is not None

def test_typeofinstruction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOfInstruction]
    expected_literals = [
        "Lecture",
        "Lab",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOfInstruction"


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
Person_strategy = st.builds(
    Person,
)
course::TA_strategy = st.builds(
    course::TA,
)
course::Lecturer_strategy = st.builds(
    course::Lecturer,
)
course::CourseCoordinator_strategy = st.builds(
    course::CourseCoordinator,
)
course::Student_strategy = st.builds(
    course::Student,
)
course::TimetableEntry_strategy = st.builds(
    course::TimetableEntry,
    type=
        safe_text,
    day=
        safe_text,
    time=
        safe_text,
    room=
        safe_text
)
course::Organisation_strategy = st.builds(
    course::Organisation,
)
course::CourseInstance_strategy = st.builds(
    course::CourseInstance,
)
course::StudyProgram_strategy = st.builds(
    course::StudyProgram,
    code=
        safe_text
)
course::Course_strategy = st.builds(
    course::Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    content=
        safe_text,
    code=
        safe_text,
    name=
        safe_text
)
course::Department_strategy = st.builds(
    course::Department,
    name=
        safe_text,
    shortName=
        safe_text
)
course::Person_strategy = st.builds(
    course::Person,
    name=
        safe_text
)
course::Timetable_strategy = st.builds(
    course::Timetable,
)
course::CourseWork_strategy = st.builds(
    course::CourseWork,
    lectureHours=
        st.integers(),
    labHours=
        st.integers()
)
course::Evaluation_strategy = st.builds(
    course::Evaluation,
    exam=
        st.integers(),
    assigments=
        st.integers(),
    project=
        st.integers()
)
course::Faculty_strategy = st.builds(
    course::Faculty,
    shortName=
        safe_text,
    name=
        safe_text
)
course::University_strategy = st.builds(
    course::University,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=course::TA_strategy)
@settings(max_examples=50)
def test_course::ta_instantiation(instance):
    assert isinstance(instance, course::TA)

@given(instance=course::Lecturer_strategy)
@settings(max_examples=50)
def test_course::lecturer_instantiation(instance):
    assert isinstance(instance, course::Lecturer)

@given(instance=course::CourseCoordinator_strategy)
@settings(max_examples=50)
def test_course::coursecoordinator_instantiation(instance):
    assert isinstance(instance, course::CourseCoordinator)

@given(instance=course::Student_strategy)
@settings(max_examples=50)
def test_course::student_instantiation(instance):
    assert isinstance(instance, course::Student)

@given(instance=course::TimetableEntry_strategy)
@settings(max_examples=50)
def test_course::timetableentry_instantiation(instance):
    assert isinstance(instance, course::TimetableEntry)

@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_room_type(instance):
    assert isinstance(instance.room, str)


@given(instance=course::TimetableEntry_strategy)
def test_course::timetableentry_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original

@given(instance=course::Organisation_strategy)
@settings(max_examples=50)
def test_course::organisation_instantiation(instance):
    assert isinstance(instance, course::Organisation)

@given(instance=course::CourseInstance_strategy)
@settings(max_examples=50)
def test_course::courseinstance_instantiation(instance):
    assert isinstance(instance, course::CourseInstance)

@given(instance=course::StudyProgram_strategy)
@settings(max_examples=50)
def test_course::studyprogram_instantiation(instance):
    assert isinstance(instance, course::StudyProgram)

@given(instance=course::StudyProgram_strategy)
def test_course::studyprogram_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=course::StudyProgram_strategy)
def test_course::studyprogram_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=course::Course_strategy)
@settings(max_examples=50)
def test_course::course_instantiation(instance):
    assert isinstance(instance, course::Course)

@given(instance=course::Course_strategy)
def test_course::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=course::Course_strategy)
def test_course::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=course::Course_strategy)
def test_course::course_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=course::Course_strategy)
def test_course::course_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=course::Course_strategy)
def test_course::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=course::Course_strategy)
def test_course::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=course::Course_strategy)
def test_course::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=course::Course_strategy)
def test_course::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=course::Department_strategy)
@settings(max_examples=50)
def test_course::department_instantiation(instance):
    assert isinstance(instance, course::Department)

@given(instance=course::Department_strategy)
def test_course::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=course::Department_strategy)
def test_course::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=course::Department_strategy)
def test_course::department_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=course::Department_strategy)
def test_course::department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=course::Person_strategy)
@settings(max_examples=50)
def test_course::person_instantiation(instance):
    assert isinstance(instance, course::Person)

@given(instance=course::Person_strategy)
def test_course::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=course::Person_strategy)
def test_course::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=course::Timetable_strategy)
@settings(max_examples=50)
def test_course::timetable_instantiation(instance):
    assert isinstance(instance, course::Timetable)

@given(instance=course::CourseWork_strategy)
@settings(max_examples=50)
def test_course::coursework_instantiation(instance):
    assert isinstance(instance, course::CourseWork)

@given(instance=course::CourseWork_strategy)
def test_course::coursework_lectureHours_type(instance):
    assert isinstance(instance.lectureHours, int)


@given(instance=course::CourseWork_strategy)
def test_course::coursework_lectureHours_setter(instance):
    original = instance.lectureHours
    instance.lectureHours = original
    assert instance.lectureHours == original

@given(instance=course::CourseWork_strategy)
def test_course::coursework_labHours_type(instance):
    assert isinstance(instance.labHours, int)


@given(instance=course::CourseWork_strategy)
def test_course::coursework_labHours_setter(instance):
    original = instance.labHours
    instance.labHours = original
    assert instance.labHours == original

@given(instance=course::Evaluation_strategy)
@settings(max_examples=50)
def test_course::evaluation_instantiation(instance):
    assert isinstance(instance, course::Evaluation)

@given(instance=course::Evaluation_strategy)
def test_course::evaluation_exam_type(instance):
    assert isinstance(instance.exam, int)


@given(instance=course::Evaluation_strategy)
def test_course::evaluation_exam_setter(instance):
    original = instance.exam
    instance.exam = original
    assert instance.exam == original

@given(instance=course::Evaluation_strategy)
def test_course::evaluation_assigments_type(instance):
    assert isinstance(instance.assigments, int)


@given(instance=course::Evaluation_strategy)
def test_course::evaluation_assigments_setter(instance):
    original = instance.assigments
    instance.assigments = original
    assert instance.assigments == original

@given(instance=course::Evaluation_strategy)
def test_course::evaluation_project_type(instance):
    assert isinstance(instance.project, int)


@given(instance=course::Evaluation_strategy)
def test_course::evaluation_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=course::Faculty_strategy)
@settings(max_examples=50)
def test_course::faculty_instantiation(instance):
    assert isinstance(instance, course::Faculty)

@given(instance=course::Faculty_strategy)
def test_course::faculty_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=course::Faculty_strategy)
def test_course::faculty_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=course::Faculty_strategy)
def test_course::faculty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=course::Faculty_strategy)
def test_course::faculty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=course::University_strategy)
@settings(max_examples=50)
def test_course::university_instantiation(instance):
    assert isinstance(instance, course::University)

@given(instance=course::University_strategy)
def test_course::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=course::University_strategy)
def test_course::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
