import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xal_LargeMailUserIdentifier,
    xal_LargeMailUserName,
    xal_KeyLineCode,
    xal_EndorsementLineCode,
    xal_Xal,
    xal_FirmName,
    xal_Firm,
    xal_PremiseNumberSuffix,
    xal_PremiseNumberPrefix,
    xal_PremiseNumber,
    xal_ThoroughfareNumberSuffix,
    xal_ThoroughfareNumberPrefix,
    xal_ThoroughfareNumber,
    xal_DocumentRoot,
    xal_EStringToStringMapEntry,
    xal_ThoroughfarePreDirection,
    xal_DependentThoroughfare,
    xal_ThoroughfarePostDirection,
    xal_ThoroughfareTrailingType,
    xal_ThoroughfareName,
    xal_ThoroughfareLeadingType,
    xal_PostalRoute,
    xal_LargeMailUser,
    xal_Premise,
    xal_PostBox,
    xal_DependentLocalityNumber,
    xal_DependentLocalityName,
    xal_DependentLocality,
    xal_MailStop,
    xal_DepartmentName,
    xal_Department,
    xal_CountryName,
    xal_CountryNameCode,
    xal_Barcode,
    xal_BuildingName,
    xal_PostalCode,
    xal_PostOffice,
    xal_AddressLongitudeDirection,
    xal_SubAdministrativeArea,
    xal_AdministrativeAreaName,
    xal_AddressLine,
    xal_AddressLongitude,
    xal_AddressLatitude,
    xal_AddressLatitudeDirection,
    xal_AddressIdentifier,
    xal_AddressLines,
    xal_Thoroughfare,
    xal_Locality,
    xal_AdministrativeArea,
    xal_Country,
    xal_PostalServiceElements,
    xal_AddressDetails,
    xal_Address,
    xal_ThoroughfareNumberTo,
    xal_ThoroughfareNumberFrom,
    xal_ThoroughfareNumberRange,
    xal_SubPremiseNumberPrefix,
    xal_SubPremiseNumber,
    xal_SubPremiseNumberSuffix,
    xal_SubPremiseLocation,
    xal_SubPremiseName,
    xal_SubAdministrativeAreaName,
    xal_PremiseNumberRangeTo,
    xal_PremiseNumberRangeFrom,
    xal_SubPremise,
    xal_PremiseName,
    xal_PremiseNumberRange,
    xal_PremiseLocation,
    xal_PostTownSuffix,
    xal_PostTownName,
    xal_PostOfficeNumber,
    xal_PostOfficeName,
    xal_PostBoxNumberExtension,
    xal_PostBoxNumberSuffix,
    xal_PostBoxNumberPrefix,
    xal_SupplementaryPostalServiceData,
    xal_PostBoxNumber,
    xal_SortingCode,
    xal_PostalRouteNumber,
    xal_PostalRouteName,
    xal_PostalCodeNumberExtension,
    xal_PostalCodeNumber,
    xal_PostTown,
    xal_MailStopNumber,
    xal_MailStopName,
    xal_LocalityName,
    RangeTypeType,
    IndicatorOccurrence4,
    NumberTypeType1,
    TypeOccurrence,
    TypeOccurrence2,
    NameNumberOccurrence,
    IndicatorOccurence,
    NumberOccurrence,
    NumberTypeOccurrence,
    NumberTypeOccurrence1,
    IndicatorOccurrence,
    IndicatorOccurrence2,
    NumberRangeOccurrence,
    NumberRangeOccurence,
    TypeOccurrence1,
    DependentThoroughfaresType,
    IndicatorOccurrence1,
    NumberTypeType,
    IndicatorOccurrence3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xal_largemailuseridentifier_is_not_abstract():
    assert not inspect.isabstract(xal_LargeMailUserIdentifier)


def test_xal_largemailuseridentifier_constructor_exists():
    assert callable(xal_LargeMailUserIdentifier.__init__)


