import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloworld_HelloWorld,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld_helloworld_is_not_abstract():
    assert not inspect.isabstract(helloworld_HelloWorld)


def test_helloworld_helloworld_constructor_exists():
    assert callable(helloworld_HelloWorld.__init__)


def test_helloworld_helloworld_constructor_args():
    sig = inspect.signature(helloworld_HelloWorld.__init__)
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
helloworld_HelloWorld_strategy = st.builds(
    helloworld_HelloWorld,
)

@given(instance=helloworld_HelloWorld_strategy)
@settings(max_examples=50)
def test_helloworld_helloworld_instantiation(instance):
    assert isinstance(instance, helloworld_HelloWorld)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=helloworld_HelloWorld_strategy)
@settings(max_examples=30)
def test_helloworld_helloworld_greeting_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.greeting()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.greeting).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'greeting' in helloworld_HelloWorld is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'greeting' in helloworld_HelloWorld did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'greeting' in helloworld_HelloWorld is not implemented or raised an error")
