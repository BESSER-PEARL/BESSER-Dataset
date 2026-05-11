import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EGenericType,
    ecoreDiff::AddedEGenericType,
    ETypeParameter,
    ecoreDiff::ChangedETypeParameter,
    ecoreDiff::DeletedETypeParameter,
    ecoreDiff::AddedETypeParameter,
    EPackage,
    ecoreDiff::ChangedEPackage,
    ecoreDiff::DeletedEPackage,
    ecoreDiff::AddedEPackage,
    EClass,
    ecoreDiff::AddedEClass,
    ecoreDiff::ChangedEClass,
    ecoreDiff::DeletedEClass,
    EAnnotation,
    ecoreDiff::AddedEAnnotation,
    ecoreDiff::DifferenceElement,
    ecoreDiff::DifferenceModel,
    DifferenceElement,
    EStringToStringMapEntry,
    ecoreDiff::DeletedEStringToStringMapEntry,
    ecoreDiff::ChangedEStringToStringMapEntry,
    ecoreDiff::AddedEStringToStringMapEntry,
    ecoreDiff::ChangedEAnnotation,
    ecoreDiff::DeletedEAnnotation,
    EStructuralFeature,
    ecoreDiff::EAttribute,
    EDataType,
    ecoreDiff::DeletedEDataType,
    ecoreDiff::ChangedEDataType,
    ecoreDiff::EEnum,
    ecoreDiff::EReference,
    ecoreDiff::EStructuralFeature::Wildcard,
    EObject,
    ecoreDiff::ChangedEObject,
    ecoreDiff::DeletedEObject,
    ecoreDiff::AddedEObject,
    ETypedElement,
    ecoreDiff::EParameter,
    ecoreDiff::EClassifier::Wildcard,
    ecoreDiff::EGenericType,
    ecoreDiff::EStructuralFeature,
    ecoreDiff::EOperation,
    ENamedElement,
    ecoreDiff::ETypeParameter,
    ecoreDiff::AddedENamedElement,
    ecoreDiff::EEnumLiteral,
    ecoreDiff::ETypedElement,
    ecoreDiff::EPackage,
    ecoreDiff::ChangedENamedElement,
    ecoreDiff::DeletedENamedElement,
    ecoreDiff::EClassifier,
    EClassifier,
    ecoreDiff::DeletedEClassifier,
    ecoreDiff::ChangedEClassifier,
    ecoreDiff::EDataType,
    ecoreDiff::AddedEClassifier,
    ecoreDiff::EClass,
    ecoreDiff::EObject,
    ecoreDiff::EModelElement,
    ecoreDiff::EStringToStringMapEntry,
    EModelElement,
    ecoreDiff::EFactory,
    ecoreDiff::ENamedElement,
    ecoreDiff::EAnnotation,
    ecoreDiff::ChangedEModelElement,
    ecoreDiff::DeletedEModelElement,
    ecoreDiff::AddedEModelElement,
    EEnumLiteral,
    ecoreDiff::DeletedEEnumLiteral,
    ecoreDiff::ChangedEEnumLiteral,
    ecoreDiff::AddedEEnumLiteral,
    EStructuralFeature::Wildcard,
    ecoreDiff::AddedEStructuralFeature::Wildcard,
    EEnum,
    ecoreDiff::DeletedEEnum,
    ecoreDiff::ChangedEEnum,
    ecoreDiff::AddedEEnum,
    EReference,
    ecoreDiff::ChangedEReference,
    ecoreDiff::DeletedEReference,
    ecoreDiff::AddedEReference,
    ecoreDiff::ChangedEStructuralFeature::Wildcard,
    ecoreDiff::DeletedEStructuralFeature::Wildcard,
    ecoreDiff::ChangedEStructuralFeature,
    ecoreDiff::DeletedEStructuralFeature,
    ecoreDiff::AddedEStructuralFeature,
    EParameter,
    ecoreDiff::ChangedEParameter,
    ecoreDiff::DeletedEParameter,
    EAttribute,
    ecoreDiff::DeletedEAttribute,
    ecoreDiff::ChangedEAttribute,
    ecoreDiff::AddedEAttribute,
    EClassifier::Wildcard,
    ecoreDiff::ChangedEClassifier::Wildcard,
    ecoreDiff::DeletedEClassifier::Wildcard,
    ecoreDiff::AddedEClassifier::Wildcard,
    ecoreDiff::ChangedEGenericType,
    ecoreDiff::DeletedEGenericType,
    ecoreDiff::AddedEParameter,
    ecoreDiff::ChangedETypedElement,
    ecoreDiff::DeletedETypedElement,
    ecoreDiff::AddedETypedElement,
    EOperation,
    ecoreDiff::DeletedEOperation,
    ecoreDiff::ChangedEOperation,
    ecoreDiff::AddedEOperation,
    ecoreDiff::AddedEDataType,
    EFactory,
    ecoreDiff::DeletedEFactory,
    ecoreDiff::ChangedEFactory,
    ecoreDiff::AddedEFactory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_egenerictype_is_not_abstract():
    assert not inspect.isabstract(EGenericType)


def test_egenerictype_constructor_exists():
    assert callable(EGenericType.__init__)


def test_egenerictype_constructor_args():
    sig = inspect.signature(EGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedegenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEGenericType)


def test_ecorediff::addedegenerictype_constructor_exists():
    assert callable(ecoreDiff::AddedEGenericType.__init__)


def test_ecorediff::addedegenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEGenericType.__init__)
    params = list(sig.parameters.keys())



def test_etypeparameter_is_not_abstract():
    assert not inspect.isabstract(ETypeParameter)


def test_etypeparameter_constructor_exists():
    assert callable(ETypeParameter.__init__)


def test_etypeparameter_constructor_args():
    sig = inspect.signature(ETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedetypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedETypeParameter)


def test_ecorediff::changedetypeparameter_constructor_exists():
    assert callable(ecoreDiff::ChangedETypeParameter.__init__)


def test_ecorediff::changedetypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedetypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedETypeParameter)


def test_ecorediff::deletedetypeparameter_constructor_exists():
    assert callable(ecoreDiff::DeletedETypeParameter.__init__)


def test_ecorediff::deletedetypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedetypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedETypeParameter)


def test_ecorediff::addedetypeparameter_constructor_exists():
    assert callable(ecoreDiff::AddedETypeParameter.__init__)


def test_ecorediff::addedetypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedepackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEPackage)


def test_ecorediff::changedepackage_constructor_exists():
    assert callable(ecoreDiff::ChangedEPackage.__init__)


def test_ecorediff::changedepackage_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedepackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEPackage)


def test_ecorediff::deletedepackage_constructor_exists():
    assert callable(ecoreDiff::DeletedEPackage.__init__)


def test_ecorediff::deletedepackage_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedepackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEPackage)


def test_ecorediff::addedepackage_constructor_exists():
    assert callable(ecoreDiff::AddedEPackage.__init__)


def test_ecorediff::addedepackage_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEPackage.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEClass)


def test_ecorediff::addedeclass_constructor_exists():
    assert callable(ecoreDiff::AddedEClass.__init__)


def test_ecorediff::addedeclass_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEClass.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEClass)


def test_ecorediff::changedeclass_constructor_exists():
    assert callable(ecoreDiff::ChangedEClass.__init__)


def test_ecorediff::changedeclass_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEClass.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEClass)


def test_ecorediff::deletedeclass_constructor_exists():
    assert callable(ecoreDiff::DeletedEClass.__init__)


def test_ecorediff::deletedeclass_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEClass.__init__)
    params = list(sig.parameters.keys())



def test_eannotation_is_not_abstract():
    assert not inspect.isabstract(EAnnotation)


def test_eannotation_constructor_exists():
    assert callable(EAnnotation.__init__)


