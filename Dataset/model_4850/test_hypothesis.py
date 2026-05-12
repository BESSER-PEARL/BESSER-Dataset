import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    aml_Value,
    aml_Start,
    aml_Reliability,
    aml_Relevance,
    aml_Reader,
    aml_QuestionRelationships,
    aml_Period,
    aml_Publisher,
    aml_List,
    aml_EvidenceExhibit,
    aml_Interval,
    aml_End,
    aml_EStringToStringMapEntry,
    aml_DocumentRoot,
    aml_Dependent,
    aml_NationState,
    aml_Coverage,
    aml_Creator,
    aml_Question,
    aml_CollectionItem,
    aml_Choice,
    aml_ArgumentTemplate,
    aml_Evidence,
    aml_CreatingTool,
    aml_MetaData,
    aml_Answer,
    aml_Flag,
    aml_Witness,
    aml_Belief,
    aml_Memo,
    aml_Person,
    aml_Collection,
    aml_Annotation,
    aml_DiscoveryMethod,
    aml_AmlDocument,
    aml_Parameter,
    aml_EObject,
    aml_AggregationRule,
    aml_Exhibit,
    aml_Argument,
    aml_Template,
    Type,
    ObjectType1,
    ObjectType2,
    ObjectType,
    ObjectType3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_aml_value_is_not_abstract():
    assert not inspect.isabstract(aml_Value)


def test_aml_value_constructor_exists():
    assert callable(aml_Value.__init__)


