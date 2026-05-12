import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tdt4250case_ScheduledActivity,
    tdt4250case_ExaminationActivity,
    tdt4250case_CourseWork,
    tdt4250case_CourseInstance,
    tdt4250case_CreditReductionCourse,
    tdt4250case_Studyprogram,
    tdt4250case_Course,
    tdt4250case_Person,
    tdt4250case_CourseRole,
    tdt4250case_Department,
    tdt4250case_Timetable,
    tdt4250case_Examination,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tdt4250case_scheduledactivity_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_ScheduledActivity)


def test_tdt4250case_scheduledactivity_constructor_exists():
    assert callable(tdt4250case_ScheduledActivity.__init__)


def test_tdt4250case_scheduledactivity_constructor_args():
    sig = inspect.signature(tdt4250case_ScheduledActivity.__init__)
    params = list(sig.parameters.keys())
    assert "room" in params, "Missing parameter 'room'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "timeslot" in params, "Missing parameter 'timeslot'"

def test_tdt4250case_scheduledactivity_has_room():
    assert hasattr(tdt4250case_ScheduledActivity, "room")
    descriptor = None
    for klass in tdt4250case_ScheduledActivity.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_scheduledactivity_has_activity():
    assert hasattr(tdt4250case_ScheduledActivity, "activity")
    descriptor = None
    for klass in tdt4250case_ScheduledActivity.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_scheduledactivity_has_timeslot():
    assert hasattr(tdt4250case_ScheduledActivity, "timeslot")
    descriptor = None
    for klass in tdt4250case_ScheduledActivity.__mro__:
        if "timeslot" in klass.__dict__:
            descriptor = klass.__dict__["timeslot"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_examinationactivity_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_ExaminationActivity)


def test_tdt4250case_examinationactivity_constructor_exists():
    assert callable(tdt4250case_ExaminationActivity.__init__)


def test_tdt4250case_examinationactivity_constructor_args():
    sig = inspect.signature(tdt4250case_ExaminationActivity.__init__)
    params = list(sig.parameters.keys())
    assert "evaluationForm" in params, "Missing parameter 'evaluationForm'"
    assert "weighting" in params, "Missing parameter 'weighting'"

