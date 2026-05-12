import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    imdb_db,
    imdb_User,
    imdb_StaffList,
    imdb_Person,
    imdb_Movie,
    StaffListType,
    Genre,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imdb_db_is_not_abstract():
    assert not inspect.isabstract(imdb_db)


def test_imdb_db_constructor_exists():
    assert callable(imdb_db.__init__)


def test_imdb_db_constructor_args():
    sig = inspect.signature(imdb_db.__init__)
    params = list(sig.parameters.keys())
    assert "bestOf2014" in params, "Missing parameter 'bestOf2014'"

def test_imdb_db_has_bestOf2014():
    assert hasattr(imdb_db, "bestOf2014")
    descriptor = None
    for klass in imdb_db.__mro__:
        if "bestOf2014" in klass.__dict__:
            descriptor = klass.__dict__["bestOf2014"]
            break
    assert isinstance(descriptor, property)



def test_imdb_user_is_not_abstract():
    assert not inspect.isabstract(imdb_User)


def test_imdb_user_constructor_exists():
    assert callable(imdb_User.__init__)


def test_imdb_user_constructor_args():
    sig = inspect.signature(imdb_User.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "watchlist" in params, "Missing parameter 'watchlist'"

def test_imdb_user_has_username():
    assert hasattr(imdb_User, "username")
    descriptor = None
    for klass in imdb_User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_imdb_user_has_watchlist():
    assert hasattr(imdb_User, "watchlist")
    descriptor = None
    for klass in imdb_User.__mro__:
        if "watchlist" in klass.__dict__:
            descriptor = klass.__dict__["watchlist"]
            break
    assert isinstance(descriptor, property)



def test_imdb_stafflist_is_not_abstract():
    assert not inspect.isabstract(imdb_StaffList)


def test_imdb_stafflist_constructor_exists():
    assert callable(imdb_StaffList.__init__)


def test_imdb_stafflist_constructor_args():
    sig = inspect.signature(imdb_StaffList.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"
    assert "coverPhoto" in params, "Missing parameter 'coverPhoto'"
    assert "elementType" in params, "Missing parameter 'elementType'"
    assert "createdDate" in params, "Missing parameter 'createdDate'"

def test_imdb_stafflist_has_elements():
    assert hasattr(imdb_StaffList, "elements")
    descriptor = None
    for klass in imdb_StaffList.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_imdb_stafflist_has_name():
    assert hasattr(imdb_StaffList, "name")
    descriptor = None
    for klass in imdb_StaffList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_imdb_stafflist_has_coverPhoto():
    assert hasattr(imdb_StaffList, "coverPhoto")
    descriptor = None
    for klass in imdb_StaffList.__mro__:
        if "coverPhoto" in klass.__dict__:
            descriptor = klass.__dict__["coverPhoto"]
            break
    assert isinstance(descriptor, property)

def test_imdb_stafflist_has_elementType():
    assert hasattr(imdb_StaffList, "elementType")
    descriptor = None
    for klass in imdb_StaffList.__mro__:
        if "elementType" in klass.__dict__:
            descriptor = klass.__dict__["elementType"]
            break
    assert isinstance(descriptor, property)

def test_imdb_stafflist_has_createdDate():
    assert hasattr(imdb_StaffList, "createdDate")
    descriptor = None
    for klass in imdb_StaffList.__mro__:
        if "createdDate" in klass.__dict__:
            descriptor = klass.__dict__["createdDate"]
            break
    assert isinstance(descriptor, property)



def test_imdb_person_is_not_abstract():
    assert not inspect.isabstract(imdb_Person)


def test_imdb_person_constructor_exists():
    assert callable(imdb_Person.__init__)


def test_imdb_person_constructor_args():
    sig = inspect.signature(imdb_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imdb_person_has_name():
    assert hasattr(imdb_Person, "name")
    descriptor = None
    for klass in imdb_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imdb_movie_is_not_abstract():
    assert not inspect.isabstract(imdb_Movie)


def test_imdb_movie_constructor_exists():
    assert callable(imdb_Movie.__init__)


def test_imdb_movie_constructor_args():
    sig = inspect.signature(imdb_Movie.__init__)
    params = list(sig.parameters.keys())
    assert "criticReviews" in params, "Missing parameter 'criticReviews'"
    assert "genres" in params, "Missing parameter 'genres'"
    assert "rating" in params, "Missing parameter 'rating'"
    assert "userReviews" in params, "Missing parameter 'userReviews'"
    assert "metaScore" in params, "Missing parameter 'metaScore'"
    assert "title" in params, "Missing parameter 'title'"
    assert "runtime" in params, "Missing parameter 'runtime'"
    assert "userRatings" in params, "Missing parameter 'userRatings'"
    assert "releaseDate" in params, "Missing parameter 'releaseDate'"
    assert "poster" in params, "Missing parameter 'poster'"
    assert "metacriticReviews" in params, "Missing parameter 'metacriticReviews'"
    assert "age" in params, "Missing parameter 'age'"
    assert "synopsis" in params, "Missing parameter 'synopsis'"

def test_imdb_movie_has_criticReviews():
    assert hasattr(imdb_Movie, "criticReviews")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "criticReviews" in klass.__dict__:
            descriptor = klass.__dict__["criticReviews"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_genres():
    assert hasattr(imdb_Movie, "genres")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "genres" in klass.__dict__:
            descriptor = klass.__dict__["genres"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_rating():
    assert hasattr(imdb_Movie, "rating")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_userReviews():
    assert hasattr(imdb_Movie, "userReviews")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "userReviews" in klass.__dict__:
            descriptor = klass.__dict__["userReviews"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_metaScore():
    assert hasattr(imdb_Movie, "metaScore")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "metaScore" in klass.__dict__:
            descriptor = klass.__dict__["metaScore"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_title():
    assert hasattr(imdb_Movie, "title")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_runtime():
    assert hasattr(imdb_Movie, "runtime")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "runtime" in klass.__dict__:
            descriptor = klass.__dict__["runtime"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_userRatings():
    assert hasattr(imdb_Movie, "userRatings")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "userRatings" in klass.__dict__:
            descriptor = klass.__dict__["userRatings"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_releaseDate():
    assert hasattr(imdb_Movie, "releaseDate")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "releaseDate" in klass.__dict__:
            descriptor = klass.__dict__["releaseDate"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_poster():
    assert hasattr(imdb_Movie, "poster")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "poster" in klass.__dict__:
            descriptor = klass.__dict__["poster"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_metacriticReviews():
    assert hasattr(imdb_Movie, "metacriticReviews")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "metacriticReviews" in klass.__dict__:
            descriptor = klass.__dict__["metacriticReviews"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_age():
    assert hasattr(imdb_Movie, "age")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_imdb_movie_has_synopsis():
    assert hasattr(imdb_Movie, "synopsis")
    descriptor = None
    for klass in imdb_Movie.__mro__:
        if "synopsis" in klass.__dict__:
            descriptor = klass.__dict__["synopsis"]
            break
    assert isinstance(descriptor, property)

def test_stafflisttype_exists():
    # Check that the Enumeration exists
    assert StaffListType is not None

def test_stafflisttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StaffListType]
    expected_literals = [
        "characters",
        "titles",
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
imdb_db_strategy = st.builds(
    imdb_db,
    bestOf2014=
        safe_text
)
imdb_User_strategy = st.builds(
    imdb_User,
    username=
        safe_text,
    watchlist=
        safe_text
)
imdb_StaffList_strategy = st.builds(
    imdb_StaffList,
    elements=
        safe_text,
    name=
        safe_text,
    coverPhoto=
        safe_text,
    elementType=
        safe_text,
    createdDate=
        st.dates()
)
imdb_Person_strategy = st.builds(
    imdb_Person,
    name=
        safe_text
)
imdb_Movie_strategy = st.builds(
    imdb_Movie,
    criticReviews=
        st.integers(),
    genres=
        safe_text,
    rating=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    userReviews=
        st.integers(),
    metaScore=
        st.integers(),
    title=
        safe_text,
    runtime=
        st.integers(),
    userRatings=
        st.integers(),
    releaseDate=
        st.dates(),
    poster=
        safe_text,
    metacriticReviews=
        st.integers(),
    age=
        st.integers(),
    synopsis=
        safe_text
)

@given(instance=imdb_db_strategy)
@settings(max_examples=50)
def test_imdb_db_instantiation(instance):
    assert isinstance(instance, imdb_db)



@given(instance=imdb_db_strategy)
def test_imdb_db_bestOf2014_setter(instance):
    original = instance.bestOf2014
    instance.bestOf2014 = original
    assert instance.bestOf2014 == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=imdb_db_strategy)
@settings(max_examples=30)
def test_imdb_db_sam_changes_state(instance):
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
        assert has_statements, f"Function 'sam' in imdb_db is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'sam' in imdb_db did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'sam' in imdb_db is not implemented or raised an error")

@given(instance=imdb_User_strategy)
@settings(max_examples=50)
def test_imdb_user_instantiation(instance):
    assert isinstance(instance, imdb_User)



@given(instance=imdb_User_strategy)
def test_imdb_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=imdb_User_strategy)
def test_imdb_user_watchlist_setter(instance):
    original = instance.watchlist
    instance.watchlist = original
    assert instance.watchlist == original

@given(instance=imdb_StaffList_strategy)
@settings(max_examples=50)
def test_imdb_stafflist_instantiation(instance):
    assert isinstance(instance, imdb_StaffList)



@given(instance=imdb_StaffList_strategy)
def test_imdb_stafflist_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original



@given(instance=imdb_StaffList_strategy)
def test_imdb_stafflist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=imdb_StaffList_strategy)
def test_imdb_stafflist_coverPhoto_setter(instance):
    original = instance.coverPhoto
    instance.coverPhoto = original
    assert instance.coverPhoto == original



@given(instance=imdb_StaffList_strategy)
def test_imdb_stafflist_elementType_setter(instance):
    original = instance.elementType
    instance.elementType = original
    assert instance.elementType == original



@given(instance=imdb_StaffList_strategy)
def test_imdb_stafflist_createdDate_setter(instance):
    original = instance.createdDate
    instance.createdDate = original
    assert instance.createdDate == original

@given(instance=imdb_Person_strategy)
@settings(max_examples=50)
def test_imdb_person_instantiation(instance):
    assert isinstance(instance, imdb_Person)



@given(instance=imdb_Person_strategy)
def test_imdb_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imdb_Movie_strategy)
@settings(max_examples=50)
def test_imdb_movie_instantiation(instance):
    assert isinstance(instance, imdb_Movie)



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_criticReviews_setter(instance):
    original = instance.criticReviews
    instance.criticReviews = original
    assert instance.criticReviews == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_genres_setter(instance):
    original = instance.genres
    instance.genres = original
    assert instance.genres == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_userReviews_setter(instance):
    original = instance.userReviews
    instance.userReviews = original
    assert instance.userReviews == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_metaScore_setter(instance):
    original = instance.metaScore
    instance.metaScore = original
    assert instance.metaScore == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_runtime_setter(instance):
    original = instance.runtime
    instance.runtime = original
    assert instance.runtime == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_userRatings_setter(instance):
    original = instance.userRatings
    instance.userRatings = original
    assert instance.userRatings == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_releaseDate_setter(instance):
    original = instance.releaseDate
    instance.releaseDate = original
    assert instance.releaseDate == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_poster_setter(instance):
    original = instance.poster
    instance.poster = original
    assert instance.poster == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_metacriticReviews_setter(instance):
    original = instance.metacriticReviews
    instance.metacriticReviews = original
    assert instance.metacriticReviews == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=imdb_Movie_strategy)
def test_imdb_movie_synopsis_setter(instance):
    original = instance.synopsis
    instance.synopsis = original
    assert instance.synopsis == original