def test_aml_value_constructor_args():
    sig = inspect.signature(aml_Value.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_aml_value_has_type():
    assert hasattr(aml_Value, "type")
    descriptor = None
    for klass in aml_Value.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_aml_value_has_unit():
    assert hasattr(aml_Value, "unit")
    descriptor = None
    for klass in aml_Value.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_aml_value_has_mixed():
    assert hasattr(aml_Value, "mixed")
    descriptor = None
    for klass in aml_Value.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml_value_has_group():
    assert hasattr(aml_Value, "group")
    descriptor = None
    for klass in aml_Value.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml_start_is_not_abstract():
    assert not inspect.isabstract(aml_Start)


def test_aml_start_constructor_exists():
    assert callable(aml_Start.__init__)


def test_aml_start_constructor_args():
    sig = inspect.signature(aml_Start.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "scheme" in params, "Missing parameter 'scheme'"

def test_aml_start_has_value():
    assert hasattr(aml_Start, "value")
    descriptor = None
    for klass in aml_Start.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aml_start_has_scheme():
    assert hasattr(aml_Start, "scheme")
    descriptor = None
    for klass in aml_Start.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)



def test_aml_reliability_is_not_abstract():
    assert not inspect.isabstract(aml_Reliability)


def test_aml_reliability_constructor_exists():
    assert callable(aml_Reliability.__init__)


def test_aml_reliability_constructor_args():
    sig = inspect.signature(aml_Reliability.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml_reliability_has_description():
    assert hasattr(aml_Reliability, "description")
    descriptor = None
    for klass in aml_Reliability.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_reliability_has_ordinal():
    assert hasattr(aml_Reliability, "ordinal")
    descriptor = None
    for klass in aml_Reliability.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml_reliability_has_symbol():
    assert hasattr(aml_Reliability, "symbol")
    descriptor = None
    for klass in aml_Reliability.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml_reliability_has_label():
    assert hasattr(aml_Reliability, "label")
    descriptor = None
    for klass in aml_Reliability.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml_relevance_is_not_abstract():
    assert not inspect.isabstract(aml_Relevance)


def test_aml_relevance_constructor_exists():
    assert callable(aml_Relevance.__init__)


def test_aml_relevance_constructor_args():
    sig = inspect.signature(aml_Relevance.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "description" in params, "Missing parameter 'description'"

def test_aml_relevance_has_label():
    assert hasattr(aml_Relevance, "label")
    descriptor = None
    for klass in aml_Relevance.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_relevance_has_ordinal():
    assert hasattr(aml_Relevance, "ordinal")
    descriptor = None
    for klass in aml_Relevance.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml_relevance_has_symbol():
    assert hasattr(aml_Relevance, "symbol")
    descriptor = None
    for klass in aml_Relevance.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml_relevance_has_description():
    assert hasattr(aml_Relevance, "description")
    descriptor = None
    for klass in aml_Relevance.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aml_reader_is_not_abstract():
    assert not inspect.isabstract(aml_Reader)


def test_aml_reader_constructor_exists():
    assert callable(aml_Reader.__init__)


def test_aml_reader_constructor_args():
    sig = inspect.signature(aml_Reader.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "objectType" in params, "Missing parameter 'objectType'"

def test_aml_reader_has_description():
    assert hasattr(aml_Reader, "description")
    descriptor = None
    for klass in aml_Reader.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_reader_has_idRef():
    assert hasattr(aml_Reader, "idRef")
    descriptor = None
    for klass in aml_Reader.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml_reader_has_objectType():
    assert hasattr(aml_Reader, "objectType")
    descriptor = None
    for klass in aml_Reader.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)



def test_aml_questionrelationships_is_not_abstract():
    assert not inspect.isabstract(aml_QuestionRelationships)


def test_aml_questionrelationships_constructor_exists():
    assert callable(aml_QuestionRelationships.__init__)


def test_aml_questionrelationships_constructor_args():
    sig = inspect.signature(aml_QuestionRelationships.__init__)
    params = list(sig.parameters.keys())



def test_aml_period_is_not_abstract():
    assert not inspect.isabstract(aml_Period)


def test_aml_period_constructor_exists():
    assert callable(aml_Period.__init__)


def test_aml_period_constructor_args():
    sig = inspect.signature(aml_Period.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "label" in params, "Missing parameter 'label'"

def test_aml_period_has_group():
    assert hasattr(aml_Period, "group")
    descriptor = None
    for klass in aml_Period.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_period_has_label():
    assert hasattr(aml_Period, "label")
    descriptor = None
    for klass in aml_Period.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_aml_publisher_is_not_abstract():
    assert not inspect.isabstract(aml_Publisher)


def test_aml_publisher_constructor_exists():
    assert callable(aml_Publisher.__init__)


def test_aml_publisher_constructor_args():
    sig = inspect.signature(aml_Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "description" in params, "Missing parameter 'description'"
    assert "objectType" in params, "Missing parameter 'objectType'"

def test_aml_publisher_has_idRef():
    assert hasattr(aml_Publisher, "idRef")
    descriptor = None
    for klass in aml_Publisher.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml_publisher_has_description():
    assert hasattr(aml_Publisher, "description")
    descriptor = None
    for klass in aml_Publisher.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_publisher_has_objectType():
    assert hasattr(aml_Publisher, "objectType")
    descriptor = None
    for klass in aml_Publisher.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)



def test_aml_list_is_not_abstract():
    assert not inspect.isabstract(aml_List)


def test_aml_list_constructor_exists():
    assert callable(aml_List.__init__)


def test_aml_list_constructor_args():
    sig = inspect.signature(aml_List.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_aml_list_has_group():
    assert hasattr(aml_List, "group")
    descriptor = None
    for klass in aml_List.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml_evidenceexhibit_is_not_abstract():
    assert not inspect.isabstract(aml_EvidenceExhibit)


def test_aml_evidenceexhibit_constructor_exists():
    assert callable(aml_EvidenceExhibit.__init__)


def test_aml_evidenceexhibit_constructor_args():
    sig = inspect.signature(aml_EvidenceExhibit.__init__)
    params = list(sig.parameters.keys())
    assert "questionId" in params, "Missing parameter 'questionId'"
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "value" in params, "Missing parameter 'value'"

def test_aml_evidenceexhibit_has_questionId():
    assert hasattr(aml_EvidenceExhibit, "questionId")
    descriptor = None
    for klass in aml_EvidenceExhibit.__mro__:
        if "questionId" in klass.__dict__:
            descriptor = klass.__dict__["questionId"]
            break
    assert isinstance(descriptor, property)

def test_aml_evidenceexhibit_has_idRef():
    assert hasattr(aml_EvidenceExhibit, "idRef")
    descriptor = None
    for klass in aml_EvidenceExhibit.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml_evidenceexhibit_has_value():
    assert hasattr(aml_EvidenceExhibit, "value")
    descriptor = None
    for klass in aml_EvidenceExhibit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aml_interval_is_not_abstract():
    assert not inspect.isabstract(aml_Interval)


def test_aml_interval_constructor_exists():
    assert callable(aml_Interval.__init__)


def test_aml_interval_constructor_args():
    sig = inspect.signature(aml_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_aml_interval_has_min():
    assert hasattr(aml_Interval, "min")
    descriptor = None
    for klass in aml_Interval.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_aml_interval_has_max():
    assert hasattr(aml_Interval, "max")
    descriptor = None
    for klass in aml_Interval.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_aml_end_is_not_abstract():
    assert not inspect.isabstract(aml_End)


def test_aml_end_constructor_exists():
    assert callable(aml_End.__init__)


def test_aml_end_constructor_args():
    sig = inspect.signature(aml_End.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "value" in params, "Missing parameter 'value'"

def test_aml_end_has_scheme():
    assert hasattr(aml_End, "scheme")
    descriptor = None
    for klass in aml_End.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)

def test_aml_end_has_value():
    assert hasattr(aml_End, "value")
    descriptor = None
    for klass in aml_End.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aml_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(aml_EStringToStringMapEntry)


def test_aml_estringtostringmapentry_constructor_exists():
    assert callable(aml_EStringToStringMapEntry.__init__)


def test_aml_estringtostringmapentry_constructor_args():
    sig = inspect.signature(aml_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_aml_documentroot_is_not_abstract():
    assert not inspect.isabstract(aml_DocumentRoot)


def test_aml_documentroot_constructor_exists():
    assert callable(aml_DocumentRoot.__init__)


def test_aml_documentroot_constructor_args():
    sig = inspect.signature(aml_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "rationale" in params, "Missing parameter 'rationale'"
    assert "securityMarking" in params, "Missing parameter 'securityMarking'"
    assert "nickName" in params, "Missing parameter 'nickName'"
    assert "label" in params, "Missing parameter 'label'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "email" in params, "Missing parameter 'email'"
    assert "department" in params, "Missing parameter 'department'"
    assert "body" in params, "Missing parameter 'body'"
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "event" in params, "Missing parameter 'event'"
    assert "label1" in params, "Missing parameter 'label1'"
    assert "description1" in params, "Missing parameter 'description1'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "title" in params, "Missing parameter 'title'"
    assert "perspective" in params, "Missing parameter 'perspective'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "url" in params, "Missing parameter 'url'"
    assert "region" in params, "Missing parameter 'region'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "description" in params, "Missing parameter 'description'"
    assert "date" in params, "Missing parameter 'date'"
    assert "actor" in params, "Missing parameter 'actor'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "id" in params, "Missing parameter 'id'"

def test_aml_documentroot_has_rationale():
    assert hasattr(aml_DocumentRoot, "rationale")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_securityMarking():
    assert hasattr(aml_DocumentRoot, "securityMarking")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "securityMarking" in klass.__dict__:
            descriptor = klass.__dict__["securityMarking"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_nickName():
    assert hasattr(aml_DocumentRoot, "nickName")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "nickName" in klass.__dict__:
            descriptor = klass.__dict__["nickName"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_label():
    assert hasattr(aml_DocumentRoot, "label")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_mixed():
    assert hasattr(aml_DocumentRoot, "mixed")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_email():
    assert hasattr(aml_DocumentRoot, "email")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_department():
    assert hasattr(aml_DocumentRoot, "department")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_body():
    assert hasattr(aml_DocumentRoot, "body")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_idRef():
    assert hasattr(aml_DocumentRoot, "idRef")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_event():
    assert hasattr(aml_DocumentRoot, "event")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_label1():
    assert hasattr(aml_DocumentRoot, "label1")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "label1" in klass.__dict__:
            descriptor = klass.__dict__["label1"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_description1():
    assert hasattr(aml_DocumentRoot, "description1")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_firstName():
    assert hasattr(aml_DocumentRoot, "firstName")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_lastName():
    assert hasattr(aml_DocumentRoot, "lastName")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_title():
    assert hasattr(aml_DocumentRoot, "title")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_perspective():
    assert hasattr(aml_DocumentRoot, "perspective")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "perspective" in klass.__dict__:
            descriptor = klass.__dict__["perspective"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_organization():
    assert hasattr(aml_DocumentRoot, "organization")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_url():
    assert hasattr(aml_DocumentRoot, "url")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_region():
    assert hasattr(aml_DocumentRoot, "region")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_subject():
    assert hasattr(aml_DocumentRoot, "subject")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_description():
    assert hasattr(aml_DocumentRoot, "description")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_date():
    assert hasattr(aml_DocumentRoot, "date")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_actor():
    assert hasattr(aml_DocumentRoot, "actor")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "actor" in klass.__dict__:
            descriptor = klass.__dict__["actor"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_symbol():
    assert hasattr(aml_DocumentRoot, "symbol")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_middleName():
    assert hasattr(aml_DocumentRoot, "middleName")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_aml_documentroot_has_id():
    assert hasattr(aml_DocumentRoot, "id")
    descriptor = None
    for klass in aml_DocumentRoot.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml_dependent_is_not_abstract():
    assert not inspect.isabstract(aml_Dependent)


def test_aml_dependent_constructor_exists():
    assert callable(aml_Dependent.__init__)


def test_aml_dependent_constructor_args():
    sig = inspect.signature(aml_Dependent.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml_dependent_has_ordinal():
    assert hasattr(aml_Dependent, "ordinal")
    descriptor = None
    for klass in aml_Dependent.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml_dependent_has_idRef():
    assert hasattr(aml_Dependent, "idRef")
    descriptor = None
    for klass in aml_Dependent.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml_nationstate_is_not_abstract():
    assert not inspect.isabstract(aml_NationState)


def test_aml_nationstate_constructor_exists():
    assert callable(aml_NationState.__init__)


def test_aml_nationstate_constructor_args():
    sig = inspect.signature(aml_NationState.__init__)
    params = list(sig.parameters.keys())
    assert "actor" in params, "Missing parameter 'actor'"
    assert "perspective" in params, "Missing parameter 'perspective'"
    assert "region" in params, "Missing parameter 'region'"
    assert "group" in params, "Missing parameter 'group'"
    assert "event" in params, "Missing parameter 'event'"

def test_aml_nationstate_has_actor():
    assert hasattr(aml_NationState, "actor")
    descriptor = None
    for klass in aml_NationState.__mro__:
        if "actor" in klass.__dict__:
            descriptor = klass.__dict__["actor"]
            break
    assert isinstance(descriptor, property)

def test_aml_nationstate_has_perspective():
    assert hasattr(aml_NationState, "perspective")
    descriptor = None
    for klass in aml_NationState.__mro__:
        if "perspective" in klass.__dict__:
            descriptor = klass.__dict__["perspective"]
            break
    assert isinstance(descriptor, property)

def test_aml_nationstate_has_region():
    assert hasattr(aml_NationState, "region")
    descriptor = None
    for klass in aml_NationState.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_aml_nationstate_has_group():
    assert hasattr(aml_NationState, "group")
    descriptor = None
    for klass in aml_NationState.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_nationstate_has_event():
    assert hasattr(aml_NationState, "event")
    descriptor = None
    for klass in aml_NationState.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_aml_coverage_is_not_abstract():
    assert not inspect.isabstract(aml_Coverage)


def test_aml_coverage_constructor_exists():
    assert callable(aml_Coverage.__init__)


def test_aml_coverage_constructor_args():
    sig = inspect.signature(aml_Coverage.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_aml_coverage_has_mixed():
    assert hasattr(aml_Coverage, "mixed")
    descriptor = None
    for klass in aml_Coverage.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml_coverage_has_group():
    assert hasattr(aml_Coverage, "group")
    descriptor = None
    for klass in aml_Coverage.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml_creator_is_not_abstract():
    assert not inspect.isabstract(aml_Creator)


def test_aml_creator_constructor_exists():
    assert callable(aml_Creator.__init__)


def test_aml_creator_constructor_args():
    sig = inspect.signature(aml_Creator.__init__)
    params = list(sig.parameters.keys())
    assert "idRef" in params, "Missing parameter 'idRef'"
    assert "description" in params, "Missing parameter 'description'"
    assert "objectType" in params, "Missing parameter 'objectType'"

def test_aml_creator_has_idRef():
    assert hasattr(aml_Creator, "idRef")
    descriptor = None
    for klass in aml_Creator.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)

def test_aml_creator_has_description():
    assert hasattr(aml_Creator, "description")
    descriptor = None
    for klass in aml_Creator.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_creator_has_objectType():
    assert hasattr(aml_Creator, "objectType")
    descriptor = None
    for klass in aml_Creator.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)



def test_aml_question_is_not_abstract():
    assert not inspect.isabstract(aml_Question)


def test_aml_question_constructor_exists():
    assert callable(aml_Question.__init__)


def test_aml_question_constructor_args():
    sig = inspect.signature(aml_Question.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "amplification" in params, "Missing parameter 'amplification'"
    assert "group" in params, "Missing parameter 'group'"
    assert "label" in params, "Missing parameter 'label'"
    assert "id" in params, "Missing parameter 'id'"

def test_aml_question_has_description():
    assert hasattr(aml_Question, "description")
    descriptor = None
    for klass in aml_Question.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_question_has_amplification():
    assert hasattr(aml_Question, "amplification")
    descriptor = None
    for klass in aml_Question.__mro__:
        if "amplification" in klass.__dict__:
            descriptor = klass.__dict__["amplification"]
            break
    assert isinstance(descriptor, property)

def test_aml_question_has_group():
    assert hasattr(aml_Question, "group")
    descriptor = None
    for klass in aml_Question.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_question_has_label():
    assert hasattr(aml_Question, "label")
    descriptor = None
    for klass in aml_Question.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_question_has_id():
    assert hasattr(aml_Question, "id")
    descriptor = None
    for klass in aml_Question.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml_collectionitem_is_not_abstract():
    assert not inspect.isabstract(aml_CollectionItem)


def test_aml_collectionitem_constructor_exists():
    assert callable(aml_CollectionItem.__init__)


def test_aml_collectionitem_constructor_args():
    sig = inspect.signature(aml_CollectionItem.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "objectType" in params, "Missing parameter 'objectType'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml_collectionitem_has_ordinal():
    assert hasattr(aml_CollectionItem, "ordinal")
    descriptor = None
    for klass in aml_CollectionItem.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml_collectionitem_has_objectType():
    assert hasattr(aml_CollectionItem, "objectType")
    descriptor = None
    for klass in aml_CollectionItem.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)

def test_aml_collectionitem_has_idRef():
    assert hasattr(aml_CollectionItem, "idRef")
    descriptor = None
    for klass in aml_CollectionItem.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml_choice_is_not_abstract():
    assert not inspect.isabstract(aml_Choice)


def test_aml_choice_constructor_exists():
    assert callable(aml_Choice.__init__)


def test_aml_choice_constructor_args():
    sig = inspect.signature(aml_Choice.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_aml_choice_has_label():
    assert hasattr(aml_Choice, "label")
    descriptor = None
    for klass in aml_Choice.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_choice_has_description():
    assert hasattr(aml_Choice, "description")
    descriptor = None
    for klass in aml_Choice.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_choice_has_symbol():
    assert hasattr(aml_Choice, "symbol")
    descriptor = None
    for klass in aml_Choice.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml_choice_has_ordinal():
    assert hasattr(aml_Choice, "ordinal")
    descriptor = None
    for klass in aml_Choice.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_aml_argumenttemplate_is_not_abstract():
    assert not inspect.isabstract(aml_ArgumentTemplate)


def test_aml_argumenttemplate_constructor_exists():
    assert callable(aml_ArgumentTemplate.__init__)


def test_aml_argumenttemplate_constructor_args():
    sig = inspect.signature(aml_ArgumentTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml_argumenttemplate_has_value():
    assert hasattr(aml_ArgumentTemplate, "value")
    descriptor = None
    for klass in aml_ArgumentTemplate.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aml_argumenttemplate_has_idRef():
    assert hasattr(aml_ArgumentTemplate, "idRef")
    descriptor = None
    for klass in aml_ArgumentTemplate.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml_evidence_is_not_abstract():
    assert not inspect.isabstract(aml_Evidence)


def test_aml_evidence_constructor_exists():
    assert callable(aml_Evidence.__init__)


def test_aml_evidence_constructor_args():
    sig = inspect.signature(aml_Evidence.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "id" in params, "Missing parameter 'id'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_aml_evidence_has_label():
    assert hasattr(aml_Evidence, "label")
    descriptor = None
    for klass in aml_Evidence.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_evidence_has_id():
    assert hasattr(aml_Evidence, "id")
    descriptor = None
    for klass in aml_Evidence.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml_evidence_has_ordinal():
    assert hasattr(aml_Evidence, "ordinal")
    descriptor = None
    for klass in aml_Evidence.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_aml_creatingtool_is_not_abstract():
    assert not inspect.isabstract(aml_CreatingTool)


def test_aml_creatingtool_constructor_exists():
    assert callable(aml_CreatingTool.__init__)


def test_aml_creatingtool_constructor_args():
    sig = inspect.signature(aml_CreatingTool.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "label" in params, "Missing parameter 'label'"
    assert "toolType" in params, "Missing parameter 'toolType'"

def test_aml_creatingtool_has_version():
    assert hasattr(aml_CreatingTool, "version")
    descriptor = None
    for klass in aml_CreatingTool.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_aml_creatingtool_has_label():
    assert hasattr(aml_CreatingTool, "label")
    descriptor = None
    for klass in aml_CreatingTool.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_creatingtool_has_toolType():
    assert hasattr(aml_CreatingTool, "toolType")
    descriptor = None
    for klass in aml_CreatingTool.__mro__:
        if "toolType" in klass.__dict__:
            descriptor = klass.__dict__["toolType"]
            break
    assert isinstance(descriptor, property)



def test_aml_metadata_is_not_abstract():
    assert not inspect.isabstract(aml_MetaData)


def test_aml_metadata_constructor_exists():
    assert callable(aml_MetaData.__init__)


def test_aml_metadata_constructor_args():
    sig = inspect.signature(aml_MetaData.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "date" in params, "Missing parameter 'date'"
    assert "description" in params, "Missing parameter 'description'"
    assert "group" in params, "Missing parameter 'group'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "securityMarking" in params, "Missing parameter 'securityMarking'"

def test_aml_metadata_has_title():
    assert hasattr(aml_MetaData, "title")
    descriptor = None
    for klass in aml_MetaData.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_aml_metadata_has_date():
    assert hasattr(aml_MetaData, "date")
    descriptor = None
    for klass in aml_MetaData.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_aml_metadata_has_description():
    assert hasattr(aml_MetaData, "description")
    descriptor = None
    for klass in aml_MetaData.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_metadata_has_group():
    assert hasattr(aml_MetaData, "group")
    descriptor = None
    for klass in aml_MetaData.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_metadata_has_subject():
    assert hasattr(aml_MetaData, "subject")
    descriptor = None
    for klass in aml_MetaData.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_aml_metadata_has_securityMarking():
    assert hasattr(aml_MetaData, "securityMarking")
    descriptor = None
    for klass in aml_MetaData.__mro__:
        if "securityMarking" in klass.__dict__:
            descriptor = klass.__dict__["securityMarking"]
            break
    assert isinstance(descriptor, property)



def test_aml_answer_is_not_abstract():
    assert not inspect.isabstract(aml_Answer)


def test_aml_answer_constructor_exists():
    assert callable(aml_Answer.__init__)


def test_aml_answer_constructor_args():
    sig = inspect.signature(aml_Answer.__init__)
    params = list(sig.parameters.keys())
    assert "rationale" in params, "Missing parameter 'rationale'"
    assert "group" in params, "Missing parameter 'group'"
    assert "questionId" in params, "Missing parameter 'questionId'"

def test_aml_answer_has_rationale():
    assert hasattr(aml_Answer, "rationale")
    descriptor = None
    for klass in aml_Answer.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)

def test_aml_answer_has_group():
    assert hasattr(aml_Answer, "group")
    descriptor = None
    for klass in aml_Answer.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_answer_has_questionId():
    assert hasattr(aml_Answer, "questionId")
    descriptor = None
    for klass in aml_Answer.__mro__:
        if "questionId" in klass.__dict__:
            descriptor = klass.__dict__["questionId"]
            break
    assert isinstance(descriptor, property)



def test_aml_flag_is_not_abstract():
    assert not inspect.isabstract(aml_Flag)


def test_aml_flag_constructor_exists():
    assert callable(aml_Flag.__init__)


def test_aml_flag_constructor_args():
    sig = inspect.signature(aml_Flag.__init__)
    params = list(sig.parameters.keys())
    assert "flagType" in params, "Missing parameter 'flagType'"
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"

def test_aml_flag_has_flagType():
    assert hasattr(aml_Flag, "flagType")
    descriptor = None
    for klass in aml_Flag.__mro__:
        if "flagType" in klass.__dict__:
            descriptor = klass.__dict__["flagType"]
            break
    assert isinstance(descriptor, property)

def test_aml_flag_has_label():
    assert hasattr(aml_Flag, "label")
    descriptor = None
    for klass in aml_Flag.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_flag_has_description():
    assert hasattr(aml_Flag, "description")
    descriptor = None
    for klass in aml_Flag.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aml_witness_is_not_abstract():
    assert not inspect.isabstract(aml_Witness)


def test_aml_witness_constructor_exists():
    assert callable(aml_Witness.__init__)


def test_aml_witness_constructor_args():
    sig = inspect.signature(aml_Witness.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "idRef" in params, "Missing parameter 'idRef'"

def test_aml_witness_has_description():
    assert hasattr(aml_Witness, "description")
    descriptor = None
    for klass in aml_Witness.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_witness_has_timestamp():
    assert hasattr(aml_Witness, "timestamp")
    descriptor = None
    for klass in aml_Witness.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_aml_witness_has_idRef():
    assert hasattr(aml_Witness, "idRef")
    descriptor = None
    for klass in aml_Witness.__mro__:
        if "idRef" in klass.__dict__:
            descriptor = klass.__dict__["idRef"]
            break
    assert isinstance(descriptor, property)



def test_aml_belief_is_not_abstract():
    assert not inspect.isabstract(aml_Belief)


def test_aml_belief_constructor_exists():
    assert callable(aml_Belief.__init__)


def test_aml_belief_constructor_args():
    sig = inspect.signature(aml_Belief.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"

def test_aml_belief_has_ordinal():
    assert hasattr(aml_Belief, "ordinal")
    descriptor = None
    for klass in aml_Belief.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_aml_belief_has_symbol():
    assert hasattr(aml_Belief, "symbol")
    descriptor = None
    for klass in aml_Belief.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_aml_belief_has_label():
    assert hasattr(aml_Belief, "label")
    descriptor = None
    for klass in aml_Belief.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_belief_has_description():
    assert hasattr(aml_Belief, "description")
    descriptor = None
    for klass in aml_Belief.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aml_memo_is_not_abstract():
    assert not inspect.isabstract(aml_Memo)


def test_aml_memo_constructor_exists():
    assert callable(aml_Memo.__init__)


def test_aml_memo_constructor_args():
    sig = inspect.signature(aml_Memo.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "body" in params, "Missing parameter 'body'"

def test_aml_memo_has_type():
    assert hasattr(aml_Memo, "type")
    descriptor = None
    for klass in aml_Memo.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_aml_memo_has_id():
    assert hasattr(aml_Memo, "id")
    descriptor = None
    for klass in aml_Memo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml_memo_has_subject():
    assert hasattr(aml_Memo, "subject")
    descriptor = None
    for klass in aml_Memo.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_aml_memo_has_body():
    assert hasattr(aml_Memo, "body")
    descriptor = None
    for klass in aml_Memo.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_aml_person_is_not_abstract():
    assert not inspect.isabstract(aml_Person)


def test_aml_person_constructor_exists():
    assert callable(aml_Person.__init__)


def test_aml_person_constructor_args():
    sig = inspect.signature(aml_Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "nickName" in params, "Missing parameter 'nickName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "department" in params, "Missing parameter 'department'"
    assert "description" in params, "Missing parameter 'description'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_aml_person_has_email():
    assert hasattr(aml_Person, "email")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_organization():
    assert hasattr(aml_Person, "organization")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_middleName():
    assert hasattr(aml_Person, "middleName")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_nickName():
    assert hasattr(aml_Person, "nickName")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "nickName" in klass.__dict__:
            descriptor = klass.__dict__["nickName"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_firstName():
    assert hasattr(aml_Person, "firstName")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_id():
    assert hasattr(aml_Person, "id")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_department():
    assert hasattr(aml_Person, "department")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_description():
    assert hasattr(aml_Person, "description")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_person_has_lastName():
    assert hasattr(aml_Person, "lastName")
    descriptor = None
    for klass in aml_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_aml_collection_is_not_abstract():
    assert not inspect.isabstract(aml_Collection)


def test_aml_collection_constructor_exists():
    assert callable(aml_Collection.__init__)


def test_aml_collection_constructor_args():
    sig = inspect.signature(aml_Collection.__init__)
    params = list(sig.parameters.keys())
    assert "objectType" in params, "Missing parameter 'objectType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "label" in params, "Missing parameter 'label'"
    assert "group" in params, "Missing parameter 'group'"
    assert "label1" in params, "Missing parameter 'label1'"

def test_aml_collection_has_objectType():
    assert hasattr(aml_Collection, "objectType")
    descriptor = None
    for klass in aml_Collection.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)

def test_aml_collection_has_id():
    assert hasattr(aml_Collection, "id")
    descriptor = None
    for klass in aml_Collection.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml_collection_has_label():
    assert hasattr(aml_Collection, "label")
    descriptor = None
    for klass in aml_Collection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_collection_has_group():
    assert hasattr(aml_Collection, "group")
    descriptor = None
    for klass in aml_Collection.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_collection_has_label1():
    assert hasattr(aml_Collection, "label1")
    descriptor = None
    for klass in aml_Collection.__mro__:
        if "label1" in klass.__dict__:
            descriptor = klass.__dict__["label1"]
            break
    assert isinstance(descriptor, property)



def test_aml_annotation_is_not_abstract():
    assert not inspect.isabstract(aml_Annotation)


def test_aml_annotation_constructor_exists():
    assert callable(aml_Annotation.__init__)


def test_aml_annotation_constructor_args():
    sig = inspect.signature(aml_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_aml_annotation_has_id():
    assert hasattr(aml_Annotation, "id")
    descriptor = None
    for klass in aml_Annotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml_annotation_has_mixed():
    assert hasattr(aml_Annotation, "mixed")
    descriptor = None
    for klass in aml_Annotation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_aml_annotation_has_group():
    assert hasattr(aml_Annotation, "group")
    descriptor = None
    for klass in aml_Annotation.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_aml_discoverymethod_is_not_abstract():
    assert not inspect.isabstract(aml_DiscoveryMethod)


def test_aml_discoverymethod_constructor_exists():
    assert callable(aml_DiscoveryMethod.__init__)


def test_aml_discoverymethod_constructor_args():
    sig = inspect.signature(aml_DiscoveryMethod.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "importType" in params, "Missing parameter 'importType'"
    assert "description" in params, "Missing parameter 'description'"
    assert "autoTrigger" in params, "Missing parameter 'autoTrigger'"
    assert "label" in params, "Missing parameter 'label'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_aml_discoverymethod_has_url():
    assert hasattr(aml_DiscoveryMethod, "url")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_aml_discoverymethod_has_importType():
    assert hasattr(aml_DiscoveryMethod, "importType")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "importType" in klass.__dict__:
            descriptor = klass.__dict__["importType"]
            break
    assert isinstance(descriptor, property)

def test_aml_discoverymethod_has_description():
    assert hasattr(aml_DiscoveryMethod, "description")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aml_discoverymethod_has_autoTrigger():
    assert hasattr(aml_DiscoveryMethod, "autoTrigger")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "autoTrigger" in klass.__dict__:
            descriptor = klass.__dict__["autoTrigger"]
            break
    assert isinstance(descriptor, property)

def test_aml_discoverymethod_has_label():
    assert hasattr(aml_DiscoveryMethod, "label")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_aml_discoverymethod_has_id():
    assert hasattr(aml_DiscoveryMethod, "id")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aml_discoverymethod_has_type():
    assert hasattr(aml_DiscoveryMethod, "type")
    descriptor = None
    for klass in aml_DiscoveryMethod.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_aml_amldocument_is_not_abstract():
    assert not inspect.isabstract(aml_AmlDocument)


def test_aml_amldocument_constructor_exists():
    assert callable(aml_AmlDocument.__init__)


def test_aml_amldocument_constructor_args():
    sig = inspect.signature(aml_AmlDocument.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "version" in params, "Missing parameter 'version'"

def test_aml_amldocument_has_group():
    assert hasattr(aml_AmlDocument, "group")
    descriptor = None
    for klass in aml_AmlDocument.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_aml_amldocument_has_version():
    assert hasattr(aml_AmlDocument, "version")
    descriptor = None
    for klass in aml_AmlDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_aml_parameter_is_not_abstract():
    assert not inspect.isabstract(aml_Parameter)


def test_aml_parameter_constructor_exists():
    assert callable(aml_Parameter.__init__)


def test_aml_parameter_constructor_args():
    sig = inspect.signature(aml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_aml_parameter_has_symbol():
    assert hasattr(aml_Parameter, "symbol")
    descriptor = None
    for klass in aml_Parameter.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_aml_eobject_is_not_abstract():
    assert not inspect.isabstract(aml_EObject)


def test_aml_eobject_constructor_exists():
    assert callable(aml_EObject.__init__)


def test_aml_eobject_constructor_args():
    sig = inspect.signature(aml_EObject.__init__)
    params = list(sig.parameters.keys())



def test_aml_aggregationrule_is_not_abstract():
    assert not inspect.isabstract(aml_AggregationRule)


def test_aml_aggregationrule_constructor_exists():
    assert callable(aml_AggregationRule.__init__)


def test_aml_aggregationrule_constructor_args():
    sig = inspect.signature(aml_AggregationRule.__init__)
    params = list(sig.parameters.keys())



def test_aml_exhibit_is_not_abstract():
    assert not inspect.isabstract(aml_Exhibit)


def test_aml_exhibit_constructor_exists():
    assert callable(aml_Exhibit.__init__)


def test_aml_exhibit_constructor_args():
    sig = inspect.signature(aml_Exhibit.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_aml_exhibit_has_id():
    assert hasattr(aml_Exhibit, "id")
    descriptor = None
    for klass in aml_Exhibit.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml_argument_is_not_abstract():
    assert not inspect.isabstract(aml_Argument)


def test_aml_argument_constructor_exists():
    assert callable(aml_Argument.__init__)


def test_aml_argument_constructor_args():
    sig = inspect.signature(aml_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_aml_argument_has_id():
    assert hasattr(aml_Argument, "id")
    descriptor = None
    for klass in aml_Argument.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aml_template_is_not_abstract():
    assert not inspect.isabstract(aml_Template)


def test_aml_template_constructor_exists():
    assert callable(aml_Template.__init__)


def test_aml_template_constructor_args():
    sig = inspect.signature(aml_Template.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_aml_template_has_id():
    assert hasattr(aml_Template, "id")
    descriptor = None
    for klass in aml_Template.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Url",
        "Template",
        "Urldir",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_objecttype1_exists():
    # Check that the Enumeration exists
    assert ObjectType1 is not None

def test_objecttype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType1]
    expected_literals = [
        "argument",
        "template",
        "collection",
        "discoveryMethod",
        "exhibit",
        "person",
        "memo",
        "group",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType1"

def test_objecttype2_exists():
    # Check that the Enumeration exists
    assert ObjectType2 is not None

def test_objecttype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType2]
    expected_literals = [
        "SEQUENTIAL",
        "VERSIONING",
        "group",
        "template",
        "MISC",
        "argument",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType2"

def test_objecttype_exists():
    # Check that the Enumeration exists
    assert ObjectType is not None

def test_objecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType]
    expected_literals = [
        "argument",
        "memo",
        "group",
        "discoveryMethod",
        "person",
        "exhibit",
        "template",
        "collection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType"

def test_objecttype3_exists():
    # Check that the Enumeration exists
    assert ObjectType3 is not None

def test_objecttype3_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectType3]
    expected_literals = [
        "person",
        "memo",
        "discoveryMethod",
        "template",
        "exhibit",
        "collection",
        "group",
        "argument",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectType3"


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
aml_Value_strategy = st.builds(
    aml_Value,
    type=
        safe_text,
    unit=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
aml_Start_strategy = st.builds(
    aml_Start,
    value=
        safe_text,
    scheme=
        safe_text
)
aml_Reliability_strategy = st.builds(
    aml_Reliability,
    description=
        safe_text,
    ordinal=
        safe_text,
    symbol=
        safe_text,
    label=
        safe_text
)
aml_Relevance_strategy = st.builds(
    aml_Relevance,
    label=
        safe_text,
    ordinal=
        safe_text,
    symbol=
        safe_text,
    description=
        safe_text
)
aml_Reader_strategy = st.builds(
    aml_Reader,
    description=
        safe_text,
    idRef=
        safe_text,
    objectType=
        safe_text
)
aml_QuestionRelationships_strategy = st.builds(
    aml_QuestionRelationships,
)
aml_Period_strategy = st.builds(
    aml_Period,
    group=
        safe_text,
    label=
        safe_text
)
aml_Publisher_strategy = st.builds(
    aml_Publisher,
    idRef=
        safe_text,
    description=
        safe_text,
    objectType=
        safe_text
)
aml_List_strategy = st.builds(
    aml_List,
    group=
        safe_text
)
aml_EvidenceExhibit_strategy = st.builds(
    aml_EvidenceExhibit,
    questionId=
        safe_text,
    idRef=
        safe_text,
    value=
        safe_text
)
aml_Interval_strategy = st.builds(
    aml_Interval,
    min=
        safe_text,
    max=
        safe_text
)
aml_End_strategy = st.builds(
    aml_End,
    scheme=
        safe_text,
    value=
        safe_text
)
aml_EStringToStringMapEntry_strategy = st.builds(
    aml_EStringToStringMapEntry,
)
aml_DocumentRoot_strategy = st.builds(
    aml_DocumentRoot,
    rationale=
        safe_text,
    securityMarking=
        safe_text,
    nickName=
        safe_text,
    label=
        safe_text,
    mixed=
        safe_text,
    email=
        safe_text,
    department=
        safe_text,
    body=
        safe_text,
    idRef=
        safe_text,
    event=
        safe_text,
    label1=
        safe_text,
    description1=
        safe_text,
    firstName=
        safe_text,
    lastName=
        safe_text,
    title=
        safe_text,
    perspective=
        safe_text,
    organization=
        safe_text,
    url=
        safe_text,
    region=
        safe_text,
    subject=
        safe_text,
    description=
        safe_text,
    date=
        safe_text,
    actor=
        safe_text,
    symbol=
        safe_text,
    middleName=
        safe_text,
    id=
        safe_text
)
aml_Dependent_strategy = st.builds(
    aml_Dependent,
    ordinal=
        safe_text,
    idRef=
        safe_text
)
aml_NationState_strategy = st.builds(
    aml_NationState,
    actor=
        safe_text,
    perspective=
        safe_text,
    region=
        safe_text,
    group=
        safe_text,
    event=
        safe_text
)
aml_Coverage_strategy = st.builds(
    aml_Coverage,
    mixed=
        safe_text,
    group=
        safe_text
)
aml_Creator_strategy = st.builds(
    aml_Creator,
    idRef=
        safe_text,
    description=
        safe_text,
    objectType=
        safe_text
)
aml_Question_strategy = st.builds(
    aml_Question,
    description=
        safe_text,
    amplification=
        safe_text,
    group=
        safe_text,
    label=
        safe_text,
    id=
        safe_text
)
aml_CollectionItem_strategy = st.builds(
    aml_CollectionItem,
    ordinal=
        safe_text,
    objectType=
        safe_text,
    idRef=
        safe_text
)
aml_Choice_strategy = st.builds(
    aml_Choice,
    label=
        safe_text,
    description=
        safe_text,
    symbol=
        safe_text,
    ordinal=
        safe_text
)
aml_ArgumentTemplate_strategy = st.builds(
    aml_ArgumentTemplate,
    value=
        safe_text,
    idRef=
        safe_text
)
aml_Evidence_strategy = st.builds(
    aml_Evidence,
    label=
        safe_text,
    id=
        safe_text,
    ordinal=
        safe_text
)
aml_CreatingTool_strategy = st.builds(
    aml_CreatingTool,
    version=
        safe_text,
    label=
        safe_text,
    toolType=
        safe_text
)
aml_MetaData_strategy = st.builds(
    aml_MetaData,
    title=
        safe_text,
    date=
        safe_text,
    description=
        safe_text,
    group=
        safe_text,
    subject=
        safe_text,
    securityMarking=
        safe_text
)
aml_Answer_strategy = st.builds(
    aml_Answer,
    rationale=
        safe_text,
    group=
        safe_text,
    questionId=
        safe_text
)
aml_Flag_strategy = st.builds(
    aml_Flag,
    flagType=
        safe_text,
    label=
        safe_text,
    description=
        safe_text
)
aml_Witness_strategy = st.builds(
    aml_Witness,
    description=
        safe_text,
    timestamp=
        safe_text,
    idRef=
        safe_text
)
aml_Belief_strategy = st.builds(
    aml_Belief,
    ordinal=
        safe_text,
    symbol=
        safe_text,
    label=
        safe_text,
    description=
        safe_text
)
aml_Memo_strategy = st.builds(
    aml_Memo,
    type=
        safe_text,
    id=
        safe_text,
    subject=
        safe_text,
    body=
        safe_text
)
aml_Person_strategy = st.builds(
    aml_Person,
    email=
        safe_text,
    organization=
        safe_text,
    middleName=
        safe_text,
    nickName=
        safe_text,
    firstName=
        safe_text,
    id=
        safe_text,
    department=
        safe_text,
    description=
        safe_text,
    lastName=
        safe_text
)
aml_Collection_strategy = st.builds(
    aml_Collection,
    objectType=
        safe_text,
    id=
        safe_text,
    label=
        safe_text,
    group=
        safe_text,
    label1=
        safe_text
)
aml_Annotation_strategy = st.builds(
    aml_Annotation,
    id=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
aml_DiscoveryMethod_strategy = st.builds(
    aml_DiscoveryMethod,
    url=
        safe_text,
    importType=
        safe_text,
    description=
        safe_text,
    autoTrigger=
        safe_text,
    label=
        safe_text,
    id=
        safe_text,
    type=
        safe_text
)
aml_AmlDocument_strategy = st.builds(
    aml_AmlDocument,
    group=
        safe_text,
    version=
        safe_text
)
aml_Parameter_strategy = st.builds(
    aml_Parameter,
    symbol=
        safe_text
)
aml_EObject_strategy = st.builds(
    aml_EObject,
)
aml_AggregationRule_strategy = st.builds(
    aml_AggregationRule,
)
aml_Exhibit_strategy = st.builds(
    aml_Exhibit,
    id=
        safe_text
)
aml_Argument_strategy = st.builds(
    aml_Argument,
    id=
        safe_text
)
aml_Template_strategy = st.builds(
    aml_Template,
    id=
        safe_text
)

@given(instance=aml_Value_strategy)
@settings(max_examples=50)
def test_aml_value_instantiation(instance):
    assert isinstance(instance, aml_Value)



@given(instance=aml_Value_strategy)
def test_aml_value_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aml_Value_strategy)
def test_aml_value_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=aml_Value_strategy)
def test_aml_value_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=aml_Value_strategy)
def test_aml_value_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml_Start_strategy)
@settings(max_examples=50)
def test_aml_start_instantiation(instance):
    assert isinstance(instance, aml_Start)



@given(instance=aml_Start_strategy)
def test_aml_start_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_Start_strategy)
def test_aml_start_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=aml_Reliability_strategy)
@settings(max_examples=50)
def test_aml_reliability_instantiation(instance):
    assert isinstance(instance, aml_Reliability)



@given(instance=aml_Reliability_strategy)
def test_aml_reliability_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Reliability_strategy)
def test_aml_reliability_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=aml_Reliability_strategy)
def test_aml_reliability_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=aml_Reliability_strategy)
def test_aml_reliability_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml_Relevance_strategy)
@settings(max_examples=50)
def test_aml_relevance_instantiation(instance):
    assert isinstance(instance, aml_Relevance)



@given(instance=aml_Relevance_strategy)
def test_aml_relevance_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Relevance_strategy)
def test_aml_relevance_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=aml_Relevance_strategy)
def test_aml_relevance_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=aml_Relevance_strategy)
def test_aml_relevance_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml_Reader_strategy)
@settings(max_examples=50)
def test_aml_reader_instantiation(instance):
    assert isinstance(instance, aml_Reader)



@given(instance=aml_Reader_strategy)
def test_aml_reader_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Reader_strategy)
def test_aml_reader_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original



@given(instance=aml_Reader_strategy)
def test_aml_reader_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml_QuestionRelationships_strategy)
@settings(max_examples=50)
def test_aml_questionrelationships_instantiation(instance):
    assert isinstance(instance, aml_QuestionRelationships)

@given(instance=aml_Period_strategy)
@settings(max_examples=50)
def test_aml_period_instantiation(instance):
    assert isinstance(instance, aml_Period)



@given(instance=aml_Period_strategy)
def test_aml_period_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_Period_strategy)
def test_aml_period_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=aml_Publisher_strategy)
@settings(max_examples=50)
def test_aml_publisher_instantiation(instance):
    assert isinstance(instance, aml_Publisher)



@given(instance=aml_Publisher_strategy)
def test_aml_publisher_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original



@given(instance=aml_Publisher_strategy)
def test_aml_publisher_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Publisher_strategy)
def test_aml_publisher_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml_List_strategy)
@settings(max_examples=50)
def test_aml_list_instantiation(instance):
    assert isinstance(instance, aml_List)



@given(instance=aml_List_strategy)
def test_aml_list_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml_EvidenceExhibit_strategy)
@settings(max_examples=50)
def test_aml_evidenceexhibit_instantiation(instance):
    assert isinstance(instance, aml_EvidenceExhibit)



@given(instance=aml_EvidenceExhibit_strategy)
def test_aml_evidenceexhibit_questionId_setter(instance):
    original = instance.questionId
    instance.questionId = original
    assert instance.questionId == original



@given(instance=aml_EvidenceExhibit_strategy)
def test_aml_evidenceexhibit_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original



@given(instance=aml_EvidenceExhibit_strategy)
def test_aml_evidenceexhibit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aml_Interval_strategy)
@settings(max_examples=50)
def test_aml_interval_instantiation(instance):
    assert isinstance(instance, aml_Interval)



@given(instance=aml_Interval_strategy)
def test_aml_interval_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=aml_Interval_strategy)
def test_aml_interval_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=aml_End_strategy)
@settings(max_examples=50)
def test_aml_end_instantiation(instance):
    assert isinstance(instance, aml_End)



@given(instance=aml_End_strategy)
def test_aml_end_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original



@given(instance=aml_End_strategy)
def test_aml_end_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aml_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_aml_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, aml_EStringToStringMapEntry)

@given(instance=aml_DocumentRoot_strategy)
@settings(max_examples=50)
def test_aml_documentroot_instantiation(instance):
    assert isinstance(instance, aml_DocumentRoot)



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_securityMarking_setter(instance):
    original = instance.securityMarking
    instance.securityMarking = original
    assert instance.securityMarking == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_nickName_setter(instance):
    original = instance.nickName
    instance.nickName = original
    assert instance.nickName == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_label1_setter(instance):
    original = instance.label1
    instance.label1 = original
    assert instance.label1 == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_perspective_setter(instance):
    original = instance.perspective
    instance.perspective = original
    assert instance.perspective == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_actor_setter(instance):
    original = instance.actor
    instance.actor = original
    assert instance.actor == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=aml_DocumentRoot_strategy)
def test_aml_documentroot_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml_Dependent_strategy)
@settings(max_examples=50)
def test_aml_dependent_instantiation(instance):
    assert isinstance(instance, aml_Dependent)



@given(instance=aml_Dependent_strategy)
def test_aml_dependent_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=aml_Dependent_strategy)
def test_aml_dependent_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml_NationState_strategy)
@settings(max_examples=50)
def test_aml_nationstate_instantiation(instance):
    assert isinstance(instance, aml_NationState)



@given(instance=aml_NationState_strategy)
def test_aml_nationstate_actor_setter(instance):
    original = instance.actor
    instance.actor = original
    assert instance.actor == original



@given(instance=aml_NationState_strategy)
def test_aml_nationstate_perspective_setter(instance):
    original = instance.perspective
    instance.perspective = original
    assert instance.perspective == original



@given(instance=aml_NationState_strategy)
def test_aml_nationstate_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original



@given(instance=aml_NationState_strategy)
def test_aml_nationstate_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_NationState_strategy)
def test_aml_nationstate_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=aml_Coverage_strategy)
@settings(max_examples=50)
def test_aml_coverage_instantiation(instance):
    assert isinstance(instance, aml_Coverage)



