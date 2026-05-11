import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TrgCondition,
    jointPackage::Ecore2Maude::TrgRewriteCond,
    jointPackage::Ecore2Maude::TrgEquationalCond,
    jointPackage::Ecore2Maude::TrgCondition,
    TrgRenMapping,
    jointPackage::Ecore2Maude::TrgOpTypedMapping,
    jointPackage::Ecore2Maude::TrgOpMapping,
    jointPackage::Ecore2Maude::TrgLabelMapping,
    jointPackage::Ecore2Maude::TrgSortMapping,
    TrgViewMapping,
    jointPackage::Ecore2Maude::TrgTermMapping,
    jointPackage::Ecore2Maude::TrgViewMapping,
    TrgTerm,
    jointPackage::Ecore2Maude::TrgVariable,
    jointPackage::Ecore2Maude::TrgRecTerm,
    jointPackage::Ecore2Maude::TrgConstant,
    TrgModule,
    jointPackage::Ecore2Maude::TrgSModule,
    jointPackage::Ecore2Maude::TrgFModule,
    TrgTheory,
    jointPackage::Ecore2Maude::TrgSTheory,
    jointPackage::Ecore2Maude::TrgFTheory,
    jointPackage::Ecore2Maude::TrgModElement,
    TrgMaudeTopEl,
    jointPackage::Ecore2Maude::TrgTheory,
    TrgType,
    jointPackage::Ecore2Maude::TrgKind,
    jointPackage::Ecore2Maude::TrgType,
    TrgModElement,
    jointPackage::Ecore2Maude::TrgStatement,
    jointPackage::Ecore2Maude::TrgOperation,
    jointPackage::Ecore2Maude::TrgSubsortRel,
    jointPackage::Ecore2Maude::TrgModImportation,
    TrgEquationalCond,
    jointPackage::Ecore2Maude::TrgBooleanCond,
    jointPackage::Ecore2Maude::TrgMembershipCond,
    jointPackage::Ecore2Maude::TrgSort,
    jointPackage::Ecore2Maude::TrgTerm,
    TrgStatement,
    jointPackage::Ecore2Maude::TrgEquation,
    jointPackage::Ecore2Maude::TrgRule,
    jointPackage::Ecore2Maude::TrgMembership,
    jointPackage::Ecore2Maude::TrgMaudeTopEl,
    jointPackage::Ecore2Maude::TrgMaudeSpec,
    jointPackage::Ecore2Maude::TrgModule,
    jointPackage::Ecore2Maude::TrgRenMapping,
    jointPackage::Ecore2Maude::TrgView,
    TrgModExpression,
    jointPackage::Ecore2Maude::TrgRenModExp,
    jointPackage::Ecore2Maude::TrgTheoryIdModExp,
    jointPackage::Ecore2Maude::TrgModuleIdModExp,
    jointPackage::Ecore2Maude::TrgParameter,
    jointPackage::Ecore2Maude::TrgCompModExp,
    jointPackage::Ecore2Maude::TrgInstModExp,
    jointPackage::Ecore2Maude::TrgModExpression,
    jointPackage::Ecore2Maude::TrgMatchingCond,
    SrcEDataType,
    jointPackage::Ecore2Maude::SrcEEnum,
    SrcENamedElement,
    jointPackage::Ecore2Maude::SrcEPackage,
    jointPackage::Ecore2Maude::SrcETypedElement,
    jointPackage::Ecore2Maude::SrcEClassifier,
    SrcETypedElement,
    jointPackage::Ecore2Maude::SrcEStructuralFeature,
    jointPackage::Ecore2Maude::SrcEParameter,
    jointPackage::Ecore2Maude::SrcENamedElement,
    jointPackage::Ecore2Maude::SrcEEnumLiteral,
    SrcEClassifier,
    jointPackage::Ecore2Maude::SrcEClass,
    jointPackage::Ecore2Maude::SrcEDataType,
    SrcEStructuralFeature,
    jointPackage::Ecore2Maude::SrcEAttribute,
    jointPackage::Ecore2Maude::TrgEqualCond,
    jointPackage::Ecore2Maude::SrcEStringToStringMapEntry,
    jointPackage::Ecore2Maude::JointMM,
    jointPackage::Ecore2Maude::SrcEReference,
    jointPackage::Ecore2Maude::SrcEOperation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trgcondition_is_not_abstract():
    assert not inspect.isabstract(TrgCondition)


def test_trgcondition_constructor_exists():
    assert callable(TrgCondition.__init__)


def test_trgcondition_constructor_args():
    sig = inspect.signature(TrgCondition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgrewritecond_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgRewriteCond)


def test_jointpackage::ecore2maude::trgrewritecond_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgRewriteCond.__init__)


def test_jointpackage::ecore2maude::trgrewritecond_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgRewriteCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgequationalcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgEquationalCond)


def test_jointpackage::ecore2maude::trgequationalcond_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgEquationalCond.__init__)


def test_jointpackage::ecore2maude::trgequationalcond_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgEquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgcondition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgCondition)


def test_jointpackage::ecore2maude::trgcondition_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgCondition.__init__)


def test_jointpackage::ecore2maude::trgcondition_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgCondition.__init__)
    params = list(sig.parameters.keys())



def test_trgrenmapping_is_not_abstract():
    assert not inspect.isabstract(TrgRenMapping)


def test_trgrenmapping_constructor_exists():
    assert callable(TrgRenMapping.__init__)


def test_trgrenmapping_constructor_args():
    sig = inspect.signature(TrgRenMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgoptypedmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgOpTypedMapping)


def test_jointpackage::ecore2maude::trgoptypedmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgOpTypedMapping.__init__)


def test_jointpackage::ecore2maude::trgoptypedmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgOpTypedMapping.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage::ecore2maude::trgoptypedmapping_has_atts():
    assert hasattr(jointPackage::Ecore2Maude::TrgOpTypedMapping, "atts")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgOpTypedMapping.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::trgoptypedmapping_has_to():
    assert hasattr(jointPackage::Ecore2Maude::TrgOpTypedMapping, "to")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgOpTypedMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgopmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgOpMapping)


def test_jointpackage::ecore2maude::trgopmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgOpMapping.__init__)


def test_jointpackage::ecore2maude::trgopmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgOpMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage::ecore2maude::trgopmapping_has_to():
    assert hasattr(jointPackage::Ecore2Maude::TrgOpMapping, "to")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgOpMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trglabelmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgLabelMapping)


def test_jointpackage::ecore2maude::trglabelmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgLabelMapping.__init__)


def test_jointpackage::ecore2maude::trglabelmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgLabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage::ecore2maude::trglabelmapping_has_from_():
    assert hasattr(jointPackage::Ecore2Maude::TrgLabelMapping, "from_")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgLabelMapping.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::trglabelmapping_has_to():
    assert hasattr(jointPackage::Ecore2Maude::TrgLabelMapping, "to")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgLabelMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgsortmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgSortMapping)


