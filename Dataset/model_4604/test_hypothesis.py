import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Logic,
    henshin_text_Not,
    henshin_text_ConditionGraphRef,
    henshin_text_AND,
    henshin_text_ORorXOR,
    Expression,
    henshin_text_JavaAttributeValue,
    henshin_text_MulOrDivExpression,
    henshin_text_NotExpression,
    henshin_text_AndExpression,
    henshin_text_PlusExpression,
    henshin_text_MinusExpression,
    henshin_text_IntegerValue,
    henshin_text_EqualityExpression,
    henshin_text_BracketExpression,
    henshin_text_NaturalValue,
    henshin_text_JavaClassValue,
    henshin_text_BoolValue,
    henshin_text_NumberValue,
    henshin_text_ComparisonExpression,
    henshin_text_ParameterValue,
    henshin_text_StringValue,
    henshin_text_OrExpression,
    ModelElement,
    henshin_text_Rule,
    henshin_text_Unit,
    henshin_text_List,
    henshin_text_ParameterType,
    henshin_text_Match,
    henshin_text_ConditionNodeTypes,
    henshin_text_ConditionEdge,
    henshin_text_ConditionGraphElements,
    SequentialProperties,
    henshin_text_Rollback,
    henshin_text_Strict,
    UnitElement,
    henshin_text_IteratedUnit,
    henshin_text_PriorityUnit,
    henshin_text_IndependentUnit,
    henshin_text_ConditionalUnit,
    henshin_text_Call,
    henshin_text_LoopUnit,
    henshin_text_SequentialProperties,
    henshin_text_UnitElement,
    henshin_text_EAttribute,
    henshin_text_Attribute,
    henshin_text_EClass,
    ConditionNodeTypes,
    RuleNodeTypes,
    henshin_text_EReference,
    henshin_text_ConditionGraph,
    henshin_text_Logic,
    ConditionGraphElements,
    henshin_text_ConditionNode,
    henshin_text_ConditionReuseNode,
    henshin_text_ConditionEdges,
    henshin_text_GraphElements,
    henshin_text_Expression,
    RuleElement,
    henshin_text_CheckDangling,
    henshin_text_Conditions,
    henshin_text_InjectiveMatching,
    henshin_text_Graph,
    henshin_text_JavaImport,
    henshin_text_RuleElement,
    henshin_text_Parameter,
    henshin_text_EPackage,
    henshin_text_ModelElement,
    henshin_text_RuleNodeTypes,
    henshin_text_Edge,
    GraphElements,
    henshin_text_MultiRule,
    henshin_text_Node,
    henshin_text_MultiRuleReuseNode,
    henshin_text_Formula,
    henshin_text_Edges,
    henshin_text_EPackageImport,
    henshin_text_Model,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logic_is_not_abstract():
    assert not inspect.isabstract(Logic)


def test_logic_constructor_exists():
    assert callable(Logic.__init__)


def test_logic_constructor_args():
    sig = inspect.signature(Logic.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_not_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Not)


def test_henshin_text_not_constructor_exists():
    assert callable(henshin_text_Not.__init__)


def test_henshin_text_not_constructor_args():
    sig = inspect.signature(henshin_text_Not.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditiongraphref_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionGraphRef)


def test_henshin_text_conditiongraphref_constructor_exists():
    assert callable(henshin_text_ConditionGraphRef.__init__)