@given(instance=aml_Coverage_strategy)
def test_aml_coverage_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=aml_Coverage_strategy)
def test_aml_coverage_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml_Creator_strategy)
@settings(max_examples=50)
def test_aml_creator_instantiation(instance):
    assert isinstance(instance, aml_Creator)



@given(instance=aml_Creator_strategy)
def test_aml_creator_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original



@given(instance=aml_Creator_strategy)
def test_aml_creator_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Creator_strategy)
def test_aml_creator_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=aml_Question_strategy)
@settings(max_examples=50)
def test_aml_question_instantiation(instance):
    assert isinstance(instance, aml_Question)



@given(instance=aml_Question_strategy)
def test_aml_question_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Question_strategy)
def test_aml_question_amplification_setter(instance):
    original = instance.amplification
    instance.amplification = original
    assert instance.amplification == original



@given(instance=aml_Question_strategy)
def test_aml_question_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_Question_strategy)
def test_aml_question_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Question_strategy)
def test_aml_question_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml_CollectionItem_strategy)
@settings(max_examples=50)
def test_aml_collectionitem_instantiation(instance):
    assert isinstance(instance, aml_CollectionItem)



@given(instance=aml_CollectionItem_strategy)
def test_aml_collectionitem_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=aml_CollectionItem_strategy)
def test_aml_collectionitem_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original