def test_jointpackage::ecore2maude::trgsortmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgSortMapping.__init__)


def test_jointpackage::ecore2maude::trgsortmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgSortMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_jointpackage::ecore2maude::trgsortmapping_has_to():
    assert hasattr(jointPackage::Ecore2Maude::TrgSortMapping, "to")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgSortMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_trgviewmapping_is_not_abstract():
    assert not inspect.isabstract(TrgViewMapping)


def test_trgviewmapping_constructor_exists():
    assert callable(TrgViewMapping.__init__)


def test_trgviewmapping_constructor_args():
    sig = inspect.signature(TrgViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgtermmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgTermMapping)


def test_jointpackage::ecore2maude::trgtermmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgTermMapping.__init__)


def test_jointpackage::ecore2maude::trgtermmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgTermMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgviewmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgViewMapping)


def test_jointpackage::ecore2maude::trgviewmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgViewMapping.__init__)


def test_jointpackage::ecore2maude::trgviewmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_trgterm_is_not_abstract():
    assert not inspect.isabstract(TrgTerm)


def test_trgterm_constructor_exists():
    assert callable(TrgTerm.__init__)


def test_trgterm_constructor_args():
    sig = inspect.signature(TrgTerm.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgvariable_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgVariable)


def test_jointpackage::ecore2maude::trgvariable_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgVariable.__init__)


def test_jointpackage::ecore2maude::trgvariable_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::ecore2maude::trgvariable_has_name():
    assert hasattr(jointPackage::Ecore2Maude::TrgVariable, "name")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgrecterm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgRecTerm)


def test_jointpackage::ecore2maude::trgrecterm_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgRecTerm.__init__)


def test_jointpackage::ecore2maude::trgrecterm_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgRecTerm.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jointpackage::ecore2maude::trgrecterm_has_op():
    assert hasattr(jointPackage::Ecore2Maude::TrgRecTerm, "op")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgRecTerm.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgConstant)


def test_jointpackage::ecore2maude::trgconstant_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgConstant.__init__)


def test_jointpackage::ecore2maude::trgconstant_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgConstant.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jointpackage::ecore2maude::trgconstant_has_op():
    assert hasattr(jointPackage::Ecore2Maude::TrgConstant, "op")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgConstant.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_trgmodule_is_not_abstract():
    assert not inspect.isabstract(TrgModule)


def test_trgmodule_constructor_exists():
    assert callable(TrgModule.__init__)


def test_trgmodule_constructor_args():
    sig = inspect.signature(TrgModule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgsmodule_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgSModule)


def test_jointpackage::ecore2maude::trgsmodule_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgSModule.__init__)


def test_jointpackage::ecore2maude::trgsmodule_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgSModule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgfmodule_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgFModule)


def test_jointpackage::ecore2maude::trgfmodule_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgFModule.__init__)


def test_jointpackage::ecore2maude::trgfmodule_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgFModule.__init__)
    params = list(sig.parameters.keys())



def test_trgtheory_is_not_abstract():
    assert not inspect.isabstract(TrgTheory)


def test_trgtheory_constructor_exists():
    assert callable(TrgTheory.__init__)


def test_trgtheory_constructor_args():
    sig = inspect.signature(TrgTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgstheory_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgSTheory)


def test_jointpackage::ecore2maude::trgstheory_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgSTheory.__init__)


def test_jointpackage::ecore2maude::trgstheory_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgSTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgftheory_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgFTheory)


def test_jointpackage::ecore2maude::trgftheory_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgFTheory.__init__)


def test_jointpackage::ecore2maude::trgftheory_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgFTheory.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmodelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgModElement)


def test_jointpackage::ecore2maude::trgmodelement_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgModElement.__init__)


def test_jointpackage::ecore2maude::trgmodelement_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgModElement.__init__)
    params = list(sig.parameters.keys())



def test_trgmaudetopel_is_not_abstract():
    assert not inspect.isabstract(TrgMaudeTopEl)


def test_trgmaudetopel_constructor_exists():
    assert callable(TrgMaudeTopEl.__init__)


def test_trgmaudetopel_constructor_args():
    sig = inspect.signature(TrgMaudeTopEl.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgtheory_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgTheory)


def test_jointpackage::ecore2maude::trgtheory_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgTheory.__init__)


def test_jointpackage::ecore2maude::trgtheory_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgTheory.__init__)
    params = list(sig.parameters.keys())



def test_trgtype_is_not_abstract():
    assert not inspect.isabstract(TrgType)


def test_trgtype_constructor_exists():
    assert callable(TrgType.__init__)


def test_trgtype_constructor_args():
    sig = inspect.signature(TrgType.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgkind_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgKind)


def test_jointpackage::ecore2maude::trgkind_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgKind.__init__)


def test_jointpackage::ecore2maude::trgkind_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgKind.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgtype_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgType)


def test_jointpackage::ecore2maude::trgtype_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgType.__init__)


def test_jointpackage::ecore2maude::trgtype_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::ecore2maude::trgtype_has_name():
    assert hasattr(jointPackage::Ecore2Maude::TrgType, "name")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trgmodelement_is_not_abstract():
    assert not inspect.isabstract(TrgModElement)


def test_trgmodelement_constructor_exists():
    assert callable(TrgModElement.__init__)


def test_trgmodelement_constructor_args():
    sig = inspect.signature(TrgModElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgstatement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgStatement)


def test_jointpackage::ecore2maude::trgstatement_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgStatement.__init__)


def test_jointpackage::ecore2maude::trgstatement_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgStatement.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage::ecore2maude::trgstatement_has_atts():
    assert hasattr(jointPackage::Ecore2Maude::TrgStatement, "atts")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgStatement.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::trgstatement_has_label():
    assert hasattr(jointPackage::Ecore2Maude::TrgStatement, "label")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgoperation_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgOperation)


def test_jointpackage::ecore2maude::trgoperation_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgOperation.__init__)


def test_jointpackage::ecore2maude::trgoperation_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "atts" in params, "Missing parameter 'atts'"

def test_jointpackage::ecore2maude::trgoperation_has_name():
    assert hasattr(jointPackage::Ecore2Maude::TrgOperation, "name")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::trgoperation_has_atts():
    assert hasattr(jointPackage::Ecore2Maude::TrgOperation, "atts")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgOperation.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgsubsortrel_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgSubsortRel)


def test_jointpackage::ecore2maude::trgsubsortrel_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgSubsortRel.__init__)


def test_jointpackage::ecore2maude::trgsubsortrel_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgSubsortRel.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmodimportation_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgModImportation)


def test_jointpackage::ecore2maude::trgmodimportation_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgModImportation.__init__)


def test_jointpackage::ecore2maude::trgmodimportation_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgModImportation.__init__)
    params = list(sig.parameters.keys())



def test_trgequationalcond_is_not_abstract():
    assert not inspect.isabstract(TrgEquationalCond)