def test_tdt4250case_examinationactivity_has_evaluationForm():
    assert hasattr(tdt4250case_ExaminationActivity, "evaluationForm")
    descriptor = None
    for klass in tdt4250case_ExaminationActivity.__mro__:
        if "evaluationForm" in klass.__dict__:
            descriptor = klass.__dict__["evaluationForm"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_examinationactivity_has_weighting():
    assert hasattr(tdt4250case_ExaminationActivity, "weighting")
    descriptor = None
    for klass in tdt4250case_ExaminationActivity.__mro__:
        if "weighting" in klass.__dict__:
            descriptor = klass.__dict__["weighting"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_coursework_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_CourseWork)


def test_tdt4250case_coursework_constructor_exists():
    assert callable(tdt4250case_CourseWork.__init__)


def test_tdt4250case_coursework_constructor_args():
    sig = inspect.signature(tdt4250case_CourseWork.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "hours" in params, "Missing parameter 'hours'"

def test_tdt4250case_coursework_has_type():
    assert hasattr(tdt4250case_CourseWork, "type")
    descriptor = None
    for klass in tdt4250case_CourseWork.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_coursework_has_hours():
    assert hasattr(tdt4250case_CourseWork, "hours")
    descriptor = None
    for klass in tdt4250case_CourseWork.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_courseinstance_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_CourseInstance)


def test_tdt4250case_courseinstance_constructor_exists():
    assert callable(tdt4250case_CourseInstance.__init__)


def test_tdt4250case_courseinstance_constructor_args():
    sig = inspect.signature(tdt4250case_CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"

def test_tdt4250case_courseinstance_has_semester():
    assert hasattr(tdt4250case_CourseInstance, "semester")
    descriptor = None
    for klass in tdt4250case_CourseInstance.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_creditreductioncourse_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_CreditReductionCourse)


def test_tdt4250case_creditreductioncourse_constructor_exists():
    assert callable(tdt4250case_CreditReductionCourse.__init__)


def test_tdt4250case_creditreductioncourse_constructor_args():
    sig = inspect.signature(tdt4250case_CreditReductionCourse.__init__)
    params = list(sig.parameters.keys())
    assert "reduction" in params, "Missing parameter 'reduction'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"

def test_tdt4250case_creditreductioncourse_has_reduction():
    assert hasattr(tdt4250case_CreditReductionCourse, "reduction")
    descriptor = None
    for klass in tdt4250case_CreditReductionCourse.__mro__:
        if "reduction" in klass.__dict__:
            descriptor = klass.__dict__["reduction"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_creditreductioncourse_has_from_():
    assert hasattr(tdt4250case_CreditReductionCourse, "from_")
    descriptor = None
    for klass in tdt4250case_CreditReductionCourse.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_creditreductioncourse_has_to():
    assert hasattr(tdt4250case_CreditReductionCourse, "to")
    descriptor = None
    for klass in tdt4250case_CreditReductionCourse.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_studyprogram_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_Studyprogram)


def test_tdt4250case_studyprogram_constructor_exists():
    assert callable(tdt4250case_Studyprogram.__init__)


def test_tdt4250case_studyprogram_constructor_args():
    sig = inspect.signature(tdt4250case_Studyprogram.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_tdt4250case_studyprogram_has_code():
    assert hasattr(tdt4250case_Studyprogram, "code")
    descriptor = None
    for klass in tdt4250case_Studyprogram.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_course_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_Course)


def test_tdt4250case_course_constructor_exists():
    assert callable(tdt4250case_Course.__init__)


def test_tdt4250case_course_constructor_args():
    sig = inspect.signature(tdt4250case_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "content" in params, "Missing parameter 'content'"

def test_tdt4250case_course_has_code():
    assert hasattr(tdt4250case_Course, "code")
    descriptor = None
    for klass in tdt4250case_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_course_has_name():
    assert hasattr(tdt4250case_Course, "name")
    descriptor = None
    for klass in tdt4250case_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_course_has_credits():
    assert hasattr(tdt4250case_Course, "credits")
    descriptor = None
    for klass in tdt4250case_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_course_has_content():
    assert hasattr(tdt4250case_Course, "content")
    descriptor = None
    for klass in tdt4250case_Course.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_person_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_Person)


def test_tdt4250case_person_constructor_exists():
    assert callable(tdt4250case_Person.__init__)


def test_tdt4250case_person_constructor_args():
    sig = inspect.signature(tdt4250case_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "username" in params, "Missing parameter 'username'"

def test_tdt4250case_person_has_name():
    assert hasattr(tdt4250case_Person, "name")
    descriptor = None
    for klass in tdt4250case_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_person_has_username():
    assert hasattr(tdt4250case_Person, "username")
    descriptor = None
    for klass in tdt4250case_Person.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_courserole_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_CourseRole)


def test_tdt4250case_courserole_constructor_exists():
    assert callable(tdt4250case_CourseRole.__init__)


def test_tdt4250case_courserole_constructor_args():
    sig = inspect.signature(tdt4250case_CourseRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250case_courserole_has_name():
    assert hasattr(tdt4250case_CourseRole, "name")
    descriptor = None
    for klass in tdt4250case_CourseRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_department_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_Department)


def test_tdt4250case_department_constructor_exists():
    assert callable(tdt4250case_Department.__init__)


def test_tdt4250case_department_constructor_args():
    sig = inspect.signature(tdt4250case_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_tdt4250case_department_has_name():
    assert hasattr(tdt4250case_Department, "name")
    descriptor = None
    for klass in tdt4250case_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250case_department_has_code():
    assert hasattr(tdt4250case_Department, "code")
    descriptor = None
    for klass in tdt4250case_Department.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250case_timetable_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_Timetable)


def test_tdt4250case_timetable_constructor_exists():
    assert callable(tdt4250case_Timetable.__init__)


def test_tdt4250case_timetable_constructor_args():
    sig = inspect.signature(tdt4250case_Timetable.__init__)
    params = list(sig.parameters.keys())



def test_tdt4250case_examination_is_not_abstract():
    assert not inspect.isabstract(tdt4250case_Examination)


def test_tdt4250case_examination_constructor_exists():
    assert callable(tdt4250case_Examination.__init__)


def test_tdt4250case_examination_constructor_args():
    sig = inspect.signature(tdt4250case_Examination.__init__)
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
tdt4250case_ScheduledActivity_strategy = st.builds(
    tdt4250case_ScheduledActivity,
    room=
        safe_text,
    activity=
        safe_text,
    timeslot=
        safe_text
)
tdt4250case_ExaminationActivity_strategy = st.builds(
    tdt4250case_ExaminationActivity,
    evaluationForm=
        safe_text,
    weighting=
        safe_text
)
tdt4250case_CourseWork_strategy = st.builds(
    tdt4250case_CourseWork,
    type=
        safe_text,
    hours=
        st.integers()
)
tdt4250case_CourseInstance_strategy = st.builds(
    tdt4250case_CourseInstance,
    semester=
        safe_text
)
tdt4250case_CreditReductionCourse_strategy = st.builds(
    tdt4250case_CreditReductionCourse,
    reduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    from_=
        st.dates(),
    to=
        st.dates()
)
tdt4250case_Studyprogram_strategy = st.builds(
    tdt4250case_Studyprogram,
    code=
        safe_text
)
tdt4250case_Course_strategy = st.builds(
    tdt4250case_Course,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    content=
        safe_text
)
tdt4250case_Person_strategy = st.builds(
    tdt4250case_Person,
    name=
        safe_text,
    username=
        safe_text
)
tdt4250case_CourseRole_strategy = st.builds(
    tdt4250case_CourseRole,
    name=
        safe_text
)
tdt4250case_Department_strategy = st.builds(
    tdt4250case_Department,
    name=
        safe_text,
    code=
        safe_text
)
tdt4250case_Timetable_strategy = st.builds(
    tdt4250case_Timetable,
)
tdt4250case_Examination_strategy = st.builds(
    tdt4250case_Examination,
)

@given(instance=tdt4250case_ScheduledActivity_strategy)
@settings(max_examples=50)
def test_tdt4250case_scheduledactivity_instantiation(instance):
    assert isinstance(instance, tdt4250case_ScheduledActivity)



@given(instance=tdt4250case_ScheduledActivity_strategy)
def test_tdt4250case_scheduledactivity_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=tdt4250case_ScheduledActivity_strategy)
def test_tdt4250case_scheduledactivity_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=tdt4250case_ScheduledActivity_strategy)
def test_tdt4250case_scheduledactivity_timeslot_setter(instance):
    original = instance.timeslot
    instance.timeslot = original
    assert instance.timeslot == original