def test_xal_largemailuseridentifier_constructor_args():
    sig = inspect.signature(xal_LargeMailUserIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_largemailuseridentifier_has_code():
    assert hasattr(xal_LargeMailUserIdentifier, "code")
    descriptor = None
    for klass in xal_LargeMailUserIdentifier.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailuseridentifier_has_type():
    assert hasattr(xal_LargeMailUserIdentifier, "type")
    descriptor = None
    for klass in xal_LargeMailUserIdentifier.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailuseridentifier_has_anyAttribute():
    assert hasattr(xal_LargeMailUserIdentifier, "anyAttribute")
    descriptor = None
    for klass in xal_LargeMailUserIdentifier.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailuseridentifier_has_indicator():
    assert hasattr(xal_LargeMailUserIdentifier, "indicator")
    descriptor = None
    for klass in xal_LargeMailUserIdentifier.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailuseridentifier_has_mixed():
    assert hasattr(xal_LargeMailUserIdentifier, "mixed")
    descriptor = None
    for klass in xal_LargeMailUserIdentifier.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_largemailusername_is_not_abstract():
    assert not inspect.isabstract(xal_LargeMailUserName)


def test_xal_largemailusername_constructor_exists():
    assert callable(xal_LargeMailUserName.__init__)


def test_xal_largemailusername_constructor_args():
    sig = inspect.signature(xal_LargeMailUserName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_largemailusername_has_code():
    assert hasattr(xal_LargeMailUserName, "code")
    descriptor = None
    for klass in xal_LargeMailUserName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailusername_has_mixed():
    assert hasattr(xal_LargeMailUserName, "mixed")
    descriptor = None
    for klass in xal_LargeMailUserName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailusername_has_anyAttribute():
    assert hasattr(xal_LargeMailUserName, "anyAttribute")
    descriptor = None
    for klass in xal_LargeMailUserName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailusername_has_type():
    assert hasattr(xal_LargeMailUserName, "type")
    descriptor = None
    for klass in xal_LargeMailUserName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_keylinecode_is_not_abstract():
    assert not inspect.isabstract(xal_KeyLineCode)


def test_xal_keylinecode_constructor_exists():
    assert callable(xal_KeyLineCode.__init__)


def test_xal_keylinecode_constructor_args():
    sig = inspect.signature(xal_KeyLineCode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_keylinecode_has_type():
    assert hasattr(xal_KeyLineCode, "type")
    descriptor = None
    for klass in xal_KeyLineCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_keylinecode_has_anyAttribute():
    assert hasattr(xal_KeyLineCode, "anyAttribute")
    descriptor = None
    for klass in xal_KeyLineCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_keylinecode_has_mixed():
    assert hasattr(xal_KeyLineCode, "mixed")
    descriptor = None
    for klass in xal_KeyLineCode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_keylinecode_has_code():
    assert hasattr(xal_KeyLineCode, "code")
    descriptor = None
    for klass in xal_KeyLineCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_endorsementlinecode_is_not_abstract():
    assert not inspect.isabstract(xal_EndorsementLineCode)


def test_xal_endorsementlinecode_constructor_exists():
    assert callable(xal_EndorsementLineCode.__init__)


def test_xal_endorsementlinecode_constructor_args():
    sig = inspect.signature(xal_EndorsementLineCode.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_endorsementlinecode_has_mixed():
    assert hasattr(xal_EndorsementLineCode, "mixed")
    descriptor = None
    for klass in xal_EndorsementLineCode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_endorsementlinecode_has_type():
    assert hasattr(xal_EndorsementLineCode, "type")
    descriptor = None
    for klass in xal_EndorsementLineCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_endorsementlinecode_has_anyAttribute():
    assert hasattr(xal_EndorsementLineCode, "anyAttribute")
    descriptor = None
    for klass in xal_EndorsementLineCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_endorsementlinecode_has_code():
    assert hasattr(xal_EndorsementLineCode, "code")
    descriptor = None
    for klass in xal_EndorsementLineCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_xal_is_not_abstract():
    assert not inspect.isabstract(xal_Xal)


def test_xal_xal_constructor_exists():
    assert callable(xal_Xal.__init__)


def test_xal_xal_constructor_args():
    sig = inspect.signature(xal_Xal.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "version" in params, "Missing parameter 'version'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_xal_has_any():
    assert hasattr(xal_Xal, "any")
    descriptor = None
    for klass in xal_Xal.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_xal_has_version():
    assert hasattr(xal_Xal, "version")
    descriptor = None
    for klass in xal_Xal.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xal_xal_has_anyAttribute():
    assert hasattr(xal_Xal, "anyAttribute")
    descriptor = None
    for klass in xal_Xal.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_firmname_is_not_abstract():
    assert not inspect.isabstract(xal_FirmName)


def test_xal_firmname_constructor_exists():
    assert callable(xal_FirmName.__init__)


def test_xal_firmname_constructor_args():
    sig = inspect.signature(xal_FirmName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_firmname_has_type():
    assert hasattr(xal_FirmName, "type")
    descriptor = None
    for klass in xal_FirmName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_firmname_has_anyAttribute():
    assert hasattr(xal_FirmName, "anyAttribute")
    descriptor = None
    for klass in xal_FirmName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_firmname_has_code():
    assert hasattr(xal_FirmName, "code")
    descriptor = None
    for klass in xal_FirmName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_firmname_has_mixed():
    assert hasattr(xal_FirmName, "mixed")
    descriptor = None
    for klass in xal_FirmName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_firm_is_not_abstract():
    assert not inspect.isabstract(xal_Firm)


def test_xal_firm_constructor_exists():
    assert callable(xal_Firm.__init__)


def test_xal_firm_constructor_args():
    sig = inspect.signature(xal_Firm.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_firm_has_type():
    assert hasattr(xal_Firm, "type")
    descriptor = None
    for klass in xal_Firm.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_firm_has_any():
    assert hasattr(xal_Firm, "any")
    descriptor = None
    for klass in xal_Firm.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_firm_has_anyAttribute():
    assert hasattr(xal_Firm, "anyAttribute")
    descriptor = None
    for klass in xal_Firm.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_premisenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberSuffix)


def test_xal_premisenumbersuffix_constructor_exists():
    assert callable(xal_PremiseNumberSuffix.__init__)


def test_xal_premisenumbersuffix_constructor_args():
    sig = inspect.signature(xal_PremiseNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_premisenumbersuffix_has_anyAttribute():
    assert hasattr(xal_PremiseNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal_PremiseNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal_PremiseNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal_PremiseNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumbersuffix_has_mixed():
    assert hasattr(xal_PremiseNumberSuffix, "mixed")
    descriptor = None
    for klass in xal_PremiseNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumbersuffix_has_type():
    assert hasattr(xal_PremiseNumberSuffix, "type")
    descriptor = None
    for klass in xal_PremiseNumberSuffix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumbersuffix_has_code():
    assert hasattr(xal_PremiseNumberSuffix, "code")
    descriptor = None
    for klass in xal_PremiseNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_premisenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberPrefix)


def test_xal_premisenumberprefix_constructor_exists():
    assert callable(xal_PremiseNumberPrefix.__init__)


def test_xal_premisenumberprefix_constructor_args():
    sig = inspect.signature(xal_PremiseNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "value" in params, "Missing parameter 'value'"

def test_xal_premisenumberprefix_has_anyAttribute():
    assert hasattr(xal_PremiseNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal_PremiseNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberprefix_has_code():
    assert hasattr(xal_PremiseNumberPrefix, "code")
    descriptor = None
    for klass in xal_PremiseNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberprefix_has_type():
    assert hasattr(xal_PremiseNumberPrefix, "type")
    descriptor = None
    for klass in xal_PremiseNumberPrefix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal_PremiseNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal_PremiseNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberprefix_has_value():
    assert hasattr(xal_PremiseNumberPrefix, "value")
    descriptor = None
    for klass in xal_PremiseNumberPrefix.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xal_premisenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumber)


def test_xal_premisenumber_constructor_exists():
    assert callable(xal_PremiseNumber.__init__)


def test_xal_premisenumber_constructor_args():
    sig = inspect.signature(xal_PremiseNumber.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "numberTypeOccurrence" in params, "Missing parameter 'numberTypeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "numberType" in params, "Missing parameter 'numberType'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_premisenumber_has_type():
    assert hasattr(xal_PremiseNumber, "type")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_code():
    assert hasattr(xal_PremiseNumber, "code")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_indicator():
    assert hasattr(xal_PremiseNumber, "indicator")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_indicatorOccurrence():
    assert hasattr(xal_PremiseNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_numberTypeOccurrence():
    assert hasattr(xal_PremiseNumber, "numberTypeOccurrence")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "numberTypeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberTypeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_mixed():
    assert hasattr(xal_PremiseNumber, "mixed")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_numberType():
    assert hasattr(xal_PremiseNumber, "numberType")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "numberType" in klass.__dict__:
            descriptor = klass.__dict__["numberType"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumber_has_anyAttribute():
    assert hasattr(xal_PremiseNumber, "anyAttribute")
    descriptor = None
    for klass in xal_PremiseNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberSuffix)


def test_xal_thoroughfarenumbersuffix_constructor_exists():
    assert callable(xal_ThoroughfareNumberSuffix.__init__)


def test_xal_thoroughfarenumbersuffix_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_thoroughfarenumbersuffix_has_type():
    assert hasattr(xal_ThoroughfareNumberSuffix, "type")
    descriptor = None
    for klass in xal_ThoroughfareNumberSuffix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal_ThoroughfareNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal_ThoroughfareNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumbersuffix_has_code():
    assert hasattr(xal_ThoroughfareNumberSuffix, "code")
    descriptor = None
    for klass in xal_ThoroughfareNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumbersuffix_has_mixed():
    assert hasattr(xal_ThoroughfareNumberSuffix, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumbersuffix_has_anyAttribute():
    assert hasattr(xal_ThoroughfareNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberPrefix)


def test_xal_thoroughfarenumberprefix_constructor_exists():
    assert callable(xal_ThoroughfareNumberPrefix.__init__)


def test_xal_thoroughfarenumberprefix_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_thoroughfarenumberprefix_has_anyAttribute():
    assert hasattr(xal_ThoroughfareNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberprefix_has_type():
    assert hasattr(xal_ThoroughfareNumberPrefix, "type")
    descriptor = None
    for klass in xal_ThoroughfareNumberPrefix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberprefix_has_code():
    assert hasattr(xal_ThoroughfareNumberPrefix, "code")
    descriptor = None
    for klass in xal_ThoroughfareNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal_ThoroughfareNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal_ThoroughfareNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberprefix_has_mixed():
    assert hasattr(xal_ThoroughfareNumberPrefix, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareNumberPrefix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarenumber_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumber)


def test_xal_thoroughfarenumber_constructor_exists():
    assert callable(xal_ThoroughfareNumber.__init__)


def test_xal_thoroughfarenumber_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumber.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberType" in params, "Missing parameter 'numberType'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberOccurrence" in params, "Missing parameter 'numberOccurrence'"

def test_xal_thoroughfarenumber_has_anyAttribute():
    assert hasattr(xal_ThoroughfareNumber, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_numberType():
    assert hasattr(xal_ThoroughfareNumber, "numberType")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "numberType" in klass.__dict__:
            descriptor = klass.__dict__["numberType"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_mixed():
    assert hasattr(xal_ThoroughfareNumber, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_indicator():
    assert hasattr(xal_ThoroughfareNumber, "indicator")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_code():
    assert hasattr(xal_ThoroughfareNumber, "code")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_indicatorOccurrence():
    assert hasattr(xal_ThoroughfareNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_type():
    assert hasattr(xal_ThoroughfareNumber, "type")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumber_has_numberOccurrence():
    assert hasattr(xal_ThoroughfareNumber, "numberOccurrence")
    descriptor = None
    for klass in xal_ThoroughfareNumber.__mro__:
        if "numberOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberOccurrence"]
            break
    assert isinstance(descriptor, property)



def test_xal_documentroot_is_not_abstract():
    assert not inspect.isabstract(xal_DocumentRoot)


def test_xal_documentroot_constructor_exists():
    assert callable(xal_DocumentRoot.__init__)


def test_xal_documentroot_constructor_args():
    sig = inspect.signature(xal_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_documentroot_has_mixed():
    assert hasattr(xal_DocumentRoot, "mixed")
    descriptor = None
    for klass in xal_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xal_EStringToStringMapEntry)


def test_xal_estringtostringmapentry_constructor_exists():
    assert callable(xal_EStringToStringMapEntry.__init__)


def test_xal_estringtostringmapentry_constructor_args():
    sig = inspect.signature(xal_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xal_thoroughfarepredirection_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfarePreDirection)


def test_xal_thoroughfarepredirection_constructor_exists():
    assert callable(xal_ThoroughfarePreDirection.__init__)


def test_xal_thoroughfarepredirection_constructor_args():
    sig = inspect.signature(xal_ThoroughfarePreDirection.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_thoroughfarepredirection_has_anyAttribute():
    assert hasattr(xal_ThoroughfarePreDirection, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfarePreDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarepredirection_has_mixed():
    assert hasattr(xal_ThoroughfarePreDirection, "mixed")
    descriptor = None
    for klass in xal_ThoroughfarePreDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarepredirection_has_type():
    assert hasattr(xal_ThoroughfarePreDirection, "type")
    descriptor = None
    for klass in xal_ThoroughfarePreDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarepredirection_has_code():
    assert hasattr(xal_ThoroughfarePreDirection, "code")
    descriptor = None
    for klass in xal_ThoroughfarePreDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_dependentthoroughfare_is_not_abstract():
    assert not inspect.isabstract(xal_DependentThoroughfare)


def test_xal_dependentthoroughfare_constructor_exists():
    assert callable(xal_DependentThoroughfare.__init__)


def test_xal_dependentthoroughfare_constructor_args():
    sig = inspect.signature(xal_DependentThoroughfare.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_dependentthoroughfare_has_anyAttribute():
    assert hasattr(xal_DependentThoroughfare, "anyAttribute")
    descriptor = None
    for klass in xal_DependentThoroughfare.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentthoroughfare_has_any():
    assert hasattr(xal_DependentThoroughfare, "any")
    descriptor = None
    for klass in xal_DependentThoroughfare.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentthoroughfare_has_type():
    assert hasattr(xal_DependentThoroughfare, "type")
    descriptor = None
    for klass in xal_DependentThoroughfare.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarepostdirection_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfarePostDirection)


def test_xal_thoroughfarepostdirection_constructor_exists():
    assert callable(xal_ThoroughfarePostDirection.__init__)


def test_xal_thoroughfarepostdirection_constructor_args():
    sig = inspect.signature(xal_ThoroughfarePostDirection.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_thoroughfarepostdirection_has_mixed():
    assert hasattr(xal_ThoroughfarePostDirection, "mixed")
    descriptor = None
    for klass in xal_ThoroughfarePostDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarepostdirection_has_code():
    assert hasattr(xal_ThoroughfarePostDirection, "code")
    descriptor = None
    for klass in xal_ThoroughfarePostDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarepostdirection_has_anyAttribute():
    assert hasattr(xal_ThoroughfarePostDirection, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfarePostDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarepostdirection_has_type():
    assert hasattr(xal_ThoroughfarePostDirection, "type")
    descriptor = None
    for klass in xal_ThoroughfarePostDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfaretrailingtype_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareTrailingType)


def test_xal_thoroughfaretrailingtype_constructor_exists():
    assert callable(xal_ThoroughfareTrailingType.__init__)


def test_xal_thoroughfaretrailingtype_constructor_args():
    sig = inspect.signature(xal_ThoroughfareTrailingType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_thoroughfaretrailingtype_has_anyAttribute():
    assert hasattr(xal_ThoroughfareTrailingType, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareTrailingType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfaretrailingtype_has_mixed():
    assert hasattr(xal_ThoroughfareTrailingType, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareTrailingType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfaretrailingtype_has_code():
    assert hasattr(xal_ThoroughfareTrailingType, "code")
    descriptor = None
    for klass in xal_ThoroughfareTrailingType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfaretrailingtype_has_type():
    assert hasattr(xal_ThoroughfareTrailingType, "type")
    descriptor = None
    for klass in xal_ThoroughfareTrailingType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarename_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareName)


def test_xal_thoroughfarename_constructor_exists():
    assert callable(xal_ThoroughfareName.__init__)


def test_xal_thoroughfarename_constructor_args():
    sig = inspect.signature(xal_ThoroughfareName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_thoroughfarename_has_anyAttribute():
    assert hasattr(xal_ThoroughfareName, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarename_has_mixed():
    assert hasattr(xal_ThoroughfareName, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarename_has_code():
    assert hasattr(xal_ThoroughfareName, "code")
    descriptor = None
    for klass in xal_ThoroughfareName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarename_has_type():
    assert hasattr(xal_ThoroughfareName, "type")
    descriptor = None
    for klass in xal_ThoroughfareName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfareleadingtype_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareLeadingType)


def test_xal_thoroughfareleadingtype_constructor_exists():
    assert callable(xal_ThoroughfareLeadingType.__init__)


def test_xal_thoroughfareleadingtype_constructor_args():
    sig = inspect.signature(xal_ThoroughfareLeadingType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_thoroughfareleadingtype_has_mixed():
    assert hasattr(xal_ThoroughfareLeadingType, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareLeadingType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfareleadingtype_has_type():
    assert hasattr(xal_ThoroughfareLeadingType, "type")
    descriptor = None
    for klass in xal_ThoroughfareLeadingType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfareleadingtype_has_code():
    assert hasattr(xal_ThoroughfareLeadingType, "code")
    descriptor = None
    for klass in xal_ThoroughfareLeadingType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfareleadingtype_has_anyAttribute():
    assert hasattr(xal_ThoroughfareLeadingType, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareLeadingType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalroute_is_not_abstract():
    assert not inspect.isabstract(xal_PostalRoute)


def test_xal_postalroute_constructor_exists():
    assert callable(xal_PostalRoute.__init__)


def test_xal_postalroute_constructor_args():
    sig = inspect.signature(xal_PostalRoute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_postalroute_has_type():
    assert hasattr(xal_PostalRoute, "type")
    descriptor = None
    for klass in xal_PostalRoute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroute_has_anyAttribute():
    assert hasattr(xal_PostalRoute, "anyAttribute")
    descriptor = None
    for klass in xal_PostalRoute.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroute_has_any():
    assert hasattr(xal_PostalRoute, "any")
    descriptor = None
    for klass in xal_PostalRoute.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_largemailuser_is_not_abstract():
    assert not inspect.isabstract(xal_LargeMailUser)


def test_xal_largemailuser_constructor_exists():
    assert callable(xal_LargeMailUser.__init__)


def test_xal_largemailuser_constructor_args():
    sig = inspect.signature(xal_LargeMailUser.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_largemailuser_has_any():
    assert hasattr(xal_LargeMailUser, "any")
    descriptor = None
    for klass in xal_LargeMailUser.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailuser_has_anyAttribute():
    assert hasattr(xal_LargeMailUser, "anyAttribute")
    descriptor = None
    for klass in xal_LargeMailUser.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_largemailuser_has_type():
    assert hasattr(xal_LargeMailUser, "type")
    descriptor = None
    for klass in xal_LargeMailUser.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_premise_is_not_abstract():
    assert not inspect.isabstract(xal_Premise)


def test_xal_premise_constructor_exists():
    assert callable(xal_Premise.__init__)


def test_xal_premise_constructor_args():
    sig = inspect.signature(xal_Premise.__init__)
    params = list(sig.parameters.keys())
    assert "premiseDependency" in params, "Missing parameter 'premiseDependency'"
    assert "type" in params, "Missing parameter 'type'"
    assert "premiseThoroughfareConnector" in params, "Missing parameter 'premiseThoroughfareConnector'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "premiseDependencyType" in params, "Missing parameter 'premiseDependencyType'"

def test_xal_premise_has_premiseDependency():
    assert hasattr(xal_Premise, "premiseDependency")
    descriptor = None
    for klass in xal_Premise.__mro__:
        if "premiseDependency" in klass.__dict__:
            descriptor = klass.__dict__["premiseDependency"]
            break
    assert isinstance(descriptor, property)

def test_xal_premise_has_type():
    assert hasattr(xal_Premise, "type")
    descriptor = None
    for klass in xal_Premise.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_premise_has_premiseThoroughfareConnector():
    assert hasattr(xal_Premise, "premiseThoroughfareConnector")
    descriptor = None
    for klass in xal_Premise.__mro__:
        if "premiseThoroughfareConnector" in klass.__dict__:
            descriptor = klass.__dict__["premiseThoroughfareConnector"]
            break
    assert isinstance(descriptor, property)

def test_xal_premise_has_anyAttribute():
    assert hasattr(xal_Premise, "anyAttribute")
    descriptor = None
    for klass in xal_Premise.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_premise_has_any():
    assert hasattr(xal_Premise, "any")
    descriptor = None
    for klass in xal_Premise.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_premise_has_premiseDependencyType():
    assert hasattr(xal_Premise, "premiseDependencyType")
    descriptor = None
    for klass in xal_Premise.__mro__:
        if "premiseDependencyType" in klass.__dict__:
            descriptor = klass.__dict__["premiseDependencyType"]
            break
    assert isinstance(descriptor, property)



def test_xal_postbox_is_not_abstract():
    assert not inspect.isabstract(xal_PostBox)


def test_xal_postbox_constructor_exists():
    assert callable(xal_PostBox.__init__)


def test_xal_postbox_constructor_args():
    sig = inspect.signature(xal_PostBox.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_postbox_has_indicator():
    assert hasattr(xal_PostBox, "indicator")
    descriptor = None
    for klass in xal_PostBox.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postbox_has_type():
    assert hasattr(xal_PostBox, "type")
    descriptor = None
    for klass in xal_PostBox.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_postbox_has_anyAttribute():
    assert hasattr(xal_PostBox, "anyAttribute")
    descriptor = None
    for klass in xal_PostBox.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postbox_has_any():
    assert hasattr(xal_PostBox, "any")
    descriptor = None
    for klass in xal_PostBox.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_dependentlocalitynumber_is_not_abstract():
    assert not inspect.isabstract(xal_DependentLocalityNumber)


def test_xal_dependentlocalitynumber_constructor_exists():
    assert callable(xal_DependentLocalityNumber.__init__)


def test_xal_dependentlocalitynumber_constructor_args():
    sig = inspect.signature(xal_DependentLocalityNumber.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "nameNumberOccurrence" in params, "Missing parameter 'nameNumberOccurrence'"

def test_xal_dependentlocalitynumber_has_anyAttribute():
    assert hasattr(xal_DependentLocalityNumber, "anyAttribute")
    descriptor = None
    for klass in xal_DependentLocalityNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocalitynumber_has_code():
    assert hasattr(xal_DependentLocalityNumber, "code")
    descriptor = None
    for klass in xal_DependentLocalityNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocalitynumber_has_mixed():
    assert hasattr(xal_DependentLocalityNumber, "mixed")
    descriptor = None
    for klass in xal_DependentLocalityNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocalitynumber_has_nameNumberOccurrence():
    assert hasattr(xal_DependentLocalityNumber, "nameNumberOccurrence")
    descriptor = None
    for klass in xal_DependentLocalityNumber.__mro__:
        if "nameNumberOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["nameNumberOccurrence"]
            break
    assert isinstance(descriptor, property)



def test_xal_dependentlocalityname_is_not_abstract():
    assert not inspect.isabstract(xal_DependentLocalityName)


def test_xal_dependentlocalityname_constructor_exists():
    assert callable(xal_DependentLocalityName.__init__)


def test_xal_dependentlocalityname_constructor_args():
    sig = inspect.signature(xal_DependentLocalityName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_dependentlocalityname_has_mixed():
    assert hasattr(xal_DependentLocalityName, "mixed")
    descriptor = None
    for klass in xal_DependentLocalityName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocalityname_has_anyAttribute():
    assert hasattr(xal_DependentLocalityName, "anyAttribute")
    descriptor = None
    for klass in xal_DependentLocalityName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocalityname_has_type():
    assert hasattr(xal_DependentLocalityName, "type")
    descriptor = None
    for klass in xal_DependentLocalityName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocalityname_has_code():
    assert hasattr(xal_DependentLocalityName, "code")
    descriptor = None
    for klass in xal_DependentLocalityName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_dependentlocality_is_not_abstract():
    assert not inspect.isabstract(xal_DependentLocality)


def test_xal_dependentlocality_constructor_exists():
    assert callable(xal_DependentLocality.__init__)


def test_xal_dependentlocality_constructor_args():
    sig = inspect.signature(xal_DependentLocality.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "connector" in params, "Missing parameter 'connector'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_dependentlocality_has_type():
    assert hasattr(xal_DependentLocality, "type")
    descriptor = None
    for klass in xal_DependentLocality.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocality_has_usageType():
    assert hasattr(xal_DependentLocality, "usageType")
    descriptor = None
    for klass in xal_DependentLocality.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocality_has_connector():
    assert hasattr(xal_DependentLocality, "connector")
    descriptor = None
    for klass in xal_DependentLocality.__mro__:
        if "connector" in klass.__dict__:
            descriptor = klass.__dict__["connector"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocality_has_indicator():
    assert hasattr(xal_DependentLocality, "indicator")
    descriptor = None
    for klass in xal_DependentLocality.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocality_has_anyAttribute():
    assert hasattr(xal_DependentLocality, "anyAttribute")
    descriptor = None
    for klass in xal_DependentLocality.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_dependentlocality_has_any():
    assert hasattr(xal_DependentLocality, "any")
    descriptor = None
    for klass in xal_DependentLocality.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_mailstop_is_not_abstract():
    assert not inspect.isabstract(xal_MailStop)


def test_xal_mailstop_constructor_exists():
    assert callable(xal_MailStop.__init__)


def test_xal_mailstop_constructor_args():
    sig = inspect.signature(xal_MailStop.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_mailstop_has_anyAttribute():
    assert hasattr(xal_MailStop, "anyAttribute")
    descriptor = None
    for klass in xal_MailStop.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstop_has_type():
    assert hasattr(xal_MailStop, "type")
    descriptor = None
    for klass in xal_MailStop.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstop_has_any():
    assert hasattr(xal_MailStop, "any")
    descriptor = None
    for klass in xal_MailStop.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_departmentname_is_not_abstract():
    assert not inspect.isabstract(xal_DepartmentName)


def test_xal_departmentname_constructor_exists():
    assert callable(xal_DepartmentName.__init__)


def test_xal_departmentname_constructor_args():
    sig = inspect.signature(xal_DepartmentName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_departmentname_has_anyAttribute():
    assert hasattr(xal_DepartmentName, "anyAttribute")
    descriptor = None
    for klass in xal_DepartmentName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_departmentname_has_mixed():
    assert hasattr(xal_DepartmentName, "mixed")
    descriptor = None
    for klass in xal_DepartmentName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_departmentname_has_type():
    assert hasattr(xal_DepartmentName, "type")
    descriptor = None
    for klass in xal_DepartmentName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_departmentname_has_code():
    assert hasattr(xal_DepartmentName, "code")
    descriptor = None
    for klass in xal_DepartmentName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_department_is_not_abstract():
    assert not inspect.isabstract(xal_Department)


def test_xal_department_constructor_exists():
    assert callable(xal_Department.__init__)


def test_xal_department_constructor_args():
    sig = inspect.signature(xal_Department.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_department_has_type():
    assert hasattr(xal_Department, "type")
    descriptor = None
    for klass in xal_Department.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_department_has_anyAttribute():
    assert hasattr(xal_Department, "anyAttribute")
    descriptor = None
    for klass in xal_Department.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_department_has_any():
    assert hasattr(xal_Department, "any")
    descriptor = None
    for klass in xal_Department.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_countryname_is_not_abstract():
    assert not inspect.isabstract(xal_CountryName)


def test_xal_countryname_constructor_exists():
    assert callable(xal_CountryName.__init__)


def test_xal_countryname_constructor_args():
    sig = inspect.signature(xal_CountryName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_countryname_has_anyAttribute():
    assert hasattr(xal_CountryName, "anyAttribute")
    descriptor = None
    for klass in xal_CountryName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_countryname_has_mixed():
    assert hasattr(xal_CountryName, "mixed")
    descriptor = None
    for klass in xal_CountryName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_countryname_has_code():
    assert hasattr(xal_CountryName, "code")
    descriptor = None
    for klass in xal_CountryName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_countryname_has_type():
    assert hasattr(xal_CountryName, "type")
    descriptor = None
    for klass in xal_CountryName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_countrynamecode_is_not_abstract():
    assert not inspect.isabstract(xal_CountryNameCode)


def test_xal_countrynamecode_constructor_exists():
    assert callable(xal_CountryNameCode.__init__)


def test_xal_countrynamecode_constructor_args():
    sig = inspect.signature(xal_CountryNameCode.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_countrynamecode_has_scheme():
    assert hasattr(xal_CountryNameCode, "scheme")
    descriptor = None
    for klass in xal_CountryNameCode.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)

def test_xal_countrynamecode_has_code():
    assert hasattr(xal_CountryNameCode, "code")
    descriptor = None
    for klass in xal_CountryNameCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_countrynamecode_has_mixed():
    assert hasattr(xal_CountryNameCode, "mixed")
    descriptor = None
    for klass in xal_CountryNameCode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_countrynamecode_has_anyAttribute():
    assert hasattr(xal_CountryNameCode, "anyAttribute")
    descriptor = None
    for klass in xal_CountryNameCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_barcode_is_not_abstract():
    assert not inspect.isabstract(xal_Barcode)


def test_xal_barcode_constructor_exists():
    assert callable(xal_Barcode.__init__)


def test_xal_barcode_constructor_args():
    sig = inspect.signature(xal_Barcode.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_barcode_has_anyAttribute():
    assert hasattr(xal_Barcode, "anyAttribute")
    descriptor = None
    for klass in xal_Barcode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_barcode_has_type():
    assert hasattr(xal_Barcode, "type")
    descriptor = None
    for klass in xal_Barcode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_barcode_has_mixed():
    assert hasattr(xal_Barcode, "mixed")
    descriptor = None
    for klass in xal_Barcode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_barcode_has_code():
    assert hasattr(xal_Barcode, "code")
    descriptor = None
    for klass in xal_Barcode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_buildingname_is_not_abstract():
    assert not inspect.isabstract(xal_BuildingName)


def test_xal_buildingname_constructor_exists():
    assert callable(xal_BuildingName.__init__)


def test_xal_buildingname_constructor_args():
    sig = inspect.signature(xal_BuildingName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_buildingname_has_code():
    assert hasattr(xal_BuildingName, "code")
    descriptor = None
    for klass in xal_BuildingName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_buildingname_has_type():
    assert hasattr(xal_BuildingName, "type")
    descriptor = None
    for klass in xal_BuildingName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_buildingname_has_anyAttribute():
    assert hasattr(xal_BuildingName, "anyAttribute")
    descriptor = None
    for klass in xal_BuildingName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_buildingname_has_typeOccurrence():
    assert hasattr(xal_BuildingName, "typeOccurrence")
    descriptor = None
    for klass in xal_BuildingName.__mro__:
        if "typeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["typeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_buildingname_has_mixed():
    assert hasattr(xal_BuildingName, "mixed")
    descriptor = None
    for klass in xal_BuildingName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalcode_is_not_abstract():
    assert not inspect.isabstract(xal_PostalCode)


def test_xal_postalcode_constructor_exists():
    assert callable(xal_PostalCode.__init__)


def test_xal_postalcode_constructor_args():
    sig = inspect.signature(xal_PostalCode.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_postalcode_has_any():
    assert hasattr(xal_PostalCode, "any")
    descriptor = None
    for klass in xal_PostalCode.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcode_has_anyAttribute():
    assert hasattr(xal_PostalCode, "anyAttribute")
    descriptor = None
    for klass in xal_PostalCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcode_has_type():
    assert hasattr(xal_PostalCode, "type")
    descriptor = None
    for klass in xal_PostalCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_postoffice_is_not_abstract():
    assert not inspect.isabstract(xal_PostOffice)


def test_xal_postoffice_constructor_exists():
    assert callable(xal_PostOffice.__init__)


def test_xal_postoffice_constructor_args():
    sig = inspect.signature(xal_PostOffice.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_postoffice_has_indicator():
    assert hasattr(xal_PostOffice, "indicator")
    descriptor = None
    for klass in xal_PostOffice.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postoffice_has_type():
    assert hasattr(xal_PostOffice, "type")
    descriptor = None
    for klass in xal_PostOffice.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_postoffice_has_any():
    assert hasattr(xal_PostOffice, "any")
    descriptor = None
    for klass in xal_PostOffice.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_postoffice_has_anyAttribute():
    assert hasattr(xal_PostOffice, "anyAttribute")
    descriptor = None
    for klass in xal_PostOffice.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_addresslongitudedirection_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLongitudeDirection)


def test_xal_addresslongitudedirection_constructor_exists():
    assert callable(xal_AddressLongitudeDirection.__init__)


def test_xal_addresslongitudedirection_constructor_args():
    sig = inspect.signature(xal_AddressLongitudeDirection.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_addresslongitudedirection_has_type():
    assert hasattr(xal_AddressLongitudeDirection, "type")
    descriptor = None
    for klass in xal_AddressLongitudeDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslongitudedirection_has_mixed():
    assert hasattr(xal_AddressLongitudeDirection, "mixed")
    descriptor = None
    for klass in xal_AddressLongitudeDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslongitudedirection_has_code():
    assert hasattr(xal_AddressLongitudeDirection, "code")
    descriptor = None
    for klass in xal_AddressLongitudeDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslongitudedirection_has_anyAttribute():
    assert hasattr(xal_AddressLongitudeDirection, "anyAttribute")
    descriptor = None
    for klass in xal_AddressLongitudeDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_subadministrativearea_is_not_abstract():
    assert not inspect.isabstract(xal_SubAdministrativeArea)


def test_xal_subadministrativearea_constructor_exists():
    assert callable(xal_SubAdministrativeArea.__init__)


def test_xal_subadministrativearea_constructor_args():
    sig = inspect.signature(xal_SubAdministrativeArea.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "usageType" in params, "Missing parameter 'usageType'"

def test_xal_subadministrativearea_has_type():
    assert hasattr(xal_SubAdministrativeArea, "type")
    descriptor = None
    for klass in xal_SubAdministrativeArea.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativearea_has_any():
    assert hasattr(xal_SubAdministrativeArea, "any")
    descriptor = None
    for klass in xal_SubAdministrativeArea.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativearea_has_indicator():
    assert hasattr(xal_SubAdministrativeArea, "indicator")
    descriptor = None
    for klass in xal_SubAdministrativeArea.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativearea_has_anyAttribute():
    assert hasattr(xal_SubAdministrativeArea, "anyAttribute")
    descriptor = None
    for klass in xal_SubAdministrativeArea.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativearea_has_usageType():
    assert hasattr(xal_SubAdministrativeArea, "usageType")
    descriptor = None
    for klass in xal_SubAdministrativeArea.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)



def test_xal_administrativeareaname_is_not_abstract():
    assert not inspect.isabstract(xal_AdministrativeAreaName)


def test_xal_administrativeareaname_constructor_exists():
    assert callable(xal_AdministrativeAreaName.__init__)


def test_xal_administrativeareaname_constructor_args():
    sig = inspect.signature(xal_AdministrativeAreaName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_administrativeareaname_has_type():
    assert hasattr(xal_AdministrativeAreaName, "type")
    descriptor = None
    for klass in xal_AdministrativeAreaName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativeareaname_has_code():
    assert hasattr(xal_AdministrativeAreaName, "code")
    descriptor = None
    for klass in xal_AdministrativeAreaName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativeareaname_has_mixed():
    assert hasattr(xal_AdministrativeAreaName, "mixed")
    descriptor = None
    for klass in xal_AdministrativeAreaName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativeareaname_has_anyAttribute():
    assert hasattr(xal_AdministrativeAreaName, "anyAttribute")
    descriptor = None
    for klass in xal_AdministrativeAreaName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_addressline_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLine)


def test_xal_addressline_constructor_exists():
    assert callable(xal_AddressLine.__init__)


def test_xal_addressline_constructor_args():
    sig = inspect.signature(xal_AddressLine.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_addressline_has_code():
    assert hasattr(xal_AddressLine, "code")
    descriptor = None
    for klass in xal_AddressLine.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressline_has_anyAttribute():
    assert hasattr(xal_AddressLine, "anyAttribute")
    descriptor = None
    for klass in xal_AddressLine.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressline_has_mixed():
    assert hasattr(xal_AddressLine, "mixed")
    descriptor = None
    for klass in xal_AddressLine.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressline_has_type():
    assert hasattr(xal_AddressLine, "type")
    descriptor = None
    for klass in xal_AddressLine.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_addresslongitude_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLongitude)


def test_xal_addresslongitude_constructor_exists():
    assert callable(xal_AddressLongitude.__init__)


def test_xal_addresslongitude_constructor_args():
    sig = inspect.signature(xal_AddressLongitude.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_addresslongitude_has_code():
    assert hasattr(xal_AddressLongitude, "code")
    descriptor = None
    for klass in xal_AddressLongitude.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslongitude_has_mixed():
    assert hasattr(xal_AddressLongitude, "mixed")
    descriptor = None
    for klass in xal_AddressLongitude.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslongitude_has_type():
    assert hasattr(xal_AddressLongitude, "type")
    descriptor = None
    for klass in xal_AddressLongitude.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslongitude_has_anyAttribute():
    assert hasattr(xal_AddressLongitude, "anyAttribute")
    descriptor = None
    for klass in xal_AddressLongitude.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_addresslatitude_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLatitude)


def test_xal_addresslatitude_constructor_exists():
    assert callable(xal_AddressLatitude.__init__)


def test_xal_addresslatitude_constructor_args():
    sig = inspect.signature(xal_AddressLatitude.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_addresslatitude_has_code():
    assert hasattr(xal_AddressLatitude, "code")
    descriptor = None
    for klass in xal_AddressLatitude.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslatitude_has_type():
    assert hasattr(xal_AddressLatitude, "type")
    descriptor = None
    for klass in xal_AddressLatitude.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslatitude_has_mixed():
    assert hasattr(xal_AddressLatitude, "mixed")
    descriptor = None
    for klass in xal_AddressLatitude.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslatitude_has_anyAttribute():
    assert hasattr(xal_AddressLatitude, "anyAttribute")
    descriptor = None
    for klass in xal_AddressLatitude.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_addresslatitudedirection_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLatitudeDirection)


def test_xal_addresslatitudedirection_constructor_exists():
    assert callable(xal_AddressLatitudeDirection.__init__)


def test_xal_addresslatitudedirection_constructor_args():
    sig = inspect.signature(xal_AddressLatitudeDirection.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_addresslatitudedirection_has_code():
    assert hasattr(xal_AddressLatitudeDirection, "code")
    descriptor = None
    for klass in xal_AddressLatitudeDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslatitudedirection_has_type():
    assert hasattr(xal_AddressLatitudeDirection, "type")
    descriptor = None
    for klass in xal_AddressLatitudeDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslatitudedirection_has_anyAttribute():
    assert hasattr(xal_AddressLatitudeDirection, "anyAttribute")
    descriptor = None
    for klass in xal_AddressLatitudeDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslatitudedirection_has_mixed():
    assert hasattr(xal_AddressLatitudeDirection, "mixed")
    descriptor = None
    for klass in xal_AddressLatitudeDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_addressidentifier_is_not_abstract():
    assert not inspect.isabstract(xal_AddressIdentifier)


def test_xal_addressidentifier_constructor_exists():
    assert callable(xal_AddressIdentifier.__init__)


def test_xal_addressidentifier_constructor_args():
    sig = inspect.signature(xal_AddressIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifierType" in params, "Missing parameter 'identifierType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_addressidentifier_has_identifierType():
    assert hasattr(xal_AddressIdentifier, "identifierType")
    descriptor = None
    for klass in xal_AddressIdentifier.__mro__:
        if "identifierType" in klass.__dict__:
            descriptor = klass.__dict__["identifierType"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressidentifier_has_type():
    assert hasattr(xal_AddressIdentifier, "type")
    descriptor = None
    for klass in xal_AddressIdentifier.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressidentifier_has_code():
    assert hasattr(xal_AddressIdentifier, "code")
    descriptor = None
    for klass in xal_AddressIdentifier.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressidentifier_has_anyAttribute():
    assert hasattr(xal_AddressIdentifier, "anyAttribute")
    descriptor = None
    for klass in xal_AddressIdentifier.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressidentifier_has_mixed():
    assert hasattr(xal_AddressIdentifier, "mixed")
    descriptor = None
    for klass in xal_AddressIdentifier.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_addresslines_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLines)


def test_xal_addresslines_constructor_exists():
    assert callable(xal_AddressLines.__init__)


def test_xal_addresslines_constructor_args():
    sig = inspect.signature(xal_AddressLines.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_addresslines_has_anyAttribute():
    assert hasattr(xal_AddressLines, "anyAttribute")
    descriptor = None
    for klass in xal_AddressLines.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_addresslines_has_any():
    assert hasattr(xal_AddressLines, "any")
    descriptor = None
    for klass in xal_AddressLines.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfare_is_not_abstract():
    assert not inspect.isabstract(xal_Thoroughfare)


def test_xal_thoroughfare_constructor_exists():
    assert callable(xal_Thoroughfare.__init__)


def test_xal_thoroughfare_constructor_args():
    sig = inspect.signature(xal_Thoroughfare.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "dependentThoroughfaresIndicator" in params, "Missing parameter 'dependentThoroughfaresIndicator'"
    assert "dependentThoroughfares" in params, "Missing parameter 'dependentThoroughfares'"
    assert "group" in params, "Missing parameter 'group'"
    assert "type" in params, "Missing parameter 'type'"
    assert "dependentThoroughfaresType" in params, "Missing parameter 'dependentThoroughfaresType'"
    assert "dependentThoroughfaresConnector" in params, "Missing parameter 'dependentThoroughfaresConnector'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_thoroughfare_has_anyAttribute():
    assert hasattr(xal_Thoroughfare, "anyAttribute")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_dependentThoroughfaresIndicator():
    assert hasattr(xal_Thoroughfare, "dependentThoroughfaresIndicator")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "dependentThoroughfaresIndicator" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfaresIndicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_dependentThoroughfares():
    assert hasattr(xal_Thoroughfare, "dependentThoroughfares")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "dependentThoroughfares" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfares"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_group():
    assert hasattr(xal_Thoroughfare, "group")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_type():
    assert hasattr(xal_Thoroughfare, "type")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_dependentThoroughfaresType():
    assert hasattr(xal_Thoroughfare, "dependentThoroughfaresType")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "dependentThoroughfaresType" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfaresType"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_dependentThoroughfaresConnector():
    assert hasattr(xal_Thoroughfare, "dependentThoroughfaresConnector")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "dependentThoroughfaresConnector" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfaresConnector"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfare_has_any():
    assert hasattr(xal_Thoroughfare, "any")
    descriptor = None
    for klass in xal_Thoroughfare.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_locality_is_not_abstract():
    assert not inspect.isabstract(xal_Locality)


def test_xal_locality_constructor_exists():
    assert callable(xal_Locality.__init__)


def test_xal_locality_constructor_args():
    sig = inspect.signature(xal_Locality.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_locality_has_indicator():
    assert hasattr(xal_Locality, "indicator")
    descriptor = None
    for klass in xal_Locality.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_locality_has_usageType():
    assert hasattr(xal_Locality, "usageType")
    descriptor = None
    for klass in xal_Locality.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)

def test_xal_locality_has_type():
    assert hasattr(xal_Locality, "type")
    descriptor = None
    for klass in xal_Locality.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_locality_has_anyAttribute():
    assert hasattr(xal_Locality, "anyAttribute")
    descriptor = None
    for klass in xal_Locality.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_locality_has_any():
    assert hasattr(xal_Locality, "any")
    descriptor = None
    for klass in xal_Locality.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_administrativearea_is_not_abstract():
    assert not inspect.isabstract(xal_AdministrativeArea)


def test_xal_administrativearea_constructor_exists():
    assert callable(xal_AdministrativeArea.__init__)


def test_xal_administrativearea_constructor_args():
    sig = inspect.signature(xal_AdministrativeArea.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_administrativearea_has_indicator():
    assert hasattr(xal_AdministrativeArea, "indicator")
    descriptor = None
    for klass in xal_AdministrativeArea.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativearea_has_anyAttribute():
    assert hasattr(xal_AdministrativeArea, "anyAttribute")
    descriptor = None
    for klass in xal_AdministrativeArea.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativearea_has_usageType():
    assert hasattr(xal_AdministrativeArea, "usageType")
    descriptor = None
    for klass in xal_AdministrativeArea.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativearea_has_any():
    assert hasattr(xal_AdministrativeArea, "any")
    descriptor = None
    for klass in xal_AdministrativeArea.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_administrativearea_has_type():
    assert hasattr(xal_AdministrativeArea, "type")
    descriptor = None
    for klass in xal_AdministrativeArea.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_country_is_not_abstract():
    assert not inspect.isabstract(xal_Country)


def test_xal_country_constructor_exists():
    assert callable(xal_Country.__init__)


def test_xal_country_constructor_args():
    sig = inspect.signature(xal_Country.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_country_has_anyAttribute():
    assert hasattr(xal_Country, "anyAttribute")
    descriptor = None
    for klass in xal_Country.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_country_has_any():
    assert hasattr(xal_Country, "any")
    descriptor = None
    for klass in xal_Country.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalserviceelements_is_not_abstract():
    assert not inspect.isabstract(xal_PostalServiceElements)


def test_xal_postalserviceelements_constructor_exists():
    assert callable(xal_PostalServiceElements.__init__)


def test_xal_postalserviceelements_constructor_args():
    sig = inspect.signature(xal_PostalServiceElements.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_postalserviceelements_has_any():
    assert hasattr(xal_PostalServiceElements, "any")
    descriptor = None
    for klass in xal_PostalServiceElements.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalserviceelements_has_anyAttribute():
    assert hasattr(xal_PostalServiceElements, "anyAttribute")
    descriptor = None
    for klass in xal_PostalServiceElements.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalserviceelements_has_type():
    assert hasattr(xal_PostalServiceElements, "type")
    descriptor = None
    for klass in xal_PostalServiceElements.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_addressdetails_is_not_abstract():
    assert not inspect.isabstract(xal_AddressDetails)


def test_xal_addressdetails_constructor_exists():
    assert callable(xal_AddressDetails.__init__)


def test_xal_addressdetails_constructor_args():
    sig = inspect.signature(xal_AddressDetails.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "currentStatus" in params, "Missing parameter 'currentStatus'"
    assert "validToDate" in params, "Missing parameter 'validToDate'"
    assert "addressType" in params, "Missing parameter 'addressType'"
    assert "validFromDate" in params, "Missing parameter 'validFromDate'"
    assert "usage" in params, "Missing parameter 'usage'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "addressDetailsKey" in params, "Missing parameter 'addressDetailsKey'"

def test_xal_addressdetails_has_code():
    assert hasattr(xal_AddressDetails, "code")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_currentStatus():
    assert hasattr(xal_AddressDetails, "currentStatus")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "currentStatus" in klass.__dict__:
            descriptor = klass.__dict__["currentStatus"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_validToDate():
    assert hasattr(xal_AddressDetails, "validToDate")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "validToDate" in klass.__dict__:
            descriptor = klass.__dict__["validToDate"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_addressType():
    assert hasattr(xal_AddressDetails, "addressType")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "addressType" in klass.__dict__:
            descriptor = klass.__dict__["addressType"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_validFromDate():
    assert hasattr(xal_AddressDetails, "validFromDate")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "validFromDate" in klass.__dict__:
            descriptor = klass.__dict__["validFromDate"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_usage():
    assert hasattr(xal_AddressDetails, "usage")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "usage" in klass.__dict__:
            descriptor = klass.__dict__["usage"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_anyAttribute():
    assert hasattr(xal_AddressDetails, "anyAttribute")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_any():
    assert hasattr(xal_AddressDetails, "any")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal_addressdetails_has_addressDetailsKey():
    assert hasattr(xal_AddressDetails, "addressDetailsKey")
    descriptor = None
    for klass in xal_AddressDetails.__mro__:
        if "addressDetailsKey" in klass.__dict__:
            descriptor = klass.__dict__["addressDetailsKey"]
            break
    assert isinstance(descriptor, property)



def test_xal_address_is_not_abstract():
    assert not inspect.isabstract(xal_Address)


def test_xal_address_constructor_exists():
    assert callable(xal_Address.__init__)


def test_xal_address_constructor_args():
    sig = inspect.signature(xal_Address.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_address_has_type():
    assert hasattr(xal_Address, "type")
    descriptor = None
    for klass in xal_Address.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_address_has_code():
    assert hasattr(xal_Address, "code")
    descriptor = None
    for klass in xal_Address.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_address_has_anyAttribute():
    assert hasattr(xal_Address, "anyAttribute")
    descriptor = None
    for klass in xal_Address.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_address_has_mixed():
    assert hasattr(xal_Address, "mixed")
    descriptor = None
    for klass in xal_Address.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarenumberto_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberTo)


def test_xal_thoroughfarenumberto_constructor_exists():
    assert callable(xal_ThoroughfareNumberTo.__init__)


def test_xal_thoroughfarenumberto_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberTo.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_thoroughfarenumberto_has_code():
    assert hasattr(xal_ThoroughfareNumberTo, "code")
    descriptor = None
    for klass in xal_ThoroughfareNumberTo.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberto_has_anyAttribute():
    assert hasattr(xal_ThoroughfareNumberTo, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareNumberTo.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberto_has_mixed():
    assert hasattr(xal_ThoroughfareNumberTo, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareNumberTo.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarenumberfrom_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberFrom)


def test_xal_thoroughfarenumberfrom_constructor_exists():
    assert callable(xal_ThoroughfareNumberFrom.__init__)


def test_xal_thoroughfarenumberfrom_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberFrom.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_thoroughfarenumberfrom_has_code():
    assert hasattr(xal_ThoroughfareNumberFrom, "code")
    descriptor = None
    for klass in xal_ThoroughfareNumberFrom.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberfrom_has_anyAttribute():
    assert hasattr(xal_ThoroughfareNumberFrom, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareNumberFrom.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberfrom_has_mixed():
    assert hasattr(xal_ThoroughfareNumberFrom, "mixed")
    descriptor = None
    for klass in xal_ThoroughfareNumberFrom.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_thoroughfarenumberrange_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberRange)


def test_xal_thoroughfarenumberrange_constructor_exists():
    assert callable(xal_ThoroughfareNumberRange.__init__)


def test_xal_thoroughfarenumberrange_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberRange.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "numberRangeOccurrence" in params, "Missing parameter 'numberRangeOccurrence'"
    assert "rangeType" in params, "Missing parameter 'rangeType'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_thoroughfarenumberrange_has_type():
    assert hasattr(xal_ThoroughfareNumberRange, "type")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_numberRangeOccurrence():
    assert hasattr(xal_ThoroughfareNumberRange, "numberRangeOccurrence")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "numberRangeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberRangeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_rangeType():
    assert hasattr(xal_ThoroughfareNumberRange, "rangeType")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "rangeType" in klass.__dict__:
            descriptor = klass.__dict__["rangeType"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_indicatorOccurrence():
    assert hasattr(xal_ThoroughfareNumberRange, "indicatorOccurrence")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_indicator():
    assert hasattr(xal_ThoroughfareNumberRange, "indicator")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_code():
    assert hasattr(xal_ThoroughfareNumberRange, "code")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_separator():
    assert hasattr(xal_ThoroughfareNumberRange, "separator")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_xal_thoroughfarenumberrange_has_anyAttribute():
    assert hasattr(xal_ThoroughfareNumberRange, "anyAttribute")
    descriptor = None
    for klass in xal_ThoroughfareNumberRange.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_subpremisenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseNumberPrefix)


def test_xal_subpremisenumberprefix_constructor_exists():
    assert callable(xal_SubPremiseNumberPrefix.__init__)


def test_xal_subpremisenumberprefix_constructor_args():
    sig = inspect.signature(xal_SubPremiseNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_subpremisenumberprefix_has_anyAttribute():
    assert hasattr(xal_SubPremiseNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal_SubPremiseNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumberprefix_has_type():
    assert hasattr(xal_SubPremiseNumberPrefix, "type")
    descriptor = None
    for klass in xal_SubPremiseNumberPrefix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal_SubPremiseNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal_SubPremiseNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumberprefix_has_code():
    assert hasattr(xal_SubPremiseNumberPrefix, "code")
    descriptor = None
    for klass in xal_SubPremiseNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumberprefix_has_mixed():
    assert hasattr(xal_SubPremiseNumberPrefix, "mixed")
    descriptor = None
    for klass in xal_SubPremiseNumberPrefix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_subpremisenumber_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseNumber)


def test_xal_subpremisenumber_constructor_exists():
    assert callable(xal_SubPremiseNumber.__init__)


def test_xal_subpremisenumber_constructor_args():
    sig = inspect.signature(xal_SubPremiseNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "premiseNumberSeparator" in params, "Missing parameter 'premiseNumberSeparator'"
    assert "numberTypeOccurrence" in params, "Missing parameter 'numberTypeOccurrence'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "indicator" in params, "Missing parameter 'indicator'"

def test_xal_subpremisenumber_has_code():
    assert hasattr(xal_SubPremiseNumber, "code")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_mixed():
    assert hasattr(xal_SubPremiseNumber, "mixed")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_anyAttribute():
    assert hasattr(xal_SubPremiseNumber, "anyAttribute")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_type():
    assert hasattr(xal_SubPremiseNumber, "type")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_premiseNumberSeparator():
    assert hasattr(xal_SubPremiseNumber, "premiseNumberSeparator")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "premiseNumberSeparator" in klass.__dict__:
            descriptor = klass.__dict__["premiseNumberSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_numberTypeOccurrence():
    assert hasattr(xal_SubPremiseNumber, "numberTypeOccurrence")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "numberTypeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberTypeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_indicatorOccurrence():
    assert hasattr(xal_SubPremiseNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumber_has_indicator():
    assert hasattr(xal_SubPremiseNumber, "indicator")
    descriptor = None
    for klass in xal_SubPremiseNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)



def test_xal_subpremisenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseNumberSuffix)


def test_xal_subpremisenumbersuffix_constructor_exists():
    assert callable(xal_SubPremiseNumberSuffix.__init__)


def test_xal_subpremisenumbersuffix_constructor_args():
    sig = inspect.signature(xal_SubPremiseNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_subpremisenumbersuffix_has_code():
    assert hasattr(xal_SubPremiseNumberSuffix, "code")
    descriptor = None
    for klass in xal_SubPremiseNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumbersuffix_has_type():
    assert hasattr(xal_SubPremiseNumberSuffix, "type")
    descriptor = None
    for klass in xal_SubPremiseNumberSuffix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumbersuffix_has_anyAttribute():
    assert hasattr(xal_SubPremiseNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal_SubPremiseNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal_SubPremiseNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal_SubPremiseNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisenumbersuffix_has_mixed():
    assert hasattr(xal_SubPremiseNumberSuffix, "mixed")
    descriptor = None
    for klass in xal_SubPremiseNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_subpremiselocation_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseLocation)


def test_xal_subpremiselocation_constructor_exists():
    assert callable(xal_SubPremiseLocation.__init__)


def test_xal_subpremiselocation_constructor_args():
    sig = inspect.signature(xal_SubPremiseLocation.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_subpremiselocation_has_mixed():
    assert hasattr(xal_SubPremiseLocation, "mixed")
    descriptor = None
    for klass in xal_SubPremiseLocation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremiselocation_has_code():
    assert hasattr(xal_SubPremiseLocation, "code")
    descriptor = None
    for klass in xal_SubPremiseLocation.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_subpremisename_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseName)


def test_xal_subpremisename_constructor_exists():
    assert callable(xal_SubPremiseName.__init__)


def test_xal_subpremisename_constructor_args():
    sig = inspect.signature(xal_SubPremiseName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_subpremisename_has_type():
    assert hasattr(xal_SubPremiseName, "type")
    descriptor = None
    for klass in xal_SubPremiseName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisename_has_mixed():
    assert hasattr(xal_SubPremiseName, "mixed")
    descriptor = None
    for klass in xal_SubPremiseName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisename_has_code():
    assert hasattr(xal_SubPremiseName, "code")
    descriptor = None
    for klass in xal_SubPremiseName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisename_has_typeOccurrence():
    assert hasattr(xal_SubPremiseName, "typeOccurrence")
    descriptor = None
    for klass in xal_SubPremiseName.__mro__:
        if "typeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["typeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremisename_has_anyAttribute():
    assert hasattr(xal_SubPremiseName, "anyAttribute")
    descriptor = None
    for klass in xal_SubPremiseName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_subadministrativeareaname_is_not_abstract():
    assert not inspect.isabstract(xal_SubAdministrativeAreaName)


def test_xal_subadministrativeareaname_constructor_exists():
    assert callable(xal_SubAdministrativeAreaName.__init__)


def test_xal_subadministrativeareaname_constructor_args():
    sig = inspect.signature(xal_SubAdministrativeAreaName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_subadministrativeareaname_has_code():
    assert hasattr(xal_SubAdministrativeAreaName, "code")
    descriptor = None
    for klass in xal_SubAdministrativeAreaName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativeareaname_has_mixed():
    assert hasattr(xal_SubAdministrativeAreaName, "mixed")
    descriptor = None
    for klass in xal_SubAdministrativeAreaName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativeareaname_has_type():
    assert hasattr(xal_SubAdministrativeAreaName, "type")
    descriptor = None
    for klass in xal_SubAdministrativeAreaName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subadministrativeareaname_has_anyAttribute():
    assert hasattr(xal_SubAdministrativeAreaName, "anyAttribute")
    descriptor = None
    for klass in xal_SubAdministrativeAreaName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_premisenumberrangeto_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberRangeTo)


def test_xal_premisenumberrangeto_constructor_exists():
    assert callable(xal_PremiseNumberRangeTo.__init__)


def test_xal_premisenumberrangeto_constructor_args():
    sig = inspect.signature(xal_PremiseNumberRangeTo.__init__)
    params = list(sig.parameters.keys())



def test_xal_premisenumberrangefrom_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberRangeFrom)


def test_xal_premisenumberrangefrom_constructor_exists():
    assert callable(xal_PremiseNumberRangeFrom.__init__)


def test_xal_premisenumberrangefrom_constructor_args():
    sig = inspect.signature(xal_PremiseNumberRangeFrom.__init__)
    params = list(sig.parameters.keys())



def test_xal_subpremise_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremise)


def test_xal_subpremise_constructor_exists():
    assert callable(xal_SubPremise.__init__)


def test_xal_subpremise_constructor_args():
    sig = inspect.signature(xal_SubPremise.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal_subpremise_has_type():
    assert hasattr(xal_SubPremise, "type")
    descriptor = None
    for klass in xal_SubPremise.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremise_has_anyAttribute():
    assert hasattr(xal_SubPremise, "anyAttribute")
    descriptor = None
    for klass in xal_SubPremise.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_subpremise_has_any():
    assert hasattr(xal_SubPremise, "any")
    descriptor = None
    for klass in xal_SubPremise.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal_premisename_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseName)


def test_xal_premisename_constructor_exists():
    assert callable(xal_PremiseName.__init__)


def test_xal_premisename_constructor_args():
    sig = inspect.signature(xal_PremiseName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"

def test_xal_premisename_has_mixed():
    assert hasattr(xal_PremiseName, "mixed")
    descriptor = None
    for klass in xal_PremiseName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisename_has_anyAttribute():
    assert hasattr(xal_PremiseName, "anyAttribute")
    descriptor = None
    for klass in xal_PremiseName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisename_has_type():
    assert hasattr(xal_PremiseName, "type")
    descriptor = None
    for klass in xal_PremiseName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisename_has_code():
    assert hasattr(xal_PremiseName, "code")
    descriptor = None
    for klass in xal_PremiseName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisename_has_typeOccurrence():
    assert hasattr(xal_PremiseName, "typeOccurrence")
    descriptor = None
    for klass in xal_PremiseName.__mro__:
        if "typeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["typeOccurrence"]
            break
    assert isinstance(descriptor, property)



def test_xal_premisenumberrange_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberRange)


def test_xal_premisenumberrange_constructor_exists():
    assert callable(xal_PremiseNumberRange.__init__)


def test_xal_premisenumberrange_constructor_args():
    sig = inspect.signature(xal_PremiseNumberRange.__init__)
    params = list(sig.parameters.keys())
    assert "rangeType" in params, "Missing parameter 'rangeType'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "numberRangeOccurence" in params, "Missing parameter 'numberRangeOccurence'"
    assert "indicatorOccurence" in params, "Missing parameter 'indicatorOccurence'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_premisenumberrange_has_rangeType():
    assert hasattr(xal_PremiseNumberRange, "rangeType")
    descriptor = None
    for klass in xal_PremiseNumberRange.__mro__:
        if "rangeType" in klass.__dict__:
            descriptor = klass.__dict__["rangeType"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberrange_has_separator():
    assert hasattr(xal_PremiseNumberRange, "separator")
    descriptor = None
    for klass in xal_PremiseNumberRange.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberrange_has_indicator():
    assert hasattr(xal_PremiseNumberRange, "indicator")
    descriptor = None
    for klass in xal_PremiseNumberRange.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberrange_has_numberRangeOccurence():
    assert hasattr(xal_PremiseNumberRange, "numberRangeOccurence")
    descriptor = None
    for klass in xal_PremiseNumberRange.__mro__:
        if "numberRangeOccurence" in klass.__dict__:
            descriptor = klass.__dict__["numberRangeOccurence"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberrange_has_indicatorOccurence():
    assert hasattr(xal_PremiseNumberRange, "indicatorOccurence")
    descriptor = None
    for klass in xal_PremiseNumberRange.__mro__:
        if "indicatorOccurence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurence"]
            break
    assert isinstance(descriptor, property)

def test_xal_premisenumberrange_has_type():
    assert hasattr(xal_PremiseNumberRange, "type")
    descriptor = None
    for klass in xal_PremiseNumberRange.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_premiselocation_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseLocation)


def test_xal_premiselocation_constructor_exists():
    assert callable(xal_PremiseLocation.__init__)


def test_xal_premiselocation_constructor_args():
    sig = inspect.signature(xal_PremiseLocation.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_premiselocation_has_code():
    assert hasattr(xal_PremiseLocation, "code")
    descriptor = None
    for klass in xal_PremiseLocation.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_premiselocation_has_anyAttribute():
    assert hasattr(xal_PremiseLocation, "anyAttribute")
    descriptor = None
    for klass in xal_PremiseLocation.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_premiselocation_has_mixed():
    assert hasattr(xal_PremiseLocation, "mixed")
    descriptor = None
    for klass in xal_PremiseLocation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_posttownsuffix_is_not_abstract():
    assert not inspect.isabstract(xal_PostTownSuffix)


def test_xal_posttownsuffix_constructor_exists():
    assert callable(xal_PostTownSuffix.__init__)


def test_xal_posttownsuffix_constructor_args():
    sig = inspect.signature(xal_PostTownSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_posttownsuffix_has_code():
    assert hasattr(xal_PostTownSuffix, "code")
    descriptor = None
    for klass in xal_PostTownSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_posttownsuffix_has_mixed():
    assert hasattr(xal_PostTownSuffix, "mixed")
    descriptor = None
    for klass in xal_PostTownSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_posttownsuffix_has_anyAttribute():
    assert hasattr(xal_PostTownSuffix, "anyAttribute")
    descriptor = None
    for klass in xal_PostTownSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_posttownname_is_not_abstract():
    assert not inspect.isabstract(xal_PostTownName)


def test_xal_posttownname_constructor_exists():
    assert callable(xal_PostTownName.__init__)


def test_xal_posttownname_constructor_args():
    sig = inspect.signature(xal_PostTownName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_posttownname_has_mixed():
    assert hasattr(xal_PostTownName, "mixed")
    descriptor = None
    for klass in xal_PostTownName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_posttownname_has_code():
    assert hasattr(xal_PostTownName, "code")
    descriptor = None
    for klass in xal_PostTownName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_posttownname_has_anyAttribute():
    assert hasattr(xal_PostTownName, "anyAttribute")
    descriptor = None
    for klass in xal_PostTownName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_posttownname_has_type():
    assert hasattr(xal_PostTownName, "type")
    descriptor = None
    for klass in xal_PostTownName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_postofficenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostOfficeNumber)


def test_xal_postofficenumber_constructor_exists():
    assert callable(xal_PostOfficeNumber.__init__)


def test_xal_postofficenumber_constructor_args():
    sig = inspect.signature(xal_PostOfficeNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_postofficenumber_has_mixed():
    assert hasattr(xal_PostOfficeNumber, "mixed")
    descriptor = None
    for klass in xal_PostOfficeNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficenumber_has_indicator():
    assert hasattr(xal_PostOfficeNumber, "indicator")
    descriptor = None
    for klass in xal_PostOfficeNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficenumber_has_indicatorOccurrence():
    assert hasattr(xal_PostOfficeNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal_PostOfficeNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficenumber_has_code():
    assert hasattr(xal_PostOfficeNumber, "code")
    descriptor = None
    for klass in xal_PostOfficeNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficenumber_has_anyAttribute():
    assert hasattr(xal_PostOfficeNumber, "anyAttribute")
    descriptor = None
    for klass in xal_PostOfficeNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_postofficename_is_not_abstract():
    assert not inspect.isabstract(xal_PostOfficeName)


def test_xal_postofficename_constructor_exists():
    assert callable(xal_PostOfficeName.__init__)


def test_xal_postofficename_constructor_args():
    sig = inspect.signature(xal_PostOfficeName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_postofficename_has_mixed():
    assert hasattr(xal_PostOfficeName, "mixed")
    descriptor = None
    for klass in xal_PostOfficeName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficename_has_anyAttribute():
    assert hasattr(xal_PostOfficeName, "anyAttribute")
    descriptor = None
    for klass in xal_PostOfficeName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficename_has_type():
    assert hasattr(xal_PostOfficeName, "type")
    descriptor = None
    for klass in xal_PostOfficeName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_postofficename_has_code():
    assert hasattr(xal_PostOfficeName, "code")
    descriptor = None
    for klass in xal_PostOfficeName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_postboxnumberextension_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumberExtension)


def test_xal_postboxnumberextension_constructor_exists():
    assert callable(xal_PostBoxNumberExtension.__init__)


def test_xal_postboxnumberextension_constructor_args():
    sig = inspect.signature(xal_PostBoxNumberExtension.__init__)
    params = list(sig.parameters.keys())
    assert "numberExtensionSeparator" in params, "Missing parameter 'numberExtensionSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_postboxnumberextension_has_numberExtensionSeparator():
    assert hasattr(xal_PostBoxNumberExtension, "numberExtensionSeparator")
    descriptor = None
    for klass in xal_PostBoxNumberExtension.__mro__:
        if "numberExtensionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberExtensionSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumberextension_has_mixed():
    assert hasattr(xal_PostBoxNumberExtension, "mixed")
    descriptor = None
    for klass in xal_PostBoxNumberExtension.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumberextension_has_anyAttribute():
    assert hasattr(xal_PostBoxNumberExtension, "anyAttribute")
    descriptor = None
    for klass in xal_PostBoxNumberExtension.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_postboxnumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumberSuffix)


def test_xal_postboxnumbersuffix_constructor_exists():
    assert callable(xal_PostBoxNumberSuffix.__init__)


def test_xal_postboxnumbersuffix_constructor_args():
    sig = inspect.signature(xal_PostBoxNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_postboxnumbersuffix_has_mixed():
    assert hasattr(xal_PostBoxNumberSuffix, "mixed")
    descriptor = None
    for klass in xal_PostBoxNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumbersuffix_has_code():
    assert hasattr(xal_PostBoxNumberSuffix, "code")
    descriptor = None
    for klass in xal_PostBoxNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal_PostBoxNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal_PostBoxNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumbersuffix_has_anyAttribute():
    assert hasattr(xal_PostBoxNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal_PostBoxNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_postboxnumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumberPrefix)


def test_xal_postboxnumberprefix_constructor_exists():
    assert callable(xal_PostBoxNumberPrefix.__init__)


def test_xal_postboxnumberprefix_constructor_args():
    sig = inspect.signature(xal_PostBoxNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_postboxnumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal_PostBoxNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal_PostBoxNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumberprefix_has_anyAttribute():
    assert hasattr(xal_PostBoxNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal_PostBoxNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumberprefix_has_code():
    assert hasattr(xal_PostBoxNumberPrefix, "code")
    descriptor = None
    for klass in xal_PostBoxNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumberprefix_has_mixed():
    assert hasattr(xal_PostBoxNumberPrefix, "mixed")
    descriptor = None
    for klass in xal_PostBoxNumberPrefix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_supplementarypostalservicedata_is_not_abstract():
    assert not inspect.isabstract(xal_SupplementaryPostalServiceData)


def test_xal_supplementarypostalservicedata_constructor_exists():
    assert callable(xal_SupplementaryPostalServiceData.__init__)


def test_xal_supplementarypostalservicedata_constructor_args():
    sig = inspect.signature(xal_SupplementaryPostalServiceData.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_supplementarypostalservicedata_has_type():
    assert hasattr(xal_SupplementaryPostalServiceData, "type")
    descriptor = None
    for klass in xal_SupplementaryPostalServiceData.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_supplementarypostalservicedata_has_anyAttribute():
    assert hasattr(xal_SupplementaryPostalServiceData, "anyAttribute")
    descriptor = None
    for klass in xal_SupplementaryPostalServiceData.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_supplementarypostalservicedata_has_code():
    assert hasattr(xal_SupplementaryPostalServiceData, "code")
    descriptor = None
    for klass in xal_SupplementaryPostalServiceData.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_supplementarypostalservicedata_has_mixed():
    assert hasattr(xal_SupplementaryPostalServiceData, "mixed")
    descriptor = None
    for klass in xal_SupplementaryPostalServiceData.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_postboxnumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumber)


def test_xal_postboxnumber_constructor_exists():
    assert callable(xal_PostBoxNumber.__init__)


def test_xal_postboxnumber_constructor_args():
    sig = inspect.signature(xal_PostBoxNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_postboxnumber_has_code():
    assert hasattr(xal_PostBoxNumber, "code")
    descriptor = None
    for klass in xal_PostBoxNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumber_has_anyAttribute():
    assert hasattr(xal_PostBoxNumber, "anyAttribute")
    descriptor = None
    for klass in xal_PostBoxNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postboxnumber_has_mixed():
    assert hasattr(xal_PostBoxNumber, "mixed")
    descriptor = None
    for klass in xal_PostBoxNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_sortingcode_is_not_abstract():
    assert not inspect.isabstract(xal_SortingCode)


def test_xal_sortingcode_constructor_exists():
    assert callable(xal_SortingCode.__init__)


def test_xal_sortingcode_constructor_args():
    sig = inspect.signature(xal_SortingCode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_sortingcode_has_type():
    assert hasattr(xal_SortingCode, "type")
    descriptor = None
    for klass in xal_SortingCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_sortingcode_has_code():
    assert hasattr(xal_SortingCode, "code")
    descriptor = None
    for klass in xal_SortingCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalroutenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostalRouteNumber)


def test_xal_postalroutenumber_constructor_exists():
    assert callable(xal_PostalRouteNumber.__init__)


def test_xal_postalroutenumber_constructor_args():
    sig = inspect.signature(xal_PostalRouteNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_postalroutenumber_has_mixed():
    assert hasattr(xal_PostalRouteNumber, "mixed")
    descriptor = None
    for klass in xal_PostalRouteNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroutenumber_has_anyAttribute():
    assert hasattr(xal_PostalRouteNumber, "anyAttribute")
    descriptor = None
    for klass in xal_PostalRouteNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroutenumber_has_code():
    assert hasattr(xal_PostalRouteNumber, "code")
    descriptor = None
    for klass in xal_PostalRouteNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalroutename_is_not_abstract():
    assert not inspect.isabstract(xal_PostalRouteName)


def test_xal_postalroutename_constructor_exists():
    assert callable(xal_PostalRouteName.__init__)


def test_xal_postalroutename_constructor_args():
    sig = inspect.signature(xal_PostalRouteName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_postalroutename_has_mixed():
    assert hasattr(xal_PostalRouteName, "mixed")
    descriptor = None
    for klass in xal_PostalRouteName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroutename_has_anyAttribute():
    assert hasattr(xal_PostalRouteName, "anyAttribute")
    descriptor = None
    for klass in xal_PostalRouteName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroutename_has_code():
    assert hasattr(xal_PostalRouteName, "code")
    descriptor = None
    for klass in xal_PostalRouteName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalroutename_has_type():
    assert hasattr(xal_PostalRouteName, "type")
    descriptor = None
    for klass in xal_PostalRouteName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalcodenumberextension_is_not_abstract():
    assert not inspect.isabstract(xal_PostalCodeNumberExtension)


def test_xal_postalcodenumberextension_constructor_exists():
    assert callable(xal_PostalCodeNumberExtension.__init__)


def test_xal_postalcodenumberextension_constructor_args():
    sig = inspect.signature(xal_PostalCodeNumberExtension.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberExtensionSeparator" in params, "Missing parameter 'numberExtensionSeparator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal_postalcodenumberextension_has_code():
    assert hasattr(xal_PostalCodeNumberExtension, "code")
    descriptor = None
    for klass in xal_PostalCodeNumberExtension.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumberextension_has_anyAttribute():
    assert hasattr(xal_PostalCodeNumberExtension, "anyAttribute")
    descriptor = None
    for klass in xal_PostalCodeNumberExtension.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumberextension_has_numberExtensionSeparator():
    assert hasattr(xal_PostalCodeNumberExtension, "numberExtensionSeparator")
    descriptor = None
    for klass in xal_PostalCodeNumberExtension.__mro__:
        if "numberExtensionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberExtensionSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumberextension_has_type():
    assert hasattr(xal_PostalCodeNumberExtension, "type")
    descriptor = None
    for klass in xal_PostalCodeNumberExtension.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumberextension_has_mixed():
    assert hasattr(xal_PostalCodeNumberExtension, "mixed")
    descriptor = None
    for klass in xal_PostalCodeNumberExtension.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal_postalcodenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostalCodeNumber)


def test_xal_postalcodenumber_constructor_exists():
    assert callable(xal_PostalCodeNumber.__init__)


def test_xal_postalcodenumber_constructor_args():
    sig = inspect.signature(xal_PostalCodeNumber.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_postalcodenumber_has_type():
    assert hasattr(xal_PostalCodeNumber, "type")
    descriptor = None
    for klass in xal_PostalCodeNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumber_has_anyAttribute():
    assert hasattr(xal_PostalCodeNumber, "anyAttribute")
    descriptor = None
    for klass in xal_PostalCodeNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumber_has_mixed():
    assert hasattr(xal_PostalCodeNumber, "mixed")
    descriptor = None
    for klass in xal_PostalCodeNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_postalcodenumber_has_code():
    assert hasattr(xal_PostalCodeNumber, "code")
    descriptor = None
    for klass in xal_PostalCodeNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal_posttown_is_not_abstract():
    assert not inspect.isabstract(xal_PostTown)


def test_xal_posttown_constructor_exists():
    assert callable(xal_PostTown.__init__)


def test_xal_posttown_constructor_args():
    sig = inspect.signature(xal_PostTown.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_posttown_has_anyAttribute():
    assert hasattr(xal_PostTown, "anyAttribute")
    descriptor = None
    for klass in xal_PostTown.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_posttown_has_type():
    assert hasattr(xal_PostTown, "type")
    descriptor = None
    for klass in xal_PostTown.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_mailstopnumber_is_not_abstract():
    assert not inspect.isabstract(xal_MailStopNumber)


def test_xal_mailstopnumber_constructor_exists():
    assert callable(xal_MailStopNumber.__init__)


def test_xal_mailstopnumber_constructor_args():
    sig = inspect.signature(xal_MailStopNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "nameNumberSeparator" in params, "Missing parameter 'nameNumberSeparator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal_mailstopnumber_has_mixed():
    assert hasattr(xal_MailStopNumber, "mixed")
    descriptor = None
    for klass in xal_MailStopNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstopnumber_has_nameNumberSeparator():
    assert hasattr(xal_MailStopNumber, "nameNumberSeparator")
    descriptor = None
    for klass in xal_MailStopNumber.__mro__:
        if "nameNumberSeparator" in klass.__dict__:
            descriptor = klass.__dict__["nameNumberSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstopnumber_has_code():
    assert hasattr(xal_MailStopNumber, "code")
    descriptor = None
    for klass in xal_MailStopNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstopnumber_has_anyAttribute():
    assert hasattr(xal_MailStopNumber, "anyAttribute")
    descriptor = None
    for klass in xal_MailStopNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal_mailstopname_is_not_abstract():
    assert not inspect.isabstract(xal_MailStopName)


def test_xal_mailstopname_constructor_exists():
    assert callable(xal_MailStopName.__init__)


def test_xal_mailstopname_constructor_args():
    sig = inspect.signature(xal_MailStopName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal_mailstopname_has_anyAttribute():
    assert hasattr(xal_MailStopName, "anyAttribute")
    descriptor = None
    for klass in xal_MailStopName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstopname_has_mixed():
    assert hasattr(xal_MailStopName, "mixed")
    descriptor = None
    for klass in xal_MailStopName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstopname_has_code():
    assert hasattr(xal_MailStopName, "code")
    descriptor = None
    for klass in xal_MailStopName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal_mailstopname_has_type():
    assert hasattr(xal_MailStopName, "type")
    descriptor = None
    for klass in xal_MailStopName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal_localityname_is_not_abstract():
    assert not inspect.isabstract(xal_LocalityName)


def test_xal_localityname_constructor_exists():
    assert callable(xal_LocalityName.__init__)


def test_xal_localityname_constructor_args():
    sig = inspect.signature(xal_LocalityName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal_localityname_has_anyAttribute():
    assert hasattr(xal_LocalityName, "anyAttribute")
    descriptor = None
    for klass in xal_LocalityName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal_localityname_has_mixed():
    assert hasattr(xal_LocalityName, "mixed")
    descriptor = None
    for klass in xal_LocalityName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal_localityname_has_type():
    assert hasattr(xal_LocalityName, "type")
    descriptor = None
    for klass in xal_LocalityName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal_localityname_has_code():
    assert hasattr(xal_LocalityName, "code")
    descriptor = None
    for klass in xal_LocalityName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_rangetypetype_exists():
    # Check that the Enumeration exists
    assert RangeTypeType is not None

def test_rangetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RangeTypeType]
    expected_literals = [
        "Odd",
        "Even",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RangeTypeType"

def test_indicatoroccurrence4_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence4 is not None

def test_indicatoroccurrence4_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence4]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence4"

def test_numbertypetype1_exists():
    # Check that the Enumeration exists
    assert NumberTypeType1 is not None

def test_numbertypetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeType1]
    expected_literals = [
        "Single",
        "Range",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeType1"

def test_typeoccurrence_exists():
    # Check that the Enumeration exists
    assert TypeOccurrence is not None

def test_typeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOccurrence"

def test_typeoccurrence2_exists():
    # Check that the Enumeration exists
    assert TypeOccurrence2 is not None

def test_typeoccurrence2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOccurrence2]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOccurrence2"

def test_namenumberoccurrence_exists():
    # Check that the Enumeration exists
    assert NameNumberOccurrence is not None

def test_namenumberoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NameNumberOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NameNumberOccurrence"

def test_indicatoroccurence_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurence is not None

def test_indicatoroccurence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurence]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurence"

def test_numberoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberOccurrence is not None

def test_numberoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberOccurrence]
    expected_literals = [
        "BeforeType",
        "AfterType",
        "BeforeName",
        "AfterName",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberOccurrence"

def test_numbertypeoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberTypeOccurrence is not None

def test_numbertypeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeOccurrence"

def test_numbertypeoccurrence1_exists():
    # Check that the Enumeration exists
    assert NumberTypeOccurrence1 is not None

def test_numbertypeoccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeOccurrence1]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeOccurrence1"

def test_indicatoroccurrence_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence is not None

def test_indicatoroccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence"

def test_indicatoroccurrence2_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence2 is not None

def test_indicatoroccurrence2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence2]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence2"

def test_numberrangeoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberRangeOccurrence is not None

def test_numberrangeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberRangeOccurrence]
    expected_literals = [
        "BeforeName",
        "BeforeType",
        "AfterName",
        "AfterType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberRangeOccurrence"

def test_numberrangeoccurence_exists():
    # Check that the Enumeration exists
    assert NumberRangeOccurence is not None

def test_numberrangeoccurence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberRangeOccurence]
    expected_literals = [
        "AfterName",
        "BeforeName",
        "BeforeType",
        "AfterType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberRangeOccurence"

def test_typeoccurrence1_exists():
    # Check that the Enumeration exists
    assert TypeOccurrence1 is not None

def test_typeoccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOccurrence1]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOccurrence1"

def test_dependentthoroughfarestype_exists():
    # Check that the Enumeration exists
    assert DependentThoroughfaresType is not None

def test_dependentthoroughfarestype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DependentThoroughfaresType]
    expected_literals = [
        "No",
        "Yes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DependentThoroughfaresType"

def test_indicatoroccurrence1_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence1 is not None

def test_indicatoroccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence1]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence1"

def test_numbertypetype_exists():
    # Check that the Enumeration exists
    assert NumberTypeType is not None

def test_numbertypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeType]
    expected_literals = [
        "Single",
        "Range",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeType"

def test_indicatoroccurrence3_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence3 is not None

def test_indicatoroccurrence3_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence3]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence3"


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
xal_LargeMailUserIdentifier_strategy = st.builds(
    xal_LargeMailUserIdentifier,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    indicator=
        safe_text,
    mixed=
        safe_text
)
xal_LargeMailUserName_strategy = st.builds(
    xal_LargeMailUserName,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_KeyLineCode_strategy = st.builds(
    xal_KeyLineCode,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_EndorsementLineCode_strategy = st.builds(
    xal_EndorsementLineCode,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal_Xal_strategy = st.builds(
    xal_Xal,
    any=
        safe_text,
    version=
        safe_text,
    anyAttribute=
        safe_text
)
xal_FirmName_strategy = st.builds(
    xal_FirmName,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_Firm_strategy = st.builds(
    xal_Firm,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PremiseNumberSuffix_strategy = st.builds(
    xal_PremiseNumberSuffix,
    anyAttribute=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_PremiseNumberPrefix_strategy = st.builds(
    xal_PremiseNumberPrefix,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    value=
        safe_text
)
xal_PremiseNumber_strategy = st.builds(
    xal_PremiseNumber,
    type=
        safe_text,
    code=
        safe_text,
    indicator=
        safe_text,
    indicatorOccurrence=
        safe_text,
    numberTypeOccurrence=
        safe_text,
    mixed=
        safe_text,
    numberType=
        safe_text,
    anyAttribute=
        safe_text
)
xal_ThoroughfareNumberSuffix_strategy = st.builds(
    xal_ThoroughfareNumberSuffix,
    type=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_ThoroughfareNumberPrefix_strategy = st.builds(
    xal_ThoroughfareNumberPrefix,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumber_strategy = st.builds(
    xal_ThoroughfareNumber,
    anyAttribute=
        safe_text,
    numberType=
        safe_text,
    mixed=
        safe_text,
    indicator=
        safe_text,
    code=
        safe_text,
    indicatorOccurrence=
        safe_text,
    type=
        safe_text,
    numberOccurrence=
        safe_text
)
xal_DocumentRoot_strategy = st.builds(
    xal_DocumentRoot,
    mixed=
        safe_text
)
xal_EStringToStringMapEntry_strategy = st.builds(
    xal_EStringToStringMapEntry,
)
xal_ThoroughfarePreDirection_strategy = st.builds(
    xal_ThoroughfarePreDirection,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_DependentThoroughfare_strategy = st.builds(
    xal_DependentThoroughfare,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfarePostDirection_strategy = st.builds(
    xal_ThoroughfarePostDirection,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfareTrailingType_strategy = st.builds(
    xal_ThoroughfareTrailingType,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfareName_strategy = st.builds(
    xal_ThoroughfareName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfareLeadingType_strategy = st.builds(
    xal_ThoroughfareLeadingType,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostalRoute_strategy = st.builds(
    xal_PostalRoute,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_LargeMailUser_strategy = st.builds(
    xal_LargeMailUser,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_Premise_strategy = st.builds(
    xal_Premise,
    premiseDependency=
        safe_text,
    type=
        safe_text,
    premiseThoroughfareConnector=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    premiseDependencyType=
        safe_text
)
xal_PostBox_strategy = st.builds(
    xal_PostBox,
    indicator=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_DependentLocalityNumber_strategy = st.builds(
    xal_DependentLocalityNumber,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    nameNumberOccurrence=
        safe_text
)
xal_DependentLocalityName_strategy = st.builds(
    xal_DependentLocalityName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_DependentLocality_strategy = st.builds(
    xal_DependentLocality,
    type=
        safe_text,
    usageType=
        safe_text,
    connector=
        safe_text,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_MailStop_strategy = st.builds(
    xal_MailStop,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    any=
        safe_text
)
xal_DepartmentName_strategy = st.builds(
    xal_DepartmentName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_Department_strategy = st.builds(
    xal_Department,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_CountryName_strategy = st.builds(
    xal_CountryName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_CountryNameCode_strategy = st.builds(
    xal_CountryNameCode,
    scheme=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_Barcode_strategy = st.builds(
    xal_Barcode,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_BuildingName_strategy = st.builds(
    xal_BuildingName,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    typeOccurrence=
        safe_text,
    mixed=
        safe_text
)
xal_PostalCode_strategy = st.builds(
    xal_PostalCode,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_PostOffice_strategy = st.builds(
    xal_PostOffice,
    indicator=
        safe_text,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLongitudeDirection_strategy = st.builds(
    xal_AddressLongitudeDirection,
    type=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_SubAdministrativeArea_strategy = st.builds(
    xal_SubAdministrativeArea,
    type=
        safe_text,
    any=
        safe_text,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    usageType=
        safe_text
)
xal_AdministrativeAreaName_strategy = st.builds(
    xal_AdministrativeAreaName,
    type=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLine_strategy = st.builds(
    xal_AddressLine,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text
)
xal_AddressLongitude_strategy = st.builds(
    xal_AddressLongitude,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLatitude_strategy = st.builds(
    xal_AddressLatitude,
    code=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLatitudeDirection_strategy = st.builds(
    xal_AddressLatitudeDirection,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_AddressIdentifier_strategy = st.builds(
    xal_AddressIdentifier,
    identifierType=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_AddressLines_strategy = st.builds(
    xal_AddressLines,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_Thoroughfare_strategy = st.builds(
    xal_Thoroughfare,
    anyAttribute=
        safe_text,
    dependentThoroughfaresIndicator=
        safe_text,
    dependentThoroughfares=
        safe_text,
    group=
        safe_text,
    type=
        safe_text,
    dependentThoroughfaresType=
        safe_text,
    dependentThoroughfaresConnector=
        safe_text,
    any=
        safe_text
)
xal_Locality_strategy = st.builds(
    xal_Locality,
    indicator=
        safe_text,
    usageType=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_AdministrativeArea_strategy = st.builds(
    xal_AdministrativeArea,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    usageType=
        safe_text,
    any=
        safe_text,
    type=
        safe_text
)
xal_Country_strategy = st.builds(
    xal_Country,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_PostalServiceElements_strategy = st.builds(
    xal_PostalServiceElements,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_AddressDetails_strategy = st.builds(
    xal_AddressDetails,
    code=
        safe_text,
    currentStatus=
        safe_text,
    validToDate=
        safe_text,
    addressType=
        safe_text,
    validFromDate=
        safe_text,
    usage=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    addressDetailsKey=
        safe_text
)
xal_Address_strategy = st.builds(
    xal_Address,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumberTo_strategy = st.builds(
    xal_ThoroughfareNumberTo,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumberFrom_strategy = st.builds(
    xal_ThoroughfareNumberFrom,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumberRange_strategy = st.builds(
    xal_ThoroughfareNumberRange,
    type=
        safe_text,
    numberRangeOccurrence=
        safe_text,
    rangeType=
        safe_text,
    indicatorOccurrence=
        safe_text,
    indicator=
        safe_text,
    code=
        safe_text,
    separator=
        safe_text,
    anyAttribute=
        safe_text
)
xal_SubPremiseNumberPrefix_strategy = st.builds(
    xal_SubPremiseNumberPrefix,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_SubPremiseNumber_strategy = st.builds(
    xal_SubPremiseNumber,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    premiseNumberSeparator=
        safe_text,
    numberTypeOccurrence=
        safe_text,
    indicatorOccurrence=
        safe_text,
    indicator=
        safe_text
)
xal_SubPremiseNumberSuffix_strategy = st.builds(
    xal_SubPremiseNumberSuffix,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    mixed=
        safe_text
)
xal_SubPremiseLocation_strategy = st.builds(
    xal_SubPremiseLocation,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_SubPremiseName_strategy = st.builds(
    xal_SubPremiseName,
    type=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    typeOccurrence=
        safe_text,
    anyAttribute=
        safe_text
)
xal_SubAdministrativeAreaName_strategy = st.builds(
    xal_SubAdministrativeAreaName,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PremiseNumberRangeTo_strategy = st.builds(
    xal_PremiseNumberRangeTo,
)
xal_PremiseNumberRangeFrom_strategy = st.builds(
    xal_PremiseNumberRangeFrom,
)
xal_SubPremise_strategy = st.builds(
    xal_SubPremise,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_PremiseName_strategy = st.builds(
    xal_PremiseName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    typeOccurrence=
        safe_text
)
xal_PremiseNumberRange_strategy = st.builds(
    xal_PremiseNumberRange,
    rangeType=
        safe_text,
    separator=
        safe_text,
    indicator=
        safe_text,
    numberRangeOccurence=
        safe_text,
    indicatorOccurence=
        safe_text,
    type=
        safe_text
)
xal_PremiseLocation_strategy = st.builds(
    xal_PremiseLocation,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_PostTownSuffix_strategy = st.builds(
    xal_PostTownSuffix,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostTownName_strategy = st.builds(
    xal_PostTownName,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_PostOfficeNumber_strategy = st.builds(
    xal_PostOfficeNumber,
    mixed=
        safe_text,
    indicator=
        safe_text,
    indicatorOccurrence=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostOfficeName_strategy = st.builds(
    xal_PostOfficeName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_PostBoxNumberExtension_strategy = st.builds(
    xal_PostBoxNumberExtension,
    numberExtensionSeparator=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostBoxNumberSuffix_strategy = st.builds(
    xal_PostBoxNumberSuffix,
    mixed=
        safe_text,
    code=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostBoxNumberPrefix_strategy = st.builds(
    xal_PostBoxNumberPrefix,
    numberPrefixSeparator=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_SupplementaryPostalServiceData_strategy = st.builds(
    xal_SupplementaryPostalServiceData,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_PostBoxNumber_strategy = st.builds(
    xal_PostBoxNumber,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_SortingCode_strategy = st.builds(
    xal_SortingCode,
    type=
        safe_text,
    code=
        safe_text
)
xal_PostalRouteNumber_strategy = st.builds(
    xal_PostalRouteNumber,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal_PostalRouteName_strategy = st.builds(
    xal_PostalRouteName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_PostalCodeNumberExtension_strategy = st.builds(
    xal_PostalCodeNumberExtension,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    numberExtensionSeparator=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text
)
xal_PostalCodeNumber_strategy = st.builds(
    xal_PostalCodeNumber,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_PostTown_strategy = st.builds(
    xal_PostTown,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_MailStopNumber_strategy = st.builds(
    xal_MailStopNumber,
    mixed=
        safe_text,
    nameNumberSeparator=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_MailStopName_strategy = st.builds(
    xal_MailStopName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_LocalityName_strategy = st.builds(
    xal_LocalityName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)

@given(instance=xal_LargeMailUserIdentifier_strategy)
@settings(max_examples=50)
def test_xal_largemailuseridentifier_instantiation(instance):
    assert isinstance(instance, xal_LargeMailUserIdentifier)



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_xal_largemailuseridentifier_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_xal_largemailuseridentifier_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_xal_largemailuseridentifier_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_xal_largemailuseridentifier_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_xal_largemailuseridentifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_LargeMailUserName_strategy)
@settings(max_examples=50)
def test_xal_largemailusername_instantiation(instance):
    assert isinstance(instance, xal_LargeMailUserName)



@given(instance=xal_LargeMailUserName_strategy)
def test_xal_largemailusername_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_LargeMailUserName_strategy)
def test_xal_largemailusername_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_LargeMailUserName_strategy)
def test_xal_largemailusername_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LargeMailUserName_strategy)
def test_xal_largemailusername_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_KeyLineCode_strategy)
@settings(max_examples=50)
def test_xal_keylinecode_instantiation(instance):
    assert isinstance(instance, xal_KeyLineCode)



@given(instance=xal_KeyLineCode_strategy)
def test_xal_keylinecode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_KeyLineCode_strategy)
def test_xal_keylinecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_KeyLineCode_strategy)
def test_xal_keylinecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_KeyLineCode_strategy)
def test_xal_keylinecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_EndorsementLineCode_strategy)
@settings(max_examples=50)
def test_xal_endorsementlinecode_instantiation(instance):
    assert isinstance(instance, xal_EndorsementLineCode)



@given(instance=xal_EndorsementLineCode_strategy)
def test_xal_endorsementlinecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_EndorsementLineCode_strategy)
def test_xal_endorsementlinecode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_EndorsementLineCode_strategy)
def test_xal_endorsementlinecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_EndorsementLineCode_strategy)
def test_xal_endorsementlinecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_Xal_strategy)
@settings(max_examples=50)
def test_xal_xal_instantiation(instance):
    assert isinstance(instance, xal_Xal)



@given(instance=xal_Xal_strategy)
def test_xal_xal_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_Xal_strategy)
def test_xal_xal_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xal_Xal_strategy)
def test_xal_xal_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_FirmName_strategy)
@settings(max_examples=50)
def test_xal_firmname_instantiation(instance):
    assert isinstance(instance, xal_FirmName)



@given(instance=xal_FirmName_strategy)
def test_xal_firmname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_FirmName_strategy)
def test_xal_firmname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_FirmName_strategy)
def test_xal_firmname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_FirmName_strategy)
def test_xal_firmname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_Firm_strategy)
@settings(max_examples=50)
def test_xal_firm_instantiation(instance):
    assert isinstance(instance, xal_Firm)



@given(instance=xal_Firm_strategy)
def test_xal_firm_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Firm_strategy)
def test_xal_firm_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_Firm_strategy)
def test_xal_firm_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PremiseNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal_premisenumbersuffix_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberSuffix)



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_xal_premisenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_xal_premisenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_xal_premisenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_xal_premisenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_xal_premisenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_PremiseNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal_premisenumberprefix_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberPrefix)



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_xal_premisenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_xal_premisenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_xal_premisenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_xal_premisenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_xal_premisenumberprefix_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xal_PremiseNumber_strategy)
@settings(max_examples=50)
def test_xal_premisenumber_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumber)



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_numberTypeOccurrence_setter(instance):
    original = instance.numberTypeOccurrence
    instance.numberTypeOccurrence = original
    assert instance.numberTypeOccurrence == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_numberType_setter(instance):
    original = instance.numberType
    instance.numberType = original
    assert instance.numberType == original



@given(instance=xal_PremiseNumber_strategy)
def test_xal_premisenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_ThoroughfareNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarenumbersuffix_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberSuffix)



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_xal_thoroughfarenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_xal_thoroughfarenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_xal_thoroughfarenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_xal_thoroughfarenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_xal_thoroughfarenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_ThoroughfareNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarenumberprefix_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberPrefix)



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_xal_thoroughfarenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_xal_thoroughfarenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_xal_thoroughfarenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_xal_thoroughfarenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_xal_thoroughfarenumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_ThoroughfareNumber_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarenumber_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumber)



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_numberType_setter(instance):
    original = instance.numberType
    instance.numberType = original
    assert instance.numberType == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_xal_thoroughfarenumber_numberOccurrence_setter(instance):
    original = instance.numberOccurrence
    instance.numberOccurrence = original
    assert instance.numberOccurrence == original

@given(instance=xal_DocumentRoot_strategy)
@settings(max_examples=50)
def test_xal_documentroot_instantiation(instance):
    assert isinstance(instance, xal_DocumentRoot)



@given(instance=xal_DocumentRoot_strategy)
def test_xal_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xal_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xal_EStringToStringMapEntry)

@given(instance=xal_ThoroughfarePreDirection_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarepredirection_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfarePreDirection)



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_xal_thoroughfarepredirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_xal_thoroughfarepredirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_xal_thoroughfarepredirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_xal_thoroughfarepredirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_DependentThoroughfare_strategy)
@settings(max_examples=50)
def test_xal_dependentthoroughfare_instantiation(instance):
    assert isinstance(instance, xal_DependentThoroughfare)



@given(instance=xal_DependentThoroughfare_strategy)
def test_xal_dependentthoroughfare_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentThoroughfare_strategy)
def test_xal_dependentthoroughfare_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_DependentThoroughfare_strategy)
def test_xal_dependentthoroughfare_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_ThoroughfarePostDirection_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarepostdirection_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfarePostDirection)



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_xal_thoroughfarepostdirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_xal_thoroughfarepostdirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_xal_thoroughfarepostdirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_xal_thoroughfarepostdirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_ThoroughfareTrailingType_strategy)
@settings(max_examples=50)
def test_xal_thoroughfaretrailingtype_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareTrailingType)



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_xal_thoroughfaretrailingtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_xal_thoroughfaretrailingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_xal_thoroughfaretrailingtype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_xal_thoroughfaretrailingtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_ThoroughfareName_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarename_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareName)



@given(instance=xal_ThoroughfareName_strategy)
def test_xal_thoroughfarename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareName_strategy)
def test_xal_thoroughfarename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareName_strategy)
def test_xal_thoroughfarename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareName_strategy)
def test_xal_thoroughfarename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_ThoroughfareLeadingType_strategy)
@settings(max_examples=50)
def test_xal_thoroughfareleadingtype_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareLeadingType)



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_xal_thoroughfareleadingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_xal_thoroughfareleadingtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_xal_thoroughfareleadingtype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_xal_thoroughfareleadingtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PostalRoute_strategy)
@settings(max_examples=50)
def test_xal_postalroute_instantiation(instance):
    assert isinstance(instance, xal_PostalRoute)



@given(instance=xal_PostalRoute_strategy)
def test_xal_postalroute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostalRoute_strategy)
def test_xal_postalroute_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalRoute_strategy)
def test_xal_postalroute_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_LargeMailUser_strategy)
@settings(max_examples=50)
def test_xal_largemailuser_instantiation(instance):
    assert isinstance(instance, xal_LargeMailUser)



@given(instance=xal_LargeMailUser_strategy)
def test_xal_largemailuser_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_LargeMailUser_strategy)
def test_xal_largemailuser_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LargeMailUser_strategy)
def test_xal_largemailuser_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_Premise_strategy)
@settings(max_examples=50)
def test_xal_premise_instantiation(instance):
    assert isinstance(instance, xal_Premise)



@given(instance=xal_Premise_strategy)
def test_xal_premise_premiseDependency_setter(instance):
    original = instance.premiseDependency
    instance.premiseDependency = original
    assert instance.premiseDependency == original



@given(instance=xal_Premise_strategy)
def test_xal_premise_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Premise_strategy)
def test_xal_premise_premiseThoroughfareConnector_setter(instance):
    original = instance.premiseThoroughfareConnector
    instance.premiseThoroughfareConnector = original
    assert instance.premiseThoroughfareConnector == original



@given(instance=xal_Premise_strategy)
def test_xal_premise_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Premise_strategy)
def test_xal_premise_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_Premise_strategy)
def test_xal_premise_premiseDependencyType_setter(instance):
    original = instance.premiseDependencyType
    instance.premiseDependencyType = original
    assert instance.premiseDependencyType == original

@given(instance=xal_PostBox_strategy)
@settings(max_examples=50)
def test_xal_postbox_instantiation(instance):
    assert isinstance(instance, xal_PostBox)



@given(instance=xal_PostBox_strategy)
def test_xal_postbox_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PostBox_strategy)
def test_xal_postbox_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostBox_strategy)
def test_xal_postbox_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostBox_strategy)
def test_xal_postbox_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_DependentLocalityNumber_strategy)
@settings(max_examples=50)
def test_xal_dependentlocalitynumber_instantiation(instance):
    assert isinstance(instance, xal_DependentLocalityNumber)



@given(instance=xal_DependentLocalityNumber_strategy)
def test_xal_dependentlocalitynumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentLocalityNumber_strategy)
def test_xal_dependentlocalitynumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_DependentLocalityNumber_strategy)
def test_xal_dependentlocalitynumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_DependentLocalityNumber_strategy)
def test_xal_dependentlocalitynumber_nameNumberOccurrence_setter(instance):
    original = instance.nameNumberOccurrence
    instance.nameNumberOccurrence = original
    assert instance.nameNumberOccurrence == original

@given(instance=xal_DependentLocalityName_strategy)
@settings(max_examples=50)
def test_xal_dependentlocalityname_instantiation(instance):
    assert isinstance(instance, xal_DependentLocalityName)



@given(instance=xal_DependentLocalityName_strategy)
def test_xal_dependentlocalityname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_DependentLocalityName_strategy)
def test_xal_dependentlocalityname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentLocalityName_strategy)
def test_xal_dependentlocalityname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_DependentLocalityName_strategy)
def test_xal_dependentlocalityname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_DependentLocality_strategy)
@settings(max_examples=50)
def test_xal_dependentlocality_instantiation(instance):
    assert isinstance(instance, xal_DependentLocality)



@given(instance=xal_DependentLocality_strategy)
def test_xal_dependentlocality_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_DependentLocality_strategy)
def test_xal_dependentlocality_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original



@given(instance=xal_DependentLocality_strategy)
def test_xal_dependentlocality_connector_setter(instance):
    original = instance.connector
    instance.connector = original
    assert instance.connector == original



@given(instance=xal_DependentLocality_strategy)
def test_xal_dependentlocality_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_DependentLocality_strategy)
def test_xal_dependentlocality_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentLocality_strategy)
def test_xal_dependentlocality_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_MailStop_strategy)
@settings(max_examples=50)
def test_xal_mailstop_instantiation(instance):
    assert isinstance(instance, xal_MailStop)



@given(instance=xal_MailStop_strategy)
def test_xal_mailstop_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_MailStop_strategy)
def test_xal_mailstop_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_MailStop_strategy)
def test_xal_mailstop_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_DepartmentName_strategy)
@settings(max_examples=50)
def test_xal_departmentname_instantiation(instance):
    assert isinstance(instance, xal_DepartmentName)



@given(instance=xal_DepartmentName_strategy)
def test_xal_departmentname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DepartmentName_strategy)
def test_xal_departmentname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_DepartmentName_strategy)
def test_xal_departmentname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_DepartmentName_strategy)
def test_xal_departmentname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_Department_strategy)
@settings(max_examples=50)
def test_xal_department_instantiation(instance):
    assert isinstance(instance, xal_Department)



@given(instance=xal_Department_strategy)
def test_xal_department_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Department_strategy)
def test_xal_department_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Department_strategy)
def test_xal_department_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_CountryName_strategy)
@settings(max_examples=50)
def test_xal_countryname_instantiation(instance):
    assert isinstance(instance, xal_CountryName)



@given(instance=xal_CountryName_strategy)
def test_xal_countryname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_CountryName_strategy)
def test_xal_countryname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_CountryName_strategy)
def test_xal_countryname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_CountryName_strategy)
def test_xal_countryname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_CountryNameCode_strategy)
@settings(max_examples=50)
def test_xal_countrynamecode_instantiation(instance):
    assert isinstance(instance, xal_CountryNameCode)



@given(instance=xal_CountryNameCode_strategy)
def test_xal_countrynamecode_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original



@given(instance=xal_CountryNameCode_strategy)
def test_xal_countrynamecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_CountryNameCode_strategy)
def test_xal_countrynamecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_CountryNameCode_strategy)
def test_xal_countrynamecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_Barcode_strategy)
@settings(max_examples=50)
def test_xal_barcode_instantiation(instance):
    assert isinstance(instance, xal_Barcode)



@given(instance=xal_Barcode_strategy)
def test_xal_barcode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Barcode_strategy)
def test_xal_barcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Barcode_strategy)
def test_xal_barcode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_Barcode_strategy)
def test_xal_barcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_BuildingName_strategy)
@settings(max_examples=50)
def test_xal_buildingname_instantiation(instance):
    assert isinstance(instance, xal_BuildingName)



@given(instance=xal_BuildingName_strategy)
def test_xal_buildingname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_BuildingName_strategy)
def test_xal_buildingname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_BuildingName_strategy)
def test_xal_buildingname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_BuildingName_strategy)
def test_xal_buildingname_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original



@given(instance=xal_BuildingName_strategy)
def test_xal_buildingname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_PostalCode_strategy)
@settings(max_examples=50)
def test_xal_postalcode_instantiation(instance):
    assert isinstance(instance, xal_PostalCode)



@given(instance=xal_PostalCode_strategy)
def test_xal_postalcode_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_PostalCode_strategy)
def test_xal_postalcode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalCode_strategy)
def test_xal_postalcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_PostOffice_strategy)
@settings(max_examples=50)
def test_xal_postoffice_instantiation(instance):
    assert isinstance(instance, xal_PostOffice)



@given(instance=xal_PostOffice_strategy)
def test_xal_postoffice_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PostOffice_strategy)
def test_xal_postoffice_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostOffice_strategy)
def test_xal_postoffice_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_PostOffice_strategy)
def test_xal_postoffice_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_AddressLongitudeDirection_strategy)
@settings(max_examples=50)
def test_xal_addresslongitudedirection_instantiation(instance):
    assert isinstance(instance, xal_AddressLongitudeDirection)



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_xal_addresslongitudedirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_xal_addresslongitudedirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_xal_addresslongitudedirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_xal_addresslongitudedirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_SubAdministrativeArea_strategy)
@settings(max_examples=50)
def test_xal_subadministrativearea_instantiation(instance):
    assert isinstance(instance, xal_SubAdministrativeArea)



@given(instance=xal_SubAdministrativeArea_strategy)
def test_xal_subadministrativearea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_xal_subadministrativearea_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_xal_subadministrativearea_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_xal_subadministrativearea_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_xal_subadministrativearea_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original

@given(instance=xal_AdministrativeAreaName_strategy)
@settings(max_examples=50)
def test_xal_administrativeareaname_instantiation(instance):
    assert isinstance(instance, xal_AdministrativeAreaName)



@given(instance=xal_AdministrativeAreaName_strategy)
def test_xal_administrativeareaname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AdministrativeAreaName_strategy)
def test_xal_administrativeareaname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AdministrativeAreaName_strategy)
def test_xal_administrativeareaname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AdministrativeAreaName_strategy)
def test_xal_administrativeareaname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_AddressLine_strategy)
@settings(max_examples=50)
def test_xal_addressline_instantiation(instance):
    assert isinstance(instance, xal_AddressLine)



@given(instance=xal_AddressLine_strategy)
def test_xal_addressline_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLine_strategy)
def test_xal_addressline_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressLine_strategy)
def test_xal_addressline_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLine_strategy)
def test_xal_addressline_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_AddressLongitude_strategy)
@settings(max_examples=50)
def test_xal_addresslongitude_instantiation(instance):
    assert isinstance(instance, xal_AddressLongitude)



@given(instance=xal_AddressLongitude_strategy)
def test_xal_addresslongitude_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLongitude_strategy)
def test_xal_addresslongitude_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLongitude_strategy)
def test_xal_addresslongitude_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLongitude_strategy)
def test_xal_addresslongitude_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_AddressLatitude_strategy)
@settings(max_examples=50)
def test_xal_addresslatitude_instantiation(instance):
    assert isinstance(instance, xal_AddressLatitude)



@given(instance=xal_AddressLatitude_strategy)
def test_xal_addresslatitude_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLatitude_strategy)
def test_xal_addresslatitude_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLatitude_strategy)
def test_xal_addresslatitude_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLatitude_strategy)
def test_xal_addresslatitude_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_AddressLatitudeDirection_strategy)
@settings(max_examples=50)
def test_xal_addresslatitudedirection_instantiation(instance):
    assert isinstance(instance, xal_AddressLatitudeDirection)



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_xal_addresslatitudedirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_xal_addresslatitudedirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_xal_addresslatitudedirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_xal_addresslatitudedirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_AddressIdentifier_strategy)
@settings(max_examples=50)
def test_xal_addressidentifier_instantiation(instance):
    assert isinstance(instance, xal_AddressIdentifier)



@given(instance=xal_AddressIdentifier_strategy)
def test_xal_addressidentifier_identifierType_setter(instance):
    original = instance.identifierType
    instance.identifierType = original
    assert instance.identifierType == original



@given(instance=xal_AddressIdentifier_strategy)
def test_xal_addressidentifier_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressIdentifier_strategy)
def test_xal_addressidentifier_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressIdentifier_strategy)
def test_xal_addressidentifier_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressIdentifier_strategy)
def test_xal_addressidentifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_AddressLines_strategy)
@settings(max_examples=50)
def test_xal_addresslines_instantiation(instance):
    assert isinstance(instance, xal_AddressLines)



@given(instance=xal_AddressLines_strategy)
def test_xal_addresslines_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressLines_strategy)
def test_xal_addresslines_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_Thoroughfare_strategy)
@settings(max_examples=50)
def test_xal_thoroughfare_instantiation(instance):
    assert isinstance(instance, xal_Thoroughfare)



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_dependentThoroughfaresIndicator_setter(instance):
    original = instance.dependentThoroughfaresIndicator
    instance.dependentThoroughfaresIndicator = original
    assert instance.dependentThoroughfaresIndicator == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_dependentThoroughfares_setter(instance):
    original = instance.dependentThoroughfares
    instance.dependentThoroughfares = original
    assert instance.dependentThoroughfares == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_dependentThoroughfaresType_setter(instance):
    original = instance.dependentThoroughfaresType
    instance.dependentThoroughfaresType = original
    assert instance.dependentThoroughfaresType == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_dependentThoroughfaresConnector_setter(instance):
    original = instance.dependentThoroughfaresConnector
    instance.dependentThoroughfaresConnector = original
    assert instance.dependentThoroughfaresConnector == original



