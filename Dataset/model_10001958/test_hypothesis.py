import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin,
    Faculty,
    Student,
    Logout_UseCase,
    View_Questions_And_Post_Answers_UseCase,
    Post_Questions_UseCase,
    View_The_Uploaded_Materials_UseCase,
    Manage_Student___Faculty_List_UseCase,
    View___Modify_the_Uploaded_Materials_UseCase,
    Upload_Materials_UseCase,
    Login_UseCase,
    SignUp_UseCase,
    Admin_Actor,
    Faculty__Actor,
    Student_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mail_ID" in params, "Missing parameter 'mail_ID'"

def test_admin_has_name():
    assert hasattr(Admin, "name")
    descriptor = None
    for klass in Admin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_mail_ID():
    assert hasattr(Admin, "mail_ID")
    descriptor = None
    for klass in Admin.__mro__:
        if "mail_ID" in klass.__dict__:
            descriptor = klass.__dict__["mail_ID"]
            break
    assert isinstance(descriptor, property)



def test_faculty_is_not_abstract():
    assert not inspect.isabstract(Faculty)


def test_faculty_constructor_exists():
    assert callable(Faculty.__init__)


def test_faculty_constructor_args():
    sig = inspect.signature(Faculty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "emp_ID" in params, "Missing parameter 'emp_ID'"
    assert "mail_ID" in params, "Missing parameter 'mail_ID'"

def test_faculty_has_name():
    assert hasattr(Faculty, "name")
    descriptor = None
    for klass in Faculty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faculty_has_emp_ID():
    assert hasattr(Faculty, "emp_ID")
    descriptor = None
    for klass in Faculty.__mro__:
        if "emp_ID" in klass.__dict__:
            descriptor = klass.__dict__["emp_ID"]
            break
    assert isinstance(descriptor, property)

def test_faculty_has_mail_ID():
    assert hasattr(Faculty, "mail_ID")
    descriptor = None
    for klass in Faculty.__mro__:
        if "mail_ID" in klass.__dict__:
            descriptor = klass.__dict__["mail_ID"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "reg_Num" in params, "Missing parameter 'reg_Num'"
    assert "mail_ID" in params, "Missing parameter 'mail_ID'"
    assert "name" in params, "Missing parameter 'name'"

def test_student_has_reg_Num():
    assert hasattr(Student, "reg_Num")
    descriptor = None
    for klass in Student.__mro__:
        if "reg_Num" in klass.__dict__:
            descriptor = klass.__dict__["reg_Num"]
            break
    assert isinstance(descriptor, property)

def test_student_has_mail_ID():
    assert hasattr(Student, "mail_ID")
    descriptor = None
    for klass in Student.__mro__:
        if "mail_ID" in klass.__dict__:
            descriptor = klass.__dict__["mail_ID"]
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



def test_logout_usecase_is_not_abstract():
    assert not inspect.isabstract(Logout_UseCase)


def test_logout_usecase_constructor_exists():
    assert callable(Logout_UseCase.__init__)


def test_logout_usecase_constructor_args():
    sig = inspect.signature(Logout_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_view_questions_and_post_answers_usecase_is_not_abstract():
    assert not inspect.isabstract(View_Questions_And_Post_Answers_UseCase)


def test_view_questions_and_post_answers_usecase_constructor_exists():
    assert callable(View_Questions_And_Post_Answers_UseCase.__init__)


def test_view_questions_and_post_answers_usecase_constructor_args():
    sig = inspect.signature(View_Questions_And_Post_Answers_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_post_questions_usecase_is_not_abstract():
    assert not inspect.isabstract(Post_Questions_UseCase)


def test_post_questions_usecase_constructor_exists():
    assert callable(Post_Questions_UseCase.__init__)


def test_post_questions_usecase_constructor_args():
    sig = inspect.signature(Post_Questions_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_view_the_uploaded_materials_usecase_is_not_abstract():
    assert not inspect.isabstract(View_The_Uploaded_Materials_UseCase)


def test_view_the_uploaded_materials_usecase_constructor_exists():
    assert callable(View_The_Uploaded_Materials_UseCase.__init__)


def test_view_the_uploaded_materials_usecase_constructor_args():
    sig = inspect.signature(View_The_Uploaded_Materials_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_manage_student___faculty_list_usecase_is_not_abstract():
    assert not inspect.isabstract(Manage_Student___Faculty_List_UseCase)


def test_manage_student___faculty_list_usecase_constructor_exists():
    assert callable(Manage_Student___Faculty_List_UseCase.__init__)


def test_manage_student___faculty_list_usecase_constructor_args():
    sig = inspect.signature(Manage_Student___Faculty_List_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_view___modify_the_uploaded_materials_usecase_is_not_abstract():
    assert not inspect.isabstract(View___Modify_the_Uploaded_Materials_UseCase)


def test_view___modify_the_uploaded_materials_usecase_constructor_exists():
    assert callable(View___Modify_the_Uploaded_Materials_UseCase.__init__)


def test_view___modify_the_uploaded_materials_usecase_constructor_args():
    sig = inspect.signature(View___Modify_the_Uploaded_Materials_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_upload_materials_usecase_is_not_abstract():
    assert not inspect.isabstract(Upload_Materials_UseCase)


def test_upload_materials_usecase_constructor_exists():
    assert callable(Upload_Materials_UseCase.__init__)


def test_upload_materials_usecase_constructor_args():
    sig = inspect.signature(Upload_Materials_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase)


def test_login_usecase_constructor_exists():
    assert callable(Login_UseCase.__init__)


def test_login_usecase_constructor_args():
    sig = inspect.signature(Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_signup_usecase_is_not_abstract():
    assert not inspect.isabstract(SignUp_UseCase)


def test_signup_usecase_constructor_exists():
    assert callable(SignUp_UseCase.__init__)


def test_signup_usecase_constructor_args():
    sig = inspect.signature(SignUp_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_faculty__actor_is_not_abstract():
    assert not inspect.isabstract(Faculty__Actor)


def test_faculty__actor_constructor_exists():
    assert callable(Faculty__Actor.__init__)


def test_faculty__actor_constructor_args():
    sig = inspect.signature(Faculty__Actor.__init__)
    params = list(sig.parameters.keys())



def test_student_actor_is_not_abstract():
    assert not inspect.isabstract(Student_Actor)


def test_student_actor_constructor_exists():
    assert callable(Student_Actor.__init__)


def test_student_actor_constructor_args():
    sig = inspect.signature(Student_Actor.__init__)
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
Admin_strategy = st.builds(
    Admin,
    name=
        safe_text,
    mail_ID=
        safe_text
)
Faculty_strategy = st.builds(
    Faculty,
    name=
        safe_text,
    emp_ID=
        safe_text,
    mail_ID=
        safe_text
)
Student_strategy = st.builds(
    Student,
    reg_Num=
        safe_text,
    mail_ID=
        safe_text,
    name=
        safe_text
)
Logout_UseCase_strategy = st.builds(
    Logout_UseCase,
)
View_Questions_And_Post_Answers_UseCase_strategy = st.builds(
    View_Questions_And_Post_Answers_UseCase,
)
Post_Questions_UseCase_strategy = st.builds(
    Post_Questions_UseCase,
)
View_The_Uploaded_Materials_UseCase_strategy = st.builds(
    View_The_Uploaded_Materials_UseCase,
)
Manage_Student___Faculty_List_UseCase_strategy = st.builds(
    Manage_Student___Faculty_List_UseCase,
)
View___Modify_the_Uploaded_Materials_UseCase_strategy = st.builds(
    View___Modify_the_Uploaded_Materials_UseCase,
)
Upload_Materials_UseCase_strategy = st.builds(
    Upload_Materials_UseCase,
)
Login_UseCase_strategy = st.builds(
    Login_UseCase,
)
SignUp_UseCase_strategy = st.builds(
    SignUp_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Faculty__Actor_strategy = st.builds(
    Faculty__Actor,
)
Student_Actor_strategy = st.builds(
    Student_Actor,
)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Admin_strategy)
def test_admin_mail_ID_setter(instance):
    original = instance.mail_ID
    instance.mail_ID = original
    assert instance.mail_ID == original

@given(instance=Faculty_strategy)
@settings(max_examples=50)
def test_faculty_instantiation(instance):
    assert isinstance(instance, Faculty)



@given(instance=Faculty_strategy)
def test_faculty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Faculty_strategy)
def test_faculty_emp_ID_setter(instance):
    original = instance.emp_ID
    instance.emp_ID = original
    assert instance.emp_ID == original



@given(instance=Faculty_strategy)
def test_faculty_mail_ID_setter(instance):
    original = instance.mail_ID
    instance.mail_ID = original
    assert instance.mail_ID == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_reg_Num_setter(instance):
    original = instance.reg_Num
    instance.reg_Num = original
    assert instance.reg_Num == original



@given(instance=Student_strategy)
def test_student_mail_ID_setter(instance):
    original = instance.mail_ID
    instance.mail_ID = original
    assert instance.mail_ID == original



@given(instance=Student_strategy)
def test_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Logout_UseCase_strategy)
@settings(max_examples=50)
def test_logout_usecase_instantiation(instance):
    assert isinstance(instance, Logout_UseCase)

@given(instance=View_Questions_And_Post_Answers_UseCase_strategy)
@settings(max_examples=50)
def test_view_questions_and_post_answers_usecase_instantiation(instance):
    assert isinstance(instance, View_Questions_And_Post_Answers_UseCase)

@given(instance=Post_Questions_UseCase_strategy)
@settings(max_examples=50)
def test_post_questions_usecase_instantiation(instance):
    assert isinstance(instance, Post_Questions_UseCase)

@given(instance=View_The_Uploaded_Materials_UseCase_strategy)
@settings(max_examples=50)
def test_view_the_uploaded_materials_usecase_instantiation(instance):
    assert isinstance(instance, View_The_Uploaded_Materials_UseCase)

@given(instance=Manage_Student___Faculty_List_UseCase_strategy)
@settings(max_examples=50)
def test_manage_student___faculty_list_usecase_instantiation(instance):
    assert isinstance(instance, Manage_Student___Faculty_List_UseCase)

@given(instance=View___Modify_the_Uploaded_Materials_UseCase_strategy)
@settings(max_examples=50)
def test_view___modify_the_uploaded_materials_usecase_instantiation(instance):
    assert isinstance(instance, View___Modify_the_Uploaded_Materials_UseCase)

@given(instance=Upload_Materials_UseCase_strategy)
@settings(max_examples=50)
def test_upload_materials_usecase_instantiation(instance):
    assert isinstance(instance, Upload_Materials_UseCase)

@given(instance=Login_UseCase_strategy)
@settings(max_examples=50)
def test_login_usecase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)

@given(instance=SignUp_UseCase_strategy)
@settings(max_examples=50)
def test_signup_usecase_instantiation(instance):
    assert isinstance(instance, SignUp_UseCase)

@given(instance=Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)

@given(instance=Faculty__Actor_strategy)
@settings(max_examples=50)
def test_faculty__actor_instantiation(instance):
    assert isinstance(instance, Faculty__Actor)

@given(instance=Student_Actor_strategy)
@settings(max_examples=50)
def test_student_actor_instantiation(instance):
    assert isinstance(instance, Student_Actor)
