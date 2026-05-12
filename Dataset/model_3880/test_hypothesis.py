import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    flinkie2_Option,
    flinkie2_BoolExpr,
    flinkie2_AssignStat,
    Node,
    flinkie2_Question,
    flinkie2_Message,
    flinkie2_BooleanEvaluation,
    flinkie2_Variable,
    IntExpr,
    flinkie2_OneOpInt,
    flinkie2_IntExpr,
    BoolExpr,
    flinkie2_BracExprBool,
    flinkie2_Comparison,
    flinkie2_TwoOpBool,
    flinkie2_BoolVal,
    flinkie2_OneOpBool,
    flinkie2_BracExprInt,
    flinkie2_FlowChart,
    flinkie2_VariableExpr,
    flinkie2_Number,
    flinkie2_TwoOpInt,
    flinkie2_DeclStat,
    flinkie2_Init,
    flinkie2_Node,
    ECompOp,
    EBoolTwoOp,
    EIntTwoOp,
    EIntOneOp,
    EBoolVal,
    EBoolOneOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flinkie2_option_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Option)


def test_flinkie2_option_constructor_exists():
    assert callable(flinkie2_Option.__init__)


def test_flinkie2_option_constructor_args():
    sig = inspect.signature(flinkie2_Option.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_flinkie2_option_has_text():
    assert hasattr(flinkie2_Option, "text")
    descriptor = None
    for klass in flinkie2_Option.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_boolexpr_is_not_abstract():
    assert not inspect.isabstract(flinkie2_BoolExpr)


def test_flinkie2_boolexpr_constructor_exists():
    assert callable(flinkie2_BoolExpr.__init__)


def test_flinkie2_boolexpr_constructor_args():
    sig = inspect.signature(flinkie2_BoolExpr.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_assignstat_is_not_abstract():
    assert not inspect.isabstract(flinkie2_AssignStat)


def test_flinkie2_assignstat_constructor_exists():
    assert callable(flinkie2_AssignStat.__init__)


def test_flinkie2_assignstat_constructor_args():
    sig = inspect.signature(flinkie2_AssignStat.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_question_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Question)


def test_flinkie2_question_constructor_exists():
    assert callable(flinkie2_Question.__init__)


def test_flinkie2_question_constructor_args():
    sig = inspect.signature(flinkie2_Question.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_flinkie2_question_has_text():
    assert hasattr(flinkie2_Question, "text")
    descriptor = None
    for klass in flinkie2_Question.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_message_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Message)


def test_flinkie2_message_constructor_exists():
    assert callable(flinkie2_Message.__init__)


def test_flinkie2_message_constructor_args():
    sig = inspect.signature(flinkie2_Message.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_flinkie2_message_has_text():
    assert hasattr(flinkie2_Message, "text")
    descriptor = None
    for klass in flinkie2_Message.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_booleanevaluation_is_not_abstract():
    assert not inspect.isabstract(flinkie2_BooleanEvaluation)


def test_flinkie2_booleanevaluation_constructor_exists():
    assert callable(flinkie2_BooleanEvaluation.__init__)


def test_flinkie2_booleanevaluation_constructor_args():
    sig = inspect.signature(flinkie2_BooleanEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_variable_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Variable)


def test_flinkie2_variable_constructor_exists():
    assert callable(flinkie2_Variable.__init__)


def test_flinkie2_variable_constructor_args():
    sig = inspect.signature(flinkie2_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_flinkie2_variable_has_name():
    assert hasattr(flinkie2_Variable, "name")
    descriptor = None
    for klass in flinkie2_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_intexpr_is_not_abstract():
    assert not inspect.isabstract(IntExpr)


def test_intexpr_constructor_exists():
    assert callable(IntExpr.__init__)


def test_intexpr_constructor_args():
    sig = inspect.signature(IntExpr.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_oneopint_is_not_abstract():
    assert not inspect.isabstract(flinkie2_OneOpInt)


def test_flinkie2_oneopint_constructor_exists():
    assert callable(flinkie2_OneOpInt.__init__)


def test_flinkie2_oneopint_constructor_args():
    sig = inspect.signature(flinkie2_OneOpInt.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flinkie2_oneopint_has_operator():
    assert hasattr(flinkie2_OneOpInt, "operator")
    descriptor = None
    for klass in flinkie2_OneOpInt.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_intexpr_is_not_abstract():
    assert not inspect.isabstract(flinkie2_IntExpr)


def test_flinkie2_intexpr_constructor_exists():
    assert callable(flinkie2_IntExpr.__init__)


def test_flinkie2_intexpr_constructor_args():
    sig = inspect.signature(flinkie2_IntExpr.__init__)
    params = list(sig.parameters.keys())



def test_boolexpr_is_not_abstract():
    assert not inspect.isabstract(BoolExpr)


def test_boolexpr_constructor_exists():
    assert callable(BoolExpr.__init__)


def test_boolexpr_constructor_args():
    sig = inspect.signature(BoolExpr.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_bracexprbool_is_not_abstract():
    assert not inspect.isabstract(flinkie2_BracExprBool)


def test_flinkie2_bracexprbool_constructor_exists():
    assert callable(flinkie2_BracExprBool.__init__)


def test_flinkie2_bracexprbool_constructor_args():
    sig = inspect.signature(flinkie2_BracExprBool.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_comparison_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Comparison)


def test_flinkie2_comparison_constructor_exists():
    assert callable(flinkie2_Comparison.__init__)


def test_flinkie2_comparison_constructor_args():
    sig = inspect.signature(flinkie2_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flinkie2_comparison_has_operator():
    assert hasattr(flinkie2_Comparison, "operator")
    descriptor = None
    for klass in flinkie2_Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_twoopbool_is_not_abstract():
    assert not inspect.isabstract(flinkie2_TwoOpBool)


def test_flinkie2_twoopbool_constructor_exists():
    assert callable(flinkie2_TwoOpBool.__init__)


def test_flinkie2_twoopbool_constructor_args():
    sig = inspect.signature(flinkie2_TwoOpBool.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flinkie2_twoopbool_has_operator():
    assert hasattr(flinkie2_TwoOpBool, "operator")
    descriptor = None
    for klass in flinkie2_TwoOpBool.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_boolval_is_not_abstract():
    assert not inspect.isabstract(flinkie2_BoolVal)


def test_flinkie2_boolval_constructor_exists():
    assert callable(flinkie2_BoolVal.__init__)


def test_flinkie2_boolval_constructor_args():
    sig = inspect.signature(flinkie2_BoolVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_flinkie2_boolval_has_value():
    assert hasattr(flinkie2_BoolVal, "value")
    descriptor = None
    for klass in flinkie2_BoolVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_oneopbool_is_not_abstract():
    assert not inspect.isabstract(flinkie2_OneOpBool)


def test_flinkie2_oneopbool_constructor_exists():
    assert callable(flinkie2_OneOpBool.__init__)


def test_flinkie2_oneopbool_constructor_args():
    sig = inspect.signature(flinkie2_OneOpBool.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flinkie2_oneopbool_has_operator():
    assert hasattr(flinkie2_OneOpBool, "operator")
    descriptor = None
    for klass in flinkie2_OneOpBool.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_bracexprint_is_not_abstract():
    assert not inspect.isabstract(flinkie2_BracExprInt)


def test_flinkie2_bracexprint_constructor_exists():
    assert callable(flinkie2_BracExprInt.__init__)


def test_flinkie2_bracexprint_constructor_args():
    sig = inspect.signature(flinkie2_BracExprInt.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_flowchart_is_not_abstract():
    assert not inspect.isabstract(flinkie2_FlowChart)


def test_flinkie2_flowchart_constructor_exists():
    assert callable(flinkie2_FlowChart.__init__)


def test_flinkie2_flowchart_constructor_args():
    sig = inspect.signature(flinkie2_FlowChart.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_variableexpr_is_not_abstract():
    assert not inspect.isabstract(flinkie2_VariableExpr)


def test_flinkie2_variableexpr_constructor_exists():
    assert callable(flinkie2_VariableExpr.__init__)


def test_flinkie2_variableexpr_constructor_args():
    sig = inspect.signature(flinkie2_VariableExpr.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_number_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Number)


def test_flinkie2_number_constructor_exists():
    assert callable(flinkie2_Number.__init__)


def test_flinkie2_number_constructor_args():
    sig = inspect.signature(flinkie2_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_flinkie2_number_has_value():
    assert hasattr(flinkie2_Number, "value")
    descriptor = None
    for klass in flinkie2_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_twoopint_is_not_abstract():
    assert not inspect.isabstract(flinkie2_TwoOpInt)


def test_flinkie2_twoopint_constructor_exists():
    assert callable(flinkie2_TwoOpInt.__init__)


def test_flinkie2_twoopint_constructor_args():
    sig = inspect.signature(flinkie2_TwoOpInt.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flinkie2_twoopint_has_operator():
    assert hasattr(flinkie2_TwoOpInt, "operator")
    descriptor = None
    for klass in flinkie2_TwoOpInt.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_flinkie2_declstat_is_not_abstract():
    assert not inspect.isabstract(flinkie2_DeclStat)


def test_flinkie2_declstat_constructor_exists():
    assert callable(flinkie2_DeclStat.__init__)


def test_flinkie2_declstat_constructor_args():
    sig = inspect.signature(flinkie2_DeclStat.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_init_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Init)


def test_flinkie2_init_constructor_exists():
    assert callable(flinkie2_Init.__init__)


def test_flinkie2_init_constructor_args():
    sig = inspect.signature(flinkie2_Init.__init__)
    params = list(sig.parameters.keys())



def test_flinkie2_node_is_not_abstract():
    assert not inspect.isabstract(flinkie2_Node)


def test_flinkie2_node_constructor_exists():
    assert callable(flinkie2_Node.__init__)


def test_flinkie2_node_constructor_args():
    sig = inspect.signature(flinkie2_Node.__init__)
    params = list(sig.parameters.keys())

def test_ecompop_exists():
    # Check that the Enumeration exists
    assert ECompOp is not None

def test_ecompop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ECompOp]
    expected_literals = [
        "LE",
        "NE",
        "GT",
        "LT",
        "EQ",
        "GE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ECompOp"

def test_ebooltwoop_exists():
    # Check that the Enumeration exists
    assert EBoolTwoOp is not None

def test_ebooltwoop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EBoolTwoOp]
    expected_literals = [
        "XOR",
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EBoolTwoOp"

def test_einttwoop_exists():
    # Check that the Enumeration exists
    assert EIntTwoOp is not None

def test_einttwoop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EIntTwoOp]
    expected_literals = [
        "SUB",
        "DIV",
        "ADD",
        "MUL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EIntTwoOp"

def test_eintoneop_exists():
    # Check that the Enumeration exists
    assert EIntOneOp is not None

def test_eintoneop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EIntOneOp]
    expected_literals = [
        "MIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EIntOneOp"

def test_eboolval_exists():
    # Check that the Enumeration exists
    assert EBoolVal is not None

def test_eboolval_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EBoolVal]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EBoolVal"

def test_ebooloneop_exists():
    # Check that the Enumeration exists
    assert EBoolOneOp is not None

def test_ebooloneop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EBoolOneOp]
    expected_literals = [
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EBoolOneOp"


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
flinkie2_Option_strategy = st.builds(
    flinkie2_Option,
    text=
        safe_text
)
flinkie2_BoolExpr_strategy = st.builds(
    flinkie2_BoolExpr,
)
flinkie2_AssignStat_strategy = st.builds(
    flinkie2_AssignStat,
)
Node_strategy = st.builds(
    Node,
)
flinkie2_Question_strategy = st.builds(
    flinkie2_Question,
    text=
        safe_text
)
flinkie2_Message_strategy = st.builds(
    flinkie2_Message,
    text=
        safe_text
)
flinkie2_BooleanEvaluation_strategy = st.builds(
    flinkie2_BooleanEvaluation,
)
flinkie2_Variable_strategy = st.builds(
    flinkie2_Variable,
    name=
        safe_text
)
IntExpr_strategy = st.builds(
    IntExpr,
)
flinkie2_OneOpInt_strategy = st.builds(
    flinkie2_OneOpInt,
    operator=
        safe_text
)
flinkie2_IntExpr_strategy = st.builds(
    flinkie2_IntExpr,
)
BoolExpr_strategy = st.builds(
    BoolExpr,
)
flinkie2_BracExprBool_strategy = st.builds(
    flinkie2_BracExprBool,
)
flinkie2_Comparison_strategy = st.builds(
    flinkie2_Comparison,
    operator=
        safe_text
)
flinkie2_TwoOpBool_strategy = st.builds(
    flinkie2_TwoOpBool,
    operator=
        safe_text
)
flinkie2_BoolVal_strategy = st.builds(
    flinkie2_BoolVal,
    value=
        st.booleans()
)
flinkie2_OneOpBool_strategy = st.builds(
    flinkie2_OneOpBool,
    operator=
        safe_text
)
flinkie2_BracExprInt_strategy = st.builds(
    flinkie2_BracExprInt,
)
flinkie2_FlowChart_strategy = st.builds(
    flinkie2_FlowChart,
)
flinkie2_VariableExpr_strategy = st.builds(
    flinkie2_VariableExpr,
)
flinkie2_Number_strategy = st.builds(
    flinkie2_Number,
    value=
        st.integers()
)
flinkie2_TwoOpInt_strategy = st.builds(
    flinkie2_TwoOpInt,
    operator=
        safe_text
)
flinkie2_DeclStat_strategy = st.builds(
    flinkie2_DeclStat,
)
flinkie2_Init_strategy = st.builds(
    flinkie2_Init,
)
flinkie2_Node_strategy = st.builds(
    flinkie2_Node,
)

@given(instance=flinkie2_Option_strategy)
@settings(max_examples=50)
def test_flinkie2_option_instantiation(instance):
    assert isinstance(instance, flinkie2_Option)



@given(instance=flinkie2_Option_strategy)
def test_flinkie2_option_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=flinkie2_BoolExpr_strategy)
@settings(max_examples=50)
def test_flinkie2_boolexpr_instantiation(instance):
    assert isinstance(instance, flinkie2_BoolExpr)

@given(instance=flinkie2_AssignStat_strategy)
@settings(max_examples=50)
def test_flinkie2_assignstat_instantiation(instance):
    assert isinstance(instance, flinkie2_AssignStat)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=flinkie2_Question_strategy)
@settings(max_examples=50)
def test_flinkie2_question_instantiation(instance):
    assert isinstance(instance, flinkie2_Question)



@given(instance=flinkie2_Question_strategy)
def test_flinkie2_question_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=flinkie2_Message_strategy)
@settings(max_examples=50)
def test_flinkie2_message_instantiation(instance):
    assert isinstance(instance, flinkie2_Message)



@given(instance=flinkie2_Message_strategy)
def test_flinkie2_message_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=flinkie2_BooleanEvaluation_strategy)
@settings(max_examples=50)
def test_flinkie2_booleanevaluation_instantiation(instance):
    assert isinstance(instance, flinkie2_BooleanEvaluation)

@given(instance=flinkie2_Variable_strategy)
@settings(max_examples=50)
def test_flinkie2_variable_instantiation(instance):
    assert isinstance(instance, flinkie2_Variable)



@given(instance=flinkie2_Variable_strategy)
def test_flinkie2_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IntExpr_strategy)
@settings(max_examples=50)
def test_intexpr_instantiation(instance):
    assert isinstance(instance, IntExpr)

@given(instance=flinkie2_OneOpInt_strategy)
@settings(max_examples=50)
def test_flinkie2_oneopint_instantiation(instance):
    assert isinstance(instance, flinkie2_OneOpInt)



@given(instance=flinkie2_OneOpInt_strategy)
def test_flinkie2_oneopint_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=flinkie2_IntExpr_strategy)
@settings(max_examples=50)
def test_flinkie2_intexpr_instantiation(instance):
    assert isinstance(instance, flinkie2_IntExpr)

@given(instance=BoolExpr_strategy)
@settings(max_examples=50)
def test_boolexpr_instantiation(instance):
    assert isinstance(instance, BoolExpr)

@given(instance=flinkie2_BracExprBool_strategy)
@settings(max_examples=50)
def test_flinkie2_bracexprbool_instantiation(instance):
    assert isinstance(instance, flinkie2_BracExprBool)

@given(instance=flinkie2_Comparison_strategy)
@settings(max_examples=50)
def test_flinkie2_comparison_instantiation(instance):
    assert isinstance(instance, flinkie2_Comparison)



@given(instance=flinkie2_Comparison_strategy)
def test_flinkie2_comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=flinkie2_TwoOpBool_strategy)
@settings(max_examples=50)
def test_flinkie2_twoopbool_instantiation(instance):
    assert isinstance(instance, flinkie2_TwoOpBool)



@given(instance=flinkie2_TwoOpBool_strategy)
def test_flinkie2_twoopbool_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=flinkie2_BoolVal_strategy)
@settings(max_examples=50)
def test_flinkie2_boolval_instantiation(instance):
    assert isinstance(instance, flinkie2_BoolVal)



@given(instance=flinkie2_BoolVal_strategy)
def test_flinkie2_boolval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flinkie2_OneOpBool_strategy)
@settings(max_examples=50)
def test_flinkie2_oneopbool_instantiation(instance):
    assert isinstance(instance, flinkie2_OneOpBool)



@given(instance=flinkie2_OneOpBool_strategy)
def test_flinkie2_oneopbool_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=flinkie2_BracExprInt_strategy)
@settings(max_examples=50)
def test_flinkie2_bracexprint_instantiation(instance):
    assert isinstance(instance, flinkie2_BracExprInt)

@given(instance=flinkie2_FlowChart_strategy)
@settings(max_examples=50)
def test_flinkie2_flowchart_instantiation(instance):
    assert isinstance(instance, flinkie2_FlowChart)

@given(instance=flinkie2_VariableExpr_strategy)
@settings(max_examples=50)
def test_flinkie2_variableexpr_instantiation(instance):
    assert isinstance(instance, flinkie2_VariableExpr)

@given(instance=flinkie2_Number_strategy)
@settings(max_examples=50)
def test_flinkie2_number_instantiation(instance):
    assert isinstance(instance, flinkie2_Number)



@given(instance=flinkie2_Number_strategy)
def test_flinkie2_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flinkie2_TwoOpInt_strategy)
@settings(max_examples=50)
def test_flinkie2_twoopint_instantiation(instance):
    assert isinstance(instance, flinkie2_TwoOpInt)



@given(instance=flinkie2_TwoOpInt_strategy)
def test_flinkie2_twoopint_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=flinkie2_DeclStat_strategy)
@settings(max_examples=50)
def test_flinkie2_declstat_instantiation(instance):
    assert isinstance(instance, flinkie2_DeclStat)

@given(instance=flinkie2_Init_strategy)
@settings(max_examples=50)
def test_flinkie2_init_instantiation(instance):
    assert isinstance(instance, flinkie2_Init)

@given(instance=flinkie2_Node_strategy)
@settings(max_examples=50)
def test_flinkie2_node_instantiation(instance):
    assert isinstance(instance, flinkie2_Node)
