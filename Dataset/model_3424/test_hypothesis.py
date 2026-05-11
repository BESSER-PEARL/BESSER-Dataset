import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xal::ThoroughfareNumberTo,
    xal::ThoroughfareNumberFrom,
    xal::ThoroughfareNumberRange,
    xal::SubPremiseNumberPrefix,
    xal::SubPremiseNumber,
    xal::SubPremiseNumberSuffix,
    xal::SubPremiseLocation,
    xal::SubPremiseName,
    xal::SubAdministrativeAreaName,
    xal::PremiseNumberRangeTo,
    xal::PremiseNumberRangeFrom,
    xal::SubPremise,
    xal::PremiseName,
    xal::PremiseNumberRange,
    xal::PremiseLocation,
    xal::PostTownSuffix,
    xal::PostTownName,
    xal::PostOfficeNumber,
    xal::PostOfficeName,
    xal::PostBoxNumberExtension,
    xal::PostBoxNumberSuffix,
    xal::PostBoxNumberPrefix,
    xal::SupplementaryPostalServiceData,
    xal::PostBoxNumber,
    xal::SortingCode,
    xal::PostalRouteNumber,
    xal::PostalRouteName,
    xal::PostalCodeNumberExtension,
    xal::PostalCodeNumber,
    xal::PostTown,
    xal::MailStopNumber,
    xal::MailStopName,
    xal::LocalityName,
    xal::LargeMailUserIdentifier,
    xal::LargeMailUserName,
    xal::KeyLineCode,
    xal::EndorsementLineCode,
    xal::Xal,
    xal::FirmName,
    xal::Firm,
    xal::PremiseNumberSuffix,
    xal::PremiseNumberPrefix,
    xal::PremiseNumber,
    xal::ThoroughfareNumberSuffix,
    xal::ThoroughfareNumberPrefix,
    xal::ThoroughfareNumber,
    xal::DocumentRoot,
    xal::EStringToStringMapEntry,
    xal::ThoroughfarePreDirection,
    xal::DependentThoroughfare,
    xal::ThoroughfarePostDirection,
    xal::ThoroughfareTrailingType,
    xal::ThoroughfareName,
    xal::ThoroughfareLeadingType,
    xal::PostalRoute,
    xal::LargeMailUser,
    xal::Premise,
    xal::PostBox,
    xal::DependentLocalityNumber,
    xal::DependentLocalityName,
    xal::DependentLocality,
    xal::MailStop,
    xal::DepartmentName,
    xal::Department,
    xal::CountryName,
    xal::CountryNameCode,
    xal::Barcode,
    xal::BuildingName,
    xal::PostalCode,
    xal::PostOffice,
    xal::AddressLongitudeDirection,
    xal::SubAdministrativeArea,
    xal::AdministrativeAreaName,
    xal::AddressLine,
    xal::AddressLongitude,
    xal::AddressLatitude,
    xal::AddressLatitudeDirection,
    xal::AddressIdentifier,
    xal::AddressLines,
    xal::Thoroughfare,
    xal::Locality,
    xal::AdministrativeArea,
    xal::Country,
    xal::PostalServiceElements,
    xal::AddressDetails,
    xal::Address,
    IndicatorOccurrence1,
    TypeOccurrence2,
    NumberTypeOccurrence,
    NumberOccurrence,
    IndicatorOccurence,
    RangeTypeType,
    IndicatorOccurrence,
    NumberRangeOccurrence,
    NameNumberOccurrence,
    TypeOccurrence,
    IndicatorOccurrence3,
    DependentThoroughfaresType,
    NumberTypeType,
    IndicatorOccurrence4,
    NumberTypeOccurrence1,
    NumberTypeType1,
    TypeOccurrence1,
    NumberRangeOccurence,
    IndicatorOccurrence2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xal::thoroughfarenumberto_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareNumberTo)


def test_xal::thoroughfarenumberto_constructor_exists():
    assert callable(xal::ThoroughfareNumberTo.__init__)


