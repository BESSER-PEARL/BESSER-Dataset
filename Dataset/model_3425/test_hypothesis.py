import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecvi::ResultValue,
    ecvi::ProgramStatus,
    ecvi::PhoneNum,
    ecvi::GroupLot,
    ecvi::Premises,
    ecvi::MovementPurposes,
    ecvi::Veterinarian,
    ecvi::Ecvi,
    ecvi::EStringToStringMapEntry,
    ecvi::DocumentRoot,
    ecvi::Contact,
    ecvi::Person,
    ecvi::Test,
    ecvi::AnimalTag,
    ecvi::Animal,
    ecvi::Attachement,
    ecvi::Address,
    ecvi::Accessions,
    ecvi::GeoPoint,
    ecvi::Laboratory,
    ecvi::Accession,
    UsState,
    TagType,
    ProgramStatusValue,
    PhoneDevice,
    DocType,
    ProgramStatusName,
    Sex,
    ISO3166Country,
    ResultName,
    MovementPurpose,
    SpeciesCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecvi::resultvalue_is_not_abstract():
    assert not inspect.isabstract(ecvi::ResultValue)


def test_ecvi::resultvalue_constructor_exists():
    assert callable(ecvi::ResultValue.__init__)


def test_ecvi::resultvalue_constructor_args():
    sig = inspect.signature(ecvi::ResultValue.__init__)
    params = list(sig.parameters.keys())
    assert "resultFloat" in params, "Missing parameter 'resultFloat'"
    assert "resultName" in params, "Missing parameter 'resultName'"
    assert "resultString" in params, "Missing parameter 'resultString'"
    assert "resultInteger" in params, "Missing parameter 'resultInteger'"

