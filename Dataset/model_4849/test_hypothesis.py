import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    aml::Value,
    aml::Reliability,
    aml::Start,
    aml::Publisher,
    aml::Relevance,
    aml::Reader,
    aml::QuestionRelationships,
    aml::Period,
    aml::Interval,
    aml::List,
    aml::EvidenceExhibit,
    aml::End,
    aml::EStringToStringMapEntry,
    aml::DocumentRoot,
    aml::Dependent,
    aml::Coverage,
    aml::Creator,
    aml::NationState,
    aml::Question,
    aml::CollectionItem,
    aml::Choice,
    aml::Evidence,
    aml::CreatingTool,
    aml::MetaData,
    aml::ArgumentTemplate,
    aml::Answer,
    aml::Flag,
    aml::Witness,
    aml::Belief,
    aml::Memo,
    aml::Person,
    aml::Annotation,
    aml::DiscoveryMethod,
    aml::AmlDocument,
    aml::Parameter,
    aml::EObject,
    aml::Collection,
    aml::Exhibit,
    aml::Argument,
    aml::Template,
    aml::AggregationRule,
    ObjectType3,
    ObjectType2,
    ObjectType1,
    ObjectType,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_aml::value_is_not_abstract():
    assert not inspect.isabstract(aml::Value)


def test_aml::value_constructor_exists():
    assert callable(aml::Value.__init__)


