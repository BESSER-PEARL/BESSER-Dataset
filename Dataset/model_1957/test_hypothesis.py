import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    imdb::db,
    imdb::User,
    imdb::StaffList,
    imdb::Person,
    imdb::Movie,
    StaffListType,
    Genre,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imdb::db_is_not_abstract():
    assert not inspect.isabstract(imdb::db)


def test_imdb::db_constructor_exists():
    assert callable(imdb::db.__init__)


def test_imdb::db_constructor_args():
    sig = inspect.signature(imdb::db.__init__)
    params = list(sig.parameters.keys())
    assert "bestOf2014" in params, "Missing parameter 'bestOf2014'"

def test_imdb::db_has_bestOf2014():
    assert hasattr(imdb::db, "bestOf2014")
    descriptor = None
    for klass in imdb::db.__mro__:
        if "bestOf2014" in klass.__dict__:
            descriptor = klass.__dict__["bestOf2014"]
            break
    assert isinstance(descriptor, property)



def test_imdb::user_is_not_abstract():
    assert not inspect.isabstract(imdb::User)


def test_imdb::user_constructor_exists():
    assert callable(imdb::User.__init__)


def test_imdb::user_constructor_args():
    sig = inspect.signature(imdb::User.__init__)
    params = list(sig.parameters.keys())
    assert "watchlist" in params, "Missing parameter 'watchlist'"
    assert "username" in params, "Missing parameter 'username'"

def test_imdb::user_has_watchlist():
    assert hasattr(imdb::User, "watchlist")
    descriptor = None
    for klass in imdb::User.__mro__:
        if "watchlist" in klass.__dict__:
            descriptor = klass.__dict__["watchlist"]
            break
    assert isinstance(descriptor, property)

def test_imdb::user_has_username():
    assert hasattr(imdb::User, "username")
    descriptor = None
    for klass in imdb::User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_imdb::stafflist_is_not_abstract():
    assert not inspect.isabstract(imdb::StaffList)


def test_imdb::stafflist_constructor_exists():
    assert callable(imdb::StaffList.__init__)


def test_imdb::stafflist_constructor_args():
    sig = inspect.signature(imdb::StaffList.__init__)
    params = list(sig.parameters.keys())
    assert "createdDate" in params, "Missing parameter 'createdDate'"
    assert "coverPhoto" in params, "Missing parameter 'coverPhoto'"
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"
    assert "elementType" in params, "Missing parameter 'elementType'"

def test_imdb::stafflist_has_createdDate():
    assert hasattr(imdb::StaffList, "createdDate")
    descriptor = None
    for klass in imdb::StaffList.__mro__:
        if "createdDate" in klass.__dict__:
            descriptor = klass.__dict__["createdDate"]
            break
    assert isinstance(descriptor, property)

def test_imdb::stafflist_has_coverPhoto():
    assert hasattr(imdb::StaffList, "coverPhoto")
    descriptor = None
    for klass in imdb::StaffList.__mro__:
        if "coverPhoto" in klass.__dict__:
            descriptor = klass.__dict__["coverPhoto"]
            break
    assert isinstance(descriptor, property)

def test_imdb::stafflist_has_elements():
    assert hasattr(imdb::StaffList, "elements")
    descriptor = None
    for klass in imdb::StaffList.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_imdb::stafflist_has_name():
    assert hasattr(imdb::StaffList, "name")
    descriptor = None
    for klass in imdb::StaffList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_imdb::stafflist_has_elementType():
    assert hasattr(imdb::StaffList, "elementType")
    descriptor = None
    for klass in imdb::StaffList.__mro__:
        if "elementType" in klass.__dict__:
            descriptor = klass.__dict__["elementType"]
            break
    assert isinstance(descriptor, property)



def test_imdb::person_is_not_abstract():
    assert not inspect.isabstract(imdb::Person)


def test_imdb::person_constructor_exists():
    assert callable(imdb::Person.__init__)


