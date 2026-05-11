import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wh::ExprEq,
    wh::ExprSimple,
    wh::ExprAnd,
    wh::Foreach,
    wh::ExprNot,
    wh::ExprOr,
    wh::LExpr,
    wh::Command,
    wh::Output,
    wh::Commands,
    wh::Input,
    wh::Definition,
    wh::Function,
    wh::If,
    wh::For,
    wh::Expr,
    wh::While,
    wh::Exprs,
    wh::Vars,
    wh::Assign,
    wh::Nop,
    wh::EObject,
    wh::Program,
    wh::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh::expreq_is_not_abstract():
    assert not inspect.isabstract(wh::ExprEq)


def test_wh::expreq_constructor_exists():
    assert callable(wh::ExprEq.__init__)


def test_wh::expreq_constructor_args():
    sig = inspect.signature(wh::ExprEq.__init__)
    params = list(sig.parameters.keys())
    assert "sym" in params, "Missing parameter 'sym'"

def test_wh::expreq_has_sym():
    assert hasattr(wh::ExprEq, "sym")
    descriptor = None
    for klass in wh::ExprEq.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)



def test_wh::exprsimple_is_not_abstract():
    assert not inspect.isabstract(wh::ExprSimple)


def test_wh::exprsimple_constructor_exists():
    assert callable(wh::ExprSimple.__init__)


def test_wh::exprsimple_constructor_args():
    sig = inspect.signature(wh::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"
    assert "variable" in params, "Missing parameter 'variable'"
    assert "sym" in params, "Missing parameter 'sym'"

def test_wh::exprsimple_has_nil():
    assert hasattr(wh::ExprSimple, "nil")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_wh::exprsimple_has_variable():
    assert hasattr(wh::ExprSimple, "variable")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_wh::exprsimple_has_sym():
    assert hasattr(wh::ExprSimple, "sym")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)



def test_wh::exprand_is_not_abstract():
    assert not inspect.isabstract(wh::ExprAnd)


def test_wh::exprand_constructor_exists():
    assert callable(wh::ExprAnd.__init__)