def test_aml::value_constructor_args():
    sig = inspect.signature(aml::Value.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "type" in params, "Missing parameter 'type'"

def test_aml::value_has_mixed():
    assert hasattr(aml::Value, "mixed")
    descriptor = None
    for klass in aml::Value.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml::value_has_group():
    assert hasattr(aml::Value, "group")
    descriptor = None
    for klass in aml::Value.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::value_has_unit():
    assert hasattr(aml::Value, "unit")
    descriptor = None
    for klass in aml::Value.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_aml::value_has_type():
    assert hasattr(aml::Value, "type")
    descriptor = None
    for klass in aml::Value.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_aml::reliability_is_not_abstract():
    assert not inspect.isabstract(aml::Reliability)


def test_aml::reliability_constructor_exists():
    assert callable(aml::Reliability.__init__)


def test_aml::reliability_constructor_args():
    sig = inspect.signature(aml::Reliability.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml::reliability_has_description():
    assert hasattr(aml::Reliability, "description")
    descriptor = None
    for klass in aml::Reliability.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::reliability_has_ordinal():
    assert hasattr(aml::Reliability, "ordinal")
    descriptor = None
    for klass in aml::Reliability.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml::reliability_has_symbol():
    assert hasattr(aml::Reliability, "symbol")
    descriptor = None
    for klass in aml::Reliability.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml::reliability_has_label():
    assert hasattr(aml::Reliability, "label")
    descriptor = None
    for klass in aml::Reliability.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml::start_is_not_abstract():
    assert not inspect.isabstract(aml::Start)


def test_aml::start_constructor_exists():
    assert callable(aml::Start.__init__)


def test_aml::start_constructor_args():
    sig = inspect.signature(aml::Start.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "scheme" in params, "Missing parameter 'scheme'"

def test_aml::start_has_value():
    assert hasattr(aml::Start, "value")
    descriptor = None
    for klass in aml::Start.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aml::start_has_scheme():
    assert hasattr(aml::Start, "scheme")
    descriptor = None
    for klass in aml::Start.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)



def test_aml::publisher_is_not_abstract():
    assert not inspect.isabstract(aml::Publisher)


def test_aml::publisher_constructor_exists():
    assert callable(aml::Publisher.__init__)


def test_aml::publisher_constructor_args():
    sig = inspect.signature(aml::Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "objectType" in params, "Missing parameter 'objectType'"

def test_aml::publisher_has_description():
    assert hasattr(aml::Publisher, "description")
    descriptor = None
    for klass in aml::Publisher.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::publisher_has_idRef():
    assert hasattr(aml::Publisher, "idRef")
    descriptor = None
    for klass in aml::Publisher.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml::publisher_has_objectType():
    assert hasattr(aml::Publisher, "objectType")
    descriptor = None
    for klass in aml::Publisher.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)



def test_aml::relevance_is_not_abstract():
    assert not inspect.isabstract(aml::Relevance)


def test_aml::relevance_constructor_exists():
    assert callable(aml::Relevance.__init__)


def test_aml::relevance_constructor_args():
    sig = inspect.signature(aml::Relevance.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "description" in params, "Missing parameter 'description'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_aml::relevance_has_label():
    assert hasattr(aml::Relevance, "label")
    descriptor = None
    for klass in aml::Relevance.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::relevance_has_symbol():
    assert hasattr(aml::Relevance, "symbol")
    descriptor = None
    for klass in aml::Relevance.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml::relevance_has_description():
    assert hasattr(aml::Relevance, "description")
    descriptor = None
    for klass in aml::Relevance.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::relevance_has_ordinal():
    assert hasattr(aml::Relevance, "ordinal")
    descriptor = None
    for klass in aml::Relevance.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_aml::reader_is_not_abstract():
    assert not inspect.isabstract(aml::Reader)


def test_aml::reader_constructor_exists():
    assert callable(aml::Reader.__init__)


def test_aml::reader_constructor_args():
    sig = inspect.signature(aml::Reader.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "objectType" in params, "Missing parameter 'objectType'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml::reader_has_description():
    assert hasattr(aml::Reader, "description")
    descriptor = None
    for klass in aml::Reader.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::reader_has_objectType():
    assert hasattr(aml::Reader, "objectType")
    descriptor = None
    for klass in aml::Reader.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)

def test_aml::reader_has_idRef():
    assert hasattr(aml::Reader, "idRef")
    descriptor = None
    for klass in aml::Reader.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml::questionrelationships_is_not_abstract():
    assert not inspect.isabstract(aml::QuestionRelationships)


def test_aml::questionrelationships_constructor_exists():
    assert callable(aml::QuestionRelationships.__init__)


def test_aml::questionrelationships_constructor_args():
    sig = inspect.signature(aml::QuestionRelationships.__init__)
    params = list(sig.parameters.keys())



def test_aml::period_is_not_abstract():
    assert not inspect.isabstract(aml::Period)


def test_aml::period_constructor_exists():
    assert callable(aml::Period.__init__)


def test_aml::period_constructor_args():
    sig = inspect.signature(aml::Period.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml::period_has_group():
    assert hasattr(aml::Period, "group")
    descriptor = None
    for klass in aml::Period.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::period_has_label():
    assert hasattr(aml::Period, "label")
    descriptor = None
    for klass in aml::Period.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml::interval_is_not_abstract():
    assert not inspect.isabstract(aml::Interval)


def test_aml::interval_constructor_exists():
    assert callable(aml::Interval.__init__)


def test_aml::interval_constructor_args():
    sig = inspect.signature(aml::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_aml::interval_has_min():
    assert hasattr(aml::Interval, "min")
    descriptor = None
    for klass in aml::Interval.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_aml::interval_has_max():
    assert hasattr(aml::Interval, "max")
    descriptor = None
    for klass in aml::Interval.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_aml::list_is_not_abstract():
    assert not inspect.isabstract(aml::List)


def test_aml::list_constructor_exists():
    assert callable(aml::List.__init__)


def test_aml::list_constructor_args():
    sig = inspect.signature(aml::List.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_aml::list_has_group():
    assert hasattr(aml::List, "group")
    descriptor = None
    for klass in aml::List.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml::evidenceexhibit_is_not_abstract():
    assert not inspect.isabstract(aml::EvidenceExhibit)


def test_aml::evidenceexhibit_constructor_exists():
    assert callable(aml::EvidenceExhibit.__init__)


def test_aml::evidenceexhibit_constructor_args():
    sig = inspect.signature(aml::EvidenceExhibit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "questionId" in params, "Missing parameter 'questionId'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml::evidenceexhibit_has_value():
    assert hasattr(aml::EvidenceExhibit, "value")
    descriptor = None
    for klass in aml::EvidenceExhibit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aml::evidenceexhibit_has_questionId():
    assert hasattr(aml::EvidenceExhibit, "questionId")
    descriptor = None
    for klass in aml::EvidenceExhibit.__mro__:
        if "questionId" in klass.__dict__:
            descriptor = klass.__dict__["questionId"]
            break
    assert isinstance(descriptor, property)

def test_aml::evidenceexhibit_has_idRef():
    assert hasattr(aml::EvidenceExhibit, "idRef")
    descriptor = None
    for klass in aml::EvidenceExhibit.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml::end_is_not_abstract():
    assert not inspect.isabstract(aml::End)


def test_aml::end_constructor_exists():
    assert callable(aml::End.__init__)


def test_aml::end_constructor_args():
    sig = inspect.signature(aml::End.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "value" in params, "Missing parameter 'value'"

def test_aml::end_has_scheme():
    assert hasattr(aml::End, "scheme")
    descriptor = None
    for klass in aml::End.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)

def test_aml::end_has_value():
    assert hasattr(aml::End, "value")
    descriptor = None
    for klass in aml::End.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aml::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(aml::EStringToStringMapEntry)


def test_aml::estringtostringmapentry_constructor_exists():
    assert callable(aml::EStringToStringMapEntry.__init__)


def test_aml::estringtostringmapentry_constructor_args():
    sig = inspect.signature(aml::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_aml::documentroot_is_not_abstract():
    assert not inspect.isabstract(aml::DocumentRoot)


def test_aml::documentroot_constructor_exists():
    assert callable(aml::DocumentRoot.__init__)


def test_aml::documentroot_constructor_args():
    sig = inspect.signature(aml::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "body" in params, "Missing parameter 'body'"
    assert "email" in params, "Missing parameter 'email'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "date" in params, "Missing parameter 'date'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "region" in params, "Missing parameter 'region'"
    assert "actor" in params, "Missing parameter 'actor'"
    assert "description1" in params, "Missing parameter 'description1'"
    assert "perspective" in params, "Missing parameter 'perspective'"
    assert "event" in params, "Missing parameter 'event'"
    assert "securityMarking" in params, "Missing parameter 'securityMarking'"
    assert "description" in params, "Missing parameter 'description'"
    assert "label1" in params, "Missing parameter 'label1'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "nickName" in params, "Missing parameter 'nickName'"
    assert "label" in params, "Missing parameter 'label'"
    assert "department" in params, "Missing parameter 'department'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "url" in params, "Missing parameter 'url'"
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "rationale" in params, "Missing parameter 'rationale'"

def test_aml::documentroot_has_title():
    assert hasattr(aml::DocumentRoot, "title")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_body():
    assert hasattr(aml::DocumentRoot, "body")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_email():
    assert hasattr(aml::DocumentRoot, "email")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_organization():
    assert hasattr(aml::DocumentRoot, "organization")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_date():
    assert hasattr(aml::DocumentRoot, "date")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_symbol():
    assert hasattr(aml::DocumentRoot, "symbol")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_id():
    assert hasattr(aml::DocumentRoot, "id")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_lastName():
    assert hasattr(aml::DocumentRoot, "lastName")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_region():
    assert hasattr(aml::DocumentRoot, "region")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_actor():
    assert hasattr(aml::DocumentRoot, "actor")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "actor" in klass.__dict__:
            descriptor = klass.__dict__["actor"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_description1():
    assert hasattr(aml::DocumentRoot, "description1")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_perspective():
    assert hasattr(aml::DocumentRoot, "perspective")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "perspective" in klass.__dict__:
            descriptor = klass.__dict__["perspective"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_event():
    assert hasattr(aml::DocumentRoot, "event")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_securityMarking():
    assert hasattr(aml::DocumentRoot, "securityMarking")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "securityMarking" in klass.__dict__:
            descriptor = klass.__dict__["securityMarking"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_description():
    assert hasattr(aml::DocumentRoot, "description")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_label1():
    assert hasattr(aml::DocumentRoot, "label1")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "label1" in klass.__dict__:
            descriptor = klass.__dict__["label1"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_middleName():
    assert hasattr(aml::DocumentRoot, "middleName")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_nickName():
    assert hasattr(aml::DocumentRoot, "nickName")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "nickName" in klass.__dict__:
            descriptor = klass.__dict__["nickName"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_label():
    assert hasattr(aml::DocumentRoot, "label")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_department():
    assert hasattr(aml::DocumentRoot, "department")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_mixed():
    assert hasattr(aml::DocumentRoot, "mixed")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_url():
    assert hasattr(aml::DocumentRoot, "url")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_idRef():
    assert hasattr(aml::DocumentRoot, "idRef")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_subject():
    assert hasattr(aml::DocumentRoot, "subject")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_firstName():
    assert hasattr(aml::DocumentRoot, "firstName")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_aml::documentroot_has_rationale():
    assert hasattr(aml::DocumentRoot, "rationale")
    descriptor = None
    for klass in aml::DocumentRoot.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)



def test_aml::dependent_is_not_abstract():
    assert not inspect.isabstract(aml::Dependent)


def test_aml::dependent_constructor_exists():
    assert callable(aml::Dependent.__init__)


def test_aml::dependent_constructor_args():
    sig = inspect.signature(aml::Dependent.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml::dependent_has_ordinal():
    assert hasattr(aml::Dependent, "ordinal")
    descriptor = None
    for klass in aml::Dependent.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml::dependent_has_idRef():
    assert hasattr(aml::Dependent, "idRef")
    descriptor = None
    for klass in aml::Dependent.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml::coverage_is_not_abstract():
    assert not inspect.isabstract(aml::Coverage)


def test_aml::coverage_constructor_exists():
    assert callable(aml::Coverage.__init__)


def test_aml::coverage_constructor_args():
    sig = inspect.signature(aml::Coverage.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_aml::coverage_has_group():
    assert hasattr(aml::Coverage, "group")
    descriptor = None
    for klass in aml::Coverage.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::coverage_has_mixed():
    assert hasattr(aml::Coverage, "mixed")
    descriptor = None
    for klass in aml::Coverage.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_aml::creator_is_not_abstract():
    assert not inspect.isabstract(aml::Creator)


def test_aml::creator_constructor_exists():
    assert callable(aml::Creator.__init__)


def test_aml::creator_constructor_args():
    sig = inspect.signature(aml::Creator.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "objectType" in params, "Missing parameter 'objectType'"

def test_aml::creator_has_description():
    assert hasattr(aml::Creator, "description")
    descriptor = None
    for klass in aml::Creator.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::creator_has_idRef():
    assert hasattr(aml::Creator, "idRef")
    descriptor = None
    for klass in aml::Creator.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml::creator_has_objectType():
    assert hasattr(aml::Creator, "objectType")
    descriptor = None
    for klass in aml::Creator.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)



def test_aml::nationstate_is_not_abstract():
    assert not inspect.isabstract(aml::NationState)


def test_aml::nationstate_constructor_exists():
    assert callable(aml::NationState.__init__)


def test_aml::nationstate_constructor_args():
    sig = inspect.signature(aml::NationState.__init__)
    params = list(sig.parameters.keys())
    assert "region" in params, "Missing parameter 'region'"
    assert "perspective" in params, "Missing parameter 'perspective'"
    assert "group" in params, "Missing parameter 'group'"
    assert "event" in params, "Missing parameter 'event'"
    assert "actor" in params, "Missing parameter 'actor'"

def test_aml::nationstate_has_region():
    assert hasattr(aml::NationState, "region")
    descriptor = None
    for klass in aml::NationState.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_aml::nationstate_has_perspective():
    assert hasattr(aml::NationState, "perspective")
    descriptor = None
    for klass in aml::NationState.__mro__:
        if "perspective" in klass.__dict__:
            descriptor = klass.__dict__["perspective"]
            break
    assert isinstance(descriptor, property)

def test_aml::nationstate_has_group():
    assert hasattr(aml::NationState, "group")
    descriptor = None
    for klass in aml::NationState.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::nationstate_has_event():
    assert hasattr(aml::NationState, "event")
    descriptor = None
    for klass in aml::NationState.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_aml::nationstate_has_actor():
    assert hasattr(aml::NationState, "actor")
    descriptor = None
    for klass in aml::NationState.__mro__:
        if "actor" in klass.__dict__:
            descriptor = klass.__dict__["actor"]
            break
    assert isinstance(descriptor, property)



def test_aml::question_is_not_abstract():
    assert not inspect.isabstract(aml::Question)


def test_aml::question_constructor_exists():
    assert callable(aml::Question.__init__)


def test_aml::question_constructor_args():
    sig = inspect.signature(aml::Question.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "amplification" in params, "Missing parameter 'amplification'"
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml::question_has_description():
    assert hasattr(aml::Question, "description")
    descriptor = None
    for klass in aml::Question.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::question_has_amplification():
    assert hasattr(aml::Question, "amplification")
    descriptor = None
    for klass in aml::Question.__mro__:
        if "amplification" in klass.__dict__:
            descriptor = klass.__dict__["amplification"]
            break
    assert isinstance(descriptor, property)

def test_aml::question_has_group():
    assert hasattr(aml::Question, "group")
    descriptor = None
    for klass in aml::Question.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::question_has_id():
    assert hasattr(aml::Question, "id")
    descriptor = None
    for klass in aml::Question.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::question_has_label():
    assert hasattr(aml::Question, "label")
    descriptor = None
    for klass in aml::Question.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml::collectionitem_is_not_abstract():
    assert not inspect.isabstract(aml::CollectionItem)


def test_aml::collectionitem_constructor_exists():
    assert callable(aml::CollectionItem.__init__)


def test_aml::collectionitem_constructor_args():
    sig = inspect.signature(aml::CollectionItem.__init__)
    params = list(sig.parameters.keys())
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "objectType" in params, "Missing parameter 'objectType'"

def test_aml::collectionitem_has_idRef():
    assert hasattr(aml::CollectionItem, "idRef")
    descriptor = None
    for klass in aml::CollectionItem.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml::collectionitem_has_ordinal():
    assert hasattr(aml::CollectionItem, "ordinal")
    descriptor = None
    for klass in aml::CollectionItem.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml::collectionitem_has_objectType():
    assert hasattr(aml::CollectionItem, "objectType")
    descriptor = None
    for klass in aml::CollectionItem.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)



def test_aml::choice_is_not_abstract():
    assert not inspect.isabstract(aml::Choice)


def test_aml::choice_constructor_exists():
    assert callable(aml::Choice.__init__)


def test_aml::choice_constructor_args():
    sig = inspect.signature(aml::Choice.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "description" in params, "Missing parameter 'description'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml::choice_has_ordinal():
    assert hasattr(aml::Choice, "ordinal")
    descriptor = None
    for klass in aml::Choice.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml::choice_has_symbol():
    assert hasattr(aml::Choice, "symbol")
    descriptor = None
    for klass in aml::Choice.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml::choice_has_description():
    assert hasattr(aml::Choice, "description")
    descriptor = None
    for klass in aml::Choice.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::choice_has_label():
    assert hasattr(aml::Choice, "label")
    descriptor = None
    for klass in aml::Choice.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml::evidence_is_not_abstract():
    assert not inspect.isabstract(aml::Evidence)


def test_aml::evidence_constructor_exists():
    assert callable(aml::Evidence.__init__)


def test_aml::evidence_constructor_args():
    sig = inspect.signature(aml::Evidence.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml::evidence_has_id():
    assert hasattr(aml::Evidence, "id")
    descriptor = None
    for klass in aml::Evidence.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::evidence_has_ordinal():
    assert hasattr(aml::Evidence, "ordinal")
    descriptor = None
    for klass in aml::Evidence.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml::evidence_has_label():
    assert hasattr(aml::Evidence, "label")
    descriptor = None
    for klass in aml::Evidence.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml::creatingtool_is_not_abstract():
    assert not inspect.isabstract(aml::CreatingTool)


def test_aml::creatingtool_constructor_exists():
    assert callable(aml::CreatingTool.__init__)


def test_aml::creatingtool_constructor_args():
    sig = inspect.signature(aml::CreatingTool.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "label" in params, "Missing parameter 'label'"
    assert "toolType" in params, "Missing parameter 'toolType'"

def test_aml::creatingtool_has_version():
    assert hasattr(aml::CreatingTool, "version")
    descriptor = None
    for klass in aml::CreatingTool.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_aml::creatingtool_has_label():
    assert hasattr(aml::CreatingTool, "label")
    descriptor = None
    for klass in aml::CreatingTool.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::creatingtool_has_toolType():
    assert hasattr(aml::CreatingTool, "toolType")
    descriptor = None
    for klass in aml::CreatingTool.__mro__:
        if "toolType" in klass.__dict__:
            descriptor = klass.__dict__["toolType"]
            break
    assert isinstance(descriptor, property)



def test_aml::metadata_is_not_abstract():
    assert not inspect.isabstract(aml::MetaData)


def test_aml::metadata_constructor_exists():
    assert callable(aml::MetaData.__init__)


def test_aml::metadata_constructor_args():
    sig = inspect.signature(aml::MetaData.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "date" in params, "Missing parameter 'date'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "securityMarking" in params, "Missing parameter 'securityMarking'"
    assert "group" in params, "Missing parameter 'group'"

def test_aml::metadata_has_description():
    assert hasattr(aml::MetaData, "description")
    descriptor = None
    for klass in aml::MetaData.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::metadata_has_title():
    assert hasattr(aml::MetaData, "title")
    descriptor = None
    for klass in aml::MetaData.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_aml::metadata_has_date():
    assert hasattr(aml::MetaData, "date")
    descriptor = None
    for klass in aml::MetaData.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_aml::metadata_has_subject():
    assert hasattr(aml::MetaData, "subject")
    descriptor = None
    for klass in aml::MetaData.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_aml::metadata_has_securityMarking():
    assert hasattr(aml::MetaData, "securityMarking")
    descriptor = None
    for klass in aml::MetaData.__mro__:
        if "securityMarking" in klass.__dict__:
            descriptor = klass.__dict__["securityMarking"]
            break
    assert isinstance(descriptor, property)

def test_aml::metadata_has_group():
    assert hasattr(aml::MetaData, "group")
    descriptor = None
    for klass in aml::MetaData.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml::argumenttemplate_is_not_abstract():
    assert not inspect.isabstract(aml::ArgumentTemplate)


def test_aml::argumenttemplate_constructor_exists():
    assert callable(aml::ArgumentTemplate.__init__)


def test_aml::argumenttemplate_constructor_args():
    sig = inspect.signature(aml::ArgumentTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml::argumenttemplate_has_value():
    assert hasattr(aml::ArgumentTemplate, "value")
    descriptor = None
    for klass in aml::ArgumentTemplate.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aml::argumenttemplate_has_idRef():
    assert hasattr(aml::ArgumentTemplate, "idRef")
    descriptor = None
    for klass in aml::ArgumentTemplate.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml::answer_is_not_abstract():
    assert not inspect.isabstract(aml::Answer)


def test_aml::answer_constructor_exists():
    assert callable(aml::Answer.__init__)


def test_aml::answer_constructor_args():
    sig = inspect.signature(aml::Answer.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "questionId" in params, "Missing parameter 'questionId'"
    assert "rationale" in params, "Missing parameter 'rationale'"

def test_aml::answer_has_group():
    assert hasattr(aml::Answer, "group")
    descriptor = None
    for klass in aml::Answer.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::answer_has_questionId():
    assert hasattr(aml::Answer, "questionId")
    descriptor = None
    for klass in aml::Answer.__mro__:
        if "questionId" in klass.__dict__:
            descriptor = klass.__dict__["questionId"]
            break
    assert isinstance(descriptor, property)

def test_aml::answer_has_rationale():
    assert hasattr(aml::Answer, "rationale")
    descriptor = None
    for klass in aml::Answer.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)



def test_aml::flag_is_not_abstract():
    assert not inspect.isabstract(aml::Flag)


def test_aml::flag_constructor_exists():
    assert callable(aml::Flag.__init__)


def test_aml::flag_constructor_args():
    sig = inspect.signature(aml::Flag.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "label" in params, "Missing parameter 'label'"
    assert "flagType" in params, "Missing parameter 'flagType'"

def test_aml::flag_has_description():
    assert hasattr(aml::Flag, "description")
    descriptor = None
    for klass in aml::Flag.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::flag_has_label():
    assert hasattr(aml::Flag, "label")
    descriptor = None
    for klass in aml::Flag.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::flag_has_flagType():
    assert hasattr(aml::Flag, "flagType")
    descriptor = None
    for klass in aml::Flag.__mro__:
        if "flagType" in klass.__dict__:
            descriptor = klass.__dict__["flagType"]
            break
    assert isinstance(descriptor, property)



def test_aml::witness_is_not_abstract():
    assert not inspect.isabstract(aml::Witness)


def test_aml::witness_constructor_exists():
    assert callable(aml::Witness.__init__)


def test_aml::witness_constructor_args():
    sig = inspect.signature(aml::Witness.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "description" in params, "Missing parameter 'description'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml::witness_has_timestamp():
    assert hasattr(aml::Witness, "timestamp")
    descriptor = None
    for klass in aml::Witness.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_aml::witness_has_description():
    assert hasattr(aml::Witness, "description")
    descriptor = None
    for klass in aml::Witness.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::witness_has_idRef():
    assert hasattr(aml::Witness, "idRef")
    descriptor = None
    for klass in aml::Witness.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml::belief_is_not_abstract():
    assert not inspect.isabstract(aml::Belief)


def test_aml::belief_constructor_exists():
    assert callable(aml::Belief.__init__)


def test_aml::belief_constructor_args():
    sig = inspect.signature(aml::Belief.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_aml::belief_has_label():
    assert hasattr(aml::Belief, "label")
    descriptor = None
    for klass in aml::Belief.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::belief_has_description():
    assert hasattr(aml::Belief, "description")
    descriptor = None
    for klass in aml::Belief.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::belief_has_ordinal():
    assert hasattr(aml::Belief, "ordinal")
    descriptor = None
    for klass in aml::Belief.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml::belief_has_symbol():
    assert hasattr(aml::Belief, "symbol")
    descriptor = None
    for klass in aml::Belief.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_aml::memo_is_not_abstract():
    assert not inspect.isabstract(aml::Memo)


def test_aml::memo_constructor_exists():
    assert callable(aml::Memo.__init__)


def test_aml::memo_constructor_args():
    sig = inspect.signature(aml::Memo.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "body" in params, "Missing parameter 'body'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_aml::memo_has_type():
    assert hasattr(aml::Memo, "type")
    descriptor = None
    for klass in aml::Memo.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_aml::memo_has_body():
    assert hasattr(aml::Memo, "body")
    descriptor = None
    for klass in aml::Memo.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_aml::memo_has_id():
    assert hasattr(aml::Memo, "id")
    descriptor = None
    for klass in aml::Memo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::memo_has_subject():
    assert hasattr(aml::Memo, "subject")
    descriptor = None
    for klass in aml::Memo.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_aml::person_is_not_abstract():
    assert not inspect.isabstract(aml::Person)


def test_aml::person_constructor_exists():
    assert callable(aml::Person.__init__)


def test_aml::person_constructor_args():
    sig = inspect.signature(aml::Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "nickName" in params, "Missing parameter 'nickName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "department" in params, "Missing parameter 'department'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "email" in params, "Missing parameter 'email'"

def test_aml::person_has_id():
    assert hasattr(aml::Person, "id")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_description():
    assert hasattr(aml::Person, "description")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_nickName():
    assert hasattr(aml::Person, "nickName")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "nickName" in klass.__dict__:
            descriptor = klass.__dict__["nickName"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_firstName():
    assert hasattr(aml::Person, "firstName")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_middleName():
    assert hasattr(aml::Person, "middleName")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_department():
    assert hasattr(aml::Person, "department")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_lastName():
    assert hasattr(aml::Person, "lastName")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_organization():
    assert hasattr(aml::Person, "organization")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_aml::person_has_email():
    assert hasattr(aml::Person, "email")
    descriptor = None
    for klass in aml::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_aml::annotation_is_not_abstract():
    assert not inspect.isabstract(aml::Annotation)


def test_aml::annotation_constructor_exists():
    assert callable(aml::Annotation.__init__)


def test_aml::annotation_constructor_args():
    sig = inspect.signature(aml::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_aml::annotation_has_id():
    assert hasattr(aml::Annotation, "id")
    descriptor = None
    for klass in aml::Annotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::annotation_has_mixed():
    assert hasattr(aml::Annotation, "mixed")
    descriptor = None
    for klass in aml::Annotation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml::annotation_has_group():
    assert hasattr(aml::Annotation, "group")
    descriptor = None
    for klass in aml::Annotation.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml::discoverymethod_is_not_abstract():
    assert not inspect.isabstract(aml::DiscoveryMethod)


def test_aml::discoverymethod_constructor_exists():
    assert callable(aml::DiscoveryMethod.__init__)


def test_aml::discoverymethod_constructor_args():
    sig = inspect.signature(aml::DiscoveryMethod.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "url" in params, "Missing parameter 'url'"
    assert "id" in params, "Missing parameter 'id'"
    assert "label" in params, "Missing parameter 'label'"
    assert "autoTrigger" in params, "Missing parameter 'autoTrigger'"
    assert "importType" in params, "Missing parameter 'importType'"

def test_aml::discoverymethod_has_description():
    assert hasattr(aml::DiscoveryMethod, "description")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml::discoverymethod_has_type():
    assert hasattr(aml::DiscoveryMethod, "type")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_aml::discoverymethod_has_url():
    assert hasattr(aml::DiscoveryMethod, "url")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_aml::discoverymethod_has_id():
    assert hasattr(aml::DiscoveryMethod, "id")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml::discoverymethod_has_label():
    assert hasattr(aml::DiscoveryMethod, "label")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::discoverymethod_has_autoTrigger():
    assert hasattr(aml::DiscoveryMethod, "autoTrigger")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "autoTrigger" in klass.__dict__:
            descriptor = klass.__dict__["autoTrigger"]
            break
    assert isinstance(descriptor, property)

def test_aml::discoverymethod_has_importType():
    assert hasattr(aml::DiscoveryMethod, "importType")
    descriptor = None
    for klass in aml::DiscoveryMethod.__mro__:
        if "importType" in klass.__dict__:
            descriptor = klass.__dict__["importType"]
            break
    assert isinstance(descriptor, property)



def test_aml::amldocument_is_not_abstract():
    assert not inspect.isabstract(aml::AmlDocument)


def test_aml::amldocument_constructor_exists():
    assert callable(aml::AmlDocument.__init__)


def test_aml::amldocument_constructor_args():
    sig = inspect.signature(aml::AmlDocument.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "version" in params, "Missing parameter 'version'"

def test_aml::amldocument_has_group():
    assert hasattr(aml::AmlDocument, "group")
    descriptor = None
    for klass in aml::AmlDocument.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::amldocument_has_version():
    assert hasattr(aml::AmlDocument, "version")
    descriptor = None
    for klass in aml::AmlDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_aml::parameter_is_not_abstract():
    assert not inspect.isabstract(aml::Parameter)


def test_aml::parameter_constructor_exists():
    assert callable(aml::Parameter.__init__)


def test_aml::parameter_constructor_args():
    sig = inspect.signature(aml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_aml::parameter_has_symbol():
    assert hasattr(aml::Parameter, "symbol")
    descriptor = None
    for klass in aml::Parameter.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_aml::eobject_is_not_abstract():
    assert not inspect.isabstract(aml::EObject)


def test_aml::eobject_constructor_exists():
    assert callable(aml::EObject.__init__)


def test_aml::eobject_constructor_args():
    sig = inspect.signature(aml::EObject.__init__)
    params = list(sig.parameters.keys())



def test_aml::collection_is_not_abstract():
    assert not inspect.isabstract(aml::Collection)


def test_aml::collection_constructor_exists():
    assert callable(aml::Collection.__init__)


def test_aml::collection_constructor_args():
    sig = inspect.signature(aml::Collection.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "objectType" in params, "Missing parameter 'objectType'"
    assert "group" in params, "Missing parameter 'group'"
    assert "label1" in params, "Missing parameter 'label1'"
    assert "id" in params, "Missing parameter 'id'"

def test_aml::collection_has_label():
    assert hasattr(aml::Collection, "label")
    descriptor = None
    for klass in aml::Collection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml::collection_has_objectType():
    assert hasattr(aml::Collection, "objectType")
    descriptor = None
    for klass in aml::Collection.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)

def test_aml::collection_has_group():
    assert hasattr(aml::Collection, "group")
    descriptor = None
    for klass in aml::Collection.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml::collection_has_label1():
    assert hasattr(aml::Collection, "label1")
    descriptor = None
    for klass in aml::Collection.__mro__:
        if "label1" in klass.__dict__:
            descriptor = klass.__dict__["label1"]
            break
    assert isinstance(descriptor, property)

def test_aml::collection_has_id():
    assert hasattr(aml::Collection, "id")
    descriptor = None
    for klass in aml::Collection.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml::exhibit_is_not_abstract():
    assert not inspect.isabstract(aml::Exhibit)


def test_aml::exhibit_constructor_exists():
    assert callable(aml::Exhibit.__init__)


def test_aml::exhibit_constructor_args():
    sig = inspect.signature(aml::Exhibit.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_aml::exhibit_has_id():
    assert hasattr(aml::Exhibit, "id")
    descriptor = None
    for klass in aml::Exhibit.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml::argument_is_not_abstract():
    assert not inspect.isabstract(aml::Argument)


def test_aml::argument_constructor_exists():
    assert callable(aml::Argument.__init__)


def test_aml::argument_constructor_args():
    sig = inspect.signature(aml::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_aml::argument_has_id():
    assert hasattr(aml::Argument, "id")
    descriptor = None
    for klass in aml::Argument.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml::template_is_not_abstract():
    assert not inspect.isabstract(aml::Template)


def test_aml::template_constructor_exists():
    assert callable(aml::Template.__init__)


def test_aml::template_constructor_args():
    sig = inspect.signature(aml::Template.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_aml::template_has_id():
    assert hasattr(aml::Template, "id")
    descriptor = None
    for klass in aml::Template.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml::aggregationrule_is_not_abstract():
    assert not inspect.isabstract(aml::AggregationRule)


def test_aml::aggregationrule_constructor_exists():
    assert callable(aml::AggregationRule.__init__)


def test_aml::aggregationrule_constructor_args():
    sig = inspect.signature(aml::AggregationRule.__init__)
    params = list(sig.parameters.keys())

def test_objecttype3_exists():
    # Check that the Enumeration exists
    assert ObjectType3 is not None

def test_objecttype3_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType3]
    expected_literals = [
        "group",
        "person",
        "memo",
        "collection",
        "exhibit",
        "discoveryMethod",
        "argument",
        "template",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType3"

def test_objecttype2_exists():
    # Check that the Enumeration exists
    assert ObjectType2 is not None

def test_objecttype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType2]
    expected_literals = [
        "SEQUENTIAL",
        "VERSIONING",
        "MISC",
        "template",
        "argument",
        "group",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType2"

def test_objecttype1_exists():
    # Check that the Enumeration exists
    assert ObjectType1 is not None

def test_objecttype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType1]
    expected_literals = [
        "group",
        "argument",
        "discoveryMethod",
        "memo",
        "collection",
        "template",
        "person",
        "exhibit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType1"

def test_objecttype_exists():
    # Check that the Enumeration exists
    assert ObjectType is not None

def test_objecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType]
    expected_literals = [
        "collection",
        "template",
        "exhibit",
        "group",
        "argument",
        "person",
        "discoveryMethod",
        "memo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Urldir",
        "Template",
        "Url",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
aml::Value_strategy = st.builds(
    aml::Value,
    mixed=
        safe_text,
    group=
        safe_text,
    unit=
        safe_text,
    type=
        safe_text
)
aml::Reliability_strategy = st.builds(
    aml::Reliability,
    description=
        safe_text,
    ordinal=
        safe_text,
    symbol=
        safe_text,
    label=
        safe_text
)
aml::Start_strategy = st.builds(
    aml::Start,
    value=
        safe_text,
    scheme=
        safe_text
)
aml::Publisher_strategy = st.builds(
    aml::Publisher,
    description=
        safe_text,
    idRef=
        safe_text,
    objectType=
        safe_text
)
aml::Relevance_strategy = st.builds(
    aml::Relevance,
    label=
        safe_text,
    symbol=
        safe_text,
    description=
        safe_text,
    ordinal=
        safe_text
)
aml::Reader_strategy = st.builds(
    aml::Reader,
    description=
        safe_text,
    objectType=
        safe_text,
    idRef=
        safe_text
)
aml::QuestionRelationships_strategy = st.builds(
    aml::QuestionRelationships,
)
aml::Period_strategy = st.builds(
    aml::Period,
    group=
        safe_text,
    label=
        safe_text
)
aml::Interval_strategy = st.builds(
    aml::Interval,
    min=
        safe_text,
    max=
        safe_text
)
aml::List_strategy = st.builds(
    aml::List,
    group=
        safe_text
)
aml::EvidenceExhibit_strategy = st.builds(
    aml::EvidenceExhibit,
    value=
        safe_text,
    questionId=
        safe_text,
    idRef=
        safe_text
)
aml::End_strategy = st.builds(
    aml::End,
    scheme=
        safe_text,
    value=
        safe_text
)
aml::EStringToStringMapEntry_strategy = st.builds(
    aml::EStringToStringMapEntry,
)
aml::DocumentRoot_strategy = st.builds(
    aml::DocumentRoot,
    title=
        safe_text,
    body=
        safe_text,
    email=
        safe_text,
    organization=
        safe_text,
    date=
        safe_text,
    symbol=
        safe_text,
    id=
        safe_text,
    lastName=
        safe_text,
    region=
        safe_text,
    actor=
        safe_text,
    description1=
        safe_text,
    perspective=
        safe_text,
    event=
        safe_text,
    securityMarking=
        safe_text,
    description=
        safe_text,
    label1=
        safe_text,
    middleName=
        safe_text,
    nickName=
        safe_text,
    label=
        safe_text,
    department=
        safe_text,
    mixed=
        safe_text,
    url=
        safe_text,
    idRef=
        safe_text,
    subject=
        safe_text,
    firstName=
        safe_text,
    rationale=
        safe_text
)
aml::Dependent_strategy = st.builds(
    aml::Dependent,
    ordinal=
        safe_text,
    idRef=
        safe_text
)
aml::Coverage_strategy = st.builds(
    aml::Coverage,
    group=
        safe_text,
    mixed=
        safe_text
)
aml::Creator_strategy = st.builds(
    aml::Creator,
    description=
        safe_text,
    idRef=
        safe_text,
    objectType=
        safe_text
)
aml::NationState_strategy = st.builds(
    aml::NationState,
    region=
        safe_text,
    perspective=
        safe_text,
    group=
        safe_text,
    event=
        safe_text,
    actor=
        safe_text
)
aml::Question_strategy = st.builds(
    aml::Question,
    description=
        safe_text,
    amplification=
        safe_text,
    group=
        safe_text,
    id=
        safe_text,
    label=
        safe_text
)
aml::CollectionItem_strategy = st.builds(
    aml::CollectionItem,
    idRef=
        safe_text,
    ordinal=
        safe_text,
    objectType=
        safe_text
)
aml::Choice_strategy = st.builds(
    aml::Choice,
    ordinal=
        safe_text,
    symbol=
        safe_text,
    description=
        safe_text,
    label=
        safe_text
)
aml::Evidence_strategy = st.builds(
    aml::Evidence,
    id=
        safe_text,
    ordinal=
        safe_text,
    label=
        safe_text
)
aml::CreatingTool_strategy = st.builds(
    aml::CreatingTool,
    version=
        safe_text,
    label=
        safe_text,
    toolType=
        safe_text
)
aml::MetaData_strategy = st.builds(
    aml::MetaData,
    description=
        safe_text,
    title=
        safe_text,
    date=
        safe_text,
    subject=
        safe_text,
    securityMarking=
        safe_text,
    group=
        safe_text
)
aml::ArgumentTemplate_strategy = st.builds(
    aml::ArgumentTemplate,
    value=
        safe_text,
    idRef=
        safe_text
)
aml::Answer_strategy = st.builds(
    aml::Answer,
    group=
        safe_text,
    questionId=
        safe_text,
    rationale=
        safe_text
)
aml::Flag_strategy = st.builds(
    aml::Flag,
    description=
        safe_text,
    label=
        safe_text,
    flagType=
        safe_text
)
aml::Witness_strategy = st.builds(
    aml::Witness,
    timestamp=
        safe_text,
    description=
        safe_text,
    idRef=
        safe_text
)
aml::Belief_strategy = st.builds(
    aml::Belief,
    label=
        safe_text,
    description=
        safe_text,
    ordinal=
        safe_text,
    symbol=
        safe_text
)
aml::Memo_strategy = st.builds(
    aml::Memo,
    type=
        safe_text,
    body=
        safe_text,
    id=
        safe_text,
    subject=
        safe_text
)
aml::Person_strategy = st.builds(
    aml::Person,
    id=
        safe_text,
    description=
        safe_text,
    nickName=
        safe_text,
    firstName=
        safe_text,
    middleName=
        safe_text,
    department=
        safe_text,
    lastName=
        safe_text,
    organization=
        safe_text,
    email=
        safe_text
)
aml::Annotation_strategy = st.builds(
    aml::Annotation,
    id=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
aml::DiscoveryMethod_strategy = st.builds(
    aml::DiscoveryMethod,
    description=
        safe_text,
    type=
        safe_text,
    url=
        safe_text,
    id=
        safe_text,
    label=
        safe_text,
    autoTrigger=
        safe_text,
    importType=
        safe_text
)
aml::AmlDocument_strategy = st.builds(
    aml::AmlDocument,
    group=
        safe_text,
    version=
        safe_text
)
aml::Parameter_strategy = st.builds(
    aml::Parameter,
    symbol=
        safe_text
)
aml::EObject_strategy = st.builds(
    aml::EObject,
)
aml::Collection_strategy = st.builds(
    aml::Collection,
    label=
        safe_text,
    objectType=
        safe_text,
    group=
        safe_text,
    label1=
        safe_text,
    id=
        safe_text
)
aml::Exhibit_strategy = st.builds(
    aml::Exhibit,
    id=
        safe_text
)
aml::Argument_strategy = st.builds(
    aml::Argument,
    id=
        safe_text
)
aml::Template_strategy = st.builds(
    aml::Template,
    id=
        safe_text
)
aml::AggregationRule_strategy = st.builds(
    aml::AggregationRule,
)

@given(instance=aml::Value_strategy)
@settings(max_examples=50)
def test_aml::value_instantiation(instance):
    assert isinstance(instance, aml::Value)

@given(instance=aml::Value_strategy)
def test_aml::value_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=aml::Value_strategy)
def test_aml::value_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=aml::Value_strategy)
def test_aml::value_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Value_strategy)
def test_aml::value_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::Value_strategy)
def test_aml::value_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=aml::Value_strategy)
def test_aml::value_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=aml::Value_strategy)
def test_aml::value_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=aml::Value_strategy)
def test_aml::value_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aml::Reliability_strategy)
@settings(max_examples=50)
def test_aml::reliability_instantiation(instance):
    assert isinstance(instance, aml::Reliability)

@given(instance=aml::Reliability_strategy)
def test_aml::reliability_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Reliability_strategy)
def test_aml::reliability_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Reliability_strategy)
def test_aml::reliability_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::Reliability_strategy)
def test_aml::reliability_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::Reliability_strategy)
def test_aml::reliability_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=aml::Reliability_strategy)
def test_aml::reliability_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml::Reliability_strategy)
def test_aml::reliability_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Reliability_strategy)
def test_aml::reliability_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Start_strategy)
@settings(max_examples=50)
def test_aml::start_instantiation(instance):
    assert isinstance(instance, aml::Start)

@given(instance=aml::Start_strategy)
def test_aml::start_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aml::Start_strategy)
def test_aml::start_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aml::Start_strategy)
def test_aml::start_scheme_type(instance):
    assert isinstance(instance.scheme, str)


@given(instance=aml::Start_strategy)
def test_aml::start_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=aml::Publisher_strategy)
@settings(max_examples=50)
def test_aml::publisher_instantiation(instance):
    assert isinstance(instance, aml::Publisher)

@given(instance=aml::Publisher_strategy)
def test_aml::publisher_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Publisher_strategy)
def test_aml::publisher_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Publisher_strategy)
def test_aml::publisher_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::Publisher_strategy)
def test_aml::publisher_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::Publisher_strategy)
def test_aml::publisher_objectType_type(instance):
    assert isinstance(instance.objectType, str)


@given(instance=aml::Publisher_strategy)
def test_aml::publisher_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml::Relevance_strategy)
@settings(max_examples=50)
def test_aml::relevance_instantiation(instance):
    assert isinstance(instance, aml::Relevance)

@given(instance=aml::Relevance_strategy)
def test_aml::relevance_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Relevance_strategy)
def test_aml::relevance_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Relevance_strategy)
def test_aml::relevance_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=aml::Relevance_strategy)
def test_aml::relevance_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml::Relevance_strategy)
def test_aml::relevance_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Relevance_strategy)
def test_aml::relevance_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Relevance_strategy)
def test_aml::relevance_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::Relevance_strategy)
def test_aml::relevance_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::Reader_strategy)
@settings(max_examples=50)
def test_aml::reader_instantiation(instance):
    assert isinstance(instance, aml::Reader)

@given(instance=aml::Reader_strategy)
def test_aml::reader_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Reader_strategy)
def test_aml::reader_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Reader_strategy)
def test_aml::reader_objectType_type(instance):
    assert isinstance(instance.objectType, str)


