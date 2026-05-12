import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lobj_InternalRef,
    lobj_Publisher,
    lobj_PublishInfo,
    lobj_Note,
    lobj_AuthorizationTypes,
    lobj_Precognition,
    SimpleDidacMeta,
    lobj_Domain,
    lobj_DidacMeta,
    lobj_Person,
    lobj_Author,
    lobj_Blocktype,
    lobj_Address,
    lobj_Edition,
    lobj_Userauthorization,
    lobj_Affiliation,
    lobj_Sharednotes,
    lobj_User,
    lobj_ResrcFiletype,
    Node,
    lobj_ThemeNode,
    lobj_LuNode,
    lobj_SimpleDidacMeta,
    lobj_Node,
    lobj_Item,
    lobj_Coursetype,
    lobj_PresentationBlock,
    AbstractContent,
    lobj_Source,
    lobj_CorrBlock,
    lobj_TitleMeta,
    lobj_AccessControl,
    lobj_ExternalMetadata,
    LearningObject,
    lobj_LuMeta,
    lobj_ResrcFile,
    lobj_ResrcMeta,
    lobj_Course,
    lobj_BlockMeta,
    lobj_ModuleFolder,
    lobj_Module,
    lobj_BlockFolder,
    lobj_LearningUnit,
    lobj_CourseMeta,
    lobj_Theme,
    lobj_FolderMeta,
    lobj_ResrcFolder,
    lobj_BlockAudiofile,
    lobj_Category,
    lobj_ModuleMeta,
    lobj_LuFolder,
    lobj_Block,
    lobj_LearningObject,
    lobj_Language,
    lobj_AbstractContent,
    lobj_HypertextContent,
    Block,
    lobj_HypertextBlock,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lobj_internalref_is_not_abstract():
    assert not inspect.isabstract(lobj_InternalRef)


def test_lobj_internalref_constructor_exists():
    assert callable(lobj_InternalRef.__init__)


