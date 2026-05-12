import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DmxComplexObject,
    dmx_DmxDetail,
    dmx_DmxEntity,
    dmx_DFeature,
    dmx_DComplexType,
    dmx_DNamedElement,
    dmx_DType,
    dmx_IStaticReferenceTarget,
    dmx_DmxCallArguments,
    dmx_DmxFilterTypeDescriptor,
    dmx_DmxFilterParameter,
    DNavigableMember,
    dmx_DmxCorrelationVariable,
    dmx_DmxField,
    DPrimitive,
    dmx_DmxArchetype,
    dmx_DNavigableMember,
    DExpression,
    dmx_DmxDateLiteral,
    dmx_DmxUndefinedLiteral,
    dmx_DmxListExpression,
    dmx_DmxNaturalLiteral,
    dmx_DmxStaticReference,
    dmx_DmxUrlLiteral,
    dmx_DmxBooleanLiteral,
    dmx_DmxContextReference,
    dmx_DmxDecimalLiteral,
    dmx_DmxCastExpression,
    dmx_DmxStringLiteral,
    dmx_DmxInstanceOfExpression,
    dmx_DmxMemberNavigation,
    dmx_DmxIfExpression,
    dmx_DmxFunctionCall,
    dmx_DmxUnaryOperation,
    dmx_DmxBinaryOperation,
    dmx_DmxAssignment,
    DContext,
    dmx_DExpression,
    dmx_DmxTestContext,
    INavigableMemberContainer,
    dmx_DmxPredicateWithCorrelationVariable,
    dmx_DmxComplexObject,
    dmx_DmxTest,
    dmx_DmxFilter,
    ITypeContainer,
    DModel,
    dmx_DmxModel,
    dmx_DmxBaseTypeSet,
    DmxBinaryOperator,
    DmxUnaryOperator,
    DmxBaseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dmxcomplexobject_is_not_abstract():
    assert not inspect.isabstract(DmxComplexObject)


def test_dmxcomplexobject_constructor_exists():
    assert callable(DmxComplexObject.__init__)


def test_dmxcomplexobject_constructor_args():
    sig = inspect.signature(DmxComplexObject.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxdetail_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxDetail)


def test_dmx_dmxdetail_constructor_exists():
    assert callable(dmx_DmxDetail.__init__)


def test_dmx_dmxdetail_constructor_args():
    sig = inspect.signature(dmx_DmxDetail.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxentity_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxEntity)


def test_dmx_dmxentity_constructor_exists():
    assert callable(dmx_DmxEntity.__init__)


