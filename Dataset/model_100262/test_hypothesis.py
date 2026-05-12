import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PageSummary,
    ObjectSummary,
    xwiki_LinkCollection,
    xwiki_Link,
    xwiki_Page,
    xwiki_Object,
    xwiki_EStringToStringMapEntry,
    xwiki_DocumentRoot,
    LinkCollection,
    xwiki_Syntaxes,
    xwiki_PageSummary,
    xwiki_SearchResult,
    xwiki_PagesType,
    xwiki_Translation,
    xwiki_SpacesType,
    xwiki_Attribute,
    xwiki_ObjectsType,
    xwiki_PropertiesType,
    xwiki_ClassesType,
    xwiki_Comment,
    xwiki_AttachmentsType,
    xwiki_XWiki,
    xwiki_CommentsType,
    xwiki_HistorySummary,
    xwiki_Class,
    xwiki_Property,
    xwiki_Wiki,
    xwiki_WikisType,
    xwiki_Translations,
    xwiki_HistoryType,
    xwiki_ObjectSummary,
    xwiki_SearchResultsType,
    xwiki_TagsType,
    xwiki_Tag,
    xwiki_Space,
    xwiki_Attachment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pagesummary_is_not_abstract():
    assert not inspect.isabstract(PageSummary)


def test_pagesummary_constructor_exists():
    assert callable(PageSummary.__init__)


def test_pagesummary_constructor_args():
    sig = inspect.signature(PageSummary.__init__)
    params = list(sig.parameters.keys())



def test_objectsummary_is_not_abstract():
    assert not inspect.isabstract(ObjectSummary)


def test_objectsummary_constructor_exists():
    assert callable(ObjectSummary.__init__)


