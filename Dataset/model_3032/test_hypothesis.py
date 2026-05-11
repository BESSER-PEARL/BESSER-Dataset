import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractExpression,
    miniJava::ThisReference,
    miniJava::Multiply,
    miniJava::ClassConstruction,
    miniJava::LessThen,
    miniJava::IntLiteral,
    miniJava::Minus,
    miniJava::BlockExpression,
    miniJava::Negation,
    miniJava::ClassifierReference,
    miniJava::LengthOf,
    miniJava::Boolean,
    miniJava::Plus,
    miniJava::FunctionCall,
    miniJava::IntegerArrayConstruction,
    miniJava::And,
    miniJava::ArrayAccess,
    Statement,
    miniJava::ArrayAssignment,
    miniJava::WhileLoop,
    miniJava::PrintLine,
    miniJava::Assignment,
    miniJava::IfStatement,
    miniJava::BlockStatement,
    AbstactType,
    miniJava::ClassifierType,
    miniJava::IntegerType,
    miniJava::BooleanType,
    miniJava::IntegerArrayType,
    miniJava::AbstractExpression,
    miniJava::AbstactType,
    miniJava::MethodDeclaration,
    miniJava::VariableDeclaration,
    miniJava::Statement,
    miniJava::Identifier,
    miniJava::Class,
    miniJava::MainClass,
    miniJava::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractExpression)


def test_abstractexpression_constructor_exists():
    assert callable(AbstractExpression.__init__)


