import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    ClassesProv_Namespace,
    Element,
    ClassesProv_NamedElement,
    Association,
    Class,
    ClassesProv_AssociationClass,
    InstanceSpecification,
    ClassesProv_EnumerationLiteral,
    DataType,
    ClassesProv_Enumeration,
    ClassesProv_PrimitiveType,
    Realization,
    ClassesProv_InterfaceRealization,
    Abstraction,
    ClassesProv_Realization,
    Dependency,
    ClassesProv_Abstraction,
    ClassesProv_Usage,
    BehavioralFeature,
    ClassesProv_Operation,
    Classifier,
    ClassesProv_Class,
    StructuralFeature,
    MultiplicityElement,
    Feature,
    ClassesProv_Substitution,
    ClassesProv_Property,
    ClassesProv_Interface,
    ClassesProv_DataType,
    ClassesProv_RedefinableElement,
    ClassesProv_InstanceValue,
    LiteralSpecification,
    ClassesProv_LiteralBoolean,
    ClassesProv_LiteralUnilimitedNatural,
    ClassesProv_LiteralString,
    ClassesProv_LiteralInteger,
    ClassesProv_LiteralReal,
    ClassesProv_LiteralNull,
    Type,
    RedefinableElement,
    ClassesProv_Feature,
    ClassesProv_TypedElement,
    ClassesProv_Slot,
    TypedElement,
    ClassesProv_StructuralFeature,
    ClassesProv_Parameter,
    ClassesProv_MultiplicityElement,
    Relationship,
    ClassesProv_Association,
    ClassesProv_DirectedRelationship,
    ClassesProv_Relationship,
    ValueSpecification,
    ClassesProv_OpaqueExpression,
    ClassesProv_LiteralSpecification,
    ClassesProv_Expression,
    PackageableElement,
    ClassesProv_ValueSpecification,
    ClassesProv_GeneralizationSet,
    ClassesProv_InstanceSpecification,
    Namespace,
    ClassesProv_BehavioralFeature,
    ClassesProv_Classifier,
    ClassesProv_Package,
    DirectedRelationship,
    ClassesProv_Dependency,
    ClassesProv_Generalization,
    ClassesProv_Constraint,
    ClassesProv_PackageImport,
    ClassesProv_ElementImport,
    ClassesProv_PackageableElement,
    ClassesProv_PackageMerge,
    ClassesProv_Type,
    ClassesProv_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_namespace_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Namespace)


def test_classesprov_namespace_constructor_exists():
    assert callable(ClassesProv_Namespace.__init__)


def test_classesprov_namespace_constructor_args():
    sig = inspect.signature(ClassesProv_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_namedelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_NamedElement)


def test_classesprov_namedelement_constructor_exists():
    assert callable(ClassesProv_NamedElement.__init__)


def test_classesprov_namedelement_constructor_args():
    sig = inspect.signature(ClassesProv_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_classesprov_namedelement_has_name():
    assert hasattr(ClassesProv_NamedElement, "name")
    descriptor = None
    for klass in ClassesProv_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_namedelement_has_qualifiedName():
    assert hasattr(ClassesProv_NamedElement, "qualifiedName")
    descriptor = None
    for klass in ClassesProv_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_associationclass_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_AssociationClass)


def test_classesprov_associationclass_constructor_exists():
    assert callable(ClassesProv_AssociationClass.__init__)


def test_classesprov_associationclass_constructor_args():
    sig = inspect.signature(ClassesProv_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_EnumerationLiteral)


def test_classesprov_enumerationliteral_constructor_exists():
    assert callable(ClassesProv_EnumerationLiteral.__init__)


def test_classesprov_enumerationliteral_constructor_args():
    sig = inspect.signature(ClassesProv_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_enumeration_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Enumeration)


def test_classesprov_enumeration_constructor_exists():
    assert callable(ClassesProv_Enumeration.__init__)


def test_classesprov_enumeration_constructor_args():
    sig = inspect.signature(ClassesProv_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_PrimitiveType)


def test_classesprov_primitivetype_constructor_exists():
    assert callable(ClassesProv_PrimitiveType.__init__)


def test_classesprov_primitivetype_constructor_args():
    sig = inspect.signature(ClassesProv_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_InterfaceRealization)


def test_classesprov_interfacerealization_constructor_exists():
    assert callable(ClassesProv_InterfaceRealization.__init__)


def test_classesprov_interfacerealization_constructor_args():
    sig = inspect.signature(ClassesProv_InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_realization_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Realization)


def test_classesprov_realization_constructor_exists():
    assert callable(ClassesProv_Realization.__init__)


def test_classesprov_realization_constructor_args():
    sig = inspect.signature(ClassesProv_Realization.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_abstraction_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Abstraction)


