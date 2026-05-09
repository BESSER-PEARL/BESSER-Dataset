import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclLiteral,
    umm::OclStringLiteral,
    umm::OclIntegerLiteral,
    umm::OclBooleanLiteral,
    umm::OclEnumerationLiteral,
    OclFunctionCall,
    umm::OclSize,
    umm::OclNotEmpty,
    umm::OclIsEmpty,
    umm::OclForAll,
    umm::OclFunctionCall,
    OclBooleanLiteral,
    umm::OclBooleanTrue,
    umm::OclBooleanFalse,
    CDTProperty,
    umm::CDT::Supplement,
    umm::CDT::Content,
    umm::CDTProperty,
    umm::OclRef,
    umm::OclPathTail,
    OclReference,
    umm::OclPathFeatureHead,
    umm::OclPathSelfHead,
    OclValue,
    umm::OclLiteral,
    umm::OclReference,
    OclExpression,
    umm::OclLessOrEqual,
    umm::OclAnd,
    umm::OclLess,
    umm::OclMore,
    umm::OclMoreOrEqual,
    umm::OclXor,
    umm::OclOr,
    umm::OclArrow,
    umm::OclImplies,
    umm::OclEqual,
    umm::OclValue,
    umm::OclExpression,
    umm::CDT,
    umm::CodelistEntry,
    ACCProperty,
    umm::BCC,
    umm::ASCC,
    umm::ACCProperty,
    umm::ACC,
    BDTProperty,
    umm::Supplement,
    umm::Content,
    AssembledBase,
    umm::Assembled,
    umm::Primitive,
    ENUM,
    umm::Subset,
    umm::AssembledBase,
    umm::Original,
    umm::ENUM,
    ABIEProperty,
    umm::BBIE,
    umm::ASBIE,
    umm::OclInvariant,
    umm::TC::Constraint,
    umm::ContextRef,
    MAProperty,
    umm::ASNONE,
    umm::ASMA,
    OclRef,
    umm::BDTProperty,
    umm::ABIEProperty,
    Library,
    umm::CDTLibrary,
    umm::CCLibrary,
    umm::PrimitiveLibrary,
    umm::ENUMLibrary,
    umm::DocLibrary,
    umm::Library,
    umm::Constraint,
    umm::MAProperty,
    ContextRef,
    umm::ABIE,
    umm::BDT,
    umm::MA,
    umm::InfEnvelope,
    umm::BDTLibrary,
    umm::BIELibrary,
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



def test_umm::oclstringliteral_is_not_abstract():
    assert not inspect.isabstract(umm::OclStringLiteral)


def test_umm::oclstringliteral_constructor_exists():
    assert callable(umm::OclStringLiteral.__init__)