@given(instance=aml_CollectionItem_strategy)
def test_aml_collectionitem_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml_Choice_strategy)
@settings(max_examples=50)
def test_aml_choice_instantiation(instance):
    assert isinstance(instance, aml_Choice)



@given(instance=aml_Choice_strategy)
def test_aml_choice_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Choice_strategy)
def test_aml_choice_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Choice_strategy)
def test_aml_choice_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=aml_Choice_strategy)
def test_aml_choice_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml_ArgumentTemplate_strategy)
@settings(max_examples=50)
def test_aml_argumenttemplate_instantiation(instance):
    assert isinstance(instance, aml_ArgumentTemplate)



@given(instance=aml_ArgumentTemplate_strategy)
def test_aml_argumenttemplate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_ArgumentTemplate_strategy)
def test_aml_argumenttemplate_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml_Evidence_strategy)
@settings(max_examples=50)
def test_aml_evidence_instantiation(instance):
    assert isinstance(instance, aml_Evidence)



@given(instance=aml_Evidence_strategy)
def test_aml_evidence_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Evidence_strategy)
def test_aml_evidence_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aml_Evidence_strategy)
def test_aml_evidence_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=aml_CreatingTool_strategy)
@settings(max_examples=50)
def test_aml_creatingtool_instantiation(instance):
    assert isinstance(instance, aml_CreatingTool)