def test_classesprov_abstraction_constructor_exists():
    assert callable(ClassesProv_Abstraction.__init__)


def test_classesprov_abstraction_constructor_args():
    sig = inspect.signature(ClassesProv_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_usage_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Usage)


def test_classesprov_usage_constructor_exists():
    assert callable(ClassesProv_Usage.__init__)


def test_classesprov_usage_constructor_args():
    sig = inspect.signature(ClassesProv_Usage.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_operation_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Operation)


def test_classesprov_operation_constructor_exists():
    assert callable(ClassesProv_Operation.__init__)


def test_classesprov_operation_constructor_args():
    sig = inspect.signature(ClassesProv_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_classesprov_operation_has_upper():
    assert hasattr(ClassesProv_Operation, "upper")
    descriptor = None
    for klass in ClassesProv_Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_operation_has_isOrdered():
    assert hasattr(ClassesProv_Operation, "isOrdered")
    descriptor = None
    for klass in ClassesProv_Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_operation_has_isUnique():
    assert hasattr(ClassesProv_Operation, "isUnique")
    descriptor = None
    for klass in ClassesProv_Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_operation_has_lower():
    assert hasattr(ClassesProv_Operation, "lower")
    descriptor = None
    for klass in ClassesProv_Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_operation_has_isQuery():
    assert hasattr(ClassesProv_Operation, "isQuery")
    descriptor = None
    for klass in ClassesProv_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_class_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Class)


def test_classesprov_class_constructor_exists():
    assert callable(ClassesProv_Class.__init__)


def test_classesprov_class_constructor_args():
    sig = inspect.signature(ClassesProv_Class.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_substitution_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Substitution)


def test_classesprov_substitution_constructor_exists():
    assert callable(ClassesProv_Substitution.__init__)


def test_classesprov_substitution_constructor_args():
    sig = inspect.signature(ClassesProv_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_property_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Property)


def test_classesprov_property_constructor_exists():
    assert callable(ClassesProv_Property.__init__)


def test_classesprov_property_constructor_args():
    sig = inspect.signature(ClassesProv_Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isID" in params, "Missing parameter 'isID'"

def test_classesprov_property_has_default():
    assert hasattr(ClassesProv_Property, "default")
    descriptor = None
    for klass in ClassesProv_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_property_has_isDerived():
    assert hasattr(ClassesProv_Property, "isDerived")
    descriptor = None
    for klass in ClassesProv_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_property_has_isComposite():
    assert hasattr(ClassesProv_Property, "isComposite")
    descriptor = None
    for klass in ClassesProv_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_property_has_isDerivedUnion():
    assert hasattr(ClassesProv_Property, "isDerivedUnion")
    descriptor = None
    for klass in ClassesProv_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_property_has_isID():
    assert hasattr(ClassesProv_Property, "isID")
    descriptor = None
    for klass in ClassesProv_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_interface_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Interface)


def test_classesprov_interface_constructor_exists():
    assert callable(ClassesProv_Interface.__init__)


def test_classesprov_interface_constructor_args():
    sig = inspect.signature(ClassesProv_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_datatype_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_DataType)


def test_classesprov_datatype_constructor_exists():
    assert callable(ClassesProv_DataType.__init__)


def test_classesprov_datatype_constructor_args():
    sig = inspect.signature(ClassesProv_DataType.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_RedefinableElement)


def test_classesprov_redefinableelement_constructor_exists():
    assert callable(ClassesProv_RedefinableElement.__init__)


def test_classesprov_redefinableelement_constructor_args():
    sig = inspect.signature(ClassesProv_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_classesprov_redefinableelement_has_isLeaf():
    assert hasattr(ClassesProv_RedefinableElement, "isLeaf")
    descriptor = None
    for klass in ClassesProv_RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_instancevalue_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_InstanceValue)


def test_classesprov_instancevalue_constructor_exists():
    assert callable(ClassesProv_InstanceValue.__init__)


def test_classesprov_instancevalue_constructor_args():
    sig = inspect.signature(ClassesProv_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_literalboolean_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralBoolean)


def test_classesprov_literalboolean_constructor_exists():
    assert callable(ClassesProv_LiteralBoolean.__init__)


def test_classesprov_literalboolean_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_literalunilimitednatural_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralUnilimitedNatural)


def test_classesprov_literalunilimitednatural_constructor_exists():
    assert callable(ClassesProv_LiteralUnilimitedNatural.__init__)


def test_classesprov_literalunilimitednatural_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralUnilimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_literalstring_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralString)


def test_classesprov_literalstring_constructor_exists():
    assert callable(ClassesProv_LiteralString.__init__)


def test_classesprov_literalstring_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_literalinteger_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralInteger)


def test_classesprov_literalinteger_constructor_exists():
    assert callable(ClassesProv_LiteralInteger.__init__)


