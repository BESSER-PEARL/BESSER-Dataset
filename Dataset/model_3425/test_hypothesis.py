import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ecvi_ResultValue,
    ecvi_ProgramStatus,
    ecvi_PhoneNum,
    ecvi_GroupLot,
    ecvi_Premises,
    ecvi_MovementPurposes,
    ecvi_Veterinarian,
    ecvi_Ecvi,
    ecvi_EStringToStringMapEntry,
    ecvi_DocumentRoot,
    ecvi_Contact,
    ecvi_Person,
    ecvi_Test,
    ecvi_AnimalTag,
    ecvi_Animal,
    ecvi_Attachement,
    ecvi_Address,
    ecvi_Accessions,
    ecvi_GeoPoint,
    ecvi_Laboratory,
    ecvi_Accession,
    TagType,
    ProgramStatusName,
    ResultName,
    PhoneDevice,
    MovementPurpose,
    ISO3166Country,
    UsState,
    ProgramStatusValue,
    Sex,
    SpeciesCode,
    DocType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecvi_resultvalue_is_not_abstract():
    assert not inspect.isabstract(ecvi_ResultValue)


def test_ecvi_resultvalue_constructor_exists():
    assert callable(ecvi_ResultValue.__init__)


def test_ecvi_resultvalue_constructor_args():
    sig = inspect.signature(ecvi_ResultValue.__init__)
    params = list(sig.parameters.keys())
    assert "resultString" in params, "Missing parameter 'resultString'"
    assert "resultName" in params, "Missing parameter 'resultName'"
    assert "resultInteger" in params, "Missing parameter 'resultInteger'"
    assert "resultFloat" in params, "Missing parameter 'resultFloat'"

