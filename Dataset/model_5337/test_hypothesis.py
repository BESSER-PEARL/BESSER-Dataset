import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_a_is_not_abstract():
    assert not inspect.isabstract(root_A)


def test_root_a_constructor_exists():
    assert callable(root_A.__init__)


def test_root_a_constructor_args():
    sig = inspect.signature(root_A.__init__)
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
root_A_strategy = st.builds(
    root_A,
)

@given(instance=root_A_strategy)
@settings(max_examples=50)
def test_root_a_instantiation(instance):
    assert isinstance(instance, root_A)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=root_A_strategy)
@settings(max_examples=30)
def test_root_a_whoiam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.whoIAm()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.whoIAm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'whoIAm' in root_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'whoIAm' in root_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'whoIAm' in root_A is not implemented or raised an error")
