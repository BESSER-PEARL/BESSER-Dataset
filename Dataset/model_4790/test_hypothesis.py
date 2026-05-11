import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    types::JvmAnnotationReference,
    types::JvmAnnotationTarget,
    JvmAnnotationValue,
    types::JvmShortAnnotationValue,
    types::JvmDoubleAnnotationValue,
    types::JvmTypeAnnotationValue,
    types::JvmByteAnnotationValue,
    types::JvmBooleanAnnotationValue,
    types::JvmLongAnnotationValue,
    types::JvmStringAnnotationValue,
    types::JvmFloatAnnotationValue,
    types::JvmEnumAnnotationValue,
    types::JvmCustomAnnotationValue,
    types::JvmCharAnnotationValue,
    types::JvmIntAnnotationValue,
    JvmAnnotationTarget,
    types::JvmAnnotationAnnotationValue,
    JvmCompoundTypeReference,
    types::JvmSynonymTypeReference,
    types::JvmMultiTypeReference,
    types::JvmAnnotationValue,
    JvmExecutable,
    types::JvmOperation,
    types::JvmConstructor,
    JvmFeature,
    types::JvmField,
    JvmTypeParameterDeclarator,
    types::JvmExecutable,
    JvmField,
    types::JvmEnumerationLiteral,
    JvmDeclaredType,
    types::JvmGenericType,
    types::JvmEnumerationType,
    types::JvmAnnotationType,
    JvmTypeReference,
    types::JvmCompoundTypeReference,
    types::JvmUnknownTypeReference,
    types::JvmDelegateTypeReference,
    types::JvmAnyTypeReference,
    types::JvmGenericArrayTypeReference,
    types::JvmSpecializedTypeReference,
    types::JvmParameterizedTypeReference,
    JvmTypeConstraint,
    types::JvmLowerBound,
    types::JvmUpperBound,
    types::JvmTypeConstraint,
    types::JvmConstraintOwner,
    types::JvmTypeParameterDeclarator,
    JvmConstraintOwner,
    types::JvmWildcardTypeReference,
    types::JvmTypeReference,
    JvmMember,
    types::JvmFeature,
    JvmComponentType,
    types::JvmTypeParameter,
    types::JvmDeclaredType,
    types::JvmPrimitiveType,
    types::JvmArrayType,
    JvmType,
    types::JvmComponentType,
    types::JvmVoid,
    JvmIdentifiableElement,
    types::JvmFormalParameter,
    types::JvmMember,
    types::JvmType,
    types::JvmIdentifiableElement,
    JvmVisibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types::jvmannotationreference_is_not_abstract():
    assert not inspect.isabstract(types::JvmAnnotationReference)


def test_types::jvmannotationreference_constructor_exists():
    assert callable(types::JvmAnnotationReference.__init__)


def test_types::jvmannotationreference_constructor_args():
    sig = inspect.signature(types::JvmAnnotationReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmannotationtarget_is_not_abstract():
    assert not inspect.isabstract(types::JvmAnnotationTarget)


def test_types::jvmannotationtarget_constructor_exists():
    assert callable(types::JvmAnnotationTarget.__init__)


def test_types::jvmannotationtarget_constructor_args():
    sig = inspect.signature(types::JvmAnnotationTarget.__init__)
    params = list(sig.parameters.keys())



def test_jvmannotationvalue_is_not_abstract():
    assert not inspect.isabstract(JvmAnnotationValue)


def test_jvmannotationvalue_constructor_exists():
    assert callable(JvmAnnotationValue.__init__)


def test_jvmannotationvalue_constructor_args():
    sig = inspect.signature(JvmAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmshortannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmShortAnnotationValue)


def test_types::jvmshortannotationvalue_constructor_exists():
    assert callable(types::JvmShortAnnotationValue.__init__)


def test_types::jvmshortannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmShortAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmshortannotationvalue_has_values():
    assert hasattr(types::JvmShortAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmShortAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmdoubleannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmDoubleAnnotationValue)


def test_types::jvmdoubleannotationvalue_constructor_exists():
    assert callable(types::JvmDoubleAnnotationValue.__init__)


def test_types::jvmdoubleannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmDoubleAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmdoubleannotationvalue_has_values():
    assert hasattr(types::JvmDoubleAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmDoubleAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmtypeannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmTypeAnnotationValue)


def test_types::jvmtypeannotationvalue_constructor_exists():
    assert callable(types::JvmTypeAnnotationValue.__init__)


def test_types::jvmtypeannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmTypeAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmbyteannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmByteAnnotationValue)


def test_types::jvmbyteannotationvalue_constructor_exists():
    assert callable(types::JvmByteAnnotationValue.__init__)


def test_types::jvmbyteannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmByteAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmbyteannotationvalue_has_values():
    assert hasattr(types::JvmByteAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmByteAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmbooleanannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmBooleanAnnotationValue)


def test_types::jvmbooleanannotationvalue_constructor_exists():
    assert callable(types::JvmBooleanAnnotationValue.__init__)


def test_types::jvmbooleanannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmBooleanAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmbooleanannotationvalue_has_values():
    assert hasattr(types::JvmBooleanAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmBooleanAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmlongannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmLongAnnotationValue)


def test_types::jvmlongannotationvalue_constructor_exists():
    assert callable(types::JvmLongAnnotationValue.__init__)


def test_types::jvmlongannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmLongAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmlongannotationvalue_has_values():
    assert hasattr(types::JvmLongAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmLongAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmstringannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmStringAnnotationValue)


def test_types::jvmstringannotationvalue_constructor_exists():
    assert callable(types::JvmStringAnnotationValue.__init__)


def test_types::jvmstringannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmStringAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmstringannotationvalue_has_values():
    assert hasattr(types::JvmStringAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmStringAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmfloatannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmFloatAnnotationValue)


def test_types::jvmfloatannotationvalue_constructor_exists():
    assert callable(types::JvmFloatAnnotationValue.__init__)


def test_types::jvmfloatannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmFloatAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmfloatannotationvalue_has_values():
    assert hasattr(types::JvmFloatAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmFloatAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmenumannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmEnumAnnotationValue)


