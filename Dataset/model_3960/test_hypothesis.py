import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Association,
    Class,
    ClassesProv::AssociationClass,
    InstanceSpecification,
    ClassesProv::EnumerationLiteral,
    DataType,
    ClassesProv::Enumeration,
    ClassesProv::PrimitiveType,
    Realization,
    ClassesProv::InterfaceRealization,
    Abstraction,
    ClassesProv::Realization,
    Dependency,
    ClassesProv::Abstraction,
    ClassesProv::Usage,
    BehavioralFeature,
    ClassesProv::Operation,
    Classifier,
    ClassesProv::Class,
    StructuralFeature,
    MultiplicityElement,
    Feature,
    ClassesProv::Substitution,
    ClassesProv::Property,
    ClassesProv::Interface,
    ClassesProv::DataType,
    ClassesProv::InstanceValue,
    LiteralSpecification,
    ClassesProv::LiteralString,
    ClassesProv::LiteralBoolean,
    ClassesProv::LiteralReal,
    ClassesProv::LiteralInteger,
    ClassesProv::LiteralUnilimitedNatural,
    ClassesProv::LiteralNull,
    Type,
    RedefinableElement,
    ClassesProv::Feature,
    TypedElement,
    ClassesProv::Parameter,
    ClassesProv::StructuralFeature,
    Relationship,
    ClassesProv::Association,
    ClassesProv::DirectedRelationship,
    ValueSpecification,
    ClassesProv::LiteralSpecification,
    ClassesProv::OpaqueExpression,
    ClassesProv::Expression,
    PackageableElement,
    ClassesProv::GeneralizationSet,
    ClassesProv::ValueSpecification,
    ClassesProv::InstanceSpecification,
    Namespace,
    ClassesProv::BehavioralFeature,
    ClassesProv::Classifier,
    ClassesProv::Package,
    DirectedRelationship,
    ClassesProv::Generalization,
    ClassesProv::Constraint,
    ClassesProv::PackageImport,
    ClassesProv::ElementImport,
    NamedElement,
    ClassesProv::RedefinableElement,
    ClassesProv::TypedElement,
    ClassesProv::PackageableElement,
    ClassesProv::Dependency,
    ClassesProv::Namespace,
    Element,
    ClassesProv::Slot,
    ClassesProv::MultiplicityElement,
    ClassesProv::Relationship,
    ClassesProv::NamedElement,
    ClassesProv::PackageMerge,
    ClassesProv::Type,
    ClassesProv::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_classesprov::associationclass_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::AssociationClass)


def test_classesprov::associationclass_constructor_exists():
    assert callable(ClassesProv::AssociationClass.__init__)


def test_classesprov::associationclass_constructor_args():
    sig = inspect.signature(ClassesProv::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::EnumerationLiteral)


def test_classesprov::enumerationliteral_constructor_exists():
    assert callable(ClassesProv::EnumerationLiteral.__init__)


def test_classesprov::enumerationliteral_constructor_args():
    sig = inspect.signature(ClassesProv::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::enumeration_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Enumeration)


def test_classesprov::enumeration_constructor_exists():
    assert callable(ClassesProv::Enumeration.__init__)


def test_classesprov::enumeration_constructor_args():
    sig = inspect.signature(ClassesProv::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::PrimitiveType)


def test_classesprov::primitivetype_constructor_exists():
    assert callable(ClassesProv::PrimitiveType.__init__)


def test_classesprov::primitivetype_constructor_args():
    sig = inspect.signature(ClassesProv::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::interfacerealization_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::InterfaceRealization)


def test_classesprov::interfacerealization_constructor_exists():
    assert callable(ClassesProv::InterfaceRealization.__init__)


def test_classesprov::interfacerealization_constructor_args():
    sig = inspect.signature(ClassesProv::InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::realization_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Realization)


def test_classesprov::realization_constructor_exists():
    assert callable(ClassesProv::Realization.__init__)


def test_classesprov::realization_constructor_args():
    sig = inspect.signature(ClassesProv::Realization.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::abstraction_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Abstraction)


def test_classesprov::abstraction_constructor_exists():
    assert callable(ClassesProv::Abstraction.__init__)


def test_classesprov::abstraction_constructor_args():
    sig = inspect.signature(ClassesProv::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::usage_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Usage)


def test_classesprov::usage_constructor_exists():
    assert callable(ClassesProv::Usage.__init__)


def test_classesprov::usage_constructor_args():
    sig = inspect.signature(ClassesProv::Usage.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::operation_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Operation)


def test_classesprov::operation_constructor_exists():
    assert callable(ClassesProv::Operation.__init__)