def test_umm::oclstringliteral_constructor_args():
    sig = inspect.signature(umm::OclStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umm::oclstringliteral_has_value():
    assert hasattr(umm::OclStringLiteral, "value")
    descriptor = None
    for klass in umm::OclStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umm::oclintegerliteral_is_not_abstract():
    assert not inspect.isabstract(umm::OclIntegerLiteral)


def test_umm::oclintegerliteral_constructor_exists():
    assert callable(umm::OclIntegerLiteral.__init__)


def test_umm::oclintegerliteral_constructor_args():
    sig = inspect.signature(umm::OclIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umm::oclintegerliteral_has_value():
    assert hasattr(umm::OclIntegerLiteral, "value")
    descriptor = None
    for klass in umm::OclIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umm::oclbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(umm::OclBooleanLiteral)


def test_umm::oclbooleanliteral_constructor_exists():
    assert callable(umm::OclBooleanLiteral.__init__)


def test_umm::oclbooleanliteral_constructor_args():
    sig = inspect.signature(umm::OclBooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(umm::OclEnumerationLiteral)


def test_umm::oclenumerationliteral_constructor_exists():
    assert callable(umm::OclEnumerationLiteral.__init__)


def test_umm::oclenumerationliteral_constructor_args():
    sig = inspect.signature(umm::OclEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umm::oclenumerationliteral_has_value():
    assert hasattr(umm::OclEnumerationLiteral, "value")
    descriptor = None
    for klass in umm::OclEnumerationLiteral.__mro__:
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



def test_umm::oclsize_is_not_abstract():
    assert not inspect.isabstract(umm::OclSize)


def test_umm::oclsize_constructor_exists():
    assert callable(umm::OclSize.__init__)


def test_umm::oclsize_constructor_args():
    sig = inspect.signature(umm::OclSize.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclnotempty_is_not_abstract():
    assert not inspect.isabstract(umm::OclNotEmpty)


def test_umm::oclnotempty_constructor_exists():
    assert callable(umm::OclNotEmpty.__init__)


def test_umm::oclnotempty_constructor_args():
    sig = inspect.signature(umm::OclNotEmpty.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclisempty_is_not_abstract():
    assert not inspect.isabstract(umm::OclIsEmpty)


def test_umm::oclisempty_constructor_exists():
    assert callable(umm::OclIsEmpty.__init__)


def test_umm::oclisempty_constructor_args():
    sig = inspect.signature(umm::OclIsEmpty.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclforall_is_not_abstract():
    assert not inspect.isabstract(umm::OclForAll)


def test_umm::oclforall_constructor_exists():
    assert callable(umm::OclForAll.__init__)


def test_umm::oclforall_constructor_args():
    sig = inspect.signature(umm::OclForAll.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclfunctioncall_is_not_abstract():
    assert not inspect.isabstract(umm::OclFunctionCall)


def test_umm::oclfunctioncall_constructor_exists():
    assert callable(umm::OclFunctionCall.__init__)


def test_umm::oclfunctioncall_constructor_args():
    sig = inspect.signature(umm::OclFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_oclbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(OclBooleanLiteral)


def test_oclbooleanliteral_constructor_exists():
    assert callable(OclBooleanLiteral.__init__)


def test_oclbooleanliteral_constructor_args():
    sig = inspect.signature(OclBooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclbooleantrue_is_not_abstract():
    assert not inspect.isabstract(umm::OclBooleanTrue)


def test_umm::oclbooleantrue_constructor_exists():
    assert callable(umm::OclBooleanTrue.__init__)


def test_umm::oclbooleantrue_constructor_args():
    sig = inspect.signature(umm::OclBooleanTrue.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclbooleanfalse_is_not_abstract():
    assert not inspect.isabstract(umm::OclBooleanFalse)


def test_umm::oclbooleanfalse_constructor_exists():
    assert callable(umm::OclBooleanFalse.__init__)


def test_umm::oclbooleanfalse_constructor_args():
    sig = inspect.signature(umm::OclBooleanFalse.__init__)
    params = list(sig.parameters.keys())



def test_cdtproperty_is_not_abstract():
    assert not inspect.isabstract(CDTProperty)


def test_cdtproperty_constructor_exists():
    assert callable(CDTProperty.__init__)


def test_cdtproperty_constructor_args():
    sig = inspect.signature(CDTProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm::cdt::supplement_is_not_abstract():
    assert not inspect.isabstract(umm::CDT::Supplement)


def test_umm::cdt::supplement_constructor_exists():
    assert callable(umm::CDT::Supplement.__init__)


def test_umm::cdt::supplement_constructor_args():
    sig = inspect.signature(umm::CDT::Supplement.__init__)
    params = list(sig.parameters.keys())
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "restriction" in params, "Missing parameter 'restriction'"

def test_umm::cdt::supplement_has_fixedValue():
    assert hasattr(umm::CDT::Supplement, "fixedValue")
    descriptor = None
    for klass in umm::CDT::Supplement.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt::supplement_has_defaultValue():
    assert hasattr(umm::CDT::Supplement, "defaultValue")
    descriptor = None
    for klass in umm::CDT::Supplement.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt::supplement_has_restriction():
    assert hasattr(umm::CDT::Supplement, "restriction")
    descriptor = None
    for klass in umm::CDT::Supplement.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)



def test_umm::cdt::content_is_not_abstract():
    assert not inspect.isabstract(umm::CDT::Content)


def test_umm::cdt::content_constructor_exists():
    assert callable(umm::CDT::Content.__init__)


def test_umm::cdt::content_constructor_args():
    sig = inspect.signature(umm::CDT::Content.__init__)
    params = list(sig.parameters.keys())



def test_umm::cdtproperty_is_not_abstract():
    assert not inspect.isabstract(umm::CDTProperty)


def test_umm::cdtproperty_constructor_exists():
    assert callable(umm::CDTProperty.__init__)


def test_umm::cdtproperty_constructor_args():
    sig = inspect.signature(umm::CDTProperty.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_umm::cdtproperty_has_uniqueIdentifier():
    assert hasattr(umm::CDTProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtproperty_has_businessTerm():
    assert hasattr(umm::CDTProperty, "businessTerm")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtproperty_has_definition():
    assert hasattr(umm::CDTProperty, "definition")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtproperty_has_dictionary():
    assert hasattr(umm::CDTProperty, "dictionary")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtproperty_has_name():
    assert hasattr(umm::CDTProperty, "name")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtproperty_has_versionIdentifier():
    assert hasattr(umm::CDTProperty, "versionIdentifier")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtproperty_has_multiplicity():
    assert hasattr(umm::CDTProperty, "multiplicity")
    descriptor = None
    for klass in umm::CDTProperty.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_umm::oclref_is_not_abstract():
    assert not inspect.isabstract(umm::OclRef)


def test_umm::oclref_constructor_exists():
    assert callable(umm::OclRef.__init__)


def test_umm::oclref_constructor_args():
    sig = inspect.signature(umm::OclRef.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "name" in params, "Missing parameter 'name'"

def test_umm::oclref_has_multiplicity():
    assert hasattr(umm::OclRef, "multiplicity")
    descriptor = None
    for klass in umm::OclRef.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_umm::oclref_has_name():
    assert hasattr(umm::OclRef, "name")
    descriptor = None
    for klass in umm::OclRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm::oclpathtail_is_not_abstract():
    assert not inspect.isabstract(umm::OclPathTail)


def test_umm::oclpathtail_constructor_exists():
    assert callable(umm::OclPathTail.__init__)


def test_umm::oclpathtail_constructor_args():
    sig = inspect.signature(umm::OclPathTail.__init__)
    params = list(sig.parameters.keys())



def test_oclreference_is_not_abstract():
    assert not inspect.isabstract(OclReference)


def test_oclreference_constructor_exists():
    assert callable(OclReference.__init__)


def test_oclreference_constructor_args():
    sig = inspect.signature(OclReference.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclpathfeaturehead_is_not_abstract():
    assert not inspect.isabstract(umm::OclPathFeatureHead)


def test_umm::oclpathfeaturehead_constructor_exists():
    assert callable(umm::OclPathFeatureHead.__init__)


def test_umm::oclpathfeaturehead_constructor_args():
    sig = inspect.signature(umm::OclPathFeatureHead.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclpathselfhead_is_not_abstract():
    assert not inspect.isabstract(umm::OclPathSelfHead)


def test_umm::oclpathselfhead_constructor_exists():
    assert callable(umm::OclPathSelfHead.__init__)


def test_umm::oclpathselfhead_constructor_args():
    sig = inspect.signature(umm::OclPathSelfHead.__init__)
    params = list(sig.parameters.keys())



def test_oclvalue_is_not_abstract():
    assert not inspect.isabstract(OclValue)


def test_oclvalue_constructor_exists():
    assert callable(OclValue.__init__)


def test_oclvalue_constructor_args():
    sig = inspect.signature(OclValue.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclliteral_is_not_abstract():
    assert not inspect.isabstract(umm::OclLiteral)


def test_umm::oclliteral_constructor_exists():
    assert callable(umm::OclLiteral.__init__)


def test_umm::oclliteral_constructor_args():
    sig = inspect.signature(umm::OclLiteral.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclreference_is_not_abstract():
    assert not inspect.isabstract(umm::OclReference)


def test_umm::oclreference_constructor_exists():
    assert callable(umm::OclReference.__init__)


def test_umm::oclreference_constructor_args():
    sig = inspect.signature(umm::OclReference.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_umm::ocllessorequal_is_not_abstract():
    assert not inspect.isabstract(umm::OclLessOrEqual)


def test_umm::ocllessorequal_constructor_exists():
    assert callable(umm::OclLessOrEqual.__init__)


def test_umm::ocllessorequal_constructor_args():
    sig = inspect.signature(umm::OclLessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_umm::ocland_is_not_abstract():
    assert not inspect.isabstract(umm::OclAnd)


def test_umm::ocland_constructor_exists():
    assert callable(umm::OclAnd.__init__)


def test_umm::ocland_constructor_args():
    sig = inspect.signature(umm::OclAnd.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclless_is_not_abstract():
    assert not inspect.isabstract(umm::OclLess)


def test_umm::oclless_constructor_exists():
    assert callable(umm::OclLess.__init__)


def test_umm::oclless_constructor_args():
    sig = inspect.signature(umm::OclLess.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclmore_is_not_abstract():
    assert not inspect.isabstract(umm::OclMore)


def test_umm::oclmore_constructor_exists():
    assert callable(umm::OclMore.__init__)


def test_umm::oclmore_constructor_args():
    sig = inspect.signature(umm::OclMore.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclmoreorequal_is_not_abstract():
    assert not inspect.isabstract(umm::OclMoreOrEqual)


def test_umm::oclmoreorequal_constructor_exists():
    assert callable(umm::OclMoreOrEqual.__init__)


def test_umm::oclmoreorequal_constructor_args():
    sig = inspect.signature(umm::OclMoreOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclxor_is_not_abstract():
    assert not inspect.isabstract(umm::OclXor)


def test_umm::oclxor_constructor_exists():
    assert callable(umm::OclXor.__init__)


def test_umm::oclxor_constructor_args():
    sig = inspect.signature(umm::OclXor.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclor_is_not_abstract():
    assert not inspect.isabstract(umm::OclOr)


def test_umm::oclor_constructor_exists():
    assert callable(umm::OclOr.__init__)


def test_umm::oclor_constructor_args():
    sig = inspect.signature(umm::OclOr.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclarrow_is_not_abstract():
    assert not inspect.isabstract(umm::OclArrow)


def test_umm::oclarrow_constructor_exists():
    assert callable(umm::OclArrow.__init__)


def test_umm::oclarrow_constructor_args():
    sig = inspect.signature(umm::OclArrow.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclimplies_is_not_abstract():
    assert not inspect.isabstract(umm::OclImplies)


def test_umm::oclimplies_constructor_exists():
    assert callable(umm::OclImplies.__init__)


def test_umm::oclimplies_constructor_args():
    sig = inspect.signature(umm::OclImplies.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclequal_is_not_abstract():
    assert not inspect.isabstract(umm::OclEqual)


def test_umm::oclequal_constructor_exists():
    assert callable(umm::OclEqual.__init__)


def test_umm::oclequal_constructor_args():
    sig = inspect.signature(umm::OclEqual.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclvalue_is_not_abstract():
    assert not inspect.isabstract(umm::OclValue)


def test_umm::oclvalue_constructor_exists():
    assert callable(umm::OclValue.__init__)


def test_umm::oclvalue_constructor_args():
    sig = inspect.signature(umm::OclValue.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclexpression_is_not_abstract():
    assert not inspect.isabstract(umm::OclExpression)


def test_umm::oclexpression_constructor_exists():
    assert callable(umm::OclExpression.__init__)


def test_umm::oclexpression_constructor_args():
    sig = inspect.signature(umm::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_umm::cdt_is_not_abstract():
    assert not inspect.isabstract(umm::CDT)


def test_umm::cdt_constructor_exists():
    assert callable(umm::CDT.__init__)


def test_umm::cdt_constructor_args():
    sig = inspect.signature(umm::CDT.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"

def test_umm::cdt_has_uniqueIdentifier():
    assert hasattr(umm::CDT, "uniqueIdentifier")
    descriptor = None
    for klass in umm::CDT.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt_has_businessTerm():
    assert hasattr(umm::CDT, "businessTerm")
    descriptor = None
    for klass in umm::CDT.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt_has_versionIdentifier():
    assert hasattr(umm::CDT, "versionIdentifier")
    descriptor = None
    for klass in umm::CDT.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt_has_name():
    assert hasattr(umm::CDT, "name")
    descriptor = None
    for klass in umm::CDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt_has_definition():
    assert hasattr(umm::CDT, "definition")
    descriptor = None
    for klass in umm::CDT.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdt_has_dictionary():
    assert hasattr(umm::CDT, "dictionary")
    descriptor = None
    for klass in umm::CDT.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)



def test_umm::codelistentry_is_not_abstract():
    assert not inspect.isabstract(umm::CodelistEntry)


def test_umm::codelistentry_constructor_exists():
    assert callable(umm::CodelistEntry.__init__)


def test_umm::codelistentry_constructor_args():
    sig = inspect.signature(umm::CodelistEntry.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_umm::codelistentry_has_description():
    assert hasattr(umm::CodelistEntry, "description")
    descriptor = None
    for klass in umm::CodelistEntry.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_umm::codelistentry_has_name():
    assert hasattr(umm::CodelistEntry, "name")
    descriptor = None
    for klass in umm::CodelistEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_accproperty_is_not_abstract():
    assert not inspect.isabstract(ACCProperty)


def test_accproperty_constructor_exists():
    assert callable(ACCProperty.__init__)


def test_accproperty_constructor_args():
    sig = inspect.signature(ACCProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm::bcc_is_not_abstract():
    assert not inspect.isabstract(umm::BCC)


def test_umm::bcc_constructor_exists():
    assert callable(umm::BCC.__init__)


def test_umm::bcc_constructor_args():
    sig = inspect.signature(umm::BCC.__init__)
    params = list(sig.parameters.keys())
    assert "restriction" in params, "Missing parameter 'restriction'"
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"

def test_umm::bcc_has_restriction():
    assert hasattr(umm::BCC, "restriction")
    descriptor = None
    for klass in umm::BCC.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)

def test_umm::bcc_has_fixedValue():
    assert hasattr(umm::BCC, "fixedValue")
    descriptor = None
    for klass in umm::BCC.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)



def test_umm::ascc_is_not_abstract():
    assert not inspect.isabstract(umm::ASCC)


def test_umm::ascc_constructor_exists():
    assert callable(umm::ASCC.__init__)


def test_umm::ascc_constructor_args():
    sig = inspect.signature(umm::ASCC.__init__)
    params = list(sig.parameters.keys())



def test_umm::accproperty_is_not_abstract():
    assert not inspect.isabstract(umm::ACCProperty)


def test_umm::accproperty_constructor_exists():
    assert callable(umm::ACCProperty.__init__)


def test_umm::accproperty_constructor_args():
    sig = inspect.signature(umm::ACCProperty.__init__)
    params = list(sig.parameters.keys())
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "sequencingKey" in params, "Missing parameter 'sequencingKey'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "definition" in params, "Missing parameter 'definition'"

def test_umm::accproperty_has_versionIdentifier():
    assert hasattr(umm::ACCProperty, "versionIdentifier")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_uniqueIdentifier():
    assert hasattr(umm::ACCProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_sequencingKey():
    assert hasattr(umm::ACCProperty, "sequencingKey")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "sequencingKey" in klass.__dict__:
            descriptor = klass.__dict__["sequencingKey"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_businessTerm():
    assert hasattr(umm::ACCProperty, "businessTerm")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_multiplicity():
    assert hasattr(umm::ACCProperty, "multiplicity")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_name():
    assert hasattr(umm::ACCProperty, "name")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_dictionary():
    assert hasattr(umm::ACCProperty, "dictionary")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::accproperty_has_definition():
    assert hasattr(umm::ACCProperty, "definition")
    descriptor = None
    for klass in umm::ACCProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)



def test_umm::acc_is_not_abstract():
    assert not inspect.isabstract(umm::ACC)


def test_umm::acc_constructor_exists():
    assert callable(umm::ACC.__init__)


def test_umm::acc_constructor_args():
    sig = inspect.signature(umm::ACC.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "definition" in params, "Missing parameter 'definition'"

def test_umm::acc_has_uniqueIdentifier():
    assert hasattr(umm::ACC, "uniqueIdentifier")
    descriptor = None
    for klass in umm::ACC.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::acc_has_dictionary():
    assert hasattr(umm::ACC, "dictionary")
    descriptor = None
    for klass in umm::ACC.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::acc_has_businessTerm():
    assert hasattr(umm::ACC, "businessTerm")
    descriptor = None
    for klass in umm::ACC.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::acc_has_versionIdentifier():
    assert hasattr(umm::ACC, "versionIdentifier")
    descriptor = None
    for klass in umm::ACC.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::acc_has_name():
    assert hasattr(umm::ACC, "name")
    descriptor = None
    for klass in umm::ACC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm::acc_has_definition():
    assert hasattr(umm::ACC, "definition")
    descriptor = None
    for klass in umm::ACC.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)



def test_bdtproperty_is_not_abstract():
    assert not inspect.isabstract(BDTProperty)


def test_bdtproperty_constructor_exists():
    assert callable(BDTProperty.__init__)


def test_bdtproperty_constructor_args():
    sig = inspect.signature(BDTProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm::supplement_is_not_abstract():
    assert not inspect.isabstract(umm::Supplement)


def test_umm::supplement_constructor_exists():
    assert callable(umm::Supplement.__init__)


def test_umm::supplement_constructor_args():
    sig = inspect.signature(umm::Supplement.__init__)
    params = list(sig.parameters.keys())
    assert "restriction" in params, "Missing parameter 'restriction'"
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_umm::supplement_has_restriction():
    assert hasattr(umm::Supplement, "restriction")
    descriptor = None
    for klass in umm::Supplement.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)

def test_umm::supplement_has_fixedValue():
    assert hasattr(umm::Supplement, "fixedValue")
    descriptor = None
    for klass in umm::Supplement.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)

def test_umm::supplement_has_defaultValue():
    assert hasattr(umm::Supplement, "defaultValue")
    descriptor = None
    for klass in umm::Supplement.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_umm::content_is_not_abstract():
    assert not inspect.isabstract(umm::Content)


def test_umm::content_constructor_exists():
    assert callable(umm::Content.__init__)


def test_umm::content_constructor_args():
    sig = inspect.signature(umm::Content.__init__)
    params = list(sig.parameters.keys())
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "fractionalDigits" in params, "Missing parameter 'fractionalDigits'"
    assert "minExclusive" in params, "Missing parameter 'minExclusive'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"
    assert "maxExclusive" in params, "Missing parameter 'maxExclusive'"
    assert "totalDigits" in params, "Missing parameter 'totalDigits'"

def test_umm::content_has_minInclusive():
    assert hasattr(umm::Content, "minInclusive")
    descriptor = None
    for klass in umm::Content.__mro__:
        if "minInclusive" in klass.__dict__:
            descriptor = klass.__dict__["minInclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm::content_has_fractionalDigits():
    assert hasattr(umm::Content, "fractionalDigits")
    descriptor = None
    for klass in umm::Content.__mro__:
        if "fractionalDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionalDigits"]
            break
    assert isinstance(descriptor, property)

def test_umm::content_has_minExclusive():
    assert hasattr(umm::Content, "minExclusive")
    descriptor = None
    for klass in umm::Content.__mro__:
        if "minExclusive" in klass.__dict__:
            descriptor = klass.__dict__["minExclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm::content_has_maxInclusive():
    assert hasattr(umm::Content, "maxInclusive")
    descriptor = None
    for klass in umm::Content.__mro__:
        if "maxInclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxInclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm::content_has_maxExclusive():
    assert hasattr(umm::Content, "maxExclusive")
    descriptor = None
    for klass in umm::Content.__mro__:
        if "maxExclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxExclusive"]
            break
    assert isinstance(descriptor, property)

def test_umm::content_has_totalDigits():
    assert hasattr(umm::Content, "totalDigits")
    descriptor = None
    for klass in umm::Content.__mro__:
        if "totalDigits" in klass.__dict__:
            descriptor = klass.__dict__["totalDigits"]
            break
    assert isinstance(descriptor, property)



def test_assembledbase_is_not_abstract():
    assert not inspect.isabstract(AssembledBase)


def test_assembledbase_constructor_exists():
    assert callable(AssembledBase.__init__)


def test_assembledbase_constructor_args():
    sig = inspect.signature(AssembledBase.__init__)
    params = list(sig.parameters.keys())



def test_umm::assembled_is_not_abstract():
    assert not inspect.isabstract(umm::Assembled)


def test_umm::assembled_constructor_exists():
    assert callable(umm::Assembled.__init__)


def test_umm::assembled_constructor_args():
    sig = inspect.signature(umm::Assembled.__init__)
    params = list(sig.parameters.keys())



def test_umm::primitive_is_not_abstract():
    assert not inspect.isabstract(umm::Primitive)


def test_umm::primitive_constructor_exists():
    assert callable(umm::Primitive.__init__)


def test_umm::primitive_constructor_args():
    sig = inspect.signature(umm::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_enum_is_not_abstract():
    assert not inspect.isabstract(ENUM)


def test_enum_constructor_exists():
    assert callable(ENUM.__init__)


def test_enum_constructor_args():
    sig = inspect.signature(ENUM.__init__)
    params = list(sig.parameters.keys())



def test_umm::subset_is_not_abstract():
    assert not inspect.isabstract(umm::Subset)


def test_umm::subset_constructor_exists():
    assert callable(umm::Subset.__init__)


def test_umm::subset_constructor_args():
    sig = inspect.signature(umm::Subset.__init__)
    params = list(sig.parameters.keys())



def test_umm::assembledbase_is_not_abstract():
    assert not inspect.isabstract(umm::AssembledBase)


def test_umm::assembledbase_constructor_exists():
    assert callable(umm::AssembledBase.__init__)


def test_umm::assembledbase_constructor_args():
    sig = inspect.signature(umm::AssembledBase.__init__)
    params = list(sig.parameters.keys())



def test_umm::original_is_not_abstract():
    assert not inspect.isabstract(umm::Original)


def test_umm::original_constructor_exists():
    assert callable(umm::Original.__init__)


def test_umm::original_constructor_args():
    sig = inspect.signature(umm::Original.__init__)
    params = list(sig.parameters.keys())



def test_umm::enum_is_not_abstract():
    assert not inspect.isabstract(umm::ENUM)


def test_umm::enum_constructor_exists():
    assert callable(umm::ENUM.__init__)


def test_umm::enum_constructor_args():
    sig = inspect.signature(umm::ENUM.__init__)
    params = list(sig.parameters.keys())
    assert "definition" in params, "Missing parameter 'definition'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "codeListAgencyIdentifier" in params, "Missing parameter 'codeListAgencyIdentifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "codeListName" in params, "Missing parameter 'codeListName'"
    assert "codeListIdentifier" in params, "Missing parameter 'codeListIdentifier'"

def test_umm::enum_has_definition():
    assert hasattr(umm::ENUM, "definition")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_uniqueIdentifier():
    assert hasattr(umm::ENUM, "uniqueIdentifier")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_businessTerm():
    assert hasattr(umm::ENUM, "businessTerm")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_codeListAgencyIdentifier():
    assert hasattr(umm::ENUM, "codeListAgencyIdentifier")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "codeListAgencyIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["codeListAgencyIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_name():
    assert hasattr(umm::ENUM, "name")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_versionIdentifier():
    assert hasattr(umm::ENUM, "versionIdentifier")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_dictionary():
    assert hasattr(umm::ENUM, "dictionary")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_codeListName():
    assert hasattr(umm::ENUM, "codeListName")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "codeListName" in klass.__dict__:
            descriptor = klass.__dict__["codeListName"]
            break
    assert isinstance(descriptor, property)

def test_umm::enum_has_codeListIdentifier():
    assert hasattr(umm::ENUM, "codeListIdentifier")
    descriptor = None
    for klass in umm::ENUM.__mro__:
        if "codeListIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["codeListIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_abieproperty_is_not_abstract():
    assert not inspect.isabstract(ABIEProperty)


def test_abieproperty_constructor_exists():
    assert callable(ABIEProperty.__init__)


def test_abieproperty_constructor_args():
    sig = inspect.signature(ABIEProperty.__init__)
    params = list(sig.parameters.keys())



def test_umm::bbie_is_not_abstract():
    assert not inspect.isabstract(umm::BBIE)


def test_umm::bbie_constructor_exists():
    assert callable(umm::BBIE.__init__)


def test_umm::bbie_constructor_args():
    sig = inspect.signature(umm::BBIE.__init__)
    params = list(sig.parameters.keys())
    assert "fixedValue" in params, "Missing parameter 'fixedValue'"
    assert "restriction" in params, "Missing parameter 'restriction'"

def test_umm::bbie_has_fixedValue():
    assert hasattr(umm::BBIE, "fixedValue")
    descriptor = None
    for klass in umm::BBIE.__mro__:
        if "fixedValue" in klass.__dict__:
            descriptor = klass.__dict__["fixedValue"]
            break
    assert isinstance(descriptor, property)

def test_umm::bbie_has_restriction():
    assert hasattr(umm::BBIE, "restriction")
    descriptor = None
    for klass in umm::BBIE.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)



def test_umm::asbie_is_not_abstract():
    assert not inspect.isabstract(umm::ASBIE)


def test_umm::asbie_constructor_exists():
    assert callable(umm::ASBIE.__init__)


def test_umm::asbie_constructor_args():
    sig = inspect.signature(umm::ASBIE.__init__)
    params = list(sig.parameters.keys())



def test_umm::oclinvariant_is_not_abstract():
    assert not inspect.isabstract(umm::OclInvariant)


def test_umm::oclinvariant_constructor_exists():
    assert callable(umm::OclInvariant.__init__)


def test_umm::oclinvariant_constructor_args():
    sig = inspect.signature(umm::OclInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umm::tc::constraint_is_not_abstract():
    assert not inspect.isabstract(umm::TC::Constraint)


def test_umm::tc::constraint_constructor_exists():
    assert callable(umm::TC::Constraint.__init__)


def test_umm::tc::constraint_constructor_args():
    sig = inspect.signature(umm::TC::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "responsibleAgency" in params, "Missing parameter 'responsibleAgency'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "listIdentifier" in params, "Missing parameter 'listIdentifier'"

def test_umm::tc::constraint_has_responsibleAgency():
    assert hasattr(umm::TC::Constraint, "responsibleAgency")
    descriptor = None
    for klass in umm::TC::Constraint.__mro__:
        if "responsibleAgency" in klass.__dict__:
            descriptor = klass.__dict__["responsibleAgency"]
            break
    assert isinstance(descriptor, property)

def test_umm::tc::constraint_has_kind():
    assert hasattr(umm::TC::Constraint, "kind")
    descriptor = None
    for klass in umm::TC::Constraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umm::tc::constraint_has_listIdentifier():
    assert hasattr(umm::TC::Constraint, "listIdentifier")
    descriptor = None
    for klass in umm::TC::Constraint.__mro__:
        if "listIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["listIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm::contextref_is_not_abstract():
    assert not inspect.isabstract(umm::ContextRef)


def test_umm::contextref_constructor_exists():
    assert callable(umm::ContextRef.__init__)


def test_umm::contextref_constructor_args():
    sig = inspect.signature(umm::ContextRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umm::contextref_has_name():
    assert hasattr(umm::ContextRef, "name")
    descriptor = None
    for klass in umm::ContextRef.__mro__:
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



def test_umm::asnone_is_not_abstract():
    assert not inspect.isabstract(umm::ASNONE)


def test_umm::asnone_constructor_exists():
    assert callable(umm::ASNONE.__init__)


def test_umm::asnone_constructor_args():
    sig = inspect.signature(umm::ASNONE.__init__)
    params = list(sig.parameters.keys())



def test_umm::asma_is_not_abstract():
    assert not inspect.isabstract(umm::ASMA)


def test_umm::asma_constructor_exists():
    assert callable(umm::ASMA.__init__)


def test_umm::asma_constructor_args():
    sig = inspect.signature(umm::ASMA.__init__)
    params = list(sig.parameters.keys())



def test_oclref_is_not_abstract():
    assert not inspect.isabstract(OclRef)


def test_oclref_constructor_exists():
    assert callable(OclRef.__init__)


def test_oclref_constructor_args():
    sig = inspect.signature(OclRef.__init__)
    params = list(sig.parameters.keys())



def test_umm::bdtproperty_is_not_abstract():
    assert not inspect.isabstract(umm::BDTProperty)


def test_umm::bdtproperty_constructor_exists():
    assert callable(umm::BDTProperty.__init__)


def test_umm::bdtproperty_constructor_args():
    sig = inspect.signature(umm::BDTProperty.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm::bdtproperty_has_length():
    assert hasattr(umm::BDTProperty, "length")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_pattern():
    assert hasattr(umm::BDTProperty, "pattern")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_versionIdentifier():
    assert hasattr(umm::BDTProperty, "versionIdentifier")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_definition():
    assert hasattr(umm::BDTProperty, "definition")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_maxLength():
    assert hasattr(umm::BDTProperty, "maxLength")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_dictionary():
    assert hasattr(umm::BDTProperty, "dictionary")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_businessTerm():
    assert hasattr(umm::BDTProperty, "businessTerm")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_minLength():
    assert hasattr(umm::BDTProperty, "minLength")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtproperty_has_uniqueIdentifier():
    assert hasattr(umm::BDTProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm::BDTProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm::abieproperty_is_not_abstract():
    assert not inspect.isabstract(umm::ABIEProperty)


def test_umm::abieproperty_constructor_exists():
    assert callable(umm::ABIEProperty.__init__)


def test_umm::abieproperty_constructor_args():
    sig = inspect.signature(umm::ABIEProperty.__init__)
    params = list(sig.parameters.keys())
    assert "definition" in params, "Missing parameter 'definition'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "sequencingKey" in params, "Missing parameter 'sequencingKey'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm::abieproperty_has_definition():
    assert hasattr(umm::ABIEProperty, "definition")
    descriptor = None
    for klass in umm::ABIEProperty.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm::abieproperty_has_businessTerm():
    assert hasattr(umm::ABIEProperty, "businessTerm")
    descriptor = None
    for klass in umm::ABIEProperty.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::abieproperty_has_dictionary():
    assert hasattr(umm::ABIEProperty, "dictionary")
    descriptor = None
    for klass in umm::ABIEProperty.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::abieproperty_has_versionIdentifier():
    assert hasattr(umm::ABIEProperty, "versionIdentifier")
    descriptor = None
    for klass in umm::ABIEProperty.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::abieproperty_has_sequencingKey():
    assert hasattr(umm::ABIEProperty, "sequencingKey")
    descriptor = None
    for klass in umm::ABIEProperty.__mro__:
        if "sequencingKey" in klass.__dict__:
            descriptor = klass.__dict__["sequencingKey"]
            break
    assert isinstance(descriptor, property)

def test_umm::abieproperty_has_uniqueIdentifier():
    assert hasattr(umm::ABIEProperty, "uniqueIdentifier")
    descriptor = None
    for klass in umm::ABIEProperty.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_umm::cdtlibrary_is_not_abstract():
    assert not inspect.isabstract(umm::CDTLibrary)


def test_umm::cdtlibrary_constructor_exists():
    assert callable(umm::CDTLibrary.__init__)


def test_umm::cdtlibrary_constructor_args():
    sig = inspect.signature(umm::CDTLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"

def test_umm::cdtlibrary_has_baseURN():
    assert hasattr(umm::CDTLibrary, "baseURN")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_versionIdentifier():
    assert hasattr(umm::CDTLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_uniqueIdentifier():
    assert hasattr(umm::CDTLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_reference():
    assert hasattr(umm::CDTLibrary, "reference")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_copyright():
    assert hasattr(umm::CDTLibrary, "copyright")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_businessTerm():
    assert hasattr(umm::CDTLibrary, "businessTerm")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_owner():
    assert hasattr(umm::CDTLibrary, "owner")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm::cdtlibrary_has_namespacePrefix():
    assert hasattr(umm::CDTLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm::CDTLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)



def test_umm::cclibrary_is_not_abstract():
    assert not inspect.isabstract(umm::CCLibrary)


def test_umm::cclibrary_constructor_exists():
    assert callable(umm::CCLibrary.__init__)


def test_umm::cclibrary_constructor_args():
    sig = inspect.signature(umm::CCLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm::cclibrary_has_copyright():
    assert hasattr(umm::CCLibrary, "copyright")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_versionIdentifier():
    assert hasattr(umm::CCLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_baseURN():
    assert hasattr(umm::CCLibrary, "baseURN")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_businessTerm():
    assert hasattr(umm::CCLibrary, "businessTerm")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_namespacePrefix():
    assert hasattr(umm::CCLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_owner():
    assert hasattr(umm::CCLibrary, "owner")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_reference():
    assert hasattr(umm::CCLibrary, "reference")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm::cclibrary_has_uniqueIdentifier():
    assert hasattr(umm::CCLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm::CCLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm::primitivelibrary_is_not_abstract():
    assert not inspect.isabstract(umm::PrimitiveLibrary)


def test_umm::primitivelibrary_constructor_exists():
    assert callable(umm::PrimitiveLibrary.__init__)


def test_umm::primitivelibrary_constructor_args():
    sig = inspect.signature(umm::PrimitiveLibrary.__init__)
    params = list(sig.parameters.keys())



def test_umm::enumlibrary_is_not_abstract():
    assert not inspect.isabstract(umm::ENUMLibrary)


def test_umm::enumlibrary_constructor_exists():
    assert callable(umm::ENUMLibrary.__init__)


def test_umm::enumlibrary_constructor_args():
    sig = inspect.signature(umm::ENUMLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm::enumlibrary_has_copyright():
    assert hasattr(umm::ENUMLibrary, "copyright")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_businessTerm():
    assert hasattr(umm::ENUMLibrary, "businessTerm")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_reference():
    assert hasattr(umm::ENUMLibrary, "reference")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_versionIdentifier():
    assert hasattr(umm::ENUMLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_baseURN():
    assert hasattr(umm::ENUMLibrary, "baseURN")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_owner():
    assert hasattr(umm::ENUMLibrary, "owner")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_namespacePrefix():
    assert hasattr(umm::ENUMLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm::enumlibrary_has_uniqueIdentifier():
    assert hasattr(umm::ENUMLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm::ENUMLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm::doclibrary_is_not_abstract():
    assert not inspect.isabstract(umm::DocLibrary)


def test_umm::doclibrary_constructor_exists():
    assert callable(umm::DocLibrary.__init__)


def test_umm::doclibrary_constructor_args():
    sig = inspect.signature(umm::DocLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"

def test_umm::doclibrary_has_reference():
    assert hasattr(umm::DocLibrary, "reference")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_copyright():
    assert hasattr(umm::DocLibrary, "copyright")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_namespacePrefix():
    assert hasattr(umm::DocLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_baseURN():
    assert hasattr(umm::DocLibrary, "baseURN")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_versionIdentifier():
    assert hasattr(umm::DocLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_businessTerm():
    assert hasattr(umm::DocLibrary, "businessTerm")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_owner():
    assert hasattr(umm::DocLibrary, "owner")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm::doclibrary_has_uniqueIdentifier():
    assert hasattr(umm::DocLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm::DocLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm::library_is_not_abstract():
    assert not inspect.isabstract(umm::Library)


def test_umm::library_constructor_exists():
    assert callable(umm::Library.__init__)


def test_umm::library_constructor_args():
    sig = inspect.signature(umm::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umm::library_has_name():
    assert hasattr(umm::Library, "name")
    descriptor = None
    for klass in umm::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm::constraint_is_not_abstract():
    assert not inspect.isabstract(umm::Constraint)


def test_umm::constraint_constructor_exists():
    assert callable(umm::Constraint.__init__)


def test_umm::constraint_constructor_args():
    sig = inspect.signature(umm::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_umm::maproperty_is_not_abstract():
    assert not inspect.isabstract(umm::MAProperty)


def test_umm::maproperty_constructor_exists():
    assert callable(umm::MAProperty.__init__)


def test_umm::maproperty_constructor_args():
    sig = inspect.signature(umm::MAProperty.__init__)
    params = list(sig.parameters.keys())



def test_contextref_is_not_abstract():
    assert not inspect.isabstract(ContextRef)


def test_contextref_constructor_exists():
    assert callable(ContextRef.__init__)


def test_contextref_constructor_args():
    sig = inspect.signature(ContextRef.__init__)
    params = list(sig.parameters.keys())



def test_umm::abie_is_not_abstract():
    assert not inspect.isabstract(umm::ABIE)


def test_umm::abie_constructor_exists():
    assert callable(umm::ABIE.__init__)


def test_umm::abie_constructor_args():
    sig = inspect.signature(umm::ABIE.__init__)
    params = list(sig.parameters.keys())
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"

def test_umm::abie_has_versionIdentifier():
    assert hasattr(umm::ABIE, "versionIdentifier")
    descriptor = None
    for klass in umm::ABIE.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::abie_has_definition():
    assert hasattr(umm::ABIE, "definition")
    descriptor = None
    for klass in umm::ABIE.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_umm::abie_has_uniqueIdentifier():
    assert hasattr(umm::ABIE, "uniqueIdentifier")
    descriptor = None
    for klass in umm::ABIE.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::abie_has_businessTerm():
    assert hasattr(umm::ABIE, "businessTerm")
    descriptor = None
    for klass in umm::ABIE.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::abie_has_dictionary():
    assert hasattr(umm::ABIE, "dictionary")
    descriptor = None
    for klass in umm::ABIE.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)



def test_umm::bdt_is_not_abstract():
    assert not inspect.isabstract(umm::BDT)


def test_umm::bdt_constructor_exists():
    assert callable(umm::BDT.__init__)


def test_umm::bdt_constructor_args():
    sig = inspect.signature(umm::BDT.__init__)
    params = list(sig.parameters.keys())
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "dictionary" in params, "Missing parameter 'dictionary'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "definition" in params, "Missing parameter 'definition'"

def test_umm::bdt_has_versionIdentifier():
    assert hasattr(umm::BDT, "versionIdentifier")
    descriptor = None
    for klass in umm::BDT.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdt_has_dictionary():
    assert hasattr(umm::BDT, "dictionary")
    descriptor = None
    for klass in umm::BDT.__mro__:
        if "dictionary" in klass.__dict__:
            descriptor = klass.__dict__["dictionary"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdt_has_businessTerm():
    assert hasattr(umm::BDT, "businessTerm")
    descriptor = None
    for klass in umm::BDT.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdt_has_uniqueIdentifier():
    assert hasattr(umm::BDT, "uniqueIdentifier")
    descriptor = None
    for klass in umm::BDT.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdt_has_definition():
    assert hasattr(umm::BDT, "definition")
    descriptor = None
    for klass in umm::BDT.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)



def test_umm::ma_is_not_abstract():
    assert not inspect.isabstract(umm::MA)


def test_umm::ma_constructor_exists():
    assert callable(umm::MA.__init__)


def test_umm::ma_constructor_args():
    sig = inspect.signature(umm::MA.__init__)
    params = list(sig.parameters.keys())



def test_umm::infenvelope_is_not_abstract():
    assert not inspect.isabstract(umm::InfEnvelope)


def test_umm::infenvelope_constructor_exists():
    assert callable(umm::InfEnvelope.__init__)


def test_umm::infenvelope_constructor_args():
    sig = inspect.signature(umm::InfEnvelope.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umm::infenvelope_has_name():
    assert hasattr(umm::InfEnvelope, "name")
    descriptor = None
    for klass in umm::InfEnvelope.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umm::bdtlibrary_is_not_abstract():
    assert not inspect.isabstract(umm::BDTLibrary)


def test_umm::bdtlibrary_constructor_exists():
    assert callable(umm::BDTLibrary.__init__)


def test_umm::bdtlibrary_constructor_args():
    sig = inspect.signature(umm::BDTLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"

def test_umm::bdtlibrary_has_reference():
    assert hasattr(umm::BDTLibrary, "reference")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_copyright():
    assert hasattr(umm::BDTLibrary, "copyright")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_uniqueIdentifier():
    assert hasattr(umm::BDTLibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_baseURN():
    assert hasattr(umm::BDTLibrary, "baseURN")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_businessTerm():
    assert hasattr(umm::BDTLibrary, "businessTerm")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_namespacePrefix():
    assert hasattr(umm::BDTLibrary, "namespacePrefix")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_owner():
    assert hasattr(umm::BDTLibrary, "owner")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm::bdtlibrary_has_versionIdentifier():
    assert hasattr(umm::BDTLibrary, "versionIdentifier")
    descriptor = None
    for klass in umm::BDTLibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_umm::bielibrary_is_not_abstract():
    assert not inspect.isabstract(umm::BIELibrary)


def test_umm::bielibrary_constructor_exists():
    assert callable(umm::BIELibrary.__init__)


def test_umm::bielibrary_constructor_args():
    sig = inspect.signature(umm::BIELibrary.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "versionIdentifier" in params, "Missing parameter 'versionIdentifier'"
    assert "namespacePrefix" in params, "Missing parameter 'namespacePrefix'"
    assert "uniqueIdentifier" in params, "Missing parameter 'uniqueIdentifier'"
    assert "businessTerm" in params, "Missing parameter 'businessTerm'"
    assert "baseURN" in params, "Missing parameter 'baseURN'"

def test_umm::bielibrary_has_reference():
    assert hasattr(umm::BIELibrary, "reference")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_copyright():
    assert hasattr(umm::BIELibrary, "copyright")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_owner():
    assert hasattr(umm::BIELibrary, "owner")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_versionIdentifier():
    assert hasattr(umm::BIELibrary, "versionIdentifier")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "versionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["versionIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_namespacePrefix():
    assert hasattr(umm::BIELibrary, "namespacePrefix")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "namespacePrefix" in klass.__dict__:
            descriptor = klass.__dict__["namespacePrefix"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_uniqueIdentifier():
    assert hasattr(umm::BIELibrary, "uniqueIdentifier")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "uniqueIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["uniqueIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_businessTerm():
    assert hasattr(umm::BIELibrary, "businessTerm")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "businessTerm" in klass.__dict__:
            descriptor = klass.__dict__["businessTerm"]
            break
    assert isinstance(descriptor, property)

def test_umm::bielibrary_has_baseURN():
    assert hasattr(umm::BIELibrary, "baseURN")
    descriptor = None
    for klass in umm::BIELibrary.__mro__:
        if "baseURN" in klass.__dict__:
            descriptor = klass.__dict__["baseURN"]
            break
    assert isinstance(descriptor, property)

def test_constraintkind_exists():
    # Check that the Enumeration exists
    assert ConstraintKind is not None

def test_constraintkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintKind]
    expected_literals = [
        "payload",
        "document",
        "abie",
        "bdt",
        "invariant",
        "facet",
        "dependency",
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
        "OneOrMore",
        "One",
        "ZeroOrMore",
        "Optional",
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
umm::OclStringLiteral_strategy = st.builds(
    umm::OclStringLiteral,
    value=
        safe_text
)
umm::OclIntegerLiteral_strategy = st.builds(
    umm::OclIntegerLiteral,
    value=
        st.integers()
)
umm::OclBooleanLiteral_strategy = st.builds(
    umm::OclBooleanLiteral,
)
umm::OclEnumerationLiteral_strategy = st.builds(
    umm::OclEnumerationLiteral,
    value=
        safe_text
)
OclFunctionCall_strategy = st.builds(
    OclFunctionCall,
)
umm::OclSize_strategy = st.builds(
    umm::OclSize,
)
umm::OclNotEmpty_strategy = st.builds(
    umm::OclNotEmpty,
)
umm::OclIsEmpty_strategy = st.builds(
    umm::OclIsEmpty,
)
umm::OclForAll_strategy = st.builds(
    umm::OclForAll,
)
umm::OclFunctionCall_strategy = st.builds(
    umm::OclFunctionCall,
)
OclBooleanLiteral_strategy = st.builds(
    OclBooleanLiteral,
)
umm::OclBooleanTrue_strategy = st.builds(
    umm::OclBooleanTrue,
)
umm::OclBooleanFalse_strategy = st.builds(
    umm::OclBooleanFalse,
)
CDTProperty_strategy = st.builds(
    CDTProperty,
)
umm::CDT::Supplement_strategy = st.builds(
    umm::CDT::Supplement,
    fixedValue=
        safe_text,
    defaultValue=
        safe_text,
    restriction=
        safe_text
)
umm::CDT::Content_strategy = st.builds(
    umm::CDT::Content,
)
umm::CDTProperty_strategy = st.builds(
    umm::CDTProperty,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    definition=
        safe_text,
    dictionary=
        safe_text,
    name=
        safe_text,
    versionIdentifier=
        safe_text,
    multiplicity=
        safe_text
)
umm::OclRef_strategy = st.builds(
    umm::OclRef,
    multiplicity=
        safe_text,
    name=
        safe_text
)
umm::OclPathTail_strategy = st.builds(
    umm::OclPathTail,
)
OclReference_strategy = st.builds(
    OclReference,
)
umm::OclPathFeatureHead_strategy = st.builds(
    umm::OclPathFeatureHead,
)
umm::OclPathSelfHead_strategy = st.builds(
    umm::OclPathSelfHead,
)
OclValue_strategy = st.builds(
    OclValue,
)
umm::OclLiteral_strategy = st.builds(
    umm::OclLiteral,
)
umm::OclReference_strategy = st.builds(
    umm::OclReference,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
umm::OclLessOrEqual_strategy = st.builds(
    umm::OclLessOrEqual,
)
umm::OclAnd_strategy = st.builds(
    umm::OclAnd,
)
umm::OclLess_strategy = st.builds(
    umm::OclLess,
)
umm::OclMore_strategy = st.builds(
    umm::OclMore,
)
umm::OclMoreOrEqual_strategy = st.builds(
    umm::OclMoreOrEqual,
)
umm::OclXor_strategy = st.builds(
    umm::OclXor,
)
umm::OclOr_strategy = st.builds(
    umm::OclOr,
)
umm::OclArrow_strategy = st.builds(
    umm::OclArrow,
)
umm::OclImplies_strategy = st.builds(
    umm::OclImplies,
)
umm::OclEqual_strategy = st.builds(
    umm::OclEqual,
)
umm::OclValue_strategy = st.builds(
    umm::OclValue,
)
umm::OclExpression_strategy = st.builds(
    umm::OclExpression,
)
umm::CDT_strategy = st.builds(
    umm::CDT,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    versionIdentifier=
        safe_text,
    name=
        safe_text,
    definition=
        safe_text,
    dictionary=
        safe_text
)
umm::CodelistEntry_strategy = st.builds(
    umm::CodelistEntry,
    description=
        safe_text,
    name=
        safe_text
)
ACCProperty_strategy = st.builds(
    ACCProperty,
)
umm::BCC_strategy = st.builds(
    umm::BCC,
    restriction=
        safe_text,
    fixedValue=
        safe_text
)
umm::ASCC_strategy = st.builds(
    umm::ASCC,
)
umm::ACCProperty_strategy = st.builds(
    umm::ACCProperty,
    versionIdentifier=
        safe_text,
    uniqueIdentifier=
        safe_text,
    sequencingKey=
        safe_text,
    businessTerm=
        safe_text,
    multiplicity=
        safe_text,
    name=
        safe_text,
    dictionary=
        safe_text,
    definition=
        safe_text
)
umm::ACC_strategy = st.builds(
    umm::ACC,
    uniqueIdentifier=
        safe_text,
    dictionary=
        safe_text,
    businessTerm=
        safe_text,
    versionIdentifier=
        safe_text,
    name=
        safe_text,
    definition=
        safe_text
)
BDTProperty_strategy = st.builds(
    BDTProperty,
)
umm::Supplement_strategy = st.builds(
    umm::Supplement,
    restriction=
        safe_text,
    fixedValue=
        safe_text,
    defaultValue=
        safe_text
)
umm::Content_strategy = st.builds(
    umm::Content,
    minInclusive=
        st.integers(),
    fractionalDigits=
        st.integers(),
    minExclusive=
        st.integers(),
    maxInclusive=
        st.integers(),
    maxExclusive=
        st.integers(),
    totalDigits=
        st.integers()
)
AssembledBase_strategy = st.builds(
    AssembledBase,
)
umm::Assembled_strategy = st.builds(
    umm::Assembled,
)
umm::Primitive_strategy = st.builds(
    umm::Primitive,
)
ENUM_strategy = st.builds(
    ENUM,
)
umm::Subset_strategy = st.builds(
    umm::Subset,
)
umm::AssembledBase_strategy = st.builds(
    umm::AssembledBase,
)
umm::Original_strategy = st.builds(
    umm::Original,
)
umm::ENUM_strategy = st.builds(
    umm::ENUM,
    definition=
        safe_text,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    codeListAgencyIdentifier=
        safe_text,
    name=
        safe_text,
    versionIdentifier=
        safe_text,
    dictionary=
        safe_text,
    codeListName=
        safe_text,
    codeListIdentifier=
        safe_text
)
ABIEProperty_strategy = st.builds(
    ABIEProperty,
)
umm::BBIE_strategy = st.builds(
    umm::BBIE,
    fixedValue=
        safe_text,
    restriction=
        safe_text
)
umm::ASBIE_strategy = st.builds(
    umm::ASBIE,
)
umm::OclInvariant_strategy = st.builds(
    umm::OclInvariant,
)
umm::TC::Constraint_strategy = st.builds(
    umm::TC::Constraint,
    responsibleAgency=
        safe_text,
    kind=
        safe_text,
    listIdentifier=
        safe_text
)
umm::ContextRef_strategy = st.builds(
    umm::ContextRef,
    name=
        safe_text
)
MAProperty_strategy = st.builds(
    MAProperty,
)
umm::ASNONE_strategy = st.builds(
    umm::ASNONE,
)
umm::ASMA_strategy = st.builds(
    umm::ASMA,
)
OclRef_strategy = st.builds(
    OclRef,
)
umm::BDTProperty_strategy = st.builds(
    umm::BDTProperty,
    length=
        st.integers(),
    pattern=
        safe_text,
    versionIdentifier=
        safe_text,
    definition=
        safe_text,
    maxLength=
        st.integers(),
    dictionary=
        safe_text,
    businessTerm=
        safe_text,
    minLength=
        st.integers(),
    uniqueIdentifier=
        safe_text
)
umm::ABIEProperty_strategy = st.builds(
    umm::ABIEProperty,
    definition=
        safe_text,
    businessTerm=
        safe_text,
    dictionary=
        safe_text,
    versionIdentifier=
        safe_text,
    sequencingKey=
        safe_text,
    uniqueIdentifier=
        safe_text
)
Library_strategy = st.builds(
    Library,
)
umm::CDTLibrary_strategy = st.builds(
    umm::CDTLibrary,
    baseURN=
        safe_text,
    versionIdentifier=
        safe_text,
    uniqueIdentifier=
        safe_text,
    reference=
        safe_text,
    copyright=
        safe_text,
    businessTerm=
        safe_text,
    owner=
        safe_text,
    namespacePrefix=
        safe_text
)
umm::CCLibrary_strategy = st.builds(
    umm::CCLibrary,
    copyright=
        safe_text,
    versionIdentifier=
        safe_text,
    baseURN=
        safe_text,
    businessTerm=
        safe_text,
    namespacePrefix=
        safe_text,
    owner=
        safe_text,
    reference=
        safe_text,
    uniqueIdentifier=
        safe_text
)
umm::PrimitiveLibrary_strategy = st.builds(
    umm::PrimitiveLibrary,
)
umm::ENUMLibrary_strategy = st.builds(
    umm::ENUMLibrary,
    copyright=
        safe_text,
    businessTerm=
        safe_text,
    reference=
        safe_text,
    versionIdentifier=
        safe_text,
    baseURN=
        safe_text,
    owner=
        safe_text,
    namespacePrefix=
        safe_text,
    uniqueIdentifier=
        safe_text
)
umm::DocLibrary_strategy = st.builds(
    umm::DocLibrary,
    reference=
        safe_text,
    copyright=
        safe_text,
    namespacePrefix=
        safe_text,
    baseURN=
        safe_text,
    versionIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    owner=
        safe_text,
    uniqueIdentifier=
        safe_text
)
umm::Library_strategy = st.builds(
    umm::Library,
    name=
        safe_text
)
umm::Constraint_strategy = st.builds(
    umm::Constraint,
)
umm::MAProperty_strategy = st.builds(
    umm::MAProperty,
)
ContextRef_strategy = st.builds(
    ContextRef,
)
umm::ABIE_strategy = st.builds(
    umm::ABIE,
    versionIdentifier=
        safe_text,
    definition=
        safe_text,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    dictionary=
        safe_text
)
umm::BDT_strategy = st.builds(
    umm::BDT,
    versionIdentifier=
        safe_text,
    dictionary=
        safe_text,
    businessTerm=
        safe_text,
    uniqueIdentifier=
        safe_text,
    definition=
        safe_text
)
umm::MA_strategy = st.builds(
    umm::MA,
)
umm::InfEnvelope_strategy = st.builds(
    umm::InfEnvelope,
    name=
        safe_text
)
umm::BDTLibrary_strategy = st.builds(
    umm::BDTLibrary,
    reference=
        safe_text,
    copyright=
        safe_text,
    uniqueIdentifier=
        safe_text,
    baseURN=
        safe_text,
    businessTerm=
        safe_text,
    namespacePrefix=
        safe_text,
    owner=
        safe_text,
    versionIdentifier=
        safe_text
)
umm::BIELibrary_strategy = st.builds(
    umm::BIELibrary,
    reference=
        safe_text,
    copyright=
        safe_text,
    owner=
        safe_text,
    versionIdentifier=
        safe_text,
    namespacePrefix=
        safe_text,
    uniqueIdentifier=
        safe_text,
    businessTerm=
        safe_text,
    baseURN=
        safe_text
)

@given(instance=OclLiteral_strategy)
@settings(max_examples=50)
def test_oclliteral_instantiation(instance):
    assert isinstance(instance, OclLiteral)

@given(instance=umm::OclStringLiteral_strategy)
@settings(max_examples=50)
def test_umm::oclstringliteral_instantiation(instance):
    assert isinstance(instance, umm::OclStringLiteral)

@given(instance=umm::OclStringLiteral_strategy)
def test_umm::oclstringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=umm::OclStringLiteral_strategy)
def test_umm::oclstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=umm::OclIntegerLiteral_strategy)
@settings(max_examples=50)
def test_umm::oclintegerliteral_instantiation(instance):
    assert isinstance(instance, umm::OclIntegerLiteral)

@given(instance=umm::OclIntegerLiteral_strategy)
def test_umm::oclintegerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=umm::OclIntegerLiteral_strategy)
def test_umm::oclintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=umm::OclBooleanLiteral_strategy)
@settings(max_examples=50)
def test_umm::oclbooleanliteral_instantiation(instance):
    assert isinstance(instance, umm::OclBooleanLiteral)

@given(instance=umm::OclEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umm::oclenumerationliteral_instantiation(instance):
    assert isinstance(instance, umm::OclEnumerationLiteral)

@given(instance=umm::OclEnumerationLiteral_strategy)
def test_umm::oclenumerationliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=umm::OclEnumerationLiteral_strategy)
def test_umm::oclenumerationliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OclFunctionCall_strategy)
@settings(max_examples=50)
def test_oclfunctioncall_instantiation(instance):
    assert isinstance(instance, OclFunctionCall)

@given(instance=umm::OclSize_strategy)
@settings(max_examples=50)
def test_umm::oclsize_instantiation(instance):
    assert isinstance(instance, umm::OclSize)

@given(instance=umm::OclNotEmpty_strategy)
@settings(max_examples=50)
def test_umm::oclnotempty_instantiation(instance):
    assert isinstance(instance, umm::OclNotEmpty)

@given(instance=umm::OclIsEmpty_strategy)
@settings(max_examples=50)
def test_umm::oclisempty_instantiation(instance):
    assert isinstance(instance, umm::OclIsEmpty)

@given(instance=umm::OclForAll_strategy)
@settings(max_examples=50)
def test_umm::oclforall_instantiation(instance):
    assert isinstance(instance, umm::OclForAll)

@given(instance=umm::OclFunctionCall_strategy)
@settings(max_examples=50)
def test_umm::oclfunctioncall_instantiation(instance):
    assert isinstance(instance, umm::OclFunctionCall)

@given(instance=OclBooleanLiteral_strategy)
@settings(max_examples=50)
def test_oclbooleanliteral_instantiation(instance):
    assert isinstance(instance, OclBooleanLiteral)

@given(instance=umm::OclBooleanTrue_strategy)
@settings(max_examples=50)
def test_umm::oclbooleantrue_instantiation(instance):
    assert isinstance(instance, umm::OclBooleanTrue)

@given(instance=umm::OclBooleanFalse_strategy)
@settings(max_examples=50)
def test_umm::oclbooleanfalse_instantiation(instance):
    assert isinstance(instance, umm::OclBooleanFalse)

@given(instance=CDTProperty_strategy)
@settings(max_examples=50)
def test_cdtproperty_instantiation(instance):
    assert isinstance(instance, CDTProperty)

@given(instance=umm::CDT::Supplement_strategy)
@settings(max_examples=50)
def test_umm::cdt::supplement_instantiation(instance):
    assert isinstance(instance, umm::CDT::Supplement)

@given(instance=umm::CDT::Supplement_strategy)
def test_umm::cdt::supplement_fixedValue_type(instance):
    assert isinstance(instance.fixedValue, str)


@given(instance=umm::CDT::Supplement_strategy)
def test_umm::cdt::supplement_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original

@given(instance=umm::CDT::Supplement_strategy)
def test_umm::cdt::supplement_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=umm::CDT::Supplement_strategy)
def test_umm::cdt::supplement_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=umm::CDT::Supplement_strategy)
def test_umm::cdt::supplement_restriction_type(instance):
    assert isinstance(instance.restriction, str)


@given(instance=umm::CDT::Supplement_strategy)
def test_umm::cdt::supplement_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=umm::CDT::Content_strategy)
@settings(max_examples=50)
def test_umm::cdt::content_instantiation(instance):
    assert isinstance(instance, umm::CDT::Content)

@given(instance=umm::CDTProperty_strategy)
@settings(max_examples=50)
def test_umm::cdtproperty_instantiation(instance):
    assert isinstance(instance, umm::CDTProperty)

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=umm::CDTProperty_strategy)
def test_umm::cdtproperty_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=umm::OclRef_strategy)
@settings(max_examples=50)
def test_umm::oclref_instantiation(instance):
    assert isinstance(instance, umm::OclRef)

@given(instance=umm::OclRef_strategy)
def test_umm::oclref_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=umm::OclRef_strategy)
def test_umm::oclref_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=umm::OclRef_strategy)
def test_umm::oclref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::OclRef_strategy)
def test_umm::oclref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::OclPathTail_strategy)
@settings(max_examples=50)
def test_umm::oclpathtail_instantiation(instance):
    assert isinstance(instance, umm::OclPathTail)

@given(instance=OclReference_strategy)
@settings(max_examples=50)
def test_oclreference_instantiation(instance):
    assert isinstance(instance, OclReference)

@given(instance=umm::OclPathFeatureHead_strategy)
@settings(max_examples=50)
def test_umm::oclpathfeaturehead_instantiation(instance):
    assert isinstance(instance, umm::OclPathFeatureHead)

@given(instance=umm::OclPathSelfHead_strategy)
@settings(max_examples=50)
def test_umm::oclpathselfhead_instantiation(instance):
    assert isinstance(instance, umm::OclPathSelfHead)

@given(instance=OclValue_strategy)
@settings(max_examples=50)
def test_oclvalue_instantiation(instance):
    assert isinstance(instance, OclValue)

@given(instance=umm::OclLiteral_strategy)
@settings(max_examples=50)
def test_umm::oclliteral_instantiation(instance):
    assert isinstance(instance, umm::OclLiteral)

@given(instance=umm::OclReference_strategy)
@settings(max_examples=50)
def test_umm::oclreference_instantiation(instance):
    assert isinstance(instance, umm::OclReference)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=umm::OclLessOrEqual_strategy)
@settings(max_examples=50)
def test_umm::ocllessorequal_instantiation(instance):
    assert isinstance(instance, umm::OclLessOrEqual)

@given(instance=umm::OclAnd_strategy)
@settings(max_examples=50)
def test_umm::ocland_instantiation(instance):
    assert isinstance(instance, umm::OclAnd)

@given(instance=umm::OclLess_strategy)
@settings(max_examples=50)
def test_umm::oclless_instantiation(instance):
    assert isinstance(instance, umm::OclLess)

@given(instance=umm::OclMore_strategy)
@settings(max_examples=50)
def test_umm::oclmore_instantiation(instance):
    assert isinstance(instance, umm::OclMore)

@given(instance=umm::OclMoreOrEqual_strategy)
@settings(max_examples=50)
def test_umm::oclmoreorequal_instantiation(instance):
    assert isinstance(instance, umm::OclMoreOrEqual)

@given(instance=umm::OclXor_strategy)
@settings(max_examples=50)
def test_umm::oclxor_instantiation(instance):
    assert isinstance(instance, umm::OclXor)

@given(instance=umm::OclOr_strategy)
@settings(max_examples=50)
def test_umm::oclor_instantiation(instance):
    assert isinstance(instance, umm::OclOr)

@given(instance=umm::OclArrow_strategy)
@settings(max_examples=50)
def test_umm::oclarrow_instantiation(instance):
    assert isinstance(instance, umm::OclArrow)

@given(instance=umm::OclImplies_strategy)
@settings(max_examples=50)
def test_umm::oclimplies_instantiation(instance):
    assert isinstance(instance, umm::OclImplies)

@given(instance=umm::OclEqual_strategy)
@settings(max_examples=50)
def test_umm::oclequal_instantiation(instance):
    assert isinstance(instance, umm::OclEqual)

@given(instance=umm::OclValue_strategy)
@settings(max_examples=50)
def test_umm::oclvalue_instantiation(instance):
    assert isinstance(instance, umm::OclValue)

@given(instance=umm::OclExpression_strategy)
@settings(max_examples=50)
def test_umm::oclexpression_instantiation(instance):
    assert isinstance(instance, umm::OclExpression)

@given(instance=umm::CDT_strategy)
@settings(max_examples=50)
def test_umm::cdt_instantiation(instance):
    assert isinstance(instance, umm::CDT)

@given(instance=umm::CDT_strategy)
def test_umm::cdt_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::CDT_strategy)
def test_umm::cdt_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::CDT_strategy)
def test_umm::cdt_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::CDT_strategy)
def test_umm::cdt_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::CDT_strategy)
def test_umm::cdt_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::CDT_strategy)
def test_umm::cdt_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::CDT_strategy)
def test_umm::cdt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::CDT_strategy)
def test_umm::cdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::CDT_strategy)
def test_umm::cdt_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::CDT_strategy)
def test_umm::cdt_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::CDT_strategy)
def test_umm::cdt_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::CDT_strategy)
def test_umm::cdt_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::CodelistEntry_strategy)
@settings(max_examples=50)
def test_umm::codelistentry_instantiation(instance):
    assert isinstance(instance, umm::CodelistEntry)

@given(instance=umm::CodelistEntry_strategy)
def test_umm::codelistentry_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=umm::CodelistEntry_strategy)
def test_umm::codelistentry_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=umm::CodelistEntry_strategy)
def test_umm::codelistentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::CodelistEntry_strategy)
def test_umm::codelistentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACCProperty_strategy)
@settings(max_examples=50)
def test_accproperty_instantiation(instance):
    assert isinstance(instance, ACCProperty)

@given(instance=umm::BCC_strategy)
@settings(max_examples=50)
def test_umm::bcc_instantiation(instance):
    assert isinstance(instance, umm::BCC)

@given(instance=umm::BCC_strategy)
def test_umm::bcc_restriction_type(instance):
    assert isinstance(instance.restriction, str)


@given(instance=umm::BCC_strategy)
def test_umm::bcc_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=umm::BCC_strategy)
def test_umm::bcc_fixedValue_type(instance):
    assert isinstance(instance.fixedValue, str)


@given(instance=umm::BCC_strategy)
def test_umm::bcc_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original

@given(instance=umm::ASCC_strategy)
@settings(max_examples=50)
def test_umm::ascc_instantiation(instance):
    assert isinstance(instance, umm::ASCC)

@given(instance=umm::ACCProperty_strategy)
@settings(max_examples=50)
def test_umm::accproperty_instantiation(instance):
    assert isinstance(instance, umm::ACCProperty)

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_sequencingKey_type(instance):
    assert isinstance(instance.sequencingKey, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_sequencingKey_setter(instance):
    original = instance.sequencingKey
    instance.sequencingKey = original
    assert instance.sequencingKey == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::ACCProperty_strategy)
def test_umm::accproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::ACC_strategy)
@settings(max_examples=50)
def test_umm::acc_instantiation(instance):
    assert isinstance(instance, umm::ACC)

@given(instance=umm::ACC_strategy)
def test_umm::acc_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::ACC_strategy)
def test_umm::acc_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::ACC_strategy)
def test_umm::acc_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::ACC_strategy)
def test_umm::acc_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::ACC_strategy)
def test_umm::acc_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::ACC_strategy)
def test_umm::acc_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::ACC_strategy)
def test_umm::acc_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::ACC_strategy)
def test_umm::acc_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::ACC_strategy)
def test_umm::acc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::ACC_strategy)
def test_umm::acc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::ACC_strategy)
def test_umm::acc_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::ACC_strategy)
def test_umm::acc_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=BDTProperty_strategy)
@settings(max_examples=50)
def test_bdtproperty_instantiation(instance):
    assert isinstance(instance, BDTProperty)

@given(instance=umm::Supplement_strategy)
@settings(max_examples=50)
def test_umm::supplement_instantiation(instance):
    assert isinstance(instance, umm::Supplement)

@given(instance=umm::Supplement_strategy)
def test_umm::supplement_restriction_type(instance):
    assert isinstance(instance.restriction, str)


@given(instance=umm::Supplement_strategy)
def test_umm::supplement_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=umm::Supplement_strategy)
def test_umm::supplement_fixedValue_type(instance):
    assert isinstance(instance.fixedValue, str)


@given(instance=umm::Supplement_strategy)
def test_umm::supplement_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original

@given(instance=umm::Supplement_strategy)
def test_umm::supplement_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=umm::Supplement_strategy)
def test_umm::supplement_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=umm::Content_strategy)
@settings(max_examples=50)
def test_umm::content_instantiation(instance):
    assert isinstance(instance, umm::Content)

@given(instance=umm::Content_strategy)
def test_umm::content_minInclusive_type(instance):
    assert isinstance(instance.minInclusive, int)


@given(instance=umm::Content_strategy)
def test_umm::content_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original

@given(instance=umm::Content_strategy)
def test_umm::content_fractionalDigits_type(instance):
    assert isinstance(instance.fractionalDigits, int)


@given(instance=umm::Content_strategy)
def test_umm::content_fractionalDigits_setter(instance):
    original = instance.fractionalDigits
    instance.fractionalDigits = original
    assert instance.fractionalDigits == original

@given(instance=umm::Content_strategy)
def test_umm::content_minExclusive_type(instance):
    assert isinstance(instance.minExclusive, int)


@given(instance=umm::Content_strategy)
def test_umm::content_minExclusive_setter(instance):
    original = instance.minExclusive
    instance.minExclusive = original
    assert instance.minExclusive == original

@given(instance=umm::Content_strategy)
def test_umm::content_maxInclusive_type(instance):
    assert isinstance(instance.maxInclusive, int)


@given(instance=umm::Content_strategy)
def test_umm::content_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original

@given(instance=umm::Content_strategy)
def test_umm::content_maxExclusive_type(instance):
    assert isinstance(instance.maxExclusive, int)


@given(instance=umm::Content_strategy)
def test_umm::content_maxExclusive_setter(instance):
    original = instance.maxExclusive
    instance.maxExclusive = original
    assert instance.maxExclusive == original

@given(instance=umm::Content_strategy)
def test_umm::content_totalDigits_type(instance):
    assert isinstance(instance.totalDigits, int)


@given(instance=umm::Content_strategy)
def test_umm::content_totalDigits_setter(instance):
    original = instance.totalDigits
    instance.totalDigits = original
    assert instance.totalDigits == original

@given(instance=AssembledBase_strategy)
@settings(max_examples=50)
def test_assembledbase_instantiation(instance):
    assert isinstance(instance, AssembledBase)

@given(instance=umm::Assembled_strategy)
@settings(max_examples=50)
def test_umm::assembled_instantiation(instance):
    assert isinstance(instance, umm::Assembled)

@given(instance=umm::Primitive_strategy)
@settings(max_examples=50)
def test_umm::primitive_instantiation(instance):
    assert isinstance(instance, umm::Primitive)

@given(instance=ENUM_strategy)
@settings(max_examples=50)
def test_enum_instantiation(instance):
    assert isinstance(instance, ENUM)

@given(instance=umm::Subset_strategy)
@settings(max_examples=50)
def test_umm::subset_instantiation(instance):
    assert isinstance(instance, umm::Subset)

@given(instance=umm::AssembledBase_strategy)
@settings(max_examples=50)
def test_umm::assembledbase_instantiation(instance):
    assert isinstance(instance, umm::AssembledBase)

@given(instance=umm::Original_strategy)
@settings(max_examples=50)
def test_umm::original_instantiation(instance):
    assert isinstance(instance, umm::Original)

@given(instance=umm::ENUM_strategy)
@settings(max_examples=50)
def test_umm::enum_instantiation(instance):
    assert isinstance(instance, umm::ENUM)

@given(instance=umm::ENUM_strategy)
def test_umm::enum_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_codeListAgencyIdentifier_type(instance):
    assert isinstance(instance.codeListAgencyIdentifier, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_codeListAgencyIdentifier_setter(instance):
    original = instance.codeListAgencyIdentifier
    instance.codeListAgencyIdentifier = original
    assert instance.codeListAgencyIdentifier == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_codeListName_type(instance):
    assert isinstance(instance.codeListName, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_codeListName_setter(instance):
    original = instance.codeListName
    instance.codeListName = original
    assert instance.codeListName == original

@given(instance=umm::ENUM_strategy)
def test_umm::enum_codeListIdentifier_type(instance):
    assert isinstance(instance.codeListIdentifier, str)


@given(instance=umm::ENUM_strategy)
def test_umm::enum_codeListIdentifier_setter(instance):
    original = instance.codeListIdentifier
    instance.codeListIdentifier = original
    assert instance.codeListIdentifier == original

@given(instance=ABIEProperty_strategy)
@settings(max_examples=50)
def test_abieproperty_instantiation(instance):
    assert isinstance(instance, ABIEProperty)

@given(instance=umm::BBIE_strategy)
@settings(max_examples=50)
def test_umm::bbie_instantiation(instance):
    assert isinstance(instance, umm::BBIE)

@given(instance=umm::BBIE_strategy)
def test_umm::bbie_fixedValue_type(instance):
    assert isinstance(instance.fixedValue, str)


@given(instance=umm::BBIE_strategy)
def test_umm::bbie_fixedValue_setter(instance):
    original = instance.fixedValue
    instance.fixedValue = original
    assert instance.fixedValue == original

@given(instance=umm::BBIE_strategy)
def test_umm::bbie_restriction_type(instance):
    assert isinstance(instance.restriction, str)


@given(instance=umm::BBIE_strategy)
def test_umm::bbie_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=umm::ASBIE_strategy)
@settings(max_examples=50)
def test_umm::asbie_instantiation(instance):
    assert isinstance(instance, umm::ASBIE)

@given(instance=umm::OclInvariant_strategy)
@settings(max_examples=50)
def test_umm::oclinvariant_instantiation(instance):
    assert isinstance(instance, umm::OclInvariant)

@given(instance=umm::TC::Constraint_strategy)
@settings(max_examples=50)
def test_umm::tc::constraint_instantiation(instance):
    assert isinstance(instance, umm::TC::Constraint)

@given(instance=umm::TC::Constraint_strategy)
def test_umm::tc::constraint_responsibleAgency_type(instance):
    assert isinstance(instance.responsibleAgency, str)


@given(instance=umm::TC::Constraint_strategy)
def test_umm::tc::constraint_responsibleAgency_setter(instance):
    original = instance.responsibleAgency
    instance.responsibleAgency = original
    assert instance.responsibleAgency == original

@given(instance=umm::TC::Constraint_strategy)
def test_umm::tc::constraint_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umm::TC::Constraint_strategy)
def test_umm::tc::constraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umm::TC::Constraint_strategy)
def test_umm::tc::constraint_listIdentifier_type(instance):
    assert isinstance(instance.listIdentifier, str)


@given(instance=umm::TC::Constraint_strategy)
def test_umm::tc::constraint_listIdentifier_setter(instance):
    original = instance.listIdentifier
    instance.listIdentifier = original
    assert instance.listIdentifier == original

@given(instance=umm::ContextRef_strategy)
@settings(max_examples=50)
def test_umm::contextref_instantiation(instance):
    assert isinstance(instance, umm::ContextRef)

@given(instance=umm::ContextRef_strategy)
def test_umm::contextref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::ContextRef_strategy)
def test_umm::contextref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MAProperty_strategy)
@settings(max_examples=50)
def test_maproperty_instantiation(instance):
    assert isinstance(instance, MAProperty)

@given(instance=umm::ASNONE_strategy)
@settings(max_examples=50)
def test_umm::asnone_instantiation(instance):
    assert isinstance(instance, umm::ASNONE)

@given(instance=umm::ASMA_strategy)
@settings(max_examples=50)
def test_umm::asma_instantiation(instance):
    assert isinstance(instance, umm::ASMA)

@given(instance=OclRef_strategy)
@settings(max_examples=50)
def test_oclref_instantiation(instance):
    assert isinstance(instance, OclRef)

@given(instance=umm::BDTProperty_strategy)
@settings(max_examples=50)
def test_umm::bdtproperty_instantiation(instance):
    assert isinstance(instance, umm::BDTProperty)

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_maxLength_type(instance):
    assert isinstance(instance.maxLength, int)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_minLength_type(instance):
    assert isinstance(instance.minLength, int)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original

@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::BDTProperty_strategy)
def test_umm::bdtproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::ABIEProperty_strategy)
@settings(max_examples=50)
def test_umm::abieproperty_instantiation(instance):
    assert isinstance(instance, umm::ABIEProperty)

@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_sequencingKey_type(instance):
    assert isinstance(instance.sequencingKey, str)


@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_sequencingKey_setter(instance):
    original = instance.sequencingKey
    instance.sequencingKey = original
    assert instance.sequencingKey == original

@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::ABIEProperty_strategy)
def test_umm::abieproperty_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=umm::CDTLibrary_strategy)
@settings(max_examples=50)
def test_umm::cdtlibrary_instantiation(instance):
    assert isinstance(instance, umm::CDTLibrary)

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_baseURN_type(instance):
    assert isinstance(instance.baseURN, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_namespacePrefix_type(instance):
    assert isinstance(instance.namespacePrefix, str)


@given(instance=umm::CDTLibrary_strategy)
def test_umm::cdtlibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original

@given(instance=umm::CCLibrary_strategy)
@settings(max_examples=50)
def test_umm::cclibrary_instantiation(instance):
    assert isinstance(instance, umm::CCLibrary)

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_baseURN_type(instance):
    assert isinstance(instance.baseURN, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_namespacePrefix_type(instance):
    assert isinstance(instance.namespacePrefix, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::CCLibrary_strategy)
def test_umm::cclibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::PrimitiveLibrary_strategy)
@settings(max_examples=50)
def test_umm::primitivelibrary_instantiation(instance):
    assert isinstance(instance, umm::PrimitiveLibrary)

@given(instance=umm::ENUMLibrary_strategy)
@settings(max_examples=50)
def test_umm::enumlibrary_instantiation(instance):
    assert isinstance(instance, umm::ENUMLibrary)

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_baseURN_type(instance):
    assert isinstance(instance.baseURN, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_namespacePrefix_type(instance):
    assert isinstance(instance.namespacePrefix, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original

@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::ENUMLibrary_strategy)
def test_umm::enumlibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::DocLibrary_strategy)
@settings(max_examples=50)
def test_umm::doclibrary_instantiation(instance):
    assert isinstance(instance, umm::DocLibrary)

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_namespacePrefix_type(instance):
    assert isinstance(instance.namespacePrefix, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_baseURN_type(instance):
    assert isinstance(instance.baseURN, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::DocLibrary_strategy)
def test_umm::doclibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::Library_strategy)
@settings(max_examples=50)
def test_umm::library_instantiation(instance):
    assert isinstance(instance, umm::Library)

@given(instance=umm::Library_strategy)
def test_umm::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::Library_strategy)
def test_umm::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::Constraint_strategy)
@settings(max_examples=50)
def test_umm::constraint_instantiation(instance):
    assert isinstance(instance, umm::Constraint)

@given(instance=umm::MAProperty_strategy)
@settings(max_examples=50)
def test_umm::maproperty_instantiation(instance):
    assert isinstance(instance, umm::MAProperty)

@given(instance=ContextRef_strategy)
@settings(max_examples=50)
def test_contextref_instantiation(instance):
    assert isinstance(instance, ContextRef)

@given(instance=umm::ABIE_strategy)
@settings(max_examples=50)
def test_umm::abie_instantiation(instance):
    assert isinstance(instance, umm::ABIE)

@given(instance=umm::ABIE_strategy)
def test_umm::abie_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::ABIE_strategy)
def test_umm::abie_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::ABIE_strategy)
def test_umm::abie_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::ABIE_strategy)
def test_umm::abie_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::ABIE_strategy)
def test_umm::abie_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::ABIE_strategy)
def test_umm::abie_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::ABIE_strategy)
def test_umm::abie_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::ABIE_strategy)
def test_umm::abie_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::ABIE_strategy)
def test_umm::abie_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::ABIE_strategy)
def test_umm::abie_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::BDT_strategy)
@settings(max_examples=50)
def test_umm::bdt_instantiation(instance):
    assert isinstance(instance, umm::BDT)

