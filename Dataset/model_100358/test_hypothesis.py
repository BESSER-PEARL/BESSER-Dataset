import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Literal,
    fmpl_Field,
    fmpl_StringLit,
    fmpl_IntegerLit,
    Expression,
    fmpl_Literal,
    fmpl_Cond,
    fmpl_Write,
    fmpl_Init,
    fmpl_ArithmeticExpression,
    fmpl_Relational,
    fmpl_VarDeclaration,
    fmpl_VarReference,
    fmpl_Read,
    fmpl_Exec,
    fmpl_Transition,
    fmpl_State,
    fmpl_Expression,
    fmpl_Automata,
    fmpl_Policy,
    ArithmeticOperator,
    RelationalOperator,
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



def test_fmpl_field_is_not_abstract():
    assert not inspect.isabstract(fmpl_Field)


def test_fmpl_field_constructor_exists():
    assert callable(fmpl_Field.__init__)


def test_fmpl_field_constructor_args():
    sig = inspect.signature(fmpl_Field.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_stringlit_is_not_abstract():
    assert not inspect.isabstract(fmpl_StringLit)


def test_fmpl_stringlit_constructor_exists():
    assert callable(fmpl_StringLit.__init__)


def test_fmpl_stringlit_constructor_args():
    sig = inspect.signature(fmpl_StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fmpl_stringlit_has_value():
    assert hasattr(fmpl_StringLit, "value")
    descriptor = None
    for klass in fmpl_StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_integerlit_is_not_abstract():
    assert not inspect.isabstract(fmpl_IntegerLit)


def test_fmpl_integerlit_constructor_exists():
    assert callable(fmpl_IntegerLit.__init__)


def test_fmpl_integerlit_constructor_args():
    sig = inspect.signature(fmpl_IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fmpl_integerlit_has_value():
    assert hasattr(fmpl_IntegerLit, "value")
    descriptor = None
    for klass in fmpl_IntegerLit.__mro__:
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



def test_fmpl_literal_is_not_abstract():
    assert not inspect.isabstract(fmpl_Literal)


def test_fmpl_literal_constructor_exists():
    assert callable(fmpl_Literal.__init__)


def test_fmpl_literal_constructor_args():
    sig = inspect.signature(fmpl_Literal.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_cond_is_not_abstract():
    assert not inspect.isabstract(fmpl_Cond)


def test_fmpl_cond_constructor_exists():
    assert callable(fmpl_Cond.__init__)


def test_fmpl_cond_constructor_args():
    sig = inspect.signature(fmpl_Cond.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_write_is_not_abstract():
    assert not inspect.isabstract(fmpl_Write)


def test_fmpl_write_constructor_exists():
    assert callable(fmpl_Write.__init__)


def test_fmpl_write_constructor_args():
    sig = inspect.signature(fmpl_Write.__init__)
    params = list(sig.parameters.keys())
    assert "initBit" in params, "Missing parameter 'initBit'"
    assert "length" in params, "Missing parameter 'length'"

def test_fmpl_write_has_initBit():
    assert hasattr(fmpl_Write, "initBit")
    descriptor = None
    for klass in fmpl_Write.__mro__:
        if "initBit" in klass.__dict__:
            descriptor = klass.__dict__["initBit"]
            break
    assert isinstance(descriptor, property)

def test_fmpl_write_has_length():
    assert hasattr(fmpl_Write, "length")
    descriptor = None
    for klass in fmpl_Write.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_init_is_not_abstract():
    assert not inspect.isabstract(fmpl_Init)


def test_fmpl_init_constructor_exists():
    assert callable(fmpl_Init.__init__)


def test_fmpl_init_constructor_args():
    sig = inspect.signature(fmpl_Init.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(fmpl_ArithmeticExpression)


def test_fmpl_arithmeticexpression_constructor_exists():
    assert callable(fmpl_ArithmeticExpression.__init__)


def test_fmpl_arithmeticexpression_constructor_args():
    sig = inspect.signature(fmpl_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fmpl_arithmeticexpression_has_operator():
    assert hasattr(fmpl_ArithmeticExpression, "operator")
    descriptor = None
    for klass in fmpl_ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_relational_is_not_abstract():
    assert not inspect.isabstract(fmpl_Relational)


def test_fmpl_relational_constructor_exists():
    assert callable(fmpl_Relational.__init__)


def test_fmpl_relational_constructor_args():
    sig = inspect.signature(fmpl_Relational.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fmpl_relational_has_operator():
    assert hasattr(fmpl_Relational, "operator")
    descriptor = None
    for klass in fmpl_Relational.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(fmpl_VarDeclaration)


def test_fmpl_vardeclaration_constructor_exists():
    assert callable(fmpl_VarDeclaration.__init__)


def test_fmpl_vardeclaration_constructor_args():
    sig = inspect.signature(fmpl_VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl_vardeclaration_has_name():
    assert hasattr(fmpl_VarDeclaration, "name")
    descriptor = None
    for klass in fmpl_VarDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_varreference_is_not_abstract():
    assert not inspect.isabstract(fmpl_VarReference)


def test_fmpl_varreference_constructor_exists():
    assert callable(fmpl_VarReference.__init__)


def test_fmpl_varreference_constructor_args():
    sig = inspect.signature(fmpl_VarReference.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_read_is_not_abstract():
    assert not inspect.isabstract(fmpl_Read)


def test_fmpl_read_constructor_exists():
    assert callable(fmpl_Read.__init__)


def test_fmpl_read_constructor_args():
    sig = inspect.signature(fmpl_Read.__init__)
    params = list(sig.parameters.keys())
    assert "initBit" in params, "Missing parameter 'initBit'"
    assert "length" in params, "Missing parameter 'length'"

def test_fmpl_read_has_initBit():
    assert hasattr(fmpl_Read, "initBit")
    descriptor = None
    for klass in fmpl_Read.__mro__:
        if "initBit" in klass.__dict__:
            descriptor = klass.__dict__["initBit"]
            break
    assert isinstance(descriptor, property)

def test_fmpl_read_has_length():
    assert hasattr(fmpl_Read, "length")
    descriptor = None
    for klass in fmpl_Read.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_exec_is_not_abstract():
    assert not inspect.isabstract(fmpl_Exec)


def test_fmpl_exec_constructor_exists():
    assert callable(fmpl_Exec.__init__)


def test_fmpl_exec_constructor_args():
    sig = inspect.signature(fmpl_Exec.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_transition_is_not_abstract():
    assert not inspect.isabstract(fmpl_Transition)


def test_fmpl_transition_constructor_exists():
    assert callable(fmpl_Transition.__init__)


def test_fmpl_transition_constructor_args():
    sig = inspect.signature(fmpl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl_transition_has_name():
    assert hasattr(fmpl_Transition, "name")
    descriptor = None
    for klass in fmpl_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_state_is_not_abstract():
    assert not inspect.isabstract(fmpl_State)


def test_fmpl_state_constructor_exists():
    assert callable(fmpl_State.__init__)


def test_fmpl_state_constructor_args():
    sig = inspect.signature(fmpl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl_state_has_name():
    assert hasattr(fmpl_State, "name")
    descriptor = None
    for klass in fmpl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_expression_is_not_abstract():
    assert not inspect.isabstract(fmpl_Expression)


def test_fmpl_expression_constructor_exists():
    assert callable(fmpl_Expression.__init__)


def test_fmpl_expression_constructor_args():
    sig = inspect.signature(fmpl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_fmpl_automata_is_not_abstract():
    assert not inspect.isabstract(fmpl_Automata)


def test_fmpl_automata_constructor_exists():
    assert callable(fmpl_Automata.__init__)


def test_fmpl_automata_constructor_args():
    sig = inspect.signature(fmpl_Automata.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl_automata_has_name():
    assert hasattr(fmpl_Automata, "name")
    descriptor = None
    for klass in fmpl_Automata.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fmpl_policy_is_not_abstract():
    assert not inspect.isabstract(fmpl_Policy)


def test_fmpl_policy_constructor_exists():
    assert callable(fmpl_Policy.__init__)


def test_fmpl_policy_constructor_args():
    sig = inspect.signature(fmpl_Policy.__init__)
    params = list(sig.parameters.keys())
    assert "parserURI" in params, "Missing parameter 'parserURI'"
    assert "name" in params, "Missing parameter 'name'"

def test_fmpl_policy_has_parserURI():
    assert hasattr(fmpl_Policy, "parserURI")
    descriptor = None
    for klass in fmpl_Policy.__mro__:
        if "parserURI" in klass.__dict__:
            descriptor = klass.__dict__["parserURI"]
            break
    assert isinstance(descriptor, property)

def test_fmpl_policy_has_name():
    assert hasattr(fmpl_Policy, "name")
    descriptor = None
    for klass in fmpl_Policy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "plus",
        "minus",
        "mult",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "and_",
        "greaterEqual",
        "lessEqual",
        "equal",
        "greater",
        "less",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
fmpl_Field_strategy = st.builds(
    fmpl_Field,
)
fmpl_StringLit_strategy = st.builds(
    fmpl_StringLit,
    value=
        safe_text
)
fmpl_IntegerLit_strategy = st.builds(
    fmpl_IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
fmpl_Literal_strategy = st.builds(
    fmpl_Literal,
)
fmpl_Cond_strategy = st.builds(
    fmpl_Cond,
)
fmpl_Write_strategy = st.builds(
    fmpl_Write,
    initBit=
        st.integers(),
    length=
        st.integers()
)
fmpl_Init_strategy = st.builds(
    fmpl_Init,
)
fmpl_ArithmeticExpression_strategy = st.builds(
    fmpl_ArithmeticExpression,
    operator=
        safe_text
)
fmpl_Relational_strategy = st.builds(
    fmpl_Relational,
    operator=
        safe_text
)
fmpl_VarDeclaration_strategy = st.builds(
    fmpl_VarDeclaration,
    name=
        safe_text
)
fmpl_VarReference_strategy = st.builds(
    fmpl_VarReference,
)
fmpl_Read_strategy = st.builds(
    fmpl_Read,
    initBit=
        st.integers(),
    length=
        st.integers()
)
fmpl_Exec_strategy = st.builds(
    fmpl_Exec,
)
fmpl_Transition_strategy = st.builds(
    fmpl_Transition,
    name=
        safe_text
)
fmpl_State_strategy = st.builds(
    fmpl_State,
    name=
        safe_text
)
fmpl_Expression_strategy = st.builds(
    fmpl_Expression,
)
fmpl_Automata_strategy = st.builds(
    fmpl_Automata,
    name=
        safe_text
)
fmpl_Policy_strategy = st.builds(
    fmpl_Policy,
    parserURI=
        safe_text,
    name=
        safe_text
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fmpl_Field_strategy)
@settings(max_examples=50)
def test_fmpl_field_instantiation(instance):
    assert isinstance(instance, fmpl_Field)

@given(instance=fmpl_StringLit_strategy)
@settings(max_examples=50)
def test_fmpl_stringlit_instantiation(instance):
    assert isinstance(instance, fmpl_StringLit)



@given(instance=fmpl_StringLit_strategy)
def test_fmpl_stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fmpl_IntegerLit_strategy)
@settings(max_examples=50)
def test_fmpl_integerlit_instantiation(instance):
    assert isinstance(instance, fmpl_IntegerLit)



@given(instance=fmpl_IntegerLit_strategy)
def test_fmpl_integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=fmpl_Literal_strategy)
@settings(max_examples=50)
def test_fmpl_literal_instantiation(instance):
    assert isinstance(instance, fmpl_Literal)

@given(instance=fmpl_Cond_strategy)
@settings(max_examples=50)
def test_fmpl_cond_instantiation(instance):
    assert isinstance(instance, fmpl_Cond)

@given(instance=fmpl_Write_strategy)
@settings(max_examples=50)
def test_fmpl_write_instantiation(instance):
    assert isinstance(instance, fmpl_Write)



@given(instance=fmpl_Write_strategy)
def test_fmpl_write_initBit_setter(instance):
    original = instance.initBit
    instance.initBit = original
    assert instance.initBit == original



@given(instance=fmpl_Write_strategy)
def test_fmpl_write_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=fmpl_Init_strategy)
@settings(max_examples=50)
def test_fmpl_init_instantiation(instance):
    assert isinstance(instance, fmpl_Init)

@given(instance=fmpl_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_fmpl_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, fmpl_ArithmeticExpression)



@given(instance=fmpl_ArithmeticExpression_strategy)
def test_fmpl_arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fmpl_Relational_strategy)
@settings(max_examples=50)
def test_fmpl_relational_instantiation(instance):
    assert isinstance(instance, fmpl_Relational)



@given(instance=fmpl_Relational_strategy)
def test_fmpl_relational_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fmpl_VarDeclaration_strategy)
@settings(max_examples=50)
def test_fmpl_vardeclaration_instantiation(instance):
    assert isinstance(instance, fmpl_VarDeclaration)



@given(instance=fmpl_VarDeclaration_strategy)
def test_fmpl_vardeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl_VarReference_strategy)
@settings(max_examples=50)
def test_fmpl_varreference_instantiation(instance):
    assert isinstance(instance, fmpl_VarReference)

@given(instance=fmpl_Read_strategy)
@settings(max_examples=50)
def test_fmpl_read_instantiation(instance):
    assert isinstance(instance, fmpl_Read)



@given(instance=fmpl_Read_strategy)
def test_fmpl_read_initBit_setter(instance):
    original = instance.initBit
    instance.initBit = original
    assert instance.initBit == original



@given(instance=fmpl_Read_strategy)
def test_fmpl_read_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=fmpl_Exec_strategy)
@settings(max_examples=50)
def test_fmpl_exec_instantiation(instance):
    assert isinstance(instance, fmpl_Exec)

@given(instance=fmpl_Transition_strategy)
@settings(max_examples=50)
def test_fmpl_transition_instantiation(instance):
    assert isinstance(instance, fmpl_Transition)



@given(instance=fmpl_Transition_strategy)
def test_fmpl_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl_State_strategy)
@settings(max_examples=50)
def test_fmpl_state_instantiation(instance):
    assert isinstance(instance, fmpl_State)



@given(instance=fmpl_State_strategy)
def test_fmpl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl_Expression_strategy)
@settings(max_examples=50)
def test_fmpl_expression_instantiation(instance):
    assert isinstance(instance, fmpl_Expression)

@given(instance=fmpl_Automata_strategy)
@settings(max_examples=50)
def test_fmpl_automata_instantiation(instance):
    assert isinstance(instance, fmpl_Automata)



@given(instance=fmpl_Automata_strategy)
def test_fmpl_automata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmpl_Policy_strategy)
@settings(max_examples=50)
def test_fmpl_policy_instantiation(instance):
    assert isinstance(instance, fmpl_Policy)



@given(instance=fmpl_Policy_strategy)
def test_fmpl_policy_parserURI_setter(instance):
    original = instance.parserURI
    instance.parserURI = original
    assert instance.parserURI == original



@given(instance=fmpl_Policy_strategy)
def test_fmpl_policy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
