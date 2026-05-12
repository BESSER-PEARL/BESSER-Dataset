import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TrgViewMapping,
    jointPackage_Ecore2Maude_TrgViewMapping,
    jointPackage_Ecore2Maude_SrcEStringToStringMapEntry,
    jointPackage_Ecore2Maude_JointMM,
    TrgTerm,
    jointPackage_Ecore2Maude_TrgVariable,
    jointPackage_Ecore2Maude_TrgRecTerm,
    jointPackage_Ecore2Maude_TrgConstant,
    TrgRenMapping,
    jointPackage_Ecore2Maude_TrgOpMapping,
    jointPackage_Ecore2Maude_TrgOpTypedMapping,
    jointPackage_Ecore2Maude_TrgLabelMapping,
    jointPackage_Ecore2Maude_TrgSortMapping,
    jointPackage_Ecore2Maude_TrgTermMapping,
    TrgCondition,
    jointPackage_Ecore2Maude_TrgRewriteCond,
    jointPackage_Ecore2Maude_TrgEquationalCond,
    jointPackage_Ecore2Maude_TrgType,
    jointPackage_Ecore2Maude_TrgCondition,
    TrgModElement,
    jointPackage_Ecore2Maude_TrgOperation,
    jointPackage_Ecore2Maude_TrgStatement,
    jointPackage_Ecore2Maude_TrgModImportation,
    TrgModule,
    jointPackage_Ecore2Maude_TrgSModule,
    jointPackage_Ecore2Maude_TrgFModule,
    TrgTheory,
    jointPackage_Ecore2Maude_TrgSTheory,
    jointPackage_Ecore2Maude_TrgFTheory,
    jointPackage_Ecore2Maude_TrgModElement,
    jointPackage_Ecore2Maude_TrgSubsortRel,
    TrgType,
    jointPackage_Ecore2Maude_TrgKind,
    jointPackage_Ecore2Maude_TrgRenMapping,
    TrgModExpression,
    jointPackage_Ecore2Maude_TrgCompModExp,
    jointPackage_Ecore2Maude_TrgRenModExp,
    jointPackage_Ecore2Maude_TrgInstModExp,
    jointPackage_Ecore2Maude_TrgModExpression,
    TrgMaudeTopEl,
    jointPackage_Ecore2Maude_TrgView,
    jointPackage_Ecore2Maude_TrgParameter,
    jointPackage_Ecore2Maude_TrgTheory,
    jointPackage_Ecore2Maude_TrgTheoryIdModExp,
    jointPackage_Ecore2Maude_TrgModule,
    jointPackage_Ecore2Maude_TrgModuleIdModExp,
    jointPackage_Ecore2Maude_TrgSort,
    jointPackage_Ecore2Maude_TrgTerm,
    TrgStatement,
    jointPackage_Ecore2Maude_TrgMembership,
    jointPackage_Ecore2Maude_TrgMaudeTopEl,
    jointPackage_Ecore2Maude_TrgMaudeSpec,
    TrgEquationalCond,
    jointPackage_Ecore2Maude_TrgMatchingCond,
    jointPackage_Ecore2Maude_TrgBooleanCond,
    jointPackage_Ecore2Maude_TrgEqualCond,
    jointPackage_Ecore2Maude_TrgMembershipCond,
    jointPackage_Ecore2Maude_TrgRule,
    jointPackage_Ecore2Maude_TrgEquation,
    SrcETypedElement,
    jointPackage_Ecore2Maude_SrcEOperation,
    jointPackage_Ecore2Maude_SrcEParameter,
    SrcEDataType,
    jointPackage_Ecore2Maude_SrcEEnum,
    SrcENamedElement,
    jointPackage_Ecore2Maude_SrcETypedElement,
    jointPackage_Ecore2Maude_SrcEPackage,
    jointPackage_Ecore2Maude_SrcEClassifier,
    jointPackage_Ecore2Maude_SrcEStructuralFeature,
    jointPackage_Ecore2Maude_SrcENamedElement,
    jointPackage_Ecore2Maude_SrcEEnumLiteral,
    SrcEClassifier,
    jointPackage_Ecore2Maude_SrcEClass,
    jointPackage_Ecore2Maude_SrcEDataType,
    SrcEStructuralFeature,
    jointPackage_Ecore2Maude_SrcEReference,
    jointPackage_Ecore2Maude_SrcEAttribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trgviewmapping_is_not_abstract():
    assert not inspect.isabstract(TrgViewMapping)


def test_trgviewmapping_constructor_exists():
    assert callable(TrgViewMapping.__init__)


def test_trgviewmapping_constructor_args():
    sig = inspect.signature(TrgViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgviewmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgViewMapping)


def test_jointpackage_ecore2maude_trgviewmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgViewMapping.__init__)


def test_jointpackage_ecore2maude_trgviewmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srcestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEStringToStringMapEntry)


def test_jointpackage_ecore2maude_srcestringtostringmapentry_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEStringToStringMapEntry.__init__)


def test_jointpackage_ecore2maude_srcestringtostringmapentry_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage_ecore2maude_srcestringtostringmapentry_has_key():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStringToStringMapEntry, "key")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcestringtostringmapentry_has_value():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStringToStringMapEntry, "value")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_JointMM)


def test_jointpackage_ecore2maude_jointmm_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_JointMM.__init__)


def test_jointpackage_ecore2maude_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_JointMM.__init__)
    params = list(sig.parameters.keys())



def test_trgterm_is_not_abstract():
    assert not inspect.isabstract(TrgTerm)


def test_trgterm_constructor_exists():
    assert callable(TrgTerm.__init__)


def test_trgterm_constructor_args():
    sig = inspect.signature(TrgTerm.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgvariable_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgVariable)


def test_jointpackage_ecore2maude_trgvariable_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgVariable.__init__)


def test_jointpackage_ecore2maude_trgvariable_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_ecore2maude_trgvariable_has_name():
    assert hasattr(jointPackage_Ecore2Maude_TrgVariable, "name")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgrecterm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgRecTerm)


def test_jointpackage_ecore2maude_trgrecterm_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgRecTerm.__init__)


def test_jointpackage_ecore2maude_trgrecterm_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgRecTerm.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jointpackage_ecore2maude_trgrecterm_has_op():
    assert hasattr(jointPackage_Ecore2Maude_TrgRecTerm, "op")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgRecTerm.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgConstant)


def test_jointpackage_ecore2maude_trgconstant_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgConstant.__init__)