def test_classesprov_literalinteger_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_literalreal_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralReal)


def test_classesprov_literalreal_constructor_exists():
    assert callable(ClassesProv_LiteralReal.__init__)


def test_classesprov_literalreal_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_literalnull_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralNull)


def test_classesprov_literalnull_constructor_exists():
    assert callable(ClassesProv_LiteralNull.__init__)


def test_classesprov_literalnull_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_feature_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Feature)


def test_classesprov_feature_constructor_exists():
    assert callable(ClassesProv_Feature.__init__)


def test_classesprov_feature_constructor_args():
    sig = inspect.signature(ClassesProv_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_classesprov_feature_has_isStatic():
    assert hasattr(ClassesProv_Feature, "isStatic")
    descriptor = None
    for klass in ClassesProv_Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_typedelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_TypedElement)


def test_classesprov_typedelement_constructor_exists():
    assert callable(ClassesProv_TypedElement.__init__)


def test_classesprov_typedelement_constructor_args():
    sig = inspect.signature(ClassesProv_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_slot_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Slot)


def test_classesprov_slot_constructor_exists():
    assert callable(ClassesProv_Slot.__init__)


def test_classesprov_slot_constructor_args():
    sig = inspect.signature(ClassesProv_Slot.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_StructuralFeature)


def test_classesprov_structuralfeature_constructor_exists():
    assert callable(ClassesProv_StructuralFeature.__init__)


