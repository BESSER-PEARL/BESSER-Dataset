import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    structure::ModelTypeDefinitionBinding,
    structure::ModelTransformation,
    structure::EnumerationLiteral,
    structure::Property,
    structure::Operation,
    CallFeature,
    org::behavior::CallModelTransformation,
    org::behavior::CallProperty,
    org::behavior::CallOperation,
    structure::UnresolvedOperation,
    structure::Using,
    structure::UnresolvedReference,
    Literal,
    org::behavior::VoidLiteral,
    org::behavior::IntegerLiteral,
    behavior::LambdaParameter,
    MultiplicityElement,
    org::structure::ModelTransformation,
    org::behavior::TypeReference,
    org::behavior::CallTypeLiteral,
    org::behavior::BooleanLiteral,
    org::behavior::StringLiteral,
    CallVariable,
    org::behavior::CallResult,
    CallOperation,
    org::behavior::CallSuperOperation,
    behavior::TypeReference,
    KermetaModelElement,
    org::behavior::LambdaParameter,
    org::behavior::Rescue,
    structure::Type,
    structure::TypeContainer,
    structure::KermetaModelElement,
    org::behavior::Expression,
    behavior::Expression,
    behavior::CallExpression,
    org::behavior::UnresolvedCall,
    CallExpression,
    org::behavior::CallEnumLiteral,
    org::behavior::CallValue,
    org::behavior::CallFeature,
    org::behavior::CallVariable,
    behavior::Rescue,
    Expression,
    org::behavior::CallExpression,
    org::behavior::LambdaExpression,
    org::behavior::EmptyExpression,
    org::behavior::Loop,
    org::behavior::Literal,
    org::behavior::SelfExpression,
    org::behavior::Conditional,
    org::behavior::JavaStaticCall,
    org::behavior::Raise,
    org::behavior::Block,
    org::behavior::VariableDecl,
    org::behavior::Assignment,
    structure::Metamodel,
    org::structure::FilteredMetamodelReference,
    TypeDefinition,
    org::structure::ModelTypeDefinition,
    org::structure::ModelElementTypeDefinition,
    org::structure::ModelTypeDefinitionContainer,
    org::structure::UnresolvedModelTransformation,
    org::structure::UseAdaptationOperator,
    structure::AdaptationParameter,
    org::structure::OperationBinding,
    org::structure::PropertyBinding,
    org::structure::EnumerationBinding,
    structure::OperationBinding,
    structure::PropertyBinding,
    org::structure::ClassDefinitionBinding,
    structure::ModelTypeDefinition,
    org::structure::UnresolvedModelTypeDefinition,
    structure::EnumerationBinding,
    structure::UseAdaptationOperator,
    structure::ClassDefinitionBinding,
    AdaptationOperator,
    org::structure::OperationAdaptationOperator,
    org::structure::PropertyAdaptationOperator,
    org::structure::FunctionType,
    org::structure::ProductType,
    org::structure::Using,
    org::structure::UnresolvedReference,
    org::structure::UnresolvedInferredType,
    structure::ModelTypeVariable,
    ObjectTypeVariable,
    org::structure::VirtualType,
    structure::VirtualType,
    TypeVariable,
    org::structure::ModelTypeVariable,
    org::structure::ObjectTypeVariable,
    structure::GenericTypeDefinition,
    structure::TypeVariableBinding,
    Type,
    org::structure::ModelType,
    org::structure::VoidType,
    org::structure::ParameterizedType,
    org::structure::UnresolvedType,
    org::structure::AbstractOperation,
    org::structure::Model,
    structure::FilteredMetamodelReference,
    structure::ModelTypeDefinitionContainer,
    org::structure::ModelTypeDefinitionBinding,
    GenericTypeDefinition,
    org::structure::ClassDefinition,
    ModelElementTypeDefinition,
    org::structure::GenericTypeDefinition,
    org::structure::AbstractProperty,
    org::structure::Tag,
    org::structure::Parameter,
    structure::Package,
    structure::ModelElementTypeDefinitionContainer,
    org::structure::NamedElement,
    DataType,
    org::structure::PrimitiveType,
    org::structure::Enumeration,
    structure::ModelElementTypeDefinition,
    org::structure::DataType,
    structure::Class,
    structure::AdaptationOperator,
    org::structure::UnresolvedAdaptationOperator,
    structure::NamedElement,
    org::structure::TypedElement,
    org::structure::Metamodel,
    org::structure::Package,
    org::structure::TypeVariable,
    org::structure::TypeDefinition,
    TypedElement,
    org::structure::AdaptationParameter,
    org::structure::MultiplicityElement,
    org::structure::TypeVariableBinding,
    structure::Enumeration,
    NamedElement,
    org::structure::ModelElementTypeDefinitionContainer,
    org::structure::AdaptationOperator,
    org::structure::Constraint,
    org::structure::EnumerationLiteral,
    org::structure::TypeContainer,
    ParameterizedType,
    org::structure::Class,
    structure::UnresolvedProperty,
    structure::AbstractProperty,
    org::structure::UnresolvedProperty,
    structure::TypeVariable,
    org::structure::UnresolvedTypeVariable,
    structure::ClassDefinition,
    org::structure::Type,
    structure::Constraint,
    structure::Parameter,
    structure::AbstractOperation,
    org::structure::UnresolvedOperation,
    structure::MultiplicityElement,
    org::structure::Property,
    org::structure::Operation,
    structure::Tag,
    org::structure::KermetaModelElement,
    ConstraintType,
    ConstraintLanguage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structure::modeltypedefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(structure::ModelTypeDefinitionBinding)


def test_structure::modeltypedefinitionbinding_constructor_exists():
    assert callable(structure::ModelTypeDefinitionBinding.__init__)


