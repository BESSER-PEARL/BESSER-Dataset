import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ocl_type_ESignal,
    ECollectionType,
    ocl_type_ESequenceType,
    ocl_type_EBagType,
    ocl_type_ESetType,
    ocl_type_EOrderedSetType,
    EDataType,
    ocl_type_ETupleType,
    ocl_type_EPrimitiveType,
    ocl_type_ECollectionType,
    ESignal,
    ocl_type_EClassifier,
    EFeatureCallExp,
    ocl_exp_ENavigationCallExp,
    ELiteralExp,
    ocl_exp_EPrimitiveType,
    ENumericLiteralExp,
    ocl_exp_EIntegerLiteralExp,
    EOperationCallExp,
    ocl_exp_EOclExpression,
    ELoopExp,
    ocl_exp_EIteratorExp,
    ocl_exp_EVariable,
    EPrimitiveType,
    ocl_exp_EBooleanLiteralExp,
    ocl_exp_ENumericLiteralExp,
    ENavigationCallExp,
    ocl_exp_EPropertyCallExp,
    ocl_exp_EAssociationClassCallExp,
    ocl_exp_EStringLiteralExp,
    ocl_exp_EOperationCallExp,
    EVariable,
    EOclExpression,
    ocl_exp_ELiteralExp,
    ocl_exp_ECallExp,
    ocl_exp_EVariableExp,
    ocl_dm_EAttribute,
    ocl_dm_EDataModel,
    EEntity,
    ocl_dm_EAssociationEnd,
    EAttribute,
    EAssociationEnd,
    EClassifier,
    ocl_type_EVoidType,
    ocl_type_EAnyType,
    ocl_type_EMessageType,
    ocl_type_EDataType,
    ocl_type_EInvalidType,
    ECallExp,
    ocl_exp_EFeatureCallExp,
    ocl_exp_ELoopExp,
    ocl_exp_ETypeExp,
    ocl_dm_EEntity,
    EIteratorKind,
    EOperator,
    EMultiplicity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl_type_esignal_is_not_abstract():
    assert not inspect.isabstract(ocl_type_ESignal)


def test_ocl_type_esignal_constructor_exists():
    assert callable(ocl_type_ESignal.__init__)


def test_ocl_type_esignal_constructor_args():
    sig = inspect.signature(ocl_type_ESignal.__init__)
    params = list(sig.parameters.keys())



def test_ecollectiontype_is_not_abstract():
    assert not inspect.isabstract(ECollectionType)


def test_ecollectiontype_constructor_exists():
    assert callable(ECollectionType.__init__)


def test_ecollectiontype_constructor_args():
    sig = inspect.signature(ECollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_esequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_ESequenceType)


def test_ocl_type_esequencetype_constructor_exists():
    assert callable(ocl_type_ESequenceType.__init__)


def test_ocl_type_esequencetype_constructor_args():
    sig = inspect.signature(ocl_type_ESequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_ebagtype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EBagType)


def test_ocl_type_ebagtype_constructor_exists():
    assert callable(ocl_type_EBagType.__init__)


def test_ocl_type_ebagtype_constructor_args():
    sig = inspect.signature(ocl_type_EBagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_esettype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_ESetType)


def test_ocl_type_esettype_constructor_exists():
    assert callable(ocl_type_ESetType.__init__)


def test_ocl_type_esettype_constructor_args():
    sig = inspect.signature(ocl_type_ESetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_eorderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EOrderedSetType)


def test_ocl_type_eorderedsettype_constructor_exists():
    assert callable(ocl_type_EOrderedSetType.__init__)


def test_ocl_type_eorderedsettype_constructor_args():
    sig = inspect.signature(ocl_type_EOrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_etupletype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_ETupleType)


def test_ocl_type_etupletype_constructor_exists():
    assert callable(ocl_type_ETupleType.__init__)


def test_ocl_type_etupletype_constructor_args():
    sig = inspect.signature(ocl_type_ETupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_eprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EPrimitiveType)


def test_ocl_type_eprimitivetype_constructor_exists():
    assert callable(ocl_type_EPrimitiveType.__init__)


def test_ocl_type_eprimitivetype_constructor_args():
    sig = inspect.signature(ocl_type_EPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_ecollectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_ECollectionType)


def test_ocl_type_ecollectiontype_constructor_exists():
    assert callable(ocl_type_ECollectionType.__init__)