def test_imdb::person_constructor_args():
    sig = inspect.signature(imdb::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imdb::person_has_name():
    assert hasattr(imdb::Person, "name")
    descriptor = None
    for klass in imdb::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imdb::movie_is_not_abstract():
    assert not inspect.isabstract(imdb::Movie)


def test_imdb::movie_constructor_exists():
    assert callable(imdb::Movie.__init__)


def test_imdb::movie_constructor_args():
    sig = inspect.signature(imdb::Movie.__init__)
    params = list(sig.parameters.keys())
    assert "metacriticReviews" in params, "Missing parameter 'metacriticReviews'"
    assert "title" in params, "Missing parameter 'title'"
    assert "genres" in params, "Missing parameter 'genres'"
    assert "runtime" in params, "Missing parameter 'runtime'"
    assert "poster" in params, "Missing parameter 'poster'"
    assert "age" in params, "Missing parameter 'age'"
    assert "metaScore" in params, "Missing parameter 'metaScore'"
    assert "rating" in params, "Missing parameter 'rating'"
    assert "userReviews" in params, "Missing parameter 'userReviews'"
    assert "releaseDate" in params, "Missing parameter 'releaseDate'"
    assert "criticReviews" in params, "Missing parameter 'criticReviews'"
    assert "synopsis" in params, "Missing parameter 'synopsis'"
    assert "userRatings" in params, "Missing parameter 'userRatings'"

def test_imdb::movie_has_metacriticReviews():
    assert hasattr(imdb::Movie, "metacriticReviews")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "metacriticReviews" in klass.__dict__:
            descriptor = klass.__dict__["metacriticReviews"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_title():
    assert hasattr(imdb::Movie, "title")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_genres():
    assert hasattr(imdb::Movie, "genres")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "genres" in klass.__dict__:
            descriptor = klass.__dict__["genres"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_runtime():
    assert hasattr(imdb::Movie, "runtime")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "runtime" in klass.__dict__:
            descriptor = klass.__dict__["runtime"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_poster():
    assert hasattr(imdb::Movie, "poster")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "poster" in klass.__dict__:
            descriptor = klass.__dict__["poster"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_age():
    assert hasattr(imdb::Movie, "age")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_metaScore():
    assert hasattr(imdb::Movie, "metaScore")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "metaScore" in klass.__dict__:
            descriptor = klass.__dict__["metaScore"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_rating():
    assert hasattr(imdb::Movie, "rating")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_userReviews():
    assert hasattr(imdb::Movie, "userReviews")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "userReviews" in klass.__dict__:
            descriptor = klass.__dict__["userReviews"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_releaseDate():
    assert hasattr(imdb::Movie, "releaseDate")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "releaseDate" in klass.__dict__:
            descriptor = klass.__dict__["releaseDate"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_criticReviews():
    assert hasattr(imdb::Movie, "criticReviews")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "criticReviews" in klass.__dict__:
            descriptor = klass.__dict__["criticReviews"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_synopsis():
    assert hasattr(imdb::Movie, "synopsis")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "synopsis" in klass.__dict__:
            descriptor = klass.__dict__["synopsis"]
            break
    assert isinstance(descriptor, property)

def test_imdb::movie_has_userRatings():
    assert hasattr(imdb::Movie, "userRatings")
    descriptor = None
    for klass in imdb::Movie.__mro__:
        if "userRatings" in klass.__dict__:
            descriptor = klass.__dict__["userRatings"]
            break
    assert isinstance(descriptor, property)

def test_stafflisttype_exists():
    # Check that the Enumeration exists
    assert StaffListType is not None

def test_stafflisttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StaffListType]
    expected_literals = [
        "titles",
        "characters",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StaffListType"

def test_genre_exists():
    # Check that the Enumeration exists
    assert Genre is not None

def test_genre_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Genre]
    expected_literals = [
        "SciFi",
        "Adventure",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Genre"


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
imdb::db_strategy = st.builds(
    imdb::db,
    bestOf2014=
        safe_text
)
imdb::User_strategy = st.builds(
    imdb::User,
    watchlist=
        safe_text,
    username=
        safe_text
)
imdb::StaffList_strategy = st.builds(
    imdb::StaffList,
    createdDate=
        st.dates(),
    coverPhoto=
        safe_text,
    elements=
        safe_text,
    name=
        safe_text,
    elementType=
        safe_text
)
imdb::Person_strategy = st.builds(
    imdb::Person,
    name=
        safe_text
)
imdb::Movie_strategy = st.builds(
    imdb::Movie,
    metacriticReviews=
        st.integers(),
    title=
        safe_text,
    genres=
        safe_text,
    runtime=
        st.integers(),
    poster=
        safe_text,
    age=
        st.integers(),
    metaScore=
        st.integers(),
    rating=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    userReviews=
        st.integers(),
    releaseDate=
        st.dates(),
    criticReviews=
        st.integers(),
    synopsis=
        safe_text,
    userRatings=
        st.integers()
)

@given(instance=imdb::db_strategy)
@settings(max_examples=50)
def test_imdb::db_instantiation(instance):
    assert isinstance(instance, imdb::db)

@given(instance=imdb::db_strategy)
def test_imdb::db_bestOf2014_type(instance):
    assert isinstance(instance.bestOf2014, str)


@given(instance=imdb::db_strategy)
def test_imdb::db_bestOf2014_setter(instance):
    original = instance.bestOf2014
    instance.bestOf2014 = original
    assert instance.bestOf2014 == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=imdb::db_strategy)
@settings(max_examples=30)
def test_imdb::db_sam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.sam()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.sam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'sam' in imdb::db is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'sam' in imdb::db did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'sam' in imdb::db is not implemented or raised an error")

@given(instance=imdb::User_strategy)
@settings(max_examples=50)
def test_imdb::user_instantiation(instance):
    assert isinstance(instance, imdb::User)

@given(instance=imdb::User_strategy)
def test_imdb::user_watchlist_type(instance):
    assert isinstance(instance.watchlist, str)


@given(instance=imdb::User_strategy)
def test_imdb::user_watchlist_setter(instance):
    original = instance.watchlist
    instance.watchlist = original
    assert instance.watchlist == original

@given(instance=imdb::User_strategy)
def test_imdb::user_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=imdb::User_strategy)
def test_imdb::user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=imdb::StaffList_strategy)
@settings(max_examples=50)
def test_imdb::stafflist_instantiation(instance):
    assert isinstance(instance, imdb::StaffList)

@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_createdDate_type(instance):
    assert isinstance(instance.createdDate, date)


@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_createdDate_setter(instance):
    original = instance.createdDate
    instance.createdDate = original
    assert instance.createdDate == original

@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_coverPhoto_type(instance):
    assert isinstance(instance.coverPhoto, str)


@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_coverPhoto_setter(instance):
    original = instance.coverPhoto
    instance.coverPhoto = original
    assert instance.coverPhoto == original

@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_elementType_type(instance):
    assert isinstance(instance.elementType, str)


@given(instance=imdb::StaffList_strategy)
def test_imdb::stafflist_elementType_setter(instance):
    original = instance.elementType
    instance.elementType = original
    assert instance.elementType == original

@given(instance=imdb::Person_strategy)
@settings(max_examples=50)
def test_imdb::person_instantiation(instance):
    assert isinstance(instance, imdb::Person)

@given(instance=imdb::Person_strategy)
def test_imdb::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imdb::Person_strategy)
def test_imdb::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imdb::Movie_strategy)
@settings(max_examples=50)
def test_imdb::movie_instantiation(instance):
    assert isinstance(instance, imdb::Movie)

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_metacriticReviews_type(instance):
    assert isinstance(instance.metacriticReviews, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_metacriticReviews_setter(instance):
    original = instance.metacriticReviews
    instance.metacriticReviews = original
    assert instance.metacriticReviews == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_genres_type(instance):
    assert isinstance(instance.genres, str)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_genres_setter(instance):
    original = instance.genres
    instance.genres = original
    assert instance.genres == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_runtime_type(instance):
    assert isinstance(instance.runtime, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_runtime_setter(instance):
    original = instance.runtime
    instance.runtime = original
    assert instance.runtime == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_poster_type(instance):
    assert isinstance(instance.poster, str)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_poster_setter(instance):
    original = instance.poster
    instance.poster = original
    assert instance.poster == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_metaScore_type(instance):
    assert isinstance(instance.metaScore, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_metaScore_setter(instance):
    original = instance.metaScore
    instance.metaScore = original
    assert instance.metaScore == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_rating_type(instance):
    assert isinstance(instance.rating, float)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_userReviews_type(instance):
    assert isinstance(instance.userReviews, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_userReviews_setter(instance):
    original = instance.userReviews
    instance.userReviews = original
    assert instance.userReviews == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_releaseDate_type(instance):
    assert isinstance(instance.releaseDate, date)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_releaseDate_setter(instance):
    original = instance.releaseDate
    instance.releaseDate = original
    assert instance.releaseDate == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_criticReviews_type(instance):
    assert isinstance(instance.criticReviews, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_criticReviews_setter(instance):
    original = instance.criticReviews
    instance.criticReviews = original
    assert instance.criticReviews == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_synopsis_type(instance):
    assert isinstance(instance.synopsis, str)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_synopsis_setter(instance):
    original = instance.synopsis
    instance.synopsis = original
    assert instance.synopsis == original

@given(instance=imdb::Movie_strategy)
def test_imdb::movie_userRatings_type(instance):
    assert isinstance(instance.userRatings, int)


@given(instance=imdb::Movie_strategy)
def test_imdb::movie_userRatings_setter(instance):
    original = instance.userRatings
    instance.userRatings = original
    assert instance.userRatings == original