@given(instance=xal_Thoroughfare_strategy)
def test_xal_thoroughfare_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_Locality_strategy)
@settings(max_examples=50)
def test_xal_locality_instantiation(instance):
    assert isinstance(instance, xal_Locality)



@given(instance=xal_Locality_strategy)
def test_xal_locality_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_Locality_strategy)
def test_xal_locality_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original



@given(instance=xal_Locality_strategy)
def test_xal_locality_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Locality_strategy)
def test_xal_locality_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Locality_strategy)
def test_xal_locality_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_AdministrativeArea_strategy)
@settings(max_examples=50)
def test_xal_administrativearea_instantiation(instance):
    assert isinstance(instance, xal_AdministrativeArea)



@given(instance=xal_AdministrativeArea_strategy)
def test_xal_administrativearea_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_AdministrativeArea_strategy)
def test_xal_administrativearea_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AdministrativeArea_strategy)
def test_xal_administrativearea_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original



@given(instance=xal_AdministrativeArea_strategy)
def test_xal_administrativearea_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_AdministrativeArea_strategy)
def test_xal_administrativearea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_Country_strategy)
@settings(max_examples=50)
def test_xal_country_instantiation(instance):
    assert isinstance(instance, xal_Country)



@given(instance=xal_Country_strategy)
def test_xal_country_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Country_strategy)
def test_xal_country_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_PostalServiceElements_strategy)
@settings(max_examples=50)
def test_xal_postalserviceelements_instantiation(instance):
    assert isinstance(instance, xal_PostalServiceElements)



