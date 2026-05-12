import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Literal,
    fmpl::Field,
    fmpl::StringLit,
    fmpl::IntegerLit,
    Expression,
    fmpl::VarDeclaration,
    fmpl::Cond,
    fmpl::Literal,
    fmpl::VarReference,
    fmpl::Init,
    fmpl::Write,
    fmpl::Relational,
    fmpl::ArithmeticExpression,
    fmpl::Read,
    fmpl::Exec,
    fmpl::Transition,
    fmpl::State,
    fmpl::Expression,
    fmpl::Automata,
    fmpl::Policy,
    RelationalOperator,
    ArithmeticOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::field_is_not_abstract():
    assert not inspect.isabstract(fmpl::Field)


def test_fmpl::field_constructor_exists():
    assert callable(fmpl::Field.__init__)


def test_fmpl::field_constructor_args():
    sig = inspect.signature(fmpl::Field.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::stringlit_is_not_abstract():
    assert not inspect.isabstract(fmpl::StringLit)


def test_fmpl::stringlit_constructor_exists():
    assert callable(fmpl::StringLit.__init__)


def test_fmpl::stringlit_constructor_args():
    sig = inspect.signature(fmpl::StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fmpl::stringlit_has_value():
    assert hasattr(fmpl::StringLit, "value")
    descriptor = None
    for klass in fmpl::StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::integerlit_is_not_abstract():
    assert not inspect.isabstract(fmpl::IntegerLit)


def test_fmpl::integerlit_constructor_exists():
    assert callable(fmpl::IntegerLit.__init__)


def test_fmpl::integerlit_constructor_args():
    sig = inspect.signature(fmpl::IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fmpl::integerlit_has_value():
    assert hasattr(fmpl::IntegerLit, "value")
    descriptor = None
    for klass in fmpl::IntegerLit.__mro__:
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



def test_fmpl::vardeclaration_is_not_abstract():
    assert not inspect.isabstract(fmpl::VarDeclaration)


def test_fmpl::vardeclaration_constructor_exists():
    assert callable(fmpl::VarDeclaration.__init__)


def test_fmpl::vardeclaration_constructor_args():
    sig = inspect.signature(fmpl::VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl::vardeclaration_has_name():
    assert hasattr(fmpl::VarDeclaration, "name")
    descriptor = None
    for klass in fmpl::VarDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::cond_is_not_abstract():
    assert not inspect.isabstract(fmpl::Cond)


def test_fmpl::cond_constructor_exists():
    assert callable(fmpl::Cond.__init__)


def test_fmpl::cond_constructor_args():
    sig = inspect.signature(fmpl::Cond.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::literal_is_not_abstract():
    assert not inspect.isabstract(fmpl::Literal)


def test_fmpl::literal_constructor_exists():
    assert callable(fmpl::Literal.__init__)


def test_fmpl::literal_constructor_args():
    sig = inspect.signature(fmpl::Literal.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::varreference_is_not_abstract():
    assert not inspect.isabstract(fmpl::VarReference)


def test_fmpl::varreference_constructor_exists():
    assert callable(fmpl::VarReference.__init__)


def test_fmpl::varreference_constructor_args():
    sig = inspect.signature(fmpl::VarReference.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::init_is_not_abstract():
    assert not inspect.isabstract(fmpl::Init)


def test_fmpl::init_constructor_exists():
    assert callable(fmpl::Init.__init__)


def test_fmpl::init_constructor_args():
    sig = inspect.signature(fmpl::Init.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::write_is_not_abstract():
    assert not inspect.isabstract(fmpl::Write)


def test_fmpl::write_constructor_exists():
    assert callable(fmpl::Write.__init__)


def test_fmpl::write_constructor_args():
    sig = inspect.signature(fmpl::Write.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "initBit" in params, "Missing parameter 'initBit'"

def test_fmpl::write_has_length():
    assert hasattr(fmpl::Write, "length")
    descriptor = None
    for klass in fmpl::Write.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_fmpl::write_has_initBit():
    assert hasattr(fmpl::Write, "initBit")
    descriptor = None
    for klass in fmpl::Write.__mro__:
        if "initBit" in klass.__dict__:
            descriptor = klass.__dict__["initBit"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::relational_is_not_abstract():
    assert not inspect.isabstract(fmpl::Relational)


def test_fmpl::relational_constructor_exists():
    assert callable(fmpl::Relational.__init__)


def test_fmpl::relational_constructor_args():
    sig = inspect.signature(fmpl::Relational.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fmpl::relational_has_operator():
    assert hasattr(fmpl::Relational, "operator")
    descriptor = None
    for klass in fmpl::Relational.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(fmpl::ArithmeticExpression)


def test_fmpl::arithmeticexpression_constructor_exists():
    assert callable(fmpl::ArithmeticExpression.__init__)


def test_fmpl::arithmeticexpression_constructor_args():
    sig = inspect.signature(fmpl::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fmpl::arithmeticexpression_has_operator():
    assert hasattr(fmpl::ArithmeticExpression, "operator")
    descriptor = None
    for klass in fmpl::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::read_is_not_abstract():
    assert not inspect.isabstract(fmpl::Read)


def test_fmpl::read_constructor_exists():
    assert callable(fmpl::Read.__init__)


def test_fmpl::read_constructor_args():
    sig = inspect.signature(fmpl::Read.__init__)
    params = list(sig.parameters.keys())
    assert "initBit" in params, "Missing parameter 'initBit'"
    assert "length" in params, "Missing parameter 'length'"

def test_fmpl::read_has_initBit():
    assert hasattr(fmpl::Read, "initBit")
    descriptor = None
    for klass in fmpl::Read.__mro__:
        if "initBit" in klass.__dict__:
            descriptor = klass.__dict__["initBit"]
            break
    assert isinstance(descriptor, property)

def test_fmpl::read_has_length():
    assert hasattr(fmpl::Read, "length")
    descriptor = None
    for klass in fmpl::Read.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::exec_is_not_abstract():
    assert not inspect.isabstract(fmpl::Exec)


def test_fmpl::exec_constructor_exists():
    assert callable(fmpl::Exec.__init__)


def test_fmpl::exec_constructor_args():
    sig = inspect.signature(fmpl::Exec.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::transition_is_not_abstract():
    assert not inspect.isabstract(fmpl::Transition)


def test_fmpl::transition_constructor_exists():
    assert callable(fmpl::Transition.__init__)


def test_fmpl::transition_constructor_args():
    sig = inspect.signature(fmpl::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl::transition_has_name():
    assert hasattr(fmpl::Transition, "name")
    descriptor = None
    for klass in fmpl::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::state_is_not_abstract():
    assert not inspect.isabstract(fmpl::State)


def test_fmpl::state_constructor_exists():
    assert callable(fmpl::State.__init__)


def test_fmpl::state_constructor_args():
    sig = inspect.signature(fmpl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl::state_has_name():
    assert hasattr(fmpl::State, "name")
    descriptor = None
    for klass in fmpl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::expression_is_not_abstract():
    assert not inspect.isabstract(fmpl::Expression)


def test_fmpl::expression_constructor_exists():
    assert callable(fmpl::Expression.__init__)


def test_fmpl::expression_constructor_args():
    sig = inspect.signature(fmpl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_fmpl::automata_is_not_abstract():
    assert not inspect.isabstract(fmpl::Automata)


def test_fmpl::automata_constructor_exists():
    assert callable(fmpl::Automata.__init__)


def test_fmpl::automata_constructor_args():
    sig = inspect.signature(fmpl::Automata.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl::automata_has_name():
    assert hasattr(fmpl::Automata, "name")
    descriptor = None
    for klass in fmpl::Automata.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl::policy_is_not_abstract():
    assert not inspect.isabstract(fmpl::Policy)


def test_fmpl::policy_constructor_exists():
    assert callable(fmpl::Policy.__init__)


def test_fmpl::policy_constructor_args():
    sig = inspect.signature(fmpl::Policy.__init__)
    params = list(sig.parameters.keys())
    assert "parserURI" in params, "Missing parameter 'parserURI'"
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl::policy_has_parserURI():
    assert hasattr(fmpl::Policy, "parserURI")
    descriptor = None
    for klass in fmpl::Policy.__mro__:
        if "parserURI" in klass.__dict__:
            descriptor = klass.__dict__["parserURI"]
            break
    assert isinstance(descriptor, property)

def test_fmpl::policy_has_name():
    assert hasattr(fmpl::Policy, "name")
    descriptor = None
    for klass in fmpl::Policy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "greater",
        "less",
        "and_",
        "lessEqual",
        "greaterEqual",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "plus",
        "mult",
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
Literal_strategy = st.builds(
    Literal,
)
fmpl::Field_strategy = st.builds(
    fmpl::Field,
)
fmpl::StringLit_strategy = st.builds(
    fmpl::StringLit,
    value=
        safe_text
)
fmpl::IntegerLit_strategy = st.builds(
    fmpl::IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
fmpl::VarDeclaration_strategy = st.builds(
    fmpl::VarDeclaration,
    name=
        safe_text
)
fmpl::Cond_strategy = st.builds(
    fmpl::Cond,
)
fmpl::Literal_strategy = st.builds(
    fmpl::Literal,
)
fmpl::VarReference_strategy = st.builds(
    fmpl::VarReference,
)
fmpl::Init_strategy = st.builds(
    fmpl::Init,
)
fmpl::Write_strategy = st.builds(
    fmpl::Write,
    length=
        st.integers(),
    initBit=
        st.integers()
)
fmpl::Relational_strategy = st.builds(
    fmpl::Relational,
    operator=
        safe_text
)
fmpl::ArithmeticExpression_strategy = st.builds(
    fmpl::ArithmeticExpression,
    operator=
        safe_text
)
fmpl::Read_strategy = st.builds(
    fmpl::Read,
    initBit=
        st.integers(),
    length=
        st.integers()
)
fmpl::Exec_strategy = st.builds(
    fmpl::Exec,
)
fmpl::Transition_strategy = st.builds(
    fmpl::Transition,
    name=
        safe_text
)
fmpl::State_strategy = st.builds(
    fmpl::State,
    name=
        safe_text
)
fmpl::Expression_strategy = st.builds(
    fmpl::Expression,
)
fmpl::Automata_strategy = st.builds(
    fmpl::Automata,
    name=
        safe_text
)
fmpl::Policy_strategy = st.builds(
    fmpl::Policy,
    parserURI=
        safe_text,
    name=
        safe_text
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fmpl::Field_strategy)
@settings(max_examples=50)
def test_fmpl::field_instantiation(instance):
    assert isinstance(instance, fmpl::Field)

@given(instance=fmpl::StringLit_strategy)
@settings(max_examples=50)
def test_fmpl::stringlit_instantiation(instance):
    assert isinstance(instance, fmpl::StringLit)

@given(instance=fmpl::StringLit_strategy)
def test_fmpl::stringlit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fmpl::StringLit_strategy)
def test_fmpl::stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fmpl::IntegerLit_strategy)
@settings(max_examples=50)
def test_fmpl::integerlit_instantiation(instance):
    assert isinstance(instance, fmpl::IntegerLit)

@given(instance=fmpl::IntegerLit_strategy)
def test_fmpl::integerlit_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fmpl::IntegerLit_strategy)
def test_fmpl::integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=fmpl::VarDeclaration_strategy)
@settings(max_examples=50)
def test_fmpl::vardeclaration_instantiation(instance):
    assert isinstance(instance, fmpl::VarDeclaration)

@given(instance=fmpl::VarDeclaration_strategy)
def test_fmpl::vardeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fmpl::VarDeclaration_strategy)
def test_fmpl::vardeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl::Cond_strategy)
@settings(max_examples=50)
def test_fmpl::cond_instantiation(instance):
    assert isinstance(instance, fmpl::Cond)

@given(instance=fmpl::Literal_strategy)
@settings(max_examples=50)
def test_fmpl::literal_instantiation(instance):
    assert isinstance(instance, fmpl::Literal)

@given(instance=fmpl::VarReference_strategy)
@settings(max_examples=50)
def test_fmpl::varreference_instantiation(instance):
    assert isinstance(instance, fmpl::VarReference)

@given(instance=fmpl::Init_strategy)
@settings(max_examples=50)
def test_fmpl::init_instantiation(instance):
    assert isinstance(instance, fmpl::Init)

@given(instance=fmpl::Write_strategy)
@settings(max_examples=50)
def test_fmpl::write_instantiation(instance):
    assert isinstance(instance, fmpl::Write)

@given(instance=fmpl::Write_strategy)
def test_fmpl::write_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=fmpl::Write_strategy)
def test_fmpl::write_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=fmpl::Write_strategy)
def test_fmpl::write_initBit_type(instance):
    assert isinstance(instance.initBit, int)


@given(instance=fmpl::Write_strategy)
def test_fmpl::write_initBit_setter(instance):
    original = instance.initBit
    instance.initBit = original
    assert instance.initBit == original

@given(instance=fmpl::Relational_strategy)
@settings(max_examples=50)
def test_fmpl::relational_instantiation(instance):
    assert isinstance(instance, fmpl::Relational)

@given(instance=fmpl::Relational_strategy)
def test_fmpl::relational_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=fmpl::Relational_strategy)
def test_fmpl::relational_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fmpl::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_fmpl::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, fmpl::ArithmeticExpression)

@given(instance=fmpl::ArithmeticExpression_strategy)
def test_fmpl::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=fmpl::ArithmeticExpression_strategy)
def test_fmpl::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fmpl::Read_strategy)
@settings(max_examples=50)
def test_fmpl::read_instantiation(instance):
    assert isinstance(instance, fmpl::Read)

@given(instance=fmpl::Read_strategy)
def test_fmpl::read_initBit_type(instance):
    assert isinstance(instance.initBit, int)


@given(instance=fmpl::Read_strategy)
def test_fmpl::read_initBit_setter(instance):
    original = instance.initBit
    instance.initBit = original
    assert instance.initBit == original

@given(instance=fmpl::Read_strategy)
def test_fmpl::read_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=fmpl::Read_strategy)
def test_fmpl::read_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=fmpl::Exec_strategy)
@settings(max_examples=50)
def test_fmpl::exec_instantiation(instance):
    assert isinstance(instance, fmpl::Exec)

@given(instance=fmpl::Transition_strategy)
@settings(max_examples=50)
def test_fmpl::transition_instantiation(instance):
    assert isinstance(instance, fmpl::Transition)

@given(instance=fmpl::Transition_strategy)
def test_fmpl::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fmpl::Transition_strategy)
def test_fmpl::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl::State_strategy)
@settings(max_examples=50)
def test_fmpl::state_instantiation(instance):
    assert isinstance(instance, fmpl::State)

@given(instance=fmpl::State_strategy)
def test_fmpl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fmpl::State_strategy)
def test_fmpl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl::Expression_strategy)
@settings(max_examples=50)
def test_fmpl::expression_instantiation(instance):
    assert isinstance(instance, fmpl::Expression)

@given(instance=fmpl::Automata_strategy)
@settings(max_examples=50)
def test_fmpl::automata_instantiation(instance):
    assert isinstance(instance, fmpl::Automata)

@given(instance=fmpl::Automata_strategy)
def test_fmpl::automata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fmpl::Automata_strategy)
def test_fmpl::automata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl::Policy_strategy)
@settings(max_examples=50)
def test_fmpl::policy_instantiation(instance):
    assert isinstance(instance, fmpl::Policy)

@given(instance=fmpl::Policy_strategy)
def test_fmpl::policy_parserURI_type(instance):
    assert isinstance(instance.parserURI, str)


@given(instance=fmpl::Policy_strategy)
def test_fmpl::policy_parserURI_setter(instance):
    original = instance.parserURI
    instance.parserURI = original
    assert instance.parserURI == original

@given(instance=fmpl::Policy_strategy)
def test_fmpl::policy_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fmpl::Policy_strategy)
def test_fmpl::policy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
