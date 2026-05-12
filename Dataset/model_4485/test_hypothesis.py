import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    kmLogo_Expression,
    Primitive,
    kmLogo_Forward,
    kmLogo_Back,
    Instruction,
    kmLogo_Primitive,
    kmLogo_Instruction,
    kmLogo_VarDecl,
    kmLogo_LogoProgram,
    Literal,
    kmLogo_BoolLit,
    kmLogo_StringLit,
    kmLogo_IntegerLit,
    Expression,
    kmLogo_RelationalExpression,
    kmLogo_ArithmeticExpression,
    kmLogo_VarReference,
    kmLogo_Literal,
    kmLogo_Clear,
    kmLogo_PenUp,
    kmLogo_PenDown,
    kmLogo_Right,
    kmLogo_Left,
    ArithmeticOperator,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kmlogo_expression_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Expression)


def test_kmlogo_expression_constructor_exists():
    assert callable(kmLogo_Expression.__init__)


def test_kmlogo_expression_constructor_args():
    sig = inspect.signature(kmLogo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_forward_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Forward)


def test_kmlogo_forward_constructor_exists():
    assert callable(kmLogo_Forward.__init__)


def test_kmlogo_forward_constructor_args():
    sig = inspect.signature(kmLogo_Forward.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_back_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Back)


def test_kmlogo_back_constructor_exists():
    assert callable(kmLogo_Back.__init__)


def test_kmlogo_back_constructor_args():
    sig = inspect.signature(kmLogo_Back.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_primitive_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Primitive)


def test_kmlogo_primitive_constructor_exists():
    assert callable(kmLogo_Primitive.__init__)


def test_kmlogo_primitive_constructor_args():
    sig = inspect.signature(kmLogo_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_instruction_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Instruction)


def test_kmlogo_instruction_constructor_exists():
    assert callable(kmLogo_Instruction.__init__)


