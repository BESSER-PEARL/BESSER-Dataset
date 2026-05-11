import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ConsoleOutput,
    flowchartpck::Print,
    flowchartpck::Println,
    Statement,
    flowchartpck::ConsoleOutput,
    flowchartpck::VarDecl,
    flowchartpck::Assignation,
    flowchartpck::Loop,
    flowchartpck::Conditional,
    flowchartpck::Statement,
    flowchartpck::Wait,
    Literal,
    flowchartpck::StringLit,
    flowchartpck::BoolLit,
    flowchartpck::IntegerLit,
    Expression,
    flowchartpck::VarReference,
    flowchartpck::ArithmeticExpression,
    flowchartpck::Literal,
    flowchartpck::Expression,
    Constraint,
    flowchartpck::RelationalConstraint,
    flowchartpck::Constraint,
    flowchartpck::Program,
    Node,
    flowchartpck::Decision,
    flowchartpck::End,
    flowchartpck::Start,
    flowchartpck::Action,
    flowchartpck::RelationalExpression,
    NamedElement,
    flowchartpck::Node,
    flowchartpck::Flowchart,
    flowchartpck::NamedElement,
    flowchartpck::Arc,
    RelationalOperator,
    ArithmeticOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_consoleoutput_is_not_abstract():
    assert not inspect.isabstract(ConsoleOutput)


def test_consoleoutput_constructor_exists():
    assert callable(ConsoleOutput.__init__)


def test_consoleoutput_constructor_args():
    sig = inspect.signature(ConsoleOutput.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::print_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Print)


def test_flowchartpck::print_constructor_exists():
    assert callable(flowchartpck::Print.__init__)


def test_flowchartpck::print_constructor_args():
    sig = inspect.signature(flowchartpck::Print.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::println_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Println)


def test_flowchartpck::println_constructor_exists():
    assert callable(flowchartpck::Println.__init__)


def test_flowchartpck::println_constructor_args():
    sig = inspect.signature(flowchartpck::Println.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::consoleoutput_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::ConsoleOutput)


def test_flowchartpck::consoleoutput_constructor_exists():
    assert callable(flowchartpck::ConsoleOutput.__init__)


def test_flowchartpck::consoleoutput_constructor_args():
    sig = inspect.signature(flowchartpck::ConsoleOutput.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_flowchartpck::consoleoutput_has_input():
    assert hasattr(flowchartpck::ConsoleOutput, "input")
    descriptor = None
    for klass in flowchartpck::ConsoleOutput.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::vardecl_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::VarDecl)


def test_flowchartpck::vardecl_constructor_exists():
    assert callable(flowchartpck::VarDecl.__init__)


def test_flowchartpck::vardecl_constructor_args():
    sig = inspect.signature(flowchartpck::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_flowchartpck::vardecl_has_key():
    assert hasattr(flowchartpck::VarDecl, "key")
    descriptor = None
    for klass in flowchartpck::VarDecl.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::assignation_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Assignation)


def test_flowchartpck::assignation_constructor_exists():
    assert callable(flowchartpck::Assignation.__init__)


def test_flowchartpck::assignation_constructor_args():
    sig = inspect.signature(flowchartpck::Assignation.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::loop_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Loop)


def test_flowchartpck::loop_constructor_exists():
    assert callable(flowchartpck::Loop.__init__)


def test_flowchartpck::loop_constructor_args():
    sig = inspect.signature(flowchartpck::Loop.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::conditional_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Conditional)


def test_flowchartpck::conditional_constructor_exists():
    assert callable(flowchartpck::Conditional.__init__)


def test_flowchartpck::conditional_constructor_args():
    sig = inspect.signature(flowchartpck::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::statement_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Statement)


def test_flowchartpck::statement_constructor_exists():
    assert callable(flowchartpck::Statement.__init__)


def test_flowchartpck::statement_constructor_args():
    sig = inspect.signature(flowchartpck::Statement.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::wait_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Wait)


def test_flowchartpck::wait_constructor_exists():
    assert callable(flowchartpck::Wait.__init__)


