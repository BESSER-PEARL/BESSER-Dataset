import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AssignmentStmt,
    Statement,
    codemodel::statements::IfStmt,
    codemodel::statements::CompositeStmt,
    codemodel::statements::AssignmentStmt,
    codemodel::statements::ForStmt,
    expressions::codemodel::Variable,
    Expression,
    codemodel::expressions::LiteralExp,
    codemodel::expressions::BinaryExp,
    codemodel::expressions::VariableExp,
    DataType,
    codemodel::ScalarType,
    codemodel::VectorType,
    codemodel::MatrixType,
    Variable,
    codemodel::LocalVariable,
    codemodel::FunctionArgument,
    codemodel::GlobalVariable,
    CMElement,
    codemodel::DataType,
    codemodel::statements::Statement,
    codemodel::Variable,
    codemodel::expressions::Expression,
    codemodel::Function,
    codemodel::CodeModule,
    codemodel::CMElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_assignmentstmt_is_not_abstract():
    assert not inspect.isabstract(AssignmentStmt)


def test_assignmentstmt_constructor_exists():
    assert callable(AssignmentStmt.__init__)


def test_assignmentstmt_constructor_args():
    sig = inspect.signature(AssignmentStmt.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::ifstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::IfStmt)


def test_codemodel::statements::ifstmt_constructor_exists():
    assert callable(codemodel::statements::IfStmt.__init__)


def test_codemodel::statements::ifstmt_constructor_args():
    sig = inspect.signature(codemodel::statements::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::compositestmt_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::CompositeStmt)


def test_codemodel::statements::compositestmt_constructor_exists():
    assert callable(codemodel::statements::CompositeStmt.__init__)


def test_codemodel::statements::compositestmt_constructor_args():
    sig = inspect.signature(codemodel::statements::CompositeStmt.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::assignmentstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::AssignmentStmt)


def test_codemodel::statements::assignmentstmt_constructor_exists():
    assert callable(codemodel::statements::AssignmentStmt.__init__)


def test_codemodel::statements::assignmentstmt_constructor_args():
    sig = inspect.signature(codemodel::statements::AssignmentStmt.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::forstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::ForStmt)


def test_codemodel::statements::forstmt_constructor_exists():
    assert callable(codemodel::statements::ForStmt.__init__)


def test_codemodel::statements::forstmt_constructor_args():
    sig = inspect.signature(codemodel::statements::ForStmt.__init__)
    params = list(sig.parameters.keys())



def test_expressions::codemodel::variable_is_not_abstract():
    assert not inspect.isabstract(expressions::codemodel::Variable)


def test_expressions::codemodel::variable_constructor_exists():
    assert callable(expressions::codemodel::Variable.__init__)


def test_expressions::codemodel::variable_constructor_args():
    sig = inspect.signature(expressions::codemodel::Variable.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::expressions::literalexp_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::LiteralExp)


def test_codemodel::expressions::literalexp_constructor_exists():
    assert callable(codemodel::expressions::LiteralExp.__init__)


def test_codemodel::expressions::literalexp_constructor_args():
    sig = inspect.signature(codemodel::expressions::LiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_codemodel::expressions::literalexp_has_value():
    assert hasattr(codemodel::expressions::LiteralExp, "value")
    descriptor = None
    for klass in codemodel::expressions::LiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::expressions::binaryexp_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::BinaryExp)


def test_codemodel::expressions::binaryexp_constructor_exists():
    assert callable(codemodel::expressions::BinaryExp.__init__)


def test_codemodel::expressions::binaryexp_constructor_args():
    sig = inspect.signature(codemodel::expressions::BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_codemodel::expressions::binaryexp_has_operator():
    assert hasattr(codemodel::expressions::BinaryExp, "operator")
    descriptor = None
    for klass in codemodel::expressions::BinaryExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::expressions::variableexp_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::VariableExp)


def test_codemodel::expressions::variableexp_constructor_exists():
    assert callable(codemodel::expressions::VariableExp.__init__)


