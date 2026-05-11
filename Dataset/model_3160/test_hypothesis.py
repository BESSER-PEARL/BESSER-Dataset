import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TransitionExpression,
    altarica::TransitionOr,
    altarica::TransitionAnd,
    Instruction,
    altarica::Assignment,
    altarica::Conditional,
    altarica::Block,
    altarica::Skip,
    altarica::Transition,
    NamedElement,
    altarica::Variable,
    altarica::Parameter,
    altarica::Node,
    altarica::Event,
    altarica::Attribute,
    altarica::SymbolicConstant,
    altarica::Observer,
    altarica::Domain,
    AbstractDeclaration,
    altarica::AbstractDeclaration,
    altarica::Error,
    altarica::Model,
    Expression,
    altarica::SwitchExpression,
    altarica::ARString,
    altarica::Addition,
    altarica::Multiplication,
    altarica::FunctionCall,
    altarica::LogicalAnd,
    altarica::LogicalOr,
    altarica::Minus,
    altarica::ARNumber,
    altarica::Equal,
    altarica::Not,
    altarica::ARBoolean,
    altarica::Expression,
    altarica::EObject,
    altarica::CaseExpression,
    altarica::Instruction,
    altarica::TransitionExpression,
    altarica::NameRef,
    altarica::LabeledTransition,
    altarica::Declaration,
    Type,
    altarica::NamedType,
    altarica::BaseType,
    altarica::Type,
    Declaration,
    altarica::NamedElement,
    Severity,
    BaseTypeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transitionexpression_is_not_abstract():
    assert not inspect.isabstract(TransitionExpression)


def test_transitionexpression_constructor_exists():
    assert callable(TransitionExpression.__init__)