def test_eannotation_constructor_args():
    sig = inspect.signature(EAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEAnnotation)


def test_ecorediff::addedeannotation_constructor_exists():
    assert callable(ecoreDiff::AddedEAnnotation.__init__)


def test_ecorediff::addedeannotation_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::differenceelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DifferenceElement)


def test_ecorediff::differenceelement_constructor_exists():
    assert callable(ecoreDiff::DifferenceElement.__init__)


def test_ecorediff::differenceelement_constructor_args():
    sig = inspect.signature(ecoreDiff::DifferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::differencemodel_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DifferenceModel)


def test_ecorediff::differencemodel_constructor_exists():
    assert callable(ecoreDiff::DifferenceModel.__init__)


def test_ecorediff::differencemodel_constructor_args():
    sig = inspect.signature(ecoreDiff::DifferenceModel.__init__)
    params = list(sig.parameters.keys())



def test_differenceelement_is_not_abstract():
    assert not inspect.isabstract(DifferenceElement)


def test_differenceelement_constructor_exists():
    assert callable(DifferenceElement.__init__)


def test_differenceelement_constructor_args():
    sig = inspect.signature(DifferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(EStringToStringMapEntry)


def test_estringtostringmapentry_constructor_exists():
    assert callable(EStringToStringMapEntry.__init__)


def test_estringtostringmapentry_constructor_args():
    sig = inspect.signature(EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEStringToStringMapEntry)


def test_ecorediff::deletedestringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff::DeletedEStringToStringMapEntry.__init__)


def test_ecorediff::deletedestringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEStringToStringMapEntry)


def test_ecorediff::changedestringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff::ChangedEStringToStringMapEntry.__init__)


def test_ecorediff::changedestringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEStringToStringMapEntry)


def test_ecorediff::addedestringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff::AddedEStringToStringMapEntry.__init__)


def test_ecorediff::addedestringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEAnnotation)


def test_ecorediff::changedeannotation_constructor_exists():
    assert callable(ecoreDiff::ChangedEAnnotation.__init__)


def test_ecorediff::changedeannotation_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEAnnotation)


def test_ecorediff::deletedeannotation_constructor_exists():
    assert callable(ecoreDiff::DeletedEAnnotation.__init__)


def test_ecorediff::deletedeannotation_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EAttribute)


def test_ecorediff::eattribute_constructor_exists():
    assert callable(ecoreDiff::EAttribute.__init__)


def test_ecorediff::eattribute_constructor_args():
    sig = inspect.signature(ecoreDiff::EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_ecorediff::eattribute_has_iD():
    assert hasattr(ecoreDiff::EAttribute, "iD")
    descriptor = None
    for klass in ecoreDiff::EAttribute.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletededatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEDataType)


def test_ecorediff::deletededatatype_constructor_exists():
    assert callable(ecoreDiff::DeletedEDataType.__init__)


def test_ecorediff::deletededatatype_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changededatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEDataType)


def test_ecorediff::changededatatype_constructor_exists():
    assert callable(ecoreDiff::ChangedEDataType.__init__)


def test_ecorediff::changededatatype_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EEnum)


def test_ecorediff::eenum_constructor_exists():
    assert callable(ecoreDiff::EEnum.__init__)


def test_ecorediff::eenum_constructor_args():
    sig = inspect.signature(ecoreDiff::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::ereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EReference)


def test_ecorediff::ereference_constructor_exists():
    assert callable(ecoreDiff::EReference.__init__)


def test_ecorediff::ereference_constructor_args():
    sig = inspect.signature(ecoreDiff::EReference.__init__)
    params = list(sig.parameters.keys())
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"
    assert "containment" in params, "Missing parameter 'containment'"

def test_ecorediff::ereference_has_resolveProxies():
    assert hasattr(ecoreDiff::EReference, "resolveProxies")
    descriptor = None
    for klass in ecoreDiff::EReference.__mro__:
        if "resolveProxies" in klass.__dict__:
            descriptor = klass.__dict__["resolveProxies"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::ereference_has_containment():
    assert hasattr(ecoreDiff::EReference, "containment")
    descriptor = None
    for klass in ecoreDiff::EReference.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::estructuralfeature::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EStructuralFeature::Wildcard)


def test_ecorediff::estructuralfeature::wildcard_constructor_exists():
    assert callable(ecoreDiff::EStructuralFeature::Wildcard.__init__)


def test_ecorediff::estructuralfeature::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::EStructuralFeature::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEObject)


def test_ecorediff::changedeobject_constructor_exists():
    assert callable(ecoreDiff::ChangedEObject.__init__)


def test_ecorediff::changedeobject_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEObject)


def test_ecorediff::deletedeobject_constructor_exists():
    assert callable(ecoreDiff::DeletedEObject.__init__)


def test_ecorediff::deletedeobject_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEObject)


def test_ecorediff::addedeobject_constructor_exists():
    assert callable(ecoreDiff::AddedEObject.__init__)


def test_ecorediff::addedeobject_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEObject.__init__)
    params = list(sig.parameters.keys())



def test_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EParameter)


def test_ecorediff::eparameter_constructor_exists():
    assert callable(ecoreDiff::EParameter.__init__)


def test_ecorediff::eparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::EParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eclassifier::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EClassifier::Wildcard)


def test_ecorediff::eclassifier::wildcard_constructor_exists():
    assert callable(ecoreDiff::EClassifier::Wildcard.__init__)


def test_ecorediff::eclassifier::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::EClassifier::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::egenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EGenericType)


def test_ecorediff::egenerictype_constructor_exists():
    assert callable(ecoreDiff::EGenericType.__init__)


def test_ecorediff::egenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff::EGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EStructuralFeature)


def test_ecorediff::estructuralfeature_constructor_exists():
    assert callable(ecoreDiff::EStructuralFeature.__init__)


def test_ecorediff::estructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "unsettable" in params, "Missing parameter 'unsettable'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_ecorediff::estructuralfeature_has_transient():
    assert hasattr(ecoreDiff::EStructuralFeature, "transient")
    descriptor = None
    for klass in ecoreDiff::EStructuralFeature.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::estructuralfeature_has_changeable():
    assert hasattr(ecoreDiff::EStructuralFeature, "changeable")
    descriptor = None
    for klass in ecoreDiff::EStructuralFeature.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::estructuralfeature_has_defaultValueLiteral():
    assert hasattr(ecoreDiff::EStructuralFeature, "defaultValueLiteral")
    descriptor = None
    for klass in ecoreDiff::EStructuralFeature.__mro__:
        if "defaultValueLiteral" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueLiteral"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::estructuralfeature_has_volatile():
    assert hasattr(ecoreDiff::EStructuralFeature, "volatile")
    descriptor = None
    for klass in ecoreDiff::EStructuralFeature.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::estructuralfeature_has_unsettable():
    assert hasattr(ecoreDiff::EStructuralFeature, "unsettable")
    descriptor = None
    for klass in ecoreDiff::EStructuralFeature.__mro__:
        if "unsettable" in klass.__dict__:
            descriptor = klass.__dict__["unsettable"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::estructuralfeature_has_derived():
    assert hasattr(ecoreDiff::EStructuralFeature, "derived")
    descriptor = None
    for klass in ecoreDiff::EStructuralFeature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::eoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EOperation)


def test_ecorediff::eoperation_constructor_exists():
    assert callable(ecoreDiff::EOperation.__init__)


def test_ecorediff::eoperation_constructor_args():
    sig = inspect.signature(ecoreDiff::EOperation.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::etypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ETypeParameter)


def test_ecorediff::etypeparameter_constructor_exists():
    assert callable(ecoreDiff::ETypeParameter.__init__)


