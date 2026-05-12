import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fenix_scheduleOfCourse,
    fenix_Capacity,
    fenix_CourseLoad,
    fenix_LessonPeriod,
    fenix_Occupation,
    fenix_Shift,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fenix_scheduleofcourse_is_not_abstract():
    assert not inspect.isabstract(fenix_scheduleOfCourse)


def test_fenix_scheduleofcourse_constructor_exists():
    assert callable(fenix_scheduleOfCourse.__init__)


def test_fenix_scheduleofcourse_constructor_args():
    sig = inspect.signature(fenix_scheduleOfCourse.__init__)
    params = list(sig.parameters.keys())



def test_fenix_capacity_is_not_abstract():
    assert not inspect.isabstract(fenix_Capacity)


def test_fenix_capacity_constructor_exists():
    assert callable(fenix_Capacity.__init__)


def test_fenix_capacity_constructor_args():
    sig = inspect.signature(fenix_Capacity.__init__)
    params = list(sig.parameters.keys())
    assert "exam" in params, "Missing parameter 'exam'"
    assert "normal" in params, "Missing parameter 'normal'"

def test_fenix_capacity_has_exam():
    assert hasattr(fenix_Capacity, "exam")
    descriptor = None
    for klass in fenix_Capacity.__mro__:
        if "exam" in klass.__dict__:
            descriptor = klass.__dict__["exam"]
            break
    assert isinstance(descriptor, property)

def test_fenix_capacity_has_normal():
    assert hasattr(fenix_Capacity, "normal")
    descriptor = None
    for klass in fenix_Capacity.__mro__:
        if "normal" in klass.__dict__:
            descriptor = klass.__dict__["normal"]
            break
    assert isinstance(descriptor, property)



def test_fenix_courseload_is_not_abstract():
    assert not inspect.isabstract(fenix_CourseLoad)


def test_fenix_courseload_constructor_exists():
    assert callable(fenix_CourseLoad.__init__)


