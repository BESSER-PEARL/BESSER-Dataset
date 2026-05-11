import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TermReference,
    mprologTermReference::VariableReference,
    mprologTermReference::FunctorReference,
    mprologTermReference::Operator,
    Term,
    mprologTermReference::Parenthesis,
    mprologTermReference::List,
    mprologTermReference::QuotedAtom,
    mprologTermReference::TermReference,
    mprologTermReference::InfixExpression,
    mprologTermReference::Variable,
    mprologTermReference::Term,
    mprologTermReference::Functor,
    mprologTermReference::Body,
    mprologTermReference::Head,
    mprologTermReference::Clause,
    mprologTermReference::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_termreference_is_not_abstract():
    assert not inspect.isabstract(TermReference)


def test_termreference_constructor_exists():
    assert callable(TermReference.__init__)


def test_termreference_constructor_args():
    sig = inspect.signature(TermReference.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::variablereference_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::VariableReference)


def test_mprologtermreference::variablereference_constructor_exists():
    assert callable(mprologTermReference::VariableReference.__init__)


def test_mprologtermreference::variablereference_constructor_args():
    sig = inspect.signature(mprologTermReference::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::functorreference_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::FunctorReference)


def test_mprologtermreference::functorreference_constructor_exists():
    assert callable(mprologTermReference::FunctorReference.__init__)


def test_mprologtermreference::functorreference_constructor_args():
    sig = inspect.signature(mprologTermReference::FunctorReference.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::operator_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Operator)


def test_mprologtermreference::operator_constructor_exists():
    assert callable(mprologTermReference::Operator.__init__)


def test_mprologtermreference::operator_constructor_args():
    sig = inspect.signature(mprologTermReference::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_mprologtermreference::operator_has_symbol():
    assert hasattr(mprologTermReference::Operator, "symbol")
    descriptor = None
    for klass in mprologTermReference::Operator.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::parenthesis_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Parenthesis)


def test_mprologtermreference::parenthesis_constructor_exists():
    assert callable(mprologTermReference::Parenthesis.__init__)


def test_mprologtermreference::parenthesis_constructor_args():
    sig = inspect.signature(mprologTermReference::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::list_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::List)


def test_mprologtermreference::list_constructor_exists():
    assert callable(mprologTermReference::List.__init__)


def test_mprologtermreference::list_constructor_args():
    sig = inspect.signature(mprologTermReference::List.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::quotedatom_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::QuotedAtom)


def test_mprologtermreference::quotedatom_constructor_exists():
    assert callable(mprologTermReference::QuotedAtom.__init__)


def test_mprologtermreference::quotedatom_constructor_args():
    sig = inspect.signature(mprologTermReference::QuotedAtom.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mprologtermreference::quotedatom_has_text():
    assert hasattr(mprologTermReference::QuotedAtom, "text")
    descriptor = None
    for klass in mprologTermReference::QuotedAtom.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mprologtermreference::termreference_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::TermReference)


def test_mprologtermreference::termreference_constructor_exists():
    assert callable(mprologTermReference::TermReference.__init__)


def test_mprologtermreference::termreference_constructor_args():
    sig = inspect.signature(mprologTermReference::TermReference.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::infixexpression_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::InfixExpression)


def test_mprologtermreference::infixexpression_constructor_exists():
    assert callable(mprologTermReference::InfixExpression.__init__)


def test_mprologtermreference::infixexpression_constructor_args():
    sig = inspect.signature(mprologTermReference::InfixExpression.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::variable_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Variable)


def test_mprologtermreference::variable_constructor_exists():
    assert callable(mprologTermReference::Variable.__init__)


def test_mprologtermreference::variable_constructor_args():
    sig = inspect.signature(mprologTermReference::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mprologtermreference::variable_has_name():
    assert hasattr(mprologTermReference::Variable, "name")
    descriptor = None
    for klass in mprologTermReference::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mprologtermreference::term_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Term)


def test_mprologtermreference::term_constructor_exists():
    assert callable(mprologTermReference::Term.__init__)


def test_mprologtermreference::term_constructor_args():
    sig = inspect.signature(mprologTermReference::Term.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::functor_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Functor)


def test_mprologtermreference::functor_constructor_exists():
    assert callable(mprologTermReference::Functor.__init__)


def test_mprologtermreference::functor_constructor_args():
    sig = inspect.signature(mprologTermReference::Functor.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mprologtermreference::functor_has_text():
    assert hasattr(mprologTermReference::Functor, "text")
    descriptor = None
    for klass in mprologTermReference::Functor.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mprologtermreference::body_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Body)


def test_mprologtermreference::body_constructor_exists():
    assert callable(mprologTermReference::Body.__init__)


def test_mprologtermreference::body_constructor_args():
    sig = inspect.signature(mprologTermReference::Body.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::head_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Head)


def test_mprologtermreference::head_constructor_exists():
    assert callable(mprologTermReference::Head.__init__)


def test_mprologtermreference::head_constructor_args():
    sig = inspect.signature(mprologTermReference::Head.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::clause_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Clause)


def test_mprologtermreference::clause_constructor_exists():
    assert callable(mprologTermReference::Clause.__init__)


def test_mprologtermreference::clause_constructor_args():
    sig = inspect.signature(mprologTermReference::Clause.__init__)
    params = list(sig.parameters.keys())



def test_mprologtermreference::model_is_not_abstract():
    assert not inspect.isabstract(mprologTermReference::Model)


def test_mprologtermreference::model_constructor_exists():
    assert callable(mprologTermReference::Model.__init__)