def test_ecorediff::etypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::ETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedenamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedENamedElement)


def test_ecorediff::addedenamedelement_constructor_exists():
    assert callable(ecoreDiff::AddedENamedElement.__init__)


def test_ecorediff::addedenamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EEnumLiteral)


def test_ecorediff::eenumliteral_constructor_exists():
    assert callable(ecoreDiff::EEnumLiteral.__init__)


def test_ecorediff::eenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "literal" in params, "Missing parameter 'literal'"

def test_ecorediff::eenumliteral_has_value():
    assert hasattr(ecoreDiff::EEnumLiteral, "value")
    descriptor = None
    for klass in ecoreDiff::EEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::eenumliteral_has_instance():
    assert hasattr(ecoreDiff::EEnumLiteral, "instance")
    descriptor = None
    for klass in ecoreDiff::EEnumLiteral.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::eenumliteral_has_literal():
    assert hasattr(ecoreDiff::EEnumLiteral, "literal")
    descriptor = None
    for klass in ecoreDiff::EEnumLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::etypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ETypedElement)


def test_ecorediff::etypedelement_constructor_exists():
    assert callable(ecoreDiff::ETypedElement.__init__)


def test_ecorediff::etypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::ETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_ecorediff::etypedelement_has_ordered():
    assert hasattr(ecoreDiff::ETypedElement, "ordered")
    descriptor = None
    for klass in ecoreDiff::ETypedElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::etypedelement_has_lowerBound():
    assert hasattr(ecoreDiff::ETypedElement, "lowerBound")
    descriptor = None
    for klass in ecoreDiff::ETypedElement.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::etypedelement_has_upperBound():
    assert hasattr(ecoreDiff::ETypedElement, "upperBound")
    descriptor = None
    for klass in ecoreDiff::ETypedElement.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::etypedelement_has_unique():
    assert hasattr(ecoreDiff::ETypedElement, "unique")
    descriptor = None
    for klass in ecoreDiff::ETypedElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::epackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EPackage)


def test_ecorediff::epackage_constructor_exists():
    assert callable(ecoreDiff::EPackage.__init__)


def test_ecorediff::epackage_constructor_args():
    sig = inspect.signature(ecoreDiff::EPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"

def test_ecorediff::epackage_has_nsURI():
    assert hasattr(ecoreDiff::EPackage, "nsURI")
    descriptor = None
    for klass in ecoreDiff::EPackage.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::epackage_has_nsPrefix():
    assert hasattr(ecoreDiff::EPackage, "nsPrefix")
    descriptor = None
    for klass in ecoreDiff::EPackage.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::changedenamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedENamedElement)


def test_ecorediff::changedenamedelement_constructor_exists():
    assert callable(ecoreDiff::ChangedENamedElement.__init__)


def test_ecorediff::changedenamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedenamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedENamedElement)


def test_ecorediff::deletedenamedelement_constructor_exists():
    assert callable(ecoreDiff::DeletedENamedElement.__init__)


def test_ecorediff::deletedenamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EClassifier)


def test_ecorediff::eclassifier_constructor_exists():
    assert callable(ecoreDiff::EClassifier.__init__)


def test_ecorediff::eclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff::EClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"
    assert "instanceTypeName" in params, "Missing parameter 'instanceTypeName'"

def test_ecorediff::eclassifier_has_instanceClassName():
    assert hasattr(ecoreDiff::EClassifier, "instanceClassName")
    descriptor = None
    for klass in ecoreDiff::EClassifier.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::eclassifier_has_instanceTypeName():
    assert hasattr(ecoreDiff::EClassifier, "instanceTypeName")
    descriptor = None
    for klass in ecoreDiff::EClassifier.__mro__:
        if "instanceTypeName" in klass.__dict__:
            descriptor = klass.__dict__["instanceTypeName"]
            break
    assert isinstance(descriptor, property)



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEClassifier)


def test_ecorediff::deletedeclassifier_constructor_exists():
    assert callable(ecoreDiff::DeletedEClassifier.__init__)


def test_ecorediff::deletedeclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEClassifier)


def test_ecorediff::changedeclassifier_constructor_exists():
    assert callable(ecoreDiff::ChangedEClassifier.__init__)


def test_ecorediff::changedeclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::edatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EDataType)


def test_ecorediff::edatatype_constructor_exists():
    assert callable(ecoreDiff::EDataType.__init__)


def test_ecorediff::edatatype_constructor_args():
    sig = inspect.signature(ecoreDiff::EDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"

def test_ecorediff::edatatype_has_serializable():
    assert hasattr(ecoreDiff::EDataType, "serializable")
    descriptor = None
    for klass in ecoreDiff::EDataType.__mro__:
        if "serializable" in klass.__dict__:
            descriptor = klass.__dict__["serializable"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::addedeclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEClassifier)


def test_ecorediff::addedeclassifier_constructor_exists():
    assert callable(ecoreDiff::AddedEClassifier.__init__)


def test_ecorediff::addedeclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::eclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EClass)


def test_ecorediff::eclass_constructor_exists():
    assert callable(ecoreDiff::EClass.__init__)


def test_ecorediff::eclass_constructor_args():
    sig = inspect.signature(ecoreDiff::EClass.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ecorediff::eclass_has_interface():
    assert hasattr(ecoreDiff::EClass, "interface")
    descriptor = None
    for klass in ecoreDiff::EClass.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::eclass_has_abstract():
    assert hasattr(ecoreDiff::EClass, "abstract")
    descriptor = None
    for klass in ecoreDiff::EClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::eobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EObject)


def test_ecorediff::eobject_constructor_exists():
    assert callable(ecoreDiff::EObject.__init__)


def test_ecorediff::eobject_constructor_args():
    sig = inspect.signature(ecoreDiff::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::emodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EModelElement)


def test_ecorediff::emodelelement_constructor_exists():
    assert callable(ecoreDiff::EModelElement.__init__)


def test_ecorediff::emodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff::EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EStringToStringMapEntry)


def test_ecorediff::estringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff::EStringToStringMapEntry.__init__)


def test_ecorediff::estringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_ecorediff::estringtostringmapentry_has_key():
    assert hasattr(ecoreDiff::EStringToStringMapEntry, "key")
    descriptor = None
    for klass in ecoreDiff::EStringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff::estringtostringmapentry_has_value():
    assert hasattr(ecoreDiff::EStringToStringMapEntry, "value")
    descriptor = None
    for klass in ecoreDiff::EStringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::efactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EFactory)


def test_ecorediff::efactory_constructor_exists():
    assert callable(ecoreDiff::EFactory.__init__)


def test_ecorediff::efactory_constructor_args():
    sig = inspect.signature(ecoreDiff::EFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::enamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ENamedElement)


def test_ecorediff::enamedelement_constructor_exists():
    assert callable(ecoreDiff::ENamedElement.__init__)


def test_ecorediff::enamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecorediff::enamedelement_has_name():
    assert hasattr(ecoreDiff::ENamedElement, "name")
    descriptor = None
    for klass in ecoreDiff::ENamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::eannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::EAnnotation)


def test_ecorediff::eannotation_constructor_exists():
    assert callable(ecoreDiff::EAnnotation.__init__)


def test_ecorediff::eannotation_constructor_args():
    sig = inspect.signature(ecoreDiff::EAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_ecorediff::eannotation_has_source():
    assert hasattr(ecoreDiff::EAnnotation, "source")
    descriptor = None
    for klass in ecoreDiff::EAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff::changedemodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEModelElement)


def test_ecorediff::changedemodelelement_constructor_exists():
    assert callable(ecoreDiff::ChangedEModelElement.__init__)


def test_ecorediff::changedemodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedemodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEModelElement)