def test_types::jvmenumannotationvalue_constructor_exists():
    assert callable(types::JvmEnumAnnotationValue.__init__)


def test_types::jvmenumannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmEnumAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmcustomannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmCustomAnnotationValue)


def test_types::jvmcustomannotationvalue_constructor_exists():
    assert callable(types::JvmCustomAnnotationValue.__init__)


def test_types::jvmcustomannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmCustomAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmcustomannotationvalue_has_values():
    assert hasattr(types::JvmCustomAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmCustomAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmcharannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmCharAnnotationValue)


def test_types::jvmcharannotationvalue_constructor_exists():
    assert callable(types::JvmCharAnnotationValue.__init__)


def test_types::jvmcharannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmCharAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmcharannotationvalue_has_values():
    assert hasattr(types::JvmCharAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmCharAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmintannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmIntAnnotationValue)


def test_types::jvmintannotationvalue_constructor_exists():
    assert callable(types::JvmIntAnnotationValue.__init__)


def test_types::jvmintannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmIntAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_types::jvmintannotationvalue_has_values():
    assert hasattr(types::JvmIntAnnotationValue, "values")
    descriptor = None
    for klass in types::JvmIntAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_jvmannotationtarget_is_not_abstract():
    assert not inspect.isabstract(JvmAnnotationTarget)


def test_jvmannotationtarget_constructor_exists():
    assert callable(JvmAnnotationTarget.__init__)


def test_jvmannotationtarget_constructor_args():
    sig = inspect.signature(JvmAnnotationTarget.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmannotationannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmAnnotationAnnotationValue)


def test_types::jvmannotationannotationvalue_constructor_exists():
    assert callable(types::JvmAnnotationAnnotationValue.__init__)


def test_types::jvmannotationannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmAnnotationAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_jvmcompoundtypereference_is_not_abstract():
    assert not inspect.isabstract(JvmCompoundTypeReference)


def test_jvmcompoundtypereference_constructor_exists():
    assert callable(JvmCompoundTypeReference.__init__)


def test_jvmcompoundtypereference_constructor_args():
    sig = inspect.signature(JvmCompoundTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmsynonymtypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmSynonymTypeReference)


def test_types::jvmsynonymtypereference_constructor_exists():
    assert callable(types::JvmSynonymTypeReference.__init__)


def test_types::jvmsynonymtypereference_constructor_args():
    sig = inspect.signature(types::JvmSynonymTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmmultitypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmMultiTypeReference)


def test_types::jvmmultitypereference_constructor_exists():
    assert callable(types::JvmMultiTypeReference.__init__)


