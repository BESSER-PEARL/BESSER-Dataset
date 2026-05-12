import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    errors_Fk,
    errors_Column,
    errors_Table,
    Error,
    errors_ForeignError,
    errors_Error,
    errors_Errores,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_errors_fk_is_not_abstract():
    assert not inspect.isabstract(errors_Fk)


def test_errors_fk_constructor_exists():
    assert callable(errors_Fk.__init__)


def test_errors_fk_constructor_args():
    sig = inspect.signature(errors_Fk.__init__)
    params = list(sig.parameters.keys())



def test_errors_column_is_not_abstract():
    assert not inspect.isabstract(errors_Column)


def test_errors_column_constructor_exists():
    assert callable(errors_Column.__init__)


def test_errors_column_constructor_args():
    sig = inspect.signature(errors_Column.__init__)
    params = list(sig.parameters.keys())



def test_errors_table_is_not_abstract():
    assert not inspect.isabstract(errors_Table)


def test_errors_table_constructor_exists():
    assert callable(errors_Table.__init__)


def test_errors_table_constructor_args():
    sig = inspect.signature(errors_Table.__init__)
    params = list(sig.parameters.keys())



def test_error_is_not_abstract():
    assert not inspect.isabstract(Error)


def test_error_constructor_exists():
    assert callable(Error.__init__)


def test_error_constructor_args():
    sig = inspect.signature(Error.__init__)
    params = list(sig.parameters.keys())



def test_errors_foreignerror_is_not_abstract():
    assert not inspect.isabstract(errors_ForeignError)


def test_errors_foreignerror_constructor_exists():
    assert callable(errors_ForeignError.__init__)


def test_errors_foreignerror_constructor_args():
    sig = inspect.signature(errors_ForeignError.__init__)
    params = list(sig.parameters.keys())
    assert "porcent" in params, "Missing parameter 'porcent'"

def test_errors_foreignerror_has_porcent():
    assert hasattr(errors_ForeignError, "porcent")
    descriptor = None
    for klass in errors_ForeignError.__mro__:
        if "porcent" in klass.__dict__:
            descriptor = klass.__dict__["porcent"]
            break
    assert isinstance(descriptor, property)



def test_errors_error_is_not_abstract():
    assert not inspect.isabstract(errors_Error)


def test_errors_error_constructor_exists():
    assert callable(errors_Error.__init__)


def test_errors_error_constructor_args():
    sig = inspect.signature(errors_Error.__init__)
    params = list(sig.parameters.keys())
    assert "apply" in params, "Missing parameter 'apply'"
    assert "id" in params, "Missing parameter 'id'"

def test_errors_error_has_apply():
    assert hasattr(errors_Error, "apply")
    descriptor = None
    for klass in errors_Error.__mro__:
        if "apply" in klass.__dict__:
            descriptor = klass.__dict__["apply"]
            break
    assert isinstance(descriptor, property)

def test_errors_error_has_id():
    assert hasattr(errors_Error, "id")
    descriptor = None
    for klass in errors_Error.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_errors_errores_is_not_abstract():
    assert not inspect.isabstract(errors_Errores)


def test_errors_errores_constructor_exists():
    assert callable(errors_Errores.__init__)


def test_errors_errores_constructor_args():
    sig = inspect.signature(errors_Errores.__init__)
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
errors_Fk_strategy = st.builds(
    errors_Fk,
)
errors_Column_strategy = st.builds(
    errors_Column,
)
errors_Table_strategy = st.builds(
    errors_Table,
)
Error_strategy = st.builds(
    Error,
)
errors_ForeignError_strategy = st.builds(
    errors_ForeignError,
    porcent=
        st.integers()
)
errors_Error_strategy = st.builds(
    errors_Error,
    apply=
        st.booleans(),
    id=
        st.integers()
)
errors_Errores_strategy = st.builds(
    errors_Errores,
)

@given(instance=errors_Fk_strategy)
@settings(max_examples=50)
def test_errors_fk_instantiation(instance):
    assert isinstance(instance, errors_Fk)

@given(instance=errors_Column_strategy)
@settings(max_examples=50)
def test_errors_column_instantiation(instance):
    assert isinstance(instance, errors_Column)

@given(instance=errors_Table_strategy)
@settings(max_examples=50)
def test_errors_table_instantiation(instance):
    assert isinstance(instance, errors_Table)

@given(instance=Error_strategy)
@settings(max_examples=50)
def test_error_instantiation(instance):
    assert isinstance(instance, Error)

@given(instance=errors_ForeignError_strategy)
@settings(max_examples=50)
def test_errors_foreignerror_instantiation(instance):
    assert isinstance(instance, errors_ForeignError)



@given(instance=errors_ForeignError_strategy)
def test_errors_foreignerror_porcent_setter(instance):
    original = instance.porcent
    instance.porcent = original
    assert instance.porcent == original

@given(instance=errors_Error_strategy)
@settings(max_examples=50)
def test_errors_error_instantiation(instance):
    assert isinstance(instance, errors_Error)



@given(instance=errors_Error_strategy)
def test_errors_error_apply_setter(instance):
    original = instance.apply
    instance.apply = original
    assert instance.apply == original



@given(instance=errors_Error_strategy)
def test_errors_error_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=errors_Errores_strategy)
@settings(max_examples=50)
def test_errors_errores_instantiation(instance):
    assert isinstance(instance, errors_Errores)
