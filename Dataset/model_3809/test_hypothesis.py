import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example_MP3,
    example_Audio,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_mp3_is_not_abstract():
    assert not inspect.isabstract(example_MP3)


def test_example_mp3_constructor_exists():
    assert callable(example_MP3.__init__)


def test_example_mp3_constructor_args():
    sig = inspect.signature(example_MP3.__init__)
    params = list(sig.parameters.keys())



def test_example_audio_is_not_abstract():
    assert not inspect.isabstract(example_Audio)


def test_example_audio_constructor_exists():
    assert callable(example_Audio.__init__)


def test_example_audio_constructor_args():
    sig = inspect.signature(example_Audio.__init__)
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
example_MP3_strategy = st.builds(
    example_MP3,
)
example_Audio_strategy = st.builds(
    example_Audio,
)

@given(instance=example_MP3_strategy)
@settings(max_examples=50)
def test_example_mp3_instantiation(instance):
    assert isinstance(instance, example_MP3)

@given(instance=example_Audio_strategy)
@settings(max_examples=50)
def test_example_audio_instantiation(instance):
    assert isinstance(instance, example_Audio)