def test_classesprov_structuralfeature_constructor_args():
    sig = inspect.signature(ClassesProv_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_classesprov_structuralfeature_has_isReadOnly():
    assert hasattr(ClassesProv_StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in ClassesProv_StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_parameter_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Parameter)


def test_classesprov_parameter_constructor_exists():
    assert callable(ClassesProv_Parameter.__init__)


def test_classesprov_parameter_constructor_args():
    sig = inspect.signature(ClassesProv_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_classesprov_parameter_has_default():
    assert hasattr(ClassesProv_Parameter, "default")
    descriptor = None
    for klass in ClassesProv_Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_MultiplicityElement)


def test_classesprov_multiplicityelement_constructor_exists():
    assert callable(ClassesProv_MultiplicityElement.__init__)


def test_classesprov_multiplicityelement_constructor_args():
    sig = inspect.signature(ClassesProv_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_classesprov_multiplicityelement_has_upper():
    assert hasattr(ClassesProv_MultiplicityElement, "upper")
    descriptor = None
    for klass in ClassesProv_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_multiplicityelement_has_lower():
    assert hasattr(ClassesProv_MultiplicityElement, "lower")
    descriptor = None
    for klass in ClassesProv_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_multiplicityelement_has_isUnique():
    assert hasattr(ClassesProv_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in ClassesProv_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_multiplicityelement_has_isOrdered():
    assert hasattr(ClassesProv_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in ClassesProv_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_association_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Association)


def test_classesprov_association_constructor_exists():
    assert callable(ClassesProv_Association.__init__)


def test_classesprov_association_constructor_args():
    sig = inspect.signature(ClassesProv_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_classesprov_association_has_isDerived():
    assert hasattr(ClassesProv_Association, "isDerived")
    descriptor = None
    for klass in ClassesProv_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_DirectedRelationship)


def test_classesprov_directedrelationship_constructor_exists():
    assert callable(ClassesProv_DirectedRelationship.__init__)


def test_classesprov_directedrelationship_constructor_args():
    sig = inspect.signature(ClassesProv_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_relationship_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Relationship)


def test_classesprov_relationship_constructor_exists():
    assert callable(ClassesProv_Relationship.__init__)


def test_classesprov_relationship_constructor_args():
    sig = inspect.signature(ClassesProv_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_OpaqueExpression)


def test_classesprov_opaqueexpression_constructor_exists():
    assert callable(ClassesProv_OpaqueExpression.__init__)


def test_classesprov_opaqueexpression_constructor_args():
    sig = inspect.signature(ClassesProv_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_classesprov_opaqueexpression_has_body():
    assert hasattr(ClassesProv_OpaqueExpression, "body")
    descriptor = None
    for klass in ClassesProv_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_opaqueexpression_has_language():
    assert hasattr(ClassesProv_OpaqueExpression, "language")
    descriptor = None
    for klass in ClassesProv_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_literalspecification_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_LiteralSpecification)


def test_classesprov_literalspecification_constructor_exists():
    assert callable(ClassesProv_LiteralSpecification.__init__)


def test_classesprov_literalspecification_constructor_args():
    sig = inspect.signature(ClassesProv_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_expression_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Expression)


def test_classesprov_expression_constructor_exists():
    assert callable(ClassesProv_Expression.__init__)


def test_classesprov_expression_constructor_args():
    sig = inspect.signature(ClassesProv_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_classesprov_expression_has_symbol():
    assert hasattr(ClassesProv_Expression, "symbol")
    descriptor = None
    for klass in ClassesProv_Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_ValueSpecification)


def test_classesprov_valuespecification_constructor_exists():
    assert callable(ClassesProv_ValueSpecification.__init__)


def test_classesprov_valuespecification_constructor_args():
    sig = inspect.signature(ClassesProv_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_generalizationset_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_GeneralizationSet)


def test_classesprov_generalizationset_constructor_exists():
    assert callable(ClassesProv_GeneralizationSet.__init__)


def test_classesprov_generalizationset_constructor_args():
    sig = inspect.signature(ClassesProv_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_classesprov_generalizationset_has_isCovering():
    assert hasattr(ClassesProv_GeneralizationSet, "isCovering")
    descriptor = None
    for klass in ClassesProv_GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_generalizationset_has_isDisjoint():
    assert hasattr(ClassesProv_GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in ClassesProv_GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_instancespecification_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_InstanceSpecification)


def test_classesprov_instancespecification_constructor_exists():
    assert callable(ClassesProv_InstanceSpecification.__init__)


def test_classesprov_instancespecification_constructor_args():
    sig = inspect.signature(ClassesProv_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_BehavioralFeature)


def test_classesprov_behavioralfeature_constructor_exists():
    assert callable(ClassesProv_BehavioralFeature.__init__)


def test_classesprov_behavioralfeature_constructor_args():
    sig = inspect.signature(ClassesProv_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_classifier_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Classifier)


def test_classesprov_classifier_constructor_exists():
    assert callable(ClassesProv_Classifier.__init__)


def test_classesprov_classifier_constructor_args():
    sig = inspect.signature(ClassesProv_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isFinalSpecialization" in params, "Missing parameter 'isFinalSpecialization'"

def test_classesprov_classifier_has_isAbstract():
    assert hasattr(ClassesProv_Classifier, "isAbstract")
    descriptor = None
    for klass in ClassesProv_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_classesprov_classifier_has_isFinalSpecialization():
    assert hasattr(ClassesProv_Classifier, "isFinalSpecialization")
    descriptor = None
    for klass in ClassesProv_Classifier.__mro__:
        if "isFinalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["isFinalSpecialization"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_package_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Package)


def test_classesprov_package_constructor_exists():
    assert callable(ClassesProv_Package.__init__)


def test_classesprov_package_constructor_args():
    sig = inspect.signature(ClassesProv_Package.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"

def test_classesprov_package_has_URI():
    assert hasattr(ClassesProv_Package, "URI")
    descriptor = None
    for klass in ClassesProv_Package.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_dependency_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Dependency)


def test_classesprov_dependency_constructor_exists():
    assert callable(ClassesProv_Dependency.__init__)


def test_classesprov_dependency_constructor_args():
    sig = inspect.signature(ClassesProv_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_generalization_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Generalization)


def test_classesprov_generalization_constructor_exists():
    assert callable(ClassesProv_Generalization.__init__)


def test_classesprov_generalization_constructor_args():
    sig = inspect.signature(ClassesProv_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_classesprov_generalization_has_isSubstitutable():
    assert hasattr(ClassesProv_Generalization, "isSubstitutable")
    descriptor = None
    for klass in ClassesProv_Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_constraint_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Constraint)


def test_classesprov_constraint_constructor_exists():
    assert callable(ClassesProv_Constraint.__init__)


def test_classesprov_constraint_constructor_args():
    sig = inspect.signature(ClassesProv_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_packageimport_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_PackageImport)


def test_classesprov_packageimport_constructor_exists():
    assert callable(ClassesProv_PackageImport.__init__)


def test_classesprov_packageimport_constructor_args():
    sig = inspect.signature(ClassesProv_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_elementimport_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_ElementImport)


def test_classesprov_elementimport_constructor_exists():
    assert callable(ClassesProv_ElementImport.__init__)


def test_classesprov_elementimport_constructor_args():
    sig = inspect.signature(ClassesProv_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_classesprov_elementimport_has_alias():
    assert hasattr(ClassesProv_ElementImport, "alias")
    descriptor = None
    for klass in ClassesProv_ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_classesprov_packageableelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_PackageableElement)


def test_classesprov_packageableelement_constructor_exists():
    assert callable(ClassesProv_PackageableElement.__init__)


def test_classesprov_packageableelement_constructor_args():
    sig = inspect.signature(ClassesProv_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_packagemerge_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_PackageMerge)


def test_classesprov_packagemerge_constructor_exists():
    assert callable(ClassesProv_PackageMerge.__init__)


def test_classesprov_packagemerge_constructor_args():
    sig = inspect.signature(ClassesProv_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_type_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Type)


def test_classesprov_type_constructor_exists():
    assert callable(ClassesProv_Type.__init__)


def test_classesprov_type_constructor_args():
    sig = inspect.signature(ClassesProv_Type.__init__)
    params = list(sig.parameters.keys())



def test_classesprov_element_is_not_abstract():
    assert not inspect.isabstract(ClassesProv_Element)


def test_classesprov_element_constructor_exists():
    assert callable(ClassesProv_Element.__init__)


def test_classesprov_element_constructor_args():
    sig = inspect.signature(ClassesProv_Element.__init__)
    params = list(sig.parameters.keys())


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
NamedElement_strategy = st.builds(
    NamedElement,
)
ClassesProv_Namespace_strategy = st.builds(
    ClassesProv_Namespace,
)
Element_strategy = st.builds(
    Element,
)
ClassesProv_NamedElement_strategy = st.builds(
    ClassesProv_NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
Class_strategy = st.builds(
    Class,
)
ClassesProv_AssociationClass_strategy = st.builds(
    ClassesProv_AssociationClass,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
ClassesProv_EnumerationLiteral_strategy = st.builds(
    ClassesProv_EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
ClassesProv_Enumeration_strategy = st.builds(
    ClassesProv_Enumeration,
)
ClassesProv_PrimitiveType_strategy = st.builds(
    ClassesProv_PrimitiveType,
)
Realization_strategy = st.builds(
    Realization,
)
ClassesProv_InterfaceRealization_strategy = st.builds(
    ClassesProv_InterfaceRealization,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
ClassesProv_Realization_strategy = st.builds(
    ClassesProv_Realization,
)
Dependency_strategy = st.builds(
    Dependency,
)
ClassesProv_Abstraction_strategy = st.builds(
    ClassesProv_Abstraction,
)
ClassesProv_Usage_strategy = st.builds(
    ClassesProv_Usage,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
ClassesProv_Operation_strategy = st.builds(
    ClassesProv_Operation,
    upper=
        st.integers(),
    isOrdered=
        st.booleans(),
    isUnique=
        st.booleans(),
    lower=
        st.integers(),
    isQuery=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassesProv_Class_strategy = st.builds(
    ClassesProv_Class,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
Feature_strategy = st.builds(
    Feature,
)
ClassesProv_Substitution_strategy = st.builds(
    ClassesProv_Substitution,
)
ClassesProv_Property_strategy = st.builds(
    ClassesProv_Property,
    default=
        safe_text,
    isDerived=
        st.booleans(),
    isComposite=
        st.booleans(),
    isDerivedUnion=
        st.booleans(),
    isID=
        st.booleans()
)
ClassesProv_Interface_strategy = st.builds(
    ClassesProv_Interface,
)
ClassesProv_DataType_strategy = st.builds(
    ClassesProv_DataType,
)
ClassesProv_RedefinableElement_strategy = st.builds(
    ClassesProv_RedefinableElement,
    isLeaf=
        st.booleans()
)
ClassesProv_InstanceValue_strategy = st.builds(
    ClassesProv_InstanceValue,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
ClassesProv_LiteralBoolean_strategy = st.builds(
    ClassesProv_LiteralBoolean,
)
ClassesProv_LiteralUnilimitedNatural_strategy = st.builds(
    ClassesProv_LiteralUnilimitedNatural,
)
ClassesProv_LiteralString_strategy = st.builds(
    ClassesProv_LiteralString,
)
ClassesProv_LiteralInteger_strategy = st.builds(
    ClassesProv_LiteralInteger,
)
ClassesProv_LiteralReal_strategy = st.builds(
    ClassesProv_LiteralReal,
)
ClassesProv_LiteralNull_strategy = st.builds(
    ClassesProv_LiteralNull,
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
ClassesProv_Feature_strategy = st.builds(
    ClassesProv_Feature,
    isStatic=
        st.booleans()
)
ClassesProv_TypedElement_strategy = st.builds(
    ClassesProv_TypedElement,
)
ClassesProv_Slot_strategy = st.builds(
    ClassesProv_Slot,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ClassesProv_StructuralFeature_strategy = st.builds(
    ClassesProv_StructuralFeature,
    isReadOnly=
        st.booleans()
)
ClassesProv_Parameter_strategy = st.builds(
    ClassesProv_Parameter,
    default=
        safe_text
)
ClassesProv_MultiplicityElement_strategy = st.builds(
    ClassesProv_MultiplicityElement,
    upper=
        st.integers(),
    lower=
        st.integers(),
    isUnique=
        st.booleans(),
    isOrdered=
        st.booleans()
)
Relationship_strategy = st.builds(
    Relationship,
)
ClassesProv_Association_strategy = st.builds(
    ClassesProv_Association,
    isDerived=
        st.booleans()
)
ClassesProv_DirectedRelationship_strategy = st.builds(
    ClassesProv_DirectedRelationship,
)
ClassesProv_Relationship_strategy = st.builds(
    ClassesProv_Relationship,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
ClassesProv_OpaqueExpression_strategy = st.builds(
    ClassesProv_OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
ClassesProv_LiteralSpecification_strategy = st.builds(
    ClassesProv_LiteralSpecification,
)
ClassesProv_Expression_strategy = st.builds(
    ClassesProv_Expression,
    symbol=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
ClassesProv_ValueSpecification_strategy = st.builds(
    ClassesProv_ValueSpecification,
)
ClassesProv_GeneralizationSet_strategy = st.builds(
    ClassesProv_GeneralizationSet,
    isCovering=
        st.booleans(),
    isDisjoint=
        st.booleans()
)
ClassesProv_InstanceSpecification_strategy = st.builds(
    ClassesProv_InstanceSpecification,
)
Namespace_strategy = st.builds(
    Namespace,
)
ClassesProv_BehavioralFeature_strategy = st.builds(
    ClassesProv_BehavioralFeature,
)
ClassesProv_Classifier_strategy = st.builds(
    ClassesProv_Classifier,
    isAbstract=
        st.booleans(),
    isFinalSpecialization=
        st.booleans()
)
ClassesProv_Package_strategy = st.builds(
    ClassesProv_Package,
    URI=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
ClassesProv_Dependency_strategy = st.builds(
    ClassesProv_Dependency,
)
ClassesProv_Generalization_strategy = st.builds(
    ClassesProv_Generalization,
    isSubstitutable=
        st.booleans()
)
ClassesProv_Constraint_strategy = st.builds(
    ClassesProv_Constraint,
)
ClassesProv_PackageImport_strategy = st.builds(
    ClassesProv_PackageImport,
)
ClassesProv_ElementImport_strategy = st.builds(
    ClassesProv_ElementImport,
    alias=
        safe_text
)
ClassesProv_PackageableElement_strategy = st.builds(
    ClassesProv_PackageableElement,
)
ClassesProv_PackageMerge_strategy = st.builds(
    ClassesProv_PackageMerge,
)
ClassesProv_Type_strategy = st.builds(
    ClassesProv_Type,
)
ClassesProv_Element_strategy = st.builds(
    ClassesProv_Element,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ClassesProv_Namespace_strategy)
@settings(max_examples=50)
def test_classesprov_namespace_instantiation(instance):
    assert isinstance(instance, ClassesProv_Namespace)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ClassesProv_NamedElement_strategy)
@settings(max_examples=50)
def test_classesprov_namedelement_instantiation(instance):
    assert isinstance(instance, ClassesProv_NamedElement)



@given(instance=ClassesProv_NamedElement_strategy)
def test_classesprov_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ClassesProv_NamedElement_strategy)
def test_classesprov_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=ClassesProv_AssociationClass_strategy)
@settings(max_examples=50)
def test_classesprov_associationclass_instantiation(instance):
    assert isinstance(instance, ClassesProv_AssociationClass)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=ClassesProv_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_classesprov_enumerationliteral_instantiation(instance):
    assert isinstance(instance, ClassesProv_EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=ClassesProv_Enumeration_strategy)
@settings(max_examples=50)
def test_classesprov_enumeration_instantiation(instance):
    assert isinstance(instance, ClassesProv_Enumeration)

@given(instance=ClassesProv_PrimitiveType_strategy)
@settings(max_examples=50)
def test_classesprov_primitivetype_instantiation(instance):
    assert isinstance(instance, ClassesProv_PrimitiveType)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=ClassesProv_InterfaceRealization_strategy)
@settings(max_examples=50)
def test_classesprov_interfacerealization_instantiation(instance):
    assert isinstance(instance, ClassesProv_InterfaceRealization)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=ClassesProv_Realization_strategy)
@settings(max_examples=50)
def test_classesprov_realization_instantiation(instance):
    assert isinstance(instance, ClassesProv_Realization)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=ClassesProv_Abstraction_strategy)
@settings(max_examples=50)
def test_classesprov_abstraction_instantiation(instance):
    assert isinstance(instance, ClassesProv_Abstraction)

@given(instance=ClassesProv_Usage_strategy)
@settings(max_examples=50)
def test_classesprov_usage_instantiation(instance):
    assert isinstance(instance, ClassesProv_Usage)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=ClassesProv_Operation_strategy)
@settings(max_examples=50)
def test_classesprov_operation_instantiation(instance):
    assert isinstance(instance, ClassesProv_Operation)



@given(instance=ClassesProv_Operation_strategy)
def test_classesprov_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=ClassesProv_Operation_strategy)
def test_classesprov_operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=ClassesProv_Operation_strategy)
def test_classesprov_operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=ClassesProv_Operation_strategy)
def test_classesprov_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=ClassesProv_Operation_strategy)
def test_classesprov_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassesProv_Class_strategy)
@settings(max_examples=50)
def test_classesprov_class_instantiation(instance):
    assert isinstance(instance, ClassesProv_Class)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ClassesProv_Substitution_strategy)
@settings(max_examples=50)
def test_classesprov_substitution_instantiation(instance):
    assert isinstance(instance, ClassesProv_Substitution)

@given(instance=ClassesProv_Property_strategy)
@settings(max_examples=50)
def test_classesprov_property_instantiation(instance):
    assert isinstance(instance, ClassesProv_Property)



@given(instance=ClassesProv_Property_strategy)
def test_classesprov_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=ClassesProv_Property_strategy)
def test_classesprov_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=ClassesProv_Property_strategy)
def test_classesprov_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=ClassesProv_Property_strategy)
def test_classesprov_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=ClassesProv_Property_strategy)
def test_classesprov_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=ClassesProv_Interface_strategy)
@settings(max_examples=50)
def test_classesprov_interface_instantiation(instance):
    assert isinstance(instance, ClassesProv_Interface)

@given(instance=ClassesProv_DataType_strategy)
@settings(max_examples=50)
def test_classesprov_datatype_instantiation(instance):
    assert isinstance(instance, ClassesProv_DataType)

@given(instance=ClassesProv_RedefinableElement_strategy)
@settings(max_examples=50)
def test_classesprov_redefinableelement_instantiation(instance):
    assert isinstance(instance, ClassesProv_RedefinableElement)



@given(instance=ClassesProv_RedefinableElement_strategy)
def test_classesprov_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=ClassesProv_InstanceValue_strategy)
@settings(max_examples=50)
def test_classesprov_instancevalue_instantiation(instance):
    assert isinstance(instance, ClassesProv_InstanceValue)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=ClassesProv_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_classesprov_literalboolean_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralBoolean)