@given(instance=aml::Reader_strategy)
def test_aml::reader_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml::Reader_strategy)
def test_aml::reader_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::Reader_strategy)
def test_aml::reader_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::QuestionRelationships_strategy)
@settings(max_examples=50)
def test_aml::questionrelationships_instantiation(instance):
    assert isinstance(instance, aml::QuestionRelationships)

@given(instance=aml::Period_strategy)
@settings(max_examples=50)
def test_aml::period_instantiation(instance):
    assert isinstance(instance, aml::Period)

@given(instance=aml::Period_strategy)
def test_aml::period_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Period_strategy)
def test_aml::period_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::Period_strategy)
def test_aml::period_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Period_strategy)
def test_aml::period_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Interval_strategy)
@settings(max_examples=50)
def test_aml::interval_instantiation(instance):
    assert isinstance(instance, aml::Interval)

@given(instance=aml::Interval_strategy)
def test_aml::interval_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=aml::Interval_strategy)
def test_aml::interval_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=aml::Interval_strategy)
def test_aml::interval_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=aml::Interval_strategy)
def test_aml::interval_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=aml::List_strategy)
@settings(max_examples=50)
def test_aml::list_instantiation(instance):
    assert isinstance(instance, aml::List)

@given(instance=aml::List_strategy)
def test_aml::list_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::List_strategy)
def test_aml::list_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::EvidenceExhibit_strategy)
@settings(max_examples=50)
def test_aml::evidenceexhibit_instantiation(instance):
    assert isinstance(instance, aml::EvidenceExhibit)