def test_xal::thoroughfarenumberto_constructor_args():
    sig = inspect.signature(xal::ThoroughfareNumberTo.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::thoroughfarenumberto_has_code():
    assert hasattr(xal::ThoroughfareNumberTo, "code")
    descriptor = None
    for klass in xal::ThoroughfareNumberTo.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberto_has_anyAttribute():
    assert hasattr(xal::ThoroughfareNumberTo, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareNumberTo.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberto_has_mixed():
    assert hasattr(xal::ThoroughfareNumberTo, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareNumberTo.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarenumberfrom_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareNumberFrom)


def test_xal::thoroughfarenumberfrom_constructor_exists():
    assert callable(xal::ThoroughfareNumberFrom.__init__)


def test_xal::thoroughfarenumberfrom_constructor_args():
    sig = inspect.signature(xal::ThoroughfareNumberFrom.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::thoroughfarenumberfrom_has_code():
    assert hasattr(xal::ThoroughfareNumberFrom, "code")
    descriptor = None
    for klass in xal::ThoroughfareNumberFrom.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberfrom_has_mixed():
    assert hasattr(xal::ThoroughfareNumberFrom, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareNumberFrom.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberfrom_has_anyAttribute():
    assert hasattr(xal::ThoroughfareNumberFrom, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareNumberFrom.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarenumberrange_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareNumberRange)


def test_xal::thoroughfarenumberrange_constructor_exists():
    assert callable(xal::ThoroughfareNumberRange.__init__)


def test_xal::thoroughfarenumberrange_constructor_args():
    sig = inspect.signature(xal::ThoroughfareNumberRange.__init__)
    params = list(sig.parameters.keys())
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberRangeOccurrence" in params, "Missing parameter 'numberRangeOccurrence'"
    assert "code" in params, "Missing parameter 'code'"
    assert "rangeType" in params, "Missing parameter 'rangeType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "indicator" in params, "Missing parameter 'indicator'"

def test_xal::thoroughfarenumberrange_has_indicatorOccurrence():
    assert hasattr(xal::ThoroughfareNumberRange, "indicatorOccurrence")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_anyAttribute():
    assert hasattr(xal::ThoroughfareNumberRange, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_numberRangeOccurrence():
    assert hasattr(xal::ThoroughfareNumberRange, "numberRangeOccurrence")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "numberRangeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberRangeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_code():
    assert hasattr(xal::ThoroughfareNumberRange, "code")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_rangeType():
    assert hasattr(xal::ThoroughfareNumberRange, "rangeType")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "rangeType" in klass.__dict__:
            descriptor = klass.__dict__["rangeType"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_type():
    assert hasattr(xal::ThoroughfareNumberRange, "type")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_separator():
    assert hasattr(xal::ThoroughfareNumberRange, "separator")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberrange_has_indicator():
    assert hasattr(xal::ThoroughfareNumberRange, "indicator")
    descriptor = None
    for klass in xal::ThoroughfareNumberRange.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)



def test_xal::subpremisenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal::SubPremiseNumberPrefix)


def test_xal::subpremisenumberprefix_constructor_exists():
    assert callable(xal::SubPremiseNumberPrefix.__init__)


def test_xal::subpremisenumberprefix_constructor_args():
    sig = inspect.signature(xal::SubPremiseNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::subpremisenumberprefix_has_type():
    assert hasattr(xal::SubPremiseNumberPrefix, "type")
    descriptor = None
    for klass in xal::SubPremiseNumberPrefix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumberprefix_has_anyAttribute():
    assert hasattr(xal::SubPremiseNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal::SubPremiseNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumberprefix_has_code():
    assert hasattr(xal::SubPremiseNumberPrefix, "code")
    descriptor = None
    for klass in xal::SubPremiseNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal::SubPremiseNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal::SubPremiseNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumberprefix_has_mixed():
    assert hasattr(xal::SubPremiseNumberPrefix, "mixed")
    descriptor = None
    for klass in xal::SubPremiseNumberPrefix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::subpremisenumber_is_not_abstract():
    assert not inspect.isabstract(xal::SubPremiseNumber)


def test_xal::subpremisenumber_constructor_exists():
    assert callable(xal::SubPremiseNumber.__init__)


def test_xal::subpremisenumber_constructor_args():
    sig = inspect.signature(xal::SubPremiseNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "numberTypeOccurrence" in params, "Missing parameter 'numberTypeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "premiseNumberSeparator" in params, "Missing parameter 'premiseNumberSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::subpremisenumber_has_code():
    assert hasattr(xal::SubPremiseNumber, "code")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_indicatorOccurrence():
    assert hasattr(xal::SubPremiseNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_numberTypeOccurrence():
    assert hasattr(xal::SubPremiseNumber, "numberTypeOccurrence")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "numberTypeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberTypeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_mixed():
    assert hasattr(xal::SubPremiseNumber, "mixed")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_indicator():
    assert hasattr(xal::SubPremiseNumber, "indicator")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_premiseNumberSeparator():
    assert hasattr(xal::SubPremiseNumber, "premiseNumberSeparator")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "premiseNumberSeparator" in klass.__dict__:
            descriptor = klass.__dict__["premiseNumberSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_anyAttribute():
    assert hasattr(xal::SubPremiseNumber, "anyAttribute")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumber_has_type():
    assert hasattr(xal::SubPremiseNumber, "type")
    descriptor = None
    for klass in xal::SubPremiseNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::subpremisenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal::SubPremiseNumberSuffix)


def test_xal::subpremisenumbersuffix_constructor_exists():
    assert callable(xal::SubPremiseNumberSuffix.__init__)


def test_xal::subpremisenumbersuffix_constructor_args():
    sig = inspect.signature(xal::SubPremiseNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::subpremisenumbersuffix_has_code():
    assert hasattr(xal::SubPremiseNumberSuffix, "code")
    descriptor = None
    for klass in xal::SubPremiseNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal::SubPremiseNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal::SubPremiseNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumbersuffix_has_type():
    assert hasattr(xal::SubPremiseNumberSuffix, "type")
    descriptor = None
    for klass in xal::SubPremiseNumberSuffix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumbersuffix_has_anyAttribute():
    assert hasattr(xal::SubPremiseNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal::SubPremiseNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisenumbersuffix_has_mixed():
    assert hasattr(xal::SubPremiseNumberSuffix, "mixed")
    descriptor = None
    for klass in xal::SubPremiseNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::subpremiselocation_is_not_abstract():
    assert not inspect.isabstract(xal::SubPremiseLocation)


def test_xal::subpremiselocation_constructor_exists():
    assert callable(xal::SubPremiseLocation.__init__)


def test_xal::subpremiselocation_constructor_args():
    sig = inspect.signature(xal::SubPremiseLocation.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::subpremiselocation_has_code():
    assert hasattr(xal::SubPremiseLocation, "code")
    descriptor = None
    for klass in xal::SubPremiseLocation.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremiselocation_has_mixed():
    assert hasattr(xal::SubPremiseLocation, "mixed")
    descriptor = None
    for klass in xal::SubPremiseLocation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::subpremisename_is_not_abstract():
    assert not inspect.isabstract(xal::SubPremiseName)


def test_xal::subpremisename_constructor_exists():
    assert callable(xal::SubPremiseName.__init__)


def test_xal::subpremisename_constructor_args():
    sig = inspect.signature(xal::SubPremiseName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::subpremisename_has_anyAttribute():
    assert hasattr(xal::SubPremiseName, "anyAttribute")
    descriptor = None
    for klass in xal::SubPremiseName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisename_has_code():
    assert hasattr(xal::SubPremiseName, "code")
    descriptor = None
    for klass in xal::SubPremiseName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisename_has_type():
    assert hasattr(xal::SubPremiseName, "type")
    descriptor = None
    for klass in xal::SubPremiseName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisename_has_typeOccurrence():
    assert hasattr(xal::SubPremiseName, "typeOccurrence")
    descriptor = None
    for klass in xal::SubPremiseName.__mro__:
        if "typeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["typeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremisename_has_mixed():
    assert hasattr(xal::SubPremiseName, "mixed")
    descriptor = None
    for klass in xal::SubPremiseName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::subadministrativeareaname_is_not_abstract():
    assert not inspect.isabstract(xal::SubAdministrativeAreaName)


def test_xal::subadministrativeareaname_constructor_exists():
    assert callable(xal::SubAdministrativeAreaName.__init__)


def test_xal::subadministrativeareaname_constructor_args():
    sig = inspect.signature(xal::SubAdministrativeAreaName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::subadministrativeareaname_has_mixed():
    assert hasattr(xal::SubAdministrativeAreaName, "mixed")
    descriptor = None
    for klass in xal::SubAdministrativeAreaName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativeareaname_has_type():
    assert hasattr(xal::SubAdministrativeAreaName, "type")
    descriptor = None
    for klass in xal::SubAdministrativeAreaName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativeareaname_has_anyAttribute():
    assert hasattr(xal::SubAdministrativeAreaName, "anyAttribute")
    descriptor = None
    for klass in xal::SubAdministrativeAreaName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativeareaname_has_code():
    assert hasattr(xal::SubAdministrativeAreaName, "code")
    descriptor = None
    for klass in xal::SubAdministrativeAreaName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::premisenumberrangeto_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseNumberRangeTo)


def test_xal::premisenumberrangeto_constructor_exists():
    assert callable(xal::PremiseNumberRangeTo.__init__)


def test_xal::premisenumberrangeto_constructor_args():
    sig = inspect.signature(xal::PremiseNumberRangeTo.__init__)
    params = list(sig.parameters.keys())



def test_xal::premisenumberrangefrom_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseNumberRangeFrom)


def test_xal::premisenumberrangefrom_constructor_exists():
    assert callable(xal::PremiseNumberRangeFrom.__init__)


def test_xal::premisenumberrangefrom_constructor_args():
    sig = inspect.signature(xal::PremiseNumberRangeFrom.__init__)
    params = list(sig.parameters.keys())



def test_xal::subpremise_is_not_abstract():
    assert not inspect.isabstract(xal::SubPremise)


def test_xal::subpremise_constructor_exists():
    assert callable(xal::SubPremise.__init__)


def test_xal::subpremise_constructor_args():
    sig = inspect.signature(xal::SubPremise.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal::subpremise_has_type():
    assert hasattr(xal::SubPremise, "type")
    descriptor = None
    for klass in xal::SubPremise.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremise_has_anyAttribute():
    assert hasattr(xal::SubPremise, "anyAttribute")
    descriptor = None
    for klass in xal::SubPremise.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subpremise_has_any():
    assert hasattr(xal::SubPremise, "any")
    descriptor = None
    for klass in xal::SubPremise.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal::premisename_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseName)


def test_xal::premisename_constructor_exists():
    assert callable(xal::PremiseName.__init__)


def test_xal::premisename_constructor_args():
    sig = inspect.signature(xal::PremiseName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::premisename_has_mixed():
    assert hasattr(xal::PremiseName, "mixed")
    descriptor = None
    for klass in xal::PremiseName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisename_has_typeOccurrence():
    assert hasattr(xal::PremiseName, "typeOccurrence")
    descriptor = None
    for klass in xal::PremiseName.__mro__:
        if "typeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["typeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisename_has_type():
    assert hasattr(xal::PremiseName, "type")
    descriptor = None
    for klass in xal::PremiseName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisename_has_anyAttribute():
    assert hasattr(xal::PremiseName, "anyAttribute")
    descriptor = None
    for klass in xal::PremiseName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisename_has_code():
    assert hasattr(xal::PremiseName, "code")
    descriptor = None
    for klass in xal::PremiseName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::premisenumberrange_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseNumberRange)


def test_xal::premisenumberrange_constructor_exists():
    assert callable(xal::PremiseNumberRange.__init__)


def test_xal::premisenumberrange_constructor_args():
    sig = inspect.signature(xal::PremiseNumberRange.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "indicatorOccurence" in params, "Missing parameter 'indicatorOccurence'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "rangeType" in params, "Missing parameter 'rangeType'"
    assert "numberRangeOccurence" in params, "Missing parameter 'numberRangeOccurence'"

def test_xal::premisenumberrange_has_indicator():
    assert hasattr(xal::PremiseNumberRange, "indicator")
    descriptor = None
    for klass in xal::PremiseNumberRange.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberrange_has_type():
    assert hasattr(xal::PremiseNumberRange, "type")
    descriptor = None
    for klass in xal::PremiseNumberRange.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberrange_has_indicatorOccurence():
    assert hasattr(xal::PremiseNumberRange, "indicatorOccurence")
    descriptor = None
    for klass in xal::PremiseNumberRange.__mro__:
        if "indicatorOccurence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurence"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberrange_has_separator():
    assert hasattr(xal::PremiseNumberRange, "separator")
    descriptor = None
    for klass in xal::PremiseNumberRange.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberrange_has_rangeType():
    assert hasattr(xal::PremiseNumberRange, "rangeType")
    descriptor = None
    for klass in xal::PremiseNumberRange.__mro__:
        if "rangeType" in klass.__dict__:
            descriptor = klass.__dict__["rangeType"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberrange_has_numberRangeOccurence():
    assert hasattr(xal::PremiseNumberRange, "numberRangeOccurence")
    descriptor = None
    for klass in xal::PremiseNumberRange.__mro__:
        if "numberRangeOccurence" in klass.__dict__:
            descriptor = klass.__dict__["numberRangeOccurence"]
            break
    assert isinstance(descriptor, property)



def test_xal::premiselocation_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseLocation)


def test_xal::premiselocation_constructor_exists():
    assert callable(xal::PremiseLocation.__init__)


def test_xal::premiselocation_constructor_args():
    sig = inspect.signature(xal::PremiseLocation.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::premiselocation_has_anyAttribute():
    assert hasattr(xal::PremiseLocation, "anyAttribute")
    descriptor = None
    for klass in xal::PremiseLocation.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::premiselocation_has_code():
    assert hasattr(xal::PremiseLocation, "code")
    descriptor = None
    for klass in xal::PremiseLocation.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::premiselocation_has_mixed():
    assert hasattr(xal::PremiseLocation, "mixed")
    descriptor = None
    for klass in xal::PremiseLocation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::posttownsuffix_is_not_abstract():
    assert not inspect.isabstract(xal::PostTownSuffix)


def test_xal::posttownsuffix_constructor_exists():
    assert callable(xal::PostTownSuffix.__init__)


def test_xal::posttownsuffix_constructor_args():
    sig = inspect.signature(xal::PostTownSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::posttownsuffix_has_anyAttribute():
    assert hasattr(xal::PostTownSuffix, "anyAttribute")
    descriptor = None
    for klass in xal::PostTownSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::posttownsuffix_has_code():
    assert hasattr(xal::PostTownSuffix, "code")
    descriptor = None
    for klass in xal::PostTownSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::posttownsuffix_has_mixed():
    assert hasattr(xal::PostTownSuffix, "mixed")
    descriptor = None
    for klass in xal::PostTownSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::posttownname_is_not_abstract():
    assert not inspect.isabstract(xal::PostTownName)


def test_xal::posttownname_constructor_exists():
    assert callable(xal::PostTownName.__init__)


def test_xal::posttownname_constructor_args():
    sig = inspect.signature(xal::PostTownName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::posttownname_has_code():
    assert hasattr(xal::PostTownName, "code")
    descriptor = None
    for klass in xal::PostTownName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::posttownname_has_mixed():
    assert hasattr(xal::PostTownName, "mixed")
    descriptor = None
    for klass in xal::PostTownName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::posttownname_has_anyAttribute():
    assert hasattr(xal::PostTownName, "anyAttribute")
    descriptor = None
    for klass in xal::PostTownName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::posttownname_has_type():
    assert hasattr(xal::PostTownName, "type")
    descriptor = None
    for klass in xal::PostTownName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::postofficenumber_is_not_abstract():
    assert not inspect.isabstract(xal::PostOfficeNumber)


def test_xal::postofficenumber_constructor_exists():
    assert callable(xal::PostOfficeNumber.__init__)


def test_xal::postofficenumber_constructor_args():
    sig = inspect.signature(xal::PostOfficeNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "code" in params, "Missing parameter 'code'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postofficenumber_has_mixed():
    assert hasattr(xal::PostOfficeNumber, "mixed")
    descriptor = None
    for klass in xal::PostOfficeNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficenumber_has_indicatorOccurrence():
    assert hasattr(xal::PostOfficeNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal::PostOfficeNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficenumber_has_code():
    assert hasattr(xal::PostOfficeNumber, "code")
    descriptor = None
    for klass in xal::PostOfficeNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficenumber_has_indicator():
    assert hasattr(xal::PostOfficeNumber, "indicator")
    descriptor = None
    for klass in xal::PostOfficeNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficenumber_has_anyAttribute():
    assert hasattr(xal::PostOfficeNumber, "anyAttribute")
    descriptor = None
    for klass in xal::PostOfficeNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::postofficename_is_not_abstract():
    assert not inspect.isabstract(xal::PostOfficeName)


def test_xal::postofficename_constructor_exists():
    assert callable(xal::PostOfficeName.__init__)


def test_xal::postofficename_constructor_args():
    sig = inspect.signature(xal::PostOfficeName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postofficename_has_code():
    assert hasattr(xal::PostOfficeName, "code")
    descriptor = None
    for klass in xal::PostOfficeName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficename_has_mixed():
    assert hasattr(xal::PostOfficeName, "mixed")
    descriptor = None
    for klass in xal::PostOfficeName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficename_has_type():
    assert hasattr(xal::PostOfficeName, "type")
    descriptor = None
    for klass in xal::PostOfficeName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::postofficename_has_anyAttribute():
    assert hasattr(xal::PostOfficeName, "anyAttribute")
    descriptor = None
    for klass in xal::PostOfficeName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::postboxnumberextension_is_not_abstract():
    assert not inspect.isabstract(xal::PostBoxNumberExtension)


def test_xal::postboxnumberextension_constructor_exists():
    assert callable(xal::PostBoxNumberExtension.__init__)


def test_xal::postboxnumberextension_constructor_args():
    sig = inspect.signature(xal::PostBoxNumberExtension.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberExtensionSeparator" in params, "Missing parameter 'numberExtensionSeparator'"

def test_xal::postboxnumberextension_has_mixed():
    assert hasattr(xal::PostBoxNumberExtension, "mixed")
    descriptor = None
    for klass in xal::PostBoxNumberExtension.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumberextension_has_anyAttribute():
    assert hasattr(xal::PostBoxNumberExtension, "anyAttribute")
    descriptor = None
    for klass in xal::PostBoxNumberExtension.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumberextension_has_numberExtensionSeparator():
    assert hasattr(xal::PostBoxNumberExtension, "numberExtensionSeparator")
    descriptor = None
    for klass in xal::PostBoxNumberExtension.__mro__:
        if "numberExtensionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberExtensionSeparator"]
            break
    assert isinstance(descriptor, property)



def test_xal::postboxnumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal::PostBoxNumberSuffix)


def test_xal::postboxnumbersuffix_constructor_exists():
    assert callable(xal::PostBoxNumberSuffix.__init__)


def test_xal::postboxnumbersuffix_constructor_args():
    sig = inspect.signature(xal::PostBoxNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postboxnumbersuffix_has_mixed():
    assert hasattr(xal::PostBoxNumberSuffix, "mixed")
    descriptor = None
    for klass in xal::PostBoxNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumbersuffix_has_code():
    assert hasattr(xal::PostBoxNumberSuffix, "code")
    descriptor = None
    for klass in xal::PostBoxNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal::PostBoxNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal::PostBoxNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumbersuffix_has_anyAttribute():
    assert hasattr(xal::PostBoxNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal::PostBoxNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::postboxnumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal::PostBoxNumberPrefix)


def test_xal::postboxnumberprefix_constructor_exists():
    assert callable(xal::PostBoxNumberPrefix.__init__)


def test_xal::postboxnumberprefix_constructor_args():
    sig = inspect.signature(xal::PostBoxNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postboxnumberprefix_has_code():
    assert hasattr(xal::PostBoxNumberPrefix, "code")
    descriptor = None
    for klass in xal::PostBoxNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumberprefix_has_mixed():
    assert hasattr(xal::PostBoxNumberPrefix, "mixed")
    descriptor = None
    for klass in xal::PostBoxNumberPrefix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal::PostBoxNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal::PostBoxNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumberprefix_has_anyAttribute():
    assert hasattr(xal::PostBoxNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal::PostBoxNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::supplementarypostalservicedata_is_not_abstract():
    assert not inspect.isabstract(xal::SupplementaryPostalServiceData)


def test_xal::supplementarypostalservicedata_constructor_exists():
    assert callable(xal::SupplementaryPostalServiceData.__init__)


def test_xal::supplementarypostalservicedata_constructor_args():
    sig = inspect.signature(xal::SupplementaryPostalServiceData.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::supplementarypostalservicedata_has_mixed():
    assert hasattr(xal::SupplementaryPostalServiceData, "mixed")
    descriptor = None
    for klass in xal::SupplementaryPostalServiceData.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::supplementarypostalservicedata_has_anyAttribute():
    assert hasattr(xal::SupplementaryPostalServiceData, "anyAttribute")
    descriptor = None
    for klass in xal::SupplementaryPostalServiceData.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::supplementarypostalservicedata_has_type():
    assert hasattr(xal::SupplementaryPostalServiceData, "type")
    descriptor = None
    for klass in xal::SupplementaryPostalServiceData.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::supplementarypostalservicedata_has_code():
    assert hasattr(xal::SupplementaryPostalServiceData, "code")
    descriptor = None
    for klass in xal::SupplementaryPostalServiceData.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::postboxnumber_is_not_abstract():
    assert not inspect.isabstract(xal::PostBoxNumber)


def test_xal::postboxnumber_constructor_exists():
    assert callable(xal::PostBoxNumber.__init__)


def test_xal::postboxnumber_constructor_args():
    sig = inspect.signature(xal::PostBoxNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postboxnumber_has_code():
    assert hasattr(xal::PostBoxNumber, "code")
    descriptor = None
    for klass in xal::PostBoxNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumber_has_mixed():
    assert hasattr(xal::PostBoxNumber, "mixed")
    descriptor = None
    for klass in xal::PostBoxNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postboxnumber_has_anyAttribute():
    assert hasattr(xal::PostBoxNumber, "anyAttribute")
    descriptor = None
    for klass in xal::PostBoxNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::sortingcode_is_not_abstract():
    assert not inspect.isabstract(xal::SortingCode)


def test_xal::sortingcode_constructor_exists():
    assert callable(xal::SortingCode.__init__)


def test_xal::sortingcode_constructor_args():
    sig = inspect.signature(xal::SortingCode.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::sortingcode_has_code():
    assert hasattr(xal::SortingCode, "code")
    descriptor = None
    for klass in xal::SortingCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::sortingcode_has_type():
    assert hasattr(xal::SortingCode, "type")
    descriptor = None
    for klass in xal::SortingCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalroutenumber_is_not_abstract():
    assert not inspect.isabstract(xal::PostalRouteNumber)


def test_xal::postalroutenumber_constructor_exists():
    assert callable(xal::PostalRouteNumber.__init__)


def test_xal::postalroutenumber_constructor_args():
    sig = inspect.signature(xal::PostalRouteNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::postalroutenumber_has_code():
    assert hasattr(xal::PostalRouteNumber, "code")
    descriptor = None
    for klass in xal::PostalRouteNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroutenumber_has_anyAttribute():
    assert hasattr(xal::PostalRouteNumber, "anyAttribute")
    descriptor = None
    for klass in xal::PostalRouteNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroutenumber_has_mixed():
    assert hasattr(xal::PostalRouteNumber, "mixed")
    descriptor = None
    for klass in xal::PostalRouteNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalroutename_is_not_abstract():
    assert not inspect.isabstract(xal::PostalRouteName)


def test_xal::postalroutename_constructor_exists():
    assert callable(xal::PostalRouteName.__init__)


def test_xal::postalroutename_constructor_args():
    sig = inspect.signature(xal::PostalRouteName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::postalroutename_has_anyAttribute():
    assert hasattr(xal::PostalRouteName, "anyAttribute")
    descriptor = None
    for klass in xal::PostalRouteName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroutename_has_code():
    assert hasattr(xal::PostalRouteName, "code")
    descriptor = None
    for klass in xal::PostalRouteName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroutename_has_mixed():
    assert hasattr(xal::PostalRouteName, "mixed")
    descriptor = None
    for klass in xal::PostalRouteName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroutename_has_type():
    assert hasattr(xal::PostalRouteName, "type")
    descriptor = None
    for klass in xal::PostalRouteName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalcodenumberextension_is_not_abstract():
    assert not inspect.isabstract(xal::PostalCodeNumberExtension)


def test_xal::postalcodenumberextension_constructor_exists():
    assert callable(xal::PostalCodeNumberExtension.__init__)


def test_xal::postalcodenumberextension_constructor_args():
    sig = inspect.signature(xal::PostalCodeNumberExtension.__init__)
    params = list(sig.parameters.keys())
    assert "numberExtensionSeparator" in params, "Missing parameter 'numberExtensionSeparator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::postalcodenumberextension_has_numberExtensionSeparator():
    assert hasattr(xal::PostalCodeNumberExtension, "numberExtensionSeparator")
    descriptor = None
    for klass in xal::PostalCodeNumberExtension.__mro__:
        if "numberExtensionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberExtensionSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumberextension_has_type():
    assert hasattr(xal::PostalCodeNumberExtension, "type")
    descriptor = None
    for klass in xal::PostalCodeNumberExtension.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumberextension_has_anyAttribute():
    assert hasattr(xal::PostalCodeNumberExtension, "anyAttribute")
    descriptor = None
    for klass in xal::PostalCodeNumberExtension.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumberextension_has_mixed():
    assert hasattr(xal::PostalCodeNumberExtension, "mixed")
    descriptor = None
    for klass in xal::PostalCodeNumberExtension.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumberextension_has_code():
    assert hasattr(xal::PostalCodeNumberExtension, "code")
    descriptor = None
    for klass in xal::PostalCodeNumberExtension.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalcodenumber_is_not_abstract():
    assert not inspect.isabstract(xal::PostalCodeNumber)


def test_xal::postalcodenumber_constructor_exists():
    assert callable(xal::PostalCodeNumber.__init__)


def test_xal::postalcodenumber_constructor_args():
    sig = inspect.signature(xal::PostalCodeNumber.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::postalcodenumber_has_type():
    assert hasattr(xal::PostalCodeNumber, "type")
    descriptor = None
    for klass in xal::PostalCodeNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumber_has_anyAttribute():
    assert hasattr(xal::PostalCodeNumber, "anyAttribute")
    descriptor = None
    for klass in xal::PostalCodeNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumber_has_code():
    assert hasattr(xal::PostalCodeNumber, "code")
    descriptor = None
    for klass in xal::PostalCodeNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcodenumber_has_mixed():
    assert hasattr(xal::PostalCodeNumber, "mixed")
    descriptor = None
    for klass in xal::PostalCodeNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::posttown_is_not_abstract():
    assert not inspect.isabstract(xal::PostTown)


def test_xal::posttown_constructor_exists():
    assert callable(xal::PostTown.__init__)


def test_xal::posttown_constructor_args():
    sig = inspect.signature(xal::PostTown.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::posttown_has_anyAttribute():
    assert hasattr(xal::PostTown, "anyAttribute")
    descriptor = None
    for klass in xal::PostTown.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::posttown_has_type():
    assert hasattr(xal::PostTown, "type")
    descriptor = None
    for klass in xal::PostTown.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::mailstopnumber_is_not_abstract():
    assert not inspect.isabstract(xal::MailStopNumber)


def test_xal::mailstopnumber_constructor_exists():
    assert callable(xal::MailStopNumber.__init__)


def test_xal::mailstopnumber_constructor_args():
    sig = inspect.signature(xal::MailStopNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "nameNumberSeparator" in params, "Missing parameter 'nameNumberSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::mailstopnumber_has_code():
    assert hasattr(xal::MailStopNumber, "code")
    descriptor = None
    for klass in xal::MailStopNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstopnumber_has_anyAttribute():
    assert hasattr(xal::MailStopNumber, "anyAttribute")
    descriptor = None
    for klass in xal::MailStopNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstopnumber_has_nameNumberSeparator():
    assert hasattr(xal::MailStopNumber, "nameNumberSeparator")
    descriptor = None
    for klass in xal::MailStopNumber.__mro__:
        if "nameNumberSeparator" in klass.__dict__:
            descriptor = klass.__dict__["nameNumberSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstopnumber_has_mixed():
    assert hasattr(xal::MailStopNumber, "mixed")
    descriptor = None
    for klass in xal::MailStopNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::mailstopname_is_not_abstract():
    assert not inspect.isabstract(xal::MailStopName)


def test_xal::mailstopname_constructor_exists():
    assert callable(xal::MailStopName.__init__)


def test_xal::mailstopname_constructor_args():
    sig = inspect.signature(xal::MailStopName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::mailstopname_has_code():
    assert hasattr(xal::MailStopName, "code")
    descriptor = None
    for klass in xal::MailStopName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstopname_has_type():
    assert hasattr(xal::MailStopName, "type")
    descriptor = None
    for klass in xal::MailStopName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstopname_has_anyAttribute():
    assert hasattr(xal::MailStopName, "anyAttribute")
    descriptor = None
    for klass in xal::MailStopName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstopname_has_mixed():
    assert hasattr(xal::MailStopName, "mixed")
    descriptor = None
    for klass in xal::MailStopName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::localityname_is_not_abstract():
    assert not inspect.isabstract(xal::LocalityName)


def test_xal::localityname_constructor_exists():
    assert callable(xal::LocalityName.__init__)


def test_xal::localityname_constructor_args():
    sig = inspect.signature(xal::LocalityName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::localityname_has_anyAttribute():
    assert hasattr(xal::LocalityName, "anyAttribute")
    descriptor = None
    for klass in xal::LocalityName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::localityname_has_mixed():
    assert hasattr(xal::LocalityName, "mixed")
    descriptor = None
    for klass in xal::LocalityName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::localityname_has_type():
    assert hasattr(xal::LocalityName, "type")
    descriptor = None
    for klass in xal::LocalityName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::localityname_has_code():
    assert hasattr(xal::LocalityName, "code")
    descriptor = None
    for klass in xal::LocalityName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::largemailuseridentifier_is_not_abstract():
    assert not inspect.isabstract(xal::LargeMailUserIdentifier)


def test_xal::largemailuseridentifier_constructor_exists():
    assert callable(xal::LargeMailUserIdentifier.__init__)


def test_xal::largemailuseridentifier_constructor_args():
    sig = inspect.signature(xal::LargeMailUserIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "indicator" in params, "Missing parameter 'indicator'"

def test_xal::largemailuseridentifier_has_anyAttribute():
    assert hasattr(xal::LargeMailUserIdentifier, "anyAttribute")
    descriptor = None
    for klass in xal::LargeMailUserIdentifier.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailuseridentifier_has_code():
    assert hasattr(xal::LargeMailUserIdentifier, "code")
    descriptor = None
    for klass in xal::LargeMailUserIdentifier.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailuseridentifier_has_mixed():
    assert hasattr(xal::LargeMailUserIdentifier, "mixed")
    descriptor = None
    for klass in xal::LargeMailUserIdentifier.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailuseridentifier_has_type():
    assert hasattr(xal::LargeMailUserIdentifier, "type")
    descriptor = None
    for klass in xal::LargeMailUserIdentifier.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailuseridentifier_has_indicator():
    assert hasattr(xal::LargeMailUserIdentifier, "indicator")
    descriptor = None
    for klass in xal::LargeMailUserIdentifier.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)



def test_xal::largemailusername_is_not_abstract():
    assert not inspect.isabstract(xal::LargeMailUserName)


def test_xal::largemailusername_constructor_exists():
    assert callable(xal::LargeMailUserName.__init__)


def test_xal::largemailusername_constructor_args():
    sig = inspect.signature(xal::LargeMailUserName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::largemailusername_has_mixed():
    assert hasattr(xal::LargeMailUserName, "mixed")
    descriptor = None
    for klass in xal::LargeMailUserName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailusername_has_type():
    assert hasattr(xal::LargeMailUserName, "type")
    descriptor = None
    for klass in xal::LargeMailUserName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailusername_has_anyAttribute():
    assert hasattr(xal::LargeMailUserName, "anyAttribute")
    descriptor = None
    for klass in xal::LargeMailUserName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailusername_has_code():
    assert hasattr(xal::LargeMailUserName, "code")
    descriptor = None
    for klass in xal::LargeMailUserName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::keylinecode_is_not_abstract():
    assert not inspect.isabstract(xal::KeyLineCode)


def test_xal::keylinecode_constructor_exists():
    assert callable(xal::KeyLineCode.__init__)


def test_xal::keylinecode_constructor_args():
    sig = inspect.signature(xal::KeyLineCode.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::keylinecode_has_code():
    assert hasattr(xal::KeyLineCode, "code")
    descriptor = None
    for klass in xal::KeyLineCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::keylinecode_has_mixed():
    assert hasattr(xal::KeyLineCode, "mixed")
    descriptor = None
    for klass in xal::KeyLineCode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::keylinecode_has_type():
    assert hasattr(xal::KeyLineCode, "type")
    descriptor = None
    for klass in xal::KeyLineCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::keylinecode_has_anyAttribute():
    assert hasattr(xal::KeyLineCode, "anyAttribute")
    descriptor = None
    for klass in xal::KeyLineCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::endorsementlinecode_is_not_abstract():
    assert not inspect.isabstract(xal::EndorsementLineCode)


def test_xal::endorsementlinecode_constructor_exists():
    assert callable(xal::EndorsementLineCode.__init__)


def test_xal::endorsementlinecode_constructor_args():
    sig = inspect.signature(xal::EndorsementLineCode.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::endorsementlinecode_has_mixed():
    assert hasattr(xal::EndorsementLineCode, "mixed")
    descriptor = None
    for klass in xal::EndorsementLineCode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::endorsementlinecode_has_anyAttribute():
    assert hasattr(xal::EndorsementLineCode, "anyAttribute")
    descriptor = None
    for klass in xal::EndorsementLineCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::endorsementlinecode_has_code():
    assert hasattr(xal::EndorsementLineCode, "code")
    descriptor = None
    for klass in xal::EndorsementLineCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::endorsementlinecode_has_type():
    assert hasattr(xal::EndorsementLineCode, "type")
    descriptor = None
    for klass in xal::EndorsementLineCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::xal_is_not_abstract():
    assert not inspect.isabstract(xal::Xal)


def test_xal::xal_constructor_exists():
    assert callable(xal::Xal.__init__)


def test_xal::xal_constructor_args():
    sig = inspect.signature(xal::Xal.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "version" in params, "Missing parameter 'version'"

def test_xal::xal_has_any():
    assert hasattr(xal::Xal, "any")
    descriptor = None
    for klass in xal::Xal.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::xal_has_anyAttribute():
    assert hasattr(xal::Xal, "anyAttribute")
    descriptor = None
    for klass in xal::Xal.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::xal_has_version():
    assert hasattr(xal::Xal, "version")
    descriptor = None
    for klass in xal::Xal.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_xal::firmname_is_not_abstract():
    assert not inspect.isabstract(xal::FirmName)


def test_xal::firmname_constructor_exists():
    assert callable(xal::FirmName.__init__)


def test_xal::firmname_constructor_args():
    sig = inspect.signature(xal::FirmName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::firmname_has_code():
    assert hasattr(xal::FirmName, "code")
    descriptor = None
    for klass in xal::FirmName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::firmname_has_type():
    assert hasattr(xal::FirmName, "type")
    descriptor = None
    for klass in xal::FirmName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::firmname_has_mixed():
    assert hasattr(xal::FirmName, "mixed")
    descriptor = None
    for klass in xal::FirmName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::firmname_has_anyAttribute():
    assert hasattr(xal::FirmName, "anyAttribute")
    descriptor = None
    for klass in xal::FirmName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::firm_is_not_abstract():
    assert not inspect.isabstract(xal::Firm)


def test_xal::firm_constructor_exists():
    assert callable(xal::Firm.__init__)


def test_xal::firm_constructor_args():
    sig = inspect.signature(xal::Firm.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal::firm_has_anyAttribute():
    assert hasattr(xal::Firm, "anyAttribute")
    descriptor = None
    for klass in xal::Firm.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::firm_has_type():
    assert hasattr(xal::Firm, "type")
    descriptor = None
    for klass in xal::Firm.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::firm_has_any():
    assert hasattr(xal::Firm, "any")
    descriptor = None
    for klass in xal::Firm.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal::premisenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseNumberSuffix)


def test_xal::premisenumbersuffix_constructor_exists():
    assert callable(xal::PremiseNumberSuffix.__init__)


def test_xal::premisenumbersuffix_constructor_args():
    sig = inspect.signature(xal::PremiseNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::premisenumbersuffix_has_anyAttribute():
    assert hasattr(xal::PremiseNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal::PremiseNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumbersuffix_has_mixed():
    assert hasattr(xal::PremiseNumberSuffix, "mixed")
    descriptor = None
    for klass in xal::PremiseNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal::PremiseNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal::PremiseNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumbersuffix_has_type():
    assert hasattr(xal::PremiseNumberSuffix, "type")
    descriptor = None
    for klass in xal::PremiseNumberSuffix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumbersuffix_has_code():
    assert hasattr(xal::PremiseNumberSuffix, "code")
    descriptor = None
    for klass in xal::PremiseNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::premisenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseNumberPrefix)


def test_xal::premisenumberprefix_constructor_exists():
    assert callable(xal::PremiseNumberPrefix.__init__)


def test_xal::premisenumberprefix_constructor_args():
    sig = inspect.signature(xal::PremiseNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "value" in params, "Missing parameter 'value'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::premisenumberprefix_has_anyAttribute():
    assert hasattr(xal::PremiseNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal::PremiseNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberprefix_has_value():
    assert hasattr(xal::PremiseNumberPrefix, "value")
    descriptor = None
    for klass in xal::PremiseNumberPrefix.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal::PremiseNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal::PremiseNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberprefix_has_type():
    assert hasattr(xal::PremiseNumberPrefix, "type")
    descriptor = None
    for klass in xal::PremiseNumberPrefix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumberprefix_has_code():
    assert hasattr(xal::PremiseNumberPrefix, "code")
    descriptor = None
    for klass in xal::PremiseNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::premisenumber_is_not_abstract():
    assert not inspect.isabstract(xal::PremiseNumber)


def test_xal::premisenumber_constructor_exists():
    assert callable(xal::PremiseNumber.__init__)


def test_xal::premisenumber_constructor_args():
    sig = inspect.signature(xal::PremiseNumber.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberTypeOccurrence" in params, "Missing parameter 'numberTypeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "numberType" in params, "Missing parameter 'numberType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"

def test_xal::premisenumber_has_indicator():
    assert hasattr(xal::PremiseNumber, "indicator")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_code():
    assert hasattr(xal::PremiseNumber, "code")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_numberTypeOccurrence():
    assert hasattr(xal::PremiseNumber, "numberTypeOccurrence")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "numberTypeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberTypeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_mixed():
    assert hasattr(xal::PremiseNumber, "mixed")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_numberType():
    assert hasattr(xal::PremiseNumber, "numberType")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "numberType" in klass.__dict__:
            descriptor = klass.__dict__["numberType"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_type():
    assert hasattr(xal::PremiseNumber, "type")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_anyAttribute():
    assert hasattr(xal::PremiseNumber, "anyAttribute")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::premisenumber_has_indicatorOccurrence():
    assert hasattr(xal::PremiseNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal::PremiseNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareNumberSuffix)


def test_xal::thoroughfarenumbersuffix_constructor_exists():
    assert callable(xal::ThoroughfareNumberSuffix.__init__)


def test_xal::thoroughfarenumbersuffix_constructor_args():
    sig = inspect.signature(xal::ThoroughfareNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"

def test_xal::thoroughfarenumbersuffix_has_anyAttribute():
    assert hasattr(xal::ThoroughfareNumberSuffix, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareNumberSuffix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumbersuffix_has_code():
    assert hasattr(xal::ThoroughfareNumberSuffix, "code")
    descriptor = None
    for klass in xal::ThoroughfareNumberSuffix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumbersuffix_has_type():
    assert hasattr(xal::ThoroughfareNumberSuffix, "type")
    descriptor = None
    for klass in xal::ThoroughfareNumberSuffix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumbersuffix_has_mixed():
    assert hasattr(xal::ThoroughfareNumberSuffix, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareNumberSuffix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumbersuffix_has_numberSuffixSeparator():
    assert hasattr(xal::ThoroughfareNumberSuffix, "numberSuffixSeparator")
    descriptor = None
    for klass in xal::ThoroughfareNumberSuffix.__mro__:
        if "numberSuffixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberSuffixSeparator"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareNumberPrefix)


def test_xal::thoroughfarenumberprefix_constructor_exists():
    assert callable(xal::ThoroughfareNumberPrefix.__init__)


def test_xal::thoroughfarenumberprefix_constructor_args():
    sig = inspect.signature(xal::ThoroughfareNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::thoroughfarenumberprefix_has_numberPrefixSeparator():
    assert hasattr(xal::ThoroughfareNumberPrefix, "numberPrefixSeparator")
    descriptor = None
    for klass in xal::ThoroughfareNumberPrefix.__mro__:
        if "numberPrefixSeparator" in klass.__dict__:
            descriptor = klass.__dict__["numberPrefixSeparator"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberprefix_has_mixed():
    assert hasattr(xal::ThoroughfareNumberPrefix, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareNumberPrefix.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberprefix_has_type():
    assert hasattr(xal::ThoroughfareNumberPrefix, "type")
    descriptor = None
    for klass in xal::ThoroughfareNumberPrefix.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberprefix_has_anyAttribute():
    assert hasattr(xal::ThoroughfareNumberPrefix, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareNumberPrefix.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumberprefix_has_code():
    assert hasattr(xal::ThoroughfareNumberPrefix, "code")
    descriptor = None
    for klass in xal::ThoroughfareNumberPrefix.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarenumber_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareNumber)


def test_xal::thoroughfarenumber_constructor_exists():
    assert callable(xal::ThoroughfareNumber.__init__)


def test_xal::thoroughfarenumber_constructor_args():
    sig = inspect.signature(xal::ThoroughfareNumber.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "numberOccurrence" in params, "Missing parameter 'numberOccurrence'"
    assert "numberType" in params, "Missing parameter 'numberType'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::thoroughfarenumber_has_anyAttribute():
    assert hasattr(xal::ThoroughfareNumber, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_indicator():
    assert hasattr(xal::ThoroughfareNumber, "indicator")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_numberOccurrence():
    assert hasattr(xal::ThoroughfareNumber, "numberOccurrence")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "numberOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["numberOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_numberType():
    assert hasattr(xal::ThoroughfareNumber, "numberType")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "numberType" in klass.__dict__:
            descriptor = klass.__dict__["numberType"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_code():
    assert hasattr(xal::ThoroughfareNumber, "code")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_mixed():
    assert hasattr(xal::ThoroughfareNumber, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_indicatorOccurrence():
    assert hasattr(xal::ThoroughfareNumber, "indicatorOccurrence")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "indicatorOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["indicatorOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarenumber_has_type():
    assert hasattr(xal::ThoroughfareNumber, "type")
    descriptor = None
    for klass in xal::ThoroughfareNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::documentroot_is_not_abstract():
    assert not inspect.isabstract(xal::DocumentRoot)


def test_xal::documentroot_constructor_exists():
    assert callable(xal::DocumentRoot.__init__)


def test_xal::documentroot_constructor_args():
    sig = inspect.signature(xal::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::documentroot_has_mixed():
    assert hasattr(xal::DocumentRoot, "mixed")
    descriptor = None
    for klass in xal::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xal::EStringToStringMapEntry)


def test_xal::estringtostringmapentry_constructor_exists():
    assert callable(xal::EStringToStringMapEntry.__init__)


def test_xal::estringtostringmapentry_constructor_args():
    sig = inspect.signature(xal::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xal::thoroughfarepredirection_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfarePreDirection)


def test_xal::thoroughfarepredirection_constructor_exists():
    assert callable(xal::ThoroughfarePreDirection.__init__)


def test_xal::thoroughfarepredirection_constructor_args():
    sig = inspect.signature(xal::ThoroughfarePreDirection.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::thoroughfarepredirection_has_anyAttribute():
    assert hasattr(xal::ThoroughfarePreDirection, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfarePreDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarepredirection_has_code():
    assert hasattr(xal::ThoroughfarePreDirection, "code")
    descriptor = None
    for klass in xal::ThoroughfarePreDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarepredirection_has_type():
    assert hasattr(xal::ThoroughfarePreDirection, "type")
    descriptor = None
    for klass in xal::ThoroughfarePreDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarepredirection_has_mixed():
    assert hasattr(xal::ThoroughfarePreDirection, "mixed")
    descriptor = None
    for klass in xal::ThoroughfarePreDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::dependentthoroughfare_is_not_abstract():
    assert not inspect.isabstract(xal::DependentThoroughfare)


def test_xal::dependentthoroughfare_constructor_exists():
    assert callable(xal::DependentThoroughfare.__init__)


def test_xal::dependentthoroughfare_constructor_args():
    sig = inspect.signature(xal::DependentThoroughfare.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::dependentthoroughfare_has_any():
    assert hasattr(xal::DependentThoroughfare, "any")
    descriptor = None
    for klass in xal::DependentThoroughfare.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentthoroughfare_has_anyAttribute():
    assert hasattr(xal::DependentThoroughfare, "anyAttribute")
    descriptor = None
    for klass in xal::DependentThoroughfare.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentthoroughfare_has_type():
    assert hasattr(xal::DependentThoroughfare, "type")
    descriptor = None
    for klass in xal::DependentThoroughfare.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarepostdirection_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfarePostDirection)


def test_xal::thoroughfarepostdirection_constructor_exists():
    assert callable(xal::ThoroughfarePostDirection.__init__)


def test_xal::thoroughfarepostdirection_constructor_args():
    sig = inspect.signature(xal::ThoroughfarePostDirection.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::thoroughfarepostdirection_has_mixed():
    assert hasattr(xal::ThoroughfarePostDirection, "mixed")
    descriptor = None
    for klass in xal::ThoroughfarePostDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarepostdirection_has_type():
    assert hasattr(xal::ThoroughfarePostDirection, "type")
    descriptor = None
    for klass in xal::ThoroughfarePostDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarepostdirection_has_anyAttribute():
    assert hasattr(xal::ThoroughfarePostDirection, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfarePostDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarepostdirection_has_code():
    assert hasattr(xal::ThoroughfarePostDirection, "code")
    descriptor = None
    for klass in xal::ThoroughfarePostDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfaretrailingtype_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareTrailingType)


def test_xal::thoroughfaretrailingtype_constructor_exists():
    assert callable(xal::ThoroughfareTrailingType.__init__)


def test_xal::thoroughfaretrailingtype_constructor_args():
    sig = inspect.signature(xal::ThoroughfareTrailingType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::thoroughfaretrailingtype_has_mixed():
    assert hasattr(xal::ThoroughfareTrailingType, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareTrailingType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfaretrailingtype_has_anyAttribute():
    assert hasattr(xal::ThoroughfareTrailingType, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareTrailingType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfaretrailingtype_has_code():
    assert hasattr(xal::ThoroughfareTrailingType, "code")
    descriptor = None
    for klass in xal::ThoroughfareTrailingType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfaretrailingtype_has_type():
    assert hasattr(xal::ThoroughfareTrailingType, "type")
    descriptor = None
    for klass in xal::ThoroughfareTrailingType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfarename_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareName)


def test_xal::thoroughfarename_constructor_exists():
    assert callable(xal::ThoroughfareName.__init__)


def test_xal::thoroughfarename_constructor_args():
    sig = inspect.signature(xal::ThoroughfareName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::thoroughfarename_has_type():
    assert hasattr(xal::ThoroughfareName, "type")
    descriptor = None
    for klass in xal::ThoroughfareName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarename_has_anyAttribute():
    assert hasattr(xal::ThoroughfareName, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarename_has_code():
    assert hasattr(xal::ThoroughfareName, "code")
    descriptor = None
    for klass in xal::ThoroughfareName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfarename_has_mixed():
    assert hasattr(xal::ThoroughfareName, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfareleadingtype_is_not_abstract():
    assert not inspect.isabstract(xal::ThoroughfareLeadingType)


def test_xal::thoroughfareleadingtype_constructor_exists():
    assert callable(xal::ThoroughfareLeadingType.__init__)


def test_xal::thoroughfareleadingtype_constructor_args():
    sig = inspect.signature(xal::ThoroughfareLeadingType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::thoroughfareleadingtype_has_code():
    assert hasattr(xal::ThoroughfareLeadingType, "code")
    descriptor = None
    for klass in xal::ThoroughfareLeadingType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfareleadingtype_has_anyAttribute():
    assert hasattr(xal::ThoroughfareLeadingType, "anyAttribute")
    descriptor = None
    for klass in xal::ThoroughfareLeadingType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfareleadingtype_has_mixed():
    assert hasattr(xal::ThoroughfareLeadingType, "mixed")
    descriptor = None
    for klass in xal::ThoroughfareLeadingType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfareleadingtype_has_type():
    assert hasattr(xal::ThoroughfareLeadingType, "type")
    descriptor = None
    for klass in xal::ThoroughfareLeadingType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalroute_is_not_abstract():
    assert not inspect.isabstract(xal::PostalRoute)


def test_xal::postalroute_constructor_exists():
    assert callable(xal::PostalRoute.__init__)


def test_xal::postalroute_constructor_args():
    sig = inspect.signature(xal::PostalRoute.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postalroute_has_any():
    assert hasattr(xal::PostalRoute, "any")
    descriptor = None
    for klass in xal::PostalRoute.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroute_has_type():
    assert hasattr(xal::PostalRoute, "type")
    descriptor = None
    for klass in xal::PostalRoute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalroute_has_anyAttribute():
    assert hasattr(xal::PostalRoute, "anyAttribute")
    descriptor = None
    for klass in xal::PostalRoute.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::largemailuser_is_not_abstract():
    assert not inspect.isabstract(xal::LargeMailUser)


def test_xal::largemailuser_constructor_exists():
    assert callable(xal::LargeMailUser.__init__)


def test_xal::largemailuser_constructor_args():
    sig = inspect.signature(xal::LargeMailUser.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::largemailuser_has_type():
    assert hasattr(xal::LargeMailUser, "type")
    descriptor = None
    for klass in xal::LargeMailUser.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailuser_has_any():
    assert hasattr(xal::LargeMailUser, "any")
    descriptor = None
    for klass in xal::LargeMailUser.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::largemailuser_has_anyAttribute():
    assert hasattr(xal::LargeMailUser, "anyAttribute")
    descriptor = None
    for klass in xal::LargeMailUser.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::premise_is_not_abstract():
    assert not inspect.isabstract(xal::Premise)


def test_xal::premise_constructor_exists():
    assert callable(xal::Premise.__init__)


def test_xal::premise_constructor_args():
    sig = inspect.signature(xal::Premise.__init__)
    params = list(sig.parameters.keys())
    assert "premiseDependencyType" in params, "Missing parameter 'premiseDependencyType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "premiseThoroughfareConnector" in params, "Missing parameter 'premiseThoroughfareConnector'"
    assert "premiseDependency" in params, "Missing parameter 'premiseDependency'"

def test_xal::premise_has_premiseDependencyType():
    assert hasattr(xal::Premise, "premiseDependencyType")
    descriptor = None
    for klass in xal::Premise.__mro__:
        if "premiseDependencyType" in klass.__dict__:
            descriptor = klass.__dict__["premiseDependencyType"]
            break
    assert isinstance(descriptor, property)

def test_xal::premise_has_type():
    assert hasattr(xal::Premise, "type")
    descriptor = None
    for klass in xal::Premise.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::premise_has_any():
    assert hasattr(xal::Premise, "any")
    descriptor = None
    for klass in xal::Premise.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::premise_has_anyAttribute():
    assert hasattr(xal::Premise, "anyAttribute")
    descriptor = None
    for klass in xal::Premise.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::premise_has_premiseThoroughfareConnector():
    assert hasattr(xal::Premise, "premiseThoroughfareConnector")
    descriptor = None
    for klass in xal::Premise.__mro__:
        if "premiseThoroughfareConnector" in klass.__dict__:
            descriptor = klass.__dict__["premiseThoroughfareConnector"]
            break
    assert isinstance(descriptor, property)

def test_xal::premise_has_premiseDependency():
    assert hasattr(xal::Premise, "premiseDependency")
    descriptor = None
    for klass in xal::Premise.__mro__:
        if "premiseDependency" in klass.__dict__:
            descriptor = klass.__dict__["premiseDependency"]
            break
    assert isinstance(descriptor, property)



def test_xal::postbox_is_not_abstract():
    assert not inspect.isabstract(xal::PostBox)


def test_xal::postbox_constructor_exists():
    assert callable(xal::PostBox.__init__)


def test_xal::postbox_constructor_args():
    sig = inspect.signature(xal::PostBox.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::postbox_has_anyAttribute():
    assert hasattr(xal::PostBox, "anyAttribute")
    descriptor = None
    for klass in xal::PostBox.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postbox_has_any():
    assert hasattr(xal::PostBox, "any")
    descriptor = None
    for klass in xal::PostBox.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::postbox_has_indicator():
    assert hasattr(xal::PostBox, "indicator")
    descriptor = None
    for klass in xal::PostBox.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::postbox_has_type():
    assert hasattr(xal::PostBox, "type")
    descriptor = None
    for klass in xal::PostBox.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::dependentlocalitynumber_is_not_abstract():
    assert not inspect.isabstract(xal::DependentLocalityNumber)


def test_xal::dependentlocalitynumber_constructor_exists():
    assert callable(xal::DependentLocalityNumber.__init__)


def test_xal::dependentlocalitynumber_constructor_args():
    sig = inspect.signature(xal::DependentLocalityNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "nameNumberOccurrence" in params, "Missing parameter 'nameNumberOccurrence'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::dependentlocalitynumber_has_mixed():
    assert hasattr(xal::DependentLocalityNumber, "mixed")
    descriptor = None
    for klass in xal::DependentLocalityNumber.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocalitynumber_has_anyAttribute():
    assert hasattr(xal::DependentLocalityNumber, "anyAttribute")
    descriptor = None
    for klass in xal::DependentLocalityNumber.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocalitynumber_has_nameNumberOccurrence():
    assert hasattr(xal::DependentLocalityNumber, "nameNumberOccurrence")
    descriptor = None
    for klass in xal::DependentLocalityNumber.__mro__:
        if "nameNumberOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["nameNumberOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocalitynumber_has_code():
    assert hasattr(xal::DependentLocalityNumber, "code")
    descriptor = None
    for klass in xal::DependentLocalityNumber.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::dependentlocalityname_is_not_abstract():
    assert not inspect.isabstract(xal::DependentLocalityName)


def test_xal::dependentlocalityname_constructor_exists():
    assert callable(xal::DependentLocalityName.__init__)


def test_xal::dependentlocalityname_constructor_args():
    sig = inspect.signature(xal::DependentLocalityName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::dependentlocalityname_has_mixed():
    assert hasattr(xal::DependentLocalityName, "mixed")
    descriptor = None
    for klass in xal::DependentLocalityName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocalityname_has_code():
    assert hasattr(xal::DependentLocalityName, "code")
    descriptor = None
    for klass in xal::DependentLocalityName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocalityname_has_type():
    assert hasattr(xal::DependentLocalityName, "type")
    descriptor = None
    for klass in xal::DependentLocalityName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocalityname_has_anyAttribute():
    assert hasattr(xal::DependentLocalityName, "anyAttribute")
    descriptor = None
    for klass in xal::DependentLocalityName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::dependentlocality_is_not_abstract():
    assert not inspect.isabstract(xal::DependentLocality)


def test_xal::dependentlocality_constructor_exists():
    assert callable(xal::DependentLocality.__init__)


def test_xal::dependentlocality_constructor_args():
    sig = inspect.signature(xal::DependentLocality.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "connector" in params, "Missing parameter 'connector'"

def test_xal::dependentlocality_has_indicator():
    assert hasattr(xal::DependentLocality, "indicator")
    descriptor = None
    for klass in xal::DependentLocality.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocality_has_type():
    assert hasattr(xal::DependentLocality, "type")
    descriptor = None
    for klass in xal::DependentLocality.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocality_has_usageType():
    assert hasattr(xal::DependentLocality, "usageType")
    descriptor = None
    for klass in xal::DependentLocality.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocality_has_any():
    assert hasattr(xal::DependentLocality, "any")
    descriptor = None
    for klass in xal::DependentLocality.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocality_has_anyAttribute():
    assert hasattr(xal::DependentLocality, "anyAttribute")
    descriptor = None
    for klass in xal::DependentLocality.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::dependentlocality_has_connector():
    assert hasattr(xal::DependentLocality, "connector")
    descriptor = None
    for klass in xal::DependentLocality.__mro__:
        if "connector" in klass.__dict__:
            descriptor = klass.__dict__["connector"]
            break
    assert isinstance(descriptor, property)



def test_xal::mailstop_is_not_abstract():
    assert not inspect.isabstract(xal::MailStop)


def test_xal::mailstop_constructor_exists():
    assert callable(xal::MailStop.__init__)


def test_xal::mailstop_constructor_args():
    sig = inspect.signature(xal::MailStop.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal::mailstop_has_anyAttribute():
    assert hasattr(xal::MailStop, "anyAttribute")
    descriptor = None
    for klass in xal::MailStop.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstop_has_type():
    assert hasattr(xal::MailStop, "type")
    descriptor = None
    for klass in xal::MailStop.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::mailstop_has_any():
    assert hasattr(xal::MailStop, "any")
    descriptor = None
    for klass in xal::MailStop.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal::departmentname_is_not_abstract():
    assert not inspect.isabstract(xal::DepartmentName)


def test_xal::departmentname_constructor_exists():
    assert callable(xal::DepartmentName.__init__)


def test_xal::departmentname_constructor_args():
    sig = inspect.signature(xal::DepartmentName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::departmentname_has_mixed():
    assert hasattr(xal::DepartmentName, "mixed")
    descriptor = None
    for klass in xal::DepartmentName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::departmentname_has_type():
    assert hasattr(xal::DepartmentName, "type")
    descriptor = None
    for klass in xal::DepartmentName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::departmentname_has_code():
    assert hasattr(xal::DepartmentName, "code")
    descriptor = None
    for klass in xal::DepartmentName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::departmentname_has_anyAttribute():
    assert hasattr(xal::DepartmentName, "anyAttribute")
    descriptor = None
    for klass in xal::DepartmentName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::department_is_not_abstract():
    assert not inspect.isabstract(xal::Department)


def test_xal::department_constructor_exists():
    assert callable(xal::Department.__init__)


def test_xal::department_constructor_args():
    sig = inspect.signature(xal::Department.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal::department_has_type():
    assert hasattr(xal::Department, "type")
    descriptor = None
    for klass in xal::Department.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::department_has_anyAttribute():
    assert hasattr(xal::Department, "anyAttribute")
    descriptor = None
    for klass in xal::Department.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::department_has_any():
    assert hasattr(xal::Department, "any")
    descriptor = None
    for klass in xal::Department.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal::countryname_is_not_abstract():
    assert not inspect.isabstract(xal::CountryName)


def test_xal::countryname_constructor_exists():
    assert callable(xal::CountryName.__init__)


def test_xal::countryname_constructor_args():
    sig = inspect.signature(xal::CountryName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::countryname_has_code():
    assert hasattr(xal::CountryName, "code")
    descriptor = None
    for klass in xal::CountryName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::countryname_has_mixed():
    assert hasattr(xal::CountryName, "mixed")
    descriptor = None
    for klass in xal::CountryName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::countryname_has_anyAttribute():
    assert hasattr(xal::CountryName, "anyAttribute")
    descriptor = None
    for klass in xal::CountryName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::countryname_has_type():
    assert hasattr(xal::CountryName, "type")
    descriptor = None
    for klass in xal::CountryName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::countrynamecode_is_not_abstract():
    assert not inspect.isabstract(xal::CountryNameCode)


def test_xal::countrynamecode_constructor_exists():
    assert callable(xal::CountryNameCode.__init__)


def test_xal::countrynamecode_constructor_args():
    sig = inspect.signature(xal::CountryNameCode.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::countrynamecode_has_scheme():
    assert hasattr(xal::CountryNameCode, "scheme")
    descriptor = None
    for klass in xal::CountryNameCode.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)

def test_xal::countrynamecode_has_code():
    assert hasattr(xal::CountryNameCode, "code")
    descriptor = None
    for klass in xal::CountryNameCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::countrynamecode_has_mixed():
    assert hasattr(xal::CountryNameCode, "mixed")
    descriptor = None
    for klass in xal::CountryNameCode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::countrynamecode_has_anyAttribute():
    assert hasattr(xal::CountryNameCode, "anyAttribute")
    descriptor = None
    for klass in xal::CountryNameCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::barcode_is_not_abstract():
    assert not inspect.isabstract(xal::Barcode)


def test_xal::barcode_constructor_exists():
    assert callable(xal::Barcode.__init__)


def test_xal::barcode_constructor_args():
    sig = inspect.signature(xal::Barcode.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::barcode_has_anyAttribute():
    assert hasattr(xal::Barcode, "anyAttribute")
    descriptor = None
    for klass in xal::Barcode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::barcode_has_type():
    assert hasattr(xal::Barcode, "type")
    descriptor = None
    for klass in xal::Barcode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::barcode_has_code():
    assert hasattr(xal::Barcode, "code")
    descriptor = None
    for klass in xal::Barcode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::barcode_has_mixed():
    assert hasattr(xal::Barcode, "mixed")
    descriptor = None
    for klass in xal::Barcode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::buildingname_is_not_abstract():
    assert not inspect.isabstract(xal::BuildingName)


def test_xal::buildingname_constructor_exists():
    assert callable(xal::BuildingName.__init__)


def test_xal::buildingname_constructor_args():
    sig = inspect.signature(xal::BuildingName.__init__)
    params = list(sig.parameters.keys())
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::buildingname_has_typeOccurrence():
    assert hasattr(xal::BuildingName, "typeOccurrence")
    descriptor = None
    for klass in xal::BuildingName.__mro__:
        if "typeOccurrence" in klass.__dict__:
            descriptor = klass.__dict__["typeOccurrence"]
            break
    assert isinstance(descriptor, property)

def test_xal::buildingname_has_mixed():
    assert hasattr(xal::BuildingName, "mixed")
    descriptor = None
    for klass in xal::BuildingName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::buildingname_has_type():
    assert hasattr(xal::BuildingName, "type")
    descriptor = None
    for klass in xal::BuildingName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::buildingname_has_anyAttribute():
    assert hasattr(xal::BuildingName, "anyAttribute")
    descriptor = None
    for klass in xal::BuildingName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::buildingname_has_code():
    assert hasattr(xal::BuildingName, "code")
    descriptor = None
    for klass in xal::BuildingName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalcode_is_not_abstract():
    assert not inspect.isabstract(xal::PostalCode)


def test_xal::postalcode_constructor_exists():
    assert callable(xal::PostalCode.__init__)


def test_xal::postalcode_constructor_args():
    sig = inspect.signature(xal::PostalCode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postalcode_has_type():
    assert hasattr(xal::PostalCode, "type")
    descriptor = None
    for klass in xal::PostalCode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcode_has_any():
    assert hasattr(xal::PostalCode, "any")
    descriptor = None
    for klass in xal::PostalCode.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalcode_has_anyAttribute():
    assert hasattr(xal::PostalCode, "anyAttribute")
    descriptor = None
    for klass in xal::PostalCode.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::postoffice_is_not_abstract():
    assert not inspect.isabstract(xal::PostOffice)


def test_xal::postoffice_constructor_exists():
    assert callable(xal::PostOffice.__init__)


def test_xal::postoffice_constructor_args():
    sig = inspect.signature(xal::PostOffice.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::postoffice_has_any():
    assert hasattr(xal::PostOffice, "any")
    descriptor = None
    for klass in xal::PostOffice.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::postoffice_has_type():
    assert hasattr(xal::PostOffice, "type")
    descriptor = None
    for klass in xal::PostOffice.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::postoffice_has_indicator():
    assert hasattr(xal::PostOffice, "indicator")
    descriptor = None
    for klass in xal::PostOffice.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::postoffice_has_anyAttribute():
    assert hasattr(xal::PostOffice, "anyAttribute")
    descriptor = None
    for klass in xal::PostOffice.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::addresslongitudedirection_is_not_abstract():
    assert not inspect.isabstract(xal::AddressLongitudeDirection)


def test_xal::addresslongitudedirection_constructor_exists():
    assert callable(xal::AddressLongitudeDirection.__init__)


def test_xal::addresslongitudedirection_constructor_args():
    sig = inspect.signature(xal::AddressLongitudeDirection.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::addresslongitudedirection_has_type():
    assert hasattr(xal::AddressLongitudeDirection, "type")
    descriptor = None
    for klass in xal::AddressLongitudeDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslongitudedirection_has_mixed():
    assert hasattr(xal::AddressLongitudeDirection, "mixed")
    descriptor = None
    for klass in xal::AddressLongitudeDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslongitudedirection_has_anyAttribute():
    assert hasattr(xal::AddressLongitudeDirection, "anyAttribute")
    descriptor = None
    for klass in xal::AddressLongitudeDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslongitudedirection_has_code():
    assert hasattr(xal::AddressLongitudeDirection, "code")
    descriptor = None
    for klass in xal::AddressLongitudeDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::subadministrativearea_is_not_abstract():
    assert not inspect.isabstract(xal::SubAdministrativeArea)


def test_xal::subadministrativearea_constructor_exists():
    assert callable(xal::SubAdministrativeArea.__init__)


def test_xal::subadministrativearea_constructor_args():
    sig = inspect.signature(xal::SubAdministrativeArea.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "usageType" in params, "Missing parameter 'usageType'"

def test_xal::subadministrativearea_has_anyAttribute():
    assert hasattr(xal::SubAdministrativeArea, "anyAttribute")
    descriptor = None
    for klass in xal::SubAdministrativeArea.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativearea_has_type():
    assert hasattr(xal::SubAdministrativeArea, "type")
    descriptor = None
    for klass in xal::SubAdministrativeArea.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativearea_has_any():
    assert hasattr(xal::SubAdministrativeArea, "any")
    descriptor = None
    for klass in xal::SubAdministrativeArea.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativearea_has_indicator():
    assert hasattr(xal::SubAdministrativeArea, "indicator")
    descriptor = None
    for klass in xal::SubAdministrativeArea.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::subadministrativearea_has_usageType():
    assert hasattr(xal::SubAdministrativeArea, "usageType")
    descriptor = None
    for klass in xal::SubAdministrativeArea.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)



def test_xal::administrativeareaname_is_not_abstract():
    assert not inspect.isabstract(xal::AdministrativeAreaName)


def test_xal::administrativeareaname_constructor_exists():
    assert callable(xal::AdministrativeAreaName.__init__)


def test_xal::administrativeareaname_constructor_args():
    sig = inspect.signature(xal::AdministrativeAreaName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::administrativeareaname_has_code():
    assert hasattr(xal::AdministrativeAreaName, "code")
    descriptor = None
    for klass in xal::AdministrativeAreaName.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativeareaname_has_anyAttribute():
    assert hasattr(xal::AdministrativeAreaName, "anyAttribute")
    descriptor = None
    for klass in xal::AdministrativeAreaName.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativeareaname_has_type():
    assert hasattr(xal::AdministrativeAreaName, "type")
    descriptor = None
    for klass in xal::AdministrativeAreaName.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativeareaname_has_mixed():
    assert hasattr(xal::AdministrativeAreaName, "mixed")
    descriptor = None
    for klass in xal::AdministrativeAreaName.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::addressline_is_not_abstract():
    assert not inspect.isabstract(xal::AddressLine)


def test_xal::addressline_constructor_exists():
    assert callable(xal::AddressLine.__init__)


def test_xal::addressline_constructor_args():
    sig = inspect.signature(xal::AddressLine.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::addressline_has_anyAttribute():
    assert hasattr(xal::AddressLine, "anyAttribute")
    descriptor = None
    for klass in xal::AddressLine.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressline_has_mixed():
    assert hasattr(xal::AddressLine, "mixed")
    descriptor = None
    for klass in xal::AddressLine.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressline_has_code():
    assert hasattr(xal::AddressLine, "code")
    descriptor = None
    for klass in xal::AddressLine.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressline_has_type():
    assert hasattr(xal::AddressLine, "type")
    descriptor = None
    for klass in xal::AddressLine.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::addresslongitude_is_not_abstract():
    assert not inspect.isabstract(xal::AddressLongitude)


def test_xal::addresslongitude_constructor_exists():
    assert callable(xal::AddressLongitude.__init__)


def test_xal::addresslongitude_constructor_args():
    sig = inspect.signature(xal::AddressLongitude.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::addresslongitude_has_mixed():
    assert hasattr(xal::AddressLongitude, "mixed")
    descriptor = None
    for klass in xal::AddressLongitude.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslongitude_has_anyAttribute():
    assert hasattr(xal::AddressLongitude, "anyAttribute")
    descriptor = None
    for klass in xal::AddressLongitude.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslongitude_has_code():
    assert hasattr(xal::AddressLongitude, "code")
    descriptor = None
    for klass in xal::AddressLongitude.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslongitude_has_type():
    assert hasattr(xal::AddressLongitude, "type")
    descriptor = None
    for klass in xal::AddressLongitude.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::addresslatitude_is_not_abstract():
    assert not inspect.isabstract(xal::AddressLatitude)


def test_xal::addresslatitude_constructor_exists():
    assert callable(xal::AddressLatitude.__init__)


def test_xal::addresslatitude_constructor_args():
    sig = inspect.signature(xal::AddressLatitude.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::addresslatitude_has_mixed():
    assert hasattr(xal::AddressLatitude, "mixed")
    descriptor = None
    for klass in xal::AddressLatitude.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslatitude_has_code():
    assert hasattr(xal::AddressLatitude, "code")
    descriptor = None
    for klass in xal::AddressLatitude.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslatitude_has_anyAttribute():
    assert hasattr(xal::AddressLatitude, "anyAttribute")
    descriptor = None
    for klass in xal::AddressLatitude.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslatitude_has_type():
    assert hasattr(xal::AddressLatitude, "type")
    descriptor = None
    for klass in xal::AddressLatitude.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::addresslatitudedirection_is_not_abstract():
    assert not inspect.isabstract(xal::AddressLatitudeDirection)


def test_xal::addresslatitudedirection_constructor_exists():
    assert callable(xal::AddressLatitudeDirection.__init__)


def test_xal::addresslatitudedirection_constructor_args():
    sig = inspect.signature(xal::AddressLatitudeDirection.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::addresslatitudedirection_has_anyAttribute():
    assert hasattr(xal::AddressLatitudeDirection, "anyAttribute")
    descriptor = None
    for klass in xal::AddressLatitudeDirection.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslatitudedirection_has_type():
    assert hasattr(xal::AddressLatitudeDirection, "type")
    descriptor = None
    for klass in xal::AddressLatitudeDirection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslatitudedirection_has_code():
    assert hasattr(xal::AddressLatitudeDirection, "code")
    descriptor = None
    for klass in xal::AddressLatitudeDirection.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslatitudedirection_has_mixed():
    assert hasattr(xal::AddressLatitudeDirection, "mixed")
    descriptor = None
    for klass in xal::AddressLatitudeDirection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xal::addressidentifier_is_not_abstract():
    assert not inspect.isabstract(xal::AddressIdentifier)


def test_xal::addressidentifier_constructor_exists():
    assert callable(xal::AddressIdentifier.__init__)


def test_xal::addressidentifier_constructor_args():
    sig = inspect.signature(xal::AddressIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "identifierType" in params, "Missing parameter 'identifierType'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"

def test_xal::addressidentifier_has_anyAttribute():
    assert hasattr(xal::AddressIdentifier, "anyAttribute")
    descriptor = None
    for klass in xal::AddressIdentifier.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressidentifier_has_identifierType():
    assert hasattr(xal::AddressIdentifier, "identifierType")
    descriptor = None
    for klass in xal::AddressIdentifier.__mro__:
        if "identifierType" in klass.__dict__:
            descriptor = klass.__dict__["identifierType"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressidentifier_has_mixed():
    assert hasattr(xal::AddressIdentifier, "mixed")
    descriptor = None
    for klass in xal::AddressIdentifier.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressidentifier_has_type():
    assert hasattr(xal::AddressIdentifier, "type")
    descriptor = None
    for klass in xal::AddressIdentifier.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressidentifier_has_code():
    assert hasattr(xal::AddressIdentifier, "code")
    descriptor = None
    for klass in xal::AddressIdentifier.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_xal::addresslines_is_not_abstract():
    assert not inspect.isabstract(xal::AddressLines)


def test_xal::addresslines_constructor_exists():
    assert callable(xal::AddressLines.__init__)


def test_xal::addresslines_constructor_args():
    sig = inspect.signature(xal::AddressLines.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::addresslines_has_any():
    assert hasattr(xal::AddressLines, "any")
    descriptor = None
    for klass in xal::AddressLines.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::addresslines_has_anyAttribute():
    assert hasattr(xal::AddressLines, "anyAttribute")
    descriptor = None
    for klass in xal::AddressLines.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::thoroughfare_is_not_abstract():
    assert not inspect.isabstract(xal::Thoroughfare)


def test_xal::thoroughfare_constructor_exists():
    assert callable(xal::Thoroughfare.__init__)


def test_xal::thoroughfare_constructor_args():
    sig = inspect.signature(xal::Thoroughfare.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "group" in params, "Missing parameter 'group'"
    assert "dependentThoroughfares" in params, "Missing parameter 'dependentThoroughfares'"
    assert "dependentThoroughfaresType" in params, "Missing parameter 'dependentThoroughfaresType'"
    assert "dependentThoroughfaresConnector" in params, "Missing parameter 'dependentThoroughfaresConnector'"
    assert "any" in params, "Missing parameter 'any'"
    assert "dependentThoroughfaresIndicator" in params, "Missing parameter 'dependentThoroughfaresIndicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::thoroughfare_has_type():
    assert hasattr(xal::Thoroughfare, "type")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_group():
    assert hasattr(xal::Thoroughfare, "group")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_dependentThoroughfares():
    assert hasattr(xal::Thoroughfare, "dependentThoroughfares")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "dependentThoroughfares" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfares"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_dependentThoroughfaresType():
    assert hasattr(xal::Thoroughfare, "dependentThoroughfaresType")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "dependentThoroughfaresType" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfaresType"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_dependentThoroughfaresConnector():
    assert hasattr(xal::Thoroughfare, "dependentThoroughfaresConnector")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "dependentThoroughfaresConnector" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfaresConnector"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_any():
    assert hasattr(xal::Thoroughfare, "any")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_dependentThoroughfaresIndicator():
    assert hasattr(xal::Thoroughfare, "dependentThoroughfaresIndicator")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "dependentThoroughfaresIndicator" in klass.__dict__:
            descriptor = klass.__dict__["dependentThoroughfaresIndicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::thoroughfare_has_anyAttribute():
    assert hasattr(xal::Thoroughfare, "anyAttribute")
    descriptor = None
    for klass in xal::Thoroughfare.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::locality_is_not_abstract():
    assert not inspect.isabstract(xal::Locality)


def test_xal::locality_constructor_exists():
    assert callable(xal::Locality.__init__)


def test_xal::locality_constructor_args():
    sig = inspect.signature(xal::Locality.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "any" in params, "Missing parameter 'any'"

def test_xal::locality_has_type():
    assert hasattr(xal::Locality, "type")
    descriptor = None
    for klass in xal::Locality.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::locality_has_usageType():
    assert hasattr(xal::Locality, "usageType")
    descriptor = None
    for klass in xal::Locality.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)

def test_xal::locality_has_anyAttribute():
    assert hasattr(xal::Locality, "anyAttribute")
    descriptor = None
    for klass in xal::Locality.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::locality_has_indicator():
    assert hasattr(xal::Locality, "indicator")
    descriptor = None
    for klass in xal::Locality.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::locality_has_any():
    assert hasattr(xal::Locality, "any")
    descriptor = None
    for klass in xal::Locality.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xal::administrativearea_is_not_abstract():
    assert not inspect.isabstract(xal::AdministrativeArea)


def test_xal::administrativearea_constructor_exists():
    assert callable(xal::AdministrativeArea.__init__)


def test_xal::administrativearea_constructor_args():
    sig = inspect.signature(xal::AdministrativeArea.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::administrativearea_has_indicator():
    assert hasattr(xal::AdministrativeArea, "indicator")
    descriptor = None
    for klass in xal::AdministrativeArea.__mro__:
        if "indicator" in klass.__dict__:
            descriptor = klass.__dict__["indicator"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativearea_has_anyAttribute():
    assert hasattr(xal::AdministrativeArea, "anyAttribute")
    descriptor = None
    for klass in xal::AdministrativeArea.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativearea_has_any():
    assert hasattr(xal::AdministrativeArea, "any")
    descriptor = None
    for klass in xal::AdministrativeArea.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativearea_has_usageType():
    assert hasattr(xal::AdministrativeArea, "usageType")
    descriptor = None
    for klass in xal::AdministrativeArea.__mro__:
        if "usageType" in klass.__dict__:
            descriptor = klass.__dict__["usageType"]
            break
    assert isinstance(descriptor, property)

def test_xal::administrativearea_has_type():
    assert hasattr(xal::AdministrativeArea, "type")
    descriptor = None
    for klass in xal::AdministrativeArea.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::country_is_not_abstract():
    assert not inspect.isabstract(xal::Country)


def test_xal::country_constructor_exists():
    assert callable(xal::Country.__init__)


def test_xal::country_constructor_args():
    sig = inspect.signature(xal::Country.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_xal::country_has_any():
    assert hasattr(xal::Country, "any")
    descriptor = None
    for klass in xal::Country.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::country_has_anyAttribute():
    assert hasattr(xal::Country, "anyAttribute")
    descriptor = None
    for klass in xal::Country.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_xal::postalserviceelements_is_not_abstract():
    assert not inspect.isabstract(xal::PostalServiceElements)


def test_xal::postalserviceelements_constructor_exists():
    assert callable(xal::PostalServiceElements.__init__)


def test_xal::postalserviceelements_constructor_args():
    sig = inspect.signature(xal::PostalServiceElements.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_xal::postalserviceelements_has_any():
    assert hasattr(xal::PostalServiceElements, "any")
    descriptor = None
    for klass in xal::PostalServiceElements.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalserviceelements_has_anyAttribute():
    assert hasattr(xal::PostalServiceElements, "anyAttribute")
    descriptor = None
    for klass in xal::PostalServiceElements.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::postalserviceelements_has_type():
    assert hasattr(xal::PostalServiceElements, "type")
    descriptor = None
    for klass in xal::PostalServiceElements.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xal::addressdetails_is_not_abstract():
    assert not inspect.isabstract(xal::AddressDetails)


def test_xal::addressdetails_constructor_exists():
    assert callable(xal::AddressDetails.__init__)


def test_xal::addressdetails_constructor_args():
    sig = inspect.signature(xal::AddressDetails.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "currentStatus" in params, "Missing parameter 'currentStatus'"
    assert "validFromDate" in params, "Missing parameter 'validFromDate'"
    assert "usage" in params, "Missing parameter 'usage'"
    assert "validToDate" in params, "Missing parameter 'validToDate'"
    assert "code" in params, "Missing parameter 'code'"
    assert "addressDetailsKey" in params, "Missing parameter 'addressDetailsKey'"
    assert "any" in params, "Missing parameter 'any'"
    assert "addressType" in params, "Missing parameter 'addressType'"

def test_xal::addressdetails_has_anyAttribute():
    assert hasattr(xal::AddressDetails, "anyAttribute")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_currentStatus():
    assert hasattr(xal::AddressDetails, "currentStatus")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "currentStatus" in klass.__dict__:
            descriptor = klass.__dict__["currentStatus"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_validFromDate():
    assert hasattr(xal::AddressDetails, "validFromDate")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "validFromDate" in klass.__dict__:
            descriptor = klass.__dict__["validFromDate"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_usage():
    assert hasattr(xal::AddressDetails, "usage")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "usage" in klass.__dict__:
            descriptor = klass.__dict__["usage"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_validToDate():
    assert hasattr(xal::AddressDetails, "validToDate")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "validToDate" in klass.__dict__:
            descriptor = klass.__dict__["validToDate"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_code():
    assert hasattr(xal::AddressDetails, "code")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_addressDetailsKey():
    assert hasattr(xal::AddressDetails, "addressDetailsKey")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "addressDetailsKey" in klass.__dict__:
            descriptor = klass.__dict__["addressDetailsKey"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_any():
    assert hasattr(xal::AddressDetails, "any")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xal::addressdetails_has_addressType():
    assert hasattr(xal::AddressDetails, "addressType")
    descriptor = None
    for klass in xal::AddressDetails.__mro__:
        if "addressType" in klass.__dict__:
            descriptor = klass.__dict__["addressType"]
            break
    assert isinstance(descriptor, property)



def test_xal::address_is_not_abstract():
    assert not inspect.isabstract(xal::Address)


def test_xal::address_constructor_exists():
    assert callable(xal::Address.__init__)


def test_xal::address_constructor_args():
    sig = inspect.signature(xal::Address.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xal::address_has_code():
    assert hasattr(xal::Address, "code")
    descriptor = None
    for klass in xal::Address.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_xal::address_has_type():
    assert hasattr(xal::Address, "type")
    descriptor = None
    for klass in xal::Address.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xal::address_has_anyAttribute():
    assert hasattr(xal::Address, "anyAttribute")
    descriptor = None
    for klass in xal::Address.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_xal::address_has_mixed():
    assert hasattr(xal::Address, "mixed")
    descriptor = None
    for klass in xal::Address.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_indicatoroccurrence1_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence1 is not None

def test_indicatoroccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence1]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence1"

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

def test_numbertypeoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberTypeOccurrence is not None

def test_numbertypeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeOccurrence]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeOccurrence"

def test_numberoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberOccurrence is not None

def test_numberoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberOccurrence]
    expected_literals = [
        "BeforeName",
        "AfterName",
        "AfterType",
        "BeforeType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberOccurrence"

def test_indicatoroccurence_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurence is not None

def test_indicatoroccurence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurence"

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

def test_indicatoroccurrence_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence is not None

def test_indicatoroccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence"

def test_numberrangeoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberRangeOccurrence is not None

def test_numberrangeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberRangeOccurrence]
    expected_literals = [
        "AfterType",
        "AfterName",
        "BeforeType",
        "BeforeName",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberRangeOccurrence"

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

def test_dependentthoroughfarestype_exists():
    # Check that the Enumeration exists
    assert DependentThoroughfaresType is not None

def test_dependentthoroughfarestype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DependentThoroughfaresType]
    expected_literals = [
        "Yes",
        "No",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DependentThoroughfaresType"

def test_numbertypetype_exists():
    # Check that the Enumeration exists
    assert NumberTypeType is not None

def test_numbertypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeType]
    expected_literals = [
        "Range",
        "Single",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeType"

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

def test_numbertypeoccurrence1_exists():
    # Check that the Enumeration exists
    assert NumberTypeOccurrence1 is not None

def test_numbertypeoccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeOccurrence1]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeOccurrence1"

def test_numbertypetype1_exists():
    # Check that the Enumeration exists
    assert NumberTypeType1 is not None

def test_numbertypetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeType1]
    expected_literals = [
        "Range",
        "Single",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeType1"

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

def test_numberrangeoccurence_exists():
    # Check that the Enumeration exists
    assert NumberRangeOccurence is not None

def test_numberrangeoccurence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberRangeOccurence]
    expected_literals = [
        "BeforeName",
        "BeforeType",
        "AfterType",
        "AfterName",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberRangeOccurence"

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
xal::ThoroughfareNumberTo_strategy = st.builds(
    xal::ThoroughfareNumberTo,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal::ThoroughfareNumberFrom_strategy = st.builds(
    xal::ThoroughfareNumberFrom,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal::ThoroughfareNumberRange_strategy = st.builds(
    xal::ThoroughfareNumberRange,
    indicatorOccurrence=
        safe_text,
    anyAttribute=
        safe_text,
    numberRangeOccurrence=
        safe_text,
    code=
        safe_text,
    rangeType=
        safe_text,
    type=
        safe_text,
    separator=
        safe_text,
    indicator=
        safe_text
)
xal::SubPremiseNumberPrefix_strategy = st.builds(
    xal::SubPremiseNumberPrefix,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    mixed=
        safe_text
)
xal::SubPremiseNumber_strategy = st.builds(
    xal::SubPremiseNumber,
    code=
        safe_text,
    indicatorOccurrence=
        safe_text,
    numberTypeOccurrence=
        safe_text,
    mixed=
        safe_text,
    indicator=
        safe_text,
    premiseNumberSeparator=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::SubPremiseNumberSuffix_strategy = st.builds(
    xal::SubPremiseNumberSuffix,
    code=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal::SubPremiseLocation_strategy = st.builds(
    xal::SubPremiseLocation,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::SubPremiseName_strategy = st.builds(
    xal::SubPremiseName,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text,
    typeOccurrence=
        safe_text,
    mixed=
        safe_text
)
xal::SubAdministrativeAreaName_strategy = st.builds(
    xal::SubAdministrativeAreaName,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::PremiseNumberRangeTo_strategy = st.builds(
    xal::PremiseNumberRangeTo,
)
xal::PremiseNumberRangeFrom_strategy = st.builds(
    xal::PremiseNumberRangeFrom,
)
xal::SubPremise_strategy = st.builds(
    xal::SubPremise,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal::PremiseName_strategy = st.builds(
    xal::PremiseName,
    mixed=
        safe_text,
    typeOccurrence=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::PremiseNumberRange_strategy = st.builds(
    xal::PremiseNumberRange,
    indicator=
        safe_text,
    type=
        safe_text,
    indicatorOccurence=
        safe_text,
    separator=
        safe_text,
    rangeType=
        safe_text,
    numberRangeOccurence=
        safe_text
)
xal::PremiseLocation_strategy = st.builds(
    xal::PremiseLocation,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::PostTownSuffix_strategy = st.builds(
    xal::PostTownSuffix,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::PostTownName_strategy = st.builds(
    xal::PostTownName,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::PostOfficeNumber_strategy = st.builds(
    xal::PostOfficeNumber,
    mixed=
        safe_text,
    indicatorOccurrence=
        safe_text,
    code=
        safe_text,
    indicator=
        safe_text,
    anyAttribute=
        safe_text
)
xal::PostOfficeName_strategy = st.builds(
    xal::PostOfficeName,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal::PostBoxNumberExtension_strategy = st.builds(
    xal::PostBoxNumberExtension,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    numberExtensionSeparator=
        safe_text
)
xal::PostBoxNumberSuffix_strategy = st.builds(
    xal::PostBoxNumberSuffix,
    mixed=
        safe_text,
    code=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    anyAttribute=
        safe_text
)
xal::PostBoxNumberPrefix_strategy = st.builds(
    xal::PostBoxNumberPrefix,
    code=
        safe_text,
    mixed=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    anyAttribute=
        safe_text
)
xal::SupplementaryPostalServiceData_strategy = st.builds(
    xal::SupplementaryPostalServiceData,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal::PostBoxNumber_strategy = st.builds(
    xal::PostBoxNumber,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal::SortingCode_strategy = st.builds(
    xal::SortingCode,
    code=
        safe_text,
    type=
        safe_text
)
xal::PostalRouteNumber_strategy = st.builds(
    xal::PostalRouteNumber,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal::PostalRouteName_strategy = st.builds(
    xal::PostalRouteName,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text
)
xal::PostalCodeNumberExtension_strategy = st.builds(
    xal::PostalCodeNumberExtension,
    numberExtensionSeparator=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal::PostalCodeNumber_strategy = st.builds(
    xal::PostalCodeNumber,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::PostTown_strategy = st.builds(
    xal::PostTown,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::MailStopNumber_strategy = st.builds(
    xal::MailStopNumber,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    nameNumberSeparator=
        safe_text,
    mixed=
        safe_text
)
xal::MailStopName_strategy = st.builds(
    xal::MailStopName,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal::LocalityName_strategy = st.builds(
    xal::LocalityName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal::LargeMailUserIdentifier_strategy = st.builds(
    xal::LargeMailUserIdentifier,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    indicator=
        safe_text
)
xal::LargeMailUserName_strategy = st.builds(
    xal::LargeMailUserName,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::KeyLineCode_strategy = st.builds(
    xal::KeyLineCode,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal::EndorsementLineCode_strategy = st.builds(
    xal::EndorsementLineCode,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal::Xal_strategy = st.builds(
    xal::Xal,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    version=
        safe_text
)
xal::FirmName_strategy = st.builds(
    xal::FirmName,
    code=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal::Firm_strategy = st.builds(
    xal::Firm,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    any=
        safe_text
)
xal::PremiseNumberSuffix_strategy = st.builds(
    xal::PremiseNumberSuffix,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal::PremiseNumberPrefix_strategy = st.builds(
    xal::PremiseNumberPrefix,
    anyAttribute=
        safe_text,
    value=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal::PremiseNumber_strategy = st.builds(
    xal::PremiseNumber,
    indicator=
        safe_text,
    code=
        safe_text,
    numberTypeOccurrence=
        safe_text,
    mixed=
        safe_text,
    numberType=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    indicatorOccurrence=
        safe_text
)
xal::ThoroughfareNumberSuffix_strategy = st.builds(
    xal::ThoroughfareNumberSuffix,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    numberSuffixSeparator=
        safe_text
)
xal::ThoroughfareNumberPrefix_strategy = st.builds(
    xal::ThoroughfareNumberPrefix,
    numberPrefixSeparator=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::ThoroughfareNumber_strategy = st.builds(
    xal::ThoroughfareNumber,
    anyAttribute=
        safe_text,
    indicator=
        safe_text,
    numberOccurrence=
        safe_text,
    numberType=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    indicatorOccurrence=
        safe_text,
    type=
        safe_text
)
xal::DocumentRoot_strategy = st.builds(
    xal::DocumentRoot,
    mixed=
        safe_text
)
xal::EStringToStringMapEntry_strategy = st.builds(
    xal::EStringToStringMapEntry,
)
xal::ThoroughfarePreDirection_strategy = st.builds(
    xal::ThoroughfarePreDirection,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text
)
xal::DependentThoroughfare_strategy = st.builds(
    xal::DependentThoroughfare,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::ThoroughfarePostDirection_strategy = st.builds(
    xal::ThoroughfarePostDirection,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::ThoroughfareTrailingType_strategy = st.builds(
    xal::ThoroughfareTrailingType,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal::ThoroughfareName_strategy = st.builds(
    xal::ThoroughfareName,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::ThoroughfareLeadingType_strategy = st.builds(
    xal::ThoroughfareLeadingType,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text
)
xal::PostalRoute_strategy = st.builds(
    xal::PostalRoute,
    any=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal::LargeMailUser_strategy = st.builds(
    xal::LargeMailUser,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal::Premise_strategy = st.builds(
    xal::Premise,
    premiseDependencyType=
        safe_text,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    premiseThoroughfareConnector=
        safe_text,
    premiseDependency=
        safe_text
)
xal::PostBox_strategy = st.builds(
    xal::PostBox,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    indicator=
        safe_text,
    type=
        safe_text
)
xal::DependentLocalityNumber_strategy = st.builds(
    xal::DependentLocalityNumber,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    nameNumberOccurrence=
        safe_text,
    code=
        safe_text
)
xal::DependentLocalityName_strategy = st.builds(
    xal::DependentLocalityName,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal::DependentLocality_strategy = st.builds(
    xal::DependentLocality,
    indicator=
        safe_text,
    type=
        safe_text,
    usageType=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    connector=
        safe_text
)
xal::MailStop_strategy = st.builds(
    xal::MailStop,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    any=
        safe_text
)
xal::DepartmentName_strategy = st.builds(
    xal::DepartmentName,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal::Department_strategy = st.builds(
    xal::Department,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal::CountryName_strategy = st.builds(
    xal::CountryName,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::CountryNameCode_strategy = st.builds(
    xal::CountryNameCode,
    scheme=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal::Barcode_strategy = st.builds(
    xal::Barcode,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::BuildingName_strategy = st.builds(
    xal::BuildingName,
    typeOccurrence=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::PostalCode_strategy = st.builds(
    xal::PostalCode,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal::PostOffice_strategy = st.builds(
    xal::PostOffice,
    any=
        safe_text,
    type=
        safe_text,
    indicator=
        safe_text,
    anyAttribute=
        safe_text
)
xal::AddressLongitudeDirection_strategy = st.builds(
    xal::AddressLongitudeDirection,
    type=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal::SubAdministrativeArea_strategy = st.builds(
    xal::SubAdministrativeArea,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    any=
        safe_text,
    indicator=
        safe_text,
    usageType=
        safe_text
)
xal::AdministrativeAreaName_strategy = st.builds(
    xal::AdministrativeAreaName,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text
)
xal::AddressLine_strategy = st.builds(
    xal::AddressLine,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal::AddressLongitude_strategy = st.builds(
    xal::AddressLongitude,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal::AddressLatitude_strategy = st.builds(
    xal::AddressLatitude,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::AddressLatitudeDirection_strategy = st.builds(
    xal::AddressLatitudeDirection,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal::AddressIdentifier_strategy = st.builds(
    xal::AddressIdentifier,
    anyAttribute=
        safe_text,
    identifierType=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal::AddressLines_strategy = st.builds(
    xal::AddressLines,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal::Thoroughfare_strategy = st.builds(
    xal::Thoroughfare,
    type=
        safe_text,
    group=
        safe_text,
    dependentThoroughfares=
        safe_text,
    dependentThoroughfaresType=
        safe_text,
    dependentThoroughfaresConnector=
        safe_text,
    any=
        safe_text,
    dependentThoroughfaresIndicator=
        safe_text,
    anyAttribute=
        safe_text
)
xal::Locality_strategy = st.builds(
    xal::Locality,
    type=
        safe_text,
    usageType=
        safe_text,
    anyAttribute=
        safe_text,
    indicator=
        safe_text,
    any=
        safe_text
)
xal::AdministrativeArea_strategy = st.builds(
    xal::AdministrativeArea,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    usageType=
        safe_text,
    type=
        safe_text
)
xal::Country_strategy = st.builds(
    xal::Country,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal::PostalServiceElements_strategy = st.builds(
    xal::PostalServiceElements,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal::AddressDetails_strategy = st.builds(
    xal::AddressDetails,
    anyAttribute=
        safe_text,
    currentStatus=
        safe_text,
    validFromDate=
        safe_text,
    usage=
        safe_text,
    validToDate=
        safe_text,
    code=
        safe_text,
    addressDetailsKey=
        safe_text,
    any=
        safe_text,
    addressType=
        safe_text
)
xal::Address_strategy = st.builds(
    xal::Address,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)

@given(instance=xal::ThoroughfareNumberTo_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarenumberto_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareNumberTo)

@given(instance=xal::ThoroughfareNumberTo_strategy)
def test_xal::thoroughfarenumberto_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareNumberTo_strategy)
def test_xal::thoroughfarenumberto_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareNumberTo_strategy)
def test_xal::thoroughfarenumberto_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareNumberTo_strategy)
def test_xal::thoroughfarenumberto_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareNumberTo_strategy)
def test_xal::thoroughfarenumberto_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareNumberTo_strategy)
def test_xal::thoroughfarenumberto_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareNumberFrom_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarenumberfrom_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareNumberFrom)

@given(instance=xal::ThoroughfareNumberFrom_strategy)
def test_xal::thoroughfarenumberfrom_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareNumberFrom_strategy)
def test_xal::thoroughfarenumberfrom_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareNumberFrom_strategy)
def test_xal::thoroughfarenumberfrom_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareNumberFrom_strategy)
def test_xal::thoroughfarenumberfrom_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareNumberFrom_strategy)
def test_xal::thoroughfarenumberfrom_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareNumberFrom_strategy)
def test_xal::thoroughfarenumberfrom_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarenumberrange_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareNumberRange)

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_indicatorOccurrence_type(instance):
    assert isinstance(instance.indicatorOccurrence, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_numberRangeOccurrence_type(instance):
    assert isinstance(instance.numberRangeOccurrence, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_numberRangeOccurrence_setter(instance):
    original = instance.numberRangeOccurrence
    instance.numberRangeOccurrence = original
    assert instance.numberRangeOccurrence == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_rangeType_type(instance):
    assert isinstance(instance.rangeType, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_rangeType_setter(instance):
    original = instance.rangeType
    instance.rangeType = original
    assert instance.rangeType == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_separator_type(instance):
    assert isinstance(instance.separator, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::ThoroughfareNumberRange_strategy)
def test_xal::thoroughfarenumberrange_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::SubPremiseNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal::subpremisenumberprefix_instantiation(instance):
    assert isinstance(instance, xal::SubPremiseNumberPrefix)

@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_numberPrefixSeparator_type(instance):
    assert isinstance(instance.numberPrefixSeparator, str)


@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original

@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SubPremiseNumberPrefix_strategy)
def test_xal::subpremisenumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SubPremiseNumber_strategy)
@settings(max_examples=50)
def test_xal::subpremisenumber_instantiation(instance):
    assert isinstance(instance, xal::SubPremiseNumber)

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_indicatorOccurrence_type(instance):
    assert isinstance(instance.indicatorOccurrence, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_numberTypeOccurrence_type(instance):
    assert isinstance(instance.numberTypeOccurrence, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_numberTypeOccurrence_setter(instance):
    original = instance.numberTypeOccurrence
    instance.numberTypeOccurrence = original
    assert instance.numberTypeOccurrence == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_premiseNumberSeparator_type(instance):
    assert isinstance(instance.premiseNumberSeparator, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_premiseNumberSeparator_setter(instance):
    original = instance.premiseNumberSeparator
    instance.premiseNumberSeparator = original
    assert instance.premiseNumberSeparator == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubPremiseNumber_strategy)
def test_xal::subpremisenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubPremiseNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal::subpremisenumbersuffix_instantiation(instance):
    assert isinstance(instance, xal::SubPremiseNumberSuffix)

@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_numberSuffixSeparator_type(instance):
    assert isinstance(instance.numberSuffixSeparator, str)


@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original

@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SubPremiseNumberSuffix_strategy)
def test_xal::subpremisenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SubPremiseLocation_strategy)
@settings(max_examples=50)
def test_xal::subpremiselocation_instantiation(instance):
    assert isinstance(instance, xal::SubPremiseLocation)

@given(instance=xal::SubPremiseLocation_strategy)
def test_xal::subpremiselocation_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SubPremiseLocation_strategy)
def test_xal::subpremiselocation_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SubPremiseLocation_strategy)
def test_xal::subpremiselocation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SubPremiseLocation_strategy)
def test_xal::subpremiselocation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SubPremiseName_strategy)
@settings(max_examples=50)
def test_xal::subpremisename_instantiation(instance):
    assert isinstance(instance, xal::SubPremiseName)

@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_typeOccurrence_type(instance):
    assert isinstance(instance.typeOccurrence, str)


@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original

@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SubPremiseName_strategy)
def test_xal::subpremisename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SubAdministrativeAreaName_strategy)
@settings(max_examples=50)
def test_xal::subadministrativeareaname_instantiation(instance):
    assert isinstance(instance, xal::SubAdministrativeAreaName)

@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SubAdministrativeAreaName_strategy)
def test_xal::subadministrativeareaname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PremiseNumberRangeTo_strategy)
@settings(max_examples=50)
def test_xal::premisenumberrangeto_instantiation(instance):
    assert isinstance(instance, xal::PremiseNumberRangeTo)

@given(instance=xal::PremiseNumberRangeFrom_strategy)
@settings(max_examples=50)
def test_xal::premisenumberrangefrom_instantiation(instance):
    assert isinstance(instance, xal::PremiseNumberRangeFrom)

@given(instance=xal::SubPremise_strategy)
@settings(max_examples=50)
def test_xal::subpremise_instantiation(instance):
    assert isinstance(instance, xal::SubPremise)

@given(instance=xal::SubPremise_strategy)
def test_xal::subpremise_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubPremise_strategy)
def test_xal::subpremise_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubPremise_strategy)
def test_xal::subpremise_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubPremise_strategy)
def test_xal::subpremise_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubPremise_strategy)
def test_xal::subpremise_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::SubPremise_strategy)
def test_xal::subpremise_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PremiseName_strategy)
@settings(max_examples=50)
def test_xal::premisename_instantiation(instance):
    assert isinstance(instance, xal::PremiseName)

@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_typeOccurrence_type(instance):
    assert isinstance(instance.typeOccurrence, str)


@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original

@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PremiseName_strategy)
def test_xal::premisename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PremiseNumberRange_strategy)
@settings(max_examples=50)
def test_xal::premisenumberrange_instantiation(instance):
    assert isinstance(instance, xal::PremiseNumberRange)

@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_indicatorOccurence_type(instance):
    assert isinstance(instance.indicatorOccurence, str)


@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_indicatorOccurence_setter(instance):
    original = instance.indicatorOccurence
    instance.indicatorOccurence = original
    assert instance.indicatorOccurence == original

@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_separator_type(instance):
    assert isinstance(instance.separator, str)


@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_rangeType_type(instance):
    assert isinstance(instance.rangeType, str)


@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_rangeType_setter(instance):
    original = instance.rangeType
    instance.rangeType = original
    assert instance.rangeType == original

@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_numberRangeOccurence_type(instance):
    assert isinstance(instance.numberRangeOccurence, str)


@given(instance=xal::PremiseNumberRange_strategy)
def test_xal::premisenumberrange_numberRangeOccurence_setter(instance):
    original = instance.numberRangeOccurence
    instance.numberRangeOccurence = original
    assert instance.numberRangeOccurence == original

@given(instance=xal::PremiseLocation_strategy)
@settings(max_examples=50)
def test_xal::premiselocation_instantiation(instance):
    assert isinstance(instance, xal::PremiseLocation)

@given(instance=xal::PremiseLocation_strategy)
def test_xal::premiselocation_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PremiseLocation_strategy)
def test_xal::premiselocation_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PremiseLocation_strategy)
def test_xal::premiselocation_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PremiseLocation_strategy)
def test_xal::premiselocation_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PremiseLocation_strategy)
def test_xal::premiselocation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PremiseLocation_strategy)
def test_xal::premiselocation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostTownSuffix_strategy)
@settings(max_examples=50)
def test_xal::posttownsuffix_instantiation(instance):
    assert isinstance(instance, xal::PostTownSuffix)

@given(instance=xal::PostTownSuffix_strategy)
def test_xal::posttownsuffix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostTownSuffix_strategy)
def test_xal::posttownsuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostTownSuffix_strategy)
def test_xal::posttownsuffix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostTownSuffix_strategy)
def test_xal::posttownsuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostTownSuffix_strategy)
def test_xal::posttownsuffix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostTownSuffix_strategy)
def test_xal::posttownsuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostTownName_strategy)
@settings(max_examples=50)
def test_xal::posttownname_instantiation(instance):
    assert isinstance(instance, xal::PostTownName)

@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostTownName_strategy)
def test_xal::posttownname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostOfficeNumber_strategy)
@settings(max_examples=50)
def test_xal::postofficenumber_instantiation(instance):
    assert isinstance(instance, xal::PostOfficeNumber)

@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_indicatorOccurrence_type(instance):
    assert isinstance(instance.indicatorOccurrence, str)


@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original

@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostOfficeNumber_strategy)
def test_xal::postofficenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostOfficeName_strategy)
@settings(max_examples=50)
def test_xal::postofficename_instantiation(instance):
    assert isinstance(instance, xal::PostOfficeName)

@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostOfficeName_strategy)
def test_xal::postofficename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostBoxNumberExtension_strategy)
@settings(max_examples=50)
def test_xal::postboxnumberextension_instantiation(instance):
    assert isinstance(instance, xal::PostBoxNumberExtension)

@given(instance=xal::PostBoxNumberExtension_strategy)
def test_xal::postboxnumberextension_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostBoxNumberExtension_strategy)
def test_xal::postboxnumberextension_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostBoxNumberExtension_strategy)
def test_xal::postboxnumberextension_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostBoxNumberExtension_strategy)
def test_xal::postboxnumberextension_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostBoxNumberExtension_strategy)
def test_xal::postboxnumberextension_numberExtensionSeparator_type(instance):
    assert isinstance(instance.numberExtensionSeparator, str)


@given(instance=xal::PostBoxNumberExtension_strategy)
def test_xal::postboxnumberextension_numberExtensionSeparator_setter(instance):
    original = instance.numberExtensionSeparator
    instance.numberExtensionSeparator = original
    assert instance.numberExtensionSeparator == original

@given(instance=xal::PostBoxNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal::postboxnumbersuffix_instantiation(instance):
    assert isinstance(instance, xal::PostBoxNumberSuffix)

@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_numberSuffixSeparator_type(instance):
    assert isinstance(instance.numberSuffixSeparator, str)


@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original

@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostBoxNumberSuffix_strategy)
def test_xal::postboxnumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostBoxNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal::postboxnumberprefix_instantiation(instance):
    assert isinstance(instance, xal::PostBoxNumberPrefix)

@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_numberPrefixSeparator_type(instance):
    assert isinstance(instance.numberPrefixSeparator, str)


@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original

@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostBoxNumberPrefix_strategy)
def test_xal::postboxnumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SupplementaryPostalServiceData_strategy)
@settings(max_examples=50)
def test_xal::supplementarypostalservicedata_instantiation(instance):
    assert isinstance(instance, xal::SupplementaryPostalServiceData)

@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SupplementaryPostalServiceData_strategy)
def test_xal::supplementarypostalservicedata_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostBoxNumber_strategy)
@settings(max_examples=50)
def test_xal::postboxnumber_instantiation(instance):
    assert isinstance(instance, xal::PostBoxNumber)

@given(instance=xal::PostBoxNumber_strategy)
def test_xal::postboxnumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostBoxNumber_strategy)
def test_xal::postboxnumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostBoxNumber_strategy)
def test_xal::postboxnumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostBoxNumber_strategy)
def test_xal::postboxnumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostBoxNumber_strategy)
def test_xal::postboxnumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostBoxNumber_strategy)
def test_xal::postboxnumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SortingCode_strategy)
@settings(max_examples=50)
def test_xal::sortingcode_instantiation(instance):
    assert isinstance(instance, xal::SortingCode)

@given(instance=xal::SortingCode_strategy)
def test_xal::sortingcode_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::SortingCode_strategy)
def test_xal::sortingcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SortingCode_strategy)
def test_xal::sortingcode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SortingCode_strategy)
def test_xal::sortingcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalRouteNumber_strategy)
@settings(max_examples=50)
def test_xal::postalroutenumber_instantiation(instance):
    assert isinstance(instance, xal::PostalRouteNumber)

@given(instance=xal::PostalRouteNumber_strategy)
def test_xal::postalroutenumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostalRouteNumber_strategy)
def test_xal::postalroutenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostalRouteNumber_strategy)
def test_xal::postalroutenumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalRouteNumber_strategy)
def test_xal::postalroutenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostalRouteNumber_strategy)
def test_xal::postalroutenumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostalRouteNumber_strategy)
def test_xal::postalroutenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostalRouteName_strategy)
@settings(max_examples=50)
def test_xal::postalroutename_instantiation(instance):
    assert isinstance(instance, xal::PostalRouteName)

@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostalRouteName_strategy)
def test_xal::postalroutename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalCodeNumberExtension_strategy)
@settings(max_examples=50)
def test_xal::postalcodenumberextension_instantiation(instance):
    assert isinstance(instance, xal::PostalCodeNumberExtension)

@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_numberExtensionSeparator_type(instance):
    assert isinstance(instance.numberExtensionSeparator, str)


@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_numberExtensionSeparator_setter(instance):
    original = instance.numberExtensionSeparator
    instance.numberExtensionSeparator = original
    assert instance.numberExtensionSeparator == original

@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostalCodeNumberExtension_strategy)
def test_xal::postalcodenumberextension_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostalCodeNumber_strategy)
@settings(max_examples=50)
def test_xal::postalcodenumber_instantiation(instance):
    assert isinstance(instance, xal::PostalCodeNumber)

@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PostalCodeNumber_strategy)
def test_xal::postalcodenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PostTown_strategy)
@settings(max_examples=50)
def test_xal::posttown_instantiation(instance):
    assert isinstance(instance, xal::PostTown)

@given(instance=xal::PostTown_strategy)
def test_xal::posttown_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostTown_strategy)
def test_xal::posttown_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostTown_strategy)
def test_xal::posttown_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostTown_strategy)
def test_xal::posttown_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::MailStopNumber_strategy)
@settings(max_examples=50)
def test_xal::mailstopnumber_instantiation(instance):
    assert isinstance(instance, xal::MailStopNumber)

@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_nameNumberSeparator_type(instance):
    assert isinstance(instance.nameNumberSeparator, str)


@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_nameNumberSeparator_setter(instance):
    original = instance.nameNumberSeparator
    instance.nameNumberSeparator = original
    assert instance.nameNumberSeparator == original

@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::MailStopNumber_strategy)
def test_xal::mailstopnumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::MailStopName_strategy)
@settings(max_examples=50)
def test_xal::mailstopname_instantiation(instance):
    assert isinstance(instance, xal::MailStopName)

@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::MailStopName_strategy)
def test_xal::mailstopname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::LocalityName_strategy)
@settings(max_examples=50)
def test_xal::localityname_instantiation(instance):
    assert isinstance(instance, xal::LocalityName)

@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::LocalityName_strategy)
def test_xal::localityname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::LargeMailUserIdentifier_strategy)
@settings(max_examples=50)
def test_xal::largemailuseridentifier_instantiation(instance):
    assert isinstance(instance, xal::LargeMailUserIdentifier)

@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::LargeMailUserIdentifier_strategy)
def test_xal::largemailuseridentifier_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::LargeMailUserName_strategy)
@settings(max_examples=50)
def test_xal::largemailusername_instantiation(instance):
    assert isinstance(instance, xal::LargeMailUserName)

@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::LargeMailUserName_strategy)
def test_xal::largemailusername_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::KeyLineCode_strategy)
@settings(max_examples=50)
def test_xal::keylinecode_instantiation(instance):
    assert isinstance(instance, xal::KeyLineCode)

@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::KeyLineCode_strategy)
def test_xal::keylinecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::EndorsementLineCode_strategy)
@settings(max_examples=50)
def test_xal::endorsementlinecode_instantiation(instance):
    assert isinstance(instance, xal::EndorsementLineCode)

@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::EndorsementLineCode_strategy)
def test_xal::endorsementlinecode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Xal_strategy)
@settings(max_examples=50)
def test_xal::xal_instantiation(instance):
    assert isinstance(instance, xal::Xal)

@given(instance=xal::Xal_strategy)
def test_xal::xal_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Xal_strategy)
def test_xal::xal_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::Xal_strategy)
def test_xal::xal_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Xal_strategy)
def test_xal::xal_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Xal_strategy)
def test_xal::xal_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xal::Xal_strategy)
def test_xal::xal_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xal::FirmName_strategy)
@settings(max_examples=50)
def test_xal::firmname_instantiation(instance):
    assert isinstance(instance, xal::FirmName)

@given(instance=xal::FirmName_strategy)
def test_xal::firmname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::FirmName_strategy)
def test_xal::firmname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::FirmName_strategy)
def test_xal::firmname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::FirmName_strategy)
def test_xal::firmname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::FirmName_strategy)
def test_xal::firmname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::FirmName_strategy)
def test_xal::firmname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::FirmName_strategy)
def test_xal::firmname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::FirmName_strategy)
def test_xal::firmname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Firm_strategy)
@settings(max_examples=50)
def test_xal::firm_instantiation(instance):
    assert isinstance(instance, xal::Firm)

@given(instance=xal::Firm_strategy)
def test_xal::firm_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Firm_strategy)
def test_xal::firm_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Firm_strategy)
def test_xal::firm_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Firm_strategy)
def test_xal::firm_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Firm_strategy)
def test_xal::firm_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Firm_strategy)
def test_xal::firm_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PremiseNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal::premisenumbersuffix_instantiation(instance):
    assert isinstance(instance, xal::PremiseNumberSuffix)

@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_numberSuffixSeparator_type(instance):
    assert isinstance(instance.numberSuffixSeparator, str)


@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original

@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PremiseNumberSuffix_strategy)
def test_xal::premisenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PremiseNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal::premisenumberprefix_instantiation(instance):
    assert isinstance(instance, xal::PremiseNumberPrefix)

@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_numberPrefixSeparator_type(instance):
    assert isinstance(instance.numberPrefixSeparator, str)


@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original

@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PremiseNumberPrefix_strategy)
def test_xal::premisenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PremiseNumber_strategy)
@settings(max_examples=50)
def test_xal::premisenumber_instantiation(instance):
    assert isinstance(instance, xal::PremiseNumber)

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_numberTypeOccurrence_type(instance):
    assert isinstance(instance.numberTypeOccurrence, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_numberTypeOccurrence_setter(instance):
    original = instance.numberTypeOccurrence
    instance.numberTypeOccurrence = original
    assert instance.numberTypeOccurrence == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_numberType_type(instance):
    assert isinstance(instance.numberType, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_numberType_setter(instance):
    original = instance.numberType
    instance.numberType = original
    assert instance.numberType == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_indicatorOccurrence_type(instance):
    assert isinstance(instance.indicatorOccurrence, str)


@given(instance=xal::PremiseNumber_strategy)
def test_xal::premisenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original

@given(instance=xal::ThoroughfareNumberSuffix_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarenumbersuffix_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareNumberSuffix)

@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_numberSuffixSeparator_type(instance):
    assert isinstance(instance.numberSuffixSeparator, str)


@given(instance=xal::ThoroughfareNumberSuffix_strategy)
def test_xal::thoroughfarenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original

@given(instance=xal::ThoroughfareNumberPrefix_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarenumberprefix_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareNumberPrefix)

@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_numberPrefixSeparator_type(instance):
    assert isinstance(instance.numberPrefixSeparator, str)


@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original

@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareNumberPrefix_strategy)
def test_xal::thoroughfarenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareNumber_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarenumber_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareNumber)

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_numberOccurrence_type(instance):
    assert isinstance(instance.numberOccurrence, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_numberOccurrence_setter(instance):
    original = instance.numberOccurrence
    instance.numberOccurrence = original
    assert instance.numberOccurrence == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_numberType_type(instance):
    assert isinstance(instance.numberType, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_numberType_setter(instance):
    original = instance.numberType
    instance.numberType = original
    assert instance.numberType == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_indicatorOccurrence_type(instance):
    assert isinstance(instance.indicatorOccurrence, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original

@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareNumber_strategy)
def test_xal::thoroughfarenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::DocumentRoot_strategy)
@settings(max_examples=50)
def test_xal::documentroot_instantiation(instance):
    assert isinstance(instance, xal::DocumentRoot)

@given(instance=xal::DocumentRoot_strategy)
def test_xal::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::DocumentRoot_strategy)
def test_xal::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xal::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xal::EStringToStringMapEntry)

@given(instance=xal::ThoroughfarePreDirection_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarepredirection_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfarePreDirection)

@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfarePreDirection_strategy)
def test_xal::thoroughfarepredirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::DependentThoroughfare_strategy)
@settings(max_examples=50)
def test_xal::dependentthoroughfare_instantiation(instance):
    assert isinstance(instance, xal::DependentThoroughfare)

@given(instance=xal::DependentThoroughfare_strategy)
def test_xal::dependentthoroughfare_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::DependentThoroughfare_strategy)
def test_xal::dependentthoroughfare_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::DependentThoroughfare_strategy)
def test_xal::dependentthoroughfare_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::DependentThoroughfare_strategy)
def test_xal::dependentthoroughfare_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::DependentThoroughfare_strategy)
def test_xal::dependentthoroughfare_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::DependentThoroughfare_strategy)
def test_xal::dependentthoroughfare_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfarePostDirection_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarepostdirection_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfarePostDirection)

@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfarePostDirection_strategy)
def test_xal::thoroughfarepostdirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareTrailingType_strategy)
@settings(max_examples=50)
def test_xal::thoroughfaretrailingtype_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareTrailingType)

@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareTrailingType_strategy)
def test_xal::thoroughfaretrailingtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfareName_strategy)
@settings(max_examples=50)
def test_xal::thoroughfarename_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareName)

@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareName_strategy)
def test_xal::thoroughfarename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareLeadingType_strategy)
@settings(max_examples=50)
def test_xal::thoroughfareleadingtype_instantiation(instance):
    assert isinstance(instance, xal::ThoroughfareLeadingType)

@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::ThoroughfareLeadingType_strategy)
def test_xal::thoroughfareleadingtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalRoute_strategy)
@settings(max_examples=50)
def test_xal::postalroute_instantiation(instance):
    assert isinstance(instance, xal::PostalRoute)

@given(instance=xal::PostalRoute_strategy)
def test_xal::postalroute_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::PostalRoute_strategy)
def test_xal::postalroute_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PostalRoute_strategy)
def test_xal::postalroute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostalRoute_strategy)
def test_xal::postalroute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalRoute_strategy)
def test_xal::postalroute_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalRoute_strategy)
def test_xal::postalroute_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::LargeMailUser_strategy)
@settings(max_examples=50)
def test_xal::largemailuser_instantiation(instance):
    assert isinstance(instance, xal::LargeMailUser)

@given(instance=xal::LargeMailUser_strategy)
def test_xal::largemailuser_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::LargeMailUser_strategy)
def test_xal::largemailuser_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::LargeMailUser_strategy)
def test_xal::largemailuser_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::LargeMailUser_strategy)
def test_xal::largemailuser_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::LargeMailUser_strategy)
def test_xal::largemailuser_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::LargeMailUser_strategy)
def test_xal::largemailuser_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Premise_strategy)
@settings(max_examples=50)
def test_xal::premise_instantiation(instance):
    assert isinstance(instance, xal::Premise)