@given(instance=ClassesProv_LiteralUnilimitedNatural_strategy)
@settings(max_examples=50)
def test_classesprov_literalunilimitednatural_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralUnilimitedNatural)

@given(instance=ClassesProv_LiteralString_strategy)
@settings(max_examples=50)
def test_classesprov_literalstring_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralString)

@given(instance=ClassesProv_LiteralInteger_strategy)
@settings(max_examples=50)
def test_classesprov_literalinteger_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralInteger)

@given(instance=ClassesProv_LiteralReal_strategy)
@settings(max_examples=50)
def test_classesprov_literalreal_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralReal)

@given(instance=ClassesProv_LiteralNull_strategy)
@settings(max_examples=50)
def test_classesprov_literalnull_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralNull)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=ClassesProv_Feature_strategy)
@settings(max_examples=50)
def test_classesprov_feature_instantiation(instance):
    assert isinstance(instance, ClassesProv_Feature)



@given(instance=ClassesProv_Feature_strategy)
def test_classesprov_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=ClassesProv_TypedElement_strategy)
@settings(max_examples=50)
def test_classesprov_typedelement_instantiation(instance):
    assert isinstance(instance, ClassesProv_TypedElement)

@given(instance=ClassesProv_Slot_strategy)
@settings(max_examples=50)
def test_classesprov_slot_instantiation(instance):
    assert isinstance(instance, ClassesProv_Slot)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ClassesProv_StructuralFeature_strategy)
