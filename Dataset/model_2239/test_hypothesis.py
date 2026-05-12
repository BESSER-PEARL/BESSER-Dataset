import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    course_TA,
    course_Lecturer,
    course_CourseCoordinator,
    course_Student,
    course_TimetableEntry,
    course_Organisation,
    course_CourseInstance,
    course_StudyProgram,
    course_Course,
    course_Department,
    course_Person,
    course_Timetable,
    course_CourseWork,
    course_Evaluation,
    course_Faculty,
    course_University,
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



def test_course_ta_is_not_abstract():
    assert not inspect.isabstract(course_TA)


def test_course_ta_constructor_exists():
    assert callable(course_TA.__init__)


def test_course_ta_constructor_args():
    sig = inspect.signature(course_TA.__init__)
    params = list(sig.parameters.keys())



def test_course_lecturer_is_not_abstract():
    assert not inspect.isabstract(course_Lecturer)


def test_course_lecturer_constructor_exists():
    assert callable(course_Lecturer.__init__)


def test_course_lecturer_constructor_args():
    sig = inspect.signature(course_Lecturer.__init__)
    params = list(sig.parameters.keys())



def test_course_coursecoordinator_is_not_abstract():
    assert not inspect.isabstract(course_CourseCoordinator)


def test_course_coursecoordinator_constructor_exists():
    assert callable(course_CourseCoordinator.__init__)


def test_course_coursecoordinator_constructor_args():
    sig = inspect.signature(course_CourseCoordinator.__init__)
    params = list(sig.parameters.keys())



def test_course_student_is_not_abstract():
    assert not inspect.isabstract(course_Student)


def test_course_student_constructor_exists():
    assert callable(course_Student.__init__)


def test_course_student_constructor_args():
    sig = inspect.signature(course_Student.__init__)
    params = list(sig.parameters.keys())



def test_course_timetableentry_is_not_abstract():
    assert not inspect.isabstract(course_TimetableEntry)


def test_course_timetableentry_constructor_exists():
    assert callable(course_TimetableEntry.__init__)