def test_wh::exprand_constructor_args():
    sig = inspect.signature(wh::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_wh::foreach_is_not_abstract():
    assert not inspect.isabstract(wh::Foreach)


def test_wh::foreach_constructor_exists():
    assert callable(wh::Foreach.__init__)


def test_wh::foreach_constructor_args():
    sig = inspect.signature(wh::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprnot_is_not_abstract():
    assert not inspect.isabstract(wh::ExprNot)


def test_wh::exprnot_constructor_exists():
    assert callable(wh::ExprNot.__init__)


def test_wh::exprnot_constructor_args():
    sig = inspect.signature(wh::ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "hasNot" in params, "Missing parameter 'hasNot'"

def test_wh::exprnot_has_hasNot():
    assert hasattr(wh::ExprNot, "hasNot")
    descriptor = None
    for klass in wh::ExprNot.__mro__:
        if "hasNot" in klass.__dict__:
            descriptor = klass.__dict__["hasNot"]
            break
    assert isinstance(descriptor, property)



def test_wh::expror_is_not_abstract():
    assert not inspect.isabstract(wh::ExprOr)


def test_wh::expror_constructor_exists():
    assert callable(wh::ExprOr.__init__)


def test_wh::expror_constructor_args():
    sig = inspect.signature(wh::ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_wh::lexpr_is_not_abstract():
    assert not inspect.isabstract(wh::LExpr)


def test_wh::lexpr_constructor_exists():
    assert callable(wh::LExpr.__init__)


def test_wh::lexpr_constructor_args():
    sig = inspect.signature(wh::LExpr.__init__)
    params = list(sig.parameters.keys())



def test_wh::command_is_not_abstract():
    assert not inspect.isabstract(wh::Command)


def test_wh::command_constructor_exists():
    assert callable(wh::Command.__init__)


def test_wh::command_constructor_args():
    sig = inspect.signature(wh::Command.__init__)
    params = list(sig.parameters.keys())



def test_wh::output_is_not_abstract():
    assert not inspect.isabstract(wh::Output)


def test_wh::output_constructor_exists():
    assert callable(wh::Output.__init__)


def test_wh::output_constructor_args():
    sig = inspect.signature(wh::Output.__init__)
    params = list(sig.parameters.keys())
    assert "r_values" in params, "Missing parameter 'r_values'"

def test_wh::output_has_r_values():
    assert hasattr(wh::Output, "r_values")
    descriptor = None
    for klass in wh::Output.__mro__:
        if "r_values" in klass.__dict__:
            descriptor = klass.__dict__["r_values"]
            break
    assert isinstance(descriptor, property)



def test_wh::commands_is_not_abstract():
    assert not inspect.isabstract(wh::Commands)


def test_wh::commands_constructor_exists():
    assert callable(wh::Commands.__init__)


def test_wh::commands_constructor_args():
    sig = inspect.signature(wh::Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh::input_is_not_abstract():
    assert not inspect.isabstract(wh::Input)


def test_wh::input_constructor_exists():
    assert callable(wh::Input.__init__)


def test_wh::input_constructor_args():
    sig = inspect.signature(wh::Input.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"

def test_wh::input_has_params():
    assert hasattr(wh::Input, "params")
    descriptor = None
    for klass in wh::Input.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_wh::definition_is_not_abstract():
    assert not inspect.isabstract(wh::Definition)


def test_wh::definition_constructor_exists():
    assert callable(wh::Definition.__init__)


def test_wh::definition_constructor_args():
    sig = inspect.signature(wh::Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh::function_is_not_abstract():
    assert not inspect.isabstract(wh::Function)


def test_wh::function_constructor_exists():
    assert callable(wh::Function.__init__)


def test_wh::function_constructor_args():
    sig = inspect.signature(wh::Function.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"

def test_wh::function_has_fname():
    assert hasattr(wh::Function, "fname")
    descriptor = None
    for klass in wh::Function.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)



def test_wh::if_is_not_abstract():
    assert not inspect.isabstract(wh::If)


def test_wh::if_constructor_exists():
    assert callable(wh::If.__init__)


def test_wh::if_constructor_args():
    sig = inspect.signature(wh::If.__init__)
    params = list(sig.parameters.keys())



def test_wh::for_is_not_abstract():
    assert not inspect.isabstract(wh::For)


def test_wh::for_constructor_exists():
    assert callable(wh::For.__init__)


def test_wh::for_constructor_args():
    sig = inspect.signature(wh::For.__init__)
    params = list(sig.parameters.keys())



def test_wh::expr_is_not_abstract():
    assert not inspect.isabstract(wh::Expr)


def test_wh::expr_constructor_exists():
    assert callable(wh::Expr.__init__)


def test_wh::expr_constructor_args():
    sig = inspect.signature(wh::Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh::while_is_not_abstract():
    assert not inspect.isabstract(wh::While)


def test_wh::while_constructor_exists():
    assert callable(wh::While.__init__)


def test_wh::while_constructor_args():
    sig = inspect.signature(wh::While.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprs_is_not_abstract():
    assert not inspect.isabstract(wh::Exprs)


def test_wh::exprs_constructor_exists():
    assert callable(wh::Exprs.__init__)


def test_wh::exprs_constructor_args():
    sig = inspect.signature(wh::Exprs.__init__)
    params = list(sig.parameters.keys())



def test_wh::vars_is_not_abstract():
    assert not inspect.isabstract(wh::Vars)


def test_wh::vars_constructor_exists():
    assert callable(wh::Vars.__init__)


def test_wh::vars_constructor_args():
    sig = inspect.signature(wh::Vars.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"

def test_wh::vars_has_variables():
    assert hasattr(wh::Vars, "variables")
    descriptor = None
    for klass in wh::Vars.__mro__:
        if "variables" in klass.__dict__:
            descriptor = klass.__dict__["variables"]
            break
    assert isinstance(descriptor, property)



def test_wh::assign_is_not_abstract():
    assert not inspect.isabstract(wh::Assign)


def test_wh::assign_constructor_exists():
    assert callable(wh::Assign.__init__)


def test_wh::assign_constructor_args():
    sig = inspect.signature(wh::Assign.__init__)
    params = list(sig.parameters.keys())



def test_wh::nop_is_not_abstract():
    assert not inspect.isabstract(wh::Nop)


def test_wh::nop_constructor_exists():
    assert callable(wh::Nop.__init__)


def test_wh::nop_constructor_args():
    sig = inspect.signature(wh::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_wh::nop_has_nop():
    assert hasattr(wh::Nop, "nop")
    descriptor = None
    for klass in wh::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_wh::eobject_is_not_abstract():
    assert not inspect.isabstract(wh::EObject)


def test_wh::eobject_constructor_exists():
    assert callable(wh::EObject.__init__)


def test_wh::eobject_constructor_args():
    sig = inspect.signature(wh::EObject.__init__)
    params = list(sig.parameters.keys())



def test_wh::program_is_not_abstract():
    assert not inspect.isabstract(wh::Program)


def test_wh::program_constructor_exists():
    assert callable(wh::Program.__init__)


def test_wh::program_constructor_args():
    sig = inspect.signature(wh::Program.__init__)
    params = list(sig.parameters.keys())



def test_wh::model_is_not_abstract():
    assert not inspect.isabstract(wh::Model)


def test_wh::model_constructor_exists():
    assert callable(wh::Model.__init__)


def test_wh::model_constructor_args():
    sig = inspect.signature(wh::Model.__init__)
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
wh::ExprEq_strategy = st.builds(
    wh::ExprEq,
    sym=
        safe_text
)
wh::ExprSimple_strategy = st.builds(
    wh::ExprSimple,
    nil=
        safe_text,
    variable=
        safe_text,
    sym=
        safe_text
)
wh::ExprAnd_strategy = st.builds(
    wh::ExprAnd,
)
wh::Foreach_strategy = st.builds(
    wh::Foreach,
)
wh::ExprNot_strategy = st.builds(
    wh::ExprNot,
    hasNot=
        safe_text
)
wh::ExprOr_strategy = st.builds(
    wh::ExprOr,
)
wh::LExpr_strategy = st.builds(
    wh::LExpr,
)
wh::Command_strategy = st.builds(
    wh::Command,
)
wh::Output_strategy = st.builds(
    wh::Output,
    r_values=
        safe_text
)
wh::Commands_strategy = st.builds(
    wh::Commands,
)
wh::Input_strategy = st.builds(
    wh::Input,
    params=
        safe_text
)
wh::Definition_strategy = st.builds(
    wh::Definition,
)
wh::Function_strategy = st.builds(
    wh::Function,
    fname=
        safe_text
)
wh::If_strategy = st.builds(
    wh::If,
)
wh::For_strategy = st.builds(
    wh::For,
)
wh::Expr_strategy = st.builds(
    wh::Expr,
)
wh::While_strategy = st.builds(
    wh::While,
)
wh::Exprs_strategy = st.builds(
    wh::Exprs,
)
wh::Vars_strategy = st.builds(
    wh::Vars,
    variables=
        safe_text
)
wh::Assign_strategy = st.builds(
    wh::Assign,
)
wh::Nop_strategy = st.builds(
    wh::Nop,
    nop=
        safe_text
)
wh::EObject_strategy = st.builds(
    wh::EObject,
)
wh::Program_strategy = st.builds(
    wh::Program,
)
wh::Model_strategy = st.builds(
    wh::Model,
)

@given(instance=wh::ExprEq_strategy)
@settings(max_examples=50)
def test_wh::expreq_instantiation(instance):
    assert isinstance(instance, wh::ExprEq)

@given(instance=wh::ExprEq_strategy)
def test_wh::expreq_sym_type(instance):
    assert isinstance(instance.sym, str)


@given(instance=wh::ExprEq_strategy)
def test_wh::expreq_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=wh::ExprSimple_strategy)
@settings(max_examples=50)
def test_wh::exprsimple_instantiation(instance):
    assert isinstance(instance, wh::ExprSimple)

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_nil_type(instance):
    assert isinstance(instance.nil, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_sym_type(instance):
    assert isinstance(instance.sym, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=wh::ExprAnd_strategy)
@settings(max_examples=50)
def test_wh::exprand_instantiation(instance):
    assert isinstance(instance, wh::ExprAnd)

@given(instance=wh::Foreach_strategy)
@settings(max_examples=50)
def test_wh::foreach_instantiation(instance):
    assert isinstance(instance, wh::Foreach)

@given(instance=wh::ExprNot_strategy)
@settings(max_examples=50)
def test_wh::exprnot_instantiation(instance):
    assert isinstance(instance, wh::ExprNot)

@given(instance=wh::ExprNot_strategy)
def test_wh::exprnot_hasNot_type(instance):
    assert isinstance(instance.hasNot, str)


@given(instance=wh::ExprNot_strategy)
def test_wh::exprnot_hasNot_setter(instance):
    original = instance.hasNot
    instance.hasNot = original
    assert instance.hasNot == original

@given(instance=wh::ExprOr_strategy)
@settings(max_examples=50)
def test_wh::expror_instantiation(instance):
    assert isinstance(instance, wh::ExprOr)

@given(instance=wh::LExpr_strategy)
@settings(max_examples=50)
def test_wh::lexpr_instantiation(instance):
    assert isinstance(instance, wh::LExpr)

@given(instance=wh::Command_strategy)
@settings(max_examples=50)
def test_wh::command_instantiation(instance):
    assert isinstance(instance, wh::Command)

@given(instance=wh::Output_strategy)
@settings(max_examples=50)
def test_wh::output_instantiation(instance):
    assert isinstance(instance, wh::Output)

@given(instance=wh::Output_strategy)
def test_wh::output_r_values_type(instance):
    assert isinstance(instance.r_values, str)


@given(instance=wh::Output_strategy)
def test_wh::output_r_values_setter(instance):
    original = instance.r_values
    instance.r_values = original
    assert instance.r_values == original

@given(instance=wh::Commands_strategy)
@settings(max_examples=50)
def test_wh::commands_instantiation(instance):
    assert isinstance(instance, wh::Commands)

@given(instance=wh::Input_strategy)
@settings(max_examples=50)
def test_wh::input_instantiation(instance):
    assert isinstance(instance, wh::Input)

@given(instance=wh::Input_strategy)
def test_wh::input_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=wh::Input_strategy)
def test_wh::input_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=wh::Definition_strategy)
@settings(max_examples=50)
def test_wh::definition_instantiation(instance):
    assert isinstance(instance, wh::Definition)

@given(instance=wh::Function_strategy)
@settings(max_examples=50)
def test_wh::function_instantiation(instance):
    assert isinstance(instance, wh::Function)

@given(instance=wh::Function_strategy)
def test_wh::function_fname_type(instance):
    assert isinstance(instance.fname, str)


@given(instance=wh::Function_strategy)
def test_wh::function_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original

@given(instance=wh::If_strategy)
@settings(max_examples=50)
def test_wh::if_instantiation(instance):
    assert isinstance(instance, wh::If)

@given(instance=wh::For_strategy)
@settings(max_examples=50)
def test_wh::for_instantiation(instance):
    assert isinstance(instance, wh::For)

@given(instance=wh::Expr_strategy)
@settings(max_examples=50)
def test_wh::expr_instantiation(instance):
    assert isinstance(instance, wh::Expr)

@given(instance=wh::While_strategy)
@settings(max_examples=50)
def test_wh::while_instantiation(instance):
    assert isinstance(instance, wh::While)

@given(instance=wh::Exprs_strategy)
@settings(max_examples=50)
def test_wh::exprs_instantiation(instance):
    assert isinstance(instance, wh::Exprs)

@given(instance=wh::Vars_strategy)
@settings(max_examples=50)
def test_wh::vars_instantiation(instance):
    assert isinstance(instance, wh::Vars)

@given(instance=wh::Vars_strategy)
def test_wh::vars_variables_type(instance):
    assert isinstance(instance.variables, str)


@given(instance=wh::Vars_strategy)
def test_wh::vars_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original

@given(instance=wh::Assign_strategy)
@settings(max_examples=50)
def test_wh::assign_instantiation(instance):
    assert isinstance(instance, wh::Assign)

@given(instance=wh::Nop_strategy)
@settings(max_examples=50)
def test_wh::nop_instantiation(instance):
    assert isinstance(instance, wh::Nop)

@given(instance=wh::Nop_strategy)
def test_wh::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=wh::Nop_strategy)
def test_wh::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh::EObject_strategy)
@settings(max_examples=50)
def test_wh::eobject_instantiation(instance):
    assert isinstance(instance, wh::EObject)

@given(instance=wh::Program_strategy)
@settings(max_examples=50)
def test_wh::program_instantiation(instance):
    assert isinstance(instance, wh::Program)

@given(instance=wh::Model_strategy)
@settings(max_examples=50)
def test_wh::model_instantiation(instance):
    assert isinstance(instance, wh::Model)