@settings(max_examples=50)
def test_classesprov_structuralfeature_instantiation(instance):
    assert isinstance(instance, ClassesProv_StructuralFeature)



@given(instance=ClassesProv_StructuralFeature_strategy)
def test_classesprov_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=ClassesProv_Parameter_strategy)
@settings(max_examples=50)
def test_classesprov_parameter_instantiation(instance):
    assert isinstance(instance, ClassesProv_Parameter)



@given(instance=ClassesProv_Parameter_strategy)
def test_classesprov_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=ClassesProv_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_classesprov_multiplicityelement_instantiation(instance):
    assert isinstance(instance, ClassesProv_MultiplicityElement)



@given(instance=ClassesProv_MultiplicityElement_strategy)
def test_classesprov_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=ClassesProv_MultiplicityElement_strategy)
def test_classesprov_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=ClassesProv_MultiplicityElement_strategy)
def test_classesprov_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=ClassesProv_MultiplicityElement_strategy)
def test_classesprov_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=ClassesProv_Association_strategy)
@settings(max_examples=50)
def test_classesprov_association_instantiation(instance):
    assert isinstance(instance, ClassesProv_Association)



@given(instance=ClassesProv_Association_strategy)
def test_classesprov_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=ClassesProv_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_classesprov_directedrelationship_instantiation(instance):
    assert isinstance(instance, ClassesProv_DirectedRelationship)