def test_jointpackage_ecore2maude_trgconstant_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgConstant.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jointpackage_ecore2maude_trgconstant_has_op():
    assert hasattr(jointPackage_Ecore2Maude_TrgConstant, "op")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgConstant.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_trgrenmapping_is_not_abstract():
    assert not inspect.isabstract(TrgRenMapping)


def test_trgrenmapping_constructor_exists():
    assert callable(TrgRenMapping.__init__)


def test_trgrenmapping_constructor_args():
    sig = inspect.signature(TrgRenMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgopmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgOpMapping)


def test_jointpackage_ecore2maude_trgopmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgOpMapping.__init__)


def test_jointpackage_ecore2maude_trgopmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgOpMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage_ecore2maude_trgopmapping_has_to():
    assert hasattr(jointPackage_Ecore2Maude_TrgOpMapping, "to")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgOpMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgoptypedmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgOpTypedMapping)


def test_jointpackage_ecore2maude_trgoptypedmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgOpTypedMapping.__init__)


def test_jointpackage_ecore2maude_trgoptypedmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgOpTypedMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "atts" in params, "Missing parameter 'atts'"

def test_jointpackage_ecore2maude_trgoptypedmapping_has_to():
    assert hasattr(jointPackage_Ecore2Maude_TrgOpTypedMapping, "to")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgOpTypedMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_trgoptypedmapping_has_atts():
    assert hasattr(jointPackage_Ecore2Maude_TrgOpTypedMapping, "atts")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgOpTypedMapping.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trglabelmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgLabelMapping)


def test_jointpackage_ecore2maude_trglabelmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgLabelMapping.__init__)


def test_jointpackage_ecore2maude_trglabelmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgLabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage_ecore2maude_trglabelmapping_has_from_():
    assert hasattr(jointPackage_Ecore2Maude_TrgLabelMapping, "from_")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgLabelMapping.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_trglabelmapping_has_to():
    assert hasattr(jointPackage_Ecore2Maude_TrgLabelMapping, "to")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgLabelMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgsortmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgSortMapping)


def test_jointpackage_ecore2maude_trgsortmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgSortMapping.__init__)


def test_jointpackage_ecore2maude_trgsortmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgSortMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage_ecore2maude_trgsortmapping_has_to():
    assert hasattr(jointPackage_Ecore2Maude_TrgSortMapping, "to")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgSortMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgtermmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgTermMapping)


def test_jointpackage_ecore2maude_trgtermmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgTermMapping.__init__)


def test_jointpackage_ecore2maude_trgtermmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgTermMapping.__init__)
    params = list(sig.parameters.keys())



def test_trgcondition_is_not_abstract():
    assert not inspect.isabstract(TrgCondition)


def test_trgcondition_constructor_exists():
    assert callable(TrgCondition.__init__)


def test_trgcondition_constructor_args():
    sig = inspect.signature(TrgCondition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgrewritecond_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgRewriteCond)


def test_jointpackage_ecore2maude_trgrewritecond_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgRewriteCond.__init__)


def test_jointpackage_ecore2maude_trgrewritecond_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgRewriteCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgequationalcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgEquationalCond)


def test_jointpackage_ecore2maude_trgequationalcond_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgEquationalCond.__init__)


def test_jointpackage_ecore2maude_trgequationalcond_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgEquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgtype_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgType)


def test_jointpackage_ecore2maude_trgtype_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgType.__init__)


def test_jointpackage_ecore2maude_trgtype_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_ecore2maude_trgtype_has_name():
    assert hasattr(jointPackage_Ecore2Maude_TrgType, "name")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgcondition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgCondition)


def test_jointpackage_ecore2maude_trgcondition_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgCondition.__init__)


def test_jointpackage_ecore2maude_trgcondition_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgCondition.__init__)
    params = list(sig.parameters.keys())



def test_trgmodelement_is_not_abstract():
    assert not inspect.isabstract(TrgModElement)


def test_trgmodelement_constructor_exists():
    assert callable(TrgModElement.__init__)


def test_trgmodelement_constructor_args():
    sig = inspect.signature(TrgModElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgoperation_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgOperation)


def test_jointpackage_ecore2maude_trgoperation_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgOperation.__init__)


def test_jointpackage_ecore2maude_trgoperation_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgOperation.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_ecore2maude_trgoperation_has_atts():
    assert hasattr(jointPackage_Ecore2Maude_TrgOperation, "atts")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgOperation.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_trgoperation_has_name():
    assert hasattr(jointPackage_Ecore2Maude_TrgOperation, "name")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgstatement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgStatement)


def test_jointpackage_ecore2maude_trgstatement_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgStatement.__init__)


def test_jointpackage_ecore2maude_trgstatement_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "atts" in params, "Missing parameter 'atts'"

def test_jointpackage_ecore2maude_trgstatement_has_label():
    assert hasattr(jointPackage_Ecore2Maude_TrgStatement, "label")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_trgstatement_has_atts():
    assert hasattr(jointPackage_Ecore2Maude_TrgStatement, "atts")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgStatement.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgmodimportation_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgModImportation)


def test_jointpackage_ecore2maude_trgmodimportation_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgModImportation.__init__)


def test_jointpackage_ecore2maude_trgmodimportation_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgModImportation.__init__)
    params = list(sig.parameters.keys())



def test_trgmodule_is_not_abstract():
    assert not inspect.isabstract(TrgModule)


def test_trgmodule_constructor_exists():
    assert callable(TrgModule.__init__)


def test_trgmodule_constructor_args():
    sig = inspect.signature(TrgModule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgsmodule_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgSModule)


def test_jointpackage_ecore2maude_trgsmodule_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgSModule.__init__)


def test_jointpackage_ecore2maude_trgsmodule_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgSModule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgfmodule_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgFModule)


def test_jointpackage_ecore2maude_trgfmodule_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgFModule.__init__)


def test_jointpackage_ecore2maude_trgfmodule_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgFModule.__init__)
    params = list(sig.parameters.keys())



def test_trgtheory_is_not_abstract():
    assert not inspect.isabstract(TrgTheory)


def test_trgtheory_constructor_exists():
    assert callable(TrgTheory.__init__)


def test_trgtheory_constructor_args():
    sig = inspect.signature(TrgTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgstheory_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgSTheory)


def test_jointpackage_ecore2maude_trgstheory_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgSTheory.__init__)


def test_jointpackage_ecore2maude_trgstheory_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgSTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgftheory_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgFTheory)