def test_fenix_courseload_constructor_args():
    sig = inspect.signature(fenix_CourseLoad.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "totalQuantity" in params, "Missing parameter 'totalQuantity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "unitQuantity" in params, "Missing parameter 'unitQuantity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_fenix_courseload_has_description():
    assert hasattr(fenix_CourseLoad, "description")
    descriptor = None
    for klass in fenix_CourseLoad.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fenix_courseload_has_totalQuantity():
    assert hasattr(fenix_CourseLoad, "totalQuantity")
    descriptor = None
    for klass in fenix_CourseLoad.__mro__:
        if "totalQuantity" in klass.__dict__:
            descriptor = klass.__dict__["totalQuantity"]
            break
    assert isinstance(descriptor, property)

def test_fenix_courseload_has_type():
    assert hasattr(fenix_CourseLoad, "type")
    descriptor = None
    for klass in fenix_CourseLoad.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fenix_courseload_has_unitQuantity():
    assert hasattr(fenix_CourseLoad, "unitQuantity")
    descriptor = None
    for klass in fenix_CourseLoad.__mro__:
        if "unitQuantity" in klass.__dict__:
            descriptor = klass.__dict__["unitQuantity"]
            break
    assert isinstance(descriptor, property)

def test_fenix_courseload_has_name():
    assert hasattr(fenix_CourseLoad, "name")
    descriptor = None
    for klass in fenix_CourseLoad.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fenix_courseload_has_id():
    assert hasattr(fenix_CourseLoad, "id")
    descriptor = None
    for klass in fenix_CourseLoad.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_fenix_lessonperiod_is_not_abstract():
    assert not inspect.isabstract(fenix_LessonPeriod)


def test_fenix_lessonperiod_constructor_exists():
    assert callable(fenix_LessonPeriod.__init__)


def test_fenix_lessonperiod_constructor_args():
    sig = inspect.signature(fenix_LessonPeriod.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_fenix_lessonperiod_has_start():
    assert hasattr(fenix_LessonPeriod, "start")
    descriptor = None
    for klass in fenix_LessonPeriod.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_fenix_lessonperiod_has_end():
    assert hasattr(fenix_LessonPeriod, "end")
    descriptor = None
    for klass in fenix_LessonPeriod.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_fenix_occupation_is_not_abstract():
    assert not inspect.isabstract(fenix_Occupation)


def test_fenix_occupation_constructor_exists():
    assert callable(fenix_Occupation.__init__)


def test_fenix_occupation_constructor_args():
    sig = inspect.signature(fenix_Occupation.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "current" in params, "Missing parameter 'current'"

def test_fenix_occupation_has_max():
    assert hasattr(fenix_Occupation, "max")
    descriptor = None
    for klass in fenix_Occupation.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fenix_occupation_has_current():
    assert hasattr(fenix_Occupation, "current")
    descriptor = None
    for klass in fenix_Occupation.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)



def test_fenix_shift_is_not_abstract():
    assert not inspect.isabstract(fenix_Shift)


def test_fenix_shift_constructor_exists():
    assert callable(fenix_Shift.__init__)


def test_fenix_shift_constructor_args():
    sig = inspect.signature(fenix_Shift.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"
    assert "name" in params, "Missing parameter 'name'"

def test_fenix_shift_has_types():
    assert hasattr(fenix_Shift, "types")
    descriptor = None
    for klass in fenix_Shift.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)

def test_fenix_shift_has_name():
    assert hasattr(fenix_Shift, "name")
    descriptor = None
    for klass in fenix_Shift.__mro__:
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
fenix_scheduleOfCourse_strategy = st.builds(
    fenix_scheduleOfCourse,
)
fenix_Capacity_strategy = st.builds(
    fenix_Capacity,
    exam=
        st.integers(),
    normal=
        st.integers()
)
fenix_CourseLoad_strategy = st.builds(
    fenix_CourseLoad,
    description=
        safe_text,
    totalQuantity=
        st.integers(),
    type=
        safe_text,
    unitQuantity=
        st.integers(),
    name=
        safe_text,
    id=
        safe_text
)
fenix_LessonPeriod_strategy = st.builds(
    fenix_LessonPeriod,
    start=
        safe_text,
    end=
        safe_text
)
fenix_Occupation_strategy = st.builds(
    fenix_Occupation,
    max=
        st.integers(),
    current=
        st.integers()
)
fenix_Shift_strategy = st.builds(
    fenix_Shift,
    types=
        safe_text,
    name=
        safe_text
)

@given(instance=fenix_scheduleOfCourse_strategy)
@settings(max_examples=50)
def test_fenix_scheduleofcourse_instantiation(instance):
    assert isinstance(instance, fenix_scheduleOfCourse)

@given(instance=fenix_Capacity_strategy)
@settings(max_examples=50)
def test_fenix_capacity_instantiation(instance):
    assert isinstance(instance, fenix_Capacity)



@given(instance=fenix_Capacity_strategy)
def test_fenix_capacity_exam_setter(instance):
    original = instance.exam
    instance.exam = original
    assert instance.exam == original



@given(instance=fenix_Capacity_strategy)
def test_fenix_capacity_normal_setter(instance):
    original = instance.normal
    instance.normal = original
    assert instance.normal == original

@given(instance=fenix_CourseLoad_strategy)
@settings(max_examples=50)
def test_fenix_courseload_instantiation(instance):
    assert isinstance(instance, fenix_CourseLoad)



@given(instance=fenix_CourseLoad_strategy)
def test_fenix_courseload_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fenix_CourseLoad_strategy)
def test_fenix_courseload_totalQuantity_setter(instance):
    original = instance.totalQuantity
    instance.totalQuantity = original
    assert instance.totalQuantity == original



@given(instance=fenix_CourseLoad_strategy)
def test_fenix_courseload_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=fenix_CourseLoad_strategy)
def test_fenix_courseload_unitQuantity_setter(instance):
    original = instance.unitQuantity
    instance.unitQuantity = original
    assert instance.unitQuantity == original



@given(instance=fenix_CourseLoad_strategy)
def test_fenix_courseload_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fenix_CourseLoad_strategy)
def test_fenix_courseload_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fenix_LessonPeriod_strategy)
@settings(max_examples=50)
def test_fenix_lessonperiod_instantiation(instance):
    assert isinstance(instance, fenix_LessonPeriod)



@given(instance=fenix_LessonPeriod_strategy)
def test_fenix_lessonperiod_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=fenix_LessonPeriod_strategy)
def test_fenix_lessonperiod_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=fenix_Occupation_strategy)
@settings(max_examples=50)
def test_fenix_occupation_instantiation(instance):
    assert isinstance(instance, fenix_Occupation)



@given(instance=fenix_Occupation_strategy)
def test_fenix_occupation_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=fenix_Occupation_strategy)
def test_fenix_occupation_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=fenix_Shift_strategy)
@settings(max_examples=50)
def test_fenix_shift_instantiation(instance):
    assert isinstance(instance, fenix_Shift)



@given(instance=fenix_Shift_strategy)
def test_fenix_shift_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original



@given(instance=fenix_Shift_strategy)
def test_fenix_shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
