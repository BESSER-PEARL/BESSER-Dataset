import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocl::type::ESignal,
    ECollectionType,
    ocl::type::ESetType,
    ocl::type::ESequenceType,
    ocl::type::EBagType,
    ocl::type::EOrderedSetType,
    EDataType,
    ocl::type::ETupleType,
    ocl::type::EPrimitiveType,
    ocl::type::ECollectionType,
    ESignal,
    ocl::type::EClassifier,
    EFeatureCallExp,
    ocl::exp::EOperationCallExp,
    ocl::exp::ENavigationCallExp,
    ELiteralExp,
    ocl::exp::EPrimitiveType,
    ENumericLiteralExp,
    ocl::exp::EIntegerLiteralExp,
    EOperationCallExp,
    EIfExp,
    EIterateExp,
    ELoopExp,
    ocl::exp::EIterateExp,
    ocl::exp::EVariable,
    EPrimitiveType,
    ocl::exp::EStringLiteralExp,
    ocl::exp::EBooleanLiteralExp,
    ocl::exp::ENumericLiteralExp,
    ENavigationCallExp,
    ocl::exp::EAssociationClassCallExp,
    ECallExp,
    ocl::exp::EFeatureCallExp,
    ocl::exp::ELoopExp,
    EVariable,
    EOclExpression,
    ocl::exp::EMessageExp,
    ocl::exp::ELiteralExp,
    ocl::exp::ECallExp,
    ocl::exp::EIfExp,
    ocl::exp::EStateExp,
    ocl::exp::ETypeExp,
    ocl::exp::EVariableExp,
    ocl::exp::EOclExpression,
    ocl::exp::EIteratorExp,
    ocl::exp::EPropertyCallExp,
    ocl::dm::EAttribute,
    ocl::dm::EDataModel,
    EEntity,
    ocl::dm::EAssociationEnd,
    EAttribute,
    EAssociationEnd,
    EClassifier,
    ocl::type::EVoidType,
    ocl::type::EMessageType,
    ocl::type::EAnyType,
    ocl::type::EDataType,
    ocl::type::EInvalidType,
    ocl::dm::EEntity,
    EOperator,
    EIteratorKind,
    EMultiplicity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl::type::esignal_is_not_abstract():
    assert not inspect.isabstract(ocl::type::ESignal)


def test_ocl::type::esignal_constructor_exists():
    assert callable(ocl::type::ESignal.__init__)


def test_ocl::type::esignal_constructor_args():
    sig = inspect.signature(ocl::type::ESignal.__init__)
    params = list(sig.parameters.keys())



def test_ecollectiontype_is_not_abstract():
    assert not inspect.isabstract(ECollectionType)


def test_ecollectiontype_constructor_exists():
    assert callable(ECollectionType.__init__)


def test_ecollectiontype_constructor_args():
    sig = inspect.signature(ECollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::esettype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::ESetType)


def test_ocl::type::esettype_constructor_exists():
    assert callable(ocl::type::ESetType.__init__)


def test_ocl::type::esettype_constructor_args():
    sig = inspect.signature(ocl::type::ESetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::esequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::ESequenceType)


def test_ocl::type::esequencetype_constructor_exists():
    assert callable(ocl::type::ESequenceType.__init__)


def test_ocl::type::esequencetype_constructor_args():
    sig = inspect.signature(ocl::type::ESequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::ebagtype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EBagType)


def test_ocl::type::ebagtype_constructor_exists():
    assert callable(ocl::type::EBagType.__init__)


def test_ocl::type::ebagtype_constructor_args():
    sig = inspect.signature(ocl::type::EBagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::eorderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EOrderedSetType)


def test_ocl::type::eorderedsettype_constructor_exists():
    assert callable(ocl::type::EOrderedSetType.__init__)


def test_ocl::type::eorderedsettype_constructor_args():
    sig = inspect.signature(ocl::type::EOrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::etupletype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::ETupleType)


def test_ocl::type::etupletype_constructor_exists():
    assert callable(ocl::type::ETupleType.__init__)


def test_ocl::type::etupletype_constructor_args():
    sig = inspect.signature(ocl::type::ETupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::eprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EPrimitiveType)


def test_ocl::type::eprimitivetype_constructor_exists():
    assert callable(ocl::type::EPrimitiveType.__init__)


def test_ocl::type::eprimitivetype_constructor_args():
    sig = inspect.signature(ocl::type::EPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::ecollectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::ECollectionType)


def test_ocl::type::ecollectiontype_constructor_exists():
    assert callable(ocl::type::ECollectionType.__init__)


def test_ocl::type::ecollectiontype_constructor_args():
    sig = inspect.signature(ocl::type::ECollectionType.__init__)
    params = list(sig.parameters.keys())



def test_esignal_is_not_abstract():
    assert not inspect.isabstract(ESignal)


