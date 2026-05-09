import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DurationArtifact,
    MediaLibrary::MusicTrack,
    MediaLibrary::Video,
    MediaLibrary::AudioBook,
    Artifact,
    MediaLibrary::Ebook,
    MediaLibrary::Image,
    MediaLibrary::DurationArtifact,
    MediaSource,
    MediaLibrary::Store,
    MediaLibrary::ExternalSource,
    NamedElement,
    MediaLibrary::MediaCollection,
    MediaLibrary::Artifact,
    MediaLibrary::MediaSource,
    MediaLibrary::Device,
    MediaLibrary::Library,
    MediaLibrary::Ecosystem,
    Device,
    MediaLibrary::EReader,
    MediaLibrary::Smartphone,
    MediaLibrary::Computer,
    MediaLibrary::Tablet,
    MediaLibrary::NamedElement,
    SourceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_durationartifact_is_not_abstract():
    assert not inspect.isabstract(DurationArtifact)


def test_durationartifact_constructor_exists():
    assert callable(DurationArtifact.__init__)


def test_durationartifact_constructor_args():
    sig = inspect.signature(DurationArtifact.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::musictrack_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::MusicTrack)


def test_medialibrary::musictrack_constructor_exists():
    assert callable(MediaLibrary::MusicTrack.__init__)


def test_medialibrary::musictrack_constructor_args():
    sig = inspect.signature(MediaLibrary::MusicTrack.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::video_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Video)


def test_medialibrary::video_constructor_exists():
    assert callable(MediaLibrary::Video.__init__)


def test_medialibrary::video_constructor_args():
    sig = inspect.signature(MediaLibrary::Video.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::audiobook_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::AudioBook)


def test_medialibrary::audiobook_constructor_exists():
    assert callable(MediaLibrary::AudioBook.__init__)


def test_medialibrary::audiobook_constructor_args():
    sig = inspect.signature(MediaLibrary::AudioBook.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::ebook_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Ebook)


def test_medialibrary::ebook_constructor_exists():
    assert callable(MediaLibrary::Ebook.__init__)


def test_medialibrary::ebook_constructor_args():
    sig = inspect.signature(MediaLibrary::Ebook.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::image_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Image)


def test_medialibrary::image_constructor_exists():
    assert callable(MediaLibrary::Image.__init__)


def test_medialibrary::image_constructor_args():
    sig = inspect.signature(MediaLibrary::Image.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::durationartifact_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::DurationArtifact)


def test_medialibrary::durationartifact_constructor_exists():
    assert callable(MediaLibrary::DurationArtifact.__init__)