def test_trgequationalcond_constructor_exists():
    assert callable(TrgEquationalCond.__init__)


def test_trgequationalcond_constructor_args():
    sig = inspect.signature(TrgEquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgbooleancond_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgBooleanCond)


def test_jointpackage::ecore2maude::trgbooleancond_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgBooleanCond.__init__)


def test_jointpackage::ecore2maude::trgbooleancond_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgBooleanCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmembershipcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgMembershipCond)


def test_jointpackage::ecore2maude::trgmembershipcond_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgMembershipCond.__init__)


def test_jointpackage::ecore2maude::trgmembershipcond_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgMembershipCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgsort_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgSort)


def test_jointpackage::ecore2maude::trgsort_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgSort.__init__)


def test_jointpackage::ecore2maude::trgsort_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgSort.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgterm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgTerm)


def test_jointpackage::ecore2maude::trgterm_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgTerm.__init__)


def test_jointpackage::ecore2maude::trgterm_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgTerm.__init__)
    params = list(sig.parameters.keys())



def test_trgstatement_is_not_abstract():
    assert not inspect.isabstract(TrgStatement)


def test_trgstatement_constructor_exists():
    assert callable(TrgStatement.__init__)


def test_trgstatement_constructor_args():
    sig = inspect.signature(TrgStatement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgequation_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgEquation)


def test_jointpackage::ecore2maude::trgequation_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgEquation.__init__)


def test_jointpackage::ecore2maude::trgequation_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgEquation.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgrule_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgRule)


def test_jointpackage::ecore2maude::trgrule_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgRule.__init__)


def test_jointpackage::ecore2maude::trgrule_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgRule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmembership_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgMembership)


def test_jointpackage::ecore2maude::trgmembership_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgMembership.__init__)


def test_jointpackage::ecore2maude::trgmembership_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgMembership.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmaudetopel_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgMaudeTopEl)


def test_jointpackage::ecore2maude::trgmaudetopel_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgMaudeTopEl.__init__)


def test_jointpackage::ecore2maude::trgmaudetopel_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgMaudeTopEl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::ecore2maude::trgmaudetopel_has_name():
    assert hasattr(jointPackage::Ecore2Maude::TrgMaudeTopEl, "name")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgMaudeTopEl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgmaudespec_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgMaudeSpec)


def test_jointpackage::ecore2maude::trgmaudespec_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgMaudeSpec.__init__)


def test_jointpackage::ecore2maude::trgmaudespec_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgMaudeSpec.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmodule_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgModule)


def test_jointpackage::ecore2maude::trgmodule_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgModule.__init__)


def test_jointpackage::ecore2maude::trgmodule_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgModule.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgrenmapping_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgRenMapping)


def test_jointpackage::ecore2maude::trgrenmapping_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgRenMapping.__init__)


def test_jointpackage::ecore2maude::trgrenmapping_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgRenMapping.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgview_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgView)


def test_jointpackage::ecore2maude::trgview_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgView.__init__)


def test_jointpackage::ecore2maude::trgview_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgView.__init__)
    params = list(sig.parameters.keys())



def test_trgmodexpression_is_not_abstract():
    assert not inspect.isabstract(TrgModExpression)


def test_trgmodexpression_constructor_exists():
    assert callable(TrgModExpression.__init__)


def test_trgmodexpression_constructor_args():
    sig = inspect.signature(TrgModExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgrenmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgRenModExp)


def test_jointpackage::ecore2maude::trgrenmodexp_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgRenModExp.__init__)


def test_jointpackage::ecore2maude::trgrenmodexp_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgRenModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgtheoryidmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgTheoryIdModExp)


def test_jointpackage::ecore2maude::trgtheoryidmodexp_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgTheoryIdModExp.__init__)


def test_jointpackage::ecore2maude::trgtheoryidmodexp_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgTheoryIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmoduleidmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgModuleIdModExp)


def test_jointpackage::ecore2maude::trgmoduleidmodexp_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgModuleIdModExp.__init__)


def test_jointpackage::ecore2maude::trgmoduleidmodexp_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgModuleIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgparameter_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgParameter)


def test_jointpackage::ecore2maude::trgparameter_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgParameter.__init__)


def test_jointpackage::ecore2maude::trgparameter_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgParameter.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage::ecore2maude::trgparameter_has_label():
    assert hasattr(jointPackage::Ecore2Maude::TrgParameter, "label")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::TrgParameter.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgcompmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgCompModExp)


def test_jointpackage::ecore2maude::trgcompmodexp_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgCompModExp.__init__)


def test_jointpackage::ecore2maude::trgcompmodexp_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgCompModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trginstmodexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgInstModExp)


def test_jointpackage::ecore2maude::trginstmodexp_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgInstModExp.__init__)


def test_jointpackage::ecore2maude::trginstmodexp_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgInstModExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmodexpression_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgModExpression)


def test_jointpackage::ecore2maude::trgmodexpression_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgModExpression.__init__)


def test_jointpackage::ecore2maude::trgmodexpression_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgModExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::trgmatchingcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgMatchingCond)


def test_jointpackage::ecore2maude::trgmatchingcond_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgMatchingCond.__init__)


def test_jointpackage::ecore2maude::trgmatchingcond_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgMatchingCond.__init__)
    params = list(sig.parameters.keys())



def test_srcedatatype_is_not_abstract():
    assert not inspect.isabstract(SrcEDataType)


def test_srcedatatype_constructor_exists():
    assert callable(SrcEDataType.__init__)


def test_srcedatatype_constructor_args():
    sig = inspect.signature(SrcEDataType.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srceenum_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEEnum)


def test_jointpackage::ecore2maude::srceenum_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEEnum.__init__)


def test_jointpackage::ecore2maude::srceenum_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEEnum.__init__)
    params = list(sig.parameters.keys())



def test_srcenamedelement_is_not_abstract():
    assert not inspect.isabstract(SrcENamedElement)


def test_srcenamedelement_constructor_exists():
    assert callable(SrcENamedElement.__init__)


def test_srcenamedelement_constructor_args():
    sig = inspect.signature(SrcENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srcepackage_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEPackage)


def test_jointpackage::ecore2maude::srcepackage_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEPackage.__init__)


def test_jointpackage::ecore2maude::srcepackage_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"

def test_jointpackage::ecore2maude::srcepackage_has_nsURI():
    assert hasattr(jointPackage::Ecore2Maude::SrcEPackage, "nsURI")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEPackage.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcepackage_has_nsPrefix():
    assert hasattr(jointPackage::Ecore2Maude::SrcEPackage, "nsPrefix")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEPackage.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::srcetypedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcETypedElement)


def test_jointpackage::ecore2maude::srcetypedelement_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcETypedElement.__init__)


