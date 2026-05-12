import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EReference,
    ecoreDiff_DeletedEReference,
    ecoreDiff_AddedEReference,
    EStructuralFeature_Wildcard,
    ecoreDiff_DeletedEStructuralFeature_Wildcard,
    ecoreDiff_ChangedEStructuralFeature_Wildcard,
    ecoreDiff_AddedEStructuralFeature_Wildcard,
    EAttribute,
    ecoreDiff_ChangedEAttribute,
    ecoreDiff_DeletedEAttribute,
    ecoreDiff_AddedEAttribute,
    EEnumLiteral,
    ecoreDiff_DeletedEEnumLiteral,
    ecoreDiff_ChangedEEnumLiteral,
    ecoreDiff_AddedEEnumLiteral,
    EEnum,
    ecoreDiff_DeletedEEnum,
    ecoreDiff_ChangedEEnum,
    ecoreDiff_AddedEEnum,
    ecoreDiff_ChangedEReference,
    EOperation,
    ecoreDiff_ChangedEOperation,
    ecoreDiff_DeletedEOperation,
    ecoreDiff_AddedEOperation,
    EClassifier_Wildcard,
    ecoreDiff_ChangedEClassifier_Wildcard,
    ecoreDiff_DeletedEClassifier_Wildcard,
    ecoreDiff_AddedEClassifier_Wildcard,
    EParameter,
    ecoreDiff_DeletedEParameter,
    ecoreDiff_ChangedEParameter,
    ecoreDiff_AddedEParameter,
    EFactory,
    ecoreDiff_ChangedEFactory,
    ecoreDiff_DeletedEFactory,
    ecoreDiff_AddedEFactory,
    EPackage,
    ecoreDiff_ChangedEPackage,
    ecoreDiff_DeletedEPackage,
    ecoreDiff_AddedEPackage,
    EGenericType,
    ecoreDiff_DeletedEGenericType,
    ecoreDiff_ChangedEGenericType,
    ecoreDiff_AddedEGenericType,
    ETypeParameter,
    ecoreDiff_DeletedETypeParameter,
    ecoreDiff_ChangedETypeParameter,
    ecoreDiff_AddedETypeParameter,
    EClass,
    ecoreDiff_ChangedEClass,
    ecoreDiff_DeletedEClass,
    ecoreDiff_AddedEClass,
    EStringToStringMapEntry,
    ecoreDiff_DeletedEStringToStringMapEntry,
    ecoreDiff_ChangedEStringToStringMapEntry,
    ecoreDiff_AddedEStringToStringMapEntry,
    EAnnotation,
    ecoreDiff_DeletedEAnnotation,
    ecoreDiff_ChangedEAnnotation,
    ecoreDiff_AddedEAnnotation,
    ecoreDiff_DifferenceElement,
    ecoreDiff_DifferenceModel,
    DifferenceElement,
    EDataType,
    ecoreDiff_AddedEDataType,
    ecoreDiff_DeletedEDataType,
    ecoreDiff_ChangedEDataType,
    ecoreDiff_EEnum,
    ecoreDiff_EStructuralFeature_Wildcard,
    EStructuralFeature,
    ecoreDiff_DeletedEStructuralFeature,
    ecoreDiff_AddedEStructuralFeature,
    ecoreDiff_ChangedEStructuralFeature,
    EObject,
    ecoreDiff_AddedEObject,
    ecoreDiff_DeletedEObject,
    ecoreDiff_ChangedEObject,
    ETypedElement,
    ecoreDiff_DeletedETypedElement,
    ecoreDiff_EParameter,
    ecoreDiff_AddedETypedElement,
    ecoreDiff_ChangedETypedElement,
    ecoreDiff_EClassifier_Wildcard,
    ENamedElement,
    ecoreDiff_ETypedElement,
    ecoreDiff_DeletedENamedElement,
    ecoreDiff_EEnumLiteral,
    ecoreDiff_ETypeParameter,
    ecoreDiff_EPackage,
    ecoreDiff_AddedENamedElement,
    ecoreDiff_ChangedENamedElement,
    ecoreDiff_EClassifier,
    ecoreDiff_EGenericType,
    ecoreDiff_EReference,
    ecoreDiff_EStructuralFeature,
    ecoreDiff_EAttribute,
    ecoreDiff_EOperation,
    EClassifier,
    ecoreDiff_AddedEClassifier,
    ecoreDiff_EDataType,
    ecoreDiff_ChangedEClassifier,
    ecoreDiff_DeletedEClassifier,
    ecoreDiff_EClass,
    EModelElement,
    ecoreDiff_ENamedElement,
    ecoreDiff_DeletedEModelElement,
    ecoreDiff_EFactory,
    ecoreDiff_ChangedEModelElement,
    ecoreDiff_AddedEModelElement,
    ecoreDiff_EAnnotation,
    ecoreDiff_EObject,
    ecoreDiff_EModelElement,
    ecoreDiff_EStringToStringMapEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ereference_is_not_abstract():
    assert not inspect.isabstract(EReference)


def test_ereference_constructor_exists():
    assert callable(EReference.__init__)


def test_ereference_constructor_args():
    sig = inspect.signature(EReference.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEReference)


def test_ecorediff_deletedereference_constructor_exists():
    assert callable(ecoreDiff_DeletedEReference.__init__)


def test_ecorediff_deletedereference_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEReference.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEReference)


def test_ecorediff_addedereference_constructor_exists():
    assert callable(ecoreDiff_AddedEReference.__init__)


def test_ecorediff_addedereference_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEReference.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeature_wildcard_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature_Wildcard)


def test_estructuralfeature_wildcard_constructor_exists():
    assert callable(EStructuralFeature_Wildcard.__init__)


def test_estructuralfeature_wildcard_constructor_args():
    sig = inspect.signature(EStructuralFeature_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedestructuralfeature_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEStructuralFeature_Wildcard)


def test_ecorediff_deletedestructuralfeature_wildcard_constructor_exists():
    assert callable(ecoreDiff_DeletedEStructuralFeature_Wildcard.__init__)


def test_ecorediff_deletedestructuralfeature_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEStructuralFeature_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedestructuralfeature_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEStructuralFeature_Wildcard)


def test_ecorediff_changedestructuralfeature_wildcard_constructor_exists():
    assert callable(ecoreDiff_ChangedEStructuralFeature_Wildcard.__init__)


def test_ecorediff_changedestructuralfeature_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEStructuralFeature_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedestructuralfeature_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEStructuralFeature_Wildcard)


def test_ecorediff_addedestructuralfeature_wildcard_constructor_exists():
    assert callable(ecoreDiff_AddedEStructuralFeature_Wildcard.__init__)


def test_ecorediff_addedestructuralfeature_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEStructuralFeature_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEAttribute)


def test_ecorediff_changedeattribute_constructor_exists():
    assert callable(ecoreDiff_ChangedEAttribute.__init__)


def test_ecorediff_changedeattribute_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEAttribute)


def test_ecorediff_deletedeattribute_constructor_exists():
    assert callable(ecoreDiff_DeletedEAttribute.__init__)


def test_ecorediff_deletedeattribute_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEAttribute)


def test_ecorediff_addedeattribute_constructor_exists():
    assert callable(ecoreDiff_AddedEAttribute.__init__)


def test_ecorediff_addedeattribute_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(EEnumLiteral)


def test_eenumliteral_constructor_exists():
    assert callable(EEnumLiteral.__init__)


def test_eenumliteral_constructor_args():
    sig = inspect.signature(EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEEnumLiteral)


def test_ecorediff_deletedeenumliteral_constructor_exists():
    assert callable(ecoreDiff_DeletedEEnumLiteral.__init__)


def test_ecorediff_deletedeenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEEnumLiteral)