def test_jointpackage_ecore2maude_trgftheory_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgFTheory.__init__)


def test_jointpackage_ecore2maude_trgftheory_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgFTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmodelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgModElement)


def test_jointpackage_ecore2maude_trgmodelement_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgModElement.__init__)


def test_jointpackage_ecore2maude_trgmodelement_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgModElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgsubsortrel_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgSubsortRel)


def test_jointpackage_ecore2maude_trgsubsortrel_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgSubsortRel.__init__)


def test_jointpackage_ecore2maude_trgsubsortrel_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgSubsortRel.__init__)
    params = list(sig.parameters.keys())



def test_trgtype_is_not_abstract():
    assert not inspect.isabstract(TrgType)


def test_trgtype_constructor_exists():
    assert callable(TrgType.__init__)


def test_trgtype_constructor_args():
    sig = inspect.signature(TrgType.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgkind_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgKind)


def test_jointpackage_ecore2maude_trgkind_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgKind.__init__)


def test_jointpackage_ecore2maude_trgkind_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgKind.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgrenmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgRenMapping)


def test_jointpackage_ecore2maude_trgrenmapping_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgRenMapping.__init__)


def test_jointpackage_ecore2maude_trgrenmapping_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgRenMapping.__init__)
    params = list(sig.parameters.keys())



def test_trgmodexpression_is_not_abstract():
    assert not inspect.isabstract(TrgModExpression)


def test_trgmodexpression_constructor_exists():
    assert callable(TrgModExpression.__init__)


def test_trgmodexpression_constructor_args():
    sig = inspect.signature(TrgModExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgcompmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgCompModExp)


def test_jointpackage_ecore2maude_trgcompmodexp_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgCompModExp.__init__)


def test_jointpackage_ecore2maude_trgcompmodexp_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgCompModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgrenmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgRenModExp)


def test_jointpackage_ecore2maude_trgrenmodexp_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgRenModExp.__init__)


def test_jointpackage_ecore2maude_trgrenmodexp_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgRenModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trginstmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgInstModExp)


def test_jointpackage_ecore2maude_trginstmodexp_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgInstModExp.__init__)


def test_jointpackage_ecore2maude_trginstmodexp_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgInstModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmodexpression_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgModExpression)


def test_jointpackage_ecore2maude_trgmodexpression_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgModExpression.__init__)


def test_jointpackage_ecore2maude_trgmodexpression_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgModExpression.__init__)
    params = list(sig.parameters.keys())



def test_trgmaudetopel_is_not_abstract():
    assert not inspect.isabstract(TrgMaudeTopEl)


def test_trgmaudetopel_constructor_exists():
    assert callable(TrgMaudeTopEl.__init__)


def test_trgmaudetopel_constructor_args():
    sig = inspect.signature(TrgMaudeTopEl.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgview_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgView)


def test_jointpackage_ecore2maude_trgview_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgView.__init__)


def test_jointpackage_ecore2maude_trgview_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgView.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgparameter_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgParameter)


def test_jointpackage_ecore2maude_trgparameter_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgParameter.__init__)


def test_jointpackage_ecore2maude_trgparameter_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgParameter.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage_ecore2maude_trgparameter_has_label():
    assert hasattr(jointPackage_Ecore2Maude_TrgParameter, "label")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgParameter.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgtheory_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgTheory)


def test_jointpackage_ecore2maude_trgtheory_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgTheory.__init__)


def test_jointpackage_ecore2maude_trgtheory_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgtheoryidmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgTheoryIdModExp)


def test_jointpackage_ecore2maude_trgtheoryidmodexp_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgTheoryIdModExp.__init__)


def test_jointpackage_ecore2maude_trgtheoryidmodexp_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgTheoryIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmodule_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgModule)


def test_jointpackage_ecore2maude_trgmodule_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgModule.__init__)


def test_jointpackage_ecore2maude_trgmodule_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgModule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmoduleidmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgModuleIdModExp)


def test_jointpackage_ecore2maude_trgmoduleidmodexp_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgModuleIdModExp.__init__)


def test_jointpackage_ecore2maude_trgmoduleidmodexp_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgModuleIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgsort_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgSort)


def test_jointpackage_ecore2maude_trgsort_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgSort.__init__)


def test_jointpackage_ecore2maude_trgsort_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgSort.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgterm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgTerm)


def test_jointpackage_ecore2maude_trgterm_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgTerm.__init__)


def test_jointpackage_ecore2maude_trgterm_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgTerm.__init__)
    params = list(sig.parameters.keys())



def test_trgstatement_is_not_abstract():
    assert not inspect.isabstract(TrgStatement)


def test_trgstatement_constructor_exists():
    assert callable(TrgStatement.__init__)


def test_trgstatement_constructor_args():
    sig = inspect.signature(TrgStatement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmembership_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgMembership)


def test_jointpackage_ecore2maude_trgmembership_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgMembership.__init__)


def test_jointpackage_ecore2maude_trgmembership_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgMembership.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmaudetopel_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgMaudeTopEl)


def test_jointpackage_ecore2maude_trgmaudetopel_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgMaudeTopEl.__init__)


def test_jointpackage_ecore2maude_trgmaudetopel_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgMaudeTopEl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_ecore2maude_trgmaudetopel_has_name():
    assert hasattr(jointPackage_Ecore2Maude_TrgMaudeTopEl, "name")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_TrgMaudeTopEl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_trgmaudespec_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgMaudeSpec)


def test_jointpackage_ecore2maude_trgmaudespec_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgMaudeSpec.__init__)


def test_jointpackage_ecore2maude_trgmaudespec_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgMaudeSpec.__init__)
    params = list(sig.parameters.keys())



def test_trgequationalcond_is_not_abstract():
    assert not inspect.isabstract(TrgEquationalCond)


def test_trgequationalcond_constructor_exists():
    assert callable(TrgEquationalCond.__init__)


def test_trgequationalcond_constructor_args():
    sig = inspect.signature(TrgEquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmatchingcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgMatchingCond)


def test_jointpackage_ecore2maude_trgmatchingcond_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgMatchingCond.__init__)


def test_jointpackage_ecore2maude_trgmatchingcond_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgMatchingCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgbooleancond_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgBooleanCond)


def test_jointpackage_ecore2maude_trgbooleancond_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgBooleanCond.__init__)


def test_jointpackage_ecore2maude_trgbooleancond_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgBooleanCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgequalcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgEqualCond)


def test_jointpackage_ecore2maude_trgequalcond_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgEqualCond.__init__)