@given(instance=aml::EvidenceExhibit_strategy)
def test_aml::evidenceexhibit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aml::EvidenceExhibit_strategy)
def test_aml::evidenceexhibit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aml::EvidenceExhibit_strategy)
def test_aml::evidenceexhibit_questionId_type(instance):
    assert isinstance(instance.questionId, str)


@given(instance=aml::EvidenceExhibit_strategy)
def test_aml::evidenceexhibit_questionId_setter(instance):
    original = instance.questionId
    instance.questionId = original
    assert instance.questionId == original

@given(instance=aml::EvidenceExhibit_strategy)
def test_aml::evidenceexhibit_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::EvidenceExhibit_strategy)
def test_aml::evidenceexhibit_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::End_strategy)
@settings(max_examples=50)
def test_aml::end_instantiation(instance):
    assert isinstance(instance, aml::End)

@given(instance=aml::End_strategy)
def test_aml::end_scheme_type(instance):
    assert isinstance(instance.scheme, str)


@given(instance=aml::End_strategy)
def test_aml::end_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=aml::End_strategy)
def test_aml::end_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aml::End_strategy)
def test_aml::end_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aml::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_aml::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, aml::EStringToStringMapEntry)

@given(instance=aml::DocumentRoot_strategy)
@settings(max_examples=50)
def test_aml::documentroot_instantiation(instance):
    assert isinstance(instance, aml::DocumentRoot)

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_region_type(instance):
    assert isinstance(instance.region, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_actor_type(instance):
    assert isinstance(instance.actor, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_actor_setter(instance):
    original = instance.actor
    instance.actor = original
    assert instance.actor == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_description1_type(instance):
    assert isinstance(instance.description1, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_perspective_type(instance):
    assert isinstance(instance.perspective, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_perspective_setter(instance):
    original = instance.perspective
    instance.perspective = original
    assert instance.perspective == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_securityMarking_type(instance):
    assert isinstance(instance.securityMarking, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_securityMarking_setter(instance):
    original = instance.securityMarking
    instance.securityMarking = original
    assert instance.securityMarking == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_label1_type(instance):
    assert isinstance(instance.label1, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_label1_setter(instance):
    original = instance.label1
    instance.label1 = original
    assert instance.label1 == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_middleName_type(instance):
    assert isinstance(instance.middleName, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_nickName_type(instance):
    assert isinstance(instance.nickName, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_nickName_setter(instance):
    original = instance.nickName
    instance.nickName = original
    assert instance.nickName == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_department_type(instance):
    assert isinstance(instance.department, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_rationale_type(instance):
    assert isinstance(instance.rationale, str)


@given(instance=aml::DocumentRoot_strategy)
def test_aml::documentroot_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original

@given(instance=aml::Dependent_strategy)
@settings(max_examples=50)
def test_aml::dependent_instantiation(instance):
    assert isinstance(instance, aml::Dependent)

@given(instance=aml::Dependent_strategy)
def test_aml::dependent_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::Dependent_strategy)
def test_aml::dependent_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::Dependent_strategy)
def test_aml::dependent_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::Dependent_strategy)
def test_aml::dependent_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::Coverage_strategy)
@settings(max_examples=50)
def test_aml::coverage_instantiation(instance):
    assert isinstance(instance, aml::Coverage)

@given(instance=aml::Coverage_strategy)
def test_aml::coverage_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Coverage_strategy)
def test_aml::coverage_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::Coverage_strategy)
def test_aml::coverage_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=aml::Coverage_strategy)
def test_aml::coverage_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=aml::Creator_strategy)
@settings(max_examples=50)
def test_aml::creator_instantiation(instance):
    assert isinstance(instance, aml::Creator)

@given(instance=aml::Creator_strategy)
def test_aml::creator_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Creator_strategy)
def test_aml::creator_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Creator_strategy)
def test_aml::creator_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::Creator_strategy)
def test_aml::creator_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::Creator_strategy)
def test_aml::creator_objectType_type(instance):
    assert isinstance(instance.objectType, str)


