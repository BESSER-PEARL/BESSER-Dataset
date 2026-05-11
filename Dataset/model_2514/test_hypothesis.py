import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractD,
    test::ast::D,
    test::ntas::C,
    test::ntas::B,
    test::ast::AbstractD,
    B,
    A,
    test::ntas::Root,
    test::ntas::A,
    D,
    test::ast::E,
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



def test_test::ast::d_is_not_abstract():
    assert not inspect.isabstract(test::ast::D)


def test_test::ast::d_constructor_exists():
    assert callable(test::ast::D.__init__)


def test_test::ast::d_constructor_args():
    sig = inspect.signature(test::ast::D.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "someCollection" in params, "Missing parameter 'someCollection'"
    assert "name" in params, "Missing parameter 'name'"
    assert "someOtherBool" in params, "Missing parameter 'someOtherBool'"
    assert "someQCollection" in params, "Missing parameter 'someQCollection'"
    assert "someBool" in params, "Missing parameter 'someBool'"

def test_test::ast::d_has_index():
    assert hasattr(test::ast::D, "index")
    descriptor = None
    for klass in test::ast::D.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_test::ast::d_has_someCollection():
    assert hasattr(test::ast::D, "someCollection")
    descriptor = None
    for klass in test::ast::D.__mro__:
        if "someCollection" in klass.__dict__:
            descriptor = klass.__dict__["someCollection"]
            break
    assert isinstance(descriptor, property)

def test_test::ast::d_has_name():
    assert hasattr(test::ast::D, "name")
    descriptor = None
    for klass in test::ast::D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_test::ast::d_has_someOtherBool():
    assert hasattr(test::ast::D, "someOtherBool")
    descriptor = None
    for klass in test::ast::D.__mro__:
        if "someOtherBool" in klass.__dict__:
            descriptor = klass.__dict__["someOtherBool"]
            break
    assert isinstance(descriptor, property)

def test_test::ast::d_has_someQCollection():
    assert hasattr(test::ast::D, "someQCollection")
    descriptor = None
    for klass in test::ast::D.__mro__:
        if "someQCollection" in klass.__dict__:
            descriptor = klass.__dict__["someQCollection"]
            break
    assert isinstance(descriptor, property)

def test_test::ast::d_has_someBool():
    assert hasattr(test::ast::D, "someBool")
    descriptor = None
    for klass in test::ast::D.__mro__:
        if "someBool" in klass.__dict__:
            descriptor = klass.__dict__["someBool"]
            break
    assert isinstance(descriptor, property)



def test_test::ntas::c_is_not_abstract():
    assert not inspect.isabstract(test::ntas::C)


def test_test::ntas::c_constructor_exists():
    assert callable(test::ntas::C.__init__)


def test_test::ntas::c_constructor_args():
    sig = inspect.signature(test::ntas::C.__init__)
    params = list(sig.parameters.keys())
    assert "someTerminal" in params, "Missing parameter 'someTerminal'"

def test_test::ntas::c_has_someTerminal():
    assert hasattr(test::ntas::C, "someTerminal")
    descriptor = None
    for klass in test::ntas::C.__mro__:
        if "someTerminal" in klass.__dict__:
            descriptor = klass.__dict__["someTerminal"]
            break
    assert isinstance(descriptor, property)



def test_test::ntas::b_is_not_abstract():
    assert not inspect.isabstract(test::ntas::B)


def test_test::ntas::b_constructor_exists():
    assert callable(test::ntas::B.__init__)


def test_test::ntas::b_constructor_args():
    sig = inspect.signature(test::ntas::B.__init__)
    params = list(sig.parameters.keys())



def test_test::ast::abstractd_is_not_abstract():
    assert not inspect.isabstract(test::ast::AbstractD)


def test_test::ast::abstractd_constructor_exists():
    assert callable(test::ast::AbstractD.__init__)


def test_test::ast::abstractd_constructor_args():
    sig = inspect.signature(test::ast::AbstractD.__init__)
    params = list(sig.parameters.keys())
    assert "derivedString" in params, "Missing parameter 'derivedString'"

def test_test::ast::abstractd_has_derivedString():
    assert hasattr(test::ast::AbstractD, "derivedString")
    descriptor = None
    for klass in test::ast::AbstractD.__mro__:
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



def test_test::ntas::root_is_not_abstract():
    assert not inspect.isabstract(test::ntas::Root)


def test_test::ntas::root_constructor_exists():
    assert callable(test::ntas::Root.__init__)


def test_test::ntas::root_constructor_args():
    sig = inspect.signature(test::ntas::Root.__init__)
    params = list(sig.parameters.keys())



def test_test::ntas::a_is_not_abstract():
    assert not inspect.isabstract(test::ntas::A)


def test_test::ntas::a_constructor_exists():
    assert callable(test::ntas::A.__init__)


def test_test::ntas::a_constructor_args():
    sig = inspect.signature(test::ntas::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test::ntas::a_has_name():
    assert hasattr(test::ntas::A, "name")
    descriptor = None
    for klass in test::ntas::A.__mro__:
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



def test_test::ast::e_is_not_abstract():
    assert not inspect.isabstract(test::ast::E)


def test_test::ast::e_constructor_exists():
    assert callable(test::ast::E.__init__)


def test_test::ast::e_constructor_args():
    sig = inspect.signature(test::ast::E.__init__)
    params = list(sig.parameters.keys())
    assert "derivedBool" in params, "Missing parameter 'derivedBool'"
    assert "lazyBool" in params, "Missing parameter 'lazyBool'"

def test_test::ast::e_has_derivedBool():
    assert hasattr(test::ast::E, "derivedBool")
    descriptor = None
    for klass in test::ast::E.__mro__:
        if "derivedBool" in klass.__dict__:
            descriptor = klass.__dict__["derivedBool"]
            break
    assert isinstance(descriptor, property)

def test_test::ast::e_has_lazyBool():
    assert hasattr(test::ast::E, "lazyBool")
    descriptor = None
    for klass in test::ast::E.__mro__:
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
test::ast::D_strategy = st.builds(
    test::ast::D,
    index=
        st.integers(),
    someCollection=
        safe_text,
    name=
        safe_text,
    someOtherBool=
        safe_text,
    someQCollection=
        safe_text,
    someBool=
        st.booleans()
)
test::ntas::C_strategy = st.builds(
    test::ntas::C,
    someTerminal=
        safe_text
)
test::ntas::B_strategy = st.builds(
    test::ntas::B,
)
test::ast::AbstractD_strategy = st.builds(
    test::ast::AbstractD,
    derivedString=
        safe_text
)
B_strategy = st.builds(
    B,
)
A_strategy = st.builds(
    A,
)
test::ntas::Root_strategy = st.builds(
    test::ntas::Root,
)
test::ntas::A_strategy = st.builds(
    test::ntas::A,
    name=
        safe_text
)
D_strategy = st.builds(
    D,
)
test::ast::E_strategy = st.builds(
    test::ast::E,
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

@given(instance=test::ast::D_strategy)
@settings(max_examples=50)
def test_test::ast::d_instantiation(instance):
    assert isinstance(instance, test::ast::D)

@given(instance=test::ast::D_strategy)
def test_test::ast::d_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=test::ast::D_strategy)
def test_test::ast::d_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=test::ast::D_strategy)
def test_test::ast::d_someCollection_type(instance):
    assert isinstance(instance.someCollection, str)


@given(instance=test::ast::D_strategy)
def test_test::ast::d_someCollection_setter(instance):
    original = instance.someCollection
    instance.someCollection = original
    assert instance.someCollection == original

@given(instance=test::ast::D_strategy)
def test_test::ast::d_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::ast::D_strategy)
def test_test::ast::d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=test::ast::D_strategy)
def test_test::ast::d_someOtherBool_type(instance):
    assert isinstance(instance.someOtherBool, str)