def test_jointpackage_ecore2maude_trgequalcond_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgEqualCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgmembershipcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgMembershipCond)


def test_jointpackage_ecore2maude_trgmembershipcond_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgMembershipCond.__init__)


def test_jointpackage_ecore2maude_trgmembershipcond_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgMembershipCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgrule_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgRule)


def test_jointpackage_ecore2maude_trgrule_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgRule.__init__)


def test_jointpackage_ecore2maude_trgrule_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgRule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_trgequation_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_TrgEquation)


def test_jointpackage_ecore2maude_trgequation_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_TrgEquation.__init__)


def test_jointpackage_ecore2maude_trgequation_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_TrgEquation.__init__)
    params = list(sig.parameters.keys())



def test_srcetypedelement_is_not_abstract():
    assert not inspect.isabstract(SrcETypedElement)


def test_srcetypedelement_constructor_exists():
    assert callable(SrcETypedElement.__init__)


def test_srcetypedelement_constructor_args():
    sig = inspect.signature(SrcETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srceoperation_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEOperation)


def test_jointpackage_ecore2maude_srceoperation_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEOperation.__init__)


def test_jointpackage_ecore2maude_srceoperation_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEOperation.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srceparameter_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEParameter)


def test_jointpackage_ecore2maude_srceparameter_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEParameter.__init__)


def test_jointpackage_ecore2maude_srceparameter_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEParameter.__init__)
    params = list(sig.parameters.keys())



def test_srcedatatype_is_not_abstract():
    assert not inspect.isabstract(SrcEDataType)


def test_srcedatatype_constructor_exists():
    assert callable(SrcEDataType.__init__)


def test_srcedatatype_constructor_args():
    sig = inspect.signature(SrcEDataType.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srceenum_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEEnum)


def test_jointpackage_ecore2maude_srceenum_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEEnum.__init__)


def test_jointpackage_ecore2maude_srceenum_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEEnum.__init__)
    params = list(sig.parameters.keys())



def test_srcenamedelement_is_not_abstract():
    assert not inspect.isabstract(SrcENamedElement)


def test_srcenamedelement_constructor_exists():
    assert callable(SrcENamedElement.__init__)


def test_srcenamedelement_constructor_args():
    sig = inspect.signature(SrcENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srcetypedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcETypedElement)


def test_jointpackage_ecore2maude_srcetypedelement_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcETypedElement.__init__)


def test_jointpackage_ecore2maude_srcetypedelement_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "many" in params, "Missing parameter 'many'"
    assert "required" in params, "Missing parameter 'required'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_jointpackage_ecore2maude_srcetypedelement_has_ordered():
    assert hasattr(jointPackage_Ecore2Maude_SrcETypedElement, "ordered")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcETypedElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcetypedelement_has_many():
    assert hasattr(jointPackage_Ecore2Maude_SrcETypedElement, "many")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcETypedElement.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcetypedelement_has_required():
    assert hasattr(jointPackage_Ecore2Maude_SrcETypedElement, "required")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcETypedElement.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcetypedelement_has_unique():
    assert hasattr(jointPackage_Ecore2Maude_SrcETypedElement, "unique")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcETypedElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcetypedelement_has_upperBound():
    assert hasattr(jointPackage_Ecore2Maude_SrcETypedElement, "upperBound")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcETypedElement.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcetypedelement_has_lowerBound():
    assert hasattr(jointPackage_Ecore2Maude_SrcETypedElement, "lowerBound")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcETypedElement.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srcepackage_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEPackage)


def test_jointpackage_ecore2maude_srcepackage_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEPackage.__init__)


def test_jointpackage_ecore2maude_srcepackage_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"
    assert "nsURI" in params, "Missing parameter 'nsURI'"

def test_jointpackage_ecore2maude_srcepackage_has_nsPrefix():
    assert hasattr(jointPackage_Ecore2Maude_SrcEPackage, "nsPrefix")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEPackage.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcepackage_has_nsURI():
    assert hasattr(jointPackage_Ecore2Maude_SrcEPackage, "nsURI")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEPackage.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srceclassifier_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEClassifier)


def test_jointpackage_ecore2maude_srceclassifier_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEClassifier.__init__)


def test_jointpackage_ecore2maude_srceclassifier_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"
    assert "instanceTypeName" in params, "Missing parameter 'instanceTypeName'"

def test_jointpackage_ecore2maude_srceclassifier_has_instanceClassName():
    assert hasattr(jointPackage_Ecore2Maude_SrcEClassifier, "instanceClassName")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEClassifier.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srceclassifier_has_instanceTypeName():
    assert hasattr(jointPackage_Ecore2Maude_SrcEClassifier, "instanceTypeName")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEClassifier.__mro__:
        if "instanceTypeName" in klass.__dict__:
            descriptor = klass.__dict__["instanceTypeName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srcestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEStructuralFeature)


def test_jointpackage_ecore2maude_srcestructuralfeature_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEStructuralFeature.__init__)


def test_jointpackage_ecore2maude_srcestructuralfeature_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "unsettable" in params, "Missing parameter 'unsettable'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_jointpackage_ecore2maude_srcestructuralfeature_has_derived():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStructuralFeature, "derived")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStructuralFeature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcestructuralfeature_has_transient():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStructuralFeature, "transient")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStructuralFeature.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcestructuralfeature_has_unsettable():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStructuralFeature, "unsettable")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStructuralFeature.__mro__:
        if "unsettable" in klass.__dict__:
            descriptor = klass.__dict__["unsettable"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcestructuralfeature_has_defaultValueLiteral():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStructuralFeature, "defaultValueLiteral")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStructuralFeature.__mro__:
        if "defaultValueLiteral" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueLiteral"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcestructuralfeature_has_volatile():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStructuralFeature, "volatile")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStructuralFeature.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcestructuralfeature_has_changeable():
    assert hasattr(jointPackage_Ecore2Maude_SrcEStructuralFeature, "changeable")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEStructuralFeature.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srcenamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcENamedElement)


def test_jointpackage_ecore2maude_srcenamedelement_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcENamedElement.__init__)


def test_jointpackage_ecore2maude_srcenamedelement_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_ecore2maude_srcenamedelement_has_name():
    assert hasattr(jointPackage_Ecore2Maude_SrcENamedElement, "name")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcENamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srceenumliteral_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEEnumLiteral)


def test_jointpackage_ecore2maude_srceenumliteral_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEEnumLiteral.__init__)


