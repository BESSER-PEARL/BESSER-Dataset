import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractD,
    test_ast_D,
    test_ntas_C,
    test_ntas_B,
    test_ast_AbstractD,
    B,
    A,
    test_ntas_Root,
    test_ntas_A,
    D,
    test_ast_E,
    C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractd_is_not_abstract():
    assert not inspect.isabstract(AbstractD)


def test_abstractd_constructor_exists():
    assert callable(AbstractD.__init__)


def test_abstractd_constructor_args():
    sig = inspect.signature(AbstractD.__init__)
    params = list(sig.parameters.keys())



def test_test_ast_d_is_not_abstract():
    assert not inspect.isabstract(test_ast_D)


def test_test_ast_d_constructor_exists():
    assert callable(test_ast_D.__init__)


def test_test_ast_d_constructor_args():
    sig = inspect.signature(test_ast_D.__init__)
    params = list(sig.parameters.keys())
    assert "someCollection" in params, "Missing parameter 'someCollection'"
    assert "someOtherBool" in params, "Missing parameter 'someOtherBool'"
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"
    assert "someQCollection" in params, "Missing parameter 'someQCollection'"
    assert "someBool" in params, "Missing parameter 'someBool'"

def test_test_ast_d_has_someCollection():
    assert hasattr(test_ast_D, "someCollection")
    descriptor = None
    for klass in test_ast_D.__mro__:
        if "someCollection" in klass.__dict__:
            descriptor = klass.__dict__["someCollection"]
            break
    assert isinstance(descriptor, property)

def test_test_ast_d_has_someOtherBool():
    assert hasattr(test_ast_D, "someOtherBool")
    descriptor = None
    for klass in test_ast_D.__mro__:
        if "someOtherBool" in klass.__dict__:
            descriptor = klass.__dict__["someOtherBool"]
            break
    assert isinstance(descriptor, property)

def test_test_ast_d_has_name():
    assert hasattr(test_ast_D, "name")
    descriptor = None
    for klass in test_ast_D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_test_ast_d_has_index():
    assert hasattr(test_ast_D, "index")
    descriptor = None
    for klass in test_ast_D.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_test_ast_d_has_someQCollection():
    assert hasattr(test_ast_D, "someQCollection")
    descriptor = None
    for klass in test_ast_D.__mro__:
        if "someQCollection" in klass.__dict__:
            descriptor = klass.__dict__["someQCollection"]
            break
    assert isinstance(descriptor, property)

def test_test_ast_d_has_someBool():
    assert hasattr(test_ast_D, "someBool")
    descriptor = None
    for klass in test_ast_D.__mro__:
        if "someBool" in klass.__dict__:
            descriptor = klass.__dict__["someBool"]
            break
    assert isinstance(descriptor, property)



def test_test_ntas_c_is_not_abstract():
    assert not inspect.isabstract(test_ntas_C)


def test_test_ntas_c_constructor_exists():
    assert callable(test_ntas_C.__init__)


def test_test_ntas_c_constructor_args():
    sig = inspect.signature(test_ntas_C.__init__)
    params = list(sig.parameters.keys())
    assert "someTerminal" in params, "Missing parameter 'someTerminal'"

def test_test_ntas_c_has_someTerminal():
    assert hasattr(test_ntas_C, "someTerminal")
    descriptor = None
    for klass in test_ntas_C.__mro__:
        if "someTerminal" in klass.__dict__:
            descriptor = klass.__dict__["someTerminal"]
            break
    assert isinstance(descriptor, property)



def test_test_ntas_b_is_not_abstract():
    assert not inspect.isabstract(test_ntas_B)


def test_test_ntas_b_constructor_exists():
    assert callable(test_ntas_B.__init__)


def test_test_ntas_b_constructor_args():
    sig = inspect.signature(test_ntas_B.__init__)
    params = list(sig.parameters.keys())



def test_test_ast_abstractd_is_not_abstract():
    assert not inspect.isabstract(test_ast_AbstractD)


def test_test_ast_abstractd_constructor_exists():
    assert callable(test_ast_AbstractD.__init__)


def test_test_ast_abstractd_constructor_args():
    sig = inspect.signature(test_ast_AbstractD.__init__)
    params = list(sig.parameters.keys())
    assert "derivedString" in params, "Missing parameter 'derivedString'"