def test_jointpackage::ecore2maude::srcetypedelement_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "required" in params, "Missing parameter 'required'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "many" in params, "Missing parameter 'many'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_jointpackage::ecore2maude::srcetypedelement_has_lowerBound():
    assert hasattr(jointPackage::Ecore2Maude::SrcETypedElement, "lowerBound")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcETypedElement.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcetypedelement_has_required():
    assert hasattr(jointPackage::Ecore2Maude::SrcETypedElement, "required")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcETypedElement.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcetypedelement_has_unique():
    assert hasattr(jointPackage::Ecore2Maude::SrcETypedElement, "unique")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcETypedElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcetypedelement_has_many():
    assert hasattr(jointPackage::Ecore2Maude::SrcETypedElement, "many")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcETypedElement.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcetypedelement_has_ordered():
    assert hasattr(jointPackage::Ecore2Maude::SrcETypedElement, "ordered")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcETypedElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcetypedelement_has_upperBound():
    assert hasattr(jointPackage::Ecore2Maude::SrcETypedElement, "upperBound")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcETypedElement.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::srceclassifier_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEClassifier)


def test_jointpackage::ecore2maude::srceclassifier_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEClassifier.__init__)


def test_jointpackage::ecore2maude::srceclassifier_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "instanceTypeName" in params, "Missing parameter 'instanceTypeName'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_jointpackage::ecore2maude::srceclassifier_has_instanceTypeName():
    assert hasattr(jointPackage::Ecore2Maude::SrcEClassifier, "instanceTypeName")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEClassifier.__mro__:
        if "instanceTypeName" in klass.__dict__:
            descriptor = klass.__dict__["instanceTypeName"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srceclassifier_has_instanceClassName():
    assert hasattr(jointPackage::Ecore2Maude::SrcEClassifier, "instanceClassName")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEClassifier.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_srcetypedelement_is_not_abstract():
    assert not inspect.isabstract(SrcETypedElement)


def test_srcetypedelement_constructor_exists():
    assert callable(SrcETypedElement.__init__)


def test_srcetypedelement_constructor_args():
    sig = inspect.signature(SrcETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srcestructuralfeature_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEStructuralFeature)


def test_jointpackage::ecore2maude::srcestructuralfeature_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEStructuralFeature.__init__)


def test_jointpackage::ecore2maude::srcestructuralfeature_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "unsettable" in params, "Missing parameter 'unsettable'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"

def test_jointpackage::ecore2maude::srcestructuralfeature_has_unsettable():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStructuralFeature, "unsettable")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStructuralFeature.__mro__:
        if "unsettable" in klass.__dict__:
            descriptor = klass.__dict__["unsettable"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcestructuralfeature_has_changeable():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStructuralFeature, "changeable")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStructuralFeature.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcestructuralfeature_has_defaultValueLiteral():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStructuralFeature, "defaultValueLiteral")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStructuralFeature.__mro__:
        if "defaultValueLiteral" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueLiteral"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcestructuralfeature_has_derived():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStructuralFeature, "derived")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStructuralFeature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcestructuralfeature_has_transient():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStructuralFeature, "transient")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStructuralFeature.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcestructuralfeature_has_volatile():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStructuralFeature, "volatile")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStructuralFeature.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::srceparameter_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEParameter)


def test_jointpackage::ecore2maude::srceparameter_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEParameter.__init__)


def test_jointpackage::ecore2maude::srceparameter_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEParameter.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srcenamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcENamedElement)


def test_jointpackage::ecore2maude::srcenamedelement_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcENamedElement.__init__)


def test_jointpackage::ecore2maude::srcenamedelement_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::ecore2maude::srcenamedelement_has_name():
    assert hasattr(jointPackage::Ecore2Maude::SrcENamedElement, "name")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcENamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::srceenumliteral_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEEnumLiteral)


def test_jointpackage::ecore2maude::srceenumliteral_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEEnumLiteral.__init__)


def test_jointpackage::ecore2maude::srceenumliteral_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "literal" in params, "Missing parameter 'literal'"

def test_jointpackage::ecore2maude::srceenumliteral_has_value():
    assert hasattr(jointPackage::Ecore2Maude::SrcEEnumLiteral, "value")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srceenumliteral_has_literal():
    assert hasattr(jointPackage::Ecore2Maude::SrcEEnumLiteral, "literal")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEEnumLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_srceclassifier_is_not_abstract():
    assert not inspect.isabstract(SrcEClassifier)


def test_srceclassifier_constructor_exists():
    assert callable(SrcEClassifier.__init__)


def test_srceclassifier_constructor_args():
    sig = inspect.signature(SrcEClassifier.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srceclass_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEClass)


def test_jointpackage::ecore2maude::srceclass_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEClass.__init__)


def test_jointpackage::ecore2maude::srceclass_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEClass.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_jointpackage::ecore2maude::srceclass_has_interface():
    assert hasattr(jointPackage::Ecore2Maude::SrcEClass, "interface")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEClass.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srceclass_has_abstract():
    assert hasattr(jointPackage::Ecore2Maude::SrcEClass, "abstract")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::srcedatatype_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEDataType)


def test_jointpackage::ecore2maude::srcedatatype_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEDataType.__init__)


def test_jointpackage::ecore2maude::srcedatatype_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"

def test_jointpackage::ecore2maude::srcedatatype_has_serializable():
    assert hasattr(jointPackage::Ecore2Maude::SrcEDataType, "serializable")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEDataType.__mro__:
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



def test_jointpackage::ecore2maude::srceattribute_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEAttribute)


def test_jointpackage::ecore2maude::srceattribute_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEAttribute.__init__)


def test_jointpackage::ecore2maude::srceattribute_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_jointpackage::ecore2maude::srceattribute_has_iD():
    assert hasattr(jointPackage::Ecore2Maude::SrcEAttribute, "iD")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEAttribute.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::trgequalcond_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::TrgEqualCond)


def test_jointpackage::ecore2maude::trgequalcond_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::TrgEqualCond.__init__)


def test_jointpackage::ecore2maude::trgequalcond_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::TrgEqualCond.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srcestringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEStringToStringMapEntry)


def test_jointpackage::ecore2maude::srcestringtostringmapentry_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEStringToStringMapEntry.__init__)


def test_jointpackage::ecore2maude::srcestringtostringmapentry_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage::ecore2maude::srcestringtostringmapentry_has_key():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStringToStringMapEntry, "key")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcestringtostringmapentry_has_value():
    assert hasattr(jointPackage::Ecore2Maude::SrcEStringToStringMapEntry, "value")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEStringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::JointMM)


def test_jointpackage::ecore2maude::jointmm_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::JointMM.__init__)


def test_jointpackage::ecore2maude::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::JointMM.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::ecore2maude::srcereference_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEReference)


def test_jointpackage::ecore2maude::srcereference_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEReference.__init__)


def test_jointpackage::ecore2maude::srcereference_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEReference.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"
    assert "container" in params, "Missing parameter 'container'"
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"