def test_abstractexpression_constructor_args():
    sig = inspect.signature(AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_minijava::thisreference_is_not_abstract():
    assert not inspect.isabstract(miniJava::ThisReference)


def test_minijava::thisreference_constructor_exists():
    assert callable(miniJava::ThisReference.__init__)


def test_minijava::thisreference_constructor_args():
    sig = inspect.signature(miniJava::ThisReference.__init__)
    params = list(sig.parameters.keys())



def test_minijava::multiply_is_not_abstract():
    assert not inspect.isabstract(miniJava::Multiply)


def test_minijava::multiply_constructor_exists():
    assert callable(miniJava::Multiply.__init__)


def test_minijava::multiply_constructor_args():
    sig = inspect.signature(miniJava::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_minijava::classconstruction_is_not_abstract():
    assert not inspect.isabstract(miniJava::ClassConstruction)


def test_minijava::classconstruction_constructor_exists():
    assert callable(miniJava::ClassConstruction.__init__)


def test_minijava::classconstruction_constructor_args():
    sig = inspect.signature(miniJava::ClassConstruction.__init__)
    params = list(sig.parameters.keys())



def test_minijava::lessthen_is_not_abstract():
    assert not inspect.isabstract(miniJava::LessThen)


def test_minijava::lessthen_constructor_exists():
    assert callable(miniJava::LessThen.__init__)


def test_minijava::lessthen_constructor_args():
    sig = inspect.signature(miniJava::LessThen.__init__)
    params = list(sig.parameters.keys())



def test_minijava::intliteral_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntLiteral)


def test_minijava::intliteral_constructor_exists():
    assert callable(miniJava::IntLiteral.__init__)


def test_minijava::intliteral_constructor_args():
    sig = inspect.signature(miniJava::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "resultInt" in params, "Missing parameter 'resultInt'"

def test_minijava::intliteral_has_resultInt():
    assert hasattr(miniJava::IntLiteral, "resultInt")
    descriptor = None
    for klass in miniJava::IntLiteral.__mro__:
        if "resultInt" in klass.__dict__:
            descriptor = klass.__dict__["resultInt"]
            break
    assert isinstance(descriptor, property)



def test_minijava::minus_is_not_abstract():
    assert not inspect.isabstract(miniJava::Minus)


def test_minijava::minus_constructor_exists():
    assert callable(miniJava::Minus.__init__)


def test_minijava::minus_constructor_args():
    sig = inspect.signature(miniJava::Minus.__init__)
    params = list(sig.parameters.keys())



def test_minijava::blockexpression_is_not_abstract():
    assert not inspect.isabstract(miniJava::BlockExpression)


def test_minijava::blockexpression_constructor_exists():
    assert callable(miniJava::BlockExpression.__init__)


def test_minijava::blockexpression_constructor_args():
    sig = inspect.signature(miniJava::BlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_minijava::negation_is_not_abstract():
    assert not inspect.isabstract(miniJava::Negation)


def test_minijava::negation_constructor_exists():
    assert callable(miniJava::Negation.__init__)


def test_minijava::negation_constructor_args():
    sig = inspect.signature(miniJava::Negation.__init__)
    params = list(sig.parameters.keys())



def test_minijava::classifierreference_is_not_abstract():
    assert not inspect.isabstract(miniJava::ClassifierReference)


def test_minijava::classifierreference_constructor_exists():
    assert callable(miniJava::ClassifierReference.__init__)


def test_minijava::classifierreference_constructor_args():
    sig = inspect.signature(miniJava::ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_minijava::lengthof_is_not_abstract():
    assert not inspect.isabstract(miniJava::LengthOf)


def test_minijava::lengthof_constructor_exists():
    assert callable(miniJava::LengthOf.__init__)


def test_minijava::lengthof_constructor_args():
    sig = inspect.signature(miniJava::LengthOf.__init__)
    params = list(sig.parameters.keys())



def test_minijava::boolean_is_not_abstract():
    assert not inspect.isabstract(miniJava::Boolean)


def test_minijava::boolean_constructor_exists():
    assert callable(miniJava::Boolean.__init__)


def test_minijava::boolean_constructor_args():
    sig = inspect.signature(miniJava::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "result" in params, "Missing parameter 'result'"

def test_minijava::boolean_has_result():
    assert hasattr(miniJava::Boolean, "result")
    descriptor = None
    for klass in miniJava::Boolean.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)



def test_minijava::plus_is_not_abstract():
    assert not inspect.isabstract(miniJava::Plus)


def test_minijava::plus_constructor_exists():
    assert callable(miniJava::Plus.__init__)


def test_minijava::plus_constructor_args():
    sig = inspect.signature(miniJava::Plus.__init__)
    params = list(sig.parameters.keys())



def test_minijava::functioncall_is_not_abstract():
    assert not inspect.isabstract(miniJava::FunctionCall)


def test_minijava::functioncall_constructor_exists():
    assert callable(miniJava::FunctionCall.__init__)


def test_minijava::functioncall_constructor_args():
    sig = inspect.signature(miniJava::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava::integerarrayconstruction_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntegerArrayConstruction)


def test_minijava::integerarrayconstruction_constructor_exists():
    assert callable(miniJava::IntegerArrayConstruction.__init__)


def test_minijava::integerarrayconstruction_constructor_args():
    sig = inspect.signature(miniJava::IntegerArrayConstruction.__init__)
    params = list(sig.parameters.keys())



def test_minijava::and_is_not_abstract():
    assert not inspect.isabstract(miniJava::And)


def test_minijava::and_constructor_exists():
    assert callable(miniJava::And.__init__)


def test_minijava::and_constructor_args():
    sig = inspect.signature(miniJava::And.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayAccess)


def test_minijava::arrayaccess_constructor_exists():
    assert callable(miniJava::ArrayAccess.__init__)


def test_minijava::arrayaccess_constructor_args():
    sig = inspect.signature(miniJava::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arrayassignment_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayAssignment)


def test_minijava::arrayassignment_constructor_exists():
    assert callable(miniJava::ArrayAssignment.__init__)


def test_minijava::arrayassignment_constructor_args():
    sig = inspect.signature(miniJava::ArrayAssignment.__init__)
    params = list(sig.parameters.keys())



def test_minijava::whileloop_is_not_abstract():
    assert not inspect.isabstract(miniJava::WhileLoop)


def test_minijava::whileloop_constructor_exists():
    assert callable(miniJava::WhileLoop.__init__)


def test_minijava::whileloop_constructor_args():
    sig = inspect.signature(miniJava::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_minijava::printline_is_not_abstract():
    assert not inspect.isabstract(miniJava::PrintLine)


def test_minijava::printline_constructor_exists():
    assert callable(miniJava::PrintLine.__init__)


def test_minijava::printline_constructor_args():
    sig = inspect.signature(miniJava::PrintLine.__init__)
    params = list(sig.parameters.keys())



def test_minijava::assignment_is_not_abstract():
    assert not inspect.isabstract(miniJava::Assignment)


def test_minijava::assignment_constructor_exists():
    assert callable(miniJava::Assignment.__init__)


def test_minijava::assignment_constructor_args():
    sig = inspect.signature(miniJava::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_minijava::ifstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::IfStatement)


def test_minijava::ifstatement_constructor_exists():
    assert callable(miniJava::IfStatement.__init__)


def test_minijava::ifstatement_constructor_args():
    sig = inspect.signature(miniJava::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::blockstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::BlockStatement)


def test_minijava::blockstatement_constructor_exists():
    assert callable(miniJava::BlockStatement.__init__)


def test_minijava::blockstatement_constructor_args():
    sig = inspect.signature(miniJava::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstacttype_is_not_abstract():
    assert not inspect.isabstract(AbstactType)


def test_abstacttype_constructor_exists():
    assert callable(AbstactType.__init__)


def test_abstacttype_constructor_args():
    sig = inspect.signature(AbstactType.__init__)
    params = list(sig.parameters.keys())



def test_minijava::classifiertype_is_not_abstract():
    assert not inspect.isabstract(miniJava::ClassifierType)


def test_minijava::classifiertype_constructor_exists():
    assert callable(miniJava::ClassifierType.__init__)


def test_minijava::classifiertype_constructor_args():
    sig = inspect.signature(miniJava::ClassifierType.__init__)
    params = list(sig.parameters.keys())



def test_minijava::integertype_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntegerType)


def test_minijava::integertype_constructor_exists():
    assert callable(miniJava::IntegerType.__init__)


def test_minijava::integertype_constructor_args():
    sig = inspect.signature(miniJava::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_minijava::booleantype_is_not_abstract():
    assert not inspect.isabstract(miniJava::BooleanType)


def test_minijava::booleantype_constructor_exists():
    assert callable(miniJava::BooleanType.__init__)


def test_minijava::booleantype_constructor_args():
    sig = inspect.signature(miniJava::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_minijava::integerarraytype_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntegerArrayType)


def test_minijava::integerarraytype_constructor_exists():
    assert callable(miniJava::IntegerArrayType.__init__)


def test_minijava::integerarraytype_constructor_args():
    sig = inspect.signature(miniJava::IntegerArrayType.__init__)
    params = list(sig.parameters.keys())



def test_minijava::abstractexpression_is_not_abstract():
    assert not inspect.isabstract(miniJava::AbstractExpression)


def test_minijava::abstractexpression_constructor_exists():
    assert callable(miniJava::AbstractExpression.__init__)


def test_minijava::abstractexpression_constructor_args():
    sig = inspect.signature(miniJava::AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_minijava::abstacttype_is_not_abstract():
    assert not inspect.isabstract(miniJava::AbstactType)


def test_minijava::abstacttype_constructor_exists():
    assert callable(miniJava::AbstactType.__init__)


def test_minijava::abstacttype_constructor_args():
    sig = inspect.signature(miniJava::AbstactType.__init__)
    params = list(sig.parameters.keys())



def test_minijava::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::MethodDeclaration)


def test_minijava::methoddeclaration_constructor_exists():
    assert callable(miniJava::MethodDeclaration.__init__)


def test_minijava::methoddeclaration_constructor_args():
    sig = inspect.signature(miniJava::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::VariableDeclaration)


def test_minijava::variabledeclaration_constructor_exists():
    assert callable(miniJava::VariableDeclaration.__init__)


def test_minijava::variabledeclaration_constructor_args():
    sig = inspect.signature(miniJava::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::statement_is_not_abstract():
    assert not inspect.isabstract(miniJava::Statement)


def test_minijava::statement_constructor_exists():
    assert callable(miniJava::Statement.__init__)


def test_minijava::statement_constructor_args():
    sig = inspect.signature(miniJava::Statement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::identifier_is_not_abstract():
    assert not inspect.isabstract(miniJava::Identifier)


def test_minijava::identifier_constructor_exists():
    assert callable(miniJava::Identifier.__init__)


def test_minijava::identifier_constructor_args():
    sig = inspect.signature(miniJava::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::identifier_has_value():
    assert hasattr(miniJava::Identifier, "value")
    descriptor = None
    for klass in miniJava::Identifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::class_is_not_abstract():
    assert not inspect.isabstract(miniJava::Class)


def test_minijava::class_constructor_exists():
    assert callable(miniJava::Class.__init__)


def test_minijava::class_constructor_args():
    sig = inspect.signature(miniJava::Class.__init__)
    params = list(sig.parameters.keys())



def test_minijava::mainclass_is_not_abstract():
    assert not inspect.isabstract(miniJava::MainClass)


def test_minijava::mainclass_constructor_exists():
    assert callable(miniJava::MainClass.__init__)


def test_minijava::mainclass_constructor_args():
    sig = inspect.signature(miniJava::MainClass.__init__)
    params = list(sig.parameters.keys())



def test_minijava::program_is_not_abstract():
    assert not inspect.isabstract(miniJava::Program)


def test_minijava::program_constructor_exists():
    assert callable(miniJava::Program.__init__)


def test_minijava::program_constructor_args():
    sig = inspect.signature(miniJava::Program.__init__)
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
AbstractExpression_strategy = st.builds(
    AbstractExpression,
)
miniJava::ThisReference_strategy = st.builds(
    miniJava::ThisReference,
)
miniJava::Multiply_strategy = st.builds(
    miniJava::Multiply,
)
miniJava::ClassConstruction_strategy = st.builds(
    miniJava::ClassConstruction,
)
miniJava::LessThen_strategy = st.builds(
    miniJava::LessThen,
)
miniJava::IntLiteral_strategy = st.builds(
    miniJava::IntLiteral,
    resultInt=
        st.integers()
)
miniJava::Minus_strategy = st.builds(
    miniJava::Minus,
)
miniJava::BlockExpression_strategy = st.builds(
    miniJava::BlockExpression,
)
miniJava::Negation_strategy = st.builds(
    miniJava::Negation,
)
miniJava::ClassifierReference_strategy = st.builds(
    miniJava::ClassifierReference,
)
miniJava::LengthOf_strategy = st.builds(
    miniJava::LengthOf,
)
miniJava::Boolean_strategy = st.builds(
    miniJava::Boolean,
    result=
        st.booleans()
)
miniJava::Plus_strategy = st.builds(
    miniJava::Plus,
)
miniJava::FunctionCall_strategy = st.builds(
    miniJava::FunctionCall,
)
miniJava::IntegerArrayConstruction_strategy = st.builds(
    miniJava::IntegerArrayConstruction,
)
miniJava::And_strategy = st.builds(
    miniJava::And,
)
miniJava::ArrayAccess_strategy = st.builds(
    miniJava::ArrayAccess,
)
Statement_strategy = st.builds(
    Statement,
)
miniJava::ArrayAssignment_strategy = st.builds(
    miniJava::ArrayAssignment,
)
miniJava::WhileLoop_strategy = st.builds(
    miniJava::WhileLoop,
)
miniJava::PrintLine_strategy = st.builds(
    miniJava::PrintLine,
)
miniJava::Assignment_strategy = st.builds(
    miniJava::Assignment,
)
miniJava::IfStatement_strategy = st.builds(
    miniJava::IfStatement,
)
miniJava::BlockStatement_strategy = st.builds(
    miniJava::BlockStatement,
)
AbstactType_strategy = st.builds(
    AbstactType,
)
miniJava::ClassifierType_strategy = st.builds(
    miniJava::ClassifierType,
)
miniJava::IntegerType_strategy = st.builds(
    miniJava::IntegerType,
)
miniJava::BooleanType_strategy = st.builds(
    miniJava::BooleanType,
)
miniJava::IntegerArrayType_strategy = st.builds(
    miniJava::IntegerArrayType,
)
miniJava::AbstractExpression_strategy = st.builds(
    miniJava::AbstractExpression,
)
miniJava::AbstactType_strategy = st.builds(
    miniJava::AbstactType,
)
miniJava::MethodDeclaration_strategy = st.builds(
    miniJava::MethodDeclaration,
)
miniJava::VariableDeclaration_strategy = st.builds(
    miniJava::VariableDeclaration,
)
miniJava::Statement_strategy = st.builds(
    miniJava::Statement,
)
miniJava::Identifier_strategy = st.builds(
    miniJava::Identifier,
    value=
        safe_text
)
miniJava::Class_strategy = st.builds(
    miniJava::Class,
)
miniJava::MainClass_strategy = st.builds(
    miniJava::MainClass,
)
miniJava::Program_strategy = st.builds(
    miniJava::Program,
)

@given(instance=AbstractExpression_strategy)
@settings(max_examples=50)
def test_abstractexpression_instantiation(instance):
    assert isinstance(instance, AbstractExpression)

@given(instance=miniJava::ThisReference_strategy)
@settings(max_examples=50)
def test_minijava::thisreference_instantiation(instance):
    assert isinstance(instance, miniJava::ThisReference)

@given(instance=miniJava::Multiply_strategy)
@settings(max_examples=50)
def test_minijava::multiply_instantiation(instance):
    assert isinstance(instance, miniJava::Multiply)

@given(instance=miniJava::ClassConstruction_strategy)
@settings(max_examples=50)
def test_minijava::classconstruction_instantiation(instance):
    assert isinstance(instance, miniJava::ClassConstruction)

@given(instance=miniJava::LessThen_strategy)
@settings(max_examples=50)
def test_minijava::lessthen_instantiation(instance):
    assert isinstance(instance, miniJava::LessThen)

@given(instance=miniJava::IntLiteral_strategy)
@settings(max_examples=50)
def test_minijava::intliteral_instantiation(instance):
    assert isinstance(instance, miniJava::IntLiteral)

@given(instance=miniJava::IntLiteral_strategy)
def test_minijava::intliteral_resultInt_type(instance):
    assert isinstance(instance.resultInt, int)


@given(instance=miniJava::IntLiteral_strategy)
def test_minijava::intliteral_resultInt_setter(instance):
    original = instance.resultInt
    instance.resultInt = original
    assert instance.resultInt == original

@given(instance=miniJava::Minus_strategy)
@settings(max_examples=50)
def test_minijava::minus_instantiation(instance):
    assert isinstance(instance, miniJava::Minus)

@given(instance=miniJava::BlockExpression_strategy)
@settings(max_examples=50)
def test_minijava::blockexpression_instantiation(instance):
    assert isinstance(instance, miniJava::BlockExpression)

@given(instance=miniJava::Negation_strategy)
@settings(max_examples=50)
def test_minijava::negation_instantiation(instance):
    assert isinstance(instance, miniJava::Negation)

@given(instance=miniJava::ClassifierReference_strategy)
@settings(max_examples=50)
def test_minijava::classifierreference_instantiation(instance):
    assert isinstance(instance, miniJava::ClassifierReference)

@given(instance=miniJava::LengthOf_strategy)
@settings(max_examples=50)
def test_minijava::lengthof_instantiation(instance):
    assert isinstance(instance, miniJava::LengthOf)

@given(instance=miniJava::Boolean_strategy)
@settings(max_examples=50)
def test_minijava::boolean_instantiation(instance):
    assert isinstance(instance, miniJava::Boolean)

@given(instance=miniJava::Boolean_strategy)
def test_minijava::boolean_result_type(instance):
    assert isinstance(instance.result, bool)


@given(instance=miniJava::Boolean_strategy)
def test_minijava::boolean_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original

@given(instance=miniJava::Plus_strategy)
@settings(max_examples=50)
def test_minijava::plus_instantiation(instance):
    assert isinstance(instance, miniJava::Plus)

@given(instance=miniJava::FunctionCall_strategy)
@settings(max_examples=50)
def test_minijava::functioncall_instantiation(instance):
    assert isinstance(instance, miniJava::FunctionCall)

@given(instance=miniJava::IntegerArrayConstruction_strategy)
@settings(max_examples=50)
def test_minijava::integerarrayconstruction_instantiation(instance):
    assert isinstance(instance, miniJava::IntegerArrayConstruction)

@given(instance=miniJava::And_strategy)
@settings(max_examples=50)
def test_minijava::and_instantiation(instance):
    assert isinstance(instance, miniJava::And)

@given(instance=miniJava::ArrayAccess_strategy)
@settings(max_examples=50)
def test_minijava::arrayaccess_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayAccess)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=miniJava::ArrayAssignment_strategy)
@settings(max_examples=50)
def test_minijava::arrayassignment_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayAssignment)

@given(instance=miniJava::WhileLoop_strategy)
@settings(max_examples=50)
def test_minijava::whileloop_instantiation(instance):
    assert isinstance(instance, miniJava::WhileLoop)

@given(instance=miniJava::PrintLine_strategy)
@settings(max_examples=50)
def test_minijava::printline_instantiation(instance):
    assert isinstance(instance, miniJava::PrintLine)

@given(instance=miniJava::Assignment_strategy)
@settings(max_examples=50)
def test_minijava::assignment_instantiation(instance):
    assert isinstance(instance, miniJava::Assignment)

@given(instance=miniJava::IfStatement_strategy)
@settings(max_examples=50)
def test_minijava::ifstatement_instantiation(instance):
    assert isinstance(instance, miniJava::IfStatement)

@given(instance=miniJava::BlockStatement_strategy)
@settings(max_examples=50)
def test_minijava::blockstatement_instantiation(instance):
    assert isinstance(instance, miniJava::BlockStatement)

@given(instance=AbstactType_strategy)
@settings(max_examples=50)
def test_abstacttype_instantiation(instance):
    assert isinstance(instance, AbstactType)

@given(instance=miniJava::ClassifierType_strategy)
@settings(max_examples=50)
def test_minijava::classifiertype_instantiation(instance):
    assert isinstance(instance, miniJava::ClassifierType)

@given(instance=miniJava::IntegerType_strategy)
@settings(max_examples=50)
def test_minijava::integertype_instantiation(instance):
    assert isinstance(instance, miniJava::IntegerType)

@given(instance=miniJava::BooleanType_strategy)
@settings(max_examples=50)
def test_minijava::booleantype_instantiation(instance):
    assert isinstance(instance, miniJava::BooleanType)

@given(instance=miniJava::IntegerArrayType_strategy)
@settings(max_examples=50)
def test_minijava::integerarraytype_instantiation(instance):
    assert isinstance(instance, miniJava::IntegerArrayType)

@given(instance=miniJava::AbstractExpression_strategy)
@settings(max_examples=50)
def test_minijava::abstractexpression_instantiation(instance):
    assert isinstance(instance, miniJava::AbstractExpression)

@given(instance=miniJava::AbstactType_strategy)
@settings(max_examples=50)
def test_minijava::abstacttype_instantiation(instance):
    assert isinstance(instance, miniJava::AbstactType)

@given(instance=miniJava::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::methoddeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::MethodDeclaration)

@given(instance=miniJava::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::variabledeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::VariableDeclaration)

@given(instance=miniJava::Statement_strategy)
@settings(max_examples=50)
def test_minijava::statement_instantiation(instance):
    assert isinstance(instance, miniJava::Statement)

@given(instance=miniJava::Identifier_strategy)
@settings(max_examples=50)
def test_minijava::identifier_instantiation(instance):
    assert isinstance(instance, miniJava::Identifier)

@given(instance=miniJava::Identifier_strategy)
def test_minijava::identifier_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=miniJava::Identifier_strategy)
def test_minijava::identifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::Class_strategy)
@settings(max_examples=50)
def test_minijava::class_instantiation(instance):
    assert isinstance(instance, miniJava::Class)

@given(instance=miniJava::MainClass_strategy)
@settings(max_examples=50)
def test_minijava::mainclass_instantiation(instance):
    assert isinstance(instance, miniJava::MainClass)

@given(instance=miniJava::Program_strategy)
@settings(max_examples=50)
def test_minijava::program_instantiation(instance):
    assert isinstance(instance, miniJava::Program)