def test_henshin_text_conditiongraphref_constructor_args():
    sig = inspect.signature(henshin_text_ConditionGraphRef.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_and_is_not_abstract():
    assert not inspect.isabstract(henshin_text_AND)


def test_henshin_text_and_constructor_exists():
    assert callable(henshin_text_AND.__init__)


def test_henshin_text_and_constructor_args():
    sig = inspect.signature(henshin_text_AND.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_ororxor_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ORorXOR)


def test_henshin_text_ororxor_constructor_exists():
    assert callable(henshin_text_ORorXOR.__init__)


def test_henshin_text_ororxor_constructor_args():
    sig = inspect.signature(henshin_text_ORorXOR.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin_text_ororxor_has_op():
    assert hasattr(henshin_text_ORorXOR, "op")
    descriptor = None
    for klass in henshin_text_ORorXOR.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_javaattributevalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_JavaAttributeValue)


def test_henshin_text_javaattributevalue_constructor_exists():
    assert callable(henshin_text_JavaAttributeValue.__init__)


def test_henshin_text_javaattributevalue_constructor_args():
    sig = inspect.signature(henshin_text_JavaAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_javaattributevalue_has_value():
    assert hasattr(henshin_text_JavaAttributeValue, "value")
    descriptor = None
    for klass in henshin_text_JavaAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_mulordivexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MulOrDivExpression)


def test_henshin_text_mulordivexpression_constructor_exists():
    assert callable(henshin_text_MulOrDivExpression.__init__)


def test_henshin_text_mulordivexpression_constructor_args():
    sig = inspect.signature(henshin_text_MulOrDivExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin_text_mulordivexpression_has_op():
    assert hasattr(henshin_text_MulOrDivExpression, "op")
    descriptor = None
    for klass in henshin_text_MulOrDivExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_notexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_NotExpression)


def test_henshin_text_notexpression_constructor_exists():
    assert callable(henshin_text_NotExpression.__init__)


def test_henshin_text_notexpression_constructor_args():
    sig = inspect.signature(henshin_text_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_andexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_AndExpression)


def test_henshin_text_andexpression_constructor_exists():
    assert callable(henshin_text_AndExpression.__init__)


def test_henshin_text_andexpression_constructor_args():
    sig = inspect.signature(henshin_text_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_plusexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_PlusExpression)


def test_henshin_text_plusexpression_constructor_exists():
    assert callable(henshin_text_PlusExpression.__init__)


def test_henshin_text_plusexpression_constructor_args():
    sig = inspect.signature(henshin_text_PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_minusexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MinusExpression)


def test_henshin_text_minusexpression_constructor_exists():
    assert callable(henshin_text_MinusExpression.__init__)


def test_henshin_text_minusexpression_constructor_args():
    sig = inspect.signature(henshin_text_MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_integervalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_IntegerValue)


def test_henshin_text_integervalue_constructor_exists():
    assert callable(henshin_text_IntegerValue.__init__)


def test_henshin_text_integervalue_constructor_args():
    sig = inspect.signature(henshin_text_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_integervalue_has_value():
    assert hasattr(henshin_text_IntegerValue, "value")
    descriptor = None
    for klass in henshin_text_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EqualityExpression)


def test_henshin_text_equalityexpression_constructor_exists():
    assert callable(henshin_text_EqualityExpression.__init__)


def test_henshin_text_equalityexpression_constructor_args():
    sig = inspect.signature(henshin_text_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin_text_equalityexpression_has_op():
    assert hasattr(henshin_text_EqualityExpression, "op")
    descriptor = None
    for klass in henshin_text_EqualityExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_bracketexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_BracketExpression)


def test_henshin_text_bracketexpression_constructor_exists():
    assert callable(henshin_text_BracketExpression.__init__)


def test_henshin_text_bracketexpression_constructor_args():
    sig = inspect.signature(henshin_text_BracketExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_naturalvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_NaturalValue)


def test_henshin_text_naturalvalue_constructor_exists():
    assert callable(henshin_text_NaturalValue.__init__)


def test_henshin_text_naturalvalue_constructor_args():
    sig = inspect.signature(henshin_text_NaturalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_naturalvalue_has_value():
    assert hasattr(henshin_text_NaturalValue, "value")
    descriptor = None
    for klass in henshin_text_NaturalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_javaclassvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_JavaClassValue)


def test_henshin_text_javaclassvalue_constructor_exists():
    assert callable(henshin_text_JavaClassValue.__init__)


def test_henshin_text_javaclassvalue_constructor_args():
    sig = inspect.signature(henshin_text_JavaClassValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_javaclassvalue_has_value():
    assert hasattr(henshin_text_JavaClassValue, "value")
    descriptor = None
    for klass in henshin_text_JavaClassValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_boolvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_BoolValue)


def test_henshin_text_boolvalue_constructor_exists():
    assert callable(henshin_text_BoolValue.__init__)


def test_henshin_text_boolvalue_constructor_args():
    sig = inspect.signature(henshin_text_BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_boolvalue_has_value():
    assert hasattr(henshin_text_BoolValue, "value")
    descriptor = None
    for klass in henshin_text_BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_numbervalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_NumberValue)


def test_henshin_text_numbervalue_constructor_exists():
    assert callable(henshin_text_NumberValue.__init__)


def test_henshin_text_numbervalue_constructor_args():
    sig = inspect.signature(henshin_text_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_numbervalue_has_value():
    assert hasattr(henshin_text_NumberValue, "value")
    descriptor = None
    for klass in henshin_text_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ComparisonExpression)


def test_henshin_text_comparisonexpression_constructor_exists():
    assert callable(henshin_text_ComparisonExpression.__init__)


def test_henshin_text_comparisonexpression_constructor_args():
    sig = inspect.signature(henshin_text_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin_text_comparisonexpression_has_op():
    assert hasattr(henshin_text_ComparisonExpression, "op")
    descriptor = None
    for klass in henshin_text_ComparisonExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_parametervalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ParameterValue)


def test_henshin_text_parametervalue_constructor_exists():
    assert callable(henshin_text_ParameterValue.__init__)


def test_henshin_text_parametervalue_constructor_args():
    sig = inspect.signature(henshin_text_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_stringvalue_is_not_abstract():
    assert not inspect.isabstract(henshin_text_StringValue)


def test_henshin_text_stringvalue_constructor_exists():
    assert callable(henshin_text_StringValue.__init__)


def test_henshin_text_stringvalue_constructor_args():
    sig = inspect.signature(henshin_text_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin_text_stringvalue_has_value():
    assert hasattr(henshin_text_StringValue, "value")
    descriptor = None
    for klass in henshin_text_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_orexpression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_OrExpression)


def test_henshin_text_orexpression_constructor_exists():
    assert callable(henshin_text_OrExpression.__init__)


def test_henshin_text_orexpression_constructor_args():
    sig = inspect.signature(henshin_text_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_rule_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Rule)


def test_henshin_text_rule_constructor_exists():
    assert callable(henshin_text_Rule.__init__)


def test_henshin_text_rule_constructor_args():
    sig = inspect.signature(henshin_text_Rule.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_unit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Unit)


def test_henshin_text_unit_constructor_exists():
    assert callable(henshin_text_Unit.__init__)


def test_henshin_text_unit_constructor_args():
    sig = inspect.signature(henshin_text_Unit.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_list_is_not_abstract():
    assert not inspect.isabstract(henshin_text_List)


def test_henshin_text_list_constructor_exists():
    assert callable(henshin_text_List.__init__)


def test_henshin_text_list_constructor_args():
    sig = inspect.signature(henshin_text_List.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_parametertype_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ParameterType)


def test_henshin_text_parametertype_constructor_exists():
    assert callable(henshin_text_ParameterType.__init__)


def test_henshin_text_parametertype_constructor_args():
    sig = inspect.signature(henshin_text_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "enumType" in params, "Missing parameter 'enumType'"

def test_henshin_text_parametertype_has_enumType():
    assert hasattr(henshin_text_ParameterType, "enumType")
    descriptor = None
    for klass in henshin_text_ParameterType.__mro__:
        if "enumType" in klass.__dict__:
            descriptor = klass.__dict__["enumType"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_match_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Match)


def test_henshin_text_match_constructor_exists():
    assert callable(henshin_text_Match.__init__)


def test_henshin_text_match_constructor_args():
    sig = inspect.signature(henshin_text_Match.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditionnodetypes_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionNodeTypes)


def test_henshin_text_conditionnodetypes_constructor_exists():
    assert callable(henshin_text_ConditionNodeTypes.__init__)


def test_henshin_text_conditionnodetypes_constructor_args():
    sig = inspect.signature(henshin_text_ConditionNodeTypes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin_text_conditionnodetypes_has_name():
    assert hasattr(henshin_text_ConditionNodeTypes, "name")
    descriptor = None
    for klass in henshin_text_ConditionNodeTypes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_conditionedge_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionEdge)


def test_henshin_text_conditionedge_constructor_exists():
    assert callable(henshin_text_ConditionEdge.__init__)


def test_henshin_text_conditionedge_constructor_args():
    sig = inspect.signature(henshin_text_ConditionEdge.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditiongraphelements_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionGraphElements)


def test_henshin_text_conditiongraphelements_constructor_exists():
    assert callable(henshin_text_ConditionGraphElements.__init__)


def test_henshin_text_conditiongraphelements_constructor_args():
    sig = inspect.signature(henshin_text_ConditionGraphElements.__init__)
    params = list(sig.parameters.keys())



def test_sequentialproperties_is_not_abstract():
    assert not inspect.isabstract(SequentialProperties)


def test_sequentialproperties_constructor_exists():
    assert callable(SequentialProperties.__init__)


def test_sequentialproperties_constructor_args():
    sig = inspect.signature(SequentialProperties.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_rollback_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Rollback)


def test_henshin_text_rollback_constructor_exists():
    assert callable(henshin_text_Rollback.__init__)


def test_henshin_text_rollback_constructor_args():
    sig = inspect.signature(henshin_text_Rollback.__init__)
    params = list(sig.parameters.keys())
    assert "rollback" in params, "Missing parameter 'rollback'"

def test_henshin_text_rollback_has_rollback():
    assert hasattr(henshin_text_Rollback, "rollback")
    descriptor = None
    for klass in henshin_text_Rollback.__mro__:
        if "rollback" in klass.__dict__:
            descriptor = klass.__dict__["rollback"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_strict_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Strict)


def test_henshin_text_strict_constructor_exists():
    assert callable(henshin_text_Strict.__init__)


def test_henshin_text_strict_constructor_args():
    sig = inspect.signature(henshin_text_Strict.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"

def test_henshin_text_strict_has_strict():
    assert hasattr(henshin_text_Strict, "strict")
    descriptor = None
    for klass in henshin_text_Strict.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_unitelement_is_not_abstract():
    assert not inspect.isabstract(UnitElement)


def test_unitelement_constructor_exists():
    assert callable(UnitElement.__init__)


def test_unitelement_constructor_args():
    sig = inspect.signature(UnitElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_iteratedunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_IteratedUnit)


def test_henshin_text_iteratedunit_constructor_exists():
    assert callable(henshin_text_IteratedUnit.__init__)


def test_henshin_text_iteratedunit_constructor_args():
    sig = inspect.signature(henshin_text_IteratedUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_priorityunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_PriorityUnit)


def test_henshin_text_priorityunit_constructor_exists():
    assert callable(henshin_text_PriorityUnit.__init__)


def test_henshin_text_priorityunit_constructor_args():
    sig = inspect.signature(henshin_text_PriorityUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_independentunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_IndependentUnit)


def test_henshin_text_independentunit_constructor_exists():
    assert callable(henshin_text_IndependentUnit.__init__)


def test_henshin_text_independentunit_constructor_args():
    sig = inspect.signature(henshin_text_IndependentUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditionalunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionalUnit)


def test_henshin_text_conditionalunit_constructor_exists():
    assert callable(henshin_text_ConditionalUnit.__init__)


def test_henshin_text_conditionalunit_constructor_args():
    sig = inspect.signature(henshin_text_ConditionalUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_call_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Call)


def test_henshin_text_call_constructor_exists():
    assert callable(henshin_text_Call.__init__)


def test_henshin_text_call_constructor_args():
    sig = inspect.signature(henshin_text_Call.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_loopunit_is_not_abstract():
    assert not inspect.isabstract(henshin_text_LoopUnit)


def test_henshin_text_loopunit_constructor_exists():
    assert callable(henshin_text_LoopUnit.__init__)


def test_henshin_text_loopunit_constructor_args():
    sig = inspect.signature(henshin_text_LoopUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_sequentialproperties_is_not_abstract():
    assert not inspect.isabstract(henshin_text_SequentialProperties)


def test_henshin_text_sequentialproperties_constructor_exists():
    assert callable(henshin_text_SequentialProperties.__init__)


def test_henshin_text_sequentialproperties_constructor_args():
    sig = inspect.signature(henshin_text_SequentialProperties.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_unitelement_is_not_abstract():
    assert not inspect.isabstract(henshin_text_UnitElement)


def test_henshin_text_unitelement_constructor_exists():
    assert callable(henshin_text_UnitElement.__init__)


def test_henshin_text_unitelement_constructor_args():
    sig = inspect.signature(henshin_text_UnitElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_eattribute_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EAttribute)


def test_henshin_text_eattribute_constructor_exists():
    assert callable(henshin_text_EAttribute.__init__)


def test_henshin_text_eattribute_constructor_args():
    sig = inspect.signature(henshin_text_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_attribute_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Attribute)


def test_henshin_text_attribute_constructor_exists():
    assert callable(henshin_text_Attribute.__init__)


def test_henshin_text_attribute_constructor_args():
    sig = inspect.signature(henshin_text_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"
    assert "update" in params, "Missing parameter 'update'"

def test_henshin_text_attribute_has_actiontype():
    assert hasattr(henshin_text_Attribute, "actiontype")
    descriptor = None
    for klass in henshin_text_Attribute.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)

def test_henshin_text_attribute_has_update():
    assert hasattr(henshin_text_Attribute, "update")
    descriptor = None
    for klass in henshin_text_Attribute.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_eclass_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EClass)


def test_henshin_text_eclass_constructor_exists():
    assert callable(henshin_text_EClass.__init__)


def test_henshin_text_eclass_constructor_args():
    sig = inspect.signature(henshin_text_EClass.__init__)
    params = list(sig.parameters.keys())



def test_conditionnodetypes_is_not_abstract():
    assert not inspect.isabstract(ConditionNodeTypes)


def test_conditionnodetypes_constructor_exists():
    assert callable(ConditionNodeTypes.__init__)


def test_conditionnodetypes_constructor_args():
    sig = inspect.signature(ConditionNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_rulenodetypes_is_not_abstract():
    assert not inspect.isabstract(RuleNodeTypes)


def test_rulenodetypes_constructor_exists():
    assert callable(RuleNodeTypes.__init__)


def test_rulenodetypes_constructor_args():
    sig = inspect.signature(RuleNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_ereference_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EReference)


def test_henshin_text_ereference_constructor_exists():
    assert callable(henshin_text_EReference.__init__)


def test_henshin_text_ereference_constructor_args():
    sig = inspect.signature(henshin_text_EReference.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditiongraph_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionGraph)


def test_henshin_text_conditiongraph_constructor_exists():
    assert callable(henshin_text_ConditionGraph.__init__)


def test_henshin_text_conditiongraph_constructor_args():
    sig = inspect.signature(henshin_text_ConditionGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin_text_conditiongraph_has_name():
    assert hasattr(henshin_text_ConditionGraph, "name")
    descriptor = None
    for klass in henshin_text_ConditionGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_logic_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Logic)


def test_henshin_text_logic_constructor_exists():
    assert callable(henshin_text_Logic.__init__)


def test_henshin_text_logic_constructor_args():
    sig = inspect.signature(henshin_text_Logic.__init__)
    params = list(sig.parameters.keys())



def test_conditiongraphelements_is_not_abstract():
    assert not inspect.isabstract(ConditionGraphElements)


def test_conditiongraphelements_constructor_exists():
    assert callable(ConditionGraphElements.__init__)


def test_conditiongraphelements_constructor_args():
    sig = inspect.signature(ConditionGraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditionnode_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionNode)


def test_henshin_text_conditionnode_constructor_exists():
    assert callable(henshin_text_ConditionNode.__init__)


def test_henshin_text_conditionnode_constructor_args():
    sig = inspect.signature(henshin_text_ConditionNode.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditionreusenode_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionReuseNode)


def test_henshin_text_conditionreusenode_constructor_exists():
    assert callable(henshin_text_ConditionReuseNode.__init__)


def test_henshin_text_conditionreusenode_constructor_args():
    sig = inspect.signature(henshin_text_ConditionReuseNode.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_conditionedges_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ConditionEdges)


def test_henshin_text_conditionedges_constructor_exists():
    assert callable(henshin_text_ConditionEdges.__init__)


def test_henshin_text_conditionedges_constructor_args():
    sig = inspect.signature(henshin_text_ConditionEdges.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_graphelements_is_not_abstract():
    assert not inspect.isabstract(henshin_text_GraphElements)


def test_henshin_text_graphelements_constructor_exists():
    assert callable(henshin_text_GraphElements.__init__)


def test_henshin_text_graphelements_constructor_args():
    sig = inspect.signature(henshin_text_GraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_expression_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Expression)


def test_henshin_text_expression_constructor_exists():
    assert callable(henshin_text_Expression.__init__)


def test_henshin_text_expression_constructor_args():
    sig = inspect.signature(henshin_text_Expression.__init__)
    params = list(sig.parameters.keys())



def test_ruleelement_is_not_abstract():
    assert not inspect.isabstract(RuleElement)


def test_ruleelement_constructor_exists():
    assert callable(RuleElement.__init__)


def test_ruleelement_constructor_args():
    sig = inspect.signature(RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_checkdangling_is_not_abstract():
    assert not inspect.isabstract(henshin_text_CheckDangling)


def test_henshin_text_checkdangling_constructor_exists():
    assert callable(henshin_text_CheckDangling.__init__)


def test_henshin_text_checkdangling_constructor_args():
    sig = inspect.signature(henshin_text_CheckDangling.__init__)
    params = list(sig.parameters.keys())
    assert "checkDangling" in params, "Missing parameter 'checkDangling'"

def test_henshin_text_checkdangling_has_checkDangling():
    assert hasattr(henshin_text_CheckDangling, "checkDangling")
    descriptor = None
    for klass in henshin_text_CheckDangling.__mro__:
        if "checkDangling" in klass.__dict__:
            descriptor = klass.__dict__["checkDangling"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_conditions_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Conditions)


def test_henshin_text_conditions_constructor_exists():
    assert callable(henshin_text_Conditions.__init__)


def test_henshin_text_conditions_constructor_args():
    sig = inspect.signature(henshin_text_Conditions.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_injectivematching_is_not_abstract():
    assert not inspect.isabstract(henshin_text_InjectiveMatching)


def test_henshin_text_injectivematching_constructor_exists():
    assert callable(henshin_text_InjectiveMatching.__init__)


def test_henshin_text_injectivematching_constructor_args():
    sig = inspect.signature(henshin_text_InjectiveMatching.__init__)
    params = list(sig.parameters.keys())
    assert "injectiveMatching" in params, "Missing parameter 'injectiveMatching'"

def test_henshin_text_injectivematching_has_injectiveMatching():
    assert hasattr(henshin_text_InjectiveMatching, "injectiveMatching")
    descriptor = None
    for klass in henshin_text_InjectiveMatching.__mro__:
        if "injectiveMatching" in klass.__dict__:
            descriptor = klass.__dict__["injectiveMatching"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_graph_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Graph)


def test_henshin_text_graph_constructor_exists():
    assert callable(henshin_text_Graph.__init__)


def test_henshin_text_graph_constructor_args():
    sig = inspect.signature(henshin_text_Graph.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_javaimport_is_not_abstract():
    assert not inspect.isabstract(henshin_text_JavaImport)


def test_henshin_text_javaimport_constructor_exists():
    assert callable(henshin_text_JavaImport.__init__)


def test_henshin_text_javaimport_constructor_args():
    sig = inspect.signature(henshin_text_JavaImport.__init__)
    params = list(sig.parameters.keys())
    assert "packagename" in params, "Missing parameter 'packagename'"

def test_henshin_text_javaimport_has_packagename():
    assert hasattr(henshin_text_JavaImport, "packagename")
    descriptor = None
    for klass in henshin_text_JavaImport.__mro__:
        if "packagename" in klass.__dict__:
            descriptor = klass.__dict__["packagename"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_ruleelement_is_not_abstract():
    assert not inspect.isabstract(henshin_text_RuleElement)


def test_henshin_text_ruleelement_constructor_exists():
    assert callable(henshin_text_RuleElement.__init__)


def test_henshin_text_ruleelement_constructor_args():
    sig = inspect.signature(henshin_text_RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_parameter_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Parameter)


def test_henshin_text_parameter_constructor_exists():
    assert callable(henshin_text_Parameter.__init__)


def test_henshin_text_parameter_constructor_args():
    sig = inspect.signature(henshin_text_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin_text_parameter_has_name():
    assert hasattr(henshin_text_Parameter, "name")
    descriptor = None
    for klass in henshin_text_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_epackage_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EPackage)


def test_henshin_text_epackage_constructor_exists():
    assert callable(henshin_text_EPackage.__init__)


def test_henshin_text_epackage_constructor_args():
    sig = inspect.signature(henshin_text_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_modelelement_is_not_abstract():
    assert not inspect.isabstract(henshin_text_ModelElement)


def test_henshin_text_modelelement_constructor_exists():
    assert callable(henshin_text_ModelElement.__init__)


def test_henshin_text_modelelement_constructor_args():
    sig = inspect.signature(henshin_text_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin_text_modelelement_has_name():
    assert hasattr(henshin_text_ModelElement, "name")
    descriptor = None
    for klass in henshin_text_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_rulenodetypes_is_not_abstract():
    assert not inspect.isabstract(henshin_text_RuleNodeTypes)


def test_henshin_text_rulenodetypes_constructor_exists():
    assert callable(henshin_text_RuleNodeTypes.__init__)


def test_henshin_text_rulenodetypes_constructor_args():
    sig = inspect.signature(henshin_text_RuleNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_edge_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Edge)


def test_henshin_text_edge_constructor_exists():
    assert callable(henshin_text_Edge.__init__)


def test_henshin_text_edge_constructor_args():
    sig = inspect.signature(henshin_text_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"

def test_henshin_text_edge_has_actiontype():
    assert hasattr(henshin_text_Edge, "actiontype")
    descriptor = None
    for klass in henshin_text_Edge.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)



def test_graphelements_is_not_abstract():
    assert not inspect.isabstract(GraphElements)


def test_graphelements_constructor_exists():
    assert callable(GraphElements.__init__)


def test_graphelements_constructor_args():
    sig = inspect.signature(GraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_multirule_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MultiRule)


def test_henshin_text_multirule_constructor_exists():
    assert callable(henshin_text_MultiRule.__init__)


def test_henshin_text_multirule_constructor_args():
    sig = inspect.signature(henshin_text_MultiRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin_text_multirule_has_name():
    assert hasattr(henshin_text_MultiRule, "name")
    descriptor = None
    for klass in henshin_text_MultiRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_node_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Node)


def test_henshin_text_node_constructor_exists():
    assert callable(henshin_text_Node.__init__)


def test_henshin_text_node_constructor_args():
    sig = inspect.signature(henshin_text_Node.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"

def test_henshin_text_node_has_actiontype():
    assert hasattr(henshin_text_Node, "actiontype")
    descriptor = None
    for klass in henshin_text_Node.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)



def test_henshin_text_multirulereusenode_is_not_abstract():
    assert not inspect.isabstract(henshin_text_MultiRuleReuseNode)


def test_henshin_text_multirulereusenode_constructor_exists():
    assert callable(henshin_text_MultiRuleReuseNode.__init__)


def test_henshin_text_multirulereusenode_constructor_args():
    sig = inspect.signature(henshin_text_MultiRuleReuseNode.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_formula_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Formula)


def test_henshin_text_formula_constructor_exists():
    assert callable(henshin_text_Formula.__init__)


def test_henshin_text_formula_constructor_args():
    sig = inspect.signature(henshin_text_Formula.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_edges_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Edges)


def test_henshin_text_edges_constructor_exists():
    assert callable(henshin_text_Edges.__init__)


def test_henshin_text_edges_constructor_args():
    sig = inspect.signature(henshin_text_Edges.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_epackageimport_is_not_abstract():
    assert not inspect.isabstract(henshin_text_EPackageImport)


def test_henshin_text_epackageimport_constructor_exists():
    assert callable(henshin_text_EPackageImport.__init__)


def test_henshin_text_epackageimport_constructor_args():
    sig = inspect.signature(henshin_text_EPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_henshin_text_model_is_not_abstract():
    assert not inspect.isabstract(henshin_text_Model)


def test_henshin_text_model_constructor_exists():
    assert callable(henshin_text_Model.__init__)


def test_henshin_text_model_constructor_args():
    sig = inspect.signature(henshin_text_Model.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "eLong",
        "eResource",
        "eBoolean",
        "eDate",
        "eLongObject",
        "eBigInteger",
        "eDoubleObject",
        "eDouble",
        "eJavaClass",
        "eInt",
        "eByteArray",
        "eEList",
        "eBooleanObject",
        "eDiagnosticChain",
        "eResourceSet",
        "eChar",
        "eEnumerator",
        "eMap",
        "eIntegerObject",
        "eFloat",
        "eJavaObject",
        "eFloatObject",
        "eInvocationTargetException",
        "eShortObject",
        "eShort",
        "eByteObject",
        "eCharacterObject",
        "eBigDecimal",
        "eByte",
        "eTreeIterator",
        "eFeatureMap",
        "eString",
        "eFeatureMapEntry",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
Logic_strategy = st.builds(
    Logic,
)
henshin_text_Not_strategy = st.builds(
    henshin_text_Not,
)
henshin_text_ConditionGraphRef_strategy = st.builds(
    henshin_text_ConditionGraphRef,
)
henshin_text_AND_strategy = st.builds(
    henshin_text_AND,
)
henshin_text_ORorXOR_strategy = st.builds(
    henshin_text_ORorXOR,
    op=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
henshin_text_JavaAttributeValue_strategy = st.builds(
    henshin_text_JavaAttributeValue,
    value=
        safe_text
)
henshin_text_MulOrDivExpression_strategy = st.builds(
    henshin_text_MulOrDivExpression,
    op=
        safe_text
)
henshin_text_NotExpression_strategy = st.builds(
    henshin_text_NotExpression,
)
henshin_text_AndExpression_strategy = st.builds(
    henshin_text_AndExpression,
)
henshin_text_PlusExpression_strategy = st.builds(
    henshin_text_PlusExpression,
)
henshin_text_MinusExpression_strategy = st.builds(
    henshin_text_MinusExpression,
)
henshin_text_IntegerValue_strategy = st.builds(
    henshin_text_IntegerValue,
    value=
        safe_text
)
henshin_text_EqualityExpression_strategy = st.builds(
    henshin_text_EqualityExpression,
    op=
        safe_text
)
henshin_text_BracketExpression_strategy = st.builds(
    henshin_text_BracketExpression,
)
henshin_text_NaturalValue_strategy = st.builds(
    henshin_text_NaturalValue,
    value=
        st.integers()
)
henshin_text_JavaClassValue_strategy = st.builds(
    henshin_text_JavaClassValue,
    value=
        safe_text
)
henshin_text_BoolValue_strategy = st.builds(
    henshin_text_BoolValue,
    value=
        st.booleans()
)
henshin_text_NumberValue_strategy = st.builds(
    henshin_text_NumberValue,
    value=
        safe_text
)
henshin_text_ComparisonExpression_strategy = st.builds(
    henshin_text_ComparisonExpression,
    op=
        safe_text
)
henshin_text_ParameterValue_strategy = st.builds(
    henshin_text_ParameterValue,
)
henshin_text_StringValue_strategy = st.builds(
    henshin_text_StringValue,
    value=
        safe_text
)
henshin_text_OrExpression_strategy = st.builds(
    henshin_text_OrExpression,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
henshin_text_Rule_strategy = st.builds(
    henshin_text_Rule,
)
henshin_text_Unit_strategy = st.builds(
    henshin_text_Unit,
)
henshin_text_List_strategy = st.builds(
    henshin_text_List,
)
henshin_text_ParameterType_strategy = st.builds(
    henshin_text_ParameterType,
    enumType=
        safe_text
)
henshin_text_Match_strategy = st.builds(
    henshin_text_Match,
)
henshin_text_ConditionNodeTypes_strategy = st.builds(
    henshin_text_ConditionNodeTypes,
    name=
        safe_text
)
henshin_text_ConditionEdge_strategy = st.builds(
    henshin_text_ConditionEdge,
)
henshin_text_ConditionGraphElements_strategy = st.builds(
    henshin_text_ConditionGraphElements,
)
SequentialProperties_strategy = st.builds(
    SequentialProperties,
)
henshin_text_Rollback_strategy = st.builds(
    henshin_text_Rollback,
    rollback=
        st.booleans()
)
henshin_text_Strict_strategy = st.builds(
    henshin_text_Strict,
    strict=
        st.booleans()
)
UnitElement_strategy = st.builds(
    UnitElement,
)
henshin_text_IteratedUnit_strategy = st.builds(
    henshin_text_IteratedUnit,
)
henshin_text_PriorityUnit_strategy = st.builds(
    henshin_text_PriorityUnit,
)
henshin_text_IndependentUnit_strategy = st.builds(
    henshin_text_IndependentUnit,
)
henshin_text_ConditionalUnit_strategy = st.builds(
    henshin_text_ConditionalUnit,
)
henshin_text_Call_strategy = st.builds(
    henshin_text_Call,
)
henshin_text_LoopUnit_strategy = st.builds(
    henshin_text_LoopUnit,
)
henshin_text_SequentialProperties_strategy = st.builds(
    henshin_text_SequentialProperties,
)
henshin_text_UnitElement_strategy = st.builds(
    henshin_text_UnitElement,
)
henshin_text_EAttribute_strategy = st.builds(
    henshin_text_EAttribute,
)
henshin_text_Attribute_strategy = st.builds(
    henshin_text_Attribute,
    actiontype=
        safe_text,
    update=
        safe_text
)
henshin_text_EClass_strategy = st.builds(
    henshin_text_EClass,
)
ConditionNodeTypes_strategy = st.builds(
    ConditionNodeTypes,
)
RuleNodeTypes_strategy = st.builds(
    RuleNodeTypes,
)
henshin_text_EReference_strategy = st.builds(
    henshin_text_EReference,
)
henshin_text_ConditionGraph_strategy = st.builds(
    henshin_text_ConditionGraph,
    name=
        safe_text
)
henshin_text_Logic_strategy = st.builds(
    henshin_text_Logic,
)
ConditionGraphElements_strategy = st.builds(
    ConditionGraphElements,
)
henshin_text_ConditionNode_strategy = st.builds(
    henshin_text_ConditionNode,
)
henshin_text_ConditionReuseNode_strategy = st.builds(
    henshin_text_ConditionReuseNode,
)
henshin_text_ConditionEdges_strategy = st.builds(
    henshin_text_ConditionEdges,
)
henshin_text_GraphElements_strategy = st.builds(
    henshin_text_GraphElements,
)
henshin_text_Expression_strategy = st.builds(
    henshin_text_Expression,
)
RuleElement_strategy = st.builds(
    RuleElement,
)
henshin_text_CheckDangling_strategy = st.builds(
    henshin_text_CheckDangling,
    checkDangling=
        st.booleans()
)
henshin_text_Conditions_strategy = st.builds(
    henshin_text_Conditions,
)
henshin_text_InjectiveMatching_strategy = st.builds(
    henshin_text_InjectiveMatching,
    injectiveMatching=
        st.booleans()
)
henshin_text_Graph_strategy = st.builds(
    henshin_text_Graph,
)
henshin_text_JavaImport_strategy = st.builds(
    henshin_text_JavaImport,
    packagename=
        safe_text
)
henshin_text_RuleElement_strategy = st.builds(
    henshin_text_RuleElement,
)
henshin_text_Parameter_strategy = st.builds(
    henshin_text_Parameter,
    name=
        safe_text
)
henshin_text_EPackage_strategy = st.builds(
    henshin_text_EPackage,
)
henshin_text_ModelElement_strategy = st.builds(
    henshin_text_ModelElement,
    name=
        safe_text
)
henshin_text_RuleNodeTypes_strategy = st.builds(
    henshin_text_RuleNodeTypes,
)
henshin_text_Edge_strategy = st.builds(
    henshin_text_Edge,
    actiontype=
        safe_text
)
GraphElements_strategy = st.builds(
    GraphElements,
)
henshin_text_MultiRule_strategy = st.builds(
    henshin_text_MultiRule,
    name=
        safe_text
)
henshin_text_Node_strategy = st.builds(
    henshin_text_Node,
    actiontype=
        safe_text
)
henshin_text_MultiRuleReuseNode_strategy = st.builds(
    henshin_text_MultiRuleReuseNode,
)
henshin_text_Formula_strategy = st.builds(
    henshin_text_Formula,
)
henshin_text_Edges_strategy = st.builds(
    henshin_text_Edges,
)
henshin_text_EPackageImport_strategy = st.builds(
    henshin_text_EPackageImport,
)
henshin_text_Model_strategy = st.builds(
    henshin_text_Model,
)

@given(instance=Logic_strategy)
@settings(max_examples=50)
def test_logic_instantiation(instance):
    assert isinstance(instance, Logic)

@given(instance=henshin_text_Not_strategy)
@settings(max_examples=50)
def test_henshin_text_not_instantiation(instance):
    assert isinstance(instance, henshin_text_Not)

@given(instance=henshin_text_ConditionGraphRef_strategy)
@settings(max_examples=50)
def test_henshin_text_conditiongraphref_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionGraphRef)

@given(instance=henshin_text_AND_strategy)
@settings(max_examples=50)
def test_henshin_text_and_instantiation(instance):
    assert isinstance(instance, henshin_text_AND)

@given(instance=henshin_text_ORorXOR_strategy)
@settings(max_examples=50)
def test_henshin_text_ororxor_instantiation(instance):
    assert isinstance(instance, henshin_text_ORorXOR)



@given(instance=henshin_text_ORorXOR_strategy)
def test_henshin_text_ororxor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=henshin_text_JavaAttributeValue_strategy)
@settings(max_examples=50)
def test_henshin_text_javaattributevalue_instantiation(instance):
    assert isinstance(instance, henshin_text_JavaAttributeValue)



@given(instance=henshin_text_JavaAttributeValue_strategy)
def test_henshin_text_javaattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_MulOrDivExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_mulordivexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_MulOrDivExpression)



@given(instance=henshin_text_MulOrDivExpression_strategy)
def test_henshin_text_mulordivexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=henshin_text_NotExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_notexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_NotExpression)

@given(instance=henshin_text_AndExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_andexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_AndExpression)

@given(instance=henshin_text_PlusExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_plusexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_PlusExpression)

@given(instance=henshin_text_MinusExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_minusexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_MinusExpression)

@given(instance=henshin_text_IntegerValue_strategy)
@settings(max_examples=50)
def test_henshin_text_integervalue_instantiation(instance):
    assert isinstance(instance, henshin_text_IntegerValue)



@given(instance=henshin_text_IntegerValue_strategy)
def test_henshin_text_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_EqualityExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_equalityexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_EqualityExpression)



@given(instance=henshin_text_EqualityExpression_strategy)
def test_henshin_text_equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=henshin_text_BracketExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_bracketexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_BracketExpression)

@given(instance=henshin_text_NaturalValue_strategy)
@settings(max_examples=50)
def test_henshin_text_naturalvalue_instantiation(instance):
    assert isinstance(instance, henshin_text_NaturalValue)



@given(instance=henshin_text_NaturalValue_strategy)
def test_henshin_text_naturalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_JavaClassValue_strategy)
@settings(max_examples=50)
def test_henshin_text_javaclassvalue_instantiation(instance):
    assert isinstance(instance, henshin_text_JavaClassValue)



@given(instance=henshin_text_JavaClassValue_strategy)
def test_henshin_text_javaclassvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_BoolValue_strategy)
@settings(max_examples=50)
def test_henshin_text_boolvalue_instantiation(instance):
    assert isinstance(instance, henshin_text_BoolValue)



@given(instance=henshin_text_BoolValue_strategy)
def test_henshin_text_boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_NumberValue_strategy)
@settings(max_examples=50)
def test_henshin_text_numbervalue_instantiation(instance):
    assert isinstance(instance, henshin_text_NumberValue)



@given(instance=henshin_text_NumberValue_strategy)
def test_henshin_text_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_ComparisonExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_comparisonexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_ComparisonExpression)



@given(instance=henshin_text_ComparisonExpression_strategy)
def test_henshin_text_comparisonexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=henshin_text_ParameterValue_strategy)
@settings(max_examples=50)
def test_henshin_text_parametervalue_instantiation(instance):
    assert isinstance(instance, henshin_text_ParameterValue)

@given(instance=henshin_text_StringValue_strategy)
@settings(max_examples=50)
def test_henshin_text_stringvalue_instantiation(instance):
    assert isinstance(instance, henshin_text_StringValue)



@given(instance=henshin_text_StringValue_strategy)
def test_henshin_text_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin_text_OrExpression_strategy)
@settings(max_examples=50)
def test_henshin_text_orexpression_instantiation(instance):
    assert isinstance(instance, henshin_text_OrExpression)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=henshin_text_Rule_strategy)
@settings(max_examples=50)
def test_henshin_text_rule_instantiation(instance):
    assert isinstance(instance, henshin_text_Rule)

@given(instance=henshin_text_Unit_strategy)
@settings(max_examples=50)
def test_henshin_text_unit_instantiation(instance):
    assert isinstance(instance, henshin_text_Unit)

@given(instance=henshin_text_List_strategy)
@settings(max_examples=50)
def test_henshin_text_list_instantiation(instance):
    assert isinstance(instance, henshin_text_List)

@given(instance=henshin_text_ParameterType_strategy)
@settings(max_examples=50)
def test_henshin_text_parametertype_instantiation(instance):
    assert isinstance(instance, henshin_text_ParameterType)



@given(instance=henshin_text_ParameterType_strategy)
def test_henshin_text_parametertype_enumType_setter(instance):
    original = instance.enumType
    instance.enumType = original
    assert instance.enumType == original

@given(instance=henshin_text_Match_strategy)
@settings(max_examples=50)
def test_henshin_text_match_instantiation(instance):
    assert isinstance(instance, henshin_text_Match)

@given(instance=henshin_text_ConditionNodeTypes_strategy)
@settings(max_examples=50)
def test_henshin_text_conditionnodetypes_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionNodeTypes)



@given(instance=henshin_text_ConditionNodeTypes_strategy)
def test_henshin_text_conditionnodetypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin_text_ConditionEdge_strategy)
@settings(max_examples=50)
def test_henshin_text_conditionedge_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionEdge)

@given(instance=henshin_text_ConditionGraphElements_strategy)
@settings(max_examples=50)
def test_henshin_text_conditiongraphelements_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionGraphElements)

@given(instance=SequentialProperties_strategy)
@settings(max_examples=50)
def test_sequentialproperties_instantiation(instance):
    assert isinstance(instance, SequentialProperties)

@given(instance=henshin_text_Rollback_strategy)
@settings(max_examples=50)
def test_henshin_text_rollback_instantiation(instance):
    assert isinstance(instance, henshin_text_Rollback)



@given(instance=henshin_text_Rollback_strategy)
def test_henshin_text_rollback_rollback_setter(instance):
    original = instance.rollback
    instance.rollback = original
    assert instance.rollback == original

@given(instance=henshin_text_Strict_strategy)
@settings(max_examples=50)
def test_henshin_text_strict_instantiation(instance):
    assert isinstance(instance, henshin_text_Strict)



@given(instance=henshin_text_Strict_strategy)
def test_henshin_text_strict_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=UnitElement_strategy)
@settings(max_examples=50)
def test_unitelement_instantiation(instance):
    assert isinstance(instance, UnitElement)

@given(instance=henshin_text_IteratedUnit_strategy)
@settings(max_examples=50)
def test_henshin_text_iteratedunit_instantiation(instance):
    assert isinstance(instance, henshin_text_IteratedUnit)

@given(instance=henshin_text_PriorityUnit_strategy)
@settings(max_examples=50)
def test_henshin_text_priorityunit_instantiation(instance):
    assert isinstance(instance, henshin_text_PriorityUnit)

@given(instance=henshin_text_IndependentUnit_strategy)
@settings(max_examples=50)
def test_henshin_text_independentunit_instantiation(instance):
    assert isinstance(instance, henshin_text_IndependentUnit)

@given(instance=henshin_text_ConditionalUnit_strategy)
@settings(max_examples=50)
def test_henshin_text_conditionalunit_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionalUnit)

@given(instance=henshin_text_Call_strategy)
@settings(max_examples=50)
def test_henshin_text_call_instantiation(instance):
    assert isinstance(instance, henshin_text_Call)

@given(instance=henshin_text_LoopUnit_strategy)
@settings(max_examples=50)
def test_henshin_text_loopunit_instantiation(instance):
    assert isinstance(instance, henshin_text_LoopUnit)

@given(instance=henshin_text_SequentialProperties_strategy)
@settings(max_examples=50)
def test_henshin_text_sequentialproperties_instantiation(instance):
    assert isinstance(instance, henshin_text_SequentialProperties)

@given(instance=henshin_text_UnitElement_strategy)
@settings(max_examples=50)
def test_henshin_text_unitelement_instantiation(instance):
    assert isinstance(instance, henshin_text_UnitElement)

@given(instance=henshin_text_EAttribute_strategy)
@settings(max_examples=50)
def test_henshin_text_eattribute_instantiation(instance):
    assert isinstance(instance, henshin_text_EAttribute)

@given(instance=henshin_text_Attribute_strategy)
@settings(max_examples=50)
def test_henshin_text_attribute_instantiation(instance):
    assert isinstance(instance, henshin_text_Attribute)



@given(instance=henshin_text_Attribute_strategy)
def test_henshin_text_attribute_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original



@given(instance=henshin_text_Attribute_strategy)
def test_henshin_text_attribute_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=henshin_text_EClass_strategy)
@settings(max_examples=50)
def test_henshin_text_eclass_instantiation(instance):
    assert isinstance(instance, henshin_text_EClass)

