import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Users,
    Reviews,
    Places,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "date_joined" in params, "Missing parameter 'date_joined'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "average_star" in params, "Missing parameter 'average_star'"
    assert "review_count" in params, "Missing parameter 'review_count'"
    assert "name" in params, "Missing parameter 'name'"

def test_users_has_date_joined():
    assert hasattr(Users, "date_joined")
    descriptor = None
    for klass in Users.__mro__:
        if "date_joined" in klass.__dict__:
            descriptor = klass.__dict__["date_joined"]
            break
    assert isinstance(descriptor, property)

def test_users_has_ID():
    assert hasattr(Users, "ID")
    descriptor = None
    for klass in Users.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_users_has_average_star():
    assert hasattr(Users, "average_star")
    descriptor = None
    for klass in Users.__mro__:
        if "average_star" in klass.__dict__:
            descriptor = klass.__dict__["average_star"]
            break
    assert isinstance(descriptor, property)

def test_users_has_review_count():
    assert hasattr(Users, "review_count")
    descriptor = None
    for klass in Users.__mro__:
        if "review_count" in klass.__dict__:
            descriptor = klass.__dict__["review_count"]
            break
    assert isinstance(descriptor, property)

def test_users_has_name():
    assert hasattr(Users, "name")
    descriptor = None
    for klass in Users.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_reviews_is_not_abstract():
    assert not inspect.isabstract(Reviews)


def test_reviews_constructor_exists():
    assert callable(Reviews.__init__)


def test_reviews_constructor_args():
    sig = inspect.signature(Reviews.__init__)
    params = list(sig.parameters.keys())
    assert "business_id" in params, "Missing parameter 'business_id'"
    assert "rating" in params, "Missing parameter 'rating'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "text" in params, "Missing parameter 'text'"

def test_reviews_has_business_id():
    assert hasattr(Reviews, "business_id")
    descriptor = None
    for klass in Reviews.__mro__:
        if "business_id" in klass.__dict__:
            descriptor = klass.__dict__["business_id"]
            break
    assert isinstance(descriptor, property)

def test_reviews_has_rating():
    assert hasattr(Reviews, "rating")
    descriptor = None
    for klass in Reviews.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_reviews_has_ID():
    assert hasattr(Reviews, "ID")
    descriptor = None
    for klass in Reviews.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_reviews_has_user_id():
    assert hasattr(Reviews, "user_id")
    descriptor = None
    for klass in Reviews.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_reviews_has_date():
    assert hasattr(Reviews, "date")
    descriptor = None
    for klass in Reviews.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_reviews_has_text():
    assert hasattr(Reviews, "text")
    descriptor = None
    for klass in Reviews.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_places_is_not_abstract():
    assert not inspect.isabstract(Places)


def test_places_constructor_exists():
    assert callable(Places.__init__)


def test_places_constructor_args():
    sig = inspect.signature(Places.__init__)
    params = list(sig.parameters.keys())
    assert "wifi" in params, "Missing parameter 'wifi'"
    assert "plugs" in params, "Missing parameter 'plugs'"
    assert "place_id" in params, "Missing parameter 'place_id'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "address" in params, "Missing parameter 'address'"
    assert "opening_times" in params, "Missing parameter 'opening_times'"
    assert "music" in params, "Missing parameter 'music'"
    assert "review_count" in params, "Missing parameter 'review_count'"

def test_places_has_wifi():
    assert hasattr(Places, "wifi")
    descriptor = None
    for klass in Places.__mro__:
        if "wifi" in klass.__dict__:
            descriptor = klass.__dict__["wifi"]
            break
    assert isinstance(descriptor, property)

def test_places_has_plugs():
    assert hasattr(Places, "plugs")
    descriptor = None
    for klass in Places.__mro__:
        if "plugs" in klass.__dict__:
            descriptor = klass.__dict__["plugs"]
            break
    assert isinstance(descriptor, property)

def test_places_has_place_id():
    assert hasattr(Places, "place_id")
    descriptor = None
    for klass in Places.__mro__:
        if "place_id" in klass.__dict__:
            descriptor = klass.__dict__["place_id"]
            break
    assert isinstance(descriptor, property)