def test_flowchartpck::wait_constructor_args():
    sig = inspect.signature(flowchartpck::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "miliseconds" in params, "Missing parameter 'miliseconds'"

def test_flowchartpck::wait_has_miliseconds():
    assert hasattr(flowchartpck::Wait, "miliseconds")
    descriptor = None
    for klass in flowchartpck::Wait.__mro__:
        if "miliseconds" in klass.__dict__:
            descriptor = klass.__dict__["miliseconds"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::stringlit_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::StringLit)


def test_flowchartpck::stringlit_constructor_exists():
    assert callable(flowchartpck::StringLit.__init__)


def test_flowchartpck::stringlit_constructor_args():
    sig = inspect.signature(flowchartpck::StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_flowchartpck::stringlit_has_value():
    assert hasattr(flowchartpck::StringLit, "value")
    descriptor = None
    for klass in flowchartpck::StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::boollit_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::BoolLit)


def test_flowchartpck::boollit_constructor_exists():
    assert callable(flowchartpck::BoolLit.__init__)


def test_flowchartpck::boollit_constructor_args():
    sig = inspect.signature(flowchartpck::BoolLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_flowchartpck::boollit_has_value():
    assert hasattr(flowchartpck::BoolLit, "value")
    descriptor = None
    for klass in flowchartpck::BoolLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::integerlit_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::IntegerLit)


def test_flowchartpck::integerlit_constructor_exists():
    assert callable(flowchartpck::IntegerLit.__init__)


def test_flowchartpck::integerlit_constructor_args():
    sig = inspect.signature(flowchartpck::IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_flowchartpck::integerlit_has_value():
    assert hasattr(flowchartpck::IntegerLit, "value")
    descriptor = None
    for klass in flowchartpck::IntegerLit.__mro__:
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



def test_flowchartpck::varreference_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::VarReference)


def test_flowchartpck::varreference_constructor_exists():
    assert callable(flowchartpck::VarReference.__init__)


def test_flowchartpck::varreference_constructor_args():
    sig = inspect.signature(flowchartpck::VarReference.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_flowchartpck::varreference_has_key():
    assert hasattr(flowchartpck::VarReference, "key")
    descriptor = None
    for klass in flowchartpck::VarReference.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::ArithmeticExpression)


def test_flowchartpck::arithmeticexpression_constructor_exists():
    assert callable(flowchartpck::ArithmeticExpression.__init__)


def test_flowchartpck::arithmeticexpression_constructor_args():
    sig = inspect.signature(flowchartpck::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flowchartpck::arithmeticexpression_has_operator():
    assert hasattr(flowchartpck::ArithmeticExpression, "operator")
    descriptor = None
    for klass in flowchartpck::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::literal_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Literal)


def test_flowchartpck::literal_constructor_exists():
    assert callable(flowchartpck::Literal.__init__)


def test_flowchartpck::literal_constructor_args():
    sig = inspect.signature(flowchartpck::Literal.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::expression_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Expression)


def test_flowchartpck::expression_constructor_exists():
    assert callable(flowchartpck::Expression.__init__)


def test_flowchartpck::expression_constructor_args():
    sig = inspect.signature(flowchartpck::Expression.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::relationalconstraint_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::RelationalConstraint)


def test_flowchartpck::relationalconstraint_constructor_exists():
    assert callable(flowchartpck::RelationalConstraint.__init__)


def test_flowchartpck::relationalconstraint_constructor_args():
    sig = inspect.signature(flowchartpck::RelationalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::constraint_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Constraint)


def test_flowchartpck::constraint_constructor_exists():
    assert callable(flowchartpck::Constraint.__init__)


def test_flowchartpck::constraint_constructor_args():
    sig = inspect.signature(flowchartpck::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::program_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Program)


def test_flowchartpck::program_constructor_exists():
    assert callable(flowchartpck::Program.__init__)


def test_flowchartpck::program_constructor_args():
    sig = inspect.signature(flowchartpck::Program.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::decision_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Decision)


def test_flowchartpck::decision_constructor_exists():
    assert callable(flowchartpck::Decision.__init__)


def test_flowchartpck::decision_constructor_args():
    sig = inspect.signature(flowchartpck::Decision.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::end_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::End)


def test_flowchartpck::end_constructor_exists():
    assert callable(flowchartpck::End.__init__)


def test_flowchartpck::end_constructor_args():
    sig = inspect.signature(flowchartpck::End.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::start_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Start)


def test_flowchartpck::start_constructor_exists():
    assert callable(flowchartpck::Start.__init__)


def test_flowchartpck::start_constructor_args():
    sig = inspect.signature(flowchartpck::Start.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::action_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Action)


def test_flowchartpck::action_constructor_exists():
    assert callable(flowchartpck::Action.__init__)


def test_flowchartpck::action_constructor_args():
    sig = inspect.signature(flowchartpck::Action.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::RelationalExpression)


def test_flowchartpck::relationalexpression_constructor_exists():
    assert callable(flowchartpck::RelationalExpression.__init__)


def test_flowchartpck::relationalexpression_constructor_args():
    sig = inspect.signature(flowchartpck::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_flowchartpck::relationalexpression_has_operator():
    assert hasattr(flowchartpck::RelationalExpression, "operator")
    descriptor = None
    for klass in flowchartpck::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::node_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Node)


def test_flowchartpck::node_constructor_exists():
    assert callable(flowchartpck::Node.__init__)


def test_flowchartpck::node_constructor_args():
    sig = inspect.signature(flowchartpck::Node.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::flowchart_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Flowchart)


def test_flowchartpck::flowchart_constructor_exists():
    assert callable(flowchartpck::Flowchart.__init__)


def test_flowchartpck::flowchart_constructor_args():
    sig = inspect.signature(flowchartpck::Flowchart.__init__)
    params = list(sig.parameters.keys())



def test_flowchartpck::namedelement_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::NamedElement)


