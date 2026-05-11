import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tdt4250case::ScheduledActivity,
    tdt4250case::ExaminationActivity,
    tdt4250case::CourseWork,
    tdt4250case::CourseInstance,
    tdt4250case::CreditReductionCourse,
    tdt4250case::Studyprogram,
    tdt4250case::Course,
    tdt4250case::Person,
    tdt4250case::CourseRole,
    tdt4250case::Department,
    tdt4250case::Timetable,
    tdt4250case::Examination,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tdt4250case::scheduledactivity_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::ScheduledActivity)


def test_tdt4250case::scheduledactivity_constructor_exists():
    assert callable(tdt4250case::ScheduledActivity.__init__)


def test_tdt4250case::scheduledactivity_constructor_args():
    sig = inspect.signature(tdt4250case::ScheduledActivity.__init__)
    params = list(sig.parameters.keys())
    assert "timeslot" in params, "Missing parameter 'timeslot'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "room" in params, "Missing parameter 'room'"

def test_tdt4250case::scheduledactivity_has_timeslot():
    assert hasattr(tdt4250case::ScheduledActivity, "timeslot")
    descriptor = None
    for klass in tdt4250case::ScheduledActivity.__mro__:
        if "timeslot" in klass.__dict__:
            descriptor = klass.__dict__["timeslot"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::scheduledactivity_has_activity():
    assert hasattr(tdt4250case::ScheduledActivity, "activity")
    descriptor = None
    for klass in tdt4250case::ScheduledActivity.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::scheduledactivity_has_room():
    assert hasattr(tdt4250case::ScheduledActivity, "room")
    descriptor = None
    for klass in tdt4250case::ScheduledActivity.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::examinationactivity_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::ExaminationActivity)


def test_tdt4250case::examinationactivity_constructor_exists():
    assert callable(tdt4250case::ExaminationActivity.__init__)


def test_tdt4250case::examinationactivity_constructor_args():
    sig = inspect.signature(tdt4250case::ExaminationActivity.__init__)
    params = list(sig.parameters.keys())
    assert "weighting" in params, "Missing parameter 'weighting'"
    assert "evaluationForm" in params, "Missing parameter 'evaluationForm'"

def test_tdt4250case::examinationactivity_has_weighting():
    assert hasattr(tdt4250case::ExaminationActivity, "weighting")
    descriptor = None
    for klass in tdt4250case::ExaminationActivity.__mro__:
        if "weighting" in klass.__dict__:
            descriptor = klass.__dict__["weighting"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::examinationactivity_has_evaluationForm():
    assert hasattr(tdt4250case::ExaminationActivity, "evaluationForm")
    descriptor = None
    for klass in tdt4250case::ExaminationActivity.__mro__:
        if "evaluationForm" in klass.__dict__:
            descriptor = klass.__dict__["evaluationForm"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::coursework_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::CourseWork)


def test_tdt4250case::coursework_constructor_exists():
    assert callable(tdt4250case::CourseWork.__init__)


def test_tdt4250case::coursework_constructor_args():
    sig = inspect.signature(tdt4250case::CourseWork.__init__)
    params = list(sig.parameters.keys())
    assert "hours" in params, "Missing parameter 'hours'"
    assert "type" in params, "Missing parameter 'type'"

def test_tdt4250case::coursework_has_hours():
    assert hasattr(tdt4250case::CourseWork, "hours")
    descriptor = None
    for klass in tdt4250case::CourseWork.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::coursework_has_type():
    assert hasattr(tdt4250case::CourseWork, "type")
    descriptor = None
    for klass in tdt4250case::CourseWork.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::courseinstance_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::CourseInstance)


def test_tdt4250case::courseinstance_constructor_exists():
    assert callable(tdt4250case::CourseInstance.__init__)


def test_tdt4250case::courseinstance_constructor_args():
    sig = inspect.signature(tdt4250case::CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"

def test_tdt4250case::courseinstance_has_semester():
    assert hasattr(tdt4250case::CourseInstance, "semester")
    descriptor = None
    for klass in tdt4250case::CourseInstance.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::creditreductioncourse_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::CreditReductionCourse)


def test_tdt4250case::creditreductioncourse_constructor_exists():
    assert callable(tdt4250case::CreditReductionCourse.__init__)


