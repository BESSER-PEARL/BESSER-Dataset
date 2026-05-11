import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    javali::Relation,
    javali::Equality,
    javali::Multiplication,
    javali::Addition,
    javali::And,
    javali::Xor,
    javali::Or,
    javali::NewObject,
    javali::NewArray,
    javali::Null,
    javali::VarExpression,
    javali::Procedure,
    javali::Record,
    javali::Constant,
    javali::Module,
    javali::Expression,
    Statement,
    javali::Continue,
    javali::While,
    javali::IfElse,
    javali::VarAssign,
    javali::Increment,
    javali::DoWhile,
    javali::ProcCall,
    javali::Decrement,
    javali::Break,
    javali::For,
    javali::Return,
    javali::Statement,
    javali::Block,
    javali::VarDeclaration,
    javali::Literal,
    javali::Identifier,
    javali::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javali::relation_is_not_abstract():
    assert not inspect.isabstract(javali::Relation)


def test_javali::relation_constructor_exists():
    assert callable(javali::Relation.__init__)


def test_javali::relation_constructor_args():
    sig = inspect.signature(javali::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javali::relation_has_operator():
    assert hasattr(javali::Relation, "operator")
    descriptor = None
    for klass in javali::Relation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javali::equality_is_not_abstract():
    assert not inspect.isabstract(javali::Equality)


def test_javali::equality_constructor_exists():
    assert callable(javali::Equality.__init__)


def test_javali::equality_constructor_args():
    sig = inspect.signature(javali::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javali::equality_has_operator():
    assert hasattr(javali::Equality, "operator")
    descriptor = None
    for klass in javali::Equality.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javali::multiplication_is_not_abstract():
    assert not inspect.isabstract(javali::Multiplication)


def test_javali::multiplication_constructor_exists():
    assert callable(javali::Multiplication.__init__)


def test_javali::multiplication_constructor_args():
    sig = inspect.signature(javali::Multiplication.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javali::multiplication_has_operator():
    assert hasattr(javali::Multiplication, "operator")
    descriptor = None
    for klass in javali::Multiplication.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javali::addition_is_not_abstract():
    assert not inspect.isabstract(javali::Addition)


def test_javali::addition_constructor_exists():
    assert callable(javali::Addition.__init__)


def test_javali::addition_constructor_args():
    sig = inspect.signature(javali::Addition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javali::addition_has_operator():
    assert hasattr(javali::Addition, "operator")
    descriptor = None
    for klass in javali::Addition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javali::and_is_not_abstract():
    assert not inspect.isabstract(javali::And)


def test_javali::and_constructor_exists():
    assert callable(javali::And.__init__)


def test_javali::and_constructor_args():
    sig = inspect.signature(javali::And.__init__)
    params = list(sig.parameters.keys())



def test_javali::xor_is_not_abstract():
    assert not inspect.isabstract(javali::Xor)


def test_javali::xor_constructor_exists():
    assert callable(javali::Xor.__init__)


def test_javali::xor_constructor_args():
    sig = inspect.signature(javali::Xor.__init__)
    params = list(sig.parameters.keys())



def test_javali::or_is_not_abstract():
    assert not inspect.isabstract(javali::Or)


def test_javali::or_constructor_exists():
    assert callable(javali::Or.__init__)


def test_javali::or_constructor_args():
    sig = inspect.signature(javali::Or.__init__)
    params = list(sig.parameters.keys())



def test_javali::newobject_is_not_abstract():
    assert not inspect.isabstract(javali::NewObject)


def test_javali::newobject_constructor_exists():
    assert callable(javali::NewObject.__init__)


def test_javali::newobject_constructor_args():
    sig = inspect.signature(javali::NewObject.__init__)
    params = list(sig.parameters.keys())



def test_javali::newarray_is_not_abstract():
    assert not inspect.isabstract(javali::NewArray)


def test_javali::newarray_constructor_exists():
    assert callable(javali::NewArray.__init__)


def test_javali::newarray_constructor_args():
    sig = inspect.signature(javali::NewArray.__init__)
    params = list(sig.parameters.keys())



def test_javali::null_is_not_abstract():
    assert not inspect.isabstract(javali::Null)


def test_javali::null_constructor_exists():
    assert callable(javali::Null.__init__)


def test_javali::null_constructor_args():
    sig = inspect.signature(javali::Null.__init__)
    params = list(sig.parameters.keys())



def test_javali::varexpression_is_not_abstract():
    assert not inspect.isabstract(javali::VarExpression)


def test_javali::varexpression_constructor_exists():
    assert callable(javali::VarExpression.__init__)


def test_javali::varexpression_constructor_args():
    sig = inspect.signature(javali::VarExpression.__init__)
    params = list(sig.parameters.keys())



def test_javali::procedure_is_not_abstract():
    assert not inspect.isabstract(javali::Procedure)


def test_javali::procedure_constructor_exists():
    assert callable(javali::Procedure.__init__)


def test_javali::procedure_constructor_args():
    sig = inspect.signature(javali::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "void" in params, "Missing parameter 'void'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "static" in params, "Missing parameter 'static'"

def test_javali::procedure_has_void():
    assert hasattr(javali::Procedure, "void")
    descriptor = None
    for klass in javali::Procedure.__mro__:
        if "void" in klass.__dict__:
            descriptor = klass.__dict__["void"]
            break
    assert isinstance(descriptor, property)

def test_javali::procedure_has_comment():
    assert hasattr(javali::Procedure, "comment")
    descriptor = None
    for klass in javali::Procedure.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_javali::procedure_has_static():
    assert hasattr(javali::Procedure, "static")
    descriptor = None
    for klass in javali::Procedure.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_javali::record_is_not_abstract():
    assert not inspect.isabstract(javali::Record)


def test_javali::record_constructor_exists():
    assert callable(javali::Record.__init__)


def test_javali::record_constructor_args():
    sig = inspect.signature(javali::Record.__init__)
    params = list(sig.parameters.keys())



def test_javali::constant_is_not_abstract():
    assert not inspect.isabstract(javali::Constant)


def test_javali::constant_constructor_exists():
    assert callable(javali::Constant.__init__)


def test_javali::constant_constructor_args():
    sig = inspect.signature(javali::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_javali::constant_has_static():
    assert hasattr(javali::Constant, "static")
    descriptor = None
    for klass in javali::Constant.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_javali::module_is_not_abstract():
    assert not inspect.isabstract(javali::Module)


def test_javali::module_constructor_exists():
    assert callable(javali::Module.__init__)


def test_javali::module_constructor_args():
    sig = inspect.signature(javali::Module.__init__)
    params = list(sig.parameters.keys())



def test_javali::expression_is_not_abstract():
    assert not inspect.isabstract(javali::Expression)


def test_javali::expression_constructor_exists():
    assert callable(javali::Expression.__init__)


def test_javali::expression_constructor_args():
    sig = inspect.signature(javali::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javali::continue_is_not_abstract():
    assert not inspect.isabstract(javali::Continue)


def test_javali::continue_constructor_exists():
    assert callable(javali::Continue.__init__)


def test_javali::continue_constructor_args():
    sig = inspect.signature(javali::Continue.__init__)
    params = list(sig.parameters.keys())



def test_javali::while_is_not_abstract():
    assert not inspect.isabstract(javali::While)


def test_javali::while_constructor_exists():
    assert callable(javali::While.__init__)


def test_javali::while_constructor_args():
    sig = inspect.signature(javali::While.__init__)
    params = list(sig.parameters.keys())



def test_javali::ifelse_is_not_abstract():
    assert not inspect.isabstract(javali::IfElse)


def test_javali::ifelse_constructor_exists():
    assert callable(javali::IfElse.__init__)


def test_javali::ifelse_constructor_args():
    sig = inspect.signature(javali::IfElse.__init__)
    params = list(sig.parameters.keys())



def test_javali::varassign_is_not_abstract():
    assert not inspect.isabstract(javali::VarAssign)


def test_javali::varassign_constructor_exists():
    assert callable(javali::VarAssign.__init__)


def test_javali::varassign_constructor_args():
    sig = inspect.signature(javali::VarAssign.__init__)
    params = list(sig.parameters.keys())



def test_javali::increment_is_not_abstract():
    assert not inspect.isabstract(javali::Increment)


def test_javali::increment_constructor_exists():
    assert callable(javali::Increment.__init__)


def test_javali::increment_constructor_args():
    sig = inspect.signature(javali::Increment.__init__)
    params = list(sig.parameters.keys())



def test_javali::dowhile_is_not_abstract():
    assert not inspect.isabstract(javali::DoWhile)


def test_javali::dowhile_constructor_exists():
    assert callable(javali::DoWhile.__init__)


def test_javali::dowhile_constructor_args():
    sig = inspect.signature(javali::DoWhile.__init__)
    params = list(sig.parameters.keys())



def test_javali::proccall_is_not_abstract():
    assert not inspect.isabstract(javali::ProcCall)


def test_javali::proccall_constructor_exists():
    assert callable(javali::ProcCall.__init__)


def test_javali::proccall_constructor_args():
    sig = inspect.signature(javali::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_javali::decrement_is_not_abstract():
    assert not inspect.isabstract(javali::Decrement)


def test_javali::decrement_constructor_exists():
    assert callable(javali::Decrement.__init__)


def test_javali::decrement_constructor_args():
    sig = inspect.signature(javali::Decrement.__init__)
    params = list(sig.parameters.keys())



def test_javali::break_is_not_abstract():
    assert not inspect.isabstract(javali::Break)


def test_javali::break_constructor_exists():
    assert callable(javali::Break.__init__)


def test_javali::break_constructor_args():
    sig = inspect.signature(javali::Break.__init__)
    params = list(sig.parameters.keys())



def test_javali::for_is_not_abstract():
    assert not inspect.isabstract(javali::For)


def test_javali::for_constructor_exists():
    assert callable(javali::For.__init__)


def test_javali::for_constructor_args():
    sig = inspect.signature(javali::For.__init__)
    params = list(sig.parameters.keys())



def test_javali::return_is_not_abstract():
    assert not inspect.isabstract(javali::Return)


def test_javali::return_constructor_exists():
    assert callable(javali::Return.__init__)


def test_javali::return_constructor_args():
    sig = inspect.signature(javali::Return.__init__)
    params = list(sig.parameters.keys())



def test_javali::statement_is_not_abstract():
    assert not inspect.isabstract(javali::Statement)


def test_javali::statement_constructor_exists():
    assert callable(javali::Statement.__init__)


def test_javali::statement_constructor_args():
    sig = inspect.signature(javali::Statement.__init__)
    params = list(sig.parameters.keys())



def test_javali::block_is_not_abstract():
    assert not inspect.isabstract(javali::Block)


def test_javali::block_constructor_exists():
    assert callable(javali::Block.__init__)


def test_javali::block_constructor_args():
    sig = inspect.signature(javali::Block.__init__)
    params = list(sig.parameters.keys())



def test_javali::vardeclaration_is_not_abstract():
    assert not inspect.isabstract(javali::VarDeclaration)


def test_javali::vardeclaration_constructor_exists():
    assert callable(javali::VarDeclaration.__init__)


def test_javali::vardeclaration_constructor_args():
    sig = inspect.signature(javali::VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javali::literal_is_not_abstract():
    assert not inspect.isabstract(javali::Literal)


def test_javali::literal_constructor_exists():
    assert callable(javali::Literal.__init__)


def test_javali::literal_constructor_args():
    sig = inspect.signature(javali::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_javali::literal_has_value():
    assert hasattr(javali::Literal, "value")
    descriptor = None
    for klass in javali::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_javali::identifier_is_not_abstract():
    assert not inspect.isabstract(javali::Identifier)


def test_javali::identifier_constructor_exists():
    assert callable(javali::Identifier.__init__)


def test_javali::identifier_constructor_args():
    sig = inspect.signature(javali::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_javali::identifier_has_id():
    assert hasattr(javali::Identifier, "id")
    descriptor = None
    for klass in javali::Identifier.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_javali::type_is_not_abstract():
    assert not inspect.isabstract(javali::Type)


def test_javali::type_constructor_exists():
    assert callable(javali::Type.__init__)


def test_javali::type_constructor_args():
    sig = inspect.signature(javali::Type.__init__)
    params = list(sig.parameters.keys())
    assert "arrayDims" in params, "Missing parameter 'arrayDims'"

def test_javali::type_has_arrayDims():
    assert hasattr(javali::Type, "arrayDims")
    descriptor = None
    for klass in javali::Type.__mro__:
        if "arrayDims" in klass.__dict__:
            descriptor = klass.__dict__["arrayDims"]
            break
    assert isinstance(descriptor, property)


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
Expression_strategy = st.builds(
    Expression,
)
javali::Relation_strategy = st.builds(
    javali::Relation,
    operator=
        safe_text
)
javali::Equality_strategy = st.builds(
    javali::Equality,
    operator=
        safe_text
)
javali::Multiplication_strategy = st.builds(
    javali::Multiplication,
    operator=
        safe_text
)
javali::Addition_strategy = st.builds(
    javali::Addition,
    operator=
        safe_text
)
javali::And_strategy = st.builds(
    javali::And,
)
javali::Xor_strategy = st.builds(
    javali::Xor,
)
javali::Or_strategy = st.builds(
    javali::Or,
)
javali::NewObject_strategy = st.builds(
    javali::NewObject,
)
javali::NewArray_strategy = st.builds(
    javali::NewArray,
)
javali::Null_strategy = st.builds(
    javali::Null,
)
javali::VarExpression_strategy = st.builds(
    javali::VarExpression,
)
javali::Procedure_strategy = st.builds(
    javali::Procedure,
    void=
        st.booleans(),
    comment=
        safe_text,
    static=
        st.booleans()
)
javali::Record_strategy = st.builds(
    javali::Record,
)
javali::Constant_strategy = st.builds(
    javali::Constant,
    static=
        st.booleans()
)
javali::Module_strategy = st.builds(
    javali::Module,
)
javali::Expression_strategy = st.builds(
    javali::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
javali::Continue_strategy = st.builds(
    javali::Continue,
)
javali::While_strategy = st.builds(
    javali::While,
)
javali::IfElse_strategy = st.builds(
    javali::IfElse,
)
javali::VarAssign_strategy = st.builds(
    javali::VarAssign,
)
javali::Increment_strategy = st.builds(
    javali::Increment,
)
javali::DoWhile_strategy = st.builds(
    javali::DoWhile,
)
javali::ProcCall_strategy = st.builds(
    javali::ProcCall,
)
javali::Decrement_strategy = st.builds(
    javali::Decrement,
)
javali::Break_strategy = st.builds(
    javali::Break,
)
javali::For_strategy = st.builds(
    javali::For,
)
javali::Return_strategy = st.builds(
    javali::Return,
)
javali::Statement_strategy = st.builds(
    javali::Statement,
)
javali::Block_strategy = st.builds(
    javali::Block,
)
javali::VarDeclaration_strategy = st.builds(
    javali::VarDeclaration,
)
javali::Literal_strategy = st.builds(
    javali::Literal,
    value=
        safe_text
)
javali::Identifier_strategy = st.builds(
    javali::Identifier,
    id=
        safe_text
)
javali::Type_strategy = st.builds(
    javali::Type,
    arrayDims=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=javali::Relation_strategy)
@settings(max_examples=50)
def test_javali::relation_instantiation(instance):
    assert isinstance(instance, javali::Relation)

@given(instance=javali::Relation_strategy)
def test_javali::relation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=javali::Relation_strategy)
def test_javali::relation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=javali::Equality_strategy)
@settings(max_examples=50)
def test_javali::equality_instantiation(instance):
    assert isinstance(instance, javali::Equality)

@given(instance=javali::Equality_strategy)
def test_javali::equality_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=javali::Equality_strategy)
def test_javali::equality_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=javali::Multiplication_strategy)
@settings(max_examples=50)
def test_javali::multiplication_instantiation(instance):
    assert isinstance(instance, javali::Multiplication)

@given(instance=javali::Multiplication_strategy)
def test_javali::multiplication_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=javali::Multiplication_strategy)
def test_javali::multiplication_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=javali::Addition_strategy)
@settings(max_examples=50)
def test_javali::addition_instantiation(instance):
    assert isinstance(instance, javali::Addition)

@given(instance=javali::Addition_strategy)
def test_javali::addition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=javali::Addition_strategy)
def test_javali::addition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=javali::And_strategy)
@settings(max_examples=50)
def test_javali::and_instantiation(instance):
    assert isinstance(instance, javali::And)

@given(instance=javali::Xor_strategy)
@settings(max_examples=50)
def test_javali::xor_instantiation(instance):
    assert isinstance(instance, javali::Xor)

@given(instance=javali::Or_strategy)
@settings(max_examples=50)
def test_javali::or_instantiation(instance):
    assert isinstance(instance, javali::Or)

@given(instance=javali::NewObject_strategy)
@settings(max_examples=50)
def test_javali::newobject_instantiation(instance):
    assert isinstance(instance, javali::NewObject)

@given(instance=javali::NewArray_strategy)
@settings(max_examples=50)
def test_javali::newarray_instantiation(instance):
    assert isinstance(instance, javali::NewArray)

@given(instance=javali::Null_strategy)
@settings(max_examples=50)
def test_javali::null_instantiation(instance):
    assert isinstance(instance, javali::Null)

@given(instance=javali::VarExpression_strategy)
@settings(max_examples=50)
def test_javali::varexpression_instantiation(instance):
    assert isinstance(instance, javali::VarExpression)

@given(instance=javali::Procedure_strategy)
@settings(max_examples=50)
def test_javali::procedure_instantiation(instance):
    assert isinstance(instance, javali::Procedure)

@given(instance=javali::Procedure_strategy)
def test_javali::procedure_void_type(instance):
    assert isinstance(instance.void, bool)


@given(instance=javali::Procedure_strategy)
def test_javali::procedure_void_setter(instance):
    original = instance.void
    instance.void = original
    assert instance.void == original

@given(instance=javali::Procedure_strategy)
def test_javali::procedure_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=javali::Procedure_strategy)
def test_javali::procedure_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=javali::Procedure_strategy)
def test_javali::procedure_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=javali::Procedure_strategy)
def test_javali::procedure_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=javali::Record_strategy)
@settings(max_examples=50)
def test_javali::record_instantiation(instance):
    assert isinstance(instance, javali::Record)

