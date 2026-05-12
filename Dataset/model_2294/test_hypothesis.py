import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scheduleOfCourse_scheduleOfCourse,
    scheduleOfCourse_TopLevelSpace,
    scheduleOfCourse_Capacity,
    scheduleOfCourse_CourseLoad,
    scheduleOfCourse_LessonPeriod,
    scheduleOfCourse_Room,
    scheduleOfCourse_Lesson,
    scheduleOfCourse_Occupation,
    scheduleOfCourse_Shift,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scheduleofcourse_scheduleofcourse_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_scheduleOfCourse)


def test_scheduleofcourse_scheduleofcourse_constructor_exists():
    assert callable(scheduleOfCourse_scheduleOfCourse.__init__)


def test_scheduleofcourse_scheduleofcourse_constructor_args():
    sig = inspect.signature(scheduleOfCourse_scheduleOfCourse.__init__)
    params = list(sig.parameters.keys())



def test_scheduleofcourse_toplevelspace_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_TopLevelSpace)


def test_scheduleofcourse_toplevelspace_constructor_exists():
    assert callable(scheduleOfCourse_TopLevelSpace.__init__)


def test_scheduleofcourse_toplevelspace_constructor_args():
    sig = inspect.signature(scheduleOfCourse_TopLevelSpace.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_scheduleofcourse_toplevelspace_has_id():
    assert hasattr(scheduleOfCourse_TopLevelSpace, "id")
    descriptor = None
    for klass in scheduleOfCourse_TopLevelSpace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_toplevelspace_has_type():
    assert hasattr(scheduleOfCourse_TopLevelSpace, "type")
    descriptor = None
    for klass in scheduleOfCourse_TopLevelSpace.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_toplevelspace_has_name():
    assert hasattr(scheduleOfCourse_TopLevelSpace, "name")
    descriptor = None
    for klass in scheduleOfCourse_TopLevelSpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_capacity_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_Capacity)


def test_scheduleofcourse_capacity_constructor_exists():
    assert callable(scheduleOfCourse_Capacity.__init__)


def test_scheduleofcourse_capacity_constructor_args():
    sig = inspect.signature(scheduleOfCourse_Capacity.__init__)
    params = list(sig.parameters.keys())
    assert "exam" in params, "Missing parameter 'exam'"
    assert "normal" in params, "Missing parameter 'normal'"