@given(instance=umm::BDT_strategy)
def test_umm::bdt_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::BDT_strategy)
def test_umm::bdt_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::BDT_strategy)
def test_umm::bdt_dictionary_type(instance):
    assert isinstance(instance.dictionary, str)


@given(instance=umm::BDT_strategy)
def test_umm::bdt_dictionary_setter(instance):
    original = instance.dictionary
    instance.dictionary = original
    assert instance.dictionary == original

@given(instance=umm::BDT_strategy)
def test_umm::bdt_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::BDT_strategy)
def test_umm::bdt_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::BDT_strategy)
def test_umm::bdt_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::BDT_strategy)
def test_umm::bdt_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::BDT_strategy)
def test_umm::bdt_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=umm::BDT_strategy)
def test_umm::bdt_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=umm::MA_strategy)
@settings(max_examples=50)
def test_umm::ma_instantiation(instance):
    assert isinstance(instance, umm::MA)

@given(instance=umm::InfEnvelope_strategy)
@settings(max_examples=50)
def test_umm::infenvelope_instantiation(instance):
    assert isinstance(instance, umm::InfEnvelope)

@given(instance=umm::InfEnvelope_strategy)
def test_umm::infenvelope_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umm::InfEnvelope_strategy)
def test_umm::infenvelope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umm::BDTLibrary_strategy)
@settings(max_examples=50)
def test_umm::bdtlibrary_instantiation(instance):
    assert isinstance(instance, umm::BDTLibrary)

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_baseURN_type(instance):
    assert isinstance(instance.baseURN, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_namespacePrefix_type(instance):
    assert isinstance(instance.namespacePrefix, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::BDTLibrary_strategy)
def test_umm::bdtlibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::BIELibrary_strategy)
@settings(max_examples=50)
def test_umm::bielibrary_instantiation(instance):
    assert isinstance(instance, umm::BIELibrary)

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_versionIdentifier_type(instance):
    assert isinstance(instance.versionIdentifier, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_versionIdentifier_setter(instance):
    original = instance.versionIdentifier
    instance.versionIdentifier = original
    assert instance.versionIdentifier == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_namespacePrefix_type(instance):
    assert isinstance(instance.namespacePrefix, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_namespacePrefix_setter(instance):
    original = instance.namespacePrefix
    instance.namespacePrefix = original
    assert instance.namespacePrefix == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_uniqueIdentifier_type(instance):
    assert isinstance(instance.uniqueIdentifier, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_uniqueIdentifier_setter(instance):
    original = instance.uniqueIdentifier
    instance.uniqueIdentifier = original
    assert instance.uniqueIdentifier == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_businessTerm_type(instance):
    assert isinstance(instance.businessTerm, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_businessTerm_setter(instance):
    original = instance.businessTerm
    instance.businessTerm = original
    assert instance.businessTerm == original

@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_baseURN_type(instance):
    assert isinstance(instance.baseURN, str)


@given(instance=umm::BIELibrary_strategy)
def test_umm::bielibrary_baseURN_setter(instance):
    original = instance.baseURN
    instance.baseURN = original
    assert instance.baseURN == original