def test_dmx_dmxentity_constructor_args():
    sig = inspect.signature(dmx_DmxEntity.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dfeature_is_not_abstract():
    assert not inspect.isabstract(dmx_DFeature)


def test_dmx_dfeature_constructor_exists():
    assert callable(dmx_DFeature.__init__)


def test_dmx_dfeature_constructor_args():
    sig = inspect.signature(dmx_DFeature.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dcomplextype_is_not_abstract():
    assert not inspect.isabstract(dmx_DComplexType)


def test_dmx_dcomplextype_constructor_exists():
    assert callable(dmx_DComplexType.__init__)


def test_dmx_dcomplextype_constructor_args():
    sig = inspect.signature(dmx_DComplexType.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dnamedelement_is_not_abstract():
    assert not inspect.isabstract(dmx_DNamedElement)


def test_dmx_dnamedelement_constructor_exists():
    assert callable(dmx_DNamedElement.__init__)


def test_dmx_dnamedelement_constructor_args():
    sig = inspect.signature(dmx_DNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dtype_is_not_abstract():
    assert not inspect.isabstract(dmx_DType)


def test_dmx_dtype_constructor_exists():
    assert callable(dmx_DType.__init__)


def test_dmx_dtype_constructor_args():
    sig = inspect.signature(dmx_DType.__init__)
    params = list(sig.parameters.keys())



def test_dmx_istaticreferencetarget_is_not_abstract():
    assert not inspect.isabstract(dmx_IStaticReferenceTarget)


def test_dmx_istaticreferencetarget_constructor_exists():
    assert callable(dmx_IStaticReferenceTarget.__init__)


def test_dmx_istaticreferencetarget_constructor_args():
    sig = inspect.signature(dmx_IStaticReferenceTarget.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxcallarguments_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxCallArguments)


def test_dmx_dmxcallarguments_constructor_exists():
    assert callable(dmx_DmxCallArguments.__init__)


def test_dmx_dmxcallarguments_constructor_args():
    sig = inspect.signature(dmx_DmxCallArguments.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxfiltertypedescriptor_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxFilterTypeDescriptor)


def test_dmx_dmxfiltertypedescriptor_constructor_exists():
    assert callable(dmx_DmxFilterTypeDescriptor.__init__)


def test_dmx_dmxfiltertypedescriptor_constructor_args():
    sig = inspect.signature(dmx_DmxFilterTypeDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "single" in params, "Missing parameter 'single'"
    assert "collection" in params, "Missing parameter 'collection'"
    assert "multiTyped" in params, "Missing parameter 'multiTyped'"

def test_dmx_dmxfiltertypedescriptor_has_single():
    assert hasattr(dmx_DmxFilterTypeDescriptor, "single")
    descriptor = None
    for klass in dmx_DmxFilterTypeDescriptor.__mro__:
        if "single" in klass.__dict__:
            descriptor = klass.__dict__["single"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxfiltertypedescriptor_has_collection():
    assert hasattr(dmx_DmxFilterTypeDescriptor, "collection")
    descriptor = None
    for klass in dmx_DmxFilterTypeDescriptor.__mro__:
        if "collection" in klass.__dict__:
            descriptor = klass.__dict__["collection"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxfiltertypedescriptor_has_multiTyped():
    assert hasattr(dmx_DmxFilterTypeDescriptor, "multiTyped")
    descriptor = None
    for klass in dmx_DmxFilterTypeDescriptor.__mro__:
        if "multiTyped" in klass.__dict__:
            descriptor = klass.__dict__["multiTyped"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxfilterparameter_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxFilterParameter)


def test_dmx_dmxfilterparameter_constructor_exists():
    assert callable(dmx_DmxFilterParameter.__init__)


def test_dmx_dmxfilterparameter_constructor_args():
    sig = inspect.signature(dmx_DmxFilterParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dmx_dmxfilterparameter_has_name():
    assert hasattr(dmx_DmxFilterParameter, "name")
    descriptor = None
    for klass in dmx_DmxFilterParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dnavigablemember_is_not_abstract():
    assert not inspect.isabstract(DNavigableMember)


def test_dnavigablemember_constructor_exists():
    assert callable(DNavigableMember.__init__)


def test_dnavigablemember_constructor_args():
    sig = inspect.signature(DNavigableMember.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxcorrelationvariable_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxCorrelationVariable)


def test_dmx_dmxcorrelationvariable_constructor_exists():
    assert callable(dmx_DmxCorrelationVariable.__init__)


def test_dmx_dmxcorrelationvariable_constructor_args():
    sig = inspect.signature(dmx_DmxCorrelationVariable.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxfield_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxField)


def test_dmx_dmxfield_constructor_exists():
    assert callable(dmx_DmxField.__init__)


def test_dmx_dmxfield_constructor_args():
    sig = inspect.signature(dmx_DmxField.__init__)
    params = list(sig.parameters.keys())



def test_dprimitive_is_not_abstract():
    assert not inspect.isabstract(DPrimitive)


def test_dprimitive_constructor_exists():
    assert callable(DPrimitive.__init__)


def test_dprimitive_constructor_args():
    sig = inspect.signature(DPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxarchetype_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxArchetype)


def test_dmx_dmxarchetype_constructor_exists():
    assert callable(dmx_DmxArchetype.__init__)


def test_dmx_dmxarchetype_constructor_args():
    sig = inspect.signature(dmx_DmxArchetype.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"

def test_dmx_dmxarchetype_has_baseType():
    assert hasattr(dmx_DmxArchetype, "baseType")
    descriptor = None
    for klass in dmx_DmxArchetype.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dnavigablemember_is_not_abstract():
    assert not inspect.isabstract(dmx_DNavigableMember)


def test_dmx_dnavigablemember_constructor_exists():
    assert callable(dmx_DNavigableMember.__init__)


def test_dmx_dnavigablemember_constructor_args():
    sig = inspect.signature(dmx_DNavigableMember.__init__)
    params = list(sig.parameters.keys())



def test_dexpression_is_not_abstract():
    assert not inspect.isabstract(DExpression)


def test_dexpression_constructor_exists():
    assert callable(DExpression.__init__)


def test_dexpression_constructor_args():
    sig = inspect.signature(DExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxdateliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxDateLiteral)


def test_dmx_dmxdateliteral_constructor_exists():
    assert callable(dmx_DmxDateLiteral.__init__)


def test_dmx_dmxdateliteral_constructor_args():
    sig = inspect.signature(dmx_DmxDateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dmx_dmxdateliteral_has_value():
    assert hasattr(dmx_DmxDateLiteral, "value")
    descriptor = None
    for klass in dmx_DmxDateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxundefinedliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxUndefinedLiteral)


def test_dmx_dmxundefinedliteral_constructor_exists():
    assert callable(dmx_DmxUndefinedLiteral.__init__)


def test_dmx_dmxundefinedliteral_constructor_args():
    sig = inspect.signature(dmx_DmxUndefinedLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxlistexpression_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxListExpression)


def test_dmx_dmxlistexpression_constructor_exists():
    assert callable(dmx_DmxListExpression.__init__)


def test_dmx_dmxlistexpression_constructor_args():
    sig = inspect.signature(dmx_DmxListExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxnaturalliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxNaturalLiteral)


def test_dmx_dmxnaturalliteral_constructor_exists():
    assert callable(dmx_DmxNaturalLiteral.__init__)


def test_dmx_dmxnaturalliteral_constructor_args():
    sig = inspect.signature(dmx_DmxNaturalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dmx_dmxnaturalliteral_has_value():
    assert hasattr(dmx_DmxNaturalLiteral, "value")
    descriptor = None
    for klass in dmx_DmxNaturalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxstaticreference_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxStaticReference)


def test_dmx_dmxstaticreference_constructor_exists():
    assert callable(dmx_DmxStaticReference.__init__)


def test_dmx_dmxstaticreference_constructor_args():
    sig = inspect.signature(dmx_DmxStaticReference.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "plural" in params, "Missing parameter 'plural'"

def test_dmx_dmxstaticreference_has_displayName():
    assert hasattr(dmx_DmxStaticReference, "displayName")
    descriptor = None
    for klass in dmx_DmxStaticReference.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxstaticreference_has_plural():
    assert hasattr(dmx_DmxStaticReference, "plural")
    descriptor = None
    for klass in dmx_DmxStaticReference.__mro__:
        if "plural" in klass.__dict__:
            descriptor = klass.__dict__["plural"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxurlliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxUrlLiteral)


def test_dmx_dmxurlliteral_constructor_exists():
    assert callable(dmx_DmxUrlLiteral.__init__)


def test_dmx_dmxurlliteral_constructor_args():
    sig = inspect.signature(dmx_DmxUrlLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "display" in params, "Missing parameter 'display'"

def test_dmx_dmxurlliteral_has_value():
    assert hasattr(dmx_DmxUrlLiteral, "value")
    descriptor = None
    for klass in dmx_DmxUrlLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxurlliteral_has_display():
    assert hasattr(dmx_DmxUrlLiteral, "display")
    descriptor = None
    for klass in dmx_DmxUrlLiteral.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxBooleanLiteral)


def test_dmx_dmxbooleanliteral_constructor_exists():
    assert callable(dmx_DmxBooleanLiteral.__init__)


def test_dmx_dmxbooleanliteral_constructor_args():
    sig = inspect.signature(dmx_DmxBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dmx_dmxbooleanliteral_has_value():
    assert hasattr(dmx_DmxBooleanLiteral, "value")
    descriptor = None
    for klass in dmx_DmxBooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxcontextreference_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxContextReference)


def test_dmx_dmxcontextreference_constructor_exists():
    assert callable(dmx_DmxContextReference.__init__)


def test_dmx_dmxcontextreference_constructor_args():
    sig = inspect.signature(dmx_DmxContextReference.__init__)
    params = list(sig.parameters.keys())
    assert "before" in params, "Missing parameter 'before'"
    assert "all" in params, "Missing parameter 'all'"

def test_dmx_dmxcontextreference_has_before():
    assert hasattr(dmx_DmxContextReference, "before")
    descriptor = None
    for klass in dmx_DmxContextReference.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxcontextreference_has_all():
    assert hasattr(dmx_DmxContextReference, "all")
    descriptor = None
    for klass in dmx_DmxContextReference.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxdecimalliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxDecimalLiteral)


def test_dmx_dmxdecimalliteral_constructor_exists():
    assert callable(dmx_DmxDecimalLiteral.__init__)


def test_dmx_dmxdecimalliteral_constructor_args():
    sig = inspect.signature(dmx_DmxDecimalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dmx_dmxdecimalliteral_has_value():
    assert hasattr(dmx_DmxDecimalLiteral, "value")
    descriptor = None
    for klass in dmx_DmxDecimalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxcastexpression_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxCastExpression)


def test_dmx_dmxcastexpression_constructor_exists():
    assert callable(dmx_DmxCastExpression.__init__)


def test_dmx_dmxcastexpression_constructor_args():
    sig = inspect.signature(dmx_DmxCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxstringliteral_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxStringLiteral)


def test_dmx_dmxstringliteral_constructor_exists():
    assert callable(dmx_DmxStringLiteral.__init__)


def test_dmx_dmxstringliteral_constructor_args():
    sig = inspect.signature(dmx_DmxStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dmx_dmxstringliteral_has_value():
    assert hasattr(dmx_DmxStringLiteral, "value")
    descriptor = None
    for klass in dmx_DmxStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxinstanceofexpression_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxInstanceOfExpression)


def test_dmx_dmxinstanceofexpression_constructor_exists():
    assert callable(dmx_DmxInstanceOfExpression.__init__)


def test_dmx_dmxinstanceofexpression_constructor_args():
    sig = inspect.signature(dmx_DmxInstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxmembernavigation_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxMemberNavigation)


def test_dmx_dmxmembernavigation_constructor_exists():
    assert callable(dmx_DmxMemberNavigation.__init__)


def test_dmx_dmxmembernavigation_constructor_args():
    sig = inspect.signature(dmx_DmxMemberNavigation.__init__)
    params = list(sig.parameters.keys())
    assert "before" in params, "Missing parameter 'before'"
    assert "explicitOperationCall" in params, "Missing parameter 'explicitOperationCall'"

def test_dmx_dmxmembernavigation_has_before():
    assert hasattr(dmx_DmxMemberNavigation, "before")
    descriptor = None
    for klass in dmx_DmxMemberNavigation.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxmembernavigation_has_explicitOperationCall():
    assert hasattr(dmx_DmxMemberNavigation, "explicitOperationCall")
    descriptor = None
    for klass in dmx_DmxMemberNavigation.__mro__:
        if "explicitOperationCall" in klass.__dict__:
            descriptor = klass.__dict__["explicitOperationCall"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxifexpression_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxIfExpression)


def test_dmx_dmxifexpression_constructor_exists():
    assert callable(dmx_DmxIfExpression.__init__)


def test_dmx_dmxifexpression_constructor_args():
    sig = inspect.signature(dmx_DmxIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxfunctioncall_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxFunctionCall)


def test_dmx_dmxfunctioncall_constructor_exists():
    assert callable(dmx_DmxFunctionCall.__init__)


def test_dmx_dmxfunctioncall_constructor_args():
    sig = inspect.signature(dmx_DmxFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxunaryoperation_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxUnaryOperation)


def test_dmx_dmxunaryoperation_constructor_exists():
    assert callable(dmx_DmxUnaryOperation.__init__)


def test_dmx_dmxunaryoperation_constructor_args():
    sig = inspect.signature(dmx_DmxUnaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dmx_dmxunaryoperation_has_operator():
    assert hasattr(dmx_DmxUnaryOperation, "operator")
    descriptor = None
    for klass in dmx_DmxUnaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxbinaryoperation_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxBinaryOperation)


def test_dmx_dmxbinaryoperation_constructor_exists():
    assert callable(dmx_DmxBinaryOperation.__init__)


def test_dmx_dmxbinaryoperation_constructor_args():
    sig = inspect.signature(dmx_DmxBinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dmx_dmxbinaryoperation_has_operator():
    assert hasattr(dmx_DmxBinaryOperation, "operator")
    descriptor = None
    for klass in dmx_DmxBinaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxassignment_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxAssignment)


def test_dmx_dmxassignment_constructor_exists():
    assert callable(dmx_DmxAssignment.__init__)


def test_dmx_dmxassignment_constructor_args():
    sig = inspect.signature(dmx_DmxAssignment.__init__)
    params = list(sig.parameters.keys())



def test_dcontext_is_not_abstract():
    assert not inspect.isabstract(DContext)


def test_dcontext_constructor_exists():
    assert callable(DContext.__init__)


def test_dcontext_constructor_args():
    sig = inspect.signature(DContext.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dexpression_is_not_abstract():
    assert not inspect.isabstract(dmx_DExpression)


def test_dmx_dexpression_constructor_exists():
    assert callable(dmx_DExpression.__init__)


def test_dmx_dexpression_constructor_args():
    sig = inspect.signature(dmx_DExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxtestcontext_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxTestContext)


def test_dmx_dmxtestcontext_constructor_exists():
    assert callable(dmx_DmxTestContext.__init__)


def test_dmx_dmxtestcontext_constructor_args():
    sig = inspect.signature(dmx_DmxTestContext.__init__)
    params = list(sig.parameters.keys())



def test_inavigablemembercontainer_is_not_abstract():
    assert not inspect.isabstract(INavigableMemberContainer)


def test_inavigablemembercontainer_constructor_exists():
    assert callable(INavigableMemberContainer.__init__)


def test_inavigablemembercontainer_constructor_args():
    sig = inspect.signature(INavigableMemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxpredicatewithcorrelationvariable_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxPredicateWithCorrelationVariable)


def test_dmx_dmxpredicatewithcorrelationvariable_constructor_exists():
    assert callable(dmx_DmxPredicateWithCorrelationVariable.__init__)


def test_dmx_dmxpredicatewithcorrelationvariable_constructor_args():
    sig = inspect.signature(dmx_DmxPredicateWithCorrelationVariable.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxcomplexobject_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxComplexObject)


def test_dmx_dmxcomplexobject_constructor_exists():
    assert callable(dmx_DmxComplexObject.__init__)


def test_dmx_dmxcomplexobject_constructor_args():
    sig = inspect.signature(dmx_DmxComplexObject.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxtest_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxTest)


def test_dmx_dmxtest_constructor_exists():
    assert callable(dmx_DmxTest.__init__)


def test_dmx_dmxtest_constructor_args():
    sig = inspect.signature(dmx_DmxTest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dmx_dmxtest_has_name():
    assert hasattr(dmx_DmxTest, "name")
    descriptor = None
    for klass in dmx_DmxTest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dmx_dmxfilter_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxFilter)


def test_dmx_dmxfilter_constructor_exists():
    assert callable(dmx_DmxFilter.__init__)


def test_dmx_dmxfilter_constructor_args():
    sig = inspect.signature(dmx_DmxFilter.__init__)
    params = list(sig.parameters.keys())



def test_itypecontainer_is_not_abstract():
    assert not inspect.isabstract(ITypeContainer)


def test_itypecontainer_constructor_exists():
    assert callable(ITypeContainer.__init__)


def test_itypecontainer_constructor_args():
    sig = inspect.signature(ITypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_dmodel_is_not_abstract():
    assert not inspect.isabstract(DModel)


def test_dmodel_constructor_exists():
    assert callable(DModel.__init__)


def test_dmodel_constructor_args():
    sig = inspect.signature(DModel.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxmodel_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxModel)


def test_dmx_dmxmodel_constructor_exists():
    assert callable(dmx_DmxModel.__init__)


def test_dmx_dmxmodel_constructor_args():
    sig = inspect.signature(dmx_DmxModel.__init__)
    params = list(sig.parameters.keys())



def test_dmx_dmxbasetypeset_is_not_abstract():
    assert not inspect.isabstract(dmx_DmxBaseTypeSet)


def test_dmx_dmxbasetypeset_constructor_exists():
    assert callable(dmx_DmxBaseTypeSet.__init__)


def test_dmx_dmxbasetypeset_constructor_args():
    sig = inspect.signature(dmx_DmxBaseTypeSet.__init__)
    params = list(sig.parameters.keys())
    assert "members" in params, "Missing parameter 'members'"
    assert "name" in params, "Missing parameter 'name'"

def test_dmx_dmxbasetypeset_has_members():
    assert hasattr(dmx_DmxBaseTypeSet, "members")
    descriptor = None
    for klass in dmx_DmxBaseTypeSet.__mro__:
        if "members" in klass.__dict__:
            descriptor = klass.__dict__["members"]
            break
    assert isinstance(descriptor, property)

def test_dmx_dmxbasetypeset_has_name():
    assert hasattr(dmx_DmxBaseTypeSet, "name")
    descriptor = None
    for klass in dmx_DmxBaseTypeSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dmxbinaryoperator_exists():
    # Check that the Enumeration exists
    assert DmxBinaryOperator is not None

def test_dmxbinaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DmxBinaryOperator]
    expected_literals = [
        "POWER",
        "XOR",
        "DIVIDE",
        "UNTIL",
        "MULTIPLY",
        "SUBTRACT",
        "DOUBLE_ARROW",
        "OR",
        "GREATER_OR_EQUAL",
        "SINGLE_ARROW",
        "NOT_EQUAL",
        "MODULO",
        "LESS",
        "GREATER",
        "AND",
        "EQUAL",
        "ADD",
        "LESS_OR_EQUAL",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DmxBinaryOperator"

def test_dmxunaryoperator_exists():
    # Check that the Enumeration exists
    assert DmxUnaryOperator is not None

def test_dmxunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DmxUnaryOperator]
    expected_literals = [
        "NOT",
        "PLUS",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DmxUnaryOperator"

def test_dmxbasetype_exists():
    # Check that the Enumeration exists
    assert DmxBaseType is not None

def test_dmxbasetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DmxBaseType]
    expected_literals = [
        "STATE",
        "UNDEFINED",
        "IDENTIFIER",
        "AGGREGATE",
        "AMBIGUOUS",
        "STATE_EVENT",
        "COMPLEX",
        "TIMEPOINT",
        "ENUM",
        "VOID",
        "BOOLEAN",
        "NUMBER",
        "NOTIFICATION",
        "SERVICE",
        "TEXT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DmxBaseType"


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
DmxComplexObject_strategy = st.builds(
    DmxComplexObject,
)
dmx_DmxDetail_strategy = st.builds(
    dmx_DmxDetail,
)
dmx_DmxEntity_strategy = st.builds(
    dmx_DmxEntity,
)
dmx_DFeature_strategy = st.builds(
    dmx_DFeature,
)
dmx_DComplexType_strategy = st.builds(
    dmx_DComplexType,
)
dmx_DNamedElement_strategy = st.builds(
    dmx_DNamedElement,
)
dmx_DType_strategy = st.builds(
    dmx_DType,
)
dmx_IStaticReferenceTarget_strategy = st.builds(
    dmx_IStaticReferenceTarget,
)
dmx_DmxCallArguments_strategy = st.builds(
    dmx_DmxCallArguments,
)
dmx_DmxFilterTypeDescriptor_strategy = st.builds(
    dmx_DmxFilterTypeDescriptor,
    single=
        safe_text,
    collection=
        st.booleans(),
    multiTyped=
        st.booleans()
)
dmx_DmxFilterParameter_strategy = st.builds(
    dmx_DmxFilterParameter,
    name=
        safe_text
)
DNavigableMember_strategy = st.builds(
    DNavigableMember,
)
dmx_DmxCorrelationVariable_strategy = st.builds(
    dmx_DmxCorrelationVariable,
)
dmx_DmxField_strategy = st.builds(
    dmx_DmxField,
)
DPrimitive_strategy = st.builds(
    DPrimitive,
)
dmx_DmxArchetype_strategy = st.builds(
    dmx_DmxArchetype,
    baseType=
        safe_text
)
dmx_DNavigableMember_strategy = st.builds(
    dmx_DNavigableMember,
)
DExpression_strategy = st.builds(
    DExpression,
)
dmx_DmxDateLiteral_strategy = st.builds(
    dmx_DmxDateLiteral,
    value=
        st.dates()
)
dmx_DmxUndefinedLiteral_strategy = st.builds(
    dmx_DmxUndefinedLiteral,
)
dmx_DmxListExpression_strategy = st.builds(
    dmx_DmxListExpression,
)
dmx_DmxNaturalLiteral_strategy = st.builds(
    dmx_DmxNaturalLiteral,
    value=
        st.integers()
)
dmx_DmxStaticReference_strategy = st.builds(
    dmx_DmxStaticReference,
    displayName=
        safe_text,
    plural=
        st.booleans()
)
dmx_DmxUrlLiteral_strategy = st.builds(
    dmx_DmxUrlLiteral,
    value=
        safe_text,
    display=
        safe_text
)
dmx_DmxBooleanLiteral_strategy = st.builds(
    dmx_DmxBooleanLiteral,
    value=
        st.booleans()
)
dmx_DmxContextReference_strategy = st.builds(
    dmx_DmxContextReference,
    before=
        st.booleans(),
    all=
        st.booleans()
)
dmx_DmxDecimalLiteral_strategy = st.builds(
    dmx_DmxDecimalLiteral,
    value=
        safe_text
)
dmx_DmxCastExpression_strategy = st.builds(
    dmx_DmxCastExpression,
)
dmx_DmxStringLiteral_strategy = st.builds(
    dmx_DmxStringLiteral,
    value=
        safe_text
)
dmx_DmxInstanceOfExpression_strategy = st.builds(
    dmx_DmxInstanceOfExpression,
)
dmx_DmxMemberNavigation_strategy = st.builds(
    dmx_DmxMemberNavigation,
    before=
        st.booleans(),
    explicitOperationCall=
        st.booleans()
)
dmx_DmxIfExpression_strategy = st.builds(
    dmx_DmxIfExpression,
)
dmx_DmxFunctionCall_strategy = st.builds(
    dmx_DmxFunctionCall,
)
dmx_DmxUnaryOperation_strategy = st.builds(
    dmx_DmxUnaryOperation,
    operator=
        safe_text
)
dmx_DmxBinaryOperation_strategy = st.builds(
    dmx_DmxBinaryOperation,
    operator=
        safe_text
)
dmx_DmxAssignment_strategy = st.builds(
    dmx_DmxAssignment,
)
DContext_strategy = st.builds(
    DContext,
)
dmx_DExpression_strategy = st.builds(
    dmx_DExpression,
)
dmx_DmxTestContext_strategy = st.builds(
    dmx_DmxTestContext,
)
INavigableMemberContainer_strategy = st.builds(
    INavigableMemberContainer,
)
dmx_DmxPredicateWithCorrelationVariable_strategy = st.builds(
    dmx_DmxPredicateWithCorrelationVariable,
)
dmx_DmxComplexObject_strategy = st.builds(
    dmx_DmxComplexObject,
)
dmx_DmxTest_strategy = st.builds(
    dmx_DmxTest,
    name=
        safe_text
)
dmx_DmxFilter_strategy = st.builds(
    dmx_DmxFilter,
)
ITypeContainer_strategy = st.builds(
    ITypeContainer,
)
DModel_strategy = st.builds(
    DModel,
)
dmx_DmxModel_strategy = st.builds(
    dmx_DmxModel,
)
dmx_DmxBaseTypeSet_strategy = st.builds(
    dmx_DmxBaseTypeSet,
    members=
        safe_text,
    name=
        safe_text
)

@given(instance=DmxComplexObject_strategy)
@settings(max_examples=50)
def test_dmxcomplexobject_instantiation(instance):
    assert isinstance(instance, DmxComplexObject)

@given(instance=dmx_DmxDetail_strategy)
@settings(max_examples=50)
def test_dmx_dmxdetail_instantiation(instance):
    assert isinstance(instance, dmx_DmxDetail)

@given(instance=dmx_DmxEntity_strategy)
@settings(max_examples=50)
def test_dmx_dmxentity_instantiation(instance):
    assert isinstance(instance, dmx_DmxEntity)

@given(instance=dmx_DFeature_strategy)
@settings(max_examples=50)
def test_dmx_dfeature_instantiation(instance):
    assert isinstance(instance, dmx_DFeature)

@given(instance=dmx_DComplexType_strategy)
@settings(max_examples=50)
def test_dmx_dcomplextype_instantiation(instance):
    assert isinstance(instance, dmx_DComplexType)

@given(instance=dmx_DNamedElement_strategy)
@settings(max_examples=50)
def test_dmx_dnamedelement_instantiation(instance):
    assert isinstance(instance, dmx_DNamedElement)

@given(instance=dmx_DType_strategy)
@settings(max_examples=50)
def test_dmx_dtype_instantiation(instance):
    assert isinstance(instance, dmx_DType)

@given(instance=dmx_IStaticReferenceTarget_strategy)
@settings(max_examples=50)
def test_dmx_istaticreferencetarget_instantiation(instance):
    assert isinstance(instance, dmx_IStaticReferenceTarget)

@given(instance=dmx_DmxCallArguments_strategy)
@settings(max_examples=50)
def test_dmx_dmxcallarguments_instantiation(instance):
    assert isinstance(instance, dmx_DmxCallArguments)

@given(instance=dmx_DmxFilterTypeDescriptor_strategy)
@settings(max_examples=50)
def test_dmx_dmxfiltertypedescriptor_instantiation(instance):
    assert isinstance(instance, dmx_DmxFilterTypeDescriptor)



@given(instance=dmx_DmxFilterTypeDescriptor_strategy)
def test_dmx_dmxfiltertypedescriptor_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original



@given(instance=dmx_DmxFilterTypeDescriptor_strategy)
def test_dmx_dmxfiltertypedescriptor_collection_setter(instance):
    original = instance.collection
    instance.collection = original
    assert instance.collection == original



@given(instance=dmx_DmxFilterTypeDescriptor_strategy)
def test_dmx_dmxfiltertypedescriptor_multiTyped_setter(instance):
    original = instance.multiTyped
    instance.multiTyped = original
    assert instance.multiTyped == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dmx_DmxFilterTypeDescriptor_strategy)
@settings(max_examples=30)
def test_dmx_dmxfiltertypedescriptor_iscompatible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isCompatible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isCompatible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isCompatible' in dmx_DmxFilterTypeDescriptor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isCompatible' in dmx_DmxFilterTypeDescriptor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isCompatible' in dmx_DmxFilterTypeDescriptor is not implemented or raised an error")

@given(instance=dmx_DmxFilterParameter_strategy)
@settings(max_examples=50)
def test_dmx_dmxfilterparameter_instantiation(instance):
    assert isinstance(instance, dmx_DmxFilterParameter)



@given(instance=dmx_DmxFilterParameter_strategy)
def test_dmx_dmxfilterparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DNavigableMember_strategy)
@settings(max_examples=50)
def test_dnavigablemember_instantiation(instance):
    assert isinstance(instance, DNavigableMember)

@given(instance=dmx_DmxCorrelationVariable_strategy)
@settings(max_examples=50)
def test_dmx_dmxcorrelationvariable_instantiation(instance):
    assert isinstance(instance, dmx_DmxCorrelationVariable)

@given(instance=dmx_DmxField_strategy)
@settings(max_examples=50)
def test_dmx_dmxfield_instantiation(instance):
    assert isinstance(instance, dmx_DmxField)

@given(instance=DPrimitive_strategy)
@settings(max_examples=50)
def test_dprimitive_instantiation(instance):
    assert isinstance(instance, DPrimitive)

@given(instance=dmx_DmxArchetype_strategy)
@settings(max_examples=50)
def test_dmx_dmxarchetype_instantiation(instance):
    assert isinstance(instance, dmx_DmxArchetype)



@given(instance=dmx_DmxArchetype_strategy)
def test_dmx_dmxarchetype_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=dmx_DNavigableMember_strategy)
@settings(max_examples=50)
def test_dmx_dnavigablemember_instantiation(instance):
    assert isinstance(instance, dmx_DNavigableMember)

@given(instance=DExpression_strategy)
@settings(max_examples=50)
def test_dexpression_instantiation(instance):
    assert isinstance(instance, DExpression)

@given(instance=dmx_DmxDateLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxdateliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxDateLiteral)



@given(instance=dmx_DmxDateLiteral_strategy)
def test_dmx_dmxdateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dmx_DmxUndefinedLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxundefinedliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxUndefinedLiteral)

@given(instance=dmx_DmxListExpression_strategy)
@settings(max_examples=50)
def test_dmx_dmxlistexpression_instantiation(instance):
    assert isinstance(instance, dmx_DmxListExpression)

@given(instance=dmx_DmxNaturalLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxnaturalliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxNaturalLiteral)



@given(instance=dmx_DmxNaturalLiteral_strategy)
def test_dmx_dmxnaturalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dmx_DmxStaticReference_strategy)
@settings(max_examples=50)
def test_dmx_dmxstaticreference_instantiation(instance):
    assert isinstance(instance, dmx_DmxStaticReference)



@given(instance=dmx_DmxStaticReference_strategy)
def test_dmx_dmxstaticreference_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=dmx_DmxStaticReference_strategy)
def test_dmx_dmxstaticreference_plural_setter(instance):
    original = instance.plural
    instance.plural = original
    assert instance.plural == original

@given(instance=dmx_DmxUrlLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxurlliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxUrlLiteral)



@given(instance=dmx_DmxUrlLiteral_strategy)
def test_dmx_dmxurlliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=dmx_DmxUrlLiteral_strategy)
def test_dmx_dmxurlliteral_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original

@given(instance=dmx_DmxBooleanLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxbooleanliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxBooleanLiteral)



@given(instance=dmx_DmxBooleanLiteral_strategy)
def test_dmx_dmxbooleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dmx_DmxContextReference_strategy)
@settings(max_examples=50)
def test_dmx_dmxcontextreference_instantiation(instance):
    assert isinstance(instance, dmx_DmxContextReference)



@given(instance=dmx_DmxContextReference_strategy)
def test_dmx_dmxcontextreference_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original



@given(instance=dmx_DmxContextReference_strategy)
def test_dmx_dmxcontextreference_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=dmx_DmxDecimalLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxdecimalliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxDecimalLiteral)



@given(instance=dmx_DmxDecimalLiteral_strategy)
def test_dmx_dmxdecimalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dmx_DmxCastExpression_strategy)
@settings(max_examples=50)
def test_dmx_dmxcastexpression_instantiation(instance):
    assert isinstance(instance, dmx_DmxCastExpression)

@given(instance=dmx_DmxStringLiteral_strategy)
@settings(max_examples=50)
def test_dmx_dmxstringliteral_instantiation(instance):
    assert isinstance(instance, dmx_DmxStringLiteral)



@given(instance=dmx_DmxStringLiteral_strategy)
def test_dmx_dmxstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dmx_DmxInstanceOfExpression_strategy)
@settings(max_examples=50)
def test_dmx_dmxinstanceofexpression_instantiation(instance):
    assert isinstance(instance, dmx_DmxInstanceOfExpression)

