import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Dessert,
    Main_Course,
    Login,
    Bio_Info,
    Social_Media,
    Visitor_Comment,
    Drinks,
    Vegetarian,
    Browse_Recipes,
    Return,
    Profile_Page,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dessert_is_not_abstract():
    assert not inspect.isabstract(Dessert)


def test_dessert_constructor_exists():
    assert callable(Dessert.__init__)


def test_dessert_constructor_args():
    sig = inspect.signature(Dessert.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dessert_has_name():
    assert hasattr(Dessert, "name")
    descriptor = None
    for klass in Dessert.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_main_course_is_not_abstract():
    assert not inspect.isabstract(Main_Course)


def test_main_course_constructor_exists():
    assert callable(Main_Course.__init__)


def test_main_course_constructor_args():
    sig = inspect.signature(Main_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main_course_has_name():
    assert hasattr(Main_Course, "name")
    descriptor = None
    for klass in Main_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_bio_info_is_not_abstract():
    assert not inspect.isabstract(Bio_Info)


def test_bio_info_constructor_exists():
    assert callable(Bio_Info.__init__)


def test_bio_info_constructor_args():
    sig = inspect.signature(Bio_Info.__init__)
    params = list(sig.parameters.keys())
    assert "favourite_cuisine" in params, "Missing parameter 'favourite_cuisine'"
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "average_ratings" in params, "Missing parameter 'average_ratings'"

def test_bio_info_has_favourite_cuisine():
    assert hasattr(Bio_Info, "favourite_cuisine")
    descriptor = None
    for klass in Bio_Info.__mro__:
        if "favourite_cuisine" in klass.__dict__:
            descriptor = klass.__dict__["favourite_cuisine"]
            break
    assert isinstance(descriptor, property)

def test_bio_info_has_name():
    assert hasattr(Bio_Info, "name")
    descriptor = None
    for klass in Bio_Info.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bio_info_has_age():
    assert hasattr(Bio_Info, "age")
    descriptor = None
    for klass in Bio_Info.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_bio_info_has_average_ratings():
    assert hasattr(Bio_Info, "average_ratings")
    descriptor = None
    for klass in Bio_Info.__mro__:
        if "average_ratings" in klass.__dict__:
            descriptor = klass.__dict__["average_ratings"]
            break
    assert isinstance(descriptor, property)



def test_social_media_is_not_abstract():
    assert not inspect.isabstract(Social_Media)


def test_social_media_constructor_exists():
    assert callable(Social_Media.__init__)


def test_social_media_constructor_args():
    sig = inspect.signature(Social_Media.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_social_media_has_name():
    assert hasattr(Social_Media, "name")
    descriptor = None
    for klass in Social_Media.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_visitor_comment_is_not_abstract():
    assert not inspect.isabstract(Visitor_Comment)


def test_visitor_comment_constructor_exists():
    assert callable(Visitor_Comment.__init__)


def test_visitor_comment_constructor_args():
    sig = inspect.signature(Visitor_Comment.__init__)
    params = list(sig.parameters.keys())



def test_drinks_is_not_abstract():
    assert not inspect.isabstract(Drinks)


def test_drinks_constructor_exists():
    assert callable(Drinks.__init__)


def test_drinks_constructor_args():
    sig = inspect.signature(Drinks.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drinks_has_name():
    assert hasattr(Drinks, "name")
    descriptor = None
    for klass in Drinks.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vegetarian_is_not_abstract():
    assert not inspect.isabstract(Vegetarian)


def test_vegetarian_constructor_exists():
    assert callable(Vegetarian.__init__)


def test_vegetarian_constructor_args():
    sig = inspect.signature(Vegetarian.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vegetarian_has_name():
    assert hasattr(Vegetarian, "name")
    descriptor = None
    for klass in Vegetarian.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_browse_recipes_is_not_abstract():
    assert not inspect.isabstract(Browse_Recipes)


def test_browse_recipes_constructor_exists():
    assert callable(Browse_Recipes.__init__)


def test_browse_recipes_constructor_args():
    sig = inspect.signature(Browse_Recipes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_browse_recipes_has_name():
    assert hasattr(Browse_Recipes, "name")
    descriptor = None
    for klass in Browse_Recipes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_browse_recipes_has_description():
    assert hasattr(Browse_Recipes, "description")
    descriptor = None
    for klass in Browse_Recipes.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_return_is_not_abstract():
    assert not inspect.isabstract(Return)


def test_return_constructor_exists():
    assert callable(Return.__init__)


def test_return_constructor_args():
    sig = inspect.signature(Return.__init__)
    params = list(sig.parameters.keys())



def test_profile_page_is_not_abstract():
    assert not inspect.isabstract(Profile_Page)


def test_profile_page_constructor_exists():
    assert callable(Profile_Page.__init__)


def test_profile_page_constructor_args():
    sig = inspect.signature(Profile_Page.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_profile_page_has_username():
    assert hasattr(Profile_Page, "username")
    descriptor = None
    for klass in Profile_Page.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_profile_page_has_password():
    assert hasattr(Profile_Page, "password")
    descriptor = None
    for klass in Profile_Page.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_user_has_name():
    assert hasattr(User, "name")
    descriptor = None
    for klass in User.__mro__:
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
Dessert_strategy = st.builds(
    Dessert,
    name=
        safe_text
)
Main_Course_strategy = st.builds(
    Main_Course,
    name=
        safe_text
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    password=
        safe_text
)
Bio_Info_strategy = st.builds(
    Bio_Info,
    favourite_cuisine=
        safe_text,
    name=
        safe_text,
    age=
        safe_text,
    average_ratings=
        st.integers()
)
Social_Media_strategy = st.builds(
    Social_Media,
    name=
        safe_text
)
Visitor_Comment_strategy = st.builds(
    Visitor_Comment,
)
Drinks_strategy = st.builds(
    Drinks,
    name=
        safe_text
)
Vegetarian_strategy = st.builds(
    Vegetarian,
    name=
        safe_text
)
Browse_Recipes_strategy = st.builds(
    Browse_Recipes,
    name=
        safe_text,
    description=
        safe_text
)
Return_strategy = st.builds(
    Return,
)
Profile_Page_strategy = st.builds(
    Profile_Page,
    username=
        safe_text,
    password=
        safe_text
)
User_strategy = st.builds(
    User,
    name=
        safe_text
)

@given(instance=Dessert_strategy)
@settings(max_examples=50)
def test_dessert_instantiation(instance):
    assert isinstance(instance, Dessert)



@given(instance=Dessert_strategy)
def test_dessert_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Main_Course_strategy)
@settings(max_examples=50)
def test_main_course_instantiation(instance):
    assert isinstance(instance, Main_Course)



@given(instance=Main_Course_strategy)
def test_main_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Bio_Info_strategy)
@settings(max_examples=50)
def test_bio_info_instantiation(instance):
    assert isinstance(instance, Bio_Info)



@given(instance=Bio_Info_strategy)
def test_bio_info_favourite_cuisine_setter(instance):
    original = instance.favourite_cuisine
    instance.favourite_cuisine = original
    assert instance.favourite_cuisine == original



@given(instance=Bio_Info_strategy)
def test_bio_info_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Bio_Info_strategy)
def test_bio_info_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Bio_Info_strategy)
def test_bio_info_average_ratings_setter(instance):
    original = instance.average_ratings
    instance.average_ratings = original
    assert instance.average_ratings == original

@given(instance=Social_Media_strategy)
@settings(max_examples=50)
def test_social_media_instantiation(instance):
    assert isinstance(instance, Social_Media)



@given(instance=Social_Media_strategy)
def test_social_media_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Visitor_Comment_strategy)
@settings(max_examples=50)
def test_visitor_comment_instantiation(instance):
    assert isinstance(instance, Visitor_Comment)

@given(instance=Drinks_strategy)
@settings(max_examples=50)
def test_drinks_instantiation(instance):
    assert isinstance(instance, Drinks)



@given(instance=Drinks_strategy)
def test_drinks_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Vegetarian_strategy)
@settings(max_examples=50)
def test_vegetarian_instantiation(instance):
    assert isinstance(instance, Vegetarian)



@given(instance=Vegetarian_strategy)
def test_vegetarian_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Browse_Recipes_strategy)
@settings(max_examples=50)
def test_browse_recipes_instantiation(instance):
    assert isinstance(instance, Browse_Recipes)



@given(instance=Browse_Recipes_strategy)
def test_browse_recipes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Browse_Recipes_strategy)
def test_browse_recipes_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Return_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, Return)

@given(instance=Profile_Page_strategy)
@settings(max_examples=50)
def test_profile_page_instantiation(instance):
    assert isinstance(instance, Profile_Page)



@given(instance=Profile_Page_strategy)
def test_profile_page_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Profile_Page_strategy)
def test_profile_page_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