@given(instance=xal_PostalServiceElements_strategy)
def test_xal_postalserviceelements_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_PostalServiceElements_strategy)
def test_xal_postalserviceelements_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalServiceElements_strategy)
def test_xal_postalserviceelements_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_AddressDetails_strategy)
@settings(max_examples=50)
def test_xal_addressdetails_instantiation(instance):
    assert isinstance(instance, xal_AddressDetails)



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_currentStatus_setter(instance):
    original = instance.currentStatus
    instance.currentStatus = original
    assert instance.currentStatus == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_validToDate_setter(instance):
    original = instance.validToDate
    instance.validToDate = original
    assert instance.validToDate == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_addressType_setter(instance):
    original = instance.addressType
    instance.addressType = original
    assert instance.addressType == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_validFromDate_setter(instance):
    original = instance.validFromDate
    instance.validFromDate = original
    assert instance.validFromDate == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_usage_setter(instance):
    original = instance.usage
    instance.usage = original
    assert instance.usage == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_AddressDetails_strategy)
def test_xal_addressdetails_addressDetailsKey_setter(instance):
    original = instance.addressDetailsKey
    instance.addressDetailsKey = original
    assert instance.addressDetailsKey == original

@given(instance=xal_Address_strategy)
@settings(max_examples=50)
def test_xal_address_instantiation(instance):
    assert isinstance(instance, xal_Address)



