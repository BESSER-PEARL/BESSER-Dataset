import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    admin_Actor,
    _Component,
    faculty_Actor,
    student_Actor,
    modify_list_of_students_external,
    view_cumiliative_attendance_external,
    send_attendance_sms_external,
    logout_external,
    login_external,
    answer_attendance_call_external,
    post_attendance_external,
    generate_class_wise_attendance_report_external,
    take_attendance_call_external,
    ADMIN,
    PARENT,
    STUDENT,
    FACULTY,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test__component_is_not_abstract():
    assert not inspect.isabstract(_Component)


def test__component_constructor_exists():
    assert callable(_Component.__init__)


def test__component_constructor_args():
    sig = inspect.signature(_Component.__init__)
    params = list(sig.parameters.keys())



def test_faculty_actor_is_not_abstract():
    assert not inspect.isabstract(faculty_Actor)


def test_faculty_actor_constructor_exists():
    assert callable(faculty_Actor.__init__)


def test_faculty_actor_constructor_args():
    sig = inspect.signature(faculty_Actor.__init__)
    params = list(sig.parameters.keys())



def test_student_actor_is_not_abstract():
    assert not inspect.isabstract(student_Actor)


def test_student_actor_constructor_exists():
    assert callable(student_Actor.__init__)


def test_student_actor_constructor_args():
    sig = inspect.signature(student_Actor.__init__)
    params = list(sig.parameters.keys())



def test_modify_list_of_students_external_is_not_abstract():
    assert not inspect.isabstract(modify_list_of_students_external)


def test_modify_list_of_students_external_constructor_exists():
    assert callable(modify_list_of_students_external.__init__)


def test_modify_list_of_students_external_constructor_args():
    sig = inspect.signature(modify_list_of_students_external.__init__)
    params = list(sig.parameters.keys())



def test_view_cumiliative_attendance_external_is_not_abstract():
    assert not inspect.isabstract(view_cumiliative_attendance_external)


def test_view_cumiliative_attendance_external_constructor_exists():
    assert callable(view_cumiliative_attendance_external.__init__)


def test_view_cumiliative_attendance_external_constructor_args():
    sig = inspect.signature(view_cumiliative_attendance_external.__init__)
    params = list(sig.parameters.keys())



def test_send_attendance_sms_external_is_not_abstract():
    assert not inspect.isabstract(send_attendance_sms_external)


def test_send_attendance_sms_external_constructor_exists():
    assert callable(send_attendance_sms_external.__init__)


def test_send_attendance_sms_external_constructor_args():
    sig = inspect.signature(send_attendance_sms_external.__init__)
    params = list(sig.parameters.keys())



def test_logout_external_is_not_abstract():
    assert not inspect.isabstract(logout_external)


def test_logout_external_constructor_exists():
    assert callable(logout_external.__init__)


def test_logout_external_constructor_args():
    sig = inspect.signature(logout_external.__init__)
    params = list(sig.parameters.keys())



def test_login_external_is_not_abstract():
    assert not inspect.isabstract(login_external)


def test_login_external_constructor_exists():
    assert callable(login_external.__init__)


def test_login_external_constructor_args():
    sig = inspect.signature(login_external.__init__)
    params = list(sig.parameters.keys())



def test_answer_attendance_call_external_is_not_abstract():
    assert not inspect.isabstract(answer_attendance_call_external)


def test_answer_attendance_call_external_constructor_exists():
    assert callable(answer_attendance_call_external.__init__)


def test_answer_attendance_call_external_constructor_args():
    sig = inspect.signature(answer_attendance_call_external.__init__)
    params = list(sig.parameters.keys())



def test_post_attendance_external_is_not_abstract():
    assert not inspect.isabstract(post_attendance_external)


def test_post_attendance_external_constructor_exists():
    assert callable(post_attendance_external.__init__)


def test_post_attendance_external_constructor_args():
    sig = inspect.signature(post_attendance_external.__init__)
    params = list(sig.parameters.keys())



def test_generate_class_wise_attendance_report_external_is_not_abstract():
    assert not inspect.isabstract(generate_class_wise_attendance_report_external)


def test_generate_class_wise_attendance_report_external_constructor_exists():
    assert callable(generate_class_wise_attendance_report_external.__init__)


def test_generate_class_wise_attendance_report_external_constructor_args():
    sig = inspect.signature(generate_class_wise_attendance_report_external.__init__)
    params = list(sig.parameters.keys())



def test_take_attendance_call_external_is_not_abstract():
    assert not inspect.isabstract(take_attendance_call_external)


def test_take_attendance_call_external_constructor_exists():
    assert callable(take_attendance_call_external.__init__)