def test_jointpackage::ecore2maude::srcereference_has_containment():
    assert hasattr(jointPackage::Ecore2Maude::SrcEReference, "containment")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEReference.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcereference_has_container():
    assert hasattr(jointPackage::Ecore2Maude::SrcEReference, "container")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEReference.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::ecore2maude::srcereference_has_resolveProxies():
    assert hasattr(jointPackage::Ecore2Maude::SrcEReference, "resolveProxies")
    descriptor = None
    for klass in jointPackage::Ecore2Maude::SrcEReference.__mro__:
        if "resolveProxies" in klass.__dict__:
            descriptor = klass.__dict__["resolveProxies"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::ecore2maude::srceoperation_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Ecore2Maude::SrcEOperation)


def test_jointpackage::ecore2maude::srceoperation_constructor_exists():
    assert callable(jointPackage::Ecore2Maude::SrcEOperation.__init__)


def test_jointpackage::ecore2maude::srceoperation_constructor_args():
    sig = inspect.signature(jointPackage::Ecore2Maude::SrcEOperation.__init__)
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
TrgCondition_strategy = st.builds(
    TrgCondition,
)
jointPackage::Ecore2Maude::TrgRewriteCond_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgRewriteCond,
)
jointPackage::Ecore2Maude::TrgEquationalCond_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgEquationalCond,
)
jointPackage::Ecore2Maude::TrgCondition_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgCondition,
)
TrgRenMapping_strategy = st.builds(
    TrgRenMapping,
)
jointPackage::Ecore2Maude::TrgOpTypedMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgOpTypedMapping,
    atts=
        safe_text,
    to=
        safe_text
)
jointPackage::Ecore2Maude::TrgOpMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgOpMapping,
    to=
        safe_text
)
jointPackage::Ecore2Maude::TrgLabelMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgLabelMapping,
    from_=
        safe_text,
    to=
        safe_text
)
jointPackage::Ecore2Maude::TrgSortMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgSortMapping,
    to=
        safe_text
)
TrgViewMapping_strategy = st.builds(
    TrgViewMapping,
)
jointPackage::Ecore2Maude::TrgTermMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgTermMapping,
)
jointPackage::Ecore2Maude::TrgViewMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgViewMapping,
)
TrgTerm_strategy = st.builds(
    TrgTerm,
)
jointPackage::Ecore2Maude::TrgVariable_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgVariable,
    name=
        safe_text
)
jointPackage::Ecore2Maude::TrgRecTerm_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgRecTerm,
    op=
        safe_text
)
jointPackage::Ecore2Maude::TrgConstant_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgConstant,
    op=
        safe_text
)
TrgModule_strategy = st.builds(
    TrgModule,
)
jointPackage::Ecore2Maude::TrgSModule_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgSModule,
)
jointPackage::Ecore2Maude::TrgFModule_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgFModule,
)
TrgTheory_strategy = st.builds(
    TrgTheory,
)
jointPackage::Ecore2Maude::TrgSTheory_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgSTheory,
)
jointPackage::Ecore2Maude::TrgFTheory_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgFTheory,
)
jointPackage::Ecore2Maude::TrgModElement_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgModElement,
)
TrgMaudeTopEl_strategy = st.builds(
    TrgMaudeTopEl,
)
jointPackage::Ecore2Maude::TrgTheory_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgTheory,
)
TrgType_strategy = st.builds(
    TrgType,
)
jointPackage::Ecore2Maude::TrgKind_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgKind,
)
jointPackage::Ecore2Maude::TrgType_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgType,
    name=
        safe_text
)
TrgModElement_strategy = st.builds(
    TrgModElement,
)
jointPackage::Ecore2Maude::TrgStatement_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgStatement,
    atts=
        safe_text,
    label=
        safe_text
)
jointPackage::Ecore2Maude::TrgOperation_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgOperation,
    name=
        safe_text,
    atts=
        safe_text
)
jointPackage::Ecore2Maude::TrgSubsortRel_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgSubsortRel,
)
jointPackage::Ecore2Maude::TrgModImportation_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgModImportation,
)
TrgEquationalCond_strategy = st.builds(
    TrgEquationalCond,
)
jointPackage::Ecore2Maude::TrgBooleanCond_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgBooleanCond,
)
jointPackage::Ecore2Maude::TrgMembershipCond_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgMembershipCond,
)
jointPackage::Ecore2Maude::TrgSort_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgSort,
)
jointPackage::Ecore2Maude::TrgTerm_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgTerm,
)
TrgStatement_strategy = st.builds(
    TrgStatement,
)
jointPackage::Ecore2Maude::TrgEquation_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgEquation,
)
jointPackage::Ecore2Maude::TrgRule_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgRule,
)
jointPackage::Ecore2Maude::TrgMembership_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgMembership,
)
jointPackage::Ecore2Maude::TrgMaudeTopEl_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgMaudeTopEl,
    name=
        safe_text
)
jointPackage::Ecore2Maude::TrgMaudeSpec_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgMaudeSpec,
)
jointPackage::Ecore2Maude::TrgModule_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgModule,
)
jointPackage::Ecore2Maude::TrgRenMapping_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgRenMapping,
)
jointPackage::Ecore2Maude::TrgView_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgView,
)
TrgModExpression_strategy = st.builds(
    TrgModExpression,
)
jointPackage::Ecore2Maude::TrgRenModExp_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgRenModExp,
)
jointPackage::Ecore2Maude::TrgTheoryIdModExp_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgTheoryIdModExp,
)
jointPackage::Ecore2Maude::TrgModuleIdModExp_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgModuleIdModExp,
)
jointPackage::Ecore2Maude::TrgParameter_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgParameter,
    label=
        safe_text
)
jointPackage::Ecore2Maude::TrgCompModExp_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgCompModExp,
)
jointPackage::Ecore2Maude::TrgInstModExp_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgInstModExp,
)
jointPackage::Ecore2Maude::TrgModExpression_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgModExpression,
)
jointPackage::Ecore2Maude::TrgMatchingCond_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgMatchingCond,
)
SrcEDataType_strategy = st.builds(
    SrcEDataType,
)
jointPackage::Ecore2Maude::SrcEEnum_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEEnum,
)
SrcENamedElement_strategy = st.builds(
    SrcENamedElement,
)
jointPackage::Ecore2Maude::SrcEPackage_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEPackage,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
jointPackage::Ecore2Maude::SrcETypedElement_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcETypedElement,
    lowerBound=
        st.integers(),
    required=
        st.booleans(),
    unique=
        st.booleans(),
    many=
        st.booleans(),
    ordered=
        st.booleans(),
    upperBound=
        st.integers()
)
jointPackage::Ecore2Maude::SrcEClassifier_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEClassifier,
    instanceTypeName=
        safe_text,
    instanceClassName=
        safe_text
)
SrcETypedElement_strategy = st.builds(
    SrcETypedElement,
)
jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEStructuralFeature,
    unsettable=
        st.booleans(),
    changeable=
        st.booleans(),
    defaultValueLiteral=
        safe_text,
    derived=
        st.booleans(),
    transient=
        st.booleans(),
    volatile=
        st.booleans()
)
jointPackage::Ecore2Maude::SrcEParameter_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEParameter,
)
jointPackage::Ecore2Maude::SrcENamedElement_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcENamedElement,
    name=
        safe_text
)
jointPackage::Ecore2Maude::SrcEEnumLiteral_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEEnumLiteral,
    value=
        st.integers(),
    literal=
        safe_text
)
SrcEClassifier_strategy = st.builds(
    SrcEClassifier,
)
jointPackage::Ecore2Maude::SrcEClass_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEClass,
    interface=
        st.booleans(),
    abstract=
        st.booleans()
)
jointPackage::Ecore2Maude::SrcEDataType_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEDataType,
    serializable=
        st.booleans()
)
SrcEStructuralFeature_strategy = st.builds(
    SrcEStructuralFeature,
)
jointPackage::Ecore2Maude::SrcEAttribute_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEAttribute,
    iD=
        st.booleans()
)
jointPackage::Ecore2Maude::TrgEqualCond_strategy = st.builds(
    jointPackage::Ecore2Maude::TrgEqualCond,
)
jointPackage::Ecore2Maude::SrcEStringToStringMapEntry_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEStringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
jointPackage::Ecore2Maude::JointMM_strategy = st.builds(
    jointPackage::Ecore2Maude::JointMM,
)
jointPackage::Ecore2Maude::SrcEReference_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEReference,
    containment=
        st.booleans(),
    container=
        st.booleans(),
    resolveProxies=
        st.booleans()
)
jointPackage::Ecore2Maude::SrcEOperation_strategy = st.builds(
    jointPackage::Ecore2Maude::SrcEOperation,
)