@given(instance=xal_Address_strategy)
def test_xal_address_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Address_strategy)
def test_xal_address_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_Address_strategy)
def test_xal_address_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Address_strategy)
def test_xal_address_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_ThoroughfareNumberTo_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarenumberto_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberTo)



@given(instance=xal_ThoroughfareNumberTo_strategy)
def test_xal_thoroughfarenumberto_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberTo_strategy)
def test_xal_thoroughfarenumberto_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumberTo_strategy)
def test_xal_thoroughfarenumberto_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_ThoroughfareNumberFrom_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarenumberfrom_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberFrom)



@given(instance=xal_ThoroughfareNumberFrom_strategy)
def test_xal_thoroughfarenumberfrom_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberFrom_strategy)
def test_xal_thoroughfarenumberfrom_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumberFrom_strategy)
def test_xal_thoroughfarenumberfrom_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_ThoroughfareNumberRange_strategy)
@settings(max_examples=50)
def test_xal_thoroughfarenumberrange_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberRange)



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_numberRangeOccurrence_setter(instance):
    original = instance.numberRangeOccurrence
    instance.numberRangeOccurrence = original
    assert instance.numberRangeOccurrence == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_rangeType_setter(instance):
    original = instance.rangeType
    instance.rangeType = original
    assert instance.rangeType == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_xal_thoroughfarenumberrange_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_SubPremiseNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal_subpremisenumberprefix_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseNumberPrefix)



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_xal_subpremisenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_xal_subpremisenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_xal_subpremisenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_xal_subpremisenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_xal_subpremisenumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_SubPremiseNumber_strategy)
@settings(max_examples=50)
def test_xal_subpremisenumber_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseNumber)



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_premiseNumberSeparator_setter(instance):
    original = instance.premiseNumberSeparator
    instance.premiseNumberSeparator = original
    assert instance.premiseNumberSeparator == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_numberTypeOccurrence_setter(instance):
    original = instance.numberTypeOccurrence
    instance.numberTypeOccurrence = original
    assert instance.numberTypeOccurrence == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_xal_subpremisenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal_SubPremiseNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal_subpremisenumbersuffix_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseNumberSuffix)



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_xal_subpremisenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_xal_subpremisenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_xal_subpremisenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_xal_subpremisenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_xal_subpremisenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_SubPremiseLocation_strategy)
@settings(max_examples=50)
def test_xal_subpremiselocation_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseLocation)



