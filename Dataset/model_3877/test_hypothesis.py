import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fl::Function,
    fl::ProgramType,
    fl::EStringToStringMapEntry,
    fl::DocumentRoot,
    fl::Expr,
    Expr,
    fl::Literal,
    fl::Argument,
    fl::IfThenElse,
    fl::Apply,
    fl::Binary,
    Ops,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fl::function_is_not_abstract():
    assert not inspect.isabstract(fl::Function)


def test_fl::function_constructor_exists():
    assert callable(fl::Function.__init__)


def test_fl::function_constructor_args():
    sig = inspect.signature(fl::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "arg" in params, "Missing parameter 'arg'"

def test_fl::function_has_name():
    assert hasattr(fl::Function, "name")
    descriptor = None
    for klass in fl::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fl::function_has_arg():
    assert hasattr(fl::Function, "arg")
    descriptor = None
    for klass in fl::Function.__mro__:
        if "arg" in klass.__dict__:
            descriptor = klass.__dict__["arg"]
            break
    assert isinstance(descriptor, property)



def test_fl::programtype_is_not_abstract():
    assert not inspect.isabstract(fl::ProgramType)


def test_fl::programtype_constructor_exists():
    assert callable(fl::ProgramType.__init__)


def test_fl::programtype_constructor_args():
    sig = inspect.signature(fl::ProgramType.__init__)
    params = list(sig.parameters.keys())



def test_fl::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(fl::EStringToStringMapEntry)


def test_fl::estringtostringmapentry_constructor_exists():
    assert callable(fl::EStringToStringMapEntry.__init__)


def test_fl::estringtostringmapentry_constructor_args():
    sig = inspect.signature(fl::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_fl::documentroot_is_not_abstract():
    assert not inspect.isabstract(fl::DocumentRoot)


def test_fl::documentroot_constructor_exists():
    assert callable(fl::DocumentRoot.__init__)


def test_fl::documentroot_constructor_args():
    sig = inspect.signature(fl::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_fl::documentroot_has_mixed():
    assert hasattr(fl::DocumentRoot, "mixed")
    descriptor = None
    for klass in fl::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_fl::expr_is_not_abstract():
    assert not inspect.isabstract(fl::Expr)


def test_fl::expr_constructor_exists():
    assert callable(fl::Expr.__init__)


def test_fl::expr_constructor_args():
    sig = inspect.signature(fl::Expr.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_fl::literal_is_not_abstract():
    assert not inspect.isabstract(fl::Literal)


def test_fl::literal_constructor_exists():
    assert callable(fl::Literal.__init__)


def test_fl::literal_constructor_args():
    sig = inspect.signature(fl::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"

def test_fl::literal_has_info():
    assert hasattr(fl::Literal, "info")
    descriptor = None
    for klass in fl::Literal.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_fl::argument_is_not_abstract():
    assert not inspect.isabstract(fl::Argument)


def test_fl::argument_constructor_exists():
    assert callable(fl::Argument.__init__)


def test_fl::argument_constructor_args():
    sig = inspect.signature(fl::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl::argument_has_name():
    assert hasattr(fl::Argument, "name")
    descriptor = None
    for klass in fl::Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl::ifthenelse_is_not_abstract():
    assert not inspect.isabstract(fl::IfThenElse)


def test_fl::ifthenelse_constructor_exists():
    assert callable(fl::IfThenElse.__init__)


def test_fl::ifthenelse_constructor_args():
    sig = inspect.signature(fl::IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_fl::apply_is_not_abstract():
    assert not inspect.isabstract(fl::Apply)


def test_fl::apply_constructor_exists():
    assert callable(fl::Apply.__init__)


def test_fl::apply_constructor_args():
    sig = inspect.signature(fl::Apply.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl::apply_has_name():
    assert hasattr(fl::Apply, "name")
    descriptor = None
    for klass in fl::Apply.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl::binary_is_not_abstract():
    assert not inspect.isabstract(fl::Binary)


def test_fl::binary_constructor_exists():
    assert callable(fl::Binary.__init__)


def test_fl::binary_constructor_args():
    sig = inspect.signature(fl::Binary.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_fl::binary_has_ops():
    assert hasattr(fl::Binary, "ops")
    descriptor = None
    for klass in fl::Binary.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)

def test_ops_exists():
    # Check that the Enumeration exists
    assert Ops is not None

def test_ops_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Ops]
    expected_literals = [
        "Minus",
        "Plus",
        "Equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Ops"


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
fl::Function_strategy = st.builds(
    fl::Function,
    name=
        safe_text,
    arg=
        safe_text
)
fl::ProgramType_strategy = st.builds(
    fl::ProgramType,
)
fl::EStringToStringMapEntry_strategy = st.builds(
    fl::EStringToStringMapEntry,
)
fl::DocumentRoot_strategy = st.builds(
    fl::DocumentRoot,
    mixed=
        safe_text
)
fl::Expr_strategy = st.builds(
    fl::Expr,
)
Expr_strategy = st.builds(
    Expr,
)
fl::Literal_strategy = st.builds(
    fl::Literal,
    info=
        safe_text
)
fl::Argument_strategy = st.builds(
    fl::Argument,
    name=
        safe_text
)
fl::IfThenElse_strategy = st.builds(
    fl::IfThenElse,
)
fl::Apply_strategy = st.builds(
    fl::Apply,
    name=
        safe_text
)
fl::Binary_strategy = st.builds(
    fl::Binary,
    ops=
        safe_text
)

@given(instance=fl::Function_strategy)
@settings(max_examples=50)
def test_fl::function_instantiation(instance):
    assert isinstance(instance, fl::Function)

@given(instance=fl::Function_strategy)
def test_fl::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fl::Function_strategy)
def test_fl::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl::Function_strategy)
def test_fl::function_arg_type(instance):
    assert isinstance(instance.arg, str)


@given(instance=fl::Function_strategy)
def test_fl::function_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original

@given(instance=fl::ProgramType_strategy)
@settings(max_examples=50)
def test_fl::programtype_instantiation(instance):
    assert isinstance(instance, fl::ProgramType)

@given(instance=fl::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_fl::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, fl::EStringToStringMapEntry)

@given(instance=fl::DocumentRoot_strategy)
@settings(max_examples=50)
def test_fl::documentroot_instantiation(instance):
    assert isinstance(instance, fl::DocumentRoot)

@given(instance=fl::DocumentRoot_strategy)
def test_fl::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=fl::DocumentRoot_strategy)
def test_fl::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=fl::Expr_strategy)
@settings(max_examples=50)
def test_fl::expr_instantiation(instance):
    assert isinstance(instance, fl::Expr)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=fl::Literal_strategy)
@settings(max_examples=50)
def test_fl::literal_instantiation(instance):
    assert isinstance(instance, fl::Literal)

@given(instance=fl::Literal_strategy)
def test_fl::literal_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=fl::Literal_strategy)
def test_fl::literal_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=fl::Argument_strategy)
@settings(max_examples=50)
def test_fl::argument_instantiation(instance):
    assert isinstance(instance, fl::Argument)

@given(instance=fl::Argument_strategy)
def test_fl::argument_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fl::Argument_strategy)
def test_fl::argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl::IfThenElse_strategy)
@settings(max_examples=50)
def test_fl::ifthenelse_instantiation(instance):
    assert isinstance(instance, fl::IfThenElse)

@given(instance=fl::Apply_strategy)
@settings(max_examples=50)
def test_fl::apply_instantiation(instance):
    assert isinstance(instance, fl::Apply)

@given(instance=fl::Apply_strategy)
def test_fl::apply_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fl::Apply_strategy)
def test_fl::apply_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl::Binary_strategy)
@settings(max_examples=50)
def test_fl::binary_instantiation(instance):
    assert isinstance(instance, fl::Binary)

@given(instance=fl::Binary_strategy)
def test_fl::binary_ops_type(instance):
    assert isinstance(instance.ops, str)


@given(instance=fl::Binary_strategy)
def test_fl::binary_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original
