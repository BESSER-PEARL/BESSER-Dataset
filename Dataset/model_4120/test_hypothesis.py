import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    whileLanguage::Lexpr,
    whileLanguage::While,
    whileLanguage::For,
    whileLanguage::If,
    whileLanguage::Expr,
    whileLanguage::Affectation,
    whileLanguage::Write,
    whileLanguage::Commands,
    whileLanguage::Read,
    whileLanguage::Definition,
    whileLanguage::Function,
    whileLanguage::Program,
    whileLanguage::Foreach,
    whileLanguage::EObject,
    whileLanguage::Command,
    whileLanguage::Nop,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_whilelanguage::lexpr_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Lexpr)


def test_whilelanguage::lexpr_constructor_exists():
    assert callable(whileLanguage::Lexpr.__init__)


def test_whilelanguage::lexpr_constructor_args():
    sig = inspect.signature(whileLanguage::Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::while_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::While)


def test_whilelanguage::while_constructor_exists():
    assert callable(whileLanguage::While.__init__)


def test_whilelanguage::while_constructor_args():
    sig = inspect.signature(whileLanguage::While.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::for_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::For)


def test_whilelanguage::for_constructor_exists():
    assert callable(whileLanguage::For.__init__)


def test_whilelanguage::for_constructor_args():
    sig = inspect.signature(whileLanguage::For.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::if_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::If)


def test_whilelanguage::if_constructor_exists():
    assert callable(whileLanguage::If.__init__)


def test_whilelanguage::if_constructor_args():
    sig = inspect.signature(whileLanguage::If.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::expr_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Expr)


def test_whilelanguage::expr_constructor_exists():
    assert callable(whileLanguage::Expr.__init__)


def test_whilelanguage::expr_constructor_args():
    sig = inspect.signature(whileLanguage::Expr.__init__)
    params = list(sig.parameters.keys())
    assert "ope" in params, "Missing parameter 'ope'"
    assert "valeur" in params, "Missing parameter 'valeur'"

def test_whilelanguage::expr_has_ope():
    assert hasattr(whileLanguage::Expr, "ope")
    descriptor = None
    for klass in whileLanguage::Expr.__mro__:
        if "ope" in klass.__dict__:
            descriptor = klass.__dict__["ope"]
            break
    assert isinstance(descriptor, property)

def test_whilelanguage::expr_has_valeur():
    assert hasattr(whileLanguage::Expr, "valeur")
    descriptor = None
    for klass in whileLanguage::Expr.__mro__:
        if "valeur" in klass.__dict__:
            descriptor = klass.__dict__["valeur"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage::affectation_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Affectation)


def test_whilelanguage::affectation_constructor_exists():
    assert callable(whileLanguage::Affectation.__init__)


def test_whilelanguage::affectation_constructor_args():
    sig = inspect.signature(whileLanguage::Affectation.__init__)
    params = list(sig.parameters.keys())
    assert "affectations" in params, "Missing parameter 'affectations'"

def test_whilelanguage::affectation_has_affectations():
    assert hasattr(whileLanguage::Affectation, "affectations")
    descriptor = None
    for klass in whileLanguage::Affectation.__mro__:
        if "affectations" in klass.__dict__:
            descriptor = klass.__dict__["affectations"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage::write_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Write)


def test_whilelanguage::write_constructor_exists():
    assert callable(whileLanguage::Write.__init__)


def test_whilelanguage::write_constructor_args():
    sig = inspect.signature(whileLanguage::Write.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilelanguage::write_has_variable():
    assert hasattr(whileLanguage::Write, "variable")
    descriptor = None
    for klass in whileLanguage::Write.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage::commands_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Commands)


def test_whilelanguage::commands_constructor_exists():
    assert callable(whileLanguage::Commands.__init__)


def test_whilelanguage::commands_constructor_args():
    sig = inspect.signature(whileLanguage::Commands.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::read_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Read)


def test_whilelanguage::read_constructor_exists():
    assert callable(whileLanguage::Read.__init__)


def test_whilelanguage::read_constructor_args():
    sig = inspect.signature(whileLanguage::Read.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilelanguage::read_has_variable():
    assert hasattr(whileLanguage::Read, "variable")
    descriptor = None
    for klass in whileLanguage::Read.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage::definition_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Definition)


