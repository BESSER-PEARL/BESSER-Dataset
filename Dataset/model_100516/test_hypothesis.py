import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sml::StructuralFeatureValue,
    sml::CollectionAccess,
    sml::Variable,
    sml::Document,
    Value,
    sml::EnumValue,
    sml::NullValue,
    sml::StringValue,
    sml::BooleanValue,
    sml::IntegerValue,
    Expression,
    sml::BinaryOperationExpression,
    sml::UnaryOperationExpression,
    sml::Value,
    VariableExpression,
    sml::VariableAssignment,
    sml::TypedVariableDeclaration,
    sml::VariableDeclaration,
    ExpressionAndVariables,
    sml::ExpressionOrRegion,
    ExpressionOrRegion,
    sml::ExpressionAndVariables,
    sml::ExpressionRegion,
    sml::Message,
    Condition,
    sml::InterruptCondition,
    sml::ViolationCondition,
    sml::WaitCondition,
    sml::ConditionExpression,
    sml::LoopCondition,
    sml::CaseCondition,
    sml::Case,
    sml::VariableValue,
    sml::Expression,
    ParameterExpression,
    sml::ExpressionParameter,
    sml::VariableBindingParameter,
    sml::RandomParameter,
    sml::ParameterExpression,
    sml::ParameterBinding,
    sml::ConstraintBlock,
    sml::VariableExpression,
    InteractionFragment,
    sml::Condition,
    sml::Loop,
    sml::Alternative,
    sml::ModalMessage,
    sml::Parallel,
    sml::VariableFragment,
    sml::InteractionFragment,
    sml::FeatureAccess,
    BindingExpression,
    sml::FeatureAccessBindingExpression,
    sml::BindingExpression,
    sml::Interaction,
    sml::RoleBindingConstraint,
    sml::SmlEStructuralFeature,
    sml::SmlEClassifier,
    AbstractRanges,
    sml::StringRanges,
    sml::EnumRanges,
    sml::IntegerRanges,
    sml::AbstractRanges,
    sml::RangesForParameter,
    sml::Scenario,
    sml::Role,
    sml::SmlEEnumLiteral,
    sml::SmlEEnum,
    sml::Collaboration,
    sml::EventParameterRanges,
    sml::SmlETypedElement,
    sml::SmlEClass,
    sml::SmlEPackage,
    sml::Import,
    sml::Specification,
    CollectionOperation,
    ScenarioKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sml::structuralfeaturevalue_is_not_abstract():
    assert not inspect.isabstract(sml::StructuralFeatureValue)


def test_sml::structuralfeaturevalue_constructor_exists():
    assert callable(sml::StructuralFeatureValue.__init__)