@given(instance=xal::Premise_strategy)
def test_xal::premise_premiseDependencyType_type(instance):
    assert isinstance(instance.premiseDependencyType, str)


@given(instance=xal::Premise_strategy)
def test_xal::premise_premiseDependencyType_setter(instance):
    original = instance.premiseDependencyType
    instance.premiseDependencyType = original
    assert instance.premiseDependencyType == original

@given(instance=xal::Premise_strategy)
def test_xal::premise_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Premise_strategy)
def test_xal::premise_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Premise_strategy)
def test_xal::premise_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Premise_strategy)
def test_xal::premise_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::Premise_strategy)
def test_xal::premise_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Premise_strategy)
def test_xal::premise_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Premise_strategy)
def test_xal::premise_premiseThoroughfareConnector_type(instance):
    assert isinstance(instance.premiseThoroughfareConnector, str)


@given(instance=xal::Premise_strategy)
def test_xal::premise_premiseThoroughfareConnector_setter(instance):
    original = instance.premiseThoroughfareConnector
    instance.premiseThoroughfareConnector = original
    assert instance.premiseThoroughfareConnector == original

@given(instance=xal::Premise_strategy)
def test_xal::premise_premiseDependency_type(instance):
    assert isinstance(instance.premiseDependency, str)


@given(instance=xal::Premise_strategy)
def test_xal::premise_premiseDependency_setter(instance):
    original = instance.premiseDependency
    instance.premiseDependency = original
    assert instance.premiseDependency == original

