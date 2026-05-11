import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    errors::Ck,
    errors::Registry,
    errors::Fk,
    errors::Column,
    errors::Table,
    Error,
    errors::CheckError,
    errors::ForeignError,
    errors::Error,
    errors::Errores,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_errors::ck_is_not_abstract():
    assert not inspect.isabstract(errors::Ck)


def test_errors::ck_constructor_exists():
    assert callable(errors::Ck.__init__)


def test_errors::ck_constructor_args():
    sig = inspect.signature(errors::Ck.__init__)
    params = list(sig.parameters.keys())



def test_errors::registry_is_not_abstract():
    assert not inspect.isabstract(errors::Registry)


def test_errors::registry_constructor_exists():
    assert callable(errors::Registry.__init__)


def test_errors::registry_constructor_args():
    sig = inspect.signature(errors::Registry.__init__)
    params = list(sig.parameters.keys())



def test_errors::fk_is_not_abstract():
    assert not inspect.isabstract(errors::Fk)


def test_errors::fk_constructor_exists():
    assert callable(errors::Fk.__init__)


def test_errors::fk_constructor_args():
    sig = inspect.signature(errors::Fk.__init__)
    params = list(sig.parameters.keys())



def test_errors::column_is_not_abstract():
    assert not inspect.isabstract(errors::Column)


def test_errors::column_constructor_exists():
    assert callable(errors::Column.__init__)


def test_errors::column_constructor_args():
    sig = inspect.signature(errors::Column.__init__)
    params = list(sig.parameters.keys())



def test_errors::table_is_not_abstract():
    assert not inspect.isabstract(errors::Table)


def test_errors::table_constructor_exists():
    assert callable(errors::Table.__init__)


def test_errors::table_constructor_args():
    sig = inspect.signature(errors::Table.__init__)
    params = list(sig.parameters.keys())



def test_error_is_not_abstract():
    assert not inspect.isabstract(Error)


def test_error_constructor_exists():
    assert callable(Error.__init__)


def test_error_constructor_args():
    sig = inspect.signature(Error.__init__)
    params = list(sig.parameters.keys())



def test_errors::checkerror_is_not_abstract():
    assert not inspect.isabstract(errors::CheckError)


def test_errors::checkerror_constructor_exists():
    assert callable(errors::CheckError.__init__)


def test_errors::checkerror_constructor_args():
    sig = inspect.signature(errors::CheckError.__init__)
    params = list(sig.parameters.keys())
    assert "porcent" in params, "Missing parameter 'porcent'"

def test_errors::checkerror_has_porcent():
    assert hasattr(errors::CheckError, "porcent")
    descriptor = None
    for klass in errors::CheckError.__mro__:
        if "porcent" in klass.__dict__:
            descriptor = klass.__dict__["porcent"]
            break
    assert isinstance(descriptor, property)



def test_errors::foreignerror_is_not_abstract():
    assert not inspect.isabstract(errors::ForeignError)


def test_errors::foreignerror_constructor_exists():
    assert callable(errors::ForeignError.__init__)


def test_errors::foreignerror_constructor_args():
    sig = inspect.signature(errors::ForeignError.__init__)
    params = list(sig.parameters.keys())
    assert "porcent" in params, "Missing parameter 'porcent'"

def test_errors::foreignerror_has_porcent():
    assert hasattr(errors::ForeignError, "porcent")
    descriptor = None
    for klass in errors::ForeignError.__mro__:
        if "porcent" in klass.__dict__:
            descriptor = klass.__dict__["porcent"]
            break
    assert isinstance(descriptor, property)



def test_errors::error_is_not_abstract():
    assert not inspect.isabstract(errors::Error)


def test_errors::error_constructor_exists():
    assert callable(errors::Error.__init__)