def test_places_has_ID():
    assert hasattr(Places, "ID")
    descriptor = None
    for klass in Places.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_places_has_address():
    assert hasattr(Places, "address")
    descriptor = None
    for klass in Places.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_places_has_opening_times():
    assert hasattr(Places, "opening_times")
    descriptor = None
    for klass in Places.__mro__:
        if "opening_times" in klass.__dict__:
            descriptor = klass.__dict__["opening_times"]
            break
    assert isinstance(descriptor, property)

def test_places_has_music():
    assert hasattr(Places, "music")
    descriptor = None
    for klass in Places.__mro__:
        if "music" in klass.__dict__:
            descriptor = klass.__dict__["music"]
            break
    assert isinstance(descriptor, property)

def test_places_has_review_count():
    assert hasattr(Places, "review_count")
    descriptor = None
    for klass in Places.__mro__:
        if "review_count" in klass.__dict__:
            descriptor = klass.__dict__["review_count"]
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
Users_strategy = st.builds(
    Users,
    date_joined=
        st.dates(),
    ID=
        st.integers(),
    average_star=
        st.integers(),
    review_count=
        st.integers(),
    name=
        safe_text
)
Reviews_strategy = st.builds(
    Reviews,
    business_id=
        st.integers(),
    rating=
        st.integers(),
    ID=
        st.integers(),
    user_id=
        st.integers(),
    date=
        st.dates(),
    text=
        safe_text
)
Places_strategy = st.builds(
    Places,
    wifi=
        safe_text,
    plugs=
        safe_text,
    place_id=
        safe_text,
    ID=
        st.integers(),
    address=
        safe_text,
    opening_times=
        st.dates(),
    music=
        safe_text,
    review_count=
        st.integers()
)

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_date_joined_setter(instance):
    original = instance.date_joined
    instance.date_joined = original
    assert instance.date_joined == original



@given(instance=Users_strategy)
def test_users_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Users_strategy)
def test_users_average_star_setter(instance):
    original = instance.average_star
    instance.average_star = original
    assert instance.average_star == original



@given(instance=Users_strategy)
def test_users_review_count_setter(instance):
    original = instance.review_count
    instance.review_count = original
    assert instance.review_count == original



@given(instance=Users_strategy)
def test_users_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Reviews_strategy)
@settings(max_examples=50)
def test_reviews_instantiation(instance):
    assert isinstance(instance, Reviews)



@given(instance=Reviews_strategy)
def test_reviews_business_id_setter(instance):
    original = instance.business_id
    instance.business_id = original
    assert instance.business_id == original



@given(instance=Reviews_strategy)
def test_reviews_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original



@given(instance=Reviews_strategy)
def test_reviews_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Reviews_strategy)
def test_reviews_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Reviews_strategy)
def test_reviews_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Reviews_strategy)
def test_reviews_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Places_strategy)
@settings(max_examples=50)
def test_places_instantiation(instance):
    assert isinstance(instance, Places)



@given(instance=Places_strategy)
def test_places_wifi_setter(instance):
    original = instance.wifi
    instance.wifi = original
    assert instance.wifi == original



@given(instance=Places_strategy)
def test_places_plugs_setter(instance):
    original = instance.plugs
    instance.plugs = original
    assert instance.plugs == original



@given(instance=Places_strategy)
def test_places_place_id_setter(instance):
    original = instance.place_id
    instance.place_id = original
    assert instance.place_id == original



@given(instance=Places_strategy)
def test_places_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Places_strategy)
def test_places_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Places_strategy)
def test_places_opening_times_setter(instance):
    original = instance.opening_times
    instance.opening_times = original
    assert instance.opening_times == original



@given(instance=Places_strategy)
def test_places_music_setter(instance):
    original = instance.music
    instance.music = original
    assert instance.music == original



@given(instance=Places_strategy)
def test_places_review_count_setter(instance):
    original = instance.review_count
    instance.review_count = original
    assert instance.review_count == original