def test_ocl_type_ecollectiontype_constructor_args():
    sig = inspect.signature(ocl_type_ECollectionType.__init__)
    params = list(sig.parameters.keys())



def test_esignal_is_not_abstract():
    assert not inspect.isabstract(ESignal)


def test_esignal_constructor_exists():
    assert callable(ESignal.__init__)


def test_esignal_constructor_args():
    sig = inspect.signature(ESignal.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_eclassifier_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EClassifier)


def test_ocl_type_eclassifier_constructor_exists():
    assert callable(ocl_type_EClassifier.__init__)


def test_ocl_type_eclassifier_constructor_args():
    sig = inspect.signature(ocl_type_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_efeaturecallexp_is_not_abstract():
    assert not inspect.isabstract(EFeatureCallExp)


def test_efeaturecallexp_constructor_exists():
    assert callable(EFeatureCallExp.__init__)


def test_efeaturecallexp_constructor_args():
    sig = inspect.signature(EFeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_enavigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_ENavigationCallExp)


def test_ocl_exp_enavigationcallexp_constructor_exists():
    assert callable(ocl_exp_ENavigationCallExp.__init__)


def test_ocl_exp_enavigationcallexp_constructor_args():
    sig = inspect.signature(ocl_exp_ENavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_eliteralexp_is_not_abstract():
    assert not inspect.isabstract(ELiteralExp)


def test_eliteralexp_constructor_exists():
    assert callable(ELiteralExp.__init__)


def test_eliteralexp_constructor_args():
    sig = inspect.signature(ELiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EPrimitiveType)


def test_ocl_exp_eprimitivetype_constructor_exists():
    assert callable(ocl_exp_EPrimitiveType.__init__)


def test_ocl_exp_eprimitivetype_constructor_args():
    sig = inspect.signature(ocl_exp_EPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_enumericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ENumericLiteralExp)


def test_enumericliteralexp_constructor_exists():
    assert callable(ENumericLiteralExp.__init__)


def test_enumericliteralexp_constructor_args():
    sig = inspect.signature(ENumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eintegerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EIntegerLiteralExp)


def test_ocl_exp_eintegerliteralexp_constructor_exists():
    assert callable(ocl_exp_EIntegerLiteralExp.__init__)


def test_ocl_exp_eintegerliteralexp_constructor_args():
    sig = inspect.signature(ocl_exp_EIntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_ocl_exp_eintegerliteralexp_has_integerValue():
    assert hasattr(ocl_exp_EIntegerLiteralExp, "integerValue")
    descriptor = None
    for klass in ocl_exp_EIntegerLiteralExp.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_eoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(EOperationCallExp)


def test_eoperationcallexp_constructor_exists():
    assert callable(EOperationCallExp.__init__)


def test_eoperationcallexp_constructor_args():
    sig = inspect.signature(EOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eoclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EOclExpression)


def test_ocl_exp_eoclexpression_constructor_exists():
    assert callable(ocl_exp_EOclExpression.__init__)


def test_ocl_exp_eoclexpression_constructor_args():
    sig = inspect.signature(ocl_exp_EOclExpression.__init__)
    params = list(sig.parameters.keys())



def test_eloopexp_is_not_abstract():
    assert not inspect.isabstract(ELoopExp)


def test_eloopexp_constructor_exists():
    assert callable(ELoopExp.__init__)


def test_eloopexp_constructor_args():
    sig = inspect.signature(ELoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eiteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EIteratorExp)


def test_ocl_exp_eiteratorexp_constructor_exists():
    assert callable(ocl_exp_EIteratorExp.__init__)


def test_ocl_exp_eiteratorexp_constructor_args():
    sig = inspect.signature(ocl_exp_EIteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl_exp_eiteratorexp_has_kind():
    assert hasattr(ocl_exp_EIteratorExp, "kind")
    descriptor = None
    for klass in ocl_exp_EIteratorExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl_exp_evariable_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EVariable)


def test_ocl_exp_evariable_constructor_exists():
    assert callable(ocl_exp_EVariable.__init__)


def test_ocl_exp_evariable_constructor_args():
    sig = inspect.signature(ocl_exp_EVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_exp_evariable_has_name():
    assert hasattr(ocl_exp_EVariable, "name")
    descriptor = None
    for klass in ocl_exp_EVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eprimitivetype_is_not_abstract():
    assert not inspect.isabstract(EPrimitiveType)


def test_eprimitivetype_constructor_exists():
    assert callable(EPrimitiveType.__init__)


def test_eprimitivetype_constructor_args():
    sig = inspect.signature(EPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_ebooleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EBooleanLiteralExp)


def test_ocl_exp_ebooleanliteralexp_constructor_exists():
    assert callable(ocl_exp_EBooleanLiteralExp.__init__)


def test_ocl_exp_ebooleanliteralexp_constructor_args():
    sig = inspect.signature(ocl_exp_EBooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_ocl_exp_ebooleanliteralexp_has_booleanValue():
    assert hasattr(ocl_exp_EBooleanLiteralExp, "booleanValue")
    descriptor = None
    for klass in ocl_exp_EBooleanLiteralExp.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_ocl_exp_enumericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_ENumericLiteralExp)


def test_ocl_exp_enumericliteralexp_constructor_exists():
    assert callable(ocl_exp_ENumericLiteralExp.__init__)


def test_ocl_exp_enumericliteralexp_constructor_args():
    sig = inspect.signature(ocl_exp_ENumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_enavigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ENavigationCallExp)


def test_enavigationcallexp_constructor_exists():
    assert callable(ENavigationCallExp.__init__)


def test_enavigationcallexp_constructor_args():
    sig = inspect.signature(ENavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_epropertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EPropertyCallExp)


def test_ocl_exp_epropertycallexp_constructor_exists():
    assert callable(ocl_exp_EPropertyCallExp.__init__)


def test_ocl_exp_epropertycallexp_constructor_args():
    sig = inspect.signature(ocl_exp_EPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eassociationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EAssociationClassCallExp)


def test_ocl_exp_eassociationclasscallexp_constructor_exists():
    assert callable(ocl_exp_EAssociationClassCallExp.__init__)


def test_ocl_exp_eassociationclasscallexp_constructor_args():
    sig = inspect.signature(ocl_exp_EAssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_estringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EStringLiteralExp)


def test_ocl_exp_estringliteralexp_constructor_exists():
    assert callable(ocl_exp_EStringLiteralExp.__init__)


def test_ocl_exp_estringliteralexp_constructor_args():
    sig = inspect.signature(ocl_exp_EStringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_ocl_exp_estringliteralexp_has_stringValue():
    assert hasattr(ocl_exp_EStringLiteralExp, "stringValue")
    descriptor = None
    for klass in ocl_exp_EStringLiteralExp.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_ocl_exp_eoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EOperationCallExp)


def test_ocl_exp_eoperationcallexp_constructor_exists():
    assert callable(ocl_exp_EOperationCallExp.__init__)


def test_ocl_exp_eoperationcallexp_constructor_args():
    sig = inspect.signature(ocl_exp_EOperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredOperation" in params, "Missing parameter 'referredOperation'"

def test_ocl_exp_eoperationcallexp_has_referredOperation():
    assert hasattr(ocl_exp_EOperationCallExp, "referredOperation")
    descriptor = None
    for klass in ocl_exp_EOperationCallExp.__mro__:
        if "referredOperation" in klass.__dict__:
            descriptor = klass.__dict__["referredOperation"]
            break
    assert isinstance(descriptor, property)



def test_evariable_is_not_abstract():
    assert not inspect.isabstract(EVariable)


def test_evariable_constructor_exists():
    assert callable(EVariable.__init__)


def test_evariable_constructor_args():
    sig = inspect.signature(EVariable.__init__)
    params = list(sig.parameters.keys())



def test_eoclexpression_is_not_abstract():
    assert not inspect.isabstract(EOclExpression)


def test_eoclexpression_constructor_exists():
    assert callable(EOclExpression.__init__)


def test_eoclexpression_constructor_args():
    sig = inspect.signature(EOclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_ELiteralExp)


def test_ocl_exp_eliteralexp_constructor_exists():
    assert callable(ocl_exp_ELiteralExp.__init__)


def test_ocl_exp_eliteralexp_constructor_args():
    sig = inspect.signature(ocl_exp_ELiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_ecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_ECallExp)


def test_ocl_exp_ecallexp_constructor_exists():
    assert callable(ocl_exp_ECallExp.__init__)


def test_ocl_exp_ecallexp_constructor_args():
    sig = inspect.signature(ocl_exp_ECallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_evariableexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EVariableExp)


def test_ocl_exp_evariableexp_constructor_exists():
    assert callable(ocl_exp_EVariableExp.__init__)


def test_ocl_exp_evariableexp_constructor_args():
    sig = inspect.signature(ocl_exp_EVariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_dm_eattribute_is_not_abstract():
    assert not inspect.isabstract(ocl_dm_EAttribute)


def test_ocl_dm_eattribute_constructor_exists():
    assert callable(ocl_dm_EAttribute.__init__)


def test_ocl_dm_eattribute_constructor_args():
    sig = inspect.signature(ocl_dm_EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_dm_eattribute_has_type():
    assert hasattr(ocl_dm_EAttribute, "type")
    descriptor = None
    for klass in ocl_dm_EAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ocl_dm_eattribute_has_name():
    assert hasattr(ocl_dm_EAttribute, "name")
    descriptor = None
    for klass in ocl_dm_EAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_dm_edatamodel_is_not_abstract():
    assert not inspect.isabstract(ocl_dm_EDataModel)


def test_ocl_dm_edatamodel_constructor_exists():
    assert callable(ocl_dm_EDataModel.__init__)


def test_ocl_dm_edatamodel_constructor_args():
    sig = inspect.signature(ocl_dm_EDataModel.__init__)
    params = list(sig.parameters.keys())



def test_eentity_is_not_abstract():
    assert not inspect.isabstract(EEntity)


def test_eentity_constructor_exists():
    assert callable(EEntity.__init__)


def test_eentity_constructor_args():
    sig = inspect.signature(EEntity.__init__)
    params = list(sig.parameters.keys())



def test_ocl_dm_eassociationend_is_not_abstract():
    assert not inspect.isabstract(ocl_dm_EAssociationEnd)


def test_ocl_dm_eassociationend_constructor_exists():
    assert callable(ocl_dm_EAssociationEnd.__init__)


def test_ocl_dm_eassociationend_constructor_args():
    sig = inspect.signature(ocl_dm_EAssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "mult" in params, "Missing parameter 'mult'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_dm_eassociationend_has_mult():
    assert hasattr(ocl_dm_EAssociationEnd, "mult")
    descriptor = None
    for klass in ocl_dm_EAssociationEnd.__mro__:
        if "mult" in klass.__dict__:
            descriptor = klass.__dict__["mult"]
            break
    assert isinstance(descriptor, property)

def test_ocl_dm_eassociationend_has_name():
    assert hasattr(ocl_dm_EAssociationEnd, "name")
    descriptor = None
    for klass in ocl_dm_EAssociationEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_eassociationend_is_not_abstract():
    assert not inspect.isabstract(EAssociationEnd)


def test_eassociationend_constructor_exists():
    assert callable(EAssociationEnd.__init__)


def test_eassociationend_constructor_args():
    sig = inspect.signature(EAssociationEnd.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_evoidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EVoidType)


def test_ocl_type_evoidtype_constructor_exists():
    assert callable(ocl_type_EVoidType.__init__)


def test_ocl_type_evoidtype_constructor_args():
    sig = inspect.signature(ocl_type_EVoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_eanytype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EAnyType)


def test_ocl_type_eanytype_constructor_exists():
    assert callable(ocl_type_EAnyType.__init__)


def test_ocl_type_eanytype_constructor_args():
    sig = inspect.signature(ocl_type_EAnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_emessagetype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EMessageType)


def test_ocl_type_emessagetype_constructor_exists():
    assert callable(ocl_type_EMessageType.__init__)


def test_ocl_type_emessagetype_constructor_args():
    sig = inspect.signature(ocl_type_EMessageType.__init__)
    params = list(sig.parameters.keys())
    assert "referredOperation" in params, "Missing parameter 'referredOperation'"

def test_ocl_type_emessagetype_has_referredOperation():
    assert hasattr(ocl_type_EMessageType, "referredOperation")
    descriptor = None
    for klass in ocl_type_EMessageType.__mro__:
        if "referredOperation" in klass.__dict__:
            descriptor = klass.__dict__["referredOperation"]
            break
    assert isinstance(descriptor, property)



def test_ocl_type_edatatype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EDataType)


def test_ocl_type_edatatype_constructor_exists():
    assert callable(ocl_type_EDataType.__init__)


def test_ocl_type_edatatype_constructor_args():
    sig = inspect.signature(ocl_type_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_type_einvalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_type_EInvalidType)


def test_ocl_type_einvalidtype_constructor_exists():
    assert callable(ocl_type_EInvalidType.__init__)


def test_ocl_type_einvalidtype_constructor_args():
    sig = inspect.signature(ocl_type_EInvalidType.__init__)
    params = list(sig.parameters.keys())



def test_ecallexp_is_not_abstract():
    assert not inspect.isabstract(ECallExp)


def test_ecallexp_constructor_exists():
    assert callable(ECallExp.__init__)


def test_ecallexp_constructor_args():
    sig = inspect.signature(ECallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_efeaturecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_EFeatureCallExp)


def test_ocl_exp_efeaturecallexp_constructor_exists():
    assert callable(ocl_exp_EFeatureCallExp.__init__)


def test_ocl_exp_efeaturecallexp_constructor_args():
    sig = inspect.signature(ocl_exp_EFeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_eloopexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_ELoopExp)


def test_ocl_exp_eloopexp_constructor_exists():
    assert callable(ocl_exp_ELoopExp.__init__)


def test_ocl_exp_eloopexp_constructor_args():
    sig = inspect.signature(ocl_exp_ELoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_exp_etypeexp_is_not_abstract():
    assert not inspect.isabstract(ocl_exp_ETypeExp)


def test_ocl_exp_etypeexp_constructor_exists():
    assert callable(ocl_exp_ETypeExp.__init__)


def test_ocl_exp_etypeexp_constructor_args():
    sig = inspect.signature(ocl_exp_ETypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_dm_eentity_is_not_abstract():
    assert not inspect.isabstract(ocl_dm_EEntity)


def test_ocl_dm_eentity_constructor_exists():
    assert callable(ocl_dm_EEntity.__init__)


def test_ocl_dm_eentity_constructor_args():
    sig = inspect.signature(ocl_dm_EEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_dm_eentity_has_name():
    assert hasattr(ocl_dm_EEntity, "name")
    descriptor = None
    for klass in ocl_dm_EEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eiteratorkind_exists():
    # Check that the Enumeration exists
    assert EIteratorKind is not None

def test_eiteratorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EIteratorKind]
    expected_literals = [
        "forAll",
        "collect",
        "select",
        "exists",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EIteratorKind"

def test_eoperator_exists():
    # Check that the Enumeration exists
    assert EOperator is not None

def test_eoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOperator]
    expected_literals = [
        "isUnique",
        "size",
        "less",
        "oclIsUndefined",
        "AND",
        "greater",
        "OR",
        "isEmpty",
        "notEqual",
        "notEmpty",
        "lessOrEqual",
        "equal",
        "flatten",
        "greaterOrEqual",
        "allInstances",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOperator"

def test_emultiplicity_exists():
    # Check that the Enumeration exists
    assert EMultiplicity is not None

def test_emultiplicity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EMultiplicity]
    expected_literals = [
        "many",
        "one",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EMultiplicity"


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
ocl_type_ESignal_strategy = st.builds(
    ocl_type_ESignal,
)
ECollectionType_strategy = st.builds(
    ECollectionType,
)
ocl_type_ESequenceType_strategy = st.builds(
    ocl_type_ESequenceType,
)
ocl_type_EBagType_strategy = st.builds(
    ocl_type_EBagType,
)
ocl_type_ESetType_strategy = st.builds(
    ocl_type_ESetType,
)
ocl_type_EOrderedSetType_strategy = st.builds(
    ocl_type_EOrderedSetType,
)
EDataType_strategy = st.builds(
    EDataType,
)
ocl_type_ETupleType_strategy = st.builds(
    ocl_type_ETupleType,
)
ocl_type_EPrimitiveType_strategy = st.builds(
    ocl_type_EPrimitiveType,
)
ocl_type_ECollectionType_strategy = st.builds(
    ocl_type_ECollectionType,
)
ESignal_strategy = st.builds(
    ESignal,
)
ocl_type_EClassifier_strategy = st.builds(
    ocl_type_EClassifier,
)
EFeatureCallExp_strategy = st.builds(
    EFeatureCallExp,
)
ocl_exp_ENavigationCallExp_strategy = st.builds(
    ocl_exp_ENavigationCallExp,
)
ELiteralExp_strategy = st.builds(
    ELiteralExp,
)
ocl_exp_EPrimitiveType_strategy = st.builds(
    ocl_exp_EPrimitiveType,
)
ENumericLiteralExp_strategy = st.builds(
    ENumericLiteralExp,
)
ocl_exp_EIntegerLiteralExp_strategy = st.builds(
    ocl_exp_EIntegerLiteralExp,
    integerValue=
        safe_text
)
EOperationCallExp_strategy = st.builds(
    EOperationCallExp,
)
ocl_exp_EOclExpression_strategy = st.builds(
    ocl_exp_EOclExpression,
)
ELoopExp_strategy = st.builds(
    ELoopExp,
)
ocl_exp_EIteratorExp_strategy = st.builds(
    ocl_exp_EIteratorExp,
    kind=
        safe_text
)
ocl_exp_EVariable_strategy = st.builds(
    ocl_exp_EVariable,
    name=
        safe_text
)
EPrimitiveType_strategy = st.builds(
    EPrimitiveType,
)
ocl_exp_EBooleanLiteralExp_strategy = st.builds(
    ocl_exp_EBooleanLiteralExp,
    booleanValue=
        safe_text
)
ocl_exp_ENumericLiteralExp_strategy = st.builds(
    ocl_exp_ENumericLiteralExp,
)
ENavigationCallExp_strategy = st.builds(
    ENavigationCallExp,
)
ocl_exp_EPropertyCallExp_strategy = st.builds(
    ocl_exp_EPropertyCallExp,
)
ocl_exp_EAssociationClassCallExp_strategy = st.builds(
    ocl_exp_EAssociationClassCallExp,
)
ocl_exp_EStringLiteralExp_strategy = st.builds(
    ocl_exp_EStringLiteralExp,
    stringValue=
        safe_text
)
ocl_exp_EOperationCallExp_strategy = st.builds(
    ocl_exp_EOperationCallExp,
    referredOperation=
        safe_text
)
EVariable_strategy = st.builds(
    EVariable,
)
EOclExpression_strategy = st.builds(
    EOclExpression,
)
ocl_exp_ELiteralExp_strategy = st.builds(
    ocl_exp_ELiteralExp,
)
ocl_exp_ECallExp_strategy = st.builds(
    ocl_exp_ECallExp,
)
ocl_exp_EVariableExp_strategy = st.builds(
    ocl_exp_EVariableExp,
)
ocl_dm_EAttribute_strategy = st.builds(
    ocl_dm_EAttribute,
    type=
        safe_text,
    name=
        safe_text
)
ocl_dm_EDataModel_strategy = st.builds(
    ocl_dm_EDataModel,
)
EEntity_strategy = st.builds(
    EEntity,
)
ocl_dm_EAssociationEnd_strategy = st.builds(
    ocl_dm_EAssociationEnd,
    mult=
        safe_text,
    name=
        safe_text
)
EAttribute_strategy = st.builds(
    EAttribute,
)
EAssociationEnd_strategy = st.builds(
    EAssociationEnd,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
ocl_type_EVoidType_strategy = st.builds(
    ocl_type_EVoidType,
)
ocl_type_EAnyType_strategy = st.builds(
    ocl_type_EAnyType,
)
ocl_type_EMessageType_strategy = st.builds(
    ocl_type_EMessageType,
    referredOperation=
        safe_text
)
ocl_type_EDataType_strategy = st.builds(
    ocl_type_EDataType,
)
ocl_type_EInvalidType_strategy = st.builds(
    ocl_type_EInvalidType,
)
ECallExp_strategy = st.builds(
    ECallExp,
)
ocl_exp_EFeatureCallExp_strategy = st.builds(
    ocl_exp_EFeatureCallExp,
)
ocl_exp_ELoopExp_strategy = st.builds(
    ocl_exp_ELoopExp,
)
ocl_exp_ETypeExp_strategy = st.builds(
    ocl_exp_ETypeExp,
)
ocl_dm_EEntity_strategy = st.builds(
    ocl_dm_EEntity,
    name=
        safe_text
)

@given(instance=ocl_type_ESignal_strategy)
@settings(max_examples=50)
def test_ocl_type_esignal_instantiation(instance):
    assert isinstance(instance, ocl_type_ESignal)

@given(instance=ECollectionType_strategy)
@settings(max_examples=50)
def test_ecollectiontype_instantiation(instance):
    assert isinstance(instance, ECollectionType)

@given(instance=ocl_type_ESequenceType_strategy)
@settings(max_examples=50)
def test_ocl_type_esequencetype_instantiation(instance):
    assert isinstance(instance, ocl_type_ESequenceType)

@given(instance=ocl_type_EBagType_strategy)
@settings(max_examples=50)
def test_ocl_type_ebagtype_instantiation(instance):
    assert isinstance(instance, ocl_type_EBagType)

@given(instance=ocl_type_ESetType_strategy)
@settings(max_examples=50)
def test_ocl_type_esettype_instantiation(instance):
    assert isinstance(instance, ocl_type_ESetType)

@given(instance=ocl_type_EOrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl_type_eorderedsettype_instantiation(instance):
    assert isinstance(instance, ocl_type_EOrderedSetType)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=ocl_type_ETupleType_strategy)
@settings(max_examples=50)
def test_ocl_type_etupletype_instantiation(instance):
    assert isinstance(instance, ocl_type_ETupleType)

@given(instance=ocl_type_EPrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl_type_eprimitivetype_instantiation(instance):
    assert isinstance(instance, ocl_type_EPrimitiveType)

@given(instance=ocl_type_ECollectionType_strategy)
@settings(max_examples=50)
def test_ocl_type_ecollectiontype_instantiation(instance):
    assert isinstance(instance, ocl_type_ECollectionType)

@given(instance=ESignal_strategy)
@settings(max_examples=50)
def test_esignal_instantiation(instance):
    assert isinstance(instance, ESignal)

@given(instance=ocl_type_EClassifier_strategy)
@settings(max_examples=50)
def test_ocl_type_eclassifier_instantiation(instance):
    assert isinstance(instance, ocl_type_EClassifier)

@given(instance=EFeatureCallExp_strategy)
@settings(max_examples=50)
def test_efeaturecallexp_instantiation(instance):
    assert isinstance(instance, EFeatureCallExp)

@given(instance=ocl_exp_ENavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_enavigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_ENavigationCallExp)

@given(instance=ELiteralExp_strategy)
@settings(max_examples=50)
def test_eliteralexp_instantiation(instance):
    assert isinstance(instance, ELiteralExp)

@given(instance=ocl_exp_EPrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl_exp_eprimitivetype_instantiation(instance):
    assert isinstance(instance, ocl_exp_EPrimitiveType)

@given(instance=ENumericLiteralExp_strategy)
@settings(max_examples=50)
def test_enumericliteralexp_instantiation(instance):
    assert isinstance(instance, ENumericLiteralExp)

@given(instance=ocl_exp_EIntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_eintegerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EIntegerLiteralExp)



@given(instance=ocl_exp_EIntegerLiteralExp_strategy)
def test_ocl_exp_eintegerliteralexp_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=EOperationCallExp_strategy)
@settings(max_examples=50)
def test_eoperationcallexp_instantiation(instance):
    assert isinstance(instance, EOperationCallExp)

@given(instance=ocl_exp_EOclExpression_strategy)
@settings(max_examples=50)
def test_ocl_exp_eoclexpression_instantiation(instance):
    assert isinstance(instance, ocl_exp_EOclExpression)

@given(instance=ELoopExp_strategy)
@settings(max_examples=50)
def test_eloopexp_instantiation(instance):
    assert isinstance(instance, ELoopExp)

@given(instance=ocl_exp_EIteratorExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_eiteratorexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EIteratorExp)



@given(instance=ocl_exp_EIteratorExp_strategy)
def test_ocl_exp_eiteratorexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ocl_exp_EVariable_strategy)
@settings(max_examples=50)
def test_ocl_exp_evariable_instantiation(instance):
    assert isinstance(instance, ocl_exp_EVariable)



@given(instance=ocl_exp_EVariable_strategy)
def test_ocl_exp_evariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EPrimitiveType_strategy)
@settings(max_examples=50)
def test_eprimitivetype_instantiation(instance):
    assert isinstance(instance, EPrimitiveType)

@given(instance=ocl_exp_EBooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_ebooleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EBooleanLiteralExp)



@given(instance=ocl_exp_EBooleanLiteralExp_strategy)
def test_ocl_exp_ebooleanliteralexp_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=ocl_exp_ENumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_enumericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_ENumericLiteralExp)

@given(instance=ENavigationCallExp_strategy)
@settings(max_examples=50)
def test_enavigationcallexp_instantiation(instance):
    assert isinstance(instance, ENavigationCallExp)

@given(instance=ocl_exp_EPropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_epropertycallexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EPropertyCallExp)

@given(instance=ocl_exp_EAssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_eassociationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EAssociationClassCallExp)

@given(instance=ocl_exp_EStringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_estringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EStringLiteralExp)



@given(instance=ocl_exp_EStringLiteralExp_strategy)
def test_ocl_exp_estringliteralexp_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=ocl_exp_EOperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_eoperationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EOperationCallExp)



@given(instance=ocl_exp_EOperationCallExp_strategy)
def test_ocl_exp_eoperationcallexp_referredOperation_setter(instance):
    original = instance.referredOperation
    instance.referredOperation = original
    assert instance.referredOperation == original

@given(instance=EVariable_strategy)
@settings(max_examples=50)
def test_evariable_instantiation(instance):
    assert isinstance(instance, EVariable)

@given(instance=EOclExpression_strategy)
@settings(max_examples=50)
def test_eoclexpression_instantiation(instance):
    assert isinstance(instance, EOclExpression)

@given(instance=ocl_exp_ELiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_eliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_ELiteralExp)

@given(instance=ocl_exp_ECallExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_ecallexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_ECallExp)

@given(instance=ocl_exp_EVariableExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_evariableexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EVariableExp)

@given(instance=ocl_dm_EAttribute_strategy)
@settings(max_examples=50)
def test_ocl_dm_eattribute_instantiation(instance):
    assert isinstance(instance, ocl_dm_EAttribute)



@given(instance=ocl_dm_EAttribute_strategy)
def test_ocl_dm_eattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ocl_dm_EAttribute_strategy)
def test_ocl_dm_eattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl_dm_EDataModel_strategy)
@settings(max_examples=50)
def test_ocl_dm_edatamodel_instantiation(instance):
    assert isinstance(instance, ocl_dm_EDataModel)

@given(instance=EEntity_strategy)
@settings(max_examples=50)
def test_eentity_instantiation(instance):
    assert isinstance(instance, EEntity)

@given(instance=ocl_dm_EAssociationEnd_strategy)
@settings(max_examples=50)
def test_ocl_dm_eassociationend_instantiation(instance):
    assert isinstance(instance, ocl_dm_EAssociationEnd)



@given(instance=ocl_dm_EAssociationEnd_strategy)
def test_ocl_dm_eassociationend_mult_setter(instance):
    original = instance.mult
    instance.mult = original
    assert instance.mult == original



@given(instance=ocl_dm_EAssociationEnd_strategy)
def test_ocl_dm_eassociationend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=EAssociationEnd_strategy)
@settings(max_examples=50)
def test_eassociationend_instantiation(instance):
    assert isinstance(instance, EAssociationEnd)

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=ocl_type_EVoidType_strategy)
@settings(max_examples=50)
def test_ocl_type_evoidtype_instantiation(instance):
    assert isinstance(instance, ocl_type_EVoidType)

@given(instance=ocl_type_EAnyType_strategy)
@settings(max_examples=50)
def test_ocl_type_eanytype_instantiation(instance):
    assert isinstance(instance, ocl_type_EAnyType)

@given(instance=ocl_type_EMessageType_strategy)
@settings(max_examples=50)
def test_ocl_type_emessagetype_instantiation(instance):
    assert isinstance(instance, ocl_type_EMessageType)



@given(instance=ocl_type_EMessageType_strategy)
def test_ocl_type_emessagetype_referredOperation_setter(instance):
    original = instance.referredOperation
    instance.referredOperation = original
    assert instance.referredOperation == original

@given(instance=ocl_type_EDataType_strategy)
@settings(max_examples=50)
def test_ocl_type_edatatype_instantiation(instance):
    assert isinstance(instance, ocl_type_EDataType)

@given(instance=ocl_type_EInvalidType_strategy)
@settings(max_examples=50)
def test_ocl_type_einvalidtype_instantiation(instance):
    assert isinstance(instance, ocl_type_EInvalidType)

@given(instance=ECallExp_strategy)
@settings(max_examples=50)
def test_ecallexp_instantiation(instance):
    assert isinstance(instance, ECallExp)

@given(instance=ocl_exp_EFeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_efeaturecallexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_EFeatureCallExp)

@given(instance=ocl_exp_ELoopExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_eloopexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_ELoopExp)

@given(instance=ocl_exp_ETypeExp_strategy)
@settings(max_examples=50)
def test_ocl_exp_etypeexp_instantiation(instance):
    assert isinstance(instance, ocl_exp_ETypeExp)

@given(instance=ocl_dm_EEntity_strategy)
@settings(max_examples=50)
def test_ocl_dm_eentity_instantiation(instance):
    assert isinstance(instance, ocl_dm_EEntity)



@given(instance=ocl_dm_EEntity_strategy)
def test_ocl_dm_eentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
