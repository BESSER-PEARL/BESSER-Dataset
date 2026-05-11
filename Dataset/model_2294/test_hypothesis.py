import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scheduleOfCourse::scheduleOfCourse,
    scheduleOfCourse::TopLevelSpace,
    scheduleOfCourse::Capacity,
    scheduleOfCourse::CourseLoad,
    scheduleOfCourse::LessonPeriod,
    scheduleOfCourse::Room,
    scheduleOfCourse::Lesson,
    scheduleOfCourse::Occupation,
    scheduleOfCourse::Shift,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scheduleofcourse::scheduleofcourse_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::scheduleOfCourse)


def test_scheduleofcourse::scheduleofcourse_constructor_exists():
    assert callable(scheduleOfCourse::scheduleOfCourse.__init__)


def test_scheduleofcourse::scheduleofcourse_constructor_args():
    sig = inspect.signature(scheduleOfCourse::scheduleOfCourse.__init__)
    params = list(sig.parameters.keys())



def test_scheduleofcourse::toplevelspace_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::TopLevelSpace)


def test_scheduleofcourse::toplevelspace_constructor_exists():
    assert callable(scheduleOfCourse::TopLevelSpace.__init__)


def test_scheduleofcourse::toplevelspace_constructor_args():
    sig = inspect.signature(scheduleOfCourse::TopLevelSpace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_scheduleofcourse::toplevelspace_has_name():
    assert hasattr(scheduleOfCourse::TopLevelSpace, "name")
    descriptor = None
    for klass in scheduleOfCourse::TopLevelSpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::toplevelspace_has_type():
    assert hasattr(scheduleOfCourse::TopLevelSpace, "type")
    descriptor = None
    for klass in scheduleOfCourse::TopLevelSpace.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::toplevelspace_has_id():
    assert hasattr(scheduleOfCourse::TopLevelSpace, "id")
    descriptor = None
    for klass in scheduleOfCourse::TopLevelSpace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::capacity_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::Capacity)


def test_scheduleofcourse::capacity_constructor_exists():
    assert callable(scheduleOfCourse::Capacity.__init__)


def test_scheduleofcourse::capacity_constructor_args():
    sig = inspect.signature(scheduleOfCourse::Capacity.__init__)
    params = list(sig.parameters.keys())
    assert "exam" in params, "Missing parameter 'exam'"
    assert "normal" in params, "Missing parameter 'normal'"