@given(instance=TrgCondition_strategy)
@settings(max_examples=50)
def test_trgcondition_instantiation(instance):
    assert isinstance(instance, TrgCondition)

@given(instance=jointPackage::Ecore2Maude::TrgRewriteCond_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgrewritecond_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgRewriteCond)

@given(instance=jointPackage::Ecore2Maude::TrgEquationalCond_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgequationalcond_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgEquationalCond)

@given(instance=jointPackage::Ecore2Maude::TrgCondition_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgcondition_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgCondition)

@given(instance=TrgRenMapping_strategy)
@settings(max_examples=50)
def test_trgrenmapping_instantiation(instance):
    assert isinstance(instance, TrgRenMapping)

@given(instance=jointPackage::Ecore2Maude::TrgOpTypedMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgoptypedmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgOpTypedMapping)

@given(instance=jointPackage::Ecore2Maude::TrgOpTypedMapping_strategy)
def test_jointpackage::ecore2maude::trgoptypedmapping_atts_type(instance):
    assert isinstance(instance.atts, str)


@given(instance=jointPackage::Ecore2Maude::TrgOpTypedMapping_strategy)
def test_jointpackage::ecore2maude::trgoptypedmapping_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=jointPackage::Ecore2Maude::TrgOpTypedMapping_strategy)
def test_jointpackage::ecore2maude::trgoptypedmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jointPackage::Ecore2Maude::TrgOpTypedMapping_strategy)
def test_jointpackage::ecore2maude::trgoptypedmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jointPackage::Ecore2Maude::TrgOpMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgopmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgOpMapping)

@given(instance=jointPackage::Ecore2Maude::TrgOpMapping_strategy)
def test_jointpackage::ecore2maude::trgopmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jointPackage::Ecore2Maude::TrgOpMapping_strategy)
def test_jointpackage::ecore2maude::trgopmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jointPackage::Ecore2Maude::TrgLabelMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trglabelmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgLabelMapping)

@given(instance=jointPackage::Ecore2Maude::TrgLabelMapping_strategy)
def test_jointpackage::ecore2maude::trglabelmapping_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=jointPackage::Ecore2Maude::TrgLabelMapping_strategy)
def test_jointpackage::ecore2maude::trglabelmapping_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=jointPackage::Ecore2Maude::TrgLabelMapping_strategy)
def test_jointpackage::ecore2maude::trglabelmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jointPackage::Ecore2Maude::TrgLabelMapping_strategy)
def test_jointpackage::ecore2maude::trglabelmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=jointPackage::Ecore2Maude::TrgSortMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgsortmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgSortMapping)

@given(instance=jointPackage::Ecore2Maude::TrgSortMapping_strategy)
def test_jointpackage::ecore2maude::trgsortmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=jointPackage::Ecore2Maude::TrgSortMapping_strategy)
def test_jointpackage::ecore2maude::trgsortmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=TrgViewMapping_strategy)
@settings(max_examples=50)
def test_trgviewmapping_instantiation(instance):
    assert isinstance(instance, TrgViewMapping)

@given(instance=jointPackage::Ecore2Maude::TrgTermMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgtermmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgTermMapping)

@given(instance=jointPackage::Ecore2Maude::TrgViewMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgviewmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgViewMapping)

@given(instance=TrgTerm_strategy)
@settings(max_examples=50)
def test_trgterm_instantiation(instance):
    assert isinstance(instance, TrgTerm)

@given(instance=jointPackage::Ecore2Maude::TrgVariable_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgvariable_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgVariable)

@given(instance=jointPackage::Ecore2Maude::TrgVariable_strategy)
def test_jointpackage::ecore2maude::trgvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Ecore2Maude::TrgVariable_strategy)
def test_jointpackage::ecore2maude::trgvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::Ecore2Maude::TrgRecTerm_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgrecterm_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgRecTerm)

@given(instance=jointPackage::Ecore2Maude::TrgRecTerm_strategy)
def test_jointpackage::ecore2maude::trgrecterm_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=jointPackage::Ecore2Maude::TrgRecTerm_strategy)
def test_jointpackage::ecore2maude::trgrecterm_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jointPackage::Ecore2Maude::TrgConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgConstant)

@given(instance=jointPackage::Ecore2Maude::TrgConstant_strategy)
def test_jointpackage::ecore2maude::trgconstant_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=jointPackage::Ecore2Maude::TrgConstant_strategy)
def test_jointpackage::ecore2maude::trgconstant_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=TrgModule_strategy)
@settings(max_examples=50)
def test_trgmodule_instantiation(instance):
    assert isinstance(instance, TrgModule)

@given(instance=jointPackage::Ecore2Maude::TrgSModule_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgsmodule_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgSModule)

@given(instance=jointPackage::Ecore2Maude::TrgFModule_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgfmodule_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgFModule)

@given(instance=TrgTheory_strategy)
@settings(max_examples=50)
def test_trgtheory_instantiation(instance):
    assert isinstance(instance, TrgTheory)

@given(instance=jointPackage::Ecore2Maude::TrgSTheory_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgstheory_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgSTheory)

@given(instance=jointPackage::Ecore2Maude::TrgFTheory_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgftheory_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgFTheory)

@given(instance=jointPackage::Ecore2Maude::TrgModElement_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmodelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgModElement)