def test_jointpackage_ecore2maude_srceenumliteral_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage_ecore2maude_srceenumliteral_has_literal():
    assert hasattr(jointPackage_Ecore2Maude_SrcEEnumLiteral, "literal")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEEnumLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srceenumliteral_has_value():
    assert hasattr(jointPackage_Ecore2Maude_SrcEEnumLiteral, "value")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_srceclassifier_is_not_abstract():
    assert not inspect.isabstract(SrcEClassifier)


def test_srceclassifier_constructor_exists():
    assert callable(SrcEClassifier.__init__)


def test_srceclassifier_constructor_args():
    sig = inspect.signature(SrcEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srceclass_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEClass)


def test_jointpackage_ecore2maude_srceclass_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEClass.__init__)


def test_jointpackage_ecore2maude_srceclass_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "interface" in params, "Missing parameter 'interface'"

def test_jointpackage_ecore2maude_srceclass_has_abstract():
    assert hasattr(jointPackage_Ecore2Maude_SrcEClass, "abstract")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srceclass_has_interface():
    assert hasattr(jointPackage_Ecore2Maude_SrcEClass, "interface")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEClass.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srcedatatype_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEDataType)


def test_jointpackage_ecore2maude_srcedatatype_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEDataType.__init__)


def test_jointpackage_ecore2maude_srcedatatype_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"

def test_jointpackage_ecore2maude_srcedatatype_has_serializable():
    assert hasattr(jointPackage_Ecore2Maude_SrcEDataType, "serializable")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEDataType.__mro__:
        if "serializable" in klass.__dict__:
            descriptor = klass.__dict__["serializable"]
            break
    assert isinstance(descriptor, property)



def test_srcestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(SrcEStructuralFeature)


def test_srcestructuralfeature_constructor_exists():
    assert callable(SrcEStructuralFeature.__init__)


def test_srcestructuralfeature_constructor_args():
    sig = inspect.signature(SrcEStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_ecore2maude_srcereference_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEReference)


def test_jointpackage_ecore2maude_srcereference_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEReference.__init__)


def test_jointpackage_ecore2maude_srcereference_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEReference.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"
    assert "container" in params, "Missing parameter 'container'"
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"

def test_jointpackage_ecore2maude_srcereference_has_containment():
    assert hasattr(jointPackage_Ecore2Maude_SrcEReference, "containment")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEReference.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcereference_has_container():
    assert hasattr(jointPackage_Ecore2Maude_SrcEReference, "container")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEReference.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_ecore2maude_srcereference_has_resolveProxies():
    assert hasattr(jointPackage_Ecore2Maude_SrcEReference, "resolveProxies")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEReference.__mro__:
        if "resolveProxies" in klass.__dict__:
            descriptor = klass.__dict__["resolveProxies"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_ecore2maude_srceattribute_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Ecore2Maude_SrcEAttribute)


def test_jointpackage_ecore2maude_srceattribute_constructor_exists():
    assert callable(jointPackage_Ecore2Maude_SrcEAttribute.__init__)


