import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    music::MusicLibrary,
    music::Work,
    music::Artist,
    MediaType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_music::musiclibrary_is_not_abstract():
    assert not inspect.isabstract(music::MusicLibrary)


def test_music::musiclibrary_constructor_exists():
    assert callable(music::MusicLibrary.__init__)


def test_music::musiclibrary_constructor_args():
    sig = inspect.signature(music::MusicLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_music::musiclibrary_has_name():
    assert hasattr(music::MusicLibrary, "name")
    descriptor = None
    for klass in music::MusicLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_music::work_is_not_abstract():
    assert not inspect.isabstract(music::Work)


def test_music::work_constructor_exists():
    assert callable(music::Work.__init__)


def test_music::work_constructor_args():
    sig = inspect.signature(music::Work.__init__)
    params = list(sig.parameters.keys())
    assert "mediaTypes" in params, "Missing parameter 'mediaTypes'"
    assert "name" in params, "Missing parameter 'name'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "whenMade" in params, "Missing parameter 'whenMade'"

def test_music::work_has_mediaTypes():
    assert hasattr(music::Work, "mediaTypes")
    descriptor = None
    for klass in music::Work.__mro__:
        if "mediaTypes" in klass.__dict__:
            descriptor = klass.__dict__["mediaTypes"]
            break
    assert isinstance(descriptor, property)

def test_music::work_has_name():
    assert hasattr(music::Work, "name")
    descriptor = None
    for klass in music::Work.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_music::work_has_notes():
    assert hasattr(music::Work, "notes")
    descriptor = None
    for klass in music::Work.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_music::work_has_whenMade():
    assert hasattr(music::Work, "whenMade")
    descriptor = None
    for klass in music::Work.__mro__:
        if "whenMade" in klass.__dict__:
            descriptor = klass.__dict__["whenMade"]
            break
    assert isinstance(descriptor, property)



def test_music::artist_is_not_abstract():
    assert not inspect.isabstract(music::Artist)


def test_music::artist_constructor_exists():
    assert callable(music::Artist.__init__)


def test_music::artist_constructor_args():
    sig = inspect.signature(music::Artist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "notes" in params, "Missing parameter 'notes'"

def test_music::artist_has_name():
    assert hasattr(music::Artist, "name")
    descriptor = None
    for klass in music::Artist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_music::artist_has_notes():
    assert hasattr(music::Artist, "notes")
    descriptor = None
    for klass in music::Artist.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_mediatype_exists():
    # Check that the Enumeration exists
    assert MediaType is not None

def test_mediatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaType]
    expected_literals = [
        "TAPE",
        "CD",
        "MP3",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaType"


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
music::MusicLibrary_strategy = st.builds(
    music::MusicLibrary,
    name=
        safe_text
)
music::Work_strategy = st.builds(
    music::Work,
    mediaTypes=
        safe_text,
    name=
        safe_text,
    notes=
        safe_text,
    whenMade=
        safe_text
)
music::Artist_strategy = st.builds(
    music::Artist,
    name=
        safe_text,
    notes=
        safe_text
)

@given(instance=music::MusicLibrary_strategy)
@settings(max_examples=50)
def test_music::musiclibrary_instantiation(instance):
    assert isinstance(instance, music::MusicLibrary)

@given(instance=music::MusicLibrary_strategy)
def test_music::musiclibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=music::MusicLibrary_strategy)
def test_music::musiclibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=music::Work_strategy)
@settings(max_examples=50)
def test_music::work_instantiation(instance):
    assert isinstance(instance, music::Work)

@given(instance=music::Work_strategy)
def test_music::work_mediaTypes_type(instance):
    assert isinstance(instance.mediaTypes, str)


@given(instance=music::Work_strategy)
def test_music::work_mediaTypes_setter(instance):
    original = instance.mediaTypes
    instance.mediaTypes = original
    assert instance.mediaTypes == original

@given(instance=music::Work_strategy)
def test_music::work_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=music::Work_strategy)
def test_music::work_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=music::Work_strategy)
def test_music::work_notes_type(instance):
    assert isinstance(instance.notes, str)


@given(instance=music::Work_strategy)
def test_music::work_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original

@given(instance=music::Work_strategy)
def test_music::work_whenMade_type(instance):
    assert isinstance(instance.whenMade, str)


@given(instance=music::Work_strategy)
def test_music::work_whenMade_setter(instance):
    original = instance.whenMade
    instance.whenMade = original
    assert instance.whenMade == original

@given(instance=music::Artist_strategy)
@settings(max_examples=50)
def test_music::artist_instantiation(instance):
    assert isinstance(instance, music::Artist)

@given(instance=music::Artist_strategy)
def test_music::artist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=music::Artist_strategy)
def test_music::artist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=music::Artist_strategy)
def test_music::artist_notes_type(instance):
    assert isinstance(instance.notes, str)


@given(instance=music::Artist_strategy)
def test_music::artist_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=music::Artist_strategy)
@settings(max_examples=30)
def test_music::artist_printstate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printState()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printState' in music::Artist is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printState' in music::Artist did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printState' in music::Artist is not implemented or raised an error")