def test_tdt4250case::creditreductioncourse_constructor_args():
    sig = inspect.signature(tdt4250case::CreditReductionCourse.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"
    assert "reduction" in params, "Missing parameter 'reduction'"

def test_tdt4250case::creditreductioncourse_has_from_():
    assert hasattr(tdt4250case::CreditReductionCourse, "from_")
    descriptor = None
    for klass in tdt4250case::CreditReductionCourse.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::creditreductioncourse_has_to():
    assert hasattr(tdt4250case::CreditReductionCourse, "to")
    descriptor = None
    for klass in tdt4250case::CreditReductionCourse.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::creditreductioncourse_has_reduction():
    assert hasattr(tdt4250case::CreditReductionCourse, "reduction")
    descriptor = None
    for klass in tdt4250case::CreditReductionCourse.__mro__:
        if "reduction" in klass.__dict__:
            descriptor = klass.__dict__["reduction"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::studyprogram_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::Studyprogram)


def test_tdt4250case::studyprogram_constructor_exists():
    assert callable(tdt4250case::Studyprogram.__init__)


def test_tdt4250case::studyprogram_constructor_args():
    sig = inspect.signature(tdt4250case::Studyprogram.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_tdt4250case::studyprogram_has_code():
    assert hasattr(tdt4250case::Studyprogram, "code")
    descriptor = None
    for klass in tdt4250case::Studyprogram.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::course_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::Course)


def test_tdt4250case::course_constructor_exists():
    assert callable(tdt4250case::Course.__init__)


def test_tdt4250case::course_constructor_args():
    sig = inspect.signature(tdt4250case::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "content" in params, "Missing parameter 'content'"

def test_tdt4250case::course_has_name():
    assert hasattr(tdt4250case::Course, "name")
    descriptor = None
    for klass in tdt4250case::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::course_has_code():
    assert hasattr(tdt4250case::Course, "code")
    descriptor = None
    for klass in tdt4250case::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::course_has_credits():
    assert hasattr(tdt4250case::Course, "credits")
    descriptor = None
    for klass in tdt4250case::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::course_has_content():
    assert hasattr(tdt4250case::Course, "content")
    descriptor = None
    for klass in tdt4250case::Course.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::person_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::Person)


def test_tdt4250case::person_constructor_exists():
    assert callable(tdt4250case::Person.__init__)


def test_tdt4250case::person_constructor_args():
    sig = inspect.signature(tdt4250case::Person.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250case::person_has_username():
    assert hasattr(tdt4250case::Person, "username")
    descriptor = None
    for klass in tdt4250case::Person.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::person_has_name():
    assert hasattr(tdt4250case::Person, "name")
    descriptor = None
    for klass in tdt4250case::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::courserole_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::CourseRole)


def test_tdt4250case::courserole_constructor_exists():
    assert callable(tdt4250case::CourseRole.__init__)


def test_tdt4250case::courserole_constructor_args():
    sig = inspect.signature(tdt4250case::CourseRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250case::courserole_has_name():
    assert hasattr(tdt4250case::CourseRole, "name")
    descriptor = None
    for klass in tdt4250case::CourseRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::department_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::Department)


def test_tdt4250case::department_constructor_exists():
    assert callable(tdt4250case::Department.__init__)


def test_tdt4250case::department_constructor_args():
    sig = inspect.signature(tdt4250case::Department.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250case::department_has_code():
    assert hasattr(tdt4250case::Department, "code")
    descriptor = None
    for klass in tdt4250case::Department.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case::department_has_name():
    assert hasattr(tdt4250case::Department, "name")
    descriptor = None
    for klass in tdt4250case::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case::timetable_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::Timetable)


def test_tdt4250case::timetable_constructor_exists():
    assert callable(tdt4250case::Timetable.__init__)


def test_tdt4250case::timetable_constructor_args():
    sig = inspect.signature(tdt4250case::Timetable.__init__)
    params = list(sig.parameters.keys())



def test_tdt4250case::examination_is_not_abstract():
    assert not inspect.isabstract(tdt4250case::Examination)


def test_tdt4250case::examination_constructor_exists():
    assert callable(tdt4250case::Examination.__init__)


def test_tdt4250case::examination_constructor_args():
    sig = inspect.signature(tdt4250case::Examination.__init__)
    params = list(sig.parameters.keys())


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
tdt4250case::ScheduledActivity_strategy = st.builds(
    tdt4250case::ScheduledActivity,
    timeslot=
        safe_text,
    activity=
        safe_text,
    room=
        safe_text
)
tdt4250case::ExaminationActivity_strategy = st.builds(
    tdt4250case::ExaminationActivity,
    weighting=
        safe_text,
    evaluationForm=
        safe_text
)
tdt4250case::CourseWork_strategy = st.builds(
    tdt4250case::CourseWork,
    hours=
        st.integers(),
    type=
        safe_text
)
tdt4250case::CourseInstance_strategy = st.builds(
    tdt4250case::CourseInstance,
    semester=
        safe_text
)
tdt4250case::CreditReductionCourse_strategy = st.builds(
    tdt4250case::CreditReductionCourse,
    from_=
        st.dates(),
    to=
        st.dates(),
    reduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
tdt4250case::Studyprogram_strategy = st.builds(
    tdt4250case::Studyprogram,
    code=
        safe_text
)
tdt4250case::Course_strategy = st.builds(
    tdt4250case::Course,
    name=
        safe_text,
    code=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    content=
        safe_text
)
tdt4250case::Person_strategy = st.builds(
    tdt4250case::Person,
    username=
        safe_text,
    name=
        safe_text
)
tdt4250case::CourseRole_strategy = st.builds(
    tdt4250case::CourseRole,
    name=
        safe_text
)
tdt4250case::Department_strategy = st.builds(
    tdt4250case::Department,
    code=
        safe_text,
    name=
        safe_text
)
tdt4250case::Timetable_strategy = st.builds(
    tdt4250case::Timetable,
)
tdt4250case::Examination_strategy = st.builds(
    tdt4250case::Examination,
)

@given(instance=tdt4250case::ScheduledActivity_strategy)
@settings(max_examples=50)
def test_tdt4250case::scheduledactivity_instantiation(instance):
    assert isinstance(instance, tdt4250case::ScheduledActivity)

@given(instance=tdt4250case::ScheduledActivity_strategy)
def test_tdt4250case::scheduledactivity_timeslot_type(instance):
    assert isinstance(instance.timeslot, str)


@given(instance=tdt4250case::ScheduledActivity_strategy)
def test_tdt4250case::scheduledactivity_timeslot_setter(instance):
    original = instance.timeslot
    instance.timeslot = original
    assert instance.timeslot == original

@given(instance=tdt4250case::ScheduledActivity_strategy)
def test_tdt4250case::scheduledactivity_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=tdt4250case::ScheduledActivity_strategy)
def test_tdt4250case::scheduledactivity_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=tdt4250case::ScheduledActivity_strategy)
def test_tdt4250case::scheduledactivity_room_type(instance):
    assert isinstance(instance.room, str)