def test_ecorediff_changedeenumliteral_constructor_exists():
    assert callable(ecoreDiff_ChangedEEnumLiteral.__init__)


def test_ecorediff_changedeenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEEnumLiteral)


def test_ecorediff_addedeenumliteral_constructor_exists():
    assert callable(ecoreDiff_AddedEEnumLiteral.__init__)


def test_ecorediff_addedeenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_eenum_is_not_abstract():
    assert not inspect.isabstract(EEnum)


def test_eenum_constructor_exists():
    assert callable(EEnum.__init__)


def test_eenum_constructor_args():
    sig = inspect.signature(EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEEnum)


def test_ecorediff_deletedeenum_constructor_exists():
    assert callable(ecoreDiff_DeletedEEnum.__init__)


def test_ecorediff_deletedeenum_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEEnum)


def test_ecorediff_changedeenum_constructor_exists():
    assert callable(ecoreDiff_ChangedEEnum.__init__)


def test_ecorediff_changedeenum_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEEnum)


def test_ecorediff_addedeenum_constructor_exists():
    assert callable(ecoreDiff_AddedEEnum.__init__)


def test_ecorediff_addedeenum_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEReference)


def test_ecorediff_changedereference_constructor_exists():
    assert callable(ecoreDiff_ChangedEReference.__init__)


def test_ecorediff_changedereference_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEReference.__init__)
    params = list(sig.parameters.keys())



def test_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEOperation)


def test_ecorediff_changedeoperation_constructor_exists():
    assert callable(ecoreDiff_ChangedEOperation.__init__)


def test_ecorediff_changedeoperation_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEOperation)


def test_ecorediff_deletedeoperation_constructor_exists():
    assert callable(ecoreDiff_DeletedEOperation.__init__)


def test_ecorediff_deletedeoperation_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEOperation)


def test_ecorediff_addedeoperation_constructor_exists():
    assert callable(ecoreDiff_AddedEOperation.__init__)


def test_ecorediff_addedeoperation_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEOperation.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier_wildcard_is_not_abstract():
    assert not inspect.isabstract(EClassifier_Wildcard)


def test_eclassifier_wildcard_constructor_exists():
    assert callable(EClassifier_Wildcard.__init__)


def test_eclassifier_wildcard_constructor_args():
    sig = inspect.signature(EClassifier_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeclassifier_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEClassifier_Wildcard)


def test_ecorediff_changedeclassifier_wildcard_constructor_exists():
    assert callable(ecoreDiff_ChangedEClassifier_Wildcard.__init__)


def test_ecorediff_changedeclassifier_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEClassifier_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeclassifier_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEClassifier_Wildcard)


def test_ecorediff_deletedeclassifier_wildcard_constructor_exists():
    assert callable(ecoreDiff_DeletedEClassifier_Wildcard.__init__)


def test_ecorediff_deletedeclassifier_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEClassifier_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeclassifier_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEClassifier_Wildcard)


def test_ecorediff_addedeclassifier_wildcard_constructor_exists():
    assert callable(ecoreDiff_AddedEClassifier_Wildcard.__init__)


def test_ecorediff_addedeclassifier_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEClassifier_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_eparameter_is_not_abstract():
    assert not inspect.isabstract(EParameter)


def test_eparameter_constructor_exists():
    assert callable(EParameter.__init__)


def test_eparameter_constructor_args():
    sig = inspect.signature(EParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEParameter)


def test_ecorediff_deletedeparameter_constructor_exists():
    assert callable(ecoreDiff_DeletedEParameter.__init__)


def test_ecorediff_deletedeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEParameter)


def test_ecorediff_changedeparameter_constructor_exists():
    assert callable(ecoreDiff_ChangedEParameter.__init__)


def test_ecorediff_changedeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEParameter)


def test_ecorediff_addedeparameter_constructor_exists():
    assert callable(ecoreDiff_AddedEParameter.__init__)


def test_ecorediff_addedeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEParameter.__init__)
    params = list(sig.parameters.keys())



def test_efactory_is_not_abstract():
    assert not inspect.isabstract(EFactory)


def test_efactory_constructor_exists():
    assert callable(EFactory.__init__)


def test_efactory_constructor_args():
    sig = inspect.signature(EFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedefactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEFactory)


def test_ecorediff_changedefactory_constructor_exists():
    assert callable(ecoreDiff_ChangedEFactory.__init__)


def test_ecorediff_changedefactory_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedefactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEFactory)


def test_ecorediff_deletedefactory_constructor_exists():
    assert callable(ecoreDiff_DeletedEFactory.__init__)


def test_ecorediff_deletedefactory_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedefactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEFactory)


def test_ecorediff_addedefactory_constructor_exists():
    assert callable(ecoreDiff_AddedEFactory.__init__)


def test_ecorediff_addedefactory_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEFactory.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedepackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEPackage)


def test_ecorediff_changedepackage_constructor_exists():
    assert callable(ecoreDiff_ChangedEPackage.__init__)


def test_ecorediff_changedepackage_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedepackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEPackage)


def test_ecorediff_deletedepackage_constructor_exists():
    assert callable(ecoreDiff_DeletedEPackage.__init__)


def test_ecorediff_deletedepackage_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedepackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEPackage)


def test_ecorediff_addedepackage_constructor_exists():
    assert callable(ecoreDiff_AddedEPackage.__init__)


def test_ecorediff_addedepackage_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEPackage.__init__)
    params = list(sig.parameters.keys())



def test_egenerictype_is_not_abstract():
    assert not inspect.isabstract(EGenericType)


def test_egenerictype_constructor_exists():
    assert callable(EGenericType.__init__)


def test_egenerictype_constructor_args():
    sig = inspect.signature(EGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedegenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEGenericType)


def test_ecorediff_deletedegenerictype_constructor_exists():
    assert callable(ecoreDiff_DeletedEGenericType.__init__)


def test_ecorediff_deletedegenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedegenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEGenericType)


def test_ecorediff_changedegenerictype_constructor_exists():
    assert callable(ecoreDiff_ChangedEGenericType.__init__)


def test_ecorediff_changedegenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedegenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEGenericType)


def test_ecorediff_addedegenerictype_constructor_exists():
    assert callable(ecoreDiff_AddedEGenericType.__init__)


def test_ecorediff_addedegenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEGenericType.__init__)
    params = list(sig.parameters.keys())



def test_etypeparameter_is_not_abstract():
    assert not inspect.isabstract(ETypeParameter)


def test_etypeparameter_constructor_exists():
    assert callable(ETypeParameter.__init__)


def test_etypeparameter_constructor_args():
    sig = inspect.signature(ETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedetypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedETypeParameter)


def test_ecorediff_deletedetypeparameter_constructor_exists():
    assert callable(ecoreDiff_DeletedETypeParameter.__init__)


def test_ecorediff_deletedetypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedetypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedETypeParameter)


def test_ecorediff_changedetypeparameter_constructor_exists():
    assert callable(ecoreDiff_ChangedETypeParameter.__init__)


def test_ecorediff_changedetypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedetypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedETypeParameter)


def test_ecorediff_addedetypeparameter_constructor_exists():
    assert callable(ecoreDiff_AddedETypeParameter.__init__)


def test_ecorediff_addedetypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEClass)


def test_ecorediff_changedeclass_constructor_exists():
    assert callable(ecoreDiff_ChangedEClass.__init__)


def test_ecorediff_changedeclass_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEClass.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEClass)


def test_ecorediff_deletedeclass_constructor_exists():
    assert callable(ecoreDiff_DeletedEClass.__init__)


def test_ecorediff_deletedeclass_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEClass.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEClass)


def test_ecorediff_addedeclass_constructor_exists():
    assert callable(ecoreDiff_AddedEClass.__init__)


def test_ecorediff_addedeclass_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEClass.__init__)
    params = list(sig.parameters.keys())



