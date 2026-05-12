import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    outputgenerator,
    ATTGS,
    activity_manager,
    time_manager,
    subject_manager,
    data_manager,
    faculty_manager,
    class_manager,
    room_manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_outputgenerator_is_not_abstract():
    assert not inspect.isabstract(outputgenerator)


def test_outputgenerator_constructor_exists():
    assert callable(outputgenerator.__init__)


def test_outputgenerator_constructor_args():
    sig = inspect.signature(outputgenerator.__init__)
    params = list(sig.parameters.keys())



def test_attgs_is_not_abstract():
    assert not inspect.isabstract(ATTGS)


def test_attgs_constructor_exists():
    assert callable(ATTGS.__init__)


def test_attgs_constructor_args():
    sig = inspect.signature(ATTGS.__init__)
    params = list(sig.parameters.keys())



def test_activity_manager_is_not_abstract():
    assert not inspect.isabstract(activity_manager)


def test_activity_manager_constructor_exists():
    assert callable(activity_manager.__init__)


def test_activity_manager_constructor_args():
    sig = inspect.signature(activity_manager.__init__)
    params = list(sig.parameters.keys())



def test_time_manager_is_not_abstract():
    assert not inspect.isabstract(time_manager)


def test_time_manager_constructor_exists():
    assert callable(time_manager.__init__)


def test_time_manager_constructor_args():
    sig = inspect.signature(time_manager.__init__)
    params = list(sig.parameters.keys())



def test_subject_manager_is_not_abstract():
    assert not inspect.isabstract(subject_manager)


def test_subject_manager_constructor_exists():
    assert callable(subject_manager.__init__)


def test_subject_manager_constructor_args():
    sig = inspect.signature(subject_manager.__init__)
    params = list(sig.parameters.keys())



def test_data_manager_is_not_abstract():
    assert not inspect.isabstract(data_manager)


def test_data_manager_constructor_exists():
    assert callable(data_manager.__init__)


def test_data_manager_constructor_args():
    sig = inspect.signature(data_manager.__init__)
    params = list(sig.parameters.keys())



def test_faculty_manager_is_not_abstract():
    assert not inspect.isabstract(faculty_manager)


def test_faculty_manager_constructor_exists():
    assert callable(faculty_manager.__init__)


def test_faculty_manager_constructor_args():
    sig = inspect.signature(faculty_manager.__init__)
    params = list(sig.parameters.keys())



def test_class_manager_is_not_abstract():
    assert not inspect.isabstract(class_manager)


def test_class_manager_constructor_exists():
    assert callable(class_manager.__init__)


def test_class_manager_constructor_args():
    sig = inspect.signature(class_manager.__init__)
    params = list(sig.parameters.keys())



def test_room_manager_is_not_abstract():
    assert not inspect.isabstract(room_manager)


def test_room_manager_constructor_exists():
    assert callable(room_manager.__init__)


def test_room_manager_constructor_args():
    sig = inspect.signature(room_manager.__init__)
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
outputgenerator_strategy = st.builds(
    outputgenerator,
)
ATTGS_strategy = st.builds(
    ATTGS,
)
activity_manager_strategy = st.builds(
    activity_manager,
)
time_manager_strategy = st.builds(
    time_manager,
)
subject_manager_strategy = st.builds(
    subject_manager,
)
data_manager_strategy = st.builds(
    data_manager,
)
faculty_manager_strategy = st.builds(
    faculty_manager,
)
class_manager_strategy = st.builds(
    class_manager,
)
room_manager_strategy = st.builds(
    room_manager,
)

@given(instance=outputgenerator_strategy)
@settings(max_examples=50)
def test_outputgenerator_instantiation(instance):
    assert isinstance(instance, outputgenerator)

@given(instance=ATTGS_strategy)
@settings(max_examples=50)
def test_attgs_instantiation(instance):
    assert isinstance(instance, ATTGS)

@given(instance=activity_manager_strategy)
@settings(max_examples=50)
def test_activity_manager_instantiation(instance):
    assert isinstance(instance, activity_manager)

@given(instance=time_manager_strategy)
@settings(max_examples=50)
def test_time_manager_instantiation(instance):
    assert isinstance(instance, time_manager)

@given(instance=subject_manager_strategy)
@settings(max_examples=50)
def test_subject_manager_instantiation(instance):
    assert isinstance(instance, subject_manager)

@given(instance=data_manager_strategy)
@settings(max_examples=50)
def test_data_manager_instantiation(instance):
    assert isinstance(instance, data_manager)

@given(instance=faculty_manager_strategy)
@settings(max_examples=50)
def test_faculty_manager_instantiation(instance):
    assert isinstance(instance, faculty_manager)

@given(instance=class_manager_strategy)
@settings(max_examples=50)
def test_class_manager_instantiation(instance):
    assert isinstance(instance, class_manager)

@given(instance=room_manager_strategy)
@settings(max_examples=50)
def test_room_manager_instantiation(instance):
    assert isinstance(instance, room_manager)
