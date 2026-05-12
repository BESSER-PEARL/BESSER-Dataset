import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    prolog_Part,
    Part,
    prolog_Assignment,
    prolog_Tail,
    prolog_Conjunction,
    prolog_Clause,
    prolog_PrologProgram,
    Tail,
    Term,
    prolog_List,
    prolog_Predicate,
    prolog_AnonymousVariable,
    prolog_Power,
    prolog_Additive,
    prolog_Multiplicative,
    prolog_Negation,
    prolog_Variable,
    prolog_VariableReference,
    prolog_BracketExpression,
    prolog_String,
    prolog_Numeral,
    prolog_Term,
    MULTIPLICATIVE_OPERATOR,
    ADDITIVE_OPERATOR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prolog_part_is_not_abstract():
    assert not inspect.isabstract(prolog_Part)


def test_prolog_part_constructor_exists():
    assert callable(prolog_Part.__init__)


def test_prolog_part_constructor_args():
    sig = inspect.signature(prolog_Part.__init__)
    params = list(sig.parameters.keys())



def test_part_is_not_abstract():
    assert not inspect.isabstract(Part)


def test_part_constructor_exists():
    assert callable(Part.__init__)


def test_part_constructor_args():
    sig = inspect.signature(Part.__init__)
    params = list(sig.parameters.keys())



def test_prolog_assignment_is_not_abstract():
    assert not inspect.isabstract(prolog_Assignment)


def test_prolog_assignment_constructor_exists():
    assert callable(prolog_Assignment.__init__)


