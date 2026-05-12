import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    whileLanguage_Lexpr,
    whileLanguage_While,
    whileLanguage_For,
    whileLanguage_If,
    whileLanguage_Expr,
    whileLanguage_Affectation,
    whileLanguage_Write,
    whileLanguage_Commands,
    whileLanguage_Read,
    whileLanguage_Definition,
    whileLanguage_Function,
    whileLanguage_Program,
    whileLanguage_Foreach,
    whileLanguage_EObject,
    whileLanguage_Command,
    whileLanguage_Nop,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_whilelanguage_lexpr_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Lexpr)


def test_whilelanguage_lexpr_constructor_exists():
    assert callable(whileLanguage_Lexpr.__init__)


def test_whilelanguage_lexpr_constructor_args():
    sig = inspect.signature(whileLanguage_Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_while_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_While)


def test_whilelanguage_while_constructor_exists():
    assert callable(whileLanguage_While.__init__)


def test_whilelanguage_while_constructor_args():
    sig = inspect.signature(whileLanguage_While.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_for_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_For)


def test_whilelanguage_for_constructor_exists():
    assert callable(whileLanguage_For.__init__)


def test_whilelanguage_for_constructor_args():
    sig = inspect.signature(whileLanguage_For.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_if_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_If)


def test_whilelanguage_if_constructor_exists():
    assert callable(whileLanguage_If.__init__)


def test_whilelanguage_if_constructor_args():
    sig = inspect.signature(whileLanguage_If.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_expr_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Expr)


def test_whilelanguage_expr_constructor_exists():
    assert callable(whileLanguage_Expr.__init__)


def test_whilelanguage_expr_constructor_args():
    sig = inspect.signature(whileLanguage_Expr.__init__)
    params = list(sig.parameters.keys())
    assert "valeur" in params, "Missing parameter 'valeur'"
    assert "ope" in params, "Missing parameter 'ope'"

def test_whilelanguage_expr_has_valeur():
    assert hasattr(whileLanguage_Expr, "valeur")
    descriptor = None
    for klass in whileLanguage_Expr.__mro__:
        if "valeur" in klass.__dict__:
            descriptor = klass.__dict__["valeur"]
            break
    assert isinstance(descriptor, property)

def test_whilelanguage_expr_has_ope():
    assert hasattr(whileLanguage_Expr, "ope")
    descriptor = None
    for klass in whileLanguage_Expr.__mro__:
        if "ope" in klass.__dict__:
            descriptor = klass.__dict__["ope"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage_affectation_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Affectation)


def test_whilelanguage_affectation_constructor_exists():
    assert callable(whileLanguage_Affectation.__init__)


def test_whilelanguage_affectation_constructor_args():
    sig = inspect.signature(whileLanguage_Affectation.__init__)
    params = list(sig.parameters.keys())
    assert "affectations" in params, "Missing parameter 'affectations'"

def test_whilelanguage_affectation_has_affectations():
    assert hasattr(whileLanguage_Affectation, "affectations")
    descriptor = None
    for klass in whileLanguage_Affectation.__mro__:
        if "affectations" in klass.__dict__:
            descriptor = klass.__dict__["affectations"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage_write_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Write)


def test_whilelanguage_write_constructor_exists():
    assert callable(whileLanguage_Write.__init__)


def test_whilelanguage_write_constructor_args():
    sig = inspect.signature(whileLanguage_Write.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilelanguage_write_has_variable():
    assert hasattr(whileLanguage_Write, "variable")
    descriptor = None
    for klass in whileLanguage_Write.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage_commands_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Commands)


def test_whilelanguage_commands_constructor_exists():
    assert callable(whileLanguage_Commands.__init__)


def test_whilelanguage_commands_constructor_args():
    sig = inspect.signature(whileLanguage_Commands.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_read_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Read)


def test_whilelanguage_read_constructor_exists():
    assert callable(whileLanguage_Read.__init__)