def test_errors::error_constructor_args():
    sig = inspect.signature(errors::Error.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "apply" in params, "Missing parameter 'apply'"

def test_errors::error_has_id():
    assert hasattr(errors::Error, "id")
    descriptor = None
    for klass in errors::Error.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_errors::error_has_apply():
    assert hasattr(errors::Error, "apply")
    descriptor = None
    for klass in errors::Error.__mro__:
        if "apply" in klass.__dict__:
            descriptor = klass.__dict__["apply"]
            break
    assert isinstance(descriptor, property)



def test_errors::errores_is_not_abstract():
    assert not inspect.isabstract(errors::Errores)


def test_errors::errores_constructor_exists():
    assert callable(errors::Errores.__init__)


def test_errors::errores_constructor_args():
    sig = inspect.signature(errors::Errores.__init__)
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
errors::Ck_strategy = st.builds(
    errors::Ck,
)
errors::Registry_strategy = st.builds(
    errors::Registry,
)
errors::Fk_strategy = st.builds(
    errors::Fk,
)
errors::Column_strategy = st.builds(
    errors::Column,
)
errors::Table_strategy = st.builds(
    errors::Table,
)
Error_strategy = st.builds(
    Error,
)
errors::CheckError_strategy = st.builds(
    errors::CheckError,
    porcent=
        safe_text
)
errors::ForeignError_strategy = st.builds(
    errors::ForeignError,
    porcent=
        safe_text
)
errors::Error_strategy = st.builds(
    errors::Error,
    id=
        safe_text,
    apply=
        safe_text
)
errors::Errores_strategy = st.builds(
    errors::Errores,
)

@given(instance=errors::Ck_strategy)
@settings(max_examples=50)
def test_errors::ck_instantiation(instance):
    assert isinstance(instance, errors::Ck)

@given(instance=errors::Registry_strategy)
@settings(max_examples=50)
def test_errors::registry_instantiation(instance):
    assert isinstance(instance, errors::Registry)

@given(instance=errors::Fk_strategy)
@settings(max_examples=50)
def test_errors::fk_instantiation(instance):
    assert isinstance(instance, errors::Fk)

@given(instance=errors::Column_strategy)
@settings(max_examples=50)
def test_errors::column_instantiation(instance):
    assert isinstance(instance, errors::Column)

@given(instance=errors::Table_strategy)
@settings(max_examples=50)
def test_errors::table_instantiation(instance):
    assert isinstance(instance, errors::Table)

@given(instance=Error_strategy)
@settings(max_examples=50)
def test_error_instantiation(instance):
    assert isinstance(instance, Error)

@given(instance=errors::CheckError_strategy)
@settings(max_examples=50)
def test_errors::checkerror_instantiation(instance):
    assert isinstance(instance, errors::CheckError)

@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_porcent_type(instance):
    assert isinstance(instance.porcent, str)


@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_porcent_setter(instance):
    original = instance.porcent
    instance.porcent = original
    assert instance.porcent == original

@given(instance=errors::ForeignError_strategy)
@settings(max_examples=50)
def test_errors::foreignerror_instantiation(instance):
    assert isinstance(instance, errors::ForeignError)

@given(instance=errors::ForeignError_strategy)
def test_errors::foreignerror_porcent_type(instance):
    assert isinstance(instance.porcent, str)


@given(instance=errors::ForeignError_strategy)
def test_errors::foreignerror_porcent_setter(instance):
    original = instance.porcent
    instance.porcent = original
    assert instance.porcent == original

@given(instance=errors::Error_strategy)
@settings(max_examples=50)
def test_errors::error_instantiation(instance):
    assert isinstance(instance, errors::Error)

@given(instance=errors::Error_strategy)
def test_errors::error_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=errors::Error_strategy)
def test_errors::error_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=errors::Error_strategy)
def test_errors::error_apply_type(instance):
    assert isinstance(instance.apply, str)


@given(instance=errors::Error_strategy)
def test_errors::error_apply_setter(instance):
    original = instance.apply
    instance.apply = original
    assert instance.apply == original

@given(instance=errors::Errores_strategy)
@settings(max_examples=50)
def test_errors::errores_instantiation(instance):
    assert isinstance(instance, errors::Errores)
