import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lobj::InternalRef,
    lobj::Publisher,
    lobj::PublishInfo,
    lobj::Note,
    lobj::AuthorizationTypes,
    lobj::Precognition,
    SimpleDidacMeta,
    lobj::Domain,
    lobj::DidacMeta,
    lobj::Person,
    lobj::Author,
    lobj::Blocktype,
    lobj::Address,
    lobj::Edition,
    lobj::Userauthorization,
    lobj::Affiliation,
    lobj::Sharednotes,
    lobj::User,
    lobj::ResrcFiletype,
    Node,
    lobj::ThemeNode,
    lobj::LuNode,
    lobj::SimpleDidacMeta,
    lobj::Node,
    lobj::Item,
    lobj::Coursetype,
    lobj::PresentationBlock,
    AbstractContent,
    lobj::Source,
    lobj::CorrBlock,
    lobj::TitleMeta,
    lobj::AccessControl,
    lobj::ExternalMetadata,
    LearningObject,
    lobj::BlockAudiofile,
    lobj::LuMeta,
    lobj::FolderMeta,
    lobj::CourseMeta,
    lobj::LearningUnit,
    lobj::ResrcFile,
    lobj::Module,
    lobj::Theme,
    lobj::BlockMeta,
    lobj::LuFolder,
    lobj::ResrcMeta,
    lobj::ModuleMeta,
    lobj::ModuleFolder,
    lobj::Category,
    lobj::BlockFolder,
    lobj::Course,
    lobj::ResrcFolder,
    lobj::Block,
    lobj::LearningObject,
    lobj::Language,
    lobj::AbstractContent,
    lobj::HypertextContent,
    Block,
    lobj::HypertextBlock,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lobj::internalref_is_not_abstract():
    assert not inspect.isabstract(lobj::InternalRef)


def test_lobj::internalref_constructor_exists():
    assert callable(lobj::InternalRef.__init__)


def test_lobj::internalref_constructor_args():
    sig = inspect.signature(lobj::InternalRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "reftype" in params, "Missing parameter 'reftype'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "file" in params, "Missing parameter 'file'"

def test_lobj::internalref_has_id():
    assert hasattr(lobj::InternalRef, "id")
    descriptor = None
    for klass in lobj::InternalRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::internalref_has_reftype():
    assert hasattr(lobj::InternalRef, "reftype")
    descriptor = None
    for klass in lobj::InternalRef.__mro__:
        if "reftype" in klass.__dict__:
            descriptor = klass.__dict__["reftype"]
            break
    assert isinstance(descriptor, property)

def test_lobj::internalref_has_ref():
    assert hasattr(lobj::InternalRef, "ref")
    descriptor = None
    for klass in lobj::InternalRef.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)

def test_lobj::internalref_has_file():
    assert hasattr(lobj::InternalRef, "file")
    descriptor = None
    for klass in lobj::InternalRef.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_lobj::publisher_is_not_abstract():
    assert not inspect.isabstract(lobj::Publisher)


def test_lobj::publisher_constructor_exists():
    assert callable(lobj::Publisher.__init__)


