import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    codemodel::statements::CompStmt,
    codemodel::statements::AsgnStmt,
    CMElement,
    codemodel::Variable,
    codemodel::statements::Statement,
    codemodel::CodeModel,
    codemodel::CMElement,
    expressions::codemodel::Variable,
    Expression,
    codemodel::expressions::BinExp,
    codemodel::expressions::VarExp,
    codemodel::expressions::Expression,
    codemodel::E,
    codemodel::D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::compstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::CompStmt)


def test_codemodel::statements::compstmt_constructor_exists():
    assert callable(codemodel::statements::CompStmt.__init__)


def test_codemodel::statements::compstmt_constructor_args():
    sig = inspect.signature(codemodel::statements::CompStmt.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::asgnstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::AsgnStmt)


def test_codemodel::statements::asgnstmt_constructor_exists():
    assert callable(codemodel::statements::AsgnStmt.__init__)


def test_codemodel::statements::asgnstmt_constructor_args():
    sig = inspect.signature(codemodel::statements::AsgnStmt.__init__)
    params = list(sig.parameters.keys())



def test_cmelement_is_not_abstract():
    assert not inspect.isabstract(CMElement)


def test_cmelement_constructor_exists():
    assert callable(CMElement.__init__)


def test_cmelement_constructor_args():
    sig = inspect.signature(CMElement.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::variable_is_not_abstract():
    assert not inspect.isabstract(codemodel::Variable)


def test_codemodel::variable_constructor_exists():
    assert callable(codemodel::Variable.__init__)


def test_codemodel::variable_constructor_args():
    sig = inspect.signature(codemodel::Variable.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::statements::statement_is_not_abstract():
    assert not inspect.isabstract(codemodel::statements::Statement)


def test_codemodel::statements::statement_constructor_exists():
    assert callable(codemodel::statements::Statement.__init__)


def test_codemodel::statements::statement_constructor_args():
    sig = inspect.signature(codemodel::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::codemodel_is_not_abstract():
    assert not inspect.isabstract(codemodel::CodeModel)


def test_codemodel::codemodel_constructor_exists():
    assert callable(codemodel::CodeModel.__init__)


def test_codemodel::codemodel_constructor_args():
    sig = inspect.signature(codemodel::CodeModel.__init__)
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



def test_codemodel::expressions::binexp_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::BinExp)


def test_codemodel::expressions::binexp_constructor_exists():
    assert callable(codemodel::expressions::BinExp.__init__)


def test_codemodel::expressions::binexp_constructor_args():
    sig = inspect.signature(codemodel::expressions::BinExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_codemodel::expressions::binexp_has_operator():
    assert hasattr(codemodel::expressions::BinExp, "operator")
    descriptor = None
    for klass in codemodel::expressions::BinExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_codemodel::expressions::varexp_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::VarExp)


def test_codemodel::expressions::varexp_constructor_exists():
    assert callable(codemodel::expressions::VarExp.__init__)


def test_codemodel::expressions::varexp_constructor_args():
    sig = inspect.signature(codemodel::expressions::VarExp.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(codemodel::expressions::Expression)


def test_codemodel::expressions::expression_constructor_exists():
    assert callable(codemodel::expressions::Expression.__init__)


def test_codemodel::expressions::expression_constructor_args():
    sig = inspect.signature(codemodel::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::e_is_not_abstract():
    assert not inspect.isabstract(codemodel::E)


def test_codemodel::e_constructor_exists():
    assert callable(codemodel::E.__init__)


def test_codemodel::e_constructor_args():
    sig = inspect.signature(codemodel::E.__init__)
    params = list(sig.parameters.keys())



def test_codemodel::d_is_not_abstract():
    assert not inspect.isabstract(codemodel::D)


def test_codemodel::d_constructor_exists():
    assert callable(codemodel::D.__init__)


def test_codemodel::d_constructor_args():
    sig = inspect.signature(codemodel::D.__init__)
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
Statement_strategy = st.builds(
    Statement,
)
codemodel::statements::CompStmt_strategy = st.builds(
    codemodel::statements::CompStmt,
)
codemodel::statements::AsgnStmt_strategy = st.builds(
    codemodel::statements::AsgnStmt,
)
CMElement_strategy = st.builds(
    CMElement,
)
codemodel::Variable_strategy = st.builds(
    codemodel::Variable,
)
codemodel::statements::Statement_strategy = st.builds(
    codemodel::statements::Statement,
)
codemodel::CodeModel_strategy = st.builds(
    codemodel::CodeModel,
)
codemodel::CMElement_strategy = st.builds(
    codemodel::CMElement,
    name=
        safe_text
)
expressions::codemodel::Variable_strategy = st.builds(
    expressions::codemodel::Variable,
)
Expression_strategy = st.builds(
    Expression,
)
codemodel::expressions::BinExp_strategy = st.builds(
    codemodel::expressions::BinExp,
    operator=
        safe_text
)
codemodel::expressions::VarExp_strategy = st.builds(
    codemodel::expressions::VarExp,
)
codemodel::expressions::Expression_strategy = st.builds(
    codemodel::expressions::Expression,
)
codemodel::E_strategy = st.builds(
    codemodel::E,
)
codemodel::D_strategy = st.builds(
    codemodel::D,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=codemodel::statements::CompStmt_strategy)
@settings(max_examples=50)
def test_codemodel::statements::compstmt_instantiation(instance):
    assert isinstance(instance, codemodel::statements::CompStmt)

@given(instance=codemodel::statements::AsgnStmt_strategy)
@settings(max_examples=50)
def test_codemodel::statements::asgnstmt_instantiation(instance):
    assert isinstance(instance, codemodel::statements::AsgnStmt)

@given(instance=CMElement_strategy)
@settings(max_examples=50)
def test_cmelement_instantiation(instance):
    assert isinstance(instance, CMElement)

@given(instance=codemodel::Variable_strategy)
@settings(max_examples=50)
def test_codemodel::variable_instantiation(instance):
    assert isinstance(instance, codemodel::Variable)

@given(instance=codemodel::statements::Statement_strategy)
@settings(max_examples=50)
def test_codemodel::statements::statement_instantiation(instance):
    assert isinstance(instance, codemodel::statements::Statement)

@given(instance=codemodel::CodeModel_strategy)
@settings(max_examples=50)
def test_codemodel::codemodel_instantiation(instance):
    assert isinstance(instance, codemodel::CodeModel)

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

@given(instance=expressions::codemodel::Variable_strategy)
@settings(max_examples=50)
def test_expressions::codemodel::variable_instantiation(instance):
    assert isinstance(instance, expressions::codemodel::Variable)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=codemodel::expressions::BinExp_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::binexp_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::BinExp)

@given(instance=codemodel::expressions::BinExp_strategy)
def test_codemodel::expressions::binexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=codemodel::expressions::BinExp_strategy)
def test_codemodel::expressions::binexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=codemodel::expressions::VarExp_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::varexp_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::VarExp)

@given(instance=codemodel::expressions::Expression_strategy)
@settings(max_examples=50)
def test_codemodel::expressions::expression_instantiation(instance):
    assert isinstance(instance, codemodel::expressions::Expression)

@given(instance=codemodel::E_strategy)
@settings(max_examples=50)
def test_codemodel::e_instantiation(instance):
    assert isinstance(instance, codemodel::E)

@given(instance=codemodel::D_strategy)
@settings(max_examples=50)
def test_codemodel::d_instantiation(instance):
    assert isinstance(instance, codemodel::D)