@given(instance=test::ast::D_strategy)
def test_test::ast::d_someOtherBool_setter(instance):
    original = instance.someOtherBool
    instance.someOtherBool = original
    assert instance.someOtherBool == original

@given(instance=test::ast::D_strategy)
def test_test::ast::d_someQCollection_type(instance):
    assert isinstance(instance.someQCollection, str)


@given(instance=test::ast::D_strategy)
def test_test::ast::d_someQCollection_setter(instance):
    original = instance.someQCollection
    instance.someQCollection = original
    assert instance.someQCollection == original

@given(instance=test::ast::D_strategy)
def test_test::ast::d_someBool_type(instance):
    assert isinstance(instance.someBool, bool)


@given(instance=test::ast::D_strategy)
def test_test::ast::d_someBool_setter(instance):
    original = instance.someBool
    instance.someBool = original
    assert instance.someBool == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test::ast::D_strategy)
@settings(max_examples=30)
def test_test::ast::d_operationattribute_changes_state(instance):
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
        assert has_statements, f"Function 'operationAttribute' in test::ast::D is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'operationAttribute' in test::ast::D did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'operationAttribute' in test::ast::D is not implemented or raised an error")

@given(instance=test::ntas::C_strategy)
@settings(max_examples=50)
def test_test::ntas::c_instantiation(instance):
    assert isinstance(instance, test::ntas::C)