@given(instance=xal_SubPremiseLocation_strategy)
def test_xal_subpremiselocation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubPremiseLocation_strategy)
def test_xal_subpremiselocation_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_SubPremiseName_strategy)
@settings(max_examples=50)
def test_xal_subpremisename_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseName)



@given(instance=xal_SubPremiseName_strategy)
def test_xal_subpremisename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseName_strategy)
def test_xal_subpremisename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubPremiseName_strategy)
def test_xal_subpremisename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseName_strategy)
def test_xal_subpremisename_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original



@given(instance=xal_SubPremiseName_strategy)
def test_xal_subpremisename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_SubAdministrativeAreaName_strategy)
@settings(max_examples=50)
def test_xal_subadministrativeareaname_instantiation(instance):
    assert isinstance(instance, xal_SubAdministrativeAreaName)



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_xal_subadministrativeareaname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_xal_subadministrativeareaname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_xal_subadministrativeareaname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_xal_subadministrativeareaname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PremiseNumberRangeTo_strategy)
@settings(max_examples=50)
def test_xal_premisenumberrangeto_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberRangeTo)

@given(instance=xal_PremiseNumberRangeFrom_strategy)
@settings(max_examples=50)
def test_xal_premisenumberrangefrom_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberRangeFrom)

@given(instance=xal_SubPremise_strategy)
@settings(max_examples=50)
def test_xal_subpremise_instantiation(instance):
    assert isinstance(instance, xal_SubPremise)