def test_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(EStringToStringMapEntry)


def test_estringtostringmapentry_constructor_exists():
    assert callable(EStringToStringMapEntry.__init__)


def test_estringtostringmapentry_constructor_args():
    sig = inspect.signature(EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEStringToStringMapEntry)


def test_ecorediff_deletedestringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff_DeletedEStringToStringMapEntry.__init__)


def test_ecorediff_deletedestringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEStringToStringMapEntry)


def test_ecorediff_changedestringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff_ChangedEStringToStringMapEntry.__init__)


def test_ecorediff_changedestringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEStringToStringMapEntry)


def test_ecorediff_addedestringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff_AddedEStringToStringMapEntry.__init__)


def test_ecorediff_addedestringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_eannotation_is_not_abstract():
    assert not inspect.isabstract(EAnnotation)


def test_eannotation_constructor_exists():
    assert callable(EAnnotation.__init__)


def test_eannotation_constructor_args():
    sig = inspect.signature(EAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEAnnotation)


def test_ecorediff_deletedeannotation_constructor_exists():
    assert callable(ecoreDiff_DeletedEAnnotation.__init__)


def test_ecorediff_deletedeannotation_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEAnnotation)


def test_ecorediff_changedeannotation_constructor_exists():
    assert callable(ecoreDiff_ChangedEAnnotation.__init__)


def test_ecorediff_changedeannotation_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEAnnotation)


def test_ecorediff_addedeannotation_constructor_exists():
    assert callable(ecoreDiff_AddedEAnnotation.__init__)


def test_ecorediff_addedeannotation_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_differenceelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DifferenceElement)


def test_ecorediff_differenceelement_constructor_exists():
    assert callable(ecoreDiff_DifferenceElement.__init__)


def test_ecorediff_differenceelement_constructor_args():
    sig = inspect.signature(ecoreDiff_DifferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_differencemodel_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DifferenceModel)


def test_ecorediff_differencemodel_constructor_exists():
    assert callable(ecoreDiff_DifferenceModel.__init__)


def test_ecorediff_differencemodel_constructor_args():
    sig = inspect.signature(ecoreDiff_DifferenceModel.__init__)
    params = list(sig.parameters.keys())



def test_differenceelement_is_not_abstract():
    assert not inspect.isabstract(DifferenceElement)


def test_differenceelement_constructor_exists():
    assert callable(DifferenceElement.__init__)


def test_differenceelement_constructor_args():
    sig = inspect.signature(DifferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addededatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEDataType)


def test_ecorediff_addededatatype_constructor_exists():
    assert callable(ecoreDiff_AddedEDataType.__init__)


def test_ecorediff_addededatatype_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletededatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEDataType)


def test_ecorediff_deletededatatype_constructor_exists():
    assert callable(ecoreDiff_DeletedEDataType.__init__)


def test_ecorediff_deletededatatype_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changededatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEDataType)


def test_ecorediff_changededatatype_constructor_exists():
    assert callable(ecoreDiff_ChangedEDataType.__init__)


def test_ecorediff_changededatatype_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEDataType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eenum_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EEnum)


def test_ecorediff_eenum_constructor_exists():
    assert callable(ecoreDiff_EEnum.__init__)


def test_ecorediff_eenum_constructor_args():
    sig = inspect.signature(ecoreDiff_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_estructuralfeature_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EStructuralFeature_Wildcard)


def test_ecorediff_estructuralfeature_wildcard_constructor_exists():
    assert callable(ecoreDiff_EStructuralFeature_Wildcard.__init__)


def test_ecorediff_estructuralfeature_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_EStructuralFeature_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEStructuralFeature)


def test_ecorediff_deletedestructuralfeature_constructor_exists():
    assert callable(ecoreDiff_DeletedEStructuralFeature.__init__)


def test_ecorediff_deletedestructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEStructuralFeature)


def test_ecorediff_addedestructuralfeature_constructor_exists():
    assert callable(ecoreDiff_AddedEStructuralFeature.__init__)


def test_ecorediff_addedestructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEStructuralFeature)


def test_ecorediff_changedestructuralfeature_constructor_exists():
    assert callable(ecoreDiff_ChangedEStructuralFeature.__init__)


def test_ecorediff_changedestructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEObject)


def test_ecorediff_addedeobject_constructor_exists():
    assert callable(ecoreDiff_AddedEObject.__init__)


def test_ecorediff_addedeobject_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEObject)


def test_ecorediff_deletedeobject_constructor_exists():
    assert callable(ecoreDiff_DeletedEObject.__init__)


def test_ecorediff_deletedeobject_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedeobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEObject)


def test_ecorediff_changedeobject_constructor_exists():
    assert callable(ecoreDiff_ChangedEObject.__init__)


def test_ecorediff_changedeobject_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEObject.__init__)
    params = list(sig.parameters.keys())



def test_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedetypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedETypedElement)


def test_ecorediff_deletedetypedelement_constructor_exists():
    assert callable(ecoreDiff_DeletedETypedElement.__init__)


def test_ecorediff_deletedetypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EParameter)


def test_ecorediff_eparameter_constructor_exists():
    assert callable(ecoreDiff_EParameter.__init__)


def test_ecorediff_eparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_EParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedetypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedETypedElement)


def test_ecorediff_addedetypedelement_constructor_exists():
    assert callable(ecoreDiff_AddedETypedElement.__init__)


def test_ecorediff_addedetypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedetypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedETypedElement)


def test_ecorediff_changedetypedelement_constructor_exists():
    assert callable(ecoreDiff_ChangedETypedElement.__init__)


def test_ecorediff_changedetypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eclassifier_wildcard_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EClassifier_Wildcard)


def test_ecorediff_eclassifier_wildcard_constructor_exists():
    assert callable(ecoreDiff_EClassifier_Wildcard.__init__)


def test_ecorediff_eclassifier_wildcard_constructor_args():
    sig = inspect.signature(ecoreDiff_EClassifier_Wildcard.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ETypedElement)


def test_ecorediff_etypedelement_constructor_exists():
    assert callable(ecoreDiff_ETypedElement.__init__)


def test_ecorediff_etypedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_ETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "required" in params, "Missing parameter 'required'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_ecorediff_etypedelement_has_many():
    assert hasattr(ecoreDiff_ETypedElement, "many")
    descriptor = None
    for klass in ecoreDiff_ETypedElement.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_etypedelement_has_lowerBound():
    assert hasattr(ecoreDiff_ETypedElement, "lowerBound")
    descriptor = None
    for klass in ecoreDiff_ETypedElement.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_etypedelement_has_unique():
    assert hasattr(ecoreDiff_ETypedElement, "unique")
    descriptor = None
    for klass in ecoreDiff_ETypedElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_etypedelement_has_required():
    assert hasattr(ecoreDiff_ETypedElement, "required")
    descriptor = None
    for klass in ecoreDiff_ETypedElement.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_etypedelement_has_upperBound():
    assert hasattr(ecoreDiff_ETypedElement, "upperBound")
    descriptor = None
    for klass in ecoreDiff_ETypedElement.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_etypedelement_has_ordered():
    assert hasattr(ecoreDiff_ETypedElement, "ordered")
    descriptor = None
    for klass in ecoreDiff_ETypedElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_deletedenamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedENamedElement)


def test_ecorediff_deletedenamedelement_constructor_exists():
    assert callable(ecoreDiff_DeletedENamedElement.__init__)


def test_ecorediff_deletedenamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EEnumLiteral)


def test_ecorediff_eenumliteral_constructor_exists():
    assert callable(ecoreDiff_EEnumLiteral.__init__)