def test_codemodel::expressions::variableexp_constructor_args():
    sig = inspect.signature(codemodel::expressions::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::scalartype_is_not_abstract():
    assert not inspect.isabstract(codemodel::ScalarType)


def test_codemodel::scalartype_constructor_exists():
    assert callable(codemodel::ScalarType.__init__)


def test_codemodel::scalartype_constructor_args():
    sig = inspect.signature(codemodel::ScalarType.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::vectortype_is_not_abstract():
    assert not inspect.isabstract(codemodel::VectorType)


def test_codemodel::vectortype_constructor_exists():
    assert callable(codemodel::VectorType.__init__)


def test_codemodel::vectortype_constructor_args():
    sig = inspect.signature(codemodel::VectorType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_codemodel::vectortype_has_size():
    assert hasattr(codemodel::VectorType, "size")
    descriptor = None
    for klass in codemodel::VectorType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::matrixtype_is_not_abstract():
    assert not inspect.isabstract(codemodel::MatrixType)


def test_codemodel::matrixtype_constructor_exists():
    assert callable(codemodel::MatrixType.__init__)


def test_codemodel::matrixtype_constructor_args():
    sig = inspect.signature(codemodel::MatrixType.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"
    assert "columns" in params, "Missing parameter 'columns'"

def test_codemodel::matrixtype_has_rows():
    assert hasattr(codemodel::MatrixType, "rows")
    descriptor = None
    for klass in codemodel::MatrixType.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_codemodel::matrixtype_has_columns():
    assert hasattr(codemodel::MatrixType, "columns")
    descriptor = None
    for klass in codemodel::MatrixType.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::localvariable_is_not_abstract():
    assert not inspect.isabstract(codemodel::LocalVariable)


def test_codemodel::localvariable_constructor_exists():
    assert callable(codemodel::LocalVariable.__init__)


def test_codemodel::localvariable_constructor_args():
    sig = inspect.signature(codemodel::LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::functionargument_is_not_abstract():
    assert not inspect.isabstract(codemodel::FunctionArgument)


def test_codemodel::functionargument_constructor_exists():
    assert callable(codemodel::FunctionArgument.__init__)


def test_codemodel::functionargument_constructor_args():
    sig = inspect.signature(codemodel::FunctionArgument.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::globalvariable_is_not_abstract():
    assert not inspect.isabstract(codemodel::GlobalVariable)


def test_codemodel::globalvariable_constructor_exists():
    assert callable(codemodel::GlobalVariable.__init__)


def test_codemodel::globalvariable_constructor_args():
    sig = inspect.signature(codemodel::GlobalVariable.__init__)
    params = list(sig.parameters.keys())



def test_cmelement_is_not_abstract():
    assert not inspect.isabstract(CMElement)


def test_cmelement_constructor_exists():
    assert callable(CMElement.__init__)


def test_cmelement_constructor_args():
    sig = inspect.signature(CMElement.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::datatype_is_not_abstract():
    assert not inspect.isabstract(codemodel::DataType)


def test_codemodel::datatype_constructor_exists():
    assert callable(codemodel::DataType.__init__)


def test_codemodel::datatype_constructor_args():
    sig = inspect.signature(codemodel::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "basetype" in params, "Missing parameter 'basetype'"

def test_codemodel::datatype_has_basetype():
    assert hasattr(codemodel::DataType, "basetype")
    descriptor = None
    for klass in codemodel::DataType.__mro__:
        if "basetype" in klass.__dict__:
            descriptor = klass.__dict__["basetype"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::statements::statement_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::Statement)


def test_codemodel::statements::statement_constructor_exists():
    assert callable(codemodel::statements::Statement.__init__)


def test_codemodel::statements::statement_constructor_args():
    sig = inspect.signature(codemodel::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::variable_is_not_abstract():
    assert not inspect.isabstract(codemodel::Variable)


def test_codemodel::variable_constructor_exists():
    assert callable(codemodel::Variable.__init__)


def test_codemodel::variable_constructor_args():
    sig = inspect.signature(codemodel::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_codemodel::variable_has_constant():
    assert hasattr(codemodel::Variable, "constant")
    descriptor = None
    for klass in codemodel::Variable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_codemodel::variable_has_identifier():
    assert hasattr(codemodel::Variable, "identifier")
    descriptor = None
    for klass in codemodel::Variable.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::Expression)


def test_codemodel::expressions::expression_constructor_exists():
    assert callable(codemodel::expressions::Expression.__init__)


def test_codemodel::expressions::expression_constructor_args():
    sig = inspect.signature(codemodel::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::function_is_not_abstract():
    assert not inspect.isabstract(codemodel::Function)


def test_codemodel::function_constructor_exists():
    assert callable(codemodel::Function.__init__)


def test_codemodel::function_constructor_args():
    sig = inspect.signature(codemodel::Function.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_codemodel::function_has_identifier():
    assert hasattr(codemodel::Function, "identifier")
    descriptor = None
    for klass in codemodel::Function.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::codemodule_is_not_abstract():
    assert not inspect.isabstract(codemodel::CodeModule)


def test_codemodel::codemodule_constructor_exists():
    assert callable(codemodel::CodeModule.__init__)


def test_codemodel::codemodule_constructor_args():
    sig = inspect.signature(codemodel::CodeModule.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::cmelement_is_not_abstract():
    assert not inspect.isabstract(codemodel::CMElement)


def test_codemodel::cmelement_constructor_exists():
    assert callable(codemodel::CMElement.__init__)


def test_codemodel::cmelement_constructor_args():
    sig = inspect.signature(codemodel::CMElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_codemodel::cmelement_has_name():
    assert hasattr(codemodel::CMElement, "name")
    descriptor = None
    for klass in codemodel::CMElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
AssignmentStmt_strategy = st.builds(
    AssignmentStmt,
)
Statement_strategy = st.builds(
    Statement,
)
codemodel::statements::IfStmt_strategy = st.builds(
    codemodel::statements::IfStmt,
)
codemodel::statements::CompositeStmt_strategy = st.builds(
    codemodel::statements::CompositeStmt,
)
codemodel::statements::AssignmentStmt_strategy = st.builds(
    codemodel::statements::AssignmentStmt,
)
codemodel::statements::ForStmt_strategy = st.builds(
    codemodel::statements::ForStmt,
)
expressions::codemodel::Variable_strategy = st.builds(
    expressions::codemodel::Variable,
)
Expression_strategy = st.builds(
    Expression,
)
codemodel::expressions::LiteralExp_strategy = st.builds(
    codemodel::expressions::LiteralExp,
    value=
        safe_text
)
codemodel::expressions::BinaryExp_strategy = st.builds(
    codemodel::expressions::BinaryExp,
    operator=
        safe_text
)
codemodel::expressions::VariableExp_strategy = st.builds(
    codemodel::expressions::VariableExp,
)
DataType_strategy = st.builds(
    DataType,
)
codemodel::ScalarType_strategy = st.builds(
    codemodel::ScalarType,
)
codemodel::VectorType_strategy = st.builds(
    codemodel::VectorType,
    size=
        safe_text
)
codemodel::MatrixType_strategy = st.builds(
    codemodel::MatrixType,
    rows=
        safe_text,
    columns=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
codemodel::LocalVariable_strategy = st.builds(
    codemodel::LocalVariable,
)
codemodel::FunctionArgument_strategy = st.builds(
    codemodel::FunctionArgument,
)
codemodel::GlobalVariable_strategy = st.builds(
    codemodel::GlobalVariable,
)
CMElement_strategy = st.builds(
    CMElement,
)
codemodel::DataType_strategy = st.builds(
    codemodel::DataType,
    basetype=
        safe_text
)
codemodel::statements::Statement_strategy = st.builds(
    codemodel::statements::Statement,
)
codemodel::Variable_strategy = st.builds(
    codemodel::Variable,
    constant=
        st.booleans(),
    identifier=
        safe_text
)
codemodel::expressions::Expression_strategy = st.builds(
    codemodel::expressions::Expression,
)
codemodel::Function_strategy = st.builds(
    codemodel::Function,
    identifier=
        safe_text
)
codemodel::CodeModule_strategy = st.builds(
    codemodel::CodeModule,
)
codemodel::CMElement_strategy = st.builds(
    codemodel::CMElement,
    name=
        safe_text
)

@given(instance=AssignmentStmt_strategy)
@settings(max_examples=50)
def test_assignmentstmt_instantiation(instance):
    assert isinstance(instance, AssignmentStmt)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=codemodel::statements::IfStmt_strategy)
@settings(max_examples=50)
def test_codemodel::statements::ifstmt_instantiation(instance):
    assert isinstance(instance, codemodel::statements::IfStmt)

@given(instance=codemodel::statements::CompositeStmt_strategy)
@settings(max_examples=50)
def test_codemodel::statements::compositestmt_instantiation(instance):
    assert isinstance(instance, codemodel::statements::CompositeStmt)

@given(instance=codemodel::statements::AssignmentStmt_strategy)
@settings(max_examples=50)
def test_codemodel::statements::assignmentstmt_instantiation(instance):
    assert isinstance(instance, codemodel::statements::AssignmentStmt)

@given(instance=codemodel::statements::ForStmt_strategy)
@settings(max_examples=50)
def test_codemodel::statements::forstmt_instantiation(instance):
    assert isinstance(instance, codemodel::statements::ForStmt)

@given(instance=expressions::codemodel::Variable_strategy)
@settings(max_examples=50)
def test_expressions::codemodel::variable_instantiation(instance):
    assert isinstance(instance, expressions::codemodel::Variable)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=codemodel::expressions::LiteralExp_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::literalexp_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::LiteralExp)

@given(instance=codemodel::expressions::LiteralExp_strategy)
def test_codemodel::expressions::literalexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=codemodel::expressions::LiteralExp_strategy)
def test_codemodel::expressions::literalexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=codemodel::expressions::BinaryExp_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::binaryexp_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::BinaryExp)

@given(instance=codemodel::expressions::BinaryExp_strategy)
def test_codemodel::expressions::binaryexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=codemodel::expressions::BinaryExp_strategy)
def test_codemodel::expressions::binaryexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=codemodel::expressions::VariableExp_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::variableexp_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::VariableExp)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=codemodel::ScalarType_strategy)
@settings(max_examples=50)
def test_codemodel::scalartype_instantiation(instance):
    assert isinstance(instance, codemodel::ScalarType)

@given(instance=codemodel::VectorType_strategy)
@settings(max_examples=50)
def test_codemodel::vectortype_instantiation(instance):
    assert isinstance(instance, codemodel::VectorType)

@given(instance=codemodel::VectorType_strategy)
def test_codemodel::vectortype_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=codemodel::VectorType_strategy)
def test_codemodel::vectortype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=codemodel::MatrixType_strategy)
@settings(max_examples=50)
def test_codemodel::matrixtype_instantiation(instance):
    assert isinstance(instance, codemodel::MatrixType)

@given(instance=codemodel::MatrixType_strategy)
def test_codemodel::matrixtype_rows_type(instance):
    assert isinstance(instance.rows, str)


@given(instance=codemodel::MatrixType_strategy)
def test_codemodel::matrixtype_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=codemodel::MatrixType_strategy)
def test_codemodel::matrixtype_columns_type(instance):
    assert isinstance(instance.columns, str)


@given(instance=codemodel::MatrixType_strategy)
def test_codemodel::matrixtype_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=codemodel::LocalVariable_strategy)
@settings(max_examples=50)
def test_codemodel::localvariable_instantiation(instance):
    assert isinstance(instance, codemodel::LocalVariable)

@given(instance=codemodel::FunctionArgument_strategy)
@settings(max_examples=50)
def test_codemodel::functionargument_instantiation(instance):
    assert isinstance(instance, codemodel::FunctionArgument)

@given(instance=codemodel::GlobalVariable_strategy)
@settings(max_examples=50)
def test_codemodel::globalvariable_instantiation(instance):
    assert isinstance(instance, codemodel::GlobalVariable)

@given(instance=CMElement_strategy)
@settings(max_examples=50)
def test_cmelement_instantiation(instance):
    assert isinstance(instance, CMElement)

@given(instance=codemodel::DataType_strategy)
@settings(max_examples=50)
def test_codemodel::datatype_instantiation(instance):
    assert isinstance(instance, codemodel::DataType)

@given(instance=codemodel::DataType_strategy)
def test_codemodel::datatype_basetype_type(instance):
    assert isinstance(instance.basetype, str)


@given(instance=codemodel::DataType_strategy)
def test_codemodel::datatype_basetype_setter(instance):
    original = instance.basetype
    instance.basetype = original
    assert instance.basetype == original

@given(instance=codemodel::statements::Statement_strategy)
@settings(max_examples=50)
def test_codemodel::statements::statement_instantiation(instance):
    assert isinstance(instance, codemodel::statements::Statement)

@given(instance=codemodel::Variable_strategy)
@settings(max_examples=50)
def test_codemodel::variable_instantiation(instance):
    assert isinstance(instance, codemodel::Variable)

@given(instance=codemodel::Variable_strategy)
def test_codemodel::variable_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=codemodel::Variable_strategy)
def test_codemodel::variable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=codemodel::Variable_strategy)
def test_codemodel::variable_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=codemodel::Variable_strategy)
def test_codemodel::variable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=codemodel::expressions::Expression_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::expression_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::Expression)

@given(instance=codemodel::Function_strategy)
@settings(max_examples=50)
def test_codemodel::function_instantiation(instance):
    assert isinstance(instance, codemodel::Function)

@given(instance=codemodel::Function_strategy)
def test_codemodel::function_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=codemodel::Function_strategy)
def test_codemodel::function_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=codemodel::CodeModule_strategy)
@settings(max_examples=50)
def test_codemodel::codemodule_instantiation(instance):
    assert isinstance(instance, codemodel::CodeModule)

@given(instance=codemodel::CMElement_strategy)
@settings(max_examples=50)
def test_codemodel::cmelement_instantiation(instance):
    assert isinstance(instance, codemodel::CMElement)

@given(instance=codemodel::CMElement_strategy)
def test_codemodel::cmelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=codemodel::CMElement_strategy)
def test_codemodel::cmelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