def test_flowchartpck::namedelement_constructor_exists():
    assert callable(flowchartpck::NamedElement.__init__)


def test_flowchartpck::namedelement_constructor_args():
    sig = inspect.signature(flowchartpck::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_flowchartpck::namedelement_has_name():
    assert hasattr(flowchartpck::NamedElement, "name")
    descriptor = None
    for klass in flowchartpck::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_flowchartpck::arc_is_not_abstract():
    assert not inspect.isabstract(flowchartpck::Arc)


def test_flowchartpck::arc_constructor_exists():
    assert callable(flowchartpck::Arc.__init__)


def test_flowchartpck::arc_constructor_args():
    sig = inspect.signature(flowchartpck::Arc.__init__)
    params = list(sig.parameters.keys())

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "equals",
        "greaterThanOrEqualTo",
        "notEqual",
        "lessThanOrEqualTo",
        "lessThan",
        "greaterThan",
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
        "div",
        "minus",
        "mult",
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
ConsoleOutput_strategy = st.builds(
    ConsoleOutput,
)
flowchartpck::Print_strategy = st.builds(
    flowchartpck::Print,
)
flowchartpck::Println_strategy = st.builds(
    flowchartpck::Println,
)
Statement_strategy = st.builds(
    Statement,
)
flowchartpck::ConsoleOutput_strategy = st.builds(
    flowchartpck::ConsoleOutput,
    input=
        safe_text
)
flowchartpck::VarDecl_strategy = st.builds(
    flowchartpck::VarDecl,
    key=
        safe_text
)
flowchartpck::Assignation_strategy = st.builds(
    flowchartpck::Assignation,
)
flowchartpck::Loop_strategy = st.builds(
    flowchartpck::Loop,
)
flowchartpck::Conditional_strategy = st.builds(
    flowchartpck::Conditional,
)
flowchartpck::Statement_strategy = st.builds(
    flowchartpck::Statement,
)
flowchartpck::Wait_strategy = st.builds(
    flowchartpck::Wait,
    miliseconds=
        safe_text
)
Literal_strategy = st.builds(
    Literal,
)
flowchartpck::StringLit_strategy = st.builds(
    flowchartpck::StringLit,
    value=
        safe_text
)
flowchartpck::BoolLit_strategy = st.builds(
    flowchartpck::BoolLit,
    value=
        st.booleans()
)
flowchartpck::IntegerLit_strategy = st.builds(
    flowchartpck::IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
flowchartpck::VarReference_strategy = st.builds(
    flowchartpck::VarReference,
    key=
        safe_text
)
flowchartpck::ArithmeticExpression_strategy = st.builds(
    flowchartpck::ArithmeticExpression,
    operator=
        safe_text
)
flowchartpck::Literal_strategy = st.builds(
    flowchartpck::Literal,
)
flowchartpck::Expression_strategy = st.builds(
    flowchartpck::Expression,
)
Constraint_strategy = st.builds(
    Constraint,
)
flowchartpck::RelationalConstraint_strategy = st.builds(
    flowchartpck::RelationalConstraint,
)
flowchartpck::Constraint_strategy = st.builds(
    flowchartpck::Constraint,
)
flowchartpck::Program_strategy = st.builds(
    flowchartpck::Program,
)
Node_strategy = st.builds(
    Node,
)
flowchartpck::Decision_strategy = st.builds(
    flowchartpck::Decision,
)
flowchartpck::End_strategy = st.builds(
    flowchartpck::End,
)
flowchartpck::Start_strategy = st.builds(
    flowchartpck::Start,
)
flowchartpck::Action_strategy = st.builds(
    flowchartpck::Action,
)
flowchartpck::RelationalExpression_strategy = st.builds(
    flowchartpck::RelationalExpression,
    operator=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
flowchartpck::Node_strategy = st.builds(
    flowchartpck::Node,
)
flowchartpck::Flowchart_strategy = st.builds(
    flowchartpck::Flowchart,
)
flowchartpck::NamedElement_strategy = st.builds(
    flowchartpck::NamedElement,
    name=
        safe_text
)
flowchartpck::Arc_strategy = st.builds(
    flowchartpck::Arc,
)

@given(instance=ConsoleOutput_strategy)
@settings(max_examples=50)
def test_consoleoutput_instantiation(instance):
    assert isinstance(instance, ConsoleOutput)

@given(instance=flowchartpck::Print_strategy)
@settings(max_examples=50)
def test_flowchartpck::print_instantiation(instance):
    assert isinstance(instance, flowchartpck::Print)

@given(instance=flowchartpck::Println_strategy)
@settings(max_examples=50)
def test_flowchartpck::println_instantiation(instance):
    assert isinstance(instance, flowchartpck::Println)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=flowchartpck::ConsoleOutput_strategy)
@settings(max_examples=50)
def test_flowchartpck::consoleoutput_instantiation(instance):
    assert isinstance(instance, flowchartpck::ConsoleOutput)

@given(instance=flowchartpck::ConsoleOutput_strategy)
def test_flowchartpck::consoleoutput_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=flowchartpck::ConsoleOutput_strategy)
def test_flowchartpck::consoleoutput_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=flowchartpck::VarDecl_strategy)
@settings(max_examples=50)
def test_flowchartpck::vardecl_instantiation(instance):
    assert isinstance(instance, flowchartpck::VarDecl)

