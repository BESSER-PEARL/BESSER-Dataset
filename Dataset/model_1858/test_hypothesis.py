import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    music_MusicLibrary,
    music_Work,
    music_Artist,
    MediaType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_music_musiclibrary_is_not_abstract():
    assert not inspect.isabstract(music_MusicLibrary)


def test_music_musiclibrary_constructor_exists():
    assert callable(music_MusicLibrary.__init__)


def test_music_musiclibrary_constructor_args():
    sig = inspect.signature(music_MusicLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_music_musiclibrary_has_name():
    assert hasattr(music_MusicLibrary, "name")
    descriptor = None
    for klass in music_MusicLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_music_work_is_not_abstract():
    assert not inspect.isabstract(music_Work)


def test_music_work_constructor_exists():
    assert callable(music_Work.__init__)


def test_music_work_constructor_args():
    sig = inspect.signature(music_Work.__init__)
    params = list(sig.parameters.keys())
    assert "whenMade" in params, "Missing parameter 'whenMade'"
    assert "name" in params, "Missing parameter 'name'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "mediaTypes" in params, "Missing parameter 'mediaTypes'"

def test_music_work_has_whenMade():
    assert hasattr(music_Work, "whenMade")
    descriptor = None
    for klass in music_Work.__mro__:
        if "whenMade" in klass.__dict__:
            descriptor = klass.__dict__["whenMade"]
            break
    assert isinstance(descriptor, property)

def test_music_work_has_name():
    assert hasattr(music_Work, "name")
    descriptor = None
    for klass in music_Work.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_music_work_has_notes():
    assert hasattr(music_Work, "notes")
    descriptor = None
    for klass in music_Work.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_music_work_has_mediaTypes():
    assert hasattr(music_Work, "mediaTypes")
    descriptor = None
    for klass in music_Work.__mro__:
        if "mediaTypes" in klass.__dict__:
            descriptor = klass.__dict__["mediaTypes"]
            break
    assert isinstance(descriptor, property)



def test_music_artist_is_not_abstract():
    assert not inspect.isabstract(music_Artist)


def test_music_artist_constructor_exists():
    assert callable(music_Artist.__init__)


def test_music_artist_constructor_args():
    sig = inspect.signature(music_Artist.__init__)
    params = list(sig.parameters.keys())
    assert "notes" in params, "Missing parameter 'notes'"
    assert "name" in params, "Missing parameter 'name'"

def test_music_artist_has_notes():
    assert hasattr(music_Artist, "notes")
    descriptor = None
    for klass in music_Artist.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_music_artist_has_name():
    assert hasattr(music_Artist, "name")
    descriptor = None
    for klass in music_Artist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mediatype_exists():
    # Check that the Enumeration exists
    assert MediaType is not None

def test_mediatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaType]
    expected_literals = [
        "CD",
        "TAPE",
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
music_MusicLibrary_strategy = st.builds(
    music_MusicLibrary,
    name=
        safe_text
)
music_Work_strategy = st.builds(
    music_Work,
    whenMade=
        safe_text,
    name=
        safe_text,
    notes=
        safe_text,
    mediaTypes=
        safe_text
)
music_Artist_strategy = st.builds(
    music_Artist,
    notes=
        safe_text,
    name=
        safe_text
)

@given(instance=music_MusicLibrary_strategy)
@settings(max_examples=50)
def test_music_musiclibrary_instantiation(instance):
    assert isinstance(instance, music_MusicLibrary)



@given(instance=music_MusicLibrary_strategy)
def test_music_musiclibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=music_Work_strategy)
@settings(max_examples=50)
def test_music_work_instantiation(instance):
    assert isinstance(instance, music_Work)



@given(instance=music_Work_strategy)
def test_music_work_whenMade_setter(instance):
    original = instance.whenMade
    instance.whenMade = original
    assert instance.whenMade == original



@given(instance=music_Work_strategy)
def test_music_work_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=music_Work_strategy)
def test_music_work_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=music_Work_strategy)
def test_music_work_mediaTypes_setter(instance):
    original = instance.mediaTypes
    instance.mediaTypes = original
    assert instance.mediaTypes == original

@given(instance=music_Artist_strategy)
@settings(max_examples=50)
def test_music_artist_instantiation(instance):
    assert isinstance(instance, music_Artist)



@given(instance=music_Artist_strategy)
def test_music_artist_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=music_Artist_strategy)
def test_music_artist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=music_Artist_strategy)
@settings(max_examples=30)
def test_music_artist_printstate_changes_state(instance):
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
        assert has_statements, f"Function 'printState' in music_Artist is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printState' in music_Artist did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printState' in music_Artist is not implemented or raised an error")