def test_ecorediff_eenumliteral_constructor_args():
    sig = inspect.signature(ecoreDiff_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "value" in params, "Missing parameter 'value'"

def test_ecorediff_eenumliteral_has_literal():
    assert hasattr(ecoreDiff_EEnumLiteral, "literal")
    descriptor = None
    for klass in ecoreDiff_EEnumLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_eenumliteral_has_instance():
    assert hasattr(ecoreDiff_EEnumLiteral, "instance")
    descriptor = None
    for klass in ecoreDiff_EEnumLiteral.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_eenumliteral_has_value():
    assert hasattr(ecoreDiff_EEnumLiteral, "value")
    descriptor = None
    for klass in ecoreDiff_EEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_etypeparameter_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ETypeParameter)


def test_ecorediff_etypeparameter_constructor_exists():
    assert callable(ecoreDiff_ETypeParameter.__init__)


def test_ecorediff_etypeparameter_constructor_args():
    sig = inspect.signature(ecoreDiff_ETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_epackage_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EPackage)


def test_ecorediff_epackage_constructor_exists():
    assert callable(ecoreDiff_EPackage.__init__)


def test_ecorediff_epackage_constructor_args():
    sig = inspect.signature(ecoreDiff_EPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"
    assert "nsURI" in params, "Missing parameter 'nsURI'"

def test_ecorediff_epackage_has_nsPrefix():
    assert hasattr(ecoreDiff_EPackage, "nsPrefix")
    descriptor = None
    for klass in ecoreDiff_EPackage.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_epackage_has_nsURI():
    assert hasattr(ecoreDiff_EPackage, "nsURI")
    descriptor = None
    for klass in ecoreDiff_EPackage.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_addedenamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedENamedElement)


def test_ecorediff_addedenamedelement_constructor_exists():
    assert callable(ecoreDiff_AddedENamedElement.__init__)


def test_ecorediff_addedenamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedenamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedENamedElement)


def test_ecorediff_changedenamedelement_constructor_exists():
    assert callable(ecoreDiff_ChangedENamedElement.__init__)


def test_ecorediff_changedenamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EClassifier)


def test_ecorediff_eclassifier_constructor_exists():
    assert callable(ecoreDiff_EClassifier.__init__)


def test_ecorediff_eclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff_EClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "instanceTypeName" in params, "Missing parameter 'instanceTypeName'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"

def test_ecorediff_eclassifier_has_defaultValue():
    assert hasattr(ecoreDiff_EClassifier, "defaultValue")
    descriptor = None
    for klass in ecoreDiff_EClassifier.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_eclassifier_has_instanceTypeName():
    assert hasattr(ecoreDiff_EClassifier, "instanceTypeName")
    descriptor = None
    for klass in ecoreDiff_EClassifier.__mro__:
        if "instanceTypeName" in klass.__dict__:
            descriptor = klass.__dict__["instanceTypeName"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_eclassifier_has_instanceClassName():
    assert hasattr(ecoreDiff_EClassifier, "instanceClassName")
    descriptor = None
    for klass in ecoreDiff_EClassifier.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_eclassifier_has_instanceClass():
    assert hasattr(ecoreDiff_EClassifier, "instanceClass")
    descriptor = None
    for klass in ecoreDiff_EClassifier.__mro__:
        if "instanceClass" in klass.__dict__:
            descriptor = klass.__dict__["instanceClass"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_egenerictype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EGenericType)


def test_ecorediff_egenerictype_constructor_exists():
    assert callable(ecoreDiff_EGenericType.__init__)


def test_ecorediff_egenerictype_constructor_args():
    sig = inspect.signature(ecoreDiff_EGenericType.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_ereference_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EReference)


def test_ecorediff_ereference_constructor_exists():
    assert callable(ecoreDiff_EReference.__init__)


def test_ecorediff_ereference_constructor_args():
    sig = inspect.signature(ecoreDiff_EReference.__init__)
    params = list(sig.parameters.keys())
    assert "container" in params, "Missing parameter 'container'"
    assert "containment" in params, "Missing parameter 'containment'"
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"

def test_ecorediff_ereference_has_container():
    assert hasattr(ecoreDiff_EReference, "container")
    descriptor = None
    for klass in ecoreDiff_EReference.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_ereference_has_containment():
    assert hasattr(ecoreDiff_EReference, "containment")
    descriptor = None
    for klass in ecoreDiff_EReference.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_ereference_has_resolveProxies():
    assert hasattr(ecoreDiff_EReference, "resolveProxies")
    descriptor = None
    for klass in ecoreDiff_EReference.__mro__:
        if "resolveProxies" in klass.__dict__:
            descriptor = klass.__dict__["resolveProxies"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EStructuralFeature)


def test_ecorediff_estructuralfeature_constructor_exists():
    assert callable(ecoreDiff_EStructuralFeature.__init__)


def test_ecorediff_estructuralfeature_constructor_args():
    sig = inspect.signature(ecoreDiff_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "unsettable" in params, "Missing parameter 'unsettable'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"

def test_ecorediff_estructuralfeature_has_transient():
    assert hasattr(ecoreDiff_EStructuralFeature, "transient")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estructuralfeature_has_defaultValue():
    assert hasattr(ecoreDiff_EStructuralFeature, "defaultValue")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estructuralfeature_has_unsettable():
    assert hasattr(ecoreDiff_EStructuralFeature, "unsettable")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "unsettable" in klass.__dict__:
            descriptor = klass.__dict__["unsettable"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estructuralfeature_has_changeable():
    assert hasattr(ecoreDiff_EStructuralFeature, "changeable")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estructuralfeature_has_derived():
    assert hasattr(ecoreDiff_EStructuralFeature, "derived")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estructuralfeature_has_volatile():
    assert hasattr(ecoreDiff_EStructuralFeature, "volatile")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estructuralfeature_has_defaultValueLiteral():
    assert hasattr(ecoreDiff_EStructuralFeature, "defaultValueLiteral")
    descriptor = None
    for klass in ecoreDiff_EStructuralFeature.__mro__:
        if "defaultValueLiteral" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueLiteral"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_eattribute_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EAttribute)


def test_ecorediff_eattribute_constructor_exists():
    assert callable(ecoreDiff_EAttribute.__init__)


def test_ecorediff_eattribute_constructor_args():
    sig = inspect.signature(ecoreDiff_EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_ecorediff_eattribute_has_iD():
    assert hasattr(ecoreDiff_EAttribute, "iD")
    descriptor = None
    for klass in ecoreDiff_EAttribute.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_eoperation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EOperation)


def test_ecorediff_eoperation_constructor_exists():
    assert callable(ecoreDiff_EOperation.__init__)


def test_ecorediff_eoperation_constructor_args():
    sig = inspect.signature(ecoreDiff_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedeclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEClassifier)


def test_ecorediff_addedeclassifier_constructor_exists():
    assert callable(ecoreDiff_AddedEClassifier.__init__)


def test_ecorediff_addedeclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_edatatype_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EDataType)


def test_ecorediff_edatatype_constructor_exists():
    assert callable(ecoreDiff_EDataType.__init__)


def test_ecorediff_edatatype_constructor_args():
    sig = inspect.signature(ecoreDiff_EDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"

def test_ecorediff_edatatype_has_serializable():
    assert hasattr(ecoreDiff_EDataType, "serializable")
    descriptor = None
    for klass in ecoreDiff_EDataType.__mro__:
        if "serializable" in klass.__dict__:
            descriptor = klass.__dict__["serializable"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_changedeclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEClassifier)


def test_ecorediff_changedeclassifier_constructor_exists():
    assert callable(ecoreDiff_ChangedEClassifier.__init__)


def test_ecorediff_changedeclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_deletedeclassifier_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEClassifier)


def test_ecorediff_deletedeclassifier_constructor_exists():
    assert callable(ecoreDiff_DeletedEClassifier.__init__)


def test_ecorediff_deletedeclassifier_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eclass_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EClass)


def test_ecorediff_eclass_constructor_exists():
    assert callable(ecoreDiff_EClass.__init__)


def test_ecorediff_eclass_constructor_args():
    sig = inspect.signature(ecoreDiff_EClass.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ecorediff_eclass_has_interface():
    assert hasattr(ecoreDiff_EClass, "interface")
    descriptor = None
    for klass in ecoreDiff_EClass.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_eclass_has_abstract():
    assert hasattr(ecoreDiff_EClass, "abstract")
    descriptor = None
    for klass in ecoreDiff_EClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ENamedElement)


def test_ecorediff_enamedelement_constructor_exists():
    assert callable(ecoreDiff_ENamedElement.__init__)


def test_ecorediff_enamedelement_constructor_args():
    sig = inspect.signature(ecoreDiff_ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecorediff_enamedelement_has_name():
    assert hasattr(ecoreDiff_ENamedElement, "name")
    descriptor = None
    for klass in ecoreDiff_ENamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_deletedemodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_DeletedEModelElement)


def test_ecorediff_deletedemodelelement_constructor_exists():
    assert callable(ecoreDiff_DeletedEModelElement.__init__)


def test_ecorediff_deletedemodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff_DeletedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_efactory_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EFactory)