@given(instance=dmx_DmxMemberNavigation_strategy)
@settings(max_examples=50)
def test_dmx_dmxmembernavigation_instantiation(instance):
    assert isinstance(instance, dmx_DmxMemberNavigation)



@given(instance=dmx_DmxMemberNavigation_strategy)
def test_dmx_dmxmembernavigation_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original



@given(instance=dmx_DmxMemberNavigation_strategy)
def test_dmx_dmxmembernavigation_explicitOperationCall_setter(instance):
    original = instance.explicitOperationCall
    instance.explicitOperationCall = original
    assert instance.explicitOperationCall == original

@given(instance=dmx_DmxIfExpression_strategy)
@settings(max_examples=50)
def test_dmx_dmxifexpression_instantiation(instance):
    assert isinstance(instance, dmx_DmxIfExpression)

@given(instance=dmx_DmxFunctionCall_strategy)
@settings(max_examples=50)
def test_dmx_dmxfunctioncall_instantiation(instance):
    assert isinstance(instance, dmx_DmxFunctionCall)

@given(instance=dmx_DmxUnaryOperation_strategy)
@settings(max_examples=50)
def test_dmx_dmxunaryoperation_instantiation(instance):
    assert isinstance(instance, dmx_DmxUnaryOperation)



@given(instance=dmx_DmxUnaryOperation_strategy)
def test_dmx_dmxunaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dmx_DmxBinaryOperation_strategy)
@settings(max_examples=50)
def test_dmx_dmxbinaryoperation_instantiation(instance):
    assert isinstance(instance, dmx_DmxBinaryOperation)