def test_course_timetableentry_constructor_args():
    sig = inspect.signature(course_TimetableEntry.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "time" in params, "Missing parameter 'time'"
    assert "room" in params, "Missing parameter 'room'"
    assert "type" in params, "Missing parameter 'type'"

def test_course_timetableentry_has_day():
    assert hasattr(course_TimetableEntry, "day")
    descriptor = None
    for klass in course_TimetableEntry.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_course_timetableentry_has_time():
    assert hasattr(course_TimetableEntry, "time")
    descriptor = None
    for klass in course_TimetableEntry.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_course_timetableentry_has_room():
    assert hasattr(course_TimetableEntry, "room")
    descriptor = None
    for klass in course_TimetableEntry.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_course_timetableentry_has_type():
    assert hasattr(course_TimetableEntry, "type")
    descriptor = None
    for klass in course_TimetableEntry.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_course_organisation_is_not_abstract():
    assert not inspect.isabstract(course_Organisation)


def test_course_organisation_constructor_exists():
    assert callable(course_Organisation.__init__)


def test_course_organisation_constructor_args():
    sig = inspect.signature(course_Organisation.__init__)
    params = list(sig.parameters.keys())



def test_course_courseinstance_is_not_abstract():
    assert not inspect.isabstract(course_CourseInstance)


def test_course_courseinstance_constructor_exists():
    assert callable(course_CourseInstance.__init__)


def test_course_courseinstance_constructor_args():
    sig = inspect.signature(course_CourseInstance.__init__)
    params = list(sig.parameters.keys())



def test_course_studyprogram_is_not_abstract():
    assert not inspect.isabstract(course_StudyProgram)


def test_course_studyprogram_constructor_exists():
    assert callable(course_StudyProgram.__init__)


def test_course_studyprogram_constructor_args():
    sig = inspect.signature(course_StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_course_studyprogram_has_code():
    assert hasattr(course_StudyProgram, "code")
    descriptor = None
    for klass in course_StudyProgram.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_course_course_is_not_abstract():
    assert not inspect.isabstract(course_Course)


def test_course_course_constructor_exists():
    assert callable(course_Course.__init__)


def test_course_course_constructor_args():
    sig = inspect.signature(course_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "content" in params, "Missing parameter 'content'"

def test_course_course_has_credits():
    assert hasattr(course_Course, "credits")
    descriptor = None
    for klass in course_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_course_course_has_code():
    assert hasattr(course_Course, "code")
    descriptor = None
    for klass in course_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_course_course_has_name():
    assert hasattr(course_Course, "name")
    descriptor = None
    for klass in course_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_course_course_has_content():
    assert hasattr(course_Course, "content")
    descriptor = None
    for klass in course_Course.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_course_department_is_not_abstract():
    assert not inspect.isabstract(course_Department)


def test_course_department_constructor_exists():
    assert callable(course_Department.__init__)


def test_course_department_constructor_args():
    sig = inspect.signature(course_Department.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_course_department_has_shortName():
    assert hasattr(course_Department, "shortName")
    descriptor = None
    for klass in course_Department.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_course_department_has_name():
    assert hasattr(course_Department, "name")
    descriptor = None
    for klass in course_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_course_person_is_not_abstract():
    assert not inspect.isabstract(course_Person)


def test_course_person_constructor_exists():
    assert callable(course_Person.__init__)


def test_course_person_constructor_args():
    sig = inspect.signature(course_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_course_person_has_name():
    assert hasattr(course_Person, "name")
    descriptor = None
    for klass in course_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_course_timetable_is_not_abstract():
    assert not inspect.isabstract(course_Timetable)


def test_course_timetable_constructor_exists():
    assert callable(course_Timetable.__init__)


def test_course_timetable_constructor_args():
    sig = inspect.signature(course_Timetable.__init__)
    params = list(sig.parameters.keys())



def test_course_coursework_is_not_abstract():
    assert not inspect.isabstract(course_CourseWork)


def test_course_coursework_constructor_exists():
    assert callable(course_CourseWork.__init__)


def test_course_coursework_constructor_args():
    sig = inspect.signature(course_CourseWork.__init__)
    params = list(sig.parameters.keys())
    assert "lectureHours" in params, "Missing parameter 'lectureHours'"
    assert "labHours" in params, "Missing parameter 'labHours'"

def test_course_coursework_has_lectureHours():
    assert hasattr(course_CourseWork, "lectureHours")
    descriptor = None
    for klass in course_CourseWork.__mro__:
        if "lectureHours" in klass.__dict__:
            descriptor = klass.__dict__["lectureHours"]
            break
    assert isinstance(descriptor, property)

def test_course_coursework_has_labHours():
    assert hasattr(course_CourseWork, "labHours")
    descriptor = None
    for klass in course_CourseWork.__mro__:
        if "labHours" in klass.__dict__:
            descriptor = klass.__dict__["labHours"]
            break
    assert isinstance(descriptor, property)



def test_course_evaluation_is_not_abstract():
    assert not inspect.isabstract(course_Evaluation)


def test_course_evaluation_constructor_exists():
    assert callable(course_Evaluation.__init__)


def test_course_evaluation_constructor_args():
    sig = inspect.signature(course_Evaluation.__init__)
    params = list(sig.parameters.keys())
    assert "exam" in params, "Missing parameter 'exam'"
    assert "assigments" in params, "Missing parameter 'assigments'"
    assert "project" in params, "Missing parameter 'project'"

def test_course_evaluation_has_exam():
    assert hasattr(course_Evaluation, "exam")
    descriptor = None
    for klass in course_Evaluation.__mro__:
        if "exam" in klass.__dict__:
            descriptor = klass.__dict__["exam"]
            break
    assert isinstance(descriptor, property)

def test_course_evaluation_has_assigments():
    assert hasattr(course_Evaluation, "assigments")
    descriptor = None
    for klass in course_Evaluation.__mro__:
        if "assigments" in klass.__dict__:
            descriptor = klass.__dict__["assigments"]
            break
    assert isinstance(descriptor, property)

def test_course_evaluation_has_project():
    assert hasattr(course_Evaluation, "project")
    descriptor = None
    for klass in course_Evaluation.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)



def test_course_faculty_is_not_abstract():
    assert not inspect.isabstract(course_Faculty)


def test_course_faculty_constructor_exists():
    assert callable(course_Faculty.__init__)


def test_course_faculty_constructor_args():
    sig = inspect.signature(course_Faculty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_course_faculty_has_name():
    assert hasattr(course_Faculty, "name")
    descriptor = None
    for klass in course_Faculty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_course_faculty_has_shortName():
    assert hasattr(course_Faculty, "shortName")
    descriptor = None
    for klass in course_Faculty.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)



def test_course_university_is_not_abstract():
    assert not inspect.isabstract(course_University)


def test_course_university_constructor_exists():
    assert callable(course_University.__init__)


def test_course_university_constructor_args():
    sig = inspect.signature(course_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_course_university_has_name():
    assert hasattr(course_University, "name")
    descriptor = None
    for klass in course_University.__mro__:
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
        "Friday",
        "Monday",
        "Thursday",
        "Tuesday",
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
        "Lab",
        "Lecture",
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
course_TA_strategy = st.builds(
    course_TA,
)
course_Lecturer_strategy = st.builds(
    course_Lecturer,
)
course_CourseCoordinator_strategy = st.builds(
    course_CourseCoordinator,
)
course_Student_strategy = st.builds(
    course_Student,
)
course_TimetableEntry_strategy = st.builds(
    course_TimetableEntry,
    day=
        safe_text,
    time=
        safe_text,
    room=
        safe_text,
    type=
        safe_text
)
course_Organisation_strategy = st.builds(
    course_Organisation,
)
course_CourseInstance_strategy = st.builds(
    course_CourseInstance,
)
course_StudyProgram_strategy = st.builds(
    course_StudyProgram,
    code=
        safe_text
)
course_Course_strategy = st.builds(
    course_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    name=
        safe_text,
    content=
        safe_text
)
course_Department_strategy = st.builds(
    course_Department,
    shortName=
        safe_text,
    name=
        safe_text
)
course_Person_strategy = st.builds(
    course_Person,
    name=
        safe_text
)
course_Timetable_strategy = st.builds(
    course_Timetable,
)
course_CourseWork_strategy = st.builds(
    course_CourseWork,
    lectureHours=
        st.integers(),
    labHours=
        st.integers()
)
course_Evaluation_strategy = st.builds(
    course_Evaluation,
    exam=
        st.integers(),
    assigments=
        st.integers(),
    project=
        st.integers()
)
course_Faculty_strategy = st.builds(
    course_Faculty,
    name=
        safe_text,
    shortName=
        safe_text
)
course_University_strategy = st.builds(
    course_University,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=course_TA_strategy)
@settings(max_examples=50)
def test_course_ta_instantiation(instance):
    assert isinstance(instance, course_TA)

@given(instance=course_Lecturer_strategy)
@settings(max_examples=50)
def test_course_lecturer_instantiation(instance):
    assert isinstance(instance, course_Lecturer)

@given(instance=course_CourseCoordinator_strategy)
@settings(max_examples=50)
def test_course_coursecoordinator_instantiation(instance):
    assert isinstance(instance, course_CourseCoordinator)

@given(instance=course_Student_strategy)
@settings(max_examples=50)
def test_course_student_instantiation(instance):
    assert isinstance(instance, course_Student)

@given(instance=course_TimetableEntry_strategy)
@settings(max_examples=50)
def test_course_timetableentry_instantiation(instance):
    assert isinstance(instance, course_TimetableEntry)



@given(instance=course_TimetableEntry_strategy)
def test_course_timetableentry_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=course_TimetableEntry_strategy)
def test_course_timetableentry_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=course_TimetableEntry_strategy)
def test_course_timetableentry_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=course_TimetableEntry_strategy)
def test_course_timetableentry_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=course_Organisation_strategy)
@settings(max_examples=50)
def test_course_organisation_instantiation(instance):
    assert isinstance(instance, course_Organisation)

@given(instance=course_CourseInstance_strategy)
@settings(max_examples=50)
def test_course_courseinstance_instantiation(instance):
    assert isinstance(instance, course_CourseInstance)

@given(instance=course_StudyProgram_strategy)
@settings(max_examples=50)
def test_course_studyprogram_instantiation(instance):
    assert isinstance(instance, course_StudyProgram)



@given(instance=course_StudyProgram_strategy)
def test_course_studyprogram_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=course_Course_strategy)
@settings(max_examples=50)
def test_course_course_instantiation(instance):
    assert isinstance(instance, course_Course)