@given(instance=ConditionNodeTypes_strategy)
@settings(max_examples=50)
def test_conditionnodetypes_instantiation(instance):
    assert isinstance(instance, ConditionNodeTypes)

@given(instance=RuleNodeTypes_strategy)
@settings(max_examples=50)
def test_rulenodetypes_instantiation(instance):
    assert isinstance(instance, RuleNodeTypes)

@given(instance=henshin_text_EReference_strategy)
@settings(max_examples=50)
def test_henshin_text_ereference_instantiation(instance):
    assert isinstance(instance, henshin_text_EReference)

@given(instance=henshin_text_ConditionGraph_strategy)
@settings(max_examples=50)
def test_henshin_text_conditiongraph_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionGraph)



@given(instance=henshin_text_ConditionGraph_strategy)
def test_henshin_text_conditiongraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin_text_Logic_strategy)
@settings(max_examples=50)
def test_henshin_text_logic_instantiation(instance):
    assert isinstance(instance, henshin_text_Logic)

@given(instance=ConditionGraphElements_strategy)
@settings(max_examples=50)
def test_conditiongraphelements_instantiation(instance):
    assert isinstance(instance, ConditionGraphElements)

@given(instance=henshin_text_ConditionNode_strategy)
@settings(max_examples=50)
def test_henshin_text_conditionnode_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionNode)