@given(instance=dmx_DmxBinaryOperation_strategy)
def test_dmx_dmxbinaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dmx_DmxAssignment_strategy)
@settings(max_examples=50)
def test_dmx_dmxassignment_instantiation(instance):
    assert isinstance(instance, dmx_DmxAssignment)

@given(instance=DContext_strategy)
@settings(max_examples=50)
def test_dcontext_instantiation(instance):
    assert isinstance(instance, DContext)

@given(instance=dmx_DExpression_strategy)
@settings(max_examples=50)
def test_dmx_dexpression_instantiation(instance):
    assert isinstance(instance, dmx_DExpression)

@given(instance=dmx_DmxTestContext_strategy)
@settings(max_examples=50)
def test_dmx_dmxtestcontext_instantiation(instance):
    assert isinstance(instance, dmx_DmxTestContext)

@given(instance=INavigableMemberContainer_strategy)
@settings(max_examples=50)
def test_inavigablemembercontainer_instantiation(instance):
    assert isinstance(instance, INavigableMemberContainer)

@given(instance=dmx_DmxPredicateWithCorrelationVariable_strategy)
@settings(max_examples=50)
def test_dmx_dmxpredicatewithcorrelationvariable_instantiation(instance):
    assert isinstance(instance, dmx_DmxPredicateWithCorrelationVariable)