def test_ecorediff::deletedemodelelement_constructor_exists():
    assert callable(ecoreDiff::DeletedEModelElement.__init__)


def test_ecorediff::deletedemodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedemodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEModelElement)


def test_ecorediff::addedemodelelement_constructor_exists():
    assert callable(ecoreDiff::AddedEModelElement.__init__)


def test_ecorediff::addedemodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(EEnumLiteral)


def test_eenumliteral_constructor_exists():
    assert callable(EEnumLiteral.__init__)


def test_eenumliteral_constructor_args():
    sig = inspect.signature(EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEEnumLiteral)


def test_ecorediff::deletedeenumliteral_constructor_exists():
    assert callable(ecoreDiff::DeletedEEnumLiteral.__init__)


def test_ecorediff::deletedeenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEEnumLiteral)


def test_ecorediff::changedeenumliteral_constructor_exists():
    assert callable(ecoreDiff::ChangedEEnumLiteral.__init__)


def test_ecorediff::changedeenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEEnumLiteral)


def test_ecorediff::addedeenumliteral_constructor_exists():
    assert callable(ecoreDiff::AddedEEnumLiteral.__init__)


def test_ecorediff::addedeenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeature::wildcard_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature::Wildcard)


def test_estructuralfeature::wildcard_constructor_exists():
    assert callable(EStructuralFeature::Wildcard.__init__)


def test_estructuralfeature::wildcard_constructor_args():
    sig = inspect.signature(EStructuralFeature::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedestructuralfeature::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEStructuralFeature::Wildcard)


def test_ecorediff::addedestructuralfeature::wildcard_constructor_exists():
    assert callable(ecoreDiff::AddedEStructuralFeature::Wildcard.__init__)


def test_ecorediff::addedestructuralfeature::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEStructuralFeature::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_eenum_is_not_abstract():
    assert not inspect.isabstract(EEnum)


def test_eenum_constructor_exists():
    assert callable(EEnum.__init__)


def test_eenum_constructor_args():
    sig = inspect.signature(EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEEnum)


def test_ecorediff::deletedeenum_constructor_exists():
    assert callable(ecoreDiff::DeletedEEnum.__init__)


def test_ecorediff::deletedeenum_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEEnum)


def test_ecorediff::changedeenum_constructor_exists():
    assert callable(ecoreDiff::ChangedEEnum.__init__)


def test_ecorediff::changedeenum_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEEnum)


def test_ecorediff::addedeenum_constructor_exists():
    assert callable(ecoreDiff::AddedEEnum.__init__)


def test_ecorediff::addedeenum_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEEnum.__init__)
    params = list(sig.parameters.keys())



def test_ereference_is_not_abstract():
    assert not inspect.isabstract(EReference)


def test_ereference_constructor_exists():
    assert callable(EReference.__init__)


def test_ereference_constructor_args():
    sig = inspect.signature(EReference.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEReference)


def test_ecorediff::changedereference_constructor_exists():
    assert callable(ecoreDiff::ChangedEReference.__init__)


def test_ecorediff::changedereference_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEReference.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEReference)


def test_ecorediff::deletedereference_constructor_exists():
    assert callable(ecoreDiff::DeletedEReference.__init__)


def test_ecorediff::deletedereference_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEReference.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEReference)


def test_ecorediff::addedereference_constructor_exists():
    assert callable(ecoreDiff::AddedEReference.__init__)


def test_ecorediff::addedereference_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEReference.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedestructuralfeature::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEStructuralFeature::Wildcard)


def test_ecorediff::changedestructuralfeature::wildcard_constructor_exists():
    assert callable(ecoreDiff::ChangedEStructuralFeature::Wildcard.__init__)


def test_ecorediff::changedestructuralfeature::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEStructuralFeature::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedestructuralfeature::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEStructuralFeature::Wildcard)


def test_ecorediff::deletedestructuralfeature::wildcard_constructor_exists():
    assert callable(ecoreDiff::DeletedEStructuralFeature::Wildcard.__init__)


def test_ecorediff::deletedestructuralfeature::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEStructuralFeature::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEStructuralFeature)


def test_ecorediff::changedestructuralfeature_constructor_exists():
    assert callable(ecoreDiff::ChangedEStructuralFeature.__init__)


def test_ecorediff::changedestructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEStructuralFeature)


def test_ecorediff::deletedestructuralfeature_constructor_exists():
    assert callable(ecoreDiff::DeletedEStructuralFeature.__init__)


def test_ecorediff::deletedestructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEStructuralFeature)


def test_ecorediff::addedestructuralfeature_constructor_exists():
    assert callable(ecoreDiff::AddedEStructuralFeature.__init__)


def test_ecorediff::addedestructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_eparameter_is_not_abstract():
    assert not inspect.isabstract(EParameter)


def test_eparameter_constructor_exists():
    assert callable(EParameter.__init__)


def test_eparameter_constructor_args():
    sig = inspect.signature(EParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEParameter)


def test_ecorediff::changedeparameter_constructor_exists():
    assert callable(ecoreDiff::ChangedEParameter.__init__)


def test_ecorediff::changedeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEParameter)


def test_ecorediff::deletedeparameter_constructor_exists():
    assert callable(ecoreDiff::DeletedEParameter.__init__)


def test_ecorediff::deletedeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEParameter.__init__)
    params = list(sig.parameters.keys())



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEAttribute)


def test_ecorediff::deletedeattribute_constructor_exists():
    assert callable(ecoreDiff::DeletedEAttribute.__init__)


def test_ecorediff::deletedeattribute_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEAttribute)


def test_ecorediff::changedeattribute_constructor_exists():
    assert callable(ecoreDiff::ChangedEAttribute.__init__)


def test_ecorediff::changedeattribute_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEAttribute)


def test_ecorediff::addedeattribute_constructor_exists():
    assert callable(ecoreDiff::AddedEAttribute.__init__)


def test_ecorediff::addedeattribute_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier::wildcard_is_not_abstract():
    assert not inspect.isabstract(EClassifier::Wildcard)


def test_eclassifier::wildcard_constructor_exists():
    assert callable(EClassifier::Wildcard.__init__)


def test_eclassifier::wildcard_constructor_args():
    sig = inspect.signature(EClassifier::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeclassifier::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEClassifier::Wildcard)


def test_ecorediff::changedeclassifier::wildcard_constructor_exists():
    assert callable(ecoreDiff::ChangedEClassifier::Wildcard.__init__)


def test_ecorediff::changedeclassifier::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEClassifier::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeclassifier::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEClassifier::Wildcard)


def test_ecorediff::deletedeclassifier::wildcard_constructor_exists():
    assert callable(ecoreDiff::DeletedEClassifier::Wildcard.__init__)


def test_ecorediff::deletedeclassifier::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEClassifier::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeclassifier::wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEClassifier::Wildcard)


def test_ecorediff::addedeclassifier::wildcard_constructor_exists():
    assert callable(ecoreDiff::AddedEClassifier::Wildcard.__init__)


def test_ecorediff::addedeclassifier::wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEClassifier::Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedegenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEGenericType)


def test_ecorediff::changedegenerictype_constructor_exists():
    assert callable(ecoreDiff::ChangedEGenericType.__init__)


def test_ecorediff::changedegenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedegenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEGenericType)


def test_ecorediff::deletedegenerictype_constructor_exists():
    assert callable(ecoreDiff::DeletedEGenericType.__init__)


def test_ecorediff::deletedegenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEParameter)


def test_ecorediff::addedeparameter_constructor_exists():
    assert callable(ecoreDiff::AddedEParameter.__init__)


def test_ecorediff::addedeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedetypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedETypedElement)


def test_ecorediff::changedetypedelement_constructor_exists():
    assert callable(ecoreDiff::ChangedETypedElement.__init__)