@given(instance=henshin_text_ConditionReuseNode_strategy)
@settings(max_examples=50)
def test_henshin_text_conditionreusenode_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionReuseNode)

@given(instance=henshin_text_ConditionEdges_strategy)
@settings(max_examples=50)
def test_henshin_text_conditionedges_instantiation(instance):
    assert isinstance(instance, henshin_text_ConditionEdges)

@given(instance=henshin_text_GraphElements_strategy)
@settings(max_examples=50)
def test_henshin_text_graphelements_instantiation(instance):
    assert isinstance(instance, henshin_text_GraphElements)

@given(instance=henshin_text_Expression_strategy)
@settings(max_examples=50)
def test_henshin_text_expression_instantiation(instance):
    assert isinstance(instance, henshin_text_Expression)

@given(instance=RuleElement_strategy)
@settings(max_examples=50)
def test_ruleelement_instantiation(instance):
    assert isinstance(instance, RuleElement)

@given(instance=henshin_text_CheckDangling_strategy)
@settings(max_examples=50)
def test_henshin_text_checkdangling_instantiation(instance):
    assert isinstance(instance, henshin_text_CheckDangling)



@given(instance=henshin_text_CheckDangling_strategy)
def test_henshin_text_checkdangling_checkDangling_setter(instance):
    original = instance.checkDangling
    instance.checkDangling = original
    assert instance.checkDangling == original