@given(instance=xal::PostBox_strategy)
@settings(max_examples=50)
def test_xal::postbox_instantiation(instance):
    assert isinstance(instance, xal::PostBox)

@given(instance=xal::PostBox_strategy)
def test_xal::postbox_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostBox_strategy)
def test_xal::postbox_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostBox_strategy)
def test_xal::postbox_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::PostBox_strategy)
def test_xal::postbox_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PostBox_strategy)
def test_xal::postbox_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::PostBox_strategy)
def test_xal::postbox_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::PostBox_strategy)
def test_xal::postbox_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostBox_strategy)
def test_xal::postbox_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::DependentLocalityNumber_strategy)
@settings(max_examples=50)
def test_xal::dependentlocalitynumber_instantiation(instance):
    assert isinstance(instance, xal::DependentLocalityNumber)

@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_nameNumberOccurrence_type(instance):
    assert isinstance(instance.nameNumberOccurrence, str)


@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_nameNumberOccurrence_setter(instance):
    original = instance.nameNumberOccurrence
    instance.nameNumberOccurrence = original
    assert instance.nameNumberOccurrence == original

@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::DependentLocalityNumber_strategy)
def test_xal::dependentlocalitynumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::DependentLocalityName_strategy)
@settings(max_examples=50)
def test_xal::dependentlocalityname_instantiation(instance):
    assert isinstance(instance, xal::DependentLocalityName)