@given(instance=javali::Constant_strategy)
@settings(max_examples=50)
def test_javali::constant_instantiation(instance):
    assert isinstance(instance, javali::Constant)

@given(instance=javali::Constant_strategy)
def test_javali::constant_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=javali::Constant_strategy)
def test_javali::constant_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=javali::Module_strategy)
@settings(max_examples=50)
def test_javali::module_instantiation(instance):
    assert isinstance(instance, javali::Module)

@given(instance=javali::Expression_strategy)
@settings(max_examples=50)
def test_javali::expression_instantiation(instance):
    assert isinstance(instance, javali::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=javali::Continue_strategy)
@settings(max_examples=50)
def test_javali::continue_instantiation(instance):
    assert isinstance(instance, javali::Continue)

@given(instance=javali::While_strategy)
@settings(max_examples=50)
def test_javali::while_instantiation(instance):
    assert isinstance(instance, javali::While)

@given(instance=javali::IfElse_strategy)
@settings(max_examples=50)
def test_javali::ifelse_instantiation(instance):
    assert isinstance(instance, javali::IfElse)

@given(instance=javali::VarAssign_strategy)
@settings(max_examples=50)
def test_javali::varassign_instantiation(instance):
    assert isinstance(instance, javali::VarAssign)

@given(instance=javali::Increment_strategy)
@settings(max_examples=50)
def test_javali::increment_instantiation(instance):
    assert isinstance(instance, javali::Increment)