def test_classesprov::operation_constructor_args():
    sig = inspect.signature(ClassesProv::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_classesprov::operation_has_isOrdered():
    assert hasattr(ClassesProv::Operation, "isOrdered")
    descriptor = None
    for klass in ClassesProv::Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::operation_has_upper():
    assert hasattr(ClassesProv::Operation, "upper")
    descriptor = None
    for klass in ClassesProv::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::operation_has_isUnique():
    assert hasattr(ClassesProv::Operation, "isUnique")
    descriptor = None
    for klass in ClassesProv::Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::operation_has_lower():
    assert hasattr(ClassesProv::Operation, "lower")
    descriptor = None
    for klass in ClassesProv::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::operation_has_isQuery():
    assert hasattr(ClassesProv::Operation, "isQuery")
    descriptor = None
    for klass in ClassesProv::Operation.__mro__:
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



def test_classesprov::class_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Class)


def test_classesprov::class_constructor_exists():
    assert callable(ClassesProv::Class.__init__)


def test_classesprov::class_constructor_args():
    sig = inspect.signature(ClassesProv::Class.__init__)
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



def test_classesprov::substitution_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Substitution)


def test_classesprov::substitution_constructor_exists():
    assert callable(ClassesProv::Substitution.__init__)


def test_classesprov::substitution_constructor_args():
    sig = inspect.signature(ClassesProv::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::property_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Property)


def test_classesprov::property_constructor_exists():
    assert callable(ClassesProv::Property.__init__)


def test_classesprov::property_constructor_args():
    sig = inspect.signature(ClassesProv::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isID" in params, "Missing parameter 'isID'"

def test_classesprov::property_has_isDerivedUnion():
    assert hasattr(ClassesProv::Property, "isDerivedUnion")
    descriptor = None
    for klass in ClassesProv::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::property_has_default():
    assert hasattr(ClassesProv::Property, "default")
    descriptor = None
    for klass in ClassesProv::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::property_has_isDerived():
    assert hasattr(ClassesProv::Property, "isDerived")
    descriptor = None
    for klass in ClassesProv::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::property_has_isComposite():
    assert hasattr(ClassesProv::Property, "isComposite")
    descriptor = None
    for klass in ClassesProv::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::property_has_isID():
    assert hasattr(ClassesProv::Property, "isID")
    descriptor = None
    for klass in ClassesProv::Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::interface_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Interface)


def test_classesprov::interface_constructor_exists():
    assert callable(ClassesProv::Interface.__init__)


def test_classesprov::interface_constructor_args():
    sig = inspect.signature(ClassesProv::Interface.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::datatype_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::DataType)


def test_classesprov::datatype_constructor_exists():
    assert callable(ClassesProv::DataType.__init__)


def test_classesprov::datatype_constructor_args():
    sig = inspect.signature(ClassesProv::DataType.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::instancevalue_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::InstanceValue)


def test_classesprov::instancevalue_constructor_exists():
    assert callable(ClassesProv::InstanceValue.__init__)


def test_classesprov::instancevalue_constructor_args():
    sig = inspect.signature(ClassesProv::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalstring_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralString)


def test_classesprov::literalstring_constructor_exists():
    assert callable(ClassesProv::LiteralString.__init__)


def test_classesprov::literalstring_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalboolean_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralBoolean)


def test_classesprov::literalboolean_constructor_exists():
    assert callable(ClassesProv::LiteralBoolean.__init__)


def test_classesprov::literalboolean_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalreal_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralReal)


def test_classesprov::literalreal_constructor_exists():
    assert callable(ClassesProv::LiteralReal.__init__)


def test_classesprov::literalreal_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalinteger_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralInteger)


def test_classesprov::literalinteger_constructor_exists():
    assert callable(ClassesProv::LiteralInteger.__init__)


def test_classesprov::literalinteger_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalunilimitednatural_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralUnilimitedNatural)


def test_classesprov::literalunilimitednatural_constructor_exists():
    assert callable(ClassesProv::LiteralUnilimitedNatural.__init__)


def test_classesprov::literalunilimitednatural_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralUnilimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalnull_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralNull)


def test_classesprov::literalnull_constructor_exists():
    assert callable(ClassesProv::LiteralNull.__init__)


def test_classesprov::literalnull_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralNull.__init__)
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



def test_classesprov::feature_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Feature)


def test_classesprov::feature_constructor_exists():
    assert callable(ClassesProv::Feature.__init__)


def test_classesprov::feature_constructor_args():
    sig = inspect.signature(ClassesProv::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_classesprov::feature_has_isStatic():
    assert hasattr(ClassesProv::Feature, "isStatic")
    descriptor = None
    for klass in ClassesProv::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::parameter_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Parameter)


def test_classesprov::parameter_constructor_exists():
    assert callable(ClassesProv::Parameter.__init__)


def test_classesprov::parameter_constructor_args():
    sig = inspect.signature(ClassesProv::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_classesprov::parameter_has_default():
    assert hasattr(ClassesProv::Parameter, "default")
    descriptor = None
    for klass in ClassesProv::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::StructuralFeature)