def test_medialibrary::durationartifact_constructor_args():
    sig = inspect.signature(MediaLibrary::DurationArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_medialibrary::durationartifact_has_duration():
    assert hasattr(MediaLibrary::DurationArtifact, "duration")
    descriptor = None
    for klass in MediaLibrary::DurationArtifact.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_mediasource_is_not_abstract():
    assert not inspect.isabstract(MediaSource)


def test_mediasource_constructor_exists():
    assert callable(MediaSource.__init__)


def test_mediasource_constructor_args():
    sig = inspect.signature(MediaSource.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::store_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Store)


def test_medialibrary::store_constructor_exists():
    assert callable(MediaLibrary::Store.__init__)


def test_medialibrary::store_constructor_args():
    sig = inspect.signature(MediaLibrary::Store.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::externalsource_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::ExternalSource)


def test_medialibrary::externalsource_constructor_exists():
    assert callable(MediaLibrary::ExternalSource.__init__)


def test_medialibrary::externalsource_constructor_args():
    sig = inspect.signature(MediaLibrary::ExternalSource.__init__)
    params = list(sig.parameters.keys())
    assert "sourceType" in params, "Missing parameter 'sourceType'"

def test_medialibrary::externalsource_has_sourceType():
    assert hasattr(MediaLibrary::ExternalSource, "sourceType")
    descriptor = None
    for klass in MediaLibrary::ExternalSource.__mro__:
        if "sourceType" in klass.__dict__:
            descriptor = klass.__dict__["sourceType"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::mediacollection_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::MediaCollection)


def test_medialibrary::mediacollection_constructor_exists():
    assert callable(MediaLibrary::MediaCollection.__init__)


def test_medialibrary::mediacollection_constructor_args():
    sig = inspect.signature(MediaLibrary::MediaCollection.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::artifact_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Artifact)


def test_medialibrary::artifact_constructor_exists():
    assert callable(MediaLibrary::Artifact.__init__)


def test_medialibrary::artifact_constructor_args():
    sig = inspect.signature(MediaLibrary::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::mediasource_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::MediaSource)


def test_medialibrary::mediasource_constructor_exists():
    assert callable(MediaLibrary::MediaSource.__init__)


def test_medialibrary::mediasource_constructor_args():
    sig = inspect.signature(MediaLibrary::MediaSource.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::device_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Device)


def test_medialibrary::device_constructor_exists():
    assert callable(MediaLibrary::Device.__init__)


def test_medialibrary::device_constructor_args():
    sig = inspect.signature(MediaLibrary::Device.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::library_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Library)


def test_medialibrary::library_constructor_exists():
    assert callable(MediaLibrary::Library.__init__)


def test_medialibrary::library_constructor_args():
    sig = inspect.signature(MediaLibrary::Library.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::ecosystem_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Ecosystem)


def test_medialibrary::ecosystem_constructor_exists():
    assert callable(MediaLibrary::Ecosystem.__init__)


def test_medialibrary::ecosystem_constructor_args():
    sig = inspect.signature(MediaLibrary::Ecosystem.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::ereader_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::EReader)


def test_medialibrary::ereader_constructor_exists():
    assert callable(MediaLibrary::EReader.__init__)


def test_medialibrary::ereader_constructor_args():
    sig = inspect.signature(MediaLibrary::EReader.__init__)
    params = list(sig.parameters.keys())
    assert "videoEnabled" in params, "Missing parameter 'videoEnabled'"
    assert "audioEnabled" in params, "Missing parameter 'audioEnabled'"

def test_medialibrary::ereader_has_videoEnabled():
    assert hasattr(MediaLibrary::EReader, "videoEnabled")
    descriptor = None
    for klass in MediaLibrary::EReader.__mro__:
        if "videoEnabled" in klass.__dict__:
            descriptor = klass.__dict__["videoEnabled"]
            break
    assert isinstance(descriptor, property)

def test_medialibrary::ereader_has_audioEnabled():
    assert hasattr(MediaLibrary::EReader, "audioEnabled")
    descriptor = None
    for klass in MediaLibrary::EReader.__mro__:
        if "audioEnabled" in klass.__dict__:
            descriptor = klass.__dict__["audioEnabled"]
            break
    assert isinstance(descriptor, property)



def test_medialibrary::smartphone_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Smartphone)


def test_medialibrary::smartphone_constructor_exists():
    assert callable(MediaLibrary::Smartphone.__init__)


def test_medialibrary::smartphone_constructor_args():
    sig = inspect.signature(MediaLibrary::Smartphone.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::computer_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Computer)


def test_medialibrary::computer_constructor_exists():
    assert callable(MediaLibrary::Computer.__init__)


def test_medialibrary::computer_constructor_args():
    sig = inspect.signature(MediaLibrary::Computer.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::tablet_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::Tablet)


def test_medialibrary::tablet_constructor_exists():
    assert callable(MediaLibrary::Tablet.__init__)


def test_medialibrary::tablet_constructor_args():
    sig = inspect.signature(MediaLibrary::Tablet.__init__)
    params = list(sig.parameters.keys())



def test_medialibrary::namedelement_is_not_abstract():
    assert not inspect.isabstract(MediaLibrary::NamedElement)


def test_medialibrary::namedelement_constructor_exists():
    assert callable(MediaLibrary::NamedElement.__init__)