def test_ecorediff_efactory_constructor_exists():
    assert callable(ecoreDiff_EFactory.__init__)


def test_ecorediff_efactory_constructor_args():
    sig = inspect.signature(ecoreDiff_EFactory.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_changedemodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_ChangedEModelElement)


def test_ecorediff_changedemodelelement_constructor_exists():
    assert callable(ecoreDiff_ChangedEModelElement.__init__)


def test_ecorediff_changedemodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff_ChangedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_addedemodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_AddedEModelElement)


def test_ecorediff_addedemodelelement_constructor_exists():
    assert callable(ecoreDiff_AddedEModelElement.__init__)


def test_ecorediff_addedemodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff_AddedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_eannotation_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EAnnotation)


def test_ecorediff_eannotation_constructor_exists():
    assert callable(ecoreDiff_EAnnotation.__init__)


def test_ecorediff_eannotation_constructor_args():
    sig = inspect.signature(ecoreDiff_EAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_ecorediff_eannotation_has_source():
    assert hasattr(ecoreDiff_EAnnotation, "source")
    descriptor = None
    for klass in ecoreDiff_EAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_ecorediff_eobject_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EObject)


def test_ecorediff_eobject_constructor_exists():
    assert callable(ecoreDiff_EObject.__init__)


def test_ecorediff_eobject_constructor_args():
    sig = inspect.signature(ecoreDiff_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_emodelelement_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EModelElement)


def test_ecorediff_emodelelement_constructor_exists():
    assert callable(ecoreDiff_EModelElement.__init__)


def test_ecorediff_emodelelement_constructor_args():
    sig = inspect.signature(ecoreDiff_EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ecorediff_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecoreDiff_EStringToStringMapEntry)


def test_ecorediff_estringtostringmapentry_constructor_exists():
    assert callable(ecoreDiff_EStringToStringMapEntry.__init__)