def test_classesprov::structuralfeature_constructor_exists():
    assert callable(ClassesProv::StructuralFeature.__init__)


def test_classesprov::structuralfeature_constructor_args():
    sig = inspect.signature(ClassesProv::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_classesprov::structuralfeature_has_isReadOnly():
    assert hasattr(ClassesProv::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in ClassesProv::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::association_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Association)


def test_classesprov::association_constructor_exists():
    assert callable(ClassesProv::Association.__init__)


def test_classesprov::association_constructor_args():
    sig = inspect.signature(ClassesProv::Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_classesprov::association_has_isDerived():
    assert hasattr(ClassesProv::Association, "isDerived")
    descriptor = None
    for klass in ClassesProv::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::DirectedRelationship)


def test_classesprov::directedrelationship_constructor_exists():
    assert callable(ClassesProv::DirectedRelationship.__init__)


def test_classesprov::directedrelationship_constructor_args():
    sig = inspect.signature(ClassesProv::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::literalspecification_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::LiteralSpecification)


def test_classesprov::literalspecification_constructor_exists():
    assert callable(ClassesProv::LiteralSpecification.__init__)


def test_classesprov::literalspecification_constructor_args():
    sig = inspect.signature(ClassesProv::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::OpaqueExpression)


def test_classesprov::opaqueexpression_constructor_exists():
    assert callable(ClassesProv::OpaqueExpression.__init__)


def test_classesprov::opaqueexpression_constructor_args():
    sig = inspect.signature(ClassesProv::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_classesprov::opaqueexpression_has_language():
    assert hasattr(ClassesProv::OpaqueExpression, "language")
    descriptor = None
    for klass in ClassesProv::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::opaqueexpression_has_body():
    assert hasattr(ClassesProv::OpaqueExpression, "body")
    descriptor = None
    for klass in ClassesProv::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::expression_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Expression)


def test_classesprov::expression_constructor_exists():
    assert callable(ClassesProv::Expression.__init__)


def test_classesprov::expression_constructor_args():
    sig = inspect.signature(ClassesProv::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_classesprov::expression_has_symbol():
    assert hasattr(ClassesProv::Expression, "symbol")
    descriptor = None
    for klass in ClassesProv::Expression.__mro__:
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



def test_classesprov::generalizationset_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::GeneralizationSet)


def test_classesprov::generalizationset_constructor_exists():
    assert callable(ClassesProv::GeneralizationSet.__init__)


def test_classesprov::generalizationset_constructor_args():
    sig = inspect.signature(ClassesProv::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_classesprov::generalizationset_has_isCovering():
    assert hasattr(ClassesProv::GeneralizationSet, "isCovering")
    descriptor = None
    for klass in ClassesProv::GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::generalizationset_has_isDisjoint():
    assert hasattr(ClassesProv::GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in ClassesProv::GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::valuespecification_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::ValueSpecification)


def test_classesprov::valuespecification_constructor_exists():
    assert callable(ClassesProv::ValueSpecification.__init__)


def test_classesprov::valuespecification_constructor_args():
    sig = inspect.signature(ClassesProv::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::instancespecification_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::InstanceSpecification)


def test_classesprov::instancespecification_constructor_exists():
    assert callable(ClassesProv::InstanceSpecification.__init__)


def test_classesprov::instancespecification_constructor_args():
    sig = inspect.signature(ClassesProv::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::BehavioralFeature)


def test_classesprov::behavioralfeature_constructor_exists():
    assert callable(ClassesProv::BehavioralFeature.__init__)


def test_classesprov::behavioralfeature_constructor_args():
    sig = inspect.signature(ClassesProv::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Classifier)


def test_classesprov::classifier_constructor_exists():
    assert callable(ClassesProv::Classifier.__init__)


def test_classesprov::classifier_constructor_args():
    sig = inspect.signature(ClassesProv::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isFinalSpecialization" in params, "Missing parameter 'isFinalSpecialization'"

def test_classesprov::classifier_has_isAbstract():
    assert hasattr(ClassesProv::Classifier, "isAbstract")
    descriptor = None
    for klass in ClassesProv::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::classifier_has_isFinalSpecialization():
    assert hasattr(ClassesProv::Classifier, "isFinalSpecialization")
    descriptor = None
    for klass in ClassesProv::Classifier.__mro__:
        if "isFinalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["isFinalSpecialization"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::package_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Package)


def test_classesprov::package_constructor_exists():
    assert callable(ClassesProv::Package.__init__)


def test_classesprov::package_constructor_args():
    sig = inspect.signature(ClassesProv::Package.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"

def test_classesprov::package_has_URI():
    assert hasattr(ClassesProv::Package, "URI")
    descriptor = None
    for klass in ClassesProv::Package.__mro__:
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



def test_classesprov::generalization_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Generalization)


def test_classesprov::generalization_constructor_exists():
    assert callable(ClassesProv::Generalization.__init__)


def test_classesprov::generalization_constructor_args():
    sig = inspect.signature(ClassesProv::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_classesprov::generalization_has_isSubstitutable():
    assert hasattr(ClassesProv::Generalization, "isSubstitutable")
    descriptor = None
    for klass in ClassesProv::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::constraint_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Constraint)


def test_classesprov::constraint_constructor_exists():
    assert callable(ClassesProv::Constraint.__init__)


def test_classesprov::constraint_constructor_args():
    sig = inspect.signature(ClassesProv::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::packageimport_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::PackageImport)


def test_classesprov::packageimport_constructor_exists():
    assert callable(ClassesProv::PackageImport.__init__)


def test_classesprov::packageimport_constructor_args():
    sig = inspect.signature(ClassesProv::PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::elementimport_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::ElementImport)


def test_classesprov::elementimport_constructor_exists():
    assert callable(ClassesProv::ElementImport.__init__)


def test_classesprov::elementimport_constructor_args():
    sig = inspect.signature(ClassesProv::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_classesprov::elementimport_has_alias():
    assert hasattr(ClassesProv::ElementImport, "alias")
    descriptor = None
    for klass in ClassesProv::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::RedefinableElement)


def test_classesprov::redefinableelement_constructor_exists():
    assert callable(ClassesProv::RedefinableElement.__init__)


def test_classesprov::redefinableelement_constructor_args():
    sig = inspect.signature(ClassesProv::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_classesprov::redefinableelement_has_isLeaf():
    assert hasattr(ClassesProv::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in ClassesProv::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::typedelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::TypedElement)


def test_classesprov::typedelement_constructor_exists():
    assert callable(ClassesProv::TypedElement.__init__)


def test_classesprov::typedelement_constructor_args():
    sig = inspect.signature(ClassesProv::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::packageableelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::PackageableElement)


def test_classesprov::packageableelement_constructor_exists():
    assert callable(ClassesProv::PackageableElement.__init__)


def test_classesprov::packageableelement_constructor_args():
    sig = inspect.signature(ClassesProv::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::dependency_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Dependency)


def test_classesprov::dependency_constructor_exists():
    assert callable(ClassesProv::Dependency.__init__)


def test_classesprov::dependency_constructor_args():
    sig = inspect.signature(ClassesProv::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::namespace_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Namespace)


def test_classesprov::namespace_constructor_exists():
    assert callable(ClassesProv::Namespace.__init__)


def test_classesprov::namespace_constructor_args():
    sig = inspect.signature(ClassesProv::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::slot_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Slot)


def test_classesprov::slot_constructor_exists():
    assert callable(ClassesProv::Slot.__init__)


def test_classesprov::slot_constructor_args():
    sig = inspect.signature(ClassesProv::Slot.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::MultiplicityElement)


def test_classesprov::multiplicityelement_constructor_exists():
    assert callable(ClassesProv::MultiplicityElement.__init__)


def test_classesprov::multiplicityelement_constructor_args():
    sig = inspect.signature(ClassesProv::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_classesprov::multiplicityelement_has_upper():
    assert hasattr(ClassesProv::MultiplicityElement, "upper")
    descriptor = None
    for klass in ClassesProv::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::multiplicityelement_has_isOrdered():
    assert hasattr(ClassesProv::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in ClassesProv::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::multiplicityelement_has_isUnique():
    assert hasattr(ClassesProv::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in ClassesProv::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::multiplicityelement_has_lower():
    assert hasattr(ClassesProv::MultiplicityElement, "lower")
    descriptor = None
    for klass in ClassesProv::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::relationship_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Relationship)


def test_classesprov::relationship_constructor_exists():
    assert callable(ClassesProv::Relationship.__init__)


def test_classesprov::relationship_constructor_args():
    sig = inspect.signature(ClassesProv::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::namedelement_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::NamedElement)


def test_classesprov::namedelement_constructor_exists():
    assert callable(ClassesProv::NamedElement.__init__)


def test_classesprov::namedelement_constructor_args():
    sig = inspect.signature(ClassesProv::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_classesprov::namedelement_has_name():
    assert hasattr(ClassesProv::NamedElement, "name")
    descriptor = None
    for klass in ClassesProv::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classesprov::namedelement_has_qualifiedName():
    assert hasattr(ClassesProv::NamedElement, "qualifiedName")
    descriptor = None
    for klass in ClassesProv::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_classesprov::packagemerge_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::PackageMerge)


def test_classesprov::packagemerge_constructor_exists():
    assert callable(ClassesProv::PackageMerge.__init__)


def test_classesprov::packagemerge_constructor_args():
    sig = inspect.signature(ClassesProv::PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::type_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Type)


def test_classesprov::type_constructor_exists():
    assert callable(ClassesProv::Type.__init__)


def test_classesprov::type_constructor_args():
    sig = inspect.signature(ClassesProv::Type.__init__)
    params = list(sig.parameters.keys())



def test_classesprov::element_is_not_abstract():
    assert not inspect.isabstract(ClassesProv::Element)


def test_classesprov::element_constructor_exists():
    assert callable(ClassesProv::Element.__init__)


def test_classesprov::element_constructor_args():
    sig = inspect.signature(ClassesProv::Element.__init__)
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
Association_strategy = st.builds(
    Association,
)
Class_strategy = st.builds(
    Class,
)
ClassesProv::AssociationClass_strategy = st.builds(
    ClassesProv::AssociationClass,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
ClassesProv::EnumerationLiteral_strategy = st.builds(
    ClassesProv::EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
ClassesProv::Enumeration_strategy = st.builds(
    ClassesProv::Enumeration,
)
ClassesProv::PrimitiveType_strategy = st.builds(
    ClassesProv::PrimitiveType,
)
Realization_strategy = st.builds(
    Realization,
)
ClassesProv::InterfaceRealization_strategy = st.builds(
    ClassesProv::InterfaceRealization,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
ClassesProv::Realization_strategy = st.builds(
    ClassesProv::Realization,
)
Dependency_strategy = st.builds(
    Dependency,
)
ClassesProv::Abstraction_strategy = st.builds(
    ClassesProv::Abstraction,
)
ClassesProv::Usage_strategy = st.builds(
    ClassesProv::Usage,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
ClassesProv::Operation_strategy = st.builds(
    ClassesProv::Operation,
    isOrdered=
        st.booleans(),
    upper=
        st.integers(),
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
ClassesProv::Class_strategy = st.builds(
    ClassesProv::Class,
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
ClassesProv::Substitution_strategy = st.builds(
    ClassesProv::Substitution,
)
ClassesProv::Property_strategy = st.builds(
    ClassesProv::Property,
    isDerivedUnion=
        st.booleans(),
    default=
        safe_text,
    isDerived=
        st.booleans(),
    isComposite=
        st.booleans(),
    isID=
        st.booleans()
)
ClassesProv::Interface_strategy = st.builds(
    ClassesProv::Interface,
)
ClassesProv::DataType_strategy = st.builds(
    ClassesProv::DataType,
)
ClassesProv::InstanceValue_strategy = st.builds(
    ClassesProv::InstanceValue,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
ClassesProv::LiteralString_strategy = st.builds(
    ClassesProv::LiteralString,
)
ClassesProv::LiteralBoolean_strategy = st.builds(
    ClassesProv::LiteralBoolean,
)
ClassesProv::LiteralReal_strategy = st.builds(
    ClassesProv::LiteralReal,
)
ClassesProv::LiteralInteger_strategy = st.builds(
    ClassesProv::LiteralInteger,
)
ClassesProv::LiteralUnilimitedNatural_strategy = st.builds(
    ClassesProv::LiteralUnilimitedNatural,
)
ClassesProv::LiteralNull_strategy = st.builds(
    ClassesProv::LiteralNull,
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
ClassesProv::Feature_strategy = st.builds(
    ClassesProv::Feature,
    isStatic=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ClassesProv::Parameter_strategy = st.builds(
    ClassesProv::Parameter,
    default=
        safe_text
)
ClassesProv::StructuralFeature_strategy = st.builds(
    ClassesProv::StructuralFeature,
    isReadOnly=
        st.booleans()
)
Relationship_strategy = st.builds(
    Relationship,
)
ClassesProv::Association_strategy = st.builds(
    ClassesProv::Association,
    isDerived=
        st.booleans()
)
ClassesProv::DirectedRelationship_strategy = st.builds(
    ClassesProv::DirectedRelationship,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
ClassesProv::LiteralSpecification_strategy = st.builds(
    ClassesProv::LiteralSpecification,
)
ClassesProv::OpaqueExpression_strategy = st.builds(
    ClassesProv::OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
ClassesProv::Expression_strategy = st.builds(
    ClassesProv::Expression,
    symbol=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
ClassesProv::GeneralizationSet_strategy = st.builds(
    ClassesProv::GeneralizationSet,
    isCovering=
        st.booleans(),
    isDisjoint=
        st.booleans()
)
ClassesProv::ValueSpecification_strategy = st.builds(
    ClassesProv::ValueSpecification,
)
ClassesProv::InstanceSpecification_strategy = st.builds(
    ClassesProv::InstanceSpecification,
)
Namespace_strategy = st.builds(
    Namespace,
)
ClassesProv::BehavioralFeature_strategy = st.builds(
    ClassesProv::BehavioralFeature,
)
ClassesProv::Classifier_strategy = st.builds(
    ClassesProv::Classifier,
    isAbstract=
        st.booleans(),
    isFinalSpecialization=
        st.booleans()
)
ClassesProv::Package_strategy = st.builds(
    ClassesProv::Package,
    URI=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
ClassesProv::Generalization_strategy = st.builds(
    ClassesProv::Generalization,
    isSubstitutable=
        st.booleans()
)
ClassesProv::Constraint_strategy = st.builds(
    ClassesProv::Constraint,
)
ClassesProv::PackageImport_strategy = st.builds(
    ClassesProv::PackageImport,
)
ClassesProv::ElementImport_strategy = st.builds(
    ClassesProv::ElementImport,
    alias=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ClassesProv::RedefinableElement_strategy = st.builds(
    ClassesProv::RedefinableElement,
    isLeaf=
        st.booleans()
)
ClassesProv::TypedElement_strategy = st.builds(
    ClassesProv::TypedElement,
)
ClassesProv::PackageableElement_strategy = st.builds(
    ClassesProv::PackageableElement,
)
ClassesProv::Dependency_strategy = st.builds(
    ClassesProv::Dependency,
)
ClassesProv::Namespace_strategy = st.builds(
    ClassesProv::Namespace,
)
Element_strategy = st.builds(
    Element,
)
ClassesProv::Slot_strategy = st.builds(
    ClassesProv::Slot,
)
ClassesProv::MultiplicityElement_strategy = st.builds(
    ClassesProv::MultiplicityElement,
    upper=
        st.integers(),
    isOrdered=
        st.booleans(),
    isUnique=
        st.booleans(),
    lower=
        st.integers()
)
ClassesProv::Relationship_strategy = st.builds(
    ClassesProv::Relationship,
)
ClassesProv::NamedElement_strategy = st.builds(
    ClassesProv::NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text
)
ClassesProv::PackageMerge_strategy = st.builds(
    ClassesProv::PackageMerge,
)
ClassesProv::Type_strategy = st.builds(
    ClassesProv::Type,
)
ClassesProv::Element_strategy = st.builds(
    ClassesProv::Element,
)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=ClassesProv::AssociationClass_strategy)
@settings(max_examples=50)
def test_classesprov::associationclass_instantiation(instance):
    assert isinstance(instance, ClassesProv::AssociationClass)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=ClassesProv::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_classesprov::enumerationliteral_instantiation(instance):
    assert isinstance(instance, ClassesProv::EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=ClassesProv::Enumeration_strategy)
@settings(max_examples=50)
def test_classesprov::enumeration_instantiation(instance):
    assert isinstance(instance, ClassesProv::Enumeration)

@given(instance=ClassesProv::PrimitiveType_strategy)
@settings(max_examples=50)
def test_classesprov::primitivetype_instantiation(instance):
    assert isinstance(instance, ClassesProv::PrimitiveType)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=ClassesProv::InterfaceRealization_strategy)
@settings(max_examples=50)
def test_classesprov::interfacerealization_instantiation(instance):
    assert isinstance(instance, ClassesProv::InterfaceRealization)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=ClassesProv::Realization_strategy)
@settings(max_examples=50)
def test_classesprov::realization_instantiation(instance):
    assert isinstance(instance, ClassesProv::Realization)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=ClassesProv::Abstraction_strategy)
@settings(max_examples=50)
def test_classesprov::abstraction_instantiation(instance):
    assert isinstance(instance, ClassesProv::Abstraction)

@given(instance=ClassesProv::Usage_strategy)
@settings(max_examples=50)
def test_classesprov::usage_instantiation(instance):
    assert isinstance(instance, ClassesProv::Usage)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=ClassesProv::Operation_strategy)
@settings(max_examples=50)
def test_classesprov::operation_instantiation(instance):
    assert isinstance(instance, ClassesProv::Operation)

@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, bool)


@given(instance=ClassesProv::Operation_strategy)
def test_classesprov::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassesProv::Class_strategy)
@settings(max_examples=50)
def test_classesprov::class_instantiation(instance):
    assert isinstance(instance, ClassesProv::Class)

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

@given(instance=ClassesProv::Substitution_strategy)
@settings(max_examples=50)
def test_classesprov::substitution_instantiation(instance):
    assert isinstance(instance, ClassesProv::Substitution)

@given(instance=ClassesProv::Property_strategy)
@settings(max_examples=50)
def test_classesprov::property_instantiation(instance):
    assert isinstance(instance, ClassesProv::Property)

@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, bool)


@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isID_type(instance):
    assert isinstance(instance.isID, bool)


@given(instance=ClassesProv::Property_strategy)
def test_classesprov::property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=ClassesProv::Interface_strategy)
@settings(max_examples=50)
def test_classesprov::interface_instantiation(instance):
    assert isinstance(instance, ClassesProv::Interface)

@given(instance=ClassesProv::DataType_strategy)
@settings(max_examples=50)
def test_classesprov::datatype_instantiation(instance):
    assert isinstance(instance, ClassesProv::DataType)

@given(instance=ClassesProv::InstanceValue_strategy)
@settings(max_examples=50)
def test_classesprov::instancevalue_instantiation(instance):
    assert isinstance(instance, ClassesProv::InstanceValue)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=ClassesProv::LiteralString_strategy)
@settings(max_examples=50)
def test_classesprov::literalstring_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralString)

@given(instance=ClassesProv::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_classesprov::literalboolean_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralBoolean)

@given(instance=ClassesProv::LiteralReal_strategy)
@settings(max_examples=50)
def test_classesprov::literalreal_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralReal)

@given(instance=ClassesProv::LiteralInteger_strategy)
@settings(max_examples=50)
def test_classesprov::literalinteger_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralInteger)

@given(instance=ClassesProv::LiteralUnilimitedNatural_strategy)
@settings(max_examples=50)
def test_classesprov::literalunilimitednatural_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralUnilimitedNatural)

@given(instance=ClassesProv::LiteralNull_strategy)
@settings(max_examples=50)
def test_classesprov::literalnull_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralNull)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=ClassesProv::Feature_strategy)
@settings(max_examples=50)
def test_classesprov::feature_instantiation(instance):
    assert isinstance(instance, ClassesProv::Feature)

@given(instance=ClassesProv::Feature_strategy)
def test_classesprov::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=ClassesProv::Feature_strategy)
def test_classesprov::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ClassesProv::Parameter_strategy)
@settings(max_examples=50)
def test_classesprov::parameter_instantiation(instance):
    assert isinstance(instance, ClassesProv::Parameter)

@given(instance=ClassesProv::Parameter_strategy)
def test_classesprov::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=ClassesProv::Parameter_strategy)
def test_classesprov::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=ClassesProv::StructuralFeature_strategy)
@settings(max_examples=50)
def test_classesprov::structuralfeature_instantiation(instance):
    assert isinstance(instance, ClassesProv::StructuralFeature)