def test_scheduleofcourse_capacity_has_exam():
    assert hasattr(scheduleOfCourse_Capacity, "exam")
    descriptor = None
    for klass in scheduleOfCourse_Capacity.__mro__:
        if "exam" in klass.__dict__:
            descriptor = klass.__dict__["exam"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_capacity_has_normal():
    assert hasattr(scheduleOfCourse_Capacity, "normal")
    descriptor = None
    for klass in scheduleOfCourse_Capacity.__mro__:
        if "normal" in klass.__dict__:
            descriptor = klass.__dict__["normal"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_courseload_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_CourseLoad)


def test_scheduleofcourse_courseload_constructor_exists():
    assert callable(scheduleOfCourse_CourseLoad.__init__)


def test_scheduleofcourse_courseload_constructor_args():
    sig = inspect.signature(scheduleOfCourse_CourseLoad.__init__)
    params = list(sig.parameters.keys())
    assert "totalQuantity" in params, "Missing parameter 'totalQuantity'"
    assert "unitQuantity" in params, "Missing parameter 'unitQuantity'"
    assert "type" in params, "Missing parameter 'type'"

def test_scheduleofcourse_courseload_has_totalQuantity():
    assert hasattr(scheduleOfCourse_CourseLoad, "totalQuantity")
    descriptor = None
    for klass in scheduleOfCourse_CourseLoad.__mro__:
        if "totalQuantity" in klass.__dict__:
            descriptor = klass.__dict__["totalQuantity"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_courseload_has_unitQuantity():
    assert hasattr(scheduleOfCourse_CourseLoad, "unitQuantity")
    descriptor = None
    for klass in scheduleOfCourse_CourseLoad.__mro__:
        if "unitQuantity" in klass.__dict__:
            descriptor = klass.__dict__["unitQuantity"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_courseload_has_type():
    assert hasattr(scheduleOfCourse_CourseLoad, "type")
    descriptor = None
    for klass in scheduleOfCourse_CourseLoad.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_lessonperiod_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_LessonPeriod)


def test_scheduleofcourse_lessonperiod_constructor_exists():
    assert callable(scheduleOfCourse_LessonPeriod.__init__)


def test_scheduleofcourse_lessonperiod_constructor_args():
    sig = inspect.signature(scheduleOfCourse_LessonPeriod.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_scheduleofcourse_lessonperiod_has_start():
    assert hasattr(scheduleOfCourse_LessonPeriod, "start")
    descriptor = None
    for klass in scheduleOfCourse_LessonPeriod.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_lessonperiod_has_end():
    assert hasattr(scheduleOfCourse_LessonPeriod, "end")
    descriptor = None
    for klass in scheduleOfCourse_LessonPeriod.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_room_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_Room)


def test_scheduleofcourse_room_constructor_exists():
    assert callable(scheduleOfCourse_Room.__init__)


def test_scheduleofcourse_room_constructor_args():
    sig = inspect.signature(scheduleOfCourse_Room.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_scheduleofcourse_room_has_type():
    assert hasattr(scheduleOfCourse_Room, "type")
    descriptor = None
    for klass in scheduleOfCourse_Room.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_room_has_id():
    assert hasattr(scheduleOfCourse_Room, "id")
    descriptor = None
    for klass in scheduleOfCourse_Room.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_room_has_description():
    assert hasattr(scheduleOfCourse_Room, "description")
    descriptor = None
    for klass in scheduleOfCourse_Room.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_room_has_name():
    assert hasattr(scheduleOfCourse_Room, "name")
    descriptor = None
    for klass in scheduleOfCourse_Room.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_lesson_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_Lesson)


def test_scheduleofcourse_lesson_constructor_exists():
    assert callable(scheduleOfCourse_Lesson.__init__)


def test_scheduleofcourse_lesson_constructor_args():
    sig = inspect.signature(scheduleOfCourse_Lesson.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_scheduleofcourse_lesson_has_end():
    assert hasattr(scheduleOfCourse_Lesson, "end")
    descriptor = None
    for klass in scheduleOfCourse_Lesson.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_lesson_has_start():
    assert hasattr(scheduleOfCourse_Lesson, "start")
    descriptor = None
    for klass in scheduleOfCourse_Lesson.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_occupation_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_Occupation)


def test_scheduleofcourse_occupation_constructor_exists():
    assert callable(scheduleOfCourse_Occupation.__init__)


def test_scheduleofcourse_occupation_constructor_args():
    sig = inspect.signature(scheduleOfCourse_Occupation.__init__)
    params = list(sig.parameters.keys())
    assert "current" in params, "Missing parameter 'current'"
    assert "max" in params, "Missing parameter 'max'"

def test_scheduleofcourse_occupation_has_current():
    assert hasattr(scheduleOfCourse_Occupation, "current")
    descriptor = None
    for klass in scheduleOfCourse_Occupation.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_occupation_has_max():
    assert hasattr(scheduleOfCourse_Occupation, "max")
    descriptor = None
    for klass in scheduleOfCourse_Occupation.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_scheduleofcourse_shift_is_not_abstract():
    assert not inspect.isabstract(scheduleOfCourse_Shift)


def test_scheduleofcourse_shift_constructor_exists():
    assert callable(scheduleOfCourse_Shift.__init__)


def test_scheduleofcourse_shift_constructor_args():
    sig = inspect.signature(scheduleOfCourse_Shift.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "types" in params, "Missing parameter 'types'"

def test_scheduleofcourse_shift_has_name():
    assert hasattr(scheduleOfCourse_Shift, "name")
    descriptor = None
    for klass in scheduleOfCourse_Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scheduleofcourse_shift_has_types():
    assert hasattr(scheduleOfCourse_Shift, "types")
    descriptor = None
    for klass in scheduleOfCourse_Shift.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
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
scheduleOfCourse_scheduleOfCourse_strategy = st.builds(
    scheduleOfCourse_scheduleOfCourse,
)
scheduleOfCourse_TopLevelSpace_strategy = st.builds(
    scheduleOfCourse_TopLevelSpace,
    id=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
scheduleOfCourse_Capacity_strategy = st.builds(
    scheduleOfCourse_Capacity,
    exam=
        st.integers(),
    normal=
        st.integers()
)
scheduleOfCourse_CourseLoad_strategy = st.builds(
    scheduleOfCourse_CourseLoad,
    totalQuantity=
        st.integers(),
    unitQuantity=
        st.integers(),
    type=
        safe_text
)
scheduleOfCourse_LessonPeriod_strategy = st.builds(
    scheduleOfCourse_LessonPeriod,
    start=
        safe_text,
    end=
        safe_text
)
scheduleOfCourse_Room_strategy = st.builds(
    scheduleOfCourse_Room,
    type=
        safe_text,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
scheduleOfCourse_Lesson_strategy = st.builds(
    scheduleOfCourse_Lesson,
    end=
        safe_text,
    start=
        safe_text
)
scheduleOfCourse_Occupation_strategy = st.builds(
    scheduleOfCourse_Occupation,
    current=
        st.integers(),
    max=
        st.integers()
)
scheduleOfCourse_Shift_strategy = st.builds(
    scheduleOfCourse_Shift,
    name=
        safe_text,
    types=
        safe_text
)

@given(instance=scheduleOfCourse_scheduleOfCourse_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_scheduleofcourse_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_scheduleOfCourse)

@given(instance=scheduleOfCourse_TopLevelSpace_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_toplevelspace_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_TopLevelSpace)



@given(instance=scheduleOfCourse_TopLevelSpace_strategy)
def test_scheduleofcourse_toplevelspace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scheduleOfCourse_TopLevelSpace_strategy)
def test_scheduleofcourse_toplevelspace_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scheduleOfCourse_TopLevelSpace_strategy)
def test_scheduleofcourse_toplevelspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scheduleOfCourse_Capacity_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_capacity_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Capacity)



@given(instance=scheduleOfCourse_Capacity_strategy)
def test_scheduleofcourse_capacity_exam_setter(instance):
    original = instance.exam
    instance.exam = original
    assert instance.exam == original



@given(instance=scheduleOfCourse_Capacity_strategy)
def test_scheduleofcourse_capacity_normal_setter(instance):
    original = instance.normal
    instance.normal = original
    assert instance.normal == original

@given(instance=scheduleOfCourse_CourseLoad_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_courseload_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_CourseLoad)



@given(instance=scheduleOfCourse_CourseLoad_strategy)
def test_scheduleofcourse_courseload_totalQuantity_setter(instance):
    original = instance.totalQuantity
    instance.totalQuantity = original
    assert instance.totalQuantity == original



@given(instance=scheduleOfCourse_CourseLoad_strategy)
def test_scheduleofcourse_courseload_unitQuantity_setter(instance):
    original = instance.unitQuantity
    instance.unitQuantity = original
    assert instance.unitQuantity == original



@given(instance=scheduleOfCourse_CourseLoad_strategy)
def test_scheduleofcourse_courseload_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scheduleOfCourse_LessonPeriod_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_lessonperiod_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_LessonPeriod)



@given(instance=scheduleOfCourse_LessonPeriod_strategy)
def test_scheduleofcourse_lessonperiod_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=scheduleOfCourse_LessonPeriod_strategy)
def test_scheduleofcourse_lessonperiod_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=scheduleOfCourse_Room_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_room_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Room)



@given(instance=scheduleOfCourse_Room_strategy)
def test_scheduleofcourse_room_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scheduleOfCourse_Room_strategy)
def test_scheduleofcourse_room_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scheduleOfCourse_Room_strategy)
def test_scheduleofcourse_room_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=scheduleOfCourse_Room_strategy)
def test_scheduleofcourse_room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scheduleOfCourse_Lesson_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_lesson_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Lesson)



@given(instance=scheduleOfCourse_Lesson_strategy)
def test_scheduleofcourse_lesson_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=scheduleOfCourse_Lesson_strategy)
def test_scheduleofcourse_lesson_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=scheduleOfCourse_Occupation_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_occupation_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Occupation)



@given(instance=scheduleOfCourse_Occupation_strategy)
def test_scheduleofcourse_occupation_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original



@given(instance=scheduleOfCourse_Occupation_strategy)
def test_scheduleofcourse_occupation_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=scheduleOfCourse_Shift_strategy)
@settings(max_examples=50)
def test_scheduleofcourse_shift_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Shift)



@given(instance=scheduleOfCourse_Shift_strategy)
def test_scheduleofcourse_shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=scheduleOfCourse_Shift_strategy)
def test_scheduleofcourse_shift_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original