def test_ecorediff::changedetypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedetypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedETypedElement)


def test_ecorediff::deletedetypedelement_constructor_exists():
    assert callable(ecoreDiff::DeletedETypedElement.__init__)


def test_ecorediff::deletedetypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedetypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedETypedElement)


def test_ecorediff::addedetypedelement_constructor_exists():
    assert callable(ecoreDiff::AddedETypedElement.__init__)


def test_ecorediff::addedetypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedeoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEOperation)


def test_ecorediff::deletedeoperation_constructor_exists():
    assert callable(ecoreDiff::DeletedEOperation.__init__)


def test_ecorediff::deletedeoperation_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedeoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEOperation)


def test_ecorediff::changedeoperation_constructor_exists():
    assert callable(ecoreDiff::ChangedEOperation.__init__)


def test_ecorediff::changedeoperation_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedeoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEOperation)


def test_ecorediff::addedeoperation_constructor_exists():
    assert callable(ecoreDiff::AddedEOperation.__init__)


def test_ecorediff::addedeoperation_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addededatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEDataType)


def test_ecorediff::addededatatype_constructor_exists():
    assert callable(ecoreDiff::AddedEDataType.__init__)


def test_ecorediff::addededatatype_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEDataType.__init__)
    params = list(sig.parameters.keys())



def test_efactory_is_not_abstract():
    assert not inspect.isabstract(EFactory)


def test_efactory_constructor_exists():
    assert callable(EFactory.__init__)


def test_efactory_constructor_args():
    sig = inspect.signature(EFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::deletedefactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::DeletedEFactory)


def test_ecorediff::deletedefactory_constructor_exists():
    assert callable(ecoreDiff::DeletedEFactory.__init__)


def test_ecorediff::deletedefactory_constructor_args():
    sig = inspect.signature(ecoreDiff::DeletedEFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::changedefactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::ChangedEFactory)


def test_ecorediff::changedefactory_constructor_exists():
    assert callable(ecoreDiff::ChangedEFactory.__init__)


def test_ecorediff::changedefactory_constructor_args():
    sig = inspect.signature(ecoreDiff::ChangedEFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff::addedefactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff::AddedEFactory)


def test_ecorediff::addedefactory_constructor_exists():
    assert callable(ecoreDiff::AddedEFactory.__init__)