def test_medialibrary::namedelement_constructor_args():
    sig = inspect.signature(MediaLibrary::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_medialibrary::namedelement_has_name():
    assert hasattr(MediaLibrary::NamedElement, "name")
    descriptor = None
    for klass in MediaLibrary::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcetype_exists():
    # Check that the Enumeration exists
    assert SourceType is not None

def test_sourcetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SourceType]
    expected_literals = [
        "VHS",
        "OTHER",
        "CD",
        "CASSETTE",
        "DVD",
        "HDD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SourceType"


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
DurationArtifact_strategy = st.builds(
    DurationArtifact,
)
MediaLibrary::MusicTrack_strategy = st.builds(
    MediaLibrary::MusicTrack,
)
MediaLibrary::Video_strategy = st.builds(
    MediaLibrary::Video,
)
MediaLibrary::AudioBook_strategy = st.builds(
    MediaLibrary::AudioBook,
)
Artifact_strategy = st.builds(
    Artifact,
)
MediaLibrary::Ebook_strategy = st.builds(
    MediaLibrary::Ebook,
)
MediaLibrary::Image_strategy = st.builds(
    MediaLibrary::Image,
)
MediaLibrary::DurationArtifact_strategy = st.builds(
    MediaLibrary::DurationArtifact,
    duration=
        st.integers()
)
MediaSource_strategy = st.builds(
    MediaSource,
)
MediaLibrary::Store_strategy = st.builds(
    MediaLibrary::Store,
)
MediaLibrary::ExternalSource_strategy = st.builds(
    MediaLibrary::ExternalSource,
    sourceType=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MediaLibrary::MediaCollection_strategy = st.builds(
    MediaLibrary::MediaCollection,
)
MediaLibrary::Artifact_strategy = st.builds(
    MediaLibrary::Artifact,
)
MediaLibrary::MediaSource_strategy = st.builds(
    MediaLibrary::MediaSource,
)
MediaLibrary::Device_strategy = st.builds(
    MediaLibrary::Device,
)
MediaLibrary::Library_strategy = st.builds(
    MediaLibrary::Library,
)
MediaLibrary::Ecosystem_strategy = st.builds(
    MediaLibrary::Ecosystem,
)
Device_strategy = st.builds(
    Device,
)
MediaLibrary::EReader_strategy = st.builds(
    MediaLibrary::EReader,
    videoEnabled=
        safe_text,
    audioEnabled=
        safe_text
)
MediaLibrary::Smartphone_strategy = st.builds(
    MediaLibrary::Smartphone,
)
MediaLibrary::Computer_strategy = st.builds(
    MediaLibrary::Computer,
)
MediaLibrary::Tablet_strategy = st.builds(
    MediaLibrary::Tablet,
)
MediaLibrary::NamedElement_strategy = st.builds(
    MediaLibrary::NamedElement,
    name=
        safe_text
)

@given(instance=DurationArtifact_strategy)
@settings(max_examples=50)
def test_durationartifact_instantiation(instance):
    assert isinstance(instance, DurationArtifact)

@given(instance=MediaLibrary::MusicTrack_strategy)
@settings(max_examples=50)
def test_medialibrary::musictrack_instantiation(instance):
    assert isinstance(instance, MediaLibrary::MusicTrack)

@given(instance=MediaLibrary::Video_strategy)
@settings(max_examples=50)
def test_medialibrary::video_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Video)

@given(instance=MediaLibrary::AudioBook_strategy)
@settings(max_examples=50)
def test_medialibrary::audiobook_instantiation(instance):
    assert isinstance(instance, MediaLibrary::AudioBook)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=MediaLibrary::Ebook_strategy)
@settings(max_examples=50)
def test_medialibrary::ebook_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Ebook)

@given(instance=MediaLibrary::Image_strategy)
@settings(max_examples=50)
def test_medialibrary::image_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Image)

@given(instance=MediaLibrary::DurationArtifact_strategy)
@settings(max_examples=50)
def test_medialibrary::durationartifact_instantiation(instance):
    assert isinstance(instance, MediaLibrary::DurationArtifact)