def test_esignal_constructor_exists():
    assert callable(ESignal.__init__)


def test_esignal_constructor_args():
    sig = inspect.signature(ESignal.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::eclassifier_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EClassifier)


def test_ocl::type::eclassifier_constructor_exists():
    assert callable(ocl::type::EClassifier.__init__)


def test_ocl::type::eclassifier_constructor_args():
    sig = inspect.signature(ocl::type::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_efeaturecallexp_is_not_abstract():
    assert not inspect.isabstract(EFeatureCallExp)


def test_efeaturecallexp_constructor_exists():
    assert callable(EFeatureCallExp.__init__)


def test_efeaturecallexp_constructor_args():
    sig = inspect.signature(EFeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EOperationCallExp)


def test_ocl::exp::eoperationcallexp_constructor_exists():
    assert callable(ocl::exp::EOperationCallExp.__init__)


def test_ocl::exp::eoperationcallexp_constructor_args():
    sig = inspect.signature(ocl::exp::EOperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredOperation" in params, "Missing parameter 'referredOperation'"

def test_ocl::exp::eoperationcallexp_has_referredOperation():
    assert hasattr(ocl::exp::EOperationCallExp, "referredOperation")
    descriptor = None
    for klass in ocl::exp::EOperationCallExp.__mro__:
        if "referredOperation" in klass.__dict__:
            descriptor = klass.__dict__["referredOperation"]
            break
    assert isinstance(descriptor, property)



def test_ocl::exp::enavigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::ENavigationCallExp)


def test_ocl::exp::enavigationcallexp_constructor_exists():
    assert callable(ocl::exp::ENavigationCallExp.__init__)


def test_ocl::exp::enavigationcallexp_constructor_args():
    sig = inspect.signature(ocl::exp::ENavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_eliteralexp_is_not_abstract():
    assert not inspect.isabstract(ELiteralExp)


def test_eliteralexp_constructor_exists():
    assert callable(ELiteralExp.__init__)


def test_eliteralexp_constructor_args():
    sig = inspect.signature(ELiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EPrimitiveType)


def test_ocl::exp::eprimitivetype_constructor_exists():
    assert callable(ocl::exp::EPrimitiveType.__init__)


def test_ocl::exp::eprimitivetype_constructor_args():
    sig = inspect.signature(ocl::exp::EPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_enumericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ENumericLiteralExp)


def test_enumericliteralexp_constructor_exists():
    assert callable(ENumericLiteralExp.__init__)


def test_enumericliteralexp_constructor_args():
    sig = inspect.signature(ENumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eintegerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EIntegerLiteralExp)


def test_ocl::exp::eintegerliteralexp_constructor_exists():
    assert callable(ocl::exp::EIntegerLiteralExp.__init__)


def test_ocl::exp::eintegerliteralexp_constructor_args():
    sig = inspect.signature(ocl::exp::EIntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_ocl::exp::eintegerliteralexp_has_integerValue():
    assert hasattr(ocl::exp::EIntegerLiteralExp, "integerValue")
    descriptor = None
    for klass in ocl::exp::EIntegerLiteralExp.__mro__:
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



def test_eifexp_is_not_abstract():
    assert not inspect.isabstract(EIfExp)


def test_eifexp_constructor_exists():
    assert callable(EIfExp.__init__)


def test_eifexp_constructor_args():
    sig = inspect.signature(EIfExp.__init__)
    params = list(sig.parameters.keys())



def test_eiterateexp_is_not_abstract():
    assert not inspect.isabstract(EIterateExp)


def test_eiterateexp_constructor_exists():
    assert callable(EIterateExp.__init__)


def test_eiterateexp_constructor_args():
    sig = inspect.signature(EIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_eloopexp_is_not_abstract():
    assert not inspect.isabstract(ELoopExp)


def test_eloopexp_constructor_exists():
    assert callable(ELoopExp.__init__)


def test_eloopexp_constructor_args():
    sig = inspect.signature(ELoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eiterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EIterateExp)


def test_ocl::exp::eiterateexp_constructor_exists():
    assert callable(ocl::exp::EIterateExp.__init__)


def test_ocl::exp::eiterateexp_constructor_args():
    sig = inspect.signature(ocl::exp::EIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::evariable_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EVariable)


def test_ocl::exp::evariable_constructor_exists():
    assert callable(ocl::exp::EVariable.__init__)


def test_ocl::exp::evariable_constructor_args():
    sig = inspect.signature(ocl::exp::EVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::exp::evariable_has_name():
    assert hasattr(ocl::exp::EVariable, "name")
    descriptor = None
    for klass in ocl::exp::EVariable.__mro__:
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



def test_ocl::exp::estringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EStringLiteralExp)


def test_ocl::exp::estringliteralexp_constructor_exists():
    assert callable(ocl::exp::EStringLiteralExp.__init__)


def test_ocl::exp::estringliteralexp_constructor_args():
    sig = inspect.signature(ocl::exp::EStringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_ocl::exp::estringliteralexp_has_stringValue():
    assert hasattr(ocl::exp::EStringLiteralExp, "stringValue")
    descriptor = None
    for klass in ocl::exp::EStringLiteralExp.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_ocl::exp::ebooleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EBooleanLiteralExp)


def test_ocl::exp::ebooleanliteralexp_constructor_exists():
    assert callable(ocl::exp::EBooleanLiteralExp.__init__)


def test_ocl::exp::ebooleanliteralexp_constructor_args():
    sig = inspect.signature(ocl::exp::EBooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_ocl::exp::ebooleanliteralexp_has_booleanValue():
    assert hasattr(ocl::exp::EBooleanLiteralExp, "booleanValue")
    descriptor = None
    for klass in ocl::exp::EBooleanLiteralExp.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_ocl::exp::enumericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::ENumericLiteralExp)


def test_ocl::exp::enumericliteralexp_constructor_exists():
    assert callable(ocl::exp::ENumericLiteralExp.__init__)


def test_ocl::exp::enumericliteralexp_constructor_args():
    sig = inspect.signature(ocl::exp::ENumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_enavigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ENavigationCallExp)


def test_enavigationcallexp_constructor_exists():
    assert callable(ENavigationCallExp.__init__)


def test_enavigationcallexp_constructor_args():
    sig = inspect.signature(ENavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eassociationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EAssociationClassCallExp)


def test_ocl::exp::eassociationclasscallexp_constructor_exists():
    assert callable(ocl::exp::EAssociationClassCallExp.__init__)


def test_ocl::exp::eassociationclasscallexp_constructor_args():
    sig = inspect.signature(ocl::exp::EAssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ecallexp_is_not_abstract():
    assert not inspect.isabstract(ECallExp)


def test_ecallexp_constructor_exists():
    assert callable(ECallExp.__init__)


def test_ecallexp_constructor_args():
    sig = inspect.signature(ECallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::efeaturecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EFeatureCallExp)


def test_ocl::exp::efeaturecallexp_constructor_exists():
    assert callable(ocl::exp::EFeatureCallExp.__init__)


def test_ocl::exp::efeaturecallexp_constructor_args():
    sig = inspect.signature(ocl::exp::EFeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eloopexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::ELoopExp)


def test_ocl::exp::eloopexp_constructor_exists():
    assert callable(ocl::exp::ELoopExp.__init__)


def test_ocl::exp::eloopexp_constructor_args():
    sig = inspect.signature(ocl::exp::ELoopExp.__init__)
    params = list(sig.parameters.keys())



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



def test_ocl::exp::emessageexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EMessageExp)


def test_ocl::exp::emessageexp_constructor_exists():
    assert callable(ocl::exp::EMessageExp.__init__)


def test_ocl::exp::emessageexp_constructor_args():
    sig = inspect.signature(ocl::exp::EMessageExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::ELiteralExp)


def test_ocl::exp::eliteralexp_constructor_exists():
    assert callable(ocl::exp::ELiteralExp.__init__)


def test_ocl::exp::eliteralexp_constructor_args():
    sig = inspect.signature(ocl::exp::ELiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::ecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::ECallExp)


def test_ocl::exp::ecallexp_constructor_exists():
    assert callable(ocl::exp::ECallExp.__init__)


def test_ocl::exp::ecallexp_constructor_args():
    sig = inspect.signature(ocl::exp::ECallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eifexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EIfExp)


def test_ocl::exp::eifexp_constructor_exists():
    assert callable(ocl::exp::EIfExp.__init__)


def test_ocl::exp::eifexp_constructor_args():
    sig = inspect.signature(ocl::exp::EIfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::estateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EStateExp)


def test_ocl::exp::estateexp_constructor_exists():
    assert callable(ocl::exp::EStateExp.__init__)


def test_ocl::exp::estateexp_constructor_args():
    sig = inspect.signature(ocl::exp::EStateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::etypeexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::ETypeExp)


def test_ocl::exp::etypeexp_constructor_exists():
    assert callable(ocl::exp::ETypeExp.__init__)


def test_ocl::exp::etypeexp_constructor_args():
    sig = inspect.signature(ocl::exp::ETypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::evariableexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EVariableExp)


def test_ocl::exp::evariableexp_constructor_exists():
    assert callable(ocl::exp::EVariableExp.__init__)


def test_ocl::exp::evariableexp_constructor_args():
    sig = inspect.signature(ocl::exp::EVariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eoclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EOclExpression)


def test_ocl::exp::eoclexpression_constructor_exists():
    assert callable(ocl::exp::EOclExpression.__init__)


def test_ocl::exp::eoclexpression_constructor_args():
    sig = inspect.signature(ocl::exp::EOclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::exp::eiteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EIteratorExp)


def test_ocl::exp::eiteratorexp_constructor_exists():
    assert callable(ocl::exp::EIteratorExp.__init__)


def test_ocl::exp::eiteratorexp_constructor_args():
    sig = inspect.signature(ocl::exp::EIteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl::exp::eiteratorexp_has_kind():
    assert hasattr(ocl::exp::EIteratorExp, "kind")
    descriptor = None
    for klass in ocl::exp::EIteratorExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl::exp::epropertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::exp::EPropertyCallExp)


def test_ocl::exp::epropertycallexp_constructor_exists():
    assert callable(ocl::exp::EPropertyCallExp.__init__)


def test_ocl::exp::epropertycallexp_constructor_args():
    sig = inspect.signature(ocl::exp::EPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::dm::eattribute_is_not_abstract():
    assert not inspect.isabstract(ocl::dm::EAttribute)


def test_ocl::dm::eattribute_constructor_exists():
    assert callable(ocl::dm::EAttribute.__init__)


def test_ocl::dm::eattribute_constructor_args():
    sig = inspect.signature(ocl::dm::EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::dm::eattribute_has_type():
    assert hasattr(ocl::dm::EAttribute, "type")
    descriptor = None
    for klass in ocl::dm::EAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ocl::dm::eattribute_has_name():
    assert hasattr(ocl::dm::EAttribute, "name")
    descriptor = None
    for klass in ocl::dm::EAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::dm::edatamodel_is_not_abstract():
    assert not inspect.isabstract(ocl::dm::EDataModel)


def test_ocl::dm::edatamodel_constructor_exists():
    assert callable(ocl::dm::EDataModel.__init__)


def test_ocl::dm::edatamodel_constructor_args():
    sig = inspect.signature(ocl::dm::EDataModel.__init__)
    params = list(sig.parameters.keys())



def test_eentity_is_not_abstract():
    assert not inspect.isabstract(EEntity)


def test_eentity_constructor_exists():
    assert callable(EEntity.__init__)


def test_eentity_constructor_args():
    sig = inspect.signature(EEntity.__init__)
    params = list(sig.parameters.keys())



def test_ocl::dm::eassociationend_is_not_abstract():
    assert not inspect.isabstract(ocl::dm::EAssociationEnd)


def test_ocl::dm::eassociationend_constructor_exists():
    assert callable(ocl::dm::EAssociationEnd.__init__)


def test_ocl::dm::eassociationend_constructor_args():
    sig = inspect.signature(ocl::dm::EAssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "mult" in params, "Missing parameter 'mult'"
    assert "opp" in params, "Missing parameter 'opp'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::dm::eassociationend_has_mult():
    assert hasattr(ocl::dm::EAssociationEnd, "mult")
    descriptor = None
    for klass in ocl::dm::EAssociationEnd.__mro__:
        if "mult" in klass.__dict__:
            descriptor = klass.__dict__["mult"]
            break
    assert isinstance(descriptor, property)

def test_ocl::dm::eassociationend_has_opp():
    assert hasattr(ocl::dm::EAssociationEnd, "opp")
    descriptor = None
    for klass in ocl::dm::EAssociationEnd.__mro__:
        if "opp" in klass.__dict__:
            descriptor = klass.__dict__["opp"]
            break
    assert isinstance(descriptor, property)

def test_ocl::dm::eassociationend_has_name():
    assert hasattr(ocl::dm::EAssociationEnd, "name")
    descriptor = None
    for klass in ocl::dm::EAssociationEnd.__mro__:
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



def test_ocl::type::evoidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EVoidType)


def test_ocl::type::evoidtype_constructor_exists():
    assert callable(ocl::type::EVoidType.__init__)


def test_ocl::type::evoidtype_constructor_args():
    sig = inspect.signature(ocl::type::EVoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::emessagetype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EMessageType)


def test_ocl::type::emessagetype_constructor_exists():
    assert callable(ocl::type::EMessageType.__init__)


def test_ocl::type::emessagetype_constructor_args():
    sig = inspect.signature(ocl::type::EMessageType.__init__)
    params = list(sig.parameters.keys())
    assert "referredOperation" in params, "Missing parameter 'referredOperation'"

def test_ocl::type::emessagetype_has_referredOperation():
    assert hasattr(ocl::type::EMessageType, "referredOperation")
    descriptor = None
    for klass in ocl::type::EMessageType.__mro__:
        if "referredOperation" in klass.__dict__:
            descriptor = klass.__dict__["referredOperation"]
            break
    assert isinstance(descriptor, property)



def test_ocl::type::eanytype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EAnyType)


def test_ocl::type::eanytype_constructor_exists():
    assert callable(ocl::type::EAnyType.__init__)


def test_ocl::type::eanytype_constructor_args():
    sig = inspect.signature(ocl::type::EAnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::edatatype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EDataType)


def test_ocl::type::edatatype_constructor_exists():
    assert callable(ocl::type::EDataType.__init__)


def test_ocl::type::edatatype_constructor_args():
    sig = inspect.signature(ocl::type::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::type::einvalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::type::EInvalidType)


def test_ocl::type::einvalidtype_constructor_exists():
    assert callable(ocl::type::EInvalidType.__init__)


def test_ocl::type::einvalidtype_constructor_args():
    sig = inspect.signature(ocl::type::EInvalidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::dm::eentity_is_not_abstract():
    assert not inspect.isabstract(ocl::dm::EEntity)


def test_ocl::dm::eentity_constructor_exists():
    assert callable(ocl::dm::EEntity.__init__)


def test_ocl::dm::eentity_constructor_args():
    sig = inspect.signature(ocl::dm::EEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::dm::eentity_has_name():
    assert hasattr(ocl::dm::EEntity, "name")
    descriptor = None
    for klass in ocl::dm::EEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eoperator_exists():
    # Check that the Enumeration exists
    assert EOperator is not None

def test_eoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOperator]
    expected_literals = [
        "allInstances",
        "notEmpty",
        "AND",
        "flatten",
        "greaterOrEqual",
        "lessOrEqual",
        "notEqual",
        "less",
        "isEmpty",
        "oclIsUndefined",
        "size",
        "isUnique",
        "OR",
        "equal",
        "IMPLIES",
        "greater",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOperator"

def test_eiteratorkind_exists():
    # Check that the Enumeration exists
    assert EIteratorKind is not None

def test_eiteratorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EIteratorKind]
    expected_literals = [
        "collect",
        "select",
        "forAll",
        "exists",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EIteratorKind"

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
ocl::type::ESignal_strategy = st.builds(
    ocl::type::ESignal,
)
ECollectionType_strategy = st.builds(
    ECollectionType,
)
ocl::type::ESetType_strategy = st.builds(
    ocl::type::ESetType,
)
ocl::type::ESequenceType_strategy = st.builds(
    ocl::type::ESequenceType,
)
ocl::type::EBagType_strategy = st.builds(
    ocl::type::EBagType,
)
ocl::type::EOrderedSetType_strategy = st.builds(
    ocl::type::EOrderedSetType,
)
EDataType_strategy = st.builds(
    EDataType,
)
ocl::type::ETupleType_strategy = st.builds(
    ocl::type::ETupleType,
)
ocl::type::EPrimitiveType_strategy = st.builds(
    ocl::type::EPrimitiveType,
)
ocl::type::ECollectionType_strategy = st.builds(
    ocl::type::ECollectionType,
)
ESignal_strategy = st.builds(
    ESignal,
)
ocl::type::EClassifier_strategy = st.builds(
    ocl::type::EClassifier,
)
EFeatureCallExp_strategy = st.builds(
    EFeatureCallExp,
)
ocl::exp::EOperationCallExp_strategy = st.builds(
    ocl::exp::EOperationCallExp,
    referredOperation=
        safe_text
)
ocl::exp::ENavigationCallExp_strategy = st.builds(
    ocl::exp::ENavigationCallExp,
)
ELiteralExp_strategy = st.builds(
    ELiteralExp,
)
ocl::exp::EPrimitiveType_strategy = st.builds(
    ocl::exp::EPrimitiveType,
)
ENumericLiteralExp_strategy = st.builds(
    ENumericLiteralExp,
)
ocl::exp::EIntegerLiteralExp_strategy = st.builds(
    ocl::exp::EIntegerLiteralExp,
    integerValue=
        safe_text
)
EOperationCallExp_strategy = st.builds(
    EOperationCallExp,
)
EIfExp_strategy = st.builds(
    EIfExp,
)
EIterateExp_strategy = st.builds(
    EIterateExp,
)
ELoopExp_strategy = st.builds(
    ELoopExp,
)
ocl::exp::EIterateExp_strategy = st.builds(
    ocl::exp::EIterateExp,
)
ocl::exp::EVariable_strategy = st.builds(
    ocl::exp::EVariable,
    name=
        safe_text
)
EPrimitiveType_strategy = st.builds(
    EPrimitiveType,
)
ocl::exp::EStringLiteralExp_strategy = st.builds(
    ocl::exp::EStringLiteralExp,
    stringValue=
        safe_text
)
ocl::exp::EBooleanLiteralExp_strategy = st.builds(
    ocl::exp::EBooleanLiteralExp,
    booleanValue=
        safe_text
)
ocl::exp::ENumericLiteralExp_strategy = st.builds(
    ocl::exp::ENumericLiteralExp,
)
ENavigationCallExp_strategy = st.builds(
    ENavigationCallExp,
)
ocl::exp::EAssociationClassCallExp_strategy = st.builds(
    ocl::exp::EAssociationClassCallExp,
)
ECallExp_strategy = st.builds(
    ECallExp,
)
ocl::exp::EFeatureCallExp_strategy = st.builds(
    ocl::exp::EFeatureCallExp,
)
ocl::exp::ELoopExp_strategy = st.builds(
    ocl::exp::ELoopExp,
)
EVariable_strategy = st.builds(
    EVariable,
)
EOclExpression_strategy = st.builds(
    EOclExpression,
)
ocl::exp::EMessageExp_strategy = st.builds(
    ocl::exp::EMessageExp,
)
ocl::exp::ELiteralExp_strategy = st.builds(
    ocl::exp::ELiteralExp,
)
ocl::exp::ECallExp_strategy = st.builds(
    ocl::exp::ECallExp,
)
ocl::exp::EIfExp_strategy = st.builds(
    ocl::exp::EIfExp,
)
ocl::exp::EStateExp_strategy = st.builds(
    ocl::exp::EStateExp,
)
ocl::exp::ETypeExp_strategy = st.builds(
    ocl::exp::ETypeExp,
)
ocl::exp::EVariableExp_strategy = st.builds(
    ocl::exp::EVariableExp,
)
ocl::exp::EOclExpression_strategy = st.builds(
    ocl::exp::EOclExpression,
)
ocl::exp::EIteratorExp_strategy = st.builds(
    ocl::exp::EIteratorExp,
    kind=
        safe_text
)
ocl::exp::EPropertyCallExp_strategy = st.builds(
    ocl::exp::EPropertyCallExp,
)
ocl::dm::EAttribute_strategy = st.builds(
    ocl::dm::EAttribute,
    type=
        safe_text,
    name=
        safe_text
)
ocl::dm::EDataModel_strategy = st.builds(
    ocl::dm::EDataModel,
)
EEntity_strategy = st.builds(
    EEntity,
)
ocl::dm::EAssociationEnd_strategy = st.builds(
    ocl::dm::EAssociationEnd,
    mult=
        safe_text,
    opp=
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
ocl::type::EVoidType_strategy = st.builds(
    ocl::type::EVoidType,
)
ocl::type::EMessageType_strategy = st.builds(
    ocl::type::EMessageType,
    referredOperation=
        safe_text
)
ocl::type::EAnyType_strategy = st.builds(
    ocl::type::EAnyType,
)
ocl::type::EDataType_strategy = st.builds(
    ocl::type::EDataType,
)
ocl::type::EInvalidType_strategy = st.builds(
    ocl::type::EInvalidType,
)
ocl::dm::EEntity_strategy = st.builds(
    ocl::dm::EEntity,
    name=
        safe_text
)

@given(instance=ocl::type::ESignal_strategy)
@settings(max_examples=50)
def test_ocl::type::esignal_instantiation(instance):
    assert isinstance(instance, ocl::type::ESignal)

@given(instance=ECollectionType_strategy)
@settings(max_examples=50)
def test_ecollectiontype_instantiation(instance):
    assert isinstance(instance, ECollectionType)

@given(instance=ocl::type::ESetType_strategy)
@settings(max_examples=50)
def test_ocl::type::esettype_instantiation(instance):
    assert isinstance(instance, ocl::type::ESetType)

@given(instance=ocl::type::ESequenceType_strategy)
@settings(max_examples=50)
def test_ocl::type::esequencetype_instantiation(instance):
    assert isinstance(instance, ocl::type::ESequenceType)

@given(instance=ocl::type::EBagType_strategy)
@settings(max_examples=50)
def test_ocl::type::ebagtype_instantiation(instance):
    assert isinstance(instance, ocl::type::EBagType)

@given(instance=ocl::type::EOrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl::type::eorderedsettype_instantiation(instance):
    assert isinstance(instance, ocl::type::EOrderedSetType)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=ocl::type::ETupleType_strategy)
@settings(max_examples=50)
def test_ocl::type::etupletype_instantiation(instance):
    assert isinstance(instance, ocl::type::ETupleType)

@given(instance=ocl::type::EPrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl::type::eprimitivetype_instantiation(instance):
    assert isinstance(instance, ocl::type::EPrimitiveType)

@given(instance=ocl::type::ECollectionType_strategy)
@settings(max_examples=50)
def test_ocl::type::ecollectiontype_instantiation(instance):
    assert isinstance(instance, ocl::type::ECollectionType)

@given(instance=ESignal_strategy)
@settings(max_examples=50)
def test_esignal_instantiation(instance):
    assert isinstance(instance, ESignal)

@given(instance=ocl::type::EClassifier_strategy)
@settings(max_examples=50)
def test_ocl::type::eclassifier_instantiation(instance):
    assert isinstance(instance, ocl::type::EClassifier)

@given(instance=EFeatureCallExp_strategy)
@settings(max_examples=50)
def test_efeaturecallexp_instantiation(instance):
    assert isinstance(instance, EFeatureCallExp)

@given(instance=ocl::exp::EOperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eoperationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EOperationCallExp)

@given(instance=ocl::exp::EOperationCallExp_strategy)
def test_ocl::exp::eoperationcallexp_referredOperation_type(instance):
    assert isinstance(instance.referredOperation, str)


@given(instance=ocl::exp::EOperationCallExp_strategy)
def test_ocl::exp::eoperationcallexp_referredOperation_setter(instance):
    original = instance.referredOperation
    instance.referredOperation = original
    assert instance.referredOperation == original

@given(instance=ocl::exp::ENavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::enavigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::ENavigationCallExp)

@given(instance=ELiteralExp_strategy)
@settings(max_examples=50)
def test_eliteralexp_instantiation(instance):
    assert isinstance(instance, ELiteralExp)

@given(instance=ocl::exp::EPrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl::exp::eprimitivetype_instantiation(instance):
    assert isinstance(instance, ocl::exp::EPrimitiveType)

@given(instance=ENumericLiteralExp_strategy)
@settings(max_examples=50)
def test_enumericliteralexp_instantiation(instance):
    assert isinstance(instance, ENumericLiteralExp)

@given(instance=ocl::exp::EIntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eintegerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EIntegerLiteralExp)

@given(instance=ocl::exp::EIntegerLiteralExp_strategy)
def test_ocl::exp::eintegerliteralexp_integerValue_type(instance):
    assert isinstance(instance.integerValue, str)


@given(instance=ocl::exp::EIntegerLiteralExp_strategy)
def test_ocl::exp::eintegerliteralexp_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=EOperationCallExp_strategy)
@settings(max_examples=50)
def test_eoperationcallexp_instantiation(instance):
    assert isinstance(instance, EOperationCallExp)

@given(instance=EIfExp_strategy)
@settings(max_examples=50)
def test_eifexp_instantiation(instance):
    assert isinstance(instance, EIfExp)

@given(instance=EIterateExp_strategy)
@settings(max_examples=50)
def test_eiterateexp_instantiation(instance):
    assert isinstance(instance, EIterateExp)

@given(instance=ELoopExp_strategy)
@settings(max_examples=50)
def test_eloopexp_instantiation(instance):
    assert isinstance(instance, ELoopExp)

@given(instance=ocl::exp::EIterateExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eiterateexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EIterateExp)

@given(instance=ocl::exp::EVariable_strategy)
@settings(max_examples=50)
def test_ocl::exp::evariable_instantiation(instance):
    assert isinstance(instance, ocl::exp::EVariable)

@given(instance=ocl::exp::EVariable_strategy)
def test_ocl::exp::evariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::exp::EVariable_strategy)
def test_ocl::exp::evariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EPrimitiveType_strategy)
@settings(max_examples=50)
def test_eprimitivetype_instantiation(instance):
    assert isinstance(instance, EPrimitiveType)

@given(instance=ocl::exp::EStringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::estringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EStringLiteralExp)

@given(instance=ocl::exp::EStringLiteralExp_strategy)
def test_ocl::exp::estringliteralexp_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=ocl::exp::EStringLiteralExp_strategy)
def test_ocl::exp::estringliteralexp_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=ocl::exp::EBooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::ebooleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EBooleanLiteralExp)

@given(instance=ocl::exp::EBooleanLiteralExp_strategy)
def test_ocl::exp::ebooleanliteralexp_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, str)


@given(instance=ocl::exp::EBooleanLiteralExp_strategy)
def test_ocl::exp::ebooleanliteralexp_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=ocl::exp::ENumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::enumericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::ENumericLiteralExp)

@given(instance=ENavigationCallExp_strategy)
@settings(max_examples=50)
def test_enavigationcallexp_instantiation(instance):
    assert isinstance(instance, ENavigationCallExp)

@given(instance=ocl::exp::EAssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eassociationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EAssociationClassCallExp)

@given(instance=ECallExp_strategy)
@settings(max_examples=50)
def test_ecallexp_instantiation(instance):
    assert isinstance(instance, ECallExp)

@given(instance=ocl::exp::EFeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::efeaturecallexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EFeatureCallExp)

@given(instance=ocl::exp::ELoopExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eloopexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::ELoopExp)

@given(instance=EVariable_strategy)
@settings(max_examples=50)
def test_evariable_instantiation(instance):
    assert isinstance(instance, EVariable)

@given(instance=EOclExpression_strategy)
@settings(max_examples=50)
def test_eoclexpression_instantiation(instance):
    assert isinstance(instance, EOclExpression)

@given(instance=ocl::exp::EMessageExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::emessageexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EMessageExp)

@given(instance=ocl::exp::ELiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::ELiteralExp)

@given(instance=ocl::exp::ECallExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::ecallexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::ECallExp)

@given(instance=ocl::exp::EIfExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eifexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EIfExp)

@given(instance=ocl::exp::EStateExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::estateexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EStateExp)

@given(instance=ocl::exp::ETypeExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::etypeexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::ETypeExp)

@given(instance=ocl::exp::EVariableExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::evariableexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EVariableExp)

@given(instance=ocl::exp::EOclExpression_strategy)
@settings(max_examples=50)
def test_ocl::exp::eoclexpression_instantiation(instance):
    assert isinstance(instance, ocl::exp::EOclExpression)

@given(instance=ocl::exp::EIteratorExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::eiteratorexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EIteratorExp)

@given(instance=ocl::exp::EIteratorExp_strategy)
def test_ocl::exp::eiteratorexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ocl::exp::EIteratorExp_strategy)
def test_ocl::exp::eiteratorexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ocl::exp::EPropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::exp::epropertycallexp_instantiation(instance):
    assert isinstance(instance, ocl::exp::EPropertyCallExp)

@given(instance=ocl::dm::EAttribute_strategy)
@settings(max_examples=50)
def test_ocl::dm::eattribute_instantiation(instance):
    assert isinstance(instance, ocl::dm::EAttribute)

@given(instance=ocl::dm::EAttribute_strategy)
def test_ocl::dm::eattribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ocl::dm::EAttribute_strategy)
def test_ocl::dm::eattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ocl::dm::EAttribute_strategy)
def test_ocl::dm::eattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::dm::EAttribute_strategy)
def test_ocl::dm::eattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl::dm::EDataModel_strategy)
@settings(max_examples=50)
def test_ocl::dm::edatamodel_instantiation(instance):
    assert isinstance(instance, ocl::dm::EDataModel)