@given(instance=TrgMaudeTopEl_strategy)
@settings(max_examples=50)
def test_trgmaudetopel_instantiation(instance):
    assert isinstance(instance, TrgMaudeTopEl)

@given(instance=jointPackage::Ecore2Maude::TrgTheory_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgtheory_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgTheory)

@given(instance=TrgType_strategy)
@settings(max_examples=50)
def test_trgtype_instantiation(instance):
    assert isinstance(instance, TrgType)

@given(instance=jointPackage::Ecore2Maude::TrgKind_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgkind_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgKind)

@given(instance=jointPackage::Ecore2Maude::TrgType_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgtype_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgType)

@given(instance=jointPackage::Ecore2Maude::TrgType_strategy)
def test_jointpackage::ecore2maude::trgtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Ecore2Maude::TrgType_strategy)
def test_jointpackage::ecore2maude::trgtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrgModElement_strategy)
@settings(max_examples=50)
def test_trgmodelement_instantiation(instance):
    assert isinstance(instance, TrgModElement)

@given(instance=jointPackage::Ecore2Maude::TrgStatement_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgstatement_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgStatement)

@given(instance=jointPackage::Ecore2Maude::TrgStatement_strategy)
def test_jointpackage::ecore2maude::trgstatement_atts_type(instance):
    assert isinstance(instance.atts, str)


@given(instance=jointPackage::Ecore2Maude::TrgStatement_strategy)
def test_jointpackage::ecore2maude::trgstatement_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=jointPackage::Ecore2Maude::TrgStatement_strategy)
def test_jointpackage::ecore2maude::trgstatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=jointPackage::Ecore2Maude::TrgStatement_strategy)
def test_jointpackage::ecore2maude::trgstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=jointPackage::Ecore2Maude::TrgOperation_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgoperation_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgOperation)

@given(instance=jointPackage::Ecore2Maude::TrgOperation_strategy)
def test_jointpackage::ecore2maude::trgoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Ecore2Maude::TrgOperation_strategy)
def test_jointpackage::ecore2maude::trgoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::Ecore2Maude::TrgOperation_strategy)
def test_jointpackage::ecore2maude::trgoperation_atts_type(instance):
    assert isinstance(instance.atts, str)


@given(instance=jointPackage::Ecore2Maude::TrgOperation_strategy)
def test_jointpackage::ecore2maude::trgoperation_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=jointPackage::Ecore2Maude::TrgSubsortRel_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgsubsortrel_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgSubsortRel)

@given(instance=jointPackage::Ecore2Maude::TrgModImportation_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmodimportation_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgModImportation)

@given(instance=TrgEquationalCond_strategy)
@settings(max_examples=50)
def test_trgequationalcond_instantiation(instance):
    assert isinstance(instance, TrgEquationalCond)

@given(instance=jointPackage::Ecore2Maude::TrgBooleanCond_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgbooleancond_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgBooleanCond)

@given(instance=jointPackage::Ecore2Maude::TrgMembershipCond_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmembershipcond_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgMembershipCond)

@given(instance=jointPackage::Ecore2Maude::TrgSort_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgsort_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgSort)

@given(instance=jointPackage::Ecore2Maude::TrgTerm_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgterm_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgTerm)

@given(instance=TrgStatement_strategy)
@settings(max_examples=50)
def test_trgstatement_instantiation(instance):
    assert isinstance(instance, TrgStatement)

@given(instance=jointPackage::Ecore2Maude::TrgEquation_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgequation_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgEquation)

@given(instance=jointPackage::Ecore2Maude::TrgRule_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgrule_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgRule)

@given(instance=jointPackage::Ecore2Maude::TrgMembership_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmembership_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgMembership)

@given(instance=jointPackage::Ecore2Maude::TrgMaudeTopEl_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmaudetopel_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgMaudeTopEl)

@given(instance=jointPackage::Ecore2Maude::TrgMaudeTopEl_strategy)
def test_jointpackage::ecore2maude::trgmaudetopel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Ecore2Maude::TrgMaudeTopEl_strategy)
def test_jointpackage::ecore2maude::trgmaudetopel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::Ecore2Maude::TrgMaudeSpec_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmaudespec_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgMaudeSpec)

@given(instance=jointPackage::Ecore2Maude::TrgModule_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmodule_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgModule)

@given(instance=jointPackage::Ecore2Maude::TrgRenMapping_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgrenmapping_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgRenMapping)

@given(instance=jointPackage::Ecore2Maude::TrgView_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgview_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgView)

@given(instance=TrgModExpression_strategy)
@settings(max_examples=50)
def test_trgmodexpression_instantiation(instance):
    assert isinstance(instance, TrgModExpression)

@given(instance=jointPackage::Ecore2Maude::TrgRenModExp_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgrenmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgRenModExp)

@given(instance=jointPackage::Ecore2Maude::TrgTheoryIdModExp_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgtheoryidmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgTheoryIdModExp)

@given(instance=jointPackage::Ecore2Maude::TrgModuleIdModExp_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmoduleidmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgModuleIdModExp)

@given(instance=jointPackage::Ecore2Maude::TrgParameter_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgparameter_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgParameter)

@given(instance=jointPackage::Ecore2Maude::TrgParameter_strategy)
def test_jointpackage::ecore2maude::trgparameter_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=jointPackage::Ecore2Maude::TrgParameter_strategy)
def test_jointpackage::ecore2maude::trgparameter_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=jointPackage::Ecore2Maude::TrgCompModExp_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgcompmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgCompModExp)

@given(instance=jointPackage::Ecore2Maude::TrgInstModExp_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trginstmodexp_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgInstModExp)

@given(instance=jointPackage::Ecore2Maude::TrgModExpression_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmodexpression_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgModExpression)

@given(instance=jointPackage::Ecore2Maude::TrgMatchingCond_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgmatchingcond_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgMatchingCond)

@given(instance=SrcEDataType_strategy)
@settings(max_examples=50)
def test_srcedatatype_instantiation(instance):
    assert isinstance(instance, SrcEDataType)

@given(instance=jointPackage::Ecore2Maude::SrcEEnum_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceenum_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEEnum)

@given(instance=SrcENamedElement_strategy)
@settings(max_examples=50)
def test_srcenamedelement_instantiation(instance):
    assert isinstance(instance, SrcENamedElement)

@given(instance=jointPackage::Ecore2Maude::SrcEPackage_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcepackage_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEPackage)

@given(instance=jointPackage::Ecore2Maude::SrcEPackage_strategy)
def test_jointpackage::ecore2maude::srcepackage_nsURI_type(instance):
    assert isinstance(instance.nsURI, str)


@given(instance=jointPackage::Ecore2Maude::SrcEPackage_strategy)
def test_jointpackage::ecore2maude::srcepackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

@given(instance=jointPackage::Ecore2Maude::SrcEPackage_strategy)
def test_jointpackage::ecore2maude::srcepackage_nsPrefix_type(instance):
    assert isinstance(instance.nsPrefix, str)


