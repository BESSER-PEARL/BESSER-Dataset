import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExpr,
    Logo::BooleanExpr,
    Logo::ArithmeticExpr,
    ControlStructure,
    Logo::While,
    Logo::Block,
    Logo::If,
    Logo::Instruction,
    Logo::LogoProgram,
    Literal,
    Logo::String,
    Logo::Boolean,
    Logo::Double,
    Logo::Void,
    Logo::Integer,
    Expression,
    Logo::ProcedureCall,
    Logo::BinaryExpr,
    Logo::VarReference,
    Logo::Literal,
    Primitive,
    Logo::Right,
    Logo::Back,
    Logo::Left,
    Logo::Forward,
    Instruction,
    Logo::VarDecl,
    Logo::ControlStructure,
    Logo::Procedure,
    Logo::Assignation,
    Logo::Expression,
    Logo::Primitive,
    ArithmeticOperator,
    BooleanOperator,
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



def test_logo::booleanexpr_is_not_abstract():
    assert not inspect.isabstract(Logo::BooleanExpr)


def test_logo::booleanexpr_constructor_exists():
    assert callable(Logo::BooleanExpr.__init__)


def test_logo::booleanexpr_constructor_args():
    sig = inspect.signature(Logo::BooleanExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_logo::booleanexpr_has_operator():
    assert hasattr(Logo::BooleanExpr, "operator")
    descriptor = None
    for klass in Logo::BooleanExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_logo::arithmeticexpr_is_not_abstract():
    assert not inspect.isabstract(Logo::ArithmeticExpr)


def test_logo::arithmeticexpr_constructor_exists():
    assert callable(Logo::ArithmeticExpr.__init__)


def test_logo::arithmeticexpr_constructor_args():
    sig = inspect.signature(Logo::ArithmeticExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_logo::arithmeticexpr_has_operator():
    assert hasattr(Logo::ArithmeticExpr, "operator")
    descriptor = None
    for klass in Logo::ArithmeticExpr.__mro__:
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



def test_logo::while_is_not_abstract():
    assert not inspect.isabstract(Logo::While)


def test_logo::while_constructor_exists():
    assert callable(Logo::While.__init__)


def test_logo::while_constructor_args():
    sig = inspect.signature(Logo::While.__init__)
    params = list(sig.parameters.keys())



def test_logo::block_is_not_abstract():
    assert not inspect.isabstract(Logo::Block)


def test_logo::block_constructor_exists():
    assert callable(Logo::Block.__init__)


def test_logo::block_constructor_args():
    sig = inspect.signature(Logo::Block.__init__)
    params = list(sig.parameters.keys())



def test_logo::if_is_not_abstract():
    assert not inspect.isabstract(Logo::If)


def test_logo::if_constructor_exists():
    assert callable(Logo::If.__init__)


def test_logo::if_constructor_args():
    sig = inspect.signature(Logo::If.__init__)
    params = list(sig.parameters.keys())



def test_logo::instruction_is_not_abstract():
    assert not inspect.isabstract(Logo::Instruction)


def test_logo::instruction_constructor_exists():
    assert callable(Logo::Instruction.__init__)


def test_logo::instruction_constructor_args():
    sig = inspect.signature(Logo::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo::logoprogram_is_not_abstract():
    assert not inspect.isabstract(Logo::LogoProgram)


def test_logo::logoprogram_constructor_exists():
    assert callable(Logo::LogoProgram.__init__)


def test_logo::logoprogram_constructor_args():
    sig = inspect.signature(Logo::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_logo::string_is_not_abstract():
    assert not inspect.isabstract(Logo::String)


def test_logo::string_constructor_exists():
    assert callable(Logo::String.__init__)


def test_logo::string_constructor_args():
    sig = inspect.signature(Logo::String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::string_has_value():
    assert hasattr(Logo::String, "value")
    descriptor = None
    for klass in Logo::String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo::boolean_is_not_abstract():
    assert not inspect.isabstract(Logo::Boolean)


def test_logo::boolean_constructor_exists():
    assert callable(Logo::Boolean.__init__)


def test_logo::boolean_constructor_args():
    sig = inspect.signature(Logo::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::boolean_has_value():
    assert hasattr(Logo::Boolean, "value")
    descriptor = None
    for klass in Logo::Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo::double_is_not_abstract():
    assert not inspect.isabstract(Logo::Double)


def test_logo::double_constructor_exists():
    assert callable(Logo::Double.__init__)


def test_logo::double_constructor_args():
    sig = inspect.signature(Logo::Double.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::double_has_value():
    assert hasattr(Logo::Double, "value")
    descriptor = None
    for klass in Logo::Double.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo::void_is_not_abstract():
    assert not inspect.isabstract(Logo::Void)


def test_logo::void_constructor_exists():
    assert callable(Logo::Void.__init__)


def test_logo::void_constructor_args():
    sig = inspect.signature(Logo::Void.__init__)
    params = list(sig.parameters.keys())



def test_logo::integer_is_not_abstract():
    assert not inspect.isabstract(Logo::Integer)


def test_logo::integer_constructor_exists():
    assert callable(Logo::Integer.__init__)


def test_logo::integer_constructor_args():
    sig = inspect.signature(Logo::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::integer_has_value():
    assert hasattr(Logo::Integer, "value")
    descriptor = None
    for klass in Logo::Integer.__mro__:
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



def test_logo::procedurecall_is_not_abstract():
    assert not inspect.isabstract(Logo::ProcedureCall)


def test_logo::procedurecall_constructor_exists():
    assert callable(Logo::ProcedureCall.__init__)


def test_logo::procedurecall_constructor_args():
    sig = inspect.signature(Logo::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_logo::binaryexpr_is_not_abstract():
    assert not inspect.isabstract(Logo::BinaryExpr)


def test_logo::binaryexpr_constructor_exists():
    assert callable(Logo::BinaryExpr.__init__)


def test_logo::binaryexpr_constructor_args():
    sig = inspect.signature(Logo::BinaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_logo::varreference_is_not_abstract():
    assert not inspect.isabstract(Logo::VarReference)


def test_logo::varreference_constructor_exists():
    assert callable(Logo::VarReference.__init__)


def test_logo::varreference_constructor_args():
    sig = inspect.signature(Logo::VarReference.__init__)
    params = list(sig.parameters.keys())



def test_logo::literal_is_not_abstract():
    assert not inspect.isabstract(Logo::Literal)


def test_logo::literal_constructor_exists():
    assert callable(Logo::Literal.__init__)


def test_logo::literal_constructor_args():
    sig = inspect.signature(Logo::Literal.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logo::right_is_not_abstract():
    assert not inspect.isabstract(Logo::Right)


def test_logo::right_constructor_exists():
    assert callable(Logo::Right.__init__)


def test_logo::right_constructor_args():
    sig = inspect.signature(Logo::Right.__init__)
    params = list(sig.parameters.keys())



def test_logo::back_is_not_abstract():
    assert not inspect.isabstract(Logo::Back)


def test_logo::back_constructor_exists():
    assert callable(Logo::Back.__init__)


def test_logo::back_constructor_args():
    sig = inspect.signature(Logo::Back.__init__)
    params = list(sig.parameters.keys())



def test_logo::left_is_not_abstract():
    assert not inspect.isabstract(Logo::Left)


def test_logo::left_constructor_exists():
    assert callable(Logo::Left.__init__)


def test_logo::left_constructor_args():
    sig = inspect.signature(Logo::Left.__init__)
    params = list(sig.parameters.keys())



def test_logo::forward_is_not_abstract():
    assert not inspect.isabstract(Logo::Forward)


def test_logo::forward_constructor_exists():
    assert callable(Logo::Forward.__init__)


def test_logo::forward_constructor_args():
    sig = inspect.signature(Logo::Forward.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo::vardecl_is_not_abstract():
    assert not inspect.isabstract(Logo::VarDecl)


def test_logo::vardecl_constructor_exists():
    assert callable(Logo::VarDecl.__init__)


def test_logo::vardecl_constructor_args():
    sig = inspect.signature(Logo::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::vardecl_has_name():
    assert hasattr(Logo::VarDecl, "name")
    descriptor = None
    for klass in Logo::VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::controlstructure_is_not_abstract():
    assert not inspect.isabstract(Logo::ControlStructure)


def test_logo::controlstructure_constructor_exists():
    assert callable(Logo::ControlStructure.__init__)


def test_logo::controlstructure_constructor_args():
    sig = inspect.signature(Logo::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_logo::procedure_is_not_abstract():
    assert not inspect.isabstract(Logo::Procedure)


def test_logo::procedure_constructor_exists():
    assert callable(Logo::Procedure.__init__)


def test_logo::procedure_constructor_args():
    sig = inspect.signature(Logo::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::procedure_has_name():
    assert hasattr(Logo::Procedure, "name")
    descriptor = None
    for klass in Logo::Procedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::assignation_is_not_abstract():
    assert not inspect.isabstract(Logo::Assignation)


def test_logo::assignation_constructor_exists():
    assert callable(Logo::Assignation.__init__)


def test_logo::assignation_constructor_args():
    sig = inspect.signature(Logo::Assignation.__init__)
    params = list(sig.parameters.keys())



def test_logo::expression_is_not_abstract():
    assert not inspect.isabstract(Logo::Expression)


def test_logo::expression_constructor_exists():
    assert callable(Logo::Expression.__init__)


def test_logo::expression_constructor_args():
    sig = inspect.signature(Logo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_logo::primitive_is_not_abstract():
    assert not inspect.isabstract(Logo::Primitive)


def test_logo::primitive_constructor_exists():
    assert callable(Logo::Primitive.__init__)


def test_logo::primitive_constructor_args():
    sig = inspect.signature(Logo::Primitive.__init__)
    params = list(sig.parameters.keys())

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "mult",
        "plus",
        "minus",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "lowerThan",
        "greaterThan",
        "diff",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"


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
Logo::BooleanExpr_strategy = st.builds(
    Logo::BooleanExpr,
    operator=
        safe_text
)
Logo::ArithmeticExpr_strategy = st.builds(
    Logo::ArithmeticExpr,
    operator=
        safe_text
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
Logo::While_strategy = st.builds(
    Logo::While,
)
Logo::Block_strategy = st.builds(
    Logo::Block,
)
Logo::If_strategy = st.builds(
    Logo::If,
)
Logo::Instruction_strategy = st.builds(
    Logo::Instruction,
)
Logo::LogoProgram_strategy = st.builds(
    Logo::LogoProgram,
)
Literal_strategy = st.builds(
    Literal,
)
Logo::String_strategy = st.builds(
    Logo::String,
    value=
        safe_text
)
Logo::Boolean_strategy = st.builds(
    Logo::Boolean,
    value=
        st.booleans()
)
Logo::Double_strategy = st.builds(
    Logo::Double,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Logo::Void_strategy = st.builds(
    Logo::Void,
)
Logo::Integer_strategy = st.builds(
    Logo::Integer,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
Logo::ProcedureCall_strategy = st.builds(
    Logo::ProcedureCall,
)
Logo::BinaryExpr_strategy = st.builds(
    Logo::BinaryExpr,
)
Logo::VarReference_strategy = st.builds(
    Logo::VarReference,
)
Logo::Literal_strategy = st.builds(
    Logo::Literal,
)
Primitive_strategy = st.builds(
    Primitive,
)
Logo::Right_strategy = st.builds(
    Logo::Right,
)
Logo::Back_strategy = st.builds(
    Logo::Back,
)
Logo::Left_strategy = st.builds(
    Logo::Left,
)
Logo::Forward_strategy = st.builds(
    Logo::Forward,
)
Instruction_strategy = st.builds(
    Instruction,
)
Logo::VarDecl_strategy = st.builds(
    Logo::VarDecl,
    name=
        safe_text
)
Logo::ControlStructure_strategy = st.builds(
    Logo::ControlStructure,
)
Logo::Procedure_strategy = st.builds(
    Logo::Procedure,
    name=
        safe_text
)
Logo::Assignation_strategy = st.builds(
    Logo::Assignation,
)
Logo::Expression_strategy = st.builds(
    Logo::Expression,
)
Logo::Primitive_strategy = st.builds(
    Logo::Primitive,
)

@given(instance=BinaryExpr_strategy)
@settings(max_examples=50)
def test_binaryexpr_instantiation(instance):
    assert isinstance(instance, BinaryExpr)

@given(instance=Logo::BooleanExpr_strategy)
@settings(max_examples=50)
def test_logo::booleanexpr_instantiation(instance):
    assert isinstance(instance, Logo::BooleanExpr)

@given(instance=Logo::BooleanExpr_strategy)
def test_logo::booleanexpr_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Logo::BooleanExpr_strategy)
def test_logo::booleanexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Logo::ArithmeticExpr_strategy)
@settings(max_examples=50)
def test_logo::arithmeticexpr_instantiation(instance):
    assert isinstance(instance, Logo::ArithmeticExpr)

@given(instance=Logo::ArithmeticExpr_strategy)
def test_logo::arithmeticexpr_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Logo::ArithmeticExpr_strategy)
def test_logo::arithmeticexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=Logo::While_strategy)
@settings(max_examples=50)
def test_logo::while_instantiation(instance):
    assert isinstance(instance, Logo::While)

@given(instance=Logo::Block_strategy)
@settings(max_examples=50)
def test_logo::block_instantiation(instance):
    assert isinstance(instance, Logo::Block)

@given(instance=Logo::If_strategy)
@settings(max_examples=50)
def test_logo::if_instantiation(instance):
    assert isinstance(instance, Logo::If)

@given(instance=Logo::Instruction_strategy)
@settings(max_examples=50)
def test_logo::instruction_instantiation(instance):
    assert isinstance(instance, Logo::Instruction)

@given(instance=Logo::LogoProgram_strategy)
@settings(max_examples=50)
def test_logo::logoprogram_instantiation(instance):
    assert isinstance(instance, Logo::LogoProgram)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=Logo::String_strategy)
@settings(max_examples=50)
def test_logo::string_instantiation(instance):
    assert isinstance(instance, Logo::String)

@given(instance=Logo::String_strategy)
def test_logo::string_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Logo::String_strategy)
def test_logo::string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Logo::Boolean_strategy)
@settings(max_examples=50)
def test_logo::boolean_instantiation(instance):
    assert isinstance(instance, Logo::Boolean)

@given(instance=Logo::Boolean_strategy)
def test_logo::boolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=Logo::Boolean_strategy)
def test_logo::boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Logo::Double_strategy)
@settings(max_examples=50)
def test_logo::double_instantiation(instance):
    assert isinstance(instance, Logo::Double)

@given(instance=Logo::Double_strategy)
def test_logo::double_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=Logo::Double_strategy)
def test_logo::double_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Logo::Void_strategy)
@settings(max_examples=50)
def test_logo::void_instantiation(instance):
    assert isinstance(instance, Logo::Void)

@given(instance=Logo::Integer_strategy)
@settings(max_examples=50)
def test_logo::integer_instantiation(instance):
    assert isinstance(instance, Logo::Integer)

@given(instance=Logo::Integer_strategy)
def test_logo::integer_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=Logo::Integer_strategy)
def test_logo::integer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Logo::ProcedureCall_strategy)
@settings(max_examples=50)
def test_logo::procedurecall_instantiation(instance):
    assert isinstance(instance, Logo::ProcedureCall)

@given(instance=Logo::BinaryExpr_strategy)
@settings(max_examples=50)
def test_logo::binaryexpr_instantiation(instance):
    assert isinstance(instance, Logo::BinaryExpr)

@given(instance=Logo::VarReference_strategy)
@settings(max_examples=50)
def test_logo::varreference_instantiation(instance):
    assert isinstance(instance, Logo::VarReference)

@given(instance=Logo::Literal_strategy)
@settings(max_examples=50)
def test_logo::literal_instantiation(instance):
    assert isinstance(instance, Logo::Literal)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=Logo::Right_strategy)
@settings(max_examples=50)
def test_logo::right_instantiation(instance):
    assert isinstance(instance, Logo::Right)

@given(instance=Logo::Back_strategy)
@settings(max_examples=50)
def test_logo::back_instantiation(instance):
    assert isinstance(instance, Logo::Back)

@given(instance=Logo::Left_strategy)
@settings(max_examples=50)
def test_logo::left_instantiation(instance):
    assert isinstance(instance, Logo::Left)

@given(instance=Logo::Forward_strategy)
@settings(max_examples=50)
def test_logo::forward_instantiation(instance):
    assert isinstance(instance, Logo::Forward)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=Logo::VarDecl_strategy)
@settings(max_examples=50)
def test_logo::vardecl_instantiation(instance):
    assert isinstance(instance, Logo::VarDecl)

@given(instance=Logo::VarDecl_strategy)
def test_logo::vardecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Logo::VarDecl_strategy)
def test_logo::vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Logo::ControlStructure_strategy)
@settings(max_examples=50)
def test_logo::controlstructure_instantiation(instance):
    assert isinstance(instance, Logo::ControlStructure)

@given(instance=Logo::Procedure_strategy)
@settings(max_examples=50)
def test_logo::procedure_instantiation(instance):
    assert isinstance(instance, Logo::Procedure)

@given(instance=Logo::Procedure_strategy)
def test_logo::procedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Logo::Procedure_strategy)
def test_logo::procedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Logo::Assignation_strategy)
@settings(max_examples=50)
def test_logo::assignation_instantiation(instance):
    assert isinstance(instance, Logo::Assignation)

@given(instance=Logo::Expression_strategy)
@settings(max_examples=50)
def test_logo::expression_instantiation(instance):
    assert isinstance(instance, Logo::Expression)

@given(instance=Logo::Primitive_strategy)
@settings(max_examples=50)
def test_logo::primitive_instantiation(instance):
    assert isinstance(instance, Logo::Primitive)