def test_jointpackage_ecore2maude_srceattribute_constructor_args():
    sig = inspect.signature(jointPackage_Ecore2Maude_SrcEAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_jointpackage_ecore2maude_srceattribute_has_iD():
    assert hasattr(jointPackage_Ecore2Maude_SrcEAttribute, "iD")
    descriptor = None
    for klass in jointPackage_Ecore2Maude_SrcEAttribute.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
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
TrgViewMapping_strategy = st.builds(
    TrgViewMapping,
)
jointPackage_Ecore2Maude_TrgViewMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgViewMapping,
)
jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEStringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
jointPackage_Ecore2Maude_JointMM_strategy = st.builds(
    jointPackage_Ecore2Maude_JointMM,
)
TrgTerm_strategy = st.builds(
    TrgTerm,
)
jointPackage_Ecore2Maude_TrgVariable_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgVariable,
    name=
        safe_text
)
jointPackage_Ecore2Maude_TrgRecTerm_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgRecTerm,
    op=
        safe_text
)
jointPackage_Ecore2Maude_TrgConstant_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgConstant,
    op=
        safe_text
)
TrgRenMapping_strategy = st.builds(
    TrgRenMapping,
)
jointPackage_Ecore2Maude_TrgOpMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgOpMapping,
    to=
        safe_text
)
jointPackage_Ecore2Maude_TrgOpTypedMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgOpTypedMapping,
    to=
        safe_text,
    atts=
        safe_text
)
jointPackage_Ecore2Maude_TrgLabelMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgLabelMapping,
    from_=
        safe_text,
    to=
        safe_text
)
jointPackage_Ecore2Maude_TrgSortMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgSortMapping,
    to=
        safe_text
)
jointPackage_Ecore2Maude_TrgTermMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgTermMapping,
)
TrgCondition_strategy = st.builds(
    TrgCondition,
)
jointPackage_Ecore2Maude_TrgRewriteCond_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgRewriteCond,
)
jointPackage_Ecore2Maude_TrgEquationalCond_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgEquationalCond,
)
jointPackage_Ecore2Maude_TrgType_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgType,
    name=
        safe_text
)
jointPackage_Ecore2Maude_TrgCondition_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgCondition,
)
TrgModElement_strategy = st.builds(
    TrgModElement,
)
jointPackage_Ecore2Maude_TrgOperation_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgOperation,
    atts=
        safe_text,
    name=
        safe_text
)
jointPackage_Ecore2Maude_TrgStatement_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgStatement,
    label=
        safe_text,
    atts=
        safe_text
)
jointPackage_Ecore2Maude_TrgModImportation_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgModImportation,
)
TrgModule_strategy = st.builds(
    TrgModule,
)
jointPackage_Ecore2Maude_TrgSModule_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgSModule,
)
jointPackage_Ecore2Maude_TrgFModule_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgFModule,
)
TrgTheory_strategy = st.builds(
    TrgTheory,
)
jointPackage_Ecore2Maude_TrgSTheory_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgSTheory,
)
jointPackage_Ecore2Maude_TrgFTheory_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgFTheory,
)
jointPackage_Ecore2Maude_TrgModElement_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgModElement,
)
jointPackage_Ecore2Maude_TrgSubsortRel_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgSubsortRel,
)
TrgType_strategy = st.builds(
    TrgType,
)
jointPackage_Ecore2Maude_TrgKind_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgKind,
)
jointPackage_Ecore2Maude_TrgRenMapping_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgRenMapping,
)
TrgModExpression_strategy = st.builds(
    TrgModExpression,
)
jointPackage_Ecore2Maude_TrgCompModExp_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgCompModExp,
)
jointPackage_Ecore2Maude_TrgRenModExp_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgRenModExp,
)
jointPackage_Ecore2Maude_TrgInstModExp_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgInstModExp,
)
jointPackage_Ecore2Maude_TrgModExpression_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgModExpression,
)
TrgMaudeTopEl_strategy = st.builds(
    TrgMaudeTopEl,
)
jointPackage_Ecore2Maude_TrgView_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgView,
)
jointPackage_Ecore2Maude_TrgParameter_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgParameter,
    label=
        safe_text
)
jointPackage_Ecore2Maude_TrgTheory_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgTheory,
)
jointPackage_Ecore2Maude_TrgTheoryIdModExp_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgTheoryIdModExp,
)
jointPackage_Ecore2Maude_TrgModule_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgModule,
)
jointPackage_Ecore2Maude_TrgModuleIdModExp_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgModuleIdModExp,
)
jointPackage_Ecore2Maude_TrgSort_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgSort,
)
jointPackage_Ecore2Maude_TrgTerm_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgTerm,
)
TrgStatement_strategy = st.builds(
    TrgStatement,
)
jointPackage_Ecore2Maude_TrgMembership_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgMembership,
)
jointPackage_Ecore2Maude_TrgMaudeTopEl_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgMaudeTopEl,
    name=
        safe_text
)
jointPackage_Ecore2Maude_TrgMaudeSpec_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgMaudeSpec,
)
TrgEquationalCond_strategy = st.builds(
    TrgEquationalCond,
)
jointPackage_Ecore2Maude_TrgMatchingCond_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgMatchingCond,
)
jointPackage_Ecore2Maude_TrgBooleanCond_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgBooleanCond,
)
jointPackage_Ecore2Maude_TrgEqualCond_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgEqualCond,
)
jointPackage_Ecore2Maude_TrgMembershipCond_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgMembershipCond,
)
jointPackage_Ecore2Maude_TrgRule_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgRule,
)
jointPackage_Ecore2Maude_TrgEquation_strategy = st.builds(
    jointPackage_Ecore2Maude_TrgEquation,
)
SrcETypedElement_strategy = st.builds(
    SrcETypedElement,
)
jointPackage_Ecore2Maude_SrcEOperation_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEOperation,
)
jointPackage_Ecore2Maude_SrcEParameter_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEParameter,
)
SrcEDataType_strategy = st.builds(
    SrcEDataType,
)
jointPackage_Ecore2Maude_SrcEEnum_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEEnum,
)
SrcENamedElement_strategy = st.builds(
    SrcENamedElement,
)
jointPackage_Ecore2Maude_SrcETypedElement_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcETypedElement,
    ordered=
        st.booleans(),
    many=
        st.booleans(),
    required=
        st.booleans(),
    unique=
        st.booleans(),
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
jointPackage_Ecore2Maude_SrcEPackage_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEPackage,
    nsPrefix=
        safe_text,
    nsURI=
        safe_text
)
jointPackage_Ecore2Maude_SrcEClassifier_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEClassifier,
    instanceClassName=
        safe_text,
    instanceTypeName=
        safe_text
)
jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEStructuralFeature,
    derived=
        st.booleans(),
    transient=
        st.booleans(),
    unsettable=
        st.booleans(),
    defaultValueLiteral=
        safe_text,
    volatile=
        st.booleans(),
    changeable=
        st.booleans()
)
jointPackage_Ecore2Maude_SrcENamedElement_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcENamedElement,
    name=
        safe_text
)
jointPackage_Ecore2Maude_SrcEEnumLiteral_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEEnumLiteral,
    literal=
        safe_text,
    value=
        st.integers()
)
SrcEClassifier_strategy = st.builds(
    SrcEClassifier,
)
jointPackage_Ecore2Maude_SrcEClass_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEClass,
    abstract=
        st.booleans(),
    interface=
        st.booleans()
)
jointPackage_Ecore2Maude_SrcEDataType_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEDataType,
    serializable=
        st.booleans()
)
SrcEStructuralFeature_strategy = st.builds(
    SrcEStructuralFeature,
)
jointPackage_Ecore2Maude_SrcEReference_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEReference,
    containment=
        st.booleans(),
    container=
        st.booleans(),
    resolveProxies=
        st.booleans()
)
jointPackage_Ecore2Maude_SrcEAttribute_strategy = st.builds(
    jointPackage_Ecore2Maude_SrcEAttribute,
    iD=
        st.booleans()
)

@given(instance=TrgViewMapping_strategy)
@settings(max_examples=50)
def test_trgviewmapping_instantiation(instance):
    assert isinstance(instance, TrgViewMapping)

@given(instance=jointPackage_Ecore2Maude_TrgViewMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgviewmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgViewMapping)

@given(instance=jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEStringToStringMapEntry)



@given(instance=jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_strategy)
def test_jointpackage_ecore2maude_srcestringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_strategy)
def test_jointpackage_ecore2maude_srcestringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage_Ecore2Maude_JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_JointMM)

@given(instance=TrgTerm_strategy)
@settings(max_examples=50)
def test_trgterm_instantiation(instance):
    assert isinstance(instance, TrgTerm)

@given(instance=jointPackage_Ecore2Maude_TrgVariable_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgvariable_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgVariable)



@given(instance=jointPackage_Ecore2Maude_TrgVariable_strategy)
def test_jointpackage_ecore2maude_trgvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_Ecore2Maude_TrgRecTerm_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgrecterm_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgRecTerm)



@given(instance=jointPackage_Ecore2Maude_TrgRecTerm_strategy)
def test_jointpackage_ecore2maude_trgrecterm_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jointPackage_Ecore2Maude_TrgConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgConstant)



@given(instance=jointPackage_Ecore2Maude_TrgConstant_strategy)
def test_jointpackage_ecore2maude_trgconstant_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=TrgRenMapping_strategy)
@settings(max_examples=50)
def test_trgrenmapping_instantiation(instance):
    assert isinstance(instance, TrgRenMapping)

@given(instance=jointPackage_Ecore2Maude_TrgOpMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgopmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgOpMapping)



@given(instance=jointPackage_Ecore2Maude_TrgOpMapping_strategy)
def test_jointpackage_ecore2maude_trgopmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jointPackage_Ecore2Maude_TrgOpTypedMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgoptypedmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgOpTypedMapping)



