import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example_Folder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_folder_is_not_abstract():
    assert not inspect.isabstract(example_Folder)


def test_example_folder_constructor_exists():
    assert callable(example_Folder.__init__)


def test_example_folder_constructor_args():
    sig = inspect.signature(example_Folder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_example_folder_has_name():
    assert hasattr(example_Folder, "name")
    descriptor = None
    for klass in example_Folder.__mro__:
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
example_Folder_strategy = st.builds(
    example_Folder,
    name=
        safe_text
)

@given(instance=example_Folder_strategy)
@settings(max_examples=50)
def test_example_folder_instantiation(instance):
    assert isinstance(instance, example_Folder)



@given(instance=example_Folder_strategy)
def test_example_folder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