def test_ecorediff::addedefactory_constructor_args():
    sig = inspect.signature(ecoreDiff::AddedEFactory.__init__)
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
EGenericType_strategy = st.builds(
    EGenericType,
)
ecoreDiff::AddedEGenericType_strategy = st.builds(
    ecoreDiff::AddedEGenericType,
)
ETypeParameter_strategy = st.builds(
    ETypeParameter,
)
ecoreDiff::ChangedETypeParameter_strategy = st.builds(
    ecoreDiff::ChangedETypeParameter,
)
ecoreDiff::DeletedETypeParameter_strategy = st.builds(
    ecoreDiff::DeletedETypeParameter,
)
ecoreDiff::AddedETypeParameter_strategy = st.builds(
    ecoreDiff::AddedETypeParameter,
)
EPackage_strategy = st.builds(
    EPackage,
)
ecoreDiff::ChangedEPackage_strategy = st.builds(
    ecoreDiff::ChangedEPackage,
)
ecoreDiff::DeletedEPackage_strategy = st.builds(
    ecoreDiff::DeletedEPackage,
)
ecoreDiff::AddedEPackage_strategy = st.builds(
    ecoreDiff::AddedEPackage,
)
EClass_strategy = st.builds(
    EClass,
)
ecoreDiff::AddedEClass_strategy = st.builds(
    ecoreDiff::AddedEClass,
)
ecoreDiff::ChangedEClass_strategy = st.builds(
    ecoreDiff::ChangedEClass,
)
ecoreDiff::DeletedEClass_strategy = st.builds(
    ecoreDiff::DeletedEClass,
)
EAnnotation_strategy = st.builds(
    EAnnotation,
)
ecoreDiff::AddedEAnnotation_strategy = st.builds(
    ecoreDiff::AddedEAnnotation,
)
ecoreDiff::DifferenceElement_strategy = st.builds(
    ecoreDiff::DifferenceElement,
)
ecoreDiff::DifferenceModel_strategy = st.builds(
    ecoreDiff::DifferenceModel,
)
DifferenceElement_strategy = st.builds(
    DifferenceElement,
)
EStringToStringMapEntry_strategy = st.builds(
    EStringToStringMapEntry,
)
ecoreDiff::DeletedEStringToStringMapEntry_strategy = st.builds(
    ecoreDiff::DeletedEStringToStringMapEntry,
)
ecoreDiff::ChangedEStringToStringMapEntry_strategy = st.builds(
    ecoreDiff::ChangedEStringToStringMapEntry,
)
ecoreDiff::AddedEStringToStringMapEntry_strategy = st.builds(
    ecoreDiff::AddedEStringToStringMapEntry,
)
ecoreDiff::ChangedEAnnotation_strategy = st.builds(
    ecoreDiff::ChangedEAnnotation,
)
ecoreDiff::DeletedEAnnotation_strategy = st.builds(
    ecoreDiff::DeletedEAnnotation,
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
ecoreDiff::EAttribute_strategy = st.builds(
    ecoreDiff::EAttribute,
    iD=
        st.booleans()
)
EDataType_strategy = st.builds(
    EDataType,
)
ecoreDiff::DeletedEDataType_strategy = st.builds(
    ecoreDiff::DeletedEDataType,
)
ecoreDiff::ChangedEDataType_strategy = st.builds(
    ecoreDiff::ChangedEDataType,
)
ecoreDiff::EEnum_strategy = st.builds(
    ecoreDiff::EEnum,
)
ecoreDiff::EReference_strategy = st.builds(
    ecoreDiff::EReference,
    resolveProxies=
        st.booleans(),
    containment=
        st.booleans()
)
ecoreDiff::EStructuralFeature::Wildcard_strategy = st.builds(
    ecoreDiff::EStructuralFeature::Wildcard,
)
EObject_strategy = st.builds(
    EObject,
)
ecoreDiff::ChangedEObject_strategy = st.builds(
    ecoreDiff::ChangedEObject,
)
ecoreDiff::DeletedEObject_strategy = st.builds(
    ecoreDiff::DeletedEObject,
)
ecoreDiff::AddedEObject_strategy = st.builds(
    ecoreDiff::AddedEObject,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
ecoreDiff::EParameter_strategy = st.builds(
    ecoreDiff::EParameter,
)
ecoreDiff::EClassifier::Wildcard_strategy = st.builds(
    ecoreDiff::EClassifier::Wildcard,
)
ecoreDiff::EGenericType_strategy = st.builds(
    ecoreDiff::EGenericType,
)
ecoreDiff::EStructuralFeature_strategy = st.builds(
    ecoreDiff::EStructuralFeature,
    transient=
        st.booleans(),
    changeable=
        st.booleans(),
    defaultValueLiteral=
        safe_text,
    volatile=
        st.booleans(),
    unsettable=
        st.booleans(),
    derived=
        st.booleans()
)
ecoreDiff::EOperation_strategy = st.builds(
    ecoreDiff::EOperation,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ecoreDiff::ETypeParameter_strategy = st.builds(
    ecoreDiff::ETypeParameter,
)
ecoreDiff::AddedENamedElement_strategy = st.builds(
    ecoreDiff::AddedENamedElement,
)
ecoreDiff::EEnumLiteral_strategy = st.builds(
    ecoreDiff::EEnumLiteral,
    value=
        st.integers(),
    instance=
        safe_text,
    literal=
        safe_text
)
ecoreDiff::ETypedElement_strategy = st.builds(
    ecoreDiff::ETypedElement,
    ordered=
        st.booleans(),
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    unique=
        st.booleans()
)
ecoreDiff::EPackage_strategy = st.builds(
    ecoreDiff::EPackage,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
ecoreDiff::ChangedENamedElement_strategy = st.builds(
    ecoreDiff::ChangedENamedElement,
)
ecoreDiff::DeletedENamedElement_strategy = st.builds(
    ecoreDiff::DeletedENamedElement,
)
ecoreDiff::EClassifier_strategy = st.builds(
    ecoreDiff::EClassifier,
    instanceClassName=
        safe_text,
    instanceTypeName=
        safe_text
)
EClassifier_strategy = st.builds(
    EClassifier,
)
ecoreDiff::DeletedEClassifier_strategy = st.builds(
    ecoreDiff::DeletedEClassifier,
)
ecoreDiff::ChangedEClassifier_strategy = st.builds(
    ecoreDiff::ChangedEClassifier,
)
ecoreDiff::EDataType_strategy = st.builds(
    ecoreDiff::EDataType,
    serializable=
        st.booleans()
)
ecoreDiff::AddedEClassifier_strategy = st.builds(
    ecoreDiff::AddedEClassifier,
)
ecoreDiff::EClass_strategy = st.builds(
    ecoreDiff::EClass,
    interface=
        st.booleans(),
    abstract=
        st.booleans()
)
ecoreDiff::EObject_strategy = st.builds(
    ecoreDiff::EObject,
)
ecoreDiff::EModelElement_strategy = st.builds(
    ecoreDiff::EModelElement,
)
ecoreDiff::EStringToStringMapEntry_strategy = st.builds(
    ecoreDiff::EStringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
EModelElement_strategy = st.builds(
    EModelElement,
)
ecoreDiff::EFactory_strategy = st.builds(
    ecoreDiff::EFactory,
)
ecoreDiff::ENamedElement_strategy = st.builds(
    ecoreDiff::ENamedElement,
    name=
        safe_text
)
ecoreDiff::EAnnotation_strategy = st.builds(
    ecoreDiff::EAnnotation,
    source=
        safe_text
)
ecoreDiff::ChangedEModelElement_strategy = st.builds(
    ecoreDiff::ChangedEModelElement,
)
ecoreDiff::DeletedEModelElement_strategy = st.builds(
    ecoreDiff::DeletedEModelElement,
)
ecoreDiff::AddedEModelElement_strategy = st.builds(
    ecoreDiff::AddedEModelElement,
)
EEnumLiteral_strategy = st.builds(
    EEnumLiteral,
)
ecoreDiff::DeletedEEnumLiteral_strategy = st.builds(
    ecoreDiff::DeletedEEnumLiteral,
)
ecoreDiff::ChangedEEnumLiteral_strategy = st.builds(
    ecoreDiff::ChangedEEnumLiteral,
)
ecoreDiff::AddedEEnumLiteral_strategy = st.builds(
    ecoreDiff::AddedEEnumLiteral,
)
EStructuralFeature::Wildcard_strategy = st.builds(
    EStructuralFeature::Wildcard,
)
ecoreDiff::AddedEStructuralFeature::Wildcard_strategy = st.builds(
    ecoreDiff::AddedEStructuralFeature::Wildcard,
)
EEnum_strategy = st.builds(
    EEnum,
)
ecoreDiff::DeletedEEnum_strategy = st.builds(
    ecoreDiff::DeletedEEnum,
)
ecoreDiff::ChangedEEnum_strategy = st.builds(
    ecoreDiff::ChangedEEnum,
)
ecoreDiff::AddedEEnum_strategy = st.builds(
    ecoreDiff::AddedEEnum,
)
EReference_strategy = st.builds(
    EReference,
)
ecoreDiff::ChangedEReference_strategy = st.builds(
    ecoreDiff::ChangedEReference,
)
ecoreDiff::DeletedEReference_strategy = st.builds(
    ecoreDiff::DeletedEReference,
)
ecoreDiff::AddedEReference_strategy = st.builds(
    ecoreDiff::AddedEReference,
)
ecoreDiff::ChangedEStructuralFeature::Wildcard_strategy = st.builds(
    ecoreDiff::ChangedEStructuralFeature::Wildcard,
)
ecoreDiff::DeletedEStructuralFeature::Wildcard_strategy = st.builds(
    ecoreDiff::DeletedEStructuralFeature::Wildcard,
)
ecoreDiff::ChangedEStructuralFeature_strategy = st.builds(
    ecoreDiff::ChangedEStructuralFeature,
)
ecoreDiff::DeletedEStructuralFeature_strategy = st.builds(
    ecoreDiff::DeletedEStructuralFeature,
)
ecoreDiff::AddedEStructuralFeature_strategy = st.builds(
    ecoreDiff::AddedEStructuralFeature,
)
EParameter_strategy = st.builds(
    EParameter,
)
ecoreDiff::ChangedEParameter_strategy = st.builds(
    ecoreDiff::ChangedEParameter,
)
ecoreDiff::DeletedEParameter_strategy = st.builds(
    ecoreDiff::DeletedEParameter,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
ecoreDiff::DeletedEAttribute_strategy = st.builds(
    ecoreDiff::DeletedEAttribute,
)
ecoreDiff::ChangedEAttribute_strategy = st.builds(
    ecoreDiff::ChangedEAttribute,
)
ecoreDiff::AddedEAttribute_strategy = st.builds(
    ecoreDiff::AddedEAttribute,
)
EClassifier::Wildcard_strategy = st.builds(
    EClassifier::Wildcard,
)
ecoreDiff::ChangedEClassifier::Wildcard_strategy = st.builds(
    ecoreDiff::ChangedEClassifier::Wildcard,
)
ecoreDiff::DeletedEClassifier::Wildcard_strategy = st.builds(
    ecoreDiff::DeletedEClassifier::Wildcard,
)
ecoreDiff::AddedEClassifier::Wildcard_strategy = st.builds(
    ecoreDiff::AddedEClassifier::Wildcard,
)
ecoreDiff::ChangedEGenericType_strategy = st.builds(
    ecoreDiff::ChangedEGenericType,
)
ecoreDiff::DeletedEGenericType_strategy = st.builds(
    ecoreDiff::DeletedEGenericType,
)
ecoreDiff::AddedEParameter_strategy = st.builds(
    ecoreDiff::AddedEParameter,
)
ecoreDiff::ChangedETypedElement_strategy = st.builds(
    ecoreDiff::ChangedETypedElement,
)
ecoreDiff::DeletedETypedElement_strategy = st.builds(
    ecoreDiff::DeletedETypedElement,
)
ecoreDiff::AddedETypedElement_strategy = st.builds(
    ecoreDiff::AddedETypedElement,
)
EOperation_strategy = st.builds(
    EOperation,
)
ecoreDiff::DeletedEOperation_strategy = st.builds(
    ecoreDiff::DeletedEOperation,
)
ecoreDiff::ChangedEOperation_strategy = st.builds(
    ecoreDiff::ChangedEOperation,
)
ecoreDiff::AddedEOperation_strategy = st.builds(
    ecoreDiff::AddedEOperation,
)
ecoreDiff::AddedEDataType_strategy = st.builds(
    ecoreDiff::AddedEDataType,
)
EFactory_strategy = st.builds(
    EFactory,
)
ecoreDiff::DeletedEFactory_strategy = st.builds(
    ecoreDiff::DeletedEFactory,
)
ecoreDiff::ChangedEFactory_strategy = st.builds(
    ecoreDiff::ChangedEFactory,
)
ecoreDiff::AddedEFactory_strategy = st.builds(
    ecoreDiff::AddedEFactory,
)

@given(instance=EGenericType_strategy)
@settings(max_examples=50)
def test_egenerictype_instantiation(instance):
    assert isinstance(instance, EGenericType)

@given(instance=ecoreDiff::AddedEGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff::addedegenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEGenericType)

@given(instance=ETypeParameter_strategy)
@settings(max_examples=50)
def test_etypeparameter_instantiation(instance):
    assert isinstance(instance, ETypeParameter)

@given(instance=ecoreDiff::ChangedETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::changedetypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedETypeParameter)

@given(instance=ecoreDiff::DeletedETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedetypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedETypeParameter)

@given(instance=ecoreDiff::AddedETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::addedetypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedETypeParameter)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=ecoreDiff::ChangedEPackage_strategy)
@settings(max_examples=50)
def test_ecorediff::changedepackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEPackage)

@given(instance=ecoreDiff::DeletedEPackage_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedepackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEPackage)

@given(instance=ecoreDiff::AddedEPackage_strategy)
@settings(max_examples=50)
def test_ecorediff::addedepackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEPackage)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=ecoreDiff::AddedEClass_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEClass)

@given(instance=ecoreDiff::ChangedEClass_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEClass)

@given(instance=ecoreDiff::DeletedEClass_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEClass)

@given(instance=EAnnotation_strategy)
@settings(max_examples=50)
def test_eannotation_instantiation(instance):
    assert isinstance(instance, EAnnotation)

@given(instance=ecoreDiff::AddedEAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEAnnotation)

@given(instance=ecoreDiff::DifferenceElement_strategy)
@settings(max_examples=50)
def test_ecorediff::differenceelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DifferenceElement)

@given(instance=ecoreDiff::DifferenceModel_strategy)
@settings(max_examples=50)
def test_ecorediff::differencemodel_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DifferenceModel)

