import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    langage_while_ExprEq,
    langage_while_ExprAnd,
    langage_while_ExprSimple,
    langage_while_ExprNot,
    langage_while_ExprOr,
    langage_while_LExpr,
    langage_while_Foreach,
    langage_while_If,
    langage_while_For,
    langage_while_While,
    langage_while_Assign,
    langage_while_Command,
    langage_while_VAR,
    langage_while_Output,
    langage_while_Expr,
    langage_while_Exprs,
    langage_while_Vars,
    langage_while_Ifconfort,
    langage_while_Commands,
    langage_while_Input,
    langage_while_Definition,
    langage_while_SYMB,
    langage_while_Function,
    langage_while_Program,
    langage_while_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_langage_while_expreq_is_not_abstract():
    assert not inspect.isabstract(langage_while_ExprEq)


def test_langage_while_expreq_constructor_exists():
    assert callable(langage_while_ExprEq.__init__)


def test_langage_while_expreq_constructor_args():
    sig = inspect.signature(langage_while_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_exprand_is_not_abstract():
    assert not inspect.isabstract(langage_while_ExprAnd)


def test_langage_while_exprand_constructor_exists():
    assert callable(langage_while_ExprAnd.__init__)


def test_langage_while_exprand_constructor_args():
    sig = inspect.signature(langage_while_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_exprsimple_is_not_abstract():
    assert not inspect.isabstract(langage_while_ExprSimple)


def test_langage_while_exprsimple_constructor_exists():
    assert callable(langage_while_ExprSimple.__init__)


def test_langage_while_exprsimple_constructor_args():
    sig = inspect.signature(langage_while_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "mot" in params, "Missing parameter 'mot'"
    assert "nil" in params, "Missing parameter 'nil'"

def test_langage_while_exprsimple_has_mot():
    assert hasattr(langage_while_ExprSimple, "mot")
    descriptor = None
    for klass in langage_while_ExprSimple.__mro__:
        if "mot" in klass.__dict__:
            descriptor = klass.__dict__["mot"]
            break
    assert isinstance(descriptor, property)

def test_langage_while_exprsimple_has_nil():
    assert hasattr(langage_while_ExprSimple, "nil")
    descriptor = None
    for klass in langage_while_ExprSimple.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)



def test_langage_while_exprnot_is_not_abstract():
    assert not inspect.isabstract(langage_while_ExprNot)


def test_langage_while_exprnot_constructor_exists():
    assert callable(langage_while_ExprNot.__init__)


def test_langage_while_exprnot_constructor_args():
    sig = inspect.signature(langage_while_ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_expror_is_not_abstract():
    assert not inspect.isabstract(langage_while_ExprOr)


def test_langage_while_expror_constructor_exists():
    assert callable(langage_while_ExprOr.__init__)


def test_langage_while_expror_constructor_args():
    sig = inspect.signature(langage_while_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_lexpr_is_not_abstract():
    assert not inspect.isabstract(langage_while_LExpr)


def test_langage_while_lexpr_constructor_exists():
    assert callable(langage_while_LExpr.__init__)


def test_langage_while_lexpr_constructor_args():
    sig = inspect.signature(langage_while_LExpr.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_foreach_is_not_abstract():
    assert not inspect.isabstract(langage_while_Foreach)


def test_langage_while_foreach_constructor_exists():
    assert callable(langage_while_Foreach.__init__)


def test_langage_while_foreach_constructor_args():
    sig = inspect.signature(langage_while_Foreach.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_if_is_not_abstract():
    assert not inspect.isabstract(langage_while_If)


def test_langage_while_if_constructor_exists():
    assert callable(langage_while_If.__init__)


def test_langage_while_if_constructor_args():
    sig = inspect.signature(langage_while_If.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_for_is_not_abstract():
    assert not inspect.isabstract(langage_while_For)


def test_langage_while_for_constructor_exists():
    assert callable(langage_while_For.__init__)


def test_langage_while_for_constructor_args():
    sig = inspect.signature(langage_while_For.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_while_is_not_abstract():
    assert not inspect.isabstract(langage_while_While)


def test_langage_while_while_constructor_exists():
    assert callable(langage_while_While.__init__)


def test_langage_while_while_constructor_args():
    sig = inspect.signature(langage_while_While.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_assign_is_not_abstract():
    assert not inspect.isabstract(langage_while_Assign)


def test_langage_while_assign_constructor_exists():
    assert callable(langage_while_Assign.__init__)


def test_langage_while_assign_constructor_args():
    sig = inspect.signature(langage_while_Assign.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_command_is_not_abstract():
    assert not inspect.isabstract(langage_while_Command)


def test_langage_while_command_constructor_exists():
    assert callable(langage_while_Command.__init__)


def test_langage_while_command_constructor_args():
    sig = inspect.signature(langage_while_Command.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_langage_while_command_has_nop():
    assert hasattr(langage_while_Command, "nop")
    descriptor = None
    for klass in langage_while_Command.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_langage_while_var_is_not_abstract():
    assert not inspect.isabstract(langage_while_VAR)


def test_langage_while_var_constructor_exists():
    assert callable(langage_while_VAR.__init__)


def test_langage_while_var_constructor_args():
    sig = inspect.signature(langage_while_VAR.__init__)
    params = list(sig.parameters.keys())
    assert "cf" in params, "Missing parameter 'cf'"
    assert "bv" in params, "Missing parameter 'bv'"

def test_langage_while_var_has_cf():
    assert hasattr(langage_while_VAR, "cf")
    descriptor = None
    for klass in langage_while_VAR.__mro__:
        if "cf" in klass.__dict__:
            descriptor = klass.__dict__["cf"]
            break
    assert isinstance(descriptor, property)

def test_langage_while_var_has_bv():
    assert hasattr(langage_while_VAR, "bv")
    descriptor = None
    for klass in langage_while_VAR.__mro__:
        if "bv" in klass.__dict__:
            descriptor = klass.__dict__["bv"]
            break
    assert isinstance(descriptor, property)



def test_langage_while_output_is_not_abstract():
    assert not inspect.isabstract(langage_while_Output)


def test_langage_while_output_constructor_exists():
    assert callable(langage_while_Output.__init__)


def test_langage_while_output_constructor_args():
    sig = inspect.signature(langage_while_Output.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_expr_is_not_abstract():
    assert not inspect.isabstract(langage_while_Expr)


def test_langage_while_expr_constructor_exists():
    assert callable(langage_while_Expr.__init__)


def test_langage_while_expr_constructor_args():
    sig = inspect.signature(langage_while_Expr.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_exprs_is_not_abstract():
    assert not inspect.isabstract(langage_while_Exprs)


def test_langage_while_exprs_constructor_exists():
    assert callable(langage_while_Exprs.__init__)


def test_langage_while_exprs_constructor_args():
    sig = inspect.signature(langage_while_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_vars_is_not_abstract():
    assert not inspect.isabstract(langage_while_Vars)


def test_langage_while_vars_constructor_exists():
    assert callable(langage_while_Vars.__init__)


def test_langage_while_vars_constructor_args():
    sig = inspect.signature(langage_while_Vars.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_ifconfort_is_not_abstract():
    assert not inspect.isabstract(langage_while_Ifconfort)


def test_langage_while_ifconfort_constructor_exists():
    assert callable(langage_while_Ifconfort.__init__)


def test_langage_while_ifconfort_constructor_args():
    sig = inspect.signature(langage_while_Ifconfort.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_commands_is_not_abstract():
    assert not inspect.isabstract(langage_while_Commands)


def test_langage_while_commands_constructor_exists():
    assert callable(langage_while_Commands.__init__)


def test_langage_while_commands_constructor_args():
    sig = inspect.signature(langage_while_Commands.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_input_is_not_abstract():
    assert not inspect.isabstract(langage_while_Input)


def test_langage_while_input_constructor_exists():
    assert callable(langage_while_Input.__init__)


def test_langage_while_input_constructor_args():
    sig = inspect.signature(langage_while_Input.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_definition_is_not_abstract():
    assert not inspect.isabstract(langage_while_Definition)


def test_langage_while_definition_constructor_exists():
    assert callable(langage_while_Definition.__init__)


def test_langage_while_definition_constructor_args():
    sig = inspect.signature(langage_while_Definition.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_symb_is_not_abstract():
    assert not inspect.isabstract(langage_while_SYMB)


def test_langage_while_symb_constructor_exists():
    assert callable(langage_while_SYMB.__init__)


def test_langage_while_symb_constructor_args():
    sig = inspect.signature(langage_while_SYMB.__init__)
    params = list(sig.parameters.keys())
    assert "bs" in params, "Missing parameter 'bs'"
    assert "cf" in params, "Missing parameter 'cf'"

def test_langage_while_symb_has_bs():
    assert hasattr(langage_while_SYMB, "bs")
    descriptor = None
    for klass in langage_while_SYMB.__mro__:
        if "bs" in klass.__dict__:
            descriptor = klass.__dict__["bs"]
            break
    assert isinstance(descriptor, property)

def test_langage_while_symb_has_cf():
    assert hasattr(langage_while_SYMB, "cf")
    descriptor = None
    for klass in langage_while_SYMB.__mro__:
        if "cf" in klass.__dict__:
            descriptor = klass.__dict__["cf"]
            break
    assert isinstance(descriptor, property)



def test_langage_while_function_is_not_abstract():
    assert not inspect.isabstract(langage_while_Function)


def test_langage_while_function_constructor_exists():
    assert callable(langage_while_Function.__init__)


def test_langage_while_function_constructor_args():
    sig = inspect.signature(langage_while_Function.__init__)
    params = list(sig.parameters.keys())



def test_langage_while_program_is_not_abstract():
    assert not inspect.isabstract(langage_while_Program)


def test_langage_while_program_constructor_exists():
    assert callable(langage_while_Program.__init__)


def test_langage_while_program_constructor_args():
    sig = inspect.signature(langage_while_Program.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_langage_while_program_has_u():
    assert hasattr(langage_while_Program, "u")
    descriptor = None
    for klass in langage_while_Program.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_langage_while_model_is_not_abstract():
    assert not inspect.isabstract(langage_while_Model)


def test_langage_while_model_constructor_exists():
    assert callable(langage_while_Model.__init__)


def test_langage_while_model_constructor_args():
    sig = inspect.signature(langage_while_Model.__init__)
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
langage_while_ExprEq_strategy = st.builds(
    langage_while_ExprEq,
)
langage_while_ExprAnd_strategy = st.builds(
    langage_while_ExprAnd,
)
langage_while_ExprSimple_strategy = st.builds(
    langage_while_ExprSimple,
    mot=
        safe_text,
    nil=
        safe_text
)
langage_while_ExprNot_strategy = st.builds(
    langage_while_ExprNot,
)
langage_while_ExprOr_strategy = st.builds(
    langage_while_ExprOr,
)
langage_while_LExpr_strategy = st.builds(
    langage_while_LExpr,
)
langage_while_Foreach_strategy = st.builds(
    langage_while_Foreach,
)
langage_while_If_strategy = st.builds(
    langage_while_If,
)
langage_while_For_strategy = st.builds(
    langage_while_For,
)
langage_while_While_strategy = st.builds(
    langage_while_While,
)
langage_while_Assign_strategy = st.builds(
    langage_while_Assign,
)
langage_while_Command_strategy = st.builds(
    langage_while_Command,
    nop=
        safe_text
)
langage_while_VAR_strategy = st.builds(
    langage_while_VAR,
    cf=
        safe_text,
    bv=
        safe_text
)
langage_while_Output_strategy = st.builds(
    langage_while_Output,
)
langage_while_Expr_strategy = st.builds(
    langage_while_Expr,
)
langage_while_Exprs_strategy = st.builds(
    langage_while_Exprs,
)
langage_while_Vars_strategy = st.builds(
    langage_while_Vars,
)
langage_while_Ifconfort_strategy = st.builds(
    langage_while_Ifconfort,
)
langage_while_Commands_strategy = st.builds(
    langage_while_Commands,
)
langage_while_Input_strategy = st.builds(
    langage_while_Input,
)
langage_while_Definition_strategy = st.builds(
    langage_while_Definition,
)
langage_while_SYMB_strategy = st.builds(
    langage_while_SYMB,
    bs=
        safe_text,
    cf=
        safe_text
)
langage_while_Function_strategy = st.builds(
    langage_while_Function,
)
langage_while_Program_strategy = st.builds(
    langage_while_Program,
    u=
        safe_text
)
langage_while_Model_strategy = st.builds(
    langage_while_Model,
)

@given(instance=langage_while_ExprEq_strategy)
@settings(max_examples=50)
def test_langage_while_expreq_instantiation(instance):
    assert isinstance(instance, langage_while_ExprEq)

@given(instance=langage_while_ExprAnd_strategy)
@settings(max_examples=50)
def test_langage_while_exprand_instantiation(instance):
    assert isinstance(instance, langage_while_ExprAnd)

@given(instance=langage_while_ExprSimple_strategy)
@settings(max_examples=50)
def test_langage_while_exprsimple_instantiation(instance):
    assert isinstance(instance, langage_while_ExprSimple)



@given(instance=langage_while_ExprSimple_strategy)
def test_langage_while_exprsimple_mot_setter(instance):
    original = instance.mot
    instance.mot = original
    assert instance.mot == original



@given(instance=langage_while_ExprSimple_strategy)
def test_langage_while_exprsimple_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=langage_while_ExprNot_strategy)
@settings(max_examples=50)
def test_langage_while_exprnot_instantiation(instance):
    assert isinstance(instance, langage_while_ExprNot)

@given(instance=langage_while_ExprOr_strategy)
@settings(max_examples=50)
def test_langage_while_expror_instantiation(instance):
    assert isinstance(instance, langage_while_ExprOr)

@given(instance=langage_while_LExpr_strategy)
@settings(max_examples=50)
def test_langage_while_lexpr_instantiation(instance):
    assert isinstance(instance, langage_while_LExpr)

@given(instance=langage_while_Foreach_strategy)
@settings(max_examples=50)
def test_langage_while_foreach_instantiation(instance):
    assert isinstance(instance, langage_while_Foreach)

@given(instance=langage_while_If_strategy)
@settings(max_examples=50)
def test_langage_while_if_instantiation(instance):
    assert isinstance(instance, langage_while_If)

@given(instance=langage_while_For_strategy)
@settings(max_examples=50)
def test_langage_while_for_instantiation(instance):
    assert isinstance(instance, langage_while_For)

@given(instance=langage_while_While_strategy)
@settings(max_examples=50)
def test_langage_while_while_instantiation(instance):
    assert isinstance(instance, langage_while_While)

@given(instance=langage_while_Assign_strategy)
@settings(max_examples=50)
def test_langage_while_assign_instantiation(instance):
    assert isinstance(instance, langage_while_Assign)

@given(instance=langage_while_Command_strategy)
@settings(max_examples=50)
def test_langage_while_command_instantiation(instance):
    assert isinstance(instance, langage_while_Command)



@given(instance=langage_while_Command_strategy)
def test_langage_while_command_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=langage_while_VAR_strategy)
@settings(max_examples=50)
def test_langage_while_var_instantiation(instance):
    assert isinstance(instance, langage_while_VAR)



@given(instance=langage_while_VAR_strategy)
def test_langage_while_var_cf_setter(instance):
    original = instance.cf
    instance.cf = original
    assert instance.cf == original



@given(instance=langage_while_VAR_strategy)
def test_langage_while_var_bv_setter(instance):
    original = instance.bv
    instance.bv = original
    assert instance.bv == original

@given(instance=langage_while_Output_strategy)
@settings(max_examples=50)
def test_langage_while_output_instantiation(instance):
    assert isinstance(instance, langage_while_Output)

@given(instance=langage_while_Expr_strategy)
@settings(max_examples=50)
def test_langage_while_expr_instantiation(instance):
    assert isinstance(instance, langage_while_Expr)

@given(instance=langage_while_Exprs_strategy)
@settings(max_examples=50)
def test_langage_while_exprs_instantiation(instance):
    assert isinstance(instance, langage_while_Exprs)

@given(instance=langage_while_Vars_strategy)
@settings(max_examples=50)
def test_langage_while_vars_instantiation(instance):
    assert isinstance(instance, langage_while_Vars)

@given(instance=langage_while_Ifconfort_strategy)
@settings(max_examples=50)
def test_langage_while_ifconfort_instantiation(instance):
    assert isinstance(instance, langage_while_Ifconfort)

@given(instance=langage_while_Commands_strategy)
@settings(max_examples=50)
def test_langage_while_commands_instantiation(instance):
    assert isinstance(instance, langage_while_Commands)

@given(instance=langage_while_Input_strategy)
@settings(max_examples=50)
def test_langage_while_input_instantiation(instance):
    assert isinstance(instance, langage_while_Input)

@given(instance=langage_while_Definition_strategy)
@settings(max_examples=50)
def test_langage_while_definition_instantiation(instance):
    assert isinstance(instance, langage_while_Definition)

@given(instance=langage_while_SYMB_strategy)
@settings(max_examples=50)
def test_langage_while_symb_instantiation(instance):
    assert isinstance(instance, langage_while_SYMB)



@given(instance=langage_while_SYMB_strategy)
def test_langage_while_symb_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original



@given(instance=langage_while_SYMB_strategy)
def test_langage_while_symb_cf_setter(instance):
    original = instance.cf
    instance.cf = original
    assert instance.cf == original

@given(instance=langage_while_Function_strategy)
@settings(max_examples=50)
def test_langage_while_function_instantiation(instance):
    assert isinstance(instance, langage_while_Function)

@given(instance=langage_while_Program_strategy)
@settings(max_examples=50)
def test_langage_while_program_instantiation(instance):
    assert isinstance(instance, langage_while_Program)



@given(instance=langage_while_Program_strategy)
def test_langage_while_program_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=langage_while_Model_strategy)
@settings(max_examples=50)
def test_langage_while_model_instantiation(instance):
    assert isinstance(instance, langage_while_Model)