@given(instance=henshin_text_Conditions_strategy)
@settings(max_examples=50)
def test_henshin_text_conditions_instantiation(instance):
    assert isinstance(instance, henshin_text_Conditions)

@given(instance=henshin_text_InjectiveMatching_strategy)
@settings(max_examples=50)
def test_henshin_text_injectivematching_instantiation(instance):
    assert isinstance(instance, henshin_text_InjectiveMatching)



@given(instance=henshin_text_InjectiveMatching_strategy)
def test_henshin_text_injectivematching_injectiveMatching_setter(instance):
    original = instance.injectiveMatching
    instance.injectiveMatching = original
    assert instance.injectiveMatching == original

@given(instance=henshin_text_Graph_strategy)
@settings(max_examples=50)
def test_henshin_text_graph_instantiation(instance):
    assert isinstance(instance, henshin_text_Graph)

@given(instance=henshin_text_JavaImport_strategy)
@settings(max_examples=50)
def test_henshin_text_javaimport_instantiation(instance):
    assert isinstance(instance, henshin_text_JavaImport)



@given(instance=henshin_text_JavaImport_strategy)
def test_henshin_text_javaimport_packagename_setter(instance):
    original = instance.packagename
    instance.packagename = original
    assert instance.packagename == original

@given(instance=henshin_text_RuleElement_strategy)
@settings(max_examples=50)
def test_henshin_text_ruleelement_instantiation(instance):
    assert isinstance(instance, henshin_text_RuleElement)