def test_lobj::publisher_constructor_args():
    sig = inspect.signature(lobj::Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "publishername" in params, "Missing parameter 'publishername'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::publisher_has_publishername():
    assert hasattr(lobj::Publisher, "publishername")
    descriptor = None
    for klass in lobj::Publisher.__mro__:
        if "publishername" in klass.__dict__:
            descriptor = klass.__dict__["publishername"]
            break
    assert isinstance(descriptor, property)

def test_lobj::publisher_has_id():
    assert hasattr(lobj::Publisher, "id")
    descriptor = None
    for klass in lobj::Publisher.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::publishinfo_is_not_abstract():
    assert not inspect.isabstract(lobj::PublishInfo)


def test_lobj::publishinfo_constructor_exists():
    assert callable(lobj::PublishInfo.__init__)


def test_lobj::publishinfo_constructor_args():
    sig = inspect.signature(lobj::PublishInfo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "pubsnumber" in params, "Missing parameter 'pubsnumber'"
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "releaseinfo" in params, "Missing parameter 'releaseinfo'"
    assert "edition" in params, "Missing parameter 'edition'"

def test_lobj::publishinfo_has_id():
    assert hasattr(lobj::PublishInfo, "id")
    descriptor = None
    for klass in lobj::PublishInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::publishinfo_has_pubsnumber():
    assert hasattr(lobj::PublishInfo, "pubsnumber")
    descriptor = None
    for klass in lobj::PublishInfo.__mro__:
        if "pubsnumber" in klass.__dict__:
            descriptor = klass.__dict__["pubsnumber"]
            break
    assert isinstance(descriptor, property)

def test_lobj::publishinfo_has_pubdate():
    assert hasattr(lobj::PublishInfo, "pubdate")
    descriptor = None
    for klass in lobj::PublishInfo.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::publishinfo_has_releaseinfo():
    assert hasattr(lobj::PublishInfo, "releaseinfo")
    descriptor = None
    for klass in lobj::PublishInfo.__mro__:
        if "releaseinfo" in klass.__dict__:
            descriptor = klass.__dict__["releaseinfo"]
            break
    assert isinstance(descriptor, property)

def test_lobj::publishinfo_has_edition():
    assert hasattr(lobj::PublishInfo, "edition")
    descriptor = None
    for klass in lobj::PublishInfo.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)



def test_lobj::note_is_not_abstract():
    assert not inspect.isabstract(lobj::Note)


def test_lobj::note_constructor_exists():
    assert callable(lobj::Note.__init__)


def test_lobj::note_constructor_args():
    sig = inspect.signature(lobj::Note.__init__)
    params = list(sig.parameters.keys())
    assert "noteAuthor" in params, "Missing parameter 'noteAuthor'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "content" in params, "Missing parameter 'content'"

def test_lobj::note_has_noteAuthor():
    assert hasattr(lobj::Note, "noteAuthor")
    descriptor = None
    for klass in lobj::Note.__mro__:
        if "noteAuthor" in klass.__dict__:
            descriptor = klass.__dict__["noteAuthor"]
            break
    assert isinstance(descriptor, property)

def test_lobj::note_has_date():
    assert hasattr(lobj::Note, "date")
    descriptor = None
    for klass in lobj::Note.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_lobj::note_has_id():
    assert hasattr(lobj::Note, "id")
    descriptor = None
    for klass in lobj::Note.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::note_has_content():
    assert hasattr(lobj::Note, "content")
    descriptor = None
    for klass in lobj::Note.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_lobj::authorizationtypes_is_not_abstract():
    assert not inspect.isabstract(lobj::AuthorizationTypes)


def test_lobj::authorizationtypes_constructor_exists():
    assert callable(lobj::AuthorizationTypes.__init__)


def test_lobj::authorizationtypes_constructor_args():
    sig = inspect.signature(lobj::AuthorizationTypes.__init__)
    params = list(sig.parameters.keys())
    assert "authType" in params, "Missing parameter 'authType'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "authTypeDesc" in params, "Missing parameter 'authTypeDesc'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::authorizationtypes_has_authType():
    assert hasattr(lobj::AuthorizationTypes, "authType")
    descriptor = None
    for klass in lobj::AuthorizationTypes.__mro__:
        if "authType" in klass.__dict__:
            descriptor = klass.__dict__["authType"]
            break
    assert isinstance(descriptor, property)

def test_lobj::authorizationtypes_has_readOnly():
    assert hasattr(lobj::AuthorizationTypes, "readOnly")
    descriptor = None
    for klass in lobj::AuthorizationTypes.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_lobj::authorizationtypes_has_authTypeDesc():
    assert hasattr(lobj::AuthorizationTypes, "authTypeDesc")
    descriptor = None
    for klass in lobj::AuthorizationTypes.__mro__:
        if "authTypeDesc" in klass.__dict__:
            descriptor = klass.__dict__["authTypeDesc"]
            break
    assert isinstance(descriptor, property)

def test_lobj::authorizationtypes_has_id():
    assert hasattr(lobj::AuthorizationTypes, "id")
    descriptor = None
    for klass in lobj::AuthorizationTypes.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::precognition_is_not_abstract():
    assert not inspect.isabstract(lobj::Precognition)


def test_lobj::precognition_constructor_exists():
    assert callable(lobj::Precognition.__init__)


def test_lobj::precognition_constructor_args():
    sig = inspect.signature(lobj::Precognition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "precog" in params, "Missing parameter 'precog'"

def test_lobj::precognition_has_id():
    assert hasattr(lobj::Precognition, "id")
    descriptor = None
    for klass in lobj::Precognition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::precognition_has_precog():
    assert hasattr(lobj::Precognition, "precog")
    descriptor = None
    for klass in lobj::Precognition.__mro__:
        if "precog" in klass.__dict__:
            descriptor = klass.__dict__["precog"]
            break
    assert isinstance(descriptor, property)



def test_simpledidacmeta_is_not_abstract():
    assert not inspect.isabstract(SimpleDidacMeta)


def test_simpledidacmeta_constructor_exists():
    assert callable(SimpleDidacMeta.__init__)


def test_simpledidacmeta_constructor_args():
    sig = inspect.signature(SimpleDidacMeta.__init__)
    params = list(sig.parameters.keys())



def test_lobj::domain_is_not_abstract():
    assert not inspect.isabstract(lobj::Domain)


def test_lobj::domain_constructor_exists():
    assert callable(lobj::Domain.__init__)


def test_lobj::domain_constructor_args():
    sig = inspect.signature(lobj::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "description" in params, "Missing parameter 'description'"
    assert "serverURL" in params, "Missing parameter 'serverURL'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_lobj::domain_has_creationDate():
    assert hasattr(lobj::Domain, "creationDate")
    descriptor = None
    for klass in lobj::Domain.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::domain_has_description():
    assert hasattr(lobj::Domain, "description")
    descriptor = None
    for klass in lobj::Domain.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj::domain_has_serverURL():
    assert hasattr(lobj::Domain, "serverURL")
    descriptor = None
    for klass in lobj::Domain.__mro__:
        if "serverURL" in klass.__dict__:
            descriptor = klass.__dict__["serverURL"]
            break
    assert isinstance(descriptor, property)

def test_lobj::domain_has_id():
    assert hasattr(lobj::Domain, "id")
    descriptor = None
    for klass in lobj::Domain.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::domain_has_name():
    assert hasattr(lobj::Domain, "name")
    descriptor = None
    for klass in lobj::Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lobj::didacmeta_is_not_abstract():
    assert not inspect.isabstract(lobj::DidacMeta)


def test_lobj::didacmeta_constructor_exists():
    assert callable(lobj::DidacMeta.__init__)


def test_lobj::didacmeta_constructor_args():
    sig = inspect.signature(lobj::DidacMeta.__init__)
    params = list(sig.parameters.keys())
    assert "goal" in params, "Missing parameter 'goal'"

def test_lobj::didacmeta_has_goal():
    assert hasattr(lobj::DidacMeta, "goal")
    descriptor = None
    for klass in lobj::DidacMeta.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)



def test_lobj::person_is_not_abstract():
    assert not inspect.isabstract(lobj::Person)


def test_lobj::person_constructor_exists():
    assert callable(lobj::Person.__init__)


def test_lobj::person_constructor_args():
    sig = inspect.signature(lobj::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "honorific" in params, "Missing parameter 'honorific'"
    assert "contrib" in params, "Missing parameter 'contrib'"
    assert "personblurb" in params, "Missing parameter 'personblurb'"
    assert "id" in params, "Missing parameter 'id'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_lobj::person_has_firstname():
    assert hasattr(lobj::Person, "firstname")
    descriptor = None
    for klass in lobj::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_lobj::person_has_honorific():
    assert hasattr(lobj::Person, "honorific")
    descriptor = None
    for klass in lobj::Person.__mro__:
        if "honorific" in klass.__dict__:
            descriptor = klass.__dict__["honorific"]
            break
    assert isinstance(descriptor, property)

def test_lobj::person_has_contrib():
    assert hasattr(lobj::Person, "contrib")
    descriptor = None
    for klass in lobj::Person.__mro__:
        if "contrib" in klass.__dict__:
            descriptor = klass.__dict__["contrib"]
            break
    assert isinstance(descriptor, property)

def test_lobj::person_has_personblurb():
    assert hasattr(lobj::Person, "personblurb")
    descriptor = None
    for klass in lobj::Person.__mro__:
        if "personblurb" in klass.__dict__:
            descriptor = klass.__dict__["personblurb"]
            break
    assert isinstance(descriptor, property)

def test_lobj::person_has_id():
    assert hasattr(lobj::Person, "id")
    descriptor = None
    for klass in lobj::Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::person_has_surname():
    assert hasattr(lobj::Person, "surname")
    descriptor = None
    for klass in lobj::Person.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_lobj::author_is_not_abstract():
    assert not inspect.isabstract(lobj::Author)


def test_lobj::author_constructor_exists():
    assert callable(lobj::Author.__init__)


def test_lobj::author_constructor_args():
    sig = inspect.signature(lobj::Author.__init__)
    params = list(sig.parameters.keys())
    assert "credittype" in params, "Missing parameter 'credittype'"
    assert "email" in params, "Missing parameter 'email'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::author_has_credittype():
    assert hasattr(lobj::Author, "credittype")
    descriptor = None
    for klass in lobj::Author.__mro__:
        if "credittype" in klass.__dict__:
            descriptor = klass.__dict__["credittype"]
            break
    assert isinstance(descriptor, property)

def test_lobj::author_has_email():
    assert hasattr(lobj::Author, "email")
    descriptor = None
    for klass in lobj::Author.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_lobj::author_has_id():
    assert hasattr(lobj::Author, "id")
    descriptor = None
    for klass in lobj::Author.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::blocktype_is_not_abstract():
    assert not inspect.isabstract(lobj::Blocktype)


def test_lobj::blocktype_constructor_exists():
    assert callable(lobj::Blocktype.__init__)


def test_lobj::blocktype_constructor_args():
    sig = inspect.signature(lobj::Blocktype.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "styleRef" in params, "Missing parameter 'styleRef'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::blocktype_has_creationDate():
    assert hasattr(lobj::Blocktype, "creationDate")
    descriptor = None
    for klass in lobj::Blocktype.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blocktype_has_styleRef():
    assert hasattr(lobj::Blocktype, "styleRef")
    descriptor = None
    for klass in lobj::Blocktype.__mro__:
        if "styleRef" in klass.__dict__:
            descriptor = klass.__dict__["styleRef"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blocktype_has_description():
    assert hasattr(lobj::Blocktype, "description")
    descriptor = None
    for klass in lobj::Blocktype.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blocktype_has_name():
    assert hasattr(lobj::Blocktype, "name")
    descriptor = None
    for klass in lobj::Blocktype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blocktype_has_id():
    assert hasattr(lobj::Blocktype, "id")
    descriptor = None
    for klass in lobj::Blocktype.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::address_is_not_abstract():
    assert not inspect.isabstract(lobj::Address)


def test_lobj::address_constructor_exists():
    assert callable(lobj::Address.__init__)


def test_lobj::address_constructor_args():
    sig = inspect.signature(lobj::Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "email" in params, "Missing parameter 'email'"
    assert "id" in params, "Missing parameter 'id'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "fax" in params, "Missing parameter 'fax'"
    assert "country" in params, "Missing parameter 'country'"
    assert "state" in params, "Missing parameter 'state'"
    assert "street" in params, "Missing parameter 'street'"
    assert "otheraddr" in params, "Missing parameter 'otheraddr'"
    assert "postcode" in params, "Missing parameter 'postcode'"

def test_lobj::address_has_city():
    assert hasattr(lobj::Address, "city")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_email():
    assert hasattr(lobj::Address, "email")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_id():
    assert hasattr(lobj::Address, "id")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_phone():
    assert hasattr(lobj::Address, "phone")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_fax():
    assert hasattr(lobj::Address, "fax")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "fax" in klass.__dict__:
            descriptor = klass.__dict__["fax"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_country():
    assert hasattr(lobj::Address, "country")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_state():
    assert hasattr(lobj::Address, "state")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_street():
    assert hasattr(lobj::Address, "street")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_otheraddr():
    assert hasattr(lobj::Address, "otheraddr")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "otheraddr" in klass.__dict__:
            descriptor = klass.__dict__["otheraddr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::address_has_postcode():
    assert hasattr(lobj::Address, "postcode")
    descriptor = None
    for klass in lobj::Address.__mro__:
        if "postcode" in klass.__dict__:
            descriptor = klass.__dict__["postcode"]
            break
    assert isinstance(descriptor, property)



def test_lobj::edition_is_not_abstract():
    assert not inspect.isabstract(lobj::Edition)


def test_lobj::edition_constructor_exists():
    assert callable(lobj::Edition.__init__)


def test_lobj::edition_constructor_args():
    sig = inspect.signature(lobj::Edition.__init__)
    params = list(sig.parameters.keys())
    assert "lastVersionNumber" in params, "Missing parameter 'lastVersionNumber'"
    assert "id" in params, "Missing parameter 'id'"
    assert "status" in params, "Missing parameter 'status'"
    assert "editedBy" in params, "Missing parameter 'editedBy'"
    assert "version" in params, "Missing parameter 'version'"
    assert "editionNr" in params, "Missing parameter 'editionNr'"
    assert "editionCreationDate" in params, "Missing parameter 'editionCreationDate'"

def test_lobj::edition_has_lastVersionNumber():
    assert hasattr(lobj::Edition, "lastVersionNumber")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "lastVersionNumber" in klass.__dict__:
            descriptor = klass.__dict__["lastVersionNumber"]
            break
    assert isinstance(descriptor, property)

def test_lobj::edition_has_id():
    assert hasattr(lobj::Edition, "id")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::edition_has_status():
    assert hasattr(lobj::Edition, "status")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_lobj::edition_has_editedBy():
    assert hasattr(lobj::Edition, "editedBy")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "editedBy" in klass.__dict__:
            descriptor = klass.__dict__["editedBy"]
            break
    assert isinstance(descriptor, property)

def test_lobj::edition_has_version():
    assert hasattr(lobj::Edition, "version")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_lobj::edition_has_editionNr():
    assert hasattr(lobj::Edition, "editionNr")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "editionNr" in klass.__dict__:
            descriptor = klass.__dict__["editionNr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::edition_has_editionCreationDate():
    assert hasattr(lobj::Edition, "editionCreationDate")
    descriptor = None
    for klass in lobj::Edition.__mro__:
        if "editionCreationDate" in klass.__dict__:
            descriptor = klass.__dict__["editionCreationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj::userauthorization_is_not_abstract():
    assert not inspect.isabstract(lobj::Userauthorization)


def test_lobj::userauthorization_constructor_exists():
    assert callable(lobj::Userauthorization.__init__)


def test_lobj::userauthorization_constructor_args():
    sig = inspect.signature(lobj::Userauthorization.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::userauthorization_has_id():
    assert hasattr(lobj::Userauthorization, "id")
    descriptor = None
    for klass in lobj::Userauthorization.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::affiliation_is_not_abstract():
    assert not inspect.isabstract(lobj::Affiliation)


def test_lobj::affiliation_constructor_exists():
    assert callable(lobj::Affiliation.__init__)


def test_lobj::affiliation_constructor_args():
    sig = inspect.signature(lobj::Affiliation.__init__)
    params = list(sig.parameters.keys())
    assert "shortaffil" in params, "Missing parameter 'shortaffil'"
    assert "jobtitle" in params, "Missing parameter 'jobtitle'"
    assert "orgdiv" in params, "Missing parameter 'orgdiv'"
    assert "orgname" in params, "Missing parameter 'orgname'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::affiliation_has_shortaffil():
    assert hasattr(lobj::Affiliation, "shortaffil")
    descriptor = None
    for klass in lobj::Affiliation.__mro__:
        if "shortaffil" in klass.__dict__:
            descriptor = klass.__dict__["shortaffil"]
            break
    assert isinstance(descriptor, property)

def test_lobj::affiliation_has_jobtitle():
    assert hasattr(lobj::Affiliation, "jobtitle")
    descriptor = None
    for klass in lobj::Affiliation.__mro__:
        if "jobtitle" in klass.__dict__:
            descriptor = klass.__dict__["jobtitle"]
            break
    assert isinstance(descriptor, property)

def test_lobj::affiliation_has_orgdiv():
    assert hasattr(lobj::Affiliation, "orgdiv")
    descriptor = None
    for klass in lobj::Affiliation.__mro__:
        if "orgdiv" in klass.__dict__:
            descriptor = klass.__dict__["orgdiv"]
            break
    assert isinstance(descriptor, property)

def test_lobj::affiliation_has_orgname():
    assert hasattr(lobj::Affiliation, "orgname")
    descriptor = None
    for klass in lobj::Affiliation.__mro__:
        if "orgname" in klass.__dict__:
            descriptor = klass.__dict__["orgname"]
            break
    assert isinstance(descriptor, property)

def test_lobj::affiliation_has_id():
    assert hasattr(lobj::Affiliation, "id")
    descriptor = None
    for klass in lobj::Affiliation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::sharednotes_is_not_abstract():
    assert not inspect.isabstract(lobj::Sharednotes)


def test_lobj::sharednotes_constructor_exists():
    assert callable(lobj::Sharednotes.__init__)


def test_lobj::sharednotes_constructor_args():
    sig = inspect.signature(lobj::Sharednotes.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::sharednotes_has_id():
    assert hasattr(lobj::Sharednotes, "id")
    descriptor = None
    for klass in lobj::Sharednotes.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::user_is_not_abstract():
    assert not inspect.isabstract(lobj::User)


def test_lobj::user_constructor_exists():
    assert callable(lobj::User.__init__)


def test_lobj::user_constructor_args():
    sig = inspect.signature(lobj::User.__init__)
    params = list(sig.parameters.keys())
    assert "entryasxml" in params, "Missing parameter 'entryasxml'"
    assert "lastcoursematerialviewnr" in params, "Missing parameter 'lastcoursematerialviewnr'"
    assert "inchatsince" in params, "Missing parameter 'inchatsince'"
    assert "chatroomnr" in params, "Missing parameter 'chatroomnr'"
    assert "datafilter" in params, "Missing parameter 'datafilter'"
    assert "icqnumber" in params, "Missing parameter 'icqnumber'"
    assert "languagenr" in params, "Missing parameter 'languagenr'"
    assert "scn" in params, "Missing parameter 'scn'"
    assert "contchatdate" in params, "Missing parameter 'contchatdate'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "icqpassword" in params, "Missing parameter 'icqpassword'"
    assert "id" in params, "Missing parameter 'id'"
    assert "onlinedate" in params, "Missing parameter 'onlinedate'"
    assert "fromext" in params, "Missing parameter 'fromext'"
    assert "loginname" in params, "Missing parameter 'loginname'"
    assert "notificationprofileasxml" in params, "Missing parameter 'notificationprofileasxml'"
    assert "matriculationnr" in params, "Missing parameter 'matriculationnr'"
    assert "lastcoursematerialnr" in params, "Missing parameter 'lastcoursematerialnr'"
    assert "onlinestatus" in params, "Missing parameter 'onlinestatus'"
    assert "dossierasxml" in params, "Missing parameter 'dossierasxml'"
    assert "currlogindate" in params, "Missing parameter 'currlogindate'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "photochanged" in params, "Missing parameter 'photochanged'"
    assert "photo" in params, "Missing parameter 'photo'"
    assert "authenticateldap" in params, "Missing parameter 'authenticateldap'"
    assert "lastlogindate" in params, "Missing parameter 'lastlogindate'"

def test_lobj::user_has_entryasxml():
    assert hasattr(lobj::User, "entryasxml")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "entryasxml" in klass.__dict__:
            descriptor = klass.__dict__["entryasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_lastcoursematerialviewnr():
    assert hasattr(lobj::User, "lastcoursematerialviewnr")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "lastcoursematerialviewnr" in klass.__dict__:
            descriptor = klass.__dict__["lastcoursematerialviewnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_inchatsince():
    assert hasattr(lobj::User, "inchatsince")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "inchatsince" in klass.__dict__:
            descriptor = klass.__dict__["inchatsince"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_chatroomnr():
    assert hasattr(lobj::User, "chatroomnr")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "chatroomnr" in klass.__dict__:
            descriptor = klass.__dict__["chatroomnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_datafilter():
    assert hasattr(lobj::User, "datafilter")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "datafilter" in klass.__dict__:
            descriptor = klass.__dict__["datafilter"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_icqnumber():
    assert hasattr(lobj::User, "icqnumber")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "icqnumber" in klass.__dict__:
            descriptor = klass.__dict__["icqnumber"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_languagenr():
    assert hasattr(lobj::User, "languagenr")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "languagenr" in klass.__dict__:
            descriptor = klass.__dict__["languagenr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_scn():
    assert hasattr(lobj::User, "scn")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "scn" in klass.__dict__:
            descriptor = klass.__dict__["scn"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_contchatdate():
    assert hasattr(lobj::User, "contchatdate")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "contchatdate" in klass.__dict__:
            descriptor = klass.__dict__["contchatdate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_lastname():
    assert hasattr(lobj::User, "lastname")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_password():
    assert hasattr(lobj::User, "password")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_icqpassword():
    assert hasattr(lobj::User, "icqpassword")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "icqpassword" in klass.__dict__:
            descriptor = klass.__dict__["icqpassword"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_id():
    assert hasattr(lobj::User, "id")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_onlinedate():
    assert hasattr(lobj::User, "onlinedate")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "onlinedate" in klass.__dict__:
            descriptor = klass.__dict__["onlinedate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_fromext():
    assert hasattr(lobj::User, "fromext")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "fromext" in klass.__dict__:
            descriptor = klass.__dict__["fromext"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_loginname():
    assert hasattr(lobj::User, "loginname")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "loginname" in klass.__dict__:
            descriptor = klass.__dict__["loginname"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_notificationprofileasxml():
    assert hasattr(lobj::User, "notificationprofileasxml")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "notificationprofileasxml" in klass.__dict__:
            descriptor = klass.__dict__["notificationprofileasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_matriculationnr():
    assert hasattr(lobj::User, "matriculationnr")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "matriculationnr" in klass.__dict__:
            descriptor = klass.__dict__["matriculationnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_lastcoursematerialnr():
    assert hasattr(lobj::User, "lastcoursematerialnr")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "lastcoursematerialnr" in klass.__dict__:
            descriptor = klass.__dict__["lastcoursematerialnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_onlinestatus():
    assert hasattr(lobj::User, "onlinestatus")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "onlinestatus" in klass.__dict__:
            descriptor = klass.__dict__["onlinestatus"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_dossierasxml():
    assert hasattr(lobj::User, "dossierasxml")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "dossierasxml" in klass.__dict__:
            descriptor = klass.__dict__["dossierasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_currlogindate():
    assert hasattr(lobj::User, "currlogindate")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "currlogindate" in klass.__dict__:
            descriptor = klass.__dict__["currlogindate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_firstname():
    assert hasattr(lobj::User, "firstname")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_photochanged():
    assert hasattr(lobj::User, "photochanged")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "photochanged" in klass.__dict__:
            descriptor = klass.__dict__["photochanged"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_photo():
    assert hasattr(lobj::User, "photo")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "photo" in klass.__dict__:
            descriptor = klass.__dict__["photo"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_authenticateldap():
    assert hasattr(lobj::User, "authenticateldap")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "authenticateldap" in klass.__dict__:
            descriptor = klass.__dict__["authenticateldap"]
            break
    assert isinstance(descriptor, property)

def test_lobj::user_has_lastlogindate():
    assert hasattr(lobj::User, "lastlogindate")
    descriptor = None
    for klass in lobj::User.__mro__:
        if "lastlogindate" in klass.__dict__:
            descriptor = klass.__dict__["lastlogindate"]
            break
    assert isinstance(descriptor, property)



def test_lobj::resrcfiletype_is_not_abstract():
    assert not inspect.isabstract(lobj::ResrcFiletype)


def test_lobj::resrcfiletype_constructor_exists():
    assert callable(lobj::ResrcFiletype.__init__)


def test_lobj::resrcfiletype_constructor_args():
    sig = inspect.signature(lobj::ResrcFiletype.__init__)
    params = list(sig.parameters.keys())
    assert "applet" in params, "Missing parameter 'applet'"
    assert "filetypeExtension" in params, "Missing parameter 'filetypeExtension'"
    assert "image" in params, "Missing parameter 'image'"
    assert "filetypeDesc" in params, "Missing parameter 'filetypeDesc'"
    assert "id" in params, "Missing parameter 'id'"
    assert "filetypeImageBif" in params, "Missing parameter 'filetypeImageBif'"
    assert "filetypeImageSmall" in params, "Missing parameter 'filetypeImageSmall'"

def test_lobj::resrcfiletype_has_applet():
    assert hasattr(lobj::ResrcFiletype, "applet")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "applet" in klass.__dict__:
            descriptor = klass.__dict__["applet"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfiletype_has_filetypeExtension():
    assert hasattr(lobj::ResrcFiletype, "filetypeExtension")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "filetypeExtension" in klass.__dict__:
            descriptor = klass.__dict__["filetypeExtension"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfiletype_has_image():
    assert hasattr(lobj::ResrcFiletype, "image")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfiletype_has_filetypeDesc():
    assert hasattr(lobj::ResrcFiletype, "filetypeDesc")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "filetypeDesc" in klass.__dict__:
            descriptor = klass.__dict__["filetypeDesc"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfiletype_has_id():
    assert hasattr(lobj::ResrcFiletype, "id")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfiletype_has_filetypeImageBif():
    assert hasattr(lobj::ResrcFiletype, "filetypeImageBif")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "filetypeImageBif" in klass.__dict__:
            descriptor = klass.__dict__["filetypeImageBif"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfiletype_has_filetypeImageSmall():
    assert hasattr(lobj::ResrcFiletype, "filetypeImageSmall")
    descriptor = None
    for klass in lobj::ResrcFiletype.__mro__:
        if "filetypeImageSmall" in klass.__dict__:
            descriptor = klass.__dict__["filetypeImageSmall"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_lobj::themenode_is_not_abstract():
    assert not inspect.isabstract(lobj::ThemeNode)


def test_lobj::themenode_constructor_exists():
    assert callable(lobj::ThemeNode.__init__)


def test_lobj::themenode_constructor_args():
    sig = inspect.signature(lobj::ThemeNode.__init__)
    params = list(sig.parameters.keys())



def test_lobj::lunode_is_not_abstract():
    assert not inspect.isabstract(lobj::LuNode)


def test_lobj::lunode_constructor_exists():
    assert callable(lobj::LuNode.__init__)


def test_lobj::lunode_constructor_args():
    sig = inspect.signature(lobj::LuNode.__init__)
    params = list(sig.parameters.keys())



def test_lobj::simpledidacmeta_is_not_abstract():
    assert not inspect.isabstract(lobj::SimpleDidacMeta)


def test_lobj::simpledidacmeta_constructor_exists():
    assert callable(lobj::SimpleDidacMeta.__init__)


def test_lobj::simpledidacmeta_constructor_args():
    sig = inspect.signature(lobj::SimpleDidacMeta.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "keywords" in params, "Missing parameter 'keywords'"

def test_lobj::simpledidacmeta_has_id():
    assert hasattr(lobj::SimpleDidacMeta, "id")
    descriptor = None
    for klass in lobj::SimpleDidacMeta.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::simpledidacmeta_has_description():
    assert hasattr(lobj::SimpleDidacMeta, "description")
    descriptor = None
    for klass in lobj::SimpleDidacMeta.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj::simpledidacmeta_has_title():
    assert hasattr(lobj::SimpleDidacMeta, "title")
    descriptor = None
    for klass in lobj::SimpleDidacMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj::simpledidacmeta_has_keywords():
    assert hasattr(lobj::SimpleDidacMeta, "keywords")
    descriptor = None
    for klass in lobj::SimpleDidacMeta.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)



def test_lobj::node_is_not_abstract():
    assert not inspect.isabstract(lobj::Node)


def test_lobj::node_constructor_exists():
    assert callable(lobj::Node.__init__)


def test_lobj::node_constructor_args():
    sig = inspect.signature(lobj::Node.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::node_has_visible():
    assert hasattr(lobj::Node, "visible")
    descriptor = None
    for klass in lobj::Node.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_lobj::node_has_id():
    assert hasattr(lobj::Node, "id")
    descriptor = None
    for klass in lobj::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::item_is_not_abstract():
    assert not inspect.isabstract(lobj::Item)


def test_lobj::item_constructor_exists():
    assert callable(lobj::Item.__init__)


def test_lobj::item_constructor_args():
    sig = inspect.signature(lobj::Item.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "luRef" in params, "Missing parameter 'luRef'"

def test_lobj::item_has_id():
    assert hasattr(lobj::Item, "id")
    descriptor = None
    for klass in lobj::Item.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::item_has_luRef():
    assert hasattr(lobj::Item, "luRef")
    descriptor = None
    for klass in lobj::Item.__mro__:
        if "luRef" in klass.__dict__:
            descriptor = klass.__dict__["luRef"]
            break
    assert isinstance(descriptor, property)



def test_lobj::coursetype_is_not_abstract():
    assert not inspect.isabstract(lobj::Coursetype)


def test_lobj::coursetype_constructor_exists():
    assert callable(lobj::Coursetype.__init__)


def test_lobj::coursetype_constructor_args():
    sig = inspect.signature(lobj::Coursetype.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"

def test_lobj::coursetype_has_title():
    assert hasattr(lobj::Coursetype, "title")
    descriptor = None
    for klass in lobj::Coursetype.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj::coursetype_has_id():
    assert hasattr(lobj::Coursetype, "id")
    descriptor = None
    for klass in lobj::Coursetype.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::coursetype_has_description():
    assert hasattr(lobj::Coursetype, "description")
    descriptor = None
    for klass in lobj::Coursetype.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_lobj::presentationblock_is_not_abstract():
    assert not inspect.isabstract(lobj::PresentationBlock)


def test_lobj::presentationblock_constructor_exists():
    assert callable(lobj::PresentationBlock.__init__)


def test_lobj::presentationblock_constructor_args():
    sig = inspect.signature(lobj::PresentationBlock.__init__)
    params = list(sig.parameters.keys())
    assert "lod" in params, "Missing parameter 'lod'"
    assert "id" in params, "Missing parameter 'id'"
    assert "rendering" in params, "Missing parameter 'rendering'"

def test_lobj::presentationblock_has_lod():
    assert hasattr(lobj::PresentationBlock, "lod")
    descriptor = None
    for klass in lobj::PresentationBlock.__mro__:
        if "lod" in klass.__dict__:
            descriptor = klass.__dict__["lod"]
            break
    assert isinstance(descriptor, property)

def test_lobj::presentationblock_has_id():
    assert hasattr(lobj::PresentationBlock, "id")
    descriptor = None
    for klass in lobj::PresentationBlock.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::presentationblock_has_rendering():
    assert hasattr(lobj::PresentationBlock, "rendering")
    descriptor = None
    for klass in lobj::PresentationBlock.__mro__:
        if "rendering" in klass.__dict__:
            descriptor = klass.__dict__["rendering"]
            break
    assert isinstance(descriptor, property)



def test_abstractcontent_is_not_abstract():
    assert not inspect.isabstract(AbstractContent)


def test_abstractcontent_constructor_exists():
    assert callable(AbstractContent.__init__)


def test_abstractcontent_constructor_args():
    sig = inspect.signature(AbstractContent.__init__)
    params = list(sig.parameters.keys())



def test_lobj::source_is_not_abstract():
    assert not inspect.isabstract(lobj::Source)


def test_lobj::source_constructor_exists():
    assert callable(lobj::Source.__init__)


def test_lobj::source_constructor_args():
    sig = inspect.signature(lobj::Source.__init__)
    params = list(sig.parameters.keys())
    assert "pp" in params, "Missing parameter 'pp'"
    assert "subtitle" in params, "Missing parameter 'subtitle'"
    assert "publishedIn" in params, "Missing parameter 'publishedIn'"
    assert "id" in params, "Missing parameter 'id'"
    assert "publishDate" in params, "Missing parameter 'publishDate'"
    assert "title" in params, "Missing parameter 'title'"
    assert "publishedBy" in params, "Missing parameter 'publishedBy'"

def test_lobj::source_has_pp():
    assert hasattr(lobj::Source, "pp")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "pp" in klass.__dict__:
            descriptor = klass.__dict__["pp"]
            break
    assert isinstance(descriptor, property)

def test_lobj::source_has_subtitle():
    assert hasattr(lobj::Source, "subtitle")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "subtitle" in klass.__dict__:
            descriptor = klass.__dict__["subtitle"]
            break
    assert isinstance(descriptor, property)

def test_lobj::source_has_publishedIn():
    assert hasattr(lobj::Source, "publishedIn")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "publishedIn" in klass.__dict__:
            descriptor = klass.__dict__["publishedIn"]
            break
    assert isinstance(descriptor, property)

def test_lobj::source_has_id():
    assert hasattr(lobj::Source, "id")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::source_has_publishDate():
    assert hasattr(lobj::Source, "publishDate")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "publishDate" in klass.__dict__:
            descriptor = klass.__dict__["publishDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::source_has_title():
    assert hasattr(lobj::Source, "title")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj::source_has_publishedBy():
    assert hasattr(lobj::Source, "publishedBy")
    descriptor = None
    for klass in lobj::Source.__mro__:
        if "publishedBy" in klass.__dict__:
            descriptor = klass.__dict__["publishedBy"]
            break
    assert isinstance(descriptor, property)



def test_lobj::corrblock_is_not_abstract():
    assert not inspect.isabstract(lobj::CorrBlock)


def test_lobj::corrblock_constructor_exists():
    assert callable(lobj::CorrBlock.__init__)


def test_lobj::corrblock_constructor_args():
    sig = inspect.signature(lobj::CorrBlock.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::corrblock_has_id():
    assert hasattr(lobj::CorrBlock, "id")
    descriptor = None
    for klass in lobj::CorrBlock.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj::titlemeta_is_not_abstract():
    assert not inspect.isabstract(lobj::TitleMeta)


def test_lobj::titlemeta_constructor_exists():
    assert callable(lobj::TitleMeta.__init__)


def test_lobj::titlemeta_constructor_args():
    sig = inspect.signature(lobj::TitleMeta.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_lobj::titlemeta_has_id():
    assert hasattr(lobj::TitleMeta, "id")
    descriptor = None
    for klass in lobj::TitleMeta.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::titlemeta_has_title():
    assert hasattr(lobj::TitleMeta, "title")
    descriptor = None
    for klass in lobj::TitleMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lobj::accesscontrol_is_not_abstract():
    assert not inspect.isabstract(lobj::AccessControl)


def test_lobj::accesscontrol_constructor_exists():
    assert callable(lobj::AccessControl.__init__)


def test_lobj::accesscontrol_constructor_args():
    sig = inspect.signature(lobj::AccessControl.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "globalAccess" in params, "Missing parameter 'globalAccess'"
    assert "status" in params, "Missing parameter 'status'"
    assert "lastStatusChange" in params, "Missing parameter 'lastStatusChange'"
    assert "lastModified" in params, "Missing parameter 'lastModified'"

def test_lobj::accesscontrol_has_id():
    assert hasattr(lobj::AccessControl, "id")
    descriptor = None
    for klass in lobj::AccessControl.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::accesscontrol_has_globalAccess():
    assert hasattr(lobj::AccessControl, "globalAccess")
    descriptor = None
    for klass in lobj::AccessControl.__mro__:
        if "globalAccess" in klass.__dict__:
            descriptor = klass.__dict__["globalAccess"]
            break
    assert isinstance(descriptor, property)

def test_lobj::accesscontrol_has_status():
    assert hasattr(lobj::AccessControl, "status")
    descriptor = None
    for klass in lobj::AccessControl.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_lobj::accesscontrol_has_lastStatusChange():
    assert hasattr(lobj::AccessControl, "lastStatusChange")
    descriptor = None
    for klass in lobj::AccessControl.__mro__:
        if "lastStatusChange" in klass.__dict__:
            descriptor = klass.__dict__["lastStatusChange"]
            break
    assert isinstance(descriptor, property)

def test_lobj::accesscontrol_has_lastModified():
    assert hasattr(lobj::AccessControl, "lastModified")
    descriptor = None
    for klass in lobj::AccessControl.__mro__:
        if "lastModified" in klass.__dict__:
            descriptor = klass.__dict__["lastModified"]
            break
    assert isinstance(descriptor, property)



def test_lobj::externalmetadata_is_not_abstract():
    assert not inspect.isabstract(lobj::ExternalMetadata)


def test_lobj::externalmetadata_constructor_exists():
    assert callable(lobj::ExternalMetadata.__init__)


def test_lobj::externalmetadata_constructor_args():
    sig = inspect.signature(lobj::ExternalMetadata.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj::externalmetadata_has_file():
    assert hasattr(lobj::ExternalMetadata, "file")
    descriptor = None
    for klass in lobj::ExternalMetadata.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_lobj::externalmetadata_has_ref():
    assert hasattr(lobj::ExternalMetadata, "ref")
    descriptor = None
    for klass in lobj::ExternalMetadata.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)

def test_lobj::externalmetadata_has_id():
    assert hasattr(lobj::ExternalMetadata, "id")
    descriptor = None
    for klass in lobj::ExternalMetadata.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_learningobject_is_not_abstract():
    assert not inspect.isabstract(LearningObject)


def test_learningobject_constructor_exists():
    assert callable(LearningObject.__init__)


def test_learningobject_constructor_args():
    sig = inspect.signature(LearningObject.__init__)
    params = list(sig.parameters.keys())



def test_lobj::blockaudiofile_is_not_abstract():
    assert not inspect.isabstract(lobj::BlockAudiofile)


def test_lobj::blockaudiofile_constructor_exists():
    assert callable(lobj::BlockAudiofile.__init__)


def test_lobj::blockaudiofile_constructor_args():
    sig = inspect.signature(lobj::BlockAudiofile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"
    assert "filesize" in params, "Missing parameter 'filesize'"
    assert "originalextension" in params, "Missing parameter 'originalextension'"
    assert "resrcHref" in params, "Missing parameter 'resrcHref'"

def test_lobj::blockaudiofile_has_file():
    assert hasattr(lobj::BlockAudiofile, "file")
    descriptor = None
    for klass in lobj::BlockAudiofile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blockaudiofile_has_filesize():
    assert hasattr(lobj::BlockAudiofile, "filesize")
    descriptor = None
    for klass in lobj::BlockAudiofile.__mro__:
        if "filesize" in klass.__dict__:
            descriptor = klass.__dict__["filesize"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blockaudiofile_has_originalextension():
    assert hasattr(lobj::BlockAudiofile, "originalextension")
    descriptor = None
    for klass in lobj::BlockAudiofile.__mro__:
        if "originalextension" in klass.__dict__:
            descriptor = klass.__dict__["originalextension"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blockaudiofile_has_resrcHref():
    assert hasattr(lobj::BlockAudiofile, "resrcHref")
    descriptor = None
    for klass in lobj::BlockAudiofile.__mro__:
        if "resrcHref" in klass.__dict__:
            descriptor = klass.__dict__["resrcHref"]
            break
    assert isinstance(descriptor, property)



def test_lobj::lumeta_is_not_abstract():
    assert not inspect.isabstract(lobj::LuMeta)


def test_lobj::lumeta_constructor_exists():
    assert callable(lobj::LuMeta.__init__)


def test_lobj::lumeta_constructor_args():
    sig = inspect.signature(lobj::LuMeta.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj::lumeta_has_creationDate():
    assert hasattr(lobj::LuMeta, "creationDate")
    descriptor = None
    for klass in lobj::LuMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj::foldermeta_is_not_abstract():
    assert not inspect.isabstract(lobj::FolderMeta)


def test_lobj::foldermeta_constructor_exists():
    assert callable(lobj::FolderMeta.__init__)


def test_lobj::foldermeta_constructor_args():
    sig = inspect.signature(lobj::FolderMeta.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"

def test_lobj::foldermeta_has_creationDate():
    assert hasattr(lobj::FolderMeta, "creationDate")
    descriptor = None
    for klass in lobj::FolderMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::foldermeta_has_description():
    assert hasattr(lobj::FolderMeta, "description")
    descriptor = None
    for klass in lobj::FolderMeta.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj::foldermeta_has_title():
    assert hasattr(lobj::FolderMeta, "title")
    descriptor = None
    for klass in lobj::FolderMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lobj::coursemeta_is_not_abstract():
    assert not inspect.isabstract(lobj::CourseMeta)


def test_lobj::coursemeta_constructor_exists():
    assert callable(lobj::CourseMeta.__init__)


def test_lobj::coursemeta_constructor_args():
    sig = inspect.signature(lobj::CourseMeta.__init__)
    params = list(sig.parameters.keys())
    assert "columnfilterasxml" in params, "Missing parameter 'columnfilterasxml'"
    assert "hours" in params, "Missing parameter 'hours'"
    assert "fromext" in params, "Missing parameter 'fromext'"
    assert "lvanr" in params, "Missing parameter 'lvanr'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj::coursemeta_has_columnfilterasxml():
    assert hasattr(lobj::CourseMeta, "columnfilterasxml")
    descriptor = None
    for klass in lobj::CourseMeta.__mro__:
        if "columnfilterasxml" in klass.__dict__:
            descriptor = klass.__dict__["columnfilterasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj::coursemeta_has_hours():
    assert hasattr(lobj::CourseMeta, "hours")
    descriptor = None
    for klass in lobj::CourseMeta.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_lobj::coursemeta_has_fromext():
    assert hasattr(lobj::CourseMeta, "fromext")
    descriptor = None
    for klass in lobj::CourseMeta.__mro__:
        if "fromext" in klass.__dict__:
            descriptor = klass.__dict__["fromext"]
            break
    assert isinstance(descriptor, property)

def test_lobj::coursemeta_has_lvanr():
    assert hasattr(lobj::CourseMeta, "lvanr")
    descriptor = None
    for klass in lobj::CourseMeta.__mro__:
        if "lvanr" in klass.__dict__:
            descriptor = klass.__dict__["lvanr"]
            break
    assert isinstance(descriptor, property)

def test_lobj::coursemeta_has_creationDate():
    assert hasattr(lobj::CourseMeta, "creationDate")
    descriptor = None
    for klass in lobj::CourseMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj::learningunit_is_not_abstract():
    assert not inspect.isabstract(lobj::LearningUnit)


def test_lobj::learningunit_constructor_exists():
    assert callable(lobj::LearningUnit.__init__)


def test_lobj::learningunit_constructor_args():
    sig = inspect.signature(lobj::LearningUnit.__init__)
    params = list(sig.parameters.keys())
    assert "luFile" in params, "Missing parameter 'luFile'"
    assert "treeAsXml" in params, "Missing parameter 'treeAsXml'"

def test_lobj::learningunit_has_luFile():
    assert hasattr(lobj::LearningUnit, "luFile")
    descriptor = None
    for klass in lobj::LearningUnit.__mro__:
        if "luFile" in klass.__dict__:
            descriptor = klass.__dict__["luFile"]
            break
    assert isinstance(descriptor, property)

def test_lobj::learningunit_has_treeAsXml():
    assert hasattr(lobj::LearningUnit, "treeAsXml")
    descriptor = None
    for klass in lobj::LearningUnit.__mro__:
        if "treeAsXml" in klass.__dict__:
            descriptor = klass.__dict__["treeAsXml"]
            break
    assert isinstance(descriptor, property)



def test_lobj::resrcfile_is_not_abstract():
    assert not inspect.isabstract(lobj::ResrcFile)


def test_lobj::resrcfile_constructor_exists():
    assert callable(lobj::ResrcFile.__init__)


def test_lobj::resrcfile_constructor_args():
    sig = inspect.signature(lobj::ResrcFile.__init__)
    params = list(sig.parameters.keys())
    assert "filesize" in params, "Missing parameter 'filesize'"
    assert "resrcHref" in params, "Missing parameter 'resrcHref'"
    assert "originalextension" in params, "Missing parameter 'originalextension'"
    assert "file_tn" in params, "Missing parameter 'file_tn'"
    assert "file" in params, "Missing parameter 'file'"

def test_lobj::resrcfile_has_filesize():
    assert hasattr(lobj::ResrcFile, "filesize")
    descriptor = None
    for klass in lobj::ResrcFile.__mro__:
        if "filesize" in klass.__dict__:
            descriptor = klass.__dict__["filesize"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfile_has_resrcHref():
    assert hasattr(lobj::ResrcFile, "resrcHref")
    descriptor = None
    for klass in lobj::ResrcFile.__mro__:
        if "resrcHref" in klass.__dict__:
            descriptor = klass.__dict__["resrcHref"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfile_has_originalextension():
    assert hasattr(lobj::ResrcFile, "originalextension")
    descriptor = None
    for klass in lobj::ResrcFile.__mro__:
        if "originalextension" in klass.__dict__:
            descriptor = klass.__dict__["originalextension"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfile_has_file_tn():
    assert hasattr(lobj::ResrcFile, "file_tn")
    descriptor = None
    for klass in lobj::ResrcFile.__mro__:
        if "file_tn" in klass.__dict__:
            descriptor = klass.__dict__["file_tn"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcfile_has_file():
    assert hasattr(lobj::ResrcFile, "file")
    descriptor = None
    for klass in lobj::ResrcFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_lobj::module_is_not_abstract():
    assert not inspect.isabstract(lobj::Module)


def test_lobj::module_constructor_exists():
    assert callable(lobj::Module.__init__)


def test_lobj::module_constructor_args():
    sig = inspect.signature(lobj::Module.__init__)
    params = list(sig.parameters.keys())
    assert "treeAsXml" in params, "Missing parameter 'treeAsXml'"
    assert "moduleFile" in params, "Missing parameter 'moduleFile'"

def test_lobj::module_has_treeAsXml():
    assert hasattr(lobj::Module, "treeAsXml")
    descriptor = None
    for klass in lobj::Module.__mro__:
        if "treeAsXml" in klass.__dict__:
            descriptor = klass.__dict__["treeAsXml"]
            break
    assert isinstance(descriptor, property)

def test_lobj::module_has_moduleFile():
    assert hasattr(lobj::Module, "moduleFile")
    descriptor = None
    for klass in lobj::Module.__mro__:
        if "moduleFile" in klass.__dict__:
            descriptor = klass.__dict__["moduleFile"]
            break
    assert isinstance(descriptor, property)



def test_lobj::theme_is_not_abstract():
    assert not inspect.isabstract(lobj::Theme)


def test_lobj::theme_constructor_exists():
    assert callable(lobj::Theme.__init__)


def test_lobj::theme_constructor_args():
    sig = inspect.signature(lobj::Theme.__init__)
    params = list(sig.parameters.keys())



def test_lobj::blockmeta_is_not_abstract():
    assert not inspect.isabstract(lobj::BlockMeta)


def test_lobj::blockmeta_constructor_exists():
    assert callable(lobj::BlockMeta.__init__)


def test_lobj::blockmeta_constructor_args():
    sig = inspect.signature(lobj::BlockMeta.__init__)
    params = list(sig.parameters.keys())
    assert "lastModified" in params, "Missing parameter 'lastModified'"
    assert "lod" in params, "Missing parameter 'lod'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "rendering" in params, "Missing parameter 'rendering'"

def test_lobj::blockmeta_has_lastModified():
    assert hasattr(lobj::BlockMeta, "lastModified")
    descriptor = None
    for klass in lobj::BlockMeta.__mro__:
        if "lastModified" in klass.__dict__:
            descriptor = klass.__dict__["lastModified"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blockmeta_has_lod():
    assert hasattr(lobj::BlockMeta, "lod")
    descriptor = None
    for klass in lobj::BlockMeta.__mro__:
        if "lod" in klass.__dict__:
            descriptor = klass.__dict__["lod"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blockmeta_has_creationDate():
    assert hasattr(lobj::BlockMeta, "creationDate")
    descriptor = None
    for klass in lobj::BlockMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj::blockmeta_has_rendering():
    assert hasattr(lobj::BlockMeta, "rendering")
    descriptor = None
    for klass in lobj::BlockMeta.__mro__:
        if "rendering" in klass.__dict__:
            descriptor = klass.__dict__["rendering"]
            break
    assert isinstance(descriptor, property)



def test_lobj::lufolder_is_not_abstract():
    assert not inspect.isabstract(lobj::LuFolder)


def test_lobj::lufolder_constructor_exists():
    assert callable(lobj::LuFolder.__init__)


def test_lobj::lufolder_constructor_args():
    sig = inspect.signature(lobj::LuFolder.__init__)
    params = list(sig.parameters.keys())



def test_lobj::resrcmeta_is_not_abstract():
    assert not inspect.isabstract(lobj::ResrcMeta)


def test_lobj::resrcmeta_constructor_exists():
    assert callable(lobj::ResrcMeta.__init__)


def test_lobj::resrcmeta_constructor_args():
    sig = inspect.signature(lobj::ResrcMeta.__init__)
    params = list(sig.parameters.keys())
    assert "lastModified" in params, "Missing parameter 'lastModified'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj::resrcmeta_has_lastModified():
    assert hasattr(lobj::ResrcMeta, "lastModified")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "lastModified" in klass.__dict__:
            descriptor = klass.__dict__["lastModified"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_description():
    assert hasattr(lobj::ResrcMeta, "description")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_title():
    assert hasattr(lobj::ResrcMeta, "title")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_filename():
    assert hasattr(lobj::ResrcMeta, "filename")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_keywords():
    assert hasattr(lobj::ResrcMeta, "keywords")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_parameters():
    assert hasattr(lobj::ResrcMeta, "parameters")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_width():
    assert hasattr(lobj::ResrcMeta, "width")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_height():
    assert hasattr(lobj::ResrcMeta, "height")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_lobj::resrcmeta_has_creationDate():
    assert hasattr(lobj::ResrcMeta, "creationDate")
    descriptor = None
    for klass in lobj::ResrcMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj::modulemeta_is_not_abstract():
    assert not inspect.isabstract(lobj::ModuleMeta)


def test_lobj::modulemeta_constructor_exists():
    assert callable(lobj::ModuleMeta.__init__)


def test_lobj::modulemeta_constructor_args():
    sig = inspect.signature(lobj::ModuleMeta.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj::modulemeta_has_creationDate():
    assert hasattr(lobj::ModuleMeta, "creationDate")
    descriptor = None
    for klass in lobj::ModuleMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj::modulefolder_is_not_abstract():
    assert not inspect.isabstract(lobj::ModuleFolder)


def test_lobj::modulefolder_constructor_exists():
    assert callable(lobj::ModuleFolder.__init__)


def test_lobj::modulefolder_constructor_args():
    sig = inspect.signature(lobj::ModuleFolder.__init__)
    params = list(sig.parameters.keys())



def test_lobj::category_is_not_abstract():
    assert not inspect.isabstract(lobj::Category)


def test_lobj::category_constructor_exists():
    assert callable(lobj::Category.__init__)


def test_lobj::category_constructor_args():
    sig = inspect.signature(lobj::Category.__init__)
    params = list(sig.parameters.keys())



def test_lobj::blockfolder_is_not_abstract():
    assert not inspect.isabstract(lobj::BlockFolder)


def test_lobj::blockfolder_constructor_exists():
    assert callable(lobj::BlockFolder.__init__)


def test_lobj::blockfolder_constructor_args():
    sig = inspect.signature(lobj::BlockFolder.__init__)
    params = list(sig.parameters.keys())



def test_lobj::course_is_not_abstract():
    assert not inspect.isabstract(lobj::Course)


def test_lobj::course_constructor_exists():
    assert callable(lobj::Course.__init__)


def test_lobj::course_constructor_args():
    sig = inspect.signature(lobj::Course.__init__)
    params = list(sig.parameters.keys())
    assert "outlineAsXml" in params, "Missing parameter 'outlineAsXml'"

def test_lobj::course_has_outlineAsXml():
    assert hasattr(lobj::Course, "outlineAsXml")
    descriptor = None
    for klass in lobj::Course.__mro__:
        if "outlineAsXml" in klass.__dict__:
            descriptor = klass.__dict__["outlineAsXml"]
            break
    assert isinstance(descriptor, property)



def test_lobj::resrcfolder_is_not_abstract():
    assert not inspect.isabstract(lobj::ResrcFolder)


def test_lobj::resrcfolder_constructor_exists():
    assert callable(lobj::ResrcFolder.__init__)


def test_lobj::resrcfolder_constructor_args():
    sig = inspect.signature(lobj::ResrcFolder.__init__)
    params = list(sig.parameters.keys())
    assert "deleteScheduled" in params, "Missing parameter 'deleteScheduled'"

def test_lobj::resrcfolder_has_deleteScheduled():
    assert hasattr(lobj::ResrcFolder, "deleteScheduled")
    descriptor = None
    for klass in lobj::ResrcFolder.__mro__:
        if "deleteScheduled" in klass.__dict__:
            descriptor = klass.__dict__["deleteScheduled"]
            break
    assert isinstance(descriptor, property)



def test_lobj::block_is_not_abstract():
    assert not inspect.isabstract(lobj::Block)


def test_lobj::block_constructor_exists():
    assert callable(lobj::Block.__init__)


def test_lobj::block_constructor_args():
    sig = inspect.signature(lobj::Block.__init__)
    params = list(sig.parameters.keys())



def test_lobj::learningobject_is_not_abstract():
    assert not inspect.isabstract(lobj::LearningObject)


def test_lobj::learningobject_constructor_exists():
    assert callable(lobj::LearningObject.__init__)


def test_lobj::learningobject_constructor_args():
    sig = inspect.signature(lobj::LearningObject.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_lobj::learningobject_has_timestamp():
    assert hasattr(lobj::LearningObject, "timestamp")
    descriptor = None
    for klass in lobj::LearningObject.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_lobj::learningobject_has_id():
    assert hasattr(lobj::LearningObject, "id")
    descriptor = None
    for klass in lobj::LearningObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj::learningobject_has_synchronized():
    assert hasattr(lobj::LearningObject, "synchronized")
    descriptor = None
    for klass in lobj::LearningObject.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_lobj::language_is_not_abstract():
    assert not inspect.isabstract(lobj::Language)


def test_lobj::language_constructor_exists():
    assert callable(lobj::Language.__init__)


def test_lobj::language_constructor_args():
    sig = inspect.signature(lobj::Language.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "code" in params, "Missing parameter 'code'"

def test_lobj::language_has_language():
    assert hasattr(lobj::Language, "language")
    descriptor = None
    for klass in lobj::Language.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_lobj::language_has_code():
    assert hasattr(lobj::Language, "code")
    descriptor = None
    for klass in lobj::Language.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_lobj::abstractcontent_is_not_abstract():
    assert not inspect.isabstract(lobj::AbstractContent)


def test_lobj::abstractcontent_constructor_exists():
    assert callable(lobj::AbstractContent.__init__)


def test_lobj::abstractcontent_constructor_args():
    sig = inspect.signature(lobj::AbstractContent.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"

def test_lobj::abstractcontent_has_heading():
    assert hasattr(lobj::AbstractContent, "heading")
    descriptor = None
    for klass in lobj::AbstractContent.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_lobj::hypertextcontent_is_not_abstract():
    assert not inspect.isabstract(lobj::HypertextContent)


def test_lobj::hypertextcontent_constructor_exists():
    assert callable(lobj::HypertextContent.__init__)


def test_lobj::hypertextcontent_constructor_args():
    sig = inspect.signature(lobj::HypertextContent.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_lobj::hypertextcontent_has_content():
    assert hasattr(lobj::HypertextContent, "content")
    descriptor = None
    for klass in lobj::HypertextContent.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_lobj::hypertextblock_is_not_abstract():
    assert not inspect.isabstract(lobj::HypertextBlock)


def test_lobj::hypertextblock_constructor_exists():
    assert callable(lobj::HypertextBlock.__init__)


def test_lobj::hypertextblock_constructor_args():
    sig = inspect.signature(lobj::HypertextBlock.__init__)
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
lobj::InternalRef_strategy = st.builds(
    lobj::InternalRef,
    id=
        safe_text,
    reftype=
        safe_text,
    ref=
        safe_text,
    file=
        safe_text
)
lobj::Publisher_strategy = st.builds(
    lobj::Publisher,
    publishername=
        safe_text,
    id=
        safe_text
)
lobj::PublishInfo_strategy = st.builds(
    lobj::PublishInfo,
    id=
        safe_text,
    pubsnumber=
        safe_text,
    pubdate=
        st.dates(),
    releaseinfo=
        safe_text,
    edition=
        safe_text
)
lobj::Note_strategy = st.builds(
    lobj::Note,
    noteAuthor=
        safe_text,
    date=
        st.dates(),
    id=
        safe_text,
    content=
        safe_text
)
lobj::AuthorizationTypes_strategy = st.builds(
    lobj::AuthorizationTypes,
    authType=
        safe_text,
    readOnly=
        st.booleans(),
    authTypeDesc=
        safe_text,
    id=
        safe_text
)
lobj::Precognition_strategy = st.builds(
    lobj::Precognition,
    id=
        safe_text,
    precog=
        safe_text
)
SimpleDidacMeta_strategy = st.builds(
    SimpleDidacMeta,
)
lobj::Domain_strategy = st.builds(
    lobj::Domain,
    creationDate=
        st.dates(),
    description=
        safe_text,
    serverURL=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
lobj::DidacMeta_strategy = st.builds(
    lobj::DidacMeta,
    goal=
        safe_text
)
lobj::Person_strategy = st.builds(
    lobj::Person,
    firstname=
        safe_text,
    honorific=
        safe_text,
    contrib=
        safe_text,
    personblurb=
        safe_text,
    id=
        safe_text,
    surname=
        safe_text
)
lobj::Author_strategy = st.builds(
    lobj::Author,
    credittype=
        safe_text,
    email=
        safe_text,
    id=
        safe_text
)
lobj::Blocktype_strategy = st.builds(
    lobj::Blocktype,
    creationDate=
        st.dates(),
    styleRef=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
lobj::Address_strategy = st.builds(
    lobj::Address,
    city=
        safe_text,
    email=
        safe_text,
    id=
        safe_text,
    phone=
        safe_text,
    fax=
        safe_text,
    country=
        safe_text,
    state=
        safe_text,
    street=
        safe_text,
    otheraddr=
        safe_text,
    postcode=
        safe_text
)
lobj::Edition_strategy = st.builds(
    lobj::Edition,
    lastVersionNumber=
        safe_text,
    id=
        safe_text,
    status=
        safe_text,
    editedBy=
        safe_text,
    version=
        safe_text,
    editionNr=
        safe_text,
    editionCreationDate=
        st.dates()
)
lobj::Userauthorization_strategy = st.builds(
    lobj::Userauthorization,
    id=
        safe_text
)
lobj::Affiliation_strategy = st.builds(
    lobj::Affiliation,
    shortaffil=
        safe_text,
    jobtitle=
        safe_text,
    orgdiv=
        safe_text,
    orgname=
        safe_text,
    id=
        safe_text
)
lobj::Sharednotes_strategy = st.builds(
    lobj::Sharednotes,
    id=
        safe_text
)
lobj::User_strategy = st.builds(
    lobj::User,
    entryasxml=
        safe_text,
    lastcoursematerialviewnr=
        safe_text,
    inchatsince=
        st.dates(),
    chatroomnr=
        safe_text,
    datafilter=
        safe_text,
    icqnumber=
        safe_text,
    languagenr=
        safe_text,
    scn=
        safe_text,
    contchatdate=
        st.dates(),
    lastname=
        safe_text,
    password=
        safe_text,
    icqpassword=
        safe_text,
    id=
        safe_text,
    onlinedate=
        st.dates(),
    fromext=
        safe_text,
    loginname=
        safe_text,
    notificationprofileasxml=
        safe_text,
    matriculationnr=
        safe_text,
    lastcoursematerialnr=
        safe_text,
    onlinestatus=
        safe_text,
    dossierasxml=
        safe_text,
    currlogindate=
        st.dates(),
    firstname=
        safe_text,
    photochanged=
        safe_text,
    photo=
        safe_text,
    authenticateldap=
        safe_text,
    lastlogindate=
        st.dates()
)
lobj::ResrcFiletype_strategy = st.builds(
    lobj::ResrcFiletype,
    applet=
        st.booleans(),
    filetypeExtension=
        safe_text,
    image=
        st.booleans(),
    filetypeDesc=
        safe_text,
    id=
        safe_text,
    filetypeImageBif=
        safe_text,
    filetypeImageSmall=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
lobj::ThemeNode_strategy = st.builds(
    lobj::ThemeNode,
)
lobj::LuNode_strategy = st.builds(
    lobj::LuNode,
)
lobj::SimpleDidacMeta_strategy = st.builds(
    lobj::SimpleDidacMeta,
    id=
        safe_text,
    description=
        safe_text,
    title=
        safe_text,
    keywords=
        safe_text
)
lobj::Node_strategy = st.builds(
    lobj::Node,
    visible=
        st.booleans(),
    id=
        safe_text
)
lobj::Item_strategy = st.builds(
    lobj::Item,
    id=
        safe_text,
    luRef=
        safe_text
)
lobj::Coursetype_strategy = st.builds(
    lobj::Coursetype,
    title=
        safe_text,
    id=
        safe_text,
    description=
        safe_text
)
lobj::PresentationBlock_strategy = st.builds(
    lobj::PresentationBlock,
    lod=
        st.integers(),
    id=
        safe_text,
    rendering=
        safe_text
)
AbstractContent_strategy = st.builds(
    AbstractContent,
)
lobj::Source_strategy = st.builds(
    lobj::Source,
    pp=
        safe_text,
    subtitle=
        safe_text,
    publishedIn=
        safe_text,
    id=
        safe_text,
    publishDate=
        safe_text,
    title=
        safe_text,
    publishedBy=
        safe_text
)
lobj::CorrBlock_strategy = st.builds(
    lobj::CorrBlock,
    id=
        safe_text
)
lobj::TitleMeta_strategy = st.builds(
    lobj::TitleMeta,
    id=
        safe_text,
    title=
        safe_text
)
lobj::AccessControl_strategy = st.builds(
    lobj::AccessControl,
    id=
        safe_text,
    globalAccess=
        st.booleans(),
    status=
        safe_text,
    lastStatusChange=
        st.dates(),
    lastModified=
        st.dates()
)
lobj::ExternalMetadata_strategy = st.builds(
    lobj::ExternalMetadata,
    file=
        safe_text,
    ref=
        safe_text,
    id=
        safe_text
)
LearningObject_strategy = st.builds(
    LearningObject,
)
lobj::BlockAudiofile_strategy = st.builds(
    lobj::BlockAudiofile,
    file=
        safe_text,
    filesize=
        st.integers(),
    originalextension=
        safe_text,
    resrcHref=
        safe_text
)
lobj::LuMeta_strategy = st.builds(
    lobj::LuMeta,
    creationDate=
        st.dates()
)
lobj::FolderMeta_strategy = st.builds(
    lobj::FolderMeta,
    creationDate=
        st.dates(),
    description=
        safe_text,
    title=
        safe_text
)
lobj::CourseMeta_strategy = st.builds(
    lobj::CourseMeta,
    columnfilterasxml=
        safe_text,
    hours=
        st.integers(),
    fromext=
        safe_text,
    lvanr=
        safe_text,
    creationDate=
        st.dates()
)
lobj::LearningUnit_strategy = st.builds(
    lobj::LearningUnit,
    luFile=
        safe_text,
    treeAsXml=
        safe_text
)
lobj::ResrcFile_strategy = st.builds(
    lobj::ResrcFile,
    filesize=
        st.integers(),
    resrcHref=
        safe_text,
    originalextension=
        safe_text,
    file_tn=
        safe_text,
    file=
        safe_text
)
lobj::Module_strategy = st.builds(
    lobj::Module,
    treeAsXml=
        safe_text,
    moduleFile=
        safe_text
)
lobj::Theme_strategy = st.builds(
    lobj::Theme,
)
lobj::BlockMeta_strategy = st.builds(
    lobj::BlockMeta,
    lastModified=
        st.dates(),
    lod=
        safe_text,
    creationDate=
        st.dates(),
    rendering=
        safe_text
)
lobj::LuFolder_strategy = st.builds(
    lobj::LuFolder,
)
lobj::ResrcMeta_strategy = st.builds(
    lobj::ResrcMeta,
    lastModified=
        st.dates(),
    description=
        safe_text,
    title=
        safe_text,
    filename=
        safe_text,
    keywords=
        safe_text,
    parameters=
        safe_text,
    width=
        st.integers(),
    height=
        st.integers(),
    creationDate=
        st.dates()
)
lobj::ModuleMeta_strategy = st.builds(
    lobj::ModuleMeta,
    creationDate=
        st.dates()
)
lobj::ModuleFolder_strategy = st.builds(
    lobj::ModuleFolder,
)
lobj::Category_strategy = st.builds(
    lobj::Category,
)
lobj::BlockFolder_strategy = st.builds(
    lobj::BlockFolder,
)
lobj::Course_strategy = st.builds(
    lobj::Course,
    outlineAsXml=
        safe_text
)
lobj::ResrcFolder_strategy = st.builds(
    lobj::ResrcFolder,
    deleteScheduled=
        st.booleans()
)
lobj::Block_strategy = st.builds(
    lobj::Block,
)
lobj::LearningObject_strategy = st.builds(
    lobj::LearningObject,
    timestamp=
        st.dates(),
    id=
        safe_text,
    synchronized=
        st.booleans()
)
lobj::Language_strategy = st.builds(
    lobj::Language,
    language=
        safe_text,
    code=
        safe_text
)
lobj::AbstractContent_strategy = st.builds(
    lobj::AbstractContent,
    heading=
        safe_text
)
lobj::HypertextContent_strategy = st.builds(
    lobj::HypertextContent,
    content=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
lobj::HypertextBlock_strategy = st.builds(
    lobj::HypertextBlock,
)

@given(instance=lobj::InternalRef_strategy)
@settings(max_examples=50)
def test_lobj::internalref_instantiation(instance):
    assert isinstance(instance, lobj::InternalRef)

@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_reftype_type(instance):
    assert isinstance(instance.reftype, str)


@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_reftype_setter(instance):
    original = instance.reftype
    instance.reftype = original
    assert instance.reftype == original

@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=lobj::InternalRef_strategy)
def test_lobj::internalref_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=lobj::Publisher_strategy)
@settings(max_examples=50)
def test_lobj::publisher_instantiation(instance):
    assert isinstance(instance, lobj::Publisher)

@given(instance=lobj::Publisher_strategy)
def test_lobj::publisher_publishername_type(instance):
    assert isinstance(instance.publishername, str)


@given(instance=lobj::Publisher_strategy)
def test_lobj::publisher_publishername_setter(instance):
    original = instance.publishername
    instance.publishername = original
    assert instance.publishername == original

@given(instance=lobj::Publisher_strategy)
def test_lobj::publisher_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Publisher_strategy)
def test_lobj::publisher_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::PublishInfo_strategy)
@settings(max_examples=50)
def test_lobj::publishinfo_instantiation(instance):
    assert isinstance(instance, lobj::PublishInfo)

@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_pubsnumber_type(instance):
    assert isinstance(instance.pubsnumber, str)


@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_pubsnumber_setter(instance):
    original = instance.pubsnumber
    instance.pubsnumber = original
    assert instance.pubsnumber == original

@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_pubdate_type(instance):
    assert isinstance(instance.pubdate, date)


@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original

@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_releaseinfo_type(instance):
    assert isinstance(instance.releaseinfo, str)


@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_releaseinfo_setter(instance):
    original = instance.releaseinfo
    instance.releaseinfo = original
    assert instance.releaseinfo == original

@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=lobj::PublishInfo_strategy)
def test_lobj::publishinfo_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=lobj::Note_strategy)
@settings(max_examples=50)
def test_lobj::note_instantiation(instance):
    assert isinstance(instance, lobj::Note)

@given(instance=lobj::Note_strategy)
def test_lobj::note_noteAuthor_type(instance):
    assert isinstance(instance.noteAuthor, str)


@given(instance=lobj::Note_strategy)
def test_lobj::note_noteAuthor_setter(instance):
    original = instance.noteAuthor
    instance.noteAuthor = original
    assert instance.noteAuthor == original

@given(instance=lobj::Note_strategy)
def test_lobj::note_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=lobj::Note_strategy)
def test_lobj::note_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=lobj::Note_strategy)
def test_lobj::note_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Note_strategy)
def test_lobj::note_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Note_strategy)
def test_lobj::note_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=lobj::Note_strategy)
def test_lobj::note_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=lobj::AuthorizationTypes_strategy)
@settings(max_examples=50)
def test_lobj::authorizationtypes_instantiation(instance):
    assert isinstance(instance, lobj::AuthorizationTypes)

@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_authType_type(instance):
    assert isinstance(instance.authType, str)


@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_authType_setter(instance):
    original = instance.authType
    instance.authType = original
    assert instance.authType == original

@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_authTypeDesc_type(instance):
    assert isinstance(instance.authTypeDesc, str)


@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_authTypeDesc_setter(instance):
    original = instance.authTypeDesc
    instance.authTypeDesc = original
    assert instance.authTypeDesc == original

@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::AuthorizationTypes_strategy)
def test_lobj::authorizationtypes_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Precognition_strategy)
@settings(max_examples=50)
def test_lobj::precognition_instantiation(instance):
    assert isinstance(instance, lobj::Precognition)

@given(instance=lobj::Precognition_strategy)
def test_lobj::precognition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Precognition_strategy)
def test_lobj::precognition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Precognition_strategy)
def test_lobj::precognition_precog_type(instance):
    assert isinstance(instance.precog, str)


@given(instance=lobj::Precognition_strategy)
def test_lobj::precognition_precog_setter(instance):
    original = instance.precog
    instance.precog = original
    assert instance.precog == original

@given(instance=SimpleDidacMeta_strategy)
@settings(max_examples=50)
def test_simpledidacmeta_instantiation(instance):
    assert isinstance(instance, SimpleDidacMeta)

@given(instance=lobj::Domain_strategy)
@settings(max_examples=50)
def test_lobj::domain_instantiation(instance):
    assert isinstance(instance, lobj::Domain)

@given(instance=lobj::Domain_strategy)
def test_lobj::domain_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::Domain_strategy)
def test_lobj::domain_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::Domain_strategy)
def test_lobj::domain_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lobj::Domain_strategy)
def test_lobj::domain_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj::Domain_strategy)
def test_lobj::domain_serverURL_type(instance):
    assert isinstance(instance.serverURL, str)


@given(instance=lobj::Domain_strategy)
def test_lobj::domain_serverURL_setter(instance):
    original = instance.serverURL
    instance.serverURL = original
    assert instance.serverURL == original

@given(instance=lobj::Domain_strategy)
def test_lobj::domain_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Domain_strategy)
def test_lobj::domain_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Domain_strategy)
def test_lobj::domain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lobj::Domain_strategy)
def test_lobj::domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lobj::DidacMeta_strategy)
@settings(max_examples=50)
def test_lobj::didacmeta_instantiation(instance):
    assert isinstance(instance, lobj::DidacMeta)

@given(instance=lobj::DidacMeta_strategy)
def test_lobj::didacmeta_goal_type(instance):
    assert isinstance(instance.goal, str)


@given(instance=lobj::DidacMeta_strategy)
def test_lobj::didacmeta_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original

@given(instance=lobj::Person_strategy)
@settings(max_examples=50)
def test_lobj::person_instantiation(instance):
    assert isinstance(instance, lobj::Person)

@given(instance=lobj::Person_strategy)
def test_lobj::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=lobj::Person_strategy)
def test_lobj::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=lobj::Person_strategy)
def test_lobj::person_honorific_type(instance):
    assert isinstance(instance.honorific, str)


@given(instance=lobj::Person_strategy)
def test_lobj::person_honorific_setter(instance):
    original = instance.honorific
    instance.honorific = original
    assert instance.honorific == original

@given(instance=lobj::Person_strategy)
def test_lobj::person_contrib_type(instance):
    assert isinstance(instance.contrib, str)


@given(instance=lobj::Person_strategy)
def test_lobj::person_contrib_setter(instance):
    original = instance.contrib
    instance.contrib = original
    assert instance.contrib == original

@given(instance=lobj::Person_strategy)
def test_lobj::person_personblurb_type(instance):
    assert isinstance(instance.personblurb, str)


@given(instance=lobj::Person_strategy)
def test_lobj::person_personblurb_setter(instance):
    original = instance.personblurb
    instance.personblurb = original
    assert instance.personblurb == original

@given(instance=lobj::Person_strategy)
def test_lobj::person_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Person_strategy)
def test_lobj::person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Person_strategy)
def test_lobj::person_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=lobj::Person_strategy)
def test_lobj::person_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=lobj::Author_strategy)
@settings(max_examples=50)
def test_lobj::author_instantiation(instance):
    assert isinstance(instance, lobj::Author)

@given(instance=lobj::Author_strategy)
def test_lobj::author_credittype_type(instance):
    assert isinstance(instance.credittype, str)


@given(instance=lobj::Author_strategy)
def test_lobj::author_credittype_setter(instance):
    original = instance.credittype
    instance.credittype = original
    assert instance.credittype == original

@given(instance=lobj::Author_strategy)
def test_lobj::author_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=lobj::Author_strategy)
def test_lobj::author_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=lobj::Author_strategy)
def test_lobj::author_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Author_strategy)
def test_lobj::author_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Blocktype_strategy)
@settings(max_examples=50)
def test_lobj::blocktype_instantiation(instance):
    assert isinstance(instance, lobj::Blocktype)

@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_styleRef_type(instance):
    assert isinstance(instance.styleRef, str)


@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_styleRef_setter(instance):
    original = instance.styleRef
    instance.styleRef = original
    assert instance.styleRef == original

@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Blocktype_strategy)
def test_lobj::blocktype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Address_strategy)
@settings(max_examples=50)
def test_lobj::address_instantiation(instance):
    assert isinstance(instance, lobj::Address)

@given(instance=lobj::Address_strategy)
def test_lobj::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_phone_type(instance):
    assert isinstance(instance.phone, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_fax_type(instance):
    assert isinstance(instance.fax, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_fax_setter(instance):
    original = instance.fax
    instance.fax = original
    assert instance.fax == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_otheraddr_type(instance):
    assert isinstance(instance.otheraddr, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_otheraddr_setter(instance):
    original = instance.otheraddr
    instance.otheraddr = original
    assert instance.otheraddr == original

@given(instance=lobj::Address_strategy)
def test_lobj::address_postcode_type(instance):
    assert isinstance(instance.postcode, str)


@given(instance=lobj::Address_strategy)
def test_lobj::address_postcode_setter(instance):
    original = instance.postcode
    instance.postcode = original
    assert instance.postcode == original

@given(instance=lobj::Edition_strategy)
@settings(max_examples=50)
def test_lobj::edition_instantiation(instance):
    assert isinstance(instance, lobj::Edition)

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_lastVersionNumber_type(instance):
    assert isinstance(instance.lastVersionNumber, str)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_lastVersionNumber_setter(instance):
    original = instance.lastVersionNumber
    instance.lastVersionNumber = original
    assert instance.lastVersionNumber == original

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_editedBy_type(instance):
    assert isinstance(instance.editedBy, str)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_editedBy_setter(instance):
    original = instance.editedBy
    instance.editedBy = original
    assert instance.editedBy == original

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_editionNr_type(instance):
    assert isinstance(instance.editionNr, str)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_editionNr_setter(instance):
    original = instance.editionNr
    instance.editionNr = original
    assert instance.editionNr == original

@given(instance=lobj::Edition_strategy)
def test_lobj::edition_editionCreationDate_type(instance):
    assert isinstance(instance.editionCreationDate, date)


@given(instance=lobj::Edition_strategy)
def test_lobj::edition_editionCreationDate_setter(instance):
    original = instance.editionCreationDate
    instance.editionCreationDate = original
    assert instance.editionCreationDate == original

@given(instance=lobj::Userauthorization_strategy)
@settings(max_examples=50)
def test_lobj::userauthorization_instantiation(instance):
    assert isinstance(instance, lobj::Userauthorization)

@given(instance=lobj::Userauthorization_strategy)
def test_lobj::userauthorization_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Userauthorization_strategy)
def test_lobj::userauthorization_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Affiliation_strategy)
@settings(max_examples=50)
def test_lobj::affiliation_instantiation(instance):
    assert isinstance(instance, lobj::Affiliation)

@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_shortaffil_type(instance):
    assert isinstance(instance.shortaffil, str)


@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_shortaffil_setter(instance):
    original = instance.shortaffil
    instance.shortaffil = original
    assert instance.shortaffil == original

@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_jobtitle_type(instance):
    assert isinstance(instance.jobtitle, str)


@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_jobtitle_setter(instance):
    original = instance.jobtitle
    instance.jobtitle = original
    assert instance.jobtitle == original

@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_orgdiv_type(instance):
    assert isinstance(instance.orgdiv, str)


@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_orgdiv_setter(instance):
    original = instance.orgdiv
    instance.orgdiv = original
    assert instance.orgdiv == original

@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_orgname_type(instance):
    assert isinstance(instance.orgname, str)


@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_orgname_setter(instance):
    original = instance.orgname
    instance.orgname = original
    assert instance.orgname == original

@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Affiliation_strategy)
def test_lobj::affiliation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Sharednotes_strategy)
@settings(max_examples=50)
def test_lobj::sharednotes_instantiation(instance):
    assert isinstance(instance, lobj::Sharednotes)

@given(instance=lobj::Sharednotes_strategy)
def test_lobj::sharednotes_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Sharednotes_strategy)
def test_lobj::sharednotes_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::User_strategy)
@settings(max_examples=50)
def test_lobj::user_instantiation(instance):
    assert isinstance(instance, lobj::User)

@given(instance=lobj::User_strategy)
def test_lobj::user_entryasxml_type(instance):
    assert isinstance(instance.entryasxml, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_entryasxml_setter(instance):
    original = instance.entryasxml
    instance.entryasxml = original
    assert instance.entryasxml == original

@given(instance=lobj::User_strategy)
def test_lobj::user_lastcoursematerialviewnr_type(instance):
    assert isinstance(instance.lastcoursematerialviewnr, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_lastcoursematerialviewnr_setter(instance):
    original = instance.lastcoursematerialviewnr
    instance.lastcoursematerialviewnr = original
    assert instance.lastcoursematerialviewnr == original

@given(instance=lobj::User_strategy)
def test_lobj::user_inchatsince_type(instance):
    assert isinstance(instance.inchatsince, date)


@given(instance=lobj::User_strategy)
def test_lobj::user_inchatsince_setter(instance):
    original = instance.inchatsince
    instance.inchatsince = original
    assert instance.inchatsince == original

@given(instance=lobj::User_strategy)
def test_lobj::user_chatroomnr_type(instance):
    assert isinstance(instance.chatroomnr, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_chatroomnr_setter(instance):
    original = instance.chatroomnr
    instance.chatroomnr = original
    assert instance.chatroomnr == original

@given(instance=lobj::User_strategy)
def test_lobj::user_datafilter_type(instance):
    assert isinstance(instance.datafilter, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_datafilter_setter(instance):
    original = instance.datafilter
    instance.datafilter = original
    assert instance.datafilter == original

@given(instance=lobj::User_strategy)
def test_lobj::user_icqnumber_type(instance):
    assert isinstance(instance.icqnumber, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_icqnumber_setter(instance):
    original = instance.icqnumber
    instance.icqnumber = original
    assert instance.icqnumber == original

@given(instance=lobj::User_strategy)
def test_lobj::user_languagenr_type(instance):
    assert isinstance(instance.languagenr, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_languagenr_setter(instance):
    original = instance.languagenr
    instance.languagenr = original
    assert instance.languagenr == original

@given(instance=lobj::User_strategy)
def test_lobj::user_scn_type(instance):
    assert isinstance(instance.scn, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_scn_setter(instance):
    original = instance.scn
    instance.scn = original
    assert instance.scn == original

@given(instance=lobj::User_strategy)
def test_lobj::user_contchatdate_type(instance):
    assert isinstance(instance.contchatdate, date)


@given(instance=lobj::User_strategy)
def test_lobj::user_contchatdate_setter(instance):
    original = instance.contchatdate
    instance.contchatdate = original
    assert instance.contchatdate == original

@given(instance=lobj::User_strategy)
def test_lobj::user_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=lobj::User_strategy)
def test_lobj::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=lobj::User_strategy)
def test_lobj::user_icqpassword_type(instance):
    assert isinstance(instance.icqpassword, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_icqpassword_setter(instance):
    original = instance.icqpassword
    instance.icqpassword = original
    assert instance.icqpassword == original

@given(instance=lobj::User_strategy)
def test_lobj::user_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::User_strategy)
def test_lobj::user_onlinedate_type(instance):
    assert isinstance(instance.onlinedate, date)


@given(instance=lobj::User_strategy)
def test_lobj::user_onlinedate_setter(instance):
    original = instance.onlinedate
    instance.onlinedate = original
    assert instance.onlinedate == original

@given(instance=lobj::User_strategy)
def test_lobj::user_fromext_type(instance):
    assert isinstance(instance.fromext, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_fromext_setter(instance):
    original = instance.fromext
    instance.fromext = original
    assert instance.fromext == original

@given(instance=lobj::User_strategy)
def test_lobj::user_loginname_type(instance):
    assert isinstance(instance.loginname, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_loginname_setter(instance):
    original = instance.loginname
    instance.loginname = original
    assert instance.loginname == original

@given(instance=lobj::User_strategy)
def test_lobj::user_notificationprofileasxml_type(instance):
    assert isinstance(instance.notificationprofileasxml, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_notificationprofileasxml_setter(instance):
    original = instance.notificationprofileasxml
    instance.notificationprofileasxml = original
    assert instance.notificationprofileasxml == original

@given(instance=lobj::User_strategy)
def test_lobj::user_matriculationnr_type(instance):
    assert isinstance(instance.matriculationnr, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_matriculationnr_setter(instance):
    original = instance.matriculationnr
    instance.matriculationnr = original
    assert instance.matriculationnr == original

@given(instance=lobj::User_strategy)
def test_lobj::user_lastcoursematerialnr_type(instance):
    assert isinstance(instance.lastcoursematerialnr, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_lastcoursematerialnr_setter(instance):
    original = instance.lastcoursematerialnr
    instance.lastcoursematerialnr = original
    assert instance.lastcoursematerialnr == original

@given(instance=lobj::User_strategy)
def test_lobj::user_onlinestatus_type(instance):
    assert isinstance(instance.onlinestatus, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_onlinestatus_setter(instance):
    original = instance.onlinestatus
    instance.onlinestatus = original
    assert instance.onlinestatus == original

@given(instance=lobj::User_strategy)
def test_lobj::user_dossierasxml_type(instance):
    assert isinstance(instance.dossierasxml, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_dossierasxml_setter(instance):
    original = instance.dossierasxml
    instance.dossierasxml = original
    assert instance.dossierasxml == original

@given(instance=lobj::User_strategy)
def test_lobj::user_currlogindate_type(instance):
    assert isinstance(instance.currlogindate, date)


@given(instance=lobj::User_strategy)
def test_lobj::user_currlogindate_setter(instance):
    original = instance.currlogindate
    instance.currlogindate = original
    assert instance.currlogindate == original

@given(instance=lobj::User_strategy)
def test_lobj::user_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=lobj::User_strategy)
def test_lobj::user_photochanged_type(instance):
    assert isinstance(instance.photochanged, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_photochanged_setter(instance):
    original = instance.photochanged
    instance.photochanged = original
    assert instance.photochanged == original

@given(instance=lobj::User_strategy)
def test_lobj::user_photo_type(instance):
    assert isinstance(instance.photo, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_photo_setter(instance):
    original = instance.photo
    instance.photo = original
    assert instance.photo == original

@given(instance=lobj::User_strategy)
def test_lobj::user_authenticateldap_type(instance):
    assert isinstance(instance.authenticateldap, str)


@given(instance=lobj::User_strategy)
def test_lobj::user_authenticateldap_setter(instance):
    original = instance.authenticateldap
    instance.authenticateldap = original
    assert instance.authenticateldap == original

@given(instance=lobj::User_strategy)
def test_lobj::user_lastlogindate_type(instance):
    assert isinstance(instance.lastlogindate, date)


@given(instance=lobj::User_strategy)
def test_lobj::user_lastlogindate_setter(instance):
    original = instance.lastlogindate
    instance.lastlogindate = original
    assert instance.lastlogindate == original

@given(instance=lobj::ResrcFiletype_strategy)
@settings(max_examples=50)
def test_lobj::resrcfiletype_instantiation(instance):
    assert isinstance(instance, lobj::ResrcFiletype)

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_applet_type(instance):
    assert isinstance(instance.applet, bool)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_applet_setter(instance):
    original = instance.applet
    instance.applet = original
    assert instance.applet == original

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeExtension_type(instance):
    assert isinstance(instance.filetypeExtension, str)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeExtension_setter(instance):
    original = instance.filetypeExtension
    instance.filetypeExtension = original
    assert instance.filetypeExtension == original

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_image_type(instance):
    assert isinstance(instance.image, bool)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeDesc_type(instance):
    assert isinstance(instance.filetypeDesc, str)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeDesc_setter(instance):
    original = instance.filetypeDesc
    instance.filetypeDesc = original
    assert instance.filetypeDesc == original

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeImageBif_type(instance):
    assert isinstance(instance.filetypeImageBif, str)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeImageBif_setter(instance):
    original = instance.filetypeImageBif
    instance.filetypeImageBif = original
    assert instance.filetypeImageBif == original

@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeImageSmall_type(instance):
    assert isinstance(instance.filetypeImageSmall, str)


@given(instance=lobj::ResrcFiletype_strategy)
def test_lobj::resrcfiletype_filetypeImageSmall_setter(instance):
    original = instance.filetypeImageSmall
    instance.filetypeImageSmall = original
    assert instance.filetypeImageSmall == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=lobj::ThemeNode_strategy)
@settings(max_examples=50)
def test_lobj::themenode_instantiation(instance):
    assert isinstance(instance, lobj::ThemeNode)

@given(instance=lobj::LuNode_strategy)
@settings(max_examples=50)
def test_lobj::lunode_instantiation(instance):
    assert isinstance(instance, lobj::LuNode)

@given(instance=lobj::SimpleDidacMeta_strategy)
@settings(max_examples=50)
def test_lobj::simpledidacmeta_instantiation(instance):
    assert isinstance(instance, lobj::SimpleDidacMeta)

@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=lobj::SimpleDidacMeta_strategy)
def test_lobj::simpledidacmeta_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=lobj::Node_strategy)
@settings(max_examples=50)
def test_lobj::node_instantiation(instance):
    assert isinstance(instance, lobj::Node)

@given(instance=lobj::Node_strategy)
def test_lobj::node_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=lobj::Node_strategy)
def test_lobj::node_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=lobj::Node_strategy)
def test_lobj::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Node_strategy)
def test_lobj::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Item_strategy)
@settings(max_examples=50)
def test_lobj::item_instantiation(instance):
    assert isinstance(instance, lobj::Item)

@given(instance=lobj::Item_strategy)
def test_lobj::item_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Item_strategy)
def test_lobj::item_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Item_strategy)
def test_lobj::item_luRef_type(instance):
    assert isinstance(instance.luRef, str)


@given(instance=lobj::Item_strategy)
def test_lobj::item_luRef_setter(instance):
    original = instance.luRef
    instance.luRef = original
    assert instance.luRef == original

@given(instance=lobj::Coursetype_strategy)
@settings(max_examples=50)
def test_lobj::coursetype_instantiation(instance):
    assert isinstance(instance, lobj::Coursetype)

@given(instance=lobj::Coursetype_strategy)
def test_lobj::coursetype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lobj::Coursetype_strategy)
def test_lobj::coursetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj::Coursetype_strategy)
def test_lobj::coursetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Coursetype_strategy)
def test_lobj::coursetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Coursetype_strategy)
def test_lobj::coursetype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lobj::Coursetype_strategy)
def test_lobj::coursetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj::PresentationBlock_strategy)
@settings(max_examples=50)
def test_lobj::presentationblock_instantiation(instance):
    assert isinstance(instance, lobj::PresentationBlock)

@given(instance=lobj::PresentationBlock_strategy)
def test_lobj::presentationblock_lod_type(instance):
    assert isinstance(instance.lod, int)


@given(instance=lobj::PresentationBlock_strategy)
def test_lobj::presentationblock_lod_setter(instance):
    original = instance.lod
    instance.lod = original
    assert instance.lod == original

@given(instance=lobj::PresentationBlock_strategy)
def test_lobj::presentationblock_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::PresentationBlock_strategy)
def test_lobj::presentationblock_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::PresentationBlock_strategy)
def test_lobj::presentationblock_rendering_type(instance):
    assert isinstance(instance.rendering, str)


@given(instance=lobj::PresentationBlock_strategy)
def test_lobj::presentationblock_rendering_setter(instance):
    original = instance.rendering
    instance.rendering = original
    assert instance.rendering == original

@given(instance=AbstractContent_strategy)
@settings(max_examples=50)
def test_abstractcontent_instantiation(instance):
    assert isinstance(instance, AbstractContent)

@given(instance=lobj::Source_strategy)
@settings(max_examples=50)
def test_lobj::source_instantiation(instance):
    assert isinstance(instance, lobj::Source)

@given(instance=lobj::Source_strategy)
def test_lobj::source_pp_type(instance):
    assert isinstance(instance.pp, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_pp_setter(instance):
    original = instance.pp
    instance.pp = original
    assert instance.pp == original

@given(instance=lobj::Source_strategy)
def test_lobj::source_subtitle_type(instance):
    assert isinstance(instance.subtitle, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_subtitle_setter(instance):
    original = instance.subtitle
    instance.subtitle = original
    assert instance.subtitle == original

@given(instance=lobj::Source_strategy)
def test_lobj::source_publishedIn_type(instance):
    assert isinstance(instance.publishedIn, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_publishedIn_setter(instance):
    original = instance.publishedIn
    instance.publishedIn = original
    assert instance.publishedIn == original

@given(instance=lobj::Source_strategy)
def test_lobj::source_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::Source_strategy)
def test_lobj::source_publishDate_type(instance):
    assert isinstance(instance.publishDate, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_publishDate_setter(instance):
    original = instance.publishDate
    instance.publishDate = original
    assert instance.publishDate == original

@given(instance=lobj::Source_strategy)
def test_lobj::source_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj::Source_strategy)
def test_lobj::source_publishedBy_type(instance):
    assert isinstance(instance.publishedBy, str)


@given(instance=lobj::Source_strategy)
def test_lobj::source_publishedBy_setter(instance):
    original = instance.publishedBy
    instance.publishedBy = original
    assert instance.publishedBy == original

@given(instance=lobj::CorrBlock_strategy)
@settings(max_examples=50)
def test_lobj::corrblock_instantiation(instance):
    assert isinstance(instance, lobj::CorrBlock)

@given(instance=lobj::CorrBlock_strategy)
def test_lobj::corrblock_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::CorrBlock_strategy)
def test_lobj::corrblock_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::TitleMeta_strategy)
@settings(max_examples=50)
def test_lobj::titlemeta_instantiation(instance):
    assert isinstance(instance, lobj::TitleMeta)

@given(instance=lobj::TitleMeta_strategy)
def test_lobj::titlemeta_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::TitleMeta_strategy)
def test_lobj::titlemeta_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::TitleMeta_strategy)
def test_lobj::titlemeta_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lobj::TitleMeta_strategy)
def test_lobj::titlemeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj::AccessControl_strategy)
@settings(max_examples=50)
def test_lobj::accesscontrol_instantiation(instance):
    assert isinstance(instance, lobj::AccessControl)

@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_globalAccess_type(instance):
    assert isinstance(instance.globalAccess, bool)


@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_globalAccess_setter(instance):
    original = instance.globalAccess
    instance.globalAccess = original
    assert instance.globalAccess == original

@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_lastStatusChange_type(instance):
    assert isinstance(instance.lastStatusChange, date)


@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_lastStatusChange_setter(instance):
    original = instance.lastStatusChange
    instance.lastStatusChange = original
    assert instance.lastStatusChange == original

@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_lastModified_type(instance):
    assert isinstance(instance.lastModified, date)


@given(instance=lobj::AccessControl_strategy)
def test_lobj::accesscontrol_lastModified_setter(instance):
    original = instance.lastModified
    instance.lastModified = original
    assert instance.lastModified == original

@given(instance=lobj::ExternalMetadata_strategy)
@settings(max_examples=50)
def test_lobj::externalmetadata_instantiation(instance):
    assert isinstance(instance, lobj::ExternalMetadata)

@given(instance=lobj::ExternalMetadata_strategy)
def test_lobj::externalmetadata_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=lobj::ExternalMetadata_strategy)
def test_lobj::externalmetadata_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=lobj::ExternalMetadata_strategy)
def test_lobj::externalmetadata_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=lobj::ExternalMetadata_strategy)
def test_lobj::externalmetadata_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=lobj::ExternalMetadata_strategy)
def test_lobj::externalmetadata_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::ExternalMetadata_strategy)
def test_lobj::externalmetadata_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=LearningObject_strategy)
@settings(max_examples=50)
def test_learningobject_instantiation(instance):
    assert isinstance(instance, LearningObject)

@given(instance=lobj::BlockAudiofile_strategy)
@settings(max_examples=50)
def test_lobj::blockaudiofile_instantiation(instance):
    assert isinstance(instance, lobj::BlockAudiofile)

@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_filesize_type(instance):
    assert isinstance(instance.filesize, int)


@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_filesize_setter(instance):
    original = instance.filesize
    instance.filesize = original
    assert instance.filesize == original

@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_originalextension_type(instance):
    assert isinstance(instance.originalextension, str)


@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_originalextension_setter(instance):
    original = instance.originalextension
    instance.originalextension = original
    assert instance.originalextension == original

@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_resrcHref_type(instance):
    assert isinstance(instance.resrcHref, str)


@given(instance=lobj::BlockAudiofile_strategy)
def test_lobj::blockaudiofile_resrcHref_setter(instance):
    original = instance.resrcHref
    instance.resrcHref = original
    assert instance.resrcHref == original

@given(instance=lobj::LuMeta_strategy)
@settings(max_examples=50)
def test_lobj::lumeta_instantiation(instance):
    assert isinstance(instance, lobj::LuMeta)

@given(instance=lobj::LuMeta_strategy)
def test_lobj::lumeta_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::LuMeta_strategy)
def test_lobj::lumeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::FolderMeta_strategy)
@settings(max_examples=50)
def test_lobj::foldermeta_instantiation(instance):
    assert isinstance(instance, lobj::FolderMeta)

@given(instance=lobj::FolderMeta_strategy)
def test_lobj::foldermeta_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::FolderMeta_strategy)
def test_lobj::foldermeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::FolderMeta_strategy)
def test_lobj::foldermeta_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lobj::FolderMeta_strategy)
def test_lobj::foldermeta_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj::FolderMeta_strategy)
def test_lobj::foldermeta_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lobj::FolderMeta_strategy)
def test_lobj::foldermeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj::CourseMeta_strategy)
@settings(max_examples=50)
def test_lobj::coursemeta_instantiation(instance):
    assert isinstance(instance, lobj::CourseMeta)

@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_columnfilterasxml_type(instance):
    assert isinstance(instance.columnfilterasxml, str)


@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_columnfilterasxml_setter(instance):
    original = instance.columnfilterasxml
    instance.columnfilterasxml = original
    assert instance.columnfilterasxml == original

@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_hours_type(instance):
    assert isinstance(instance.hours, int)


@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original

@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_fromext_type(instance):
    assert isinstance(instance.fromext, str)


@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_fromext_setter(instance):
    original = instance.fromext
    instance.fromext = original
    assert instance.fromext == original

@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_lvanr_type(instance):
    assert isinstance(instance.lvanr, str)


@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_lvanr_setter(instance):
    original = instance.lvanr
    instance.lvanr = original
    assert instance.lvanr == original

@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::CourseMeta_strategy)
def test_lobj::coursemeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::LearningUnit_strategy)
@settings(max_examples=50)
def test_lobj::learningunit_instantiation(instance):
    assert isinstance(instance, lobj::LearningUnit)

@given(instance=lobj::LearningUnit_strategy)
def test_lobj::learningunit_luFile_type(instance):
    assert isinstance(instance.luFile, str)


@given(instance=lobj::LearningUnit_strategy)
def test_lobj::learningunit_luFile_setter(instance):
    original = instance.luFile
    instance.luFile = original
    assert instance.luFile == original

@given(instance=lobj::LearningUnit_strategy)
def test_lobj::learningunit_treeAsXml_type(instance):
    assert isinstance(instance.treeAsXml, str)


@given(instance=lobj::LearningUnit_strategy)
def test_lobj::learningunit_treeAsXml_setter(instance):
    original = instance.treeAsXml
    instance.treeAsXml = original
    assert instance.treeAsXml == original

@given(instance=lobj::ResrcFile_strategy)
@settings(max_examples=50)
def test_lobj::resrcfile_instantiation(instance):
    assert isinstance(instance, lobj::ResrcFile)

@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_filesize_type(instance):
    assert isinstance(instance.filesize, int)


@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_filesize_setter(instance):
    original = instance.filesize
    instance.filesize = original
    assert instance.filesize == original

@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_resrcHref_type(instance):
    assert isinstance(instance.resrcHref, str)


@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_resrcHref_setter(instance):
    original = instance.resrcHref
    instance.resrcHref = original
    assert instance.resrcHref == original

@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_originalextension_type(instance):
    assert isinstance(instance.originalextension, str)


@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_originalextension_setter(instance):
    original = instance.originalextension
    instance.originalextension = original
    assert instance.originalextension == original

@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_file_tn_type(instance):
    assert isinstance(instance.file_tn, str)


@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_file_tn_setter(instance):
    original = instance.file_tn
    instance.file_tn = original
    assert instance.file_tn == original

@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=lobj::ResrcFile_strategy)
def test_lobj::resrcfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=lobj::Module_strategy)
@settings(max_examples=50)
def test_lobj::module_instantiation(instance):
    assert isinstance(instance, lobj::Module)

@given(instance=lobj::Module_strategy)
def test_lobj::module_treeAsXml_type(instance):
    assert isinstance(instance.treeAsXml, str)


@given(instance=lobj::Module_strategy)
def test_lobj::module_treeAsXml_setter(instance):
    original = instance.treeAsXml
    instance.treeAsXml = original
    assert instance.treeAsXml == original

@given(instance=lobj::Module_strategy)
def test_lobj::module_moduleFile_type(instance):
    assert isinstance(instance.moduleFile, str)


@given(instance=lobj::Module_strategy)
def test_lobj::module_moduleFile_setter(instance):
    original = instance.moduleFile
    instance.moduleFile = original
    assert instance.moduleFile == original

@given(instance=lobj::Theme_strategy)
@settings(max_examples=50)
def test_lobj::theme_instantiation(instance):
    assert isinstance(instance, lobj::Theme)

@given(instance=lobj::BlockMeta_strategy)
@settings(max_examples=50)
def test_lobj::blockmeta_instantiation(instance):
    assert isinstance(instance, lobj::BlockMeta)

@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_lastModified_type(instance):
    assert isinstance(instance.lastModified, date)


@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_lastModified_setter(instance):
    original = instance.lastModified
    instance.lastModified = original
    assert instance.lastModified == original

@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_lod_type(instance):
    assert isinstance(instance.lod, str)


@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_lod_setter(instance):
    original = instance.lod
    instance.lod = original
    assert instance.lod == original

@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_rendering_type(instance):
    assert isinstance(instance.rendering, str)


@given(instance=lobj::BlockMeta_strategy)
def test_lobj::blockmeta_rendering_setter(instance):
    original = instance.rendering
    instance.rendering = original
    assert instance.rendering == original

@given(instance=lobj::LuFolder_strategy)
@settings(max_examples=50)
def test_lobj::lufolder_instantiation(instance):
    assert isinstance(instance, lobj::LuFolder)

@given(instance=lobj::ResrcMeta_strategy)
@settings(max_examples=50)
def test_lobj::resrcmeta_instantiation(instance):
    assert isinstance(instance, lobj::ResrcMeta)

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_lastModified_type(instance):
    assert isinstance(instance.lastModified, date)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_lastModified_setter(instance):
    original = instance.lastModified
    instance.lastModified = original
    assert instance.lastModified == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::ResrcMeta_strategy)
def test_lobj::resrcmeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::ModuleMeta_strategy)
@settings(max_examples=50)
def test_lobj::modulemeta_instantiation(instance):
    assert isinstance(instance, lobj::ModuleMeta)