@given(instance=aml::Creator_strategy)
def test_aml::creator_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml::NationState_strategy)
@settings(max_examples=50)
def test_aml::nationstate_instantiation(instance):
    assert isinstance(instance, aml::NationState)

@given(instance=aml::NationState_strategy)
def test_aml::nationstate_region_type(instance):
    assert isinstance(instance.region, str)


@given(instance=aml::NationState_strategy)
def test_aml::nationstate_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original

@given(instance=aml::NationState_strategy)
def test_aml::nationstate_perspective_type(instance):
    assert isinstance(instance.perspective, str)


@given(instance=aml::NationState_strategy)
def test_aml::nationstate_perspective_setter(instance):
    original = instance.perspective
    instance.perspective = original
    assert instance.perspective == original

@given(instance=aml::NationState_strategy)
def test_aml::nationstate_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::NationState_strategy)
def test_aml::nationstate_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::NationState_strategy)
def test_aml::nationstate_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=aml::NationState_strategy)
def test_aml::nationstate_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=aml::NationState_strategy)
def test_aml::nationstate_actor_type(instance):
    assert isinstance(instance.actor, str)


@given(instance=aml::NationState_strategy)
def test_aml::nationstate_actor_setter(instance):
    original = instance.actor
    instance.actor = original
    assert instance.actor == original

