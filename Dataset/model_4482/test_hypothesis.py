import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinaryExpr,
    Logo_BooleanExpr,
    Logo_ArithmeticExpr,
    ControlStructure,
    Logo_Block,
    Logo_While,
    Logo_If,
    Logo_Instruction,
    Logo_LogoProgram,
    Literal,
    Logo_Double,
    Logo_Void,
    Logo_Boolean,
    Logo_String,
    Logo_Integer,
    Expression,
    Logo_BinaryExpr,
    Logo_ProcedureCall,
    Logo_VarReference,
    Logo_Literal,
    Primitive,
    Logo_Left,
    Logo_Right,
    Logo_Back,
    Logo_Forward,
    Instruction,
    Logo_ControlStructure,
    Logo_Assignation,
    Logo_VarDecl,
    Logo_Expression,
    Logo_Procedure,
    Logo_Primitive,
    BooleanOperator,
    ArithmeticOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexpr_is_not_abstract():
    assert not inspect.isabstract(BinaryExpr)


def test_binaryexpr_constructor_exists():
    assert callable(BinaryExpr.__init__)


def test_binaryexpr_constructor_args():
    sig = inspect.signature(BinaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_logo_booleanexpr_is_not_abstract():
    assert not inspect.isabstract(Logo_BooleanExpr)


def test_logo_booleanexpr_constructor_exists():
    assert callable(Logo_BooleanExpr.__init__)


def test_logo_booleanexpr_constructor_args():
    sig = inspect.signature(Logo_BooleanExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_logo_booleanexpr_has_operator():
    assert hasattr(Logo_BooleanExpr, "operator")
    descriptor = None
    for klass in Logo_BooleanExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_logo_arithmeticexpr_is_not_abstract():
    assert not inspect.isabstract(Logo_ArithmeticExpr)


def test_logo_arithmeticexpr_constructor_exists():
    assert callable(Logo_ArithmeticExpr.__init__)


def test_logo_arithmeticexpr_constructor_args():
    sig = inspect.signature(Logo_ArithmeticExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_logo_arithmeticexpr_has_operator():
    assert hasattr(Logo_ArithmeticExpr, "operator")
    descriptor = None
    for klass in Logo_ArithmeticExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_logo_block_is_not_abstract():
    assert not inspect.isabstract(Logo_Block)


def test_logo_block_constructor_exists():
    assert callable(Logo_Block.__init__)


def test_logo_block_constructor_args():
    sig = inspect.signature(Logo_Block.__init__)
    params = list(sig.parameters.keys())



def test_logo_while_is_not_abstract():
    assert not inspect.isabstract(Logo_While)


def test_logo_while_constructor_exists():
    assert callable(Logo_While.__init__)


def test_logo_while_constructor_args():
    sig = inspect.signature(Logo_While.__init__)
    params = list(sig.parameters.keys())



def test_logo_if_is_not_abstract():
    assert not inspect.isabstract(Logo_If)


def test_logo_if_constructor_exists():
    assert callable(Logo_If.__init__)


def test_logo_if_constructor_args():
    sig = inspect.signature(Logo_If.__init__)
    params = list(sig.parameters.keys())



def test_logo_instruction_is_not_abstract():
    assert not inspect.isabstract(Logo_Instruction)


def test_logo_instruction_constructor_exists():
    assert callable(Logo_Instruction.__init__)


def test_logo_instruction_constructor_args():
    sig = inspect.signature(Logo_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo_logoprogram_is_not_abstract():
    assert not inspect.isabstract(Logo_LogoProgram)


def test_logo_logoprogram_constructor_exists():
    assert callable(Logo_LogoProgram.__init__)


def test_logo_logoprogram_constructor_args():
    sig = inspect.signature(Logo_LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_logo_double_is_not_abstract():
    assert not inspect.isabstract(Logo_Double)


def test_logo_double_constructor_exists():
    assert callable(Logo_Double.__init__)


def test_logo_double_constructor_args():
    sig = inspect.signature(Logo_Double.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_double_has_value():
    assert hasattr(Logo_Double, "value")
    descriptor = None
    for klass in Logo_Double.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo_void_is_not_abstract():
    assert not inspect.isabstract(Logo_Void)


def test_logo_void_constructor_exists():
    assert callable(Logo_Void.__init__)


def test_logo_void_constructor_args():
    sig = inspect.signature(Logo_Void.__init__)
    params = list(sig.parameters.keys())



def test_logo_boolean_is_not_abstract():
    assert not inspect.isabstract(Logo_Boolean)


def test_logo_boolean_constructor_exists():
    assert callable(Logo_Boolean.__init__)


def test_logo_boolean_constructor_args():
    sig = inspect.signature(Logo_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_boolean_has_value():
    assert hasattr(Logo_Boolean, "value")
    descriptor = None
    for klass in Logo_Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo_string_is_not_abstract():
    assert not inspect.isabstract(Logo_String)


def test_logo_string_constructor_exists():
    assert callable(Logo_String.__init__)


def test_logo_string_constructor_args():
    sig = inspect.signature(Logo_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_string_has_value():
    assert hasattr(Logo_String, "value")
    descriptor = None
    for klass in Logo_String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo_integer_is_not_abstract():
    assert not inspect.isabstract(Logo_Integer)


def test_logo_integer_constructor_exists():
    assert callable(Logo_Integer.__init__)


def test_logo_integer_constructor_args():
    sig = inspect.signature(Logo_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_integer_has_value():
    assert hasattr(Logo_Integer, "value")
    descriptor = None
    for klass in Logo_Integer.__mro__:
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



def test_logo_binaryexpr_is_not_abstract():
    assert not inspect.isabstract(Logo_BinaryExpr)


def test_logo_binaryexpr_constructor_exists():
    assert callable(Logo_BinaryExpr.__init__)


def test_logo_binaryexpr_constructor_args():
    sig = inspect.signature(Logo_BinaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_logo_procedurecall_is_not_abstract():
    assert not inspect.isabstract(Logo_ProcedureCall)


def test_logo_procedurecall_constructor_exists():
    assert callable(Logo_ProcedureCall.__init__)


def test_logo_procedurecall_constructor_args():
    sig = inspect.signature(Logo_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_logo_varreference_is_not_abstract():
    assert not inspect.isabstract(Logo_VarReference)


def test_logo_varreference_constructor_exists():
    assert callable(Logo_VarReference.__init__)


def test_logo_varreference_constructor_args():
    sig = inspect.signature(Logo_VarReference.__init__)
    params = list(sig.parameters.keys())



def test_logo_literal_is_not_abstract():
    assert not inspect.isabstract(Logo_Literal)


def test_logo_literal_constructor_exists():
    assert callable(Logo_Literal.__init__)


def test_logo_literal_constructor_args():
    sig = inspect.signature(Logo_Literal.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logo_left_is_not_abstract():
    assert not inspect.isabstract(Logo_Left)


def test_logo_left_constructor_exists():
    assert callable(Logo_Left.__init__)


def test_logo_left_constructor_args():
    sig = inspect.signature(Logo_Left.__init__)
    params = list(sig.parameters.keys())



def test_logo_right_is_not_abstract():
    assert not inspect.isabstract(Logo_Right)


def test_logo_right_constructor_exists():
    assert callable(Logo_Right.__init__)


def test_logo_right_constructor_args():
    sig = inspect.signature(Logo_Right.__init__)
    params = list(sig.parameters.keys())



def test_logo_back_is_not_abstract():
    assert not inspect.isabstract(Logo_Back)


def test_logo_back_constructor_exists():
    assert callable(Logo_Back.__init__)


def test_logo_back_constructor_args():
    sig = inspect.signature(Logo_Back.__init__)
    params = list(sig.parameters.keys())



def test_logo_forward_is_not_abstract():
    assert not inspect.isabstract(Logo_Forward)


def test_logo_forward_constructor_exists():
    assert callable(Logo_Forward.__init__)


def test_logo_forward_constructor_args():
    sig = inspect.signature(Logo_Forward.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo_controlstructure_is_not_abstract():
    assert not inspect.isabstract(Logo_ControlStructure)


def test_logo_controlstructure_constructor_exists():
    assert callable(Logo_ControlStructure.__init__)


def test_logo_controlstructure_constructor_args():
    sig = inspect.signature(Logo_ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_logo_assignation_is_not_abstract():
    assert not inspect.isabstract(Logo_Assignation)


def test_logo_assignation_constructor_exists():
    assert callable(Logo_Assignation.__init__)


def test_logo_assignation_constructor_args():
    sig = inspect.signature(Logo_Assignation.__init__)
    params = list(sig.parameters.keys())



def test_logo_vardecl_is_not_abstract():
    assert not inspect.isabstract(Logo_VarDecl)


def test_logo_vardecl_constructor_exists():
    assert callable(Logo_VarDecl.__init__)


def test_logo_vardecl_constructor_args():
    sig = inspect.signature(Logo_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_vardecl_has_name():
    assert hasattr(Logo_VarDecl, "name")
    descriptor = None
    for klass in Logo_VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_expression_is_not_abstract():
    assert not inspect.isabstract(Logo_Expression)


def test_logo_expression_constructor_exists():
    assert callable(Logo_Expression.__init__)


def test_logo_expression_constructor_args():
    sig = inspect.signature(Logo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_logo_procedure_is_not_abstract():
    assert not inspect.isabstract(Logo_Procedure)


def test_logo_procedure_constructor_exists():
    assert callable(Logo_Procedure.__init__)


def test_logo_procedure_constructor_args():
    sig = inspect.signature(Logo_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_procedure_has_name():
    assert hasattr(Logo_Procedure, "name")
    descriptor = None
    for klass in Logo_Procedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_primitive_is_not_abstract():
    assert not inspect.isabstract(Logo_Primitive)


def test_logo_primitive_constructor_exists():
    assert callable(Logo_Primitive.__init__)


def test_logo_primitive_constructor_args():
    sig = inspect.signature(Logo_Primitive.__init__)
    params = list(sig.parameters.keys())

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "diff",
        "equal",
        "greaterThan",
        "lowerThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "mult",
        "plus",
        "div",
        "minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"


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
BinaryExpr_strategy = st.builds(
    BinaryExpr,
)
Logo_BooleanExpr_strategy = st.builds(
    Logo_BooleanExpr,
    operator=
        safe_text
)
Logo_ArithmeticExpr_strategy = st.builds(
    Logo_ArithmeticExpr,
    operator=
        safe_text
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
Logo_Block_strategy = st.builds(
    Logo_Block,
)
Logo_While_strategy = st.builds(
    Logo_While,
)
Logo_If_strategy = st.builds(
    Logo_If,
)
Logo_Instruction_strategy = st.builds(
    Logo_Instruction,
)
Logo_LogoProgram_strategy = st.builds(
    Logo_LogoProgram,
)
Literal_strategy = st.builds(
    Literal,
)
Logo_Double_strategy = st.builds(
    Logo_Double,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Logo_Void_strategy = st.builds(
    Logo_Void,
)
Logo_Boolean_strategy = st.builds(
    Logo_Boolean,
    value=
        st.booleans()
)
Logo_String_strategy = st.builds(
    Logo_String,
    value=
        safe_text
)
Logo_Integer_strategy = st.builds(
    Logo_Integer,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
Logo_BinaryExpr_strategy = st.builds(
    Logo_BinaryExpr,
)
Logo_ProcedureCall_strategy = st.builds(
    Logo_ProcedureCall,
)
Logo_VarReference_strategy = st.builds(
    Logo_VarReference,
)
Logo_Literal_strategy = st.builds(
    Logo_Literal,
)
Primitive_strategy = st.builds(
    Primitive,
)
Logo_Left_strategy = st.builds(
    Logo_Left,
)
Logo_Right_strategy = st.builds(
    Logo_Right,
)
Logo_Back_strategy = st.builds(
    Logo_Back,
)
Logo_Forward_strategy = st.builds(
    Logo_Forward,
)
Instruction_strategy = st.builds(
    Instruction,
)
Logo_ControlStructure_strategy = st.builds(
    Logo_ControlStructure,
)
Logo_Assignation_strategy = st.builds(
    Logo_Assignation,
)
Logo_VarDecl_strategy = st.builds(
    Logo_VarDecl,
    name=
        safe_text
)
Logo_Expression_strategy = st.builds(
    Logo_Expression,
)
Logo_Procedure_strategy = st.builds(
    Logo_Procedure,
    name=
        safe_text
)
Logo_Primitive_strategy = st.builds(
    Logo_Primitive,
)

@given(instance=BinaryExpr_strategy)
@settings(max_examples=50)
def test_binaryexpr_instantiation(instance):
    assert isinstance(instance, BinaryExpr)

@given(instance=Logo_BooleanExpr_strategy)
@settings(max_examples=50)
def test_logo_booleanexpr_instantiation(instance):
    assert isinstance(instance, Logo_BooleanExpr)



@given(instance=Logo_BooleanExpr_strategy)
def test_logo_booleanexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Logo_ArithmeticExpr_strategy)
@settings(max_examples=50)
def test_logo_arithmeticexpr_instantiation(instance):
    assert isinstance(instance, Logo_ArithmeticExpr)



@given(instance=Logo_ArithmeticExpr_strategy)
def test_logo_arithmeticexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=Logo_Block_strategy)
@settings(max_examples=50)
def test_logo_block_instantiation(instance):
    assert isinstance(instance, Logo_Block)

@given(instance=Logo_While_strategy)
@settings(max_examples=50)
def test_logo_while_instantiation(instance):
    assert isinstance(instance, Logo_While)

@given(instance=Logo_If_strategy)
@settings(max_examples=50)
def test_logo_if_instantiation(instance):
    assert isinstance(instance, Logo_If)

@given(instance=Logo_Instruction_strategy)
@settings(max_examples=50)
def test_logo_instruction_instantiation(instance):
    assert isinstance(instance, Logo_Instruction)

@given(instance=Logo_LogoProgram_strategy)
@settings(max_examples=50)
def test_logo_logoprogram_instantiation(instance):
    assert isinstance(instance, Logo_LogoProgram)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=Logo_Double_strategy)
@settings(max_examples=50)
def test_logo_double_instantiation(instance):
    assert isinstance(instance, Logo_Double)



@given(instance=Logo_Double_strategy)
def test_logo_double_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Logo_Void_strategy)
@settings(max_examples=50)
def test_logo_void_instantiation(instance):
    assert isinstance(instance, Logo_Void)

@given(instance=Logo_Boolean_strategy)
@settings(max_examples=50)
def test_logo_boolean_instantiation(instance):
    assert isinstance(instance, Logo_Boolean)



@given(instance=Logo_Boolean_strategy)
def test_logo_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Logo_String_strategy)
@settings(max_examples=50)
def test_logo_string_instantiation(instance):
    assert isinstance(instance, Logo_String)



@given(instance=Logo_String_strategy)
def test_logo_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Logo_Integer_strategy)
@settings(max_examples=50)
def test_logo_integer_instantiation(instance):
    assert isinstance(instance, Logo_Integer)



@given(instance=Logo_Integer_strategy)
def test_logo_integer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Logo_BinaryExpr_strategy)
@settings(max_examples=50)
def test_logo_binaryexpr_instantiation(instance):
    assert isinstance(instance, Logo_BinaryExpr)

@given(instance=Logo_ProcedureCall_strategy)
@settings(max_examples=50)
def test_logo_procedurecall_instantiation(instance):
    assert isinstance(instance, Logo_ProcedureCall)

@given(instance=Logo_VarReference_strategy)
@settings(max_examples=50)
def test_logo_varreference_instantiation(instance):
    assert isinstance(instance, Logo_VarReference)

@given(instance=Logo_Literal_strategy)
@settings(max_examples=50)
def test_logo_literal_instantiation(instance):
    assert isinstance(instance, Logo_Literal)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=Logo_Left_strategy)
@settings(max_examples=50)
def test_logo_left_instantiation(instance):
    assert isinstance(instance, Logo_Left)

@given(instance=Logo_Right_strategy)
@settings(max_examples=50)
def test_logo_right_instantiation(instance):
    assert isinstance(instance, Logo_Right)

@given(instance=Logo_Back_strategy)
@settings(max_examples=50)
def test_logo_back_instantiation(instance):
    assert isinstance(instance, Logo_Back)

@given(instance=Logo_Forward_strategy)
@settings(max_examples=50)
def test_logo_forward_instantiation(instance):
    assert isinstance(instance, Logo_Forward)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=Logo_ControlStructure_strategy)
@settings(max_examples=50)
def test_logo_controlstructure_instantiation(instance):
    assert isinstance(instance, Logo_ControlStructure)

@given(instance=Logo_Assignation_strategy)
@settings(max_examples=50)
def test_logo_assignation_instantiation(instance):
    assert isinstance(instance, Logo_Assignation)

@given(instance=Logo_VarDecl_strategy)
@settings(max_examples=50)
def test_logo_vardecl_instantiation(instance):
    assert isinstance(instance, Logo_VarDecl)



@given(instance=Logo_VarDecl_strategy)
def test_logo_vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Logo_Expression_strategy)
@settings(max_examples=50)
def test_logo_expression_instantiation(instance):
    assert isinstance(instance, Logo_Expression)

@given(instance=Logo_Procedure_strategy)
@settings(max_examples=50)
def test_logo_procedure_instantiation(instance):
    assert isinstance(instance, Logo_Procedure)



@given(instance=Logo_Procedure_strategy)
def test_logo_procedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Logo_Primitive_strategy)
@settings(max_examples=50)
def test_logo_primitive_instantiation(instance):
    assert isinstance(instance, Logo_Primitive)