@given(instance=tdt4250case::ScheduledActivity_strategy)
def test_tdt4250case::scheduledactivity_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original

@given(instance=tdt4250case::ExaminationActivity_strategy)
@settings(max_examples=50)
def test_tdt4250case::examinationactivity_instantiation(instance):
    assert isinstance(instance, tdt4250case::ExaminationActivity)

@given(instance=tdt4250case::ExaminationActivity_strategy)
def test_tdt4250case::examinationactivity_weighting_type(instance):
    assert isinstance(instance.weighting, str)


@given(instance=tdt4250case::ExaminationActivity_strategy)
def test_tdt4250case::examinationactivity_weighting_setter(instance):
    original = instance.weighting
    instance.weighting = original
    assert instance.weighting == original

@given(instance=tdt4250case::ExaminationActivity_strategy)
def test_tdt4250case::examinationactivity_evaluationForm_type(instance):
    assert isinstance(instance.evaluationForm, str)


@given(instance=tdt4250case::ExaminationActivity_strategy)
def test_tdt4250case::examinationactivity_evaluationForm_setter(instance):
    original = instance.evaluationForm
    instance.evaluationForm = original
    assert instance.evaluationForm == original

@given(instance=tdt4250case::CourseWork_strategy)
@settings(max_examples=50)
def test_tdt4250case::coursework_instantiation(instance):
    assert isinstance(instance, tdt4250case::CourseWork)

@given(instance=tdt4250case::CourseWork_strategy)
def test_tdt4250case::coursework_hours_type(instance):
    assert isinstance(instance.hours, int)