def test_mprologtermreference::model_constructor_args():
    sig = inspect.signature(mprologTermReference::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mprologtermreference::model_has_name():
    assert hasattr(mprologTermReference::Model, "name")
    descriptor = None
    for klass in mprologTermReference::Model.__mro__:
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
TermReference_strategy = st.builds(
    TermReference,
)
mprologTermReference::VariableReference_strategy = st.builds(
    mprologTermReference::VariableReference,
)
mprologTermReference::FunctorReference_strategy = st.builds(
    mprologTermReference::FunctorReference,
)
mprologTermReference::Operator_strategy = st.builds(
    mprologTermReference::Operator,
    symbol=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
mprologTermReference::Parenthesis_strategy = st.builds(
    mprologTermReference::Parenthesis,
)
mprologTermReference::List_strategy = st.builds(
    mprologTermReference::List,
)
mprologTermReference::QuotedAtom_strategy = st.builds(
    mprologTermReference::QuotedAtom,
    text=
        safe_text
)
mprologTermReference::TermReference_strategy = st.builds(
    mprologTermReference::TermReference,
)
mprologTermReference::InfixExpression_strategy = st.builds(
    mprologTermReference::InfixExpression,
)
mprologTermReference::Variable_strategy = st.builds(
    mprologTermReference::Variable,
    name=
        safe_text
)
mprologTermReference::Term_strategy = st.builds(
    mprologTermReference::Term,
)
mprologTermReference::Functor_strategy = st.builds(
    mprologTermReference::Functor,
    text=
        safe_text
)
mprologTermReference::Body_strategy = st.builds(
    mprologTermReference::Body,
)
mprologTermReference::Head_strategy = st.builds(
    mprologTermReference::Head,
)
mprologTermReference::Clause_strategy = st.builds(
    mprologTermReference::Clause,
)
mprologTermReference::Model_strategy = st.builds(
    mprologTermReference::Model,
    name=
        safe_text
)

@given(instance=TermReference_strategy)
@settings(max_examples=50)
def test_termreference_instantiation(instance):
    assert isinstance(instance, TermReference)

@given(instance=mprologTermReference::VariableReference_strategy)
@settings(max_examples=50)
def test_mprologtermreference::variablereference_instantiation(instance):
    assert isinstance(instance, mprologTermReference::VariableReference)

@given(instance=mprologTermReference::FunctorReference_strategy)
@settings(max_examples=50)
def test_mprologtermreference::functorreference_instantiation(instance):
    assert isinstance(instance, mprologTermReference::FunctorReference)

@given(instance=mprologTermReference::Operator_strategy)
@settings(max_examples=50)
def test_mprologtermreference::operator_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Operator)

@given(instance=mprologTermReference::Operator_strategy)
def test_mprologtermreference::operator_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=mprologTermReference::Operator_strategy)
def test_mprologtermreference::operator_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=mprologTermReference::Parenthesis_strategy)
@settings(max_examples=50)
def test_mprologtermreference::parenthesis_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Parenthesis)

@given(instance=mprologTermReference::List_strategy)
@settings(max_examples=50)
def test_mprologtermreference::list_instantiation(instance):
    assert isinstance(instance, mprologTermReference::List)

@given(instance=mprologTermReference::QuotedAtom_strategy)
@settings(max_examples=50)
def test_mprologtermreference::quotedatom_instantiation(instance):
    assert isinstance(instance, mprologTermReference::QuotedAtom)

@given(instance=mprologTermReference::QuotedAtom_strategy)
def test_mprologtermreference::quotedatom_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mprologTermReference::QuotedAtom_strategy)
def test_mprologtermreference::quotedatom_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mprologTermReference::TermReference_strategy)
@settings(max_examples=50)
def test_mprologtermreference::termreference_instantiation(instance):
    assert isinstance(instance, mprologTermReference::TermReference)

@given(instance=mprologTermReference::InfixExpression_strategy)
@settings(max_examples=50)
def test_mprologtermreference::infixexpression_instantiation(instance):
    assert isinstance(instance, mprologTermReference::InfixExpression)

@given(instance=mprologTermReference::Variable_strategy)
@settings(max_examples=50)
def test_mprologtermreference::variable_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Variable)

@given(instance=mprologTermReference::Variable_strategy)
def test_mprologtermreference::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mprologTermReference::Variable_strategy)
def test_mprologtermreference::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mprologTermReference::Term_strategy)
@settings(max_examples=50)
def test_mprologtermreference::term_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Term)

@given(instance=mprologTermReference::Functor_strategy)
@settings(max_examples=50)
def test_mprologtermreference::functor_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Functor)

@given(instance=mprologTermReference::Functor_strategy)
def test_mprologtermreference::functor_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mprologTermReference::Functor_strategy)
def test_mprologtermreference::functor_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mprologTermReference::Body_strategy)
@settings(max_examples=50)
def test_mprologtermreference::body_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Body)

@given(instance=mprologTermReference::Head_strategy)
@settings(max_examples=50)
def test_mprologtermreference::head_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Head)

@given(instance=mprologTermReference::Clause_strategy)
@settings(max_examples=50)
def test_mprologtermreference::clause_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Clause)

@given(instance=mprologTermReference::Model_strategy)
@settings(max_examples=50)
def test_mprologtermreference::model_instantiation(instance):
    assert isinstance(instance, mprologTermReference::Model)

@given(instance=mprologTermReference::Model_strategy)
def test_mprologtermreference::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mprologTermReference::Model_strategy)
def test_mprologtermreference::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
