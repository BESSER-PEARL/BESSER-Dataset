import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MediaArtifact,
    mode_Music,
    mode_EBook,
    mode_AudioBook,
    mode_Video,
    mode_MediaArtifact,
    mode_MediaCollection,
    mode_User,
    mode_Device,
    mode_MediaLibrary,
    MediaSourceType,
    DeviceType,
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



def test_mode_music_is_not_abstract():
    assert not inspect.isabstract(mode_Music)


def test_mode_music_constructor_exists():
    assert callable(mode_Music.__init__)


def test_mode_music_constructor_args():
    sig = inspect.signature(mode_Music.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_mode_music_has_length():
    assert hasattr(mode_Music, "length")
    descriptor = None
    for klass in mode_Music.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_mode_ebook_is_not_abstract():
    assert not inspect.isabstract(mode_EBook)


def test_mode_ebook_constructor_exists():
    assert callable(mode_EBook.__init__)


def test_mode_ebook_constructor_args():
    sig = inspect.signature(mode_EBook.__init__)
    params = list(sig.parameters.keys())



def test_mode_audiobook_is_not_abstract():
    assert not inspect.isabstract(mode_AudioBook)


def test_mode_audiobook_constructor_exists():
    assert callable(mode_AudioBook.__init__)


def test_mode_audiobook_constructor_args():
    sig = inspect.signature(mode_AudioBook.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_mode_audiobook_has_length():
    assert hasattr(mode_AudioBook, "length")
    descriptor = None
    for klass in mode_AudioBook.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_mode_video_is_not_abstract():
    assert not inspect.isabstract(mode_Video)


def test_mode_video_constructor_exists():
    assert callable(mode_Video.__init__)


def test_mode_video_constructor_args():
    sig = inspect.signature(mode_Video.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_mode_video_has_length():
    assert hasattr(mode_Video, "length")
    descriptor = None
    for klass in mode_Video.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_mode_mediaartifact_is_not_abstract():
    assert not inspect.isabstract(mode_MediaArtifact)


def test_mode_mediaartifact_constructor_exists():
    assert callable(mode_MediaArtifact.__init__)


def test_mode_mediaartifact_constructor_args():
    sig = inspect.signature(mode_MediaArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "source" in params, "Missing parameter 'source'"

def test_mode_mediaartifact_has_name():
    assert hasattr(mode_MediaArtifact, "name")
    descriptor = None
    for klass in mode_MediaArtifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mode_mediaartifact_has_identifier():
    assert hasattr(mode_MediaArtifact, "identifier")
    descriptor = None
    for klass in mode_MediaArtifact.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mode_mediaartifact_has_source():
    assert hasattr(mode_MediaArtifact, "source")
    descriptor = None
    for klass in mode_MediaArtifact.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_mode_mediacollection_is_not_abstract():
    assert not inspect.isabstract(mode_MediaCollection)


def test_mode_mediacollection_constructor_exists():
    assert callable(mode_MediaCollection.__init__)


def test_mode_mediacollection_constructor_args():
    sig = inspect.signature(mode_MediaCollection.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mode_mediacollection_has_name():
    assert hasattr(mode_MediaCollection, "name")
    descriptor = None
    for klass in mode_MediaCollection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mode_user_is_not_abstract():
    assert not inspect.isabstract(mode_User)


def test_mode_user_constructor_exists():
    assert callable(mode_User.__init__)


def test_mode_user_constructor_args():
    sig = inspect.signature(mode_User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mode_user_has_name():
    assert hasattr(mode_User, "name")
    descriptor = None
    for klass in mode_User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mode_device_is_not_abstract():
    assert not inspect.isabstract(mode_Device)


def test_mode_device_constructor_exists():
    assert callable(mode_Device.__init__)


def test_mode_device_constructor_args():
    sig = inspect.signature(mode_Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mode_device_has_name():
    assert hasattr(mode_Device, "name")
    descriptor = None
    for klass in mode_Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mode_device_has_type():
    assert hasattr(mode_Device, "type")
    descriptor = None
    for klass in mode_Device.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mode_medialibrary_is_not_abstract():
    assert not inspect.isabstract(mode_MediaLibrary)


def test_mode_medialibrary_constructor_exists():
    assert callable(mode_MediaLibrary.__init__)


def test_mode_medialibrary_constructor_args():
    sig = inspect.signature(mode_MediaLibrary.__init__)
    params = list(sig.parameters.keys())

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

def test_devicetype_exists():
    # Check that the Enumeration exists
    assert DeviceType is not None

def test_devicetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeviceType]
    expected_literals = [
        "Smartphone",
        "Tablet",
        "Computer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeviceType"


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
mode_Music_strategy = st.builds(
    mode_Music,
    length=
        st.integers()
)
mode_EBook_strategy = st.builds(
    mode_EBook,
)
mode_AudioBook_strategy = st.builds(
    mode_AudioBook,
    length=
        st.integers()
)
mode_Video_strategy = st.builds(
    mode_Video,
    length=
        st.integers()
)
mode_MediaArtifact_strategy = st.builds(
    mode_MediaArtifact,
    name=
        safe_text,
    identifier=
        safe_text,
    source=
        safe_text
)
mode_MediaCollection_strategy = st.builds(
    mode_MediaCollection,
    name=
        safe_text
)
mode_User_strategy = st.builds(
    mode_User,
    name=
        safe_text
)
mode_Device_strategy = st.builds(
    mode_Device,
    name=
        safe_text,
    type=
        safe_text
)
mode_MediaLibrary_strategy = st.builds(
    mode_MediaLibrary,
)

@given(instance=MediaArtifact_strategy)
@settings(max_examples=50)
def test_mediaartifact_instantiation(instance):
    assert isinstance(instance, MediaArtifact)

@given(instance=mode_Music_strategy)
@settings(max_examples=50)
def test_mode_music_instantiation(instance):
    assert isinstance(instance, mode_Music)



@given(instance=mode_Music_strategy)
def test_mode_music_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=mode_EBook_strategy)
@settings(max_examples=50)
def test_mode_ebook_instantiation(instance):
    assert isinstance(instance, mode_EBook)

@given(instance=mode_AudioBook_strategy)
@settings(max_examples=50)
def test_mode_audiobook_instantiation(instance):
    assert isinstance(instance, mode_AudioBook)



@given(instance=mode_AudioBook_strategy)
def test_mode_audiobook_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=mode_Video_strategy)
@settings(max_examples=50)
def test_mode_video_instantiation(instance):
    assert isinstance(instance, mode_Video)



@given(instance=mode_Video_strategy)
def test_mode_video_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=mode_MediaArtifact_strategy)
@settings(max_examples=50)
def test_mode_mediaartifact_instantiation(instance):
    assert isinstance(instance, mode_MediaArtifact)



@given(instance=mode_MediaArtifact_strategy)
def test_mode_mediaartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mode_MediaArtifact_strategy)
def test_mode_mediaartifact_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=mode_MediaArtifact_strategy)
def test_mode_mediaartifact_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=mode_MediaCollection_strategy)
@settings(max_examples=50)
def test_mode_mediacollection_instantiation(instance):
    assert isinstance(instance, mode_MediaCollection)



@given(instance=mode_MediaCollection_strategy)
def test_mode_mediacollection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mode_User_strategy)
@settings(max_examples=50)
def test_mode_user_instantiation(instance):
    assert isinstance(instance, mode_User)



@given(instance=mode_User_strategy)
def test_mode_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mode_Device_strategy)
@settings(max_examples=50)
def test_mode_device_instantiation(instance):
    assert isinstance(instance, mode_Device)



@given(instance=mode_Device_strategy)
def test_mode_device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mode_Device_strategy)
def test_mode_device_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mode_MediaLibrary_strategy)
@settings(max_examples=50)
def test_mode_medialibrary_instantiation(instance):
    assert isinstance(instance, mode_MediaLibrary)