@given(instance=DifferenceElement_strategy)
@settings(max_examples=50)
def test_differenceelement_instantiation(instance):
    assert isinstance(instance, DifferenceElement)

@given(instance=EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, EStringToStringMapEntry)

@given(instance=ecoreDiff::DeletedEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEStringToStringMapEntry)

@given(instance=ecoreDiff::ChangedEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff::changedestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEStringToStringMapEntry)

@given(instance=ecoreDiff::AddedEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff::addedestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEStringToStringMapEntry)

@given(instance=ecoreDiff::ChangedEAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEAnnotation)

@given(instance=ecoreDiff::DeletedEAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEAnnotation)

@given(instance=EStructuralFeature_strategy)
@settings(max_examples=50)
def test_estructuralfeature_instantiation(instance):
    assert isinstance(instance, EStructuralFeature)

@given(instance=ecoreDiff::EAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff::eattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EAttribute)

@given(instance=ecoreDiff::EAttribute_strategy)
def test_ecorediff::eattribute_iD_type(instance):
    assert isinstance(instance.iD, bool)


@given(instance=ecoreDiff::EAttribute_strategy)
def test_ecorediff::eattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=ecoreDiff::DeletedEDataType_strategy)
@settings(max_examples=50)
def test_ecorediff::deletededatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEDataType)

@given(instance=ecoreDiff::ChangedEDataType_strategy)
@settings(max_examples=50)
def test_ecorediff::changededatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEDataType)

@given(instance=ecoreDiff::EEnum_strategy)
@settings(max_examples=50)
def test_ecorediff::eenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EEnum)

@given(instance=ecoreDiff::EReference_strategy)
@settings(max_examples=50)
def test_ecorediff::ereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EReference)

@given(instance=ecoreDiff::EReference_strategy)
def test_ecorediff::ereference_resolveProxies_type(instance):
    assert isinstance(instance.resolveProxies, bool)


@given(instance=ecoreDiff::EReference_strategy)
def test_ecorediff::ereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original

@given(instance=ecoreDiff::EReference_strategy)
def test_ecorediff::ereference_containment_type(instance):
    assert isinstance(instance.containment, bool)


@given(instance=ecoreDiff::EReference_strategy)
def test_ecorediff::ereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original

@given(instance=ecoreDiff::EStructuralFeature::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::estructuralfeature::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EStructuralFeature::Wildcard)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=ecoreDiff::ChangedEObject_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEObject)

@given(instance=ecoreDiff::DeletedEObject_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEObject)

@given(instance=ecoreDiff::AddedEObject_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEObject)

@given(instance=ETypedElement_strategy)
@settings(max_examples=50)
def test_etypedelement_instantiation(instance):
    assert isinstance(instance, ETypedElement)

@given(instance=ecoreDiff::EParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::eparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EParameter)

@given(instance=ecoreDiff::EClassifier::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::eclassifier::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EClassifier::Wildcard)

@given(instance=ecoreDiff::EGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff::egenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EGenericType)

@given(instance=ecoreDiff::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff::estructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EStructuralFeature)

@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_defaultValueLiteral_type(instance):
    assert isinstance(instance.defaultValueLiteral, str)


@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original

@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_volatile_type(instance):
    assert isinstance(instance.volatile, bool)


@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_unsettable_type(instance):
    assert isinstance(instance.unsettable, bool)


@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original

@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=ecoreDiff::EStructuralFeature_strategy)
def test_ecorediff::estructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=ecoreDiff::EOperation_strategy)
@settings(max_examples=50)
def test_ecorediff::eoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EOperation)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ecoreDiff::ETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::etypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ETypeParameter)

@given(instance=ecoreDiff::AddedENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::addedenamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedENamedElement)

@given(instance=ecoreDiff::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff::eenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EEnumLiteral)

@given(instance=ecoreDiff::EEnumLiteral_strategy)
def test_ecorediff::eenumliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ecoreDiff::EEnumLiteral_strategy)
def test_ecorediff::eenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecoreDiff::EEnumLiteral_strategy)
def test_ecorediff::eenumliteral_instance_type(instance):
    assert isinstance(instance.instance, str)


@given(instance=ecoreDiff::EEnumLiteral_strategy)
def test_ecorediff::eenumliteral_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original

@given(instance=ecoreDiff::EEnumLiteral_strategy)
def test_ecorediff::eenumliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=ecoreDiff::EEnumLiteral_strategy)
def test_ecorediff::eenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=ecoreDiff::ETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::etypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ETypedElement)

@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=ecoreDiff::ETypedElement_strategy)
def test_ecorediff::etypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=ecoreDiff::EPackage_strategy)
@settings(max_examples=50)
def test_ecorediff::epackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EPackage)

@given(instance=ecoreDiff::EPackage_strategy)
def test_ecorediff::epackage_nsURI_type(instance):
    assert isinstance(instance.nsURI, str)


@given(instance=ecoreDiff::EPackage_strategy)
def test_ecorediff::epackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

@given(instance=ecoreDiff::EPackage_strategy)
def test_ecorediff::epackage_nsPrefix_type(instance):
    assert isinstance(instance.nsPrefix, str)


@given(instance=ecoreDiff::EPackage_strategy)
def test_ecorediff::epackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=ecoreDiff::ChangedENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::changedenamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedENamedElement)

@given(instance=ecoreDiff::DeletedENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedenamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedENamedElement)

@given(instance=ecoreDiff::EClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff::eclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EClassifier)

@given(instance=ecoreDiff::EClassifier_strategy)
def test_ecorediff::eclassifier_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=ecoreDiff::EClassifier_strategy)
def test_ecorediff::eclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=ecoreDiff::EClassifier_strategy)
def test_ecorediff::eclassifier_instanceTypeName_type(instance):
    assert isinstance(instance.instanceTypeName, str)


@given(instance=ecoreDiff::EClassifier_strategy)
def test_ecorediff::eclassifier_instanceTypeName_setter(instance):
    original = instance.instanceTypeName
    instance.instanceTypeName = original
    assert instance.instanceTypeName == original

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=ecoreDiff::DeletedEClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEClassifier)