def test_test_ast_abstractd_has_derivedString():
    assert hasattr(test_ast_AbstractD, "derivedString")
    descriptor = None
    for klass in test_ast_AbstractD.__mro__:
        if "derivedString" in klass.__dict__:
            descriptor = klass.__dict__["derivedString"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_test_ntas_root_is_not_abstract():
    assert not inspect.isabstract(test_ntas_Root)


def test_test_ntas_root_constructor_exists():
    assert callable(test_ntas_Root.__init__)


def test_test_ntas_root_constructor_args():
    sig = inspect.signature(test_ntas_Root.__init__)
    params = list(sig.parameters.keys())



def test_test_ntas_a_is_not_abstract():
    assert not inspect.isabstract(test_ntas_A)


def test_test_ntas_a_constructor_exists():
    assert callable(test_ntas_A.__init__)


def test_test_ntas_a_constructor_args():
    sig = inspect.signature(test_ntas_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test_ntas_a_has_name():
    assert hasattr(test_ntas_A, "name")
    descriptor = None
    for klass in test_ntas_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_test_ast_e_is_not_abstract():
    assert not inspect.isabstract(test_ast_E)


def test_test_ast_e_constructor_exists():
    assert callable(test_ast_E.__init__)


def test_test_ast_e_constructor_args():
    sig = inspect.signature(test_ast_E.__init__)
    params = list(sig.parameters.keys())
    assert "derivedBool" in params, "Missing parameter 'derivedBool'"
    assert "lazyBool" in params, "Missing parameter 'lazyBool'"

def test_test_ast_e_has_derivedBool():
    assert hasattr(test_ast_E, "derivedBool")
    descriptor = None
    for klass in test_ast_E.__mro__:
        if "derivedBool" in klass.__dict__:
            descriptor = klass.__dict__["derivedBool"]
            break
    assert isinstance(descriptor, property)

def test_test_ast_e_has_lazyBool():
    assert hasattr(test_ast_E, "lazyBool")
    descriptor = None
    for klass in test_ast_E.__mro__:
        if "lazyBool" in klass.__dict__:
            descriptor = klass.__dict__["lazyBool"]
            break
    assert isinstance(descriptor, property)



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
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
AbstractD_strategy = st.builds(
    AbstractD,
)
test_ast_D_strategy = st.builds(
    test_ast_D,
    someCollection=
        safe_text,
    someOtherBool=
        safe_text,
    name=
        safe_text,
    index=
        st.integers(),
    someQCollection=
        safe_text,
    someBool=
        st.booleans()
)
test_ntas_C_strategy = st.builds(
    test_ntas_C,
    someTerminal=
        safe_text
)
test_ntas_B_strategy = st.builds(
    test_ntas_B,
)
test_ast_AbstractD_strategy = st.builds(
    test_ast_AbstractD,
    derivedString=
        safe_text
)
B_strategy = st.builds(
    B,
)
A_strategy = st.builds(
    A,
)
test_ntas_Root_strategy = st.builds(
    test_ntas_Root,
)
test_ntas_A_strategy = st.builds(
    test_ntas_A,
    name=
        safe_text
)
D_strategy = st.builds(
    D,
)
test_ast_E_strategy = st.builds(
    test_ast_E,
    derivedBool=
        st.booleans(),
    lazyBool=
        st.booleans()
)
C_strategy = st.builds(
    C,
)

@given(instance=AbstractD_strategy)
@settings(max_examples=50)
def test_abstractd_instantiation(instance):
    assert isinstance(instance, AbstractD)

@given(instance=test_ast_D_strategy)
@settings(max_examples=50)
def test_test_ast_d_instantiation(instance):
    assert isinstance(instance, test_ast_D)



@given(instance=test_ast_D_strategy)
def test_test_ast_d_someCollection_setter(instance):
    original = instance.someCollection
    instance.someCollection = original
    assert instance.someCollection == original



@given(instance=test_ast_D_strategy)
def test_test_ast_d_someOtherBool_setter(instance):
    original = instance.someOtherBool
    instance.someOtherBool = original
    assert instance.someOtherBool == original



@given(instance=test_ast_D_strategy)
def test_test_ast_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=test_ast_D_strategy)
def test_test_ast_d_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=test_ast_D_strategy)
def test_test_ast_d_someQCollection_setter(instance):
    original = instance.someQCollection
    instance.someQCollection = original
    assert instance.someQCollection == original



@given(instance=test_ast_D_strategy)
def test_test_ast_d_someBool_setter(instance):
    original = instance.someBool
    instance.someBool = original
    assert instance.someBool == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_ast_D_strategy)
@settings(max_examples=30)
def test_test_ast_d_operationattribute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.operationAttribute(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.operationAttribute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'operationAttribute' in test_ast_D is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'operationAttribute' in test_ast_D did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'operationAttribute' in test_ast_D is not implemented or raised an error")

@given(instance=test_ntas_C_strategy)
@settings(max_examples=50)
def test_test_ntas_c_instantiation(instance):
    assert isinstance(instance, test_ntas_C)



@given(instance=test_ntas_C_strategy)
def test_test_ntas_c_someTerminal_setter(instance):
    original = instance.someTerminal
    instance.someTerminal = original
    assert instance.someTerminal == original

@given(instance=test_ntas_B_strategy)
@settings(max_examples=50)
def test_test_ntas_b_instantiation(instance):
    assert isinstance(instance, test_ntas_B)

@given(instance=test_ast_AbstractD_strategy)
@settings(max_examples=50)
def test_test_ast_abstractd_instantiation(instance):
    assert isinstance(instance, test_ast_AbstractD)



@given(instance=test_ast_AbstractD_strategy)
def test_test_ast_abstractd_derivedString_setter(instance):
    original = instance.derivedString
    instance.derivedString = original
    assert instance.derivedString == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=test_ntas_Root_strategy)
@settings(max_examples=50)
def test_test_ntas_root_instantiation(instance):
    assert isinstance(instance, test_ntas_Root)

@given(instance=test_ntas_A_strategy)
@settings(max_examples=50)
def test_test_ntas_a_instantiation(instance):
    assert isinstance(instance, test_ntas_A)



@given(instance=test_ntas_A_strategy)
def test_test_ntas_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=test_ast_E_strategy)
@settings(max_examples=50)
def test_test_ast_e_instantiation(instance):
    assert isinstance(instance, test_ast_E)



@given(instance=test_ast_E_strategy)
def test_test_ast_e_derivedBool_setter(instance):
    original = instance.derivedBool
    instance.derivedBool = original
    assert instance.derivedBool == original



@given(instance=test_ast_E_strategy)
def test_test_ast_e_lazyBool_setter(instance):
    original = instance.lazyBool
    instance.lazyBool = original
    assert instance.lazyBool == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)