@given(instance=lobj::ModuleMeta_strategy)
def test_lobj::modulemeta_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=lobj::ModuleMeta_strategy)
def test_lobj::modulemeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj::ModuleFolder_strategy)
@settings(max_examples=50)
def test_lobj::modulefolder_instantiation(instance):
    assert isinstance(instance, lobj::ModuleFolder)

@given(instance=lobj::Category_strategy)
@settings(max_examples=50)
def test_lobj::category_instantiation(instance):
    assert isinstance(instance, lobj::Category)

@given(instance=lobj::BlockFolder_strategy)
@settings(max_examples=50)
def test_lobj::blockfolder_instantiation(instance):
    assert isinstance(instance, lobj::BlockFolder)

@given(instance=lobj::Course_strategy)
@settings(max_examples=50)
def test_lobj::course_instantiation(instance):
    assert isinstance(instance, lobj::Course)

@given(instance=lobj::Course_strategy)
def test_lobj::course_outlineAsXml_type(instance):
    assert isinstance(instance.outlineAsXml, str)


@given(instance=lobj::Course_strategy)
def test_lobj::course_outlineAsXml_setter(instance):
    original = instance.outlineAsXml
    instance.outlineAsXml = original
    assert instance.outlineAsXml == original

@given(instance=lobj::ResrcFolder_strategy)
@settings(max_examples=50)
def test_lobj::resrcfolder_instantiation(instance):
    assert isinstance(instance, lobj::ResrcFolder)