def test_whilelanguage_read_constructor_args():
    sig = inspect.signature(whileLanguage_Read.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilelanguage_read_has_variable():
    assert hasattr(whileLanguage_Read, "variable")
    descriptor = None
    for klass in whileLanguage_Read.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage_definition_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Definition)


def test_whilelanguage_definition_constructor_exists():
    assert callable(whileLanguage_Definition.__init__)


def test_whilelanguage_definition_constructor_args():
    sig = inspect.signature(whileLanguage_Definition.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_function_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Function)


def test_whilelanguage_function_constructor_exists():
    assert callable(whileLanguage_Function.__init__)


def test_whilelanguage_function_constructor_args():
    sig = inspect.signature(whileLanguage_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_whilelanguage_function_has_name():
    assert hasattr(whileLanguage_Function, "name")
    descriptor = None
    for klass in whileLanguage_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_whilelanguage_program_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Program)


def test_whilelanguage_program_constructor_exists():
    assert callable(whileLanguage_Program.__init__)


def test_whilelanguage_program_constructor_args():
    sig = inspect.signature(whileLanguage_Program.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_foreach_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Foreach)


def test_whilelanguage_foreach_constructor_exists():
    assert callable(whileLanguage_Foreach.__init__)


def test_whilelanguage_foreach_constructor_args():
    sig = inspect.signature(whileLanguage_Foreach.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_eobject_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_EObject)


def test_whilelanguage_eobject_constructor_exists():
    assert callable(whileLanguage_EObject.__init__)


def test_whilelanguage_eobject_constructor_args():
    sig = inspect.signature(whileLanguage_EObject.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_command_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Command)


def test_whilelanguage_command_constructor_exists():
    assert callable(whileLanguage_Command.__init__)


def test_whilelanguage_command_constructor_args():
    sig = inspect.signature(whileLanguage_Command.__init__)
    params = list(sig.parameters.keys())



def test_whilelanguage_nop_is_not_abstract():
    assert not inspect.isabstract(whileLanguage_Nop)


def test_whilelanguage_nop_constructor_exists():
    assert callable(whileLanguage_Nop.__init__)