def test_transitionexpression_constructor_args():
    sig = inspect.signature(TransitionExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::transitionor_is_not_abstract():
    assert not inspect.isabstract(altarica::TransitionOr)


def test_altarica::transitionor_constructor_exists():
    assert callable(altarica::TransitionOr.__init__)


def test_altarica::transitionor_constructor_args():
    sig = inspect.signature(altarica::TransitionOr.__init__)
    params = list(sig.parameters.keys())



def test_altarica::transitionand_is_not_abstract():
    assert not inspect.isabstract(altarica::TransitionAnd)


def test_altarica::transitionand_constructor_exists():
    assert callable(altarica::TransitionAnd.__init__)


def test_altarica::transitionand_constructor_args():
    sig = inspect.signature(altarica::TransitionAnd.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_altarica::assignment_is_not_abstract():
    assert not inspect.isabstract(altarica::Assignment)


def test_altarica::assignment_constructor_exists():
    assert callable(altarica::Assignment.__init__)


def test_altarica::assignment_constructor_args():
    sig = inspect.signature(altarica::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_altarica::conditional_is_not_abstract():
    assert not inspect.isabstract(altarica::Conditional)


def test_altarica::conditional_constructor_exists():
    assert callable(altarica::Conditional.__init__)


def test_altarica::conditional_constructor_args():
    sig = inspect.signature(altarica::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_altarica::block_is_not_abstract():
    assert not inspect.isabstract(altarica::Block)


def test_altarica::block_constructor_exists():
    assert callable(altarica::Block.__init__)


def test_altarica::block_constructor_args():
    sig = inspect.signature(altarica::Block.__init__)
    params = list(sig.parameters.keys())



def test_altarica::skip_is_not_abstract():
    assert not inspect.isabstract(altarica::Skip)


def test_altarica::skip_constructor_exists():
    assert callable(altarica::Skip.__init__)


def test_altarica::skip_constructor_args():
    sig = inspect.signature(altarica::Skip.__init__)
    params = list(sig.parameters.keys())



def test_altarica::transition_is_not_abstract():
    assert not inspect.isabstract(altarica::Transition)


def test_altarica::transition_constructor_exists():
    assert callable(altarica::Transition.__init__)


def test_altarica::transition_constructor_args():
    sig = inspect.signature(altarica::Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_altarica::variable_is_not_abstract():
    assert not inspect.isabstract(altarica::Variable)


def test_altarica::variable_constructor_exists():
    assert callable(altarica::Variable.__init__)


def test_altarica::variable_constructor_args():
    sig = inspect.signature(altarica::Variable.__init__)
    params = list(sig.parameters.keys())



def test_altarica::parameter_is_not_abstract():
    assert not inspect.isabstract(altarica::Parameter)


def test_altarica::parameter_constructor_exists():
    assert callable(altarica::Parameter.__init__)


def test_altarica::parameter_constructor_args():
    sig = inspect.signature(altarica::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_altarica::node_is_not_abstract():
    assert not inspect.isabstract(altarica::Node)


def test_altarica::node_constructor_exists():
    assert callable(altarica::Node.__init__)


def test_altarica::node_constructor_args():
    sig = inspect.signature(altarica::Node.__init__)
    params = list(sig.parameters.keys())



def test_altarica::event_is_not_abstract():
    assert not inspect.isabstract(altarica::Event)


def test_altarica::event_constructor_exists():
    assert callable(altarica::Event.__init__)


def test_altarica::event_constructor_args():
    sig = inspect.signature(altarica::Event.__init__)
    params = list(sig.parameters.keys())



def test_altarica::attribute_is_not_abstract():
    assert not inspect.isabstract(altarica::Attribute)


def test_altarica::attribute_constructor_exists():
    assert callable(altarica::Attribute.__init__)


def test_altarica::attribute_constructor_args():
    sig = inspect.signature(altarica::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_altarica::symbolicconstant_is_not_abstract():
    assert not inspect.isabstract(altarica::SymbolicConstant)


def test_altarica::symbolicconstant_constructor_exists():
    assert callable(altarica::SymbolicConstant.__init__)


def test_altarica::symbolicconstant_constructor_args():
    sig = inspect.signature(altarica::SymbolicConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica::observer_is_not_abstract():
    assert not inspect.isabstract(altarica::Observer)


def test_altarica::observer_constructor_exists():
    assert callable(altarica::Observer.__init__)


def test_altarica::observer_constructor_args():
    sig = inspect.signature(altarica::Observer.__init__)
    params = list(sig.parameters.keys())



def test_altarica::domain_is_not_abstract():
    assert not inspect.isabstract(altarica::Domain)


def test_altarica::domain_constructor_exists():
    assert callable(altarica::Domain.__init__)


def test_altarica::domain_constructor_args():
    sig = inspect.signature(altarica::Domain.__init__)
    params = list(sig.parameters.keys())



def test_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractDeclaration)


def test_abstractdeclaration_constructor_exists():
    assert callable(AbstractDeclaration.__init__)


def test_abstractdeclaration_constructor_args():
    sig = inspect.signature(AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractDeclaration)


def test_altarica::abstractdeclaration_constructor_exists():
    assert callable(altarica::AbstractDeclaration.__init__)


def test_altarica::abstractdeclaration_constructor_args():
    sig = inspect.signature(altarica::AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::error_is_not_abstract():
    assert not inspect.isabstract(altarica::Error)


def test_altarica::error_constructor_exists():
    assert callable(altarica::Error.__init__)


def test_altarica::error_constructor_args():
    sig = inspect.signature(altarica::Error.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "message" in params, "Missing parameter 'message'"

def test_altarica::error_has_severity():
    assert hasattr(altarica::Error, "severity")
    descriptor = None
    for klass in altarica::Error.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_altarica::error_has_message():
    assert hasattr(altarica::Error, "message")
    descriptor = None
    for klass in altarica::Error.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_altarica::model_is_not_abstract():
    assert not inspect.isabstract(altarica::Model)


def test_altarica::model_constructor_exists():
    assert callable(altarica::Model.__init__)


def test_altarica::model_constructor_args():
    sig = inspect.signature(altarica::Model.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::switchexpression_is_not_abstract():
    assert not inspect.isabstract(altarica::SwitchExpression)


def test_altarica::switchexpression_constructor_exists():
    assert callable(altarica::SwitchExpression.__init__)


def test_altarica::switchexpression_constructor_args():
    sig = inspect.signature(altarica::SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::arstring_is_not_abstract():
    assert not inspect.isabstract(altarica::ARString)


def test_altarica::arstring_constructor_exists():
    assert callable(altarica::ARString.__init__)


def test_altarica::arstring_constructor_args():
    sig = inspect.signature(altarica::ARString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica::arstring_has_value():
    assert hasattr(altarica::ARString, "value")
    descriptor = None
    for klass in altarica::ARString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica::addition_is_not_abstract():
    assert not inspect.isabstract(altarica::Addition)


def test_altarica::addition_constructor_exists():
    assert callable(altarica::Addition.__init__)


def test_altarica::addition_constructor_args():
    sig = inspect.signature(altarica::Addition.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica::addition_has_op():
    assert hasattr(altarica::Addition, "op")
    descriptor = None
    for klass in altarica::Addition.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica::multiplication_is_not_abstract():
    assert not inspect.isabstract(altarica::Multiplication)


def test_altarica::multiplication_constructor_exists():
    assert callable(altarica::Multiplication.__init__)


def test_altarica::multiplication_constructor_args():
    sig = inspect.signature(altarica::Multiplication.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica::multiplication_has_op():
    assert hasattr(altarica::Multiplication, "op")
    descriptor = None
    for klass in altarica::Multiplication.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica::functioncall_is_not_abstract():
    assert not inspect.isabstract(altarica::FunctionCall)


def test_altarica::functioncall_constructor_exists():
    assert callable(altarica::FunctionCall.__init__)


def test_altarica::functioncall_constructor_args():
    sig = inspect.signature(altarica::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::functioncall_has_name():
    assert hasattr(altarica::FunctionCall, "name")
    descriptor = None
    for klass in altarica::FunctionCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::logicaland_is_not_abstract():
    assert not inspect.isabstract(altarica::LogicalAnd)


def test_altarica::logicaland_constructor_exists():
    assert callable(altarica::LogicalAnd.__init__)


def test_altarica::logicaland_constructor_args():
    sig = inspect.signature(altarica::LogicalAnd.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica::logicaland_has_op():
    assert hasattr(altarica::LogicalAnd, "op")
    descriptor = None
    for klass in altarica::LogicalAnd.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica::logicalor_is_not_abstract():
    assert not inspect.isabstract(altarica::LogicalOr)


def test_altarica::logicalor_constructor_exists():
    assert callable(altarica::LogicalOr.__init__)


def test_altarica::logicalor_constructor_args():
    sig = inspect.signature(altarica::LogicalOr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica::logicalor_has_op():
    assert hasattr(altarica::LogicalOr, "op")
    descriptor = None
    for klass in altarica::LogicalOr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica::minus_is_not_abstract():
    assert not inspect.isabstract(altarica::Minus)


def test_altarica::minus_constructor_exists():
    assert callable(altarica::Minus.__init__)


def test_altarica::minus_constructor_args():
    sig = inspect.signature(altarica::Minus.__init__)
    params = list(sig.parameters.keys())



def test_altarica::arnumber_is_not_abstract():
    assert not inspect.isabstract(altarica::ARNumber)


def test_altarica::arnumber_constructor_exists():
    assert callable(altarica::ARNumber.__init__)


def test_altarica::arnumber_constructor_args():
    sig = inspect.signature(altarica::ARNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica::arnumber_has_value():
    assert hasattr(altarica::ARNumber, "value")
    descriptor = None
    for klass in altarica::ARNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica::equal_is_not_abstract():
    assert not inspect.isabstract(altarica::Equal)


def test_altarica::equal_constructor_exists():
    assert callable(altarica::Equal.__init__)


def test_altarica::equal_constructor_args():
    sig = inspect.signature(altarica::Equal.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica::equal_has_op():
    assert hasattr(altarica::Equal, "op")
    descriptor = None
    for klass in altarica::Equal.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica::not_is_not_abstract():
    assert not inspect.isabstract(altarica::Not)


def test_altarica::not_constructor_exists():
    assert callable(altarica::Not.__init__)


def test_altarica::not_constructor_args():
    sig = inspect.signature(altarica::Not.__init__)
    params = list(sig.parameters.keys())



def test_altarica::arboolean_is_not_abstract():
    assert not inspect.isabstract(altarica::ARBoolean)


def test_altarica::arboolean_constructor_exists():
    assert callable(altarica::ARBoolean.__init__)


def test_altarica::arboolean_constructor_args():
    sig = inspect.signature(altarica::ARBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica::arboolean_has_value():
    assert hasattr(altarica::ARBoolean, "value")
    descriptor = None
    for klass in altarica::ARBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica::expression_is_not_abstract():
    assert not inspect.isabstract(altarica::Expression)


def test_altarica::expression_constructor_exists():
    assert callable(altarica::Expression.__init__)


def test_altarica::expression_constructor_args():
    sig = inspect.signature(altarica::Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::eobject_is_not_abstract():
    assert not inspect.isabstract(altarica::EObject)


def test_altarica::eobject_constructor_exists():
    assert callable(altarica::EObject.__init__)


def test_altarica::eobject_constructor_args():
    sig = inspect.signature(altarica::EObject.__init__)
    params = list(sig.parameters.keys())



def test_altarica::caseexpression_is_not_abstract():
    assert not inspect.isabstract(altarica::CaseExpression)


def test_altarica::caseexpression_constructor_exists():
    assert callable(altarica::CaseExpression.__init__)


def test_altarica::caseexpression_constructor_args():
    sig = inspect.signature(altarica::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::instruction_is_not_abstract():
    assert not inspect.isabstract(altarica::Instruction)


def test_altarica::instruction_constructor_exists():
    assert callable(altarica::Instruction.__init__)


def test_altarica::instruction_constructor_args():
    sig = inspect.signature(altarica::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_altarica::transitionexpression_is_not_abstract():
    assert not inspect.isabstract(altarica::TransitionExpression)


def test_altarica::transitionexpression_constructor_exists():
    assert callable(altarica::TransitionExpression.__init__)


def test_altarica::transitionexpression_constructor_args():
    sig = inspect.signature(altarica::TransitionExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nameref_is_not_abstract():
    assert not inspect.isabstract(altarica::NameRef)


def test_altarica::nameref_constructor_exists():
    assert callable(altarica::NameRef.__init__)


def test_altarica::nameref_constructor_args():
    sig = inspect.signature(altarica::NameRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::labeledtransition_is_not_abstract():
    assert not inspect.isabstract(altarica::LabeledTransition)


def test_altarica::labeledtransition_constructor_exists():
    assert callable(altarica::LabeledTransition.__init__)


def test_altarica::labeledtransition_constructor_args():
    sig = inspect.signature(altarica::LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_altarica::declaration_is_not_abstract():
    assert not inspect.isabstract(altarica::Declaration)


def test_altarica::declaration_constructor_exists():
    assert callable(altarica::Declaration.__init__)


def test_altarica::declaration_constructor_args():
    sig = inspect.signature(altarica::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_altarica::namedtype_is_not_abstract():
    assert not inspect.isabstract(altarica::NamedType)


def test_altarica::namedtype_constructor_exists():
    assert callable(altarica::NamedType.__init__)


def test_altarica::namedtype_constructor_args():
    sig = inspect.signature(altarica::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_altarica::basetype_is_not_abstract():
    assert not inspect.isabstract(altarica::BaseType)


def test_altarica::basetype_constructor_exists():
    assert callable(altarica::BaseType.__init__)


def test_altarica::basetype_constructor_args():
    sig = inspect.signature(altarica::BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::basetype_has_name():
    assert hasattr(altarica::BaseType, "name")
    descriptor = None
    for klass in altarica::BaseType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::type_is_not_abstract():
    assert not inspect.isabstract(altarica::Type)


def test_altarica::type_constructor_exists():
    assert callable(altarica::Type.__init__)


def test_altarica::type_constructor_args():
    sig = inspect.signature(altarica::Type.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::namedelement_is_not_abstract():
    assert not inspect.isabstract(altarica::NamedElement)


def test_altarica::namedelement_constructor_exists():
    assert callable(altarica::NamedElement.__init__)


def test_altarica::namedelement_constructor_args():
    sig = inspect.signature(altarica::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::namedelement_has_name():
    assert hasattr(altarica::NamedElement, "name")
    descriptor = None
    for klass in altarica::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "WARNING",
        "ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"

def test_basetypeenum_exists():
    # Check that the Enumeration exists
    assert BaseTypeEnum is not None

def test_basetypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BaseTypeEnum]
    expected_literals = [
        "BOOLEAN",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BaseTypeEnum"


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
TransitionExpression_strategy = st.builds(
    TransitionExpression,
)
altarica::TransitionOr_strategy = st.builds(
    altarica::TransitionOr,
)
altarica::TransitionAnd_strategy = st.builds(
    altarica::TransitionAnd,
)
Instruction_strategy = st.builds(
    Instruction,
)
altarica::Assignment_strategy = st.builds(
    altarica::Assignment,
)
altarica::Conditional_strategy = st.builds(
    altarica::Conditional,
)
altarica::Block_strategy = st.builds(
    altarica::Block,
)
altarica::Skip_strategy = st.builds(
    altarica::Skip,
)
altarica::Transition_strategy = st.builds(
    altarica::Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
altarica::Variable_strategy = st.builds(
    altarica::Variable,
)
altarica::Parameter_strategy = st.builds(
    altarica::Parameter,
)
altarica::Node_strategy = st.builds(
    altarica::Node,
)
altarica::Event_strategy = st.builds(
    altarica::Event,
)
altarica::Attribute_strategy = st.builds(
    altarica::Attribute,
)
altarica::SymbolicConstant_strategy = st.builds(
    altarica::SymbolicConstant,
)
altarica::Observer_strategy = st.builds(
    altarica::Observer,
)
altarica::Domain_strategy = st.builds(
    altarica::Domain,
)
AbstractDeclaration_strategy = st.builds(
    AbstractDeclaration,
)
altarica::AbstractDeclaration_strategy = st.builds(
    altarica::AbstractDeclaration,
)
altarica::Error_strategy = st.builds(
    altarica::Error,
    severity=
        safe_text,
    message=
        safe_text
)
altarica::Model_strategy = st.builds(
    altarica::Model,
)
Expression_strategy = st.builds(
    Expression,
)
altarica::SwitchExpression_strategy = st.builds(
    altarica::SwitchExpression,
)
altarica::ARString_strategy = st.builds(
    altarica::ARString,
    value=
        safe_text
)
altarica::Addition_strategy = st.builds(
    altarica::Addition,
    op=
        safe_text
)
altarica::Multiplication_strategy = st.builds(
    altarica::Multiplication,
    op=
        safe_text
)
altarica::FunctionCall_strategy = st.builds(
    altarica::FunctionCall,
    name=
        safe_text
)
altarica::LogicalAnd_strategy = st.builds(
    altarica::LogicalAnd,
    op=
        safe_text
)
altarica::LogicalOr_strategy = st.builds(
    altarica::LogicalOr,
    op=
        safe_text
)
altarica::Minus_strategy = st.builds(
    altarica::Minus,
)
altarica::ARNumber_strategy = st.builds(
    altarica::ARNumber,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
altarica::Equal_strategy = st.builds(
    altarica::Equal,
    op=
        safe_text
)
altarica::Not_strategy = st.builds(
    altarica::Not,
)
altarica::ARBoolean_strategy = st.builds(
    altarica::ARBoolean,
    value=
        safe_text
)
altarica::Expression_strategy = st.builds(
    altarica::Expression,
)
altarica::EObject_strategy = st.builds(
    altarica::EObject,
)
altarica::CaseExpression_strategy = st.builds(
    altarica::CaseExpression,
)
altarica::Instruction_strategy = st.builds(
    altarica::Instruction,
)
altarica::TransitionExpression_strategy = st.builds(
    altarica::TransitionExpression,
)
altarica::NameRef_strategy = st.builds(
    altarica::NameRef,
)
altarica::LabeledTransition_strategy = st.builds(
    altarica::LabeledTransition,
)
altarica::Declaration_strategy = st.builds(
    altarica::Declaration,
)
Type_strategy = st.builds(
    Type,
)
altarica::NamedType_strategy = st.builds(
    altarica::NamedType,
)
altarica::BaseType_strategy = st.builds(
    altarica::BaseType,
    name=
        safe_text
)
altarica::Type_strategy = st.builds(
    altarica::Type,
)
Declaration_strategy = st.builds(
    Declaration,
)
altarica::NamedElement_strategy = st.builds(
    altarica::NamedElement,
    name=
        safe_text
)

@given(instance=TransitionExpression_strategy)
@settings(max_examples=50)
def test_transitionexpression_instantiation(instance):
    assert isinstance(instance, TransitionExpression)

@given(instance=altarica::TransitionOr_strategy)
@settings(max_examples=50)
def test_altarica::transitionor_instantiation(instance):
    assert isinstance(instance, altarica::TransitionOr)

@given(instance=altarica::TransitionAnd_strategy)
@settings(max_examples=50)
def test_altarica::transitionand_instantiation(instance):
    assert isinstance(instance, altarica::TransitionAnd)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=altarica::Assignment_strategy)
@settings(max_examples=50)
def test_altarica::assignment_instantiation(instance):
    assert isinstance(instance, altarica::Assignment)

@given(instance=altarica::Conditional_strategy)
@settings(max_examples=50)
def test_altarica::conditional_instantiation(instance):
    assert isinstance(instance, altarica::Conditional)

@given(instance=altarica::Block_strategy)
@settings(max_examples=50)
def test_altarica::block_instantiation(instance):
    assert isinstance(instance, altarica::Block)

@given(instance=altarica::Skip_strategy)
@settings(max_examples=50)
def test_altarica::skip_instantiation(instance):
    assert isinstance(instance, altarica::Skip)

@given(instance=altarica::Transition_strategy)
@settings(max_examples=50)
def test_altarica::transition_instantiation(instance):
    assert isinstance(instance, altarica::Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=altarica::Variable_strategy)
@settings(max_examples=50)
def test_altarica::variable_instantiation(instance):
    assert isinstance(instance, altarica::Variable)

@given(instance=altarica::Parameter_strategy)
@settings(max_examples=50)
def test_altarica::parameter_instantiation(instance):
    assert isinstance(instance, altarica::Parameter)

@given(instance=altarica::Node_strategy)
@settings(max_examples=50)
def test_altarica::node_instantiation(instance):
    assert isinstance(instance, altarica::Node)

@given(instance=altarica::Event_strategy)
@settings(max_examples=50)
def test_altarica::event_instantiation(instance):
    assert isinstance(instance, altarica::Event)

@given(instance=altarica::Attribute_strategy)
@settings(max_examples=50)
def test_altarica::attribute_instantiation(instance):
    assert isinstance(instance, altarica::Attribute)

@given(instance=altarica::SymbolicConstant_strategy)
@settings(max_examples=50)
def test_altarica::symbolicconstant_instantiation(instance):
    assert isinstance(instance, altarica::SymbolicConstant)

@given(instance=altarica::Observer_strategy)
@settings(max_examples=50)
def test_altarica::observer_instantiation(instance):
    assert isinstance(instance, altarica::Observer)

@given(instance=altarica::Domain_strategy)
@settings(max_examples=50)
def test_altarica::domain_instantiation(instance):
    assert isinstance(instance, altarica::Domain)

@given(instance=AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, AbstractDeclaration)

@given(instance=altarica::AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_altarica::abstractdeclaration_instantiation(instance):
    assert isinstance(instance, altarica::AbstractDeclaration)

@given(instance=altarica::Error_strategy)
@settings(max_examples=50)
def test_altarica::error_instantiation(instance):
    assert isinstance(instance, altarica::Error)

@given(instance=altarica::Error_strategy)
def test_altarica::error_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=altarica::Error_strategy)
def test_altarica::error_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=altarica::Error_strategy)
def test_altarica::error_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=altarica::Error_strategy)
def test_altarica::error_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=altarica::Model_strategy)
@settings(max_examples=50)
def test_altarica::model_instantiation(instance):
    assert isinstance(instance, altarica::Model)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=altarica::SwitchExpression_strategy)
@settings(max_examples=50)
def test_altarica::switchexpression_instantiation(instance):
    assert isinstance(instance, altarica::SwitchExpression)

@given(instance=altarica::ARString_strategy)
@settings(max_examples=50)
def test_altarica::arstring_instantiation(instance):
    assert isinstance(instance, altarica::ARString)

@given(instance=altarica::ARString_strategy)
def test_altarica::arstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=altarica::ARString_strategy)
def test_altarica::arstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica::Addition_strategy)
@settings(max_examples=50)
def test_altarica::addition_instantiation(instance):
    assert isinstance(instance, altarica::Addition)

@given(instance=altarica::Addition_strategy)
def test_altarica::addition_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=altarica::Addition_strategy)
def test_altarica::addition_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica::Multiplication_strategy)
@settings(max_examples=50)
def test_altarica::multiplication_instantiation(instance):
    assert isinstance(instance, altarica::Multiplication)

@given(instance=altarica::Multiplication_strategy)
def test_altarica::multiplication_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=altarica::Multiplication_strategy)
def test_altarica::multiplication_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica::FunctionCall_strategy)
@settings(max_examples=50)
def test_altarica::functioncall_instantiation(instance):
    assert isinstance(instance, altarica::FunctionCall)

@given(instance=altarica::FunctionCall_strategy)
def test_altarica::functioncall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::FunctionCall_strategy)
def test_altarica::functioncall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::LogicalAnd_strategy)
@settings(max_examples=50)
def test_altarica::logicaland_instantiation(instance):
    assert isinstance(instance, altarica::LogicalAnd)

@given(instance=altarica::LogicalAnd_strategy)
def test_altarica::logicaland_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=altarica::LogicalAnd_strategy)
def test_altarica::logicaland_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica::LogicalOr_strategy)
@settings(max_examples=50)
def test_altarica::logicalor_instantiation(instance):
    assert isinstance(instance, altarica::LogicalOr)

@given(instance=altarica::LogicalOr_strategy)
def test_altarica::logicalor_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=altarica::LogicalOr_strategy)
def test_altarica::logicalor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica::Minus_strategy)
@settings(max_examples=50)
def test_altarica::minus_instantiation(instance):
    assert isinstance(instance, altarica::Minus)

@given(instance=altarica::ARNumber_strategy)
@settings(max_examples=50)
def test_altarica::arnumber_instantiation(instance):
    assert isinstance(instance, altarica::ARNumber)

@given(instance=altarica::ARNumber_strategy)
def test_altarica::arnumber_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=altarica::ARNumber_strategy)
def test_altarica::arnumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica::Equal_strategy)
@settings(max_examples=50)
def test_altarica::equal_instantiation(instance):
    assert isinstance(instance, altarica::Equal)

@given(instance=altarica::Equal_strategy)
def test_altarica::equal_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=altarica::Equal_strategy)
def test_altarica::equal_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica::Not_strategy)
@settings(max_examples=50)
def test_altarica::not_instantiation(instance):
    assert isinstance(instance, altarica::Not)

@given(instance=altarica::ARBoolean_strategy)
@settings(max_examples=50)
def test_altarica::arboolean_instantiation(instance):
    assert isinstance(instance, altarica::ARBoolean)

@given(instance=altarica::ARBoolean_strategy)
def test_altarica::arboolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=altarica::ARBoolean_strategy)
def test_altarica::arboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica::Expression_strategy)
@settings(max_examples=50)
def test_altarica::expression_instantiation(instance):
    assert isinstance(instance, altarica::Expression)

@given(instance=altarica::EObject_strategy)
@settings(max_examples=50)
def test_altarica::eobject_instantiation(instance):
    assert isinstance(instance, altarica::EObject)

@given(instance=altarica::CaseExpression_strategy)
@settings(max_examples=50)
def test_altarica::caseexpression_instantiation(instance):
    assert isinstance(instance, altarica::CaseExpression)

@given(instance=altarica::Instruction_strategy)
@settings(max_examples=50)
def test_altarica::instruction_instantiation(instance):
    assert isinstance(instance, altarica::Instruction)

@given(instance=altarica::TransitionExpression_strategy)
@settings(max_examples=50)
def test_altarica::transitionexpression_instantiation(instance):
    assert isinstance(instance, altarica::TransitionExpression)

@given(instance=altarica::NameRef_strategy)
@settings(max_examples=50)
def test_altarica::nameref_instantiation(instance):
    assert isinstance(instance, altarica::NameRef)

@given(instance=altarica::LabeledTransition_strategy)
@settings(max_examples=50)
def test_altarica::labeledtransition_instantiation(instance):
    assert isinstance(instance, altarica::LabeledTransition)

@given(instance=altarica::Declaration_strategy)
@settings(max_examples=50)
def test_altarica::declaration_instantiation(instance):
    assert isinstance(instance, altarica::Declaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=altarica::NamedType_strategy)
@settings(max_examples=50)
def test_altarica::namedtype_instantiation(instance):
    assert isinstance(instance, altarica::NamedType)

@given(instance=altarica::BaseType_strategy)
@settings(max_examples=50)
def test_altarica::basetype_instantiation(instance):
    assert isinstance(instance, altarica::BaseType)

@given(instance=altarica::BaseType_strategy)
def test_altarica::basetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::BaseType_strategy)
def test_altarica::basetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::Type_strategy)
@settings(max_examples=50)
def test_altarica::type_instantiation(instance):
    assert isinstance(instance, altarica::Type)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=altarica::NamedElement_strategy)
@settings(max_examples=50)
def test_altarica::namedelement_instantiation(instance):
    assert isinstance(instance, altarica::NamedElement)

@given(instance=altarica::NamedElement_strategy)
def test_altarica::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::NamedElement_strategy)
def test_altarica::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
