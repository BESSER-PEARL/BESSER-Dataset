import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fenix::scheduleOfCourse,
    fenix::Capacity,
    fenix::CourseLoad,
    fenix::LessonPeriod,
    fenix::Occupation,
    fenix::Shift,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fenix::scheduleofcourse_is_not_abstract():
    assert not inspect.isabstract(fenix::scheduleOfCourse)


def test_fenix::scheduleofcourse_constructor_exists():
    assert callable(fenix::scheduleOfCourse.__init__)


def test_fenix::scheduleofcourse_constructor_args():
    sig = inspect.signature(fenix::scheduleOfCourse.__init__)
    params = list(sig.parameters.keys())



def test_fenix::capacity_is_not_abstract():
    assert not inspect.isabstract(fenix::Capacity)


def test_fenix::capacity_constructor_exists():
    assert callable(fenix::Capacity.__init__)


def test_fenix::capacity_constructor_args():
    sig = inspect.signature(fenix::Capacity.__init__)
    params = list(sig.parameters.keys())
    assert "normal" in params, "Missing parameter 'normal'"
    assert "exam" in params, "Missing parameter 'exam'"

def test_fenix::capacity_has_normal():
    assert hasattr(fenix::Capacity, "normal")
    descriptor = None
    for klass in fenix::Capacity.__mro__:
        if "normal" in klass.__dict__:
            descriptor = klass.__dict__["normal"]
            break
    assert isinstance(descriptor, property)

def test_fenix::capacity_has_exam():
    assert hasattr(fenix::Capacity, "exam")
    descriptor = None
    for klass in fenix::Capacity.__mro__:
        if "exam" in klass.__dict__:
            descriptor = klass.__dict__["exam"]
            break
    assert isinstance(descriptor, property)



def test_fenix::courseload_is_not_abstract():
    assert not inspect.isabstract(fenix::CourseLoad)


def test_fenix::courseload_constructor_exists():
    assert callable(fenix::CourseLoad.__init__)


def test_fenix::courseload_constructor_args():
    sig = inspect.signature(fenix::CourseLoad.__init__)
    params = list(sig.parameters.keys())
    assert "totalQuantity" in params, "Missing parameter 'totalQuantity'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unitQuantity" in params, "Missing parameter 'unitQuantity'"

def test_fenix::courseload_has_totalQuantity():
    assert hasattr(fenix::CourseLoad, "totalQuantity")
    descriptor = None
    for klass in fenix::CourseLoad.__mro__:
        if "totalQuantity" in klass.__dict__:
            descriptor = klass.__dict__["totalQuantity"]
            break
    assert isinstance(descriptor, property)

def test_fenix::courseload_has_id():
    assert hasattr(fenix::CourseLoad, "id")
    descriptor = None
    for klass in fenix::CourseLoad.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fenix::courseload_has_description():
    assert hasattr(fenix::CourseLoad, "description")
    descriptor = None
    for klass in fenix::CourseLoad.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fenix::courseload_has_type():
    assert hasattr(fenix::CourseLoad, "type")
    descriptor = None
    for klass in fenix::CourseLoad.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fenix::courseload_has_name():
    assert hasattr(fenix::CourseLoad, "name")
    descriptor = None
    for klass in fenix::CourseLoad.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fenix::courseload_has_unitQuantity():
    assert hasattr(fenix::CourseLoad, "unitQuantity")
    descriptor = None
    for klass in fenix::CourseLoad.__mro__:
        if "unitQuantity" in klass.__dict__:
            descriptor = klass.__dict__["unitQuantity"]
            break
    assert isinstance(descriptor, property)



def test_fenix::lessonperiod_is_not_abstract():
    assert not inspect.isabstract(fenix::LessonPeriod)


def test_fenix::lessonperiod_constructor_exists():
    assert callable(fenix::LessonPeriod.__init__)