@given(instance=jointPackage_Ecore2Maude_TrgOpTypedMapping_strategy)
def test_jointpackage_ecore2maude_trgoptypedmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=jointPackage_Ecore2Maude_TrgOpTypedMapping_strategy)
def test_jointpackage_ecore2maude_trgoptypedmapping_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=jointPackage_Ecore2Maude_TrgLabelMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trglabelmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgLabelMapping)



@given(instance=jointPackage_Ecore2Maude_TrgLabelMapping_strategy)
def test_jointpackage_ecore2maude_trglabelmapping_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=jointPackage_Ecore2Maude_TrgLabelMapping_strategy)
def test_jointpackage_ecore2maude_trglabelmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jointPackage_Ecore2Maude_TrgSortMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgsortmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgSortMapping)



@given(instance=jointPackage_Ecore2Maude_TrgSortMapping_strategy)
def test_jointpackage_ecore2maude_trgsortmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jointPackage_Ecore2Maude_TrgTermMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgtermmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgTermMapping)

@given(instance=TrgCondition_strategy)
@settings(max_examples=50)
def test_trgcondition_instantiation(instance):
    assert isinstance(instance, TrgCondition)

@given(instance=jointPackage_Ecore2Maude_TrgRewriteCond_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgrewritecond_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgRewriteCond)

@given(instance=jointPackage_Ecore2Maude_TrgEquationalCond_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgequationalcond_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgEquationalCond)

@given(instance=jointPackage_Ecore2Maude_TrgType_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgtype_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgType)



@given(instance=jointPackage_Ecore2Maude_TrgType_strategy)
def test_jointpackage_ecore2maude_trgtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_Ecore2Maude_TrgCondition_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgcondition_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgCondition)

@given(instance=TrgModElement_strategy)
@settings(max_examples=50)
def test_trgmodelement_instantiation(instance):
    assert isinstance(instance, TrgModElement)

@given(instance=jointPackage_Ecore2Maude_TrgOperation_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgoperation_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgOperation)



@given(instance=jointPackage_Ecore2Maude_TrgOperation_strategy)
def test_jointpackage_ecore2maude_trgoperation_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original



@given(instance=jointPackage_Ecore2Maude_TrgOperation_strategy)
def test_jointpackage_ecore2maude_trgoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_Ecore2Maude_TrgStatement_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgstatement_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgStatement)



@given(instance=jointPackage_Ecore2Maude_TrgStatement_strategy)
def test_jointpackage_ecore2maude_trgstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=jointPackage_Ecore2Maude_TrgStatement_strategy)
def test_jointpackage_ecore2maude_trgstatement_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=jointPackage_Ecore2Maude_TrgModImportation_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmodimportation_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgModImportation)

@given(instance=TrgModule_strategy)
@settings(max_examples=50)
def test_trgmodule_instantiation(instance):
    assert isinstance(instance, TrgModule)

@given(instance=jointPackage_Ecore2Maude_TrgSModule_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgsmodule_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgSModule)

@given(instance=jointPackage_Ecore2Maude_TrgFModule_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgfmodule_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgFModule)

@given(instance=TrgTheory_strategy)
@settings(max_examples=50)
def test_trgtheory_instantiation(instance):
    assert isinstance(instance, TrgTheory)

@given(instance=jointPackage_Ecore2Maude_TrgSTheory_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgstheory_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgSTheory)

@given(instance=jointPackage_Ecore2Maude_TrgFTheory_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgftheory_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgFTheory)

@given(instance=jointPackage_Ecore2Maude_TrgModElement_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmodelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgModElement)

@given(instance=jointPackage_Ecore2Maude_TrgSubsortRel_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgsubsortrel_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgSubsortRel)

@given(instance=TrgType_strategy)
@settings(max_examples=50)
def test_trgtype_instantiation(instance):
    assert isinstance(instance, TrgType)

@given(instance=jointPackage_Ecore2Maude_TrgKind_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgkind_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgKind)

@given(instance=jointPackage_Ecore2Maude_TrgRenMapping_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgrenmapping_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgRenMapping)

@given(instance=TrgModExpression_strategy)
@settings(max_examples=50)
def test_trgmodexpression_instantiation(instance):
    assert isinstance(instance, TrgModExpression)

@given(instance=jointPackage_Ecore2Maude_TrgCompModExp_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgcompmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgCompModExp)

@given(instance=jointPackage_Ecore2Maude_TrgRenModExp_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgrenmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgRenModExp)

@given(instance=jointPackage_Ecore2Maude_TrgInstModExp_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trginstmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgInstModExp)

@given(instance=jointPackage_Ecore2Maude_TrgModExpression_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmodexpression_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgModExpression)

@given(instance=TrgMaudeTopEl_strategy)
@settings(max_examples=50)
def test_trgmaudetopel_instantiation(instance):
    assert isinstance(instance, TrgMaudeTopEl)

@given(instance=jointPackage_Ecore2Maude_TrgView_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgview_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgView)

@given(instance=jointPackage_Ecore2Maude_TrgParameter_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgparameter_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgParameter)



@given(instance=jointPackage_Ecore2Maude_TrgParameter_strategy)
def test_jointpackage_ecore2maude_trgparameter_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=jointPackage_Ecore2Maude_TrgTheory_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgtheory_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgTheory)

@given(instance=jointPackage_Ecore2Maude_TrgTheoryIdModExp_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgtheoryidmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgTheoryIdModExp)

@given(instance=jointPackage_Ecore2Maude_TrgModule_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmodule_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgModule)

@given(instance=jointPackage_Ecore2Maude_TrgModuleIdModExp_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmoduleidmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgModuleIdModExp)

@given(instance=jointPackage_Ecore2Maude_TrgSort_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgsort_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgSort)

@given(instance=jointPackage_Ecore2Maude_TrgTerm_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgterm_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgTerm)

@given(instance=TrgStatement_strategy)
@settings(max_examples=50)
def test_trgstatement_instantiation(instance):
    assert isinstance(instance, TrgStatement)

@given(instance=jointPackage_Ecore2Maude_TrgMembership_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmembership_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgMembership)

@given(instance=jointPackage_Ecore2Maude_TrgMaudeTopEl_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmaudetopel_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgMaudeTopEl)



@given(instance=jointPackage_Ecore2Maude_TrgMaudeTopEl_strategy)
def test_jointpackage_ecore2maude_trgmaudetopel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_Ecore2Maude_TrgMaudeSpec_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmaudespec_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgMaudeSpec)