@given(instance=ClassesProv::StructuralFeature_strategy)
def test_classesprov::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=ClassesProv::StructuralFeature_strategy)
def test_classesprov::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=ClassesProv::Association_strategy)
@settings(max_examples=50)
def test_classesprov::association_instantiation(instance):
    assert isinstance(instance, ClassesProv::Association)

@given(instance=ClassesProv::Association_strategy)
def test_classesprov::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=ClassesProv::Association_strategy)
def test_classesprov::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=ClassesProv::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_classesprov::directedrelationship_instantiation(instance):
    assert isinstance(instance, ClassesProv::DirectedRelationship)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=ClassesProv::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_classesprov::literalspecification_instantiation(instance):
    assert isinstance(instance, ClassesProv::LiteralSpecification)

@given(instance=ClassesProv::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_classesprov::opaqueexpression_instantiation(instance):
    assert isinstance(instance, ClassesProv::OpaqueExpression)

@given(instance=ClassesProv::OpaqueExpression_strategy)
def test_classesprov::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=ClassesProv::OpaqueExpression_strategy)
def test_classesprov::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=ClassesProv::OpaqueExpression_strategy)
def test_classesprov::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=ClassesProv::OpaqueExpression_strategy)
def test_classesprov::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=ClassesProv::Expression_strategy)
@settings(max_examples=50)
def test_classesprov::expression_instantiation(instance):
    assert isinstance(instance, ClassesProv::Expression)