def test_take_attendance_call_external_constructor_args():
    sig = inspect.signature(take_attendance_call_external.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(ADMIN)


def test_admin_constructor_exists():
    assert callable(ADMIN.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(ADMIN.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

def test_admin_has_password():
    assert hasattr(ADMIN, "password")
    descriptor = None
    for klass in ADMIN.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_id():
    assert hasattr(ADMIN, "id")
    descriptor = None
    for klass in ADMIN.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_parent_is_not_abstract():
    assert not inspect.isabstract(PARENT)


def test_parent_constructor_exists():
    assert callable(PARENT.__init__)


def test_parent_constructor_args():
    sig = inspect.signature(PARENT.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "id" in params, "Missing parameter 'id'"

def test_parent_has_password():
    assert hasattr(PARENT, "password")
    descriptor = None
    for klass in PARENT.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_parent_has_phoneNumber():
    assert hasattr(PARENT, "phoneNumber")
    descriptor = None
    for klass in PARENT.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_parent_has_id():
    assert hasattr(PARENT, "id")
    descriptor = None
    for klass in PARENT.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(STUDENT)


def test_student_constructor_exists():
    assert callable(STUDENT.__init__)


def test_student_constructor_args():
    sig = inspect.signature(STUDENT.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_student_has_id():
    assert hasattr(STUDENT, "id")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_student_has_password():
    assert hasattr(STUDENT, "password")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_faculty_is_not_abstract():
    assert not inspect.isabstract(FACULTY)


def test_faculty_constructor_exists():
    assert callable(FACULTY.__init__)


def test_faculty_constructor_args():
    sig = inspect.signature(FACULTY.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_faculty_has_id():
    assert hasattr(FACULTY, "id")
    descriptor = None
    for klass in FACULTY.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_faculty_has_password():
    assert hasattr(FACULTY, "password")
    descriptor = None
    for klass in FACULTY.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
admin_Actor_strategy = st.builds(
    admin_Actor,
)
_Component_strategy = st.builds(
    _Component,
)
faculty_Actor_strategy = st.builds(
    faculty_Actor,
)
student_Actor_strategy = st.builds(
    student_Actor,
)
modify_list_of_students_external_strategy = st.builds(
    modify_list_of_students_external,
)
view_cumiliative_attendance_external_strategy = st.builds(
    view_cumiliative_attendance_external,
)
send_attendance_sms_external_strategy = st.builds(
    send_attendance_sms_external,
)
logout_external_strategy = st.builds(
    logout_external,
)
login_external_strategy = st.builds(
    login_external,
)
answer_attendance_call_external_strategy = st.builds(
    answer_attendance_call_external,
)
post_attendance_external_strategy = st.builds(
    post_attendance_external,
)
generate_class_wise_attendance_report_external_strategy = st.builds(
    generate_class_wise_attendance_report_external,
)
take_attendance_call_external_strategy = st.builds(
    take_attendance_call_external,
)
ADMIN_strategy = st.builds(
    ADMIN,
    password=
        safe_text,
    id=
        safe_text
)
PARENT_strategy = st.builds(
    PARENT,
    password=
        safe_text,
    phoneNumber=
        st.integers(),
    id=
        safe_text
)
STUDENT_strategy = st.builds(
    STUDENT,
    id=
        safe_text,
    password=
        safe_text
)
FACULTY_strategy = st.builds(
    FACULTY,
    id=
        safe_text,
    password=
        safe_text
)

@given(instance=admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, admin_Actor)

@given(instance=_Component_strategy)
@settings(max_examples=50)
def test__component_instantiation(instance):
    assert isinstance(instance, _Component)

@given(instance=faculty_Actor_strategy)
@settings(max_examples=50)
def test_faculty_actor_instantiation(instance):
    assert isinstance(instance, faculty_Actor)

@given(instance=student_Actor_strategy)
@settings(max_examples=50)
def test_student_actor_instantiation(instance):
    assert isinstance(instance, student_Actor)

@given(instance=modify_list_of_students_external_strategy)
@settings(max_examples=50)
def test_modify_list_of_students_external_instantiation(instance):
    assert isinstance(instance, modify_list_of_students_external)

@given(instance=view_cumiliative_attendance_external_strategy)
@settings(max_examples=50)
def test_view_cumiliative_attendance_external_instantiation(instance):
    assert isinstance(instance, view_cumiliative_attendance_external)

@given(instance=send_attendance_sms_external_strategy)
@settings(max_examples=50)
def test_send_attendance_sms_external_instantiation(instance):
    assert isinstance(instance, send_attendance_sms_external)

@given(instance=logout_external_strategy)
@settings(max_examples=50)
def test_logout_external_instantiation(instance):
    assert isinstance(instance, logout_external)

@given(instance=login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, login_external)

@given(instance=answer_attendance_call_external_strategy)
@settings(max_examples=50)
def test_answer_attendance_call_external_instantiation(instance):
    assert isinstance(instance, answer_attendance_call_external)

@given(instance=post_attendance_external_strategy)
@settings(max_examples=50)
def test_post_attendance_external_instantiation(instance):
    assert isinstance(instance, post_attendance_external)

@given(instance=generate_class_wise_attendance_report_external_strategy)
@settings(max_examples=50)
def test_generate_class_wise_attendance_report_external_instantiation(instance):
    assert isinstance(instance, generate_class_wise_attendance_report_external)

@given(instance=take_attendance_call_external_strategy)
@settings(max_examples=50)
def test_take_attendance_call_external_instantiation(instance):
    assert isinstance(instance, take_attendance_call_external)

@given(instance=ADMIN_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, ADMIN)



@given(instance=ADMIN_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=ADMIN_strategy)
def test_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PARENT_strategy)
@settings(max_examples=50)
def test_parent_instantiation(instance):
    assert isinstance(instance, PARENT)



@given(instance=PARENT_strategy)
def test_parent_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=PARENT_strategy)
def test_parent_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=PARENT_strategy)
def test_parent_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=STUDENT_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, STUDENT)



@given(instance=STUDENT_strategy)
def test_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=STUDENT_strategy)
def test_student_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=FACULTY_strategy)
@settings(max_examples=50)
def test_faculty_instantiation(instance):
    assert isinstance(instance, FACULTY)



@given(instance=FACULTY_strategy)
def test_faculty_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=FACULTY_strategy)
def test_faculty_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
