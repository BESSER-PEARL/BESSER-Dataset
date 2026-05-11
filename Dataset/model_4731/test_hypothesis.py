import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Part,
    prolog::Assignment,
    prolog::Tail,
    prolog::Conjunction,
    prolog::Clause,
    prolog::PrologProgram,
    Tail,
    Term,
    prolog::Variable,
    prolog::VariableReference,
    prolog::Predicate,
    prolog::Multiplicative,
    prolog::String,
    prolog::AnonymousVariable,
    prolog::List,
    prolog::Numeral,
    prolog::Term,
    prolog::BracketExpression,
    prolog::Negation,
    prolog::Power,
    prolog::Additive,
    prolog::Part,
    MULTIPLICATIVE_OPERATOR,
    ADDITIVE_OPERATOR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_part_is_not_abstract():
    assert not inspect.isabstract(Part)


def test_part_constructor_exists():
    assert callable(Part.__init__)


def test_part_constructor_args():
    sig = inspect.signature(Part.__init__)
    params = list(sig.parameters.keys())



def test_prolog::assignment_is_not_abstract():
    assert not inspect.isabstract(prolog::Assignment)


def test_prolog::assignment_constructor_exists():
    assert callable(prolog::Assignment.__init__)


def test_prolog::assignment_constructor_args():
    sig = inspect.signature(prolog::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_prolog::tail_is_not_abstract():
    assert not inspect.isabstract(prolog::Tail)


def test_prolog::tail_constructor_exists():
    assert callable(prolog::Tail.__init__)


def test_prolog::tail_constructor_args():
    sig = inspect.signature(prolog::Tail.__init__)
    params = list(sig.parameters.keys())



def test_prolog::conjunction_is_not_abstract():
    assert not inspect.isabstract(prolog::Conjunction)


def test_prolog::conjunction_constructor_exists():
    assert callable(prolog::Conjunction.__init__)


def test_prolog::conjunction_constructor_args():
    sig = inspect.signature(prolog::Conjunction.__init__)
    params = list(sig.parameters.keys())



def test_prolog::clause_is_not_abstract():
    assert not inspect.isabstract(prolog::Clause)


def test_prolog::clause_constructor_exists():
    assert callable(prolog::Clause.__init__)


def test_prolog::clause_constructor_args():
    sig = inspect.signature(prolog::Clause.__init__)
    params = list(sig.parameters.keys())



def test_prolog::prologprogram_is_not_abstract():
    assert not inspect.isabstract(prolog::PrologProgram)


def test_prolog::prologprogram_constructor_exists():
    assert callable(prolog::PrologProgram.__init__)


def test_prolog::prologprogram_constructor_args():
    sig = inspect.signature(prolog::PrologProgram.__init__)
    params = list(sig.parameters.keys())



def test_tail_is_not_abstract():
    assert not inspect.isabstract(Tail)


def test_tail_constructor_exists():
    assert callable(Tail.__init__)


def test_tail_constructor_args():
    sig = inspect.signature(Tail.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_prolog::variable_is_not_abstract():
    assert not inspect.isabstract(prolog::Variable)


def test_prolog::variable_constructor_exists():
    assert callable(prolog::Variable.__init__)


def test_prolog::variable_constructor_args():
    sig = inspect.signature(prolog::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog::variable_has_name():
    assert hasattr(prolog::Variable, "name")
    descriptor = None
    for klass in prolog::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog::variablereference_is_not_abstract():
    assert not inspect.isabstract(prolog::VariableReference)


def test_prolog::variablereference_constructor_exists():
    assert callable(prolog::VariableReference.__init__)


def test_prolog::variablereference_constructor_args():
    sig = inspect.signature(prolog::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_prolog::predicate_is_not_abstract():
    assert not inspect.isabstract(prolog::Predicate)


def test_prolog::predicate_constructor_exists():
    assert callable(prolog::Predicate.__init__)


def test_prolog::predicate_constructor_args():
    sig = inspect.signature(prolog::Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog::predicate_has_name():
    assert hasattr(prolog::Predicate, "name")
    descriptor = None
    for klass in prolog::Predicate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog::multiplicative_is_not_abstract():
    assert not inspect.isabstract(prolog::Multiplicative)


def test_prolog::multiplicative_constructor_exists():
    assert callable(prolog::Multiplicative.__init__)


def test_prolog::multiplicative_constructor_args():
    sig = inspect.signature(prolog::Multiplicative.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_prolog::multiplicative_has_operator():
    assert hasattr(prolog::Multiplicative, "operator")
    descriptor = None
    for klass in prolog::Multiplicative.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_prolog::string_is_not_abstract():
    assert not inspect.isabstract(prolog::String)


def test_prolog::string_constructor_exists():
    assert callable(prolog::String.__init__)


def test_prolog::string_constructor_args():
    sig = inspect.signature(prolog::String.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_prolog::string_has_text():
    assert hasattr(prolog::String, "text")
    descriptor = None
    for klass in prolog::String.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_prolog::anonymousvariable_is_not_abstract():
    assert not inspect.isabstract(prolog::AnonymousVariable)


def test_prolog::anonymousvariable_constructor_exists():
    assert callable(prolog::AnonymousVariable.__init__)


def test_prolog::anonymousvariable_constructor_args():
    sig = inspect.signature(prolog::AnonymousVariable.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_prolog::anonymousvariable_has_text():
    assert hasattr(prolog::AnonymousVariable, "text")
    descriptor = None
    for klass in prolog::AnonymousVariable.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_prolog::list_is_not_abstract():
    assert not inspect.isabstract(prolog::List)


def test_prolog::list_constructor_exists():
    assert callable(prolog::List.__init__)


def test_prolog::list_constructor_args():
    sig = inspect.signature(prolog::List.__init__)
    params = list(sig.parameters.keys())



def test_prolog::numeral_is_not_abstract():
    assert not inspect.isabstract(prolog::Numeral)


def test_prolog::numeral_constructor_exists():
    assert callable(prolog::Numeral.__init__)


def test_prolog::numeral_constructor_args():
    sig = inspect.signature(prolog::Numeral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog::numeral_has_value():
    assert hasattr(prolog::Numeral, "value")
    descriptor = None
    for klass in prolog::Numeral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prolog::term_is_not_abstract():
    assert not inspect.isabstract(prolog::Term)


def test_prolog::term_constructor_exists():
    assert callable(prolog::Term.__init__)


def test_prolog::term_constructor_args():
    sig = inspect.signature(prolog::Term.__init__)
    params = list(sig.parameters.keys())



def test_prolog::bracketexpression_is_not_abstract():
    assert not inspect.isabstract(prolog::BracketExpression)


def test_prolog::bracketexpression_constructor_exists():
    assert callable(prolog::BracketExpression.__init__)


def test_prolog::bracketexpression_constructor_args():
    sig = inspect.signature(prolog::BracketExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog::negation_is_not_abstract():
    assert not inspect.isabstract(prolog::Negation)


def test_prolog::negation_constructor_exists():
    assert callable(prolog::Negation.__init__)


def test_prolog::negation_constructor_args():
    sig = inspect.signature(prolog::Negation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_prolog::negation_has_operator():
    assert hasattr(prolog::Negation, "operator")
    descriptor = None
    for klass in prolog::Negation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_prolog::power_is_not_abstract():
    assert not inspect.isabstract(prolog::Power)


def test_prolog::power_constructor_exists():
    assert callable(prolog::Power.__init__)


def test_prolog::power_constructor_args():
    sig = inspect.signature(prolog::Power.__init__)
    params = list(sig.parameters.keys())



def test_prolog::additive_is_not_abstract():
    assert not inspect.isabstract(prolog::Additive)


def test_prolog::additive_constructor_exists():
    assert callable(prolog::Additive.__init__)


def test_prolog::additive_constructor_args():
    sig = inspect.signature(prolog::Additive.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_prolog::additive_has_operator():
    assert hasattr(prolog::Additive, "operator")
    descriptor = None
    for klass in prolog::Additive.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_prolog::part_is_not_abstract():
    assert not inspect.isabstract(prolog::Part)


def test_prolog::part_constructor_exists():
    assert callable(prolog::Part.__init__)


def test_prolog::part_constructor_args():
    sig = inspect.signature(prolog::Part.__init__)
    params = list(sig.parameters.keys())

def test_multiplicative_operator_exists():
    # Check that the Enumeration exists
    assert MULTIPLICATIVE_OPERATOR is not None

def test_multiplicative_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MULTIPLICATIVE_OPERATOR]
    expected_literals = [
        "mult",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MULTIPLICATIVE_OPERATOR"

def test_additive_operator_exists():
    # Check that the Enumeration exists
    assert ADDITIVE_OPERATOR is not None

def test_additive_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ADDITIVE_OPERATOR]
    expected_literals = [
        "minus",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ADDITIVE_OPERATOR"


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
Part_strategy = st.builds(
    Part,
)
prolog::Assignment_strategy = st.builds(
    prolog::Assignment,
)
prolog::Tail_strategy = st.builds(
    prolog::Tail,
)
prolog::Conjunction_strategy = st.builds(
    prolog::Conjunction,
)
prolog::Clause_strategy = st.builds(
    prolog::Clause,
)
prolog::PrologProgram_strategy = st.builds(
    prolog::PrologProgram,
)
Tail_strategy = st.builds(
    Tail,
)
Term_strategy = st.builds(
    Term,
)
prolog::Variable_strategy = st.builds(
    prolog::Variable,
    name=
        safe_text
)
prolog::VariableReference_strategy = st.builds(
    prolog::VariableReference,
)
prolog::Predicate_strategy = st.builds(
    prolog::Predicate,
    name=
        safe_text
)
prolog::Multiplicative_strategy = st.builds(
    prolog::Multiplicative,
    operator=
        safe_text
)
prolog::String_strategy = st.builds(
    prolog::String,
    text=
        safe_text
)
prolog::AnonymousVariable_strategy = st.builds(
    prolog::AnonymousVariable,
    text=
        safe_text
)
prolog::List_strategy = st.builds(
    prolog::List,
)
prolog::Numeral_strategy = st.builds(
    prolog::Numeral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
prolog::Term_strategy = st.builds(
    prolog::Term,
)
prolog::BracketExpression_strategy = st.builds(
    prolog::BracketExpression,
)
prolog::Negation_strategy = st.builds(
    prolog::Negation,
    operator=
        safe_text
)
prolog::Power_strategy = st.builds(
    prolog::Power,
)
prolog::Additive_strategy = st.builds(
    prolog::Additive,
    operator=
        safe_text
)
prolog::Part_strategy = st.builds(
    prolog::Part,
)

@given(instance=Part_strategy)
@settings(max_examples=50)
def test_part_instantiation(instance):
    assert isinstance(instance, Part)

@given(instance=prolog::Assignment_strategy)
@settings(max_examples=50)
def test_prolog::assignment_instantiation(instance):
    assert isinstance(instance, prolog::Assignment)

@given(instance=prolog::Tail_strategy)
@settings(max_examples=50)
def test_prolog::tail_instantiation(instance):
    assert isinstance(instance, prolog::Tail)

@given(instance=prolog::Conjunction_strategy)
@settings(max_examples=50)
def test_prolog::conjunction_instantiation(instance):
    assert isinstance(instance, prolog::Conjunction)

@given(instance=prolog::Clause_strategy)
@settings(max_examples=50)
def test_prolog::clause_instantiation(instance):
    assert isinstance(instance, prolog::Clause)

@given(instance=prolog::PrologProgram_strategy)
@settings(max_examples=50)
def test_prolog::prologprogram_instantiation(instance):
    assert isinstance(instance, prolog::PrologProgram)

@given(instance=Tail_strategy)
@settings(max_examples=50)
def test_tail_instantiation(instance):
    assert isinstance(instance, Tail)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=prolog::Variable_strategy)
@settings(max_examples=50)
def test_prolog::variable_instantiation(instance):
    assert isinstance(instance, prolog::Variable)

@given(instance=prolog::Variable_strategy)
def test_prolog::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prolog::Variable_strategy)
def test_prolog::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog::VariableReference_strategy)
@settings(max_examples=50)
def test_prolog::variablereference_instantiation(instance):
    assert isinstance(instance, prolog::VariableReference)

@given(instance=prolog::Predicate_strategy)
@settings(max_examples=50)
def test_prolog::predicate_instantiation(instance):
    assert isinstance(instance, prolog::Predicate)

@given(instance=prolog::Predicate_strategy)
def test_prolog::predicate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prolog::Predicate_strategy)
def test_prolog::predicate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog::Multiplicative_strategy)
@settings(max_examples=50)
def test_prolog::multiplicative_instantiation(instance):
    assert isinstance(instance, prolog::Multiplicative)

@given(instance=prolog::Multiplicative_strategy)
def test_prolog::multiplicative_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=prolog::Multiplicative_strategy)
def test_prolog::multiplicative_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=prolog::String_strategy)
@settings(max_examples=50)
def test_prolog::string_instantiation(instance):
    assert isinstance(instance, prolog::String)

@given(instance=prolog::String_strategy)
def test_prolog::string_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=prolog::String_strategy)
def test_prolog::string_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=prolog::AnonymousVariable_strategy)
@settings(max_examples=50)
def test_prolog::anonymousvariable_instantiation(instance):
    assert isinstance(instance, prolog::AnonymousVariable)

@given(instance=prolog::AnonymousVariable_strategy)
def test_prolog::anonymousvariable_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=prolog::AnonymousVariable_strategy)
def test_prolog::anonymousvariable_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=prolog::List_strategy)
@settings(max_examples=50)
def test_prolog::list_instantiation(instance):
    assert isinstance(instance, prolog::List)

@given(instance=prolog::Numeral_strategy)
@settings(max_examples=50)
def test_prolog::numeral_instantiation(instance):
    assert isinstance(instance, prolog::Numeral)

@given(instance=prolog::Numeral_strategy)
def test_prolog::numeral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=prolog::Numeral_strategy)
def test_prolog::numeral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=prolog::Term_strategy)
@settings(max_examples=50)
def test_prolog::term_instantiation(instance):
    assert isinstance(instance, prolog::Term)

@given(instance=prolog::BracketExpression_strategy)
@settings(max_examples=50)
def test_prolog::bracketexpression_instantiation(instance):
    assert isinstance(instance, prolog::BracketExpression)

@given(instance=prolog::Negation_strategy)
@settings(max_examples=50)
def test_prolog::negation_instantiation(instance):
    assert isinstance(instance, prolog::Negation)

@given(instance=prolog::Negation_strategy)
def test_prolog::negation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=prolog::Negation_strategy)
def test_prolog::negation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=prolog::Power_strategy)
@settings(max_examples=50)
def test_prolog::power_instantiation(instance):
    assert isinstance(instance, prolog::Power)

@given(instance=prolog::Additive_strategy)
@settings(max_examples=50)
def test_prolog::additive_instantiation(instance):
    assert isinstance(instance, prolog::Additive)

@given(instance=prolog::Additive_strategy)
def test_prolog::additive_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=prolog::Additive_strategy)
def test_prolog::additive_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=prolog::Part_strategy)
@settings(max_examples=50)
def test_prolog::part_instantiation(instance):
    assert isinstance(instance, prolog::Part)