def test_objectsummary_constructor_args():
    sig = inspect.signature(ObjectSummary.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_linkcollection_is_not_abstract():
    assert not inspect.isabstract(xwiki_LinkCollection)


def test_xwiki_linkcollection_constructor_exists():
    assert callable(xwiki_LinkCollection.__init__)


def test_xwiki_linkcollection_constructor_args():
    sig = inspect.signature(xwiki_LinkCollection.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_link_is_not_abstract():
    assert not inspect.isabstract(xwiki_Link)


def test_xwiki_link_constructor_exists():
    assert callable(xwiki_Link.__init__)


def test_xwiki_link_constructor_args():
    sig = inspect.signature(xwiki_Link.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"
    assert "hrefLang" in params, "Missing parameter 'hrefLang'"
    assert "type" in params, "Missing parameter 'type'"
    assert "rel" in params, "Missing parameter 'rel'"

def test_xwiki_link_has_href():
    assert hasattr(xwiki_Link, "href")
    descriptor = None
    for klass in xwiki_Link.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_link_has_hrefLang():
    assert hasattr(xwiki_Link, "hrefLang")
    descriptor = None
    for klass in xwiki_Link.__mro__:
        if "hrefLang" in klass.__dict__:
            descriptor = klass.__dict__["hrefLang"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_link_has_type():
    assert hasattr(xwiki_Link, "type")
    descriptor = None
    for klass in xwiki_Link.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_link_has_rel():
    assert hasattr(xwiki_Link, "rel")
    descriptor = None
    for klass in xwiki_Link.__mro__:
        if "rel" in klass.__dict__:
            descriptor = klass.__dict__["rel"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_page_is_not_abstract():
    assert not inspect.isabstract(xwiki_Page)


def test_xwiki_page_constructor_exists():
    assert callable(xwiki_Page.__init__)


def test_xwiki_page_constructor_args():
    sig = inspect.signature(xwiki_Page.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "content" in params, "Missing parameter 'content'"
    assert "majorVersion" in params, "Missing parameter 'majorVersion'"
    assert "creatorName" in params, "Missing parameter 'creatorName'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "created" in params, "Missing parameter 'created'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "modifierName" in params, "Missing parameter 'modifierName'"
    assert "minorVersion" in params, "Missing parameter 'minorVersion'"

def test_xwiki_page_has_language():
    assert hasattr(xwiki_Page, "language")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_content():
    assert hasattr(xwiki_Page, "content")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_majorVersion():
    assert hasattr(xwiki_Page, "majorVersion")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "majorVersion" in klass.__dict__:
            descriptor = klass.__dict__["majorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_creatorName():
    assert hasattr(xwiki_Page, "creatorName")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "creatorName" in klass.__dict__:
            descriptor = klass.__dict__["creatorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_modifier():
    assert hasattr(xwiki_Page, "modifier")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_creator():
    assert hasattr(xwiki_Page, "creator")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_comment():
    assert hasattr(xwiki_Page, "comment")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_created():
    assert hasattr(xwiki_Page, "created")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_modified():
    assert hasattr(xwiki_Page, "modified")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_modifierName():
    assert hasattr(xwiki_Page, "modifierName")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "modifierName" in klass.__dict__:
            descriptor = klass.__dict__["modifierName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_page_has_minorVersion():
    assert hasattr(xwiki_Page, "minorVersion")
    descriptor = None
    for klass in xwiki_Page.__mro__:
        if "minorVersion" in klass.__dict__:
            descriptor = klass.__dict__["minorVersion"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_object_is_not_abstract():
    assert not inspect.isabstract(xwiki_Object)


def test_xwiki_object_constructor_exists():
    assert callable(xwiki_Object.__init__)


def test_xwiki_object_constructor_args():
    sig = inspect.signature(xwiki_Object.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xwiki_EStringToStringMapEntry)


def test_xwiki_estringtostringmapentry_constructor_exists():
    assert callable(xwiki_EStringToStringMapEntry.__init__)


def test_xwiki_estringtostringmapentry_constructor_args():
    sig = inspect.signature(xwiki_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_documentroot_is_not_abstract():
    assert not inspect.isabstract(xwiki_DocumentRoot)


def test_xwiki_documentroot_constructor_exists():
    assert callable(xwiki_DocumentRoot.__init__)


def test_xwiki_documentroot_constructor_args():
    sig = inspect.signature(xwiki_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xwiki_documentroot_has_mixed():
    assert hasattr(xwiki_DocumentRoot, "mixed")
    descriptor = None
    for klass in xwiki_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_linkcollection_is_not_abstract():
    assert not inspect.isabstract(LinkCollection)


def test_linkcollection_constructor_exists():
    assert callable(LinkCollection.__init__)


def test_linkcollection_constructor_args():
    sig = inspect.signature(LinkCollection.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_syntaxes_is_not_abstract():
    assert not inspect.isabstract(xwiki_Syntaxes)


def test_xwiki_syntaxes_constructor_exists():
    assert callable(xwiki_Syntaxes.__init__)


def test_xwiki_syntaxes_constructor_args():
    sig = inspect.signature(xwiki_Syntaxes.__init__)
    params = list(sig.parameters.keys())
    assert "syntax" in params, "Missing parameter 'syntax'"

def test_xwiki_syntaxes_has_syntax():
    assert hasattr(xwiki_Syntaxes, "syntax")
    descriptor = None
    for klass in xwiki_Syntaxes.__mro__:
        if "syntax" in klass.__dict__:
            descriptor = klass.__dict__["syntax"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_pagesummary_is_not_abstract():
    assert not inspect.isabstract(xwiki_PageSummary)


def test_xwiki_pagesummary_constructor_exists():
    assert callable(xwiki_PageSummary.__init__)


def test_xwiki_pagesummary_constructor_args():
    sig = inspect.signature(xwiki_PageSummary.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"
    assert "id" in params, "Missing parameter 'id'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "parent" in params, "Missing parameter 'parent'"
    assert "title" in params, "Missing parameter 'title'"
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "author" in params, "Missing parameter 'author'"
    assert "syntax" in params, "Missing parameter 'syntax'"

def test_xwiki_pagesummary_has_space():
    assert hasattr(xwiki_PageSummary, "space")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_id():
    assert hasattr(xwiki_PageSummary, "id")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_xwikiRelativeUrl():
    assert hasattr(xwiki_PageSummary, "xwikiRelativeUrl")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "xwikiRelativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiRelativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_parent():
    assert hasattr(xwiki_PageSummary, "parent")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "parent" in klass.__dict__:
            descriptor = klass.__dict__["parent"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_title():
    assert hasattr(xwiki_PageSummary, "title")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_parentId():
    assert hasattr(xwiki_PageSummary, "parentId")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_name():
    assert hasattr(xwiki_PageSummary, "name")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_authorName():
    assert hasattr(xwiki_PageSummary, "authorName")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_version():
    assert hasattr(xwiki_PageSummary, "version")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_wiki():
    assert hasattr(xwiki_PageSummary, "wiki")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_fullName():
    assert hasattr(xwiki_PageSummary, "fullName")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_xwikiAbsoluteUrl():
    assert hasattr(xwiki_PageSummary, "xwikiAbsoluteUrl")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "xwikiAbsoluteUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiAbsoluteUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_author():
    assert hasattr(xwiki_PageSummary, "author")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_pagesummary_has_syntax():
    assert hasattr(xwiki_PageSummary, "syntax")
    descriptor = None
    for klass in xwiki_PageSummary.__mro__:
        if "syntax" in klass.__dict__:
            descriptor = klass.__dict__["syntax"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_searchresult_is_not_abstract():
    assert not inspect.isabstract(xwiki_SearchResult)


def test_xwiki_searchresult_constructor_exists():
    assert callable(xwiki_SearchResult.__init__)


def test_xwiki_searchresult_constructor_args():
    sig = inspect.signature(xwiki_SearchResult.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "className" in params, "Missing parameter 'className'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "objectNumber" in params, "Missing parameter 'objectNumber'"
    assert "pageName" in params, "Missing parameter 'pageName'"
    assert "language" in params, "Missing parameter 'language'"
    assert "title" in params, "Missing parameter 'title'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "space" in params, "Missing parameter 'space'"
    assert "version" in params, "Missing parameter 'version'"
    assert "author" in params, "Missing parameter 'author'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "score" in params, "Missing parameter 'score'"
    assert "pageFullName" in params, "Missing parameter 'pageFullName'"

def test_xwiki_searchresult_has_id():
    assert hasattr(xwiki_SearchResult, "id")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_type():
    assert hasattr(xwiki_SearchResult, "type")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_className():
    assert hasattr(xwiki_SearchResult, "className")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_wiki():
    assert hasattr(xwiki_SearchResult, "wiki")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_objectNumber():
    assert hasattr(xwiki_SearchResult, "objectNumber")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "objectNumber" in klass.__dict__:
            descriptor = klass.__dict__["objectNumber"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_pageName():
    assert hasattr(xwiki_SearchResult, "pageName")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "pageName" in klass.__dict__:
            descriptor = klass.__dict__["pageName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_language():
    assert hasattr(xwiki_SearchResult, "language")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_title():
    assert hasattr(xwiki_SearchResult, "title")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_authorName():
    assert hasattr(xwiki_SearchResult, "authorName")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_space():
    assert hasattr(xwiki_SearchResult, "space")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_version():
    assert hasattr(xwiki_SearchResult, "version")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_author():
    assert hasattr(xwiki_SearchResult, "author")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_filename():
    assert hasattr(xwiki_SearchResult, "filename")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_modified():
    assert hasattr(xwiki_SearchResult, "modified")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_score():
    assert hasattr(xwiki_SearchResult, "score")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_searchresult_has_pageFullName():
    assert hasattr(xwiki_SearchResult, "pageFullName")
    descriptor = None
    for klass in xwiki_SearchResult.__mro__:
        if "pageFullName" in klass.__dict__:
            descriptor = klass.__dict__["pageFullName"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_pagestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_PagesType)


def test_xwiki_pagestype_constructor_exists():
    assert callable(xwiki_PagesType.__init__)


def test_xwiki_pagestype_constructor_args():
    sig = inspect.signature(xwiki_PagesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_translation_is_not_abstract():
    assert not inspect.isabstract(xwiki_Translation)


def test_xwiki_translation_constructor_exists():
    assert callable(xwiki_Translation.__init__)


def test_xwiki_translation_constructor_args():
    sig = inspect.signature(xwiki_Translation.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_xwiki_translation_has_language():
    assert hasattr(xwiki_Translation, "language")
    descriptor = None
    for klass in xwiki_Translation.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_spacestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_SpacesType)


def test_xwiki_spacestype_constructor_exists():
    assert callable(xwiki_SpacesType.__init__)


def test_xwiki_spacestype_constructor_args():
    sig = inspect.signature(xwiki_SpacesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_attribute_is_not_abstract():
    assert not inspect.isabstract(xwiki_Attribute)


def test_xwiki_attribute_constructor_exists():
    assert callable(xwiki_Attribute.__init__)


def test_xwiki_attribute_constructor_args():
    sig = inspect.signature(xwiki_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki_attribute_has_value():
    assert hasattr(xwiki_Attribute, "value")
    descriptor = None
    for klass in xwiki_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attribute_has_name():
    assert hasattr(xwiki_Attribute, "name")
    descriptor = None
    for klass in xwiki_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_objectstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_ObjectsType)


def test_xwiki_objectstype_constructor_exists():
    assert callable(xwiki_ObjectsType.__init__)


def test_xwiki_objectstype_constructor_args():
    sig = inspect.signature(xwiki_ObjectsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_propertiestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_PropertiesType)


def test_xwiki_propertiestype_constructor_exists():
    assert callable(xwiki_PropertiesType.__init__)


def test_xwiki_propertiestype_constructor_args():
    sig = inspect.signature(xwiki_PropertiesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_classestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_ClassesType)


def test_xwiki_classestype_constructor_exists():
    assert callable(xwiki_ClassesType.__init__)


def test_xwiki_classestype_constructor_args():
    sig = inspect.signature(xwiki_ClassesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_comment_is_not_abstract():
    assert not inspect.isabstract(xwiki_Comment)


def test_xwiki_comment_constructor_exists():
    assert callable(xwiki_Comment.__init__)


def test_xwiki_comment_constructor_args():
    sig = inspect.signature(xwiki_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"
    assert "replyTo" in params, "Missing parameter 'replyTo'"
    assert "date" in params, "Missing parameter 'date'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "author" in params, "Missing parameter 'author'"
    assert "highlight" in params, "Missing parameter 'highlight'"

def test_xwiki_comment_has_id():
    assert hasattr(xwiki_Comment, "id")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_text():
    assert hasattr(xwiki_Comment, "text")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_replyTo():
    assert hasattr(xwiki_Comment, "replyTo")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "replyTo" in klass.__dict__:
            descriptor = klass.__dict__["replyTo"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_date():
    assert hasattr(xwiki_Comment, "date")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_pageId():
    assert hasattr(xwiki_Comment, "pageId")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_authorName():
    assert hasattr(xwiki_Comment, "authorName")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_author():
    assert hasattr(xwiki_Comment, "author")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_comment_has_highlight():
    assert hasattr(xwiki_Comment, "highlight")
    descriptor = None
    for klass in xwiki_Comment.__mro__:
        if "highlight" in klass.__dict__:
            descriptor = klass.__dict__["highlight"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_attachmentstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_AttachmentsType)


def test_xwiki_attachmentstype_constructor_exists():
    assert callable(xwiki_AttachmentsType.__init__)


def test_xwiki_attachmentstype_constructor_args():
    sig = inspect.signature(xwiki_AttachmentsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_xwiki_is_not_abstract():
    assert not inspect.isabstract(xwiki_XWiki)


def test_xwiki_xwiki_constructor_exists():
    assert callable(xwiki_XWiki.__init__)


def test_xwiki_xwiki_constructor_args():
    sig = inspect.signature(xwiki_XWiki.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_xwiki_xwiki_has_version():
    assert hasattr(xwiki_XWiki, "version")
    descriptor = None
    for klass in xwiki_XWiki.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_commentstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_CommentsType)


def test_xwiki_commentstype_constructor_exists():
    assert callable(xwiki_CommentsType.__init__)


def test_xwiki_commentstype_constructor_args():
    sig = inspect.signature(xwiki_CommentsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_historysummary_is_not_abstract():
    assert not inspect.isabstract(xwiki_HistorySummary)


def test_xwiki_historysummary_constructor_exists():
    assert callable(xwiki_HistorySummary.__init__)


def test_xwiki_historysummary_constructor_args():
    sig = inspect.signature(xwiki_HistorySummary.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "modifierName" in params, "Missing parameter 'modifierName'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "minorVersion" in params, "Missing parameter 'minorVersion'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "majorVersion" in params, "Missing parameter 'majorVersion'"
    assert "space" in params, "Missing parameter 'space'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "language" in params, "Missing parameter 'language'"

def test_xwiki_historysummary_has_version():
    assert hasattr(xwiki_HistorySummary, "version")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_modifierName():
    assert hasattr(xwiki_HistorySummary, "modifierName")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "modifierName" in klass.__dict__:
            descriptor = klass.__dict__["modifierName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_comment():
    assert hasattr(xwiki_HistorySummary, "comment")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_modifier():
    assert hasattr(xwiki_HistorySummary, "modifier")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_name():
    assert hasattr(xwiki_HistorySummary, "name")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_minorVersion():
    assert hasattr(xwiki_HistorySummary, "minorVersion")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "minorVersion" in klass.__dict__:
            descriptor = klass.__dict__["minorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_pageId():
    assert hasattr(xwiki_HistorySummary, "pageId")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_modified():
    assert hasattr(xwiki_HistorySummary, "modified")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_majorVersion():
    assert hasattr(xwiki_HistorySummary, "majorVersion")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "majorVersion" in klass.__dict__:
            descriptor = klass.__dict__["majorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_space():
    assert hasattr(xwiki_HistorySummary, "space")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_wiki():
    assert hasattr(xwiki_HistorySummary, "wiki")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_historysummary_has_language():
    assert hasattr(xwiki_HistorySummary, "language")
    descriptor = None
    for klass in xwiki_HistorySummary.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_class_is_not_abstract():
    assert not inspect.isabstract(xwiki_Class)


def test_xwiki_class_constructor_exists():
    assert callable(xwiki_Class.__init__)


def test_xwiki_class_constructor_args():
    sig = inspect.signature(xwiki_Class.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki_class_has_id():
    assert hasattr(xwiki_Class, "id")
    descriptor = None
    for klass in xwiki_Class.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_class_has_name():
    assert hasattr(xwiki_Class, "name")
    descriptor = None
    for klass in xwiki_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_property_is_not_abstract():
    assert not inspect.isabstract(xwiki_Property)


def test_xwiki_property_constructor_exists():
    assert callable(xwiki_Property.__init__)


def test_xwiki_property_constructor_args():
    sig = inspect.signature(xwiki_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_xwiki_property_has_name():
    assert hasattr(xwiki_Property, "name")
    descriptor = None
    for klass in xwiki_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_property_has_type():
    assert hasattr(xwiki_Property, "type")
    descriptor = None
    for klass in xwiki_Property.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_property_has_value():
    assert hasattr(xwiki_Property, "value")
    descriptor = None
    for klass in xwiki_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_wiki_is_not_abstract():
    assert not inspect.isabstract(xwiki_Wiki)


def test_xwiki_wiki_constructor_exists():
    assert callable(xwiki_Wiki.__init__)


def test_xwiki_wiki_constructor_args():
    sig = inspect.signature(xwiki_Wiki.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_xwiki_wiki_has_owner():
    assert hasattr(xwiki_Wiki, "owner")
    descriptor = None
    for klass in xwiki_Wiki.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_wiki_has_description():
    assert hasattr(xwiki_Wiki, "description")
    descriptor = None
    for klass in xwiki_Wiki.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_wiki_has_name():
    assert hasattr(xwiki_Wiki, "name")
    descriptor = None
    for klass in xwiki_Wiki.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_wiki_has_id():
    assert hasattr(xwiki_Wiki, "id")
    descriptor = None
    for klass in xwiki_Wiki.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_wikistype_is_not_abstract():
    assert not inspect.isabstract(xwiki_WikisType)


def test_xwiki_wikistype_constructor_exists():
    assert callable(xwiki_WikisType.__init__)


def test_xwiki_wikistype_constructor_args():
    sig = inspect.signature(xwiki_WikisType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_translations_is_not_abstract():
    assert not inspect.isabstract(xwiki_Translations)


def test_xwiki_translations_constructor_exists():
    assert callable(xwiki_Translations.__init__)


def test_xwiki_translations_constructor_args():
    sig = inspect.signature(xwiki_Translations.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_xwiki_translations_has_default():
    assert hasattr(xwiki_Translations, "default")
    descriptor = None
    for klass in xwiki_Translations.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_historytype_is_not_abstract():
    assert not inspect.isabstract(xwiki_HistoryType)


def test_xwiki_historytype_constructor_exists():
    assert callable(xwiki_HistoryType.__init__)


def test_xwiki_historytype_constructor_args():
    sig = inspect.signature(xwiki_HistoryType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_objectsummary_is_not_abstract():
    assert not inspect.isabstract(xwiki_ObjectSummary)


def test_xwiki_objectsummary_constructor_exists():
    assert callable(xwiki_ObjectSummary.__init__)


def test_xwiki_objectsummary_constructor_args():
    sig = inspect.signature(xwiki_ObjectSummary.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "pageVersion" in params, "Missing parameter 'pageVersion'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "space" in params, "Missing parameter 'space'"
    assert "headline" in params, "Missing parameter 'headline'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "number" in params, "Missing parameter 'number'"
    assert "pageAuthorName" in params, "Missing parameter 'pageAuthorName'"
    assert "pageAuthor" in params, "Missing parameter 'pageAuthor'"
    assert "pageName" in params, "Missing parameter 'pageName'"
    assert "className" in params, "Missing parameter 'className'"

def test_xwiki_objectsummary_has_id():
    assert hasattr(xwiki_ObjectSummary, "id")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_guid():
    assert hasattr(xwiki_ObjectSummary, "guid")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_pageVersion():
    assert hasattr(xwiki_ObjectSummary, "pageVersion")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "pageVersion" in klass.__dict__:
            descriptor = klass.__dict__["pageVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_pageId():
    assert hasattr(xwiki_ObjectSummary, "pageId")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_space():
    assert hasattr(xwiki_ObjectSummary, "space")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_headline():
    assert hasattr(xwiki_ObjectSummary, "headline")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_wiki():
    assert hasattr(xwiki_ObjectSummary, "wiki")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_number():
    assert hasattr(xwiki_ObjectSummary, "number")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_pageAuthorName():
    assert hasattr(xwiki_ObjectSummary, "pageAuthorName")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "pageAuthorName" in klass.__dict__:
            descriptor = klass.__dict__["pageAuthorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_pageAuthor():
    assert hasattr(xwiki_ObjectSummary, "pageAuthor")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "pageAuthor" in klass.__dict__:
            descriptor = klass.__dict__["pageAuthor"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_pageName():
    assert hasattr(xwiki_ObjectSummary, "pageName")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "pageName" in klass.__dict__:
            descriptor = klass.__dict__["pageName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_objectsummary_has_className():
    assert hasattr(xwiki_ObjectSummary, "className")
    descriptor = None
    for klass in xwiki_ObjectSummary.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_searchresultstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_SearchResultsType)


def test_xwiki_searchresultstype_constructor_exists():
    assert callable(xwiki_SearchResultsType.__init__)


def test_xwiki_searchresultstype_constructor_args():
    sig = inspect.signature(xwiki_SearchResultsType.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"

def test_xwiki_searchresultstype_has_template():
    assert hasattr(xwiki_SearchResultsType, "template")
    descriptor = None
    for klass in xwiki_SearchResultsType.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_tagstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_TagsType)


def test_xwiki_tagstype_constructor_exists():
    assert callable(xwiki_TagsType.__init__)


def test_xwiki_tagstype_constructor_args():
    sig = inspect.signature(xwiki_TagsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki_tag_is_not_abstract():
    assert not inspect.isabstract(xwiki_Tag)


def test_xwiki_tag_constructor_exists():
    assert callable(xwiki_Tag.__init__)


def test_xwiki_tag_constructor_args():
    sig = inspect.signature(xwiki_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki_tag_has_name():
    assert hasattr(xwiki_Tag, "name")
    descriptor = None
    for klass in xwiki_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_space_is_not_abstract():
    assert not inspect.isabstract(xwiki_Space)


def test_xwiki_space_constructor_exists():
    assert callable(xwiki_Space.__init__)


def test_xwiki_space_constructor_args():
    sig = inspect.signature(xwiki_Space.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "home" in params, "Missing parameter 'home'"

def test_xwiki_space_has_id():
    assert hasattr(xwiki_Space, "id")
    descriptor = None
    for klass in xwiki_Space.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_space_has_name():
    assert hasattr(xwiki_Space, "name")
    descriptor = None
    for klass in xwiki_Space.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_space_has_xwikiRelativeUrl():
    assert hasattr(xwiki_Space, "xwikiRelativeUrl")
    descriptor = None
    for klass in xwiki_Space.__mro__:
        if "xwikiRelativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiRelativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_space_has_wiki():
    assert hasattr(xwiki_Space, "wiki")
    descriptor = None
    for klass in xwiki_Space.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_space_has_xwikiAbsoluteUrl():
    assert hasattr(xwiki_Space, "xwikiAbsoluteUrl")
    descriptor = None
    for klass in xwiki_Space.__mro__:
        if "xwikiAbsoluteUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiAbsoluteUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_space_has_home():
    assert hasattr(xwiki_Space, "home")
    descriptor = None
    for klass in xwiki_Space.__mro__:
        if "home" in klass.__dict__:
            descriptor = klass.__dict__["home"]
            break
    assert isinstance(descriptor, property)



def test_xwiki_attachment_is_not_abstract():
    assert not inspect.isabstract(xwiki_Attachment)


def test_xwiki_attachment_constructor_exists():
    assert callable(xwiki_Attachment.__init__)


def test_xwiki_attachment_constructor_args():
    sig = inspect.signature(xwiki_Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "pageVersion" in params, "Missing parameter 'pageVersion'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "size" in params, "Missing parameter 'size'"
    assert "author" in params, "Missing parameter 'author'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "version" in params, "Missing parameter 'version'"
    assert "date" in params, "Missing parameter 'date'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "id" in params, "Missing parameter 'id'"

def test_xwiki_attachment_has_pageVersion():
    assert hasattr(xwiki_Attachment, "pageVersion")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "pageVersion" in klass.__dict__:
            descriptor = klass.__dict__["pageVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_xwikiRelativeUrl():
    assert hasattr(xwiki_Attachment, "xwikiRelativeUrl")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "xwikiRelativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiRelativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_size():
    assert hasattr(xwiki_Attachment, "size")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_author():
    assert hasattr(xwiki_Attachment, "author")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_pageId():
    assert hasattr(xwiki_Attachment, "pageId")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_version():
    assert hasattr(xwiki_Attachment, "version")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_date():
    assert hasattr(xwiki_Attachment, "date")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_xwikiAbsoluteUrl():
    assert hasattr(xwiki_Attachment, "xwikiAbsoluteUrl")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "xwikiAbsoluteUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiAbsoluteUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_name():
    assert hasattr(xwiki_Attachment, "name")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_mimeType():
    assert hasattr(xwiki_Attachment, "mimeType")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_authorName():
    assert hasattr(xwiki_Attachment, "authorName")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki_attachment_has_id():
    assert hasattr(xwiki_Attachment, "id")
    descriptor = None
    for klass in xwiki_Attachment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)


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
PageSummary_strategy = st.builds(
    PageSummary,
)
ObjectSummary_strategy = st.builds(
    ObjectSummary,
)
xwiki_LinkCollection_strategy = st.builds(
    xwiki_LinkCollection,
)
xwiki_Link_strategy = st.builds(
    xwiki_Link,
    href=
        safe_text,
    hrefLang=
        safe_text,
    type=
        safe_text,
    rel=
        safe_text
)
xwiki_Page_strategy = st.builds(
    xwiki_Page,
    language=
        safe_text,
    content=
        safe_text,
    majorVersion=
        safe_text,
    creatorName=
        safe_text,
    modifier=
        safe_text,
    creator=
        safe_text,
    comment=
        safe_text,
    created=
        safe_text,
    modified=
        safe_text,
    modifierName=
        safe_text,
    minorVersion=
        safe_text
)
xwiki_Object_strategy = st.builds(
    xwiki_Object,
)
xwiki_EStringToStringMapEntry_strategy = st.builds(
    xwiki_EStringToStringMapEntry,
)
xwiki_DocumentRoot_strategy = st.builds(
    xwiki_DocumentRoot,
    mixed=
        safe_text
)
LinkCollection_strategy = st.builds(
    LinkCollection,
)
xwiki_Syntaxes_strategy = st.builds(
    xwiki_Syntaxes,
    syntax=
        safe_text
)
xwiki_PageSummary_strategy = st.builds(
    xwiki_PageSummary,
    space=
        safe_text,
    id=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    parent=
        safe_text,
    title=
        safe_text,
    parentId=
        safe_text,
    name=
        safe_text,
    authorName=
        safe_text,
    version=
        safe_text,
    wiki=
        safe_text,
    fullName=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    author=
        safe_text,
    syntax=
        safe_text
)
xwiki_SearchResult_strategy = st.builds(
    xwiki_SearchResult,
    id=
        safe_text,
    type=
        safe_text,
    className=
        safe_text,
    wiki=
        safe_text,
    objectNumber=
        safe_text,
    pageName=
        safe_text,
    language=
        safe_text,
    title=
        safe_text,
    authorName=
        safe_text,
    space=
        safe_text,
    version=
        safe_text,
    author=
        safe_text,
    filename=
        safe_text,
    modified=
        safe_text,
    score=
        safe_text,
    pageFullName=
        safe_text
)
xwiki_PagesType_strategy = st.builds(
    xwiki_PagesType,
)
xwiki_Translation_strategy = st.builds(
    xwiki_Translation,
    language=
        safe_text
)
xwiki_SpacesType_strategy = st.builds(
    xwiki_SpacesType,
)
xwiki_Attribute_strategy = st.builds(
    xwiki_Attribute,
    value=
        safe_text,
    name=
        safe_text
)
xwiki_ObjectsType_strategy = st.builds(
    xwiki_ObjectsType,
)
xwiki_PropertiesType_strategy = st.builds(
    xwiki_PropertiesType,
)
xwiki_ClassesType_strategy = st.builds(
    xwiki_ClassesType,
)
xwiki_Comment_strategy = st.builds(
    xwiki_Comment,
    id=
        safe_text,
    text=
        safe_text,
    replyTo=
        safe_text,
    date=
        safe_text,
    pageId=
        safe_text,
    authorName=
        safe_text,
    author=
        safe_text,
    highlight=
        safe_text
)
xwiki_AttachmentsType_strategy = st.builds(
    xwiki_AttachmentsType,
)
xwiki_XWiki_strategy = st.builds(
    xwiki_XWiki,
    version=
        safe_text
)
xwiki_CommentsType_strategy = st.builds(
    xwiki_CommentsType,
)
xwiki_HistorySummary_strategy = st.builds(
    xwiki_HistorySummary,
    version=
        safe_text,
    modifierName=
        safe_text,
    comment=
        safe_text,
    modifier=
        safe_text,
    name=
        safe_text,
    minorVersion=
        safe_text,
    pageId=
        safe_text,
    modified=
        safe_text,
    majorVersion=
        safe_text,
    space=
        safe_text,
    wiki=
        safe_text,
    language=
        safe_text
)
xwiki_Class_strategy = st.builds(
    xwiki_Class,
    id=
        safe_text,
    name=
        safe_text
)
xwiki_Property_strategy = st.builds(
    xwiki_Property,
    name=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
xwiki_Wiki_strategy = st.builds(
    xwiki_Wiki,
    owner=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
xwiki_WikisType_strategy = st.builds(
    xwiki_WikisType,
)
xwiki_Translations_strategy = st.builds(
    xwiki_Translations,
    default=
        safe_text
)
xwiki_HistoryType_strategy = st.builds(
    xwiki_HistoryType,
)
xwiki_ObjectSummary_strategy = st.builds(
    xwiki_ObjectSummary,
    id=
        safe_text,
    guid=
        safe_text,
    pageVersion=
        safe_text,
    pageId=
        safe_text,
    space=
        safe_text,
    headline=
        safe_text,
    wiki=
        safe_text,
    number=
        safe_text,
    pageAuthorName=
        safe_text,
    pageAuthor=
        safe_text,
    pageName=
        safe_text,
    className=
        safe_text
)
xwiki_SearchResultsType_strategy = st.builds(
    xwiki_SearchResultsType,
    template=
        safe_text
)
xwiki_TagsType_strategy = st.builds(
    xwiki_TagsType,
)
xwiki_Tag_strategy = st.builds(
    xwiki_Tag,
    name=
        safe_text
)
xwiki_Space_strategy = st.builds(
    xwiki_Space,
    id=
        safe_text,
    name=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    wiki=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    home=
        safe_text
)
xwiki_Attachment_strategy = st.builds(
    xwiki_Attachment,
    pageVersion=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    size=
        safe_text,
    author=
        safe_text,
    pageId=
        safe_text,
    version=
        safe_text,
    date=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    name=
        safe_text,
    mimeType=
        safe_text,
    authorName=
        safe_text,
    id=
        safe_text
)

@given(instance=PageSummary_strategy)
@settings(max_examples=50)
def test_pagesummary_instantiation(instance):
    assert isinstance(instance, PageSummary)

@given(instance=ObjectSummary_strategy)
@settings(max_examples=50)
def test_objectsummary_instantiation(instance):
    assert isinstance(instance, ObjectSummary)

@given(instance=xwiki_LinkCollection_strategy)
@settings(max_examples=50)
def test_xwiki_linkcollection_instantiation(instance):
    assert isinstance(instance, xwiki_LinkCollection)

@given(instance=xwiki_Link_strategy)
@settings(max_examples=50)
def test_xwiki_link_instantiation(instance):
    assert isinstance(instance, xwiki_Link)



@given(instance=xwiki_Link_strategy)
def test_xwiki_link_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=xwiki_Link_strategy)
def test_xwiki_link_hrefLang_setter(instance):
    original = instance.hrefLang
    instance.hrefLang = original
    assert instance.hrefLang == original



@given(instance=xwiki_Link_strategy)
def test_xwiki_link_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xwiki_Link_strategy)
def test_xwiki_link_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original

@given(instance=xwiki_Page_strategy)
@settings(max_examples=50)
def test_xwiki_page_instantiation(instance):
    assert isinstance(instance, xwiki_Page)



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_majorVersion_setter(instance):
    original = instance.majorVersion
    instance.majorVersion = original
    assert instance.majorVersion == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_creatorName_setter(instance):
    original = instance.creatorName
    instance.creatorName = original
    assert instance.creatorName == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_modifierName_setter(instance):
    original = instance.modifierName
    instance.modifierName = original
    assert instance.modifierName == original



@given(instance=xwiki_Page_strategy)
def test_xwiki_page_minorVersion_setter(instance):
    original = instance.minorVersion
    instance.minorVersion = original
    assert instance.minorVersion == original

@given(instance=xwiki_Object_strategy)
@settings(max_examples=50)
def test_xwiki_object_instantiation(instance):
    assert isinstance(instance, xwiki_Object)

@given(instance=xwiki_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xwiki_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xwiki_EStringToStringMapEntry)

@given(instance=xwiki_DocumentRoot_strategy)
@settings(max_examples=50)
def test_xwiki_documentroot_instantiation(instance):
    assert isinstance(instance, xwiki_DocumentRoot)



@given(instance=xwiki_DocumentRoot_strategy)
def test_xwiki_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=LinkCollection_strategy)
@settings(max_examples=50)
def test_linkcollection_instantiation(instance):
    assert isinstance(instance, LinkCollection)

@given(instance=xwiki_Syntaxes_strategy)
@settings(max_examples=50)
def test_xwiki_syntaxes_instantiation(instance):
    assert isinstance(instance, xwiki_Syntaxes)



@given(instance=xwiki_Syntaxes_strategy)
def test_xwiki_syntaxes_syntax_setter(instance):
    original = instance.syntax
    instance.syntax = original
    assert instance.syntax == original

@given(instance=xwiki_PageSummary_strategy)
@settings(max_examples=50)
def test_xwiki_pagesummary_instantiation(instance):
    assert isinstance(instance, xwiki_PageSummary)



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_PageSummary_strategy)
def test_xwiki_pagesummary_syntax_setter(instance):
    original = instance.syntax
    instance.syntax = original
    assert instance.syntax == original

@given(instance=xwiki_SearchResult_strategy)
@settings(max_examples=50)
def test_xwiki_searchresult_instantiation(instance):
    assert isinstance(instance, xwiki_SearchResult)



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_objectNumber_setter(instance):
    original = instance.objectNumber
    instance.objectNumber = original
    assert instance.objectNumber == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_pageName_setter(instance):
    original = instance.pageName
    instance.pageName = original
    assert instance.pageName == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=xwiki_SearchResult_strategy)
def test_xwiki_searchresult_pageFullName_setter(instance):
    original = instance.pageFullName
    instance.pageFullName = original
    assert instance.pageFullName == original

@given(instance=xwiki_PagesType_strategy)
@settings(max_examples=50)
def test_xwiki_pagestype_instantiation(instance):
    assert isinstance(instance, xwiki_PagesType)

@given(instance=xwiki_Translation_strategy)
@settings(max_examples=50)
def test_xwiki_translation_instantiation(instance):
    assert isinstance(instance, xwiki_Translation)



@given(instance=xwiki_Translation_strategy)
def test_xwiki_translation_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=xwiki_SpacesType_strategy)
@settings(max_examples=50)
def test_xwiki_spacestype_instantiation(instance):
    assert isinstance(instance, xwiki_SpacesType)

@given(instance=xwiki_Attribute_strategy)
@settings(max_examples=50)
def test_xwiki_attribute_instantiation(instance):
    assert isinstance(instance, xwiki_Attribute)



@given(instance=xwiki_Attribute_strategy)
def test_xwiki_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xwiki_Attribute_strategy)
def test_xwiki_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki_ObjectsType_strategy)
@settings(max_examples=50)
def test_xwiki_objectstype_instantiation(instance):
    assert isinstance(instance, xwiki_ObjectsType)

@given(instance=xwiki_PropertiesType_strategy)
@settings(max_examples=50)
def test_xwiki_propertiestype_instantiation(instance):
    assert isinstance(instance, xwiki_PropertiesType)

@given(instance=xwiki_ClassesType_strategy)
@settings(max_examples=50)
def test_xwiki_classestype_instantiation(instance):
    assert isinstance(instance, xwiki_ClassesType)

@given(instance=xwiki_Comment_strategy)
@settings(max_examples=50)
def test_xwiki_comment_instantiation(instance):
    assert isinstance(instance, xwiki_Comment)



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_replyTo_setter(instance):
    original = instance.replyTo
    instance.replyTo = original
    assert instance.replyTo == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_Comment_strategy)
def test_xwiki_comment_highlight_setter(instance):
    original = instance.highlight
    instance.highlight = original
    assert instance.highlight == original

@given(instance=xwiki_AttachmentsType_strategy)
@settings(max_examples=50)
def test_xwiki_attachmentstype_instantiation(instance):
    assert isinstance(instance, xwiki_AttachmentsType)

@given(instance=xwiki_XWiki_strategy)
@settings(max_examples=50)
def test_xwiki_xwiki_instantiation(instance):
    assert isinstance(instance, xwiki_XWiki)



@given(instance=xwiki_XWiki_strategy)
def test_xwiki_xwiki_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xwiki_CommentsType_strategy)
@settings(max_examples=50)
def test_xwiki_commentstype_instantiation(instance):
    assert isinstance(instance, xwiki_CommentsType)

@given(instance=xwiki_HistorySummary_strategy)
@settings(max_examples=50)
def test_xwiki_historysummary_instantiation(instance):
    assert isinstance(instance, xwiki_HistorySummary)



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_modifierName_setter(instance):
    original = instance.modifierName
    instance.modifierName = original
    assert instance.modifierName == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_minorVersion_setter(instance):
    original = instance.minorVersion
    instance.minorVersion = original
    assert instance.minorVersion == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_majorVersion_setter(instance):
    original = instance.majorVersion
    instance.majorVersion = original
    assert instance.majorVersion == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_HistorySummary_strategy)
def test_xwiki_historysummary_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=xwiki_Class_strategy)
@settings(max_examples=50)
def test_xwiki_class_instantiation(instance):
    assert isinstance(instance, xwiki_Class)



@given(instance=xwiki_Class_strategy)
def test_xwiki_class_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_Class_strategy)
def test_xwiki_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki_Property_strategy)
@settings(max_examples=50)
def test_xwiki_property_instantiation(instance):
    assert isinstance(instance, xwiki_Property)



@given(instance=xwiki_Property_strategy)
def test_xwiki_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Property_strategy)
def test_xwiki_property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xwiki_Property_strategy)
def test_xwiki_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xwiki_Wiki_strategy)
@settings(max_examples=50)
def test_xwiki_wiki_instantiation(instance):
    assert isinstance(instance, xwiki_Wiki)



@given(instance=xwiki_Wiki_strategy)
def test_xwiki_wiki_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=xwiki_Wiki_strategy)
def test_xwiki_wiki_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xwiki_Wiki_strategy)
def test_xwiki_wiki_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Wiki_strategy)
def test_xwiki_wiki_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki_WikisType_strategy)
@settings(max_examples=50)
def test_xwiki_wikistype_instantiation(instance):
    assert isinstance(instance, xwiki_WikisType)

@given(instance=xwiki_Translations_strategy)
@settings(max_examples=50)
def test_xwiki_translations_instantiation(instance):
    assert isinstance(instance, xwiki_Translations)



@given(instance=xwiki_Translations_strategy)
def test_xwiki_translations_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=xwiki_HistoryType_strategy)
@settings(max_examples=50)
def test_xwiki_historytype_instantiation(instance):
    assert isinstance(instance, xwiki_HistoryType)

@given(instance=xwiki_ObjectSummary_strategy)
@settings(max_examples=50)
def test_xwiki_objectsummary_instantiation(instance):
    assert isinstance(instance, xwiki_ObjectSummary)



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_pageVersion_setter(instance):
    original = instance.pageVersion
    instance.pageVersion = original
    assert instance.pageVersion == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_pageAuthorName_setter(instance):
    original = instance.pageAuthorName
    instance.pageAuthorName = original
    assert instance.pageAuthorName == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_pageAuthor_setter(instance):
    original = instance.pageAuthor
    instance.pageAuthor = original
    assert instance.pageAuthor == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_pageName_setter(instance):
    original = instance.pageName
    instance.pageName = original
    assert instance.pageName == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_xwiki_objectsummary_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=xwiki_SearchResultsType_strategy)
@settings(max_examples=50)
def test_xwiki_searchresultstype_instantiation(instance):
    assert isinstance(instance, xwiki_SearchResultsType)



@given(instance=xwiki_SearchResultsType_strategy)
def test_xwiki_searchresultstype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=xwiki_TagsType_strategy)
@settings(max_examples=50)
def test_xwiki_tagstype_instantiation(instance):
    assert isinstance(instance, xwiki_TagsType)

@given(instance=xwiki_Tag_strategy)
@settings(max_examples=50)
def test_xwiki_tag_instantiation(instance):
    assert isinstance(instance, xwiki_Tag)



@given(instance=xwiki_Tag_strategy)
def test_xwiki_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki_Space_strategy)
@settings(max_examples=50)
def test_xwiki_space_instantiation(instance):
    assert isinstance(instance, xwiki_Space)



@given(instance=xwiki_Space_strategy)
def test_xwiki_space_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_Space_strategy)
def test_xwiki_space_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Space_strategy)
def test_xwiki_space_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original



@given(instance=xwiki_Space_strategy)
def test_xwiki_space_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_Space_strategy)
def test_xwiki_space_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original



@given(instance=xwiki_Space_strategy)
def test_xwiki_space_home_setter(instance):
    original = instance.home
    instance.home = original
    assert instance.home == original

@given(instance=xwiki_Attachment_strategy)
@settings(max_examples=50)
def test_xwiki_attachment_instantiation(instance):
    assert isinstance(instance, xwiki_Attachment)



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_pageVersion_setter(instance):
    original = instance.pageVersion
    instance.pageVersion = original
    assert instance.pageVersion == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_Attachment_strategy)
def test_xwiki_attachment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