def test_ecvi::resultvalue_has_resultFloat():
    assert hasattr(ecvi::ResultValue, "resultFloat")
    descriptor = None
    for klass in ecvi::ResultValue.__mro__:
        if "resultFloat" in klass.__dict__:
            descriptor = klass.__dict__["resultFloat"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::resultvalue_has_resultName():
    assert hasattr(ecvi::ResultValue, "resultName")
    descriptor = None
    for klass in ecvi::ResultValue.__mro__:
        if "resultName" in klass.__dict__:
            descriptor = klass.__dict__["resultName"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::resultvalue_has_resultString():
    assert hasattr(ecvi::ResultValue, "resultString")
    descriptor = None
    for klass in ecvi::ResultValue.__mro__:
        if "resultString" in klass.__dict__:
            descriptor = klass.__dict__["resultString"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::resultvalue_has_resultInteger():
    assert hasattr(ecvi::ResultValue, "resultInteger")
    descriptor = None
    for klass in ecvi::ResultValue.__mro__:
        if "resultInteger" in klass.__dict__:
            descriptor = klass.__dict__["resultInteger"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::programstatus_is_not_abstract():
    assert not inspect.isabstract(ecvi::ProgramStatus)


def test_ecvi::programstatus_constructor_exists():
    assert callable(ecvi::ProgramStatus.__init__)


def test_ecvi::programstatus_constructor_args():
    sig = inspect.signature(ecvi::ProgramStatus.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "valueOther" in params, "Missing parameter 'valueOther'"
    assert "value" in params, "Missing parameter 'value'"

def test_ecvi::programstatus_has_name():
    assert hasattr(ecvi::ProgramStatus, "name")
    descriptor = None
    for klass in ecvi::ProgramStatus.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::programstatus_has_valueOther():
    assert hasattr(ecvi::ProgramStatus, "valueOther")
    descriptor = None
    for klass in ecvi::ProgramStatus.__mro__:
        if "valueOther" in klass.__dict__:
            descriptor = klass.__dict__["valueOther"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::programstatus_has_value():
    assert hasattr(ecvi::ProgramStatus, "value")
    descriptor = None
    for klass in ecvi::ProgramStatus.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::phonenum_is_not_abstract():
    assert not inspect.isabstract(ecvi::PhoneNum)


def test_ecvi::phonenum_constructor_exists():
    assert callable(ecvi::PhoneNum.__init__)


def test_ecvi::phonenum_constructor_args():
    sig = inspect.signature(ecvi::PhoneNum.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "type" in params, "Missing parameter 'type'"
    assert "number" in params, "Missing parameter 'number'"

def test_ecvi::phonenum_has_comment():
    assert hasattr(ecvi::PhoneNum, "comment")
    descriptor = None
    for klass in ecvi::PhoneNum.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::phonenum_has_type():
    assert hasattr(ecvi::PhoneNum, "type")
    descriptor = None
    for klass in ecvi::PhoneNum.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::phonenum_has_number():
    assert hasattr(ecvi::PhoneNum, "number")
    descriptor = None
    for klass in ecvi::PhoneNum.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::grouplot_is_not_abstract():
    assert not inspect.isabstract(ecvi::GroupLot)


def test_ecvi::grouplot_constructor_exists():
    assert callable(ecvi::GroupLot.__init__)


def test_ecvi::grouplot_constructor_args():
    sig = inspect.signature(ecvi::GroupLot.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "description" in params, "Missing parameter 'description'"
    assert "age" in params, "Missing parameter 'age'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "species" in params, "Missing parameter 'species'"
    assert "sexDetail" in params, "Missing parameter 'sexDetail'"

def test_ecvi::grouplot_has_quantity():
    assert hasattr(ecvi::GroupLot, "quantity")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_breed():
    assert hasattr(ecvi::GroupLot, "breed")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_unit():
    assert hasattr(ecvi::GroupLot, "unit")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_description():
    assert hasattr(ecvi::GroupLot, "description")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_age():
    assert hasattr(ecvi::GroupLot, "age")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_sex():
    assert hasattr(ecvi::GroupLot, "sex")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_species():
    assert hasattr(ecvi::GroupLot, "species")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "species" in klass.__dict__:
            descriptor = klass.__dict__["species"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::grouplot_has_sexDetail():
    assert hasattr(ecvi::GroupLot, "sexDetail")
    descriptor = None
    for klass in ecvi::GroupLot.__mro__:
        if "sexDetail" in klass.__dict__:
            descriptor = klass.__dict__["sexDetail"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::premises_is_not_abstract():
    assert not inspect.isabstract(ecvi::Premises)


def test_ecvi::premises_constructor_exists():
    assert callable(ecvi::Premises.__init__)


def test_ecvi::premises_constructor_args():
    sig = inspect.signature(ecvi::Premises.__init__)
    params = list(sig.parameters.keys())
    assert "premId" in params, "Missing parameter 'premId'"
    assert "premName" in params, "Missing parameter 'premName'"

def test_ecvi::premises_has_premId():
    assert hasattr(ecvi::Premises, "premId")
    descriptor = None
    for klass in ecvi::Premises.__mro__:
        if "premId" in klass.__dict__:
            descriptor = klass.__dict__["premId"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::premises_has_premName():
    assert hasattr(ecvi::Premises, "premName")
    descriptor = None
    for klass in ecvi::Premises.__mro__:
        if "premName" in klass.__dict__:
            descriptor = klass.__dict__["premName"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::movementpurposes_is_not_abstract():
    assert not inspect.isabstract(ecvi::MovementPurposes)


def test_ecvi::movementpurposes_constructor_exists():
    assert callable(ecvi::MovementPurposes.__init__)


def test_ecvi::movementpurposes_constructor_args():
    sig = inspect.signature(ecvi::MovementPurposes.__init__)
    params = list(sig.parameters.keys())
    assert "movementPurpose" in params, "Missing parameter 'movementPurpose'"

def test_ecvi::movementpurposes_has_movementPurpose():
    assert hasattr(ecvi::MovementPurposes, "movementPurpose")
    descriptor = None
    for klass in ecvi::MovementPurposes.__mro__:
        if "movementPurpose" in klass.__dict__:
            descriptor = klass.__dict__["movementPurpose"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::veterinarian_is_not_abstract():
    assert not inspect.isabstract(ecvi::Veterinarian)


def test_ecvi::veterinarian_constructor_exists():
    assert callable(ecvi::Veterinarian.__init__)


def test_ecvi::veterinarian_constructor_args():
    sig = inspect.signature(ecvi::Veterinarian.__init__)
    params = list(sig.parameters.keys())
    assert "licenseIssueState" in params, "Missing parameter 'licenseIssueState'"
    assert "licenseNumber" in params, "Missing parameter 'licenseNumber'"
    assert "nationalAccreditationNumber" in params, "Missing parameter 'nationalAccreditationNumber'"

def test_ecvi::veterinarian_has_licenseIssueState():
    assert hasattr(ecvi::Veterinarian, "licenseIssueState")
    descriptor = None
    for klass in ecvi::Veterinarian.__mro__:
        if "licenseIssueState" in klass.__dict__:
            descriptor = klass.__dict__["licenseIssueState"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::veterinarian_has_licenseNumber():
    assert hasattr(ecvi::Veterinarian, "licenseNumber")
    descriptor = None
    for klass in ecvi::Veterinarian.__mro__:
        if "licenseNumber" in klass.__dict__:
            descriptor = klass.__dict__["licenseNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::veterinarian_has_nationalAccreditationNumber():
    assert hasattr(ecvi::Veterinarian, "nationalAccreditationNumber")
    descriptor = None
    for klass in ecvi::Veterinarian.__mro__:
        if "nationalAccreditationNumber" in klass.__dict__:
            descriptor = klass.__dict__["nationalAccreditationNumber"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::ecvi_is_not_abstract():
    assert not inspect.isabstract(ecvi::Ecvi)


def test_ecvi::ecvi_constructor_exists():
    assert callable(ecvi::Ecvi.__init__)


def test_ecvi::ecvi_constructor_args():
    sig = inspect.signature(ecvi::Ecvi.__init__)
    params = list(sig.parameters.keys())
    assert "speciesCode" in params, "Missing parameter 'speciesCode'"
    assert "group" in params, "Missing parameter 'group'"
    assert "shipmentDate" in params, "Missing parameter 'shipmentDate'"
    assert "entryPermitNumber" in params, "Missing parameter 'entryPermitNumber'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"
    assert "issueDate" in params, "Missing parameter 'issueDate'"
    assert "cviNumber" in params, "Missing parameter 'cviNumber'"

def test_ecvi::ecvi_has_speciesCode():
    assert hasattr(ecvi::Ecvi, "speciesCode")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "speciesCode" in klass.__dict__:
            descriptor = klass.__dict__["speciesCode"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_group():
    assert hasattr(ecvi::Ecvi, "group")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_shipmentDate():
    assert hasattr(ecvi::Ecvi, "shipmentDate")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "shipmentDate" in klass.__dict__:
            descriptor = klass.__dict__["shipmentDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_entryPermitNumber():
    assert hasattr(ecvi::Ecvi, "entryPermitNumber")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "entryPermitNumber" in klass.__dict__:
            descriptor = klass.__dict__["entryPermitNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_group1():
    assert hasattr(ecvi::Ecvi, "group1")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_expirationDate():
    assert hasattr(ecvi::Ecvi, "expirationDate")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "expirationDate" in klass.__dict__:
            descriptor = klass.__dict__["expirationDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_issueDate():
    assert hasattr(ecvi::Ecvi, "issueDate")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "issueDate" in klass.__dict__:
            descriptor = klass.__dict__["issueDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::ecvi_has_cviNumber():
    assert hasattr(ecvi::Ecvi, "cviNumber")
    descriptor = None
    for klass in ecvi::Ecvi.__mro__:
        if "cviNumber" in klass.__dict__:
            descriptor = klass.__dict__["cviNumber"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecvi::EStringToStringMapEntry)


def test_ecvi::estringtostringmapentry_constructor_exists():
    assert callable(ecvi::EStringToStringMapEntry.__init__)


def test_ecvi::estringtostringmapentry_constructor_args():
    sig = inspect.signature(ecvi::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecvi::documentroot_is_not_abstract():
    assert not inspect.isabstract(ecvi::DocumentRoot)


def test_ecvi::documentroot_constructor_exists():
    assert callable(ecvi::DocumentRoot.__init__)


def test_ecvi::documentroot_constructor_args():
    sig = inspect.signature(ecvi::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_ecvi::documentroot_has_mixed():
    assert hasattr(ecvi::DocumentRoot, "mixed")
    descriptor = None
    for klass in ecvi::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::contact_is_not_abstract():
    assert not inspect.isabstract(ecvi::Contact)


def test_ecvi::contact_constructor_exists():
    assert callable(ecvi::Contact.__init__)


def test_ecvi::contact_constructor_args():
    sig = inspect.signature(ecvi::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "premName" in params, "Missing parameter 'premName'"
    assert "premId" in params, "Missing parameter 'premId'"

def test_ecvi::contact_has_premName():
    assert hasattr(ecvi::Contact, "premName")
    descriptor = None
    for klass in ecvi::Contact.__mro__:
        if "premName" in klass.__dict__:
            descriptor = klass.__dict__["premName"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::contact_has_premId():
    assert hasattr(ecvi::Contact, "premId")
    descriptor = None
    for klass in ecvi::Contact.__mro__:
        if "premId" in klass.__dict__:
            descriptor = klass.__dict__["premId"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::person_is_not_abstract():
    assert not inspect.isabstract(ecvi::Person)


def test_ecvi::person_constructor_exists():
    assert callable(ecvi::Person.__init__)


def test_ecvi::person_constructor_args():
    sig = inspect.signature(ecvi::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecvi::person_has_name():
    assert hasattr(ecvi::Person, "name")
    descriptor = None
    for klass in ecvi::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::test_is_not_abstract():
    assert not inspect.isabstract(ecvi::Test)


def test_ecvi::test_constructor_exists():
    assert callable(ecvi::Test.__init__)


def test_ecvi::test_constructor_args():
    sig = inspect.signature(ecvi::Test.__init__)
    params = list(sig.parameters.keys())
    assert "testCode" in params, "Missing parameter 'testCode'"
    assert "idref" in params, "Missing parameter 'idref'"

def test_ecvi::test_has_testCode():
    assert hasattr(ecvi::Test, "testCode")
    descriptor = None
    for klass in ecvi::Test.__mro__:
        if "testCode" in klass.__dict__:
            descriptor = klass.__dict__["testCode"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::test_has_idref():
    assert hasattr(ecvi::Test, "idref")
    descriptor = None
    for klass in ecvi::Test.__mro__:
        if "idref" in klass.__dict__:
            descriptor = klass.__dict__["idref"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::animaltag_is_not_abstract():
    assert not inspect.isabstract(ecvi::AnimalTag)


def test_ecvi::animaltag_constructor_exists():
    assert callable(ecvi::AnimalTag.__init__)


def test_ecvi::animaltag_constructor_args():
    sig = inspect.signature(ecvi::AnimalTag.__init__)
    params = list(sig.parameters.keys())
    assert "brandImage" in params, "Missing parameter 'brandImage'"
    assert "type" in params, "Missing parameter 'type'"
    assert "number" in params, "Missing parameter 'number'"

def test_ecvi::animaltag_has_brandImage():
    assert hasattr(ecvi::AnimalTag, "brandImage")
    descriptor = None
    for klass in ecvi::AnimalTag.__mro__:
        if "brandImage" in klass.__dict__:
            descriptor = klass.__dict__["brandImage"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::animaltag_has_type():
    assert hasattr(ecvi::AnimalTag, "type")
    descriptor = None
    for klass in ecvi::AnimalTag.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::animaltag_has_number():
    assert hasattr(ecvi::AnimalTag, "number")
    descriptor = None
    for klass in ecvi::AnimalTag.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::animal_is_not_abstract():
    assert not inspect.isabstract(ecvi::Animal)


def test_ecvi::animal_constructor_exists():
    assert callable(ecvi::Animal.__init__)


def test_ecvi::animal_constructor_args():
    sig = inspect.signature(ecvi::Animal.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "inspectionDate" in params, "Missing parameter 'inspectionDate'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "sexDetail" in params, "Missing parameter 'sexDetail'"

def test_ecvi::animal_has_age():
    assert hasattr(ecvi::Animal, "age")
    descriptor = None
    for klass in ecvi::Animal.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::animal_has_inspectionDate():
    assert hasattr(ecvi::Animal, "inspectionDate")
    descriptor = None
    for klass in ecvi::Animal.__mro__:
        if "inspectionDate" in klass.__dict__:
            descriptor = klass.__dict__["inspectionDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::animal_has_sex():
    assert hasattr(ecvi::Animal, "sex")
    descriptor = None
    for klass in ecvi::Animal.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::animal_has_breed():
    assert hasattr(ecvi::Animal, "breed")
    descriptor = None
    for klass in ecvi::Animal.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::animal_has_sexDetail():
    assert hasattr(ecvi::Animal, "sexDetail")
    descriptor = None
    for klass in ecvi::Animal.__mro__:
        if "sexDetail" in klass.__dict__:
            descriptor = klass.__dict__["sexDetail"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::attachement_is_not_abstract():
    assert not inspect.isabstract(ecvi::Attachement)


def test_ecvi::attachement_constructor_exists():
    assert callable(ecvi::Attachement.__init__)


def test_ecvi::attachement_constructor_args():
    sig = inspect.signature(ecvi::Attachement.__init__)
    params = list(sig.parameters.keys())
    assert "docType" in params, "Missing parameter 'docType'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "payload" in params, "Missing parameter 'payload'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_ecvi::attachement_has_docType():
    assert hasattr(ecvi::Attachement, "docType")
    descriptor = None
    for klass in ecvi::Attachement.__mro__:
        if "docType" in klass.__dict__:
            descriptor = klass.__dict__["docType"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::attachement_has_filename():
    assert hasattr(ecvi::Attachement, "filename")
    descriptor = None
    for klass in ecvi::Attachement.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::attachement_has_payload():
    assert hasattr(ecvi::Attachement, "payload")
    descriptor = None
    for klass in ecvi::Attachement.__mro__:
        if "payload" in klass.__dict__:
            descriptor = klass.__dict__["payload"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::attachement_has_mimeType():
    assert hasattr(ecvi::Attachement, "mimeType")
    descriptor = None
    for klass in ecvi::Attachement.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::attachement_has_comment():
    assert hasattr(ecvi::Attachement, "comment")
    descriptor = None
    for klass in ecvi::Attachement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::address_is_not_abstract():
    assert not inspect.isabstract(ecvi::Address)


def test_ecvi::address_constructor_exists():
    assert callable(ecvi::Address.__init__)


def test_ecvi::address_constructor_args():
    sig = inspect.signature(ecvi::Address.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "line2" in params, "Missing parameter 'line2'"
    assert "country" in params, "Missing parameter 'country'"
    assert "county" in params, "Missing parameter 'county'"
    assert "zIP" in params, "Missing parameter 'zIP'"
    assert "town" in params, "Missing parameter 'town'"
    assert "line1" in params, "Missing parameter 'line1'"

def test_ecvi::address_has_state():
    assert hasattr(ecvi::Address, "state")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::address_has_line2():
    assert hasattr(ecvi::Address, "line2")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "line2" in klass.__dict__:
            descriptor = klass.__dict__["line2"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::address_has_country():
    assert hasattr(ecvi::Address, "country")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::address_has_county():
    assert hasattr(ecvi::Address, "county")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "county" in klass.__dict__:
            descriptor = klass.__dict__["county"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::address_has_zIP():
    assert hasattr(ecvi::Address, "zIP")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "zIP" in klass.__dict__:
            descriptor = klass.__dict__["zIP"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::address_has_town():
    assert hasattr(ecvi::Address, "town")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "town" in klass.__dict__:
            descriptor = klass.__dict__["town"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::address_has_line1():
    assert hasattr(ecvi::Address, "line1")
    descriptor = None
    for klass in ecvi::Address.__mro__:
        if "line1" in klass.__dict__:
            descriptor = klass.__dict__["line1"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::accessions_is_not_abstract():
    assert not inspect.isabstract(ecvi::Accessions)


def test_ecvi::accessions_constructor_exists():
    assert callable(ecvi::Accessions.__init__)


def test_ecvi::accessions_constructor_args():
    sig = inspect.signature(ecvi::Accessions.__init__)
    params = list(sig.parameters.keys())



def test_ecvi::geopoint_is_not_abstract():
    assert not inspect.isabstract(ecvi::GeoPoint)


def test_ecvi::geopoint_constructor_exists():
    assert callable(ecvi::GeoPoint.__init__)


def test_ecvi::geopoint_constructor_args():
    sig = inspect.signature(ecvi::GeoPoint.__init__)
    params = list(sig.parameters.keys())
    assert "lng" in params, "Missing parameter 'lng'"
    assert "lat" in params, "Missing parameter 'lat'"

def test_ecvi::geopoint_has_lng():
    assert hasattr(ecvi::GeoPoint, "lng")
    descriptor = None
    for klass in ecvi::GeoPoint.__mro__:
        if "lng" in klass.__dict__:
            descriptor = klass.__dict__["lng"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::geopoint_has_lat():
    assert hasattr(ecvi::GeoPoint, "lat")
    descriptor = None
    for klass in ecvi::GeoPoint.__mro__:
        if "lat" in klass.__dict__:
            descriptor = klass.__dict__["lat"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::laboratory_is_not_abstract():
    assert not inspect.isabstract(ecvi::Laboratory)


def test_ecvi::laboratory_constructor_exists():
    assert callable(ecvi::Laboratory.__init__)


def test_ecvi::laboratory_constructor_args():
    sig = inspect.signature(ecvi::Laboratory.__init__)
    params = list(sig.parameters.keys())
    assert "accessionNumber" in params, "Missing parameter 'accessionNumber'"
    assert "labName" in params, "Missing parameter 'labName'"
    assert "accessionDate" in params, "Missing parameter 'accessionDate'"
    assert "premId" in params, "Missing parameter 'premId'"

def test_ecvi::laboratory_has_accessionNumber():
    assert hasattr(ecvi::Laboratory, "accessionNumber")
    descriptor = None
    for klass in ecvi::Laboratory.__mro__:
        if "accessionNumber" in klass.__dict__:
            descriptor = klass.__dict__["accessionNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::laboratory_has_labName():
    assert hasattr(ecvi::Laboratory, "labName")
    descriptor = None
    for klass in ecvi::Laboratory.__mro__:
        if "labName" in klass.__dict__:
            descriptor = klass.__dict__["labName"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::laboratory_has_accessionDate():
    assert hasattr(ecvi::Laboratory, "accessionDate")
    descriptor = None
    for klass in ecvi::Laboratory.__mro__:
        if "accessionDate" in klass.__dict__:
            descriptor = klass.__dict__["accessionDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::laboratory_has_premId():
    assert hasattr(ecvi::Laboratory, "premId")
    descriptor = None
    for klass in ecvi::Laboratory.__mro__:
        if "premId" in klass.__dict__:
            descriptor = klass.__dict__["premId"]
            break
    assert isinstance(descriptor, property)



def test_ecvi::accession_is_not_abstract():
    assert not inspect.isabstract(ecvi::Accession)


def test_ecvi::accession_constructor_exists():
    assert callable(ecvi::Accession.__init__)


def test_ecvi::accession_constructor_args():
    sig = inspect.signature(ecvi::Accession.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "infieldTest" in params, "Missing parameter 'infieldTest'"

def test_ecvi::accession_has_id():
    assert hasattr(ecvi::Accession, "id")
    descriptor = None
    for klass in ecvi::Accession.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ecvi::accession_has_infieldTest():
    assert hasattr(ecvi::Accession, "infieldTest")
    descriptor = None
    for klass in ecvi::Accession.__mro__:
        if "infieldTest" in klass.__dict__:
            descriptor = klass.__dict__["infieldTest"]
            break
    assert isinstance(descriptor, property)

def test_usstate_exists():
    # Check that the Enumeration exists
    assert UsState is not None

def test_usstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsState]
    expected_literals = [
        "AL",
        "PW",
        "ND",
        "MP",
        "OR",
        "CO",
        "AE",
        "OH",
        "AP",
        "IL",
        "NC",
        "NJ",
        "PA",
        "PR",
        "ME",
        "AK",
        "GU",
        "NV",
        "AR",
        "MO",
        "MH",
        "IA",
        "DC",
        "RI",
        "LA",
        "ID",
        "TN",
        "IN",
        "FM",
        "HI",
        "MI",
        "MN",
        "OK",
        "WY",
        "WA",
        "MT",
        "AA",
        "NM",
        "AS",
        "KS",
        "NY",
        "MS",
        "WI",
        "KY",
        "AZ",
        "SD",
        "VA",
        "DE",
        "NE",
        "MD",
        "SC",
        "WV",
        "VI",
        "UT",
        "VT",
        "CT",
        "MA",
        "FL",
        "GA",
        "TX",
        "CA",
        "NH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsState"

def test_tagtype_exists():
    # Check that the Enumeration exists
    assert TagType is not None

def test_tagtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TagType]
    expected_literals = [
        "NUES9",
        "SGFLID",
        "BRAND",
        "NUES8",
        "MGT",
        "BRANDIMAGE",
        "OFORID",
        "N840RFID",
        "AMID",
        "NPIN",
        "TAT",
        "BT",
        "OTH",
        "UN",
        "IMP",
        "NAME",
        "AIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TagType"

def test_programstatusvalue_exists():
    # Check that the Enumeration exists
    assert ProgramStatusValue is not None

def test_programstatusvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramStatusValue]
    expected_literals = [
        "Other",
        "Free",
        "ModifiedAdvancedAccredited",
        "ModifiedAccredited",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramStatusValue"

def test_phonedevice_exists():
    # Check that the Enumeration exists
    assert PhoneDevice is not None

def test_phonedevice_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhoneDevice]
    expected_literals = [
        "Cellphone",
        "Fax",
        "Landline",
        "Unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhoneDevice"

def test_doctype_exists():
    # Check that the Enumeration exists
    assert DocType is not None

def test_doctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DocType]
    expected_literals = [
        "ScannedPaperCVI",
        "PDFCVI",
        "PDFTestChart",
        "Other",
        "ScannedTestChart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DocType"

def test_programstatusname_exists():
    # Check that the Enumeration exists
    assert ProgramStatusName is not None

def test_programstatusname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramStatusName]
    expected_literals = [
        "BrucellosisHerd",
        "BrucellosisState",
        "BovineTuberculosis",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramStatusName"

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "SpayedFemale",
        "NeuteredMale",
        "Male",
        "TrueHermaphrodite",
        "Other",
        "Female",
        "GenderUnknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_iso3166country_exists():
    # Check that the Enumeration exists
    assert ISO3166Country is not None

def test_iso3166country_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ISO3166Country]
    expected_literals = [
        "USA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ISO3166Country"

def test_resultname_exists():
    # Check that the Enumeration exists
    assert ResultName is not None

def test_resultname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResultName]
    expected_literals = [
        "COMMENT",
        "RESULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResultName"

def test_movementpurpose_exists():
    # Check that the Enumeration exists
    assert MovementPurpose is not None

def test_movementpurpose_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MovementPurpose]
    expected_literals = [
        "pet",
        "feeding",
        "grazing",
        "training",
        "slaughter",
        "other",
        "medicalTreatment",
        "sale",
        "breeding",
        "show",
        "race",
        "rodeo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MovementPurpose"

def test_speciescode_exists():
    # Check that the Enumeration exists
    assert SpeciesCode is not None

def test_speciescode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeciesCode]
    expected_literals = [
        "BOV",
        "UNK",
        "EQU",
        "POR",
        "CER",
        "OVI",
        "CAP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeciesCode"


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
ecvi::ResultValue_strategy = st.builds(
    ecvi::ResultValue,
    resultFloat=
        safe_text,
    resultName=
        safe_text,
    resultString=
        safe_text,
    resultInteger=
        safe_text
)
ecvi::ProgramStatus_strategy = st.builds(
    ecvi::ProgramStatus,
    name=
        safe_text,
    valueOther=
        safe_text,
    value=
        safe_text
)
ecvi::PhoneNum_strategy = st.builds(
    ecvi::PhoneNum,
    comment=
        safe_text,
    type=
        safe_text,
    number=
        safe_text
)
ecvi::GroupLot_strategy = st.builds(
    ecvi::GroupLot,
    quantity=
        safe_text,
    breed=
        safe_text,
    unit=
        safe_text,
    description=
        safe_text,
    age=
        safe_text,
    sex=
        safe_text,
    species=
        safe_text,
    sexDetail=
        safe_text
)
ecvi::Premises_strategy = st.builds(
    ecvi::Premises,
    premId=
        safe_text,
    premName=
        safe_text
)
ecvi::MovementPurposes_strategy = st.builds(
    ecvi::MovementPurposes,
    movementPurpose=
        safe_text
)
ecvi::Veterinarian_strategy = st.builds(
    ecvi::Veterinarian,
    licenseIssueState=
        safe_text,
    licenseNumber=
        safe_text,
    nationalAccreditationNumber=
        safe_text
)
ecvi::Ecvi_strategy = st.builds(
    ecvi::Ecvi,
    speciesCode=
        safe_text,
    group=
        safe_text,
    shipmentDate=
        safe_text,
    entryPermitNumber=
        safe_text,
    group1=
        safe_text,
    expirationDate=
        safe_text,
    issueDate=
        safe_text,
    cviNumber=
        safe_text
)
ecvi::EStringToStringMapEntry_strategy = st.builds(
    ecvi::EStringToStringMapEntry,
)
ecvi::DocumentRoot_strategy = st.builds(
    ecvi::DocumentRoot,
    mixed=
        safe_text
)
ecvi::Contact_strategy = st.builds(
    ecvi::Contact,
    premName=
        safe_text,
    premId=
        safe_text
)
ecvi::Person_strategy = st.builds(
    ecvi::Person,
    name=
        safe_text
)
ecvi::Test_strategy = st.builds(
    ecvi::Test,
    testCode=
        safe_text,
    idref=
        safe_text
)
ecvi::AnimalTag_strategy = st.builds(
    ecvi::AnimalTag,
    brandImage=
        safe_text,
    type=
        safe_text,
    number=
        safe_text
)
ecvi::Animal_strategy = st.builds(
    ecvi::Animal,
    age=
        safe_text,
    inspectionDate=
        safe_text,
    sex=
        safe_text,
    breed=
        safe_text,
    sexDetail=
        safe_text
)
ecvi::Attachement_strategy = st.builds(
    ecvi::Attachement,
    docType=
        safe_text,
    filename=
        safe_text,
    payload=
        safe_text,
    mimeType=
        safe_text,
    comment=
        safe_text
)
ecvi::Address_strategy = st.builds(
    ecvi::Address,
    state=
        safe_text,
    line2=
        safe_text,
    country=
        safe_text,
    county=
        safe_text,
    zIP=
        safe_text,
    town=
        safe_text,
    line1=
        safe_text
)
ecvi::Accessions_strategy = st.builds(
    ecvi::Accessions,
)
ecvi::GeoPoint_strategy = st.builds(
    ecvi::GeoPoint,
    lng=
        safe_text,
    lat=
        safe_text
)
ecvi::Laboratory_strategy = st.builds(
    ecvi::Laboratory,
    accessionNumber=
        safe_text,
    labName=
        safe_text,
    accessionDate=
        safe_text,
    premId=
        safe_text
)
ecvi::Accession_strategy = st.builds(
    ecvi::Accession,
    id=
        safe_text,
    infieldTest=
        safe_text
)

@given(instance=ecvi::ResultValue_strategy)
@settings(max_examples=50)
def test_ecvi::resultvalue_instantiation(instance):
    assert isinstance(instance, ecvi::ResultValue)

@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultFloat_type(instance):
    assert isinstance(instance.resultFloat, str)


@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultFloat_setter(instance):
    original = instance.resultFloat
    instance.resultFloat = original
    assert instance.resultFloat == original

@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultName_type(instance):
    assert isinstance(instance.resultName, str)


@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultName_setter(instance):
    original = instance.resultName
    instance.resultName = original
    assert instance.resultName == original

@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultString_type(instance):
    assert isinstance(instance.resultString, str)


@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultString_setter(instance):
    original = instance.resultString
    instance.resultString = original
    assert instance.resultString == original

@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultInteger_type(instance):
    assert isinstance(instance.resultInteger, str)


@given(instance=ecvi::ResultValue_strategy)
def test_ecvi::resultvalue_resultInteger_setter(instance):
    original = instance.resultInteger
    instance.resultInteger = original
    assert instance.resultInteger == original

@given(instance=ecvi::ProgramStatus_strategy)
@settings(max_examples=50)
def test_ecvi::programstatus_instantiation(instance):
    assert isinstance(instance, ecvi::ProgramStatus)

@given(instance=ecvi::ProgramStatus_strategy)
def test_ecvi::programstatus_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecvi::ProgramStatus_strategy)
def test_ecvi::programstatus_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecvi::ProgramStatus_strategy)
def test_ecvi::programstatus_valueOther_type(instance):
    assert isinstance(instance.valueOther, str)


@given(instance=ecvi::ProgramStatus_strategy)
def test_ecvi::programstatus_valueOther_setter(instance):
    original = instance.valueOther
    instance.valueOther = original
    assert instance.valueOther == original

@given(instance=ecvi::ProgramStatus_strategy)
def test_ecvi::programstatus_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ecvi::ProgramStatus_strategy)
def test_ecvi::programstatus_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecvi::PhoneNum_strategy)
@settings(max_examples=50)
def test_ecvi::phonenum_instantiation(instance):
    assert isinstance(instance, ecvi::PhoneNum)

@given(instance=ecvi::PhoneNum_strategy)
def test_ecvi::phonenum_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=ecvi::PhoneNum_strategy)
def test_ecvi::phonenum_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ecvi::PhoneNum_strategy)
def test_ecvi::phonenum_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ecvi::PhoneNum_strategy)
def test_ecvi::phonenum_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ecvi::PhoneNum_strategy)
def test_ecvi::phonenum_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=ecvi::PhoneNum_strategy)
def test_ecvi::phonenum_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=ecvi::GroupLot_strategy)
@settings(max_examples=50)
def test_ecvi::grouplot_instantiation(instance):
    assert isinstance(instance, ecvi::GroupLot)

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_quantity_type(instance):
    assert isinstance(instance.quantity, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_breed_type(instance):
    assert isinstance(instance.breed, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_species_type(instance):
    assert isinstance(instance.species, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original

@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_sexDetail_type(instance):
    assert isinstance(instance.sexDetail, str)


@given(instance=ecvi::GroupLot_strategy)
def test_ecvi::grouplot_sexDetail_setter(instance):
    original = instance.sexDetail
    instance.sexDetail = original
    assert instance.sexDetail == original

@given(instance=ecvi::Premises_strategy)
@settings(max_examples=50)
def test_ecvi::premises_instantiation(instance):
    assert isinstance(instance, ecvi::Premises)

@given(instance=ecvi::Premises_strategy)
def test_ecvi::premises_premId_type(instance):
    assert isinstance(instance.premId, str)


@given(instance=ecvi::Premises_strategy)
def test_ecvi::premises_premId_setter(instance):
    original = instance.premId
    instance.premId = original
    assert instance.premId == original

@given(instance=ecvi::Premises_strategy)
def test_ecvi::premises_premName_type(instance):
    assert isinstance(instance.premName, str)


@given(instance=ecvi::Premises_strategy)
def test_ecvi::premises_premName_setter(instance):
    original = instance.premName
    instance.premName = original
    assert instance.premName == original

@given(instance=ecvi::MovementPurposes_strategy)
@settings(max_examples=50)
def test_ecvi::movementpurposes_instantiation(instance):
    assert isinstance(instance, ecvi::MovementPurposes)

@given(instance=ecvi::MovementPurposes_strategy)
def test_ecvi::movementpurposes_movementPurpose_type(instance):
    assert isinstance(instance.movementPurpose, str)


@given(instance=ecvi::MovementPurposes_strategy)
def test_ecvi::movementpurposes_movementPurpose_setter(instance):
    original = instance.movementPurpose
    instance.movementPurpose = original
    assert instance.movementPurpose == original

@given(instance=ecvi::Veterinarian_strategy)
@settings(max_examples=50)
def test_ecvi::veterinarian_instantiation(instance):
    assert isinstance(instance, ecvi::Veterinarian)

@given(instance=ecvi::Veterinarian_strategy)
def test_ecvi::veterinarian_licenseIssueState_type(instance):
    assert isinstance(instance.licenseIssueState, str)


@given(instance=ecvi::Veterinarian_strategy)
def test_ecvi::veterinarian_licenseIssueState_setter(instance):
    original = instance.licenseIssueState
    instance.licenseIssueState = original
    assert instance.licenseIssueState == original

@given(instance=ecvi::Veterinarian_strategy)
def test_ecvi::veterinarian_licenseNumber_type(instance):
    assert isinstance(instance.licenseNumber, str)


@given(instance=ecvi::Veterinarian_strategy)
def test_ecvi::veterinarian_licenseNumber_setter(instance):
    original = instance.licenseNumber
    instance.licenseNumber = original
    assert instance.licenseNumber == original

@given(instance=ecvi::Veterinarian_strategy)
def test_ecvi::veterinarian_nationalAccreditationNumber_type(instance):
    assert isinstance(instance.nationalAccreditationNumber, str)


@given(instance=ecvi::Veterinarian_strategy)
def test_ecvi::veterinarian_nationalAccreditationNumber_setter(instance):
    original = instance.nationalAccreditationNumber
    instance.nationalAccreditationNumber = original
    assert instance.nationalAccreditationNumber == original

@given(instance=ecvi::Ecvi_strategy)
@settings(max_examples=50)
def test_ecvi::ecvi_instantiation(instance):
    assert isinstance(instance, ecvi::Ecvi)

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_speciesCode_type(instance):
    assert isinstance(instance.speciesCode, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_speciesCode_setter(instance):
    original = instance.speciesCode
    instance.speciesCode = original
    assert instance.speciesCode == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_shipmentDate_type(instance):
    assert isinstance(instance.shipmentDate, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_shipmentDate_setter(instance):
    original = instance.shipmentDate
    instance.shipmentDate = original
    assert instance.shipmentDate == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_entryPermitNumber_type(instance):
    assert isinstance(instance.entryPermitNumber, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_entryPermitNumber_setter(instance):
    original = instance.entryPermitNumber
    instance.entryPermitNumber = original
    assert instance.entryPermitNumber == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_expirationDate_type(instance):
    assert isinstance(instance.expirationDate, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_issueDate_type(instance):
    assert isinstance(instance.issueDate, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_issueDate_setter(instance):
    original = instance.issueDate
    instance.issueDate = original
    assert instance.issueDate == original

@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_cviNumber_type(instance):
    assert isinstance(instance.cviNumber, str)


@given(instance=ecvi::Ecvi_strategy)
def test_ecvi::ecvi_cviNumber_setter(instance):
    original = instance.cviNumber
    instance.cviNumber = original
    assert instance.cviNumber == original

@given(instance=ecvi::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecvi::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecvi::EStringToStringMapEntry)

@given(instance=ecvi::DocumentRoot_strategy)
@settings(max_examples=50)
def test_ecvi::documentroot_instantiation(instance):
    assert isinstance(instance, ecvi::DocumentRoot)

@given(instance=ecvi::DocumentRoot_strategy)
def test_ecvi::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=ecvi::DocumentRoot_strategy)
def test_ecvi::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=ecvi::Contact_strategy)
@settings(max_examples=50)
def test_ecvi::contact_instantiation(instance):
    assert isinstance(instance, ecvi::Contact)

@given(instance=ecvi::Contact_strategy)
def test_ecvi::contact_premName_type(instance):
    assert isinstance(instance.premName, str)


@given(instance=ecvi::Contact_strategy)
def test_ecvi::contact_premName_setter(instance):
    original = instance.premName
    instance.premName = original
    assert instance.premName == original

@given(instance=ecvi::Contact_strategy)
def test_ecvi::contact_premId_type(instance):
    assert isinstance(instance.premId, str)


@given(instance=ecvi::Contact_strategy)
def test_ecvi::contact_premId_setter(instance):
    original = instance.premId
    instance.premId = original
    assert instance.premId == original

@given(instance=ecvi::Person_strategy)
@settings(max_examples=50)
def test_ecvi::person_instantiation(instance):
    assert isinstance(instance, ecvi::Person)

@given(instance=ecvi::Person_strategy)
def test_ecvi::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecvi::Person_strategy)
def test_ecvi::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecvi::Test_strategy)
@settings(max_examples=50)
def test_ecvi::test_instantiation(instance):
    assert isinstance(instance, ecvi::Test)

@given(instance=ecvi::Test_strategy)
def test_ecvi::test_testCode_type(instance):
    assert isinstance(instance.testCode, str)


@given(instance=ecvi::Test_strategy)
def test_ecvi::test_testCode_setter(instance):
    original = instance.testCode
    instance.testCode = original
    assert instance.testCode == original

@given(instance=ecvi::Test_strategy)
def test_ecvi::test_idref_type(instance):
    assert isinstance(instance.idref, str)


@given(instance=ecvi::Test_strategy)
def test_ecvi::test_idref_setter(instance):
    original = instance.idref
    instance.idref = original
    assert instance.idref == original

@given(instance=ecvi::AnimalTag_strategy)
@settings(max_examples=50)
def test_ecvi::animaltag_instantiation(instance):
    assert isinstance(instance, ecvi::AnimalTag)

@given(instance=ecvi::AnimalTag_strategy)
def test_ecvi::animaltag_brandImage_type(instance):
    assert isinstance(instance.brandImage, str)


@given(instance=ecvi::AnimalTag_strategy)
def test_ecvi::animaltag_brandImage_setter(instance):
    original = instance.brandImage
    instance.brandImage = original
    assert instance.brandImage == original

@given(instance=ecvi::AnimalTag_strategy)
def test_ecvi::animaltag_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ecvi::AnimalTag_strategy)
def test_ecvi::animaltag_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ecvi::AnimalTag_strategy)
def test_ecvi::animaltag_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=ecvi::AnimalTag_strategy)
def test_ecvi::animaltag_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=ecvi::Animal_strategy)
@settings(max_examples=50)
def test_ecvi::animal_instantiation(instance):
    assert isinstance(instance, ecvi::Animal)

@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_inspectionDate_type(instance):
    assert isinstance(instance.inspectionDate, str)


@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_inspectionDate_setter(instance):
    original = instance.inspectionDate
    instance.inspectionDate = original
    assert instance.inspectionDate == original

@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_breed_type(instance):
    assert isinstance(instance.breed, str)


@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original

@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_sexDetail_type(instance):
    assert isinstance(instance.sexDetail, str)


@given(instance=ecvi::Animal_strategy)
def test_ecvi::animal_sexDetail_setter(instance):
    original = instance.sexDetail
    instance.sexDetail = original
    assert instance.sexDetail == original

@given(instance=ecvi::Attachement_strategy)
@settings(max_examples=50)
def test_ecvi::attachement_instantiation(instance):
    assert isinstance(instance, ecvi::Attachement)

@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_docType_type(instance):
    assert isinstance(instance.docType, str)


@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_docType_setter(instance):
    original = instance.docType
    instance.docType = original
    assert instance.docType == original

@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_payload_type(instance):
    assert isinstance(instance.payload, str)


@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_payload_setter(instance):
    original = instance.payload
    instance.payload = original
    assert instance.payload == original

@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_mimeType_type(instance):
    assert isinstance(instance.mimeType, str)


@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=ecvi::Attachement_strategy)
def test_ecvi::attachement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ecvi::Address_strategy)
@settings(max_examples=50)
def test_ecvi::address_instantiation(instance):
    assert isinstance(instance, ecvi::Address)

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_line2_type(instance):
    assert isinstance(instance.line2, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_line2_setter(instance):
    original = instance.line2
    instance.line2 = original
    assert instance.line2 == original

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_county_type(instance):
    assert isinstance(instance.county, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_county_setter(instance):
    original = instance.county
    instance.county = original
    assert instance.county == original

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_zIP_type(instance):
    assert isinstance(instance.zIP, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_zIP_setter(instance):
    original = instance.zIP
    instance.zIP = original
    assert instance.zIP == original

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_town_type(instance):
    assert isinstance(instance.town, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_town_setter(instance):
    original = instance.town
    instance.town = original
    assert instance.town == original

@given(instance=ecvi::Address_strategy)
def test_ecvi::address_line1_type(instance):
    assert isinstance(instance.line1, str)


@given(instance=ecvi::Address_strategy)
def test_ecvi::address_line1_setter(instance):
    original = instance.line1
    instance.line1 = original
    assert instance.line1 == original

@given(instance=ecvi::Accessions_strategy)
@settings(max_examples=50)
def test_ecvi::accessions_instantiation(instance):
    assert isinstance(instance, ecvi::Accessions)

@given(instance=ecvi::GeoPoint_strategy)
@settings(max_examples=50)
def test_ecvi::geopoint_instantiation(instance):
    assert isinstance(instance, ecvi::GeoPoint)

@given(instance=ecvi::GeoPoint_strategy)
def test_ecvi::geopoint_lng_type(instance):
    assert isinstance(instance.lng, str)


@given(instance=ecvi::GeoPoint_strategy)
def test_ecvi::geopoint_lng_setter(instance):
    original = instance.lng
    instance.lng = original
    assert instance.lng == original

@given(instance=ecvi::GeoPoint_strategy)
def test_ecvi::geopoint_lat_type(instance):
    assert isinstance(instance.lat, str)


@given(instance=ecvi::GeoPoint_strategy)
def test_ecvi::geopoint_lat_setter(instance):
    original = instance.lat
    instance.lat = original
    assert instance.lat == original

@given(instance=ecvi::Laboratory_strategy)
@settings(max_examples=50)
def test_ecvi::laboratory_instantiation(instance):
    assert isinstance(instance, ecvi::Laboratory)

@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_accessionNumber_type(instance):
    assert isinstance(instance.accessionNumber, str)


@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_accessionNumber_setter(instance):
    original = instance.accessionNumber
    instance.accessionNumber = original
    assert instance.accessionNumber == original

@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_labName_type(instance):
    assert isinstance(instance.labName, str)


@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_labName_setter(instance):
    original = instance.labName
    instance.labName = original
    assert instance.labName == original

@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_accessionDate_type(instance):
    assert isinstance(instance.accessionDate, str)


@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_accessionDate_setter(instance):
    original = instance.accessionDate
    instance.accessionDate = original
    assert instance.accessionDate == original

@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_premId_type(instance):
    assert isinstance(instance.premId, str)


@given(instance=ecvi::Laboratory_strategy)
def test_ecvi::laboratory_premId_setter(instance):
    original = instance.premId
    instance.premId = original
    assert instance.premId == original

@given(instance=ecvi::Accession_strategy)
@settings(max_examples=50)
def test_ecvi::accession_instantiation(instance):
    assert isinstance(instance, ecvi::Accession)

@given(instance=ecvi::Accession_strategy)
def test_ecvi::accession_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ecvi::Accession_strategy)
def test_ecvi::accession_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ecvi::Accession_strategy)
def test_ecvi::accession_infieldTest_type(instance):
    assert isinstance(instance.infieldTest, str)


@given(instance=ecvi::Accession_strategy)
def test_ecvi::accession_infieldTest_setter(instance):
    original = instance.infieldTest
    instance.infieldTest = original
    assert instance.infieldTest == original
