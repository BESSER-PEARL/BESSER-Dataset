import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scholar::ScholarManagement,
    scholar::Named,
    Named,
    scholar::Exam,
    scholar::Discipline,
    scholar::Lecture,
    scholar::Teacher,
    scholar::Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scholar::scholarmanagement_is_not_abstract():
    assert not inspect.isabstract(scholar::ScholarManagement)


def test_scholar::scholarmanagement_constructor_exists():
    assert callable(scholar::ScholarManagement.__init__)


def test_scholar::scholarmanagement_constructor_args():
    sig = inspect.signature(scholar::ScholarManagement.__init__)
    params = list(sig.parameters.keys())



def test_scholar::named_is_not_abstract():
    assert not inspect.isabstract(scholar::Named)


def test_scholar::named_constructor_exists():
    assert callable(scholar::Named.__init__)


def test_scholar::named_constructor_args():
    sig = inspect.signature(scholar::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scholar::named_has_name():
    assert hasattr(scholar::Named, "name")
    descriptor = None
    for klass in scholar::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_scholar::exam_is_not_abstract():
    assert not inspect.isabstract(scholar::Exam)


def test_scholar::exam_constructor_exists():
    assert callable(scholar::Exam.__init__)


def test_scholar::exam_constructor_args():
    sig = inspect.signature(scholar::Exam.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"

def test_scholar::exam_has_score():
    assert hasattr(scholar::Exam, "score")
    descriptor = None
    for klass in scholar::Exam.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)



def test_scholar::discipline_is_not_abstract():
    assert not inspect.isabstract(scholar::Discipline)


def test_scholar::discipline_constructor_exists():
    assert callable(scholar::Discipline.__init__)


def test_scholar::discipline_constructor_args():
    sig = inspect.signature(scholar::Discipline.__init__)
    params = list(sig.parameters.keys())



def test_scholar::lecture_is_not_abstract():
    assert not inspect.isabstract(scholar::Lecture)


def test_scholar::lecture_constructor_exists():
    assert callable(scholar::Lecture.__init__)


def test_scholar::lecture_constructor_args():
    sig = inspect.signature(scholar::Lecture.__init__)
    params = list(sig.parameters.keys())



def test_scholar::teacher_is_not_abstract():
    assert not inspect.isabstract(scholar::Teacher)


def test_scholar::teacher_constructor_exists():
    assert callable(scholar::Teacher.__init__)


def test_scholar::teacher_constructor_args():
    sig = inspect.signature(scholar::Teacher.__init__)
    params = list(sig.parameters.keys())



def test_scholar::student_is_not_abstract():
    assert not inspect.isabstract(scholar::Student)


def test_scholar::student_constructor_exists():
    assert callable(scholar::Student.__init__)


def test_scholar::student_constructor_args():
    sig = inspect.signature(scholar::Student.__init__)
    params = list(sig.parameters.keys())
    assert "forname" in params, "Missing parameter 'forname'"

def test_scholar::student_has_forname():
    assert hasattr(scholar::Student, "forname")
    descriptor = None
    for klass in scholar::Student.__mro__:
        if "forname" in klass.__dict__:
            descriptor = klass.__dict__["forname"]
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
scholar::ScholarManagement_strategy = st.builds(
    scholar::ScholarManagement,
)
scholar::Named_strategy = st.builds(
    scholar::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
scholar::Exam_strategy = st.builds(
    scholar::Exam,
    score=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
scholar::Discipline_strategy = st.builds(
    scholar::Discipline,
)
scholar::Lecture_strategy = st.builds(
    scholar::Lecture,
)
scholar::Teacher_strategy = st.builds(
    scholar::Teacher,
)
scholar::Student_strategy = st.builds(
    scholar::Student,
    forname=
        safe_text
)

@given(instance=scholar::ScholarManagement_strategy)
@settings(max_examples=50)
def test_scholar::scholarmanagement_instantiation(instance):
    assert isinstance(instance, scholar::ScholarManagement)

@given(instance=scholar::Named_strategy)
@settings(max_examples=50)
def test_scholar::named_instantiation(instance):
    assert isinstance(instance, scholar::Named)

@given(instance=scholar::Named_strategy)
def test_scholar::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scholar::Named_strategy)
def test_scholar::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=scholar::Exam_strategy)
@settings(max_examples=50)
def test_scholar::exam_instantiation(instance):
    assert isinstance(instance, scholar::Exam)

@given(instance=scholar::Exam_strategy)
def test_scholar::exam_score_type(instance):
    assert isinstance(instance.score, float)


@given(instance=scholar::Exam_strategy)
def test_scholar::exam_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=scholar::Discipline_strategy)
@settings(max_examples=50)
def test_scholar::discipline_instantiation(instance):
    assert isinstance(instance, scholar::Discipline)

@given(instance=scholar::Lecture_strategy)
@settings(max_examples=50)
def test_scholar::lecture_instantiation(instance):
    assert isinstance(instance, scholar::Lecture)

@given(instance=scholar::Teacher_strategy)
@settings(max_examples=50)
def test_scholar::teacher_instantiation(instance):
    assert isinstance(instance, scholar::Teacher)

@given(instance=scholar::Student_strategy)
@settings(max_examples=50)
def test_scholar::student_instantiation(instance):
    assert isinstance(instance, scholar::Student)

@given(instance=scholar::Student_strategy)
def test_scholar::student_forname_type(instance):
    assert isinstance(instance.forname, str)


@given(instance=scholar::Student_strategy)
def test_scholar::student_forname_setter(instance):
    original = instance.forname
    instance.forname = original
    assert instance.forname == original