@given(instance=henshin_text_Parameter_strategy)
@settings(max_examples=50)
def test_henshin_text_parameter_instantiation(instance):
    assert isinstance(instance, henshin_text_Parameter)



@given(instance=henshin_text_Parameter_strategy)
def test_henshin_text_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin_text_EPackage_strategy)
@settings(max_examples=50)
def test_henshin_text_epackage_instantiation(instance):
    assert isinstance(instance, henshin_text_EPackage)

@given(instance=henshin_text_ModelElement_strategy)
@settings(max_examples=50)
def test_henshin_text_modelelement_instantiation(instance):
    assert isinstance(instance, henshin_text_ModelElement)



@given(instance=henshin_text_ModelElement_strategy)
def test_henshin_text_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin_text_RuleNodeTypes_strategy)
@settings(max_examples=50)
def test_henshin_text_rulenodetypes_instantiation(instance):
    assert isinstance(instance, henshin_text_RuleNodeTypes)

@given(instance=henshin_text_Edge_strategy)
@settings(max_examples=50)
def test_henshin_text_edge_instantiation(instance):
    assert isinstance(instance, henshin_text_Edge)



@given(instance=henshin_text_Edge_strategy)
def test_henshin_text_edge_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

@given(instance=GraphElements_strategy)
@settings(max_examples=50)
def test_graphelements_instantiation(instance):
    assert isinstance(instance, GraphElements)

