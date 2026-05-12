import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sml_StructuralFeatureValue,
    sml_CollectionAccess,
    sml_Variable,
    sml_Document,
    Value,
    sml_EnumValue,
    sml_BooleanValue,
    sml_StringValue,
    sml_NullValue,
    sml_IntegerValue,
    Expression,
    sml_BinaryOperationExpression,
    sml_UnaryOperationExpression,
    sml_Value,
    VariableExpression,
    sml_VariableAssignment,
    sml_TypedVariableDeclaration,
    sml_VariableDeclaration,
    ExpressionAndVariables,
    sml_ExpressionOrRegion,
    ExpressionOrRegion,
    sml_ExpressionAndVariables,
    sml_ExpressionRegion,
    sml_Message,
    Condition,
    sml_ViolationCondition,
    sml_InterruptCondition,
    sml_WaitCondition,
    sml_ConditionExpression,
    sml_LoopCondition,
    sml_CaseCondition,
    sml_Case,
    sml_VariableValue,
    sml_Expression,
    ParameterExpression,
    sml_VariableBindingParameter,
    sml_ExpressionParameter,
    sml_RandomParameter,
    sml_ParameterExpression,
    sml_ParameterBinding,
    sml_ConstraintBlock,
    sml_VariableExpression,
    InteractionFragment,
    sml_Condition,
    sml_Alternative,
    sml_Parallel,
    sml_ModalMessage,
    sml_Loop,
    sml_VariableFragment,
    sml_InteractionFragment,
    sml_FeatureAccess,
    BindingExpression,
    sml_FeatureAccessBindingExpression,
    sml_BindingExpression,
    sml_Interaction,
    sml_RoleBindingConstraint,
    sml_SmlEStructuralFeature,
    sml_SmlEClassifier,
    AbstractRanges,
    sml_StringRanges,
    sml_EnumRanges,
    sml_IntegerRanges,
    sml_AbstractRanges,
    sml_RangesForParameter,
    sml_Scenario,
    sml_Role,
    sml_SmlEEnumLiteral,
    sml_SmlEEnum,
    sml_Collaboration,
    sml_EventParameterRanges,
    sml_SmlETypedElement,
    sml_SmlEClass,
    sml_SmlEPackage,
    sml_Import,
    sml_Specification,
    ScenarioKind,
    CollectionOperation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sml_structuralfeaturevalue_is_not_abstract():
    assert not inspect.isabstract(sml_StructuralFeatureValue)


def test_sml_structuralfeaturevalue_constructor_exists():
    assert callable(sml_StructuralFeatureValue.__init__)