def test_whilelanguage::definition_constructor_exists():
    assert callable(whileLanguage::Definition.__init__)


def test_whilelanguage::definition_constructor_args():
    sig = inspect.signature(whileLanguage::Definition.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::function_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Function)


def test_whilelanguage::function_constructor_exists():
    assert callable(whileLanguage::Function.__init__)


def test_whilelanguage::function_constructor_args():
    sig = inspect.signature(whileLanguage::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_whilelanguage::function_has_name():
    assert hasattr(whileLanguage::Function, "name")
    descriptor = None
    for klass in whileLanguage::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage::program_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Program)


def test_whilelanguage::program_constructor_exists():
    assert callable(whileLanguage::Program.__init__)


def test_whilelanguage::program_constructor_args():
    sig = inspect.signature(whileLanguage::Program.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::foreach_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Foreach)


def test_whilelanguage::foreach_constructor_exists():
    assert callable(whileLanguage::Foreach.__init__)


def test_whilelanguage::foreach_constructor_args():
    sig = inspect.signature(whileLanguage::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::eobject_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::EObject)


def test_whilelanguage::eobject_constructor_exists():
    assert callable(whileLanguage::EObject.__init__)


def test_whilelanguage::eobject_constructor_args():
    sig = inspect.signature(whileLanguage::EObject.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::command_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Command)


def test_whilelanguage::command_constructor_exists():
    assert callable(whileLanguage::Command.__init__)


def test_whilelanguage::command_constructor_args():
    sig = inspect.signature(whileLanguage::Command.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage::nop_is_not_abstract():
    assert not inspect.isabstract(whileLanguage::Nop)


def test_whilelanguage::nop_constructor_exists():
    assert callable(whileLanguage::Nop.__init__)


def test_whilelanguage::nop_constructor_args():
    sig = inspect.signature(whileLanguage::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_whilelanguage::nop_has_nop():
    assert hasattr(whileLanguage::Nop, "nop")
    descriptor = None
    for klass in whileLanguage::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
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
whileLanguage::Lexpr_strategy = st.builds(
    whileLanguage::Lexpr,
)
whileLanguage::While_strategy = st.builds(
    whileLanguage::While,
)
whileLanguage::For_strategy = st.builds(
    whileLanguage::For,
)
whileLanguage::If_strategy = st.builds(
    whileLanguage::If,
)
whileLanguage::Expr_strategy = st.builds(
    whileLanguage::Expr,
    ope=
        safe_text,
    valeur=
        safe_text
)
whileLanguage::Affectation_strategy = st.builds(
    whileLanguage::Affectation,
    affectations=
        safe_text
)
whileLanguage::Write_strategy = st.builds(
    whileLanguage::Write,
    variable=
        safe_text
)
whileLanguage::Commands_strategy = st.builds(
    whileLanguage::Commands,
)
whileLanguage::Read_strategy = st.builds(
    whileLanguage::Read,
    variable=
        safe_text
)
whileLanguage::Definition_strategy = st.builds(
    whileLanguage::Definition,
)
whileLanguage::Function_strategy = st.builds(
    whileLanguage::Function,
    name=
        safe_text
)
whileLanguage::Program_strategy = st.builds(
    whileLanguage::Program,
)
whileLanguage::Foreach_strategy = st.builds(
    whileLanguage::Foreach,
)
whileLanguage::EObject_strategy = st.builds(
    whileLanguage::EObject,
)
whileLanguage::Command_strategy = st.builds(
    whileLanguage::Command,
)
whileLanguage::Nop_strategy = st.builds(
    whileLanguage::Nop,
    nop=
        safe_text
)

@given(instance=whileLanguage::Lexpr_strategy)
@settings(max_examples=50)
def test_whilelanguage::lexpr_instantiation(instance):
    assert isinstance(instance, whileLanguage::Lexpr)

@given(instance=whileLanguage::While_strategy)
@settings(max_examples=50)
def test_whilelanguage::while_instantiation(instance):
    assert isinstance(instance, whileLanguage::While)

@given(instance=whileLanguage::For_strategy)
@settings(max_examples=50)
def test_whilelanguage::for_instantiation(instance):
    assert isinstance(instance, whileLanguage::For)

@given(instance=whileLanguage::If_strategy)
@settings(max_examples=50)
def test_whilelanguage::if_instantiation(instance):
    assert isinstance(instance, whileLanguage::If)

@given(instance=whileLanguage::Expr_strategy)
@settings(max_examples=50)
def test_whilelanguage::expr_instantiation(instance):
    assert isinstance(instance, whileLanguage::Expr)

@given(instance=whileLanguage::Expr_strategy)
def test_whilelanguage::expr_ope_type(instance):
    assert isinstance(instance.ope, str)


@given(instance=whileLanguage::Expr_strategy)
def test_whilelanguage::expr_ope_setter(instance):
    original = instance.ope
    instance.ope = original
    assert instance.ope == original

@given(instance=whileLanguage::Expr_strategy)
def test_whilelanguage::expr_valeur_type(instance):
    assert isinstance(instance.valeur, str)


@given(instance=whileLanguage::Expr_strategy)
def test_whilelanguage::expr_valeur_setter(instance):
    original = instance.valeur
    instance.valeur = original
    assert instance.valeur == original

@given(instance=whileLanguage::Affectation_strategy)
@settings(max_examples=50)
def test_whilelanguage::affectation_instantiation(instance):
    assert isinstance(instance, whileLanguage::Affectation)

@given(instance=whileLanguage::Affectation_strategy)
def test_whilelanguage::affectation_affectations_type(instance):
    assert isinstance(instance.affectations, str)


@given(instance=whileLanguage::Affectation_strategy)
def test_whilelanguage::affectation_affectations_setter(instance):
    original = instance.affectations
    instance.affectations = original
    assert instance.affectations == original

@given(instance=whileLanguage::Write_strategy)
@settings(max_examples=50)
def test_whilelanguage::write_instantiation(instance):
    assert isinstance(instance, whileLanguage::Write)

@given(instance=whileLanguage::Write_strategy)
def test_whilelanguage::write_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=whileLanguage::Write_strategy)
def test_whilelanguage::write_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileLanguage::Commands_strategy)
@settings(max_examples=50)
def test_whilelanguage::commands_instantiation(instance):
    assert isinstance(instance, whileLanguage::Commands)