def test_ecorediff_estringtostringmapentry_constructor_args():
    sig = inspect.signature(ecoreDiff_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_ecorediff_estringtostringmapentry_has_key():
    assert hasattr(ecoreDiff_EStringToStringMapEntry, "key")
    descriptor = None
    for klass in ecoreDiff_EStringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_ecorediff_estringtostringmapentry_has_value():
    assert hasattr(ecoreDiff_EStringToStringMapEntry, "value")
    descriptor = None
    for klass in ecoreDiff_EStringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
EReference_strategy = st.builds(
    EReference,
)
ecoreDiff_DeletedEReference_strategy = st.builds(
    ecoreDiff_DeletedEReference,
)
ecoreDiff_AddedEReference_strategy = st.builds(
    ecoreDiff_AddedEReference,
)
EStructuralFeature_Wildcard_strategy = st.builds(
    EStructuralFeature_Wildcard,
)
ecoreDiff_DeletedEStructuralFeature_Wildcard_strategy = st.builds(
    ecoreDiff_DeletedEStructuralFeature_Wildcard,
)
ecoreDiff_ChangedEStructuralFeature_Wildcard_strategy = st.builds(
    ecoreDiff_ChangedEStructuralFeature_Wildcard,
)
ecoreDiff_AddedEStructuralFeature_Wildcard_strategy = st.builds(
    ecoreDiff_AddedEStructuralFeature_Wildcard,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
ecoreDiff_ChangedEAttribute_strategy = st.builds(
    ecoreDiff_ChangedEAttribute,
)
ecoreDiff_DeletedEAttribute_strategy = st.builds(
    ecoreDiff_DeletedEAttribute,
)
ecoreDiff_AddedEAttribute_strategy = st.builds(
    ecoreDiff_AddedEAttribute,
)
EEnumLiteral_strategy = st.builds(
    EEnumLiteral,
)
ecoreDiff_DeletedEEnumLiteral_strategy = st.builds(
    ecoreDiff_DeletedEEnumLiteral,
)
ecoreDiff_ChangedEEnumLiteral_strategy = st.builds(
    ecoreDiff_ChangedEEnumLiteral,
)
ecoreDiff_AddedEEnumLiteral_strategy = st.builds(
    ecoreDiff_AddedEEnumLiteral,
)
EEnum_strategy = st.builds(
    EEnum,
)
ecoreDiff_DeletedEEnum_strategy = st.builds(
    ecoreDiff_DeletedEEnum,
)
ecoreDiff_ChangedEEnum_strategy = st.builds(
    ecoreDiff_ChangedEEnum,
)
ecoreDiff_AddedEEnum_strategy = st.builds(
    ecoreDiff_AddedEEnum,
)
ecoreDiff_ChangedEReference_strategy = st.builds(
    ecoreDiff_ChangedEReference,
)
EOperation_strategy = st.builds(
    EOperation,
)
ecoreDiff_ChangedEOperation_strategy = st.builds(
    ecoreDiff_ChangedEOperation,
)
ecoreDiff_DeletedEOperation_strategy = st.builds(
    ecoreDiff_DeletedEOperation,
)
ecoreDiff_AddedEOperation_strategy = st.builds(
    ecoreDiff_AddedEOperation,
)
EClassifier_Wildcard_strategy = st.builds(
    EClassifier_Wildcard,
)
ecoreDiff_ChangedEClassifier_Wildcard_strategy = st.builds(
    ecoreDiff_ChangedEClassifier_Wildcard,
)
ecoreDiff_DeletedEClassifier_Wildcard_strategy = st.builds(
    ecoreDiff_DeletedEClassifier_Wildcard,
)
ecoreDiff_AddedEClassifier_Wildcard_strategy = st.builds(
    ecoreDiff_AddedEClassifier_Wildcard,
)
EParameter_strategy = st.builds(
    EParameter,
)
ecoreDiff_DeletedEParameter_strategy = st.builds(
    ecoreDiff_DeletedEParameter,
)
ecoreDiff_ChangedEParameter_strategy = st.builds(
    ecoreDiff_ChangedEParameter,
)
ecoreDiff_AddedEParameter_strategy = st.builds(
    ecoreDiff_AddedEParameter,
)
EFactory_strategy = st.builds(
    EFactory,
)
ecoreDiff_ChangedEFactory_strategy = st.builds(
    ecoreDiff_ChangedEFactory,
)
ecoreDiff_DeletedEFactory_strategy = st.builds(
    ecoreDiff_DeletedEFactory,
)
ecoreDiff_AddedEFactory_strategy = st.builds(
    ecoreDiff_AddedEFactory,
)
EPackage_strategy = st.builds(
    EPackage,
)
ecoreDiff_ChangedEPackage_strategy = st.builds(
    ecoreDiff_ChangedEPackage,
)
ecoreDiff_DeletedEPackage_strategy = st.builds(
    ecoreDiff_DeletedEPackage,
)
ecoreDiff_AddedEPackage_strategy = st.builds(
    ecoreDiff_AddedEPackage,
)
EGenericType_strategy = st.builds(
    EGenericType,
)
ecoreDiff_DeletedEGenericType_strategy = st.builds(
    ecoreDiff_DeletedEGenericType,
)
ecoreDiff_ChangedEGenericType_strategy = st.builds(
    ecoreDiff_ChangedEGenericType,
)
ecoreDiff_AddedEGenericType_strategy = st.builds(
    ecoreDiff_AddedEGenericType,
)
ETypeParameter_strategy = st.builds(
    ETypeParameter,
)
ecoreDiff_DeletedETypeParameter_strategy = st.builds(
    ecoreDiff_DeletedETypeParameter,
)
ecoreDiff_ChangedETypeParameter_strategy = st.builds(
    ecoreDiff_ChangedETypeParameter,
)
ecoreDiff_AddedETypeParameter_strategy = st.builds(
    ecoreDiff_AddedETypeParameter,
)
EClass_strategy = st.builds(
    EClass,
)
ecoreDiff_ChangedEClass_strategy = st.builds(
    ecoreDiff_ChangedEClass,
)
ecoreDiff_DeletedEClass_strategy = st.builds(
    ecoreDiff_DeletedEClass,
)
ecoreDiff_AddedEClass_strategy = st.builds(
    ecoreDiff_AddedEClass,
)
EStringToStringMapEntry_strategy = st.builds(
    EStringToStringMapEntry,
)
ecoreDiff_DeletedEStringToStringMapEntry_strategy = st.builds(
    ecoreDiff_DeletedEStringToStringMapEntry,
)
ecoreDiff_ChangedEStringToStringMapEntry_strategy = st.builds(
    ecoreDiff_ChangedEStringToStringMapEntry,
)
ecoreDiff_AddedEStringToStringMapEntry_strategy = st.builds(
    ecoreDiff_AddedEStringToStringMapEntry,
)
EAnnotation_strategy = st.builds(
    EAnnotation,
)
ecoreDiff_DeletedEAnnotation_strategy = st.builds(
    ecoreDiff_DeletedEAnnotation,
)
ecoreDiff_ChangedEAnnotation_strategy = st.builds(
    ecoreDiff_ChangedEAnnotation,
)
ecoreDiff_AddedEAnnotation_strategy = st.builds(
    ecoreDiff_AddedEAnnotation,
)
ecoreDiff_DifferenceElement_strategy = st.builds(
    ecoreDiff_DifferenceElement,
)
ecoreDiff_DifferenceModel_strategy = st.builds(
    ecoreDiff_DifferenceModel,
)
DifferenceElement_strategy = st.builds(
    DifferenceElement,
)
EDataType_strategy = st.builds(
    EDataType,
)
ecoreDiff_AddedEDataType_strategy = st.builds(
    ecoreDiff_AddedEDataType,
)
ecoreDiff_DeletedEDataType_strategy = st.builds(
    ecoreDiff_DeletedEDataType,
)
ecoreDiff_ChangedEDataType_strategy = st.builds(
    ecoreDiff_ChangedEDataType,
)
ecoreDiff_EEnum_strategy = st.builds(
    ecoreDiff_EEnum,
)
ecoreDiff_EStructuralFeature_Wildcard_strategy = st.builds(
    ecoreDiff_EStructuralFeature_Wildcard,
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
ecoreDiff_DeletedEStructuralFeature_strategy = st.builds(
    ecoreDiff_DeletedEStructuralFeature,
)
ecoreDiff_AddedEStructuralFeature_strategy = st.builds(
    ecoreDiff_AddedEStructuralFeature,
)
ecoreDiff_ChangedEStructuralFeature_strategy = st.builds(
    ecoreDiff_ChangedEStructuralFeature,
)
EObject_strategy = st.builds(
    EObject,
)
ecoreDiff_AddedEObject_strategy = st.builds(
    ecoreDiff_AddedEObject,
)
ecoreDiff_DeletedEObject_strategy = st.builds(
    ecoreDiff_DeletedEObject,
)
ecoreDiff_ChangedEObject_strategy = st.builds(
    ecoreDiff_ChangedEObject,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
ecoreDiff_DeletedETypedElement_strategy = st.builds(
    ecoreDiff_DeletedETypedElement,
)
ecoreDiff_EParameter_strategy = st.builds(
    ecoreDiff_EParameter,
)
ecoreDiff_AddedETypedElement_strategy = st.builds(
    ecoreDiff_AddedETypedElement,
)
ecoreDiff_ChangedETypedElement_strategy = st.builds(
    ecoreDiff_ChangedETypedElement,
)
ecoreDiff_EClassifier_Wildcard_strategy = st.builds(
    ecoreDiff_EClassifier_Wildcard,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ecoreDiff_ETypedElement_strategy = st.builds(
    ecoreDiff_ETypedElement,
    many=
        st.booleans(),
    lowerBound=
        st.integers(),
    unique=
        st.booleans(),
    required=
        safe_text,
    upperBound=
        st.integers(),
    ordered=
        st.booleans()
)
ecoreDiff_DeletedENamedElement_strategy = st.builds(
    ecoreDiff_DeletedENamedElement,
)
ecoreDiff_EEnumLiteral_strategy = st.builds(
    ecoreDiff_EEnumLiteral,
    literal=
        safe_text,
    instance=
        safe_text,
    value=
        st.integers()
)
ecoreDiff_ETypeParameter_strategy = st.builds(
    ecoreDiff_ETypeParameter,
)
ecoreDiff_EPackage_strategy = st.builds(
    ecoreDiff_EPackage,
    nsPrefix=
        safe_text,
    nsURI=
        safe_text
)
ecoreDiff_AddedENamedElement_strategy = st.builds(
    ecoreDiff_AddedENamedElement,
)
ecoreDiff_ChangedENamedElement_strategy = st.builds(
    ecoreDiff_ChangedENamedElement,
)
ecoreDiff_EClassifier_strategy = st.builds(
    ecoreDiff_EClassifier,
    defaultValue=
        safe_text,
    instanceTypeName=
        safe_text,
    instanceClassName=
        safe_text,
    instanceClass=
        safe_text
)
ecoreDiff_EGenericType_strategy = st.builds(
    ecoreDiff_EGenericType,
)
ecoreDiff_EReference_strategy = st.builds(
    ecoreDiff_EReference,
    container=
        st.booleans(),
    containment=
        st.booleans(),
    resolveProxies=
        st.booleans()
)
ecoreDiff_EStructuralFeature_strategy = st.builds(
    ecoreDiff_EStructuralFeature,
    transient=
        st.booleans(),
    defaultValue=
        safe_text,
    unsettable=
        st.booleans(),
    changeable=
        st.booleans(),
    derived=
        st.booleans(),
    volatile=
        st.booleans(),
    defaultValueLiteral=
        safe_text
)
ecoreDiff_EAttribute_strategy = st.builds(
    ecoreDiff_EAttribute,
    iD=
        st.booleans()
)
ecoreDiff_EOperation_strategy = st.builds(
    ecoreDiff_EOperation,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
ecoreDiff_AddedEClassifier_strategy = st.builds(
    ecoreDiff_AddedEClassifier,
)
ecoreDiff_EDataType_strategy = st.builds(
    ecoreDiff_EDataType,
    serializable=
        st.booleans()
)
ecoreDiff_ChangedEClassifier_strategy = st.builds(
    ecoreDiff_ChangedEClassifier,
)
ecoreDiff_DeletedEClassifier_strategy = st.builds(
    ecoreDiff_DeletedEClassifier,
)
ecoreDiff_EClass_strategy = st.builds(
    ecoreDiff_EClass,
    interface=
        st.booleans(),
    abstract=
        st.booleans()
)
EModelElement_strategy = st.builds(
    EModelElement,
)
ecoreDiff_ENamedElement_strategy = st.builds(
    ecoreDiff_ENamedElement,
    name=
        safe_text
)
ecoreDiff_DeletedEModelElement_strategy = st.builds(
    ecoreDiff_DeletedEModelElement,
)
ecoreDiff_EFactory_strategy = st.builds(
    ecoreDiff_EFactory,
)
ecoreDiff_ChangedEModelElement_strategy = st.builds(
    ecoreDiff_ChangedEModelElement,
)
ecoreDiff_AddedEModelElement_strategy = st.builds(
    ecoreDiff_AddedEModelElement,
)
ecoreDiff_EAnnotation_strategy = st.builds(
    ecoreDiff_EAnnotation,
    source=
        safe_text
)
ecoreDiff_EObject_strategy = st.builds(
    ecoreDiff_EObject,
)
ecoreDiff_EModelElement_strategy = st.builds(
    ecoreDiff_EModelElement,
)
ecoreDiff_EStringToStringMapEntry_strategy = st.builds(
    ecoreDiff_EStringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)

@given(instance=EReference_strategy)
@settings(max_examples=50)
def test_ereference_instantiation(instance):
    assert isinstance(instance, EReference)

@given(instance=ecoreDiff_DeletedEReference_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEReference)

@given(instance=ecoreDiff_AddedEReference_strategy)
@settings(max_examples=50)
def test_ecorediff_addedereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEReference)

@given(instance=EStructuralFeature_Wildcard_strategy)
@settings(max_examples=50)
def test_estructuralfeature_wildcard_instantiation(instance):
    assert isinstance(instance, EStructuralFeature_Wildcard)

@given(instance=ecoreDiff_DeletedEStructuralFeature_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedestructuralfeature_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEStructuralFeature_Wildcard)

@given(instance=ecoreDiff_ChangedEStructuralFeature_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_changedestructuralfeature_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEStructuralFeature_Wildcard)

@given(instance=ecoreDiff_AddedEStructuralFeature_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_addedestructuralfeature_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEStructuralFeature_Wildcard)

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=ecoreDiff_ChangedEAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEAttribute)

@given(instance=ecoreDiff_DeletedEAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEAttribute)

@given(instance=ecoreDiff_AddedEAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEAttribute)

@given(instance=EEnumLiteral_strategy)
@settings(max_examples=50)
def test_eenumliteral_instantiation(instance):
    assert isinstance(instance, EEnumLiteral)

@given(instance=ecoreDiff_DeletedEEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEEnumLiteral)

@given(instance=ecoreDiff_ChangedEEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEEnumLiteral)

@given(instance=ecoreDiff_AddedEEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEEnumLiteral)

@given(instance=EEnum_strategy)
@settings(max_examples=50)
def test_eenum_instantiation(instance):
    assert isinstance(instance, EEnum)

@given(instance=ecoreDiff_DeletedEEnum_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEEnum)

@given(instance=ecoreDiff_ChangedEEnum_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEEnum)

@given(instance=ecoreDiff_AddedEEnum_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEEnum)

@given(instance=ecoreDiff_ChangedEReference_strategy)
@settings(max_examples=50)
def test_ecorediff_changedereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEReference)

@given(instance=EOperation_strategy)
@settings(max_examples=50)
def test_eoperation_instantiation(instance):
    assert isinstance(instance, EOperation)

@given(instance=ecoreDiff_ChangedEOperation_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEOperation)

@given(instance=ecoreDiff_DeletedEOperation_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEOperation)

@given(instance=ecoreDiff_AddedEOperation_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEOperation)

@given(instance=EClassifier_Wildcard_strategy)
@settings(max_examples=50)
def test_eclassifier_wildcard_instantiation(instance):
    assert isinstance(instance, EClassifier_Wildcard)

@given(instance=ecoreDiff_ChangedEClassifier_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeclassifier_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEClassifier_Wildcard)

@given(instance=ecoreDiff_DeletedEClassifier_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeclassifier_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEClassifier_Wildcard)

@given(instance=ecoreDiff_AddedEClassifier_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeclassifier_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEClassifier_Wildcard)

@given(instance=EParameter_strategy)
@settings(max_examples=50)
def test_eparameter_instantiation(instance):
    assert isinstance(instance, EParameter)

@given(instance=ecoreDiff_DeletedEParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEParameter)

@given(instance=ecoreDiff_ChangedEParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEParameter)

@given(instance=ecoreDiff_AddedEParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEParameter)

@given(instance=EFactory_strategy)
@settings(max_examples=50)
def test_efactory_instantiation(instance):
    assert isinstance(instance, EFactory)

@given(instance=ecoreDiff_ChangedEFactory_strategy)
@settings(max_examples=50)
def test_ecorediff_changedefactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEFactory)

@given(instance=ecoreDiff_DeletedEFactory_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedefactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEFactory)

@given(instance=ecoreDiff_AddedEFactory_strategy)
@settings(max_examples=50)
def test_ecorediff_addedefactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEFactory)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=ecoreDiff_ChangedEPackage_strategy)
@settings(max_examples=50)
def test_ecorediff_changedepackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEPackage)