@given(instance=ClassesProv::Expression_strategy)
def test_classesprov::expression_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=ClassesProv::Expression_strategy)
def test_classesprov::expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=ClassesProv::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_classesprov::generalizationset_instantiation(instance):
    assert isinstance(instance, ClassesProv::GeneralizationSet)

@given(instance=ClassesProv::GeneralizationSet_strategy)
def test_classesprov::generalizationset_isCovering_type(instance):
    assert isinstance(instance.isCovering, bool)


@given(instance=ClassesProv::GeneralizationSet_strategy)
def test_classesprov::generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=ClassesProv::GeneralizationSet_strategy)
def test_classesprov::generalizationset_isDisjoint_type(instance):
    assert isinstance(instance.isDisjoint, bool)


@given(instance=ClassesProv::GeneralizationSet_strategy)
def test_classesprov::generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=ClassesProv::ValueSpecification_strategy)
@settings(max_examples=50)
def test_classesprov::valuespecification_instantiation(instance):
    assert isinstance(instance, ClassesProv::ValueSpecification)

@given(instance=ClassesProv::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_classesprov::instancespecification_instantiation(instance):
    assert isinstance(instance, ClassesProv::InstanceSpecification)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=ClassesProv::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_classesprov::behavioralfeature_instantiation(instance):
    assert isinstance(instance, ClassesProv::BehavioralFeature)

@given(instance=ClassesProv::Classifier_strategy)
@settings(max_examples=50)
def test_classesprov::classifier_instantiation(instance):
    assert isinstance(instance, ClassesProv::Classifier)

@given(instance=ClassesProv::Classifier_strategy)
def test_classesprov::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=ClassesProv::Classifier_strategy)
def test_classesprov::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ClassesProv::Classifier_strategy)
def test_classesprov::classifier_isFinalSpecialization_type(instance):
    assert isinstance(instance.isFinalSpecialization, bool)