def test_whilelanguage_nop_constructor_args():
    sig = inspect.signature(whileLanguage_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_whilelanguage_nop_has_nop():
    assert hasattr(whileLanguage_Nop, "nop")
    descriptor = None
    for klass in whileLanguage_Nop.__mro__:
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
whileLanguage_Lexpr_strategy = st.builds(
    whileLanguage_Lexpr,
)
whileLanguage_While_strategy = st.builds(
    whileLanguage_While,
)
whileLanguage_For_strategy = st.builds(
    whileLanguage_For,
)
whileLanguage_If_strategy = st.builds(
    whileLanguage_If,
)
whileLanguage_Expr_strategy = st.builds(
    whileLanguage_Expr,
    valeur=
        safe_text,
    ope=
        safe_text
)
whileLanguage_Affectation_strategy = st.builds(
    whileLanguage_Affectation,
    affectations=
        safe_text
)
whileLanguage_Write_strategy = st.builds(
    whileLanguage_Write,
    variable=
        safe_text
)
whileLanguage_Commands_strategy = st.builds(
    whileLanguage_Commands,
)
whileLanguage_Read_strategy = st.builds(
    whileLanguage_Read,
    variable=
        safe_text
)
whileLanguage_Definition_strategy = st.builds(
    whileLanguage_Definition,
)
whileLanguage_Function_strategy = st.builds(
    whileLanguage_Function,
    name=
        safe_text
)
whileLanguage_Program_strategy = st.builds(
    whileLanguage_Program,
)
whileLanguage_Foreach_strategy = st.builds(
    whileLanguage_Foreach,
)
whileLanguage_EObject_strategy = st.builds(
    whileLanguage_EObject,
)
whileLanguage_Command_strategy = st.builds(
    whileLanguage_Command,
)
whileLanguage_Nop_strategy = st.builds(
    whileLanguage_Nop,
    nop=
        safe_text
)

@given(instance=whileLanguage_Lexpr_strategy)
@settings(max_examples=50)
def test_whilelanguage_lexpr_instantiation(instance):
    assert isinstance(instance, whileLanguage_Lexpr)

@given(instance=whileLanguage_While_strategy)
@settings(max_examples=50)
def test_whilelanguage_while_instantiation(instance):
    assert isinstance(instance, whileLanguage_While)

@given(instance=whileLanguage_For_strategy)
@settings(max_examples=50)
def test_whilelanguage_for_instantiation(instance):
    assert isinstance(instance, whileLanguage_For)

@given(instance=whileLanguage_If_strategy)
@settings(max_examples=50)
def test_whilelanguage_if_instantiation(instance):
    assert isinstance(instance, whileLanguage_If)

@given(instance=whileLanguage_Expr_strategy)
@settings(max_examples=50)
def test_whilelanguage_expr_instantiation(instance):
    assert isinstance(instance, whileLanguage_Expr)



@given(instance=whileLanguage_Expr_strategy)
def test_whilelanguage_expr_valeur_setter(instance):
    original = instance.valeur
    instance.valeur = original
    assert instance.valeur == original



@given(instance=whileLanguage_Expr_strategy)
def test_whilelanguage_expr_ope_setter(instance):
    original = instance.ope
    instance.ope = original
    assert instance.ope == original

@given(instance=whileLanguage_Affectation_strategy)
@settings(max_examples=50)
def test_whilelanguage_affectation_instantiation(instance):
    assert isinstance(instance, whileLanguage_Affectation)



@given(instance=whileLanguage_Affectation_strategy)
def test_whilelanguage_affectation_affectations_setter(instance):
    original = instance.affectations
    instance.affectations = original
    assert instance.affectations == original

@given(instance=whileLanguage_Write_strategy)
@settings(max_examples=50)
def test_whilelanguage_write_instantiation(instance):
    assert isinstance(instance, whileLanguage_Write)



@given(instance=whileLanguage_Write_strategy)
def test_whilelanguage_write_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileLanguage_Commands_strategy)
@settings(max_examples=50)
def test_whilelanguage_commands_instantiation(instance):
    assert isinstance(instance, whileLanguage_Commands)

@given(instance=whileLanguage_Read_strategy)
@settings(max_examples=50)
def test_whilelanguage_read_instantiation(instance):
    assert isinstance(instance, whileLanguage_Read)



@given(instance=whileLanguage_Read_strategy)
def test_whilelanguage_read_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileLanguage_Definition_strategy)
@settings(max_examples=50)
def test_whilelanguage_definition_instantiation(instance):
    assert isinstance(instance, whileLanguage_Definition)

@given(instance=whileLanguage_Function_strategy)
@settings(max_examples=50)
def test_whilelanguage_function_instantiation(instance):
    assert isinstance(instance, whileLanguage_Function)



@given(instance=whileLanguage_Function_strategy)
def test_whilelanguage_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=whileLanguage_Program_strategy)
@settings(max_examples=50)
def test_whilelanguage_program_instantiation(instance):
    assert isinstance(instance, whileLanguage_Program)

@given(instance=whileLanguage_Foreach_strategy)
@settings(max_examples=50)
def test_whilelanguage_foreach_instantiation(instance):
    assert isinstance(instance, whileLanguage_Foreach)

@given(instance=whileLanguage_EObject_strategy)
@settings(max_examples=50)
def test_whilelanguage_eobject_instantiation(instance):
    assert isinstance(instance, whileLanguage_EObject)

@given(instance=whileLanguage_Command_strategy)
@settings(max_examples=50)
def test_whilelanguage_command_instantiation(instance):
    assert isinstance(instance, whileLanguage_Command)

@given(instance=whileLanguage_Nop_strategy)
@settings(max_examples=50)
def test_whilelanguage_nop_instantiation(instance):
    assert isinstance(instance, whileLanguage_Nop)



@given(instance=whileLanguage_Nop_strategy)
def test_whilelanguage_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original