@given(instance=aml::Question_strategy)
@settings(max_examples=50)
def test_aml::question_instantiation(instance):
    assert isinstance(instance, aml::Question)

@given(instance=aml::Question_strategy)
def test_aml::question_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Question_strategy)
def test_aml::question_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Question_strategy)
def test_aml::question_amplification_type(instance):
    assert isinstance(instance.amplification, str)


@given(instance=aml::Question_strategy)
def test_aml::question_amplification_setter(instance):
    original = instance.amplification
    instance.amplification = original
    assert instance.amplification == original

@given(instance=aml::Question_strategy)
def test_aml::question_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Question_strategy)
def test_aml::question_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::Question_strategy)
def test_aml::question_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Question_strategy)
def test_aml::question_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Question_strategy)
def test_aml::question_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Question_strategy)
def test_aml::question_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::CollectionItem_strategy)
@settings(max_examples=50)
def test_aml::collectionitem_instantiation(instance):
    assert isinstance(instance, aml::CollectionItem)

@given(instance=aml::CollectionItem_strategy)
def test_aml::collectionitem_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::CollectionItem_strategy)
def test_aml::collectionitem_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::CollectionItem_strategy)
def test_aml::collectionitem_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::CollectionItem_strategy)
def test_aml::collectionitem_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::CollectionItem_strategy)
def test_aml::collectionitem_objectType_type(instance):
    assert isinstance(instance.objectType, str)