@given(instance=tdt4250case::CourseWork_strategy)
def test_tdt4250case::coursework_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original

@given(instance=tdt4250case::CourseWork_strategy)
def test_tdt4250case::coursework_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=tdt4250case::CourseWork_strategy)
def test_tdt4250case::coursework_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tdt4250case::CourseInstance_strategy)
@settings(max_examples=50)
def test_tdt4250case::courseinstance_instantiation(instance):
    assert isinstance(instance, tdt4250case::CourseInstance)

@given(instance=tdt4250case::CourseInstance_strategy)
def test_tdt4250case::courseinstance_semester_type(instance):
    assert isinstance(instance.semester, str)


@given(instance=tdt4250case::CourseInstance_strategy)
def test_tdt4250case::courseinstance_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=tdt4250case::CreditReductionCourse_strategy)
@settings(max_examples=50)
def test_tdt4250case::creditreductioncourse_instantiation(instance):
    assert isinstance(instance, tdt4250case::CreditReductionCourse)

@given(instance=tdt4250case::CreditReductionCourse_strategy)
def test_tdt4250case::creditreductioncourse_from__type(instance):
    assert isinstance(instance.from_, date)


@given(instance=tdt4250case::CreditReductionCourse_strategy)
def test_tdt4250case::creditreductioncourse_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=tdt4250case::CreditReductionCourse_strategy)
def test_tdt4250case::creditreductioncourse_to_type(instance):
    assert isinstance(instance.to, date)


@given(instance=tdt4250case::CreditReductionCourse_strategy)
def test_tdt4250case::creditreductioncourse_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=tdt4250case::CreditReductionCourse_strategy)
def test_tdt4250case::creditreductioncourse_reduction_type(instance):
    assert isinstance(instance.reduction, float)


@given(instance=tdt4250case::CreditReductionCourse_strategy)
def test_tdt4250case::creditreductioncourse_reduction_setter(instance):
    original = instance.reduction
    instance.reduction = original
    assert instance.reduction == original

@given(instance=tdt4250case::Studyprogram_strategy)
@settings(max_examples=50)
def test_tdt4250case::studyprogram_instantiation(instance):
    assert isinstance(instance, tdt4250case::Studyprogram)

@given(instance=tdt4250case::Studyprogram_strategy)
def test_tdt4250case::studyprogram_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=tdt4250case::Studyprogram_strategy)
def test_tdt4250case::studyprogram_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=tdt4250case::Course_strategy)
@settings(max_examples=50)
def test_tdt4250case::course_instantiation(instance):
    assert isinstance(instance, tdt4250case::Course)

@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=tdt4250case::Course_strategy)
def test_tdt4250case::course_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=tdt4250case::Person_strategy)
@settings(max_examples=50)
def test_tdt4250case::person_instantiation(instance):
    assert isinstance(instance, tdt4250case::Person)

@given(instance=tdt4250case::Person_strategy)
def test_tdt4250case::person_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=tdt4250case::Person_strategy)
def test_tdt4250case::person_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=tdt4250case::Person_strategy)
def test_tdt4250case::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250case::Person_strategy)
def test_tdt4250case::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250case::CourseRole_strategy)
@settings(max_examples=50)
def test_tdt4250case::courserole_instantiation(instance):
    assert isinstance(instance, tdt4250case::CourseRole)

@given(instance=tdt4250case::CourseRole_strategy)
def test_tdt4250case::courserole_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250case::CourseRole_strategy)
def test_tdt4250case::courserole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250case::Department_strategy)
@settings(max_examples=50)
def test_tdt4250case::department_instantiation(instance):
    assert isinstance(instance, tdt4250case::Department)

@given(instance=tdt4250case::Department_strategy)
def test_tdt4250case::department_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=tdt4250case::Department_strategy)
def test_tdt4250case::department_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=tdt4250case::Department_strategy)
def test_tdt4250case::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250case::Department_strategy)
def test_tdt4250case::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250case::Timetable_strategy)
@settings(max_examples=50)
def test_tdt4250case::timetable_instantiation(instance):
    assert isinstance(instance, tdt4250case::Timetable)

@given(instance=tdt4250case::Examination_strategy)
@settings(max_examples=50)
def test_tdt4250case::examination_instantiation(instance):
    assert isinstance(instance, tdt4250case::Examination)