@given(instance=ClassesProv_Relationship_strategy)
@settings(max_examples=50)
def test_classesprov_relationship_instantiation(instance):
    assert isinstance(instance, ClassesProv_Relationship)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=ClassesProv_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_classesprov_opaqueexpression_instantiation(instance):
    assert isinstance(instance, ClassesProv_OpaqueExpression)



@given(instance=ClassesProv_OpaqueExpression_strategy)
def test_classesprov_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=ClassesProv_OpaqueExpression_strategy)
def test_classesprov_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=ClassesProv_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_classesprov_literalspecification_instantiation(instance):
    assert isinstance(instance, ClassesProv_LiteralSpecification)

@given(instance=ClassesProv_Expression_strategy)
@settings(max_examples=50)
def test_classesprov_expression_instantiation(instance):
    assert isinstance(instance, ClassesProv_Expression)



@given(instance=ClassesProv_Expression_strategy)
def test_classesprov_expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=ClassesProv_ValueSpecification_strategy)
@settings(max_examples=50)
def test_classesprov_valuespecification_instantiation(instance):
    assert isinstance(instance, ClassesProv_ValueSpecification)

@given(instance=ClassesProv_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_classesprov_generalizationset_instantiation(instance):
    assert isinstance(instance, ClassesProv_GeneralizationSet)



@given(instance=ClassesProv_GeneralizationSet_strategy)
def test_classesprov_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original



@given(instance=ClassesProv_GeneralizationSet_strategy)
def test_classesprov_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=ClassesProv_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_classesprov_instancespecification_instantiation(instance):
    assert isinstance(instance, ClassesProv_InstanceSpecification)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=ClassesProv_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_classesprov_behavioralfeature_instantiation(instance):
    assert isinstance(instance, ClassesProv_BehavioralFeature)

@given(instance=ClassesProv_Classifier_strategy)
@settings(max_examples=50)
def test_classesprov_classifier_instantiation(instance):
    assert isinstance(instance, ClassesProv_Classifier)



@given(instance=ClassesProv_Classifier_strategy)
def test_classesprov_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=ClassesProv_Classifier_strategy)
def test_classesprov_classifier_isFinalSpecialization_setter(instance):
    original = instance.isFinalSpecialization
    instance.isFinalSpecialization = original
    assert instance.isFinalSpecialization == original