def test_scheduleofcourse::capacity_has_exam():
    assert hasattr(scheduleOfCourse::Capacity, "exam")
    descriptor = None
    for klass in scheduleOfCourse::Capacity.__mro__:
        if "exam" in klass.__dict__:
            descriptor = klass.__dict__["exam"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::capacity_has_normal():
    assert hasattr(scheduleOfCourse::Capacity, "normal")
    descriptor = None
    for klass in scheduleOfCourse::Capacity.__mro__:
        if "normal" in klass.__dict__:
            descriptor = klass.__dict__["normal"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::courseload_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::CourseLoad)


def test_scheduleofcourse::courseload_constructor_exists():
    assert callable(scheduleOfCourse::CourseLoad.__init__)


def test_scheduleofcourse::courseload_constructor_args():
    sig = inspect.signature(scheduleOfCourse::CourseLoad.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "totalQuantity" in params, "Missing parameter 'totalQuantity'"
    assert "unitQuantity" in params, "Missing parameter 'unitQuantity'"

def test_scheduleofcourse::courseload_has_type():
    assert hasattr(scheduleOfCourse::CourseLoad, "type")
    descriptor = None
    for klass in scheduleOfCourse::CourseLoad.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::courseload_has_totalQuantity():
    assert hasattr(scheduleOfCourse::CourseLoad, "totalQuantity")
    descriptor = None
    for klass in scheduleOfCourse::CourseLoad.__mro__:
        if "totalQuantity" in klass.__dict__:
            descriptor = klass.__dict__["totalQuantity"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::courseload_has_unitQuantity():
    assert hasattr(scheduleOfCourse::CourseLoad, "unitQuantity")
    descriptor = None
    for klass in scheduleOfCourse::CourseLoad.__mro__:
        if "unitQuantity" in klass.__dict__:
            descriptor = klass.__dict__["unitQuantity"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::lessonperiod_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::LessonPeriod)


def test_scheduleofcourse::lessonperiod_constructor_exists():
    assert callable(scheduleOfCourse::LessonPeriod.__init__)


def test_scheduleofcourse::lessonperiod_constructor_args():
    sig = inspect.signature(scheduleOfCourse::LessonPeriod.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_scheduleofcourse::lessonperiod_has_start():
    assert hasattr(scheduleOfCourse::LessonPeriod, "start")
    descriptor = None
    for klass in scheduleOfCourse::LessonPeriod.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::lessonperiod_has_end():
    assert hasattr(scheduleOfCourse::LessonPeriod, "end")
    descriptor = None
    for klass in scheduleOfCourse::LessonPeriod.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::room_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::Room)


def test_scheduleofcourse::room_constructor_exists():
    assert callable(scheduleOfCourse::Room.__init__)


def test_scheduleofcourse::room_constructor_args():
    sig = inspect.signature(scheduleOfCourse::Room.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_scheduleofcourse::room_has_description():
    assert hasattr(scheduleOfCourse::Room, "description")
    descriptor = None
    for klass in scheduleOfCourse::Room.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::room_has_id():
    assert hasattr(scheduleOfCourse::Room, "id")
    descriptor = None
    for klass in scheduleOfCourse::Room.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::room_has_name():
    assert hasattr(scheduleOfCourse::Room, "name")
    descriptor = None
    for klass in scheduleOfCourse::Room.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::room_has_type():
    assert hasattr(scheduleOfCourse::Room, "type")
    descriptor = None
    for klass in scheduleOfCourse::Room.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::lesson_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::Lesson)


def test_scheduleofcourse::lesson_constructor_exists():
    assert callable(scheduleOfCourse::Lesson.__init__)


def test_scheduleofcourse::lesson_constructor_args():
    sig = inspect.signature(scheduleOfCourse::Lesson.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_scheduleofcourse::lesson_has_start():
    assert hasattr(scheduleOfCourse::Lesson, "start")
    descriptor = None
    for klass in scheduleOfCourse::Lesson.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::lesson_has_end():
    assert hasattr(scheduleOfCourse::Lesson, "end")
    descriptor = None
    for klass in scheduleOfCourse::Lesson.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::occupation_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::Occupation)


def test_scheduleofcourse::occupation_constructor_exists():
    assert callable(scheduleOfCourse::Occupation.__init__)


def test_scheduleofcourse::occupation_constructor_args():
    sig = inspect.signature(scheduleOfCourse::Occupation.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "current" in params, "Missing parameter 'current'"

def test_scheduleofcourse::occupation_has_max():
    assert hasattr(scheduleOfCourse::Occupation, "max")
    descriptor = None
    for klass in scheduleOfCourse::Occupation.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::occupation_has_current():
    assert hasattr(scheduleOfCourse::Occupation, "current")
    descriptor = None
    for klass in scheduleOfCourse::Occupation.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse::shift_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse::Shift)


def test_scheduleofcourse::shift_constructor_exists():
    assert callable(scheduleOfCourse::Shift.__init__)


def test_scheduleofcourse::shift_constructor_args():
    sig = inspect.signature(scheduleOfCourse::Shift.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"
    assert "name" in params, "Missing parameter 'name'"

def test_scheduleofcourse::shift_has_types():
    assert hasattr(scheduleOfCourse::Shift, "types")
    descriptor = None
    for klass in scheduleOfCourse::Shift.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse::shift_has_name():
    assert hasattr(scheduleOfCourse::Shift, "name")
    descriptor = None
    for klass in scheduleOfCourse::Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
scheduleOfCourse::scheduleOfCourse_strategy = st.builds(
    scheduleOfCourse::scheduleOfCourse,
)
scheduleOfCourse::TopLevelSpace_strategy = st.builds(
    scheduleOfCourse::TopLevelSpace,
    name=
        safe_text,
    type=
        safe_text,
    id=
        safe_text
)
scheduleOfCourse::Capacity_strategy = st.builds(
    scheduleOfCourse::Capacity,
    exam=
        st.integers(),
    normal=
        st.integers()
)
scheduleOfCourse::CourseLoad_strategy = st.builds(
    scheduleOfCourse::CourseLoad,
    type=
        safe_text,
    totalQuantity=
        st.integers(),
    unitQuantity=
        st.integers()
)
scheduleOfCourse::LessonPeriod_strategy = st.builds(
    scheduleOfCourse::LessonPeriod,
    start=
        safe_text,
    end=
        safe_text
)
scheduleOfCourse::Room_strategy = st.builds(
    scheduleOfCourse::Room,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
scheduleOfCourse::Lesson_strategy = st.builds(
    scheduleOfCourse::Lesson,
    start=
        safe_text,
    end=
        safe_text
)
scheduleOfCourse::Occupation_strategy = st.builds(
    scheduleOfCourse::Occupation,
    max=
        st.integers(),
    current=
        st.integers()
)
scheduleOfCourse::Shift_strategy = st.builds(
    scheduleOfCourse::Shift,
    types=
        safe_text,
    name=
        safe_text
)

@given(instance=scheduleOfCourse::scheduleOfCourse_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::scheduleofcourse_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::scheduleOfCourse)

@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::toplevelspace_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::TopLevelSpace)

@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
def test_scheduleofcourse::toplevelspace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
def test_scheduleofcourse::toplevelspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
def test_scheduleofcourse::toplevelspace_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
def test_scheduleofcourse::toplevelspace_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
def test_scheduleofcourse::toplevelspace_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scheduleOfCourse::TopLevelSpace_strategy)
def test_scheduleofcourse::toplevelspace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scheduleOfCourse::Capacity_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::capacity_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::Capacity)

@given(instance=scheduleOfCourse::Capacity_strategy)
def test_scheduleofcourse::capacity_exam_type(instance):
    assert isinstance(instance.exam, int)


@given(instance=scheduleOfCourse::Capacity_strategy)
def test_scheduleofcourse::capacity_exam_setter(instance):
    original = instance.exam
    instance.exam = original
    assert instance.exam == original

@given(instance=scheduleOfCourse::Capacity_strategy)
def test_scheduleofcourse::capacity_normal_type(instance):
    assert isinstance(instance.normal, int)


@given(instance=scheduleOfCourse::Capacity_strategy)
def test_scheduleofcourse::capacity_normal_setter(instance):
    original = instance.normal
    instance.normal = original
    assert instance.normal == original

@given(instance=scheduleOfCourse::CourseLoad_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::courseload_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::CourseLoad)

@given(instance=scheduleOfCourse::CourseLoad_strategy)
def test_scheduleofcourse::courseload_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scheduleOfCourse::CourseLoad_strategy)
def test_scheduleofcourse::courseload_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scheduleOfCourse::CourseLoad_strategy)
def test_scheduleofcourse::courseload_totalQuantity_type(instance):
    assert isinstance(instance.totalQuantity, int)