@given(instance=javali::DoWhile_strategy)
@settings(max_examples=50)
def test_javali::dowhile_instantiation(instance):
    assert isinstance(instance, javali::DoWhile)

@given(instance=javali::ProcCall_strategy)
@settings(max_examples=50)
def test_javali::proccall_instantiation(instance):
    assert isinstance(instance, javali::ProcCall)

@given(instance=javali::Decrement_strategy)
@settings(max_examples=50)
def test_javali::decrement_instantiation(instance):
    assert isinstance(instance, javali::Decrement)

@given(instance=javali::Break_strategy)
@settings(max_examples=50)
def test_javali::break_instantiation(instance):
    assert isinstance(instance, javali::Break)

@given(instance=javali::For_strategy)
@settings(max_examples=50)
def test_javali::for_instantiation(instance):
    assert isinstance(instance, javali::For)

@given(instance=javali::Return_strategy)
@settings(max_examples=50)
def test_javali::return_instantiation(instance):
    assert isinstance(instance, javali::Return)

@given(instance=javali::Statement_strategy)
@settings(max_examples=50)
def test_javali::statement_instantiation(instance):
    assert isinstance(instance, javali::Statement)

@given(instance=javali::Block_strategy)
@settings(max_examples=50)
def test_javali::block_instantiation(instance):
    assert isinstance(instance, javali::Block)

@given(instance=javali::VarDeclaration_strategy)
@settings(max_examples=50)
def test_javali::vardeclaration_instantiation(instance):
    assert isinstance(instance, javali::VarDeclaration)

@given(instance=javali::Literal_strategy)
@settings(max_examples=50)
def test_javali::literal_instantiation(instance):
    assert isinstance(instance, javali::Literal)

@given(instance=javali::Literal_strategy)
def test_javali::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=javali::Literal_strategy)
def test_javali::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=javali::Identifier_strategy)
@settings(max_examples=50)
def test_javali::identifier_instantiation(instance):
    assert isinstance(instance, javali::Identifier)

@given(instance=javali::Identifier_strategy)
def test_javali::identifier_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=javali::Identifier_strategy)
def test_javali::identifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=javali::Type_strategy)
@settings(max_examples=50)
def test_javali::type_instantiation(instance):
    assert isinstance(instance, javali::Type)

@given(instance=javali::Type_strategy)
def test_javali::type_arrayDims_type(instance):
    assert isinstance(instance.arrayDims, str)


@given(instance=javali::Type_strategy)
def test_javali::type_arrayDims_setter(instance):
    original = instance.arrayDims
    instance.arrayDims = original
    assert instance.arrayDims == original
