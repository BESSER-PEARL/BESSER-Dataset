import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Lexpr,
    myDsl_EObject,
    myDsl_Eq,
    myDsl_Not,
    myDsl_Or,
    myDsl_ExprTerm,
    myDsl_And,
    myDsl_ExprSimple,
    myDsl_Expr,
    myDsl_Exprs,
    myDsl_Vars,
    myDsl_Command,
    myDsl_Output,
    myDsl_Commands,
    myDsl_Input,
    myDsl_Definiton,
    myDsl_Function,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_lexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Lexpr)


def test_mydsl_lexpr_constructor_exists():
    assert callable(myDsl_Lexpr.__init__)


def test_mydsl_lexpr_constructor_args():
    sig = inspect.signature(myDsl_Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_EObject)


def test_mydsl_eobject_constructor_exists():
    assert callable(myDsl_EObject.__init__)


def test_mydsl_eobject_constructor_args():
    sig = inspect.signature(myDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_eq_is_not_abstract():
    assert not inspect.isabstract(myDsl_Eq)


def test_mydsl_eq_constructor_exists():
    assert callable(myDsl_Eq.__init__)


def test_mydsl_eq_constructor_args():
    sig = inspect.signature(myDsl_Eq.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_not_is_not_abstract():
    assert not inspect.isabstract(myDsl_Not)


def test_mydsl_not_constructor_exists():
    assert callable(myDsl_Not.__init__)


def test_mydsl_not_constructor_args():
    sig = inspect.signature(myDsl_Not.__init__)
    params = list(sig.parameters.keys())
    assert "non" in params, "Missing parameter 'non'"

def test_mydsl_not_has_non():
    assert hasattr(myDsl_Not, "non")
    descriptor = None
    for klass in myDsl_Not.__mro__:
        if "non" in klass.__dict__:
            descriptor = klass.__dict__["non"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_or_is_not_abstract():
    assert not inspect.isabstract(myDsl_Or)


def test_mydsl_or_constructor_exists():
    assert callable(myDsl_Or.__init__)


def test_mydsl_or_constructor_args():
    sig = inspect.signature(myDsl_Or.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprterm_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprTerm)


def test_mydsl_exprterm_constructor_exists():
    assert callable(myDsl_ExprTerm.__init__)


def test_mydsl_exprterm_constructor_args():
    sig = inspect.signature(myDsl_ExprTerm.__init__)
    params = list(sig.parameters.keys())
    assert "termVar" in params, "Missing parameter 'termVar'"
    assert "termSym" in params, "Missing parameter 'termSym'"

def test_mydsl_exprterm_has_termVar():
    assert hasattr(myDsl_ExprTerm, "termVar")
    descriptor = None
    for klass in myDsl_ExprTerm.__mro__:
        if "termVar" in klass.__dict__:
            descriptor = klass.__dict__["termVar"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_exprterm_has_termSym():
    assert hasattr(myDsl_ExprTerm, "termSym")
    descriptor = None
    for klass in myDsl_ExprTerm.__mro__:
        if "termSym" in klass.__dict__:
            descriptor = klass.__dict__["termSym"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_and_is_not_abstract():
    assert not inspect.isabstract(myDsl_And)


def test_mydsl_and_constructor_exists():
    assert callable(myDsl_And.__init__)


def test_mydsl_and_constructor_args():
    sig = inspect.signature(myDsl_And.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprSimple)


def test_mydsl_exprsimple_constructor_exists():
    assert callable(myDsl_ExprSimple.__init__)


def test_mydsl_exprsimple_constructor_args():
    sig = inspect.signature(myDsl_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "mot" in params, "Missing parameter 'mot'"

def test_mydsl_exprsimple_has_mot():
    assert hasattr(myDsl_ExprSimple, "mot")
    descriptor = None
    for klass in myDsl_ExprSimple.__mro__:
        if "mot" in klass.__dict__:
            descriptor = klass.__dict__["mot"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expr)


def test_mydsl_expr_constructor_exists():
    assert callable(myDsl_Expr.__init__)


def test_mydsl_expr_constructor_args():
    sig = inspect.signature(myDsl_Expr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprs_is_not_abstract():
    assert not inspect.isabstract(myDsl_Exprs)


def test_mydsl_exprs_constructor_exists():
    assert callable(myDsl_Exprs.__init__)


def test_mydsl_exprs_constructor_args():
    sig = inspect.signature(myDsl_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_vars_is_not_abstract():
    assert not inspect.isabstract(myDsl_Vars)


def test_mydsl_vars_constructor_exists():
    assert callable(myDsl_Vars.__init__)


def test_mydsl_vars_constructor_args():
    sig = inspect.signature(myDsl_Vars.__init__)
    params = list(sig.parameters.keys())
    assert "v1" in params, "Missing parameter 'v1'"
    assert "v2" in params, "Missing parameter 'v2'"

def test_mydsl_vars_has_v1():
    assert hasattr(myDsl_Vars, "v1")
    descriptor = None
    for klass in myDsl_Vars.__mro__:
        if "v1" in klass.__dict__:
            descriptor = klass.__dict__["v1"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_vars_has_v2():
    assert hasattr(myDsl_Vars, "v2")
    descriptor = None
    for klass in myDsl_Vars.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_command_is_not_abstract():
    assert not inspect.isabstract(myDsl_Command)


def test_mydsl_command_constructor_exists():
    assert callable(myDsl_Command.__init__)


def test_mydsl_command_constructor_args():
    sig = inspect.signature(myDsl_Command.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_mydsl_command_has_nom():
    assert hasattr(myDsl_Command, "nom")
    descriptor = None
    for klass in myDsl_Command.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_output_is_not_abstract():
    assert not inspect.isabstract(myDsl_Output)


def test_mydsl_output_constructor_exists():
    assert callable(myDsl_Output.__init__)


def test_mydsl_output_constructor_args():
    sig = inspect.signature(myDsl_Output.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "v2" in params, "Missing parameter 'v2'"

def test_mydsl_output_has_v():
    assert hasattr(myDsl_Output, "v")
    descriptor = None
    for klass in myDsl_Output.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_output_has_v2():
    assert hasattr(myDsl_Output, "v2")
    descriptor = None
    for klass in myDsl_Output.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_commands_is_not_abstract():
    assert not inspect.isabstract(myDsl_Commands)


def test_mydsl_commands_constructor_exists():
    assert callable(myDsl_Commands.__init__)


def test_mydsl_commands_constructor_args():
    sig = inspect.signature(myDsl_Commands.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_input_is_not_abstract():
    assert not inspect.isabstract(myDsl_Input)


def test_mydsl_input_constructor_exists():
    assert callable(myDsl_Input.__init__)


def test_mydsl_input_constructor_args():
    sig = inspect.signature(myDsl_Input.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "v2" in params, "Missing parameter 'v2'"

def test_mydsl_input_has_v():
    assert hasattr(myDsl_Input, "v")
    descriptor = None
    for klass in myDsl_Input.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_input_has_v2():
    assert hasattr(myDsl_Input, "v2")
    descriptor = None
    for klass in myDsl_Input.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_definiton_is_not_abstract():
    assert not inspect.isabstract(myDsl_Definiton)


def test_mydsl_definiton_constructor_exists():
    assert callable(myDsl_Definiton.__init__)


def test_mydsl_definiton_constructor_args():
    sig = inspect.signature(myDsl_Definiton.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_function_is_not_abstract():
    assert not inspect.isabstract(myDsl_Function)


def test_mydsl_function_constructor_exists():
    assert callable(myDsl_Function.__init__)


def test_mydsl_function_constructor_args():
    sig = inspect.signature(myDsl_Function.__init__)
    params = list(sig.parameters.keys())
    assert "funName" in params, "Missing parameter 'funName'"

def test_mydsl_function_has_funName():
    assert hasattr(myDsl_Function, "funName")
    descriptor = None
    for klass in myDsl_Function.__mro__:
        if "funName" in klass.__dict__:
            descriptor = klass.__dict__["funName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
myDsl_Lexpr_strategy = st.builds(
    myDsl_Lexpr,
)
myDsl_EObject_strategy = st.builds(
    myDsl_EObject,
)
myDsl_Eq_strategy = st.builds(
    myDsl_Eq,
)
myDsl_Not_strategy = st.builds(
    myDsl_Not,
    non=
        safe_text
)
myDsl_Or_strategy = st.builds(
    myDsl_Or,
)
myDsl_ExprTerm_strategy = st.builds(
    myDsl_ExprTerm,
    termVar=
        safe_text,
    termSym=
        safe_text
)
myDsl_And_strategy = st.builds(
    myDsl_And,
)
myDsl_ExprSimple_strategy = st.builds(
    myDsl_ExprSimple,
    mot=
        safe_text
)
myDsl_Expr_strategy = st.builds(
    myDsl_Expr,
)
myDsl_Exprs_strategy = st.builds(
    myDsl_Exprs,
)
myDsl_Vars_strategy = st.builds(
    myDsl_Vars,
    v1=
        safe_text,
    v2=
        safe_text
)
myDsl_Command_strategy = st.builds(
    myDsl_Command,
    nom=
        safe_text
)
myDsl_Output_strategy = st.builds(
    myDsl_Output,
    v=
        safe_text,
    v2=
        safe_text
)
myDsl_Commands_strategy = st.builds(
    myDsl_Commands,
)
myDsl_Input_strategy = st.builds(
    myDsl_Input,
    v=
        safe_text,
    v2=
        safe_text
)
myDsl_Definiton_strategy = st.builds(
    myDsl_Definiton,
)
myDsl_Function_strategy = st.builds(
    myDsl_Function,
    funName=
        safe_text
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=myDsl_Lexpr_strategy)
@settings(max_examples=50)
def test_mydsl_lexpr_instantiation(instance):
    assert isinstance(instance, myDsl_Lexpr)

@given(instance=myDsl_EObject_strategy)
@settings(max_examples=50)
def test_mydsl_eobject_instantiation(instance):
    assert isinstance(instance, myDsl_EObject)

@given(instance=myDsl_Eq_strategy)
@settings(max_examples=50)
def test_mydsl_eq_instantiation(instance):
    assert isinstance(instance, myDsl_Eq)

@given(instance=myDsl_Not_strategy)
@settings(max_examples=50)
def test_mydsl_not_instantiation(instance):
    assert isinstance(instance, myDsl_Not)



@given(instance=myDsl_Not_strategy)
def test_mydsl_not_non_setter(instance):
    original = instance.non
    instance.non = original
    assert instance.non == original

@given(instance=myDsl_Or_strategy)
@settings(max_examples=50)
def test_mydsl_or_instantiation(instance):
    assert isinstance(instance, myDsl_Or)

@given(instance=myDsl_ExprTerm_strategy)
@settings(max_examples=50)
def test_mydsl_exprterm_instantiation(instance):
    assert isinstance(instance, myDsl_ExprTerm)



@given(instance=myDsl_ExprTerm_strategy)
def test_mydsl_exprterm_termVar_setter(instance):
    original = instance.termVar
    instance.termVar = original
    assert instance.termVar == original



@given(instance=myDsl_ExprTerm_strategy)
def test_mydsl_exprterm_termSym_setter(instance):
    original = instance.termSym
    instance.termSym = original
    assert instance.termSym == original

@given(instance=myDsl_And_strategy)
@settings(max_examples=50)
def test_mydsl_and_instantiation(instance):
    assert isinstance(instance, myDsl_And)

@given(instance=myDsl_ExprSimple_strategy)
@settings(max_examples=50)
def test_mydsl_exprsimple_instantiation(instance):
    assert isinstance(instance, myDsl_ExprSimple)



@given(instance=myDsl_ExprSimple_strategy)
def test_mydsl_exprsimple_mot_setter(instance):
    original = instance.mot
    instance.mot = original
    assert instance.mot == original

@given(instance=myDsl_Expr_strategy)
@settings(max_examples=50)
def test_mydsl_expr_instantiation(instance):
    assert isinstance(instance, myDsl_Expr)

@given(instance=myDsl_Exprs_strategy)
@settings(max_examples=50)
def test_mydsl_exprs_instantiation(instance):
    assert isinstance(instance, myDsl_Exprs)

@given(instance=myDsl_Vars_strategy)
@settings(max_examples=50)
def test_mydsl_vars_instantiation(instance):
    assert isinstance(instance, myDsl_Vars)



@given(instance=myDsl_Vars_strategy)
def test_mydsl_vars_v1_setter(instance):
    original = instance.v1
    instance.v1 = original
    assert instance.v1 == original



@given(instance=myDsl_Vars_strategy)
def test_mydsl_vars_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=myDsl_Command_strategy)
@settings(max_examples=50)
def test_mydsl_command_instantiation(instance):
    assert isinstance(instance, myDsl_Command)



@given(instance=myDsl_Command_strategy)
def test_mydsl_command_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=myDsl_Output_strategy)
@settings(max_examples=50)
def test_mydsl_output_instantiation(instance):
    assert isinstance(instance, myDsl_Output)



@given(instance=myDsl_Output_strategy)
def test_mydsl_output_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original



@given(instance=myDsl_Output_strategy)
def test_mydsl_output_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=myDsl_Commands_strategy)
@settings(max_examples=50)
def test_mydsl_commands_instantiation(instance):
    assert isinstance(instance, myDsl_Commands)

@given(instance=myDsl_Input_strategy)
@settings(max_examples=50)
def test_mydsl_input_instantiation(instance):
    assert isinstance(instance, myDsl_Input)



@given(instance=myDsl_Input_strategy)
def test_mydsl_input_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original



@given(instance=myDsl_Input_strategy)
def test_mydsl_input_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=myDsl_Definiton_strategy)
@settings(max_examples=50)
def test_mydsl_definiton_instantiation(instance):
    assert isinstance(instance, myDsl_Definiton)

@given(instance=myDsl_Function_strategy)
@settings(max_examples=50)
def test_mydsl_function_instantiation(instance):
    assert isinstance(instance, myDsl_Function)



@given(instance=myDsl_Function_strategy)
def test_mydsl_function_funName_setter(instance):
    original = instance.funName
    instance.funName = original
    assert instance.funName == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
