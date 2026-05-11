import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Stmt,
    simpleal::Assign,
    simpleal::Print,
    ArithOp,
    simpleal::ArithMinus,
    simpleal::ArithPlus,
    Arith,
    simpleal::ArithLit,
    simpleal::ArithOp,
    simpleal::VarRef,
    simpleal::Arith,
    simpleal::Stmt,
    simpleal::Block,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::assign_is_not_abstract():
    assert not inspect.isabstract(simpleal::Assign)


def test_simpleal::assign_constructor_exists():
    assert callable(simpleal::Assign.__init__)


def test_simpleal::assign_constructor_args():
    sig = inspect.signature(simpleal::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleal::assign_has_name():
    assert hasattr(simpleal::Assign, "name")
    descriptor = None
    for klass in simpleal::Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleal::print_is_not_abstract():
    assert not inspect.isabstract(simpleal::Print)


def test_simpleal::print_constructor_exists():
    assert callable(simpleal::Print.__init__)


def test_simpleal::print_constructor_args():
    sig = inspect.signature(simpleal::Print.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleal::print_has_name():
    assert hasattr(simpleal::Print, "name")
    descriptor = None
    for klass in simpleal::Print.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arithop_is_not_abstract():
    assert not inspect.isabstract(ArithOp)


def test_arithop_constructor_exists():
    assert callable(ArithOp.__init__)


def test_arithop_constructor_args():
    sig = inspect.signature(ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::arithminus_is_not_abstract():
    assert not inspect.isabstract(simpleal::ArithMinus)


def test_simpleal::arithminus_constructor_exists():
    assert callable(simpleal::ArithMinus.__init__)


def test_simpleal::arithminus_constructor_args():
    sig = inspect.signature(simpleal::ArithMinus.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::arithplus_is_not_abstract():
    assert not inspect.isabstract(simpleal::ArithPlus)


def test_simpleal::arithplus_constructor_exists():
    assert callable(simpleal::ArithPlus.__init__)


def test_simpleal::arithplus_constructor_args():
    sig = inspect.signature(simpleal::ArithPlus.__init__)
    params = list(sig.parameters.keys())



def test_arith_is_not_abstract():
    assert not inspect.isabstract(Arith)


def test_arith_constructor_exists():
    assert callable(Arith.__init__)


def test_arith_constructor_args():
    sig = inspect.signature(Arith.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::arithlit_is_not_abstract():
    assert not inspect.isabstract(simpleal::ArithLit)


def test_simpleal::arithlit_constructor_exists():
    assert callable(simpleal::ArithLit.__init__)


def test_simpleal::arithlit_constructor_args():
    sig = inspect.signature(simpleal::ArithLit.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_simpleal::arithlit_has_val():
    assert hasattr(simpleal::ArithLit, "val")
    descriptor = None
    for klass in simpleal::ArithLit.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_simpleal::arithop_is_not_abstract():
    assert not inspect.isabstract(simpleal::ArithOp)


def test_simpleal::arithop_constructor_exists():
    assert callable(simpleal::ArithOp.__init__)


def test_simpleal::arithop_constructor_args():
    sig = inspect.signature(simpleal::ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::varref_is_not_abstract():
    assert not inspect.isabstract(simpleal::VarRef)


def test_simpleal::varref_constructor_exists():
    assert callable(simpleal::VarRef.__init__)


def test_simpleal::varref_constructor_args():
    sig = inspect.signature(simpleal::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleal::varref_has_name():
    assert hasattr(simpleal::VarRef, "name")
    descriptor = None
    for klass in simpleal::VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleal::arith_is_not_abstract():
    assert not inspect.isabstract(simpleal::Arith)


def test_simpleal::arith_constructor_exists():
    assert callable(simpleal::Arith.__init__)


def test_simpleal::arith_constructor_args():
    sig = inspect.signature(simpleal::Arith.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::stmt_is_not_abstract():
    assert not inspect.isabstract(simpleal::Stmt)


def test_simpleal::stmt_constructor_exists():
    assert callable(simpleal::Stmt.__init__)


def test_simpleal::stmt_constructor_args():
    sig = inspect.signature(simpleal::Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simpleal::block_is_not_abstract():
    assert not inspect.isabstract(simpleal::Block)


def test_simpleal::block_constructor_exists():
    assert callable(simpleal::Block.__init__)


def test_simpleal::block_constructor_args():
    sig = inspect.signature(simpleal::Block.__init__)
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
Stmt_strategy = st.builds(
    Stmt,
)
simpleal::Assign_strategy = st.builds(
    simpleal::Assign,
    name=
        safe_text
)
simpleal::Print_strategy = st.builds(
    simpleal::Print,
    name=
        safe_text
)
ArithOp_strategy = st.builds(
    ArithOp,
)
simpleal::ArithMinus_strategy = st.builds(
    simpleal::ArithMinus,
)
simpleal::ArithPlus_strategy = st.builds(
    simpleal::ArithPlus,
)
Arith_strategy = st.builds(
    Arith,
)
simpleal::ArithLit_strategy = st.builds(
    simpleal::ArithLit,
    val=
        st.integers()
)
simpleal::ArithOp_strategy = st.builds(
    simpleal::ArithOp,
)
simpleal::VarRef_strategy = st.builds(
    simpleal::VarRef,
    name=
        safe_text
)
simpleal::Arith_strategy = st.builds(
    simpleal::Arith,
)
simpleal::Stmt_strategy = st.builds(
    simpleal::Stmt,
)
simpleal::Block_strategy = st.builds(
    simpleal::Block,
)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=simpleal::Assign_strategy)
@settings(max_examples=50)
def test_simpleal::assign_instantiation(instance):
    assert isinstance(instance, simpleal::Assign)

@given(instance=simpleal::Assign_strategy)
def test_simpleal::assign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleal::Assign_strategy)
def test_simpleal::assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleal::Print_strategy)
@settings(max_examples=50)
def test_simpleal::print_instantiation(instance):
    assert isinstance(instance, simpleal::Print)

@given(instance=simpleal::Print_strategy)
def test_simpleal::print_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleal::Print_strategy)
def test_simpleal::print_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ArithOp_strategy)
@settings(max_examples=50)
def test_arithop_instantiation(instance):
    assert isinstance(instance, ArithOp)

@given(instance=simpleal::ArithMinus_strategy)
@settings(max_examples=50)
def test_simpleal::arithminus_instantiation(instance):
    assert isinstance(instance, simpleal::ArithMinus)

@given(instance=simpleal::ArithPlus_strategy)
@settings(max_examples=50)
def test_simpleal::arithplus_instantiation(instance):
    assert isinstance(instance, simpleal::ArithPlus)

@given(instance=Arith_strategy)
@settings(max_examples=50)
def test_arith_instantiation(instance):
    assert isinstance(instance, Arith)

@given(instance=simpleal::ArithLit_strategy)
@settings(max_examples=50)
def test_simpleal::arithlit_instantiation(instance):
    assert isinstance(instance, simpleal::ArithLit)

@given(instance=simpleal::ArithLit_strategy)
def test_simpleal::arithlit_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=simpleal::ArithLit_strategy)
def test_simpleal::arithlit_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=simpleal::ArithOp_strategy)
@settings(max_examples=50)
def test_simpleal::arithop_instantiation(instance):
    assert isinstance(instance, simpleal::ArithOp)

@given(instance=simpleal::VarRef_strategy)
@settings(max_examples=50)
def test_simpleal::varref_instantiation(instance):
    assert isinstance(instance, simpleal::VarRef)

@given(instance=simpleal::VarRef_strategy)
def test_simpleal::varref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleal::VarRef_strategy)
def test_simpleal::varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleal::Arith_strategy)
@settings(max_examples=50)
def test_simpleal::arith_instantiation(instance):
    assert isinstance(instance, simpleal::Arith)

@given(instance=simpleal::Stmt_strategy)
@settings(max_examples=50)
def test_simpleal::stmt_instantiation(instance):
    assert isinstance(instance, simpleal::Stmt)

@given(instance=simpleal::Block_strategy)
@settings(max_examples=50)
def test_simpleal::block_instantiation(instance):
    assert isinstance(instance, simpleal::Block)