@given(instance=aml_CreatingTool_strategy)
def test_aml_creatingtool_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=aml_CreatingTool_strategy)
def test_aml_creatingtool_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_CreatingTool_strategy)
def test_aml_creatingtool_toolType_setter(instance):
    original = instance.toolType
    instance.toolType = original
    assert instance.toolType == original

@given(instance=aml_MetaData_strategy)
@settings(max_examples=50)
def test_aml_metadata_instantiation(instance):
    assert isinstance(instance, aml_MetaData)



@given(instance=aml_MetaData_strategy)
def test_aml_metadata_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=aml_MetaData_strategy)
def test_aml_metadata_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=aml_MetaData_strategy)
def test_aml_metadata_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_MetaData_strategy)
def test_aml_metadata_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_MetaData_strategy)
def test_aml_metadata_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=aml_MetaData_strategy)
def test_aml_metadata_securityMarking_setter(instance):
    original = instance.securityMarking
    instance.securityMarking = original
    assert instance.securityMarking == original

@given(instance=aml_Answer_strategy)
@settings(max_examples=50)
def test_aml_answer_instantiation(instance):
    assert isinstance(instance, aml_Answer)



@given(instance=aml_Answer_strategy)
def test_aml_answer_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original



@given(instance=aml_Answer_strategy)
def test_aml_answer_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_Answer_strategy)
def test_aml_answer_questionId_setter(instance):
    original = instance.questionId
    instance.questionId = original
    assert instance.questionId == original