def test_structure::modeltypedefinitionbinding_constructor_args():
    sig = inspect.signature(structure::ModelTypeDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure::modeltransformation_is_not_abstract():
    assert not inspect.isabstract(structure::ModelTransformation)


def test_structure::modeltransformation_constructor_exists():
    assert callable(structure::ModelTransformation.__init__)


def test_structure::modeltransformation_constructor_args():
    sig = inspect.signature(structure::ModelTransformation.__init__)
    params = list(sig.parameters.keys())



def test_structure::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(structure::EnumerationLiteral)


def test_structure::enumerationliteral_constructor_exists():
    assert callable(structure::EnumerationLiteral.__init__)


def test_structure::enumerationliteral_constructor_args():
    sig = inspect.signature(structure::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_structure::property_is_not_abstract():
    assert not inspect.isabstract(structure::Property)


def test_structure::property_constructor_exists():
    assert callable(structure::Property.__init__)


def test_structure::property_constructor_args():
    sig = inspect.signature(structure::Property.__init__)
    params = list(sig.parameters.keys())



def test_structure::operation_is_not_abstract():
    assert not inspect.isabstract(structure::Operation)


def test_structure::operation_constructor_exists():
    assert callable(structure::Operation.__init__)


def test_structure::operation_constructor_args():
    sig = inspect.signature(structure::Operation.__init__)
    params = list(sig.parameters.keys())



def test_callfeature_is_not_abstract():
    assert not inspect.isabstract(CallFeature)


def test_callfeature_constructor_exists():
    assert callable(CallFeature.__init__)


def test_callfeature_constructor_args():
    sig = inspect.signature(CallFeature.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callmodeltransformation_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallModelTransformation)


def test_org::behavior::callmodeltransformation_constructor_exists():
    assert callable(org::behavior::CallModelTransformation.__init__)


def test_org::behavior::callmodeltransformation_constructor_args():
    sig = inspect.signature(org::behavior::CallModelTransformation.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callproperty_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallProperty)


def test_org::behavior::callproperty_constructor_exists():
    assert callable(org::behavior::CallProperty.__init__)


def test_org::behavior::callproperty_constructor_args():
    sig = inspect.signature(org::behavior::CallProperty.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::calloperation_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallOperation)


def test_org::behavior::calloperation_constructor_exists():
    assert callable(org::behavior::CallOperation.__init__)


def test_org::behavior::calloperation_constructor_args():
    sig = inspect.signature(org::behavior::CallOperation.__init__)
    params = list(sig.parameters.keys())



def test_structure::unresolvedoperation_is_not_abstract():
    assert not inspect.isabstract(structure::UnresolvedOperation)


def test_structure::unresolvedoperation_constructor_exists():
    assert callable(structure::UnresolvedOperation.__init__)


def test_structure::unresolvedoperation_constructor_args():
    sig = inspect.signature(structure::UnresolvedOperation.__init__)
    params = list(sig.parameters.keys())



def test_structure::using_is_not_abstract():
    assert not inspect.isabstract(structure::Using)


def test_structure::using_constructor_exists():
    assert callable(structure::Using.__init__)


def test_structure::using_constructor_args():
    sig = inspect.signature(structure::Using.__init__)
    params = list(sig.parameters.keys())



def test_structure::unresolvedreference_is_not_abstract():
    assert not inspect.isabstract(structure::UnresolvedReference)


def test_structure::unresolvedreference_constructor_exists():
    assert callable(structure::UnresolvedReference.__init__)


def test_structure::unresolvedreference_constructor_args():
    sig = inspect.signature(structure::UnresolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::voidliteral_is_not_abstract():
    assert not inspect.isabstract(org::behavior::VoidLiteral)


def test_org::behavior::voidliteral_constructor_exists():
    assert callable(org::behavior::VoidLiteral.__init__)


def test_org::behavior::voidliteral_constructor_args():
    sig = inspect.signature(org::behavior::VoidLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::integerliteral_is_not_abstract():
    assert not inspect.isabstract(org::behavior::IntegerLiteral)


def test_org::behavior::integerliteral_constructor_exists():
    assert callable(org::behavior::IntegerLiteral.__init__)


def test_org::behavior::integerliteral_constructor_args():
    sig = inspect.signature(org::behavior::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_org::behavior::integerliteral_has_value():
    assert hasattr(org::behavior::IntegerLiteral, "value")
    descriptor = None
    for klass in org::behavior::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behavior::lambdaparameter_is_not_abstract():
    assert not inspect.isabstract(behavior::LambdaParameter)


def test_behavior::lambdaparameter_constructor_exists():
    assert callable(behavior::LambdaParameter.__init__)


def test_behavior::lambdaparameter_constructor_args():
    sig = inspect.signature(behavior::LambdaParameter.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modeltransformation_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelTransformation)


def test_org::structure::modeltransformation_constructor_exists():
    assert callable(org::structure::ModelTransformation.__init__)


def test_org::structure::modeltransformation_constructor_args():
    sig = inspect.signature(org::structure::ModelTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_org::structure::modeltransformation_has_isAbstract():
    assert hasattr(org::structure::ModelTransformation, "isAbstract")
    descriptor = None
    for klass in org::structure::ModelTransformation.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::typereference_is_not_abstract():
    assert not inspect.isabstract(org::behavior::TypeReference)


def test_org::behavior::typereference_constructor_exists():
    assert callable(org::behavior::TypeReference.__init__)


def test_org::behavior::typereference_constructor_args():
    sig = inspect.signature(org::behavior::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::calltypeliteral_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallTypeLiteral)


def test_org::behavior::calltypeliteral_constructor_exists():
    assert callable(org::behavior::CallTypeLiteral.__init__)


def test_org::behavior::calltypeliteral_constructor_args():
    sig = inspect.signature(org::behavior::CallTypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(org::behavior::BooleanLiteral)


def test_org::behavior::booleanliteral_constructor_exists():
    assert callable(org::behavior::BooleanLiteral.__init__)


def test_org::behavior::booleanliteral_constructor_args():
    sig = inspect.signature(org::behavior::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_org::behavior::booleanliteral_has_value():
    assert hasattr(org::behavior::BooleanLiteral, "value")
    descriptor = None
    for klass in org::behavior::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::stringliteral_is_not_abstract():
    assert not inspect.isabstract(org::behavior::StringLiteral)


def test_org::behavior::stringliteral_constructor_exists():
    assert callable(org::behavior::StringLiteral.__init__)


def test_org::behavior::stringliteral_constructor_args():
    sig = inspect.signature(org::behavior::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_org::behavior::stringliteral_has_value():
    assert hasattr(org::behavior::StringLiteral, "value")
    descriptor = None
    for klass in org::behavior::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_callvariable_is_not_abstract():
    assert not inspect.isabstract(CallVariable)


def test_callvariable_constructor_exists():
    assert callable(CallVariable.__init__)


def test_callvariable_constructor_args():
    sig = inspect.signature(CallVariable.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callresult_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallResult)


def test_org::behavior::callresult_constructor_exists():
    assert callable(org::behavior::CallResult.__init__)


def test_org::behavior::callresult_constructor_args():
    sig = inspect.signature(org::behavior::CallResult.__init__)
    params = list(sig.parameters.keys())



def test_calloperation_is_not_abstract():
    assert not inspect.isabstract(CallOperation)


def test_calloperation_constructor_exists():
    assert callable(CallOperation.__init__)


def test_calloperation_constructor_args():
    sig = inspect.signature(CallOperation.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callsuperoperation_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallSuperOperation)


def test_org::behavior::callsuperoperation_constructor_exists():
    assert callable(org::behavior::CallSuperOperation.__init__)


def test_org::behavior::callsuperoperation_constructor_args():
    sig = inspect.signature(org::behavior::CallSuperOperation.__init__)
    params = list(sig.parameters.keys())



def test_behavior::typereference_is_not_abstract():
    assert not inspect.isabstract(behavior::TypeReference)


def test_behavior::typereference_constructor_exists():
    assert callable(behavior::TypeReference.__init__)


def test_behavior::typereference_constructor_args():
    sig = inspect.signature(behavior::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_kermetamodelelement_is_not_abstract():
    assert not inspect.isabstract(KermetaModelElement)


def test_kermetamodelelement_constructor_exists():
    assert callable(KermetaModelElement.__init__)


def test_kermetamodelelement_constructor_args():
    sig = inspect.signature(KermetaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::lambdaparameter_is_not_abstract():
    assert not inspect.isabstract(org::behavior::LambdaParameter)


def test_org::behavior::lambdaparameter_constructor_exists():
    assert callable(org::behavior::LambdaParameter.__init__)


def test_org::behavior::lambdaparameter_constructor_args():
    sig = inspect.signature(org::behavior::LambdaParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org::behavior::lambdaparameter_has_name():
    assert hasattr(org::behavior::LambdaParameter, "name")
    descriptor = None
    for klass in org::behavior::LambdaParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::rescue_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Rescue)


def test_org::behavior::rescue_constructor_exists():
    assert callable(org::behavior::Rescue.__init__)


def test_org::behavior::rescue_constructor_args():
    sig = inspect.signature(org::behavior::Rescue.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionName" in params, "Missing parameter 'exceptionName'"

def test_org::behavior::rescue_has_exceptionName():
    assert hasattr(org::behavior::Rescue, "exceptionName")
    descriptor = None
    for klass in org::behavior::Rescue.__mro__:
        if "exceptionName" in klass.__dict__:
            descriptor = klass.__dict__["exceptionName"]
            break
    assert isinstance(descriptor, property)



def test_structure::type_is_not_abstract():
    assert not inspect.isabstract(structure::Type)


def test_structure::type_constructor_exists():
    assert callable(structure::Type.__init__)


def test_structure::type_constructor_args():
    sig = inspect.signature(structure::Type.__init__)
    params = list(sig.parameters.keys())



def test_structure::typecontainer_is_not_abstract():
    assert not inspect.isabstract(structure::TypeContainer)


def test_structure::typecontainer_constructor_exists():
    assert callable(structure::TypeContainer.__init__)


def test_structure::typecontainer_constructor_args():
    sig = inspect.signature(structure::TypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_structure::kermetamodelelement_is_not_abstract():
    assert not inspect.isabstract(structure::KermetaModelElement)


def test_structure::kermetamodelelement_constructor_exists():
    assert callable(structure::KermetaModelElement.__init__)


def test_structure::kermetamodelelement_constructor_args():
    sig = inspect.signature(structure::KermetaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::expression_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Expression)


def test_org::behavior::expression_constructor_exists():
    assert callable(org::behavior::Expression.__init__)


def test_org::behavior::expression_constructor_args():
    sig = inspect.signature(org::behavior::Expression.__init__)
    params = list(sig.parameters.keys())



def test_behavior::expression_is_not_abstract():
    assert not inspect.isabstract(behavior::Expression)


def test_behavior::expression_constructor_exists():
    assert callable(behavior::Expression.__init__)


def test_behavior::expression_constructor_args():
    sig = inspect.signature(behavior::Expression.__init__)
    params = list(sig.parameters.keys())



def test_behavior::callexpression_is_not_abstract():
    assert not inspect.isabstract(behavior::CallExpression)


def test_behavior::callexpression_constructor_exists():
    assert callable(behavior::CallExpression.__init__)


def test_behavior::callexpression_constructor_args():
    sig = inspect.signature(behavior::CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::unresolvedcall_is_not_abstract():
    assert not inspect.isabstract(org::behavior::UnresolvedCall)


def test_org::behavior::unresolvedcall_constructor_exists():
    assert callable(org::behavior::UnresolvedCall.__init__)


def test_org::behavior::unresolvedcall_constructor_args():
    sig = inspect.signature(org::behavior::UnresolvedCall.__init__)
    params = list(sig.parameters.keys())
    assert "isAtpre" in params, "Missing parameter 'isAtpre'"
    assert "isCalledWithParenthesis" in params, "Missing parameter 'isCalledWithParenthesis'"

def test_org::behavior::unresolvedcall_has_isAtpre():
    assert hasattr(org::behavior::UnresolvedCall, "isAtpre")
    descriptor = None
    for klass in org::behavior::UnresolvedCall.__mro__:
        if "isAtpre" in klass.__dict__:
            descriptor = klass.__dict__["isAtpre"]
            break
    assert isinstance(descriptor, property)

def test_org::behavior::unresolvedcall_has_isCalledWithParenthesis():
    assert hasattr(org::behavior::UnresolvedCall, "isCalledWithParenthesis")
    descriptor = None
    for klass in org::behavior::UnresolvedCall.__mro__:
        if "isCalledWithParenthesis" in klass.__dict__:
            descriptor = klass.__dict__["isCalledWithParenthesis"]
            break
    assert isinstance(descriptor, property)



def test_callexpression_is_not_abstract():
    assert not inspect.isabstract(CallExpression)


def test_callexpression_constructor_exists():
    assert callable(CallExpression.__init__)


def test_callexpression_constructor_args():
    sig = inspect.signature(CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callenumliteral_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallEnumLiteral)


def test_org::behavior::callenumliteral_constructor_exists():
    assert callable(org::behavior::CallEnumLiteral.__init__)


def test_org::behavior::callenumliteral_constructor_args():
    sig = inspect.signature(org::behavior::CallEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callvalue_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallValue)


def test_org::behavior::callvalue_constructor_exists():
    assert callable(org::behavior::CallValue.__init__)


def test_org::behavior::callvalue_constructor_args():
    sig = inspect.signature(org::behavior::CallValue.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callfeature_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallFeature)


def test_org::behavior::callfeature_constructor_exists():
    assert callable(org::behavior::CallFeature.__init__)


def test_org::behavior::callfeature_constructor_args():
    sig = inspect.signature(org::behavior::CallFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isAtpre" in params, "Missing parameter 'isAtpre'"

def test_org::behavior::callfeature_has_isAtpre():
    assert hasattr(org::behavior::CallFeature, "isAtpre")
    descriptor = None
    for klass in org::behavior::CallFeature.__mro__:
        if "isAtpre" in klass.__dict__:
            descriptor = klass.__dict__["isAtpre"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::callvariable_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallVariable)


def test_org::behavior::callvariable_constructor_exists():
    assert callable(org::behavior::CallVariable.__init__)


def test_org::behavior::callvariable_constructor_args():
    sig = inspect.signature(org::behavior::CallVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isAtpre" in params, "Missing parameter 'isAtpre'"

def test_org::behavior::callvariable_has_isAtpre():
    assert hasattr(org::behavior::CallVariable, "isAtpre")
    descriptor = None
    for klass in org::behavior::CallVariable.__mro__:
        if "isAtpre" in klass.__dict__:
            descriptor = klass.__dict__["isAtpre"]
            break
    assert isinstance(descriptor, property)



def test_behavior::rescue_is_not_abstract():
    assert not inspect.isabstract(behavior::Rescue)


def test_behavior::rescue_constructor_exists():
    assert callable(behavior::Rescue.__init__)


def test_behavior::rescue_constructor_args():
    sig = inspect.signature(behavior::Rescue.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::callexpression_is_not_abstract():
    assert not inspect.isabstract(org::behavior::CallExpression)


def test_org::behavior::callexpression_constructor_exists():
    assert callable(org::behavior::CallExpression.__init__)


def test_org::behavior::callexpression_constructor_args():
    sig = inspect.signature(org::behavior::CallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org::behavior::callexpression_has_name():
    assert hasattr(org::behavior::CallExpression, "name")
    descriptor = None
    for klass in org::behavior::CallExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(org::behavior::LambdaExpression)


def test_org::behavior::lambdaexpression_constructor_exists():
    assert callable(org::behavior::LambdaExpression.__init__)


def test_org::behavior::lambdaexpression_constructor_args():
    sig = inspect.signature(org::behavior::LambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::emptyexpression_is_not_abstract():
    assert not inspect.isabstract(org::behavior::EmptyExpression)


def test_org::behavior::emptyexpression_constructor_exists():
    assert callable(org::behavior::EmptyExpression.__init__)


def test_org::behavior::emptyexpression_constructor_args():
    sig = inspect.signature(org::behavior::EmptyExpression.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::loop_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Loop)


def test_org::behavior::loop_constructor_exists():
    assert callable(org::behavior::Loop.__init__)


def test_org::behavior::loop_constructor_args():
    sig = inspect.signature(org::behavior::Loop.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::literal_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Literal)


def test_org::behavior::literal_constructor_exists():
    assert callable(org::behavior::Literal.__init__)


def test_org::behavior::literal_constructor_args():
    sig = inspect.signature(org::behavior::Literal.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::selfexpression_is_not_abstract():
    assert not inspect.isabstract(org::behavior::SelfExpression)


def test_org::behavior::selfexpression_constructor_exists():
    assert callable(org::behavior::SelfExpression.__init__)


def test_org::behavior::selfexpression_constructor_args():
    sig = inspect.signature(org::behavior::SelfExpression.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::conditional_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Conditional)


def test_org::behavior::conditional_constructor_exists():
    assert callable(org::behavior::Conditional.__init__)


def test_org::behavior::conditional_constructor_args():
    sig = inspect.signature(org::behavior::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::javastaticcall_is_not_abstract():
    assert not inspect.isabstract(org::behavior::JavaStaticCall)


def test_org::behavior::javastaticcall_constructor_exists():
    assert callable(org::behavior::JavaStaticCall.__init__)


def test_org::behavior::javastaticcall_constructor_args():
    sig = inspect.signature(org::behavior::JavaStaticCall.__init__)
    params = list(sig.parameters.keys())
    assert "jmethod" in params, "Missing parameter 'jmethod'"
    assert "jclass" in params, "Missing parameter 'jclass'"

def test_org::behavior::javastaticcall_has_jmethod():
    assert hasattr(org::behavior::JavaStaticCall, "jmethod")
    descriptor = None
    for klass in org::behavior::JavaStaticCall.__mro__:
        if "jmethod" in klass.__dict__:
            descriptor = klass.__dict__["jmethod"]
            break
    assert isinstance(descriptor, property)

def test_org::behavior::javastaticcall_has_jclass():
    assert hasattr(org::behavior::JavaStaticCall, "jclass")
    descriptor = None
    for klass in org::behavior::JavaStaticCall.__mro__:
        if "jclass" in klass.__dict__:
            descriptor = klass.__dict__["jclass"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::raise_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Raise)


def test_org::behavior::raise_constructor_exists():
    assert callable(org::behavior::Raise.__init__)


def test_org::behavior::raise_constructor_args():
    sig = inspect.signature(org::behavior::Raise.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::block_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Block)


def test_org::behavior::block_constructor_exists():
    assert callable(org::behavior::Block.__init__)


def test_org::behavior::block_constructor_args():
    sig = inspect.signature(org::behavior::Block.__init__)
    params = list(sig.parameters.keys())



def test_org::behavior::variabledecl_is_not_abstract():
    assert not inspect.isabstract(org::behavior::VariableDecl)


def test_org::behavior::variabledecl_constructor_exists():
    assert callable(org::behavior::VariableDecl.__init__)


def test_org::behavior::variabledecl_constructor_args():
    sig = inspect.signature(org::behavior::VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_org::behavior::variabledecl_has_identifier():
    assert hasattr(org::behavior::VariableDecl, "identifier")
    descriptor = None
    for klass in org::behavior::VariableDecl.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_org::behavior::assignment_is_not_abstract():
    assert not inspect.isabstract(org::behavior::Assignment)


def test_org::behavior::assignment_constructor_exists():
    assert callable(org::behavior::Assignment.__init__)


def test_org::behavior::assignment_constructor_args():
    sig = inspect.signature(org::behavior::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isCast" in params, "Missing parameter 'isCast'"

def test_org::behavior::assignment_has_isCast():
    assert hasattr(org::behavior::Assignment, "isCast")
    descriptor = None
    for klass in org::behavior::Assignment.__mro__:
        if "isCast" in klass.__dict__:
            descriptor = klass.__dict__["isCast"]
            break
    assert isinstance(descriptor, property)



def test_structure::metamodel_is_not_abstract():
    assert not inspect.isabstract(structure::Metamodel)


def test_structure::metamodel_constructor_exists():
    assert callable(structure::Metamodel.__init__)


def test_structure::metamodel_constructor_args():
    sig = inspect.signature(structure::Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::filteredmetamodelreference_is_not_abstract():
    assert not inspect.isabstract(org::structure::FilteredMetamodelReference)


def test_org::structure::filteredmetamodelreference_constructor_exists():
    assert callable(org::structure::FilteredMetamodelReference.__init__)


def test_org::structure::filteredmetamodelreference_constructor_args():
    sig = inspect.signature(org::structure::FilteredMetamodelReference.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modeltypedefinition_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelTypeDefinition)


def test_org::structure::modeltypedefinition_constructor_exists():
    assert callable(org::structure::ModelTypeDefinition.__init__)


def test_org::structure::modeltypedefinition_constructor_args():
    sig = inspect.signature(org::structure::ModelTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modelelementtypedefinition_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelElementTypeDefinition)


def test_org::structure::modelelementtypedefinition_constructor_exists():
    assert callable(org::structure::ModelElementTypeDefinition.__init__)


def test_org::structure::modelelementtypedefinition_constructor_args():
    sig = inspect.signature(org::structure::ModelElementTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modeltypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelTypeDefinitionContainer)


def test_org::structure::modeltypedefinitioncontainer_constructor_exists():
    assert callable(org::structure::ModelTypeDefinitionContainer.__init__)


def test_org::structure::modeltypedefinitioncontainer_constructor_args():
    sig = inspect.signature(org::structure::ModelTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedmodeltransformation_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedModelTransformation)


def test_org::structure::unresolvedmodeltransformation_constructor_exists():
    assert callable(org::structure::UnresolvedModelTransformation.__init__)


def test_org::structure::unresolvedmodeltransformation_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedModelTransformation.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::useadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org::structure::UseAdaptationOperator)


def test_org::structure::useadaptationoperator_constructor_exists():
    assert callable(org::structure::UseAdaptationOperator.__init__)


def test_org::structure::useadaptationoperator_constructor_args():
    sig = inspect.signature(org::structure::UseAdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_structure::adaptationparameter_is_not_abstract():
    assert not inspect.isabstract(structure::AdaptationParameter)


def test_structure::adaptationparameter_constructor_exists():
    assert callable(structure::AdaptationParameter.__init__)


def test_structure::adaptationparameter_constructor_args():
    sig = inspect.signature(structure::AdaptationParameter.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::operationbinding_is_not_abstract():
    assert not inspect.isabstract(org::structure::OperationBinding)


def test_org::structure::operationbinding_constructor_exists():
    assert callable(org::structure::OperationBinding.__init__)


def test_org::structure::operationbinding_constructor_args():
    sig = inspect.signature(org::structure::OperationBinding.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::propertybinding_is_not_abstract():
    assert not inspect.isabstract(org::structure::PropertyBinding)


def test_org::structure::propertybinding_constructor_exists():
    assert callable(org::structure::PropertyBinding.__init__)


def test_org::structure::propertybinding_constructor_args():
    sig = inspect.signature(org::structure::PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::enumerationbinding_is_not_abstract():
    assert not inspect.isabstract(org::structure::EnumerationBinding)


def test_org::structure::enumerationbinding_constructor_exists():
    assert callable(org::structure::EnumerationBinding.__init__)


def test_org::structure::enumerationbinding_constructor_args():
    sig = inspect.signature(org::structure::EnumerationBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure::operationbinding_is_not_abstract():
    assert not inspect.isabstract(structure::OperationBinding)


def test_structure::operationbinding_constructor_exists():
    assert callable(structure::OperationBinding.__init__)


def test_structure::operationbinding_constructor_args():
    sig = inspect.signature(structure::OperationBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure::propertybinding_is_not_abstract():
    assert not inspect.isabstract(structure::PropertyBinding)


def test_structure::propertybinding_constructor_exists():
    assert callable(structure::PropertyBinding.__init__)


def test_structure::propertybinding_constructor_args():
    sig = inspect.signature(structure::PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::classdefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(org::structure::ClassDefinitionBinding)


def test_org::structure::classdefinitionbinding_constructor_exists():
    assert callable(org::structure::ClassDefinitionBinding.__init__)


def test_org::structure::classdefinitionbinding_constructor_args():
    sig = inspect.signature(org::structure::ClassDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure::modeltypedefinition_is_not_abstract():
    assert not inspect.isabstract(structure::ModelTypeDefinition)


def test_structure::modeltypedefinition_constructor_exists():
    assert callable(structure::ModelTypeDefinition.__init__)


def test_structure::modeltypedefinition_constructor_args():
    sig = inspect.signature(structure::ModelTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedmodeltypedefinition_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedModelTypeDefinition)


def test_org::structure::unresolvedmodeltypedefinition_constructor_exists():
    assert callable(org::structure::UnresolvedModelTypeDefinition.__init__)


def test_org::structure::unresolvedmodeltypedefinition_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedModelTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure::enumerationbinding_is_not_abstract():
    assert not inspect.isabstract(structure::EnumerationBinding)


def test_structure::enumerationbinding_constructor_exists():
    assert callable(structure::EnumerationBinding.__init__)


def test_structure::enumerationbinding_constructor_args():
    sig = inspect.signature(structure::EnumerationBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure::useadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(structure::UseAdaptationOperator)


def test_structure::useadaptationoperator_constructor_exists():
    assert callable(structure::UseAdaptationOperator.__init__)


def test_structure::useadaptationoperator_constructor_args():
    sig = inspect.signature(structure::UseAdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_structure::classdefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(structure::ClassDefinitionBinding)


def test_structure::classdefinitionbinding_constructor_exists():
    assert callable(structure::ClassDefinitionBinding.__init__)


def test_structure::classdefinitionbinding_constructor_args():
    sig = inspect.signature(structure::ClassDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_adaptationoperator_is_not_abstract():
    assert not inspect.isabstract(AdaptationOperator)


def test_adaptationoperator_constructor_exists():
    assert callable(AdaptationOperator.__init__)


def test_adaptationoperator_constructor_args():
    sig = inspect.signature(AdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::operationadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org::structure::OperationAdaptationOperator)


def test_org::structure::operationadaptationoperator_constructor_exists():
    assert callable(org::structure::OperationAdaptationOperator.__init__)


def test_org::structure::operationadaptationoperator_constructor_args():
    sig = inspect.signature(org::structure::OperationAdaptationOperator.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_org::structure::operationadaptationoperator_has_body():
    assert hasattr(org::structure::OperationAdaptationOperator, "body")
    descriptor = None
    for klass in org::structure::OperationAdaptationOperator.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::propertyadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org::structure::PropertyAdaptationOperator)


def test_org::structure::propertyadaptationoperator_constructor_exists():
    assert callable(org::structure::PropertyAdaptationOperator.__init__)


def test_org::structure::propertyadaptationoperator_constructor_args():
    sig = inspect.signature(org::structure::PropertyAdaptationOperator.__init__)
    params = list(sig.parameters.keys())
    assert "getter" in params, "Missing parameter 'getter'"
    assert "setter" in params, "Missing parameter 'setter'"
    assert "remover" in params, "Missing parameter 'remover'"
    assert "adder" in params, "Missing parameter 'adder'"

def test_org::structure::propertyadaptationoperator_has_getter():
    assert hasattr(org::structure::PropertyAdaptationOperator, "getter")
    descriptor = None
    for klass in org::structure::PropertyAdaptationOperator.__mro__:
        if "getter" in klass.__dict__:
            descriptor = klass.__dict__["getter"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::propertyadaptationoperator_has_setter():
    assert hasattr(org::structure::PropertyAdaptationOperator, "setter")
    descriptor = None
    for klass in org::structure::PropertyAdaptationOperator.__mro__:
        if "setter" in klass.__dict__:
            descriptor = klass.__dict__["setter"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::propertyadaptationoperator_has_remover():
    assert hasattr(org::structure::PropertyAdaptationOperator, "remover")
    descriptor = None
    for klass in org::structure::PropertyAdaptationOperator.__mro__:
        if "remover" in klass.__dict__:
            descriptor = klass.__dict__["remover"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::propertyadaptationoperator_has_adder():
    assert hasattr(org::structure::PropertyAdaptationOperator, "adder")
    descriptor = None
    for klass in org::structure::PropertyAdaptationOperator.__mro__:
        if "adder" in klass.__dict__:
            descriptor = klass.__dict__["adder"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::functiontype_is_not_abstract():
    assert not inspect.isabstract(org::structure::FunctionType)


def test_org::structure::functiontype_constructor_exists():
    assert callable(org::structure::FunctionType.__init__)


def test_org::structure::functiontype_constructor_args():
    sig = inspect.signature(org::structure::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::producttype_is_not_abstract():
    assert not inspect.isabstract(org::structure::ProductType)


def test_org::structure::producttype_constructor_exists():
    assert callable(org::structure::ProductType.__init__)


def test_org::structure::producttype_constructor_args():
    sig = inspect.signature(org::structure::ProductType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::using_is_not_abstract():
    assert not inspect.isabstract(org::structure::Using)


def test_org::structure::using_constructor_exists():
    assert callable(org::structure::Using.__init__)


def test_org::structure::using_constructor_args():
    sig = inspect.signature(org::structure::Using.__init__)
    params = list(sig.parameters.keys())
    assert "fromQName" in params, "Missing parameter 'fromQName'"
    assert "toName" in params, "Missing parameter 'toName'"

def test_org::structure::using_has_fromQName():
    assert hasattr(org::structure::Using, "fromQName")
    descriptor = None
    for klass in org::structure::Using.__mro__:
        if "fromQName" in klass.__dict__:
            descriptor = klass.__dict__["fromQName"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::using_has_toName():
    assert hasattr(org::structure::Using, "toName")
    descriptor = None
    for klass in org::structure::Using.__mro__:
        if "toName" in klass.__dict__:
            descriptor = klass.__dict__["toName"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::unresolvedreference_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedReference)


def test_org::structure::unresolvedreference_constructor_exists():
    assert callable(org::structure::UnresolvedReference.__init__)


def test_org::structure::unresolvedreference_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedinferredtype_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedInferredType)


def test_org::structure::unresolvedinferredtype_constructor_exists():
    assert callable(org::structure::UnresolvedInferredType.__init__)


def test_org::structure::unresolvedinferredtype_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedInferredType.__init__)
    params = list(sig.parameters.keys())



def test_structure::modeltypevariable_is_not_abstract():
    assert not inspect.isabstract(structure::ModelTypeVariable)


def test_structure::modeltypevariable_constructor_exists():
    assert callable(structure::ModelTypeVariable.__init__)


def test_structure::modeltypevariable_constructor_args():
    sig = inspect.signature(structure::ModelTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_objecttypevariable_is_not_abstract():
    assert not inspect.isabstract(ObjectTypeVariable)


def test_objecttypevariable_constructor_exists():
    assert callable(ObjectTypeVariable.__init__)


def test_objecttypevariable_constructor_args():
    sig = inspect.signature(ObjectTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::virtualtype_is_not_abstract():
    assert not inspect.isabstract(org::structure::VirtualType)


def test_org::structure::virtualtype_constructor_exists():
    assert callable(org::structure::VirtualType.__init__)


def test_org::structure::virtualtype_constructor_args():
    sig = inspect.signature(org::structure::VirtualType.__init__)
    params = list(sig.parameters.keys())



def test_structure::virtualtype_is_not_abstract():
    assert not inspect.isabstract(structure::VirtualType)


def test_structure::virtualtype_constructor_exists():
    assert callable(structure::VirtualType.__init__)


def test_structure::virtualtype_constructor_args():
    sig = inspect.signature(structure::VirtualType.__init__)
    params = list(sig.parameters.keys())



def test_typevariable_is_not_abstract():
    assert not inspect.isabstract(TypeVariable)


def test_typevariable_constructor_exists():
    assert callable(TypeVariable.__init__)


def test_typevariable_constructor_args():
    sig = inspect.signature(TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modeltypevariable_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelTypeVariable)


def test_org::structure::modeltypevariable_constructor_exists():
    assert callable(org::structure::ModelTypeVariable.__init__)


def test_org::structure::modeltypevariable_constructor_args():
    sig = inspect.signature(org::structure::ModelTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::objecttypevariable_is_not_abstract():
    assert not inspect.isabstract(org::structure::ObjectTypeVariable)


def test_org::structure::objecttypevariable_constructor_exists():
    assert callable(org::structure::ObjectTypeVariable.__init__)


def test_org::structure::objecttypevariable_constructor_args():
    sig = inspect.signature(org::structure::ObjectTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_structure::generictypedefinition_is_not_abstract():
    assert not inspect.isabstract(structure::GenericTypeDefinition)


def test_structure::generictypedefinition_constructor_exists():
    assert callable(structure::GenericTypeDefinition.__init__)


def test_structure::generictypedefinition_constructor_args():
    sig = inspect.signature(structure::GenericTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure::typevariablebinding_is_not_abstract():
    assert not inspect.isabstract(structure::TypeVariableBinding)


def test_structure::typevariablebinding_constructor_exists():
    assert callable(structure::TypeVariableBinding.__init__)


def test_structure::typevariablebinding_constructor_args():
    sig = inspect.signature(structure::TypeVariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modeltype_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelType)


def test_org::structure::modeltype_constructor_exists():
    assert callable(org::structure::ModelType.__init__)


def test_org::structure::modeltype_constructor_args():
    sig = inspect.signature(org::structure::ModelType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::voidtype_is_not_abstract():
    assert not inspect.isabstract(org::structure::VoidType)


def test_org::structure::voidtype_constructor_exists():
    assert callable(org::structure::VoidType.__init__)


def test_org::structure::voidtype_constructor_args():
    sig = inspect.signature(org::structure::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(org::structure::ParameterizedType)


def test_org::structure::parameterizedtype_constructor_exists():
    assert callable(org::structure::ParameterizedType.__init__)


def test_org::structure::parameterizedtype_constructor_args():
    sig = inspect.signature(org::structure::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedType)


def test_org::structure::unresolvedtype_constructor_exists():
    assert callable(org::structure::UnresolvedType.__init__)


def test_org::structure::unresolvedtype_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedType.__init__)
    params = list(sig.parameters.keys())
    assert "typeIdentifier" in params, "Missing parameter 'typeIdentifier'"

def test_org::structure::unresolvedtype_has_typeIdentifier():
    assert hasattr(org::structure::UnresolvedType, "typeIdentifier")
    descriptor = None
    for klass in org::structure::UnresolvedType.__mro__:
        if "typeIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["typeIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::abstractoperation_is_not_abstract():
    assert not inspect.isabstract(org::structure::AbstractOperation)


def test_org::structure::abstractoperation_constructor_exists():
    assert callable(org::structure::AbstractOperation.__init__)


def test_org::structure::abstractoperation_constructor_args():
    sig = inspect.signature(org::structure::AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::model_is_not_abstract():
    assert not inspect.isabstract(org::structure::Model)


def test_org::structure::model_constructor_exists():
    assert callable(org::structure::Model.__init__)


def test_org::structure::model_constructor_args():
    sig = inspect.signature(org::structure::Model.__init__)
    params = list(sig.parameters.keys())



def test_structure::filteredmetamodelreference_is_not_abstract():
    assert not inspect.isabstract(structure::FilteredMetamodelReference)


def test_structure::filteredmetamodelreference_constructor_exists():
    assert callable(structure::FilteredMetamodelReference.__init__)


def test_structure::filteredmetamodelreference_constructor_args():
    sig = inspect.signature(structure::FilteredMetamodelReference.__init__)
    params = list(sig.parameters.keys())



def test_structure::modeltypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(structure::ModelTypeDefinitionContainer)


def test_structure::modeltypedefinitioncontainer_constructor_exists():
    assert callable(structure::ModelTypeDefinitionContainer.__init__)


def test_structure::modeltypedefinitioncontainer_constructor_args():
    sig = inspect.signature(structure::ModelTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modeltypedefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelTypeDefinitionBinding)


def test_org::structure::modeltypedefinitionbinding_constructor_exists():
    assert callable(org::structure::ModelTypeDefinitionBinding.__init__)


def test_org::structure::modeltypedefinitionbinding_constructor_args():
    sig = inspect.signature(org::structure::ModelTypeDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_generictypedefinition_is_not_abstract():
    assert not inspect.isabstract(GenericTypeDefinition)


def test_generictypedefinition_constructor_exists():
    assert callable(GenericTypeDefinition.__init__)


def test_generictypedefinition_constructor_args():
    sig = inspect.signature(GenericTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::classdefinition_is_not_abstract():
    assert not inspect.isabstract(org::structure::ClassDefinition)


def test_org::structure::classdefinition_constructor_exists():
    assert callable(org::structure::ClassDefinition.__init__)


def test_org::structure::classdefinition_constructor_args():
    sig = inspect.signature(org::structure::ClassDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isSingleton" in params, "Missing parameter 'isSingleton'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_org::structure::classdefinition_has_isFinal():
    assert hasattr(org::structure::ClassDefinition, "isFinal")
    descriptor = None
    for klass in org::structure::ClassDefinition.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::classdefinition_has_isSingleton():
    assert hasattr(org::structure::ClassDefinition, "isSingleton")
    descriptor = None
    for klass in org::structure::ClassDefinition.__mro__:
        if "isSingleton" in klass.__dict__:
            descriptor = klass.__dict__["isSingleton"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::classdefinition_has_isAbstract():
    assert hasattr(org::structure::ClassDefinition, "isAbstract")
    descriptor = None
    for klass in org::structure::ClassDefinition.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_modelelementtypedefinition_is_not_abstract():
    assert not inspect.isabstract(ModelElementTypeDefinition)


def test_modelelementtypedefinition_constructor_exists():
    assert callable(ModelElementTypeDefinition.__init__)


def test_modelelementtypedefinition_constructor_args():
    sig = inspect.signature(ModelElementTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::generictypedefinition_is_not_abstract():
    assert not inspect.isabstract(org::structure::GenericTypeDefinition)


def test_org::structure::generictypedefinition_constructor_exists():
    assert callable(org::structure::GenericTypeDefinition.__init__)


def test_org::structure::generictypedefinition_constructor_args():
    sig = inspect.signature(org::structure::GenericTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::abstractproperty_is_not_abstract():
    assert not inspect.isabstract(org::structure::AbstractProperty)


def test_org::structure::abstractproperty_constructor_exists():
    assert callable(org::structure::AbstractProperty.__init__)


def test_org::structure::abstractproperty_constructor_args():
    sig = inspect.signature(org::structure::AbstractProperty.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::tag_is_not_abstract():
    assert not inspect.isabstract(org::structure::Tag)


def test_org::structure::tag_constructor_exists():
    assert callable(org::structure::Tag.__init__)


def test_org::structure::tag_constructor_args():
    sig = inspect.signature(org::structure::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_org::structure::tag_has_name():
    assert hasattr(org::structure::Tag, "name")
    descriptor = None
    for klass in org::structure::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::tag_has_value():
    assert hasattr(org::structure::Tag, "value")
    descriptor = None
    for klass in org::structure::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::parameter_is_not_abstract():
    assert not inspect.isabstract(org::structure::Parameter)


def test_org::structure::parameter_constructor_exists():
    assert callable(org::structure::Parameter.__init__)


def test_org::structure::parameter_constructor_args():
    sig = inspect.signature(org::structure::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_structure::package_is_not_abstract():
    assert not inspect.isabstract(structure::Package)


def test_structure::package_constructor_exists():
    assert callable(structure::Package.__init__)


def test_structure::package_constructor_args():
    sig = inspect.signature(structure::Package.__init__)
    params = list(sig.parameters.keys())



def test_structure::modelelementtypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(structure::ModelElementTypeDefinitionContainer)


def test_structure::modelelementtypedefinitioncontainer_constructor_exists():
    assert callable(structure::ModelElementTypeDefinitionContainer.__init__)


def test_structure::modelelementtypedefinitioncontainer_constructor_args():
    sig = inspect.signature(structure::ModelElementTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::namedelement_is_not_abstract():
    assert not inspect.isabstract(org::structure::NamedElement)


def test_org::structure::namedelement_constructor_exists():
    assert callable(org::structure::NamedElement.__init__)


def test_org::structure::namedelement_constructor_args():
    sig = inspect.signature(org::structure::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org::structure::namedelement_has_name():
    assert hasattr(org::structure::NamedElement, "name")
    descriptor = None
    for klass in org::structure::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::primitivetype_is_not_abstract():
    assert not inspect.isabstract(org::structure::PrimitiveType)


def test_org::structure::primitivetype_constructor_exists():
    assert callable(org::structure::PrimitiveType.__init__)


def test_org::structure::primitivetype_constructor_args():
    sig = inspect.signature(org::structure::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::enumeration_is_not_abstract():
    assert not inspect.isabstract(org::structure::Enumeration)


def test_org::structure::enumeration_constructor_exists():
    assert callable(org::structure::Enumeration.__init__)


def test_org::structure::enumeration_constructor_args():
    sig = inspect.signature(org::structure::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_structure::modelelementtypedefinition_is_not_abstract():
    assert not inspect.isabstract(structure::ModelElementTypeDefinition)


def test_structure::modelelementtypedefinition_constructor_exists():
    assert callable(structure::ModelElementTypeDefinition.__init__)


def test_structure::modelelementtypedefinition_constructor_args():
    sig = inspect.signature(structure::ModelElementTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::datatype_is_not_abstract():
    assert not inspect.isabstract(org::structure::DataType)


def test_org::structure::datatype_constructor_exists():
    assert callable(org::structure::DataType.__init__)


def test_org::structure::datatype_constructor_args():
    sig = inspect.signature(org::structure::DataType.__init__)
    params = list(sig.parameters.keys())



def test_structure::class_is_not_abstract():
    assert not inspect.isabstract(structure::Class)


def test_structure::class_constructor_exists():
    assert callable(structure::Class.__init__)


def test_structure::class_constructor_args():
    sig = inspect.signature(structure::Class.__init__)
    params = list(sig.parameters.keys())



def test_structure::adaptationoperator_is_not_abstract():
    assert not inspect.isabstract(structure::AdaptationOperator)


def test_structure::adaptationoperator_constructor_exists():
    assert callable(structure::AdaptationOperator.__init__)


def test_structure::adaptationoperator_constructor_args():
    sig = inspect.signature(structure::AdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedAdaptationOperator)


def test_org::structure::unresolvedadaptationoperator_constructor_exists():
    assert callable(org::structure::UnresolvedAdaptationOperator.__init__)


def test_org::structure::unresolvedadaptationoperator_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedAdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_structure::namedelement_is_not_abstract():
    assert not inspect.isabstract(structure::NamedElement)


def test_structure::namedelement_constructor_exists():
    assert callable(structure::NamedElement.__init__)


def test_structure::namedelement_constructor_args():
    sig = inspect.signature(structure::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::typedelement_is_not_abstract():
    assert not inspect.isabstract(org::structure::TypedElement)


def test_org::structure::typedelement_constructor_exists():
    assert callable(org::structure::TypedElement.__init__)


def test_org::structure::typedelement_constructor_args():
    sig = inspect.signature(org::structure::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::metamodel_is_not_abstract():
    assert not inspect.isabstract(org::structure::Metamodel)


def test_org::structure::metamodel_constructor_exists():
    assert callable(org::structure::Metamodel.__init__)


def test_org::structure::metamodel_constructor_args():
    sig = inspect.signature(org::structure::Metamodel.__init__)
    params = list(sig.parameters.keys())
    assert "isResolved" in params, "Missing parameter 'isResolved'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_org::structure::metamodel_has_isResolved():
    assert hasattr(org::structure::Metamodel, "isResolved")
    descriptor = None
    for klass in org::structure::Metamodel.__mro__:
        if "isResolved" in klass.__dict__:
            descriptor = klass.__dict__["isResolved"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::metamodel_has_uri():
    assert hasattr(org::structure::Metamodel, "uri")
    descriptor = None
    for klass in org::structure::Metamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::package_is_not_abstract():
    assert not inspect.isabstract(org::structure::Package)


def test_org::structure::package_constructor_exists():
    assert callable(org::structure::Package.__init__)


def test_org::structure::package_constructor_args():
    sig = inspect.signature(org::structure::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_org::structure::package_has_uri():
    assert hasattr(org::structure::Package, "uri")
    descriptor = None
    for klass in org::structure::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::typevariable_is_not_abstract():
    assert not inspect.isabstract(org::structure::TypeVariable)


def test_org::structure::typevariable_constructor_exists():
    assert callable(org::structure::TypeVariable.__init__)


def test_org::structure::typevariable_constructor_args():
    sig = inspect.signature(org::structure::TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::typedefinition_is_not_abstract():
    assert not inspect.isabstract(org::structure::TypeDefinition)


def test_org::structure::typedefinition_constructor_exists():
    assert callable(org::structure::TypeDefinition.__init__)


def test_org::structure::typedefinition_constructor_args():
    sig = inspect.signature(org::structure::TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isAspect" in params, "Missing parameter 'isAspect'"

def test_org::structure::typedefinition_has_isAspect():
    assert hasattr(org::structure::TypeDefinition, "isAspect")
    descriptor = None
    for klass in org::structure::TypeDefinition.__mro__:
        if "isAspect" in klass.__dict__:
            descriptor = klass.__dict__["isAspect"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::adaptationparameter_is_not_abstract():
    assert not inspect.isabstract(org::structure::AdaptationParameter)


def test_org::structure::adaptationparameter_constructor_exists():
    assert callable(org::structure::AdaptationParameter.__init__)


def test_org::structure::adaptationparameter_constructor_args():
    sig = inspect.signature(org::structure::AdaptationParameter.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(org::structure::MultiplicityElement)


def test_org::structure::multiplicityelement_constructor_exists():
    assert callable(org::structure::MultiplicityElement.__init__)


def test_org::structure::multiplicityelement_constructor_args():
    sig = inspect.signature(org::structure::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_org::structure::multiplicityelement_has_isUnique():
    assert hasattr(org::structure::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in org::structure::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::multiplicityelement_has_lower():
    assert hasattr(org::structure::MultiplicityElement, "lower")
    descriptor = None
    for klass in org::structure::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::multiplicityelement_has_isOrdered():
    assert hasattr(org::structure::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in org::structure::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::multiplicityelement_has_upper():
    assert hasattr(org::structure::MultiplicityElement, "upper")
    descriptor = None
    for klass in org::structure::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::typevariablebinding_is_not_abstract():
    assert not inspect.isabstract(org::structure::TypeVariableBinding)


def test_org::structure::typevariablebinding_constructor_exists():
    assert callable(org::structure::TypeVariableBinding.__init__)


def test_org::structure::typevariablebinding_constructor_args():
    sig = inspect.signature(org::structure::TypeVariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure::enumeration_is_not_abstract():
    assert not inspect.isabstract(structure::Enumeration)


def test_structure::enumeration_constructor_exists():
    assert callable(structure::Enumeration.__init__)


def test_structure::enumeration_constructor_args():
    sig = inspect.signature(structure::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::modelelementtypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(org::structure::ModelElementTypeDefinitionContainer)


def test_org::structure::modelelementtypedefinitioncontainer_constructor_exists():
    assert callable(org::structure::ModelElementTypeDefinitionContainer.__init__)


def test_org::structure::modelelementtypedefinitioncontainer_constructor_args():
    sig = inspect.signature(org::structure::ModelElementTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::adaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org::structure::AdaptationOperator)


def test_org::structure::adaptationoperator_constructor_exists():
    assert callable(org::structure::AdaptationOperator.__init__)


def test_org::structure::adaptationoperator_constructor_args():
    sig = inspect.signature(org::structure::AdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::constraint_is_not_abstract():
    assert not inspect.isabstract(org::structure::Constraint)


def test_org::structure::constraint_constructor_exists():
    assert callable(org::structure::Constraint.__init__)


def test_org::structure::constraint_constructor_args():
    sig = inspect.signature(org::structure::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_org::structure::constraint_has_language():
    assert hasattr(org::structure::Constraint, "language")
    descriptor = None
    for klass in org::structure::Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::constraint_has_stereotype():
    assert hasattr(org::structure::Constraint, "stereotype")
    descriptor = None
    for klass in org::structure::Constraint.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(org::structure::EnumerationLiteral)


def test_org::structure::enumerationliteral_constructor_exists():
    assert callable(org::structure::EnumerationLiteral.__init__)


def test_org::structure::enumerationliteral_constructor_args():
    sig = inspect.signature(org::structure::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::typecontainer_is_not_abstract():
    assert not inspect.isabstract(org::structure::TypeContainer)


def test_org::structure::typecontainer_constructor_exists():
    assert callable(org::structure::TypeContainer.__init__)


def test_org::structure::typecontainer_constructor_args():
    sig = inspect.signature(org::structure::TypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ParameterizedType)


def test_parameterizedtype_constructor_exists():
    assert callable(ParameterizedType.__init__)


def test_parameterizedtype_constructor_args():
    sig = inspect.signature(ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::class_is_not_abstract():
    assert not inspect.isabstract(org::structure::Class)


def test_org::structure::class_constructor_exists():
    assert callable(org::structure::Class.__init__)


def test_org::structure::class_constructor_args():
    sig = inspect.signature(org::structure::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_org::structure::class_has_isAbstract():
    assert hasattr(org::structure::Class, "isAbstract")
    descriptor = None
    for klass in org::structure::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::class_has_name():
    assert hasattr(org::structure::Class, "name")
    descriptor = None
    for klass in org::structure::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_structure::unresolvedproperty_is_not_abstract():
    assert not inspect.isabstract(structure::UnresolvedProperty)


def test_structure::unresolvedproperty_constructor_exists():
    assert callable(structure::UnresolvedProperty.__init__)


def test_structure::unresolvedproperty_constructor_args():
    sig = inspect.signature(structure::UnresolvedProperty.__init__)
    params = list(sig.parameters.keys())



def test_structure::abstractproperty_is_not_abstract():
    assert not inspect.isabstract(structure::AbstractProperty)


def test_structure::abstractproperty_constructor_exists():
    assert callable(structure::AbstractProperty.__init__)


def test_structure::abstractproperty_constructor_args():
    sig = inspect.signature(structure::AbstractProperty.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedproperty_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedProperty)


def test_org::structure::unresolvedproperty_constructor_exists():
    assert callable(org::structure::UnresolvedProperty.__init__)


def test_org::structure::unresolvedproperty_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedProperty.__init__)
    params = list(sig.parameters.keys())
    assert "propertyIdentifier" in params, "Missing parameter 'propertyIdentifier'"

def test_org::structure::unresolvedproperty_has_propertyIdentifier():
    assert hasattr(org::structure::UnresolvedProperty, "propertyIdentifier")
    descriptor = None
    for klass in org::structure::UnresolvedProperty.__mro__:
        if "propertyIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["propertyIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_structure::typevariable_is_not_abstract():
    assert not inspect.isabstract(structure::TypeVariable)


def test_structure::typevariable_constructor_exists():
    assert callable(structure::TypeVariable.__init__)


def test_structure::typevariable_constructor_args():
    sig = inspect.signature(structure::TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedtypevariable_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedTypeVariable)


def test_org::structure::unresolvedtypevariable_constructor_exists():
    assert callable(org::structure::UnresolvedTypeVariable.__init__)


def test_org::structure::unresolvedtypevariable_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_structure::classdefinition_is_not_abstract():
    assert not inspect.isabstract(structure::ClassDefinition)


def test_structure::classdefinition_constructor_exists():
    assert callable(structure::ClassDefinition.__init__)


def test_structure::classdefinition_constructor_args():
    sig = inspect.signature(structure::ClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::type_is_not_abstract():
    assert not inspect.isabstract(org::structure::Type)


def test_org::structure::type_constructor_exists():
    assert callable(org::structure::Type.__init__)


def test_org::structure::type_constructor_args():
    sig = inspect.signature(org::structure::Type.__init__)
    params = list(sig.parameters.keys())



def test_structure::constraint_is_not_abstract():
    assert not inspect.isabstract(structure::Constraint)


def test_structure::constraint_constructor_exists():
    assert callable(structure::Constraint.__init__)


def test_structure::constraint_constructor_args():
    sig = inspect.signature(structure::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_structure::parameter_is_not_abstract():
    assert not inspect.isabstract(structure::Parameter)


def test_structure::parameter_constructor_exists():
    assert callable(structure::Parameter.__init__)


def test_structure::parameter_constructor_args():
    sig = inspect.signature(structure::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_structure::abstractoperation_is_not_abstract():
    assert not inspect.isabstract(structure::AbstractOperation)


def test_structure::abstractoperation_constructor_exists():
    assert callable(structure::AbstractOperation.__init__)


def test_structure::abstractoperation_constructor_args():
    sig = inspect.signature(structure::AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::unresolvedoperation_is_not_abstract():
    assert not inspect.isabstract(org::structure::UnresolvedOperation)


def test_org::structure::unresolvedoperation_constructor_exists():
    assert callable(org::structure::UnresolvedOperation.__init__)


def test_org::structure::unresolvedoperation_constructor_args():
    sig = inspect.signature(org::structure::UnresolvedOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operationIdentifier" in params, "Missing parameter 'operationIdentifier'"

def test_org::structure::unresolvedoperation_has_operationIdentifier():
    assert hasattr(org::structure::UnresolvedOperation, "operationIdentifier")
    descriptor = None
    for klass in org::structure::UnresolvedOperation.__mro__:
        if "operationIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["operationIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_structure::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(structure::MultiplicityElement)


def test_structure::multiplicityelement_constructor_exists():
    assert callable(structure::MultiplicityElement.__init__)


def test_structure::multiplicityelement_constructor_args():
    sig = inspect.signature(structure::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::property_is_not_abstract():
    assert not inspect.isabstract(org::structure::Property)


def test_org::structure::property_constructor_exists():
    assert callable(org::structure::Property.__init__)


def test_org::structure::property_constructor_args():
    sig = inspect.signature(org::structure::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isSetterAbstract" in params, "Missing parameter 'isSetterAbstract'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isGetterAbstract" in params, "Missing parameter 'isGetterAbstract'"

def test_org::structure::property_has_isSetterAbstract():
    assert hasattr(org::structure::Property, "isSetterAbstract")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "isSetterAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isSetterAbstract"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::property_has_isReadOnly():
    assert hasattr(org::structure::Property, "isReadOnly")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::property_has_isDerived():
    assert hasattr(org::structure::Property, "isDerived")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::property_has_isComposite():
    assert hasattr(org::structure::Property, "isComposite")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::property_has_isID():
    assert hasattr(org::structure::Property, "isID")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::property_has_default():
    assert hasattr(org::structure::Property, "default")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::property_has_isGetterAbstract():
    assert hasattr(org::structure::Property, "isGetterAbstract")
    descriptor = None
    for klass in org::structure::Property.__mro__:
        if "isGetterAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isGetterAbstract"]
            break
    assert isinstance(descriptor, property)



def test_org::structure::operation_is_not_abstract():
    assert not inspect.isabstract(org::structure::Operation)


def test_org::structure::operation_constructor_exists():
    assert callable(org::structure::Operation.__init__)


def test_org::structure::operation_constructor_args():
    sig = inspect.signature(org::structure::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"

def test_org::structure::operation_has_isAbstract():
    assert hasattr(org::structure::Operation, "isAbstract")
    descriptor = None
    for klass in org::structure::Operation.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_org::structure::operation_has_uniqueName():
    assert hasattr(org::structure::Operation, "uniqueName")
    descriptor = None
    for klass in org::structure::Operation.__mro__:
        if "uniqueName" in klass.__dict__:
            descriptor = klass.__dict__["uniqueName"]
            break
    assert isinstance(descriptor, property)



def test_structure::tag_is_not_abstract():
    assert not inspect.isabstract(structure::Tag)


def test_structure::tag_constructor_exists():
    assert callable(structure::Tag.__init__)


def test_structure::tag_constructor_args():
    sig = inspect.signature(structure::Tag.__init__)
    params = list(sig.parameters.keys())



def test_org::structure::kermetamodelelement_is_not_abstract():
    assert not inspect.isabstract(org::structure::KermetaModelElement)


def test_org::structure::kermetamodelelement_constructor_exists():
    assert callable(org::structure::KermetaModelElement.__init__)


def test_org::structure::kermetamodelelement_constructor_args():
    sig = inspect.signature(org::structure::KermetaModelElement.__init__)
    params = list(sig.parameters.keys())

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "post",
        "pre",
        "inv",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintType"

def test_constraintlanguage_exists():
    # Check that the Enumeration exists
    assert ConstraintLanguage is not None

def test_constraintlanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintLanguage]
    expected_literals = [
        "ocl",
        "kermeta",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintLanguage"


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
structure::ModelTypeDefinitionBinding_strategy = st.builds(
    structure::ModelTypeDefinitionBinding,
)
structure::ModelTransformation_strategy = st.builds(
    structure::ModelTransformation,
)
structure::EnumerationLiteral_strategy = st.builds(
    structure::EnumerationLiteral,
)
structure::Property_strategy = st.builds(
    structure::Property,
)
structure::Operation_strategy = st.builds(
    structure::Operation,
)
CallFeature_strategy = st.builds(
    CallFeature,
)
org::behavior::CallModelTransformation_strategy = st.builds(
    org::behavior::CallModelTransformation,
)
org::behavior::CallProperty_strategy = st.builds(
    org::behavior::CallProperty,
)
org::behavior::CallOperation_strategy = st.builds(
    org::behavior::CallOperation,
)
structure::UnresolvedOperation_strategy = st.builds(
    structure::UnresolvedOperation,
)
structure::Using_strategy = st.builds(
    structure::Using,
)
structure::UnresolvedReference_strategy = st.builds(
    structure::UnresolvedReference,
)
Literal_strategy = st.builds(
    Literal,
)
org::behavior::VoidLiteral_strategy = st.builds(
    org::behavior::VoidLiteral,
)
org::behavior::IntegerLiteral_strategy = st.builds(
    org::behavior::IntegerLiteral,
    value=
        safe_text
)
behavior::LambdaParameter_strategy = st.builds(
    behavior::LambdaParameter,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
org::structure::ModelTransformation_strategy = st.builds(
    org::structure::ModelTransformation,
    isAbstract=
        safe_text
)
org::behavior::TypeReference_strategy = st.builds(
    org::behavior::TypeReference,
)
org::behavior::CallTypeLiteral_strategy = st.builds(
    org::behavior::CallTypeLiteral,
)
org::behavior::BooleanLiteral_strategy = st.builds(
    org::behavior::BooleanLiteral,
    value=
        safe_text
)
org::behavior::StringLiteral_strategy = st.builds(
    org::behavior::StringLiteral,
    value=
        safe_text
)
CallVariable_strategy = st.builds(
    CallVariable,
)
org::behavior::CallResult_strategy = st.builds(
    org::behavior::CallResult,
)
CallOperation_strategy = st.builds(
    CallOperation,
)
org::behavior::CallSuperOperation_strategy = st.builds(
    org::behavior::CallSuperOperation,
)
behavior::TypeReference_strategy = st.builds(
    behavior::TypeReference,
)
KermetaModelElement_strategy = st.builds(
    KermetaModelElement,
)
org::behavior::LambdaParameter_strategy = st.builds(
    org::behavior::LambdaParameter,
    name=
        safe_text
)
org::behavior::Rescue_strategy = st.builds(
    org::behavior::Rescue,
    exceptionName=
        safe_text
)
structure::Type_strategy = st.builds(
    structure::Type,
)
structure::TypeContainer_strategy = st.builds(
    structure::TypeContainer,
)
structure::KermetaModelElement_strategy = st.builds(
    structure::KermetaModelElement,
)
org::behavior::Expression_strategy = st.builds(
    org::behavior::Expression,
)
behavior::Expression_strategy = st.builds(
    behavior::Expression,
)
behavior::CallExpression_strategy = st.builds(
    behavior::CallExpression,
)
org::behavior::UnresolvedCall_strategy = st.builds(
    org::behavior::UnresolvedCall,
    isAtpre=
        safe_text,
    isCalledWithParenthesis=
        safe_text
)
CallExpression_strategy = st.builds(
    CallExpression,
)
org::behavior::CallEnumLiteral_strategy = st.builds(
    org::behavior::CallEnumLiteral,
)
org::behavior::CallValue_strategy = st.builds(
    org::behavior::CallValue,
)
org::behavior::CallFeature_strategy = st.builds(
    org::behavior::CallFeature,
    isAtpre=
        safe_text
)
org::behavior::CallVariable_strategy = st.builds(
    org::behavior::CallVariable,
    isAtpre=
        safe_text
)
behavior::Rescue_strategy = st.builds(
    behavior::Rescue,
)
Expression_strategy = st.builds(
    Expression,
)
org::behavior::CallExpression_strategy = st.builds(
    org::behavior::CallExpression,
    name=
        safe_text
)
org::behavior::LambdaExpression_strategy = st.builds(
    org::behavior::LambdaExpression,
)
org::behavior::EmptyExpression_strategy = st.builds(
    org::behavior::EmptyExpression,
)
org::behavior::Loop_strategy = st.builds(
    org::behavior::Loop,
)
org::behavior::Literal_strategy = st.builds(
    org::behavior::Literal,
)
org::behavior::SelfExpression_strategy = st.builds(
    org::behavior::SelfExpression,
)
org::behavior::Conditional_strategy = st.builds(
    org::behavior::Conditional,
)
org::behavior::JavaStaticCall_strategy = st.builds(
    org::behavior::JavaStaticCall,
    jmethod=
        safe_text,
    jclass=
        safe_text
)
org::behavior::Raise_strategy = st.builds(
    org::behavior::Raise,
)
org::behavior::Block_strategy = st.builds(
    org::behavior::Block,
)
org::behavior::VariableDecl_strategy = st.builds(
    org::behavior::VariableDecl,
    identifier=
        safe_text
)
org::behavior::Assignment_strategy = st.builds(
    org::behavior::Assignment,
    isCast=
        safe_text
)
structure::Metamodel_strategy = st.builds(
    structure::Metamodel,
)
org::structure::FilteredMetamodelReference_strategy = st.builds(
    org::structure::FilteredMetamodelReference,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
org::structure::ModelTypeDefinition_strategy = st.builds(
    org::structure::ModelTypeDefinition,
)
org::structure::ModelElementTypeDefinition_strategy = st.builds(
    org::structure::ModelElementTypeDefinition,
)
org::structure::ModelTypeDefinitionContainer_strategy = st.builds(
    org::structure::ModelTypeDefinitionContainer,
)
org::structure::UnresolvedModelTransformation_strategy = st.builds(
    org::structure::UnresolvedModelTransformation,
)
org::structure::UseAdaptationOperator_strategy = st.builds(
    org::structure::UseAdaptationOperator,
)
structure::AdaptationParameter_strategy = st.builds(
    structure::AdaptationParameter,
)
org::structure::OperationBinding_strategy = st.builds(
    org::structure::OperationBinding,
)
org::structure::PropertyBinding_strategy = st.builds(
    org::structure::PropertyBinding,
)
org::structure::EnumerationBinding_strategy = st.builds(
    org::structure::EnumerationBinding,
)
structure::OperationBinding_strategy = st.builds(
    structure::OperationBinding,
)
structure::PropertyBinding_strategy = st.builds(
    structure::PropertyBinding,
)
org::structure::ClassDefinitionBinding_strategy = st.builds(
    org::structure::ClassDefinitionBinding,
)
structure::ModelTypeDefinition_strategy = st.builds(
    structure::ModelTypeDefinition,
)
org::structure::UnresolvedModelTypeDefinition_strategy = st.builds(
    org::structure::UnresolvedModelTypeDefinition,
)
structure::EnumerationBinding_strategy = st.builds(
    structure::EnumerationBinding,
)
structure::UseAdaptationOperator_strategy = st.builds(
    structure::UseAdaptationOperator,
)
structure::ClassDefinitionBinding_strategy = st.builds(
    structure::ClassDefinitionBinding,
)
AdaptationOperator_strategy = st.builds(
    AdaptationOperator,
)
org::structure::OperationAdaptationOperator_strategy = st.builds(
    org::structure::OperationAdaptationOperator,
    body=
        safe_text
)
org::structure::PropertyAdaptationOperator_strategy = st.builds(
    org::structure::PropertyAdaptationOperator,
    getter=
        safe_text,
    setter=
        safe_text,
    remover=
        safe_text,
    adder=
        safe_text
)
org::structure::FunctionType_strategy = st.builds(
    org::structure::FunctionType,
)
org::structure::ProductType_strategy = st.builds(
    org::structure::ProductType,
)
org::structure::Using_strategy = st.builds(
    org::structure::Using,
    fromQName=
        safe_text,
    toName=
        safe_text
)
org::structure::UnresolvedReference_strategy = st.builds(
    org::structure::UnresolvedReference,
)
org::structure::UnresolvedInferredType_strategy = st.builds(
    org::structure::UnresolvedInferredType,
)
structure::ModelTypeVariable_strategy = st.builds(
    structure::ModelTypeVariable,
)
ObjectTypeVariable_strategy = st.builds(
    ObjectTypeVariable,
)
org::structure::VirtualType_strategy = st.builds(
    org::structure::VirtualType,
)
structure::VirtualType_strategy = st.builds(
    structure::VirtualType,
)
TypeVariable_strategy = st.builds(
    TypeVariable,
)
org::structure::ModelTypeVariable_strategy = st.builds(
    org::structure::ModelTypeVariable,
)
org::structure::ObjectTypeVariable_strategy = st.builds(
    org::structure::ObjectTypeVariable,
)
structure::GenericTypeDefinition_strategy = st.builds(
    structure::GenericTypeDefinition,
)
structure::TypeVariableBinding_strategy = st.builds(
    structure::TypeVariableBinding,
)
Type_strategy = st.builds(
    Type,
)
org::structure::ModelType_strategy = st.builds(
    org::structure::ModelType,
)
org::structure::VoidType_strategy = st.builds(
    org::structure::VoidType,
)
org::structure::ParameterizedType_strategy = st.builds(
    org::structure::ParameterizedType,
)
org::structure::UnresolvedType_strategy = st.builds(
    org::structure::UnresolvedType,
    typeIdentifier=
        safe_text
)
org::structure::AbstractOperation_strategy = st.builds(
    org::structure::AbstractOperation,
)
org::structure::Model_strategy = st.builds(
    org::structure::Model,
)
structure::FilteredMetamodelReference_strategy = st.builds(
    structure::FilteredMetamodelReference,
)
structure::ModelTypeDefinitionContainer_strategy = st.builds(
    structure::ModelTypeDefinitionContainer,
)
org::structure::ModelTypeDefinitionBinding_strategy = st.builds(
    org::structure::ModelTypeDefinitionBinding,
)
GenericTypeDefinition_strategy = st.builds(
    GenericTypeDefinition,
)
org::structure::ClassDefinition_strategy = st.builds(
    org::structure::ClassDefinition,
    isFinal=
        safe_text,
    isSingleton=
        safe_text,
    isAbstract=
        safe_text
)
ModelElementTypeDefinition_strategy = st.builds(
    ModelElementTypeDefinition,
)
org::structure::GenericTypeDefinition_strategy = st.builds(
    org::structure::GenericTypeDefinition,
)
org::structure::AbstractProperty_strategy = st.builds(
    org::structure::AbstractProperty,
)
org::structure::Tag_strategy = st.builds(
    org::structure::Tag,
    name=
        safe_text,
    value=
        safe_text
)
org::structure::Parameter_strategy = st.builds(
    org::structure::Parameter,
)
structure::Package_strategy = st.builds(
    structure::Package,
)
structure::ModelElementTypeDefinitionContainer_strategy = st.builds(
    structure::ModelElementTypeDefinitionContainer,
)
org::structure::NamedElement_strategy = st.builds(
    org::structure::NamedElement,
    name=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
org::structure::PrimitiveType_strategy = st.builds(
    org::structure::PrimitiveType,
)
org::structure::Enumeration_strategy = st.builds(
    org::structure::Enumeration,
)
structure::ModelElementTypeDefinition_strategy = st.builds(
    structure::ModelElementTypeDefinition,
)
org::structure::DataType_strategy = st.builds(
    org::structure::DataType,
)
structure::Class_strategy = st.builds(
    structure::Class,
)
structure::AdaptationOperator_strategy = st.builds(
    structure::AdaptationOperator,
)
org::structure::UnresolvedAdaptationOperator_strategy = st.builds(
    org::structure::UnresolvedAdaptationOperator,
)
structure::NamedElement_strategy = st.builds(
    structure::NamedElement,
)
org::structure::TypedElement_strategy = st.builds(
    org::structure::TypedElement,
)
org::structure::Metamodel_strategy = st.builds(
    org::structure::Metamodel,
    isResolved=
        st.booleans(),
    uri=
        safe_text
)
org::structure::Package_strategy = st.builds(
    org::structure::Package,
    uri=
        safe_text
)
org::structure::TypeVariable_strategy = st.builds(
    org::structure::TypeVariable,
)
org::structure::TypeDefinition_strategy = st.builds(
    org::structure::TypeDefinition,
    isAspect=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
org::structure::AdaptationParameter_strategy = st.builds(
    org::structure::AdaptationParameter,
)
org::structure::MultiplicityElement_strategy = st.builds(
    org::structure::MultiplicityElement,
    isUnique=
        safe_text,
    lower=
        safe_text,
    isOrdered=
        safe_text,
    upper=
        safe_text
)
org::structure::TypeVariableBinding_strategy = st.builds(
    org::structure::TypeVariableBinding,
)
structure::Enumeration_strategy = st.builds(
    structure::Enumeration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
org::structure::ModelElementTypeDefinitionContainer_strategy = st.builds(
    org::structure::ModelElementTypeDefinitionContainer,
)
org::structure::AdaptationOperator_strategy = st.builds(
    org::structure::AdaptationOperator,
)
org::structure::Constraint_strategy = st.builds(
    org::structure::Constraint,
    language=
        safe_text,
    stereotype=
        safe_text
)
org::structure::EnumerationLiteral_strategy = st.builds(
    org::structure::EnumerationLiteral,
)
org::structure::TypeContainer_strategy = st.builds(
    org::structure::TypeContainer,
)
ParameterizedType_strategy = st.builds(
    ParameterizedType,
)
org::structure::Class_strategy = st.builds(
    org::structure::Class,
    isAbstract=
        safe_text,
    name=
        safe_text
)
structure::UnresolvedProperty_strategy = st.builds(
    structure::UnresolvedProperty,
)
structure::AbstractProperty_strategy = st.builds(
    structure::AbstractProperty,
)
org::structure::UnresolvedProperty_strategy = st.builds(
    org::structure::UnresolvedProperty,
    propertyIdentifier=
        safe_text
)
structure::TypeVariable_strategy = st.builds(
    structure::TypeVariable,
)
org::structure::UnresolvedTypeVariable_strategy = st.builds(
    org::structure::UnresolvedTypeVariable,
)
structure::ClassDefinition_strategy = st.builds(
    structure::ClassDefinition,
)
org::structure::Type_strategy = st.builds(
    org::structure::Type,
)
structure::Constraint_strategy = st.builds(
    structure::Constraint,
)
structure::Parameter_strategy = st.builds(
    structure::Parameter,
)
structure::AbstractOperation_strategy = st.builds(
    structure::AbstractOperation,
)
org::structure::UnresolvedOperation_strategy = st.builds(
    org::structure::UnresolvedOperation,
    operationIdentifier=
        safe_text
)
structure::MultiplicityElement_strategy = st.builds(
    structure::MultiplicityElement,
)
org::structure::Property_strategy = st.builds(
    org::structure::Property,
    isSetterAbstract=
        safe_text,
    isReadOnly=
        safe_text,
    isDerived=
        safe_text,
    isComposite=
        safe_text,
    isID=
        safe_text,
    default=
        safe_text,
    isGetterAbstract=
        safe_text
)
org::structure::Operation_strategy = st.builds(
    org::structure::Operation,
    isAbstract=
        safe_text,
    uniqueName=
        safe_text
)
structure::Tag_strategy = st.builds(
    structure::Tag,
)
org::structure::KermetaModelElement_strategy = st.builds(
    org::structure::KermetaModelElement,
)

@given(instance=structure::ModelTypeDefinitionBinding_strategy)
@settings(max_examples=50)
def test_structure::modeltypedefinitionbinding_instantiation(instance):
    assert isinstance(instance, structure::ModelTypeDefinitionBinding)

@given(instance=structure::ModelTransformation_strategy)
@settings(max_examples=50)
def test_structure::modeltransformation_instantiation(instance):
    assert isinstance(instance, structure::ModelTransformation)

@given(instance=structure::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_structure::enumerationliteral_instantiation(instance):
    assert isinstance(instance, structure::EnumerationLiteral)

@given(instance=structure::Property_strategy)
@settings(max_examples=50)
def test_structure::property_instantiation(instance):
    assert isinstance(instance, structure::Property)

@given(instance=structure::Operation_strategy)
@settings(max_examples=50)
def test_structure::operation_instantiation(instance):
    assert isinstance(instance, structure::Operation)

@given(instance=CallFeature_strategy)
@settings(max_examples=50)
def test_callfeature_instantiation(instance):
    assert isinstance(instance, CallFeature)

@given(instance=org::behavior::CallModelTransformation_strategy)
@settings(max_examples=50)
def test_org::behavior::callmodeltransformation_instantiation(instance):
    assert isinstance(instance, org::behavior::CallModelTransformation)

@given(instance=org::behavior::CallProperty_strategy)
@settings(max_examples=50)
def test_org::behavior::callproperty_instantiation(instance):
    assert isinstance(instance, org::behavior::CallProperty)

@given(instance=org::behavior::CallOperation_strategy)
@settings(max_examples=50)
def test_org::behavior::calloperation_instantiation(instance):
    assert isinstance(instance, org::behavior::CallOperation)

@given(instance=structure::UnresolvedOperation_strategy)
@settings(max_examples=50)
def test_structure::unresolvedoperation_instantiation(instance):
    assert isinstance(instance, structure::UnresolvedOperation)

@given(instance=structure::Using_strategy)
@settings(max_examples=50)
def test_structure::using_instantiation(instance):
    assert isinstance(instance, structure::Using)

@given(instance=structure::UnresolvedReference_strategy)
@settings(max_examples=50)
def test_structure::unresolvedreference_instantiation(instance):
    assert isinstance(instance, structure::UnresolvedReference)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=org::behavior::VoidLiteral_strategy)
@settings(max_examples=50)
def test_org::behavior::voidliteral_instantiation(instance):
    assert isinstance(instance, org::behavior::VoidLiteral)

@given(instance=org::behavior::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_org::behavior::integerliteral_instantiation(instance):
    assert isinstance(instance, org::behavior::IntegerLiteral)

@given(instance=org::behavior::IntegerLiteral_strategy)
def test_org::behavior::integerliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=org::behavior::IntegerLiteral_strategy)
def test_org::behavior::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behavior::LambdaParameter_strategy)
@settings(max_examples=50)
def test_behavior::lambdaparameter_instantiation(instance):
    assert isinstance(instance, behavior::LambdaParameter)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=org::structure::ModelTransformation_strategy)
@settings(max_examples=50)
def test_org::structure::modeltransformation_instantiation(instance):
    assert isinstance(instance, org::structure::ModelTransformation)

@given(instance=org::structure::ModelTransformation_strategy)
def test_org::structure::modeltransformation_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=org::structure::ModelTransformation_strategy)
def test_org::structure::modeltransformation_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=org::behavior::TypeReference_strategy)
@settings(max_examples=50)
def test_org::behavior::typereference_instantiation(instance):
    assert isinstance(instance, org::behavior::TypeReference)

@given(instance=org::behavior::CallTypeLiteral_strategy)
@settings(max_examples=50)
def test_org::behavior::calltypeliteral_instantiation(instance):
    assert isinstance(instance, org::behavior::CallTypeLiteral)

@given(instance=org::behavior::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_org::behavior::booleanliteral_instantiation(instance):
    assert isinstance(instance, org::behavior::BooleanLiteral)

@given(instance=org::behavior::BooleanLiteral_strategy)
def test_org::behavior::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=org::behavior::BooleanLiteral_strategy)
def test_org::behavior::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=org::behavior::StringLiteral_strategy)
@settings(max_examples=50)
def test_org::behavior::stringliteral_instantiation(instance):
    assert isinstance(instance, org::behavior::StringLiteral)

@given(instance=org::behavior::StringLiteral_strategy)
def test_org::behavior::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=org::behavior::StringLiteral_strategy)
def test_org::behavior::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CallVariable_strategy)
@settings(max_examples=50)
def test_callvariable_instantiation(instance):
    assert isinstance(instance, CallVariable)

@given(instance=org::behavior::CallResult_strategy)
@settings(max_examples=50)
def test_org::behavior::callresult_instantiation(instance):
    assert isinstance(instance, org::behavior::CallResult)

@given(instance=CallOperation_strategy)
@settings(max_examples=50)
def test_calloperation_instantiation(instance):
    assert isinstance(instance, CallOperation)

@given(instance=org::behavior::CallSuperOperation_strategy)
@settings(max_examples=50)
def test_org::behavior::callsuperoperation_instantiation(instance):
    assert isinstance(instance, org::behavior::CallSuperOperation)

@given(instance=behavior::TypeReference_strategy)
@settings(max_examples=50)
def test_behavior::typereference_instantiation(instance):
    assert isinstance(instance, behavior::TypeReference)

@given(instance=KermetaModelElement_strategy)
@settings(max_examples=50)
def test_kermetamodelelement_instantiation(instance):
    assert isinstance(instance, KermetaModelElement)

@given(instance=org::behavior::LambdaParameter_strategy)
@settings(max_examples=50)
def test_org::behavior::lambdaparameter_instantiation(instance):
    assert isinstance(instance, org::behavior::LambdaParameter)

@given(instance=org::behavior::LambdaParameter_strategy)
def test_org::behavior::lambdaparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::behavior::LambdaParameter_strategy)
def test_org::behavior::lambdaparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::behavior::Rescue_strategy)
@settings(max_examples=50)
def test_org::behavior::rescue_instantiation(instance):
    assert isinstance(instance, org::behavior::Rescue)

@given(instance=org::behavior::Rescue_strategy)
def test_org::behavior::rescue_exceptionName_type(instance):
    assert isinstance(instance.exceptionName, str)


@given(instance=org::behavior::Rescue_strategy)
def test_org::behavior::rescue_exceptionName_setter(instance):
    original = instance.exceptionName
    instance.exceptionName = original
    assert instance.exceptionName == original

@given(instance=structure::Type_strategy)
@settings(max_examples=50)
def test_structure::type_instantiation(instance):
    assert isinstance(instance, structure::Type)

@given(instance=structure::TypeContainer_strategy)
@settings(max_examples=50)
def test_structure::typecontainer_instantiation(instance):
    assert isinstance(instance, structure::TypeContainer)

@given(instance=structure::KermetaModelElement_strategy)
@settings(max_examples=50)
def test_structure::kermetamodelelement_instantiation(instance):
    assert isinstance(instance, structure::KermetaModelElement)

@given(instance=org::behavior::Expression_strategy)
@settings(max_examples=50)
def test_org::behavior::expression_instantiation(instance):
    assert isinstance(instance, org::behavior::Expression)

@given(instance=behavior::Expression_strategy)
@settings(max_examples=50)
def test_behavior::expression_instantiation(instance):
    assert isinstance(instance, behavior::Expression)

@given(instance=behavior::CallExpression_strategy)
@settings(max_examples=50)
def test_behavior::callexpression_instantiation(instance):
    assert isinstance(instance, behavior::CallExpression)

@given(instance=org::behavior::UnresolvedCall_strategy)
@settings(max_examples=50)
def test_org::behavior::unresolvedcall_instantiation(instance):
    assert isinstance(instance, org::behavior::UnresolvedCall)

@given(instance=org::behavior::UnresolvedCall_strategy)
def test_org::behavior::unresolvedcall_isAtpre_type(instance):
    assert isinstance(instance.isAtpre, str)


@given(instance=org::behavior::UnresolvedCall_strategy)
def test_org::behavior::unresolvedcall_isAtpre_setter(instance):
    original = instance.isAtpre
    instance.isAtpre = original
    assert instance.isAtpre == original

@given(instance=org::behavior::UnresolvedCall_strategy)
def test_org::behavior::unresolvedcall_isCalledWithParenthesis_type(instance):
    assert isinstance(instance.isCalledWithParenthesis, str)


@given(instance=org::behavior::UnresolvedCall_strategy)
def test_org::behavior::unresolvedcall_isCalledWithParenthesis_setter(instance):
    original = instance.isCalledWithParenthesis
    instance.isCalledWithParenthesis = original
    assert instance.isCalledWithParenthesis == original

@given(instance=CallExpression_strategy)
@settings(max_examples=50)
def test_callexpression_instantiation(instance):
    assert isinstance(instance, CallExpression)

@given(instance=org::behavior::CallEnumLiteral_strategy)
@settings(max_examples=50)
def test_org::behavior::callenumliteral_instantiation(instance):
    assert isinstance(instance, org::behavior::CallEnumLiteral)

@given(instance=org::behavior::CallValue_strategy)
@settings(max_examples=50)
def test_org::behavior::callvalue_instantiation(instance):
    assert isinstance(instance, org::behavior::CallValue)

@given(instance=org::behavior::CallFeature_strategy)
@settings(max_examples=50)
def test_org::behavior::callfeature_instantiation(instance):
    assert isinstance(instance, org::behavior::CallFeature)

@given(instance=org::behavior::CallFeature_strategy)
def test_org::behavior::callfeature_isAtpre_type(instance):
    assert isinstance(instance.isAtpre, str)


@given(instance=org::behavior::CallFeature_strategy)
def test_org::behavior::callfeature_isAtpre_setter(instance):
    original = instance.isAtpre
    instance.isAtpre = original
    assert instance.isAtpre == original

@given(instance=org::behavior::CallVariable_strategy)
@settings(max_examples=50)
def test_org::behavior::callvariable_instantiation(instance):
    assert isinstance(instance, org::behavior::CallVariable)

@given(instance=org::behavior::CallVariable_strategy)
def test_org::behavior::callvariable_isAtpre_type(instance):
    assert isinstance(instance.isAtpre, str)


@given(instance=org::behavior::CallVariable_strategy)
def test_org::behavior::callvariable_isAtpre_setter(instance):
    original = instance.isAtpre
    instance.isAtpre = original
    assert instance.isAtpre == original

@given(instance=behavior::Rescue_strategy)
@settings(max_examples=50)
def test_behavior::rescue_instantiation(instance):
    assert isinstance(instance, behavior::Rescue)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=org::behavior::CallExpression_strategy)
@settings(max_examples=50)
def test_org::behavior::callexpression_instantiation(instance):
    assert isinstance(instance, org::behavior::CallExpression)

@given(instance=org::behavior::CallExpression_strategy)
def test_org::behavior::callexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::behavior::CallExpression_strategy)
def test_org::behavior::callexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::behavior::LambdaExpression_strategy)
@settings(max_examples=50)
def test_org::behavior::lambdaexpression_instantiation(instance):
    assert isinstance(instance, org::behavior::LambdaExpression)

@given(instance=org::behavior::EmptyExpression_strategy)
@settings(max_examples=50)
def test_org::behavior::emptyexpression_instantiation(instance):
    assert isinstance(instance, org::behavior::EmptyExpression)

@given(instance=org::behavior::Loop_strategy)
@settings(max_examples=50)
def test_org::behavior::loop_instantiation(instance):
    assert isinstance(instance, org::behavior::Loop)

@given(instance=org::behavior::Literal_strategy)
@settings(max_examples=50)
def test_org::behavior::literal_instantiation(instance):
    assert isinstance(instance, org::behavior::Literal)

@given(instance=org::behavior::SelfExpression_strategy)
@settings(max_examples=50)
def test_org::behavior::selfexpression_instantiation(instance):
    assert isinstance(instance, org::behavior::SelfExpression)

@given(instance=org::behavior::Conditional_strategy)
@settings(max_examples=50)
def test_org::behavior::conditional_instantiation(instance):
    assert isinstance(instance, org::behavior::Conditional)

@given(instance=org::behavior::JavaStaticCall_strategy)
@settings(max_examples=50)
def test_org::behavior::javastaticcall_instantiation(instance):
    assert isinstance(instance, org::behavior::JavaStaticCall)

@given(instance=org::behavior::JavaStaticCall_strategy)
def test_org::behavior::javastaticcall_jmethod_type(instance):
    assert isinstance(instance.jmethod, str)


@given(instance=org::behavior::JavaStaticCall_strategy)
def test_org::behavior::javastaticcall_jmethod_setter(instance):
    original = instance.jmethod
    instance.jmethod = original
    assert instance.jmethod == original

@given(instance=org::behavior::JavaStaticCall_strategy)
def test_org::behavior::javastaticcall_jclass_type(instance):
    assert isinstance(instance.jclass, str)


@given(instance=org::behavior::JavaStaticCall_strategy)
def test_org::behavior::javastaticcall_jclass_setter(instance):
    original = instance.jclass
    instance.jclass = original
    assert instance.jclass == original

@given(instance=org::behavior::Raise_strategy)
@settings(max_examples=50)
def test_org::behavior::raise_instantiation(instance):
    assert isinstance(instance, org::behavior::Raise)

@given(instance=org::behavior::Block_strategy)
@settings(max_examples=50)
def test_org::behavior::block_instantiation(instance):
    assert isinstance(instance, org::behavior::Block)

@given(instance=org::behavior::VariableDecl_strategy)
@settings(max_examples=50)
def test_org::behavior::variabledecl_instantiation(instance):
    assert isinstance(instance, org::behavior::VariableDecl)

@given(instance=org::behavior::VariableDecl_strategy)
def test_org::behavior::variabledecl_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=org::behavior::VariableDecl_strategy)
def test_org::behavior::variabledecl_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=org::behavior::Assignment_strategy)
@settings(max_examples=50)
def test_org::behavior::assignment_instantiation(instance):
    assert isinstance(instance, org::behavior::Assignment)

@given(instance=org::behavior::Assignment_strategy)
def test_org::behavior::assignment_isCast_type(instance):
    assert isinstance(instance.isCast, str)


@given(instance=org::behavior::Assignment_strategy)
def test_org::behavior::assignment_isCast_setter(instance):
    original = instance.isCast
    instance.isCast = original
    assert instance.isCast == original

@given(instance=structure::Metamodel_strategy)
@settings(max_examples=50)
def test_structure::metamodel_instantiation(instance):
    assert isinstance(instance, structure::Metamodel)

@given(instance=org::structure::FilteredMetamodelReference_strategy)
@settings(max_examples=50)
def test_org::structure::filteredmetamodelreference_instantiation(instance):
    assert isinstance(instance, org::structure::FilteredMetamodelReference)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=org::structure::ModelTypeDefinition_strategy)
@settings(max_examples=50)
def test_org::structure::modeltypedefinition_instantiation(instance):
    assert isinstance(instance, org::structure::ModelTypeDefinition)

@given(instance=org::structure::ModelElementTypeDefinition_strategy)
@settings(max_examples=50)
def test_org::structure::modelelementtypedefinition_instantiation(instance):
    assert isinstance(instance, org::structure::ModelElementTypeDefinition)

@given(instance=org::structure::ModelTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_org::structure::modeltypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, org::structure::ModelTypeDefinitionContainer)

@given(instance=org::structure::UnresolvedModelTransformation_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedmodeltransformation_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedModelTransformation)

@given(instance=org::structure::UseAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org::structure::useadaptationoperator_instantiation(instance):
    assert isinstance(instance, org::structure::UseAdaptationOperator)

@given(instance=structure::AdaptationParameter_strategy)
@settings(max_examples=50)
def test_structure::adaptationparameter_instantiation(instance):
    assert isinstance(instance, structure::AdaptationParameter)

@given(instance=org::structure::OperationBinding_strategy)
@settings(max_examples=50)
def test_org::structure::operationbinding_instantiation(instance):
    assert isinstance(instance, org::structure::OperationBinding)

@given(instance=org::structure::PropertyBinding_strategy)
@settings(max_examples=50)
def test_org::structure::propertybinding_instantiation(instance):
    assert isinstance(instance, org::structure::PropertyBinding)

@given(instance=org::structure::EnumerationBinding_strategy)
@settings(max_examples=50)
def test_org::structure::enumerationbinding_instantiation(instance):
    assert isinstance(instance, org::structure::EnumerationBinding)

@given(instance=structure::OperationBinding_strategy)
@settings(max_examples=50)
def test_structure::operationbinding_instantiation(instance):
    assert isinstance(instance, structure::OperationBinding)

@given(instance=structure::PropertyBinding_strategy)
@settings(max_examples=50)
def test_structure::propertybinding_instantiation(instance):
    assert isinstance(instance, structure::PropertyBinding)

@given(instance=org::structure::ClassDefinitionBinding_strategy)
@settings(max_examples=50)
def test_org::structure::classdefinitionbinding_instantiation(instance):
    assert isinstance(instance, org::structure::ClassDefinitionBinding)

@given(instance=structure::ModelTypeDefinition_strategy)
@settings(max_examples=50)
def test_structure::modeltypedefinition_instantiation(instance):
    assert isinstance(instance, structure::ModelTypeDefinition)

@given(instance=org::structure::UnresolvedModelTypeDefinition_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedmodeltypedefinition_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedModelTypeDefinition)

@given(instance=structure::EnumerationBinding_strategy)
@settings(max_examples=50)
def test_structure::enumerationbinding_instantiation(instance):
    assert isinstance(instance, structure::EnumerationBinding)

@given(instance=structure::UseAdaptationOperator_strategy)
@settings(max_examples=50)
def test_structure::useadaptationoperator_instantiation(instance):
    assert isinstance(instance, structure::UseAdaptationOperator)

@given(instance=structure::ClassDefinitionBinding_strategy)
@settings(max_examples=50)
def test_structure::classdefinitionbinding_instantiation(instance):
    assert isinstance(instance, structure::ClassDefinitionBinding)

@given(instance=AdaptationOperator_strategy)
@settings(max_examples=50)
def test_adaptationoperator_instantiation(instance):
    assert isinstance(instance, AdaptationOperator)

@given(instance=org::structure::OperationAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org::structure::operationadaptationoperator_instantiation(instance):
    assert isinstance(instance, org::structure::OperationAdaptationOperator)

@given(instance=org::structure::OperationAdaptationOperator_strategy)
def test_org::structure::operationadaptationoperator_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=org::structure::OperationAdaptationOperator_strategy)
def test_org::structure::operationadaptationoperator_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=org::structure::PropertyAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org::structure::propertyadaptationoperator_instantiation(instance):
    assert isinstance(instance, org::structure::PropertyAdaptationOperator)

@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_getter_type(instance):
    assert isinstance(instance.getter, str)


@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_getter_setter(instance):
    original = instance.getter
    instance.getter = original
    assert instance.getter == original

@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_setter_type(instance):
    assert isinstance(instance.setter, str)


@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_setter_setter(instance):
    original = instance.setter
    instance.setter = original
    assert instance.setter == original

@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_remover_type(instance):
    assert isinstance(instance.remover, str)


@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_remover_setter(instance):
    original = instance.remover
    instance.remover = original
    assert instance.remover == original

@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_adder_type(instance):
    assert isinstance(instance.adder, str)


@given(instance=org::structure::PropertyAdaptationOperator_strategy)
def test_org::structure::propertyadaptationoperator_adder_setter(instance):
    original = instance.adder
    instance.adder = original
    assert instance.adder == original

@given(instance=org::structure::FunctionType_strategy)
@settings(max_examples=50)
def test_org::structure::functiontype_instantiation(instance):
    assert isinstance(instance, org::structure::FunctionType)

@given(instance=org::structure::ProductType_strategy)
@settings(max_examples=50)
def test_org::structure::producttype_instantiation(instance):
    assert isinstance(instance, org::structure::ProductType)

@given(instance=org::structure::Using_strategy)
@settings(max_examples=50)
def test_org::structure::using_instantiation(instance):
    assert isinstance(instance, org::structure::Using)

@given(instance=org::structure::Using_strategy)
def test_org::structure::using_fromQName_type(instance):
    assert isinstance(instance.fromQName, str)


@given(instance=org::structure::Using_strategy)
def test_org::structure::using_fromQName_setter(instance):
    original = instance.fromQName
    instance.fromQName = original
    assert instance.fromQName == original

@given(instance=org::structure::Using_strategy)
def test_org::structure::using_toName_type(instance):
    assert isinstance(instance.toName, str)


@given(instance=org::structure::Using_strategy)
def test_org::structure::using_toName_setter(instance):
    original = instance.toName
    instance.toName = original
    assert instance.toName == original

@given(instance=org::structure::UnresolvedReference_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedreference_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedReference)

@given(instance=org::structure::UnresolvedInferredType_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedinferredtype_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedInferredType)

@given(instance=structure::ModelTypeVariable_strategy)
@settings(max_examples=50)
def test_structure::modeltypevariable_instantiation(instance):
    assert isinstance(instance, structure::ModelTypeVariable)

@given(instance=ObjectTypeVariable_strategy)
@settings(max_examples=50)
def test_objecttypevariable_instantiation(instance):
    assert isinstance(instance, ObjectTypeVariable)

@given(instance=org::structure::VirtualType_strategy)
@settings(max_examples=50)
def test_org::structure::virtualtype_instantiation(instance):
    assert isinstance(instance, org::structure::VirtualType)

@given(instance=structure::VirtualType_strategy)
@settings(max_examples=50)
def test_structure::virtualtype_instantiation(instance):
    assert isinstance(instance, structure::VirtualType)

@given(instance=TypeVariable_strategy)
@settings(max_examples=50)
def test_typevariable_instantiation(instance):
    assert isinstance(instance, TypeVariable)

@given(instance=org::structure::ModelTypeVariable_strategy)
@settings(max_examples=50)
def test_org::structure::modeltypevariable_instantiation(instance):
    assert isinstance(instance, org::structure::ModelTypeVariable)

@given(instance=org::structure::ObjectTypeVariable_strategy)
@settings(max_examples=50)
def test_org::structure::objecttypevariable_instantiation(instance):
    assert isinstance(instance, org::structure::ObjectTypeVariable)

@given(instance=structure::GenericTypeDefinition_strategy)
@settings(max_examples=50)
def test_structure::generictypedefinition_instantiation(instance):
    assert isinstance(instance, structure::GenericTypeDefinition)

@given(instance=structure::TypeVariableBinding_strategy)
@settings(max_examples=50)
def test_structure::typevariablebinding_instantiation(instance):
    assert isinstance(instance, structure::TypeVariableBinding)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=org::structure::ModelType_strategy)
@settings(max_examples=50)
def test_org::structure::modeltype_instantiation(instance):
    assert isinstance(instance, org::structure::ModelType)

@given(instance=org::structure::VoidType_strategy)
@settings(max_examples=50)
def test_org::structure::voidtype_instantiation(instance):
    assert isinstance(instance, org::structure::VoidType)

@given(instance=org::structure::ParameterizedType_strategy)
@settings(max_examples=50)
def test_org::structure::parameterizedtype_instantiation(instance):
    assert isinstance(instance, org::structure::ParameterizedType)

@given(instance=org::structure::UnresolvedType_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedtype_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedType)

@given(instance=org::structure::UnresolvedType_strategy)
def test_org::structure::unresolvedtype_typeIdentifier_type(instance):
    assert isinstance(instance.typeIdentifier, str)


@given(instance=org::structure::UnresolvedType_strategy)
def test_org::structure::unresolvedtype_typeIdentifier_setter(instance):
    original = instance.typeIdentifier
    instance.typeIdentifier = original
    assert instance.typeIdentifier == original

@given(instance=org::structure::AbstractOperation_strategy)
@settings(max_examples=50)
def test_org::structure::abstractoperation_instantiation(instance):
    assert isinstance(instance, org::structure::AbstractOperation)

@given(instance=org::structure::Model_strategy)
@settings(max_examples=50)
def test_org::structure::model_instantiation(instance):
    assert isinstance(instance, org::structure::Model)

@given(instance=structure::FilteredMetamodelReference_strategy)
@settings(max_examples=50)
def test_structure::filteredmetamodelreference_instantiation(instance):
    assert isinstance(instance, structure::FilteredMetamodelReference)

@given(instance=structure::ModelTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_structure::modeltypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, structure::ModelTypeDefinitionContainer)

@given(instance=org::structure::ModelTypeDefinitionBinding_strategy)
@settings(max_examples=50)
def test_org::structure::modeltypedefinitionbinding_instantiation(instance):
    assert isinstance(instance, org::structure::ModelTypeDefinitionBinding)

@given(instance=GenericTypeDefinition_strategy)
@settings(max_examples=50)
def test_generictypedefinition_instantiation(instance):
    assert isinstance(instance, GenericTypeDefinition)

@given(instance=org::structure::ClassDefinition_strategy)
@settings(max_examples=50)
def test_org::structure::classdefinition_instantiation(instance):
    assert isinstance(instance, org::structure::ClassDefinition)

@given(instance=org::structure::ClassDefinition_strategy)
def test_org::structure::classdefinition_isFinal_type(instance):
    assert isinstance(instance.isFinal, str)


@given(instance=org::structure::ClassDefinition_strategy)
def test_org::structure::classdefinition_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=org::structure::ClassDefinition_strategy)
def test_org::structure::classdefinition_isSingleton_type(instance):
    assert isinstance(instance.isSingleton, str)


@given(instance=org::structure::ClassDefinition_strategy)
def test_org::structure::classdefinition_isSingleton_setter(instance):
    original = instance.isSingleton
    instance.isSingleton = original
    assert instance.isSingleton == original

@given(instance=org::structure::ClassDefinition_strategy)
def test_org::structure::classdefinition_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=org::structure::ClassDefinition_strategy)
def test_org::structure::classdefinition_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ModelElementTypeDefinition_strategy)
@settings(max_examples=50)
def test_modelelementtypedefinition_instantiation(instance):
    assert isinstance(instance, ModelElementTypeDefinition)

@given(instance=org::structure::GenericTypeDefinition_strategy)
@settings(max_examples=50)
def test_org::structure::generictypedefinition_instantiation(instance):
    assert isinstance(instance, org::structure::GenericTypeDefinition)

@given(instance=org::structure::AbstractProperty_strategy)
@settings(max_examples=50)
def test_org::structure::abstractproperty_instantiation(instance):
    assert isinstance(instance, org::structure::AbstractProperty)

@given(instance=org::structure::Tag_strategy)
@settings(max_examples=50)
def test_org::structure::tag_instantiation(instance):
    assert isinstance(instance, org::structure::Tag)

@given(instance=org::structure::Tag_strategy)
def test_org::structure::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::structure::Tag_strategy)
def test_org::structure::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::structure::Tag_strategy)
def test_org::structure::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=org::structure::Tag_strategy)
def test_org::structure::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=org::structure::Parameter_strategy)
@settings(max_examples=50)
def test_org::structure::parameter_instantiation(instance):
    assert isinstance(instance, org::structure::Parameter)

@given(instance=structure::Package_strategy)
@settings(max_examples=50)
def test_structure::package_instantiation(instance):
    assert isinstance(instance, structure::Package)

@given(instance=structure::ModelElementTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_structure::modelelementtypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, structure::ModelElementTypeDefinitionContainer)

@given(instance=org::structure::NamedElement_strategy)
@settings(max_examples=50)
def test_org::structure::namedelement_instantiation(instance):
    assert isinstance(instance, org::structure::NamedElement)

@given(instance=org::structure::NamedElement_strategy)
def test_org::structure::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::structure::NamedElement_strategy)
def test_org::structure::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=org::structure::PrimitiveType_strategy)
@settings(max_examples=50)
def test_org::structure::primitivetype_instantiation(instance):
    assert isinstance(instance, org::structure::PrimitiveType)

@given(instance=org::structure::Enumeration_strategy)
@settings(max_examples=50)
def test_org::structure::enumeration_instantiation(instance):
    assert isinstance(instance, org::structure::Enumeration)

@given(instance=structure::ModelElementTypeDefinition_strategy)
@settings(max_examples=50)
def test_structure::modelelementtypedefinition_instantiation(instance):
    assert isinstance(instance, structure::ModelElementTypeDefinition)

@given(instance=org::structure::DataType_strategy)
@settings(max_examples=50)
def test_org::structure::datatype_instantiation(instance):
    assert isinstance(instance, org::structure::DataType)

@given(instance=structure::Class_strategy)
@settings(max_examples=50)
def test_structure::class_instantiation(instance):
    assert isinstance(instance, structure::Class)

@given(instance=structure::AdaptationOperator_strategy)
@settings(max_examples=50)
def test_structure::adaptationoperator_instantiation(instance):
    assert isinstance(instance, structure::AdaptationOperator)

@given(instance=org::structure::UnresolvedAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedadaptationoperator_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedAdaptationOperator)

@given(instance=structure::NamedElement_strategy)
@settings(max_examples=50)
def test_structure::namedelement_instantiation(instance):
    assert isinstance(instance, structure::NamedElement)

@given(instance=org::structure::TypedElement_strategy)
@settings(max_examples=50)
def test_org::structure::typedelement_instantiation(instance):
    assert isinstance(instance, org::structure::TypedElement)

@given(instance=org::structure::Metamodel_strategy)
@settings(max_examples=50)
def test_org::structure::metamodel_instantiation(instance):
    assert isinstance(instance, org::structure::Metamodel)

@given(instance=org::structure::Metamodel_strategy)
def test_org::structure::metamodel_isResolved_type(instance):
    assert isinstance(instance.isResolved, bool)


@given(instance=org::structure::Metamodel_strategy)
def test_org::structure::metamodel_isResolved_setter(instance):
    original = instance.isResolved
    instance.isResolved = original
    assert instance.isResolved == original

@given(instance=org::structure::Metamodel_strategy)
def test_org::structure::metamodel_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=org::structure::Metamodel_strategy)
def test_org::structure::metamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=org::structure::Package_strategy)
@settings(max_examples=50)
def test_org::structure::package_instantiation(instance):
    assert isinstance(instance, org::structure::Package)

@given(instance=org::structure::Package_strategy)
def test_org::structure::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=org::structure::Package_strategy)
def test_org::structure::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=org::structure::TypeVariable_strategy)
@settings(max_examples=50)
def test_org::structure::typevariable_instantiation(instance):
    assert isinstance(instance, org::structure::TypeVariable)

@given(instance=org::structure::TypeDefinition_strategy)
@settings(max_examples=50)
def test_org::structure::typedefinition_instantiation(instance):
    assert isinstance(instance, org::structure::TypeDefinition)

@given(instance=org::structure::TypeDefinition_strategy)
def test_org::structure::typedefinition_isAspect_type(instance):
    assert isinstance(instance.isAspect, str)


@given(instance=org::structure::TypeDefinition_strategy)
def test_org::structure::typedefinition_isAspect_setter(instance):
    original = instance.isAspect
    instance.isAspect = original
    assert instance.isAspect == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=org::structure::AdaptationParameter_strategy)
@settings(max_examples=50)
def test_org::structure::adaptationparameter_instantiation(instance):
    assert isinstance(instance, org::structure::AdaptationParameter)

@given(instance=org::structure::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_org::structure::multiplicityelement_instantiation(instance):
    assert isinstance(instance, org::structure::MultiplicityElement)

@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=org::structure::MultiplicityElement_strategy)
def test_org::structure::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=org::structure::TypeVariableBinding_strategy)
@settings(max_examples=50)
def test_org::structure::typevariablebinding_instantiation(instance):
    assert isinstance(instance, org::structure::TypeVariableBinding)

@given(instance=structure::Enumeration_strategy)
@settings(max_examples=50)
def test_structure::enumeration_instantiation(instance):
    assert isinstance(instance, structure::Enumeration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=org::structure::ModelElementTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_org::structure::modelelementtypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, org::structure::ModelElementTypeDefinitionContainer)

@given(instance=org::structure::AdaptationOperator_strategy)
@settings(max_examples=50)
def test_org::structure::adaptationoperator_instantiation(instance):
    assert isinstance(instance, org::structure::AdaptationOperator)

@given(instance=org::structure::Constraint_strategy)
@settings(max_examples=50)
def test_org::structure::constraint_instantiation(instance):
    assert isinstance(instance, org::structure::Constraint)

@given(instance=org::structure::Constraint_strategy)
def test_org::structure::constraint_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=org::structure::Constraint_strategy)
def test_org::structure::constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=org::structure::Constraint_strategy)
def test_org::structure::constraint_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=org::structure::Constraint_strategy)
def test_org::structure::constraint_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=org::structure::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_org::structure::enumerationliteral_instantiation(instance):
    assert isinstance(instance, org::structure::EnumerationLiteral)

@given(instance=org::structure::TypeContainer_strategy)
@settings(max_examples=50)
def test_org::structure::typecontainer_instantiation(instance):
    assert isinstance(instance, org::structure::TypeContainer)

@given(instance=ParameterizedType_strategy)
@settings(max_examples=50)
def test_parameterizedtype_instantiation(instance):
    assert isinstance(instance, ParameterizedType)

@given(instance=org::structure::Class_strategy)
@settings(max_examples=50)
def test_org::structure::class_instantiation(instance):
    assert isinstance(instance, org::structure::Class)

@given(instance=org::structure::Class_strategy)
def test_org::structure::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=org::structure::Class_strategy)
def test_org::structure::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=org::structure::Class_strategy)
def test_org::structure::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::structure::Class_strategy)
def test_org::structure::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=structure::UnresolvedProperty_strategy)
@settings(max_examples=50)
def test_structure::unresolvedproperty_instantiation(instance):
    assert isinstance(instance, structure::UnresolvedProperty)

@given(instance=structure::AbstractProperty_strategy)
@settings(max_examples=50)
def test_structure::abstractproperty_instantiation(instance):
    assert isinstance(instance, structure::AbstractProperty)

@given(instance=org::structure::UnresolvedProperty_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedproperty_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedProperty)

@given(instance=org::structure::UnresolvedProperty_strategy)
def test_org::structure::unresolvedproperty_propertyIdentifier_type(instance):
    assert isinstance(instance.propertyIdentifier, str)


@given(instance=org::structure::UnresolvedProperty_strategy)
def test_org::structure::unresolvedproperty_propertyIdentifier_setter(instance):
    original = instance.propertyIdentifier
    instance.propertyIdentifier = original
    assert instance.propertyIdentifier == original

@given(instance=structure::TypeVariable_strategy)
@settings(max_examples=50)
def test_structure::typevariable_instantiation(instance):
    assert isinstance(instance, structure::TypeVariable)

@given(instance=org::structure::UnresolvedTypeVariable_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedtypevariable_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedTypeVariable)

@given(instance=structure::ClassDefinition_strategy)
@settings(max_examples=50)
def test_structure::classdefinition_instantiation(instance):
    assert isinstance(instance, structure::ClassDefinition)

@given(instance=org::structure::Type_strategy)
@settings(max_examples=50)
def test_org::structure::type_instantiation(instance):
    assert isinstance(instance, org::structure::Type)

@given(instance=structure::Constraint_strategy)
@settings(max_examples=50)
def test_structure::constraint_instantiation(instance):
    assert isinstance(instance, structure::Constraint)

@given(instance=structure::Parameter_strategy)
@settings(max_examples=50)
def test_structure::parameter_instantiation(instance):
    assert isinstance(instance, structure::Parameter)

@given(instance=structure::AbstractOperation_strategy)
@settings(max_examples=50)
def test_structure::abstractoperation_instantiation(instance):
    assert isinstance(instance, structure::AbstractOperation)

@given(instance=org::structure::UnresolvedOperation_strategy)
@settings(max_examples=50)
def test_org::structure::unresolvedoperation_instantiation(instance):
    assert isinstance(instance, org::structure::UnresolvedOperation)

@given(instance=org::structure::UnresolvedOperation_strategy)
def test_org::structure::unresolvedoperation_operationIdentifier_type(instance):
    assert isinstance(instance.operationIdentifier, str)


@given(instance=org::structure::UnresolvedOperation_strategy)
def test_org::structure::unresolvedoperation_operationIdentifier_setter(instance):
    original = instance.operationIdentifier
    instance.operationIdentifier = original
    assert instance.operationIdentifier == original

@given(instance=structure::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_structure::multiplicityelement_instantiation(instance):
    assert isinstance(instance, structure::MultiplicityElement)

@given(instance=org::structure::Property_strategy)
@settings(max_examples=50)
def test_org::structure::property_instantiation(instance):
    assert isinstance(instance, org::structure::Property)

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isSetterAbstract_type(instance):
    assert isinstance(instance.isSetterAbstract, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isSetterAbstract_setter(instance):
    original = instance.isSetterAbstract
    instance.isSetterAbstract = original
    assert instance.isSetterAbstract == original

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isID_type(instance):
    assert isinstance(instance.isID, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isGetterAbstract_type(instance):
    assert isinstance(instance.isGetterAbstract, str)


@given(instance=org::structure::Property_strategy)
def test_org::structure::property_isGetterAbstract_setter(instance):
    original = instance.isGetterAbstract
    instance.isGetterAbstract = original
    assert instance.isGetterAbstract == original

@given(instance=org::structure::Operation_strategy)
@settings(max_examples=50)
def test_org::structure::operation_instantiation(instance):
    assert isinstance(instance, org::structure::Operation)

@given(instance=org::structure::Operation_strategy)
def test_org::structure::operation_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=org::structure::Operation_strategy)
def test_org::structure::operation_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=org::structure::Operation_strategy)
def test_org::structure::operation_uniqueName_type(instance):
    assert isinstance(instance.uniqueName, str)


@given(instance=org::structure::Operation_strategy)
def test_org::structure::operation_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original

@given(instance=structure::Tag_strategy)
@settings(max_examples=50)
def test_structure::tag_instantiation(instance):
    assert isinstance(instance, structure::Tag)

@given(instance=org::structure::KermetaModelElement_strategy)
@settings(max_examples=50)
def test_org::structure::kermetamodelelement_instantiation(instance):
    assert isinstance(instance, org::structure::KermetaModelElement)