@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::DependentLocalityName_strategy)
def test_xal::dependentlocalityname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::DependentLocality_strategy)
@settings(max_examples=50)
def test_xal::dependentlocality_instantiation(instance):
    assert isinstance(instance, xal::DependentLocality)

@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_usageType_type(instance):
    assert isinstance(instance.usageType, str)


@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original

@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_connector_type(instance):
    assert isinstance(instance.connector, str)


@given(instance=xal::DependentLocality_strategy)
def test_xal::dependentlocality_connector_setter(instance):
    original = instance.connector
    instance.connector = original
    assert instance.connector == original

@given(instance=xal::MailStop_strategy)
@settings(max_examples=50)
def test_xal::mailstop_instantiation(instance):
    assert isinstance(instance, xal::MailStop)

@given(instance=xal::MailStop_strategy)
def test_xal::mailstop_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::MailStop_strategy)
def test_xal::mailstop_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::MailStop_strategy)
def test_xal::mailstop_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::MailStop_strategy)
def test_xal::mailstop_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::MailStop_strategy)
def test_xal::mailstop_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::MailStop_strategy)
def test_xal::mailstop_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::DepartmentName_strategy)
@settings(max_examples=50)
def test_xal::departmentname_instantiation(instance):
    assert isinstance(instance, xal::DepartmentName)