@given(instance=jointPackage::Ecore2Maude::SrcEPackage_strategy)
def test_jointpackage::ecore2maude::srcepackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcetypedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcETypedElement)

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=jointPackage::Ecore2Maude::SrcETypedElement_strategy)
def test_jointpackage::ecore2maude::srcetypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=jointPackage::Ecore2Maude::SrcEClassifier_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceclassifier_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEClassifier)

@given(instance=jointPackage::Ecore2Maude::SrcEClassifier_strategy)
def test_jointpackage::ecore2maude::srceclassifier_instanceTypeName_type(instance):
    assert isinstance(instance.instanceTypeName, str)


@given(instance=jointPackage::Ecore2Maude::SrcEClassifier_strategy)
def test_jointpackage::ecore2maude::srceclassifier_instanceTypeName_setter(instance):
    original = instance.instanceTypeName
    instance.instanceTypeName = original
    assert instance.instanceTypeName == original

@given(instance=jointPackage::Ecore2Maude::SrcEClassifier_strategy)
def test_jointpackage::ecore2maude::srceclassifier_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=jointPackage::Ecore2Maude::SrcEClassifier_strategy)
def test_jointpackage::ecore2maude::srceclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=SrcETypedElement_strategy)
@settings(max_examples=50)
def test_srcetypedelement_instantiation(instance):
    assert isinstance(instance, SrcETypedElement)

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcestructuralfeature_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEStructuralFeature)

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_unsettable_type(instance):
    assert isinstance(instance.unsettable, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_defaultValueLiteral_type(instance):
    assert isinstance(instance.defaultValueLiteral, str)


@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_volatile_type(instance):
    assert isinstance(instance.volatile, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEStructuralFeature_strategy)
def test_jointpackage::ecore2maude::srcestructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=jointPackage::Ecore2Maude::SrcEParameter_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceparameter_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEParameter)

@given(instance=jointPackage::Ecore2Maude::SrcENamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcenamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcENamedElement)

@given(instance=jointPackage::Ecore2Maude::SrcENamedElement_strategy)
def test_jointpackage::ecore2maude::srcenamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Ecore2Maude::SrcENamedElement_strategy)
def test_jointpackage::ecore2maude::srcenamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::Ecore2Maude::SrcEEnumLiteral_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceenumliteral_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEEnumLiteral)

@given(instance=jointPackage::Ecore2Maude::SrcEEnumLiteral_strategy)
def test_jointpackage::ecore2maude::srceenumliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=jointPackage::Ecore2Maude::SrcEEnumLiteral_strategy)
def test_jointpackage::ecore2maude::srceenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage::Ecore2Maude::SrcEEnumLiteral_strategy)
def test_jointpackage::ecore2maude::srceenumliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=jointPackage::Ecore2Maude::SrcEEnumLiteral_strategy)
def test_jointpackage::ecore2maude::srceenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=SrcEClassifier_strategy)
@settings(max_examples=50)
def test_srceclassifier_instantiation(instance):
    assert isinstance(instance, SrcEClassifier)

@given(instance=jointPackage::Ecore2Maude::SrcEClass_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceclass_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEClass)

@given(instance=jointPackage::Ecore2Maude::SrcEClass_strategy)
def test_jointpackage::ecore2maude::srceclass_interface_type(instance):
    assert isinstance(instance.interface, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEClass_strategy)
def test_jointpackage::ecore2maude::srceclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=jointPackage::Ecore2Maude::SrcEClass_strategy)
def test_jointpackage::ecore2maude::srceclass_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEClass_strategy)
def test_jointpackage::ecore2maude::srceclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jointPackage::Ecore2Maude::SrcEClass_strategy)
@settings(max_examples=30)
def test_jointpackage::ecore2maude::srceclass_issupertypeof_changes_state(instance):
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
        assert has_statements, f"Function 'isSuperTypeOf' in jointPackage::Ecore2Maude::SrcEClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in jointPackage::Ecore2Maude::SrcEClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in jointPackage::Ecore2Maude::SrcEClass is not implemented or raised an error")

@given(instance=jointPackage::Ecore2Maude::SrcEDataType_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcedatatype_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEDataType)

@given(instance=jointPackage::Ecore2Maude::SrcEDataType_strategy)
def test_jointpackage::ecore2maude::srcedatatype_serializable_type(instance):
    assert isinstance(instance.serializable, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEDataType_strategy)
def test_jointpackage::ecore2maude::srcedatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original

@given(instance=SrcEStructuralFeature_strategy)
@settings(max_examples=50)
def test_srcestructuralfeature_instantiation(instance):
    assert isinstance(instance, SrcEStructuralFeature)

@given(instance=jointPackage::Ecore2Maude::SrcEAttribute_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceattribute_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEAttribute)

@given(instance=jointPackage::Ecore2Maude::SrcEAttribute_strategy)
def test_jointpackage::ecore2maude::srceattribute_iD_type(instance):
    assert isinstance(instance.iD, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEAttribute_strategy)
def test_jointpackage::ecore2maude::srceattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=jointPackage::Ecore2Maude::TrgEqualCond_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::trgequalcond_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::TrgEqualCond)

@given(instance=jointPackage::Ecore2Maude::SrcEStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcestringtostringmapentry_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEStringToStringMapEntry)

@given(instance=jointPackage::Ecore2Maude::SrcEStringToStringMapEntry_strategy)
def test_jointpackage::ecore2maude::srcestringtostringmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=jointPackage::Ecore2Maude::SrcEStringToStringMapEntry_strategy)
def test_jointpackage::ecore2maude::srcestringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=jointPackage::Ecore2Maude::SrcEStringToStringMapEntry_strategy)
def test_jointpackage::ecore2maude::srcestringtostringmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=jointPackage::Ecore2Maude::SrcEStringToStringMapEntry_strategy)
def test_jointpackage::ecore2maude::srcestringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage::Ecore2Maude::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::JointMM)

@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srcereference_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEReference)

@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
def test_jointpackage::ecore2maude::srcereference_containment_type(instance):
    assert isinstance(instance.containment, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
def test_jointpackage::ecore2maude::srcereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original

@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
def test_jointpackage::ecore2maude::srcereference_container_type(instance):
    assert isinstance(instance.container, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
def test_jointpackage::ecore2maude::srcereference_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
def test_jointpackage::ecore2maude::srcereference_resolveProxies_type(instance):
    assert isinstance(instance.resolveProxies, bool)


@given(instance=jointPackage::Ecore2Maude::SrcEReference_strategy)
def test_jointpackage::ecore2maude::srcereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original

@given(instance=jointPackage::Ecore2Maude::SrcEOperation_strategy)
@settings(max_examples=50)
def test_jointpackage::ecore2maude::srceoperation_instantiation(instance):
    assert isinstance(instance, jointPackage::Ecore2Maude::SrcEOperation)