@given(instance=ClassesProv::Classifier_strategy)
def test_classesprov::classifier_isFinalSpecialization_setter(instance):
    original = instance.isFinalSpecialization
    instance.isFinalSpecialization = original
    assert instance.isFinalSpecialization == original

@given(instance=ClassesProv::Package_strategy)
@settings(max_examples=50)
def test_classesprov::package_instantiation(instance):
    assert isinstance(instance, ClassesProv::Package)

@given(instance=ClassesProv::Package_strategy)
def test_classesprov::package_URI_type(instance):
    assert isinstance(instance.URI, str)


@given(instance=ClassesProv::Package_strategy)
def test_classesprov::package_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=ClassesProv::Generalization_strategy)
@settings(max_examples=50)
def test_classesprov::generalization_instantiation(instance):
    assert isinstance(instance, ClassesProv::Generalization)

@given(instance=ClassesProv::Generalization_strategy)
def test_classesprov::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, bool)


@given(instance=ClassesProv::Generalization_strategy)
def test_classesprov::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=ClassesProv::Constraint_strategy)
@settings(max_examples=50)
def test_classesprov::constraint_instantiation(instance):
    assert isinstance(instance, ClassesProv::Constraint)

@given(instance=ClassesProv::PackageImport_strategy)
@settings(max_examples=50)
def test_classesprov::packageimport_instantiation(instance):
    assert isinstance(instance, ClassesProv::PackageImport)

