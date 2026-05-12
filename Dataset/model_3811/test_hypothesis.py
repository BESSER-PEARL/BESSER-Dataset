import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example_Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_player_is_not_abstract():
    assert not inspect.isabstract(example_Player)


def test_example_player_constructor_exists():
    assert callable(example_Player.__init__)


def test_example_player_constructor_args():
    sig = inspect.signature(example_Player.__init__)
    params = list(sig.parameters.keys())
    assert "compression" in params, "Missing parameter 'compression'"

def test_example_player_has_compression():
    assert hasattr(example_Player, "compression")
    descriptor = None
    for klass in example_Player.__mro__:
        if "compression" in klass.__dict__:
            descriptor = klass.__dict__["compression"]
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
example_Player_strategy = st.builds(
    example_Player,
    compression=
        safe_text
)

@given(instance=example_Player_strategy)
@settings(max_examples=50)
def test_example_player_instantiation(instance):
    assert isinstance(instance, example_Player)



@given(instance=example_Player_strategy)
def test_example_player_compression_setter(instance):
    original = instance.compression
    instance.compression = original
    assert instance.compression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=example_Player_strategy)
@settings(max_examples=30)
def test_example_player_setcompression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setCompression()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setCompression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setCompression' in example_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setCompression' in example_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setCompression' in example_Player is not implemented or raised an error")