@given(instance=tdt4250case_ExaminationActivity_strategy)
@settings(max_examples=50)
def test_tdt4250case_examinationactivity_instantiation(instance):
    assert isinstance(instance, tdt4250case_ExaminationActivity)



@given(instance=tdt4250case_ExaminationActivity_strategy)
def test_tdt4250case_examinationactivity_evaluationForm_setter(instance):
    original = instance.evaluationForm
    instance.evaluationForm = original
    assert instance.evaluationForm == original



@given(instance=tdt4250case_ExaminationActivity_strategy)
def test_tdt4250case_examinationactivity_weighting_setter(instance):
    original = instance.weighting
    instance.weighting = original
    assert instance.weighting == original

@given(instance=tdt4250case_CourseWork_strategy)
@settings(max_examples=50)
def test_tdt4250case_coursework_instantiation(instance):
    assert isinstance(instance, tdt4250case_CourseWork)



@given(instance=tdt4250case_CourseWork_strategy)
def test_tdt4250case_coursework_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=tdt4250case_CourseWork_strategy)
def test_tdt4250case_coursework_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original

@given(instance=tdt4250case_CourseInstance_strategy)
@settings(max_examples=50)
def test_tdt4250case_courseinstance_instantiation(instance):
    assert isinstance(instance, tdt4250case_CourseInstance)



@given(instance=tdt4250case_CourseInstance_strategy)
def test_tdt4250case_courseinstance_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=tdt4250case_CreditReductionCourse_strategy)
@settings(max_examples=50)
def test_tdt4250case_creditreductioncourse_instantiation(instance):
    assert isinstance(instance, tdt4250case_CreditReductionCourse)



@given(instance=tdt4250case_CreditReductionCourse_strategy)
def test_tdt4250case_creditreductioncourse_reduction_setter(instance):
    original = instance.reduction
    instance.reduction = original
    assert instance.reduction == original



@given(instance=tdt4250case_CreditReductionCourse_strategy)
def test_tdt4250case_creditreductioncourse_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=tdt4250case_CreditReductionCourse_strategy)
def test_tdt4250case_creditreductioncourse_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=tdt4250case_Studyprogram_strategy)
@settings(max_examples=50)
def test_tdt4250case_studyprogram_instantiation(instance):
    assert isinstance(instance, tdt4250case_Studyprogram)



@given(instance=tdt4250case_Studyprogram_strategy)
def test_tdt4250case_studyprogram_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=tdt4250case_Course_strategy)
@settings(max_examples=50)
def test_tdt4250case_course_instantiation(instance):
    assert isinstance(instance, tdt4250case_Course)



@given(instance=tdt4250case_Course_strategy)
def test_tdt4250case_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=tdt4250case_Course_strategy)
def test_tdt4250case_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250case_Course_strategy)
def test_tdt4250case_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=tdt4250case_Course_strategy)
def test_tdt4250case_course_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=tdt4250case_Person_strategy)
@settings(max_examples=50)
def test_tdt4250case_person_instantiation(instance):
    assert isinstance(instance, tdt4250case_Person)



@given(instance=tdt4250case_Person_strategy)
def test_tdt4250case_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250case_Person_strategy)
def test_tdt4250case_person_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=tdt4250case_CourseRole_strategy)
@settings(max_examples=50)
def test_tdt4250case_courserole_instantiation(instance):
    assert isinstance(instance, tdt4250case_CourseRole)



@given(instance=tdt4250case_CourseRole_strategy)
def test_tdt4250case_courserole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250case_Department_strategy)
@settings(max_examples=50)
def test_tdt4250case_department_instantiation(instance):
    assert isinstance(instance, tdt4250case_Department)



@given(instance=tdt4250case_Department_strategy)
def test_tdt4250case_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250case_Department_strategy)
def test_tdt4250case_department_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=tdt4250case_Timetable_strategy)
@settings(max_examples=50)
def test_tdt4250case_timetable_instantiation(instance):
    assert isinstance(instance, tdt4250case_Timetable)

@given(instance=tdt4250case_Examination_strategy)
@settings(max_examples=50)
def test_tdt4250case_examination_instantiation(instance):
    assert isinstance(instance, tdt4250case_Examination)
