import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    structure_Metamodel,
    structure_ModelTypeDefinitionBinding,
    TypeDefinition,
    org_structure_ModelTypeDefinition,
    org_structure_ModelElementTypeDefinition,
    AdaptationOperator,
    org_structure_OperationAdaptationOperator,
    org_structure_PropertyAdaptationOperator,
    structure_AdaptationParameter,
    structure_OperationBinding,
    structure_PropertyBinding,
    structure_ModelTypeDefinition,
    structure_EnumerationBinding,
    structure_UseAdaptationOperator,
    structure_ClassDefinitionBinding,
    TypeVariable,
    org_structure_ObjectTypeVariable,
    structure_ModelTypeVariable,
    ObjectTypeVariable,
    org_structure_VirtualType,
    structure_VirtualType,
    org_structure_ModelTypeVariable,
    structure_GenericTypeDefinition,
    structure_TypeVariableBinding,
    Type,
    org_structure_ModelType,
    org_structure_VoidType,
    org_structure_ParameterizedType,
    ModelElementTypeDefinition,
    org_structure_GenericTypeDefinition,
    structure_FilteredMetamodelReference,
    structure_ModelTypeDefinitionContainer,
    GenericTypeDefinition,
    org_structure_ClassDefinition,
    DataType,
    org_structure_Enumeration,
    org_structure_PrimitiveType,
    structure_AdaptationOperator,
    structure_Package,
    structure_ModelElementTypeDefinitionContainer,
    structure_ModelElementTypeDefinition,
    structure_Class,
    ParameterizedType,
    org_structure_Class,
    structure_NamedElement,
    org_structure_Package,
    TypedElement,
    org_structure_AdaptationParameter,
    org_structure_MultiplicityElement,
    structure_Enumeration,
    NamedElement,
    org_structure_Constraint,
    org_structure_AdaptationOperator,
    org_structure_ModelElementTypeDefinitionContainer,
    org_structure_EnumerationLiteral,
    structure_UnresolvedProperty,
    structure_Constraint,
    structure_AbstractProperty,
    structure_TypeVariable,
    structure_ClassDefinition,
    structure_UnresolvedOperation,
    structure_Using,
    structure_Parameter,
    structure_AbstractOperation,
    structure_MultiplicityElement,
    org_structure_Property,
    org_structure_Operation,
    structure_Tag,
    org_structure_KermetaModelElement,
    structure_ModelTransformation,
    structure_EnumerationLiteral,
    structure_Property,
    structure_Operation,
    CallFeature,
    org_behavior_CallProperty,
    org_behavior_CallModelTransformation,
    org_behavior_CallOperation,
    Literal,
    structure_UnresolvedReference,
    org_structure_UnresolvedModelTransformation,
    org_structure_UnresolvedProperty,
    org_structure_UnresolvedModelTypeDefinition,
    org_structure_UnresolvedTypeVariable,
    org_structure_UnresolvedAdaptationOperator,
    org_behavior_VoidLiteral,
    org_behavior_CallTypeLiteral,
    org_behavior_BooleanLiteral,
    org_behavior_StringLiteral,
    org_behavior_IntegerLiteral,
    behavior_LambdaParameter,
    MultiplicityElement,
    org_structure_Parameter,
    org_structure_ModelTransformation,
    org_behavior_TypeReference,
    behavior_TypeReference,
    KermetaModelElement,
    org_structure_UnresolvedReference,
    org_structure_ClassDefinitionBinding,
    org_structure_UseAdaptationOperator,
    org_structure_Tag,
    org_structure_FilteredMetamodelReference,
    org_structure_TypeContainer,
    org_structure_PropertyBinding,
    org_structure_Type,
    org_structure_EnumerationBinding,
    org_structure_Using,
    org_structure_NamedElement,
    org_structure_AbstractProperty,
    org_structure_OperationBinding,
    org_structure_AbstractOperation,
    org_structure_ModelTypeDefinitionContainer,
    org_behavior_LambdaParameter,
    org_structure_Model,
    org_behavior_Rescue,
    CallVariable,
    org_behavior_CallResult,
    CallOperation,
    org_behavior_CallSuperOperation,
    CallExpression,
    org_behavior_CallValue,
    org_behavior_CallEnumLiteral,
    org_behavior_CallFeature,
    org_behavior_CallVariable,
    behavior_Rescue,
    structure_Type,
    org_structure_UnresolvedInferredType,
    org_structure_DataType,
    structure_TypeContainer,
    org_structure_UnresolvedOperation,
    org_structure_TypeVariable,
    org_structure_ProductType,
    org_structure_FunctionType,
    org_structure_UnresolvedType,
    org_structure_TypedElement,
    org_structure_TypeDefinition,
    structure_KermetaModelElement,
    org_structure_ModelTypeDefinitionBinding,
    org_structure_Metamodel,
    org_structure_TypeVariableBinding,
    org_behavior_Expression,
    behavior_Expression,
    behavior_CallExpression,
    org_behavior_UnresolvedCall,
    Expression,
    org_behavior_Literal,
    org_behavior_Raise,
    org_behavior_JavaStaticCall,
    org_behavior_CallExpression,
    org_behavior_LambdaExpression,
    org_behavior_Conditional,
    org_behavior_VariableDecl,
    org_behavior_SelfExpression,
    org_behavior_Loop,
    org_behavior_EmptyExpression,
    org_behavior_Block,
    org_behavior_Assignment,
    ConstraintType,
    ConstraintLanguage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structure_metamodel_is_not_abstract():
    assert not inspect.isabstract(structure_Metamodel)


def test_structure_metamodel_constructor_exists():
    assert callable(structure_Metamodel.__init__)


