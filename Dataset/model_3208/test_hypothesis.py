import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hlp_Nameable,
    ConditionalLoop,
    hlp_WhileLoop,
    Loop,
    hlp_ForLoop,
    hlp_ConditionalLoop,
    hlp_VariableDeclarationScope,
    BinaryExpression,
    hlp_ArithmeticExpression,
    UnaryExpression,
    hlp_UnaryMinusExpression,
    Expression,
    hlp_UnaryExpression,
    hlp_BinaryExpression,
    hlp_AtomicExpression,
    ArithmeticExpression,
    hlp_DivideExpression,
    hlp_SubtractExpression,
    hlp_MultiplyExpression,
    hlp_AddExpression,
    AtomicExpression,
    hlp_LiteralValue,
    hlp_Statement,
    hlp_VariableReference,
    Statement,
    hlp_ExpressionStatement,
    hlp_Loop,
    hlp_SynchronizedStatement,
    hlp_Assignment,
    hlp_Condition,
    hlp_IfStatement,
    hlp_Block,
    hlp_ParenthesisExpression,
    hlp_Expression,
    hlp_VariableDeclaration,
    hlp_ScheduleInstruction,
    Nameable,
    hlp_Variable,
    VariableDeclarationScope,
    hlp_Task,
    hlp_HighLevelProgram,
    ComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hlp_nameable_is_not_abstract():
    assert not inspect.isabstract(hlp_Nameable)


def test_hlp_nameable_constructor_exists():
    assert callable(hlp_Nameable.__init__)


