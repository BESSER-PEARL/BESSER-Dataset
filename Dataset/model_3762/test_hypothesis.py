import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    movies::Place,
    movies::MoviesDB,
    CriticsReview,
    movies::CustomerReview,
    movies::Movie,
    movies::CriticsReview,
    movies::Copy,
    GenreTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_movies::place_is_not_abstract():
    assert not inspect.isabstract(movies::Place)


def test_movies::place_constructor_exists():
    assert callable(movies::Place.__init__)


def test_movies::place_constructor_args():
    sig = inspect.signature(movies::Place.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_movies::place_has_id():
    assert hasattr(movies::Place, "id")
    descriptor = None
    for klass in movies::Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_movies::place_has_name():
    assert hasattr(movies::Place, "name")
    descriptor = None
    for klass in movies::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_movies::moviesdb_is_not_abstract():
    assert not inspect.isabstract(movies::MoviesDB)


def test_movies::moviesdb_constructor_exists():
    assert callable(movies::MoviesDB.__init__)


def test_movies::moviesdb_constructor_args():
    sig = inspect.signature(movies::MoviesDB.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_movies::moviesdb_has_comment():
    assert hasattr(movies::MoviesDB, "comment")
    descriptor = None
    for klass in movies::MoviesDB.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_criticsreview_is_not_abstract():
    assert not inspect.isabstract(CriticsReview)


def test_criticsreview_constructor_exists():
    assert callable(CriticsReview.__init__)


def test_criticsreview_constructor_args():
    sig = inspect.signature(CriticsReview.__init__)
    params = list(sig.parameters.keys())



def test_movies::customerreview_is_not_abstract():
    assert not inspect.isabstract(movies::CustomerReview)


def test_movies::customerreview_constructor_exists():
    assert callable(movies::CustomerReview.__init__)


def test_movies::customerreview_constructor_args():
    sig = inspect.signature(movies::CustomerReview.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_movies::customerreview_has_comment():
    assert hasattr(movies::CustomerReview, "comment")
    descriptor = None
    for klass in movies::CustomerReview.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_movies::movie_is_not_abstract():
    assert not inspect.isabstract(movies::Movie)


def test_movies::movie_constructor_exists():
    assert callable(movies::Movie.__init__)


def test_movies::movie_constructor_args():
    sig = inspect.signature(movies::Movie.__init__)
    params = list(sig.parameters.keys())
    assert "actors" in params, "Missing parameter 'actors'"
    assert "summary" in params, "Missing parameter 'summary'"
    assert "genre" in params, "Missing parameter 'genre'"
    assert "title" in params, "Missing parameter 'title'"
    assert "director" in params, "Missing parameter 'director'"

def test_movies::movie_has_actors():
    assert hasattr(movies::Movie, "actors")
    descriptor = None
    for klass in movies::Movie.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_movies::movie_has_summary():
    assert hasattr(movies::Movie, "summary")
    descriptor = None
    for klass in movies::Movie.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_movies::movie_has_genre():
    assert hasattr(movies::Movie, "genre")
    descriptor = None
    for klass in movies::Movie.__mro__:
        if "genre" in klass.__dict__:
            descriptor = klass.__dict__["genre"]
            break
    assert isinstance(descriptor, property)

def test_movies::movie_has_title():
    assert hasattr(movies::Movie, "title")
    descriptor = None
    for klass in movies::Movie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_movies::movie_has_director():
    assert hasattr(movies::Movie, "director")
    descriptor = None
    for klass in movies::Movie.__mro__:
        if "director" in klass.__dict__:
            descriptor = klass.__dict__["director"]
            break
    assert isinstance(descriptor, property)



def test_movies::criticsreview_is_not_abstract():
    assert not inspect.isabstract(movies::CriticsReview)


def test_movies::criticsreview_constructor_exists():
    assert callable(movies::CriticsReview.__init__)


def test_movies::criticsreview_constructor_args():
    sig = inspect.signature(movies::CriticsReview.__init__)
    params = list(sig.parameters.keys())
    assert "reviewedBy" in params, "Missing parameter 'reviewedBy'"
    assert "rating" in params, "Missing parameter 'rating'"

def test_movies::criticsreview_has_reviewedBy():
    assert hasattr(movies::CriticsReview, "reviewedBy")
    descriptor = None
    for klass in movies::CriticsReview.__mro__:
        if "reviewedBy" in klass.__dict__:
            descriptor = klass.__dict__["reviewedBy"]
            break
    assert isinstance(descriptor, property)

def test_movies::criticsreview_has_rating():
    assert hasattr(movies::CriticsReview, "rating")
    descriptor = None
    for klass in movies::CriticsReview.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_movies::copy_is_not_abstract():
    assert not inspect.isabstract(movies::Copy)


def test_movies::copy_constructor_exists():
    assert callable(movies::Copy.__init__)


def test_movies::copy_constructor_args():
    sig = inspect.signature(movies::Copy.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_movies::copy_has_id():
    assert hasattr(movies::Copy, "id")
    descriptor = None
    for klass in movies::Copy.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_genretypes_exists():
    # Check that the Enumeration exists
    assert GenreTypes is not None

def test_genretypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GenreTypes]
    expected_literals = [
        "Documentary",
        "Action",
        "Romance",
        "Family",
        "NewRelease",
        "Horror",
        "Comedy",
        "Classics",
        "Animation",
        "Thriller",
        "SciFi",
        "Drama",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GenreTypes"


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
movies::Place_strategy = st.builds(
    movies::Place,
    id=
        safe_text,
    name=
        safe_text
)
movies::MoviesDB_strategy = st.builds(
    movies::MoviesDB,
    comment=
        safe_text
)
CriticsReview_strategy = st.builds(
    CriticsReview,
)
movies::CustomerReview_strategy = st.builds(
    movies::CustomerReview,
    comment=
        safe_text
)
movies::Movie_strategy = st.builds(
    movies::Movie,
    actors=
        safe_text,
    summary=
        safe_text,
    genre=
        safe_text,
    title=
        safe_text,
    director=
        safe_text
)
movies::CriticsReview_strategy = st.builds(
    movies::CriticsReview,
    reviewedBy=
        safe_text,
    rating=
        safe_text
)
movies::Copy_strategy = st.builds(
    movies::Copy,
    id=
        safe_text
)

@given(instance=movies::Place_strategy)
@settings(max_examples=50)
def test_movies::place_instantiation(instance):
    assert isinstance(instance, movies::Place)

@given(instance=movies::Place_strategy)
def test_movies::place_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=movies::Place_strategy)
def test_movies::place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=movies::Place_strategy)
def test_movies::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=movies::Place_strategy)
def test_movies::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=movies::MoviesDB_strategy)
@settings(max_examples=50)
def test_movies::moviesdb_instantiation(instance):
    assert isinstance(instance, movies::MoviesDB)