def test_sml_structuralfeaturevalue_constructor_args():
    sig = inspect.signature(sml_StructuralFeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_sml_collectionaccess_is_not_abstract():
    assert not inspect.isabstract(sml_CollectionAccess)


def test_sml_collectionaccess_constructor_exists():
    assert callable(sml_CollectionAccess.__init__)


def test_sml_collectionaccess_constructor_args():
    sig = inspect.signature(sml_CollectionAccess.__init__)
    params = list(sig.parameters.keys())
    assert "collectionOperation" in params, "Missing parameter 'collectionOperation'"

def test_sml_collectionaccess_has_collectionOperation():
    assert hasattr(sml_CollectionAccess, "collectionOperation")
    descriptor = None
    for klass in sml_CollectionAccess.__mro__:
        if "collectionOperation" in klass.__dict__:
            descriptor = klass.__dict__["collectionOperation"]
            break
    assert isinstance(descriptor, property)



def test_sml_variable_is_not_abstract():
    assert not inspect.isabstract(sml_Variable)


def test_sml_variable_constructor_exists():
    assert callable(sml_Variable.__init__)


def test_sml_variable_constructor_args():
    sig = inspect.signature(sml_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_variable_has_name():
    assert hasattr(sml_Variable, "name")
    descriptor = None
    for klass in sml_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_document_is_not_abstract():
    assert not inspect.isabstract(sml_Document)


def test_sml_document_constructor_exists():
    assert callable(sml_Document.__init__)


def test_sml_document_constructor_args():
    sig = inspect.signature(sml_Document.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_sml_enumvalue_is_not_abstract():
    assert not inspect.isabstract(sml_EnumValue)


def test_sml_enumvalue_constructor_exists():
    assert callable(sml_EnumValue.__init__)


def test_sml_enumvalue_constructor_args():
    sig = inspect.signature(sml_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_sml_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(sml_BooleanValue)


def test_sml_booleanvalue_constructor_exists():
    assert callable(sml_BooleanValue.__init__)


def test_sml_booleanvalue_constructor_args():
    sig = inspect.signature(sml_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sml_booleanvalue_has_value():
    assert hasattr(sml_BooleanValue, "value")
    descriptor = None
    for klass in sml_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sml_stringvalue_is_not_abstract():
    assert not inspect.isabstract(sml_StringValue)


def test_sml_stringvalue_constructor_exists():
    assert callable(sml_StringValue.__init__)


def test_sml_stringvalue_constructor_args():
    sig = inspect.signature(sml_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sml_stringvalue_has_value():
    assert hasattr(sml_StringValue, "value")
    descriptor = None
    for klass in sml_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sml_nullvalue_is_not_abstract():
    assert not inspect.isabstract(sml_NullValue)


def test_sml_nullvalue_constructor_exists():
    assert callable(sml_NullValue.__init__)


def test_sml_nullvalue_constructor_args():
    sig = inspect.signature(sml_NullValue.__init__)
    params = list(sig.parameters.keys())



def test_sml_integervalue_is_not_abstract():
    assert not inspect.isabstract(sml_IntegerValue)


def test_sml_integervalue_constructor_exists():
    assert callable(sml_IntegerValue.__init__)


def test_sml_integervalue_constructor_args():
    sig = inspect.signature(sml_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sml_integervalue_has_value():
    assert hasattr(sml_IntegerValue, "value")
    descriptor = None
    for klass in sml_IntegerValue.__mro__:
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



def test_sml_binaryoperationexpression_is_not_abstract():
    assert not inspect.isabstract(sml_BinaryOperationExpression)


def test_sml_binaryoperationexpression_constructor_exists():
    assert callable(sml_BinaryOperationExpression.__init__)


def test_sml_binaryoperationexpression_constructor_args():
    sig = inspect.signature(sml_BinaryOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sml_binaryoperationexpression_has_operator():
    assert hasattr(sml_BinaryOperationExpression, "operator")
    descriptor = None
    for klass in sml_BinaryOperationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sml_unaryoperationexpression_is_not_abstract():
    assert not inspect.isabstract(sml_UnaryOperationExpression)


def test_sml_unaryoperationexpression_constructor_exists():
    assert callable(sml_UnaryOperationExpression.__init__)


def test_sml_unaryoperationexpression_constructor_args():
    sig = inspect.signature(sml_UnaryOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sml_unaryoperationexpression_has_operator():
    assert hasattr(sml_UnaryOperationExpression, "operator")
    descriptor = None
    for klass in sml_UnaryOperationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sml_value_is_not_abstract():
    assert not inspect.isabstract(sml_Value)


def test_sml_value_constructor_exists():
    assert callable(sml_Value.__init__)


def test_sml_value_constructor_args():
    sig = inspect.signature(sml_Value.__init__)
    params = list(sig.parameters.keys())



def test_variableexpression_is_not_abstract():
    assert not inspect.isabstract(VariableExpression)


def test_variableexpression_constructor_exists():
    assert callable(VariableExpression.__init__)


def test_variableexpression_constructor_args():
    sig = inspect.signature(VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_variableassignment_is_not_abstract():
    assert not inspect.isabstract(sml_VariableAssignment)


def test_sml_variableassignment_constructor_exists():
    assert callable(sml_VariableAssignment.__init__)


def test_sml_variableassignment_constructor_args():
    sig = inspect.signature(sml_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_sml_typedvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(sml_TypedVariableDeclaration)


def test_sml_typedvariabledeclaration_constructor_exists():
    assert callable(sml_TypedVariableDeclaration.__init__)


def test_sml_typedvariabledeclaration_constructor_args():
    sig = inspect.signature(sml_TypedVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_typedvariabledeclaration_has_name():
    assert hasattr(sml_TypedVariableDeclaration, "name")
    descriptor = None
    for klass in sml_TypedVariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(sml_VariableDeclaration)


def test_sml_variabledeclaration_constructor_exists():
    assert callable(sml_VariableDeclaration.__init__)


def test_sml_variabledeclaration_constructor_args():
    sig = inspect.signature(sml_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_variabledeclaration_has_name():
    assert hasattr(sml_VariableDeclaration, "name")
    descriptor = None
    for klass in sml_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expressionandvariables_is_not_abstract():
    assert not inspect.isabstract(ExpressionAndVariables)


def test_expressionandvariables_constructor_exists():
    assert callable(ExpressionAndVariables.__init__)


def test_expressionandvariables_constructor_args():
    sig = inspect.signature(ExpressionAndVariables.__init__)
    params = list(sig.parameters.keys())



def test_sml_expressionorregion_is_not_abstract():
    assert not inspect.isabstract(sml_ExpressionOrRegion)


def test_sml_expressionorregion_constructor_exists():
    assert callable(sml_ExpressionOrRegion.__init__)


def test_sml_expressionorregion_constructor_args():
    sig = inspect.signature(sml_ExpressionOrRegion.__init__)
    params = list(sig.parameters.keys())



def test_expressionorregion_is_not_abstract():
    assert not inspect.isabstract(ExpressionOrRegion)


def test_expressionorregion_constructor_exists():
    assert callable(ExpressionOrRegion.__init__)


def test_expressionorregion_constructor_args():
    sig = inspect.signature(ExpressionOrRegion.__init__)
    params = list(sig.parameters.keys())



def test_sml_expressionandvariables_is_not_abstract():
    assert not inspect.isabstract(sml_ExpressionAndVariables)


def test_sml_expressionandvariables_constructor_exists():
    assert callable(sml_ExpressionAndVariables.__init__)


def test_sml_expressionandvariables_constructor_args():
    sig = inspect.signature(sml_ExpressionAndVariables.__init__)
    params = list(sig.parameters.keys())



def test_sml_expressionregion_is_not_abstract():
    assert not inspect.isabstract(sml_ExpressionRegion)


def test_sml_expressionregion_constructor_exists():
    assert callable(sml_ExpressionRegion.__init__)


def test_sml_expressionregion_constructor_args():
    sig = inspect.signature(sml_ExpressionRegion.__init__)
    params = list(sig.parameters.keys())



def test_sml_message_is_not_abstract():
    assert not inspect.isabstract(sml_Message)


def test_sml_message_constructor_exists():
    assert callable(sml_Message.__init__)


def test_sml_message_constructor_args():
    sig = inspect.signature(sml_Message.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sml_violationcondition_is_not_abstract():
    assert not inspect.isabstract(sml_ViolationCondition)


def test_sml_violationcondition_constructor_exists():
    assert callable(sml_ViolationCondition.__init__)


def test_sml_violationcondition_constructor_args():
    sig = inspect.signature(sml_ViolationCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml_interruptcondition_is_not_abstract():
    assert not inspect.isabstract(sml_InterruptCondition)


def test_sml_interruptcondition_constructor_exists():
    assert callable(sml_InterruptCondition.__init__)


def test_sml_interruptcondition_constructor_args():
    sig = inspect.signature(sml_InterruptCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml_waitcondition_is_not_abstract():
    assert not inspect.isabstract(sml_WaitCondition)


def test_sml_waitcondition_constructor_exists():
    assert callable(sml_WaitCondition.__init__)


def test_sml_waitcondition_constructor_args():
    sig = inspect.signature(sml_WaitCondition.__init__)
    params = list(sig.parameters.keys())
    assert "requested" in params, "Missing parameter 'requested'"
    assert "strict" in params, "Missing parameter 'strict'"

def test_sml_waitcondition_has_requested():
    assert hasattr(sml_WaitCondition, "requested")
    descriptor = None
    for klass in sml_WaitCondition.__mro__:
        if "requested" in klass.__dict__:
            descriptor = klass.__dict__["requested"]
            break
    assert isinstance(descriptor, property)

def test_sml_waitcondition_has_strict():
    assert hasattr(sml_WaitCondition, "strict")
    descriptor = None
    for klass in sml_WaitCondition.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_sml_conditionexpression_is_not_abstract():
    assert not inspect.isabstract(sml_ConditionExpression)


def test_sml_conditionexpression_constructor_exists():
    assert callable(sml_ConditionExpression.__init__)


def test_sml_conditionexpression_constructor_args():
    sig = inspect.signature(sml_ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_loopcondition_is_not_abstract():
    assert not inspect.isabstract(sml_LoopCondition)


def test_sml_loopcondition_constructor_exists():
    assert callable(sml_LoopCondition.__init__)


def test_sml_loopcondition_constructor_args():
    sig = inspect.signature(sml_LoopCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml_casecondition_is_not_abstract():
    assert not inspect.isabstract(sml_CaseCondition)


def test_sml_casecondition_constructor_exists():
    assert callable(sml_CaseCondition.__init__)


def test_sml_casecondition_constructor_args():
    sig = inspect.signature(sml_CaseCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml_case_is_not_abstract():
    assert not inspect.isabstract(sml_Case)


def test_sml_case_constructor_exists():
    assert callable(sml_Case.__init__)


def test_sml_case_constructor_args():
    sig = inspect.signature(sml_Case.__init__)
    params = list(sig.parameters.keys())



def test_sml_variablevalue_is_not_abstract():
    assert not inspect.isabstract(sml_VariableValue)


def test_sml_variablevalue_constructor_exists():
    assert callable(sml_VariableValue.__init__)


def test_sml_variablevalue_constructor_args():
    sig = inspect.signature(sml_VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_sml_expression_is_not_abstract():
    assert not inspect.isabstract(sml_Expression)


def test_sml_expression_constructor_exists():
    assert callable(sml_Expression.__init__)


def test_sml_expression_constructor_args():
    sig = inspect.signature(sml_Expression.__init__)
    params = list(sig.parameters.keys())



def test_parameterexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterExpression)


def test_parameterexpression_constructor_exists():
    assert callable(ParameterExpression.__init__)


def test_parameterexpression_constructor_args():
    sig = inspect.signature(ParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_variablebindingparameter_is_not_abstract():
    assert not inspect.isabstract(sml_VariableBindingParameter)


def test_sml_variablebindingparameter_constructor_exists():
    assert callable(sml_VariableBindingParameter.__init__)


def test_sml_variablebindingparameter_constructor_args():
    sig = inspect.signature(sml_VariableBindingParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml_expressionparameter_is_not_abstract():
    assert not inspect.isabstract(sml_ExpressionParameter)


def test_sml_expressionparameter_constructor_exists():
    assert callable(sml_ExpressionParameter.__init__)


def test_sml_expressionparameter_constructor_args():
    sig = inspect.signature(sml_ExpressionParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml_randomparameter_is_not_abstract():
    assert not inspect.isabstract(sml_RandomParameter)


def test_sml_randomparameter_constructor_exists():
    assert callable(sml_RandomParameter.__init__)


def test_sml_randomparameter_constructor_args():
    sig = inspect.signature(sml_RandomParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml_parameterexpression_is_not_abstract():
    assert not inspect.isabstract(sml_ParameterExpression)


def test_sml_parameterexpression_constructor_exists():
    assert callable(sml_ParameterExpression.__init__)


def test_sml_parameterexpression_constructor_args():
    sig = inspect.signature(sml_ParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_parameterbinding_is_not_abstract():
    assert not inspect.isabstract(sml_ParameterBinding)


def test_sml_parameterbinding_constructor_exists():
    assert callable(sml_ParameterBinding.__init__)


def test_sml_parameterbinding_constructor_args():
    sig = inspect.signature(sml_ParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_sml_constraintblock_is_not_abstract():
    assert not inspect.isabstract(sml_ConstraintBlock)


def test_sml_constraintblock_constructor_exists():
    assert callable(sml_ConstraintBlock.__init__)


def test_sml_constraintblock_constructor_args():
    sig = inspect.signature(sml_ConstraintBlock.__init__)
    params = list(sig.parameters.keys())



def test_sml_variableexpression_is_not_abstract():
    assert not inspect.isabstract(sml_VariableExpression)


def test_sml_variableexpression_constructor_exists():
    assert callable(sml_VariableExpression.__init__)


def test_sml_variableexpression_constructor_args():
    sig = inspect.signature(sml_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_sml_condition_is_not_abstract():
    assert not inspect.isabstract(sml_Condition)


def test_sml_condition_constructor_exists():
    assert callable(sml_Condition.__init__)


def test_sml_condition_constructor_args():
    sig = inspect.signature(sml_Condition.__init__)
    params = list(sig.parameters.keys())



def test_sml_alternative_is_not_abstract():
    assert not inspect.isabstract(sml_Alternative)


def test_sml_alternative_constructor_exists():
    assert callable(sml_Alternative.__init__)


def test_sml_alternative_constructor_args():
    sig = inspect.signature(sml_Alternative.__init__)
    params = list(sig.parameters.keys())



def test_sml_parallel_is_not_abstract():
    assert not inspect.isabstract(sml_Parallel)


def test_sml_parallel_constructor_exists():
    assert callable(sml_Parallel.__init__)


def test_sml_parallel_constructor_args():
    sig = inspect.signature(sml_Parallel.__init__)
    params = list(sig.parameters.keys())



def test_sml_modalmessage_is_not_abstract():
    assert not inspect.isabstract(sml_ModalMessage)


def test_sml_modalmessage_constructor_exists():
    assert callable(sml_ModalMessage.__init__)


def test_sml_modalmessage_constructor_args():
    sig = inspect.signature(sml_ModalMessage.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"
    assert "requested" in params, "Missing parameter 'requested'"

def test_sml_modalmessage_has_strict():
    assert hasattr(sml_ModalMessage, "strict")
    descriptor = None
    for klass in sml_ModalMessage.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_sml_modalmessage_has_requested():
    assert hasattr(sml_ModalMessage, "requested")
    descriptor = None
    for klass in sml_ModalMessage.__mro__:
        if "requested" in klass.__dict__:
            descriptor = klass.__dict__["requested"]
            break
    assert isinstance(descriptor, property)



def test_sml_loop_is_not_abstract():
    assert not inspect.isabstract(sml_Loop)


def test_sml_loop_constructor_exists():
    assert callable(sml_Loop.__init__)


def test_sml_loop_constructor_args():
    sig = inspect.signature(sml_Loop.__init__)
    params = list(sig.parameters.keys())



def test_sml_variablefragment_is_not_abstract():
    assert not inspect.isabstract(sml_VariableFragment)


def test_sml_variablefragment_constructor_exists():
    assert callable(sml_VariableFragment.__init__)


def test_sml_variablefragment_constructor_args():
    sig = inspect.signature(sml_VariableFragment.__init__)
    params = list(sig.parameters.keys())



def test_sml_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(sml_InteractionFragment)


def test_sml_interactionfragment_constructor_exists():
    assert callable(sml_InteractionFragment.__init__)


def test_sml_interactionfragment_constructor_args():
    sig = inspect.signature(sml_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_sml_featureaccess_is_not_abstract():
    assert not inspect.isabstract(sml_FeatureAccess)


def test_sml_featureaccess_constructor_exists():
    assert callable(sml_FeatureAccess.__init__)


def test_sml_featureaccess_constructor_args():
    sig = inspect.signature(sml_FeatureAccess.__init__)
    params = list(sig.parameters.keys())



def test_bindingexpression_is_not_abstract():
    assert not inspect.isabstract(BindingExpression)


def test_bindingexpression_constructor_exists():
    assert callable(BindingExpression.__init__)


def test_bindingexpression_constructor_args():
    sig = inspect.signature(BindingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_featureaccessbindingexpression_is_not_abstract():
    assert not inspect.isabstract(sml_FeatureAccessBindingExpression)


def test_sml_featureaccessbindingexpression_constructor_exists():
    assert callable(sml_FeatureAccessBindingExpression.__init__)


def test_sml_featureaccessbindingexpression_constructor_args():
    sig = inspect.signature(sml_FeatureAccessBindingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_bindingexpression_is_not_abstract():
    assert not inspect.isabstract(sml_BindingExpression)


def test_sml_bindingexpression_constructor_exists():
    assert callable(sml_BindingExpression.__init__)


def test_sml_bindingexpression_constructor_args():
    sig = inspect.signature(sml_BindingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml_interaction_is_not_abstract():
    assert not inspect.isabstract(sml_Interaction)


def test_sml_interaction_constructor_exists():
    assert callable(sml_Interaction.__init__)


def test_sml_interaction_constructor_args():
    sig = inspect.signature(sml_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_sml_rolebindingconstraint_is_not_abstract():
    assert not inspect.isabstract(sml_RoleBindingConstraint)


def test_sml_rolebindingconstraint_constructor_exists():
    assert callable(sml_RoleBindingConstraint.__init__)


def test_sml_rolebindingconstraint_constructor_args():
    sig = inspect.signature(sml_RoleBindingConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sml_smlestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(sml_SmlEStructuralFeature)


def test_sml_smlestructuralfeature_constructor_exists():
    assert callable(sml_SmlEStructuralFeature.__init__)


def test_sml_smlestructuralfeature_constructor_args():
    sig = inspect.signature(sml_SmlEStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smlestructuralfeature_has_name():
    assert hasattr(sml_SmlEStructuralFeature, "name")
    descriptor = None
    for klass in sml_SmlEStructuralFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_smleclassifier_is_not_abstract():
    assert not inspect.isabstract(sml_SmlEClassifier)


def test_sml_smleclassifier_constructor_exists():
    assert callable(sml_SmlEClassifier.__init__)


def test_sml_smleclassifier_constructor_args():
    sig = inspect.signature(sml_SmlEClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smleclassifier_has_name():
    assert hasattr(sml_SmlEClassifier, "name")
    descriptor = None
    for klass in sml_SmlEClassifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractranges_is_not_abstract():
    assert not inspect.isabstract(AbstractRanges)


def test_abstractranges_constructor_exists():
    assert callable(AbstractRanges.__init__)


def test_abstractranges_constructor_args():
    sig = inspect.signature(AbstractRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml_stringranges_is_not_abstract():
    assert not inspect.isabstract(sml_StringRanges)


def test_sml_stringranges_constructor_exists():
    assert callable(sml_StringRanges.__init__)


def test_sml_stringranges_constructor_args():
    sig = inspect.signature(sml_StringRanges.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_sml_stringranges_has_values():
    assert hasattr(sml_StringRanges, "values")
    descriptor = None
    for klass in sml_StringRanges.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_sml_enumranges_is_not_abstract():
    assert not inspect.isabstract(sml_EnumRanges)


def test_sml_enumranges_constructor_exists():
    assert callable(sml_EnumRanges.__init__)


def test_sml_enumranges_constructor_args():
    sig = inspect.signature(sml_EnumRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml_integerranges_is_not_abstract():
    assert not inspect.isabstract(sml_IntegerRanges)


def test_sml_integerranges_constructor_exists():
    assert callable(sml_IntegerRanges.__init__)


def test_sml_integerranges_constructor_args():
    sig = inspect.signature(sml_IntegerRanges.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_sml_integerranges_has_values():
    assert hasattr(sml_IntegerRanges, "values")
    descriptor = None
    for klass in sml_IntegerRanges.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_sml_integerranges_has_min():
    assert hasattr(sml_IntegerRanges, "min")
    descriptor = None
    for klass in sml_IntegerRanges.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_sml_integerranges_has_max():
    assert hasattr(sml_IntegerRanges, "max")
    descriptor = None
    for klass in sml_IntegerRanges.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_sml_abstractranges_is_not_abstract():
    assert not inspect.isabstract(sml_AbstractRanges)


def test_sml_abstractranges_constructor_exists():
    assert callable(sml_AbstractRanges.__init__)


def test_sml_abstractranges_constructor_args():
    sig = inspect.signature(sml_AbstractRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml_rangesforparameter_is_not_abstract():
    assert not inspect.isabstract(sml_RangesForParameter)


def test_sml_rangesforparameter_constructor_exists():
    assert callable(sml_RangesForParameter.__init__)


def test_sml_rangesforparameter_constructor_args():
    sig = inspect.signature(sml_RangesForParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml_scenario_is_not_abstract():
    assert not inspect.isabstract(sml_Scenario)


def test_sml_scenario_constructor_exists():
    assert callable(sml_Scenario.__init__)


def test_sml_scenario_constructor_args():
    sig = inspect.signature(sml_Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "singular" in params, "Missing parameter 'singular'"
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sml_scenario_has_singular():
    assert hasattr(sml_Scenario, "singular")
    descriptor = None
    for klass in sml_Scenario.__mro__:
        if "singular" in klass.__dict__:
            descriptor = klass.__dict__["singular"]
            break
    assert isinstance(descriptor, property)

def test_sml_scenario_has_name():
    assert hasattr(sml_Scenario, "name")
    descriptor = None
    for klass in sml_Scenario.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sml_scenario_has_kind():
    assert hasattr(sml_Scenario, "kind")
    descriptor = None
    for klass in sml_Scenario.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sml_role_is_not_abstract():
    assert not inspect.isabstract(sml_Role)


def test_sml_role_constructor_exists():
    assert callable(sml_Role.__init__)


def test_sml_role_constructor_args():
    sig = inspect.signature(sml_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "static" in params, "Missing parameter 'static'"

def test_sml_role_has_name():
    assert hasattr(sml_Role, "name")
    descriptor = None
    for klass in sml_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sml_role_has_static():
    assert hasattr(sml_Role, "static")
    descriptor = None
    for klass in sml_Role.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_sml_smleenumliteral_is_not_abstract():
    assert not inspect.isabstract(sml_SmlEEnumLiteral)


def test_sml_smleenumliteral_constructor_exists():
    assert callable(sml_SmlEEnumLiteral.__init__)


def test_sml_smleenumliteral_constructor_args():
    sig = inspect.signature(sml_SmlEEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smleenumliteral_has_name():
    assert hasattr(sml_SmlEEnumLiteral, "name")
    descriptor = None
    for klass in sml_SmlEEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_smleenum_is_not_abstract():
    assert not inspect.isabstract(sml_SmlEEnum)


def test_sml_smleenum_constructor_exists():
    assert callable(sml_SmlEEnum.__init__)


def test_sml_smleenum_constructor_args():
    sig = inspect.signature(sml_SmlEEnum.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smleenum_has_name():
    assert hasattr(sml_SmlEEnum, "name")
    descriptor = None
    for klass in sml_SmlEEnum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_collaboration_is_not_abstract():
    assert not inspect.isabstract(sml_Collaboration)


def test_sml_collaboration_constructor_exists():
    assert callable(sml_Collaboration.__init__)


def test_sml_collaboration_constructor_args():
    sig = inspect.signature(sml_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_collaboration_has_name():
    assert hasattr(sml_Collaboration, "name")
    descriptor = None
    for klass in sml_Collaboration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_eventparameterranges_is_not_abstract():
    assert not inspect.isabstract(sml_EventParameterRanges)


def test_sml_eventparameterranges_constructor_exists():
    assert callable(sml_EventParameterRanges.__init__)


def test_sml_eventparameterranges_constructor_args():
    sig = inspect.signature(sml_EventParameterRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml_smletypedelement_is_not_abstract():
    assert not inspect.isabstract(sml_SmlETypedElement)


def test_sml_smletypedelement_constructor_exists():
    assert callable(sml_SmlETypedElement.__init__)


def test_sml_smletypedelement_constructor_args():
    sig = inspect.signature(sml_SmlETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smletypedelement_has_name():
    assert hasattr(sml_SmlETypedElement, "name")
    descriptor = None
    for klass in sml_SmlETypedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_smleclass_is_not_abstract():
    assert not inspect.isabstract(sml_SmlEClass)


def test_sml_smleclass_constructor_exists():
    assert callable(sml_SmlEClass.__init__)


def test_sml_smleclass_constructor_args():
    sig = inspect.signature(sml_SmlEClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smleclass_has_name():
    assert hasattr(sml_SmlEClass, "name")
    descriptor = None
    for klass in sml_SmlEClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_smlepackage_is_not_abstract():
    assert not inspect.isabstract(sml_SmlEPackage)


def test_sml_smlepackage_constructor_exists():
    assert callable(sml_SmlEPackage.__init__)


def test_sml_smlepackage_constructor_args():
    sig = inspect.signature(sml_SmlEPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_smlepackage_has_name():
    assert hasattr(sml_SmlEPackage, "name")
    descriptor = None
    for klass in sml_SmlEPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml_import_is_not_abstract():
    assert not inspect.isabstract(sml_Import)


def test_sml_import_constructor_exists():
    assert callable(sml_Import.__init__)


def test_sml_import_constructor_args():
    sig = inspect.signature(sml_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_sml_import_has_importURI():
    assert hasattr(sml_Import, "importURI")
    descriptor = None
    for klass in sml_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_sml_specification_is_not_abstract():
    assert not inspect.isabstract(sml_Specification)


def test_sml_specification_constructor_exists():
    assert callable(sml_Specification.__init__)


def test_sml_specification_constructor_args():
    sig = inspect.signature(sml_Specification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml_specification_has_name():
    assert hasattr(sml_Specification, "name")
    descriptor = None
    for klass in sml_Specification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scenariokind_exists():
    # Check that the Enumeration exists
    assert ScenarioKind is not None

def test_scenariokind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScenarioKind]
    expected_literals = [
        "specification",
        "existential",
        "requirement",
        "assumption",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScenarioKind"

def test_collectionoperation_exists():
    # Check that the Enumeration exists
    assert CollectionOperation is not None

def test_collectionoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionOperation]
    expected_literals = [
        "containsAll",
        "isEmpty",
        "contains",
        "get",
        "any",
        "last",
        "first",
        "size",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionOperation"


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
sml_StructuralFeatureValue_strategy = st.builds(
    sml_StructuralFeatureValue,
)
sml_CollectionAccess_strategy = st.builds(
    sml_CollectionAccess,
    collectionOperation=
        safe_text
)
sml_Variable_strategy = st.builds(
    sml_Variable,
    name=
        safe_text
)
sml_Document_strategy = st.builds(
    sml_Document,
)
Value_strategy = st.builds(
    Value,
)
sml_EnumValue_strategy = st.builds(
    sml_EnumValue,
)
sml_BooleanValue_strategy = st.builds(
    sml_BooleanValue,
    value=
        st.booleans()
)
sml_StringValue_strategy = st.builds(
    sml_StringValue,
    value=
        safe_text
)
sml_NullValue_strategy = st.builds(
    sml_NullValue,
)
sml_IntegerValue_strategy = st.builds(
    sml_IntegerValue,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
sml_BinaryOperationExpression_strategy = st.builds(
    sml_BinaryOperationExpression,
    operator=
        safe_text
)
sml_UnaryOperationExpression_strategy = st.builds(
    sml_UnaryOperationExpression,
    operator=
        safe_text
)
sml_Value_strategy = st.builds(
    sml_Value,
)
VariableExpression_strategy = st.builds(
    VariableExpression,
)
sml_VariableAssignment_strategy = st.builds(
    sml_VariableAssignment,
)
sml_TypedVariableDeclaration_strategy = st.builds(
    sml_TypedVariableDeclaration,
    name=
        safe_text
)
sml_VariableDeclaration_strategy = st.builds(
    sml_VariableDeclaration,
    name=
        safe_text
)
ExpressionAndVariables_strategy = st.builds(
    ExpressionAndVariables,
)
sml_ExpressionOrRegion_strategy = st.builds(
    sml_ExpressionOrRegion,
)
ExpressionOrRegion_strategy = st.builds(
    ExpressionOrRegion,
)
sml_ExpressionAndVariables_strategy = st.builds(
    sml_ExpressionAndVariables,
)
sml_ExpressionRegion_strategy = st.builds(
    sml_ExpressionRegion,
)
sml_Message_strategy = st.builds(
    sml_Message,
)
Condition_strategy = st.builds(
    Condition,
)
sml_ViolationCondition_strategy = st.builds(
    sml_ViolationCondition,
)
sml_InterruptCondition_strategy = st.builds(
    sml_InterruptCondition,
)
sml_WaitCondition_strategy = st.builds(
    sml_WaitCondition,
    requested=
        st.booleans(),
    strict=
        st.booleans()
)
sml_ConditionExpression_strategy = st.builds(
    sml_ConditionExpression,
)
sml_LoopCondition_strategy = st.builds(
    sml_LoopCondition,
)
sml_CaseCondition_strategy = st.builds(
    sml_CaseCondition,
)
sml_Case_strategy = st.builds(
    sml_Case,
)
sml_VariableValue_strategy = st.builds(
    sml_VariableValue,
)
sml_Expression_strategy = st.builds(
    sml_Expression,
)
ParameterExpression_strategy = st.builds(
    ParameterExpression,
)
sml_VariableBindingParameter_strategy = st.builds(
    sml_VariableBindingParameter,
)
sml_ExpressionParameter_strategy = st.builds(
    sml_ExpressionParameter,
)
sml_RandomParameter_strategy = st.builds(
    sml_RandomParameter,
)
sml_ParameterExpression_strategy = st.builds(
    sml_ParameterExpression,
)
sml_ParameterBinding_strategy = st.builds(
    sml_ParameterBinding,
)
sml_ConstraintBlock_strategy = st.builds(
    sml_ConstraintBlock,
)
sml_VariableExpression_strategy = st.builds(
    sml_VariableExpression,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
sml_Condition_strategy = st.builds(
    sml_Condition,
)
sml_Alternative_strategy = st.builds(
    sml_Alternative,
)
sml_Parallel_strategy = st.builds(
    sml_Parallel,
)
sml_ModalMessage_strategy = st.builds(
    sml_ModalMessage,
    strict=
        st.booleans(),
    requested=
        st.booleans()
)
sml_Loop_strategy = st.builds(
    sml_Loop,
)
sml_VariableFragment_strategy = st.builds(
    sml_VariableFragment,
)
sml_InteractionFragment_strategy = st.builds(
    sml_InteractionFragment,
)
sml_FeatureAccess_strategy = st.builds(
    sml_FeatureAccess,
)
BindingExpression_strategy = st.builds(
    BindingExpression,
)
sml_FeatureAccessBindingExpression_strategy = st.builds(
    sml_FeatureAccessBindingExpression,
)
sml_BindingExpression_strategy = st.builds(
    sml_BindingExpression,
)
sml_Interaction_strategy = st.builds(
    sml_Interaction,
)
sml_RoleBindingConstraint_strategy = st.builds(
    sml_RoleBindingConstraint,
)
sml_SmlEStructuralFeature_strategy = st.builds(
    sml_SmlEStructuralFeature,
    name=
        safe_text
)
sml_SmlEClassifier_strategy = st.builds(
    sml_SmlEClassifier,
    name=
        safe_text
)
AbstractRanges_strategy = st.builds(
    AbstractRanges,
)
sml_StringRanges_strategy = st.builds(
    sml_StringRanges,
    values=
        safe_text
)
sml_EnumRanges_strategy = st.builds(
    sml_EnumRanges,
)
sml_IntegerRanges_strategy = st.builds(
    sml_IntegerRanges,
    values=
        st.integers(),
    min=
        st.integers(),
    max=
        st.integers()
)
sml_AbstractRanges_strategy = st.builds(
    sml_AbstractRanges,
)
sml_RangesForParameter_strategy = st.builds(
    sml_RangesForParameter,
)
sml_Scenario_strategy = st.builds(
    sml_Scenario,
    singular=
        st.booleans(),
    name=
        safe_text,
    kind=
        safe_text
)
sml_Role_strategy = st.builds(
    sml_Role,
    name=
        safe_text,
    static=
        st.booleans()
)
sml_SmlEEnumLiteral_strategy = st.builds(
    sml_SmlEEnumLiteral,
    name=
        safe_text
)
sml_SmlEEnum_strategy = st.builds(
    sml_SmlEEnum,
    name=
        safe_text
)
sml_Collaboration_strategy = st.builds(
    sml_Collaboration,
    name=
        safe_text
)
sml_EventParameterRanges_strategy = st.builds(
    sml_EventParameterRanges,
)
sml_SmlETypedElement_strategy = st.builds(
    sml_SmlETypedElement,
    name=
        safe_text
)
sml_SmlEClass_strategy = st.builds(
    sml_SmlEClass,
    name=
        safe_text
)
sml_SmlEPackage_strategy = st.builds(
    sml_SmlEPackage,
    name=
        safe_text
)
sml_Import_strategy = st.builds(
    sml_Import,
    importURI=
        safe_text
)
sml_Specification_strategy = st.builds(
    sml_Specification,
    name=
        safe_text
)

@given(instance=sml_StructuralFeatureValue_strategy)
@settings(max_examples=50)
def test_sml_structuralfeaturevalue_instantiation(instance):
    assert isinstance(instance, sml_StructuralFeatureValue)

@given(instance=sml_CollectionAccess_strategy)
@settings(max_examples=50)
def test_sml_collectionaccess_instantiation(instance):
    assert isinstance(instance, sml_CollectionAccess)



@given(instance=sml_CollectionAccess_strategy)
def test_sml_collectionaccess_collectionOperation_setter(instance):
    original = instance.collectionOperation
    instance.collectionOperation = original
    assert instance.collectionOperation == original

@given(instance=sml_Variable_strategy)
@settings(max_examples=50)
def test_sml_variable_instantiation(instance):
    assert isinstance(instance, sml_Variable)



@given(instance=sml_Variable_strategy)
def test_sml_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_Document_strategy)
@settings(max_examples=50)
def test_sml_document_instantiation(instance):
    assert isinstance(instance, sml_Document)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=sml_EnumValue_strategy)
@settings(max_examples=50)
def test_sml_enumvalue_instantiation(instance):
    assert isinstance(instance, sml_EnumValue)

@given(instance=sml_BooleanValue_strategy)
@settings(max_examples=50)
def test_sml_booleanvalue_instantiation(instance):
    assert isinstance(instance, sml_BooleanValue)



@given(instance=sml_BooleanValue_strategy)
def test_sml_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sml_StringValue_strategy)
@settings(max_examples=50)
def test_sml_stringvalue_instantiation(instance):
    assert isinstance(instance, sml_StringValue)



@given(instance=sml_StringValue_strategy)
def test_sml_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sml_NullValue_strategy)
@settings(max_examples=50)
def test_sml_nullvalue_instantiation(instance):
    assert isinstance(instance, sml_NullValue)

@given(instance=sml_IntegerValue_strategy)
@settings(max_examples=50)
def test_sml_integervalue_instantiation(instance):
    assert isinstance(instance, sml_IntegerValue)



@given(instance=sml_IntegerValue_strategy)
def test_sml_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sml_BinaryOperationExpression_strategy)
@settings(max_examples=50)
def test_sml_binaryoperationexpression_instantiation(instance):
    assert isinstance(instance, sml_BinaryOperationExpression)



@given(instance=sml_BinaryOperationExpression_strategy)
def test_sml_binaryoperationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sml_UnaryOperationExpression_strategy)
@settings(max_examples=50)
def test_sml_unaryoperationexpression_instantiation(instance):
    assert isinstance(instance, sml_UnaryOperationExpression)



@given(instance=sml_UnaryOperationExpression_strategy)
def test_sml_unaryoperationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sml_Value_strategy)
@settings(max_examples=50)
def test_sml_value_instantiation(instance):
    assert isinstance(instance, sml_Value)

@given(instance=VariableExpression_strategy)
@settings(max_examples=50)
def test_variableexpression_instantiation(instance):
    assert isinstance(instance, VariableExpression)

@given(instance=sml_VariableAssignment_strategy)
@settings(max_examples=50)
def test_sml_variableassignment_instantiation(instance):
    assert isinstance(instance, sml_VariableAssignment)

@given(instance=sml_TypedVariableDeclaration_strategy)
@settings(max_examples=50)
def test_sml_typedvariabledeclaration_instantiation(instance):
    assert isinstance(instance, sml_TypedVariableDeclaration)



@given(instance=sml_TypedVariableDeclaration_strategy)
def test_sml_typedvariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_sml_variabledeclaration_instantiation(instance):
    assert isinstance(instance, sml_VariableDeclaration)



@given(instance=sml_VariableDeclaration_strategy)
def test_sml_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExpressionAndVariables_strategy)
@settings(max_examples=50)
def test_expressionandvariables_instantiation(instance):
    assert isinstance(instance, ExpressionAndVariables)

@given(instance=sml_ExpressionOrRegion_strategy)
@settings(max_examples=50)
def test_sml_expressionorregion_instantiation(instance):
    assert isinstance(instance, sml_ExpressionOrRegion)

@given(instance=ExpressionOrRegion_strategy)
@settings(max_examples=50)
def test_expressionorregion_instantiation(instance):
    assert isinstance(instance, ExpressionOrRegion)

@given(instance=sml_ExpressionAndVariables_strategy)
@settings(max_examples=50)
def test_sml_expressionandvariables_instantiation(instance):
    assert isinstance(instance, sml_ExpressionAndVariables)

@given(instance=sml_ExpressionRegion_strategy)
@settings(max_examples=50)
def test_sml_expressionregion_instantiation(instance):
    assert isinstance(instance, sml_ExpressionRegion)

@given(instance=sml_Message_strategy)
@settings(max_examples=50)
def test_sml_message_instantiation(instance):
    assert isinstance(instance, sml_Message)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sml_ViolationCondition_strategy)
@settings(max_examples=50)
def test_sml_violationcondition_instantiation(instance):
    assert isinstance(instance, sml_ViolationCondition)

@given(instance=sml_InterruptCondition_strategy)
@settings(max_examples=50)
def test_sml_interruptcondition_instantiation(instance):
    assert isinstance(instance, sml_InterruptCondition)

@given(instance=sml_WaitCondition_strategy)
@settings(max_examples=50)
def test_sml_waitcondition_instantiation(instance):
    assert isinstance(instance, sml_WaitCondition)



@given(instance=sml_WaitCondition_strategy)
def test_sml_waitcondition_requested_setter(instance):
    original = instance.requested
    instance.requested = original
    assert instance.requested == original



@given(instance=sml_WaitCondition_strategy)
def test_sml_waitcondition_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=sml_ConditionExpression_strategy)
@settings(max_examples=50)
def test_sml_conditionexpression_instantiation(instance):
    assert isinstance(instance, sml_ConditionExpression)

@given(instance=sml_LoopCondition_strategy)
@settings(max_examples=50)
def test_sml_loopcondition_instantiation(instance):
    assert isinstance(instance, sml_LoopCondition)

@given(instance=sml_CaseCondition_strategy)
@settings(max_examples=50)
def test_sml_casecondition_instantiation(instance):
    assert isinstance(instance, sml_CaseCondition)

@given(instance=sml_Case_strategy)
@settings(max_examples=50)
def test_sml_case_instantiation(instance):
    assert isinstance(instance, sml_Case)

@given(instance=sml_VariableValue_strategy)
@settings(max_examples=50)
def test_sml_variablevalue_instantiation(instance):
    assert isinstance(instance, sml_VariableValue)

@given(instance=sml_Expression_strategy)
@settings(max_examples=50)
def test_sml_expression_instantiation(instance):
    assert isinstance(instance, sml_Expression)

@given(instance=ParameterExpression_strategy)
@settings(max_examples=50)
def test_parameterexpression_instantiation(instance):
    assert isinstance(instance, ParameterExpression)

@given(instance=sml_VariableBindingParameter_strategy)
@settings(max_examples=50)
def test_sml_variablebindingparameter_instantiation(instance):
    assert isinstance(instance, sml_VariableBindingParameter)

@given(instance=sml_ExpressionParameter_strategy)
@settings(max_examples=50)
def test_sml_expressionparameter_instantiation(instance):
    assert isinstance(instance, sml_ExpressionParameter)

@given(instance=sml_RandomParameter_strategy)
@settings(max_examples=50)
def test_sml_randomparameter_instantiation(instance):
    assert isinstance(instance, sml_RandomParameter)

@given(instance=sml_ParameterExpression_strategy)
@settings(max_examples=50)
def test_sml_parameterexpression_instantiation(instance):
    assert isinstance(instance, sml_ParameterExpression)

@given(instance=sml_ParameterBinding_strategy)
@settings(max_examples=50)
def test_sml_parameterbinding_instantiation(instance):
    assert isinstance(instance, sml_ParameterBinding)

@given(instance=sml_ConstraintBlock_strategy)
@settings(max_examples=50)
def test_sml_constraintblock_instantiation(instance):
    assert isinstance(instance, sml_ConstraintBlock)

@given(instance=sml_VariableExpression_strategy)
@settings(max_examples=50)
def test_sml_variableexpression_instantiation(instance):
    assert isinstance(instance, sml_VariableExpression)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=sml_Condition_strategy)
@settings(max_examples=50)
def test_sml_condition_instantiation(instance):
    assert isinstance(instance, sml_Condition)

@given(instance=sml_Alternative_strategy)
@settings(max_examples=50)
def test_sml_alternative_instantiation(instance):
    assert isinstance(instance, sml_Alternative)

@given(instance=sml_Parallel_strategy)
@settings(max_examples=50)
def test_sml_parallel_instantiation(instance):
    assert isinstance(instance, sml_Parallel)

@given(instance=sml_ModalMessage_strategy)
@settings(max_examples=50)
def test_sml_modalmessage_instantiation(instance):
    assert isinstance(instance, sml_ModalMessage)



@given(instance=sml_ModalMessage_strategy)
def test_sml_modalmessage_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original



@given(instance=sml_ModalMessage_strategy)
def test_sml_modalmessage_requested_setter(instance):
    original = instance.requested
    instance.requested = original
    assert instance.requested == original

@given(instance=sml_Loop_strategy)
@settings(max_examples=50)
def test_sml_loop_instantiation(instance):
    assert isinstance(instance, sml_Loop)

@given(instance=sml_VariableFragment_strategy)
@settings(max_examples=50)
def test_sml_variablefragment_instantiation(instance):
    assert isinstance(instance, sml_VariableFragment)

@given(instance=sml_InteractionFragment_strategy)
@settings(max_examples=50)
def test_sml_interactionfragment_instantiation(instance):
    assert isinstance(instance, sml_InteractionFragment)

@given(instance=sml_FeatureAccess_strategy)
@settings(max_examples=50)
def test_sml_featureaccess_instantiation(instance):
    assert isinstance(instance, sml_FeatureAccess)

@given(instance=BindingExpression_strategy)
@settings(max_examples=50)
def test_bindingexpression_instantiation(instance):
    assert isinstance(instance, BindingExpression)

@given(instance=sml_FeatureAccessBindingExpression_strategy)
@settings(max_examples=50)
def test_sml_featureaccessbindingexpression_instantiation(instance):
    assert isinstance(instance, sml_FeatureAccessBindingExpression)

@given(instance=sml_BindingExpression_strategy)
@settings(max_examples=50)
def test_sml_bindingexpression_instantiation(instance):
    assert isinstance(instance, sml_BindingExpression)

@given(instance=sml_Interaction_strategy)
@settings(max_examples=50)
def test_sml_interaction_instantiation(instance):
    assert isinstance(instance, sml_Interaction)

@given(instance=sml_RoleBindingConstraint_strategy)
@settings(max_examples=50)
def test_sml_rolebindingconstraint_instantiation(instance):
    assert isinstance(instance, sml_RoleBindingConstraint)

@given(instance=sml_SmlEStructuralFeature_strategy)
@settings(max_examples=50)
def test_sml_smlestructuralfeature_instantiation(instance):
    assert isinstance(instance, sml_SmlEStructuralFeature)



@given(instance=sml_SmlEStructuralFeature_strategy)
def test_sml_smlestructuralfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_SmlEClassifier_strategy)
@settings(max_examples=50)
def test_sml_smleclassifier_instantiation(instance):
    assert isinstance(instance, sml_SmlEClassifier)



@given(instance=sml_SmlEClassifier_strategy)
def test_sml_smleclassifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractRanges_strategy)
@settings(max_examples=50)
def test_abstractranges_instantiation(instance):
    assert isinstance(instance, AbstractRanges)

@given(instance=sml_StringRanges_strategy)
@settings(max_examples=50)
def test_sml_stringranges_instantiation(instance):
    assert isinstance(instance, sml_StringRanges)



@given(instance=sml_StringRanges_strategy)
def test_sml_stringranges_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=sml_EnumRanges_strategy)
@settings(max_examples=50)
def test_sml_enumranges_instantiation(instance):
    assert isinstance(instance, sml_EnumRanges)

@given(instance=sml_IntegerRanges_strategy)
@settings(max_examples=50)
def test_sml_integerranges_instantiation(instance):
    assert isinstance(instance, sml_IntegerRanges)



@given(instance=sml_IntegerRanges_strategy)
def test_sml_integerranges_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=sml_IntegerRanges_strategy)
def test_sml_integerranges_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=sml_IntegerRanges_strategy)
def test_sml_integerranges_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=sml_AbstractRanges_strategy)
@settings(max_examples=50)
def test_sml_abstractranges_instantiation(instance):
    assert isinstance(instance, sml_AbstractRanges)

@given(instance=sml_RangesForParameter_strategy)
@settings(max_examples=50)
def test_sml_rangesforparameter_instantiation(instance):
    assert isinstance(instance, sml_RangesForParameter)

@given(instance=sml_Scenario_strategy)
@settings(max_examples=50)
def test_sml_scenario_instantiation(instance):
    assert isinstance(instance, sml_Scenario)



@given(instance=sml_Scenario_strategy)
def test_sml_scenario_singular_setter(instance):
    original = instance.singular
    instance.singular = original
    assert instance.singular == original



@given(instance=sml_Scenario_strategy)
def test_sml_scenario_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sml_Scenario_strategy)
def test_sml_scenario_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sml_Role_strategy)
@settings(max_examples=50)
def test_sml_role_instantiation(instance):
    assert isinstance(instance, sml_Role)



@given(instance=sml_Role_strategy)
def test_sml_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sml_Role_strategy)
def test_sml_role_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=sml_SmlEEnumLiteral_strategy)
@settings(max_examples=50)
def test_sml_smleenumliteral_instantiation(instance):
    assert isinstance(instance, sml_SmlEEnumLiteral)



@given(instance=sml_SmlEEnumLiteral_strategy)
def test_sml_smleenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_SmlEEnum_strategy)
@settings(max_examples=50)
def test_sml_smleenum_instantiation(instance):
    assert isinstance(instance, sml_SmlEEnum)



@given(instance=sml_SmlEEnum_strategy)
def test_sml_smleenum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_Collaboration_strategy)
@settings(max_examples=50)
def test_sml_collaboration_instantiation(instance):
    assert isinstance(instance, sml_Collaboration)



@given(instance=sml_Collaboration_strategy)
def test_sml_collaboration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_EventParameterRanges_strategy)
@settings(max_examples=50)
def test_sml_eventparameterranges_instantiation(instance):
    assert isinstance(instance, sml_EventParameterRanges)

@given(instance=sml_SmlETypedElement_strategy)
@settings(max_examples=50)
def test_sml_smletypedelement_instantiation(instance):
    assert isinstance(instance, sml_SmlETypedElement)



@given(instance=sml_SmlETypedElement_strategy)
def test_sml_smletypedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_SmlEClass_strategy)
@settings(max_examples=50)
def test_sml_smleclass_instantiation(instance):
    assert isinstance(instance, sml_SmlEClass)



@given(instance=sml_SmlEClass_strategy)
def test_sml_smleclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_SmlEPackage_strategy)
@settings(max_examples=50)
def test_sml_smlepackage_instantiation(instance):
    assert isinstance(instance, sml_SmlEPackage)



@given(instance=sml_SmlEPackage_strategy)
def test_sml_smlepackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml_Import_strategy)
@settings(max_examples=50)
def test_sml_import_instantiation(instance):
    assert isinstance(instance, sml_Import)



@given(instance=sml_Import_strategy)
def test_sml_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=sml_Specification_strategy)
@settings(max_examples=50)
def test_sml_specification_instantiation(instance):
    assert isinstance(instance, sml_Specification)



@given(instance=sml_Specification_strategy)
def test_sml_specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