@given(instance=MediaLibrary::DurationArtifact_strategy)
def test_medialibrary::durationartifact_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=MediaLibrary::DurationArtifact_strategy)
def test_medialibrary::durationartifact_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=MediaSource_strategy)
@settings(max_examples=50)
def test_mediasource_instantiation(instance):
    assert isinstance(instance, MediaSource)

@given(instance=MediaLibrary::Store_strategy)
@settings(max_examples=50)
def test_medialibrary::store_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Store)

@given(instance=MediaLibrary::ExternalSource_strategy)
@settings(max_examples=50)
def test_medialibrary::externalsource_instantiation(instance):
    assert isinstance(instance, MediaLibrary::ExternalSource)

@given(instance=MediaLibrary::ExternalSource_strategy)
def test_medialibrary::externalsource_sourceType_type(instance):
    assert isinstance(instance.sourceType, str)


@given(instance=MediaLibrary::ExternalSource_strategy)
def test_medialibrary::externalsource_sourceType_setter(instance):
    original = instance.sourceType
    instance.sourceType = original
    assert instance.sourceType == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MediaLibrary::MediaCollection_strategy)
@settings(max_examples=50)
def test_medialibrary::mediacollection_instantiation(instance):
    assert isinstance(instance, MediaLibrary::MediaCollection)

@given(instance=MediaLibrary::Artifact_strategy)
@settings(max_examples=50)
def test_medialibrary::artifact_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Artifact)

@given(instance=MediaLibrary::MediaSource_strategy)
@settings(max_examples=50)
def test_medialibrary::mediasource_instantiation(instance):
    assert isinstance(instance, MediaLibrary::MediaSource)

@given(instance=MediaLibrary::Device_strategy)
@settings(max_examples=50)
def test_medialibrary::device_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Device)

@given(instance=MediaLibrary::Library_strategy)
@settings(max_examples=50)
def test_medialibrary::library_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Library)

@given(instance=MediaLibrary::Ecosystem_strategy)
@settings(max_examples=50)
def test_medialibrary::ecosystem_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Ecosystem)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=MediaLibrary::EReader_strategy)
@settings(max_examples=50)
def test_medialibrary::ereader_instantiation(instance):
    assert isinstance(instance, MediaLibrary::EReader)

@given(instance=MediaLibrary::EReader_strategy)
def test_medialibrary::ereader_videoEnabled_type(instance):
    assert isinstance(instance.videoEnabled, str)


@given(instance=MediaLibrary::EReader_strategy)
def test_medialibrary::ereader_videoEnabled_setter(instance):
    original = instance.videoEnabled
    instance.videoEnabled = original
    assert instance.videoEnabled == original

@given(instance=MediaLibrary::EReader_strategy)
def test_medialibrary::ereader_audioEnabled_type(instance):
    assert isinstance(instance.audioEnabled, str)


@given(instance=MediaLibrary::EReader_strategy)
def test_medialibrary::ereader_audioEnabled_setter(instance):
    original = instance.audioEnabled
    instance.audioEnabled = original
    assert instance.audioEnabled == original

@given(instance=MediaLibrary::Smartphone_strategy)
@settings(max_examples=50)
def test_medialibrary::smartphone_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Smartphone)

@given(instance=MediaLibrary::Computer_strategy)
@settings(max_examples=50)
def test_medialibrary::computer_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Computer)

@given(instance=MediaLibrary::Tablet_strategy)
@settings(max_examples=50)
def test_medialibrary::tablet_instantiation(instance):
    assert isinstance(instance, MediaLibrary::Tablet)

@given(instance=MediaLibrary::NamedElement_strategy)
@settings(max_examples=50)
def test_medialibrary::namedelement_instantiation(instance):
    assert isinstance(instance, MediaLibrary::NamedElement)

@given(instance=MediaLibrary::NamedElement_strategy)
def test_medialibrary::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MediaLibrary::NamedElement_strategy)
def test_medialibrary::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