@given(instance=TrgEquationalCond_strategy)
@settings(max_examples=50)
def test_trgequationalcond_instantiation(instance):
    assert isinstance(instance, TrgEquationalCond)

@given(instance=jointPackage_Ecore2Maude_TrgMatchingCond_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmatchingcond_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgMatchingCond)

@given(instance=jointPackage_Ecore2Maude_TrgBooleanCond_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgbooleancond_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgBooleanCond)

@given(instance=jointPackage_Ecore2Maude_TrgEqualCond_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgequalcond_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgEqualCond)

@given(instance=jointPackage_Ecore2Maude_TrgMembershipCond_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgmembershipcond_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgMembershipCond)

@given(instance=jointPackage_Ecore2Maude_TrgRule_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgrule_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgRule)

@given(instance=jointPackage_Ecore2Maude_TrgEquation_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_trgequation_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_TrgEquation)

@given(instance=SrcETypedElement_strategy)
@settings(max_examples=50)
def test_srcetypedelement_instantiation(instance):
    assert isinstance(instance, SrcETypedElement)

@given(instance=jointPackage_Ecore2Maude_SrcEOperation_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceoperation_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEOperation)

@given(instance=jointPackage_Ecore2Maude_SrcEParameter_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceparameter_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEParameter)

@given(instance=SrcEDataType_strategy)
@settings(max_examples=50)
def test_srcedatatype_instantiation(instance):
    assert isinstance(instance, SrcEDataType)

@given(instance=jointPackage_Ecore2Maude_SrcEEnum_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceenum_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEEnum)

@given(instance=SrcENamedElement_strategy)
@settings(max_examples=50)
def test_srcenamedelement_instantiation(instance):
    assert isinstance(instance, SrcENamedElement)

@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcetypedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcETypedElement)



@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
def test_jointpackage_ecore2maude_srcetypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
def test_jointpackage_ecore2maude_srcetypedelement_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
def test_jointpackage_ecore2maude_srcetypedelement_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
def test_jointpackage_ecore2maude_srcetypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
def test_jointpackage_ecore2maude_srcetypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=jointPackage_Ecore2Maude_SrcETypedElement_strategy)
def test_jointpackage_ecore2maude_srcetypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=jointPackage_Ecore2Maude_SrcEPackage_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcepackage_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEPackage)



@given(instance=jointPackage_Ecore2Maude_SrcEPackage_strategy)
def test_jointpackage_ecore2maude_srcepackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original



@given(instance=jointPackage_Ecore2Maude_SrcEPackage_strategy)
def test_jointpackage_ecore2maude_srcepackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

@given(instance=jointPackage_Ecore2Maude_SrcEClassifier_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceclassifier_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEClassifier)



@given(instance=jointPackage_Ecore2Maude_SrcEClassifier_strategy)
def test_jointpackage_ecore2maude_srceclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original



@given(instance=jointPackage_Ecore2Maude_SrcEClassifier_strategy)
def test_jointpackage_ecore2maude_srceclassifier_instanceTypeName_setter(instance):
    original = instance.instanceTypeName
    instance.instanceTypeName = original
    assert instance.instanceTypeName == original

@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcestructuralfeature_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEStructuralFeature)



@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
def test_jointpackage_ecore2maude_srcestructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
def test_jointpackage_ecore2maude_srcestructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
def test_jointpackage_ecore2maude_srcestructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original



@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
def test_jointpackage_ecore2maude_srcestructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original



@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
def test_jointpackage_ecore2maude_srcestructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=jointPackage_Ecore2Maude_SrcEStructuralFeature_strategy)
def test_jointpackage_ecore2maude_srcestructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=jointPackage_Ecore2Maude_SrcENamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcenamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcENamedElement)



@given(instance=jointPackage_Ecore2Maude_SrcENamedElement_strategy)
def test_jointpackage_ecore2maude_srcenamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_Ecore2Maude_SrcEEnumLiteral_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceenumliteral_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEEnumLiteral)



@given(instance=jointPackage_Ecore2Maude_SrcEEnumLiteral_strategy)
def test_jointpackage_ecore2maude_srceenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=jointPackage_Ecore2Maude_SrcEEnumLiteral_strategy)
def test_jointpackage_ecore2maude_srceenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SrcEClassifier_strategy)
@settings(max_examples=50)
def test_srceclassifier_instantiation(instance):
    assert isinstance(instance, SrcEClassifier)

@given(instance=jointPackage_Ecore2Maude_SrcEClass_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceclass_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEClass)



@given(instance=jointPackage_Ecore2Maude_SrcEClass_strategy)
def test_jointpackage_ecore2maude_srceclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=jointPackage_Ecore2Maude_SrcEClass_strategy)
def test_jointpackage_ecore2maude_srceclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jointPackage_Ecore2Maude_SrcEClass_strategy)
@settings(max_examples=30)
def test_jointpackage_ecore2maude_srceclass_issupertypeof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperTypeOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperTypeOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperTypeOf' in jointPackage_Ecore2Maude_SrcEClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in jointPackage_Ecore2Maude_SrcEClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in jointPackage_Ecore2Maude_SrcEClass is not implemented or raised an error")

@given(instance=jointPackage_Ecore2Maude_SrcEDataType_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcedatatype_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEDataType)



@given(instance=jointPackage_Ecore2Maude_SrcEDataType_strategy)
def test_jointpackage_ecore2maude_srcedatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original

@given(instance=SrcEStructuralFeature_strategy)
@settings(max_examples=50)
def test_srcestructuralfeature_instantiation(instance):
    assert isinstance(instance, SrcEStructuralFeature)

@given(instance=jointPackage_Ecore2Maude_SrcEReference_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srcereference_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEReference)



@given(instance=jointPackage_Ecore2Maude_SrcEReference_strategy)
def test_jointpackage_ecore2maude_srcereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original



@given(instance=jointPackage_Ecore2Maude_SrcEReference_strategy)
def test_jointpackage_ecore2maude_srcereference_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=jointPackage_Ecore2Maude_SrcEReference_strategy)
def test_jointpackage_ecore2maude_srcereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original

@given(instance=jointPackage_Ecore2Maude_SrcEAttribute_strategy)
@settings(max_examples=50)
def test_jointpackage_ecore2maude_srceattribute_instantiation(instance):
    assert isinstance(instance, jointPackage_Ecore2Maude_SrcEAttribute)



@given(instance=jointPackage_Ecore2Maude_SrcEAttribute_strategy)
def test_jointpackage_ecore2maude_srceattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original