@given(instance=aml::CollectionItem_strategy)
def test_aml::collectionitem_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml::Choice_strategy)
@settings(max_examples=50)
def test_aml::choice_instantiation(instance):
    assert isinstance(instance, aml::Choice)

@given(instance=aml::Choice_strategy)
def test_aml::choice_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::Choice_strategy)
def test_aml::choice_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::Choice_strategy)
def test_aml::choice_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=aml::Choice_strategy)
def test_aml::choice_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml::Choice_strategy)
def test_aml::choice_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Choice_strategy)
def test_aml::choice_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Choice_strategy)
def test_aml::choice_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Choice_strategy)
def test_aml::choice_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Evidence_strategy)
@settings(max_examples=50)
def test_aml::evidence_instantiation(instance):
    assert isinstance(instance, aml::Evidence)

@given(instance=aml::Evidence_strategy)
def test_aml::evidence_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Evidence_strategy)
def test_aml::evidence_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Evidence_strategy)
def test_aml::evidence_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::Evidence_strategy)
def test_aml::evidence_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::Evidence_strategy)
def test_aml::evidence_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Evidence_strategy)
def test_aml::evidence_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::CreatingTool_strategy)
@settings(max_examples=50)
def test_aml::creatingtool_instantiation(instance):
    assert isinstance(instance, aml::CreatingTool)

@given(instance=aml::CreatingTool_strategy)
def test_aml::creatingtool_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=aml::CreatingTool_strategy)
def test_aml::creatingtool_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=aml::CreatingTool_strategy)
def test_aml::creatingtool_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::CreatingTool_strategy)
def test_aml::creatingtool_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::CreatingTool_strategy)
def test_aml::creatingtool_toolType_type(instance):
    assert isinstance(instance.toolType, str)


@given(instance=aml::CreatingTool_strategy)
def test_aml::creatingtool_toolType_setter(instance):
    original = instance.toolType
    instance.toolType = original
    assert instance.toolType == original

@given(instance=aml::MetaData_strategy)
@settings(max_examples=50)
def test_aml::metadata_instantiation(instance):
    assert isinstance(instance, aml::MetaData)

@given(instance=aml::MetaData_strategy)
def test_aml::metadata_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::MetaData_strategy)
def test_aml::metadata_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::MetaData_strategy)
def test_aml::metadata_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=aml::MetaData_strategy)
def test_aml::metadata_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=aml::MetaData_strategy)
def test_aml::metadata_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=aml::MetaData_strategy)
def test_aml::metadata_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=aml::MetaData_strategy)
def test_aml::metadata_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=aml::MetaData_strategy)
def test_aml::metadata_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=aml::MetaData_strategy)
def test_aml::metadata_securityMarking_type(instance):
    assert isinstance(instance.securityMarking, str)


@given(instance=aml::MetaData_strategy)
def test_aml::metadata_securityMarking_setter(instance):
    original = instance.securityMarking
    instance.securityMarking = original
    assert instance.securityMarking == original

@given(instance=aml::MetaData_strategy)
def test_aml::metadata_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::MetaData_strategy)
def test_aml::metadata_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::ArgumentTemplate_strategy)
@settings(max_examples=50)
def test_aml::argumenttemplate_instantiation(instance):
    assert isinstance(instance, aml::ArgumentTemplate)

@given(instance=aml::ArgumentTemplate_strategy)
def test_aml::argumenttemplate_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aml::ArgumentTemplate_strategy)
def test_aml::argumenttemplate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aml::ArgumentTemplate_strategy)
def test_aml::argumenttemplate_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::ArgumentTemplate_strategy)
def test_aml::argumenttemplate_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::Answer_strategy)
@settings(max_examples=50)
def test_aml::answer_instantiation(instance):
    assert isinstance(instance, aml::Answer)

@given(instance=aml::Answer_strategy)
def test_aml::answer_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Answer_strategy)
def test_aml::answer_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::Answer_strategy)
def test_aml::answer_questionId_type(instance):
    assert isinstance(instance.questionId, str)