@given(instance=movies::MoviesDB_strategy)
def test_movies::moviesdb_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=movies::MoviesDB_strategy)
def test_movies::moviesdb_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=CriticsReview_strategy)
@settings(max_examples=50)
def test_criticsreview_instantiation(instance):
    assert isinstance(instance, CriticsReview)

@given(instance=movies::CustomerReview_strategy)
@settings(max_examples=50)
def test_movies::customerreview_instantiation(instance):
    assert isinstance(instance, movies::CustomerReview)

@given(instance=movies::CustomerReview_strategy)
def test_movies::customerreview_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=movies::CustomerReview_strategy)
def test_movies::customerreview_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=movies::Movie_strategy)
@settings(max_examples=50)
def test_movies::movie_instantiation(instance):
    assert isinstance(instance, movies::Movie)

@given(instance=movies::Movie_strategy)
def test_movies::movie_actors_type(instance):
    assert isinstance(instance.actors, str)


@given(instance=movies::Movie_strategy)
def test_movies::movie_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original

@given(instance=movies::Movie_strategy)
def test_movies::movie_summary_type(instance):
    assert isinstance(instance.summary, str)


@given(instance=movies::Movie_strategy)
def test_movies::movie_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original

@given(instance=movies::Movie_strategy)
def test_movies::movie_genre_type(instance):
    assert isinstance(instance.genre, str)


@given(instance=movies::Movie_strategy)
def test_movies::movie_genre_setter(instance):
    original = instance.genre
    instance.genre = original
    assert instance.genre == original

@given(instance=movies::Movie_strategy)
def test_movies::movie_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=movies::Movie_strategy)
def test_movies::movie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=movies::Movie_strategy)
def test_movies::movie_director_type(instance):
    assert isinstance(instance.director, str)


@given(instance=movies::Movie_strategy)
def test_movies::movie_director_setter(instance):
    original = instance.director
    instance.director = original
    assert instance.director == original

@given(instance=movies::CriticsReview_strategy)
@settings(max_examples=50)
def test_movies::criticsreview_instantiation(instance):
    assert isinstance(instance, movies::CriticsReview)

@given(instance=movies::CriticsReview_strategy)
def test_movies::criticsreview_reviewedBy_type(instance):
    assert isinstance(instance.reviewedBy, str)


@given(instance=movies::CriticsReview_strategy)
def test_movies::criticsreview_reviewedBy_setter(instance):
    original = instance.reviewedBy
    instance.reviewedBy = original
    assert instance.reviewedBy == original

@given(instance=movies::CriticsReview_strategy)
def test_movies::criticsreview_rating_type(instance):
    assert isinstance(instance.rating, str)


@given(instance=movies::CriticsReview_strategy)
def test_movies::criticsreview_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=movies::Copy_strategy)
@settings(max_examples=50)
def test_movies::copy_instantiation(instance):
    assert isinstance(instance, movies::Copy)

@given(instance=movies::Copy_strategy)
def test_movies::copy_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=movies::Copy_strategy)
def test_movies::copy_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