@given(instance=EEntity_strategy)
@settings(max_examples=50)
def test_eentity_instantiation(instance):
    assert isinstance(instance, EEntity)

@given(instance=ocl::dm::EAssociationEnd_strategy)
@settings(max_examples=50)
def test_ocl::dm::eassociationend_instantiation(instance):
    assert isinstance(instance, ocl::dm::EAssociationEnd)

@given(instance=ocl::dm::EAssociationEnd_strategy)
def test_ocl::dm::eassociationend_mult_type(instance):
    assert isinstance(instance.mult, str)


@given(instance=ocl::dm::EAssociationEnd_strategy)
def test_ocl::dm::eassociationend_mult_setter(instance):
    original = instance.mult
    instance.mult = original
    assert instance.mult == original

@given(instance=ocl::dm::EAssociationEnd_strategy)
def test_ocl::dm::eassociationend_opp_type(instance):
    assert isinstance(instance.opp, str)


@given(instance=ocl::dm::EAssociationEnd_strategy)
def test_ocl::dm::eassociationend_opp_setter(instance):
    original = instance.opp
    instance.opp = original
    assert instance.opp == original

@given(instance=ocl::dm::EAssociationEnd_strategy)
def test_ocl::dm::eassociationend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::dm::EAssociationEnd_strategy)
def test_ocl::dm::eassociationend_name_setter(instance):
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

