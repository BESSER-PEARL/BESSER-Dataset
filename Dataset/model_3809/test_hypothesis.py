import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example::MP3,
    example::Audio,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::mp3_is_not_abstract():
    assert not inspect.isabstract(example::MP3)


def test_example::mp3_constructor_exists():
    assert callable(example::MP3.__init__)


def test_example::mp3_constructor_args():
    sig = inspect.signature(example::MP3.__init__)
    params = list(sig.parameters.keys())



def test_example::audio_is_not_abstract():
    assert not inspect.isabstract(example::Audio)


def test_example::audio_constructor_exists():
    assert callable(example::Audio.__init__)


def test_example::audio_constructor_args():
    sig = inspect.signature(example::Audio.__init__)
    params = list(sig.parameters.keys())


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
example::MP3_strategy = st.builds(
    example::MP3,
)
example::Audio_strategy = st.builds(
    example::Audio,
)

@given(instance=example::MP3_strategy)
@settings(max_examples=50)
def test_example::mp3_instantiation(instance):
    assert isinstance(instance, example::MP3)

@given(instance=example::Audio_strategy)
@settings(max_examples=50)
def test_example::audio_instantiation(instance):
    assert isinstance(instance, example::Audio)
