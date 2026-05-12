import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    news,
    Quiz,
    Task,
    Mark,
    Department,
    Student,
    teacher,
    user,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_news_is_not_abstract():
    assert not inspect.isabstract(news)


def test_news_constructor_exists():
    assert callable(news.__init__)


def test_news_constructor_args():
    sig = inspect.signature(news.__init__)
    params = list(sig.parameters.keys())
    assert "dlnews" in params, "Missing parameter 'dlnews'"
    assert "author" in params, "Missing parameter 'author'"

def test_news_has_dlnews():
    assert hasattr(news, "dlnews")
    descriptor = None
    for klass in news.__mro__:
        if "dlnews" in klass.__dict__:
            descriptor = klass.__dict__["dlnews"]
            break
    assert isinstance(descriptor, property)

def test_news_has_author():
    assert hasattr(news, "author")
    descriptor = None
    for klass in news.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_quiz_is_not_abstract():
    assert not inspect.isabstract(Quiz)


def test_quiz_constructor_exists():
    assert callable(Quiz.__init__)


def test_quiz_constructor_args():
    sig = inspect.signature(Quiz.__init__)
    params = list(sig.parameters.keys())
    assert "questions__" in params, "Missing parameter 'questions__'"
    assert "title" in params, "Missing parameter 'title'"
    assert "moduleName" in params, "Missing parameter 'moduleName'"

def test_quiz_has_questions__():
    assert hasattr(Quiz, "questions__")
    descriptor = None
    for klass in Quiz.__mro__:
        if "questions__" in klass.__dict__:
            descriptor = klass.__dict__["questions__"]
            break
    assert isinstance(descriptor, property)

def test_quiz_has_title():
    assert hasattr(Quiz, "title")
    descriptor = None
    for klass in Quiz.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_quiz_has_moduleName():
    assert hasattr(Quiz, "moduleName")
    descriptor = None
    for klass in Quiz.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_mark_is_not_abstract():
    assert not inspect.isabstract(Mark)


def test_mark_constructor_exists():
    assert callable(Mark.__init__)


def test_mark_constructor_args():
    sig = inspect.signature(Mark.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Mark" in params, "Missing parameter 'Mark'"

def test_mark_has_id():
    assert hasattr(Mark, "id")
    descriptor = None
    for klass in Mark.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mark_has_Mark():
    assert hasattr(Mark, "Mark")
    descriptor = None
    for klass in Mark.__mro__:
        if "Mark" in klass.__dict__:
            descriptor = klass.__dict__["Mark"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "teachers__" in params, "Missing parameter 'teachers__'"
    assert "modules__" in params, "Missing parameter 'modules__'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_department_has_teachers__():
    assert hasattr(Department, "teachers__")
    descriptor = None
    for klass in Department.__mro__:
        if "teachers__" in klass.__dict__:
            descriptor = klass.__dict__["teachers__"]
            break
    assert isinstance(descriptor, property)

def test_department_has_modules__():
    assert hasattr(Department, "modules__")
    descriptor = None
    for klass in Department.__mro__:
        if "modules__" in klass.__dict__:
            descriptor = klass.__dict__["modules__"]
            break
    assert isinstance(descriptor, property)

def test_department_has_name():
    assert hasattr(Department, "name")
    descriptor = None
    for klass in Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_department_has_id():
    assert hasattr(Department, "id")
    descriptor = None
    for klass in Department.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_student_has_id():
    assert hasattr(Student, "id")
    descriptor = None
    for klass in Student.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_student_has_name():
    assert hasattr(Student, "name")
    descriptor = None
    for klass in Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_teacher_is_not_abstract():
    assert not inspect.isabstract(teacher)


def test_teacher_constructor_exists():
    assert callable(teacher.__init__)


def test_teacher_constructor_args():
    sig = inspect.signature(teacher.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_teacher_has_id():
    assert hasattr(teacher, "id")
    descriptor = None
    for klass in teacher.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_teacher_has_name():
    assert hasattr(teacher, "name")
    descriptor = None
    for klass in teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_user_has_name():
    assert hasattr(user, "name")
    descriptor = None
    for klass in user.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id():
    assert hasattr(user, "id")
    descriptor = None
    for klass in user.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
news_strategy = st.builds(
    news,
    dlnews=
        safe_text,
    author=
        safe_text
)
Quiz_strategy = st.builds(
    Quiz,
    questions__=
        safe_text,
    title=
        safe_text,
    moduleName=
        safe_text
)
Task_strategy = st.builds(
    Task,
)
Mark_strategy = st.builds(
    Mark,
    id=
        st.none(),
    Mark=
        st.integers()
)
Department_strategy = st.builds(
    Department,
    teachers__=
        st.integers(),
    modules__=
        safe_text,
    name=
        safe_text,
    id=
        st.integers()
)
Student_strategy = st.builds(
    Student,
    id=
        st.integers(),
    name=
        safe_text
)
teacher_strategy = st.builds(
    teacher,
    id=
        st.integers(),
    name=
        safe_text
)
user_strategy = st.builds(
    user,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=news_strategy)
@settings(max_examples=50)
def test_news_instantiation(instance):
    assert isinstance(instance, news)



@given(instance=news_strategy)
def test_news_dlnews_setter(instance):
    original = instance.dlnews
    instance.dlnews = original
    assert instance.dlnews == original



@given(instance=news_strategy)
def test_news_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=Quiz_strategy)
@settings(max_examples=50)
def test_quiz_instantiation(instance):
    assert isinstance(instance, Quiz)



@given(instance=Quiz_strategy)
def test_quiz_questions___setter(instance):
    original = instance.questions__
    instance.questions__ = original
    assert instance.questions__ == original



@given(instance=Quiz_strategy)
def test_quiz_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Quiz_strategy)
def test_quiz_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=Mark_strategy)
@settings(max_examples=50)
def test_mark_instantiation(instance):
    assert isinstance(instance, Mark)



@given(instance=Mark_strategy)
def test_mark_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Mark_strategy)
def test_mark_Mark_setter(instance):
    original = instance.Mark
    instance.Mark = original
    assert instance.Mark == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_teachers___setter(instance):
    original = instance.teachers__
    instance.teachers__ = original
    assert instance.teachers__ == original



@given(instance=Department_strategy)
def test_department_modules___setter(instance):
    original = instance.modules__
    instance.modules__ = original
    assert instance.modules__ == original



@given(instance=Department_strategy)
def test_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Department_strategy)
def test_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Student_strategy)
def test_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=teacher_strategy)
@settings(max_examples=50)
def test_teacher_instantiation(instance):
    assert isinstance(instance, teacher)



@given(instance=teacher_strategy)
def test_teacher_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=teacher_strategy)
def test_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=user_strategy)
def test_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