@given(instance=whileLanguage::Read_strategy)
@settings(max_examples=50)
def test_whilelanguage::read_instantiation(instance):
    assert isinstance(instance, whileLanguage::Read)

@given(instance=whileLanguage::Read_strategy)
def test_whilelanguage::read_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=whileLanguage::Read_strategy)
def test_whilelanguage::read_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileLanguage::Definition_strategy)
@settings(max_examples=50)
def test_whilelanguage::definition_instantiation(instance):
    assert isinstance(instance, whileLanguage::Definition)

@given(instance=whileLanguage::Function_strategy)
@settings(max_examples=50)
def test_whilelanguage::function_instantiation(instance):
    assert isinstance(instance, whileLanguage::Function)

@given(instance=whileLanguage::Function_strategy)
def test_whilelanguage::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=whileLanguage::Function_strategy)
def test_whilelanguage::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=whileLanguage::Program_strategy)
@settings(max_examples=50)
def test_whilelanguage::program_instantiation(instance):
    assert isinstance(instance, whileLanguage::Program)

@given(instance=whileLanguage::Foreach_strategy)
@settings(max_examples=50)
def test_whilelanguage::foreach_instantiation(instance):
    assert isinstance(instance, whileLanguage::Foreach)

@given(instance=whileLanguage::EObject_strategy)
@settings(max_examples=50)
def test_whilelanguage::eobject_instantiation(instance):
    assert isinstance(instance, whileLanguage::EObject)

@given(instance=whileLanguage::Command_strategy)
@settings(max_examples=50)
def test_whilelanguage::command_instantiation(instance):
    assert isinstance(instance, whileLanguage::Command)

@given(instance=whileLanguage::Nop_strategy)
@settings(max_examples=50)
def test_whilelanguage::nop_instantiation(instance):
    assert isinstance(instance, whileLanguage::Nop)

@given(instance=whileLanguage::Nop_strategy)
def test_whilelanguage::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=whileLanguage::Nop_strategy)
def test_whilelanguage::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original