def test_fenix::lessonperiod_constructor_args():
    sig = inspect.signature(fenix::LessonPeriod.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_fenix::lessonperiod_has_start():
    assert hasattr(fenix::LessonPeriod, "start")
    descriptor = None
    for klass in fenix::LessonPeriod.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_fenix::lessonperiod_has_end():
    assert hasattr(fenix::LessonPeriod, "end")
    descriptor = None
    for klass in fenix::LessonPeriod.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_fenix::occupation_is_not_abstract():
    assert not inspect.isabstract(fenix::Occupation)


def test_fenix::occupation_constructor_exists():
    assert callable(fenix::Occupation.__init__)


def test_fenix::occupation_constructor_args():
    sig = inspect.signature(fenix::Occupation.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "current" in params, "Missing parameter 'current'"

def test_fenix::occupation_has_max():
    assert hasattr(fenix::Occupation, "max")
    descriptor = None
    for klass in fenix::Occupation.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fenix::occupation_has_current():
    assert hasattr(fenix::Occupation, "current")
    descriptor = None
    for klass in fenix::Occupation.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)



def test_fenix::shift_is_not_abstract():
    assert not inspect.isabstract(fenix::Shift)


def test_fenix::shift_constructor_exists():
    assert callable(fenix::Shift.__init__)


def test_fenix::shift_constructor_args():
    sig = inspect.signature(fenix::Shift.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "types" in params, "Missing parameter 'types'"

def test_fenix::shift_has_name():
    assert hasattr(fenix::Shift, "name")
    descriptor = None
    for klass in fenix::Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fenix::shift_has_types():
    assert hasattr(fenix::Shift, "types")
    descriptor = None
    for klass in fenix::Shift.__mro__:
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
fenix::scheduleOfCourse_strategy = st.builds(
    fenix::scheduleOfCourse,
)
fenix::Capacity_strategy = st.builds(
    fenix::Capacity,
    normal=
        st.integers(),
    exam=
        st.integers()
)
fenix::CourseLoad_strategy = st.builds(
    fenix::CourseLoad,
    totalQuantity=
        st.integers(),
    id=
        safe_text,
    description=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    unitQuantity=
        st.integers()
)
fenix::LessonPeriod_strategy = st.builds(
    fenix::LessonPeriod,
    start=
        safe_text,
    end=
        safe_text
)
fenix::Occupation_strategy = st.builds(
    fenix::Occupation,
    max=
        st.integers(),
    current=
        st.integers()
)
fenix::Shift_strategy = st.builds(
    fenix::Shift,
    name=
        safe_text,
    types=
        safe_text
)

@given(instance=fenix::scheduleOfCourse_strategy)
@settings(max_examples=50)
def test_fenix::scheduleofcourse_instantiation(instance):
    assert isinstance(instance, fenix::scheduleOfCourse)

@given(instance=fenix::Capacity_strategy)
@settings(max_examples=50)
def test_fenix::capacity_instantiation(instance):
    assert isinstance(instance, fenix::Capacity)

@given(instance=fenix::Capacity_strategy)
def test_fenix::capacity_normal_type(instance):
    assert isinstance(instance.normal, int)


@given(instance=fenix::Capacity_strategy)
def test_fenix::capacity_normal_setter(instance):
    original = instance.normal
    instance.normal = original
    assert instance.normal == original

@given(instance=fenix::Capacity_strategy)
def test_fenix::capacity_exam_type(instance):
    assert isinstance(instance.exam, int)


@given(instance=fenix::Capacity_strategy)
def test_fenix::capacity_exam_setter(instance):
    original = instance.exam
    instance.exam = original
    assert instance.exam == original

@given(instance=fenix::CourseLoad_strategy)
@settings(max_examples=50)
def test_fenix::courseload_instantiation(instance):
    assert isinstance(instance, fenix::CourseLoad)

@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_totalQuantity_type(instance):
    assert isinstance(instance.totalQuantity, int)


@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_totalQuantity_setter(instance):
    original = instance.totalQuantity
    instance.totalQuantity = original
    assert instance.totalQuantity == original

@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_unitQuantity_type(instance):
    assert isinstance(instance.unitQuantity, int)


@given(instance=fenix::CourseLoad_strategy)
def test_fenix::courseload_unitQuantity_setter(instance):
    original = instance.unitQuantity
    instance.unitQuantity = original
    assert instance.unitQuantity == original

@given(instance=fenix::LessonPeriod_strategy)
@settings(max_examples=50)
def test_fenix::lessonperiod_instantiation(instance):
    assert isinstance(instance, fenix::LessonPeriod)

@given(instance=fenix::LessonPeriod_strategy)
def test_fenix::lessonperiod_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=fenix::LessonPeriod_strategy)
def test_fenix::lessonperiod_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=fenix::LessonPeriod_strategy)
def test_fenix::lessonperiod_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=fenix::LessonPeriod_strategy)
def test_fenix::lessonperiod_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=fenix::Occupation_strategy)
@settings(max_examples=50)
def test_fenix::occupation_instantiation(instance):
    assert isinstance(instance, fenix::Occupation)

@given(instance=fenix::Occupation_strategy)
def test_fenix::occupation_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=fenix::Occupation_strategy)
def test_fenix::occupation_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=fenix::Occupation_strategy)
def test_fenix::occupation_current_type(instance):
    assert isinstance(instance.current, int)


@given(instance=fenix::Occupation_strategy)
def test_fenix::occupation_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=fenix::Shift_strategy)
@settings(max_examples=50)
def test_fenix::shift_instantiation(instance):
    assert isinstance(instance, fenix::Shift)

@given(instance=fenix::Shift_strategy)
def test_fenix::shift_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fenix::Shift_strategy)
def test_fenix::shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fenix::Shift_strategy)
def test_fenix::shift_types_type(instance):
    assert isinstance(instance.types, str)


@given(instance=fenix::Shift_strategy)
def test_fenix::shift_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original