def test_ecvi_resultvalue_has_resultString():
    assert hasattr(ecvi_ResultValue, "resultString")
    descriptor = None
    for klass in ecvi_ResultValue.__mro__:
        if "resultString" in klass.__dict__:
            descriptor = klass.__dict__["resultString"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_resultvalue_has_resultName():
    assert hasattr(ecvi_ResultValue, "resultName")
    descriptor = None
    for klass in ecvi_ResultValue.__mro__:
        if "resultName" in klass.__dict__:
            descriptor = klass.__dict__["resultName"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_resultvalue_has_resultInteger():
    assert hasattr(ecvi_ResultValue, "resultInteger")
    descriptor = None
    for klass in ecvi_ResultValue.__mro__:
        if "resultInteger" in klass.__dict__:
            descriptor = klass.__dict__["resultInteger"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_resultvalue_has_resultFloat():
    assert hasattr(ecvi_ResultValue, "resultFloat")
    descriptor = None
    for klass in ecvi_ResultValue.__mro__:
        if "resultFloat" in klass.__dict__:
            descriptor = klass.__dict__["resultFloat"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_programstatus_is_not_abstract():
    assert not inspect.isabstract(ecvi_ProgramStatus)


def test_ecvi_programstatus_constructor_exists():
    assert callable(ecvi_ProgramStatus.__init__)


def test_ecvi_programstatus_constructor_args():
    sig = inspect.signature(ecvi_ProgramStatus.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "valueOther" in params, "Missing parameter 'valueOther'"

def test_ecvi_programstatus_has_value():
    assert hasattr(ecvi_ProgramStatus, "value")
    descriptor = None
    for klass in ecvi_ProgramStatus.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_programstatus_has_name():
    assert hasattr(ecvi_ProgramStatus, "name")
    descriptor = None
    for klass in ecvi_ProgramStatus.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_programstatus_has_valueOther():
    assert hasattr(ecvi_ProgramStatus, "valueOther")
    descriptor = None
    for klass in ecvi_ProgramStatus.__mro__:
        if "valueOther" in klass.__dict__:
            descriptor = klass.__dict__["valueOther"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_phonenum_is_not_abstract():
    assert not inspect.isabstract(ecvi_PhoneNum)


def test_ecvi_phonenum_constructor_exists():
    assert callable(ecvi_PhoneNum.__init__)


def test_ecvi_phonenum_constructor_args():
    sig = inspect.signature(ecvi_PhoneNum.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "number" in params, "Missing parameter 'number'"

def test_ecvi_phonenum_has_type():
    assert hasattr(ecvi_PhoneNum, "type")
    descriptor = None
    for klass in ecvi_PhoneNum.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_phonenum_has_comment():
    assert hasattr(ecvi_PhoneNum, "comment")
    descriptor = None
    for klass in ecvi_PhoneNum.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_phonenum_has_number():
    assert hasattr(ecvi_PhoneNum, "number")
    descriptor = None
    for klass in ecvi_PhoneNum.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_grouplot_is_not_abstract():
    assert not inspect.isabstract(ecvi_GroupLot)


def test_ecvi_grouplot_constructor_exists():
    assert callable(ecvi_GroupLot.__init__)


def test_ecvi_grouplot_constructor_args():
    sig = inspect.signature(ecvi_GroupLot.__init__)
    params = list(sig.parameters.keys())
    assert "species" in params, "Missing parameter 'species'"
    assert "description" in params, "Missing parameter 'description'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "age" in params, "Missing parameter 'age'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "sexDetail" in params, "Missing parameter 'sexDetail'"
    assert "breed" in params, "Missing parameter 'breed'"

def test_ecvi_grouplot_has_species():
    assert hasattr(ecvi_GroupLot, "species")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "species" in klass.__dict__:
            descriptor = klass.__dict__["species"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_description():
    assert hasattr(ecvi_GroupLot, "description")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_quantity():
    assert hasattr(ecvi_GroupLot, "quantity")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_sex():
    assert hasattr(ecvi_GroupLot, "sex")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_age():
    assert hasattr(ecvi_GroupLot, "age")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_unit():
    assert hasattr(ecvi_GroupLot, "unit")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_sexDetail():
    assert hasattr(ecvi_GroupLot, "sexDetail")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "sexDetail" in klass.__dict__:
            descriptor = klass.__dict__["sexDetail"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_grouplot_has_breed():
    assert hasattr(ecvi_GroupLot, "breed")
    descriptor = None
    for klass in ecvi_GroupLot.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_premises_is_not_abstract():
    assert not inspect.isabstract(ecvi_Premises)


def test_ecvi_premises_constructor_exists():
    assert callable(ecvi_Premises.__init__)


def test_ecvi_premises_constructor_args():
    sig = inspect.signature(ecvi_Premises.__init__)
    params = list(sig.parameters.keys())
    assert "premName" in params, "Missing parameter 'premName'"
    assert "premId" in params, "Missing parameter 'premId'"

def test_ecvi_premises_has_premName():
    assert hasattr(ecvi_Premises, "premName")
    descriptor = None
    for klass in ecvi_Premises.__mro__:
        if "premName" in klass.__dict__:
            descriptor = klass.__dict__["premName"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_premises_has_premId():
    assert hasattr(ecvi_Premises, "premId")
    descriptor = None
    for klass in ecvi_Premises.__mro__:
        if "premId" in klass.__dict__:
            descriptor = klass.__dict__["premId"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_movementpurposes_is_not_abstract():
    assert not inspect.isabstract(ecvi_MovementPurposes)


def test_ecvi_movementpurposes_constructor_exists():
    assert callable(ecvi_MovementPurposes.__init__)


def test_ecvi_movementpurposes_constructor_args():
    sig = inspect.signature(ecvi_MovementPurposes.__init__)
    params = list(sig.parameters.keys())
    assert "movementPurpose" in params, "Missing parameter 'movementPurpose'"

def test_ecvi_movementpurposes_has_movementPurpose():
    assert hasattr(ecvi_MovementPurposes, "movementPurpose")
    descriptor = None
    for klass in ecvi_MovementPurposes.__mro__:
        if "movementPurpose" in klass.__dict__:
            descriptor = klass.__dict__["movementPurpose"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_veterinarian_is_not_abstract():
    assert not inspect.isabstract(ecvi_Veterinarian)


def test_ecvi_veterinarian_constructor_exists():
    assert callable(ecvi_Veterinarian.__init__)


def test_ecvi_veterinarian_constructor_args():
    sig = inspect.signature(ecvi_Veterinarian.__init__)
    params = list(sig.parameters.keys())
    assert "licenseNumber" in params, "Missing parameter 'licenseNumber'"
    assert "nationalAccreditationNumber" in params, "Missing parameter 'nationalAccreditationNumber'"
    assert "licenseIssueState" in params, "Missing parameter 'licenseIssueState'"

def test_ecvi_veterinarian_has_licenseNumber():
    assert hasattr(ecvi_Veterinarian, "licenseNumber")
    descriptor = None
    for klass in ecvi_Veterinarian.__mro__:
        if "licenseNumber" in klass.__dict__:
            descriptor = klass.__dict__["licenseNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_veterinarian_has_nationalAccreditationNumber():
    assert hasattr(ecvi_Veterinarian, "nationalAccreditationNumber")
    descriptor = None
    for klass in ecvi_Veterinarian.__mro__:
        if "nationalAccreditationNumber" in klass.__dict__:
            descriptor = klass.__dict__["nationalAccreditationNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_veterinarian_has_licenseIssueState():
    assert hasattr(ecvi_Veterinarian, "licenseIssueState")
    descriptor = None
    for klass in ecvi_Veterinarian.__mro__:
        if "licenseIssueState" in klass.__dict__:
            descriptor = klass.__dict__["licenseIssueState"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_ecvi_is_not_abstract():
    assert not inspect.isabstract(ecvi_Ecvi)


def test_ecvi_ecvi_constructor_exists():
    assert callable(ecvi_Ecvi.__init__)


def test_ecvi_ecvi_constructor_args():
    sig = inspect.signature(ecvi_Ecvi.__init__)
    params = list(sig.parameters.keys())
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"
    assert "cviNumber" in params, "Missing parameter 'cviNumber'"
    assert "group" in params, "Missing parameter 'group'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "shipmentDate" in params, "Missing parameter 'shipmentDate'"
    assert "issueDate" in params, "Missing parameter 'issueDate'"
    assert "entryPermitNumber" in params, "Missing parameter 'entryPermitNumber'"
    assert "speciesCode" in params, "Missing parameter 'speciesCode'"

def test_ecvi_ecvi_has_expirationDate():
    assert hasattr(ecvi_Ecvi, "expirationDate")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "expirationDate" in klass.__dict__:
            descriptor = klass.__dict__["expirationDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_cviNumber():
    assert hasattr(ecvi_Ecvi, "cviNumber")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "cviNumber" in klass.__dict__:
            descriptor = klass.__dict__["cviNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_group():
    assert hasattr(ecvi_Ecvi, "group")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_group1():
    assert hasattr(ecvi_Ecvi, "group1")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_shipmentDate():
    assert hasattr(ecvi_Ecvi, "shipmentDate")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "shipmentDate" in klass.__dict__:
            descriptor = klass.__dict__["shipmentDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_issueDate():
    assert hasattr(ecvi_Ecvi, "issueDate")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "issueDate" in klass.__dict__:
            descriptor = klass.__dict__["issueDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_entryPermitNumber():
    assert hasattr(ecvi_Ecvi, "entryPermitNumber")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "entryPermitNumber" in klass.__dict__:
            descriptor = klass.__dict__["entryPermitNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_ecvi_has_speciesCode():
    assert hasattr(ecvi_Ecvi, "speciesCode")
    descriptor = None
    for klass in ecvi_Ecvi.__mro__:
        if "speciesCode" in klass.__dict__:
            descriptor = klass.__dict__["speciesCode"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecvi_EStringToStringMapEntry)


def test_ecvi_estringtostringmapentry_constructor_exists():
    assert callable(ecvi_EStringToStringMapEntry.__init__)


def test_ecvi_estringtostringmapentry_constructor_args():
    sig = inspect.signature(ecvi_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ecvi_documentroot_is_not_abstract():
    assert not inspect.isabstract(ecvi_DocumentRoot)


def test_ecvi_documentroot_constructor_exists():
    assert callable(ecvi_DocumentRoot.__init__)


def test_ecvi_documentroot_constructor_args():
    sig = inspect.signature(ecvi_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_ecvi_documentroot_has_mixed():
    assert hasattr(ecvi_DocumentRoot, "mixed")
    descriptor = None
    for klass in ecvi_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_contact_is_not_abstract():
    assert not inspect.isabstract(ecvi_Contact)


def test_ecvi_contact_constructor_exists():
    assert callable(ecvi_Contact.__init__)


def test_ecvi_contact_constructor_args():
    sig = inspect.signature(ecvi_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "premId" in params, "Missing parameter 'premId'"
    assert "premName" in params, "Missing parameter 'premName'"

def test_ecvi_contact_has_premId():
    assert hasattr(ecvi_Contact, "premId")
    descriptor = None
    for klass in ecvi_Contact.__mro__:
        if "premId" in klass.__dict__:
            descriptor = klass.__dict__["premId"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_contact_has_premName():
    assert hasattr(ecvi_Contact, "premName")
    descriptor = None
    for klass in ecvi_Contact.__mro__:
        if "premName" in klass.__dict__:
            descriptor = klass.__dict__["premName"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_person_is_not_abstract():
    assert not inspect.isabstract(ecvi_Person)


def test_ecvi_person_constructor_exists():
    assert callable(ecvi_Person.__init__)


def test_ecvi_person_constructor_args():
    sig = inspect.signature(ecvi_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecvi_person_has_name():
    assert hasattr(ecvi_Person, "name")
    descriptor = None
    for klass in ecvi_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_test_is_not_abstract():
    assert not inspect.isabstract(ecvi_Test)


def test_ecvi_test_constructor_exists():
    assert callable(ecvi_Test.__init__)


def test_ecvi_test_constructor_args():
    sig = inspect.signature(ecvi_Test.__init__)
    params = list(sig.parameters.keys())
    assert "idref" in params, "Missing parameter 'idref'"
    assert "testCode" in params, "Missing parameter 'testCode'"

def test_ecvi_test_has_idref():
    assert hasattr(ecvi_Test, "idref")
    descriptor = None
    for klass in ecvi_Test.__mro__:
        if "idref" in klass.__dict__:
            descriptor = klass.__dict__["idref"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_test_has_testCode():
    assert hasattr(ecvi_Test, "testCode")
    descriptor = None
    for klass in ecvi_Test.__mro__:
        if "testCode" in klass.__dict__:
            descriptor = klass.__dict__["testCode"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_animaltag_is_not_abstract():
    assert not inspect.isabstract(ecvi_AnimalTag)


def test_ecvi_animaltag_constructor_exists():
    assert callable(ecvi_AnimalTag.__init__)


def test_ecvi_animaltag_constructor_args():
    sig = inspect.signature(ecvi_AnimalTag.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "brandImage" in params, "Missing parameter 'brandImage'"
    assert "type" in params, "Missing parameter 'type'"

def test_ecvi_animaltag_has_number():
    assert hasattr(ecvi_AnimalTag, "number")
    descriptor = None
    for klass in ecvi_AnimalTag.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_animaltag_has_brandImage():
    assert hasattr(ecvi_AnimalTag, "brandImage")
    descriptor = None
    for klass in ecvi_AnimalTag.__mro__:
        if "brandImage" in klass.__dict__:
            descriptor = klass.__dict__["brandImage"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_animaltag_has_type():
    assert hasattr(ecvi_AnimalTag, "type")
    descriptor = None
    for klass in ecvi_AnimalTag.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_animal_is_not_abstract():
    assert not inspect.isabstract(ecvi_Animal)


def test_ecvi_animal_constructor_exists():
    assert callable(ecvi_Animal.__init__)


def test_ecvi_animal_constructor_args():
    sig = inspect.signature(ecvi_Animal.__init__)
    params = list(sig.parameters.keys())
    assert "inspectionDate" in params, "Missing parameter 'inspectionDate'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "sexDetail" in params, "Missing parameter 'sexDetail'"
    assert "age" in params, "Missing parameter 'age'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_ecvi_animal_has_inspectionDate():
    assert hasattr(ecvi_Animal, "inspectionDate")
    descriptor = None
    for klass in ecvi_Animal.__mro__:
        if "inspectionDate" in klass.__dict__:
            descriptor = klass.__dict__["inspectionDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_animal_has_breed():
    assert hasattr(ecvi_Animal, "breed")
    descriptor = None
    for klass in ecvi_Animal.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_animal_has_sexDetail():
    assert hasattr(ecvi_Animal, "sexDetail")
    descriptor = None
    for klass in ecvi_Animal.__mro__:
        if "sexDetail" in klass.__dict__:
            descriptor = klass.__dict__["sexDetail"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_animal_has_age():
    assert hasattr(ecvi_Animal, "age")
    descriptor = None
    for klass in ecvi_Animal.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_animal_has_sex():
    assert hasattr(ecvi_Animal, "sex")
    descriptor = None
    for klass in ecvi_Animal.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_attachement_is_not_abstract():
    assert not inspect.isabstract(ecvi_Attachement)


def test_ecvi_attachement_constructor_exists():
    assert callable(ecvi_Attachement.__init__)


def test_ecvi_attachement_constructor_args():
    sig = inspect.signature(ecvi_Attachement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "payload" in params, "Missing parameter 'payload'"
    assert "docType" in params, "Missing parameter 'docType'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"

def test_ecvi_attachement_has_comment():
    assert hasattr(ecvi_Attachement, "comment")
    descriptor = None
    for klass in ecvi_Attachement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_attachement_has_filename():
    assert hasattr(ecvi_Attachement, "filename")
    descriptor = None
    for klass in ecvi_Attachement.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_attachement_has_payload():
    assert hasattr(ecvi_Attachement, "payload")
    descriptor = None
    for klass in ecvi_Attachement.__mro__:
        if "payload" in klass.__dict__:
            descriptor = klass.__dict__["payload"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_attachement_has_docType():
    assert hasattr(ecvi_Attachement, "docType")
    descriptor = None
    for klass in ecvi_Attachement.__mro__:
        if "docType" in klass.__dict__:
            descriptor = klass.__dict__["docType"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_attachement_has_mimeType():
    assert hasattr(ecvi_Attachement, "mimeType")
    descriptor = None
    for klass in ecvi_Attachement.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_address_is_not_abstract():
    assert not inspect.isabstract(ecvi_Address)


def test_ecvi_address_constructor_exists():
    assert callable(ecvi_Address.__init__)


def test_ecvi_address_constructor_args():
    sig = inspect.signature(ecvi_Address.__init__)
    params = list(sig.parameters.keys())
    assert "line1" in params, "Missing parameter 'line1'"
    assert "zIP" in params, "Missing parameter 'zIP'"
    assert "town" in params, "Missing parameter 'town'"
    assert "line2" in params, "Missing parameter 'line2'"
    assert "state" in params, "Missing parameter 'state'"
    assert "county" in params, "Missing parameter 'county'"
    assert "country" in params, "Missing parameter 'country'"

def test_ecvi_address_has_line1():
    assert hasattr(ecvi_Address, "line1")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "line1" in klass.__dict__:
            descriptor = klass.__dict__["line1"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_address_has_zIP():
    assert hasattr(ecvi_Address, "zIP")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "zIP" in klass.__dict__:
            descriptor = klass.__dict__["zIP"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_address_has_town():
    assert hasattr(ecvi_Address, "town")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "town" in klass.__dict__:
            descriptor = klass.__dict__["town"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_address_has_line2():
    assert hasattr(ecvi_Address, "line2")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "line2" in klass.__dict__:
            descriptor = klass.__dict__["line2"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_address_has_state():
    assert hasattr(ecvi_Address, "state")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_address_has_county():
    assert hasattr(ecvi_Address, "county")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "county" in klass.__dict__:
            descriptor = klass.__dict__["county"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_address_has_country():
    assert hasattr(ecvi_Address, "country")
    descriptor = None
    for klass in ecvi_Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_accessions_is_not_abstract():
    assert not inspect.isabstract(ecvi_Accessions)


def test_ecvi_accessions_constructor_exists():
    assert callable(ecvi_Accessions.__init__)


def test_ecvi_accessions_constructor_args():
    sig = inspect.signature(ecvi_Accessions.__init__)
    params = list(sig.parameters.keys())



def test_ecvi_geopoint_is_not_abstract():
    assert not inspect.isabstract(ecvi_GeoPoint)


def test_ecvi_geopoint_constructor_exists():
    assert callable(ecvi_GeoPoint.__init__)


def test_ecvi_geopoint_constructor_args():
    sig = inspect.signature(ecvi_GeoPoint.__init__)
    params = list(sig.parameters.keys())
    assert "lng" in params, "Missing parameter 'lng'"
    assert "lat" in params, "Missing parameter 'lat'"

def test_ecvi_geopoint_has_lng():
    assert hasattr(ecvi_GeoPoint, "lng")
    descriptor = None
    for klass in ecvi_GeoPoint.__mro__:
        if "lng" in klass.__dict__:
            descriptor = klass.__dict__["lng"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_geopoint_has_lat():
    assert hasattr(ecvi_GeoPoint, "lat")
    descriptor = None
    for klass in ecvi_GeoPoint.__mro__:
        if "lat" in klass.__dict__:
            descriptor = klass.__dict__["lat"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_laboratory_is_not_abstract():
    assert not inspect.isabstract(ecvi_Laboratory)


def test_ecvi_laboratory_constructor_exists():
    assert callable(ecvi_Laboratory.__init__)


def test_ecvi_laboratory_constructor_args():
    sig = inspect.signature(ecvi_Laboratory.__init__)
    params = list(sig.parameters.keys())
    assert "premId" in params, "Missing parameter 'premId'"
    assert "accessionNumber" in params, "Missing parameter 'accessionNumber'"
    assert "accessionDate" in params, "Missing parameter 'accessionDate'"
    assert "labName" in params, "Missing parameter 'labName'"

def test_ecvi_laboratory_has_premId():
    assert hasattr(ecvi_Laboratory, "premId")
    descriptor = None
    for klass in ecvi_Laboratory.__mro__:
        if "premId" in klass.__dict__:
            descriptor = klass.__dict__["premId"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_laboratory_has_accessionNumber():
    assert hasattr(ecvi_Laboratory, "accessionNumber")
    descriptor = None
    for klass in ecvi_Laboratory.__mro__:
        if "accessionNumber" in klass.__dict__:
            descriptor = klass.__dict__["accessionNumber"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_laboratory_has_accessionDate():
    assert hasattr(ecvi_Laboratory, "accessionDate")
    descriptor = None
    for klass in ecvi_Laboratory.__mro__:
        if "accessionDate" in klass.__dict__:
            descriptor = klass.__dict__["accessionDate"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_laboratory_has_labName():
    assert hasattr(ecvi_Laboratory, "labName")
    descriptor = None
    for klass in ecvi_Laboratory.__mro__:
        if "labName" in klass.__dict__:
            descriptor = klass.__dict__["labName"]
            break
    assert isinstance(descriptor, property)



def test_ecvi_accession_is_not_abstract():
    assert not inspect.isabstract(ecvi_Accession)


def test_ecvi_accession_constructor_exists():
    assert callable(ecvi_Accession.__init__)


def test_ecvi_accession_constructor_args():
    sig = inspect.signature(ecvi_Accession.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "infieldTest" in params, "Missing parameter 'infieldTest'"

def test_ecvi_accession_has_id():
    assert hasattr(ecvi_Accession, "id")
    descriptor = None
    for klass in ecvi_Accession.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ecvi_accession_has_infieldTest():
    assert hasattr(ecvi_Accession, "infieldTest")
    descriptor = None
    for klass in ecvi_Accession.__mro__:
        if "infieldTest" in klass.__dict__:
            descriptor = klass.__dict__["infieldTest"]
            break
    assert isinstance(descriptor, property)

def test_tagtype_exists():
    # Check that the Enumeration exists
    assert TagType is not None

def test_tagtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TagType]
    expected_literals = [
        "UN",
        "MGT",
        "BRAND",
        "NUES8",
        "NAME",
        "NPIN",
        "SGFLID",
        "IMP",
        "BRANDIMAGE",
        "NUES9",
        "OFORID",
        "TAT",
        "AIN",
        "BT",
        "N840RFID",
        "AMID",
        "OTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TagType"

def test_programstatusname_exists():
    # Check that the Enumeration exists
    assert ProgramStatusName is not None

def test_programstatusname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramStatusName]
    expected_literals = [
        "BrucellosisState",
        "BrucellosisHerd",
        "BovineTuberculosis",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramStatusName"

def test_resultname_exists():
    # Check that the Enumeration exists
    assert ResultName is not None

def test_resultname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResultName]
    expected_literals = [
        "RESULT",
        "COMMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResultName"

def test_phonedevice_exists():
    # Check that the Enumeration exists
    assert PhoneDevice is not None

def test_phonedevice_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhoneDevice]
    expected_literals = [
        "Fax",
        "Cellphone",
        "Landline",
        "Unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhoneDevice"

def test_movementpurpose_exists():
    # Check that the Enumeration exists
    assert MovementPurpose is not None

def test_movementpurpose_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MovementPurpose]
    expected_literals = [
        "training",
        "slaughter",
        "show",
        "breeding",
        "rodeo",
        "grazing",
        "pet",
        "other",
        "sale",
        "race",
        "medicalTreatment",
        "feeding",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MovementPurpose"

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

def test_usstate_exists():
    # Check that the Enumeration exists
    assert UsState is not None

def test_usstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsState]
    expected_literals = [
        "ME",
        "CT",
        "NJ",
        "NM",
        "SD",
        "NV",
        "PA",
        "AR",
        "IL",
        "NE",
        "MT",
        "PR",
        "OK",
        "IA",
        "ID",
        "OR",
        "DE",
        "WI",
        "OH",
        "FL",
        "MA",
        "TX",
        "SC",
        "GU",
        "IN",
        "MP",
        "PW",
        "RI",
        "AA",
        "MH",
        "AS",
        "AK",
        "WV",
        "AZ",
        "NH",
        "AP",
        "AL",
        "MI",
        "VI",
        "NC",
        "FM",
        "MD",
        "MN",
        "CO",
        "NY",
        "HI",
        "MS",
        "WA",
        "ND",
        "DC",
        "KS",
        "UT",
        "TN",
        "MO",
        "CA",
        "VT",
        "AE",
        "VA",
        "GA",
        "WY",
        "KY",
        "LA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsState"

def test_programstatusvalue_exists():
    # Check that the Enumeration exists
    assert ProgramStatusValue is not None

def test_programstatusvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramStatusValue]
    expected_literals = [
        "Free",
        "Other",
        "ModifiedAccredited",
        "ModifiedAdvancedAccredited",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramStatusValue"

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "GenderUnknown",
        "Other",
        "Female",
        "Male",
        "TrueHermaphrodite",
        "SpayedFemale",
        "NeuteredMale",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_speciescode_exists():
    # Check that the Enumeration exists
    assert SpeciesCode is not None

def test_speciescode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeciesCode]
    expected_literals = [
        "BOV",
        "OVI",
        "UNK",
        "EQU",
        "POR",
        "CAP",
        "CER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeciesCode"

def test_doctype_exists():
    # Check that the Enumeration exists
    assert DocType is not None

def test_doctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DocType]
    expected_literals = [
        "Other",
        "ScannedTestChart",
        "PDFCVI",
        "ScannedPaperCVI",
        "PDFTestChart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DocType"


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
ecvi_ResultValue_strategy = st.builds(
    ecvi_ResultValue,
    resultString=
        safe_text,
    resultName=
        safe_text,
    resultInteger=
        safe_text,
    resultFloat=
        safe_text
)
ecvi_ProgramStatus_strategy = st.builds(
    ecvi_ProgramStatus,
    value=
        safe_text,
    name=
        safe_text,
    valueOther=
        safe_text
)
ecvi_PhoneNum_strategy = st.builds(
    ecvi_PhoneNum,
    type=
        safe_text,
    comment=
        safe_text,
    number=
        safe_text
)
ecvi_GroupLot_strategy = st.builds(
    ecvi_GroupLot,
    species=
        safe_text,
    description=
        safe_text,
    quantity=
        safe_text,
    sex=
        safe_text,
    age=
        safe_text,
    unit=
        safe_text,
    sexDetail=
        safe_text,
    breed=
        safe_text
)
ecvi_Premises_strategy = st.builds(
    ecvi_Premises,
    premName=
        safe_text,
    premId=
        safe_text
)
ecvi_MovementPurposes_strategy = st.builds(
    ecvi_MovementPurposes,
    movementPurpose=
        safe_text
)
ecvi_Veterinarian_strategy = st.builds(
    ecvi_Veterinarian,
    licenseNumber=
        safe_text,
    nationalAccreditationNumber=
        safe_text,
    licenseIssueState=
        safe_text
)
ecvi_Ecvi_strategy = st.builds(
    ecvi_Ecvi,
    expirationDate=
        safe_text,
    cviNumber=
        safe_text,
    group=
        safe_text,
    group1=
        safe_text,
    shipmentDate=
        safe_text,
    issueDate=
        safe_text,
    entryPermitNumber=
        safe_text,
    speciesCode=
        safe_text
)
ecvi_EStringToStringMapEntry_strategy = st.builds(
    ecvi_EStringToStringMapEntry,
)
ecvi_DocumentRoot_strategy = st.builds(
    ecvi_DocumentRoot,
    mixed=
        safe_text
)
ecvi_Contact_strategy = st.builds(
    ecvi_Contact,
    premId=
        safe_text,
    premName=
        safe_text
)
ecvi_Person_strategy = st.builds(
    ecvi_Person,
    name=
        safe_text
)
ecvi_Test_strategy = st.builds(
    ecvi_Test,
    idref=
        safe_text,
    testCode=
        safe_text
)
ecvi_AnimalTag_strategy = st.builds(
    ecvi_AnimalTag,
    number=
        safe_text,
    brandImage=
        safe_text,
    type=
        safe_text
)
ecvi_Animal_strategy = st.builds(
    ecvi_Animal,
    inspectionDate=
        safe_text,
    breed=
        safe_text,
    sexDetail=
        safe_text,
    age=
        safe_text,
    sex=
        safe_text
)
ecvi_Attachement_strategy = st.builds(
    ecvi_Attachement,
    comment=
        safe_text,
    filename=
        safe_text,
    payload=
        safe_text,
    docType=
        safe_text,
    mimeType=
        safe_text
)
ecvi_Address_strategy = st.builds(
    ecvi_Address,
    line1=
        safe_text,
    zIP=
        safe_text,
    town=
        safe_text,
    line2=
        safe_text,
    state=
        safe_text,
    county=
        safe_text,
    country=
        safe_text
)
ecvi_Accessions_strategy = st.builds(
    ecvi_Accessions,
)
ecvi_GeoPoint_strategy = st.builds(
    ecvi_GeoPoint,
    lng=
        safe_text,
    lat=
        safe_text
)
ecvi_Laboratory_strategy = st.builds(
    ecvi_Laboratory,
    premId=
        safe_text,
    accessionNumber=
        safe_text,
    accessionDate=
        safe_text,
    labName=
        safe_text
)
ecvi_Accession_strategy = st.builds(
    ecvi_Accession,
    id=
        safe_text,
    infieldTest=
        safe_text
)

@given(instance=ecvi_ResultValue_strategy)
@settings(max_examples=50)
def test_ecvi_resultvalue_instantiation(instance):
    assert isinstance(instance, ecvi_ResultValue)



@given(instance=ecvi_ResultValue_strategy)
def test_ecvi_resultvalue_resultString_setter(instance):
    original = instance.resultString
    instance.resultString = original
    assert instance.resultString == original



@given(instance=ecvi_ResultValue_strategy)
def test_ecvi_resultvalue_resultName_setter(instance):
    original = instance.resultName
    instance.resultName = original
    assert instance.resultName == original



@given(instance=ecvi_ResultValue_strategy)
def test_ecvi_resultvalue_resultInteger_setter(instance):
    original = instance.resultInteger
    instance.resultInteger = original
    assert instance.resultInteger == original



@given(instance=ecvi_ResultValue_strategy)
def test_ecvi_resultvalue_resultFloat_setter(instance):
    original = instance.resultFloat
    instance.resultFloat = original
    assert instance.resultFloat == original

@given(instance=ecvi_ProgramStatus_strategy)
@settings(max_examples=50)
def test_ecvi_programstatus_instantiation(instance):
    assert isinstance(instance, ecvi_ProgramStatus)



@given(instance=ecvi_ProgramStatus_strategy)
def test_ecvi_programstatus_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ecvi_ProgramStatus_strategy)
def test_ecvi_programstatus_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ecvi_ProgramStatus_strategy)
def test_ecvi_programstatus_valueOther_setter(instance):
    original = instance.valueOther
    instance.valueOther = original
    assert instance.valueOther == original

@given(instance=ecvi_PhoneNum_strategy)
@settings(max_examples=50)
def test_ecvi_phonenum_instantiation(instance):
    assert isinstance(instance, ecvi_PhoneNum)



@given(instance=ecvi_PhoneNum_strategy)
def test_ecvi_phonenum_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ecvi_PhoneNum_strategy)
def test_ecvi_phonenum_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=ecvi_PhoneNum_strategy)
def test_ecvi_phonenum_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=ecvi_GroupLot_strategy)
@settings(max_examples=50)
def test_ecvi_grouplot_instantiation(instance):
    assert isinstance(instance, ecvi_GroupLot)



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_sexDetail_setter(instance):
    original = instance.sexDetail
    instance.sexDetail = original
    assert instance.sexDetail == original



@given(instance=ecvi_GroupLot_strategy)
def test_ecvi_grouplot_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original

@given(instance=ecvi_Premises_strategy)
@settings(max_examples=50)
def test_ecvi_premises_instantiation(instance):
    assert isinstance(instance, ecvi_Premises)



@given(instance=ecvi_Premises_strategy)
def test_ecvi_premises_premName_setter(instance):
    original = instance.premName
    instance.premName = original
    assert instance.premName == original



@given(instance=ecvi_Premises_strategy)
def test_ecvi_premises_premId_setter(instance):
    original = instance.premId
    instance.premId = original
    assert instance.premId == original

@given(instance=ecvi_MovementPurposes_strategy)
@settings(max_examples=50)
def test_ecvi_movementpurposes_instantiation(instance):
    assert isinstance(instance, ecvi_MovementPurposes)



@given(instance=ecvi_MovementPurposes_strategy)
def test_ecvi_movementpurposes_movementPurpose_setter(instance):
    original = instance.movementPurpose
    instance.movementPurpose = original
    assert instance.movementPurpose == original

@given(instance=ecvi_Veterinarian_strategy)
@settings(max_examples=50)
def test_ecvi_veterinarian_instantiation(instance):
    assert isinstance(instance, ecvi_Veterinarian)



@given(instance=ecvi_Veterinarian_strategy)
def test_ecvi_veterinarian_licenseNumber_setter(instance):
    original = instance.licenseNumber
    instance.licenseNumber = original
    assert instance.licenseNumber == original



@given(instance=ecvi_Veterinarian_strategy)
def test_ecvi_veterinarian_nationalAccreditationNumber_setter(instance):
    original = instance.nationalAccreditationNumber
    instance.nationalAccreditationNumber = original
    assert instance.nationalAccreditationNumber == original



@given(instance=ecvi_Veterinarian_strategy)
def test_ecvi_veterinarian_licenseIssueState_setter(instance):
    original = instance.licenseIssueState
    instance.licenseIssueState = original
    assert instance.licenseIssueState == original

@given(instance=ecvi_Ecvi_strategy)
@settings(max_examples=50)
def test_ecvi_ecvi_instantiation(instance):
    assert isinstance(instance, ecvi_Ecvi)



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_cviNumber_setter(instance):
    original = instance.cviNumber
    instance.cviNumber = original
    assert instance.cviNumber == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_shipmentDate_setter(instance):
    original = instance.shipmentDate
    instance.shipmentDate = original
    assert instance.shipmentDate == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_issueDate_setter(instance):
    original = instance.issueDate
    instance.issueDate = original
    assert instance.issueDate == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_entryPermitNumber_setter(instance):
    original = instance.entryPermitNumber
    instance.entryPermitNumber = original
    assert instance.entryPermitNumber == original



@given(instance=ecvi_Ecvi_strategy)
def test_ecvi_ecvi_speciesCode_setter(instance):
    original = instance.speciesCode
    instance.speciesCode = original
    assert instance.speciesCode == original

@given(instance=ecvi_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ecvi_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ecvi_EStringToStringMapEntry)

@given(instance=ecvi_DocumentRoot_strategy)
@settings(max_examples=50)
def test_ecvi_documentroot_instantiation(instance):
    assert isinstance(instance, ecvi_DocumentRoot)



@given(instance=ecvi_DocumentRoot_strategy)
def test_ecvi_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=ecvi_Contact_strategy)
@settings(max_examples=50)
def test_ecvi_contact_instantiation(instance):
    assert isinstance(instance, ecvi_Contact)



@given(instance=ecvi_Contact_strategy)
def test_ecvi_contact_premId_setter(instance):
    original = instance.premId
    instance.premId = original
    assert instance.premId == original



@given(instance=ecvi_Contact_strategy)
def test_ecvi_contact_premName_setter(instance):
    original = instance.premName
    instance.premName = original
    assert instance.premName == original

@given(instance=ecvi_Person_strategy)
@settings(max_examples=50)
def test_ecvi_person_instantiation(instance):
    assert isinstance(instance, ecvi_Person)



@given(instance=ecvi_Person_strategy)
def test_ecvi_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecvi_Test_strategy)
@settings(max_examples=50)
def test_ecvi_test_instantiation(instance):
    assert isinstance(instance, ecvi_Test)



@given(instance=ecvi_Test_strategy)
def test_ecvi_test_idref_setter(instance):
    original = instance.idref
    instance.idref = original
    assert instance.idref == original



@given(instance=ecvi_Test_strategy)
def test_ecvi_test_testCode_setter(instance):
    original = instance.testCode
    instance.testCode = original
    assert instance.testCode == original

@given(instance=ecvi_AnimalTag_strategy)
@settings(max_examples=50)
def test_ecvi_animaltag_instantiation(instance):
    assert isinstance(instance, ecvi_AnimalTag)



@given(instance=ecvi_AnimalTag_strategy)
def test_ecvi_animaltag_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=ecvi_AnimalTag_strategy)
def test_ecvi_animaltag_brandImage_setter(instance):
    original = instance.brandImage
    instance.brandImage = original
    assert instance.brandImage == original



@given(instance=ecvi_AnimalTag_strategy)
def test_ecvi_animaltag_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ecvi_Animal_strategy)
@settings(max_examples=50)
def test_ecvi_animal_instantiation(instance):
    assert isinstance(instance, ecvi_Animal)



@given(instance=ecvi_Animal_strategy)
def test_ecvi_animal_inspectionDate_setter(instance):
    original = instance.inspectionDate
    instance.inspectionDate = original
    assert instance.inspectionDate == original



@given(instance=ecvi_Animal_strategy)
def test_ecvi_animal_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original



@given(instance=ecvi_Animal_strategy)
def test_ecvi_animal_sexDetail_setter(instance):
    original = instance.sexDetail
    instance.sexDetail = original
    assert instance.sexDetail == original



@given(instance=ecvi_Animal_strategy)
def test_ecvi_animal_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=ecvi_Animal_strategy)
def test_ecvi_animal_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=ecvi_Attachement_strategy)
@settings(max_examples=50)
def test_ecvi_attachement_instantiation(instance):
    assert isinstance(instance, ecvi_Attachement)



@given(instance=ecvi_Attachement_strategy)
def test_ecvi_attachement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=ecvi_Attachement_strategy)
def test_ecvi_attachement_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=ecvi_Attachement_strategy)
def test_ecvi_attachement_payload_setter(instance):
    original = instance.payload
    instance.payload = original
    assert instance.payload == original



@given(instance=ecvi_Attachement_strategy)
def test_ecvi_attachement_docType_setter(instance):
    original = instance.docType
    instance.docType = original
    assert instance.docType == original



@given(instance=ecvi_Attachement_strategy)
def test_ecvi_attachement_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=ecvi_Address_strategy)
@settings(max_examples=50)
def test_ecvi_address_instantiation(instance):
    assert isinstance(instance, ecvi_Address)



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_line1_setter(instance):
    original = instance.line1
    instance.line1 = original
    assert instance.line1 == original



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_zIP_setter(instance):
    original = instance.zIP
    instance.zIP = original
    assert instance.zIP == original



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_town_setter(instance):
    original = instance.town
    instance.town = original
    assert instance.town == original



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_line2_setter(instance):
    original = instance.line2
    instance.line2 = original
    assert instance.line2 == original



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_county_setter(instance):
    original = instance.county
    instance.county = original
    assert instance.county == original



@given(instance=ecvi_Address_strategy)
def test_ecvi_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=ecvi_Accessions_strategy)
@settings(max_examples=50)
def test_ecvi_accessions_instantiation(instance):
    assert isinstance(instance, ecvi_Accessions)

@given(instance=ecvi_GeoPoint_strategy)
@settings(max_examples=50)
def test_ecvi_geopoint_instantiation(instance):
    assert isinstance(instance, ecvi_GeoPoint)



@given(instance=ecvi_GeoPoint_strategy)
def test_ecvi_geopoint_lng_setter(instance):
    original = instance.lng
    instance.lng = original
    assert instance.lng == original



@given(instance=ecvi_GeoPoint_strategy)
def test_ecvi_geopoint_lat_setter(instance):
    original = instance.lat
    instance.lat = original
    assert instance.lat == original

@given(instance=ecvi_Laboratory_strategy)
@settings(max_examples=50)
def test_ecvi_laboratory_instantiation(instance):
    assert isinstance(instance, ecvi_Laboratory)



@given(instance=ecvi_Laboratory_strategy)
def test_ecvi_laboratory_premId_setter(instance):
    original = instance.premId
    instance.premId = original
    assert instance.premId == original



@given(instance=ecvi_Laboratory_strategy)
def test_ecvi_laboratory_accessionNumber_setter(instance):
    original = instance.accessionNumber
    instance.accessionNumber = original
    assert instance.accessionNumber == original



@given(instance=ecvi_Laboratory_strategy)
def test_ecvi_laboratory_accessionDate_setter(instance):
    original = instance.accessionDate
    instance.accessionDate = original
    assert instance.accessionDate == original



@given(instance=ecvi_Laboratory_strategy)
def test_ecvi_laboratory_labName_setter(instance):
    original = instance.labName
    instance.labName = original
    assert instance.labName == original

@given(instance=ecvi_Accession_strategy)
@settings(max_examples=50)
def test_ecvi_accession_instantiation(instance):
    assert isinstance(instance, ecvi_Accession)



@given(instance=ecvi_Accession_strategy)
def test_ecvi_accession_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ecvi_Accession_strategy)
def test_ecvi_accession_infieldTest_setter(instance):
    original = instance.infieldTest
    instance.infieldTest = original
    assert instance.infieldTest == original