@given(instance=ClassesProv::ElementImport_strategy)
@settings(max_examples=50)
def test_classesprov::elementimport_instantiation(instance):
    assert isinstance(instance, ClassesProv::ElementImport)

@given(instance=ClassesProv::ElementImport_strategy)
def test_classesprov::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=ClassesProv::ElementImport_strategy)
def test_classesprov::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ClassesProv::RedefinableElement_strategy)
@settings(max_examples=50)
def test_classesprov::redefinableelement_instantiation(instance):
    assert isinstance(instance, ClassesProv::RedefinableElement)

@given(instance=ClassesProv::RedefinableElement_strategy)
def test_classesprov::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, bool)


@given(instance=ClassesProv::RedefinableElement_strategy)
def test_classesprov::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=ClassesProv::TypedElement_strategy)
@settings(max_examples=50)
def test_classesprov::typedelement_instantiation(instance):
    assert isinstance(instance, ClassesProv::TypedElement)

@given(instance=ClassesProv::PackageableElement_strategy)
@settings(max_examples=50)
def test_classesprov::packageableelement_instantiation(instance):
    assert isinstance(instance, ClassesProv::PackageableElement)

@given(instance=ClassesProv::Dependency_strategy)
@settings(max_examples=50)
def test_classesprov::dependency_instantiation(instance):
    assert isinstance(instance, ClassesProv::Dependency)