@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::DepartmentName_strategy)
def test_xal::departmentname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Department_strategy)
@settings(max_examples=50)
def test_xal::department_instantiation(instance):
    assert isinstance(instance, xal::Department)

@given(instance=xal::Department_strategy)
def test_xal::department_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Department_strategy)
def test_xal::department_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Department_strategy)
def test_xal::department_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Department_strategy)
def test_xal::department_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Department_strategy)
def test_xal::department_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Department_strategy)
def test_xal::department_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::CountryName_strategy)
@settings(max_examples=50)
def test_xal::countryname_instantiation(instance):
    assert isinstance(instance, xal::CountryName)

@given(instance=xal::CountryName_strategy)
def test_xal::countryname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::CountryName_strategy)
def test_xal::countryname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::CountryName_strategy)
def test_xal::countryname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::CountryName_strategy)
def test_xal::countryname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::CountryName_strategy)
def test_xal::countryname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::CountryName_strategy)
def test_xal::countryname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::CountryName_strategy)
def test_xal::countryname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::CountryName_strategy)
def test_xal::countryname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::CountryNameCode_strategy)
@settings(max_examples=50)
def test_xal::countrynamecode_instantiation(instance):
    assert isinstance(instance, xal::CountryNameCode)

@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_scheme_type(instance):
    assert isinstance(instance.scheme, str)


