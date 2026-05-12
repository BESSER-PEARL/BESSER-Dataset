import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TransitionExpression,
    altarica_TransitionOr,
    altarica_TransitionAnd,
    Instruction,
    altarica_Block,
    altarica_Assignment,
    altarica_Conditional,
    altarica_Skip,
    altarica_Transition,
    NamedElement,
    altarica_Event,
    altarica_Node,
    altarica_Parameter,
    altarica_Attribute,
    altarica_SymbolicConstant,
    altarica_Observer,
    altarica_Variable,
    altarica_Domain,
    AbstractDeclaration,
    altarica_AbstractDeclaration,
    altarica_Error,
    altarica_Model,
    Expression,
    altarica_Equal,
    altarica_ARString,
    altarica_ARNumber,
    altarica_LogicalAnd,
    altarica_SwitchExpression,
    altarica_FunctionCall,
    altarica_Addition,
    altarica_LogicalOr,
    altarica_Minus,
    altarica_Multiplication,
    altarica_Not,
    altarica_ARBoolean,
    altarica_Expression,
    altarica_EObject,
    altarica_CaseExpression,
    altarica_Instruction,
    altarica_TransitionExpression,
    altarica_NameRef,
    altarica_LabeledTransition,
    altarica_Declaration,
    Type,
    altarica_NamedType,
    altarica_BaseType,
    altarica_Type,
    Declaration,
    altarica_NamedElement,
    BaseTypeEnum,
    Severity,
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



def test_altarica_transitionor_is_not_abstract():
    assert not inspect.isabstract(altarica_TransitionOr)


def test_altarica_transitionor_constructor_exists():
    assert callable(altarica_TransitionOr.__init__)


def test_altarica_transitionor_constructor_args():
    sig = inspect.signature(altarica_TransitionOr.__init__)
    params = list(sig.parameters.keys())



def test_altarica_transitionand_is_not_abstract():
    assert not inspect.isabstract(altarica_TransitionAnd)


def test_altarica_transitionand_constructor_exists():
    assert callable(altarica_TransitionAnd.__init__)