@given(instance=dmx_DmxComplexObject_strategy)
@settings(max_examples=50)
def test_dmx_dmxcomplexobject_instantiation(instance):
    assert isinstance(instance, dmx_DmxComplexObject)

@given(instance=dmx_DmxTest_strategy)
@settings(max_examples=50)
def test_dmx_dmxtest_instantiation(instance):
    assert isinstance(instance, dmx_DmxTest)



@given(instance=dmx_DmxTest_strategy)
def test_dmx_dmxtest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dmx_DmxFilter_strategy)
@settings(max_examples=50)
def test_dmx_dmxfilter_instantiation(instance):
    assert isinstance(instance, dmx_DmxFilter)

@given(instance=ITypeContainer_strategy)
@settings(max_examples=50)
def test_itypecontainer_instantiation(instance):
    assert isinstance(instance, ITypeContainer)

@given(instance=DModel_strategy)
@settings(max_examples=50)
def test_dmodel_instantiation(instance):
    assert isinstance(instance, DModel)

@given(instance=dmx_DmxModel_strategy)
@settings(max_examples=50)
def test_dmx_dmxmodel_instantiation(instance):
    assert isinstance(instance, dmx_DmxModel)

@given(instance=dmx_DmxBaseTypeSet_strategy)
@settings(max_examples=50)
def test_dmx_dmxbasetypeset_instantiation(instance):
    assert isinstance(instance, dmx_DmxBaseTypeSet)



@given(instance=dmx_DmxBaseTypeSet_strategy)
def test_dmx_dmxbasetypeset_members_setter(instance):
    original = instance.members
    instance.members = original
    assert instance.members == original



@given(instance=dmx_DmxBaseTypeSet_strategy)
def test_dmx_dmxbasetypeset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