@given(instance=ClassesProv::Namespace_strategy)
@settings(max_examples=50)
def test_classesprov::namespace_instantiation(instance):
    assert isinstance(instance, ClassesProv::Namespace)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ClassesProv::Slot_strategy)
@settings(max_examples=50)
def test_classesprov::slot_instantiation(instance):
    assert isinstance(instance, ClassesProv::Slot)

@given(instance=ClassesProv::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_classesprov::multiplicityelement_instantiation(instance):
    assert isinstance(instance, ClassesProv::MultiplicityElement)

@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=ClassesProv::MultiplicityElement_strategy)
def test_classesprov::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=ClassesProv::Relationship_strategy)
@settings(max_examples=50)
def test_classesprov::relationship_instantiation(instance):
    assert isinstance(instance, ClassesProv::Relationship)

@given(instance=ClassesProv::NamedElement_strategy)
@settings(max_examples=50)
def test_classesprov::namedelement_instantiation(instance):
    assert isinstance(instance, ClassesProv::NamedElement)

@given(instance=ClassesProv::NamedElement_strategy)
def test_classesprov::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassesProv::NamedElement_strategy)
def test_classesprov::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassesProv::NamedElement_strategy)
def test_classesprov::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=ClassesProv::NamedElement_strategy)
def test_classesprov::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=ClassesProv::PackageMerge_strategy)
@settings(max_examples=50)
def test_classesprov::packagemerge_instantiation(instance):
    assert isinstance(instance, ClassesProv::PackageMerge)

@given(instance=ClassesProv::Type_strategy)
@settings(max_examples=50)
def test_classesprov::type_instantiation(instance):
    assert isinstance(instance, ClassesProv::Type)

@given(instance=ClassesProv::Element_strategy)
@settings(max_examples=50)
def test_classesprov::element_instantiation(instance):
    assert isinstance(instance, ClassesProv::Element)