@given(instance=aml_Flag_strategy)
@settings(max_examples=50)
def test_aml_flag_instantiation(instance):
    assert isinstance(instance, aml_Flag)



@given(instance=aml_Flag_strategy)
def test_aml_flag_flagType_setter(instance):
    original = instance.flagType
    instance.flagType = original
    assert instance.flagType == original



@given(instance=aml_Flag_strategy)
def test_aml_flag_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Flag_strategy)
def test_aml_flag_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml_Witness_strategy)
@settings(max_examples=50)
def test_aml_witness_instantiation(instance):
    assert isinstance(instance, aml_Witness)



@given(instance=aml_Witness_strategy)
def test_aml_witness_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Witness_strategy)
def test_aml_witness_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=aml_Witness_strategy)
def test_aml_witness_idRef_setter(instance):
    original = instance.idRef
    instance.idRef = original
    assert instance.idRef == original

@given(instance=aml_Belief_strategy)
@settings(max_examples=50)
def test_aml_belief_instantiation(instance):
    assert isinstance(instance, aml_Belief)



@given(instance=aml_Belief_strategy)
def test_aml_belief_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=aml_Belief_strategy)
def test_aml_belief_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=aml_Belief_strategy)
def test_aml_belief_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Belief_strategy)
def test_aml_belief_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aml_Memo_strategy)
@settings(max_examples=50)
def test_aml_memo_instantiation(instance):
    assert isinstance(instance, aml_Memo)