@given(instance=aml::Answer_strategy)
def test_aml::answer_questionId_setter(instance):
    original = instance.questionId
    instance.questionId = original
    assert instance.questionId == original

@given(instance=aml::Answer_strategy)
def test_aml::answer_rationale_type(instance):
    assert isinstance(instance.rationale, str)


@given(instance=aml::Answer_strategy)
def test_aml::answer_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original

@given(instance=aml::Flag_strategy)
@settings(max_examples=50)
def test_aml::flag_instantiation(instance):
    assert isinstance(instance, aml::Flag)

@given(instance=aml::Flag_strategy)
def test_aml::flag_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Flag_strategy)
def test_aml::flag_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Flag_strategy)
def test_aml::flag_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Flag_strategy)
def test_aml::flag_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Flag_strategy)
def test_aml::flag_flagType_type(instance):
    assert isinstance(instance.flagType, str)


@given(instance=aml::Flag_strategy)
def test_aml::flag_flagType_setter(instance):
    original = instance.flagType
    instance.flagType = original
    assert instance.flagType == original

@given(instance=aml::Witness_strategy)
@settings(max_examples=50)
def test_aml::witness_instantiation(instance):
    assert isinstance(instance, aml::Witness)

@given(instance=aml::Witness_strategy)
def test_aml::witness_timestamp_type(instance):
    assert isinstance(instance.timestamp, str)


@given(instance=aml::Witness_strategy)
def test_aml::witness_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=aml::Witness_strategy)
def test_aml::witness_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Witness_strategy)
def test_aml::witness_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Witness_strategy)
def test_aml::witness_idRef_type(instance):
    assert isinstance(instance.idRef, str)


@given(instance=aml::Witness_strategy)
def test_aml::witness_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml::Belief_strategy)
@settings(max_examples=50)
def test_aml::belief_instantiation(instance):
    assert isinstance(instance, aml::Belief)

@given(instance=aml::Belief_strategy)
def test_aml::belief_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Belief_strategy)
def test_aml::belief_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Belief_strategy)
def test_aml::belief_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Belief_strategy)
def test_aml::belief_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Belief_strategy)
def test_aml::belief_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=aml::Belief_strategy)
def test_aml::belief_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml::Belief_strategy)
def test_aml::belief_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=aml::Belief_strategy)
def test_aml::belief_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml::Memo_strategy)
@settings(max_examples=50)
def test_aml::memo_instantiation(instance):
    assert isinstance(instance, aml::Memo)

@given(instance=aml::Memo_strategy)
def test_aml::memo_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=aml::Memo_strategy)
def test_aml::memo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aml::Memo_strategy)
def test_aml::memo_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=aml::Memo_strategy)
def test_aml::memo_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=aml::Memo_strategy)
def test_aml::memo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Memo_strategy)
def test_aml::memo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Memo_strategy)
def test_aml::memo_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=aml::Memo_strategy)
def test_aml::memo_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=aml::Person_strategy)
@settings(max_examples=50)
def test_aml::person_instantiation(instance):
    assert isinstance(instance, aml::Person)

@given(instance=aml::Person_strategy)
def test_aml::person_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Person_strategy)
def test_aml::person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Person_strategy)
def test_aml::person_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::Person_strategy)
def test_aml::person_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::Person_strategy)
def test_aml::person_nickName_type(instance):
    assert isinstance(instance.nickName, str)


@given(instance=aml::Person_strategy)
def test_aml::person_nickName_setter(instance):
    original = instance.nickName
    instance.nickName = original
    assert instance.nickName == original

@given(instance=aml::Person_strategy)
def test_aml::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=aml::Person_strategy)
def test_aml::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=aml::Person_strategy)
def test_aml::person_middleName_type(instance):
    assert isinstance(instance.middleName, str)


@given(instance=aml::Person_strategy)
def test_aml::person_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original

@given(instance=aml::Person_strategy)
def test_aml::person_department_type(instance):
    assert isinstance(instance.department, str)


@given(instance=aml::Person_strategy)
def test_aml::person_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original

@given(instance=aml::Person_strategy)
def test_aml::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=aml::Person_strategy)
def test_aml::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=aml::Person_strategy)
def test_aml::person_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=aml::Person_strategy)
def test_aml::person_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=aml::Person_strategy)
def test_aml::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=aml::Person_strategy)
def test_aml::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=aml::Annotation_strategy)
@settings(max_examples=50)
def test_aml::annotation_instantiation(instance):
    assert isinstance(instance, aml::Annotation)

@given(instance=aml::Annotation_strategy)
def test_aml::annotation_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Annotation_strategy)
def test_aml::annotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Annotation_strategy)
def test_aml::annotation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=aml::Annotation_strategy)
def test_aml::annotation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=aml::Annotation_strategy)
def test_aml::annotation_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Annotation_strategy)
def test_aml::annotation_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::DiscoveryMethod_strategy)
@settings(max_examples=50)
def test_aml::discoverymethod_instantiation(instance):
    assert isinstance(instance, aml::DiscoveryMethod)

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_autoTrigger_type(instance):
    assert isinstance(instance.autoTrigger, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_autoTrigger_setter(instance):
    original = instance.autoTrigger
    instance.autoTrigger = original
    assert instance.autoTrigger == original

@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_importType_type(instance):
    assert isinstance(instance.importType, str)


@given(instance=aml::DiscoveryMethod_strategy)
def test_aml::discoverymethod_importType_setter(instance):
    original = instance.importType
    instance.importType = original
    assert instance.importType == original

@given(instance=aml::AmlDocument_strategy)
@settings(max_examples=50)
def test_aml::amldocument_instantiation(instance):
    assert isinstance(instance, aml::AmlDocument)

@given(instance=aml::AmlDocument_strategy)
def test_aml::amldocument_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::AmlDocument_strategy)
def test_aml::amldocument_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::AmlDocument_strategy)
def test_aml::amldocument_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=aml::AmlDocument_strategy)
def test_aml::amldocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=aml::Parameter_strategy)
@settings(max_examples=50)
def test_aml::parameter_instantiation(instance):
    assert isinstance(instance, aml::Parameter)

@given(instance=aml::Parameter_strategy)
def test_aml::parameter_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=aml::Parameter_strategy)
def test_aml::parameter_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml::EObject_strategy)
@settings(max_examples=50)
def test_aml::eobject_instantiation(instance):
    assert isinstance(instance, aml::EObject)

@given(instance=aml::Collection_strategy)
@settings(max_examples=50)
def test_aml::collection_instantiation(instance):
    assert isinstance(instance, aml::Collection)

@given(instance=aml::Collection_strategy)
def test_aml::collection_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=aml::Collection_strategy)
def test_aml::collection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml::Collection_strategy)
def test_aml::collection_objectType_type(instance):
    assert isinstance(instance.objectType, str)


@given(instance=aml::Collection_strategy)
def test_aml::collection_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml::Collection_strategy)
def test_aml::collection_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=aml::Collection_strategy)
def test_aml::collection_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml::Collection_strategy)
def test_aml::collection_label1_type(instance):
    assert isinstance(instance.label1, str)


@given(instance=aml::Collection_strategy)
def test_aml::collection_label1_setter(instance):
    original = instance.label1
    instance.label1 = original
    assert instance.label1 == original

@given(instance=aml::Collection_strategy)
def test_aml::collection_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Collection_strategy)
def test_aml::collection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Exhibit_strategy)
@settings(max_examples=50)
def test_aml::exhibit_instantiation(instance):
    assert isinstance(instance, aml::Exhibit)

@given(instance=aml::Exhibit_strategy)
def test_aml::exhibit_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Exhibit_strategy)
def test_aml::exhibit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Argument_strategy)
@settings(max_examples=50)
def test_aml::argument_instantiation(instance):
    assert isinstance(instance, aml::Argument)

@given(instance=aml::Argument_strategy)
def test_aml::argument_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Argument_strategy)
def test_aml::argument_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::Template_strategy)
@settings(max_examples=50)
def test_aml::template_instantiation(instance):
    assert isinstance(instance, aml::Template)

@given(instance=aml::Template_strategy)
def test_aml::template_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aml::Template_strategy)
def test_aml::template_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml::AggregationRule_strategy)
@settings(max_examples=50)
def test_aml::aggregationrule_instantiation(instance):
    assert isinstance(instance, aml::AggregationRule)
