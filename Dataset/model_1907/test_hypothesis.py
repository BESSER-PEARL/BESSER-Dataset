import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OclLiteral,
    umm_OclIntegerLiteral,
    umm_OclBooleanLiteral,
    umm_OclStringLiteral,
    umm_OclEnumerationLiteral,
    OclFunctionCall,
    umm_OclIsEmpty,
    umm_OclNotEmpty,
    umm_OclSize,
    umm_OclForAll,
    umm_OclFunctionCall,
    OclBooleanLiteral,
    umm_OclBooleanTrue,
    umm_OclBooleanFalse,
    CDTProperty,
    umm_CDT_Supplement,
    umm_CDT_Content,
    umm_CDTProperty,
    umm_OclRef,
    umm_OclPathTail,
    OclReference,
    umm_OclPathFeatureHead,
    umm_OclPathSelfHead,
    OclValue,
    umm_OclLiteral,
    umm_OclReference,
    OclExpression,
    umm_OclLessOrEqual,
    umm_OclOr,
    umm_OclMoreOrEqual,
    umm_OclAnd,
    umm_OclMore,
    umm_OclImplies,
    umm_OclEqual,
    umm_OclXor,
    umm_OclLess,
    umm_OclArrow,
    umm_OclValue,
    umm_OclExpression,
    umm_CDT,
    umm_CodelistEntry,
    ACCProperty,
    umm_BCC,
    umm_ASCC,
    umm_ACCProperty,
    umm_ACC,
    BDTProperty,
    umm_Supplement,
    umm_Content,
    AssembledBase,
    umm_Assembled,
    umm_Primitive,
    ENUM,
    umm_Original,
    umm_Subset,
    umm_AssembledBase,
    umm_ENUM,
    ABIEProperty,
    umm_BBIE,
    umm_ASBIE,
    umm_OclInvariant,
    umm_TC_Constraint,
    umm_ContextRef,
    MAProperty,
    umm_ASNONE,
    umm_ASMA,
    OclRef,
    umm_BDTProperty,
    umm_ABIEProperty,
    Library,
    umm_CCLibrary,
    umm_CDTLibrary,
    umm_PrimitiveLibrary,
    umm_ENUMLibrary,
    umm_DocLibrary,
    umm_Library,
    umm_Constraint,
    umm_MAProperty,
    ContextRef,
    umm_ABIE,
    umm_BDT,
    umm_MA,
    umm_InfEnvelope,
    umm_BDTLibrary,
    umm_BIELibrary,
    ConstraintKind,
    MultiplicityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclliteral_is_not_abstract():
    assert not inspect.isabstract(OclLiteral)


def test_oclliteral_constructor_exists():
    assert callable(OclLiteral.__init__)