def test_sml::structuralfeaturevalue_constructor_args():
    sig = inspect.signature(sml::StructuralFeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_sml::collectionaccess_is_not_abstract():
    assert not inspect.isabstract(sml::CollectionAccess)


def test_sml::collectionaccess_constructor_exists():
    assert callable(sml::CollectionAccess.__init__)


def test_sml::collectionaccess_constructor_args():
    sig = inspect.signature(sml::CollectionAccess.__init__)
    params = list(sig.parameters.keys())
    assert "collectionOperation" in params, "Missing parameter 'collectionOperation'"

def test_sml::collectionaccess_has_collectionOperation():
    assert hasattr(sml::CollectionAccess, "collectionOperation")
    descriptor = None
    for klass in sml::CollectionAccess.__mro__:
        if "collectionOperation" in klass.__dict__:
            descriptor = klass.__dict__["collectionOperation"]
            break
    assert isinstance(descriptor, property)



def test_sml::variable_is_not_abstract():
    assert not inspect.isabstract(sml::Variable)


def test_sml::variable_constructor_exists():
    assert callable(sml::Variable.__init__)


def test_sml::variable_constructor_args():
    sig = inspect.signature(sml::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::variable_has_name():
    assert hasattr(sml::Variable, "name")
    descriptor = None
    for klass in sml::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::document_is_not_abstract():
    assert not inspect.isabstract(sml::Document)


def test_sml::document_constructor_exists():
    assert callable(sml::Document.__init__)


def test_sml::document_constructor_args():
    sig = inspect.signature(sml::Document.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_sml::enumvalue_is_not_abstract():
    assert not inspect.isabstract(sml::EnumValue)


def test_sml::enumvalue_constructor_exists():
    assert callable(sml::EnumValue.__init__)


def test_sml::enumvalue_constructor_args():
    sig = inspect.signature(sml::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_sml::nullvalue_is_not_abstract():
    assert not inspect.isabstract(sml::NullValue)


def test_sml::nullvalue_constructor_exists():
    assert callable(sml::NullValue.__init__)


def test_sml::nullvalue_constructor_args():
    sig = inspect.signature(sml::NullValue.__init__)
    params = list(sig.parameters.keys())



def test_sml::stringvalue_is_not_abstract():
    assert not inspect.isabstract(sml::StringValue)


def test_sml::stringvalue_constructor_exists():
    assert callable(sml::StringValue.__init__)


def test_sml::stringvalue_constructor_args():
    sig = inspect.signature(sml::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sml::stringvalue_has_value():
    assert hasattr(sml::StringValue, "value")
    descriptor = None
    for klass in sml::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sml::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(sml::BooleanValue)


def test_sml::booleanvalue_constructor_exists():
    assert callable(sml::BooleanValue.__init__)


def test_sml::booleanvalue_constructor_args():
    sig = inspect.signature(sml::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sml::booleanvalue_has_value():
    assert hasattr(sml::BooleanValue, "value")
    descriptor = None
    for klass in sml::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sml::integervalue_is_not_abstract():
    assert not inspect.isabstract(sml::IntegerValue)


def test_sml::integervalue_constructor_exists():
    assert callable(sml::IntegerValue.__init__)


def test_sml::integervalue_constructor_args():
    sig = inspect.signature(sml::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sml::integervalue_has_value():
    assert hasattr(sml::IntegerValue, "value")
    descriptor = None
    for klass in sml::IntegerValue.__mro__:
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



def test_sml::binaryoperationexpression_is_not_abstract():
    assert not inspect.isabstract(sml::BinaryOperationExpression)


def test_sml::binaryoperationexpression_constructor_exists():
    assert callable(sml::BinaryOperationExpression.__init__)


def test_sml::binaryoperationexpression_constructor_args():
    sig = inspect.signature(sml::BinaryOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sml::binaryoperationexpression_has_operator():
    assert hasattr(sml::BinaryOperationExpression, "operator")
    descriptor = None
    for klass in sml::BinaryOperationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sml::unaryoperationexpression_is_not_abstract():
    assert not inspect.isabstract(sml::UnaryOperationExpression)


def test_sml::unaryoperationexpression_constructor_exists():
    assert callable(sml::UnaryOperationExpression.__init__)


def test_sml::unaryoperationexpression_constructor_args():
    sig = inspect.signature(sml::UnaryOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sml::unaryoperationexpression_has_operator():
    assert hasattr(sml::UnaryOperationExpression, "operator")
    descriptor = None
    for klass in sml::UnaryOperationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sml::value_is_not_abstract():
    assert not inspect.isabstract(sml::Value)


def test_sml::value_constructor_exists():
    assert callable(sml::Value.__init__)


def test_sml::value_constructor_args():
    sig = inspect.signature(sml::Value.__init__)
    params = list(sig.parameters.keys())



def test_variableexpression_is_not_abstract():
    assert not inspect.isabstract(VariableExpression)


def test_variableexpression_constructor_exists():
    assert callable(VariableExpression.__init__)


def test_variableexpression_constructor_args():
    sig = inspect.signature(VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::variableassignment_is_not_abstract():
    assert not inspect.isabstract(sml::VariableAssignment)


def test_sml::variableassignment_constructor_exists():
    assert callable(sml::VariableAssignment.__init__)


def test_sml::variableassignment_constructor_args():
    sig = inspect.signature(sml::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_sml::typedvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(sml::TypedVariableDeclaration)


def test_sml::typedvariabledeclaration_constructor_exists():
    assert callable(sml::TypedVariableDeclaration.__init__)


def test_sml::typedvariabledeclaration_constructor_args():
    sig = inspect.signature(sml::TypedVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::typedvariabledeclaration_has_name():
    assert hasattr(sml::TypedVariableDeclaration, "name")
    descriptor = None
    for klass in sml::TypedVariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(sml::VariableDeclaration)


def test_sml::variabledeclaration_constructor_exists():
    assert callable(sml::VariableDeclaration.__init__)


def test_sml::variabledeclaration_constructor_args():
    sig = inspect.signature(sml::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::variabledeclaration_has_name():
    assert hasattr(sml::VariableDeclaration, "name")
    descriptor = None
    for klass in sml::VariableDeclaration.__mro__:
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



def test_sml::expressionorregion_is_not_abstract():
    assert not inspect.isabstract(sml::ExpressionOrRegion)


def test_sml::expressionorregion_constructor_exists():
    assert callable(sml::ExpressionOrRegion.__init__)


def test_sml::expressionorregion_constructor_args():
    sig = inspect.signature(sml::ExpressionOrRegion.__init__)
    params = list(sig.parameters.keys())



def test_expressionorregion_is_not_abstract():
    assert not inspect.isabstract(ExpressionOrRegion)


def test_expressionorregion_constructor_exists():
    assert callable(ExpressionOrRegion.__init__)


def test_expressionorregion_constructor_args():
    sig = inspect.signature(ExpressionOrRegion.__init__)
    params = list(sig.parameters.keys())



def test_sml::expressionandvariables_is_not_abstract():
    assert not inspect.isabstract(sml::ExpressionAndVariables)


def test_sml::expressionandvariables_constructor_exists():
    assert callable(sml::ExpressionAndVariables.__init__)


def test_sml::expressionandvariables_constructor_args():
    sig = inspect.signature(sml::ExpressionAndVariables.__init__)
    params = list(sig.parameters.keys())



def test_sml::expressionregion_is_not_abstract():
    assert not inspect.isabstract(sml::ExpressionRegion)


def test_sml::expressionregion_constructor_exists():
    assert callable(sml::ExpressionRegion.__init__)


def test_sml::expressionregion_constructor_args():
    sig = inspect.signature(sml::ExpressionRegion.__init__)
    params = list(sig.parameters.keys())



def test_sml::message_is_not_abstract():
    assert not inspect.isabstract(sml::Message)


def test_sml::message_constructor_exists():
    assert callable(sml::Message.__init__)


def test_sml::message_constructor_args():
    sig = inspect.signature(sml::Message.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sml::interruptcondition_is_not_abstract():
    assert not inspect.isabstract(sml::InterruptCondition)


def test_sml::interruptcondition_constructor_exists():
    assert callable(sml::InterruptCondition.__init__)


def test_sml::interruptcondition_constructor_args():
    sig = inspect.signature(sml::InterruptCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml::violationcondition_is_not_abstract():
    assert not inspect.isabstract(sml::ViolationCondition)


def test_sml::violationcondition_constructor_exists():
    assert callable(sml::ViolationCondition.__init__)


def test_sml::violationcondition_constructor_args():
    sig = inspect.signature(sml::ViolationCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml::waitcondition_is_not_abstract():
    assert not inspect.isabstract(sml::WaitCondition)


def test_sml::waitcondition_constructor_exists():
    assert callable(sml::WaitCondition.__init__)


def test_sml::waitcondition_constructor_args():
    sig = inspect.signature(sml::WaitCondition.__init__)
    params = list(sig.parameters.keys())
    assert "requested" in params, "Missing parameter 'requested'"
    assert "strict" in params, "Missing parameter 'strict'"

def test_sml::waitcondition_has_requested():
    assert hasattr(sml::WaitCondition, "requested")
    descriptor = None
    for klass in sml::WaitCondition.__mro__:
        if "requested" in klass.__dict__:
            descriptor = klass.__dict__["requested"]
            break
    assert isinstance(descriptor, property)

def test_sml::waitcondition_has_strict():
    assert hasattr(sml::WaitCondition, "strict")
    descriptor = None
    for klass in sml::WaitCondition.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_sml::conditionexpression_is_not_abstract():
    assert not inspect.isabstract(sml::ConditionExpression)


def test_sml::conditionexpression_constructor_exists():
    assert callable(sml::ConditionExpression.__init__)


def test_sml::conditionexpression_constructor_args():
    sig = inspect.signature(sml::ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::loopcondition_is_not_abstract():
    assert not inspect.isabstract(sml::LoopCondition)


def test_sml::loopcondition_constructor_exists():
    assert callable(sml::LoopCondition.__init__)


def test_sml::loopcondition_constructor_args():
    sig = inspect.signature(sml::LoopCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml::casecondition_is_not_abstract():
    assert not inspect.isabstract(sml::CaseCondition)


def test_sml::casecondition_constructor_exists():
    assert callable(sml::CaseCondition.__init__)


def test_sml::casecondition_constructor_args():
    sig = inspect.signature(sml::CaseCondition.__init__)
    params = list(sig.parameters.keys())



def test_sml::case_is_not_abstract():
    assert not inspect.isabstract(sml::Case)


def test_sml::case_constructor_exists():
    assert callable(sml::Case.__init__)


def test_sml::case_constructor_args():
    sig = inspect.signature(sml::Case.__init__)
    params = list(sig.parameters.keys())



def test_sml::variablevalue_is_not_abstract():
    assert not inspect.isabstract(sml::VariableValue)


def test_sml::variablevalue_constructor_exists():
    assert callable(sml::VariableValue.__init__)


def test_sml::variablevalue_constructor_args():
    sig = inspect.signature(sml::VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_sml::expression_is_not_abstract():
    assert not inspect.isabstract(sml::Expression)


def test_sml::expression_constructor_exists():
    assert callable(sml::Expression.__init__)


def test_sml::expression_constructor_args():
    sig = inspect.signature(sml::Expression.__init__)
    params = list(sig.parameters.keys())



def test_parameterexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterExpression)


def test_parameterexpression_constructor_exists():
    assert callable(ParameterExpression.__init__)


def test_parameterexpression_constructor_args():
    sig = inspect.signature(ParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::expressionparameter_is_not_abstract():
    assert not inspect.isabstract(sml::ExpressionParameter)


def test_sml::expressionparameter_constructor_exists():
    assert callable(sml::ExpressionParameter.__init__)


def test_sml::expressionparameter_constructor_args():
    sig = inspect.signature(sml::ExpressionParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml::variablebindingparameter_is_not_abstract():
    assert not inspect.isabstract(sml::VariableBindingParameter)


def test_sml::variablebindingparameter_constructor_exists():
    assert callable(sml::VariableBindingParameter.__init__)


def test_sml::variablebindingparameter_constructor_args():
    sig = inspect.signature(sml::VariableBindingParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml::randomparameter_is_not_abstract():
    assert not inspect.isabstract(sml::RandomParameter)


def test_sml::randomparameter_constructor_exists():
    assert callable(sml::RandomParameter.__init__)


def test_sml::randomparameter_constructor_args():
    sig = inspect.signature(sml::RandomParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml::parameterexpression_is_not_abstract():
    assert not inspect.isabstract(sml::ParameterExpression)


def test_sml::parameterexpression_constructor_exists():
    assert callable(sml::ParameterExpression.__init__)


def test_sml::parameterexpression_constructor_args():
    sig = inspect.signature(sml::ParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::parameterbinding_is_not_abstract():
    assert not inspect.isabstract(sml::ParameterBinding)


def test_sml::parameterbinding_constructor_exists():
    assert callable(sml::ParameterBinding.__init__)


def test_sml::parameterbinding_constructor_args():
    sig = inspect.signature(sml::ParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_sml::constraintblock_is_not_abstract():
    assert not inspect.isabstract(sml::ConstraintBlock)


def test_sml::constraintblock_constructor_exists():
    assert callable(sml::ConstraintBlock.__init__)


def test_sml::constraintblock_constructor_args():
    sig = inspect.signature(sml::ConstraintBlock.__init__)
    params = list(sig.parameters.keys())



def test_sml::variableexpression_is_not_abstract():
    assert not inspect.isabstract(sml::VariableExpression)


def test_sml::variableexpression_constructor_exists():
    assert callable(sml::VariableExpression.__init__)


def test_sml::variableexpression_constructor_args():
    sig = inspect.signature(sml::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_sml::condition_is_not_abstract():
    assert not inspect.isabstract(sml::Condition)


def test_sml::condition_constructor_exists():
    assert callable(sml::Condition.__init__)


def test_sml::condition_constructor_args():
    sig = inspect.signature(sml::Condition.__init__)
    params = list(sig.parameters.keys())



def test_sml::loop_is_not_abstract():
    assert not inspect.isabstract(sml::Loop)


def test_sml::loop_constructor_exists():
    assert callable(sml::Loop.__init__)


def test_sml::loop_constructor_args():
    sig = inspect.signature(sml::Loop.__init__)
    params = list(sig.parameters.keys())



def test_sml::alternative_is_not_abstract():
    assert not inspect.isabstract(sml::Alternative)


def test_sml::alternative_constructor_exists():
    assert callable(sml::Alternative.__init__)


def test_sml::alternative_constructor_args():
    sig = inspect.signature(sml::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_sml::modalmessage_is_not_abstract():
    assert not inspect.isabstract(sml::ModalMessage)


def test_sml::modalmessage_constructor_exists():
    assert callable(sml::ModalMessage.__init__)


def test_sml::modalmessage_constructor_args():
    sig = inspect.signature(sml::ModalMessage.__init__)
    params = list(sig.parameters.keys())
    assert "requested" in params, "Missing parameter 'requested'"
    assert "strict" in params, "Missing parameter 'strict'"

def test_sml::modalmessage_has_requested():
    assert hasattr(sml::ModalMessage, "requested")
    descriptor = None
    for klass in sml::ModalMessage.__mro__:
        if "requested" in klass.__dict__:
            descriptor = klass.__dict__["requested"]
            break
    assert isinstance(descriptor, property)

def test_sml::modalmessage_has_strict():
    assert hasattr(sml::ModalMessage, "strict")
    descriptor = None
    for klass in sml::ModalMessage.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_sml::parallel_is_not_abstract():
    assert not inspect.isabstract(sml::Parallel)


def test_sml::parallel_constructor_exists():
    assert callable(sml::Parallel.__init__)


def test_sml::parallel_constructor_args():
    sig = inspect.signature(sml::Parallel.__init__)
    params = list(sig.parameters.keys())



def test_sml::variablefragment_is_not_abstract():
    assert not inspect.isabstract(sml::VariableFragment)


def test_sml::variablefragment_constructor_exists():
    assert callable(sml::VariableFragment.__init__)


def test_sml::variablefragment_constructor_args():
    sig = inspect.signature(sml::VariableFragment.__init__)
    params = list(sig.parameters.keys())



def test_sml::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(sml::InteractionFragment)


def test_sml::interactionfragment_constructor_exists():
    assert callable(sml::InteractionFragment.__init__)


def test_sml::interactionfragment_constructor_args():
    sig = inspect.signature(sml::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_sml::featureaccess_is_not_abstract():
    assert not inspect.isabstract(sml::FeatureAccess)


def test_sml::featureaccess_constructor_exists():
    assert callable(sml::FeatureAccess.__init__)


def test_sml::featureaccess_constructor_args():
    sig = inspect.signature(sml::FeatureAccess.__init__)
    params = list(sig.parameters.keys())



def test_bindingexpression_is_not_abstract():
    assert not inspect.isabstract(BindingExpression)


def test_bindingexpression_constructor_exists():
    assert callable(BindingExpression.__init__)


def test_bindingexpression_constructor_args():
    sig = inspect.signature(BindingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::featureaccessbindingexpression_is_not_abstract():
    assert not inspect.isabstract(sml::FeatureAccessBindingExpression)


def test_sml::featureaccessbindingexpression_constructor_exists():
    assert callable(sml::FeatureAccessBindingExpression.__init__)


def test_sml::featureaccessbindingexpression_constructor_args():
    sig = inspect.signature(sml::FeatureAccessBindingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::bindingexpression_is_not_abstract():
    assert not inspect.isabstract(sml::BindingExpression)


def test_sml::bindingexpression_constructor_exists():
    assert callable(sml::BindingExpression.__init__)


def test_sml::bindingexpression_constructor_args():
    sig = inspect.signature(sml::BindingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sml::interaction_is_not_abstract():
    assert not inspect.isabstract(sml::Interaction)


def test_sml::interaction_constructor_exists():
    assert callable(sml::Interaction.__init__)


def test_sml::interaction_constructor_args():
    sig = inspect.signature(sml::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_sml::rolebindingconstraint_is_not_abstract():
    assert not inspect.isabstract(sml::RoleBindingConstraint)


def test_sml::rolebindingconstraint_constructor_exists():
    assert callable(sml::RoleBindingConstraint.__init__)


def test_sml::rolebindingconstraint_constructor_args():
    sig = inspect.signature(sml::RoleBindingConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sml::smlestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(sml::SmlEStructuralFeature)


def test_sml::smlestructuralfeature_constructor_exists():
    assert callable(sml::SmlEStructuralFeature.__init__)


def test_sml::smlestructuralfeature_constructor_args():
    sig = inspect.signature(sml::SmlEStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smlestructuralfeature_has_name():
    assert hasattr(sml::SmlEStructuralFeature, "name")
    descriptor = None
    for klass in sml::SmlEStructuralFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::smleclassifier_is_not_abstract():
    assert not inspect.isabstract(sml::SmlEClassifier)


def test_sml::smleclassifier_constructor_exists():
    assert callable(sml::SmlEClassifier.__init__)


def test_sml::smleclassifier_constructor_args():
    sig = inspect.signature(sml::SmlEClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smleclassifier_has_name():
    assert hasattr(sml::SmlEClassifier, "name")
    descriptor = None
    for klass in sml::SmlEClassifier.__mro__:
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



def test_sml::stringranges_is_not_abstract():
    assert not inspect.isabstract(sml::StringRanges)


def test_sml::stringranges_constructor_exists():
    assert callable(sml::StringRanges.__init__)


def test_sml::stringranges_constructor_args():
    sig = inspect.signature(sml::StringRanges.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_sml::stringranges_has_values():
    assert hasattr(sml::StringRanges, "values")
    descriptor = None
    for klass in sml::StringRanges.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_sml::enumranges_is_not_abstract():
    assert not inspect.isabstract(sml::EnumRanges)


def test_sml::enumranges_constructor_exists():
    assert callable(sml::EnumRanges.__init__)


def test_sml::enumranges_constructor_args():
    sig = inspect.signature(sml::EnumRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml::integerranges_is_not_abstract():
    assert not inspect.isabstract(sml::IntegerRanges)


def test_sml::integerranges_constructor_exists():
    assert callable(sml::IntegerRanges.__init__)


def test_sml::integerranges_constructor_args():
    sig = inspect.signature(sml::IntegerRanges.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_sml::integerranges_has_values():
    assert hasattr(sml::IntegerRanges, "values")
    descriptor = None
    for klass in sml::IntegerRanges.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_sml::integerranges_has_min():
    assert hasattr(sml::IntegerRanges, "min")
    descriptor = None
    for klass in sml::IntegerRanges.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_sml::integerranges_has_max():
    assert hasattr(sml::IntegerRanges, "max")
    descriptor = None
    for klass in sml::IntegerRanges.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_sml::abstractranges_is_not_abstract():
    assert not inspect.isabstract(sml::AbstractRanges)


def test_sml::abstractranges_constructor_exists():
    assert callable(sml::AbstractRanges.__init__)


def test_sml::abstractranges_constructor_args():
    sig = inspect.signature(sml::AbstractRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml::rangesforparameter_is_not_abstract():
    assert not inspect.isabstract(sml::RangesForParameter)


def test_sml::rangesforparameter_constructor_exists():
    assert callable(sml::RangesForParameter.__init__)


def test_sml::rangesforparameter_constructor_args():
    sig = inspect.signature(sml::RangesForParameter.__init__)
    params = list(sig.parameters.keys())



def test_sml::scenario_is_not_abstract():
    assert not inspect.isabstract(sml::Scenario)


def test_sml::scenario_constructor_exists():
    assert callable(sml::Scenario.__init__)


def test_sml::scenario_constructor_args():
    sig = inspect.signature(sml::Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "singular" in params, "Missing parameter 'singular'"

def test_sml::scenario_has_kind():
    assert hasattr(sml::Scenario, "kind")
    descriptor = None
    for klass in sml::Scenario.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_sml::scenario_has_name():
    assert hasattr(sml::Scenario, "name")
    descriptor = None
    for klass in sml::Scenario.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sml::scenario_has_singular():
    assert hasattr(sml::Scenario, "singular")
    descriptor = None
    for klass in sml::Scenario.__mro__:
        if "singular" in klass.__dict__:
            descriptor = klass.__dict__["singular"]
            break
    assert isinstance(descriptor, property)



def test_sml::role_is_not_abstract():
    assert not inspect.isabstract(sml::Role)


def test_sml::role_constructor_exists():
    assert callable(sml::Role.__init__)


def test_sml::role_constructor_args():
    sig = inspect.signature(sml::Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "static" in params, "Missing parameter 'static'"

def test_sml::role_has_name():
    assert hasattr(sml::Role, "name")
    descriptor = None
    for klass in sml::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sml::role_has_static():
    assert hasattr(sml::Role, "static")
    descriptor = None
    for klass in sml::Role.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_sml::smleenumliteral_is_not_abstract():
    assert not inspect.isabstract(sml::SmlEEnumLiteral)


def test_sml::smleenumliteral_constructor_exists():
    assert callable(sml::SmlEEnumLiteral.__init__)


def test_sml::smleenumliteral_constructor_args():
    sig = inspect.signature(sml::SmlEEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smleenumliteral_has_name():
    assert hasattr(sml::SmlEEnumLiteral, "name")
    descriptor = None
    for klass in sml::SmlEEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::smleenum_is_not_abstract():
    assert not inspect.isabstract(sml::SmlEEnum)


def test_sml::smleenum_constructor_exists():
    assert callable(sml::SmlEEnum.__init__)


def test_sml::smleenum_constructor_args():
    sig = inspect.signature(sml::SmlEEnum.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smleenum_has_name():
    assert hasattr(sml::SmlEEnum, "name")
    descriptor = None
    for klass in sml::SmlEEnum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::collaboration_is_not_abstract():
    assert not inspect.isabstract(sml::Collaboration)


def test_sml::collaboration_constructor_exists():
    assert callable(sml::Collaboration.__init__)


def test_sml::collaboration_constructor_args():
    sig = inspect.signature(sml::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::collaboration_has_name():
    assert hasattr(sml::Collaboration, "name")
    descriptor = None
    for klass in sml::Collaboration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::eventparameterranges_is_not_abstract():
    assert not inspect.isabstract(sml::EventParameterRanges)


def test_sml::eventparameterranges_constructor_exists():
    assert callable(sml::EventParameterRanges.__init__)


def test_sml::eventparameterranges_constructor_args():
    sig = inspect.signature(sml::EventParameterRanges.__init__)
    params = list(sig.parameters.keys())



def test_sml::smletypedelement_is_not_abstract():
    assert not inspect.isabstract(sml::SmlETypedElement)


def test_sml::smletypedelement_constructor_exists():
    assert callable(sml::SmlETypedElement.__init__)


def test_sml::smletypedelement_constructor_args():
    sig = inspect.signature(sml::SmlETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smletypedelement_has_name():
    assert hasattr(sml::SmlETypedElement, "name")
    descriptor = None
    for klass in sml::SmlETypedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::smleclass_is_not_abstract():
    assert not inspect.isabstract(sml::SmlEClass)


def test_sml::smleclass_constructor_exists():
    assert callable(sml::SmlEClass.__init__)


def test_sml::smleclass_constructor_args():
    sig = inspect.signature(sml::SmlEClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smleclass_has_name():
    assert hasattr(sml::SmlEClass, "name")
    descriptor = None
    for klass in sml::SmlEClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::smlepackage_is_not_abstract():
    assert not inspect.isabstract(sml::SmlEPackage)


def test_sml::smlepackage_constructor_exists():
    assert callable(sml::SmlEPackage.__init__)


def test_sml::smlepackage_constructor_args():
    sig = inspect.signature(sml::SmlEPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::smlepackage_has_name():
    assert hasattr(sml::SmlEPackage, "name")
    descriptor = None
    for klass in sml::SmlEPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sml::import_is_not_abstract():
    assert not inspect.isabstract(sml::Import)


def test_sml::import_constructor_exists():
    assert callable(sml::Import.__init__)


def test_sml::import_constructor_args():
    sig = inspect.signature(sml::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_sml::import_has_importURI():
    assert hasattr(sml::Import, "importURI")
    descriptor = None
    for klass in sml::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_sml::specification_is_not_abstract():
    assert not inspect.isabstract(sml::Specification)


def test_sml::specification_constructor_exists():
    assert callable(sml::Specification.__init__)


def test_sml::specification_constructor_args():
    sig = inspect.signature(sml::Specification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sml::specification_has_name():
    assert hasattr(sml::Specification, "name")
    descriptor = None
    for klass in sml::Specification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_collectionoperation_exists():
    # Check that the Enumeration exists
    assert CollectionOperation is not None

def test_collectionoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionOperation]
    expected_literals = [
        "first",
        "containsAll",
        "get",
        "contains",
        "any",
        "isEmpty",
        "size",
        "last",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionOperation"

def test_scenariokind_exists():
    # Check that the Enumeration exists
    assert ScenarioKind is not None

def test_scenariokind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScenarioKind]
    expected_literals = [
        "specification",
        "requirement",
        "existential",
        "assumption",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScenarioKind"


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
sml::StructuralFeatureValue_strategy = st.builds(
    sml::StructuralFeatureValue,
)
sml::CollectionAccess_strategy = st.builds(
    sml::CollectionAccess,
    collectionOperation=
        safe_text
)
sml::Variable_strategy = st.builds(
    sml::Variable,
    name=
        safe_text
)
sml::Document_strategy = st.builds(
    sml::Document,
)
Value_strategy = st.builds(
    Value,
)
sml::EnumValue_strategy = st.builds(
    sml::EnumValue,
)
sml::NullValue_strategy = st.builds(
    sml::NullValue,
)
sml::StringValue_strategy = st.builds(
    sml::StringValue,
    value=
        safe_text
)
sml::BooleanValue_strategy = st.builds(
    sml::BooleanValue,
    value=
        st.booleans()
)
sml::IntegerValue_strategy = st.builds(
    sml::IntegerValue,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
sml::BinaryOperationExpression_strategy = st.builds(
    sml::BinaryOperationExpression,
    operator=
        safe_text
)
sml::UnaryOperationExpression_strategy = st.builds(
    sml::UnaryOperationExpression,
    operator=
        safe_text
)
sml::Value_strategy = st.builds(
    sml::Value,
)
VariableExpression_strategy = st.builds(
    VariableExpression,
)
sml::VariableAssignment_strategy = st.builds(
    sml::VariableAssignment,
)
sml::TypedVariableDeclaration_strategy = st.builds(
    sml::TypedVariableDeclaration,
    name=
        safe_text
)
sml::VariableDeclaration_strategy = st.builds(
    sml::VariableDeclaration,
    name=
        safe_text
)
ExpressionAndVariables_strategy = st.builds(
    ExpressionAndVariables,
)
sml::ExpressionOrRegion_strategy = st.builds(
    sml::ExpressionOrRegion,
)
ExpressionOrRegion_strategy = st.builds(
    ExpressionOrRegion,
)
sml::ExpressionAndVariables_strategy = st.builds(
    sml::ExpressionAndVariables,
)
sml::ExpressionRegion_strategy = st.builds(
    sml::ExpressionRegion,
)
sml::Message_strategy = st.builds(
    sml::Message,
)
Condition_strategy = st.builds(
    Condition,
)
sml::InterruptCondition_strategy = st.builds(
    sml::InterruptCondition,
)
sml::ViolationCondition_strategy = st.builds(
    sml::ViolationCondition,
)
sml::WaitCondition_strategy = st.builds(
    sml::WaitCondition,
    requested=
        st.booleans(),
    strict=
        st.booleans()
)
sml::ConditionExpression_strategy = st.builds(
    sml::ConditionExpression,
)
sml::LoopCondition_strategy = st.builds(
    sml::LoopCondition,
)
sml::CaseCondition_strategy = st.builds(
    sml::CaseCondition,
)
sml::Case_strategy = st.builds(
    sml::Case,
)
sml::VariableValue_strategy = st.builds(
    sml::VariableValue,
)
sml::Expression_strategy = st.builds(
    sml::Expression,
)
ParameterExpression_strategy = st.builds(
    ParameterExpression,
)
sml::ExpressionParameter_strategy = st.builds(
    sml::ExpressionParameter,
)
sml::VariableBindingParameter_strategy = st.builds(
    sml::VariableBindingParameter,
)
sml::RandomParameter_strategy = st.builds(
    sml::RandomParameter,
)
sml::ParameterExpression_strategy = st.builds(
    sml::ParameterExpression,
)
sml::ParameterBinding_strategy = st.builds(
    sml::ParameterBinding,
)
sml::ConstraintBlock_strategy = st.builds(
    sml::ConstraintBlock,
)
sml::VariableExpression_strategy = st.builds(
    sml::VariableExpression,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
sml::Condition_strategy = st.builds(
    sml::Condition,
)
sml::Loop_strategy = st.builds(
    sml::Loop,
)
sml::Alternative_strategy = st.builds(
    sml::Alternative,
)
sml::ModalMessage_strategy = st.builds(
    sml::ModalMessage,
    requested=
        st.booleans(),
    strict=
        st.booleans()
)
sml::Parallel_strategy = st.builds(
    sml::Parallel,
)
sml::VariableFragment_strategy = st.builds(
    sml::VariableFragment,
)
sml::InteractionFragment_strategy = st.builds(
    sml::InteractionFragment,
)
sml::FeatureAccess_strategy = st.builds(
    sml::FeatureAccess,
)
BindingExpression_strategy = st.builds(
    BindingExpression,
)
sml::FeatureAccessBindingExpression_strategy = st.builds(
    sml::FeatureAccessBindingExpression,
)
sml::BindingExpression_strategy = st.builds(
    sml::BindingExpression,
)
sml::Interaction_strategy = st.builds(
    sml::Interaction,
)
sml::RoleBindingConstraint_strategy = st.builds(
    sml::RoleBindingConstraint,
)
sml::SmlEStructuralFeature_strategy = st.builds(
    sml::SmlEStructuralFeature,
    name=
        safe_text
)
sml::SmlEClassifier_strategy = st.builds(
    sml::SmlEClassifier,
    name=
        safe_text
)
AbstractRanges_strategy = st.builds(
    AbstractRanges,
)
sml::StringRanges_strategy = st.builds(
    sml::StringRanges,
    values=
        safe_text
)
sml::EnumRanges_strategy = st.builds(
    sml::EnumRanges,
)
sml::IntegerRanges_strategy = st.builds(
    sml::IntegerRanges,
    values=
        st.integers(),
    min=
        st.integers(),
    max=
        st.integers()
)
sml::AbstractRanges_strategy = st.builds(
    sml::AbstractRanges,
)
sml::RangesForParameter_strategy = st.builds(
    sml::RangesForParameter,
)
sml::Scenario_strategy = st.builds(
    sml::Scenario,
    kind=
        safe_text,
    name=
        safe_text,
    singular=
        st.booleans()
)
sml::Role_strategy = st.builds(
    sml::Role,
    name=
        safe_text,
    static=
        st.booleans()
)
sml::SmlEEnumLiteral_strategy = st.builds(
    sml::SmlEEnumLiteral,
    name=
        safe_text
)
sml::SmlEEnum_strategy = st.builds(
    sml::SmlEEnum,
    name=
        safe_text
)
sml::Collaboration_strategy = st.builds(
    sml::Collaboration,
    name=
        safe_text
)
sml::EventParameterRanges_strategy = st.builds(
    sml::EventParameterRanges,
)
sml::SmlETypedElement_strategy = st.builds(
    sml::SmlETypedElement,
    name=
        safe_text
)
sml::SmlEClass_strategy = st.builds(
    sml::SmlEClass,
    name=
        safe_text
)
sml::SmlEPackage_strategy = st.builds(
    sml::SmlEPackage,
    name=
        safe_text
)
sml::Import_strategy = st.builds(
    sml::Import,
    importURI=
        safe_text
)
sml::Specification_strategy = st.builds(
    sml::Specification,
    name=
        safe_text
)

@given(instance=sml::StructuralFeatureValue_strategy)
@settings(max_examples=50)
def test_sml::structuralfeaturevalue_instantiation(instance):
    assert isinstance(instance, sml::StructuralFeatureValue)

@given(instance=sml::CollectionAccess_strategy)
@settings(max_examples=50)
def test_sml::collectionaccess_instantiation(instance):
    assert isinstance(instance, sml::CollectionAccess)

@given(instance=sml::CollectionAccess_strategy)
def test_sml::collectionaccess_collectionOperation_type(instance):
    assert isinstance(instance.collectionOperation, str)


@given(instance=sml::CollectionAccess_strategy)
def test_sml::collectionaccess_collectionOperation_setter(instance):
    original = instance.collectionOperation
    instance.collectionOperation = original
    assert instance.collectionOperation == original

@given(instance=sml::Variable_strategy)
@settings(max_examples=50)
def test_sml::variable_instantiation(instance):
    assert isinstance(instance, sml::Variable)

@given(instance=sml::Variable_strategy)
def test_sml::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::Variable_strategy)
def test_sml::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::Document_strategy)
@settings(max_examples=50)
def test_sml::document_instantiation(instance):
    assert isinstance(instance, sml::Document)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=sml::EnumValue_strategy)
@settings(max_examples=50)
def test_sml::enumvalue_instantiation(instance):
    assert isinstance(instance, sml::EnumValue)

@given(instance=sml::NullValue_strategy)
@settings(max_examples=50)
def test_sml::nullvalue_instantiation(instance):
    assert isinstance(instance, sml::NullValue)

@given(instance=sml::StringValue_strategy)
@settings(max_examples=50)
def test_sml::stringvalue_instantiation(instance):
    assert isinstance(instance, sml::StringValue)

@given(instance=sml::StringValue_strategy)
def test_sml::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sml::StringValue_strategy)
def test_sml::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sml::BooleanValue_strategy)
@settings(max_examples=50)
def test_sml::booleanvalue_instantiation(instance):
    assert isinstance(instance, sml::BooleanValue)

@given(instance=sml::BooleanValue_strategy)
def test_sml::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=sml::BooleanValue_strategy)
def test_sml::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sml::IntegerValue_strategy)
@settings(max_examples=50)
def test_sml::integervalue_instantiation(instance):
    assert isinstance(instance, sml::IntegerValue)

@given(instance=sml::IntegerValue_strategy)
def test_sml::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=sml::IntegerValue_strategy)
def test_sml::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sml::BinaryOperationExpression_strategy)
@settings(max_examples=50)
def test_sml::binaryoperationexpression_instantiation(instance):
    assert isinstance(instance, sml::BinaryOperationExpression)

@given(instance=sml::BinaryOperationExpression_strategy)
def test_sml::binaryoperationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=sml::BinaryOperationExpression_strategy)
def test_sml::binaryoperationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sml::UnaryOperationExpression_strategy)
@settings(max_examples=50)
def test_sml::unaryoperationexpression_instantiation(instance):
    assert isinstance(instance, sml::UnaryOperationExpression)

@given(instance=sml::UnaryOperationExpression_strategy)
def test_sml::unaryoperationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=sml::UnaryOperationExpression_strategy)
def test_sml::unaryoperationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sml::Value_strategy)
@settings(max_examples=50)
def test_sml::value_instantiation(instance):
    assert isinstance(instance, sml::Value)

@given(instance=VariableExpression_strategy)
@settings(max_examples=50)
def test_variableexpression_instantiation(instance):
    assert isinstance(instance, VariableExpression)

@given(instance=sml::VariableAssignment_strategy)
@settings(max_examples=50)
def test_sml::variableassignment_instantiation(instance):
    assert isinstance(instance, sml::VariableAssignment)

@given(instance=sml::TypedVariableDeclaration_strategy)
@settings(max_examples=50)
def test_sml::typedvariabledeclaration_instantiation(instance):
    assert isinstance(instance, sml::TypedVariableDeclaration)

@given(instance=sml::TypedVariableDeclaration_strategy)
def test_sml::typedvariabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::TypedVariableDeclaration_strategy)
def test_sml::typedvariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_sml::variabledeclaration_instantiation(instance):
    assert isinstance(instance, sml::VariableDeclaration)

@given(instance=sml::VariableDeclaration_strategy)
def test_sml::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::VariableDeclaration_strategy)
def test_sml::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExpressionAndVariables_strategy)
@settings(max_examples=50)
def test_expressionandvariables_instantiation(instance):
    assert isinstance(instance, ExpressionAndVariables)

@given(instance=sml::ExpressionOrRegion_strategy)
@settings(max_examples=50)
def test_sml::expressionorregion_instantiation(instance):
    assert isinstance(instance, sml::ExpressionOrRegion)

@given(instance=ExpressionOrRegion_strategy)
@settings(max_examples=50)
def test_expressionorregion_instantiation(instance):
    assert isinstance(instance, ExpressionOrRegion)

@given(instance=sml::ExpressionAndVariables_strategy)
@settings(max_examples=50)
def test_sml::expressionandvariables_instantiation(instance):
    assert isinstance(instance, sml::ExpressionAndVariables)

@given(instance=sml::ExpressionRegion_strategy)
@settings(max_examples=50)
def test_sml::expressionregion_instantiation(instance):
    assert isinstance(instance, sml::ExpressionRegion)

@given(instance=sml::Message_strategy)
@settings(max_examples=50)
def test_sml::message_instantiation(instance):
    assert isinstance(instance, sml::Message)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sml::InterruptCondition_strategy)
@settings(max_examples=50)
def test_sml::interruptcondition_instantiation(instance):
    assert isinstance(instance, sml::InterruptCondition)

@given(instance=sml::ViolationCondition_strategy)
@settings(max_examples=50)
def test_sml::violationcondition_instantiation(instance):
    assert isinstance(instance, sml::ViolationCondition)

@given(instance=sml::WaitCondition_strategy)
@settings(max_examples=50)
def test_sml::waitcondition_instantiation(instance):
    assert isinstance(instance, sml::WaitCondition)

@given(instance=sml::WaitCondition_strategy)
def test_sml::waitcondition_requested_type(instance):
    assert isinstance(instance.requested, bool)


@given(instance=sml::WaitCondition_strategy)
def test_sml::waitcondition_requested_setter(instance):
    original = instance.requested
    instance.requested = original
    assert instance.requested == original

@given(instance=sml::WaitCondition_strategy)
def test_sml::waitcondition_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=sml::WaitCondition_strategy)
def test_sml::waitcondition_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=sml::ConditionExpression_strategy)
@settings(max_examples=50)
def test_sml::conditionexpression_instantiation(instance):
    assert isinstance(instance, sml::ConditionExpression)

@given(instance=sml::LoopCondition_strategy)
@settings(max_examples=50)
def test_sml::loopcondition_instantiation(instance):
    assert isinstance(instance, sml::LoopCondition)

@given(instance=sml::CaseCondition_strategy)
@settings(max_examples=50)
def test_sml::casecondition_instantiation(instance):
    assert isinstance(instance, sml::CaseCondition)

@given(instance=sml::Case_strategy)
@settings(max_examples=50)
def test_sml::case_instantiation(instance):
    assert isinstance(instance, sml::Case)

@given(instance=sml::VariableValue_strategy)
@settings(max_examples=50)
def test_sml::variablevalue_instantiation(instance):
    assert isinstance(instance, sml::VariableValue)

@given(instance=sml::Expression_strategy)
@settings(max_examples=50)
def test_sml::expression_instantiation(instance):
    assert isinstance(instance, sml::Expression)

@given(instance=ParameterExpression_strategy)
@settings(max_examples=50)
def test_parameterexpression_instantiation(instance):
    assert isinstance(instance, ParameterExpression)

@given(instance=sml::ExpressionParameter_strategy)
@settings(max_examples=50)
def test_sml::expressionparameter_instantiation(instance):
    assert isinstance(instance, sml::ExpressionParameter)

@given(instance=sml::VariableBindingParameter_strategy)
@settings(max_examples=50)
def test_sml::variablebindingparameter_instantiation(instance):
    assert isinstance(instance, sml::VariableBindingParameter)

@given(instance=sml::RandomParameter_strategy)
@settings(max_examples=50)
def test_sml::randomparameter_instantiation(instance):
    assert isinstance(instance, sml::RandomParameter)

@given(instance=sml::ParameterExpression_strategy)
@settings(max_examples=50)
def test_sml::parameterexpression_instantiation(instance):
    assert isinstance(instance, sml::ParameterExpression)

@given(instance=sml::ParameterBinding_strategy)
@settings(max_examples=50)
def test_sml::parameterbinding_instantiation(instance):
    assert isinstance(instance, sml::ParameterBinding)

@given(instance=sml::ConstraintBlock_strategy)
@settings(max_examples=50)
def test_sml::constraintblock_instantiation(instance):
    assert isinstance(instance, sml::ConstraintBlock)

@given(instance=sml::VariableExpression_strategy)
@settings(max_examples=50)
def test_sml::variableexpression_instantiation(instance):
    assert isinstance(instance, sml::VariableExpression)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=sml::Condition_strategy)
@settings(max_examples=50)
def test_sml::condition_instantiation(instance):
    assert isinstance(instance, sml::Condition)

@given(instance=sml::Loop_strategy)
@settings(max_examples=50)
def test_sml::loop_instantiation(instance):
    assert isinstance(instance, sml::Loop)

@given(instance=sml::Alternative_strategy)
@settings(max_examples=50)
def test_sml::alternative_instantiation(instance):
    assert isinstance(instance, sml::Alternative)

@given(instance=sml::ModalMessage_strategy)
@settings(max_examples=50)
def test_sml::modalmessage_instantiation(instance):
    assert isinstance(instance, sml::ModalMessage)

@given(instance=sml::ModalMessage_strategy)
def test_sml::modalmessage_requested_type(instance):
    assert isinstance(instance.requested, bool)


@given(instance=sml::ModalMessage_strategy)
def test_sml::modalmessage_requested_setter(instance):
    original = instance.requested
    instance.requested = original
    assert instance.requested == original

@given(instance=sml::ModalMessage_strategy)
def test_sml::modalmessage_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=sml::ModalMessage_strategy)
def test_sml::modalmessage_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=sml::Parallel_strategy)
@settings(max_examples=50)
def test_sml::parallel_instantiation(instance):
    assert isinstance(instance, sml::Parallel)

@given(instance=sml::VariableFragment_strategy)
@settings(max_examples=50)
def test_sml::variablefragment_instantiation(instance):
    assert isinstance(instance, sml::VariableFragment)

@given(instance=sml::InteractionFragment_strategy)
@settings(max_examples=50)
def test_sml::interactionfragment_instantiation(instance):
    assert isinstance(instance, sml::InteractionFragment)

@given(instance=sml::FeatureAccess_strategy)
@settings(max_examples=50)
def test_sml::featureaccess_instantiation(instance):
    assert isinstance(instance, sml::FeatureAccess)

@given(instance=BindingExpression_strategy)
@settings(max_examples=50)
def test_bindingexpression_instantiation(instance):
    assert isinstance(instance, BindingExpression)

@given(instance=sml::FeatureAccessBindingExpression_strategy)
@settings(max_examples=50)
def test_sml::featureaccessbindingexpression_instantiation(instance):
    assert isinstance(instance, sml::FeatureAccessBindingExpression)

@given(instance=sml::BindingExpression_strategy)
@settings(max_examples=50)
def test_sml::bindingexpression_instantiation(instance):
    assert isinstance(instance, sml::BindingExpression)

@given(instance=sml::Interaction_strategy)
@settings(max_examples=50)
def test_sml::interaction_instantiation(instance):
    assert isinstance(instance, sml::Interaction)

@given(instance=sml::RoleBindingConstraint_strategy)
@settings(max_examples=50)
def test_sml::rolebindingconstraint_instantiation(instance):
    assert isinstance(instance, sml::RoleBindingConstraint)

@given(instance=sml::SmlEStructuralFeature_strategy)
@settings(max_examples=50)
def test_sml::smlestructuralfeature_instantiation(instance):
    assert isinstance(instance, sml::SmlEStructuralFeature)

@given(instance=sml::SmlEStructuralFeature_strategy)
def test_sml::smlestructuralfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlEStructuralFeature_strategy)
def test_sml::smlestructuralfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::SmlEClassifier_strategy)
@settings(max_examples=50)
def test_sml::smleclassifier_instantiation(instance):
    assert isinstance(instance, sml::SmlEClassifier)

@given(instance=sml::SmlEClassifier_strategy)
def test_sml::smleclassifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlEClassifier_strategy)
def test_sml::smleclassifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractRanges_strategy)
@settings(max_examples=50)
def test_abstractranges_instantiation(instance):
    assert isinstance(instance, AbstractRanges)

@given(instance=sml::StringRanges_strategy)
@settings(max_examples=50)
def test_sml::stringranges_instantiation(instance):
    assert isinstance(instance, sml::StringRanges)

@given(instance=sml::StringRanges_strategy)
def test_sml::stringranges_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=sml::StringRanges_strategy)
def test_sml::stringranges_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=sml::EnumRanges_strategy)
@settings(max_examples=50)
def test_sml::enumranges_instantiation(instance):
    assert isinstance(instance, sml::EnumRanges)

@given(instance=sml::IntegerRanges_strategy)
@settings(max_examples=50)
def test_sml::integerranges_instantiation(instance):
    assert isinstance(instance, sml::IntegerRanges)

@given(instance=sml::IntegerRanges_strategy)
def test_sml::integerranges_values_type(instance):
    assert isinstance(instance.values, int)


@given(instance=sml::IntegerRanges_strategy)
def test_sml::integerranges_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=sml::IntegerRanges_strategy)
def test_sml::integerranges_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=sml::IntegerRanges_strategy)
def test_sml::integerranges_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=sml::IntegerRanges_strategy)
def test_sml::integerranges_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=sml::IntegerRanges_strategy)
def test_sml::integerranges_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=sml::AbstractRanges_strategy)
@settings(max_examples=50)
def test_sml::abstractranges_instantiation(instance):
    assert isinstance(instance, sml::AbstractRanges)

@given(instance=sml::RangesForParameter_strategy)
@settings(max_examples=50)
def test_sml::rangesforparameter_instantiation(instance):
    assert isinstance(instance, sml::RangesForParameter)

@given(instance=sml::Scenario_strategy)
@settings(max_examples=50)
def test_sml::scenario_instantiation(instance):
    assert isinstance(instance, sml::Scenario)

@given(instance=sml::Scenario_strategy)
def test_sml::scenario_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sml::Scenario_strategy)
def test_sml::scenario_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sml::Scenario_strategy)
def test_sml::scenario_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::Scenario_strategy)
def test_sml::scenario_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::Scenario_strategy)
def test_sml::scenario_singular_type(instance):
    assert isinstance(instance.singular, bool)


@given(instance=sml::Scenario_strategy)
def test_sml::scenario_singular_setter(instance):
    original = instance.singular
    instance.singular = original
    assert instance.singular == original

@given(instance=sml::Role_strategy)
@settings(max_examples=50)
def test_sml::role_instantiation(instance):
    assert isinstance(instance, sml::Role)

@given(instance=sml::Role_strategy)
def test_sml::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::Role_strategy)
def test_sml::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::Role_strategy)
def test_sml::role_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=sml::Role_strategy)
def test_sml::role_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=sml::SmlEEnumLiteral_strategy)
@settings(max_examples=50)
def test_sml::smleenumliteral_instantiation(instance):
    assert isinstance(instance, sml::SmlEEnumLiteral)

@given(instance=sml::SmlEEnumLiteral_strategy)
def test_sml::smleenumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlEEnumLiteral_strategy)
def test_sml::smleenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::SmlEEnum_strategy)
@settings(max_examples=50)
def test_sml::smleenum_instantiation(instance):
    assert isinstance(instance, sml::SmlEEnum)

@given(instance=sml::SmlEEnum_strategy)
def test_sml::smleenum_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlEEnum_strategy)
def test_sml::smleenum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::Collaboration_strategy)
@settings(max_examples=50)
def test_sml::collaboration_instantiation(instance):
    assert isinstance(instance, sml::Collaboration)

@given(instance=sml::Collaboration_strategy)
def test_sml::collaboration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::Collaboration_strategy)
def test_sml::collaboration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::EventParameterRanges_strategy)
@settings(max_examples=50)
def test_sml::eventparameterranges_instantiation(instance):
    assert isinstance(instance, sml::EventParameterRanges)

@given(instance=sml::SmlETypedElement_strategy)
@settings(max_examples=50)
def test_sml::smletypedelement_instantiation(instance):
    assert isinstance(instance, sml::SmlETypedElement)

@given(instance=sml::SmlETypedElement_strategy)
def test_sml::smletypedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlETypedElement_strategy)
def test_sml::smletypedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::SmlEClass_strategy)
@settings(max_examples=50)
def test_sml::smleclass_instantiation(instance):
    assert isinstance(instance, sml::SmlEClass)

@given(instance=sml::SmlEClass_strategy)
def test_sml::smleclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlEClass_strategy)
def test_sml::smleclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::SmlEPackage_strategy)
@settings(max_examples=50)
def test_sml::smlepackage_instantiation(instance):
    assert isinstance(instance, sml::SmlEPackage)

@given(instance=sml::SmlEPackage_strategy)
def test_sml::smlepackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::SmlEPackage_strategy)
def test_sml::smlepackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sml::Import_strategy)
@settings(max_examples=50)
def test_sml::import_instantiation(instance):
    assert isinstance(instance, sml::Import)

@given(instance=sml::Import_strategy)
def test_sml::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=sml::Import_strategy)
def test_sml::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=sml::Specification_strategy)
@settings(max_examples=50)
def test_sml::specification_instantiation(instance):
    assert isinstance(instance, sml::Specification)

@given(instance=sml::Specification_strategy)
def test_sml::specification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sml::Specification_strategy)
def test_sml::specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