@given(instance=ecoreDiff_DeletedEPackage_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedepackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEPackage)

@given(instance=ecoreDiff_AddedEPackage_strategy)
@settings(max_examples=50)
def test_ecorediff_addedepackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEPackage)

@given(instance=EGenericType_strategy)
@settings(max_examples=50)
def test_egenerictype_instantiation(instance):
    assert isinstance(instance, EGenericType)

@given(instance=ecoreDiff_DeletedEGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedegenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEGenericType)

@given(instance=ecoreDiff_ChangedEGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff_changedegenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEGenericType)

@given(instance=ecoreDiff_AddedEGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff_addedegenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEGenericType)

@given(instance=ETypeParameter_strategy)
@settings(max_examples=50)
def test_etypeparameter_instantiation(instance):
    assert isinstance(instance, ETypeParameter)

@given(instance=ecoreDiff_DeletedETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedetypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedETypeParameter)

@given(instance=ecoreDiff_ChangedETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_changedetypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedETypeParameter)

@given(instance=ecoreDiff_AddedETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_addedetypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedETypeParameter)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=ecoreDiff_ChangedEClass_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEClass)

@given(instance=ecoreDiff_DeletedEClass_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEClass)

@given(instance=ecoreDiff_AddedEClass_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEClass)

@given(instance=EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, EStringToStringMapEntry)

@given(instance=ecoreDiff_DeletedEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEStringToStringMapEntry)

@given(instance=ecoreDiff_ChangedEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff_changedestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEStringToStringMapEntry)

@given(instance=ecoreDiff_AddedEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff_addedestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEStringToStringMapEntry)

@given(instance=EAnnotation_strategy)
@settings(max_examples=50)
def test_eannotation_instantiation(instance):
    assert isinstance(instance, EAnnotation)

@given(instance=ecoreDiff_DeletedEAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEAnnotation)

@given(instance=ecoreDiff_ChangedEAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEAnnotation)

@given(instance=ecoreDiff_AddedEAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEAnnotation)

@given(instance=ecoreDiff_DifferenceElement_strategy)
@settings(max_examples=50)
def test_ecorediff_differenceelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DifferenceElement)

@given(instance=ecoreDiff_DifferenceModel_strategy)
@settings(max_examples=50)
def test_ecorediff_differencemodel_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DifferenceModel)

@given(instance=DifferenceElement_strategy)
@settings(max_examples=50)
def test_differenceelement_instantiation(instance):
    assert isinstance(instance, DifferenceElement)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=ecoreDiff_AddedEDataType_strategy)