@given(instance=ocl::type::EVoidType_strategy)
@settings(max_examples=50)
def test_ocl::type::evoidtype_instantiation(instance):
    assert isinstance(instance, ocl::type::EVoidType)

@given(instance=ocl::type::EMessageType_strategy)
@settings(max_examples=50)
def test_ocl::type::emessagetype_instantiation(instance):
    assert isinstance(instance, ocl::type::EMessageType)

@given(instance=ocl::type::EMessageType_strategy)
def test_ocl::type::emessagetype_referredOperation_type(instance):
    assert isinstance(instance.referredOperation, str)


@given(instance=ocl::type::EMessageType_strategy)
def test_ocl::type::emessagetype_referredOperation_setter(instance):
    original = instance.referredOperation
    instance.referredOperation = original
    assert instance.referredOperation == original

@given(instance=ocl::type::EAnyType_strategy)
@settings(max_examples=50)
def test_ocl::type::eanytype_instantiation(instance):
    assert isinstance(instance, ocl::type::EAnyType)

@given(instance=ocl::type::EDataType_strategy)
@settings(max_examples=50)
def test_ocl::type::edatatype_instantiation(instance):
    assert isinstance(instance, ocl::type::EDataType)

@given(instance=ocl::type::EInvalidType_strategy)
@settings(max_examples=50)
def test_ocl::type::einvalidtype_instantiation(instance):
    assert isinstance(instance, ocl::type::EInvalidType)

@given(instance=ocl::dm::EEntity_strategy)
@settings(max_examples=50)
def test_ocl::dm::eentity_instantiation(instance):
    assert isinstance(instance, ocl::dm::EEntity)

@given(instance=ocl::dm::EEntity_strategy)
def test_ocl::dm::eentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::dm::EEntity_strategy)
def test_ocl::dm::eentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