@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::CountryNameCode_strategy)
def test_xal::countrynamecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Barcode_strategy)
@settings(max_examples=50)
def test_xal::barcode_instantiation(instance):
    assert isinstance(instance, xal::Barcode)

@given(instance=xal::Barcode_strategy)
def test_xal::barcode_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Barcode_strategy)
def test_xal::barcode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Barcode_strategy)
def test_xal::barcode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Barcode_strategy)
def test_xal::barcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Barcode_strategy)
def test_xal::barcode_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::Barcode_strategy)
def test_xal::barcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::Barcode_strategy)
def test_xal::barcode_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::Barcode_strategy)
def test_xal::barcode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::BuildingName_strategy)
@settings(max_examples=50)
def test_xal::buildingname_instantiation(instance):
    assert isinstance(instance, xal::BuildingName)

@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_typeOccurrence_type(instance):
    assert isinstance(instance.typeOccurrence, str)


@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original

@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::BuildingName_strategy)
def test_xal::buildingname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::PostalCode_strategy)
@settings(max_examples=50)
def test_xal::postalcode_instantiation(instance):
    assert isinstance(instance, xal::PostalCode)

@given(instance=xal::PostalCode_strategy)
def test_xal::postalcode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostalCode_strategy)
def test_xal::postalcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostalCode_strategy)
def test_xal::postalcode_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::PostalCode_strategy)
def test_xal::postalcode_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PostalCode_strategy)
def test_xal::postalcode_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalCode_strategy)
def test_xal::postalcode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostOffice_strategy)
@settings(max_examples=50)
def test_xal::postoffice_instantiation(instance):
    assert isinstance(instance, xal::PostOffice)