@given(instance=test::ntas::C_strategy)
def test_test::ntas::c_someTerminal_type(instance):
    assert isinstance(instance.someTerminal, str)


@given(instance=test::ntas::C_strategy)
def test_test::ntas::c_someTerminal_setter(instance):
    original = instance.someTerminal
    instance.someTerminal = original
    assert instance.someTerminal == original

@given(instance=test::ntas::B_strategy)
@settings(max_examples=50)
def test_test::ntas::b_instantiation(instance):
    assert isinstance(instance, test::ntas::B)

@given(instance=test::ast::AbstractD_strategy)
@settings(max_examples=50)
def test_test::ast::abstractd_instantiation(instance):
    assert isinstance(instance, test::ast::AbstractD)

@given(instance=test::ast::AbstractD_strategy)
def test_test::ast::abstractd_derivedString_type(instance):
    assert isinstance(instance.derivedString, str)


@given(instance=test::ast::AbstractD_strategy)
def test_test::ast::abstractd_derivedString_setter(instance):
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

@given(instance=test::ntas::Root_strategy)
@settings(max_examples=50)
def test_test::ntas::root_instantiation(instance):
    assert isinstance(instance, test::ntas::Root)

@given(instance=test::ntas::A_strategy)
@settings(max_examples=50)
def test_test::ntas::a_instantiation(instance):
    assert isinstance(instance, test::ntas::A)

@given(instance=test::ntas::A_strategy)
def test_test::ntas::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::ntas::A_strategy)
def test_test::ntas::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=test::ast::E_strategy)
@settings(max_examples=50)
def test_test::ast::e_instantiation(instance):
    assert isinstance(instance, test::ast::E)

@given(instance=test::ast::E_strategy)
def test_test::ast::e_derivedBool_type(instance):
    assert isinstance(instance.derivedBool, bool)


@given(instance=test::ast::E_strategy)
def test_test::ast::e_derivedBool_setter(instance):
    original = instance.derivedBool
    instance.derivedBool = original
    assert instance.derivedBool == original

@given(instance=test::ast::E_strategy)
def test_test::ast::e_lazyBool_type(instance):
    assert isinstance(instance.lazyBool, bool)


@given(instance=test::ast::E_strategy)
def test_test::ast::e_lazyBool_setter(instance):
    original = instance.lazyBool
    instance.lazyBool = original
    assert instance.lazyBool == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)