@given(instance=lobj::ResrcFolder_strategy)
def test_lobj::resrcfolder_deleteScheduled_type(instance):
    assert isinstance(instance.deleteScheduled, bool)


@given(instance=lobj::ResrcFolder_strategy)
def test_lobj::resrcfolder_deleteScheduled_setter(instance):
    original = instance.deleteScheduled
    instance.deleteScheduled = original
    assert instance.deleteScheduled == original

@given(instance=lobj::Block_strategy)
@settings(max_examples=50)
def test_lobj::block_instantiation(instance):
    assert isinstance(instance, lobj::Block)

@given(instance=lobj::LearningObject_strategy)
@settings(max_examples=50)
def test_lobj::learningobject_instantiation(instance):
    assert isinstance(instance, lobj::LearningObject)

@given(instance=lobj::LearningObject_strategy)
def test_lobj::learningobject_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=lobj::LearningObject_strategy)
def test_lobj::learningobject_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=lobj::LearningObject_strategy)
def test_lobj::learningobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=lobj::LearningObject_strategy)
def test_lobj::learningobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj::LearningObject_strategy)
def test_lobj::learningobject_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=lobj::LearningObject_strategy)
def test_lobj::learningobject_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=lobj::Language_strategy)
@settings(max_examples=50)
def test_lobj::language_instantiation(instance):
    assert isinstance(instance, lobj::Language)

@given(instance=lobj::Language_strategy)
def test_lobj::language_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=lobj::Language_strategy)
def test_lobj::language_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=lobj::Language_strategy)
def test_lobj::language_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=lobj::Language_strategy)
def test_lobj::language_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=lobj::AbstractContent_strategy)
@settings(max_examples=50)
def test_lobj::abstractcontent_instantiation(instance):
    assert isinstance(instance, lobj::AbstractContent)

@given(instance=lobj::AbstractContent_strategy)
def test_lobj::abstractcontent_heading_type(instance):
    assert isinstance(instance.heading, str)


@given(instance=lobj::AbstractContent_strategy)
def test_lobj::abstractcontent_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=lobj::HypertextContent_strategy)
@settings(max_examples=50)
def test_lobj::hypertextcontent_instantiation(instance):
    assert isinstance(instance, lobj::HypertextContent)

@given(instance=lobj::HypertextContent_strategy)
def test_lobj::hypertextcontent_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=lobj::HypertextContent_strategy)
def test_lobj::hypertextcontent_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=lobj::HypertextBlock_strategy)
@settings(max_examples=50)
def test_lobj::hypertextblock_instantiation(instance):
    assert isinstance(instance, lobj::HypertextBlock)
