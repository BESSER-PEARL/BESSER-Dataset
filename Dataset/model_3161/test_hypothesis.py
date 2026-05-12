import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VariableRef,
    altarica_NestedQualifiedVariableRef,
    EventRef,
    altarica_NestedQualifiedEventRef,
    Expression,
    altarica_StrictUpper,
    altarica_Imply,
    altarica_Division,
    altarica_EBoolean,
    altarica_StrictLower,
    altarica_Addition,
    altarica_Lower,
    altarica_Multiplication,
    altarica_Minus,
    altarica_EInteger,
    altarica_Equal,
    altarica_NotEqual,
    altarica_Upper,
    altarica_EString,
    altarica_VariableRef,
    altarica_NavigableVariable,
    altarica_Or,
    altarica_And,
    altarica_CaseExpression,
    AbstractBooleanExpression,
    AbstractExpression,
    altarica_Switch,
    altarica_Transition,
    altarica_EventRef,
    altarica_Cardinality,
    altarica_VectorParameter,
    altarica_Vector,
    altarica_EObject,
    altarica_IfThenElse,
    altarica_NodeInstanceDeclaration,
    altarica_StateDeclaration,
    altarica_AbstractExpression,
    altarica_Priority,
    NavigableVariable,
    altarica_NonNavigableVariable,
    altarica_Event,
    altarica_EventDeclaration,
    altarica_AbstractTypeRef,
    altarica_AbstractBooleanExpression,
    altarica_Assert,
    altarica_NodeInstance,
    altarica_Affectation,
    altarica_InitStatement,
    AbstractSpecification,
    altarica_AssertSpecification,
    altarica_StateSpecification,
    altarica_NodeInstanceSpecification,
    altarica_TransitionSpecification,
    altarica_VectorSpecification,
    altarica_EventSpecification,
    altarica_InitSpecification,
    altarica_VariableAttribute,
    altarica_AbstractSpecification,
    AbstractDomain,
    altarica_PrimitiveType,
    altarica_Enumeration,
    altarica_Range,
    AbstractTypeRef,
    altarica_DomainRef,
    altarica_AbstractDomain,
    AbstractDefinitionConstant,
    altarica_DomainConstant,
    altarica_ExpressionConstant,
    altarica_Expression,
    altarica_FlowDeclaration,
    altarica_FlowSpecification,
    altarica_ExternalDirective,
    altarica_ExternalSpecification,
    altarica_System,
    NonNavigableVariable,
    altarica_Literal,
    altarica_State,
    altarica_Flow,
    altarica_AbstractDefinitionConstant,
    altarica_Constant,
    AbstractDeclaration,
    altarica_Node,
    altarica_Domain,
    altarica_ConstantDefinition,
    altarica_AbstractDeclaration,
    PrimitiveTypeKind,
    FlowKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variableref_is_not_abstract():
    assert not inspect.isabstract(VariableRef)


def test_variableref_constructor_exists():
    assert callable(VariableRef.__init__)