@given(instance=course_Course_strategy)
def test_course_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=course_Course_strategy)
def test_course_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=course_Course_strategy)
def test_course_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=course_Course_strategy)
def test_course_course_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=course_Department_strategy)
@settings(max_examples=50)
def test_course_department_instantiation(instance):
    assert isinstance(instance, course_Department)



@given(instance=course_Department_strategy)
def test_course_department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original



@given(instance=course_Department_strategy)
def test_course_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=course_Person_strategy)
@settings(max_examples=50)
def test_course_person_instantiation(instance):
    assert isinstance(instance, course_Person)



@given(instance=course_Person_strategy)
def test_course_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=course_Timetable_strategy)
@settings(max_examples=50)
def test_course_timetable_instantiation(instance):
    assert isinstance(instance, course_Timetable)

@given(instance=course_CourseWork_strategy)
@settings(max_examples=50)
def test_course_coursework_instantiation(instance):
    assert isinstance(instance, course_CourseWork)



@given(instance=course_CourseWork_strategy)
def test_course_coursework_lectureHours_setter(instance):
    original = instance.lectureHours
    instance.lectureHours = original
    assert instance.lectureHours == original



@given(instance=course_CourseWork_strategy)
def test_course_coursework_labHours_setter(instance):
    original = instance.labHours
    instance.labHours = original
    assert instance.labHours == original

@given(instance=course_Evaluation_strategy)
@settings(max_examples=50)
def test_course_evaluation_instantiation(instance):
    assert isinstance(instance, course_Evaluation)



@given(instance=course_Evaluation_strategy)
def test_course_evaluation_exam_setter(instance):
    original = instance.exam
    instance.exam = original
    assert instance.exam == original



@given(instance=course_Evaluation_strategy)
def test_course_evaluation_assigments_setter(instance):
    original = instance.assigments
    instance.assigments = original
    assert instance.assigments == original



@given(instance=course_Evaluation_strategy)
def test_course_evaluation_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=course_Faculty_strategy)
@settings(max_examples=50)
def test_course_faculty_instantiation(instance):
    assert isinstance(instance, course_Faculty)



@given(instance=course_Faculty_strategy)
def test_course_faculty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=course_Faculty_strategy)
def test_course_faculty_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=course_University_strategy)
@settings(max_examples=50)
def test_course_university_instantiation(instance):
    assert isinstance(instance, course_University)



@given(instance=course_University_strategy)
def test_course_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