@given(instance=aml_Memo_strategy)
def test_aml_memo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aml_Memo_strategy)
def test_aml_memo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aml_Memo_strategy)
def test_aml_memo_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=aml_Memo_strategy)
def test_aml_memo_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=aml_Person_strategy)
@settings(max_examples=50)
def test_aml_person_instantiation(instance):
    assert isinstance(instance, aml_Person)



@given(instance=aml_Person_strategy)
def test_aml_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=aml_Person_strategy)
def test_aml_person_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=aml_Person_strategy)
def test_aml_person_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=aml_Person_strategy)
def test_aml_person_nickName_setter(instance):
    original = instance.nickName
    instance.nickName = original
    assert instance.nickName == original



@given(instance=aml_Person_strategy)
def test_aml_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=aml_Person_strategy)
def test_aml_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aml_Person_strategy)
def test_aml_person_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=aml_Person_strategy)
def test_aml_person_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_Person_strategy)
def test_aml_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=aml_Collection_strategy)
@settings(max_examples=50)
def test_aml_collection_instantiation(instance):
    assert isinstance(instance, aml_Collection)



@given(instance=aml_Collection_strategy)
def test_aml_collection_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original



@given(instance=aml_Collection_strategy)
def test_aml_collection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aml_Collection_strategy)
def test_aml_collection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_Collection_strategy)
def test_aml_collection_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_Collection_strategy)
def test_aml_collection_label1_setter(instance):
    original = instance.label1
    instance.label1 = original
    assert instance.label1 == original