def test_variableref_constructor_args():
    sig = inspect.signature(VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nestedqualifiedvariableref_is_not_abstract():
    assert not inspect.isabstract(altarica_NestedQualifiedVariableRef)


def test_altarica_nestedqualifiedvariableref_constructor_exists():
    assert callable(altarica_NestedQualifiedVariableRef.__init__)


def test_altarica_nestedqualifiedvariableref_constructor_args():
    sig = inspect.signature(altarica_NestedQualifiedVariableRef.__init__)
    params = list(sig.parameters.keys())



def test_eventref_is_not_abstract():
    assert not inspect.isabstract(EventRef)


def test_eventref_constructor_exists():
    assert callable(EventRef.__init__)


def test_eventref_constructor_args():
    sig = inspect.signature(EventRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nestedqualifiedeventref_is_not_abstract():
    assert not inspect.isabstract(altarica_NestedQualifiedEventRef)


def test_altarica_nestedqualifiedeventref_constructor_exists():
    assert callable(altarica_NestedQualifiedEventRef.__init__)


def test_altarica_nestedqualifiedeventref_constructor_args():
    sig = inspect.signature(altarica_NestedQualifiedEventRef.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_strictupper_is_not_abstract():
    assert not inspect.isabstract(altarica_StrictUpper)


def test_altarica_strictupper_constructor_exists():
    assert callable(altarica_StrictUpper.__init__)


def test_altarica_strictupper_constructor_args():
    sig = inspect.signature(altarica_StrictUpper.__init__)
    params = list(sig.parameters.keys())



def test_altarica_imply_is_not_abstract():
    assert not inspect.isabstract(altarica_Imply)


def test_altarica_imply_constructor_exists():
    assert callable(altarica_Imply.__init__)


def test_altarica_imply_constructor_args():
    sig = inspect.signature(altarica_Imply.__init__)
    params = list(sig.parameters.keys())



def test_altarica_division_is_not_abstract():
    assert not inspect.isabstract(altarica_Division)


def test_altarica_division_constructor_exists():
    assert callable(altarica_Division.__init__)


def test_altarica_division_constructor_args():
    sig = inspect.signature(altarica_Division.__init__)
    params = list(sig.parameters.keys())



def test_altarica_eboolean_is_not_abstract():
    assert not inspect.isabstract(altarica_EBoolean)


def test_altarica_eboolean_constructor_exists():
    assert callable(altarica_EBoolean.__init__)


def test_altarica_eboolean_constructor_args():
    sig = inspect.signature(altarica_EBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica_eboolean_has_value():
    assert hasattr(altarica_EBoolean, "value")
    descriptor = None
    for klass in altarica_EBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica_strictlower_is_not_abstract():
    assert not inspect.isabstract(altarica_StrictLower)


def test_altarica_strictlower_constructor_exists():
    assert callable(altarica_StrictLower.__init__)


def test_altarica_strictlower_constructor_args():
    sig = inspect.signature(altarica_StrictLower.__init__)
    params = list(sig.parameters.keys())



def test_altarica_addition_is_not_abstract():
    assert not inspect.isabstract(altarica_Addition)


def test_altarica_addition_constructor_exists():
    assert callable(altarica_Addition.__init__)


def test_altarica_addition_constructor_args():
    sig = inspect.signature(altarica_Addition.__init__)
    params = list(sig.parameters.keys())



def test_altarica_lower_is_not_abstract():
    assert not inspect.isabstract(altarica_Lower)


def test_altarica_lower_constructor_exists():
    assert callable(altarica_Lower.__init__)


def test_altarica_lower_constructor_args():
    sig = inspect.signature(altarica_Lower.__init__)
    params = list(sig.parameters.keys())



def test_altarica_multiplication_is_not_abstract():
    assert not inspect.isabstract(altarica_Multiplication)


def test_altarica_multiplication_constructor_exists():
    assert callable(altarica_Multiplication.__init__)


def test_altarica_multiplication_constructor_args():
    sig = inspect.signature(altarica_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_altarica_minus_is_not_abstract():
    assert not inspect.isabstract(altarica_Minus)


def test_altarica_minus_constructor_exists():
    assert callable(altarica_Minus.__init__)


def test_altarica_minus_constructor_args():
    sig = inspect.signature(altarica_Minus.__init__)
    params = list(sig.parameters.keys())



def test_altarica_einteger_is_not_abstract():
    assert not inspect.isabstract(altarica_EInteger)


def test_altarica_einteger_constructor_exists():
    assert callable(altarica_EInteger.__init__)


def test_altarica_einteger_constructor_args():
    sig = inspect.signature(altarica_EInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica_einteger_has_value():
    assert hasattr(altarica_EInteger, "value")
    descriptor = None
    for klass in altarica_EInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica_equal_is_not_abstract():
    assert not inspect.isabstract(altarica_Equal)


def test_altarica_equal_constructor_exists():
    assert callable(altarica_Equal.__init__)


def test_altarica_equal_constructor_args():
    sig = inspect.signature(altarica_Equal.__init__)
    params = list(sig.parameters.keys())



def test_altarica_notequal_is_not_abstract():
    assert not inspect.isabstract(altarica_NotEqual)


def test_altarica_notequal_constructor_exists():
    assert callable(altarica_NotEqual.__init__)


def test_altarica_notequal_constructor_args():
    sig = inspect.signature(altarica_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_altarica_upper_is_not_abstract():
    assert not inspect.isabstract(altarica_Upper)


def test_altarica_upper_constructor_exists():
    assert callable(altarica_Upper.__init__)


def test_altarica_upper_constructor_args():
    sig = inspect.signature(altarica_Upper.__init__)
    params = list(sig.parameters.keys())



def test_altarica_estring_is_not_abstract():
    assert not inspect.isabstract(altarica_EString)


def test_altarica_estring_constructor_exists():
    assert callable(altarica_EString.__init__)


def test_altarica_estring_constructor_args():
    sig = inspect.signature(altarica_EString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica_estring_has_value():
    assert hasattr(altarica_EString, "value")
    descriptor = None
    for klass in altarica_EString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica_variableref_is_not_abstract():
    assert not inspect.isabstract(altarica_VariableRef)


def test_altarica_variableref_constructor_exists():
    assert callable(altarica_VariableRef.__init__)


def test_altarica_variableref_constructor_args():
    sig = inspect.signature(altarica_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_navigablevariable_is_not_abstract():
    assert not inspect.isabstract(altarica_NavigableVariable)


def test_altarica_navigablevariable_constructor_exists():
    assert callable(altarica_NavigableVariable.__init__)


def test_altarica_navigablevariable_constructor_args():
    sig = inspect.signature(altarica_NavigableVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_navigablevariable_has_name():
    assert hasattr(altarica_NavigableVariable, "name")
    descriptor = None
    for klass in altarica_NavigableVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_or_is_not_abstract():
    assert not inspect.isabstract(altarica_Or)


def test_altarica_or_constructor_exists():
    assert callable(altarica_Or.__init__)


def test_altarica_or_constructor_args():
    sig = inspect.signature(altarica_Or.__init__)
    params = list(sig.parameters.keys())



def test_altarica_and_is_not_abstract():
    assert not inspect.isabstract(altarica_And)


def test_altarica_and_constructor_exists():
    assert callable(altarica_And.__init__)


def test_altarica_and_constructor_args():
    sig = inspect.signature(altarica_And.__init__)
    params = list(sig.parameters.keys())



def test_altarica_caseexpression_is_not_abstract():
    assert not inspect.isabstract(altarica_CaseExpression)


def test_altarica_caseexpression_constructor_exists():
    assert callable(altarica_CaseExpression.__init__)


def test_altarica_caseexpression_constructor_args():
    sig = inspect.signature(altarica_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractBooleanExpression)


def test_abstractbooleanexpression_constructor_exists():
    assert callable(AbstractBooleanExpression.__init__)


def test_abstractbooleanexpression_constructor_args():
    sig = inspect.signature(AbstractBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractExpression)


def test_abstractexpression_constructor_exists():
    assert callable(AbstractExpression.__init__)


def test_abstractexpression_constructor_args():
    sig = inspect.signature(AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_switch_is_not_abstract():
    assert not inspect.isabstract(altarica_Switch)


def test_altarica_switch_constructor_exists():
    assert callable(altarica_Switch.__init__)


def test_altarica_switch_constructor_args():
    sig = inspect.signature(altarica_Switch.__init__)
    params = list(sig.parameters.keys())



def test_altarica_transition_is_not_abstract():
    assert not inspect.isabstract(altarica_Transition)


def test_altarica_transition_constructor_exists():
    assert callable(altarica_Transition.__init__)


def test_altarica_transition_constructor_args():
    sig = inspect.signature(altarica_Transition.__init__)
    params = list(sig.parameters.keys())



def test_altarica_eventref_is_not_abstract():
    assert not inspect.isabstract(altarica_EventRef)


def test_altarica_eventref_constructor_exists():
    assert callable(altarica_EventRef.__init__)


def test_altarica_eventref_constructor_args():
    sig = inspect.signature(altarica_EventRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_cardinality_is_not_abstract():
    assert not inspect.isabstract(altarica_Cardinality)


def test_altarica_cardinality_constructor_exists():
    assert callable(altarica_Cardinality.__init__)


def test_altarica_cardinality_constructor_args():
    sig = inspect.signature(altarica_Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_altarica_vectorparameter_is_not_abstract():
    assert not inspect.isabstract(altarica_VectorParameter)


def test_altarica_vectorparameter_constructor_exists():
    assert callable(altarica_VectorParameter.__init__)


def test_altarica_vectorparameter_constructor_args():
    sig = inspect.signature(altarica_VectorParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_altarica_vectorparameter_has_isRequired():
    assert hasattr(altarica_VectorParameter, "isRequired")
    descriptor = None
    for klass in altarica_VectorParameter.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_altarica_vector_is_not_abstract():
    assert not inspect.isabstract(altarica_Vector)


def test_altarica_vector_constructor_exists():
    assert callable(altarica_Vector.__init__)


def test_altarica_vector_constructor_args():
    sig = inspect.signature(altarica_Vector.__init__)
    params = list(sig.parameters.keys())



def test_altarica_eobject_is_not_abstract():
    assert not inspect.isabstract(altarica_EObject)


def test_altarica_eobject_constructor_exists():
    assert callable(altarica_EObject.__init__)


def test_altarica_eobject_constructor_args():
    sig = inspect.signature(altarica_EObject.__init__)
    params = list(sig.parameters.keys())



def test_altarica_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(altarica_IfThenElse)


def test_altarica_ifthenelse_constructor_exists():
    assert callable(altarica_IfThenElse.__init__)


def test_altarica_ifthenelse_constructor_args():
    sig = inspect.signature(altarica_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nodeinstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica_NodeInstanceDeclaration)


def test_altarica_nodeinstancedeclaration_constructor_exists():
    assert callable(altarica_NodeInstanceDeclaration.__init__)


def test_altarica_nodeinstancedeclaration_constructor_args():
    sig = inspect.signature(altarica_NodeInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_statedeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica_StateDeclaration)


def test_altarica_statedeclaration_constructor_exists():
    assert callable(altarica_StateDeclaration.__init__)


def test_altarica_statedeclaration_constructor_args():
    sig = inspect.signature(altarica_StateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractExpression)


def test_altarica_abstractexpression_constructor_exists():
    assert callable(altarica_AbstractExpression.__init__)


def test_altarica_abstractexpression_constructor_args():
    sig = inspect.signature(altarica_AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_priority_is_not_abstract():
    assert not inspect.isabstract(altarica_Priority)


def test_altarica_priority_constructor_exists():
    assert callable(altarica_Priority.__init__)


def test_altarica_priority_constructor_args():
    sig = inspect.signature(altarica_Priority.__init__)
    params = list(sig.parameters.keys())



def test_navigablevariable_is_not_abstract():
    assert not inspect.isabstract(NavigableVariable)


def test_navigablevariable_constructor_exists():
    assert callable(NavigableVariable.__init__)


def test_navigablevariable_constructor_args():
    sig = inspect.signature(NavigableVariable.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nonnavigablevariable_is_not_abstract():
    assert not inspect.isabstract(altarica_NonNavigableVariable)


def test_altarica_nonnavigablevariable_constructor_exists():
    assert callable(altarica_NonNavigableVariable.__init__)


def test_altarica_nonnavigablevariable_constructor_args():
    sig = inspect.signature(altarica_NonNavigableVariable.__init__)
    params = list(sig.parameters.keys())



def test_altarica_event_is_not_abstract():
    assert not inspect.isabstract(altarica_Event)


def test_altarica_event_constructor_exists():
    assert callable(altarica_Event.__init__)


def test_altarica_event_constructor_args():
    sig = inspect.signature(altarica_Event.__init__)
    params = list(sig.parameters.keys())



def test_altarica_eventdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica_EventDeclaration)


def test_altarica_eventdeclaration_constructor_exists():
    assert callable(altarica_EventDeclaration.__init__)


def test_altarica_eventdeclaration_constructor_args():
    sig = inspect.signature(altarica_EventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstracttyperef_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractTypeRef)


def test_altarica_abstracttyperef_constructor_exists():
    assert callable(altarica_AbstractTypeRef.__init__)


def test_altarica_abstracttyperef_constructor_args():
    sig = inspect.signature(altarica_AbstractTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstractbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractBooleanExpression)


def test_altarica_abstractbooleanexpression_constructor_exists():
    assert callable(altarica_AbstractBooleanExpression.__init__)


def test_altarica_abstractbooleanexpression_constructor_args():
    sig = inspect.signature(altarica_AbstractBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_assert_is_not_abstract():
    assert not inspect.isabstract(altarica_Assert)


def test_altarica_assert_constructor_exists():
    assert callable(altarica_Assert.__init__)


def test_altarica_assert_constructor_args():
    sig = inspect.signature(altarica_Assert.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(altarica_NodeInstance)


def test_altarica_nodeinstance_constructor_exists():
    assert callable(altarica_NodeInstance.__init__)


def test_altarica_nodeinstance_constructor_args():
    sig = inspect.signature(altarica_NodeInstance.__init__)
    params = list(sig.parameters.keys())



def test_altarica_affectation_is_not_abstract():
    assert not inspect.isabstract(altarica_Affectation)


def test_altarica_affectation_constructor_exists():
    assert callable(altarica_Affectation.__init__)


def test_altarica_affectation_constructor_args():
    sig = inspect.signature(altarica_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_altarica_initstatement_is_not_abstract():
    assert not inspect.isabstract(altarica_InitStatement)


def test_altarica_initstatement_constructor_exists():
    assert callable(altarica_InitStatement.__init__)


def test_altarica_initstatement_constructor_args():
    sig = inspect.signature(altarica_InitStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractspecification_is_not_abstract():
    assert not inspect.isabstract(AbstractSpecification)


def test_abstractspecification_constructor_exists():
    assert callable(AbstractSpecification.__init__)


def test_abstractspecification_constructor_args():
    sig = inspect.signature(AbstractSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_assertspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_AssertSpecification)


def test_altarica_assertspecification_constructor_exists():
    assert callable(altarica_AssertSpecification.__init__)


def test_altarica_assertspecification_constructor_args():
    sig = inspect.signature(altarica_AssertSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_statespecification_is_not_abstract():
    assert not inspect.isabstract(altarica_StateSpecification)


def test_altarica_statespecification_constructor_exists():
    assert callable(altarica_StateSpecification.__init__)


def test_altarica_statespecification_constructor_args():
    sig = inspect.signature(altarica_StateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_nodeinstancespecification_is_not_abstract():
    assert not inspect.isabstract(altarica_NodeInstanceSpecification)


def test_altarica_nodeinstancespecification_constructor_exists():
    assert callable(altarica_NodeInstanceSpecification.__init__)


def test_altarica_nodeinstancespecification_constructor_args():
    sig = inspect.signature(altarica_NodeInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_transitionspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_TransitionSpecification)


def test_altarica_transitionspecification_constructor_exists():
    assert callable(altarica_TransitionSpecification.__init__)


def test_altarica_transitionspecification_constructor_args():
    sig = inspect.signature(altarica_TransitionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_vectorspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_VectorSpecification)


def test_altarica_vectorspecification_constructor_exists():
    assert callable(altarica_VectorSpecification.__init__)


def test_altarica_vectorspecification_constructor_args():
    sig = inspect.signature(altarica_VectorSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_eventspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_EventSpecification)


def test_altarica_eventspecification_constructor_exists():
    assert callable(altarica_EventSpecification.__init__)


def test_altarica_eventspecification_constructor_args():
    sig = inspect.signature(altarica_EventSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_initspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_InitSpecification)


def test_altarica_initspecification_constructor_exists():
    assert callable(altarica_InitSpecification.__init__)


def test_altarica_initspecification_constructor_args():
    sig = inspect.signature(altarica_InitSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_variableattribute_is_not_abstract():
    assert not inspect.isabstract(altarica_VariableAttribute)


def test_altarica_variableattribute_constructor_exists():
    assert callable(altarica_VariableAttribute.__init__)


def test_altarica_variableattribute_constructor_args():
    sig = inspect.signature(altarica_VariableAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_variableattribute_has_name():
    assert hasattr(altarica_VariableAttribute, "name")
    descriptor = None
    for klass in altarica_VariableAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_abstractspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractSpecification)


def test_altarica_abstractspecification_constructor_exists():
    assert callable(altarica_AbstractSpecification.__init__)


def test_altarica_abstractspecification_constructor_args():
    sig = inspect.signature(altarica_AbstractSpecification.__init__)
    params = list(sig.parameters.keys())



def test_abstractdomain_is_not_abstract():
    assert not inspect.isabstract(AbstractDomain)


def test_abstractdomain_constructor_exists():
    assert callable(AbstractDomain.__init__)


def test_abstractdomain_constructor_args():
    sig = inspect.signature(AbstractDomain.__init__)
    params = list(sig.parameters.keys())



def test_altarica_primitivetype_is_not_abstract():
    assert not inspect.isabstract(altarica_PrimitiveType)


def test_altarica_primitivetype_constructor_exists():
    assert callable(altarica_PrimitiveType.__init__)


def test_altarica_primitivetype_constructor_args():
    sig = inspect.signature(altarica_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_primitivetype_has_name():
    assert hasattr(altarica_PrimitiveType, "name")
    descriptor = None
    for klass in altarica_PrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_enumeration_is_not_abstract():
    assert not inspect.isabstract(altarica_Enumeration)


def test_altarica_enumeration_constructor_exists():
    assert callable(altarica_Enumeration.__init__)


def test_altarica_enumeration_constructor_args():
    sig = inspect.signature(altarica_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_range_is_not_abstract():
    assert not inspect.isabstract(altarica_Range)


def test_altarica_range_constructor_exists():
    assert callable(altarica_Range.__init__)


def test_altarica_range_constructor_args():
    sig = inspect.signature(altarica_Range.__init__)
    params = list(sig.parameters.keys())



def test_abstracttyperef_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeRef)


def test_abstracttyperef_constructor_exists():
    assert callable(AbstractTypeRef.__init__)


def test_abstracttyperef_constructor_args():
    sig = inspect.signature(AbstractTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_domainref_is_not_abstract():
    assert not inspect.isabstract(altarica_DomainRef)


def test_altarica_domainref_constructor_exists():
    assert callable(altarica_DomainRef.__init__)


def test_altarica_domainref_constructor_args():
    sig = inspect.signature(altarica_DomainRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstractdomain_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractDomain)


def test_altarica_abstractdomain_constructor_exists():
    assert callable(altarica_AbstractDomain.__init__)


def test_altarica_abstractdomain_constructor_args():
    sig = inspect.signature(altarica_AbstractDomain.__init__)
    params = list(sig.parameters.keys())



def test_abstractdefinitionconstant_is_not_abstract():
    assert not inspect.isabstract(AbstractDefinitionConstant)


def test_abstractdefinitionconstant_constructor_exists():
    assert callable(AbstractDefinitionConstant.__init__)


def test_abstractdefinitionconstant_constructor_args():
    sig = inspect.signature(AbstractDefinitionConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica_domainconstant_is_not_abstract():
    assert not inspect.isabstract(altarica_DomainConstant)


def test_altarica_domainconstant_constructor_exists():
    assert callable(altarica_DomainConstant.__init__)


def test_altarica_domainconstant_constructor_args():
    sig = inspect.signature(altarica_DomainConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica_expressionconstant_is_not_abstract():
    assert not inspect.isabstract(altarica_ExpressionConstant)


def test_altarica_expressionconstant_constructor_exists():
    assert callable(altarica_ExpressionConstant.__init__)


def test_altarica_expressionconstant_constructor_args():
    sig = inspect.signature(altarica_ExpressionConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica_expression_is_not_abstract():
    assert not inspect.isabstract(altarica_Expression)


def test_altarica_expression_constructor_exists():
    assert callable(altarica_Expression.__init__)


def test_altarica_expression_constructor_args():
    sig = inspect.signature(altarica_Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica_flowdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica_FlowDeclaration)


def test_altarica_flowdeclaration_constructor_exists():
    assert callable(altarica_FlowDeclaration.__init__)


def test_altarica_flowdeclaration_constructor_args():
    sig = inspect.signature(altarica_FlowDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_altarica_flowdeclaration_has_kind():
    assert hasattr(altarica_FlowDeclaration, "kind")
    descriptor = None
    for klass in altarica_FlowDeclaration.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_altarica_flowspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_FlowSpecification)


def test_altarica_flowspecification_constructor_exists():
    assert callable(altarica_FlowSpecification.__init__)


def test_altarica_flowspecification_constructor_args():
    sig = inspect.signature(altarica_FlowSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_externaldirective_is_not_abstract():
    assert not inspect.isabstract(altarica_ExternalDirective)


def test_altarica_externaldirective_constructor_exists():
    assert callable(altarica_ExternalDirective.__init__)


def test_altarica_externaldirective_constructor_args():
    sig = inspect.signature(altarica_ExternalDirective.__init__)
    params = list(sig.parameters.keys())
    assert "directive" in params, "Missing parameter 'directive'"

def test_altarica_externaldirective_has_directive():
    assert hasattr(altarica_ExternalDirective, "directive")
    descriptor = None
    for klass in altarica_ExternalDirective.__mro__:
        if "directive" in klass.__dict__:
            descriptor = klass.__dict__["directive"]
            break
    assert isinstance(descriptor, property)



def test_altarica_externalspecification_is_not_abstract():
    assert not inspect.isabstract(altarica_ExternalSpecification)


def test_altarica_externalspecification_constructor_exists():
    assert callable(altarica_ExternalSpecification.__init__)


def test_altarica_externalspecification_constructor_args():
    sig = inspect.signature(altarica_ExternalSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica_system_is_not_abstract():
    assert not inspect.isabstract(altarica_System)


def test_altarica_system_constructor_exists():
    assert callable(altarica_System.__init__)


def test_altarica_system_constructor_args():
    sig = inspect.signature(altarica_System.__init__)
    params = list(sig.parameters.keys())



def test_nonnavigablevariable_is_not_abstract():
    assert not inspect.isabstract(NonNavigableVariable)


def test_nonnavigablevariable_constructor_exists():
    assert callable(NonNavigableVariable.__init__)


def test_nonnavigablevariable_constructor_args():
    sig = inspect.signature(NonNavigableVariable.__init__)
    params = list(sig.parameters.keys())



def test_altarica_literal_is_not_abstract():
    assert not inspect.isabstract(altarica_Literal)


def test_altarica_literal_constructor_exists():
    assert callable(altarica_Literal.__init__)


def test_altarica_literal_constructor_args():
    sig = inspect.signature(altarica_Literal.__init__)
    params = list(sig.parameters.keys())



def test_altarica_state_is_not_abstract():
    assert not inspect.isabstract(altarica_State)


def test_altarica_state_constructor_exists():
    assert callable(altarica_State.__init__)


def test_altarica_state_constructor_args():
    sig = inspect.signature(altarica_State.__init__)
    params = list(sig.parameters.keys())



def test_altarica_flow_is_not_abstract():
    assert not inspect.isabstract(altarica_Flow)


def test_altarica_flow_constructor_exists():
    assert callable(altarica_Flow.__init__)


def test_altarica_flow_constructor_args():
    sig = inspect.signature(altarica_Flow.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstractdefinitionconstant_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractDefinitionConstant)


def test_altarica_abstractdefinitionconstant_constructor_exists():
    assert callable(altarica_AbstractDefinitionConstant.__init__)


def test_altarica_abstractdefinitionconstant_constructor_args():
    sig = inspect.signature(altarica_AbstractDefinitionConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica_constant_is_not_abstract():
    assert not inspect.isabstract(altarica_Constant)


def test_altarica_constant_constructor_exists():
    assert callable(altarica_Constant.__init__)


def test_altarica_constant_constructor_args():
    sig = inspect.signature(altarica_Constant.__init__)
    params = list(sig.parameters.keys())



def test_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractDeclaration)


def test_abstractdeclaration_constructor_exists():
    assert callable(AbstractDeclaration.__init__)


def test_abstractdeclaration_constructor_args():
    sig = inspect.signature(AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica_node_is_not_abstract():
    assert not inspect.isabstract(altarica_Node)


def test_altarica_node_constructor_exists():
    assert callable(altarica_Node.__init__)


def test_altarica_node_constructor_args():
    sig = inspect.signature(altarica_Node.__init__)
    params = list(sig.parameters.keys())
    assert "isMain" in params, "Missing parameter 'isMain'"
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_node_has_isMain():
    assert hasattr(altarica_Node, "isMain")
    descriptor = None
    for klass in altarica_Node.__mro__:
        if "isMain" in klass.__dict__:
            descriptor = klass.__dict__["isMain"]
            break
    assert isinstance(descriptor, property)

def test_altarica_node_has_name():
    assert hasattr(altarica_Node, "name")
    descriptor = None
    for klass in altarica_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_domain_is_not_abstract():
    assert not inspect.isabstract(altarica_Domain)


def test_altarica_domain_constructor_exists():
    assert callable(altarica_Domain.__init__)


def test_altarica_domain_constructor_args():
    sig = inspect.signature(altarica_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica_domain_has_name():
    assert hasattr(altarica_Domain, "name")
    descriptor = None
    for klass in altarica_Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica_constantdefinition_is_not_abstract():
    assert not inspect.isabstract(altarica_ConstantDefinition)


def test_altarica_constantdefinition_constructor_exists():
    assert callable(altarica_ConstantDefinition.__init__)


def test_altarica_constantdefinition_constructor_args():
    sig = inspect.signature(altarica_ConstantDefinition.__init__)
    params = list(sig.parameters.keys())



def test_altarica_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica_AbstractDeclaration)


def test_altarica_abstractdeclaration_constructor_exists():
    assert callable(altarica_AbstractDeclaration.__init__)


def test_altarica_abstractdeclaration_constructor_args():
    sig = inspect.signature(altarica_AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_primitivetypekind_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypeKind is not None

def test_primitivetypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypeKind]
    expected_literals = [
        "BOOLEAN",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypeKind"

def test_flowkind_exists():
    # Check that the Enumeration exists
    assert FlowKind is not None

def test_flowkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowKind]
    expected_literals = [
        "IN",
        "OUT",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowKind"


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
VariableRef_strategy = st.builds(
    VariableRef,
)
altarica_NestedQualifiedVariableRef_strategy = st.builds(
    altarica_NestedQualifiedVariableRef,
)
EventRef_strategy = st.builds(
    EventRef,
)
altarica_NestedQualifiedEventRef_strategy = st.builds(
    altarica_NestedQualifiedEventRef,
)
Expression_strategy = st.builds(
    Expression,
)
altarica_StrictUpper_strategy = st.builds(
    altarica_StrictUpper,
)
altarica_Imply_strategy = st.builds(
    altarica_Imply,
)
altarica_Division_strategy = st.builds(
    altarica_Division,
)
altarica_EBoolean_strategy = st.builds(
    altarica_EBoolean,
    value=
        safe_text
)
altarica_StrictLower_strategy = st.builds(
    altarica_StrictLower,
)
altarica_Addition_strategy = st.builds(
    altarica_Addition,
)
altarica_Lower_strategy = st.builds(
    altarica_Lower,
)
altarica_Multiplication_strategy = st.builds(
    altarica_Multiplication,
)
altarica_Minus_strategy = st.builds(
    altarica_Minus,
)
altarica_EInteger_strategy = st.builds(
    altarica_EInteger,
    value=
        st.integers()
)
altarica_Equal_strategy = st.builds(
    altarica_Equal,
)
altarica_NotEqual_strategy = st.builds(
    altarica_NotEqual,
)
altarica_Upper_strategy = st.builds(
    altarica_Upper,
)
altarica_EString_strategy = st.builds(
    altarica_EString,
    value=
        safe_text
)
altarica_VariableRef_strategy = st.builds(
    altarica_VariableRef,
)
altarica_NavigableVariable_strategy = st.builds(
    altarica_NavigableVariable,
    name=
        safe_text
)
altarica_Or_strategy = st.builds(
    altarica_Or,
)
altarica_And_strategy = st.builds(
    altarica_And,
)
altarica_CaseExpression_strategy = st.builds(
    altarica_CaseExpression,
)
AbstractBooleanExpression_strategy = st.builds(
    AbstractBooleanExpression,
)
AbstractExpression_strategy = st.builds(
    AbstractExpression,
)
altarica_Switch_strategy = st.builds(
    altarica_Switch,
)
altarica_Transition_strategy = st.builds(
    altarica_Transition,
)
altarica_EventRef_strategy = st.builds(
    altarica_EventRef,
)
altarica_Cardinality_strategy = st.builds(
    altarica_Cardinality,
)
altarica_VectorParameter_strategy = st.builds(
    altarica_VectorParameter,
    isRequired=
        st.booleans()
)
altarica_Vector_strategy = st.builds(
    altarica_Vector,
)
altarica_EObject_strategy = st.builds(
    altarica_EObject,
)
altarica_IfThenElse_strategy = st.builds(
    altarica_IfThenElse,
)
altarica_NodeInstanceDeclaration_strategy = st.builds(
    altarica_NodeInstanceDeclaration,
)
altarica_StateDeclaration_strategy = st.builds(
    altarica_StateDeclaration,
)
altarica_AbstractExpression_strategy = st.builds(
    altarica_AbstractExpression,
)
altarica_Priority_strategy = st.builds(
    altarica_Priority,
)
NavigableVariable_strategy = st.builds(
    NavigableVariable,
)
altarica_NonNavigableVariable_strategy = st.builds(
    altarica_NonNavigableVariable,
)
altarica_Event_strategy = st.builds(
    altarica_Event,
)
altarica_EventDeclaration_strategy = st.builds(
    altarica_EventDeclaration,
)
altarica_AbstractTypeRef_strategy = st.builds(
    altarica_AbstractTypeRef,
)
altarica_AbstractBooleanExpression_strategy = st.builds(
    altarica_AbstractBooleanExpression,
)
altarica_Assert_strategy = st.builds(
    altarica_Assert,
)
altarica_NodeInstance_strategy = st.builds(
    altarica_NodeInstance,
)
altarica_Affectation_strategy = st.builds(
    altarica_Affectation,
)
altarica_InitStatement_strategy = st.builds(
    altarica_InitStatement,
)
AbstractSpecification_strategy = st.builds(
    AbstractSpecification,
)
altarica_AssertSpecification_strategy = st.builds(
    altarica_AssertSpecification,
)
altarica_StateSpecification_strategy = st.builds(
    altarica_StateSpecification,
)
altarica_NodeInstanceSpecification_strategy = st.builds(
    altarica_NodeInstanceSpecification,
)
altarica_TransitionSpecification_strategy = st.builds(
    altarica_TransitionSpecification,
)
altarica_VectorSpecification_strategy = st.builds(
    altarica_VectorSpecification,
)
altarica_EventSpecification_strategy = st.builds(
    altarica_EventSpecification,
)
altarica_InitSpecification_strategy = st.builds(
    altarica_InitSpecification,
)
altarica_VariableAttribute_strategy = st.builds(
    altarica_VariableAttribute,
    name=
        safe_text
)
altarica_AbstractSpecification_strategy = st.builds(
    altarica_AbstractSpecification,
)
AbstractDomain_strategy = st.builds(
    AbstractDomain,
)
altarica_PrimitiveType_strategy = st.builds(
    altarica_PrimitiveType,
    name=
        safe_text
)
altarica_Enumeration_strategy = st.builds(
    altarica_Enumeration,
)
altarica_Range_strategy = st.builds(
    altarica_Range,
)
AbstractTypeRef_strategy = st.builds(
    AbstractTypeRef,
)
altarica_DomainRef_strategy = st.builds(
    altarica_DomainRef,
)
altarica_AbstractDomain_strategy = st.builds(
    altarica_AbstractDomain,
)
AbstractDefinitionConstant_strategy = st.builds(
    AbstractDefinitionConstant,
)
altarica_DomainConstant_strategy = st.builds(
    altarica_DomainConstant,
)
altarica_ExpressionConstant_strategy = st.builds(
    altarica_ExpressionConstant,
)
altarica_Expression_strategy = st.builds(
    altarica_Expression,
)
altarica_FlowDeclaration_strategy = st.builds(
    altarica_FlowDeclaration,
    kind=
        safe_text
)
altarica_FlowSpecification_strategy = st.builds(
    altarica_FlowSpecification,
)
altarica_ExternalDirective_strategy = st.builds(
    altarica_ExternalDirective,
    directive=
        safe_text
)
altarica_ExternalSpecification_strategy = st.builds(
    altarica_ExternalSpecification,
)
altarica_System_strategy = st.builds(
    altarica_System,
)
NonNavigableVariable_strategy = st.builds(
    NonNavigableVariable,
)
altarica_Literal_strategy = st.builds(
    altarica_Literal,
)
altarica_State_strategy = st.builds(
    altarica_State,
)
altarica_Flow_strategy = st.builds(
    altarica_Flow,
)
altarica_AbstractDefinitionConstant_strategy = st.builds(
    altarica_AbstractDefinitionConstant,
)
altarica_Constant_strategy = st.builds(
    altarica_Constant,
)
AbstractDeclaration_strategy = st.builds(
    AbstractDeclaration,
)
altarica_Node_strategy = st.builds(
    altarica_Node,
    isMain=
        st.booleans(),
    name=
        safe_text
)
altarica_Domain_strategy = st.builds(
    altarica_Domain,
    name=
        safe_text
)
altarica_ConstantDefinition_strategy = st.builds(
    altarica_ConstantDefinition,
)
altarica_AbstractDeclaration_strategy = st.builds(
    altarica_AbstractDeclaration,
)

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=altarica_NestedQualifiedVariableRef_strategy)
@settings(max_examples=50)
def test_altarica_nestedqualifiedvariableref_instantiation(instance):
    assert isinstance(instance, altarica_NestedQualifiedVariableRef)

@given(instance=EventRef_strategy)
@settings(max_examples=50)
def test_eventref_instantiation(instance):
    assert isinstance(instance, EventRef)

@given(instance=altarica_NestedQualifiedEventRef_strategy)
@settings(max_examples=50)
def test_altarica_nestedqualifiedeventref_instantiation(instance):
    assert isinstance(instance, altarica_NestedQualifiedEventRef)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=altarica_StrictUpper_strategy)
@settings(max_examples=50)
def test_altarica_strictupper_instantiation(instance):
    assert isinstance(instance, altarica_StrictUpper)

@given(instance=altarica_Imply_strategy)
@settings(max_examples=50)
def test_altarica_imply_instantiation(instance):
    assert isinstance(instance, altarica_Imply)

@given(instance=altarica_Division_strategy)
@settings(max_examples=50)
def test_altarica_division_instantiation(instance):
    assert isinstance(instance, altarica_Division)

@given(instance=altarica_EBoolean_strategy)
@settings(max_examples=50)
def test_altarica_eboolean_instantiation(instance):
    assert isinstance(instance, altarica_EBoolean)



@given(instance=altarica_EBoolean_strategy)
def test_altarica_eboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica_StrictLower_strategy)
@settings(max_examples=50)
def test_altarica_strictlower_instantiation(instance):
    assert isinstance(instance, altarica_StrictLower)

@given(instance=altarica_Addition_strategy)
@settings(max_examples=50)
def test_altarica_addition_instantiation(instance):
    assert isinstance(instance, altarica_Addition)

@given(instance=altarica_Lower_strategy)
@settings(max_examples=50)
def test_altarica_lower_instantiation(instance):
    assert isinstance(instance, altarica_Lower)

@given(instance=altarica_Multiplication_strategy)
@settings(max_examples=50)
def test_altarica_multiplication_instantiation(instance):
    assert isinstance(instance, altarica_Multiplication)

@given(instance=altarica_Minus_strategy)
@settings(max_examples=50)
def test_altarica_minus_instantiation(instance):
    assert isinstance(instance, altarica_Minus)

@given(instance=altarica_EInteger_strategy)
@settings(max_examples=50)
def test_altarica_einteger_instantiation(instance):
    assert isinstance(instance, altarica_EInteger)



@given(instance=altarica_EInteger_strategy)
def test_altarica_einteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica_Equal_strategy)
@settings(max_examples=50)
def test_altarica_equal_instantiation(instance):
    assert isinstance(instance, altarica_Equal)

@given(instance=altarica_NotEqual_strategy)
@settings(max_examples=50)
def test_altarica_notequal_instantiation(instance):
    assert isinstance(instance, altarica_NotEqual)

@given(instance=altarica_Upper_strategy)
@settings(max_examples=50)
def test_altarica_upper_instantiation(instance):
    assert isinstance(instance, altarica_Upper)

@given(instance=altarica_EString_strategy)
@settings(max_examples=50)
def test_altarica_estring_instantiation(instance):
    assert isinstance(instance, altarica_EString)



@given(instance=altarica_EString_strategy)
def test_altarica_estring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica_VariableRef_strategy)
@settings(max_examples=50)
def test_altarica_variableref_instantiation(instance):
    assert isinstance(instance, altarica_VariableRef)

@given(instance=altarica_NavigableVariable_strategy)
@settings(max_examples=50)
def test_altarica_navigablevariable_instantiation(instance):
    assert isinstance(instance, altarica_NavigableVariable)



@given(instance=altarica_NavigableVariable_strategy)
def test_altarica_navigablevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_Or_strategy)
@settings(max_examples=50)
def test_altarica_or_instantiation(instance):
    assert isinstance(instance, altarica_Or)

@given(instance=altarica_And_strategy)
@settings(max_examples=50)
def test_altarica_and_instantiation(instance):
    assert isinstance(instance, altarica_And)

@given(instance=altarica_CaseExpression_strategy)
@settings(max_examples=50)
def test_altarica_caseexpression_instantiation(instance):
    assert isinstance(instance, altarica_CaseExpression)

@given(instance=AbstractBooleanExpression_strategy)
@settings(max_examples=50)
def test_abstractbooleanexpression_instantiation(instance):
    assert isinstance(instance, AbstractBooleanExpression)

@given(instance=AbstractExpression_strategy)
@settings(max_examples=50)
def test_abstractexpression_instantiation(instance):
    assert isinstance(instance, AbstractExpression)

@given(instance=altarica_Switch_strategy)
@settings(max_examples=50)
def test_altarica_switch_instantiation(instance):
    assert isinstance(instance, altarica_Switch)

@given(instance=altarica_Transition_strategy)
@settings(max_examples=50)
def test_altarica_transition_instantiation(instance):
    assert isinstance(instance, altarica_Transition)

@given(instance=altarica_EventRef_strategy)
@settings(max_examples=50)
def test_altarica_eventref_instantiation(instance):
    assert isinstance(instance, altarica_EventRef)

@given(instance=altarica_Cardinality_strategy)
@settings(max_examples=50)
def test_altarica_cardinality_instantiation(instance):
    assert isinstance(instance, altarica_Cardinality)

@given(instance=altarica_VectorParameter_strategy)
@settings(max_examples=50)
def test_altarica_vectorparameter_instantiation(instance):
    assert isinstance(instance, altarica_VectorParameter)



@given(instance=altarica_VectorParameter_strategy)
def test_altarica_vectorparameter_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=altarica_Vector_strategy)
@settings(max_examples=50)
def test_altarica_vector_instantiation(instance):
    assert isinstance(instance, altarica_Vector)

@given(instance=altarica_EObject_strategy)
@settings(max_examples=50)
def test_altarica_eobject_instantiation(instance):
    assert isinstance(instance, altarica_EObject)

@given(instance=altarica_IfThenElse_strategy)
@settings(max_examples=50)
def test_altarica_ifthenelse_instantiation(instance):
    assert isinstance(instance, altarica_IfThenElse)

@given(instance=altarica_NodeInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_altarica_nodeinstancedeclaration_instantiation(instance):
    assert isinstance(instance, altarica_NodeInstanceDeclaration)

@given(instance=altarica_StateDeclaration_strategy)
@settings(max_examples=50)
def test_altarica_statedeclaration_instantiation(instance):
    assert isinstance(instance, altarica_StateDeclaration)

@given(instance=altarica_AbstractExpression_strategy)
@settings(max_examples=50)
def test_altarica_abstractexpression_instantiation(instance):
    assert isinstance(instance, altarica_AbstractExpression)

@given(instance=altarica_Priority_strategy)
@settings(max_examples=50)
def test_altarica_priority_instantiation(instance):
    assert isinstance(instance, altarica_Priority)

@given(instance=NavigableVariable_strategy)
@settings(max_examples=50)
def test_navigablevariable_instantiation(instance):
    assert isinstance(instance, NavigableVariable)

@given(instance=altarica_NonNavigableVariable_strategy)
@settings(max_examples=50)
def test_altarica_nonnavigablevariable_instantiation(instance):
    assert isinstance(instance, altarica_NonNavigableVariable)

@given(instance=altarica_Event_strategy)
@settings(max_examples=50)
def test_altarica_event_instantiation(instance):
    assert isinstance(instance, altarica_Event)

@given(instance=altarica_EventDeclaration_strategy)
@settings(max_examples=50)
def test_altarica_eventdeclaration_instantiation(instance):
    assert isinstance(instance, altarica_EventDeclaration)

@given(instance=altarica_AbstractTypeRef_strategy)
@settings(max_examples=50)
def test_altarica_abstracttyperef_instantiation(instance):
    assert isinstance(instance, altarica_AbstractTypeRef)

@given(instance=altarica_AbstractBooleanExpression_strategy)
@settings(max_examples=50)
def test_altarica_abstractbooleanexpression_instantiation(instance):
    assert isinstance(instance, altarica_AbstractBooleanExpression)

@given(instance=altarica_Assert_strategy)
@settings(max_examples=50)
def test_altarica_assert_instantiation(instance):
    assert isinstance(instance, altarica_Assert)

@given(instance=altarica_NodeInstance_strategy)
@settings(max_examples=50)
def test_altarica_nodeinstance_instantiation(instance):
    assert isinstance(instance, altarica_NodeInstance)

@given(instance=altarica_Affectation_strategy)
@settings(max_examples=50)
def test_altarica_affectation_instantiation(instance):
    assert isinstance(instance, altarica_Affectation)

@given(instance=altarica_InitStatement_strategy)
@settings(max_examples=50)
def test_altarica_initstatement_instantiation(instance):
    assert isinstance(instance, altarica_InitStatement)

@given(instance=AbstractSpecification_strategy)
@settings(max_examples=50)
def test_abstractspecification_instantiation(instance):
    assert isinstance(instance, AbstractSpecification)

@given(instance=altarica_AssertSpecification_strategy)
@settings(max_examples=50)
def test_altarica_assertspecification_instantiation(instance):
    assert isinstance(instance, altarica_AssertSpecification)

@given(instance=altarica_StateSpecification_strategy)
@settings(max_examples=50)
def test_altarica_statespecification_instantiation(instance):
    assert isinstance(instance, altarica_StateSpecification)

@given(instance=altarica_NodeInstanceSpecification_strategy)
@settings(max_examples=50)
def test_altarica_nodeinstancespecification_instantiation(instance):
    assert isinstance(instance, altarica_NodeInstanceSpecification)

@given(instance=altarica_TransitionSpecification_strategy)
@settings(max_examples=50)
def test_altarica_transitionspecification_instantiation(instance):
    assert isinstance(instance, altarica_TransitionSpecification)

@given(instance=altarica_VectorSpecification_strategy)
@settings(max_examples=50)
def test_altarica_vectorspecification_instantiation(instance):
    assert isinstance(instance, altarica_VectorSpecification)

@given(instance=altarica_EventSpecification_strategy)
@settings(max_examples=50)
def test_altarica_eventspecification_instantiation(instance):
    assert isinstance(instance, altarica_EventSpecification)

@given(instance=altarica_InitSpecification_strategy)
@settings(max_examples=50)
def test_altarica_initspecification_instantiation(instance):
    assert isinstance(instance, altarica_InitSpecification)

@given(instance=altarica_VariableAttribute_strategy)
@settings(max_examples=50)
def test_altarica_variableattribute_instantiation(instance):
    assert isinstance(instance, altarica_VariableAttribute)



@given(instance=altarica_VariableAttribute_strategy)
def test_altarica_variableattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_AbstractSpecification_strategy)
@settings(max_examples=50)
def test_altarica_abstractspecification_instantiation(instance):
    assert isinstance(instance, altarica_AbstractSpecification)

@given(instance=AbstractDomain_strategy)
@settings(max_examples=50)
def test_abstractdomain_instantiation(instance):
    assert isinstance(instance, AbstractDomain)

@given(instance=altarica_PrimitiveType_strategy)
@settings(max_examples=50)
def test_altarica_primitivetype_instantiation(instance):
    assert isinstance(instance, altarica_PrimitiveType)



@given(instance=altarica_PrimitiveType_strategy)
def test_altarica_primitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_Enumeration_strategy)
@settings(max_examples=50)
def test_altarica_enumeration_instantiation(instance):
    assert isinstance(instance, altarica_Enumeration)

@given(instance=altarica_Range_strategy)
@settings(max_examples=50)
def test_altarica_range_instantiation(instance):
    assert isinstance(instance, altarica_Range)

@given(instance=AbstractTypeRef_strategy)
@settings(max_examples=50)
def test_abstracttyperef_instantiation(instance):
    assert isinstance(instance, AbstractTypeRef)

@given(instance=altarica_DomainRef_strategy)
@settings(max_examples=50)
def test_altarica_domainref_instantiation(instance):
    assert isinstance(instance, altarica_DomainRef)

@given(instance=altarica_AbstractDomain_strategy)
@settings(max_examples=50)
def test_altarica_abstractdomain_instantiation(instance):
    assert isinstance(instance, altarica_AbstractDomain)

@given(instance=AbstractDefinitionConstant_strategy)
@settings(max_examples=50)
def test_abstractdefinitionconstant_instantiation(instance):
    assert isinstance(instance, AbstractDefinitionConstant)

@given(instance=altarica_DomainConstant_strategy)
@settings(max_examples=50)
def test_altarica_domainconstant_instantiation(instance):
    assert isinstance(instance, altarica_DomainConstant)

@given(instance=altarica_ExpressionConstant_strategy)
@settings(max_examples=50)
def test_altarica_expressionconstant_instantiation(instance):
    assert isinstance(instance, altarica_ExpressionConstant)

@given(instance=altarica_Expression_strategy)
@settings(max_examples=50)
def test_altarica_expression_instantiation(instance):
    assert isinstance(instance, altarica_Expression)

@given(instance=altarica_FlowDeclaration_strategy)
@settings(max_examples=50)
def test_altarica_flowdeclaration_instantiation(instance):
    assert isinstance(instance, altarica_FlowDeclaration)



@given(instance=altarica_FlowDeclaration_strategy)
def test_altarica_flowdeclaration_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=altarica_FlowSpecification_strategy)
@settings(max_examples=50)
def test_altarica_flowspecification_instantiation(instance):
    assert isinstance(instance, altarica_FlowSpecification)

@given(instance=altarica_ExternalDirective_strategy)
@settings(max_examples=50)
def test_altarica_externaldirective_instantiation(instance):
    assert isinstance(instance, altarica_ExternalDirective)



@given(instance=altarica_ExternalDirective_strategy)
def test_altarica_externaldirective_directive_setter(instance):
    original = instance.directive
    instance.directive = original
    assert instance.directive == original

@given(instance=altarica_ExternalSpecification_strategy)
@settings(max_examples=50)
def test_altarica_externalspecification_instantiation(instance):
    assert isinstance(instance, altarica_ExternalSpecification)

@given(instance=altarica_System_strategy)
@settings(max_examples=50)
def test_altarica_system_instantiation(instance):
    assert isinstance(instance, altarica_System)

@given(instance=NonNavigableVariable_strategy)
@settings(max_examples=50)
def test_nonnavigablevariable_instantiation(instance):
    assert isinstance(instance, NonNavigableVariable)

@given(instance=altarica_Literal_strategy)
@settings(max_examples=50)
def test_altarica_literal_instantiation(instance):
    assert isinstance(instance, altarica_Literal)

@given(instance=altarica_State_strategy)
@settings(max_examples=50)
def test_altarica_state_instantiation(instance):
    assert isinstance(instance, altarica_State)

@given(instance=altarica_Flow_strategy)
@settings(max_examples=50)
def test_altarica_flow_instantiation(instance):
    assert isinstance(instance, altarica_Flow)

@given(instance=altarica_AbstractDefinitionConstant_strategy)
@settings(max_examples=50)
def test_altarica_abstractdefinitionconstant_instantiation(instance):
    assert isinstance(instance, altarica_AbstractDefinitionConstant)

@given(instance=altarica_Constant_strategy)
@settings(max_examples=50)
def test_altarica_constant_instantiation(instance):
    assert isinstance(instance, altarica_Constant)

@given(instance=AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, AbstractDeclaration)

@given(instance=altarica_Node_strategy)
@settings(max_examples=50)
def test_altarica_node_instantiation(instance):
    assert isinstance(instance, altarica_Node)



@given(instance=altarica_Node_strategy)
def test_altarica_node_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original



@given(instance=altarica_Node_strategy)
def test_altarica_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_Domain_strategy)
@settings(max_examples=50)
def test_altarica_domain_instantiation(instance):
    assert isinstance(instance, altarica_Domain)



@given(instance=altarica_Domain_strategy)
def test_altarica_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica_ConstantDefinition_strategy)
@settings(max_examples=50)
def test_altarica_constantdefinition_instantiation(instance):
    assert isinstance(instance, altarica_ConstantDefinition)

@given(instance=altarica_AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_altarica_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, altarica_AbstractDeclaration)