@given(instance=xal_SubPremise_strategy)
def test_xal_subpremise_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremise_strategy)
def test_xal_subpremise_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremise_strategy)
def test_xal_subpremise_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal_PremiseName_strategy)
@settings(max_examples=50)
def test_xal_premisename_instantiation(instance):
    assert isinstance(instance, xal_PremiseName)



@given(instance=xal_PremiseName_strategy)
def test_xal_premisename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PremiseName_strategy)
def test_xal_premisename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseName_strategy)
def test_xal_premisename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseName_strategy)
def test_xal_premisename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseName_strategy)
def test_xal_premisename_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original

@given(instance=xal_PremiseNumberRange_strategy)
@settings(max_examples=50)
def test_xal_premisenumberrange_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberRange)



@given(instance=xal_PremiseNumberRange_strategy)
def test_xal_premisenumberrange_rangeType_setter(instance):
    original = instance.rangeType
    instance.rangeType = original
    assert instance.rangeType == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_xal_premisenumberrange_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_xal_premisenumberrange_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_xal_premisenumberrange_numberRangeOccurence_setter(instance):
    original = instance.numberRangeOccurence
    instance.numberRangeOccurence = original
    assert instance.numberRangeOccurence == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_xal_premisenumberrange_indicatorOccurence_setter(instance):
    original = instance.indicatorOccurence
    instance.indicatorOccurence = original
    assert instance.indicatorOccurence == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_xal_premisenumberrange_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_PremiseLocation_strategy)