@given(instance=flowchartpck::VarDecl_strategy)
def test_flowchartpck::vardecl_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=flowchartpck::VarDecl_strategy)
def test_flowchartpck::vardecl_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=flowchartpck::Assignation_strategy)
@settings(max_examples=50)
def test_flowchartpck::assignation_instantiation(instance):
    assert isinstance(instance, flowchartpck::Assignation)

@given(instance=flowchartpck::Loop_strategy)
@settings(max_examples=50)
def test_flowchartpck::loop_instantiation(instance):
    assert isinstance(instance, flowchartpck::Loop)

@given(instance=flowchartpck::Conditional_strategy)
@settings(max_examples=50)
def test_flowchartpck::conditional_instantiation(instance):
    assert isinstance(instance, flowchartpck::Conditional)

@given(instance=flowchartpck::Statement_strategy)
@settings(max_examples=50)
def test_flowchartpck::statement_instantiation(instance):
    assert isinstance(instance, flowchartpck::Statement)

@given(instance=flowchartpck::Wait_strategy)
@settings(max_examples=50)
def test_flowchartpck::wait_instantiation(instance):
    assert isinstance(instance, flowchartpck::Wait)

@given(instance=flowchartpck::Wait_strategy)
def test_flowchartpck::wait_miliseconds_type(instance):
    assert isinstance(instance.miliseconds, str)


@given(instance=flowchartpck::Wait_strategy)
def test_flowchartpck::wait_miliseconds_setter(instance):
    original = instance.miliseconds
    instance.miliseconds = original
    assert instance.miliseconds == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=flowchartpck::StringLit_strategy)
@settings(max_examples=50)
def test_flowchartpck::stringlit_instantiation(instance):
    assert isinstance(instance, flowchartpck::StringLit)

@given(instance=flowchartpck::StringLit_strategy)
def test_flowchartpck::stringlit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=flowchartpck::StringLit_strategy)
def test_flowchartpck::stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flowchartpck::BoolLit_strategy)
@settings(max_examples=50)
def test_flowchartpck::boollit_instantiation(instance):
    assert isinstance(instance, flowchartpck::BoolLit)