def test_lobj_internalref_constructor_args():
    sig = inspect.signature(lobj_InternalRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "reftype" in params, "Missing parameter 'reftype'"
    assert "file" in params, "Missing parameter 'file'"
    assert "ref" in params, "Missing parameter 'ref'"

def test_lobj_internalref_has_id():
    assert hasattr(lobj_InternalRef, "id")
    descriptor = None
    for klass in lobj_InternalRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_internalref_has_reftype():
    assert hasattr(lobj_InternalRef, "reftype")
    descriptor = None
    for klass in lobj_InternalRef.__mro__:
        if "reftype" in klass.__dict__:
            descriptor = klass.__dict__["reftype"]
            break
    assert isinstance(descriptor, property)

def test_lobj_internalref_has_file():
    assert hasattr(lobj_InternalRef, "file")
    descriptor = None
    for klass in lobj_InternalRef.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_lobj_internalref_has_ref():
    assert hasattr(lobj_InternalRef, "ref")
    descriptor = None
    for klass in lobj_InternalRef.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_lobj_publisher_is_not_abstract():
    assert not inspect.isabstract(lobj_Publisher)


def test_lobj_publisher_constructor_exists():
    assert callable(lobj_Publisher.__init__)


def test_lobj_publisher_constructor_args():
    sig = inspect.signature(lobj_Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "publishername" in params, "Missing parameter 'publishername'"

def test_lobj_publisher_has_id():
    assert hasattr(lobj_Publisher, "id")
    descriptor = None
    for klass in lobj_Publisher.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_publisher_has_publishername():
    assert hasattr(lobj_Publisher, "publishername")
    descriptor = None
    for klass in lobj_Publisher.__mro__:
        if "publishername" in klass.__dict__:
            descriptor = klass.__dict__["publishername"]
            break
    assert isinstance(descriptor, property)



def test_lobj_publishinfo_is_not_abstract():
    assert not inspect.isabstract(lobj_PublishInfo)


def test_lobj_publishinfo_constructor_exists():
    assert callable(lobj_PublishInfo.__init__)


def test_lobj_publishinfo_constructor_args():
    sig = inspect.signature(lobj_PublishInfo.__init__)
    params = list(sig.parameters.keys())
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "pubsnumber" in params, "Missing parameter 'pubsnumber'"
    assert "id" in params, "Missing parameter 'id'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "releaseinfo" in params, "Missing parameter 'releaseinfo'"

def test_lobj_publishinfo_has_pubdate():
    assert hasattr(lobj_PublishInfo, "pubdate")
    descriptor = None
    for klass in lobj_PublishInfo.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_publishinfo_has_pubsnumber():
    assert hasattr(lobj_PublishInfo, "pubsnumber")
    descriptor = None
    for klass in lobj_PublishInfo.__mro__:
        if "pubsnumber" in klass.__dict__:
            descriptor = klass.__dict__["pubsnumber"]
            break
    assert isinstance(descriptor, property)

def test_lobj_publishinfo_has_id():
    assert hasattr(lobj_PublishInfo, "id")
    descriptor = None
    for klass in lobj_PublishInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_publishinfo_has_edition():
    assert hasattr(lobj_PublishInfo, "edition")
    descriptor = None
    for klass in lobj_PublishInfo.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_lobj_publishinfo_has_releaseinfo():
    assert hasattr(lobj_PublishInfo, "releaseinfo")
    descriptor = None
    for klass in lobj_PublishInfo.__mro__:
        if "releaseinfo" in klass.__dict__:
            descriptor = klass.__dict__["releaseinfo"]
            break
    assert isinstance(descriptor, property)



def test_lobj_note_is_not_abstract():
    assert not inspect.isabstract(lobj_Note)


def test_lobj_note_constructor_exists():
    assert callable(lobj_Note.__init__)


def test_lobj_note_constructor_args():
    sig = inspect.signature(lobj_Note.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "noteAuthor" in params, "Missing parameter 'noteAuthor'"
    assert "id" in params, "Missing parameter 'id'"
    assert "date" in params, "Missing parameter 'date'"

def test_lobj_note_has_content():
    assert hasattr(lobj_Note, "content")
    descriptor = None
    for klass in lobj_Note.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_lobj_note_has_noteAuthor():
    assert hasattr(lobj_Note, "noteAuthor")
    descriptor = None
    for klass in lobj_Note.__mro__:
        if "noteAuthor" in klass.__dict__:
            descriptor = klass.__dict__["noteAuthor"]
            break
    assert isinstance(descriptor, property)

def test_lobj_note_has_id():
    assert hasattr(lobj_Note, "id")
    descriptor = None
    for klass in lobj_Note.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_note_has_date():
    assert hasattr(lobj_Note, "date")
    descriptor = None
    for klass in lobj_Note.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_lobj_authorizationtypes_is_not_abstract():
    assert not inspect.isabstract(lobj_AuthorizationTypes)


def test_lobj_authorizationtypes_constructor_exists():
    assert callable(lobj_AuthorizationTypes.__init__)


def test_lobj_authorizationtypes_constructor_args():
    sig = inspect.signature(lobj_AuthorizationTypes.__init__)
    params = list(sig.parameters.keys())
    assert "authType" in params, "Missing parameter 'authType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "authTypeDesc" in params, "Missing parameter 'authTypeDesc'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_lobj_authorizationtypes_has_authType():
    assert hasattr(lobj_AuthorizationTypes, "authType")
    descriptor = None
    for klass in lobj_AuthorizationTypes.__mro__:
        if "authType" in klass.__dict__:
            descriptor = klass.__dict__["authType"]
            break
    assert isinstance(descriptor, property)

def test_lobj_authorizationtypes_has_id():
    assert hasattr(lobj_AuthorizationTypes, "id")
    descriptor = None
    for klass in lobj_AuthorizationTypes.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_authorizationtypes_has_authTypeDesc():
    assert hasattr(lobj_AuthorizationTypes, "authTypeDesc")
    descriptor = None
    for klass in lobj_AuthorizationTypes.__mro__:
        if "authTypeDesc" in klass.__dict__:
            descriptor = klass.__dict__["authTypeDesc"]
            break
    assert isinstance(descriptor, property)

def test_lobj_authorizationtypes_has_readOnly():
    assert hasattr(lobj_AuthorizationTypes, "readOnly")
    descriptor = None
    for klass in lobj_AuthorizationTypes.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_lobj_precognition_is_not_abstract():
    assert not inspect.isabstract(lobj_Precognition)


def test_lobj_precognition_constructor_exists():
    assert callable(lobj_Precognition.__init__)


def test_lobj_precognition_constructor_args():
    sig = inspect.signature(lobj_Precognition.__init__)
    params = list(sig.parameters.keys())
    assert "precog" in params, "Missing parameter 'precog'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj_precognition_has_precog():
    assert hasattr(lobj_Precognition, "precog")
    descriptor = None
    for klass in lobj_Precognition.__mro__:
        if "precog" in klass.__dict__:
            descriptor = klass.__dict__["precog"]
            break
    assert isinstance(descriptor, property)

def test_lobj_precognition_has_id():
    assert hasattr(lobj_Precognition, "id")
    descriptor = None
    for klass in lobj_Precognition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simpledidacmeta_is_not_abstract():
    assert not inspect.isabstract(SimpleDidacMeta)


def test_simpledidacmeta_constructor_exists():
    assert callable(SimpleDidacMeta.__init__)


def test_simpledidacmeta_constructor_args():
    sig = inspect.signature(SimpleDidacMeta.__init__)
    params = list(sig.parameters.keys())



def test_lobj_domain_is_not_abstract():
    assert not inspect.isabstract(lobj_Domain)


def test_lobj_domain_constructor_exists():
    assert callable(lobj_Domain.__init__)


def test_lobj_domain_constructor_args():
    sig = inspect.signature(lobj_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "serverURL" in params, "Missing parameter 'serverURL'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_lobj_domain_has_creationDate():
    assert hasattr(lobj_Domain, "creationDate")
    descriptor = None
    for klass in lobj_Domain.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_domain_has_id():
    assert hasattr(lobj_Domain, "id")
    descriptor = None
    for klass in lobj_Domain.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_domain_has_serverURL():
    assert hasattr(lobj_Domain, "serverURL")
    descriptor = None
    for klass in lobj_Domain.__mro__:
        if "serverURL" in klass.__dict__:
            descriptor = klass.__dict__["serverURL"]
            break
    assert isinstance(descriptor, property)

def test_lobj_domain_has_name():
    assert hasattr(lobj_Domain, "name")
    descriptor = None
    for klass in lobj_Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_lobj_domain_has_description():
    assert hasattr(lobj_Domain, "description")
    descriptor = None
    for klass in lobj_Domain.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_lobj_didacmeta_is_not_abstract():
    assert not inspect.isabstract(lobj_DidacMeta)


def test_lobj_didacmeta_constructor_exists():
    assert callable(lobj_DidacMeta.__init__)


def test_lobj_didacmeta_constructor_args():
    sig = inspect.signature(lobj_DidacMeta.__init__)
    params = list(sig.parameters.keys())
    assert "goal" in params, "Missing parameter 'goal'"

def test_lobj_didacmeta_has_goal():
    assert hasattr(lobj_DidacMeta, "goal")
    descriptor = None
    for klass in lobj_DidacMeta.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)



def test_lobj_person_is_not_abstract():
    assert not inspect.isabstract(lobj_Person)


def test_lobj_person_constructor_exists():
    assert callable(lobj_Person.__init__)


def test_lobj_person_constructor_args():
    sig = inspect.signature(lobj_Person.__init__)
    params = list(sig.parameters.keys())
    assert "honorific" in params, "Missing parameter 'honorific'"
    assert "contrib" in params, "Missing parameter 'contrib'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "id" in params, "Missing parameter 'id'"
    assert "personblurb" in params, "Missing parameter 'personblurb'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_lobj_person_has_honorific():
    assert hasattr(lobj_Person, "honorific")
    descriptor = None
    for klass in lobj_Person.__mro__:
        if "honorific" in klass.__dict__:
            descriptor = klass.__dict__["honorific"]
            break
    assert isinstance(descriptor, property)

def test_lobj_person_has_contrib():
    assert hasattr(lobj_Person, "contrib")
    descriptor = None
    for klass in lobj_Person.__mro__:
        if "contrib" in klass.__dict__:
            descriptor = klass.__dict__["contrib"]
            break
    assert isinstance(descriptor, property)

def test_lobj_person_has_firstname():
    assert hasattr(lobj_Person, "firstname")
    descriptor = None
    for klass in lobj_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_lobj_person_has_id():
    assert hasattr(lobj_Person, "id")
    descriptor = None
    for klass in lobj_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_person_has_personblurb():
    assert hasattr(lobj_Person, "personblurb")
    descriptor = None
    for klass in lobj_Person.__mro__:
        if "personblurb" in klass.__dict__:
            descriptor = klass.__dict__["personblurb"]
            break
    assert isinstance(descriptor, property)

def test_lobj_person_has_surname():
    assert hasattr(lobj_Person, "surname")
    descriptor = None
    for klass in lobj_Person.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_lobj_author_is_not_abstract():
    assert not inspect.isabstract(lobj_Author)


def test_lobj_author_constructor_exists():
    assert callable(lobj_Author.__init__)


def test_lobj_author_constructor_args():
    sig = inspect.signature(lobj_Author.__init__)
    params = list(sig.parameters.keys())
    assert "credittype" in params, "Missing parameter 'credittype'"
    assert "id" in params, "Missing parameter 'id'"
    assert "email" in params, "Missing parameter 'email'"

def test_lobj_author_has_credittype():
    assert hasattr(lobj_Author, "credittype")
    descriptor = None
    for klass in lobj_Author.__mro__:
        if "credittype" in klass.__dict__:
            descriptor = klass.__dict__["credittype"]
            break
    assert isinstance(descriptor, property)

def test_lobj_author_has_id():
    assert hasattr(lobj_Author, "id")
    descriptor = None
    for klass in lobj_Author.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_author_has_email():
    assert hasattr(lobj_Author, "email")
    descriptor = None
    for klass in lobj_Author.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_lobj_blocktype_is_not_abstract():
    assert not inspect.isabstract(lobj_Blocktype)


def test_lobj_blocktype_constructor_exists():
    assert callable(lobj_Blocktype.__init__)


def test_lobj_blocktype_constructor_args():
    sig = inspect.signature(lobj_Blocktype.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "styleRef" in params, "Missing parameter 'styleRef'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_lobj_blocktype_has_creationDate():
    assert hasattr(lobj_Blocktype, "creationDate")
    descriptor = None
    for klass in lobj_Blocktype.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blocktype_has_styleRef():
    assert hasattr(lobj_Blocktype, "styleRef")
    descriptor = None
    for klass in lobj_Blocktype.__mro__:
        if "styleRef" in klass.__dict__:
            descriptor = klass.__dict__["styleRef"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blocktype_has_description():
    assert hasattr(lobj_Blocktype, "description")
    descriptor = None
    for klass in lobj_Blocktype.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blocktype_has_id():
    assert hasattr(lobj_Blocktype, "id")
    descriptor = None
    for klass in lobj_Blocktype.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blocktype_has_name():
    assert hasattr(lobj_Blocktype, "name")
    descriptor = None
    for klass in lobj_Blocktype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lobj_address_is_not_abstract():
    assert not inspect.isabstract(lobj_Address)


def test_lobj_address_constructor_exists():
    assert callable(lobj_Address.__init__)


def test_lobj_address_constructor_args():
    sig = inspect.signature(lobj_Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "otheraddr" in params, "Missing parameter 'otheraddr'"
    assert "email" in params, "Missing parameter 'email'"
    assert "postcode" in params, "Missing parameter 'postcode'"
    assert "street" in params, "Missing parameter 'street'"
    assert "fax" in params, "Missing parameter 'fax'"
    assert "id" in params, "Missing parameter 'id'"
    assert "country" in params, "Missing parameter 'country'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "state" in params, "Missing parameter 'state'"

def test_lobj_address_has_city():
    assert hasattr(lobj_Address, "city")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_otheraddr():
    assert hasattr(lobj_Address, "otheraddr")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "otheraddr" in klass.__dict__:
            descriptor = klass.__dict__["otheraddr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_email():
    assert hasattr(lobj_Address, "email")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_postcode():
    assert hasattr(lobj_Address, "postcode")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "postcode" in klass.__dict__:
            descriptor = klass.__dict__["postcode"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_street():
    assert hasattr(lobj_Address, "street")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_fax():
    assert hasattr(lobj_Address, "fax")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "fax" in klass.__dict__:
            descriptor = klass.__dict__["fax"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_id():
    assert hasattr(lobj_Address, "id")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_country():
    assert hasattr(lobj_Address, "country")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_phone():
    assert hasattr(lobj_Address, "phone")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_lobj_address_has_state():
    assert hasattr(lobj_Address, "state")
    descriptor = None
    for klass in lobj_Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_lobj_edition_is_not_abstract():
    assert not inspect.isabstract(lobj_Edition)


def test_lobj_edition_constructor_exists():
    assert callable(lobj_Edition.__init__)


def test_lobj_edition_constructor_args():
    sig = inspect.signature(lobj_Edition.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "editionNr" in params, "Missing parameter 'editionNr'"
    assert "editedBy" in params, "Missing parameter 'editedBy'"
    assert "editionCreationDate" in params, "Missing parameter 'editionCreationDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "status" in params, "Missing parameter 'status'"
    assert "lastVersionNumber" in params, "Missing parameter 'lastVersionNumber'"

def test_lobj_edition_has_version():
    assert hasattr(lobj_Edition, "version")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_lobj_edition_has_editionNr():
    assert hasattr(lobj_Edition, "editionNr")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "editionNr" in klass.__dict__:
            descriptor = klass.__dict__["editionNr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_edition_has_editedBy():
    assert hasattr(lobj_Edition, "editedBy")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "editedBy" in klass.__dict__:
            descriptor = klass.__dict__["editedBy"]
            break
    assert isinstance(descriptor, property)

def test_lobj_edition_has_editionCreationDate():
    assert hasattr(lobj_Edition, "editionCreationDate")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "editionCreationDate" in klass.__dict__:
            descriptor = klass.__dict__["editionCreationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_edition_has_id():
    assert hasattr(lobj_Edition, "id")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_edition_has_status():
    assert hasattr(lobj_Edition, "status")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_lobj_edition_has_lastVersionNumber():
    assert hasattr(lobj_Edition, "lastVersionNumber")
    descriptor = None
    for klass in lobj_Edition.__mro__:
        if "lastVersionNumber" in klass.__dict__:
            descriptor = klass.__dict__["lastVersionNumber"]
            break
    assert isinstance(descriptor, property)



def test_lobj_userauthorization_is_not_abstract():
    assert not inspect.isabstract(lobj_Userauthorization)


def test_lobj_userauthorization_constructor_exists():
    assert callable(lobj_Userauthorization.__init__)


def test_lobj_userauthorization_constructor_args():
    sig = inspect.signature(lobj_Userauthorization.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lobj_userauthorization_has_id():
    assert hasattr(lobj_Userauthorization, "id")
    descriptor = None
    for klass in lobj_Userauthorization.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj_affiliation_is_not_abstract():
    assert not inspect.isabstract(lobj_Affiliation)


def test_lobj_affiliation_constructor_exists():
    assert callable(lobj_Affiliation.__init__)


def test_lobj_affiliation_constructor_args():
    sig = inspect.signature(lobj_Affiliation.__init__)
    params = list(sig.parameters.keys())
    assert "jobtitle" in params, "Missing parameter 'jobtitle'"
    assert "orgname" in params, "Missing parameter 'orgname'"
    assert "id" in params, "Missing parameter 'id'"
    assert "orgdiv" in params, "Missing parameter 'orgdiv'"
    assert "shortaffil" in params, "Missing parameter 'shortaffil'"

def test_lobj_affiliation_has_jobtitle():
    assert hasattr(lobj_Affiliation, "jobtitle")
    descriptor = None
    for klass in lobj_Affiliation.__mro__:
        if "jobtitle" in klass.__dict__:
            descriptor = klass.__dict__["jobtitle"]
            break
    assert isinstance(descriptor, property)

def test_lobj_affiliation_has_orgname():
    assert hasattr(lobj_Affiliation, "orgname")
    descriptor = None
    for klass in lobj_Affiliation.__mro__:
        if "orgname" in klass.__dict__:
            descriptor = klass.__dict__["orgname"]
            break
    assert isinstance(descriptor, property)

def test_lobj_affiliation_has_id():
    assert hasattr(lobj_Affiliation, "id")
    descriptor = None
    for klass in lobj_Affiliation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_affiliation_has_orgdiv():
    assert hasattr(lobj_Affiliation, "orgdiv")
    descriptor = None
    for klass in lobj_Affiliation.__mro__:
        if "orgdiv" in klass.__dict__:
            descriptor = klass.__dict__["orgdiv"]
            break
    assert isinstance(descriptor, property)

def test_lobj_affiliation_has_shortaffil():
    assert hasattr(lobj_Affiliation, "shortaffil")
    descriptor = None
    for klass in lobj_Affiliation.__mro__:
        if "shortaffil" in klass.__dict__:
            descriptor = klass.__dict__["shortaffil"]
            break
    assert isinstance(descriptor, property)



def test_lobj_sharednotes_is_not_abstract():
    assert not inspect.isabstract(lobj_Sharednotes)


def test_lobj_sharednotes_constructor_exists():
    assert callable(lobj_Sharednotes.__init__)


def test_lobj_sharednotes_constructor_args():
    sig = inspect.signature(lobj_Sharednotes.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lobj_sharednotes_has_id():
    assert hasattr(lobj_Sharednotes, "id")
    descriptor = None
    for klass in lobj_Sharednotes.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj_user_is_not_abstract():
    assert not inspect.isabstract(lobj_User)


def test_lobj_user_constructor_exists():
    assert callable(lobj_User.__init__)


def test_lobj_user_constructor_args():
    sig = inspect.signature(lobj_User.__init__)
    params = list(sig.parameters.keys())
    assert "lastcoursematerialviewnr" in params, "Missing parameter 'lastcoursematerialviewnr'"
    assert "loginname" in params, "Missing parameter 'loginname'"
    assert "datafilter" in params, "Missing parameter 'datafilter'"
    assert "icqnumber" in params, "Missing parameter 'icqnumber'"
    assert "dossierasxml" in params, "Missing parameter 'dossierasxml'"
    assert "currlogindate" in params, "Missing parameter 'currlogindate'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "photochanged" in params, "Missing parameter 'photochanged'"
    assert "matriculationnr" in params, "Missing parameter 'matriculationnr'"
    assert "authenticateldap" in params, "Missing parameter 'authenticateldap'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lastcoursematerialnr" in params, "Missing parameter 'lastcoursematerialnr'"
    assert "inchatsince" in params, "Missing parameter 'inchatsince'"
    assert "fromext" in params, "Missing parameter 'fromext'"
    assert "contchatdate" in params, "Missing parameter 'contchatdate'"
    assert "lastlogindate" in params, "Missing parameter 'lastlogindate'"
    assert "scn" in params, "Missing parameter 'scn'"
    assert "onlinestatus" in params, "Missing parameter 'onlinestatus'"
    assert "languagenr" in params, "Missing parameter 'languagenr'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "entryasxml" in params, "Missing parameter 'entryasxml'"
    assert "icqpassword" in params, "Missing parameter 'icqpassword'"
    assert "photo" in params, "Missing parameter 'photo'"
    assert "onlinedate" in params, "Missing parameter 'onlinedate'"
    assert "notificationprofileasxml" in params, "Missing parameter 'notificationprofileasxml'"
    assert "chatroomnr" in params, "Missing parameter 'chatroomnr'"
    assert "password" in params, "Missing parameter 'password'"

def test_lobj_user_has_lastcoursematerialviewnr():
    assert hasattr(lobj_User, "lastcoursematerialviewnr")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "lastcoursematerialviewnr" in klass.__dict__:
            descriptor = klass.__dict__["lastcoursematerialviewnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_loginname():
    assert hasattr(lobj_User, "loginname")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "loginname" in klass.__dict__:
            descriptor = klass.__dict__["loginname"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_datafilter():
    assert hasattr(lobj_User, "datafilter")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "datafilter" in klass.__dict__:
            descriptor = klass.__dict__["datafilter"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_icqnumber():
    assert hasattr(lobj_User, "icqnumber")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "icqnumber" in klass.__dict__:
            descriptor = klass.__dict__["icqnumber"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_dossierasxml():
    assert hasattr(lobj_User, "dossierasxml")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "dossierasxml" in klass.__dict__:
            descriptor = klass.__dict__["dossierasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_currlogindate():
    assert hasattr(lobj_User, "currlogindate")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "currlogindate" in klass.__dict__:
            descriptor = klass.__dict__["currlogindate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_lastname():
    assert hasattr(lobj_User, "lastname")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_photochanged():
    assert hasattr(lobj_User, "photochanged")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "photochanged" in klass.__dict__:
            descriptor = klass.__dict__["photochanged"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_matriculationnr():
    assert hasattr(lobj_User, "matriculationnr")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "matriculationnr" in klass.__dict__:
            descriptor = klass.__dict__["matriculationnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_authenticateldap():
    assert hasattr(lobj_User, "authenticateldap")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "authenticateldap" in klass.__dict__:
            descriptor = klass.__dict__["authenticateldap"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_id():
    assert hasattr(lobj_User, "id")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_lastcoursematerialnr():
    assert hasattr(lobj_User, "lastcoursematerialnr")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "lastcoursematerialnr" in klass.__dict__:
            descriptor = klass.__dict__["lastcoursematerialnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_inchatsince():
    assert hasattr(lobj_User, "inchatsince")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "inchatsince" in klass.__dict__:
            descriptor = klass.__dict__["inchatsince"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_fromext():
    assert hasattr(lobj_User, "fromext")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "fromext" in klass.__dict__:
            descriptor = klass.__dict__["fromext"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_contchatdate():
    assert hasattr(lobj_User, "contchatdate")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "contchatdate" in klass.__dict__:
            descriptor = klass.__dict__["contchatdate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_lastlogindate():
    assert hasattr(lobj_User, "lastlogindate")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "lastlogindate" in klass.__dict__:
            descriptor = klass.__dict__["lastlogindate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_scn():
    assert hasattr(lobj_User, "scn")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "scn" in klass.__dict__:
            descriptor = klass.__dict__["scn"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_onlinestatus():
    assert hasattr(lobj_User, "onlinestatus")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "onlinestatus" in klass.__dict__:
            descriptor = klass.__dict__["onlinestatus"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_languagenr():
    assert hasattr(lobj_User, "languagenr")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "languagenr" in klass.__dict__:
            descriptor = klass.__dict__["languagenr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_firstname():
    assert hasattr(lobj_User, "firstname")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_entryasxml():
    assert hasattr(lobj_User, "entryasxml")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "entryasxml" in klass.__dict__:
            descriptor = klass.__dict__["entryasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_icqpassword():
    assert hasattr(lobj_User, "icqpassword")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "icqpassword" in klass.__dict__:
            descriptor = klass.__dict__["icqpassword"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_photo():
    assert hasattr(lobj_User, "photo")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "photo" in klass.__dict__:
            descriptor = klass.__dict__["photo"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_onlinedate():
    assert hasattr(lobj_User, "onlinedate")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "onlinedate" in klass.__dict__:
            descriptor = klass.__dict__["onlinedate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_notificationprofileasxml():
    assert hasattr(lobj_User, "notificationprofileasxml")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "notificationprofileasxml" in klass.__dict__:
            descriptor = klass.__dict__["notificationprofileasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_chatroomnr():
    assert hasattr(lobj_User, "chatroomnr")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "chatroomnr" in klass.__dict__:
            descriptor = klass.__dict__["chatroomnr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_user_has_password():
    assert hasattr(lobj_User, "password")
    descriptor = None
    for klass in lobj_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_lobj_resrcfiletype_is_not_abstract():
    assert not inspect.isabstract(lobj_ResrcFiletype)


def test_lobj_resrcfiletype_constructor_exists():
    assert callable(lobj_ResrcFiletype.__init__)


def test_lobj_resrcfiletype_constructor_args():
    sig = inspect.signature(lobj_ResrcFiletype.__init__)
    params = list(sig.parameters.keys())
    assert "filetypeImageBif" in params, "Missing parameter 'filetypeImageBif'"
    assert "filetypeDesc" in params, "Missing parameter 'filetypeDesc'"
    assert "filetypeImageSmall" in params, "Missing parameter 'filetypeImageSmall'"
    assert "image" in params, "Missing parameter 'image'"
    assert "applet" in params, "Missing parameter 'applet'"
    assert "id" in params, "Missing parameter 'id'"
    assert "filetypeExtension" in params, "Missing parameter 'filetypeExtension'"

def test_lobj_resrcfiletype_has_filetypeImageBif():
    assert hasattr(lobj_ResrcFiletype, "filetypeImageBif")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "filetypeImageBif" in klass.__dict__:
            descriptor = klass.__dict__["filetypeImageBif"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfiletype_has_filetypeDesc():
    assert hasattr(lobj_ResrcFiletype, "filetypeDesc")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "filetypeDesc" in klass.__dict__:
            descriptor = klass.__dict__["filetypeDesc"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfiletype_has_filetypeImageSmall():
    assert hasattr(lobj_ResrcFiletype, "filetypeImageSmall")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "filetypeImageSmall" in klass.__dict__:
            descriptor = klass.__dict__["filetypeImageSmall"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfiletype_has_image():
    assert hasattr(lobj_ResrcFiletype, "image")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfiletype_has_applet():
    assert hasattr(lobj_ResrcFiletype, "applet")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "applet" in klass.__dict__:
            descriptor = klass.__dict__["applet"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfiletype_has_id():
    assert hasattr(lobj_ResrcFiletype, "id")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfiletype_has_filetypeExtension():
    assert hasattr(lobj_ResrcFiletype, "filetypeExtension")
    descriptor = None
    for klass in lobj_ResrcFiletype.__mro__:
        if "filetypeExtension" in klass.__dict__:
            descriptor = klass.__dict__["filetypeExtension"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_lobj_themenode_is_not_abstract():
    assert not inspect.isabstract(lobj_ThemeNode)


def test_lobj_themenode_constructor_exists():
    assert callable(lobj_ThemeNode.__init__)


def test_lobj_themenode_constructor_args():
    sig = inspect.signature(lobj_ThemeNode.__init__)
    params = list(sig.parameters.keys())



def test_lobj_lunode_is_not_abstract():
    assert not inspect.isabstract(lobj_LuNode)


def test_lobj_lunode_constructor_exists():
    assert callable(lobj_LuNode.__init__)


def test_lobj_lunode_constructor_args():
    sig = inspect.signature(lobj_LuNode.__init__)
    params = list(sig.parameters.keys())



def test_lobj_simpledidacmeta_is_not_abstract():
    assert not inspect.isabstract(lobj_SimpleDidacMeta)


def test_lobj_simpledidacmeta_constructor_exists():
    assert callable(lobj_SimpleDidacMeta.__init__)


def test_lobj_simpledidacmeta_constructor_args():
    sig = inspect.signature(lobj_SimpleDidacMeta.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "description" in params, "Missing parameter 'description'"
    assert "keywords" in params, "Missing parameter 'keywords'"

def test_lobj_simpledidacmeta_has_id():
    assert hasattr(lobj_SimpleDidacMeta, "id")
    descriptor = None
    for klass in lobj_SimpleDidacMeta.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_simpledidacmeta_has_title():
    assert hasattr(lobj_SimpleDidacMeta, "title")
    descriptor = None
    for klass in lobj_SimpleDidacMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj_simpledidacmeta_has_description():
    assert hasattr(lobj_SimpleDidacMeta, "description")
    descriptor = None
    for klass in lobj_SimpleDidacMeta.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj_simpledidacmeta_has_keywords():
    assert hasattr(lobj_SimpleDidacMeta, "keywords")
    descriptor = None
    for klass in lobj_SimpleDidacMeta.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)



def test_lobj_node_is_not_abstract():
    assert not inspect.isabstract(lobj_Node)


def test_lobj_node_constructor_exists():
    assert callable(lobj_Node.__init__)


def test_lobj_node_constructor_args():
    sig = inspect.signature(lobj_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_lobj_node_has_id():
    assert hasattr(lobj_Node, "id")
    descriptor = None
    for klass in lobj_Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_node_has_visible():
    assert hasattr(lobj_Node, "visible")
    descriptor = None
    for klass in lobj_Node.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_lobj_item_is_not_abstract():
    assert not inspect.isabstract(lobj_Item)


def test_lobj_item_constructor_exists():
    assert callable(lobj_Item.__init__)


def test_lobj_item_constructor_args():
    sig = inspect.signature(lobj_Item.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "luRef" in params, "Missing parameter 'luRef'"

def test_lobj_item_has_id():
    assert hasattr(lobj_Item, "id")
    descriptor = None
    for klass in lobj_Item.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_item_has_luRef():
    assert hasattr(lobj_Item, "luRef")
    descriptor = None
    for klass in lobj_Item.__mro__:
        if "luRef" in klass.__dict__:
            descriptor = klass.__dict__["luRef"]
            break
    assert isinstance(descriptor, property)



def test_lobj_coursetype_is_not_abstract():
    assert not inspect.isabstract(lobj_Coursetype)


def test_lobj_coursetype_constructor_exists():
    assert callable(lobj_Coursetype.__init__)


def test_lobj_coursetype_constructor_args():
    sig = inspect.signature(lobj_Coursetype.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "description" in params, "Missing parameter 'description'"

def test_lobj_coursetype_has_id():
    assert hasattr(lobj_Coursetype, "id")
    descriptor = None
    for klass in lobj_Coursetype.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_coursetype_has_title():
    assert hasattr(lobj_Coursetype, "title")
    descriptor = None
    for klass in lobj_Coursetype.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj_coursetype_has_description():
    assert hasattr(lobj_Coursetype, "description")
    descriptor = None
    for klass in lobj_Coursetype.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_lobj_presentationblock_is_not_abstract():
    assert not inspect.isabstract(lobj_PresentationBlock)


def test_lobj_presentationblock_constructor_exists():
    assert callable(lobj_PresentationBlock.__init__)


def test_lobj_presentationblock_constructor_args():
    sig = inspect.signature(lobj_PresentationBlock.__init__)
    params = list(sig.parameters.keys())
    assert "lod" in params, "Missing parameter 'lod'"
    assert "rendering" in params, "Missing parameter 'rendering'"
    assert "id" in params, "Missing parameter 'id'"

def test_lobj_presentationblock_has_lod():
    assert hasattr(lobj_PresentationBlock, "lod")
    descriptor = None
    for klass in lobj_PresentationBlock.__mro__:
        if "lod" in klass.__dict__:
            descriptor = klass.__dict__["lod"]
            break
    assert isinstance(descriptor, property)

def test_lobj_presentationblock_has_rendering():
    assert hasattr(lobj_PresentationBlock, "rendering")
    descriptor = None
    for klass in lobj_PresentationBlock.__mro__:
        if "rendering" in klass.__dict__:
            descriptor = klass.__dict__["rendering"]
            break
    assert isinstance(descriptor, property)

def test_lobj_presentationblock_has_id():
    assert hasattr(lobj_PresentationBlock, "id")
    descriptor = None
    for klass in lobj_PresentationBlock.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abstractcontent_is_not_abstract():
    assert not inspect.isabstract(AbstractContent)


def test_abstractcontent_constructor_exists():
    assert callable(AbstractContent.__init__)


def test_abstractcontent_constructor_args():
    sig = inspect.signature(AbstractContent.__init__)
    params = list(sig.parameters.keys())



def test_lobj_source_is_not_abstract():
    assert not inspect.isabstract(lobj_Source)


def test_lobj_source_constructor_exists():
    assert callable(lobj_Source.__init__)


def test_lobj_source_constructor_args():
    sig = inspect.signature(lobj_Source.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "publishedIn" in params, "Missing parameter 'publishedIn'"
    assert "id" in params, "Missing parameter 'id'"
    assert "publishedBy" in params, "Missing parameter 'publishedBy'"
    assert "pp" in params, "Missing parameter 'pp'"
    assert "subtitle" in params, "Missing parameter 'subtitle'"
    assert "publishDate" in params, "Missing parameter 'publishDate'"

def test_lobj_source_has_title():
    assert hasattr(lobj_Source, "title")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj_source_has_publishedIn():
    assert hasattr(lobj_Source, "publishedIn")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "publishedIn" in klass.__dict__:
            descriptor = klass.__dict__["publishedIn"]
            break
    assert isinstance(descriptor, property)

def test_lobj_source_has_id():
    assert hasattr(lobj_Source, "id")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_source_has_publishedBy():
    assert hasattr(lobj_Source, "publishedBy")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "publishedBy" in klass.__dict__:
            descriptor = klass.__dict__["publishedBy"]
            break
    assert isinstance(descriptor, property)

def test_lobj_source_has_pp():
    assert hasattr(lobj_Source, "pp")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "pp" in klass.__dict__:
            descriptor = klass.__dict__["pp"]
            break
    assert isinstance(descriptor, property)

def test_lobj_source_has_subtitle():
    assert hasattr(lobj_Source, "subtitle")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "subtitle" in klass.__dict__:
            descriptor = klass.__dict__["subtitle"]
            break
    assert isinstance(descriptor, property)

def test_lobj_source_has_publishDate():
    assert hasattr(lobj_Source, "publishDate")
    descriptor = None
    for klass in lobj_Source.__mro__:
        if "publishDate" in klass.__dict__:
            descriptor = klass.__dict__["publishDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj_corrblock_is_not_abstract():
    assert not inspect.isabstract(lobj_CorrBlock)


def test_lobj_corrblock_constructor_exists():
    assert callable(lobj_CorrBlock.__init__)


def test_lobj_corrblock_constructor_args():
    sig = inspect.signature(lobj_CorrBlock.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lobj_corrblock_has_id():
    assert hasattr(lobj_CorrBlock, "id")
    descriptor = None
    for klass in lobj_CorrBlock.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_lobj_titlemeta_is_not_abstract():
    assert not inspect.isabstract(lobj_TitleMeta)


def test_lobj_titlemeta_constructor_exists():
    assert callable(lobj_TitleMeta.__init__)


def test_lobj_titlemeta_constructor_args():
    sig = inspect.signature(lobj_TitleMeta.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_lobj_titlemeta_has_id():
    assert hasattr(lobj_TitleMeta, "id")
    descriptor = None
    for klass in lobj_TitleMeta.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_titlemeta_has_title():
    assert hasattr(lobj_TitleMeta, "title")
    descriptor = None
    for klass in lobj_TitleMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lobj_accesscontrol_is_not_abstract():
    assert not inspect.isabstract(lobj_AccessControl)


def test_lobj_accesscontrol_constructor_exists():
    assert callable(lobj_AccessControl.__init__)


def test_lobj_accesscontrol_constructor_args():
    sig = inspect.signature(lobj_AccessControl.__init__)
    params = list(sig.parameters.keys())
    assert "lastStatusChange" in params, "Missing parameter 'lastStatusChange'"
    assert "lastModified" in params, "Missing parameter 'lastModified'"
    assert "id" in params, "Missing parameter 'id'"
    assert "status" in params, "Missing parameter 'status'"
    assert "globalAccess" in params, "Missing parameter 'globalAccess'"

def test_lobj_accesscontrol_has_lastStatusChange():
    assert hasattr(lobj_AccessControl, "lastStatusChange")
    descriptor = None
    for klass in lobj_AccessControl.__mro__:
        if "lastStatusChange" in klass.__dict__:
            descriptor = klass.__dict__["lastStatusChange"]
            break
    assert isinstance(descriptor, property)

def test_lobj_accesscontrol_has_lastModified():
    assert hasattr(lobj_AccessControl, "lastModified")
    descriptor = None
    for klass in lobj_AccessControl.__mro__:
        if "lastModified" in klass.__dict__:
            descriptor = klass.__dict__["lastModified"]
            break
    assert isinstance(descriptor, property)

def test_lobj_accesscontrol_has_id():
    assert hasattr(lobj_AccessControl, "id")
    descriptor = None
    for klass in lobj_AccessControl.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_accesscontrol_has_status():
    assert hasattr(lobj_AccessControl, "status")
    descriptor = None
    for klass in lobj_AccessControl.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_lobj_accesscontrol_has_globalAccess():
    assert hasattr(lobj_AccessControl, "globalAccess")
    descriptor = None
    for klass in lobj_AccessControl.__mro__:
        if "globalAccess" in klass.__dict__:
            descriptor = klass.__dict__["globalAccess"]
            break
    assert isinstance(descriptor, property)



def test_lobj_externalmetadata_is_not_abstract():
    assert not inspect.isabstract(lobj_ExternalMetadata)


def test_lobj_externalmetadata_constructor_exists():
    assert callable(lobj_ExternalMetadata.__init__)


def test_lobj_externalmetadata_constructor_args():
    sig = inspect.signature(lobj_ExternalMetadata.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "file" in params, "Missing parameter 'file'"
    assert "ref" in params, "Missing parameter 'ref'"

def test_lobj_externalmetadata_has_id():
    assert hasattr(lobj_ExternalMetadata, "id")
    descriptor = None
    for klass in lobj_ExternalMetadata.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_externalmetadata_has_file():
    assert hasattr(lobj_ExternalMetadata, "file")
    descriptor = None
    for klass in lobj_ExternalMetadata.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_lobj_externalmetadata_has_ref():
    assert hasattr(lobj_ExternalMetadata, "ref")
    descriptor = None
    for klass in lobj_ExternalMetadata.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_learningobject_is_not_abstract():
    assert not inspect.isabstract(LearningObject)


def test_learningobject_constructor_exists():
    assert callable(LearningObject.__init__)


def test_learningobject_constructor_args():
    sig = inspect.signature(LearningObject.__init__)
    params = list(sig.parameters.keys())



def test_lobj_lumeta_is_not_abstract():
    assert not inspect.isabstract(lobj_LuMeta)


def test_lobj_lumeta_constructor_exists():
    assert callable(lobj_LuMeta.__init__)


def test_lobj_lumeta_constructor_args():
    sig = inspect.signature(lobj_LuMeta.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj_lumeta_has_creationDate():
    assert hasattr(lobj_LuMeta, "creationDate")
    descriptor = None
    for klass in lobj_LuMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj_resrcfile_is_not_abstract():
    assert not inspect.isabstract(lobj_ResrcFile)


def test_lobj_resrcfile_constructor_exists():
    assert callable(lobj_ResrcFile.__init__)


def test_lobj_resrcfile_constructor_args():
    sig = inspect.signature(lobj_ResrcFile.__init__)
    params = list(sig.parameters.keys())
    assert "filesize" in params, "Missing parameter 'filesize'"
    assert "file_tn" in params, "Missing parameter 'file_tn'"
    assert "originalextension" in params, "Missing parameter 'originalextension'"
    assert "file" in params, "Missing parameter 'file'"
    assert "resrcHref" in params, "Missing parameter 'resrcHref'"

def test_lobj_resrcfile_has_filesize():
    assert hasattr(lobj_ResrcFile, "filesize")
    descriptor = None
    for klass in lobj_ResrcFile.__mro__:
        if "filesize" in klass.__dict__:
            descriptor = klass.__dict__["filesize"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfile_has_file_tn():
    assert hasattr(lobj_ResrcFile, "file_tn")
    descriptor = None
    for klass in lobj_ResrcFile.__mro__:
        if "file_tn" in klass.__dict__:
            descriptor = klass.__dict__["file_tn"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfile_has_originalextension():
    assert hasattr(lobj_ResrcFile, "originalextension")
    descriptor = None
    for klass in lobj_ResrcFile.__mro__:
        if "originalextension" in klass.__dict__:
            descriptor = klass.__dict__["originalextension"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfile_has_file():
    assert hasattr(lobj_ResrcFile, "file")
    descriptor = None
    for klass in lobj_ResrcFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcfile_has_resrcHref():
    assert hasattr(lobj_ResrcFile, "resrcHref")
    descriptor = None
    for klass in lobj_ResrcFile.__mro__:
        if "resrcHref" in klass.__dict__:
            descriptor = klass.__dict__["resrcHref"]
            break
    assert isinstance(descriptor, property)



def test_lobj_resrcmeta_is_not_abstract():
    assert not inspect.isabstract(lobj_ResrcMeta)


def test_lobj_resrcmeta_constructor_exists():
    assert callable(lobj_ResrcMeta.__init__)


def test_lobj_resrcmeta_constructor_args():
    sig = inspect.signature(lobj_ResrcMeta.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "description" in params, "Missing parameter 'description'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "title" in params, "Missing parameter 'title'"
    assert "lastModified" in params, "Missing parameter 'lastModified'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj_resrcmeta_has_parameters():
    assert hasattr(lobj_ResrcMeta, "parameters")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_height():
    assert hasattr(lobj_ResrcMeta, "height")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_width():
    assert hasattr(lobj_ResrcMeta, "width")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_description():
    assert hasattr(lobj_ResrcMeta, "description")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_filename():
    assert hasattr(lobj_ResrcMeta, "filename")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_keywords():
    assert hasattr(lobj_ResrcMeta, "keywords")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_title():
    assert hasattr(lobj_ResrcMeta, "title")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_lastModified():
    assert hasattr(lobj_ResrcMeta, "lastModified")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "lastModified" in klass.__dict__:
            descriptor = klass.__dict__["lastModified"]
            break
    assert isinstance(descriptor, property)

def test_lobj_resrcmeta_has_creationDate():
    assert hasattr(lobj_ResrcMeta, "creationDate")
    descriptor = None
    for klass in lobj_ResrcMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj_course_is_not_abstract():
    assert not inspect.isabstract(lobj_Course)


def test_lobj_course_constructor_exists():
    assert callable(lobj_Course.__init__)


def test_lobj_course_constructor_args():
    sig = inspect.signature(lobj_Course.__init__)
    params = list(sig.parameters.keys())
    assert "outlineAsXml" in params, "Missing parameter 'outlineAsXml'"

def test_lobj_course_has_outlineAsXml():
    assert hasattr(lobj_Course, "outlineAsXml")
    descriptor = None
    for klass in lobj_Course.__mro__:
        if "outlineAsXml" in klass.__dict__:
            descriptor = klass.__dict__["outlineAsXml"]
            break
    assert isinstance(descriptor, property)



def test_lobj_blockmeta_is_not_abstract():
    assert not inspect.isabstract(lobj_BlockMeta)


def test_lobj_blockmeta_constructor_exists():
    assert callable(lobj_BlockMeta.__init__)


def test_lobj_blockmeta_constructor_args():
    sig = inspect.signature(lobj_BlockMeta.__init__)
    params = list(sig.parameters.keys())
    assert "rendering" in params, "Missing parameter 'rendering'"
    assert "lod" in params, "Missing parameter 'lod'"
    assert "lastModified" in params, "Missing parameter 'lastModified'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj_blockmeta_has_rendering():
    assert hasattr(lobj_BlockMeta, "rendering")
    descriptor = None
    for klass in lobj_BlockMeta.__mro__:
        if "rendering" in klass.__dict__:
            descriptor = klass.__dict__["rendering"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blockmeta_has_lod():
    assert hasattr(lobj_BlockMeta, "lod")
    descriptor = None
    for klass in lobj_BlockMeta.__mro__:
        if "lod" in klass.__dict__:
            descriptor = klass.__dict__["lod"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blockmeta_has_lastModified():
    assert hasattr(lobj_BlockMeta, "lastModified")
    descriptor = None
    for klass in lobj_BlockMeta.__mro__:
        if "lastModified" in klass.__dict__:
            descriptor = klass.__dict__["lastModified"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blockmeta_has_creationDate():
    assert hasattr(lobj_BlockMeta, "creationDate")
    descriptor = None
    for klass in lobj_BlockMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj_modulefolder_is_not_abstract():
    assert not inspect.isabstract(lobj_ModuleFolder)


def test_lobj_modulefolder_constructor_exists():
    assert callable(lobj_ModuleFolder.__init__)


def test_lobj_modulefolder_constructor_args():
    sig = inspect.signature(lobj_ModuleFolder.__init__)
    params = list(sig.parameters.keys())



def test_lobj_module_is_not_abstract():
    assert not inspect.isabstract(lobj_Module)


def test_lobj_module_constructor_exists():
    assert callable(lobj_Module.__init__)


def test_lobj_module_constructor_args():
    sig = inspect.signature(lobj_Module.__init__)
    params = list(sig.parameters.keys())
    assert "treeAsXml" in params, "Missing parameter 'treeAsXml'"
    assert "moduleFile" in params, "Missing parameter 'moduleFile'"

def test_lobj_module_has_treeAsXml():
    assert hasattr(lobj_Module, "treeAsXml")
    descriptor = None
    for klass in lobj_Module.__mro__:
        if "treeAsXml" in klass.__dict__:
            descriptor = klass.__dict__["treeAsXml"]
            break
    assert isinstance(descriptor, property)

def test_lobj_module_has_moduleFile():
    assert hasattr(lobj_Module, "moduleFile")
    descriptor = None
    for klass in lobj_Module.__mro__:
        if "moduleFile" in klass.__dict__:
            descriptor = klass.__dict__["moduleFile"]
            break
    assert isinstance(descriptor, property)



def test_lobj_blockfolder_is_not_abstract():
    assert not inspect.isabstract(lobj_BlockFolder)


def test_lobj_blockfolder_constructor_exists():
    assert callable(lobj_BlockFolder.__init__)


def test_lobj_blockfolder_constructor_args():
    sig = inspect.signature(lobj_BlockFolder.__init__)
    params = list(sig.parameters.keys())



def test_lobj_learningunit_is_not_abstract():
    assert not inspect.isabstract(lobj_LearningUnit)


def test_lobj_learningunit_constructor_exists():
    assert callable(lobj_LearningUnit.__init__)


def test_lobj_learningunit_constructor_args():
    sig = inspect.signature(lobj_LearningUnit.__init__)
    params = list(sig.parameters.keys())
    assert "luFile" in params, "Missing parameter 'luFile'"
    assert "treeAsXml" in params, "Missing parameter 'treeAsXml'"

def test_lobj_learningunit_has_luFile():
    assert hasattr(lobj_LearningUnit, "luFile")
    descriptor = None
    for klass in lobj_LearningUnit.__mro__:
        if "luFile" in klass.__dict__:
            descriptor = klass.__dict__["luFile"]
            break
    assert isinstance(descriptor, property)

def test_lobj_learningunit_has_treeAsXml():
    assert hasattr(lobj_LearningUnit, "treeAsXml")
    descriptor = None
    for klass in lobj_LearningUnit.__mro__:
        if "treeAsXml" in klass.__dict__:
            descriptor = klass.__dict__["treeAsXml"]
            break
    assert isinstance(descriptor, property)



def test_lobj_coursemeta_is_not_abstract():
    assert not inspect.isabstract(lobj_CourseMeta)


def test_lobj_coursemeta_constructor_exists():
    assert callable(lobj_CourseMeta.__init__)


def test_lobj_coursemeta_constructor_args():
    sig = inspect.signature(lobj_CourseMeta.__init__)
    params = list(sig.parameters.keys())
    assert "columnfilterasxml" in params, "Missing parameter 'columnfilterasxml'"
    assert "hours" in params, "Missing parameter 'hours'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "lvanr" in params, "Missing parameter 'lvanr'"
    assert "fromext" in params, "Missing parameter 'fromext'"

def test_lobj_coursemeta_has_columnfilterasxml():
    assert hasattr(lobj_CourseMeta, "columnfilterasxml")
    descriptor = None
    for klass in lobj_CourseMeta.__mro__:
        if "columnfilterasxml" in klass.__dict__:
            descriptor = klass.__dict__["columnfilterasxml"]
            break
    assert isinstance(descriptor, property)

def test_lobj_coursemeta_has_hours():
    assert hasattr(lobj_CourseMeta, "hours")
    descriptor = None
    for klass in lobj_CourseMeta.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_lobj_coursemeta_has_creationDate():
    assert hasattr(lobj_CourseMeta, "creationDate")
    descriptor = None
    for klass in lobj_CourseMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_lobj_coursemeta_has_lvanr():
    assert hasattr(lobj_CourseMeta, "lvanr")
    descriptor = None
    for klass in lobj_CourseMeta.__mro__:
        if "lvanr" in klass.__dict__:
            descriptor = klass.__dict__["lvanr"]
            break
    assert isinstance(descriptor, property)

def test_lobj_coursemeta_has_fromext():
    assert hasattr(lobj_CourseMeta, "fromext")
    descriptor = None
    for klass in lobj_CourseMeta.__mro__:
        if "fromext" in klass.__dict__:
            descriptor = klass.__dict__["fromext"]
            break
    assert isinstance(descriptor, property)



def test_lobj_theme_is_not_abstract():
    assert not inspect.isabstract(lobj_Theme)


def test_lobj_theme_constructor_exists():
    assert callable(lobj_Theme.__init__)


def test_lobj_theme_constructor_args():
    sig = inspect.signature(lobj_Theme.__init__)
    params = list(sig.parameters.keys())



def test_lobj_foldermeta_is_not_abstract():
    assert not inspect.isabstract(lobj_FolderMeta)


def test_lobj_foldermeta_constructor_exists():
    assert callable(lobj_FolderMeta.__init__)


def test_lobj_foldermeta_constructor_args():
    sig = inspect.signature(lobj_FolderMeta.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj_foldermeta_has_description():
    assert hasattr(lobj_FolderMeta, "description")
    descriptor = None
    for klass in lobj_FolderMeta.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lobj_foldermeta_has_title():
    assert hasattr(lobj_FolderMeta, "title")
    descriptor = None
    for klass in lobj_FolderMeta.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lobj_foldermeta_has_creationDate():
    assert hasattr(lobj_FolderMeta, "creationDate")
    descriptor = None
    for klass in lobj_FolderMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj_resrcfolder_is_not_abstract():
    assert not inspect.isabstract(lobj_ResrcFolder)


def test_lobj_resrcfolder_constructor_exists():
    assert callable(lobj_ResrcFolder.__init__)


def test_lobj_resrcfolder_constructor_args():
    sig = inspect.signature(lobj_ResrcFolder.__init__)
    params = list(sig.parameters.keys())
    assert "deleteScheduled" in params, "Missing parameter 'deleteScheduled'"

def test_lobj_resrcfolder_has_deleteScheduled():
    assert hasattr(lobj_ResrcFolder, "deleteScheduled")
    descriptor = None
    for klass in lobj_ResrcFolder.__mro__:
        if "deleteScheduled" in klass.__dict__:
            descriptor = klass.__dict__["deleteScheduled"]
            break
    assert isinstance(descriptor, property)



def test_lobj_blockaudiofile_is_not_abstract():
    assert not inspect.isabstract(lobj_BlockAudiofile)


def test_lobj_blockaudiofile_constructor_exists():
    assert callable(lobj_BlockAudiofile.__init__)


def test_lobj_blockaudiofile_constructor_args():
    sig = inspect.signature(lobj_BlockAudiofile.__init__)
    params = list(sig.parameters.keys())
    assert "originalextension" in params, "Missing parameter 'originalextension'"
    assert "resrcHref" in params, "Missing parameter 'resrcHref'"
    assert "filesize" in params, "Missing parameter 'filesize'"
    assert "file" in params, "Missing parameter 'file'"

def test_lobj_blockaudiofile_has_originalextension():
    assert hasattr(lobj_BlockAudiofile, "originalextension")
    descriptor = None
    for klass in lobj_BlockAudiofile.__mro__:
        if "originalextension" in klass.__dict__:
            descriptor = klass.__dict__["originalextension"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blockaudiofile_has_resrcHref():
    assert hasattr(lobj_BlockAudiofile, "resrcHref")
    descriptor = None
    for klass in lobj_BlockAudiofile.__mro__:
        if "resrcHref" in klass.__dict__:
            descriptor = klass.__dict__["resrcHref"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blockaudiofile_has_filesize():
    assert hasattr(lobj_BlockAudiofile, "filesize")
    descriptor = None
    for klass in lobj_BlockAudiofile.__mro__:
        if "filesize" in klass.__dict__:
            descriptor = klass.__dict__["filesize"]
            break
    assert isinstance(descriptor, property)

def test_lobj_blockaudiofile_has_file():
    assert hasattr(lobj_BlockAudiofile, "file")
    descriptor = None
    for klass in lobj_BlockAudiofile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_lobj_category_is_not_abstract():
    assert not inspect.isabstract(lobj_Category)


def test_lobj_category_constructor_exists():
    assert callable(lobj_Category.__init__)


def test_lobj_category_constructor_args():
    sig = inspect.signature(lobj_Category.__init__)
    params = list(sig.parameters.keys())



def test_lobj_modulemeta_is_not_abstract():
    assert not inspect.isabstract(lobj_ModuleMeta)


def test_lobj_modulemeta_constructor_exists():
    assert callable(lobj_ModuleMeta.__init__)


def test_lobj_modulemeta_constructor_args():
    sig = inspect.signature(lobj_ModuleMeta.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_lobj_modulemeta_has_creationDate():
    assert hasattr(lobj_ModuleMeta, "creationDate")
    descriptor = None
    for klass in lobj_ModuleMeta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_lobj_lufolder_is_not_abstract():
    assert not inspect.isabstract(lobj_LuFolder)


def test_lobj_lufolder_constructor_exists():
    assert callable(lobj_LuFolder.__init__)


def test_lobj_lufolder_constructor_args():
    sig = inspect.signature(lobj_LuFolder.__init__)
    params = list(sig.parameters.keys())



def test_lobj_block_is_not_abstract():
    assert not inspect.isabstract(lobj_Block)


def test_lobj_block_constructor_exists():
    assert callable(lobj_Block.__init__)


def test_lobj_block_constructor_args():
    sig = inspect.signature(lobj_Block.__init__)
    params = list(sig.parameters.keys())



def test_lobj_learningobject_is_not_abstract():
    assert not inspect.isabstract(lobj_LearningObject)


def test_lobj_learningobject_constructor_exists():
    assert callable(lobj_LearningObject.__init__)


def test_lobj_learningobject_constructor_args():
    sig = inspect.signature(lobj_LearningObject.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_lobj_learningobject_has_timestamp():
    assert hasattr(lobj_LearningObject, "timestamp")
    descriptor = None
    for klass in lobj_LearningObject.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_lobj_learningobject_has_id():
    assert hasattr(lobj_LearningObject, "id")
    descriptor = None
    for klass in lobj_LearningObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_lobj_learningobject_has_synchronized():
    assert hasattr(lobj_LearningObject, "synchronized")
    descriptor = None
    for klass in lobj_LearningObject.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_lobj_language_is_not_abstract():
    assert not inspect.isabstract(lobj_Language)


def test_lobj_language_constructor_exists():
    assert callable(lobj_Language.__init__)


def test_lobj_language_constructor_args():
    sig = inspect.signature(lobj_Language.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "code" in params, "Missing parameter 'code'"

def test_lobj_language_has_language():
    assert hasattr(lobj_Language, "language")
    descriptor = None
    for klass in lobj_Language.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_lobj_language_has_code():
    assert hasattr(lobj_Language, "code")
    descriptor = None
    for klass in lobj_Language.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_lobj_abstractcontent_is_not_abstract():
    assert not inspect.isabstract(lobj_AbstractContent)


def test_lobj_abstractcontent_constructor_exists():
    assert callable(lobj_AbstractContent.__init__)


def test_lobj_abstractcontent_constructor_args():
    sig = inspect.signature(lobj_AbstractContent.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"

def test_lobj_abstractcontent_has_heading():
    assert hasattr(lobj_AbstractContent, "heading")
    descriptor = None
    for klass in lobj_AbstractContent.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_lobj_hypertextcontent_is_not_abstract():
    assert not inspect.isabstract(lobj_HypertextContent)


def test_lobj_hypertextcontent_constructor_exists():
    assert callable(lobj_HypertextContent.__init__)


def test_lobj_hypertextcontent_constructor_args():
    sig = inspect.signature(lobj_HypertextContent.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_lobj_hypertextcontent_has_content():
    assert hasattr(lobj_HypertextContent, "content")
    descriptor = None
    for klass in lobj_HypertextContent.__mro__:
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



def test_lobj_hypertextblock_is_not_abstract():
    assert not inspect.isabstract(lobj_HypertextBlock)


def test_lobj_hypertextblock_constructor_exists():
    assert callable(lobj_HypertextBlock.__init__)


def test_lobj_hypertextblock_constructor_args():
    sig = inspect.signature(lobj_HypertextBlock.__init__)
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
lobj_InternalRef_strategy = st.builds(
    lobj_InternalRef,
    id=
        safe_text,
    reftype=
        safe_text,
    file=
        safe_text,
    ref=
        safe_text
)
lobj_Publisher_strategy = st.builds(
    lobj_Publisher,
    id=
        safe_text,
    publishername=
        safe_text
)
lobj_PublishInfo_strategy = st.builds(
    lobj_PublishInfo,
    pubdate=
        st.dates(),
    pubsnumber=
        safe_text,
    id=
        safe_text,
    edition=
        safe_text,
    releaseinfo=
        safe_text
)
lobj_Note_strategy = st.builds(
    lobj_Note,
    content=
        safe_text,
    noteAuthor=
        safe_text,
    id=
        safe_text,
    date=
        st.dates()
)
lobj_AuthorizationTypes_strategy = st.builds(
    lobj_AuthorizationTypes,
    authType=
        safe_text,
    id=
        safe_text,
    authTypeDesc=
        safe_text,
    readOnly=
        st.booleans()
)
lobj_Precognition_strategy = st.builds(
    lobj_Precognition,
    precog=
        safe_text,
    id=
        safe_text
)
SimpleDidacMeta_strategy = st.builds(
    SimpleDidacMeta,
)
lobj_Domain_strategy = st.builds(
    lobj_Domain,
    creationDate=
        st.dates(),
    id=
        safe_text,
    serverURL=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
lobj_DidacMeta_strategy = st.builds(
    lobj_DidacMeta,
    goal=
        safe_text
)
lobj_Person_strategy = st.builds(
    lobj_Person,
    honorific=
        safe_text,
    contrib=
        safe_text,
    firstname=
        safe_text,
    id=
        safe_text,
    personblurb=
        safe_text,
    surname=
        safe_text
)
lobj_Author_strategy = st.builds(
    lobj_Author,
    credittype=
        safe_text,
    id=
        safe_text,
    email=
        safe_text
)
lobj_Blocktype_strategy = st.builds(
    lobj_Blocktype,
    creationDate=
        st.dates(),
    styleRef=
        safe_text,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
lobj_Address_strategy = st.builds(
    lobj_Address,
    city=
        safe_text,
    otheraddr=
        safe_text,
    email=
        safe_text,
    postcode=
        safe_text,
    street=
        safe_text,
    fax=
        safe_text,
    id=
        safe_text,
    country=
        safe_text,
    phone=
        safe_text,
    state=
        safe_text
)
lobj_Edition_strategy = st.builds(
    lobj_Edition,
    version=
        safe_text,
    editionNr=
        safe_text,
    editedBy=
        safe_text,
    editionCreationDate=
        st.dates(),
    id=
        safe_text,
    status=
        safe_text,
    lastVersionNumber=
        safe_text
)
lobj_Userauthorization_strategy = st.builds(
    lobj_Userauthorization,
    id=
        safe_text
)
lobj_Affiliation_strategy = st.builds(
    lobj_Affiliation,
    jobtitle=
        safe_text,
    orgname=
        safe_text,
    id=
        safe_text,
    orgdiv=
        safe_text,
    shortaffil=
        safe_text
)
lobj_Sharednotes_strategy = st.builds(
    lobj_Sharednotes,
    id=
        safe_text
)
lobj_User_strategy = st.builds(
    lobj_User,
    lastcoursematerialviewnr=
        safe_text,
    loginname=
        safe_text,
    datafilter=
        safe_text,
    icqnumber=
        safe_text,
    dossierasxml=
        safe_text,
    currlogindate=
        st.dates(),
    lastname=
        safe_text,
    photochanged=
        safe_text,
    matriculationnr=
        safe_text,
    authenticateldap=
        safe_text,
    id=
        safe_text,
    lastcoursematerialnr=
        safe_text,
    inchatsince=
        st.dates(),
    fromext=
        safe_text,
    contchatdate=
        st.dates(),
    lastlogindate=
        st.dates(),
    scn=
        safe_text,
    onlinestatus=
        safe_text,
    languagenr=
        safe_text,
    firstname=
        safe_text,
    entryasxml=
        safe_text,
    icqpassword=
        safe_text,
    photo=
        safe_text,
    onlinedate=
        st.dates(),
    notificationprofileasxml=
        safe_text,
    chatroomnr=
        safe_text,
    password=
        safe_text
)
lobj_ResrcFiletype_strategy = st.builds(
    lobj_ResrcFiletype,
    filetypeImageBif=
        safe_text,
    filetypeDesc=
        safe_text,
    filetypeImageSmall=
        safe_text,
    image=
        st.booleans(),
    applet=
        st.booleans(),
    id=
        safe_text,
    filetypeExtension=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
lobj_ThemeNode_strategy = st.builds(
    lobj_ThemeNode,
)
lobj_LuNode_strategy = st.builds(
    lobj_LuNode,
)
lobj_SimpleDidacMeta_strategy = st.builds(
    lobj_SimpleDidacMeta,
    id=
        safe_text,
    title=
        safe_text,
    description=
        safe_text,
    keywords=
        safe_text
)
lobj_Node_strategy = st.builds(
    lobj_Node,
    id=
        safe_text,
    visible=
        st.booleans()
)
lobj_Item_strategy = st.builds(
    lobj_Item,
    id=
        safe_text,
    luRef=
        safe_text
)
lobj_Coursetype_strategy = st.builds(
    lobj_Coursetype,
    id=
        safe_text,
    title=
        safe_text,
    description=
        safe_text
)
lobj_PresentationBlock_strategy = st.builds(
    lobj_PresentationBlock,
    lod=
        st.integers(),
    rendering=
        safe_text,
    id=
        safe_text
)
AbstractContent_strategy = st.builds(
    AbstractContent,
)
lobj_Source_strategy = st.builds(
    lobj_Source,
    title=
        safe_text,
    publishedIn=
        safe_text,
    id=
        safe_text,
    publishedBy=
        safe_text,
    pp=
        safe_text,
    subtitle=
        safe_text,
    publishDate=
        safe_text
)
lobj_CorrBlock_strategy = st.builds(
    lobj_CorrBlock,
    id=
        safe_text
)
lobj_TitleMeta_strategy = st.builds(
    lobj_TitleMeta,
    id=
        safe_text,
    title=
        safe_text
)
lobj_AccessControl_strategy = st.builds(
    lobj_AccessControl,
    lastStatusChange=
        st.dates(),
    lastModified=
        st.dates(),
    id=
        safe_text,
    status=
        safe_text,
    globalAccess=
        st.booleans()
)
lobj_ExternalMetadata_strategy = st.builds(
    lobj_ExternalMetadata,
    id=
        safe_text,
    file=
        safe_text,
    ref=
        safe_text
)
LearningObject_strategy = st.builds(
    LearningObject,
)
lobj_LuMeta_strategy = st.builds(
    lobj_LuMeta,
    creationDate=
        st.dates()
)
lobj_ResrcFile_strategy = st.builds(
    lobj_ResrcFile,
    filesize=
        st.integers(),
    file_tn=
        safe_text,
    originalextension=
        safe_text,
    file=
        safe_text,
    resrcHref=
        safe_text
)
lobj_ResrcMeta_strategy = st.builds(
    lobj_ResrcMeta,
    parameters=
        safe_text,
    height=
        st.integers(),
    width=
        st.integers(),
    description=
        safe_text,
    filename=
        safe_text,
    keywords=
        safe_text,
    title=
        safe_text,
    lastModified=
        st.dates(),
    creationDate=
        st.dates()
)
lobj_Course_strategy = st.builds(
    lobj_Course,
    outlineAsXml=
        safe_text
)
lobj_BlockMeta_strategy = st.builds(
    lobj_BlockMeta,
    rendering=
        safe_text,
    lod=
        safe_text,
    lastModified=
        st.dates(),
    creationDate=
        st.dates()
)
lobj_ModuleFolder_strategy = st.builds(
    lobj_ModuleFolder,
)
lobj_Module_strategy = st.builds(
    lobj_Module,
    treeAsXml=
        safe_text,
    moduleFile=
        safe_text
)
lobj_BlockFolder_strategy = st.builds(
    lobj_BlockFolder,
)
lobj_LearningUnit_strategy = st.builds(
    lobj_LearningUnit,
    luFile=
        safe_text,
    treeAsXml=
        safe_text
)
lobj_CourseMeta_strategy = st.builds(
    lobj_CourseMeta,
    columnfilterasxml=
        safe_text,
    hours=
        st.integers(),
    creationDate=
        st.dates(),
    lvanr=
        safe_text,
    fromext=
        safe_text
)
lobj_Theme_strategy = st.builds(
    lobj_Theme,
)
lobj_FolderMeta_strategy = st.builds(
    lobj_FolderMeta,
    description=
        safe_text,
    title=
        safe_text,
    creationDate=
        st.dates()
)
lobj_ResrcFolder_strategy = st.builds(
    lobj_ResrcFolder,
    deleteScheduled=
        st.booleans()
)
lobj_BlockAudiofile_strategy = st.builds(
    lobj_BlockAudiofile,
    originalextension=
        safe_text,
    resrcHref=
        safe_text,
    filesize=
        st.integers(),
    file=
        safe_text
)
lobj_Category_strategy = st.builds(
    lobj_Category,
)
lobj_ModuleMeta_strategy = st.builds(
    lobj_ModuleMeta,
    creationDate=
        st.dates()
)
lobj_LuFolder_strategy = st.builds(
    lobj_LuFolder,
)
lobj_Block_strategy = st.builds(
    lobj_Block,
)
lobj_LearningObject_strategy = st.builds(
    lobj_LearningObject,
    timestamp=
        st.dates(),
    id=
        safe_text,
    synchronized=
        st.booleans()
)
lobj_Language_strategy = st.builds(
    lobj_Language,
    language=
        safe_text,
    code=
        safe_text
)
lobj_AbstractContent_strategy = st.builds(
    lobj_AbstractContent,
    heading=
        safe_text
)
lobj_HypertextContent_strategy = st.builds(
    lobj_HypertextContent,
    content=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
lobj_HypertextBlock_strategy = st.builds(
    lobj_HypertextBlock,
)

@given(instance=lobj_InternalRef_strategy)
@settings(max_examples=50)
def test_lobj_internalref_instantiation(instance):
    assert isinstance(instance, lobj_InternalRef)



@given(instance=lobj_InternalRef_strategy)
def test_lobj_internalref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_InternalRef_strategy)
def test_lobj_internalref_reftype_setter(instance):
    original = instance.reftype
    instance.reftype = original
    assert instance.reftype == original



@given(instance=lobj_InternalRef_strategy)
def test_lobj_internalref_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=lobj_InternalRef_strategy)
def test_lobj_internalref_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=lobj_Publisher_strategy)
@settings(max_examples=50)
def test_lobj_publisher_instantiation(instance):
    assert isinstance(instance, lobj_Publisher)



@given(instance=lobj_Publisher_strategy)
def test_lobj_publisher_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Publisher_strategy)
def test_lobj_publisher_publishername_setter(instance):
    original = instance.publishername
    instance.publishername = original
    assert instance.publishername == original

@given(instance=lobj_PublishInfo_strategy)
@settings(max_examples=50)
def test_lobj_publishinfo_instantiation(instance):
    assert isinstance(instance, lobj_PublishInfo)



@given(instance=lobj_PublishInfo_strategy)
def test_lobj_publishinfo_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original



@given(instance=lobj_PublishInfo_strategy)
def test_lobj_publishinfo_pubsnumber_setter(instance):
    original = instance.pubsnumber
    instance.pubsnumber = original
    assert instance.pubsnumber == original



@given(instance=lobj_PublishInfo_strategy)
def test_lobj_publishinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_PublishInfo_strategy)
def test_lobj_publishinfo_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original



@given(instance=lobj_PublishInfo_strategy)
def test_lobj_publishinfo_releaseinfo_setter(instance):
    original = instance.releaseinfo
    instance.releaseinfo = original
    assert instance.releaseinfo == original

@given(instance=lobj_Note_strategy)
@settings(max_examples=50)
def test_lobj_note_instantiation(instance):
    assert isinstance(instance, lobj_Note)



@given(instance=lobj_Note_strategy)
def test_lobj_note_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=lobj_Note_strategy)
def test_lobj_note_noteAuthor_setter(instance):
    original = instance.noteAuthor
    instance.noteAuthor = original
    assert instance.noteAuthor == original



@given(instance=lobj_Note_strategy)
def test_lobj_note_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Note_strategy)
def test_lobj_note_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=lobj_AuthorizationTypes_strategy)
@settings(max_examples=50)
def test_lobj_authorizationtypes_instantiation(instance):
    assert isinstance(instance, lobj_AuthorizationTypes)



@given(instance=lobj_AuthorizationTypes_strategy)
def test_lobj_authorizationtypes_authType_setter(instance):
    original = instance.authType
    instance.authType = original
    assert instance.authType == original



@given(instance=lobj_AuthorizationTypes_strategy)
def test_lobj_authorizationtypes_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_AuthorizationTypes_strategy)
def test_lobj_authorizationtypes_authTypeDesc_setter(instance):
    original = instance.authTypeDesc
    instance.authTypeDesc = original
    assert instance.authTypeDesc == original



@given(instance=lobj_AuthorizationTypes_strategy)
def test_lobj_authorizationtypes_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=lobj_Precognition_strategy)
@settings(max_examples=50)
def test_lobj_precognition_instantiation(instance):
    assert isinstance(instance, lobj_Precognition)



@given(instance=lobj_Precognition_strategy)
def test_lobj_precognition_precog_setter(instance):
    original = instance.precog
    instance.precog = original
    assert instance.precog == original



@given(instance=lobj_Precognition_strategy)
def test_lobj_precognition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleDidacMeta_strategy)
@settings(max_examples=50)
def test_simpledidacmeta_instantiation(instance):
    assert isinstance(instance, SimpleDidacMeta)

@given(instance=lobj_Domain_strategy)
@settings(max_examples=50)
def test_lobj_domain_instantiation(instance):
    assert isinstance(instance, lobj_Domain)



@given(instance=lobj_Domain_strategy)
def test_lobj_domain_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=lobj_Domain_strategy)
def test_lobj_domain_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Domain_strategy)
def test_lobj_domain_serverURL_setter(instance):
    original = instance.serverURL
    instance.serverURL = original
    assert instance.serverURL == original



@given(instance=lobj_Domain_strategy)
def test_lobj_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=lobj_Domain_strategy)
def test_lobj_domain_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj_DidacMeta_strategy)
@settings(max_examples=50)
def test_lobj_didacmeta_instantiation(instance):
    assert isinstance(instance, lobj_DidacMeta)



@given(instance=lobj_DidacMeta_strategy)
def test_lobj_didacmeta_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original

@given(instance=lobj_Person_strategy)
@settings(max_examples=50)
def test_lobj_person_instantiation(instance):
    assert isinstance(instance, lobj_Person)



@given(instance=lobj_Person_strategy)
def test_lobj_person_honorific_setter(instance):
    original = instance.honorific
    instance.honorific = original
    assert instance.honorific == original



@given(instance=lobj_Person_strategy)
def test_lobj_person_contrib_setter(instance):
    original = instance.contrib
    instance.contrib = original
    assert instance.contrib == original



@given(instance=lobj_Person_strategy)
def test_lobj_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=lobj_Person_strategy)
def test_lobj_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Person_strategy)
def test_lobj_person_personblurb_setter(instance):
    original = instance.personblurb
    instance.personblurb = original
    assert instance.personblurb == original



@given(instance=lobj_Person_strategy)
def test_lobj_person_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=lobj_Author_strategy)
@settings(max_examples=50)
def test_lobj_author_instantiation(instance):
    assert isinstance(instance, lobj_Author)



@given(instance=lobj_Author_strategy)
def test_lobj_author_credittype_setter(instance):
    original = instance.credittype
    instance.credittype = original
    assert instance.credittype == original



@given(instance=lobj_Author_strategy)
def test_lobj_author_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Author_strategy)
def test_lobj_author_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=lobj_Blocktype_strategy)
@settings(max_examples=50)
def test_lobj_blocktype_instantiation(instance):
    assert isinstance(instance, lobj_Blocktype)



@given(instance=lobj_Blocktype_strategy)
def test_lobj_blocktype_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=lobj_Blocktype_strategy)
def test_lobj_blocktype_styleRef_setter(instance):
    original = instance.styleRef
    instance.styleRef = original
    assert instance.styleRef == original



@given(instance=lobj_Blocktype_strategy)
def test_lobj_blocktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=lobj_Blocktype_strategy)
def test_lobj_blocktype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Blocktype_strategy)
def test_lobj_blocktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lobj_Address_strategy)
@settings(max_examples=50)
def test_lobj_address_instantiation(instance):
    assert isinstance(instance, lobj_Address)



@given(instance=lobj_Address_strategy)
def test_lobj_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_otheraddr_setter(instance):
    original = instance.otheraddr
    instance.otheraddr = original
    assert instance.otheraddr == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_postcode_setter(instance):
    original = instance.postcode
    instance.postcode = original
    assert instance.postcode == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_fax_setter(instance):
    original = instance.fax
    instance.fax = original
    assert instance.fax == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=lobj_Address_strategy)
def test_lobj_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=lobj_Edition_strategy)
@settings(max_examples=50)
def test_lobj_edition_instantiation(instance):
    assert isinstance(instance, lobj_Edition)



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_editionNr_setter(instance):
    original = instance.editionNr
    instance.editionNr = original
    assert instance.editionNr == original



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_editedBy_setter(instance):
    original = instance.editedBy
    instance.editedBy = original
    assert instance.editedBy == original



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_editionCreationDate_setter(instance):
    original = instance.editionCreationDate
    instance.editionCreationDate = original
    assert instance.editionCreationDate == original



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=lobj_Edition_strategy)
def test_lobj_edition_lastVersionNumber_setter(instance):
    original = instance.lastVersionNumber
    instance.lastVersionNumber = original
    assert instance.lastVersionNumber == original

@given(instance=lobj_Userauthorization_strategy)
@settings(max_examples=50)
def test_lobj_userauthorization_instantiation(instance):
    assert isinstance(instance, lobj_Userauthorization)



@given(instance=lobj_Userauthorization_strategy)
def test_lobj_userauthorization_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj_Affiliation_strategy)
@settings(max_examples=50)
def test_lobj_affiliation_instantiation(instance):
    assert isinstance(instance, lobj_Affiliation)



@given(instance=lobj_Affiliation_strategy)
def test_lobj_affiliation_jobtitle_setter(instance):
    original = instance.jobtitle
    instance.jobtitle = original
    assert instance.jobtitle == original



@given(instance=lobj_Affiliation_strategy)
def test_lobj_affiliation_orgname_setter(instance):
    original = instance.orgname
    instance.orgname = original
    assert instance.orgname == original



@given(instance=lobj_Affiliation_strategy)
def test_lobj_affiliation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Affiliation_strategy)
def test_lobj_affiliation_orgdiv_setter(instance):
    original = instance.orgdiv
    instance.orgdiv = original
    assert instance.orgdiv == original



@given(instance=lobj_Affiliation_strategy)
def test_lobj_affiliation_shortaffil_setter(instance):
    original = instance.shortaffil
    instance.shortaffil = original
    assert instance.shortaffil == original

@given(instance=lobj_Sharednotes_strategy)
@settings(max_examples=50)
def test_lobj_sharednotes_instantiation(instance):
    assert isinstance(instance, lobj_Sharednotes)



@given(instance=lobj_Sharednotes_strategy)
def test_lobj_sharednotes_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj_User_strategy)
@settings(max_examples=50)
def test_lobj_user_instantiation(instance):
    assert isinstance(instance, lobj_User)



@given(instance=lobj_User_strategy)
def test_lobj_user_lastcoursematerialviewnr_setter(instance):
    original = instance.lastcoursematerialviewnr
    instance.lastcoursematerialviewnr = original
    assert instance.lastcoursematerialviewnr == original



@given(instance=lobj_User_strategy)
def test_lobj_user_loginname_setter(instance):
    original = instance.loginname
    instance.loginname = original
    assert instance.loginname == original



@given(instance=lobj_User_strategy)
def test_lobj_user_datafilter_setter(instance):
    original = instance.datafilter
    instance.datafilter = original
    assert instance.datafilter == original



@given(instance=lobj_User_strategy)
def test_lobj_user_icqnumber_setter(instance):
    original = instance.icqnumber
    instance.icqnumber = original
    assert instance.icqnumber == original



@given(instance=lobj_User_strategy)
def test_lobj_user_dossierasxml_setter(instance):
    original = instance.dossierasxml
    instance.dossierasxml = original
    assert instance.dossierasxml == original



@given(instance=lobj_User_strategy)
def test_lobj_user_currlogindate_setter(instance):
    original = instance.currlogindate
    instance.currlogindate = original
    assert instance.currlogindate == original



@given(instance=lobj_User_strategy)
def test_lobj_user_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=lobj_User_strategy)
def test_lobj_user_photochanged_setter(instance):
    original = instance.photochanged
    instance.photochanged = original
    assert instance.photochanged == original



@given(instance=lobj_User_strategy)
def test_lobj_user_matriculationnr_setter(instance):
    original = instance.matriculationnr
    instance.matriculationnr = original
    assert instance.matriculationnr == original



@given(instance=lobj_User_strategy)
def test_lobj_user_authenticateldap_setter(instance):
    original = instance.authenticateldap
    instance.authenticateldap = original
    assert instance.authenticateldap == original



@given(instance=lobj_User_strategy)
def test_lobj_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_User_strategy)
def test_lobj_user_lastcoursematerialnr_setter(instance):
    original = instance.lastcoursematerialnr
    instance.lastcoursematerialnr = original
    assert instance.lastcoursematerialnr == original



@given(instance=lobj_User_strategy)
def test_lobj_user_inchatsince_setter(instance):
    original = instance.inchatsince
    instance.inchatsince = original
    assert instance.inchatsince == original



@given(instance=lobj_User_strategy)
def test_lobj_user_fromext_setter(instance):
    original = instance.fromext
    instance.fromext = original
    assert instance.fromext == original



@given(instance=lobj_User_strategy)
def test_lobj_user_contchatdate_setter(instance):
    original = instance.contchatdate
    instance.contchatdate = original
    assert instance.contchatdate == original



@given(instance=lobj_User_strategy)
def test_lobj_user_lastlogindate_setter(instance):
    original = instance.lastlogindate
    instance.lastlogindate = original
    assert instance.lastlogindate == original



@given(instance=lobj_User_strategy)
def test_lobj_user_scn_setter(instance):
    original = instance.scn
    instance.scn = original
    assert instance.scn == original



@given(instance=lobj_User_strategy)
def test_lobj_user_onlinestatus_setter(instance):
    original = instance.onlinestatus
    instance.onlinestatus = original
    assert instance.onlinestatus == original



@given(instance=lobj_User_strategy)
def test_lobj_user_languagenr_setter(instance):
    original = instance.languagenr
    instance.languagenr = original
    assert instance.languagenr == original



@given(instance=lobj_User_strategy)
def test_lobj_user_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=lobj_User_strategy)
def test_lobj_user_entryasxml_setter(instance):
    original = instance.entryasxml
    instance.entryasxml = original
    assert instance.entryasxml == original



@given(instance=lobj_User_strategy)
def test_lobj_user_icqpassword_setter(instance):
    original = instance.icqpassword
    instance.icqpassword = original
    assert instance.icqpassword == original



@given(instance=lobj_User_strategy)
def test_lobj_user_photo_setter(instance):
    original = instance.photo
    instance.photo = original
    assert instance.photo == original



@given(instance=lobj_User_strategy)
def test_lobj_user_onlinedate_setter(instance):
    original = instance.onlinedate
    instance.onlinedate = original
    assert instance.onlinedate == original



@given(instance=lobj_User_strategy)
def test_lobj_user_notificationprofileasxml_setter(instance):
    original = instance.notificationprofileasxml
    instance.notificationprofileasxml = original
    assert instance.notificationprofileasxml == original



@given(instance=lobj_User_strategy)
def test_lobj_user_chatroomnr_setter(instance):
    original = instance.chatroomnr
    instance.chatroomnr = original
    assert instance.chatroomnr == original



@given(instance=lobj_User_strategy)
def test_lobj_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=lobj_ResrcFiletype_strategy)
@settings(max_examples=50)
def test_lobj_resrcfiletype_instantiation(instance):
    assert isinstance(instance, lobj_ResrcFiletype)



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_filetypeImageBif_setter(instance):
    original = instance.filetypeImageBif
    instance.filetypeImageBif = original
    assert instance.filetypeImageBif == original



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_filetypeDesc_setter(instance):
    original = instance.filetypeDesc
    instance.filetypeDesc = original
    assert instance.filetypeDesc == original



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_filetypeImageSmall_setter(instance):
    original = instance.filetypeImageSmall
    instance.filetypeImageSmall = original
    assert instance.filetypeImageSmall == original



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_applet_setter(instance):
    original = instance.applet
    instance.applet = original
    assert instance.applet == original



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_ResrcFiletype_strategy)
def test_lobj_resrcfiletype_filetypeExtension_setter(instance):
    original = instance.filetypeExtension
    instance.filetypeExtension = original
    assert instance.filetypeExtension == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=lobj_ThemeNode_strategy)
@settings(max_examples=50)
def test_lobj_themenode_instantiation(instance):
    assert isinstance(instance, lobj_ThemeNode)

@given(instance=lobj_LuNode_strategy)
@settings(max_examples=50)
def test_lobj_lunode_instantiation(instance):
    assert isinstance(instance, lobj_LuNode)

@given(instance=lobj_SimpleDidacMeta_strategy)
@settings(max_examples=50)
def test_lobj_simpledidacmeta_instantiation(instance):
    assert isinstance(instance, lobj_SimpleDidacMeta)



@given(instance=lobj_SimpleDidacMeta_strategy)
def test_lobj_simpledidacmeta_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_SimpleDidacMeta_strategy)
def test_lobj_simpledidacmeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=lobj_SimpleDidacMeta_strategy)
def test_lobj_simpledidacmeta_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=lobj_SimpleDidacMeta_strategy)
def test_lobj_simpledidacmeta_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=lobj_Node_strategy)
@settings(max_examples=50)
def test_lobj_node_instantiation(instance):
    assert isinstance(instance, lobj_Node)



@given(instance=lobj_Node_strategy)
def test_lobj_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Node_strategy)
def test_lobj_node_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=lobj_Item_strategy)
@settings(max_examples=50)
def test_lobj_item_instantiation(instance):
    assert isinstance(instance, lobj_Item)



@given(instance=lobj_Item_strategy)
def test_lobj_item_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Item_strategy)
def test_lobj_item_luRef_setter(instance):
    original = instance.luRef
    instance.luRef = original
    assert instance.luRef == original

@given(instance=lobj_Coursetype_strategy)
@settings(max_examples=50)
def test_lobj_coursetype_instantiation(instance):
    assert isinstance(instance, lobj_Coursetype)



@given(instance=lobj_Coursetype_strategy)
def test_lobj_coursetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Coursetype_strategy)
def test_lobj_coursetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=lobj_Coursetype_strategy)
def test_lobj_coursetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=lobj_PresentationBlock_strategy)
@settings(max_examples=50)
def test_lobj_presentationblock_instantiation(instance):
    assert isinstance(instance, lobj_PresentationBlock)



@given(instance=lobj_PresentationBlock_strategy)
def test_lobj_presentationblock_lod_setter(instance):
    original = instance.lod
    instance.lod = original
    assert instance.lod == original



@given(instance=lobj_PresentationBlock_strategy)
def test_lobj_presentationblock_rendering_setter(instance):
    original = instance.rendering
    instance.rendering = original
    assert instance.rendering == original



@given(instance=lobj_PresentationBlock_strategy)
def test_lobj_presentationblock_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractContent_strategy)
@settings(max_examples=50)
def test_abstractcontent_instantiation(instance):
    assert isinstance(instance, AbstractContent)

@given(instance=lobj_Source_strategy)
@settings(max_examples=50)
def test_lobj_source_instantiation(instance):
    assert isinstance(instance, lobj_Source)



@given(instance=lobj_Source_strategy)
def test_lobj_source_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=lobj_Source_strategy)
def test_lobj_source_publishedIn_setter(instance):
    original = instance.publishedIn
    instance.publishedIn = original
    assert instance.publishedIn == original



@given(instance=lobj_Source_strategy)
def test_lobj_source_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_Source_strategy)
def test_lobj_source_publishedBy_setter(instance):
    original = instance.publishedBy
    instance.publishedBy = original
    assert instance.publishedBy == original



@given(instance=lobj_Source_strategy)
def test_lobj_source_pp_setter(instance):
    original = instance.pp
    instance.pp = original
    assert instance.pp == original



@given(instance=lobj_Source_strategy)
def test_lobj_source_subtitle_setter(instance):
    original = instance.subtitle
    instance.subtitle = original
    assert instance.subtitle == original



@given(instance=lobj_Source_strategy)
def test_lobj_source_publishDate_setter(instance):
    original = instance.publishDate
    instance.publishDate = original
    assert instance.publishDate == original

@given(instance=lobj_CorrBlock_strategy)
@settings(max_examples=50)
def test_lobj_corrblock_instantiation(instance):
    assert isinstance(instance, lobj_CorrBlock)



@given(instance=lobj_CorrBlock_strategy)
def test_lobj_corrblock_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=lobj_TitleMeta_strategy)
@settings(max_examples=50)
def test_lobj_titlemeta_instantiation(instance):
    assert isinstance(instance, lobj_TitleMeta)



@given(instance=lobj_TitleMeta_strategy)
def test_lobj_titlemeta_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_TitleMeta_strategy)
def test_lobj_titlemeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lobj_AccessControl_strategy)
@settings(max_examples=50)
def test_lobj_accesscontrol_instantiation(instance):
    assert isinstance(instance, lobj_AccessControl)



@given(instance=lobj_AccessControl_strategy)
def test_lobj_accesscontrol_lastStatusChange_setter(instance):
    original = instance.lastStatusChange
    instance.lastStatusChange = original
    assert instance.lastStatusChange == original



@given(instance=lobj_AccessControl_strategy)
def test_lobj_accesscontrol_lastModified_setter(instance):
    original = instance.lastModified
    instance.lastModified = original
    assert instance.lastModified == original



@given(instance=lobj_AccessControl_strategy)
def test_lobj_accesscontrol_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_AccessControl_strategy)
def test_lobj_accesscontrol_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=lobj_AccessControl_strategy)
def test_lobj_accesscontrol_globalAccess_setter(instance):
    original = instance.globalAccess
    instance.globalAccess = original
    assert instance.globalAccess == original

@given(instance=lobj_ExternalMetadata_strategy)
@settings(max_examples=50)
def test_lobj_externalmetadata_instantiation(instance):
    assert isinstance(instance, lobj_ExternalMetadata)



@given(instance=lobj_ExternalMetadata_strategy)
def test_lobj_externalmetadata_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_ExternalMetadata_strategy)
def test_lobj_externalmetadata_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=lobj_ExternalMetadata_strategy)
def test_lobj_externalmetadata_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=LearningObject_strategy)
@settings(max_examples=50)
def test_learningobject_instantiation(instance):
    assert isinstance(instance, LearningObject)

@given(instance=lobj_LuMeta_strategy)
@settings(max_examples=50)
def test_lobj_lumeta_instantiation(instance):
    assert isinstance(instance, lobj_LuMeta)



@given(instance=lobj_LuMeta_strategy)
def test_lobj_lumeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj_ResrcFile_strategy)
@settings(max_examples=50)
def test_lobj_resrcfile_instantiation(instance):
    assert isinstance(instance, lobj_ResrcFile)



@given(instance=lobj_ResrcFile_strategy)
def test_lobj_resrcfile_filesize_setter(instance):
    original = instance.filesize
    instance.filesize = original
    assert instance.filesize == original



@given(instance=lobj_ResrcFile_strategy)
def test_lobj_resrcfile_file_tn_setter(instance):
    original = instance.file_tn
    instance.file_tn = original
    assert instance.file_tn == original



@given(instance=lobj_ResrcFile_strategy)
def test_lobj_resrcfile_originalextension_setter(instance):
    original = instance.originalextension
    instance.originalextension = original
    assert instance.originalextension == original



@given(instance=lobj_ResrcFile_strategy)
def test_lobj_resrcfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=lobj_ResrcFile_strategy)
def test_lobj_resrcfile_resrcHref_setter(instance):
    original = instance.resrcHref
    instance.resrcHref = original
    assert instance.resrcHref == original

@given(instance=lobj_ResrcMeta_strategy)
@settings(max_examples=50)
def test_lobj_resrcmeta_instantiation(instance):
    assert isinstance(instance, lobj_ResrcMeta)



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_lastModified_setter(instance):
    original = instance.lastModified
    instance.lastModified = original
    assert instance.lastModified == original



@given(instance=lobj_ResrcMeta_strategy)
def test_lobj_resrcmeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj_Course_strategy)
@settings(max_examples=50)
def test_lobj_course_instantiation(instance):
    assert isinstance(instance, lobj_Course)



@given(instance=lobj_Course_strategy)
def test_lobj_course_outlineAsXml_setter(instance):
    original = instance.outlineAsXml
    instance.outlineAsXml = original
    assert instance.outlineAsXml == original

@given(instance=lobj_BlockMeta_strategy)
@settings(max_examples=50)
def test_lobj_blockmeta_instantiation(instance):
    assert isinstance(instance, lobj_BlockMeta)



@given(instance=lobj_BlockMeta_strategy)
def test_lobj_blockmeta_rendering_setter(instance):
    original = instance.rendering
    instance.rendering = original
    assert instance.rendering == original



@given(instance=lobj_BlockMeta_strategy)
def test_lobj_blockmeta_lod_setter(instance):
    original = instance.lod
    instance.lod = original
    assert instance.lod == original



@given(instance=lobj_BlockMeta_strategy)
def test_lobj_blockmeta_lastModified_setter(instance):
    original = instance.lastModified
    instance.lastModified = original
    assert instance.lastModified == original



@given(instance=lobj_BlockMeta_strategy)
def test_lobj_blockmeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj_ModuleFolder_strategy)
@settings(max_examples=50)
def test_lobj_modulefolder_instantiation(instance):
    assert isinstance(instance, lobj_ModuleFolder)

@given(instance=lobj_Module_strategy)
@settings(max_examples=50)
def test_lobj_module_instantiation(instance):
    assert isinstance(instance, lobj_Module)



@given(instance=lobj_Module_strategy)
def test_lobj_module_treeAsXml_setter(instance):
    original = instance.treeAsXml
    instance.treeAsXml = original
    assert instance.treeAsXml == original



@given(instance=lobj_Module_strategy)
def test_lobj_module_moduleFile_setter(instance):
    original = instance.moduleFile
    instance.moduleFile = original
    assert instance.moduleFile == original

@given(instance=lobj_BlockFolder_strategy)
@settings(max_examples=50)
def test_lobj_blockfolder_instantiation(instance):
    assert isinstance(instance, lobj_BlockFolder)

@given(instance=lobj_LearningUnit_strategy)
@settings(max_examples=50)
def test_lobj_learningunit_instantiation(instance):
    assert isinstance(instance, lobj_LearningUnit)



@given(instance=lobj_LearningUnit_strategy)
def test_lobj_learningunit_luFile_setter(instance):
    original = instance.luFile
    instance.luFile = original
    assert instance.luFile == original



@given(instance=lobj_LearningUnit_strategy)
def test_lobj_learningunit_treeAsXml_setter(instance):
    original = instance.treeAsXml
    instance.treeAsXml = original
    assert instance.treeAsXml == original

@given(instance=lobj_CourseMeta_strategy)
@settings(max_examples=50)
def test_lobj_coursemeta_instantiation(instance):
    assert isinstance(instance, lobj_CourseMeta)



@given(instance=lobj_CourseMeta_strategy)
def test_lobj_coursemeta_columnfilterasxml_setter(instance):
    original = instance.columnfilterasxml
    instance.columnfilterasxml = original
    assert instance.columnfilterasxml == original



@given(instance=lobj_CourseMeta_strategy)
def test_lobj_coursemeta_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original



@given(instance=lobj_CourseMeta_strategy)
def test_lobj_coursemeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=lobj_CourseMeta_strategy)
def test_lobj_coursemeta_lvanr_setter(instance):
    original = instance.lvanr
    instance.lvanr = original
    assert instance.lvanr == original



@given(instance=lobj_CourseMeta_strategy)
def test_lobj_coursemeta_fromext_setter(instance):
    original = instance.fromext
    instance.fromext = original
    assert instance.fromext == original

@given(instance=lobj_Theme_strategy)
@settings(max_examples=50)
def test_lobj_theme_instantiation(instance):
    assert isinstance(instance, lobj_Theme)

@given(instance=lobj_FolderMeta_strategy)
@settings(max_examples=50)
def test_lobj_foldermeta_instantiation(instance):
    assert isinstance(instance, lobj_FolderMeta)



@given(instance=lobj_FolderMeta_strategy)
def test_lobj_foldermeta_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=lobj_FolderMeta_strategy)
def test_lobj_foldermeta_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=lobj_FolderMeta_strategy)
def test_lobj_foldermeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj_ResrcFolder_strategy)
@settings(max_examples=50)
def test_lobj_resrcfolder_instantiation(instance):
    assert isinstance(instance, lobj_ResrcFolder)



@given(instance=lobj_ResrcFolder_strategy)
def test_lobj_resrcfolder_deleteScheduled_setter(instance):
    original = instance.deleteScheduled
    instance.deleteScheduled = original
    assert instance.deleteScheduled == original

@given(instance=lobj_BlockAudiofile_strategy)
@settings(max_examples=50)
def test_lobj_blockaudiofile_instantiation(instance):
    assert isinstance(instance, lobj_BlockAudiofile)



@given(instance=lobj_BlockAudiofile_strategy)
def test_lobj_blockaudiofile_originalextension_setter(instance):
    original = instance.originalextension
    instance.originalextension = original
    assert instance.originalextension == original



@given(instance=lobj_BlockAudiofile_strategy)
def test_lobj_blockaudiofile_resrcHref_setter(instance):
    original = instance.resrcHref
    instance.resrcHref = original
    assert instance.resrcHref == original



@given(instance=lobj_BlockAudiofile_strategy)
def test_lobj_blockaudiofile_filesize_setter(instance):
    original = instance.filesize
    instance.filesize = original
    assert instance.filesize == original



@given(instance=lobj_BlockAudiofile_strategy)
def test_lobj_blockaudiofile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=lobj_Category_strategy)
@settings(max_examples=50)
def test_lobj_category_instantiation(instance):
    assert isinstance(instance, lobj_Category)

@given(instance=lobj_ModuleMeta_strategy)
@settings(max_examples=50)
def test_lobj_modulemeta_instantiation(instance):
    assert isinstance(instance, lobj_ModuleMeta)



@given(instance=lobj_ModuleMeta_strategy)
def test_lobj_modulemeta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=lobj_LuFolder_strategy)
@settings(max_examples=50)
def test_lobj_lufolder_instantiation(instance):
    assert isinstance(instance, lobj_LuFolder)

@given(instance=lobj_Block_strategy)
@settings(max_examples=50)
def test_lobj_block_instantiation(instance):
    assert isinstance(instance, lobj_Block)

@given(instance=lobj_LearningObject_strategy)
@settings(max_examples=50)
def test_lobj_learningobject_instantiation(instance):
    assert isinstance(instance, lobj_LearningObject)



@given(instance=lobj_LearningObject_strategy)
def test_lobj_learningobject_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=lobj_LearningObject_strategy)
def test_lobj_learningobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=lobj_LearningObject_strategy)
def test_lobj_learningobject_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=lobj_Language_strategy)
@settings(max_examples=50)
def test_lobj_language_instantiation(instance):
    assert isinstance(instance, lobj_Language)



@given(instance=lobj_Language_strategy)
def test_lobj_language_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=lobj_Language_strategy)
def test_lobj_language_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=lobj_AbstractContent_strategy)
@settings(max_examples=50)
def test_lobj_abstractcontent_instantiation(instance):
    assert isinstance(instance, lobj_AbstractContent)



@given(instance=lobj_AbstractContent_strategy)
def test_lobj_abstractcontent_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=lobj_HypertextContent_strategy)
@settings(max_examples=50)
def test_lobj_hypertextcontent_instantiation(instance):
    assert isinstance(instance, lobj_HypertextContent)



@given(instance=lobj_HypertextContent_strategy)
def test_lobj_hypertextcontent_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=lobj_HypertextBlock_strategy)
@settings(max_examples=50)
def test_lobj_hypertextblock_instantiation(instance):
    assert isinstance(instance, lobj_HypertextBlock)