@given(instance=scheduleOfCourse::CourseLoad_strategy)
def test_scheduleofcourse::courseload_totalQuantity_setter(instance):
    original = instance.totalQuantity
    instance.totalQuantity = original
    assert instance.totalQuantity == original

@given(instance=scheduleOfCourse::CourseLoad_strategy)
def test_scheduleofcourse::courseload_unitQuantity_type(instance):
    assert isinstance(instance.unitQuantity, int)


@given(instance=scheduleOfCourse::CourseLoad_strategy)
def test_scheduleofcourse::courseload_unitQuantity_setter(instance):
    original = instance.unitQuantity
    instance.unitQuantity = original
    assert instance.unitQuantity == original

@given(instance=scheduleOfCourse::LessonPeriod_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::lessonperiod_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::LessonPeriod)

@given(instance=scheduleOfCourse::LessonPeriod_strategy)
def test_scheduleofcourse::lessonperiod_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=scheduleOfCourse::LessonPeriod_strategy)
def test_scheduleofcourse::lessonperiod_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=scheduleOfCourse::LessonPeriod_strategy)
def test_scheduleofcourse::lessonperiod_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=scheduleOfCourse::LessonPeriod_strategy)
def test_scheduleofcourse::lessonperiod_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=scheduleOfCourse::Room_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::room_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::Room)

@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scheduleOfCourse::Room_strategy)
def test_scheduleofcourse::room_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scheduleOfCourse::Lesson_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::lesson_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::Lesson)

@given(instance=scheduleOfCourse::Lesson_strategy)
def test_scheduleofcourse::lesson_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=scheduleOfCourse::Lesson_strategy)
def test_scheduleofcourse::lesson_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=scheduleOfCourse::Lesson_strategy)
def test_scheduleofcourse::lesson_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=scheduleOfCourse::Lesson_strategy)
def test_scheduleofcourse::lesson_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=scheduleOfCourse::Occupation_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::occupation_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::Occupation)

@given(instance=scheduleOfCourse::Occupation_strategy)
def test_scheduleofcourse::occupation_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=scheduleOfCourse::Occupation_strategy)
def test_scheduleofcourse::occupation_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=scheduleOfCourse::Occupation_strategy)
def test_scheduleofcourse::occupation_current_type(instance):
    assert isinstance(instance.current, int)


@given(instance=scheduleOfCourse::Occupation_strategy)
def test_scheduleofcourse::occupation_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=scheduleOfCourse::Shift_strategy)
@settings(max_examples=50)
def test_scheduleofcourse::shift_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse::Shift)

@given(instance=scheduleOfCourse::Shift_strategy)
def test_scheduleofcourse::shift_types_type(instance):
    assert isinstance(instance.types, str)


@given(instance=scheduleOfCourse::Shift_strategy)
def test_scheduleofcourse::shift_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=scheduleOfCourse::Shift_strategy)
def test_scheduleofcourse::shift_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scheduleOfCourse::Shift_strategy)
def test_scheduleofcourse::shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