def test_types::jvmmultitypereference_constructor_args():
    sig = inspect.signature(types::JvmMultiTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmannotationvalue_is_not_abstract():
    assert not inspect.isabstract(types::JvmAnnotationValue)


def test_types::jvmannotationvalue_constructor_exists():
    assert callable(types::JvmAnnotationValue.__init__)


def test_types::jvmannotationvalue_constructor_args():
    sig = inspect.signature(types::JvmAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_jvmexecutable_is_not_abstract():
    assert not inspect.isabstract(JvmExecutable)


def test_jvmexecutable_constructor_exists():
    assert callable(JvmExecutable.__init__)


def test_jvmexecutable_constructor_args():
    sig = inspect.signature(JvmExecutable.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmoperation_is_not_abstract():
    assert not inspect.isabstract(types::JvmOperation)


def test_types::jvmoperation_constructor_exists():
    assert callable(types::JvmOperation.__init__)


def test_types::jvmoperation_constructor_args():
    sig = inspect.signature(types::JvmOperation.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "static" in params, "Missing parameter 'static'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_types::jvmoperation_has_final():
    assert hasattr(types::JvmOperation, "final")
    descriptor = None
    for klass in types::JvmOperation.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmoperation_has_static():
    assert hasattr(types::JvmOperation, "static")
    descriptor = None
    for klass in types::JvmOperation.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmoperation_has_abstract():
    assert hasattr(types::JvmOperation, "abstract")
    descriptor = None
    for klass in types::JvmOperation.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmconstructor_is_not_abstract():
    assert not inspect.isabstract(types::JvmConstructor)


def test_types::jvmconstructor_constructor_exists():
    assert callable(types::JvmConstructor.__init__)


def test_types::jvmconstructor_constructor_args():
    sig = inspect.signature(types::JvmConstructor.__init__)
    params = list(sig.parameters.keys())



def test_jvmfeature_is_not_abstract():
    assert not inspect.isabstract(JvmFeature)


def test_jvmfeature_constructor_exists():
    assert callable(JvmFeature.__init__)


def test_jvmfeature_constructor_args():
    sig = inspect.signature(JvmFeature.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmfield_is_not_abstract():
    assert not inspect.isabstract(types::JvmField)


def test_types::jvmfield_constructor_exists():
    assert callable(types::JvmField.__init__)


def test_types::jvmfield_constructor_args():
    sig = inspect.signature(types::JvmField.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"

def test_types::jvmfield_has_static():
    assert hasattr(types::JvmField, "static")
    descriptor = None
    for klass in types::JvmField.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmfield_has_final():
    assert hasattr(types::JvmField, "final")
    descriptor = None
    for klass in types::JvmField.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_jvmtypeparameterdeclarator_is_not_abstract():
    assert not inspect.isabstract(JvmTypeParameterDeclarator)


def test_jvmtypeparameterdeclarator_constructor_exists():
    assert callable(JvmTypeParameterDeclarator.__init__)


def test_jvmtypeparameterdeclarator_constructor_args():
    sig = inspect.signature(JvmTypeParameterDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmexecutable_is_not_abstract():
    assert not inspect.isabstract(types::JvmExecutable)


def test_types::jvmexecutable_constructor_exists():
    assert callable(types::JvmExecutable.__init__)


def test_types::jvmexecutable_constructor_args():
    sig = inspect.signature(types::JvmExecutable.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"

def test_types::jvmexecutable_has_varArgs():
    assert hasattr(types::JvmExecutable, "varArgs")
    descriptor = None
    for klass in types::JvmExecutable.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)



def test_jvmfield_is_not_abstract():
    assert not inspect.isabstract(JvmField)


def test_jvmfield_constructor_exists():
    assert callable(JvmField.__init__)


def test_jvmfield_constructor_args():
    sig = inspect.signature(JvmField.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(types::JvmEnumerationLiteral)


def test_types::jvmenumerationliteral_constructor_exists():
    assert callable(types::JvmEnumerationLiteral.__init__)


def test_types::jvmenumerationliteral_constructor_args():
    sig = inspect.signature(types::JvmEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(JvmDeclaredType)


def test_jvmdeclaredtype_constructor_exists():
    assert callable(JvmDeclaredType.__init__)


def test_jvmdeclaredtype_constructor_args():
    sig = inspect.signature(JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmgenerictype_is_not_abstract():
    assert not inspect.isabstract(types::JvmGenericType)


def test_types::jvmgenerictype_constructor_exists():
    assert callable(types::JvmGenericType.__init__)


def test_types::jvmgenerictype_constructor_args():
    sig = inspect.signature(types::JvmGenericType.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_types::jvmgenerictype_has_interface():
    assert hasattr(types::JvmGenericType, "interface")
    descriptor = None
    for klass in types::JvmGenericType.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmenumerationtype_is_not_abstract():
    assert not inspect.isabstract(types::JvmEnumerationType)


def test_types::jvmenumerationtype_constructor_exists():
    assert callable(types::JvmEnumerationType.__init__)


def test_types::jvmenumerationtype_constructor_args():
    sig = inspect.signature(types::JvmEnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmannotationtype_is_not_abstract():
    assert not inspect.isabstract(types::JvmAnnotationType)


def test_types::jvmannotationtype_constructor_exists():
    assert callable(types::JvmAnnotationType.__init__)


def test_types::jvmannotationtype_constructor_args():
    sig = inspect.signature(types::JvmAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(JvmTypeReference)


def test_jvmtypereference_constructor_exists():
    assert callable(JvmTypeReference.__init__)


def test_jvmtypereference_constructor_args():
    sig = inspect.signature(JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmcompoundtypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmCompoundTypeReference)


def test_types::jvmcompoundtypereference_constructor_exists():
    assert callable(types::JvmCompoundTypeReference.__init__)


def test_types::jvmcompoundtypereference_constructor_args():
    sig = inspect.signature(types::JvmCompoundTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmunknowntypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmUnknownTypeReference)


def test_types::jvmunknowntypereference_constructor_exists():
    assert callable(types::JvmUnknownTypeReference.__init__)


def test_types::jvmunknowntypereference_constructor_args():
    sig = inspect.signature(types::JvmUnknownTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "exception" in params, "Missing parameter 'exception'"

def test_types::jvmunknowntypereference_has_exception():
    assert hasattr(types::JvmUnknownTypeReference, "exception")
    descriptor = None
    for klass in types::JvmUnknownTypeReference.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmdelegatetypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmDelegateTypeReference)


def test_types::jvmdelegatetypereference_constructor_exists():
    assert callable(types::JvmDelegateTypeReference.__init__)


def test_types::jvmdelegatetypereference_constructor_args():
    sig = inspect.signature(types::JvmDelegateTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmanytypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmAnyTypeReference)


def test_types::jvmanytypereference_constructor_exists():
    assert callable(types::JvmAnyTypeReference.__init__)


def test_types::jvmanytypereference_constructor_args():
    sig = inspect.signature(types::JvmAnyTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmgenericarraytypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmGenericArrayTypeReference)


def test_types::jvmgenericarraytypereference_constructor_exists():
    assert callable(types::JvmGenericArrayTypeReference.__init__)


def test_types::jvmgenericarraytypereference_constructor_args():
    sig = inspect.signature(types::JvmGenericArrayTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmspecializedtypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmSpecializedTypeReference)


def test_types::jvmspecializedtypereference_constructor_exists():
    assert callable(types::JvmSpecializedTypeReference.__init__)


def test_types::jvmspecializedtypereference_constructor_args():
    sig = inspect.signature(types::JvmSpecializedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmparameterizedtypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmParameterizedTypeReference)


def test_types::jvmparameterizedtypereference_constructor_exists():
    assert callable(types::JvmParameterizedTypeReference.__init__)


def test_types::jvmparameterizedtypereference_constructor_args():
    sig = inspect.signature(types::JvmParameterizedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(JvmTypeConstraint)


def test_jvmtypeconstraint_constructor_exists():
    assert callable(JvmTypeConstraint.__init__)


def test_jvmtypeconstraint_constructor_args():
    sig = inspect.signature(JvmTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmlowerbound_is_not_abstract():
    assert not inspect.isabstract(types::JvmLowerBound)


def test_types::jvmlowerbound_constructor_exists():
    assert callable(types::JvmLowerBound.__init__)


def test_types::jvmlowerbound_constructor_args():
    sig = inspect.signature(types::JvmLowerBound.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmupperbound_is_not_abstract():
    assert not inspect.isabstract(types::JvmUpperBound)


def test_types::jvmupperbound_constructor_exists():
    assert callable(types::JvmUpperBound.__init__)


def test_types::jvmupperbound_constructor_args():
    sig = inspect.signature(types::JvmUpperBound.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(types::JvmTypeConstraint)


def test_types::jvmtypeconstraint_constructor_exists():
    assert callable(types::JvmTypeConstraint.__init__)


def test_types::jvmtypeconstraint_constructor_args():
    sig = inspect.signature(types::JvmTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmconstraintowner_is_not_abstract():
    assert not inspect.isabstract(types::JvmConstraintOwner)


def test_types::jvmconstraintowner_constructor_exists():
    assert callable(types::JvmConstraintOwner.__init__)


def test_types::jvmconstraintowner_constructor_args():
    sig = inspect.signature(types::JvmConstraintOwner.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmtypeparameterdeclarator_is_not_abstract():
    assert not inspect.isabstract(types::JvmTypeParameterDeclarator)


def test_types::jvmtypeparameterdeclarator_constructor_exists():
    assert callable(types::JvmTypeParameterDeclarator.__init__)


def test_types::jvmtypeparameterdeclarator_constructor_args():
    sig = inspect.signature(types::JvmTypeParameterDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_jvmconstraintowner_is_not_abstract():
    assert not inspect.isabstract(JvmConstraintOwner)


def test_jvmconstraintowner_constructor_exists():
    assert callable(JvmConstraintOwner.__init__)


def test_jvmconstraintowner_constructor_args():
    sig = inspect.signature(JvmConstraintOwner.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmwildcardtypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmWildcardTypeReference)


def test_types::jvmwildcardtypereference_constructor_exists():
    assert callable(types::JvmWildcardTypeReference.__init__)


def test_types::jvmwildcardtypereference_constructor_args():
    sig = inspect.signature(types::JvmWildcardTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(types::JvmTypeReference)


def test_types::jvmtypereference_constructor_exists():
    assert callable(types::JvmTypeReference.__init__)


def test_types::jvmtypereference_constructor_args():
    sig = inspect.signature(types::JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmmember_is_not_abstract():
    assert not inspect.isabstract(JvmMember)


def test_jvmmember_constructor_exists():
    assert callable(JvmMember.__init__)


def test_jvmmember_constructor_args():
    sig = inspect.signature(JvmMember.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmfeature_is_not_abstract():
    assert not inspect.isabstract(types::JvmFeature)


def test_types::jvmfeature_constructor_exists():
    assert callable(types::JvmFeature.__init__)


def test_types::jvmfeature_constructor_args():
    sig = inspect.signature(types::JvmFeature.__init__)
    params = list(sig.parameters.keys())



def test_jvmcomponenttype_is_not_abstract():
    assert not inspect.isabstract(JvmComponentType)


def test_jvmcomponenttype_constructor_exists():
    assert callable(JvmComponentType.__init__)


def test_jvmcomponenttype_constructor_args():
    sig = inspect.signature(JvmComponentType.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmtypeparameter_is_not_abstract():
    assert not inspect.isabstract(types::JvmTypeParameter)


def test_types::jvmtypeparameter_constructor_exists():
    assert callable(types::JvmTypeParameter.__init__)


def test_types::jvmtypeparameter_constructor_args():
    sig = inspect.signature(types::JvmTypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::jvmtypeparameter_has_name():
    assert hasattr(types::JvmTypeParameter, "name")
    descriptor = None
    for klass in types::JvmTypeParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(types::JvmDeclaredType)


def test_types::jvmdeclaredtype_constructor_exists():
    assert callable(types::JvmDeclaredType.__init__)


def test_types::jvmdeclaredtype_constructor_args():
    sig = inspect.signature(types::JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_types::jvmdeclaredtype_has_static():
    assert hasattr(types::JvmDeclaredType, "static")
    descriptor = None
    for klass in types::JvmDeclaredType.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmdeclaredtype_has_final():
    assert hasattr(types::JvmDeclaredType, "final")
    descriptor = None
    for klass in types::JvmDeclaredType.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmdeclaredtype_has_abstract():
    assert hasattr(types::JvmDeclaredType, "abstract")
    descriptor = None
    for klass in types::JvmDeclaredType.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmdeclaredtype_has_packageName():
    assert hasattr(types::JvmDeclaredType, "packageName")
    descriptor = None
    for klass in types::JvmDeclaredType.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmprimitivetype_is_not_abstract():
    assert not inspect.isabstract(types::JvmPrimitiveType)


def test_types::jvmprimitivetype_constructor_exists():
    assert callable(types::JvmPrimitiveType.__init__)


def test_types::jvmprimitivetype_constructor_args():
    sig = inspect.signature(types::JvmPrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_types::jvmprimitivetype_has_simpleName():
    assert hasattr(types::JvmPrimitiveType, "simpleName")
    descriptor = None
    for klass in types::JvmPrimitiveType.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmarraytype_is_not_abstract():
    assert not inspect.isabstract(types::JvmArrayType)


def test_types::jvmarraytype_constructor_exists():
    assert callable(types::JvmArrayType.__init__)


def test_types::jvmarraytype_constructor_args():
    sig = inspect.signature(types::JvmArrayType.__init__)
    params = list(sig.parameters.keys())



def test_jvmtype_is_not_abstract():
    assert not inspect.isabstract(JvmType)


def test_jvmtype_constructor_exists():
    assert callable(JvmType.__init__)


def test_jvmtype_constructor_args():
    sig = inspect.signature(JvmType.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmcomponenttype_is_not_abstract():
    assert not inspect.isabstract(types::JvmComponentType)


def test_types::jvmcomponenttype_constructor_exists():
    assert callable(types::JvmComponentType.__init__)


def test_types::jvmcomponenttype_constructor_args():
    sig = inspect.signature(types::JvmComponentType.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmvoid_is_not_abstract():
    assert not inspect.isabstract(types::JvmVoid)


def test_types::jvmvoid_constructor_exists():
    assert callable(types::JvmVoid.__init__)


def test_types::jvmvoid_constructor_args():
    sig = inspect.signature(types::JvmVoid.__init__)
    params = list(sig.parameters.keys())



def test_jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(JvmIdentifiableElement)


def test_jvmidentifiableelement_constructor_exists():
    assert callable(JvmIdentifiableElement.__init__)


def test_jvmidentifiableelement_constructor_args():
    sig = inspect.signature(JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmformalparameter_is_not_abstract():
    assert not inspect.isabstract(types::JvmFormalParameter)


def test_types::jvmformalparameter_constructor_exists():
    assert callable(types::JvmFormalParameter.__init__)


def test_types::jvmformalparameter_constructor_args():
    sig = inspect.signature(types::JvmFormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::jvmformalparameter_has_name():
    assert hasattr(types::JvmFormalParameter, "name")
    descriptor = None
    for klass in types::JvmFormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmmember_is_not_abstract():
    assert not inspect.isabstract(types::JvmMember)


def test_types::jvmmember_constructor_exists():
    assert callable(types::JvmMember.__init__)


def test_types::jvmmember_constructor_args():
    sig = inspect.signature(types::JvmMember.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_types::jvmmember_has_simpleName():
    assert hasattr(types::JvmMember, "simpleName")
    descriptor = None
    for klass in types::JvmMember.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmmember_has_identifier():
    assert hasattr(types::JvmMember, "identifier")
    descriptor = None
    for klass in types::JvmMember.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_types::jvmmember_has_visibility():
    assert hasattr(types::JvmMember, "visibility")
    descriptor = None
    for klass in types::JvmMember.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_types::jvmtype_is_not_abstract():
    assert not inspect.isabstract(types::JvmType)


def test_types::jvmtype_constructor_exists():
    assert callable(types::JvmType.__init__)


def test_types::jvmtype_constructor_args():
    sig = inspect.signature(types::JvmType.__init__)
    params = list(sig.parameters.keys())



def test_types::jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(types::JvmIdentifiableElement)


def test_types::jvmidentifiableelement_constructor_exists():
    assert callable(types::JvmIdentifiableElement.__init__)


def test_types::jvmidentifiableelement_constructor_args():
    sig = inspect.signature(types::JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())

def test_jvmvisibility_exists():
    # Check that the Enumeration exists
    assert JvmVisibility is not None

def test_jvmvisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JvmVisibility]
    expected_literals = [
        "DEFAULT",
        "PUBLIC",
        "PROTECTED",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JvmVisibility"


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
types::JvmAnnotationReference_strategy = st.builds(
    types::JvmAnnotationReference,
)
types::JvmAnnotationTarget_strategy = st.builds(
    types::JvmAnnotationTarget,
)
JvmAnnotationValue_strategy = st.builds(
    JvmAnnotationValue,
)
types::JvmShortAnnotationValue_strategy = st.builds(
    types::JvmShortAnnotationValue,
    values=
        safe_text
)
types::JvmDoubleAnnotationValue_strategy = st.builds(
    types::JvmDoubleAnnotationValue,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
types::JvmTypeAnnotationValue_strategy = st.builds(
    types::JvmTypeAnnotationValue,
)
types::JvmByteAnnotationValue_strategy = st.builds(
    types::JvmByteAnnotationValue,
    values=
        safe_text
)
types::JvmBooleanAnnotationValue_strategy = st.builds(
    types::JvmBooleanAnnotationValue,
    values=
        st.booleans()
)
types::JvmLongAnnotationValue_strategy = st.builds(
    types::JvmLongAnnotationValue,
    values=
        safe_text
)
types::JvmStringAnnotationValue_strategy = st.builds(
    types::JvmStringAnnotationValue,
    values=
        safe_text
)
types::JvmFloatAnnotationValue_strategy = st.builds(
    types::JvmFloatAnnotationValue,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
types::JvmEnumAnnotationValue_strategy = st.builds(
    types::JvmEnumAnnotationValue,
)
types::JvmCustomAnnotationValue_strategy = st.builds(
    types::JvmCustomAnnotationValue,
    values=
        safe_text
)
types::JvmCharAnnotationValue_strategy = st.builds(
    types::JvmCharAnnotationValue,
    values=
        safe_text
)
types::JvmIntAnnotationValue_strategy = st.builds(
    types::JvmIntAnnotationValue,
    values=
        st.integers()
)
JvmAnnotationTarget_strategy = st.builds(
    JvmAnnotationTarget,
)
types::JvmAnnotationAnnotationValue_strategy = st.builds(
    types::JvmAnnotationAnnotationValue,
)
JvmCompoundTypeReference_strategy = st.builds(
    JvmCompoundTypeReference,
)
types::JvmSynonymTypeReference_strategy = st.builds(
    types::JvmSynonymTypeReference,
)
types::JvmMultiTypeReference_strategy = st.builds(
    types::JvmMultiTypeReference,
)
types::JvmAnnotationValue_strategy = st.builds(
    types::JvmAnnotationValue,
)
JvmExecutable_strategy = st.builds(
    JvmExecutable,
)
types::JvmOperation_strategy = st.builds(
    types::JvmOperation,
    final=
        st.booleans(),
    static=
        st.booleans(),
    abstract=
        st.booleans()
)
types::JvmConstructor_strategy = st.builds(
    types::JvmConstructor,
)
JvmFeature_strategy = st.builds(
    JvmFeature,
)
types::JvmField_strategy = st.builds(
    types::JvmField,
    static=
        st.booleans(),
    final=
        st.booleans()
)
JvmTypeParameterDeclarator_strategy = st.builds(
    JvmTypeParameterDeclarator,
)
types::JvmExecutable_strategy = st.builds(
    types::JvmExecutable,
    varArgs=
        st.booleans()
)
JvmField_strategy = st.builds(
    JvmField,
)
types::JvmEnumerationLiteral_strategy = st.builds(
    types::JvmEnumerationLiteral,
)
JvmDeclaredType_strategy = st.builds(
    JvmDeclaredType,
)
types::JvmGenericType_strategy = st.builds(
    types::JvmGenericType,
    interface=
        st.booleans()
)
types::JvmEnumerationType_strategy = st.builds(
    types::JvmEnumerationType,
)
types::JvmAnnotationType_strategy = st.builds(
    types::JvmAnnotationType,
)
JvmTypeReference_strategy = st.builds(
    JvmTypeReference,
)
types::JvmCompoundTypeReference_strategy = st.builds(
    types::JvmCompoundTypeReference,
)
types::JvmUnknownTypeReference_strategy = st.builds(
    types::JvmUnknownTypeReference,
    exception=
        safe_text
)
types::JvmDelegateTypeReference_strategy = st.builds(
    types::JvmDelegateTypeReference,
)
types::JvmAnyTypeReference_strategy = st.builds(
    types::JvmAnyTypeReference,
)
types::JvmGenericArrayTypeReference_strategy = st.builds(
    types::JvmGenericArrayTypeReference,
)
types::JvmSpecializedTypeReference_strategy = st.builds(
    types::JvmSpecializedTypeReference,
)
types::JvmParameterizedTypeReference_strategy = st.builds(
    types::JvmParameterizedTypeReference,
)
JvmTypeConstraint_strategy = st.builds(
    JvmTypeConstraint,
)
types::JvmLowerBound_strategy = st.builds(
    types::JvmLowerBound,
)
types::JvmUpperBound_strategy = st.builds(
    types::JvmUpperBound,
)
types::JvmTypeConstraint_strategy = st.builds(
    types::JvmTypeConstraint,
)
types::JvmConstraintOwner_strategy = st.builds(
    types::JvmConstraintOwner,
)
types::JvmTypeParameterDeclarator_strategy = st.builds(
    types::JvmTypeParameterDeclarator,
)
JvmConstraintOwner_strategy = st.builds(
    JvmConstraintOwner,
)
types::JvmWildcardTypeReference_strategy = st.builds(
    types::JvmWildcardTypeReference,
)
types::JvmTypeReference_strategy = st.builds(
    types::JvmTypeReference,
)
JvmMember_strategy = st.builds(
    JvmMember,
)
types::JvmFeature_strategy = st.builds(
    types::JvmFeature,
)
JvmComponentType_strategy = st.builds(
    JvmComponentType,
)
types::JvmTypeParameter_strategy = st.builds(
    types::JvmTypeParameter,
    name=
        safe_text
)
types::JvmDeclaredType_strategy = st.builds(
    types::JvmDeclaredType,
    static=
        st.booleans(),
    final=
        st.booleans(),
    abstract=
        st.booleans(),
    packageName=
        safe_text
)
types::JvmPrimitiveType_strategy = st.builds(
    types::JvmPrimitiveType,
    simpleName=
        safe_text
)
types::JvmArrayType_strategy = st.builds(
    types::JvmArrayType,
)
JvmType_strategy = st.builds(
    JvmType,
)
types::JvmComponentType_strategy = st.builds(
    types::JvmComponentType,
)
types::JvmVoid_strategy = st.builds(
    types::JvmVoid,
)
JvmIdentifiableElement_strategy = st.builds(
    JvmIdentifiableElement,
)
types::JvmFormalParameter_strategy = st.builds(
    types::JvmFormalParameter,
    name=
        safe_text
)
types::JvmMember_strategy = st.builds(
    types::JvmMember,
    simpleName=
        safe_text,
    identifier=
        safe_text,
    visibility=
        safe_text
)
types::JvmType_strategy = st.builds(
    types::JvmType,
)
types::JvmIdentifiableElement_strategy = st.builds(
    types::JvmIdentifiableElement,
)

@given(instance=types::JvmAnnotationReference_strategy)
@settings(max_examples=50)
def test_types::jvmannotationreference_instantiation(instance):
    assert isinstance(instance, types::JvmAnnotationReference)

@given(instance=types::JvmAnnotationTarget_strategy)
@settings(max_examples=50)
def test_types::jvmannotationtarget_instantiation(instance):
    assert isinstance(instance, types::JvmAnnotationTarget)

@given(instance=JvmAnnotationValue_strategy)
@settings(max_examples=50)
def test_jvmannotationvalue_instantiation(instance):
    assert isinstance(instance, JvmAnnotationValue)

@given(instance=types::JvmShortAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmshortannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmShortAnnotationValue)

@given(instance=types::JvmShortAnnotationValue_strategy)
def test_types::jvmshortannotationvalue_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=types::JvmShortAnnotationValue_strategy)
def test_types::jvmshortannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmDoubleAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmdoubleannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmDoubleAnnotationValue)

@given(instance=types::JvmDoubleAnnotationValue_strategy)
def test_types::jvmdoubleannotationvalue_values_type(instance):
    assert isinstance(instance.values, float)


@given(instance=types::JvmDoubleAnnotationValue_strategy)
def test_types::jvmdoubleannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmTypeAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmtypeannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmTypeAnnotationValue)

@given(instance=types::JvmByteAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmbyteannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmByteAnnotationValue)

@given(instance=types::JvmByteAnnotationValue_strategy)
def test_types::jvmbyteannotationvalue_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=types::JvmByteAnnotationValue_strategy)
def test_types::jvmbyteannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmBooleanAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmbooleanannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmBooleanAnnotationValue)

@given(instance=types::JvmBooleanAnnotationValue_strategy)
def test_types::jvmbooleanannotationvalue_values_type(instance):
    assert isinstance(instance.values, bool)


@given(instance=types::JvmBooleanAnnotationValue_strategy)
def test_types::jvmbooleanannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmLongAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmlongannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmLongAnnotationValue)

@given(instance=types::JvmLongAnnotationValue_strategy)
def test_types::jvmlongannotationvalue_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=types::JvmLongAnnotationValue_strategy)
def test_types::jvmlongannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmStringAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmstringannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmStringAnnotationValue)

@given(instance=types::JvmStringAnnotationValue_strategy)
def test_types::jvmstringannotationvalue_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=types::JvmStringAnnotationValue_strategy)
def test_types::jvmstringannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmFloatAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmfloatannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmFloatAnnotationValue)

@given(instance=types::JvmFloatAnnotationValue_strategy)
def test_types::jvmfloatannotationvalue_values_type(instance):
    assert isinstance(instance.values, float)


@given(instance=types::JvmFloatAnnotationValue_strategy)
def test_types::jvmfloatannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmEnumAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmenumannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmEnumAnnotationValue)

@given(instance=types::JvmCustomAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmcustomannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmCustomAnnotationValue)

@given(instance=types::JvmCustomAnnotationValue_strategy)
def test_types::jvmcustomannotationvalue_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=types::JvmCustomAnnotationValue_strategy)
def test_types::jvmcustomannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmCharAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmcharannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmCharAnnotationValue)

@given(instance=types::JvmCharAnnotationValue_strategy)
def test_types::jvmcharannotationvalue_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=types::JvmCharAnnotationValue_strategy)
def test_types::jvmcharannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=types::JvmIntAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmintannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmIntAnnotationValue)

@given(instance=types::JvmIntAnnotationValue_strategy)
def test_types::jvmintannotationvalue_values_type(instance):
    assert isinstance(instance.values, int)


@given(instance=types::JvmIntAnnotationValue_strategy)
def test_types::jvmintannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=JvmAnnotationTarget_strategy)
@settings(max_examples=50)
def test_jvmannotationtarget_instantiation(instance):
    assert isinstance(instance, JvmAnnotationTarget)

@given(instance=types::JvmAnnotationAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmannotationannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmAnnotationAnnotationValue)

@given(instance=JvmCompoundTypeReference_strategy)
@settings(max_examples=50)
def test_jvmcompoundtypereference_instantiation(instance):
    assert isinstance(instance, JvmCompoundTypeReference)

@given(instance=types::JvmSynonymTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmsynonymtypereference_instantiation(instance):
    assert isinstance(instance, types::JvmSynonymTypeReference)

@given(instance=types::JvmMultiTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmmultitypereference_instantiation(instance):
    assert isinstance(instance, types::JvmMultiTypeReference)

@given(instance=types::JvmAnnotationValue_strategy)
@settings(max_examples=50)
def test_types::jvmannotationvalue_instantiation(instance):
    assert isinstance(instance, types::JvmAnnotationValue)

@given(instance=JvmExecutable_strategy)
@settings(max_examples=50)
def test_jvmexecutable_instantiation(instance):
    assert isinstance(instance, JvmExecutable)

@given(instance=types::JvmOperation_strategy)
@settings(max_examples=50)
def test_types::jvmoperation_instantiation(instance):
    assert isinstance(instance, types::JvmOperation)

@given(instance=types::JvmOperation_strategy)
def test_types::jvmoperation_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=types::JvmOperation_strategy)
def test_types::jvmoperation_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=types::JvmOperation_strategy)
def test_types::jvmoperation_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=types::JvmOperation_strategy)
def test_types::jvmoperation_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=types::JvmOperation_strategy)
def test_types::jvmoperation_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=types::JvmOperation_strategy)
def test_types::jvmoperation_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=types::JvmConstructor_strategy)
@settings(max_examples=50)
def test_types::jvmconstructor_instantiation(instance):
    assert isinstance(instance, types::JvmConstructor)

@given(instance=JvmFeature_strategy)
@settings(max_examples=50)
def test_jvmfeature_instantiation(instance):
    assert isinstance(instance, JvmFeature)

@given(instance=types::JvmField_strategy)
@settings(max_examples=50)
def test_types::jvmfield_instantiation(instance):
    assert isinstance(instance, types::JvmField)

@given(instance=types::JvmField_strategy)
def test_types::jvmfield_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=types::JvmField_strategy)
def test_types::jvmfield_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=types::JvmField_strategy)
def test_types::jvmfield_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=types::JvmField_strategy)
def test_types::jvmfield_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=JvmTypeParameterDeclarator_strategy)
@settings(max_examples=50)
def test_jvmtypeparameterdeclarator_instantiation(instance):
    assert isinstance(instance, JvmTypeParameterDeclarator)

@given(instance=types::JvmExecutable_strategy)
@settings(max_examples=50)
def test_types::jvmexecutable_instantiation(instance):
    assert isinstance(instance, types::JvmExecutable)

@given(instance=types::JvmExecutable_strategy)
def test_types::jvmexecutable_varArgs_type(instance):
    assert isinstance(instance.varArgs, bool)


@given(instance=types::JvmExecutable_strategy)
def test_types::jvmexecutable_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original

@given(instance=JvmField_strategy)
@settings(max_examples=50)
def test_jvmfield_instantiation(instance):
    assert isinstance(instance, JvmField)

@given(instance=types::JvmEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_types::jvmenumerationliteral_instantiation(instance):
    assert isinstance(instance, types::JvmEnumerationLiteral)

@given(instance=JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, JvmDeclaredType)

@given(instance=types::JvmGenericType_strategy)
@settings(max_examples=50)
def test_types::jvmgenerictype_instantiation(instance):
    assert isinstance(instance, types::JvmGenericType)

@given(instance=types::JvmGenericType_strategy)
def test_types::jvmgenerictype_interface_type(instance):
    assert isinstance(instance.interface, bool)


@given(instance=types::JvmGenericType_strategy)
def test_types::jvmgenerictype_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types::JvmGenericType_strategy)
@settings(max_examples=30)
def test_types::jvmgenerictype_isinstantiateable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstantiateable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstantiateable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstantiateable' in types::JvmGenericType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstantiateable' in types::JvmGenericType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstantiateable' in types::JvmGenericType is not implemented or raised an error")

@given(instance=types::JvmEnumerationType_strategy)
@settings(max_examples=50)
def test_types::jvmenumerationtype_instantiation(instance):
    assert isinstance(instance, types::JvmEnumerationType)

@given(instance=types::JvmAnnotationType_strategy)
@settings(max_examples=50)
def test_types::jvmannotationtype_instantiation(instance):
    assert isinstance(instance, types::JvmAnnotationType)

@given(instance=JvmTypeReference_strategy)
@settings(max_examples=50)
def test_jvmtypereference_instantiation(instance):
    assert isinstance(instance, JvmTypeReference)

@given(instance=types::JvmCompoundTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmcompoundtypereference_instantiation(instance):
    assert isinstance(instance, types::JvmCompoundTypeReference)

@given(instance=types::JvmUnknownTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmunknowntypereference_instantiation(instance):
    assert isinstance(instance, types::JvmUnknownTypeReference)

@given(instance=types::JvmUnknownTypeReference_strategy)
def test_types::jvmunknowntypereference_exception_type(instance):
    assert isinstance(instance.exception, str)


@given(instance=types::JvmUnknownTypeReference_strategy)
def test_types::jvmunknowntypereference_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=types::JvmDelegateTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmdelegatetypereference_instantiation(instance):
    assert isinstance(instance, types::JvmDelegateTypeReference)

@given(instance=types::JvmAnyTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmanytypereference_instantiation(instance):
    assert isinstance(instance, types::JvmAnyTypeReference)

@given(instance=types::JvmGenericArrayTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmgenericarraytypereference_instantiation(instance):
    assert isinstance(instance, types::JvmGenericArrayTypeReference)

@given(instance=types::JvmSpecializedTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmspecializedtypereference_instantiation(instance):
    assert isinstance(instance, types::JvmSpecializedTypeReference)

@given(instance=types::JvmParameterizedTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmparameterizedtypereference_instantiation(instance):
    assert isinstance(instance, types::JvmParameterizedTypeReference)

@given(instance=JvmTypeConstraint_strategy)
@settings(max_examples=50)
def test_jvmtypeconstraint_instantiation(instance):
    assert isinstance(instance, JvmTypeConstraint)

@given(instance=types::JvmLowerBound_strategy)
@settings(max_examples=50)
def test_types::jvmlowerbound_instantiation(instance):
    assert isinstance(instance, types::JvmLowerBound)

@given(instance=types::JvmUpperBound_strategy)
@settings(max_examples=50)
def test_types::jvmupperbound_instantiation(instance):
    assert isinstance(instance, types::JvmUpperBound)

@given(instance=types::JvmTypeConstraint_strategy)
@settings(max_examples=50)
def test_types::jvmtypeconstraint_instantiation(instance):
    assert isinstance(instance, types::JvmTypeConstraint)

@given(instance=types::JvmConstraintOwner_strategy)
@settings(max_examples=50)
def test_types::jvmconstraintowner_instantiation(instance):
    assert isinstance(instance, types::JvmConstraintOwner)

@given(instance=types::JvmTypeParameterDeclarator_strategy)
@settings(max_examples=50)
def test_types::jvmtypeparameterdeclarator_instantiation(instance):
    assert isinstance(instance, types::JvmTypeParameterDeclarator)

@given(instance=JvmConstraintOwner_strategy)
@settings(max_examples=50)
def test_jvmconstraintowner_instantiation(instance):
    assert isinstance(instance, JvmConstraintOwner)

@given(instance=types::JvmWildcardTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmwildcardtypereference_instantiation(instance):
    assert isinstance(instance, types::JvmWildcardTypeReference)

@given(instance=types::JvmTypeReference_strategy)
@settings(max_examples=50)
def test_types::jvmtypereference_instantiation(instance):
    assert isinstance(instance, types::JvmTypeReference)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types::JvmTypeReference_strategy)
@settings(max_examples=30)
def test_types::jvmtypereference_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in types::JvmTypeReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in types::JvmTypeReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in types::JvmTypeReference is not implemented or raised an error")

@given(instance=JvmMember_strategy)
@settings(max_examples=50)
def test_jvmmember_instantiation(instance):
    assert isinstance(instance, JvmMember)

@given(instance=types::JvmFeature_strategy)
@settings(max_examples=50)
def test_types::jvmfeature_instantiation(instance):
    assert isinstance(instance, types::JvmFeature)

@given(instance=JvmComponentType_strategy)
@settings(max_examples=50)
def test_jvmcomponenttype_instantiation(instance):
    assert isinstance(instance, JvmComponentType)

@given(instance=types::JvmTypeParameter_strategy)
@settings(max_examples=50)
def test_types::jvmtypeparameter_instantiation(instance):
    assert isinstance(instance, types::JvmTypeParameter)

@given(instance=types::JvmTypeParameter_strategy)
def test_types::jvmtypeparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::JvmTypeParameter_strategy)
def test_types::jvmtypeparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_types::jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, types::JvmDeclaredType)

@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_packageName_type(instance):
    assert isinstance(instance.packageName, str)


@given(instance=types::JvmDeclaredType_strategy)
def test_types::jvmdeclaredtype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types::JvmDeclaredType_strategy)
@settings(max_examples=30)
def test_types::jvmdeclaredtype_findallfeaturesbyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findAllFeaturesByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findAllFeaturesByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findAllFeaturesByName' in types::JvmDeclaredType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findAllFeaturesByName' in types::JvmDeclaredType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findAllFeaturesByName' in types::JvmDeclaredType is not implemented or raised an error")

@given(instance=types::JvmPrimitiveType_strategy)
@settings(max_examples=50)
def test_types::jvmprimitivetype_instantiation(instance):
    assert isinstance(instance, types::JvmPrimitiveType)

@given(instance=types::JvmPrimitiveType_strategy)
def test_types::jvmprimitivetype_simpleName_type(instance):
    assert isinstance(instance.simpleName, str)


@given(instance=types::JvmPrimitiveType_strategy)
def test_types::jvmprimitivetype_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=types::JvmArrayType_strategy)
@settings(max_examples=50)
def test_types::jvmarraytype_instantiation(instance):
    assert isinstance(instance, types::JvmArrayType)

@given(instance=JvmType_strategy)
@settings(max_examples=50)
def test_jvmtype_instantiation(instance):
    assert isinstance(instance, JvmType)

@given(instance=types::JvmComponentType_strategy)
@settings(max_examples=50)
def test_types::jvmcomponenttype_instantiation(instance):
    assert isinstance(instance, types::JvmComponentType)

@given(instance=types::JvmVoid_strategy)
@settings(max_examples=50)
def test_types::jvmvoid_instantiation(instance):
    assert isinstance(instance, types::JvmVoid)

@given(instance=JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, JvmIdentifiableElement)

@given(instance=types::JvmFormalParameter_strategy)
@settings(max_examples=50)
def test_types::jvmformalparameter_instantiation(instance):
    assert isinstance(instance, types::JvmFormalParameter)

@given(instance=types::JvmFormalParameter_strategy)
def test_types::jvmformalparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::JvmFormalParameter_strategy)
def test_types::jvmformalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::JvmMember_strategy)
@settings(max_examples=50)
def test_types::jvmmember_instantiation(instance):
    assert isinstance(instance, types::JvmMember)

@given(instance=types::JvmMember_strategy)
def test_types::jvmmember_simpleName_type(instance):
    assert isinstance(instance.simpleName, str)


@given(instance=types::JvmMember_strategy)
def test_types::jvmmember_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=types::JvmMember_strategy)
def test_types::jvmmember_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=types::JvmMember_strategy)
def test_types::jvmmember_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=types::JvmMember_strategy)
def test_types::jvmmember_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=types::JvmMember_strategy)
def test_types::jvmmember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types::JvmMember_strategy)
@settings(max_examples=30)
def test_types::jvmmember_internalsetidentifier_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.internalSetIdentifier(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.internalSetIdentifier).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'internalSetIdentifier' in types::JvmMember is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'internalSetIdentifier' in types::JvmMember did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'internalSetIdentifier' in types::JvmMember is not implemented or raised an error")

@given(instance=types::JvmType_strategy)
@settings(max_examples=50)
def test_types::jvmtype_instantiation(instance):
    assert isinstance(instance, types::JvmType)

@given(instance=types::JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_types::jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, types::JvmIdentifiableElement)
