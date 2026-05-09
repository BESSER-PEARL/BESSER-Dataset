import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MediaArtifact,
    mode::AudioBook,
    mode::EBook,
    mode::Music,
    mode::Video,
    mode::MediaArtifact,
    mode::MediaCollection,
    mode::User,
    mode::Device,
    mode::MediaLibrary,
    DeviceType,
    MediaSourceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mediaartifact_is_not_abstract():
    assert not inspect.isabstract(MediaArtifact)


def test_mediaartifact_constructor_exists():
    assert callable(MediaArtifact.__init__)


def test_mediaartifact_constructor_args():
    sig = inspect.signature(MediaArtifact.__init__)
    params = list(sig.parameters.keys())



def test_mode::audiobook_is_not_abstract():
    assert not inspect.isabstract(mode::AudioBook)


def test_mode::audiobook_constructor_exists():
    assert callable(mode::AudioBook.__init__)


def test_mode::audiobook_constructor_args():
    sig = inspect.signature(mode::AudioBook.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_mode::audiobook_has_length():
    assert hasattr(mode::AudioBook, "length")
    descriptor = None
    for klass in mode::AudioBook.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_mode::ebook_is_not_abstract():
    assert not inspect.isabstract(mode::EBook)


def test_mode::ebook_constructor_exists():
    assert callable(mode::EBook.__init__)


def test_mode::ebook_constructor_args():
    sig = inspect.signature(mode::EBook.__init__)
    params = list(sig.parameters.keys())



def test_mode::music_is_not_abstract():
    assert not inspect.isabstract(mode::Music)


def test_mode::music_constructor_exists():
    assert callable(mode::Music.__init__)


def test_mode::music_constructor_args():
    sig = inspect.signature(mode::Music.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_mode::music_has_length():
    assert hasattr(mode::Music, "length")
    descriptor = None
    for klass in mode::Music.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_mode::video_is_not_abstract():
    assert not inspect.isabstract(mode::Video)


def test_mode::video_constructor_exists():
    assert callable(mode::Video.__init__)


def test_mode::video_constructor_args():
    sig = inspect.signature(mode::Video.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_mode::video_has_length():
    assert hasattr(mode::Video, "length")
    descriptor = None
    for klass in mode::Video.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_mode::mediaartifact_is_not_abstract():
    assert not inspect.isabstract(mode::MediaArtifact)


def test_mode::mediaartifact_constructor_exists():
    assert callable(mode::MediaArtifact.__init__)


def test_mode::mediaartifact_constructor_args():
    sig = inspect.signature(mode::MediaArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_mode::mediaartifact_has_source():
    assert hasattr(mode::MediaArtifact, "source")
    descriptor = None
    for klass in mode::MediaArtifact.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_mode::mediaartifact_has_identifier():
    assert hasattr(mode::MediaArtifact, "identifier")
    descriptor = None
    for klass in mode::MediaArtifact.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mode::mediaartifact_has_name():
    assert hasattr(mode::MediaArtifact, "name")
    descriptor = None
    for klass in mode::MediaArtifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mode::mediacollection_is_not_abstract():
    assert not inspect.isabstract(mode::MediaCollection)


def test_mode::mediacollection_constructor_exists():
    assert callable(mode::MediaCollection.__init__)


def test_mode::mediacollection_constructor_args():
    sig = inspect.signature(mode::MediaCollection.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mode::mediacollection_has_name():
    assert hasattr(mode::MediaCollection, "name")
    descriptor = None
    for klass in mode::MediaCollection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mode::user_is_not_abstract():
    assert not inspect.isabstract(mode::User)


def test_mode::user_constructor_exists():
    assert callable(mode::User.__init__)


def test_mode::user_constructor_args():
    sig = inspect.signature(mode::User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mode::user_has_name():
    assert hasattr(mode::User, "name")
    descriptor = None
    for klass in mode::User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mode::device_is_not_abstract():
    assert not inspect.isabstract(mode::Device)


def test_mode::device_constructor_exists():
    assert callable(mode::Device.__init__)


def test_mode::device_constructor_args():
    sig = inspect.signature(mode::Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mode::device_has_name():
    assert hasattr(mode::Device, "name")
    descriptor = None
    for klass in mode::Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mode::device_has_type():
    assert hasattr(mode::Device, "type")
    descriptor = None
    for klass in mode::Device.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mode::medialibrary_is_not_abstract():
    assert not inspect.isabstract(mode::MediaLibrary)


def test_mode::medialibrary_constructor_exists():
    assert callable(mode::MediaLibrary.__init__)


def test_mode::medialibrary_constructor_args():
    sig = inspect.signature(mode::MediaLibrary.__init__)
    params = list(sig.parameters.keys())

def test_devicetype_exists():
    # Check that the Enumeration exists
    assert DeviceType is not None

def test_devicetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeviceType]
    expected_literals = [
        "Computer",
        "Tablet",
        "Smartphone",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeviceType"

def test_mediasourcetype_exists():
    # Check that the Enumeration exists
    assert MediaSourceType is not None

def test_mediasourcetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaSourceType]
    expected_literals = [
        "ExternalArtifact",
        "MediaStore",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaSourceType"


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
MediaArtifact_strategy = st.builds(
    MediaArtifact,
)
mode::AudioBook_strategy = st.builds(
    mode::AudioBook,
    length=
        st.integers()
)
mode::EBook_strategy = st.builds(
    mode::EBook,
)
mode::Music_strategy = st.builds(
    mode::Music,
    length=
        st.integers()
)
mode::Video_strategy = st.builds(
    mode::Video,
    length=
        st.integers()
)
mode::MediaArtifact_strategy = st.builds(
    mode::MediaArtifact,
    source=
        safe_text,
    identifier=
        safe_text,
    name=
        safe_text
)
mode::MediaCollection_strategy = st.builds(
    mode::MediaCollection,
    name=
        safe_text
)
mode::User_strategy = st.builds(
    mode::User,
    name=
        safe_text
)
mode::Device_strategy = st.builds(
    mode::Device,
    name=
        safe_text,
    type=
        safe_text
)
mode::MediaLibrary_strategy = st.builds(
    mode::MediaLibrary,
)

@given(instance=MediaArtifact_strategy)
@settings(max_examples=50)
def test_mediaartifact_instantiation(instance):
    assert isinstance(instance, MediaArtifact)

@given(instance=mode::AudioBook_strategy)
@settings(max_examples=50)
def test_mode::audiobook_instantiation(instance):
    assert isinstance(instance, mode::AudioBook)

@given(instance=mode::AudioBook_strategy)
def test_mode::audiobook_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=mode::AudioBook_strategy)
def test_mode::audiobook_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=mode::EBook_strategy)
@settings(max_examples=50)
def test_mode::ebook_instantiation(instance):
    assert isinstance(instance, mode::EBook)

@given(instance=mode::Music_strategy)
@settings(max_examples=50)
def test_mode::music_instantiation(instance):
    assert isinstance(instance, mode::Music)

@given(instance=mode::Music_strategy)
def test_mode::music_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=mode::Music_strategy)
def test_mode::music_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=mode::Video_strategy)
@settings(max_examples=50)
def test_mode::video_instantiation(instance):
    assert isinstance(instance, mode::Video)

@given(instance=mode::Video_strategy)
def test_mode::video_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=mode::Video_strategy)
def test_mode::video_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=mode::MediaArtifact_strategy)
@settings(max_examples=50)
def test_mode::mediaartifact_instantiation(instance):
    assert isinstance(instance, mode::MediaArtifact)

@given(instance=mode::MediaArtifact_strategy)
def test_mode::mediaartifact_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=mode::MediaArtifact_strategy)
def test_mode::mediaartifact_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=mode::MediaArtifact_strategy)
def test_mode::mediaartifact_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=mode::MediaArtifact_strategy)
def test_mode::mediaartifact_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=mode::MediaArtifact_strategy)
def test_mode::mediaartifact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mode::MediaArtifact_strategy)
def test_mode::mediaartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mode::MediaCollection_strategy)
@settings(max_examples=50)
def test_mode::mediacollection_instantiation(instance):
    assert isinstance(instance, mode::MediaCollection)

@given(instance=mode::MediaCollection_strategy)
def test_mode::mediacollection_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mode::MediaCollection_strategy)
def test_mode::mediacollection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mode::User_strategy)
@settings(max_examples=50)
def test_mode::user_instantiation(instance):
    assert isinstance(instance, mode::User)

@given(instance=mode::User_strategy)
def test_mode::user_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mode::User_strategy)
def test_mode::user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mode::Device_strategy)
@settings(max_examples=50)
def test_mode::device_instantiation(instance):
    assert isinstance(instance, mode::Device)

@given(instance=mode::Device_strategy)
def test_mode::device_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mode::Device_strategy)
def test_mode::device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mode::Device_strategy)
def test_mode::device_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mode::Device_strategy)
def test_mode::device_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mode::MediaLibrary_strategy)
@settings(max_examples=50)
def test_mode::medialibrary_instantiation(instance):
    assert isinstance(instance, mode::MediaLibrary)
