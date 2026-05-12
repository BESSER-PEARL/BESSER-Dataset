import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fl_DocumentRoot,
    fl_Function,
    fl_ProgramType,
    fl_EStringToStringMapEntry,
    Expr,
    fl_IfThenElse,
    fl_Literal,
    fl_Apply,
    fl_Binary,
    fl_Argument,
    fl_Expr,
    Ops,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fl_documentroot_is_not_abstract():
    assert not inspect.isabstract(fl_DocumentRoot)


def test_fl_documentroot_constructor_exists():
    assert callable(fl_DocumentRoot.__init__)


def test_fl_documentroot_constructor_args():
    sig = inspect.signature(fl_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_fl_documentroot_has_mixed():
    assert hasattr(fl_DocumentRoot, "mixed")
    descriptor = None
    for klass in fl_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_fl_function_is_not_abstract():
    assert not inspect.isabstract(fl_Function)


def test_fl_function_constructor_exists():
    assert callable(fl_Function.__init__)


def test_fl_function_constructor_args():
    sig = inspect.signature(fl_Function.__init__)
    params = list(sig.parameters.keys())
    assert "arg" in params, "Missing parameter 'arg'"
    assert "name" in params, "Missing parameter 'name'"

def test_fl_function_has_arg():
    assert hasattr(fl_Function, "arg")
    descriptor = None
    for klass in fl_Function.__mro__:
        if "arg" in klass.__dict__:
            descriptor = klass.__dict__["arg"]
            break
    assert isinstance(descriptor, property)

def test_fl_function_has_name():
    assert hasattr(fl_Function, "name")
    descriptor = None
    for klass in fl_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl_programtype_is_not_abstract():
    assert not inspect.isabstract(fl_ProgramType)


def test_fl_programtype_constructor_exists():
    assert callable(fl_ProgramType.__init__)


def test_fl_programtype_constructor_args():
    sig = inspect.signature(fl_ProgramType.__init__)
    params = list(sig.parameters.keys())



def test_fl_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(fl_EStringToStringMapEntry)


def test_fl_estringtostringmapentry_constructor_exists():
    assert callable(fl_EStringToStringMapEntry.__init__)


def test_fl_estringtostringmapentry_constructor_args():
    sig = inspect.signature(fl_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_fl_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(fl_IfThenElse)


def test_fl_ifthenelse_constructor_exists():
    assert callable(fl_IfThenElse.__init__)


def test_fl_ifthenelse_constructor_args():
    sig = inspect.signature(fl_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_fl_literal_is_not_abstract():
    assert not inspect.isabstract(fl_Literal)


def test_fl_literal_constructor_exists():
    assert callable(fl_Literal.__init__)


def test_fl_literal_constructor_args():
    sig = inspect.signature(fl_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"

def test_fl_literal_has_info():
    assert hasattr(fl_Literal, "info")
    descriptor = None
    for klass in fl_Literal.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_fl_apply_is_not_abstract():
    assert not inspect.isabstract(fl_Apply)


def test_fl_apply_constructor_exists():
    assert callable(fl_Apply.__init__)


def test_fl_apply_constructor_args():
    sig = inspect.signature(fl_Apply.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl_apply_has_name():
    assert hasattr(fl_Apply, "name")
    descriptor = None
    for klass in fl_Apply.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl_binary_is_not_abstract():
    assert not inspect.isabstract(fl_Binary)


def test_fl_binary_constructor_exists():
    assert callable(fl_Binary.__init__)


def test_fl_binary_constructor_args():
    sig = inspect.signature(fl_Binary.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_fl_binary_has_ops():
    assert hasattr(fl_Binary, "ops")
    descriptor = None
    for klass in fl_Binary.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_fl_argument_is_not_abstract():
    assert not inspect.isabstract(fl_Argument)


def test_fl_argument_constructor_exists():
    assert callable(fl_Argument.__init__)


def test_fl_argument_constructor_args():
    sig = inspect.signature(fl_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl_argument_has_name():
    assert hasattr(fl_Argument, "name")
    descriptor = None
    for klass in fl_Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl_expr_is_not_abstract():
    assert not inspect.isabstract(fl_Expr)


def test_fl_expr_constructor_exists():
    assert callable(fl_Expr.__init__)


def test_fl_expr_constructor_args():
    sig = inspect.signature(fl_Expr.__init__)
    params = list(sig.parameters.keys())

def test_ops_exists():
    # Check that the Enumeration exists
    assert Ops is not None

def test_ops_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Ops]
    expected_literals = [
        "Equal",
        "Minus",
        "Plus",
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
fl_DocumentRoot_strategy = st.builds(
    fl_DocumentRoot,
    mixed=
        safe_text
)
fl_Function_strategy = st.builds(
    fl_Function,
    arg=
        safe_text,
    name=
        safe_text
)
fl_ProgramType_strategy = st.builds(
    fl_ProgramType,
)
fl_EStringToStringMapEntry_strategy = st.builds(
    fl_EStringToStringMapEntry,
)
Expr_strategy = st.builds(
    Expr,
)
fl_IfThenElse_strategy = st.builds(
    fl_IfThenElse,
)
fl_Literal_strategy = st.builds(
    fl_Literal,
    info=
        safe_text
)
fl_Apply_strategy = st.builds(
    fl_Apply,
    name=
        safe_text
)
fl_Binary_strategy = st.builds(
    fl_Binary,
    ops=
        safe_text
)
fl_Argument_strategy = st.builds(
    fl_Argument,
    name=
        safe_text
)
fl_Expr_strategy = st.builds(
    fl_Expr,
)

@given(instance=fl_DocumentRoot_strategy)
@settings(max_examples=50)
def test_fl_documentroot_instantiation(instance):
    assert isinstance(instance, fl_DocumentRoot)



@given(instance=fl_DocumentRoot_strategy)
def test_fl_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=fl_Function_strategy)
@settings(max_examples=50)
def test_fl_function_instantiation(instance):
    assert isinstance(instance, fl_Function)



@given(instance=fl_Function_strategy)
def test_fl_function_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original



@given(instance=fl_Function_strategy)
def test_fl_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl_ProgramType_strategy)
@settings(max_examples=50)
def test_fl_programtype_instantiation(instance):
    assert isinstance(instance, fl_ProgramType)

@given(instance=fl_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_fl_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, fl_EStringToStringMapEntry)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=fl_IfThenElse_strategy)
@settings(max_examples=50)
def test_fl_ifthenelse_instantiation(instance):
    assert isinstance(instance, fl_IfThenElse)

@given(instance=fl_Literal_strategy)
@settings(max_examples=50)
def test_fl_literal_instantiation(instance):
    assert isinstance(instance, fl_Literal)



@given(instance=fl_Literal_strategy)
def test_fl_literal_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=fl_Apply_strategy)
@settings(max_examples=50)
def test_fl_apply_instantiation(instance):
    assert isinstance(instance, fl_Apply)



@given(instance=fl_Apply_strategy)
def test_fl_apply_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl_Binary_strategy)
@settings(max_examples=50)
def test_fl_binary_instantiation(instance):
    assert isinstance(instance, fl_Binary)



@given(instance=fl_Binary_strategy)
def test_fl_binary_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=fl_Argument_strategy)
@settings(max_examples=50)
def test_fl_argument_instantiation(instance):
    assert isinstance(instance, fl_Argument)



@given(instance=fl_Argument_strategy)
def test_fl_argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl_Expr_strategy)
@settings(max_examples=50)
def test_fl_expr_instantiation(instance):
    assert isinstance(instance, fl_Expr)