@settings(max_examples=50)
def test_ecorediff_addededatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEDataType)

@given(instance=ecoreDiff_DeletedEDataType_strategy)
@settings(max_examples=50)
def test_ecorediff_deletededatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEDataType)

@given(instance=ecoreDiff_ChangedEDataType_strategy)
@settings(max_examples=50)
def test_ecorediff_changededatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEDataType)

@given(instance=ecoreDiff_EEnum_strategy)
@settings(max_examples=50)
def test_ecorediff_eenum_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EEnum)

@given(instance=ecoreDiff_EStructuralFeature_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_estructuralfeature_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EStructuralFeature_Wildcard)

@given(instance=EStructuralFeature_strategy)
@settings(max_examples=50)
def test_estructuralfeature_instantiation(instance):
    assert isinstance(instance, EStructuralFeature)

@given(instance=ecoreDiff_DeletedEStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedestructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEStructuralFeature)

@given(instance=ecoreDiff_AddedEStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff_addedestructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEStructuralFeature)

@given(instance=ecoreDiff_ChangedEStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff_changedestructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEStructuralFeature)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=ecoreDiff_AddedEObject_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEObject)

@given(instance=ecoreDiff_DeletedEObject_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEObject)

@given(instance=ecoreDiff_ChangedEObject_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEObject)

@given(instance=ETypedElement_strategy)
@settings(max_examples=50)
def test_etypedelement_instantiation(instance):
    assert isinstance(instance, ETypedElement)

@given(instance=ecoreDiff_DeletedETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedetypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedETypedElement)

@given(instance=ecoreDiff_EParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_eparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EParameter)

@given(instance=ecoreDiff_AddedETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_addedetypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedETypedElement)

@given(instance=ecoreDiff_ChangedETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_changedetypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedETypedElement)

@given(instance=ecoreDiff_EClassifier_Wildcard_strategy)
@settings(max_examples=50)
def test_ecorediff_eclassifier_wildcard_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EClassifier_Wildcard)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ecoreDiff_ETypedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_etypedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ETypedElement)



@given(instance=ecoreDiff_ETypedElement_strategy)
def test_ecorediff_etypedelement_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=ecoreDiff_ETypedElement_strategy)
def test_ecorediff_etypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=ecoreDiff_ETypedElement_strategy)
def test_ecorediff_etypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=ecoreDiff_ETypedElement_strategy)
def test_ecorediff_etypedelement_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=ecoreDiff_ETypedElement_strategy)
def test_ecorediff_etypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=ecoreDiff_ETypedElement_strategy)
def test_ecorediff_etypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=ecoreDiff_DeletedENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedenamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedENamedElement)

@given(instance=ecoreDiff_EEnumLiteral_strategy)
@settings(max_examples=50)
def test_ecorediff_eenumliteral_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EEnumLiteral)



@given(instance=ecoreDiff_EEnumLiteral_strategy)
def test_ecorediff_eenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=ecoreDiff_EEnumLiteral_strategy)
def test_ecorediff_eenumliteral_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original



@given(instance=ecoreDiff_EEnumLiteral_strategy)
def test_ecorediff_eenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecoreDiff_ETypeParameter_strategy)
@settings(max_examples=50)
def test_ecorediff_etypeparameter_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ETypeParameter)

@given(instance=ecoreDiff_EPackage_strategy)
@settings(max_examples=50)
def test_ecorediff_epackage_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EPackage)



@given(instance=ecoreDiff_EPackage_strategy)
def test_ecorediff_epackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original



@given(instance=ecoreDiff_EPackage_strategy)
def test_ecorediff_epackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

@given(instance=ecoreDiff_AddedENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_addedenamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedENamedElement)

@given(instance=ecoreDiff_ChangedENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_changedenamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedENamedElement)

@given(instance=ecoreDiff_EClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff_eclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EClassifier)



@given(instance=ecoreDiff_EClassifier_strategy)
def test_ecorediff_eclassifier_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=ecoreDiff_EClassifier_strategy)
def test_ecorediff_eclassifier_instanceTypeName_setter(instance):
    original = instance.instanceTypeName
    instance.instanceTypeName = original
    assert instance.instanceTypeName == original



@given(instance=ecoreDiff_EClassifier_strategy)
def test_ecorediff_eclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original



@given(instance=ecoreDiff_EClassifier_strategy)
def test_ecorediff_eclassifier_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original

@given(instance=ecoreDiff_EGenericType_strategy)
@settings(max_examples=50)
def test_ecorediff_egenerictype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EGenericType)

@given(instance=ecoreDiff_EReference_strategy)
@settings(max_examples=50)
def test_ecorediff_ereference_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EReference)



@given(instance=ecoreDiff_EReference_strategy)
def test_ecorediff_ereference_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=ecoreDiff_EReference_strategy)
def test_ecorediff_ereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original



@given(instance=ecoreDiff_EReference_strategy)
def test_ecorediff_ereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original

@given(instance=ecoreDiff_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_ecorediff_estructuralfeature_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EStructuralFeature)



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=ecoreDiff_EStructuralFeature_strategy)
def test_ecorediff_estructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original

@given(instance=ecoreDiff_EAttribute_strategy)
@settings(max_examples=50)
def test_ecorediff_eattribute_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EAttribute)



@given(instance=ecoreDiff_EAttribute_strategy)
def test_ecorediff_eattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=ecoreDiff_EOperation_strategy)
@settings(max_examples=50)
def test_ecorediff_eoperation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EOperation)

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=ecoreDiff_AddedEClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff_addedeclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEClassifier)

@given(instance=ecoreDiff_EDataType_strategy)
@settings(max_examples=50)
def test_ecorediff_edatatype_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EDataType)



@given(instance=ecoreDiff_EDataType_strategy)
def test_ecorediff_edatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original

@given(instance=ecoreDiff_ChangedEClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff_changedeclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEClassifier)

@given(instance=ecoreDiff_DeletedEClassifier_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedeclassifier_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEClassifier)

@given(instance=ecoreDiff_EClass_strategy)
@settings(max_examples=50)
def test_ecorediff_eclass_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EClass)



@given(instance=ecoreDiff_EClass_strategy)
def test_ecorediff_eclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original



@given(instance=ecoreDiff_EClass_strategy)
def test_ecorediff_eclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=ecoreDiff_ENamedElement_strategy)
@settings(max_examples=50)
def test_ecorediff_enamedelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ENamedElement)



@given(instance=ecoreDiff_ENamedElement_strategy)
def test_ecorediff_enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecoreDiff_DeletedEModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff_deletedemodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_DeletedEModelElement)

@given(instance=ecoreDiff_EFactory_strategy)
@settings(max_examples=50)
def test_ecorediff_efactory_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EFactory)

@given(instance=ecoreDiff_ChangedEModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff_changedemodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_ChangedEModelElement)

@given(instance=ecoreDiff_AddedEModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff_addedemodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_AddedEModelElement)

@given(instance=ecoreDiff_EAnnotation_strategy)
@settings(max_examples=50)
def test_ecorediff_eannotation_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EAnnotation)



@given(instance=ecoreDiff_EAnnotation_strategy)
def test_ecorediff_eannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=ecoreDiff_EObject_strategy)
@settings(max_examples=50)
def test_ecorediff_eobject_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EObject)

@given(instance=ecoreDiff_EModelElement_strategy)
@settings(max_examples=50)
def test_ecorediff_emodelelement_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EModelElement)

@given(instance=ecoreDiff_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecorediff_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecoreDiff_EStringToStringMapEntry)



@given(instance=ecoreDiff_EStringToStringMapEntry_strategy)
def test_ecorediff_estringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=ecoreDiff_EStringToStringMapEntry_strategy)
def test_ecorediff_estringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