def test_oclliteral_constructor_args():
    sig = inspect.signature(OclLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclintegerliteral_is_not_abstract():
    assert not inspect.isabstract(umm_OclIntegerLiteral)


def test_umm_oclintegerliteral_constructor_exists():
    assert callable(umm_OclIntegerLiteral.__init__)


def test_umm_oclintegerliteral_constructor_args():
    sig = inspect.signature(umm_OclIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umm_oclintegerliteral_has_value():
    assert hasattr(umm_OclIntegerLiteral, "value")
    descriptor = None
    for klass in umm_OclIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umm_oclbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(umm_OclBooleanLiteral)


def test_umm_oclbooleanliteral_constructor_exists():
    assert callable(umm_OclBooleanLiteral.__init__)


def test_umm_oclbooleanliteral_constructor_args():
    sig = inspect.signature(umm_OclBooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclstringliteral_is_not_abstract():
    assert not inspect.isabstract(umm_OclStringLiteral)


def test_umm_oclstringliteral_constructor_exists():
    assert callable(umm_OclStringLiteral.__init__)


def test_umm_oclstringliteral_constructor_args():
    sig = inspect.signature(umm_OclStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umm_oclstringliteral_has_value():
    assert hasattr(umm_OclStringLiteral, "value")
    descriptor = None
    for klass in umm_OclStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umm_oclenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(umm_OclEnumerationLiteral)


def test_umm_oclenumerationliteral_constructor_exists():
    assert callable(umm_OclEnumerationLiteral.__init__)


def test_umm_oclenumerationliteral_constructor_args():
    sig = inspect.signature(umm_OclEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umm_oclenumerationliteral_has_value():
    assert hasattr(umm_OclEnumerationLiteral, "value")
    descriptor = None
    for klass in umm_OclEnumerationLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclfunctioncall_is_not_abstract():
    assert not inspect.isabstract(OclFunctionCall)


def test_oclfunctioncall_constructor_exists():
    assert callable(OclFunctionCall.__init__)


def test_oclfunctioncall_constructor_args():
    sig = inspect.signature(OclFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclisempty_is_not_abstract():
    assert not inspect.isabstract(umm_OclIsEmpty)


def test_umm_oclisempty_constructor_exists():
    assert callable(umm_OclIsEmpty.__init__)


def test_umm_oclisempty_constructor_args():
    sig = inspect.signature(umm_OclIsEmpty.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclnotempty_is_not_abstract():
    assert not inspect.isabstract(umm_OclNotEmpty)


def test_umm_oclnotempty_constructor_exists():
    assert callable(umm_OclNotEmpty.__init__)


def test_umm_oclnotempty_constructor_args():
    sig = inspect.signature(umm_OclNotEmpty.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclsize_is_not_abstract():
    assert not inspect.isabstract(umm_OclSize)


def test_umm_oclsize_constructor_exists():
    assert callable(umm_OclSize.__init__)


def test_umm_oclsize_constructor_args():
    sig = inspect.signature(umm_OclSize.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclforall_is_not_abstract():
    assert not inspect.isabstract(umm_OclForAll)


def test_umm_oclforall_constructor_exists():
    assert callable(umm_OclForAll.__init__)


def test_umm_oclforall_constructor_args():
    sig = inspect.signature(umm_OclForAll.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclfunctioncall_is_not_abstract():
    assert not inspect.isabstract(umm_OclFunctionCall)


def test_umm_oclfunctioncall_constructor_exists():
    assert callable(umm_OclFunctionCall.__init__)


def test_umm_oclfunctioncall_constructor_args():
    sig = inspect.signature(umm_OclFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_oclbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(OclBooleanLiteral)


def test_oclbooleanliteral_constructor_exists():
    assert callable(OclBooleanLiteral.__init__)


def test_oclbooleanliteral_constructor_args():
    sig = inspect.signature(OclBooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclbooleantrue_is_not_abstract():
    assert not inspect.isabstract(umm_OclBooleanTrue)


def test_umm_oclbooleantrue_constructor_exists():
    assert callable(umm_OclBooleanTrue.__init__)


def test_umm_oclbooleantrue_constructor_args():
    sig = inspect.signature(umm_OclBooleanTrue.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclbooleanfalse_is_not_abstract():
    assert not inspect.isabstract(umm_OclBooleanFalse)


def test_umm_oclbooleanfalse_constructor_exists():
    assert callable(umm_OclBooleanFalse.__init__)


def test_umm_oclbooleanfalse_constructor_args():
    sig = inspect.signature(umm_OclBooleanFalse.__init__)
    params = list(sig.parameters.keys())



def test_cdtproperty_is_not_abstract():
    assert not inspect.isabstract(CDTProperty)


def test_cdtproperty_constructor_exists():
    assert callable(CDTProperty.__init__)


def test_cdtproperty_constructor_args():
    sig = inspect.signature(CDTProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm_cdt_supplement_is_not_abstract():
    assert not inspect.isabstract(umm_CDT_Supplement)


def test_umm_cdt_supplement_constructor_exists():
    assert callable(umm_CDT_Supplement.__init__)


def test_umm_cdt_supplement_constructor_args():
    sig = inspect.signature(umm_CDT_Supplement.__init__)
    params = list(sig.parameters.keys())
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"
    assert "restriction" in params, "Missing parameter 'restriction'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_umm_cdt_supplement_has_fixedValue():
    assert hasattr(umm_CDT_Supplement, "fixedValue")
    descriptor = None
    for klass in umm_CDT_Supplement.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_supplement_has_restriction():
    assert hasattr(umm_CDT_Supplement, "restriction")
    descriptor = None
    for klass in umm_CDT_Supplement.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_supplement_has_defaultValue():
    assert hasattr(umm_CDT_Supplement, "defaultValue")
    descriptor = None
    for klass in umm_CDT_Supplement.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_umm_cdt_content_is_not_abstract():
    assert not inspect.isabstract(umm_CDT_Content)


def test_umm_cdt_content_constructor_exists():
    assert callable(umm_CDT_Content.__init__)


def test_umm_cdt_content_constructor_args():
    sig = inspect.signature(umm_CDT_Content.__init__)
    params = list(sig.parameters.keys())



def test_umm_cdtproperty_is_not_abstract():
    assert not inspect.isabstract(umm_CDTProperty)


def test_umm_cdtproperty_constructor_exists():
    assert callable(umm_CDTProperty.__init__)


def test_umm_cdtproperty_constructor_args():
    sig = inspect.signature(umm_CDTProperty.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"

def test_umm_cdtproperty_has_multiplicity():
    assert hasattr(umm_CDTProperty, "multiplicity")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtproperty_has_name():
    assert hasattr(umm_CDTProperty, "name")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtproperty_has_dictionary():
    assert hasattr(umm_CDTProperty, "dictionary")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtproperty_has_versionIdentifier():
    assert hasattr(umm_CDTProperty, "versionIdentifier")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtproperty_has_definition():
    assert hasattr(umm_CDTProperty, "definition")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtproperty_has_uniqueIdentifier():
    assert hasattr(umm_CDTProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtproperty_has_businessTerm():
    assert hasattr(umm_CDTProperty, "businessTerm")
    descriptor = None
    for klass in umm_CDTProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)



def test_umm_oclref_is_not_abstract():
    assert not inspect.isabstract(umm_OclRef)


def test_umm_oclref_constructor_exists():
    assert callable(umm_OclRef.__init__)


def test_umm_oclref_constructor_args():
    sig = inspect.signature(umm_OclRef.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "name" in params, "Missing parameter 'name'"

def test_umm_oclref_has_multiplicity():
    assert hasattr(umm_OclRef, "multiplicity")
    descriptor = None
    for klass in umm_OclRef.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_umm_oclref_has_name():
    assert hasattr(umm_OclRef, "name")
    descriptor = None
    for klass in umm_OclRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm_oclpathtail_is_not_abstract():
    assert not inspect.isabstract(umm_OclPathTail)


def test_umm_oclpathtail_constructor_exists():
    assert callable(umm_OclPathTail.__init__)


def test_umm_oclpathtail_constructor_args():
    sig = inspect.signature(umm_OclPathTail.__init__)
    params = list(sig.parameters.keys())



def test_oclreference_is_not_abstract():
    assert not inspect.isabstract(OclReference)


def test_oclreference_constructor_exists():
    assert callable(OclReference.__init__)


def test_oclreference_constructor_args():
    sig = inspect.signature(OclReference.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclpathfeaturehead_is_not_abstract():
    assert not inspect.isabstract(umm_OclPathFeatureHead)


def test_umm_oclpathfeaturehead_constructor_exists():
    assert callable(umm_OclPathFeatureHead.__init__)


def test_umm_oclpathfeaturehead_constructor_args():
    sig = inspect.signature(umm_OclPathFeatureHead.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclpathselfhead_is_not_abstract():
    assert not inspect.isabstract(umm_OclPathSelfHead)


def test_umm_oclpathselfhead_constructor_exists():
    assert callable(umm_OclPathSelfHead.__init__)


def test_umm_oclpathselfhead_constructor_args():
    sig = inspect.signature(umm_OclPathSelfHead.__init__)
    params = list(sig.parameters.keys())



def test_oclvalue_is_not_abstract():
    assert not inspect.isabstract(OclValue)


def test_oclvalue_constructor_exists():
    assert callable(OclValue.__init__)


def test_oclvalue_constructor_args():
    sig = inspect.signature(OclValue.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclliteral_is_not_abstract():
    assert not inspect.isabstract(umm_OclLiteral)


def test_umm_oclliteral_constructor_exists():
    assert callable(umm_OclLiteral.__init__)


def test_umm_oclliteral_constructor_args():
    sig = inspect.signature(umm_OclLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclreference_is_not_abstract():
    assert not inspect.isabstract(umm_OclReference)


def test_umm_oclreference_constructor_exists():
    assert callable(umm_OclReference.__init__)


def test_umm_oclreference_constructor_args():
    sig = inspect.signature(umm_OclReference.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_umm_ocllessorequal_is_not_abstract():
    assert not inspect.isabstract(umm_OclLessOrEqual)


def test_umm_ocllessorequal_constructor_exists():
    assert callable(umm_OclLessOrEqual.__init__)


def test_umm_ocllessorequal_constructor_args():
    sig = inspect.signature(umm_OclLessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclor_is_not_abstract():
    assert not inspect.isabstract(umm_OclOr)


def test_umm_oclor_constructor_exists():
    assert callable(umm_OclOr.__init__)


def test_umm_oclor_constructor_args():
    sig = inspect.signature(umm_OclOr.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclmoreorequal_is_not_abstract():
    assert not inspect.isabstract(umm_OclMoreOrEqual)


def test_umm_oclmoreorequal_constructor_exists():
    assert callable(umm_OclMoreOrEqual.__init__)


def test_umm_oclmoreorequal_constructor_args():
    sig = inspect.signature(umm_OclMoreOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_umm_ocland_is_not_abstract():
    assert not inspect.isabstract(umm_OclAnd)


def test_umm_ocland_constructor_exists():
    assert callable(umm_OclAnd.__init__)


def test_umm_ocland_constructor_args():
    sig = inspect.signature(umm_OclAnd.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclmore_is_not_abstract():
    assert not inspect.isabstract(umm_OclMore)


def test_umm_oclmore_constructor_exists():
    assert callable(umm_OclMore.__init__)


def test_umm_oclmore_constructor_args():
    sig = inspect.signature(umm_OclMore.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclimplies_is_not_abstract():
    assert not inspect.isabstract(umm_OclImplies)


def test_umm_oclimplies_constructor_exists():
    assert callable(umm_OclImplies.__init__)


def test_umm_oclimplies_constructor_args():
    sig = inspect.signature(umm_OclImplies.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclequal_is_not_abstract():
    assert not inspect.isabstract(umm_OclEqual)


def test_umm_oclequal_constructor_exists():
    assert callable(umm_OclEqual.__init__)


def test_umm_oclequal_constructor_args():
    sig = inspect.signature(umm_OclEqual.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclxor_is_not_abstract():
    assert not inspect.isabstract(umm_OclXor)


def test_umm_oclxor_constructor_exists():
    assert callable(umm_OclXor.__init__)


def test_umm_oclxor_constructor_args():
    sig = inspect.signature(umm_OclXor.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclless_is_not_abstract():
    assert not inspect.isabstract(umm_OclLess)


def test_umm_oclless_constructor_exists():
    assert callable(umm_OclLess.__init__)


def test_umm_oclless_constructor_args():
    sig = inspect.signature(umm_OclLess.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclarrow_is_not_abstract():
    assert not inspect.isabstract(umm_OclArrow)


def test_umm_oclarrow_constructor_exists():
    assert callable(umm_OclArrow.__init__)


def test_umm_oclarrow_constructor_args():
    sig = inspect.signature(umm_OclArrow.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclvalue_is_not_abstract():
    assert not inspect.isabstract(umm_OclValue)


def test_umm_oclvalue_constructor_exists():
    assert callable(umm_OclValue.__init__)


def test_umm_oclvalue_constructor_args():
    sig = inspect.signature(umm_OclValue.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclexpression_is_not_abstract():
    assert not inspect.isabstract(umm_OclExpression)


def test_umm_oclexpression_constructor_exists():
    assert callable(umm_OclExpression.__init__)


def test_umm_oclexpression_constructor_args():
    sig = inspect.signature(umm_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_umm_cdt_is_not_abstract():
    assert not inspect.isabstract(umm_CDT)


def test_umm_cdt_constructor_exists():
    assert callable(umm_CDT.__init__)


def test_umm_cdt_constructor_args():
    sig = inspect.signature(umm_CDT.__init__)
    params = list(sig.parameters.keys())
    assert "definition" in params, "Missing parameter 'definition'"
    assert "name" in params, "Missing parameter 'name'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"

def test_umm_cdt_has_definition():
    assert hasattr(umm_CDT, "definition")
    descriptor = None
    for klass in umm_CDT.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_has_name():
    assert hasattr(umm_CDT, "name")
    descriptor = None
    for klass in umm_CDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_has_versionIdentifier():
    assert hasattr(umm_CDT, "versionIdentifier")
    descriptor = None
    for klass in umm_CDT.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_has_businessTerm():
    assert hasattr(umm_CDT, "businessTerm")
    descriptor = None
    for klass in umm_CDT.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_has_uniqueIdentifier():
    assert hasattr(umm_CDT, "uniqueIdentifier")
    descriptor = None
    for klass in umm_CDT.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdt_has_dictionary():
    assert hasattr(umm_CDT, "dictionary")
    descriptor = None
    for klass in umm_CDT.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)



def test_umm_codelistentry_is_not_abstract():
    assert not inspect.isabstract(umm_CodelistEntry)


def test_umm_codelistentry_constructor_exists():
    assert callable(umm_CodelistEntry.__init__)


def test_umm_codelistentry_constructor_args():
    sig = inspect.signature(umm_CodelistEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_umm_codelistentry_has_name():
    assert hasattr(umm_CodelistEntry, "name")
    descriptor = None
    for klass in umm_CodelistEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm_codelistentry_has_description():
    assert hasattr(umm_CodelistEntry, "description")
    descriptor = None
    for klass in umm_CodelistEntry.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_accproperty_is_not_abstract():
    assert not inspect.isabstract(ACCProperty)


def test_accproperty_constructor_exists():
    assert callable(ACCProperty.__init__)


def test_accproperty_constructor_args():
    sig = inspect.signature(ACCProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm_bcc_is_not_abstract():
    assert not inspect.isabstract(umm_BCC)


def test_umm_bcc_constructor_exists():
    assert callable(umm_BCC.__init__)


def test_umm_bcc_constructor_args():
    sig = inspect.signature(umm_BCC.__init__)
    params = list(sig.parameters.keys())
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"
    assert "restriction" in params, "Missing parameter 'restriction'"

def test_umm_bcc_has_fixedValue():
    assert hasattr(umm_BCC, "fixedValue")
    descriptor = None
    for klass in umm_BCC.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)

def test_umm_bcc_has_restriction():
    assert hasattr(umm_BCC, "restriction")
    descriptor = None
    for klass in umm_BCC.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)



def test_umm_ascc_is_not_abstract():
    assert not inspect.isabstract(umm_ASCC)


def test_umm_ascc_constructor_exists():
    assert callable(umm_ASCC.__init__)


def test_umm_ascc_constructor_args():
    sig = inspect.signature(umm_ASCC.__init__)
    params = list(sig.parameters.keys())



def test_umm_accproperty_is_not_abstract():
    assert not inspect.isabstract(umm_ACCProperty)


def test_umm_accproperty_constructor_exists():
    assert callable(umm_ACCProperty.__init__)


def test_umm_accproperty_constructor_args():
    sig = inspect.signature(umm_ACCProperty.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "sequencingKey" in params, "Missing parameter 'sequencingKey'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "name" in params, "Missing parameter 'name'"

def test_umm_accproperty_has_uniqueIdentifier():
    assert hasattr(umm_ACCProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_versionIdentifier():
    assert hasattr(umm_ACCProperty, "versionIdentifier")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_sequencingKey():
    assert hasattr(umm_ACCProperty, "sequencingKey")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "sequencingKey" in klass.__dict__:
            descriptor = klass.__dict__["sequencingKey"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_definition():
    assert hasattr(umm_ACCProperty, "definition")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_dictionary():
    assert hasattr(umm_ACCProperty, "dictionary")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_multiplicity():
    assert hasattr(umm_ACCProperty, "multiplicity")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_businessTerm():
    assert hasattr(umm_ACCProperty, "businessTerm")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_accproperty_has_name():
    assert hasattr(umm_ACCProperty, "name")
    descriptor = None
    for klass in umm_ACCProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm_acc_is_not_abstract():
    assert not inspect.isabstract(umm_ACC)


def test_umm_acc_constructor_exists():
    assert callable(umm_ACC.__init__)


def test_umm_acc_constructor_args():
    sig = inspect.signature(umm_ACC.__init__)
    params = list(sig.parameters.keys())
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"

def test_umm_acc_has_businessTerm():
    assert hasattr(umm_ACC, "businessTerm")
    descriptor = None
    for klass in umm_ACC.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_acc_has_definition():
    assert hasattr(umm_ACC, "definition")
    descriptor = None
    for klass in umm_ACC.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_acc_has_uniqueIdentifier():
    assert hasattr(umm_ACC, "uniqueIdentifier")
    descriptor = None
    for klass in umm_ACC.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_acc_has_name():
    assert hasattr(umm_ACC, "name")
    descriptor = None
    for klass in umm_ACC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm_acc_has_dictionary():
    assert hasattr(umm_ACC, "dictionary")
    descriptor = None
    for klass in umm_ACC.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_acc_has_versionIdentifier():
    assert hasattr(umm_ACC, "versionIdentifier")
    descriptor = None
    for klass in umm_ACC.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_bdtproperty_is_not_abstract():
    assert not inspect.isabstract(BDTProperty)


def test_bdtproperty_constructor_exists():
    assert callable(BDTProperty.__init__)


def test_bdtproperty_constructor_args():
    sig = inspect.signature(BDTProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm_supplement_is_not_abstract():
    assert not inspect.isabstract(umm_Supplement)


def test_umm_supplement_constructor_exists():
    assert callable(umm_Supplement.__init__)


def test_umm_supplement_constructor_args():
    sig = inspect.signature(umm_Supplement.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"
    assert "restriction" in params, "Missing parameter 'restriction'"

def test_umm_supplement_has_defaultValue():
    assert hasattr(umm_Supplement, "defaultValue")
    descriptor = None
    for klass in umm_Supplement.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_umm_supplement_has_fixedValue():
    assert hasattr(umm_Supplement, "fixedValue")
    descriptor = None
    for klass in umm_Supplement.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)

def test_umm_supplement_has_restriction():
    assert hasattr(umm_Supplement, "restriction")
    descriptor = None
    for klass in umm_Supplement.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)



def test_umm_content_is_not_abstract():
    assert not inspect.isabstract(umm_Content)


def test_umm_content_constructor_exists():
    assert callable(umm_Content.__init__)


def test_umm_content_constructor_args():
    sig = inspect.signature(umm_Content.__init__)
    params = list(sig.parameters.keys())
    assert "maxExclusive" in params, "Missing parameter 'maxExclusive'"
    assert "minExclusive" in params, "Missing parameter 'minExclusive'"
    assert "totalDigits" in params, "Missing parameter 'totalDigits'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "fractionalDigits" in params, "Missing parameter 'fractionalDigits'"

def test_umm_content_has_maxExclusive():
    assert hasattr(umm_Content, "maxExclusive")
    descriptor = None
    for klass in umm_Content.__mro__:
        if "maxExclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxExclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm_content_has_minExclusive():
    assert hasattr(umm_Content, "minExclusive")
    descriptor = None
    for klass in umm_Content.__mro__:
        if "minExclusive" in klass.__dict__:
            descriptor = klass.__dict__["minExclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm_content_has_totalDigits():
    assert hasattr(umm_Content, "totalDigits")
    descriptor = None
    for klass in umm_Content.__mro__:
        if "totalDigits" in klass.__dict__:
            descriptor = klass.__dict__["totalDigits"]
            break
    assert isinstance(descriptor, property)

def test_umm_content_has_maxInclusive():
    assert hasattr(umm_Content, "maxInclusive")
    descriptor = None
    for klass in umm_Content.__mro__:
        if "maxInclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxInclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm_content_has_minInclusive():
    assert hasattr(umm_Content, "minInclusive")
    descriptor = None
    for klass in umm_Content.__mro__:
        if "minInclusive" in klass.__dict__:
            descriptor = klass.__dict__["minInclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm_content_has_fractionalDigits():
    assert hasattr(umm_Content, "fractionalDigits")
    descriptor = None
    for klass in umm_Content.__mro__:
        if "fractionalDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionalDigits"]
            break
    assert isinstance(descriptor, property)



def test_assembledbase_is_not_abstract():
    assert not inspect.isabstract(AssembledBase)


def test_assembledbase_constructor_exists():
    assert callable(AssembledBase.__init__)


def test_assembledbase_constructor_args():
    sig = inspect.signature(AssembledBase.__init__)
    params = list(sig.parameters.keys())



def test_umm_assembled_is_not_abstract():
    assert not inspect.isabstract(umm_Assembled)


def test_umm_assembled_constructor_exists():
    assert callable(umm_Assembled.__init__)


def test_umm_assembled_constructor_args():
    sig = inspect.signature(umm_Assembled.__init__)
    params = list(sig.parameters.keys())



def test_umm_primitive_is_not_abstract():
    assert not inspect.isabstract(umm_Primitive)


def test_umm_primitive_constructor_exists():
    assert callable(umm_Primitive.__init__)


def test_umm_primitive_constructor_args():
    sig = inspect.signature(umm_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_enum_is_not_abstract():
    assert not inspect.isabstract(ENUM)


def test_enum_constructor_exists():
    assert callable(ENUM.__init__)


def test_enum_constructor_args():
    sig = inspect.signature(ENUM.__init__)
    params = list(sig.parameters.keys())



def test_umm_original_is_not_abstract():
    assert not inspect.isabstract(umm_Original)


def test_umm_original_constructor_exists():
    assert callable(umm_Original.__init__)


def test_umm_original_constructor_args():
    sig = inspect.signature(umm_Original.__init__)
    params = list(sig.parameters.keys())



def test_umm_subset_is_not_abstract():
    assert not inspect.isabstract(umm_Subset)


def test_umm_subset_constructor_exists():
    assert callable(umm_Subset.__init__)


def test_umm_subset_constructor_args():
    sig = inspect.signature(umm_Subset.__init__)
    params = list(sig.parameters.keys())



def test_umm_assembledbase_is_not_abstract():
    assert not inspect.isabstract(umm_AssembledBase)


def test_umm_assembledbase_constructor_exists():
    assert callable(umm_AssembledBase.__init__)


def test_umm_assembledbase_constructor_args():
    sig = inspect.signature(umm_AssembledBase.__init__)
    params = list(sig.parameters.keys())



def test_umm_enum_is_not_abstract():
    assert not inspect.isabstract(umm_ENUM)


def test_umm_enum_constructor_exists():
    assert callable(umm_ENUM.__init__)


def test_umm_enum_constructor_args():
    sig = inspect.signature(umm_ENUM.__init__)
    params = list(sig.parameters.keys())
    assert "codeListAgencyIdentifier" in params, "Missing parameter 'codeListAgencyIdentifier'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "codeListName" in params, "Missing parameter 'codeListName'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "codeListIdentifier" in params, "Missing parameter 'codeListIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_umm_enum_has_codeListAgencyIdentifier():
    assert hasattr(umm_ENUM, "codeListAgencyIdentifier")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "codeListAgencyIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["codeListAgencyIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_definition():
    assert hasattr(umm_ENUM, "definition")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_codeListName():
    assert hasattr(umm_ENUM, "codeListName")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "codeListName" in klass.__dict__:
            descriptor = klass.__dict__["codeListName"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_uniqueIdentifier():
    assert hasattr(umm_ENUM, "uniqueIdentifier")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_codeListIdentifier():
    assert hasattr(umm_ENUM, "codeListIdentifier")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "codeListIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["codeListIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_businessTerm():
    assert hasattr(umm_ENUM, "businessTerm")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_dictionary():
    assert hasattr(umm_ENUM, "dictionary")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_versionIdentifier():
    assert hasattr(umm_ENUM, "versionIdentifier")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_enum_has_name():
    assert hasattr(umm_ENUM, "name")
    descriptor = None
    for klass in umm_ENUM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abieproperty_is_not_abstract():
    assert not inspect.isabstract(ABIEProperty)


def test_abieproperty_constructor_exists():
    assert callable(ABIEProperty.__init__)


def test_abieproperty_constructor_args():
    sig = inspect.signature(ABIEProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm_bbie_is_not_abstract():
    assert not inspect.isabstract(umm_BBIE)


def test_umm_bbie_constructor_exists():
    assert callable(umm_BBIE.__init__)


def test_umm_bbie_constructor_args():
    sig = inspect.signature(umm_BBIE.__init__)
    params = list(sig.parameters.keys())
    assert "restriction" in params, "Missing parameter 'restriction'"
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"

def test_umm_bbie_has_restriction():
    assert hasattr(umm_BBIE, "restriction")
    descriptor = None
    for klass in umm_BBIE.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)

def test_umm_bbie_has_fixedValue():
    assert hasattr(umm_BBIE, "fixedValue")
    descriptor = None
    for klass in umm_BBIE.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)



def test_umm_asbie_is_not_abstract():
    assert not inspect.isabstract(umm_ASBIE)


def test_umm_asbie_constructor_exists():
    assert callable(umm_ASBIE.__init__)


def test_umm_asbie_constructor_args():
    sig = inspect.signature(umm_ASBIE.__init__)
    params = list(sig.parameters.keys())



def test_umm_oclinvariant_is_not_abstract():
    assert not inspect.isabstract(umm_OclInvariant)


def test_umm_oclinvariant_constructor_exists():
    assert callable(umm_OclInvariant.__init__)


def test_umm_oclinvariant_constructor_args():
    sig = inspect.signature(umm_OclInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umm_tc_constraint_is_not_abstract():
    assert not inspect.isabstract(umm_TC_Constraint)


def test_umm_tc_constraint_constructor_exists():
    assert callable(umm_TC_Constraint.__init__)


def test_umm_tc_constraint_constructor_args():
    sig = inspect.signature(umm_TC_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "listIdentifier" in params, "Missing parameter 'listIdentifier'"
    assert "responsibleAgency" in params, "Missing parameter 'responsibleAgency'"

def test_umm_tc_constraint_has_kind():
    assert hasattr(umm_TC_Constraint, "kind")
    descriptor = None
    for klass in umm_TC_Constraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umm_tc_constraint_has_listIdentifier():
    assert hasattr(umm_TC_Constraint, "listIdentifier")
    descriptor = None
    for klass in umm_TC_Constraint.__mro__:
        if "listIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["listIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_tc_constraint_has_responsibleAgency():
    assert hasattr(umm_TC_Constraint, "responsibleAgency")
    descriptor = None
    for klass in umm_TC_Constraint.__mro__:
        if "responsibleAgency" in klass.__dict__:
            descriptor = klass.__dict__["responsibleAgency"]
            break
    assert isinstance(descriptor, property)



def test_umm_contextref_is_not_abstract():
    assert not inspect.isabstract(umm_ContextRef)


def test_umm_contextref_constructor_exists():
    assert callable(umm_ContextRef.__init__)


def test_umm_contextref_constructor_args():
    sig = inspect.signature(umm_ContextRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umm_contextref_has_name():
    assert hasattr(umm_ContextRef, "name")
    descriptor = None
    for klass in umm_ContextRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maproperty_is_not_abstract():
    assert not inspect.isabstract(MAProperty)


def test_maproperty_constructor_exists():
    assert callable(MAProperty.__init__)


def test_maproperty_constructor_args():
    sig = inspect.signature(MAProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm_asnone_is_not_abstract():
    assert not inspect.isabstract(umm_ASNONE)


def test_umm_asnone_constructor_exists():
    assert callable(umm_ASNONE.__init__)


def test_umm_asnone_constructor_args():
    sig = inspect.signature(umm_ASNONE.__init__)
    params = list(sig.parameters.keys())



def test_umm_asma_is_not_abstract():
    assert not inspect.isabstract(umm_ASMA)


def test_umm_asma_constructor_exists():
    assert callable(umm_ASMA.__init__)


def test_umm_asma_constructor_args():
    sig = inspect.signature(umm_ASMA.__init__)
    params = list(sig.parameters.keys())



def test_oclref_is_not_abstract():
    assert not inspect.isabstract(OclRef)


def test_oclref_constructor_exists():
    assert callable(OclRef.__init__)


def test_oclref_constructor_args():
    sig = inspect.signature(OclRef.__init__)
    params = list(sig.parameters.keys())



def test_umm_bdtproperty_is_not_abstract():
    assert not inspect.isabstract(umm_BDTProperty)


def test_umm_bdtproperty_constructor_exists():
    assert callable(umm_BDTProperty.__init__)


def test_umm_bdtproperty_constructor_args():
    sig = inspect.signature(umm_BDTProperty.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "length" in params, "Missing parameter 'length'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "definition" in params, "Missing parameter 'definition'"

def test_umm_bdtproperty_has_maxLength():
    assert hasattr(umm_BDTProperty, "maxLength")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_dictionary():
    assert hasattr(umm_BDTProperty, "dictionary")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_length():
    assert hasattr(umm_BDTProperty, "length")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_versionIdentifier():
    assert hasattr(umm_BDTProperty, "versionIdentifier")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_businessTerm():
    assert hasattr(umm_BDTProperty, "businessTerm")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_minLength():
    assert hasattr(umm_BDTProperty, "minLength")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_uniqueIdentifier():
    assert hasattr(umm_BDTProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_pattern():
    assert hasattr(umm_BDTProperty, "pattern")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtproperty_has_definition():
    assert hasattr(umm_BDTProperty, "definition")
    descriptor = None
    for klass in umm_BDTProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)



def test_umm_abieproperty_is_not_abstract():
    assert not inspect.isabstract(umm_ABIEProperty)


def test_umm_abieproperty_constructor_exists():
    assert callable(umm_ABIEProperty.__init__)


def test_umm_abieproperty_constructor_args():
    sig = inspect.signature(umm_ABIEProperty.__init__)
    params = list(sig.parameters.keys())
    assert "definition" in params, "Missing parameter 'definition'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "sequencingKey" in params, "Missing parameter 'sequencingKey'"

def test_umm_abieproperty_has_definition():
    assert hasattr(umm_ABIEProperty, "definition")
    descriptor = None
    for klass in umm_ABIEProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_abieproperty_has_businessTerm():
    assert hasattr(umm_ABIEProperty, "businessTerm")
    descriptor = None
    for klass in umm_ABIEProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_abieproperty_has_dictionary():
    assert hasattr(umm_ABIEProperty, "dictionary")
    descriptor = None
    for klass in umm_ABIEProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_abieproperty_has_versionIdentifier():
    assert hasattr(umm_ABIEProperty, "versionIdentifier")
    descriptor = None
    for klass in umm_ABIEProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_abieproperty_has_uniqueIdentifier():
    assert hasattr(umm_ABIEProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm_ABIEProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_abieproperty_has_sequencingKey():
    assert hasattr(umm_ABIEProperty, "sequencingKey")
    descriptor = None
    for klass in umm_ABIEProperty.__mro__:
        if "sequencingKey" in klass.__dict__:
            descriptor = klass.__dict__["sequencingKey"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_umm_cclibrary_is_not_abstract():
    assert not inspect.isabstract(umm_CCLibrary)


def test_umm_cclibrary_constructor_exists():
    assert callable(umm_CCLibrary.__init__)


def test_umm_cclibrary_constructor_args():
    sig = inspect.signature(umm_CCLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm_cclibrary_has_baseURN():
    assert hasattr(umm_CCLibrary, "baseURN")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_namespacePrefix():
    assert hasattr(umm_CCLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_businessTerm():
    assert hasattr(umm_CCLibrary, "businessTerm")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_reference():
    assert hasattr(umm_CCLibrary, "reference")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_versionIdentifier():
    assert hasattr(umm_CCLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_copyright():
    assert hasattr(umm_CCLibrary, "copyright")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_owner():
    assert hasattr(umm_CCLibrary, "owner")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm_cclibrary_has_uniqueIdentifier():
    assert hasattr(umm_CCLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm_CCLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm_cdtlibrary_is_not_abstract():
    assert not inspect.isabstract(umm_CDTLibrary)


def test_umm_cdtlibrary_constructor_exists():
    assert callable(umm_CDTLibrary.__init__)


def test_umm_cdtlibrary_constructor_args():
    sig = inspect.signature(umm_CDTLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm_cdtlibrary_has_versionIdentifier():
    assert hasattr(umm_CDTLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_namespacePrefix():
    assert hasattr(umm_CDTLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_copyright():
    assert hasattr(umm_CDTLibrary, "copyright")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_reference():
    assert hasattr(umm_CDTLibrary, "reference")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_businessTerm():
    assert hasattr(umm_CDTLibrary, "businessTerm")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_baseURN():
    assert hasattr(umm_CDTLibrary, "baseURN")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_owner():
    assert hasattr(umm_CDTLibrary, "owner")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm_cdtlibrary_has_uniqueIdentifier():
    assert hasattr(umm_CDTLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm_CDTLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm_primitivelibrary_is_not_abstract():
    assert not inspect.isabstract(umm_PrimitiveLibrary)


def test_umm_primitivelibrary_constructor_exists():
    assert callable(umm_PrimitiveLibrary.__init__)


def test_umm_primitivelibrary_constructor_args():
    sig = inspect.signature(umm_PrimitiveLibrary.__init__)
    params = list(sig.parameters.keys())



def test_umm_enumlibrary_is_not_abstract():
    assert not inspect.isabstract(umm_ENUMLibrary)


def test_umm_enumlibrary_constructor_exists():
    assert callable(umm_ENUMLibrary.__init__)


def test_umm_enumlibrary_constructor_args():
    sig = inspect.signature(umm_ENUMLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "copyright" in params, "Missing parameter 'copyright'"

def test_umm_enumlibrary_has_reference():
    assert hasattr(umm_ENUMLibrary, "reference")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_baseURN():
    assert hasattr(umm_ENUMLibrary, "baseURN")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_namespacePrefix():
    assert hasattr(umm_ENUMLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_versionIdentifier():
    assert hasattr(umm_ENUMLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_businessTerm():
    assert hasattr(umm_ENUMLibrary, "businessTerm")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_uniqueIdentifier():
    assert hasattr(umm_ENUMLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_owner():
    assert hasattr(umm_ENUMLibrary, "owner")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm_enumlibrary_has_copyright():
    assert hasattr(umm_ENUMLibrary, "copyright")
    descriptor = None
    for klass in umm_ENUMLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)



def test_umm_doclibrary_is_not_abstract():
    assert not inspect.isabstract(umm_DocLibrary)


def test_umm_doclibrary_constructor_exists():
    assert callable(umm_DocLibrary.__init__)


def test_umm_doclibrary_constructor_args():
    sig = inspect.signature(umm_DocLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"

def test_umm_doclibrary_has_versionIdentifier():
    assert hasattr(umm_DocLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_reference():
    assert hasattr(umm_DocLibrary, "reference")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_owner():
    assert hasattr(umm_DocLibrary, "owner")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_copyright():
    assert hasattr(umm_DocLibrary, "copyright")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_baseURN():
    assert hasattr(umm_DocLibrary, "baseURN")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_namespacePrefix():
    assert hasattr(umm_DocLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_uniqueIdentifier():
    assert hasattr(umm_DocLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_doclibrary_has_businessTerm():
    assert hasattr(umm_DocLibrary, "businessTerm")
    descriptor = None
    for klass in umm_DocLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)



def test_umm_library_is_not_abstract():
    assert not inspect.isabstract(umm_Library)


def test_umm_library_constructor_exists():
    assert callable(umm_Library.__init__)


def test_umm_library_constructor_args():
    sig = inspect.signature(umm_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umm_library_has_name():
    assert hasattr(umm_Library, "name")
    descriptor = None
    for klass in umm_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm_constraint_is_not_abstract():
    assert not inspect.isabstract(umm_Constraint)


def test_umm_constraint_constructor_exists():
    assert callable(umm_Constraint.__init__)


def test_umm_constraint_constructor_args():
    sig = inspect.signature(umm_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_umm_maproperty_is_not_abstract():
    assert not inspect.isabstract(umm_MAProperty)


def test_umm_maproperty_constructor_exists():
    assert callable(umm_MAProperty.__init__)


def test_umm_maproperty_constructor_args():
    sig = inspect.signature(umm_MAProperty.__init__)
    params = list(sig.parameters.keys())



def test_contextref_is_not_abstract():
    assert not inspect.isabstract(ContextRef)


def test_contextref_constructor_exists():
    assert callable(ContextRef.__init__)


def test_contextref_constructor_args():
    sig = inspect.signature(ContextRef.__init__)
    params = list(sig.parameters.keys())



def test_umm_abie_is_not_abstract():
    assert not inspect.isabstract(umm_ABIE)


def test_umm_abie_constructor_exists():
    assert callable(umm_ABIE.__init__)


def test_umm_abie_constructor_args():
    sig = inspect.signature(umm_ABIE.__init__)
    params = list(sig.parameters.keys())
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "definition" in params, "Missing parameter 'definition'"

def test_umm_abie_has_dictionary():
    assert hasattr(umm_ABIE, "dictionary")
    descriptor = None
    for klass in umm_ABIE.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_abie_has_versionIdentifier():
    assert hasattr(umm_ABIE, "versionIdentifier")
    descriptor = None
    for klass in umm_ABIE.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_abie_has_businessTerm():
    assert hasattr(umm_ABIE, "businessTerm")
    descriptor = None
    for klass in umm_ABIE.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_abie_has_uniqueIdentifier():
    assert hasattr(umm_ABIE, "uniqueIdentifier")
    descriptor = None
    for klass in umm_ABIE.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_abie_has_definition():
    assert hasattr(umm_ABIE, "definition")
    descriptor = None
    for klass in umm_ABIE.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)



def test_umm_bdt_is_not_abstract():
    assert not inspect.isabstract(umm_BDT)


def test_umm_bdt_constructor_exists():
    assert callable(umm_BDT.__init__)


def test_umm_bdt_constructor_args():
    sig = inspect.signature(umm_BDT.__init__)
    params = list(sig.parameters.keys())
    assert "definition" in params, "Missing parameter 'definition'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm_bdt_has_definition():
    assert hasattr(umm_BDT, "definition")
    descriptor = None
    for klass in umm_BDT.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdt_has_businessTerm():
    assert hasattr(umm_BDT, "businessTerm")
    descriptor = None
    for klass in umm_BDT.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdt_has_versionIdentifier():
    assert hasattr(umm_BDT, "versionIdentifier")
    descriptor = None
    for klass in umm_BDT.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdt_has_dictionary():
    assert hasattr(umm_BDT, "dictionary")
    descriptor = None
    for klass in umm_BDT.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdt_has_uniqueIdentifier():
    assert hasattr(umm_BDT, "uniqueIdentifier")
    descriptor = None
    for klass in umm_BDT.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm_ma_is_not_abstract():
    assert not inspect.isabstract(umm_MA)


def test_umm_ma_constructor_exists():
    assert callable(umm_MA.__init__)


def test_umm_ma_constructor_args():
    sig = inspect.signature(umm_MA.__init__)
    params = list(sig.parameters.keys())



def test_umm_infenvelope_is_not_abstract():
    assert not inspect.isabstract(umm_InfEnvelope)


def test_umm_infenvelope_constructor_exists():
    assert callable(umm_InfEnvelope.__init__)


def test_umm_infenvelope_constructor_args():
    sig = inspect.signature(umm_InfEnvelope.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umm_infenvelope_has_name():
    assert hasattr(umm_InfEnvelope, "name")
    descriptor = None
    for klass in umm_InfEnvelope.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm_bdtlibrary_is_not_abstract():
    assert not inspect.isabstract(umm_BDTLibrary)


def test_umm_bdtlibrary_constructor_exists():
    assert callable(umm_BDTLibrary.__init__)


def test_umm_bdtlibrary_constructor_args():
    sig = inspect.signature(umm_BDTLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"

def test_umm_bdtlibrary_has_baseURN():
    assert hasattr(umm_BDTLibrary, "baseURN")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_uniqueIdentifier():
    assert hasattr(umm_BDTLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_namespacePrefix():
    assert hasattr(umm_BDTLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_businessTerm():
    assert hasattr(umm_BDTLibrary, "businessTerm")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_reference():
    assert hasattr(umm_BDTLibrary, "reference")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_copyright():
    assert hasattr(umm_BDTLibrary, "copyright")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_owner():
    assert hasattr(umm_BDTLibrary, "owner")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm_bdtlibrary_has_versionIdentifier():
    assert hasattr(umm_BDTLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm_BDTLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm_bielibrary_is_not_abstract():
    assert not inspect.isabstract(umm_BIELibrary)


def test_umm_bielibrary_constructor_exists():
    assert callable(umm_BIELibrary.__init__)


def test_umm_bielibrary_constructor_args():
    sig = inspect.signature(umm_BIELibrary.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_umm_bielibrary_has_owner():
    assert hasattr(umm_BIELibrary, "owner")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_businessTerm():
    assert hasattr(umm_BIELibrary, "businessTerm")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_namespacePrefix():
    assert hasattr(umm_BIELibrary, "namespacePrefix")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_copyright():
    assert hasattr(umm_BIELibrary, "copyright")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_baseURN():
    assert hasattr(umm_BIELibrary, "baseURN")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_versionIdentifier():
    assert hasattr(umm_BIELibrary, "versionIdentifier")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_uniqueIdentifier():
    assert hasattr(umm_BIELibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm_bielibrary_has_reference():
    assert hasattr(umm_BIELibrary, "reference")
    descriptor = None
    for klass in umm_BIELibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_constraintkind_exists():
    # Check that the Enumeration exists
    assert ConstraintKind is not None

def test_constraintkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintKind]
    expected_literals = [
        "invariant",
        "facet",
        "abie",
        "bdt",
        "dependency",
        "document",
        "payload",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintKind"

def test_multiplicitykind_exists():
    # Check that the Enumeration exists
    assert MultiplicityKind is not None

def test_multiplicitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicityKind]
    expected_literals = [
        "Optional",
        "OneOrMore",
        "ZeroOrMore",
        "One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicityKind"


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
OclLiteral_strategy = st.builds(
    OclLiteral,
)
umm_OclIntegerLiteral_strategy = st.builds(
    umm_OclIntegerLiteral,
    value=
        st.integers()
)
umm_OclBooleanLiteral_strategy = st.builds(
    umm_OclBooleanLiteral,
)
umm_OclStringLiteral_strategy = st.builds(
    umm_OclStringLiteral,
    value=
        safe_text
)
umm_OclEnumerationLiteral_strategy = st.builds(
    umm_OclEnumerationLiteral,
    value=
        safe_text
)
OclFunctionCall_strategy = st.builds(
    OclFunctionCall,
)
umm_OclIsEmpty_strategy = st.builds(
    umm_OclIsEmpty,
)
umm_OclNotEmpty_strategy = st.builds(
    umm_OclNotEmpty,
)
umm_OclSize_strategy = st.builds(
    umm_OclSize,
)
umm_OclForAll_strategy = st.builds(
    umm_OclForAll,
)
umm_OclFunctionCall_strategy = st.builds(
    umm_OclFunctionCall,
)
OclBooleanLiteral_strategy = st.builds(
    OclBooleanLiteral,
)
umm_OclBooleanTrue_strategy = st.builds(
    umm_OclBooleanTrue,
)
umm_OclBooleanFalse_strategy = st.builds(
    umm_OclBooleanFalse,
)
CDTProperty_strategy = st.builds(
    CDTProperty,
)
umm_CDT_Supplement_strategy = st.builds(
    umm_CDT_Supplement,
    fixedValue=
        safe_text,
    restriction=
        safe_text,
    defaultValue=
        safe_text
)
umm_CDT_Content_strategy = st.builds(
    umm_CDT_Content,
)
umm_CDTProperty_strategy = st.builds(
    umm_CDTProperty,
    multiplicity=
        safe_text,
    name=
        safe_text,
    dictionary=
        safe_text,
    versionIdentifier=
        safe_text,
    definition=
        safe_text,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text
)
umm_OclRef_strategy = st.builds(
    umm_OclRef,
    multiplicity=
        safe_text,
    name=
        safe_text
)
umm_OclPathTail_strategy = st.builds(
    umm_OclPathTail,
)
OclReference_strategy = st.builds(
    OclReference,
)
umm_OclPathFeatureHead_strategy = st.builds(
    umm_OclPathFeatureHead,
)
umm_OclPathSelfHead_strategy = st.builds(
    umm_OclPathSelfHead,
)
OclValue_strategy = st.builds(
    OclValue,
)
umm_OclLiteral_strategy = st.builds(
    umm_OclLiteral,
)
umm_OclReference_strategy = st.builds(
    umm_OclReference,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
umm_OclLessOrEqual_strategy = st.builds(
    umm_OclLessOrEqual,
)
umm_OclOr_strategy = st.builds(
    umm_OclOr,
)
umm_OclMoreOrEqual_strategy = st.builds(
    umm_OclMoreOrEqual,
)
umm_OclAnd_strategy = st.builds(
    umm_OclAnd,
)
umm_OclMore_strategy = st.builds(
    umm_OclMore,
)
umm_OclImplies_strategy = st.builds(
    umm_OclImplies,
)
umm_OclEqual_strategy = st.builds(
    umm_OclEqual,
)
umm_OclXor_strategy = st.builds(
    umm_OclXor,
)
umm_OclLess_strategy = st.builds(
    umm_OclLess,
)
umm_OclArrow_strategy = st.builds(
    umm_OclArrow,
)
umm_OclValue_strategy = st.builds(
    umm_OclValue,
)
umm_OclExpression_strategy = st.builds(
    umm_OclExpression,
)
umm_CDT_strategy = st.builds(
    umm_CDT,
    definition=
        safe_text,
    name=
        safe_text,
    versionIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    uniqueIdentifier=
        safe_text,
    dictionary=
        safe_text
)
umm_CodelistEntry_strategy = st.builds(
    umm_CodelistEntry,
    name=
        safe_text,
    description=
        safe_text
)
ACCProperty_strategy = st.builds(
    ACCProperty,
)
umm_BCC_strategy = st.builds(
    umm_BCC,
    fixedValue=
        safe_text,
    restriction=
        safe_text
)
umm_ASCC_strategy = st.builds(
    umm_ASCC,
)
umm_ACCProperty_strategy = st.builds(
    umm_ACCProperty,
    uniqueIdentifier=
        safe_text,
    versionIdentifier=
        safe_text,
    sequencingKey=
        safe_text,
    definition=
        safe_text,
    dictionary=
        safe_text,
    multiplicity=
        safe_text,
    businessTerm=
        safe_text,
    name=
        safe_text
)
umm_ACC_strategy = st.builds(
    umm_ACC,
    businessTerm=
        safe_text,
    definition=
        safe_text,
    uniqueIdentifier=
        safe_text,
    name=
        safe_text,
    dictionary=
        safe_text,
    versionIdentifier=
        safe_text
)
BDTProperty_strategy = st.builds(
    BDTProperty,
)
umm_Supplement_strategy = st.builds(
    umm_Supplement,
    defaultValue=
        safe_text,
    fixedValue=
        safe_text,
    restriction=
        safe_text
)
umm_Content_strategy = st.builds(
    umm_Content,
    maxExclusive=
        st.integers(),
    minExclusive=
        st.integers(),
    totalDigits=
        st.integers(),
    maxInclusive=
        st.integers(),
    minInclusive=
        st.integers(),
    fractionalDigits=
        st.integers()
)
AssembledBase_strategy = st.builds(
    AssembledBase,
)
umm_Assembled_strategy = st.builds(
    umm_Assembled,
)
umm_Primitive_strategy = st.builds(
    umm_Primitive,
)
ENUM_strategy = st.builds(
    ENUM,
)
umm_Original_strategy = st.builds(
    umm_Original,
)
umm_Subset_strategy = st.builds(
    umm_Subset,
)
umm_AssembledBase_strategy = st.builds(
    umm_AssembledBase,
)
umm_ENUM_strategy = st.builds(
    umm_ENUM,
    codeListAgencyIdentifier=
        safe_text,
    definition=
        safe_text,
    codeListName=
        safe_text,
    uniqueIdentifier=
        safe_text,
    codeListIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    dictionary=
        safe_text,
    versionIdentifier=
        safe_text,
    name=
        safe_text
)
ABIEProperty_strategy = st.builds(
    ABIEProperty,
)
umm_BBIE_strategy = st.builds(
    umm_BBIE,
    restriction=
        safe_text,
    fixedValue=
        safe_text
)
umm_ASBIE_strategy = st.builds(
    umm_ASBIE,
)
umm_OclInvariant_strategy = st.builds(
    umm_OclInvariant,
)
umm_TC_Constraint_strategy = st.builds(
    umm_TC_Constraint,
    kind=
        safe_text,
    listIdentifier=
        safe_text,
    responsibleAgency=
        safe_text
)
umm_ContextRef_strategy = st.builds(
    umm_ContextRef,
    name=
        safe_text
)
MAProperty_strategy = st.builds(
    MAProperty,
)
umm_ASNONE_strategy = st.builds(
    umm_ASNONE,
)
umm_ASMA_strategy = st.builds(
    umm_ASMA,
)
OclRef_strategy = st.builds(
    OclRef,
)
umm_BDTProperty_strategy = st.builds(
    umm_BDTProperty,
    maxLength=
        st.integers(),
    dictionary=
        safe_text,
    length=
        st.integers(),
    versionIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    minLength=
        st.integers(),
    uniqueIdentifier=
        safe_text,
    pattern=
        safe_text,
    definition=
        safe_text
)
umm_ABIEProperty_strategy = st.builds(
    umm_ABIEProperty,
    definition=
        safe_text,
    businessTerm=
        safe_text,
    dictionary=
        safe_text,
    versionIdentifier=
        safe_text,
    uniqueIdentifier=
        safe_text,
    sequencingKey=
        safe_text
)
Library_strategy = st.builds(
    Library,
)
umm_CCLibrary_strategy = st.builds(
    umm_CCLibrary,
    baseURN=
        safe_text,
    namespacePrefix=
        safe_text,
    businessTerm=
        safe_text,
    reference=
        safe_text,
    versionIdentifier=
        safe_text,
    copyright=
        safe_text,
    owner=
        safe_text,
    uniqueIdentifier=
        safe_text
)
umm_CDTLibrary_strategy = st.builds(
    umm_CDTLibrary,
    versionIdentifier=
        safe_text,
    namespacePrefix=
        safe_text,
    copyright=
        safe_text,
    reference=
        safe_text,
    businessTerm=
        safe_text,
    baseURN=
        safe_text,
    owner=
        safe_text,
    uniqueIdentifier=
        safe_text
)
umm_PrimitiveLibrary_strategy = st.builds(
    umm_PrimitiveLibrary,
)
umm_ENUMLibrary_strategy = st.builds(
    umm_ENUMLibrary,
    reference=
        safe_text,
    baseURN=
        safe_text,
    namespacePrefix=
        safe_text,
    versionIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    uniqueIdentifier=
        safe_text,
    owner=
        safe_text,
    copyright=
        safe_text
)
umm_DocLibrary_strategy = st.builds(
    umm_DocLibrary,
    versionIdentifier=
        safe_text,
    reference=
        safe_text,
    owner=
        safe_text,
    copyright=
        safe_text,
    baseURN=
        safe_text,
    namespacePrefix=
        safe_text,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text
)
umm_Library_strategy = st.builds(
    umm_Library,
    name=
        safe_text
)
umm_Constraint_strategy = st.builds(
    umm_Constraint,
)
umm_MAProperty_strategy = st.builds(
    umm_MAProperty,
)
ContextRef_strategy = st.builds(
    ContextRef,
)
umm_ABIE_strategy = st.builds(
    umm_ABIE,
    dictionary=
        safe_text,
    versionIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    uniqueIdentifier=
        safe_text,
    definition=
        safe_text
)
umm_BDT_strategy = st.builds(
    umm_BDT,
    definition=
        safe_text,
    businessTerm=
        safe_text,
    versionIdentifier=
        safe_text,
    dictionary=
        safe_text,
    uniqueIdentifier=
        safe_text
)
umm_MA_strategy = st.builds(
    umm_MA,
)
umm_InfEnvelope_strategy = st.builds(
    umm_InfEnvelope,
    name=
        safe_text
)
umm_BDTLibrary_strategy = st.builds(
    umm_BDTLibrary,
    baseURN=
        safe_text,
    uniqueIdentifier=
        safe_text,
    namespacePrefix=
        safe_text,
    businessTerm=
        safe_text,
    reference=
        safe_text,
    copyright=
        safe_text,
    owner=
        safe_text,
    versionIdentifier=
        safe_text
)
umm_BIELibrary_strategy = st.builds(
    umm_BIELibrary,
    owner=
        safe_text,
    businessTerm=
        safe_text,
    namespacePrefix=
        safe_text,
    copyright=
        safe_text,
    baseURN=
        safe_text,
    versionIdentifier=
        safe_text,
    uniqueIdentifier=
        safe_text,
    reference=
        safe_text
)

@given(instance=OclLiteral_strategy)
@settings(max_examples=50)
def test_oclliteral_instantiation(instance):
    assert isinstance(instance, OclLiteral)

@given(instance=umm_OclIntegerLiteral_strategy)
@settings(max_examples=50)
def test_umm_oclintegerliteral_instantiation(instance):
    assert isinstance(instance, umm_OclIntegerLiteral)



@given(instance=umm_OclIntegerLiteral_strategy)
def test_umm_oclintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=umm_OclBooleanLiteral_strategy)
@settings(max_examples=50)
def test_umm_oclbooleanliteral_instantiation(instance):
    assert isinstance(instance, umm_OclBooleanLiteral)

@given(instance=umm_OclStringLiteral_strategy)
@settings(max_examples=50)
def test_umm_oclstringliteral_instantiation(instance):
    assert isinstance(instance, umm_OclStringLiteral)



@given(instance=umm_OclStringLiteral_strategy)
def test_umm_oclstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=umm_OclEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umm_oclenumerationliteral_instantiation(instance):
    assert isinstance(instance, umm_OclEnumerationLiteral)



@given(instance=umm_OclEnumerationLiteral_strategy)
def test_umm_oclenumerationliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OclFunctionCall_strategy)
@settings(max_examples=50)
def test_oclfunctioncall_instantiation(instance):
    assert isinstance(instance, OclFunctionCall)

@given(instance=umm_OclIsEmpty_strategy)
@settings(max_examples=50)
def test_umm_oclisempty_instantiation(instance):
    assert isinstance(instance, umm_OclIsEmpty)

@given(instance=umm_OclNotEmpty_strategy)
@settings(max_examples=50)
def test_umm_oclnotempty_instantiation(instance):
    assert isinstance(instance, umm_OclNotEmpty)

@given(instance=umm_OclSize_strategy)
@settings(max_examples=50)
def test_umm_oclsize_instantiation(instance):
    assert isinstance(instance, umm_OclSize)

@given(instance=umm_OclForAll_strategy)
@settings(max_examples=50)
def test_umm_oclforall_instantiation(instance):
    assert isinstance(instance, umm_OclForAll)

@given(instance=umm_OclFunctionCall_strategy)
@settings(max_examples=50)
def test_umm_oclfunctioncall_instantiation(instance):
    assert isinstance(instance, umm_OclFunctionCall)

@given(instance=OclBooleanLiteral_strategy)
@settings(max_examples=50)
def test_oclbooleanliteral_instantiation(instance):
    assert isinstance(instance, OclBooleanLiteral)

@given(instance=umm_OclBooleanTrue_strategy)
@settings(max_examples=50)
def test_umm_oclbooleantrue_instantiation(instance):
    assert isinstance(instance, umm_OclBooleanTrue)

@given(instance=umm_OclBooleanFalse_strategy)
@settings(max_examples=50)
def test_umm_oclbooleanfalse_instantiation(instance):
    assert isinstance(instance, umm_OclBooleanFalse)

@given(instance=CDTProperty_strategy)
@settings(max_examples=50)
def test_cdtproperty_instantiation(instance):
    assert isinstance(instance, CDTProperty)

@given(instance=umm_CDT_Supplement_strategy)
@settings(max_examples=50)
def test_umm_cdt_supplement_instantiation(instance):
    assert isinstance(instance, umm_CDT_Supplement)



@given(instance=umm_CDT_Supplement_strategy)
def test_umm_cdt_supplement_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original



@given(instance=umm_CDT_Supplement_strategy)
def test_umm_cdt_supplement_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original



@given(instance=umm_CDT_Supplement_strategy)
def test_umm_cdt_supplement_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=umm_CDT_Content_strategy)
@settings(max_examples=50)
def test_umm_cdt_content_instantiation(instance):
    assert isinstance(instance, umm_CDT_Content)

@given(instance=umm_CDTProperty_strategy)
@settings(max_examples=50)
def test_umm_cdtproperty_instantiation(instance):
    assert isinstance(instance, umm_CDTProperty)



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_CDTProperty_strategy)
def test_umm_cdtproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm_OclRef_strategy)
@settings(max_examples=50)
def test_umm_oclref_instantiation(instance):
    assert isinstance(instance, umm_OclRef)



@given(instance=umm_OclRef_strategy)
def test_umm_oclref_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original



@given(instance=umm_OclRef_strategy)
def test_umm_oclref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm_OclPathTail_strategy)
@settings(max_examples=50)
def test_umm_oclpathtail_instantiation(instance):
    assert isinstance(instance, umm_OclPathTail)

@given(instance=OclReference_strategy)
@settings(max_examples=50)
def test_oclreference_instantiation(instance):
    assert isinstance(instance, OclReference)

@given(instance=umm_OclPathFeatureHead_strategy)
@settings(max_examples=50)
def test_umm_oclpathfeaturehead_instantiation(instance):
    assert isinstance(instance, umm_OclPathFeatureHead)

@given(instance=umm_OclPathSelfHead_strategy)
@settings(max_examples=50)
def test_umm_oclpathselfhead_instantiation(instance):
    assert isinstance(instance, umm_OclPathSelfHead)

@given(instance=OclValue_strategy)
@settings(max_examples=50)
def test_oclvalue_instantiation(instance):
    assert isinstance(instance, OclValue)

@given(instance=umm_OclLiteral_strategy)
@settings(max_examples=50)
def test_umm_oclliteral_instantiation(instance):
    assert isinstance(instance, umm_OclLiteral)

@given(instance=umm_OclReference_strategy)
@settings(max_examples=50)
def test_umm_oclreference_instantiation(instance):
    assert isinstance(instance, umm_OclReference)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=umm_OclLessOrEqual_strategy)
@settings(max_examples=50)
def test_umm_ocllessorequal_instantiation(instance):
    assert isinstance(instance, umm_OclLessOrEqual)

@given(instance=umm_OclOr_strategy)
@settings(max_examples=50)
def test_umm_oclor_instantiation(instance):
    assert isinstance(instance, umm_OclOr)

@given(instance=umm_OclMoreOrEqual_strategy)
@settings(max_examples=50)
def test_umm_oclmoreorequal_instantiation(instance):
    assert isinstance(instance, umm_OclMoreOrEqual)

@given(instance=umm_OclAnd_strategy)
@settings(max_examples=50)
def test_umm_ocland_instantiation(instance):
    assert isinstance(instance, umm_OclAnd)

@given(instance=umm_OclMore_strategy)
@settings(max_examples=50)
def test_umm_oclmore_instantiation(instance):
    assert isinstance(instance, umm_OclMore)

@given(instance=umm_OclImplies_strategy)
@settings(max_examples=50)
def test_umm_oclimplies_instantiation(instance):
    assert isinstance(instance, umm_OclImplies)

@given(instance=umm_OclEqual_strategy)
@settings(max_examples=50)
def test_umm_oclequal_instantiation(instance):
    assert isinstance(instance, umm_OclEqual)

@given(instance=umm_OclXor_strategy)
@settings(max_examples=50)
def test_umm_oclxor_instantiation(instance):
    assert isinstance(instance, umm_OclXor)

@given(instance=umm_OclLess_strategy)
@settings(max_examples=50)
def test_umm_oclless_instantiation(instance):
    assert isinstance(instance, umm_OclLess)

@given(instance=umm_OclArrow_strategy)
@settings(max_examples=50)
def test_umm_oclarrow_instantiation(instance):
    assert isinstance(instance, umm_OclArrow)

@given(instance=umm_OclValue_strategy)
@settings(max_examples=50)
def test_umm_oclvalue_instantiation(instance):
    assert isinstance(instance, umm_OclValue)

@given(instance=umm_OclExpression_strategy)
@settings(max_examples=50)
def test_umm_oclexpression_instantiation(instance):
    assert isinstance(instance, umm_OclExpression)

@given(instance=umm_CDT_strategy)
@settings(max_examples=50)
def test_umm_cdt_instantiation(instance):
    assert isinstance(instance, umm_CDT)



@given(instance=umm_CDT_strategy)
def test_umm_cdt_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_CDT_strategy)
def test_umm_cdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=umm_CDT_strategy)
def test_umm_cdt_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_CDT_strategy)
def test_umm_cdt_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_CDT_strategy)
def test_umm_cdt_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_CDT_strategy)
def test_umm_cdt_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm_CodelistEntry_strategy)
@settings(max_examples=50)
def test_umm_codelistentry_instantiation(instance):
    assert isinstance(instance, umm_CodelistEntry)



@given(instance=umm_CodelistEntry_strategy)
def test_umm_codelistentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=umm_CodelistEntry_strategy)
def test_umm_codelistentry_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ACCProperty_strategy)
@settings(max_examples=50)
def test_accproperty_instantiation(instance):
    assert isinstance(instance, ACCProperty)

@given(instance=umm_BCC_strategy)
@settings(max_examples=50)
def test_umm_bcc_instantiation(instance):
    assert isinstance(instance, umm_BCC)



@given(instance=umm_BCC_strategy)
def test_umm_bcc_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original



@given(instance=umm_BCC_strategy)
def test_umm_bcc_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=umm_ASCC_strategy)
@settings(max_examples=50)
def test_umm_ascc_instantiation(instance):
    assert isinstance(instance, umm_ASCC)

@given(instance=umm_ACCProperty_strategy)
@settings(max_examples=50)
def test_umm_accproperty_instantiation(instance):
    assert isinstance(instance, umm_ACCProperty)



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_sequencingKey_setter(instance):
    original = instance.sequencingKey
    instance.sequencingKey = original
    assert instance.sequencingKey == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_ACCProperty_strategy)
def test_umm_accproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm_ACC_strategy)
@settings(max_examples=50)
def test_umm_acc_instantiation(instance):
    assert isinstance(instance, umm_ACC)



@given(instance=umm_ACC_strategy)
def test_umm_acc_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_ACC_strategy)
def test_umm_acc_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_ACC_strategy)
def test_umm_acc_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_ACC_strategy)
def test_umm_acc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=umm_ACC_strategy)
def test_umm_acc_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_ACC_strategy)
def test_umm_acc_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=BDTProperty_strategy)
@settings(max_examples=50)
def test_bdtproperty_instantiation(instance):
    assert isinstance(instance, BDTProperty)

@given(instance=umm_Supplement_strategy)
@settings(max_examples=50)
def test_umm_supplement_instantiation(instance):
    assert isinstance(instance, umm_Supplement)



@given(instance=umm_Supplement_strategy)
def test_umm_supplement_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=umm_Supplement_strategy)
def test_umm_supplement_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original



@given(instance=umm_Supplement_strategy)
def test_umm_supplement_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=umm_Content_strategy)
@settings(max_examples=50)
def test_umm_content_instantiation(instance):
    assert isinstance(instance, umm_Content)



@given(instance=umm_Content_strategy)
def test_umm_content_maxExclusive_setter(instance):
    original = instance.maxExclusive
    instance.maxExclusive = original
    assert instance.maxExclusive == original



@given(instance=umm_Content_strategy)
def test_umm_content_minExclusive_setter(instance):
    original = instance.minExclusive
    instance.minExclusive = original
    assert instance.minExclusive == original



@given(instance=umm_Content_strategy)
def test_umm_content_totalDigits_setter(instance):
    original = instance.totalDigits
    instance.totalDigits = original
    assert instance.totalDigits == original



@given(instance=umm_Content_strategy)
def test_umm_content_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original



@given(instance=umm_Content_strategy)
def test_umm_content_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original



@given(instance=umm_Content_strategy)
def test_umm_content_fractionalDigits_setter(instance):
    original = instance.fractionalDigits
    instance.fractionalDigits = original
    assert instance.fractionalDigits == original

@given(instance=AssembledBase_strategy)
@settings(max_examples=50)
def test_assembledbase_instantiation(instance):
    assert isinstance(instance, AssembledBase)

@given(instance=umm_Assembled_strategy)
@settings(max_examples=50)
def test_umm_assembled_instantiation(instance):
    assert isinstance(instance, umm_Assembled)

@given(instance=umm_Primitive_strategy)
@settings(max_examples=50)
def test_umm_primitive_instantiation(instance):
    assert isinstance(instance, umm_Primitive)

@given(instance=ENUM_strategy)
@settings(max_examples=50)
def test_enum_instantiation(instance):
    assert isinstance(instance, ENUM)

@given(instance=umm_Original_strategy)
@settings(max_examples=50)
def test_umm_original_instantiation(instance):
    assert isinstance(instance, umm_Original)

@given(instance=umm_Subset_strategy)
@settings(max_examples=50)
def test_umm_subset_instantiation(instance):
    assert isinstance(instance, umm_Subset)

@given(instance=umm_AssembledBase_strategy)
@settings(max_examples=50)
def test_umm_assembledbase_instantiation(instance):
    assert isinstance(instance, umm_AssembledBase)

@given(instance=umm_ENUM_strategy)
@settings(max_examples=50)
def test_umm_enum_instantiation(instance):
    assert isinstance(instance, umm_ENUM)



@given(instance=umm_ENUM_strategy)
def test_umm_enum_codeListAgencyIdentifier_setter(instance):
    original = instance.codeListAgencyIdentifier
    instance.codeListAgencyIdentifier = original
    assert instance.codeListAgencyIdentifier == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_codeListName_setter(instance):
    original = instance.codeListName
    instance.codeListName = original
    assert instance.codeListName == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_codeListIdentifier_setter(instance):
    original = instance.codeListIdentifier
    instance.codeListIdentifier = original
    assert instance.codeListIdentifier == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_ENUM_strategy)
def test_umm_enum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ABIEProperty_strategy)
@settings(max_examples=50)
def test_abieproperty_instantiation(instance):
    assert isinstance(instance, ABIEProperty)

@given(instance=umm_BBIE_strategy)
@settings(max_examples=50)
def test_umm_bbie_instantiation(instance):
    assert isinstance(instance, umm_BBIE)



@given(instance=umm_BBIE_strategy)
def test_umm_bbie_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original



@given(instance=umm_BBIE_strategy)
def test_umm_bbie_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original

@given(instance=umm_ASBIE_strategy)
@settings(max_examples=50)
def test_umm_asbie_instantiation(instance):
    assert isinstance(instance, umm_ASBIE)

@given(instance=umm_OclInvariant_strategy)
@settings(max_examples=50)
def test_umm_oclinvariant_instantiation(instance):
    assert isinstance(instance, umm_OclInvariant)

@given(instance=umm_TC_Constraint_strategy)
@settings(max_examples=50)
def test_umm_tc_constraint_instantiation(instance):
    assert isinstance(instance, umm_TC_Constraint)



@given(instance=umm_TC_Constraint_strategy)
def test_umm_tc_constraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=umm_TC_Constraint_strategy)
def test_umm_tc_constraint_listIdentifier_setter(instance):
    original = instance.listIdentifier
    instance.listIdentifier = original
    assert instance.listIdentifier == original



@given(instance=umm_TC_Constraint_strategy)
def test_umm_tc_constraint_responsibleAgency_setter(instance):
    original = instance.responsibleAgency
    instance.responsibleAgency = original
    assert instance.responsibleAgency == original

@given(instance=umm_ContextRef_strategy)
@settings(max_examples=50)
def test_umm_contextref_instantiation(instance):
    assert isinstance(instance, umm_ContextRef)



@given(instance=umm_ContextRef_strategy)
def test_umm_contextref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MAProperty_strategy)
@settings(max_examples=50)
def test_maproperty_instantiation(instance):
    assert isinstance(instance, MAProperty)

@given(instance=umm_ASNONE_strategy)
@settings(max_examples=50)
def test_umm_asnone_instantiation(instance):
    assert isinstance(instance, umm_ASNONE)

@given(instance=umm_ASMA_strategy)
@settings(max_examples=50)
def test_umm_asma_instantiation(instance):
    assert isinstance(instance, umm_ASMA)

@given(instance=OclRef_strategy)
@settings(max_examples=50)
def test_oclref_instantiation(instance):
    assert isinstance(instance, OclRef)

@given(instance=umm_BDTProperty_strategy)
@settings(max_examples=50)
def test_umm_bdtproperty_instantiation(instance):
    assert isinstance(instance, umm_BDTProperty)



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=umm_BDTProperty_strategy)
def test_umm_bdtproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm_ABIEProperty_strategy)
@settings(max_examples=50)
def test_umm_abieproperty_instantiation(instance):
    assert isinstance(instance, umm_ABIEProperty)



@given(instance=umm_ABIEProperty_strategy)
def test_umm_abieproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_ABIEProperty_strategy)
def test_umm_abieproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_ABIEProperty_strategy)
def test_umm_abieproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_ABIEProperty_strategy)
def test_umm_abieproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_ABIEProperty_strategy)
def test_umm_abieproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_ABIEProperty_strategy)
def test_umm_abieproperty_sequencingKey_setter(instance):
    original = instance.sequencingKey
    instance.sequencingKey = original
    assert instance.sequencingKey == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=umm_CCLibrary_strategy)
@settings(max_examples=50)
def test_umm_cclibrary_instantiation(instance):
    assert isinstance(instance, umm_CCLibrary)



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=umm_CCLibrary_strategy)
def test_umm_cclibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm_CDTLibrary_strategy)
@settings(max_examples=50)
def test_umm_cdtlibrary_instantiation(instance):
    assert isinstance(instance, umm_CDTLibrary)



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=umm_CDTLibrary_strategy)
def test_umm_cdtlibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm_PrimitiveLibrary_strategy)
@settings(max_examples=50)
def test_umm_primitivelibrary_instantiation(instance):
    assert isinstance(instance, umm_PrimitiveLibrary)

@given(instance=umm_ENUMLibrary_strategy)
@settings(max_examples=50)
def test_umm_enumlibrary_instantiation(instance):
    assert isinstance(instance, umm_ENUMLibrary)



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=umm_ENUMLibrary_strategy)
def test_umm_enumlibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm_DocLibrary_strategy)
@settings(max_examples=50)
def test_umm_doclibrary_instantiation(instance):
    assert isinstance(instance, umm_DocLibrary)



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_DocLibrary_strategy)
def test_umm_doclibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm_Library_strategy)
@settings(max_examples=50)
def test_umm_library_instantiation(instance):
    assert isinstance(instance, umm_Library)



@given(instance=umm_Library_strategy)
def test_umm_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm_Constraint_strategy)
@settings(max_examples=50)
def test_umm_constraint_instantiation(instance):
    assert isinstance(instance, umm_Constraint)

@given(instance=umm_MAProperty_strategy)
@settings(max_examples=50)
def test_umm_maproperty_instantiation(instance):
    assert isinstance(instance, umm_MAProperty)

@given(instance=ContextRef_strategy)
@settings(max_examples=50)
def test_contextref_instantiation(instance):
    assert isinstance(instance, ContextRef)

@given(instance=umm_ABIE_strategy)
@settings(max_examples=50)
def test_umm_abie_instantiation(instance):
    assert isinstance(instance, umm_ABIE)



@given(instance=umm_ABIE_strategy)
def test_umm_abie_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_ABIE_strategy)
def test_umm_abie_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_ABIE_strategy)
def test_umm_abie_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_ABIE_strategy)
def test_umm_abie_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_ABIE_strategy)
def test_umm_abie_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm_BDT_strategy)
@settings(max_examples=50)
def test_umm_bdt_instantiation(instance):
    assert isinstance(instance, umm_BDT)



@given(instance=umm_BDT_strategy)
def test_umm_bdt_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=umm_BDT_strategy)
def test_umm_bdt_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_BDT_strategy)
def test_umm_bdt_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_BDT_strategy)
def test_umm_bdt_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original



@given(instance=umm_BDT_strategy)
def test_umm_bdt_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm_MA_strategy)
@settings(max_examples=50)
def test_umm_ma_instantiation(instance):
    assert isinstance(instance, umm_MA)

@given(instance=umm_InfEnvelope_strategy)
@settings(max_examples=50)
def test_umm_infenvelope_instantiation(instance):
    assert isinstance(instance, umm_InfEnvelope)



@given(instance=umm_InfEnvelope_strategy)
def test_umm_infenvelope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm_BDTLibrary_strategy)
@settings(max_examples=50)
def test_umm_bdtlibrary_instantiation(instance):
    assert isinstance(instance, umm_BDTLibrary)



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=umm_BDTLibrary_strategy)
def test_umm_bdtlibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm_BIELibrary_strategy)
@settings(max_examples=50)
def test_umm_bielibrary_instantiation(instance):
    assert isinstance(instance, umm_BIELibrary)



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original



@given(instance=umm_BIELibrary_strategy)
def test_umm_bielibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original
