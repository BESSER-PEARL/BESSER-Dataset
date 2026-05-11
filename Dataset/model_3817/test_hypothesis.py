import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example::Folder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::folder_is_not_abstract():
    assert not inspect.isabstract(example::Folder)


def test_example::folder_constructor_exists():
    assert callable(example::Folder.__init__)


def test_example::folder_constructor_args():
    sig = inspect.signature(example::Folder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_example::folder_has_name():
    assert hasattr(example::Folder, "name")
    descriptor = None
    for klass in example::Folder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
example::Folder_strategy = st.builds(
    example::Folder,
    name=
        safe_text
)

@given(instance=example::Folder_strategy)
@settings(max_examples=50)
def test_example::folder_instantiation(instance):
    assert isinstance(instance, example::Folder)

@given(instance=example::Folder_strategy)
def test_example::folder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=example::Folder_strategy)
def test_example::folder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