@given(instance=henshin_text_MultiRule_strategy)
@settings(max_examples=50)
def test_henshin_text_multirule_instantiation(instance):
    assert isinstance(instance, henshin_text_MultiRule)



@given(instance=henshin_text_MultiRule_strategy)
def test_henshin_text_multirule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin_text_Node_strategy)
@settings(max_examples=50)
def test_henshin_text_node_instantiation(instance):
    assert isinstance(instance, henshin_text_Node)



@given(instance=henshin_text_Node_strategy)
def test_henshin_text_node_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

@given(instance=henshin_text_MultiRuleReuseNode_strategy)
@settings(max_examples=50)
def test_henshin_text_multirulereusenode_instantiation(instance):
    assert isinstance(instance, henshin_text_MultiRuleReuseNode)

@given(instance=henshin_text_Formula_strategy)
@settings(max_examples=50)
def test_henshin_text_formula_instantiation(instance):
    assert isinstance(instance, henshin_text_Formula)

@given(instance=henshin_text_Edges_strategy)
@settings(max_examples=50)
def test_henshin_text_edges_instantiation(instance):
    assert isinstance(instance, henshin_text_Edges)

@given(instance=henshin_text_EPackageImport_strategy)
@settings(max_examples=50)
def test_henshin_text_epackageimport_instantiation(instance):
    assert isinstance(instance, henshin_text_EPackageImport)

@given(instance=henshin_text_Model_strategy)
@settings(max_examples=50)
def test_henshin_text_model_instantiation(instance):
    assert isinstance(instance, henshin_text_Model)
