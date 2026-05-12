import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wh_For,
    wh_Expr,
    wh_While,
    wh_Exprs,
    wh_Vars,
    wh_Assign,
    wh_Nop,
    wh_ExprEq,
    wh_EObject,
    wh_ExprSimple,
    wh_Program,
    wh_ExprAnd,
    wh_Foreach,
    wh_ExprNot,
    wh_ExprOr,
    wh_LExpr,
    wh_Command,
    wh_Model,
    wh_Output,
    wh_Commands,
    wh_Input,
    wh_Definition,
    wh_Function,
    wh_If,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh_for_is_not_abstract():
    assert not inspect.isabstract(wh_For)


def test_wh_for_constructor_exists():
    assert callable(wh_For.__init__)


def test_wh_for_constructor_args():
    sig = inspect.signature(wh_For.__init__)
    params = list(sig.parameters.keys())



def test_wh_expr_is_not_abstract():
    assert not inspect.isabstract(wh_Expr)


def test_wh_expr_constructor_exists():
    assert callable(wh_Expr.__init__)


def test_wh_expr_constructor_args():
    sig = inspect.signature(wh_Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh_while_is_not_abstract():
    assert not inspect.isabstract(wh_While)


def test_wh_while_constructor_exists():
    assert callable(wh_While.__init__)


def test_wh_while_constructor_args():
    sig = inspect.signature(wh_While.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprs_is_not_abstract():
    assert not inspect.isabstract(wh_Exprs)


def test_wh_exprs_constructor_exists():
    assert callable(wh_Exprs.__init__)


def test_wh_exprs_constructor_args():
    sig = inspect.signature(wh_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_wh_vars_is_not_abstract():
    assert not inspect.isabstract(wh_Vars)


def test_wh_vars_constructor_exists():
    assert callable(wh_Vars.__init__)


def test_wh_vars_constructor_args():
    sig = inspect.signature(wh_Vars.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"

def test_wh_vars_has_variables():
    assert hasattr(wh_Vars, "variables")
    descriptor = None
    for klass in wh_Vars.__mro__:
        if "variables" in klass.__dict__:
            descriptor = klass.__dict__["variables"]
            break
    assert isinstance(descriptor, property)



def test_wh_assign_is_not_abstract():
    assert not inspect.isabstract(wh_Assign)


def test_wh_assign_constructor_exists():
    assert callable(wh_Assign.__init__)


def test_wh_assign_constructor_args():
    sig = inspect.signature(wh_Assign.__init__)
    params = list(sig.parameters.keys())



def test_wh_nop_is_not_abstract():
    assert not inspect.isabstract(wh_Nop)


def test_wh_nop_constructor_exists():
    assert callable(wh_Nop.__init__)


def test_wh_nop_constructor_args():
    sig = inspect.signature(wh_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_wh_nop_has_nop():
    assert hasattr(wh_Nop, "nop")
    descriptor = None
    for klass in wh_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_wh_expreq_is_not_abstract():
    assert not inspect.isabstract(wh_ExprEq)


def test_wh_expreq_constructor_exists():
    assert callable(wh_ExprEq.__init__)


def test_wh_expreq_constructor_args():
    sig = inspect.signature(wh_ExprEq.__init__)
    params = list(sig.parameters.keys())
    assert "sym" in params, "Missing parameter 'sym'"

def test_wh_expreq_has_sym():
    assert hasattr(wh_ExprEq, "sym")
    descriptor = None
    for klass in wh_ExprEq.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)



def test_wh_eobject_is_not_abstract():
    assert not inspect.isabstract(wh_EObject)


def test_wh_eobject_constructor_exists():
    assert callable(wh_EObject.__init__)


def test_wh_eobject_constructor_args():
    sig = inspect.signature(wh_EObject.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprsimple_is_not_abstract():
    assert not inspect.isabstract(wh_ExprSimple)


def test_wh_exprsimple_constructor_exists():
    assert callable(wh_ExprSimple.__init__)


def test_wh_exprsimple_constructor_args():
    sig = inspect.signature(wh_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"
    assert "sym" in params, "Missing parameter 'sym'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_wh_exprsimple_has_nil():
    assert hasattr(wh_ExprSimple, "nil")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_wh_exprsimple_has_sym():
    assert hasattr(wh_ExprSimple, "sym")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)

def test_wh_exprsimple_has_variable():
    assert hasattr(wh_ExprSimple, "variable")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_wh_program_is_not_abstract():
    assert not inspect.isabstract(wh_Program)


def test_wh_program_constructor_exists():
    assert callable(wh_Program.__init__)


def test_wh_program_constructor_args():
    sig = inspect.signature(wh_Program.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprand_is_not_abstract():
    assert not inspect.isabstract(wh_ExprAnd)


def test_wh_exprand_constructor_exists():
    assert callable(wh_ExprAnd.__init__)


def test_wh_exprand_constructor_args():
    sig = inspect.signature(wh_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_wh_foreach_is_not_abstract():
    assert not inspect.isabstract(wh_Foreach)


def test_wh_foreach_constructor_exists():
    assert callable(wh_Foreach.__init__)


def test_wh_foreach_constructor_args():
    sig = inspect.signature(wh_Foreach.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprnot_is_not_abstract():
    assert not inspect.isabstract(wh_ExprNot)


def test_wh_exprnot_constructor_exists():
    assert callable(wh_ExprNot.__init__)


def test_wh_exprnot_constructor_args():
    sig = inspect.signature(wh_ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "hasNot" in params, "Missing parameter 'hasNot'"

def test_wh_exprnot_has_hasNot():
    assert hasattr(wh_ExprNot, "hasNot")
    descriptor = None
    for klass in wh_ExprNot.__mro__:
        if "hasNot" in klass.__dict__:
            descriptor = klass.__dict__["hasNot"]
            break
    assert isinstance(descriptor, property)



def test_wh_expror_is_not_abstract():
    assert not inspect.isabstract(wh_ExprOr)


def test_wh_expror_constructor_exists():
    assert callable(wh_ExprOr.__init__)


def test_wh_expror_constructor_args():
    sig = inspect.signature(wh_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_wh_lexpr_is_not_abstract():
    assert not inspect.isabstract(wh_LExpr)


def test_wh_lexpr_constructor_exists():
    assert callable(wh_LExpr.__init__)


def test_wh_lexpr_constructor_args():
    sig = inspect.signature(wh_LExpr.__init__)
    params = list(sig.parameters.keys())



def test_wh_command_is_not_abstract():
    assert not inspect.isabstract(wh_Command)


def test_wh_command_constructor_exists():
    assert callable(wh_Command.__init__)


def test_wh_command_constructor_args():
    sig = inspect.signature(wh_Command.__init__)
    params = list(sig.parameters.keys())



def test_wh_model_is_not_abstract():
    assert not inspect.isabstract(wh_Model)


def test_wh_model_constructor_exists():
    assert callable(wh_Model.__init__)


def test_wh_model_constructor_args():
    sig = inspect.signature(wh_Model.__init__)
    params = list(sig.parameters.keys())



def test_wh_output_is_not_abstract():
    assert not inspect.isabstract(wh_Output)


def test_wh_output_constructor_exists():
    assert callable(wh_Output.__init__)


def test_wh_output_constructor_args():
    sig = inspect.signature(wh_Output.__init__)
    params = list(sig.parameters.keys())
    assert "r_values" in params, "Missing parameter 'r_values'"

def test_wh_output_has_r_values():
    assert hasattr(wh_Output, "r_values")
    descriptor = None
    for klass in wh_Output.__mro__:
        if "r_values" in klass.__dict__:
            descriptor = klass.__dict__["r_values"]
            break
    assert isinstance(descriptor, property)



def test_wh_commands_is_not_abstract():
    assert not inspect.isabstract(wh_Commands)


def test_wh_commands_constructor_exists():
    assert callable(wh_Commands.__init__)


def test_wh_commands_constructor_args():
    sig = inspect.signature(wh_Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh_input_is_not_abstract():
    assert not inspect.isabstract(wh_Input)


def test_wh_input_constructor_exists():
    assert callable(wh_Input.__init__)


def test_wh_input_constructor_args():
    sig = inspect.signature(wh_Input.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"

def test_wh_input_has_params():
    assert hasattr(wh_Input, "params")
    descriptor = None
    for klass in wh_Input.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_wh_definition_is_not_abstract():
    assert not inspect.isabstract(wh_Definition)


def test_wh_definition_constructor_exists():
    assert callable(wh_Definition.__init__)


def test_wh_definition_constructor_args():
    sig = inspect.signature(wh_Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh_function_is_not_abstract():
    assert not inspect.isabstract(wh_Function)


def test_wh_function_constructor_exists():
    assert callable(wh_Function.__init__)


def test_wh_function_constructor_args():
    sig = inspect.signature(wh_Function.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"

def test_wh_function_has_fname():
    assert hasattr(wh_Function, "fname")
    descriptor = None
    for klass in wh_Function.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)



def test_wh_if_is_not_abstract():
    assert not inspect.isabstract(wh_If)


def test_wh_if_constructor_exists():
    assert callable(wh_If.__init__)


def test_wh_if_constructor_args():
    sig = inspect.signature(wh_If.__init__)
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
wh_For_strategy = st.builds(
    wh_For,
)
wh_Expr_strategy = st.builds(
    wh_Expr,
)
wh_While_strategy = st.builds(
    wh_While,
)
wh_Exprs_strategy = st.builds(
    wh_Exprs,
)
wh_Vars_strategy = st.builds(
    wh_Vars,
    variables=
        safe_text
)
wh_Assign_strategy = st.builds(
    wh_Assign,
)
wh_Nop_strategy = st.builds(
    wh_Nop,
    nop=
        safe_text
)
wh_ExprEq_strategy = st.builds(
    wh_ExprEq,
    sym=
        safe_text
)
wh_EObject_strategy = st.builds(
    wh_EObject,
)
wh_ExprSimple_strategy = st.builds(
    wh_ExprSimple,
    nil=
        safe_text,
    sym=
        safe_text,
    variable=
        safe_text
)
wh_Program_strategy = st.builds(
    wh_Program,
)
wh_ExprAnd_strategy = st.builds(
    wh_ExprAnd,
)
wh_Foreach_strategy = st.builds(
    wh_Foreach,
)
wh_ExprNot_strategy = st.builds(
    wh_ExprNot,
    hasNot=
        safe_text
)
wh_ExprOr_strategy = st.builds(
    wh_ExprOr,
)
wh_LExpr_strategy = st.builds(
    wh_LExpr,
)
wh_Command_strategy = st.builds(
    wh_Command,
)
wh_Model_strategy = st.builds(
    wh_Model,
)
wh_Output_strategy = st.builds(
    wh_Output,
    r_values=
        safe_text
)
wh_Commands_strategy = st.builds(
    wh_Commands,
)
wh_Input_strategy = st.builds(
    wh_Input,
    params=
        safe_text
)
wh_Definition_strategy = st.builds(
    wh_Definition,
)
wh_Function_strategy = st.builds(
    wh_Function,
    fname=
        safe_text
)
wh_If_strategy = st.builds(
    wh_If,
)

@given(instance=wh_For_strategy)
@settings(max_examples=50)
def test_wh_for_instantiation(instance):
    assert isinstance(instance, wh_For)

@given(instance=wh_Expr_strategy)
@settings(max_examples=50)
def test_wh_expr_instantiation(instance):
    assert isinstance(instance, wh_Expr)

@given(instance=wh_While_strategy)
@settings(max_examples=50)
def test_wh_while_instantiation(instance):
    assert isinstance(instance, wh_While)

@given(instance=wh_Exprs_strategy)
@settings(max_examples=50)
def test_wh_exprs_instantiation(instance):
    assert isinstance(instance, wh_Exprs)

@given(instance=wh_Vars_strategy)
@settings(max_examples=50)
def test_wh_vars_instantiation(instance):
    assert isinstance(instance, wh_Vars)



@given(instance=wh_Vars_strategy)
def test_wh_vars_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original

@given(instance=wh_Assign_strategy)
@settings(max_examples=50)
def test_wh_assign_instantiation(instance):
    assert isinstance(instance, wh_Assign)

@given(instance=wh_Nop_strategy)
@settings(max_examples=50)
def test_wh_nop_instantiation(instance):
    assert isinstance(instance, wh_Nop)



@given(instance=wh_Nop_strategy)
def test_wh_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh_ExprEq_strategy)
@settings(max_examples=50)
def test_wh_expreq_instantiation(instance):
    assert isinstance(instance, wh_ExprEq)



@given(instance=wh_ExprEq_strategy)
def test_wh_expreq_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=wh_EObject_strategy)
@settings(max_examples=50)
def test_wh_eobject_instantiation(instance):
    assert isinstance(instance, wh_EObject)

@given(instance=wh_ExprSimple_strategy)
@settings(max_examples=50)
def test_wh_exprsimple_instantiation(instance):
    assert isinstance(instance, wh_ExprSimple)



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=wh_Program_strategy)
@settings(max_examples=50)
def test_wh_program_instantiation(instance):
    assert isinstance(instance, wh_Program)

@given(instance=wh_ExprAnd_strategy)
@settings(max_examples=50)
def test_wh_exprand_instantiation(instance):
    assert isinstance(instance, wh_ExprAnd)

@given(instance=wh_Foreach_strategy)
@settings(max_examples=50)
def test_wh_foreach_instantiation(instance):
    assert isinstance(instance, wh_Foreach)

@given(instance=wh_ExprNot_strategy)
@settings(max_examples=50)
def test_wh_exprnot_instantiation(instance):
    assert isinstance(instance, wh_ExprNot)



@given(instance=wh_ExprNot_strategy)
def test_wh_exprnot_hasNot_setter(instance):
    original = instance.hasNot
    instance.hasNot = original
    assert instance.hasNot == original

@given(instance=wh_ExprOr_strategy)
@settings(max_examples=50)
def test_wh_expror_instantiation(instance):
    assert isinstance(instance, wh_ExprOr)

@given(instance=wh_LExpr_strategy)
@settings(max_examples=50)
def test_wh_lexpr_instantiation(instance):
    assert isinstance(instance, wh_LExpr)

@given(instance=wh_Command_strategy)
@settings(max_examples=50)
def test_wh_command_instantiation(instance):
    assert isinstance(instance, wh_Command)

@given(instance=wh_Model_strategy)
@settings(max_examples=50)
def test_wh_model_instantiation(instance):
    assert isinstance(instance, wh_Model)

@given(instance=wh_Output_strategy)
@settings(max_examples=50)
def test_wh_output_instantiation(instance):
    assert isinstance(instance, wh_Output)



@given(instance=wh_Output_strategy)
def test_wh_output_r_values_setter(instance):
    original = instance.r_values
    instance.r_values = original
    assert instance.r_values == original

@given(instance=wh_Commands_strategy)
@settings(max_examples=50)
def test_wh_commands_instantiation(instance):
    assert isinstance(instance, wh_Commands)

@given(instance=wh_Input_strategy)
@settings(max_examples=50)
def test_wh_input_instantiation(instance):
    assert isinstance(instance, wh_Input)



@given(instance=wh_Input_strategy)
def test_wh_input_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=wh_Definition_strategy)
@settings(max_examples=50)
def test_wh_definition_instantiation(instance):
    assert isinstance(instance, wh_Definition)

@given(instance=wh_Function_strategy)
@settings(max_examples=50)
def test_wh_function_instantiation(instance):
    assert isinstance(instance, wh_Function)



@given(instance=wh_Function_strategy)
def test_wh_function_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original

@given(instance=wh_If_strategy)
@settings(max_examples=50)
def test_wh_if_instantiation(instance):
    assert isinstance(instance, wh_If)
