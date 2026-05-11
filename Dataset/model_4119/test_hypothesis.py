import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    whileComp::Tl,
    whileComp::Hd,
    whileComp::List,
    whileComp::Nil2,
    whileComp::Cons,
    whileComp::Not,
    whileComp::Lexpr,
    whileComp::ExprSimple,
    whileComp::While,
    whileComp::For,
    whileComp::If,
    whileComp::Program,
    whileComp::Foreach,
    whileComp::EObject,
    whileComp::Command,
    whileComp::Nop,
    whileComp::Expr,
    whileComp::Affectation,
    whileComp::Write,
    whileComp::Commands,
    whileComp::Read,
    whileComp::Definition,
    whileComp::Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_whilecomp::tl_is_not_abstract():
    assert not inspect.isabstract(whileComp::Tl)


def test_whilecomp::tl_constructor_exists():
    assert callable(whileComp::Tl.__init__)


def test_whilecomp::tl_constructor_args():
    sig = inspect.signature(whileComp::Tl.__init__)
    params = list(sig.parameters.keys())
    assert "tl" in params, "Missing parameter 'tl'"

def test_whilecomp::tl_has_tl():
    assert hasattr(whileComp::Tl, "tl")
    descriptor = None
    for klass in whileComp::Tl.__mro__:
        if "tl" in klass.__dict__:
            descriptor = klass.__dict__["tl"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::hd_is_not_abstract():
    assert not inspect.isabstract(whileComp::Hd)


def test_whilecomp::hd_constructor_exists():
    assert callable(whileComp::Hd.__init__)


def test_whilecomp::hd_constructor_args():
    sig = inspect.signature(whileComp::Hd.__init__)
    params = list(sig.parameters.keys())
    assert "hd" in params, "Missing parameter 'hd'"

def test_whilecomp::hd_has_hd():
    assert hasattr(whileComp::Hd, "hd")
    descriptor = None
    for klass in whileComp::Hd.__mro__:
        if "hd" in klass.__dict__:
            descriptor = klass.__dict__["hd"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::list_is_not_abstract():
    assert not inspect.isabstract(whileComp::List)


def test_whilecomp::list_constructor_exists():
    assert callable(whileComp::List.__init__)


def test_whilecomp::list_constructor_args():
    sig = inspect.signature(whileComp::List.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_whilecomp::list_has_list():
    assert hasattr(whileComp::List, "list")
    descriptor = None
    for klass in whileComp::List.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::nil2_is_not_abstract():
    assert not inspect.isabstract(whileComp::Nil2)


def test_whilecomp::nil2_constructor_exists():
    assert callable(whileComp::Nil2.__init__)


def test_whilecomp::nil2_constructor_args():
    sig = inspect.signature(whileComp::Nil2.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"

def test_whilecomp::nil2_has_nil():
    assert hasattr(whileComp::Nil2, "nil")
    descriptor = None
    for klass in whileComp::Nil2.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::cons_is_not_abstract():
    assert not inspect.isabstract(whileComp::Cons)


def test_whilecomp::cons_constructor_exists():
    assert callable(whileComp::Cons.__init__)


def test_whilecomp::cons_constructor_args():
    sig = inspect.signature(whileComp::Cons.__init__)
    params = list(sig.parameters.keys())
    assert "cons" in params, "Missing parameter 'cons'"

def test_whilecomp::cons_has_cons():
    assert hasattr(whileComp::Cons, "cons")
    descriptor = None
    for klass in whileComp::Cons.__mro__:
        if "cons" in klass.__dict__:
            descriptor = klass.__dict__["cons"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::not_is_not_abstract():
    assert not inspect.isabstract(whileComp::Not)


def test_whilecomp::not_constructor_exists():
    assert callable(whileComp::Not.__init__)


def test_whilecomp::not_constructor_args():
    sig = inspect.signature(whileComp::Not.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_whilecomp::not_has_not_():
    assert hasattr(whileComp::Not, "not_")
    descriptor = None
    for klass in whileComp::Not.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::lexpr_is_not_abstract():
    assert not inspect.isabstract(whileComp::Lexpr)


def test_whilecomp::lexpr_constructor_exists():
    assert callable(whileComp::Lexpr.__init__)


def test_whilecomp::lexpr_constructor_args():
    sig = inspect.signature(whileComp::Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::exprsimple_is_not_abstract():
    assert not inspect.isabstract(whileComp::ExprSimple)


def test_whilecomp::exprsimple_constructor_exists():
    assert callable(whileComp::ExprSimple.__init__)


def test_whilecomp::exprsimple_constructor_args():
    sig = inspect.signature(whileComp::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "valeur" in params, "Missing parameter 'valeur'"
    assert "ope" in params, "Missing parameter 'ope'"
    assert "call" in params, "Missing parameter 'call'"

def test_whilecomp::exprsimple_has_valeur():
    assert hasattr(whileComp::ExprSimple, "valeur")
    descriptor = None
    for klass in whileComp::ExprSimple.__mro__:
        if "valeur" in klass.__dict__:
            descriptor = klass.__dict__["valeur"]
            break
    assert isinstance(descriptor, property)

def test_whilecomp::exprsimple_has_ope():
    assert hasattr(whileComp::ExprSimple, "ope")
    descriptor = None
    for klass in whileComp::ExprSimple.__mro__:
        if "ope" in klass.__dict__:
            descriptor = klass.__dict__["ope"]
            break
    assert isinstance(descriptor, property)

def test_whilecomp::exprsimple_has_call():
    assert hasattr(whileComp::ExprSimple, "call")
    descriptor = None
    for klass in whileComp::ExprSimple.__mro__:
        if "call" in klass.__dict__:
            descriptor = klass.__dict__["call"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::while_is_not_abstract():
    assert not inspect.isabstract(whileComp::While)


def test_whilecomp::while_constructor_exists():
    assert callable(whileComp::While.__init__)


def test_whilecomp::while_constructor_args():
    sig = inspect.signature(whileComp::While.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::for_is_not_abstract():
    assert not inspect.isabstract(whileComp::For)


def test_whilecomp::for_constructor_exists():
    assert callable(whileComp::For.__init__)


def test_whilecomp::for_constructor_args():
    sig = inspect.signature(whileComp::For.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::if_is_not_abstract():
    assert not inspect.isabstract(whileComp::If)


def test_whilecomp::if_constructor_exists():
    assert callable(whileComp::If.__init__)


def test_whilecomp::if_constructor_args():
    sig = inspect.signature(whileComp::If.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::program_is_not_abstract():
    assert not inspect.isabstract(whileComp::Program)


def test_whilecomp::program_constructor_exists():
    assert callable(whileComp::Program.__init__)


def test_whilecomp::program_constructor_args():
    sig = inspect.signature(whileComp::Program.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::foreach_is_not_abstract():
    assert not inspect.isabstract(whileComp::Foreach)


def test_whilecomp::foreach_constructor_exists():
    assert callable(whileComp::Foreach.__init__)


def test_whilecomp::foreach_constructor_args():
    sig = inspect.signature(whileComp::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::eobject_is_not_abstract():
    assert not inspect.isabstract(whileComp::EObject)


def test_whilecomp::eobject_constructor_exists():
    assert callable(whileComp::EObject.__init__)


def test_whilecomp::eobject_constructor_args():
    sig = inspect.signature(whileComp::EObject.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::command_is_not_abstract():
    assert not inspect.isabstract(whileComp::Command)


def test_whilecomp::command_constructor_exists():
    assert callable(whileComp::Command.__init__)


def test_whilecomp::command_constructor_args():
    sig = inspect.signature(whileComp::Command.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::nop_is_not_abstract():
    assert not inspect.isabstract(whileComp::Nop)


def test_whilecomp::nop_constructor_exists():
    assert callable(whileComp::Nop.__init__)


def test_whilecomp::nop_constructor_args():
    sig = inspect.signature(whileComp::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_whilecomp::nop_has_nop():
    assert hasattr(whileComp::Nop, "nop")
    descriptor = None
    for klass in whileComp::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::expr_is_not_abstract():
    assert not inspect.isabstract(whileComp::Expr)


def test_whilecomp::expr_constructor_exists():
    assert callable(whileComp::Expr.__init__)


def test_whilecomp::expr_constructor_args():
    sig = inspect.signature(whileComp::Expr.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::affectation_is_not_abstract():
    assert not inspect.isabstract(whileComp::Affectation)


def test_whilecomp::affectation_constructor_exists():
    assert callable(whileComp::Affectation.__init__)


def test_whilecomp::affectation_constructor_args():
    sig = inspect.signature(whileComp::Affectation.__init__)
    params = list(sig.parameters.keys())
    assert "affectations" in params, "Missing parameter 'affectations'"

def test_whilecomp::affectation_has_affectations():
    assert hasattr(whileComp::Affectation, "affectations")
    descriptor = None
    for klass in whileComp::Affectation.__mro__:
        if "affectations" in klass.__dict__:
            descriptor = klass.__dict__["affectations"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::write_is_not_abstract():
    assert not inspect.isabstract(whileComp::Write)


def test_whilecomp::write_constructor_exists():
    assert callable(whileComp::Write.__init__)


def test_whilecomp::write_constructor_args():
    sig = inspect.signature(whileComp::Write.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilecomp::write_has_variable():
    assert hasattr(whileComp::Write, "variable")
    descriptor = None
    for klass in whileComp::Write.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::commands_is_not_abstract():
    assert not inspect.isabstract(whileComp::Commands)


def test_whilecomp::commands_constructor_exists():
    assert callable(whileComp::Commands.__init__)


def test_whilecomp::commands_constructor_args():
    sig = inspect.signature(whileComp::Commands.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::read_is_not_abstract():
    assert not inspect.isabstract(whileComp::Read)


def test_whilecomp::read_constructor_exists():
    assert callable(whileComp::Read.__init__)


def test_whilecomp::read_constructor_args():
    sig = inspect.signature(whileComp::Read.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilecomp::read_has_variable():
    assert hasattr(whileComp::Read, "variable")
    descriptor = None
    for klass in whileComp::Read.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp::definition_is_not_abstract():
    assert not inspect.isabstract(whileComp::Definition)


def test_whilecomp::definition_constructor_exists():
    assert callable(whileComp::Definition.__init__)


def test_whilecomp::definition_constructor_args():
    sig = inspect.signature(whileComp::Definition.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp::function_is_not_abstract():
    assert not inspect.isabstract(whileComp::Function)


def test_whilecomp::function_constructor_exists():
    assert callable(whileComp::Function.__init__)


def test_whilecomp::function_constructor_args():
    sig = inspect.signature(whileComp::Function.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_whilecomp::function_has_function():
    assert hasattr(whileComp::Function, "function")
    descriptor = None
    for klass in whileComp::Function.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
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
whileComp::Tl_strategy = st.builds(
    whileComp::Tl,
    tl=
        safe_text
)
whileComp::Hd_strategy = st.builds(
    whileComp::Hd,
    hd=
        safe_text
)
whileComp::List_strategy = st.builds(
    whileComp::List,
    list=
        safe_text
)
whileComp::Nil2_strategy = st.builds(
    whileComp::Nil2,
    nil=
        safe_text
)
whileComp::Cons_strategy = st.builds(
    whileComp::Cons,
    cons=
        safe_text
)
whileComp::Not_strategy = st.builds(
    whileComp::Not,
    not_=
        safe_text
)
whileComp::Lexpr_strategy = st.builds(
    whileComp::Lexpr,
)
whileComp::ExprSimple_strategy = st.builds(
    whileComp::ExprSimple,
    valeur=
        safe_text,
    ope=
        safe_text,
    call=
        safe_text
)
whileComp::While_strategy = st.builds(
    whileComp::While,
)
whileComp::For_strategy = st.builds(
    whileComp::For,
)
whileComp::If_strategy = st.builds(
    whileComp::If,
)
whileComp::Program_strategy = st.builds(
    whileComp::Program,
)
whileComp::Foreach_strategy = st.builds(
    whileComp::Foreach,
)
whileComp::EObject_strategy = st.builds(
    whileComp::EObject,
)
whileComp::Command_strategy = st.builds(
    whileComp::Command,
)
whileComp::Nop_strategy = st.builds(
    whileComp::Nop,
    nop=
        safe_text
)
whileComp::Expr_strategy = st.builds(
    whileComp::Expr,
)
whileComp::Affectation_strategy = st.builds(
    whileComp::Affectation,
    affectations=
        safe_text
)
whileComp::Write_strategy = st.builds(
    whileComp::Write,
    variable=
        safe_text
)
whileComp::Commands_strategy = st.builds(
    whileComp::Commands,
)
whileComp::Read_strategy = st.builds(
    whileComp::Read,
    variable=
        safe_text
)
whileComp::Definition_strategy = st.builds(
    whileComp::Definition,
)
whileComp::Function_strategy = st.builds(
    whileComp::Function,
    function=
        safe_text
)

@given(instance=whileComp::Tl_strategy)
@settings(max_examples=50)
def test_whilecomp::tl_instantiation(instance):
    assert isinstance(instance, whileComp::Tl)

@given(instance=whileComp::Tl_strategy)
def test_whilecomp::tl_tl_type(instance):
    assert isinstance(instance.tl, str)


@given(instance=whileComp::Tl_strategy)
def test_whilecomp::tl_tl_setter(instance):
    original = instance.tl
    instance.tl = original
    assert instance.tl == original

@given(instance=whileComp::Hd_strategy)
@settings(max_examples=50)
def test_whilecomp::hd_instantiation(instance):
    assert isinstance(instance, whileComp::Hd)

@given(instance=whileComp::Hd_strategy)
def test_whilecomp::hd_hd_type(instance):
    assert isinstance(instance.hd, str)


@given(instance=whileComp::Hd_strategy)
def test_whilecomp::hd_hd_setter(instance):
    original = instance.hd
    instance.hd = original
    assert instance.hd == original

@given(instance=whileComp::List_strategy)
@settings(max_examples=50)
def test_whilecomp::list_instantiation(instance):
    assert isinstance(instance, whileComp::List)

@given(instance=whileComp::List_strategy)
def test_whilecomp::list_list_type(instance):
    assert isinstance(instance.list, str)


@given(instance=whileComp::List_strategy)
def test_whilecomp::list_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=whileComp::Nil2_strategy)
@settings(max_examples=50)
def test_whilecomp::nil2_instantiation(instance):
    assert isinstance(instance, whileComp::Nil2)

@given(instance=whileComp::Nil2_strategy)
def test_whilecomp::nil2_nil_type(instance):
    assert isinstance(instance.nil, str)


@given(instance=whileComp::Nil2_strategy)
def test_whilecomp::nil2_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=whileComp::Cons_strategy)
@settings(max_examples=50)
def test_whilecomp::cons_instantiation(instance):
    assert isinstance(instance, whileComp::Cons)

@given(instance=whileComp::Cons_strategy)
def test_whilecomp::cons_cons_type(instance):
    assert isinstance(instance.cons, str)


@given(instance=whileComp::Cons_strategy)
def test_whilecomp::cons_cons_setter(instance):
    original = instance.cons
    instance.cons = original
    assert instance.cons == original

@given(instance=whileComp::Not_strategy)
@settings(max_examples=50)
def test_whilecomp::not_instantiation(instance):
    assert isinstance(instance, whileComp::Not)

@given(instance=whileComp::Not_strategy)
def test_whilecomp::not_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=whileComp::Not_strategy)
def test_whilecomp::not_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=whileComp::Lexpr_strategy)
@settings(max_examples=50)
def test_whilecomp::lexpr_instantiation(instance):
    assert isinstance(instance, whileComp::Lexpr)

@given(instance=whileComp::ExprSimple_strategy)
@settings(max_examples=50)
def test_whilecomp::exprsimple_instantiation(instance):
    assert isinstance(instance, whileComp::ExprSimple)

@given(instance=whileComp::ExprSimple_strategy)
def test_whilecomp::exprsimple_valeur_type(instance):
    assert isinstance(instance.valeur, str)


@given(instance=whileComp::ExprSimple_strategy)
def test_whilecomp::exprsimple_valeur_setter(instance):
    original = instance.valeur
    instance.valeur = original
    assert instance.valeur == original

@given(instance=whileComp::ExprSimple_strategy)
def test_whilecomp::exprsimple_ope_type(instance):
    assert isinstance(instance.ope, str)


@given(instance=whileComp::ExprSimple_strategy)
def test_whilecomp::exprsimple_ope_setter(instance):
    original = instance.ope
    instance.ope = original
    assert instance.ope == original

@given(instance=whileComp::ExprSimple_strategy)
def test_whilecomp::exprsimple_call_type(instance):
    assert isinstance(instance.call, str)


@given(instance=whileComp::ExprSimple_strategy)
def test_whilecomp::exprsimple_call_setter(instance):
    original = instance.call
    instance.call = original
    assert instance.call == original

@given(instance=whileComp::While_strategy)
@settings(max_examples=50)
def test_whilecomp::while_instantiation(instance):
    assert isinstance(instance, whileComp::While)

@given(instance=whileComp::For_strategy)
@settings(max_examples=50)
def test_whilecomp::for_instantiation(instance):
    assert isinstance(instance, whileComp::For)

@given(instance=whileComp::If_strategy)
@settings(max_examples=50)
def test_whilecomp::if_instantiation(instance):
    assert isinstance(instance, whileComp::If)

@given(instance=whileComp::Program_strategy)
@settings(max_examples=50)
def test_whilecomp::program_instantiation(instance):
    assert isinstance(instance, whileComp::Program)

@given(instance=whileComp::Foreach_strategy)
@settings(max_examples=50)
def test_whilecomp::foreach_instantiation(instance):
    assert isinstance(instance, whileComp::Foreach)

@given(instance=whileComp::EObject_strategy)
@settings(max_examples=50)
def test_whilecomp::eobject_instantiation(instance):
    assert isinstance(instance, whileComp::EObject)

@given(instance=whileComp::Command_strategy)
@settings(max_examples=50)
def test_whilecomp::command_instantiation(instance):
    assert isinstance(instance, whileComp::Command)

@given(instance=whileComp::Nop_strategy)
@settings(max_examples=50)
def test_whilecomp::nop_instantiation(instance):
    assert isinstance(instance, whileComp::Nop)

@given(instance=whileComp::Nop_strategy)
def test_whilecomp::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=whileComp::Nop_strategy)
def test_whilecomp::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=whileComp::Expr_strategy)
@settings(max_examples=50)
def test_whilecomp::expr_instantiation(instance):
    assert isinstance(instance, whileComp::Expr)

@given(instance=whileComp::Affectation_strategy)
@settings(max_examples=50)
def test_whilecomp::affectation_instantiation(instance):
    assert isinstance(instance, whileComp::Affectation)

@given(instance=whileComp::Affectation_strategy)
def test_whilecomp::affectation_affectations_type(instance):
    assert isinstance(instance.affectations, str)


@given(instance=whileComp::Affectation_strategy)
def test_whilecomp::affectation_affectations_setter(instance):
    original = instance.affectations
    instance.affectations = original
    assert instance.affectations == original

@given(instance=whileComp::Write_strategy)
@settings(max_examples=50)
def test_whilecomp::write_instantiation(instance):
    assert isinstance(instance, whileComp::Write)

@given(instance=whileComp::Write_strategy)
def test_whilecomp::write_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=whileComp::Write_strategy)
def test_whilecomp::write_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileComp::Commands_strategy)
@settings(max_examples=50)
def test_whilecomp::commands_instantiation(instance):
    assert isinstance(instance, whileComp::Commands)

@given(instance=whileComp::Read_strategy)
@settings(max_examples=50)
def test_whilecomp::read_instantiation(instance):
    assert isinstance(instance, whileComp::Read)

@given(instance=whileComp::Read_strategy)
def test_whilecomp::read_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=whileComp::Read_strategy)
def test_whilecomp::read_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileComp::Definition_strategy)
@settings(max_examples=50)
def test_whilecomp::definition_instantiation(instance):
    assert isinstance(instance, whileComp::Definition)

@given(instance=whileComp::Function_strategy)
@settings(max_examples=50)
def test_whilecomp::function_instantiation(instance):
    assert isinstance(instance, whileComp::Function)

@given(instance=whileComp::Function_strategy)
def test_whilecomp::function_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=whileComp::Function_strategy)
def test_whilecomp::function_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original