@settings(max_examples=50)
def test_xal_premiselocation_instantiation(instance):
    assert isinstance(instance, xal_PremiseLocation)



@given(instance=xal_PremiseLocation_strategy)
def test_xal_premiselocation_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseLocation_strategy)
def test_xal_premiselocation_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseLocation_strategy)
def test_xal_premiselocation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_PostTownSuffix_strategy)
@settings(max_examples=50)
def test_xal_posttownsuffix_instantiation(instance):
    assert isinstance(instance, xal_PostTownSuffix)



@given(instance=xal_PostTownSuffix_strategy)
def test_xal_posttownsuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostTownSuffix_strategy)
def test_xal_posttownsuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostTownSuffix_strategy)
def test_xal_posttownsuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PostTownName_strategy)
@settings(max_examples=50)
def test_xal_posttownname_instantiation(instance):
    assert isinstance(instance, xal_PostTownName)



@given(instance=xal_PostTownName_strategy)
def test_xal_posttownname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostTownName_strategy)
def test_xal_posttownname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostTownName_strategy)
def test_xal_posttownname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostTownName_strategy)
def test_xal_posttownname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_PostOfficeNumber_strategy)
@settings(max_examples=50)
def test_xal_postofficenumber_instantiation(instance):
    assert isinstance(instance, xal_PostOfficeNumber)



@given(instance=xal_PostOfficeNumber_strategy)
def test_xal_postofficenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_xal_postofficenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_xal_postofficenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_xal_postofficenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_xal_postofficenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PostOfficeName_strategy)
@settings(max_examples=50)
def test_xal_postofficename_instantiation(instance):
    assert isinstance(instance, xal_PostOfficeName)



@given(instance=xal_PostOfficeName_strategy)
def test_xal_postofficename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostOfficeName_strategy)
def test_xal_postofficename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostOfficeName_strategy)
def test_xal_postofficename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostOfficeName_strategy)
def test_xal_postofficename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_PostBoxNumberExtension_strategy)
@settings(max_examples=50)
def test_xal_postboxnumberextension_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumberExtension)



@given(instance=xal_PostBoxNumberExtension_strategy)
def test_xal_postboxnumberextension_numberExtensionSeparator_setter(instance):
    original = instance.numberExtensionSeparator
    instance.numberExtensionSeparator = original
    assert instance.numberExtensionSeparator == original



@given(instance=xal_PostBoxNumberExtension_strategy)
def test_xal_postboxnumberextension_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostBoxNumberExtension_strategy)
def test_xal_postboxnumberextension_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PostBoxNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal_postboxnumbersuffix_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumberSuffix)



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_xal_postboxnumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_xal_postboxnumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_xal_postboxnumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_xal_postboxnumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_PostBoxNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal_postboxnumberprefix_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumberPrefix)



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_xal_postboxnumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_xal_postboxnumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_xal_postboxnumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_xal_postboxnumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_SupplementaryPostalServiceData_strategy)
@settings(max_examples=50)
def test_xal_supplementarypostalservicedata_instantiation(instance):
    assert isinstance(instance, xal_SupplementaryPostalServiceData)



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_xal_supplementarypostalservicedata_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_xal_supplementarypostalservicedata_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_xal_supplementarypostalservicedata_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_xal_supplementarypostalservicedata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_PostBoxNumber_strategy)
@settings(max_examples=50)
def test_xal_postboxnumber_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumber)



@given(instance=xal_PostBoxNumber_strategy)
def test_xal_postboxnumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostBoxNumber_strategy)
def test_xal_postboxnumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostBoxNumber_strategy)
def test_xal_postboxnumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_SortingCode_strategy)
@settings(max_examples=50)
def test_xal_sortingcode_instantiation(instance):
    assert isinstance(instance, xal_SortingCode)



@given(instance=xal_SortingCode_strategy)
def test_xal_sortingcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SortingCode_strategy)
def test_xal_sortingcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_PostalRouteNumber_strategy)
@settings(max_examples=50)
def test_xal_postalroutenumber_instantiation(instance):
    assert isinstance(instance, xal_PostalRouteNumber)



@given(instance=xal_PostalRouteNumber_strategy)
def test_xal_postalroutenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostalRouteNumber_strategy)
def test_xal_postalroutenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalRouteNumber_strategy)
def test_xal_postalroutenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_PostalRouteName_strategy)
@settings(max_examples=50)
def test_xal_postalroutename_instantiation(instance):
    assert isinstance(instance, xal_PostalRouteName)



@given(instance=xal_PostalRouteName_strategy)
def test_xal_postalroutename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostalRouteName_strategy)
def test_xal_postalroutename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalRouteName_strategy)
def test_xal_postalroutename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostalRouteName_strategy)
def test_xal_postalroutename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_PostalCodeNumberExtension_strategy)
@settings(max_examples=50)
def test_xal_postalcodenumberextension_instantiation(instance):
    assert isinstance(instance, xal_PostalCodeNumberExtension)



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_xal_postalcodenumberextension_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_xal_postalcodenumberextension_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_xal_postalcodenumberextension_numberExtensionSeparator_setter(instance):
    original = instance.numberExtensionSeparator
    instance.numberExtensionSeparator = original
    assert instance.numberExtensionSeparator == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_xal_postalcodenumberextension_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_xal_postalcodenumberextension_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal_PostalCodeNumber_strategy)
@settings(max_examples=50)
def test_xal_postalcodenumber_instantiation(instance):
    assert isinstance(instance, xal_PostalCodeNumber)



@given(instance=xal_PostalCodeNumber_strategy)
def test_xal_postalcodenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostalCodeNumber_strategy)
def test_xal_postalcodenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalCodeNumber_strategy)
def test_xal_postalcodenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostalCodeNumber_strategy)
def test_xal_postalcodenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal_PostTown_strategy)
@settings(max_examples=50)
def test_xal_posttown_instantiation(instance):
    assert isinstance(instance, xal_PostTown)



@given(instance=xal_PostTown_strategy)
def test_xal_posttown_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostTown_strategy)
def test_xal_posttown_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_MailStopNumber_strategy)
@settings(max_examples=50)
def test_xal_mailstopnumber_instantiation(instance):
    assert isinstance(instance, xal_MailStopNumber)



@given(instance=xal_MailStopNumber_strategy)
def test_xal_mailstopnumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_MailStopNumber_strategy)
def test_xal_mailstopnumber_nameNumberSeparator_setter(instance):
    original = instance.nameNumberSeparator
    instance.nameNumberSeparator = original
    assert instance.nameNumberSeparator == original



@given(instance=xal_MailStopNumber_strategy)
def test_xal_mailstopnumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_MailStopNumber_strategy)
def test_xal_mailstopnumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal_MailStopName_strategy)
@settings(max_examples=50)
def test_xal_mailstopname_instantiation(instance):
    assert isinstance(instance, xal_MailStopName)



@given(instance=xal_MailStopName_strategy)
def test_xal_mailstopname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_MailStopName_strategy)
def test_xal_mailstopname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_MailStopName_strategy)
def test_xal_mailstopname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_MailStopName_strategy)
def test_xal_mailstopname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal_LocalityName_strategy)
@settings(max_examples=50)
def test_xal_localityname_instantiation(instance):
    assert isinstance(instance, xal_LocalityName)



@given(instance=xal_LocalityName_strategy)
def test_xal_localityname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LocalityName_strategy)
def test_xal_localityname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_LocalityName_strategy)
def test_xal_localityname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_LocalityName_strategy)
def test_xal_localityname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original