@given(instance=flowchartpck::BoolLit_strategy)
def test_flowchartpck::boollit_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=flowchartpck::BoolLit_strategy)
def test_flowchartpck::boollit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flowchartpck::IntegerLit_strategy)
@settings(max_examples=50)
def test_flowchartpck::integerlit_instantiation(instance):
    assert isinstance(instance, flowchartpck::IntegerLit)

@given(instance=flowchartpck::IntegerLit_strategy)
def test_flowchartpck::integerlit_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=flowchartpck::IntegerLit_strategy)
def test_flowchartpck::integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=flowchartpck::VarReference_strategy)
@settings(max_examples=50)
def test_flowchartpck::varreference_instantiation(instance):
    assert isinstance(instance, flowchartpck::VarReference)

@given(instance=flowchartpck::VarReference_strategy)
def test_flowchartpck::varreference_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=flowchartpck::VarReference_strategy)
def test_flowchartpck::varreference_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=flowchartpck::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_flowchartpck::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, flowchartpck::ArithmeticExpression)

@given(instance=flowchartpck::ArithmeticExpression_strategy)
def test_flowchartpck::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=flowchartpck::ArithmeticExpression_strategy)
def test_flowchartpck::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=flowchartpck::Literal_strategy)
@settings(max_examples=50)
def test_flowchartpck::literal_instantiation(instance):
    assert isinstance(instance, flowchartpck::Literal)

@given(instance=flowchartpck::Expression_strategy)
@settings(max_examples=50)
def test_flowchartpck::expression_instantiation(instance):
    assert isinstance(instance, flowchartpck::Expression)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=flowchartpck::RelationalConstraint_strategy)
@settings(max_examples=50)
def test_flowchartpck::relationalconstraint_instantiation(instance):
    assert isinstance(instance, flowchartpck::RelationalConstraint)

@given(instance=flowchartpck::Constraint_strategy)
@settings(max_examples=50)
def test_flowchartpck::constraint_instantiation(instance):
    assert isinstance(instance, flowchartpck::Constraint)

@given(instance=flowchartpck::Program_strategy)
@settings(max_examples=50)
def test_flowchartpck::program_instantiation(instance):
    assert isinstance(instance, flowchartpck::Program)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=flowchartpck::Decision_strategy)
@settings(max_examples=50)
def test_flowchartpck::decision_instantiation(instance):
    assert isinstance(instance, flowchartpck::Decision)

@given(instance=flowchartpck::End_strategy)
@settings(max_examples=50)
def test_flowchartpck::end_instantiation(instance):
    assert isinstance(instance, flowchartpck::End)

@given(instance=flowchartpck::Start_strategy)
@settings(max_examples=50)
def test_flowchartpck::start_instantiation(instance):
    assert isinstance(instance, flowchartpck::Start)

@given(instance=flowchartpck::Action_strategy)
@settings(max_examples=50)
def test_flowchartpck::action_instantiation(instance):
    assert isinstance(instance, flowchartpck::Action)

@given(instance=flowchartpck::RelationalExpression_strategy)
@settings(max_examples=50)
def test_flowchartpck::relationalexpression_instantiation(instance):
    assert isinstance(instance, flowchartpck::RelationalExpression)

@given(instance=flowchartpck::RelationalExpression_strategy)
def test_flowchartpck::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=flowchartpck::RelationalExpression_strategy)
def test_flowchartpck::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=flowchartpck::Node_strategy)
@settings(max_examples=50)
def test_flowchartpck::node_instantiation(instance):
    assert isinstance(instance, flowchartpck::Node)

@given(instance=flowchartpck::Flowchart_strategy)
@settings(max_examples=50)
def test_flowchartpck::flowchart_instantiation(instance):
    assert isinstance(instance, flowchartpck::Flowchart)

@given(instance=flowchartpck::NamedElement_strategy)
@settings(max_examples=50)
def test_flowchartpck::namedelement_instantiation(instance):
    assert isinstance(instance, flowchartpck::NamedElement)

@given(instance=flowchartpck::NamedElement_strategy)
def test_flowchartpck::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=flowchartpck::NamedElement_strategy)
def test_flowchartpck::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=flowchartpck::Arc_strategy)
@settings(max_examples=50)
def test_flowchartpck::arc_instantiation(instance):
    assert isinstance(instance, flowchartpck::Arc)