@given(instance=ClassesProv_Package_strategy)
@settings(max_examples=50)
def test_classesprov_package_instantiation(instance):
    assert isinstance(instance, ClassesProv_Package)



@given(instance=ClassesProv_Package_strategy)
def test_classesprov_package_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=ClassesProv_Dependency_strategy)
@settings(max_examples=50)
def test_classesprov_dependency_instantiation(instance):
    assert isinstance(instance, ClassesProv_Dependency)

@given(instance=ClassesProv_Generalization_strategy)
@settings(max_examples=50)
def test_classesprov_generalization_instantiation(instance):
    assert isinstance(instance, ClassesProv_Generalization)



@given(instance=ClassesProv_Generalization_strategy)
def test_classesprov_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=ClassesProv_Constraint_strategy)
@settings(max_examples=50)
def test_classesprov_constraint_instantiation(instance):
    assert isinstance(instance, ClassesProv_Constraint)

@given(instance=ClassesProv_PackageImport_strategy)
@settings(max_examples=50)
def test_classesprov_packageimport_instantiation(instance):
    assert isinstance(instance, ClassesProv_PackageImport)

@given(instance=ClassesProv_ElementImport_strategy)
@settings(max_examples=50)
def test_classesprov_elementimport_instantiation(instance):
    assert isinstance(instance, ClassesProv_ElementImport)



@given(instance=ClassesProv_ElementImport_strategy)
def test_classesprov_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=ClassesProv_PackageableElement_strategy)
@settings(max_examples=50)
def test_classesprov_packageableelement_instantiation(instance):
    assert isinstance(instance, ClassesProv_PackageableElement)

@given(instance=ClassesProv_PackageMerge_strategy)
@settings(max_examples=50)
def test_classesprov_packagemerge_instantiation(instance):
    assert isinstance(instance, ClassesProv_PackageMerge)

@given(instance=ClassesProv_Type_strategy)
@settings(max_examples=50)
def test_classesprov_type_instantiation(instance):
    assert isinstance(instance, ClassesProv_Type)

@given(instance=ClassesProv_Element_strategy)
@settings(max_examples=50)
def test_classesprov_element_instantiation(instance):
    assert isinstance(instance, ClassesProv_Element)