def test_structure_metamodel_constructor_args():
    sig = inspect.signature(structure_Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_structure_modeltypedefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(structure_ModelTypeDefinitionBinding)


def test_structure_modeltypedefinitionbinding_constructor_exists():
    assert callable(structure_ModelTypeDefinitionBinding.__init__)


def test_structure_modeltypedefinitionbinding_constructor_args():
    sig = inspect.signature(structure_ModelTypeDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modeltypedefinition_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelTypeDefinition)


def test_org_structure_modeltypedefinition_constructor_exists():
    assert callable(org_structure_ModelTypeDefinition.__init__)


def test_org_structure_modeltypedefinition_constructor_args():
    sig = inspect.signature(org_structure_ModelTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modelelementtypedefinition_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelElementTypeDefinition)


def test_org_structure_modelelementtypedefinition_constructor_exists():
    assert callable(org_structure_ModelElementTypeDefinition.__init__)


def test_org_structure_modelelementtypedefinition_constructor_args():
    sig = inspect.signature(org_structure_ModelElementTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adaptationoperator_is_not_abstract():
    assert not inspect.isabstract(AdaptationOperator)


def test_adaptationoperator_constructor_exists():
    assert callable(AdaptationOperator.__init__)


def test_adaptationoperator_constructor_args():
    sig = inspect.signature(AdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_operationadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org_structure_OperationAdaptationOperator)


def test_org_structure_operationadaptationoperator_constructor_exists():
    assert callable(org_structure_OperationAdaptationOperator.__init__)


def test_org_structure_operationadaptationoperator_constructor_args():
    sig = inspect.signature(org_structure_OperationAdaptationOperator.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_org_structure_operationadaptationoperator_has_body():
    assert hasattr(org_structure_OperationAdaptationOperator, "body")
    descriptor = None
    for klass in org_structure_OperationAdaptationOperator.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_propertyadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org_structure_PropertyAdaptationOperator)


def test_org_structure_propertyadaptationoperator_constructor_exists():
    assert callable(org_structure_PropertyAdaptationOperator.__init__)


def test_org_structure_propertyadaptationoperator_constructor_args():
    sig = inspect.signature(org_structure_PropertyAdaptationOperator.__init__)
    params = list(sig.parameters.keys())
    assert "remover" in params, "Missing parameter 'remover'"
    assert "getter" in params, "Missing parameter 'getter'"
    assert "setter" in params, "Missing parameter 'setter'"
    assert "adder" in params, "Missing parameter 'adder'"

def test_org_structure_propertyadaptationoperator_has_remover():
    assert hasattr(org_structure_PropertyAdaptationOperator, "remover")
    descriptor = None
    for klass in org_structure_PropertyAdaptationOperator.__mro__:
        if "remover" in klass.__dict__:
            descriptor = klass.__dict__["remover"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_propertyadaptationoperator_has_getter():
    assert hasattr(org_structure_PropertyAdaptationOperator, "getter")
    descriptor = None
    for klass in org_structure_PropertyAdaptationOperator.__mro__:
        if "getter" in klass.__dict__:
            descriptor = klass.__dict__["getter"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_propertyadaptationoperator_has_setter():
    assert hasattr(org_structure_PropertyAdaptationOperator, "setter")
    descriptor = None
    for klass in org_structure_PropertyAdaptationOperator.__mro__:
        if "setter" in klass.__dict__:
            descriptor = klass.__dict__["setter"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_propertyadaptationoperator_has_adder():
    assert hasattr(org_structure_PropertyAdaptationOperator, "adder")
    descriptor = None
    for klass in org_structure_PropertyAdaptationOperator.__mro__:
        if "adder" in klass.__dict__:
            descriptor = klass.__dict__["adder"]
            break
    assert isinstance(descriptor, property)



def test_structure_adaptationparameter_is_not_abstract():
    assert not inspect.isabstract(structure_AdaptationParameter)


def test_structure_adaptationparameter_constructor_exists():
    assert callable(structure_AdaptationParameter.__init__)


def test_structure_adaptationparameter_constructor_args():
    sig = inspect.signature(structure_AdaptationParameter.__init__)
    params = list(sig.parameters.keys())



def test_structure_operationbinding_is_not_abstract():
    assert not inspect.isabstract(structure_OperationBinding)


def test_structure_operationbinding_constructor_exists():
    assert callable(structure_OperationBinding.__init__)


def test_structure_operationbinding_constructor_args():
    sig = inspect.signature(structure_OperationBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure_propertybinding_is_not_abstract():
    assert not inspect.isabstract(structure_PropertyBinding)


def test_structure_propertybinding_constructor_exists():
    assert callable(structure_PropertyBinding.__init__)


def test_structure_propertybinding_constructor_args():
    sig = inspect.signature(structure_PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure_modeltypedefinition_is_not_abstract():
    assert not inspect.isabstract(structure_ModelTypeDefinition)


def test_structure_modeltypedefinition_constructor_exists():
    assert callable(structure_ModelTypeDefinition.__init__)


def test_structure_modeltypedefinition_constructor_args():
    sig = inspect.signature(structure_ModelTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure_enumerationbinding_is_not_abstract():
    assert not inspect.isabstract(structure_EnumerationBinding)


def test_structure_enumerationbinding_constructor_exists():
    assert callable(structure_EnumerationBinding.__init__)


def test_structure_enumerationbinding_constructor_args():
    sig = inspect.signature(structure_EnumerationBinding.__init__)
    params = list(sig.parameters.keys())



def test_structure_useadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(structure_UseAdaptationOperator)


def test_structure_useadaptationoperator_constructor_exists():
    assert callable(structure_UseAdaptationOperator.__init__)


def test_structure_useadaptationoperator_constructor_args():
    sig = inspect.signature(structure_UseAdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_structure_classdefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(structure_ClassDefinitionBinding)


def test_structure_classdefinitionbinding_constructor_exists():
    assert callable(structure_ClassDefinitionBinding.__init__)


def test_structure_classdefinitionbinding_constructor_args():
    sig = inspect.signature(structure_ClassDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_typevariable_is_not_abstract():
    assert not inspect.isabstract(TypeVariable)


def test_typevariable_constructor_exists():
    assert callable(TypeVariable.__init__)


def test_typevariable_constructor_args():
    sig = inspect.signature(TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_objecttypevariable_is_not_abstract():
    assert not inspect.isabstract(org_structure_ObjectTypeVariable)


def test_org_structure_objecttypevariable_constructor_exists():
    assert callable(org_structure_ObjectTypeVariable.__init__)


def test_org_structure_objecttypevariable_constructor_args():
    sig = inspect.signature(org_structure_ObjectTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_structure_modeltypevariable_is_not_abstract():
    assert not inspect.isabstract(structure_ModelTypeVariable)


def test_structure_modeltypevariable_constructor_exists():
    assert callable(structure_ModelTypeVariable.__init__)


def test_structure_modeltypevariable_constructor_args():
    sig = inspect.signature(structure_ModelTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_objecttypevariable_is_not_abstract():
    assert not inspect.isabstract(ObjectTypeVariable)


def test_objecttypevariable_constructor_exists():
    assert callable(ObjectTypeVariable.__init__)


def test_objecttypevariable_constructor_args():
    sig = inspect.signature(ObjectTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_virtualtype_is_not_abstract():
    assert not inspect.isabstract(org_structure_VirtualType)


def test_org_structure_virtualtype_constructor_exists():
    assert callable(org_structure_VirtualType.__init__)


def test_org_structure_virtualtype_constructor_args():
    sig = inspect.signature(org_structure_VirtualType.__init__)
    params = list(sig.parameters.keys())



def test_structure_virtualtype_is_not_abstract():
    assert not inspect.isabstract(structure_VirtualType)


def test_structure_virtualtype_constructor_exists():
    assert callable(structure_VirtualType.__init__)


def test_structure_virtualtype_constructor_args():
    sig = inspect.signature(structure_VirtualType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modeltypevariable_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelTypeVariable)


def test_org_structure_modeltypevariable_constructor_exists():
    assert callable(org_structure_ModelTypeVariable.__init__)


def test_org_structure_modeltypevariable_constructor_args():
    sig = inspect.signature(org_structure_ModelTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_structure_generictypedefinition_is_not_abstract():
    assert not inspect.isabstract(structure_GenericTypeDefinition)


def test_structure_generictypedefinition_constructor_exists():
    assert callable(structure_GenericTypeDefinition.__init__)


def test_structure_generictypedefinition_constructor_args():
    sig = inspect.signature(structure_GenericTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure_typevariablebinding_is_not_abstract():
    assert not inspect.isabstract(structure_TypeVariableBinding)


def test_structure_typevariablebinding_constructor_exists():
    assert callable(structure_TypeVariableBinding.__init__)


def test_structure_typevariablebinding_constructor_args():
    sig = inspect.signature(structure_TypeVariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modeltype_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelType)


def test_org_structure_modeltype_constructor_exists():
    assert callable(org_structure_ModelType.__init__)


def test_org_structure_modeltype_constructor_args():
    sig = inspect.signature(org_structure_ModelType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_voidtype_is_not_abstract():
    assert not inspect.isabstract(org_structure_VoidType)


def test_org_structure_voidtype_constructor_exists():
    assert callable(org_structure_VoidType.__init__)


def test_org_structure_voidtype_constructor_args():
    sig = inspect.signature(org_structure_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(org_structure_ParameterizedType)


def test_org_structure_parameterizedtype_constructor_exists():
    assert callable(org_structure_ParameterizedType.__init__)


def test_org_structure_parameterizedtype_constructor_args():
    sig = inspect.signature(org_structure_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_modelelementtypedefinition_is_not_abstract():
    assert not inspect.isabstract(ModelElementTypeDefinition)


def test_modelelementtypedefinition_constructor_exists():
    assert callable(ModelElementTypeDefinition.__init__)


def test_modelelementtypedefinition_constructor_args():
    sig = inspect.signature(ModelElementTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_generictypedefinition_is_not_abstract():
    assert not inspect.isabstract(org_structure_GenericTypeDefinition)


def test_org_structure_generictypedefinition_constructor_exists():
    assert callable(org_structure_GenericTypeDefinition.__init__)


def test_org_structure_generictypedefinition_constructor_args():
    sig = inspect.signature(org_structure_GenericTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure_filteredmetamodelreference_is_not_abstract():
    assert not inspect.isabstract(structure_FilteredMetamodelReference)


def test_structure_filteredmetamodelreference_constructor_exists():
    assert callable(structure_FilteredMetamodelReference.__init__)


def test_structure_filteredmetamodelreference_constructor_args():
    sig = inspect.signature(structure_FilteredMetamodelReference.__init__)
    params = list(sig.parameters.keys())



def test_structure_modeltypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(structure_ModelTypeDefinitionContainer)


def test_structure_modeltypedefinitioncontainer_constructor_exists():
    assert callable(structure_ModelTypeDefinitionContainer.__init__)


def test_structure_modeltypedefinitioncontainer_constructor_args():
    sig = inspect.signature(structure_ModelTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_generictypedefinition_is_not_abstract():
    assert not inspect.isabstract(GenericTypeDefinition)


def test_generictypedefinition_constructor_exists():
    assert callable(GenericTypeDefinition.__init__)


def test_generictypedefinition_constructor_args():
    sig = inspect.signature(GenericTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_classdefinition_is_not_abstract():
    assert not inspect.isabstract(org_structure_ClassDefinition)


def test_org_structure_classdefinition_constructor_exists():
    assert callable(org_structure_ClassDefinition.__init__)


def test_org_structure_classdefinition_constructor_args():
    sig = inspect.signature(org_structure_ClassDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isSingleton" in params, "Missing parameter 'isSingleton'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_org_structure_classdefinition_has_isFinal():
    assert hasattr(org_structure_ClassDefinition, "isFinal")
    descriptor = None
    for klass in org_structure_ClassDefinition.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_classdefinition_has_isSingleton():
    assert hasattr(org_structure_ClassDefinition, "isSingleton")
    descriptor = None
    for klass in org_structure_ClassDefinition.__mro__:
        if "isSingleton" in klass.__dict__:
            descriptor = klass.__dict__["isSingleton"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_classdefinition_has_isAbstract():
    assert hasattr(org_structure_ClassDefinition, "isAbstract")
    descriptor = None
    for klass in org_structure_ClassDefinition.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_enumeration_is_not_abstract():
    assert not inspect.isabstract(org_structure_Enumeration)


def test_org_structure_enumeration_constructor_exists():
    assert callable(org_structure_Enumeration.__init__)


def test_org_structure_enumeration_constructor_args():
    sig = inspect.signature(org_structure_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_primitivetype_is_not_abstract():
    assert not inspect.isabstract(org_structure_PrimitiveType)


def test_org_structure_primitivetype_constructor_exists():
    assert callable(org_structure_PrimitiveType.__init__)


def test_org_structure_primitivetype_constructor_args():
    sig = inspect.signature(org_structure_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_structure_adaptationoperator_is_not_abstract():
    assert not inspect.isabstract(structure_AdaptationOperator)


def test_structure_adaptationoperator_constructor_exists():
    assert callable(structure_AdaptationOperator.__init__)


def test_structure_adaptationoperator_constructor_args():
    sig = inspect.signature(structure_AdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_structure_package_is_not_abstract():
    assert not inspect.isabstract(structure_Package)


def test_structure_package_constructor_exists():
    assert callable(structure_Package.__init__)


def test_structure_package_constructor_args():
    sig = inspect.signature(structure_Package.__init__)
    params = list(sig.parameters.keys())



def test_structure_modelelementtypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(structure_ModelElementTypeDefinitionContainer)


def test_structure_modelelementtypedefinitioncontainer_constructor_exists():
    assert callable(structure_ModelElementTypeDefinitionContainer.__init__)


def test_structure_modelelementtypedefinitioncontainer_constructor_args():
    sig = inspect.signature(structure_ModelElementTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_structure_modelelementtypedefinition_is_not_abstract():
    assert not inspect.isabstract(structure_ModelElementTypeDefinition)


def test_structure_modelelementtypedefinition_constructor_exists():
    assert callable(structure_ModelElementTypeDefinition.__init__)


def test_structure_modelelementtypedefinition_constructor_args():
    sig = inspect.signature(structure_ModelElementTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure_class_is_not_abstract():
    assert not inspect.isabstract(structure_Class)


def test_structure_class_constructor_exists():
    assert callable(structure_Class.__init__)


def test_structure_class_constructor_args():
    sig = inspect.signature(structure_Class.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ParameterizedType)


def test_parameterizedtype_constructor_exists():
    assert callable(ParameterizedType.__init__)


def test_parameterizedtype_constructor_args():
    sig = inspect.signature(ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_class_is_not_abstract():
    assert not inspect.isabstract(org_structure_Class)


def test_org_structure_class_constructor_exists():
    assert callable(org_structure_Class.__init__)


def test_org_structure_class_constructor_args():
    sig = inspect.signature(org_structure_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_org_structure_class_has_name():
    assert hasattr(org_structure_Class, "name")
    descriptor = None
    for klass in org_structure_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_class_has_isAbstract():
    assert hasattr(org_structure_Class, "isAbstract")
    descriptor = None
    for klass in org_structure_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_structure_namedelement_is_not_abstract():
    assert not inspect.isabstract(structure_NamedElement)


def test_structure_namedelement_constructor_exists():
    assert callable(structure_NamedElement.__init__)


def test_structure_namedelement_constructor_args():
    sig = inspect.signature(structure_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_package_is_not_abstract():
    assert not inspect.isabstract(org_structure_Package)


def test_org_structure_package_constructor_exists():
    assert callable(org_structure_Package.__init__)


def test_org_structure_package_constructor_args():
    sig = inspect.signature(org_structure_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_org_structure_package_has_uri():
    assert hasattr(org_structure_Package, "uri")
    descriptor = None
    for klass in org_structure_Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_adaptationparameter_is_not_abstract():
    assert not inspect.isabstract(org_structure_AdaptationParameter)


def test_org_structure_adaptationparameter_constructor_exists():
    assert callable(org_structure_AdaptationParameter.__init__)


def test_org_structure_adaptationparameter_constructor_args():
    sig = inspect.signature(org_structure_AdaptationParameter.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(org_structure_MultiplicityElement)


def test_org_structure_multiplicityelement_constructor_exists():
    assert callable(org_structure_MultiplicityElement.__init__)


def test_org_structure_multiplicityelement_constructor_args():
    sig = inspect.signature(org_structure_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_org_structure_multiplicityelement_has_isOrdered():
    assert hasattr(org_structure_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in org_structure_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_multiplicityelement_has_isUnique():
    assert hasattr(org_structure_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in org_structure_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_multiplicityelement_has_lower():
    assert hasattr(org_structure_MultiplicityElement, "lower")
    descriptor = None
    for klass in org_structure_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_multiplicityelement_has_upper():
    assert hasattr(org_structure_MultiplicityElement, "upper")
    descriptor = None
    for klass in org_structure_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_structure_enumeration_is_not_abstract():
    assert not inspect.isabstract(structure_Enumeration)


def test_structure_enumeration_constructor_exists():
    assert callable(structure_Enumeration.__init__)


def test_structure_enumeration_constructor_args():
    sig = inspect.signature(structure_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_constraint_is_not_abstract():
    assert not inspect.isabstract(org_structure_Constraint)


def test_org_structure_constraint_constructor_exists():
    assert callable(org_structure_Constraint.__init__)


def test_org_structure_constraint_constructor_args():
    sig = inspect.signature(org_structure_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"
    assert "language" in params, "Missing parameter 'language'"

def test_org_structure_constraint_has_stereotype():
    assert hasattr(org_structure_Constraint, "stereotype")
    descriptor = None
    for klass in org_structure_Constraint.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_constraint_has_language():
    assert hasattr(org_structure_Constraint, "language")
    descriptor = None
    for klass in org_structure_Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_adaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org_structure_AdaptationOperator)


def test_org_structure_adaptationoperator_constructor_exists():
    assert callable(org_structure_AdaptationOperator.__init__)


def test_org_structure_adaptationoperator_constructor_args():
    sig = inspect.signature(org_structure_AdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modelelementtypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelElementTypeDefinitionContainer)


def test_org_structure_modelelementtypedefinitioncontainer_constructor_exists():
    assert callable(org_structure_ModelElementTypeDefinitionContainer.__init__)


def test_org_structure_modelelementtypedefinitioncontainer_constructor_args():
    sig = inspect.signature(org_structure_ModelElementTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(org_structure_EnumerationLiteral)


def test_org_structure_enumerationliteral_constructor_exists():
    assert callable(org_structure_EnumerationLiteral.__init__)


def test_org_structure_enumerationliteral_constructor_args():
    sig = inspect.signature(org_structure_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_structure_unresolvedproperty_is_not_abstract():
    assert not inspect.isabstract(structure_UnresolvedProperty)


def test_structure_unresolvedproperty_constructor_exists():
    assert callable(structure_UnresolvedProperty.__init__)


def test_structure_unresolvedproperty_constructor_args():
    sig = inspect.signature(structure_UnresolvedProperty.__init__)
    params = list(sig.parameters.keys())



def test_structure_constraint_is_not_abstract():
    assert not inspect.isabstract(structure_Constraint)


def test_structure_constraint_constructor_exists():
    assert callable(structure_Constraint.__init__)


def test_structure_constraint_constructor_args():
    sig = inspect.signature(structure_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_structure_abstractproperty_is_not_abstract():
    assert not inspect.isabstract(structure_AbstractProperty)


def test_structure_abstractproperty_constructor_exists():
    assert callable(structure_AbstractProperty.__init__)


def test_structure_abstractproperty_constructor_args():
    sig = inspect.signature(structure_AbstractProperty.__init__)
    params = list(sig.parameters.keys())



def test_structure_typevariable_is_not_abstract():
    assert not inspect.isabstract(structure_TypeVariable)


def test_structure_typevariable_constructor_exists():
    assert callable(structure_TypeVariable.__init__)


def test_structure_typevariable_constructor_args():
    sig = inspect.signature(structure_TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_structure_classdefinition_is_not_abstract():
    assert not inspect.isabstract(structure_ClassDefinition)


def test_structure_classdefinition_constructor_exists():
    assert callable(structure_ClassDefinition.__init__)


def test_structure_classdefinition_constructor_args():
    sig = inspect.signature(structure_ClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_structure_unresolvedoperation_is_not_abstract():
    assert not inspect.isabstract(structure_UnresolvedOperation)


def test_structure_unresolvedoperation_constructor_exists():
    assert callable(structure_UnresolvedOperation.__init__)


def test_structure_unresolvedoperation_constructor_args():
    sig = inspect.signature(structure_UnresolvedOperation.__init__)
    params = list(sig.parameters.keys())



def test_structure_using_is_not_abstract():
    assert not inspect.isabstract(structure_Using)


def test_structure_using_constructor_exists():
    assert callable(structure_Using.__init__)


def test_structure_using_constructor_args():
    sig = inspect.signature(structure_Using.__init__)
    params = list(sig.parameters.keys())



def test_structure_parameter_is_not_abstract():
    assert not inspect.isabstract(structure_Parameter)


def test_structure_parameter_constructor_exists():
    assert callable(structure_Parameter.__init__)


def test_structure_parameter_constructor_args():
    sig = inspect.signature(structure_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_structure_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(structure_AbstractOperation)


def test_structure_abstractoperation_constructor_exists():
    assert callable(structure_AbstractOperation.__init__)


def test_structure_abstractoperation_constructor_args():
    sig = inspect.signature(structure_AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_structure_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(structure_MultiplicityElement)


def test_structure_multiplicityelement_constructor_exists():
    assert callable(structure_MultiplicityElement.__init__)


def test_structure_multiplicityelement_constructor_args():
    sig = inspect.signature(structure_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_property_is_not_abstract():
    assert not inspect.isabstract(org_structure_Property)


def test_org_structure_property_constructor_exists():
    assert callable(org_structure_Property.__init__)


def test_org_structure_property_constructor_args():
    sig = inspect.signature(org_structure_Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isGetterAbstract" in params, "Missing parameter 'isGetterAbstract'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSetterAbstract" in params, "Missing parameter 'isSetterAbstract'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_org_structure_property_has_default():
    assert hasattr(org_structure_Property, "default")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_property_has_isComposite():
    assert hasattr(org_structure_Property, "isComposite")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_property_has_isID():
    assert hasattr(org_structure_Property, "isID")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_property_has_isGetterAbstract():
    assert hasattr(org_structure_Property, "isGetterAbstract")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "isGetterAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isGetterAbstract"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_property_has_isReadOnly():
    assert hasattr(org_structure_Property, "isReadOnly")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_property_has_isSetterAbstract():
    assert hasattr(org_structure_Property, "isSetterAbstract")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "isSetterAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isSetterAbstract"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_property_has_isDerived():
    assert hasattr(org_structure_Property, "isDerived")
    descriptor = None
    for klass in org_structure_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_operation_is_not_abstract():
    assert not inspect.isabstract(org_structure_Operation)


def test_org_structure_operation_constructor_exists():
    assert callable(org_structure_Operation.__init__)


def test_org_structure_operation_constructor_args():
    sig = inspect.signature(org_structure_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"

def test_org_structure_operation_has_isAbstract():
    assert hasattr(org_structure_Operation, "isAbstract")
    descriptor = None
    for klass in org_structure_Operation.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_operation_has_uniqueName():
    assert hasattr(org_structure_Operation, "uniqueName")
    descriptor = None
    for klass in org_structure_Operation.__mro__:
        if "uniqueName" in klass.__dict__:
            descriptor = klass.__dict__["uniqueName"]
            break
    assert isinstance(descriptor, property)



def test_structure_tag_is_not_abstract():
    assert not inspect.isabstract(structure_Tag)


def test_structure_tag_constructor_exists():
    assert callable(structure_Tag.__init__)


def test_structure_tag_constructor_args():
    sig = inspect.signature(structure_Tag.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_kermetamodelelement_is_not_abstract():
    assert not inspect.isabstract(org_structure_KermetaModelElement)


def test_org_structure_kermetamodelelement_constructor_exists():
    assert callable(org_structure_KermetaModelElement.__init__)


def test_org_structure_kermetamodelelement_constructor_args():
    sig = inspect.signature(org_structure_KermetaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_structure_modeltransformation_is_not_abstract():
    assert not inspect.isabstract(structure_ModelTransformation)


def test_structure_modeltransformation_constructor_exists():
    assert callable(structure_ModelTransformation.__init__)


def test_structure_modeltransformation_constructor_args():
    sig = inspect.signature(structure_ModelTransformation.__init__)
    params = list(sig.parameters.keys())



def test_structure_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(structure_EnumerationLiteral)


def test_structure_enumerationliteral_constructor_exists():
    assert callable(structure_EnumerationLiteral.__init__)


def test_structure_enumerationliteral_constructor_args():
    sig = inspect.signature(structure_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_structure_property_is_not_abstract():
    assert not inspect.isabstract(structure_Property)


def test_structure_property_constructor_exists():
    assert callable(structure_Property.__init__)


def test_structure_property_constructor_args():
    sig = inspect.signature(structure_Property.__init__)
    params = list(sig.parameters.keys())



def test_structure_operation_is_not_abstract():
    assert not inspect.isabstract(structure_Operation)


def test_structure_operation_constructor_exists():
    assert callable(structure_Operation.__init__)


def test_structure_operation_constructor_args():
    sig = inspect.signature(structure_Operation.__init__)
    params = list(sig.parameters.keys())



def test_callfeature_is_not_abstract():
    assert not inspect.isabstract(CallFeature)


def test_callfeature_constructor_exists():
    assert callable(CallFeature.__init__)


def test_callfeature_constructor_args():
    sig = inspect.signature(CallFeature.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callproperty_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallProperty)


def test_org_behavior_callproperty_constructor_exists():
    assert callable(org_behavior_CallProperty.__init__)


def test_org_behavior_callproperty_constructor_args():
    sig = inspect.signature(org_behavior_CallProperty.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callmodeltransformation_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallModelTransformation)


def test_org_behavior_callmodeltransformation_constructor_exists():
    assert callable(org_behavior_CallModelTransformation.__init__)


def test_org_behavior_callmodeltransformation_constructor_args():
    sig = inspect.signature(org_behavior_CallModelTransformation.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_calloperation_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallOperation)


def test_org_behavior_calloperation_constructor_exists():
    assert callable(org_behavior_CallOperation.__init__)


def test_org_behavior_calloperation_constructor_args():
    sig = inspect.signature(org_behavior_CallOperation.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_structure_unresolvedreference_is_not_abstract():
    assert not inspect.isabstract(structure_UnresolvedReference)


def test_structure_unresolvedreference_constructor_exists():
    assert callable(structure_UnresolvedReference.__init__)


def test_structure_unresolvedreference_constructor_args():
    sig = inspect.signature(structure_UnresolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedmodeltransformation_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedModelTransformation)


def test_org_structure_unresolvedmodeltransformation_constructor_exists():
    assert callable(org_structure_UnresolvedModelTransformation.__init__)


def test_org_structure_unresolvedmodeltransformation_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedModelTransformation.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedproperty_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedProperty)


def test_org_structure_unresolvedproperty_constructor_exists():
    assert callable(org_structure_UnresolvedProperty.__init__)


def test_org_structure_unresolvedproperty_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedProperty.__init__)
    params = list(sig.parameters.keys())
    assert "propertyIdentifier" in params, "Missing parameter 'propertyIdentifier'"

def test_org_structure_unresolvedproperty_has_propertyIdentifier():
    assert hasattr(org_structure_UnresolvedProperty, "propertyIdentifier")
    descriptor = None
    for klass in org_structure_UnresolvedProperty.__mro__:
        if "propertyIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["propertyIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_unresolvedmodeltypedefinition_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedModelTypeDefinition)


def test_org_structure_unresolvedmodeltypedefinition_constructor_exists():
    assert callable(org_structure_UnresolvedModelTypeDefinition.__init__)


def test_org_structure_unresolvedmodeltypedefinition_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedModelTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedtypevariable_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedTypeVariable)


def test_org_structure_unresolvedtypevariable_constructor_exists():
    assert callable(org_structure_UnresolvedTypeVariable.__init__)


def test_org_structure_unresolvedtypevariable_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedAdaptationOperator)


def test_org_structure_unresolvedadaptationoperator_constructor_exists():
    assert callable(org_structure_UnresolvedAdaptationOperator.__init__)


def test_org_structure_unresolvedadaptationoperator_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedAdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_voidliteral_is_not_abstract():
    assert not inspect.isabstract(org_behavior_VoidLiteral)


def test_org_behavior_voidliteral_constructor_exists():
    assert callable(org_behavior_VoidLiteral.__init__)


def test_org_behavior_voidliteral_constructor_args():
    sig = inspect.signature(org_behavior_VoidLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_calltypeliteral_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallTypeLiteral)


def test_org_behavior_calltypeliteral_constructor_exists():
    assert callable(org_behavior_CallTypeLiteral.__init__)


def test_org_behavior_calltypeliteral_constructor_args():
    sig = inspect.signature(org_behavior_CallTypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(org_behavior_BooleanLiteral)


def test_org_behavior_booleanliteral_constructor_exists():
    assert callable(org_behavior_BooleanLiteral.__init__)


def test_org_behavior_booleanliteral_constructor_args():
    sig = inspect.signature(org_behavior_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_org_behavior_booleanliteral_has_value():
    assert hasattr(org_behavior_BooleanLiteral, "value")
    descriptor = None
    for klass in org_behavior_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_stringliteral_is_not_abstract():
    assert not inspect.isabstract(org_behavior_StringLiteral)


def test_org_behavior_stringliteral_constructor_exists():
    assert callable(org_behavior_StringLiteral.__init__)


def test_org_behavior_stringliteral_constructor_args():
    sig = inspect.signature(org_behavior_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_org_behavior_stringliteral_has_value():
    assert hasattr(org_behavior_StringLiteral, "value")
    descriptor = None
    for klass in org_behavior_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_integerliteral_is_not_abstract():
    assert not inspect.isabstract(org_behavior_IntegerLiteral)


def test_org_behavior_integerliteral_constructor_exists():
    assert callable(org_behavior_IntegerLiteral.__init__)


def test_org_behavior_integerliteral_constructor_args():
    sig = inspect.signature(org_behavior_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_org_behavior_integerliteral_has_value():
    assert hasattr(org_behavior_IntegerLiteral, "value")
    descriptor = None
    for klass in org_behavior_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behavior_lambdaparameter_is_not_abstract():
    assert not inspect.isabstract(behavior_LambdaParameter)


def test_behavior_lambdaparameter_constructor_exists():
    assert callable(behavior_LambdaParameter.__init__)


def test_behavior_lambdaparameter_constructor_args():
    sig = inspect.signature(behavior_LambdaParameter.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_parameter_is_not_abstract():
    assert not inspect.isabstract(org_structure_Parameter)


def test_org_structure_parameter_constructor_exists():
    assert callable(org_structure_Parameter.__init__)


def test_org_structure_parameter_constructor_args():
    sig = inspect.signature(org_structure_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modeltransformation_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelTransformation)


def test_org_structure_modeltransformation_constructor_exists():
    assert callable(org_structure_ModelTransformation.__init__)


def test_org_structure_modeltransformation_constructor_args():
    sig = inspect.signature(org_structure_ModelTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_org_structure_modeltransformation_has_isAbstract():
    assert hasattr(org_structure_ModelTransformation, "isAbstract")
    descriptor = None
    for klass in org_structure_ModelTransformation.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_typereference_is_not_abstract():
    assert not inspect.isabstract(org_behavior_TypeReference)


def test_org_behavior_typereference_constructor_exists():
    assert callable(org_behavior_TypeReference.__init__)


def test_org_behavior_typereference_constructor_args():
    sig = inspect.signature(org_behavior_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_behavior_typereference_is_not_abstract():
    assert not inspect.isabstract(behavior_TypeReference)


def test_behavior_typereference_constructor_exists():
    assert callable(behavior_TypeReference.__init__)


def test_behavior_typereference_constructor_args():
    sig = inspect.signature(behavior_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_kermetamodelelement_is_not_abstract():
    assert not inspect.isabstract(KermetaModelElement)


def test_kermetamodelelement_constructor_exists():
    assert callable(KermetaModelElement.__init__)


def test_kermetamodelelement_constructor_args():
    sig = inspect.signature(KermetaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedreference_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedReference)


def test_org_structure_unresolvedreference_constructor_exists():
    assert callable(org_structure_UnresolvedReference.__init__)


def test_org_structure_unresolvedreference_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_classdefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(org_structure_ClassDefinitionBinding)


def test_org_structure_classdefinitionbinding_constructor_exists():
    assert callable(org_structure_ClassDefinitionBinding.__init__)


def test_org_structure_classdefinitionbinding_constructor_args():
    sig = inspect.signature(org_structure_ClassDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_useadaptationoperator_is_not_abstract():
    assert not inspect.isabstract(org_structure_UseAdaptationOperator)


def test_org_structure_useadaptationoperator_constructor_exists():
    assert callable(org_structure_UseAdaptationOperator.__init__)


def test_org_structure_useadaptationoperator_constructor_args():
    sig = inspect.signature(org_structure_UseAdaptationOperator.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_tag_is_not_abstract():
    assert not inspect.isabstract(org_structure_Tag)


def test_org_structure_tag_constructor_exists():
    assert callable(org_structure_Tag.__init__)


def test_org_structure_tag_constructor_args():
    sig = inspect.signature(org_structure_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_org_structure_tag_has_value():
    assert hasattr(org_structure_Tag, "value")
    descriptor = None
    for klass in org_structure_Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_tag_has_name():
    assert hasattr(org_structure_Tag, "name")
    descriptor = None
    for klass in org_structure_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_filteredmetamodelreference_is_not_abstract():
    assert not inspect.isabstract(org_structure_FilteredMetamodelReference)


def test_org_structure_filteredmetamodelreference_constructor_exists():
    assert callable(org_structure_FilteredMetamodelReference.__init__)


def test_org_structure_filteredmetamodelreference_constructor_args():
    sig = inspect.signature(org_structure_FilteredMetamodelReference.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_typecontainer_is_not_abstract():
    assert not inspect.isabstract(org_structure_TypeContainer)


def test_org_structure_typecontainer_constructor_exists():
    assert callable(org_structure_TypeContainer.__init__)


def test_org_structure_typecontainer_constructor_args():
    sig = inspect.signature(org_structure_TypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_propertybinding_is_not_abstract():
    assert not inspect.isabstract(org_structure_PropertyBinding)


def test_org_structure_propertybinding_constructor_exists():
    assert callable(org_structure_PropertyBinding.__init__)


def test_org_structure_propertybinding_constructor_args():
    sig = inspect.signature(org_structure_PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_type_is_not_abstract():
    assert not inspect.isabstract(org_structure_Type)


def test_org_structure_type_constructor_exists():
    assert callable(org_structure_Type.__init__)


def test_org_structure_type_constructor_args():
    sig = inspect.signature(org_structure_Type.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_enumerationbinding_is_not_abstract():
    assert not inspect.isabstract(org_structure_EnumerationBinding)


def test_org_structure_enumerationbinding_constructor_exists():
    assert callable(org_structure_EnumerationBinding.__init__)


def test_org_structure_enumerationbinding_constructor_args():
    sig = inspect.signature(org_structure_EnumerationBinding.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_using_is_not_abstract():
    assert not inspect.isabstract(org_structure_Using)


def test_org_structure_using_constructor_exists():
    assert callable(org_structure_Using.__init__)


def test_org_structure_using_constructor_args():
    sig = inspect.signature(org_structure_Using.__init__)
    params = list(sig.parameters.keys())
    assert "fromQName" in params, "Missing parameter 'fromQName'"
    assert "toName" in params, "Missing parameter 'toName'"

def test_org_structure_using_has_fromQName():
    assert hasattr(org_structure_Using, "fromQName")
    descriptor = None
    for klass in org_structure_Using.__mro__:
        if "fromQName" in klass.__dict__:
            descriptor = klass.__dict__["fromQName"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_using_has_toName():
    assert hasattr(org_structure_Using, "toName")
    descriptor = None
    for klass in org_structure_Using.__mro__:
        if "toName" in klass.__dict__:
            descriptor = klass.__dict__["toName"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_namedelement_is_not_abstract():
    assert not inspect.isabstract(org_structure_NamedElement)


def test_org_structure_namedelement_constructor_exists():
    assert callable(org_structure_NamedElement.__init__)


def test_org_structure_namedelement_constructor_args():
    sig = inspect.signature(org_structure_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org_structure_namedelement_has_name():
    assert hasattr(org_structure_NamedElement, "name")
    descriptor = None
    for klass in org_structure_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_abstractproperty_is_not_abstract():
    assert not inspect.isabstract(org_structure_AbstractProperty)


def test_org_structure_abstractproperty_constructor_exists():
    assert callable(org_structure_AbstractProperty.__init__)


def test_org_structure_abstractproperty_constructor_args():
    sig = inspect.signature(org_structure_AbstractProperty.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_operationbinding_is_not_abstract():
    assert not inspect.isabstract(org_structure_OperationBinding)


def test_org_structure_operationbinding_constructor_exists():
    assert callable(org_structure_OperationBinding.__init__)


def test_org_structure_operationbinding_constructor_args():
    sig = inspect.signature(org_structure_OperationBinding.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(org_structure_AbstractOperation)


def test_org_structure_abstractoperation_constructor_exists():
    assert callable(org_structure_AbstractOperation.__init__)


def test_org_structure_abstractoperation_constructor_args():
    sig = inspect.signature(org_structure_AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modeltypedefinitioncontainer_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelTypeDefinitionContainer)


def test_org_structure_modeltypedefinitioncontainer_constructor_exists():
    assert callable(org_structure_ModelTypeDefinitionContainer.__init__)


def test_org_structure_modeltypedefinitioncontainer_constructor_args():
    sig = inspect.signature(org_structure_ModelTypeDefinitionContainer.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_lambdaparameter_is_not_abstract():
    assert not inspect.isabstract(org_behavior_LambdaParameter)


def test_org_behavior_lambdaparameter_constructor_exists():
    assert callable(org_behavior_LambdaParameter.__init__)


def test_org_behavior_lambdaparameter_constructor_args():
    sig = inspect.signature(org_behavior_LambdaParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org_behavior_lambdaparameter_has_name():
    assert hasattr(org_behavior_LambdaParameter, "name")
    descriptor = None
    for klass in org_behavior_LambdaParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_model_is_not_abstract():
    assert not inspect.isabstract(org_structure_Model)


def test_org_structure_model_constructor_exists():
    assert callable(org_structure_Model.__init__)


def test_org_structure_model_constructor_args():
    sig = inspect.signature(org_structure_Model.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_rescue_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Rescue)


def test_org_behavior_rescue_constructor_exists():
    assert callable(org_behavior_Rescue.__init__)


def test_org_behavior_rescue_constructor_args():
    sig = inspect.signature(org_behavior_Rescue.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionName" in params, "Missing parameter 'exceptionName'"

def test_org_behavior_rescue_has_exceptionName():
    assert hasattr(org_behavior_Rescue, "exceptionName")
    descriptor = None
    for klass in org_behavior_Rescue.__mro__:
        if "exceptionName" in klass.__dict__:
            descriptor = klass.__dict__["exceptionName"]
            break
    assert isinstance(descriptor, property)



def test_callvariable_is_not_abstract():
    assert not inspect.isabstract(CallVariable)


def test_callvariable_constructor_exists():
    assert callable(CallVariable.__init__)


def test_callvariable_constructor_args():
    sig = inspect.signature(CallVariable.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callresult_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallResult)


def test_org_behavior_callresult_constructor_exists():
    assert callable(org_behavior_CallResult.__init__)


def test_org_behavior_callresult_constructor_args():
    sig = inspect.signature(org_behavior_CallResult.__init__)
    params = list(sig.parameters.keys())



def test_calloperation_is_not_abstract():
    assert not inspect.isabstract(CallOperation)


def test_calloperation_constructor_exists():
    assert callable(CallOperation.__init__)


def test_calloperation_constructor_args():
    sig = inspect.signature(CallOperation.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callsuperoperation_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallSuperOperation)


def test_org_behavior_callsuperoperation_constructor_exists():
    assert callable(org_behavior_CallSuperOperation.__init__)


def test_org_behavior_callsuperoperation_constructor_args():
    sig = inspect.signature(org_behavior_CallSuperOperation.__init__)
    params = list(sig.parameters.keys())



def test_callexpression_is_not_abstract():
    assert not inspect.isabstract(CallExpression)


def test_callexpression_constructor_exists():
    assert callable(CallExpression.__init__)


def test_callexpression_constructor_args():
    sig = inspect.signature(CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callvalue_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallValue)


def test_org_behavior_callvalue_constructor_exists():
    assert callable(org_behavior_CallValue.__init__)


def test_org_behavior_callvalue_constructor_args():
    sig = inspect.signature(org_behavior_CallValue.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callenumliteral_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallEnumLiteral)


def test_org_behavior_callenumliteral_constructor_exists():
    assert callable(org_behavior_CallEnumLiteral.__init__)


def test_org_behavior_callenumliteral_constructor_args():
    sig = inspect.signature(org_behavior_CallEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_callfeature_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallFeature)


def test_org_behavior_callfeature_constructor_exists():
    assert callable(org_behavior_CallFeature.__init__)


def test_org_behavior_callfeature_constructor_args():
    sig = inspect.signature(org_behavior_CallFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isAtpre" in params, "Missing parameter 'isAtpre'"

def test_org_behavior_callfeature_has_isAtpre():
    assert hasattr(org_behavior_CallFeature, "isAtpre")
    descriptor = None
    for klass in org_behavior_CallFeature.__mro__:
        if "isAtpre" in klass.__dict__:
            descriptor = klass.__dict__["isAtpre"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_callvariable_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallVariable)


def test_org_behavior_callvariable_constructor_exists():
    assert callable(org_behavior_CallVariable.__init__)


def test_org_behavior_callvariable_constructor_args():
    sig = inspect.signature(org_behavior_CallVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isAtpre" in params, "Missing parameter 'isAtpre'"

def test_org_behavior_callvariable_has_isAtpre():
    assert hasattr(org_behavior_CallVariable, "isAtpre")
    descriptor = None
    for klass in org_behavior_CallVariable.__mro__:
        if "isAtpre" in klass.__dict__:
            descriptor = klass.__dict__["isAtpre"]
            break
    assert isinstance(descriptor, property)



def test_behavior_rescue_is_not_abstract():
    assert not inspect.isabstract(behavior_Rescue)


def test_behavior_rescue_constructor_exists():
    assert callable(behavior_Rescue.__init__)


def test_behavior_rescue_constructor_args():
    sig = inspect.signature(behavior_Rescue.__init__)
    params = list(sig.parameters.keys())



def test_structure_type_is_not_abstract():
    assert not inspect.isabstract(structure_Type)


def test_structure_type_constructor_exists():
    assert callable(structure_Type.__init__)


def test_structure_type_constructor_args():
    sig = inspect.signature(structure_Type.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedinferredtype_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedInferredType)


def test_org_structure_unresolvedinferredtype_constructor_exists():
    assert callable(org_structure_UnresolvedInferredType.__init__)


def test_org_structure_unresolvedinferredtype_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedInferredType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_datatype_is_not_abstract():
    assert not inspect.isabstract(org_structure_DataType)


def test_org_structure_datatype_constructor_exists():
    assert callable(org_structure_DataType.__init__)


def test_org_structure_datatype_constructor_args():
    sig = inspect.signature(org_structure_DataType.__init__)
    params = list(sig.parameters.keys())



def test_structure_typecontainer_is_not_abstract():
    assert not inspect.isabstract(structure_TypeContainer)


def test_structure_typecontainer_constructor_exists():
    assert callable(structure_TypeContainer.__init__)


def test_structure_typecontainer_constructor_args():
    sig = inspect.signature(structure_TypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedoperation_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedOperation)


def test_org_structure_unresolvedoperation_constructor_exists():
    assert callable(org_structure_UnresolvedOperation.__init__)


def test_org_structure_unresolvedoperation_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operationIdentifier" in params, "Missing parameter 'operationIdentifier'"

def test_org_structure_unresolvedoperation_has_operationIdentifier():
    assert hasattr(org_structure_UnresolvedOperation, "operationIdentifier")
    descriptor = None
    for klass in org_structure_UnresolvedOperation.__mro__:
        if "operationIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["operationIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_typevariable_is_not_abstract():
    assert not inspect.isabstract(org_structure_TypeVariable)


def test_org_structure_typevariable_constructor_exists():
    assert callable(org_structure_TypeVariable.__init__)


def test_org_structure_typevariable_constructor_args():
    sig = inspect.signature(org_structure_TypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_producttype_is_not_abstract():
    assert not inspect.isabstract(org_structure_ProductType)


def test_org_structure_producttype_constructor_exists():
    assert callable(org_structure_ProductType.__init__)


def test_org_structure_producttype_constructor_args():
    sig = inspect.signature(org_structure_ProductType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_functiontype_is_not_abstract():
    assert not inspect.isabstract(org_structure_FunctionType)


def test_org_structure_functiontype_constructor_exists():
    assert callable(org_structure_FunctionType.__init__)


def test_org_structure_functiontype_constructor_args():
    sig = inspect.signature(org_structure_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(org_structure_UnresolvedType)


def test_org_structure_unresolvedtype_constructor_exists():
    assert callable(org_structure_UnresolvedType.__init__)


def test_org_structure_unresolvedtype_constructor_args():
    sig = inspect.signature(org_structure_UnresolvedType.__init__)
    params = list(sig.parameters.keys())
    assert "typeIdentifier" in params, "Missing parameter 'typeIdentifier'"

def test_org_structure_unresolvedtype_has_typeIdentifier():
    assert hasattr(org_structure_UnresolvedType, "typeIdentifier")
    descriptor = None
    for klass in org_structure_UnresolvedType.__mro__:
        if "typeIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["typeIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_typedelement_is_not_abstract():
    assert not inspect.isabstract(org_structure_TypedElement)


def test_org_structure_typedelement_constructor_exists():
    assert callable(org_structure_TypedElement.__init__)


def test_org_structure_typedelement_constructor_args():
    sig = inspect.signature(org_structure_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_typedefinition_is_not_abstract():
    assert not inspect.isabstract(org_structure_TypeDefinition)


def test_org_structure_typedefinition_constructor_exists():
    assert callable(org_structure_TypeDefinition.__init__)


def test_org_structure_typedefinition_constructor_args():
    sig = inspect.signature(org_structure_TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isAspect" in params, "Missing parameter 'isAspect'"

def test_org_structure_typedefinition_has_isAspect():
    assert hasattr(org_structure_TypeDefinition, "isAspect")
    descriptor = None
    for klass in org_structure_TypeDefinition.__mro__:
        if "isAspect" in klass.__dict__:
            descriptor = klass.__dict__["isAspect"]
            break
    assert isinstance(descriptor, property)



def test_structure_kermetamodelelement_is_not_abstract():
    assert not inspect.isabstract(structure_KermetaModelElement)


def test_structure_kermetamodelelement_constructor_exists():
    assert callable(structure_KermetaModelElement.__init__)


def test_structure_kermetamodelelement_constructor_args():
    sig = inspect.signature(structure_KermetaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_modeltypedefinitionbinding_is_not_abstract():
    assert not inspect.isabstract(org_structure_ModelTypeDefinitionBinding)


def test_org_structure_modeltypedefinitionbinding_constructor_exists():
    assert callable(org_structure_ModelTypeDefinitionBinding.__init__)


def test_org_structure_modeltypedefinitionbinding_constructor_args():
    sig = inspect.signature(org_structure_ModelTypeDefinitionBinding.__init__)
    params = list(sig.parameters.keys())



def test_org_structure_metamodel_is_not_abstract():
    assert not inspect.isabstract(org_structure_Metamodel)


def test_org_structure_metamodel_constructor_exists():
    assert callable(org_structure_Metamodel.__init__)


def test_org_structure_metamodel_constructor_args():
    sig = inspect.signature(org_structure_Metamodel.__init__)
    params = list(sig.parameters.keys())
    assert "isResolved" in params, "Missing parameter 'isResolved'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_org_structure_metamodel_has_isResolved():
    assert hasattr(org_structure_Metamodel, "isResolved")
    descriptor = None
    for klass in org_structure_Metamodel.__mro__:
        if "isResolved" in klass.__dict__:
            descriptor = klass.__dict__["isResolved"]
            break
    assert isinstance(descriptor, property)

def test_org_structure_metamodel_has_uri():
    assert hasattr(org_structure_Metamodel, "uri")
    descriptor = None
    for klass in org_structure_Metamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_org_structure_typevariablebinding_is_not_abstract():
    assert not inspect.isabstract(org_structure_TypeVariableBinding)


def test_org_structure_typevariablebinding_constructor_exists():
    assert callable(org_structure_TypeVariableBinding.__init__)


def test_org_structure_typevariablebinding_constructor_args():
    sig = inspect.signature(org_structure_TypeVariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_expression_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Expression)


def test_org_behavior_expression_constructor_exists():
    assert callable(org_behavior_Expression.__init__)


def test_org_behavior_expression_constructor_args():
    sig = inspect.signature(org_behavior_Expression.__init__)
    params = list(sig.parameters.keys())



def test_behavior_expression_is_not_abstract():
    assert not inspect.isabstract(behavior_Expression)


def test_behavior_expression_constructor_exists():
    assert callable(behavior_Expression.__init__)


def test_behavior_expression_constructor_args():
    sig = inspect.signature(behavior_Expression.__init__)
    params = list(sig.parameters.keys())



def test_behavior_callexpression_is_not_abstract():
    assert not inspect.isabstract(behavior_CallExpression)


def test_behavior_callexpression_constructor_exists():
    assert callable(behavior_CallExpression.__init__)


def test_behavior_callexpression_constructor_args():
    sig = inspect.signature(behavior_CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_unresolvedcall_is_not_abstract():
    assert not inspect.isabstract(org_behavior_UnresolvedCall)


def test_org_behavior_unresolvedcall_constructor_exists():
    assert callable(org_behavior_UnresolvedCall.__init__)


def test_org_behavior_unresolvedcall_constructor_args():
    sig = inspect.signature(org_behavior_UnresolvedCall.__init__)
    params = list(sig.parameters.keys())
    assert "isCalledWithParenthesis" in params, "Missing parameter 'isCalledWithParenthesis'"
    assert "isAtpre" in params, "Missing parameter 'isAtpre'"

def test_org_behavior_unresolvedcall_has_isCalledWithParenthesis():
    assert hasattr(org_behavior_UnresolvedCall, "isCalledWithParenthesis")
    descriptor = None
    for klass in org_behavior_UnresolvedCall.__mro__:
        if "isCalledWithParenthesis" in klass.__dict__:
            descriptor = klass.__dict__["isCalledWithParenthesis"]
            break
    assert isinstance(descriptor, property)

def test_org_behavior_unresolvedcall_has_isAtpre():
    assert hasattr(org_behavior_UnresolvedCall, "isAtpre")
    descriptor = None
    for klass in org_behavior_UnresolvedCall.__mro__:
        if "isAtpre" in klass.__dict__:
            descriptor = klass.__dict__["isAtpre"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_literal_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Literal)


def test_org_behavior_literal_constructor_exists():
    assert callable(org_behavior_Literal.__init__)


def test_org_behavior_literal_constructor_args():
    sig = inspect.signature(org_behavior_Literal.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_raise_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Raise)


def test_org_behavior_raise_constructor_exists():
    assert callable(org_behavior_Raise.__init__)


def test_org_behavior_raise_constructor_args():
    sig = inspect.signature(org_behavior_Raise.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_javastaticcall_is_not_abstract():
    assert not inspect.isabstract(org_behavior_JavaStaticCall)


def test_org_behavior_javastaticcall_constructor_exists():
    assert callable(org_behavior_JavaStaticCall.__init__)


def test_org_behavior_javastaticcall_constructor_args():
    sig = inspect.signature(org_behavior_JavaStaticCall.__init__)
    params = list(sig.parameters.keys())
    assert "jmethod" in params, "Missing parameter 'jmethod'"
    assert "jclass" in params, "Missing parameter 'jclass'"

def test_org_behavior_javastaticcall_has_jmethod():
    assert hasattr(org_behavior_JavaStaticCall, "jmethod")
    descriptor = None
    for klass in org_behavior_JavaStaticCall.__mro__:
        if "jmethod" in klass.__dict__:
            descriptor = klass.__dict__["jmethod"]
            break
    assert isinstance(descriptor, property)

def test_org_behavior_javastaticcall_has_jclass():
    assert hasattr(org_behavior_JavaStaticCall, "jclass")
    descriptor = None
    for klass in org_behavior_JavaStaticCall.__mro__:
        if "jclass" in klass.__dict__:
            descriptor = klass.__dict__["jclass"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_callexpression_is_not_abstract():
    assert not inspect.isabstract(org_behavior_CallExpression)


def test_org_behavior_callexpression_constructor_exists():
    assert callable(org_behavior_CallExpression.__init__)


def test_org_behavior_callexpression_constructor_args():
    sig = inspect.signature(org_behavior_CallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org_behavior_callexpression_has_name():
    assert hasattr(org_behavior_CallExpression, "name")
    descriptor = None
    for klass in org_behavior_CallExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(org_behavior_LambdaExpression)


def test_org_behavior_lambdaexpression_constructor_exists():
    assert callable(org_behavior_LambdaExpression.__init__)


def test_org_behavior_lambdaexpression_constructor_args():
    sig = inspect.signature(org_behavior_LambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_conditional_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Conditional)


def test_org_behavior_conditional_constructor_exists():
    assert callable(org_behavior_Conditional.__init__)


def test_org_behavior_conditional_constructor_args():
    sig = inspect.signature(org_behavior_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_variabledecl_is_not_abstract():
    assert not inspect.isabstract(org_behavior_VariableDecl)


def test_org_behavior_variabledecl_constructor_exists():
    assert callable(org_behavior_VariableDecl.__init__)


def test_org_behavior_variabledecl_constructor_args():
    sig = inspect.signature(org_behavior_VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_org_behavior_variabledecl_has_identifier():
    assert hasattr(org_behavior_VariableDecl, "identifier")
    descriptor = None
    for klass in org_behavior_VariableDecl.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_org_behavior_selfexpression_is_not_abstract():
    assert not inspect.isabstract(org_behavior_SelfExpression)


def test_org_behavior_selfexpression_constructor_exists():
    assert callable(org_behavior_SelfExpression.__init__)


def test_org_behavior_selfexpression_constructor_args():
    sig = inspect.signature(org_behavior_SelfExpression.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_loop_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Loop)


def test_org_behavior_loop_constructor_exists():
    assert callable(org_behavior_Loop.__init__)


def test_org_behavior_loop_constructor_args():
    sig = inspect.signature(org_behavior_Loop.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_emptyexpression_is_not_abstract():
    assert not inspect.isabstract(org_behavior_EmptyExpression)


def test_org_behavior_emptyexpression_constructor_exists():
    assert callable(org_behavior_EmptyExpression.__init__)


def test_org_behavior_emptyexpression_constructor_args():
    sig = inspect.signature(org_behavior_EmptyExpression.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_block_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Block)


def test_org_behavior_block_constructor_exists():
    assert callable(org_behavior_Block.__init__)


def test_org_behavior_block_constructor_args():
    sig = inspect.signature(org_behavior_Block.__init__)
    params = list(sig.parameters.keys())



def test_org_behavior_assignment_is_not_abstract():
    assert not inspect.isabstract(org_behavior_Assignment)


def test_org_behavior_assignment_constructor_exists():
    assert callable(org_behavior_Assignment.__init__)


def test_org_behavior_assignment_constructor_args():
    sig = inspect.signature(org_behavior_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isCast" in params, "Missing parameter 'isCast'"

def test_org_behavior_assignment_has_isCast():
    assert hasattr(org_behavior_Assignment, "isCast")
    descriptor = None
    for klass in org_behavior_Assignment.__mro__:
        if "isCast" in klass.__dict__:
            descriptor = klass.__dict__["isCast"]
            break
    assert isinstance(descriptor, property)

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "inv",
        "pre",
        "post",
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
structure_Metamodel_strategy = st.builds(
    structure_Metamodel,
)
structure_ModelTypeDefinitionBinding_strategy = st.builds(
    structure_ModelTypeDefinitionBinding,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
org_structure_ModelTypeDefinition_strategy = st.builds(
    org_structure_ModelTypeDefinition,
)
org_structure_ModelElementTypeDefinition_strategy = st.builds(
    org_structure_ModelElementTypeDefinition,
)
AdaptationOperator_strategy = st.builds(
    AdaptationOperator,
)
org_structure_OperationAdaptationOperator_strategy = st.builds(
    org_structure_OperationAdaptationOperator,
    body=
        safe_text
)
org_structure_PropertyAdaptationOperator_strategy = st.builds(
    org_structure_PropertyAdaptationOperator,
    remover=
        safe_text,
    getter=
        safe_text,
    setter=
        safe_text,
    adder=
        safe_text
)
structure_AdaptationParameter_strategy = st.builds(
    structure_AdaptationParameter,
)
structure_OperationBinding_strategy = st.builds(
    structure_OperationBinding,
)
structure_PropertyBinding_strategy = st.builds(
    structure_PropertyBinding,
)
structure_ModelTypeDefinition_strategy = st.builds(
    structure_ModelTypeDefinition,
)
structure_EnumerationBinding_strategy = st.builds(
    structure_EnumerationBinding,
)
structure_UseAdaptationOperator_strategy = st.builds(
    structure_UseAdaptationOperator,
)
structure_ClassDefinitionBinding_strategy = st.builds(
    structure_ClassDefinitionBinding,
)
TypeVariable_strategy = st.builds(
    TypeVariable,
)
org_structure_ObjectTypeVariable_strategy = st.builds(
    org_structure_ObjectTypeVariable,
)
structure_ModelTypeVariable_strategy = st.builds(
    structure_ModelTypeVariable,
)
ObjectTypeVariable_strategy = st.builds(
    ObjectTypeVariable,
)
org_structure_VirtualType_strategy = st.builds(
    org_structure_VirtualType,
)
structure_VirtualType_strategy = st.builds(
    structure_VirtualType,
)
org_structure_ModelTypeVariable_strategy = st.builds(
    org_structure_ModelTypeVariable,
)
structure_GenericTypeDefinition_strategy = st.builds(
    structure_GenericTypeDefinition,
)
structure_TypeVariableBinding_strategy = st.builds(
    structure_TypeVariableBinding,
)
Type_strategy = st.builds(
    Type,
)
org_structure_ModelType_strategy = st.builds(
    org_structure_ModelType,
)
org_structure_VoidType_strategy = st.builds(
    org_structure_VoidType,
)
org_structure_ParameterizedType_strategy = st.builds(
    org_structure_ParameterizedType,
)
ModelElementTypeDefinition_strategy = st.builds(
    ModelElementTypeDefinition,
)
org_structure_GenericTypeDefinition_strategy = st.builds(
    org_structure_GenericTypeDefinition,
)
structure_FilteredMetamodelReference_strategy = st.builds(
    structure_FilteredMetamodelReference,
)
structure_ModelTypeDefinitionContainer_strategy = st.builds(
    structure_ModelTypeDefinitionContainer,
)
GenericTypeDefinition_strategy = st.builds(
    GenericTypeDefinition,
)
org_structure_ClassDefinition_strategy = st.builds(
    org_structure_ClassDefinition,
    isFinal=
        safe_text,
    isSingleton=
        safe_text,
    isAbstract=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
org_structure_Enumeration_strategy = st.builds(
    org_structure_Enumeration,
)
org_structure_PrimitiveType_strategy = st.builds(
    org_structure_PrimitiveType,
)
structure_AdaptationOperator_strategy = st.builds(
    structure_AdaptationOperator,
)
structure_Package_strategy = st.builds(
    structure_Package,
)
structure_ModelElementTypeDefinitionContainer_strategy = st.builds(
    structure_ModelElementTypeDefinitionContainer,
)
structure_ModelElementTypeDefinition_strategy = st.builds(
    structure_ModelElementTypeDefinition,
)
structure_Class_strategy = st.builds(
    structure_Class,
)
ParameterizedType_strategy = st.builds(
    ParameterizedType,
)
org_structure_Class_strategy = st.builds(
    org_structure_Class,
    name=
        safe_text,
    isAbstract=
        safe_text
)
structure_NamedElement_strategy = st.builds(
    structure_NamedElement,
)
org_structure_Package_strategy = st.builds(
    org_structure_Package,
    uri=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
org_structure_AdaptationParameter_strategy = st.builds(
    org_structure_AdaptationParameter,
)
org_structure_MultiplicityElement_strategy = st.builds(
    org_structure_MultiplicityElement,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    lower=
        safe_text,
    upper=
        safe_text
)
structure_Enumeration_strategy = st.builds(
    structure_Enumeration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
org_structure_Constraint_strategy = st.builds(
    org_structure_Constraint,
    stereotype=
        safe_text,
    language=
        safe_text
)
org_structure_AdaptationOperator_strategy = st.builds(
    org_structure_AdaptationOperator,
)
org_structure_ModelElementTypeDefinitionContainer_strategy = st.builds(
    org_structure_ModelElementTypeDefinitionContainer,
)
org_structure_EnumerationLiteral_strategy = st.builds(
    org_structure_EnumerationLiteral,
)
structure_UnresolvedProperty_strategy = st.builds(
    structure_UnresolvedProperty,
)
structure_Constraint_strategy = st.builds(
    structure_Constraint,
)
structure_AbstractProperty_strategy = st.builds(
    structure_AbstractProperty,
)
structure_TypeVariable_strategy = st.builds(
    structure_TypeVariable,
)
structure_ClassDefinition_strategy = st.builds(
    structure_ClassDefinition,
)
structure_UnresolvedOperation_strategy = st.builds(
    structure_UnresolvedOperation,
)
structure_Using_strategy = st.builds(
    structure_Using,
)
structure_Parameter_strategy = st.builds(
    structure_Parameter,
)
structure_AbstractOperation_strategy = st.builds(
    structure_AbstractOperation,
)
structure_MultiplicityElement_strategy = st.builds(
    structure_MultiplicityElement,
)
org_structure_Property_strategy = st.builds(
    org_structure_Property,
    default=
        safe_text,
    isComposite=
        safe_text,
    isID=
        safe_text,
    isGetterAbstract=
        safe_text,
    isReadOnly=
        safe_text,
    isSetterAbstract=
        safe_text,
    isDerived=
        safe_text
)
org_structure_Operation_strategy = st.builds(
    org_structure_Operation,
    isAbstract=
        safe_text,
    uniqueName=
        safe_text
)
structure_Tag_strategy = st.builds(
    structure_Tag,
)
org_structure_KermetaModelElement_strategy = st.builds(
    org_structure_KermetaModelElement,
)
structure_ModelTransformation_strategy = st.builds(
    structure_ModelTransformation,
)
structure_EnumerationLiteral_strategy = st.builds(
    structure_EnumerationLiteral,
)
structure_Property_strategy = st.builds(
    structure_Property,
)
structure_Operation_strategy = st.builds(
    structure_Operation,
)
CallFeature_strategy = st.builds(
    CallFeature,
)
org_behavior_CallProperty_strategy = st.builds(
    org_behavior_CallProperty,
)
org_behavior_CallModelTransformation_strategy = st.builds(
    org_behavior_CallModelTransformation,
)
org_behavior_CallOperation_strategy = st.builds(
    org_behavior_CallOperation,
)
Literal_strategy = st.builds(
    Literal,
)
structure_UnresolvedReference_strategy = st.builds(
    structure_UnresolvedReference,
)
org_structure_UnresolvedModelTransformation_strategy = st.builds(
    org_structure_UnresolvedModelTransformation,
)
org_structure_UnresolvedProperty_strategy = st.builds(
    org_structure_UnresolvedProperty,
    propertyIdentifier=
        safe_text
)
org_structure_UnresolvedModelTypeDefinition_strategy = st.builds(
    org_structure_UnresolvedModelTypeDefinition,
)
org_structure_UnresolvedTypeVariable_strategy = st.builds(
    org_structure_UnresolvedTypeVariable,
)
org_structure_UnresolvedAdaptationOperator_strategy = st.builds(
    org_structure_UnresolvedAdaptationOperator,
)
org_behavior_VoidLiteral_strategy = st.builds(
    org_behavior_VoidLiteral,
)
org_behavior_CallTypeLiteral_strategy = st.builds(
    org_behavior_CallTypeLiteral,
)
org_behavior_BooleanLiteral_strategy = st.builds(
    org_behavior_BooleanLiteral,
    value=
        safe_text
)
org_behavior_StringLiteral_strategy = st.builds(
    org_behavior_StringLiteral,
    value=
        safe_text
)
org_behavior_IntegerLiteral_strategy = st.builds(
    org_behavior_IntegerLiteral,
    value=
        safe_text
)
behavior_LambdaParameter_strategy = st.builds(
    behavior_LambdaParameter,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
org_structure_Parameter_strategy = st.builds(
    org_structure_Parameter,
)
org_structure_ModelTransformation_strategy = st.builds(
    org_structure_ModelTransformation,
    isAbstract=
        safe_text
)
org_behavior_TypeReference_strategy = st.builds(
    org_behavior_TypeReference,
)
behavior_TypeReference_strategy = st.builds(
    behavior_TypeReference,
)
KermetaModelElement_strategy = st.builds(
    KermetaModelElement,
)
org_structure_UnresolvedReference_strategy = st.builds(
    org_structure_UnresolvedReference,
)
org_structure_ClassDefinitionBinding_strategy = st.builds(
    org_structure_ClassDefinitionBinding,
)
org_structure_UseAdaptationOperator_strategy = st.builds(
    org_structure_UseAdaptationOperator,
)
org_structure_Tag_strategy = st.builds(
    org_structure_Tag,
    value=
        safe_text,
    name=
        safe_text
)
org_structure_FilteredMetamodelReference_strategy = st.builds(
    org_structure_FilteredMetamodelReference,
)
org_structure_TypeContainer_strategy = st.builds(
    org_structure_TypeContainer,
)
org_structure_PropertyBinding_strategy = st.builds(
    org_structure_PropertyBinding,
)
org_structure_Type_strategy = st.builds(
    org_structure_Type,
)
org_structure_EnumerationBinding_strategy = st.builds(
    org_structure_EnumerationBinding,
)
org_structure_Using_strategy = st.builds(
    org_structure_Using,
    fromQName=
        safe_text,
    toName=
        safe_text
)
org_structure_NamedElement_strategy = st.builds(
    org_structure_NamedElement,
    name=
        safe_text
)
org_structure_AbstractProperty_strategy = st.builds(
    org_structure_AbstractProperty,
)
org_structure_OperationBinding_strategy = st.builds(
    org_structure_OperationBinding,
)
org_structure_AbstractOperation_strategy = st.builds(
    org_structure_AbstractOperation,
)
org_structure_ModelTypeDefinitionContainer_strategy = st.builds(
    org_structure_ModelTypeDefinitionContainer,
)
org_behavior_LambdaParameter_strategy = st.builds(
    org_behavior_LambdaParameter,
    name=
        safe_text
)
org_structure_Model_strategy = st.builds(
    org_structure_Model,
)
org_behavior_Rescue_strategy = st.builds(
    org_behavior_Rescue,
    exceptionName=
        safe_text
)
CallVariable_strategy = st.builds(
    CallVariable,
)
org_behavior_CallResult_strategy = st.builds(
    org_behavior_CallResult,
)
CallOperation_strategy = st.builds(
    CallOperation,
)
org_behavior_CallSuperOperation_strategy = st.builds(
    org_behavior_CallSuperOperation,
)
CallExpression_strategy = st.builds(
    CallExpression,
)
org_behavior_CallValue_strategy = st.builds(
    org_behavior_CallValue,
)
org_behavior_CallEnumLiteral_strategy = st.builds(
    org_behavior_CallEnumLiteral,
)
org_behavior_CallFeature_strategy = st.builds(
    org_behavior_CallFeature,
    isAtpre=
        safe_text
)
org_behavior_CallVariable_strategy = st.builds(
    org_behavior_CallVariable,
    isAtpre=
        safe_text
)
behavior_Rescue_strategy = st.builds(
    behavior_Rescue,
)
structure_Type_strategy = st.builds(
    structure_Type,
)
org_structure_UnresolvedInferredType_strategy = st.builds(
    org_structure_UnresolvedInferredType,
)
org_structure_DataType_strategy = st.builds(
    org_structure_DataType,
)
structure_TypeContainer_strategy = st.builds(
    structure_TypeContainer,
)
org_structure_UnresolvedOperation_strategy = st.builds(
    org_structure_UnresolvedOperation,
    operationIdentifier=
        safe_text
)
org_structure_TypeVariable_strategy = st.builds(
    org_structure_TypeVariable,
)
org_structure_ProductType_strategy = st.builds(
    org_structure_ProductType,
)
org_structure_FunctionType_strategy = st.builds(
    org_structure_FunctionType,
)
org_structure_UnresolvedType_strategy = st.builds(
    org_structure_UnresolvedType,
    typeIdentifier=
        safe_text
)
org_structure_TypedElement_strategy = st.builds(
    org_structure_TypedElement,
)
org_structure_TypeDefinition_strategy = st.builds(
    org_structure_TypeDefinition,
    isAspect=
        safe_text
)
structure_KermetaModelElement_strategy = st.builds(
    structure_KermetaModelElement,
)
org_structure_ModelTypeDefinitionBinding_strategy = st.builds(
    org_structure_ModelTypeDefinitionBinding,
)
org_structure_Metamodel_strategy = st.builds(
    org_structure_Metamodel,
    isResolved=
        st.booleans(),
    uri=
        safe_text
)
org_structure_TypeVariableBinding_strategy = st.builds(
    org_structure_TypeVariableBinding,
)
org_behavior_Expression_strategy = st.builds(
    org_behavior_Expression,
)
behavior_Expression_strategy = st.builds(
    behavior_Expression,
)
behavior_CallExpression_strategy = st.builds(
    behavior_CallExpression,
)
org_behavior_UnresolvedCall_strategy = st.builds(
    org_behavior_UnresolvedCall,
    isCalledWithParenthesis=
        safe_text,
    isAtpre=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
org_behavior_Literal_strategy = st.builds(
    org_behavior_Literal,
)
org_behavior_Raise_strategy = st.builds(
    org_behavior_Raise,
)
org_behavior_JavaStaticCall_strategy = st.builds(
    org_behavior_JavaStaticCall,
    jmethod=
        safe_text,
    jclass=
        safe_text
)
org_behavior_CallExpression_strategy = st.builds(
    org_behavior_CallExpression,
    name=
        safe_text
)
org_behavior_LambdaExpression_strategy = st.builds(
    org_behavior_LambdaExpression,
)
org_behavior_Conditional_strategy = st.builds(
    org_behavior_Conditional,
)
org_behavior_VariableDecl_strategy = st.builds(
    org_behavior_VariableDecl,
    identifier=
        safe_text
)
org_behavior_SelfExpression_strategy = st.builds(
    org_behavior_SelfExpression,
)
org_behavior_Loop_strategy = st.builds(
    org_behavior_Loop,
)
org_behavior_EmptyExpression_strategy = st.builds(
    org_behavior_EmptyExpression,
)
org_behavior_Block_strategy = st.builds(
    org_behavior_Block,
)
org_behavior_Assignment_strategy = st.builds(
    org_behavior_Assignment,
    isCast=
        safe_text
)

@given(instance=structure_Metamodel_strategy)
@settings(max_examples=50)
def test_structure_metamodel_instantiation(instance):
    assert isinstance(instance, structure_Metamodel)

@given(instance=structure_ModelTypeDefinitionBinding_strategy)
@settings(max_examples=50)
def test_structure_modeltypedefinitionbinding_instantiation(instance):
    assert isinstance(instance, structure_ModelTypeDefinitionBinding)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=org_structure_ModelTypeDefinition_strategy)
@settings(max_examples=50)
def test_org_structure_modeltypedefinition_instantiation(instance):
    assert isinstance(instance, org_structure_ModelTypeDefinition)

@given(instance=org_structure_ModelElementTypeDefinition_strategy)
@settings(max_examples=50)
def test_org_structure_modelelementtypedefinition_instantiation(instance):
    assert isinstance(instance, org_structure_ModelElementTypeDefinition)

@given(instance=AdaptationOperator_strategy)
@settings(max_examples=50)
def test_adaptationoperator_instantiation(instance):
    assert isinstance(instance, AdaptationOperator)

@given(instance=org_structure_OperationAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org_structure_operationadaptationoperator_instantiation(instance):
    assert isinstance(instance, org_structure_OperationAdaptationOperator)



@given(instance=org_structure_OperationAdaptationOperator_strategy)
def test_org_structure_operationadaptationoperator_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=org_structure_PropertyAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org_structure_propertyadaptationoperator_instantiation(instance):
    assert isinstance(instance, org_structure_PropertyAdaptationOperator)



@given(instance=org_structure_PropertyAdaptationOperator_strategy)
def test_org_structure_propertyadaptationoperator_remover_setter(instance):
    original = instance.remover
    instance.remover = original
    assert instance.remover == original



@given(instance=org_structure_PropertyAdaptationOperator_strategy)
def test_org_structure_propertyadaptationoperator_getter_setter(instance):
    original = instance.getter
    instance.getter = original
    assert instance.getter == original



@given(instance=org_structure_PropertyAdaptationOperator_strategy)
def test_org_structure_propertyadaptationoperator_setter_setter(instance):
    original = instance.setter
    instance.setter = original
    assert instance.setter == original



@given(instance=org_structure_PropertyAdaptationOperator_strategy)
def test_org_structure_propertyadaptationoperator_adder_setter(instance):
    original = instance.adder
    instance.adder = original
    assert instance.adder == original

@given(instance=structure_AdaptationParameter_strategy)
@settings(max_examples=50)
def test_structure_adaptationparameter_instantiation(instance):
    assert isinstance(instance, structure_AdaptationParameter)

@given(instance=structure_OperationBinding_strategy)
@settings(max_examples=50)
def test_structure_operationbinding_instantiation(instance):
    assert isinstance(instance, structure_OperationBinding)

@given(instance=structure_PropertyBinding_strategy)
@settings(max_examples=50)
def test_structure_propertybinding_instantiation(instance):
    assert isinstance(instance, structure_PropertyBinding)

@given(instance=structure_ModelTypeDefinition_strategy)
@settings(max_examples=50)
def test_structure_modeltypedefinition_instantiation(instance):
    assert isinstance(instance, structure_ModelTypeDefinition)

@given(instance=structure_EnumerationBinding_strategy)
@settings(max_examples=50)
def test_structure_enumerationbinding_instantiation(instance):
    assert isinstance(instance, structure_EnumerationBinding)

@given(instance=structure_UseAdaptationOperator_strategy)
@settings(max_examples=50)
def test_structure_useadaptationoperator_instantiation(instance):
    assert isinstance(instance, structure_UseAdaptationOperator)

@given(instance=structure_ClassDefinitionBinding_strategy)
@settings(max_examples=50)
def test_structure_classdefinitionbinding_instantiation(instance):
    assert isinstance(instance, structure_ClassDefinitionBinding)

@given(instance=TypeVariable_strategy)
@settings(max_examples=50)
def test_typevariable_instantiation(instance):
    assert isinstance(instance, TypeVariable)

@given(instance=org_structure_ObjectTypeVariable_strategy)
@settings(max_examples=50)
def test_org_structure_objecttypevariable_instantiation(instance):
    assert isinstance(instance, org_structure_ObjectTypeVariable)

@given(instance=structure_ModelTypeVariable_strategy)
@settings(max_examples=50)
def test_structure_modeltypevariable_instantiation(instance):
    assert isinstance(instance, structure_ModelTypeVariable)

@given(instance=ObjectTypeVariable_strategy)
@settings(max_examples=50)
def test_objecttypevariable_instantiation(instance):
    assert isinstance(instance, ObjectTypeVariable)

@given(instance=org_structure_VirtualType_strategy)
@settings(max_examples=50)
def test_org_structure_virtualtype_instantiation(instance):
    assert isinstance(instance, org_structure_VirtualType)

@given(instance=structure_VirtualType_strategy)
@settings(max_examples=50)
def test_structure_virtualtype_instantiation(instance):
    assert isinstance(instance, structure_VirtualType)

@given(instance=org_structure_ModelTypeVariable_strategy)
@settings(max_examples=50)
def test_org_structure_modeltypevariable_instantiation(instance):
    assert isinstance(instance, org_structure_ModelTypeVariable)

@given(instance=structure_GenericTypeDefinition_strategy)
@settings(max_examples=50)
def test_structure_generictypedefinition_instantiation(instance):
    assert isinstance(instance, structure_GenericTypeDefinition)

@given(instance=structure_TypeVariableBinding_strategy)
@settings(max_examples=50)
def test_structure_typevariablebinding_instantiation(instance):
    assert isinstance(instance, structure_TypeVariableBinding)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=org_structure_ModelType_strategy)
@settings(max_examples=50)
def test_org_structure_modeltype_instantiation(instance):
    assert isinstance(instance, org_structure_ModelType)

@given(instance=org_structure_VoidType_strategy)
@settings(max_examples=50)
def test_org_structure_voidtype_instantiation(instance):
    assert isinstance(instance, org_structure_VoidType)

@given(instance=org_structure_ParameterizedType_strategy)
@settings(max_examples=50)
def test_org_structure_parameterizedtype_instantiation(instance):
    assert isinstance(instance, org_structure_ParameterizedType)

@given(instance=ModelElementTypeDefinition_strategy)
@settings(max_examples=50)
def test_modelelementtypedefinition_instantiation(instance):
    assert isinstance(instance, ModelElementTypeDefinition)

@given(instance=org_structure_GenericTypeDefinition_strategy)
@settings(max_examples=50)
def test_org_structure_generictypedefinition_instantiation(instance):
    assert isinstance(instance, org_structure_GenericTypeDefinition)

@given(instance=structure_FilteredMetamodelReference_strategy)
@settings(max_examples=50)
def test_structure_filteredmetamodelreference_instantiation(instance):
    assert isinstance(instance, structure_FilteredMetamodelReference)

@given(instance=structure_ModelTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_structure_modeltypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, structure_ModelTypeDefinitionContainer)

@given(instance=GenericTypeDefinition_strategy)
@settings(max_examples=50)
def test_generictypedefinition_instantiation(instance):
    assert isinstance(instance, GenericTypeDefinition)

@given(instance=org_structure_ClassDefinition_strategy)
@settings(max_examples=50)
def test_org_structure_classdefinition_instantiation(instance):
    assert isinstance(instance, org_structure_ClassDefinition)



@given(instance=org_structure_ClassDefinition_strategy)
def test_org_structure_classdefinition_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=org_structure_ClassDefinition_strategy)
def test_org_structure_classdefinition_isSingleton_setter(instance):
    original = instance.isSingleton
    instance.isSingleton = original
    assert instance.isSingleton == original



@given(instance=org_structure_ClassDefinition_strategy)
def test_org_structure_classdefinition_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=org_structure_Enumeration_strategy)
@settings(max_examples=50)
def test_org_structure_enumeration_instantiation(instance):
    assert isinstance(instance, org_structure_Enumeration)

@given(instance=org_structure_PrimitiveType_strategy)
@settings(max_examples=50)
def test_org_structure_primitivetype_instantiation(instance):
    assert isinstance(instance, org_structure_PrimitiveType)

@given(instance=structure_AdaptationOperator_strategy)
@settings(max_examples=50)
def test_structure_adaptationoperator_instantiation(instance):
    assert isinstance(instance, structure_AdaptationOperator)

@given(instance=structure_Package_strategy)
@settings(max_examples=50)
def test_structure_package_instantiation(instance):
    assert isinstance(instance, structure_Package)

@given(instance=structure_ModelElementTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_structure_modelelementtypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, structure_ModelElementTypeDefinitionContainer)

@given(instance=structure_ModelElementTypeDefinition_strategy)
@settings(max_examples=50)
def test_structure_modelelementtypedefinition_instantiation(instance):
    assert isinstance(instance, structure_ModelElementTypeDefinition)

@given(instance=structure_Class_strategy)
@settings(max_examples=50)
def test_structure_class_instantiation(instance):
    assert isinstance(instance, structure_Class)

@given(instance=ParameterizedType_strategy)
@settings(max_examples=50)
def test_parameterizedtype_instantiation(instance):
    assert isinstance(instance, ParameterizedType)

@given(instance=org_structure_Class_strategy)
@settings(max_examples=50)
def test_org_structure_class_instantiation(instance):
    assert isinstance(instance, org_structure_Class)



@given(instance=org_structure_Class_strategy)
def test_org_structure_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=org_structure_Class_strategy)
def test_org_structure_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=structure_NamedElement_strategy)
@settings(max_examples=50)
def test_structure_namedelement_instantiation(instance):
    assert isinstance(instance, structure_NamedElement)

@given(instance=org_structure_Package_strategy)
@settings(max_examples=50)
def test_org_structure_package_instantiation(instance):
    assert isinstance(instance, org_structure_Package)



@given(instance=org_structure_Package_strategy)
def test_org_structure_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=org_structure_AdaptationParameter_strategy)
@settings(max_examples=50)
def test_org_structure_adaptationparameter_instantiation(instance):
    assert isinstance(instance, org_structure_AdaptationParameter)

@given(instance=org_structure_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_org_structure_multiplicityelement_instantiation(instance):
    assert isinstance(instance, org_structure_MultiplicityElement)



@given(instance=org_structure_MultiplicityElement_strategy)
def test_org_structure_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=org_structure_MultiplicityElement_strategy)
def test_org_structure_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=org_structure_MultiplicityElement_strategy)
def test_org_structure_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=org_structure_MultiplicityElement_strategy)
def test_org_structure_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=structure_Enumeration_strategy)
@settings(max_examples=50)
def test_structure_enumeration_instantiation(instance):
    assert isinstance(instance, structure_Enumeration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=org_structure_Constraint_strategy)
@settings(max_examples=50)
def test_org_structure_constraint_instantiation(instance):
    assert isinstance(instance, org_structure_Constraint)



@given(instance=org_structure_Constraint_strategy)
def test_org_structure_constraint_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original



@given(instance=org_structure_Constraint_strategy)
def test_org_structure_constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=org_structure_AdaptationOperator_strategy)
@settings(max_examples=50)
def test_org_structure_adaptationoperator_instantiation(instance):
    assert isinstance(instance, org_structure_AdaptationOperator)

@given(instance=org_structure_ModelElementTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_org_structure_modelelementtypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, org_structure_ModelElementTypeDefinitionContainer)

@given(instance=org_structure_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_org_structure_enumerationliteral_instantiation(instance):
    assert isinstance(instance, org_structure_EnumerationLiteral)

@given(instance=structure_UnresolvedProperty_strategy)
@settings(max_examples=50)
def test_structure_unresolvedproperty_instantiation(instance):
    assert isinstance(instance, structure_UnresolvedProperty)

@given(instance=structure_Constraint_strategy)
@settings(max_examples=50)
def test_structure_constraint_instantiation(instance):
    assert isinstance(instance, structure_Constraint)

@given(instance=structure_AbstractProperty_strategy)
@settings(max_examples=50)
def test_structure_abstractproperty_instantiation(instance):
    assert isinstance(instance, structure_AbstractProperty)

@given(instance=structure_TypeVariable_strategy)
@settings(max_examples=50)
def test_structure_typevariable_instantiation(instance):
    assert isinstance(instance, structure_TypeVariable)

@given(instance=structure_ClassDefinition_strategy)
@settings(max_examples=50)
def test_structure_classdefinition_instantiation(instance):
    assert isinstance(instance, structure_ClassDefinition)

@given(instance=structure_UnresolvedOperation_strategy)
@settings(max_examples=50)
def test_structure_unresolvedoperation_instantiation(instance):
    assert isinstance(instance, structure_UnresolvedOperation)

@given(instance=structure_Using_strategy)
@settings(max_examples=50)
def test_structure_using_instantiation(instance):
    assert isinstance(instance, structure_Using)

@given(instance=structure_Parameter_strategy)
@settings(max_examples=50)
def test_structure_parameter_instantiation(instance):
    assert isinstance(instance, structure_Parameter)

@given(instance=structure_AbstractOperation_strategy)
@settings(max_examples=50)
def test_structure_abstractoperation_instantiation(instance):
    assert isinstance(instance, structure_AbstractOperation)

@given(instance=structure_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_structure_multiplicityelement_instantiation(instance):
    assert isinstance(instance, structure_MultiplicityElement)

@given(instance=org_structure_Property_strategy)
@settings(max_examples=50)
def test_org_structure_property_instantiation(instance):
    assert isinstance(instance, org_structure_Property)



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_isGetterAbstract_setter(instance):
    original = instance.isGetterAbstract
    instance.isGetterAbstract = original
    assert instance.isGetterAbstract == original



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_isSetterAbstract_setter(instance):
    original = instance.isSetterAbstract
    instance.isSetterAbstract = original
    assert instance.isSetterAbstract == original



@given(instance=org_structure_Property_strategy)
def test_org_structure_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=org_structure_Operation_strategy)
@settings(max_examples=50)
def test_org_structure_operation_instantiation(instance):
    assert isinstance(instance, org_structure_Operation)



@given(instance=org_structure_Operation_strategy)
def test_org_structure_operation_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=org_structure_Operation_strategy)
def test_org_structure_operation_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original

@given(instance=structure_Tag_strategy)
@settings(max_examples=50)
def test_structure_tag_instantiation(instance):
    assert isinstance(instance, structure_Tag)

@given(instance=org_structure_KermetaModelElement_strategy)
@settings(max_examples=50)
def test_org_structure_kermetamodelelement_instantiation(instance):
    assert isinstance(instance, org_structure_KermetaModelElement)

@given(instance=structure_ModelTransformation_strategy)
@settings(max_examples=50)
def test_structure_modeltransformation_instantiation(instance):
    assert isinstance(instance, structure_ModelTransformation)

@given(instance=structure_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_structure_enumerationliteral_instantiation(instance):
    assert isinstance(instance, structure_EnumerationLiteral)

@given(instance=structure_Property_strategy)
@settings(max_examples=50)
def test_structure_property_instantiation(instance):
    assert isinstance(instance, structure_Property)

@given(instance=structure_Operation_strategy)
@settings(max_examples=50)
def test_structure_operation_instantiation(instance):
    assert isinstance(instance, structure_Operation)

@given(instance=CallFeature_strategy)
@settings(max_examples=50)
def test_callfeature_instantiation(instance):
    assert isinstance(instance, CallFeature)

@given(instance=org_behavior_CallProperty_strategy)
@settings(max_examples=50)
def test_org_behavior_callproperty_instantiation(instance):
    assert isinstance(instance, org_behavior_CallProperty)

@given(instance=org_behavior_CallModelTransformation_strategy)
@settings(max_examples=50)
def test_org_behavior_callmodeltransformation_instantiation(instance):
    assert isinstance(instance, org_behavior_CallModelTransformation)

@given(instance=org_behavior_CallOperation_strategy)
@settings(max_examples=50)
def test_org_behavior_calloperation_instantiation(instance):
    assert isinstance(instance, org_behavior_CallOperation)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=structure_UnresolvedReference_strategy)
@settings(max_examples=50)
def test_structure_unresolvedreference_instantiation(instance):
    assert isinstance(instance, structure_UnresolvedReference)

@given(instance=org_structure_UnresolvedModelTransformation_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedmodeltransformation_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedModelTransformation)

@given(instance=org_structure_UnresolvedProperty_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedproperty_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedProperty)



@given(instance=org_structure_UnresolvedProperty_strategy)
def test_org_structure_unresolvedproperty_propertyIdentifier_setter(instance):
    original = instance.propertyIdentifier
    instance.propertyIdentifier = original
    assert instance.propertyIdentifier == original

@given(instance=org_structure_UnresolvedModelTypeDefinition_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedmodeltypedefinition_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedModelTypeDefinition)

@given(instance=org_structure_UnresolvedTypeVariable_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedtypevariable_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedTypeVariable)

@given(instance=org_structure_UnresolvedAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedadaptationoperator_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedAdaptationOperator)

@given(instance=org_behavior_VoidLiteral_strategy)
@settings(max_examples=50)
def test_org_behavior_voidliteral_instantiation(instance):
    assert isinstance(instance, org_behavior_VoidLiteral)

@given(instance=org_behavior_CallTypeLiteral_strategy)
@settings(max_examples=50)
def test_org_behavior_calltypeliteral_instantiation(instance):
    assert isinstance(instance, org_behavior_CallTypeLiteral)

@given(instance=org_behavior_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_org_behavior_booleanliteral_instantiation(instance):
    assert isinstance(instance, org_behavior_BooleanLiteral)



@given(instance=org_behavior_BooleanLiteral_strategy)
def test_org_behavior_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=org_behavior_StringLiteral_strategy)
@settings(max_examples=50)
def test_org_behavior_stringliteral_instantiation(instance):
    assert isinstance(instance, org_behavior_StringLiteral)



@given(instance=org_behavior_StringLiteral_strategy)
def test_org_behavior_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=org_behavior_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_org_behavior_integerliteral_instantiation(instance):
    assert isinstance(instance, org_behavior_IntegerLiteral)



@given(instance=org_behavior_IntegerLiteral_strategy)
def test_org_behavior_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behavior_LambdaParameter_strategy)
@settings(max_examples=50)
def test_behavior_lambdaparameter_instantiation(instance):
    assert isinstance(instance, behavior_LambdaParameter)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=org_structure_Parameter_strategy)
@settings(max_examples=50)
def test_org_structure_parameter_instantiation(instance):
    assert isinstance(instance, org_structure_Parameter)

@given(instance=org_structure_ModelTransformation_strategy)
@settings(max_examples=50)
def test_org_structure_modeltransformation_instantiation(instance):
    assert isinstance(instance, org_structure_ModelTransformation)



@given(instance=org_structure_ModelTransformation_strategy)
def test_org_structure_modeltransformation_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=org_behavior_TypeReference_strategy)
@settings(max_examples=50)
def test_org_behavior_typereference_instantiation(instance):
    assert isinstance(instance, org_behavior_TypeReference)

@given(instance=behavior_TypeReference_strategy)
@settings(max_examples=50)
def test_behavior_typereference_instantiation(instance):
    assert isinstance(instance, behavior_TypeReference)

@given(instance=KermetaModelElement_strategy)
@settings(max_examples=50)
def test_kermetamodelelement_instantiation(instance):
    assert isinstance(instance, KermetaModelElement)

@given(instance=org_structure_UnresolvedReference_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedreference_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedReference)

@given(instance=org_structure_ClassDefinitionBinding_strategy)
@settings(max_examples=50)
def test_org_structure_classdefinitionbinding_instantiation(instance):
    assert isinstance(instance, org_structure_ClassDefinitionBinding)

@given(instance=org_structure_UseAdaptationOperator_strategy)
@settings(max_examples=50)
def test_org_structure_useadaptationoperator_instantiation(instance):
    assert isinstance(instance, org_structure_UseAdaptationOperator)

@given(instance=org_structure_Tag_strategy)
@settings(max_examples=50)
def test_org_structure_tag_instantiation(instance):
    assert isinstance(instance, org_structure_Tag)



@given(instance=org_structure_Tag_strategy)
def test_org_structure_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=org_structure_Tag_strategy)
def test_org_structure_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org_structure_FilteredMetamodelReference_strategy)
@settings(max_examples=50)
def test_org_structure_filteredmetamodelreference_instantiation(instance):
    assert isinstance(instance, org_structure_FilteredMetamodelReference)

@given(instance=org_structure_TypeContainer_strategy)
@settings(max_examples=50)
def test_org_structure_typecontainer_instantiation(instance):
    assert isinstance(instance, org_structure_TypeContainer)

@given(instance=org_structure_PropertyBinding_strategy)
@settings(max_examples=50)
def test_org_structure_propertybinding_instantiation(instance):
    assert isinstance(instance, org_structure_PropertyBinding)

@given(instance=org_structure_Type_strategy)
@settings(max_examples=50)
def test_org_structure_type_instantiation(instance):
    assert isinstance(instance, org_structure_Type)

@given(instance=org_structure_EnumerationBinding_strategy)
@settings(max_examples=50)
def test_org_structure_enumerationbinding_instantiation(instance):
    assert isinstance(instance, org_structure_EnumerationBinding)

@given(instance=org_structure_Using_strategy)
@settings(max_examples=50)
def test_org_structure_using_instantiation(instance):
    assert isinstance(instance, org_structure_Using)



@given(instance=org_structure_Using_strategy)
def test_org_structure_using_fromQName_setter(instance):
    original = instance.fromQName
    instance.fromQName = original
    assert instance.fromQName == original



@given(instance=org_structure_Using_strategy)
def test_org_structure_using_toName_setter(instance):
    original = instance.toName
    instance.toName = original
    assert instance.toName == original

@given(instance=org_structure_NamedElement_strategy)
@settings(max_examples=50)
def test_org_structure_namedelement_instantiation(instance):
    assert isinstance(instance, org_structure_NamedElement)



@given(instance=org_structure_NamedElement_strategy)
def test_org_structure_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org_structure_AbstractProperty_strategy)
@settings(max_examples=50)
def test_org_structure_abstractproperty_instantiation(instance):
    assert isinstance(instance, org_structure_AbstractProperty)

@given(instance=org_structure_OperationBinding_strategy)
@settings(max_examples=50)
def test_org_structure_operationbinding_instantiation(instance):
    assert isinstance(instance, org_structure_OperationBinding)

@given(instance=org_structure_AbstractOperation_strategy)
@settings(max_examples=50)
def test_org_structure_abstractoperation_instantiation(instance):
    assert isinstance(instance, org_structure_AbstractOperation)

@given(instance=org_structure_ModelTypeDefinitionContainer_strategy)
@settings(max_examples=50)
def test_org_structure_modeltypedefinitioncontainer_instantiation(instance):
    assert isinstance(instance, org_structure_ModelTypeDefinitionContainer)

@given(instance=org_behavior_LambdaParameter_strategy)
@settings(max_examples=50)
def test_org_behavior_lambdaparameter_instantiation(instance):
    assert isinstance(instance, org_behavior_LambdaParameter)



@given(instance=org_behavior_LambdaParameter_strategy)
def test_org_behavior_lambdaparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org_structure_Model_strategy)
@settings(max_examples=50)
def test_org_structure_model_instantiation(instance):
    assert isinstance(instance, org_structure_Model)

@given(instance=org_behavior_Rescue_strategy)
@settings(max_examples=50)
def test_org_behavior_rescue_instantiation(instance):
    assert isinstance(instance, org_behavior_Rescue)



@given(instance=org_behavior_Rescue_strategy)
def test_org_behavior_rescue_exceptionName_setter(instance):
    original = instance.exceptionName
    instance.exceptionName = original
    assert instance.exceptionName == original

@given(instance=CallVariable_strategy)
@settings(max_examples=50)
def test_callvariable_instantiation(instance):
    assert isinstance(instance, CallVariable)

@given(instance=org_behavior_CallResult_strategy)
@settings(max_examples=50)
def test_org_behavior_callresult_instantiation(instance):
    assert isinstance(instance, org_behavior_CallResult)

@given(instance=CallOperation_strategy)
@settings(max_examples=50)
def test_calloperation_instantiation(instance):
    assert isinstance(instance, CallOperation)

@given(instance=org_behavior_CallSuperOperation_strategy)
@settings(max_examples=50)
def test_org_behavior_callsuperoperation_instantiation(instance):
    assert isinstance(instance, org_behavior_CallSuperOperation)

@given(instance=CallExpression_strategy)
@settings(max_examples=50)
def test_callexpression_instantiation(instance):
    assert isinstance(instance, CallExpression)

@given(instance=org_behavior_CallValue_strategy)
@settings(max_examples=50)
def test_org_behavior_callvalue_instantiation(instance):
    assert isinstance(instance, org_behavior_CallValue)

@given(instance=org_behavior_CallEnumLiteral_strategy)
@settings(max_examples=50)
def test_org_behavior_callenumliteral_instantiation(instance):
    assert isinstance(instance, org_behavior_CallEnumLiteral)

@given(instance=org_behavior_CallFeature_strategy)
@settings(max_examples=50)
def test_org_behavior_callfeature_instantiation(instance):
    assert isinstance(instance, org_behavior_CallFeature)



@given(instance=org_behavior_CallFeature_strategy)
def test_org_behavior_callfeature_isAtpre_setter(instance):
    original = instance.isAtpre
    instance.isAtpre = original
    assert instance.isAtpre == original

@given(instance=org_behavior_CallVariable_strategy)
@settings(max_examples=50)
def test_org_behavior_callvariable_instantiation(instance):
    assert isinstance(instance, org_behavior_CallVariable)



@given(instance=org_behavior_CallVariable_strategy)
def test_org_behavior_callvariable_isAtpre_setter(instance):
    original = instance.isAtpre
    instance.isAtpre = original
    assert instance.isAtpre == original

@given(instance=behavior_Rescue_strategy)
@settings(max_examples=50)
def test_behavior_rescue_instantiation(instance):
    assert isinstance(instance, behavior_Rescue)

@given(instance=structure_Type_strategy)
@settings(max_examples=50)
def test_structure_type_instantiation(instance):
    assert isinstance(instance, structure_Type)

@given(instance=org_structure_UnresolvedInferredType_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedinferredtype_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedInferredType)

@given(instance=org_structure_DataType_strategy)
@settings(max_examples=50)
def test_org_structure_datatype_instantiation(instance):
    assert isinstance(instance, org_structure_DataType)

@given(instance=structure_TypeContainer_strategy)
@settings(max_examples=50)
def test_structure_typecontainer_instantiation(instance):
    assert isinstance(instance, structure_TypeContainer)

@given(instance=org_structure_UnresolvedOperation_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedoperation_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedOperation)



@given(instance=org_structure_UnresolvedOperation_strategy)
def test_org_structure_unresolvedoperation_operationIdentifier_setter(instance):
    original = instance.operationIdentifier
    instance.operationIdentifier = original
    assert instance.operationIdentifier == original

@given(instance=org_structure_TypeVariable_strategy)
@settings(max_examples=50)
def test_org_structure_typevariable_instantiation(instance):
    assert isinstance(instance, org_structure_TypeVariable)

@given(instance=org_structure_ProductType_strategy)
@settings(max_examples=50)
def test_org_structure_producttype_instantiation(instance):
    assert isinstance(instance, org_structure_ProductType)

@given(instance=org_structure_FunctionType_strategy)
@settings(max_examples=50)
def test_org_structure_functiontype_instantiation(instance):
    assert isinstance(instance, org_structure_FunctionType)

@given(instance=org_structure_UnresolvedType_strategy)
@settings(max_examples=50)
def test_org_structure_unresolvedtype_instantiation(instance):
    assert isinstance(instance, org_structure_UnresolvedType)



@given(instance=org_structure_UnresolvedType_strategy)
def test_org_structure_unresolvedtype_typeIdentifier_setter(instance):
    original = instance.typeIdentifier
    instance.typeIdentifier = original
    assert instance.typeIdentifier == original

@given(instance=org_structure_TypedElement_strategy)
@settings(max_examples=50)
def test_org_structure_typedelement_instantiation(instance):
    assert isinstance(instance, org_structure_TypedElement)

@given(instance=org_structure_TypeDefinition_strategy)
@settings(max_examples=50)
def test_org_structure_typedefinition_instantiation(instance):
    assert isinstance(instance, org_structure_TypeDefinition)



@given(instance=org_structure_TypeDefinition_strategy)
def test_org_structure_typedefinition_isAspect_setter(instance):
    original = instance.isAspect
    instance.isAspect = original
    assert instance.isAspect == original

@given(instance=structure_KermetaModelElement_strategy)
@settings(max_examples=50)
def test_structure_kermetamodelelement_instantiation(instance):
    assert isinstance(instance, structure_KermetaModelElement)

@given(instance=org_structure_ModelTypeDefinitionBinding_strategy)
@settings(max_examples=50)
def test_org_structure_modeltypedefinitionbinding_instantiation(instance):
    assert isinstance(instance, org_structure_ModelTypeDefinitionBinding)

@given(instance=org_structure_Metamodel_strategy)
@settings(max_examples=50)
def test_org_structure_metamodel_instantiation(instance):
    assert isinstance(instance, org_structure_Metamodel)



@given(instance=org_structure_Metamodel_strategy)
def test_org_structure_metamodel_isResolved_setter(instance):
    original = instance.isResolved
    instance.isResolved = original
    assert instance.isResolved == original



@given(instance=org_structure_Metamodel_strategy)
def test_org_structure_metamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=org_structure_TypeVariableBinding_strategy)
@settings(max_examples=50)
def test_org_structure_typevariablebinding_instantiation(instance):
    assert isinstance(instance, org_structure_TypeVariableBinding)

@given(instance=org_behavior_Expression_strategy)
@settings(max_examples=50)
def test_org_behavior_expression_instantiation(instance):
    assert isinstance(instance, org_behavior_Expression)

@given(instance=behavior_Expression_strategy)
@settings(max_examples=50)
def test_behavior_expression_instantiation(instance):
    assert isinstance(instance, behavior_Expression)

@given(instance=behavior_CallExpression_strategy)
@settings(max_examples=50)
def test_behavior_callexpression_instantiation(instance):
    assert isinstance(instance, behavior_CallExpression)

@given(instance=org_behavior_UnresolvedCall_strategy)
@settings(max_examples=50)
def test_org_behavior_unresolvedcall_instantiation(instance):
    assert isinstance(instance, org_behavior_UnresolvedCall)



@given(instance=org_behavior_UnresolvedCall_strategy)
def test_org_behavior_unresolvedcall_isCalledWithParenthesis_setter(instance):
    original = instance.isCalledWithParenthesis
    instance.isCalledWithParenthesis = original
    assert instance.isCalledWithParenthesis == original



@given(instance=org_behavior_UnresolvedCall_strategy)
def test_org_behavior_unresolvedcall_isAtpre_setter(instance):
    original = instance.isAtpre
    instance.isAtpre = original
    assert instance.isAtpre == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=org_behavior_Literal_strategy)
@settings(max_examples=50)
def test_org_behavior_literal_instantiation(instance):
    assert isinstance(instance, org_behavior_Literal)

@given(instance=org_behavior_Raise_strategy)
@settings(max_examples=50)
def test_org_behavior_raise_instantiation(instance):
    assert isinstance(instance, org_behavior_Raise)

@given(instance=org_behavior_JavaStaticCall_strategy)
@settings(max_examples=50)
def test_org_behavior_javastaticcall_instantiation(instance):
    assert isinstance(instance, org_behavior_JavaStaticCall)



@given(instance=org_behavior_JavaStaticCall_strategy)
def test_org_behavior_javastaticcall_jmethod_setter(instance):
    original = instance.jmethod
    instance.jmethod = original
    assert instance.jmethod == original



@given(instance=org_behavior_JavaStaticCall_strategy)
def test_org_behavior_javastaticcall_jclass_setter(instance):
    original = instance.jclass
    instance.jclass = original
    assert instance.jclass == original

@given(instance=org_behavior_CallExpression_strategy)
@settings(max_examples=50)
def test_org_behavior_callexpression_instantiation(instance):
    assert isinstance(instance, org_behavior_CallExpression)



@given(instance=org_behavior_CallExpression_strategy)
def test_org_behavior_callexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org_behavior_LambdaExpression_strategy)
@settings(max_examples=50)
def test_org_behavior_lambdaexpression_instantiation(instance):
    assert isinstance(instance, org_behavior_LambdaExpression)

@given(instance=org_behavior_Conditional_strategy)
@settings(max_examples=50)
def test_org_behavior_conditional_instantiation(instance):
    assert isinstance(instance, org_behavior_Conditional)

@given(instance=org_behavior_VariableDecl_strategy)
@settings(max_examples=50)
def test_org_behavior_variabledecl_instantiation(instance):
    assert isinstance(instance, org_behavior_VariableDecl)



@given(instance=org_behavior_VariableDecl_strategy)
def test_org_behavior_variabledecl_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=org_behavior_SelfExpression_strategy)
@settings(max_examples=50)
def test_org_behavior_selfexpression_instantiation(instance):
    assert isinstance(instance, org_behavior_SelfExpression)

@given(instance=org_behavior_Loop_strategy)
@settings(max_examples=50)
def test_org_behavior_loop_instantiation(instance):
    assert isinstance(instance, org_behavior_Loop)

@given(instance=org_behavior_EmptyExpression_strategy)
@settings(max_examples=50)
def test_org_behavior_emptyexpression_instantiation(instance):
    assert isinstance(instance, org_behavior_EmptyExpression)

@given(instance=org_behavior_Block_strategy)
@settings(max_examples=50)
def test_org_behavior_block_instantiation(instance):
    assert isinstance(instance, org_behavior_Block)

@given(instance=org_behavior_Assignment_strategy)
@settings(max_examples=50)
def test_org_behavior_assignment_instantiation(instance):
    assert isinstance(instance, org_behavior_Assignment)



@given(instance=org_behavior_Assignment_strategy)
def test_org_behavior_assignment_isCast_setter(instance):
    original = instance.isCast
    instance.isCast = original
    assert instance.isCast == original