def test_prolog_assignment_constructor_args():
    sig = inspect.signature(prolog_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_prolog_tail_is_not_abstract():
    assert not inspect.isabstract(prolog_Tail)


def test_prolog_tail_constructor_exists():
    assert callable(prolog_Tail.__init__)


def test_prolog_tail_constructor_args():
    sig = inspect.signature(prolog_Tail.__init__)
    params = list(sig.parameters.keys())



def test_prolog_conjunction_is_not_abstract():
    assert not inspect.isabstract(prolog_Conjunction)


def test_prolog_conjunction_constructor_exists():
    assert callable(prolog_Conjunction.__init__)


def test_prolog_conjunction_constructor_args():
    sig = inspect.signature(prolog_Conjunction.__init__)
    params = list(sig.parameters.keys())



def test_prolog_clause_is_not_abstract():
    assert not inspect.isabstract(prolog_Clause)


def test_prolog_clause_constructor_exists():
    assert callable(prolog_Clause.__init__)


def test_prolog_clause_constructor_args():
    sig = inspect.signature(prolog_Clause.__init__)
    params = list(sig.parameters.keys())



def test_prolog_prologprogram_is_not_abstract():
    assert not inspect.isabstract(prolog_PrologProgram)


def test_prolog_prologprogram_constructor_exists():
    assert callable(prolog_PrologProgram.__init__)


def test_prolog_prologprogram_constructor_args():
    sig = inspect.signature(prolog_PrologProgram.__init__)
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



def test_prolog_list_is_not_abstract():
    assert not inspect.isabstract(prolog_List)


def test_prolog_list_constructor_exists():
    assert callable(prolog_List.__init__)


def test_prolog_list_constructor_args():
    sig = inspect.signature(prolog_List.__init__)
    params = list(sig.parameters.keys())



def test_prolog_predicate_is_not_abstract():
    assert not inspect.isabstract(prolog_Predicate)


def test_prolog_predicate_constructor_exists():
    assert callable(prolog_Predicate.__init__)


def test_prolog_predicate_constructor_args():
    sig = inspect.signature(prolog_Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog_predicate_has_name():
    assert hasattr(prolog_Predicate, "name")
    descriptor = None
    for klass in prolog_Predicate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog_anonymousvariable_is_not_abstract():
    assert not inspect.isabstract(prolog_AnonymousVariable)


def test_prolog_anonymousvariable_constructor_exists():
    assert callable(prolog_AnonymousVariable.__init__)


def test_prolog_anonymousvariable_constructor_args():
    sig = inspect.signature(prolog_AnonymousVariable.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_prolog_anonymousvariable_has_text():
    assert hasattr(prolog_AnonymousVariable, "text")
    descriptor = None
    for klass in prolog_AnonymousVariable.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_prolog_power_is_not_abstract():
    assert not inspect.isabstract(prolog_Power)


def test_prolog_power_constructor_exists():
    assert callable(prolog_Power.__init__)


def test_prolog_power_constructor_args():
    sig = inspect.signature(prolog_Power.__init__)
    params = list(sig.parameters.keys())



def test_prolog_additive_is_not_abstract():
    assert not inspect.isabstract(prolog_Additive)


def test_prolog_additive_constructor_exists():
    assert callable(prolog_Additive.__init__)


def test_prolog_additive_constructor_args():
    sig = inspect.signature(prolog_Additive.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_prolog_additive_has_operator():
    assert hasattr(prolog_Additive, "operator")
    descriptor = None
    for klass in prolog_Additive.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_prolog_multiplicative_is_not_abstract():
    assert not inspect.isabstract(prolog_Multiplicative)


def test_prolog_multiplicative_constructor_exists():
    assert callable(prolog_Multiplicative.__init__)


def test_prolog_multiplicative_constructor_args():
    sig = inspect.signature(prolog_Multiplicative.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_prolog_multiplicative_has_operator():
    assert hasattr(prolog_Multiplicative, "operator")
    descriptor = None
    for klass in prolog_Multiplicative.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_prolog_negation_is_not_abstract():
    assert not inspect.isabstract(prolog_Negation)


def test_prolog_negation_constructor_exists():
    assert callable(prolog_Negation.__init__)


def test_prolog_negation_constructor_args():
    sig = inspect.signature(prolog_Negation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_prolog_negation_has_operator():
    assert hasattr(prolog_Negation, "operator")
    descriptor = None
    for klass in prolog_Negation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_prolog_variable_is_not_abstract():
    assert not inspect.isabstract(prolog_Variable)


def test_prolog_variable_constructor_exists():
    assert callable(prolog_Variable.__init__)


def test_prolog_variable_constructor_args():
    sig = inspect.signature(prolog_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog_variable_has_name():
    assert hasattr(prolog_Variable, "name")
    descriptor = None
    for klass in prolog_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog_variablereference_is_not_abstract():
    assert not inspect.isabstract(prolog_VariableReference)


def test_prolog_variablereference_constructor_exists():
    assert callable(prolog_VariableReference.__init__)


def test_prolog_variablereference_constructor_args():
    sig = inspect.signature(prolog_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_prolog_bracketexpression_is_not_abstract():
    assert not inspect.isabstract(prolog_BracketExpression)


def test_prolog_bracketexpression_constructor_exists():
    assert callable(prolog_BracketExpression.__init__)


def test_prolog_bracketexpression_constructor_args():
    sig = inspect.signature(prolog_BracketExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog_string_is_not_abstract():
    assert not inspect.isabstract(prolog_String)


def test_prolog_string_constructor_exists():
    assert callable(prolog_String.__init__)


def test_prolog_string_constructor_args():
    sig = inspect.signature(prolog_String.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_prolog_string_has_text():
    assert hasattr(prolog_String, "text")
    descriptor = None
    for klass in prolog_String.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_prolog_numeral_is_not_abstract():
    assert not inspect.isabstract(prolog_Numeral)


def test_prolog_numeral_constructor_exists():
    assert callable(prolog_Numeral.__init__)


def test_prolog_numeral_constructor_args():
    sig = inspect.signature(prolog_Numeral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog_numeral_has_value():
    assert hasattr(prolog_Numeral, "value")
    descriptor = None
    for klass in prolog_Numeral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prolog_term_is_not_abstract():
    assert not inspect.isabstract(prolog_Term)


def test_prolog_term_constructor_exists():
    assert callable(prolog_Term.__init__)


def test_prolog_term_constructor_args():
    sig = inspect.signature(prolog_Term.__init__)
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
        "plus",
        "minus",
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
prolog_Part_strategy = st.builds(
    prolog_Part,
)
Part_strategy = st.builds(
    Part,
)
prolog_Assignment_strategy = st.builds(
    prolog_Assignment,
)
prolog_Tail_strategy = st.builds(
    prolog_Tail,
)
prolog_Conjunction_strategy = st.builds(
    prolog_Conjunction,
)
prolog_Clause_strategy = st.builds(
    prolog_Clause,
)
prolog_PrologProgram_strategy = st.builds(
    prolog_PrologProgram,
)
Tail_strategy = st.builds(
    Tail,
)
Term_strategy = st.builds(
    Term,
)
prolog_List_strategy = st.builds(
    prolog_List,
)
prolog_Predicate_strategy = st.builds(
    prolog_Predicate,
    name=
        safe_text
)
prolog_AnonymousVariable_strategy = st.builds(
    prolog_AnonymousVariable,
    text=
        safe_text
)
prolog_Power_strategy = st.builds(
    prolog_Power,
)
prolog_Additive_strategy = st.builds(
    prolog_Additive,
    operator=
        safe_text
)
prolog_Multiplicative_strategy = st.builds(
    prolog_Multiplicative,
    operator=
        safe_text
)
prolog_Negation_strategy = st.builds(
    prolog_Negation,
    operator=
        safe_text
)
prolog_Variable_strategy = st.builds(
    prolog_Variable,
    name=
        safe_text
)
prolog_VariableReference_strategy = st.builds(
    prolog_VariableReference,
)
prolog_BracketExpression_strategy = st.builds(
    prolog_BracketExpression,
)
prolog_String_strategy = st.builds(
    prolog_String,
    text=
        safe_text
)
prolog_Numeral_strategy = st.builds(
    prolog_Numeral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
prolog_Term_strategy = st.builds(
    prolog_Term,
)

@given(instance=prolog_Part_strategy)
@settings(max_examples=50)
def test_prolog_part_instantiation(instance):
    assert isinstance(instance, prolog_Part)

@given(instance=Part_strategy)
@settings(max_examples=50)
def test_part_instantiation(instance):
    assert isinstance(instance, Part)

@given(instance=prolog_Assignment_strategy)
@settings(max_examples=50)
def test_prolog_assignment_instantiation(instance):
    assert isinstance(instance, prolog_Assignment)

@given(instance=prolog_Tail_strategy)
@settings(max_examples=50)
def test_prolog_tail_instantiation(instance):
    assert isinstance(instance, prolog_Tail)

@given(instance=prolog_Conjunction_strategy)
@settings(max_examples=50)
def test_prolog_conjunction_instantiation(instance):
    assert isinstance(instance, prolog_Conjunction)

@given(instance=prolog_Clause_strategy)
@settings(max_examples=50)
def test_prolog_clause_instantiation(instance):
    assert isinstance(instance, prolog_Clause)

@given(instance=prolog_PrologProgram_strategy)
@settings(max_examples=50)
def test_prolog_prologprogram_instantiation(instance):
    assert isinstance(instance, prolog_PrologProgram)

@given(instance=Tail_strategy)
@settings(max_examples=50)
def test_tail_instantiation(instance):
    assert isinstance(instance, Tail)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=prolog_List_strategy)
@settings(max_examples=50)
def test_prolog_list_instantiation(instance):
    assert isinstance(instance, prolog_List)

@given(instance=prolog_Predicate_strategy)
@settings(max_examples=50)
def test_prolog_predicate_instantiation(instance):
    assert isinstance(instance, prolog_Predicate)



@given(instance=prolog_Predicate_strategy)
def test_prolog_predicate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog_AnonymousVariable_strategy)
@settings(max_examples=50)
def test_prolog_anonymousvariable_instantiation(instance):
    assert isinstance(instance, prolog_AnonymousVariable)



@given(instance=prolog_AnonymousVariable_strategy)
def test_prolog_anonymousvariable_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=prolog_Power_strategy)
@settings(max_examples=50)
def test_prolog_power_instantiation(instance):
    assert isinstance(instance, prolog_Power)

@given(instance=prolog_Additive_strategy)
@settings(max_examples=50)
def test_prolog_additive_instantiation(instance):
    assert isinstance(instance, prolog_Additive)



@given(instance=prolog_Additive_strategy)
def test_prolog_additive_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=prolog_Multiplicative_strategy)
@settings(max_examples=50)
def test_prolog_multiplicative_instantiation(instance):
    assert isinstance(instance, prolog_Multiplicative)



@given(instance=prolog_Multiplicative_strategy)
def test_prolog_multiplicative_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=prolog_Negation_strategy)
@settings(max_examples=50)
def test_prolog_negation_instantiation(instance):
    assert isinstance(instance, prolog_Negation)



@given(instance=prolog_Negation_strategy)
def test_prolog_negation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=prolog_Variable_strategy)
@settings(max_examples=50)
def test_prolog_variable_instantiation(instance):
    assert isinstance(instance, prolog_Variable)



@given(instance=prolog_Variable_strategy)
def test_prolog_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog_VariableReference_strategy)
@settings(max_examples=50)
def test_prolog_variablereference_instantiation(instance):
    assert isinstance(instance, prolog_VariableReference)

@given(instance=prolog_BracketExpression_strategy)
@settings(max_examples=50)
def test_prolog_bracketexpression_instantiation(instance):
    assert isinstance(instance, prolog_BracketExpression)

@given(instance=prolog_String_strategy)
@settings(max_examples=50)
def test_prolog_string_instantiation(instance):
    assert isinstance(instance, prolog_String)



@given(instance=prolog_String_strategy)
def test_prolog_string_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=prolog_Numeral_strategy)
@settings(max_examples=50)
def test_prolog_numeral_instantiation(instance):
    assert isinstance(instance, prolog_Numeral)



@given(instance=prolog_Numeral_strategy)
def test_prolog_numeral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=prolog_Term_strategy)
@settings(max_examples=50)
def test_prolog_term_instantiation(instance):
    assert isinstance(instance, prolog_Term)