def test_kmlogo_instruction_constructor_args():
    sig = inspect.signature(kmLogo_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_vardecl_is_not_abstract():
    assert not inspect.isabstract(kmLogo_VarDecl)


def test_kmlogo_vardecl_constructor_exists():
    assert callable(kmLogo_VarDecl.__init__)


def test_kmlogo_vardecl_constructor_args():
    sig = inspect.signature(kmLogo_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_kmlogo_vardecl_has_key():
    assert hasattr(kmLogo_VarDecl, "key")
    descriptor = None
    for klass in kmLogo_VarDecl.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo_logoprogram_is_not_abstract():
    assert not inspect.isabstract(kmLogo_LogoProgram)


def test_kmlogo_logoprogram_constructor_exists():
    assert callable(kmLogo_LogoProgram.__init__)


def test_kmlogo_logoprogram_constructor_args():
    sig = inspect.signature(kmLogo_LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_boollit_is_not_abstract():
    assert not inspect.isabstract(kmLogo_BoolLit)


def test_kmlogo_boollit_constructor_exists():
    assert callable(kmLogo_BoolLit.__init__)


def test_kmlogo_boollit_constructor_args():
    sig = inspect.signature(kmLogo_BoolLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kmlogo_boollit_has_value():
    assert hasattr(kmLogo_BoolLit, "value")
    descriptor = None
    for klass in kmLogo_BoolLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo_stringlit_is_not_abstract():
    assert not inspect.isabstract(kmLogo_StringLit)


def test_kmlogo_stringlit_constructor_exists():
    assert callable(kmLogo_StringLit.__init__)


def test_kmlogo_stringlit_constructor_args():
    sig = inspect.signature(kmLogo_StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kmlogo_stringlit_has_value():
    assert hasattr(kmLogo_StringLit, "value")
    descriptor = None
    for klass in kmLogo_StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo_integerlit_is_not_abstract():
    assert not inspect.isabstract(kmLogo_IntegerLit)


def test_kmlogo_integerlit_constructor_exists():
    assert callable(kmLogo_IntegerLit.__init__)


def test_kmlogo_integerlit_constructor_args():
    sig = inspect.signature(kmLogo_IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kmlogo_integerlit_has_value():
    assert hasattr(kmLogo_IntegerLit, "value")
    descriptor = None
    for klass in kmLogo_IntegerLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(kmLogo_RelationalExpression)


def test_kmlogo_relationalexpression_constructor_exists():
    assert callable(kmLogo_RelationalExpression.__init__)


def test_kmlogo_relationalexpression_constructor_args():
    sig = inspect.signature(kmLogo_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_kmlogo_relationalexpression_has_operator():
    assert hasattr(kmLogo_RelationalExpression, "operator")
    descriptor = None
    for klass in kmLogo_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(kmLogo_ArithmeticExpression)


def test_kmlogo_arithmeticexpression_constructor_exists():
    assert callable(kmLogo_ArithmeticExpression.__init__)


def test_kmlogo_arithmeticexpression_constructor_args():
    sig = inspect.signature(kmLogo_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_kmlogo_arithmeticexpression_has_operator():
    assert hasattr(kmLogo_ArithmeticExpression, "operator")
    descriptor = None
    for klass in kmLogo_ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo_varreference_is_not_abstract():
    assert not inspect.isabstract(kmLogo_VarReference)


def test_kmlogo_varreference_constructor_exists():
    assert callable(kmLogo_VarReference.__init__)


def test_kmlogo_varreference_constructor_args():
    sig = inspect.signature(kmLogo_VarReference.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_kmlogo_varreference_has_key():
    assert hasattr(kmLogo_VarReference, "key")
    descriptor = None
    for klass in kmLogo_VarReference.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo_literal_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Literal)


def test_kmlogo_literal_constructor_exists():
    assert callable(kmLogo_Literal.__init__)


def test_kmlogo_literal_constructor_args():
    sig = inspect.signature(kmLogo_Literal.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_clear_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Clear)


def test_kmlogo_clear_constructor_exists():
    assert callable(kmLogo_Clear.__init__)


def test_kmlogo_clear_constructor_args():
    sig = inspect.signature(kmLogo_Clear.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_penup_is_not_abstract():
    assert not inspect.isabstract(kmLogo_PenUp)


def test_kmlogo_penup_constructor_exists():
    assert callable(kmLogo_PenUp.__init__)


def test_kmlogo_penup_constructor_args():
    sig = inspect.signature(kmLogo_PenUp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_pendown_is_not_abstract():
    assert not inspect.isabstract(kmLogo_PenDown)


def test_kmlogo_pendown_constructor_exists():
    assert callable(kmLogo_PenDown.__init__)


def test_kmlogo_pendown_constructor_args():
    sig = inspect.signature(kmLogo_PenDown.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_right_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Right)


def test_kmlogo_right_constructor_exists():
    assert callable(kmLogo_Right.__init__)


def test_kmlogo_right_constructor_args():
    sig = inspect.signature(kmLogo_Right.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_left_is_not_abstract():
    assert not inspect.isabstract(kmLogo_Left)


def test_kmlogo_left_constructor_exists():
    assert callable(kmLogo_Left.__init__)


def test_kmlogo_left_constructor_args():
    sig = inspect.signature(kmLogo_Left.__init__)
    params = list(sig.parameters.keys())

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "div",
        "plus",
        "mult",
        "minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "greaterThan",
        "lessThan",
        "equals",
        "greaterThanOrEqualTo",
        "notEqual",
        "lessThanOrEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
kmLogo_Expression_strategy = st.builds(
    kmLogo_Expression,
)
Primitive_strategy = st.builds(
    Primitive,
)
kmLogo_Forward_strategy = st.builds(
    kmLogo_Forward,
)
kmLogo_Back_strategy = st.builds(
    kmLogo_Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
kmLogo_Primitive_strategy = st.builds(
    kmLogo_Primitive,
)
kmLogo_Instruction_strategy = st.builds(
    kmLogo_Instruction,
)
kmLogo_VarDecl_strategy = st.builds(
    kmLogo_VarDecl,
    key=
        safe_text
)
kmLogo_LogoProgram_strategy = st.builds(
    kmLogo_LogoProgram,
)
Literal_strategy = st.builds(
    Literal,
)
kmLogo_BoolLit_strategy = st.builds(
    kmLogo_BoolLit,
    value=
        st.booleans()
)
kmLogo_StringLit_strategy = st.builds(
    kmLogo_StringLit,
    value=
        safe_text
)
kmLogo_IntegerLit_strategy = st.builds(
    kmLogo_IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
kmLogo_RelationalExpression_strategy = st.builds(
    kmLogo_RelationalExpression,
    operator=
        safe_text
)
kmLogo_ArithmeticExpression_strategy = st.builds(
    kmLogo_ArithmeticExpression,
    operator=
        safe_text
)
kmLogo_VarReference_strategy = st.builds(
    kmLogo_VarReference,
    key=
        safe_text
)
kmLogo_Literal_strategy = st.builds(
    kmLogo_Literal,
)
kmLogo_Clear_strategy = st.builds(
    kmLogo_Clear,
)
kmLogo_PenUp_strategy = st.builds(
    kmLogo_PenUp,
)
kmLogo_PenDown_strategy = st.builds(
    kmLogo_PenDown,
)
kmLogo_Right_strategy = st.builds(
    kmLogo_Right,
)
kmLogo_Left_strategy = st.builds(
    kmLogo_Left,
)

@given(instance=kmLogo_Expression_strategy)
@settings(max_examples=50)
def test_kmlogo_expression_instantiation(instance):
    assert isinstance(instance, kmLogo_Expression)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=kmLogo_Forward_strategy)
@settings(max_examples=50)
def test_kmlogo_forward_instantiation(instance):
    assert isinstance(instance, kmLogo_Forward)

@given(instance=kmLogo_Back_strategy)
@settings(max_examples=50)
def test_kmlogo_back_instantiation(instance):
    assert isinstance(instance, kmLogo_Back)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=kmLogo_Primitive_strategy)
@settings(max_examples=50)
def test_kmlogo_primitive_instantiation(instance):
    assert isinstance(instance, kmLogo_Primitive)

@given(instance=kmLogo_Instruction_strategy)
@settings(max_examples=50)
def test_kmlogo_instruction_instantiation(instance):
    assert isinstance(instance, kmLogo_Instruction)

@given(instance=kmLogo_VarDecl_strategy)
@settings(max_examples=50)
def test_kmlogo_vardecl_instantiation(instance):
    assert isinstance(instance, kmLogo_VarDecl)



@given(instance=kmLogo_VarDecl_strategy)
def test_kmlogo_vardecl_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=kmLogo_LogoProgram_strategy)
@settings(max_examples=50)
def test_kmlogo_logoprogram_instantiation(instance):
    assert isinstance(instance, kmLogo_LogoProgram)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=kmLogo_BoolLit_strategy)
@settings(max_examples=50)
def test_kmlogo_boollit_instantiation(instance):
    assert isinstance(instance, kmLogo_BoolLit)



@given(instance=kmLogo_BoolLit_strategy)
def test_kmlogo_boollit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kmLogo_StringLit_strategy)
@settings(max_examples=50)
def test_kmlogo_stringlit_instantiation(instance):
    assert isinstance(instance, kmLogo_StringLit)



@given(instance=kmLogo_StringLit_strategy)
def test_kmlogo_stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kmLogo_IntegerLit_strategy)
@settings(max_examples=50)
def test_kmlogo_integerlit_instantiation(instance):
    assert isinstance(instance, kmLogo_IntegerLit)



@given(instance=kmLogo_IntegerLit_strategy)
def test_kmlogo_integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=kmLogo_RelationalExpression_strategy)
@settings(max_examples=50)
def test_kmlogo_relationalexpression_instantiation(instance):
    assert isinstance(instance, kmLogo_RelationalExpression)



@given(instance=kmLogo_RelationalExpression_strategy)
def test_kmlogo_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=kmLogo_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_kmlogo_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, kmLogo_ArithmeticExpression)



@given(instance=kmLogo_ArithmeticExpression_strategy)
def test_kmlogo_arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=kmLogo_VarReference_strategy)
@settings(max_examples=50)
def test_kmlogo_varreference_instantiation(instance):
    assert isinstance(instance, kmLogo_VarReference)



@given(instance=kmLogo_VarReference_strategy)
def test_kmlogo_varreference_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=kmLogo_Literal_strategy)
@settings(max_examples=50)
def test_kmlogo_literal_instantiation(instance):
    assert isinstance(instance, kmLogo_Literal)

@given(instance=kmLogo_Clear_strategy)
@settings(max_examples=50)
def test_kmlogo_clear_instantiation(instance):
    assert isinstance(instance, kmLogo_Clear)

@given(instance=kmLogo_PenUp_strategy)
@settings(max_examples=50)
def test_kmlogo_penup_instantiation(instance):
    assert isinstance(instance, kmLogo_PenUp)

@given(instance=kmLogo_PenDown_strategy)
@settings(max_examples=50)
def test_kmlogo_pendown_instantiation(instance):
    assert isinstance(instance, kmLogo_PenDown)

@given(instance=kmLogo_Right_strategy)
@settings(max_examples=50)
def test_kmlogo_right_instantiation(instance):
    assert isinstance(instance, kmLogo_Right)

@given(instance=kmLogo_Left_strategy)
@settings(max_examples=50)
def test_kmlogo_left_instantiation(instance):
    assert isinstance(instance, kmLogo_Left)
