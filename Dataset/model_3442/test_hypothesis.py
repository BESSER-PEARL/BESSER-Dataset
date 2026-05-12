import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scholar_ScholarManagement,
    scholar_Named,
    Named,
    scholar_Discipline,
    scholar_Teacher,
    scholar_Lecture,
    scholar_Exam,
    scholar_Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scholar_scholarmanagement_is_not_abstract():
    assert not inspect.isabstract(scholar_ScholarManagement)


def test_scholar_scholarmanagement_constructor_exists():
    assert callable(scholar_ScholarManagement.__init__)


def test_scholar_scholarmanagement_constructor_args():
    sig = inspect.signature(scholar_ScholarManagement.__init__)
    params = list(sig.parameters.keys())



def test_scholar_named_is_not_abstract():
    assert not inspect.isabstract(scholar_Named)


def test_scholar_named_constructor_exists():
    assert callable(scholar_Named.__init__)


def test_scholar_named_constructor_args():
    sig = inspect.signature(scholar_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scholar_named_has_name():
    assert hasattr(scholar_Named, "name")
    descriptor = None
    for klass in scholar_Named.__mro__:
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



def test_scholar_discipline_is_not_abstract():
    assert not inspect.isabstract(scholar_Discipline)


def test_scholar_discipline_constructor_exists():
    assert callable(scholar_Discipline.__init__)


def test_scholar_discipline_constructor_args():
    sig = inspect.signature(scholar_Discipline.__init__)
    params = list(sig.parameters.keys())



def test_scholar_teacher_is_not_abstract():
    assert not inspect.isabstract(scholar_Teacher)


def test_scholar_teacher_constructor_exists():
    assert callable(scholar_Teacher.__init__)


def test_scholar_teacher_constructor_args():
    sig = inspect.signature(scholar_Teacher.__init__)
    params = list(sig.parameters.keys())



def test_scholar_lecture_is_not_abstract():
    assert not inspect.isabstract(scholar_Lecture)


def test_scholar_lecture_constructor_exists():
    assert callable(scholar_Lecture.__init__)


def test_scholar_lecture_constructor_args():
    sig = inspect.signature(scholar_Lecture.__init__)
    params = list(sig.parameters.keys())



def test_scholar_exam_is_not_abstract():
    assert not inspect.isabstract(scholar_Exam)


def test_scholar_exam_constructor_exists():
    assert callable(scholar_Exam.__init__)


def test_scholar_exam_constructor_args():
    sig = inspect.signature(scholar_Exam.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"

def test_scholar_exam_has_score():
    assert hasattr(scholar_Exam, "score")
    descriptor = None
    for klass in scholar_Exam.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)



def test_scholar_student_is_not_abstract():
    assert not inspect.isabstract(scholar_Student)


def test_scholar_student_constructor_exists():
    assert callable(scholar_Student.__init__)


def test_scholar_student_constructor_args():
    sig = inspect.signature(scholar_Student.__init__)
    params = list(sig.parameters.keys())
    assert "forname" in params, "Missing parameter 'forname'"

def test_scholar_student_has_forname():
    assert hasattr(scholar_Student, "forname")
    descriptor = None
    for klass in scholar_Student.__mro__:
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
scholar_ScholarManagement_strategy = st.builds(
    scholar_ScholarManagement,
)
scholar_Named_strategy = st.builds(
    scholar_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
scholar_Discipline_strategy = st.builds(
    scholar_Discipline,
)
scholar_Teacher_strategy = st.builds(
    scholar_Teacher,
)
scholar_Lecture_strategy = st.builds(
    scholar_Lecture,
)
scholar_Exam_strategy = st.builds(
    scholar_Exam,
    score=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
scholar_Student_strategy = st.builds(
    scholar_Student,
    forname=
        safe_text
)

@given(instance=scholar_ScholarManagement_strategy)
@settings(max_examples=50)
def test_scholar_scholarmanagement_instantiation(instance):
    assert isinstance(instance, scholar_ScholarManagement)

@given(instance=scholar_Named_strategy)
@settings(max_examples=50)
def test_scholar_named_instantiation(instance):
    assert isinstance(instance, scholar_Named)



@given(instance=scholar_Named_strategy)
def test_scholar_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=scholar_Discipline_strategy)
@settings(max_examples=50)
def test_scholar_discipline_instantiation(instance):
    assert isinstance(instance, scholar_Discipline)

@given(instance=scholar_Teacher_strategy)
@settings(max_examples=50)
def test_scholar_teacher_instantiation(instance):
    assert isinstance(instance, scholar_Teacher)

@given(instance=scholar_Lecture_strategy)
@settings(max_examples=50)
def test_scholar_lecture_instantiation(instance):
    assert isinstance(instance, scholar_Lecture)

@given(instance=scholar_Exam_strategy)
@settings(max_examples=50)
def test_scholar_exam_instantiation(instance):
    assert isinstance(instance, scholar_Exam)



@given(instance=scholar_Exam_strategy)
def test_scholar_exam_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=scholar_Student_strategy)
@settings(max_examples=50)
def test_scholar_student_instantiation(instance):
    assert isinstance(instance, scholar_Student)



@given(instance=scholar_Student_strategy)
def test_scholar_student_forname_setter(instance):
    original = instance.forname
    instance.forname = original
    assert instance.forname == original
