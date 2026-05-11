import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Lexpr,
    myDsl::EObject,
    myDsl::Eq,
    myDsl::Not,
    myDsl::Or,
    myDsl::ExprTerm,
    myDsl::And,
    myDsl::ExprSimple,
    myDsl::Expr,
    myDsl::Exprs,
    myDsl::Vars,
    myDsl::Command,
    myDsl::Output,
    myDsl::Commands,
    myDsl::Input,
    myDsl::Definiton,
    myDsl::Function,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::lexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Lexpr)


def test_mydsl::lexpr_constructor_exists():
    assert callable(myDsl::Lexpr.__init__)


def test_mydsl::lexpr_constructor_args():
    sig = inspect.signature(myDsl::Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::EObject)


def test_mydsl::eobject_constructor_exists():
    assert callable(myDsl::EObject.__init__)


def test_mydsl::eobject_constructor_args():
    sig = inspect.signature(myDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::eq_is_not_abstract():
    assert not inspect.isabstract(myDsl::Eq)


def test_mydsl::eq_constructor_exists():
    assert callable(myDsl::Eq.__init__)


def test_mydsl::eq_constructor_args():
    sig = inspect.signature(myDsl::Eq.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::not_is_not_abstract():
    assert not inspect.isabstract(myDsl::Not)


def test_mydsl::not_constructor_exists():
    assert callable(myDsl::Not.__init__)


def test_mydsl::not_constructor_args():
    sig = inspect.signature(myDsl::Not.__init__)
    params = list(sig.parameters.keys())
    assert "non" in params, "Missing parameter 'non'"

def test_mydsl::not_has_non():
    assert hasattr(myDsl::Not, "non")
    descriptor = None
    for klass in myDsl::Not.__mro__:
        if "non" in klass.__dict__:
            descriptor = klass.__dict__["non"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::or_is_not_abstract():
    assert not inspect.isabstract(myDsl::Or)


def test_mydsl::or_constructor_exists():
    assert callable(myDsl::Or.__init__)


def test_mydsl::or_constructor_args():
    sig = inspect.signature(myDsl::Or.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprterm_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprTerm)


def test_mydsl::exprterm_constructor_exists():
    assert callable(myDsl::ExprTerm.__init__)


def test_mydsl::exprterm_constructor_args():
    sig = inspect.signature(myDsl::ExprTerm.__init__)
    params = list(sig.parameters.keys())
    assert "termSym" in params, "Missing parameter 'termSym'"
    assert "termVar" in params, "Missing parameter 'termVar'"

def test_mydsl::exprterm_has_termSym():
    assert hasattr(myDsl::ExprTerm, "termSym")
    descriptor = None
    for klass in myDsl::ExprTerm.__mro__:
        if "termSym" in klass.__dict__:
            descriptor = klass.__dict__["termSym"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::exprterm_has_termVar():
    assert hasattr(myDsl::ExprTerm, "termVar")
    descriptor = None
    for klass in myDsl::ExprTerm.__mro__:
        if "termVar" in klass.__dict__:
            descriptor = klass.__dict__["termVar"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::and_is_not_abstract():
    assert not inspect.isabstract(myDsl::And)


def test_mydsl::and_constructor_exists():
    assert callable(myDsl::And.__init__)


def test_mydsl::and_constructor_args():
    sig = inspect.signature(myDsl::And.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprSimple)


def test_mydsl::exprsimple_constructor_exists():
    assert callable(myDsl::ExprSimple.__init__)


def test_mydsl::exprsimple_constructor_args():
    sig = inspect.signature(myDsl::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "mot" in params, "Missing parameter 'mot'"

def test_mydsl::exprsimple_has_mot():
    assert hasattr(myDsl::ExprSimple, "mot")
    descriptor = None
    for klass in myDsl::ExprSimple.__mro__:
        if "mot" in klass.__dict__:
            descriptor = klass.__dict__["mot"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expr)


def test_mydsl::expr_constructor_exists():
    assert callable(myDsl::Expr.__init__)


def test_mydsl::expr_constructor_args():
    sig = inspect.signature(myDsl::Expr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprs_is_not_abstract():
    assert not inspect.isabstract(myDsl::Exprs)


def test_mydsl::exprs_constructor_exists():
    assert callable(myDsl::Exprs.__init__)


def test_mydsl::exprs_constructor_args():
    sig = inspect.signature(myDsl::Exprs.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::vars_is_not_abstract():
    assert not inspect.isabstract(myDsl::Vars)


def test_mydsl::vars_constructor_exists():
    assert callable(myDsl::Vars.__init__)


def test_mydsl::vars_constructor_args():
    sig = inspect.signature(myDsl::Vars.__init__)
    params = list(sig.parameters.keys())
    assert "v2" in params, "Missing parameter 'v2'"
    assert "v1" in params, "Missing parameter 'v1'"

def test_mydsl::vars_has_v2():
    assert hasattr(myDsl::Vars, "v2")
    descriptor = None
    for klass in myDsl::Vars.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::vars_has_v1():
    assert hasattr(myDsl::Vars, "v1")
    descriptor = None
    for klass in myDsl::Vars.__mro__:
        if "v1" in klass.__dict__:
            descriptor = klass.__dict__["v1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::command_is_not_abstract():
    assert not inspect.isabstract(myDsl::Command)


def test_mydsl::command_constructor_exists():
    assert callable(myDsl::Command.__init__)


def test_mydsl::command_constructor_args():
    sig = inspect.signature(myDsl::Command.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_mydsl::command_has_nom():
    assert hasattr(myDsl::Command, "nom")
    descriptor = None
    for klass in myDsl::Command.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::output_is_not_abstract():
    assert not inspect.isabstract(myDsl::Output)


def test_mydsl::output_constructor_exists():
    assert callable(myDsl::Output.__init__)


def test_mydsl::output_constructor_args():
    sig = inspect.signature(myDsl::Output.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "v2" in params, "Missing parameter 'v2'"

def test_mydsl::output_has_v():
    assert hasattr(myDsl::Output, "v")
    descriptor = None
    for klass in myDsl::Output.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::output_has_v2():
    assert hasattr(myDsl::Output, "v2")
    descriptor = None
    for klass in myDsl::Output.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::commands_is_not_abstract():
    assert not inspect.isabstract(myDsl::Commands)


def test_mydsl::commands_constructor_exists():
    assert callable(myDsl::Commands.__init__)


def test_mydsl::commands_constructor_args():
    sig = inspect.signature(myDsl::Commands.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::input_is_not_abstract():
    assert not inspect.isabstract(myDsl::Input)


def test_mydsl::input_constructor_exists():
    assert callable(myDsl::Input.__init__)


def test_mydsl::input_constructor_args():
    sig = inspect.signature(myDsl::Input.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "v2" in params, "Missing parameter 'v2'"

def test_mydsl::input_has_v():
    assert hasattr(myDsl::Input, "v")
    descriptor = None
    for klass in myDsl::Input.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::input_has_v2():
    assert hasattr(myDsl::Input, "v2")
    descriptor = None
    for klass in myDsl::Input.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::definiton_is_not_abstract():
    assert not inspect.isabstract(myDsl::Definiton)


def test_mydsl::definiton_constructor_exists():
    assert callable(myDsl::Definiton.__init__)


def test_mydsl::definiton_constructor_args():
    sig = inspect.signature(myDsl::Definiton.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::function_is_not_abstract():
    assert not inspect.isabstract(myDsl::Function)


def test_mydsl::function_constructor_exists():
    assert callable(myDsl::Function.__init__)


def test_mydsl::function_constructor_args():
    sig = inspect.signature(myDsl::Function.__init__)
    params = list(sig.parameters.keys())
    assert "funName" in params, "Missing parameter 'funName'"

def test_mydsl::function_has_funName():
    assert hasattr(myDsl::Function, "funName")
    descriptor = None
    for klass in myDsl::Function.__mro__:
        if "funName" in klass.__dict__:
            descriptor = klass.__dict__["funName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::Lexpr_strategy = st.builds(
    myDsl::Lexpr,
)
myDsl::EObject_strategy = st.builds(
    myDsl::EObject,
)
myDsl::Eq_strategy = st.builds(
    myDsl::Eq,
)
myDsl::Not_strategy = st.builds(
    myDsl::Not,
    non=
        safe_text
)
myDsl::Or_strategy = st.builds(
    myDsl::Or,
)
myDsl::ExprTerm_strategy = st.builds(
    myDsl::ExprTerm,
    termSym=
        safe_text,
    termVar=
        safe_text
)
myDsl::And_strategy = st.builds(
    myDsl::And,
)
myDsl::ExprSimple_strategy = st.builds(
    myDsl::ExprSimple,
    mot=
        safe_text
)
myDsl::Expr_strategy = st.builds(
    myDsl::Expr,
)
myDsl::Exprs_strategy = st.builds(
    myDsl::Exprs,
)
myDsl::Vars_strategy = st.builds(
    myDsl::Vars,
    v2=
        safe_text,
    v1=
        safe_text
)
myDsl::Command_strategy = st.builds(
    myDsl::Command,
    nom=
        safe_text
)
myDsl::Output_strategy = st.builds(
    myDsl::Output,
    v=
        safe_text,
    v2=
        safe_text
)
myDsl::Commands_strategy = st.builds(
    myDsl::Commands,
)
myDsl::Input_strategy = st.builds(
    myDsl::Input,
    v=
        safe_text,
    v2=
        safe_text
)
myDsl::Definiton_strategy = st.builds(
    myDsl::Definiton,
)
myDsl::Function_strategy = st.builds(
    myDsl::Function,
    funName=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::Lexpr_strategy)
@settings(max_examples=50)
def test_mydsl::lexpr_instantiation(instance):
    assert isinstance(instance, myDsl::Lexpr)

@given(instance=myDsl::EObject_strategy)
@settings(max_examples=50)
def test_mydsl::eobject_instantiation(instance):
    assert isinstance(instance, myDsl::EObject)

@given(instance=myDsl::Eq_strategy)
@settings(max_examples=50)
def test_mydsl::eq_instantiation(instance):
    assert isinstance(instance, myDsl::Eq)

@given(instance=myDsl::Not_strategy)
@settings(max_examples=50)
def test_mydsl::not_instantiation(instance):
    assert isinstance(instance, myDsl::Not)

@given(instance=myDsl::Not_strategy)
def test_mydsl::not_non_type(instance):
    assert isinstance(instance.non, str)


@given(instance=myDsl::Not_strategy)
def test_mydsl::not_non_setter(instance):
    original = instance.non
    instance.non = original
    assert instance.non == original

@given(instance=myDsl::Or_strategy)
@settings(max_examples=50)
def test_mydsl::or_instantiation(instance):
    assert isinstance(instance, myDsl::Or)

@given(instance=myDsl::ExprTerm_strategy)
@settings(max_examples=50)
def test_mydsl::exprterm_instantiation(instance):
    assert isinstance(instance, myDsl::ExprTerm)

@given(instance=myDsl::ExprTerm_strategy)
def test_mydsl::exprterm_termSym_type(instance):
    assert isinstance(instance.termSym, str)


@given(instance=myDsl::ExprTerm_strategy)
def test_mydsl::exprterm_termSym_setter(instance):
    original = instance.termSym
    instance.termSym = original
    assert instance.termSym == original

@given(instance=myDsl::ExprTerm_strategy)
def test_mydsl::exprterm_termVar_type(instance):
    assert isinstance(instance.termVar, str)


@given(instance=myDsl::ExprTerm_strategy)
def test_mydsl::exprterm_termVar_setter(instance):
    original = instance.termVar
    instance.termVar = original
    assert instance.termVar == original

@given(instance=myDsl::And_strategy)
@settings(max_examples=50)
def test_mydsl::and_instantiation(instance):
    assert isinstance(instance, myDsl::And)

@given(instance=myDsl::ExprSimple_strategy)
@settings(max_examples=50)
def test_mydsl::exprsimple_instantiation(instance):
    assert isinstance(instance, myDsl::ExprSimple)

@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_mot_type(instance):
    assert isinstance(instance.mot, str)


@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_mot_setter(instance):
    original = instance.mot
    instance.mot = original
    assert instance.mot == original

@given(instance=myDsl::Expr_strategy)
@settings(max_examples=50)
def test_mydsl::expr_instantiation(instance):
    assert isinstance(instance, myDsl::Expr)

@given(instance=myDsl::Exprs_strategy)
@settings(max_examples=50)
def test_mydsl::exprs_instantiation(instance):
    assert isinstance(instance, myDsl::Exprs)

@given(instance=myDsl::Vars_strategy)
@settings(max_examples=50)
def test_mydsl::vars_instantiation(instance):
    assert isinstance(instance, myDsl::Vars)

@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_v2_type(instance):
    assert isinstance(instance.v2, str)


@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_v1_type(instance):
    assert isinstance(instance.v1, str)


@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_v1_setter(instance):
    original = instance.v1
    instance.v1 = original
    assert instance.v1 == original

@given(instance=myDsl::Command_strategy)
@settings(max_examples=50)
def test_mydsl::command_instantiation(instance):
    assert isinstance(instance, myDsl::Command)

@given(instance=myDsl::Command_strategy)
def test_mydsl::command_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=myDsl::Command_strategy)
def test_mydsl::command_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=myDsl::Output_strategy)
@settings(max_examples=50)
def test_mydsl::output_instantiation(instance):
    assert isinstance(instance, myDsl::Output)

@given(instance=myDsl::Output_strategy)
def test_mydsl::output_v_type(instance):
    assert isinstance(instance.v, str)


@given(instance=myDsl::Output_strategy)
def test_mydsl::output_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=myDsl::Output_strategy)
def test_mydsl::output_v2_type(instance):
    assert isinstance(instance.v2, str)


@given(instance=myDsl::Output_strategy)
def test_mydsl::output_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=myDsl::Commands_strategy)
@settings(max_examples=50)
def test_mydsl::commands_instantiation(instance):
    assert isinstance(instance, myDsl::Commands)

@given(instance=myDsl::Input_strategy)
@settings(max_examples=50)
def test_mydsl::input_instantiation(instance):
    assert isinstance(instance, myDsl::Input)

@given(instance=myDsl::Input_strategy)
def test_mydsl::input_v_type(instance):
    assert isinstance(instance.v, str)


@given(instance=myDsl::Input_strategy)
def test_mydsl::input_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=myDsl::Input_strategy)
def test_mydsl::input_v2_type(instance):
    assert isinstance(instance.v2, str)


@given(instance=myDsl::Input_strategy)
def test_mydsl::input_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=myDsl::Definiton_strategy)
@settings(max_examples=50)
def test_mydsl::definiton_instantiation(instance):
    assert isinstance(instance, myDsl::Definiton)

@given(instance=myDsl::Function_strategy)
@settings(max_examples=50)
def test_mydsl::function_instantiation(instance):
    assert isinstance(instance, myDsl::Function)

@given(instance=myDsl::Function_strategy)
def test_mydsl::function_funName_type(instance):
    assert isinstance(instance.funName, str)


@given(instance=myDsl::Function_strategy)
def test_mydsl::function_funName_setter(instance):
    original = instance.funName
    instance.funName = original
    assert instance.funName == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