@given(instance=ecoreDiff::ChangedEClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEClassifier)

@given(instance=ecoreDiff::EDataType_strategy)
@settings(max_examples=50)
def test_ecorediff::edatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EDataType)

@given(instance=ecoreDiff::EDataType_strategy)
def test_ecorediff::edatatype_serializable_type(instance):
    assert isinstance(instance.serializable, bool)


@given(instance=ecoreDiff::EDataType_strategy)
def test_ecorediff::edatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original

@given(instance=ecoreDiff::AddedEClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEClassifier)

@given(instance=ecoreDiff::EClass_strategy)
@settings(max_examples=50)
def test_ecorediff::eclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EClass)

@given(instance=ecoreDiff::EClass_strategy)
def test_ecorediff::eclass_interface_type(instance):
    assert isinstance(instance.interface, bool)


@given(instance=ecoreDiff::EClass_strategy)
def test_ecorediff::eclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=ecoreDiff::EClass_strategy)
def test_ecorediff::eclass_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=ecoreDiff::EClass_strategy)
def test_ecorediff::eclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ecoreDiff::EObject_strategy)
@settings(max_examples=50)
def test_ecorediff::eobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EObject)

@given(instance=ecoreDiff::EModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff::emodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EModelElement)

@given(instance=ecoreDiff::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EStringToStringMapEntry)

@given(instance=ecoreDiff::EStringToStringMapEntry_strategy)
def test_ecorediff::estringtostringmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ecoreDiff::EStringToStringMapEntry_strategy)
def test_ecorediff::estringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ecoreDiff::EStringToStringMapEntry_strategy)
def test_ecorediff::estringtostringmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ecoreDiff::EStringToStringMapEntry_strategy)
def test_ecorediff::estringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=ecoreDiff::EFactory_strategy)
@settings(max_examples=50)
def test_ecorediff::efactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EFactory)

@given(instance=ecoreDiff::ENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::enamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ENamedElement)

@given(instance=ecoreDiff::ENamedElement_strategy)
def test_ecorediff::enamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecoreDiff::ENamedElement_strategy)
def test_ecorediff::enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecoreDiff::EAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff::eannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::EAnnotation)

@given(instance=ecoreDiff::EAnnotation_strategy)
def test_ecorediff::eannotation_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=ecoreDiff::EAnnotation_strategy)
def test_ecorediff::eannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=ecoreDiff::ChangedEModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff::changedemodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEModelElement)

@given(instance=ecoreDiff::DeletedEModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedemodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEModelElement)

@given(instance=ecoreDiff::AddedEModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff::addedemodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEModelElement)

@given(instance=EEnumLiteral_strategy)
@settings(max_examples=50)
def test_eenumliteral_instantiation(instance):
    assert isinstance(instance, EEnumLiteral)

@given(instance=ecoreDiff::DeletedEEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEEnumLiteral)

@given(instance=ecoreDiff::ChangedEEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEEnumLiteral)

@given(instance=ecoreDiff::AddedEEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEEnumLiteral)

@given(instance=EStructuralFeature::Wildcard_strategy)
@settings(max_examples=50)
def test_estructuralfeature::wildcard_instantiation(instance):
    assert isinstance(instance, EStructuralFeature::Wildcard)

@given(instance=ecoreDiff::AddedEStructuralFeature::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::addedestructuralfeature::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEStructuralFeature::Wildcard)

@given(instance=EEnum_strategy)
@settings(max_examples=50)
def test_eenum_instantiation(instance):
    assert isinstance(instance, EEnum)

@given(instance=ecoreDiff::DeletedEEnum_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEEnum)

@given(instance=ecoreDiff::ChangedEEnum_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEEnum)

@given(instance=ecoreDiff::AddedEEnum_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEEnum)

@given(instance=EReference_strategy)
@settings(max_examples=50)
def test_ereference_instantiation(instance):
    assert isinstance(instance, EReference)

@given(instance=ecoreDiff::ChangedEReference_strategy)
@settings(max_examples=50)
def test_ecorediff::changedereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEReference)

@given(instance=ecoreDiff::DeletedEReference_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEReference)

@given(instance=ecoreDiff::AddedEReference_strategy)
@settings(max_examples=50)
def test_ecorediff::addedereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEReference)

@given(instance=ecoreDiff::ChangedEStructuralFeature::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::changedestructuralfeature::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEStructuralFeature::Wildcard)

@given(instance=ecoreDiff::DeletedEStructuralFeature::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedestructuralfeature::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEStructuralFeature::Wildcard)

@given(instance=ecoreDiff::ChangedEStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff::changedestructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEStructuralFeature)

@given(instance=ecoreDiff::DeletedEStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedestructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEStructuralFeature)

@given(instance=ecoreDiff::AddedEStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff::addedestructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEStructuralFeature)

@given(instance=EParameter_strategy)
@settings(max_examples=50)
def test_eparameter_instantiation(instance):
    assert isinstance(instance, EParameter)

@given(instance=ecoreDiff::ChangedEParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEParameter)

@given(instance=ecoreDiff::DeletedEParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEParameter)

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=ecoreDiff::DeletedEAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEAttribute)

@given(instance=ecoreDiff::ChangedEAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEAttribute)

@given(instance=ecoreDiff::AddedEAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEAttribute)

@given(instance=EClassifier::Wildcard_strategy)
@settings(max_examples=50)
def test_eclassifier::wildcard_instantiation(instance):
    assert isinstance(instance, EClassifier::Wildcard)

@given(instance=ecoreDiff::ChangedEClassifier::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeclassifier::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEClassifier::Wildcard)

@given(instance=ecoreDiff::DeletedEClassifier::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeclassifier::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEClassifier::Wildcard)

@given(instance=ecoreDiff::AddedEClassifier::Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeclassifier::wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEClassifier::Wildcard)

@given(instance=ecoreDiff::ChangedEGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff::changedegenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEGenericType)

@given(instance=ecoreDiff::DeletedEGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedegenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEGenericType)

@given(instance=ecoreDiff::AddedEParameter_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEParameter)

@given(instance=ecoreDiff::ChangedETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::changedetypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedETypedElement)

@given(instance=ecoreDiff::DeletedETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedetypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedETypedElement)

@given(instance=ecoreDiff::AddedETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff::addedetypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedETypedElement)

@given(instance=EOperation_strategy)
@settings(max_examples=50)
def test_eoperation_instantiation(instance):
    assert isinstance(instance, EOperation)

@given(instance=ecoreDiff::DeletedEOperation_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedeoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEOperation)

@given(instance=ecoreDiff::ChangedEOperation_strategy)
@settings(max_examples=50)
def test_ecorediff::changedeoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEOperation)

@given(instance=ecoreDiff::AddedEOperation_strategy)
@settings(max_examples=50)
def test_ecorediff::addedeoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEOperation)

@given(instance=ecoreDiff::AddedEDataType_strategy)
@settings(max_examples=50)
def test_ecorediff::addededatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEDataType)

@given(instance=EFactory_strategy)
@settings(max_examples=50)
def test_efactory_instantiation(instance):
    assert isinstance(instance, EFactory)

@given(instance=ecoreDiff::DeletedEFactory_strategy)
@settings(max_examples=50)
def test_ecorediff::deletedefactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff::DeletedEFactory)

@given(instance=ecoreDiff::ChangedEFactory_strategy)
@settings(max_examples=50)
def test_ecorediff::changedefactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff::ChangedEFactory)

@given(instance=ecoreDiff::AddedEFactory_strategy)
@settings(max_examples=50)
def test_ecorediff::addedefactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff::AddedEFactory)