@given(instance=aml_Annotation_strategy)
@settings(max_examples=50)
def test_aml_annotation_instantiation(instance):
    assert isinstance(instance, aml_Annotation)



@given(instance=aml_Annotation_strategy)
def test_aml_annotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aml_Annotation_strategy)
def test_aml_annotation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=aml_Annotation_strategy)
def test_aml_annotation_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=aml_DiscoveryMethod_strategy)
@settings(max_examples=50)
def test_aml_discoverymethod_instantiation(instance):
    assert isinstance(instance, aml_DiscoveryMethod)



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_importType_setter(instance):
    original = instance.importType
    instance.importType = original
    assert instance.importType == original



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_autoTrigger_setter(instance):
    original = instance.autoTrigger
    instance.autoTrigger = original
    assert instance.autoTrigger == original



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aml_DiscoveryMethod_strategy)
def test_aml_discoverymethod_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aml_AmlDocument_strategy)
@settings(max_examples=50)
def test_aml_amldocument_instantiation(instance):
    assert isinstance(instance, aml_AmlDocument)



@given(instance=aml_AmlDocument_strategy)
def test_aml_amldocument_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=aml_AmlDocument_strategy)
def test_aml_amldocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=aml_Parameter_strategy)
@settings(max_examples=50)
def test_aml_parameter_instantiation(instance):
    assert isinstance(instance, aml_Parameter)



@given(instance=aml_Parameter_strategy)
def test_aml_parameter_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=aml_EObject_strategy)
@settings(max_examples=50)
def test_aml_eobject_instantiation(instance):
    assert isinstance(instance, aml_EObject)

@given(instance=aml_AggregationRule_strategy)
@settings(max_examples=50)
def test_aml_aggregationrule_instantiation(instance):
    assert isinstance(instance, aml_AggregationRule)

@given(instance=aml_Exhibit_strategy)
@settings(max_examples=50)
def test_aml_exhibit_instantiation(instance):
    assert isinstance(instance, aml_Exhibit)



@given(instance=aml_Exhibit_strategy)
def test_aml_exhibit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml_Argument_strategy)
@settings(max_examples=50)
def test_aml_argument_instantiation(instance):
    assert isinstance(instance, aml_Argument)



@given(instance=aml_Argument_strategy)
def test_aml_argument_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aml_Template_strategy)
@settings(max_examples=50)
def test_aml_template_instantiation(instance):
    assert isinstance(instance, aml_Template)



@given(instance=aml_Template_strategy)
def test_aml_template_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