def test_hlp_nameable_constructor_args():
    sig = inspect.signature(hlp_Nameable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hlp_nameable_has_name():
    assert hasattr(hlp_Nameable, "name")
    descriptor = None
    for klass in hlp_Nameable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conditionalloop_is_not_abstract():
    assert not inspect.isabstract(ConditionalLoop)


def test_conditionalloop_constructor_exists():
    assert callable(ConditionalLoop.__init__)


def test_conditionalloop_constructor_args():
    sig = inspect.signature(ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_hlp_whileloop_is_not_abstract():
    assert not inspect.isabstract(hlp_WhileLoop)


def test_hlp_whileloop_constructor_exists():
    assert callable(hlp_WhileLoop.__init__)


def test_hlp_whileloop_constructor_args():
    sig = inspect.signature(hlp_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_loop_is_not_abstract():
    assert not inspect.isabstract(Loop)


def test_loop_constructor_exists():
    assert callable(Loop.__init__)


def test_loop_constructor_args():
    sig = inspect.signature(Loop.__init__)
    params = list(sig.parameters.keys())



def test_hlp_forloop_is_not_abstract():
    assert not inspect.isabstract(hlp_ForLoop)


def test_hlp_forloop_constructor_exists():
    assert callable(hlp_ForLoop.__init__)


def test_hlp_forloop_constructor_args():
    sig = inspect.signature(hlp_ForLoop.__init__)
    params = list(sig.parameters.keys())
    assert "incrementing" in params, "Missing parameter 'incrementing'"

def test_hlp_forloop_has_incrementing():
    assert hasattr(hlp_ForLoop, "incrementing")
    descriptor = None
    for klass in hlp_ForLoop.__mro__:
        if "incrementing" in klass.__dict__:
            descriptor = klass.__dict__["incrementing"]
            break
    assert isinstance(descriptor, property)



def test_hlp_conditionalloop_is_not_abstract():
    assert not inspect.isabstract(hlp_ConditionalLoop)


def test_hlp_conditionalloop_constructor_exists():
    assert callable(hlp_ConditionalLoop.__init__)


def test_hlp_conditionalloop_constructor_args():
    sig = inspect.signature(hlp_ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_hlp_variabledeclarationscope_is_not_abstract():
    assert not inspect.isabstract(hlp_VariableDeclarationScope)


def test_hlp_variabledeclarationscope_constructor_exists():
    assert callable(hlp_VariableDeclarationScope.__init__)


def test_hlp_variabledeclarationscope_constructor_args():
    sig = inspect.signature(hlp_VariableDeclarationScope.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_ArithmeticExpression)


def test_hlp_arithmeticexpression_constructor_exists():
    assert callable(hlp_ArithmeticExpression.__init__)


def test_hlp_arithmeticexpression_constructor_args():
    sig = inspect.signature(hlp_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_UnaryMinusExpression)


def test_hlp_unaryminusexpression_constructor_exists():
    assert callable(hlp_UnaryMinusExpression.__init__)


def test_hlp_unaryminusexpression_constructor_args():
    sig = inspect.signature(hlp_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_UnaryExpression)


def test_hlp_unaryexpression_constructor_exists():
    assert callable(hlp_UnaryExpression.__init__)


def test_hlp_unaryexpression_constructor_args():
    sig = inspect.signature(hlp_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_BinaryExpression)


def test_hlp_binaryexpression_constructor_exists():
    assert callable(hlp_BinaryExpression.__init__)


def test_hlp_binaryexpression_constructor_args():
    sig = inspect.signature(hlp_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_AtomicExpression)


def test_hlp_atomicexpression_constructor_exists():
    assert callable(hlp_AtomicExpression.__init__)


def test_hlp_atomicexpression_constructor_args():
    sig = inspect.signature(hlp_AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_divideexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_DivideExpression)


def test_hlp_divideexpression_constructor_exists():
    assert callable(hlp_DivideExpression.__init__)


def test_hlp_divideexpression_constructor_args():
    sig = inspect.signature(hlp_DivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_subtractexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_SubtractExpression)


def test_hlp_subtractexpression_constructor_exists():
    assert callable(hlp_SubtractExpression.__init__)


def test_hlp_subtractexpression_constructor_args():
    sig = inspect.signature(hlp_SubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_multiplyexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_MultiplyExpression)


def test_hlp_multiplyexpression_constructor_exists():
    assert callable(hlp_MultiplyExpression.__init__)


def test_hlp_multiplyexpression_constructor_args():
    sig = inspect.signature(hlp_MultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_addexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_AddExpression)


def test_hlp_addexpression_constructor_exists():
    assert callable(hlp_AddExpression.__init__)


def test_hlp_addexpression_constructor_args():
    sig = inspect.signature(hlp_AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicExpression)


def test_atomicexpression_constructor_exists():
    assert callable(AtomicExpression.__init__)


def test_atomicexpression_constructor_args():
    sig = inspect.signature(AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_literalvalue_is_not_abstract():
    assert not inspect.isabstract(hlp_LiteralValue)


def test_hlp_literalvalue_constructor_exists():
    assert callable(hlp_LiteralValue.__init__)


def test_hlp_literalvalue_constructor_args():
    sig = inspect.signature(hlp_LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_hlp_literalvalue_has_rawValue():
    assert hasattr(hlp_LiteralValue, "rawValue")
    descriptor = None
    for klass in hlp_LiteralValue.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_hlp_statement_is_not_abstract():
    assert not inspect.isabstract(hlp_Statement)


def test_hlp_statement_constructor_exists():
    assert callable(hlp_Statement.__init__)


def test_hlp_statement_constructor_args():
    sig = inspect.signature(hlp_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hlp_variablereference_is_not_abstract():
    assert not inspect.isabstract(hlp_VariableReference)


def test_hlp_variablereference_constructor_exists():
    assert callable(hlp_VariableReference.__init__)


def test_hlp_variablereference_constructor_args():
    sig = inspect.signature(hlp_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hlp_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(hlp_ExpressionStatement)


def test_hlp_expressionstatement_constructor_exists():
    assert callable(hlp_ExpressionStatement.__init__)


def test_hlp_expressionstatement_constructor_args():
    sig = inspect.signature(hlp_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hlp_loop_is_not_abstract():
    assert not inspect.isabstract(hlp_Loop)


def test_hlp_loop_constructor_exists():
    assert callable(hlp_Loop.__init__)


def test_hlp_loop_constructor_args():
    sig = inspect.signature(hlp_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hlp_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(hlp_SynchronizedStatement)


def test_hlp_synchronizedstatement_constructor_exists():
    assert callable(hlp_SynchronizedStatement.__init__)


def test_hlp_synchronizedstatement_constructor_args():
    sig = inspect.signature(hlp_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hlp_assignment_is_not_abstract():
    assert not inspect.isabstract(hlp_Assignment)


def test_hlp_assignment_constructor_exists():
    assert callable(hlp_Assignment.__init__)


def test_hlp_assignment_constructor_args():
    sig = inspect.signature(hlp_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hlp_condition_is_not_abstract():
    assert not inspect.isabstract(hlp_Condition)


def test_hlp_condition_constructor_exists():
    assert callable(hlp_Condition.__init__)


def test_hlp_condition_constructor_args():
    sig = inspect.signature(hlp_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_hlp_condition_has_operator():
    assert hasattr(hlp_Condition, "operator")
    descriptor = None
    for klass in hlp_Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_hlp_ifstatement_is_not_abstract():
    assert not inspect.isabstract(hlp_IfStatement)


def test_hlp_ifstatement_constructor_exists():
    assert callable(hlp_IfStatement.__init__)


def test_hlp_ifstatement_constructor_args():
    sig = inspect.signature(hlp_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hlp_block_is_not_abstract():
    assert not inspect.isabstract(hlp_Block)


def test_hlp_block_constructor_exists():
    assert callable(hlp_Block.__init__)


def test_hlp_block_constructor_args():
    sig = inspect.signature(hlp_Block.__init__)
    params = list(sig.parameters.keys())



def test_hlp_parenthesisexpression_is_not_abstract():
    assert not inspect.isabstract(hlp_ParenthesisExpression)


def test_hlp_parenthesisexpression_constructor_exists():
    assert callable(hlp_ParenthesisExpression.__init__)


def test_hlp_parenthesisexpression_constructor_args():
    sig = inspect.signature(hlp_ParenthesisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_expression_is_not_abstract():
    assert not inspect.isabstract(hlp_Expression)


def test_hlp_expression_constructor_exists():
    assert callable(hlp_Expression.__init__)


def test_hlp_expression_constructor_args():
    sig = inspect.signature(hlp_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hlp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(hlp_VariableDeclaration)


def test_hlp_variabledeclaration_constructor_exists():
    assert callable(hlp_VariableDeclaration.__init__)


def test_hlp_variabledeclaration_constructor_args():
    sig = inspect.signature(hlp_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hlp_scheduleinstruction_is_not_abstract():
    assert not inspect.isabstract(hlp_ScheduleInstruction)


def test_hlp_scheduleinstruction_constructor_exists():
    assert callable(hlp_ScheduleInstruction.__init__)


def test_hlp_scheduleinstruction_constructor_args():
    sig = inspect.signature(hlp_ScheduleInstruction.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_hlp_variable_is_not_abstract():
    assert not inspect.isabstract(hlp_Variable)


def test_hlp_variable_constructor_exists():
    assert callable(hlp_Variable.__init__)


def test_hlp_variable_constructor_args():
    sig = inspect.signature(hlp_Variable.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationscope_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationScope)


def test_variabledeclarationscope_constructor_exists():
    assert callable(VariableDeclarationScope.__init__)


def test_variabledeclarationscope_constructor_args():
    sig = inspect.signature(VariableDeclarationScope.__init__)
    params = list(sig.parameters.keys())



def test_hlp_task_is_not_abstract():
    assert not inspect.isabstract(hlp_Task)


def test_hlp_task_constructor_exists():
    assert callable(hlp_Task.__init__)


def test_hlp_task_constructor_args():
    sig = inspect.signature(hlp_Task.__init__)
    params = list(sig.parameters.keys())



def test_hlp_highlevelprogram_is_not_abstract():
    assert not inspect.isabstract(hlp_HighLevelProgram)


def test_hlp_highlevelprogram_constructor_exists():
    assert callable(hlp_HighLevelProgram.__init__)


def test_hlp_highlevelprogram_constructor_args():
    sig = inspect.signature(hlp_HighLevelProgram.__init__)
    params = list(sig.parameters.keys())

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "UNEQUAL",
        "EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"


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
hlp_Nameable_strategy = st.builds(
    hlp_Nameable,
    name=
        safe_text
)
ConditionalLoop_strategy = st.builds(
    ConditionalLoop,
)
hlp_WhileLoop_strategy = st.builds(
    hlp_WhileLoop,
)
Loop_strategy = st.builds(
    Loop,
)
hlp_ForLoop_strategy = st.builds(
    hlp_ForLoop,
    incrementing=
        st.booleans()
)
hlp_ConditionalLoop_strategy = st.builds(
    hlp_ConditionalLoop,
)
hlp_VariableDeclarationScope_strategy = st.builds(
    hlp_VariableDeclarationScope,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
hlp_ArithmeticExpression_strategy = st.builds(
    hlp_ArithmeticExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
hlp_UnaryMinusExpression_strategy = st.builds(
    hlp_UnaryMinusExpression,
)
Expression_strategy = st.builds(
    Expression,
)
hlp_UnaryExpression_strategy = st.builds(
    hlp_UnaryExpression,
)
hlp_BinaryExpression_strategy = st.builds(
    hlp_BinaryExpression,
)
hlp_AtomicExpression_strategy = st.builds(
    hlp_AtomicExpression,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
hlp_DivideExpression_strategy = st.builds(
    hlp_DivideExpression,
)
hlp_SubtractExpression_strategy = st.builds(
    hlp_SubtractExpression,
)
hlp_MultiplyExpression_strategy = st.builds(
    hlp_MultiplyExpression,
)
hlp_AddExpression_strategy = st.builds(
    hlp_AddExpression,
)
AtomicExpression_strategy = st.builds(
    AtomicExpression,
)
hlp_LiteralValue_strategy = st.builds(
    hlp_LiteralValue,
    rawValue=
        safe_text
)
hlp_Statement_strategy = st.builds(
    hlp_Statement,
)
hlp_VariableReference_strategy = st.builds(
    hlp_VariableReference,
)
Statement_strategy = st.builds(
    Statement,
)
hlp_ExpressionStatement_strategy = st.builds(
    hlp_ExpressionStatement,
)
hlp_Loop_strategy = st.builds(
    hlp_Loop,
)
hlp_SynchronizedStatement_strategy = st.builds(
    hlp_SynchronizedStatement,
)
hlp_Assignment_strategy = st.builds(
    hlp_Assignment,
)
hlp_Condition_strategy = st.builds(
    hlp_Condition,
    operator=
        safe_text
)
hlp_IfStatement_strategy = st.builds(
    hlp_IfStatement,
)
hlp_Block_strategy = st.builds(
    hlp_Block,
)
hlp_ParenthesisExpression_strategy = st.builds(
    hlp_ParenthesisExpression,
)
hlp_Expression_strategy = st.builds(
    hlp_Expression,
)
hlp_VariableDeclaration_strategy = st.builds(
    hlp_VariableDeclaration,
)
hlp_ScheduleInstruction_strategy = st.builds(
    hlp_ScheduleInstruction,
)
Nameable_strategy = st.builds(
    Nameable,
)
hlp_Variable_strategy = st.builds(
    hlp_Variable,
)
VariableDeclarationScope_strategy = st.builds(
    VariableDeclarationScope,
)
hlp_Task_strategy = st.builds(
    hlp_Task,
)
hlp_HighLevelProgram_strategy = st.builds(
    hlp_HighLevelProgram,
)

@given(instance=hlp_Nameable_strategy)
@settings(max_examples=50)
def test_hlp_nameable_instantiation(instance):
    assert isinstance(instance, hlp_Nameable)



@given(instance=hlp_Nameable_strategy)
def test_hlp_nameable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConditionalLoop_strategy)
@settings(max_examples=50)
def test_conditionalloop_instantiation(instance):
    assert isinstance(instance, ConditionalLoop)

@given(instance=hlp_WhileLoop_strategy)
@settings(max_examples=50)
def test_hlp_whileloop_instantiation(instance):
    assert isinstance(instance, hlp_WhileLoop)

@given(instance=Loop_strategy)
@settings(max_examples=50)
def test_loop_instantiation(instance):
    assert isinstance(instance, Loop)

@given(instance=hlp_ForLoop_strategy)
@settings(max_examples=50)
def test_hlp_forloop_instantiation(instance):
    assert isinstance(instance, hlp_ForLoop)



@given(instance=hlp_ForLoop_strategy)
def test_hlp_forloop_incrementing_setter(instance):
    original = instance.incrementing
    instance.incrementing = original
    assert instance.incrementing == original

@given(instance=hlp_ConditionalLoop_strategy)
@settings(max_examples=50)
def test_hlp_conditionalloop_instantiation(instance):
    assert isinstance(instance, hlp_ConditionalLoop)

@given(instance=hlp_VariableDeclarationScope_strategy)
@settings(max_examples=50)
def test_hlp_variabledeclarationscope_instantiation(instance):
    assert isinstance(instance, hlp_VariableDeclarationScope)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=hlp_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_hlp_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, hlp_ArithmeticExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=hlp_UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_hlp_unaryminusexpression_instantiation(instance):
    assert isinstance(instance, hlp_UnaryMinusExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=hlp_UnaryExpression_strategy)
@settings(max_examples=50)
def test_hlp_unaryexpression_instantiation(instance):
    assert isinstance(instance, hlp_UnaryExpression)

@given(instance=hlp_BinaryExpression_strategy)
@settings(max_examples=50)
def test_hlp_binaryexpression_instantiation(instance):
    assert isinstance(instance, hlp_BinaryExpression)

@given(instance=hlp_AtomicExpression_strategy)
@settings(max_examples=50)
def test_hlp_atomicexpression_instantiation(instance):
    assert isinstance(instance, hlp_AtomicExpression)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=hlp_DivideExpression_strategy)
@settings(max_examples=50)
def test_hlp_divideexpression_instantiation(instance):
    assert isinstance(instance, hlp_DivideExpression)

@given(instance=hlp_SubtractExpression_strategy)
@settings(max_examples=50)
def test_hlp_subtractexpression_instantiation(instance):
    assert isinstance(instance, hlp_SubtractExpression)

@given(instance=hlp_MultiplyExpression_strategy)
@settings(max_examples=50)
def test_hlp_multiplyexpression_instantiation(instance):
    assert isinstance(instance, hlp_MultiplyExpression)

@given(instance=hlp_AddExpression_strategy)
@settings(max_examples=50)
def test_hlp_addexpression_instantiation(instance):
    assert isinstance(instance, hlp_AddExpression)

@given(instance=AtomicExpression_strategy)
@settings(max_examples=50)
def test_atomicexpression_instantiation(instance):
    assert isinstance(instance, AtomicExpression)

@given(instance=hlp_LiteralValue_strategy)
@settings(max_examples=50)
def test_hlp_literalvalue_instantiation(instance):
    assert isinstance(instance, hlp_LiteralValue)



@given(instance=hlp_LiteralValue_strategy)
def test_hlp_literalvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

@given(instance=hlp_Statement_strategy)
@settings(max_examples=50)
def test_hlp_statement_instantiation(instance):
    assert isinstance(instance, hlp_Statement)

@given(instance=hlp_VariableReference_strategy)
@settings(max_examples=50)
def test_hlp_variablereference_instantiation(instance):
    assert isinstance(instance, hlp_VariableReference)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=hlp_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_hlp_expressionstatement_instantiation(instance):
    assert isinstance(instance, hlp_ExpressionStatement)

@given(instance=hlp_Loop_strategy)
@settings(max_examples=50)
def test_hlp_loop_instantiation(instance):
    assert isinstance(instance, hlp_Loop)

@given(instance=hlp_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_hlp_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, hlp_SynchronizedStatement)

@given(instance=hlp_Assignment_strategy)
@settings(max_examples=50)
def test_hlp_assignment_instantiation(instance):
    assert isinstance(instance, hlp_Assignment)

@given(instance=hlp_Condition_strategy)
@settings(max_examples=50)
def test_hlp_condition_instantiation(instance):
    assert isinstance(instance, hlp_Condition)



@given(instance=hlp_Condition_strategy)
def test_hlp_condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=hlp_IfStatement_strategy)
@settings(max_examples=50)
def test_hlp_ifstatement_instantiation(instance):
    assert isinstance(instance, hlp_IfStatement)

@given(instance=hlp_Block_strategy)
@settings(max_examples=50)
def test_hlp_block_instantiation(instance):
    assert isinstance(instance, hlp_Block)

@given(instance=hlp_ParenthesisExpression_strategy)
@settings(max_examples=50)
def test_hlp_parenthesisexpression_instantiation(instance):
    assert isinstance(instance, hlp_ParenthesisExpression)

@given(instance=hlp_Expression_strategy)
@settings(max_examples=50)
def test_hlp_expression_instantiation(instance):
    assert isinstance(instance, hlp_Expression)

@given(instance=hlp_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_hlp_variabledeclaration_instantiation(instance):
    assert isinstance(instance, hlp_VariableDeclaration)

@given(instance=hlp_ScheduleInstruction_strategy)
@settings(max_examples=50)
def test_hlp_scheduleinstruction_instantiation(instance):
    assert isinstance(instance, hlp_ScheduleInstruction)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=hlp_Variable_strategy)
@settings(max_examples=50)
def test_hlp_variable_instantiation(instance):
    assert isinstance(instance, hlp_Variable)

@given(instance=VariableDeclarationScope_strategy)
@settings(max_examples=50)
def test_variabledeclarationscope_instantiation(instance):
    assert isinstance(instance, VariableDeclarationScope)

@given(instance=hlp_Task_strategy)
@settings(max_examples=50)
def test_hlp_task_instantiation(instance):
    assert isinstance(instance, hlp_Task)

@given(instance=hlp_HighLevelProgram_strategy)
@settings(max_examples=50)
def test_hlp_highlevelprogram_instantiation(instance):
    assert isinstance(instance, hlp_HighLevelProgram)