def test_altarica_transitionand_constructor_args():
    sig = inspect.signature(altarica_TransitionAnd.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_altarica_block_is_not_abstract():
    assert not inspect.isabstract(altarica_Block)


def test_altarica_block_constructor_exists():
    assert callable(altarica_Block.__init__)


def test_altarica_block_constructor_args():
    sig = inspect.signature(altarica_Block.__init__)
    params = list(sig.parameters.keys())



def test_altarica_assignment_is_not_abstract():
    assert not inspect.isabstract(altarica_Assignment)


def test_altarica_assignment_constructor_exists():
    assert callable(altarica_Assignment.__init__)


def test_altarica_assignment_constructor_args():
    sig = inspect.signature(altarica_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_altarica_conditional_is_not_abstract():
    assert not inspect.isabstract(altarica_Conditional)


def test_altarica_conditional_constructor_exists():
    assert callable(altarica_Conditional.__init__)


def test_altarica_conditional_constructor_args():
    sig = inspect.signature(altarica_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_altarica_skip_is_not_abstract():
    assert not inspect.isabstract(altarica_Skip)


def test_altarica_skip_constructor_exists():
    assert callable(altarica_Skip.__init__)


def test_altarica_skip_constructor_args():
    sig = inspect.signature(altarica_Skip.__init__)
    params = list(sig.parameters.keys())



def test_altarica_transition_is_not_abstract():
    assert not inspect.isabstract(altarica_Transition)


def test_altarica_transition_constructor_exists():
    assert callable(altarica_Transition.__init__)


def test_altarica_transition_constructor_args():
    sig = inspect.signature(altarica_Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_altarica_event_is_not_abstract():
    assert not inspect.isabstract(altarica_Event)


def test_altarica_event_constructor_exists():
    assert callable(altarica_Event.__init__)


def test_altarica_event_constructor_args():
    sig = inspect.signature(altarica_Event.__init__)
    params = list(sig.parameters.keys())



def test_altarica_node_is_not_abstract():
    assert not inspect.isabstract(altarica_Node)


def test_altarica_node_constructor_exists():
    assert callable(altarica_Node.__init__)


def test_altarica_node_constructor_args():
    sig = inspect.signature(altarica_Node.__init__)
    params = list(sig.parameters.keys())



def test_altarica_parameter_is_not_abstract():
    assert not inspect.isabstract(altarica_Parameter)


def test_altarica_parameter_constructor_exists():
    assert callable(altarica_Parameter.__init__)


def test_altarica_parameter_constructor_args():
    sig = inspect.signature(altarica_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_altarica_attribute_is_not_abstract():
    assert not inspect.isabstract(altarica_Attribute)


def test_altarica_attribute_constructor_exists():
    assert callable(altarica_Attribute.__init__)


def test_altarica_attribute_constructor_args():
    sig = inspect.signature(altarica_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_altarica_symbolicconstant_is_not_abstract():
    assert not inspect.isabstract(altarica_SymbolicConstant)


def test_altarica_symbolicconstant_constructor_exists():
    assert callable(altarica_SymbolicConstant.__init__)


def test_altarica_symbolicconstant_constructor_args():
    sig = inspect.signature(altarica_SymbolicConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica_observer_is_not_abstract():
    assert not inspect.isabstract(altarica_Observer)


def test_altarica_observer_constructor_exists():
    assert callable(altarica_Observer.__init__)


def test_altarica_observer_constructor_args():
    sig = inspect.signature(altarica_Observer.__init__)
    params = list(sig.parameters.keys())



def test_altarica_variable_is_not_abstract():
    assert not inspect.isabstract(altarica_Variable)


def test_altarica_variable_constructor_exists():
    assert callable(altarica_Variable.__init__)


def test_altarica_variable_constructor_args():
    sig = inspect.signature(altarica_Variable.__init__)
    params = list(sig.parameters.keys())



def test_altarica_domain_is_not_abstract():
    assert not inspect.isabstract(altarica_Domain)


def test_altarica_domain_constructor_exists():
    assert callable(altarica_Domain.__init__)


def test_altarica_domain_constructor_args():
    sig = inspect.signature(altarica_Domain.__init__)
    params = list(sig.parameters.keys())



def test_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractDeclaration)


def test_abstractdeclaration_constructor_exists():
    assert callable(AbstractDeclaration.__init__)


def test_abstractdeclaration_constructor_args():
    sig = inspect.signature(AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractDeclaration)


def test_altarica_abstractdeclaration_constructor_exists():
    assert callable(altarica_AbstractDeclaration.__init__)


def test_altarica_abstractdeclaration_constructor_args():
    sig = inspect.signature(altarica_AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_error_is_not_abstract():
    assert not inspect.isabstract(altarica_Error)


def test_altarica_error_constructor_exists():
    assert callable(altarica_Error.__init__)


def test_altarica_error_constructor_args():
    sig = inspect.signature(altarica_Error.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "severity" in params, "Missing parameter 'severity'"

def test_altarica_error_has_message():
    assert hasattr(altarica_Error, "message")
    descriptor = None
    for klass in altarica_Error.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_altarica_error_has_severity():
    assert hasattr(altarica_Error, "severity")
    descriptor = None
    for klass in altarica_Error.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_altarica_model_is_not_abstract():
    assert not inspect.isabstract(altarica_Model)


def test_altarica_model_constructor_exists():
    assert callable(altarica_Model.__init__)


def test_altarica_model_constructor_args():
    sig = inspect.signature(altarica_Model.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_equal_is_not_abstract():
    assert not inspect.isabstract(altarica_Equal)


def test_altarica_equal_constructor_exists():
    assert callable(altarica_Equal.__init__)


def test_altarica_equal_constructor_args():
    sig = inspect.signature(altarica_Equal.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica_equal_has_op():
    assert hasattr(altarica_Equal, "op")
    descriptor = None
    for klass in altarica_Equal.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica_arstring_is_not_abstract():
    assert not inspect.isabstract(altarica_ARString)


def test_altarica_arstring_constructor_exists():
    assert callable(altarica_ARString.__init__)


def test_altarica_arstring_constructor_args():
    sig = inspect.signature(altarica_ARString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica_arstring_has_value():
    assert hasattr(altarica_ARString, "value")
    descriptor = None
    for klass in altarica_ARString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica_arnumber_is_not_abstract():
    assert not inspect.isabstract(altarica_ARNumber)


def test_altarica_arnumber_constructor_exists():
    assert callable(altarica_ARNumber.__init__)


def test_altarica_arnumber_constructor_args():
    sig = inspect.signature(altarica_ARNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica_arnumber_has_value():
    assert hasattr(altarica_ARNumber, "value")
    descriptor = None
    for klass in altarica_ARNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica_logicaland_is_not_abstract():
    assert not inspect.isabstract(altarica_LogicalAnd)


def test_altarica_logicaland_constructor_exists():
    assert callable(altarica_LogicalAnd.__init__)


def test_altarica_logicaland_constructor_args():
    sig = inspect.signature(altarica_LogicalAnd.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica_logicaland_has_op():
    assert hasattr(altarica_LogicalAnd, "op")
    descriptor = None
    for klass in altarica_LogicalAnd.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica_switchexpression_is_not_abstract():
    assert not inspect.isabstract(altarica_SwitchExpression)


def test_altarica_switchexpression_constructor_exists():
    assert callable(altarica_SwitchExpression.__init__)


def test_altarica_switchexpression_constructor_args():
    sig = inspect.signature(altarica_SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_functioncall_is_not_abstract():
    assert not inspect.isabstract(altarica_FunctionCall)


def test_altarica_functioncall_constructor_exists():
    assert callable(altarica_FunctionCall.__init__)


def test_altarica_functioncall_constructor_args():
    sig = inspect.signature(altarica_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_functioncall_has_name():
    assert hasattr(altarica_FunctionCall, "name")
    descriptor = None
    for klass in altarica_FunctionCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_addition_is_not_abstract():
    assert not inspect.isabstract(altarica_Addition)


def test_altarica_addition_constructor_exists():
    assert callable(altarica_Addition.__init__)


def test_altarica_addition_constructor_args():
    sig = inspect.signature(altarica_Addition.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica_addition_has_op():
    assert hasattr(altarica_Addition, "op")
    descriptor = None
    for klass in altarica_Addition.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica_logicalor_is_not_abstract():
    assert not inspect.isabstract(altarica_LogicalOr)


def test_altarica_logicalor_constructor_exists():
    assert callable(altarica_LogicalOr.__init__)


def test_altarica_logicalor_constructor_args():
    sig = inspect.signature(altarica_LogicalOr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica_logicalor_has_op():
    assert hasattr(altarica_LogicalOr, "op")
    descriptor = None
    for klass in altarica_LogicalOr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica_minus_is_not_abstract():
    assert not inspect.isabstract(altarica_Minus)


def test_altarica_minus_constructor_exists():
    assert callable(altarica_Minus.__init__)


def test_altarica_minus_constructor_args():
    sig = inspect.signature(altarica_Minus.__init__)
    params = list(sig.parameters.keys())



def test_altarica_multiplication_is_not_abstract():
    assert not inspect.isabstract(altarica_Multiplication)


def test_altarica_multiplication_constructor_exists():
    assert callable(altarica_Multiplication.__init__)


def test_altarica_multiplication_constructor_args():
    sig = inspect.signature(altarica_Multiplication.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_altarica_multiplication_has_op():
    assert hasattr(altarica_Multiplication, "op")
    descriptor = None
    for klass in altarica_Multiplication.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_altarica_not_is_not_abstract():
    assert not inspect.isabstract(altarica_Not)


def test_altarica_not_constructor_exists():
    assert callable(altarica_Not.__init__)


def test_altarica_not_constructor_args():
    sig = inspect.signature(altarica_Not.__init__)
    params = list(sig.parameters.keys())



def test_altarica_arboolean_is_not_abstract():
    assert not inspect.isabstract(altarica_ARBoolean)


def test_altarica_arboolean_constructor_exists():
    assert callable(altarica_ARBoolean.__init__)


def test_altarica_arboolean_constructor_args():
    sig = inspect.signature(altarica_ARBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica_arboolean_has_value():
    assert hasattr(altarica_ARBoolean, "value")
    descriptor = None
    for klass in altarica_ARBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica_expression_is_not_abstract():
    assert not inspect.isabstract(altarica_Expression)


def test_altarica_expression_constructor_exists():
    assert callable(altarica_Expression.__init__)


def test_altarica_expression_constructor_args():
    sig = inspect.signature(altarica_Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_eobject_is_not_abstract():
    assert not inspect.isabstract(altarica_EObject)


def test_altarica_eobject_constructor_exists():
    assert callable(altarica_EObject.__init__)


def test_altarica_eobject_constructor_args():
    sig = inspect.signature(altarica_EObject.__init__)
    params = list(sig.parameters.keys())



def test_altarica_caseexpression_is_not_abstract():
    assert not inspect.isabstract(altarica_CaseExpression)


def test_altarica_caseexpression_constructor_exists():
    assert callable(altarica_CaseExpression.__init__)


def test_altarica_caseexpression_constructor_args():
    sig = inspect.signature(altarica_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_instruction_is_not_abstract():
    assert not inspect.isabstract(altarica_Instruction)


def test_altarica_instruction_constructor_exists():
    assert callable(altarica_Instruction.__init__)


def test_altarica_instruction_constructor_args():
    sig = inspect.signature(altarica_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_altarica_transitionexpression_is_not_abstract():
    assert not inspect.isabstract(altarica_TransitionExpression)


def test_altarica_transitionexpression_constructor_exists():
    assert callable(altarica_TransitionExpression.__init__)


def test_altarica_transitionexpression_constructor_args():
    sig = inspect.signature(altarica_TransitionExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nameref_is_not_abstract():
    assert not inspect.isabstract(altarica_NameRef)


def test_altarica_nameref_constructor_exists():
    assert callable(altarica_NameRef.__init__)


def test_altarica_nameref_constructor_args():
    sig = inspect.signature(altarica_NameRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_labeledtransition_is_not_abstract():
    assert not inspect.isabstract(altarica_LabeledTransition)


def test_altarica_labeledtransition_constructor_exists():
    assert callable(altarica_LabeledTransition.__init__)


def test_altarica_labeledtransition_constructor_args():
    sig = inspect.signature(altarica_LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_altarica_declaration_is_not_abstract():
    assert not inspect.isabstract(altarica_Declaration)


def test_altarica_declaration_constructor_exists():
    assert callable(altarica_Declaration.__init__)


def test_altarica_declaration_constructor_args():
    sig = inspect.signature(altarica_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_altarica_namedtype_is_not_abstract():
    assert not inspect.isabstract(altarica_NamedType)


def test_altarica_namedtype_constructor_exists():
    assert callable(altarica_NamedType.__init__)


def test_altarica_namedtype_constructor_args():
    sig = inspect.signature(altarica_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_altarica_basetype_is_not_abstract():
    assert not inspect.isabstract(altarica_BaseType)


def test_altarica_basetype_constructor_exists():
    assert callable(altarica_BaseType.__init__)


def test_altarica_basetype_constructor_args():
    sig = inspect.signature(altarica_BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_basetype_has_name():
    assert hasattr(altarica_BaseType, "name")
    descriptor = None
    for klass in altarica_BaseType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_type_is_not_abstract():
    assert not inspect.isabstract(altarica_Type)


def test_altarica_type_constructor_exists():
    assert callable(altarica_Type.__init__)


def test_altarica_type_constructor_args():
    sig = inspect.signature(altarica_Type.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_namedelement_is_not_abstract():
    assert not inspect.isabstract(altarica_NamedElement)


def test_altarica_namedelement_constructor_exists():
    assert callable(altarica_NamedElement.__init__)


def test_altarica_namedelement_constructor_args():
    sig = inspect.signature(altarica_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_namedelement_has_name():
    assert hasattr(altarica_NamedElement, "name")
    descriptor = None
    for klass in altarica_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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
altarica_TransitionOr_strategy = st.builds(
    altarica_TransitionOr,
)
altarica_TransitionAnd_strategy = st.builds(
    altarica_TransitionAnd,
)
Instruction_strategy = st.builds(
    Instruction,
)
altarica_Block_strategy = st.builds(
    altarica_Block,
)
altarica_Assignment_strategy = st.builds(
    altarica_Assignment,
)
altarica_Conditional_strategy = st.builds(
    altarica_Conditional,
)
altarica_Skip_strategy = st.builds(
    altarica_Skip,
)
altarica_Transition_strategy = st.builds(
    altarica_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
altarica_Event_strategy = st.builds(
    altarica_Event,
)
altarica_Node_strategy = st.builds(
    altarica_Node,
)
altarica_Parameter_strategy = st.builds(
    altarica_Parameter,
)
altarica_Attribute_strategy = st.builds(
    altarica_Attribute,
)
altarica_SymbolicConstant_strategy = st.builds(
    altarica_SymbolicConstant,
)
altarica_Observer_strategy = st.builds(
    altarica_Observer,
)
altarica_Variable_strategy = st.builds(
    altarica_Variable,
)
altarica_Domain_strategy = st.builds(
    altarica_Domain,
)
AbstractDeclaration_strategy = st.builds(
    AbstractDeclaration,
)
altarica_AbstractDeclaration_strategy = st.builds(
    altarica_AbstractDeclaration,
)
altarica_Error_strategy = st.builds(
    altarica_Error,
    message=
        safe_text,
    severity=
        safe_text
)
altarica_Model_strategy = st.builds(
    altarica_Model,
)
Expression_strategy = st.builds(
    Expression,
)
altarica_Equal_strategy = st.builds(
    altarica_Equal,
    op=
        safe_text
)
altarica_ARString_strategy = st.builds(
    altarica_ARString,
    value=
        safe_text
)
altarica_ARNumber_strategy = st.builds(
    altarica_ARNumber,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
altarica_LogicalAnd_strategy = st.builds(
    altarica_LogicalAnd,
    op=
        safe_text
)
altarica_SwitchExpression_strategy = st.builds(
    altarica_SwitchExpression,
)
altarica_FunctionCall_strategy = st.builds(
    altarica_FunctionCall,
    name=
        safe_text
)
altarica_Addition_strategy = st.builds(
    altarica_Addition,
    op=
        safe_text
)
altarica_LogicalOr_strategy = st.builds(
    altarica_LogicalOr,
    op=
        safe_text
)
altarica_Minus_strategy = st.builds(
    altarica_Minus,
)
altarica_Multiplication_strategy = st.builds(
    altarica_Multiplication,
    op=
        safe_text
)
altarica_Not_strategy = st.builds(
    altarica_Not,
)
altarica_ARBoolean_strategy = st.builds(
    altarica_ARBoolean,
    value=
        safe_text
)
altarica_Expression_strategy = st.builds(
    altarica_Expression,
)
altarica_EObject_strategy = st.builds(
    altarica_EObject,
)
altarica_CaseExpression_strategy = st.builds(
    altarica_CaseExpression,
)
altarica_Instruction_strategy = st.builds(
    altarica_Instruction,
)
altarica_TransitionExpression_strategy = st.builds(
    altarica_TransitionExpression,
)
altarica_NameRef_strategy = st.builds(
    altarica_NameRef,
)
altarica_LabeledTransition_strategy = st.builds(
    altarica_LabeledTransition,
)
altarica_Declaration_strategy = st.builds(
    altarica_Declaration,
)
Type_strategy = st.builds(
    Type,
)
altarica_NamedType_strategy = st.builds(
    altarica_NamedType,
)
altarica_BaseType_strategy = st.builds(
    altarica_BaseType,
    name=
        safe_text
)
altarica_Type_strategy = st.builds(
    altarica_Type,
)
Declaration_strategy = st.builds(
    Declaration,
)
altarica_NamedElement_strategy = st.builds(
    altarica_NamedElement,
    name=
        safe_text
)

@given(instance=TransitionExpression_strategy)
@settings(max_examples=50)
def test_transitionexpression_instantiation(instance):
    assert isinstance(instance, TransitionExpression)

@given(instance=altarica_TransitionOr_strategy)
@settings(max_examples=50)
def test_altarica_transitionor_instantiation(instance):
    assert isinstance(instance, altarica_TransitionOr)

@given(instance=altarica_TransitionAnd_strategy)
@settings(max_examples=50)
def test_altarica_transitionand_instantiation(instance):
    assert isinstance(instance, altarica_TransitionAnd)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=altarica_Block_strategy)
@settings(max_examples=50)
def test_altarica_block_instantiation(instance):
    assert isinstance(instance, altarica_Block)

@given(instance=altarica_Assignment_strategy)
@settings(max_examples=50)
def test_altarica_assignment_instantiation(instance):
    assert isinstance(instance, altarica_Assignment)

@given(instance=altarica_Conditional_strategy)
@settings(max_examples=50)
def test_altarica_conditional_instantiation(instance):
    assert isinstance(instance, altarica_Conditional)

@given(instance=altarica_Skip_strategy)
@settings(max_examples=50)
def test_altarica_skip_instantiation(instance):
    assert isinstance(instance, altarica_Skip)

@given(instance=altarica_Transition_strategy)
@settings(max_examples=50)
def test_altarica_transition_instantiation(instance):
    assert isinstance(instance, altarica_Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=altarica_Event_strategy)
@settings(max_examples=50)
def test_altarica_event_instantiation(instance):
    assert isinstance(instance, altarica_Event)

@given(instance=altarica_Node_strategy)
@settings(max_examples=50)
def test_altarica_node_instantiation(instance):
    assert isinstance(instance, altarica_Node)

@given(instance=altarica_Parameter_strategy)
@settings(max_examples=50)
def test_altarica_parameter_instantiation(instance):
    assert isinstance(instance, altarica_Parameter)

@given(instance=altarica_Attribute_strategy)
@settings(max_examples=50)
def test_altarica_attribute_instantiation(instance):
    assert isinstance(instance, altarica_Attribute)

@given(instance=altarica_SymbolicConstant_strategy)
@settings(max_examples=50)
def test_altarica_symbolicconstant_instantiation(instance):
    assert isinstance(instance, altarica_SymbolicConstant)

@given(instance=altarica_Observer_strategy)
@settings(max_examples=50)
def test_altarica_observer_instantiation(instance):
    assert isinstance(instance, altarica_Observer)

@given(instance=altarica_Variable_strategy)
@settings(max_examples=50)
def test_altarica_variable_instantiation(instance):
    assert isinstance(instance, altarica_Variable)

@given(instance=altarica_Domain_strategy)
@settings(max_examples=50)
def test_altarica_domain_instantiation(instance):
    assert isinstance(instance, altarica_Domain)

@given(instance=AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, AbstractDeclaration)

@given(instance=altarica_AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_altarica_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, altarica_AbstractDeclaration)

@given(instance=altarica_Error_strategy)
@settings(max_examples=50)
def test_altarica_error_instantiation(instance):
    assert isinstance(instance, altarica_Error)



@given(instance=altarica_Error_strategy)
def test_altarica_error_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=altarica_Error_strategy)
def test_altarica_error_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=altarica_Model_strategy)
@settings(max_examples=50)
def test_altarica_model_instantiation(instance):
    assert isinstance(instance, altarica_Model)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=altarica_Equal_strategy)
@settings(max_examples=50)
def test_altarica_equal_instantiation(instance):
    assert isinstance(instance, altarica_Equal)



@given(instance=altarica_Equal_strategy)
def test_altarica_equal_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica_ARString_strategy)
@settings(max_examples=50)
def test_altarica_arstring_instantiation(instance):
    assert isinstance(instance, altarica_ARString)



@given(instance=altarica_ARString_strategy)
def test_altarica_arstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica_ARNumber_strategy)
@settings(max_examples=50)
def test_altarica_arnumber_instantiation(instance):
    assert isinstance(instance, altarica_ARNumber)



@given(instance=altarica_ARNumber_strategy)
def test_altarica_arnumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica_LogicalAnd_strategy)
@settings(max_examples=50)
def test_altarica_logicaland_instantiation(instance):
    assert isinstance(instance, altarica_LogicalAnd)



@given(instance=altarica_LogicalAnd_strategy)
def test_altarica_logicaland_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica_SwitchExpression_strategy)
@settings(max_examples=50)
def test_altarica_switchexpression_instantiation(instance):
    assert isinstance(instance, altarica_SwitchExpression)

@given(instance=altarica_FunctionCall_strategy)
@settings(max_examples=50)
def test_altarica_functioncall_instantiation(instance):
    assert isinstance(instance, altarica_FunctionCall)



@given(instance=altarica_FunctionCall_strategy)
def test_altarica_functioncall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_Addition_strategy)
@settings(max_examples=50)
def test_altarica_addition_instantiation(instance):
    assert isinstance(instance, altarica_Addition)



@given(instance=altarica_Addition_strategy)
def test_altarica_addition_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica_LogicalOr_strategy)
@settings(max_examples=50)
def test_altarica_logicalor_instantiation(instance):
    assert isinstance(instance, altarica_LogicalOr)



@given(instance=altarica_LogicalOr_strategy)
def test_altarica_logicalor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica_Minus_strategy)
@settings(max_examples=50)
def test_altarica_minus_instantiation(instance):
    assert isinstance(instance, altarica_Minus)

@given(instance=altarica_Multiplication_strategy)
@settings(max_examples=50)
def test_altarica_multiplication_instantiation(instance):
    assert isinstance(instance, altarica_Multiplication)



@given(instance=altarica_Multiplication_strategy)
def test_altarica_multiplication_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=altarica_Not_strategy)
@settings(max_examples=50)
def test_altarica_not_instantiation(instance):
    assert isinstance(instance, altarica_Not)

@given(instance=altarica_ARBoolean_strategy)
@settings(max_examples=50)
def test_altarica_arboolean_instantiation(instance):
    assert isinstance(instance, altarica_ARBoolean)



@given(instance=altarica_ARBoolean_strategy)
def test_altarica_arboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica_Expression_strategy)
@settings(max_examples=50)
def test_altarica_expression_instantiation(instance):
    assert isinstance(instance, altarica_Expression)

@given(instance=altarica_EObject_strategy)
@settings(max_examples=50)
def test_altarica_eobject_instantiation(instance):
    assert isinstance(instance, altarica_EObject)

@given(instance=altarica_CaseExpression_strategy)
@settings(max_examples=50)
def test_altarica_caseexpression_instantiation(instance):
    assert isinstance(instance, altarica_CaseExpression)

@given(instance=altarica_Instruction_strategy)
@settings(max_examples=50)
def test_altarica_instruction_instantiation(instance):
    assert isinstance(instance, altarica_Instruction)

@given(instance=altarica_TransitionExpression_strategy)
@settings(max_examples=50)
def test_altarica_transitionexpression_instantiation(instance):
    assert isinstance(instance, altarica_TransitionExpression)

@given(instance=altarica_NameRef_strategy)
@settings(max_examples=50)
def test_altarica_nameref_instantiation(instance):
    assert isinstance(instance, altarica_NameRef)

@given(instance=altarica_LabeledTransition_strategy)
@settings(max_examples=50)
def test_altarica_labeledtransition_instantiation(instance):
    assert isinstance(instance, altarica_LabeledTransition)

@given(instance=altarica_Declaration_strategy)
@settings(max_examples=50)
def test_altarica_declaration_instantiation(instance):
    assert isinstance(instance, altarica_Declaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=altarica_NamedType_strategy)
@settings(max_examples=50)
def test_altarica_namedtype_instantiation(instance):
    assert isinstance(instance, altarica_NamedType)

@given(instance=altarica_BaseType_strategy)
@settings(max_examples=50)
def test_altarica_basetype_instantiation(instance):
    assert isinstance(instance, altarica_BaseType)



@given(instance=altarica_BaseType_strategy)
def test_altarica_basetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_Type_strategy)
@settings(max_examples=50)
def test_altarica_type_instantiation(instance):
    assert isinstance(instance, altarica_Type)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=altarica_NamedElement_strategy)
@settings(max_examples=50)
def test_altarica_namedelement_instantiation(instance):
    assert isinstance(instance, altarica_NamedElement)



@given(instance=altarica_NamedElement_strategy)
def test_altarica_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