@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostOffice_strategy)
def test_xal::postoffice_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressLongitudeDirection_strategy)
@settings(max_examples=50)
def test_xal::addresslongitudedirection_instantiation(instance):
    assert isinstance(instance, xal::AddressLongitudeDirection)

@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressLongitudeDirection_strategy)
def test_xal::addresslongitudedirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::SubAdministrativeArea_strategy)
@settings(max_examples=50)
def test_xal::subadministrativearea_instantiation(instance):
    assert isinstance(instance, xal::SubAdministrativeArea)

@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_usageType_type(instance):
    assert isinstance(instance.usageType, str)


@given(instance=xal::SubAdministrativeArea_strategy)
def test_xal::subadministrativearea_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original

@given(instance=xal::AdministrativeAreaName_strategy)
@settings(max_examples=50)
def test_xal::administrativeareaname_instantiation(instance):
    assert isinstance(instance, xal::AdministrativeAreaName)

@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AdministrativeAreaName_strategy)
def test_xal::administrativeareaname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressLine_strategy)
@settings(max_examples=50)
def test_xal::addressline_instantiation(instance):
    assert isinstance(instance, xal::AddressLine)

@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AddressLine_strategy)
def test_xal::addressline_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressLongitude_strategy)
@settings(max_examples=50)
def test_xal::addresslongitude_instantiation(instance):
    assert isinstance(instance, xal::AddressLongitude)

@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AddressLongitude_strategy)
def test_xal::addresslongitude_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressLatitude_strategy)
@settings(max_examples=50)
def test_xal::addresslatitude_instantiation(instance):
    assert isinstance(instance, xal::AddressLatitude)

@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AddressLatitude_strategy)
def test_xal::addresslatitude_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressLatitudeDirection_strategy)
@settings(max_examples=50)
def test_xal::addresslatitudedirection_instantiation(instance):
    assert isinstance(instance, xal::AddressLatitudeDirection)

@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AddressLatitudeDirection_strategy)
def test_xal::addresslatitudedirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressIdentifier_strategy)
@settings(max_examples=50)
def test_xal::addressidentifier_instantiation(instance):
    assert isinstance(instance, xal::AddressIdentifier)

@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_identifierType_type(instance):
    assert isinstance(instance.identifierType, str)


@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_identifierType_setter(instance):
    original = instance.identifierType
    instance.identifierType = original
    assert instance.identifierType == original

@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressIdentifier_strategy)
def test_xal::addressidentifier_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AddressLines_strategy)
@settings(max_examples=50)
def test_xal::addresslines_instantiation(instance):
    assert isinstance(instance, xal::AddressLines)

@given(instance=xal::AddressLines_strategy)
def test_xal::addresslines_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::AddressLines_strategy)
def test_xal::addresslines_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::AddressLines_strategy)
def test_xal::addresslines_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressLines_strategy)
def test_xal::addresslines_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Thoroughfare_strategy)
@settings(max_examples=50)
def test_xal::thoroughfare_instantiation(instance):
    assert isinstance(instance, xal::Thoroughfare)

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfares_type(instance):
    assert isinstance(instance.dependentThoroughfares, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfares_setter(instance):
    original = instance.dependentThoroughfares
    instance.dependentThoroughfares = original
    assert instance.dependentThoroughfares == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfaresType_type(instance):
    assert isinstance(instance.dependentThoroughfaresType, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfaresType_setter(instance):
    original = instance.dependentThoroughfaresType
    instance.dependentThoroughfaresType = original
    assert instance.dependentThoroughfaresType == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfaresConnector_type(instance):
    assert isinstance(instance.dependentThoroughfaresConnector, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfaresConnector_setter(instance):
    original = instance.dependentThoroughfaresConnector
    instance.dependentThoroughfaresConnector = original
    assert instance.dependentThoroughfaresConnector == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfaresIndicator_type(instance):
    assert isinstance(instance.dependentThoroughfaresIndicator, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_dependentThoroughfaresIndicator_setter(instance):
    original = instance.dependentThoroughfaresIndicator
    instance.dependentThoroughfaresIndicator = original
    assert instance.dependentThoroughfaresIndicator == original

@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Thoroughfare_strategy)
def test_xal::thoroughfare_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Locality_strategy)
@settings(max_examples=50)
def test_xal::locality_instantiation(instance):
    assert isinstance(instance, xal::Locality)

@given(instance=xal::Locality_strategy)
def test_xal::locality_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Locality_strategy)
def test_xal::locality_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Locality_strategy)
def test_xal::locality_usageType_type(instance):
    assert isinstance(instance.usageType, str)


@given(instance=xal::Locality_strategy)
def test_xal::locality_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original

@given(instance=xal::Locality_strategy)
def test_xal::locality_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Locality_strategy)
def test_xal::locality_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Locality_strategy)
def test_xal::locality_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::Locality_strategy)
def test_xal::locality_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::Locality_strategy)
def test_xal::locality_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Locality_strategy)
def test_xal::locality_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::AdministrativeArea_strategy)
@settings(max_examples=50)
def test_xal::administrativearea_instantiation(instance):
    assert isinstance(instance, xal::AdministrativeArea)

@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_indicator_type(instance):
    assert isinstance(instance.indicator, str)


@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original

@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_usageType_type(instance):
    assert isinstance(instance.usageType, str)


@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original

@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::AdministrativeArea_strategy)
def test_xal::administrativearea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Country_strategy)
@settings(max_examples=50)
def test_xal::country_instantiation(instance):
    assert isinstance(instance, xal::Country)

@given(instance=xal::Country_strategy)
def test_xal::country_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::Country_strategy)
def test_xal::country_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::Country_strategy)
def test_xal::country_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Country_strategy)
def test_xal::country_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostalServiceElements_strategy)
@settings(max_examples=50)
def test_xal::postalserviceelements_instantiation(instance):
    assert isinstance(instance, xal::PostalServiceElements)

@given(instance=xal::PostalServiceElements_strategy)
def test_xal::postalserviceelements_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::PostalServiceElements_strategy)
def test_xal::postalserviceelements_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::PostalServiceElements_strategy)
def test_xal::postalserviceelements_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::PostalServiceElements_strategy)
def test_xal::postalserviceelements_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::PostalServiceElements_strategy)
def test_xal::postalserviceelements_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::PostalServiceElements_strategy)
def test_xal::postalserviceelements_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::AddressDetails_strategy)
@settings(max_examples=50)
def test_xal::addressdetails_instantiation(instance):
    assert isinstance(instance, xal::AddressDetails)

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_currentStatus_type(instance):
    assert isinstance(instance.currentStatus, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_currentStatus_setter(instance):
    original = instance.currentStatus
    instance.currentStatus = original
    assert instance.currentStatus == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_validFromDate_type(instance):
    assert isinstance(instance.validFromDate, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_validFromDate_setter(instance):
    original = instance.validFromDate
    instance.validFromDate = original
    assert instance.validFromDate == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_usage_type(instance):
    assert isinstance(instance.usage, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_usage_setter(instance):
    original = instance.usage
    instance.usage = original
    assert instance.usage == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_validToDate_type(instance):
    assert isinstance(instance.validToDate, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_validToDate_setter(instance):
    original = instance.validToDate
    instance.validToDate = original
    assert instance.validToDate == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_addressDetailsKey_type(instance):
    assert isinstance(instance.addressDetailsKey, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_addressDetailsKey_setter(instance):
    original = instance.addressDetailsKey
    instance.addressDetailsKey = original
    assert instance.addressDetailsKey == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_addressType_type(instance):
    assert isinstance(instance.addressType, str)


@given(instance=xal::AddressDetails_strategy)
def test_xal::addressdetails_addressType_setter(instance):
    original = instance.addressType
    instance.addressType = original
    assert instance.addressType == original

@given(instance=xal::Address_strategy)
@settings(max_examples=50)
def test_xal::address_instantiation(instance):
    assert isinstance(instance, xal::Address)

@given(instance=xal::Address_strategy)
def test_xal::address_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=xal::Address_strategy)
def test_xal::address_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=xal::Address_strategy)
def test_xal::address_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xal::Address_strategy)
def test_xal::address_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xal::Address_strategy)
def test_xal::address_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=xal::Address_strategy)
def test_xal::address_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=xal::Address_strategy)
def test_xal::address_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xal::Address_strategy)
def test_xal::address_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
